# Aug~ as the BGG-Verma Differential (doubly-laced)

> **STATUS (2026-05-13, Day 11): PROVED at REDUCED-multiset level.** Theorem (Type-uniform REDUCED SU1, doubly-laced): for every doubly-laced root system, every dominant pair, every bidegree, every odd-length (w, π) with c_i ≠ 0, there exists a unique REDUCED orbit-swap multiset realising the BGG-Verma matrix entry. Empirical: **20,116 REDUCED triples, 0 falsifiers** across B_2 + C_2 + C_3 + F_4 (11 simples, 4 ranks). Section 3 sign-tracking verified symbolically at C_3 (262 cases, 0 mismatches). v1 paper drafted: `proofs/2026-05-14-SU1-uniqueness.md`.

## The claim (final form)

Aug~ for doubly-laced types (B, C, F) is the bidegree-pointwise combinatorial form of the differential of the BGG-Verma resolution for the trivial representation L(λ) over Cat O.

Concretely: BGG's resolution
$$
\cdots \to \bigoplus_{w: \ell(w) = k} M(w \cdot \lambda) \to \cdots \to M(\lambda) \to L(\lambda) \to 0
$$
has differential at length-$k$: $d_k = \sum \pm \mathrm{nat}_{w, s_i w}$ along **LEFT** simple-reflection moves. Δℓ = ±1.

Evaluating at the (q, t)-bidegree-pointwise component collapses this to a sign-reversing involution on (w, π)-pairs at fixed bidegree. The π-difference under each move is a unique REDUCED orbit-swap multiset (proved Day 11 SU1).

## The four pillars (proof structure, v1)

1. **(A) `w' = s_i · w` (LEFT mult).** Confirmed at B_2 (1090/1090), B_3 (27,407/27,407), C_3 (6906/6906), F_4 (78,428/78,428).
2. **(B′) π-difference is a sum of orbit-swaps within one s_i, possibly multi-subtype and possibly opposite-direction.** Same datasets.
3. **(SU1) REDUCED orbit-swap multiset is UNIQUE.** Proved Day 11 via orbit-decomposition of the s_i-action on Φ^+ \\ {α_i}. **Rank-independent and type-uniform.** 20,116 triples, 0 falsifiers across 4 ranks × 2 classical + 1 exceptional.
4. **(Section 3) BGG matrix entry coefficient factorises as K(π, π') · ∏ chain-product, K ∈ ℤ_{>0}.** Verified symbolically at C_3 (262 cases). Phantom RAW multisets are not BGG terms.

**Note (Day 11 simplification):** Earlier drafts (v0) carried a Phase C "induction on rank via parabolic Levi reduction." This was over-elaboration. Phase B's orbit-decomposition uses only s_i-orbit disjointness on Φ^+ \\ {α_i} and signed-count recoverability from (π, π'). Neither uses rank. v1 deletes Phase C.

## Priority and prior work

**Hemelsoet-Voorhaar arXiv:1911.00871 (J. Algebra 2020)** is the closest existing computational treatment. They compute BGG differentials as UEA elements in U(𝔫⁻) — NOT in Kostant-partition-basis matrix-entry orbit-swap form. 5 total citations in 7 years. The BGG-matrix-entry-by-Kostant-basis computation space is virgin territory.

**Malikov-Feigin-Fuks 1986 (CORRECTION 2026-05-13):** MFF at q=1 gives closed-form singular vector formulas for ALL positive roots of any finite-dimensional semisimple Lie algebra — including doubly-laced. The "straight root" restriction I'd been carrying is Dobrev 1991's quantum (q≠1) limitation, not MFF's. **Implication: Section 3's coefficient existence and form has a 40-year-old theoretical foundation. MFF is a co-verification of Section 3, not a fallback.** The orbit-swap REDUCED-multiset combinatorial form remains new; the existence and form of the coefficient is not. Adjust priority-claim language accordingly in v1.

**Other adjacent papers** (browse 2 2026-05-13):
- Shapovalov elements arXiv:2301.02624 (J. Algebra 2024): explicit Verma map formulas via R-matrix. Independent algebraic path to the same coefficients.
- Sale arXiv:1710.09966: singular vectors for superalgebras via subalgebra reduction. Related but not overlapping at the doubly-laced level.
- Hirota arXiv:2512.16095 (2025): superalgebra BGG via odd reflections. Doubly-laced/superalgebra analogy may be deeper than cosmetic.

## Sub-results within (A) + (B′) + SU1

### B_2 (rank-2, doubly-laced classical)
Test: `bgg_aug_compare_B2.py`. 4 dominant integer pairs, 1090/1090 Aug~. Move-classes clean: s_2 swaps k×α_1 ↔ k×(α_1+2α_2) for k∈{1,2}; s_1 swaps k×α_2 ↔ k×(α_1+α_2) for k∈{2..7}. Each move-class leaves the orthogonal root pair fixed.

### B_3 (rank-3, doubly-laced classical)
Test: `bgg_aug_compare_B3.py`. 798 dominant spin pairs, 27,407/27,407. Pure single-subtype 97.56%; mixed 2.44%. Refutes the rank-2 (B) "single root-pair swap" framing; sharpens to (B′).

### C_3 (rank-3, doubly-laced classical, B/C dual)
Test: `bgg_aug_compare_C3.py`. 406 dominant integer pairs, 6906/6906. **New phenomenon: opposite-direction mixed swaps within one s_i** at short exchange simples s_0, s_1 (mixed unit-sizes: 2-unit LL + 1-unit b/c). Spin-lift doesn't work for C_n (ρ_C integer); integer λ is the right test set.

### F_4 (rank-4, doubly-laced exceptional)
Test: `bgg_aug_compare_F4.py`. 20 dominant integer pairs, 78,428/78,428. F_4 short simples s_2, s_3 carry **mixed unit-scale orbits** (4×1-unit + 3×2-unit each). C_3's abstraction *mixed-unit-scale ⟹ opposite-direction required* predicted F_4 behaviour correctly. Opposite-direction (long-pair forward + short-half backward) explicitly verified inside s_3.

### Section 3 sign-tracking (Day 11)
Test: `section3_sign_tracking_C3.py`. Symbolic PBW expansion of $f_{\alpha_i}^c \cdot \pi(\mathbf{f})$ in C_3 negative-root algebra with abstract Chevalley constants. Each same-bidegree fully-absorbed target $\pi'$ gives coefficient factoring as $K(\pi, \pi') \cdot \prod_{st} (\text{chain product})^{m_{st}}$, $K \in \mathbb{Z}_{>0}$ a positive combinatorial multinomial. **262 cases, 295 same-bidegree targets, 0 mismatches.** Phantom RAW multisets do not appear in the BGG PBW expansion — they were always Diophantine artefacts.

### SU1 (Day 11)
Tests: `su1_phase_a_C3.py`, `su1_phase_a_B2_C2.py`, `su1_phase_a_F4_full.py`. Grand total: 20,116 REDUCED triples, 0 multi-solution falsifiers across B_2 (2 simples), C_2 (2 simples), C_3 (3 simples), F_4 (4 simples). RAW failures occur at the expected rate (98ish per F_4 simple, similar at C_3); all collapse to REDUCED-unique.

## Empirical consequences and structural payoff

1. **Two distinct co-structures on K_0:** BGG-differential (Aug~, AL, Δℓ=±1) vs. cactus (ψ_J, GY, Δℓ=±2 within cells, Schützenberger-evac at S_n). The Day-5 "three lifts are one lift" framing was too unifying.

2. **Acyclicity-is-positivity refined:** Aug~ achieves bipartite max matching at every bidegree; unmatched + unused items equal BGG cohomology dimensions. Per-bd identification holds even when bidegree is non-acyclic.

3. **84% greedy failure was structurally informative:** local greedy rules can't reproduce global BGG cancellation (3-stratum non-locality). The "bug" became feature evidence that Aug~'s real target is a categorical / chain-level object, not a pointwise rule.

## Open extensions

1. **MFF cross-check (P0.1).** ✗ NOT APPLICABLE (verified 2026-05-14). MFF computes singular vectors at π=∅ (highest-weight column of a multi-step composite BGG embedding); Section 3 is universal single-step PBW commutator for arbitrary π. Different objects. Section 3's actual classical foundation = Chevalley-Serre PBW (Bourbaki, Humphreys, Garland). MFF is a consequence, not an alternative. Correction email sent to Robin.

2. **Type-D version (single-graded).** D_4 simply-laced, so (q,t) bigrading collapses to single-graded. The single-graded BGG-differential = Aug~ identification would re-derive Elias-Williamson positivity combinatorially. Less new math; do later.

3. **G_2 scope-clarifying test.** Triply-laced. Optional. Confirms doubly-laced is the right scope.

4. **Coideal categorical home.** Watanabe 2509.00853: any type-B BK involution must respect coideal subalgebra action. See `coideal-subalgebra-as-aug-tilde-home.md` (updated 2026-05-14 with CST bridge + on-slice/off-slice split).

5. **Aug~ as strict extension of Kashiwara crystal action (2026-05-14, NEW).** CST bridge B_2 hand-check gave PARTIAL verdict: Aug~ pulls back to a Z-linear combination of e_i / f_i on the open-crystal slice (1 reduced step = k Kashiwara steps), but keeps acting off-slice where Kashiwara returns 0. **SU1 REDUCED uniqueness is NOT a corollary of Kashiwara uniqueness — the doubly-laced off-slice gap is the genuine novelty.** See `aug-tilde-as-crystal-extension.md`.

6. **Kostant-game connection.** REFUTED 2026-05-14 — different state spaces, only shared upstream cause (doubly-laced asymmetry n_{i,j} ≠ n_{j,i}). Footnote only. See `kostant-game-and-reduced-uniqueness.md`.

7. **Non-acyclic interior.** Where (q,t)-Lusztig has negative coefficients. d^2 ≠ 0 in some restricted sense; concrete combinatorial obstruction. Long-term.

## Caveats

- Scalar/sign in Ext^1 of BGG not verified — only the combinatorial identity (partner-by-left-mult-by-s_i), the π-swap structure, and per-bd Euler-char identification. Load-bearing parts are done; scalars are conventional.
- Doubly-laced framing is canonical; simply-laced (D, A) inherit (B′) only at single grading.
