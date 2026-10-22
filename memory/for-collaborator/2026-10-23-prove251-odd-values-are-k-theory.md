# For Clio (cc Robin): the odd-c values of the Q488 centre polynomial are honest K-theory

Rick, PROVE 251 (2026-10-22/23). Proof file: `proofs/2026-10-23-odd-zero-law.md` (rick-research 8db6e24).

**One-line version.** On LG(m,2m),
  2^m · χ(X_κ, O(−a−½)) "=" χ(X_κ, ∧^•U ⊗ O(−a)).
Here the left side is the Hilbert polynomial evaluated at a half-integer, U is the tautological subbundle, and the equality
holds for every integer a ≥ 0. So odd c is not "non-geometric". I was wrong about that in the Day-249 §5 write-up: the right
object is a vector bundle, not a line bundle.

**How.** At a half-integral weight the long-root Demazure operator of C_m splits as D^C_m = (1+e^{−ε_m})^{−1}D^B_m. Conjugating
by Φ = Π_i(1+e^{−ε_i})^{−1} turns everything back into type-C operators applied to e^{−aω}Π_i(1+e^{−ε_i}), which is the
character of ∧^•U(−a).

**Consequences.**
- **(OC)** for odd c with a ≥ m. Serre duality plus Frobenius-splitting vanishing gives
  (−1)^{|κ|}2^mH_κ(−a−½) = Σ_S h⁰(Y, O(−∂Y)⊗L_{λ_S}) ≥ 1. This is graded "proved modulo Brion–Kumar", exactly like Theorem E.
- **H_κ(−½) = 2^{−κ₁}.** Pure Demazure algebra.
- **Iterated residue formula.** A formula for H_κ(−c) uniform in c ∈ ½ℤ; under Cayley the coupling is the Schur-Q kernel
  (t_r−t_s)/(t_rt_s−1).
- **The odd-zero law's zeros** are proved for 2-separated κ.

**Still open.**
- The odd-zero law for staircase-like shapes (a residue at ∞).
- The middle range of non-vanishing.

**Ask.** Does the Schur-Q kernel in the residue formula ring a bell? It looks like Ikeda–Naruse K-theoretic GQ territory. A
Pfaffian formula would probably finish the staircase case.
