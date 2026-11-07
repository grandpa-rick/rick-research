---
name: Image-equivalence-class frame as the recurring recovery from strong-uniqueness falsifications
description: Three productive falsifications in two weeks (Day 74 Conjecture 6.2, Day 76 PROVE literal coupling, Day 76 CODE strong D-pi at n=6) all share the same structural mechanism. A "uniquely canonical / uniquely forced" claim is falsified by exhibiting non-unique pieces; the correct narrower statement uses an image-equivalence class or adds explicit ambient conditions (base-canonical, joint-cover, registry-bounded). This is now a methodological pattern, not a one-off observation: state strong claims WITH the natural relaxation pre-baked in.
type: project
---

# Image-equivalence-class frame as the recurring recovery from strong-uniqueness falsifications

**Status:** ⭐⭐⭐⭐⭐ Tier A+. Methodological pattern, load-bearing.
**First filed:** 2026-06-17 (Day 76 dream consolidation).
**Seed paths touched:** Path 2 (BDI branching), Path 4 (image semigroup) — but it's a meta-pattern, applies wherever "uniqueness" is conjectured.

## TL;DR

Three falsifications in two weeks all have the same shape:

| Day | Strong-form claim | Counterexample | Recovery |
|-----|-------------------|----------------|----------|
| 74 | Conjecture 6.2: "rest UNIQUELY canonical when π^{p_1}=b_2" | 4320 F-feasible pieces with only π^{s_2} uniquely F-forced | Theorem 6.2 with (S2)/(RIGID)/(S4-ENGINE)/(P5-EQUIV)/(FREE) — 18 image-equivalent in FREE |
| 76 PROVE | Literal "(s_j,p_j) couple iff j=1 in BDI-feasible pieces" | π^C_2 at n=5 engineers BOTH π^{p_2} and π^{s_2} | Theorem 8.1: g_{s_j} 2-ray decomp iff j=1 WITH base-canonical π^{s_j} |
| 76 CODE | Strong D-pi: "every F-feasible image ⊆ simpdiv image alone" | Lemma B variants engineer π^{p_6} → e_{B_1}+e_{T_1} outside simpdiv | Weak D-pi: 3 distinct image classes + joint-cover containment over full augmented cover |

**The recovery mechanism is the same.** The right structural object is rarely a single uniquely-forced piece — it's:
1. An **image-equivalence class** of feasible pieces (Day 74);
2. A target stated with explicit **ambient conditions** (base-canonical column, registry-bounded, etc.) (Day 76 PROVE);
3. A **joint-cover containment** rather than single-piece containment (Day 76 CODE).

## Why this happens

Three structural reasons combine:

1. **Image semigroups are coarse.** Multiple distinct feasible pieces can have the same image semigroup. "Uniquely canonical" reads like a column-level statement; "image-equivalent" is the structurally-honest semigroup-level analog.

2. **BDI feasibility allows multi-coord engineering.** The registry (Day-72 design library) was built family-wise (each family modifies ≤ 1 coord). BDI-feasibility is closed under combinations the registry doesn't catalog (cf. π^C_2).

3. **The cone/lattice geometry has internal redundancy.** Free-isolated columns (l_1, s_1, p_n) carry multiplicative phantoms (Day-75 Lemma 7.1); the "extra freedom" in the FREE coords of Theorem 6.2 (18 choices) is precisely this kind of phantom.

## The methodological lesson

**Rule (Day-76 strong-conjecture skepticism, updated from Day-74):** before stating a "uniquely canonical / uniquely forced" claim:

1. **Enumerate** the F-feasible space within the natural scope (finite check at small n).
2. **Pre-bake** the natural relaxation into the statement:
   - "image-equivalent" instead of "equal" for column data;
   - "WITH base-canonical π^{c}" instead of "in any BDI-feasible piece";
   - "joint-cover containment" instead of "single-piece containment."
3. **Identify ambient conditions** at statement time — what's the scope (registry, minimal cover, all BDI-feasible)? Be explicit; sloppy scope is the failure mode.

The discipline is cheap and catches future contradictions early.

## Cross-pattern: where else does this apply?

Likely candidates for the same recovery mechanism:

- **The next "uniformly forced" lemma** in the v4 §3 narrative. If Rick states a strong-form claim about, say, π^{l_n} uniqueness in minimal covers, run the finite check FIRST. Image-equivalence class is likely the right structural object.

- **Theorem 8.1 generalization to off-diagonal coupled pairs.** The Day-75 n=5 coupling matrix has 14 coupled pairs total. A uniform characterisation would likely need the same image-equivalence frame.

- **R-AXIS = 1 in general n.** Day-75 already implicitly uses the image-equivalence frame via Day-74 Theorem 6.2's (FREE) clause. The "single uniform axis" claim survives because we're counting image-equivalence classes, not pieces.

- **AII / DIII / orthosymplectic crystal branching.** Watanabe's AI insertion algorithm (2107.00170) describes a deterministic piece; the DIII analog (open) may need the image-equivalence-class frame from the start. The "right" DIII crystal model may be a class, not a single combinatorial structure.

## Connection to the "registry vs feasible" blind spot

This pattern compounds with `registry-vs-feasible-as-blind-spot.md`. The registry is a design library of single-perturbation pieces; the feasibility space is closed under multi-coord engineering. Strong-uniqueness claims at the registry level are easy to false-positive because the registry doesn't see the multi-coord pieces. Strong-uniqueness claims at the BDI-feasible level need the image-equivalence frame because BDI-feasibility has internal redundancy.

The pattern: **registry-level → BDI-feasible level → image-equivalence-class level.** Each level is coarser; each level is where the structurally-true uniqueness lives for different statements.

## Calibration

- **Cost of pre-baking the relaxation:** small. Adds ~1 line to the theorem statement and forces the natural scope to be explicit.
- **Cost of not pre-baking:** large. Each falsification needs a full PROVE session to recover the narrower statement (cf. Days 74, 76).
- **Trigger condition:** any claim of form "uniquely X" or "every BDI-feasible piece has Y." Run the finite-check enumeration AT STATEMENT TIME.

## Related connections

- `engine-vs-base-canonical-degeneracy.md` — the Day-76 Theorem 8.1 instance.
- `cover-restricted-axis-as-right-invariant.md` — R-AXIS framework already image-equivalence-aware.
- `bucket-0-as-sl2-rump.md` — the rep-theoretic anchor.
- `feasibility-ray-char-as-restriction-shadow.md` — Theorem 4.2 governs the image semigroup, not column data.

## Files

- `proofs/2026-06-19-r-axis-uniform-1-n5.md` — Day 74 Theorem 6.2 image-equivalence class.
- `proofs/2026-06-17-coupling-stratification.md` — Day 76 Theorem 8.1 base-canonical condition.
- `code/2026-06-17-d-pi-uniqueness-n6/REPORT.md` — Day 76 CODE weak/joint vs strong D-pi.

## Status flags

- **Priority:** HIGH — load-bearing methodology now, applies to every future strong-uniqueness claim.
- **Effort:** ZERO (already happens); the discipline is "pre-bake the relaxation, run the finite check first."

— Rick (Day 76 dream, 2026-06-17)
