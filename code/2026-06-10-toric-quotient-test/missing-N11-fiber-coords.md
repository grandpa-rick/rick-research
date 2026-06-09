---
title: "Day 60 Task 4 — Missing N=11 BDI points with fiber-coord analysis"
author: Rick
date: 2026-06-10
status: 7 missing points (down from 15 in earlier registry).
        Characterized by $M_2 = P_a$ boundary + high S + varied T-ratios.
---

# The 7 missing points

Under the 94-piece registry `ALL_PI` (from `verify_full_v9.py`), at $N
= 11$, $7$ BDI lattice points are not covered:

| # | $M_2$ | $B_1$ | $T_1$ | $B_2$ | $T_2$ | $S$ | $P_1$ | $P_2$ | $T_1{:}T_2$ |
|---|-------|-------|-------|-------|-------|-----|-------|-------|-------------|
| 1 | 4 | 2 | 0 | 2 | 2 | 1 | 4 | 4 | 0:2 |
| 2 | 3 | 3 | 1 | 0 | 0 | 4 | 4 | 4 | 1:0 |
| 3 | 4 | 3 | 1 | 0 | 0 | 3 | 4 | 4 | 1:0 |
| 4 | 2 | 2 | 1 | 3 | 3 | 0 | 2 | 2 | 1:3 |
| 5 | 4 | 2 | 0 | 1 | 1 | 3 | 4 | 4 | 0:1 |
| 6 | 3 | 3 | 0 | 0 | 0 | 5 | 6 | 6 | 0:0 |
| 7 | 4 | 3 | 1 | 1 | 1 | 1 | 4 | 4 | 1:1 |

# Structural pattern

| Feature | Count / 7 |
|---|---|
| $M_2 = P_1 = P_2$ saturated | 6 |
| $S = P_2$ (S at max) | 1 |
| Both $M_2$ and $S$ positive | 7 |
| $P_1 = P_2$ ($B_2 = T_2$) | 5 |
| $T_2 = 0$ | 3 |
| $T_1 = 0$ | 3 |
| $T_1 = T_2 > 0$ | 1 |

**Distillation.** Every missing point has $M_2$ AND $S$ simultaneously
positive, with $M_2$ at the upper boundary ($M_2 = P_1 = P_2$) in
nearly all cases. The 6th point has $S = 5, P_2 = 6$ instead — the
"max-S" version of the same pattern.

# Each missing point's nearest hit

For each missing $g$, the nearest hit (L1 distance 1) of the registry
is listed below. Differences are mostly in $\Delta M_2 = -1$,
$\Delta T_a = \pm 1$, $\Delta S = \pm 1$, or $\Delta B_a = +1$ — that
is, small shifts in **boundary-saturating** coordinates.

```
g #1 (4, 2, 0, 2, 2, 1) — nearest hits: (3,2,0,2,2,1), (4,2,0,2,1,1),
                                          (4,2,0,2,2,0), (4,2,0,2,2,2),
                                          (4,2,0,3,2,1).
g #2 (3, 3, 1, 0, 0, 4) — nearest hits: (2,3,1,0,0,4), (3,3,0,0,0,4),
                                          (3,3,1,0,0,3), (3,3,1,1,0,4),
                                          (3,4,1,0,0,4).
g #3 (4, 3, 1, 0, 0, 3) — nearest hits: (3,3,1,0,0,3), (4,3,0,0,0,3),
                                          (4,3,1,0,0,2), (4,3,1,0,0,4),
                                          (4,3,1,1,0,3).
g #4 (2, 2, 1, 3, 3, 0) — nearest hits: (1,2,1,3,3,0), (2,2,0,3,3,0),
                                          (2,2,1,3,2,0), (2,2,1,3,3,1),
                                          (2,3,1,3,3,0).
g #5 (4, 2, 0, 1, 1, 3) — nearest hits: (3,2,0,1,1,3), (4,2,0,1,0,3),
                                          (4,2,0,1,1,2), (4,2,0,1,1,4),
                                          (4,2,0,2,1,3).
g #6 (3, 3, 0, 0, 0, 5) — nearest hits: (2,3,0,0,0,5), (3,3,0,0,0,4),
                                          (3,3,0,0,0,6), (3,3,0,1,0,5),
                                          (3,4,0,0,0,5).
g #7 (4, 3, 1, 1, 1, 1) — nearest hits: (3,3,1,1,1,1), (4,3,0,1,1,1),
                                          (4,3,1,1,0,1), (4,3,1,1,1,0),
                                          (4,3,1,1,1,2).
```

# What this tells us

1. **Boundary cross-talk.** All 7 missing points are at the
   $M_2 = P_a$ boundary AND have $S > 0$. The 94-piece registry's
   "$M_2$ sources" and "$S$ sources" are essentially independent: each
   piece sources $M_2$ from a specific combination of AII vars (e.g.,
   $m_{12356}$, $2 m_{23456}$, etc.) and $S$ from another combo (e.g.,
   $m_{12346} + 2 m_{1234}$). At extreme $M_2$ saturation, no piece
   can simultaneously max out both.

2. **The "leak" is small but structural.** Going from 15 (earlier
   registry) to 7 (current) missing points suggests the registry can
   be expanded further. But the OBSTRUCTION pattern is the same:
   high-$M_2$ + high-$S$ + non-trivial $T$ at boundary.

3. **Hint at fractional-linear cure.** A piece of the form
   $S = m_{12346} + m_{1234} + \alpha m_{23456}$ with $\alpha$ chosen
   based on $T_1, T_2$ (i.e., $\alpha$ depending on the BDI target)
   could absorb the missing family. This is the "fractional-linear PL"
   direction flagged by Day-60 PROVE Step 4.

# Fiber-coord requirement for each missing point

For each missing $g$, the required fiber coords $(T_1, T_2)$ in the
implicit "BDI torus orbit" are:

```
#1: T_1 = 0, T_2 = 2.  At g #1, |g|−B_1−B_2 = 11−2−2 = 7 = M_2+T_2+S = 4+2+1 ✓.
#2: T_1 = 1, T_2 = 0.  P_1 = 4 saturates M_2 = 3, P_2 = 4 saturates S = 4? No, S=4 = P_2 ✓ (S at max).
#3: T_1 = 1, T_2 = 0.  P_1 = 4 = M_2 - 0 = 4 ✓ ($M_2$ saturated).
#4: T_1 = 1, T_2 = 3.  P_1 = 2 = M_2 ✓ (saturated).
#5: T_1 = 0, T_2 = 1.  P_1 = 4 = M_2 ✓ (saturated).
#6: T_1 = 0, T_2 = 0.  S = 5 < P_2 = 6, so S NOT at max.
#7: T_1 = 1, T_2 = 1.  P_1 = 4 = M_2 ✓.
```

Each missing point's $(T_1, T_2)$ is a specific rational ratio that
*could* in principle be hit by a piece if the piece's $T_1, T_2$
expressions matched. The varied ratios (0:2, 1:0, 1:3, 0:1, 1:1)
suggest no single "missing piece" would fix all 7.

# Recommendation

To close the 7-point N=11 leak with the existing piece structure,
**we'd need 7 new pieces** — one per missing point — each tuned to a
specific $(M_2, T_1, T_2, S)$ saturation configuration. That's not a
*structural* fix; it's whack-a-mole.

A structural fix requires either:

(a) Fractional-linear pieces (per Day-60 PROVE Step 4 (a)). E.g., a
    piece where $M_2 = m_{12356} \cdot \mathbf{1}[T_1 > 0] +
    m_{23456}$ — switching $M_2$ source based on $T_1$.
(b) Allow the "T" coords to be fractional (rational rather than
    integer) at the AII level, with integrality imposed only at the
    BDI level.
(c) Replace the registry with a tropical / stack / fan-based object
    where boundary saturation is encoded combinatorially.

— Rick, Day 60 (2026-06-10)
