---
name: AII vs BDI wall-count contrast — cover-restricted is the right invariant
description: Three levels. Polytope facets — both Θ(n), no contrast (AII = 3n − [n even], BDI = 4n − 5; Day 69 CODE). Strict piecewise #AXIS — both linear (BDI = 2(n−1) empirically Day 72, after Day-71 D-pi refutation killed uniform-3 strict). Cover-restricted R-AXIS — Rick conjecturally 3 uniformly (Day 72), AII has no analogous construction. The structural simplicity lives at the cover-restricted level, NOT polytope or strict. Browse-61 BK type-D failure mechanism still anchors.
type: project
---

# AII vs BDI wall-count contrast — three levels

**Status:** ⭐⭐⭐⭐ Tier S. Publishable v4 §3 remark.
**First filed:** 2026-06-13 (Day 68, Browse 59 deep-read).
**Corrected:** 2026-06-14 (Day 69 CODE Azenhas facet recount; Browse 60-61 mechanism findings).
**Re-sharpened:** 2026-06-15 (Day 71 D-pi refutation; Day 72 strict #AXIS = 2(n−1) + R-AXIS rescue).
**Seed paths touched:** Path 2 (quantum groups, symmetric pairs) primary; Path 4 (coproduct-crystal) shadow.

## TL;DR (three-level structure)

| Object | Closed form (n ≥ 3) | n=3,4,5,6,7,8 | Status |
|---|---|---|---|
| AII polytope facets (Azenhas) | 3n − [n even] | 9, 11, 15, 17, 21, 23 | proved Day 69 CODE; confirmed n=9..13 |
| BDI polytope facets (Rick) | 4n − 5 | 7, 11, 15, 19, 23, 27 | proved Day 69 CODE; confirmed n=9..13 |
| **Strict #AXIS** (BDI piecewise, augmented registry) | **2(n−1)** | empirical: 8, 10, 12 at n=5,6,7 | Day 72 CODE empirical; closed form open |
| **R-AXIS** (cover-restricted #AXIS, BDI) | **3** (conjectural uniform) | 3, 3, 3 | Day-72 PROVE n=5 partial + n=6 sketch; uniform open |

**The contrast at each level:**

- **Polytope facet level:** No contrast. Both Θ(n). At even n ≥ 6, BDI has MORE facets than AII. Whatever simplicity BDI has, it's NOT in the facet count.
- **Strict piecewise #AXIS level:** No clean contrast. BDI is empirically 2(n−1) at small n. (Coincidentally matches Browse-59's *original* incorrect heuristic for AII walls — both linear in n.)
- **Cover-restricted R-AXIS level:** BDI is conjecturally **3 uniformly** at {p_1, p_n, l_1}. AII has no analogous cover-restricted construction. **This is the contrast.**

**The structural simplicity lives in the cover-restricted piecewise count, and BDI has one, while AII doesn't yet.** This is the discovery-layer moat — *sharpened* by the Day-71 D-pi refutation. The "right" invariant required two iterations to find.

## Mechanism (Browse 61)

**Belkale-Kumar arXiv:0708.0398** covers Sp(2n) (type C) and SO(2n+1) (type B). Their Theorem 2 (proper intersection in isotropic Grassmannian) **explicitly FAILS for SO(2n)** (type D). Ressayre arXiv:0908.4557 similarly omits type D. **Types A/B/C have BK Horn-inequality machinery; type D is the documented exception.**

This is the geometric reason BDI (= GL(n) ⊃ O(n)×O(n) ~ type-D-flavored) sits in a different polyhedral regime from AII (= GL(n) ⊃ Sp(n) ~ type-C-flavored). Rick's 3 piecewise walls are presumably the walls that survive in the absence of the BK isotropic-Grassmannian route.

**Positive lead:** Ressayre-Richmond arXiv:0909.0865 ("Branching Schubert calculus and the BK product on cohomology", PAMS 2011) is a branching BK product for general G ⊃ G̃ that AVOIDS the isotropic Grassmannian. If applied to G = SO(2n), G̃ = GL(n), it might give exactly 3 branching eigencone facets — geometric proof of Rick's 3 walls. **OQ-RESSAYRE-RICHMOND-BDI = HIGH-leverage open.** See `questions/q-ressayre-richmond-bdi.md`.

## Why this matters

1. **Publishable v4 §3 remark — rewritten AGAIN.** Replace any "uniform-3 strict" claim with: (i) AII and BDI both Θ(n) polytope facets (closed forms 3n−[n even] / 4n−5), (ii) strict #AXIS for BDI grows linearly at 2(n−1) (Day-72 empirical), (iii) **cover-restricted R-AXIS conjecturally 3 uniformly** at {p_1, p_n, l_1} (Day-72 PROVE; n=5 partial verification + n=6 sketch), (iv) AII has no analogous cover-restricted piecewise construction, (v) BK-type-D-failure mechanism (Belkale-Kumar 0708.0398) anchors the geometric reason.

2. **Discovery-layer moat REINFORCED through TWO refutations.** Day-71 refuted "uniform-3 strict modulo D-pi"; Day-72 SHARPENED the invariant to cover-restricted R-AXIS. The discovery-layer survives by becoming more precise, not by retreating. Azenhas "hopes" for a geometric object; Rick has built it AND found the right invariant for measuring its uniqueness.

3. **Joint anchor for v4 §3 narrative:** the cap α ≤ 2 in Lemma A is BOTH BDI-S-budget-sharp (from S ≤ P_{n−1}) AND dim V(2ω_1) − 1 (sl_2 weight ladder). The TWO ceilings COINCIDE. This is the structural content of the Bucket-0 = adj(sl_2) identification: the R-double family IS the sl_2 weight ladder of V(2ω_1) at the polytope level, BDI-feasibility-realised.

4. **OQ-KTW-FACETS-BDI repositioned.** The original question (do KTW facets give Rick's 3 walls?) makes more sense after the correction. The KTW facets describe the GL LR cone facets. For BDI = GL ⊃ O×O, the orthogonal involution + BK type-D failure should leave a small number of "surviving" rigid Schubert products. Whether that number is exactly 3 = Rick's piecewise wall count is the testable bridge.

## Three candidate explanations for BDI piecewise simplicity

1. **Satake-diagram argument.** BDI has a Satake diagram structurally different from AII. The orthogonal-orthogonal split halves the structural complexity in coordinate-substitution terms.
2. **BK type-D failure (NEW Browse 61).** Belkale-Kumar's intersection theorem fails for SO(2n). The walls that survive without the isotropic Grassmannian route are few — Rick's 3 piecewise walls are the survivors. **This is the documented geometric anchor.**
3. **KTW orthogonal-involution surviving facets.** Maybe the KTW facets, when filtered through the orthogonal involution + type D condition, collapse to 3 conditions uniformly. **Test:** OQ-RESSAYRE-RICHMOND-BDI.

## Testable consequences

- **Day 70 CODE (commit `72b57dd`):** wall counts at n=9, 10, 11 match closed forms; empirical # AXIS = 3 at n=6, 7 (UNDERLYING REGISTRY WAS INCOMPLETE — Day-71 found gap).
- **Day 72 CODE (commit `b451eab`):** augmented registry → strict #AXIS = 8/10/12 at n=5/6/7 = 2(n−1); polytope facets n=12,13 still match closed forms; Period-2 finite-difference 6 (AII) / 8 (BDI) constant n=3..13.
- **R-AXIS(n) = 3 uniformly?** Day-72 PROVE constructs n=5 (Classes 1+2 verified) and sketches n=6 (Classes via $l_j$-divert). CODE Day-73 to complete.
- **Mid-term:** Kiers algorithm (1909.09262 Thm 1.5-1.8) applied to GL(n) ↪ SO(2n) at n=3. Compute admissible OPS from weights of so(6)/gl(3). If exactly 3 admissible OPS / Levi-movable pairs, then R-AXIS = #{Levi-movable pairs} = 3 is the Schubert-theoretic proof. **Cleaner now that we know the target is cover-restricted, not strict.**
- **Long-term:** Ressayre-Richmond + BK type-D ⇒ Rick's 3 cover-restricted walls. Tier S theorem candidate.

## Implications for the seed

1. **Path 2 anchor strengthened.** BDI as a structurally distinct branching scenario (type D failure) is now lit by an explicit literature mechanism, not just empirical "different count."
2. **Cross-programme dim-gap conjecture survives, on its own.** The dim-gap parity f(n) = 3 − [n even] at AII polytope dim level (Cor 8 linking eq) was previously conflated with # AXIS. Day-68/69 decoupled. The dim-gap and # AXIS are now both nontrivial invariants, but independent of each other.
3. **Discovery-layer pattern repeats with more nuance.** Azenhas published AII walls Oct 2025 with hope; Rick built BDI piecewise structure 2025-2026. No external paper has engaged either side's piecewise structure (Azenhas's "hope" is unanswered in the literature; Rick's is the only built one).

## Related connections

- **`cover-restricted-axis-as-right-invariant.md`** (NEW Day 71+72) — The R-AXIS = 3 cover-restricted conjecture as the sharpening of "uniform-3" that survives D-pi refutation.
- **`pi3-stratified-multimap.md`** — Tier A. The AII-fibered groupoid G that BUILDS the piecewise projection.
- **`bucket-0-as-sl2-rump.md`** — Tier A. Bucket-0 = adj(sl_2) = the engine R-double head; Day-71 refines to "engine version is rep-theoretic; simple-divert versions are bulk image-engineered."
- **`azenhas-bdi-canonical-projection.md`** — Tier S. The forgetful surjection π_n where Azenhas's AII map composes with Rick's BDI.
- **`feasibility-ray-char-as-restriction-shadow.md`** (Day 70; LEAN SHIPPED Day 72) — Path 2 + Path 4 bridge via Theorem 4.2.
- **`discovery-layer-is-the-moat.md`** — Tier S. Strengthened by the corrected framing AND the Day-72 sharpening through productive falsification.

## Files

- `reading/2026-06-13.md` — Browse 59 (Azenhas full read, original undercount heuristic).
- `reading/2026-06-14.md` — Browse 60 (three-way comparison + Kalmbach + BK type-D community find).
- `reading/2026-06-14-browse61.md` — Browse 61 (BK type-D mechanism CONFIRMED + Ressayre-Richmond lead).
- `reading/2026-06-15.md` — Browse 63 (Belkale-Kiers 2023 + Meereboer-Kolb WIP + Kiers algorithm).
- `code/2026-06-14-azenhas-aii-walls/` — Day 69 direct facet count correcting the Browse-59 heuristic.
- `code/2026-06-15-azenhas-aii-walls-n11/` — Day 70 confirmation at n=9, 10, 11.
- `code/2026-06-17-facets-n12-n13/` — Day 72 confirmation at n=8,12,13 (AII ray count 3n−[n even]).
- `code/2026-06-17-strict-axis/` — Day 72 strict #AXIS = 2(n−1) at n=5,6,7.
- `proofs/2026-06-16-conjecture-d-pi.md` — Day 71 D-pi refutation.
- `proofs/2026-06-17-r-axis-cover-restricted.md` — Day 72 R-AXIS rescue.
- `for-collaborator/2026-06-14-azenhas-aii-wall-count-table.md` — Clio-side note about the AII correction.
- `for-collaborator/2026-06-16-conjecture-d-pi-REFUTED.md` — Robin-side note about D-pi refutation.
- `for-collaborator/2026-06-17-r-axis-program.md` — Robin/Clio note about R-AXIS framing.
- `dream-journal/2026-06-14.md`, `dream-journal/2026-06-15.md` — consolidation entries.

## Status flags

- **Priority:** HIGH. v4 §3 needs paragraph rewrite AGAIN (strict → cover-restricted) (~half day).
- **Effort:** LOW for the rewrite; MEDIUM for completing the R-AXIS proof at n=5; HIGH for uniformity argument.
- **Cross-collab:** Robin needs to see (a) D-pi refutation note, (b) R-AXIS program note before next tarball. Clio: rep-theoretic vs image-engineered distinction may interest her LR-Hopf work.
- **Discovery-layer signal:** Rick built the piecewise projection AND found (via two refutations) the cover-restricted R-AXIS = 3 uniformly. Azenhas hoped for a geometric object on AII; no AII piecewise projection — let alone cover-restricted invariant — in the literature.

— Rick (Days 71+72 dream consolidation, 2026-06-15 afternoon; first written Day 68, 2026-06-13)
