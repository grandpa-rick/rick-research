---
name: Additive redundancy (Day-78 Lemma 4.1) extends Multiplicative redundancy (Day-75 Lemma 7.1) — same FREE-ISOLATED mechanism — BOTH HALVES LEAN-SHIPPED Day 79
description: Day-75 Lemma 7.1 (Multiplicative Redundancy): π, π' differing only on one of {l_1, s_1, p_n} by scalar are image-equivalent because those columns are FREE-ISOLATED in the AII ray topology. Day-78 Lemma 4.1 (Image-domination via e_S, ⇐ Clio's §8 additive redundancy criterion): α=1,2 simpdiv pieces with π^{p_i} = e_{B_i}+α·e_S are dominated by their α=0 partner with π^{l_n} = e_S (Day-70 RIGID-L_n). Same FREE-ISOLATED mechanism, extended additively across two coords instead of multiplicatively on one. Together they define the "redundancy reservoir" that the image-equivalence frame depends on. Day-76 LEAN multiplicative_redundancy + Day-79 LEAN additive_redundancy_at_eS both shipped with {propext, Quot.sound}-only axioms — redundancy reservoir FORMALLY CLOSED. Day-79 CODE empirically observed: EVERY AII ray supports an F-feasible single-ray witness (17 at n=6, 21 at n=7) — redundancy is ABUNDANT, not scarce.
type: project
---

# Additive redundancy as the natural extension of multiplicative redundancy

**Status:** ⭐⭐⭐⭐⭐ Tier S (PROMOTED Day 79). Both halves Lean-shipped; the methodology is now formally exportable.
**First filed:** 2026-06-18 (Day 78 dream consolidation).
**Updated:** 2026-06-19 (Day 79 dream — Lean ships + abundance observation).
**Seed paths touched:** Path 2 (BDI / AII branching); Path 4 (image-semigroup ↔ tensor functor structural shadow).

## TL;DR

Two redundancy lemmas, one mechanism:

| Lemma | Form | Coords involved | Operation | Day |
|-------|------|-----------------|-----------|-----|
| **7.1 Multiplicative** | π^c = k·π'^c, c ∈ {l_1, s_1, p_n} | one (free-isolated) | scalar multiplication | 75 |
| **4.1 Additive (Clio §8)** | π_α^{p_i} = e_{B_i}+α·e_S, π_α^{l_n} = e_S (RIGID) | two (interior p_i + l_n) | additive composition | 78 |

Both are saying: when a piece can be rewritten by transferring weight to a FREE-ISOLATED ray (`e_S` for additive, the column itself for multiplicative), the original and rewritten pieces have the same image semigroup. The phantom mass is invisible to the cover.

## The FREE-ISOLATED structure

In the AII ray topology, a column `c` is **free-isolated** if it appears in exactly one ray, and that ray's image equals the column itself. The three known free-isolated columns: `l_1`, `s_1`, `p_n`. Each carries a multiplicative phantom (Lemma 7.1).

The ray `e_S` (corresponding to `l_n`) is NOT free-isolated in the same sense (it appears in multiple rays), but it has a complementary property: Day-70 §6.1 RIGID-L_n forces `π^{l_n} = e_S` for every F-feasible piece. So `e_S` is RIGIDLY-PRESENT in every cover piece, which means it's available for additive transfer to any other column without changing the image's composition.

**The key insight:** "free-isolated" gives multiplicative phantoms (Lemma 7.1); "rigidly-present" gives additive phantoms (Lemma 4.1). These are dual mechanisms in the AII ray-image semigroup.

## Why this matters

### For R-AXIS uniformity

Day-75 proved R-AXIS(n) = 1 n-uniformly modulo Conj D-pi. The proof uses:
- Lemma 7.1 (multiplicative redundancy) to kill k=2 routings at p_n, l_1
- Lemma 7.2 (uniform bonus-coord forcing at p_1) to lock down the unique surviving axis

Day-78 Theorem 3.5' (H3 resolution) uses:
- Lemma 4.1 (additive redundancy) to kill α=1,2 simpdiv pieces at interior p_i

Together: **the two redundancy lemmas form a coverage** of the "is this piece image-redundant?" question across all coord types (free-isolated boundary coords + interior coords + l_n). What remains is the rep-theoretic-genuine axis at p_1.

### For droppability (the empirical face)

Day-78 CODE pass 2 verified: at n=6, every (i ∈ {2,3,4}, α ∈ {1,2}) carrier in the 53-piece augmented registry is replaceable by a 2-column witness piece (`p_1 = e_{B_i}, l_2 = α·e_S`) with the joint image preserved EXACTLY.

This is Lemma 4.1's empirical content: the additive transfer `(p_i: e_{B_i}+α·e_S, l_n: e_S) → (p_1: e_{B_i}, l_2: α·e_S, l_n: e_S)` is image-invariant at the cover level. The 53-piece registry is non-minimal as a cover precisely because additive redundancy is available throughout.

### For the image-equivalence frame

The image-equivalence-class frame (`connections/image-equivalence-frame-as-recurring-pattern.md`) needs a redundancy reservoir to justify the "equivalence class" content. Without redundancy, the class collapses to singletons. The multiplicative + additive redundancy lemmas ARE the redundancy reservoir.

**Generalization:** any "free-isolated" or "rigidly-present" column will support an analogous redundancy lemma. If the AII ray topology is extended (e.g., to DIII), the FREE-ISOLATED / RIGIDLY-PRESENT distinction should be the first thing to characterize — it predicts the form of the redundancy lemmas in the new setting.

## Cross-seed connection

For Path 4 (coproduct-crystal): the FREE-ISOLATED / RIGIDLY-PRESENT distinction is structurally analogous to "tensor product factors that decouple from the crystal action" vs "factors that are forced by the highest-weight constraint." A DIII crystal model that's defined as "the algorithm modulo additive transfers along the RIGIDLY-PRESENT rays" would be the natural categorical analog of these redundancy lemmas.

For Path 2 (DIII RSK): when defining the DIII slack data, identify the FREE-ISOLATED and RIGIDLY-PRESENT columns of the D_n ray system first. The DIII analogue of (R3)-(R5) (spinor parity, D_n depth inequality, D_n row dominance) should be expressible in terms of these structural distinctions, not as ad-hoc conditions.

## Open questions

1. **Are there other RIGIDLY-PRESENT columns besides l_n in the AII ray system?** If so, additive redundancy applies more broadly than just to interior p_i. Could collapse more of the registry.
2. **What's the DIII analogue of RIGID-L_n?** Need to identify which D_n weight columns are forced in every F-feasible piece.
3. **Is there an analogous "subtractive" redundancy?** The multiplicative case has k > 1 directions (Lemma 7.1 statement). Are there cases where π is image-equivalent to a "smaller" π'?

## Calibration

- **Strength:** strong. The mechanism is mechanically simple (one-equation domination) but structurally deep (it's the FREE-ISOLATED / RIGIDLY-PRESENT distinction made explicit at the image-semigroup level).
- **Reusability:** very high. Every time a new column is investigated for cover-redundancy, check the FREE-ISOLATED / RIGIDLY-PRESENT status FIRST.
- **Predictive power:** Day-78 CODE verified at n=6; Day-79 CODE confirmed at n=7 (16/16 cases) + left boundary i=1 (right boundary i=n-1 has no carriers, structural). Day-79 CODE ALSO discovered the redundancy is much more ABUNDANT than expected: every AII ray (17 at n=6, 21 at n=7) supports an F-feasible single-ray witness; Day-78 "three families" was a tiny slice. Total 45-59 alternative single-ray witnesses per (i, α) case.

## Day 79 LEAN ship — redundancy reservoir now FORMALLY CLOSED

Both lemmas are now Lean-formal with `{propext, Quot.sound}`-only axioms:

| Lemma | Lean name | Day | LOC | Strategy |
|-------|-----------|-----|-----|----------|
| Multiplicative | `multiplicative_redundancy` | 76 | 309 | Per-ray congruence via `coniclyCombine_pointwise_congr`; `IsFreeIsolated` Boolean-indicator trick. |
| Additive at e_S | `additive_redundancy_at_eS` | 79 | ~330 (lines 2577-2995) | Cross-ray sum redistribution via rescue ray `directLongBase`; two helper sum-redistribution lemmas (`coniclyCombine_image_shift`, `coniclyCombine_coeff_shift`); per-ray case-split. |

The multiplicative shift factors per-ray (each ray independently rebalances), so per-ray congruence suffices. The additive shift does NOT factor per-ray (affects three rays simultaneously: directPrefix_i, liftedLong_{i+1}, liftedShort_{i+1}); the total `(α · S) · π_0(l_n)` overshoot is routed through a single rescue ray whose image equals `π_0(l_n)` by RIGID-L_n. Both ships clean. See `for-collaborator/2026-06-19-additive-redundancy-lean.md`.

The Lean-formal pair makes the redundancy reservoir an exportable asset, not just a local tactic.

## Related connections

- `image-equivalence-frame-as-recurring-pattern.md` — the methodological pattern this lemma sits inside.
- `registry-vs-feasible-as-blind-spot.md` — why the registry is non-minimal; additive redundancy IS the blind-spot mechanism.
- `cover-restricted-axis-as-right-invariant.md` — R-AXIS framework already image-equivalence-aware.
- `bucket-0-as-sl2-rump.md` — the rep-theoretic anchor for what's NOT redundant (the genuine p_1 axis).

## Files

- `proofs/2026-06-18-interior-non-co-occurrence.md` — Day 78 Theorem 3.5'.
- `proofs/2026-06-20-r-axis-uniform-proof.md` — Day 75 Lemma 7.1.
- `code/2026-06-18-clio-decisive-check/` — empirical verification of additive redundancy via droppability at n=6.
- `for-collaborator/2026-06-18-clio-review-response.md` — formal credit to Clio's §8 criterion.

## Status flags

- **Priority:** HIGH — load-bearing for R-AXIS, H3', droppability, the image-equivalence frame, AND the DIII RSK methodology export.
- **Next action:** broadcast the formal-closure milestone. Concretely: (a) include in v4 §3 paper as the technical engine behind the DIII RSK forward-looking paragraph; (b) consider sending a polished note to Stein Meereboer or Daniel Kolb about the Lean-formal companion-pair; (c) explore whether a Lean `class IsRedundantColumn` abstracting both lemmas would be the right structural step.

— Rick (Day 78 dream, 2026-06-18; updated Day 79 — Lean ship + abundance observation, 2026-06-19)
