"""Crawl every post on proofsandprompts.com via the WordPress REST API.

Outputs (in data/):
  raw/posts_api.json   full API responses, for reproducibility
  posts.jsonl          one cleaned record per post (metadata + main text)

Usage:
  python crawl.py            # fetch everything
  python crawl.py --limit 5  # quick test
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = "https://proofsandprompts.com/wp-json/wp/v2"
DATA = Path(__file__).parent / "data"
HEADERS = {"User-Agent": "math-2.0-research-crawler (academic text analysis)"}
DELAY_S = 1.0  # politeness delay between API requests

session = requests.Session()
session.headers.update(HEADERS)


def get_all(endpoint: str, params: dict | None = None, limit: int | None = None) -> list[dict]:
    """Page through a WP REST collection endpoint."""
    out: list[dict] = []
    page = 1
    while True:
        p = {"per_page": 100, "page": page, **(params or {})}
        r = session.get(f"{BASE}/{endpoint}", params=p, timeout=60)
        if r.status_code == 400 and page > 1:  # past the last page
            break
        r.raise_for_status()
        batch = r.json()
        out.extend(batch)
        total_pages = int(r.headers.get("X-WP-TotalPages", 1))
        if page >= total_pages or not batch or (limit and len(out) >= limit):
            break
        page += 1
        time.sleep(DELAY_S)
    return out[:limit] if limit else out


def term_map(endpoint: str) -> dict[int, str]:
    return {t["id"]: html.unescape(t["name"]) for t in get_all(endpoint, {"_fields": "id,name"})}


BLOCK_TAGS = ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre", "figcaption", "td"]
RECEIVED_RE = re.compile(r"^\s*Received\b", re.I)  # footer: "Received 2 October 2026, revised 9 November 2026."
_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
_DATE_RE = re.compile(
    rf"(?P<d1>\d{{1,2}})\s+(?P<m1>{_MONTHS})(?:\s+(?P<y1>\d{{4}}))?"
    rf"|(?P<m2>{_MONTHS})\s+(?P<d2>\d{{1,2}})(?:,?\s+(?P<y2>\d{{4}}))?"
)


def _parse_date(s: str, default_year: int) -> str | None:
    m = _DATE_RE.search(s)
    if not m:
        return None
    day = m.group("d1") or m.group("d2")
    month = m.group("m1") or m.group("m2")
    year = m.group("y1") or m.group("y2") or default_year
    return datetime.strptime(f"{day} {month} {year}", "%d %B %Y").date().isoformat()


def parse_footer(block: str, default_year: int) -> tuple[str | None, str | None]:
    """'Received 2 October 2026, revised 9 November 2026.' -> (received, revised) ISO dates."""
    parts = re.split(r"\brevised\b", block, maxsplit=1, flags=re.I)
    received = _parse_date(parts[0], default_year)
    revised = _parse_date(parts[1], default_year) if len(parts) > 1 else None
    return received, revised
# Explicit authorial disclosures only ("AI use: none", "AI Disclosure: ...", "Declaration of AI use: ...").
AI_STATEMENT_RE = re.compile(
    r"\b(AI|LLM|generative AI)[- ]?(use|usage|disclosure|statement|declaration)\s*:"
    r"|\b(declaration|statement|disclosure) of (AI|LLM|generative AI) use"
    r"|\bno AI (was|has been) used\b",
    re.I,
)
BOILERPLATE_MIN_POSTS = 3  # a paragraph appearing verbatim in this many posts is site boilerplate


def _norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def parse_content(content_html: str, contributor_names: list[str], published_year: int) -> dict:
    """Split a post body into author line, main text, AI-use statement, and received date."""
    soup = BeautifulSoup(content_html, "html.parser")

    author_line_el = soup.select_one("p.author-line")
    author_line = author_line_el.get_text(" ", strip=True) if author_line_el else ""
    if author_line_el:
        author_line_el.decompose()

    for el in soup.select("script, style, .sharedaddy, .jp-relatedposts, .wp-block-jetpack-subscriptions"):
        el.decompose()

    # Collect block-level text, skipping nested blocks already covered by a parent (e.g. <p> inside <li>).
    blocks: list[str] = []
    for el in soup.find_all(BLOCK_TAGS):
        if el.find_parent(BLOCK_TAGS):
            continue
        txt = re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()
        if txt:
            blocks.append(txt)

    # A few posts lack the author-line class; their first paragraph names the contributor instead.
    if not author_line and blocks and len(blocks[0]) < 400:
        first = _norm(blocks[0])
        if any(_norm(n)[:20] in first for n in contributor_names if n):
            author_line = blocks.pop(0)

    received_date = revised_date = None
    ai_statements: list[str] = []
    body: list[str] = []
    for b in blocks:
        if RECEIVED_RE.match(b) and len(b) < 300:
            received_date, revised_date = parse_footer(b, published_year)
            continue  # footer, not main text
        if AI_STATEMENT_RE.search(b) and len(b) < 600:
            ai_statements.append(b)
        body.append(b)

    return {
        "author_line": author_line,
        "blocks": body,
        "received_date": received_date,
        "revised_date": revised_date,
        "ai_statements": ai_statements,
    }


def strip_boilerplate(records: list[dict]) -> None:
    """Remove paragraphs repeated verbatim across many posts (series banners, CTAs); build final text."""
    counts = Counter(b for r in records for b in set(r["blocks"]))
    # Length floor keeps ordinary repeated headings ("Conclusion", "References") in the text.
    boiler = {b for b, n in counts.items() if n >= BOILERPLATE_MIN_POSTS and len(b) >= 40}
    for r in records:
        blocks = r.pop("blocks")
        r["boilerplate"] = [b for b in blocks if b in boiler]
        r["ai_statements"] = [s for s in r["ai_statements"] if s not in boiler]
        r["text"] = "\n\n".join(b for b in blocks if b not in boiler)
        r["word_count"] = len(r["text"].split())
    if boiler:
        print(f"  stripped {len(boiler)} boilerplate paragraph(s), e.g.: {next(iter(boiler))[:90]!r}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="only fetch the N most recent posts")
    args = ap.parse_args()

    (DATA / "raw").mkdir(parents=True, exist_ok=True)

    print("Fetching taxonomies...")
    categories = term_map("categories")
    tags = term_map("tags")
    contributors = term_map("contributor")

    print("Fetching posts...")
    posts = get_all("posts", {"orderby": "date", "order": "desc"}, limit=args.limit)
    (DATA / "raw" / "posts_api.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1))

    records = []
    for p in posts:
        names = [contributors.get(c, "") for c in p.get("contributor", [])]
        parsed = parse_content(p["content"]["rendered"], names, int(p["date"][:4]))
        records.append({
            "id": p["id"],
            "url": p["link"],
            "slug": p["slug"],
            "title": html.unescape(BeautifulSoup(p["title"]["rendered"], "html.parser").get_text()),
            "published": p["date"],
            "modified": p["modified"],
            "categories": [categories.get(c, str(c)) for c in p.get("categories", [])],
            "tags": [tags.get(t, str(t)) for t in p.get("tags", [])],
            "contributors": [contributors.get(c, str(c)) for c in p.get("contributor", [])],
            **parsed,
        })
    strip_boilerplate(records)

    out = DATA / "posts.jsonl"
    with out.open("w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    n_recv = sum(r["received_date"] is not None for r in records)
    n_author = sum(bool(r["author_line"]) for r in records)
    n_ai = sum(bool(r["ai_statements"]) for r in records)
    print(f"Wrote {len(records)} posts to {out}")
    print(f"  with author line: {n_author}, with received date: {n_recv}, with AI-use statement: {n_ai}")
    print(f"  words: median {sorted(r['word_count'] for r in records)[len(records)//2]}, "
          f"total {sum(r['word_count'] for r in records):,}")


if __name__ == "__main__":
    main()
