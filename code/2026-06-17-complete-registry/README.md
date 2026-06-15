# Day 72 CODE Task A — BDI-feasible piece registry at n = 5, 6, 7

**Goal.** Build a piece registry that includes all known structurally
distinct BDI-feasible pieces — supporting the Day-72 PROVE pivot to
cover-restricted #AXIS.

## Composition of the augmented registry

For each `n ∈ {5, 6, 7}`:
- **(A)** Day-70 minimal cover (base + P_n routings + L_1 routings + R-double family).
- **(B)** Day-71 simple-divert pieces `π_α^{(i)}` for interior `i ∈ {2, …, n-2}` and `α ∈ {0, 1, 2}` (adds `α e_S` to the `prefix[i]` column).
- **(C)** Day-72 l_j-divert pieces for `j ∈ {2, …, n-1}` and `β ∈ {0, 1, 2}` (adds `β e_S` to the `long[j]` column).
- **(D)** Day-72 Class-1 auxiliary pieces from the R-AXIS upper bound proof.

After feasibility filtering and matrix-level dedup:
- **n = 5:** 42 pieces
- **n = 6:** 53 pieces
- **n = 7:** 66 pieces

## Feasibility check method

A piece is BDI-feasible iff for every AII extreme ray `r`, `M @ r` is a
BDI lattice point (Day-70 Cor 5.1). The AII rays are enumerated for the
*general_axis* cone:
```
  Main_i:  long[i] + short[i] ≤ prefix[i-1]   for i = 2 … n
  (at even n: short[n] is absent and the i=n constraint reduces to long[n] ≤ prefix[n-1])
  linking eq (even n):  linkLHS = ∑_{i=1..n-1} short[i]
```
This yields `3n` rays at odd `n` and `3n - 1` rays at even `n`. The ray
list is in `run.py::aii_rays(n)`.

## Acceptance checks

| n | Day-70 in registry | Simple-divert in registry |
|---|---|---|
| 5 | 30 / 32 (2 Day-70 listed as infeasible) | 6 / 6 |
| 6 | 36 / 38 (2 infeasible) | 9 / 9 |
| 7 | 44 / 46 (2 infeasible) | 12 / 12 |

The 2 missing pieces per `n` are `P_n_in_S` and `L_1_in_S` (route `p_n`
or `l_1` to `S`). These fail the *pure* ray check on `e_{prefix[n]}`
respectively `e_{long[1]}`: image becomes `e_S` with `P_{n-1} = 0`, so
`S = 1 > 0 = P_{n-1}` is BDI-infeasible. Day-70's own filter (`n6_axis.py`)
already flags these as infeasible.

## Notes on the "full universe"

We attempted full enumeration over all BDI-feasible pieces with ray-image
sum bounded by `N`. Even at `N = 2` the count exceeds 1 million pieces at
`n = 5` (matrix-by-DFS hits the cap in < 1s). Hence the augmented
registry above — containing every structurally identified family —
is what we use for the #AXIS analysis (Task B). It strictly contains
every Day-70 and Day-71 piece we know about.

## Outputs

- `registry-n5.json`, `registry-n6.json`, `registry-n7.json` —
  piece dicts `{name: {aii_var: bdi_column}}`.
- `results.json` — per-n statistics (total sum distribution, max ray
  image sum distribution, routing counts per AII variable) and
  acceptance results.

## Reproducing

```
python3 run.py
```
