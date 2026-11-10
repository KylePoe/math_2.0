# AI-generated proofs in applied mathematics: informal proofs, formal proofs, and certified computation

*Research notes for the "Math 2.0" talk. Compiled 2026-11-09. This goes deeper than [04](04-applied-engineering-views.md), which covered institutions and the corpus. Here the focus is **what applied mathematicians have written** about AI-generated proofs, and what changes when a formal proof comes with them.*

The verification layers from note 01 are used throughout:
- **L1, kernel:** the proof assistant accepts the proof.
- **L2, statement fidelity:** the formal statement says what the paper's theorem says.
- **L3, proof fidelity:** the formal proof follows the paper's argument.

---

## 0. Bottom line

Applied mathematicians writing on this in 2026 broadly agree on three points:

1. **An informal AI proof is a lead, not a result.** It has to be checked by an expert. The specific complaints: it is fluent on the easy steps, skims the hard ones, cites unreliably, and is plausible in ways that fail on inspection. This view comes from Hairer, Kolda, Colbrook and Gómez-Serrano.
2. **A formal proof settles whether the deductions are valid, but not much else that applied mathematicians care about.** The open questions it leaves are:
   - whether the formal statement matches the paper (Hansen's group showed the Navier–Stokes formalization proves a weaker inequality);
   - whether the *model* describes reality (verification and validation, V&V);
   - whether anyone understands the proof (Tao: verified but not understood counts as "incomplete").
3. **For most applied analysis, formalization is not yet available.** Mathlib got its first major modern PDE theorem only in April 2026 (Armstrong–Kempe), and a full Navier–Stokes theory is still out of reach. In practice, the applied choice is usually between an **informal AI proof** and an **AI-assisted computer-assisted proof** (interval arithmetic plus a certificate). It is rarely between informal and Lean.

**The applied view in one sentence:** formal proof assures correct deduction, while applied work needs a correct number, a correct model and a correct statement as well, so a Lean certificate is one useful layer of checking and does not settle the result.

---

## 1. Four ways a proof can be produced

Applied mathematics already had a third mode between "informal proof" and "formal proof": the **computer-assisted proof**. Applied practice also has to consider a fourth, where that computation is itself formally verified.

| Mode | What you hold | What is trusted | Typical failure | Applied examples |
|---|---|---|---|---|
| **A. Informal AI proof** | Text | The model, then the referee | Skimmed hard steps; hidden sources; arguments that look complete but aren't | First Proof (Feb 2026); Kolda's problem #10; Colbrook's failed tail argument |
| **B. AI proof with a Lean certificate** | Text plus Lean code | Lean's kernel, Mathlib's definitions, the statement file | **Statement drift**: the formal theorem is weaker or different; agents change the argument until it compiles | OpenAI's Navier–Stokes code (m+5 derivatives where the paper has m+4); note 01 §5 |
| **C. Computer-assisted proof (validated numerics)** | Text plus interval-arithmetic code plus certificate | The numerical code and the arithmetic library | Bugs in the code; floating-point errors; a gap between the analysis and what the code actually checks | Tucker's Lorenz attractor (2002); Hou–Chen Euler blow-up (2022); Gómez-Serrano's work; **AI-assisted:** Colbrook's eigenvalues (2026) |
| **D. Formally verified computer-assisted proof** | Mode C, with the numerics verified in a proof assistant | Only the kernel | Coverage: very few such tools exist | **Immler's Isabelle verification of Tucker's Lorenz proof** (2015–18); Flyspeck (Kepler, 2014); LeanCert (2026, early) |

**Why mode C matters for the talk:** applied mathematics has accepted **proofs no human reads in full** since the 1970s: the Four Colour theorem, Kepler, Lorenz. It also argued about them for decades. It already knows the trust problem that pure math is meeting now: *what exactly is the trusted code, and who checked that the code checks the right thing?*

---

## 2. What applied mathematicians have written about informal AI proofs (mode A)

### Martin Hairer: "strings together known arguments" but "hard to trust"
- Hairer works on stochastic PDE and is a Fields Medallist. He co-led **First Proof** ([arXiv 2602.05192](https://arxiv.org/abs/2602.05192), Feb 2026) with Abouzaid, Blumberg, Kileel, **Kolda**, Nelson, **Spielman**, **Srivastava**, **Ward**, Weinberger and Williams. That is an unusually applied and TCS-heavy author list for this kind of exercise. The project posed **10 unpublished research questions** taken from the authors' own work.
- **Hairer's comments** (NYT interview, Feb 7, 2026; [EPFL repost](https://actu.epfl.ch/news/prof-m-hairer-on-artificial-intelligence-and-mathe)) [secondary wording]:
  - He was impressed that it could chain known arguments and calculations correctly.
  - It gives **a lot of detail on easy steps and skims the hard ones**.
  - **The output is hard to trust.**
  - In his view mathematics remains "quite safe."
- **Failure types reported for First Proof** [secondary summary]: global gluing arguments that failed (symplectic geometry); **false premises about measure equivalence (stochastic analysis)**; an outright admission that it couldn't solve the **numerical linear algebra** problem. One numerical linear algebra result was a success.

### Tamara Kolda: "Human-AI scrapple"
Kolda is SIAM's Vice President for Publications. She wrote [*The Future of Math Research in the Age of AI*](https://siliconreckoner.substack.com/p/the-future-of-math-research-in-the) on the Silicon Reckoner Substack, Feb 21, 2026.
- **What happened with her problem (#10):** both Gemini Deep Research and ChatGPT 5.2 Pro solved it, and each found a published technique missing from her own solution. **Neither cited it.** The two solutions were strikingly similar, which made her suspect a known source, and she had to track it down herself.
- **The term she coined:** **"Human-AI scrapple"**, meaning AI output that humans assemble into research without validating it. As the SIAM officer who handles author-integrity cases, she sees it directly: invented citations, weak arguments, incoherent reasoning.
- **Her quotes:** "AI models cannot reliably provide sources for their knowledge." And: "it is so tempting to accept an AI's output at face value."
- **The applied angle:** her own work turns vague problems from stakeholders into precise mathematical questions. She sees that judgment as the mathematician's core role.
- **What she doesn't discuss:** **formalization.** Her trust model is human validation plus provenance. She also signed the Leiden Declaration.

### Javier Gómez-Serrano: "a proof that nobody understands" isn't helpful
- Gómez-Serrano works on fluids and computer-assisted proofs. He collaborated with DeepMind on **unstable singularities** (2025): physics-informed neural networks found families of singular solutions, with residuals near machine precision. **Turning those into theorems was left to future computer-assisted proofs.** That is mode A or C, not mode B.
- In [Brown's profile, Aug 26, 2026](https://www.brown.edu/news/2026-08-26/javier-gomez-serrano-lab) he says: "I don't think a proof that nobody understands is helpful," and "Humans are not going to be left out of the loop." Any candidate singularity found by AI still needs years of conventional proof.
- **Lean doesn't appear in his account.** His pipeline is neural-network numerics, then interval arithmetic, then a human proof (mode C).
- **A caveat from one summary:** in this work the equations, the self-similar ansatz and the loss function were designed by humans. "The network is the solver."

### Matthew Colbrook: "a number with a proof"
Colbrook works in numerical spectral theory. His paper is [*Ten Digits on a Train: AI-Assisted Verification of Two Eigenvalue Problems*](https://arxiv.org/abs/2606.23821), arXiv, Jun 2026, math.NA.
- **What he certified, to ten digits:** the negative spectrum of a singular Schrödinger operator, and a resonance pair in a non-normal benchmark that hadn't previously been resolved. The tools were verified zero counting, Dirichlet–Neumann bracketing, and a componentwise Krawczyk–Brouwer inclusion.
- **What AI contributed:** fast candidate values and plausible proof strategies. **Several of those strategies failed.** One tail argument looked complete but omitted a componentwise check that a non-uniform polydisc requires. The human caught it.
- **His thesis:** in validated computation the deliverable is "a number with a proof." As generation gets cheaper, **verification, interpretation, attribution and human judgment become more central, not less.**
- **For the talk**, this is the clearest applied paper on the subject. It is mode C with AI assistance, and **no formal proof assistant is involved.**

### Terence Tao's ICM essay (cited here because it frames the distinction)
[*Mathematics in the age of AI*](https://arxiv.org/html/2608.16753v1), arXiv 2608.16753, Aug 2026, based on his ICM 2026 lecture.
- **§6:** a formally verified proof is one "whose correctness no longer depends on the reputation or the diligence of its author."
- **§7, "Proof scarcity and proof abundance":** AI proofs may pile up faster than they can be verified, written up, refereed or made standard. He calls this **"proof indigestion."** Institutions built for scarcity, such as journals, priority and promotion, may work badly under abundance. **This section is directly on the theme of your talk.**
- **§8:** a verified proof that no human can explain "should be viewed as incomplete, even if it has been formally verified." He argues the emphasis should move from generating proofs to digesting them: exposition, refereeing, canonicalization.
- **Applied mathematics** gets only a passing mention: some applications become feasible only once the theory is "fully digested."

---

## 3. What applied mathematicians have written about formalized AI proofs (mode B)

### Bastounis, Circelli & Hansen: "Navier–Stokes lost in translation"
[arXiv 2610.08144](https://arxiv.org/html/2610.08144v1), Oct 2026. Anders Hansen leads Cambridge's group on the foundations of computational mathematics.
- **This is the central applied text on mode B.** They compared OpenAI's Navier–Stokes paper with its Lean code line by line.
  - **Ex. 3.1:** the paper's eq. (8.19) needs m+4 derivatives. The Lean theorem `norm_derivativeWord_inverse_le` assumes m+5 and uses a different series exponent, and the m+5 pattern recurs.
  - **Ex. 3.3:** the paper's pressure-flux bound depends only on B_R. The Lean bound also depends on A_R, and it uses Sobolev embedding into L² instead of Riesz transforms on L^{3/2}, different Hölder exponents, and an interpolation step the paper doesn't have.
- **Their central claim:** "Lean acceptance (compilation) of translation does not imply semantic preservation." An AI can change the meaning to make the proof compile, and a "success if it compiles" criterion **does not check that the original argument survived** (L3).
- **Their theoretical argument:** resolving the ambiguities in mathematical text is, in general, harder than the Halting problem. It has infinite Solvability Complexity Index, Hansen's own hierarchy for classifying computational problems. Translating the Lean back into English doesn't solve this.
- **Recommendations:**
  - Lean-verifying AI formalizations is **no substitute for peer review of the natural-language proof**.
  - Assess whether the statement *and the argument* match, not only whether the code compiles.
  - Treat faithful autoformalization as an **open research problem**.
- **What they don't claim:** that OpenAI's natural-language proof is wrong.
- **Why this is applied-flavoured:** in analysis and PDE, theorems are stated through **hypotheses and constants**: derivative counts, exponents, norms. Those can drift slightly and still compile. Algebraic statements are harder to weaken quietly.

### Haugen, Stepanenko & Hansen: verify the computed object, not the method
[arXiv 2509.26122](https://arxiv.org/abs/2509.26122), revised Sep 2026.
- **Their method:** **a posteriori** verification of neural-network PDE solvers. Quadrature bounds the L² norms of the network and its derivatives, and energy estimates turn those into ε-accuracy against the unknown true solution, "regardless of training method."
- **Their argument:** **a priori guarantees about training are impossible**, because the training optimization problems are not algorithmically decidable. So **you certify the output, not the process that produced it.**
- **Parallel:** this is the numerical-analysis version of the Lean philosophy. Trust what can be checked, whatever produced it. **Unlike Lean, though, the check concerns a quantity in the problem (error against the true solution), not a formal derivation.**

### Armstrong & Kempe: PDE has only just reached Lean
[arXiv 2604.05984](https://arxiv.org/abs/2604.05984), Apr 2026.
- They formalized interior **De Giorgi–Nash–Moser** theory: local boundedness, the weak Harnack inequality, Moser's Harnack inequality, and Hölder regularity. They call it "the first machine-checked formalization of a major theorem in modern PDE theory."
- **Infrastructure they had to build:** Sobolev spaces on bounded domains, weak solutions, and quantitative estimates. They also note that **Mathlib's Lp spaces, defined as a quotient by almost-everywhere equality, add significant computational overhead.**
- They describe it as "large-scale autoformalization of hard analysis." Kempe is an ML researcher; **how much AI was used isn't stated in the abstract.**
- **Context for PDE coverage:** a formalization of tempered distributions and Sobolev spaces exists ([review](https://www.themoonlight.io/review/formalizing-schwartz-functions-and-tempered-distributions)). A Leray–Hopf weak-existence package exists, but only for the unforced equation and for one solution curve ([Reservoir](https://reservoir.lean-lang.org/@uda-lab/lerayHopf)).
- **This explains the Navier–Stokes drift:** the AI had to build the analysis it needed almost from scratch, so there was no shared Mathlib statement to pin it to.

### Other formal-side evidence relevant to applied work
- **TorchLean** ([arXiv 2602.22631](https://arxiv.org/abs/2602.22631)) formalizes neural networks in Lean. It notes that its network *verifier*, which certifies properties of concrete network computations, must account for IEEE-754 rounding when used on deployed models. This is a design point about that tool. It is **not** a limit of formal proof: a theorem about a mathematical object certifies that object's structure, and claims about an implementation have to be stated about the implementation (a statement-scope question, L2). *(Corrected 2026-11-10: an earlier version presented this as a general "floating-point gap" in formal proof, which overstated it.)*
- **Certified numerics in Lean are early.** LeanCert v1.0 (Jan 2026) generates interval-arithmetic proofs by branch-and-bound, but only for goals of the form ∀x ∈ I ([Zulip](https://leanprover-community.github.io/archive/stream/113488-general/topic/LeanCert.20-.20Verified.20Computation.20.26.20Interval.20Arithmetic.html)).
- **Engineering certification.** A 2026 survey of AI in verification and validation (AVAF, [Information 17:974](https://doi.org/10.3390/info17100974)) notes that kernel-checked proofs "lack DO-178C tool qualification." **A formal proof is not yet accepted as certification evidence** for aviation software.
- **Getting definitions right is the bottleneck.** In *Sorries Are Not the Hard Part* (Ilin & Nugent, [arXiv 2606.13925](https://arxiv.org/abs/2606.13925)), a formalization done mostly by agents compiled with no `sorry`, yet experts found problems with definitions, generality and API design. The example is from algebraic geometry, but the lesson carries over: **"compiles" is not "acceptable."**
- **ICIAM's statement (Sep 2026) doesn't mention formal proof at all.** It speaks of "open, robust mathematical validation environments" (note 04 §2). The international applied community's idea of verification is V&V, not Lean.

### The proposal to accept Lean in place of written proofs (TCS, but relevant)
- Kothari, Meka and Raghavendra ([Shtetl-Optimized, Sep 19, 2026](https://scottaaronson.blog/?m=202609)) propose a conceptual track at STOC/FOCS/SODA. **Papers would carry a Lean certificate instead of full proofs**, and reviewers would judge only the ideas.
- **That is mode B taken as sufficient.** The applied writers above (Hansen, Colbrook, Gómez-Serrano) would object that it is sufficient **only when the statement has been checked by a human**, which is L2 again.

---

## 4. Applied mathematics' earlier version of this debate (modes C and D)

- **Tucker and the Lorenz attractor (2002; Smale's 14th problem).** It was a computer-assisted proof in C++ that settled a major open problem. **Tucker himself later found and fixed bugs in his code.**
- **Immler, 2015–2018** ([JAR 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6044317/)) **certified Tucker's computations with a rigorous ODE solver formally verified in Isabelle/HOL.** That takes the trusted base from "Tucker's C++ code" down to "Isabelle's kernel."
  - **This is the applied precedent for "AI proof plus formalization."** The new element was a formally verified numerical engine, not a formalization of the analysis.
  - The parallel for today: **formally verify the checker, then let the untrusted generator** (Tucker's code, or now an AI) **produce candidates freely.**
- **Flyspeck (2014)** did the same for Kepler. Referees were "99% certain," the formal proof settled it, and the work took about 10 years.
- **Hou–Chen (2022)** proved blow-up for the 3D Euler equations with boundary using a computer-assisted proof. **DeepMind with Gómez-Serrano (2025)** used neural networks to find candidates for the computer-assisted pipeline.
- **The pattern:** the applied community already accepts **machine-generated candidates plus machine-checkable certificates**. What it argues about is **the trusted code**. AI adds a far more productive but untrustworthy generator. Formal verification of **the checker** (Immler-style), rather than of each proof, is the approach that fits applied work best.

---

## 5. Side by side: what a formal proof adds, from the applied viewpoint

| Question an applied mathematician asks | Informal AI proof (A) | With a Lean certificate (B) | With certified numerics (C/D) | What remains open |
|---|---|---|---|---|
| Are the deductions valid? | Unknown until an expert reads it | **Yes (L1)**, apart from kernel bugs (Collatz exploit, note 02 F) | Yes for the computed part, if the code is right (C) or verified (D) | |
| Is the formal statement the paper's statement? | Not applicable (the text is the statement) | **Must be checked by a human.** Analysis statements drift in derivative counts, exponents and norms (Navier–Stokes). Hansen: undecidable in general. | The certificate checks a specific inequality or enclosure. Is it the one the analysis needs? | L2 |
| Does the proof follow the paper's argument? | Not applicable | **Not checked.** Agents change the argument until it compiles (Hansen). | The argument is human; the computation is the machine's | L3 |
| Is a computed value right? | You trust the code | Not what a formal proof is for: it certifies the deduction. A computation is covered only if the theorem is stated about it (LeanCert) | **Yes, by construction** (interval enclosures) | Mostly mode C/D territory |
| Does the model describe the world? | V&V | **The formal proof says nothing about this** | V&V | V&V, always (ICIAM, Dutykh) |
| Was the source credited? | Often not (Kolda) | Not addressed | Not addressed | Provenance |
| Does anyone understand it? | Hairer: easy steps in detail, hard steps skimmed | Tao: verified but unexplained is "incomplete"; Gómez-Serrano: not helpful | Partly: the strategy is human | Exposition |
| Can it be done at all in my field? | Yes | **Often not yet** (PDE infrastructure only arrived in 2026) | Yes, for problems that suit it | Library coverage |

---

## 6. Agreement and disagreement

**Broad agreement among applied writers:**
- Informal AI proofs need expert checking: Hairer, Kolda, Colbrook, Gómez-Serrano, and the ICIAM statement.
- Being right is not the same as being understood: Tao, Gómez-Serrano, Colbrook.
- Verification, attribution and provenance get *more* important as generation gets cheaper: Colbrook, Kolda, ICIAM.
- Certify the output, not the process that produced it: Haugen–Stepanenko–Hansen, Immler, and Lean's own philosophy.

**Disagreement over how much a formal proof is worth:**

| More trust in formal proofs | Less trust in formal proofs |
|---|---|
| Matt Baker (pure math): below 1% chance of a mismatch; LLMs catch mismatches well (note 01) | Bastounis–Circelli–Hansen: compiling is not preserving meaning; faithfulness is undecidable in general |
| Kothari–Meka–Raghavendra: a Lean certificate instead of written proofs, in a conceptual track | Tao: verified but unexplained is incomplete |
| Suomela (2025): if Lean accepts it, human verification matters less | Ilin & Nugent: no `sorry` is not the same as acceptable to experts |
| | The AVAF survey: not yet certification evidence |

**The pattern:** the more a field's theorems are stated through **inequalities, constants and function spaces** (analysis, PDE, numerics), and the more its results end in **a number or a prediction**, the less a Lean certificate settles. Applied mathematics sits at that end.

---

## 7. Answers to your two questions

**1. Where is the applied-math writing on AI-generated proofs?** The core reading list:
1. Bastounis, Circelli & Hansen, *Navier–Stokes lost in translation*, [arXiv 2610.08144](https://arxiv.org/html/2610.08144v1). **The key text** on informal against formal.
2. Colbrook, *Ten Digits on a Train*, [arXiv 2606.23821](https://arxiv.org/abs/2606.23821). AI in certified numerics.
3. Kolda, *The Future of Math Research in the Age of AI*, [Silicon Reckoner](https://siliconreckoner.substack.com/p/the-future-of-math-research-in-the). The view of trust from the publications side.
4. Abouzaid, …, Hairer, …, Kolda, …, Ward et al., *First Proof*, [arXiv 2602.05192](https://arxiv.org/abs/2602.05192), plus Hairer's NYT interview.
5. Haugen, Stepanenko & Hansen, verification for neural-network PDE solvers, [arXiv 2509.26122](https://arxiv.org/abs/2509.26122).
6. Armstrong & Kempe, De Giorgi–Nash–Moser in Lean, [arXiv 2604.05984](https://arxiv.org/abs/2604.05984).
7. The ICIAM statement, [iciam.org](https://iciam.org/news/26/9/24/iciam-statement-mathematics-and-artificial-intelligence).
8. Tao, *Mathematics in the age of AI*, §§6–8, [arXiv 2608.16753](https://arxiv.org/html/2608.16753v1). For the "proof abundance" framing.
9. Immler, *A Verified ODE Solver and the Lorenz Attractor*, [JAR 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6044317/). The historical precedent.

**2. What is the difference between an AI proof and an AI proof plus formalization?** From the applied side:
- **Formalization turns "is it correct?" into "is the formal statement the right one?"** That is a smaller question, and still a human one.
- In applied analysis that smaller question is **harder than it looks**, because the content sits in hypotheses and constants.
- Formalization doesn't touch **numbers, models, provenance or understanding**.
- In most applied areas it **isn't yet possible**.

The applied tradition's own answer is **computer-assisted proof with a verified checker** (Immler-style mode D): let the AI generate freely, and formally verify the tool that checks it.

---

## Still to verify
- [ ] The full NYT text of Hairer's Feb 7 interview (current wording comes from reposts).
- [ ] The First Proof results paper: the failure types are from a secondary summary.
- [ ] How much AI Armstrong & Kempe used (read the full paper).
- [ ] The SIAM News essays (Omelchenko and others) that returned 403. Check whether SIAM News has run anything on Lean or AI proofs.
- [ ] Whether Hou, Chen or Buckmaster have written publicly about AI proofs with versus without formalization since the Navier–Stokes episode.
- [ ] Whether anyone has proposed Immler-style verified checkers for AI-assisted computer-assisted proofs in 2026.

## Sources
- Bastounis, Circelli, Hansen: https://arxiv.org/html/2610.08144v1
- Haugen, Stepanenko, Hansen: https://arxiv.org/abs/2509.26122
- Colbrook: https://arxiv.org/abs/2606.23821
- Kolda: https://siliconreckoner.substack.com/p/the-future-of-math-research-in-the
- First Proof: https://arxiv.org/abs/2602.05192 · Hairer: https://actu.epfl.ch/news/prof-m-hairer-on-artificial-intelligence-and-mathe · https://bernoulli.epfl.ch/professor-martin-hairer-on-artificial-intelligence-and-mathematical-research
- Gómez-Serrano: https://www.brown.edu/news/2026-08-26/javier-gomez-serrano-lab · https://lims.ac.uk/event/discovery-of-unstable-singularities/
- Tao ICM essay: https://arxiv.org/html/2608.16753v1
- Armstrong & Kempe: https://arxiv.org/abs/2604.05984 · Leray–Hopf in Lean: https://reservoir.lean-lang.org/@uda-lab/lerayHopf
- Immler: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6044317/ · https://link.springer.com/article/10.1007/s10817-017-9448-y
- TorchLean: https://arxiv.org/abs/2602.22631 · LeanCert: https://leanprover-community.github.io/archive/stream/113488-general/topic/LeanCert.20-.20Verified.20Computation.20.26.20Interval.20Arithmetic.html
- Ilin & Nugent: https://arxiv.org/abs/2606.13925
- AVAF survey: https://doi.org/10.3390/info17100974
- ICIAM: https://iciam.org/news/26/9/24/iciam-statement-mathematics-and-artificial-intelligence
- Kothari, Meka, Raghavendra: https://scottaaronson.blog/?m=202609
- NAS workshop panel notes: https://web.mit.edu/~ywang02/www/blog/nas-formalization/posts/05-panel-structures-to-understand-knowledge.html
