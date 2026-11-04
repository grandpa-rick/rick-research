# PROVE 276 — Q65/Q66: K_0 of type-A quasi-crystals is QSym, and quasification is monoidal

Date: 2026-11-04 (session for the 11-05 slot). Scripts: `proofs/prove276/` (`q66.py`, `test_iv.py`, `test_i_ii.py`, `test_sym_levi.py`).
Builds on PROVE 275 (`proofs/2026-11-04-q62-quasi-crystal-tensor-rule.md`): Theorem A (quasi-tensor rule), Theorem B (components
C_σ ≅ P_D(n), character F_D), Prop P (product), Theorem C (Levi slices).

**Verdict.** All four parts are TRUE. (iv) holds in more generality than asked: it needs only seminormality and polynomial weights, with no
Stembridge axioms and no reading-word embedding. Polynomiality is sharp. The minimal failure is gl_2, det^{-1} ⊗ det (one element:
ε̈ = 0 on one side, +∞ on the other). The minimal failure with a missing *edge* is B(0,−1) ⊗ B(2,1) ⊃ B(2,0).
The one-line reason is **the defect identity δ(x⊗y) = δ(x) + δ(y) + min(ε̃_i(x), φ̃_i(y))**. The kill clause of the quasi-tensor rule is
the min term.

---

## 0. Conventions

Type A_{n−1}, weights in Z^n, α_i = e_i − e_{i+1}. Words over [n]: x^w = ∏ x_{w_k}.

**Crystal tensor product, word order.** For seminormal crystals B, B' let B ⊗ B' be B × B' with wt additive and, writing
ε = ε̃_i(x), φ = φ̃_i(x), ε' = ε̃_i(y), φ' = φ̃_i(y), m = min(ε, φ'):
ε̃_i(x⊗y) = ε + ε' − m, φ̃_i(x⊗y) = φ + φ' − m; ẽ_i acts on x iff ε > φ' (else on y); f̃_i acts on y iff φ' > ε (else on x).
This is the convention in which the word crystal of uv is (word crystal of u) ⊗ (word crystal of v): bracket i+1 with a *later* i.
It equals Kashiwara's y ⊗_K x. Checked: `test_iv.py` asserts tensor = concatenation on all 5418 pairs.

**Quasi-tensor product, word order** (Theorem A of PROVE 275; = CGM 2301.00271 Thm 5.1 / CMRR 2309.14898 Def 3.10 with factors reversed,
by the CMRR p.10 remark "x ⊗̈ y is identified with the word yx"). On Q × Q', wt additive, and:
* ε̈_i(x⊗̈y) = φ̈_i(x⊗̈y) = +∞ iff ε̈_i(x) = ∞ or ε̈_i(y) = ∞ or (ε̈_i(x) > 0 and φ̈_i(y) > 0);
* otherwise ε̈ = ε̈(x)+ε̈(y), φ̈ = φ̈(x)+φ̈(y); ë_i acts on x if ε̈(x) > 0, else on y if ε̈(y) > 0, else ⊥; f̈_i acts on y if φ̈(y) > 0,
  else on x if φ̈(x) > 0, else ⊥.

**Quasification** (CMRR 2309.14898 Def 4.5 p.16, read first-hand this session): same set and wt;
ε̈_i(x) = ε̃_i(x), ë_i(x) = ẽ_i(x) if ε̃_i(x) = wt_{i+1}(x), and else ε̈_i(x) = +∞, ë_i(x) = ⊥. Also φ̈ := ε̈ + ⟨wt, α_i⟩ and
f̈_i(x) = y :⟺ ë_i(y) = x. CMRR state it for connected Stembridge crystals. The formula is pointwise, so it applies verbatim to any
seminormal crystal (= componentwise on a disjoint union). That is how Q_{B⊗B'} is meant below.

**Defect.** δ_i(x) := wt_{i+1}(x) − ε̃_i(x). Since φ̃_i − ε̃_i = wt_i − wt_{i+1} (seminormal), also δ_i(x) = wt_i(x) − φ̃_i(x).
So x is **i-alive** (ë_i, f̈_i not forced ⊥, ε̈_i finite) iff δ_i(x) = 0, and the condition is symmetric between ε̃ and φ̃ (= CMRR Lemma 4.4).

**Lemma 0.** (a) δ_i is constant on i-strings. (b) If all weights of B are polynomial (in Z_{≥0}^n), then δ_i ≥ 0 on B.
(c) For alive x: f̈_i(x) = f̃_i(x), and ε̈_i = ε̃_i, φ̈_i = φ̃_i.
*Proof.* (a) ẽ_i lowers both wt_{i+1} and ε̃_i by 1. (b) y = ẽ_i^{ε̃_i(x)} x exists (seminormal), and wt_{i+1}(y) = wt_{i+1}(x) − ε̃_i(x) = δ_i(x) ≥ 0.
(c) If f̃_i(x) = y then ẽ_i(y) = x and y is alive by (a), so ë_i(y) = x, i.e. f̈_i(x) = y. Conversely ë_i(y) = x forces ẽ_i(y) = x, so y = f̃_i(x).
For φ̈: φ̈ = ε̃ + ⟨wt, α_i⟩ = φ̃. ∎

On words: δ_i(w) = #(i+1) − #(unbracketed i+1) = number of bracketed pairs. That is 0 iff w has no subsequence (i+1)…i, since a word with
'(' before ')' has an adjacent "()" in its {i,i+1}-subword. So **Q of the word crystal = the word quasi-crystal** (CMRR 2309.14887 Def 2.13).

## 1. (i) Connected objects ↔ compositions, and ch is injective on isoclasses

𝒬_n := quasi-crystals isomorphic to finite disjoint unions of components of word quasi-crystals [n]^N (N ≥ 0, with [n]^0 = {∅}).
Morphisms are isomorphisms (wt-preserving bijections commuting with ë_i, f̈_i, ε̈_i, φ̈_i).

**Theorem (i).** The map C ↦ ch C = Σ_{x∈C} x^{wt x} induces a bijection
{isoclasses of connected objects of 𝒬_n} → {F_α(x_1..x_n) : α a composition with ℓ(α) ≤ n}, and these F_α are distinct
(indeed Z-linearly independent).

*Proof.* By Theorem B, a connected object is ≅ C_σ ≅ P_D(n) with D = iDes σ ⊆ [N−1]. P_D(n) depends only on (N, D). So the
isoclass is a function of the composition α = α(N, D), and C_σ ≠ ∅ iff P_D(n) ≠ ∅ iff |D| ≤ n−1 iff ℓ(α) ≤ n. Every such α occurs
(take σ with iDes σ = D). Hence connected isoclasses are a *quotient* of {α : ℓ(α) ≤ n}, and ch(P_D(n)) = F_α(x_1..x_n) by Theorem B.

Injectivity, two independent ways:
1. *Character-free.* By Theorem B(iv), P_D(n) has exactly one element b⁰ on which every ë_i is ⊥ (every other b admits some ë_i).
   Its weight is wt(b⁰) = (α_1, …, α_ℓ, 0, …, 0), and an isomorphism preserves "all ë_i = ⊥" and wt. So α is an isomorphism invariant.
2. *Via ch.* F_α = Σ_{β refines α} M_β (Gessel). In n variables, M_β(x_1..x_n) = 0 if ℓ(β) > n, and otherwise its x^{(β,0..0)}
   coefficient is 1. The M_β with ℓ(β) ≤ n have pairwise disjoint monomial supports, so they are linearly independent. The transition
   F → M is unitriangular for refinement order, so {F_α(x_1..x_n) : ℓ(α) ≤ n} is a Z-basis of QSym_n and in particular has no repeats. ∎

Computed (`test_i_ii.py`): n ≤ 4, N ≤ 6 (n ≤ 3) / N ≤ 5 (n = 4). There are 752 components, and canonical forms are computed by BFS from the unique ë-source.
#isoclasses = #compositions with ℓ ≤ n (7/22/42/31), with 0 collisions, and the source weight is α padded every time.

**Corollary.** K_0(𝒬_n) (free on connected isoclasses, [A ⊔ B] = [A] + [B]) → QSym_n, [C] ↦ ch C, is an isomorphism of abelian groups.
Decomposition into connected components is canonical, so K_0 is free on the connected isoclasses. Those go bijectively to a Z-basis.

## 2. (ii) Ring structure

The rule of §0 is pointwise in the factor data, so ⊗̈ is a functor on isomorphisms: Q ≅ Q₁ and Q' ≅ Q'₁ give Q⊗̈Q' ≅ Q₁⊗̈Q'₁. It also
distributes over ⊔. **𝒬_n is closed under ⊗̈.** If Q ⊆ [n]^m and Q' ⊆ [n]^k are unions of components, (u, v) ↦ uv is injective
(lengths fixed) and, by Theorem A, an isomorphism Q⊗̈Q' → {uv}. By Prop P that image is ⊔ C_τ, a union of components of [n]^{m+k}.
The unit is {∅}, and associativity up to isomorphism follows from associativity of concatenation.

**Theorem (ii).** ch(Q⊗̈Q') = ch(Q)·ch(Q') (wt is additive). So K_0(𝒬_n) ≅ QSym_n **as rings**, with isoclasses ↦ F-basis.
In particular C_α ⊗̈ C_β ≅ ⊔_γ C_γ^{⊕ c^γ_{αβ}}, where F_α F_β = Σ c^γ_{αβ} F_γ in QSym_n (F_γ with ℓ(γ) > n drop out).

**Corollary (commutativity for free).** Q⊗̈Q' ≅ Q'⊗̈Q for all Q, Q' ∈ 𝒬_n, although ⊗̈ is not symmetric pointwise (the kill clause is
asymmetric) and there is no canonical commutor. Both sides have the same character, and by (i) the character determines the isoclass.
Computed: n = 3, all σ1, σ2 ∈ S_{≤3} (100 pairs). The abstract ⊗̈ of the abstract components decomposes exactly as the shuffle prediction
(0 failures), and C⊗̈C' ≅ C'⊗̈C componentwise (0 failures).

**Stability n → n+1.** res: 𝒬_{n+1} → 𝒬_n keeps {x : wt_{n+1}(x) = 0} and forgets ë_n, f̈_n. This subset is closed under ë_i, f̈_i for i < n,
and for words it is "words over [n]". So res(C_σ^{[n+1]}) = C_σ^{[n]}. Weights are ≥ 0, so wt_{n+1}(x⊗̈y) = 0 iff both are 0, and the
rule for i < n only uses i-data. Hence res(Q⊗̈Q') = res Q ⊗̈ res Q'. Also ch ∘ res = (x_{n+1} ↦ 0) ∘ ch, and F_α(x_1..x_{n+1})|_{x_{n+1}=0} = F_α(x_1..x_n).
So the K_0-rings form the inverse system QSym_{n+1} → QSym_n, and the graded inverse limit is QSym, with [C_α] ↦ F_α.

## 3. (iii) Levi branching

Fix 1 ≤ a ≤ n−1. For Q ∈ 𝒬_n, Res_a Q keeps ë_i, f̈_i (i ≠ a). Read it as an A_{a−1} × A_{n−a−1} quasi-crystal: indices i < a use
x_1..x_a, and indices i > a are relabelled i − a and use x_{a+1}..x_n. ⊠ denotes the external product (factor-wise structure).

**Theorem (iii).** Let C ≅ C_σ have character F_α(x_1..x_n), N = |α|, D = D(α). Then
  Res_a C ≅ ⊔_{k=0}^{N} C_{β_k}^{(a)} ⊠ C_{γ_k}^{(n−a)}   (terms with ℓ(β_k) > a or ℓ(γ_k) > n−a omitted),
where (β_k, γ_k) is the unique pair with |β_k| = k, and β_k·γ_k = α if k ∈ D ∪ {0, N}, β_k ⊙ γ_k = α if k ∉ D (· = concatenation,
⊙ = merge last part of β with first part of γ). Hence
  ch Res_a C = Σ_k F_{β_k}(x_1..x_a) F_{γ_k}(x_{a+1}..x_n) = F_α(x_1..x_a ; x_{a+1}..x_n) = (Δ F_α) evaluated on the two alphabets.

*Proof.* Theorem C gives the slices C_σ^{(k)} (k = #letters ≤ a) as the Res-components. Here is a cleaner isomorphism than the b-coordinates:
ψ(w) = (w|_{≤a}, w|_{>a} − a) (subwords). ë_i, f̈_i and the inversion test for i < a see only letters i, i+1 ≤ a, so they commute with ψ on the
first coordinate and fix the second. The case i > a is symmetric. Since std w = σ, the letters ≤ a sit exactly at positions σ⁻¹([1,k]), so ψ
is injective on C_σ^{(k)}. Its image is all of C_{σ1} × C_{σ2}, where σ1 = std of σ's values 1..k read in position order, and σ2 is the
same for the values k+1..N. Indeed, placing u at positions σ⁻¹([1,k]) and v + a elsewhere gives a word with standardisation σ, because all
letters of u are smaller than all letters of v + a. Finally, iDes σ1 = D ∩ [1,k−1] and iDes σ2 = (D ∩ [k+1, N−1]) − k, and these are
the D-sets of β_k, γ_k. The last equality is Gessel's F_α(x + y) formula = the definition of Δ on the F-basis (Grinberg–Reiner 1409.8356 §5,
textbook). ∎

Also Res_a(Q⊗̈Q') = Res_a Q ⊗̈ Res_a Q' (the rule is per-index), and (A⊠B)⊗̈(A'⊠B') ≅ (A⊗̈A')⊠(B⊗̈B') via ((a,b),(a',b')) ↦ ((a,a'),(b,b')),
because for i < a all data of (a,b) is that of a. So **Res_a is a ring map K_0(𝒬_n) → K_0(𝒬_a) ⊗ K_0(𝒬_{n−a})**, i.e. f ↦ f(x_{≤a}; x_{>a}).
In the limit a, n−a → ∞ this is Δ: QSym → QSym ⊗ QSym, and its multiplicativity is the bialgebra axiom, now realised by quasi-crystals.
Computed (`test_sym_levi.py`): ψ is an isomorphism onto C_{σ1} × C_{σ2} for all 434 slices (n = 3, 4, N ≤ 4, all a); PROVE 275 checked
the characters 183/183 and connectivity 753/753.

## 4. (iv) Q66 — quasification is strict monoidal

**Defect identity.** For seminormal B, B' and any weights: δ_i(x⊗y) = δ_i(x) + δ_i(y) + min(ε̃_i(x), φ̃_i(y)).
*Proof.* wt_{i+1} is additive, and ε̃_i(x⊗y) = ε̃_i(x) + ε̃_i(y) − min(ε̃_i(x), φ̃_i(y)) by §0. Subtract. ∎

**Theorem (iv).** Let B, B' be seminormal gl_n crystals with all weights polynomial. Then the identity map on B × B' is an equality of
quasi-crystals Q_{B⊗B'} = Q_B ⊗̈ Q_{B'} (word order on both sides; equivalently Q_{B' ⊗_K B} = Q_{B'} ⊗̈_CGM Q_B in Kashiwara/CGM order).

*Proof.* Fix i, x ∈ B, y ∈ B'. Write ε = ε̃_i(x), φ' = φ̃_i(y). By Lemma 0(b) all three summands of the defect identity are ≥ 0, so
  x⊗y alive ⟺ δ(x) = 0 ∧ δ(y) = 0 ∧ min(ε, φ') = 0.
If x is dead, ε̈(x) = ∞ and the ⊗̈ rule kills, which matches. Same for y. If both are alive, ε̈(x) = ε and φ̈(y) = φ' (Lemma 0(c)), so
"min(ε, φ') > 0" is exactly the kill clause "ε̈(x) > 0 ∧ φ̈(y) > 0". So the dead sets coincide, and on them both sides have ε̈ = φ̈ = ∞
and ë = f̈ = ⊥. On the alive set m = 0, so ε̃_i(x⊗y) = ε + ε̃_i(y) = ε̈(x) + ε̈(y), and likewise for φ. The signature rule acts with ẽ_i on x
iff ε > φ'. With m = 0, either ε = 0 (then ẽ acts on y; if also ε̃(y) = 0 both give ⊥) or φ' = 0 < ε (then it acts on x). That is
exactly the ⊗̈ rule "on x if ε̈(x) > 0, else on y". f̃ is symmetric. By Lemma 0(c), ë = ẽ and f̈ = f̃ on alive elements on both sides. ∎

So the answer to "does it need ε̃_i = wt_{i+1} on *both* factors?" is that it's automatic. With polynomial weights, alive(x⊗y) ⇒ alive(x) ∧ alive(y),
because defects only add. This is the abstract reason a dead factor kills in the quasi-tensor rule.

**Sharpness (non-polynomial weights).** Without Lemma 0(b), the defect identity still holds, but δ(x) = −δ(y) ≠ 0 can make x⊗y alive while both
factors are dead.
* *Minimal:* gl_2, B = det^{−1} = {pt, wt (−1,−1)}, B' = det = {pt, wt (1,1)}. δ = −1 and +1, ε̃ = φ̃ = 0. Q_{B⊗B'} has ε̈ = 0, but
  Q_B ⊗̈ Q_{B'} has ε̈ = ∞.
* *Minimal with a lost edge:* gl_2, B = B(0,−1) (weights (0,−1) → (−1,0), δ ≡ −1), B' = B(2,1) (δ ≡ +1). B ⊗ B' ⊃ B(2,0), whose
  3-element 1-string is fully alive in Q_{B⊗B'} (ε̈ = 0, 1, 2), while every element of Q_B ⊗̈ Q_{B'} is dead (`test_iv.py`, printed).
* Non-polynomial is necessary but not sufficient: in the shifted census (B(λ) ⊗ det^c, c ∈ {−2..1}, n = 2, 3), 136 of the 384 non-polynomial pairs
  fail, and all 128 polynomial pairs pass.

**Corollaries.**
(a) Q_{B(λ)} ∈ 𝒬_n for λ ⊢ N with ℓ(λ) ≤ n. A reading-word embedding identifies B(λ) with a union of components of the word crystal [n]^N,
and Q of the word crystal is the word quasi-crystal (§0). Q of a sub-crystal is the restriction, hence closed under ë, f̈, hence a union of
quasi-components. ch Q_{B(λ)} = ch B(λ) = s_λ.
(b) [B] ↦ [Q_B] is a ring map K_0(polynomial gl_n crystals) = Sym_n → K_0(𝒬_n) = QSym_n by Theorem (iv), and it is injective (it is the
inclusion Sym_n ⊂ QSym_n under ch). By (i) the decomposition is forced: [Q_{B(λ)}] = ch⁻¹(s_λ) = Σ_{T ∈ SYT(λ)} [C_{Des T}], using Gessel's
s_λ = Σ_T F_{Des T} (Stanley EC2 Thm 7.19.7). The component count f^λ is CMRR 2309.14898 Cor 4.10. Computed: 37 shapes, |λ| ≤ 5, n ≤ 4,
0 failures.
(c) Res_a ∘ Q = Q ∘ Res_a holds literally (Def 4.5 is per index, and the index-i condition for i > a is the same after relabelling). Together with §3 this makes
Sym → QSym a bialgebra map in the limit. (The content there is all in (iv) and (iii). The Hopf statement for Sym ⊂ QSym is textbook.)

Computed (`test_iv.py`): all pairs λ, μ with |λ|, |μ| ≤ 3 and n = 2, 3, 4, which is 134 tensor pairs and 5418 elements. B ⊗ B' is computed **abstractly** by the
signature rule (not by concatenation). The comparison Q_{B⊗B'} vs Q_B ⊗̈ Q_{B'} on (wt, ë, f̈, ε̈, φ̈) gave **0 failures**.
**Negative control** (kill clause swapped to φ̈(x) > 0 ∧ ε̈(y) > 0): **4500 failures**, so the orientation is the content.

## 5. Owner status

* (i)–(iii): the *content* is Gessel/Malvenuto–Reutenauer (F-basis, shuffle product, F_α(x+y)). The quasi-crystal statements are
  repackaging of PROVE 275 Theorems B, C and Prop P, plus the isoclass/injectivity bookkeeping and the commutativity corollary. The Wake 275 agent text search of CGM 2301.00271
  and CMRR 2309.14887/2309.14898 found no K_0/ring statement. This session I grepped section 4 of 2309.14898 myself: it has no "⊗"/"tensor"
  statement at all, so CMRR do not state Q_{B⊗B'} = Q_B ⊗̈ Q_{B'}.
* **Owner check NOT done:** Maas-Gariépy 2302.07694 (CMRR p.16 calls her construction "equivalent" to Def 4.5) and Brauner–Corteel–
  Daugherty–Schilling 2503.14782 (crystal skeletons). Both are agent-summary only, and this was a no-browsing session. Either could own (iv) or the
  K_0 statement. Prior: (iv) is a 5-line observation once the defect identity is written, so it's likely folklore. Footnote risk, not a gate.

## Gaps

1. Owner check above (MG23, BCDS 2503.14782): one locator read each, next Browse.
2. Citations used as textbook facts, not re-derived here: Gessel's s_λ = Σ_T F_{Des T} (only for the explicit form in Cor (b); the ring-map
   statement doesn't need it); Theorem B(iv)'s unique-source claim is from PROVE 275 (proved there).
3. The definition of 𝒬_n uses words. An intrinsic axiomatic characterisation (CMRR 2309.14898's local axioms ⇒ in 𝒬_n?) is not addressed.
