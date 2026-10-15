# PROVE 240: n = +1 or n = −1? Both are right, at different parameter points.

Date 2026-10-15. Grade: **proved** (hand proofs below, read against the printed sources; computed confirmation in §4).

## Problem
Wake 240 computed (Y): Y^H_i = θ^{N−1}(Y^DFK_{i,−1})^{-1} for all i, at the *same* (q, θ), with t = θ². The long version
(rem:subset-DFK l.189, rem:N-DFK l.631) says E_k = t^{k(m−k)}M_{k;1} (twist n = +1), and l.189 says a symbol-by-symbol
comparison "would be with (Y_{i,1})^{-1}". Are these consistent? Which sentence is wrong?

**Answer.** (Y) is true (proof in §1). rem:N-DFK is true: it is a coefficient-by-coefficient comparison of two explicit
symmetric operators (§2). They are consistent because rem:N-DFK uses the dictionary (q,t)_DFK = (s, t^{-1}), while (Y)
holds at (q,t)_DFK = (s^{-1}, t) = Hikita's own (q,t). The two are linked by the elementary inversion identity (I) (§3),
which sends k ↦ N−k and n ↦ −n. Only one clause is wrong: l.189's "symbol-by-symbol comparison would be with (Y_{i,1})^{-1}".
The symbol-by-symbol match is with θ^{m−1}(Y_{i,−1})^{-1}, and no operator-level n=+1 match exists at the inverted
parameters (computed, T6). Bonus: (Y) + DFK Thm 2.17 gives a 3-line second proof of thm:subset, with the right scalar t^{C(k,2)}.

Conventions. DFK = arXiv 1704.00154 (deformDAHA.tex §"functional representation"; (1.2), (1.5); Def. of Y_{i,n}; Lemma commuYin;
Thm genmacthm). Hikita = arXiv 2503.23597 eqs (1)–(3). Long version: a_ij = (x_i − t x_j)/(x_i − x_j), c_A = ∏_{i∈A, j∉A} a_ij,
E_kF = Σ_A c_A x_A F|_{x_i ↦ s x_i (i∈A)}, s = q_H^{-1} (longversion l.523). Operators compose right-to-left. T_j, π below are DFK's ρ(T_j), ρ(π).

## 1. Theorem (Y). On Laurent polynomials, Y^H_i = θ^{N−1} (Y_{i,−1})^{-1} for 1 ≤ i ≤ N (same q, t = θ²).

*Dictionary.* θ·ρ(T_j) = θ²s_j + (θ²−1)(s_j − 1)/(x_j/x_{j+1} − 1) = t s_j + (t−1)(1 − s_j)/(1 − x_j/x_{j+1}) = T^H_j (Hikita (1)).
So (T^H_j)^{-1} = θ^{-1}T_j^{-1}. Also Π = x_1 π (Hikita (2) vs DFK ρ(π): both substitute (x_2,…,x_N, q^{-1}x_1)).
Hence Y^H_i = t^{N−i}θ^{i−1}θ^{−(N−i)} T_{i−1}⋯T_1 x_1 π T_{N−1}^{-1}⋯T_i^{-1} = θ^{N−1} T_{i−1}⋯T_1 x_1 π T_{N−1}^{-1}⋯T_i^{-1}.

*DFK side.* Y_i = T_i⋯T_{N−1}π^{-1}T_1^{-1}⋯T_{i−1}^{-1}, so Y_i^{-1} = T_{i−1}⋯T_1 π T_{N−1}^{-1}⋯T_i^{-1}, and
(Y_{i,−1})^{-1} = [(x_1⋯x_{i−1}) Y_i (x_1⋯x_i)^{-1}]^{-1} = (x_1⋯x_i) Y_i^{-1} (x_1⋯x_{i−1})^{-1}.

*Two commutations.* (i) Multiplication by g commutes with T_j whenever g is symmetric in x_j, x_{j+1}, because T_j is a
combination of s_j and 1 with coefficients that are functions. (ii) π∘g = (πg)∘π, where π is a ring endomorphism.
- x_1⋯x_{i−1} is symmetric in x_j, x_{j+1} for j ≥ i, so it passes T_{N−1}^{-1}⋯T_i^{-1}. Then π(x_1⋯x_{i−1})^{-1} = (x_2⋯x_i)^{-1}π.
- x_1⋯x_i is symmetric in x_j, x_{j+1} for j ≤ i−1, so it passes T_{i−1}⋯T_1.

Therefore (Y_{i,−1})^{-1} = (x_1⋯x_i) T_{i−1}⋯T_1 (x_2⋯x_i)^{-1} π T_{N−1}^{-1}⋯T_i^{-1}
= T_{i−1}⋯T_1 (x_1⋯x_i)(x_2⋯x_i)^{-1} π T_{N−1}^{-1}⋯T_i^{-1} = T_{i−1}⋯T_1 x_1 π T_{N−1}^{-1}⋯T_i^{-1} = θ^{1−N}Y^H_i. ∎

Why only n = −1: for general n the same moves give Y^H_i Y_{i,n} = θ^{N−1}·T_{i−1}⋯T_1 x_1(x_2⋯x_i)^{-n} T_1^{-1}⋯T_{i−1}^{-1}·(x_1⋯x_i)^n.
This is a multiplication operator iff x_1(x_2⋯x_i)^{-n} is symmetric in x_1..x_i. For i ≥ 2 that forces n = −1.
For i = 1 there is no conjugation, which explains Clio's identity for all n. (This is the Wake 240 sketch, now cold-checked.
The direct proof above does not need it.)

## 2. rem:N-DFK's E_k = t^{k(m−k)} M_{k;1} at (q,t)_DFK = (s, t^{-1}) is correct, by inspection
DFK (1.5): M_{k;1} = Σ_I x_I ∏_{i∈I, j∉I}(t_D x_i − x_j)/(x_i − x_j) Γ_I, where Γ_i: x_i ↦ q_D x_i (1.2).
Put t_D = t^{-1} and q_D = s. Then (t^{-1}x_i − x_j)/(x_i − x_j) = t^{-1} a_ij, so M_{k;1} = t^{-k(m−k)} Σ c_I x_I Γ_I^{(s)} = t^{-k(m−k)}E_k. ✓
Also D_{k;1} ∝ τ_+(D_k) (DFK Lemma dalga + Lemma taupluslemma), so the τ_+ sentence of rem:N-DFK stands. Nothing in rem:N-DFK
uses Hikita's nonsymmetric Y_i, so (Y) cannot contradict it.

## 3. The bridge: inversion identity (I)
**(I)** On symmetric Laurent polynomials in N variables, for any (q,t):
  M_{N;−1}^{-1} M_{N−k;−1} |_{(q,t)} = q^{-k} t^{k(N−k)} M_{k;1} |_{(q^{-1}, t^{-1})} = q^{-k} E_k |_{s = q^{-1}}.

*Proof.* M_{N;−1}F = e_N^{-1} F(qx), so M_{N;−1}^{-1}G = q^{-N} e_N G(q^{-1}x). Write I = [N] ∖ J with |J| = N−k. In M_{N−k;−1},
(t x_j − x_i)/(x_j − x_i) = a_ij for j ∈ J, i ∈ I, so the coefficient is x_J^{-1}c_I, which is homogeneous of degree −(N−k) in x.
Evaluating at q^{-1}x gives q^{N−k}x_J^{-1}c_I, and F(Γ_J·) at q^{-1}x is F with x_I ↦ q^{-1}x_I. Hence
M_{N;−1}^{-1}M_{N−k;−1}F = q^{-N}q^{N−k} Σ_I e_N x_J^{-1} c_I F|_{x_I ↦ q^{-1}x_I} = q^{-k} Σ_I c_I x_I F|_{x_I↦q^{-1}x_I}. The second equality is §2 with s = q^{-1}. ∎

**Corollary (second proof of thm:subset).** On Λ_N, with q = q_H = s^{-1}:
e_k(Y^H) = θ^{k(N−1)} e_k(Y_{·,−1}^{-1})   [by (Y)]
 = θ^{k(N−1)} e_{N−k}(Y_{·,−1}) e_N(Y_{·,−1})^{-1}   [the Y_{i,−1} commute and are invertible: DFK Lemma commuYin]
 = θ^{k(N−1)} q^{-(N−k)}q^{N} 𝒟_{N−k;−1}𝒟_{N;−1}^{-1}   [DFK Def: D_{α;n} = q^{-αn}e_α(Y_{·,n}); D_{N;−1} restricts to the invertible e_N^{-1}Γ_{[N]}]
 = θ^{k(N−1)} q^{k} θ^{-k(N−k)} M_{N−k;−1}M_{N;−1}^{-1}   [DFK Thm genmacthm: 𝒟_{α;n} = θ^{-α(N−α)}M_{α;n}]
 = θ^{k(N−1)−k(N−k)} E_k = t^{C(k,2)} E_k   [(I)].
That is exactly thm:subset (e_k ⋆ F = t^{-C(k,2)}e_k(Y)F = E_kF), scalar included.

So: Hikita's Y = DFK's n = −1 family (inverted, θ-rescaled) at the same parameters. On symmetric functions, inverting
the family turns e_k into e_{N−k}/e_N, and (I) turns that into the n = +1 operator at inverted parameters. That is the
"duality" (b) asked for: (q, t, k, n) ↦ (q^{-1}, t^{-1}, N−k, −n), in the elementary form (I). It lives on symmetric
functions only (T6 below: no operator-level n=+1 match at inverted parameters).

## 4. Verification (computed; script work-in-progress/scripts/day240/prove240_check.py, output .out)
Operators come from the printed formulas: Hikita (1)–(3); DFK ρ, Y_{i,n}, (1.2), (1.5). Tests on monomial symmetric functions, N=2,3 (deg ≤ 3) and N=4 (deg ≤ 2), all k:
- T2 thm:subset via Hikita's operators, s = q^{-1}; T3 printed rem:N-DFK E_k = t^{k(m−k)}M_{k;1} at (s, t^{-1});
- T3' DFK's own operators at (q,θ)_D = (s, θ^{-1}): s^{-k}e_k(Y_{·,1}) = θ_D^{-k(N−k)}M_{k;1}. This checks that the printed chain (1.5) ↔ Y_{i,n} is self-consistent;
- T4 bridge (I) at free (Q,T); controls: invert only q, invert only t, drop k ↔ N−k (all must break);
- T5 the composite e_k(Y^H) = t^{C(k,2)+k(N−k)}M_{k;1}|_{(q^{-1},t^{-1})};
- T6 operator-level search: is Y^H_i ∘ (Y_{j,1})^{±1}|_{(q^{-1},θ^{-1})} a multiplication operator for any i, j?
### 4a. Results (prove240_check.out, prove240_T3p_fix.out)
- T2, T3, T4 (bridge (I)), T5: **bad = 0** for every N ∈ {2,3,4} and every k.
- T3' (rerun in prove240_T3p_fix.py, substituting once at the end): bad = 0 for all N, k. The first run substituted
  θ→θ^{-1} after each factor, which re-inverted the earlier factors. That was a script bug and it failed for k ≥ 2. Its control (θ not inverted) breaks for k < N.
- Controls for (I): invert only t → breaks for all k. Drop k ↔ N−k → breaks wherever defined. Invert only q → breaks for k < N.
  It passes at k = N, where (I) has an empty t-product, so this control is **vacuous at k = N** and not a real pass.
- T6: **no hit**. For no i, j is Y^H_i ∘ (Y^DFK_{j,1})^{±1}|_{(q^{-1},θ^{-1})} a multiplication operator (N = 2,3,4, monomials of deg ≤ 2).
  So no n = +1 operator-level match exists, even at the inverted dictionary.

## 5. What changes in the long version
Only the l.189 clause. Replacement text (applied in WIP bf85c76; 38 pp, 0 overfull; printed clause re-read from the PDF text): the symbol-by-symbol match is
Y_i = t^{(m−1)/2}(Y_{i,−1})^{-1} at DFK's (q,t) = (s^{-1}, t), with n = −1 rather than n = 1. The n = 1 form of the
first paragraph arises on symmetric functions after (q,t) ↦ (q^{-1},t^{-1}), via (I). rem:N-DFK, Rem 6.4's t^{-C(k,2)}
bookkeeping, and the intro l.64 are unaffected.
Clio: response PDF be17f3e accepted "(Y_{i,1})^{-1}". That is the clause now corrected, so a correction is owed (draft in for-collaborator/, unsent).
