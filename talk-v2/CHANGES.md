# talk-v2: what changed from talk/

*2026-11-10. A restructured copy of the deck for side-by-side comparison. `talk/` is untouched. Build with `latexmk main.tex` here; the PDF is `build/main.pdf`. Compare with `../talk/build/main.pdf`.*

The restructure follows `../talk/AUDIT.md` §5. Part I now argues the **integrity** half of the thesis as a chain of steps. Part II is re-skeletoned around the **productivity** half, using Part I's pipeline as its spine. `REFERENCE.md` in this folder is still the original's and does not describe this version.

## Thesis (Math 1.0 and Math 2.0 slide)

| talk/ | talk-v2 |
|---|---|
| "…gracefully and ethically navigating the transition to Math 2.0 will require reckoning with societal-level issues as well as developing individual familiarity with the emergent paradigm of AI-assisted formalization." | "AI will keep making proofs cheaper. Making formalization a standard step in research is how that abundance raises both scientific integrity and individual productivity, instead of trading one for the other." |

The rest of the opening is unchanged, including the two AcadMathSci timeline slides and the "Why believe it?" line. The audit's suggestions for those (§4.5, §4.6) are not applied here.

## Part I, slide by slide

| # | talk-v2 section › slide | Step in the argument | Source in talk/ |
|---|---|---|---|
| 1 | Checking did not scale › The Poison Fountain | Production scaled | Unchanged |
| 2 | Checking did not scale › Checking did not scale | Expert checking did not | **New.** The evidence column of *Review capacity*, plus Mathlib's reviewer ratio. Responses moved to slide 4. |
| 3 | Provenance is unknowable › Who wrote it? | Disclosure doesn't hold, so the check must ignore the author | **New.** Built from the disclosure row of *Credit, disclosure and confidentiality*. |
| 4 | Provenance is unknowable › What institutions tried | Restrict and disclose are stopgaps; only verification scales | **New.** The response columns of *Credit…* and *Review capacity*, regrouped by strategy. |
| 5 | Certificates › AI-assisted formalization | The certificate | Unchanged |
| 6 | Certificates › Formalization got cheap | It is affordable | **New.** Log-scale chart pairing human-era and AI-era efforts; AI figures tagged as self-reported. |
| 7 | Certificates › Certificates catch what review missed | It works | **New.** OpenAI withdrawals (all outside Lean coverage), CFSG and Stacks errors. |
| 8 | Certificates › No verifier, no flywheel | It is where AI improves | **New.** Was a Part II stub. |
| 9 | Certificates › The paper and the code disagree | Necessary, not sufficient | One added line: "The drift was found because there was formal code to hold the paper against." |
| 10 | Certificates › Three layers of checking | Hand-off to Part II | Bottom line now reads "Layer 1 makes correctness cheap and auditable. Layers 2 and 3 stay human: Part II." |

**Moved to backup, unchanged:**
- Proofs and Prompts: A Sentiment Analysis
- Proofs and Prompts: What Each Cluster Writes About
- Credit, disclosure and confidentiality
- Training, access and narrowing

Their anchors are now referenced in the Part II budget stub (access) and the closing "Stay the author" stub (deskilling, narrowing).

## Part II and closing (still stubs)

| Section | Stubs |
|---|---|
| Learning theory | Formalization reaches learning theory · Why learning theory needs statement discipline · Running example |
| The workflow | State: you own the statement (L2) · Prove: let the machine fill it in (L1) · Check: read what compiled (L1) · Understand and share (L3) · A spectrum of human direction (one slide instead of five) |
| In the lab | Beyond proofs: code and experiments · Budget and access · Checklist |

Removed from talk/'s plan:
- the four separate case slides, now one spectrum slide;
- "No verifier, no flywheel", now built in Part I;
- the separate "three layers" subsection, now carried by the workflow stages;
- "The tools" as a standalone map, now folded into the stages.

The closing stubs now restate the thesis, and "Stay the author" picks up the deskilling, narrowing and convex-hull anchors.

## Timing

| Part | talk/ | talk-v2 |
|---|---|---|
| Opening | 7 min | 7 min (unchanged) |
| Part I | 15 min, 9 slides | 14.5 min, 10 slides |
| Part II | 20 min, 18 stubs | 19.5 min, 11 stubs |
| Closing | 3 min | 3 min |

## Claims on the new slides that still need checking

- **Mathlib: 65 reviewers for 950 contributors** comes from the AcadMathSci draft, which gives no source. It is marked "(reported)" on the slide.
- **"No effect" of journal AI policies** (5,114 journals, arXiv 2512.06705) is cited through AcadMathSci; read the paper.
- **The three withdrawn OpenAI papers were all outside Lean coverage.** Note 01 cites secondary sources (redreamality, Wikipedia); find the withdrawal notice itself.
- **CFSG and Stacks errors** are Axiom's own reports; CFSG has no independent build yet. Both are tagged on the slide.
- **"Welcome but unenforceable"** is Times Higher Education's headline (May 2026); confirm the wording.
- **AlphaProof: about 1M problems into about 80M Lean statements** is from AcadMathSci A.5.
- **"Experts had checked for 40 years"** (CFSG) is the note's phrasing; soften it if no source says so.
- The hook's open items are unchanged: the Navier–Stokes statement's faithfulness, Clay and forcing, and the causal line on "Why believe it?".
