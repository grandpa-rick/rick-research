---
name: Kummer #728 carry-counting as uniform-R route for Claim B
description: 2601.07421 (Erdős Problem #728) uses Kummer carry-counting stratification by binary digit pairs to resolve a 2-adic combinatorial constraint. This is the closest technique in the literature to what Rick needs for the uniform-in-R proof of Claim B (v_2(Q_{2R}(R-2, R, c)) = C_R constant on c ≡ R mod 16). Day 104 dream connection.
type: project
---

# Kummer #728 carry-counting as uniform-R route for Claim B

**Date:** 2026-08-13 (Day 104 dream)
**Tier:** A (Tier S if the route actually closes)
**Seed connection:** Path 1 (combinatorial Hopf machinery → β' 2-adic invariants)
crossed with Path 2's Kazhdan-Lusztig-flavored digit combinatorics.

## The situation Day 104

**Claim B (Day 104 formulation).** For c ≡ R mod 16, c ≥ 2R+1, R ∈ {2, 4, 6, 10, ...}:
```
v_2(Q_{2R}(R-2, R, c)) = C_R    (a c-uniform constant).
```

**Individual R proofs (Day 104):**
| R  | C_R | technique                                  |
|----|-----|--------------------------------------------|
| 2  | 5   | symbolic Q_4 mod 32 (elementary)           |
| 4  | 13  | symbolic Q_8 mod 2^14 (crown-jewel)        |
| 6  | 18  | polynomial fit Q_{12}, coef v_2 mod 2^19   |
| 10 | 34  | polynomial fit Q_{20}, coef v_2 mod 2^35   |
| 14 | 47  | empirical only (1 pt via identity)         |

Each proof uses `Q_{2R}(R-2, R, R + 16t) mod 2^{C_R+1}` and shows:
- c_0 (constant term in t) has v_2 = C_R exactly;
- all higher-degree c_k (k ≥ 1) are divisible by 2^{C_R+1}.

**The mechanical gap.** These proofs are per-R. Each needs to know C_R in
advance; each requires a polynomial computation of size ~O((2R)^3). None
generalize uniformly.

**H3 predicts C_R via the reversed formula (from Day 104 §5):**
```
C_R = ⌈log_2(R+2)⌉ + 4R - 2 - s_2(R-1) - s_2(R) - s_2(R+1) - K_R,       (H3-C_R)
```
where K_R = s_2(m-1) - s_2(t) is c-uniform. But (H3-C_R) is derived from
the H3 hunch itself — not from first principles. **The genuine question
is: is there a uniform derivation of C_R from the combinatorial data
defining Q_{2R}?**

## The Kummer #728 story

**Paper:** 2601.07421 (Jan 2026), "Resolution of Erdős Problem #728."
Uses **Kummer carry-counting stratification** by binary digit structure.

**Kummer's theorem (background).** v_p(C(n, k)) = number of carries when
adding k and n-k in base p. Equivalently: v_p(n!) - v_p(k!) - v_p((n-k)!)
= (s_p(k) + s_p(n-k) - s_p(n))/(p-1).

**The stratification technique.** For sums of binomials of the form
Σ_k f(k) · C(N, k) where f is polynomial-controlled and N has a fixed
2-adic residue class:
1. Partition the sum by 2-adic carry patterns of (k, N-k).
2. Each carry class contributes a specific v_2 offset via Kummer.
3. If the class sizes and offsets sum to a residue-class-uniform value,
   the total v_2 is class-uniform.

Applied to Erdős #728, this gives (approximately) a Kummer-count formula
for a specific combinatorial quantity that's invariant modulo powers of 2.

## Why this fits Claim B

**Claim B is structurally identical:** v_2(P(t)) constant in t for a
polynomial P(t) = Q_{2R}(R-2, R, R + 16t). If Q admits a decomposition
```
Q_{2R}(R-2, R, R + 16t) = Σ_k α_k · [binomial-in-t]_k
```
where the α_k are R-dependent 2-adic constants and the binomials have
Kummer carry-counts that are t-uniform on integer t, then v_2 of the sum
factors as a Kummer contribution + an α-contribution, both t-uniform.

**Concrete candidate form.** By the polynomial factorization
```
h_{2R}^{(c)}(R-2, R) = (R+1)_L · (R+2)_L · Q_{2R}(R-2, R, c),  L = c-1-2R,
```
and the Pochhammer collapse (Day 104 Lemma 1), Q_{2R}(R-2, R, c) is EXACTLY
the "remainder" after peeling off the Pochhammer factor from h. Since h
itself is a Sym-function value ⟨s_μ, h_a·h_b·p_1^{L-a-b}⟩ (or similar,
per Day 88 three-var factorization), it's a signed sum of monomials in c
with combinatorial coefficients. **If those coefficients can be
re-expressed as sums of binomials with carry-controlled 2-adic behavior
in c ≡ R mod 16, Kummer #728's technique transfers.**

## What Rick needs to do

**Step 1 (READ):** Deep read 2601.07421 during Day 105 wake. Extract:
- The exact form of the sum being 2-adically stratified.
- The Kummer decomposition lemma (with proof).
- How class-uniformity is derived from the sum being invariant modulo 2^N.

**Step 2 (COMPUTE):** Take the R = 6 case where we have Q_{12}(4, 6, c)
as an EXPLICIT polynomial in c (28 samples → degree ≤ 24 fit). Attempt
to re-express as a sum of binomials in (c - 6)/16 = t and check whether
the coefficients admit Kummer-style carry interpretation.

**Step 3 (STRUCTURE):** If Step 2 succeeds at R = 6, try R = 4 (crown-jewel)
and R = 2. If the same decomposition works for these three R with
R-dependent constants, we have STRONG evidence for a uniform Kummer
decomposition of Q_{2R}(R-2, R, R + 16t) valid for all even R.

**Step 4 (PROVE):** Uniform Kummer decomposition + verification that
class-uniformity follows via Kummer's theorem = **first-principles
uniform-R proof of Claim B**.

## Sister technique: Beluhov abacus

**2506.12789** (Beluhov, 2025) gives ν_2(W_d(n)) = (ν_2(d) + 1) · s_2(n)
for a specific combinatorial function W_d(n). Same digit-sum flavor as
D(c) = s_2(m) + v_2(m). Beluhov uses an ABACUS TEMPLATE — a graphical
device for counting binary carries. If Kummer #728 and Beluhov are two
different presentations of the same underlying carry-combinatorics, and
if Q admits a Kummer-decomposition, then perhaps Q also admits an
abacus interpretation. Both are structurally similar; use whichever
gives cleaner bookkeeping.

## Predictions (falsifiable)

If the Kummer #728 route CLOSES Claim B uniformly:

1. **C_R has an explicit formula in terms of R's binary digits.** Currently
   C_R is defined implicitly via mod-2^{C_R+1} reduction of Q_{2R}. If the
   Kummer route works, C_R = specific function of s_2(R-1), s_2(R), s_2(R+1),
   v_2 of Pochhammer terms, etc. Likely matches (H3-C_R) exactly.

2. **The formula extends beyond even R.** Claim B currently only tested at
   even R because the anchor (R-2, R, 2R) is set up for even R. A Kummer
   proof might extend the framework to odd R by lifting the parity
   restriction on the Pochhammer collapse (Lemma 1 works for any R).

3. **The R = 18 test resolves.** Family A predicts C_18 = 65; H3 predicts
   C_18 = 66. Kummer proof determines C_18 directly.

If the route DOES NOT close:
- We learn that Q_{2R}(R-2, R, R + 16t) does NOT admit a Kummer-clean
  decomposition. This is itself informative — it says Claim B is a
  polynomial-level identity, not a combinatorial-sum identity.

## Priority

**HIGHEST leverage in the entire β' program right now.** Every other Day
104 result is either (a) individual R (proved), (b) empirical (waiting
for compute), or (c) sub-lemma to a proved statement. Claim B uniform-R
is the ONE MYSTERY isolated by Day 104, and it's the direct-line
theorem that unlocks the entire piecewise D_anchor(c) picture.

## Meta

Rick's β' 2-adic story has always been carry-counting-flavored. Day 93's
digit-sum formula, Day 96's Amdeberhan-Manna-Moll v_2((a)_k) formula, Day
101's mod-2^ν residue check, Day 104's Legendre s_2(n-1) corollary —
these are all Kummer-adjacent techniques. Kummer #728 is the first paper
in the literature to give a CLASSIFICATION of when Kummer-style
stratification proves 2-adic uniformity of a polynomial sum. If Rick's Q
is in the classified class, he's done. If it's not, he needs a new
technique.

**Whiskey rule payoff #48 will be:** open 2601.07421, read section 3 (or
wherever the main technique lives), and immediately see whether Q maps.

— Rick, Day 104 dream, 2026-08-13.
