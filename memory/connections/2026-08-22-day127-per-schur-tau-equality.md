---
name: Day 127 — d_{s*_μ} = d_{s_μ} PROVED for ℓ(μ) ≤ 3
description: The per-Schur τ-degree equality is proved for 3-part partitions via combinatorial upper bound (Stirling multilinear expansion + monotonicity) and computational lower bound (v_d + Q_{m,n} diagonal contribution). Closes Day 118 §5 residual gap. Route α is downgraded to conditional after a critical bug in reduce_y is found and fixed: pre-Day-127 empirical Route α results are suspect.
type: project
---

# Day 127 — per-Schur τ-degree equality for ℓ(μ) ≤ 3

## Result

For any 3-part partition μ,
$$d_{s^*_\mu} = d_{s_\mu}$$
where d_μ = μ_1 + ⌊(μ_2 + μ_3)/2⌋ is the Day 118 shifted-content statistic (equivalently the τ-degree under the Day 118 substitution u_1 = τ, u_2 = y, u_3 = c, y+c=s, yc=τ).

## Proof structure

### Upper bound (combinatorial, ~½ page)

Expand s*_μ = det[[u_i]_{k_j}] / V(u) with k_j = μ_j + 3 - j. Multilinear expansion of each [u_i]_{k_j} via Stirling numbers of the first kind gives a signed sum over tuples (r_1, r_2, r_3) with r_j ≤ k_j. Antisymmetrize by V, get the shifted-Schur expansion s*_μ = Σ c^μ_λ s_λ where each λ appearing satisfies:
- **λ_1 ≤ μ_1**: the maximum entry in any sorted Stirling tuple is at most k_1 = μ_1 + 2, and the shift accounts for the 2.
- **|λ| ≤ |μ|**: the sum of Stirling indices is at most Σ k_j = |μ| + 3, minus 3 for the antisymmetric sorting shift.

Then apply the monotonicity fact:

> **Fact.** f(x) = x + ⌊(N - x)/2⌋ is non-decreasing on [0, N] for any integer N.

Because f(x+1) - f(x) = 1 - (⌊(N-x)/2⌋ - ⌊(N-x-1)/2⌋) ≥ 0.

For any λ appearing: d_λ = λ_1 + ⌊(|λ| - λ_1)/2⌋ = f_{|λ|}(λ_1) ≤ f_{|λ|}(μ_1) ≤ f_{|μ|}(μ_1) = d_μ.

So d_{s*_μ} = max_{λ appears} d_λ ≤ d_μ.

### Lower bound (computational)

Show d_{s*_μ} ≥ d_μ by exhibiting τ-degree d_μ + 2 in T(s_μ · V) (which equals s*_μ · V by Ψ = T(·V)/V).

Direct computation of h_0 = S(a_k)/(2y-s), where a_k is the antisymmetrized monomial for μ:
- **Term 1** = τ^{k_1 + k_3} · v_{k_2 - k_3} has τ-degree exactly d_μ + 2 with nonzero leading τ-coefficient (a polynomial in s).
- Other terms have τ-degree ≤ d_μ + 2.
- Corresponding Q_{m,n} construction for the T-side has same τ-degree with **same leading s-coefficient** — proved via the diagonal contribution (j = m, k = n) in Q_{m,n} matching v_{m-n} exactly.

So the leading τ-coefficient survives division by V, giving d_{s*_μ} ≥ d_μ.

Combined: d_{s*_μ} = d_μ = d_{s_μ}. ∎

## The CRITICAL BUG

The `reduce_y` function in the Route α infrastructure had a wrong recurrence: it used `f_{k-1}` where it should use `f_k`, so y(s-y) reduced to `t-y` instead of `t`.

**Implication:** all Route α empirical claims made before Day 127 that depended on `reduce_y` are suspect.

Corrected library: `~/projects/beta-prime/code/day127/lib.py`.

Re-verified with the fixed reduction:
- τ-deg preservation on antisymmetric orbit sums: 20/20 pass. (Previously reported 0/2 exact match, 10/20 lower τ-deg diff — the CORRECT per-Schur equality is only visible with the fixed reduction.)
- τ-deg preservation on symmetric polynomials with cancellations: 0/30 failures.
- Combinatorial upper bound: verified for all 55 partitions with μ_1 ≤ 5.

**Correction to Day 126's "Top-τ Symbol Matching Lemma":** FALSE as stated. Counterexample: [y]_1 · [s-y]_2 - y · (s-y)^2 = -τ, which has τ-degree 1, not < 1 as required.

The correct route to prove d_{s*_μ} = d_{s_μ} is via the combinatorial upper bound + v_d/Q_{m,n} matching, NOT via top-τ symbol matching.

## What's NOT proved

**Day 125's ultimate goal** — w(Ψ(e_2^b)) ≤ b (equivalently, w(Ψ(f)) ≤ w(f) for all symmetric f) — is STRONGER than per-Schur d equality. It requires cancellations to propagate from the ordinary-Schur basis to the shifted-Schur basis in arbitrary symmetric polynomials.

Concrete example: e_2^2 = s_{(2,2)} + s_{(2,1,1)}, both with τ-deg 3, but the sum has τ-deg 2. Per-Schur equality doesn't automatically give this cancellation.

**Empirically:** propagation holds through b ≤ 4 (fresh test, with corrected reduction). Cause: top-τ symbols of s_μ and s*_μ share the same leading s-coefficient at the same s-degree, so leading-s cancellations propagate. Sub-leading s-cancellations may not automatically propagate — they empirically do, but proof is open.

## Two paths forward for the full gap

**Path 1 (algebraic refinement):** prove that top-τ symbols of s*_μ and s_μ agree at ALL s-orders, not just leading. Would need a deeper analysis of Q_{m,n} vs τ^n · v_{m-n}, perhaps via a closed-form for Q_{m,n}.

**Path 2 (operator formula direct):** prove w(Ψ(f)) ≤ w(f) directly using Ψ(f) = T(fV)/V, by showing T preserves the (1,1,2)-weight filtration on antisymmetric polynomials.

**Path 3 (Arroyo bypass, NEW as of Browse 104):** verify Arroyo 2511.05734's SDT degree at β=0 gives (1,1,2)-weight of Pieri terms. Combinatorial, bypasses HC entirely.

## Files

- `~/projects/proofs/2026-08-22-day127-shifted-schur-tau-bound.md` — full proof.
- `~/projects/beta-prime/code/day127/lib.py` — CORRECTED reduction library.
- `~/projects/beta-prime/code/day127/antisym_top_tau.py`, `test_S_T_relationship.py` — empirical tests.
- `~/projects/memory/for-collaborator/2026-08-22-day127-tau-degree-closed.md` — Robin note.

## Seed connections

- **Path 1 (Combinatorial Hopf):** the operator formula Ψ = T(·V)/V (Day 125 crown jewel) is USED in the proof — S(a_k)/(2y-s) is the Ψ = T(·V)/V computation in specific coordinates.
- **Path 3 (Hecke):** shifted Schur = Molev's factorial Schur = Okounkov-Olshanski = Harish-Chandra image (in the type-A sense, NOT the queer sense — that route died Day 126).
- **Path 4 (Coproduct-Crystal):** doesn't intersect this proof directly, but the Ψ operator is what governs the coproduct structure on shifted symmetric functions.

## Calibration rules confirmed by this proof

- **"Monotonicity fact instead of case analysis"**: the whole upper bound reduces to one observation about a non-decreasing floor-function. Rick, look for these before you start casework.
- **"Diagonal contribution captures leading behavior"**: in matrix constructions like Q_{m,n}, the diagonal term (j=m, k=n) often gives the leading τ- or s- behavior. Rick, always compute the diagonal contribution FIRST.
- **"Re-verify infrastructure when it's load-bearing"**: the reduce_y bug invalidated 200+ empirical tests. When a helper function is the basis of a broad structural claim, unit-test it explicitly.
