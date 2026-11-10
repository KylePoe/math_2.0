"""Score each crawled post with Claude along the rubric in rubric.py, then build the dataset.

Inputs:   data/posts.jsonl              (from crawl.py)
Outputs:  data/scores.jsonl             raw annotations, one per post (append-only cache)
          data/dataset.csv              flat table: metadata + scores, no full text
          data/dataset.jsonl            same rows plus the cleaned text, for word clouds / EDA

Results are cached by (post id, prompt version). Re-running only scores posts that are new
or whose rubric/model/effort changed. Use --rebuild to regenerate the dataset files only.

Usage:
  export ANTHROPIC_API_KEY=...
  export ANTHROPIC_WORKSPACE_ID=...      # only if your key is not scoped to a workspace
  python score.py --limit 3             # try a few posts first
  python score.py                        # score everything
  python score.py --effort high          # deeper reading (costs more; re-scores everything)
  python score.py --rebuild              # just rebuild dataset.csv / dataset.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic
import pandas as pd
from pydantic import ValidationError

import rubric

DATA = Path(__file__).parent / "data"
POSTS = DATA / "posts.jsonl"
SCORES = DATA / "scores.jsonl"

MODEL = "claude-opus-5-5"
# $ per million tokens, for the running cost estimate printed at the end.
PRICE = {"claude-opus-5-5": (4.00, 20.00)}

_write_lock = threading.Lock()


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _api_error_message(e: anthropic.APIStatusError) -> str:
    """The human-readable message inside the API's error body, falling back to the full text."""
    body = e.body if isinstance(e.body, dict) else {}
    return (body.get("error") or {}).get("message") or e.message


def score_post(client: anthropic.Anthropic, post: dict, model: str, effort: str) -> dict:
    """One API call -> validated annotation dict (or an error record)."""
    base = {"id": post["id"], "prompt_version": rubric.prompt_version(model, effort),
            "model_requested": model, "effort": effort}
    try:
        resp = client.beta.messages.create(
            model=model,
            max_tokens=16000,
            # Server-side refusal fallback: if a safety classifier declines, the API re-runs
            # the request on a fallback model within the same call.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            output_config={
                "effort": effort,
                "format": {"type": "json_schema", "schema": rubric.OUTPUT_SCHEMA},
            },
            system=[{"type": "text", "text": rubric.SYSTEM_PROMPT,
                     "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": rubric.build_user_message(post)}],
        )
    except anthropic.APIStatusError as e:
        return {**base, "error": f"api_{e.status_code}: {_api_error_message(e)}"}
    except anthropic.APIConnectionError as e:
        return {**base, "error": f"connection: {e}"}

    u = resp.usage
    meta = {
        "model_served": resp.model,
        "request_id": resp._request_id,
        "stop_reason": resp.stop_reason,
        "input_tokens": u.input_tokens,
        "output_tokens": u.output_tokens,
        "cache_read_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
        "cache_write_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
    }
    if resp.stop_reason != "end_turn":
        return {**base, **meta, "error": f"stop_reason={resp.stop_reason}"}

    text = next((b.text for b in resp.content if b.type == "text"), "")
    try:
        parsed = rubric.PostScore.model_validate_json(text)
    except ValidationError as e:
        return {**base, **meta, "error": f"validation: {e}", "raw": text}

    out = parsed.model_dump()
    for d in out["dimensions"].values():  # clamp; schema can't enforce numeric bounds
        d["score"] = max(-1.0, min(1.0, float(d["score"])))
    out["emotional_tone"]["score"] = max(-1.0, min(1.0, float(out["emotional_tone"]["score"])))
    return {**base, **meta, "annotation": out}


def run_scoring(args) -> None:
    posts = load_jsonl(POSTS)
    if not posts:
        sys.exit(f"{POSTS} not found or empty - run crawl.py first.")
    if args.ids:
        wanted = {int(x) for x in args.ids.split(",")}
        posts = [p for p in posts if p["id"] in wanted]

    version = rubric.prompt_version(args.model, args.effort)
    done = {r["id"] for r in load_jsonl(SCORES)
            if r.get("prompt_version") == version and "annotation" in r}
    todo = [p for p in posts if args.force or p["id"] not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"Prompt version {version}: {len(done)} cached, {len(todo)} to score "
          f"(model={args.model}, effort={args.effort}, workers={args.workers})")
    if not todo:
        return

    # Keys not scoped to a workspace must name one per request.
    workspace = os.environ.get("ANTHROPIC_WORKSPACE_ID")
    headers = {"anthropic-workspace-id": workspace} if workspace else None
    client = anthropic.Anthropic(max_retries=6, default_headers=headers)
    in_tok = out_tok = 0
    n_err = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(score_post, client, p, args.model, args.effort): p for p in todo}
        for i, fut in enumerate(as_completed(futs), 1):
            p, rec = futs[fut], fut.result()
            with _write_lock, SCORES.open("a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            in_tok += rec.get("input_tokens", 0)
            out_tok += rec.get("output_tokens", 0)
            if "error" in rec:
                n_err += 1
                status = f"ERROR {rec['error'][:220]}"
            else:
                a = rec["annotation"]
                status = (f"overall={a['dimensions']['overall']['score']:+.2f} "
                          f"{a['post_type']}, {a['author']['career_stage']}")
            print(f"[{i}/{len(todo)}] {p['title'][:55]:<55} {status}", flush=True)

    pin, pout = PRICE.get(args.model, (0, 0))
    cost = in_tok / 1e6 * pin + out_tok / 1e6 * pout
    print(f"\nDone in {time.time() - t0:.0f}s. {n_err} errors. "
          f"Tokens: {in_tok:,} in / {out_tok:,} out  (~${cost:.2f} at list price)")


def build_dataset(model: str, effort: str) -> None:
    posts = {p["id"]: p for p in load_jsonl(POSTS)}
    version = rubric.prompt_version(model, effort)
    latest: dict[int, dict] = {}
    for r in load_jsonl(SCORES):  # last successful annotation per post for this version wins
        if r.get("prompt_version") == version and "annotation" in r:
            latest[r["id"]] = r

    rows = []
    for pid, post in posts.items():
        row = {
            "id": pid, "url": post["url"], "title": post["title"],
            "published": post["published"][:10], "received": post["received_date"],
            "revised": post.get("revised_date"),
            "categories": "; ".join(post["categories"]), "tags": "; ".join(post["tags"]),
            "contributors": "; ".join(post["contributors"]), "author_line": post["author_line"],
            "word_count": post["word_count"], "has_ai_statement": bool(post["ai_statements"]),
            "scored": pid in latest,
        }
        if pid in latest:
            a = latest[pid]["annotation"]
            row.update({
                "post_type": a["post_type"], "relevance": a["ai_in_math_relevance"],
                "summary": a["summary"],
            })
            for k, d in a["dimensions"].items():
                row[f"{k}"] = d["score"] if d["addressed"] else None
                row[f"{k}_evidence"] = d["evidence"]
            row["tone"] = a["emotional_tone"]["score"]
            row.update({f"author_{k}": v for k, v in a["author"].items()})
            row.update({f"ai_{k}": v for k, v in a["ai_use"].items()})
            row["model_served"] = latest[pid].get("model_served")
        rows.append(row)

    df = pd.DataFrame(rows).sort_values("published")
    df.to_csv(DATA / "dataset.csv", index=False)
    with (DATA / "dataset.jsonl").open("w") as f:
        for row in df.to_dict(orient="records"):
            row["text"] = posts[row["id"]]["text"]
            f.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
    print(f"Wrote {len(df)} rows ({int(df['scored'].sum())} scored) to "
          f"{DATA / 'dataset.csv'} and dataset.jsonl")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--limit", type=int, help="score at most N uncached posts")
    ap.add_argument("--ids", help="comma-separated post ids to score")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--force", action="store_true", help="re-score even if cached")
    ap.add_argument("--rebuild", action="store_true", help="only rebuild dataset files")
    args = ap.parse_args()

    if not args.rebuild:
        run_scoring(args)
    build_dataset(args.model, args.effort)


if __name__ == "__main__":
    main()
