# Day 137 — Density verification stretched to b = 12

## Setup

Script: `verify_density_b12.py` (sympy).
Method: iterate the Day-131 recursion
```
  Psi_{b+1} = [E_2 - (b+1) E_1 + (b+1)^2] Psi_b
              - 3 b       E_3 sigma(Psi_{b-1})
              -  b(b-1)(E_1 - 2b - 2) E_3 sigma(Psi_{b-2})
```
with sigma(E_1) = E_1 - 3, sigma(E_2) = E_2 - 2 E_1 + 3,
sigma(E_3) = E_3 - E_2 + E_1 - 1.

**Base cases (verified against `Psi_direct` in day128):**
`Psi_0 = 1`, `Psi_1 = E_2 - E_1 + 1`.

The task-brief line "Psi_1 = E_2 + 1" is missing the `-E_1` term; with
that omission the sequence diverges from the true `T(e_2^b V)/V`. The
`day136/verify_phi_recursion.py` script already contains the correct
`Psi_1`, and Day-135 verified through b = 10, so we adopted the same
base cases here.

Total runtime: **~6 seconds** (well under the 3-min budget).

Cross-check against `Psi_direct` for b = 0..6: exact match at every b.

## 1. Density conjecture (main result)

For every `b` in `2..12` and every weight `w` in `0..b`, the number of
nonzero coefficients of `[E_1^{x1} E_2^{x2} E_3^{x3}] Psi_b` with
`x1 + x2 + 2 x3 = w` equals

  `A002620(w + 2) = floor((w+2)^2 / 4)`

which is `p_{1,1,2}(w)` — the number of admissible triples.

**No zero coefficients found anywhere.** Full support at every
(b, w) slice for `b = 2..12`. Density conjecture CONFIRMED to b = 12.

Support table (nonzero / allowed, `=` means full):
```
  b    w=0    w=1    w=2    w=3    w=4    w=5    w=6    w=7    w=8    w=9   w=10   w=11   w=12
  2   1/1=   2/2=   4/4=
  3   1/1=   2/2=   4/4=   6/6=
  4   1/1=   2/2=   4/4=   6/6=   9/9=
  ...
 12   1/1=   2/2=   4/4=   6/6=   9/9=  12/12=  16/16= 20/20=  25/25= 30/30= 36/36= 42/42=  49/49=
```

## 2. P_b := phi(Psi_b) strict positivity

phi: E_1 -> -E_1, E_2 -> E_2, E_3 -> -E_3.

For b = 2..10, every coefficient of P_b at an admissible monomial is a
**strictly positive integer**. Total counts:

| b  | # nonzero (= total allowed) |
|----|-----------------------------|
|  2 | 7   |
|  3 | 13  |
|  4 | 22  |
|  5 | 34  |
|  6 | 50  |
|  7 | 70  |
|  8 | 95  |
|  9 | 125 |
| 10 | 161 |

VERDICT: strict positivity of P_b holds for `b = 2..10`.

## 3. Extremal monomials at b = 8, 10, 12

| b  | [E_2^b]  | [E_3^{b/2}] | [E_1^b] |
|----|----------|-------------|---------|
|  8 | 1        | 8 505       | 40 320 = 8! |
| 10 | 1        | -229 635    | 3 628 800 = 10! |
| 12 | 1        | 7 577 955   | 479 001 600 = 12! |

Observations:
- `[E_2^b] Psi_b = 1` for all b (top-weight-0 monomial).
- `[E_1^b] Psi_b = b!` (nonzero at all b; this is the value at the
  extreme high-E_1 monomial).
- `[E_3^{b/2}] Psi_b` alternates sign with `b/2` and grows rapidly.

## 4. Smallest-magnitude nonzero coefficients (thinnest monomials)

**Psi_10, top 5 smallest |coefficient|:**

| monomial      | weight | coeff |
|---------------|--------|-------|
| `E_2^10`      | 10     | 1     |
| `E_1 E_2^9`   | 10     | -55   |
| `E_2^8 E_3`   | 10     | -135  |
| `E_2^9`       | 9      | 385   |
| `E_1^2 E_2^8` | 10     | 1 320 |

**Psi_8, top 5 smallest |coefficient|:**

| monomial      | weight | coeff |
|---------------|--------|-------|
| `E_2^8`       | 8      | 1     |
| `E_1 E_2^7`   | 8      | -36   |
| `E_2^6 E_3`   | 8      | -84   |
| `E_2^7`       | 7      | 204   |
| `E_1^2 E_2^6` | 8      | 546   |

**Pattern:** the thinnest monomials are the ones nearest to `E_2^b`
(top-weight, high powers of E_2, low powers of E_1 and E_3). These
are structurally special: `E_2^b` itself always has coefficient `+1`,
and small perturbations `E_1^i E_2^{b-i}` (small `i`) or
`E_2^{b-2j} E_3^j` (small `j`) sit at the next magnitudes.

**Implication for the proof of strict positivity of P_b:** if
positivity ever fails, the failure would appear first in one of these
top-weight `E_2^{b-...}` corners, where the coefficient magnitudes are
smallest and the arithmetic cancellations are tightest. Through b = 12
(density) and b = 10 (strict positivity of P_b) no such failure occurs,
and the coefficients grow with `b` at each named corner (`[E_1 E_2^{b-1}] Psi_b`
values: -35 -> -36 -> -55 for b = 7, 8, 10, so grows in magnitude).

## Summary

1. Density conjecture — CONFIRMED for b = 2..12, no zero coefficients
   at any admissible monomial.
2. Support cardinalities per weight w match `A002620(w+2)` exactly.
3. P_b = phi(Psi_b) has strictly positive integer coefficients for
   b = 2..10 at every admissible monomial (161 for b=10; all > 0).
4. Thin monomials are concentrated near `E_2^b`; the tightest ones
   are `E_2^b (=1)`, `E_1 E_2^{b-1}` (order b), and `E_2^{b-2} E_3`
   (grows quadratically in b). No sign of failure through b = 12.
