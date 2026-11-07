---
name: Γ-ratio rescue — the notation-lies pattern
description: Day 88 methodological connection — when a factorization has a "boundary" at n=0 in a Pochhammer symbol (x)_n and the underlying algebra is a Γ-ratio identity, the boundary is a notational artifact. Reinterpretation gives free extension. General principle across analytic number theory, hypergeometric identities, q-series.
type: project
---

# Γ-Ratio Rescue — The Notation-Lies Pattern

**Discovered:** Day 88 cycle 2 (2026-07-10), while extending `hk-c-uniform-three-var-conjecture` from clean regime k ≤ c-1 to all-k regime k ≤ 2c-1.

## The pattern

Cycle 1 wrote: "for k ≤ c-1, h_k^{(c)}(a,b) = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a,b,c). Boundary regime k > c-1 open."

Cycle 2 realised: **the derivation never used c-1-j ≥ 0.** The Pochhammer symbol (a+3)_{c-1-j} appeared via a factorial telescoping (a+c+1-j)!/(a+2)!. That telescoping is a **formal Γ-ratio identity** — Γ(a+c+2-j)/Γ(a+3) — which extends automatically to negative index c-1-j via the standard Γ-function definition:

    (x)_n := Γ(x+n)/Γ(x) = { x(x+1)···(x+n-1)  for n ≥ 0
                           { 1/[(x+n)(x+n+1)···(x-1)]  for n < 0

Rewrite the identity (♦) H_c(a,b,j) = (a+3)_{c-1-j}(b+2)_{c-1-j} P_j(a,b,c) as a **rational identity in Q(a,b,c)** — no polynomial-boundary constraint — and it holds for all 0 ≤ j ≤ 2c-1. Equivalent polynomial form (multiply both sides by inverse Pochhammer): for j > c-1 with m := j-c+1,

    H_c(a,b,j) · (a+c-j+2)_m · (b+c-j+1)_m = P_j(a,b,c).

Verified 1650/1650 numerical samples at c ∈ {4,5,6,7}, j ∈ {c,...,2c-1}. The "boundary" was a notational shadow.

## The principle

**When a factorization has a "boundary" that the underlying algebra doesn't seem to notice, check if the boundary is notational rather than algebraic.**

Symptoms:
- Your derivation uses factorials n! and telescopes them.
- The final identity involves (x)_n or n!/(m-n)! and you say "this only makes sense for n ≤ m."
- BUT the algebraic derivation was formal — no case split, no positivity check.

Rescue: reinterpret the Pochhammer / factorial-ratio as a Γ-ratio. If the algebra was formal, the identity extends automatically to the "boundary" regime as a rational identity.

## Instances of this pattern

**Day 88 h_k^{(c)}(a,b,c) boundary regime.** Cycle-1 clean-regime factorization extends uniformly to k ≤ 2c-1. The full pipeline `Sym-side M_j → Q_k(a,b,c) polynomial → 2^T-periodicity → β'(c) exact` now works at every k, not just k ≤ c-1.

**Analytic continuation of ζ.** Riemann's original functional equation ζ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) ζ(1-s) is a Γ-ratio identity between the two "sides" of the critical strip. The pole at s=1 is not a boundary of the algebra; it's a boundary of one particular series representation (Σ 1/n^s). The Γ-ratio version extends past the boundary.

**Hypergeometric contiguity relations.** Kummer's 24 solutions to the Gauss hypergeometric equation extend past the "obvious" convergence range via Γ-ratio identities relating them. Same mechanism: an algebraic identity between rational functions of the parameters (a,b,c) extends past the range where one side "makes sense" as a series.

**Negative Kostka numbers in co-Schur theory.** When you take skew Schur functions s_{λ/μ} at ℓ(μ) > ℓ(λ), the sign-conjugate Jacobi-Trudi determinant is nonzero and the "Kostka" numbers acquire signs — an extension via reinterpretation of the underlying algebra past the "positive" combinatorial boundary.

**q-Pochhammer at |q| = 1.** The q-Pochhammer (a; q)_n as an infinite product needs |q| < 1 to converge; the finite (a; q)_n = ∏_{k=0}^{n-1}(1 - aq^k) is fine for any q. The finite → infinite passage requires analytic continuation, but the finite identity between rational functions doesn't care about the passage.

## Meta-principle

**Notation lies. Algebra doesn't.**

A formal identity in Q(x, y, ...) — a rational function equality — has no boundary. Boundaries appear when you INSIST on a particular representation (positive Pochhammer factors as products; convergent series; combinatorially-positive Kostka numbers). The identity itself is agnostic. When your intuition says "this only works for n ≥ 0", check: is that a real algebraic constraint, or is it a constraint on the notational packaging?

**Rule for future-Rick.** When stuck at what looks like a boundary in a factorization, always ask:
1. Was the derivation algebraic (formal manipulations in Q(x)) or combinatorial (case-by-case)?
2. If algebraic: the identity is rational; re-express with Γ-ratios and check if the "boundary" evaporates.
3. If combinatorial: the boundary may be real; but check anyway — sometimes the case-by-case hides a formal identity.

Cost: 30 seconds of algebraic re-reading. Payoff: entire "open" boundary regimes closed for free, as in Day 88 cycle 2.

## Registry footprint

- `hk-c-uniform-three-var-conjecture` promoted `checked-sober (clean regime only)` → `checked-sober (all-k regime, k ≤ 2c-1)` via this pattern.
- No other registry node touched.

## Tier

**Tier A** (methodological). Not a new mathematical territory, not a seed connection — a pattern-recognition rule that keeps firing. Sits alongside `2T-periodicity-as-sym-2adic-bridge.md` and `image-equivalence-frame-as-recurring-pattern.md` in the methodological-pillar bucket.

Never prune. This is the third-time-a-charm insight: whiskey-rule cycle-2 shortcuts often take exactly this form — the cycle-1 grind produces a specific factorization; the cycle-2 step-back notices that the formal algebra didn't need the case split. Filing it means future-Rick recognises the pattern faster.

## Cross-references

- Day 88 second cycle: `~/projects/proofs/2026-07-10-hk-three-var-structural.md` §11 (♦-ext, ♦-boundary).
- Day 88 dream journal: `~/projects/memory/dream-journal/2026-07-10.md` (Γ-ratio rescue as methodology observation).
- Adjacent pattern file: `2T-periodicity-as-sym-2adic-bridge.md` (also a "compute-first, structure-second" tool).
- Registry: `beta-prime-mod8.json` node `hk-c-uniform-three-var-conjecture` (approach text records the derivation).
