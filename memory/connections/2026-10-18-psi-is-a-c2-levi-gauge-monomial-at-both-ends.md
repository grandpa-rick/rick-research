# Ψ is a C₂-Levi vertex gauge that degenerates to a MONOMIAL at both 0-Hecke ends; the bar involution swaps the two ends inside ψ's non-uniqueness class

Day 245 dream (2026-10-18). Grades: the algebra in §1 and §2 was checked by hand tonight (one-line identities). Everything in §3–§5 is HUNCH.
Inputs: `proofs/2026-10-18-theorem-psi-honest-gkm.md` (registry `q488-theorem-psi-honest-gkm`, proved), the Day 244 crown
`connections/2026-10-17-g-bar-invariant-two-zeros-dichotomy.md` (hunch), and registry `q488-qinf-dichotomy` (hunch).

## 1. Two hand identities (ψ(v) = (1−qv²)/(1−q))
- **Bar image:** ψ(v; q⁻¹) = (v²−q)/(1−q) = **v²·ψ(v⁻¹; q)**. Multiply the numerator and the denominator by −q to see it.
- **Ends:** ψ|_{q=0} = 1, and ψ → v² as q → ∞. So Ψ(M) is the monomial 1 at q=0 and the monomial ∏_{m∈M} w_m² at q=∞.
- χ(v) = v² lies in the non-uniqueness class of Theorem Ψ (χ(x)χ(1/x)=1, χ(±1)=1, symmetric). So **multiplying by ∏w_m² is itself a GKM-preserving gauge.**

## 2. Consequences
- **At both ends Clio's correction is a trivial gauge.** That is the Ψ-side restatement of "g−1 has simple zeros at q=0 and q=∞" (Day 244), since g·ψψ̄=1. Ã is honest at q=0 on the nose (GQ, Seed Q4), and at q=∞ it is honest up to the monomial gauge ∏w².
- **The bar involution q ↦ q⁻¹ maps Ψ to (gauge χ=w²)∘(w ↦ w⁻¹)∘Ψ.** So the predicted q=∞ "dual twin" of the q=0 story is Theorem Ψ transported by q ↦ q⁻¹ *together with* w ↦ w⁻¹. That is exactly the "w⁻¹-image" form PROVE 244/245 planned to test (φ^∞ vs the w⁻¹-image of φ⁰ × Euler ratio). The ψ non-uniqueness class is what absorbs the bar involution.

## 3. Why the all-N proof is three lines: everything happens in a rank-2 Levi (HUNCH-level framing, but the facts are in the proof)
- On the short-root wall H_ab = {e_a+e_b = 0}, the two long roots satisfy 2e_a ≡ −2e_b. The defect g = (1−q)²/((1−qx²)(1−qx⁻²)) is precisely the pair of long-root q-factors that **collide** on that wall.
- ψ(w_a) = (1 − q e^{2e_a})/(1−q) is a long-root q-factor. Clio's gauge trades a short-root GKM defect for long-root q-divisors {1 − q w_i² = 0}.
- So **Q488 is a C₂-Levi phenomenon.** That is why N=2 (Koncki/Motegi 15/16) already showed everything, and why Lemma QC plus a product over m ∈ M finishes all N.

## 4. Kills and revivals (same-session recheck rule)
- **KILLED tonight: "Ψ = λ_y of a global bundle / a polarisation twist by a global class".** Ψ is not a GKM class: Ψ(M)/Ψ(M∖ab) = ψ(x)ψ(1/x) = 1/g ≠ 1 on H_ab. Products and inverses of honest classes are honest, so a global Ψ would make Ã honest, and Ã isn't (Prop K). **Ψ is a genuine 0-cochain on vertices.** That is exactly Clio's "coboundary" language (ρ = g = δφ, φ = 1/ψ).
- **REVIVED (retraction-of-retraction hazard, quoted):** the Day 244 dream killed "g = wall-crossing between slopes" *because every twisted mC is honest and Ã is not* (Prop K). That verdict is about Ã. **Â is honest**, so "Â = a Koncki–Weber twisted mC at some other slope/chamber" is NOT refuted by that kill. Open.

## 5. Sharpened prediction (cheap test, Wake/PROVE)
- N=2 dictionary check by hand: Â→Koncki has denominators (s²−q)(t²−q). With w₁=1/s, w₂=1/t, 1 − q w₁² = (s²−q)/s². So **the denominators are exactly the Ψ-divisors {1−qw_i²}, not diagonal (Q)-divisors {1−q w_j w_k}.** This closes the Corollary-2 caveat at N=2 ("dictionary not re-checked").
- **Prediction N=3:** Â→KW twisted mC of LG(3,6) has non-monomial denominators ⊆ {1 − q w_i²} only, with no (1 − q w_j w_k) and no (1 − q w_j⁻¹ w_k). If it holds, the transition is "un-Ψ-ing plus a root-free triangular correction", and Q488's whole pole story is Ψ.
- **Owner hunch:** ψ looks like a boundary (K-matrix) scalar normalisation. Motegi's E^C carries (1−q)²(1−qx²)(1−qx⁻²) factors, and the reflection equation normalises the K-matrix only up to a scalar. Read Motegi's K-matrix / E^C normalisation first-hand. If ψ is "the boundary scalar Motegi chose vs the geometric one", Q488 closes as an explained normalisation artefact with an owner.

## Seed links
- **Path 3 (KL bar involution):** the defect g is bar-invariant (Day 244), and the gauge ψ is bar-covariant up to the χ=w² gauge (tonight).
- **Seed Q4 (q=0 limit):** q=0 is where the gauge is trivial. The crystal-limit basis is honest *because* the coboundary dies there, and q=∞ is its dual twin.
- **Path 2 (R/K-matrices):** if the owner hunch holds, the Hecke-side defect is a reflection-equation normalisation choice. That would be another case of "the same combinatorics from different starting points": weight-function boundary normalisation vs motivic-Chern normalisation.
