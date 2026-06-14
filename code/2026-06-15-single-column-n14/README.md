---
title: "Day 70 CODE Task B — single-column lemma at n=12, 13, 14"
author: Rick
date: 2026-06-15
status: **PASS at all three n.** OQ-PI3-GROWTH branch (a) closed at n ∈ {2,..,14}.
---

# Bottom line

Single-column piece pi^(g)(p) := p[long[1]] * g — feasible at n=12, 13, 14
on all 100 sampled BDI-feasible lattice points × scaling k ∈ [0, 10].

**100/100 PASS at each n.** OQ-PI3-GROWTH branch (a) is now closed at
n ∈ {2, ..., 14}.

# Method

For each n ∈ {12, 13, 14}:
1. Confirm `long[1]` is FREE at level n (does not appear in any Main_i
   inequality or the Cor 8 linking equation).
2. Sample 100 random BDI-feasible lattice points g with total mass ≤ 12.
3. For each g, verify k*g remains BDI-feasible for k ∈ [0, 10] integer.
4. PASS = all 100 samples pass the scaling test.

BDI is a polyhedral cone (all defining inequalities linear, no equations)
so it is closed under nonneg integer scaling. The test exercises the
explicit BDI feasibility predicate as a sanity check.

# Results

| n  | parity | long[1] FREE | pass / 100 | fail / 100 | wall (s) |
|----|--------|--------------|------------|------------|----------|
| 12 | even   | yes          | 100        | 0          | 0.0      |
| 13 | odd    | yes          | 100        | 0          | 0.0      |
| 14 | even   | yes          | 100        | 0          | 0.0      |

# Verdict

OQ-PI3-GROWTH branch (a) is **closed at n ∈ {2, ..., 14}**.

The closed-form structural reason (general n): BDI is a polyhedral cone,
long[1] is unconstrained in the AII polytope (no Main_i mentions it,
no Cor 8 linking eq involves it), and the single-column piece is just
nonneg integer scaling of g — automatically feasible.

# Files

- `run.py` — driver.
- `results.json` — per-n samples and verdict.

— Rick, Day 70 CODE Task B, 2026-06-15
