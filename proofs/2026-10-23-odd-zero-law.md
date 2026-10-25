# The odd values of H_κ are honest K-theory: H(−½) = 2^{−κ₁}, and (OC) (PROVE 251)

> **SUPERSEDED IN PART (2026-10-25 note; text below is the PROVE 251 record, left as written).**
> - **Theorem B = (OC)** is no longer "modulo (G1)–(G4)". PROVE 254 derives it from Theorem HZ (`proofs/2026-10-25-crownF-strict-reciprocity.md` §9) given (G0), (G1), (BR) only, with no Brion–Kumar (G2)–(G4). Registry `q488-oc-thmB-OC`: trust `proved`, conditional_grade "proved given (G0), (G1), (BR first-hand) via Theorem HZ (file Sec.9.6); the original G1-G4 route stays as recorded". (The crownF file states Theorem HZ, not Theorem B by name; the one-line derivation a=(M−1)/2 ≥ m ≥ κ₁ ⇒ 2a ≥ κ₁ and ⌈r(κ′)/2⌉ ≤ m−1 < a is in the registry note_prove254.)
> - **Case B of (Z)** is closed for all κ by Theorem Z, `proofs/2026-10-24-Z-by-hyperplane-induction.md` (registry `q488-oc-Z-by-induction`: trust `proved`, "proved given (G0) Chevalley + (G1) Demazure + (BR) 1005.2605 first-hand"); a second proof is crownF §9.6 via Theorem HZ.
> - §7 gap 4 (integer window) is closed by Theorem I, `proofs/2026-10-24-integer-window-and-OG-twin.md` (registry `q488-oc-Zint-by-induction`: proved given (G0), (G1), (BR)).

Rick, 2026-10-22/23, PROVE 251. Notation and conventions follow `proofs/2026-10-21-window-is-kodaira-vanishing.md` §1:
- C_m has simple roots α_i = ε_i − ε_{i+1} (i<m) and α_m = 2ε_m, and ω := ω_m = ε_1+…+ε_m.
- D_i f = (f − e^{−α_i}s_i f)/(1 − e^{−α_i}).
- κ ⊆ [m] is a strict partition κ₁ > κ₂ > … > κ_ℓ. w_κ ∈ W^P is the minimal coset representative with w_κω = v_κ, the sign
  vector with −1 exactly at the positions p = m+1−k, k ∈ κ, and ℓ(w_κ) = |κ|.
- H_κ(j) := χ(X_κ, O(j)), X_κ ⊂ LG(m,2m).
- y_i := e^{−ε_i}.

Scripts are in `work-in-progress/scripts/prove251/`.

**Nothing below uses the LS parity model.** Everything is about H_κ = χ(X_κ, O(j)) itself, via Demazure operators.

## 0. Verdict

| item | statement | grade |
|---|---|---|
| **Prop. H** (bridge) | For every integer a ≥ 0: 2^m·H_κ(−a−½) = D_{w_κ}(Π_{i=1}^m y_i^a(1+y_i))\|_{y=1}. Geometrically, 2^m H_κ(−a−½) = χ(X_κ, ∧^•U ⊗ O(−a)), U the tautological subbundle. | **proved** given (G1); checked 110/110 against the LS model (m ≤ 4, M ≤ 9) |
| **Thm A** | H_κ(−½) = 2^{−κ₁}. | **proved** given (G1); pure Demazure algebra after Prop. H |
| **Thm B = (OC)** | For odd M ≥ 2m+1: (−1)^{\|κ\|}·2^m·H_κ(−M/2) ∈ ℤ_{≥1}. In particular there is no zero at half-integers j ≤ −m−½. | **proved modulo (G1)–(G4)**, the same citation family as Theorem E (Brion–Kumar, not deep-read). **[SUPERSEDED 2026-10-25: proved given (G0), (G1), (BR) via Theorem HZ, PROVE 254 — see top note.]** The dual-side atom identity was checked independently 110/110, and all atoms were ≥ 0 for a ≥ m. |
| **Thm C** (M = 3) | For κ₁ ≥ 2: H_κ(−3/2) = 2^{−κ₁}·H_{κ′}(−1), κ′ := κ∖{κ₁}; and H_{(1)}(−3/2) = −½. So H_κ(−3/2) = 0 iff ℓ(κ) ≥ 2, and = 2^{−κ₁} for one-row κ with κ₁ ≥ 2. | **proved** given (G1) |
| **Lemma L** (Coxeter localisation) | For any one-variable φ: D_1⋯D_k(Π_jφ(x_j)) = Σ_i A(x_i)Π_{j≠i}B(x_j)/(x_j−x_i), with x = e^{ε}, B = xφ and A = D^{(1)}φ. Consequence: G_k(a) := D_1⋯D_k F_a = e^{−aω} − (−1)^{k−1}F_{a−1}·Σ_{s<a} h_{2s−k+1}(x). | **proved** (§6bis, algebraic induction); formula checked 20/20 (k ≤ 5, a ≤ 4) |
| **Prop. R** (purity) | If 2a ≤ κ₁ then H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a). If 2a−1 = κ₁ then H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a) − H_{κ′}(−a+½). | **proved** given (G1): Lemma Q is the case k = 2a−1 of Lemma L. |
| **Thm R** (residue formula) | For all c ∈ ½ℤ (indeed as a polynomial identity in c): H_κ(−c) = (−1)^{\|κ\|−ℓ} Res_{t₁=1}⋯Res_{t_ℓ=1} Π_{s=1}^{ℓ} t_s(1−ρ_s(t_s))/((t_s²−1)(t_s−1)^{κ_s}), where ρ_s(t) = t^{2c−1−s}Π_{r<s}(t_r−t)/(t_rt−1) and the residues are taken innermost (t_ℓ) first. Under t = (1+z)/(1−z) the coupling becomes the Schur-Q kernel (z_r−z_s)/(z_r+z_s). | **proved** given (G1) (§6ter: Lemma L applied block by block + nested contours); checked 70/70 (10 κ, c ∈ {½,…,7/2}) |
| **(Z)** | the full vanishing range: H_κ(−M/2) = 0 for odd M ∈ [3, 2⌈r′/2⌉+1] | **computed** in general (63/63 m ≤ 6; per-k form m ≤ 5). **Proved given (G1)** for M = 3 (Thm C), for all κ with **ℓ(κ) ≤ 2**, and for all **2-separated** κ (κ_i ≥ κ_{i+1}+2) (Thm Z₂ and Cor. Z, §6quater). Open for Case-B (staircase-like) shapes: the residue at t₁ = ∞ (§6quater), or equivalently the per-k vanishing **(Z_k)**. **UPDATE PROVE 252:** Case B is closed for all κ by hyperplane-section induction, given (G1) + the Buch–Ravikumar K-Pieri *support* (abstract-level citation); see `proofs/2026-10-24-Z-by-hyperplane-induction.md`. |

**Headline.** At half-integers the type-C operator D_m splits as a type-B operator times (1+e^{−ε_m})^{−1}. Conjugating by
Φ = Π_i(1+y_i)^{−1} turns the whole chain back into honest type-C Demazure operators applied to an *integral* weight
character. So **2^m·H_κ(−a−½) is the Euler characteristic of an honest vector bundle**, χ(X_κ, ∧^•U(−a)).

The day-249 §5 sentence "there is no sheaf on X_κ whose Euler characteristic is P(c)" was wrong: you have to take ∧^•U, not
a line bundle. After that, (OC) is Serre duality plus Frobenius-splitting vanishing, and H(−½) is a three-line Demazure
computation.

## 1. Lemma P (polynomial extension)

Work with analytic germs at h = 0 on 𝔥 = ℂ^m, with e^μ(h) := e^{⟨μ,h⟩} for every μ ∈ ℂ^m. Each D_i maps germs to germs: the
numerator vanishes on the hyperplane α_i(h) = 0, and 1 − e^{−α_i} = α_i·(unit).

**Lemma P.** P_w(λ) := [D_w e^λ](0) is a polynomial in λ ∈ ℂ^m of degree ≤ ℓ(w). For κ, H_κ(j) = P_{w_κ}(jω) for every j ∈ ℂ.

*Proof.* Let 𝔪 be the maximal ideal of germs at 0. For f ∈ 𝔪^k with k ≥ 1:
- D_i f = (f − s_if)/(1 − e^{−α_i}) + s_if;
- f − s_if ∈ 𝔪^k vanishes on α_i = 0, so (f − s_if)/α_i ∈ 𝔪^{k−1}.

Hence D_i(𝔪^k) ⊆ 𝔪^{k−1}, and D_w(𝔪^{L+1}) ⊆ 𝔪 for L = ℓ(w). Write e^λ = Σ_{k≤L}⟨λ,h⟩^k/k! + R with R ∈ 𝔪^{L+1}. Then
[D_w e^λ](0) = Σ_{k≤L}[D_w⟨λ,h⟩^k](0)/k!. Each term is polynomial in λ, since D_w is ℂ-linear and ⟨λ,h⟩^k is polynomial in λ.

For integral λ, D_we^λ is a Laurent polynomial and its value at h = 0 is the coefficient sum. By (G1), H_κ(j) = P_{w_κ}(jω)
for integers j ≥ 0. Both sides are polynomials in j. ∎

## 2. Lemma W (the reduced word)

For 1 ≤ k ≤ m put c(k) := s_{m−k+1}s_{m−k+2}⋯s_m (length k). Note D_{c(k)} = D_{m−k+1}∘⋯∘D_m, so D_m acts first.

**Lemma W.** w_κ = c(κ_ℓ)⋯c(κ₂)c(κ₁), and this word is reduced. Equivalently w_κ = w_{κ′}·c(κ₁) with lengths adding, and
w_{κ′} ∈ ⟨s_j : j ≥ m−κ₁+2⟩.

*Proof.* Let p = m−κ₁+1. Apply the letters of c(κ₁) right to left:
- s_m flips coordinate m;
- s_{m−1}, …, s_p carry the −1 to position p.

So c(κ₁)ω = v_{(κ₁)}. Let u_{κ′} := c(κ_ℓ)⋯c(κ₂). Every letter of u_{κ′} is s_j with j ≥ m−κ₂+1 ≥ p+1, because κ₂ ≤ κ₁−1. So
u_{κ′} only moves coordinates ≥ p+1, where v_{(κ₁)} is all +1. By induction on ℓ(κ), u_{κ′}c(κ₁)ω = v_κ.

The word has length |κ| = ℓ(w_κ). It lies in the coset w_κW_P, because Stab_W(ω) = S_m = W_P. The minimal coset
representative is the unique element of minimal length in its coset. So the word is reduced and equals w_κ. ∎

(Computer check: the BFS words of `prove249d/dem.py:word` are exactly these, m ≤ 4.)

## 3. Lemma C (the conjugation) and Prop. H

Put D^B_m g := (g − y_m s_mg)/(1 − y_m), the type-B operator for the short root ε_m. Put D′_i := D_i for i < m and
D′_m := (1+y_m)^{−1}D^B_m. Put Φ := Π_{i=1}^m (1+y_i)^{−1}, an analytic germ with Φ(0) = 2^{−m}.

**Lemma C.**
- (i) D_i(e^{−ω/2}g) = e^{−ω/2}D′_i(g) for all i.
- (ii) D′_i(Φg) = Φ·D_i(g) for all i.
- Hence D_w(e^{−ω/2}g) = e^{−ω/2}·Φ·D_w(Φ^{−1}g) for every w.

*Proof.*
- **i < m.** e^{−ω/2} and Φ are S_m-invariant, and D_i(φg) = φD_ig whenever s_iφ = φ.
- **(i), i = m.** s_m(e^{−ω/2}) = e^{−ω/2}e^{ε_m} and e^{−α_m} = y_m². So
  D_m(e^{−ω/2}g) = e^{−ω/2}(g − y_m s_mg)/(1 − y_m²) = e^{−ω/2}(1+y_m)^{−1}D^B_m g.
- **(ii), i = m.** Write Φ = Φ′(1+y_m)^{−1} with Φ′ s_m-invariant, and use s_m(1+y_m)^{−1} = y_m(1+y_m)^{−1}. Then
  D^B_m((1+y_m)^{−1}g) = (g − y_m²s_mg)/((1+y_m)(1−y_m)). Multiplying by (1+y_m)^{−1}Φ′ gives Φ·(g − y_m²s_mg)/(1 − y_m²)
  = Φ·D_m g. ∎

**Prop. H.** For every a ∈ ℤ_{≥0}, 2^m H_κ(−a−½) = [D_{w_κ}(F_a)](1), where F_a := Π_i y_i^a(1+y_i) = e^{−aω}Φ^{−1}.

*Proof.* By Lemma P, H_κ(−a−½) = [D_{w_κ}(e^{−ω/2}·e^{−aω})](0). By Lemma C this is [e^{−ω/2}ΦD_{w_κ}(F_a)](0), and
e^{−ω/2}Φ = 2^{−m} at 0. ∎

*Geometric reading.* F_a is the character of the P-module C_{−aω} ⊗ ∧^•(U₀), where U₀ is the Levi-module with weights −ε_i.
That is the fibre of U, since det U = O(−1) ↔ e^{−ω}. F_a is S_m-symmetric, so D_{w_κ}F_a = D_{w_κ w_{0,P}}F_a. Pulling back to
Y = π^{−1}X_κ ⊂ G/B and filtering by B-weights, (G1) gives

  **2^m·H_κ(−a−½) = χ(X_κ, ∧^•U ⊗ O(−a)).**

(Sanity check, m = 1, X = ℙ¹, U = O(−1): χ(O ⊕ O(−1)) = 1 = 2·H(−½) = 2·½.)

Check (`dem_half.py`): Prop. H against the LS-model polynomial at M = 1,3,5,7,9, all κ, m = 3 (35/35) and m = 4 (75/75).

## 4. Theorem A: H_κ(−½) = 2^{−κ₁}

*Proof.* By Prop. H with a = 0, 2^mH_κ(−½) = [D_{w_κ}Π_i(1+y_i)](1). Let p = m−κ₁+1.

1. **Claim.** D_{c(κ₁)}Π_{i=1}^m(1+y_i) = Π_{i<p}(1+y_i). Apply D_m, D_{m−1}, …, D_p in turn. Before D_q acts, the function is
   Π_{i≤q}(1+y_i) (true for q = m), and Π_{i<q}(1+y_i) is s_q-invariant. So
   D_q(Π_{i≤q}(1+y_i)) = Π_{i<q}(1+y_i)·(1 + D_q e^{−ε_q}).
   Here ⟨−ε_q, α_q^∨⟩ = −1, both for q < m (α_q^∨ = ε_q − ε_{q+1}) and for q = m (α_m^∨ = ε_m). So D_qe^{−ε_q} = 0.
2. By Lemma W, the remaining letters s_j all have j ≥ p+1. They fix Π_{i<p}(1+y_i), and D_j(1) = 1.
3. So D_{w_κ}Π(1+y_i) = Π_{i<p}(1+y_i), whose value at 1 is 2^{p−1} = 2^{m−κ₁}. Hence H_κ(−½) = 2^{−κ₁}. ∎

Geometric reading: χ(X_κ, ∧^kU) = binom(m−κ₁, k) (computed, m ≤ 5, `perk.py`). When κ₁ = m, the Koszul-type sum collapses to
χ(O_X) = 1.

## 5. Theorem B: (OC)

Cited facts (as in Theorem E, `2026-10-21-window-is-kodaira-vanishing.md` §3; Brion–Kumar ch. 3, Kumar ch. 8; **not deep-read**):
- **(G1)** Demazure character formula for line bundles on Schubert varieties Y ⊂ G/B.
- **(G2)** Schubert varieties are normal and Cohen–Macaulay, with rational singularities.
- **(G3)** For L ample on a Schubert variety Y ⊂ G/B, H^j(Y, L^{−1}) = 0 for j < dim Y.
- **(G4)** ω_Y = O_Y(−∂Y) ⊗ L_{−ρ}.

**Theorem B.** Let M = 2a+1 with a ≥ m. Then
  (−1)^{|κ|}·2^m·H_κ(−M/2) = Σ_{S⊆[m]} h⁰(Y, O_Y(−∂Y) ⊗ L_{λ_S}) ≥ 1,  λ_S := (a−i+[i∈S])_{i=1..m}.
In particular H_κ has no zero at any half-integer j ≤ −m−½. This is (OC), and the sign is (−1)^{|κ|}.

*Proof.* Let X = X_κ, d = |κ|, π: Y → X the P/B-bundle, and 𝒱 := ∧^•U ⊗ O(−a).
1. **Bridge.** By Prop. H, 2^mH_κ(−M/2) = χ(X, 𝒱).
2. **Serre duality** on the CM variety X (G2): χ(X,𝒱) = (−1)^dχ(X, ω_X ⊗ 𝒱^∨), with 𝒱^∨ = ∧^•U^∨ ⊗ O(a).
3. **Pull back.** As in Theorem E step 2 (from (G4) and ω_{Y/X} = L_{−2ρ} ⊗ π^*O(m+1)),
   π^*ω_X = O_Y(−∂Y) ⊗ L_{ρ−(m+1)ω}. π^*𝒱^∨ is G×^B of a B-module with weights aω + ε_S, S ⊆ [m]. A B-stable flag (Lie–Kolchin)
   filters π^*(ω_X ⊗ 𝒱^∨) with subquotients O_Y(−∂Y) ⊗ L_{λ_S}, where λ_S = ρ + (a−m−1)ω + ε_S = (a−i+s_i)_i.
4. **Dominance.** For a ≥ m, every λ_S is C_m-dominant:
   - λ_i − λ_{i+1} = 1 + s_i − s_{i+1} ≥ 0;
   - λ_m = a − m + s_m ≥ 0.
5. **Vanishing.** For λ dominant, λ+ρ is regular dominant, so L_{λ+ρ}|_Y is ample. Then
   O_Y(−∂Y) ⊗ L_λ = ω_Y ⊗ L_{λ+ρ} (G4), and Serre duality on Y (G2) with (G3) gives H^i(Y, ω_Y ⊗ L_{λ+ρ}) ≅ H^{N−i}(Y, L_{λ+ρ}^{−1})^* = 0
   for i > 0. By the long exact sequences of the filtration:
   - H^i(Y, π^*(ω_X⊗𝒱^∨)) = 0 for i > 0;
   - h⁰ is additive over the subquotients.
   Since Rπ_*O_Y = O_X (fibres P/B), Leray and the projection formula give H^i(X, ω_X⊗𝒱^∨) = H^i(Y, π^*(…)).
   So χ(X, ω_X⊗𝒱^∨) = Σ_S h⁰(Y, O_Y(−∂Y)⊗L_{λ_S}).
6. **A nonzero term.** Take S = [m], so λ = ρ + (a−m)ω. By Theorem E step 2, H⁰(Y, O_Y(−∂Y)⊗L_ρ) ∋ p_v ≠ 0. Multiply by a
   section of L_{(a−m)ω} = π^*O(a−m) that is generically nonzero on the integral Y (O(1) is globally generated). The product is
   nonzero because O_Y(−∂Y)⊗L_ρ is torsion-free. So the S = [m] term is ≥ 1. ∎

*Checks.*
- `atoms.py` re-derives the dual-side identity (−1)^{|κ|}2^mH_κ(−a−½) = Σ_S D̄_{w_max}(e^{λ_S})|₁ (D̄_i = D_i − 1, the atom
  operators) for a = m−2, …, m+2: m = 3, 35/35 and m = 4, 75/75. This independently checks the sign and the weights of
  steps 2–3.
- For a ≥ m every atom is ≥ 0 and the S = [m] atom is ≥ 1 (assertions pass).
- Negative control: at a = m−2 a negative atom does appear (κ = (3), a = 1). So the dominance in step 4 is doing the work.

*Remark (sharper sign range, computed only).* Data suggest every atom is already ≥ 0 for a ≥ m−1, and that the sign
(−1)^{|κ|} holds for all odd M ≥ r(κ)+2. The theorem as proved needs only a ≥ m.

## 6. M = 3, purity, and what is left of (Z)

**Theorem C.** If κ₁ ≥ 2 then H_κ(−3/2) = 2^{−κ₁}H_{κ′}(−1); and H_{(1)}(−3/2) = −½. Moreover H_ν(−1) = 0 for every nonempty ν (H_∅ ≡ 1). Hence H_κ(−3/2) = 0 iff
ℓ(κ) ≥ 2, which is the M = 3 case of the odd-zero law (3 ≤ 2⌈r′/2⌉+1 ⇔ r′ ≥ 1 ⇔ κ′ ≠ ∅).

*Proof.* Take a = 1 and f(y) = y + y². Let p = m−κ₁+1.
1. D_m f(y_m): ⟨−ε_m, α_m^∨⟩ = −1 gives 0, and ⟨−2ε_m, α_m^∨⟩ = −2 gives −e^{0}. So D_mf(y_m) = −1.
2. D_{m−1}(−f(y_{m−1})): the e^{−ε_{m−1}} term is killed (pairing −1). The e^{−2ε_{m−1}} term has pairing −2 and gives
   −e^{−ε_{m−1}−ε_m}. So D_{m−1}(−f(y_{m−1})) = y_{m−1}y_m.
3. For q < m−1, D_q(f(y_q)y_{q+1}): the term y_qy_{q+1} has pairing 0 and is fixed; the term y_q²y_{q+1} has pairing −1 and
   is killed. The untouched factors are s_q-invariant.
4. Hence D_{c(κ₁)}F₁ = Π_{i<p}f(y_i)·y_p·(y_{p+1}⋯y_m). (If κ₁ = 1, D_mF₁ = −Π_{i<m}f(y_i).)
5. Now apply D_{w_{κ′}}, which acts on coordinates p+1..m (Lemma W). The prefactor is inert, and y_{p+1}⋯y_m = e^{−ω″} for the
   rank-(κ₁−1) block. At y = 1: 2^mH_κ(−3/2) = 2^{p−1}·[D_{w_{κ′}}e^{−ω″}](1) = 2^{m−κ₁}H_{κ′}(−1).
   This uses that H_{κ′} is rank-independent, by the same inert-factor argument.
6. For the edge case κ₁ = 1 (κ = (1)): directly, H_{(1)}(−3/2) = −½ ≠ 0, matching ℓ(κ) = 1.
7. **Vanishing of H_ν(−1).** For ν ≠ ∅ the reduced word of w_ν ends (rightmost) with s_m, and
   D_m e^{−ω} = 0 because ⟨−ω, α_m^∨⟩ = −1. ∎

**Purity.** Let G_k(a) := D_1D_2⋯D_k(F_a) in rank k, which is the C_k-block factor of D_{c(κ₁)}F_a when k = κ₁.
- **Propagation (proved).** If the input to D_q is f_a(y_q)·Π_{i>q}y_i^a, the output is Π_{i≥q}y_i^a. The term y_q^ay_{q+1}^a
  has pairing 0; the term y_q^{a+1}y_{q+1}^a has pairing −1.
- **Lemma Q (now proved; see §6bis).** G_{2a−1}(a) = e^{−aω} − F_{a−1} in rank 2a−1. (First found by computation for a ≤ 4, `pure2.py`.)
- **Q ⇒ G_{2a}(a) = e^{−aω} (proved).** In rank 2a, after the last 2a−1 operators the function is
  f_a(y_1)(e^{−aω′} − F′_{a−1}). Here f_a(y_1)F′_{a−1} = y_1·F_{a−1}, with F_{a−1} fully symmetric, so
  D_1(y_1F_{a−1}) = F_{a−1}D_1(e^{−ε_1}) = 0. Propagation then gives G_k(a) = e^{−aω} for all k ≥ 2a.
- **Prop. R.**
  - For κ₁ ≥ 2a: H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a).
  - For κ₁ = 2a−1: H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a) − H_{κ′}(−a+½). The F′_{a−1} term gives 2·2^{κ₁−1}H_{κ′}(−(a−1)−½) by
    Prop. H for κ′.
  - Both are now unconditional (given (G1)): Lemma Q is proved in §6bis.
- Bott check of Lemma Q, non-equivariant. X_{(k)} is the projective cone over v₂(ℙ^{k−1}) (its Hilbert function is
  Σ_h binom(2h+k−1,k−1)). It is resolved by a ℙ¹-bundle over ℙ^{k−1}, on which U ⊃ H ≅ Ω¹(1). Bott's formula gives
  χ = 1 − 2^k at k = 2a−1, as Lemma Q predicts. The equivariant version is not written.
- Prop. R is not in the span beyond κ₁ ≥ 2a−1: G_k(a) ∉ span{F_b, e^{−bω}} for 2 ≤ k ≤ 2a−2 (`span.py`).

**What (Z) needs, exactly.** Combine Prop. H, the vanishing of every S with a "01" pattern, and the identification of the
S = ∅, [m] terms with integer values. This gives
  2^mH_κ(−a−½) = H_κ(−a) + H_κ(−a−1) + Σ_{t=1}^{m−1} χ(X_κ, ∧^tU(−a)),
and the integer terms vanish inside the integer window (a+1 ≤ ⌊(r+1)/2⌋, which follows from a ≤ ⌈r′/2⌉ since r ≥ r′+2).

(The t = 0 and t = m terms are χ(O(−a)) and χ(∧^mU(−a)) = χ(O(−a−1)), since ∧^mU = O(−1).)

So, given the integer window, (Z) ⇐ **(Z_k)**: χ(X_κ, ∧^tU(−a)) = 0 for 1 ≤ t ≤ m−1, κ₁ = m, 1 ≤ a ≤ ⌈r′/2⌉. Computed, m ≤ 5 (`zr.py`). There:
- each t has its own vanishing range, always ≥ ⌈r′/2⌉;
- the minimum over t is exactly ⌈r′/2⌉, which is why the odd-zero law is sharp.

Proved instances:
- a = 1 (Thm C);
- a ≤ κ₁/2 given Lemma Q and the integer window of κ′. The integer window of κ′ is itself "proved mod the LS model" (Ehrhart
  reciprocity), or would follow geometrically from h⁰(X_{κ′}, ω(b)) = 0 for b ≤ ⌊(r′+1)/2⌋, which is not proved here.

(NZ) for ⌈r′/2⌉ < a < m (the middle range) is computed only; Theorem B covers a ≥ m.

## 6bis. Lemma L (Coxeter localisation) and the proof of Lemma Q

Work in rank k, with D_k the long-root operator and x_j := e^{ε_j} = 1/y_j. In x-variables:
- D_i g = (x_ig − x_{i+1}s_ig)/(x_i − x_{i+1}) for i < k;
- D^{(1)}φ(x) := (x²φ(x) − φ(1/x))/(x² − 1) is the long-root operator on one variable.

**Lemma L.** Let φ be a one-variable Laurent polynomial (or rational function, or formal family). Put B(x) := xφ(x) and
A := D^{(1)}φ. Then
  D_1D_2⋯D_k(Π_{j=1}^kφ(x_j)) = Σ_{i=1}^k A(x_i)·Π_{j≠i}B(x_j)/Π_{j≠i}(x_j − x_i).

*Proof.* Induction on k; k = 1 is the definition of A.
1. **Set-up.** By induction applied to variables 2..k (they form a rank-(k−1) system with the same long root),
   D_2⋯D_k(Π_jφ(x_j)) = φ(x_1)·Σ_{i≥2}A(x_i)Π_{j≠i, j≥2}B(x_j)/Π_{j≠i, j≥2}(x_j − x_i).
   Since φ(x_1) = B(x_1)/x_1, this is (1/x_1)Σ_{i≥2}R_i, with R_i := A(x_i)Π_{j≠i}B(x_j)/Π_{j≠i, j≥2}(x_j − x_i).
   So D_1 of it is (Σ_{i≥2}R_i − Σ_{i≥2}s_1R_i)/(x_1 − x_2).
2. **i ≥ 3.** R_i and s_1R_i differ only in the factor 1/(x_2 − x_i) versus 1/(x_1 − x_i). Their difference divided by
   (x_1 − x_2) is A(x_i)Π_{j≠i}B(x_j)/Π_{j≠i}(x_j − x_i).
3. **i = 2.** R_2/(x_1 − x_2) + s_1R_2/(x_2 − x_1) is exactly the sum of the i = 2 and i = 1 terms of the claim. ∎

**Divided differences.** Write Δ_k[g] := Σ_ig(x_i)/Π_{j≠i}(x_j − x_i) = (−1)^{k−1}g[x_1,…,x_k]. Then:
- Δ_k[t^n] = (−1)^{k−1}h_{n−k+1}(x), with h_{<0} = 0;
- Δ_k[1/(1+t)] = 1/Π_j(1+x_j).

**Proof of Lemma Q and the formula for G_k(a).** Take φ = f_a = x^{−a−1}(1+x). Then:
- B = x^{−a}(1+x);
- A = D^{(1)}f_a = −(x^{1−a} + … + x^{a−1}) (rank-one string);
- A/B = −P_a(x)/(1+x) with P_a(t) = t + … + t^{2a−1}, and P_a(t)/(1+t) = (1 + t² + … + t^{2a−2}) − 1/(1+t).

Lemma L gives G_k(a) = Π_jB(x_j)·Δ_k[A/B]. Also Π_jB(x_j) = e^{−aω}Π_j(1+x_j) = F_{a−1}. Hence
  **G_k(a) = e^{−aω} − (−1)^{k−1}F_{a−1}·Σ_{s=0}^{a−1}h_{2s−k+1}(x).**
- For k ≥ 2a all h vanish (purity).
- For k = 2a−1 only s = a−1 survives, with h_0 = 1 (Lemma Q). ∎

The same computation with φ = x^{−b} gives the single-row integer window: D_c(e^{−bω}) = 0 for 1 ≤ b ≤ (k+1)/2.

## 6ter. Theorem R (iterated residue formula)

Apply Lemma L stage by stage along w_κ = c(κ_ℓ)⋯c(κ₁), so the first stage is block 1 = the last κ₁ coordinates.
1. **Contour form.** Write Lemma L as R = (−1)^{k−1}∮_{|t−1|=ε}(dt/2πi)·(A/B)(t)·Π_j B(x_j)/(t − x_j). This is valid when every
   x_j lies inside the circle and A/B is holomorphic on the closed disc. At t = 1 the singularity is removable, because
   B(1/t)/B(t) → 1.
2. **Stages.** Stage s uses the product function φ^{(s−1)}, where φ^{(0)} = φ₀ and φ^{(s)}(x) = B^{(s−1)}(x)/(t_s − x).
   Coordinates of block s that are not in block s+1 are inert from then on and are set to 1. Exchanging D with the contour
   integral is legitimate: the integrand is jointly analytic and the D's preserve analyticity.
3. **Nesting.** Nested radii ε_1 > ε_2 > ⋯ > ε_ℓ keep each pole t = 1/t_r outside the later circles.
4. **Bookkeeping.** With ρ_s := B^{(s−1)}(1/t)/B^{(s−1)}(t) and ρ₀ = t^{2c−2}:
   - φ₀ = x^{−b} (c = b) gives ρ₀ = t^{2b−2};
   - φ₀ = f_a (c = a+½, via Prop. H) gives ρ₀ = t^{2a−1};
   - in both cases ρ_s(t) = t^{2c−1−s}Π_{r<s}(t_r − t)/(t_rt − 1).
   The constant prefactors are φ₀(1)^{m−κ₁}B₀(1)^{κ₁}, which equals 1 or 2^m and cancels the 2^m of Prop. H.
   The inert evaluations give Π_r(t_r−1)^{−κ_r}.

Hence
  **H_κ(−c) = (−1)^{|κ|−ℓ}·Res_{t₁=1}⋯Res_{t_ℓ=1}Π_{s=1}^ℓ t_s(1 − ρ_s(t_s))/((t_s²−1)(t_s−1)^{κ_s}).**

With t = (1+z)/(1−z), the measure t dt/((t²−1)(t−1)^κ) becomes (1+z)(1−z)^{κ−1}dz/(2^{κ+1}z^{κ+1}), and
(t_r−t)/(t_rt−1) becomes (z_r−z)/(z_r+z), the Schur-Q kernel.

Check (`resid.py`): 70/70 against the LS-model polynomial (κ ∈ {(1),(2),(3),(1,2),(1,3),(2,3),(1,2,3),(2,4),(1,2,4),(3,4)},
c ∈ {½,1,…,7/2}).

**Why this matters for (Z).** In Thm R the variables t₂…t_ℓ see κ′ at c′ = c − ½, deformed by the kernel K(t₁,·) = (t₁−·)/(t₁·−1).
So the half-integer window of κ is the *integer* window of κ′ under deformation, and vice versa. That is exactly the
numerology ⌈r′/2⌉ = ⌊(r(κ′)+1)/2⌋. Two cautions:
- At t₁ = 1 the kernel equals −1, not 1. The undeformed object is the Koszul-signed variant (1+ρ′), which is the
  λ_{−1}(U)-twist: the sub-LG {Λ ∋ v}.
- The naive "deformation-robust window" is false: χ(X_κ, Sym^nQ(−b)) leaves the window as n grows (`symq.py`). A proof of
  (Z) needs the graded version: vanishing to order κ₁ in t₁ − 1.

## 6quater. Moving the outer residue: the recursion, and (Z) for 2-separated κ

Write 𝓗_κ(c;T) for the residue expression of Thm R without the sign (−1)^{|κ|−ℓ}, with extra kernels Π_{τ∈T}K(τ,t_s) put into
every ρ_s, where K(τ,t) := (τ−t)/(τt−1). So H_κ(−c) = (−1)^{|κ|−ℓ}𝓗_κ(c;∅). Thm R is recursive:
  𝓗_κ(c;T) = Res_{t₁=1} m_{κ₁}(t₁)(1 − t₁^{2c−2}Π_{τ∈T}K(τ,t₁))·𝓗_{κ′}(c−½; T∪{t₁}),  m_κ(t) = t/((t²−1)(t−1)^κ).

**Poles in t₁.** After the inner residues, 𝓗_{κ′}(c′; T∪{t₁}) is rational in t₁. Its only pole is t₁ = 1 (from K(t₁,t_s) at
t_s = 1), and it stays bounded as t₁ → ∞, where K(t₁,t) → 1/t. So the t₁-integrand has poles only at:
- t₁ = 1;
- t₁ = −1 (from m);
- t₁ = 1/τ for τ ∈ T (from K(τ,t₁));
- t₁ = 0 (only if c ≤ 0);
- t₁ = ∞ (only if 2c ≥ κ₁+2).

**The three useful identities.**
- K(−1,t) = 1;
- K(τ,−1) = −1;
- K(τ,t)K(1/τ,t) = 1.

**Prop. M (outer residue moved; proved given Thm R).** Let c ∈ ½ℤ with 1 ≤ c and 2c ≤ κ₁+1. Then
  𝓗_κ(c;T) = −r_{κ₁}(1 − (−1)^{2c+|T|})𝓗_{κ′}(c−½;T) − (−1)^{κ₁}Σ_{τ∈T}τ^{κ₁+1−2c}(τ−1)^{−κ₁}Π_{τ′≠τ}K(τ′,1/τ)·𝓗_{κ′}(c−½;T∖{τ}),
where r_κ = Res_{t=−1}m_κ = (−1)^κ2^{−κ−1}. In particular, for T = ∅:
- **c = b an integer:** H_κ(−b) = 0 for 1 ≤ b ≤ (κ₁+1)/2. This is the integer window from the first row, now LS-model-free.
- **c = a+½:** H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a) for 2a ≤ κ₁. This is Prop. R again, in two lines.

*Proof.* Apply the residue theorem on ℙ¹ in t₁: the residue at 1 is minus the sum of the residues at −1, at the 1/τ, and at
0 and ∞. The last two are absent in this range. At −1 the kernels evaluate by the identities above. At 1/τ, K(τ,t₁) has
residue 1 − τ^{−2}, and the pair K(τ,·)K(1/τ,·) cancels inside 𝓗_{κ′}. ∎

**Theorem Z₂ (odd-zero law for 2-separated κ; proved given (G1)).** Suppose κ_i ≥ κ_{i+1}+2 for all i. Then
r(κ_{≥i}) = κ_i and r′ = κ₂. For odd M = 2a+1 ≥ 3: H_κ(−M/2) = 0 ⟺ a ≤ ⌈κ₂/2⌉. The "⇒" direction (no zeros beyond) is proved
in the range 2a ≤ κ₁; above it, see the remark below.

*Proof of the zeros.*
1. Let 1 ≤ a ≤ ⌈κ₂/2⌉. Then 2a ≤ κ₂+1 ≤ κ₁−1, so Prop. M gives H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a).
2. Apply Prop. M to κ′ (first row κ₂) with c = a: since 2a ≤ κ₂+1, H_{κ′}(−a) = 0. ∎

*The "⇐" direction in range.* For ⌈κ₂/2⌉ < a and 2a ≤ κ₁, H_κ(−a−½) = 2^{−κ₁}H_{κ′}(−a), so we need H_{κ′}(−a) ≠ 0 for a beyond
κ′'s integer window. That is Theorem E territory (proved there only for a ≥ m(κ′)+1).


**Corollary Z (two rows, and a general sufficient condition; proved given (G1)).**
1. **ℓ(κ) ≤ 2: the zeros of the odd-zero law hold.** For κ = (k₁,k₂) and 1 ≤ a ≤ ⌈k₂/2⌉ we have 2a ≤ k₂+1 ≤ k₁. Prop. M gives
   H_κ(−a−½) = 2^{−k₁}H_{(k₂)}(−a), and Prop. M again (for the row (k₂), c = a, 2a ≤ k₂+1) gives 0.
2. **Non-vanishing for ℓ(κ) ≤ 2, in range.** If ⌈k₂/2⌉ < a and 2a ≤ k₁, then H_κ(−a−½) = 2^{−k₁}H_{(k₂)}(−a) ≠ 0. Proof: for a
   single row, Prop. M's ingredients give the closed form
     H_{(k)}(−b) = 2^{−k−1}(1 + (−1)^kP), P = [z^k](1+z)^{2b−1}(1−z)^{k+1−2b}.
   For 2b ≥ k+2 every term of P is positive and P ≥ binom(2b−1,k) ≥ 3, so H ≠ 0 with sign (−1)^k.
3. **General sufficient condition.** The zeros of (Z) hold for κ whenever r(κ″) ≤ κ₂−1 and 2⌈r(κ′)/2⌉ ≤ κ₁, where
   κ″ = κ minus its two largest parts. The same two applications of Prop. M work. This covers all 2-separated κ, all κ with
   ℓ ≤ 2, and more.

**A false shortcut (recorded so nobody repeats it).** The non-selected rows of Thm R decouple exactly: moving t_r's residue to
−1 kills its kernels, and this was checked term by term, 8/8 S-terms. But H is **not** a single Schur extraction
[z^κ]Π_s(ε_sz^{κ_s} − f_s)Π K for ℓ ≥ 3: a "decoupled" middle variable can carry cancelling kernel shifts. The correct
statement is the subset sum Ĥ = Σ_S(−1)^{|S|}Π_{r∉S}ε_r·Ĵ_S, with each Ĵ_S a Schur-type extraction over S (hence a
Pfaffian). Scripts: `decouple.py`, `dectest.py`, `pf.py`, `dbg*.py`.

**Remarks.**
- For κ₁ ≥ r′+2 ("Case A") the same argument reduces (Z) for κ to the integer window of κ′. For 2-separated κ the
  reduction closes by induction.
- **[2026-10-25: Case B CLOSED by Theorem Z, `2026-10-24-Z-by-hyperplane-induction.md`; see top note.]**
- When some κ_i ≤ r(κ_{>i})+1 ("Case B", e.g. the staircase), the needed c reach 2c ≥ κ₁+2. Then the residue at t₁ = ∞
  contributes: −Res_{s=0}s^{κ₁+1−2c}(…)·𝓗_{κ′}(c−½; T∪{1/s}). Controlling it is the open part of (Z).
- **Erosion (computed, `robust.py`).** With |T| = q generic kernels, the zero set of c ↦ 𝓗_κ(c;T) consists of the c whose
  whole ½ℤ-neighbourhood of radius q/2 lies in the q = 0 zero set. Example: (1,2) has zeros {1, 3/2, 2} at q = 0, {3/2} at
  q = 1, and none at q = 2. The q = 1 case at half-integers is exactly the per-t statement (Z_k), because
  Σ_t u^tχ(∧^tU(−a)) is 𝓗 with the single kernel τ = −1/u.

## 7. Gaps (precise)

1. (G1)–(G4) are cited, not deep-read. This is the same debt as Theorem E (registry node q488-theorem-E-even-c-empty, graded
   computed for exactly this reason). Thm A and Thm C need **only (G1)**; Thm B needs all four. **[SUPERSEDED 2026-10-25: Thm B
   now needs only (G0), (G1), (BR) via Theorem HZ (PROVE 254, crownF §9); registry `q488-oc-thmB-OC` proved.]**
2. ~~Lemma Q computed only~~: **closed**, Lemma L proves it for all a (§6bis).
3. (Z) is **proved for 2-separated κ** (Thm Z₂, §6quater), and for every κ with a ≤ ⌊κ₁/2⌋ given κ′'s integer window.
   It remains open for Case-B shapes (staircase-like), where the residue at t₁ = ∞ must be controlled. Exact
   reformulations: (Z_k), or the erosion statement for 𝓗_κ(c;T). **[CLOSED 2026-10-24/25: Theorem Z,
   `2026-10-24-Z-by-hyperplane-induction.md`, registry `q488-oc-Z-by-induction` proved given (G0), (G1), (BR).]**
4. The integer window H_ν(−b) = 0 for 1 ≤ b ≤ ⌊(r(ν)+1)/2⌋ is not proved here geometrically. It is used only in Prop. R's
   application to (Z). **[CLOSED: Theorem I, `2026-10-24-integer-window-and-OG-twin.md`, registry `q488-oc-Zint-by-induction` proved.]**

## 8. Lesson

The obstruction "no line bundle has these Euler characteristics" was true and irrelevant. The right question was "which
**vector** bundle". The type-B/C mismatch at the long root is a factor (1+e^{−ε}), and the product of those factors over all i
is a character, ∧^•U. **When half-integral twists look non-geometric, try conjugating the defect factor into a W-symmetric
product and read the product as a bundle.**
