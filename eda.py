"""Exploratory analysis of data/dataset.csv: which features are informative for clustering?

Writes figures to figures/ and prints the supporting tables.

  python eda.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import fisher_exact
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).parent
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

DIMS = ["capability", "understanding", "community", "institutions", "adoption", "overall"]
ALL_SCORES = DIMS + ["tone"]
# Dimensions that move together (see correlation figure); averaged into one "valence" axis.
VALENCE_DIMS = ["understanding", "community", "adoption", "overall"]

EVENTS = {
    "2026-09-08": "OpenAI Navier–Stokes\nannouncement",
    "2026-10-06": "OpenAI releases\n722 manuscripts",
}

# --- palette (reference instance from the dataviz skill; validated all-pairs for 3 slots) ---
SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT_2 = "#52514e"
MUTED = "#a3a29c"
GRID = "#e6e5e0"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a"]
MARKERS = ["o", "s", "^"]
DIVERGING = LinearSegmentedColormap.from_list("div", ["#e34948", "#f0efec", "#2a78d6"])

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRID, "axes.labelcolor": TEXT_2, "axes.titlecolor": TEXT,
    "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlelocation": "left",
    "axes.labelsize": 10, "xtick.color": TEXT_2, "ytick.color": TEXT_2,
    "xtick.labelsize": 9, "ytick.labelsize": 9, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.8, "axes.axisbelow": True, "axes.spines.top": False,
    "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 9,
    "font.size": 10, "figure.dpi": 110, "savefig.dpi": 160, "savefig.bbox": "tight",
})

CAREER_GROUP = {
    "undergraduate_or_prospective": "Students",
    "phd_student": "Students",
    "postdoc": "Early career",
    "early_career_faculty": "Early career",
    "senior_faculty": "Senior",
    "emeritus_or_retired": "Senior",
}
GROUP_ORDER = ["Students", "Early career", "Senior"]

AI_USE_GROUP = {
    "substantial": "Uses AI (regularly)",
    "occasional": "Uses AI (regularly)",
    "experimented": "Tried / open to it",
    "open_to_or_planning": "Tried / open to it",
    "none": "Doesn't use AI",
    "not_stated": "Not stated",
}
AI_USE_ORDER = ["Uses AI (regularly)", "Tried / open to it", "Doesn't use AI", "Not stated"]

# Hand-curated author field groups (data/field_groups.csv). The model-extracted author_field is
# blank for most posts, so applied/engineering/TCS/physics authors were classified by reading
# author_line; every post not listed there counts as core mathematics.
CORE = "Core math (rest)"
APPLIED_ALL = "All applied-side"
FIELD_ORDER = [CORE, APPLIED_ALL, "PDE / numerics / fluids", "Probability / stats / econ",
               "Physics", "Industry / engineering", "TCS / CS"]


def section(title: str) -> None:
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(ROOT / "data" / "dataset.csv", parse_dates=["published", "received", "revised"])
    df["written"] = df["received"].fillna(df["published"])  # best estimate of when it was written
    df["valence"] = df[VALENCE_DIMS].mean(axis=1, skipna=True)
    df["career_group"] = df["author_career_stage"].map(CAREER_GROUP).fillna("Other")
    df["ai_use_group"] = df["ai_in_research"].map(AI_USE_GROUP)
    fields = pd.read_csv(ROOT / "data" / "field_groups.csv", usecols=["id", "field_group"])
    df = df.merge(fields, on="id", how="left")
    df["field_group"] = df["field_group"].fillna(CORE)
    # Analysis set: individual or collective argued positions about AI in math.
    keep = (df["relevance"] != "minimal") & ~df["post_type"].isin(["announcement", "creative_or_satire", "other"])
    return df, df[keep].copy()


def boot_ci(x: pd.Series, n: int = 4000, seed: int = 0) -> tuple[float, float, float]:
    x = x.dropna().to_numpy()
    if len(x) < 2:
        return (float(x.mean()) if len(x) else np.nan, np.nan, np.nan)
    rng = np.random.default_rng(seed)
    means = rng.choice(x, size=(n, len(x)), replace=True).mean(axis=1)
    return x.mean(), *np.percentile(means, [2.5, 97.5])


# ---------------------------------------------------------------------------
def fig_distributions(a: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.2))
    rng = np.random.default_rng(1)
    for i, d in enumerate(ALL_SCORES):
        y = len(ALL_SCORES) - 1 - i
        v = a[d].dropna()
        ax.scatter(v, y + rng.uniform(-0.22, 0.22, len(v)), s=14, color=SERIES[0], alpha=0.45, lw=0)
        ax.plot([v.median()] * 2, [y - 0.32, y + 0.32], color=TEXT, lw=2, solid_capstyle="round")
        ax.text(1.08, y, f"n={len(v)}  mean {v.mean():+.2f}", va="center", fontsize=8.5, color=TEXT_2)
    ax.set_yticks(range(len(ALL_SCORES)), ALL_SCORES[::-1])
    ax.axvline(0, color=MUTED, lw=1)
    ax.set_xlim(-1.08, 1.05)
    ax.set_xlabel("score  (−1 negative  ·  +1 positive)")
    ax.set_title("Mathematicians rate AI as capable but are split on its consequences")
    ax.grid(axis="y", visible=False)
    fig.text(0.01, -0.02, "Each dot is a post; black bar is the median. Blank (not addressed) scores omitted.",
             fontsize=8, color=TEXT_2)
    fig.savefig(FIG / "01_distributions.png")
    plt.close(fig)


def fig_correlation(a: pd.DataFrame) -> pd.DataFrame:
    corr = a[ALL_SCORES].corr()
    fig, ax = plt.subplots(figsize=(6.2, 5.2))
    im = ax.imshow(corr, cmap=DIVERGING, vmin=-1, vmax=1)
    ax.set_xticks(range(len(ALL_SCORES)), ALL_SCORES, rotation=40, ha="right")
    ax.set_yticks(range(len(ALL_SCORES)), ALL_SCORES)
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    for i in range(len(ALL_SCORES)):
        for j in range(len(ALL_SCORES)):
            ax.text(j, i, f"{corr.iat[i, j]:.2f}", ha="center", va="center", fontsize=8.5,
                    color=TEXT if abs(corr.iat[i, j]) < 0.75 else SURFACE)
    cb = fig.colorbar(im, ax=ax, shrink=0.8)
    cb.outline.set_visible(False)
    cb.ax.tick_params(labelsize=8)
    ax.set_title("Capability stands apart; the other dimensions move together")
    fig.savefig(FIG / "02_correlation.png")
    plt.close(fig)
    return corr


def pca_analysis(a: pd.DataFrame) -> None:
    section("PCA on the six stance dimensions")
    variants = {
        "complete cases only": a[DIMS].dropna(),
        "blanks imputed as 0 (neutral)": a[DIMS].fillna(0),
    }
    loadings = None
    for name, X in variants.items():
        Z = StandardScaler().fit_transform(X)
        p = PCA().fit(Z)
        ev = p.explained_variance_ratio_
        print(f"\n{name}: n={len(X)}  variance explained "
              + "  ".join(f"PC{i+1} {v:.0%}" for i, v in enumerate(ev[:4])))
        L = pd.DataFrame(p.components_[:3].T, index=DIMS, columns=["PC1", "PC2", "PC3"])
        # Orient for readability: PC1 so 'overall' loads positive, PC2 so 'capability' does.
        L["PC1"] *= np.sign(L.at["overall", "PC1"])
        L["PC2"] *= np.sign(L.at["capability", "PC2"])
        L["PC3"] *= np.sign(L.at["institutions", "PC3"])
        print(L.round(2).to_string())
        if loadings is None:
            loadings, evr = L, ev

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8), gridspec_kw={"width_ratios": [1, 1.6]})
    ax1.bar(range(1, 7), evr, color=SERIES[0], width=0.6)
    for i, v in enumerate(evr):
        ax1.text(i + 1, v + 0.01, f"{v:.0%}", ha="center", fontsize=8.5, color=TEXT_2)
    ax1.set_xticks(range(1, 7), [f"PC{i}" for i in range(1, 7)])
    ax1.set_ylabel("share of variance")
    ax1.set_title("Two components carry most of the signal")
    ax1.grid(axis="x", visible=False)

    y = np.arange(len(DIMS))
    h = 0.36
    ax2.barh(y - h / 2, loadings["PC1"], height=h, color=SERIES[0], label="PC1")
    ax2.barh(y + h / 2, loadings["PC2"], height=h, color=SERIES[1], label="PC2")
    ax2.set_yticks(y, DIMS)
    ax2.invert_yaxis()
    ax2.axvline(0, color=MUTED, lw=1)
    ax2.set_xlabel("loading")
    ax2.set_title("PC1 ≈ valence, PC2 ≈ capability")
    ax2.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))
    ax2.grid(axis="y", visible=False)
    fig.text(0.01, -0.03, "Standardised scores, complete cases only.", fontsize=8, color=TEXT_2)
    fig.tight_layout(w_pad=4)
    fig.savefig(FIG / "03_pca.png")
    plt.close(fig)


def fig_scatter(a: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7.2, 6))
    rng = np.random.default_rng(2)
    jit = lambda n: rng.uniform(-0.025, 0.025, n)  # scores are on a 0.05 grid; separate overlaps
    other = a[a["career_group"] == "Other"]
    ax.scatter(other["capability"] + jit(len(other)), other["valence"] + jit(len(other)), s=34,
               color=MUTED, marker="D", lw=0, alpha=0.7, label=f"Other / unknown (n={len(other)})")
    for g, c, m in zip(GROUP_ORDER, SERIES, MARKERS):
        s = a[a["career_group"] == g]
        ax.scatter(s["capability"] + jit(len(s)), s["valence"] + jit(len(s)), s=40, color=c, marker=m,
                   edgecolor=SURFACE, lw=1.2, alpha=0.9, label=f"{g} (n={len(s)})")
    ax.axhline(0, color=MUTED, lw=1)
    ax.axvline(0, color=MUTED, lw=1)
    for (x, y, t, ha) in [(-0.95, 0.92, "doubts AI, positive", "left"), (0.95, 0.92, "rates AI capable, positive", "right"),
                          (-0.95, -0.95, "doubts AI, negative", "left"), (0.95, -0.95, "rates AI capable, negative", "right")]:
        ax.text(x, y, t, ha=ha, fontsize=8.5, color=TEXT_2, style="italic")
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_xlabel("capability  (how useful AI is for doing mathematics)")
    ax.set_ylabel("valence  (mean of understanding, community, adoption, overall)")
    ax.set_title("Most posts sit right of centre: the disagreement is about consequences")
    ax.legend(loc="upper left", bbox_to_anchor=(0, -0.11), ncol=2)
    n_missing = a["capability"].isna().sum()
    fig.text(0.01, -0.12, f"{n_missing} posts that do not address capability are not shown.",
             fontsize=8, color=TEXT_2)
    fig.savefig(FIG / "04_capability_vs_valence.png")
    plt.close(fig)


def fig_time(a: pd.DataFrame) -> None:
    section("Sentiment over time (by date written = received date, else published)")
    t = a.sort_values("written").set_index("written")
    fig, axes = plt.subplots(3, 1, figsize=(9, 7.4), sharex=True,
                             gridspec_kw={"height_ratios": [1, 2, 2]})
    weekly = t.resample("W")["id"].count()
    axes[0].bar(weekly.index, weekly.values, width=5, color=SERIES[0])
    axes[0].set_ylabel("posts / week")
    axes[0].grid(axis="x", visible=False)

    for ax, col in zip(axes[1:], ["capability", "valence"]):
        s = t[col].dropna()
        ax.scatter(s.index, s.values, s=14, color=SERIES[0], alpha=0.35, lw=0)
        # Rolling mean over posts in the trailing 21 days, computed per day so that
        # several posts on one date don't produce vertical steps.
        daily = s.groupby(s.index.normalize()).agg(["sum", "count"]).asfreq("D", fill_value=0)
        win = daily.rolling("21D").sum()
        roll = (win["sum"] / win["count"]).where(win["count"] >= 5)
        ax.plot(roll.index, roll.values, color=SERIES[0], lw=2, label="21-day rolling mean")
        ax.axhline(0, color=MUTED, lw=1)
        ax.set_ylim(-1.05, 1.05)
        ax.set_ylabel(col)
    axes[1].legend(loc="lower left")
    for ax in axes:
        for d in EVENTS:
            ax.axvline(pd.Timestamp(d), color=TEXT_2, lw=1, ls=(0, (3, 3)))
    for d, lbl in EVENTS.items():
        axes[0].annotate(lbl, (pd.Timestamp(d), 1.0), xycoords=("data", "axes fraction"),
                         xytext=(0, 4), textcoords="offset points", fontsize=8, color=TEXT_2,
                         va="bottom", ha="center", annotation_clip=False)
    axes[0].set_title("Volume and sentiment by date written", pad=34)
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    fig.tight_layout()
    fig.savefig(FIG / "05_time.png")
    plt.close(fig)

    # Before / after each event, by date written.
    rows = []
    for d, lbl in EVENTS.items():
        cut = pd.Timestamp(d)
        for col in ["capability", "valence", "overall", "tone"]:
            b, af = a.loc[a["written"] < cut, col].dropna(), a.loc[a["written"] >= cut, col].dropna()
            rows.append({"event": lbl.replace("\n", " "), "measure": col, "n_before": len(b),
                         "mean_before": b.mean(), "n_after": len(af), "mean_after": af.mean(),
                         "diff": af.mean() - b.mean(), "perm_p": perm_test(b, af)})
    print(pd.DataFrame(rows).round(3).to_string(index=False))
    print("\nperm_p: two-sided permutation test on the difference in means (10,000 shuffles).")


def perm_test(x: pd.Series, y: pd.Series, n: int = 10000, seed: int = 0) -> float:
    x, y = x.to_numpy(), y.to_numpy()
    if len(x) < 3 or len(y) < 3:
        return np.nan
    obs = abs(y.mean() - x.mean())
    pooled = np.concatenate([x, y])
    rng = np.random.default_rng(seed)
    cnt = 0
    for _ in range(n):
        rng.shuffle(pooled)
        cnt += abs(pooled[len(x):].mean() - pooled[: len(x)].mean()) >= obs
    return (cnt + 1) / (n + 1)


def fig_groups(a: pd.DataFrame, col: str, order: list[str], fname: str, title: str,
               measures: list[str] | None = None) -> pd.DataFrame:
    measures = measures or ["capability", "valence", "community", "institutions"]
    fig, axes = plt.subplots(1, len(measures), figsize=(2.75 * len(measures), 0.55 * len(order) + 1.6),
                             sharey=True)
    table = []
    for ax, m in zip(axes, measures):
        for i, g in enumerate(order):
            mean, lo, hi = boot_ci(a.loc[a[col] == g, m])
            n = a.loc[a[col] == g, m].notna().sum()
            table.append({"group": g, "measure": m, "n": n, "mean": mean, "ci_lo": lo, "ci_hi": hi})
            if np.isnan(mean):
                continue
            ax.plot([lo, hi], [i, i], color=SERIES[0], lw=2, solid_capstyle="round", alpha=0.5)
            ax.scatter([mean], [i], s=48, color=SERIES[0], zorder=3, edgecolor=SURFACE, lw=1.2)
            ax.text(mean, i - 0.22, f"n={n}", fontsize=7.5, color=TEXT_2, va="bottom", ha="center")
        ax.axvline(0, color=MUTED, lw=1)
        ax.set_xlim(-1, 1)
        ax.set_title(m, fontsize=10, loc="center")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(len(order)), order)
    axes[0].set_ylim(len(order) - 0.5, -0.75)  # inverted, with headroom for the top row's n label
    fig.suptitle(title, x=0.01, ha="left", fontsize=12, fontweight="bold", color=TEXT)
    fig.text(0.01, -0.04, "Dot = mean score; line = 95% bootstrap interval.", fontsize=8, color=TEXT_2)
    fig.tight_layout()
    fig.savefig(FIG / fname)
    plt.close(fig)
    t = pd.DataFrame(table).pivot(index="group", columns="measure", values="mean").reindex(order)
    n = pd.DataFrame(table).pivot(index="group", columns="measure", values="n").reindex(order)
    print(t[measures].round(2).astype(str).add("  (n=").add(n[measures].astype(int).astype(str)).add(")").to_string())
    return t


def field_groups(a: pd.DataFrame) -> None:
    section("By author field: applied / engineering / TCS / physics vs core mathematics")
    applied = a[a["field_group"] != CORE]
    # Pooled applied row alongside its sub-groups (applied posts appear twice in the plot frame).
    plot = pd.concat([a, applied.assign(field_group=APPLIED_ALL)], ignore_index=True)
    fig_groups(plot, "field_group", FIELD_ORDER, "10_field_group.png",
               "Applied-side authors rate AI about as capable as core mathematicians do, but lean toward adopting it",
               measures=["capability", "adoption", "understanding", "community", "institutions"])
    core = a[a["field_group"] == CORE]
    print("\nApplied-side vs core math (two-sided permutation test on the difference in means):")
    for m in ["capability", "adoption", "understanding", "community", "institutions", "overall"]:
        x, y = core[m].dropna(), applied[m].dropna()
        print(f"  {m:13s} core {x.mean():+.2f} (n={len(x)})  applied {y.mean():+.2f} (n={len(y)})  "
              f"diff {y.mean() - x.mean():+.2f}  p={perm_test(x, y):.3f}")
    subst = a.assign(s=a["ai_in_research"].eq("substantial")).groupby(a["field_group"] != CORE)["s"]
    k, n = subst.sum(), subst.size()
    p = fisher_exact([[k[True], n[True] - k[True]], [k[False], n[False] - k[False]]]).pvalue
    print(f"\nReports substantial AI use in research: core {k[False] / n[False]:.0%} ({k[False]}/{n[False]}), "
          f"applied {k[True] / n[True]:.0%} ({k[True]}/{n[True]}); Fisher exact p={p:.4f}")


def tone_check(a: pd.DataFrame) -> None:
    section("Tone vs stance: does emotional register bleed into scores?")
    d = a.dropna(subset=["overall", "tone"])
    gap = (d["tone"] - d["overall"])
    print(f"corr(tone, overall) = {d['tone'].corr(d['overall']):.2f};  mean |tone − overall| = {gap.abs().mean():.2f}")
    print(f"posts where tone and overall differ in sign: {(np.sign(d['tone']) * np.sign(d['overall']) < 0).sum()} of {len(d)}")
    print("largest gaps (worth reading by hand):")
    for _, r in d.loc[gap.abs().sort_values(ascending=False).index[:6]].iterrows():
        print(f"  tone {r['tone']:+.2f}  overall {r['overall']:+.2f}  {r['title'][:70]}")


def cluster_preview(a: pd.DataFrame) -> None:
    section("Cluster tendency on reduced axes (preview only)")
    feature_sets = {
        "capability + valence": ["capability", "valence"],
        "capability + valence + institutions": ["capability", "valence", "institutions"],
        "all six dimensions": DIMS,
    }
    for name, cols in feature_sets.items():
        X = a[cols].fillna(0)  # blanks as neutral, for the preview
        Z = StandardScaler().fit_transform(X)
        sil = {k: silhouette_score(Z, KMeans(k, n_init=20, random_state=0).fit_predict(Z)) for k in range(2, 8)}
        bic = {k: GaussianMixture(k, n_init=5, random_state=0).fit(Z).bic(Z) for k in range(1, 8)}
        print(f"\n{name} (n={len(X)})")
        print("  k-means silhouette: " + "  ".join(f"k={k} {v:.2f}" for k, v in sil.items()))
        print("  GMM BIC (lower is better): " + "  ".join(f"k={k} {v:.0f}" for k, v in bic.items()))
    print("\nSilhouette > 0.5 = clear structure; 0.25-0.5 = weak; < 0.25 = little natural clustering.")


def main() -> None:
    df, a = load()
    section("Analysis set")
    print(f"{len(df)} posts total; {len(a)} kept after dropping announcements, creative pieces, "
          f"'other', and minimal-relevance posts.")
    print(a["post_type"].value_counts().to_string())
    print("\nBlank (not addressed) rate:")
    print((a[DIMS].isna().mean() * 100).round(0).astype(int).astype(str).add("%").to_string())

    fig_distributions(a)
    section("Correlation of scores")
    print(fig_correlation(a).round(2).to_string())
    pca_analysis(a)
    fig_scatter(a)
    fig_time(a)
    section("By career stage")
    fig_groups(a, "career_group", GROUP_ORDER + ["Other"], "06_career_stage.png",
               "Career stage barely separates the groups; everyone is negative about community")
    section("By the author's own AI use")
    fig_groups(a, "ai_use_group", AI_USE_ORDER, "07_ai_use.png",
               "Authors who use AI lean more positive, but non-users are only a handful of posts")
    field_groups(a)
    tone_check(a)
    cluster_preview(a)
    print(f"\nFigures written to {FIG}/")


if __name__ == "__main__":
    main()
