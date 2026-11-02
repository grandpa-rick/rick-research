# Q60 — when is Baumann's HN factorisation Φ_θ local for ẽ_j?  (PROVE 272, 2026-11-02/03)

Scripts: `proofs/prove272/`. Registry: `seedQ1-polite.json`. Conventions are those of §6 and the audit in
`proofs/2026-11-02-seedQ1-polite-bases-expository.md`: degrees in Q_+, b_+ sits in the θ-top bidegree,
ẽ_j is the left Kashiwara operator of the perfect basis B. In type A, e_j f(n) = d/dt f(n·exp tE_{j,j+1}),
i.e. e_1 = ∂_x and e_2 = ∂_y + x∂_z in A_2, exactly as in `seedQ1/a2_polite_factorisation.py`.

## Statement

G simply laced, B the polite basis of O(N) (dual canonical at q=1), θ generic, S = {θ>0}, T = Δ_+∖S, j ∈ I.
Three mutually exclusive cases:
- **neg:** α_j ∈ T.
- **adj:** α_j ∈ S and T∪{α_j} is biconvex (⟺ x^{-1}α_j is simple, where T = N(x^{-1})).
- **far:** otherwise (⟺ ∃ α ∈ T with α+α_j ∈ S).

In type A_n, write θ(ε_a − ε_b) = g(a) − g(b) with g injective. Then:
- neg ⟺ g(j) < g(j+1);
- adj ⟺ g(j) > g(j+1) and no g(k) lies strictly between them;
- far ⟺ ∃ k ∉ {j, j+1} with g(j+1) < g(k) < g(j).

**Theorem Q60.**
- **(a) neg ⇒** for all b with ẽ_j b ≠ 0: Φ_θ(ẽ_j b) = (b_+, ẽ_j b_−).
- **(b) adj ⇒** for all b with ẽ_j b ≠ 0, Φ_θ(ẽ_j b) is (ẽ_j b_+, b_−) if ε_j(b_+) > φ_j(b_−), and (b_+, ẽ_j b_−) otherwise.
  Here φ_j(c) = ε_j(c) + ⟨h_j, wt c⟩ with wt ∈ −Q_+. This is Kashiwara's tensor rule on b_− ⊗ (α_j-string of length ε_j(b_+)).
- **(c) far ⇒** some b ∈ B_S has ẽ_j b ≠ 0 and **both** coordinates of Φ_θ change. Locality therefore fails even in the weak form.

Hence Φ_θ is ẽ_j-local ⟺ not far. Strong and weak locality coincide.

**Grades.**
- (c) is **proved in type A** from first-hand sources only.
- (a) and (b) are **sketched**: the argument is complete but depends on the identification P0 below and on three textbook crystal facts cited from memory.
- (a), (b) and (c) are **computed** in A_2, A_3 and A_4: 12/12, 72/72 and 480/480 (θ, j) pairs. The exact (b) rule holds on 12672/12672 elements in A_4.

## P0. Φ_θ is the split of the Lusztig datum (sketched + computed)

Let T = N(x^{-1}), ℓ = ℓ(x), and let **i** be a reduced word of w_0 starting with a reduced word of x. Its first ℓ roots
β_k = s_{i_1}⋯s_{i_{k−1}}α_{i_k} are exactly T. Write the Lusztig datum as n = (n_T, n_S). Then

  Φ_θ(b(n)) = (b(0, n_S), b(n_T, 0))   [b_− = T-part, b_+ = S-part].

- **Source:** Tingley–Webster 1210.6921 Props 3.4 and 3.9 (cut factorisation along a convex order), together with Baumann 2401.10340 Ex 3.2 (dual canonical = polite). The orientation (T-part = b_−, T listed first) was not traced through the conventions.
- **Computed instead:** the Lusztig-data model (`lusztig.py`: Lusztig's PL map (a,b,c) ↦ (b+c−p, p, a+b−p) with p = min(a,c); ẽ_j decrements n_1 in a word with i_1 = j, Kamnitzer 0505398 Prop 3.4) with this split reproduces **every** A_2 count of the independent polynomial computation (`seedQ1/a2_polite_factorisation.out`): 22/22 in all local cases, 14/22 (b_+:14) in C3/j=1 and C5/j=2, and 14/8 in the adj cases.
- **Word independence:** the split does not depend on the choice of T-first word. 0 failures over all T-first words, A_2–A_4 (`q60_checks.py`).

## (a) proof (given P0)

α_j ∈ T = N(x^{-1}) ⟺ x^{-1}α_j < 0 ⟺ ℓ(s_j x) < ℓ(x), so x has a reduced word starting with j. Take **i** = (j, …) with T first.
By Kamnitzer 0505398 Prop 3.4(ii) [first-hand], ẽ_j sends (n_1, n_2, …) to (n_1 − 1, n_2, …), and ẽ_j b ≠ 0 ⟺ n_1 ≥ 1. The coordinate n_1 sits on β_1 = α_j ∈ T, so n_S is unchanged.
Apply the same Prop to b_− = b(n_T, 0), which has the same n_1: ẽ_j b_− = b(n_T − δ_1, 0). Hence Φ_θ(ẽ_j b) = (b_+, ẽ_j b_−). ∎

## (b) proof (given P0, B2, B3)

**Setup.** adj means T∪{α_j} is biconvex, hence an inversion set N(y^{-1}) ⊃ N(x^{-1}) with one extra root. So y = x s_i with xα_i = α_j and ℓ(y) = ℓ+1. [Biconvex = inversion set, and inclusion of inversion sets = weak order: textbook, mem.]
Put v := x s_i = s_j x, since x s_i x^{-1} = s_{xα_i} = s_j. Take **i** = (x-word, i, rest), with roots T, α_j, S' := S∖{α_j}. Write the datum as (n_T, m, n_{S'}). By P0, b_− = b(n_T, 0, 0) and b_+ = b(0, m, n_{S'}).

**B1 (prefix lemma; proved).** **i**' = (j, x-word, rest) is also a reduced word of w_0. Both (x-word, i) and (j, x-word) are reduced words of v, so by Matsumoto they are joined by braid moves inside the first ℓ+1 positions. Those PL transition maps fix the last N−ℓ−1 coordinates.
So in **i**' the datum is (R(n_T, m), n_{S'}) for a bijection R of N^{ℓ+1}. By Kamnitzer Prop 3.4, ẽ_j b = b(R^{-1}(R(n_T,m) − δ_1), n_{S'}). Two consequences:
- ẽ_j **never changes n_{S'}**, and the new prefix depends only on (n_T, m);
- B_v := {b : n_{S'} = 0} (= B ∩ U^+(v)) is stable under ẽ_j.

**B2 (star-string lemma; sketched + computed).** For c = b(n_T, m, 0) ∈ B_v: c = (f̃_j^*)^m b(n_T, 0, 0) and ε_j^*(b(n_T, 0, 0)) = 0. Hence ε_j^*(c) = m, and an element of B_v has ε_j^* = 0 iff m = 0.
- *Sketch:* the root vector for α_j in **i** is T_x(E_i) = E_j [Lusztig, mem], so the PBW monomial is E(n_T, m, 0) = E_T(n_T) E_j^{(m)}.
- Since (j, x-word) is reduced, T_j maps every root vector of x into U^+. Hence U^+(x) ⊂ U^+ ∩ T_j^{-1}U^+ = ker e_j'^* [Lusztig 38.1.2, mem; T vs T^{-1} convention unchecked].
- For u ∈ L(∞) ∩ ker e_j'^*: u E_j^{(m)} ≡ (f̃_j^*)^m u mod qL(∞) [Kashiwara, mem]. Apply this to u = E_T(n_T) and to the qL-correction term, which lies in U^+(x) ∩ qL.
- *Computed:* ε_j^*(b(n_T, m, 0)) = m in the model, where ε_k^* is the last coordinate in a word whose last root is α_k (`b_lemma.py`, see Verification).

**B3 (Kashiwara embedding; cited, mem).** Ψ_j^* : b ↦ (ẽ_j^*)^{ε_j^*(b)} b ⊗ b_j(−ε_j^*(b)) is a strict embedding B(∞) → B(∞) ⊗ B_j for all ẽ_k, with the tensor rule
ẽ(b_1 ⊗ b_2) = ẽb_1 ⊗ b_2 if φ(b_1) ≥ ε(b_2), and b_1 ⊗ ẽb_2 otherwise; here ε_j(b_j(−m)) = m.
- Sources: Kashiwara Duke 71 (1993) 839–858 [locator unverified]. First-hand secondary: TW 1210.6921, proof of Prop 1.4, citing [KS97, Prop 3.2.3].
- The tensor-rule orientation is fixed by the computation: 12672/12672.

**Conclusion.** Let c = b(n_T, m, 0). By B1, ẽ_j b = b(prefix of ẽ_j c, n_{S'}). By B2, Ψ_j^*(c) = b_− ⊗ b_j(−m).
- **If m > φ_j(b_−):** Ψ(ẽ_j c) = b_− ⊗ b_j(−m+1), so ẽ_j c = (f̃_j^*)^{m−1} b_− = b(n_T, m−1, 0) by B2. Hence ẽ_j b = b(n_T, m−1, n_{S'}).
  The same argument with n_T = 0 gives ẽ_j b_+ = b(0, m−1, n_{S'}), since φ_j(1) = 0 < m. So Φ(ẽ_j b) = (ẽ_j b_+, b_−).
- **If m ≤ φ_j(b_−):** Ψ(ẽ_j c) = ẽ_j b_− ⊗ b_j(−m), so ε_j^*(ẽ_j c) = m and ε_j^*(ẽ_j b_−) = 0.
  ẽ_j b_− ∈ B_v by B1, so B2 gives ẽ_j b_− = b(n'_T, 0, 0) ∈ B_T and ẽ_j c = b(n'_T, m, 0). Hence ẽ_j b = b(n'_T, m, n_{S'}) and Φ(ẽ_j b) = (b_+, ẽ_j b_−). ∎

Note: ε_j(b_+) = m (B1 with n_T = 0 and R(0, m) = (m, 0), because E_j^{(m)} is the same monomial in both words). So the rule is exactly the "reversed(b_− ⊗ b_+)" column that matched 34/34 in the A_2 adj chambers C4 and C6.

## (c) proof (type A; first-hand sources only)

**Ingredients.**
- (i) Flag minors Δ_{[1,p],J}|_N lie in every biperfect basis of C[N]: BKK 1905.08460 Rem 2.10 [first-hand]. Here Ψ_λ(v)(n) = v_λ^*(n v) with λ = ϖ_p.
- Polite ⇒ biperfect: Baumann Prop 3.12. So these minors lie in B.
- (ii) Perfect basis axiom: e_j b = ε_j(b) ẽ_j b + Σ_{ε_j(b′) < ε_j(b) − 1} c_{b′} b′ [BKK §2, first-hand]. Hence if e_j b ≠ 0 and e_j² b = 0, then ε_j(b) = 1 and ẽ_j b = e_j b.
- (iii) Cauchy–Binet: Δ(Δ_{I,J}) = Σ_K Δ_{I,K} ⊗ Δ_{K,J}. The first factor has degree ν_K = Σ_I ε − Σ_K ε ∈ Q_+, so θ(ν_K) = g(I) − g(K) (writing g(K) = Σ_{k∈K} g(k)).
  Δ_{I,K}|_N = 0 unless I ≤ K componentwise (zero block). Distinct K have distinct ν_K, so each bidegree component is a single term.
  Hence b_+ ∈ k·Δ_{I,K*} with K* = argmin g(K) over the support, and **b ∈ B_S ⟺ the support's g-minimiser is J**.
- (iv) e_j Δ_{I,J} = Δ_{I, J−(j+1)+j} if j+1 ∈ J and j ∉ J, and 0 otherwise. This is the column operation of right translation by exp tE_{j,j+1}.

**Weight lemma.** If b ∈ B_S, ẽ_j b ≠ 0 and ẽ_j b ∉ B_S, then both coordinates change.
Φ(b) = (b, 1). Φ(ẽ_j b) = (c_+, c_−) has c_− ≠ 1 because ẽ_j b ∉ B_S, and c_+ ≠ b because wt c_+ ≤ wt ẽ_j b < wt b. ∎

**Witness.** Assume far.

*Case R* (some k > j+1 with g(j+1) < g(k) < g(j)). Take the least such k, and let L = {r ∈ (j+1, k) : g(r) < g(j+1)}.
Every other r ∈ (j+1, k) has g(r) > g(j) (they are not far, by minimality of k). Set

  J = [1, j−1] ∪ {j+1} ∪ L ∪ {k},  p = |J|,  b = Δ_{[1,p], J}.

- *b ∈ B_S.* K ≤ J forces K ⊇ [1, j−1], and the remaining |L|+2 elements lie in [j, k]. Let U = {j, j+1} ∪ L ∪ {k}. Every element of [j, k] ∖ U has g > g(j) = max_U g.
  So any (|L|+2)-subset of [j, k] has g-sum ≥ g(U) − g(j), with equality only for U∖{j} = J ∩ [j, k]. J itself is in the support (Δ_{J,J} = 1). So K* = J.
- *ε_j(b) = 1.* j+1 ∈ J and j ∉ J, so ẽ_j b = e_j b = Δ_{[1,p], J'} with J' = [1, j−1] ∪ {j} ∪ L ∪ {k}, and e_j² b = 0. Δ_{[1,p], J'} ≠ 0 by BKK injectivity of Ψ_λ.
- *ẽ_j b ∉ B_S.* The competitor K_c = [1, j+1] ∪ L is ≤ J', and g(K_c) − g(J') = g(j+1) − g(k) < 0.
  Its term Δ_{[1,p],K_c} ⊗ Δ_{K_c,J'} is nonzero. The first factor is a flag minor (≠ 0). The second reduces, after the unitriangular block [1, j], to rows (j+1, l_1, …, l_s), columns (l_1, …, l_s, k). Evaluated at n_0 = 1 + E_{j+1,l_1} + E_{l_1,l_2} + ⋯ + E_{l_s,k}, it is a unit lower-triangular determinant, = 1.
  So the support's minimiser is not J'.

*Case L* (no such k > j+1). Let k = max{k < j : g(j+1) < g(k) < g(j)} and L = {r ∈ (k, j) : g(r) < g(j+1)}. The other r ∈ (k, j) have g > g(j). Set

  J = [1, k−1] ∪ L ∪ {j+1},  J' = [1, k−1] ∪ L ∪ {j},  K_c = [1, k] ∪ L.

- With U = {k} ∪ L ∪ {j+1}: max_U g = g(k), and every element of [k, j+1] ∖ U (the highs, and j) has g > g(k). So J is the unique minimiser.
- g(K_c) − g(J') = g(k) − g(j) < 0. The competitor term is nonzero via the chain k < l_1 < ⋯ < l_s < j.

The weight lemma then finishes. ∎

In A_2 the witness is Δ_{12,23} = xy − z = w with ẽ_1 w = y: exactly the documented C3 failure.

## Verification (all `computed`)

| check | result | script |
|---|---|---|
| A_2 calibration vs polynomial model | all 12 (θ, j) counts identical | `q60_test.py 2 5` |
| A_3 classification | 72/72 (36 neg / 18 adj / 18 far), height ≤ 6 | `q60_test.py 3 6` → `a3_h6.out` |
| A_4 classification | 480/480 (240 / 96 / 144), height ≤ 5 | `q60_checks.py 4 5` |
| exact (b) rule | 136 (A_2) + 2160 (A_3) + 12672 (A_4) / same | `q60_checks.py` |
| split word-independence | 0 failures A_2–A_4 | `q60_checks.py` |
| (c) flag-minor witness, combinatorics + n_0 determinant | 12164/12164 far (g, j), SL_m with m ≤ 7 | `c_witness_flag.py` |
| (c) witness with honest polynomials (Cauchy–Binet via f(XY), column derivation) | 18/18 far pairs, SL_4 | `c_poly_A3.py` |
| B2: ε_j^*(b(n_T, m, 0)) = m (ε_k^* = last coordinate in a word whose last root is α_k) | 6216/6216 in A_3 over 48 adj (word, ℓ) cases; A_4 run not finished in session | `b_lemma.py 3 8` |
| **negative control (breaking)** | wrong criterion "T∪{α_j} co-closed" (always true) predicts all local; actual: 18 non-local A_3 pairs → 18 mismatches | `negctrl_wrongbiconvex.py` |
| negative control (relabel, DISCARDED) | swapping b_+ ↔ b_− still matches 72/72. The test is symmetric, so this control cannot fail; recorded as non-evidence | `q60_test.py 3 6 BREAK` |

## Gaps (precise)

1. **P0 orientation and identification.** Φ_θ = (S-part, T-part) of the Lusztig datum in a T-first word. TW 3.4/3.9 is cited, but the orientation is fixed only by the A_2 calibration plus A_3/A_4 consistency. (a) and (b) rest on it; (c) does not.
2. **B2** rests on three Lusztig/Kashiwara facts cited from memory. One of them, U^+(x) ⊂ ker e_j'^*, has an unchecked T vs T^{-1} convention.
3. **B3** locator (Kas93 Thm 2.2.1) is unverified first-hand.
4. **(c) outside type A** is not proved. Expected route: the rank-2 subsystem {α, α_j, α+α_j}, or (c) through B2-type star strings.
5. **Owner check** for (b) was not run: no browsing in a PROVE session. The PROVE brief asked for 10 minutes; this is now owed to Wake/Browse.
   Risk: (b) is "Kashiwara's embedding seen through a convex order with α_j in position ℓ+1". It is plausibly folklore in the Saito-reflection / BZ-trail literature.
