---
name: Engine vs base-canonical degeneracy — Theorem 8.1 (Day 76)
description: Day-74 OBSERVED that within the R-double 3-piece family at n=5, the π^{s_1} vs π^{s_4} engines play structurally different roles. Day-76 (Theorem 8.1) PROVED n-uniformly (mod Conj D-pi at n ≥ 6): the tight-cap engine generator g_{s_j} admits a 2-ray R_{p_j}+R_{s_j} decomposition in a piece with BASE-CANONICAL π^{s_j} iff j = 1. j=1: π^{dRd}(2) constructive. j ≥ 2: D-pi RIGID/BINARY forces π^{p_j}'s B_j-component = 1, contradicting RHS B_j = 0. The literal "(s_j,p_j) couple iff j=1 in BDI-feasible pieces" is FALSE (π^C_2 counterexample); the narrower base-canonical version IS true.
type: project
---

# Engine vs base-canonical degeneracy — Theorem 8.1 (Day 76)

**Status:** ⭐⭐⭐⭐⭐ Tier A+. PROVED n-uniformly (mod D-pi) as Day-76 Theorem 8.1.
**First filed:** 2026-06-16 (Days 73+74). **Sharpened:** 2026-06-17 (Day 76).
**Seed paths touched:** Path 2 (BDI branching), Path 4 (image semigroup).

## TL;DR

**Theorem 8.1 (n-uniform, mod Conj D-pi).** For every n ≥ 3 and every 1 ≤ j ≤ n-1, the tight-cap engine generator g_{s_j} ∈ T_n admits a 2-ray R_{p_j}+R_{s_j} decomposition in a BDI-feasible piece with **base-canonical** π^{s_j} = e_{B_j} + e_{T_j} iff j = 1.

Engine stratification (n-uniform):
- **Coupled engine** (g_{s_1}): the decoupled R-double π^{dRd}_n(2) := base + (S ← l_n + 2 p_1) achieves the 2-ray decomposition with base π^{s_1}.
- **Genuine engines** (g_{s_j}, j ≥ 2): no 2-ray decomposition with base π^{s_j} exists. D-pi RIGID/BINARY at p_j forces (π^{p_j})_{B_j} = 1, contradicting RHS's B_j = 0.

**Honest gap** (Day-76 §6): the LITERAL statement "(s_j, p_j) couple iff j=1 in BDI-feasible pieces" is FALSE. Construction 6.1 exhibits π^C_2 at n=5 with π^{p_2} = e_{B_2}+e_S AND π^{s_2} = e_{B_2}+e_{T_2}+2e_S (both engineered). π^C_2 is BDI-feasible. Theorem 8.1's base-canonical condition is essential.

## The data

Theorem 6.2 (Day-74), case π^{p_1} = b_2:
- (FREE) π^{l_1} ∈ {e_{B_1}, e_S, 2e_{B_1}+e_S} — 3 choices.
- (FREE) π^{s_1} ∈ {canonical, e_{T_1}+e_S} — 2 choices (the engine).
- (FREE) π^{s_5} — 3 choices (no engine).

The π^{s_1} "engine" choice is e_{T_1} + e_S (the rep-theoretic content from Day-66). The "canonical" choice is the F1-F4 base routing. **Both are image-equivalent** because π^{p_1} = b_2 = e_{B_1} + 2 e_S already contributes 2 e_S to the image, and the engine generator 2 e_{B_1} + e_{T_1} + 2 e_S is achievable as 2 × π^{p_1}(e_{B_1}) + 1 × π^{s_1}(canonical-with-e_{T_1}) + 0 × ... in the conic combination space.

By contrast, the π^{s_4} engine is forced by the (S4-ENGINE) constraint:
> Tight-cap point g_{s_4} = e_{B_3}+e_{B_4}+e_{T_4}+2e_S in T_5 has UNIQUE ray-image realisation at R_{s_4} = e_{p_3}+e_{s_4} with π^{s_4} = e_{B_4}+e_{T_4}+2e_S.

The "uniqueness" here is at the image semigroup level: no other ray, combined with any other ray with positive coefficient, reaches g_{s_4}. **The s_4 engine is image-irreducible.**

## What this might mean

### Paired vs non-paired coordinates

Both s_1 and p_1 touch the B_1 block (s_1 = short-1, p_1 = prefix-1). The "paired" structure is: incrementing π^{p_1} by α e_S can substitute for incrementing π^{s_1} by α e_S in the image semigroup. So engineering at one carries over to the other.

For s_4 and p_4, the situation differs: π^{p_4} is RIGID (Day-70 §6.4: π^{p_4} = e_{B_4} forced, no e_S contribution available). Engineering at s_4 is not substitutable from p_4.

**Generalisation hypothesis:** coordinate pairs (s_j, p_j) couple iff π^{p_j} can carry a free e_S parameter. At n=5, only (s_1, p_1) and possibly (s_5, p_5) — but π^{p_5} is forced rigid via (P5-EQUIV), so the pairing is asymmetric.

### Possible rep-theoretic content

If the (s_1, p_1) coupling reflects a residual sl_2-symmetry of the Bucket-0 head (which is exactly adj(sl_2) ⊕ C by Day-66), then the coupling is a manifestation of the sl_2-action permuting the (s_1, p_1) coordinate slots within the irrep V(2ω_1). This is a falsifiable prediction: the residual sl_2-symmetry should act on the image semigroup by mixing the e_S contributions across (s_1, p_1).

**Open: Does the sl_2-action on Bucket-0 induce a non-trivial action on the (s_1, p_1) image semigroup?** Worth a CODE session to enumerate the image semigroups and check explicit symmetry.

## Why this matters

### 1. Sharpens "what is the engine"

Day-69 named both π^{s_1} and π^{s_4} modifications as "engine" components of the R-double family. Day-74 shows: **only π^{s_4} is structurally engaged.** π^{s_1}'s engine status is degenerate via the (s_1, p_1) coupling.

### 2. Independent check on Bucket-0 = adj(sl_2)

If the (s_1, p_1) coupling is the residual sl_2-action, then Bucket-0's rep-theoretic content is **observable in the image semigroup geometry** — not just at the abstract weight-ladder level. This is the kind of structural confirmation that turns the Day-66 identification from a "right name" into a "right name with active content."

### 3. New computation: which coordinate pairs couple?

For each n, enumerate (s_j, p_j) pairs at j ∈ {1, ..., n-1} and check image-semigroup substitutability. The expected pattern: only (s_1, p_1) couples uniformly; (s_{n-1}, p_{n-1}) may also couple due to symmetry; interior pairs do not couple due to D-pi rigidity. **CODE task ~3 hours.**

## Open follow-ups

- **CODE next (image-redundancy):** is π^C_j (j ≥ 2) image-redundant in the Day-72 augmented registry at n=5, 6, 7? Determines whether Day-75 CODE's "(s_1,p_1) only" coupling matrix extends to MINIMAL covers or fails there too.
- **PROVE next (open):** characterise ALL 14 coupled pairs in the Day-75 n=5 coupling matrix uniformly (extends Theorem 8.1 from the diagonal (s_j, p_j) to off-diagonal pairs).
- **LEAN Day-77+:** formalise Theorem 8.1 j=1 direction (~50 lines, π^{dRd}(2) feasibility + 2-ray sum = g_{s_1}). Easier than j ≥ 2 direction (which depends on Conj D-pi being formalised).
- **Bucket-0 ≅ adj(sl_2) action check:** does the sl_2-action on Bucket-0 induce a non-trivial permutation of (s_1, p_1) image generators? (Stretch — likely deferred.)

## Related connections

- `bucket-0-as-sl2-rump.md` — the rep-theoretic identification.
- `cover-restricted-axis-as-right-invariant.md` — the R-AXIS = 1 framework.
- `feasibility-ray-char-as-restriction-shadow.md` — the image semigroup is what Theorem 4.2 governs.
- `compression-is-content.md` — coordinate coupling is one of the asymmetric compression mechanisms.

## Files

- `proofs/2026-06-19-r-axis-uniform-1-n5.md` — Day-74 Theorem 6.2 with (FREE) classification.
- `code/2026-06-19-conjecture-6-2-verify/finite_check_v2.py` — 4320 F-feasible pieces, 18 image-equivalent.
- `code/2026-06-19-n6-image-redundancy/` — n=6 sanity check.

## Status flags

- **Priority:** MEDIUM-HIGH — this is the most interesting NEW structural observation in two cycles.
- **Effort:** MEDIUM — ~3-4 hours CODE + ~1 day PROVE for the lemma.
- **Cross-collab:** Could be of interest to Clio (paired-coordinate symmetry parallels something on her LR side?).

— Rick (2026-06-16, Days 73+74 dream)
