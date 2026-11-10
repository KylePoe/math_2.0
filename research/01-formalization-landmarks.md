# Formalization landmarks: what got verified, and what "verified" means

*Research notes for the "Math 2.0" talk. Compiled 2026-11-09.*

**Reliability key.** **[self-reported]** means the only source is the organization that did the work. **[independent]** means someone outside checked it. **[unverified]** means the claim is still open. Many 2026 figures, such as line counts and day counts, come only from company announcements and differ across press coverage. Where sources disagree, that is noted.

---

## 0. The frame: three layers of "verified"

The most useful idea for the talk comes from the post-mortem of OpenAI's Navier–Stokes formalization ([redreamality](https://redreamality.com/blog/ai-math-verification-lean-faithfulness/), built on [Bastounis–Circelli–Hansen](https://arxiv.org/html/2610.08144v1)). It separates three things:

| Layer | Question | Who or what checks it |
|---|---|---|
| **L1: kernel** | Does the Lean code compile, with no `sorry` and only the standard axioms? | Machine: cheap, and a solved problem |
| **L2: statement fidelity** | Does the formal statement say what the theorem says? | Humans, with AI help. Tools: Lean FRO's Comparator, TauCeti's adversarial reviewers |
| **L3: proof fidelity** | Does the formal proof follow the paper's argument? | Almost no one checks this |

Proofs are now plentiful at L1. L2 and L3, which hold the insight, are scarce. Every case below fits somewhere on this table.

Seewoo Lee states the L3 worry in the Proofs & Prompts corpus (post 848, "(auto)formalization, but why", EPFL). The worst case, in Lee's words, is that the original proof is wrong and the LLM "is able to fix it quietly without telling you." Lee's advice is to read the code.

---

## 1. Timeline at a glance

### Human-led era (baseline)

*Verified against primary sources on 2026-11-10 for slide 4. Each row below is cited in `talk/sections/01-opener-paradigm.tex`.*

| Date | Event | Primary source |
|---|---|---|
| 1 Mar 1977 | Landau's *Grundlagen der Analysis* checked in Automath. Jutting's PhD thesis, TH Eindhoven, supervised by de Bruijn | [CWI record](https://ir.cwi.nl/pub/32108) |
| 1976 | Appel–Haken prove the four colour theorem using a computer case analysis that "could not, in any real sense, be performed by hand" | Gonthier, *A computer-checked proof of the Four Colour Theorem*, MSR report, 2005, §1 |
| 2005 | The four colour theorem is "fully checked by the Coq v7.3.1 proof assistant". Gonthier notes that Robertson et al.'s 1995 proof had already "cleared up most doubts" | Same report ([copy](https://www.cl.cam.ac.uk/~lp15/Pages/4colproof.pdf)) |
| 4 Sep 1998 → 16 Aug 2005 | Hales, *A proof of the Kepler conjecture*, Ann. Math. 162 (2005): received, then accepted | [Annals](https://annals.math.princeton.edu/2005/162-3/p01) |
| Jan 2003 → 10 Aug 2014 | Flyspeck announced, then completed. The Kepler proof "was published without complete certification from the referees" | [arXiv 1501.02155](https://arxiv.org/abs/1501.02155) · [repo](https://github.com/flyspeck/flyspeck) |
| 2012 | Feit–Thompson in Coq, a "six-year collaborative effort" (ITP 2013). The day (20 Sep 2012) is confirmed only by secondary sources | [MSR](https://www.microsoft.com/en-us/research/?p=720412) |
| Summer 2017 | Mathlib begins, factored out of the Lean 3 core library | The mathlib Community, CPP 2020, §1.1 ([arXiv 1910.09336](https://arxiv.org/abs/1910.09336)) |
| 5 Dec 2020 → 14 Jul 2022 | Scholze's challenge ("being 99.9% sure is not enough") → LTE completed, led by Commelin | [Xena blog](https://xenaproject.wordpress.com/2020/12/05/liquid-tensor-experiment/) · [Lean blog](https://leanprover-community.github.io/blog/posts/lte-final) |
| 9 Nov → 5 Dec 2023 | PFR preprint → formalization's "primary goals" completed | [arXiv 2311.05762](https://arxiv.org/abs/2311.05762) · [Tao's blog comment](https://terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/) |

Not verified from a primary source, so not used on slides: the referees' "99% certain" (only through Nature 2003, paywalled); Automath's start in 1968; Mizar's start in 1973; PFR in "3 weeks".

| Year | Project | System | Why it matters |
|---|---|---|---|
| 2005 | Four Colour Theorem (Gonthier, Werner) | Coq | Removed doubt about a computer-assisted proof |
| 2012 | Feit–Thompson Odd Order Theorem (Gonthier et al.) | Coq | The first large piece of CFSG to be formalized; took about 6 years |
| 2014 | Kepler conjecture, Flyspeck (Hales et al.) | HOL Light + Isabelle | Referees were only "99% certain"; formalization settled it after about 10 years |
| 2020–22 | Liquid Tensor Experiment (Scholze's challenge, led by Commelin) | Lean 3 | Formalization used to *check* a proof the author doubted; 19 months |
| 2023 | Polynomial Freiman–Ruzsa (Gowers–Green–Manners–Tao) | Lean 4 | Took about 3 weeks; the constant was later improved "for free" because the proof was formal |
| 2024 | Equational Theories Project (Tao) | Lean 4 | Crowdsourced proofs of about 22M implications between magma laws, with automated provers |
| 2024– | Fermat's Last Theorem (Buzzard, 5-year EPSRC grant) | Lean 4 | The flagship human project; FLT for regular primes was done separately in 2024 |
| 2025 | Carleson's theorem (van Doorn et al.) | Lean 4 | A large hard-analysis formalization led by humans |

### AI-led era (2025–2026)
| Date | Project | Who | Scale (as claimed) | Status |
|---|---|---|---|---|
| 2025 | Strong Prime Number Theorem | Math, Inc. (Gauss) | About 25k lines in 3 weeks, against 18 months for the human-led Tao–Kontorovich effort | [self-reported] [project page](https://math-inc.github.io/strongpnt/) |
| Feb–Mar 2026 | Sphere packing in dimensions 8 and 24 (Viazovska) | Math, Inc. (Gauss) | First proof about 450k lines, final about 200k. Built on a human blueprint | [self-reported] Partly documented in [arXiv 2604.23468](https://arxiv.org/pdf/2604.23468) |
| Aug 2026 | Hamilton's theorem on 3-manifolds of positive Ricci curvature | Chow, Liao, Qin | Includes the Ricci-flow infrastructure | [arXiv 2608.21502](https://arxiv.org/pdf/2608.21502) |
| Sep 4, 2026 | **Fermat's Last Theorem, end to end** | Anthropic (Claude agents) | About 13M lines, 11 days, about 6B output tokens | [self-reported] [Anthropic](https://anthropic.com/research/formalizing-fermats-last-theorem). A comparator check matched the statement to Mathlib's FLT |
| Sep–Oct 2026 | Poincaré conjecture (Hamilton–Perelman proof); geometrization in [arXiv 2610.13897](https://papers.cool/arxiv/2610.13897) | Qin, Liao, Chow, Khaitan | Press claims "4.7M lines" | [unverified] Semantic review still pending ([tracker](https://kingy.ai/mathematics-science-breakthrough-tracker/records/math-poincare-lean-formalization-2026/)) |
| Oct 6, 2026 | OpenAI's bulk release: 722 manuscripts | OpenAI | About 42% have Lean proofs (300/719) | Mixed. See §5 |
| Oct 26–27, 2026 | **Classification of Finite Simple Groups** | Axiom | About 43.1M lines, 24 days | [self-reported] Independent build not yet reproduced. See §2 |
| Nov 4, 2026 | **The Stacks Project** | Axiom | About 16M lines covering about 7,500 pages | [self-reported] See §3 |
| Nov 5–8, 2026 | **"Z is Diophantine in Q"** | Glazer et al. with several AI models | Main Lean declaration still contains `sorry` | [unverified] See §4 |

In the scale column, Mathlib itself is roughly 2M lines. The FLT formalization claims more than 5 times that.

---

## 2. Case study: the Classification of Finite Simple Groups (Axiom, Oct 2026)

**The claim.** Axiom calls this the "first complete computer-checked proof" of CFSG ([Axiom](https://axiommath.ai/research/the-enormous-theorem-formalized/)).
- About 43.1M lines of Lean and 2.05M declarations, drawn from 715 papers and books ([Latenode](https://latenode.com/news/axiom-completes-lean-checked-cfsg-proof-finds-34-deviations)). It includes about 1.2M lines from the earlier Qiuzhen-CFSG project.
- Done in 24 days by AI agent swarms. The proof map had 108 milestones and about 380 tasks, coordinated through GitHub issues and Slack.
- It follows the **first-generation** proof, not the unfinished second-generation proof.
- Axiom says it has no `sorry`, uses only the standard axioms, and avoids `native_decide`. It builds on Mathlib and TauCeti, with Lean v4.35.0-rc3.
- Richard Lyons and Ronald Solomon advised on the arguments and on the repair to the Unbalanced Group Theorem (UGT).

**Benefits shown.** This was not just transcription. Formalizing the proof found problems in the published literature:
- Axiom lists **34 noteworthy deviations** from the published record. Most are typos, table errors, and dropped hypotheses.
- **A quasithin lemma (Aschbacher–Smith):** an equality in the published proof is false. The agents found a counterexample in SL₂(5), where one side is 1 and the other is 2. The repair replaces the equality with an inequality and reworks the later case analysis.
- **The UGT (Walter 1986):** a published closure assertion has no justification. In the PSL₂(49) counterexample, a centralizer's component is PSL₂(7), which the family excludes because 7 is a Mersenne prime. Axiom built a **new route to the UGT** and a new preservation theorem, published in a companion paper.
- None of this refutes CFSG. A community note describes the errata as affecting supporting statements and proof steps, not the classification itself.

**Pitfalls and open questions.**
- **No independent L1 check yet.** An audit fork ([enuminous/CFSG](https://github.com/enuminous/CFSG), Oct 27) passed 10 static checks but rates the result only "QUALIFIED." The "no `sorry`" and "standard axioms only" claims still need an independent `lake build` and `#print axioms` run. The build also depends on **local Lake modifications that have not been upstreamed**. Coverage advises treating this as a "credible, extraordinary claim" until it is reproduced ([i10x](https://i10x.ai/news/axiom-cfsg-lean-formalization-finite-simple-groups)).
- **L2 rests on another AI-built library.** The top-level statement comes from TauCeti, which is itself written by AI and reviewed by AI against human roadmaps ([Lean FRO](https://lean-lang.org/use-cases/tau-ceti)). The statement is a single existential over an index type, `CFSGIndex`, so whether the 26 sporadic groups and 16 Lie-type families are encoded correctly depends on definitions that humans need to read.
- **Axiom's own admissions.** Early plans rested on prerequisites nobody had proved. Tens of thousands of lines were deleted and restarted. Only one milestone had closed by day 12. Axiom also writes that "Lean can verify results under additional assumptions, so progress can be overstated." Constructing a group, proving it is simple, and recognizing it are three separate tasks, and the Monster is the hard example.
- **Who can read 43M lines?** Corpus post 830 (Nesterov, Stanford) recalls that some mathematicians rejected CFSG because no single person understood all of it. A formal proof 20 times the size of Mathlib answers "is it true?" but makes "does anyone understand it?" worse.

**Slide line:** formalization found real errors in a 10,000-page proof that experts had checked for 40 years. The repairs, though, were written by agents and checked by two human experts.

---

## 3. Case study: the Stacks Project (Axiom, Nov 4, 2026)

**The claim.** Axiom says it formalized the entire Stacks Project, the open-source algebraic geometry reference of roughly 7,500 pages, in about 16M lines of Lean on top of Mathlib ([Axiom](https://axiommath.ai/research/the-stacks-project-formalized/)). It calls this the largest integrated formal library so far.
- Every Lean declaration links back to its permanent Stacks tag. The original text can be read beside the Lean at stacks.axiommath.ai, with an interactive dependency graph.
- For L2, Axiom used multi-agent auditing, semantic cross-checks against the source text, and a requirement that each definition work with the theorems that depend on it. It ran targeted audits on foundational definitions and landmark theorems.

**Benefits.**
- **Traceable formalization.** The tag-to-declaration mapping is the best answer to L2 in any of these projects, because a human can check one tag at a time.
- **Errors found.** Axiom reports dozens of statements that needed local refinement: missing hypotheses, edge cases in positive characteristic, and claims that fail in the stated generality. The agents built counterexamples. Where a false lemma left a gap, they found another route in the literature to the main result under its original hypotheses.
- **It contrasts with 2024.** The Herald dataset ([arXiv 2410.10878](https://arxiv.org/pdf/2410.10878)) autoformalized only one Stacks section, Normal Extensions, as a demonstration.

**Pitfalls and governance tension.**
- **The maintainer did not ask for this.** On Oct 21, 2026, according to Axiom, Johan de Jong asked that AI-generated comments and pull requests not be sent to the upstream Stacks repository "for now." Axiom keeps its corrections in its own fork. That creates **a canonical human text and a separate, corrected formal copy owned by a company.** I could not find de Jong's announcement itself; confirm it on the Stacks site before quoting.
- Axiom's post does not state the axioms, the `sorry` status, the number of tags formalized, or how long the work took. It has no caveats section.
- Corpus post 1862 (Lerario, SISSA) names the Stacks Project as a model for a "branching, enriched and layered hypergraph" of mathematical knowledge. The open question is who maintains that layer.

**Slide line:** the formal copy of the Stacks Project corrects the original, but the original's maintainer has asked to keep AI output out. Which version is canonical?

---

## 4. Case study: "Z is Diophantine in Q" (Nov 2026). The problematic case

**Background.** If Z has a Diophantine definition in Q, Hilbert's Tenth Problem over Q is undecidable. This was a central open question. Koenigsmann (2016) showed that **Q∖Z** is Diophantine, which is the easier direction. Mazur's conjectures on the topology of rational points were widely believed to imply that **Z is not** Diophantine in Q.

**What happened.**
1. **Oct 6:** OpenAI's bulk release included a 62-page preprint, *Hilbert's tenth problem over the rational numbers* (file dated Sep 24), claiming H10 over Q is **undecidable**. It came with **no Lean formalization** and has not been independently verified ([Emergent Mind entry 004](https://www.emergentmind.com/openai-math-explorer/results/004)).
2. **Oct 11:** Sohail Farhangi, working with ChatGPT, posted a manuscript that is conditional on four arithmetic inputs from OpenAI.
3. **Nov 4–5:** Elliot Glazer, working with several AI models (the README names Astra, Sol, and Opus, with auditing by Fable), claimed an explicit polynomial defining Z in Q. The [first announcement](https://x.com/ElliotGlazer/status/2118403066198376903) had about **292.9 billion variables**, degree below 2↑↑7, and coefficients below 2↑↑8. As a consequence, it claims **Mazur's conjecture is false**.
4. **A race to shrink the polynomial.** A public leaderboard (bigospeedrun.com) drove reductions: 12,504 variables in V2, 962 in V6, 498 in V12, and **394 in V13 (Nov 7)**. V13 gives degree-4 polynomials in 394 variables with symbolic coefficients, or 411 with decimal coefficients ([repo](https://github.com/elliotglazer/diophantine-z-q)).
5. **Nov 6–8: review by AI.** Manvir Jaswal reviewed the manuscript "with a Claude research system" ([issue #2](https://github.com/elliotglazer/diophantine-z-q/issues/2)) and found **9 issues**:
   - missing credit to Mazur's 1992 paper
   - an ambiguity in Prop. 8.9
   - a Turing-degree corollary already in OpenAI's preprint
   - a gap at p = 2: Perrin-Riou's result assumes p is odd
   - an unwritten valuation step
   The fix to the p = 2 gap had its own gap, which was caught on recheck and repaired in V11. None of the issues changed the polynomial.
6. A separate AI-authored audit by another group ([darkhipo/z-diophantine-research](https://github.com/darkhipo/z-diophantine-research)) maps the **conditional steps** in one branch of the proof. These include an implication internal to the manuscript and an "ultrafilter stage-limit framework" that is uncited and unpublished. The audit also checks an 11-variable construction for Q∖Z by machine.

**Why it belongs in the talk.**
- **L1 is not met, though it looks as if it is.** The repo has 48 Lean helper modules and 463 declarations, but **the main bounded-polynomial declaration still contains `sorry`**. The finite checks verify coordinate changes, eliminations, and coefficient statistics. They **do not** verify the arithmetic characterization of Z. The repo says this itself: "AI review and successful finite checks do not constitute independent human peer review or a completed formal proof."
- **The verification is mostly AI checking AI.** It took 13 versions in 3 days, with AI reviews, AI repairs, and AI rechecks, plus a few human reviewers.
- **Credit is unclear.** Ideas are attributed to Pheidas for the rank-one elliptic curve strategy, to Zhi-Wei Sun for the prime patterns, to OpenAI's preprint, and to a group of about 8 named humans. The manuscript's author field is blank.
- **The norms have not caught up.** Glazer asked critics publicly: "what do you think I should have done differently?" ([X](https://x.com/ElliotGlazer/status/2118815518916579530)). Nobody has an agreed answer.
- **A milestone that was gamified.** The headline progress was a falling variable count on a leaderboard, not understanding why the result is true.
- **No expert verdict yet.** I found no public assessment from Poonen, Koenigsmann, or Shlapentokh. Watch for one.

**Slide line:** a decades-old question may have been answered in a week. It refutes a well-known conjecture, has an explicit 394-variable witness, and has no completed formal proof. It is the clearest example of abundant proof without established insight.

---

## 5. Supporting case: OpenAI's release and "lost in translation" (Sep–Oct 2026)

This is the strongest evidence that **L1 does not imply L2 or L3**.

- **The Navier–Stokes claim (Sep 8)** came with Lean code. [Bastounis, Circelli, and Hansen (arXiv 2610.08144)](https://arxiv.org/html/2610.08144v1) compared the code with the paper:
  - The paper's eq. (8.19) needs m+4 derivatives. The matching Lean theorem `norm_derivativeWord_inverse_le` **assumes m+5** and uses a different series exponent, and the m+5 pattern repeats elsewhere.
  - The paper's pressure-flux bound (10.19) depends only on B_R. The Lean bound **also depends on A_R** and proves it by a different route (Sobolev embedding into L² instead of Riesz transforms in L^{3/2}).
  - Their conclusion: "Lean acceptance (compilation) of translation does not imply semantic preservation." They also argue that faithfulness is not decidable in general. They do **not** claim the paper is wrong.
- **The bulk release (Oct 6):** 722 manuscripts covering about 372 problems ([Wikipedia](https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers)).
  - Within days, **3 were withdrawn** because of a sign error in a result on Weil classes and two papers that depended on it. All three were **outside** Lean coverage.
  - **14 proofs or statements were repaired** ([redreamality](https://redreamality.com/blog/ai-math-verification-lean-faithfulness/)).
- **A community audit** of all 245 formalized families ([borism/openai-math-slop #2](https://github.com/borism/openai-math-slop/issues/2)) found:
  - about 210 consistent at the level of statements
  - 5 that prove only a supporting lemma but are listed as main results
  - about 4 weaker or partial
  - **21 headline results with "(Lean)" links that are not actually formalized**
  - 2 that rest on very large custom definitions, including about 52k lines of definitions for the CM Hodge result, edited after release
  - It found **no theorem shown to be false.**
- **Lean's conventions as a trap.** In Lean, the infimum of an empty set of naturals is 0, so an undefined quantity can silently become a number. One reported target uses `riemannZeta 1`, a value Lean assigns by convention at the pole.
- **The opposing view.** Matt Baker ([blog, Oct 8](https://mattbaker.blog/2026/10/08/some-early-morning-thoughts-on-the-openai-dump/)) puts the chance of a statement mismatch or kernel exploit in the Lean-certified results **below 1%**. He says frontier LLMs are good at spotting such mismatches.
- **Smaller-scale examples.** DeepMind's formal-conjectures repo had an AI "disprove" an OEIS conjecture for about $0.17 of API spend. The statement turned out to be misformalized ([issue #5226](https://github.com/google-deepmind/formal-conjectures/issues/5226)). Several Erdős problem statements, including #124, were corrected after AI attempts exposed ambiguities such as which notion of density was meant ([Xena](https://xenaproject.wordpress.com/)).

---

## 6. Synthesis for slides

### Benefits, with an example for each
1. **Errors found in the canon.** CFSG had 34 deviations, including a false equality and an unjustified closure in the UGT. Stacks had dozens of statements fail in the stated generality.
2. **Speed.** PFR took 3 weeks with humans. Strong PNT took 3 weeks with AI, against 18 months for humans. FLT took 11 days, against a 5-year grant. CFSG took 24 days, against 6 years for Odd Order alone.
3. **New mathematics as a by-product.** CFSG produced a new route to the UGT. Sphere packing produced proofs that are easier to formalize. PFR's constant was improved "for free."
4. **Navigable libraries.** The Stacks tag-to-Lean mapping makes the knowledge base searchable and checkable one piece at a time.
5. **It levels the field.** Amateurs and outsiders can produce checkable arguments (corpus post 2736 on sphere packings).

### Pitfalls, with an example for each
1. **Statement drift (L2).** Navier–Stokes needed m+5 derivatives where the paper had m+4. Some OpenAI "main results" were only lemmas. The OEIS "proof" cost $0.17.
2. **Proof drift (L3).** The AI changes the argument until the code compiles. Lee warns it may "fix it quietly."
3. **Labels that claim more than exists.** OpenAI had 21 "(Lean)" links with no formalization behind them. The Z-in-Q repo has 48 modules but its main theorem still has `sorry`.
4. **Trust stacked on AI-built foundations.** CFSG rests on TauCeti, which is AI-written, and on Lake changes that are not upstream. The CM Hodge result rests on 52k lines of custom definitions.
5. **Claims nobody has reproduced.** 43M or 16M lines that only a company can build. Independent `lake build` runs are still pending.
6. **Proofs too large to understand.** Formal proofs 5 to 20 times the size of Mathlib answer whether something is true and make understanding harder.
7. **Governance and credit.** De Jong's request to keep AI output out, corrections held in a corporate fork, a blank author field on Z-in-Q, and the Navier–Stokes priority dispute.
8. **Gamified progress.** A leaderboard of variable counts stands in for understanding.

### The thesis in one sentence
> Formalization has turned proof checking (L1) into something cheap enough to buy in bulk. Fidelity (L2), understanding (L3), and stewardship of the result are now the scarce resources, and they are where Math 2.0 has to invest.

This lines up with Tao's "Math 1.0 → 2.0" framing. He used it first on Mathstodon on Oct 6, gave a Caltech lecture on Oct 9, and posted to his [blog on Oct 10](https://terrytao.wordpress.com/2026/10/10/math-2-0/). His argument is to move past problem-solving toward understanding and community. Quote from his [slides](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf), not from secondary coverage: the widely quoted "the bottleneck is imagination" line has not been confirmed in his own text.

---

## 7. Voices from the Proofs & Prompts corpus (`data/posts.jsonl`)

| id | Author | Post | Relevance |
|---|---|---|---|
| 848 | Seewoo Lee (EPFL) | [(auto)formalization, but why](https://proofsandprompts.com/2026/09/08/autoformalization-but-why/) | The best short statement of L2 and L3; history of LTE, Flyspeck, and PFR |
| 2654 | Filippo Nuccio (Saint-Étienne) | [Formalisation as a concrete manifestation of mathematical understanding](https://proofsandprompts.com/2026/11/08/formalisation-as-a-concrete-manifestation-of-mathematical-understanding/) | Compares autoformalization to the printing press and human formalization to bookbinding; notes that almost every autoformalization project "relies on Mathlib" |
| 830 | Stepan Nesterov (Stanford) | [Can AI truly prove anything?](https://proofsandprompts.com/2026/09/29/can-ai-truly-prove-anything/) | CFSG, the Four Colour Theorem, and Kepler as precedents for proofs no one person understands. *Note: the post says both were formalized "in Rocq". Kepler was actually done in HOL Light and Isabelle.* |
| 1862 | Antonio Lerario (SISSA) | [The shape of mathematical knowledge](https://proofsandprompts.com/2026/11/09/the-shape-of-mathematical-knowledge/) | The Stacks Project and blueprints as precursors of a layered knowledge graph |
| 630 | Jeremy Avigad (CMU) | [What is mathematics now, and what should it be?](https://proofsandprompts.com/2026/09/07/what-is-mathematics-now-and-what-should-it-be/) | Historical parallel: the 19th-century fight over abstract methods |

The `score.py` annotations (`capability`, `understanding`) could be used to show where these authors sit relative to the rest of the corpus.

---

## 8. Still to verify before presenting
- [ ] Whether anyone outside Axiom has rebuilt CFSG or Stacks and run `#print axioms`.
- [ ] De Jong's Oct 21 statement, from the source (stacks.math.columbia.edu or the GitHub repo).
- [ ] The Z-in-Q version history and dates (V13 on Nov 7 versus the V10/V11 numbering in issue #2). Any reaction from experts in H10 over Q.
- [ ] Whether the OpenAI H10 preprint (an undecidability result) and the Glazer construction depend on each other. Glazer's work builds on the preprint, and the Turing-degree corollary was already in it.
- [ ] Exact quotes from Tao's slides.
- [ ] Line counts: FLT's 13M and CFSG's 43.1M are self-reported. Mathlib is about 2M.
- [ ] Further reading not yet examined: *The Faithfulness Gap* ([arXiv 2606.16541](https://arxiv.org/pdf/2606.16541)); *FormaTheoria*, an academic route toward CFSG ([arXiv 2608.10894](https://arxiv.org/pdf/2608.10894)); *LeanMarathon*'s misformalization audit phase ([arXiv 2606.05400](https://arxiv.org/html/2606.05400)).

## Sources
- Axiom, CFSG: https://axiommath.ai/research/the-enormous-theorem-formalized/
- Audit fork of CFSG: https://github.com/enuminous/CFSG
- Axiom, Stacks: https://axiommath.ai/research/the-stacks-project-formalized/
- Anthropic, FLT: https://anthropic.com/research/formalizing-fermats-last-theorem
- Math, Inc., Strong PNT: https://math-inc.github.io/strongpnt/ · Sphere packing: https://www.math.inc/gauss-on-github · https://arxiv.org/pdf/2604.23468
- Hamilton's theorem: https://arxiv.org/pdf/2608.21502 · Poincaré tracker: https://kingy.ai/mathematics-science-breakthrough-tracker/records/math-poincare-lean-formalization-2026/
- Z in Q: https://github.com/elliotglazer/diophantine-z-q · https://github.com/qqwref/diophantine-z-q · https://github.com/elliotglazer/diophantine-z-q/issues/2 · https://github.com/darkhipo/z-diophantine-research
- OpenAI H10 preprint (entry 004): https://www.emergentmind.com/openai-math-explorer/results/004
- OpenAI release: https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers · https://www.science.org/content/article/openai-just-changed-math-forever-exactly-how-no-one-yet-knows
- Navier–Stokes lost in translation: https://arxiv.org/html/2610.08144v1
- Correction week: https://redreamality.com/blog/ai-math-verification-lean-faithfulness/
- Community audit: https://github.com/borism/openai-math-slop/issues/2
- Matt Baker: https://mattbaker.blog/2026/10/08/some-early-morning-thoughts-on-the-openai-dump/
- Formal-conjectures misformalization: https://github.com/google-deepmind/formal-conjectures/issues/5226
- TauCeti: https://lean-lang.org/use-cases/tau-ceti
- Tao, Math 2.0: https://terrytao.wordpress.com/2026/10/10/math-2-0/
