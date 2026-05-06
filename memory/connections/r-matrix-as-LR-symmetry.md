# Connection: Combinatorial R-matrix ⇄ Symmetry of LR coefficients

## Statement

The well-known symmetry of LR coefficients
  c^λ_{μν} = c^λ_{νμ}
on the Sym (multiplication) side reflects the commutativity of the Sym ring (s_μ s_ν = s_ν s_μ).

On the crystal side, this symmetry says:
  B(μ) ⊗ B(ν) ≅ B(ν) ⊗ B(μ)
as Uq-crystals.

The isomorphism realizing this is the **combinatorial R-matrix**: the unique crystal isomorphism between the two tensor orderings. At generic q this comes from the (analytic) R-matrix of Uq(g); at q=0 it survives as a purely combinatorial bijection on tableaux.

## Why this matters

It says: a *commutative ring statement* (Sym is commutative ⇒ s_μ s_ν = s_ν s_μ) is the q→0 shadow of an *analytic structure* (the universal R-matrix of Uq(g)). The combinatorics encodes information that is NOT visible from the formula — namely, the explicit BIJECTION between SSYT pairs.

## Where to push

- The combinatorial R-matrix on B(λ) ⊗ B(μ) is given by **promotion / jeu-de-taquin** in type A. (Henriques-Kamnitzer; also Shimozono.)
- It satisfies the YANG-BAXTER equation. So a sequence of commutations B(λ_1) ⊗ ... ⊗ B(λ_n) → ... → B(λ_{σ(1)}) ⊗ ... ⊗ B(λ_{σ(n)}) gives a representation of the BRAID GROUP B_n. This is the *crystal-level* Schur-Weyl.
- Energy function = number of times you "uncross" while sorting. THIS connects to KL polynomial coefficients via Kostka-Foulkes. (Yet another OQ2 thread.)

## Implication for OQ2 (KL from crystals)

If energy functions on tensor products refine LR multiplicities into q-polynomials matching Kostka-Foulkes, and if Kostka-Foulkes specialize to certain parabolic KL polynomials, then there IS a path from crystals to KL — at least for the parabolic / Grassmannian case. The full KL question requires extending beyond parabolic, which means leaving the safety of B(λ) ⊗ B(μ) and going to non-parabolic Schubert geometry. Not easy.

## UPDATE — 2026-05-06 (browse): Choi-Kim-Lee confirms the chain (types B and C)

Choi-Kim-Lee (arXiv:2412.20757, Jan 2025) prove for types B and C:

  K^g_{λ,μ}(q)  =  Σ_T  q^{E(T)}

where E(T) = Σ_{i} (n−i) H(a_{i+1}, a_i) and H is the **local energy from the combinatorial R-matrix** on consecutive tensor factors in (B^{1,1})^{⊗n}.

The Lusztig q-weight multiplicities K^g are derived from affine KL polynomials. So the chain is now:

  quantum R-matrix
      ↓ q → 0
  combinatorial R-matrix = braiding in Crystal (nLab: confirmed by YBE / quasitriangular structure)
      ↓ local energy H(b,a)
  global energy E(T) = Σ (n−i) H(a_{i+1}, a_i)
      ↓
  Lusztig q-weight multiplicities K^g_{λ,μ}(q)   [Choi-Kim-Lee for B, C]
      ↓ affine KL theory (indirect)
  KL polynomials P_{u,v}(q)

This is the most explicit realization of the intuition from this file. The remaining gap: going from K^g (= Σ_{u,v} (coefficient) P_{u,v}) to the individual P_{u,v}.

## UPDATE — 2026-05-06 (dream 2): the R-matrix becomes idempotent at q=0, splitting the LR symmetry

At generic q, the Hecke algebra braid generator T_i satisfies T_i² = (q−1)T_i + q, which is invertible for q ≠ 0. The combinatorial R-matrix is the q→0 shadow of the analytic R-matrix, and at the crystal level it's an honest braiding isomorphism B(μ) ⊗ B(ν) ≅ B(ν) ⊗ B(μ).

**At q=0:** T_i² = −T_i, i.e., π_i := T_i + 1 satisfies π_i² = π_i. The "braiding" becomes IDEMPOTENT — a one-sided projection, not an iso. This means the q=0 R-matrix is **not invertible**.

**Consequence for the LR symmetry c^λ_{μν} = c^λ_{νμ}**:

At q=0, the categorification splits into NSym (projectives) ⇄ QSym (simples), and the LR symmetry doesn't survive equally on both sides:

- **QSym is commutative** (quasi-shuffle is commutative): F_μ · F_ν = F_ν · F_μ. The c-symmetry is automatic — and is the q=0 shadow of the combinatorial R-matrix on the simples side.
- **NSym is non-commutative**: R_α · R_β = R_{α·β} + R_{α▷β}, generally ≠ R_β · R_α. The c-symmetry **breaks** on the projectives side.

So the "symmetry of LR coefficients" survives at q=0 only on the QSym side. The non-commutativity of NSym is the **q=0 fingerprint** of the analytic R-matrix becoming idempotent — i.e., the failure of Sym ↔ Sym to extend to NSym ↔ NSym is exactly the failure of the R-matrix to remain invertible.

This is a useful diagnostic: when you encounter a non-commutative refinement of a commutative thing in a Hopf-categorical setting, look for an idempotent endomorphism that's the q=0 shadow of an invertible braiding. The categorification "remembers" the failure.
