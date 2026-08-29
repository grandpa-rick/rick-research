# Day 133 — Full Density of tops[b] := Ψ(e_2^b)|_{top}

**Author.** Rick.
**Date.** 2026-08-25.
**Depends on.** Day 131 closed form F(T) = A(T)·B(T) (`2026-08-23-psi-e2-egf-closed-form.md`).

---

## 1. Statement

Let Ψ, e_2, and the (1,1,2)-grading on ℤ[E_1, E_2, E_3] be as in Day 131 (recap: w(E_1^a E_2^b E_3^c) = a + b + 2c). Set

  Ψ_b := Ψ(e_2^b) ∈ ℤ[E_1, E_2, E_3],  tops[b] := Ψ_b |_{w = b}.

**Theorem 1 (Full Density).** For every b ≥ 0 and every (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2 x_3 = b,

  [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b] ≠ 0.

Equivalently, supp(tops[b]) = {(x_1, x_2, x_3) : x_1 + x_2 + 2 x_3 = b}, whose size is ⌊(b+2)²/4⌋ = A002620(b + 2).

**Theorem 2 (Uniform sign).** In fact,

  sign([E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b]) = (−1)^{b − x_2 − x_3}.

**Theorem 3 (Closed form).** With m := b − n, k := x_3,

  [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b]  =  (−1)^{b − x_2 − x_3} · N(b; x_1, x_2, x_3),

where

  N(b; x_1, x_2, x_3)  :=  Σ_{n = x_2}^{b − 2 x_3}   C(b, n) · e_{n − x_2}(1, 2, …, n) · (m!/k!) · P(m, k),

and

  P(m, k)  :=  Σ_{(n_1,…,n_k) : n_i ≥ 2, Σ n_i = m}   Π_{i=1}^{k} (n_i² − 1)/n_i.

Every factor is a strictly positive rational whenever the summation range is nonempty; in particular N > 0. (For k = 0 use the convention P(0, 0) = 1, and only n = b contributes; for k ≥ 1 the range is nonempty iff x_1 ≥ 0, which holds by assumption.)

---

## 2. Setup: EGF coefficient extraction

Day 131 established F(T) := Σ_{b ≥ 0} tops[b] · T^b/b! = A(T) · B(T), with

  A(T) = (1 + E_1 T)^{E_2/E_1 − 1},
  B(T) = exp(E_3 · M(T)),
  M(T) = T / (E_1(1 + E_1 T)²)  −  log(1 + E_1 T) / E_1².

Write A(T) = Σ_n A_n T^n/n! and B(T) = Σ_m B_m T^m/m!. Then

  tops[b] = b! · [T^b] A(T) B(T) = Σ_{n + m = b} C(b, n) · A_n · B_m.  (★)

**Lemma 1 (A_n, closed form).** A_n = Π_{r=1}^n (E_2 − r · E_1).

*Proof.* Let α := E_2/E_1 − 1. Generalized binomial expansion:

  A(T) = (1 + E_1 T)^{α} = Σ_{n ≥ 0} (1/n!) · Π_{j=0}^{n−1} (α − j) · (E_1 T)^n.

So A_n = n! · [T^n] A(T) = Π_{j=0}^{n−1} (α − j) · E_1^n. Since (α − j) · E_1 = E_2 − (j + 1) E_1, distributing one factor of E_1 into each parenthesis:

  A_n = Π_{j=0}^{n−1} ((α − j) · E_1) = Π_{j=0}^{n−1} (E_2 − (j + 1) E_1) = Π_{r=1}^{n} (E_2 − r E_1). ∎

**Lemma 2 (M(T), coefficient form).** M(T) = Σ_{n ≥ 2} μ_n E_1^{n−2} T^n, with

  μ_n = (−1)^{n − 1} · (n² − 1)/n.

*Proof.* From T/(1 + E_1 T)² = Σ_{n ≥ 1} (−1)^{n−1} n (E_1 T)^n / E_1, dividing by E_1 gives T/(E_1 (1 + E_1 T)²) = Σ_{n ≥ 1} (−1)^{n−1} n · E_1^{n−2} · T^n. From log(1 + E_1 T)/E_1² = Σ_{n ≥ 1} (−1)^{n−1} · (1/n) · E_1^{n−2} T^n. Subtracting yields μ_n = (−1)^{n−1} (n − 1/n) = (−1)^{n−1} (n² − 1)/n. Since μ_1 = 0 by cancellation, the sum ranges over n ≥ 2. ∎

**Remark.** For n ≥ 2, sign(μ_n) = (−1)^{n−1} and |μ_n| = (n² − 1)/n > 0. Numerical values: μ_2 = −3/2, μ_3 = 8/3, μ_4 = −15/4, μ_5 = 24/5. (The PROVE.md line 56 sample list had μ_2 = 3/2 and μ_3 = −8/3, which is a sign-flip typo relative to the correct formula on line 54.)

---

## 3. A_n: coefficient of E_1^{n−x_2} E_2^{x_2}

**Lemma 3.** For 0 ≤ x_2 ≤ n,

  [E_1^{n − x_2} E_2^{x_2}] A_n  =  (−1)^{n − x_2} · e_{n − x_2}(1, 2, …, n),

where e_j denotes the j-th elementary symmetric polynomial. This is nonzero, of sign (−1)^{n − x_2}, and of positive integer magnitude e_{n−x_2}(1,…,n) ≥ 1.

*Proof.* A_n = Π_{r=1}^{n} (E_2 − r E_1). To extract E_2^{x_2}, choose the E_2-summand from x_2 of the factors and the −r E_1 summand from the remaining j := n − x_2 factors. Summing over all size-j subsets S ⊆ {1, …, n}:

  [E_1^{j} E_2^{x_2}] A_n = Σ_{|S| = j} Π_{r ∈ S} (−r) = (−1)^j · Σ_{|S| = j} Π_{r ∈ S} r = (−1)^{n − x_2} · e_{n − x_2}(1, …, n). ∎

**Remark.** e_j(1, …, n) is the (unsigned) coefficient of x^{n − j} in (x + 1)(x + 2)…(x + n), equivalently a Stirling number of the first kind. It is a *strictly positive integer* for 0 ≤ j ≤ n. In particular, for x_2 = n, we have e_0 = 1 (empty product), and for x_2 = 0, we have e_n(1, …, n) = n!.

---

## 4. B_m: coefficient of E_1^{m − 2k} E_3^{k}

**Lemma 4.** For k ≥ 1 and m ≥ 2k,

  [E_1^{m − 2k} E_3^{k}] B_m  =  (−1)^{m − k} · (m! / k!) · P(m, k),

where

  P(m, k) := Σ_{(n_1, …, n_k) : n_i ≥ 2, Σ n_i = m} Π_{i} (n_i² − 1)/n_i

is a sum of strictly positive rationals. In particular, P(m, k) > 0 whenever m ≥ 2k (since (n_1, …, n_k) = (2, …, 2, m − 2(k−1)) is always a valid composition when m ≥ 2k). For k = 0, [E_1^{m} E_3^{0}] B_m = δ_{m, 0}.

*Proof.* By definition B_m = m! · [T^m] B(T) and B(T) = Σ_{k ≥ 0} E_3^k · M(T)^k / k!. Hence

  [E_3^k] B_m / m!  =  [T^m] M(T)^k / k!.

Compute [T^m E_1^{m − 2k}] M(T)^k. Since M(T) = Σ_{n ≥ 2} μ_n E_1^{n − 2} T^n, taking the k-fold product,

  M(T)^k  =  Σ_{(n_1, …, n_k), n_i ≥ 2} Π μ_{n_i} · E_1^{Σ (n_i − 2)} · T^{Σ n_i}.

The T^m coefficient collects (n_1, …, n_k) with Σ n_i = m; the E_1-degree is then m − 2k automatically. So

  [T^m E_1^{m − 2k}] M(T)^k  =  Σ_{compositions} Π_i μ_{n_i}.

By Lemma 2, μ_{n_i} = (−1)^{n_i − 1} · |μ_{n_i}| with |μ_{n_i}| = (n_i² − 1)/n_i > 0. Therefore

  Π μ_{n_i}  =  (−1)^{Σ (n_i − 1)} · Π (n_i² − 1)/n_i  =  (−1)^{m − k} · [strictly positive rational].

The overall sign (−1)^{m − k} is INDEPENDENT of the composition, so all summands share the same sign. Multiplying by m!/k! yields the claim.

For the k = 0 case, M(T)^0 = 1, so [T^m] M(T)^0 = δ_{m, 0}, whence [E_3^0 E_1^m] B_m = δ_{m, 0}. ∎

---

## 5. Combining: the uniform-sign proof

**Proof of Theorems 1, 2, 3.**

Fix b ≥ 0 and (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2 x_3 = b. Write k := x_3.

By (★) and the previous lemmas, the coefficient of E_1^{x_1} E_2^{x_2} E_3^{x_3} in tops[b] is:

  Σ_{n + m = b}  C(b, n) · [E_1^{n − x_2} E_2^{x_2}] A_n · [E_1^{m − 2k} E_3^{k}] B_m.

For the summand to be nonzero we need (from Lemma 3) x_2 ≤ n, and (from Lemma 4) either (k = 0 ∧ m = 0) or (k ≥ 1 ∧ m ≥ 2k). Let I be the set of n giving nonzero summands:

  I = {b}                       if k = 0  (from k = 0, m = 0 forcing n = b),
  I = {x_2, x_2 + 1, …, b − 2k}  if k ≥ 1  (from x_2 ≤ n and m = b − n ≥ 2k).

In either case I is nonempty: for k = 0, {b} is nonempty; for k ≥ 1, the interval endpoints satisfy x_2 ≤ b − 2k ⇔ x_1 = b − x_2 − 2k ≥ 0, which holds by assumption.

For each n ∈ I, set m := b − n. Apply Lemmas 3 and 4:

  contribution(n)  =  C(b, n) · (−1)^{n − x_2} e_{n − x_2}(1, …, n) · (−1)^{m − k} (m!/k!) P(m, k)
                   =  (−1)^{n − x_2 + m − k} · [strictly positive]
                   =  (−1)^{(n + m) − x_2 − k} · [strictly positive]
                   =  (−1)^{b − x_2 − x_3} · [strictly positive].    (†)

**Crucially, the sign is INDEPENDENT of n.** Every summand carries the same sign (−1)^{b − x_2 − x_3}.

Sum over n ∈ I:

  [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b]  =  (−1)^{b − x_2 − x_3} · N(b; x_1, x_2, x_3),

with

  N(b; x_1, x_2, x_3)  :=  Σ_{n ∈ I} C(b, n) · e_{n − x_2}(1, …, n) · (m!/k!) · P(m, k)  >  0,

the strict inequality because I is nonempty and every summand is strictly positive:
- C(b, n) is a positive integer.
- e_{n − x_2}(1, …, n) is a positive integer for 0 ≤ n − x_2 ≤ n.
- m!/k! is a positive integer for m ≥ k.
- P(m, k) > 0 for m ≥ 2k (Lemma 4); P(0, 0) = 1 by convention.

This proves Theorems 1, 2, 3. ∎

---

## 6. Corollaries

### 6.1 Pure-E_1 corner

For x_1 = b, x_2 = x_3 = 0: only n = b contributes (since k = 0). N = C(b, b) · e_b(1, …, b) · 1 · 1 = 1 · b! · 1 · 1 = b!. Sign (−1)^{b − 0 − 0} = (−1)^b.

  **[E_1^b] tops[b] = (−1)^b · b!.**

### 6.2 Pure-E_2 corner

For x_2 = b, x_1 = x_3 = 0: only n = b contributes; e_0(1, …, b) = 1. N = 1.

  **[E_2^b] tops[b] = 1.**

### 6.3 Pure-E_3 corner (even b)

For b = 2ℓ, x_3 = ℓ, x_1 = x_2 = 0: I = {0}, so only n = 0 contributes. Then m = b, k = ℓ, and P(b, ℓ) picks up compositions of b into ℓ parts each ≥ 2. Since the minimum sum with ℓ parts ≥ 2 is 2ℓ = b, the ONLY composition is (2, 2, …, 2). Hence

  P(b, ℓ) = Π_{i=1}^{ℓ} (4 − 1)/2 = (3/2)^ℓ.

Compute N: C(b, 0) · e_0() · (b!/ℓ!) · (3/2)^ℓ = (b!/ℓ!) · 3^ℓ / 2^ℓ. But 2^ℓ · ℓ! = b!! (double factorial for even b), and b! / b!! = (b − 1)!!, so

  N = 3^ℓ · (b − 1)!!.

Sign (−1)^{b − 0 − ℓ} = (−1)^{ℓ} (since b = 2ℓ). Therefore

  **[E_3^{b/2}] tops[b]  =  (−3)^{b/2} · (b − 1)!!    for even b.**

Verification: b = 2: −3 · 1 = −3 ✓. b = 4: 9 · 3 = 27 ✓. b = 6: −27 · 15 = −405 ✓. b = 8: 81 · 105 = 8505 ✓. b = 10 predicted: −243 · 945 = −229 635. All match direct expansion of A(T)B(T) (see `day133_density/verify_e3_column.py`).

### 6.4 Full support and count

The support of tops[b] as a polynomial in ℤ[E_1, E_2, E_3] equals {(x_1, x_2, x_3) ∈ ℤ_{≥0}^3 : x_1 + x_2 + 2 x_3 = b}. Its cardinality is Σ_{k = 0}^{⌊b/2⌋} (b − 2k + 1) = ⌊(b + 2)²/4⌋ = A002620(b + 2).

---

## 7. Computational verification

All claims verified in `/home/agent/projects/beta-prime/code/day133_density/`:

- `verify_signs.py`: recomputes tops[b] from A(T)·B(T) for b = 0..8, checks that every monomial in every tops[b] has sign exactly (−1)^{b − x_2 − x_3}. Result: **zero mismatches, zero missing monomials**. Also reproduces sanity-check values [E_1^b] = (−1)^b b!, [E_2^b] = 1, and [E_3^{b/2}] values 27, −405, 8505 for b = 4, 6, 8. Independently re-run and extended in Day-133 deep-work: b = 9..12 also fully dense with uniform sign (36, 42, 49 nonzero monomials matching A002620(b+2)). Zero failures.

- `verify_individual.py`: for b = 2..7 and every monomial (x_1, x_2, x_3), computes each (n, m)-contribution to the coefficient using Lemmas 3 and 4, and checks that (i) every individual contribution has sign (−1)^{b − x_2 − x_3}, and (ii) the sum matches the value computed directly from A(T)·B(T). Result: **zero mismatches** across all monomials and all decompositions.

- `verify_e3_column.py`: checks the closed form [E_3^{b/2}] tops[b] = (−3)^{b/2} · (b − 1)!! against empirical values for b ∈ {2, 4, 6, 8}. All match.

---

## 8. What this closes

- **Full Density Theorem** for Ψ(e_2^b)|_top (Theorem 1). Every allowed monomial appears with nonzero coefficient — no cancellations, ever.
- **Uniform Sign Theorem** (Theorem 2). The sign is combinatorially explicit: (−1)^{b − x_2 − x_3}.
- **Explicit closed-form coefficient formula** (Theorem 3). Every top coefficient is a *positive-summand* rational combination whose sign is determined a priori.
- **Boundary closed forms** (Corollaries 6.1–6.3). Pure-E_1, pure-E_2, and pure-E_3 columns admit particularly clean expressions; the pure-E_3 formula (−3)^{b/2} (b−1)!! generalizes Rick's day-132 pattern (27, −405, 8505, …) to all even b.

Combined with the Day 131 closed form F(T) = A(T)·B(T), this **settles the entire structure of tops[b]**: it is a fully-supported (1,1,2)-weight-b polynomial with a totally explicit coefficient formula.

---

## 9. What this does NOT close

- Extension to Ψ(e_r^b) for r ≠ 2. Separate PROVE cycle needed; but the shift-ODE approach should generalize once the analog of Lemma K5 (Q(e_r, V)/V = something clean) is nailed.
- The atom itself (Ψ_b, not just tops[b]) has the same support-shape at lower weights (empirically). Density at *sub-top* weight is a separate question — one that the shift-ODE does not immediately address.
- Interpretation. The uniform sign (−1)^{b − x_2 − x_3} demands a combinatorial or representation-theoretic explanation. Why does the parity of x_1 (= b − x_2 − 2x_3, so has same parity as b − x_2) control the coefficient sign? Feels like a Möbius / sign-reversing involution should be lurking. Not addressed here.

---

## 10. Rick's note

Uniform sign. The whole thing collapses on ONE observation: each factor μ_n has a monotone-in-n sign, so a product of μ_{n_i}'s has sign (−1)^{Σ (n_i − 1)} = (−1)^{m − k}, and this is IDENTICAL to the sign of the A_n coefficient (−1)^{n − x_2} when summed with n + m = b. The sign patterns are *cofibrant* — every decomposition of b is aligned. That's why the empirical pattern was so clean: there was never any cancellation to worry about, just a sum of positive terms with a global sign.

The A(T)·B(T) factorization from Day 131 wasn't just "a closed form" — it was the *canonical* factorization that separates the (1,1)-Stirling data (A) from the E_3-composition data (B), each carrying its own alternating sign, and the products aligning to give uniform sign globally. That's a real structural theorem, not just a compact reformulation.

Also: **[E_3^{b/2}] tops[b] = (−3)^{b/2} (b−1)!!** is a beautiful little closed form. That double-factorial-with-signed-power appears NATURALLY here — one composition, one product, done. If someone asked me to guess this coefficient without the closed form, I'd probably have gone hunting through OEIS. Instead the machinery drops it out.

Streak = 29.
