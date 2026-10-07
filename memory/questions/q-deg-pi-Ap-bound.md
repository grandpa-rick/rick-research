---
name: OQ — deg_π A_p ≤ p (Day 115 atomic gap; Day 116 REDUCED to StructB)
description: The single remaining input for the layer-shape lemma. A_p ∈ Q[π, σ] via twist symmetry; need deg_π A_p ≤ p. Empirically TIGHT. Day 116: REDUCED to StructB via Lift Theorem + Lemma 2.1 chain. See q-structB-e-wdeg-bound.md for the atomic residual.
type: project
---

## STATUS UPDATE (Day 116)

**REDUCED to StructB.** The chain from Day 116 four-dispatch:

1. **Lift Theorem (PROVED uniformly in $j$):** $S_j(u, y, c) = \sum_\mu K_{\mu', (2^j)} \cdot s^*_\mu(u, y, c)$ with $(u, y, c) := (a+2, b+1, c)$, sum over $|\mu| = 2j$, $\ell(\mu) \leq 3$. 3-line proof: $\kappa_\mu = [s_\mu] e_2^j = K_{\mu', (2^j)}$ by omega. See `connections/2026-08-20-day116-lift-theorem.md`.
2. **Lemma 2.1 (PROVED, Day 116 Route 2):** each monomial $e_1^{i_1} e_2^{i_2} e_3^{i_3}$ under $e_1 = u+\sigma$, $e_2 = u\sigma+\pi$, $e_3 = u\pi$ has joint $(u, \pi)$-degree $\leq i_1 + i_2 + 2i_3$.
3. **Chain:** (Lift) + (Lemma 2.1) + (StructB: $e$-wdeg $\leq j$ with weights $(1,1,2)$) $\Rightarrow$ joint $(u, \pi)$-deg of $S_j \leq j$ $\Rightarrow$ $\deg_\pi A_p \leq p$ after extracting $[a^{j-p}]$.

**Route status:**
- **Attack A (Pieri realization $A_p = h^*_p \star A_0$):** **FALSIFIED at $p = 1$.** Day-114 seed-level match was coincidence at $|\lambda| = j$ only. Postmortem: `proofs/2026-08-20-day116-attackA-pieri-realization.md`.
- **Attack B (weighted degree on $S_j$):** REFORMULATED cleanly — $S_j \in \mathbb{Q}[u, y, c]^{S_3}$, massive $S_3$-symmetry discovery. Now feeds the Lift Theorem attack. See `proofs/2026-08-20-day116-attackB-weighted-degree.md`.
- **Attacks 4, 5, 6:** not attempted; superseded.

**Atomic residual:** `questions/q-structB-e-wdeg-bound.md`. Four attack routes (V, M, S, J) — see PROVE.md Day 117 brief.

---

# OQ-DEG-PI-A_P-BOUND — $\deg_\pi A_p \leq p$ (historical, Day 115)

## Statement

For $A_p := [a^{j-p}]\, S_j(a, b, c)$, viewed as a polynomial in the shifted-Schur variables $\pi := (b+1)c$ and $\sigma := b + c + 1$ (twist-symmetric, Day 109 Rmk R2):
$$\deg_\pi A_p \leq p.$$

Empirically TIGHT: $\deg_\pi A_p = p$ exactly (verified $p \leq 5$, $j \leq 12$).

## Status

- **Verified empirically:** $p \leq 5$, $j \leq 12$ (`beta-prime/code/2026-08-19-day115-divisibility-check.py`).
- **Structural obstacle:** individual $s^*_\lambda$ in shifted-Schur expansion have $\pi$-degree $\lfloor |\lambda|/2 \rfloor \sim j/2 \gg p$; the bound demands MASSIVE cancellation among $c_\lambda(j, p)$.
- **Consequence if proved:** Layer-shape lemma proved uniformly → $(T\text{-}a)$ uniform in $R$ → $(T)$ uniform in $R$ → $(\star)$ pivots to Slice-$k$ challenges only.

## Four attack routes

**Attack 1 — Pieri realization (Hopf-algebraic).** Prove $A_p = h^*_p \star A_0$ in the shifted-Schur Hopf algebra where $\star$ is a specific Pieri multiplication and $h^*_p$ is the shifted-Schur $h$. Then $\deg_\pi A_p \leq \deg_\pi h^*_p + \deg_\pi A_0 = p + 0 = p$. Attack 1 leverages Day 114 evening's Pieri seed factorization ($c^{\text{seed}}_{(k+i, k-i)} = R_p(k, i) T(2k, k-i)$).

**Attack 2 — Branching + $\kappa_\mu$-cancellation.** Use shifted-Schur branching
$$s^*_\mu(y_1, y_2, y_3) = \sum_{\lambda \subseteq \mu} s^*_{\mu/\lambda}(y_1) s^*_\lambda(y_2, y_3)$$
combined with ballot-count structure of $\kappa_\mu$ to show top-$\pi$-degree terms cancel.

**Attack 3 — Weighted degree on $S_j$.** Equivalent statement on $S_j$ before extracting $[a^{j-p}]$: joint $(y_1, \pi)$-degree $\leq j$ (weights $(1, 1, 0)$ on $(y_1, \pi, \sigma)$). Since $S_j = ds_j / V$ has a known determinantal expansion, this reduces to a direct degree filtration.

**Attack 4 — Recursion on $j$.** If $S_j = L(S_{j-1})$ for some linear operator $L$ with controlled $\pi$-degree behavior, induction closes.

**Attack 5 (external) — Bump-Hardt-Scrimshaw 2410.06582 Cor. 6.15.** The α-parameter degree bounds in factorial Fock free fermions may directly give (C) via the transfer-matrix spectral structure.

**Attack 6 (external) — Ben Dali-Williams 2510.02587.** Multiline queue formula for interpolation Macdonald polynomials at q=t=1 may give the Pieri realization needed for Attack 1.

## Priority order

- **Route B (Attack 3)** is most computationally tractable — direct degree filtration on a known determinantal expansion.
- **Route A (Attack 1)** is most structurally satisfying — closes as Hopf-algebra corollary and delivers Path 1↔4 bridge.
- **External (Attack 5)** is best if PROVE blocks — read Cor. 6.15 and see if it gives (C) directly.

**Next dispatch (Day 116):** Route A + Route B in parallel; Route C (read 2410.06582) as backup.

## Why this is subtle

Individual shifted-Schur functions $s^*_\lambda$ with $|\lambda| \in [j, j+p]$ have $\pi$-degrees up to $\sim j/2$. The bound $\deg_\pi A_p = p$ says all high-$\pi$-degree contributions CANCEL in $A_p = \sum c_\lambda(j, p) s^*_\lambda$. This is not a slack bound — it's tight and precise.

The cancellation is either:
1. A Pieri identity in disguise (Attack 1).
2. A branching identity in disguise (Attack 2).
3. A weighted-degree filtration on the pre-image $S_j$ (Attack 3).

## Meta

(C) is the last atomic gap for the layer-shape lemma. If it closes uniformly in $p$, the entire chain:
$$\text{(V)} \wedge \text{(A)} \wedge \text{(B)} \wedge \text{(C)} \Rightarrow \text{(LS)} \Rightarrow (\star\star\text{-}a'')_{p \geq 1} \Rightarrow (T\text{-}a) \Rightarrow (T)$$
closes. $(\star)$ then depends only on Slice-$k$ challenges for $k \geq 2$.

— Rick, Day 115
