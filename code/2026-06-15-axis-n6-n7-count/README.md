---
title: "Day 70 CODE Task A — # AXIS count at n=6 and n=7"
author: Rick
date: 2026-06-15
status: **# AXIS = 3 at both n=6 and n=7.** Lemma D upper bound confirmed empirically through n=7.
---

# Bottom line

Both n=6 (EVEN) and n=7 (ODD) match the uniform-3 hypothesis. AXIS at
each n is **`{prefix[1], prefix[n], long[1]}`** — exactly the structural
axis triple from n=3, 4, 5.

**# AXIS(n) = 3 confirmed at n ∈ {3, 4, 5, 6, 7}.** Lemma D upper bound
has solid empirical support — go nail the proof.

## Summary table

| n | parity | # AXIS | AXIS                                       | linkLHS? |
|---|--------|--------|--------------------------------------------|----------|
| 3 | odd    | 3      | {prefix[1], prefix[3], long[1]}            | no       |
| 4 | even   | 3      | {prefix[1], prefix[4], long[1]}            | yes      |
| 5 | odd    | 3      | {prefix[1], prefix[5], long[1]}            | no       |
| 6 | even   | **3**  | **{prefix[1], prefix[6], long[1]}**        | yes      |
| 7 | odd    | **3**  | **{prefix[1], prefix[7], long[1]}**        | no       |

The triple is *uniform in n* and *parity-independent*. R-double family
(α ∈ {0,1,2}) is the **only** mechanism lifting `prefix[1]` out of RIGID.
prefix[n] and long[1] are the unique "free" coords of the AII polytope.

# Method

For each n ∈ {6, 7}:
1. Build the AII polytope (3n vars: prefix[1..n], long[1..n], short[1..],
   plus linkLHS at even n).
2. Build the BDI polytope (3n−3 vars: M_2..M_{n−1}, B_1..B_{n−1},
   T_1..T_{n−1}, S).
3. Enumerate AII-feasible lattice points up to sum ≤ n.
4. Generate the candidate piece set (general scaffold lifted from n=5):
    - 1 base piece
    - P_n routing variants (BT_i for i=1..n−1, BT_2 doubled, S, M_i, splits)
    - L_1 routing variants (B_2..B_{n−1}, M_2..M_{n−1}, S, doubled at M_2,
      BT_2)
    - Singleton variant (odd n): s_n → 2·S
    - R-double family at every level a ∈ {1, ..., n−1} with α ∈ {0, 1, 2}
5. Filter by BDI-feasibility (apply piece to every AII-feasible point).
6. Compute the kernel arrangement: rank-1 piece-pair walls.
7. AXIS = coord-walls with ≥3 piece-pair collisions.

# Results

## n = 6 (EVEN, linkLHS variable present)

- 18 AII vars, 15 BDI vars, 5190 feasible lattice pts at sum ≤ 6.
- 38 candidate pieces; 36 BDI-feasible (2 dropped: P_n→S and L_1→S put
  too much mass into S).
- **All 15 R-double pieces FEASIBLE** (levels 1..5 × α ∈ {0,1,2}).
- Rank distribution: rank 1 = 129, rank 2 = 217, rank 3 = 240, rank 4 = 44.

### Column-count breakdown (full registry):

| AII var       | # cols | role                            |
|---------------|--------|---------------------------------|
| prefix[1]     | 3      | **AXIS** (R-double family)      |
| prefix[2..5]  | 1      | RIGID                           |
| prefix[6]     | 11     | **AXIS** (free prefix)          |
| long[1]       | 12     | **AXIS** (free long)            |
| long[2..6]    | 1      | RIGID                           |
| short[1..5]   | 2      | BINARY (R-double S-shift)       |
| linkLHS       | 1      | RIGID (no nontrivial routing)   |

### Rank-1 coordinate walls (cone-interior):

- `{prefix[6] = 0}`: 55 pairs  [COORD]  — AXIS
- `{long[1] = 0}`:   55 pairs  [COORD]  — AXIS
- `{prefix[1] = 0}`: 15 pairs  [COORD]  — AXIS (R-double family)
- `{short[2..5] = 0}`: 1 pair each  — BINARY toggles

**`# AXIS(6) = 3`** with AXIS = {prefix[1], prefix[6], long[1]}.

## n = 7 (ODD, no linkLHS)

- 21 AII vars, 18 BDI vars, 56264 feasible lattice pts at sum ≤ 7.
- 46 candidate pieces; 44 BDI-feasible (same 2 dropped).
- **All 18 R-double pieces FEASIBLE** (levels 1..6 × α ∈ {0,1,2}).
- Rank distribution: rank 1 = 181, rank 2 = 347, rank 3 = 362, rank 4 = 56.

### Column-count breakdown (full registry):

| AII var       | # cols | role                            |
|---------------|--------|---------------------------------|
| prefix[1]     | 3      | **AXIS** (R-double family)      |
| prefix[2..6]  | 1      | RIGID                           |
| prefix[7]     | 13     | **AXIS** (free prefix)          |
| long[1]       | 14     | **AXIS** (free long)            |
| long[2..7]    | 1      | RIGID                           |
| short[1..7]   | 2      | BINARY                          |

### Rank-1 coordinate walls (cone-interior):

- `{prefix[7] = 0}`: 78 pairs  [COORD]  — AXIS
- `{long[1] = 0}`:   78 pairs  [COORD]  — AXIS
- `{prefix[1] = 0}`: 18 pairs  [COORD]  — AXIS (R-double family)
- `{short[i] = 0}`: 1 pair each  — BINARY toggles

**`# AXIS(7) = 3`** with AXIS = {prefix[1], prefix[7], long[1]}.

# Files

- `general_axis.py` — n-agnostic AII/BDI structures, lattice enumeration,
   piece-matrix building, AXIS analysis.
- `general_pieces.py` — n-agnostic piece registry generator (base +
   P_n/L_1 variants + R-double family at every level).
- `n6_axis.py` — n=6 driver.
- `n7_axis.py` — n=7 driver.
- `sanity_n5.py` — sanity check: reproduces Day-68 result # AXIS(5) = 3.
- `n6_results.json` / `n7_results.json` — full analysis data.
- `n6_registry.json` / `n7_registry.json` — piece registry (BDI columns
   per AII var, per piece).

# Verdict

**Lemma D upper bound** (`# AXIS(n) ≤ 3` for all n ≥ 3) has solid
empirical support across n ∈ {3, 4, 5, 6, 7}. The structural pattern is
parity-independent: the R-double family at level 1 contributes the
prefix[1] AXIS uniformly, while prefix[n] and long[1] are free coords of
the AII polytope. No new piece family is needed at n=6, 7 — the n=5
scaffold lifts directly.

The next step is the PROVE side (Day 70 concurrent session): characterise
the AXIS triple abstractly and prove # AXIS(n) = 3 for all n ≥ 3.

— Rick, Day 70 CODE Task A, 2026-06-15
