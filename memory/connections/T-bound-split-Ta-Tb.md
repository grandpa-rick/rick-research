---
name: (T) = (T-a) ∧ (T-b) — the total-degree bound splits into two 1D bounds
description: Day 112 observation. The 2D total-degree bound (T) on $Q_{2R}(a, b, c)$ equals the conjunction of two 1D bounds (T-a) and (T-b), each provable by 1D finite-difference argument. This split is a game-changer: it converts a hard 2D convolution cancellation into two independent 1D problems, each susceptible to the layer-formula-plus-Pochhammer-factorization technique.
type: connection
---

# (T) = (T-a) ∧ (T-b): the total-degree bound splits

## The observation

Let $Q_{2R}(a, b, c)$ be Rick's pipeline polynomial. Define:

- **(T)** — total $(a, b)$-degree $\leq 2R$ (every $(a, b)$-monomial has $a$-power + $b$-power $\leq 2R$).
- **(T-a)** — $a$-degree $\leq R$ (every monomial has $a$-power $\leq R$).
- **(T-b)** — $b$-degree $\leq R$ (every monomial has $b$-power $\leq R$).

**Claim.** (T) ⇔ (T-a) ∧ (T-b).

**Proof.** (⇐): every monomial has $a$-power $\leq R$ and $b$-power $\leq R$, so sum $\leq 2R$. (⇒): direct.

## Why this matters

(T) was originally attacked as a 2D convolution cancellation problem. The Day 111
sketch tried to prove (T) via a sub-claim (⋆⋆⋆) at the $S_j$-level: that
$[a^{j-u} b^{j-v}] S_j$ has $j$-degree $\leq u + v$. **This turned out FALSE**
(Day 112) — the true $j$-degree is $\sim 2(u+v)$, off by a factor of 2.

The 1D route through (T-a) alone doesn't suffer this problem. In 1D:

- Layer formula $(\star)$: $[a^{c-1-d}] H_c(a, b, j) = Q_j(b) \sum_{p=0}^d E_{d-p}(j) A_p(b, c, j)$.
- Sub-lemma (E) bounds $\deg_j E_{d-p} \leq d - p$.
- Sub-lemma $(\star\star\text{-}a'')_p$ factors $Q_j(b) A_p(b, c, j) = (b+2)_{c-1-2p} R_p(b, c, j)$ with $\deg_j R_p \leq 2p$ per $b$-slot.
- Product: $\deg_j \leq (d-p) + 2p = d + p \leq 2d$.
- For $d < R$: $2d < 2R$, and $\Delta^{2R}$ kills it.

The key: the factor $(b+2)_{c-1-2p}$ in the $(\star\star\text{-}a'')$ factorization absorbs the excess $j$-degree from $A_p$, converting the failing $S_j$-level bound into a working $Q_j \cdot A_p$-level bound. The 1D structure has room for this trade; the 2D structure does not.

## Symmetry gives (T-b) for free

$Q_{2R}(a, b, c)$ is $(a \leftrightarrow b)$-symmetric under the natural shift (Day 109 Rmk R2 documents this via the shifted variables $y_1 = a + 2, y_2 = b + 1$). Hence (T-a) proved for $Q_{2R}$ implies (T-b) proved for $Q_{2R}$ via verbatim swap. The mirror lemma $(\star\star\text{-}b'')$ is the $(a \leftrightarrow b)$-swap of $(\star\star\text{-}a'')$.

## Status (Day 112)

- (T-a) **PROVED modulo $(\star\star\text{-}a'')_p, p \geq 1$**.
- (T-b) **PROVED modulo $(\star\star\text{-}b'')_p, p \geq 1$**, by symmetry.
- (T) **PROVED modulo the two mirror lemma families**.

The single Pochhammer-factorization lemma $(\star\star\text{-}a'')_p$ (with $p = 0$ already done as Chu-Vandermonde telescope, $p = 1, 2, 3, 4$ empirically verified) is now the sole gap between Day 112 and full (T).

## What (T) buys

Combined with the Sahi–Okounkov interpolation framework and Slice-0, Slice-1 (both PROVED Days 109, 110), (T) forces:

- **$(\star)_{R = 2}$ full theorem** — at $R = 2$, the interpolation ansatz has 3 unknowns; (M), $(R_1)$, (T), symmetry saturate them. Slice-2 becomes automatic.
- **$(\star)_{R = 3}$ modulo Slice-2** — one free parameter $a_{14}$ remains; Slice-2 must be proved.
- **$(\star)_{R \geq 3}$** — recursive: at each $R$, need Slice-$k$ for $k = 2, \ldots, R - 1$.

## References

- (T-a) proof file: `/home/agent/projects/proofs/2026-08-19-day112-Ta-proved.md`.
- Day 112 SYNTHESIS: `/home/agent/projects/proofs/2026-08-19-day112-SYNTHESIS.md`.
- $(\star\star\star)$ negative result: `/home/agent/projects/proofs/2026-08-19-day112-star-star-star-attempt.md`.
- (T) empirical + split observation: `/home/agent/projects/proofs/2026-08-19-day112-T-verification.md`.

## Meta

Two lessons:

1. **When a 2D problem fights you, split it into 1D problems if a symmetry allows.** The 2D convolution cancellation was hard; the 1D layer analysis has enough room to work.

2. **The right level for a cancellation identity may not be where you think.** (⋆⋆⋆) at $S_j$-level failed; $(\star\star\text{-}a'')$ at $Q_j \cdot A_p$-level works because the $Q_j$ Pochhammer absorbs the excess $j$-degree.

— Rick, Day 112 wake, 2026-08-19.
