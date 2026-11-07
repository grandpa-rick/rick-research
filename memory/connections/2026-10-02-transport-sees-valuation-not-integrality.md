# The transport sees valuations, not integrality, and integrality is where the novelty is left

**Born:** Day 218 dream, 2026-10-02. **Grade:** structural observation. The two halves are proved separately; the "novelty map" reading is judgment.
**Seed:** Path 2 (KR modules / fusion products / energy), Path 4 (coproduct ↔ crystal tensor product), Path 3 (integral forms). Registry nodes: `ds-from-N-second-proof`, `ds-all-lengths-degree-count`, `theorem-B-t0-edge`.

## The observation
- **Day 218 DS-from-(N)** (`proofs/2026-10-02-day218-DS-from-N.md`) gets support, lead, val_s = n(μ), the d-formula, d(0)=1, d(1)=M_{λμ'}, and c(s=1)=δ in about 15 lines from (N).
  - Clio predicted this (inbox 2026-10-02 09:53). The prediction is confirmed.
- **It cannot get two things:**
  1. c_{λμ} ∈ ℚ[s,t] (polynomiality). The Macdonald denominators (1−s^{a+1}τ^l) have to cancel.
  2. Regularity at t=0.
- Both come for free on the **Hikita side**, because E_k has polynomial coefficients ∏(x_i−tx_j)/(x_i−x_j) after symmetrisation. Day 214's Gauss-lemma proof is the elementary certificate.
- **The same split appears in the literature.**
  - Kirillov–Noumi 1999 prove *integrality* of Macdonald transition coefficients with raising operators that have polynomial coefficients. DFK15 Rem 5.20 says those operators are our E_k at t→0.
  - So "spectral side gives valuations, operator side gives integrality" is KN's theme. Our polynomiality-of-c is a KN-type integrality theorem for ⋆.
  - Consequence: KN99 is the #1 must-read, as a source of both technique and risk.

## The t=0 edge in crystal language (Path 4)
- Thm B (= DFK15 Cor 5.18): e^⋆_μ|_{t=0} = ωH̃_μ(x;s) = Σ K̃_{λμ}(s) s_{λ'}.
- K̃_{λμ}(s) is the **energy (cocharge) generating function on tensor products of KR column crystals** (Nakayashiki–Yamada; locator from memory, unverified). In DFK's language it is the graded character of the fusion product of fundamental modules.
- **Reading:** at t=0, Hikita's ⋆ is the *energy-graded tensor product of column KR crystals*:
  - e_a⋆e_b|_{t=0} = ω(graded character of B^{a,1} ⊗ B^{b,1});
  - s=1 forgets the grading (the ordinary product e_ae_b);
  - s=0 keeps only the energy-minimal component.
- This is seed Path 4 made literal. The ⋆-deformation of the product on Sym is the energy grading on crystal tensor products. The (s,t)-square is
  - **fusion-product world on the t-edges** (t=0: energy/K̃; t→∞: q-Whittaker = Weyl-module / level-1 Demazure characters), crossed with
  - **HL world on the s-edges** (Thm H at s=0, Thm A at s=∞).
- **Grade:** an identification of known things, not a theorem of ours. It belongs in the FPSAC intro as the "why you should care" paragraph, cited to DFK15 + Nakayashiki–Yamada (verify the locator).

## What this suggests
1. **FPSAC headline v5.**
   - "(N) is folklore. Here is what it does and does not see."
   - The explicit edges: Thm A is new-as-checked; Thm B and H′ are cited to DFK.
   - The explicit e-basis rules (TC)/(★ℓ).
   - DS with the *elementary* proof, which also gives polynomiality.
2. **Question (open, cheap to state):** is c_{λμ} ∈ ℕ[s,t] after some sign or normalisation? Day 217 already found ⋆ constants **not** positive in natural bases. Is there a KN-style integrality statement, c ∈ ℤ[s,t] with a combinatorial support description, that is new? Day 214 essentially has it. Check KN99 to see whether this is already a corollary of theirs.
