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
- *Locator (Wake 273, first-hand):* Tingley–Webster 1210.6921 Def 1.18 + Prop 1.19 pp.10–11: the Lusztig-datum coordinate at an extremal root α_i of the convex order is φ*_i (α_i maximal) / φ_i (α_i minimal) — TW work in B(−∞); the passage to the B(∞) form ε*_j used here goes through the standard B(−∞) ↔ B(∞) identification, which was not checked separately. TW prove Prop 1.19 via Saito Prop 3.4.7, which was **not** read first-hand.
- *Computed:* ε_j^*(b(n_T, m, 0)) = m in the model, where ε_k^* is the last coordinate in a word whose last root is α_k (`b_lemma.py`, see Verification).

**B3 (Kashiwara embedding; cited, first-hand Wake 273: Kashiwara–Saito, Duke 89 (1997), q-alg/9606009, Thm 3.2.2 p.7 = Kashiwara Duke 71 (1993) Thm 2.2.1).** Ψ_j^* : b ↦ (ẽ_j^*)^{ε_j^*(b)} b ⊗ b_j(−ε_j^*(b)) is a strict embedding B(∞) → B(∞) ⊗ B_j for all ẽ_k, with the tensor rule
ẽ(b_1 ⊗ b_2) = ẽb_1 ⊗ b_2 if φ(b_1) ≥ ε(b_2), and b_1 ⊗ ẽb_2 otherwise; here ε_j(b_j(−m)) = m.
- Sources: Kashiwara–Saito q-alg/9606009 Thm 3.2.2 p.7 [first-hand, Wake 273], = Kashiwara Duke 71 (1993) 839–858 Thm 2.2.1 [original not read]. Tensor-rule convention: KS97 §3.1 pp.6–7 (Kashiwara convention) [first-hand]; restated in Nakashima–Zelevinsky q-alg/9703045 eqs (2.16)–(2.21) and Thm 2.6 [first-hand]. Kashiwara's original CMP 133 / Duke 63 not on arXiv, not read. Also: TW 1210.6921, proof of Prop 1.4, citing [KS97, Prop 3.2.3].
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
3. **B3** locator: closed Wake 273 — Kashiwara–Saito q-alg/9606009 Thm 3.2.2 (= Kas93 Thm 2.2.1), first-hand. Kas93 itself not read.
4. **(c) outside type A** is not proved. Expected route: the rank-2 subsystem {α, α_j, α+α_j}, or (c) through B2-type star strings.
5. **Owner check** for (b): run Wake 273 (see section below). Verdict: owned modulo P0. Still open: P0 traced first-hand (TW Props 3.4/3.9, BKT 1110.3661 Thm 4.4/Prop 5.24); Saito Prop 3.4.7 (behind B2's TW locator) not read first-hand.
   Risk: (b) is "Kashiwara's embedding seen through a convex order with α_j in position ℓ+1". It is plausibly folklore in the Saito-reflection / BZ-trail literature.

## Owner check (Wake 273, 2026-11-03)

Sources read first-hand; verbatim quotes in `memory/reading/2026-11-03-wake273-owner-check.md`.

- **Verdict: owned modulo P0.** (b) is Kashiwara's Ψ_j embedding read through a convex order with α_j at the seam; the content of Q60 beyond the literature is the far/non-local classification (c) and the chamber criterion.
- **Best citation:** Kashiwara–Saito, Duke 89 (1997), q-alg/9606009, Thm 3.2.2 (= Kashiwara Duke 71 (1993) Thm 2.2.1), with the tensor rule of §3.1. The ∗-end coordinate is supplied by Tingley–Webster 1210.6921 Def 1.18/Prop 1.19 (via Saito Prop 3.4.7, not read first-hand).
- The non-trivial end is the ∗-end. The other end is trivial: BKT 1110.3661 Thm 1.5(iii), TW Prop 3.13.
- No source states Q60(b) word for word.
- **P0 not traced first-hand.** P0 identifies Baumann's HN factorisation Φ_θ, with its orientation, with the Lusztig-datum split. Candidate sources: TW Props 3.4/3.9; BKT 1110.3661 Thm 4.4/Prop 5.24 (torsion pairs ↔ HN).
- No grade changes.

---

## PROVE 273 (2026-11-03): P0-free proof of (a) and (b)

**Change of problem.** PROVE 273 was meant to trace P0, the identification of Φ_θ with the Lusztig-datum split, through
TW/BKT conventions. P0 turns out to be **unnecessary**. (a) and (b) follow directly from Baumann's axioms
(Def 3.1, Thm 2.6, Prop 2.9, Prop 3.3, Cor 3.5, Prop 3.12) together with Kashiwara–Saito Thm 3.2.2. No Lusztig data,
no PBW bases, no TW/BKT. All Baumann locators were read first-hand today in `reading/pdfs/2401.10340.pdf` (pdftotext).
P0 is demoted to a side remark (§P0 below). The proof holds for **every polite basis** and every G (not only simply laced),
because B3 is a statement about the bicrystal B(∞), which is the same for all biperfect bases.

### Conventions (Baumann §3.1–3.2, first-hand)

- n·f = f(?n) (left action = right translation), f·n = f(n?). ⟨x, f⟩ = (x·f)(1).
- x·f = (id ⊗ ⟨x,·⟩)Δf and f·x = (⟨x,·⟩ ⊗ id)Δf. Also Δ(x·f) = (id ⊗ x·)Δf, because (x·f)(gh) = ∂_t f(gh e^{tx}).
- Degrees are written in Q_+ (deg f = −weight). L(f) is the set of left degrees of Δf, and Pol(f) = conv L(f).
- For θ: S = {θ > 0}, T = {θ < 0}. N_{<0} = N_T, N_{>0} = N_S, and N = N_S ⋈ N_T (Zappa–Szép, §3.2).
  O_{>0} = ^{N_T}O is the set of functions with f(gn) = f(g) for n ∈ N_T, i.e. functions of u_S in g = u_S u_T.
  O_{≤0} = O^{N_S} is the set of functions with f(ng) = f(g) for n ∈ N_S, i.e. functions of u_T.
  Multiplication O_{>0} ⊗ O_{≤0} → O is an algebra isomorphism (Thm 2.6 grouped by Prop 2.7, or directly from Zappa–Szép).
- Γ_θ-degree (r, d) = (ht, θ). The order is x_1 ≤′ x_2 ⟺ d_1 < d_2 or (d_1 = d_2 and r_1 ≥ r_2). F′_x = span{f : L(f) ⊂ x + Π′}.
  The **level** of b is the ≤′-maximum of L(b).
  Polite (iii): the (level, ν − level) component of Δb is b_+ ⊗ b_−, with b_+ ∈ B_S := B ∩ O_{>0} and b_− ∈ B_T := B ∩ O_{≤0}.
  Φ_θ : B → B_S × B_T, b ↦ (b_+, b_−), is a degree-additive bijection.
- **Φ_θ depends only on the Weyl chamber of θ.** For generic θ and b ∈ B, the θ-max of the GGMS polytope Pol(b) (Cor 3.5) is a
  single vertex α. It is the ≤′-maximum of L(b), and b_+ is the left factor of the (α, ν−α) component.
- **Crystal.** B is biperfect (Prop 3.12). The string map b ↦ (e_j^{(ℓ)}·b, ℓ), with ℓ = ℓ_j(b) := max{n : e_j^n·b ≠ 0}, is a
  bijection B → (B ∩ ker e_j) × ℕ (proof of Prop 3.12, quoted). Define ẽ_j b as the element with the same string top and ℓ − 1.
  This agrees with BKK Def 2.1's ẽ_j, because e_j^{(ε)}·b = ẽ_j^{ε} b [BKK §2.3, first-hand]. Define ẽ*_j in the same way via ·e_j.
- ζ_j^k is the unique element of B of degree kα_j, because O_{−kα_j} = kζ_j^k (α_j is simple). Also ⟨e_j^{(k)}, ζ_j^k⟩ = 1.

### Lemma A (string lemma). If α_j ∈ T, then ℓ_j(b) = ℓ_j(b_−) for all b ∈ B, and Φ_θ(e_j^{(ℓ)}·b) = (b_+, e_j^{(ℓ)}·b_−) for ℓ = ℓ_j(b).

*Proof.*
1. **e_j acts on the second factor.** E_j ∈ n_T, so e_j· kills O_{>0} (right N_T-invariants). e_j· is a derivation, and it
   preserves O_{≤0}, since right translations commute with left translations. So under O ≅ O_{>0} ⊗ O_{≤0}, e_j = id ⊗ e_j.
2. **Leading component.** Let α be the level of b. Δ(e_j^{(n)}·b) = (id ⊗ e_j^{(n)})Δb, so L(e_j^{(n)}·b) ⊂ L(b), and the
   (α, ·) component of Δ(e_j^{(n)}·b) is b_+ ⊗ e_j^{(n)}·b_−.
   - If e_j^{(n)}·b_− ≠ 0, then e_j^{(n)}·b ≠ 0, so ℓ_j(b) ≥ ℓ_j(b_−) pointwise.
   - If moreover e_j^{(n)}·b ∈ B, then its level is α and Φ_θ(e_j^{(n)}·b) = (b_+, e_j^{(n)}·b_−).
3. **Counting.** For a perfect basis, B ∩ ker e_j^{n+1} = {ℓ_j ≤ n} is a basis of ker e_j^{n+1}. (If f = Σ c_b b ∈ ker e^{n+1} and
   m = max ℓ over the support is > n, then e^{(m)}f is a nonzero combination of distinct basis elements; contradiction.)
   - The same holds for B_T inside O_{≤0}: it is a basis of O_{≤0} by polite (iii), and it is e_j-perfect because e_j^{(ℓ)} maps
     B_T into B ∩ O_{≤0}.
   - By step 1, ker(e_j^{n+1}) ≅ O_{>0} ⊗ ker(e_j^{n+1}|O_{≤0}).
   - Using the bijection Φ_θ in each degree ν:
     #{b ∈ B_ν : ℓ_j(b_−) ≤ n} = Σ_α dim O_{>0,α} · dim ker(e_j^{n+1}|O_{≤0})_{ν−α} = dim ker(e_j^{n+1})_ν = #{b ∈ B_ν : ℓ_j(b) ≤ n}.
   - Since ℓ_j(b) ≥ ℓ_j(b_−) pointwise, {ℓ_j(b) ≤ n} ⊂ {ℓ_j(b_−) ≤ n}. The two sets have equal cardinality, so they are equal.
     Hence ℓ_j(b) = ℓ_j(b_−).
4. With ℓ = ℓ_j(b) = ℓ_j(b_−), e_j^{(ℓ)}·b ∈ B by perfectness, and step 2 gives the formula. ∎

### Theorem (a). If α_j ∈ T and ẽ_j b ≠ 0, then Φ_θ(ẽ_j b) = (b_+, ẽ_j b_−). Also ε_j(b) = ε_j(b_−).

*Proof.* Let b′ = ẽ_j b, ℓ = ℓ_j(b). Then ℓ_j(b′) = ℓ − 1 and e_j^{(ℓ−1)}·b′ = e_j^{(ℓ)}·b.
By Lemma A applied to b and to b′:
(b′_+, e_j^{(ℓ−1)}·b′_−) = Φ_θ(e_j^{(ℓ−1)}·b′) = Φ_θ(e_j^{(ℓ)}·b) = (b_+, e_j^{(ℓ)}·b_−).
So b′_+ = b_+. Also b′_− and b_− are elements of B with the same string top, and ℓ_j(b′_−) = ℓ − 1, ℓ_j(b_−) = ℓ.
Hence b′_− = ẽ_j b_−. ∎

### Lemma C (coherence across a wall). Let T′ = T ⊔ {α_j} be biconvex (the "adj" case for θ), with θ′ in the T′-chamber.
For b ∈ B write Φ_θ′(b) = (p, q) and Φ_θ(b) = (b_+, b_−). Then there is m ≥ 0 such that
  Φ_θ′(b_+) = (p, ζ_j^m),  Φ_θ(q) = (ζ_j^m, b_−),  m = ε_j(b_+) = ε*_j(q),  b_− = q·e_j^{(m)}.

*Proof.*
- **Choice of θ*.** The T- and T′-chambers share the wall α_j^⊥. Pick θ* on that wall, generic on it (θ*(β) ≠ 0 for β ≠ α_j).
  For small η > 0, θ* + η·ht lies in the T-chamber and θ* − η·ht in the T′-chamber. By chamber-independence, take θ = θ* + η·ht and θ′ = θ* − η·ht.
  For θ*: N_{>0} = N_{S′} with S′ = S ∖ {α_j}, N_0 = U_j, N_{<0} = N_T, and N = N_{S′} ⋈ U_j ⋈ N_T (§3.2).
- **The face.** Let F be the θ*-max face of Pol(b). Pol(b) is GGMS (Cor 3.5), so its normal cone at F contains the Weyl wall cone through θ*,
  whose span is α_j^⊥. Hence F ⊂ α + ℝα_j: F is a segment [α′, α] with α − α′ = mα_j, m ∈ ℤ_{≥0}.
  Here α is the endpoint of larger height (the θ-max vertex) and α′ the endpoint of smaller height (the θ′-max vertex).
  Every point of L(b) with θ* = max lies on F.
- **Bilevel.** For θ*:
  - the F′-level of b (max θ*, ties broken by smallest height) is α′;
  - the F″-level (Baumann §2.3: ≤″-max of R(b), i.e. min θ* of the right degree, ties broken by smallest height) is y := ν − α.
- **Δ₂-injectivity, proved here from Thm 2.6 (Prop 2.11's proof is omitted in the paper).**
  Fix homogeneous bases of the A_{[μ]} and use the ordered-monomial basis of Thm 2.6, grouped as A_{>0} ⊗ A_0 ⊗ A_{<0} ≅ A.
  - By Lemma 2.4(i), an ordered monomial a_+ a_0 a_− has ≤′-max left degree |a_+|: the left end of the slope-0 segment of its rim.
    By the proof of Prop 2.9 (F′_x is spanned by ordered monomials with Pol∧ ⊂ x + Π′), F′_x = ⊕_{x′ ≤′ x} A_{>0,x′} ⊗ A_0 ⊗ A_{<0}.
  - Mirror: F″_y = ⊕_{y′ ≤″ y} A_{>0} ⊗ A_0 ⊗ A_{<0,y′}. The R-condition is an L-condition on a convex region containing the chord, so Prop 2.5 applies.
  - For homogeneous a_± and a_0, the (|a_+|, |a_0|, |a_−|) component of (Δ⊗id)Δ(a_+a_0a_−) is a_+ ⊗ a_0 ⊗ a_−.
    This is the d-coordinate argument: R(a_+) has d > 0 or is 0, A_0 has d = 0, and L(a_−) has d < 0 or is 0.
    Monomials with x′ <′ x, or with y′ <″ y, have no (x, ·, y) component.
  - Hence the (x, ·, y) tri-component map has kernel exactly F′_{<x} ∩ F″_y + F′_x ∩ F″_{<y} on F′_x ∩ F″_y.
- **Basis compatibility.** F′_x ∩ F″_y ∩ O_ν, F′_{<x} ∩ F″_y ∩ O_ν and F′_x ∩ F″_{<y} ∩ O_ν each have the form {f : L(f) ⊂ K} with K convex.
  (Note (x + Π′) ∖ {x} is convex.) So each equals O_ν ∩ S(conv(K ∩ M_ν)), and by Prop 3.3 it is spanned by its intersection with B.
  b has exact bilevel (α′, y), so b ∉ F′_{<α′} ∩ F″_y + F′_{α′} ∩ F″_{<y} (linear independence of B).
  Therefore the tri-component C := [(Δ⊗id)Δb]_{(α′, mα_j, ν−α)} ≠ 0.
- **Reading C two ways** (coassociativity).
  From θ: C = [Δb_+]_{(α′, mα_j)} ⊗ b_− = (e_j^{(m)}·b_+) ⊗ ζ_j^m ⊗ b_−.
  From θ′: C = p ⊗ [Δq]_{(mα_j, ν−α)} = p ⊗ ζ_j^m ⊗ (q·e_j^{(m)}).
  The two middle factors are ζ_j^m because O_{−mα_j} = kζ_j^m; the outer factors follow from the two action formulas.
- **b_+ side.** b_+ is a function of u_S. Right factors of Δb_+ are right N_T-invariant. The θ′-right factor of b_+ is also
  left N_{S′}-invariant, hence a function of the U_j-coordinate, i.e. ζ_j^k with k = ε_j(b_+).
  So Φ_θ′(b_+) = (p′, ζ_j^k) at level α − kα_j.
  - C ≠ 0 gives α′ ∈ L(b_+), so θ′(α′) ≤ θ′(α − kα_j), i.e. m ≤ k.
  - p′ ⊗ ζ^k ⊗ b_− is a nonzero tri-component of b at (α − kα_j, kα_j, ν−α). Hence α − kα_j ∈ L(b) on F, so k ≤ m.
  - So k = m, and p′ ⊗ ζ^m ⊗ b_− = C = p ⊗ ζ^m ⊗ q·e_j^{(m)}. Hence p′ = p (two elements of B that are proportional are equal)
    and q·e_j^{(m)} = b_−.
- **q side.** Symmetrically, Φ_θ(q) = (ζ_j^{k′}, q·e_j^{(k′)}) with k′ = ε*_j(q). Left factors of q are left N_{S′}-invariant,
  and the θ-left factor is also right N_T-invariant.
  - C ≠ 0 gives mα_j ∈ L(q), so k′ ≥ m.
  - α′ + k′α_j ∈ L(b) on F, so k′ ≤ m. Hence k′ = m. ∎

### Theorem (b). Assume adj (T ∪ {α_j} biconvex, α_j ∈ S). If ẽ_j b ≠ 0, then
  Φ_θ(ẽ_j b) = (ẽ_j b_+, b_−) if ε_j(b_+) > φ_j(b_−), and (b_+, ẽ_j b_−) otherwise, where φ_j(c) = ε_j(c) + ⟨h_j, wt c⟩.

*Proof.* Take θ′ and the notation of Lemma C; m = ε_j(b_+).
1. **On B_{T′}, Φ_θ is the ∗-string decomposition.** For c ∈ B_{T′} = B ∩ O^θ′_{≤0}: Φ_θ(c) = (ζ_j^{ε*_j(c)}, (ẽ*_j)^{max} c).
   This is the q-side argument of Lemma C, which only used c ∈ B_{T′}.
2. **Reduce to B_{T′}.** α_j ∈ T′, so (a) for θ′ gives ẽ_j b = Φ_θ′^{-1}(p, ẽ_j q) with ẽ_j q ∈ B_{T′}, and ẽ_j q ≠ 0.
3. **B3.** [Kashiwara–Saito q-alg/9606009 Thm 3.2.2, first-hand today, pp.6–7.]
   - Ψ_j : B(∞) ↪ B(∞) ⊗ B_j is a strict embedding.
   - Ψ_j(c) = c′ ⊗ f̃_j^n b_j with n = ε_j(c*), ε_j(c′*) = 0, c = f̃*_j^n c′.
   - Tensor rule (§3.1): ẽ(b_1 ⊗ b_2) = ẽb_1 ⊗ b_2 if φ(b_1) ≥ ε(b_2), and b_1 ⊗ ẽb_2 otherwise. Also ε_j(f̃_j^n b_j) = n.
   - It applies to (B, ẽ, ẽ*): by BKK 1905.08460 Thm 2.4 [first-hand] the bicrystal of a biperfect basis is unique, hence is the
     bicrystal of the dual canonical basis, i.e. Kashiwara's (B(∞), ẽ, ẽ*). If the identification swaps ẽ and ẽ*, compose with ∗.
   - With c = q, n = m and c′ = b_−:
     - if m ≤ φ_j(b_−): ẽ_j q = f̃*_j^m ẽ_j b_− with ε*_j(ẽ_j b_−) = 0, so by step 1, Φ_θ(ẽ_j q) = (ζ^m, ẽ_j b_−);
     - if m > φ_j(b_−): ẽ_j q = f̃*_j^{m−1} b_−, so Φ_θ(ẽ_j q) = (ζ^{m−1}, b_−).
4. **Apply Lemma C to ẽ_j b.** We have Φ_θ′(ẽ_j b) = (p, ẽ_j q), so Φ_θ(ẽ_j b) = (Φ_θ′^{-1}(p, (ẽ_j q)_+), (ẽ_j q)_−).
   - Case m ≤ φ: this is (Φ_θ′^{-1}(p, ζ^m), ẽ_j b_−) = (b_+, ẽ_j b_−).
   - Case m > φ: this is (Φ_θ′^{-1}(p, ζ^{m−1}), b_−). By (a) for θ′ applied to b_+, using Φ_θ′(b_+) = (p, ζ^m) and ẽ_j ζ^m = ζ^{m−1},
     we get Φ_θ′^{-1}(p, ζ^{m−1}) = ẽ_j b_+.
   - Finally ε_j(b_+) = ε_j(ζ^m) = m (Lemma A for θ′). ∎

**Scope.** (a) and (b) hold for every polite basis of O(N), G any split reductive group (Baumann's setting), and every generic θ.
Simply-lacedness is not used. Together with (c) (type A, first-hand), Theorem Q60 is now **proved in type A**:
locality ⟺ not far, with the exact tensor rule. Outside type A, (c) is still open (gap 4).

### P0, demoted
P0 (Lusztig-datum split) is no longer a premise of anything. What is now proved is its intrinsic form.
Iterating Lemma C over a maximal chain of cuts gives the "HN datum" (the edge lengths of Pol(b) along the path), and Φ_θ splits it.
- The generalisation of Lemma C to non-simple walls β is the same proof with ζ_j^m replaced by the B-elements of O(U_β) = k[x_β]. Not written out.
- Identifying the HN datum with Kamnitzer-convention Lusztig data is Kamnitzer's MV-polytope theorem plus Baumann §3.3 (Pol(B) = MV polytopes).
  Not traced; not needed.
- The orientation anchor is first-hand anyway: for T = {α_j}, Baumann's proof of Prop 3.12 gives Φ(b) = (e_j^{(ε)}·b, ζ_j^ε).
  So b_− carries ε_j = the n_1 of a T-first word (Kamnitzer Prop 3.4), which is P0's orientation.

### Verification (PROVE 273, `proofs/prove273/`)

| check | result | script |
|---|---|---|
| Lemma A on honest A_2 polynomials (Φ from Δ, BKK Ex 2.3 basis, h ≤ 5): ε_j(b) = ε_j(b_−) for α_j ∈ T | 204/204 | `a2_coherence.py` |
| control (breaks): ε_j(b) = ε_j(b_+) | 72/204 (fails) | same |
| Lemma C, all adjacent chamber pairs, simple and non-simple walls | 204/204 | same |
| control (breaks): b_− = q (no second split) | 90/204 (fails) | same |
| Lemma C numerics: m = ε_j(b_+) = ε*_j(q) on simple walls | 136/136 | same |
| Lusztig model, exact (b) rule, A_3 h ≤ 6 | 2160/2160 | `q60_checks_rev.py 3 6` |
| **negative control (breaks), split REVERSED** (b_+ = T-part) | rule 845/2160 (fails); classification still 72/72 (it is swap-symmetric, as noted in PROVE 272) | `q60_checks_rev.py 3 6 REV` |

The reversed-split control breaks the exact rule, so the P0 orientation (b_− = T-part) is the only one consistent with (b).
The "indep failures 2640" line in the REV run is an artefact: the independence check hard-codes the unreversed split. Ignore it.
The A_4 B2 run was not finished: B2 is no longer a premise.

### Gaps after PROVE 273
1. ~~P0~~: no longer needed.
2. ~~B2~~: no longer needed (replaced by Lemma C).
3. B3 is cited first-hand (KS97 Thm 3.2.2). BKK Thm 2.4 is cited first-hand.
   Remaining non-first-hand link: "the dual canonical basis at q = 1 is biperfect with bicrystal = Kashiwara's B(∞)".
   BKK state it with references [Lu3 Thms 1.6, 7.5; Kas2 §5.3], which I have not read. Textbook.
4. (c) outside type A: open.
5. Not cold-re-derived yet. Grade **proved** (written, every step cited or argued). The sober recheck is owed (Dream 273 / Wake 274).

### Dream 273 cold read (2026-11-03): PASS, no grade change
I re-derived each step from the printed text, without the scripts. Points checked:
- Lemma A step 3. The kernel basis claim uses only that the string-top map is injective, and B_T inherits that by restriction.
- Lemma C, the subtle step: "b ∉ F′_{<α′}∩F″_y + F′_{α′}∩F″_{<y}". This does NOT follow from b missing each summand separately.
  It is rescued correctly: each summand is {L ⊂ K} with K convex, so each is B-spanned (Prop 3.3), and linear independence then applies. The (x+Π′)∖{x} convexity holds.
- In Lemma C, m ≤ k and k ≤ m both reduce to θ*(α_j) = 0 plus the height perturbation. Tri-component ≠ 0 ⇒ left degree ∈ L(b) by coassociativity. OK.
- Theorem (b), step 3. ε*_j(ẽ_j b_−) = 0 is automatic: ẽ_j commutes with the strict embedding Ψ_j, and the image has that form. In case m > φ, ẽ_j b_+ ≠ 0 because m ≥ 1.
- Orientation: (b) is Kashiwara's rule on b_− ⊗ (string of b_+), i.e. φ(b_−) ≥ ε(b_+) ⇒ act on b_−. This is consistent with KS §3.1.
Remaining (unchanged): gap 3 (dual canonical at q=1 biperfect with Kashiwara bicrystal; textbook, Lu/Kas2 unread) and gap 4 ((c) outside type A).
Ownership (Wake 273): the *statement* (b) is Saito/TW-owned for the MV/canonical basis. What is ours is the axiomatic, P0-free route. A remark, not a paper.
