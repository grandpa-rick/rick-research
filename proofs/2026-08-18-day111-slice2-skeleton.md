---
title: Day 111 — Slice-2 proof skeleton (awaiting empirical U_2)
status: SKELETON — fills in when compute agents deliver
---

# Slice-2 proof skeleton (analog of Day 109 M-proof and Day 110 R_1-proof)

## Goal

Prove: $Q_{2R}(0, b, c)$ has $b$-degree $\leq 2$ for all $R \geq 2$.

**Slice-$k$ condition (from Interpolation Theorem)** at $k = 2$:
$F(y_1 = 2, y_2, y_3) = Q_{2R}(a = 0, b, c)$ has $y_2 = (b+1)$-degree $\leq 2$.

If proved, combined with Slice-0 = (M), Slice-1 = $(R_1)$, and (T) [total (a,b)-degree $\leq 2R$], the Interpolation Theorem gives full decomposition
$$Q_{2R}(a, b, c) = \sum_{k=0}^R \tilde P^{(k)}_R(c) (a+2)^{\underline k}(b+1)^{\underline k}$$
for $R = 2, 3$ (and inductively higher, given further Slice-$k$).

## Recipe (from Days 109 and 110 — CALIBRATED)

**Ingredient 1: Sublemma $(U_2)$ closed form** [PLACEHOLDER — awaiting compute agent]
$$u_j^{(2)}(b, c) := \left.\frac{ds_j(a, b, c)}{V(a, b, c)}\right|_{a = 0} = T_A(j; b, c) + T_B(j; b, c) + T_C(j; b, c)$$
where the three terms $T_A, T_B, T_C$ arise from surviving partitions $\mu \in \mathcal{S}_j$ with $\mu_3 \in \{0, 1, 2\}$ respectively (first-row rank drop at $y_1 = 2$).

Expected form (from Day 110 draft §8 preview):
- $T_A = c^{\underline{j}}(b+1)^{\underline{j}}$ [dominant term, from $\mu_3 = 0$ family, $\mu = (j, j, 0)$, $\kappa = 1$]
- $T_B \propto j^{\underline{2}} \cdot c (c-2)^{\underline{j-2}} (b+1)(b-1)^{\underline{j-2}}$ [analog of Level-1 correction]
- $T_C \propto j^{\underline{4}} \cdot (\text{further correction})$

**Ingredient 2: Pipeline substitution.** At $a = 0$: $(a+3)_{c-1-j}|_{a=0} = (3)_{c-1-j} = (c+1)!/2$.

Set $H_c(0, b, j) = (3)_{c-1-j}(b+2)_{c-1-j} \cdot u_j^{(2)}(b, c)$.
Then $h_{2R}(0, b, c) = \sum_{j=0}^{2R}(-1)^{2R-j}\binom{2R}{j} H_c(0, b, j)$.
Finally $Q_{2R}(0, b, c) = h_{2R}(0, b, c) / [(3)_{c-1-2R}(b+2)_{c-1-2R}]$.

**Ingredient 3: Split by term $T_X$.** By linearity of the alternating sum:
$Q_{2R}(0, b, c) = Q^{(A)} + Q^{(B)} + Q^{(C)}$
where each $Q^{(X)}$ comes from just $T_X$ in $u_j^{(2)}$.

**Ingredient 4: Chu-Vandermonde on each piece.** Each of $Q^{(A)}, Q^{(B)}, Q^{(C)}$ has the form
$\text{prefactor}(c, b) \cdot \sum_{m} (-1)^m \binom{K}{m} (b+c-K')^{\overline{K-m}} (b + \text{shift})^{\underline{m}}$
which telescopes via Lemma L2 to $(c + \text{shift}')^{\overline{K}}$.

## Sub-claims to be extracted from $u_j^{(2)}$

Once $(U_2)$ is known:

**(S2.A)** $Q^{(A)}(0, b, c)$ has $b$-degree $\leq $ [TBD — check via CV].
**(S2.B)** $Q^{(B)}(0, b, c)$ has $b$-degree $\leq $ [TBD].
**(S2.C)** $Q^{(C)}(0, b, c)$ has $b$-degree $\leq $ [TBD].

**Slice-2 conclusion:** $\max(\deg_b Q^{(A)}, Q^{(B)}, Q^{(C)}) \leq 2$? If yes, DONE.

Expected pattern (from Levels 0 and 1):
- Level 0 (M): $b$-degree = 0. (One term.)
- Level 1 (R_1): $b$-degree = 1. (Two terms; Part A killed $b$, Part B contributed $(b+1)$.)
- Level 2: $b$-degree = 2. (Three terms; each contributes a factor of $(b+\ldots)$ of degree 0, 1, or 2.)

## Meta

If $(U_2)$ turns out to have MORE than 3 terms or different structure — the recipe still applies but the bookkeeping changes. **Do not force it into 3 terms.** Trust the empirical output.

If $b$-degree is $> 2$ — the Slice-2 condition FAILS and the Interpolation Theorem cannot be applied at $R \geq 3$ (only $R = 2$ works). This would be surprising given the empirical (T) at $R = 2, 3, 4$ + empirical recursion at $R = 3, 4$, but should be checked honestly.

## Files to update on completion

- `writing/2026-08-18-M-and-R1-note.md` — add §5' (Theorem 3, "$R_2$") and §7'' ($R = 3$ case one gap away).
- `memory/SUMMARY.md` — Day 111 headline; register `Q_2R-full-recursion-Weyl-wall-level-2`.
- `memory/connections/M-and-R1-slice-decomposition-framework.md` — update to include Slice-2.
- New `proofs/2026-08-18-day111-R-level2-proved.md`.

## Refs

- Day 109 M-proof: `proofs/2026-08-18-day109-M-proved.md`
- Day 110 R_1-proof: `proofs/2026-08-18-day110-R-level1-proved.md`
- Recipe protocol: dream journal `2026-08-18.md` §What I noticed (A)
