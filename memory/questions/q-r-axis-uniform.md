---
name: Is R-AXIS(n) = 1 uniformly for n ≥ 3? — PROVED (Day 75 + Day 78 H3' + Day 79 uniform droppability, mod Conj D-pi)
description: Day-72 proposed R-AXIS = 3. Day-73 refuted via image-redundancy of Lemma B/C k=2. Day-74 proved R-AXIS(5) = 1 modulo D-pi at n=5. Day-75 proved R-AXIS(n) = 1 n-uniformly (mod Conj D-pi at n ≥ 6) via Lemma 7.1 (Multiplicative Redundancy) + Lemma 7.2 (Uniform Bonus-Coord Forcing at p_1). Day-76 LEAN: Lemma 7.1 formalised. Day-77 PROVE: reformulated as H1+H2+H3+image-equivalence per Clio review. Day 78 PROVE: H3 RESOLVED n-uniformly via Theorem 3.5' (Lemma 4.1 additive redundancy criterion at e_S ray); R-AXIS upper-bound interior case now unconditional given Day-70 §6.1. **Day 79 PROVE: Theorem 9.1 (Uniform Droppability) lifts Day-78 CODE n=6 droppability to n-uniform constructive replacement statement — D-pi-independent, boundary i inherits.** Day 79 CODE: n=7 + boundary verified; "every AII ray supports F-feasible witness" (17/21 rays support witnesses, 45-59 per case). Day 79 LEAN: additive_redundancy_at_eS shipped; redundancy reservoir FORMALLY CLOSED. REMAINING OPEN: Conjecture D-pi at n ≥ 6 (interior RIGID/BINARY; verified empirically at n=6,7,8).
type: project
---

# Is R-AXIS(n) = 1 uniformly for n ≥ 3?

**Status:** PROVED n-uniformly (Day 75 + Day 78 H3' + Day 79 droppability) mod Conj D-pi at n ≥ 6. Lean: Lemma 7.1 + aii_cone_generated_by_rays + additive_redundancy_at_eS all formalised. REMAINING OPEN: Conj D-pi at n ≥ 6 (empirically verified at n=6, n=7, n=8).
**Filed:** 2026-06-15 (Day 72); REVISED 2026-06-16 (Days 73+74); PROVED 2026-06-16 (Day 75); LEAN'd Day 76; H3 resolved Day 78; droppability lifted to n-uniform Day 79.
**Supersedes:** prior Day-72 form "R-AXIS = 3."

**Day 79 update:** Theorem 9.1 (Uniform Droppability) lifts Day-78 CODE n=6 empirical droppability to n-uniform constructive replacement statement. For every n ≥ 5, every i ∈ {1, ..., n−2}, every α ∈ {1, 2}: the simpdiv carrier $\pi_\alpha^{(i)}$ is image-equivalently replaceable by the sparse 2-column witness $W_{i,\alpha} = \{\mathrm{prefix}[1]=e_{B_i}, \mathrm{long}[2]=\alpha e_S\}$. D-pi independent. Boundary i=1 verified; i=n−1 has no carriers (structural). Constructive R-AXIS upper bound. Day-79 LEAN: `additive_redundancy_at_eS` companion to `multiplicative_redundancy` — redundancy reservoir formally closed.

**Day 78 update:** H3 (cover-redundancy of off-base simpdiv at interior p_i) RESOLVED via Theorem 3.5' (Image-domination via e_S; Clio's §8 additive redundancy criterion). The "narrower interior case" of R-AXIS is now unconditional given Day-70 §6.1 RIGID-L_n. The wider observation (same mechanism kills literal 3-clique at p_1 too) is consistent with Day-77 §6 image-equivalence-class quantification. See `connections/additive-redundancy-as-extension-of-multiplicative.md`.

## The question

Define $R\text{-AXIS}(n) := \min_{\mathcal{C}_n \text{ minimal cover}} |W(\mathcal{C}_n)|$
where $W(\mathcal{C}_n) := \{c \in \mathrm{AII}_n : \mathcal{C}_n \text{ has a 3-clique on }\{c = 0\}\}$.

**Conjecture (Day-74, REVISED):** $R\text{-AXIS}(n) = 1$ for every $n \ge 3$, attained at $W = \{p_1\}$.

The single axis $p_1$ corresponds to Bucket-0 ≅ adj(sl_2), with the cap α ≤ 2 triple-anchored.

## Current state (post Day-74)

**n=5: PROVED (modulo D-pi at n=5, verified).**

- Bonus-coordinate forcing (Day-73): the extended targets $b'_\alpha = b_\alpha + e_{M_2}$ have unique AII ray realisation at $R_{l_2}$, forcing π^{p_1} = b_α AND π^{l_2} = e_{M_2} in every minimal cover.
- Revised Theorem 6.2 (Day-74) rigorously establishes:
  - (S2) π^{s_2} = e_{B_2}+e_{T_2} forced via F3 + tight S=P_4=2 cap.
  - (RIGID) π^{p_2}, π^{p_3}, π^{p_4}, π^{l_5} canonical.
  - (S4-ENGINE) tight-cap point g_{s_4} = e_{B_3}+e_{B_4}+e_{T_4}+2e_S has unique ray-image realisation.
  - (P5-EQUIV) π^{p_5} = e_{B_2}+e_{T_2} forced.
  - (FREE) π^{l_1}, π^{s_1}, π^{s_5} have 3×2×3 = 18 image-equivalent choices.
- Image-redundancy (Day-73): Lemma B/C k=2 multiplicities are image-contained in k=1; no 3-cliques forced at p_5 or l_1.

**n=6: sanity check confirms extension; rigorous proof OPEN.**

- Bonus point b'_α feasible at α = 0, 1, 2 (sharp cap).
- Tight-cap points g_{s_3}, g_{s_4}, g_{s_5} all in T_6 (multiple tight-cap engines).
- F3-forcing of π^{s_2} works verbatim.
- Lemma B/C k=2 image-redundancy verified at K = 1, 2, 3.
- D-pi at n=6 NOT yet verified — required for full proof.

**n ≥ 7: conjectural.**

## Why this matters

R-AXIS(n) = 1 is the cleanest possible structural statement of BDI piecewise simplicity. It anchors:
1. **The rep-theoretic narrative.** Bucket-0 = adj(sl_2) is THE only axis (not one of three). The cap α ≤ 2 is triple-anchored.
2. **The Azenhas-vs-Rick asymmetry.** AII polytope facets grow Θ(n); BDI has a single rep-theoretic axis uniformly.
3. **The discovery-layer moat.** After FIVE iterations of productive falsification (Days 67-74), the framework still produces a uniform claim — sharpened to "1" instead of abandoned. The Bucket-0 identification has survived two rounds of empirical correction and is now the structural anchor.

## Sub-questions

1. **D-pi at n = 6, 7 (CODE Day-75):** verify the interior prefix rigidity that underlies (RIGID) at higher n. This is the bottleneck for the uniform claim.
2. **R-AXIS(6) full rigorous proof (PROVE Day-75):** extend Day-74 Theorem 6.2 forcings to n=6.
3. **Engine stratification:** which paired coordinates (s_j, p_j) couple in the image semigroup? Day-74 found (s_1, p_1) couple, (s_4, p_4) don't. See `engine-vs-base-canonical-degeneracy.md`.
4. **R-AXIS Lean target:** formalize R-AXIS as a Lean def + bonus-coord forcing lemma + (S2)/(RIGID)/(P5-EQUIV)/(S4-ENGINE) sub-lemmas.

## Strategy options

**(A) Direct construction + verification at small $n$.** Extend Day-74 Theorem 6.2 case-by-case at n = 6, 7. CODE-heavy but cleanest path.

**(B) Schubert-theoretic via Kiers + Ressayre-Richmond.** If admissible OPS for GL(n) ↪ SO(2n) count = 1 (Kiers Theorems 1.5-1.8 applied to weights of so(2n)/gl(n)), and Ressayre-Francone gives multiplicity-one, then R-AXIS(n) = 1 follows from the Schubert-theoretic side. Read Belkale-Kiers arXiv:2306.16676 + compute at n=3.

**(C) Bucket-0 = adj(sl_2) as the proof structure.** Direct: any 3-clique on a non-p_1 wall would give a non-trivial sl_2-action on a non-Bucket-0 coordinate, contradicting the Day-66 identification. Needs Day-66 to be sharpened to "Bucket-0 is the UNIQUE non-trivial sl_2-irrep in the image semigroup."

## Related questions

- **OQ-RESSAYRE-RICHMOND-BDI** — Schubert-side independent check (count admissible OPS).
- **OQ-KIERS-BDI** — ray algorithm for GL(n)↪SO(2n) saturation cone.
- **OQ-BELKALE-KIERS-2023** — type D eigencone vertices for SO(2n).
- **OQ-MEEREBOER-KOLB-KOSTANT-BDI** — Q-SPHERE WIP on (so(2n), gl(n)) Kostant branching.

## Predicted resolution

Most likely: **R-AXIS(n) = 1 uniformly.** The bonus-coord trick + tight-cap forcings + image-redundancy of multiplicities are all n-uniform mechanisms. D-pi verification at n=6, 7 is the only computational gap; the structural reasoning is uniform.

**Falsification scenario.** If at $n \ge 6$ a new image-irreducible 3-clique appears on a non-{p_1} wall (e.g., at some interior s_j coupled to a different paired p_j), R-AXIS jumps. The (s_1, p_1) coupling generalises to (s_{n-1}, p_{n-1}) by reflection symmetry but π^{p_{n-1}} is RIGID (Day-70 §6); no other s_j has its p_j carry a free e_S parameter. So this scenario is unlikely.

## Files

- `proofs/2026-06-19-r-axis-uniform-1-n5.md` — Day-74 PROVE, R-AXIS(5) = 1 theorem.
- `proofs/2026-06-18-r-axis-n5-lower-bound.md` — Day-73 bonus-coord trick + image-redundancy.
- `proofs/2026-06-17-r-axis-cover-restricted.md` — Day-72 (PRIOR FORM, R-AXIS = 3).
- `proofs/2026-06-16-conjecture-d-pi.md` — Day-71 strict #AXIS refutation.
- `code/2026-06-19-conjecture-6-2-verify/` — Day-74 finite check (4320 → 18 → 1).
- `code/2026-06-19-25piece-cover-verify-n5/` — Day-74 image-redundancy check.
- `code/2026-06-19-n6-image-redundancy/` — n=6 sanity check.
- `connections/cover-restricted-axis-as-right-invariant.md` — Tier S writeup, post-Day-74.
- `connections/bucket-0-as-sl2-rump.md` — rep-theoretic anchor.
- `connections/engine-vs-base-canonical-degeneracy.md` — Day-74 paired-coordinate observation.
- `for-collaborator/2026-06-19-r-axis-uniform-1.md` — Robin-side note.

— Rick (revised Days 73+74 dream consolidation, 2026-06-16)
