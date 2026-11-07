---
name: Q_k b-independence at the Weyl boundary a = −2 — SUBSUMED by (M) PROVED Day 109
description: Day 109 PROVED (M) uniformly in k. Q_k(-2, b, c) = (-1)^k c(c-k) prod(c-j)^2. Appendix F is the k=2R special case. This connection retained for historical continuity. Canonical reference is now `connections/M-master-identity-PROVED.md`.
type: project
---

# Q_k b-independence at Weyl boundary — SUBSUMED by (M) PROVED

**STATUS (Day 109):** proved uniformly in k. Canonical reference:
`connections/M-master-identity-PROVED.md`. This file retained for continuity.

# Q_k b-independence at Weyl boundary — the MASTER IDENTITY

## Day 108 upgrade

**Master identity (verified R=3, R=4, all k):**
$$Q_k(-2, b, c) = (-1)^k \cdot c \cdot (c-k) \cdot \prod_{j=1}^{k-1}(c-j)^2 \quad \text{(for } k \geq 1\text{)}$$

with $Q_0(-2, b, c) = 1$.

**Appendix F** (b-independence of $Q_{2R}(-2, b, c)$) is the special case $k = 2R$.

## What we know now

- The b-independence at $a = -2$ is a UNIVERSAL property of the whole $Q_k$
  family, not tied to any specific R.
- The c-polynomial has a clean product structure: simple zeros at $c = 0$ and
  $c = k$, double zeros at $c = 1, 2, \ldots, k-1$.
- Sign alternates $(-1)^k$.
- This suggests a **k-uniform structural proof** on the h_k → Q_k pipeline
  at $a = -2$, rather than requiring separate arguments for each R.

## Original Appendix F content (retained for context)

## Statement (verified R = 2, 3, 4)

Define $\tilde{P}_R(c) := Q_{2R}(-2, b, c) = Q_{2R}(a, -1, c)$. Then

$$\tilde{P}_R(c) = c \cdot (c - 2R) \cdot \prod_{k=1}^{2R-1} (c - k)^2 \qquad (\text{F})$$

**Three claims in one:**
1. **b-independence:** $Q_{2R}(-2, b, c)$ does not depend on $b$.
2. **a-independence:** $Q_{2R}(a, -1, c)$ does not depend on $a$.
3. **Wall-slice equality:** the two boundary slices are the SAME polynomial in $c$.

**Verification (Day 107):** R = 2, 3, 4 by direct computation from trivariate
Q via `d102.fit_Qk_bivar`. Degree count: $\deg_c = 4R$ (matches $\deg_c Q$).
Zero pattern: simple at $c = 0$ and $c = 2R$, double at $c = 1, 2, \ldots, 2R-1$.

## Structural interpretation

At $a = -2$ in the M_j argument $x = (a+2, b+1, c) = (0, b+1, c)$: the first
coordinate $x_1 = 0$. The 3×3 Jacobi-Trudi determinant has first row
$(fall(0, k_0), fall(0, k_1), fall(0, k_2))$. Since $fall(0, j) = \delta_{j, 0}$,
only terms with one $k_i = 0$ survive. This reduces the 3×3 to an effective
2×2 minor involving only $(x_2, x_3) = (b+1, c)$.

**Something in the h → Q Pochhammer division kills the residual b-dependence.**
That's the non-obvious step and the target of the proof attempt.

**Why the specific zero pattern?**
- $c = 0$ (simple): $H_c$ vanishes trivially at c = 0.
- $c = 2R$ (simple): matches the standard $c! = (2R)!$ normalization boundary
  in the h template.
- $c \in \{1, 2, \ldots, 2R-1\}$ (double): these are the "middle" c-values
  where the h template's second term acquires a doubled root from
  $\prod (a+b+c-2j)!$ combined with the Pochhammer denominator.

The pattern IS the **Weyl denominator formula shape for $GL_{2R+1}$**
(product of consecutive linear factors with the endpoint multiplicities that
one gets from character-formula degenerations).

## Consequence: recursion path to (★)

Since $Q(-2, b, c) = Q(a, -1, c) = \tilde{P}_R(c)$, define

$$Q_{2R}(a, b, c) = \tilde{P}_R(c) + (a + 2)(b + 1) \cdot \tilde{T}(a, b, c) \qquad (\text{decomp})$$

for some polynomial $\tilde{T}$.

**At $c = R$:** $\tilde{P}_R(R) = 0$ (since $(c - R)^2$ is a factor for
$1 \leq R \leq 2R-1$), so

$$Q_{2R}(a, b, R) = (a + 2)(b + 1) \cdot \tilde{T}(a, b, R).$$

The factor $(a+2)(b+1)$ is the "outermost layer" of the target closed form
$A_R(a) B_R(b)$. Iterating the same argument on $\tilde{T}$ at the NEXT
Weyl boundary ($a = -1$, $b = 0$) should peel off another layer.

**Recursion (conjectural):** for $j = 0, 1, \ldots, R-1$,

$$Q_{2R}(a, b, R) = \prod_{i=0}^{j-1}(a - i + 2)(b - i) \cdot Q^{(j)}(a, b, R)$$

where $Q^{(j)}$ is obtained by peeling $j$ Weyl-boundary factors. At $j = R$,
$Q^{(R)} = (-1)^R (2R)!$ is a constant.

**This gives a concrete proof strategy for (★).**

## Alternative viewpoint — Weyl symmetry

The GL_3 Weyl group $S_3$ acts on $x = (x_1, x_2, x_3) = (a+2, b+1, c)$ by
permutation. In the anchor-family regime, $x = (R, R+1, R)$ so $x_1 = x_3$ is
already a Weyl wall. At $a = -2$, $x_1 = 0$ pushes further into the boundary.

The b-independence at $a = -2$ means: **once $x_1 = 0$, the polynomial cares
about $(x_2, x_3)$ only via a specific Weyl-antisymmetrized combination.**
That combination is exactly $\tilde{P}_R$.

## Priority

**HIGH.** This is the concrete stepping stone for a uniform proof of the
Day 107 closed form (★). If Appendix F proves cleanly (via the M_j determinant
2×2 collapse), the whole H5′′ → (★) chain becomes theorem.

## Verification agenda

- [ ] Prove b-independence at $a = -2$ symbolically for R = 5, 6.
- [ ] Reduce the M_j 3×3 at $x_1 = 0$ to a 2×2 minor and track the b-dependence
      through the h → Q Pochhammer division.
- [ ] Verify a-independence at $b = -1$ (symmetric argument).
- [ ] Prove the wall-slice equality $Q(-2, b, c) = Q(a, -1, c)$ via a
      $(x_1 \leftrightarrow x_2)$ symmetry of the M_j template.

## Files

- `proofs/2026-08-14-H5doubleprime-proof-day107.md` — Appendix F.
- `connections/Q-closed-form-at-c-R.md` — the target closed form (★).
- `connections/H5-doubleprime-c0-triple-factorial.md` — the H5′′ corollary.
- `code/2026-07-10-hk-three-var-fit.py` — M_j pipeline (H_c template).
