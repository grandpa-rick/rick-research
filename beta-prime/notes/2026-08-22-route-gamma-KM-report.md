# Day 125 — Route γ report: Kashuba–Molev arXiv:2512.21631 §5

**Date:** 2026-08-22
**Paper:** *Universal Capelli identities and quantum immanants for the queer Lie superalgebra*, Iryna Kashuba & Alexander Molev, arXiv:2512.21631v1 (25 Dec 2025), 25 pages.
**Local:** `/home/agent/papers/kashuba-molev-2512.21631.pdf` (`.txt` extracted).
**Task:** determine whether the queer HC identification closes the gap
`w(Ψ(e_2^b)) ≤ b` for Ψ = Okounkov–Olshanski shifted-Schur map on Λ*_3.

---

## 0. Executive summary

**Route γ does NOT close the gap in a straight read.** The KM paper is
beautiful and cleanly proves `χ(S^λ) = Q^+_λ(y)` — but the object on the
symmetric-function side is a *factorial Schur Q-polynomial* indexed by
**strict** partitions, living in the algebra Γ_N of supersymmetric polynomials.
Rick's Ψ maps to *classical shifted Schur functions* s*_μ indexed by
**ordinary** partitions, living in ordinary symmetric polynomials Λ*_3. Under
the queer HC these are DIFFERENT algebras / DIFFERENT bases; the identification
"Ψ = queer HC" as stated in the Route-γ hypothesis is incorrect at face value.

Route γ can perhaps be salvaged (the "(2c+1)-shift = queer content doubled"
alignment is not accidental — KM's contents κ_a(U) = ±√(σ(σ+1)) with σ = j−i
DO produce the shifted content pattern), but the direct closure via
"|λ| ≤ b in the Q^+_λ expansion" argument does not work. Section 5 gives no
direct hook to bound the (1,1,2)-weight of e_2^b under Ψ.

## 1. What §5 actually proves

**Theorem 5.2 (KM, p. 20).** Under the queer Harish-Chandra isomorphism
`χ : Z(U(q_N)) → Γ_N` (supersymmetric polys in y_1,…,y_N),
`χ(S^λ) = Q^+_λ(y_1,…,y_N)`,
where S^λ is the quantum immanant `str EU (F_1+κ_1(U))…(F_n+κ_n(U))` (eq. 5.1)
and Q^+_λ is Ivanov's factorial Schur Q from eq. (3.1).

**Corollary 5.3.** The image of S^λ in differential operators acting on
poly(x_{a,k}) is `2^⌊ℓ(λ)/2⌋ / (2^n n!) · str X^λ X_1…X_n D_1…D_n`.

**Remark 5.4.** S^λ, Nazarov's Capelli C_λ, and Alldridge–Sahi–Salmasian's z_λ
are all mutually proportional; only the sign convention for y differs.

The proof method is **exactly** the Okounkov 1996 template:
1. Top-degree component of χ(S^λ) is Q_λ(y) (ordinary Schur Q) — proved via
   Sergeev duality + Prop. 3.1: the highest-weight scalar's top degree is
   `str EU Y_1…Y_n = Q_λ(y)` (eq. 3.6).
2. χ(S^λ) vanishes on all shifted diagrams µ with |µ| < |λ|. This uses
   Corollary 4.3's *even Capelli identity* — the differential-operator image
   annihilates all polynomials of degree ≤ n−1.
3. Ivanov's characterization (§3, KM p. 12; ref [5]) then forces
   χ(S^λ) = Q^+_λ.

## 2. The filtration structure (task question 1)

The filtration used in §5 is the **PBW / degree-in-y filtration** on Γ_N:
"χ(S^λ) is a supersymmetric polynomial in y of degree not exceeding n" (proof
of Thm 5.2, line 1596). Concretely:

- **On Z(U(q_N)):** the standard Capelli degree = |λ| for S^λ (equivalently,
  the number of tensor factors n in (5.1)).
- **On Γ_N:** the polynomial-degree filtration Γ_N^{≤k} = {P ∈ Γ_N : deg P ≤ k}.
- **HC is filtered:** deg χ(S^λ) ≤ |λ|, with **top-degree component
  = Q_λ(y)** (ordinary Schur Q).

This is a "degree" filtration in y. It is NOT the (1,1,2)-weight w in
Rick's problem — those are different weights on different algebras (see §4
below).

## 3. HC^{-1}(e_2) — the crucial question (task question 2)

**KM do not compute HC^{-1}(e_2) explicitly.** The paper produces only:

- basis `{S^λ}` (immanants, indexed by strict partitions), and
- Nazarov's basis `{C_λ}` (proportional to S^λ, Remark 5.4).

There is **no discussion of the elementary symmetric polynomials e_r**, no
Newton-identity generator basis, and no c_{2r−1} generators. In particular,
if you want HC^{-1}(e_2), you must invert Q^+_λ ↦ y-basis on Γ_N.

Now — **e_2 is NOT a supersymmetric polynomial** in y_1,…,y_N. Recall
supersymmetric means the "cancellation property": setting y_1 = −y_2 = z gives
a value independent of z. For e_2(y) = ∑_{i<j} y_i y_j, setting y_1 = −y_2 = z
gives −z^2 + (∑_{i≥3} y_i)·0 + e_2(y_3,…,y_N), which DOES depend on z.
So `e_2 ∉ Γ_N`, and **HC^{-1}(e_2) does not exist** in the queer HC picture at all.

This is a fatal obstruction to the naïve form of Route γ: the object e_2
whose powers Rick is bounding lives on the polynomial side of the *type-A*
(gl_N) Harish-Chandra picture, not the queer one.

## 4. Where Route γ actually breaks down

The four alignments in the task setup:

1. **(2c+1)-shift matches queer content doubled.** True and remarkable —
   KM's signed contents κ_a(U) = ±√(σ_a(σ_a+1)) satisfy κ_a^2 = σ_a(σ_a+1)
   = c(c+1) at content c. The (2c+1)-shift Rick sees in Day 124's top-symbol
   formula is exactly (c+1)^2 − c^2. This is genuinely a queer-content
   signature, but is compatible with several unrelated combinatorial gadgets.

2. **HC(S^λ) = Q^+_λ.** True (Thm 5.2). But Rick's Ψ maps to `s*_μ`
   (ordinary shifted Schur), not `Q^+_λ`. On Λ*_3 = ℚ[e_1,e_2,e_3] the
   basis {s*_μ : ℓ(μ) ≤ 3} runs over **all** partitions of length ≤ 3, while
   {Q^+_λ : ℓ(λ) ≤ 3} runs only over **strict** partitions. These are
   different bases of different (though related) algebras.

3. **Stirling-triangular Newton identity (Das–Pattanayak arXiv:2608.17431).**
   That identity — {c_{2r−1}} ↔ {D_r} via Stirling matrix — lives in
   Z(U(q_N)). Its image under χ gives a Stirling-triangular relation between
   **odd power sums** p_{2r−1}(y) and factorial versions of them
   (since HC(c_{2r−1}) is essentially the odd power sum on the queer side —
   Sergeev's classical computation). It does NOT give a Stirling identity
   for e_2 in the `{Q^+_λ}` basis, because:
   - The image algebra Γ_N is generated by odd power sums p_1, p_3, p_5, …
     (super-symmetric restriction kills all even power sums up to signs).
   - e_2 = (p_1^2 − p_2)/2, which contains p_2 → not in Γ_N.

4. The "(1,1,2)-weight matches |λ| under identification with Q^+_λ" hope
   assumed the queer picture applied. It doesn't.

## 5. Diagnosis of the mismatch

The classical Okounkov–Olshanski shifted-Schur map, which is Rick's Ψ, is the
Harish-Chandra image on `Z(U(gl_N))` — the **type-A** center. That HC picture
sends:
- Capelli elements → shifted Schur s*_μ (Okounkov 1996);
- basis: ordinary partitions;
- codomain: Λ*_N (shifted symmetric polys), a **flat deformation** of Λ_N
  containing e_1, e_2, e_3 as legitimate elements.

The queer version (KM 2025) is a **different** central algebra with a
**different** HC map. Both have "shifted Schur–like" descriptions of their
images, but the polynomials and indexing sets are distinct (ordinary vs. strict).

The (2c+1) shift Rick sees in Ψ is the *shifted-Schur* content shift
2·(j−i) + 1 = (j−i+1)^2 − (j−i)^2 arising from the falling-factorial [u]_k in
det Ψ(f) = T(f·V)/V. It coincides *numerically* with the queer κ_a^2 pattern
because both are 2c+1 differences, but the structural origin in Rick's Ψ is
the falling-factorial derivative rule — a plain-Vandermonde/Weyl-denominator
identity — which is present already in the type-A story of Okounkov.

## 6. Recommended pivot

Route γ (queer HC) does not close the gap on a straight read. Two options:

**(a) Go back to the correct HC picture.** Rick's Ψ IS the classical
Okounkov–Olshanski HC. Then:
- HC^{-1}(e_2) exists cleanly in Z(U(gl_N)) — it is a linear combination
  of *quadratic Casimirs* (∑ E_ii^2 + 2 ∑_{i<j} E_ij E_ji type element),
  and via Okounkov 1996 Prop. 3 it corresponds to a specific
  linear combination of Capelli elements C_λ with |λ| ≤ 2.
- The (1,1,2)-weight w is a *different* weight on Λ*_3 from the polynomial
  degree — it is `(1,1,2)` on `(e_1,e_2,e_3)`. Under Ψ this corresponds
  to the "shifted-content" weight seen in Day 118 (d_μ = μ_1 + ⌊(μ_2+μ_3)/2⌋),
  which is **not** |μ|. In particular the sought bound
  `w(Ψ(e_2^b)) ≤ b` is stronger than `deg Ψ(e_2^b) ≤ 2b` — polynomial
  degree does NOT give it.

**(b) Look at KM's proof method, not the theorem.** Their proof step (vanishing
on µ with |µ| < n via the differential-operator image) is potentially
transportable: if we can realize e_2^b in Z(U(gl_N)) as an operator that
annihilates polynomials of degree < 2b in a suitable representation, we get
`w`-drop-like statements. But this is speculative and requires a new
differential-operator model for the (1,1,2)-weight.

## 7. Concrete deliverables from this reading

- **HC^{-1}(e_2) in queer:** does not exist (e_2 ∉ Γ_N).
- **Filtration in §5:** polynomial degree in y, matched by S^λ ↔ |λ| via
  top-symbol Q_λ.
- **Das–Pattanayak Stirling transfer:** does NOT give a Stirling identity
  for e_2 in {Q^+_λ}; wrong algebra.
- **Closure of `w(Ψ(e_2^b)) ≤ b`:** NOT achieved via Route γ.

## 8. Missing lemma (if Route γ were to be revived)

The salvage would require:
- (i) an algebra map ι : Λ*_3 → some quotient/subring of Γ_3 sending e_2 → f
  with `f = Q^+_(1,1)(y) + ...` of bounded Q^+-support,
- (ii) *and* an argument that `w(ι^{-1}(Q^+_λ)) = |λ|`, which requires
  computing ι^{-1}(Q^+_λ) as an e-polynomial — the very thing we're trying
  to bound.

That is circular. Route γ, as stated, is a dead end for the immediate gap.

**Recommendation:** Rick should try the Okounkov–Olshanski classical HC
route (Route α?), where HC^{-1}(e_2) genuinely exists as a quadratic Casimir
in Z(U(gl_N)), and look for a *representation-theoretic* interpretation of
the (1,1,2)-weight on the polynomial side. The correct queer analogue of the
(1,1,2)-weight would be the |λ|-degree on Γ_N — but the type-A e_2 is not
supersymmetric, so it doesn't live in Γ_N.
