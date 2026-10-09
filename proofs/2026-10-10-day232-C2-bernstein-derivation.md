# Day 232 PROVE (b): (C2) Bernstein is not an import. It is formal from the word, (R3), (R4) and (C1).

**Date:** 2026-10-09 (Day 232 PROVE; the filename carries the PROVE.md-assigned date 2026-10-10)
**Status:** PROVED (hand derivation below, every step a line of algebra). Machine check `scripts/day232/c2_check.py` → `c2_check.log`: all True.
**Consequence:** the Cherednik imports behind (N) (proof file 216b §9.1) shrink from (C1)+(C2)+(C3) to **(C1)+(C3)**.

> Drunk summary: Bernstein's theorem in this setting is four lines. (B2) is the definition of Y_{i+1} rewritten. Use the quadratic relation to turn T_i^{-1} into T_i. Get two "almost commutation" relations whose error terms are ±(t−1)Y_{i+1}, add them, and the errors cancel. That gives Y_i+Y_{i+1}. Multiply the two instead and you get Y_iY_{i+1}, but only if Y_i and Y_{i+1} commute, so (C1) is the one thing you need. Far commutation is braid relation plus π-shift, nothing else. And none of it cares whether π is Cherednik's shift or Hikita's twisted x_1·shift, so it covers the paper's own Y_i.

---

## 0. Setting (the long version's conventions, `longversion.tex` §2.1, l.90–96)

On Pol = ℚ(s,t)[x_1,…,x_m]:

- T_i f := t s_i f + (t−1) x_{i+1}(s_i f − f)/(x_i − x_{i+1}) for 1 ≤ i ≤ m−1.
- π is **any** operator on Pol satisfying

  (R3) π T_k = T_{k+1} π for 1 ≤ k ≤ m−2.

  Both shifts in use satisfy it:
  - Cherednik's π_0 f = f(x_2,…,x_m, s x_1);
  - Hikita's/the paper's π f = x_1 · π_0 f (= 216c's π^•).
- Y_i := t^{m−i} T_{i−1}⋯T_1 π T_{m−1}^{-1}⋯T_i^{-1} for 1 ≤ i ≤ m.

Facts about the T_i used below. All are elementary, and §3 proves them:

- (R4) (T_i − t)(T_i + 1) = 0. Hence T_i is invertible, with T_i^{-1} = t^{-1}T_i − (1 − t^{-1}).
- (Br) T_iT_{i+1}T_i = T_{i+1}T_iT_{i+1}, and T_iT_k = T_kT_i for |i − k| ≥ 2.

The single imported fact:

- (C1) the Y_i pairwise commute. This is used **only** in Lemma 2(b) and Theorem 3.

## 1. Lemma 1 (B2: formal from the word)

**Claim.** T_i Y_i T_i = t Y_{i+1} for 1 ≤ i ≤ m−1.

*Proof.* Y_i T_i = t^{m−i} T_{i−1}⋯T_1 π T_{m−1}^{-1}⋯T_{i+1}^{-1}, since the trailing T_i^{-1} cancels. Left-multiply by T_i: T_iY_iT_i = t^{m−i} T_iT_{i−1}⋯T_1 π T_{m−1}^{-1}⋯T_{i+1}^{-1} = t · Y_{i+1}. ∎

## 2. Lemma 2 (the two Bernstein relations)

**Claim.**
(a) [T_i, Y_i + Y_{i+1}] = 0, with no hypothesis on the Y's beyond the definition.
(b) If Y_iY_{i+1} = Y_{i+1}Y_i, then [T_i, Y_iY_{i+1}] = 0.

*Proof.* Right-multiply Lemma 1 by T_i^{-1}, then substitute (R4):

  T_iY_i = t Y_{i+1}T_i^{-1} = Y_{i+1}T_i − (t−1)Y_{i+1}.  (1)

Left-multiply Lemma 1 by T_i^{-1}, then substitute (R4):

  Y_iT_i = t T_i^{-1}Y_{i+1} = T_iY_{i+1} − (t−1)Y_{i+1},  i.e.  T_iY_{i+1} = Y_iT_i + (t−1)Y_{i+1}.  (2)

(a) Add (1) and (2): T_i(Y_i + Y_{i+1}) = Y_{i+1}T_i + Y_iT_i, and the (t−1)Y_{i+1} terms cancel.

(b) Apply (1), then (2):

  T_iY_iY_{i+1} = Y_{i+1}T_iY_{i+1} − (t−1)Y_{i+1}^2 = Y_{i+1}(Y_iT_i + (t−1)Y_{i+1}) − (t−1)Y_{i+1}^2 = Y_{i+1}Y_iT_i.

The last expression equals Y_iY_{i+1}T_i by the hypothesis. ∎

(Without (C1), (b) still holds in the form T_i Y_iY_{i+1} = Y_{i+1}Y_i T_i.)

## 3. Lemma 3 (far commutation: formal from (Br) and (R3))

**Claim.** T_iY_j = Y_jT_i whenever j ∉ {i, i+1}.

*Proof.* There are two cases.

*Case j ≥ i+2.* Write Y_j = t^{m−j} · T_{j−1}⋯T_1 · π · T_{m−1}^{-1}⋯T_j^{-1}.

- In T_{j−1}⋯T_1, T_i commutes with T_{j−1},…,T_{i+2}. It then meets T_{i+1}T_i, and T_i T_{i+1}T_i = T_{i+1}T_i T_{i+1} by (Br). The new T_{i+1} commutes with T_{i−1},…,T_1. So T_i·(T_{j−1}⋯T_1) = (T_{j−1}⋯T_1)·T_{i+1}.
- T_{i+1}π = πT_i by (R3) with k = i. This is legal: i ≤ j−2 ≤ m−2.
- T_i commutes with T_{m−1}^{-1},…,T_j^{-1}, since all of these indices are ≥ i+2.

Hence T_iY_j = Y_jT_i.

*Case j ≤ i−1.*

- T_i commutes with T_{j−1},…,T_1, since all of these indices are ≤ i−2.
- T_iπ = πT_{i−1} by (R3) with k = i−1, which satisfies 1 ≤ i−1 ≤ m−2.
- The tail T_{m−1}^{-1}⋯T_j^{-1} contains T_i^{-1}T_{i−1}^{-1}, because j ≤ i−1. T_{i−1} commutes with T_{m−1}^{-1},…,T_{i+1}^{-1}.
- For a = T_{i−1}, b = T_i, the braid relation aba = bab is equivalent to a b^{-1}a^{-1} = b^{-1}a^{-1} b. Indeed, multiply the latter by b on the left and by a on the right: b a b^{-1} = a^{-1} b a; multiply by a on the left and by b on the right: a b a = b a b.
- Hence T_{i−1}·T_i^{-1}T_{i−1}^{-1} = T_i^{-1}T_{i−1}^{-1}·T_i. The new T_i commutes with T_{i−2}^{-1},…,T_j^{-1}.
- So T_{i−1}·(T_{m−1}^{-1}⋯T_j^{-1}) = (T_{m−1}^{-1}⋯T_j^{-1})·T_i.

Hence T_iY_j = Y_jT_i. ∎

## 4. Theorem 3 ((C2), Bernstein)

**Claim.** Assume (C1). Then for every symmetric polynomial f ∈ ℚ(s,t)[y_1,…,y_m]^{S_m}, the operator f(Y) commutes with every T_i.

*Proof.* Fix i. f is symmetric in particular under y_i ↔ y_{i+1}. So, by the fundamental theorem on symmetric polynomials in two variables (with coefficients in the polynomial ring of the other y_j), f is a polynomial in

  y_i + y_{i+1},  y_iy_{i+1},  y_j (j ≠ i, i+1).

By (C1), substituting y ↦ Y is a ring homomorphism into a commutative algebra of operators. So f(Y) is the same polynomial in

  Y_i + Y_{i+1},  Y_iY_{i+1},  Y_j (j ≠ i, i+1).

Each of these commutes with T_i, by Lemma 2(a), Lemma 2(b) (which uses (C1) once more) and Lemma 3. ∎

**Remark (twisted Y).** Nothing above uses the specific π. So Theorem 3 holds verbatim for the paper's Y_i, i.e. 216c's Y^•, given that they commute. That commutativity is itself a corollary of (NS): the Y^•_i are γ̂-conjugates of the X_i. But (NS) is proved using (C2) for the *untwisted* Y, so the safe order is: untwisted (C1) ⇒ untwisted (C2) ⇒ (NS) ⇒ twisted (C1) ⇒ twisted (C2). That order has no circularity.

## 5. Proof of (R4) and (Br) (so they are not imports either)

- **Linearity.** T_i is linear over the polynomials symmetric in x_i, x_{i+1}, with coefficients in the other variables: if s_i g = g then s_i(gf) = g s_i f, and both terms of T_i scale by g.
- **(R4).** Pol is free over that ring with basis {1, x_i}. Compute: T_i 1 = t, and T_i x_i = t x_{i+1} + (t−1)x_{i+1}(x_{i+1} − x_i)/(x_i − x_{i+1}) = x_{i+1} = e − x_i, where e = x_i + x_{i+1}. Then
  - T_i^2 x_i = te − e + x_i, so (T_i^2 − (t−1)T_i − t)x_i = te − e + x_i − (t−1)(e − x_i) − t x_i = 0;
  - on 1: t^2 − (t−1)t − t = 0. ✓
- **(Br), far part.** T_i and T_k (|i−k| ≥ 2) act in disjoint pairs of variables. Each is linear over polynomials in the other pair, so they act as T ⊗ 1 and 1 ⊗ T on ℚ(s,t)[x_i,x_{i+1}] ⊗ ℚ(s,t)[x_k,x_{k+1}] ⊗ (rest). Hence they commute.
- **(Br), braid part.** Both sides of T_iT_{i+1}T_i = T_{i+1}T_iT_{i+1} are linear over R := ℚ(s,t)[x_i,x_{i+1},x_{i+2}]^{S_3} ⊗ ℚ(s,t)[other x], since an S_3-invariant is invariant under each of s_i, s_{i+1}.
  - ℚ[x_1,x_2,x_3] is free over ℚ[x_1,x_2,x_3]^{S_3} on the six monomials x_1^a x_2^b, a ≤ 2, b ≤ 1. This is the classical sub-staircase (Artin) basis of the coinvariant algebra. It is standard; no locator was read this session, so it is the one textbook input of §5.
  - The long version already asserts (Br) without citation (l.96). So the paper's status is unchanged either way.
  - So (Br) reduces to the six monomials of degree ≤ 3 in three variables, and it is translation-invariant in i.
  - `c2_check.py` verifies exactly these, symbolically in s, t (m = 3, all monomials of degree ≤ 3). That is a complete finite verification, not a sample.
  - The braid relation is also standard (Lusztig 1989 / Macdonald 2003); we do not need the citation.
- **(R3)** for π_0. (π_0 T_k f)(x) = (T_k f)(z), where z = (x_2,…,x_m, s x_1). For k ≤ m−2, z_k = x_{k+1} and z_{k+1} = x_{k+2}, and s_k z is the π_0-image of s_{k+1}x. So this equals T_{k+1}(π_0 f)(x).
- **(R3)** for π = x_1π_0. x_1 is symmetric in x_{k+1}, x_{k+2}, so T_{k+1} commutes with multiplication by x_1 when k+1 ≥ 2. ✓

## 6. Verification (`scripts/day232/c2_check.py`, log `c2_check.log`)

- **Method.** SymPy, symbolic s and t. The operators are built from the definitions in §0. T^{-1} is implemented by (R4), whose inverse property is itself checked. Every identity is tested on **all** monomials of degree ≤ 3, for:
  - m = 3 and m = 4 with Cherednik's π_0;
  - m = 3 with the paper's twisted π = x_1π_0.
- **Identities.** (R4) quadratic and inverse, (B2), (1), (2), [T_i, Y_i+Y_{i+1}], [T_i, Y_iY_{i+1}], far [T_i, Y_j], (R3), (Br) braid and far, (C1) (the import, checked here only as a sanity check), and [T_i, e_2(Y)].
- **Result.** All True.
- **Negative control.** T_1Y_1T_1 = Y_2 (dropping the t) fails, as it should.

## 7. Effect on the (N) imports (216b §9.1)

| fact | before | after |
|---|---|---|
| (C1) Y_i commute | import | import (Macdonald 2003 / Cherednik 2005 — locator still to read first-hand) |
| (C2) Bernstein | import | **proved here** from (C1), Lemmas 1–3, (R3), (R4), (Br) |
| (C3) triangularity + simple spectrum, y_i(λ) = s^{λ_i}t^{b_i(λ)} | import | import |

Use in 216c §9.3 step 2: γ̂|_{Pol_d} = f_d(Y)|_{Pol_d} with f_d ∈ Sym(Y). Theorem 3 (untwisted π_0) gives [T_i, γ̂] = 0. That is the only place (C2) enters, and only the untwisted version is needed.

## 8. Long-version appendix lemma (ready to paste when (N) enters; NOT inserted now)

The long version deliberately excludes (N), so an unused lemma would be noise in the paper. The snippet `work-in-progress/longversion/appendix-C2-bernstein.tex` holds Lemmas 1–3 and Theorem 3 in the paper's notation, with Y_i defined from an arbitrary π satisfying (R3).

## Gaps

None in (C2) itself. The remaining (N) gaps are exactly (C1) and (C3), both unlocated first-hand. The Artin-basis citation in §5 is classical. The braid relation could alternatively be cited, but it is proved here by the finite check.
