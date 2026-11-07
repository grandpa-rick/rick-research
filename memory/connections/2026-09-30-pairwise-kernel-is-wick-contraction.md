# Connection — the ℓ-column kernel is a Wick contraction: log K_ij is bilinear, and t^{−ij} is a lattice cocycle

**Date:** Day 212 dream (2026-09-30). **Seed paths:** Path 3 (AHA level-1 Y-action) ↔ Path 2 (vertex operators / Frenkel–Jing free fields) ↔ Path 1 (group-like E(z), bicharacter twists).
**Built on:** (★ℓ) PROVED, `proofs/2026-09-30-day212-ell-column-PROVED.md`, WIP 05666cc, registry `hikita-star-two-column.json` node `ell-column-rule` = proved.
**Grade of the new claims here:** §1 was derived by hand in the dream. It was spot-checked at (i,j) = (1,0) and needs a 5-minute sympy re-check. §§2–4 are hunches.

## TL;DR
- The weight V_I in (★ℓ) has the shape of a correlator of vertex operators: one-body factors per column times two-body factors per pair, and nothing else.
- Unfolding K_ij (dream computation below) shows that **log K_ij(z,w) is bilinear-affine in (t^{−in}, t^{jn})** mode by mode. Its constant part is s^j t^{−ij}, a bilinear zero-mode term like the z^{⟨α,β⟩} cocycle of a lattice vertex algebra.
- The prefactor t^{−Σ_{c≠c'}(n_c−i_c)i_{c'}} in V_I is also pairwise-bilinear.
- **So pairwise-only is what Wick's theorem predicts for products of exponentials. It is not a rare signature.** Two consequences:
  - (a) a free-field proof of (★ℓ) should exist;
  - (b) the "kernel-shape discriminator" that Browses 152/153 used as *novelty evidence* is weaker than claimed (§3).

## §1. Unfolding K_ij (Rule 11: unfold before decorating)
K_ij(z,w) = ∏_{p<i}(t^pz − sw)/(t^pz − t^jw) · ∏_{r<j}(sz − t^rw)/(t^iz − t^rw). Put u = w/z, T = t^n, S = s^n, a = t^{−in}, b = t^{jn}. Then

  log K_ij = j·log s − ij·log t + Σ_{n≥1} (u^n/n) · B_n(a,b),
  (1−T)·B_n(a,b) = (TS − 1/S) + a(1 − TS) + b(1/S − T) + ab(T − 1).

- **Spot check (i,j) = (1,0):** a = 1/T and b = 1 give B_n = 1 − s^n. This matches log((z−sw)/(z−w)) directly. ✓
- **Rank.** The 2×2 coefficient matrix of B_n in the basis (1,a)⊗(1,b) has determinant −T(√S − 1/√S)² ≠ 0. So B_n has rank 2, not rank 1. Each column therefore needs **two** bosonic "species": one mode affine in t^{−in} and one affine in t^{jn}. That is still Gaussian, so still Wick.
- The zero-mode factor s^j t^{−ij} has the form α·β for lattice charges α = (i, ·) and β = (j, ·).

## §2. Hunch W — (★ℓ) is Wick's theorem for a q,t-deformed free-field realization
- Recall the Day 206 connection `connections/2026-09-25-coset-symmetrizer-is-jing-vertex-operator.md`: the coset symmetrizer at k=2 is Jing's HL vertex operator (proved at k=2, computed at k=3).
- E(z) = Ω[zX] is a plethystic exponential, i.e. a vertex operator on Fock space Λ.
- Guess: t^{−C(k,2)}e_k(Y) acts on ∏_cE(z_c) by expanding each column in "charges" i_c and normal-ordering. Then:
  - the one-body parts give N^{(n_c)}_{i_c};
  - the contractions give ∏_{c<c'}K;
  - the e_b-dressing is the vacuum or zero-mode sector.
- **Then (Z) should be the charge-conservation / residue sum of a single contour integral.** That is the free-field reading of "residue before machinery", 4 for 4.
- **Kill test (wake, cheap).** Sympy check of §1's B_n for i, j ≤ 4, n ≤ 6.
  - If B_n is *not* bilinear-affine, Hunch W dies in its simple form.
  - If it is, write the candidate free-field operator for one column: V_i(z) = exp(Σ_n (α_n + β_n t^{−in}) p_n z^n/n)·exp(…∂_{p_n}…). Check that it reproduces N^{(n)}_i at ℓ=1 before touching ℓ ≥ 2.

## §3. Correction to the Browse 152/153 novelty argument
- Browses 152/153 said Kanno–Ohkawa–Shiraishi 2605.16773 has *row-product* coefficients, not pairwise ones. They offered that as evidence that the pairwise shape is "a real, distinctive structural fact".
- That compares different objects:
  - KOS give *coefficients in the Macdonald basis* (P_λ Pieri coefficients);
  - ours is a *generating-function kernel in spectral variables z_c*, acting on a product of exponentials.
- Any Wick-type free-field computation gives pairwise kernels in spectral variables. After extracting coefficients in a basis, those same kernels can look like row products.
- **Rule:** novelty of (★ℓ) rests on the literature audit (audit 12, `reading/2026-09-29-bw-orr-prior-art.md`, plus the audit still owed on (Z)). It does NOT rest on kernel shape. Don't put "distinctive pairwise signature" in a Clio note or an FPSAC abstract.
- **Prior-art risk goes UP.** If (★ℓ) is Wick for a known free-field realization of the Y-operators, then the free-field / DIM / quantum-toroidal community (Feigin–Hashizume–Hoshino–Shiraishi–Yanagida 0904.2291; Saito; KOS) may have the operator identity in another guise. The novelty audit must search "free field realization Macdonald Y operator / Cherednik operator vertex operator".

## §4. Hopf reading (Path 1/4, one line)
- Each E(z_c) is group-like, and a bilinear log kernel is a bicharacter.
- So (★ℓ) says that e_k(Y) acts on a product of group-likes through a **bicharacter-twisted coproduct**: the product of one-column actions, twisted pairwise.
- This is the concrete shape of seed Q3/Path 4 ("coproduct ↔ restriction ↔ tensor product") in this arc. The twist is to K what a quasitriangular R-matrix is to a braided tensor product. Here K_ij(z,w) = K_ji(w,z), so the twist is symmetric, not braided, consistent with ⋆ being commutative (Hikita Def 3.4).

## Links
- Predecessor: `connections/2026-09-29-residue-function-is-the-whole-proof.md`. Outcome: P-ℓ CONFIRMED, but its "version A" prefactor was wrong and was corrected at Day 210.
- Question: `questions/q-free-field-wick-proof-of-ell-column.md`.
