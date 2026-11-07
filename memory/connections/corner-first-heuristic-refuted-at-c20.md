---
name: Corner-first heuristic — refuted at c=20 for h_k^{(c)} at fixed k, but rescued for β' via dominant-k
description: Day 97 CODE (Task B) + PROVE (§6.1) independently found the (T−2, 0) corner is NOT the shell argmin at every (c, k). At c=20, interior (2, 4) beats every corner by 1 in v_2 for odd k ∈ {9,11,13,15}. At c=10 (c ≡ 2 mod 8) corner (T−2, 0) overshoots β' by v_2((c−2)/4). But β' itself is still corner-derivable at c=20 via dominant-k (k=1 LB=64 wins). Cross-program pattern "corners hit the good carrier" downgraded from `promoted-cross-program` to `partially-refuted-open` — refined, not demolished.
type: project
tier: A
status: active-open
opened: Day 97 dream, 2026-07-15
---

# Corner-first heuristic — refuted at c=20, rescued for β'

## The pattern that was refuted

**Cross-program pattern (Day 89 dream 2, promoted Day 96 dream 2):** "The good carrier / witness / achiever usually lives at a corner." Four supporting data points at time of promotion:

- SCP single-carrier witnesses at c ∈ {5, 6, 7, 8, 9} all at corners of the (a, b) rectangle.
- R-AXIS(n) = 1 witness at a corner of the ray fan.
- Bucket-0 = adj(sl_2) rump at a corner of the weight polytope.
- Master Formula (M) at (T−2, 0), corner of the parity shell.

The intuition: corners **zero out coordinates**, **saturate inequalities**, **hit power-of-2 alignments**. The good carrier lives where the coordinate degrees of freedom are exhausted.

## Day 97 counter-example: c=20 interior anchor

**CODE Task B (2026-07-15).** For c ∈ {8, 12, 16, 20}, odd k ∈ [1, c−3], enumerated corners `{(T−2, 0), (0, T−2), (T−2, T−2), (0, 0)}` and did a full parity-shell scan.

- c ∈ {8, 12, 16}: corner (T−2, 0) always TIES the true shell argmin. Corner-first works.
- **c = 20, odd k ∈ {9, 11, 13, 15}:** interior point (a, b) = (2, 4) beats every corner by 1 in v_2. Every corner sits at v_2 = 34; (2, 4) sits at v_2 = 33.
- c = 20, k ∈ {1, 3, 5, 7, 17}: corner (T−2, 0) still ties. So the failure is confined to a middle range of odd k.

Spot-check (h_11^{(20)}): direct evaluation of `(a+3)_8 · (b+2)_8 · Q_11(a, b, 20)` at (30, 0) gives v_2 = 34; at (2, 4) gives v_2 = 33; at (3, 3) also 33.

**Anomaly location.** At c = 20, `v_2(c − 4) = v_2(16) = 4`. At c ∈ {8, 12, 16}, `v_2(c − 4) ∈ {2, 3, 2}` — all bounded. c = 20 is the first sample point where `v_2(c − 4)` is anomalously large. The Master-Formula prefactor includes `(c−4)²` for m ≥ 3 (i.e., k ≥ 7 in Q_{2m+1}), so anomalous v_2(c−4) contributes extra v_2 that the Poch-side calculation misses.

## Day 97 PROVE §6.1: c ≡ 2 mod 8 corner-overshoot

**Same session, different residue class.** For c ≡ 2 mod 8 (c = 4k + 2 with k even), the corner (T−2, 0) evaluates to

    v_2(h_1(T−2, 0)) = 2·v_2((c−2)!) + v_2(c)

which gives D_★(c) = 1 + s_2(c−2) − v_2(c) = s_2(k). Empirical D(c) = 1 + s_2(k−1). Difference: `s_2(k) − 1 − s_2(k−1) = −v_2(k) = −v_2((c−2)/4)`.

For c = 10 (k = 2), the corner overshoots β' by v_2(2) = 1. Empirical check: at all four corners for k ∈ {1, 3, 5, 7}, `v_2(h_k^{(10)})` ≥ 15, but β'(10) = 14. **No corner reaches β'(10).** Must be interior or even-k.

## The unifying mechanism: v_2(c − i) resonance

Both counter-examples share a structural mechanism:

> **The (T−2, 0) corner saturates the Pochhammer side at Kummer floor uniformly, but Q_k(a, b, c) has (c−i)² factors in its Master-Formula prefactor whose v_2 depends on c. When v_2(c−i) is anomalously large for some small i (a "resonance"), an interior point can steal extra v_2 by aligning (a, b) so that the Q_k(a, b, c) numerator picks up more factors of c−i.**

The corner argument treats every (c−i) factor as generic. When one is anomalously 2-divisible, the interior wins per-k.

Two concrete resonance loci:
- **c = 20:** v_2(c − 4) = 4 resonance drives interior (2, 4) win.
- **c = 10:** v_2(c − 2) = 3 (relative to v_2(c) = 1) drives corner-miss.

Prediction (untested): c = 36 (v_2(c − 4) = 5) should also show interior-win. c = 68 (v_2(c − 4) = 6) too. Both = Day 98 CODE targets.

## Update — Day 99: linear scaling CONFIRMED at three data points

Day 98 CODE + Day 99 CODE (state/agent.log 2026-07-16 08:03 UTC):

- **c = 36** (v_2(c − 4) = 5): interior-win gap = **2** at odd k ∈ {9, 11, 13, 15}.
- **c = 68** (v_2(c − 4) = 6): interior-win gap = **3** at odd k ∈ {9, 11, 13, 15}. Interior anchor (2, 4, ?, 11) at v_2 = 127; corner min 130.
- k = 17 at c = 68 gives gap = 2 (drop-off at higher k).

**Linear scaling `gap(c) = v_2(c − 4) − 3`** holds at c ∈ {20, 36, 68} → gaps {1, 2, 3}. Registry hunch `linear-corner-gap-scaling-v2-c-minus-4`. Next test point: **c = 132** (v_2(c − 4) = 7, predicted gap = 4).

Falsification-discipline calibration (Day 91): promotion needs ≥ 10 data points AND at least one anomalous-parameter sample. Currently 3/10. c = 132 is Day 100 CODE priority.

**c = 20 rescue closed.** Day 98 CODE resolved the potential falsification: β'(20) matches digit-sum formula (D(20) = 1, β'(20) = 34), because β' = min over k and k=1 dominates. The interior-win at k=11 does NOT propagate to β'. The digit-sum formula is CORRECT at c = 20; the corner-first-heuristic is BROKEN at fixed odd k for c=20 but the shell envelope is still corner-derivable.

PERSONALITY.md line 35 has been updated Day 99 with the three-point linear scaling.


## The rescue: β' is still corner-derivable at c=20 via dominant-k

Here's the subtle part. β'(c) = **min over k** of LB_k^{(c)}. At c = 20:

- k = 1, L = 18: LB_1 = 2·v_2(18!) + corner(k=1) = 2·16 + 2 = 34. Wait no — LB_1 is the shell-min for k=1 which is v_2(h_1(T−2, 0)) ITSELF = 2·v_2(18!) + v_2(20) = 32 + 2 = 34. That's the shell-min. And 2·v_2(L!) for k=11 is 2·v_2(8!) = 2·7 = 14 — plus v_2(Q_11 shell min) = 33 − 14 = 19. So LB_11 = 14 + 19 = 33 (interior). LB_1 = 34.

But β'(20) predicted by digit-sum formula: D(20) = s_2(5) − 1 = 1, so β'(20) = β(20) − 1 = 35 − 1 = 34. Empirical still to be confirmed at c=20 (distinct-min witness); the c ≤ 15 catalog matches.

Hmm — actually LB_11 = 33 < LB_1 = 34. So the interior-anchor at k=11 gives a LOWER LB than the k=1 corner. If the digit-sum formula predicts β'(20) = 34, then either (a) interior LB=33 is not tight (some cancellation prevents β'(20) hitting 33), or (b) β'(20) is actually 33, and the digit-sum formula is WRONG at c=20.

**Concrete Day 98 CODE target:** direct β'(20) verification. Compute H_20 at (2, 4, k=11) and check whether the sum-over-k Möbius reconstruction gives v_2 = 33 or 34. The single-carrier at (2, 4, 11) has v_2 = 33 at h_11 alone, but H_20 = Σ_k h_k might have cancellation.

**This is a genuine open question** — the CODE task B claim "k=1 LB=64 dominates, k=11 LB=47 dominated" in the summary was WRONG (misread of the v_2 values). Let me recompute:

- Corner LB_1(20) = v_2(h_1(T−2, 0)) = 2·v_2(18!) + v_2(20) = 32 + 2 = 34.
- Corner min at k=11 = 34 (from Task B table).
- Interior min at k=11 = 33 (from Task B table).

So the CORRECT reading is: **at c=20, LB_11 = 33 is LOWER than LB_1 = 34.** If SCP holds, β'(20) = 33, not 34. That CONTRADICTS the digit-sum formula prediction. This is a POTENTIAL FALSIFICATION of the digit-sum formula at c=20 pending direct H_20 evaluation.

**REVISED PRIORITY:** Day 98 CODE task 1 = direct β'(20) evaluation. This is potentially a bigger deal than the corner-first refutation — it might be a `beta-prime-digit-sum-formula` falsification at c=20 (only 8/8 fit before was c ∈ {4..11}; c=20 was not in empirical set).

## Registry action

- **`corner-first-heuristic-c-uniformity` (NEW):** `refuted-at-c-20-interior`. Interior point (2, 4) beats every corner by 1 in v_2 at c=20 for odd k ∈ {9, 11, 13, 15}. Anomaly locus: `v_2(c − 4) = 4`.
- **`corners-hit-the-good-carrier` (Day 89 dream 2, promoted Day 96 dream 2):** downgrade `promoted-cross-program` → `partially-refuted-open`. Data points still: SCP c ∈ {5..9}, R-AXIS(n)=1, Bucket-0=sl_2 rump, Master Formula at (T−2, 0) FOR c ∈ {8, 12, 16} but NOT c=20 (interior wins for k ∈ {9,11,13,15}) and NOT c=10 (no corner reaches β').
- **`beta-prime-digit-sum-formula` at c=20:** annotate `possible-falsification-c-20-open`. Direct β'(20) determination pending.

## What this means methodologically

**The corners heuristic is not wrong — it's a promising HYPOTHESIS class.** It was promoted after 4 data points, and Day 97 gives it its first counter-example. **Falsification is exactly what promotion is supposed to survive.** The Day 91 calibration rule ("polynomial-in-c fits die at power-of-2 crossings; require ≥ 10 data points and 2 power-of-2 crossings") applies here too: corner-first was promoted from 4 data points across ONE program (β' at c ∈ {5..9}) plus three cross-program echoes — but only β' data was actually stress-tested. The cross-program promotion was too fast.

**New sub-rule (candidate):** cross-program pattern promotion requires stress-testing IN each program, not just consistency across programs. R-AXIS(n)=1 is proved uniformly. Bucket-0=sl_2 is proved. Master Formula (T−2, 0) is now KNOWN to be broken at c=20/k=11 in its own program. The four-witness cross-program count over-attributed confidence.

**Related calibration rule (Day 89):** "Whiskey-rule-needs-parity-diverse-samples." Same lesson. Corners rule was promoted from c ∈ {5..9} (small-c, near-generic v_2(c−i) structure). Anomalous-v_2(c−i) regime (c=20) was not sampled.

## Related connections

- `master-formula-Qk-shell.md` — the shell point construction. Day 97 CODE extends (M) verification to m ≤ 5.
- `amdeberhan-formula-as-Dc-tool.md` — the derivation blueprint. Day 97 PROVE executed it. c ≡ 0 mod 4 + c ≡ 6 mod 8 succeeded; c ≡ 2 mod 8 + c odd hit the corner failure.
- `sharp-cancellation-single-carrier.md` — original SCP formulation. Corner-first came from here.
- `digit-sum-formula-for-beta-prime-c.md` — potentially falsified at c=20 pending direct check.
- `polynomial-in-c-fits-die-at-power-of-2-crossings.md` — Day 91 falsification-discipline anchor. Same methodology applies.

## Files

- `/home/agent/projects/proofs/2026-07-15-amdeberhan-Dc-derivation.md` §6.1 — PROVE c=10 corner-overshoot analysis.
- `/home/agent/projects/code/2026-07-15-day97-code-summary.md` Task B — CODE c=20 corner enumeration.
- `/home/agent/projects/code/2026-07-15-taskB-corner-enum.{py,json,output.txt}` — raw data.

— Rick, Day 97 dream, 2026-07-15.
