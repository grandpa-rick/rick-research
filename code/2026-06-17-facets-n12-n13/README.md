# Day 72 CODE Task C — AII rays at n = 8 + facet count at n = 12, 13

## Three checks

### (1) AII cone extreme rays at n = 8

Day-70 Theorem 4.2 predicts at even `n` the linking equation
`linkLHS = ∑ short[i]` collapses one ray relative to the odd-n pattern
of `3n` rays. So at `n = 8` we expect **23 = 3·8 − 1** extreme rays.

**Result:** 23 rays ✓

### (2) AII facet count at n = 12, 13

Closed form (Day-69, reverified Day-70 at n=9..11):
`#{AII facets} = 3n - [n even]`.

| n | observed | predicted | match |
|---|---|---|---|
| 12 | 35 | 35 (= 3·12 − 1) | ✓ |
| 13 | 39 | 39 (= 3·13)     | ✓ |

### (3) BDI facet count at n = 12, 13

Closed form `#{BDI facets} = 4n - 5`.

| n | observed | predicted | match |
|---|---|---|---|
| 12 | 43 | 43 (= 4·12 − 5) | ✓ |
| 13 | 47 | 47 (= 4·13 − 5) | ✓ |

### (4) Period-2 finite difference (Day-58 calibration)

The only valid quasi-poly test (Day-58): step-by-step second-difference
across two periods should be constant.

```
AII series (n=3..13): [9, 11, 15, 17, 21, 23, 27, 29, 33, 35, 39]
BDI series (n=3..13): [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47]

AII period-2 diff: [6, 6, 6, 6, 6, 6, 6, 6, 6]   ✓ const 6 (= 2·3 for linear 3n)
BDI period-2 diff: [8, 8, 8, 8, 8, 8, 8, 8, 8]   ✓ const 8 (= 2·4 for linear 4n)
```

## Verdict

**CONFIRMED.** AII rays at `n = 8` count `23 = 3n - 1`. Facet closed
forms `3n - [n even]` (AII) and `4n - 5` (BDI) hold at `n = 12, 13`.
Period-2 finite differences are exactly `6` and `8` throughout
`n = 3..13`. Day-69 quasi-poly fit is rock solid out to `n = 13`.

## Reproducing

```
python3 run.py
```

## Outputs

- `results.json` — full ray + facet + diff results.
