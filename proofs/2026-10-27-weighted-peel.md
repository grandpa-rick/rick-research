# PROVE 259: The weighted peel (Q45). T-characters on LG, and Theorem Q30 without Buch–Ravikumar

Date: 2026-10-26 (session file dated 2026-10-27 per PROVE.md). Registry: `proofs/registry/q488-converse.json`,
nodes `q488-Q45-equivariant-peel-lift`, `q488-Q45-strict-character`, `q488-Q45-Q30-BR-free`.
Scripts: `work-in-progress/scripts/prove259/` (verify.py, cmp_q45.py, out_*.txt).

## 0. Setting and notation
Type C_m, ε-coordinates, ω = ω_m = ε_1+…+ε_m, x^μ = x_1^{μ_1}⋯x_m^{μ_m}. For a strict κ with parts ≤ m,
D(κ) = shifted diagram, P_κ = D(κ) with product order, w_κ ∈ W^P with w_κω = v_κ (−1 exactly at positions m+1−p,
p ∈ κ) (main.tex §2.2). ch_κ(j) := D_{w_κ}(e^{jω}) ∈ Z[x^±] for all j ∈ Z (Demazure operators, main.tex §2.3).
n_κ(j) := (−1)^{|κ|} ch_κ(−j). For ρ ⊆ κ put θ = D(κ)∖D(ρ). A *V-map* on θ is a strictly order-preserving
g: θ → {e<o} with g = e on diagonal boxes; V(θ) is their number.

**Box weights.** For a box x = (a,b) with offset d = b−a put
  β(x) = ε_m if d = 0,  β(x) = ε_{m−d} − ε_{m+1−d} if 1 ≤ d ≤ m−1.

**Lemma 0 (telescoping).** For every shifted diagram τ: Σ_{x∈D(τ)} β(x) = Σ_{p∈τ} ε_{m+1−p}. Hence
w_τω = ω − 2 Σ_{x∈D(τ)} β(x).
*Proof.* A row of length p has offsets 0,…,p−1; the sum ε_m + Σ_{d=1}^{p−1}(ε_{m−d} − ε_{m+1−d}) telescopes
to ε_{m+1−p}. The second statement is the definition of v_τ. ∎

Also put ℓ(μ) := Σ_c (m+1−c) μ_c (pairing with the regular dominant coweight (m,…,1)). Then ℓ(β(x)) = 1 for every
box: ℓ(ε_m) = 1 and ℓ(ε_{m−d} − ε_{m+1−d}) = (d+1) − d = 1.

## 1. Theorem A (T-character of the LS-parity model). For j ≥ 0,
  ch_κ(j) = Σ_G x^{ j·w_κω + Σ_{x} G(x) β(x) },
the sum over order-preserving G: P_κ → {0,…,2j}, even on diagonal boxes.

*Proof.* By (LS) (main.tex, Littelmann), ch_κ(j) = Σ_π x^{π(1)} over LS paths of shape jω with initial direction
≤ w_κ. Proposition `prop:model` gives a bijection π ↔ g = 2j·t (order-reversing, even on the diagonal), with G = 2j − g,
where t(x) = a_{i(x)} (with t(x) = 0 if x ∉ D(τ_1)). We have to compute π(1) = Σ_i (a_i − a_{i−1}) jw_{τ_i}ω. By
Lemma 0, jw_{τ_i}ω = jω − 2j Σ_{x∈D(τ_i)} β(x). So
  π(1) = jω − 2j Σ_x β(x)·Σ_{i: x∈D(τ_i)} (a_i − a_{i−1}) = jω − 2j Σ_x β(x) t(x) = jω − Σ_x g(x)β(x),
because x ∈ D(τ_i) iff i ≤ i(x), so the inner sum telescopes to a_{i(x)} = t(x). (Boxes x ∉ D(τ_1) contribute 0 = t(x).
The case j = 0 is trivial: one path, G ≡ 0, weight 0.) Substituting g = 2j − G and using Lemma 0 for κ:
jω − 2jΣ_{D(κ)}β + Σ Gβ = j w_κω + Σ Gβ. ∎

## 2. Theorem B (strict side: the T-character of N_κ(j)). For j ≥ 1,
  n_κ(j) = (−1)^{|κ|} ch_κ(−j) = Σ_f x^{ −j·w_κω − Σ_x f(x)β(x) },
the sum over strictly order-preserving f: P_κ → {1,…,2j−1}, even on diagonal boxes. At x = 1 this is Theorem
`thm:main`(b).

*Proof.* Two inputs.

(i) *Exponential form.* For every w, D_w e^{jω} = Σ_u R_u(x)·y_u^j for all j ∈ Z, with finitely many R_u ∈ Q(x)
and Laurent monomials y_u, independent of j. Induction on the word: D_k(r·e^{jν}) = (r e^{jν} − e^{−α_k}s_k(r)e^{j s_kν})/
(1−e^{−α_k}), the same rational formula for every j (the piecewise formula in main.tex §2.3 is this quotient).
Consequently, with F(t) := Σ_{j≥0} ch_κ(j)t^j = Σ_u R_u/(1−y_u t) ∈ Q(x)(t), one has
  Σ_{j≥1} ch_κ(−j) t^j = Σ_u R_u (t/y_u)/(1−t/y_u) = −F(1/t)        (Popoviciu/Stanley, EC1 Prop. 4.2.3 style).

(ii) *Stanley reciprocity for a cone.* Let M = Λ'×Z, Λ' = {G ∈ Z^{P_κ}: G even on diagonal boxes}, and
C = {(G,s) ∈ R^{P_κ}×R: 0 ≤ G(x) ≤ 2s, G order-preserving}, a pointed rational cone of dimension d+1, d = |κ|,
with C∩{s=0} = {0}. Its interior points in M are (f,j) with f strictly order-preserving, 0 < f < 2j, f ∈ Λ'. Stanley's
reciprocity theorem (Stanley, Adv. Math. 14 (1974); Beck–Robins, *Computing the continuous discretely*, Thm 4.3,
applied after the linear isomorphism M ≅ Z^{d+1} halving diagonal coordinates) gives, in Q(z,s),
  σ_{C°}(z,s) = (−1)^{d+1} σ_C(z^{−1}, s^{−1}),  σ_K(z,s) := Σ_{(G,j)∈K∩M} z^G s^j.
Specialize z^G ↦ x^{Σ G(x)β(x)}, s ↦ x^{w_κω}·t. Every ray of C has s-degree ≥ 1, so each denominator factor of σ_C
becomes 1 − (monomial)·t^{k}, k ≥ 1, nonzero; and since each t-degree slice of C∩M is finite, the specialization is a
ring map on the series side, compatible with the rational expressions. By Theorem A, the specialized σ_C is F(t).
Specializing σ_{C°} at z ↦ x^{−β}, s ↦ x^{−w_κω}t and applying the reciprocity identity:
  Σ_{j≥1} t^j Σ_f x^{−j w_κω − Σ fβ} = (−1)^{d+1}F(1/t).
Compare with (i): Σ_{j≥1} ch_κ(−j)t^j = −F(1/t) = (−1)^d·(that sum). Take coefficients of t^j. ∎

## 3. Theorem C (the weighted peel). For j ≥ 1 and every κ,
  n_κ(j+1) = Σ_{ρ⊆κ} P_{κρ}(x) n_ρ(j),   P_{κρ}(x) := Σ_{g V-map on θ} x^{ −w_κω − Σ_{x∈θ, g(x)=o} β(x) },
and the bijection of `lem:peel` (f ↦ (f|_θ, f|_{D(ρ)}), with e = 2j, o = 2j+1) is weight-preserving for the weights
of Theorem B. In particular P(x) is coefficient-positive, P(1) = I+V, supp P = supp(I+V), and each entry is a sum of
exactly V(θ) monomials, which is the Wake 259 observation. Moreover the identity holds for all j ∈ Z:
  ch(i−1) = S P(x) S · ch(i)  for every i ∈ Z,  S = diag((−1)^{|κ|}).   (†)
Equivalently, the Wake 259 solve C(x) (ch(j+1) = C ch(j)) is C = S P^{−1} S.

*Proof.* Let f be a level-(j+1) strict map (values in [2j+1]) and (g,h) its peel: θ = f^{−1}{2j,2j+1}, h = f|_{D(ρ)}
a level-j map. Write g̃(x) = f(x) ∈ {2j, 2j+1} on θ. By Theorem B,
  wt_{j+1}(f) − wt_j(h) = −(j+1)w_κω + j w_ρω − Σ_{x∈θ} g̃(x)β(x).
By Lemma 0, w_ρω = w_κω + 2Σ_θ β, so this is −w_κω + Σ_θ (2j − g̃(x))β(x) = −w_κω − Σ_{g(x)=o} β(x). It depends
only on g, not on j or h. Summing over the bijection of `lem:peel` gives the identity for j ≥ 1. Writing n = S ch(−·):
ch(i−1) = SPS ch(i) for all i ≤ −1. Each entry of the difference is of the form Σ_u R_u y_u^i (by §2(i)), and it vanishes
on infinitely many consecutive integers, so it vanishes identically (Vandermonde over Q(x)). Hence (†) holds for all
i. ∎

Sanity example (m = 3): P[(2),(1)]: θ = {(0,1)}, −w_{(2)}ω = (−1,1,−1). For g = e we get x_2/(x_1x_3). For g = o,
subtract β(0,1) = ε_2 − ε_3 to get 1/x_1. The sum (x_2+x_3)/(x_1x_3) is the Wake 259 entry.

## 4. Lemma D (equivariant independence). For any finite set R of strict partitions (parts ≤ m), the functions
j ↦ ch_ρ(j) (j ≥ 1), ρ ∈ R, are linearly independent over Q(x).

*Proof.* Suppose Σ_ρ a_ρ ch_ρ(j) = 0 for all j ≥ 1, with a_ρ ∈ Q[x^±] not all zero (clear denominators). Grade Laurent
polynomials by ℓ. By Theorem A and ℓ(β) = 1, ch_ρ(j) = x^{j w_ρω}·(1 + terms of ℓ-degree ≥ 1 higher), and
ℓ(w_ρω) = ℓ(ω) − 2|ρ| (Lemma 0). Let a_ρ^{low} be the lowest ℓ-component of a_ρ, of degree δ_ρ. The lowest-degree part
of a_ρch_ρ(j) is a_ρ^{low}x^{jw_ρω}, of degree δ_ρ + jℓ(ω) − 2j|ρ|. Let N = max{|ρ| : a_ρ ≠ 0}. For j larger than the
spread of the δ's, the minimum of these degrees is attained exactly at T* = {ρ : a_ρ≠0, |ρ| = N, δ_ρ minimal}, and
every other contribution has strictly higher degree. Hence Σ_{ρ∈T*} a_ρ^{low}·(x^{w_ρω})^j = 0 for all large j. The
x^{w_ρω} are pairwise distinct (distinct sign vectors), so Vandermonde over Q(x) gives a_ρ^{low} = 0, a contradiction. ∎

(Remark: this is exactly what fails at x = 1. Crown K / Dream 258: H_ρ = ch_ρ|_{x=1} are dependent for κ = (3,1).
The torus breaks the dependence.)

## 5. Theorem E (equivariant K-Chevalley for L^{−1} on LG, and Theorem Q30 without (BR)).
Inputs: (G0), (G1) in its T-equivariant form (as stated in main.tex, (G1) is a statement about T-characters), and
(KT): the image of K^T_0(X_κ) in K_T(X) is spanned over R(T) by [O_{X_ρ}]_T, ρ ⊆ κ. (KT) follows from the equivariant
localization sequence and K^T_0(cell) = R(T) (Thomason), exactly as in the proof of `lem:hyperplane`. Also: the
forgetful map K_T(X) → K(X) sends [O_{X_ρ}]_T ↦ [O_{X_ρ}] and restricts to the augmentation x ↦ 1 on R(T).

**Statement.** In K_T(LG(m,2m)), [O_{X_κ} ⊗ L^{−1}]_T = Σ_{ρ⊆κ} A_{κρ}[O_{X_ρ}]_T with
A_{κρ} = ψ((−1)^{|θ|}P_{κρ}(x)) (ψ = the duality x ↦ x^{−1} of R(T), coming from the dual in (G1)). In particular
A is unique, and A_{κρ} is (−1)^{|θ|} times a positive sum of V(θ) monomials. Forgetting T:
  [O_{X_κ}]·O^1 = Σ_{ρ⊊κ} (−1)^{|θ|−1} V(θ) [O_{X_ρ}],
which is Theorem `thm:Q30` (c_ρ = (−1)^{|θ|−1}V(θ)), proved from (G0), (G1), (LS), (KT) and Stanley reciprocity,
**without (BR)**.

*Proof.* By (KT) choose A_{κρ} ∈ R(T) with [O_{X_κ}⊗L^{−1}]_T = Σ_{ρ⊆κ}A_{κρ}[O_{X_ρ}]_T. Put
Φ(F)(j) := ψ χ_T(X, F⊗L^j). It is ψ-semilinear over R(T), and for j ≥ 1 equivariant (G1) gives
Φ(O_{X_ρ})(j) = ch_ρ(j) and Φ(O_{X_κ}⊗L^{−1})(j) = ch_κ(j−1) (j−1 ≥ 0, L^j⊗L^{−1} = L^{j−1} equivariantly).
So ch_κ(j−1) = Σ_ρ ψ(A_{κρ}) ch_ρ(j) for j ≥ 1. By (†), ch_κ(j−1) = Σ_ρ (SPS)_{κρ} ch_ρ(j), and row κ of SPS is
supported on ρ ⊆ κ. Subtracting and applying Lemma D gives ψ(A_{κρ}) = (−1)^{|κ|+|ρ|}P_{κρ}. Since |κ|−|ρ| = |θ|, this
is the formula. At x = 1, A(1) = S(I+V)S, so [O_κ](1−[L^{−1}]) = Σ_ρ (δ_{κρ} − (−1)^{|θ|}V(θ))[O_ρ]. The diagonal
coefficient is 1 − V(∅) = 0, and for ρ ⊊ κ it is (−1)^{|θ|−1}V(θ). By (G0), 1 − [L^{−1}] = O^1. ∎

## 6. Verification (computational)
`work-in-progress/scripts/prove259/verify.py m J` builds ch_κ(j) by Demazure operators (dem.py from prove249d) and
compares with the explicit sums.
- V1 (Theorem B), V2 (Theorem A), V3 (Theorem C, peel identity at the character level): all True for
  m = 2 (j ≤ 4), m = 3 (j ≤ 4), m = 4 (j ≤ 5), m = 5 (j ≤ 4). Outputs: out_verify_m4.txt, out_verify_m5.txt.
- cmp_q45.py: all 22 nonzero entries of the combinatorial P at m = 3 equal the Wake 259 linear-solve S C^{−1} S
  (out_q45_m3.txt).
- Negative control (verify.py 3 4 pert): flip β on offset-1 boxes to ε_{m−1}+ε_m. V1, V2 and V3 all FAIL (several κ,
  every j ≥ 2). out_negctrl_m3.txt. The control breaks the claim, not just a relabeling of it.
- Lemma D for m = 3: the Wake 259 solve had unique solutions for every κ (the coefficient matrix was invertible).

## 7. Gaps / honesty
- Theorems A–C and Lemma D: complete given (LS) (already a cited input of the paper, read first-hand in the ICM
  survey) and Stanley's cone reciprocity (a textbook theorem; Beck–Robins Thm 4.3, cited by statement and not
  re-derived). Grade: proved.
- Theorem E additionally uses (KT) and the equivariant reading of (G1). (G1) as printed in main.tex is already a
  character statement, so this is no new input. (KT) is standard (the equivariant version of the localization argument
  already in `lem:hyperplane`), but I have not written out the Thomason homotopy-invariance citation with a locator.
  Grade: proved modulo (KT) as a cited standard input. The ψ convention only affects the equivariant statement, not
  the x = 1 corollary.
- Owner: the equivariant Chevalley formula for [L_{±λ}][O_w] is owned (Lenart–Shimozono 1203.3237 Thm 3.2/Cor 3.4;
  Lenart–Postnikov math/0309207; Pittie–Ram). Equivariant coefficients are unique, so the ω_m case of their
  formula must equal A above. Nonequivariantly, Q30 is the x = 1 case of K-Chevalley for L^{−1}, so the *values* c_ρ
  are in principle owned by K-Chevalley as well as by BR. What is new here is the derivation route:
  LS → Stanley reciprocity → strict characters → weighted peel → independence ⇒ Pieri. It also gives the closed
  shifted-diagram form (V(θ), one monomial per V-map) and explains the Wake 259 positivity. I did not check that the
  ω_m case of LS Cor 3.4 reads literally as P (no browsing this session). Footnote-level risk, per the PERSONALITY gate.
- The draft is not touched. This is post-submission material. At most a Remark: "Theorem Q30 also follows from (LS)
  by working T-equivariantly, because the T-characters ch_ρ are independent although the H_ρ are not."
