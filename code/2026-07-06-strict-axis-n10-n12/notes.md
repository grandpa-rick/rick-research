# Strict #AXIS partition extended to n = 10, 11, 12 (2026-07-06)

| n | prefix-strict | long-strict | total | 2(n-1) | Theorem 10.1 partition | runtime |
|---:|---:|---:|---:|---:|:--:|---:|
| 10 | 9 | 9 | 18 | 18 | MATCH | 1.6 s |
| 11 | 10 | 10 | 20 | 20 | MATCH | 2.4 s |
| 12 | 11 | 11 | 22 | 22 | MATCH | 3.4 s |

**Verdict: MATCH.** For each n in {10, 11, 12}, the empirical strict-AXIS coordinate set equals the Theorem-10.1-predicted partition set-theoretically: prefix-strict = {prefix[1..n-2], prefix[n]}, long-strict = {long[1..n-1]}. Total 2(n-1). No runtime issues (all n completed well under 15 s). Trust: `computed` (empirical only; Theorem 10.1 is Rick's proof). Details in `strict_axis_partition_n10_n12.csv` and `strict_axis_indexed_n10_n12.csv`; run log in `run.log`.
