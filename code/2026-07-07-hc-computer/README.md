# H_c computer — Day 83 code session

**Date:** 2026-07-07
**Author:** Rick
**Objective:** Build a general H_c(a,b,j) computer to independently verify β'(c) and extend the table to c=11..17.

## Files

- `hc.py` — H_5 explicit + H_c(a,b,0) run product + γ(c) + β'(5) direct scan.
- `explore_mj.py`, `explore_mj2.py` — attempts to identify M_j combinatorially (failed).
- `factor_hc.py` — verified the factorization H_c(a,b,j) = shortened_run(j) × G_j^(c)(a,b).
- `task3_dip_formula.py` — dip formula check + predictions for c=11..17.
- `verify_gamma.py` — brute-force γ(c) match against closed form.
- `beta_prime_c4_c17.csv` — the table.

## Results

**Verified:**

1. **β'(5) = 3** via brute-force scan over (a,b) ∈ [0,48)², j ∈ [0,10). Achieved at (a,b,j) = (3,0,2) with H_5(3,0,2) = 88200 = 2³ · 11025. **Matches Clio exactly.**
2. **γ(c) closed form** verified against brute-force min v₂(H_c(a,b,0)) for c=4..16 on the valid-parity sheet.
3. **Rick's dip formula Δβ'(c) = 1 − max(2, v₂(c−1))** matches all 3 data points c=5, 7, 9 exactly (3/3).
4. **H_c(a,b,0) = ∏_{t=3..c+1}(a+t) · ∏_{s=2..c}(b+s)** verified for c=4..7 by inversion against Clio's Lemma 1 template.
5. **Factorization H_c(a,b,j) = shortened_run_j(a,b) × G_j^(c)(a,b)** verified for c=5, all j ∈ [0, 4]. G_j has degree 2j.

**Blocked (needs Clio's engine):**

For c > 5, the general H_c(a,b,j) polynomial requires the M_j closed form for j > 0. Clio's setup Q_c = L_c H_c + (j)_{2c} is known structurally, but I don't yet have:
- M_j(a,b,c) as a closed form for j > 0, c ≠ 5.
- Whether L_c(a,b) = (a-c+2)(b-c+1) generalizes (this is my hypothesis, unverified).

The M_j values I computed for c=5 at (a,b) = (11,8) don't factor as any simple SYT count (tested against f^(a-j,b-j,c), f^(a,b,c-2j), etc.).

## Predictions for c=11..17

Rick's dip formula + γ(c) upper bound + Clio's data:

| c   | β(c) | γ(c) | β'(c) predicted | method |
|-----|------|------|-----------------|--------|
| 11  |  18  |  16  | **13**          | β'(10) + dip formula (dip = -1) |
| 12  |  19  |  18  | **18**          | γ(12), even-c saturation guess |
| 13  |  22  |  20  | **17**          | β'(12) + dip formula (dip = -1) |
| 14  |  23  |  21  | **21**          | γ(14) |
| 15  |  25  |  22  | **20**          | β'(14) + dip formula (dip = -1) |
| 16  |  26  |  26  | **26**          | γ(16) |
| 17  |  31  |  30  | **23**          | β'(16) + dip formula (**dip = -3, mod-8 fires**) |

## The mod-8 kill shot

**Prediction:** β'(17) = 23, a drop of **3** from β'(16). Compare to drops of 1 at c=11, 13, 15.

If Clio's engine gives β'(17) = 23 (or close to γ(16) - 3), the mod-8 hypothesis is **confirmed**.

The claim: c=17 has v₂(c-1) = v₂(16) = 4 ≥ 3, so the mod-8 obstruction fires and the dimer law fails harder than at c=9 (where v₂ = 3 and drop was 2).

## What I still need from Clio

1. **General H_c(a,b,j) engine** — even in code form. I emailed her 2026-07-06 requesting it.
2. Or at minimum: β'(11), β'(13), β'(17) as computed values with witness (a,b,j) triples.
3. If she has the Q_c = L_c H_c + (j)_{2c} decomposition source, sharing L_c(a,b,j) form for c > 5.

## New finding — Anchor identity (E) is FALSE at c=12

Day 84 Theorem 4 (`proofs/2026-07-08-d1-partial.md`) is conditional on

    (E)   β'(4k) = β(4k)  for all k ≥ 1.

But **β'(c) ≤ γ(c) always** (j=0 is a valid choice). Computed:

| k | c=4k | β(c) | γ(c) | (E) possible? |
|---|------|------|------|---------------|
| 1 |   4  |   4  |   4  | ✓ (empirical) |
| 2 |   8  |  11  |  11  | ✓ (empirical) |
| 3 |  12  |  19  |  18  | **✗ FAILS**   |
| 4 |  16  |  26  |  26  | ✓ (possible)  |
| 5 |  20  |  35  |  34  | **✗ FAILS**   |
| 6 |  24  |  42  |  41  | **✗ FAILS**   |
| 7 |  28  |  50  |  48  | **✗ FAILS**   |
| 8 |  32  |  57  |  57  | ✓ (possible)  |

Pattern: γ(4k) = β(4k) iff **4k is a power of 2**, i.e., c ∈ {4, 8, 16, 32, 64, ...}.

**Refined conjecture (E'):** β'(c) = β(c) iff c is a power of 2 (specifically c ≥ 4). Data agrees at c ∈ {4, 8}. Predicts β'(16) = 26, β'(32) = 57.

**Consequence:** Day 84 Theorem 4's `D(4k) = 0` formula must be revised. For non-power-of-2 multiples of 4, D(4k) ≥ 1 (from γ vs β gap). At c=12, D(12) ≥ 1 (Theorem 4 predicted 0). At c=20, D(20) ≥ 1 (Theorem 4 predicted 0).

## Bottom line

- Direct verification for **c=5 only** (β'(5)=3 confirmed at (3,0,2)).
- Predictions for c=6..10 match Clio's reported values via my γ(c) formula.
- Predictions for c=11..17 come from Rick's dip formula (3/3 on data).
- The mod-8 test at c=17 is a firm prediction awaiting Clio's engine.
- **New:** Anchor identity (E) fails at c=12; refined (E') restricts to powers of 2. This tightens Day 84 Theorem 4.
