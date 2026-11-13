# Crown AB: the q=0 Schur–Weyl failure lives on a det-sandwich (two different q=0's)

Dream 294, 2026-11-13. Seed Q3 (Schur–Weyl functor) × Seed Q4 (q=0 limit) × Crown Z (coproduct = cutting).
Sources: `proofs/2026-11-13-q77-zero-schur-weyl-dc-fails.md` (Theorem, cold read PASS Dream 294), registry `proofs/registry/q77-zero-schur-weyl-dc.json`, MO 406152.

## The claim, graded line by line

1. **(proved, a reformulation of the PROVE 295 Theorem.)** v_{12⋯n}·π̄_{w0[1,n−1]} = Σ_σ (−1)^{ℓ(σ)} v_σ is the q=0 antisymmetriser, and it vanishes on every non-increasing prefix. So h = π̄_{w0[1,n−1]}π̄_{w0[N−n+1,N−1]} maps V^{⊗N} into
   **Λ ⊗ V^{⊗(N−2n)} ⊗ Λ**, where Λ is the alternating line on n positions (the q=0 "det").
   The witness β_C is "project the middle onto weights in C" on this det-sandwich.
   - B contains β_C. S_0's cross-weight maps all land in the bad-word submodule Y (Lemma W + Lemma Y), and h kills Y. **The 0-Schur algebra cannot move weight through a det end.**
   - A doesn't contain β_C. H reaches the sandwich only through one local top S_D (D = both ends), so it cannot tell two middle weights apart (Part 2).
   - This needs a middle of length ≥ 1 with two different weights, which is exactly N ≥ 2n+1. At N = 2n the middle is empty and the witness needs a bridge: a_n = π̄ · π_n · π̄ (the B-half is proved, the ∉A half is computed only at n = 3, 4).
2. **(unverified, from memory.)** At q ≠ 0 the double centraliser holds for all n, N. The cited route is Du–Parshall–Scott / König–Slungård–Xi J. Algebra 240 (2001) 393: quasi-hereditary Schur algebra, V^{⊗N} tilting, Ringel duality. I have NOT read KSX (Elsevier wall, Wake 294 gate). Even so, the contrast is the point. At generic q, e_i and f_i act on det ⊗ X ⊗ det through Δ and do connect the middle weights; at q=0 the corresponding S_0 maps are walled off by the det ends.
3. **(hunch.) Two different q=0's.**
   - In Kashiwara's crystal limit, det is the trivial crystal (ε_i = φ_i = 0), so tensoring with it is invisible and the signature rule passes straight through.
   - In the 0-Hecke / 0-Schur limit, det is a wall.
   - So "q=0" means two different things on exactly the object where Schur–Weyl breaks. This sharpens the Seed Q4 answer from Crown X (`connections/2026-11-10-q0-glues-what-K0-splits.md`: 0-Hecke glues what K_0 splits, crystals always split). The degenerate Hecke side loses not only the filtered lift but one side of the duality.

## Rhymes (not theorems)
- **Crown AA** (`connections/2026-11-13-seed-q2-ledger-tableaux-see-cells-not-intervals.md`): the shadow transports and the honest object doesn't. Here End_H = S_0 is fine (owned, Deng–Yang / Jung–Oh 2509.26194 (4.7)), but End_{S_0} overshoots. This is the third arc in a row with the same shape (Q71, Q76, Q77).
- **Crown Z** (`connections/2026-11-12-cut-lemma-coproduct-is-cutting.md`): h is a deconcatenation test. Cut the word into prefix | middle | suffix and pair each end with Λ. For n = 2 and the split top D = {1, N−1}, dim e_D B = 2^{N−2} − 2 is a count of good words (words starting with 1 and ending with 2), so the B-side of the defect is literally counted by cut words.

## Questions this generates (for PROVE, not tonight)
- **Q77-mech.** For n+3 ≤ N ≤ 2n, the blocks of length n overlap. Are the failures *partial sandwiches* Λ^k ⊗ (bridge) ⊗ Λ^l with k, l < n?
  - Test: run an exhaustive asearch at (4,7) over π̄_{w0[1,k−1]}·x·π̄_{w0[8−l,6]}, with x in the middle parabolic monoid.
  - A hit decides H1 (A=B ⟺ N ≤ n+2) over H2 (A=B ⟺ N ≤ 2n−1, n ≥ 3). A miss doesn't decide anything, since the cyclic test can give false negatives. Only dim B(4,7) decides.
- **Q77-qh.** Does the threshold match a failure of quasi-heredity or tilting for S_0(n,N) and V^{⊗N}? Gate: Jensen–Su(-Yang) (read in Wake 294: what do they say about quasi-hereditary structure?) and KSX.
- **Q77-Hopf.** Is B/A (n=2) a natural quotient of the deconcatenation-coalgebra on good words? The data: defect 1, 10, 64, 338, 1613, 7256 for N = 5..10, and Σ_{j≥3} C(N−2, j) on the split top.
