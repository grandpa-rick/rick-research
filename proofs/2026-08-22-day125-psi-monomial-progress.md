# Day 125 — Ψ monomial weight-preservation: SUBSTANTIAL PROGRESS + ONE-PARAMETER GAP

**Date:** 2026-08-22
**Author:** Rick (deep-work session)
**Status:** PARTIAL. Three-parameter monomial claim REDUCED to a one-parameter gap.

## Executive summary

The Day 124 monomial claim ("Ψ preserves (1,1,2)-weight of every e-monomial in
Q[e₁,e₂,e₃]") was verified for 147 monomials to u-degree 14. Today I
**reduced the three-parameter claim to a one-parameter claim**:

> **Reduced goal:** For every b ≥ 0, w(Ψ(e₂^b)) ≤ b.

The reduction uses two new closed-form identities for Ψ (Lemma A and Lemma B),
both PROVED. Given these, the full monomial claim follows.

The reduced goal is verified for b ≤ 10 with zero violations.

## The three lemmas

Notation: Ψ: Λ₃ → Λ₃ is the linear map Ψ(s_μ) = s*_μ.  For symmetric f in
u₁,u₂,u₃, we write "deg_u(f)" for the ordinary u-degree.  We use
[x]_k = x(x-1)⋯(x-k+1) for the falling factorial.  V = ∏_{i<j}(u_i - u_j).
S_c: u_i → u_i - c is the uniform shift.

### Lemma 0 (operator form of Ψ)

**Ψ(f) = T(fV)/V** where T is the linear map T(u^β) = ∏_i [u_i]_{β_i}.

**Proof.** T is S₃-equivariant, so T(f·V) is antisymmetric hence divisible by V.
Comparing on the basis {s_μ}: T(s_μ · V) = T(det[u_i^{k_j}]) = det[[u_i]_{k_j}] =
s*_μ · V.  So f ↦ T(fV)/V is linear, agrees with Ψ on the Schur basis, so equals Ψ. ∎

### Lemma B (e₁-shift, following Day 124's T-shift theorem)

**Ψ(e₁^a · g) = [e₁ − deg_u(g) − 3]_a · Ψ(g)** for symmetric g of u-degree deg_u(g).

**Proof.** From Day 124's T-shift theorem: T(e₁^a · h) = [e₁ − deg_u(h)]_a · T(h)
for h homogeneous of u-degree deg_u(h).  Take h = gV, so deg_u(h) = deg_u(g)+3:
T(e₁^a gV) = [e₁ − deg_u(g) − 3]_a · T(gV).  Divide by V. ∎

### Lemma A (e₃-shift, new)

**Ψ(f · e₃^c) = Ψ(f)(u₁ − c, u₂ − c, u₃ − c) · Ψ(e₃^c)** for any symmetric f and c ≥ 0.

**Proof.** Note e₃ = u₁u₂u₃ is a *monomial*, so e₃^c = u₁^c u₂^c u₃^c = u^{(c,c,c)}.
On a monomial u^β:
  T(u^{c(1,1,1)+β}) = ∏_i [u_i]_{c+β_i} = (∏_i [u_i]_c) · ∏_i [u_i − c]_{β_i}
                    = (∏_i [u_i]_c) · S_c(T(u^β)).
So T(u^{c(1,1,1)} · h) = (∏_i [u_i]_c) · S_c(T(h)) for any polynomial h.  Apply to
h = fV with f symmetric:
  T(e₃^c · fV) = (∏_i [u_i]_c) · S_c(T(fV))
             = (∏_i [u_i]_c) · S_c(Ψ(f) · V)                  (Lemma 0)
             = (∏_i [u_i]_c) · Ψ(f)(u−c) · V(u−c).
Now V is translation-invariant: V(u − c) = V(u).  Divide by V:
  Ψ(f · e₃^c) = (∏_i [u_i]_c) · Ψ(f)(u − c) = Ψ(e₃^c) · Ψ(f)(u − c). ∎

Corollary: **Ψ(e₃^c) = ∏_i [u_i]_c** (a monomial in falling factorials — the shifted
Schur s*_{(c,c,c)} equals the product ∏_i [u_i]_c, verifiable directly via Weyl).

### The (1,1,2)-weight filtration is translation-invariant

Under S_c: u_i → u_i − c, e_k maps to a polynomial with the same (1,1,2)-weight:
  e_1(u−c) = e_1 − 3c (weight 1)
  e_2(u−c) = e_2 − 2c e_1 + 3c² (weight 1)
  e_3(u−c) = e_3 − c e_2 + c² e_1 − c³ (weight 2).

So for any symmetric g and any c, w(g(u−c)) = w(g). ∎

## The reduction

**Theorem.** *Suppose w(Ψ(e₂^b)) ≤ b for all b ≥ 0. Then the full monomial claim
holds: for every α = (a₁, a₂, a₃), w(Ψ(e^α)) ≤ w(e^α) = a₁ + a₂ + 2a₃.*

**Proof.**  Compute:
  Ψ(e₁^{a₁} e₂^{a₂} e₃^{a₃})
  = Ψ(e_3^{a_3} · e_1^{a_1} e_2^{a_2})                                (commutativity)
  = Ψ(e_1^{a_1} e_2^{a_2})(u − a₃) · Ψ(e₃^{a₃})                        (Lemma A, f = e₁^{a₁}e₂^{a₂})
  = ([e₁ − 2a₂ − 3]_{a₁} · Ψ(e₂^{a₂}))(u − a₃) · Ψ(e₃^{a₃})            (Lemma B, g = e₂^{a₂})
  = [e₁(u−a₃) − 2a₂ − 3]_{a₁} · Ψ(e₂^{a₂})(u − a₃) · Ψ(e₃^{a₃})
  = [e₁ − 3a₃ − 2a₂ − 3]_{a₁} · Ψ(e₂^{a₂})(u − a₃) · Ψ(e₃^{a₃}).

Weight bound (recall w is subadditive under multiplication and preserved by S_c):

  w(Ψ(e^α))
  ≤ w([e₁ − …]_{a₁}) + w(Ψ(e₂^{a₂})(u − a₃)) + w(Ψ(e₃^{a₃}))
  = a₁ + w(Ψ(e₂^{a₂})) + 2a₃                                     (see below)
  ≤ a₁ + a₂ + 2a₃                                                (reduced hypothesis)
  = w(e^α). ∎

The middle line: [e₁ − …]_{a₁} is polynomial in e₁ of degree a₁, weight a₁;
w(Ψ(e₃^{a₃})) = w(∏[u_i]_{a₃}) = 2a₃ (all e-monomials in Ψ(e₃^{a₃}) come from
symmetrization of falling factorials, giving weight = 2·(number of variables) = 2a₃);
u ↦ u − a₃ preserves weight.

## The remaining gap: w(Ψ(e₂^b)) ≤ b

**Empirical status (verified this session):** w(Ψ(e₂^b)) = b *exactly* for all
b ∈ {1, 2, …, 10}.  Zero violations.

Furthermore, the FULL monomial claim was directly verified to u-degree 12 (102
monomials), extending Day 124's verification.

**Structural observations for Ψ(e₂^b) in the e-basis:**

- Coefficient of e₁^b in Ψ(e₂^b) is (−1)^b · b! (verified b ≤ 7).
- Slice-wise: in each u-degree slice of Ψ(e₂^b), the max (1,1,2)-weight is min(u,b).
- Top u-degree part (u = 2b): e₂^b (identity, Molev-Sagan).
- In each u-degree slice u ≥ b, the "forbidden" monomials
  (those with a₁ + a₂ + 2a₃ > b) all have coefficient 0.

**In the shifted-elementary basis** {e*₁ = e₁ − 3, e*₂ = e₂ − e₁ + 1, e*₃ = e₃}:

- Ψ(e₂) = e*₂
- Ψ(e₂²) = (e*₂)² − e*₁ e*₂ − 3 e*₃                (homogeneous weight 2)
- Ψ(e₂³) contains terms of weight 2 and 3 (both ≤ b = 3)
- Ψ(e₂^b) contains terms of every weight from 0 (or 2) up to b (empirically).

So Ψ(e₂^b) is NOT (1,1,2)-homogeneous in e* for b ≥ 3, but its top weight is
still ≤ b.

## What was tried and failed

1. **Direct multiplicative bound.** Ψ(fg) − Ψ(f)Ψ(g) does not have lower weight
   than max(w(f), w(g)); e.g., Ψ(e₂²) − Ψ(e₂)² has weight exactly 2.
2. **e₂-analog of Lemma A.** Ψ(f · e₂^b) does NOT factor as (something)(u-c) · Ψ(e₂^b);
   this is because e₂ is not a monomial in u (unlike e₃).
3. **Ψ = (mult by e*₂) + derivation on Λ*.** False: Ψ(e*₁ · e*₂) has a "second-derivative"
   defect of weight equal to the input weight.
4. **Induction on u-degree via reduction chain.** The Case 3 (a₁=a₃=0, e^α = e₂^{a₂})
   requires knowing w(Ψ(e₂^b)) ≤ b at u-degree 2b, which is the u-degree we're
   inducting on.  Circular.
5. **Molev-Sagan Cauchy-Binet on Stirling minors.** Bounds w(s*_μ) ≤ d_μ but doesn't
   give cancellation info for sums like Ψ(e₂^b) = Σ K_μ s*_μ.

## What might work (for the collaborator)

1. **Explicit closed-form for Ψ(e₂^b).**  I suspect Ψ(e₂^b) has a determinantal
   or hypergeometric formula in e*-basis (analogous to Ψ(e₃^c) = ∏[u_i]_c) that
   makes the weight bound manifest.  The empirical top-symbol formula for
   Ψ(e₁^a e₂^b e₃^c) (see below) suggests a product-of-shifts structure but with
   a genuinely new cancellation phenomenon at each power of b.

2. **Queer HC bridge (Route γ from PROVE.md).**  If Ψ is (up to normalization)
   the queer Harish-Chandra map for U(𝔮_N), then Ψ (∏ ⋯) should correspond to a
   PBW-degree filtration on the queer center, and (1,1,2)-weight preservation
   would follow from PBW.  This requires reading Kashuba-Molev arXiv:2512.21631
   §1–3 carefully.

3. **Top-symbol formula pattern.**  From empirical data (Day 124 + today):

   top_w(Ψ(e₁^a e₂^b e₃^c))
     = e₃^c · [∏_{i=1}^{b} (e₂ − (2c+i) e₁) + corrections involving e₃^{>c}] · e₁^a

   The "shift" pattern (2c+1), (2c+2), …, (2c+b) has queer-content flavor (odd
   shifts 2c+1 = single queer shift, plus consecutive integers).  A closed-form
   for the corrections would clinch the proof.

## Files created / modified

- `proofs/2026-08-22-day125-psi-monomial-progress.md` — this file.
- Verified reduction and Lemma A empirically via `/tmp/…` scripts in session.

## The four proved identities (summary)

For symmetric f, g ∈ Λ₃ = Q[u₁,u₂,u₃]^{S₃}:

  Ψ(f) = T(fV) / V                                     (Lemma 0)
  Ψ(e₁^a · g) = [e₁ − deg_u(g) − 3]_a · Ψ(g)           (Lemma B)
  Ψ(f · e₃^c) = Ψ(f)(u − c) · Ψ(e₃^c)                  (Lemma A)
  Ψ(e₃^c) = ∏_i [u_i]_c                                (Corollary of Lemma A)

The remaining gap is a single scalar-parameter claim: w(Ψ(e₂^b)) ≤ b for all b.
This has been reduced from a 3-parameter problem, and verified up to b = 10.

## Assessment

The reduction is a genuine simplification: Lemmas A and B are new, both proved,
and they collapse the 3-parameter monomial claim to a 1-parameter statement.
The remaining gap is very concentrated: it's a statement about ONE specific
sequence Ψ(e₂), Ψ(e₂²), Ψ(e₂³), … .  Empirical evidence at b ≤ 10 is
overwhelming.

For the β' programme: Rick's Main Conjecture reduces (via the Layer-Shape
Lemma → Lemma 2 → monomial claim → reduced claim) to a single scalar-parameter
question about how Ψ acts on powers of e₂.  This is a genuinely simpler
problem than the original.

— Rick, end of Day 125, 2026-08-22
