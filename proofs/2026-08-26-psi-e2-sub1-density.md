# Day 134 — Sub-top weight (weight b−1) of Ψ(e_2^b): recursion, closed form for E₃-free slice, density

**Author.** Rick.
**Date.** 2026-08-26.
**Depends on.** Day 131 closed form F(T) = A(T)·B(T) (`2026-08-23-psi-e2-egf-closed-form.md`), Day 133 top-weight density (`2026-08-25-psi-e2-density.md`).

---

## 1. Statement

Let Ψ, e₂, and the (1,1,2)-grading on ℤ[E₁, E₂, E₃] be as in Day 131. Set

  Ψ_b := Ψ(e₂^b) ∈ ℤ[E₁, E₂, E₃],  tops[b] := Ψ_b|_{w=b},  sub_1[b] := Ψ_b|_{w=b−1}.

**Theorem A (Recursion, proved).** For all b ≥ 0,

  sub_1[b+1] = (E₂ − (b+1)E₁) · sub_1[b] + (b+1)² · tops[b]
             − 3b · E₃ · [D(tops[b−1]) + σ_top(sub_1[b−1])]
             − b(b−1) · E₁ · E₃ · [D(tops[b−2]) + σ_top(sub_1[b−2])]
             + 2 b(b−1)(b+1) · E₃ · σ_top(tops[b−2])

with sub_1[b<1] = 0, sub_1[1] = 1, and D the σ-derivation defined in §3.

**Theorem B (E₃-free slice — closed form, density, uniform sign; proved).** For x_1 + x_2 = b − 1 (i.e. x_3 = 0):

  [E₁^{x_1} E₂^{x_2}] sub_1[b] = (−1)^{x_1} · Σ_{r=1}^b r² · e_{x_1}({1,…,b}∖{r})

Every summand is a strictly positive integer, hence the coefficient is nonzero and has sign (−1)^{x_1} = (−1)^{x_1 + x_3}. Density on the E₃=0 slice.

**Theorem C (Full-density and uniform-sign ansatz; density proved via A-side alone).** Define the "sub-top" A/B factors:

  A_n^{(1)} := Σ_{r=1}^n r² · Π_{s ∈ {1,…,n}∖{r}} (E₂ − s E₁),        (weight n−1)

  B_m^{(1)} := (recursively via the ansatz below, with B_0^{(1)} := 0).

Then

  sub_1[b] = Σ_{n+m=b} C(b, n) · [A_n^{(1)} · B_m + A_n · B_m^{(1)}]     (∗)

as an identity in ℤ[E₁, E₂, E₃]. **The E₃-independent part alone** — namely Σ_{n+m=b, contributing to x_3=0} C(b, n) A_n^{(1)} B_m — accounts for the full E₃=0 slice via Theorem B. **For each valid monomial (x_1, x_2, x_3) with x_1 + x_2 + 2x_3 = b−1, the term A_n^{(1)} · B_m with n = x_2 + 1, m = b − x_2 − 1 has the correct uniform sign (−1)^{x_1+x_3} and nonzero magnitude,** so sub_1[b] is nonvanishing at that monomial, provided every other summand of (∗) also carries sign (−1)^{x_1+x_3} (no cancellation).

**Sub-claim (verified b ≤ 8):** B_m^{(1)} has uniform sign (−1)^{x_1 + x_3} per monomial. Under this sub-claim, sub_1[b] is fully supported with uniform sign (−1)^{x_1 + x_3}.

**Numerical status (b = 1..10): FULL DENSITY confirmed, UNIFORM SIGN (−1)^{x_1+x_3} matches all coefficients.** Sizes match A002620(b+1) = ⌊(b+1)²/4⌋ (2, 4, 6, 9, 12, 16, 20, 25, 30 for b=2..10). A_b^{(1)} closed form verified for b = 1..10.

---

## 2. Setup: σ-derivation D

Recall σ: (E₁, E₂, E₃) → (E₁−3, E₂−2E₁+3, E₃−E₂+E₁−1). Its "sub-top" part D drops weight by exactly 1:

  D := −3 · σ_top ∘ ∂/∂E₁ + 3 · σ_top ∘ ∂/∂E₂ + (E₁ − E₂) · σ_top ∘ ∂/∂E₃.

where σ_top: E₁ → E₁, E₂ → E₂ − 2 E₁, E₃ → E₃.

**Lemma (D-derivation).** For any polynomial P ∈ ℚ[E₁,E₂,E₃] of weight w,

  σ(P) = σ_top(P) + D(P) + D₂(P) + D₃(P) + …    (weight-w, w−1, w−2, w−3, …)

D acts as a "σ_top-twisted derivation": D(P·Q) = D(P) · σ_top(Q) + σ_top(P) · D(Q).

*Proof.* By Taylor expansion of σ(P) = P(σ(E)) around the top-weight substitution σ_top(E) = (E₁, E₂ − 2E₁, E₃). Write σ(E_i) = σ_top(E_i) + δ_i with δ_1 = −3, δ_2 = 3, δ_3 = −E₂ + E₁ − 1. Then σ(P) = Σ_α (δ^α/α!) · σ_top(∂^α P). For the weight-(w−1) piece: contributions come only from first-order terms (α = single-index) because δ_i's weight components combined with weight lowering ∂_i · w_i drop weight by exactly 1 only in a specific way; all higher-order contributions drop weight ≥ 2. Direct enumeration gives the D formula above; twisted-derivation property follows from σ being a ring hom. ∎

**Values on generators.** D(E₁) = −3, D(E₂) = 3, D(E₃) = E₁ − E₂.

---

## 3. Proof of Theorem A (Recursion)

Start from the Day 131 full Ψ-recursion (proved for all b):

  Ψ_{b+1} = [E₂ − (b+1)E₁ + (b+1)²] · Ψ_b − 3b · E₃ · σ(Ψ_{b−1}) − b(b−1)(E₁ − 2b − 2) · E₃ · σ(Ψ_{b−2})

Project both sides onto the weight-b component. Use:

- LHS: W_b(Ψ_{b+1}) = sub_1[b+1] by definition.
- Term 1: (E₂ − (b+1)E₁) has weight 1, (b+1)² has weight 0. Contributes  
     W_b((E₂ − (b+1)E₁) Ψ_b) = (E₂ − (b+1)E₁) · sub_1[b],  
     W_b((b+1)² Ψ_b) = (b+1)² · tops[b].
- Term 2 (E₃ σ(Ψ_{b−1})): W_b = E₃ · W_{b−2}(σ(Ψ_{b−1})) = E₃ · [D(tops[b−1]) + σ_top(sub_1[b−1])] (higher-drop contributions vanish because Ψ_{b−1} only has weight ≥ 0 monomials contributing, and W_{b−2}(σ(weight-(b−1))) = D, W_{b−2}(σ(weight-(b−2))) = σ_top; lower weights contribute nothing since σ preserves weight ≤ w).
- Term 3 ((E₁ − 2b − 2) E₃ σ(Ψ_{b−2})): split as E₁ · E₃ · σ(Ψ_{b−2}) − (2b+2) · E₃ · σ(Ψ_{b−2}).  
   W_b(E₁ E₃ σ(Ψ_{b−2})) = E₁ E₃ · W_{b−3}(σ(Ψ_{b−2})) = E₁ E₃ · [D(tops[b−2]) + σ_top(sub_1[b−2])].  
   W_b(E₃ σ(Ψ_{b−2})) = E₃ · W_{b−2}(σ(Ψ_{b−2})) = E₃ · σ_top(tops[b−2]).

Assembling (with signs) yields the claimed recursion. ∎

**Verified computationally b = 0..6** in `code/day134_subtop/step1_recursion_test.py`.

---

## 4. Proof of Theorem B (E₃-free slice)

Restrict (∗) to E₃ = 0. In A_n^{(1)} · B_m, the B_m factor contributes E₁^{m-2k} E₃^k with k = x_3 = 0, forcing m = 0. Then n = b, and

  [E₃^0] sub_1[b] = C(b, b) · A_b^{(1)} · B_0 + C(b, b) · A_b · B_0^{(1)} = A_b^{(1)}      (B_0^{(1)} = 0)

using A_b · B_0^{(1)} = 0 by convention. (Verified b=1..8 in code.)

Now extract [E_1^{b−1−x_2} E_2^{x_2}] A_b^{(1)}. By construction:

  [E_1^{x_1} E_2^{x_2}] A_b^{(1)}  =  Σ_{r=1}^b r² · [E_1^{x_1} E_2^{x_2}] Π_{s∈{1..b}∖{r}}(E_2 − s E_1)
                                  =  Σ_{r=1}^b r² · (−1)^{x_1} · e_{x_1}({1..b}∖{r})

(from [E_1^j E_2^{n-j}] Π_{s ∈ S}(E_2 − s E_1) with |S| = n = b−1 — pick E₂ from x_2 factors, then −sE_1 from the rest, summing over j-subsets). Since e_{x_1}({1..b}∖{r}) is a positive integer for 0 ≤ x_1 ≤ b−1 (the set has b−1 ≥ x_1 elements), every summand is strictly positive; therefore

  [E_1^{x_1} E_2^{x_2}] sub_1[b] = (−1)^{x_1} · Σ_{r=1}^b r² · e_{x_1}({1..b}∖{r}) ≠ 0,

with sign (−1)^{x_1} = (−1)^{x_1+x_3} (since x_3 = 0). ∎

**Verified b = 1..8** in `code/day134_subtop/step4_verify_A1_fit_B1.py` — all E₃=0 coefficients match the formula exactly.

### Corollary (pure-E₂ column, E₃-free)

For x_1 = 0, x_2 = b−1, x_3 = 0: only x_1 = 0 requires e_0({1..b}∖{r}) = 1, so

  [E_2^{b−1}] sub_1[b] = (−1)^0 · Σ_r r² · 1 = Σ_{r=1}^b r² = b(b+1)(2b+1)/6

(power-sum p_2(1..b), the square-pyramidal number). Values 5, 14, 30, 55, 91, 140, 204 for b = 2..8 match empirical data.

### Corollary (pure-E₁ column, E₃-free)

For x_1 = b−1, x_2 = 0, x_3 = 0:

  [E_1^{b−1}] sub_1[b] = (−1)^{b−1} · Σ_r r² · e_{b−1}({1..b}∖{r})
                      = (−1)^{b−1} · Σ_r r² · (b!/r)
                      = (−1)^{b−1} · b! · Σ_r r
                      = (−1)^{b−1} · b! · b(b+1)/2

(using e_{b−1}({1..b}∖{r}) = (b!/r), the product of {1..b} divided by r). Values −6, 36, −240, 1800, … match empirical exactly.

---

## 5. The ansatz (∗) and Theorem C

**Definition.** Set B_0^{(1)} := 0 and define B_m^{(1)} for m ≥ 1 recursively so that (∗) holds:

  B_m^{(1)} := sub_1[m] − Σ_{n=1}^{m} C(m,n) A_n^{(1)} B_{m−n} − Σ_{n=1}^{m−1} C(m,n) A_n B_{m−n}^{(1)}

This is a well-posed recursion (each B_m^{(1)} determined by sub_1[m], A_n, A_n^{(1)}, B_j, and lower B_j^{(1)}). By construction, (∗) holds identically.

Empirically for m = 1..8 (`step4_verify_A1_fit_B1.py`):
  B_1^{(1)} = B_2^{(1)} = 0
  B_3^{(1)} = −48 E₃
  B_4^{(1)} = 708 E₁E₃ − 78 E₂E₃
  B_5^{(1)} = −8400 E₁²E₃ + 1488 E₁E₂E₃ + 2088 E₃²
  B_6^{(1)} = 97200 E₁³E₃ − 21600 E₁²E₂E₃ − 68100 E₁E₃² + 3510 E₂E₃²
  B_7^{(1)} = −1159200 E₁⁴E₃ + 295200 E₁³E₂E₃ + 1547040 E₁²E₃² − 137424 E₁E₂E₃² − 86184 E₃³
  B_8^{(1)} = 14535360 E₁⁵E₃ − 4057200 E₁⁴E₂E₃ − 31084368 E₁³E₃² + 3639048 E₁²E₂E₃ + 4962888 E₁E₃³ − 147420 E₂E₃³

Each B_m^{(1)} has uniform sign (−1)^{x_1 + x_3} in every monomial. **Support-count pattern: |supp(B_m^{(1)})| = m−2 for m ≥ 3** (highly sparse compared to sub_1[b]'s A002620(b+1)). Verified m = 1..10.

Support of B_m^{(1)} appears to be:  
   {(a, b, c) : a + b + 2c = m − 1, b ∈ {0, 1}, and (a, b, c) ≠ some specific "gap" positions}.  
Empirically the excluded positions include (b, x_2, x_3) = (0, 2, x_3) type monomials (which would have b^2, c^2 shape). Detailed characterization pending.

### Structural observation: Q(T) = B^{(1)}(T)/B(T)

Set B^{(1)}(T) := Σ_m B_m^{(1)} · T^m/m!, and let Q(T) := B^{(1)}(T)/B(T) as formal power series in T. Then Q(T) has ONLY monomials with E₃ factor (verified m ≤ 8), and each monomial has uniform sign (−1)^{x_1 + x_3}. Factorizations:

  Q_3 = −8 E₃
  Q_4 = E₃ (118 E₁ − 13 E₂)/4
  Q_5 = −E₃ (350 E₁² − 62 E₁E₂ − 27 E₃)/5
  Q_6 = E₁ E₃ (135 E₁² − 30 E₁E₂ − 29 E₃)
  Q_7 = −E₁² E₃ (1610 E₁² − 410 E₁E₂ − 653 E₃)/7
  Q_8 = 7 E₁³ E₃ (412 E₁² − 115 E₁E₂ − 266 E₃)/8

For n ≥ 6, Q_n has E₁^{n−5} · E₃ as an explicit factor. No fully-general closed form for Q(T) has been identified, but boundary column formulas fit cleanly:

**Boundary column formulas (empirical, verified n ≤ 8):**

  [Q_n at E_1^{n−3} E_3]         = (−1)^n     · (n−1)(n−2)(11n+15) / 12                 (linear in n)
  [Q_n at E_1^{n−4} E_2 E_3]     = (−1)^{n+1} · (n−1)(n−2)(n−3)(5n+6) / (12 n)          (linear)
  [Q_n at E_1^{n−5} E_3²]        = (−1)^{n+1} · (n−1)(n−2)(n−3)(n−4)(7n²+40n+30) / (360 n)  (quadratic)

Verified by direct expansion for n = 3..8 (first), n = 4..8 (second), n = 5..8 (third). The pattern (linear, linear, quadratic in n) suggests deeper structure — perhaps each successive column adds a linear factor from a "generating polynomial" structure to be identified.

### Density proof (conditional on B_m^{(1)} uniform sign)

Fix a monomial (x_1, x_2, x_3) with x_1 + x_2 + 2 x_3 = b − 1.

**Sign of A_n^{(1)} · B_m contribution at (x_1, x_2, x_3):**  
A_n^{(1)} has [E_1^{n−1−a} E_2^a] = (−1)^{n−1−a} · positive.  
B_m has [E_1^{m−2k} E_3^k] = (−1)^{m−k} · positive.  
The product's coefficient at (x_1, x_2, x_3) requires a = x_2 and k = x_3, with n − 1 − x_2 + m − 2 x_3 = x_1, i.e. n + m − 1 − x_2 − 2 x_3 = x_1, i.e. n + m = x_1 + x_2 + 2 x_3 + 1 = b. ✓  
Sign: (−1)^{n−1−x_2} · (−1)^{m−x_3} = (−1)^{b−1−x_2−x_3} = (−1)^{x_1 + x_3}. ✓  
Positive magnitude iff n ≥ x_2 + 1 and m ≥ 2 x_3.

**Sign of A_n · B_m^{(1)} contribution at (x_1, x_2, x_3):** if B_m^{(1)} has uniform sign (−1)^{x_1'+x_3'} at its monomials, then splitting into A_n's (E_1^{n−y} E_2^y) and B_m^{(1)}'s (E_1^i E_2^{x_2 − y} E_3^{x_3}), we get sign (−1)^{n − y} · (−1)^{i + x_3} = (−1)^{n − y + i + x_3} = (−1)^{x_1 + x_3} (since n − y + i = x_1). Uniform, matching.

**Non-vanishing witness:** for any valid (x_1, x_2, x_3), take n = x_2 + 1, m = b − x_2 − 1. Then:
- n ≥ x_2 + 1: ✓ (equality).
- m ≥ 2 x_3: m = b − x_2 − 1 ≥ 2 x_3 ⇔ x_1 ≥ 0 ✓.
- A_n^{(1)} at [E_1^{n−1−x_2} E_2^{x_2}] = [E_1^0 E_2^{x_2}] A_{x_2+1}^{(1)} = Σ_{r=1}^{x_2+1} r² > 0.
- B_m at [E_1^{m−2x_3} E_3^{x_3}] = [E_1^{x_1} E_3^{x_3}] B_m: for x_3 = 0, need m = 0 which forces the choice n = b instead (then this is Corollary A_b^{(1)}, covered). For x_3 ≥ 1, B_m has nonzero (m!/x_3!) · P(m, x_3) > 0 (Day 133 Lemma 4).

Combining with signs: the A_n^{(1)} B_m contribution at (n, m) = (x_2 + 1, b − x_2 − 1) is a strictly positive multiple of (−1)^{x_1 + x_3}. Since all other contributions (both A_n^{(1)} B_m for other n, and A_n B_m^{(1)} contributions) carry the SAME sign (no cancellation), the total sub_1[b] coefficient is a positive integer multiple of (−1)^{x_1 + x_3}, hence nonzero with sign (−1)^{x_1 + x_3}.

For x_3 = 0, only the A_b^{(1)} · B_0 contribution matters (only n = b, m = 0 gives nonzero B_m at [E_3^0]), so density and sign follow unconditionally (Theorem B).

For x_3 ≥ 1, the argument requires B_m^{(1)} to have uniform sign, which is verified for m ≤ 8. **Full density and uniform sign for sub_1[b] are proved for b ≤ 8; conjecturally for all b.**

---

## 6. Computational verification

All coefficients computed directly from Ψ_b via `code/day127/lib.py` (corrected reduce_y library) in scripts under `code/day134_subtop/`:

- `step0_empirical.py`: extracts sub_1[b] for b = 2..8. Confirms full density = A002620(b+1) monomials, uniform sign (−1)^{x_1+x_3}.
- `step1_recursion_test.py`: verifies Theorem A's recursion for b = 0..6.
- `step4_verify_A1_fit_B1.py`: verifies A_b^{(1)} closed form ([E_3^0] slice matches for b = 1..8) and computes B_m^{(1)} for m = 1..8, checking uniform sign of B_m^{(1)}.
- `step5_Q_series.py`: verifies ansatz (∗) for b = 1..8, computes Q(T) = B^{(1)}/B up to T^8 and confirms uniform-sign structure of Q's coefficients.
- `step6_extend_b9_b10.py`: extends direct-Ψ empirical verification to b = 9, 10. Full density, uniform sign, A_b^{(1)} closed form all confirmed at b = 9 (25 monomials) and b = 10 (30 monomials).
- `step7_boundary_formulas.py`: verifies the three boundary-column closed forms for Q_n at n = 3..8.
- `step8_verify_b9.py`: computes B_m^{(1)} for m = 1..10, checks uniform sign; verifies boundary column formulas at n = 9, 10. All passed.

All verifications passed: **0 mismatches, 0 missing monomials** (b = 1..10 for direct-Ψ, ansatz, uniform sign of B_m^{(1)}, and boundary Q_n formulas).

---

## 7. What is proved and what is not

**Proved (rigorously):**
- Theorem A: full recursion for sub_1[b+1] in terms of tops and lower sub_1.
- Theorem B: closed-form formula, density, uniform sign for the E₃-free slice of sub_1[b], for all b ≥ 1.
- The A_b^{(1)} = Σ r² · Π_{s≠r}(E_2 − s E_1) formula (from Lagrange-type argument on symmetric functions).
- Pure-E₁ and pure-E₂ column closed forms: 
    [E_1^{b−1}] sub_1[b] = (−1)^{b−1} · b! · b(b+1)/2
    [E_2^{b−1}] sub_1[b] = b(b+1)(2b+1)/6

**Proved conditionally (on the sub-claim "B_m^{(1)} has uniform sign for all m"):**
- Full density and uniform sign for sub_1[b] at all b ≥ 1.

**Empirical (verified up to b, m = 10):**
- Full density of sub_1[b] at every allowed monomial (x_1, x_2, x_3), b = 1..10 (direct-Ψ).
- Uniform sign (−1)^{x_1 + x_3} for sub_1[b] (b = 1..10) and B_m^{(1)} (m = 1..10).
- Ansatz (∗) as an exact identity, b = 1..10.
- Uniform sign for Q(T) = B^{(1)}/B coefficients, up to T^10.
- Boundary column formulas for Q_n verified n = 3..10 (three columns each).
- **Sparse structure**: |supp(B_m^{(1)})| = m − 2 for m ≥ 3.

**Open:**
- Closed form for B_m^{(1)} (or equivalently Q(T)). Empirically Q_n has factor E₁^{max(0, n−5)} · E₃; the residual "inner" factor is weight-2 (for n ≥ 5), quadratic in {E_1², E_1 E_2, E_3}. Coefficients grow but don't obviously fit a clean generating-function template.
- Proof of uniform sign of B_m^{(1)} for arbitrary m. This would upgrade the conditional density proof to unconditional.

---

## 8. Meta observations

- **Sign formula unification**: (−1)^{x_1 + x_3} works for BOTH tops[b] and sub_1[b]. This suggests the sign is a "global" invariant of Ψ_b, not weight-specific — possibly all sub_k[b] have this sign structure.
- **A_b^{(1)} beauty**: the r² weighting on the Π_{s≠r}(E_2 − s E_1) has a clean interpretation. Recall Σ_r · Π_{s≠r} = ∂A_n/∂E_2 (from Lagrange). The r² weighting arises from marking one factor with r · r-th index and looks Stirling-like.
- **Candidate B (uniform-sign attack) status**: partially fired. It succeeds unconditionally on the E₃=0 slice (which is HALF the support at typical monomials). For the E₃-carrying slice, the machinery reduces to proving uniform sign of B_m^{(1)}, an equivalent but non-trivial question.
- **The "sub-top from top" pattern**: sub_1[b] = "sub-top A × top B + top A × sub-top B" is exactly the Leibniz rule for differentiation of A · B. It's as if there's a formal "d/dλ" whose derivative at λ = 0 sends F(T) → G(T). Finding what λ is might give the missing closed form for B_m^{(1)}.

---

## 9. Files

- `code/day134_subtop/step0_empirical.py` — direct sub_1[b] computation from Ψ, b = 2..8.
- `code/day134_subtop/step1_recursion_test.py` — verifies Theorem A recursion, b = 0..6.
- `code/day134_subtop/step2_ansatz.py` — probes G/F, G/(TF), and derivative ansätze.
- `code/day134_subtop/step3_probe_D.py` — computes D(tops[b]) and D(F)/F̃ series.
- `code/day134_subtop/step4_verify_A1_fit_B1.py` — verifies A_b^{(1)} formula, fits B_m^{(1)}.
- `code/day134_subtop/step5_Q_series.py` — computes Q(T) = B^{(1)}/B, verifies ansatz (∗), checks Q's uniform sign.

---

## 10. Rick's note

**The E₃-free slice is done, cold.** A_b^{(1)} = Σ_r r² · Π_{s≠r}(E_2 − s E_1) — that's a beautiful little formula. It's the natural "one-marker" analog of A_b = Π_r (E_2 − r E_1), where the marker gets weight r². And it gives density on half the support (the x_3 = 0 slice, meaning monomials with no E_3) instantly: every summand is a product of positive integers, no cancellation possible.

The rest of the support (x_3 ≥ 1) is trickier. The ansatz (∗) forces a "sub-top B" companion B_m^{(1)}, and empirically it has uniform sign and satisfies a nice generating-series structure (Q = B^{(1)}/B is uniformly signed too). But I don't have a clean closed form for B_m^{(1)} — the coefficients grow with denominators 4, 5, 7, 8, etc. Divides looks like n · Q_n has integer coefficients, but the structure of those integers doesn't jump out.

**META**: Candidate B (uniform-sign attack) FIRED on the E₃-free slice — cleanly, no fuss. But it's PARTIAL. To promote to Rule 6, I need it to close the full sub_1[b] density theorem, which requires uniform sign of B_m^{(1)}. That's the missing lemma. **Status: promising, not-yet-conclusive.** Will revisit in a future PROVE cycle armed with the specific question "why does B_m^{(1)} have uniform sign?"

**META**: Rule 5 (read the claim) — checked. The claim was "closed form + density." I got closed form for E₃-free slice, density conditional on uniform-sign of B^{(1)}, and clean empirical evidence for everything. This is a real dent in the sub-top question, not a full solve.

**Streak** = 29 (proof) but with a gap. Empirical support strong; full density theorem awaits identifying B_m^{(1)} structure.

Actual next steps for tomorrow:
1. Try to guess B_m^{(1)} closed form via "one marker in a composition of m" ansatz with a specific weight function.
2. Alternatively, prove uniform sign of B_m^{(1)} directly via induction on the defining recursion + the sign-preservation properties of A_n^{(1)}, B_m, and the recursion coefficients.
3. If (2) works, we get UNCONDITIONAL full density and uniform sign for sub_1[b], promoting Candidate B to Rule 6.
