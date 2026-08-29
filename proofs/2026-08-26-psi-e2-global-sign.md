# Day 136 — Ψ(e_2^b) global uniform sign invariant

**Author.** Rick.
**Date.** 2026-08-26.
**Depends on.** Day 131 Ψ-recursion + σ (`2026-08-23-psi-e2-egf-closed-form.md`).
**Companion code.** `/home/agent/projects/beta-prime/code/day136_global_sign/`.

---

## 1. Statement

Let Ψ, e_2, and the (1,1,2)-grading on ℤ[E_1, E_2, E_3] be as in Day 131. Set

  Ψ_b := Ψ(e_2^b) ∈ ℤ[E_1, E_2, E_3].

**Theorem (Ψ_b-global uniform sign).** For every b ≥ 0 and every monomial E_1^{x_1} E_2^{x_2} E_3^{x_3} appearing with nonzero coefficient in Ψ_b,

  sign([E_1^{x_1} E_2^{x_2} E_3^{x_3}] Ψ_b) = (−1)^{x_1 + x_3}.

Equivalently: the sign of every nonzero coefficient of Ψ_b is a function of (x_1, x_2, x_3) that is independent of b and of the weight slice x_1 + x_2 + 2 x_3.

*Prior status (Day 135).* Confirmed empirically for b = 2, …, 10 (597 nonzero coefficients, zero mismatches). Established rigorously only on the top-weight slice (Day 133) and on the E_3-free sub-top slice (Day 134). The general case was open.

---

## 2. The φ-reformulation

Let φ : ℤ[E_1, E_2, E_3] → ℤ[E_1, E_2, E_3] be the ring involution defined on generators by

  φ(E_1) = −E_1,   φ(E_2) = E_2,   φ(E_3) = −E_3.

Note that φ is an involution (φ² = id).

**Lemma 2.1 (sign ⇔ nonnegativity).** For any P ∈ ℤ[E_1, E_2, E_3],

  every nonzero coeff of P has sign (−1)^{x_1+x_3}    ⇔    every coeff of φ(P) is ≥ 0.

*Proof.* [E_1^{x_1} E_2^{x_2} E_3^{x_3}] φ(P) = (−1)^{x_1+x_3} · [E_1^{x_1} E_2^{x_2} E_3^{x_3}] P. Multiplying a real number by the sign that ought to appear yields a nonnegative value iff the original sign was correct (or the coeff was zero). ∎

**Setup.** Define P_b := φ(Ψ_b). The Theorem is equivalent to:

**Reformulated Theorem.** For every b ≥ 0, all coefficients of P_b are nonnegative.

The proof below proves the Reformulated Theorem.

---

## 3. The conjugate operator τ := φ ∘ σ ∘ φ

Recall σ : E_1 ↦ E_1 − 3, E_2 ↦ E_2 − 2E_1 + 3, E_3 ↦ E_3 − E_2 + E_1 − 1 (ring endomorphism; Day 131 §3.2). Define τ := φ ∘ σ ∘ φ, again a ring endomorphism.

**Lemma 3.1 (τ on generators).**

  τ(E_1) = E_1 + 3
  τ(E_2) = 2 E_1 + E_2 + 3
  τ(E_3) = E_1 + E_2 + E_3 + 1

*Proof.* Direct computation:
- τ(E_1) = φ(σ(−E_1)) = φ(−(E_1 − 3)) = φ(−E_1 + 3) = E_1 + 3.
- τ(E_2) = φ(σ(E_2)) = φ(E_2 − 2E_1 + 3) = E_2 + 2E_1 + 3.
- τ(E_3) = φ(σ(−E_3)) = φ(−(E_3 − E_2 + E_1 − 1)) = φ(−E_3 + E_2 − E_1 + 1) = E_3 + E_2 + E_1 + 1. ∎

**Lemma 3.2 (τ preserves nonnegativity).** If Q ∈ ℤ[E_1, E_2, E_3] has all nonneg coefficients, so does τ(Q).

*Proof.* τ is a ring homomorphism sending each generator to a polynomial with nonnegative integer coefficients (Lemma 3.1). Hence for any monomial E_1^{a_1} E_2^{a_2} E_3^{a_3}, τ(E_1^{a_1} E_2^{a_2} E_3^{a_3}) = τ(E_1)^{a_1} τ(E_2)^{a_2} τ(E_3)^{a_3} is a product of polynomials with nonneg coefficients, hence has nonneg coefficients. Extending by linearity: if Q = Σ c_α · monomial_α with c_α ≥ 0, then τ(Q) = Σ c_α · τ(monomial_α) is a nonneg-coefficient combination of nonneg polynomials. ∎

**Compatibility with σ.** From τ = φσφ and φ² = id: φ ∘ σ = τ ∘ φ, i.e. φ(σ(X)) = τ(φ(X)) for all X.

---

## 4. The φ-transformed Ψ-recursion

The Ψ-recursion (Day 131, proved for all b ≥ 0, with Ψ_c := 0 for c < 0):

  Ψ_{b+1} = [E_2 − (b+1) E_1 + (b+1)²] · Ψ_b − 3b · E_3 · σ(Ψ_{b−1}) − b(b−1)(E_1 − 2b − 2) · E_3 · σ(Ψ_{b−2})    (★)

Apply φ to both sides. Since φ is a ring homomorphism and φ(σ(Ψ_c)) = τ(P_c):

- φ([E_2 − (b+1)E_1 + (b+1)²]) = E_2 + (b+1) E_1 + (b+1)².
- φ(−3b · E_3) = 3b · E_3.
- φ(−b(b−1)(E_1 − 2b − 2) · E_3) = −b(b−1) · φ(E_1 − 2b − 2) · φ(E_3) = −b(b−1)(−E_1 − 2b − 2)(−E_3) = −b(b−1)(E_1 + 2b + 2) · E_3.

Thus:

**φ-recursion.** For all b ≥ 0,

  P_{b+1} = [E_2 + (b+1)E_1 + (b+1)²] · P_b + 3b · E_3 · τ(P_{b−1}) − b(b−1)(E_1 + 2b + 2) · E_3 · τ(P_{b−2}).    (♥)

*Note.* The first two summands manifestly preserve nonnegativity; the third — the only obstruction to a naive term-by-term induction — is negative. The remainder of the proof shows that terms 2 and 3 combine into an object that is itself nonnegative.

---

## 5. The auxiliary polynomial Q_b

Define, for b ≥ 1,

  Q_b := 3 · τ(P_{b−1}) − (b−1)(E_1 + 2b + 2) · τ(P_{b−2}).    (Q-def)

(Conventions: P_c := 0 for c < 0, so Q_1 = 3 · τ(P_0) = 3.)

**Lemma 5.1 (P-recursion refactoring).** For all b ≥ 0,

  P_{b+1} = [E_2 + (b+1)E_1 + (b+1)²] · P_b + b · E_3 · Q_b.    (P-rec)

*Proof.* Factor b out of terms 2 and 3 of (♥):
  3b · τ(P_{b−1}) − b(b−1)(E_1 + 2b + 2) · τ(P_{b−2}) = b · [3 · τ(P_{b−1}) − (b−1)(E_1 + 2b + 2) · τ(P_{b−2})] = b · Q_b.
At b = 0 the summand is 0 regardless of Q_0 (which is undefined/irrelevant). ∎

**Lemma 5.2 (Q-recursion).** For all b ≥ 2,

  Q_b = [(2b + 4) E_1 + 3 E_2 + b² + 3b + 5] · τ(P_{b−2}) + 3(b − 2)(E_1 + E_2 + E_3 + 1) · τ(Q_{b−2}).    (Q-rec)

*Proof.* Apply the P-recursion (P-rec) at index b − 2 (valid since b ≥ 2, so b − 2 ≥ 0):

  P_{b−1} = [E_2 + (b−1) E_1 + (b−1)²] · P_{b−2} + (b − 2) · E_3 · Q_{b−2}.

Apply τ (ring hom):

  τ(P_{b−1}) = τ([E_2 + (b−1)E_1 + (b−1)²]) · τ(P_{b−2}) + (b − 2) · τ(E_3) · τ(Q_{b−2}).

Compute the first coefficient using Lemma 3.1:
  τ(E_2) + (b−1) · τ(E_1) + (b−1)² · τ(1)
   = (2 E_1 + E_2 + 3) + (b−1)(E_1 + 3) + (b−1)²
   = (b + 1) E_1 + E_2 + [3 + 3(b−1) + (b−1)²]
   = (b + 1) E_1 + E_2 + (b² + b + 1).
The bracket simplification: 3 + 3(b−1) + (b−1)² = 3 + 3b − 3 + b² − 2b + 1 = b² + b + 1.

And τ(E_3) = E_1 + E_2 + E_3 + 1.

So:

  τ(P_{b−1}) = [(b+1)E_1 + E_2 + (b² + b + 1)] · τ(P_{b−2}) + (b − 2)(E_1 + E_2 + E_3 + 1) · τ(Q_{b−2}).    (☆)

Substitute (☆) into (Q-def):

  Q_b = 3 · [(b+1)E_1 + E_2 + (b² + b + 1)] · τ(P_{b−2}) + 3(b − 2)(E_1 + E_2 + E_3 + 1) · τ(Q_{b−2}) − (b−1)(E_1 + 2b + 2) · τ(P_{b−2}).

Collect the coefficient of τ(P_{b−2}):

  3(b+1)E_1 + 3 E_2 + 3(b² + b + 1) − (b−1)(E_1 + 2b + 2)
    = [3(b+1) − (b−1)] E_1 + 3 E_2 + [3(b² + b + 1) − (b−1)(2b + 2)]
    = (2b + 4) E_1 + 3 E_2 + [3b² + 3b + 3 − 2(b² − 1)]
    = (2b + 4) E_1 + 3 E_2 + [b² + 3b + 5].

This yields (Q-rec). ∎

**Remark 5.3.** At b = 2, the right-hand side of (Q-rec) evaluates to [8E_1 + 3E_2 + 15] · τ(P_0) + 0 = 8E_1 + 3E_2 + 15, matching the direct evaluation Q_2 = 3 · τ(P_1) − (E_1 + 6) · τ(P_0) = 3(3E_1 + E_2 + 7) − (E_1 + 6) = 8E_1 + 3E_2 + 15.

---

## 6. The main theorem: simultaneous induction on P and Q

**Theorem.** For every b ≥ 0, P_b has nonnegative coefficients. For every b ≥ 1, Q_b has nonnegative coefficients.

*Proof.* Strong induction on b, proving both statements simultaneously.

**Base cases (direct evaluation).**
- P_0 = φ(Ψ_0) = φ(1) = 1. Nonneg. ✓
- P_1 = φ(Ψ_1) = φ(−E_1 + E_2 + 1) = E_1 + E_2 + 1. Nonneg. ✓
- Q_1 = 3 · τ(P_0) − 0 · (…) = 3 · 1 = 3. Nonneg. ✓
- Q_2 = [8E_1 + 3E_2 + 15] (Remark 5.3). Nonneg. ✓

**Inductive step.** Let b ≥ 1 and assume P_c ≥ 0 for all 0 ≤ c ≤ b and Q_c ≥ 0 for all 1 ≤ c ≤ b. We show P_{b+1} ≥ 0, and if b + 1 ≥ 2, Q_{b+1} ≥ 0.

*P_{b+1} nonneg.* By (P-rec),
  P_{b+1} = [E_2 + (b+1)E_1 + (b+1)²] · P_b + b · E_3 · Q_b.
The coefficient polynomials E_2 + (b+1)E_1 + (b+1)² and b · E_3 have nonneg coefficients (b + 1 ≥ 1, b ≥ 1). P_b ≥ 0 and Q_b ≥ 0 by IH. Product and sum of polynomials with nonneg coefficients have nonneg coefficients. ∴ P_{b+1} ≥ 0.

*Q_{b+1} nonneg (for b + 1 ≥ 2, i.e. b ≥ 1).* By (Q-rec) at index b + 1,
  Q_{b+1} = [(2(b+1) + 4) E_1 + 3 E_2 + (b+1)² + 3(b+1) + 5] · τ(P_{b−1}) + 3((b+1) − 2)(E_1 + E_2 + E_3 + 1) · τ(Q_{b−1}).

- The E_1-, E_2-, constant-coefficient polynomial [(2b + 6) E_1 + 3 E_2 + (b² + 5b + 9)] has all nonneg coefficients (b + 1 ≥ 2 gives positive constant and E_1-coeff).
- The scalar 3(b − 1) ≥ 0 (using b ≥ 1); and (E_1 + E_2 + E_3 + 1) has nonneg coefficients.
- P_{b−1} ≥ 0 and Q_{b−1} ≥ 0 by IH; for b − 1 = 0, P_0 = 1 ≥ 0 and the coefficient 3(b − 1) = 0 kills the Q_{b−1} term (so Q_0 need not be defined).
- τ preserves nonnegativity (Lemma 3.2).

Product and sum of nonneg polynomials are nonneg. ∴ Q_{b+1} ≥ 0.

By induction, P_b ≥ 0 for all b ≥ 0 and Q_b ≥ 0 for all b ≥ 1. ∎

**Corollary (Ψ_b-global uniform sign).** For every b ≥ 0 and every monomial E_1^{x_1} E_2^{x_2} E_3^{x_3} appearing with nonzero coefficient in Ψ_b,
  sign([E_1^{x_1} E_2^{x_2} E_3^{x_3}] Ψ_b) = (−1)^{x_1 + x_3}. ∎

---

## 7. Corollaries and remarks

### 7.1 The sign function is a Ψ_b-global invariant

The result subsumes and unifies:
- Day 133 (top-weight): sign(coeff at top) = (−1)^{b − x_2 − x_3} = (−1)^{x_1 + x_3}, since at top x_1 + x_2 + 2 x_3 = b implies x_1 = b − x_2 − 2 x_3 ≡ b − x_2 (mod 2), so (−1)^{b−x_2−x_3} = (−1)^{x_1 + x_3}.
- Day 134 (sub-top E_3-free): sign = (−1)^{x_1} = (−1)^{x_1 + x_3}, since x_3 = 0.
- Day 135 (full-support empirical to b ≤ 10): now proved unconditionally.

### 7.2 Structural reading

The proof's crux is that the Ψ-recursion, when viewed through the involution φ, has a NEGATIVE term that can be absorbed once and for all into an auxiliary quantity Q_b whose OWN recursion (arising from re-invoking the P-recursion inside) has only nonneg coefficients. The essential magic is:

  3(b+1) − (b−1) = 2b + 4 ≥ 0        (E_1-coefficient survives with correct sign)
  3(b² + b + 1) − 2(b² − 1) = b² + 3b + 5 ≥ 0     (constant survives)

Both cancellations are polynomial in b with strictly positive residue for all b ≥ 0. The proof is thus a "polynomial-magnitude" argument dressed up in a bootstrap: one round of unfolding the P-recursion inside the definition of Q_b creates enough positive contribution to swamp the negative term.

### 7.3 τ = φσφ is the "right" endomorphism

Whereas σ (a ring endomorphism whose values on generators have mixed signs) is hard to analyze for sign-preservation, its conjugate τ = φσφ has

  τ(E_1) = E_1 + 3,  τ(E_2) = 2E_1 + E_2 + 3,  τ(E_3) = E_1 + E_2 + E_3 + 1,

i.e., all generators mapped to polynomials with strictly positive coefficients. Hence τ is manifestly nonneg-preserving (Lemma 3.2). This drops the L5 lemma (Day 135) from "requires multinomial parity accounting" to "one-line observation." This is a Rick-level punchline: the sign obstacle in σ was an artifact of choosing coordinates; τ = φσφ is the right coordinate.

### 7.4 Density (STRETCH goal — NOT proved here)

The Theorem shows every nonzero coefficient of Ψ_b has the predicted sign, but does NOT show all allowed monomials have nonzero coefficient (density). Empirically (Day 135), Ψ_b is fully supported for b ≤ 10, but a proof requires showing no cancellation to zero — the recursions (P-rec) and (Q-rec) both compose nonnegative contributions, so a zero coefficient at some position would require all summands to contribute zero there simultaneously. This is a natural extension and left for a future PROVE cycle.

### 7.5 Boundary cases

- b = 0: Ψ_0 = 1, P_0 = 1 ≥ 0. ✓
- b = 1: Ψ_1 = −E_1 + E_2 + 1, P_1 = E_1 + E_2 + 1 ≥ 0, sign of Ψ_1 coefficients: (−E_1: −), (E_2: +), (const: +) matching (−1)^{x_1+x_3}: (E_1: −, E_2: +, const: +). ✓

---

## 8. Computational verification

All statements verified in `/home/agent/projects/beta-prime/code/day136_global_sign/`:

- `verify_phi_recursion.py`: verifies (♥) and the original Ψ-recursion for b = 2..7; confirms P_b ≥ 0 for b = 0..7.
- `test_magnitude_lemma.py`: verifies Q_b ≥ 0 for b = 1..8 and the refactoring P_{b+1} = [E_2 + (b+1)E_1 + (b+1)²] · P_b + b · E_3 · Q_b.
- `test_Q_recursion.py`: verifies (Q-rec) for b = 2..8 as an exact polynomial identity.
- `verify_extended.py`: extends verification to b = 0..11.

Empirical prior verification of the sign invariant itself: `day135_sub2_sign/verify_all_slices.py` — 597 coefficients across b = 2..10, zero mismatches.

---

## 9. What this closes

- **Ψ_b-global uniform sign theorem** (Day 133 → 134 → 135 empirical → 136 proved).
- **FPSAC §6**: promotes the top-only sign result to a Ψ-global statement. The paper title Ψ(e_2^b) can now be "Density and Ψ-global uniform sign for Ψ(e_2^b)."
- **META_STACK Candidate B (uniform-sign attack)** — now closed as **Rule 6**. The technique fires three times: Day 133 (tops via A·B factorization), Day 134 partial (sub-top E_3-free), Day 136 (all slices via φ-conjugation + auxiliary bootstrap).
- **λ-deformation program**: no longer needed for the FPSAC paper. The direct-recursion proof supersedes the deformation guess.
- **L5 (σ preserves the invariant)** dissolved into a one-line observation about τ = φσφ.

---

## 10. Rick's note

**The move is φ.** Everything else follows once you conjugate by the sign involution.

The original σ has σ(E_1) = E_1 − 3 (negative shift), σ(E_2) = E_2 − 2E_1 + 3 (mixed), σ(E_3) = E_3 − E_2 + E_1 − 1 (mixed). Trying to prove nonnegativity of coefficients under σ-action is a nightmare of sign-tracking — Day 135 needed a multinomial parity computation over three separate multinomial expansions just to show σ preserves the invariant.

But conjugate σ by φ: E_i → (−1)^{x_1+x_3}-symmetric involution. You get τ(E_1) = E_1+3, τ(E_2) = 2E_1+E_2+3, τ(E_3) = E_1+E_2+E_3+1. **All nonneg coefficients on the generators.** τ is manifestly a "positive" ring endomorphism, no accounting required. That kills L5 in one line.

Then the φ-transformed Ψ-recursion has three terms: two manifestly positive, one negative. The one negative term is b(b−1)(E_1+2b+2)·E_3·τ(P_{b−2}). Combine it with the previous term (3b·E_3·τ(P_{b−1})) into an auxiliary quantity Q_b. Prove Q_b ≥ 0 by ITS OWN recursion, derived by unfolding P_{b−1} once inside. The unfolding produces exactly enough positive contribution to swamp the negative — and the residual coefficients are polynomially strictly positive in b:

  3(b + 1) − (b − 1) = 2b + 4          ← E_1 coeff (positive for all b ≥ 0)
  3(b² + b + 1) − 2(b² − 1) = b² + 3b + 5   ← constant coeff (positive for all b ≥ 0)

Both are Q_b's "own recursion coefficients" showing the same pattern: enough positive contribution to eat the negative. That's the whole proof.

**Meta lesson.** Sign obstructions can be COORDINATE ARTIFACTS. Before doing hard sign-tracking, ask: is there an involution I can conjugate by that turns everything positive? If yes, the "hard" sign proof reduces to plain nonnegativity.

**Streak** = 30. Full sign theorem CLOSED. The uniform-sign attack (Candidate B) is now a promoted rule — Rule 6.
