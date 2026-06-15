# Day 72 CODE Task B — Strict # AXIS at n = 5, 6, 7

**Goal.** Empirically confirm Day-71's prediction that strict #AXIS (as
counted by 3-clique existence on coordinate hyperplanes) grows linearly
in `n` — the load-bearing fact that drove the Day-72 PROVE pivot from
strict to cover-restricted #AXIS.

## Strict #AXIS definition (Day-71 / Day-72 R-AXIS framework)

A coordinate `c ∈ AII` is **strict AXIS** for a registry `R` iff there
exist three pieces `π_1, π_2, π_3 ∈ R` such that

1. `M_{π_i}[:, c'] = M_{π_j}[:, c']` for every `c' ≠ c` and every `i, j`;
2. the three columns `M_{π_i}[:, c]` are pairwise distinct.

That is: the three pieces form a 3-clique on `{c = 0}` — they agree
*everywhere* except column `c`.

## Algorithm

For each AII coord `c`:
1. Group pieces by the tuple `(M[:, c'])_{c' ≠ c}`.
2. Within each group, count distinct `M[:, c]` values.
3. `c` is AXIS iff some group has `≥ 3` distinct `c`-columns.

## Results

Input: `registry-n{5,6,7}.json` from `2026-06-17-complete-registry/`.

| n | # pieces | # AXIS | Day-71 lower bound (n + 1) | Status |
|---|---|---|---|---|
| 5 | 42 | **8**  | 6 | OK |
| 6 | 53 | **10** | 7 | OK |
| 7 | 66 | **12** | 8 | OK |

`Δ(# AXIS)` between consecutive `n` is uniformly `2`. Linear growth
confirmed: **# AXIS(n) = 2(n - 1)** at `n ∈ {5, 6, 7}`.

## AXIS variables by n

**n = 5:** `{prefix[1], prefix[2], prefix[3], prefix[5], long[1], long[2], long[3], long[4]}`

**n = 6:** `{prefix[1..4], prefix[6], long[1..5]}`

**n = 7:** `{prefix[1..5], prefix[7], long[1..6]}`

### Structural reading

- **`prefix[1..n-2]`** become AXIS via the Day-71 simple-divert family.
- **`prefix[n]`** is AXIS via the free-top family (Day-69 Lemma B).
- **`long[1]`** is AXIS via the R-double family (Day-69 Lemma C / free-bottom).
- **`long[2..n-1]`** become AXIS via the Day-72 l_j-divert family.

Two AII coords are NOT axis at any `n`:
- **`prefix[n-1]`**: rigid in the augmented registry (no triple-routing variant included). Simple-divert at `i = n-1` is excluded — see Day-72 proof §4.2.
- **`long[n]`** and `linkLHS`: rigid by construction (route into `S` / linking).
- **`short[i]` for `i ≥ 2`**: max group-size = 2 (binary, not ternary) — no Lemma in the registry triples them.

## Consequence for PROVE

Strict #AXIS grows linearly in `n`. So a uniform bound `#AXIS ≤ 3` is
RIGID-impossible for the strict criterion. The Day-72 pivot to
*cover-restricted* R-AXIS is necessary, as already argued in
`proofs/2026-06-17-r-axis-cover-restricted.md`.

## Reproducing

```
python3 run.py
```

Reads from `2026-06-17-complete-registry/registry-n{5,6,7}.json`.

## Outputs

- `results.json` — per-n results: `strict_n_axis`, `axis_vars`,
  per-AII-var diagnostics with example 3-cliques.
