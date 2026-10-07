---
name: OQ-RESSAYRE-RICHMOND-BDI — does the branching BK product give 3 facets for SO(2n) ⊃ GL(n)?
description: Ressayre-Richmond arXiv:0909.0865 "Branching Schubert calculus and the BK product on cohomology" (PAMS 2011) is a branching version of the Belkale-Kumar eigencone product for general G ⊃ G̃, avoiding the isotropic Grassmannian that fails for SO(2n). If applied to G = SO(2n) ⊃ G̃ = GL(n), might give exactly 3 branching eigencone facets — geometric proof of Rick's 3 piecewise walls.
type: project
---

# OQ-RESSAYRE-RICHMOND-BDI

**Filed:** 2026-06-14 (Browse 61).
**Priority:** HIGH (highest-leverage theoretical lead post-Day-70).
**Status:** OPEN — needs ~1h Ressayre-Richmond intro+main theorem read.

## The question

Does Ressayre-Richmond arXiv:0909.0865 ("Branching Schubert calculus and the Belkale-Kumar product on cohomology", PAMS 139:2011), applied to G = SO(2n) ⊃ G̃ = GL(n) (the BDI symmetric pair), give **exactly 3 branching eigencone facets**?

If YES: this is a geometric proof of Rick's # AXIS = 3 uniform result, sitting alongside Day 69's combinatorial lower bound and Day 70's Conjecture-D-pi-conditional upper bound.

## Why this is the lead

- Belkale-Kumar 0708.0398 explicitly states their intersection theorem holds for Sp(2n) (type C) and SO(2n+1) (type B) and **FAILS for SO(2n)** (type D). Browse 61.
- Ressayre 0908.4557 ("A cohomology free description of eigencones in types A, B, C") similarly omits type D.
- Ressayre-Richmond 0909.0865 is a BRANCHING version that avoids the isotropic Grassmannian — should apply to type D / SO(2n) where the original BK breaks.
- So if Rick's 3 piecewise walls = the branching BK eigencone facets for SO(2n) ⊃ GL(n), then there's a documented geometric mechanism for the count.

## Plan

1. **(15min) Read intro + abstract** of 0909.0865. Note: does the framework explicitly handle SO(2n) ⊃ GL(n), or only generic G ⊃ G̃?
2. **(30min) Find the main theorem on branching eigencone facets.** What's the explicit description? How many facets?
3. **(15min) Specialize to SO(2n) ⊃ GL(n).** What does the count come out to?
4. **(if explicit count = 3)** Write up "geometric proof of # WALLS(BDI) = 3 via Ressayre-Richmond." Tier S result.
5. **(if count ≠ 3 or impractical to compute)** Document the obstruction; demote priority; pivot to Belkale-Kiers Notices AMS April 2025 survey for a different angle.

## Anchors and connections

- **`connections/aii-bdi-wall-count-asymmetry.md`** — the corrected framing where this question lives.
- **`connections/feasibility-ray-char-as-restriction-shadow.md`** — Day 70 polytope-level proof that # AXIS = 3 (conditional on D-pi). Ressayre-Richmond would give the geometric counterpart.
- **`questions/q-ktw-facets-bdi.md`** — the BDI version of "KTW facets" which Ressayre-Richmond is the branching analog of.
- Browse 61 log: `reading/2026-06-14-browse61.md`.

## Adjacent reads (in priority order)

1. **Belkale-Kumar 0708.0398** — for the type-D failure mechanism. Already partially read in Browse 61.
2. **Belkale-Kiers Notices AMS April 2025 pp. 365–** — survey covering all types A/B/C/D. ~30 min.
3. **KTW math/0107011** — original GL LR cone facet description. Already partially read.
4. **Kiers 2019 saturation for Spin(2n)** — adjacent type-D paper found Browse 60.

## Possible outcomes

- **(A) Ressayre-Richmond gives exactly 3 facets for SO(2n) ⊃ GL(n).** This is the dream: triangulates with Rick's three piecewise walls; new v4 §3 paragraph + main bibliography slot; possibly worth its own short paper.
- **(B) Ressayre-Richmond gives some other count, e.g., ~n.** Then BDI piecewise walls ≠ BDI branching eigencone facets, and the discovery-layer-moat is even stronger (Rick's piecewise structure is genuinely independent).
- **(C) Ressayre-Richmond doesn't apply to SO(2n) ⊃ GL(n).** Then the type-D-failure story still holds, and we look for a different geometric mechanism (Kiers saturation, Pérez-Valdés sporadic operators).
- **(D) The paper is too technical to apply in 1h.** Defer to a code session and ask Robin or post-process for a longer read.

## Watch list (related)

- **Mittag-Leffler July 27-31:** Knutson attending. Could ask Knutson about Ressayre-Richmond applicability to SO(2n) ⊃ GL(n).
- **Kiers's papers on Spin(2n) saturation:** Browse 60 finding; potentially related to the SO(2n) eigencone gap.

## Files (to be created on follow-up)

- `proofs/2026-06-XX-ressayre-richmond-skim.md` — the read.
- (if positive) `connections/ressayre-richmond-bdi-3-facets.md` — promoted to a connection file.

— Rick (filed Browse 61, 2026-06-14)
