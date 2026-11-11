# talk-v2: what changed from talk/

*Second restructure, 2026-11-11. `talk/` is untouched. Build with `latexmk main.tex` here; the PDF is `build/main.pdf`. Compare with `../talk/build/main.pdf`. A snapshot of the first talk-v2 (2026-11-10) is not kept in the project; its Part I slides are in this deck's backup, unchanged.*

Part I now lets the community and the data speak, and ends on formalization and its three layers. Part II carries Kyle's own argument and how it meets the tools. `REFERENCE.md` in this folder is still the original's and does not describe this version.

## AI use disclosure

A new slide right after the title (Kyle, 2026-11-11): "This presentation was prepared with the assistance of Claude Opus 5.5". It is the first frame of the Opening part, defined in main.tex. It has no title band (the frame has no title) and a robot icon (`\faRobot`, fontawesome5) above the box.

## Thesis (Math 1.0 and Math 2.0 slide)

Kyle's wording, with one typo fixed ("Adimst" → "Amidst"):

> Amidst the plethora of ethical concerns surrounding proliferation and normalization of the technology, AI is ushering in a new dominant paradigm for mathematical, and more broadly theoretical, research. Thoughtfully deployed, AI-assisted formalization tools will be the glue between human and machine understanding which ensures the integrity and alignment of future scientific enterprise.

The rest of the opening is unchanged, except that the overview cards on *The rest of this talk* are taller to fit Part I's five sections.

## Part I: Society

| Section | Slide | Source |
|---|---|---|
| How mathematicians are reacting | Proofs and Prompts: A Sentiment Analysis | From backup; adds the site's logo and a short description (About page, our crawl) |
| | Proofs and Prompts: What Each Cluster Writes About | Unchanged (was in backup) |
| Open Societal Problems | The Poison Fountain | "1 in 6" now cited inline and in the sources: K. Martin, *AI use in arXiv mathematics papers* (3 Nov 2026; 17.5% of Oct 2026 math preprints) |
| | Credit and careers | **New table.** Credit and priority rows from *Credit, disclosure and confidentiality*; new rows for paper mills (post 1043) and careers (post 1893; AcadMathSci hiring responses) |
| | Understanding | **New table.** Deskilling and narrowing rows from *Training, access and narrowing*; new row on opaque output (Hairer, Moshkovitz) |
| | Ongoing, without clear solutions | **New bridge.** Ten problems with their status (none in place), then formalization as the one benefit raised in every cluster: 36%, 27% and 29% of each cluster's essays discuss it (47 of 152) |
| The remedy both sides accept | Formalization is universally acknowledged | Was *Even the critics accept it*; verbatim quotes from all three clusters, then the pushback |
| | AI-Assisted Formalization in Practice | Was *AI-assisted formalization*; pipeline plus four tiles of what is being built |
| | Cheap, and it catches errors | Time chart compressed; **cost data added**: about $200 a page for a 500-page textbook (Meta, arXiv 2604.03071), £91–226k for FLT (AcadMathSci estimate), 5–10× cheaper a year for fixed capability |
| | No verifier, no flywheel | Bottom line replaced by a key box: "Where formalization lies, AI-driven gains follow." |
| What formalization must preserve | But when can it be trusted? | Was *Three layers of checking*; three criteria laid out horizontally (validity, statement fidelity, proof fidelity) under Kyle's top line |
| | Autoformalization has failed us before | Was *Where each layer broke*; column headers renamed to the three criteria |
| What certificates settle | What certificates settle, and what they don't | Status and "taken up" columns removed; ends on a key box: "What does a principled deployment of Math 2.0 look like?" |

A shared `keybox` TikZ style (main.tex) draws the emphasized boxes, matching the thesis box.

**Moved to backup, unchanged:** Checking did not scale · Who wrote it? · What institutions tried · Formalization got cheap · Certificates catch what review missed · The paper and the code disagree · Credit, disclosure and confidentiality · Training, access and narrowing.

## Part II: The Lab

| Section | Slide | Status |
|---|---|---|
| Tools and workflow | The stack | **Built.** Five kinds of tool (plan, coordinate, prove, check, publish) over the libraries, and one box on learning theory: SLT (Dudley's entropy integral, Gaussian log-Sobolev and Efron–Stein, Hanson–Wright, matrix Bernstein, Davis–Kahan, minimax rates for ℓ1 regression), StatsMLlib (topic areas), lean-rademacher, CvxLean. This is the talk's only ML-specific slide |
| | The naive workflow | **Built.** Replaces *In and around learning theory*. Human and machine lanes (state, prove, explain, revise, re-prove, repeat); why it goes wrong; Prove2Me's figure that attempts without a dependency graph gave about 7% of FLT's final lines; key box |
| | Blueprints | **Built.** Bullets on the left answer the naive workflow (a dependency graph instead of one statement and one proof; agree on statements first; a revision touches one node), with the key box "Agree node by node, not theorem by theorem." Right: a four-node blueprint for Euclid's theorem drawn in TikZ, and PFR's real graph for scale (`images/pfr_depgraph.png`, from Tao's 18 Nov 2023 post). `images/pfr_blueprint_page.png` is downloaded but no longer used |
| Statement Fidelity | The statement as consensus | **Built.** The Euclid graph twice, informal and formal (Mathlib statements), with the square on nodes 2 → 3 highlighted: translate then follow, or follow then translate, and you reach the same statement. The boxed remark is the Navier–Stokes case: comparing the graphs node by node points to the lemma that drifted (m+5 vs m+4). Retitled by Kyle *The statement as the unit of consensus* |
| | Translating statements, both ways | **Built.** Words ⇄ Lean diagram (autoformalize / back-translate; Prove2Me and Palomar checks). Left: how reliable (audit ~210 of 245 consistent; Baker's <1% estimate; DriftBench: LLM judge catches 63% of planted mistranslations, best method 90%, preprint; undecidable in general; OEIS and Erdős #124). Right: four Lean conventions a fluent translation can hide. Key box, centered on one line: "Learn enough Lean to read your own statements." |
| Proof Fidelity | Where formal proofs come from | **Built.** Two routes side by side. From the statement alone: AlphaProof Nexus (9/353 open Erdős, 44/492 OEIS), Navier–Stokes about 130B tokens. From a written proof: FLT 11 days and about 6B tokens, CFSG 24 days from 715 sources, a 500-page textbook in a week, sphere packing on a blueprint. Like for like: Draft, Sketch, Prove (20.9% → 39.3%) and DeepSeek-Prover-V2's subgoal decomposition. Key box: "A written proof is still the cheapest route to a formal one." |
| | Decomposing the proof into interpretable lemmas | **Built.** Diagram: a theorem with dependencies A, B, C and one long proof decomposes into Lemma 1 (inherits A, B) and Lemma 2 (inherits B), with the theorem keeping C; proofs drawn as small dark blocks, kernel-checked and unread. Below: when to split a node; who chooses the lemmas (the back and forth; no tool yet chooses interpretable lemmas). Key box: "The machine can propose the units; you decide whether they tell the story." |
| | Lemmas as the unit of understanding | **Built**, replacing *Sufficient for both*; simplified on Kyle's request. The walkthrough standard as a top line; two columns: we already work this way (the 715 sources of the classification; Stacks cited by tag) and established thinkers (Thurston 1994, Lakatos 1976, Parnas 1972 and Wirth 1971). Lerario removed (a blog post, not an established source). Key box: Part II's conclusion |

No running example: this is not a Lean tutorial (Kyle, 2026-11-11).

**Part II audit fixes (2026-11-11):**
- The first section is renamed *Tools and workflow* (it holds the naive workflow and Blueprints).
- The stack slide ends on a bridge from Part I's criteria: validity is the toolmakers' job; statement fidelity and proof fidelity are ours. The learning-theory box is trimmed to fit.
- The sections *The statement* and *The proof* are renamed *Statement Fidelity* and *Proof Fidelity* (Kyle, replacing the title-row badges briefly added).
- The consensus slide's third bullet is Kyle's definition of alignment: every statement is understood directly by its audience, or supported logically by statements that are.
- The decomposition slide redefines proof fidelity in red: the lemma graph matches, not every line.
- *Where formal proofs come from* ends with a bridge to decomposition (the written proof supplies the lemmas); the like-for-like paragraph is shorter and DeepSeek-Prover-V2 is dropped.
- *Translating statements*: Baker's estimate and the 90% figure are dropped from the reliability bullets.

## Closing

| Slide | Status |
|---|---|
| Summary | **Rewritten** (2026-11-11) as five one-line steps grouped by part. Society: a new norm with open problems; one remedy every camp accepts; three criteria for trust. The Lab: blueprints, not chat; lemmas are the unit of understanding. Key box: the thesis's "glue between human and machine understanding". Kyle's earlier bullets are kept in the source comments |
| Open problems and future directions | **Built.** Left, open for the field: credit and careers, access and cost (11% funded), coverage (thin libraries in PDE and applied probability), training. Right, research we could do: choosing interpretable lemmas, checking faithfulness (LLM judge 63%, preprint), formalizing learning theory, verified code. Key box |
| A call to action | **Built**, merging *Stay the author*. Three commitments (own the statement; let the machine prove, then check what compiled; keep your perspective, with Bastani and Hao as evidence) and Kyle's sentence in the key box |
| Resources | **Built**, replacing *Discussion*. A QR code to `RESOURCES.md` in the slides' public repository, beside a grouped list. Until `\resourcesurl` is set in main.tex, a placeholder is drawn instead of a code |

`RESOURCES.md` (new, in this folder) holds every link, each checked on 2026-11-11.

## Full pass (2026-11-11)

Fixed in this pass:
- *Lemmas as the unit of understanding*: the third practice bullet no longer runs into the key box; full stop added.
- Part I scorecard: the row "Understanding the proof" is now "Proof fidelity", matching the three criteria, with "or follow a different argument" added.
- *Translating statements*: Baker removed from the sources (no longer on the slide).
- Thesis box: no hyphenation ("un-derstanding" gone).
- Closing slides: the footer read "Closing › Closing"; the redundant `\section{Closing}` is removed, so it reads "Closing".

Flagged for Kyle, not changed:
- *Autoformalization has failed us before*: the validity column is the Collatz exploit, a deliberately built kernel attack, not autoformalization.
- Section name "The remedy both sides accept" against three clusters and "every camp" on the summary.
- Part names: the overview cards say "In Society" / "In The Lab"; the dividers and summary say "Society" / "The Lab".
- OpenAI release counts: the timeline says 719 manuscripts with three withdrawn the next day; AcadMathSci reconciles this as 722 released, 3 withdrawn, 719 remaining. *Cheap, and it catches errors* says "within days".
- The hook's line "Lean verification, not merely OpenAI's reputation, made the community take this seriously" is still unsourced; Part I later shows that same Lean statement drifting from the paper.
- Currencies are mixed (£ for the FLT estimate, $ elsewhere).
- The QR code on *Resources* is a placeholder until `\resourcesurl` is set.

## Round of corrections (2026-11-11, after the full pass)

- **Sections renamed.** Part I: *Public reactions to Math 2.0* · *Open Societal Problems* · *Formalization* (now holding the former "remedy" and "must preserve" sections) · *The Limits of Formalization*. Part II: *Tools and workflow* · **The Lean Blueprint** (new, holding only *Blueprints*) · *Statement Fidelity* · *Proof Fidelity*.
- **Retitled:** *Formal verification has advocates in all three groups* (was *Formalization is universally acknowledged*; the summary line uses the same words) and *Formal certificates have failed us before* (was *Autoformalization…*).
- **OpenAI counts:** the October timeline now says 722 manuscripts released, three withdrawn within a day, leaving 719 in 372 result families; *Cheap, and it catches errors* says "within a day".
- **Animation:** both *AI Transforms the Mathematical Sciences* timelines start with the axis and legend, then add one event per click in date order (13 and 11 clicks). The thesis box on *Math 1.0 and Math 2.0* appears on the second click. The PDF now has 75 pages because of the overlays; the slide numbers are unchanged.
- **But when can it be trusted?** shows only each criterion's name and question; statuses and remarks removed.
- **The stack:** pipeline boxes have equal heights and no text spills; the learning-theory box is roomier; the closing remark on the criteria is removed.
- **Blueprints:** the Euclid graph is tighter and the PFR graph is larger, filling the space beneath it.
- **Euclid node 2** now reads "Every positive m ≤ n divides n!" on both slides (Lean's version needs 0 < m). A speaker note in the consensus slide's source suggests asking the room what goes wrong without "positive".

## Timing

| Part | talk/ | talk-v2 |
|---|---|---|
| Opening | 7 min | 7 min |
| Part I | 15 min | 16.5 min, 13 slides |
| Part II | 20 min | 17.5 min, 8 slides (3 built) |
| Closing | 3 min | 3 min |
| **Total** | 45 min | **44 min**: 1 min unallocated |

## Claims still to check

- **Cost figures**: Meta's $100k / $200 a page is the paper's own figure; the FLT cost is AcadMathSci's estimate (output tokens at list price), not Anthropic's; 5–10× a year is AcadMathSci citing Gundlach et al. (arXiv 2511.23455).
- **Statuses on the bridge slide** for volume, undisclosed AI and overwhelmed review are my judgement from the Poison Fountain evidence; the rest come from the two tables.
- **Corpus quotes** are verbatim from `data/posts.jsonl`. Ellipses: Weinberger drops "an idea that has taken millennia to refine,"; Dolores-Cuenca, Weinberger and Nesterov start mid-sentence.
- **Stiegler** reports the goal of friends who work on Lean, not Lean's official aims; the slide says so.
- **Moshkovitz** and **Hairer** on the Understanding slide are secondary wording (notes 03 and 05).
- **Paper mills** row rests on one corpus essay (Dolores-Cuenca); no documented case yet.
- **Scooping by an AI-generated paper** is anecdotal in AcadMathSci (§3.4).
- **Guo's journal**: name, editors and launch date still unknown (note 03).
- **Collatz exploit**: the "fixed about an hour after" timing is from note 02 (issue #14576, PR #14577).
- **FLT "likely far longer than necessary"** is AcadMathSci's phrase (A.2); the 13M line count is self-reported.
- **11% institutional funding** is a Springer Nature survey cited through AcadMathSci.
- Unchanged from before: the Leiden Declaration's text (confirm it does not discuss formal verification), the "no effect" study of journal AI policies (now in backup), the primary source for the OpenAI withdrawals, and the hook's open items.
- **Lemmas as the unit of understanding**: Thurston and Lakatos are paraphrased, not quoted; check the wording against *On proof and progress in mathematics* and *Proofs and Refutations* before presenting.
- **Where formal proofs come from**: the two token counts are AcadMathSci estimates for different problems (a discovery and a formalization), so they illustrate rather than compare; Draft, Sketch, Prove's 20.9% → 39.3% is from its abstract and used Isabelle, not Lean; "works best on short, self-contained problems" is my reading of AlphaProof Nexus's results.
- **DriftBench numbers** (Mohammad & Sheikh, *The Faithfulness Gap*, arXiv 2606.16541) are from the abstract of a preprint with planted drift, not a base rate of real mistranslations.
- **StatsMLlib's named results**: its site lists 666 theorems but I could not read the theorem list, so the stack slide gives its topic areas only.
- **Learning-theory libraries** (Kyle, 2026-11-11): SLT, github.com/YuanheZ/lean-stat-learning-theory (Zhang, Lee & Liu, AI4SLT, arXiv 2602.02285, ICML 2026; sorry-free; built with Claude Code and Codex, humans designing the proof strategies); CvxLean, github.com/verified-optimization/CvxLean (Bentkamp, Fernández Mir & Avigad, TACAS 2023). Details are from the repository pages; read the AI4SLT paper before quoting its numbers.
- **Part II evidence to gather:** *The Faithfulness Gap* (arXiv 2606.16541) and 2026 statement-translation benchmarks; Draft, Sketch, Prove and DeepSeek-Prover-V2 numbers.
