# Day 103 — ε_R pattern analysis

**Date:** 2026-08-13
**Author:** Rick's compute-agent (Day 103)
**Prior:** Day 101/102 anchor family probes.
**Parent doc:** `proofs/2026-07-18-day102-piecewise-D-anchor.md`.

---

## 0. Data recap

Conjecture (P): for c ≡ R mod 16 (R ∈ {2, 6, 10, 14}),
```
    D(c) = 1 + s_2(m-1) + δ_R(c),        m = (c-2)/4
    δ_R(c) = max(0, v_2(c - R) - ε_R)
```

Empirical ε_R (Day 101 + Day 102 + Day 103):

| R  | ε_R | # data pts | source                                       |
|----|-----|------------|----------------------------------------------|
| 2  | —   | ∞          | base (δ_2 ≡ 0)                                |
| 6  | 3   | 12         | 11 pts Day 101 + 1 pt Day 103 (c=294)         |
| 10 | 4   | 4          | Day 102 (c ∈ {42, 74, 138, 154})              |
| 14 | 4   | ≥ 1        | Day 102 (c = 46) + Day 103 (c = 78, pending)  |

**Day 103 R=6 sanity control (c=294):** v_2(288)=5, actual δ = 2 → inferred ε_6 = 3.
CONFIRMS Day 100/101 result. The compute pipeline is stable.

**Day 103 R=14 probe (c=78):** running (est. 3h). v_2(64)=6; under ε_14=4 predicts δ=2 (v_2(H)=274). Under ε_14=5 predicts δ=1 (v_2(H)=275). Under ε_14=3 predicts δ=3 (v_2(H)=273).

---

## 1. The hypothesis space post-Day 102

Day 102 offered two hypotheses, both falsified by the R=14 c=46 data point (which gave ε_14 = 4, not 5 and not 2):
- **(H1) linear-in-R:** ε_R = (R+6)/4 → predicted ε_14 = 5. **REFUTED.**
- **(H2) Kummer-in-(R+2):** ε_R = 6 − v_2(R+2) → predicted ε_14 = 2. **REFUTED.**

The true value ε_14 = 4 matches neither. We need new candidates.

---

## 2. Exhaustive candidate search

Any function f: {6, 10, 14} → {3, 4, 4} imposes only two nontrivial constraints
(f(6)=3, f(10)=f(14)=4). Enumerating "natural" arithmetic combinations of R:

**Fits (R=6→3, R=10→4, R=14→4):**

| Formula                                    | ε_18 | ε_22 | ε_26 | ε_30 | Structural read                             |
|--------------------------------------------|------|------|------|------|---------------------------------------------|
| `min(⌈log₂(R)⌉, 4)`                        | 4    | 4    | 4    | 4    | Saturates at 4 for all R ≥ 10               |
| `min(⌈log₂(R+2)⌉, 4)`                      | 4    | 4    | 4    | 4    | Same saturation                             |
| `min((R−2)/4 + 2, 4)`                      | 4    | 4    | 4    | 4    | Linear grow-then-cap                        |
| `3 + [R ≥ 10]`                             | 4    | 4    | 4    | 4    | Trivial step                                |
| `3 + [R ≠ 6]`                              | 4    | 4    | 4    | 4    | Trivial step                                |
| `⌊log₂(R)⌋ + 1 = ⌈log₂(R+2)⌉` (uncapped)   | 5    | 5    | 5    | 5    | **UNBOUNDED log grow**                      |

**Fails to fit (R=6→3, R=10→4, R=14→4):**

- All variants of `± v_2(R±2)`, `± s_2(R±2)`, `s_2(R)+c` — none produce (3,4,4).
- `min(v_2(R−2)+2, 4) = 4` for all R ≥ 6 — misses R=6.
- `min(v_2(R−2)+1, 4)` — gives (3,4,3): fails at R=14.

Not a single "Kummer-flavored" formula involving v_2 or s_2 of R±const survives, only saturation-family formulas.

---

## 3. Two structurally distinct families

The candidates split into two structural families with different predictions:

**Family A: SATURATION AT 4.** ε_R = min(g(R), 4) for various g.
Predicts ε_R = 4 for all R ≥ 10.
- Interpretation: the anchor (R−2, R, 2R) exposes a residual factor that grows,
  but the c-uniform base absorbs at most 4 bits. Beyond R = 10 all growth is
  captured by v_2(c−R) itself.

**Family B: LOGARITHMIC UNCAPPED.** ε_R = ⌊log₂(R)⌋ + 1.
Predicts ε_18 = 5, ε_34 = 6, ε_66 = 7.
- Interpretation: each doubling of R adds a bit to the offset. Continues growing
  as R grows; the "4" for both R=10 and R=14 is coincidence of the log floor.
- log₂(10) = 3.32, log₂(14) = 3.81, log₂(18) = 4.17. So ⌊log₂⌋ + 1 = 4, 4, 5.

---

## 4. Top-2 recommended candidate ε_R laws

### Rank 1: `ε_R = min(⌈log₂(R)⌉, 4)`  (SATURATION-LOG)

- **Reason:** most parsimonious; captures the 3→4 jump between R=6 and R=10 as
  the log₂ boundary (log₂(6)<3<log₂(10)); explains why R=10, R=14 have the same
  ε (both round up to 4); predicts a *hard cap* at 4 for all larger R.
- **Prediction R=18:** ε_18 = min(⌈log₂(18)⌉, 4) = min(5, 4) = 4.
- **Structural story:** the "4" cap is the Kummer bit-budget of the (b+2)_L =
  (R+2)_L Pochhammer chain at the anchor (R-2, R, 2R). Beyond a certain R the
  chain saturates and the c-dependence in Q_{2R}(R−2, R, c) contributes at most
  a fixed 4 bits.

### Rank 2: `ε_R = ⌊log₂(R)⌋ + 1`  (UNCAPPED LOG)

- **Reason:** simplest closed form with no ad-hoc cap; matches all three known
  data points; extends smoothly without needing a threshold.
- **Prediction R=18:** ε_18 = ⌊log₂(18)⌋ + 1 = 4 + 1 = 5.
- **Structural story:** each bit of R contributes to a Kummer telescoping in
  the length-(R+2) Pochhammer chain. The floor-of-log₂ counts binary
  positions.

**Discrimination at R=18:** Family A predicts ε_18 = 4; Family B predicts ε_18 = 5.
This is the crucial next experiment.

---

## 5. Anomalies / structural notes

### 5.1 k* alignment (Task 5 partial)

For R=6 anchor (a,b)=(4,6): Day 101 sweep confirms argmin_j v_2(H_c(4,6,j))
lies at j=12 = 2R for all six c-values probed (all j > 12 became None in the
recorded sweep because the fit budget cut off, so we haven't ruled out j > 12
being tied or slightly better; but j=12 is at least a co-minimum).

For R=10 anchor (a,b)=(8,10) with j=20: not sweep-verified in Day 101/102 data.
**Deferred structural check.** Rick may want to run a j ∈ {16..24} sweep at
one R=10 c-value to confirm j=20 is the true argmin.

### 5.2 Why R=10, R=14 tie

Both R=10 and R=14 lie in the same "log₂ bucket" (⌈log₂⌉ = 4). Under Family A
this bucket saturates all further R. Under Family B the tie is a floor-artifact
that breaks at R=16 (impossible for c ≡ 2 mod 4) or R=32 (very expensive to
probe). The R=18 case (which would need c ≡ 18 mod 32) is the earliest
discriminator.

### 5.3 R=18 is outside the current mod-16 framework

R := c mod 16 takes only values {2, 6, 10, 14}. Extending to R = 18 requires
enlarging the modulus (c mod 32) and finding the analogous anchor. Rick's Day
102 §4 predicts the anchor (16, 18, 36) at c ≡ 18 mod 32. The k_max = 36 fit
would take much longer than k=28 (rough scaling: Q_k catalog has degree ~2k in
(a,b) and the fit-sample count scales quadratically). Estimate: ~15h for one
c-value at k=36. **Not feasible in a single day.**

---

## 6. Recommended next c-values for Rick

**Priority 1 (discriminates R=14 → 3 vs 4):** if c=78 result (in progress at
time of writing) shows ε=4, then R=14 offset=4 has 2 data points. Add c=142
(v_2(128)=7 → predicted δ=3 under ε=4). c=142 gives largest v_2 anomaly in
the accessible range.

**Priority 2 (thickens R=14 anomaly base):** c=142 (v_2=7, predicted δ=3
under ε=4). Provides second high-v_2 anomaly to nail down ε.

**Priority 3 (discriminates Family A vs B):** anchor (16, 18, 36) at c ≡ 18
mod 32. Smallest candidate: c=18 itself (but v_2(0) undefined; skip) or c=50
(50 mod 32 = 18, v_2(50−18) = v_2(32) = 5). Under Family A (ε_18=4): predicted
δ = 1. Under Family B (ε_18=5): predicted δ = 0. Cost: prohibitive at k=36.

**Recommendation ranking of the 3 next c-values Rick should compute:**

1. **c = 142** (R=14, v_2 = 7) — confirms ε_14 = 4 with 3rd data point.
2. **c = 174** (R=14, v_2(160) = 5) — cheap 2nd sample at moderate v_2.
3. **c = 90 or 106** (R=10, v_2 = 3 or 1) — thickens R=10 base at small v_2,
   verifies the max(0, ·) floor is exact (both should give δ = 0 under ε_10=4).

If time budget expands: after 3 more R=14 pts, attempt an R=18 anchor probe at
c = 82 (c ≡ 18 mod 32, v_2(64)=6). But k_max=36 fit is a many-hour investment.

---

## 7. Where this doc stops (Day 103 END STATE)

**Delivered:**
- R=6 pipeline sanity confirmed at c=294 (12th data pt, ε_6 = 3).
- Two competing structural families identified (A: saturation-log, B: log-uncapped)
  after exhaustive candidate search.
- R=14 c=78 probe launched (result pending at write time).

**Open:**
- R=14 c=78 v_2(H_c(12,14,28)) result (~3h compute).
- R=18 anchor probe (not attempted; too expensive at k_max=36).
- Structural mechanism (why the cap at 4? why log₂?).
- j > 2R sweep for R=10 anchor (to confirm k*=j=20 argmin).
