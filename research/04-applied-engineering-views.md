# Applied mathematics, engineering, TCS and physics: how the view differs from pure math

*Research notes for the "Math 2.0" talk. Compiled 2026-11-09. Follows [01](01-formalization-landmarks.md), [02](02-ai-math-tools.md) and [03](03-publishing-crisis.md).*

This note addresses the first question in `questions_of_interest.md`: how the applied math and theoretical engineering community sees these developments, compared with pure math. It also touches on the questions about experimentalists and about the parallel with AI-generated code.

---

## 0. Thesis: a different idea of what counts as verified

Pure mathematics has one standard of correctness: a proof. Applied fields have always had several:

| Field | What counts as "established" | What AI changes |
|---|---|---|
| Pure math | A proof that a human understands, refereed | Proofs become cheap, so understanding and credit become scarce (notes 01 and 03) |
| Applied and numerical math | **Verification and validation** (V&V): the code solves the equations correctly, and the equations describe reality. Convergence studies, error bounds, comparison with experiment. | A new tool to be held to the existing V&V standard (Dutykh, corpus post 816) |
| Rigorous and validated numerics | **"A number with a proof"**: an interval enclosure plus a certificate | AI proposes candidate values and proof strategies quickly; humans still catch the arguments that fail (Colbrook) |
| TCS | A theorem with a full proof, reviewed at a conference | Disclosure rules, caps on submissions, and proposals to stop requiring proofs in a conceptual track |
| Engineering / industry | Tests, certification (for example DO-178C in aviation), specifications | **The specification problem**: turning natural-language requirements into formal statements. The theorem prover is not the bottleneck. |
| Theoretical physics | Analytic consistency checks: limits, recursion relations, symmetries | AI-derived results checked against known limits, as in the gluon amplitudes case |

**Slide line:** applied mathematicians already knew that a correct computation does not guarantee a correct model. For them, the gap between a formal statement and what it is meant to capture is just V&V under a new name.

ICIAM, the international body for applied mathematics, puts the stance in one line ([Sep 24, 2026](https://iciam.org/news/26/9/24/iciam-statement-mathematics-and-artificial-intelligence)): "AI can accelerate discovery. Mathematics can provide understanding and trust."

---

## 1. Side note from the corpus: applied authors are more willing to adopt

> This section is supporting evidence from the Proofs & Prompts corpus only, not a reading of the field's consensus. For what applied mathematicians have written about AI proofs, and about informal versus formalized proofs, see [05-applied-ai-proofs-and-formalization.md](05-applied-ai-proofs-and-formalization.md).

**Method.** The automatically extracted `author_field` is blank for 103 of the 171 posts. Matching on department names misfires (for example, "School of Mathematics and Physics"). So I **classified 31 authors by hand**, reading `author_line` and `author_field`, into five groups, saved in [`data/field_groups.csv`](../data/field_groups.csv). Everyone else counts as core math.

The figures below use the **EDA analysis set** (152 posts: announcements, creative pieces and minimal-relevance posts are dropped), so 30 of the 31 applied-side posts remain. Produced by `eda.py`, figure: [`figures/10_field_group.png`](../figures/10_field_group.png). The subgroup sizes are tiny, so read the subgroups as **directional only**.

| Group | capability | **adoption** | understanding | community | institutions |
|---|---|---|---|---|---|
| Core math (rest) | 0.45 (n=111) | **0.07** (103) | −0.12 (108) | −0.27 (104) | −0.02 (91) |
| *All applied-side* | *0.51 (30)* | ***0.27*** *(25)* | *−0.06 (28)* | *−0.27 (26)* | *−0.06 (20)* |
| PDE / numerics / fluids | 0.62 (8) | 0.28 (7) | −0.08 (8) | −0.19 (8) | −0.08 (6) |
| Probability / stats / econ | **0.76** (6) | 0.35 (6) | −0.20 (5) | −0.44 (5) | 0.02 (4) |
| Physics | 0.53 (3) | 0.33 (3) | 0.17 (3) | 0.00 (3) | 0.30 (2) |
| Industry / engineering | 0.41 (7) | 0.32 (4) | 0.05 (6) | −0.22 (6) | −0.22 (4) |
| **TCS / CS** | **0.20** (6) | 0.06 (5) | −0.17 (6) | **−0.52** (4) | −0.12 (4) |

**Significance, applied-side against core math** (two-sided permutation tests on the difference in means):
- **adoption:** +0.19, **p = 0.085**. Suggestive, not significant.
- **capability:** +0.06, p = 0.36. No real difference.
- **understanding, community, institutions, overall:** p between 0.56 and 0.96. No difference.

**Reported AI use in research:** **30%** of applied-side authors (9 of 30) report *substantial* AI use, against **5%** (6 of 122) of core-math authors. **Fisher exact p = 0.0003.** This is the one robust difference.

**What the numbers say:**
1. **The robust finding is about behaviour, not attitude.** Applied-side authors are about **6 times more likely to say they use AI substantially in their own research**, and that holds up statistically. Their stated willingness to adopt leans the same way (+0.27 against +0.07) but doesn't reach significance with these numbers. Their **capability** ratings are essentially the same as core math's. So the difference is in *using* AI, not in *believing it works*.
2. **Probability and statistics authors rate capability highest (+0.76) but are among the most negative about community (−0.44).** These are the fields whose journals paused submissions (note 03). They see AI as powerful *and* as damaging to careers and credit. Henry's "Loss of Singularity" (922) and Ruodu Wang's game-theoretic "dilemma" (338) are the clearest examples.
3. **TCS academics are the exception.** They are the most skeptical about capability (+0.20) and the most negative about community (−0.52). Examples: von zur Gathen (2393, "AI is useless"), Rajasekaran (2483, AI as a "hostile attack"), Kretschmer (2379, demanding mandatory disclosure). Meanwhile their conferences (STOC, SODA, ITCS) have moved fastest on *policy* (§4). In TCS, the institutions are adapting faster than individual opinion.
4. **People in industry are split into camps**, not spread around the middle. They include the most negative post in the corpus, Hayward's (255, "sloppify the field", overall −0.9, drawing on AI's effect on software), and some of the most positive: Uppugunduri (1387, +0.8), Stankyavichyus (370, +0.5), Pal (1346).

**Slide:** [`figures/10_field_group.png`](../figures/10_field_group.png) shows means with 95% bootstrap intervals for five dimensions, by group. Read the subgroup rows as directional only. When presenting, say "6 times more likely to use AI" (p = 0.0003) rather than "more willing to adopt" (p = 0.085).

---

## 2. What the institutions say

### ICIAM statement (Sep 24, 2026), from the international council for applied mathematics
[iciam.org](https://iciam.org/news/26/9/24/iciam-statement-mathematics-and-artificial-intelligence)
- **AI increases the need for applied math.** AI needs stability, robustness, error control, uncertainty quantification and physical consistency. Known structure, such as conservation laws and symmetries, makes AI learn better. Many AI surrogate models resemble classical methods such as model order reduction.
- **Partnership framing:** humans set the questions, mathematics supplies structure, data links models to observations, and AI adds capability.
- **Recommendations:**
  - Build open validation environments.
  - Require attribution, reproducibility and **provenance**, and disclose the computational resources used.
  - **Report failures and limitations, not only successes.**
  - Train mathematicians to choose between classical methods, AI, and hybrids.
  - Integrate AI into industrial design and control.
  - Provide **equitable access to compute**.
- **What it does *not* mention:** formal proof systems and Lean. Validation, in this world, means V&V, not formalization.

### Compared with the Leiden Declaration (Jun 2026; mostly pure math; endorsed by the IMU)
- Leiden's concerns are **training on mathematicians' work without consent, bypassing peer review, attribution, and preserving human understanding**. It is defensive about values. Scholze signed it and avoids "reading AI-generated text as best as I can" ([TNW](https://thenextweb.com/news/leiden-declaration-ai-mathematics-proof-attribution); [CACM](https://cacm.acm.org/blogcacm/the-leiden-declaration-mathematics-ai-and-making-our-values-explicit/)).
- ICIAM's concerns are **trust, reliability and usefulness**. It is constructive about engineering.
- **The contrast for a slide:** pure math asks "what does AI do to *us*?" Applied math asks "what does AI need from *us*?"
- SIAM News (November 2026) reportedly ran an essay by Alexander Omelchenko on **gaps in Leiden that come from the applied/pure split**, and a piece on a Fields Medalists' manifesto discussing threats to applied math [secondary: the SIAM pages returned 403, so check before citing].

### SIAM
- **SIAM AI Task Force report, *The Role of Applied Mathematics in a New Era of Artificial Intelligence* (Feb 2026)** ([PDF](https://www.siam.org/media/b03hwuwe/siam-report-ai-task-force.pdf)). Its argument: AI may not reach its potential without investment in applied math. That is the "math *for* AI" framing. I couldn't extract the PDF text, so I don't have the details.
- **The 2026 SIAM Annual Meeting theme:** *"Mathematics in the Age of AI: Discovery, Verification, and the Future of Proof"* ([abstracts](https://www.siam.org/media/zxqcoyej/an26_abstracts.pdf)).
- **A MDS26 panel** on applied math and AI ([SIAM News](https://www.siam.org/publications/siam-news/articles/mds26-asks-how-artificial-intelligence-is-changing-the-mathematics-of-data-science/)).
- **Tamara Kolda** frames AI use in SIAM journal submissions as a **"contract of trust"** among authors, editors, referees and readers (cited in [arXiv 2609.21132](https://arxiv.org/pdf/2609.21132)). Kolda also co-wrote the arXiv surge analysis used in note 03.
- I found **no formal SIAM position on AI-generated proofs.**

### APS (physics), updated AI policy Jun 17, 2026
[aps.org](https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals)
- Disclosure must give the tool name and version, how it helped, how it was directed, and **how its output was verified**.
- Peer-review materials **may not be shared with unrestricted AI tools.**
- A broader APS statement on AI is expected around spring 2027.
- APS launched *PRX Intelligence*, which takes submissions from February 2026.
- Corpus post 1171 (Yates, amateur physicist) credits the APS policy as a model and proposes **author-supplied verification scripts** ("write and run a SymPy/NumPy script that checks…") as cheap verification for physics. *This is the applied-science counterpart of a Lean certificate.*

### Statistics
- The ASA's 2024 statement on ethical AI covers accountability, transparency and fairness.
- **JASA** has a 2026 special issue, "Statistical Science in AI" ([Amstat News](https://magazine.amstat.org/blog/2026/04/01/jasa-ai-revolution/)).
- The **Statistical Society of Australia** issued a statement on generative AI in March 2026 ([SSA](https://statsoc.org.au/statement-on-the-use-of-AI)).
- An Aug 2026 ASA piece argues that pharmaceutical statisticians remain essential, because judging study design, assumptions and bias matters "whether those analyses are generated by humans or machines" ([StatTrak](https://stattrak.amstat.org/2026/08/03/practicing-statistics-pharmaceuticals/)).
- **I found nothing from the IMS or INFORMS** on AI-generated theorems.
- **StatsMLlib** (note 02 H) is the formal side for statistics and learning theory.

---

## 3. Applied math: case studies

### Navier–Stokes, the applied community's flashpoint
- The OpenAI claim (Sep 8) concerns a **forced** problem: blow-up with a smooth external force. The Clay prize criteria don't cover forcing, and OpenAI pledged not to claim the prize. Coverage disagrees on scope ([Scientific American](https://www.scientificamerican.com/article/what-does-openais-blockbuster-mathematics-navier-stokes-proof-mean-for-the-real-world/); [Science](https://www.science.org/content/article/openai-breakthrough-triggers-existential-crisis-math)).
- The forcing approach goes back to **Córdoba and Martínez-Zoroa**, and then to Buckmaster and Alpöge on Euler. A priority dispute followed ([Wikipedia: Navier–Stokes priority controversy](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy)).
- **More than 1,000 mathematicians signed an open letter against the "mathathon"** [secondary].
- **Verification:** the Lean formalization **proves weaker inequalities than the paper** (m+5 derivatives where the paper has m+4). Bastounis, Circelli and Hansen, an applied-math and computation group, showed this in note 01 §5. The Clay Institute calls its process "deliberately unhurried."
- **On real-world impact:** Scientific American says applications "may be years away—if they ever arrive." Corpus post 2527 makes the same point: "the plumbing industry won't change a tiny bit."
- **Inside the corpus, reactions split:**
  - **Grief:** Sharma (1257, Caltech fluids) writes a centuries-long history of the field, ending with the machine-generated proof bringing a human endeavour abruptly to a close.
  - **Identity:** Zhang (2734) on being part of the "Navier–Stokes generation" of PhD students.
  - **Strategy:** Sun (2456, a CNRS PDE researcher) proposes **"toolization"**: give AI bounded local tasks while humans steer at the crucial branch points of the search.
  - **Fairness:** the anonymous PDE postdoc (1893) on credit.

**Why it matters for the comparison:** the problem everyone took as AI's crowning achievement is a PDE problem. It is also the case where formalization was weakest, because PDE and functional analysis are thin in Mathlib.

### Validated numerics: Colbrook, *Ten Digits on a Train* (Jun 2026)
[arXiv 2606.23821](https://arxiv.org/abs/2606.23821)
- AI-assisted **certified** computation of two eigenvalue problems, to 10 digits:
  - the full negative spectrum of a singular Schrödinger operator;
  - a resonance pair in a non-normal atom–molecule benchmark, which had not previously been resolved.
- **AI's role:** fast numerical candidates and plausible proof strategies. **Several strategies failed**, including a tail argument that looked complete but omitted a componentwise check.
- **Colbrook's framing:** the deliverable is "a number with a proof." This is the applied version of note 01's lesson: **the certificate is what matters, and AI gets that wrong in subtle ways.**
- **The formal side:** **LeanCert** (v1.0, Jan 2026) does interval arithmetic in Lean, with proofs generated by branch-and-bound. It currently handles only goals of the form ∀ x ∈ I ([Zulip](https://leanprover-community.github.io/archive/stream/113488-general/topic/LeanCert.20-.20Verified.20Computation.20.26.20Interval.20Arithmetic.html)).
- **TorchLean** (Feb 2026, [arXiv 2602.22631](https://arxiv.org/abs/2602.22631)) formalizes neural networks in Lean. Its verifier for concrete network computations has to handle IEEE-754 rounding on deployed models; that is a design point for that tool, not a limit of formal proof (see note 05 §3; corrected 2026-11-10).

### Dutykh, *Applied mathematics has met the machine before* (corpus post 816)
- Dutykh works on fluid mechanics, water waves, numerical methods and black holes. His post is **the most positive by an academic in the applied group** (overall +0.8, adoption +0.85).
- His history: human computers; the Fermi–Pasta–Ulam experiment; Courant, Friedrichs and Lewy discovering their stability condition while using finite differences to prove existence theorems; Courant's piecewise-linear functions becoming the finite element method.
- **The thesis:** embrace AI "with our usual standards of verification and validation, because we have been here before."
- **For the talk:** the most quotable statement of the applied view. Applied mathematics has had computers as partners since the 1940s, and *the machine has always been part of the method*.

### Other applied voices
- **Wegner (553, KIT, PDE):** in the human-in-the-loop scenario, people direct AI toward **application-driven problems**. If AI becomes fully superhuman, that is a problem for everyone, not just mathematicians.
- **Maltsev (3321, applied probability):** defends incremental mathematics; proposes daughter journals plus paid, AI-assisted refereeing (note 03).
- **Harlev (757, Cornell applied math):** reward exposition now.
- **G. Wang (163, Rutgers statistics):** a controlled prompting experiment on Feige's conjecture. One instruction to "search the literature broadly" took the success rate from **0 of 4 to 3 of 4** runs.

---

## 4. Theoretical computer science: institutions move faster than opinion

### Conference policy
| Venue | Rule |
|---|---|
| **STOC 2026 / FOCS 2026 / ITCS 2027** | No AI authors. Substantive AI use disclosed. Authors accountable. Full proofs must allow the main claims to be verified ([ITCS](https://itcs-conf.org/), [STOC CFP](https://acm-stoc.org/stoc2026/stoc2026-cfp.html)). |
| **STOC 2027** (deadline Nov 2, 2026), as reported by Fortnow ([blog, Sep 23](https://blog.computationalcomplexity.org/2026/09/the-new-stoc-rules-for-ai-era.html)) | **Not anonymous**, reversing the 2023 move to double-blind review. **At most 5 submissions per author.** Must be **on arXiv** before the deadline. **A 20–30 minute explanatory video** presented by an author. Substantial AI use disclosed. **Program committee members may use LLMs** on reviews, with **authors' consent required to submit**. |
| **STOC 2026 experiment** | Gemini-based feedback for authors before submission (note 03 §6) ([workshop](https://pritishkamath.github.io/ai-tcs-stoc-2026/)) |
| **SODA 2027 / QIP 2027** | Kretschmer (2379) warns of a disclosure "disaster" |

**Why STOC 2027 matters:** the video requirement and the end of anonymity are tests of **whether someone understands the paper**. They check the human author, not the proof. That answers the abundance problem with *accountability*, not formalization. Commenters raised concerns about bias against non-native speakers, privacy, and the workload of reviewing videos.

### Proposal: "Theory Beyond Theorems and Proofs"
Kothari, Meka and Raghavendra, [Shtetl-Optimized guest post, Sep 19, 2026](https://scottaaronson.blog/?m=202609):
- **The proposal:** a new STOC/FOCS/SODA track for **conceptual papers**: new definitions, questions and explanatory theories. Papers are under 10 pages. **Proofs are optional, with a Lean certificate as a supplement.** Reviewers judge conceptual merit only.
- **Their thought experiment:** even an oracle that decides whether any problem is in P would not end complexity theory. People would still want to know *why*, as with NP-completeness or polymorphisms for constraint satisfaction problems.
- **This is the clearest institutional form of "proof abundance, insight scarcity":** the proof is outsourced to Lean, and the human paper is about *ideas*.
- Aaronson's view ("The Age of Wonders and Terrors," Sep 15): the Singularity has begun. He lists AI-assisted quantum complexity results, including a QMA vs QMA(2) oracle separation and perfect completeness for QMA.

### Earlier groundwork
- **Suomela, *AI for TCS?*** ([Jul 2025](https://jukkasuomela.fi/ai-for-tcs/)): formalize the key TCS definitions in Lean now, imagine submissions that ship Lean proofs **and tested Rust implementations**, and "plan, build scaffolding, and do small-scale experiments." Much of that has since happened (note 02).
- **A human audit of OpenAI's "Ten Advances in Mathematics and TCS"** ([arXiv 2608.14673](https://arxiv.org/html/2608.14673v3)) found no surviving substantive mathematical error, relying on the Lean formalizations.

---

## 5. Engineering and industry: the specification problem

- **Safety-critical systems.** A 2026 survey of AI for V&V (the AVAF framework, [Information 17(10):974](https://doi.org/10.3390/info17100974)) found **no study reaching a complete formal guarantee over a realistic model with certifiable evidence**. It notes that kernel-checked proofs "lack DO-178C tool qualification," the aviation software certification standard. **A Lean proof is not yet certification evidence.** Its research priorities include LLMs that generate Isabelle, Coq or TLA+ from safety requirements, and measuring hallucination in LLM-written specifications.
- **AWS automated reasoning (Byron Cook):** neurosymbolic trust, with LLMs making Lean, Isabelle and HOL Light "vastly easier to use." **Automated Reasoning checks in Bedrock Guardrails** translate natural-language policies into logic and check AI outputs against them ([interview, Feb 2026](https://allthingsdistributed.com/2026/02/a-chat-with-byron-cook-on-automated-reasoning-and-trust-in-ai-systems.html)). Formal methods are being used as **guardrails for agents** ([SE Daily, May 2026](https://softwareengineeringdaily.com/2026/05/19/formal-methods-as-agent-guardrails/)). Lean's creator Leo de Moura worked at Amazon.
- **A Rust-to-Lean verification pipeline with AI provers** ([arXiv 2605.30106](https://arxiv.org/pdf/2605.30106)): formal verification of real code.
- **Pal (1346, cloud engineer):** separates **Proof**, a formal relation inside a system, from **Resolution**, acceptance relative to a requirement. He proposes an eight-step protocol in which humans own the specification, the semantic match and the explanation. This is an engineer's restatement of the L2 problem (statement fidelity) from note 01.
- **Hayward (255, data scientist):** the software-industry view at its most pessimistic. AI will "sloppify" mathematics as it did code, swamp its institutions and break the training pipeline.

**For the talk:** engineers say the hard part was always writing down *what the system should do*. That is the same as note 01's statement-fidelity layer. Software has a decade of practice with specifications, tests, guardrails and formal methods for AI-written code (note 03 §7). Pure math is having to learn this quickly.

---

## 6. Theoretical physics: analytic checks as verification

- **Gluon amplitudes (Feb 2026):** a class of tree-level gluon amplitudes that was widely assumed to vanish turns out to be nonzero under precisely defined conditions.
  - A scaffolded GPT-5.2 **derived the formula on its own and produced a proof** in about 12 hours.
  - It was checked analytically against the **Berends–Giele recursion** and **soft theorems**.
  - Co-author Nima Arkani-Hamed called it clearly journal-level research.
  - A follow-up extended it to gravitons (Mar 4).
  - Sources: [OpenAI](https://openai.com/index/new-result-theoretical-physics/), [Quantum Insider](https://thequantuminsider.com/2026/02/13/ai-scientist-spots-what-physicists-missed-in-gluon-scattering/).
  - **Criticisms:** humans checking a result is not the same as reproducing how it was found, and **access to the tool was restricted** ([UC Strategies](https://ucstrategies.com/news/ai-cracked-a-15-year-physics-problem-but-only-openais-friends-can-use-it/)).
- **Physics checks results by consistency:** known limits, symmetries, recursion relations. That is cheaper than formal proof and has been accepted for decades. **PhysLib** (note 02 H) is the formal side, with a lighter-review tier for AI-scale contributions.
- **Corpus physics voices are the most positive group** (overall +0.17, though n = 3):
  - **Pasquato (1838, astrophysicist):** LLMs break the "science = papers" signal. **Cap papers per author per year**, then let anything go. That is arXiv's 2-per-month policy, argued in advance.
  - **Yates (1171, amateur physicist):** AI enables real citizen science. Use verification scripts and AI-assisted review.
  - **Cheung (517):** maths communication as the human role.

---

## 7. Synthesis: how the applied-side view differs

| | Pure math (core of the corpus, Leiden) | Applied, engineering, physics (ICIAM, APS, corpus) | TCS |
|---|---|---|---|
| **What's threatened** | Understanding, credit, community values | Trust and reliability of models and predictions | Credit, and conference reviewing load |
| **Trusted verification** | Proof, now Lean | V&V; validated numerics; analytic consistency; verification scripts | Proofs, plus human accountability (video, no anonymity) |
| **Formalization** | Central (notes 01–02) | **Barely mentioned** (ICIAM); thin library coverage (PDE); not certification evidence (DO-178C) | Proposed as an *optional supplement* in a conceptual track |
| **Attitude to adoption (corpus)** | +0.07; 5% use AI substantially | +0.28 to +0.35; 30% use AI substantially | +0.06 |
| **Typical proposal** | Leiden values; disclosure; new journals; Palomar | AI assisted by math ("math for AI"); open validation environments; equitable compute; report failures | Caps; videos; consent to AI review; a conceptual track |
| **Biggest fear** | The end of human understanding | Unvalidated AI in decisions that matter; deskilling | Being flooded; "hostile attack" (Rajasekaran) |

**Three points for the talk:**
1. **Applied fields don't face a crisis of meaning, because the proof was never the product.** The product was a model, an algorithm or a prediction. The proof was one form of validation among several.
2. **Applied fields do face a crisis of tools.** The flagship AI result was in PDE, where formal libraries are weakest. Lean proofs don't count as engineering certification evidence. **Lean can't yet certify most of applied math.**
3. **Experimentalists need specifications more than they need theorem provers** (from the questions list). Physics-style verification scripts, Pal's Resolution protocol, and Prove2Me's captain-written cores (note 02 D) all say the same thing: experimentalists can **delegate the proof but not the statement.**

### Classification used in §1 (post IDs; also in `data/field_groups.csv`)
- **PDE / numerics / fluids:** 553, 1257, 816, 1149, 2734, 3130, 2456, 1893
- **Probability / statistics / economics:** 163, 338, 757, 922, 3321, 2533
- **Physics:** 517, 1838, 1171
- **TCS / CS:** 1336, 2379, 1502, 2393, 2130, 2483, 1573
- **Industry / engineering / data science:** 255, 370, 1316, 1346, 1387, 1043, 2159

### Corpus posts cited
| id | Author | Post |
|---|---|---|
| 816 | Denys Dutykh (Khalifa) | [Applied mathematics has met the machine before](https://proofsandprompts.com/2026/09/28/applied-mathematics-has-met-the-machine-before/) |
| 1257 | Saksham Sharma (Caltech) | [History and Future of Fluid Dynamics](https://proofsandprompts.com/2026/09/20/history-and-future-of-fluid-dynamics/) |
| 2456 | Chenmin Sun (CNRS) | [Nothing More than Tools?](https://proofsandprompts.com/2026/11/06/nothing-more-than-tools/) |
| 553 | Robert Wegner (KIT) | [A somewhat optimistic view of AI in mathematics](https://proofsandprompts.com/2026/09/10/a-somewhat-optimistic-view-of-ai-in-mathematics/) |
| 922 | Benoit Henry (IMT Nord Europe) | [The Loss of Singularity](https://proofsandprompts.com/2026/09/28/the-loss-of-singularity/) |
| 338 | Ruodu Wang (Waterloo) | [The AI-assisted mathematician's dilemma](https://proofsandprompts.com/2026/08/28/the-ai-assisted-mathematicians-dilemma/) |
| 163 | Guanyang Wang (Rutgers) | [Prompting Toward a Conjecture](https://proofsandprompts.com/2026/08/12/prompting-toward-a-conjecture/) |
| 1838 | Mario Pasquato (IASF-Milano) | [AI and the mismeasure of science](https://proofsandprompts.com/2026/10/05/ai-and-the-mismeasure-of-science/) |
| 1171 | Brandon Yates (amateur physicist) | [A new kind of citizen science](https://proofsandprompts.com/2026/10/07/a-new-kind-of-citizen-science-and-how-to-handle-it/) |
| 1346 | Pronab Pal (IntentixLab) | [Proof and Resolution](https://proofsandprompts.com/2026/10/15/proof-and-resolution-two-different-forms-of-establishment/) |
| 255 | Simon Hayward (data scientist) | [On The Brutal Mathematics of Slop](https://proofsandprompts.com/2026/08/13/on-the-brutal-mathematics-of-slop/) |
| 2393 | Joachim von zur Gathen (Bonn, CS) | [Picasso rephrased: AI is useless](https://proofsandprompts.com/2026/11/04/picasso-rephrased-ai-is-useless/) |
| 2483 | Senthil Rajasekaran (ULB, TCS) | [The Bigger Picture](https://proofsandprompts.com/2026/11/09/the-bigger-picture/) |
| 1573 | Benjamin Merlin Bumpus (São Paulo) | [Thinking Hard Above AI](https://proofsandprompts.com/2026/10/19/thinking-hard-above-ai/) |

---

## Still to verify
- [ ] The SIAM News Nov 2026 essays (Omelchenko on gaps in Leiden; the piece on a Fields Medalists' manifesto and applied math). The pages returned 403.
- [ ] The contents of the SIAM AI Task Force report. The PDF wouldn't extract; installing `pypdf` in `.venv` would fix that.
- [ ] Whether the "1,000+ mathematicians open letter against the mathathon" is the same as the Fields Medalists' declaration or a separate letter.
- [ ] The STOC 2027 rules from the program committee chair's post, not Fortnow's summary.
- [ ] Any position from IMS or INFORMS.
- [ ] Possible additions: control theory and formal methods (Lyapunov or reachability proofs in Lean or Isabelle); the computer-assisted proofs community's response (for example, the CAPA conference); the NAS formalization workshop panel of Jul 20, 2026 ([MIT blog](https://web.mit.edu/~ywang02/www/blog/nas-formalization/posts/05-panel-structures-to-understand-knowledge.html)).

## Sources
- ICIAM statement: https://iciam.org/news/26/9/24/iciam-statement-mathematics-and-artificial-intelligence
- SIAM AI Task Force: https://www.siam.org/media/b03hwuwe/siam-report-ai-task-force.pdf · AN26: https://www.siam.org/media/zxqcoyej/an26_abstracts.pdf · MDS26: https://www.siam.org/publications/siam-news/articles/mds26-asks-how-artificial-intelligence-is-changing-the-mathematics-of-data-science/
- Leiden: https://thenextweb.com/news/leiden-declaration-ai-mathematics-proof-attribution · https://cacm.acm.org/blogcacm/the-leiden-declaration-mathematics-ai-and-making-our-values-explicit/
- APS: https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals
- Statistics: https://magazine.amstat.org/blog/2026/04/01/jasa-ai-revolution/ · https://statsoc.org.au/statement-on-the-use-of-AI · https://stattrak.amstat.org/2026/08/03/practicing-statistics-pharmaceuticals/
- Navier–Stokes: https://www.scientificamerican.com/article/what-does-openais-blockbuster-mathematics-navier-stokes-proof-mean-for-the-real-world/ · https://www.science.org/content/article/openai-breakthrough-triggers-existential-crisis-math · https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy
- Colbrook: https://arxiv.org/abs/2606.23821 · LeanCert: https://leanprover-community.github.io/archive/stream/113488-general/topic/LeanCert.20-.20Verified.20Computation.20.26.20Interval.20Arithmetic.html · TorchLean: https://arxiv.org/abs/2602.22631
- TCS: https://blog.computationalcomplexity.org/2026/09/the-new-stoc-rules-for-ai-era.html · https://scottaaronson.blog/?m=202609 · https://jukkasuomela.fi/ai-for-tcs/ · https://itcs-conf.org/ · https://acm-stoc.org/stoc2026/stoc2026-cfp.html · https://pritishkamath.github.io/ai-tcs-stoc-2026/ · https://arxiv.org/html/2608.14673v3
- Engineering: https://doi.org/10.3390/info17100974 · https://allthingsdistributed.com/2026/02/a-chat-with-byron-cook-on-automated-reasoning-and-trust-in-ai-systems.html · https://softwareengineeringdaily.com/2026/05/19/formal-methods-as-agent-guardrails/ · https://arxiv.org/pdf/2605.30106
- Physics: https://openai.com/index/new-result-theoretical-physics/ · https://thequantuminsider.com/2026/02/13/ai-scientist-spots-what-physicists-missed-in-gluon-scattering/ · https://ucstrategies.com/news/ai-cracked-a-15-year-physics-problem-but-only-openais-friends-can-use-it/
