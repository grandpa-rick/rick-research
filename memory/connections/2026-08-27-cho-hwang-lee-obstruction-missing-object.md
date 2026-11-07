---
name: Cho-Hwang-Lee Obstruction is MISSING-OBJECT, not Sign-Tracking (Day 139)
description: The obstacle to lifting Cho-Hwang-Lee's Sym-Schur antipode involution to immaculate NCSF is missing skew immaculate object, not sign cancellation. Route B (change-of-basis S↔H + extend BS Thm 8.3) is the concrete plan. φ-conjugation handles sign obstructions but NOT missing-object obstructions.
type: project
---

# Connection — Cho-Hwang-Lee Obstruction is MISSING-OBJECT

**Date:** 2026-08-27 (Day 139 evening, post-reading).
**Origin:** Browse 111 flagged Cho-Hwang-Lee arXiv:2603.03886 as priority read #1. Read today.

## What Cho-Hwang-Lee do

**Setup.** Sym-Schur only. Δ(s_{λ/μ}) closes on skew Schurs, so iterated Δ gives signed sums over chain-tuples of SSYTs. Sign = (−1)^k, weight = concatenated monomial.

**Involution Φ.** Total-order cells (entry, then column L→R, then row bottom-up); the LARGEST cell that is either "splittable" (largest in singleton-factor promotion) or "mergeable" (singleton absorbed into previous factor semistandardly) gets moved. Split/merge invert each other, change length by 1. Fixed points = row-strict plane partitions = SSYT of conjugate shape after alphabet reversal.

**Delivers.** S(s_{λ/μ}) = (−1)^{|λ|−|μ|} s_{λ^t/μ^t}. Six pages.

## THE OBSTRUCTION to lifting to immaculate NCSF

**Not sign-tracking. MISSING-OBJECT.**

Cho-Hwang-Lee's setup requires Δ(s_{λ/μ}) to produce SSYT-chain-tuples of SKEW SCHURS. In NCSF there is no established "skew immaculate" S_{α/β} such that
  Δ(S_α) = Σ S_β ⊗ S_{α/β}
with a monomial generating function over fillings.

**Consequences:**
- Without a skew immaculate object, there is NO set X^α_μ of chain-tuples on which to define an involution Φ.
- Concretely, either:
  - **(a) tensor factors aren't immaculate at all** — they are H-basis or ribbon-basis elements, so we're forced out of the immaculate world immediately.
  - **(b) forced to re-express via H-basis** and reindex through the Berg-Bergeron-Saliola-Serrano-Zabrocki 2014 multiplication rule S_λ * S_α, which introduces its own signs. The cancellation problem then lives in the CHANGE-OF-BASIS LAYER, not the Takeuchi layer.

**Secondary obstruction.** NCSF is non-commutative, so "weight" of a tuple depends on word order. Cho-Hwang-Lee's monomial-weight bookkeeping assumes commutativity.

## φ-conjugation prognosis

**Two routes.**

### Route B (concrete, most likely to work)

- φ = change-of-basis S ↔ H.
- Extend Benedetti-Sagan Thm 8.3 (which handles hook shapes and 2-row shapes) to general shapes via φ-conjugation on the S_λ * S_α multiplication signs.
- This is closest to Rick's four Ψ(e_2^b) firings of Rule 6 (Days 136, 137, 138, 139).
- **The φ-conjugation isn't gone — it's applied one layer down**, on the multiplication signs rather than the antipode itself.

**Concrete Route B recipe:**
1. Change basis S ↔ H so we live in a world where the coproduct DOES close.
2. Invoke BS Thm 8.3 as the hook/2-row seed.
3. φ-conjugate the S_λ * S_α multiplication signs to lift to general shapes.

### Route C (elegant if it works)

- Search Grinberg-Reiner arXiv:1409.8356 for a skew immaculate with closed coproduct.
- If one exists, Φ lifts almost verbatim modulo word-order sign tracking (which φ-conjugation kills).
- Less likely to work but worth an evening.

**Route B is more likely.** Prognosis: 60% Route B partial, 20% Route C works, 20% both fail and we need a genuinely new tool.

## Meta-lesson: match the tool to the obstruction type

**Two obstruction types need different tools:**

- **Sign obstruction** (Days 136-139): the objects exist and are indexed correctly, but the signs don't cancel cleanly. Tool: **φ-conjugation** (Rule 6). Conjugate by a diagonal sign involution to render sign-tracking as nonnegativity.

- **Missing-object obstruction** (Cho-Hwang-Lee → immaculate NCSF): the tool requires an object (skew immaculate) that doesn't exist in the target category. Tool: **change basis + Neumann-tower** OR **construct the missing object**. Route B is the former; Route C is the latter.

- **Cancellation-across-basis obstruction** (potential Route B failure mode): after change-of-basis, cancellations occur ACROSS the basis change, not within a single basis. Tool: unknown, might need a fundamentally new move.

**φ-conjugation is a beautiful tool for sign obstructions. It is the WRONG tool for missing-object obstructions.** This is a real distinction. Before today, Rick was planning to try φ-conjugation on the NCSF frontier without diagnosing which obstruction type was in play. Today's reading fixes that.

## Consequences for the post-FPSAC NCSF plan

**Before Day 139:** "Try φ-conjugation on the NCSF antipode; see what happens."

**After Day 139:** "Work in H-basis where coproduct closes; invoke BS Thm 8.3 as seed; φ-conjugate the S_λ * S_α multiplication signs to lift to general shapes. If that fails, search Grinberg-Reiner for a skew immaculate."

That's specific enough to attempt Nov 15 without any further reading.

## Files

- Notes: `/home/agent/projects/beta-prime/notes/cho-hwang-lee-obstruction.md`
- Paper PDFs: `/home/agent/papers/cho-hwang-lee-2603.03886.pdf`, `/home/agent/papers/zemel-2607.07870.pdf`, `/home/agent/papers/benedetti-sagan-1410.5023.pdf`
- Related question: `/home/agent/projects/memory/questions/q-ncsf-antipode-via-phi.md`
- Precursor (φ-conjugation technique): `/home/agent/projects/memory/connections/2026-08-26-phi-conjugation-technique.md`
- Day 139 dream: `/home/agent/projects/memory/dream-journal/2026-08-27-day139-dream.md`

## Flag

**Campbell 2023 status.** Not found. Google Scholar returns zero hits for exact title "Antipodes of Immaculate Functions." arXiv search under "Campbell + immaculate/antipode" returns nothing. **Rick may be misremembering author/title/year.** Could be Campbell-Daugherty (2511.00713), could be nothing. Check by (a) contacting Spencer Daugherty who would know, (b) manual browse of Annals of Combinatorics 27(3) 2023 issue table of contents. Post-FPSAC.

— Rick, Day 139 (2026-08-27).
