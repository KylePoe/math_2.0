# Math 2.0: From Society to the Lab

Slides, research notes and a small data analysis for a talk on how AI is changing mathematical research, given by Kyle Poe at the Vidal Lab, University of Pennsylvania, on 11 November 2026.

The thesis of the talk:

> Amidst the plethora of ethical concerns surrounding proliferation and normalization of the technology, AI is ushering in a new dominant paradigm for mathematical, and more broadly theoretical, research. Thoughtfully deployed, AI-assisted formalization tools will be the glue between human and machine understanding which ensures the integrity and alignment of future scientific enterprise.

Part I (*Society*) looks at how mathematicians are reacting, the problems they name, and why formal verification is the one remedy with advocates in every camp, along with the three things a certificate must get right: validity, statement fidelity and proof fidelity. Part II (*The Lab*) argues for working through Lean blueprints: agree with the machine statement by statement, and treat lemmas as the unit of understanding.

## What is here

| Path | Contents |
|---|---|
| [`talk/`](talk/) | The Beamer slides. [`talk/math-2.0-slides.pdf`](talk/math-2.0-slides.pdf) is the PDF, one page per slide. |
| [`talk/RESOURCES.md`](talk/RESOURCES.md) | Every tool, library and reading recommended in the talk, with links. The QR code on the last slide points here. |
| [`research/`](research/) | Six research notes behind the slides, with sources. |
| `crawl.py`, `rubric.py`, `score.py`, `eda.py`, `cluster.py` | The sentiment analysis of the *Proofs and Prompts* essays used in Part I. |
| [`data/`](data/), [`figures/`](figures/) | Its outputs: scores, clusters, word-cloud terms and figures. |
| [`questions_of_interest.md`](questions_of_interest.md) | The questions the research set out to answer. |

## Slides

```bash
cd talk
latexmk main.tex          # XeLaTeX, output in talk/build/main.pdf
```

The build needs a recent TeX Live (2025 or later) with `pgfplots`, `qrcode` and `fontawesome5`, and the Open Sans font (the theme falls back to TeX Live's copy if it isn't installed). The two timeline slides and the thesis slide are animated, so `build/main.pdf` has more pages than slides. For one page per slide, build the handout version:

```bash
latexmk -jobname=math-2.0-slides -usepretex='\PassOptionsToClass{handout}{beamer}' main.tex
```

See [`talk/README.md`](talk/README.md) for how the deck is organized.

## Research notes

Written in November 2026 while preparing the talk. Each note tags claims by how far they can be trusted (for example *self-reported* for a lab's own announcement, *secondary* for a claim known only through another source) and ends with a list of what still needed checking.

| Note | Topic |
|---|---|
| [01](research/01-formalization-landmarks.md) | Formalization landmarks, from the four colour theorem to the 2026 AI-era projects, and what "verified" means |
| [02](research/02-ai-math-tools.md) | The tools between doing mathematics and verifying it: blueprints, agents, provers, checkers, registries, libraries |
| [03](research/03-publishing-crisis.md) | The publishing crisis: AI use and disclosure on arXiv, refereeing capacity, and the institutional responses |
| [04](research/04-applied-engineering-views.md) | How applied mathematics, engineering, TCS and physics see these developments differently from pure mathematics |
| [05](research/05-applied-ai-proofs-and-formalization.md) | AI-generated proofs in applied mathematics: informal proofs, formal proofs and certified computation |
| [06](research/06-acadmathsci-report-review.md) | A review of the Academy for the Mathematical Sciences report *The Mathematical Sciences in an AI-enabled World* (Oct 2026) |

`research/scripts/lean_count.py` counts arXiv submissions whose abstracts mention Lean or Mathlib, by month.

## The sentiment analysis

[*Proofs and Prompts*](https://proofsandprompts.com/) is a blog of essays by mathematicians on how AI is changing their practice. The pipeline crawls every post (171, from 7 August to 9 November 2026), has Claude score each one on several dimensions of its stance on AI in mathematics, and clusters the posts on two of them.

**Scores.** Each is in [−1, 1], with a short supporting quote, and is left blank when a post takes no position. The rubric is in [`rubric.py`](rubric.py).

| Dimension | −1 ⟷ +1 |
|---|---|
| `capability` | AI is useless or overhyped for mathematics ⟷ powerful, transformative |
| `understanding` | erodes understanding ⟷ deepens it |
| `community` | harms careers, training, equity ⟷ benefits them |
| `institutions` | norms and institutions will fail to adapt ⟷ will adapt well |
| `adoption` | resist or restrict ⟷ embrace or integrate |
| `overall` | negative ⟷ positive |
| `tone` | alarmed ⟷ enthusiastic (emotional register, kept apart from stance) |

Claude also records the post type, its relevance to AI in mathematics, a summary, the author's career stage, sector and field, and whether the author says they use AI.

**Analysis.** The analysis set leaves out announcements, creative pieces and posts of minimal relevance, which leaves 152 posts. `valence` is the mean of understanding, community, adoption and overall. `cluster.py` runs k-means (k = 3) on standardized capability and valence for the 141 posts that address capability, then ranks each cluster's distinctive words by a log odds ratio on the share of posts using them.

**Data.** The full text of the posts belongs to their authors and is not included. The repository has everything derived from it:

| File | Contents |
|---|---|
| `data/dataset.csv` | One row per post: metadata, scores and supporting quotes, no full text |
| `data/scores.jsonl` | Raw model annotations, used as a cache by `score.py` |
| `data/clusters.csv` | Cluster assignment and scores for each post |
| `data/wordcloud_terms.csv` | Word-cloud terms with their statistics and a short example in context; `wordcloud_terms_removed.csv` lists the generic words removed by hand |
| `data/field_groups.csv` | Hand-curated field groups for the 31 applied, engineering, TCS, physics and industry authors |

**Reproducing it.**

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python crawl.py               # fetches the posts into data/posts.jsonl
.venv/bin/python score.py --rebuild     # joins them with the cached scores; no API calls
.venv/bin/python eda.py                 # tables and figures/01–07, 10
.venv/bin/python cluster.py             # clusters and word clouds, figures/08–09
```

`score.py --rebuild` reuses the scores in `data/scores.jsonl`. Posts published after 9 November 2026 have no cached score. To score them, or to re-score after changing the rubric, set `ANTHROPIC_API_KEY` (and `ANTHROPIC_WORKSPACE_ID` if the key isn't scoped to a workspace) and run `score.py` without `--rebuild`. Scoring all 171 posts with `claude-opus-5-5` at medium effort cost about US$5.

The scores come from a language model reading a self-selected set of essays. They illustrate how one community of mathematicians is reacting; they are not a survey.

## AI use

These materials were prepared with the assistance of Claude Opus 5.5. The essays were scored by Claude, as described above.
