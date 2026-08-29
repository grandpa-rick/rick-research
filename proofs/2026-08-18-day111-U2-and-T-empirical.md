---
title: Day 111 (2026-08-18 wake) — Empirical Sublemma (U_2), (T) mechanism, Sahi–Okounkov attribution
status: EMPIRICAL — formal Slice-2 proof is next PROVE.md target
---

# Day 111 wake results

## Setting

Continuation of Days 108–110 (M) + (R_1) proof program. Today's dispatches:
1. Sublemma $(U_2)$ empirical closed form at $y_1 = 2$ (i.e., $a = 0$).
2. Total-degree bound (T) — investigation of the mechanism.
3. Interpolation Theorem literature check.

## Result 1: Sublemma $(U_2)$ empirical, 4 terms

**Verified for $j = 0, 1, \ldots, 12$.**

For each $j \geq 4$, define shells
$$S_p(j) := c(c-1)(c-3)^{\underline{j-2-p}} \cdot (b+1)b(b-2)^{\underline{j-2-p}}, \qquad p \in \{0, 1, 2\}.$$

Then
$$u_j^{(2)}(b, c) := \left.\frac{ds_j(a, b, c)}{V(a, b, c)}\right|_{a = 0} = T_0 + T_1 + T_{2A} + T_{2B}$$
where
- $T_0(j) = S_0(j)$ — from $\mu_3 = 0$ sub-family (unique $\mu = (j, j, 0)$, $\kappa = 1$).
- $T_1(j) = 2(j-1) \cdot S_1(j) \cdot (b + c - 2j)$ — from $\mu_3 = 1$ sub-family.
- $T_{2A}(j) = (j-1)(j-2) \cdot S_1(j)$ — from $\mu_3 = 2$, $\mu_2 = j-1$ sub-sub-case.
- $T_{2B}(j) = j(j-3) \cdot S_2(j) \cdot [b^2 + bc + c^2 + (2-3j)b + (1-3j)c + 3j(j-1)]$ — from $\mu_3 = 2$, $\mu_2 = j - 2$ sub-sub-case.

Edge cases:
- $u_0 = 1$
- $u_1 = bc + b + 2c$
- $u_2 = c(b+1)(bc + b + 2c - 6)$, with $T_0(2), T_1(2) = 2c(b+1)(b+c-3)$ and $T_{2A}, T_{2B} = 0$ (vanishing prefactors).

**Structural surprise.** Expected 3 terms (one per $\mu_3 \in \{0, 1, 2\}$) based on Level-0/1 pattern. Instead:
- $\mu_3 = 2$ is NOT a single sub-family; it partitions further by $\mu_2$.
- $\mu_2 = j-1$ gives a clean scalar $(j-1)(j-2)$ contribution.
- $\mu_2 = j-2$ (the "true interior" of $\mu_3 = 2$) gives a non-Pochhammer quadratic factor $b^2 + bc + c^2 + \ldots$ that is NOT $(b \leftrightarrow c)$-symmetric.

This suggests: **at Level $k$, sub-family $\mu_3 = r$ further partitions into sub-sub-cases by $\mu_2$** — total number of terms in $(U_k)$ is $\geq k + 1$ but potentially larger. Pattern needs re-calibration.

**Pipeline consistency check.** Recovering $Q_{2R}(0, b, c)$ from the 4-term ansatz matches the direct pipeline computation for $R = 2$ ($c = 5..9$) and $R = 3$ ($c = 7..10$). Independently: peeling $Q_{2R}(0, b, c)$ per Day-108 recursion recovers $\tilde P_R^{(2)}(c)$ exactly for $R = 3$ ($c = 8, 10$) and $R = 4$ ($c = 10, 12$). ✓

**Slice-2 status:** implied by empirical (U_2) via pipeline + Chu-Vandermonde, but formal proof pending — 4 terms means 4 separate Chu-Vandermonde-style applications, one of which (from $T_{2B}$) requires handling a non-standard quadratic factor.

Files: `/home/agent/projects/beta-prime/code/2026-08-19-U2-empirical.{py,txt}`.

## Result 2: Total-degree bound (T) — mechanism + ansatz-identity

**Empirical (T):** $Q_{2R}(a, b, c)$ has total $(a, b)$-degree exactly $2R$ for $R = 2, 3, 4, 5$. Individual $a$- and $b$-degrees are each exactly $R$.

**Empirical ansatz identity (I):** For $R = 2, 3$, the interpolation ansatz
$$Q_{2R}(a, b, c) = \sum_{k=0}^R \tilde P_R^{(k)}(c) \cdot (a+2)^{\underline k} (b+1)^{\underline k} \tag{I}$$
holds identically (verified over many $c$ values). So (T) is not merely IMPLIED by the ansatz — the ansatz IS the identity, and (T) is a trivial consequence of it once proved.

**Structural mechanism of (T).** Top part of $H_c(a, b, j)$ in $(a, b)$ is $a^{c-1} b^{c-1}$, $j$-independent. Alternating sum $\sum_{j=0}^{2R} (-1)^{2R-j} \binom{2R}{j} \cdot 1 = 0$ kills the top layer. This iterates $2R$ times because at layer $d < 2R$ down from top, the coefficient is a polynomial in $j$ of degree $\leq d < 2R$ (Sub-claim (⋆⋆) in `2026-08-18-day111-T-bound-proof-sketch.md`), and finite differences of order $2R$ annihilate polynomials in $j$ of degree $< 2R$.

**Missing piece:** rigorous verification of Sub-claim (⋆⋆) — that the $r$-th sub-family layer ($\mu_3 = r$) of $ds_j/V$ contributes a polynomial in $j$ of degree $\leq r$ to the layer at $(a, b)$-degree $2j - r$. Empirical evidence via (U_1) and (U_2) supports this: (U_1) has $j$-degrees $0, 2$; (U_2) has $j$-degrees $0, 1, 2, 2$ (max = 2). Consistent with degree $\leq r$ at sub-family $\mu_3 = r$.

**New found closed form for $R = 3$:**
$$\tilde P^{(2)}_3(c) = 180 c(c-4)(c-3)^2(c-2)(c-1), \quad \tilde P^{(3)}_3(c) = -120 c(c-2)(c-1).$$

Files: `/home/agent/projects/beta-prime/code/2026-08-19-T-bound-investigation.{py,txt}`.

## Result 3: Interpolation Theorem is Sahi–Okounkov

**Attribution:** Rick's "Interpolation Theorem" is the $n = 2$, universal-grid ($\Omega(i, j) = j$) case of the Newton interpolation scheme for symmetric polynomials due to Sahi (1996) and axiomatized by Okounkov (1998):

- Sahi, S. "Interpolation, integrality, and a generalization of Macdonald's polynomials." *IMRN* 1996(10), 457–471.
- Okounkov, A. "On Newton interpolation of symmetric functions: A characterization of interpolation Macdonald polynomials." *Adv. Appl. Math.* 20 (1998), 395–428. arXiv:q-alg/9712052. See Proposition 2.6 and §6 (two-variable proof attributed to Sahi).

**Consequence for the write-up:** the interpolation half-page becomes a "we record for convenience (Sahi–Okounkov)" lemma with citation. Not a Rick-named theorem. Saves the writeup from a false-priority claim.

Local copy: `/tmp/okounkov.pdf` (may be gone across container restart; downloadable from arXiv).

## Assessment

**Progress toward $(\star)$ uniform:**

| Component | Status |
|-----------|--------|
| (M) = Slice-0 | PROVED Day 109 |
| (R_1) = Slice-1 | PROVED Day 110 (up to Sublemma (U_1) for $j \leq 16$) |
| (U_2) empirical | Verified $j \leq 12$ Day 111 |
| Slice-2 formal | Awaiting Chu-Vandermonde marathon on 4-term (U_2) |
| Slice-$k$ for $k \geq 3$ | Analog sub-lemmas required |
| (T) empirical | $R = 2, 3, 4, 5$ Day 111 |
| (T) formal | Sub-claim (⋆⋆) sketch in place; needs verification |
| Ansatz identity (I) empirical | $R = 2, 3$ Day 111 |
| Interpolation Theorem | Sahi-Okounkov 1996/1998 |

**$R = 3$ case within reach:** would need Slice-2 formal + (T) formal + Slice-3 (probably follows trivially from individual $b$-degree bound if that's proved separately).

**Next PROVE session focus:** Slice-2 formal proof — the Chu-Vandermonde marathon on the 4-term (U_2). Highest leverage.
