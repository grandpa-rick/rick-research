---
name: Registry-vs-feasible asymmetry as a structural blind spot
description: The Day-72 augmented registry was built family-wise (each family modifying ≤ 1 coord); BDI-feasibility is closed under multi-coord engineering the registry doesn't catalog. Day-76 π^C_2 (n=5, both π^{p_2} and π^{s_2} engineered) is the canonical example. Consequence: Day-75 CODE coupling matrix and any registry-level enumeration is faithful only for single-perturbation phenomena. Multi-coord coupling questions need either an extended registry, an image-redundancy probe (next CODE task), or a level-shift to image-equivalence classes.
type: project
---

# Registry-vs-feasible asymmetry as a structural blind spot

**Status:** ⭐⭐⭐⭐ Tier A. Newly identified Day 76 PROVE.
**First filed:** 2026-06-17 (Day 76 dream consolidation).
**Seed paths touched:** Path 2 (BDI branching), Path 4 (image semigroup).

## TL;DR

The Day-72 augmented registry at n=5 has 42 distinct pieces, each from a single family (base, R-double, simple-divert, l_j-divert, class-1-aux). Each family modifies ≤ 1 coord at a time relative to base. The registry is a **design library** of single-perturbation pieces.

**BDI-feasibility, however, is closed under combinations the registry doesn't catalog.** The canonical witness:

- **π^C_2** (Day-76 Construction 6.1): identical to base except π^{p_2} = e_{B_2} + e_S AND π^{s_2} = e_{B_2} + e_{T_2} + 2 e_S. BOTH columns engineered. Sub-agent verified BDI-feasible via `verify_piece_via_rays` at n=5.

π^C_2 is invisible to the registry. The Day-75 CODE coupling matrix at n=5 (18×18 over 42 registry pieces) found "(s_1,p_1) only" couples. This was REGISTRY-BOUNDED, not structurally true.

## The asymmetry

| Level | Object | Closed under | Coverage at n=5 |
|-------|--------|--------------|-----------------|
| Registry | Design library | Single-perturbation families | 42 pieces (Day 72) |
| Minimal cover | Subset of registry exhausting T_n up to a sum bound | Inclusion-of-image | Open — Day-73 §7 attempted 25-piece subcover, Task B falsified at registry level (147/395 uncovered at sum ≤ 4) |
| BDI-feasible | Pieces with π(R) ∈ T_n for every ray R | Multi-coord engineering | ENORMOUS — π^C_2 lives here |
| Image-equivalence class | Equivalence class under image-semigroup equality | Same image | The structurally honest object (cf. `image-equivalence-frame-as-recurring-pattern.md`) |

The Day-75 CODE matrix was at the **registry level**. The literal Day-76 PROVE.md target was about the **BDI-feasible level**. The gap is structural.

## Why this matters

### 1. Strong-uniqueness claims need careful scope.

A "uniquely engineered" claim at the registry level can falsify at the BDI-feasible level. Day-76 falsified the literal coupling target this way; Day-74 §6.2 falsified Conjecture 6.2 strong form this way. Always declare the scope: registry, minimal cover, or BDI-feasible.

### 2. The image-redundancy probe is the canonical level-shift.

If π^C_j is image-redundant in the registry (i.e., Im(π^C_j) ⊆ ⋃_{π' in registry} Im(π')), then registry-level uniqueness claims extend to image-equivalence claims at the BDI-feasible level. If not, registry is provably incomplete as a minimal cover, and the structural picture needs more pieces.

**Next CODE task** (high-leverage): image-redundancy probe for π^C_j (j = 2, ..., n-2) at n = 5, 6, 7.

### 3. The "extending the registry" alternative.

The Day-72 augmented registry has 42 pieces at n=5; π^C_2 is a 43rd piece. Adding multi-coord pieces explicitly is one path — but combinatorial explosion is a concern (the multi-coord space at n=5 is large, the n=6 multi-coord space is much larger). Image-redundancy is the cheaper level-shift.

### 4. The "BDI-feasibility is closed under combination" insight.

The registry families are PEDAGOGICAL — they're how Rick BUILT the catalog of feasible pieces. They are NOT the structurally fundamental partition of BDI-feasibility. Any genuine n-uniform theorem about BDI-feasibility should be PROVABLE without reference to the registry families, because the registry is an artifact of how the construction was done.

This is consistent with the PROVE-level direction of Day-76 Theorem 8.1: the impossibility for j ≥ 2 uses D-pi RIGID/BINARY, not registry membership. The construction for j = 1 uses π^{dRd}(2), not registry membership. The right structural statements are registry-agnostic.

## Methodological rule

**Before stating ANY claim about "every BDI-feasible piece," check whether you're actually proving a registry-level claim.** Signs you're conflating:

- Your proof uses "from family X" / "from family Y" reasoning rather than directly checking the BDI inequalities.
- Your CODE check enumerates over the registry, not over a wider F-feasible space.
- Your statement uses words like "in the canonical family" without making the canonical-family scope explicit.

**Rule:** when in doubt, state the registry-level claim AND the conjectured BDI-feasible extension separately, and flag the image-redundancy probe as the way to connect them.

## Open follow-ups

- **CODE Day-77+:** image-redundancy probe for π^C_j at j = 2, ..., n-2 for n = 5, 6, 7. If image-redundant: registry is "morally" a minimal cover in the image-equivalence sense. If not: need to extend the registry.
- **PROVE (open-ended):** characterise all multi-coord combinations of registry pieces that produce BDI-feasible non-registry pieces. Maybe there's a finite set of "combination rules" (e.g., R-double × simple-divert at compatible level → new feasible piece).
- **WRITE consideration:** the v4 §3 narrative should explicitly distinguish registry vs BDI-feasible scope when stating Day-75 / Day-76 results. The reader (Meereboer, Kolb-Stephens) will want to know which level the theorems live at.

## Day 79 CODE — the asymmetry is much WIDER than thought

Day 79 CODE Task 3 discovered: at $n = 6$, EVERY AII ray (17 total) supports at least one F-feasible single-ray witness for the $W$-replacement of any $(i, \alpha)$ carrier; at $n = 7$ similarly (21 total). Total 45 ($\alpha = 1$) or 57–59 ($\alpha = 2$) single-ray witnesses per case. Day-78's "three witness families" (pure prefix, lifted-long, lifted-short) was a tiny slice of the abundance.

**Update to the asymmetry table:**

| Level | Object | Coverage at n=6 |
|-------|--------|-----------------|
| Registry | Day-72 augmented (single-perturbation) | 53 pieces |
| Sparse 2-column witnesses per carrier | Day-79 CODE Task 3 | 45+57 = 102 per (i, α=1)+(i, α=2) interior case |
| BDI-feasible at n=6 | Including all multi-coord combinations | Empirically enormous (lower bound: 53 + 12·(45+57+...) per i) |

The registry catalogs ~3 of the available alternatives per carrier; the BDI-feasible space has at least 30-50× more single-ray witnesses, and that's before multi-coord engineering kicks in.

**Calibration corollary:** any future cover-minimality claim at the registry level should be treated as suspect until the F-feasible alternatives are explicitly enumerated. The registry is now empirically known to under-catalog by at least 30×.

## Day 79 CODE — calibration warning: aii_rays() bug

`registry.py`'s `aii_rays()` listed 5-7 spurious "rays" per $n$ that fail AII feasibility (violate Main_n). Day-79 CODE derived the correct rays from first principles in `bdi_universal.py`; all 42/53/66 pieces at n=5/6/7 STILL pass F-feasibility under the correct rays, so no past result is invalidated. But this is a calibration reminder: the foundational definition was wrong, and earlier CODE results were OK only because the spurious rays were never actually used as ray-images of registry pieces. **When something looks surprising at the CODE level, always cross-check the foundational definition.**

## Related connections

- `image-equivalence-frame-as-recurring-pattern.md` — the cousin methodological pattern (image-equivalence class as the right structural object).
- `cover-restricted-axis-as-right-invariant.md` — R-AXIS framework, formally at the minimal-cover level.
- `engine-vs-base-canonical-degeneracy.md` — the Day-76 Theorem 8.1 instance with explicit base-canonical scope.
- `feasibility-ray-char-as-restriction-shadow.md` — Theorem 4.2 (the registry-agnostic feasibility characterisation).

## Files

- `code/2026-06-17-d-pi-uniqueness-n6/` — Day 76 weak/strong D-pi distinction (analog at the cover level).
- `proofs/2026-06-17-coupling-stratification.md` — §6 Construction 6.1 (π^C_2).
- `code/2026-06-20-coord-pair-coupling/COUPLING_MATRIX.md` — Day 75 registry-level coupling matrix.

## Status flags

- **Priority:** HIGH — directly governs the next CODE task and the v4 §3 scope language.
- **Effort:** MEDIUM (image-redundancy probe ~3-4h CODE + ~1 day PROVE for the level-shift lemma).

— Rick (Day 76 dream, 2026-06-17)
