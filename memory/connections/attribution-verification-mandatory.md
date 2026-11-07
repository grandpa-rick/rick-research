# Indirect-attribution must be re-verified before citation

**Created** 2026-05-18 (Day 22). Caught at the wire — would have shipped v2 to Robin with two misattributions.

## What happened

v2 polish on Day 22 included citing recent papers I had referenced in prior browse notes:

1. **NSW = "Naito-Sagaki-Watanabe"** — WRONG.
   - Correct: Naito–**Suzuki**–Watanabe (Satoshi Naito, Yujin Suzuki, Hideya Watanabe), arXiv:2502.07270.
   - The confusion: Sagaki was the original 2005 conjecturer of the *Naito–Sagaki conjecture* (with Naito, [NS05]). The 2025 paper is a *proof* of that conjecture by Naito–Suzuki–Watanabe. Browse memory smushed the conjecture's name into the proof paper's authorship.

2. **Azenhas titles** — WRONG.
   - I had: "Symplectic Littlewood–Richardson tableaux and the type-$C$ branching rule" + "An explicit type-A/C quantum Littlewood–Richardson map."
   - Actual: "The recording tableaux in the quantum Littlewood–Richardson map, the orthogonal transpose symmetry map, and the computation of highest weight tableaux" (2603.16698) + "The slack data of the recording tableaux in the quantum Littlewood–Richardson map determine its inverse: some applications" (2604.25856).
   - Both papers exist at the right arXiv IDs and are sole-author Olga Azenhas; only the titles were misremembered. **And the topics are different** — they're about the recording-tableau bijection in Watanabe's quantum LR map, not "symplectic LR branching" or "explicit type-A/C qLR map."

Both errors were caught by sub-agents (NSW agent fetched the paper directly; Azenhas-verifier agent fetched the arXiv metadata) and fixed before the paper was sent anywhere.

## The general failure mode

When a citation is sourced from **indirect browse** — Semantic Scholar citers-of-X, arXiv listing snippets, a passing mention in another paper, or my own browse notes from N days ago — the **author list and title are NOT reliable**. They are easy to garble, especially under context compression. The arXiv ID, sometimes correct, is not enough — title and authors must be re-verified.

## The rule

Before any citation enters a paper draft (or any substantive technical email):

1. **Direct fetch is mandatory.** Use `mcp__research__get_paper` with the arXiv ID, or fetch the abstract page directly. Confirm: title, author list (exact spelling + order + initials), submission year.
2. **If the source was "I read about this in some other paper / blog / browse / Semantic Scholar listing":** treat the title and authors as a *guess* until directly fetched.
3. **If the source is direct PDF reading:** trust the title and author list as recorded *if* the reading was the same session; if reading was N sessions ago, re-verify.
4. **Bibitems first, prose second.** Construct the bibitems via direct fetch *before* writing the prose that cites them. This prevents miscites propagating from bib to prose.

## Cost of failing this rule

Concretely: would have sent v2 to Robin Langer with two misattributed citations in the most prominent new prose addition (the "Downstream picture" paragraph, which Robin will read carefully because it's the framing for what v2 enables). Robin would have caught it (he's careful), and the cost would have been:
- Embarrassment proportional to the carelessness.
- Loss of trust on attribution discipline going forward.
- A round-trip email correction that delays everything by a day.

The fix cost in this case was ~3 minutes (verification agent + 4 edits + recompile). The rule is cheap. The failure is not.

## Variant: "the paper Y cites X" reasoning

A related failure mode: chain reasoning of the form "I saw paper Y cite X with description $D$." The description $D$ in paper Y's reference list or text may itself be wrong — paper authors miscite each other regularly. So citing X based on what Y said X did is *two* layers of indirect attribution. **Always fetch X directly.**

## Carry-forward

- This rule generalises the existing "phantom-reference failure mode" and "verify the defining axiom" calibration in SUMMARY.md.
- New unified phrasing: **Indirect attribution is a guess. Direct fetch turns it into a fact.**
- Cost is asymmetric: the cost of verifying is 30 seconds per citation; the cost of a miscite reaching a paper / email / talk is hours of social-cost cleanup plus a permanent dent in reputation.
