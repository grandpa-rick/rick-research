# Seed Q1, braided form: is it empty at its obvious point? (Day 241 PROVE)

**Date:** 2026-10-15. **Code:** `code/seedq1/{qqsym,psitest,lattice,lattice_test,lattice_bialg}.py`.
**Registry:** `proofs/registry/seed-q1-braided-terminal.json`.

**Verdict, short version.**
- (a) TRUE and trivial, but it says nothing specific about the braiding. Classical ABS's ζ isn't a graded map either.
- (b) The fix is to give ζ values in a Λ-graded target A = k_φ[Λ₊] (u-bookkeeping, i.e. a twisted monoid algebra). With that, ABS terminality transports **verbatim** to braided bialgebras in C_q (Thm 2). The terminal object is a quantum quasi-shuffle algebra QSym_{q,φ}. What does **not** transport is the character *group*: convolution of characters is no longer a character (Prop 3).
- (c) Rank 1 passes, and the controls break.
- **New and unplanned (Thm 4).** In rank ≥2 at generic q, *scalar* characters of f (φ=0) are degenerate. The q-Serre relations force ζ(F_i)ζ(F_j)=0 on every Dynkin edge, so Ψ never sees an edge. You need a quantum-torus target, u_iu_j = q^{±1}u_ju_i on edges, to get a nondegenerate Ψ. Then Ψ is injective on f, and it lifts Rosso's quantum-shuffle embedding through the "merge" quotient.

So the degenerate point was not empty. It said where the question lives: **in the antisymmetric part of the target's twist φ**, not in the braiding of H.

---

## 0. Setup

- Λ = Z^I, Λ₊ = N^I∖0, and ( , ) is a symmetric bilinear form on Λ. Rank 1: I = {1}, (a,b) = ab.
- **C_q** is the category of Λ_{≥0}-graded k-vector spaces, k = Q(q), q generic. The braiding is c(x⊗y) = q^{(|x|,|y|)} y⊗x.
  - This is natural with respect to graded maps.
  - It is compatible with any graded product: (a,b+c) = (a,b)+(a,c).
- **Braided bialgebra in C_q.** Graded algebra + graded coalgebra, such that Δ(xy) = Δ(x)·Δ(y) in the braided tensor product: (a⊗b)(c⊗d) = q^{(|b|,|c|)} ac⊗bd. "Connected" means H_0 = k.
- **Twisted target.** Take φ: Λ×Λ → Z bilinear (any bilinear form is a 2-cocycle). Set A_φ = ⊕_{λ≥0} k u_λ with u_a u_b = q^{φ(a,b)} u_{a+b}.
  - A_φ is an associative graded algebra, hence an algebra in C_q. Algebra axioms don't use the braiding.
  - A *φ-character* is a graded algebra map ζ: H → A_φ. Equivalently, it is a scalar function ζ(h) (h homogeneous, ζ(h)u_{|h|} the value) with ζ(1)=1 and ζ(xy) = q^{φ(|x|,|y|)}ζ(x)ζ(y).
  - φ=0 gives ordinary characters, i.e. the classical ABS notion.
- **QSym_{q,φ}.**
  - Basis: M_α for words α = (α_1,…,α_ℓ) in Λ₊. Degree |α| = Σα_i.
  - Coproduct: deconcatenation, Δ M_α = Σ_{α=α'α''} M_{α'}⊗M_{α''}.
  - Product: M_α * M_β = Σ_{(f,g)} wt(f,g) M_{γ(f,g)}.
    - Here (f,g) runs over quasi-shuffles: f: [r]→[m] and g: [s]→[m] strictly increasing, with im f ∪ im g = [m]. γ_k is the sum of the α_i and β_j sitting at position k.
    - The weight is wt = Π_{(i,j): g(j)<f(i)} q^{(β_j, α_i)} · Π_{(i,j): f(i)=g(j)} q^{φ(α_i,β_j)}. The first factor is a crossing weight and the second a merge weight.
  - ζ_Q(M_α) = [ℓ(α) ≤ 1] u_{|α|}.
  - Rank 1 with φ=0 gives "QSym_q": M_a*M_b = M_{ab} + q^{ab}M_{ba} + M_{a+b}.
  - In JRZ terms (from memory, **not deep-read**) this is the quantum quasi-shuffle algebra on the algebra A_φ,₊ in C_q.

## 1. Part (a): the naive question is vacuous, and that's not news

**Prop 1.** Let ζ: H → 𝟙 = k (in degree 0) be a morphism in C_q. Then ζ(H_+) = 0.

*Proof.* Morphisms in C_q are degree-preserving, and 𝟙 is concentrated in degree 0. ∎

**The point.**
- Classical ABS has the same "problem". ζ_Q(M_(n)) = 1 ≠ 0 in degree n, so ABS's ζ is a map in Vect, not in graded Vect.
- Classically this is harmless. The forgetful functor grVect → Vect is *symmetric monoidal* (trivial braiding on both sides).
- For q ≠ 1 the forgetful functor C_q → Vect is monoidal but **not braided**. So "forget the grading" is not available.
- The u-bookkeeping in §0 is the replacement. Keep the degree in u_λ and you stay inside C_q.
- With φ=0 a graded ζ: H → A_0 = k[Λ_{≥0}] is the same data as a classical character. So no characters are lost.
- PROVE.md's (b)(ii) is the right candidate. The twist φ is an *extra* degree of freedom that the classical theory can't see in rank 1: every bilinear φ on N is symmetric, so A_φ ≅ A_0 via u_n ↦ q^{φ(1,1)n²/2}u_n, after adjoining q^{1/2}. In rank ≥2 it matters (§4).

**(b)(i) dies as stated.** ζ⊗ζ is not an algebra map out of the braided tensor product H⊗H. Indeed (ζ⊗ζ)((a⊗b)(c⊗d)) = q^{(|b|,|c|)}ζ(a)ζ(b)ζ(c)ζ(d). For this to be a product of characters we need q^{(|b|,|c|)} = 1 whenever ζ(b)ζ(c) ≠ 0. But the terminality proof never needs ζ⊗ζ to be multiplicative on H⊗H. It only needs ζ∘m_H = m_A∘(ζ⊗ζ) as *linear* maps, and that is just "ζ is an algebra map". See Thm 2, step 3.

## 2. Braided ABS terminality

**Lemma A (coalgebra cofreeness, braiding-free).**
- Let C be a connected Λ-graded coalgebra and ζ: C → A_φ graded linear with ζ|_{C_0} = ε.
- Then there is a unique graded coalgebra map Ψ: C → QSym_{q,φ} with ζ_Q∘Ψ = ζ, namely
  Ψ(h) = Σ_α ζ_{α_1}⊗…⊗ζ_{α_ℓ}(π_α Δ^{(ℓ−1)} h) M_α,
  where ζ_λ is the scalar part of ζ on C_λ and π_α projects onto C_{α_1}⊗…⊗C_{α_ℓ}.

*Proof.*
- *Uniqueness.* For x ∈ QSym, the coefficient of M_α in x equals p_{α_1}⊗…⊗p_{α_ℓ}(Δ^{(ℓ−1)}x). Here p_λ is the coefficient of the one-letter word M_(λ), and p_λ = (scalar part of ζ_Q) on degree λ.
  If Ψ is a coalgebra map, Δ^{(ℓ−1)}Ψ = Ψ^{⊗ℓ}Δ^{(ℓ−1)}. So the coefficient of M_α in Ψ(h) is ⊗_i (ζ_Q Ψ)_{α_i}(π_αΔ^{(ℓ−1)}h) = ⊗_i ζ_{α_i}(π_αΔ^{(ℓ−1)}h).
- *Existence.* Define Ψ by the formula.
  - The coefficient of M_β⊗M_γ in ΔΨ(h) is the coefficient of M_{βγ} in Ψ(h). That is ⊗ζ(π_{βγ}Δ^{(ℓ+m−1)}h).
  - By coassociativity this equals (⊗ζ π_βΔ^{(ℓ−1)} ⊗ ⊗ζ π_γΔ^{(m−1)})(Δh). That is the coefficient in (Ψ⊗Ψ)Δh.
  - The counit is fine because C is connected, and ζ_QΨ = ζ by construction.
- No braiding appears anywhere: coalgebra axioms don't use c. ∎

**Lemma B.** QSym_{q,φ} is a connected braided Hopf algebra in C_q, and ζ_Q is a φ-character.

*Proof.*
- *Associativity.*
  - Iterating the definition, (M_α*M_β)*M_γ and M_α*(M_β*M_γ) are both sums over triple quasi-shuffles (f,g,h) into [m]. These are jointly surjective and strictly increasing, with at most one letter of each word per position.
  - The two-step decompositions biject with triple quasi-shuffles in both bracketings (standard).
  - Crossing weights: a later-word letter y at a position strictly before an earlier-word letter x contributes q^{(y,x)}. In either bracketing, merged letters cross bilinearly, (y,x+x') = (y,x)+(y,x'). So both give Π over such pairs q^{(y,x)}, a bracketing-free expression.
  - Merge weights: three letters a,b,c merged give q^{φ(a,b)+φ(a+b,c)} vs q^{φ(b,c)+φ(a,b+c)}. These are equal because φ is bilinear (cocycle). Two-letter merges agree trivially.
- *Bialgebra axiom.* Take a quasi-shuffle (f,g) of α,β plus a cut point k ∈ [0,m] of γ(f,g).
  - These biject with tuples (cut α=α'α'', cut β=β'β'', quasi-shuffle of (α',β'), quasi-shuffle of (α'',β'')). A cut never splits a merged letter, since merged letters occupy one position.
  - Merge weights live on one side.
  - Crossing pairs inside (α',β') or (α'',β'') are the crossings of the two smaller quasi-shuffles.
  - Pairs (α'-letter, β''-letter) never cross: the α' letter is left of the cut and the β'' letter is right of it.
  - Pairs (α''-letter x, β'-letter y) *always* cross. Together they give q^{(|β'|,|α''|)}.
  - So Δ(M_α*M_β) = Σ q^{(|α''|,|β'|)} (M_{α'}*M_{β'})⊗(M_{α''}*M_{β''}) = (m⊗m)(1⊗c⊗1)(ΔM_α⊗ΔM_β). Unit and counit are clear.
- *Antipode.* It exists by Takeuchi's formula S = Σ_k (−1)^k m^{(k)}(id−ηε)^{⊗k}Δ^{(k)}. This is locally finite on a connected graded bialgebra and uses no braiding.
- *ζ_Q.* ζ_Q(M_α*M_β) is nonzero only if some quasi-shuffle word has length ≤1.
  - If ℓ(α)+ℓ(β) ≥ 3, every word has length ≥2, and ζ_Q(M_α)ζ_Q(M_β) = 0 as well.
  - If α=(a), β=(b), the only length-1 term is the merge, with coefficient q^{φ(a,b)}. So ζ_Q(M_a*M_b) = q^{φ(a,b)}u_{a+b} = u_a u_b.
  - Empty words are trivial. ∎

**Theorem 2 (braided ABS).** Let H be a connected braided bialgebra in C_q and ζ: H → A_φ a φ-character. Then there is a unique graded coalgebra map Ψ: H → QSym_{q,φ} with ζ_QΨ = ζ, and Ψ is a morphism of braided bialgebras. So (QSym_{q,φ}, ζ_Q) is terminal among (connected braided bialgebras in C_q, φ-characters). For q=1, φ=0, Λ=Z, this is ABS Thm 4.1.

*Proof.*
1. Ψ exists and is unique by Lemma A.
2. Consider X = Ψ∘m_H and Y = m_Q∘(Ψ⊗Ψ), both maps H⊗H → QSym. Here H⊗H carries the braided tensor-product coalgebra structure (1⊗c⊗1)(Δ⊗Δ), which is graded and connected.
   - X is a coalgebra map because m_H is one (bialgebra axiom for H).
   - Ψ⊗Ψ is a coalgebra map between braided tensor coalgebras, because Ψ is graded and c is natural: c(Ψ⊗Ψ) = (Ψ⊗Ψ)c.
   - m_Q is a coalgebra map by Lemma B. So Y is a coalgebra map.
3. ζ_Q X = ζ m_H = m_A(ζ⊗ζ), because ζ is an algebra map. Also ζ_Q Y = m_A(ζ_Q⊗ζ_Q)(Ψ⊗Ψ) = m_A(ζ⊗ζ), because ζ_Q is an algebra map (Lemma B).
4. By uniqueness in Lemma A applied to C = H⊗H, X = Y. Units are clear. ∎

**Where q went.** Only into QSym's product (crossing weights) and A's product (merge weights). The universal property is formally identical to ABS. The proof is ABS's / Grinberg–Reiner's §5 argument, which is natural in the braiding. **Novelty: unknown, and I'd bet folklore or JRZ.** The JRZ quantum-quasi-shuffle universal property (0908.0083 / 1302.5888) must be read first-hand before claiming anything (Browse).

**Prop 3 (what does NOT transport: the character group).** Take q ≠ 1, rank 1, φ=0, H = k[F]. The convolution m_A(ζ_t⊗ζ_s)Δ of the characters ζ_t(F)=t and ζ_s(F)=s is not a character unless ts=0.

*Proof.* ΔF^(n) = Σ F^(a)⊗F^(n−a) with F^(n)=F^n/[n]_q!, and a character χ has χ(F^(n)) = χ(F)^n/[n]!. So the convolution has value Σ_a t^a s^{n−a}/([a]![n−a]!) on F^(n). At n=2, times [2]!: t²+(1+q)ts+s², which is ≠ (t+s)² unless ts=0. ∎

So ABS's even/odd factorization (built on the character group) has no direct braided analogue. Convolution is multiplicative only into a *braided-commutative* target, and A_φ is braided-commutative on the diagonal only if (a,a)=0.

## 3. Part (c): rank-1 test

H = f(sl_2)-model: k[F] with |F|=1, braiding q^{ab}, ΔF primitive. Then ΔF^n = Σ [n,a]_q F^a⊗F^{n−a}, since (1⊗F)(F⊗1) = qF⊗F, and so ΔF^(n) = Σ F^(a)⊗F^(n−a). For ζ(F)=t:

  Ψ(F^(n)) = t^n Σ_{α⊨n} M_α / Π_i [α_i]_q!.

For example, Ψ(F^(3)) = t³(M_{111} + (M_{12}+M_{21})/[2] + M_3/([2][3])).

**Checks** (psitest.py, SymPy-exact in q,t):
- Ψ(F^(a))*Ψ(F^(b)) = [a+b,a]_q Ψ(F^(a+b)) for all a+b ≤ 4: **6/6 TRUE**.
- **Control, wrong braiding.** QSym built with q^{−ab} crossings: **0/6** (all fail).
- **q=1.** Ψ(F^(2)) = t²(M_11 + M_2/2) = t²h_1²/2, so Ψ(F^n/n!) = h_1^n/n!, the classical ABS image.
  - Correction to PROVE.md: it said "h_n-image". That would need ζ(F^n/n!) = 1 for all n, which is not multiplicative. The right statement is h_1^n/n!.
- **Uniqueness** is Lemma A, so it holds automatically: no free parameter beyond t.

Wider checks (exact rational arithmetic, q=3/7):
- QSym_q rank 1: associativity 111/111 (deg ≤6), braided bialgebra axiom 129/129 (deg ≤6), ζ_Q multiplicative.
- **Controls.** Crossings q, braiding q^{−1}: 49/49 FAIL. Crossings q^{−1}, braiding q: 49/49 FAIL. q=1: 49/49 pass.
- Ψ on the free braided algebra on letters of degrees 1,2,1 with random t's: Ψ(uv)=Ψ(u)*Ψ(v) 400/400. Both mismatched-braiding controls 400/400 FAIL.
- Lattice rank 2 (sl_3 form), φ ∈ {0, Feigin-type, random bilinear}:
  - Free-algebra Ψ multiplicativity 128/128 each.
  - QSym_{q,φ} bialgebra axiom 225/225 and associativity 0 failures.
  - Inverted-braiding control 223/225 FAIL. The 2 survivors have one side of degree 0 or crossing exponent 0, i.e. degenerate pairs.

## 4. Rank ≥2: scalar characters of f are degenerate; the quantum torus is forced

f = U_q^- is the free braided algebra on primitive F_i (|F_i| = α_i) modulo the q-Serre ideal. With q_{ij} = q^{(α_i,α_j)}, the q-Serre element for an edge with a_ij = −1 is

  S_ij = ad_c(F_i)²(F_j) = F_i²F_j − (q_i + q_i^{−1}) F_iF_jF_i + F_jF_i², where q_i = q^{(α_i,α_i)/2}.

Computed: the kernel of Rosso's map in degree 2α_1+α_2 for sl_3 is spanned by (1, −(q+q^{−1}), 1). That matches.

**Theorem 4.** g of finite type, q generic, ζ: f → A_φ a φ-character, t_i = ζ(F_i). For i ≠ j put x = q^{φ(α_i,α_j)}, y = q^{φ(α_j,α_i)}, d = φ(α_i,α_j) − φ(α_j,α_i), q_{ij} = q^{(α_i,α_j)}, n = 1 − a_ij.
1. **Serre value.** ζ(ad_c(F_i)^n F_j) = t_i^n t_j q^{φ(α_i,α_i)C(n,2)} x^n Π_{k=0}^{n−1}(1 − q_ij q_ii^k · y/x).
   So for t_it_j ≠ 0, the relation is respected iff d ∈ {(α_i,α_j) + k(α_i,α_i) : 0 ≤ k ≤ −a_ij}.
2. **Both relations of a pair** (n = 1−a_ij and 1−a_ji) are respected with t_it_j ≠ 0 iff d = ±(α_i,α_j), using d_ia_ij = d_ja_ji and 0 ≤ k ≤ −a_ij, 0 ≤ k′ ≤ −a_ji. For a non-edge, (α_i,α_j)=0, so this means φ is symmetric on the pair.
   - Possible intermediate solutions d_i(a_ij+k) + d_jk′ = 0 with 0<k<−a_ij: in finite type one of a_ij, a_ji is −1, and then the only solutions are the endpoints.
3. **φ = 0 (ordinary scalar characters).** d=0 requires −a_ij/2 ∈ [0,−a_ij] ∩ Z *and* −a_ji/2 ∈ Z, i.e. both a_ij and a_ji even. That never happens in finite type, where a_ija_ji ∈ {1,2,3}.
   So **t_it_j = 0 on every edge**, and supp(t) is an independent set S of the Dynkin diagram. Then Ψ(F_j)=0 for j ∉ S, and Ψ factors through f/(F_j : j∉S), which is generated by the pairwise commuting F_i, i ∈ S. **Ψ(f) is commutative and generated by |S| elements: the braided ABS map of f sees no edge of the diagram.**
   (Aside: in affine A_1^{(1)}, a_ij = a_ji = −2, so d=0 is allowed and scalar characters are not degenerate there.)
4. **Feigin-type φ.** Choose an orientation and put d = ±(α_i,α_j) on each pair (0 on non-edges). Then every t ∈ (k^×)^I extends to a φ-character of f. The resulting Ψ_φ: f → QSym_{q,φ} is **injective**, and π∘Ψ_φ = Rosso∘(F_i ↦ t_iF_i), with π the quotient described below.

*Proof.*
- (1): ad_c(F_i)^n(F_j) = Σ_p (−1)^p q_ii^{C(p,2)} q_ij^p [n,p]_{q_ii} F_i^{n−p}F_jF_i^p. This is the standard expansion of the iterated braided commutator, checked by kernel computation for sl_3 and B_2.
  ζ of the word F_i^{n−p}F_jF_i^p equals t_i^nt_j q^{φ(α_i,α_i)C(n,2)} x^{n−p}y^p.
  Then apply Gauss's q-binomial theorem Σ_p (−1)^p z^C(p,2)[n,p]_z w^p = Π_{k<n}(1 − z^k w) with z = q_ii, w = q_ij y/x.
- (2) and (3) are arithmetic on (1), using (α_i,α_j) = d_ia_ij and (α_i,α_i) = 2d_i.
- (3), factorization: J = (F_j : j∉S) is a biideal (generated by primitives). So Δ^{(ℓ−1)}J ⊂ Σ f⊗…⊗J⊗…⊗f, and ζ kills J. Hence every coefficient of Ψ on J vanishes.
- (4), existence: (2) kills all Serre generators.
- (4), injectivity:
  - Let I_ns be the span of the M_α having some letter not a simple root. It is a two-sided ideal (merges only make letters bigger) and a coideal (deconcatenation keeps the bad letter on one side).
  - The quotient has basis the words in simple roots, with merges zero. It is the quantum shuffle algebra Sh_q(V) on V = span{α_i}, independent of φ.
  - π∘Ψ_φ is a graded coalgebra map f → T^c(V) with V-component F_i ↦ t_ix_i. Coalgebra maps into cofree T^c(V) are determined by their V-component (Lemma A).
  - So π∘Ψ_φ = Rosso∘rescaling, and Rosso's quantum symmetrizer map is injective on f, since f = Nichols algebra B(V) at generic q (Rosso, Invent. Math. 133 (1998); Lusztig's f = free/radical). This is **cited from memory, not deep-read**. ∎

Verified (lattice_test.py, sl_3, q = 3/7, t = (2, −5/3)):
- φ=0: Ψ(S_12) ≠ 0 and Ψ(S_21) ≠ 0.
- φ antisymmetric part ±1: both zero.
- Antisymmetric part 2: nonzero.
- That is exactly x/y ∈ {q^{±1}}.

**Reading.**
- The dream's hunch was "the braided terminal map restricted to f is Rosso's embedding". That is TRUE in rank 1, FALSE for scalar characters in rank ≥2, and TRUE again (after the merge quotient π) once the target is a Feigin-type quantum torus.
- So the quantum content of Seed Q1's braided form is carried by **the antisymmetric part of the target twist φ**. It is not carried by the braiding of H, which enters symmetrically and already works in Thm 2.
- The Feigin homomorphism U_q(n) → quantum torus (Berenstein; Joseph; "Feigin's map") is the obvious owner of the target side. **From memory, not checked.**

## 5. Gaps (precise)

1. **Novelty of Thm 2 / Lemma B.** QSym_{q,φ} is (I believe) JRZ's quantum quasi-shuffle algebra on A_φ,₊. Its braided-bialgebra property is presumably their theorem, and a braided ABS terminality may be in JRZ II 1302.5888 or Jian's later papers. The proofs above are self-contained, so the gap is attribution only. → Browse.
2. ~~Non-simply-laced existence~~ CLOSED by Thm 4(1)–(2) (q-binomial theorem). Checked on B_2 (b2_test.py): S(a1+3a2) is killed at d ∈ {−2,0,2} and S(2a1+a2) at d = ±2, exactly as predicted, so the intersection is ±(α_1,α_2). G_2 has not been computed. The expansion formula for ad_c^n is standard but was only checked for n ≤ 3.
3. ~~**Thm 4(4) injectivity** rests on f ≅ B(V) / injectivity of Rosso's map, cited from memory (standard, but not deep-read this cycle).~~ **CLOSED Day 242** (`2026-10-16-thm4-4-injective-self-contained.md`): injectivity is definitional for f = 'f/ker Θ via π∘Ψ_φ = Θ∘D_t; existence for the forced twist via the sorted-word character (also removes the hidden use of Lusztig 33.1.3 in (4)'s existence step); G2 case of gap 2 also closed symbolically.
4. Thm 4(3)'s statement "Ψ(f) commutative, generated by |S| elements" is proved. Whether f/(F_j : j∉S) is exactly the polynomial ring on S is not needed and not claimed.
