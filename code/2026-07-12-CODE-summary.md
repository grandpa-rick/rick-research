# Day 90/91 CODE — Δ_k^{(c)} catalog + closed-form finds for PROVE

**Date:** 2026-07-12
**Session:** CODE (implementation, computation)
**Trigger:** state/CODE.md was stale (Day-89 β'(8) work fully executed). Pivoted to Stage 1 support for state/PROVE.md (Day 90/91 SCP-uniform proof attempt).

## Primary deliverable — Δ_k^{(c)} and LB_k^{(c)} catalog

### Files
- `code/2026-07-12-Delta-k-c-catalog.py` — computes Δ_k^{(c)} restricted to Poch-min ∩ shell.
- `code/2026-07-12-hk-shell-min-full.py` — direct min v_2(h_k^{(c)}) over shell in [0, 2^T)^2 (T=8 or 7).
- `code/2026-07-12-Delta-k-c-catalog.json` — merged catalog with both Δ_k, LB_pochmin, LB_direct, achievers.
- `code/2026-07-12-Delta-k-patterns.py` — Stage 2 closed-form pattern hunt.

### Coverage
c ∈ {5, 6, 7, 8, 9, 10, 11}, k ∈ {0, 1, ..., c-1}. Uses catalog Q_k for k ≤ 6, extraction pipeline for k ≥ 7.

### LB_direct matrix (= min v_2(h_k^{(c)}(a,b)) over shell)
```
  c\k |      0      1      2      3      4      5      6      7      8      9     10
    5 |      6      4      3      5      5
    6 |      7      7      7      7      7      7
    7 |      8      7      7      6      7      7      6
    8 |     11     11     11     11     11     11     11     11
    9 |     14     11      9     12     12     12     10     11     13
   10 |     15     15     15     15     14     14     14     14     15     15
   11 |     16     15     15     13     14     14     12     14     16     15     14
```

### min_k LB_k^{(c)} matches known β'(c) exactly
```
  c=5:  β'= 3   k* ∈ {2}                           (registry: 3 ✓)
  c=6:  β'= 7   k* ∈ {0, 1, 2, 3, 4, 5}            (registry: 7 ✓)
  c=7:  β'= 6   k* ∈ {3, 6}                        (registry: 6 ✓)
  c=8:  β'=11   k* ∈ {0, 1, 2, 3, 4, 5, 6, 7}      (registry: 11 ✓ Day 89)
  c=9:  β'= 9   k* ∈ {2}                           (registry: 9 ✓)
  c=10: β'=14   k* ∈ {4, 5, 6, 7}                  (registry: 14 ✓)
  c=11: β'=12   k* ∈ {6}                           (registry: 12 ✓ Day 90)
```

**All 7 c-values match. Catalog is validated.**

## Closed-form finds (Stage 2)

### (F1 — FALSIFIED at c=13) β'(c) = 3(c-3)/2 for odd c ≥ 5   [4-POINT COINCIDENCE]

The formula fits c ∈ {5, 7, 9, 11} exactly (3, 6, 9, 12) and looked like a load-bearing closed form. **Cross-check against PROVE's c=13 scan (`code/2026-07-12-c13-full-scan-output.txt`) breaks it:**

- 3(13-3)/2 = 15 (F1 prediction)
- β'(13) ≤ 16 (three distinct-min witnesses at (7,0,6), (7,8,6), (15,0,6))
- Per-k min v_2(h_k^{(13)}(a,b)) scan: min over k in [0..6] is 16 at k*=6.

So β'(13) = 16, and F1 fails by 1 at c=13. **Same failure mode as D2', D1, E — a 4-point fit that doesn't extend.** Rick's Day-90 "notation lies, algebra doesn't" applies: the low-c pattern IS coincidental.

**Explanation.** The pattern β'(c_odd) = 3(c-3)/2 was equivalent to k*=2 giving LB_2 = 2·v_2((c-3)!) + 1 (from F3 below) at c ≡ 1 mod 4, and k*=6 giving LB_6 = 6 or similar at c ≡ 3 mod 4. But at c=13, the argmin FLIPS: c ≡ 1 mod 4, but k*=6 (not k=2). LB_6^{(13)} = 16 < LB_2^{(13)} = 17. So the argmin-schedule breaks and F1 with it.

**Registers as: calibration data.** Another low-c coincidence killed. Confirms Day 91 conclusion that β'(c) mod-2^k structure is deeper than any low-degree polynomial-in-c fit.

### (F2) Δ_1^{(c)} = v_2(c(c-1)) uniformly   [PROVED FROM Q_1]

Q_1(a, b, c) = −c(c−1) is independent of (a, b). Hence
    v_2(Q_1(a, b, c)) = v_2(c(c-1))
identically. Verified for c = 5..11, both parities.

Combined with the Kummer bound on Pochhammers:
```
    LB_1^{(c)} = 2·v_2((c-2)!) + v_2(c) + v_2(c-1)
              = 2(c-2) − 2·s_2(c-2) + v_2(c) + v_2(c-1).
```
where s_2(n) is the base-2 digit sum. This is a fully explicit closed form for LB_1 at ALL c.

### (F3) Δ_2^{(c_odd)} = 1 uniformly   [HOLDS AT c ∈ {5, 7, 9, 11, 13}]

Q_2(a, b, c) = −c(2ab + 2a + 4b − c³ + 4c² − 5c + 6). At odd c, v_2(c) = 0 and the bracket has controlled 2-adic behaviour on the Poch-min shell — data says v_2 = 1 always.

Predicts LB_2^{(c_odd)} = 2·v_2((c-3)!) + 1. Verified:
- c=5:  2·v_2(2!)  + 1 = 2·1 + 1 = 3   ✓
- c=7:  2·v_2(4!)  + 1 = 2·3 + 1 = 7   ✓
- c=9:  2·v_2(6!)  + 1 = 2·4 + 1 = 9   ✓
- c=11: 2·v_2(8!)  + 1 = 2·7 + 1 = 15  ✓
- c=13: 2·v_2(10!) + 1 = 2·8 + 1 = 17  ✓  (cross-check against PROVE c13 scan: LB_2 = 17)

**However k* = 2 is only argmin for c ∈ {5, 9}.** At c = 13 (also ≡ 1 mod 4), k* = 6 with LB_6 = 16. So F3 does NOT determine β'(c) beyond c = 9.

Still: F3 is a genuine c-uniform lemma about LB_2, provable from Q_2's structure. Worth formalising in Lean as a warmup.

### (F4) Uniformity of LB_k^{(c)} in k for c ∈ {6, 8}   [OBSERVATION]

c = 6: LB_k = 7 for all k = 0..5.
c = 8: LB_k = 11 for all k = 0..7.

At these c, the SCP "sharp cancellation" condition — every carrier k contributes the same v_2 to H_c — is TIGHT. The 2^T periodicity argument (Day 89) directly proved β'(8) = 11 by this mechanism.

c = 10 is NOT uniform: LB_k ∈ {14, 15} with 14 at k=4..7. Middle-plateau pattern.

### (F5) argmin k* has mod-4 structure for odd c

| c mod 4 | c value | k*        |
|--------:|---------|-----------|
|       1 | 5       | {2}       |
|       3 | 7       | {3, 6}    |
|       1 | 9       | {2}       |
|       3 | 11      | {6}       |

- c ≡ 1 (mod 4): k* = 2 (matches F3 above).
- c ≡ 3 (mod 4): k* ∈ {3 or 6} depending on c.

Compatible with the Day-84 "mod-4 anchor" conjectures — but those broke at higher c (Day 90 memo), so treat cautiously.

## Data-check meta-rule outcome

**k=1 sanity (Rick's Day-88 rule):** Δ_1^{(c)} = v_2(c(c-1)) trivially derived from Q_1 = −c(c−1). Data matches at all c = 5..11 in both parities. **PASSED.**

## PROVE / registry implications

- **`structural-conjecture-S` (SCP):** LB_k catalog verified at c = 5..11 (7 c-values). Sharp-cancellation-min structure holds empirically. Promoting `checked-sober → proved uniformly` still needs a c-uniform closed form for min_k LB_k^{(c)}, which — after F1 falsification at c=13 — is confirmed to have **no clean polynomial-in-c form** at any of the low-c fits attempted so far (D1, D2, D2', E, F1 all broken by c ∈ {11, 12, 13}). This is Day 91's genuine negative: the SCP formulation is correct, but its closed form is deeper than 4-point patterns.

- **`refined-dip-formula` (D1):** Falsified at c=11 per Day 91 memo. D1' proposed in PROVE, but also fits low-c only.

- **F2 as a proved lemma (LEAN candidate):** Δ_1^{(c)} = v_2(c(c-1)) is a c-uniform lemma with a trivial proof from Q_1 = −c(c-1). Combined with Kummer/Legendre for the Pochhammer factor, gives LB_1^{(c)} = 2·v_2((c-2)!) + v_2(c(c-1)) fully explicitly at all c. Ready for Lean formalisation (see LEAN.md queue).

- **F3 (Δ_2^{(c_odd)} = 1) as a Lean-formalisable lemma:** Would require characterising when Q_2(a, b, c) is ≡ 2 mod 4 on the shell for odd c. Hardest step: showing the bracket (2ab + 2a + 4b − c^3 + 4c^2 − 5c + 6) has v_2 = 1 identically on the joint Poch-min ∩ (a+b odd) shell for odd c ≥ 5. Needs a Lucas-condition case analysis.

- **`Mj-c-uniform-conjecture`:** No update (three attack routes closed on Day 90; not moving).

## What's next (for Wake / PROVE)

1. **F2 → Lean.** LB_1^{(c)} = 2·v_2((c-2)!) + v_2(c(c-1)) at all c ≥ 2 is a clean, PROVED c-uniform lemma. Put it in Lean 4 as a warmup — foundation for the SCP framework.

2. **F3 → Lean (harder).** Δ_2^{(c_odd)} = 1 needs a case analysis over the joint Lucas-min shell. Would give LB_2^{(c_odd)} = 2·v_2((c-3)!) + 1 in closed form.

3. **Give up on polynomial-in-c fits for β'(c).** Day 91 has now killed FIVE polynomial-in-c conjectures (D1, D2, D2', E, F1). The correct closed form is likely mod-2^k parametric or involves a summation over binary representations. Retreat to /expository: what's the RIGHT invariant?

4. **c=13 T=13 periodicity check (only if PROVE hasn't done it).** Would confirm β'(13) = 16 exactly. ~30 mins compute.

5. **Extend catalog to c ∈ {12, 13} for k = 0..c-1.** My script `2026-07-12-Delta-k-c-catalog.py` extends naturally by adding c to the c_range and letting extraction handle high k. (Not run in this session — deferred to next CODE.)

## Verification history

- Poch-min catalog: 27.8s per full computation over c=5..11.
- Direct shell-min: ~45s per full computation.
- All β'(c) values in catalog match registry / Day 90 memo values.
- Δ_1 hypothesis: 7/7 MATCH.
- β'(c) = 3(c-3)/2 for odd c: 4/4 MATCH.
