# Proofs and Prompts: AI-in-math sentiment dataset

Crawls every post on <https://proofsandprompts.com/> and annotates each one with Claude
along several sentiment dimensions about AI's role in mathematics, plus author metadata.
The output is meant for clustering posts by their scores and building per-cluster word clouds.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
export ANTHROPIC_WORKSPACE_ID=wrkspc_...   # only if the key isn't scoped to a workspace
```

The workspace ID is in the Claude Console under Settings → Workspaces. Alternatively, create an
API key inside a workspace and skip this variable.

## Run

```bash
.venv/bin/python crawl.py              # ~5 s, writes data/posts.jsonl
.venv/bin/python score.py --limit 3    # try 3 posts; prints tokens and cost
.venv/bin/python score.py              # score the rest (cached, resumable)
```

`score.py` caches results in `data/scores.jsonl`, keyed by post id plus a hash of the rubric,
model, and effort. Re-running it skips posts that are already scored. If you edit `rubric.py`
or change `--effort`, it re-scores everything under the new version.

## What is collected

**From the site** (`crawl.py`, via the WordPress REST API):

| field | notes |
|---|---|
| `published`, `received` | publication date, and the "Received <date>" submission footer (144/171 posts) |
| `categories`, `tags`, `contributors` | site taxonomies |
| `author_line` | the affiliation line at the top of each post |
| `text`, `word_count` | main text; author line, "Received" footer, and repeated site banners removed |
| `has_ai_statement` | regex hint for an explicit "AI use:" / "AI disclosure:" line |

**From Claude** (`score.py`, rubric in `rubric.py`). Each score is in [-1, 1] and comes with a
short supporting quote (`*_evidence`). A score is left blank when the post takes no position on
that dimension.

| dimension | -1 ⟷ +1 |
|---|---|
| `capability` | AI is useless or overhyped for doing math ⟷ powerful, transformative |
| `understanding` | erodes understanding / the point of math ⟷ deepens it |
| `community` | harms careers, training, equity ⟷ benefits them |
| `institutions` | norms and institutions will fail to adapt ⟷ will adapt well |
| `adoption` | resist / restrict ⟷ embrace / integrate |
| `overall` | overall negative ⟷ positive |
| `tone` | emotional register: alarmed ⟷ enthusiastic (kept separate from stance) |

Also: `post_type` (essay, practice report, proposal, statement, announcement, survey, creative),
`relevance` to AI in math, `summary`, `author_career_stage`, `author_sector`, `author_n_authors`,
`author_field`, `ai_in_research` (substantial / occasional / experimented / open_to_or_planning / none / not_stated),
and `ai_in_writing_post`.

## Outputs

- `data/dataset.csv`: one row per post, metadata plus scores (no full text)
- `data/dataset.jsonl`: the same rows plus `text`, for word clouds
- `data/scores.jsonl`: raw annotations with token usage and request ids
- `data/raw/posts_api.json`: untouched API responses
- `data/field_groups.csv`: **hand-curated**, not generated. Author field group for the 31
  applied / engineering / TCS / physics / industry authors (`id`, `field_group`, plus
  `author_line` and `title` for checking). Every post not listed counts as core mathematics. It is
  kept separate because `score.py` regenerates `dataset.csv`, and because the model-extracted
  `author_field` is blank for 103 of 171 posts.

## Exploratory analysis

```bash
.venv/bin/python eda.py   # prints tables, writes figures/01..07_*.png and 10_field_group.png
```

The analysis set excludes announcements, creative pieces, "other", and posts with minimal
relevance (152 of 171 remain). `valence` = mean of understanding, community, adoption, and
overall. `written` = the "Received" date where present, else the publication date.
`field_group` is joined from `data/field_groups.csv`. `figures/10_field_group.png` compares
core-math authors with applied-side authors (pooled, and by sub-group), with permutation tests
on the difference in means.

## Clusters and word clouds

```bash
.venv/bin/python cluster.py          # k=3; use --k 4 to compare
```

- k-means on standardised **capability + valence**. Only posts that address capability are
  clustered; the rest are listed as `capability not addressed` (cluster −1).
- Word-cloud terms are unigrams and bigrams ranked by a log odds ratio z on the **share of
  posts** containing the term (cluster vs. elsewhere), so one very long post can't dominate.
  A term must appear in ≥5 of the cluster's posts with z ≥ 2. Tune `MIN_POSTS`, `MIN_Z`, and
  `EXTRA_STOP` at the top of `cluster.py`.
- `data/wordcloud_terms.csv` has the term statistics plus an in-context `example` snippet, so you
  can check what a word refers to (e.g. "dead" → "dead ends") before using it.
- Figures: `figures/08_clusters.png`, `figures/09_wordclouds.png`, and one cloud per cluster.

## Notes

- The model is `claude-opus-5-5` at effort `medium` by default. The API's server-side refusal
  fallback is enabled, so a safety decline is retried on another model and still returns a
  result. `model_served` records which model actually answered.
- Before trusting the scores, check about 15 posts by hand against `*_evidence` and `summary`.
- Consider filtering on `post_type` and `relevance` before clustering: announcements and
  creative pieces behave differently from essays.
