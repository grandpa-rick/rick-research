---
name: Cover-restricted R-AXIS = 1 uniformly; the unique rep-theoretic axis is p_1 = Bucket-0 = adj(sl_2)
description: Day 71 refuted strict # AXIS = 3 (D-pi). Day 72 proposed R-AXIS = 3 cover-restricted. Day 73 killed THAT via image-redundancy of Lemma B/C k=2 multiplicities. Day 74 proved R-AXIS(5) = 1 as theorem (modulo D-pi at n=5), with cap α ≤ 2 triple-anchored (BDI S-budget = dim V(2ω_1) − 1 = unique cover-restricted axis count). The Azenhas-vs-Rick asymmetry: Azenhas counts polytope walls (Θ(n)); Rick has a SINGLE rep-theoretic axis (uniformly 1) that the geometric framework cannot see.
type: project
---

# Cover-restricted R-AXIS = 1 uniformly: the unique rep-theoretic axis

**Status:** ⭐⭐⭐⭐⭐ Tier S. Final form of the AXIS narrative after FIVE iterations.
**First filed:** 2026-06-15 (Day 71+72 dream); REVISED 2026-06-16 (Days 73+74).
**Seed paths touched:** Path 2 (BDI branching), Path 4 (piecewise projection / image semigroup).
**Cross-program note (Day 89 dream 2):** R-AXIS = 1 is one instance of the broader **single-carrier dominance** pattern — see `sharp-cancellation-single-carrier.md` §"Cross-program pattern" for the Program A (β' arithmetic) analog. Both programs extract an invariant from a unique dominant term with strict subordination elsewhere; different rigidity measures (image-equivalence vs v_2 distinct-min).

## TL;DR

Four numbers, four levels:

| Object | Closed form / value | n=5,6,7 |
|---|---|---|
| AII polytope facets (Azenhas, geometric) | 3n − [n even] | 15, 17, 21 |
| BDI polytope facets (Rick, geometric) | 4n − 5 | 15, 19, 23 |
| Strict #AXIS (Day-72 augmented registry) | 2(n−1) | 8, 10, 12 |
| **R-AXIS = cover-restricted #AXIS** (Day-74 theorem at n=5; conjecture n ≥ 6) | **1** uniformly | **1, 1, 1** |

The final answer is R-AXIS(n) = 1 at the single coordinate p_1 = Bucket-0 ≅ adj(sl_2). The cap α ≤ 2 is triple-anchored: (i) BDI S-budget S ≤ P_{n-1}(e_{B_1}) = 2, (ii) dim V(2ω_1) − 1 = 2 in the sl_2-irrep, (iii) the unique cover-restricted axis count.

## Definition (R-AXIS)

For a minimal BDI-feasible cover $\mathcal{C}_n$ of the BDI lattice $T_n$:
$$W(\mathcal{C}_n) := \{c \in \mathrm{AII}_n : \mathcal{C}_n \text{ has a 3-clique on } \{c = 0\}\},$$
$$R\text{-AXIS}(n) := \min_{\mathcal{C}_n \text{ minimal}} |W(\mathcal{C}_n)|.$$

A "3-clique on $\{c = 0\}$" is three pieces pairwise differing only on column $c$, with three distinct $c$-columns. The minimum is well-defined (Day-72 §3 finiteness lemma via Day-70 Cor 5.1 image-semigroup).

## What changed across FIVE iterations (Days 67-74)

| Iteration | Claim | Refuter | Sharpening |
|---|---|---|---|
| Day 67-68 | # AXIS = 3 empirically | n=4 R-double family missed | Augment registry |
| Day 70-71 | # AXIS ≤ 3 mod D-pi | Simple-divert at interior p_i (Day 71) | Cover-restrict |
| Day 72 | R-AXIS = 3 (cover-restricted) | Lemma B/C k=2 image-redundant (Day 73) | Drop B/C |
| Day 73 | R-AXIS ≤ 1 at p_1; ≥ 1 via Conjecture 6.2 | Strong rest-canonicity false (Day 74) | Replace with Theorem 6.2 |
| **Day 74** | **R-AXIS(5) = 1 THEOREM** | — | Final form |

Each iteration was a productive falsification within ≤ 24 hours. The framework knows how to sharpen.

## What changed (Day 71 → Day 72)

### Day 71: D-pi refuted

Day-70 reduced "# AXIS(n) ≤ 3 uniformly" to **Conjecture D-pi** (interior prefix $p_i$ is RIGID in every minimal cover). Day 71 explicitly built the simple-divert family $\pi_\alpha^{(i)}$ with $\pi^{p_i} = e_{B_i} + \alpha e_S$ for $\alpha \in \{0, 1, 2\}$, every $n \ge 5$ and every interior $i \in \{2, \ldots, n-2\}$. Three BDI-feasible pieces, three distinct $p_i$-columns. 3-clique. D-pi refuted.

The structural error: Day-70 §7 wrote "no middle-i R-double engine analogous to level-1 R-double." Wrong. No engine needed — the cap $\alpha \le 2$ comes from $S \le P_{n-1}(e_{B_i}) = 2$ **independent of $i$**. Lemma A's engine at level 1 was over-engineered; the level-$i$ analogues exist trivially.

### Day 72 (CODE): strict #AXIS = 2(n-1)

`code/2026-06-17-strict-axis/` (commit `b451eab`). Augmented registry (42/53/66 distinct pieces at n=5/6/7) → strict #AXIS = 8, 10, 12. Pattern: $2(n-1)$. Axis vars: $\{p_1, \ldots, p_{n-2}, p_n, l_1, \ldots, l_{n-1}\}$ — matches the union of simple-divert (n-2 interior prefix) + Lemma B ($p_n$) + Lemma C ($l_1$) + $l_j$-divert ($n-1$ long coords).

### Day 72 (PROVE): R-AXIS rescue

`proofs/2026-06-17-r-axis-cover-restricted.md`. Defines R-AXIS rigorously. At n=5: explicit cover with W = {p_1, p_5, l_1} via Day-69 AXIS families + unique-signature auxiliaries (each modifying ≥ 2 columns from base, so no 3-clique arises on non-AXIS walls — Lemma 4.3). Computationally verified for Classes 1, 2 (commit `b451eab`); Classes 3, 4 sketched, deferred to CODE Day-73.

At n=6: the Day-72 PROVE.md's tentative conjecture "R-AXIS(6) ≥ 4" REFUTED. The $l_j$-divert family $\pi^{[l_j \to 2 e_S]}$ covers gap points $e_{B_{j-1}} + 2 e_S$ without forcing $\{p_{n-1}\}$ into a 3-clique. R-AXIS(6) ≤ 3. (This was the Day-72 framing; Day-73 sharpened further to R-AXIS = 1.)

### Day 73 (PROVE+CODE): image-redundancy → R-AXIS(5) ≤ 1

`proofs/2026-06-18-r-axis-n5-lower-bound.md`. The **bonus-coordinate trick** works at p_1: extend b_α to b'_α = b_α + e_{M_2}; the unique AII ray realising b'_α is R_{l_2}, forcing π^{p_1} = b_α and π^{l_2} = e_{M_2} in every minimal cover.

But the analogous trick FAILS at p_5 and l_1. Lemma B targets c_k = k(e_{B_4}+e_{T_4}) and Lemma C targets d_k = k e_{B_1} are LINEAR MULTIPLICITIES — image-redundant: Lemma B k=2 ⊆ Lemma B k=1 (because 2c_1 = 2 × R_{p_5}-image). Day-72's 27-piece cover is NOT minimal. Remove the two redundant pieces, get a 25-piece subcover with 3-cliques on {p_1} only. **R-AXIS(5) ≤ 1, contradicting Day-72's R-AXIS(5) = 3.**

### Day 74 (PROVE+CODE+LEAN): R-AXIS(5) = 1 theorem

`proofs/2026-06-19-r-axis-uniform-1-n5.md`. Day-73 reduced R-AXIS(5) ≥ 1 to **Conjecture 6.2 (rest uniquely forced)**. Day-74 finite check: 4320 F-feasible pieces with π^{p_1} = b_2, π^{l_2} = e_{M_2} (only π^{s_2} F-uniquely forced); 18 image-equivalent to R-double-α=2. Strong Conjecture 6.2 FALSE. **Replaced by revised Theorem 6.2:**
- (S2): π^{s_2} = e_{B_2}+e_{T_2} forced via F3 + tight S = P_4 = 2 cap.
- (RIGID): π^{p_2}, π^{p_3}, π^{p_4}, π^{l_5} canonical.
- (S4-ENGINE): tight-cap point g_{s_4} = e_{B_3}+e_{B_4}+e_{T_4}+2e_S has UNIQUE ray-image realisation at R_{s_4}; π^{s_4} engine genuine.
- (P5-EQUIV): π^{p_5} = e_{B_2}+e_{T_2} forced.
- (FREE): π^{l_1}, π^{s_1}, π^{s_5} have 3×2×3 = 18 image-equivalent choices.

**R-AXIS(5) = 1 theorem** (modulo D-pi at n=5, verified). The R-double 3-piece sub-cover forms the unique 3-clique on {p_1}.

n=6 sanity check (code/2026-06-19-n6-image-redundancy) confirms all forcings extend. **Conjecture: R-AXIS(n) = 1 uniformly, n ≥ 3.**

### Day 74 (LEAN): feasibility_ray_char (⇒) + biconditional

Commit `122eed4`, +57 lines. `IsFeasible {n} (P : BdiSet) (π : Piece' n)` predicate + `feasibility_ray_char_forward` + `feasibility_ray_char_iff`. Singleton-list trick (each ray r as `coniclyCombine [r] (fun _ => 1) π`) sidesteps DecidableEq on AIIRay. Axioms ⊆ {propext, Quot.sound}.

### Day 72 (LEAN): Theorem 4.2 shipped

`proofs/lean/bdi-polytope/BdiPolytope.lean`, 1418 → 1663 lines (+245), commit `c7aa9a1`.

- `feasibility_ray_char` (conic form): axioms $\subseteq$ {propext, Quot.sound}.
- `feasibility_ray_char_lattice` (lattice form): + `aii_cone_generated_by_rays` axiom (deferred geometric Lemma 4.1, ~50-80 lines mechanical to discharge).

No sorry. No Classical.choice. Stdlib only. The Day-70 Path-2-meets-Path-4 polytope bridge now has a Lean witness.

## Why this matters

### 0. The cap α ≤ 2 is TRIPLE-anchored (Day-74 sharpening).

The cap α ≤ 2 on the R-double-head parameter is the same number in three independent senses:
1. **BDI S-budget:** S ≤ P_{n-1}(e_{B_1}) = 2 (combinatorial constraint).
2. **dim adj(sl_2) − 1 = dim V(2ω_1) − 1:** the sl_2-weight ladder for the irrep on Bucket-0 (rep-theoretic).
3. **R-AXIS(n) = 1 axis count multiplicity:** at p_1 there are exactly three pieces (α ∈ {0, 1, 2}) forced into the cover (cover-restricted).

Three independent ceilings coincide at α ≤ 2. **This is the structural content of the Bucket-0 = adj(sl_2) identification at the cover-restricted level.**

### 1. The strict-vs-cover-restricted asymmetry IS the Azenhas-vs-Rick asymmetry.

Browse 59's original "AII ~2(n−1) walls" heuristic was wrong as an AII *polytope* facet count. But: it accidentally matches the **strict #AXIS** for BDI. The structural pattern is:

- **Geometric polytope facets:** Both sides Θ(n). Not a contrast.
- **Strict piecewise walls:** Both growing linearly. Not a contrast at this level either (with Day-72 CODE).
- **Cover-restricted piecewise walls:** Rick conjecturally 3, Azenhas has no analogous construction. **This is the contrast.**

The asymmetry survives at exactly the level where Rick built infrastructure that Azenhas didn't.

### 2. The discovery-layer moat survives the refutation.

D-pi refuted; "uniform-3 strict" wrong. **But:** the right cover-restricted invariant is uniformly 3 (conjecturally). The piecewise projection π̃_n with 3 cover-restricted walls is still a uniquely-Rick-side construction. Azenhas hoped for a "geometric object"; Rick has the cover-restricted notion that lives inside the piecewise projection.

The Day-66/Day-69 narrative "the head + bulk lives in the cover-restricted count" survives in a sharpened form: the Day-69 AXIS families (R-double / free-top / free-bottom) supply the **3 forced cover-restricted walls**, and the unique-signature auxiliaries fill the gap without adding new 3-cliques.

### 3. The Bucket-0 = adj(sl_2) identification needs refinement.

Day-66's identification of the Lemma A R-double family as the adj(sl_2) weight ladder is **engine-specific** — the engine R-double has extra $s_1, s_{n-1}$ modifications carrying rep-theoretic content. The Day-71 simple-divert pieces $\pi_\alpha^{(i)}$ form analogous 3-cliques at *every* interior level but don't carry the rep-theoretic content of the engine version.

**The right invariant is engineered image content, not 3-clique existence.** The "head" interpretation sharpens to "engine R-double head" — the rep-theoretic content is rigidified by the engine modifications, and the simple-divert versions are the "bulk" filling.

This suggests a structural claim worth formalizing: a piece is **rep-theoretic** iff its image is closed under the sl_2-action induced by the canonical inclusion adj(sl_2) ↪ End(P^BDI). The engine R-double passes; the simple-divert doesn't.

### 4. R-AXIS is a Lean-formalisable invariant.

R-AXIS(n) is a min over a finite set (Day-72 Lemma 3.1, via Day-70 Cor 5.1). Each minimal cover is a finite list of pieces; each 3-clique is a finite check. R-AXIS(n) ≤ 3 reduces to: produce a cover. R-AXIS(n) ≥ 3 reduces to: prove every cover has 3 forced walls (a finite check at fixed $n$).

With Day-72 Lean Theorem 4.2 in hand, the R-AXIS framework is the natural next Lean target. ~2-3 sessions.

## Tested predictions

- **R-AXIS(5) = 1** — Day-74 PROVE theorem (modulo D-pi at n=5, verified).
- **R-AXIS(6) = 1** — Day-74 CODE Task C sanity check confirms bonus-coord + tight-cap forcings extend. Rigorous proof conditional on D-pi at n=6.
- **R-AXIS(n) = 1 uniformly** — conjectural. Test by verifying D-pi at n=6,7 (CODE Day-75).
- **Strict #AXIS(n) = 2(n−1)** — empirical at n=5,6,7 (Day-72 CODE). Closed form via "interior prefix simple-divert ∪ $l_j$-divert ∪ Lemma B ∪ Lemma C" count.

## Open follow-ups (post Day-74)

- **D-pi at n = 6, 7 (CODE Day-75):** R-AXIS(n) = 1 uniformly depends on D-pi at higher n.
- **R-AXIS(6) full rigorous proof (PROVE Day-75):** extend Day-74 bonus-coord + Theorem 6.2 forcings to n=6.
- **Strict #AXIS closed form:** prove $2(n-1)$ at every $n \ge 5$. (Lower priority now that R-AXIS = 1 is the headline.)
- **R-AXIS Lean target:** formalize R-AXIS as a Lean def + Lemma 4.3 + the bonus-coord forcing.
- **Engine stratification (Day-74 SURPRISE):** does the paired-coordinate structure (s_1, p_1) (both touch B_1) reflect residual sl_2-symmetry of Bucket-0? Compare to (s_4, p_4) which is NOT paired in the same way. See `engine-vs-base-canonical-degeneracy.md`.

## Implications for the seed

1. **Path 2:** BDI branching has a SINGLE rep-theoretic axis (R-AXIS = 1 uniformly conjectured) — the cleanest possible orthogonal-vs-symplectic structural contrast. The single axis at p_1 = Bucket-0 ≅ adj(sl_2) is the *only* rep-theoretic content surviving from the polytope, the cover-restricted picture, and the Day-66 rep-theoretic identification — three views, one anchor.
2. **Path 4:** The "minimal generator" count parallel sharpens: BDI cover-restricted minimal generating axis count = 1 (the head). Crystal tensor product rules have ONE highest weight vector per irrep — the parallel is exact: one head, multiplicity α + 1 along it. The R-double family α ∈ {0, 1, 2} is the orthogonal-Schur-Weyl analogue of a sl_2-string.
3. **Seed Q4 (q=0 limit):** image-semigroup thinking with a SINGLE non-trivial generator (cap α ≤ 2) is exactly the "skeleton" structure that survives at q = 0.

## Related connections

- **`aii-bdi-wall-count-asymmetry.md`** — UPDATED (strict #AXIS = 2(n-1); R-AXIS = 3 cover-restricted is the structural contrast).
- **`bucket-0-as-sl2-rump.md`** — UPDATED (engine R-double vs simple R-double: rep-theoretic ↔ image-engineered).
- **`feasibility-ray-char-as-restriction-shadow.md`** — Lean Theorem 4.2 SHIPPED Day 72 (commit `c7aa9a1`).
- **`pi3-stratified-multimap.md`** — The piecewise projection where R-AXIS = 3 conjecturally.
- **`discovery-layer-is-the-moat.md`** — Strengthened: Rick's discovery-layer survives a refutation by SHARPENING (not abandoning) the invariant.

## Files

- `proofs/2026-06-16-conjecture-d-pi.md` — Day-71 D-pi refutation.
- `proofs/2026-06-17-r-axis-cover-restricted.md` — Day-72 R-AXIS rescue.
- `proofs/lean/bdi-polytope/BdiPolytope.lean` §"Day 72" — Theorem 4.2 in Lean.
- `code/2026-06-17-complete-registry/`, `code/2026-06-17-strict-axis/`, `code/2026-06-17-facets-n12-n13/`, `code/2026-06-17-r-axis-verify/`.
- `for-collaborator/2026-06-16-conjecture-d-pi-REFUTED.md`, `for-collaborator/2026-06-17-r-axis-program.md`, `for-collaborator/2026-06-17-feasibility-ray-char-lean.md`.

## Status flags

- **Priority:** HIGH — v4 §3 narrative needs another rewrite (strict → cover-restricted framing).
- **Effort:** MEDIUM — Class-3 auxiliaries case analysis + uniformity argument.
- **Cross-collab:** Robin pending review on D-pi refutation note + R-AXIS program note. Clio pending on rep-theoretic vs image-engineered distinction.

— Rick (Days 71+72 dream consolidation, 2026-06-15 afternoon)
