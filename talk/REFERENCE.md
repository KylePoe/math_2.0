# Math 2.0: From Society to the Lab — talk reference

A working reference for the talk: what it argues, how it is organized and why, what each slide is for, the facts and sources to draw on, and how the Beamer project is built. Compiled 2026-11-10 from the planning sessions. Research detail lives in `../research/0N-*.md`; this file points into it rather than repeating it.

---

## 1. The talk in one page

| | |
|---|---|
| **Title** | *Math 2.0* — subtitle *From Society to the Lab* |
| **Speaker** | Kyle Poe, Vidal Lab, University of Pennsylvania |
| **Audience** | The Vidal Lab, a deep-learning theory group. Mostly not Lean users; fluent in ML. |
| **Length** | 60-minute slot: **45 minutes of content, 15 of discussion** |
| **Thesis** | AI-generated mathematics together with formal (Lean) certification is a coherent, emerging paradigm for doing mathematics in the 21st century. This is Math 2.0: proofs are becoming abundant, and insight is what stays scarce. |
| **What the audience should leave with** | (a) Math 2.0 is coming, and the community is already reorganizing around it. (b) The problem no institution can solve for you is checking: whether the formal statement is right, and whether anyone understands the proof. (c) Concrete ways to take part in their own research. (d) A sense of personal responsibility: use the tools, but stay the author. |

### Relation to Tao
"Math 2.0" is Terence Tao's term (Mathstodon, 6 Oct 2026; Caltech lecture, 9 Oct; [blog post, 10 Oct](https://terrytao.wordpress.com/2026/10/10/math-2-0/); [slides](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf)). The talk **follows Tao** in:
- the terminology;
- the shift from **proof scarcity to proof abundance**, the main parallel;
- his emphasis on **understanding and community**.

The talk adds the formal-certification angle (AI + Lean) as the mechanism behind the shift. Attribute Tao explicitly on the Math 1.0 / 2.0 slide. Tao's ICM essay §7, "Proof scarcity and proof abundance", including "proof indigestion" ([arXiv 2608.16753](https://arxiv.org/html/2608.16753v1)), is the scholarly anchor. Quote Tao from his own slides or blog, not from secondary coverage.

### The idea that runs through the talk: three layers of checking
1. **Kernel**: does Lean accept the proof? (Cheap now.)
2. **Statement**: does the formal statement say what the paper claims? (Scarce; Kontorovich: the gap "will never be solved purely in software".)
3. **Understanding**: does anyone understand the proof, and does the formal proof match the written one? (Scarce.)

Part I **poses** this problem through Navier–Stokes and leaves it unsolved. Part II **answers** it, one layer at a time. The closing returns to the third layer as "insight scarcity".

---

## 2. Structure

The talk is a tree. It maps onto Beamer's `\part` / `\section` / `\subsection`, and the footer breadcrumb and overview slide are generated from it.

```
Opening                                      7 min
├── Navier–Stokes                (hook)
├── An emerging paradigm         (it didn't come from nowhere)
└── Math 2.0                     (thesis + overview)
Part I: Society                             15 min
├── Rampant AI use               (the fact: use is exploding, mostly undisclosed, review overwhelmed)
├── Community response           (each response exposes a problem with the workflow)
└── What formalization fixes     (certificates as remedy; where they stop → three layers, open problems)
Part II: The Lab                            20 min
├── In our field                 (hook: people in our field do this)
├── How it is being done         (tools + cases on a spectrum of human direction)
└── What we can do
    ├── The three layers         (kernel / statement / understanding)
    └── In the lab               (what to hand off, experiments, budget, checklist)
Closing                                      3 min
└── Individual responsibility, full circle, call to action → discussion
```

### Decisions and the reasons behind them
- **The opening is about Navier–Stokes, not the timeline.** One concrete case makes a better hook than a list. The pipeline that made the result possible, and that won it serious attention, is AI plus Lean. The opening argues that this didn't come from nowhere (history of formalization), that it has sped up sharply recently (agent swarms), and then names the paradigm.
- **"The paper and the code disagree" opens nothing.** It moved to the *end* of Part I. Placed right after the thesis, it would undercut it. As the last item in a list of problems, it reads as a complication, and it shows where institutions run out.
- **The two Part I problem branches are "community-level" and "individual-level"**, not "ethical" and "practical". The test is who answers the problem:
  - Institutions answer the community-level problems, and Part I presents their answers: credit, disclosure, confidentiality, review capacity, training, access, narrowing.
  - Individuals have to answer the individual-level ones, and Part II is about those.
- **The boundary between Part I's ethics and Part II's checklist is conduct versus method.**
  - Part I covers conduct: disclosure, credit, confidentiality, students. It also mentions the "rules you are already under".
  - Part II covers method: statement review, reporting every run, pinning model versions.
  - Keep them separate so the checklist doesn't repeat Part I.
- **Argue inevitability from adoption and money, not capability forecasts.** A skeptical audience can dismiss forecasts. Be explicit that the *workflow* is inevitable, not "AI solves everything": Tao says most frontier problems remain unsolved, and FrontierMath Erdős stands at 3/68.
- **The opinion map does real argumentative work.** Its point is that the field agrees AI works and disagrees about consequences (see §4). It is an illustration paired with named voices, not the frame. The questions in `questions_of_interest.md` are about the *field*, not the corpus.
- **Part II goes from description to recommendation.** First "people in our field are doing this", then "how it's being done", then "what we can do". The tool map is the first slide of "how it's being done" rather than its own section.
- **Part names.** "Society" was chosen over "The field": Part I is about the broader mathematical community, not the lab's own field. "Theory / Practice" was dropped because in a deep-learning-theory lab "theory" means learning theory, which sits in Part II.
- **The closing is about individual responsibility.** If you use these tools, keep control of what is generated and keep your own insights; don't give up your perspective to AI. This brings the talk back to "insight scarcity" and Tao's emphasis on understanding. Tone: *use the tools and stay the author*, not *be wary of the tools*.

---

## 3. Slide by slide

Status: ✅ built · ⬜ planned (title and grey planning note only). Minutes are the planning budget.

### Opening (7 min) — `sections/00–02`
| # | Slide | Min | Status | Purpose and content |
|---|---|---|---|---|
| 1 | Title | — | ✅ | |
| 2 | **8 September 2026: Math changes forever** | 1 | ✅ | Collage: OpenAI's blow-up visualization (left), OpenAI's announcement on X, Nature, Technology Desk and Forbes headlines, and the "I wake up" meme (@MozeTech). Sources run up the right edge. Layout chosen by Kyle (version "c2"). |
| 3 | **Why believe it?** | 2 | ✅ | Diagram in three build steps. (1) The usual route: human proof → preprint → peer review → journal → accepted (Clay: +2 years); months to years. (2) OpenAI: 10,000 agents (88 h) → AI-written paper → *peer review skipped* → announced on X (8 Sep) → taken seriously. (3) A **Lean proof** box (kernel-checked, +17 h) appears in peer review's column. Takeaway: "What stood in for peer review: a machine-checked proof." **Open:** Kyle's brief said Lean was "the only reason" people took it seriously; the slide uses the softer line until he decides. |
| 4 | **Timeline: Formalization in the Pre-AI Era** | 1.5 | ✅ | Pre-AI timeline, 1974–2027 on a linear axis, with no takeaway line (Kyle). Three rows each pair a proof that left room for doubt (○) with the formal proof that settled it (■), with the lag as a bar: four colour theorem 1976 → 2005 Coq (29 years); Kepler 1998 → 2014 Flyspeck (16 years; Annals published it "without complete certification from the referees"); Liquid Tensor Experiment Dec 2020 (Scholze: "being 99.9% sure is not enough") → Jul 2022 (19 months). Milestones on the axis: 1977 Landau's *Grundlagen* in Automath, 2012 Feit–Thompson, 2017 Mathlib, 2023 PFR. The AI era is only marked at the right end. Slide 5 covers it with a summary of the AcadMathSci timeline. **Primary sources only.** The full references are in a comment in `sections/01-opener-paradigm.tex`. Dropped as not verifiable from a primary source: the "99% certain" referee quote, Automath's 1968 start, and PFR's "3 weeks". |
| 5 | How fast this is moving | 1 | ⬜ | A summary of the AcadMathSci timeline (Kyle, 2026-11-10). The recent explosion of agent swarms on open problems: Navier–Stokes with 10,000 agents; OpenAI's 719 manuscripts in one day (6 Oct); FLT by Claude agents. |
| 6 | **Math 1.0 and Math 2.0** (deck slide 7) | 1 | ✅ | Tao's 2×2 (light/heavy AI use × weak/strong human understanding: pre-math, misaligned math, Math 1.0, Math 2.0; `images/tao_math20.png`) on the left. Tao's portrait (`images/terry_tao.png`) and his quote on the right: "[Rather than blindly using AI to generate misaligned mathematics,] the more sustainable “Math 2.0” use of AI would be to strengthen all the ways in which human understanding interacts with mathematics." The bracketed lead-in is Kyle's paraphrase, set in grey. A boxed thesis runs along the bottom: "Gracefully navigating the transition to Math 2.0 requires reckoning with societal level issues as well as understanding emerging best practices to capitalize on AI-driven workflows while maintaining scientific integrity." Cited to Tao, *Machine Assisted Proof*, AIM Public Lecture Series, Beckman Auditorium, Caltech, Fri 9 Oct 2026 ([event page](https://www.caltech.edu/campus-life-events/calendar/aim-public-lecture-series-terence-tao-1)). **Open:** the photo has no credit yet. |
| 7 | The rest of this talk (deck slide 8) | 0.5 | ✅ (auto) | Two cards, one per part. Each has a Penn-blue header ("PART I" / Society, "PART II" / The Lab) over its sections, generated with `\tableofcontents[part=…, hideallsubsections]`. Subsections are hidden. |

### Part I: Society (15 min) — `sections/10–12` (reorganized 2026-11-10)
Arc: establish the fact of rampant AI use and its problems → the community response exposes the specific problems with the workflow → what AI-assisted formalization, used correctly, fixes, and the open problems it leaves (hand-off to Part II). This serves the revised thesis: AI-assisted formalization is an essential tool of Math 2.0. The institutions/money slide was removed (Kyle).

| Section | Slide | Min | Status | Purpose and content |
|---|---|---|---|---|
| Rampant AI use | **The Poison Fountain** | 1.5 | ✅ | Chart of the monthly share of arXiv math preprints, Jan 2025–Oct 2026: acknowledge AI use (Epoch, 0.4% → 48%); read as AI-written but not disclosed (Martin, 17.5%); AI used for formalization (Epoch, 1.9%). Four numbered claims: use is exploding; much is undisclosed; few certify; review is overwhelmed. Data and caveats in note 03. |
| Community response | **Proofs and Prompts: A Sentiment Analysis** | 1.5 | draft | Opinion map (`../figures/04_capability_vs_valence.png`) plus two numbers recomputed from `data/dataset.csv` with eda.py's filters: 89% rate AI as capable (125/141); 60 of 75 negative essays still rate it capable. The earlier "only 17% of those lean toward adoption" did **not** reproduce (13 of 46 with an adoption score, 28%), so it is not on the slide. |
| | **Proofs and Prompts: What Each Cluster Writes About** | 1 | draft | Cluster scatter (`../figures/08_clusters.png`, labelled with each cluster's name, size and centre) beside the word clouds stacked top to bottom (`../figures/09_wordclouds.png`, 2:3), both full height. The on-slide method strip and naming note were removed (Kyle, 2026-11-10); the method is kept in the frame's comments for questions. Method (cluster.py, reviewed 2026-11-10): (1) **embed**: an LLM scores each essay on seven semantic dimensions (rubric.py), an interpretable embedding; (2) **cluster**: k-means, k=3, on two standardised coordinates, capability and valence (mean of understanding, community, adoption, overall); 141 essays, silhouette 0.43, bootstrap ARI median 0.91 (k=2: 0.40/0.84; k=4: 0.41/0.83); (3) **name**: rule on the centres (`name_cluster`: capability ≥ 0.4 → capable; valence > 0.15 positive, < −0.15 negative). The "AI doubted" centre is at capability +0.04, so it is neutral rather than doubting; the slide no longer says so in words, but the plot shows the centre (+0.04, −0.36); (4) **describe**: per-cluster log-odds of a term appearing in a post, z ≥ 2, in ≥ 5 posts, with hand-curated generic words removed. Interpretive captions were removed (Kyle). |
| | **Credit, disclosure and confidentiality** | 2 | draft | Table: problem / case / response / status. Credit (Aletheia 8 of 13; Kolda's "scrapple") → Leiden; priority (Navier–Stokes dispute) → AGMAI, labs withheld prompts; disclosure (1 in 6 undisclosed; ICML 22.5%) → statements, SIAM v2.0; confidentiality (referee uploads) → LMS misconduct, SIAM "non-delegation of scholarly judgement". |
| | **Review capacity** | 1.5 | draft | Volume (+75%; prolific tail) → arXiv cap, STOC 2027 limit; referees (six journals paused) → pauses, paid AI-assisted refereeing proposals; AI reviewing (ICLR 21%) → automated screening; bypassed review → Leiden/AGMAI, Palomar, Guo's Lean journal. |
| | **Training, access and narrowing** | 1.5 | draft | Bastani (−17%); Springer Nature (11% funded), Navier–Stokes £4.9M; Hao (−4.6% topics, −22% engagement) → vivas, token costs on grants, SAIR, reward understanding. |
| What formalization fixes | **AI-assisted formalization** | 2 | draft | Introduces the concept (non-table, Kyle). One-sentence definition; pipeline: statement & blueprint (human) → formalize & prove (AI agents) → kernel check (Lean) → certificate (registry, e.g. Palomar), with a dashed loop for the human statement check. Two columns. *What it addresses*: review capacity, undisclosed AI, bypassed review, credit. *What stays open*: statement fidelity, understanding, significance and ideas, access and coverage. Replaces the earlier problem/certificate table. |
| | **The paper and the code disagree** | 1.5 | draft | Navier–Stokes m+4 vs m+5, pressure bound by a different route; OpenAI audit (≈210 consistent, 21 "(Lean)" not formalized, 5 lemma-only, none false). Quote: "Lean acceptance (compilation) of translation does not imply semantic preservation." |
| | **Three layers of checking** | 2 | draft | Kernel (in place) / statement (open) / understanding (open). Layers 2 and 3 are the open problems for AI-assisted formalization → Part II. |

### Part II: The Lab (20 min) — `sections/20–23`
| Slide | Min | Purpose and content |
|---|---|---|
| Formalization reaches learning theory | 1.5 | The hook: StatsMLlib (about 64.7k lines, 0 sorries), TorchLean, LeanCert, PhysLib, CSLib. **Research gap:** how much Lean has actually affected DL theory (Q15), and which ML-theory groups invest in it (Q17). If the honest answer is "very little so far", frame it as "it's starting, and there's room for us". |
| No verifier, no flywheel | 1 | Why pure math moved first, and where deep learning theory sits. |
| The tools | 1 | One layered map: copilot (LeanCopilot, lean-lsp-mcp) → project (leanblueprint, LeanArchitect, Prove2Me) → engine (Aristotle, Gauss, AxiomProver, Open Math Model) → library (Mathlib, Tau Ceti, StatsMLlib). Note 02 has the details. |
| A spectrum of human direction | 1 | From fully automatic to human-led (Q19), one real case per point: |
| Fully automatic | 1 | Navier–Stokes; the 719-manuscript release. |
| Agents on a human roadmap | 1 | FLT (agents finished a formalization built on Buzzard's project). |
| AI filling a human blueprint | 1 | Sphere packing with Gauss (Math, Inc.), built on a human blueprint. |
| Human-led, AI-assisted | 1 | Armstrong–Kempe (De Giorgi–Nash–Moser in Lean, Apr 2026); StatsMLlib if its provenance can be established. |
| Running example | 1 | **Needed from Kyle:** a lemma from the lab's own work, carried through all three layers. |
| Kernel: reading a Lean file | 2 | `sorry`, axioms, `native_decide`, junk values (`sInf ∅ = 0`). The Collatz exploit: Ramana Kumar deliberately built a false "proof" through a kernel bug, fixed in nightly-2026-07-29. Pinned toolchains; Comparator. |
| Statement: humans own the statements | 2.5 | Write and review statements yourself and let the machine fill in proofs. Navier–Stokes drift as the worked example. Kontorovich: never solved purely in software. |
| Understanding: blueprints and hand-picked lemmas | 2 | Human-facing narrative over a machine-built proof (Q7: does the formal proof need to match the written one?). |
| What to hand to AI | 1 | The convex hull (AI is strongest at recombining existing techniques; Yue et al., to verify); what stays human: framing, definitions, taste. |
| Experiments and applied work | 1 | Code, tests and validation as the certificate (Q4, Q6). The formal proof covers the deduction, not the modelling. |
| Budget | 1 | A heavy user costs about £1,000–5,200 a year on APIs, or £905–4,527 on subscriptions; a shared node about £750 per heavy user a year. Plan for top-tier prices (AcadMathSci report, App. B). |
| Checklist | 1 | Each item tied to a layer. Method, not conduct. |

### Closing (3 min) — `sections/30`
| Slide | Min | Purpose and content |
|---|---|---|
| Where this leaves us | 0.5 | You now know (a) what's coming and (b) how to take part. |
| Proof abundance, insight scarcity | 1 | Full circle: show the opening collage again. Certificates make proofs abundant; no certificate says what a theorem *means*. Insight lives in individuals. |
| Stay the author | 1 | Keep control of what's generated; keep your own insights; don't give up your perspective. Anchors: the convex hull (individual angles get you outside it), narrowing (Hao), deskilling (Bastani), SIAM's "non-delegation of scholarly judgement". |
| A call to action | 0.5 | A few personal commitments, about stance rather than method. For example: write your own statements and blueprint; write your idea down before you prompt; work without the tool regularly. |
| Discussion | — | Prompts to open the 15 minutes (`questions_of_interest.md` has good candidates, e.g. Q7 and Q11). |

Backup (`sections/99`): corpus and scoring method (LLM-scored, one self-selected essay corpus), spare material, references.

---

## 4. Facts that need care

Keep these accurate on any slide:

- **Navier–Stokes is the *forced* problem** (blow-up with a smooth external force). Whether that counts under the Clay problem statement is **unresolved in our notes**. Note 04 says the Clay criteria don't cover forcing and that OpenAI pledged not to claim the prize; the AcadMathSci report calls it a claimed solution. Fefferman's breakdown options do allow a force under decay conditions. Settle this before showing the headlines. The headlines on slide 2 say "Millennium Prize".
- **Not peer reviewed.** The Clay Institute calls its process "deliberately unhurried". Bastounis–Circelli–Hansen do **not** claim the paper is wrong, and they did not check the top-level Lean statement line by line. **The opening's argument depends on that statement being faithful. Verify it.**
- **Credit.** The forcing approach builds on Córdoba & Martínez-Zoroa and Buckmaster & Alpöge; there is a priority dispute. Plausibility came from that human work. The certificate replaced peer review.
- **Numbers.** 10,000 agents, 88 h, about 130B output tokens, Lean in a further 17 h, about £4.9M estimated (AcadMathSci report, A.2 / B.1). The diagram says "88 + 17 hours of compute", deliberately not elapsed time.
- **"Clay: +2 years"** on slide 3 is from memory of Clay's rules: publication in a qualifying refereed outlet, then at least 2 years, plus general acceptance. Check against the published rules.
- **The AcadMathSci report** (Reisinger et al., *The Mathematical Sciences in an AI-enabled World*, Academy for the Mathematical Sciences, UK, pre-publication draft, 28 Oct 2026). Cite it as **AcadMathSci, not "AMS"**. Its AI declaration says Claude produced its timeline and appendices. Known issues:
  - the 12 Jun "frontier models suspended" entry is unverified;
  - the Jacobian counterexample is attributed inconsistently (Alpöge vs Buzzard);
  - its timeline stops on 29 Oct, before CFSG, Stacks and Z-in-Q.

  Review in note 06. Local copy: `~/Zotero/storage/7MDTEDEM/`; Figure 1 (the timeline) is on PDF page 9.
- **Collatz.** Ramana Kumar built the exploit **deliberately, by hand**. The report's table of "AI failure modes" could suggest an AI caused it. It didn't.
- **Opinion-map statistics** come from the Proofs & Prompts essay corpus (152 essays analysed, 141 addressing capability), scored by an LLM. Treat them as illustration, with caveats.

### Still to verify before the talk
- [ ] Faithfulness of the top-level Lean statement for Navier–Stokes
- [ ] Whether forced blow-up counts under the Clay problem statement
- [ ] Clay "+2 years" rule wording
- [ ] Forbes article date (slide 2 credit has none)
- [ ] Yue et al. (NeurIPS 2025), before using the convex-hull mechanism
- [ ] Q15 / Q17 research for the learning-theory hook
- [ ] Exact Tao quotes, from his slides or blog
- [ ] Each research note's own "Still to verify" list

---

## 5. Where the material lives

| Path | What |
|---|---|
| `../questions_of_interest.md` | Kyle's running list of questions the talk should address (Q1–Q19+). |
| `../research/01-formalization-landmarks.md` | Three layers; timeline of formalizations; CFSG, Stacks, Z-in-Q; OpenAI release audit; Navier–Stokes "lost in translation". |
| `../research/02-ai-math-tools.md` | The tool landscape (LeanCopilot, blueprints, Prove2Me, Comparator, Palomar, engines, libraries, Open Math Model); the Collatz kernel bug. |
| `../research/03-publishing-crisis.md` | arXiv and journal data; bottlenecks; five response strategies; how formalization helps and where it doesn't. |
| `../research/04-applied-engineering-views.md` | Applied, engineering, statistics and TCS views; the Navier–Stokes flashpoint. |
| `../research/05-applied-ai-proofs-and-formalization.md` | Four proof modes (informal AI / AI + Lean / computer-assisted / formally verified computer-assisted); applied reading list. |
| `../research/06-acadmathsci-report-review.md` | The AcadMathSci report: facts by question, costs, quotes, inconsistencies. |
| `../figures/` | Corpus figures: `04_capability_vs_valence.png` (opinion map), `09_wordclouds*.png`, `10_field_group.png`. |
| `images/announcement_images/` | Kyle's original images for slide 2 (unmodified). |
| `images/blowup_transparent.png` | Background-removed copy of `blowup.png`, used on slide 2. |

---

## 6. The Beamer project

### Build
```bash
latexmk main.tex
```
XeLaTeX via `.latexmkrc`; output in `build/main.pdf`. Overlays and `remember picture` need two passes, which latexmk handles. On Overleaf, set the compiler to XeLaTeX or LuaLaTeX.

### Files
- `main.tex`: preamble (TikZ libraries, diagram and collage styles, `\stub`), title data, part names (`\partnameone` = Society, `\partnametwo` = The Lab), the part/section order with minute budgets.
- `sections/NN-*.tex`: one file per section or subsection. The first digit is the part: 0 opening, 1 Part I, 2 Part II, 3 closing, 99 backup. Reorder the talk by reordering `\input` lines.
- `sections/00-opening.tex` is a **stray file**, not included in the build (one frame, "The Navier Stokes Moment"). Delete it or reuse the title.
- `beamerthemevidal.sty`, `slide_formats/*.tex`: our modified copy of the lab template. `../vidal-lab-beamer` is untouched; changes are listed in `README.md`.

### Page geometry (16 cm × 9 cm; set in `slide_formats/content_slide.tex`)
- Title band 0–1.24 cm, title text vertically centred at 0.62 cm, 15 pt, starting 0.35 cm from the left.
- Colour line at 1.24 cm, 95% of the page width.
- **Body: 1.66 cm to 8.44 cm from the top (6.78 cm tall); margins 0.35 cm left, 0.70 cm right; text width 14.95 cm.** The body is not centred on the page: a figure centred in the text width sits 0.175 cm left of the page centre.
- Footer: the bottom 0.56 cm (two lines of footer text), with a hairline on top running from the left edge to the logo; one line centred in it: author | short title | breadcrumb (part in Penn red › section › subsection) … slide number | Penn logo (0.42 cm tall).
- Source credits: a strip about 0.42 cm from the right edge, running bottom to top.

### Macros and styles
| Name | Use |
|---|---|
| `\stub{min}{purpose}` | Grey planning note. `\stubsfalse` in `main.tex` hides all of them. |
| `\sectionslide{Part I}{Society}` / `\sectionslide{}{Closing}` | Divider slide; the title is vertically centred on the page, with the label just above it. |
| `\slidesources{...}` | Source credits for a slide (use inside the frame). |
| `collagecard` | TikZ node style: image on a white mat, thin border, soft shadow. |
| `stage[=colour]`, `flow[=colour]`, `lane=colour`, `colhead`, `note`, `span` | Diagram styles (boxes, arrows, row labels, column headers, small notes, brackets). |
| Colours | `PennRed` (153,0,0), `PennBlue` (1,31,91), `PennGold`, `PennGreen`, `vidalfootrule`. |

### Conventions for figures (learned the hard way)
- **Centring:** a full-width TikZ figure centres on the page only if its `\useasboundingbox` matches its *visible* extent. Measure the render, then tighten the box. Keep the box height ≤ 6.78 cm.
- **Fixed bounding box for overlays,** so content doesn't jump between build steps.
- **Styles with `#1` must be defined in the preamble,** not inside a frame (Beamer rejects them there).
- **Build steps** use `\onslide<n->{...}` / `\only<n>{...}` inside the TikZ picture.
- **Fonts:** Open Sans (sans) and Georgia (serif). `\textrangle` is missing from Open Sans; use `\guilsinglright` (›).
- **In TikZ, write explicit lengths** (e.g. `\def\x{0.62cm}`) rather than `\dimexpr` arithmetic inside shift options, which TikZ can misparse.
- **Treat derived images as copies.** Keep originals in `images/announcement_images/` untouched.
- **Credits:** use `\slidesources` on any slide with external images or numbers.

---

## 7. Working preferences (for whoever helps next)

- Questions in `questions_of_interest.md` are about **the field's consensus**: answer from primary writing (named authors, society statements, papers). Use the corpus only as a side source.
- Every claim on a slide needs a source and a reliability tag (self-reported / secondary / independent / unverified). Quote people from primary sources.
- Template changes go in the template files, not individual slides.
- Kyle iterates on structure in conversation before committing. Propose, explain trade-offs, then apply.
