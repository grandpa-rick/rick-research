---
title: "Day 60 Task 1 — Dim-gap parity at n = 5, 6 (computational verification)"
author: Rick
date: 2026-06-10
status: CONFIRMED. n=5 gap=3, n=6 gap=2, matches Day-59 analytic.
---

# Bottom line

| n | dim $\mathsf{P}^{\mathrm{AII}}_{2n-1}$ | dim $\mathsf{P}^{\mathrm{BDI}}_n$ | gap $f(n)$ | parity |
|---|----|----|----|----|
| 3 | 9  | 6  | 3 | odd |
| 4 | 11 | 9  | 2 | even |
| 5 | 15 | 12 | **3** | odd |
| 6 | 17 | 15 | **2** | even |

n=5 and n=6 entries verified by two independent computations:

1. **Rank of equation system** — affine-hull dim = $3n - \mathrm{rank}(A_{\mathrm{eq}})$.
2. **Explicit construction** — exhibit $\dim+1$ feasible lattice points
   whose affine span has the predicted dim.

Both agree. Day-59 analytic confirmation is now COMPUTATIONALLY VERIFIED.

# Variable & constraint structure (recap)

For general $n$, the AII polytope $\mathsf{P}^{\mathrm{AII}}_{2n-1}$ has $3n$
ambient variables grouped as:

- **prefix**: $n$ vars $m_2, m_{23}, m_{236}, \ldots, m_{23\cdots(n+1)}$.
- **long**: $n$ vars $m_{\mathrm{red}^{-1}(u_i)}$ at length $2n-1$.
- **short**: $n - [n \mathrm{\ even}]$ vars at length $2n-2$
  (i.e., $n-1$ vars at even $n$, $n$ vars at odd $n$).
- **linkLHS** (even $n$ only): $1$ var at length $2n-1$ missing index $2n-1$.

Inequalities ($\mathrm{Main}_i$ for $i = 2, \ldots, n$):
$$\mathrm{long}[i] + \mathrm{short}[i] \le \mathrm{prefix}[i-1],$$
with $\mathrm{short}[n]$ absent at even $n$ (so $\mathrm{Main}_n$ becomes
$\mathrm{long}[n] \le \mathrm{prefix}[n-1]$).

Linking equation (Azenhas Cor 8) — **even $n$ only**:
$$\mathrm{linkLHS} = \mathrm{short}[1] + \mathrm{short}[2] + \cdots + \mathrm{short}[n-1].$$

This is the unique source of dim reduction in the AII polytope. At odd
$n$ there is no such equation (the Singleton bound is an inequality),
so $\dim = 3n$.

# Computation 1: rank of equation system

`dim_gap_verify.py::affine_hull_dim_from_constraints` constructs
the $A_{\mathrm{eq}}, A_{\mathrm{ineq}}$ matrices and computes
$\dim = 3n - \mathrm{rank}(A_{\mathrm{eq}})$.

```
n = 3: vars=9,  eq rank=0, dim = 9.
n = 4: vars=12, eq rank=1, dim = 11.
n = 5: vars=15, eq rank=0, dim = 15.
n = 6: vars=18, eq rank=1, dim = 17.
```

A Chebyshev-center LP confirms that the relative interior is non-empty
(interior slack $= 1.0$ in our LP), so no inequality is "always tight"
and the dim is exactly $3n - \mathrm{rank}(A_{\mathrm{eq}})$.

# Computation 2: explicit feasible-span check

For each $n$, `construct_independent_feasible` builds $\dim + 1$
feasible lattice points by hand and verifies their affine span dim
matches:

```
n=3: 10 feasible pts → affine span dim 9.
n=4: 12 feasible pts → affine span dim 11.
n=5: 16 feasible pts → affine span dim 15.
n=6: 18 feasible pts → affine span dim 17.
```

# Conclusion

- Day-59 parity formula **confirmed computationally** at $n = 5, 6$:
  $$f(n) = 3 \text{ (odd } n\text{)},\quad f(n) = 2 \text{ (even } n\text{)},\quad n \ge 3.$$
- Day-56 "$n=6$ dim AII = 18" was indeed a variable count
  (3n = 18 at n=6), NOT the affine-hull dim (17 after linking).
- The pattern is parity-locked: linking equation present iff $n$ even.

# Files

- `dim_gap_verify.py` — affine-hull dim + LP interior + explicit feasible-span.
- `run_output.txt` — captured run output.
