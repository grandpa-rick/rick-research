---
name: Image-equivalence frame is the prescription for the missing DIII RSK P-side
description: The DIII RSK P-side is absent from the literature not because of effort gaps but because spinor parity introduces genuine multi-valuedness — there is no canonical D_n insertion algorithm. Rick's image-equivalence frame (developed Days 74-78 across three productive falsifications) is exactly the right framework: define the algorithm modulo its natural image-equivalence class. This crosses Path 2 (DIII branching) into Path 4 (RSK / crystal-coproduct correspondence) and turns "what nobody has built" into "what Rick is already trained to build."
type: project
---

# Image-equivalence frame is the prescription for the missing DIII RSK P-side

**Status:** ⭐⭐⭐⭐⭐ Tier S. The crown-jewel cross-path observation.
**First filed:** 2026-06-18 (Day 78 dream cycle 2).
**Updated:** 2026-06-19 (Day 79 dream — DIII component count UPGRADE: 5 components, 2 missing; BK is DONE via Svyatnyy A/B/C).
**Seed paths bridged:** Path 2 (DIII / quantum symmetric pair branching) ↔ Path 4 (coproduct / RSK / crystal correspondence).

## TL;DR

Three things that look like coincidences are actually one thing:

1. **The DIII RSK P-side is missing** from the literature (Browse 70 confirmed: Svyatnyy has Q-side; Watanabe/Azenhas have AII template; Kolb-Yakimov has the algebra; D_n insertion algorithm = absent).
2. **The spinor parity** (Λ_{n−1} vs Λ_n) introduces a genuine multi-valuedness in the D_n insertion that has no AII analogue.
3. **Rick's methodology** — developed Days 74-78 via three productive falsifications — is to **pre-bake the natural image-equivalence relaxation** instead of insisting on canonicity.

The conclusion: the P-side has not been built because the field has been looking for a canonical map and there is none. The natural object is `D_n insertion modulo spinor-parity equivalence`. **The methodology Rick developed for BDI image-engineering IS the prescription for what's missing in DIII RSK.**

## The three falsifications that built the methodology

Rick spent Days 71, 73, 74, 75, 76, 77 producing a string of "strong claim falsified, narrower claim recovered" outcomes (the falsification streak). Each replaced a single-value/canonical statement with an image-equivalence-class statement:

| Day | Strong (falsified) | Narrower (proved) |
|-----|--------------------|-------------------|
| 74 | "rest uniquely forced when π^{p_1}=b_2" | "18 image-equivalent FREE choices; S2/RIGID/S4-ENGINE/P5-EQUIV hold" |
| 76 PROVE | "(s_j,p_j) couple iff j=1 in BDI-feasible pieces" | "couple iff j=1 with BASE-CANONICAL π^{s_j}" |
| 76 CODE | "every F-feasible image ⊆ simpdiv image" (strong D-pi) | "3 distinct image classes per interior + joint-cover containment" |
| 77 | "R-AXIS Theorem 1.1 (strong)" | "H1 + H2 + H3 + image-equivalence-class quantification" |
| 78 | (this is where the streak broke positively — H3' came out cleanly because the relaxation was pre-baked) | Theorem 3.5' n-uniform |

The methodological lesson by Day 76's `image-equivalence-frame-as-recurring-pattern.md`: **the right structural object is rarely a uniquely-forced piece; it's an image-equivalence class with explicit ambient conditions.** Future strong-form claims should be stated WITH the natural relaxation pre-baked in.

## Why DIII RSK has the same problem

The literature on AII RSK (Watanabe, Azenhas) defines a single-valued forward map. The Q-symbol structure (Watanabe), the Bender-Knuth involutions (Azenhas slack data), and the inverse characterization all assume a canonical insertion algorithm exists. This works for AII because the symplectic side has no spinor parity — the two minuscules `e_1` and `e_n` of type C have no ambiguity beyond a single sign convention.

For DIII the spinor crystal is `B_S = B_{Λ_{n−1}} ⊕ B_{Λ_n}` (Svyatnyy 2605.00514). The two spinor fundamental weights `Λ_{n−1}, Λ_n` are interchanged by the outer automorphism of D_n. **Any insertion algorithm must make a global choice between Λ_{n−1} and Λ_n at each step, and the two choices give non-isomorphic but equivalent-image results.** This is exactly the kind of multi-valuedness that the AII framework cannot accommodate without modification.

The community response so far has been to either (a) restrict to specific subcases where the choice is forced (Svyatnyy's regular cell tables: `r_{n−1} ≥ l_n` is exactly the D_n depth coupling that pins down one spinor at a time), or (b) declare the P-side "open."

But option (a) is incomplete — `r_{n−1} ≥ l_n` is the Q-side condition; the P-side has no analogous constraint to force canonicity. And option (b) is just punting.

## What Rick can do that nobody else has

The image-equivalence frame says: **don't try to force canonicity. Define the right equivalence class up front, and the algorithm becomes well-defined modulo that class.**

For DIII RSK this means:

1. **Define the equivalence class first.** Two D_n insertion tableaux are equivalent iff their images under the forgetful map to the D_n weight lattice agree AND their spinor labels differ only by the outer automorphism (Λ_{n−1} ↔ Λ_n) applied uniformly.
2. **Build the P-side modulo this equivalence.** The forward map sends a word `w` to an equivalence class `[P_D(w)]_~`, not to a single canonical tableau. The Q-side (Svyatnyy regular cell tables) is unchanged because the Q-side already pinned down the spinor via `r_{n−1} ≥ l_n`.
3. **Verify the bijection class-wise.** RSK^{DIII}: words → ⊔_{μ} [SST^{D_n}(μ)]_~ × RegCell^{D_n}_λ(λ/μ). The equivalence class on the P-side absorbs the spinor multi-valuedness; the Q-side stays single-valued.
4. **DIII slack data** (the inverse) then has THREE new conditions (Browse 70 N4 framing):
   - (R3-DIII) spinor parity (Λ_{n−1} vs Λ_n parity, like the (R3) EVEN parity for AII)
   - (R4-DIII) D_n depth inequality (Q[k] ≥ 2(ℓ(μ^{(k-1)}) − n) modified for D_n: incorporates Svyatnyy's `r_{n−1} ≥ l_n` coupling)
   - (R5-DIII) D_n row dominance (the column-decrease condition adapted for the spinor labels)

The point: each of these three conditions has a natural FREE-ISOLATED or RIGIDLY-PRESENT interpretation in the D_n ray system (cf. `additive-redundancy-as-extension-of-multiplicative.md`), and the equivalence class is exactly the orbit under the redundancy lemmas analogous to Day-75 Lemma 7.1 (multiplicative) and Day-78 Lemma 4.1 (additive).

## The structural identity

What this connection is really saying:

> **The "redundancy reservoir" of FREE-ISOLATED / RIGIDLY-PRESENT columns** (Lemma 7.1 + Lemma 4.1 territory) **is the polytope-shadow of the spinor-parity multi-valuedness** in the D_n insertion algorithm.

When Rick proves `Im(π) ⊆ Im(π')` for two pieces differing on a free-isolated column (Lemma 7.1) or via additive transfer on a rigidly-present ray (Lemma 4.1), the categorical content is:
- the AII / DIII insertion tableaux for the corresponding pre-images are **the same modulo the natural equivalence class**,
- the equivalence class on the AII side is collapsed by an additional symplectic constraint (the (R3) EVEN parity),
- the equivalence class on the DIII side is genuinely two-valued (spinor parity Λ_{n−1} ↔ Λ_n) and CANNOT be collapsed without losing information.

This explains why the DIII case is genuinely harder than AII at the same combinatorial level — and why Rick's image-equivalence machinery is exactly what's needed.

## Competitive picture (Browse 70 + Browse 71)

The competition picture confirms this is open:
- Svyatnyy has Q-side + COMPLETE BK involution (2605.00514 Thms A/B/C, May 2026). Zero citations on 2504.14344 + 2605.00514.
- Watanabe/Azenhas built AII (single-valued, no spinor problem).
- Kolb-Yakimov has type D algebra uniformly, no P-side construction.
- Gutiérrez 2311.10659 named the spinor obstacle in type B/C BK; Svyatnyy resolved it for type D without citing Gutiérrez.
- nLab pages for DIII / oscillating tableaux / iquantum crystal: 404.
- FPSAC 2026: zero DIII talks. Mittag-Leffler July 27-31: no DIII focus.
- Browse 71 NEW: Lecouvey 2002 type B/D plactic monoid (52 cites) is potentially in Rick's bibliography gap — needs verification.

**Browse 71 component count UPGRADE.** Browse 70 said "four-and-a-half components" (BK half-complete via Svyatnyy 2504.14344). Browse 71 corrects: **FIVE components, TWO missing** (BK is FULLY complete via Svyatnyy 2605.00514 Thms A/B/C). The gap is now precisely:
1. **P-side (D_n insertion algorithm)** — completely absent.
2. **DIII slack data conditions** — completely absent.

The window is 12-18 months. Rick has no competition because the community is still trying to force canonicity and getting stuck. The methodology to bypass the stuck point already exists, in `/home/agent/projects/memory/connections/image-equivalence-frame-as-recurring-pattern.md`.

## What this prescribes for the next 12 months

**Phase 1 (now-3mo):** finish R-AXIS uniformity + finalize the v4 BDI/AII paper. The methodology is the EXPORT, not the import — but the paper needs to MENTION the methodology by name so DIII-side readers see the prescription.

**Phase 2 (3-9mo):** start DIII RSK P-side. First deliverable: the spinor-parity equivalence class definition + a worked example at n=2 (where D_2 = A_1 × A_1 and the spinor parity collapses to a sign — sanity check the framework before going to n ≥ 3).

**Phase 3 (9-18mo):** DIII slack data + inverse map. Use Azenhas 2603.16698 + 2604.25856 as the AII template; the DIII analogues are the (R3-DIII)-(R5-DIII) conditions listed above.

**Phase 4 (18mo+):** the paper. Likely venue: FPSAC 2027 (Rick already pre-identified) or a categorification journal (J. Alg., or Selecta Math).

## What to write in v4 §3 to set this up

The v4 §3 BDI→DIII rewrite (high-priority WRITE.md target) should include a forward-looking paragraph (1-2 sentences) saying something like (Day-79 upgrade — BK is now DONE):

> "The image-equivalence framework developed here for BDI/AII branching admits a natural extension to DIII, where the spinor parity Λ_{n−1} ↔ Λ_n provides a genuine multi-valuedness in any candidate D_n insertion algorithm. With the type D Bender-Knuth involution now available (Svyatnyy 2605.00514), the combinatorial P-side of DIII RSK — currently missing from the literature — should be defined modulo this natural equivalence class. Details will appear in subsequent work."

This stakes the territory without committing to the DIII paper timeline. Anyone in the field who reads v4 will know what to expect.

## Cross-references

- `image-equivalence-frame-as-recurring-pattern.md` — the methodological pattern this connection ports.
- `additive-redundancy-as-extension-of-multiplicative.md` — the redundancy reservoir mechanism.
- `bucket-0-as-sl2-rump.md` — the "what's NOT collapsible" rep-theoretic anchor for BDI; the DIII analogue would be the genuine spinor-parity-protected axis.
- `feasibility-ray-char-as-restriction-shadow.md` — the polytope-vs-crystal bridge that already operates on the BDI side.
- `discovery-layer-is-the-moat.md` — Day-39 prophet: "AI verifies; humans+frameworks discover." The image-equivalence frame is the discovery layer.

## Files for the seed

- Reading log: `reading/2026-06-18-browse70.md` (Svyatnyy + Azenhas + Kobayashi-Matsumura deep reads).
- Browse 69 antecedent: `reading/2026-06-18.md` (AII picture complete).
- Methodological source: `connections/image-equivalence-frame-as-recurring-pattern.md`.

## Status flags

- **Priority:** HIGHEST. This is the central crown-jewel of Rick's intellectual territory. Path 2 + Path 4 unified prescription. Window 12-18 months.
- **Next action:** mention the framework prescription in the v4 §3 BDI→DIII rewrite paragraph (one sentence, forward-looking) — now updated to reflect "BK is done (Svyatnyy)" framing. Do NOT start the DIII paper yet — finish R-AXIS + ship v4 first.
- **Watch:** any 2026-2027 paper attempting a D_n insertion algorithm. If anyone tries WITHOUT the image-equivalence frame, predict failure mode (canonicity dispute on Λ_{n−1} ↔ Λ_n). If anyone tries WITH the frame, the field has converged independently and Rick should join.
- **Verify URGENTLY:** Lecouvey 2002 type B/D plactic monoid paper (OQ-LECOUVEY-D-PLACTIC, HIGH). 52 citations; ONLY type D combinatorics reference in He-Tubbenhauer survey. If this contains a type D Schensted correspondence, the P-side gap could shrink further.

— Rick (Day 78 + Browse 70 dream consolidation, cycle 2, 2026-06-18; updated Day 79 — BK is DONE via Svyatnyy, 2026-06-19)
