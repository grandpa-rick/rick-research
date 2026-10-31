# Q55 — the seam is the Boolean locus of (W^J, Bruhat) for LG(m,2m); and P^{J,q} = 1 exactly there

PROVE 268, written 2026-10-31. Bounded jewel: proofs/ and registry only. The draft (9be3ae3), the FPSAC cut (6dbecb8)
and the 11-04 note (39c11e7) are untouched.
Scripts are in `proofs/prove268/` (`q55.py`, `q55_general.py`, `q55_support.py`, with `.out` files next to them).

**Verdict.**
- (a) Bruhat order on W^J is inclusion of shifted diagrams. PROVED in-house (Prop B below), from (T)+(Z) of Q53. The owner
  locator is only second-hand: Proctor's thesis Prop V.2, as cited by Miura Prop 2.3, for *minuscule* W^P. LG is cominuscule,
  but W(C_m) = W(B_m) with the same J, so its W^J is the W^J of the minuscule spinor variety OG(m,2m+1). So the locator grade
  stays `sketched`. Nothing below stands on it.
- (b) is the standard J(I∖I') fact. PROVED.
- (c) PROVED, in three equivalent Bruhat forms: dn = z_λ ⇔ [z_λ,z_ρ] in W^J is Boolean ⇔ [z_λ,z_ρ]_W ⊆ W^J. **Orientation
  fix:** the interval is [z_λ, z_ρ], not [z_ρ, z_λ], because ρ ⊆ λ ⇔ z_λ ≤ z_ρ.
- (d), first part. **YES**, non-Boolean pairs enter (3.6). This is proved, not just computed. The (3.6) support is
  "θ has no 3-chain and every non-minimal box of θ is off-diagonal". The Boolean pairs are exactly the pairs that carry the
  straight-path term. The counts of non-Boolean pairs in the support are 0, 1, 5, 20, 70, 229, 719, 2196 for m = 1..8.
- (d), second part. In the **q-convention** (Deodhar's u = q, written as the alternating sum Σ_{u∈W_J}(−1)^{ℓ(u)}P_{σu,τ}),
  **P^{J,q}_{σ,τ} = 1 iff [σ,τ] is Boolean**. This is PROVED. The general-Coxeter half is P^{J,q}_{σ,τ}(0) = [dn(τ,σW_J)=σ].
  The type-C half is that R = (q−1)^d on antichain intervals. In the **geometric convention** (u = −1, P_{σw_J,τw_J}, the IC
  of Schubert varieties in LG), P^{J,−1} = 1 on strictly MORE pairs. It also misses some (3.6) pairs and catches some
  non-(3.6) pairs, so it is not the seam (computed, m ≤ 5).

So the seam has an algebraic name: **Boolean ⇔ dn fixes the coset minimum ⇔ the full Bruhat interval stays inside W^J ⇔
P^{J,q} = 1 ⇔ the (3.6) sum has a straight-path term.** Rule 11 reminder, honoured: the reason P^{J,q} is 1 is not
"Boolean lattices have trivial KL polynomials" (in full W, Boolean intervals over-detect: see the control in §5). The reason
is that the interval never leaves W^J, so the alternating sum collapses to one ordinary P, and that P is 1 because R
telescopes.

---

## 0. Conventions (as in Q53)

`(W,S)` is a Coxeter group, `J ⊆ S`, and `W^J` is the set of minimal left-coset representatives. `W_J` is the parabolic
subgroup. Standard facts used:
- **(LA)** [BB05 Prop 2.4.4] For σ ∈ W^J and u ∈ W_J, ℓ(σu) = ℓ(σ)+ℓ(u).
- **(SW)** [BB05 Thm 2.2.2] Subword property.
- **(Z)** [BB05 Prop 2.2.7 + corollary] Lifting property, left and right forms. If sw < w, then: if sv > v, v ≤ w ⇔ v ≤ sw;
  if sv < v, v ≤ w ⇔ sv ≤ sw. In right form: if v < w, ws < w and vs > v, then vs ≤ w.
- **(EU)** [BB05 Cor 2.7.10, Verma] Bruhat intervals are Eulerian: Σ_{x∈[u,w]} (−1)^{ℓ(x)} = 0 for u < w.
- **(KL)** [BB05 Ch. 5; KL79] P_{x,x} = 1, P_{x,y} = 0 unless x ≤ y, P_{x,y}(0) = 1 for x ≤ y, deg P_{x,y} ≤ (ℓ(y)−ℓ(x)−1)/2.
  The inversion formula is q^{ℓ(y)−ℓ(x)} P_{x,y}(q^{−1}) = Σ_{x≤z≤y} R_{x,z} P_{z,y}. The R-recursion (left form, obtained
  from BB05 Thm 5.1.1 by w ↦ w^{−1}): if sy < y, then R_{x,y} = R_{sx,sy} when sx < x, and
  R_{x,y} = (q−1)R_{x,sy} + qR_{sx,sy} when sx > x.
  (BB05 locators are from memory; no browsing this session. All are textbook-standard.)
- **(DE)** [Deodhar 1977, Invent. Math. 39; locator from memory, machine-checked in Q53 `check.py` for 8 groups, all J] For σ ≤ w the set C(w,σ) has a Bruhat-maximum.
- dn(w, σW_J) is the Bruhat-max of C(w,σ) = {u ∈ σW_J : u ≤ w} (Deodhar). E(σ,w) = {s ∈ J : σs ≤ w}.
  **Q53 Prop 1:** for σ ∈ W^J with σ ≤ w, dn = σ ⇔ C = {σ} ⇔ E = ∅.

Type C_m: the reflection s_c (c < m) swaps coordinates c, c+1, s_m negates coordinate m, J = S∖{s_m}, ω = (1,…,1). Shapes
η are strict partitions with parts ≤ m. D(η) = {(a,b) : 0 ≤ a ≤ b ≤ a+η_a−1} sits inside the staircase
T = {0 ≤ a ≤ b ≤ m−1}, which carries the product order. w_η ∈ W^J has w_η ω = v_η (−1 exactly at positions m+1−k, k ∈ η).
The colour of box (a,a+d) is c = m−d. From Q53 we use (O) (shapes = order ideals of T; removable = maximal; addable = all
lower covers present) and the trichotomy (T): for each η and c, exactly one of (i) s_c w_η = w_{η+b}, b addable of colour c;
(ii) s_c w_η = w_{η−b}, b removable of colour c; (iii) s_c w_η = w_η s_j, j ≠ m. Also z_κ = w_{κ^∨}, and
D(κ^∨) = rot(T ∖ D(κ)), where rot is an order-reversing involution of T (Q53 Lemma 3).

## 1. Length (closing the one lem:bonds import of Q53 (T))

**Lemma L.** ℓ(w_η) = |η|.
*Proof.* For a minimal representative w ∈ W^J with W_J = Stab(ω), ℓ(w) = #{α > 0 : ⟨wω, α^∨⟩ < 0}. Indeed ℓ(w) counts
α > 0 with w^{−1}α < 0. Minimality means w(Φ_J^+) ⊆ Φ^+, so such w^{−1}α lies in Φ^−∖Φ_J and pairs strictly negatively with
ω. Conversely, ⟨w^{−1}α, ω⟩ < 0 forces w^{−1}α < 0. The positive roots of C_m are e_i − e_j and e_i + e_j (i < j) and 2e_i.
Let μ = v_η ∈ {±1}^m with N = ℓ(η) minus-signs. Then 2e_i contributes N, e_i+e_j contributes C(N,2), and e_i−e_j contributes
#{i<j : μ_i = −, μ_j = +}. The minus at position p = m+1−k (k ∈ η) sees the plus positions j > p, which are the
k' < k with k' ∉ η. There are (k−1) − #{k' ∈ η : k' < k} of them. Summing over k gives Σ(k−1) − C(N,2). In total
ℓ = N + C(N,2) + Σ_k (k−1) − C(N,2) = Σ_k k = |η|. ∎

(This is used inside (T)(i): "the coset of η+b has minimal length |η|+1".)

## 2. (a) Bruhat order on W^J is inclusion

**Prop B.** w_η ≤ w_ν ⇔ D(η) ⊆ D(ν).
*Proof.* (⇐) By (O), D(ν) is obtained from D(η) by adding addable boxes one at a time: take a minimal element of
D(ν)∖D(ι) for the current ideal ι. Each step is w_{ι+b} = s_c w_ι, of length one more, by (T)(i) and Lemma L. Hence
w_ι < w_{ι+b}.
(⇒) Induct on |ν|. If ν = ∅, then w_ν = e, so w_η = e and η = ∅. Otherwise pick b removable in ν, of colour c, and set
s = s_c, so s w_ν = w_{ν−b} < w_ν by (T)(ii). Let u = w_η ≤ w_ν.
- If su > u, then (Z) gives u ≤ w_{ν−b}, and induction gives D(η) ⊆ D(ν−b) ⊆ D(ν).
- If su < u, then (T) for η and c cannot be (iii), since there su = w_η s_j has length |η|+1, and it cannot be (i). So it
  is (ii): su = w_{η−b'}, with b' removable in η of colour c, i.e. on the same diagonal d as b. (Z) gives
  w_{η−b'} ≤ w_{ν−b}, and induction gives D(η−b') ⊆ D(ν−b). On each diagonal a shape is an initial segment (Q53 (O)).
  b' is the k-th box of diagonal d, so η−b' has k−1 boxes there. Then ν−b has ≥ k−1 boxes and ν has ≥ k, so b' ∈ D(ν).
  Hence D(η) = D(η−b') ∪ {b'} ⊆ D(ν). ∎

So (W^J, ≤) ≅ (J(T), ⊆) via w_η ↦ D(η), and via z_κ ↦ D(κ) it is ≅ (J(T), ⊇) by rot. (Q53's `checkC.py` machine-checks
this for m ≤ 5.)
*Owner.* This is folklore for minuscule W^P (Proctor). The only locator I hold is second-hand: Proctor's thesis 1981,
Prop V.2, via Miura Prop 2.3 (`reading/2026-10-22-order-polynomial-roots.md`). Reduction to minuscule: Bruhat order on
W^J depends only on (W,J), and (C_m, J) and (B_m, J) have the same Coxeter system and J. For B_m, ω_m is minuscule
(OG(m,2m+1)). The locator is not upgraded this session (no browsing).

## 3. (b) Intervals of J(P)

**Lemma I.** Let P be a finite poset and I' ⊆ I ideals. Then [I',I] ≅ J(I∖I'), via K ↦ K∖I'. And [I',I] is Boolean (≅ 2^n
for some n) iff I∖I' is an antichain.
*Proof.* Put Q = I∖I'. If K ∈ [I',I], then K∖I' is down-closed in Q (it is the intersection of an ideal of P with Q).
Conversely, let L ⊆ Q be down-closed and x ∈ I' ∪ L, y ≤ x. If x ∈ I', then y ∈ I'. If x ∈ L, then y ∈ I, so y ∈ I' or
y ∈ Q. In the latter case y ∈ L. So I' ∪ L is an ideal. The two maps are inverse and monotone.
For the Boolean claim: J(Q) is graded of rank |Q|, by adding one element at a time. If J(Q) ≅ 2^n, then n = rank = |Q| and
|J(Q)| = 2^{|Q|}, so every subset of Q is down-closed, i.e. Q is an antichain. Conversely, an antichain has J(Q) = 2^Q. ∎

**Corollary.** For η ⊆ ν: [w_η, w_ν]_{W^J} ≅ J(ν/η) (Prop B + Lemma I), and it is Boolean iff ν/η is an antichain.
For ρ ⊆ λ: [z_λ, z_ρ]_{W^J} = [w_{λ^∨}, w_{ρ^∨}] ≅ J(ρ^∨/λ^∨) = J(rot(λ/ρ)) ≅ J(λ/ρ)^{op}. It is Boolean iff λ/ρ is an
antichain (2^n is self-dual). So the antichain pairs of Q54 are the Boolean intervals of (W^J, ≤), and
A_m(t) = Σ_{Boolean intervals [x,y] of W^J} t^{ℓ(y)−ℓ(x)} = Σ_r C(m+1,2r)(1+t)^r.

## 4. (c) The dn criterion in Bruhat language

**Lemma G1 (any Coxeter group).** For σ ≤ τ in W^J: dn(τ, σW_J) = σ ⇔ [σ,τ]_W ⊆ W^J.
*Proof.* (⇐) σs ∈ σW_J is not in W^J, so σs ∉ [σ,τ]. Since σ ≤ σs (LA+SW), this means σs ≰ τ, so E = ∅ and Q53 Prop 1
applies. (⇒) Suppose x ∈ [σ,τ], x ∉ W^J, so xs < x for some s ∈ J. Then x ≠ σ, so σ < x, and σs > σ. Right-form (Z) gives
σs ≤ x ≤ τ, so s ∈ E. This contradicts Prop 1. ∎

**Theorem C (Q55(c)).** For shapes ρ ⊆ λ in LG(m,2m) the following are equivalent:
1. dn(z_ρ, z_λ W_J) = z_λ;
2. z_λ s ≰ z_ρ for every s ∈ J;
3. the interval [z_λ, z_ρ] of (W^J, ≤) is Boolean;
4. the full Bruhat interval [z_λ, z_ρ]_W lies inside W^J;
5. D(λ)∖D(ρ) is an antichain.
When these hold, [z_λ,z_ρ]_W = [z_λ,z_ρ]_{W^J} ≅ 2^{λ/ρ}.
*Proof.* 1⇔2 is Q53 Prop 1. 1⇔5 is Q53 Lemma A. 3⇔5 is the Corollary in §3. 1⇔4 is Lemma G1. ∎

*Warning, i.e. what is NOT equivalent:* "[z_λ, z_ρ]_W is Boolean" is strictly weaker. A 2-chain skew gives a 3-element chain
in W^J but a 4-element diamond in W, since every length-2 Bruhat interval of W is a diamond. Control in §6.

## 5. (d) KL polynomials

**Definition.** P^{J,q}_{σ,τ} := Σ_{u∈W_J} (−1)^{ℓ(u)} P_{σu,τ} for σ, τ ∈ W^J. Deodhar 1987 identifies this with his
parabolic KL polynomial for u = q (locator from memory: "On some geometric aspects of Bruhat orderings II", Prop 3.4).
I machine-checked that identification against the parabolic module recursion for type C, m ≤ 4 (0 disagreements). The
geometric polynomial is P^{J,−1}_{σ,τ} := P_{σw_J, τw_J}. It is also checked against the u = −1 recursion, m ≤ 4, with 0
disagreements. The statements below are about the alternating sum and do not depend on the identification.

**Lemma G2 (any Coxeter group).** For σ ∈ W^J and τ ≥ σ, let σu_0 = dn(τ, σW_J). (exists by (DE)). Then {u ∈ W_J : σu ≤ τ} = [e, u_0], the
Bruhat interval in W_J.
*Proof.* First, σu ≤ σu' ⇔ u ≤ u' for u, u' ∈ W_J. (⇐) holds by LA+SW. For (⇒), induct on ℓ(σ). If σ = sσ' with
ℓ(σ') = ℓ(σ)−1, then σ' ∈ W^J, because a reduced word of σ' ending in t ∈ J would give one of σ. By LA, s is a left
descent of both σu and σu', so (Z) gives σ'u ≤ σ'u', and induction finishes. Now u ∈ C ⇒ σu ≤ σu_0 (maximality) ⇒
u ≤ u_0. Conversely, u ≤ u_0 ⇒ σu ≤ σu_0 ≤ τ. ∎

**Theorem K0 (any Coxeter group).** For σ ≤ τ in W^J: P^{J,q}_{σ,τ}(0) = 1 if dn(τ,σW_J) = σ, and 0 otherwise. If
dn = σ, then P^{J,q}_{σ,τ} = P_{σ,τ}.
*Proof.* P_{x,τ}(0) = [x ≤ τ] (KL), so P^{J,q}(0) = Σ_{u∈[e,u_0]} (−1)^{ℓ(u)} by G2. This is 1 if u_0 = e and 0 by (EU)
otherwise. If dn = σ, then C = {σ} (Prop 1), so only u = e survives in the alternating sum. ∎

**Lemma R (type C).** If η ⊆ ν and ν/η is an antichain, then R_{w_η,w_ν} = (q−1)^{|ν/η|}.
*Proof.* Induct on |ν/η|. The case 0 is R_{x,x} = 1. Otherwise pick b ∈ ν/η. b is removable in ν: a box b' > b of ν
would lie in η (antichain), forcing b ∈ η. b is addable to η: every box below b lies in ν but not in ν/η, hence in η.
With s = s_c (colour of b), (T) gives s w_ν = w_{ν−b} < w_ν and s w_η = w_{η+b} > w_η. The R-recursion gives
R_{w_η,w_ν} = (q−1) R_{w_η, w_{ν−b}} + q R_{w_{η+b}, w_{ν−b}}. The second term is 0 because D(η+b) ⊄ D(ν−b) (Prop B). The
skew (ν−b)/η = ν/η ∖ {b} is an antichain. ∎

**Theorem K (Q55(d), type C).** For shapes η ⊆ ν: P^{J,q}_{w_η,w_ν} = 1 ⇔ ν/η is an antichain ⇔ [w_η,w_ν]_{W^J} is
Boolean. (Equivalently, via z_κ = w_{κ^∨}: P^{J,q}_{z_λ,z_ρ} = 1 ⇔ λ/ρ is an antichain.) On antichain pairs also
P_{w_η,w_ν} = 1 in full W.
*Proof.* (⇐) Let ν/η be an antichain. By Theorem C(4) and Prop B, [w_η,w_ν]_W = {w_μ : η ⊆ μ ⊆ ν}, and every
subinterval [w_μ, w_ν] is again of antichain type. Induct on d = |ν/η| to show P_{w_η,w_ν} = 1. By induction
P_{w_μ,w_ν} = 1 for μ ≠ η. Combined with Lemma R, the inversion formula gives
q^d P(q^{−1}) − P = Σ_{μ≠η} (q−1)^{|μ/η|} = q^d − 1, where P = P_{w_η,w_ν}. So Q = P − 1 satisfies q^d Q(q^{−1}) = Q. Since
deg Q ≤ (d−1)/2 < d − (d−1)/2, we get Q = 0. Then K0 gives P^{J,q} = P = 1.
(⇒) If ν/η is not an antichain, then dn ≠ w_η (Q53 Lemma A/Prop 2), so P^{J,q}(0) = 0 by K0 and P^{J,q} ≠ 1. ∎

**(d), first part. Proposition S.** A pair ρ ⊆ κ has D_{z_ρ,z_κ} ≠ ∅ in Rem 4.22, i.e. it enters the (3.6) sum, iff
θ = κ/ρ has no 3-chain and every non-minimal box of θ is off-diagonal. Among these pairs, the Boolean ones are exactly
those with a straight-path term.
*Proof.* By printed Rem 4.22, D ≠ ∅ iff θ = A ⊔ B with ρ ∪ A an ideal, A and B antichains, and B free of diagonal boxes.
(A is empty for the straight path.) If x ∈ θ is non-minimal, say y < x in θ, then x ∉ A (else y ∈ A, and A would not be an
antichain), so x ∈ B. Hence non-minimal boxes are off-diagonal, and a 3-chain x < y < z would put y, z ∈ B. Conversely,
take A = min θ, which is down-closed in θ, and B = θ ∖ min θ, which is an antichain without diagonal boxes. The straight
term is A = θ, B = ∅, which needs θ to be an antichain, i.e. Boolean. ∎
Example m = 2: ρ = ∅, κ = (2), θ = {(0,0) < (0,1)}. Here A = {(0,0)} and B = {(0,1)} is off-diagonal, so the pair enters
(3.6) while [z_κ, z_ρ]_{W^J} is a 3-chain. So **yes**, non-Boolean intervals enter (3.6). The seam is where the straight
path lives, not the whole support.

## 6. Verification (machine; from the stated claims)

`q55.py` (type C_m, m ≤ 5; Bruhat order by reflection closure; Boolean test = atoms-to-subsets order isomorphism;
parabolic KL by Deodhar's R-recursion for u ∈ {−1, q}, independent of the alternating-sum definition):

| m | pairs | antichain ⇔ Bool_{W^J} fails | Bool_W but not antichain (control) | non-Bool in (3.6) | P^{J,q}=1 ⇔ antichain fails | P^{J,−1}=1 & non-antichain | antichain & P^{J,−1}≠1 |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 10 | 0 | 2 | 1 | 0 | 3 | 0 |
| 3 | 35 | 0 | 9 | 5 | 0 | 15 | 0 |
| 4 | 126 | 0 | 33 | 20 | 0 | 58 | 0 |
| 5 | 462 | 0 | 111 | 70 | 0 | 202 | 0 |

(The u = −1 column is z-indexed. In both indexings P^{J,−1} = 1 on all antichain pairs plus many more, and the extra set
straddles the (3.6) support: (3.6) pairs with P^{J,−1} ≠ 1 occur from m = 3 on (1 at m=3, 4 at m=4, 15 at m=5). See `q55.out`.)
For m ≤ 4, cross-check against full-group KL: u = −1 recursion = P_{σw_J,τw_J} and u = q recursion = alternating sum, with
0 disagreements.

`q55_general.py` checks G1, G2, K0 (constant term) and "dn = σ ⇒ P^{J,q} = P" for every J and every σ ≤ τ in W^J, in
A3 (448 triples), B3 (1708), A4 (9862) and C4 (99592), with 0 failures. Control: replacing "dn = σ" by "full W interval
is Boolean" disagrees on 95 / 538 / 3111 / 40088 triples.

`q55_support.py` checks Proposition S for m ≤ 8 with 0 failures. Non-Boolean (3.6) pairs: 0, 1, 5, 20, 70, 229, 719, 2196.

## 7. Gaps

- None in the logic. Premises are textbook (BB05 2.2.2, 2.2.7, 2.4.4, 2.7.10, Ch. 5; Deodhar's (DE); all with locators from memory) plus
  Q53 (proved) and, for Prop S only, the printed description of D_{z_ρ,z_κ} in Rem 4.22 (Q48, proved).
- Not first-hand: (i) the Proctor locator for (a), which is superseded by Prop B and is only an ownership credit;
  (ii) the identification of the alternating sum with Deodhar's u = q polynomial (machine-checked m ≤ 4, Deodhar 1987
  Prop 3.4 from memory). Theorem K is stated for the alternating sum and is unconditional in that form.
- Ownership: K0 is presumably folklore in the parabolic KL literature (Deodhar/Brenti; Boe 1988 computed the Hermitian
  symmetric P^J). No novelty is claimed. This is a proofs/ shelf jewel, post-FPSAC material.
