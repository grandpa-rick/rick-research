# Q50: the V-map total is ∏(2+q_d) (side remark to Rem 4.22, proofs/ only)

For the LG(m,2m) negative-degree story: Σ_{ρ⊆κ} V(κ/ρ) ∏_{x∈κ/ρ} q_{diag(x)} = ∏_{d=0}^{m−1}(2+q_d), so Σ V = 3^m.

Why: λ/ρ an antichain ⇔ λ = ρ + (some addable boxes) ⇔ a parallel hop of "particles" (parts of the strict partition), with
the box on diagonal p being the hop p→p+1, and the diagonal box an injection from a reservoir. A V-map is a two-step hop
history with injection allowed only at step 1. A bond can't fire at both steps, so each diagonal holds ≤1 box. Legality
is site-local, which gives a 3-state transfer matrix [[2,1,1],[1,0,1],[1,1,0]] with eigenvector (2,1,1), eigenvalue 2+q.
There is also a bijection to ternary words: letter 2 means "diagonal d has a box".

Full proof: proofs/2026-10-30-q50-transfer-matrix.md. Not in any draft. It removes no dependency, so it stays a jewel.
Fold this into the 11-04 batch only if it's useful to you; otherwise ignore it.
