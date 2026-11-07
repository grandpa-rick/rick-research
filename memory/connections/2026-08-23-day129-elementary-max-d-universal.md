---
name: Day 129 — d_{s*_μ} = d_μ, ELEMENTARY proof for ALL ℓ (Rick was proving too much)
description: The combinatorial claim d_{s*_μ} = d_μ (max Schur-support d-value = d_μ) admits a 6-line proof via Stirling matrix triangularity, universally in partition length. Rick's Day 127 v_d/Q_{m,n}/Case A/B machinery was targeting a strictly STRONGER algebraic statement (τ-degree preservation under Char. Lemma substitution). Whether downstream needs the τ-version is now the key open question.
type: project
---

# Day 129 crown jewel — the combinatorial claim needed 6 lines, not 150

## The theorem, universally in ℓ

For any partition μ (any length ℓ, any N ≥ ℓ(μ)):
$$d_{s^*_\mu} \;:=\; \max\{d_\lambda : c^\mu_\lambda \ne 0\} \;=\; d_\mu, \qquad d_\nu := \nu_1 + \lfloor (|\nu|-\nu_1)/2 \rfloor$$

where $c^\mu_\lambda$ are the Schur expansion coefficients: $s^*_\mu(u) = \sum_\lambda c^\mu_\lambda \, s_\lambda(u)$ in Rick's u-basis convention.

## The proof (6 lines)

Multilinear Stirling-of-the-first-kind expansion of $\det[[u_i]_{k_j}]$ (with $k_j = \mu_j + N - j$) yields the closed form
$$c^\mu_\lambda \;=\; \det[s(k_j, \ell'_i)], \qquad \ell'_i = \lambda_i + N - i.$$

**Upper bound.** Row 1 nonzero requires $\ell'_1 \le k_1 = \max_j k_j$, so $\lambda_1 \le \mu_1$. Any nonzero permutation summand $\prod_i s(k_{\pi(i)}, \ell'_i)$ needs $\ell'_i \le k_{\pi(i)}$ for all $i$; summing gives $|\lambda| \le |\mu|$. Monotonicity of $f(a,b) := a + \lfloor(b-a)/2\rfloor$ (non-decreasing in each argument) yields $d_\lambda \le d_\mu$.

**Lower bound.** At $\lambda = \mu$: $\ell'_i = k_i$, and $[s(k_j, k_i)]$ is **lower triangular with unit diagonal** because $s(k, \ell) = 0$ for $\ell > k$ and $k$ is strictly decreasing. So $c^\mu_\mu = 1$, hence $d_\mu \in \{d_\lambda : c^\mu_\lambda \ne 0\}$. $\square$

## What Day 127 was actually proving

Day 127's elaborate v_d/Q_{m,n}/Case A/B machinery was targeting the **strictly stronger** algebraic statement:
$$\tau\text{-deg}\big(S(s^*_\mu)\big) = d_\mu \text{ under the Char.\ Lemma substitution } u_1 \to \tau,\ u_2 \to y,\ u_3 \to s-y.$$

This is stronger because multiple λ's can share the maximum $d_\lambda = d_\mu$ (e.g. μ = (2,1) at N = 3 has both λ = (2,1) and λ = (2) at $d = 2$). The top-τ part of $S(s^*_\mu) = \sum_\lambda c^\mu_\lambda \, S(s_\lambda)$ is then a **sum** that could a priori cancel. Cases A/B ruled out that cancellation at ℓ = 3.

For the combinatorial claim, $c^\mu_\mu = 1$ makes $d_\mu$ appear in the support unconditionally. **No cancellation analysis needed.**

## The key question after Day 129

**Does the downstream w(Ψ(e_2^b)) ≤ b program need τ-degree preservation, or just the combinatorial max-d claim?**

- If **combinatorial suffices** — the ℓ = 4 gap (and ℓ = 5, and all ℓ) is closed. Day 118 §5 residual gap = done. Move to the b-side.
- If **τ-degree required** — Day 127's ℓ ≤ 3 proof still stands, but ℓ ≥ 4 needs the Char. Lemma substitution + $Q_{m,n,p}$ machinery. The hard case is 3-way collisions like μ = (2,2,1,1) where multiple λ's hit the top τ.

Empirical evidence (Day 128): ℓ=4 sweep 53/53, ℓ=5 sweep 19/19. Zero cancellations observed at ℓ=4 collision partitions ((3,3,3,1) and (3,3,2,2)). So the τ-version is likely also true; the question is only whether we NEED to prove it.

Gut check: the crown-jewel program uses τ-degree preservation for symmetric-poly linear combinations (Day 127 "Symmetric polynomial τ-deg preservation" caveat: cancellations in Schur decomposition of f could propagate to Ψ(f)). If the crown-jewel proof can be rephrased to use only the max-d/support statement, τ-degree machinery can be shelved.

## Meta-lesson (two rules)

**Rule 1 (READ THE CLAIM):** *when the machinery you're building has grown larger than the claim itself, STOP and re-read the claim.* Rick built ~150 lines of τ-degree scaffolding when the stated combinatorial claim needed 6 lines.

**Rule 2 (SOFT LOWER BOUND FIRST):** *before writing hard lower-bound machinery, check whether the target itself appears in the support with $c^\mu_\mu = 1$.* A triangular-determinant check on the Stirling matrix takes a line. If yes, the lower bound is instant.

Both rules should be checked at the START of any new PROVE cycle, not day-2 or day-3.

## Consequences for the reduction chain

Current post-Day-129 state of the main program:

1. **Main gap:** $w(\Psi(e_2^b)) \le b$ for all $b$. Empirical b ≤ 6 tight (Day 128), zero cancellations, clean coefficient patterns.
2. **Reduction (Day 125):** 3-param monomial claim → 1-param via Lemmas A, B, factorization theorem. All 33/33 re-validated post-bug-fix (Day 128).
3. **Per-Schur support statement:** $d_{s^*_\mu} = d_\mu$ — **PROVED for ALL ℓ (Day 129).** No dimension restriction.
4. **Per-Schur τ-degree statement:** τ-deg(S(s*_μ)) = d_μ — PROVED ℓ ≤ 3 (Day 127); open ℓ ≥ 4. Uncertain whether needed.

The reformulation trajectory is now:

- Day 116: 3-line Lift Theorem.
- Day 118: Molev-Sagan (**) + closed form d_μ.
- Day 121-123: E-basis, (A,B) reduction.
- Day 125: Operator formula Ψ = T(·V)/V. 3-param → 1-param.
- Day 127: Per-Schur τ-degree ℓ ≤ 3 (v_d/Q_{m,n} machinery).
- **Day 129: Per-Schur SUPPORT statement, elementary, ALL ℓ.**

The gap remaining is now cleanly: **either close the 1-param w-bound directly (via operator formula + top-symbol generating series), OR extend Day 127's τ-degree machinery only IF downstream demands it.**

## Seed connections

- **Path 1 (Combinatorial Hopf):** The proof lives entirely in the Stirling matrix — an integer-matrix triangular-determinant argument. No operator formula, no immanant, no HC. This is Path 1 in its most elementary form. The 6-line argument would fit in a Grinberg-Reiner appendix.
- **Path 4 (Coproduct-Crystal):** The support bound $\lambda_1 \le \mu_1$ and $|\lambda| \le |\mu|$ on Schur expansions of shifted Schurs is precisely the shape of the crystal-theoretic "dominated tableaux" interval. Elementary Stirling proof + crystal-theoretic support interval = same result from two angles.
- **What's absent:** Path 2 (quantum groups) and Path 3 (Hecke) don't enter this proof. The claim is finite-combinatorial. Consistent with Day 126's finding that the queer HC bridge is a category error for Rick's specific Ψ.

## Files

- Proof: `~/projects/proofs/2026-08-23-day129-shifted-schur-l4.md`
- Robin note: `~/projects/memory/for-collaborator/2026-08-23-day129-elementary-argument.md`
- Comparison Day 127: `~/projects/proofs/2026-08-22-day127-shifted-schur-tau-bound.md`
- Companion crown jewel: `connections/2026-08-23-day128-psi-e2-bound-tight-b6.md`
