---
title: "Day 67 CODE Task 3 — single-column lemma extended to n=8"
author: Rick
date: 2026-06-12
status: 100/100 pass. OQ-PI3-GROWTH branch (a) closed for n ∈ {2,...,8}.
---

# Bottom line

100/100 sampled BDI-feasible points $g$ at $n=8$ remain feasible under
scaling $k \cdot g$ for $k \in \{0, 1, \ldots, 10\}$, with `long[1]`
verified free (not in any Main_i inequality, not in any linking
equation) at $n=8$ (even, so it does have Cor 8 linking — but `long[1]`
itself doesn't appear in the linking equation).

# Verification

- 100 random BDI-feasible lattice points $g$ at $n=8$, $\sum g \le 10$.
- For each, verified $k g$ is BDI-feasible for $k = 0, 1, \ldots, 10$.
- Pass rate: **100/100** (matches n=2,...,7 results).

# Engine-role check (`long[1]` free at n=8)

- `long[1]` is **not in any Main_i** inequality (so unbounded above on the
  AII polytope, in the sense relevant for piece $\pi^{(g)}$).
- `long[1]` is **not in the Cor 8 linking equation** (the linking only
  uses `short[i]` and `linkLHS`).
- Hence `long[1]` is a FREE AII variable at $n=8$ — the single-column
  piece $\pi^{(g)}(p) := p[\text{long}[1]] \cdot g$ is well-defined.

# Status

- ✓ OQ-PI3-GROWTH branch (a) closed at $n \in \{2, 3, 4, 5, 6, 7, 8\}$.
- Mechanism: BDI is a rational polyhedral cone (all defining
  inequalities linear, no equations), so closed under nonneg integer
  scaling. $g$ feasible $\Rightarrow$ $kg$ feasible for $k \ge 0$.
- The empirical test exercises the explicit BDI feasibility predicate
  at n=8, confirming the structural argument matches the code.

# Files

- `single_column_n8.py` — driver script (reuses n=6,7 machinery).
- `results.json` — full sample data and pass/fail counts.

— Rick, Day 67 CODE, 2026-06-12
