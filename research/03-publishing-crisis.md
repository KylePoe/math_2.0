# The publishing crisis: what AI floods and what formalization can rescue

*Research notes for the "Math 2.0" talk. Compiled 2026-11-09. This follows on from [01-formalization-landmarks.md](01-formalization-landmarks.md) and [02-ai-math-tools.md](02-ai-math-tools.md).*

It answers three questions from `questions_of_interest.md`:
- the recent problems facing the publishing industry and how they relate to AI;
- how formalization can help, and the role of automated AI review;
- partly, the parallel between AI-generated code and AI-generated proofs.

**Reliability.** **[secondary]** means I saw the claim only in press coverage or a summary, not in the primary document.

---

## 0. The thesis: production scaled, checking did not

Nee, Zhong and Ni ([arXiv 2609.04872](https://arxiv.org/abs/2609.04872v1)) end their study of the 2026 arXiv surge by naming **verification, selection, and attention** as the central constraints. That framing works for the talk:

| Bottleneck | What it was before AI | What happened in 2026 | Can formalization help? |
|---|---|---|---|
| **Verification**: is it correct? | Referees, slowly | Submissions up 33–79%; the number of referees unchanged | **Yes, for L1** (the kernel check from note 01). Only partly for L2, statement fidelity. Barely for L3, proof fidelity. |
| **Selection**: does it matter? | Editors and journal prestige | Journals paused submissions; editors cannot find referees | **No.** Significance is not a formal property. |
| **Attention**: will anyone read it? | Talks, citations, community | 722 papers in one day; proofs that are "unreadable without AI help" | **No.** If anything, a 43M-line certificate needs more attention, not less. |
| **Credit**: who did it? (a fourth, added from the corpus) | Priority to whoever published first | Navier–Stokes priority dispute; blank author field on the Z-in-Q manuscript; a possible market in AI-written papers | **Partly.** Provenance records such as Palomar's metadata or Prove2Me's ownership help. Formalization does not settle who had the idea. |

**Slide line:** formalization can take over the referee's job of checking correctness, but not the editor's job of judging what matters.

---

## 1. Timeline of pressures and responses, 2025–2026

| Date | Event | Source |
|---|---|---|
| Oct 2025 | arXiv computer science stops accepting review and position papers unless they have already passed peer review | [TNW](https://thenextweb.com/news/arxiv-ai-slop-ban-researchers-preprint) |
| **Dec 10, 2025** | arXiv **math** tightens endorsement: automatic endorsement now needs an institutional email address **plus a prior math paper accepted on arXiv**. Rolled out site-wide on Jan 21, 2026. | [CASRAI](https://casrai.org/news/arxiv-2026-endorsement-english-ai-policy-changes) [secondary] |
| May 2026 | arXiv announces a **one-year ban** for submissions showing unchecked AI generation (invented references, leftover chatbot text). Announced by the CS chair, Thomas Dietterich. | [TechCrunch](https://techcrunch.com/2026/05/16/research-repository-arxiv-will-ban-authors-for-a-year-if-they-let-ai-do-all-the-work/); [THE: "welcome but unenforceable"](https://timeshighereducation.com/news/ban-authors-submitting-ai-content-welcome-unenforceable) |
| **Jun 2, 2026** | **Leiden Declaration** on AI and mathematics: 16 researchers, **endorsed by the IMU**. It asks for disclosure, human responsibility for correctness, results announced through peer-reviewed venues rather than press releases, and journals taking the lead on policy. It has **no enforcement mechanism.** | [IMA](https://ima.org.uk/?p=29314), [TNW](https://thenextweb.com/news/leiden-declaration-ai-mathematics-proof-attribution) |
| Jul 1, 2026 | arXiv becomes an independent nonprofit, separate from Cornell | [secondary] |
| Aug 2026 | *Philosophy & Public Affairs* publishes an article mostly written by AI as an experiment, then **bans** content "substantially written by AI" and adopts AI-detection software | [Daily Nous](https://dailynous.com/2026/08/24/after-experiment-journal-decides-to-prohibit-ai-authored-content/) |
| **Aug 18, 2026** | **Palomar** registry of Lean-verified mathematics opens (Lean FRO and ICARM) | [Tao](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/) |
| Sep 8, 2026 | OpenAI announces its Navier–Stokes result, followed by a priority dispute with Buckmaster and Alpöge | Note 01, §5 |
| Sep 11, 2026 | Fields Medalists' declaration, *"A Severe Misalignment of AI in Mathematics"*. Wikipedia says 28 signatories, other coverage says 25. | [Wikipedia](https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers) |
| Sep 21–29, 2026 | An independent advisory group of 9 mathematicians forms, hosted at IAS: Charles, De Lellis, Gowers, Hairer, Srivastava, Tillmann, Vakil, Witten, Wood. It advises OpenAI on releasing results but **has no decision-making power**. | [TechCrunch](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/), [OpenAI](https://openai.com/index/advisory-group-on-mathematics-and-ai/) |
| Sep 21, 2026 | Appelo and Kolda's breakdown of arXiv math submissions: August up **+79%** | [Substack](https://tammykolda.substack.com/p/a-breakdown-of-arxiv-submissions) |
| **Oct 1, 2026** | **arXiv rate limit: 2 new papers per submitter per month** (and at most 3 active), across all categories. Rejected papers still count. Described as temporary. | [404 Media](https://404media.co/arxiv-is-rate-limiting-submissions-because-it-cant-keep-up-with-ai-slop), [Cybernews](https://cybernews.com/ai-news/arxiv-limits-researchers-to-two-papers-a-month/) |
| **Oct 6, 2026** | **OpenAI posts 722 manuscripts in one day**, on GitHub, outside any journal or arXiv. 3 withdrawn within days, 14 repaired. | Note 01, §5 |
| Oct 2026 | UK Academy for the Mathematical Sciences report, *The mathematical sciences in an AI-enabled world* | [PDF](https://www.acadmathsci.org.uk/wp-content/uploads/2026/10/Mathematical_Sciences_AI_AcadMathsSci_Oct2026_preprint_final.docx.pdf) (the fetch was blocked; figures [secondary]) |
| Oct 17, 2026 | Shaoming Guo, in a guest post on Tao's blog, proposes a **new journal that requires Lean-verified proofs** | [Tao's blog](https://terrytao.wordpress.com/2026/10/17/starting-a-new-journal/) |
| **Oct 19 – Nov 8, 2026** | **Six probability journals pause new submissions together**: ESAIM: P&S, EJP, ECP, SPA, Bernoulli, AIHP. They cite a submission surge "driven largely by" AI and use the pause to review scope and AI policy. **They reopen today (Nov 9).** Retraction Watch called it the "Mathpocalypse / Slopwave." | [EDP Sciences](https://www.edpsciences.org/fr/actualites/3059-esaim-probability-and-statistics-takes-action-to-address-increasing-manuscript-submissions-2), [Retraction Watch](https://retractionwatch.com/2026/10/24/weekend-reads-journals-and-the-mathpocalypse-autism-paper-earns-eoc-cell-press-investigating-bribery-allegations/) |
| By end of 2026 | Springer will make AI statements **mandatory** for new submissions, as told to one editorial board | Corpus post 1341 (De Bie) |

---

## 2. The data

### arXiv mathematics volume
- **August 2026 against August 2025:** math with a primary listing rose from 3,522 by **+2,785, about +79%**. That is nearly twice arXiv's overall growth of +43% ([Appelo & Kolda](https://tammykolda.substack.com/p/a-breakdown-of-arxiv-submissions)).
  - **Combinatorics** saw an "unprecedented burst" and now outpaces optimization and control.
  - **Algebraic geometry, rings and algebras, complex variables and metric geometry** spiked in August.
  - **Analysis of PDEs** grew, but not explosively.
- **September 2026:** 7,428 math articles against 4,252 in September 2025, **about +75%**. This is from the AcadMathSci report (Reisinger et al., 28 Oct 2026, §1.2), now checked against the full text; see [note 06](06-acadmathsci-report-review.md). Early 2026 was only about 10% above early 2025, so the surge is recent. arXiv cited 40,363 submissions across all categories in September 2026, against 20,569 two years earlier.
- **January to August 2026** ([Nee, Zhong, Ni, arXiv 2609.04872](https://arxiv.org/abs/2609.04872v1)):
  - **47,127** math submissions, **+33.5%** year on year.
  - That is **+11.9% above a synthetic counterfactual** built from 20 other archives (robust range 9.6–14.9%). Math shows the strongest anomaly of all 15 comparison archives.
  - **29 of 30** math subcategories grew.
  - **Concentration at the top:** the share of authors with at least 10 submissions rose from **0.21% to 0.49%**, and with at least 5 from 2.45% to 3.80%. **A small group of very prolific authors drives much of the rise.** This is the group a per-person rate limit targets.

### Disclosure and compliance
- **De Bie** (corpus post 1341) checked 152 new arXiv papers in math.CA and math.RT. About **a third report using AI for the mathematics**, and **more than half have no AI statement at all**.
- **ICML 2026 randomized trial of LLM use in reviewing** ([Kim et al., arXiv 2609.19420](https://arxiv.org/abs/2609.19420v1)): over **24,000 papers and 17,000 reviewers**, randomly assigned a no-LLM policy or a limited-LLM policy.
  - The policy had **almost no effect** on decisions, scores or confidence. Reviews under the limited-LLM policy were 5.5–7% longer.
  - **22.5% of reviewers under the ban used an LLM anyway. 36.5% under the permissive policy used it in ways that policy did not allow.** Policies on AI use are largely ignored.
- A figure that **70% of journals have disclosure policies, yet only 76 of 75,000 papers disclose** comes from a single blog summary [secondary]. Don't quote it.

### AI use, disclosure and formalization on arXiv math (researched 2026-11-10)

Three independent measurements agree on the trend. None measures undisclosed use directly, and none counts formalization done without AI.

**1. Disclosed AI use (Epoch AI).** The [data insight of 18 Sep 2026](https://epoch.ai/data-insights/math-preprints-disclosed-ai-use) by Tara Abrishami covers every math preprint from Jan 2025.
- Share acknowledging AI for any purpose: 3.89% in April (158/4,058) and 25.25% in August (1,453/5,754). That is the "4% → 25%".
- 5.86% acknowledged a *substantial research* contribution in August.
- The rate holds within 1.5 points for papers with an author who published regularly before 2023.
- Method: keyword filter, then GPT-5.6 Sol classifies each acknowledgment and Claude Fable 5 validates it. Human agreement was 93% on 200 classifications.
- Epoch's own caveat: the series measures voluntary disclosure, so the trend mixes behaviour change with use.

Epoch's [dataset](https://epoch.ai/data/arxiv) (CC BY 4.0, updated 9 Nov 2026) extends the series through October. Values below are recomputed from its monthly CSV, field `math`, population `all`. The dataset revises August to 26.3%.

| Month (2026) | Papers | Any AI acknowledged | Substantial research | **Formalization** | Writing |
|---|---|---|---|---|---|
| Apr | 4,058 | 3.9% | 0.7% | 0.4% (16) | 2.5% |
| Jun | 4,770 | 8.4% | 1.9% | 0.6% (26) | 4.8% |
| Aug | 6,115 | 26.3% | 6.1% | 1.3% (80) | 17.0% |
| Sep | 8,138 | 38.5% | 9.0% | 1.8% (147) | 26.5% |
| **Oct** | 8,489 | **48.1%** | **9.7%** | **1.9% (160)** | 35.2% |

The categories overlap: one paper can acknowledge several uses. "Formalization" means AI acknowledged *for* formalization. It does not count formalization done without AI.

**2. Independent check (Jin, Ke & Sui, [arXiv 2608.24961](https://arxiv.org/abs/2608.24961), 25 Aug 2026).**
- 32,944 math submissions from 1 Mar to 20 Aug 2026. Explicitly disclosed use rose from 4.75% to 24.14%, and substantive use from 1.39% to 14.09%.
- Counts by type of use, non-exclusive: proof construction 1,225; **formalization and verification 427 (1.3% of all submissions)**; problem formulation 146; language and formatting 2,108; code and computation 1,229.
- Substantive use is highest in combinatorics (11.7%) and metric geometry (13.1%), and lowest in numerical analysis (1.9%) and PDE (2.2%).

**3. Undisclosed use (Kimball Martin, [AI use in arXiv mathematics papers](https://kimballmartin.github.io/ai-use/), page generated 3 Nov 2026, "a study directed by Kimball Martin using Claude").**
- Method: scores the LaTeX source of every math preprint with a 0–21 rubric of AI-writing markers. 5 or more counts as "apparent AI writing" and 10 or more as "heavy". The rubric itself is unpublished.
- Pre-LLM control (2016–2022): 122 of 23,600 papers flagged (0.5%), none heavy.
- Values below are recomputed from the data embedded in the page.

| Month | Papers | Disclose any AI use | Disclose AI writing | Apparent AI writing | **of which undisclosed** | Heavy | Heavy, undisclosed |
|---|---|---|---|---|---|---|---|
| Aug 2025 | 3,203 | 0.7% | 0.4% | 5.2% | 4.9% | 0.2% | 0.2% |
| Apr 2026 | 4,039 | 3.8% | 2.3% | 13.1% | 12.2% | 1.6% | 1.4% |
| Aug 2026 | 5,795 | 24.1% | 14.1% | 28.7% | 21.1% | 7.2% | 4.8% |
| Sep 2026 | 8,220 | 37.3% | 24.0% | 33.7% | 20.6% | 8.0% | 4.1% |
| Oct 2026 | 8,707 | 47.2% | 30.9% | 32.1% | **17.5%** | 6.5% | 3.4% |

- The detector flags only **50.5%** of papers that *do* disclose AI writing (3,358 of 6,643), and 13% as heavy. So the undisclosed count is probably an undercount. Martin says so himself, and attributes the October dip to "a change in how models write, not less AI writing".
- "Undisclosed" means the paper looks AI-written but does not disclose AI *writing*. It may still disclose other AI use.
- Other trackers: the [Potsdam tracker](https://arxiv-math-tracker-a5c153.gitlab.io/) counts declarations only ("Undeclared AI use is invisible here"). A detector study reported by a blog (unslop.run via singularity.kiwi, Jul 2026) found only 0.7% of math flagged. That is a small sample, a different detector, and unverified; don't use it.
- Aronow ([note, 4 Oct 2026](https://pmaronow.github.io/llm-disclosure.pdf)) argues that "a paper without an LLM disclosure is cause for suspicion", citing Martin.

**4. Formalization in arXiv math. No published count exists, so this is our own count.**
- Method: arXiv API, `cat:math.*` by submission month, abstracts mentioning Lean or Mathlib, checked with a strict regex. Script: `research/scripts/lean_count.py` (run with `.venv/bin/python research/scripts/lean_count.py <out dir>`).
- Result: about **0.05–0.1%** of math submissions in 2025 (2–6 a month), rising to **0.84% in Aug (59), 0.99% in Sep (91) and 0.94% in Oct 2026 (94 of 10,011)**.
- A cross-check without the category filter agrees: Jun 2025 gives 2 papers with a math category, and Oct 2026 gives 96.
- This is a lower bound: abstracts only, so it misses papers that link Lean code without mentioning it in the abstract. The denominator includes cross-lists, so it differs from Epoch's.
- Many October hits are "conjecture X is true/false" papers with machine-checked proofs.
- Lean Pool ([Ilin, arXiv 2609.25199](https://arxiv.org/abs/2609.25199), an AI-produced paper) has 211 formalization projects (102 AI, 70 human, 39 mixed). It forecasts that "most new mathematics papers will have accompanying formalizations", but measures nothing at arXiv scale.

**5. Machine learning and learning theory (researched 2026-11-10).** No ML equivalent of the Epoch or Martin series exists. The nearest evidence:
- **Theory-adjacent math subfields.** Recomputed from Epoch (Oct 2026, share of papers):

  | Subfield | Any AI acknowledged | Substantial | Formalization |
  |---|---|---|---|
  | math.ST (n=199) | 40.7% | 9.0% | 1.5% |
  | math.OC (n=661) | 31.9% | 4.2% | 2.3% |
  | math.PR (n=618) | 51.1% | 10.4% | 2.8% |
  | All math | 48.1% | 9.7% | 1.9% |

  Martin's data puts **apparent undisclosed AI writing higher in optimization** than in math overall: math.OC 28.6%, against 17.5% for all of math, in Oct 2026.
- **ICLR 2026.** Pangram ([blog, 18 Nov 2025](https://pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated)) analysed about 19,000 submissions and 70,000 reviews.
  - **21% of reviews (15,899) were fully AI-generated**, and over half showed some AI involvement.
  - **9% of submissions had more than 50% AI content**; 61% were mostly human.
  - [Self-reported]: Pangram sells the detector. Its claimed false-positive rate is 1 in 10,000, and 0% on pre-2022 ICLR/NeurIPS papers.
- **ICML 2026 reviewing trial** ([Kim et al., arXiv 2609.19420](https://arxiv.org/abs/2609.19420)): under a no-LLM policy, 22.5% of reviewers used an LLM anyway (see above).
- **Lean in ML abstracts (our count, same script).**
  - **stat.ML:** 0–2 papers a month in 2025, and **4 in Oct 2026 (0.4%)**. A few are learning-theory results with Lean proofs, for example "Depth Separation for Neural Networks under Gaussian Measure".
  - **cs.LG:** 0.1% in 2025, rising to **0.38% in Oct 2026 (26 papers)**. These are mostly papers *about* Lean-based theorem proving (provers, premise selection, benchmarks), not ML results certified in Lean.
  - **So formal certification of learning-theory results is still rare, a handful a month.** This bears on Q15 and supports framing the "In our field" slide as "it's starting, and there's room for us".

**What this means for the slide.** By October 2026:
- about **half** of arXiv math papers disclose AI use;
- about **1 in 10** disclose a substantial research contribution;
- about **1 in 6** look AI-written without saying so;
- only about **1 in 50** acknowledge AI for formalization;
- and about **1 in 100** mention Lean in the abstract.

Use is widespread; certification is rare. That makes the case for Part II.

### Refereeing capacity
- I found **no systematic count of referee declines.** The AcadMathSci report itself calls for collecting that data [secondary].
- What exists is anecdotal and consistent:
  - Editors cannot find a single referee (Weinreich, [arXiv 2608.02859](https://arxiv.org/html/2608.02859v1)).
  - Some referees refuse papers that look AI-generated, and some journals forbid that refusal (Craven, post 1133).
  - Craven: "The current journal system cannot absorb a 50% increase in the number of submissions."

---

## 3. What is breaking

1. **Volume against fixed refereeing capacity.** This is the problem behind the arXiv caps and the journal pauses. Referees must be established experts, so the supply cannot grow on demand.
2. **Releases that bypass every channel.** OpenAI's 722 papers went to GitHub, with no arXiv moderation and no journal. Moshkovitz called one "so horribly written that it's impossible to read it without AI help." The Leiden Declaration objects to exactly this: announcement by press release and blog before the community can evaluate.
3. **Priority stops measuring contribution.**
   - The Navier–Stokes dispute was over leaked work and prompts.
   - Corpus post 1439 (Moraschini): "a few dollars can buy you the solution to a famous conjecture."
   - Corpus post 1893 (anonymous postdoc): the rules are changing unfairly for junior researchers. "I no longer trust the profession to offer a fair and intelligible path forward."
4. **A new kind of paper mill** (corpus post 1043, Dolores-Cuenca). AI can produce *correct*, important-looking papers on demand, so authorship becomes something that can be sold. **Journals currently have no way to detect this.** Formalization does not help here: a correct certificate is exactly what the paper mill would supply.
5. **Retreat into secrecy, the "dark forest"** (corpus post 1491, Anderson). Frontier LLMs autonomously "solved" problems from an open-problem list in algebraic combinatorics. Mathematicians may stop sharing open problems and work in progress. The Navier–Stokes leak allegation feeds the same fear.
6. **Unreliable disclosure.** It is non-compliant (ICML) and missing (De Bie). Kretschmer (post 2379) predicts QIP 2027 "will be a disaster due to a lack of sufficient AI disclosure."
7. **The access gap.** Formal verification at the scale of these projects needs frontier models. One commenter on Guo's post estimated **$50–75k in hardware** to run a capable open model locally. This connects to Open Math Model's offer of free compute (note 02, E′).

---

## 4. Five kinds of response

| Strategy | Examples | Evidence on whether it works |
|---|---|---|
| **Restrict**: reduce inflow | arXiv endorsement rules, one-year bans, 2 papers a month; the six probability journals' pause; *P&PA*'s ban on AI-written content; Craven (post 1133) proposes banning AI-generated papers and rate-limiting authors; Weinreich proposes "AI vegan" identities and tenure weight for AI-free papers | A rate limit fits the author-tail data (0.21% → 0.49%). Bans depend on detection, and THE calls the arXiv ban "welcome but unenforceable." Pauses are temporary. |
| **Disclose**: make AI use visible | Leiden Declaration; Springer's mandatory statements; Kretschmer (2379) wants detailed disclosure **with penalties**; De Bie (1341); Kaipel's task taxonomy (2451); Palomar's `formalization.yaml` disclosures | ICML shows disclosure policies are widely ignored. A taxonomy like Kaipel's makes disclosure specific and checkable. |
| **Verify**: make correctness cheap | **Palomar**; **Guo's journal requiring Lean**; Valentini (post 670) predicts journals will require "a Lean certificate"; **Lewin (post 3130)** proposes **"AI proof reports"** as raw data in a community repository, with arXiv and journals kept for human papers that draw out insight; Idrissi (1097) separates the *announcement plus certificate* from a later *explanatory paper*; ProofForum's signed referee verdicts | Covered in §5. |
| **Expand**: grow capacity | **Maltsev (post 3321)** proposes flagship journals with "daughter" journals plus **paid, AI-assisted refereeing**; Google's PAT for pre-submission checks | The most optimistic position in the corpus (institutions score +0.6). It depends on funding and on AI review being trustworthy (§6). |
| **Replace**: change the unit of credit | **Ng (post 3154)** would abolish journals in favour of public defences of preprints at thesis level; **Morris (2840)** says write fewer papers and invest in atlases, curation and exposition; **Harlev (757)** says reward exposition and refinement now, without waiting for consensus; Qi Guo (328) would subtract what AI could reproduce from human credit; Moraschini (1439) would base hiring on explanation and interviews | Mostly proposals. ProofForum and Palomar are early working examples. |

**The pattern:** the responses that actually exist (arXiv caps, journal pauses, Springer statements) restrict and disclose. The structural proposals (verify, expand, replace) are still mostly blog posts and prototypes.

---

## 5. How formalization can help, and where it can't

### What it can take over
- **Line-by-line correctness checking (L1).** Under Palomar's model, **Comparator** confirms the proof proves exactly the challenge statement, and an LLM checks that statement against the informal description ([Tao](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/)). Refereeing for correctness becomes **reviewing the statement**: a page of Lean definitions and theorem statements instead of 60 pages of proof.
- **Decoupled roles.** Tao expects formal proofs to be registered *before* a polished preprint, with a **planned overlay journal** that peer-reviews Palomar repositories. That is the arXiv-plus-overlay model, applied to certificates.
- **Triage.** A journal can require a certificate for the mechanical parts, as Lee and Valentini suggest. Referees then focus on the idea, which shrinks the refereeing task rather than the number of submissions.
- **Separating raw output from papers.** Lewin's "AI proof reports" and Idrissi's announcement/explanation split both give machine output a place to go that is *not* the journal. The journal then becomes the place where **insight** is published.

### What it can't do (with evidence from notes 01–02)
1. **Statement fidelity remains a human job.** Examples: the Navier–Stokes code needs m+5 derivatives where the paper has m+4; OpenAI listed 21 "(Lean)" results with no formalization; the OEIS "disproof" for $0.17. **Palomar's own documentation says the LLM semantic check can miss things.**
2. **Significance, novelty and attribution are not formal properties.** A paper mill can supply a valid certificate (§3.4).
3. **Coverage is uneven.** Mathlib is strong in algebra, number theory and parts of analysis, and weak in PDE and applied areas. That is why the Navier–Stokes code drifted. **Probability**, the field whose journals paused, now has StatsMLlib (about 65k lines, note 02 H), but research-level probability goes far beyond it. **Requiring Lean today would disadvantage fields like PDE and applied probability, where the libraries are thin.**
4. **The kernel is an attack surface.** The Collatz kernel exploit (note 02 F) means a journal that relies on Lean needs a policy on kernel versions and on re-checking certificates when a soundness bug is found.
5. **Access.** Lean certificates require frontier models or expert humans (the $50–75k hardware comment; Guo's reply that a third party will help formalize at first). Without public infrastructure such as Open Math Model, a Lean requirement favours well-funded groups.
6. **A Lean monoculture.** Commenters on Guo's post warn that relying on one proof assistant concentrates risk. Paulson's LCF argument (note 02) is the technical version of that warning.

**Slide line:** formalization makes the referee's correctness check cheap, which leaves editors with judgment, readers with understanding, and the community with credit. Those are the parts no certificate covers.

---

## 6. Automated AI review: where it stands

| System | What it does | Evidence | Caveat |
|---|---|---|---|
| **Google Paper Assistant Tool** ([arXiv 2606.28277](https://arxiv.org/abs/2606.28277); [blog](https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/)) | An agent based on Gemini gives authors feedback before submission. Used at **STOC 2026** and ICML. | 97% of surveyed authors found it helpful; about 90% of planted errors caught | **The benchmark has 26 papers and 29 errors**, and the numbers come from Google itself |
| **AAAI 2026** | Adds **one LLM-written review** alongside two human reviews for each paper | | [secondary] |
| **ICML 2026 trial** ([2609.19420](https://arxiv.org/abs/2609.19420v1)) | Randomized comparison of review policies | Almost no effect on outcomes; widespread non-compliance | Shows that rules on reviewers' AI use don't change much and aren't followed |
| **OpenAIReview** (UChicago CHAI) | Open-source review assistant | Still working on how to verify claims | |
| **Palomar's semantic check** | An LLM compares the informal description with the formal statement | It is the only AI review step built into a verification pipeline | Not deterministic; can miss discrepancies (Tao) |
| **AI review in the Z-in-Q case** (note 01, §4) | Several rounds of review by a "Claude research system" found 9 issues and then a gap in one of the repairs | Productive: it caught a real gap at p = 2 | **AI checking AI.** The repo itself says this is not peer review. |
| **The arms race** ([arXiv 2609.07713](https://arxiv.org/pdf/2609.07713)) | Authors learn to write for AI reviewers | | Critics' worry: authors will optimize for the review agent and debate will narrow |

**Assessment for the talk:**
- AI review is already standard **before submission** and as **an extra reviewer**.
- It is **not trusted as the deciding reviewer** anywhere I found.
- The best-supported role is the one Palomar gives it: a **narrow, specific check of whether the statement matches the claim**, inside a pipeline whose correctness check is mechanical. Open-ended "is this paper good?" is not that role.
- Maltsev's "AI-assisted, paid human refereeing" is the most plausible near-term design.

---

## 7. The software parallel

| AI-generated code | AI-generated mathematics |
|---|---|
| Continuous integration and tests | Lean kernel and Comparator |
| Test specification written by a human | Challenge file / mission core written by a human (Prove2Me, Palomar) |
| Tests pass but the specification is wrong | Proof compiles but the statement is misformalized (Navier–Stokes, OEIS) |
| Code review | Statement review; human sign-off on definitions (Lean Atlas) |
| API rate limits against spam | arXiv's 2 papers a month |
| Software bill of materials and provenance | `formalization.yaml` disclosures; Prove2Me ownership records |
| Supply-chain attack | Collatz kernel exploit; Axiom's unreleased build-tool changes |
| Open-source maintainers swamped by AI pull requests | De Jong asking that AI output be kept out of the Stacks Project; the probability journals' pause |

The table points to one conclusion. Software kept trust in AI-written code by moving human effort from *writing* to *specifying and reviewing*. Mathematics is facing the same shift, from *proving* to *stating, selecting and explaining*.

---

## 8. Mapping to `questions_of_interest.md`

| Question | Short answer | Section |
|---|---|---|
| Recent problems in publishing and their link to AI | Submissions up 33–79% while refereeing capacity is fixed; releases that bypass journals; the collapse of priority as a measure; paper mills; secrecy; ignored disclosure rules | §§1–3 |
| How formalization can help | Takes over the correctness check and moves refereeing to statement review. Doesn't cover significance, credit or fidelity. Uneven coverage across fields, an exposed kernel, and unequal access. | §5 |
| Role of automated AI review | Already used before submission and as an extra reviewer, nowhere the deciding one. Best fit: a narrow statement-matching check. | §6 |
| Parallel with AI-generated code | Move human effort to specification and review | §7 |
| Applied math versus pure math (partial) | Applied probability is at the centre (the journal pause). PDE has thin formal coverage. Harlev (757, Cornell applied math) and Maltsev (3321, applied probability) are among the most pro-reform voices. | §§2, 5 |
| Human understanding as a publication criterion | Lewin, Idrissi and Guo's journal all make **understanding the purpose of a journal** and push certificates elsewhere | §§4–5 |

---

## 9. Corpus voices on publishing (`data/dataset.jsonl`)

**Overall:** across the 121 posts that take a position, the `institutions` score (confidence that institutions will adapt) has mean **−0.03** and median +0.10. **47% are negative.** The corpus is split close to evenly on whether journals will adapt.

| id | Author | Post | institutions score | Position |
|---|---|---|---|---|
| 1133 | David Craven (Birmingham) | [Where will all the papers go?](https://proofsandprompts.com/2026/09/19/where-will-all-the-papers-go/) | −0.5 | Ban AI papers, rate-limit authors, pre-screen with LLMs |
| 2379 | William Kretschmer (UT Austin) | [On AI Disclosures](https://proofsandprompts.com/2026/10/27/on-ai-disclosures/) | −0.3 | Required detailed disclosure, with penalties |
| 3130 | Mathieu Lewin (CNRS / Dauphine) | [Please STOP writing papers!](https://proofsandprompts.com/2026/11/02/please-stop-writing-papers-there-is-another-way/) | −0.2 | "AI proof reports" as raw data, in a separate repository |
| 3321 | Anna Maltsev (QMUL, applied probability) | [In Defence of Incremental Mathematics](https://proofsandprompts.com/2026/11/04/in-defence-of-incremental-mathematics/) | **+0.6** | Daughter journals; paid, AI-assisted refereeing |
| 3154 | Andrew Ng (Bonn PhD student) | [A new system of accreditation](https://proofsandprompts.com/2026/11/01/a-new-system-of-accreditation/) | +0.3 | Abolish journals; public defences |
| 1893 | Anonymous PDE postdoc | [The Rules Cannot Change Only for Young Mathematicians](https://proofsandprompts.com/2026/10/22/the-rules-cannot-change-only-for-young-mathematicians-ai-and-the-future-of-a-mathematical-career/) | −0.5 | Unfairness to junior researchers; the Navier–Stokes credit dispute |
| 1491 | Dave Anderson (Ohio State) | [Mathematics in the Dark Forest](https://proofsandprompts.com/2026/10/18/mathematics-in-the-dark-forest/) | +0.1 | The risk of secrecy; publish prompts |
| 1043 | Eric Dolores-Cuenca (Yonsei) | [A new type of paper mill](https://proofsandprompts.com/2026/10/01/a-new-type-of-paper-mill/) | −0.5 | Correct papers for sale, undetectable |
| 1341 | Hendrik De Bie (Ghent) | [On AI statements in mathematics papers](https://proofsandprompts.com/2026/10/16/on-ai-statements-in-mathematics-papers/) | +0.4 | Survey of 152 papers; Springer making statements mandatory |
| 670 | Lisa Valentini (Cambridge PhD student) | [When inventing is not enough](https://proofsandprompts.com/2026/09/15/when-inventing-is-not-enough/) | +0.4 | A CERN-style model; Lean certificates will become required |
| 757 | Amit Harlev (Cornell applied math PhD student) | [Dear conferences, journals, and hiring committees](https://proofsandprompts.com/2026/09/25/dear-conferences-journals-and-hiring-committees-dont-wait-for-everyone-else/) | +0.2 | Reward exposition now |
| 328 | Qi Guo (Renmin) | [Evaluating mathematical merit](https://proofsandprompts.com/2026/08/27/the-future-mathematical-system-ai-tools-human-contribution-and-mathematical-evaluation/) | +0.5 | Subtract what AI could reproduce from credit |
| 2840 | Patrick Morris (UPC) | [Let's stop writing papers…](https://proofsandprompts.com/2026/10/30/lets-stop-writing-papers/) | +0.1 | Atlases, curation, exposition |
| 1097 | Najib Idrissi (Paris Cité) | [YAPOAI](https://proofsandprompts.com/2026/10/03/yapoai-yet-another-post-on-ai-ai-understanding-and-mathematical-work/) | +0.1 | Announcement plus certificate first, explanation later |
| 1439 | Tommaso Moraschini (Barcelona) | [Contribution, Credit, and Community](https://proofsandprompts.com/2026/10/19/contribution-credit-and-community/) | −0.1 | Priority can no longer ground credit |

**For a slide:** plot `institutions` against `adoption` for these 15 posts, using `cluster.py` and the existing dataset. The proposals to "replace" and "expand" will likely fall in the optimistic, pro-adoption quadrant, and the "restrict" proposals in the pessimistic one.

---

## 10. Still to verify
- [x] Figures from the AcadMathSci report (September 7,428 against 4,252; arXiv capping; journal suspensions). All three are confirmed in the full report, pre-publication draft of 28 Oct 2026; see [note 06](06-acadmathsci-report-review.md) §1. The report does not name the six journals that paused on 19 Oct, and calls the journal-side evidence "largely anecdotal".
- [ ] What the six probability journals changed when they reopened today, Nov 9.
- [ ] Whether the Annals of Probability or PTRF took similar action. Nothing found.
- [ ] arXiv's own blog post, "Fair Moderation, Equitable Access, and AI: arXiv's Updated Rate Limit Policy" (Oct 1).
- [ ] The name, editors and launch date of Guo's journal.
- [ ] Recommendations from the IAS advisory group: none were published as of the coverage I found.
- [ ] The number of Fields Medalist signatories (25 or 28) and the full text of the declaration.
- [ ] Whether the Leiden Declaration really passed 3,000 signatories (one unverified source).

## Sources
- Nee, Zhong, Ni, *The Generative AI Gold Rush in Theoretical and Computational Research*: https://arxiv.org/abs/2609.04872v1
- Appelo & Kolda, arXiv breakdown: https://tammykolda.substack.com/p/a-breakdown-of-arxiv-submissions
- AcadMathSci report: https://www.acadmathsci.org.uk/wp-content/uploads/2026/10/Mathematical_Sciences_AI_AcadMathsSci_Oct2026_preprint_final.docx.pdf
- Weinreich, *The crisis of AI-generated mathematics*: https://arxiv.org/html/2608.02859v1
- Probability journals' pause: https://www.edpsciences.org/fr/actualites/3059-esaim-probability-and-statistics-takes-action-to-address-increasing-manuscript-submissions-2 · https://retractionwatch.com/2026/10/24/weekend-reads-journals-and-the-mathpocalypse-autism-paper-earns-eoc-cell-press-investigating-bribery-allegations/
- arXiv policies: https://casrai.org/news/arxiv-2026-endorsement-english-ai-policy-changes · https://techcrunch.com/2026/05/16/research-repository-arxiv-will-ban-authors-for-a-year-if-they-let-ai-do-all-the-work/ · https://404media.co/arxiv-is-rate-limiting-submissions-because-it-cant-keep-up-with-ai-slop · https://cybernews.com/ai-news/arxiv-limits-researchers-to-two-papers-a-month/ · https://timeshighereducation.com/news/ban-authors-submitting-ai-content-welcome-unenforceable
- Leiden Declaration: https://ima.org.uk/?p=29314 · https://thenextweb.com/news/leiden-declaration-ai-mathematics-proof-attribution
- IAS / OpenAI advisory group: https://openai.com/index/advisory-group-on-mathematics-and-ai/ · https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/
- *Philosophy & Public Affairs* policy: https://dailynous.com/2026/08/24/after-experiment-journal-decides-to-prohibit-ai-authored-content/
- Palomar: https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/
- Guo's journal proposal: https://terrytao.wordpress.com/2026/10/17/starting-a-new-journal/
- ICML 2026 trial: https://arxiv.org/abs/2609.19420v1
- Google PAT: https://arxiv.org/abs/2606.28277 · https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/
- The review arms race: https://arxiv.org/pdf/2609.07713
- OpenAIReview: https://datascience.uchicago.edu/insights/openaireview/
