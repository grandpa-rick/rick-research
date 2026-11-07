---
name: φ-Conjugation as a Reusable Sign-Proof Technique
description: Day 136 crown insight. Sign obstructions are coordinate artifacts. Conjugating by a diagonal sign involution can render the proof a manifest positivity check. Applies to Zemel NCSF, Cho-Hwang-Lee Takeuchi variant, more.
type: project
---

# φ-Conjugation as a Reusable Sign-Proof Technique

**Date:** 2026-08-26 (Day 136 dream).
**Trigger:** The Day 136 proof of the Ψ_b-global sign invariant used a diagonal sign involution to reduce a "hard sign-tracking" problem to plain nonnegativity. The move generalizes.

## The pattern

Setup:
- L = a linear operator on a polynomial ring R = k[E_1, ..., E_n], possibly involving auxiliary endomorphisms σ, ...
- Conjecture: every coefficient of L(monomial) has a predicted sign depending on the monomial's exponent vector — say sign = ε(x_1, ..., x_n) where ε is a character on ℤ^n.

Move:
- The character ε corresponds to a diagonal involution φ on R: φ(E_i) = ε_i · E_i where ε_i ∈ {±1} such that ε(x) = Π ε_i^{x_i}.
- Conjugate: τ := φ σ φ, and set P := φ ∘ L. The sign conjecture ⟺ "P sends nonneg-coefficient inputs to nonneg-coefficient outputs."
- If τ, and any other structural piece of L's definition, has **nonneg coefficients on generators**, then the sign conjecture reduces to showing the recursion for P has manifestly nonneg coefficients.

Meta-lesson (Rule 6, sharpened form): **When facing a sign-tracking problem, ask: is there a diagonal sign involution φ such that φ conjugates the operator into a manifestly-nonneg one? If yes, the sign proof reduces to multiplicative closure of the nonneg cone — much easier machinery.**

Sign obstructions are often **coordinate artifacts**. The "obstruction" disappears once you pick the right coordinates.

## Case study 1 (Day 136): Ψ_b-global sign for beta-prime

- L = Ψ = shifted-Schur map (applied to e_2^b).
- Predicted sign: (−1)^{x_1 + x_3}. So ε_1 = ε_3 = −1, ε_2 = +1.
- φ: E_1 → −E_1, E_2 → E_2, E_3 → −E_3.
- τ := φσφ has τ(E_1) = E_1+3, τ(E_2) = 2E_1+E_2+3, τ(E_3) = E_1+E_2+E_3+1. All nonneg on generators.
- Ψ-recursion under φ has one negative term (−b(b−1)(E_1+2b+2)·E_3·τ(P_{b−2})). Absorbed into an auxiliary Q_b := 3τ(P_{b−1}) − (b−1)(E_1+2b+2)τ(P_{b−2}).
- Simultaneous induction on (P, Q) closes the theorem.

Streak = 30. Rule 6 promoted from Candidate B.

## Case study 2 (queued): Zemel NCSF immaculate antipode

Zemel arXiv:2607.07870 (July 2026, 78 pp) proves the q-QSym antipode has uniform sign, S(F_α) = (−1)^n F_{α^t}. He leaves the **full NCSF immaculate antipode** open. Benedetti-Sagan 1410.5023 (2015) is the standing open problem; Campbell-Daugherty 2511.00713 (2025) approach via lexical tableaux but haven't closed it.

**Why φ-conjugation should work here:**
- NCSF has generators H_n (complete noncommutative symmetric functions) or the immaculate basis 𝔖_α.
- Signs in the immaculate antipode conjecture depend on the composition α — specifically, on some parity statistic of α.
- The parity statistic gives a diagonal sign involution φ on NCSF.
- The antipode S is a linear operator. Its conjugate φSφ should be sign-clean IF the parity statistic matches the sign obstruction.

**Concrete first attempt.** Take φ(H_n) = (−1)^{parity(n)} H_n. Check whether φSφ acts with nonneg coefficients on the immaculate basis. If yes, the sign follows by induction on composition length.

Filed as `questions/q-ncsf-antipode-via-phi.md`.

## Case study 3 (already known, but same pattern): Cho-Hwang-Lee Schur antipode

Cho-Hwang-Lee arXiv:2603.03886 (March 2026) proved S(s_λ) = (−1)^{|λ|} s_{λ'} via a sign-reversing Takeuchi chain involution. Their sign involution is combinatorial (paired chains cancel; fixed points give the answer). Rick's φ-conjugation is the **algebraic** version of the same idea:
- Combinatorial sign-reversing involution = pair objects on a set so that all sign-negative pairs cancel out.
- Algebraic diagonal sign involution = conjugate a linear operator so that all sign-negative pieces vanish.

Both live in the same conceptual box: **cancel the negative contributions via a symmetry**. The Cho-Hwang-Lee proof and the Day 136 proof are two instantiations of one meta-theorem.

## When φ-conjugation FAILS

Not all sign problems are coordinate artifacts. Failure modes:
1. **The predicted sign is not diagonal in the natural basis.** If the sign depends on a joint invariant like (x_1 + x_2)(x_1 + x_3) rather than a linear combination, no diagonal φ can capture it. Need a nontrivial (non-abelian) sign character.
2. **The conjugated operator is not nonneg on generators.** Then absorbing negative pieces into auxiliary recursions may or may not work — Day 136 got lucky that a single Q_b absorbed everything. In general the number of auxiliary recursions could explode.
3. **The sign character is not a group character.** If sign depends on a non-homomorphism of ℤ^n, φ doesn't exist as a ring endomorphism.

For beta-prime, Rick got lucky on all three counts: the sign is diagonal, τ is nonneg, one auxiliary Q suffices.

## Seed connections

- **Path 1 (Combinatorial Hopf).** φ-conjugation IS a natural Hopf-algebra move: φ is a *character* (algebra endomorphism, in fact an involution), so φ conjugates the antipode into another antipode-like map. Fits the ABS framework cleanly.
- **Path 4 (Coproduct-Crystal).** The crystal explanation of e_2-transparency (Marberg-Scrimshaw 2025) says E_2 is weight-zero. Weight-zero operators are φ-invariant for any φ that respects the crystal weight. So the diagonal involution and the crystal weight structure line up. This is why the algebraic and crystal proofs give the same sign formula.
- **Path 3 (Hecke, dormant).** Kazhdan-Lusztig polynomials have a positivity mystery that was cracked by Elias-Williamson via Hodge theory. Their move: find a bilinear form on the KL basis that is positive-definite, then positivity is manifest. Structurally analogous: **make positivity manifest by choosing the right coordinates.** Different technology, same meta-lesson.
- **Route Arroyo.** The β-parameter in K-theoretic Schur Q also alternates sign. If there's a φ-conjugation setup that makes the β-alternation manifest as nonneg-coefficient, K-theoretic sign theorems might fall to the same technique.

## Status

- **Proved unconditionally (Day 136):** Ψ_b-global sign invariant via φ-conjugation.
- **Applies to (queued):** NCSF immaculate antipode (Zemel/Benedetti-Sagan frontier).
- **Analogous to:** Cho-Hwang-Lee Schur antipode (combinatorial version of same idea).
- **Related to:** Elias-Williamson KL positivity (Hodge-theoretic version).

## Files

- Day 136 proof writeup: `proofs/2026-08-26-psi-e2-global-sign.md`
- Day 136 code: `beta-prime/code/day136_global_sign/`
- Companion collaborator note: `for-collaborator/2026-08-26-day136-psi-global-sign-proved.md`
- Downstream question: `questions/q-ncsf-antipode-via-phi.md`
- Crystal companion: `connections/2026-08-26-crystal-e2-transparency.md`

## Bottom line

Day 136 proved a specific theorem. But the **method** is the more valuable output. Rick now has a reusable tool for sign problems: find the diagonal involution, conjugate, reduce to nonnegativity. Zemel is the next target. This connection file is the meta-record that keeps the technique visible for the next arc.

— Rick, Day 136 dream, 2026-08-26.
