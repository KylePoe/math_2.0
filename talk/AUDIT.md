# Audit: the formalization claim and the deck's argument

*2026-11-10. Covers every frame in `sections/` as built today, `REFERENCE.md`, and research notes 01–06. Slide names are frame titles. Nothing in the deck has been changed.*

The goal stated by Kyle:
- **Part I** drives home that formalization tools are necessary for the future of the mathematical sciences.
- **Part II** gives recommendations for practices and tools, and points to what is already happening in learning theory.

---

## 1. Verdict in brief

1. **The claim holds in a scoped form, and the evidence for it is good.** The defensible version is this. When proofs are abundant and checkers are scarce, a machine-checkable certificate is the only check that scales with production and does not depend on who, or what, wrote the proof. Formal proof is that certificate for deductive mathematics. It is **necessary, not sufficient**.
2. **The unscoped claim overreaches.** "Formalization is necessary for the mathematical sciences" is contradicted by the project's own applied-side evidence (notes 04–05, AcadMathSci). The fix is to argue for **certificates**, with formal proof as the certificate for proofs, rather than for Lean everywhere. This keeps the claim strong across the mathematical sciences, and it is what Part II's experiments slide needs anyway.
3. **The deck does not currently make the argument.** Part I spends more slides on problems formalization doesn't touch, and on what formalization can't do, than on why it is needed. An audience would leave thinking "formalization is limited" rather than "formalization is necessary".
4. **The strongest evidence for necessity is in the notes but not on the slides:**
   - the three withdrawn OpenAI papers were all outside Lean coverage;
   - formalization found errors in CFSG and the Stacks Project that decades of human review missed;
   - the "no verifier, no flywheel" argument, which is made for an ML audience.
5. **Learning theory is almost absent.** It is one stub slide and two unresearched questions (Q15, Q17). Part II's case studies are all pure mathematics.

---

## 2. The claim against the evidence

The claim breaks into five steps. Tags follow the notes: [indep.] independent; [self] self-reported; [report] from the AcadMathSci draft; [unverif.] unverified.

| # | Step | Evidence in the notes | Strength |
|---|---|---|---|
| 1 | **Production of proofs has scaled.** | arXiv math +75% year on year (Sep 2026) [report, confirmed]; disclosed AI use 0.4% → 48% in 21 months (Epoch) [indep.]; 719 manuscripts in one day (note 01 §5) | **Strong** |
| 2 | **Human checking cannot scale with it.** | Six probability journals paused [indep.]; editors can't find referees (anecdotal; the report says no systematic data exist); Mathlib has 65 reviewers for 950 contributors [report, unsourced]; "the bottleneck … is shifting from technical work to expert attention and judgement" (AcadMathSci exec. summary) | **Strong in direction, thin in numbers.** No count of referee declines exists (note 03 §2). |
| 3 | **Provenance can no longer be trusted, so the check must not depend on it.** | 17.5% of math preprints read as AI-written without disclosing it, likely an undercount (Martin) [indep., unpublished rubric]; 22.5% of ICML reviewers used an LLM under a ban [indep.]; AI-writing growth is the same with or without a journal policy [report]; arXiv's ban "welcome but unenforceable" (THE) | **Strong, and underused.** It is the cleanest argument for a provenance-independent check, but the deck presents it as a conduct problem (credit table), not as a reason for certificates. |
| 4 | **Other responses are stopgaps.** | Restrict and disclose are what exists; verify, expand and replace are prototypes (note 03 §4). Caps are "temporary", pauses ended 9 Nov, disclosure is ignored. | **Moderate.** This is an inference from the pattern of responses, not a measured failure. |
| 5 | **Formal certificates work as the check.** | *Pre-AI:* four colour, Kepler and LTE: formal proof settled doubt (slide 4) [primary]. *AI era:* the 3 withdrawn OpenAI papers were **all outside Lean coverage**; the community audit found no Lean-covered theorem false (note 01 §5) [indep., small n]; CFSG found 34 deviations including a false equality [self, not reproduced]; Stacks found dozens of statements false in stated generality [self]. *Institutions:* AcadMathSci recommends assessing correctness "utilising AI and formalisation" separately from significance and understanding; Palomar; Guo's Lean journal; the Kothari–Meka–Raghavendra STOC track proposal | **Strong for deductive mathematics.** The AI-era scale claims (FLT 13M lines, CFSG 43M) are self-reported. Use them for speed, not as proof of reliability. |

**What limits the claim** (all from the notes; the talk should concede these openly):
- **Not sufficient.** The formal statement can drift from the paper: Navier–Stokes needed m+5 derivatives where the paper had m+4; OpenAI had 21 "(Lean)" links with nothing formalized. Machine proofs explain nothing. The kernel can be exploited (Collatz). Most of this is already on the slides.
- **Not available everywhere.**
  - PDE's first major Lean theorem came only in April 2026 (Armstrong–Kempe).
  - ICIAM's statement does not mention formal proof.
  - A Lean proof is not DO-178C certification evidence.
  - The report sees "a growing divide between mathematics that is readily formalisable and mathematics that is not".
- **The formal community is divided.** Mathlib "reportedly" does not accept AI formalizations [report, unverified]. Tau Ceti, which is AI-built, is now larger than Mathlib.
- **Adoption is tiny.** 1.9% of math preprints acknowledge AI for formalization; about 1% mention Lean in the abstract. This supports "there is a gap", not "it is necessary". Present it as the gap the talk wants closed.

**The defensible thesis, in one sentence:**
> When proofs are abundant, machine-checkable certificates are the only check that scales with production and ignores provenance. For proofs, that certificate is a formal proof: necessary, though not sufficient.

### Reading forward (added after Kyle's reply)

Kyle's framing: AI will keep getting better, and making formalization a **standard step in research** benefits both **individual productivity** and **scientific integrity**. Assessed against the evidence:

- **It doesn't need a capability forecast.** `REFERENCE.md` §2 chose to avoid forecasts with a skeptical audience. The argument needs only that generation keeps getting cheaper relative to human checking, and that is already observed:
  - production +75% while referees are fixed;
  - fixed capability gets about 5–10× cheaper a year (AcadMathSci App. B) [report].

  Under any trajectory where AI improves, the gap widens. If AI stalls, the productivity benefit still stands. State it as a dominance argument, not a prediction.
- **Integrity: well supported.** This is the §2 chain: a provenance-independent check, plus auditability. Bastounis–Circelli–Hansen could point to exact lemmas because formal code existed.
- **Productivity: supported by mechanism, thin on direct evidence.**
  - *Mechanism:* a verifier lets you delegate without reading every line. You own the statement and the machine owns the proof.
  - *Evidence:*
    - blueprints with a wrong lemma can't prove a correctly stated goal, so review shrinks to statements (Lean Atlas reports a 94–99% cut in nodes needing review; Physlib 69%) [self];
    - formalization itself got fast (Strong PNT in 3 weeks against 18 months; FLT in 11 days) [self];
    - PFR's constant was improved "for free" once the proof was formal;
    - agents use the kernel to check their own work (AcadMathSci §1.2).
  - *Gap:* there is no measured case of a researcher's or lab's research output rising because of formalization. **The lab's own running example is the best possible evidence here**, which raises its priority.
  - *Counterweight to concede:* Mathlib reportedly rejects AI formalizations as fragile and hard to maintain [report, unverified], and in fields with thin libraries (much of learning theory) the up-front cost is higher today. Both are costs that fall as libraries grow; StatsMLlib is the example.
- **"Standard step in research" is a stronger position than "necessary".** It is a recommendation the evidence supports in both parts, and it doesn't have to defend the word "necessary" against the applied-side counterexamples.
- **It fits the deck's structure.** Integrity is a community-level benefit (Part I, Society). Productivity is an individual one (Part II, The Lab). Each part then argues one half of the thesis.

**Candidate thesis with this framing:**
> AI will keep making proofs cheaper. Making formalization a standard step in research is how that abundance raises both productivity and integrity, instead of trading one for the other.

The parallel for applied and experimental work is the one AcadMathSci and Haugen–Stepanenko–Hansen draw: "certify the output, not the process". Code, tests, validated numerics and documented validation play the role that formal proof plays in pure mathematics. That is the generalization Part II's experiments slide needs.

---

## 3. What the deck argues now

Each slide's role relative to the claim. **For** = argues that formalization is necessary. **Limit** = shows what it can't do. **Off-thesis** = neither.

| Section | Slide | Role now |
|---|---|---|
| Opening | September 8, 2026: Math changes forever | Hook |
| | Why believe it? | **For**, but the causal line ("Lean verification, not merely OpenAI's reputation, made the community take this seriously") has no source, and REFERENCE says Kyle hasn't decided on it |
| | Timeline: Formalization in the Pre-AI Era | **For** (formal proof settles doubt). Strong, primary-sourced. |
| | Timeline: AI Transforms the Mathematical Sciences (×2) | **Off-thesis.** About 24 events at 5–6 pt type; most aren't about formalization; contains an unverified entry (12 Jun) |
| | Math 1.0 and Math 2.0 | States a thesis, but the boxed sentence says the transition "will require … developing individual familiarity with … AI-assisted formalization", which is weaker than necessity. Tao's quote is about understanding, and nothing on the slide links it to formalization. |
| Part I | The Poison Fountain | **For** (claims 1, 3 and 4 support steps 1–2) |
| | Proofs and Prompts: A Sentiment Analysis | **Off-thesis** ("the field agrees it works") |
| | Proofs and Prompts: What Each Cluster Writes About | **Off-thesis**, except that the optimist cluster is the one writing about verification |
| | Credit, disclosure and confidentiality | **Off-thesis as framed** (conduct). The disclosure row is step 3 in disguise. |
| | Review capacity | **For** (step 2; caption: "verifying is the structural response") |
| | Training, access and narrowing | **Off-thesis**, and access cuts against the claim |
| | AI-assisted formalization | Half **for**, half **limit** |
| | The paper and the code disagree | **Limit** |
| | Three layers of checking | **Limit** (hand-off to Part II) |
| Part II | 18 stubs | Practice. Learning theory: one stub. Cases: four pure-math stubs. |

**Count for Part I:** about 2.5 slides argue for necessity, about 2.5 show limits, and 4 are off-thesis. That balance is the "unfocused" feeling.

---

## 4. Problems, in order of importance

1. **There is no single, arguable thesis.**
   - `REFERENCE.md` §1 has one thesis ("a coherent, emerging paradigm").
   - The Part I arc has another ("an essential tool of Math 2.0").
   - The boxed thesis has a third ("will require … familiarity").
   - Your stated goal is a fourth ("necessary").

   None is phrased so that Part I can be seen to prove it. Pick one sentence, put it on the Math 2.0 slide, and repeat it at the end of Part I.

2. **Part I is organized as a survey of problems, not as an argument.** Sections run fact → reactions → remedy. The remedy arrives at minute 15, and half of it is about limits. For "necessary", the order should be the steps in §2: production scaled → checking didn't → provenance is unknowable → stopgaps don't hold → certificates do → necessary, not sufficient.

3. **The limits currently read as rebuttal rather than refinement.** "The paper and the code disagree" comes right after the remedy and lands as a counterpoint. The same facts support necessity when framed this way: **the drift could be found only because there was formal code to compare against the paper**, and you cannot line up a paper against a hand-wave. Bastounis–Circelli–Hansen could point to exact lemmas (m+4 against m+5). That precision is what a certificate buys, even when it fails.

4. **The corpus slides take Part I's central time.** Two slides (about 2.5 min) of LLM-scored essays, from one self-selected site, come before any institutional evidence. Your own working rule (REFERENCE §7) is that the corpus is a side source. Their one contact with the thesis is that the optimist cluster's vocabulary is verification vocabulary: formalization appears in 23% of its posts against 7% elsewhere. That is a single line, not two slides.

5. **The opening spends its time on a list.** The two AcadMathSci timeline slides are the "list instead of a case" that REFERENCE §2 decided against. If acceleration is the point, show it with the formalization projects themselves:

   | Project | Era | Time |
   |---|---|---|
   | Odd Order | human | 6 years |
   | LTE | human | 19 months |
   | FLT | AI agents | 11 days [self] |
   | CFSG | AI agents | 24 days [self] |

   That says "the cost of formalization collapsed", which is the premise "necessary" needs: a tool cannot be necessary if it is unaffordable.

6. **The hook's causal claim is unsourced and fragile.**
   - "Lean verification … made the community take this seriously" is the opening's load-bearing line, and it has no source.
   - The top-level Navier–Stokes statement's faithfulness is still on the verify list.
   - Whether forced blow-up counts for the Clay prize is unresolved, yet the collage headlines say "Millennium Prize".

   A skeptical theory audience will test the hook first. Safer: "It came with a Lean proof, and that is why experts could audit it in weeks rather than years", which is sourced by Bastounis–Circelli–Hansen's audit itself.

7. **The forward-looking argument for this audience is missing.** "No verifier, no flywheel" (AcadMathSci A.5): AI improves fastest where a verifier provides reward signal, and Lean is becoming "the means by which AI checks its own work, generating training signal". For a deep-learning theory lab, this is the most persuasive reason formalization is necessary. Fields that can't verify will see uneven AI progress. It is currently a Part II stub. It belongs at the climax of Part I, or as the bridge into Part II. (The convex-hull mechanism behind it, Yue et al., is still on the verify list.)

8. **Learning theory is thin, and Part II's cases don't serve it.** Part II plans five slides on a "spectrum of human direction" with Navier–Stokes, FLT, sphere packing and Armstrong–Kempe. That rehearses Part I's pure-math cases. The material on learning theory today:
   - StatsMLlib: about 64.7k lines, 0 `sorry`; Dudley, McDiarmid, Rademacher complexity, Hanson–Wright. Authors and AI use unknown.
   - TorchLean (neural networks formalized in Lean).
   - Our counts: stat.ML 4 papers a month mention Lean (0.4%); cs.LG hits are mostly papers *about* provers.
   - One concrete paper: "Depth Separation for Neural Networks under Gaussian Measure", with Lean proofs.

   Q15 (impact on DL theory) and Q17 (which groups invest) are unresearched.

9. **Part II has no spine.** It is in-field, then tools, then four cases, then layers, then lab: 18 slides in 20 minutes, with the three layers explained twice (Part I and Part II). Part I's own pipeline slide (statement & blueprint → formalize & prove → kernel check → certificate) is a ready-made spine. One stage per section, each with its tools and practices, answers "recommendations for best practices and tools" directly.

---

## 5. Proposed structure

Times keep the 45-minute budget.

**Opening (6 min)**
1. September 8 collage. Retitle away from "changes forever" if the Clay question stays open.
2. Why believe it? Sourced line as in §4.6.
3. Pre-AI timeline (unchanged).
4. *Replaces both AcadMathSci timelines:* "The cost of formalization collapsed", the projects table from §4.5, with self-reported figures tagged.
5. Math 1.0 and 2.0, with the one-sentence thesis. Bridge Tao's quote to the thesis: Tao himself launched Palomar, a registry of Lean-verified results (18 Aug 2026). Certificates make correctness cheap so human attention can go to understanding, which is his "Math 2.0" use.
6. Overview.

**Part I: the case for certificates, or the integrity half of the thesis (14 min)**
1. *Production scaled*: The Poison Fountain (as is, or trim claims 3–4 into later slides).
2. *Checking didn't*: Review capacity, restricted to volume, referees and bypassed review.
3. *Provenance is unknowable*: the disclosure evidence (17.5% undisclosed, 22.5% ICML non-compliance, policies with no effect) leading to "the check has to ignore who wrote the proof". Built from the disclosure row of the credit table.
4. *What institutions tried*: restrict, disclose, verify as one table with status, compressing the credit and review-capacity tables. Caption: only verification scales.
5. *Certificates work*: the pipeline (from "AI-assisted formalization") plus evidence: withdrawn papers outside Lean, CFSG/Stacks errors [self], LTE.
6. *No verifier, no flywheel*: AI progress goes where verifiers are; why this matters for ML.
7. *Necessary, not sufficient*: "The paper and the code disagree", reframed as in §4.3, then the three layers as hand-off.
8. Optional, one slide at most: the corpus, as "the optimists are the ones writing about verification". Otherwise move the corpus slides to backup.

Move out of Part I:
- training → closing ("stay the author");
- access and cost → Part II budget;
- narrowing → closing (convex hull);
- credit and confidentiality → backup, or one line in "what institutions tried".

**Part II: practice and learning theory, or the productivity half of the thesis (20 min)**
1. *Learning theory is starting*: StatsMLlib, TorchLean, the stat.ML count, one Lean-proved learning-theory paper. Framing: "it's starting, and there's room for us". Needs Q15/Q17 research (§6).
2. *Why learning theory needs this more than it thinks*: its theorems are inequalities with constants and assumptions, exactly where Navier–Stokes drifted (note 05 §6). Certificates and statement discipline together.
3. *Running example* from the lab's own work, carried through the pipeline. Still needed from Kyle; it does the most work in Part II.
4. *The workflow, one stage per slide, each with practices and tools:*
   - **State** (L2): write statements and a blueprint yourself. Tools: leanblueprint, Verso Blueprint, Comparator challenge files.
   - **Prove** (L1): AI fills proofs. Tools: LeanCopilot, lean-lsp-mcp, Aristotle, AXLE, Gauss; StatsMLlib and Mathlib as foundations.
   - **Check** (L1): `#print axioms`, no `sorry` or `native_decide`, a pinned toolchain, re-check with `--trust=0` after soundness advisories (Collatz).
   - **Understand and share** (L3): hand-picked lemmas over a machine backend; register and disclose (Palomar, `formalization.yaml`).
5. *Spectrum of human direction*: one slide, one row per case (replaces five).
6. *Beyond proofs*: tests, validated numerics and documented validation as the certificate for code and experiments. The same principle as Part I, extended to the rest of the mathematical sciences.
7. *Budget and access* (from AcadMathSci App. B, plus the access row moved out of Part I).
8. *Checklist*: one item per pipeline stage.

**Closing (3 min)**: certificates make correctness cheap; that is what frees attention for statements and understanding; stay the author. Training, narrowing and the convex hull land here.

---

## 6. Evidence still needed for this version

| Need | Why | Where to start |
|---|---|---|
| **Q15 / Q17: learning theory and Lean** | Part II's first slide depends on it | StatsMLlib's AUTHORS.md and any paper; the "Depth Separation … Gaussian Measure" paper's authors and group. Leads from my own background, **not yet in the notes and to be verified**: a Lean formalization of Rademacher-complexity generalization bounds (Sonoda et al., 2025); a Lean proof of PAC learnability for decision stumps (Tassarotti et al., CPP 2021); a Coq ML system with verified generalization guarantees (Bagnall & Stewart, AAAI 2019). |
| A source for "Lean is why it was taken seriously" | The hook | Expert reactions from 8–15 Sep, or drop the causal wording (§4.6) |
| Withdrawn OpenAI papers outside Lean coverage | Strongest single AI-era datum for "certificates work" | Note 01 §5 cites redreamality and Wikipedia; find the withdrawal notice itself |
| CFSG / Stacks errors | "Errors humans missed" | Axiom's companion paper on the UGT; an independent build of CFSG (still pending) |
| Yue et al., NeurIPS 2025 | "No verifier, no flywheel" mechanism | Already on the verify list |
| Mathlib's AI policy | Fair statement of the community split | Mathlib's contribution guidelines (the report says "reportedly") |
| Navier–Stokes top-level statement; Clay forcing | Hook | Already on the verify list |
