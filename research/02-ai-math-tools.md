# AI math tools: the layer between doing math and verifying it

*Research notes for the "Math 2.0" talk. Compiled 2026-11-09. This follows on from [01-formalization-landmarks.md](01-formalization-landmarks.md).*

**Scope.** These are tools that connect ordinary mathematical practice to AI-generated or AI-curated results, plus the scaffolding that makes autoformalization possible. Agents are included, but they are not the focus. The tools are grouped by the job they do. Each group is tagged with the verification layer from note 01 it mainly serves:

- **L1, kernel:** the proof compiles and checks.
- **L2, statement fidelity:** the formal statement says what the theorem says.
- **L3, proof fidelity:** the formal proof follows the paper's argument.

**Reliability.** Claims from vendors are marked **[self-reported]**. Where a "Q" tag appears, it links the item to a question in `questions_of_interest.md`.

---

## The map in one picture

```
 Human math practice                                              Verified, shared knowledge
 ────────────────────                                             ──────────────────────────
 idea → informal proof → [C. blueprint / plan] → [D. coordination] → [E. engines] → [F. trust] → [G. registry / review]
            ↑ ↑                    ↑                     ↑                ↑
   [A. copilots in the editor]  [B. search & retrieval]  (agents working in parallel)
                                              underneath it all: [H. libraries: Mathlib, TauCeti, PhysLib, CSLib …]
```

The trend through 2026: groups **A and B** were built for a human writing Lean. Groups **C and D** turned out to be what lets *agent swarms* work at scale. Groups **F and G** were the ones least ready when abundance arrived.

---

## A. Copilots in the editor: a human writes, AI suggests (L1)

| Tool | What it does | Status / notes |
|---|---|---|
| **LeanCopilot** (LeanDojo team: Song, Yang, Anandkumar et al.) | Runs an LLM inside Lean. `suggest_tactics` shows clickable next steps. `search_proof` combines LLM tactics with `aesop` to search for multi-step proofs. `select_premises` retrieves relevant lemmas. Users can plug in their own model through an external API. | [GitHub](https://github.com/lean-dojo/LeanCopilot) shows about 1.3k stars and an MIT license. The paper was at NeuS 2025 ([arXiv 2404.12534](https://arxiv.org/html/2404.12534v3)). I found **no 2026 release**: it belongs to the "copilot for a human" era that agent workflows have since overtaken. LeanProgress (2025) builds on it. |
| **LeanHammer** (Zhu, Clune, Avigad, Jiang, Welleck, 2026) | Premise selection with an encoder-only transformer, plus automated reasoning. It plays the role Sledgehammer plays in Lean. | Cited in corpus post 848 as AI that is not an LLM. |
| **`grind`, `aesop`, `simp`** | Automation built into Lean and Mathlib that is not machine learning. `grind` can sometimes finish a tedious computation in one call. | It is the reason formal proofs are not always longer than informal ones (post 848). |
| **Isabelle Sledgehammer** | The precedent from before LLMs: calls external automated provers from inside the editor. | Useful as a historical contrast: AI assistance in proof assistants long predates LLMs. |

**For the talk:** copilots keep the human as author and the AI as autocomplete. They are the most comfortable tools for traditional practice, and in 2026 the least important ones.

---

## B. Search and retrieval: finding what is already known (L1, partly L2)

| Tool | What it does |
|---|---|
| **LeanSearch** | Natural-language search over Mathlib |
| **Loogle** | Search by type signature or pattern |
| **Lean Finder** | Semantic search by mathematical meaning |
| **Lean State Search** | Search for lemmas that close a given goal state |
| **lean-lsp-mcp** ([project-numina](https://github.com/project-numina/lean-lsp-mcp)) | An MCP server that gives an agent such as Claude Code or Codex access to Lean's language server (diagnostics, goal states, hover documentation), with the search tools above built in. Install with `claude mcp add lean-lsp uvx lean-lsp-mcp`. |

**For the talk:** lean-lsp-mcp is the plumbing that turned general coding agents into Lean agents. It is a small piece of infrastructure with a large effect. Most of the swarm projects in note 01 depend on this kind of interface.

---

## C. Blueprints and planning: what humans read (L2, L3)

This group answers the hand-picked-lemmas question (Q: "role of hand-picked lemmas in guiding the human-facing narrative … machine-driven backend").

| Tool | What it does | Why it matters |
|---|---|---|
| **leanblueprint** (Patrick Massot, 2020) | A plasTeX plugin. You write the informal proof in LaTeX, with each lemma tagged by its Lean name. It renders a **dependency graph coloured by formalization status**. | It became the standard way to organize formalization projects: Liquid Tensor, PFR, FLT, sphere packing, Carleson. **It is the original way to separate narrative from backend.** |
| **LeanArchitect** (Zhu, Monticone, Avigad, Welleck; [arXiv 2601.22554](https://arxiv.org/html/2601.22554v1), ITP 2026) | Reverses the direction: a `@[blueprint]` attribute on Lean declarations **generates** the blueprint from the code. Dependencies are inferred and "proved" status is detected automatically. | **Benefits:** migrating Tao's PrimeNumberTheoremAnd took about a day, and Tao found the auto-colouring "very pleasant." The inferred graph **exposed a semantically wrong lemma (Erdős 392)**. Converting 5 large projects (Carleson, Brownian Motion, Infinity Cosmos, FLT, PNT+) found unused nodes and missing edges. In a human–AI case study, GPT-5 Pro drafted a blueprint with `sorry` placeholders, Aristotle filled most of them, and a human closed the last 3. **Limits:** asking the LLM to "refine" the blueprint did not reliably fix root causes. |
| **Verso Blueprint** ([leanprover/verso-blueprint](https://github.com/leanprover/verso-blueprint), Lean FRO; E. J. Gallego Arias) | Next generation, native to Lean and built on the Verso document system. Informal text sits beside Lean panels, with an interactive graph and automatic progress tracking. | Reference blueprints exist for **FLT** and **sphere packing** (v4.35.0). This is where the official tooling is heading. |
| **Lean Atlas** (Yanahama & Sannai, Nyx Foundation / Kyoto; [arXiv 2604.16347](https://arxiv.org/pdf/2604.16347)) | Turns any Lean project's dependency graph into an interactive viewer, and **filters it down to the nodes a human must check semantically**. | It proposes a quality standard, **"aliqued" code: code that has passed human semantic verification.** For PNT+, Carleson and Brownian Motion it cut the nodes needing review by **94–99%**. The definition-heavy XMSS project saw only 27%, and PhysLib 69%. **This is direct evidence for the "hand-picked lemmas" model: if the definitions and the top statements are right, humans review only a small slice of the graph.** |
| **Stacks tags → Lean** (Axiom) | Each Stacks tag is linked to its Lean declaration, and the text can be read beside the code ([stacks.axiommath.ai](https://axiommath.ai/research/the-stacks-project-formalized/)). | A blueprint applied after the fact to a 7,500-page reference. |

**A working answer to the hand-picked-lemmas question.** In this model:

1. The **blueprint is the paper**: the human-facing narrative, a curated set of lemmas, and the definitions.
2. The **Lean graph is the appendix**: machine-produced and machine-checked.
3. Humans certify the **definitions, the top statement and the milestone lemmas**. That is L2 on a small set of nodes.
4. They do **not** certify the machine's internal route. That is L3, given up deliberately.

Prove2Me makes the same argument explicitly (see D): "a wrong lemma can't help prove a correctly stated goal." The risk is that the "faithful" proof's argument is not the paper's argument, as with the m+4 versus m+5 derivatives in Navier–Stokes (note 01, §5). That only matters if you care about the paper's own argument and not just the theorem.

---

## D. Coordination platforms: scaffolding for agent swarms (L1, L2)

Every major formalization in 2026 relied on **shared external state**: a graph of statements, issues, and immutable targets. The lesson from FLT is that agents without that structure lost track of the project.

| Tool | How it works | Evidence |
|---|---|---|
| **Prove2Me** ([prove2.me](https://prove2.me/about); [arXiv 2608.28433](https://arxiv.org/pdf/2608.28433)). Started in a Columbia class taught by Kunal Marwaha and Henry Yuen; built out by Shuze Chen and Tianyi Peng. | **Missions** come from papers, textbooks, or open problems. A human **captain** writes the core: the headline goal, the definitions, and the milestones. **Theorem statements are immutable** Lean stubs ending in `sorry`. A **proof sketch** may import unproved theorems, and each open import becomes a new task, which builds a **DAG**. Agents connect by fetching `start.md`. Lean experience is not required. | It was the coordination layer for **Anthropic's FLT** formalization ([Anthropic](https://anthropic.com/research/formalizing-fermats-last-theorem)). Attempts without the DAG contributed only about 7% of the final lines. **Fidelity (L2):** captains audit the core against the source, an independent agent back-translates the Lean into plain math, and moderators approve public missions. **Intermediate lemmas are not audited, by design.** A misformalized item cannot be edited, only **deprecated** and replaced. **Credit:** contributors permanently own the theorems they prove, and imports earn the original prover credit and "trust score." **Cost:** the FAQ says a $200/month Claude Max plan covers roughly a textbook. Marwaha argues for it as a **"world mathematical commons"** in corpus post 1907. |
| **TauCeti** ([Lean FRO](https://lean-lang.org/use-cases/tau-ceti); incubated with the Mathlib Initiative) | A library built by AI, downstream of Mathlib. **Humans write the roadmaps.** AI workers open pull requests. **Adversarial AI reviewers** check whether definitions and statements match the roadmap and whether the code is fit for others to build on ([TauCetiReview](https://reservoir.lean-lang.org/@TauCetiProject/TauCeti)). Anyone with a Claude Code or Codex account can run a worker. | Recent results include Burnside's pq theorem, Carathéodory's boundary extension, and Schur–Weyl duality. **Axiom's CFSG statement is taken from TauCeti** (note 01, §2). When Mathlib gains the same material, TauCeti switches over. **This is the second-tier "AI Mathlib" model.** |
| **Meta's textbook scaffold** ([arXiv 2604.03071](https://arxiv.org/html/2604.03071v1)) | About 30k Claude 4.5 Opus agent instances, with roles for sketching, proving, mathematical and engineering review, maintenance, triage, and progress. They shared a git repository with trunk-based development, a file-based issue tracker, and a merge queue. | Grinberg's *Introduction to Algebraic Combinatorics* (over 500 pages): about 130k lines and **all 340 targets in about one week**, for roughly **$100k, or about $200 a page**. **Failures:** one partition type defined three separate times, inconsistent Bender–Knuth definitions, and work wasted on out-of-scope material. The authors admit **some statements may not be faithful.** The code and a side-by-side blueprint site are public. **This is the most candid cost figure available.** |
| **Axiom's swarm infrastructure** (CFSG, Stacks) | A proof map with 108 milestones and about 380 tasks. Agents claim work through GitHub issues and report in Slack. Engineering includes distributed build caching and external certificates for finite computations. | [self-reported] Note 01, §§2–3. |

**For the talk:** the scaffolding is not optional. The step from "agents can prove lemmas" to "agents formalized FLT" came from **project management**: DAGs, immutable targets, issue trackers. Those are human organizational tools adapted for machines. Q-parallel: this is exactly how software engineering handles AI-generated code, with tests, continuous integration, code review, and small pull requests (about 100 lines on average in the Meta run).

---

## E. Engines that prove and autoformalize (L1)

| Engine | Access | Notable results | Notes |
|---|---|---|---|
| **Gauss** (Math, Inc.) | Projects are [public on GitHub](https://www.math.inc/gauss-on-github). The tool itself is not publicly available as far as I could find. | Strong PNT (3 weeks); sphere packing in dimensions 8 and 24 (about 200k lines); solo autoformalizations of Dvir's finite-field Kakeya proof, the Riemann hypothesis for curves over finite fields, and the security of the ZK-FRI protocol | [self-reported]. Viazovska and Buzzard are "Veritas Fellows." **Works from human blueprints.** |
| **Aristotle** (Harmonic) | A consumer app plus a **public API** with limited free access ([directory, Jun 2026](https://tooldirectory.ai/tools/harmonic)) | IMO 2025 gold, with formal proofs. Ranked first of 7 on MathArena's ArXivLean evaluation (17.07%, Mar 2026) ([MathArena](https://matharena.ai/models/aristotle_aristotle)) | Combines Lean proof search, informal lemma generation, and a geometry solver ([arXiv 2510.01346](https://arxiv.org/html/2510.01346v1)). **The most widely available research-grade formal prover.** It filled most of the `sorry` nodes in the LeanArchitect case study. |
| **AxiomProver + AXLE** (Axiom) | **AXLE**, the Axiom Lean Engine, is **free and public** (released [Mar 5, 2026](https://axiommath.ai/research/releasing-axle)). It offers `verify_proof`, `extract_theorems`, and a Comparator endpoint through a REST API, Python package, command line, and an MCP server. **AxiomProver itself is closed**: no weights, prompts, or hosted generation. | CFSG and Stacks (note 01). Axiom says 42/42 at IMO 2026 [self-reported]. | Axiom raised a $200M Series A. One changelog mentions an AXLE switch to Rocq ("AXRE"); this is unresolved, so check before quoting. |
| **AlphaProof Nexus** (Google DeepMind; [arXiv 2605.22763](https://arxiv.org/html/2605.22763v1), May 2026) | **Research system only, with no API.** The Lean proofs are on GitHub. | **9 of 353 open Erdős problems** (two open for 56 years) and **44 of 492 OEIS conjectures**, at a few hundred dollars per problem | Includes an **audit phase for misformalization**. Some Erdős statements turned out ambiguous (for example, which notion of "density" was meant), were corrected, and then proved. |
| **General agents**: Claude Code, Codex, and others with lean-lsp-mcp | Commercial | FLT, about 13M lines in 11 days (Anthropic); the TauCeti and Prove2Me workers | General models plus scaffolding (group D) have **largely caught up with** specialized provers on large projects. |
| **Discovery engines, not provers**: AlphaEvolve, OpenEvolve, ShinkaEvolve | Mixed | Constructions and bounds | Listed in corpus post 1043 as tools for a "new type of paper mill." |

### E′. Infrastructure the community controls: Open Math Model / Open Math OS
| | |
|---|---|
| **What** | [Open Math Model](https://www.openmathmodel.org/) is an initiative of the **SAIR Foundation**, which Terence Tao co-founded, to build **open-weight** models, tools and governance for mathematicians. Its tagline: "Infrastructure for Math 2.0." **Open Math OS** ([os.openmathmodel.org](https://www.openmathmodel.org/)) is a shared research and scientific-computing environment. |
| **When** | Announced **Sep 18, 2026**, with a call for partners. Open Math OS soft-launched **Oct 16, 2026** ([LDS](https://letsdatascience.com/news/sair-soft-launches-open-math-os-2fac7184), [LDS partner call](https://letsdatascience.com/news/sair-opens-partner-outreach-for-open-math-model-initiative-9ba8c64e)). |
| **What it offers now** | Hosted **existing open-weight models**, not yet a model of its own: DeepSeek V4.1 Flash, Kimi K3, GLM 5.3, Mistral Large 4.0, Nemotron 3. There is a cloud environment with 100+ preinstalled math and science tools, including **Lean and Mathlib**. Effort levels run from Low to **"Ultramath,"** which runs several agents in parallel and reports findings, including "Lean check passed." Teams can collaborate and control their data. |
| **Goals** | Open-licensed weights, published training methods, documented data sources and permissions, and reproducible evaluations. The plan is a math-focused model **post-trained from an existing open model**, with partners still to be named. The use cases are routine tasks: checking references, exploring examples, generating code, formal proofs. |
| **Data and access** | Teams apply with a description of their research at apply.openmathmodel.org. Work stays private unless shared and is used for training **only with explicit consent**. The target is **free compute for 10,000 mathematicians**, starting with 1,000 teams by November 2026. Discussion is on Zulip. |
| **Why it matters for the talk** | It is the **public-option** answer to the problems in note 01 and corpus post 224 ("On protecting mathematics from LLM companies' monopoly"): closed provers, prompts that are never released, and disputes over data and priority such as Navier–Stokes. **The community's work does not feed a lab's training without consent.** **Open questions:** whether open-weight models can match closed frontier systems on research-level formal work, and who will fund it beyond the free-credit phase. |

**For the talk:** a counterpoint is corpus post 674, "We Need a Stockfish for Math" (Hartstein). It argues that engines built around search, as AlphaProof was, should beat LLMs, just as Stockfish beats LLMs at chess. The 2026 evidence is mixed: general LLM agents with good scaffolding produced the largest formalizations.

---

## F. Trust and fidelity: checking the checker (L1 and L2)

This group answers the question "Investigate the Lean bug leading to a false disproof of the Collatz conjecture."

### Statement-matching tools (L2, partly mechanical)
- **Comparator** (Lean FRO): checks that a solution proves **exactly** the statement in a "challenge" file, with no more than the allowed axioms, and is accepted by the kernel. It has been folded into `lake comparator` from Lean 4.35. It was used for **FLT**, where the statement matched Mathlib's own FLT, and for OpenAI's release. Known issue: occasional false negatives when a statement is equal in meaning but not identical (for example, under `open Classical`) ([Zulip](https://leanprover-community.github.io/archive/stream/113488-general/topic/Does.20anyone.20use.20Comparator.3F.html)). **Comparator only moves the problem**: the challenge file itself still has to be faithful.
- **Back-translation** (Prove2Me), **adversarial AI review** (TauCetiReview), **misformalization audits** (AlphaProof Nexus, LeanMarathon [arXiv 2606.05400](https://arxiv.org/html/2606.05400)), and **"aliqued" human sign-off** (Lean Atlas).

### Kernel trust (L1): the Collatz incident, July–August 2026
- **Jul 25:** Ramana Kumar published a Lean repository with no `sorry` that "disproves" the Collatz conjecture. It **passed Lean's kernel and the independent Nanoda checker.** It was built deliberately as an exploit.
- **The bug:** the kernel did not check that projections in **nested inductive declarations** referred to the right structure. Combined with a hash collision in expressions, this allowed type confusion, so **a malicious metaprogram could produce an axiom-free proof of False (0 = 1).** Ordinary elaboration could not trigger it: the bad declaration had to be passed to the kernel directly.
- **Jul 28:** Kiran Gopinathan reduced the exploit to a proof of False and filed issue #14576. Leo de Moura's fix landed about an hour later (nightly-2026-07-29, PR #14577). The advisory ([oss-sec, Aug 2](https://seclists.org/oss-sec/2026/q3/381)) covers **all Lean 4 versions up to v4.31.0**, with CVSS 7.1. The **leanchecker replay also accepted the forged proofs.** Secondary sources say Nanoda's miss came from a *separate* bug in an outdated build.
- The advisory quotes de Moura saying that AIs are good at exploiting kernel soundness bugs: "This is going to keep happening."
- **Mitigation:** upgrade, then re-check artifacts with `--trust=0`. Thomas Hales reportedly called the period a "Summer of Soundness Bugs."
- **Paulson's response** ([blog, Jul 30](https://lawrencecpaulson.github.io/2026/07/30/Collatz.html)): kernels with rich built-in features such as nested inductives are where these bugs live. The LCF approach (Isabelle, HOL Light, HOL4, the verified Candle) derives those features from a few primitive axioms, outside the kernel. Independent checkers built on the **same design** fail in the **same way**.

**Why it matters for the talk.** In the old world, an attack on the kernel was not a realistic threat. In a world of abundant proofs, where **agents are optimized to make the build pass**, the kernel faces a constant **adversarial search** for whatever it accepts. Kernel soundness becomes a security problem, not just a logical one. Relevant here: Axiom's CFSG build depends on **custom Lake changes** that have not been released upstream (note 01).

---

## G. Registries, review, and publication (outside L1–L3: the social layer)

This group bears on the questions about publishing, about how formalization can help, and about the role of AI review.

| Tool | What it is | Mechanism | Explicitly **not** |
|---|---|---|---|
| **Palomar** (Lean FRO + ICARM; opened about **Aug 18, 2026**, announced by Tao) | Registry of Lean-verified mathematics; Tao called it a "zeroth approximation" of a preprint server for Lean proofs ([coverage](https://zeli.app/en/story/49355968)) | Submissions are GitHub snapshots pinned to a commit. Lean's kernel and an independent kernel **replay** each proof, and only permitted axioms are allowed. **Comparator** checks the challenge statement. An **LLM checks the informal description against the formal statement**, and the documentation warns this can miss things. Authorship may be human, AI, or mixed, with disclosure. | **Not peer review**, and not a journal publication. Tao is on the advisory board and submitted his Sendov's conjecture formalization. |
| **ProofForum** ([proofforum.org](https://www.proofforum.org); Marco Trombetti, Naples; corpus post 720) | **Human** verification of AI-era mathematics | Hosts papers, or links to an exact arXiv version. **AI checks, community checks, and signed "Certified Referee" verdicts are kept separate.** A result builds up "collective mathematical confidence." | It does not sell acceptance or rankings. It has **no Lean integration**: the human-trust counterpart to Palomar. Corpus post 1097 (Idrissi) cites it for recording **generation, checking, and human verification as separate contributions.** |
| **Google Paper Assistant Tool** ([arXiv 2606.28277](https://arxiv.org/abs/2606.28277); [Google blog](https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/)) | AI feedback before submission, piloted at **STOC 2026** and ICML | An agent based on Gemini reviews and checks the paper | 97% of surveyed authors found it helpful, and it caught about 90% of the planted errors, but the benchmark had **only 26 papers and 29 errors** [self-reported]. Critics worry about authors gaming the review agents and about narrower debate. |
| **OpenAIReview** (UChicago CHAI Lab; [link](https://datascience.uchicago.edu/insights/openaireview/)) | Open-source AI-assisted reviewing | Still working on how to verify claims | |
| **formal-conjectures** (Google DeepMind) and **erdosproblems.com** | Open problems stated formally, used as benchmarks and question banks | Lean statements that the community can fix | **A known misformalization channel**: issue [#5226](https://github.com/google-deepmind/formal-conjectures/issues/5226), the OEIS "disproof" for $0.17. Erdős #124 was restated. |

**The emerging division of labour for the talk:**
- **Palomar** answers "is it machine-verified, and is the statement right?" (L1 plus partial L2).
- **ProofForum** answers "has a human checked it and signed?"
- **Journals** are left with "does it matter, and is it understood?"

No one yet owns L3. The publishing question then becomes **which of these a journal should require**.

---

## H. Domain libraries beyond Mathlib

This group answers the question about Mathlib, TauCeti, and the physics and statistics repositories, and bears on the questions about applied mathematics and experimentalists.

| Library | Scope | Notes |
|---|---|---|
| **Mathlib** | Covers "essentially all of undergraduate mathematics" (corpus post 1907), about 2M lines | Every AI project in note 01 is built on it. Corpus post 2654 (Nuccio): "almost all autoformalisation projects … rely on Mathlib." |
| **TauCeti** | A second tier built by AI, downstream of Mathlib | See D. |
| **PhysLib** (formerly HepLean, then PhysLean; merged with Lean-QuantumInfo; now [leanprover-community/physlib](https://reservoir.lean-lang.org/@HEPLean/PhysLean)) | Electromagnetism, condensed matter, classical mechanics, quantum field theory, quantum information | Has a **two-tier review**: carefully reviewed Physlib, and a lighter **PhyslibAlpha** tier for large contributions, which are likely AI-generated. Lean Atlas reports a 69% cut in nodes needing review. |
| **CSLib** ([arXiv 2602.04846](https://arxiv.org/html/2602.04846v1)) | Lean computer science library | |
| **EconCSLib** ([arXiv 2606.13306](https://arxiv.org/pdf/2606.13306)) | Economics and computation, formalized with AI assistance | An example of moving beyond pure mathematics. |
| **StatsMLlib** ([site](https://statsmllib.github.io/), [GitHub: Lean-MoDS/StatsMLlib](https://github.com/Lean-MoDS/StatsMLlib)) | Probability, high-dimensional statistics, empirical processes, statistical learning theory | About 64.7k lines, 89 to 90 files, 666 theorems, 1,219 lemmas, 352 definitions, **0 `sorry`**. Its policy bans `axiom`, `admit` and `native_decide`. Pinned to Lean and Mathlib v4.35.0 (Reservoir says v4.34.0). It merges the earlier **SLT** and **FoML** projects. Modules are layered: measure theory → topology → linear algebra → analysis → probability → learning theory → statistics. **Selected results:** Dudley's entropy integral; Efron–Stein, Hoeffding, McDiarmid, Bernstein; Gaussian Poincaré and log-Sobolev inequalities; matrix Bernstein; Hanson–Wright; symmetrization, Massart's lemma, Rademacher complexity. The README has **no AI-use policy**, and I couldn't find the organizers' names (they are in AUTHORS.md). This is the clearest library aimed at **ML theorists and applied statisticians**, which bears on the questions about experimentalists and applied mathematics. |
| **Other probability** | Mathlib's probability modules; the Brownian Motion project, which appears in the Lean Atlas and LeanArchitect evaluations | |

**The pattern:** the community copies the **Mathlib-plus-second-tier** structure. There is a carefully reviewed core plus a fast lane for AI contributions, as in Physlib/PhyslibAlpha and Mathlib/TauCeti. On the publication-habits question: almost every lab release now **states its Mathlib dependency and Lean version, and ships a Comparator challenge file** (FLT, OpenAI's 245 formalized families, CFSG). Palomar turns that into a submission format.

---

## Mapping to `questions_of_interest.md`

| Question | What the tools say | Where |
|---|---|---|
| How formalization can help publishing; AI review | Palomar, ProofForum, PAT and Comparator are separating "verified," "human-checked," and "significant" | G, F |
| Parallels between AI-generated code and AI-generated proofs | The scaffolding *is* software engineering: issue trackers, merge queues, continuous integration, small pull requests, review agents, immutable targets as test specifications. The Collatz exploit is the equivalent of a supply-chain attack. | D, F |
| What to hand over to AI | Lean Atlas's 94–99% cut suggests the internal proof graph can go to machines, while definitions and top statements stay with humans. See also corpus post 2451, Kaipel's taxonomy of research tasks. | C |
| Experimentalists and rigorous math | Prove2Me requires no Lean or specialist knowledge, and a Max plan covers about a textbook. PhysLib and EconCSLib supply domain foundations. The catch is that someone must still write a faithful statement. | D, H |
| Does the formal proof need to match the handwritten one? | The blueprint model gives up L3 deliberately ("a wrong lemma can't help prove a correctly stated goal"). The LeanArchitect example of a semantically wrong Erdős 392 lemma, caught through the graph, shows L2 at intermediate nodes still matters for the *narrative*. | C |
| Influence of Mathlib, TauCeti and similar libraries on publication habits | Releases standardized on Comparator challenges, pinned Mathlib versions, and two-tier libraries | H, F |
| Collatz Lean bug | Covered in full above | F |
| Skills for graduate students | Writing statements and auditing definitions, designing blueprints, and acting as a captain or roadmap author, rather than writing tactic proofs | C, D |

---

## Corpus voices on tools (`data/posts.jsonl`)

| id | Author | Post | Takeaway |
|---|---|---|---|
| 1907 | Kunal Marwaha (UChicago; Prove2Me co-builder) | [Towards a world mathematical commons](https://proofsandprompts.com/2026/10/23/towards-a-world-mathematical-commons/) | Formalize everything into one shared graph, with AI companies donating compute |
| 720 | Marco Trombetti (Naples) | [ProofForum: Keeping AI-Generated Mathematics Human](https://proofsandprompts.com/2026/09/22/proofforum-keeping-ai-generated-mathematics-human/) | Collective confidence; credit for the person who repairs a gap |
| 1097 | Najib Idrissi (Paris Cité) | [YAPOAI](https://proofsandprompts.com/2026/10/03/yapoai-yet-another-post-on-ai-ai-understanding-and-mathematical-work/) | Separate a **certificate announcement** from a later **explanatory paper** |
| 674 | Oren Hartstein (Columbia) | [We Need a Stockfish for Math](https://proofsandprompts.com/2026/09/11/we-need-a-stockfish-for-math/) | Specialized search engines versus LLMs |
| 2451 | Maximilian Kaipel (Bielefeld) | [Why and how to transparently disclose AI use](https://proofsandprompts.com/2026/10/28/why-and-how-to-transparently-disclose-ai-use-in-mathematics-research/) | A task taxonomy (knowledge acquisition, objective identification, proof construction, …) that frames "what to hand over" |
| 1043 | Eric Dolores-Cuenca (Yonsei) | [A new type of paper mill](https://proofsandprompts.com/2026/10/01/a-new-type-of-paper-mill/) | Discovery engines (AlphaEvolve and others) as a new paper-mill risk |
| 848 | Seewoo Lee (EPFL) | [(auto)formalization, but why](https://proofsandprompts.com/2026/09/08/autoformalization-but-why/) | AI tools that are not LLMs (DeepMath, TacticToe, LeanHammer); read the code |
| 1862 | Antonio Lerario (SISSA) | [The shape of mathematical knowledge](https://proofsandprompts.com/2026/11/09/the-shape-of-mathematical-knowledge/) | Verso Blueprint, TheoremGraph, MathHub and Stacks as precursors of a knowledge graph |

---

## Still to verify
- [ ] Prove2Me's current scale: 22.3M lines and 70k theorems comes from a social post only. Check [arXiv 2608.28433](https://arxiv.org/pdf/2608.28433).
- [ ] Tao's Palomar blog post and the Palomar documentation, from the primary source. The submission format (challenge, solution, metadata) is confirmed only by secondary coverage.
- [ ] Leo de Moura's official Collatz postmortem; which stable release (v4.33.1?) first contained the fix.
- [ ] Whether AXLE moved to Rocq ("AXRE"); sources conflict.
- [ ] Whether Gauss or Aristotle API access and pricing have changed.
- [ ] StatsMLlib: the organizers (AUTHORS.md), whether AI was used in building it, and any related paper.
- [ ] Possible additions: Isabelle's AFP as a model of a curated archive; Rocq tooling; the Mathlib Initiative itself; erdosproblems.com's AI-solution tracking; Tao's ai-views page.

## Sources
- LeanCopilot: https://github.com/lean-dojo/LeanCopilot · https://arxiv.org/html/2404.12534v3
- LeanArchitect: https://arxiv.org/html/2601.22554v1 · https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2026.25
- Verso Blueprint: https://github.com/leanprover/verso-blueprint
- Lean Atlas: https://arxiv.org/pdf/2604.16347
- Prove2Me: https://prove2.me/about · https://prove2.me/faq · https://arxiv.org/pdf/2608.28433 · https://daplab.cs.columbia.edu/general/2026/09/09/fermats-last-theorem-agents.html
- TauCeti: https://lean-lang.org/use-cases/tau-ceti
- Automatic Textbook Formalization: https://arxiv.org/html/2604.03071v1
- lean-lsp-mcp: https://github.com/project-numina/lean-lsp-mcp
- Gauss: https://www.math.inc/gauss-on-github
- Aristotle: https://arxiv.org/html/2510.01346v1 · https://matharena.ai/models/aristotle_aristotle · https://tooldirectory.ai/tools/harmonic
- AXLE: https://axiommath.ai/research/releasing-axle · https://api.axle.axiommath.ai/v1/docs/
- AlphaProof Nexus: https://arxiv.org/html/2605.22763v1
- Collatz / kernel bug: https://seclists.org/oss-sec/2026/q3/381 · https://lawrencecpaulson.github.io/2026/07/30/Collatz.html · https://gigazine.net/gsc_news/en/20260803-collatz-lean-kernel-bug/
- Comparator: https://reservoir.lean-lang.org/@leanprover/Comparator
- Palomar: https://zeli.app/en/story/49355968 · https://runtimewire.com/article/palomar-lean-proof-registry-ai-mathematics
- ProofForum: https://www.proofforum.org
- Google PAT: https://arxiv.org/abs/2606.28277 · https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/
- OpenAIReview: https://datascience.uchicago.edu/insights/openaireview/
- PhysLib: https://reservoir.lean-lang.org/@HEPLean/PhysLean
- StatsMLlib: https://statsmllib.github.io/ · https://github.com/Lean-MoDS/StatsMLlib
- Open Math Model / OS: https://www.openmathmodel.org/ · https://letsdatascience.com/news/sair-soft-launches-open-math-os-2fac7184
- CSLib: https://arxiv.org/html/2602.04846v1 · EconCSLib: https://arxiv.org/pdf/2606.13306
