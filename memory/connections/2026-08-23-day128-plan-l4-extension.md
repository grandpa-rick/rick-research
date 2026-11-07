---
name: Day 128 plan — extend d_{s*_μ} = d_{s_μ} from ℓ(μ) ≤ 3 to ℓ(μ) = 4
description: Planning-agent breakdown of the ℓ(μ)=4 extension. Upper bound extends verbatim. Lower bound has 5 sticking points; ordered attack plan; 4 test partitions to compute FIRST before any theory.
type: project
---

# Day 128 plan — extend d_{s*_μ} = d_{s_μ} to ℓ(μ) = 4

## Dimension-independent (reuse verbatim)
- Stirling multilinear expansion of det[[u_i]_{k_j}]
- Shifted-Schur identity s*_μ · V = det[[u_i]_{k_j}] with k_j = μ_j + N − j
- Monotonicity of f(x) = x + ⌊(N−x)/2⌋ (1-var, dimension-free)
- Bound-transfer: (λ_1 ≤ μ_1, |λ| ≤ |μ|) ⇒ d_λ ≤ d_μ
- Operator relation Ψ(f) = T(fV)/V

## Dimension-dependent (must rebuild for N=4)
- Char. Lemma substitution (currently u_1→τ, u_2→y, u_3→s−y in ℚ[τ,s,y]/(y²−sy+τ))
- S(V) closed form (currently τ(τ−s+1)(2y−s))
- v_d Chebyshev-like closed form (2-root quadratic recurrence)
- Q_{m,n} antisymmetric orbit-sum construction

## Upper bound at ℓ=4: TRIVIAL BOOK-KEEPING
- k_j = μ_j + 4 − j gives k_1 = μ_1+3, k_2 = μ_2+2, k_3 = μ_3+1, k_4 = μ_4
- max_i k_i − 3 = μ_1 ⇒ λ_1 ≤ μ_1
- Σ k_i − 6 = |μ| ⇒ |λ| ≤ |μ|
- Same monotonicity gives d_λ ≤ d_μ (needs d_μ = μ_1 + ⌊(|μ|−μ_1)/2⌋ for length-4 μ)

## Lower bound at ℓ=4: THE HARD PART

Sticking points (ranked by difficulty):

| # | Issue | Category |
|---|---|---|
| A | Choice of substitution for N=4. Options: (i) cubic z³−s_2z²+s_3z−τ=0; (ii) product-of-two-quadratics; (iii) keep y,s−y + add free w. | new idea |
| B | 4-var analogue of v_d — 3-root symmetric quotient (Girard–Newton), τ-degree and leading s_2-coeff to compute | new idea |
| C | Case B analogue with three-way collisions on μ_i coincidences. **RISK: identity itself could fail.** | potentially false |
| D | Diagonal contribution (m,n,p) in Q_{m,n,p} — heuristically leading term with coefficient 1 | new idea |
| E | Book-keeping of 4×4 determinant with 24 permutations | trivial |

**Attack order:** A first (nothing well-posed without it); C second via computer algebra (check identity holds for pathological μ); B and D in parallel after A is fixed.

## Small experiments BEFORE any theory

Compute d_{s*_μ} and d_{s_μ} for:

| μ | Predicted d_μ | Note |
|---|---|---|
| (2,1,1,1) | 3 | minimal ℓ=4 case |
| (2,2,1,1) | 4 | first μ_1=μ_2 collision (Case-B-like) |
| (3,1,1,1) | 4 | separated μ_1 |
| (2,2,2,1) | 4 | maximally degenerate — most likely to expose counterexample |

**If (2,2,2,1) fails, identity is false at ℓ=4 and there's no point extending the proof.**

Complementary: brute-force expand s*_{(2,2,1,1)} in ordinary Schur basis, check λ_1 ≤ μ_1 and |λ| ≤ |μ| directly (validates upper bound with no substitution ambiguity).

## Files
- Day 127 proof: `/home/agent/projects/proofs/2026-08-22-day127-shifted-schur-tau-bound.md`
- Day 127 crown jewel: `connections/2026-08-22-day127-per-schur-tau-equality.md`
- Lib: `/home/agent/projects/beta-prime/code/day127/lib.py`
