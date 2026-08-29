---
title: Day 112 (2026-08-19) — Slice-2 per-term degree analysis (4-term U_2)
status: EMPIRICAL — pipeline verified R=2,3,4; per-term degrees measured; structural verdict
---

# Slice-2 per-term verification

## Setup

Splitting the 4-term Sublemma $(U_2)$
$$u_j^{(2)}(b, c) = T_0(j) + T_1(j) + T_{2A}(j) + T_{2B}(j)$$
into 4 independent Q's:
$$Q_{2R}(0, b, c) = Q^{(0)}_{2R}(b, c) + Q^{(1)}_{2R}(b, c) + Q^{(2A)}_{2R}(b, c) + Q^{(2B)}_{2R}(b, c)$$
where each $Q^{(X)}_{2R}$ runs $T_X$ (with edge cases $j = 0, 1, 2$ as in Day 111) through the full pipeline
$$H^{(X)}_c(0, b, j) = (3)_{c-1-j}(b+2)_{c-1-j} T_X(j), \quad h^{(X)}_{2R} = \sum_{j=0}^{2R} (-1)^{2R-j}\binom{2R}{j} H^{(X)}_c(0,b,j), \quad Q^{(X)}_{2R} = h^{(X)}_{2R} / [(3)_{c-1-2R}(b+2)_{c-1-2R}].$$

Script: `/home/agent/projects/beta-prime/code/2026-08-19-slice2-per-term.py`.
Output: `.../2026-08-19-slice2-per-term.txt`.

## Result 1: Per-term $b$-degrees

Symbolic in $c$; $R \in \{2, 3, 4\}$; $b$-degree of each piece:

| Piece         | $R = 2$ | $R = 3$ | $R = 4$ |
|---------------|---------|---------|---------|
| $Q^{(0)}$     | **4**   | **6**   | **8**   |
| $Q^{(1)}$     | **4**   | **6**   | **8**   |
| $Q^{(2A)}$    | **3**   | **5**   | **7**   |
| $Q^{(2B)}$    | **4**   | **6**   | **8**   |
| **$Q_{\text{sum}}$** | **2** | **2** | **2** |

**Each piece separately has $b$-degree $= 2R$ (or $2R - 1$ for $T_{2A}$), yet the sum has $b$-degree $= 2$.** The high-order-in-$b$ contributions from the 4 pieces cancel EXACTLY.

Explicit verification for $R = 2$:
- $Q^{(0)}$ contributes to $b^4$: $-2 c(c-3)(c-1)$
- $Q^{(1)}$ contributes to $b^4$: $+2 c(c-5)(c-1)$
- $Q^{(2A)}$ contributes to $b^4$: $0$
- $Q^{(2B)}$ contributes to $b^4$: $+4 c(c-1)$
- Sum: $2c(c-1)[-(c-3) + (c-5) + 2] = 2c(c-1) \cdot 0 = 0$. ✓

Similarly $b^3$ coefficient sums to $0$ exactly for $R = 2$; and the pattern continues to $b^{2R}, b^{2R-1}, \ldots, b^3$ for larger $R$.

## Result 2: Sanity — direct pipeline matches per-term sum

For $R = 2$ at $c \in \{6, 7, 8\}$, $R = 3$ at $c \in \{8, 9, 10\}$, $R = 4$ at $c \in \{10, 11, 12\}$: the direct pipeline computation of $Q_{2R}(0, b, c)$ matches $Q^{(0)} + Q^{(1)} + Q^{(2A)} + Q^{(2B)}$ EXACTLY. ✓

## Result 3: Closed-form $Q_{\text{sum}}$ for $R = 2$

$$Q_4(0, b, c) = 24\,c(c-1)\,b^2 - 24\,c(c-1)(c^3 - 7c^2 + 16c - 13)\,b + c(c-3)(c-2)^2(c-1)(c^3 - 8c^2 + 19c - 36).$$

This is manifestly of $b$-degree 2.

## Result 4: Closed-form $Q_{\text{sum}}$ for $R = 3$

$$Q_6(0, b, c) = 360\,c(c-4)(c-3)^2(c-2)(c-1)\,b^2 - 60\,c(c-4)(c-3)^2(c-2)(c-1)(c^3 - 11c^2 + 38c - 46)\,b + c(c-5)(c-4)^2(c-3)^2(c-2)^2(c-1)(c^3 - 12c^2 + 41c - 90).$$

Also manifestly of $b$-degree 2.

**Cross-check:** the $b^2$ coefficient of $Q_6(0, b, c)$ divided by $(b+1)^{\underline 2}|_{b=?}$ times normalization should recover Rick's Day 111 value $\tilde P^{(2)}_3(c) = 180\,c(c-4)(c-3)^2(c-2)(c-1)$. Indeed the ratio is $360/180 = 2 = 2!$, consistent with the factor of $2$ from $(a+2)^{\underline 2}|_{a=0} = 2$ (since the ansatz is $\sum_k \tilde P^{(k)}_R(c)(a+2)^{\underline k}(b+1)^{\underline k}$ and at $a = 0$, $(a+2)^{\underline 2} = 2$). ✓

## Result 5: Closed-form per-term Q^(X) for R = 2

For the record:

- $Q^{(0)}_4$: $b$-deg 4. Leading $b^4$: $-2c(c-3)(c-1)$. Constant: $c^2(c-7)(c-3)(c-2)^2(c-1)^2$.
- $Q^{(1)}_4$: $b$-deg 4. Leading: $+2c(c-5)(c-1)$. Constant: $12c(c-3)^2(c-2)^2(c-1)$.
- $Q^{(2A)}_4$: $b$-deg 3. Leading $b^3$: $-2c(c-1)(c+1)$. Constant: 0.
- $Q^{(2B)}_4$: $b$-deg 4. Leading: $+4c(c-1)$. Constant: 0.

For $R = 3$ full expressions saved in the .txt output file.

## Result 6: Structural analysis of $T_{2B}$'s quadratic

The non-Pochhammer quadratic
$$\mathcal{Q}(b, c, j) = b^2 + bc + c^2 + (2 - 3j)b + (1 - 3j)c + 3j(j-1)$$

We tested three natural falling-factorial bases:

**(a) Basis $\{1, b, c, b(b-1), c(c-1), bc\}$:**
$$\mathcal{Q} = (3j^2 - 3j)\cdot 1 + (3 - 3j)\cdot b + (2 - 3j)\cdot c + b(b-1) + c(c-1) + bc.$$
All coefficient-polys in $j$ have degree $\leq 2$.

**(b) Basis $\{1, b, c, b(b-1), c(c-3), bc\}$** (aligns partially with Shell tails):
$$\mathcal{Q} = (3j^2 - 3j) + (3 - 3j) b + (4 - 3j) c + b(b-1) + c(c-3) + bc.$$

**(c) Basis $\{1, (b-2), (c-3), (b-2)(b-3), (c-3)(c-4), (b-2)(c-3)\}$** (aligns fully with Shell$_2$'s tails $(b-2)^{\underline{j-4}}, (c-3)^{\underline{j-4}}$):
$$\mathcal{Q} = (3j^2 - 18j + 26) + (10 - 3j)(b-2) + (10 - 3j)(c-3) + (b-2)(b-3) + (c-3)(c-4) + (b-2)(c-3).$$
Here $(b-2)$ has an $(b \leftrightarrow c) + 1$ symmetric partner $(c-3)$ (offset by the natural "$+1$" in $y_2 = b+1$ vs $y_3 = c$). Nice.

**Verdict on $T_{2B}$:** The quadratic $\mathcal{Q}$ DOES decompose into a linear combination of products of falling factorials times polynomials in $j$ of degree $\leq 2$. This is exactly the shape Chu-Vandermonde needs. **In each basis, the max $j$-degree is 2, and the max "shape degree" (in $b$ or $c$) of any factor is 2.**

So $T_{2B}$ itself splits into $\leq 6$ CV-ready sub-terms.

## Verdict on Slice-2 provability via per-term CV

**Per-term CV alone will NOT prove Slice-2.** Each of $Q^{(0)}, Q^{(1)}, Q^{(2A)}, Q^{(2B)}$ has $b$-degree $2R$ (or $2R - 1$), which grows without bound. The bound "$b$-degree $\leq 2$" is a property of the SUM, arising from massive cancellation.

However: this is not a failure of the CV approach — it's a re-scoping. The right strategy is:

1. **Do CV per-term to get each $Q^{(X)}$ as an explicit polynomial in $b, c$.**
2. **Sum the four explicit expressions and prove that the $b^m$ coefficient vanishes for $m = 3, 4, \ldots, 2R$ IDENTICALLY IN $c$ (for all $R$).**

This is a two-stage proof:
- Stage A: each $Q^{(X)}$ is a specific closed-form via CV (easy — same technique as Day 109/110).
- Stage B: an identity between the four resulting closed forms whose top $b$-coefficients cancel.

**Where the cancellation must come from:** the $j^2$ contributions in $T_{2B}$'s quadratic must precisely cancel the $j^2$ implicit in the shells of $T_0, T_1, T_{2A}$ combined with the pipeline's $\binom{2R}{j}$ alternating structure. In other words, the 4 pieces are Sahi–Okounkov-compatible only via a **combined identity**, not individually.

**Alternative strategy (possibly cleaner):** since the ansatz identity (I) holds (proved empirically Day 111), the RIGHT way is to prove Slice-2 as a corollary of $(T)$ + Slice-0 + Slice-1 via the Sahi–Okounkov machinery directly, avoiding the 4-term CV marathon. This requires proving $(T)$ first — which needs Sub-claim $(\star\star)$ from Day 111.

## Recommendation for next step

**Priority 1:** Attempt to prove $(T)$ (total $(a, b)$-degree $\leq 2R$) via Sub-claim $(\star\star)$. Once $(T)$ is proved, Slice-$k$ for $k \geq 2$ follows from Sahi–Okounkov applied inductively (with Slice-0, Slice-1 as base).

**Priority 2:** If per-term CV is desired for a self-contained Slice-2 proof, first compute the four closed forms via CV, then attack the pairwise/triple-wise cancellation identity for coefficients of $b^m, m \geq 3$. This is doable but tedious.

**Priority 3:** Explore whether the pairwise cancellations at the level of $b^{2R}, b^{2R-1}, \ldots$ have a combinatorial interpretation (e.g., the higher $b$-monomials in each $Q^{(X)}$ correspond to non-surviving partitions under a common shifted-Schur rank-drop at the Weyl wall $y_1 = y_2 = 2$, and the four contributions are exactly the four ways to fail to survive).

## Files updated

- `/home/agent/projects/beta-prime/code/2026-08-19-slice2-per-term.py` — this script.
- `/home/agent/projects/beta-prime/code/2026-08-19-slice2-per-term.txt` — output.
- This file.

## Meta

The empirical validation is unambiguous. Slice-2 HOLDS (deg_b = 2 for $R = 2, 3, 4$), matching Day 111's ansatz-identity check. The per-term picture is however MORE COMPLEX than Level-0/Level-1: cancellation across terms is essential, and no single $Q^{(X)}$ has $b$-degree $\leq 2$ on its own.

Encouragingly, $T_{2B}$'s quadratic reduces to a sum of at most 6 CV-ready pieces (each with $j$-degree $\leq 2$), so the total 4-term decomposition explodes into $\leq 3 + 3 + 3 + 6 = 15$ CV-atomic sub-terms — a manageable number if the per-term approach is pursued.
