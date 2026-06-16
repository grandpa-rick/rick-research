---
title: "Day 75 CODE Task C (stretch) — Strict #AXIS = 14 at n = 8"
author: Rick
date: 2026-06-20
status: **PASS** — clean re-verification of Day-73's result.
---

# TL;DR

Strict #AXIS at $n = 8$ in the augmented registry:
$$\#\,\text{AXIS}(8) = 14 = 2(n - 1).$$

AXIS variables exactly match the prediction
$\{p_1, \ldots, p_{n-2}, p_n, l_1, \ldots, l_{n-1}\}$. Regression
check at $n = 5$ also confirms 8.

# Numbers

| n | # pieces (deduped) | strict #AXIS | predicted $2(n-1)$ | match |
|---|--------------------|--------------|--------------------|-------|
| 5 | 42                 | 8            | 8                  | ✓     |
| 8 | 77                 | 14           | 14                 | ✓     |

## Per-var $\max$ 3-clique size at n = 8

| AII var      | max group size | AXIS? |
|--------------|-----------------|-------|
| prefix[1]    | 3               | ✓     |
| prefix[2]    | 3               | ✓     |
| prefix[3]    | 3               | ✓     |
| prefix[4]    | 3               | ✓     |
| prefix[5]    | 3               | ✓     |
| prefix[6]    | 3               | ✓     |
| **prefix[7]**| **1**           | **NO**|
| prefix[8]    | **15**          | ✓     |
| long[1]      | **15**          | ✓     |
| long[2..7]   | 3               | ✓     |
| **long[8]**  | **1**           | **NO**|
| short[1..7]  | ≤ 2             | NO    |
| linkLHS      | 1               | NO (gauge) |

`prefix[7]` is the RIGID interior boundary ($n-1$). `long[8]` always
routes to $S$ via base — no variant. `prefix[8]` (free prefix) and
`long[1]` (free long) have very high group size (15) because they
have many variants.

# Pattern

The "stuck" (non-AXIS) coords at every $n$ are:
- $p_{n-1}$ — RIGID interior boundary (Day-69 lemma).
- $l_n$ — base routes to $S$, no need for variants.
- All $s_i$ — at most 2-valued (BINARY), never 3-clique.
- `linkLHS` at even $n$ — gauge-fixed to 0.

# Verdict

**PASS**. The $2(n-1)$ extrapolation line is now empirically validated
at $n \in \{5, 6, 7, 8, 9\}$ (the latter from Day-73's
`code/2026-06-18-strict-axis-n8-n9/`). Day-75 re-verification adds
no new data — but it's a clean, reproducible probe of the
augmented-registry pipeline.

# Files

- `strict_axis_n8.py` — driver (imports Day-73 strict_axis machinery)
- `results.json` — verification result + per-var diagnostics
- `REPORT.md` — this file

# Relation to prior work

Day-73 (`code/2026-06-18-strict-axis-n8-n9/`) already confirmed
$n = 8$ AND extended to $n = 9$. This Day-75 task is a clean
re-verification in the dedicated directory CODE.md requested.

# Calibration

- Day-69 Facet-count-before-headline: $2(n-1)$ matches closed form
  at every checked $n$. ✓
- Regression guard at $n = 5$ holds (strict #AXIS = 8). ✓

— Rick, Day 75 CODE Task C (stretch), 2026-06-20
