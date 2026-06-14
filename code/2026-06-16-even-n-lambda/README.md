---
title: "Day 71 CODE Task B — Even-n Λ ray analysis at n=4, 6"
author: Rick
date: 2026-06-16
status: **3n - [n even] extreme rays VERIFIED at n ∈ {3, 4, 5, 6}.**
---

# Bottom line

Closed-form prediction: # extreme rays of the AII cone = **3n − [n even]**.

| n | parity | # rays | predicted | match? |
|---|--------|--------|-----------|--------|
| 3 | odd    | 9      | 9         | YES    |
| 4 | even   | **11** | **11**    | YES    |
| 5 | odd    | 15     | 15        | YES    |
| 6 | even   | **17** | **17**    | YES    |

The Day-70 Theorem 4.2 §4.3 Λ-collapse sketch is **VERIFIED** at n=4, 6:
the linking equation `linkLHS = sum_{i=1..n-1} short[i]` kills exactly
one extreme ray of the AII cone at even n, dropping the count from 3n
(odd-n pattern) to 3n − 1.

Period-2 finite difference: rays at n=3..6 = [9, 11, 15, 17] and
`Δ_period2(rays)(n) = rays(n+2) - rays(n) = 6` for both parities.
This is consistent with linear growth of step 6 per period-2, hence
period-2 polynomial of degree 1 (i.e. *linear quasipoly*). Matches the
Day-58 quasi-polynomial calibration ("period-step finite-difference is
the only valid quasipoly test").

# Method

Enumerate extreme rays of the AII cone

  `{ x in R^{3n} : A_ub x ≤ 0, A_eq x = 0 }`

at n=3, 4, 5, 6:

1. Build the cone using `azenhas_system_TheoremDE_strict` (Day-69):
   - (97) `long[i] + short[i] ≤ prefix[i-1]` for `i = 2..n-1`
   - (98)L `sum_{i=1..n-1} short[i] ≤ long[n]`
   - (98)U `long[n] - sum_{i=1..n-1} short[i] ≤ prefix[n-1]`
   - positivity on every variable
   - even n: `linkLHS = sum_{i=1..n-1} short[i]`

2. Find irredundant facets via LP (Day-69 routine `count_facets`).

3. For each `(d_cone − 1)`-subset of facets:
   - solve `A_eq r = 0` AND `a_S r = 0` exactly with rationals
   - if nullspace has dim 1, take the generator, orient so
     `A_ub r ≤ 0`
   - normalize and hash (canonical: scale so first nonzero entry is 1)

4. Deduplicate. Cone dim `d_cone = n_vars - rank(A_eq)`.

Exact rational arithmetic throughout (no floating point). At even n the
single linking equation reduces `d_cone` by 1 (from 3n to 3n − 1).

# Cross-check

The first 5 example rays at n=6 are precisely the "Λ-saturating"
rays of the form

  `prefix[i] + long[6] + short[i+1] + linkLHS`, i = 0, 1, 2, 3, 4

(where the i=0 case has only `long[6] + short[1] + linkLHS`). This is
the structural pattern Day-70 Theorem 4.2 §4.3 predicts for the
even-n Λ-coupled family.

# Files

- `run.py` — full ray enumerator + driver
- `results.json` — per-n results (ray count, facet labels, ray list)

# Verdict

**Even-n Λ-collapse verified.** Day-70 even-n ray characterisation has
direct CODE backing (per the Day-69 calibration "facet-count-before-
headline" rule). Closed form `3n - [n even]` confirmed at n ∈ {3,..,6}.

— Rick, Day 71 CODE Task B, 2026-06-16
