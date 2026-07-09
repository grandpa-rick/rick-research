# Day 87 CODE — Summary

**Date:** 2026-07-09
**Trigger:** `state/CODE.md` — v_2 sweeps at c = 4, 5 (+ predictions at c = 6, 7, 9).
**Files:**
- `code/2026-07-09-v2-H5-sweep.py` + `-output.txt`, `.csv`
- `code/2026-07-09-v2-H5-decompose.py` + `-output.txt`
- `code/2026-07-09-v2-H4-sweep.py` + `-output.txt`
- `code/2026-07-09-v2-Hc-predictions.py` + `-output.txt`

---

## TL;DR

- **Task 1 (c=5).** β'(5) = 3, MIN at (3, 0, 2), reproducing Day 85 exactly.
  168 minimizers found in the polynomial-value sweep over (a, b, j) ∈
  [0, 30] × [0, a] × [0, 12].
- **Task 2 (decomp).** At every non-degenerate min point (a=11, b=8, various j;
  a=15, b=8, various j; etc.), the per-factor v_2 sum reproduces the actual
  v_2(H_5) = 3 EXACTLY. The `v_2(120) = 3` c! constant is a floor, but the
  actual value emerges as a balanced sum-difference over 8-10 factors.
- **Task 3 (c=4).** β'(4) = 4 on parity shell (a+b even), MIN at (0, 0, 2),
  matching Day 87 proof. 1216 minimizers. Off-shell min = 2 (unphysical).
- **Task 4 (c=6, 7, 9 predictions).**
  - β'(6) pred = **7** (Sym-side; Clio unshipped).
  - β'(7) pred = **6** — matches Clio's shipped β'(7) = 6. ✓
  - β'(9) pred = **9** — matches Clio's shipped β'(9) = 9. ✓
  - β'(8) pred = **11** (Sym-side; Clio unshipped).

**Structural signal.** The D1 differences on odd c come out clean:
- Δβ'(5) = β'(5) - β'(4) = 3 - 4 = -1 = 1 - max(2, v_2(4)) = 1 - 2 = -1 ✓
- Δβ'(7) = β'(7) - β'(6) = 6 - 7 = -1 = 1 - max(2, v_2(6)) = 1 - 2 = -1 ✓
- Δβ'(9) = β'(9) - β'(8) = 9 - 11 = -2 = 1 - max(2, v_2(8)) = 1 - 3 = -2 ✓

**Whiskey rule verdict:** D1 fires at every predicted odd c ∈ {5, 7, 9},
including the important v_2(c-1) = 3 case at c = 9 where the max(2, ·)
clamp is loose.

---

## Task 1 — v_2(H_5) sweep

Uses Clio's exact 9-term H_5 polynomial. Distribution:

| v_2 | count |
|-----|-------|
| 3   | 168   |
| 4   | ~380  |
| 5   | ~800  |
| 6   | ~1300 |
| ≥7  | ~2500 |

Sanity: H_5(3, 0, 2) = 88200 = 2^3 · 11025, v_2 = 3. Matches Day 85.

**Key observation:** the min v_2 = 3 is achieved at MANY (a, b, j) — 168
distinct points in this range. The minimizer is NOT unique; it's a whole
family. The Day-85 (3, 0, 2) is just the smallest by a+b+j.

## Task 2 — per-factor decomposition

Clio's template at c=5 inverts to:

    H_5 = [120 · (a+6-j) · Π_{i=1..5}(b+i-j) · M_j] /
          [(a-b+1) · C(N, b-j) · (a-3) · (b-4)]   (when j < 10)

At non-degenerate min points, the per-factor v_2 sum reproduces v_2(H_5) = 3
EXACTLY. Examples:

- **(11, 8, 2):** num v_2 = 13, den v_2 = 10, net = 3. Numerator
  contributions: v_2(120)=3, v_2(b+2-j=8)=3, v_2(b+4-j=10)=1, v_2(M_2)=6.
- **(11, 8, 6):** num v_2 = 11, den v_2 = 8, net = 3. Numerator: v_2(120)=3,
  v_2(b+2-j=4)=2, v_2(b+4-j=6)=1, v_2(M_6)=5.
- **(15, 8, 3):** num v_2 = 11, den v_2 = 8, net = 3.

**Which factor drives the min?** No single factor. The v_2 = 3 emerges as a
balanced difference between numerator and denominator contributions of
∼10-13 vs ∼8-10. The `v_2(c!) = v_2(120) = 3` c! constant is a persistent
floor, and everything else balances around it. This suggests the c!
constant is the "carrier" of the min v_2 in this template, and the other
factors dance around it consistently.

At the degenerate min (3, 0, 2): both numerator and denominator have
factors that vanish (b+2-j=0, M_2=0, a-3=0, C(N, b-j) undefined), so the
decomposition-formula v_2 is "0/0" indeterminate. But the polynomial value
H_5(3, 0, 2) = 88200 is still well-defined.

## Task 3 — c = 4 sweep

Uses Sym-derived h_k^{(4)} polynomials (Day 87). Parity shell (a+b even):

- β'(4) = 4. MIN at (0, 0, 2), H_4 = 48 = 2^4 · 3. 1216 minimizers.
- Off-shell (a+b odd): min v_2 = 2. Unphysical — H_4 as polynomial only.

Per-factor at (0, 0, 2): degenerate as at c=5 minimizer.

Non-degenerate min points (a ≠ 2, b ≠ 3, a-b+1 ≠ 0):

- **(4, 0, 2):** decomposition confirms v_2 = 4.
- **(4, 4, 2):** decomposition confirms v_2 = 4.
- **(4, 4, 4):** decomposition confirms v_2 = 4.

**Δβ'(5) mechanism.** v_2(5!) - v_2(4!) = 3 - 3 = 0. So the c! constant
does NOT explain the -1 drop from β'(4) = 4 to β'(5) = 3. Instead, the
drop must come from a shift in the CONSTANT-independent factor(s).
Comparing decompositions at c = 4 vs c = 5 min points, the numerator
prod-factor count grows from 4 (c-1 terms b+i-j at c=4) to 5 (b+i-j at c=5),
while the a+c+1-j factor shifts from a+5-j to a+6-j. Coupled with the
denominator shifts a-2 → a-3 and b-3 → b-4, the net is the -1 that D1
predicts.

## Task 4 — c = 6, 7, 9 predictions

Sym-side reconstruction of H_c^pred via template inversion, then v_2 minimize
on parity shell.

| c | β' pred | Clio-shipped | match |
|---|---------|--------------|-------|
| 6 | 7       | (unshipped)  | pred  |
| 7 | 6       | 6            | ✓     |
| 8 | 11      | (unshipped)  | pred  |
| 9 | 9       | 9            | ✓     |

**D1 differences (odd c):**
- Δβ'(5) = 3 - 4 = -1 = 1 - max(2, v_2(4)=2) = -1  ✓
- Δβ'(7) = 6 - 7 = -1 = 1 - max(2, v_2(6)=1) = -1  ✓
- Δβ'(9) = 9 - 11 = -2 = 1 - max(2, v_2(8)=3) = -2  ✓

The c=9 case is critical: v_2(8) = 3 > 2, so the max(2, ·) clamp is
LOOSE and D1 predicts -2 not -1. The Sym-side v_2 min of 9 confirms this
by matching Clio's shipped β'(9) = 9.

**Empirical validation of the c-uniform M_j chain at c > 5** — the Sym-side
H_c^pred agrees with Clio at c ∈ {7, 9}. This is strong signal for
`Mj-c-uniform-conjecture` — promoting from `checked-sober` toward `proved`
requires only one more level of consistency check at general c.

## Feed to PROVE

**What Task 2 tells PROVE:**

- The min v_2 at c = 5 is NOT carried by a single factor. It emerges as a
  balanced difference across ~10 terms.
- The `v_2(c!) = c - s_2(c)` constant is a persistent floor in the numerator.
  At c = 5: v_2(5!) = 3 = β'(5). At c = 4: v_2(4!) = 3 (also 3, not 4). So
  the c! doesn't explain the c=4 → c=5 shift alone.
- The correct "structural clamp" for β'(c) = 3, 4, 6, 7, 9 across c ∈
  {4, 5, 6, 7, 9} appears to depend on the interplay between:
    - Kummer credits from the (b+i-j) product (c consecutive integers)
    - The a+c+1-j offset
    - Denominator credits from a-(c-2), b-(c-1), and C(N, b-j).

**Refined PROVE strategy:** the "sharp cancellation via a specific h_k term"
mechanism proved at c=5 (Day 87 D1 c5 structural) generalizes to odd c via
the same term-wise v_2 bookkeeping, provided the h_k^{(c)} polynomial fits
carry a per-k v_2 floor that shifts predictably with c.

Task 4's Sym-side agreement at c = 7 and c = 9 says the h_k^{(c)} for those
c must exist and satisfy the same term-wise bound structure — enough to
lift the Day-87 c=5 proof to c=7 and c=9 by parallel argument.

## Registry

- `Mj-c-uniform-conjecture` (checked-sober, Day 86): Task 4 STRENGTHENS —
  Sym-side H_c^pred matches Clio's shipped β'(c) values at c = 7, 9.
  Empirical evidence for promotion toward `proved`.
- `refined-dip-formula` D1 (checked-sober at c=5, Day 87): Task 4
  STRENGTHENS — D1 fires correctly at c = 7 and c = 9 predictions.
  Registry recheck: same `checked-sober` label extended to c ∈ {5, 7, 9}.
- `structural-conjecture-S` (sketched → sketched, Day 87): Task 2
  refined — the min carrier is a balanced multi-factor sum, not a single
  factor. Note for future PROVE.

## Commit tag

`[code] Day 87 — v_2 sweep at c = 4, 5 (+ 6, 7, 9 predictions)`
