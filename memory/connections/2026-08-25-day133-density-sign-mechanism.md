---
name: Day 133 Full Density Theorem via Uniform-Sign Mechanism — every top monomial has explicit sign (−1)^{x_1+x_3}
description: The FULL DENSITY THEOREM for tops[b] := Ψ(e_2^b)|_top. For every b ≥ 0 and every (x_1,x_2,x_3) with x_1+x_2+2x_3=b, [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b] = (−1)^{b−x_2−x_3}·N(b;x_1,x_2,x_3) with N > 0 explicit. Support = ⌊(b+2)²/4⌋ = A002620(b+2) monomials, no cancellations ever. Sign = (−1)^{b−x_2−x_3} = (−1)^{x_1+x_3} (number of e_1 and e_3 factors). Mechanism: every μ_n = (−1)^{n−1}(n²−1)/n factor in M(T) has monotone-in-n sign; product Πμ_{n_i} over composition (n_1,...,n_k) sums to shared sign (−1)^{m−k} INDEPENDENT of composition; matches A_n = Π(E_2−rE_1) sign (−1)^{n−x_2}; every (n,m) contribution shares sign (−1)^{b−x_2−k} independent of n. All summands aligned + positive → nonzero. Bonus [E_3^{b/2}]=(−3)^{b/2}(b−1)!! for even b. Three candidate combinatorial interpretations for sign: Cho-Hwang-Lee 2603.03886 Takeuchi involution, Schmitt Möbius on incidence Hopf, Lee plethystic X↦X−tX at t=1.
type: project
---

# Day 133 Full Density Theorem — Uniform Sign Mechanism

**Statement.** For every b ≥ 0 and every (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2x_3 = b,

  **[E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b] = (−1)^{b − x_2 − x_3} · N(b; x_1, x_2, x_3)**

where N > 0 is an explicit strictly positive sum of positive rationals.

## The uniform-sign mechanism (one-observation proof)

From Day 131: F(T) = Σ tops[b] T^b/b! = A(T) · B(T) with
- **A(T)** = Σ_{n≥0} A_n T^n/n!, where A_n = Π_{r=1}^n (E_2 − r·E_1) = Σ_{x_2=0}^n [signed] E_1^{n−x_2} E_2^{x_2} with sign (−1)^{n−x_2}·(unsigned Stirling first kind).
- **B(T)** = exp(E_3 · M(T)) = Σ_{k≥0} (E_3^k / k!)·M(T)^k, where M(T) = Σ_{n≥2} μ_n E_1^{n−2} T^n with μ_n = (−1)^{n−1}(n²−1)/n.

**Key observation:** Each factor μ_n has MONOTONE-IN-n sign (−1)^{n−1}. So for any composition (n_1, ..., n_k) of m = n_1 + ... + n_k (with n_i ≥ 2), the product Π_{i=1}^k μ_{n_i} has sign (−1)^{Σ(n_i − 1)} = (−1)^{m − k}, INDEPENDENT of the specific composition.

**Extracting coefficient of E_1^{x_1} E_2^{x_2} E_3^{x_3} in tops[b] = Σ_{n+m=b} C(b,n) A_n B_m:**
- A_n contributes E_1^{n − x_2} E_2^{x_2} with sign (−1)^{n − x_2}.
- B_m = (E_3^k / k!) M(T)^m contributes E_3^{x_3} E_1^{m − 2x_3} with sign (−1)^{m − k} (any composition of m into k parts each ≥ 2, giving m − 2x_3 = Σ(n_i − 2) = m − 2k, so k = x_3).
- Combined sign: (−1)^{(n−x_2) + (m−k)} = (−1)^{b − x_2 − k} = (−1)^{b − x_2 − x_3}. INDEPENDENT of n.

Every (n, m)-contribution to the (x_1, x_2, x_3)-coefficient carries the SAME sign. All summands aligned + positive magnitudes → sum is positive → coefficient is nonzero. **QED.**

## Equivalent form: sign = (−1)^{x_1 + x_3}

  b − x_2 − x_3 = (x_1 + x_2 + 2x_3) − x_2 − x_3 = x_1 + x_3

So the sign is **(−1)^{x_1 + x_3}** — exactly the number of e_1 and e_3 factors, with e_2 factors free.

**Structural fingerprint.** e_2 acts as a "sign-neutral" element; e_1 and e_3 as "sign-flipping." This asymmetry mirrors the operator formula: T(u^β) = Π [u_i]_{β_i}, so multiplying by e_2 keeps u_i^2 combinations in a symmetric structure, while e_1 (single u_i) and e_3 (product u_1 u_2 u_3) break the symmetry in "odd" ways.

## Bonus closed form: pure-E_3 column

For even b:

  **[E_3^{b/2}] tops[b] = (−3)^{b/2} · (b − 1)!!**

Reproduces empirical b=4 → 27, b=6 → −405, b=8 → 8505 exactly.

**Why forced:** For a pure-E_3 monomial (x_1 = x_2 = 0, x_3 = b/2), the min-sum constraint x_1 + x_2 + 2x_3 = b forces x_3 = b/2. The only composition of b in M(T)^{b/2} with all parts ≥ 2 summing to b in b/2 parts is (2, 2, ..., 2) — every part is 2. μ_2 = −3/2. Product: (μ_2)^{b/2} · (b! / (2!)^{b/2}) · (E_1^0) · (from A(T) side E_2 coefficient in A_0 = 1, so n = 0). Simplifies to (−3)^{b/2}·(b−1)!!.

**Predictions:** b=10 → −229 635; b=12 → 7 577 955; b=14 → −295 540 245.

## Three candidate combinatorial interpretations of the sign

The sign (−1)^{x_1 + x_3} smells like a sign-reversing involution or Möbius function. Three literature candidates:

### 1. Cho-Hwang-Lee 2603.03886 (March 2026) — Takeuchi involution

Cho-Hwang-Lee constructed an explicit sign-reversing involution on Takeuchi chains for the Schur-basis antipode: S(s_λ) = (−1)^{|λ|} s_{λ'}. The involution acts on sequences of "cutting" operations in the Takeuchi (Schmitt) formula for the antipode; the exponent |λ| counts chain depth.

**Adaptation to Ψ(e_2^b):** In the elementary basis Takeuchi expansion of Ψ, each e_1 factor contributes "one cut," each e_3 factor contributes "one cut," and each e_2 factor contributes "zero cuts" (or "one uncut" — need to determine sign convention). Chain depth = x_1 + x_3 by construction. If Rick can identify Ψ|_top with an antipode of some sub-Hopf-algebra of Sym, Cho-Hwang-Lee's technique gives the bijective sign proof.

**Status:** PRIORITY next investigation. Concrete plan: read Cho-Hwang-Lee in full; check whether their involution technique factors through Ψ (Molev-Olshanski) at top weight.

### 2. Schmitt (1994) Möbius function of incidence Hopf algebra

Schmitt's theorem: the antipode of the reduced incidence Hopf algebra of a poset P is (up to sign) the Möbius function μ_P. Hall's alternating chain formula is the direct analogue of Takeuchi's.

**Adaptation:** define a graded poset on (1,1,2)-weight-b compositions in {e_1, e_2, e_3} where covering relations correspond to "e_2 → (e_1, e_1)" (splitting) and "e_3 → (e_1, e_2)" (splitting). If the Möbius function of this poset equals (−1)^{number of split levels}, and split levels count = x_1 + x_3, done.

**Status:** SECONDARY. Requires identifying the correct poset structure. Less immediate than Cho-Hwang-Lee.

### 3. Lee plethystic substitution X ↦ X − tX at t = 1

Lee's framework in 2606.22058 uses plethystic substitution to introduce alternating signs in coefficient expansions. At t = 1 (a degenerate limit), the substitution produces sign (−1)^{degree shift} in monomial expansions.

**Adaptation:** Rick's (1,1,2)-grading encodes E_3 as weight-2, E_1 and E_2 as weight-1. In Lee's substitution, the "unshielded" part (the piece that isn't paired with a t-factor) would be x_1 + x_3 if e_2 is treated as the "shielded" letter. This is a stretch, but Lee's paper is worth revisiting with this angle.

**Status:** SPECULATIVE. Lowest probability of yielding a clean bijection.

**Rick's prior:** 60% Cho-Hwang-Lee Takeuchi interpretation is the correct answer; 25% Schmitt Möbius; 10% Lee plethystic; 5% none of these (a new combinatorial mechanism specific to Ψ).

## Support = A002620(b+2)

The support of tops[b] is the set of (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2x_3 = b. Count:

- b = 2k even: (k+1)² = A002620(2k+2)
- b = 2k+1 odd: (k+1)(k+2) = A002620(2k+3)

Both cases = ⌊(b+2)² / 4⌋ = A002620(b+2). "Quarter squares."

**OEIS A002620 combinatorial interpretations** include: 2-element subsets of {1, ..., n+1}, maximal antichains in [1,n], and Kekulé structures on certain benzenoid graphs. If any of these has a natural bijection to Rick's (x_1, x_2, x_3)-monomials, that's a bonus structural insight.

## Related F = A · B parallels in the literature

Rick's F(T) = A(T)·B(T) has THREE independent parallels (Browse 107):
1. **Jing-Rozhkovskaya 1610.03396** (operator level): Ψ⁺(v) = Q(v) ∘ DR(v).
2. **Seelinger classical Q(z) = E(z)·H(z)** (Schur Q sub-Hopf template).
3. **Marberg-Scrimshaw 2608.11009** (crystal character): ch(SetTab_n(∞)) = ch(B(∞))·∏(1−βxᵢ)^{i−1}.

Rick's density-with-sign result provides the SCALAR-COEFFICIENT / EXPLICIT-DENSITY / COMBINATORIAL-SIGN version of these operator-level statements. None of the parent papers contains Rick's actual theorems. See `2026-08-25-three-way-A-B-parallelism.md`.

## Files

- `proofs/2026-08-25-psi-e2-density.md` — full Day 133 writeup.
- `beta-prime/code/day133_density/verify_signs.py` — uniform sign confirmed b ≤ 8.
- `beta-prime/code/day133_density/verify_individual.py` — every (n,m) contribution matches predicted sign, b ≤ 7.
- `beta-prime/code/day133_density/verify_e3_column.py` — (−3)^{b/2}(b−1)!! confirmed b ∈ {2, 4, 6, 8}.
- `for-collaborator/2026-08-25-day133-full-density-theorem.md` — Robin note.
- `connections/2026-08-25-crown-jewel-closed.md` — companion connection on Day 131 atom closure.
- `connections/2026-08-23-browse106-oeis-a002620-full-density.md` — Browse 106 support-count discovery.

## Seed connections

- **Path 1 (Combinatorial Hopf):** Uniform-sign mechanism = pure Hopf/Möbius/incidence-Hopf territory. All three candidate sign interpretations (Cho-Hwang-Lee, Schmitt, Lee plethystic) are Path 1.
- **Path 4 (Coproduct-Crystal):** Marberg-Scrimshaw's parallel non-monoidality obstruction retroactively validates the EGF route over crystal tensor product proofs.
- **Path 2 (Quantum groups):** Route Arroyo residual — if Brahma-Ikeda-Iwao-Yang β-degree matches (1,1,2)-weight, the density theorem broadens to K-theoretic Schur-Q. Test unrun.
- **Path 3 (Hecke):** dormant.

## Open questions

1. Does Cho-Hwang-Lee's Takeuchi involution technique apply directly to Ψ(e_2^b)|_top in the elementary basis?
2. Is Ψ|_top the antipode of some sub-Hopf-algebra of Sym_3? If yes, the sign is a Hopf-antipode sign automatically.
3. Does the Brahma-Ikeda-Iwao-Yang β-degree at b = c = 0 match Rick's (1,1,2)-weight? (Route Arroyo cheap test.)
4. Does A002620(b+2) have a natural bijection to (x_1, x_2, x_3)-monomials at weight b?
5. Does the density-with-sign extend to Ψ(e_r^b) for r ≠ 2? (Requires analog of K5 scalar collapse for general r.)
