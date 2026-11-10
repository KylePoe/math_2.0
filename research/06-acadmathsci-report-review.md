# Review: Reisinger et al., *The Mathematical Sciences in an AI-enabled World* (AcadMathSci, Oct 2026)

*Research notes for the "Math 2.0" talk. Compiled 2026-11-09. Source: Zotero copy `7MDTEDEM` (55 pp.).*

**The document.** Christoph Reisinger (Oxford), Rachel Bearon (KCL), Thomas Bloom (Manchester), Jennifer Gaskell (Glasgow), David Leslie (Lancaster), Zubin Siganporia (QED Analytics). *Opportunities, risks and community needs.* Pre-publication draft, dated 28 Oct 2026, for the **Academy for the Mathematical Sciences** (UK). It covers the whole discipline: pure, applied/industrial, statistics, OR, and the mathematics of AI. Its readers are departments, funders, publishers and employers. Bloom runs the Erdős problems site, so the pure-math capability appendix comes from someone close to the evidence.

**This is the "AcadMathSci report" that note 03 could only cite in summary** (§2, and still-to-verify: "The PDF returned 403"). That item can now be closed. See §1 below.

**Reliability key for this note.**
- **[report]**: the report states it and cites someone else. Treat it as secondary, and trace to the primary source before it goes on a slide.
- **[report estimate]**: the authors' own arithmetic, which they label "our estimate".
- **[report view]**: the authors' judgement.

**A caveat on provenance.** The report's AI declaration (p. 27) says Claude "drafted the appendices" and "produced the timeline and tables", and that the authors reviewed everything. The appendices hold most of the numbers (capabilities, failure modes, costs). They are carefully sourced, but primary checks matter more than usual here. §8 lists the internal inconsistencies I found.

---

## 0. Bottom line for the talk

1. **The thesis fits Math 2.0 almost word for word.** "The bottleneck in mathematical research is shifting from technical work to expert attention and judgement" (exec. summary, p. 2). The risks are "institutional rather than technical": systems "built for a world in which proofs were scarce now face abundance" (§3, p. 17). This is a society-level endorsement of the proof-abundance / insight-scarcity frame, and it quotes Tao's Math 2.0 talk directly (A.4).
2. **Its main publishing proposal is to assess correctness, significance and understanding separately** (§3.1, §4.6). Correctness would go to AI plus formalization; significance and understanding stay human-led. It adds a **separate, labelled route for bulk AI output**, and pilots of a **verified registry of formal results with overlay journals**. This is the clearest institutional version of the L1/L2/L3 split from note 01.
3. **It is the best source in the project on compute cost (Appendix B).** It gives per-problem costs, per-researcher annual costs by route, and a costed shared open-weight node. It also states a trend: fixed capability gets about 5–10× cheaper a year, while frontier use gets 3–18× costlier a year. This answers the budgeting question directly (§4, Q12).
4. **It gives applied, statistics and OR equal weight, and says they differ in structure.** These fields have "no library of clearly stated conjectures that AI can knock off" (§1.4). They lack a verifier ("no verifier, no flywheel", A.5). And for them the correctness/significance split "is harder", with "code, data and documented validation" playing the role that formal proof plays in pure math (§4.6). This supports notes 04 and 05.
5. **It names the "convex hull" explicitly** (§2.1), and gives a mechanism that fits it (RL with verifiable rewards "may sharpen rather than extend", A.5). See Q14.

---

## 1. Closes items from earlier notes

| Earlier item | What the report gives | Where |
|---|---|---|
| Note 03, still-to-verify: September 7,428 against 4,252 | Confirmed: "7,428 mathematics articles against 4,252 in September 2025, up about 75%". Early 2026 was only about 10% above early 2025, so **the surge is recent**. | §1.2, p. 10 |
| Note 03: arXiv cap | Two submissions per submitter per month, all categories, from 1 Oct 2026. arXiv cited 40,363 submissions in September 2026 against 20,569 two years earlier, and called the cap a stopgap. | §1.2 |
| Note 03: journal suspensions | "On 19 October six leading international journals in probability and statistics paused submissions." The report calls journal-side evidence "largely anecdotal" and asks for systematic submission and referee-decline data. | §1.2, §4.6 |
| Note 01: OpenAI release, 722 against 719 manuscripts | 719 manuscripts in **372 result families**, from about **4,000 problems** attempted. 300 formalized; **3 withdrawn within a day**. 722 − 3 = 719 probably explains the gap. | A.1.3, §1.1 |
| Note 02: Collatz / Lean kernel | Consistent: a "sorry-free" Collatz "disproof" exploited a kernel bug (Jul 2026); AI bug hunts found several routes to `False`, fixed in v4.33.1 (de Moura post-mortem, Aug 2026). | §2.2, A.3 |

---

## 2. New facts not yet in notes 01–05

| Fact | Tag | Where |
|---|---|---|
| Disclosed AI use in arXiv math papers rose from **4% (Apr) to 25% (Aug 2026)** (Epoch AI) | [report] | §1.1 |
| A study of 5,114 journals: AI-assisted writing grew **at the same rate with or without a journal AI policy** | [report] arXiv 2512.06705 | §1.1 |
| **Mathlib has 65 reviewers for 950 contributors** | [report] | §4.7 |
| **Mathlib "reportedly does not yet accept AI-generated formalisations"**: poorly written, fragile, hard to port, opaque | [report], "reportedly" | §2.2 |
| Tau Ceti (AI-written, AI-reviewed) is **about 3M lines, larger than Mathlib**; Avigad, Buzzard, Commelin et al. forecast that most of mathematics can be formalized in usable libraries within three years, *if done to Mathlib standards* | [report], Xena guest post, 16 Oct 2026 | A.4 |
| One autoformalization produced 1.2M lines in three weeks, against 2.3M for Mathlib over nine years (Buzzard, Jul 2026) | [report] | A.5 |
| **Simons Foundation $15M** initiative, with Anthropic and OpenAI resources, to help mathematicians evaluate AI results (Oct 2026) | [report] | §1.3, C.3 |
| XTX: $10M each to Lean FRO and the Mathlib Initiative (to 2030); £5M "Langlands Lab" at Imperial (Buzzard); £500k to ICMS. Gerko gave $10M earlier. The report: "a single private donor therefore underwrites much of the field's formal infrastructure" | [report] | §1.3, C.3 |
| **Kontorovich**: the semantic-alignment (statement-fidelity) gap "will never be solved purely in software" (NAS, Jul 2026) | [report] | A.3 |
| **First Proof Batch 3** (Oct 2026): ProofCouncil 9/10, GPT-6 Astra single call 7/10 (**$36 for all ten**), Anthropic Siege 3/10 with 5 abstentions, MerLean 4/10, open-weight Kimi K3 0/10. Negative scores for wrong answers, so systems **abstained instead of bluffing**. Some AI proofs judged better than the authors' own | [report] hexagon:2610.00244 | A.1.1, A.2, B.1 |
| Batch 3 failures: a third of the top system's answers scored negative on **exposition**; on P7 referees could not confirm a computational proof in the time allowed; MerLean built a false counterexample on a superseded arXiv definition, judged "deliberately deceptive" | [report] | A.3 |
| OpenAI release: most informal write-ups called "impenetrable" by Avigad, Buzzard et al. | [report] | A.3 |
| AGMAI (Advisory Group on Mathematics and AI): release guidelines for labs from 600+ survey responses. Labs **withheld prompts despite the group's request** (29 Sep 2026) | [report] | A.3, C.4 |
| Leiden Declaration **endorsed by the IMU**; the EMS called it valuable but did not formally endorse it | [report] | §1.2, C.1 |
| SIAM AI policy v2.0 (May 2026): more detailed rules on theorem and proof claims, code, referee confidentiality, "non-delegation of scholarly judgement". LMS: referees uploading manuscripts to AI counts as misconduct | [report] | C.1, C.5 |
| **Confidentiality leaks**: the Navier–Stokes **priority dispute** and anecdotes of "private" AI conversations leading to lab results. Scooping: a result announced in a conference-talk title was pre-empted by a hasty AI-generated paper (anecdotal) | [report] | §3.2, §3.4 |
| **US export controls cut off two frontier models for foreign nationals, 12 Jun – 1 Jul 2026** | [report], partly secondary | §3.1, B.5 |
| Narrowing: a study of 41M natural-science papers found AI adoption **shrinks topic range by 4.6% and researcher engagement by 22%** while raising individual output (Hao et al.) | [report] arXiv 2412.07727 | §3.2 |
| Students given unrestricted GPT-4 scored **17% lower** once access was removed; a tutor with guardrails largely avoided the harm (Bastani et al., PNAS) | [report] | §3.3 |
| **Springer Nature survey** (10,480 researchers): only **11%** have institutional funding for their main AI tool | [report] | §1.6, B.2 |
| Interest metric: proof length divided by statement length correlates with downstream use in Mathlib (Spearman 0.76). Training on it cut regenerations of existing Mathlib statements from 92% to 31% (Patel et al., Sep 2026) | [report] arXiv 2609.28603 | A.6 |

---

## 3. Material by question (`questions_of_interest.md`)

### Q1. How do applied math and theoretical engineering see this, compared with pure math?
This is the report's strongest contribution, because it was written to cover the whole discipline.
- **Different relation to proof.** In applied math, statistics and OR, "the maths" (formulating and proving theorems) "is a means to an end": if AI does it faster, practitioners do more useful things (§1.4). The expertise lies in finding and formulating problems and choosing assumptions with the "customer". The report calls this a negotiation among stakeholders. Whether that part can be handed over depends on trust "earned through validation, uncertainty quantification and human judgement" (citing ICIAM).
- **No conjecture list to attack.** Applied fields "have almost no reliance on solving long-established conjectures" (§1.4). That is why flagship announcements concentrate on pure math.
- **No verifier, no flywheel** (A.5, Ceiling 2). Proofs can be checked; modelling choices, significance and exposition mostly cannot. So capability "will stay uneven across the mathematical sciences". [report view]
- **Evidence of applied failure modes** (§2.3, §3.5):
  - **PDEAgent-Bench**, 645 finite-element tasks: best single-shot pass rates 54% (DOLFINx) and 32% (deal.II). "Code usually runs but fails accuracy checks." Execution feedback fixes bugs, not mis-formulated problems.
  - **ORAgentBench**: modelling errors cause over half of agent failures. OR benchmarks themselves have 26–54% error rates (arXiv 2508.10047).
  - **Many AI analysts** (Bertran, Fogliato, Wu 2026): autonomous analysts given the same data reach sharply different conclusions. Prompting them toward confirmation shifts support by 34–66 percentage points.
  - McGreivy & Hakim: 79% of ML-for-fluids papers that claimed to beat numerical methods broke a fair-comparison rule.
  - Model choice: current tools "favour popular generic models over the most appropriate one" (§2.3).
- **Industry**: in a 2023 McKinsey/NAFEMS engineering-simulation survey, about two-thirds were experimenting with AI but only about 5% had it fully integrated. Barriers: confidence in results, expertise, integration (§1.4). The report warns that firms may overestimate how sophisticated their adoption is, and suggests academics may be ahead.
- **Where the community's effort goes**: activity is "heavily skewed towards pure mathematics and formalisation, much of it philanthropic"; statistics and OR initiatives focus on professional practice, not discovery (§4, App. C).
- **Positive applied cases**: AI weather (ECMWF AIFS operational since Feb 2025, up to 20% better cyclone tracks at about 1,000× less energy; GraphCast); AlphaEvolve recovering about 0.7% of Google's compute; prediction-powered inference; reporting the whole range of defensible analyses instead of one.
- **Fit with notes 04/05**: this agrees with "a different idea of what counts as verified". The report adds evidence (benchmarks) to what were mostly opinion pieces in 04/05.

### Q2. What problems does publishing face, and how do they relate to AI?
- **Volume**: the numbers in §1 above. Also, "one AI lab alone released over 700 manuscripts in a single day … drawn from around 4,000 problems" (exec. summary).
- **Mismatch with norms**: labs announce "at scale, by press release, in formats that do not facilitate expert scrutiny" (§3.1).
- **Contamination**: erroneous synthetic material enters the literature, and models trained on it absorb it, quoting Harington & Silverman (AMS 2024) (§3.1).
- **Credit and attribution**: models reuse ideas without attribution, which is worst for expository writing where readers may not recognise "Smith's trick" (§3.2). The capability appendix adds: 8 of Aletheia's 13 meaningful Erdős results were already in the literature; in Batch 3 a GPT-6 Astra write-up was judged "tantamount to plagiarism"; systems cite arXiv far better than older journal literature (A.3).
- **Confidentiality and refereeing**: UKRI bars assessors from using generative AI except for language editing. The report suggests some AI screening may be justified if volumes rise, but only with tools that do not leak data, such as locally hosted models (§3.4).
- **Referees are "the narrowest bottleneck"** (§4.6). Proposals: credit, payment or reduced load for refereeing; more editorial capacity.
- **Policy lag**: the 5,114-journal finding (§2 above) suggests disclosure policies are not changing behaviour.

### Q3. How can formalization help? How much will automated AI review be part of it?
- **The proposal**: "assess correctness (utilising AI and formalisation), significance and understanding (both human-led) separately" (exec. summary, §4.6). This "can focus human efforts and absorb higher volumes without lowering standards".
- **Three- to five-year pilots** (§4.6): "a verified registry of formal results with overlay journals, or reviewed preprints"; a separate route for bulk AI output; guidelines for papers with a computational component "from formal proofs to code and data".
- **Twelve-month steps** (§4.6): ring-fenced AI integrity-screening tools under publishers' control; common disclosure and provenance standards building on Leiden and the LMS; transparency on whether deposited work is used for training.
- **What formalization cannot do yet** (§2.2, A.3): statement fidelity needs human checking; Mathlib doesn't accept AI formalizations; the output is opaque; Kontorovich says the alignment gap will never be solved purely in software. The report also flags "a growing divide between mathematics that is readily formalisable and mathematics that is not" (§3.1). This matches note 03 §5 (thin library coverage disadvantages PDE and probability).
- **Automated review**: the report is cautious. It supports AI screening for integrity and correctness checks inside a formal pipeline, and mentions ML conferences' trials and UKRI's trial of AI-assisted *grant* assessment. It does **not** propose AI judging significance. Its A.4 forecast is that "formal verification will need independent checkers and human review of statements".

### Q4. Parallels between AI-generated experiment code and AI-generated proofs
The report does not draw this parallel explicitly, but it supplies the evidence for it.
- **"Runs but wrong" is the code version of "compiles but misstated."** PDEAgent-Bench: code "usually runs but fails accuracy checks", and execution feedback "fixes bugs but not mis-formulated problems" (§2.3). This mirrors L1 against L2: the kernel (or the interpreter) catches local errors, not a wrong specification.
- **Subtle errors buried in large codebases** that users cannot evaluate (§3.6). The proof version is 13M-line FLT and 43M-line CFSG formalizations.
- **What counts as the certificate in applied work**: for applied and statistical work, "code, data and documented validation play the equivalent role" to formal correctness checks (§4.6). §4.7 asks for "reproducible code and data artefacts, and open validation environments with agreed benchmarks and uncertainty quantification" as the applied counterpart to Mathlib.
- **Report every run**: the many-analysts result leads to a recommendation to report *all* analyses run (§3.5). This is the same demand as Leiden/AGMAI's "report failures and resources alongside successes" for proof attempts (§4.2).
- **Reproducibility of the generator itself**: results rest on "closed, non-deterministic and changing models". A Bochum–Leipzig benchmark found significant variation across runs. Pinned open-weight versions are "the most reproducible option" (B.5). This is the software idea of pinning dependencies, applied to the model.

### Q5. Which parts of math are "right" to hand over to AI?
- **The workflow the report describes** (§1.1): the human frames the project and question and suggests proof strategy; the AI proves; they iterate; the human integrates the result. This is the division of labour as practised in Oct 2026.
- **What AI does well** (A.2): last-mile technical work on a known roadmap; counterexamples; search over constructions; formalization at scale; problems close to the literature; research lemmas; retrieving forgotten results (Erdős-1089 was answered by a remark in a 1981 paper).
- **What stays human** (exec. summary; A.6): choosing problems, providing key ideas, building theory, understanding AI proofs, translating findings into shared understanding. On the applied side: formulating questions with stakeholders, modelling trade-offs, validation, interpretation.
- **A useful split of "interest"** (A.6): *structural value* (compression, reuse, short statements with long proofs) can be measured by machine and "will be optimised hard". *Purposive value* (explanatory power, relevance to science, fit with a programme) "lives outside the formal corpus". AI will propose; direction stays with people "as a matter of purpose as much as capability". The report adds that we should not claim taste is permanently human. [report view]
- **Weak spots** (A.3): Tao says AI is bad at creating partial progress; Gowers says it lacks a "nose" for pruning; there is a bottleneck with genuinely new definitions.
- **Industrial caveat** (§3.6): general-purpose LLMs "should not be regarded as substitutes for specialist mathematical methods" in large-scale discrete optimisation, rigorous inference or high-precision simulation. Knowing when to use which is "itself an important area of expertise".

### Q6. Can autoformalization help experimentalists and others who don't usually do rigorous math?
**This is a gap in the report.** It does not discuss autoformalization for non-mathematicians. The nearest material:
- **Lowering barriers** (§2.4): AI makes established techniques accessible to practitioners without the specialist knowledge or programming resources. Optimisation for non-specialists: LLMs translating natural-language problems into optimisation models. In Gurobi's 2025 survey, 41% of commercial users expect GenAI to matter within two years, and model generation is the top use case at 51% (§2.3).
- **The standing warning**: "The ability to implement a technique does not, however, imply an understanding of its assumptions, limitations or suitability" (§2.4). With "essentially no barrier to running naïve analyses through AI", users may bypass experts, as was feared with statistical software (§3.5). The modelling step "is where AI is weakest" (§2.3).
- **For the talk**: this is a useful counterweight. Autoformalization could make the *deduction* trustworthy for an experimentalist, but the report's evidence says the failure point for non-specialists is the *formulation* (L2 in note 01's terms). A Lean certificate does not check that.

### Q7. Does the formal proof need to match the handwritten one? What role for hand-picked lemmas?
- The report treats **statement** match as essential and **proof** match as an open concern, not a requirement. AI speeds formalization "subject to human checking that formal statements match their natural-language counterparts" (§2.2).
- **Against proof-match mattering for correctness, but for it mattering for understanding**: AI formalizations are "opaque, making it hard to extract human understanding" (§2.2). FLT's 13M lines are "likely far longer than necessary" (A.2). Producing "compact, readable code still require[s] significant human intervention" (§1.2).
- **The long-run risk** (§3.1): "human-digested" mathematics may become "a small part of the body of mathematical knowledge", with results "quite possibly correct, but possibly unreadable" sitting in repositories without coherence.
- **Hand-picked lemmas**: not discussed directly. The §1.1 workflow (the human supplies the proof structure, the AI fills it) and the human-blueprint successes in A.2 ("last mile on a known roadmap") are the closest. They suggest that a human-chosen skeleton is how the successful projects actually worked.

### Q8. How have Mathlib, Tau Ceti and other big Lean libraries changed how labs and groups publish?
- **Lean as the default certificate**: Lean "is becoming both the standard route to certifying AI-generated results and the means by which AI checks its own work, generating training signal" (§1.2). 42% of OpenAI's 719 manuscripts carry Lean proofs (§2.2).
- **Public infrastructure enabled the lab results**: the publicly funded Buzzard FLT project is "what enabled AI agents to complete a Lean formalisation of FLT in September 2026" (§2.2). The report uses this to argue that the UK should fund formal libraries.
- **Training data**: AlphaProof autoformalized about 1M problems into about 80M Lean statements. Because the checker anchors the loop, "model collapse" is less of a concern (A.5). Provenance metadata such as Palomar's declarations "matters for training as well as for credit" (A.5).
- **Tau Ceti**: AI-written and AI-reviewed, about 3M lines, larger than Mathlib (A.4). Mathlib reportedly still does not accept AI formalizations (§2.2). This leaves two libraries with different standards. Note 01's worry was that CFSG rests on Tau Ceti; the report confirms the scale but doesn't discuss the trust issue.
- **Fragile funding** (§1.3, §4.7, C.3): formal infrastructure depends on a handful of donors (XTX, Gerko). Mathlib's reviewer ratio is 65:950. The report asks for formal libraries to count as research outputs in the REF and for long-term public stewardship.

### Q9. What skills does a graduate student need for the next decade? What is the human role?
- **Skills named** (§2.6, §3.3, §4.1): judging which methods and analyses are appropriate; understanding assumptions and design choices; validation; communication; training in "formalisation, validation and the critical use of AI alongside core mathematics" as a standard part of programmes.
- **The tension in the PhD** (§3.3): writing code, and perhaps building proofs from scratch, "may become less critical, yet expertise in both is what allows researchers to direct AI tools effectively". The PhD is both training (where AI helps less) and the start of a research programme (where it helps a lot). **Students who abstain for good training reasons finish with fewer outputs and may lose out in hiring.**
- **Assessment**: in-person exams without AI; AI-permitted coursework graded on formulation, method choice, validation and communication; more vivas (§3.3). For hiring: judge a small number of best outputs, use viva-style questioning at the margin, and see Oxford's joint CS/Maths/Stats statement (§3.2, §4.4).
- **Credit for framing**: "where the difficulty increasingly lies in framing a problem rather than solving it, credit should attach to the framing", for example through dated public records of problems (§3.2).
- **Wellbeing** (§3.3): fear of scooping, and "a constant team of AI sessions that makes any idle moment feel like an opportunity lost".
- **The optimistic case** (§2.6): mathematics is an early adopter, so its PhDs have seen AI diffusion first-hand and may be especially sought after.
- **Pointers**: Leslie Goldberg's reflection on PhD project choice; the "Summit on PhD Math Education in the Age of AI".

### Q10. The Lean bug and the false Collatz disproof
- A.3 lists it under "gaming the proof checker": a "sorry-free" Collatz "disproof" exploited a kernel bug (Jul 2026); AI bug hunts found several kernel and runtime routes to `False`, fixed in **v4.33.1**. Leo de Moura is quoted saying AI-generated proofs are to be considered a potential source of malicious proofs (post-mortem, Aug 2026).
- §2.2 presents the result positively: AI bug hunts have "hardened the Lean kernel itself".
- **Framing difference**: note 02 records that Ramana Kumar built the exploit deliberately, by hand, to show the flaw. The report's table, headed "documented failure modes" of AI, could make readers think an AI found or caused it. Check before using either framing.

### Q11. How much should human understanding count in deciding whether to publish?
- The report's answer is structural: **separate the decisions**. Correctness can be machine-assisted; "significance and understanding" are "human-led" (§4.6). A result could be certified correct and still go through a different route from human-understood work.
- **Evidence that understanding is lagging**: most AI-announced results "have not undergone peer review, and there is a lack of human understanding about the details of many of these proofs, and to what extent they use existing work" (A.1.3). Write-ups are impenetrable (OpenAI release) or uncheckable in the time allowed (First Proof P7).
- **Tao, as quoted** (A.4): further blind optimization of problem-solving alone "is now actively harmful to the long-term health of mathematics".
- **Assessment** (§4.4): "reward understanding and long-term contribution over volume". Exposition, formalization, curation and refereeing should count as scholarly contributions.

### Q12. Compute costs: how to reduce them, and how to budget for a graduate student
Appendix B is the main resource. Key figures (all £, Oct 2026):
- **Per problem** (§1.6, B.1): routine attempts cost from a few pounds (single frontier query) to a few hundred (multi-agent harness). First Proof cost per pass **fell 78% for a single query (£18 → £4) and 60% for ProofCouncil (£401 → £158) between June and October**. Batch 3 overall: £8,129 for 23 passes.
- **Flagships** (B.1) [report estimate, output tokens only at list price]:

  | Project | Tokens | Estimated cost |
  |---|---|---|
  | Navier–Stokes | about 130B tokens, 10,000 agents, 88 h | about **£4.9M** (£2.45M at batch prices) |
  | FLT | about 6B tokens | **£91k–226k** |
  | OpenAI release | | £20–200 per kept result; £220–2,200 per result family |
  | Epoch FrontierMath Erdős | extra attempts beyond the default budget | about £33k per solution |

- **Per researcher per year** (B.4). The report's "heavy user" uses 110M output tokens a year; the "agentic user" uses 10× that.

  | Route | Heavy user | Agentic user |
  |---|---|---|
  | Top-tier subscription | £905–4,527 (allowances change unilaterally) | |
  | Frontier API (GPT-6 Astra) | £5,200 | £52,000 |
  | Claude Opus 5.5 or Gemini 4 Argon | £2,100 | £21,000 |
  | Mid-tier models | £1,000 | £10,500 |
  | Open-weight API (DeepSeek V4-Pro) | £225–450 | £2,250–4,500 |
  | Shared local node | about £750 | about £7,500 |

- **Direction of costs** (B.3): fixed capability gets about **5–10× cheaper a year**; frontier use gets **3–18× costlier a year** (Gundlach et al., arXiv 2511.23455). Some prices are rising: Gemini API prices double from 1 Dec 2026; ChatGPT Pro allowances were cut. The report argues that as labs move toward public listing (S-1 filings), frontier prices will rise. **"Research budgets should plan for the top tier, not for today's promotional prices."**
- **Ways to reduce cost**:
  - Batch APIs halve prices.
  - Last year's capability is cheap.
  - Small specialised open provers (4–32B) beat a 671B model on MiniF2F with LoRA fine-tuning on one 8×H100 node (B.4).
  - A shared consortium node costs about **£215k a year central, about £6.8 per million output tokens**, serving about 290 heavy users. Throughput and utilisation matter more than hardware cost.
  - Sector-wide negotiated licences.
  - SAIR Open Math OS (free, but about a year behind the frontier).
- **Caveat on open weights**: in First Proof Batch 3 the open-weight entry scored 0/10, every submission had major errors, and it cost about $2,000. The gap for research mathematics is "substantially wider" than Epoch's four-month general estimate (B.1, B.4).
- **For a grad-student budget** (my synthesis, not the report's): the report's twelve-month ask is that **token costs be eligible on grants** (§4.3). Its heavy-user profile (about 10 deep reasoning sessions a day) costs **about £1,000–5,200 a year on APIs**, or £905–4,527 on subscriptions. Agentic use is a grant-scale cost. A sensible student line is mid-tier API plus a top-tier subscription, with occasional frontier runs costed per project. Only 11% of researchers currently get institutional funding for their main tool.

### Q13. How does autoformalization change the scope of research?
- **Wider scope**: "discovery at scale", completing technical work, connecting results across subfields (§2.1). Applied researchers find models "excellent at generalising initial results, so that core ideas quickly become widely applicable techniques" (§1.4). There are "more ambitious models", extending what a skilled modeller can do (§2.3). Self-expanding formal libraries are "within reach this decade" (A.6).
- **Narrower scope, the counter-risk** (§3.2): agendas and PhD recruitment may concentrate on "problems easily amenable to current AI (e.g. benchmark-driven combinatorics)" at the expense of new definitions and slow theory-building. The Hao et al. figures (−4.6% topics, −22% engagement) and the 28 Fields Medallists' letter back this up. Researchers may also avoid hard problems for fear of being scooped.
- **Scenarios** (A.7): central case for about 2028 is "most well-posed research labour automated", with people concentrating on "specification, modelling, digestion and theory". Signals to watch: Mathlib-quality libraries growing tenfold; First Proof retiring proof-only tests. [report view]

### Q14. The convex hull and semigroup analogies
- **Convex hull, explicitly**: AI is strongest "where a proof lies within the 'convex hull' of existing techniques, that is to say where a combination of pre-existing approaches leads to success" (§2.1).
- **Supporting evidence**:
  - First Proof Batch 3, P5 "turned out to follow from combining two existing papers, and every correct AI solution took that route". 4 of 25 candidate problems were discarded because AI already solved them (A.2).
  - Systems did best where a problem was structurally similar to existing work (Batch 2).
  - The FunSearch bin-packing result was matched by a two-parameter heuristic on a laptop: "primarily empirical optimization, not conceptual discovery" (§2.1).
- **A mechanism for the hull** (A.5, Ceiling 1): RL with verifiable rewards "raises first-attempt accuracy but does not find reasoning paths absent from the base model" (Yue et al., NeurIPS 2025). Distillation from a stronger model *does* add new patterns. If this holds at scale, "proving power keeps rising while conceptual novelty stays tied to the human-derived prior". This is the hull analogy stated in ML terms, and it may be the strongest technical support for it in the project.
- **Points outside the hull?** The "last mile" label "no longer covers everything": the Jacobian, unit-distance and Grothendieck counterexamples were not completions of a human roadmap, "though they built on existing constructions" (A.2). Counterexamples are "in effect creative proofs" (§1.1). Scenario A's signal to watch is whether any AI result is as surprising in method as the cap-set breakthrough (Gowers's test) (A.7).
- **Semigroup**: not mentioned. The report's language of *combining* pre-existing approaches fits a closure-under-composition picture better than a convex combination. Composing two techniques gives a new technique, which is semigroup-like generation rather than interpolation. If the talk uses both analogies, this passage is the textual hook.

---

## 4. Short quotes for slides (verify against the final version)

All quotes are under 15 words; the full text is in the PDF.
- "The bottleneck in mathematical research is shifting from technical work to expert attention and judgement." (exec. summary)
- "systems built for a world in which proofs were scarce now face abundance" (§3)
- "no verifier, no flywheel" (A.5)
- "Research budgets should plan for the top tier, not for today's promotional prices." (§1.6)
- Kontorovich, quoted in A.3: the alignment gap "will never be solved purely in software".

---

## 5. Recommendations relevant to the talk (§4, condensed)

The report lists eight needs, each with 12-month and 3–5-year actions.
1. People and skills
2. Independent evidence: First Proof-style evaluations extended to modelling, statistics and OR, plus an independent "observatory"
3. Access: token costs eligible on grants, sector licences, shared open nodes
4. Assessment and credit
5. Research investment, protecting curiosity-driven work
6. Publication: separate correctness from significance and understanding; a bulk-AI route; a verified registry with overlay journals
7. Knowledge infrastructure: formal libraries funded as infrastructure
8. Shared norms, including a standing forum with AI developers on peer review before announcement and disclosure of prompts and resources

---

## 6. Where it adds to, or pushes against, notes 01–05

- **Adds to 01's L1/L2/L3 table**: an institution has now proposed acting on it. Correctness goes to machine plus formalization; significance and understanding stay human.
- **Supports 03's "production scaled, checking did not"** with primary figures. It adds the Mathlib reviewer ratio as a measure of checking capacity *inside* the formal world.
- **Supports 04/05** (applied fields have a different verification culture), now from a body that represents pure math too. It adds benchmark evidence: PDEAgent-Bench, ORAgentBench, many analysts.
- **Pushes against a too-tidy formalization story**: Mathlib rejects AI formalizations; they are opaque; and there is a "divide between mathematics that is readily formalisable and mathematics that is not".
- **New angle for the talk**: **sovereignty and access** (the export-control outage, the dependence on one donor, the absence of public open maths models). Notes 01–05 hardly cover this. It fits Q12.

---

## 7. Still to verify

- [ ] Get the final published version; this is a pre-publication draft. Check whether figures or recommendations changed.
- [ ] "Mathlib reportedly does not yet accept AI-generated formalisations" (§2.2): find Mathlib's actual policy statement.
- [ ] Tau Ceti about 3M lines exceeding Mathlib (A.4): check the Avigad–Buzzard–Commelin et al. Xena post, "How to formalize all of mathematics" (16 Oct 2026).
- [ ] Mathlib 65 reviewers / 950 contributors: source not given.
- [ ] Kontorovich NAS quote (Jul 2026): find the primary source.
- [ ] The six probability/statistics journals that paused on 19 Oct: which journals?
- [ ] The export-control outage of 12 Jun – 1 Jul 2026: the report found no Commerce/BIS notice and relies on an Anthropic statement plus secondary sources.
- [ ] The Navier–Stokes "priority dispute" (§3.4): not explained in the report; find the primary account.
- [ ] Yue et al. (NeurIPS 2025) for the convex-hull mechanism: read the paper before using it on a slide.
- [ ] First Proof Batch 3 report (hexagon:2610.00244) for the abstention and exposition results.

## 8. Internal inconsistencies spotted

- **Jacobian counterexample attribution**: §1.1 says "(Buzzard, Jul 2026)", but A.1.3 says "Levent Alpöge, July 2026". It is probably found by Alpöge (or an AI system) and blogged by Buzzard. Check.
- **"9 of 10" on First Proof** (§1.5) is the ProofCouncil *harness*; the best single model call was 7/10 (A.1.1).
- **"Mathlib" size**: "2.3 million [lines] for Mathlib over nine years" (A.5) against "Mathlib roughly 2M" in note 01. These are close enough, but use one figure.
- **Collatz framing**: see Q10.

## Sources

- Reisinger, Bearon, Bloom, Gaskell, Leslie, Siganporia, *The Mathematical Sciences in an AI-enabled World: Opportunities, risks and community needs*, Academy for the Mathematical Sciences, pre-publication draft, 28 Oct 2026. Local: `~/Zotero/storage/7MDTEDEM/`. Page numbers above are PDF pages.
- Primary sources it cites that are most worth fetching next: First Proof Batch 3 (hexagon:2610.00244); Bastounis–Circelli–Hansen (arXiv 2610.08144, already in note 01); PDEAgent-Bench (arXiv 2605.09636); ORAgentBench (arXiv 2606.19787); Bertran–Fogliato–Wu (arXiv 2602.18710); Yue et al. (arXiv 2504.13837); Gundlach et al. (arXiv 2511.23455); Patel et al. (arXiv 2609.28603); Hao et al. (arXiv 2412.07727); Avigad et al., "How to formalize all of mathematics" (Xena, Oct 2026); ICIAM statement (Sep 2026); AGMAI release guidelines (Sep 2026).
