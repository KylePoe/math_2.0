"""Cluster posts on (capability, valence) and build per-cluster distinctive-word clouds.

Outputs:
  data/clusters.csv               one row per post in the analysis set, with its cluster
  data/wordcloud_terms.csv        distinctive terms per cluster (the word-cloud data)
  figures/08_clusters.png         clusters in the capability x valence plane
  figures/09_wordclouds.png       one cloud per cluster, side by side
  figures/09_wordcloud_<k>.png    each cloud on its own, for slides

Usage:
  python cluster.py          # k=3 (best silhouette and bootstrap stability)
  python cluster.py --k 4
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler
from wordcloud import WordCloud

import eda
from eda import FIG, MARKERS, MUTED, ROOT, SERIES, SURFACE, TEXT, TEXT_2, plt, section

FEATURES = ["capability", "valence"]
MIN_POSTS = 5       # a term must appear in at least this many posts of the cluster
MIN_Z = 2.0         # and be over-represented with z >= this (one-sided p < ~0.025)
MAX_WORDS = 60      # words per cloud

EXTRA_STOP = {
    # contractions / filler common in essays
    "don't", "doesn't", "isn't", "aren't", "can't", "won't", "it's", "i'm", "i've", "i'd", "i'll",
    "we're", "we've", "they're", "that's", "there's", "let's", "you're", "didn't", "wasn't",
    "also", "just", "like", "would", "could", "might", "may", "must", "shall", "one", "ones",
    "even", "much", "many", "really", "quite", "rather", "perhaps", "maybe", "still", "yet",
    "way", "ways", "thing", "things", "something", "anything", "lot", "lots", "kind", "sort",
    "say", "says", "said", "think", "make", "makes", "made", "get", "gets", "got", "going",
    "use", "used", "using", "want", "need", "know", "see", "seems", "seem", "take", "given",
    "time", "times", "new", "good", "well", "far", "able", "us", "e.g", "i.e", "etc", "will",
}
STOP = set(ENGLISH_STOP_WORDS) | EXTRA_STOP

# Display filter, chosen by hand after reading each term's in-context example: words that are
# statistically over-represented but name no topic, value, or stance (generic verbs, adverbs,
# quantities, time words, discourse nouns). Applied after scoring, so statistics and bigrams are
# unchanged; removed terms are written to data/wordcloud_terms_removed.csv for transparency.
# Kept on purpose despite looking generic: act, urgent, honest, stake, race, debate (the
# call-to-action theme), expensive (cost), confusion (the value of struggle).
GENERIC = {
    # verbs
    "goes", "continues", "reads", "holds", "finds", "comes", "putting", "turned", "told", "did",
    "left", "leave", "choose", "wait", "face", "hoped", "lies", "provide", "starting", "propose",
    "addressed", "influenced", "insist", "guided", "guiding", "break", "surprise", "experienced",
    "connect", "raise", "predict", "considered",
    # adverbs
    "immensely", "correctly", "completely", "frequently", "similarly", "extremely", "ultimately",
    "regardless", "effectively", "apparent", "inside", "right",
    # sizes, quantities, time
    "small", "biggest", "proportion", "longer", "recent", "today", "year", "years", "decade",
    "long run", "long term", "long-standing", "degree", "rapid",
    # generic nouns and adjectives
    "kinds", "general", "order", "case", "scope", "parts", "fixed", "narrow", "distance", "head",
    "light", "situation", "purposes", "grounds", "appearance", "unlike", "careful", "lack", "dead",
    "posts", "comments", "input", "object", "behavior", "connection", "texts", "important",
    "people", "priority", "popular", "domains", "fault", "nature", "arguments", "role",
    "controlled", "creation", "friends", "children", "discipline", "endeavour", "blog post",
    "lines", "problems", "landscape",
}
TOKEN_RE = re.compile(r"[a-z][a-z'\-]*[a-z]|[a-z]")


def tokenize(text: str) -> list[str]:
    text = text.lower().replace("’", "'").replace("‘", "'").replace("–", " ").replace("—", " ")
    toks = [t[:-2] if t.endswith("'s") else t for t in TOKEN_RE.findall(text)]
    return [t for t in toks if len(t) > 1 or t == "ai"]


def post_terms(text: str) -> set[str]:
    """Set of unigrams and bigrams (neither word a stopword) present in a post."""
    toks = tokenize(text)
    keep = [t if t not in STOP and "'" not in t else None for t in toks]  # contractions are function words
    uni = {t for t in keep if t}
    bi = {f"{a} {b}" for a, b in zip(keep, keep[1:]) if a and b and a != b}
    return uni | bi


# ---------------------------------------------------------------------------
def fit_clusters(a: pd.DataFrame, k: int) -> tuple[np.ndarray, np.ndarray, dict]:
    X = a[FEATURES].to_numpy()
    sc = StandardScaler().fit(X)
    Z = sc.transform(X)
    km = KMeans(k, n_init=50, random_state=0).fit(Z)
    rng = np.random.default_rng(0)
    aris = []
    for b in range(200):
        idx = rng.choice(len(Z), len(Z))
        aris.append(adjusted_rand_score(km.labels_, KMeans(k, n_init=10, random_state=b).fit(Z[idx]).predict(Z)))
    stats = {"silhouette": silhouette_score(Z, km.labels_), "ari_median": np.median(aris),
             "ari_p5": np.percentile(aris, 5)}
    return km.labels_, sc.inverse_transform(km.cluster_centers_), stats


def name_cluster(cap: float, val: float) -> str:
    c = "AI capable" if cap >= 0.4 else "AI doubted"
    v = "positive" if val > 0.15 else "negative" if val < -0.15 else "mixed"
    return f"{c}, {v}"


def distinctive_terms(texts: list[str], labels: np.ndarray) -> pd.DataFrame:
    """Per cluster vs the rest: log odds ratio of the share of posts containing each term.

    For each term, a 2x2 table (in cluster / elsewhere) x (contains / doesn't), with 0.5 added
    to every cell. z = log OR / SE ranks terms by how reliably they are over-represented.
    """
    doc_terms = [post_terms(t) for t in texts]
    rows = []
    for c in np.unique(labels):
        inside = [d for d, l in zip(doc_terms, labels) if l == c]
        outside = [d for d, l in zip(doc_terms, labels) if l != c]
        df_in, df_out = Counter(t for d in inside for t in d), Counter(t for d in outside for t in d)
        n_in, n_out = len(inside), len(outside)
        for term, a in df_in.items():
            if a < MIN_POSTS:
                continue
            b, cc = n_in - a, df_out.get(term, 0)
            d = n_out - cc
            a_, b_, c_, d_ = a + 0.5, b + 0.5, cc + 0.5, d + 0.5
            lor = np.log(a_ * d_ / (b_ * c_))
            se = np.sqrt(1 / a_ + 1 / b_ + 1 / c_ + 1 / d_)
            rows.append({"cluster": c, "term": term, "z": lor / se, "log_odds_ratio": lor,
                         "posts_in_cluster": a, "pct_in_cluster": a / n_in,
                         "pct_elsewhere": cc / n_out})
    out = pd.DataFrame(rows)
    out["p_one_sided"] = norm.sf(out["z"])
    return out[out["z"] >= MIN_Z].sort_values(["cluster", "z"], ascending=[True, False])


def add_examples(terms: pd.DataFrame, texts: list[str], titles: list[str], labels: np.ndarray) -> pd.DataFrame:
    """Attach one short in-context snippet per term (from a post in that cluster) for checking
    what a word actually refers to before it goes on a slide."""
    examples, sources = [], []
    for _, r in terms.iterrows():
        pat = re.compile(r"\b" + r"\W+".join(map(re.escape, r["term"].split())) + r"\b", re.I)
        snippet = source = ""
        for text, title, lab in zip(texts, titles, labels):
            if lab != r["cluster"]:
                continue
            m = pat.search(text.replace("’", "'"))
            if m:
                lo, hi = max(0, m.start() - 70), min(len(text), m.end() + 70)
                snippet = ("…" if lo else "") + re.sub(r"\s+", " ", text[lo:hi]) + ("…" if hi < len(text) else "")
                source = title
                break
        examples.append(snippet)
        sources.append(source)
    return terms.assign(example=examples, example_post=sources)


def drop_redundant(terms: pd.DataFrame) -> pd.DataFrame:
    """Within a cluster, drop a unigram when a distinctive bigram containing it occurs in at
    least 75% of the posts the unigram does (e.g. keep 'peer review', drop 'peer')."""
    keep = []
    for c, g in terms.groupby("cluster", sort=False):
        bigrams = g[g["term"].str.contains(" ")]
        for _, r in g.iterrows():
            if " " not in r["term"]:
                cover = bigrams[
                                bigrams["term"].str.split().apply(lambda w: r["term"] in w) &
                                (bigrams["posts_in_cluster"] >= 0.75 * r["posts_in_cluster"])]
                if len(cover):
                    continue
            keep.append(r)
    return pd.DataFrame(keep)


# ---------------------------------------------------------------------------
# Cluster plot sized for the talk slide: it sits left of the 2:3 word-cloud stack, in a box
# about 5.1 cm wide x 5.85 cm tall. No title or legend (the slide titles it, and colours match
# the clouds); each centre is labelled directly with its name, size, and coordinates.
CLUSTER_FIGSIZE = (4.6, 5.275)  # inches, width:height = 0.872; saved without tight cropping
CLUSTER_XLIM, CLUSTER_YLIM = (-0.62, 1.08), (-1.36, 0.97)
# Where each centre's label goes (data coords, horizontal alignment); chosen to sit in empty
# corners of the plot. Clusters with other names fall back to a label beside the centre.
LABEL_SPOTS = {
    "AI capable, positive": (-0.58, 0.79, "left"),
    "AI doubted, negative": (-0.58, -1.15, "left"),
    "AI capable, negative": (1.05, -1.15, "right"),
}


def fig_clusters(a: pd.DataFrame, centers: np.ndarray, names: list[str], order: list[int]) -> None:
    fig = plt.figure(figsize=CLUSTER_FIGSIZE)
    ax = fig.add_axes([0.19, 0.095, 0.79, 0.895])
    rng = np.random.default_rng(2)
    jit = lambda n: rng.uniform(-0.02, 0.02, n)  # scores sit on a 0.05 grid; separate overlaps
    ax.axhline(0, color=MUTED, lw=1, zorder=1)
    ax.axvline(0, color=MUTED, lw=1, zorder=1)
    for slot, c in enumerate(order):
        s = a[a["cluster"] == c]
        color, marker = SERIES[slot % len(SERIES)], MARKERS[slot % len(MARKERS)]
        ax.scatter(s["capability"] + jit(len(s)), s["valence"] + jit(len(s)), s=30,
                   color=color, marker=marker, edgecolor=SURFACE, lw=0.9, alpha=0.9, zorder=2)
        cx, cy = centers[c]
        ax.scatter(cx, cy, s=220, color=color, marker=marker, edgecolor=TEXT, lw=1.4, zorder=4)
        label = (f"$\\bf{{{names[c].replace(' ', '~')}}}$\n{len(s)} essays\n"
                 f"centre ({cx:+.2f}, {cy:+.2f})").replace("-", "−")
        if names[c] in LABEL_SPOTS:
            tx, ty, ha = LABEL_SPOTS[names[c]]
            ax.annotate(label, (cx, cy), xytext=(tx, ty), textcoords="data", ha=ha, va="center",
                        fontsize=8.5, color=TEXT, zorder=5, linespacing=1.3,
                        bbox=dict(boxstyle="round,pad=0.3", fc=SURFACE, ec=color, lw=1),
                        arrowprops=dict(arrowstyle="-", color=color, lw=1.2, shrinkB=9))
        else:
            ax.annotate(label, (cx, cy), xytext=(10, 10), textcoords="offset points", fontsize=8.5,
                        color=TEXT, zorder=5, bbox=dict(boxstyle="round,pad=0.3", fc=SURFACE, ec=color))
    ax.set_xlim(*CLUSTER_XLIM)
    ax.set_ylim(*CLUSTER_YLIM)
    ax.set_xticks([-0.5, 0, 0.5, 1])
    ax.set_yticks([-1, -0.5, 0, 0.5])
    ax.set_xlabel("capability: how useful AI is for mathematics", fontsize=9.5)
    ax.set_ylabel("valence: mean of understanding, community,\nadoption, and overall", fontsize=9.5)
    with plt.rc_context({"savefig.bbox": "standard"}):  # keep the exact aspect for the slide
        fig.savefig(FIG / "08_clusters.png", dpi=300)
    plt.close(fig)


def make_cloud(g: pd.DataFrame, color: str, width: int, height: int, max_font: int,
               margin: int = 12) -> WordCloud:
    # relative_scaling=1: font size proportional to z, so size differences mean what they show.
    wc = WordCloud(width=width, height=height, background_color=SURFACE, prefer_horizontal=1.0,
                   max_words=MAX_WORDS, relative_scaling=1.0, max_font_size=max_font,
                   min_font_size=12, margin=margin,
                   color_func=lambda *args, color=color, **kw: color, random_state=0)
    return wc.generate_from_frequencies(dict(zip(g["term"], g["z"])))


# Combined figure: clouds stacked vertically, overall aspect 2 (tall) : 3 (wide).
STACK_FIGSIZE = (12.0, 8.0)   # inches; exact, saved without tight cropping
STACK_DPI = 160


def render_clouds(terms: pd.DataFrame, names: list[str], order: list[int], sizes: dict) -> None:
    for slot, c in enumerate(order):
        g = terms[terms["cluster"] == c].head(MAX_WORDS)
        color = SERIES[slot % len(SERIES)]
        wc = make_cloud(g, color, 900, 620, 96)
        f, ax = plt.subplots(figsize=(9, 6.6))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        ax.set_title(f"{names[c]}  ·  {sizes[c]} posts", loc="left")
        f.text(0.01, 0.01, "Size = how much more often a term appears in this cluster's posts than in "
               "other posts (log-odds z).", fontsize=8, color=TEXT_2)
        f.savefig(FIG / f"09_wordcloud_{slot + 1}_{re.sub(r'[^a-z]+', '_', names[c].lower()).strip('_')}.png")
        plt.close(f)

    # Manual layout in figure fractions so the saved image keeps the exact 2:3 aspect.
    W, H = STACK_FIGSIZE
    fig = plt.figure(figsize=STACK_FIGSIZE)
    top, bottom, left, right = 0.065, 0.045, 0.012, 0.012   # margins (fractions)
    label_h, gap = 0.032, 0.012                              # per-row title band, row gap
    n = len(order)
    row_h = (1 - top - bottom - gap * (n - 1)) / n
    cloud_h = row_h - label_h
    px_w = int((1 - left - right) * W * STACK_DPI)
    px_h = int(cloud_h * H * STACK_DPI)
    fig.text(left, 1 - top / 2, "Words each cluster uses disproportionately often", ha="left",
             va="center", fontsize=13, fontweight="bold", color=TEXT)
    for i, c in enumerate(order):
        y_row_top = 1 - top - i * (row_h + gap)
        g = terms[terms["cluster"] == c].head(MAX_WORDS)
        wc = make_cloud(g, SERIES[i % len(SERIES)], px_w, px_h, max_font=int(px_h * 0.4), margin=22)
        ax = fig.add_axes([left, y_row_top - row_h, 1 - left - right, cloud_h])
        ax.imshow(wc, interpolation="bilinear", aspect="auto")
        ax.axis("off")
        fig.text(left, y_row_top - label_h / 2, f"{names[c]}  ·  {sizes[c]} posts", ha="left",
                 va="center", fontsize=11, fontweight="bold", color=TEXT)
    fig.text(left, bottom / 2, "Size = how much more often the cluster's posts contain the term than "
             f"other posts (log odds ratio z ≥ {MIN_Z:g}). Terms must appear in ≥{MIN_POSTS} of the "
             "cluster's posts; generic words removed.", ha="left", va="center", fontsize=8.5, color=TEXT_2)
    with plt.rc_context({"savefig.bbox": "standard"}):  # eda.py's rcParams crop to "tight"
        fig.savefig(FIG / "09_wordclouds.png", dpi=STACK_DPI)
    plt.close(fig)


def profile(a: pd.DataFrame, centers: np.ndarray, names: list[str], order: list[int]) -> None:
    section("Cluster profiles")
    dims = ["capability", "valence", "understanding", "community", "institutions", "adoption", "overall", "tone"]
    prof = a.groupby("cluster")[dims].mean().loc[order].round(2)
    prof.insert(0, "n", a["cluster"].value_counts().loc[order])
    prof.index = [names[c] for c in order]
    print(prof.T.to_string())

    for col, title in [("career_group", "Career stage"), ("ai_use_group", "Author's own AI use"),
                       ("post_type", "Post type")]:
        tab = pd.crosstab(a["cluster"], a[col], normalize="index").loc[order] * 100
        tab.index = [names[c] for c in order]
        print(f"\n{title} (% of cluster):")
        print(tab.round(0).astype(int).to_string())

    print("\nMost typical posts (closest to the cluster centre):")
    for c in order:
        s = a[a["cluster"] == c].copy()
        s["dist"] = np.hypot(s["capability"].fillna(0) - centers[c][0], s["valence"] - centers[c][1])
        print(f"\n  {names[c]}")
        for _, r in s.nsmallest(5, "dist").iterrows():
            print(f"    cap {r['capability'] if pd.notna(r['capability']) else 0:+.2f}  val {r['valence']:+.2f}  "
                  f"{r['title'][:75]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()

    df, a_all = eda.load()
    # Posts that take no position on capability can't be placed on that axis; filling them in
    # as 0 would wrongly read "no opinion" as "doubts AI". Cluster the rest; list these apart.
    a = a_all[a_all["capability"].notna()].copy()
    unplaced = a_all[a_all["capability"].isna()].copy()
    labels, centers, stats = fit_clusters(a, args.k)
    a["cluster"] = labels
    names = [name_cluster(*centers[c]) for c in range(args.k)]
    order = list(np.argsort(-centers[:, 1]))  # most positive valence first; fixes color slots

    section(f"k-means on {' + '.join(FEATURES)}, k={args.k}")
    print(f"silhouette {stats['silhouette']:.2f};  bootstrap ARI median {stats['ari_median']:.2f} "
          f"(5th pct {stats['ari_p5']:.2f})")
    for c in order:
        print(f"  {names[c]:<26} capability {centers[c][0]:+.2f}  valence {centers[c][1]:+.2f}  "
              f"n={int((labels == c).sum())}")
    if len(set(names)) < len(names):
        print("  note: some clusters share a name; see the centres above.")
    print(f"  ({len(unplaced)} posts don't address capability and are not clustered: "
          f"mean valence {unplaced['valence'].mean():+.2f})")

    profile(a, centers, names, order)

    texts = {r["id"]: r["text"] for r in map(json.loads, (ROOT / "data" / "dataset.jsonl").read_text().splitlines())}
    terms = distinctive_terms([texts[i] for i in a["id"]], labels)
    terms = drop_redundant(terms)
    terms["cluster_name"] = terms["cluster"].map(dict(enumerate(names)))
    removed = terms[terms["term"].isin(GENERIC)]
    removed.to_csv(ROOT / "data" / "wordcloud_terms_removed.csv", index=False)
    terms = terms[~terms["term"].isin(GENERIC)]
    print(f"\nRemoved {len(removed)} generic terms from the clouds (see data/wordcloud_terms_removed.csv)")
    terms = add_examples(terms, [texts[i] for i in a["id"]], list(a["title"]), labels)

    section("Top distinctive terms per cluster")
    for c in order:
        g = terms[terms["cluster"] == c].head(20)
        print(f"\n  {names[c]}:")
        print("    " + ", ".join(f"{t} ({p:.0%} vs {q:.0%})" for t, p, q in
                                  zip(g["term"], g["pct_in_cluster"], g["pct_elsewhere"])))

    a["cluster_name"] = a["cluster"].map(dict(enumerate(names)))
    unplaced["cluster"], unplaced["cluster_name"] = -1, "capability not addressed"
    a = pd.concat([a, unplaced])
    cols =["id", "title", "url", "published", "written", "cluster", "cluster_name", "capability",
            "valence", "understanding", "community", "institutions", "adoption", "overall", "tone",
            "post_type", "author_career_stage", "ai_in_research", "summary"]
    a[cols].sort_values(["cluster", "valence"]).to_csv(ROOT / "data" / "clusters.csv", index=False)
    terms[["cluster", "cluster_name", "term", "z", "log_odds_ratio", "p_one_sided", "posts_in_cluster",
           "pct_in_cluster", "pct_elsewhere", "example", "example_post"]].to_csv(
        ROOT / "data" / "wordcloud_terms.csv", index=False)

    fig_clusters(a, centers, names, order)
    render_clouds(terms, names, order, {c: int((labels == c).sum()) for c in range(args.k)})
    print(f"\nWrote data/clusters.csv, data/wordcloud_terms.csv, figures/08_clusters.png, figures/09_*.png")


if __name__ == "__main__":
    main()
