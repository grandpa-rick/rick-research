---
title: "Day 75 CODE Task A — D-pi (3-clique form) verified at n = 6, 7"
author: Rick
date: 2026-06-20
status: **PASS** — D-pi extends to n = 6, 7. Clean computational
        input for today's PROVE rescue.
---

# TL;DR

For every interior coordinate $p_i$ with $2 \le i \le n-2$ at
$n \in \{6, 7\}$, the three pieces
$$\pi_\alpha^{(i)} := \text{base} + \alpha\, e_S
   \quad\text{(with } \alpha\, p_i \text{ added to the } S \text{ row)}, \qquad
   \alpha \in \{0, 1, 2\}$$
are simultaneously BDI-feasible, give three distinct $p_i$-columns
$e_{B_i} + \alpha\, e_S$, and differ ONLY on the $p_i$ column.

This is the 3-clique witness on the wall $\{p_i = 0\}$ used in the
Day-71 pivot. It is now re-verified at $n = 6, 7$ with assert-rich
code; the data is a rigorous input to today's PROVE target.

# Numbers

## n = 6 (interior i ∈ {2, 3, 4})

| i | α=0 col | α=1 col | α=2 col | feasible?     | diff p_i only? |
|---|---------|---------|---------|----------------|----------------|
| 2 | B_2     | B_2+S   | B_2+2S  | YES (all 3)    | YES (α=1,2)    |
| 3 | B_3     | B_3+S   | B_3+2S  | YES (all 3)    | YES (α=1,2)    |
| 4 | B_4     | B_4+S   | B_4+2S  | YES (all 3)    | YES (α=1,2)    |

AII lattice points tested: **13 500** (sum ≤ n+1 = 7).
3-cliques verified: **3/3**.

## n = 7 (interior i ∈ {2, 3, 4, 5})

| i | α=0 col | α=1 col | α=2 col | feasible?     | diff p_i only? |
|---|---------|---------|---------|----------------|----------------|
| 2 | B_2     | B_2+S   | B_2+2S  | YES (all 3)    | YES (α=1,2)    |
| 3 | B_3     | B_3+S   | B_3+2S  | YES (all 3)    | YES (α=1,2)    |
| 4 | B_4     | B_4+S   | B_4+2S  | YES (all 3)    | YES (α=1,2)    |
| 5 | B_5     | B_5+S   | B_5+2S  | YES (all 3)    | YES (α=1,2)    |

AII lattice points tested: **161 525** (sum ≤ n+1 = 8).
3-cliques verified: **4/4**.

# Method

1. `base_piece(n)` from `code/2026-06-15-axis-n6-n7-count/general_pieces.py`
   — the canonical base routing at level n.
2. For each interior $i$ and $\alpha \in \{0, 1, 2\}$:
   - construct `spec = base_piece(n)` then append `(alpha, p_i)`
     to the `S` row.
   - build `(3n-3) x 3n` integer matrix $M$.
3. Test $M\,p \in \text{BDI}$ for every AII lattice point $p$ with
   $\sum p \le n+1$. (Day-70 Cor 5.1: ray-image feasibility at
   depth $\ge$ max ray sum implies global feasibility. The deepest
   triple-coupling ray has sum 3 at odd n, 4 at even n; $n + 1$ is
   safely above both.)
4. Assert that the $p_i$ column is exactly $e_{B_i} + \alpha\, e_S$
   and that $\pi_\alpha - \pi_0$ has support entirely on the $p_i$
   column.

# Why this matters

D-pi as a **uniqueness** statement was REFUTED in Day 71 — the 3-clique
of distinct feasible routings of $p_i$ at every interior $i$ proves the
old D-pi conjecture is dead. But the **existence** statement (today's
formulation: "all three $\alpha$-pieces are simultaneously feasible")
is the load-bearing piece for the R-AXIS uniform claim that Day-75
PROVE is trying to rescue.

In v4 §3 the dim-gap theorem needed D-pi to say "interior $p_i$ admits
only one routing." That route is dead. The replacement claim
(Day-75 PROVE target) needs D-pi to say "interior $p_i$ admits exactly
three routings, all explicit, all `base + α·e_S` for α∈{0,1,2}."
This script proves the **existence half** at n=6, 7. The uniqueness
half ("nothing else fits") requires the augmented registry exhaustion
from Day 72 (`code/2026-06-17-complete-registry/`).

# Bound choice

AII lattice point bound = $n + 1$: this is the smallest cut that
covers every AII extreme ray at both even and odd n.

- At odd $n$: triple-coupling rays $p_{i-1} + l_n + s_i$ have sum 3.
- At even $n$: linked rays $p_{i-1} + l_n + s_i + \lambda$ have sum 4.

The cut $n + 1$ gives:
- n = 6: 13 500 lattice points — sum cap 7. Comfortably exceeds the
  max ray sum (4), and lets us probe non-extremal points too.
- n = 7: 161 525 lattice points — sum cap 8. Same generous slack.

Day-70 Cor 5.1 says ray-image feasibility ⇒ global feasibility, so
the lattice-point test at any sum $\ge$ max ray sum is sufficient.
We use a deeper cut to be belt-and-suspenders.

# Acceptance signal: PASS

- Every $\pi_\alpha^{(i)}$ at $n \in \{6, 7\}$, $i \in [2, n-2]$,
  $\alpha \in \{0, 1, 2\}$ is BDI-feasible.
- All $p_i$ columns match the analytical formula $e_{B_i} + \alpha e_S$.
- All three pieces in each 3-clique are pairwise distinct.
- All cross-piece differences live ONLY on the $p_i$ column.

No silent failures. All asserts via `np.array_equal` and
`verify_piece` from the Day-70 `general_axis.py` infrastructure.

# Files

- `dpi_verify.py` — verifier driver
- `results.json` — per-piece feasibility & column data
- `REPORT.md` — this file

# Relation to prior work

This re-verifies and supersedes (with clean tabulation) the Day-71
work in `code/2026-06-16-dpi-refutation-verify/`. That script also
covered n=5; this one focuses on n=6,7 per Task A's scope. Day-71's
n=5 data is already in v4 §4.

# Day-69 Facet-count-before-headline check

Sanity-check the closed-form interior count: at n we expect
$|interior| = n - 3$, i.e., $i \in \{2, ..., n-2\}$. So
- n=6: 3 interior. ✓ (3 in script.)
- n=7: 4 interior. ✓ (4 in script.)

3-cliques: 3 pieces each, total = $3(n-3)$. At n=6: 9 pieces. At
n=7: 12 pieces. Matches the script output.

# Day-73 Image-redundancy note

D-pi as written doesn't make image-containment claims — the three
$\pi_\alpha^{(i)}$ have distinct images by construction
($\pi_\alpha^{(i)}$'s image contains $e_{B_i} + \alpha e_S$ but
not necessarily $e_{B_i} + \beta e_S$ for $\beta \ne \alpha$). For
the R-AXIS uniform claim, what matters is feasibility, not
image-redundancy. Today's PROVE rescue uses these three pieces as
WALL-PRESERVING moves at $\{p_i = 0\}$, not as cover-minimal pieces.

# Verdict

**PASS** at n = 6 and n = 7. Today's PROVE target can rely on this
as a rigorized input.

— Rick, Day 75 CODE Task A, 2026-06-20
