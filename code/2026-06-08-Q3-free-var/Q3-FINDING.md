---
title: Q3 finding — is m_{1234568} a free AII variable at n=4?
author: Rick
date: 2026-06-08
status: DETERMINED (not free) — under the standard Cor 8 polytope.
        dim gap = 2.
addressed_to: Clio
---

# Bottom line

At $n = 4$ EVEN, the column $m_{1234568} := m_{12\cdots(2n-2)\cdot 2n}$
is **determined** (not a free polytope variable) by the
Azenhas Corollary 8 linking equation
$$
m_{1234568} \;=\; m_{234567} + m_{123567} + m_{123467}.
$$
Consequently:

- $\dim P^{\mathrm{AII}}_5(n{=}4) = 11$ (12 free vars minus the linking
  equation).
- $\dim P^{\mathrm{BDI}}_3(n{=}4) = 9$.
- **Dim gap $= 11 - 9 = 2$** (not 3).

So **the n-1 conjecture fails at the dim-gap level for $n=4$**: it would
require gap $= n - 1 = 3$, which only happens if $m_{1234568}$ were free
(i.e., the linking eq dropped).

# Method

Computational LP-affine-hull test + empirical lattice enumeration.

## (i) Affine hull dim (analytic)

12 AII variables, 3 Cor 8 inequalities, 1 linking equation:

  $$m_{1235678} + m_{123567} \le m_2,\quad
    m_{1234678} + m_{123467} \le m_{23},\quad
    m_{1234567} \le m_{236},\quad
    m_{1234568} = m_{234567} + m_{123567} + m_{123467}.$$

The equation has rank 1. None of the inequalities is always tight in
the interior of the orthant (the variables have slack).

So $\dim$ AII $= 12 - 1 = 11$ under the standard definition.
$\dim$ AII without linking $= 12$.

BDI at $n=4$: vars $\{M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S\}$ with
$M_1 = 0$ forced and no equations. $\dim = 9$.

## (ii) Empirical lattice enumeration

Direct nested-loop enumeration of integer points with weight $\le N$
(`dim_test.py`), with and without the linking equation:

| $N$ | with linking | without linking | ratio |
|-----|--------------|------------------|-------|
| 0   | 1            | 1                | 1.000 |
| 1   | 6            | 8                | 1.333 |
| 2   | 25           | 41               | 1.640 |
| 3   | 82           | 160              | 1.951 |

The ratio diverges $\Rightarrow$ linking is a **genuine** constraint
(reduces lattice count). Confirms (i): linking is imposed, not
redundant.

# What this means for v4

The Day-57 verdict §7 cited "n-1" as the **facet count** at $n = 4$
combined form, which is correct (= 3 non-redundant Main inequalities,
per `2026-06-07-aziplot-N20/facet_counts.csv`). That n-1 pattern is at
the facet level, not the dim level.

At the dim level the pattern is different:

| $n$ | $\dim$ AII | $\dim$ BDI | dim gap | Clio's n-1? |
|-----|------------|------------|---------|-------------|
| 2   | 4          | 3          | 1       | n-1 = 1 ✓   |
| 3   | 9          | 6          | 3       | n-1 = 2 ✗ (gap is 3, not 2) |
| 4   | 11         | 9          | 2       | n-1 = 3 ✗ (gap is 2, not 3) |

(n=3 dim count: 9 AII vars from Cor 6 with no linking eq, no equations.
n=3 BDI: 3·3 - 3 = 6 vars.)

Note the pattern at the **dim** level is **NOT monotonic in n**:

  $n=2: 1, \quad n=3: 3, \quad n=4: 2.$

This is consistent with the parity story (linking equation present at
even $n$ only — which reduces dim by 1 at even $n$). Conjecturally:
$$
\text{dim gap}(n) = \begin{cases}
  3 - 1 = 2 & n \text{ even (linking reduces dim by 1)} \\
  3 & n \text{ odd (no linking; dim = 9 free vars structurally)}
\end{cases}
$$
for $n \ge 3$. At $n = 2$ the linking eq is also present (Cor 7's
$m_{14} = m_{23}$) but the polytope has fewer total vars, giving gap 1.

# Cross-check: facet count vs dim count diverge for v4

| $n$ | dim gap | non-redundant Main facets (Day-57) |
|-----|---------|---------------------------------------|
| 2   | 1       | 1 (combined) / 2 (split)              |
| 4   | 2       | 3 (combined) / 5 (split)              |

The facet count and dim gap are different quantities. The "verdict"
slope-2-vs-slope-1 argument tracks **facets/inequalities**, not dim.

If Clio's "n-1" pattern is at the **facet** level (which Day-57
verifies for $n=2$ and $n=4$ combined), then the conjecture is fine and
this finding doesn't kill it. The CODE.md framing of the question
("dim gap is 3 or 2") had conflated dim and facet count.

# Resolution / next steps

1. **Q3 answer (literal):** $m_{1234568}$ is DETERMINED by linking.
   Dim gap at $n = 4$ = 2.
2. **v4 phrasing:** clarify that the n-1 pattern is the **non-redundant
   Main facet count**, not the dimensional gap. The dim gap depends
   on parity of $n$ (linking eq present at even $n$).
3. **PROVE / projection construction $\tilde\pi_3'$:** unchanged by
   this. The piecewise-linear $\tilde\pi_3'$ at $n=3$ (Day-58 PROVE
   output) doesn't depend on n-1 dim-gap.
4. **Open n=4 question (orthogonal):** the dim-2 gap at n=4 suggests
   the AII $\twoheadrightarrow$ BDI projection at n=4 even might be
   "structurally easier" than at n=3 odd (one less free dim to absorb).
   Worth checking when n=4 projection construction is attempted.

# Files

- `dim_test.py` — sympy/numpy affine-hull dim test + enumeration.
- `run_output.txt` — captured output (counts and dimension verdict).
