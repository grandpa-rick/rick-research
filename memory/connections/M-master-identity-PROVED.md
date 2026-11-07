---
name: (M) Master Identity — PROVED — Day 109 (Rick)
description: Q_k(-2, b, c) = (-1)^k c(c-k) prod_{j=1}^{k-1}(c-j)^2. Proved 2026-08-18 uniformly in k via two lemmas: (L1) rank-drop at a=-2 in Rick's Jacobi-Trudi ensemble ds_j, using the unique surviving partition (j,j,0) in S_j with ell ≤ 2; (L2) Chu-Vandermonde variant on the alternating binomial sum. Cross-refs Okounkov-Olshanski shifted-Schur framework but does NOT require full O-O machinery.
---

# (M) Master Identity — PROVED — Day 109

## Statement

For all $k \geq 1$:
$$Q_k(-2, b, c) = Q_k(a, -1, c) = (-1)^k c(c-k)\prod_{j=1}^{k-1}(c-j)^2$$

where $Q_k(a, b, c)$ is Rick's h-template pipeline polynomial.

## Proof structure

Two lemmas:

**Lemma 1 (Rank-drop at $y_1 = 0$).** $(ds_j/V)|_{a=-2} = b^{\underline{j}}(c-1)^{\underline{j}}$ for all $j \geq 0$.

Structural reason:
1. At $y_1 = 0$, first row of $\det[(y_i)_{\downarrow \mu_l + 3-l}]$ vanishes if $\mu_3 > 0$.
2. In $\mathcal{S}_j$, the unique partition with $\ell(\mu) \leq 2$ is $\mu = (j, j, 0)$ with $\kappa = 1$.
   (Vertical 2-strips in 2 rows must add one cell each to rows 1 and 2.)
3. The residual 2×2 minor evaluates to $-(b+1)b^{\underline{j}}c(c-1)^{\underline{j}}(c-b-1)$.
4. $V|_{a=-2} = -(b+1)c(c-b-1)$ divides through cleanly.

**Lemma 2 (Chu-Vandermonde variant).**
$$\sum_j (-1)^{k-j}\binom{k}{j} u^{\overline{k-j}} v^{\underline{j}} = (-1)^k (u-v)^{\overline{k}}$$

Standard identity, via $v^{\underline{j}} = (-1)^j(-v)^{\overline{j}}$ + Chu-Vandermonde.

**Combining:** at $a=-2$, $H_c$ factorization + cancellation $(c-1-j)!(c-1)^{\underline{j}} = (c-1)!$ gives:
$$h_k(-2, b, c) = (c-1)!(b+2)_{c-1-k} \cdot (-1)^k(c-k+1)^{\overline{k}}.$$
Dividing by $(c-1-k)!(b+2)_{c-1-k}$ yields (M).

## Files

- `proofs/2026-08-18-day109-M-proved.md` — full proof.
- `beta-prime/code/2026-08-18-M-identity-verify-wide.{py,txt}` — k=1..9 both slices.
- `beta-prime/code/2026-08-18-k1-k2-by-hand.{py,txt}` — sympy trace k=1, 2.
- `beta-prime/code/2026-08-18-lemma1-verify.{py,txt}` — L1 for j=3..10.

## Downstream

- **Appendix F** = special case k = 2R. Now proved.
- **(★) uniform proof** reduces to (R) [recursion at Weyl walls] + (LC) [leading coef].
- **$a \leftrightarrow b$ duality** = shifted-Schur $y_i$-symmetry.

## Reference

- Okounkov-Olshanski, "Shifted Schur functions", arXiv:q-alg/9605042.
  Def 1.2 (shifted Schur as determinant ratio), used in identifying $M_\mu$
  as the numerator with $y = (a+2, b+1, c)$ the shifted variables.
  Full O-O machinery (coherence, characterization, branching) NOT needed
  in the end.

## Method — reusable pattern

The proof technique for (M) generalizes:
1. Identify a coordinate slice ($y_1 = 0$, or Weyl wall coincidence).
2. Rank drop: which partitions survive in the ensemble?
3. Explicit determinantal evaluation on the survivors.
4. Chu-Vandermonde / finite-difference collapse on the resulting alternating sum.

**Day 110 target:** apply this to (R) at Weyl coincidence walls $y_1 = y_2 = k$.
