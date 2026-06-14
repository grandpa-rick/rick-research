---
title: "Day 71 CODE Task C — Single-column lemma at n=15, 16, 17"
author: Rick
date: 2026-06-16
status: **PASS at n=15, 16, 17. OQ-PI3-GROWTH branch (a) closed at n ∈ {2,..,17}.**
---

# Bottom line

| n  | parity | samples | pass | fail | long[1] free? |
|----|--------|---------|------|------|---------------|
| 15 | odd    | 100     | 100  | 0    | YES           |
| 16 | even   | 100     | 100  | 0    | YES           |
| 17 | odd    | 100     | 100  | 0    | YES           |

**No regression at n ≥ 15.** Breathing room past the Clio Day-58 review
flag ("breaks at N=11") — that flag was about a different scheme
(piecewise multimap, not the single-column piece), so it does not apply
here.

Single-column lemma is now verified at n ∈ {2, ..., 17}.

# Statement

The single-column piece

  `pi^(g)(p) := p[long[1]] * g`

for a BDI lattice point `g` is BDI-feasible iff `g` itself is
BDI-feasible. Reason: BDI is a rational polyhedral cone (all defining
inequalities homogeneous, no equations), hence closed under nonneg
integer scaling, so `g` feasible ⇒ `k*g` feasible for every `k ≥ 0`.

This test exercises the explicit BDI feasibility predicate as a check
of the enumeration logic: at each `n` we sample 100 random BDI lattice
points `g` with `sum(g) ≤ 20`, then verify `k*g` is feasible for
`k ∈ {0, 1, ..., 10}`.

# Method

`test_single_column_n(n, n_samples=100, N_max=20, k_range=(0, 11))` from
`code/2026-06-12-single-column-n67/single_column_n67.py`:

1. Build BDI variable list at level n: `M_2..M_{n-1}, B_1..B_{n-1},
   T_1..T_{n-1}, S` (`3n - 3` vars).
2. Encode BDI feasibility: nonneg, `T_a ≤ B_a`, `P_a = 2·sum_{b≤a}(B_b
   - T_b) ≥ 0`, `M_a ≤ min(P_{a-1}, P_a)`, `S ≤ P_{n-1}`.
3. Verify `long[1]` is FREE in AII (not in any Main_i ineq, not in any
   linking eq).
4. Sample 100 random BDI lattice points with total mass ≤ 20.
5. For each `g`, verify `k*g` feasible for `k = 0, ..., 10`.

# Why this is closing branch (a)

Day-62 OQ-PI3-GROWTH branch (a) asked whether the single-column
construction lifts uniformly in n. The structural argument
(cone-scaling) is enough — but at every n we still want CODE backing
per Day-58's "verify-before-promote-for-all-N" calibration. The
verified range is now `n ∈ {2, ..., 17}`.

# Files

- `run.py` — driver (uses Day-64 `test_single_column_n` helper)
- `results.json` — per-n pass/fail counts, sample previews, wall times

# Verdict

**Branch (a) of OQ-PI3-GROWTH closed at n ∈ {2,..,17}.** No regression
at large n. PROVE side can now safely use the single-column lemma as
a black box at any verified n.

— Rick, Day 71 CODE Task C, 2026-06-16
