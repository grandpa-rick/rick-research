---
title: "Day 71 CODE Task A — Conjecture D-pi verification at n=6, 7"
author: Rick
date: 2026-06-16
status: **Registry-internally CONSISTENT, BUT D-pi as a statement about all feasible pieces was REFUTED by PROVE Day-71 (3-clique witness).**
---

# Bottom line — TL;DR

Two sides of the same coin:

1. **Within the Day-70 registry (this task's literal scope):** every
   interior prefix coord `p_i` has a SINGLE routing across all 36
   (n=6) / 44 (n=7) feasible pieces. So D-pi holds *tautologically
   within the incomplete registry*. No falsification here.

2. **Across all BDI-feasible pieces (Day-71 PROVE result):** D-pi is
   REFUTED. The pieces
   `π_α^(i) := base + (α, p_i)` in the S row, `α ∈ {0, 1, 2}`
   are individually feasible and give THREE distinct routings of `p_i`
   (`e_{B_i}`, `e_{B_i} + e_S`, `e_{B_i} + 2 e_S`). They are NOT in
   the Day-70 registry, so the registry was never a *true* minimal
   cover.

**Verdict:** the Day-70 registry is consistent with D-pi internally,
but the conjecture itself is dead. This task's data is a useful
diagnostic — it locates where the registry is incomplete (precisely
the interior i's, where one would have added the α=1, 2 pieces).

# Numbers

## n = 6 (36 registry pieces)

| interior i | # distinct routings | routing                          |
|------------|---------------------|----------------------------------|
| 2          | **1**               | `e_{B_2}`                        |
| 3          | **1**               | `e_{B_3}`                        |
| 4          | **1**               | `e_{B_4}`                        |

Boundary sanity check (not part of D-pi):
- `i = 1` (AXIS, R-double family): 3 distinct routings.
- `i = 5` (= n-1, RIGID): 1 routing.
- `i = 6` (= n,   AXIS, free prefix): 11 distinct routings.

## n = 7 (44 registry pieces)

| interior i | # distinct routings | routing                          |
|------------|---------------------|----------------------------------|
| 2          | **1**               | `e_{B_2}`                        |
| 3          | **1**               | `e_{B_3}`                        |
| 4          | **1**               | `e_{B_4}`                        |
| 5          | **1**               | `e_{B_5}`                        |

Boundary:
- `i = 1` (AXIS): 3 routings.
- `i = 6` (= n-1, RIGID): 1 routing.
- `i = 7` (= n,   AXIS): 13 routings.

# Method

1. Load Day-70 registry JSON at n=6 (`n6_registry.json`, 36 feasible
   pieces) and n=7 (`n7_registry.json`, 44 feasible pieces).
2. For each interior `i`, collect column tuples
   `M[:, idx(prefix[i])]` over every piece in the registry.
3. Count distinct tuples. D-pi predicts 1.

# Caveat: registry vs all-feasible

The minimal-cover registry by construction (Day-70 `general_pieces.py`)
keeps interior `p_i` routing canonical — the R-double family at level
`a` modifies `B_a` and `S` but never `p_i` for interior `i`. So D-pi
holds tautologically within the registry.

The Day-70+ 3-clique refutation work
(`code/2026-06-16-dpi-refutation-verify/`) shows that pieces with
routing `B_i + S` and `B_i + 2*S` are INDIVIDUALLY BDI-feasible at
n=5, 6, 7. These pieces are NOT in the registry. So:

- D-pi in the "registry sense" (this task): **HOLDS at n=6, 7.**
- D-pi in the "all-feasible sense" (3-clique refutation):
  **FAILS** — there are 3 distinct feasible routings of `p_i` for every
  interior `i`.

These are not in tension. The registry is a strict subset of all
feasible pieces. The PROVE session must decide which sense is the one
that matters for the dim-gap theorem.

# Files

- `run.py` — analysis driver
- `results.json` — per-i routing data, including labelled BDI columns

# Verdict

- Registry sense: **CONSISTENT** at n=6, n=7 — Day-70 design is
  internally coherent.
- All-feasible sense: **REFUTED** (PROVE Day-71 3-clique witness;
  see commit `b1643a0`, `code/2026-06-16-dpi-refutation-verify/`).

Day-70 Thm 8.1 (uniform `# AXIS ≤ 3` conditional on D-pi) is FALSIFIED.
v4 §3 needs revision. The pivot has already happened in PROVE.

— Rick, Day 71 CODE Task A, 2026-06-16
