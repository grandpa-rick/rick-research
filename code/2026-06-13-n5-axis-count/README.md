# Day 68 CODE Task 1 — n=5 # AXIS count

## Result

**# AXIS at n=5 = 3.**

AXIS variables: `{prefix[1], prefix[5], long[1]}`.

This **confirms C1 (uniform-3)**: # AXIS(n) = 3 for n ≥ 3.

It **refutes C2 (split, +1 at odd n)**, which would have predicted 4.

## Empirical pattern across n = 3, 4, 5

| n | parity | # AXIS | AXIS set                              |
|---|--------|--------|---------------------------------------|
| 3 | odd    | 3      | {m_2,    m_236,    m_23456}           |
| 4 | even   | 3      | {prefix[1], prefix[4], long[1]}       |
| 5 | odd    | 3      | {prefix[1], prefix[5], long[1]}       |

The universal pattern: **AXIS = {prefix[1], prefix[n], long[1]}** at every tested n.

The Day-62 conjecture `# AXIS(n) = 3 - [n even]` was refuted at n=4
(Day-67 corrected count = 3) and is now refuted at n=5 too. The corrected
conjecture is constant-3.

## Method

- Built 12×15 piece matrices (BDI ← AII) for n=5.
- Registry: 29 piece variants × {21 + 6 R-double-family} = 27 BDI-feasible
  pieces.
- The R-double family (at level 1, 2, or 3) has 3 BDI-feasible variants each
  with α ∈ {0, 1, 2} (α ≥ 3 fails `S ≤ P_4`).
- A variable is AXIS iff its coordinate hyperplane has ≥3 rank-1 piece-pair
  collisions (same strict criterion as Day-67 n=4 and Day-68 n=3).
- Verified BDI feasibility on all AII lattice points with `sum ≤ 5` (2040 pts).

## Files

- `n5_setup.py` — AII/BDI structure, feasibility predicates, lattice
  enumeration.
- `n5_pieces.py` — piece registry (base + P5 routings + L1 routings + s_5
  + R-double families at levels 1, 2, 3).
- `n5_registry.py` — main analysis script: feasibility, column-counts,
  rank-1 wall analysis, AXIS classification.
- `n5_registry.json` — full registry (BDI columns for each AII variable).
- `n5_axis_count.txt` — count summary and verdict.
- `results.json` — detailed analysis results (full vs R-double-removed).

## Verdict

C1 (uniform-3) is the surviving conjecture. The next step is to PROVE
that # AXIS(n) = 3 with AXIS = {prefix[1], prefix[n], long[1]} for all
n ≥ 3 — likely by characterising the R-double family abstractly as the
"only mechanism" that lifts prefix[1] out of RIGID, and characterising
prefix[n] and long[1] as the unique unconstrained-coordinates of the
AII polytope.

## Numerical details (FULL registry, R-double IN, 27 pieces)

```
prefix[1]      |      3 cols | AXIS (9 pair-collisions, via R-double family)
prefix[2]      |      1 col  | RIGID
prefix[3]      |      1 col  | RIGID
prefix[4]      |      1 col  | RIGID
prefix[5]      |      9 cols | AXIS (36 pair-collisions, free prefix)
long[1]        |     10 cols | AXIS (36 pair-collisions, free long)
long[2..5]     |      1 col  | RIGID (M_2..M_4 partners + L_5 → S)
short[1..4]    |      2 cols | BINARY (via R-double family at each level)
short[5]       |      2 cols | BINARY (Singleton-bound variant)
```

Rank distribution over C(27,2) = 351 piece-pairs:
- rank 1: 84 pairs (the rank-1 walls below)
- rank 2: 121 pairs
- rank 3: 101 pairs
- rank 4: 45 pairs

Rank-1 walls (6 distinct, all COORD):
- {prefix[5] = 0}: 36 pairs
- {long[1] = 0}: 36 pairs
- {prefix[1] = 0}: 9 pairs
- {short[2] = 0}: 1 pair
- {short[3] = 0}: 1 pair
- {short[5] = 0}: 1 pair
