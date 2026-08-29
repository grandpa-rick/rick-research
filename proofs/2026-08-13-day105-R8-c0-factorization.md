# Day 105 — Factorization of c_0 = Q_{16}(6, 8, R=8) and Verdict on H4

**Date:** 2026-08-13
**Data:** `/home/agent/projects/code/2026-08-14-day105-R8-samples.json` (37 samples of Q_{16}(6, 8, c) at c ≡ 8 mod 16, t = (c-8)/16 running 1..37).
**Method:** Sympy `Matrix.solve` on the 37×37 Vandermonde system in t; c_0 is the constant term, i.e. the extrapolation to t=0 (c = 8 = R).

## Result

The Vandermonde solve is exact (rationals; solution vector lies in Z as expected). The constant term:

    c_0 = Q_{16}(6, 8, 8) = 306,128,067,620,555,980,800,000

The full sympy `factorint` succeeded instantly (integer only 24 digits):

    c_0 = 2^29 · 3^12 · 5^5 · 7^4 · 11 · 13

## Valuations at small primes

| p  | v_p(c_0) |
|----|----------|
| 2  | 29 |
| 3  | 12 |
| 5  | 5  |
| 7  | 4  |
| 11 | 1  |
| 13 | 1  |
| 17 | 0  |
| 19 | 0  |

## Verdict on H4: **PARTIAL**

H4 predicted c_0 = 2^29 · 3^8 · 5^4 · 7^2 · 11 · 13, i.e. exponent pattern (8, 4, 2, 1, 1) on primes (3, 5, 7, 11, 13).

What H4 got right:
- **v_2(c_0) = 29 — exact match.** The power-of-2 prediction is confirmed.
- **Prime support = {3, 5, 7, 11, 13}** — exactly the odd primes ≤ 2R−1 = 15. No 17, no 19, no larger primes. This is a real structural constraint.
- **Plateau at exponent 1 for the top primes (11, 13).** Confirmed.

What H4 got wrong:
- The doubling pattern (8, 4, 2, …) for exponents on the small odd primes is **not** what appears. Actual exponents on (3, 5, 7) are (12, 5, 4), not (8, 4, 2). The ratio |c_0|/H4_predicted = 3^4 · 5 · 7^2 = 19,845.

## What IS the exponent pattern?

Comparing to Legendre's formula (v_p((2R)!) = Σ_j ⌊2R/p^j⌋ with 2R=16):

| p  | v_p((2R)!) | v_p(c_0) |
|----|------------|----------|
| 3  | 6          | 12       |
| 5  | 3          | 5        |
| 7  | 2          | 4        |
| 11 | 1          | 1        |
| 13 | 1          | 1        |

For p ∈ {7, 11, 13} we have v_p(c_0) = 2·v_p((2R)!). For p = 3 we again have exactly 2·v_p((16)!) = 12. But p = 5 gives 5 rather than 6, so the "twice-Legendre" rule *almost* holds but fails at p=5 by one. Meanwhile the plateau primes (11, 13) satisfy both "= 1" and "= 2·v_p((2R)!)" because v_p((2R)!) = 1 for p in (2R/2, 2R].

So the true pattern seems close to v_p(c_0) = 2 v_p((2R)!) with a defect at p=5. One data point (R=8) is not enough to fix a formula; comparison with R=6 and R=10 data would nail down the rule.

## Recommended next step

Rerun the same factorization on the R=6 and R=10 constant terms (Rick already has R=10 samples from Day 104). If the "2·v_p((2R)!)" rule holds elsewhere, the anomaly at p=5, R=8 is genuinely diagnostic; if it fails, H4 needs replacement by a different multiplicative formula.

## Files produced
- `/home/agent/projects/code/2026-08-14-day105-R8-c0-factor.py` (script)
- `/home/agent/projects/code/2026-08-14-day105-R8-c0-result.json` (structured result)
