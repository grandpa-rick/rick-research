---
title: "Day 60 Task 2 — f(n) closed form for the AII/BDI dim gap"
author: Rick
date: 2026-06-10
status: f(n) = 3 - [n even] for n ≥ 3. Verified at n = 3..7.
---

# The table

| n | $\dim \mathsf{P}^{\mathrm{AII}}_{2n-1}$ | $\dim \mathsf{P}^{\mathrm{BDI}}_n$ | $f(n)$ | parity |
|---|----|----|----|------|
| 3 | 9  | 6  | **3** | odd  |
| 4 | 11 | 9  | **2** | even |
| 5 | 15 | 12 | **3** | odd  |
| 6 | 17 | 15 | **2** | even |
| 7 | 21 | 18 | **3** | odd  |

# Closed form

$$\boxed{f(n) = 3 - [n \text{ is even}]}\qquad (n \ge 3).$$

Equivalently:

- $\dim \mathsf{P}^{\mathrm{AII}}_{2n-1} = 3n - [n \text{ is even}]$.
- $\dim \mathsf{P}^{\mathrm{BDI}}_n = 3n - 3$.

# Why the parity

Decomposition of the gap:

$$f(n) = \underbrace{(3n)}_{\text{free AII vars}} - \underbrace{(3n - 3)}_{\dim \text{BDI}} - \underbrace{[n \text{ even}]}_{\text{rank of linking eq}}.$$

| n | free vars AII | dim BDI | rank linking | $f(n)$ |
|---|---------------|---------|--------------|--------|
| 3 | 9  | 6  | 0 | 3 |
| 4 | 12 | 9  | 1 | 2 |
| 5 | 15 | 12 | 0 | 3 |
| 6 | 18 | 15 | 1 | 2 |
| 7 | 21 | 18 | 0 | 3 |

The "free AII vars - dim BDI" piece contributes a constant 3 (the
"raw" gap from variable counting). The Azenhas linking equation
(Cor 8) is present iff $n$ is even, contributing $-1$ in the even
case.

# What's notable

- $f(n)$ is **bounded** (in fact $\in \{2, 3\}$) — the gap doesn't
  grow with $n$. Importantly, $f(n) \le 3$, so the AII polytope is
  always "only a bit bigger" than the BDI image.
- $f(n)$ is **not monotonic in $n$**: $3, 2, 3, 2, 3, \ldots$
- The parity oscillation comes entirely from the Cor 8 linking
  EQUATION (Azenhas), which exists iff $n$ is even because the
  reduced reading word at even $n$ has a particular cancellation
  that doesn't occur at odd $n$.

# Implication for the toric quotient story

If a torus quotient $\mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow
\mathsf{P}^{\mathrm{BDI}}_n$ exists, its torus rank should equal $f(n)$.
So:

- **Odd $n$:** $T = (\mathbb{C}^*)^3$ — a torus of rank 3.
- **Even $n$:** $T = (\mathbb{C}^*)^2$ — a torus of rank 2.

The Day-58 "Clio $n-1$" conjecture (gap = $n-1$) was at the **facet**
level (count of non-redundant Main inequalities), NOT the dim level.
At the dim level the actual pattern is $\{2, 3\}$-periodic.

# Files

- `f_n_table.py` — table generation + closed-form verification.
- `run_output.txt` — captured run output.
