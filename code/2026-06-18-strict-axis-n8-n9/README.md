# Day 73 CODE Task B — Strict #AXIS at n = 8, 9

## Headline

**`2(n-1)` extrapolation CONFIRMED at n=8 (#AXIS=14) and n=9 (#AXIS=16).**

Combined with Day-72 (n=5,6,7 -> #AXIS=8,10,12), the table is:

| n | # pieces (augmented registry) | strict #AXIS | predicted 2(n-1) | match |
|---|---|---|---|---|
| 5 | 42 |  8 |  8 | YES |
| 6 | 53 | 10 | 10 | YES |
| 7 | 66 | 12 | 12 | YES |
| 8 | 77 | 14 | 14 | YES |
| 9 | 90 | 16 | 16 | YES |

AXIS variables match the predicted set exactly at every n:
`{p_1, ..., p_{n-2}, p_n, l_1, ..., l_{n-1}}`.

## Method

Build the augmented registry at each n (Day-70 minimal cover ∪
Day-71 simple-divert ∪ Day-72 `l_j`-divert ∪ Day-72 Class-1 aux).
Filter via Day-70 Cor 5.1 (ray-based BDI feasibility). Dedup.

Per AII coord c, group pieces by their non-c columns; c is a STRICT
AXIS iff some group has ≥ 3 distinct c-columns (3-clique on the wall
{c = 0}).

## Reproducing

```bash
python3 strict_axis.py
```

## Files

- `strict_axis.py` — extends Day-72 strict_axis to n=8, 9 with a
  built-in n=5 regression check (asserts strict #AXIS at n=5 = 8).
- `results.json` — per-n strict #AXIS count, AXIS var set, per-var
  max-3-clique-size diagnostics.

## What this promotes

Day-72 had three datapoints (n=5,6,7); the `2(n-1)` line was
over-determined but small-n. Two more datapoints (n=8,9) make it
empirically strong. The "*right* AXIS-var set" prediction also
holds: only the interior `p_2, ..., p_{n-2}` plus boundary
`p_1, p_n` (omitting `p_{n-1}`!) plus all `l_1, ..., l_{n-1}`
(omitting `l_n`).

The "stuck" variables in every n:
- `p_{n-1}` (never an AXIS — interior boundary)
- `l_n` (always routed to S directly, no freedom)
- All `short[i]` (never an AXIS — every short is 2-valued via
  the R-double, but never 3-valued)
- `linkLHS` at even n (gauge-fixed to 0)

This is consistent with the Day-72 lemma that AXIS vars are
exactly the n "free" prefix vars (minus p_{n-1}) and the n-1
non-trivial `l_j`.
