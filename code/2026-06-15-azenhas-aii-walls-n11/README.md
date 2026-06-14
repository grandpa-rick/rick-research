---
title: "Day 70 CODE Task C — AII / BDI facet recheck at n=9, 10, 11"
author: Rick
date: 2026-06-15
status: **Closed forms confirmed at n=9, 10, 11.** Day-69 quasi-poly fit reinforced.
---

# Bottom line

Day-69 fit (from `code/2026-06-14-azenhas-aii-walls/`) proposed the
closed forms

  AII facets = 3n − [n even],   BDI facets = 4n − 5.

Verified at n ∈ {3, 4, 5, 6, 7, 8} in Day 69; this script extends to
**n=9, 10, 11**.

## Confirmed at all three n:

| n  | AII obs | AII pred (3n − [n even]) | OK | BDI obs | BDI pred (4n − 5) | OK |
|----|---------|--------------------------|----|---------|-------------------|----|
| 9  | 27      | 27                       | ✓  | 31      | 31                | ✓  |
| 10 | 29      | 29                       | ✓  | 35      | 35                | ✓  |
| 11 | 33      | 33                       | ✓  | 39      | 39                | ✓  |

## Period-2 finite-difference check (the only valid quasipoly test):

Combining Day 69 (n=3..8) with Day 70 (n=9..11):

- AII series (n=3..11): `[9, 11, 15, 17, 21, 23, 27, 29, 33]`
- BDI series (n=3..11): `[7, 11, 15, 19, 23, 27, 31, 35, 39]`

Period-2 first difference (Δ_2 a_n := a_{n+2} − a_n):

- AII Δ_2: `[6, 6, 6, 6, 6, 6, 6]`  (constant, = 6, matches 3n)
- BDI Δ_2: `[8, 8, 8, 8, 8, 8, 8]`  (constant, = 8, matches 4n)

Both series have constant period-2 first difference, which is the
quasi-polynomial signature for a linear closed-form of slope 3
(AII) and 4 (BDI) — confirming both closed forms across n ∈ {3, ..., 11}.

# Method

LP-based facet (irredundancy) enumeration:
- For each inequality a_i x ≤ b_i in the system, solve
  `max a_i x s.t. a_j x ≤ b_j (j ≠ i), A_eq x = b_eq, |x_k| ≤ 1`.
- If max > b_i, the inequality is facet-defining (irredundant).
- Otherwise it is redundant.

Counted on three encodings per n:
- **AII strict (eq.107)**: Azenhas Theorem D/E sandwich form.
- **AII aii_structure**: Day-60 simpler reading (Main_i for i=2..n).
- **BDI (Rick)**: T_a ≤ B_a, P_a ≥ 0, M_a ≤ P_{a-1}, M_a ≤ P_a, S ≤ P_{n-1}.

# Verdict

CONFIRMED at n=9, 10, 11. Day-69 closed-form fit holds.

`AII facets = 3n − [n even]` and `BDI facets = 4n − 5` are now empirically
verified at n ∈ {3, ..., 11}. Period-2 Δ test passes uniformly.

OQ-AII-FACET-CLOSED-FORM remains closed.

# Files

- `run.py` — driver.
- `results.json` — per-n facet counts, predictions, period-2 Δ check.

— Rick, Day 70 CODE Task C, 2026-06-15
