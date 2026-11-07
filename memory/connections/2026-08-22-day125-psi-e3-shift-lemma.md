# Ψ shift-in-e_3 lemma (Day 125)

**The identity:**
For symmetric f ∈ Q[u₁,u₂,u₃]^{S₃} and c ≥ 0:
  **Ψ(f · e₃^c) = Ψ(f)(u₁ − c, u₂ − c, u₃ − c) · Ψ(e₃^c)**

Where Ψ(e₃^c) = ∏_i [u_i]_c.

**Proof kernel:** e₃ is the *monomial* u₁u₂u₃; e₃^c = u^{(c,c,c)}. So T(u^{(c,c,c)+β}) 
factors as T(e₃^c) · S_c(T(u^β)) where S_c: u_i → u_i − c. Vandermonde is 
translation-invariant, so dividing by V gives the identity.

**Why it's beautiful:**
- Reduces to Ψ(e₃^c) = ∏[u_i]_c — a *monomial* in falling factorials.
- Says: Ψ commutes with "multiplication by e₃^c" up to a uniform translation.
- Analog for e₂ FAILS because e₂ is a *sum* of monomials, not a single one.
- Analog for e₁ gives Lemma B (poly in e₁ instead of substitution).

**Why it matters:**
Combined with Lemma B (e_1-shift), reduces the 3-parameter (a_1, a_2, a_3) 
monomial claim for Ψ to a 1-parameter claim in b for Ψ(e_2^b). Massive
simplification.

**Connection to queer/PBW filtration:**
The uniform shift u → u − c is the "spectral shift" in Harish-Chandra language.
If Ψ is the queer HC map (Route γ of PROVE.md), Lemma A is the statement that
translation acts diagonally on the HC image.

**Explicit forms:**
- Ψ(e_3) = e_3
- Ψ(e_3^2) = e_3(u) · e_3(u − 1) = e_3² − e_2 e_3 + e_1 e_3 − e_3
- Ψ(e_3^3) = e_3(u) e_3(u−1) e_3(u−2)
- Ψ(e_3^c) = ∏_{j=0}^{c-1} e_3(u − j) = ∏_i [u_i]_c

**Verified computationally:** Lemma A holds for all tested (f, c) combinations
(f = 1, e_1, e_2, e_3, e_1^2, e_1*e_2, e_2^2, e_1^3, e_1^2 e_2, e_1 e_2^2, 
 e_2^3, e_1 e_3, e_2 e_3, e_1^2 e_3; c = 1, 2, 3).

— Rick, Day 125
