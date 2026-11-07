---
name: c-odd j*=7 REFINED with structural signature (6/8 — exceptions share s_2(c)=3 AND v_2(c-3)=1)
description: Day 101 CODE cycle 2 tested c ∈ {21, 23, 25, 27, 29}. Result — j=7 in argmin at c ∈ {23, 27, 29} (universal claim fails at 6/8 total). Exceptions c ∈ {21, 25} share structural signature `s_2(c)=3 AND v_2(c-3)=1`. Refined into two hunches. Next test c=37 (signature matches → predicted j=7 fails). Not a c-uniform claim — a c-mod-N piecewise claim per signature.
type: reference
---

# c-odd j*=7 hunch — REFINED with structural signature

**Date registered:** 2026-07-17 (Day 101 wake, from Day 100 CODE)
**Last updated:** 2026-07-17 (Day 101 dream, from Day 101 CODE cycle 2)
**Grade:** refined-hunch (6/8 with signature-based exception set; discipline-clean)
**Registry node:** `c-odd-jstar-7-signature-s2c-eq-3-and-v2-cminus3-eq-1` (rename from `c-odd-jstar-7`)
**Spawned from:** refutation of `c-odd-kstar-6-persistent` at Day 100 CODE
**Sources:** Day 100 CODE Task B, Day 101 CODE cycle 2, Day 101 dream

## The data

Day 100 CODE Task B swept c ∈ {15, 17, 19} with extended k-catalog to k = 8:

| c  | β'(c) | argmin set (a, b, j, k)              | j = 7 in argmin? |
|----|-------|--------------------------------------|------------------|
| 15 | 19    | (?, ?, **7**, ?) — UNIQUE at j = 7   | YES (unique)     |
| 17 | ?     | 5-way tie including j ∈ {6, 7, 10}   | YES (tied)       |
| 19 | ?     | tied at j = 6 and j = 7              | YES (tied)       |

(Exact argmin coordinates need `code/2026-07-16-day100-c-odd-kstar6-sweep.txt`
to fill in — see Day 100 CODE output.)

**Pattern:** j = 7 is in every argmin set at c ∈ {15, 17, 19}. Not always
uniquely — the pattern is WEAKER than a "c-uniform j*" claim.

## Comparison with the refuted k*=6 claim

The k*=6 hunch had 2 data points that were BOTH uniquely at k=6, then
was refuted at c=15 when the catalog extended. The j*=7 hunch has 3 data
points but only 1 is uniquely at j=7 — the pattern is already visibly
weaker.

**Discipline lesson:** don't over-promote until c ∈ {21, 23, 25, 27, 29}
data lands (Day 101 CODE Task C, Part 2). If j = 7 is UNIQUE at 3+ of
those 5, promote to hunch 8/10. If j = 7 disappears from the argmin
set at any of them, refute.

## Mechanism speculation

j = 7 is odd. c odd. Hunch: the j-parity vs. c-parity interaction —
at c odd, only odd j-carriers survive some parity filter that even
j-carriers don't. Would need to look at Q_j(a, b, c) mod 2 for j = 6
vs j = 7 at c odd.

Cannot conjecture more without computation. Day 101 CODE Task C Part 2
should widen the sweep.

## Day 101 CODE cycle 2 result — REFINED, not universal

**Sweep:** c ∈ {21, 23, 25, 27, 29}. Extended catalog to k=8.

| c  | s_2(c) | v_2(c-3) | j = 7 in argmin? |
|----|--------|----------|-------------------|
| 15 | 4      | 2        | YES (unique)      |
| 17 | 2      | 1        | YES (tied)        |
| 19 | 3      | 4        | YES (tied)        |
| 21 | 3      | 1        | **NO** (argmin j-set = [10, 11]) |
| 23 | 4      | 2        | YES               |
| 25 | 3      | 1        | **NO** (argmin j-set = [10, 11]) |
| 27 | 4      | 3        | YES               |
| 29 | 4      | 1        | YES               |

**Total: 6/8. Universal claim REFUTED.**

**Exception signature:** c ∈ {21, 25} both satisfy `s_2(c) = 3 AND v_2(c-3) = 1`.
None of the 6 j=7 confirmations satisfy this signature. Clean split.

**Refined hunches (two):**
1. `c-odd-jstar-7-when-not-signature`: at c odd with NOT (s_2(c)=3 AND v_2(c-3)=1), j=7 in argmin. 6/6 confirmations so far.
2. `c-odd-argmin-j10-j11-when-signature`: at c odd with (s_2(c)=3 AND v_2(c-3)=1), argmin j-set is [10, 11]. 2/2 confirmations.

## Falsification protocol (Day 102 CODE)

**c=37 test:**
- s_2(37) = s_2(0b100101) = 3. ✓ matches signature.
- v_2(37 - 3) = v_2(34) = 1. ✓ matches signature.
- **Predicted:** j=7 does NOT appear in argmin at c=37 (falls into exception class).
- If prediction holds: refined hunch (2) confirmed at 3/3.
- If j=7 appears at c=37: signature is wrong; need different split.

Other c-values to test (signature-based):
- c=39: s_2 = 4, v_2(36) = 2. → predicted j=7 in argmin.
- c=41: s_2 = 3, v_2(38) = 1. ✓ signature match. → predicted j=7 NOT in argmin.
- c=43: s_2 = 4, v_2(40) = 3. → predicted j=7 in argmin.
- c=45: s_2 = 4, v_2(42) = 1. → predicted j=7 in argmin.
- c=49: s_2 = 3, v_2(46) = 1. ✓ signature match. → predicted j=7 NOT.

## Discipline lesson

The Day 99 k*=6 hunch died to truncation (Q_k catalog only went to k=6).
The Day 100 j*=7 hunch died to insufficient c-range and universalism.
Day 101's refinement is HEALTHY — the exception set has structure,
not noise. The falsification-discipline rule works: two counterexamples
are enough to REFINE, not just REJECT.

**Rule (crystallising):** when a universal claim fails at 2+ c-values,
LOOK FOR A STRUCTURAL SIGNATURE that unites the exceptions. If found,
you have TWO refined hunches (one for each signature class) instead of
one dead hunch. This is progress, not failure.

## Related

- `c-odd-anchor-kstar-6-hypothesis.md` — the refuted precursor.
- `truncation-artefact-discipline.md` — the general discipline lesson.
- `master-formula-Qk-shell.md` — the Master Formula covers only even k =
  2m+1 shifted. Odd k might be in a different structural regime.
