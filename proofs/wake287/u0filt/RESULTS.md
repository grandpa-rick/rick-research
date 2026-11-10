# Wake 287 — Q71 U_0-variant: (ρ(U_0), H_N(0)) filtrations of V^{⊗N}. Grade: **computed**. Date 2026-11-10.

## Conventions

These are identical to `wake286/q3filt/core.py`, which is copied here.

- **H-action.** H_N(0) acts on the right by Jung–Oh 2509.26194 (4.5), with π̄_i² = −π̄_i. On a word with letters (a, b) in positions (i, i+1), π̄_i acts as: swap if a<b, −1 if a>b, 0 if a=b.
- **U_0-action.** U_0(gl_n) is as in Jung–Oh Def 4.2, with the Def 4.2 coproduct:
  - Δe_i = 1⊗e_i + e_i⊗k_i
  - Δf_i = k_{i+1}⊗f_i + f_i⊗1
  - Δk_i = k_i⊗k_i
  - ρ_V(e_i) = E_{i,i+1}, ρ_V(f_i) = E_{i+1,i}, ρ_V(k_i) = Σ_{j≠i} E_jj.
- **Generators used.** Iterating the coproduct gives:
  - e_i = Σ_p 1^{⊗p−1} ⊗ E_{i,i+1} ⊗ k_i^{⊗N−p}
  - f_i = Σ_p k_{i+1}^{⊗p−1} ⊗ E_{i+1,i} ⊗ 1^{⊗N−p}
  - k_i = (Σ_{j≠i} E_jj)^{⊗N}

  We checked that the U_0 operators commute with ρ(H).

## Dims (exact over Q; `dims_check.py`)

| (n,N) | dim ρ(U_0) | dim S_0 = End_H(V) |
|---|---|---|
| (2,3) | 19 | 20 |
| (2,4) | 31 | 35 |
| (3,3) | 165 | 165 |
| (2,5) | 46 | (not computed) |

The (2,3) and (2,4) values reproduce Wake 286 and KT NCSF V Note 5.7.

## Method (`u0filt.py`, n = 2, exact sympy)

1. **Trivial block.** Let π_i = 1+π̄_i (idempotent) and ε = π_{w0}. Then ε is a central idempotent of H: π̄_iε = επ̄_i = 0, so it is the block of the simple projective M_(N) = C_∅.
2. **Splitting V.** V = T ⊕ Y with T = V·ε and Y = V·(1−ε). Both are stable under A = ⟨ρ(U_0), ρ(H)⟩, so chains decouple across T and Y.
   - T ≅ M_(N)^{N+1}.
   - ρ(U_0)|_T is the full matrix algebra ((N+1)²: 16, 25, 36 for N = 3, 4, 5). So T = L_(N) ⊠ M_(N) with L_(N) simple, and T can be placed anywhere in a chain.
3. **Structure of Y.** Y = ⊕_{a=1}^{N−1} P_(a,N−a), where P_(a,N−a) = Y ∩ weight(a zeros, N−a ones). Each type occurs once. End_H P is local (Q or Q⊕nilpotent, checked).
   - So any H-direct summand of type P_i is a graph {x+φx}, with φ ∈ Hom_H(P_i, rest).
4. **Search.** The bottom layer is an A-stable graph. Stability is the quadratic system g21 + g22φ = φ(g11 + g12φ) for every generator g, solved exactly. Then pass to the quotient (g ↦ g22 − φg12) and recurse.
   - In Y each type occurs once, so the weak form (isotypic projective layers) and the strong form (L ⊠ M_I, each I once, L 1-dim) coincide on Y.
   - Since T is simple, **weak ⟺ strong** here.
5. **Controls.** If f_0 or e_0 is dropped (or both), the search finds chains (`control.py`). So the solver is not vacuous.

## Results

| (n,N) | ρ(U_0)\|_Y vs End_H(Y) | weak form | strong form | reason |
|---|---|---|---|---|
| (2,3) | 3 vs 4 | **NO** | **NO** | no A-stable bottom piece of either type (0 solutions, no free families) |
| (2,4) | 6 vs 10 | **NO** | **NO** | no A-stable bottom piece of any of the 3 types |
| (2,5) | 10 vs 20 | **NO** | **NO** | no A-stable bottom piece of any of the 4 types |
| (3,3) | ρ(U_0) = S_0 | **NO** | **NO** | the PROVE 287 Theorem′ applies verbatim, since the acting algebra is the full commutant (no search run) |

## Mechanism at (2,3)

Write W = P_(2,1) for the weight space of u_p (one letter 1) and W′ = P_(1,2) for that of v_p.

- ρ(U_0)|_Y = span{1_Y, e_0|_Y, f_0|_Y}, which is 3-dim.
  - f_0|_Y : W → W′ is nonzero, so it spans Hom_H(W,W′) (the map f of PROVE 287).
  - e_0|_Y : W′ → W is nonzero and spans Hom_H(W′,W) (the map g).
- The element of S_0 that is **missing** from ρ(U_0) is the weight idempotent separating W from W′ (1_W − 1_{W′}). Lemma 1 of PROVE 287 never needs that element.
- The two elements Lemma 1 does need (f∘p and g∘p) are realised by f_0 and e_0.
- **Direct argument.** Suppose X ≅ W is a bottom piece, i.e. a graph over W. Then f_0X = f_0W ⊂ W′ is nonzero, but X ∩ W′ = 0. So no such X exists, and symmetrically for W′ using e_0.

So the Hom 2-cycle W ⇄ W′ is realised inside ρ(U_0) itself. The U_0-variant fails for the same reason as the S_0 version. The larger U_0-stable lattice does not help.

## Doubts / scope

- The hunch "U_0-variant could differ" is **dead at (2,3), (2,4), (2,5), (3,3)**. This is computed; a proof for general (n,N) is not written.
  - A likely general route: show that f_i and e_i restricted to the hook summands are nonzero, which would make the Lemma 1 argument go through with ρ(U_0) in place of S_0. This is unverified.
- The convention dependence of "character F_I of L" is not tested. It is moot, since NO already holds for the weak H-only form.
- If another U_0 convention were used (e.g. KT NCSF V's own coproduct), ρ(U_0) could differ. The Wake 286 dim match 19/20 with KT Note 5.7 suggests the images agree, but this was not checked.
