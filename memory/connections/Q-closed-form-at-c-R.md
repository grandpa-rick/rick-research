---
name: Q_{2R}(a, b, R) closed form — Day 107 breakthrough
description: The trivariate polynomial Q_{2R}(a, b, c) at the Weyl-wall specialization c = R factors as (-1)^R (2R)! · A_R(a) · B_R(b) where A_R and B_R are R-term products of consecutive integers. This gives H5′′ as an immediate corollary and generalizes the Q value to arbitrary (a, b).
type: project
---

# Q_{2R}(a, b, R) closed form

## Statement (verified R = 2, 3, 4, 5 as full polynomial identity)

$$Q_{2R}(a, b, R) = (-1)^R \cdot (2R)! \cdot A_R(a) \cdot B_R(b)$$

where

- $A_R(a) = (a+2)(a+1)a(a-1)\cdots(a-R+3) = \prod_{i=0}^{R-1}(a - i + 2)$
- $B_R(b) = (b+1) \cdot b(b-1)(b-2)\cdots(b-R+2) = (b+1)\prod_{i=0}^{R-2}(b - i)$

**Why:** At $(a, b, c) = (R-2, R, R)$, the M_j determinant argument
$x = (a+2, b+1, c) = (R, R+1, R)$ has two coincident coordinates ($x_1 = x_3 = R$).
This is a Weyl chamber wall for SL_3. The wall specialization reduces the
3-variable M_j determinant to a product of 2 SL_2-like structures — one in
the a-direction (A_R) and one in the b-direction (B_R). The outer factor
$(2R)!$ comes from the c! normalization in the H_c template at c = R, and
$(-1)^R$ is the Weyl antisymmetry sign.

**How to apply:**
- To compute Q_{2R}(a, b, R) at ANY (a, b), use the formula directly.
- To recover H5′′: evaluate at (a, b) = (R-2, R): A_R(R-2) = R!, B_R(R) = (R+1)!.
- To prove uniform-in-R H5′′: prove the closed form (★).
- Interpretation of the vanishing zeros in (a, b): they correspond to
  "out-of-Weyl-chamber" specializations where x_1 or x_2 lies in {0, 1, ..., R-1}.

## Why this matters

1. **H5′′ becomes a corollary.** The whole H5 → H5′′ story reduces to (★).
2. **Stronger structural claim.** The closed form determines Q(a, b, R) at
   ALL (a, b), not just the target (R-2, R).
3. **New evaluation formula.** (★) is (as of Day 107) a genuinely new
   evaluation formula for a 3×3 Jacobi-Trudi determinant at a Weyl wall.
   Potentially publishable independently.
4. **Reveals the geometric mechanism.** The A_R · B_R structure is not
   accidental — it reflects the SL_3 → SL_2 × SL_2 wall reduction directly.

## Verification (Day 107 empirical)

| R | Method | Result |
|---|--------|--------|
| 2 | Full trivariate poly fit, 22 c-samples | EXACT match, all monomials |
| 3 | Full trivariate poly fit, 20 c-samples | EXACT match, all monomials |
| 4 | Full trivariate poly fit, 22 c-samples | EXACT match, all monomials |
| 5 | Full trivariate poly fit, 25 c-samples | EXACT match, all 27 monomials |
| 6 | Full trivariate poly fit, background job | (in progress at Day 107 close) |

**Explicit forms:**

- R = 2: Q_4(a, b, 2) = 24 (a+1)(a+2) · b(b+1)
- R = 3: Q_6(a, b, 3) = -720 · a(a+1)(a+2) · (b+1)b(b-1)
- R = 4: Q_8(a, b, 4) = 40320 · (a-1)a(a+1)(a+2) · (b+1)b(b-1)(b-2)
- R = 5: Q_{10}(a, b, 5) = -3628800 · (a-2)(a-1)a(a+1)(a+2) · (b+1)b(b-1)(b-2)(b-3)

## Master divisibility (♣) — the auxiliary identity

$$Q_{2R}(a, b, c) - Q_{2R}(a, b, R) \cdot \frac{c^{(R)}}{R!} \in (c-R)^2 (c-R-1) \cdot \mathbb{Q}[a, b, c]$$

This says Q agrees with its "c^{(R)}/R! projection" of the value at c = R
to order 2 at c = R and to order 1 at c = R+1. Equivalently: for each
(a, b)-monomial in Q, the c-polynomial coefficient satisfies
G'(R) = H_R · G(R) and G(R+1) = (R+1) · G(R), where H_R is the R-th harmonic.

Both (♣) and (★) verified R = 2..5. Combined they give H5′′.

## Path to a uniform proof of (★)

Both LHS and RHS are polynomials of bivariate degree ≤ 2R with total degree
R in each variable. It suffices to:

1. Show $Q_{2R}(a, b, R) = 0$ at $a \in \{-2, -1, 0, ..., R-3\}$ (R values).
2. Show $Q_{2R}(a, b, R) = 0$ at $b \in \{-1, 0, 1, ..., R-2\}$ (R values).
3. Determine the leading $a^R b^R$ coefficient of $Q_{2R}(a, b, R)$: it equals
   $(-1)^R (2R)!$.

Then $Q_{2R}(a, b, R) = c \cdot A_R(a) B_R(b)$ (from divisibility argument),
and $c = (-1)^R (2R)!$ from the leading coefficient.

**Vanishing conditions to prove:**

These say Q vanishes at "out-of-Weyl-chamber" specializations. Structurally,
at $a = -2$, $x_1 = 0$, and the first row of the Jacobi-Trudi becomes
$(1, 0, 0)$ (only the zero-power surviving), giving a highly degenerate
determinant that combined with the c = R wall reduces to 0.

Rigor: expand the polynomial extension of Q via the M_j formula and track
the vanishing.

## References

- `proofs/2026-08-14-H5doubleprime-proof-day107.md` — main writeup (Day 107).
- `code/2026-08-14-h5doubleprime-symbolic.py` — Route C.
- `code/2026-07-10-hk-three-var-fit.py` — M_j pipeline.
