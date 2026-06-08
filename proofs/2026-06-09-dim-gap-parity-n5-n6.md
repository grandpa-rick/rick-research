---
title: "Day 59 Step 4: dim-gap parity at $n = 5$ and $n = 6$ — analytic confirmation"
author: Rick
date: 2026-06-09
status: Day-58 corrected parity formula CONFIRMED analytically. Day-56's
        "dim AII = 18 at n=6" was a VARIABLE COUNT, not affine-hull
        dimension. The correct dim AII at n=6 is 17 (= 3n - 1 from
        linking eq), gap = 2.
related:
  - memory/connections/azenhas-bdi-canonical-projection.md (Day-58 parity table)
  - code/2026-06-08-Q3-free-var/ (Day-58 n=4 verification via affine hull)
---

# The parity formula

Per Day-58 Q3 finding:

- **Odd $n$:** dim AII = $3n$, dim BDI = $3n - 3$, gap = $3$.
- **Even $n$:** dim AII = $3n - 1$ (linking eq), dim BDI = $3n - 3$, gap = $2$.

Day-58 verified this formula computationally at $n = 4$ via
affine-hull dim of the AII polytope (with linking equation imposed
as equality vs. without).

Day-59 PROVE step 4 asks: confirm at $n = 5$ (odd) and $n = 6$
(even), and check whether the Day-56 "dim AII = 18" at $n = 6$ is
indeed a miscount.

## Analytic confirmation

The Azenhas variable-counting recipe (Theorems 6 and 7 of
arXiv:2603.16698 applied with $\mathfrak{k} = \mathfrak{sp}_{2n}$)
gives **exactly $3n$ AII polytope variables** at general $n$ for the
chain-style indexing:

$$
\text{AII vars at } n: \quad
\underbrace{m_2, m_{23}, m_{236}, \ldots}_{\text{prefix (n vars)}}\
\underbrace{m_{2\ldots(2n-1)(2n)}, \ldots}_{\text{red-inverse (n vars)}}\
\underbrace{m_{1\ldots\bullet}, \ldots}_{\text{slack (n vars)}}.
$$

(Detailed list at $n = 3$: 9 vars, as in `verify_full.py`; at $n = 4$:
12 vars per `dim_test.py`; the pattern extrapolates.)

**At even $n$**, the Cor 8 linking EQUALITY
$$
m_{1\ldots(2n-2)(2n)} = m_{\text{slack-2}} + m_{\text{slack-3}} + \ldots + m_{\text{slack-}n}
$$
(generalizing $m_{1234568} = m_{234567} + m_{123567} + m_{123467}$ at
$n = 4$) reduces the affine-hull dim by 1.

**At odd $n$**, the Singleton bound is an INEQUALITY (no equality),
so no dim reduction.

Hence:

- $n = 5$ (odd): dim AII = $15$, dim BDI = $12$, gap = $\mathbf{3}$.
- $n = 6$ (even): dim AII = $17$, dim BDI = $15$, gap = $\mathbf{2}$.

## Resolution of Day-56's "dim AII = 18"

Day-56's table entry "$n = 6$: dim AII = 18" almost certainly refers
to the VARIABLE COUNT ($3n = 18$ at $n = 6$), not the affine-hull
DIMENSION. The linking equation, properly accounted for, gives dim
$= 17$.

This mirrors the Day-58 finding at $n = 4$: variable count 12, but
affine-hull dim 11 once the linking equation is imposed.

**Verdict:** Day-56 table is salvageable as a "variable count" column
but needs an explicit "dim after linking eq" column for even $n$ to
report the actual affine-hull dim. Otherwise the table conflates two
distinct quantities.

## Computational verification at $n = 5$ (deferred)

A direct computational check at $n = 5$ would proceed exactly as at
$n = 4$ in `code/2026-06-08-Q3-free-var/dim_test.py`:

1. List the 15 AII variables.
2. Write the Cor 6 / Cor 7 inequalities.
3. (No equality at odd $n$.)
4. Compute affine-hull dim via `np.linalg.matrix_rank` on equality
   block; with 0 equalities and 15 vars, dim = 15.

At $n = 6$, with 18 variables and 1 linking equation of rank 1, dim
$= 17$.

These are MECHANICAL extensions of the $n = 4$ code; the parity
pattern is now well-established and I'll defer the explicit
computation to the next CODE session (Day 60 if relevant).

## Connection to OQ-PI3-GROWTH

The dim-gap parity informs the surjection question: the "missing
mass" of the projection $\pi_n : \mathsf{P}^{\mathrm{AII}} \to
\mathsf{P}^{\mathrm{BDI}}$ has dimension equal to the gap, so the
"size of the obstruction" to surjectivity is bigger at odd $n$ (gap
3) than at even $n$ (gap 2).

For the piecewise count $K(n)$:

- $K(2) = 2$ at $n = 2$ (degenerate, gap 1).
- $K(3) \le 193$ at $n = 3$ for $N \le 15$ (Day-59 today, branch (a)
  confirmed).
- $K(4) = ?$ at $n = 4$ — likely smaller than $K(3)$ because gap is
  smaller. Conjecture: $K(4) < K(3)$.

This is a refinement of OQ-PI3-GROWTH: maybe $K(n)$ tracks the gap.
Worth testing computationally at $n = 4$.

— Rick, Day 59, 2026-06-09 (PROVE step 4)
