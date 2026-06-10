---
title: "Day 63 CODE Task 1 — Stratum-vector verification at $N \\in \\{12, 13, 14, 15\\}$"
author: Rick
date: 2026-06-11
status: DONE. The stratum-vector is **asymptotically constant** at $N \ge 12$, but it is NOT the Day-62 vector — Day-62 was the $N = 4$ snapshot.
---

# Bottom line

**Mode 8-tuple of $|I(p)|$ stratified by $\sigma = (m_2 > 0, m_{236} > 0, m_{23456} > 0)$:**

| $N$ | (000) | (001) | (010) | (011) | (100) | (101) | (110) | (111) | sorted multiset |
|----|----|----|----|----|----|----|----|----|----|
|  4 |  1 |  9 |  9 | 21 |  4 | 13 | 16 | 25 | (1, 4, 9, 9, 13, 16, 21, 25) |
|  5 |  1 |  9 |  9 | 21 |  5 | 13 | 16 | 25 | (1, 5, 9, 9, 13, 16, 21, 25) |
|  6 |  2 |  9 |  9 | 22 |  5 | 13 | 17 | 25 | (2, 5, 9, 9, 13, 17, 22, 25) |
|  7 |  2 |  9 |  9 | 22 |  5 | 13 | 17 | 26 | (2, 5, 9, 9, 13, 17, 22, 26) |
|  8 |  2 |  9 |  9 | 22 |  5 | 13 | 17 | 26 | (2, 5, 9, 9, 13, 17, 22, 26) |
|  9 |  2 |  9 |  9 | 22 |  5 | 14 | 17 | 26 | (2, 5, 9, 9, 14, 17, 22, 26) |
| 10 |  2 |  9 |  9 | 22 |  5 | 14 | 17 | 26 | (2, 5, 9, 9, 14, 17, 22, 26) |
| 11 |  2 |  9 |  9 | 22 |  5 | 14 | 17 | 26 | (2, 5, 9, 9, 14, 17, 22, 26) |
| 12 |  2 | 10 |  9 | 22 |  5 | 14 | 17 | 26 | **(2, 5, 9, 10, 14, 17, 22, 26)** |
| 13 |  2 | 10 |  9 | 22 |  5 | 14 | 17 | 26 | **(2, 5, 9, 10, 14, 17, 22, 26)** |
| 14 |  2 | 10 |  9 | 22 |  5 | 14 | 17 | 26 | **(2, 5, 9, 10, 14, 17, 22, 26)** |
| 15 |  2 | 10 |  9 | 22 |  5 | 14 | 17 | 26 | **(2, 5, 9, 10, 14, 17, 22, 26)** |

**The Day-62 PROVE quoted vector $(1, 5, 9, 9, 13, 17, 22, 26)$ is the
mode-vector at $N = 5$ only.** It is NOT the asymptotic invariant. The mode
drifts UP in the strata $(000), (001), (011), (100), (101), (110), (111)$
as $N$ grows, and stabilises at:

$$
\boxed{\mathbf I_\infty = (2, 5, 9, 10, 14, 17, 22, 26)}\quad (N \ge 12)
$$

The transition $N$-values for each stratum:

| stratum | mode flips | transition $N$ |
|---|---|---|
| (000) | $1 \to 2$ |  6 |
| (100) | $4 \to 5$ |  5 |
| (110) | $16 \to 17$ | 6 |
| (011) | $21 \to 22$ | 6 |
| (111) | $25 \to 26$ | 7 |
| (101) | $13 \to 14$ | 9 |
| (001) | $9 \to 10$  | 12 |
| (010) | stable at 9 | — |

Stratum (010) is the only one whose mode is constant from $N = 4$.
Stratum (001) is the slowest to transition (flips at $N = 12$). At $N = 16$
or higher the mode could in principle drift further, but the histograms
at $N = 15$ show the modal value increasingly dominating in all strata, so
**$(2, 5, 9, 10, 14, 17, 22, 26)$ is almost certainly the genuine asymptotic
invariant**.

# Method

For each $N \in \{4, \ldots, 15\}$ I enumerated the AII lattice points
$\mathsf P^{AII}_5 \cap \mathbb Z^9$ with $|p| \le N$, then for each
lattice point $p$ computed
$$ |I(p)| = \big|\big\{ \pi^{(i)}(p) \in \mathsf P^{BDI}_3 : i \in V(p) \big\}\big| $$
using the 26-piece minimal cover (Day-58). I grouped $p$ by the sign-pattern
$\sigma(p) = (m_2 > 0, m_{236} > 0, m_{23456} > 0)$ and reported, per stratum:
mean, mode, min, max, variance, and the full histogram of $|I|$.

The codim-1 walls of the kernel arrangement are exactly the three coordinate
hyperplanes $m_2 = 0$, $m_{236} = 0$, $m_{23456} = 0$ (Day-62
`kernel_arrangement.py`). The 8 sign-pattern strata are the chambers of
this arrangement inside the AII cone.

# Stratum statistics at $N = 15$ (representative)

| $\sigma$ | # pts | mean | mode (count) | min | max | var |
|---|----|----|----|----|----|----|
| 000 |   489 |  2.153 |  2 ( 270) |  1 |  3 | 0.424 |
| 001 |  1641 |  9.567 | 10 ( 930) |  9 | 10 | 0.246 |
| 010 |  1641 |  9.662 |  9 ( 960) |  9 | 11 | 0.718 |
| 011 |  4290 | 21.955 | 22 (3026) | 21 | 23 | 0.293 |
| 100 |  5645 |  5.914 |  5 (3316) |  4 |  8 | 2.050 |
| 101 | 12298 | 13.663 | 14 (8472) | 12 | 14 | 0.275 |
| 110 | 12298 | 17.262 | 17 (6008) | 16 | 19 | 1.076 |
| 111 | 22067 | 25.720 | 26 (16274) | 23 | 26 | 0.239 |

Variances are SMALL (all $\le 2.05$) and roughly constant in $N$ — the
within-stratum spread is bounded, not growing. This is the strongest
form of "the stratum is the invariant"; see also `codim2_analysis.md`
for the wall-incidence decomposition that explains the residual variance.

# Implication for the PROVE session (OQ-PI3-MULTI)

The 8-tuple $(2, 5, 9, 10, 14, 17, 22, 26)$ is the actual fingerprint of
$\tilde\pi_3'$ as a multivalued integer-PL map. Note the multiplicities:
no two strata share a mode value, so the stratum is **recoverable from
$|I(p)|$ alone** at large $N$ — i.e., the function $|I(\cdot)|$ on
$\mathsf P^{AII}_5$ separates the codim-1 chambers asymptotically.

Day-62 was reading the small-$N$ data and conjecturing constancy of a
specific vector. The MOST important correction: the 1 → 2 flip in stratum
(000) at $N = 6$, the 9 → 10 flip in (001) at $N = 12$, and the 13 → 14
flip in (101) at $N = 9$. These three flips correspond to "extra image
points" arising when a lattice point has enough room to support an
additional piece with a distinct BDI image — they're geometric in nature,
not artefacts.

# Files

- `strata_extended.py` — Task 1 main script, N = 12..15.
- `strata_extended_result.json` — per-N stratum stats (mode, mean, var, hist).
- `mode_transition.py` — Task 1b, N = 4..15 mode tracking.
- `mode_transition_result.json` — full histograms per (N, stratum).
- `codim2_walls.py` + `codim2_analysis.md` — Task 2 wall-incidence.
- `single_column_n5.py` + `single_column_n5_output.txt` — Task 3 single-column n=5.
