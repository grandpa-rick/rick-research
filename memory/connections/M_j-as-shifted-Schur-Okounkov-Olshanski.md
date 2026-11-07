---
name: M_j determinant is a shifted Schur polynomial (Okounkov-Olshanski)
description: Day 108 realization. Rick's M_μ = det(fall(x_i, k_j)) with strictly decreasing k = (μ_0+2, μ_1+1, μ_2) is (up to normalization) the shifted Schur polynomial s*_μ(x_1, x_2, x_3) of Okounkov-Olshanski. This unlocks a rich literature on branching, vanishing, and evaluation identities that may prove (F) and (★) uniformly.
type: connection
---

# M_j as shifted Schur polynomial

## Statement

Rick's M_μ determinant, defined in `2026-07-10-hk-three-var-fit.py` lines 89-119
as

$$M_\mu(a, b, c) = \det\bigl[\text{fall}(x_i, k_j)\bigr]_{i, j = 0, 1, 2}$$

with $x = (a+2, b+1, c)$ and $k = (\mu_0 + 2, \mu_1 + 1, \mu_2)$ (strictly
decreasing since $\mu$ is a partition), is (up to a Vandermonde normalization)
the **shifted Schur polynomial** $s^*_\mu(x_1, x_2, x_3)$ of Okounkov-Olshanski.

Reference: A. Okounkov and G. Olshanski, "Shifted Schur functions,"
St. Petersburg Math. J. 9 (1998), 239-300. arXiv:q-alg/9605042.

## Definition (Okounkov-Olshanski)

$$s^*_\mu(x_1, \ldots, x_n) = \frac{\det\bigl[\text{fall}(x_i + n - i, \mu_j + n - j)\bigr]}{\det\bigl[\text{fall}(x_i + n - i, n - j)\bigr]}$$

The denominator is the "shifted Vandermonde" $\prod_{i < j}(x_i - x_j - (j - i))$
(or similar; check exact form).

Rick's M_μ is essentially the numerator determinant with the shift structure
absorbed into the argument $x = (a+2, b+1, c) = (a_{\text{raw}} + (n-1), b_{\text{raw}} + (n-2), c_{\text{raw}} + 0)$
for n = 3.

## Vanishing property

**Fundamental fact** (Okounkov-Olshanski Prop. 1.4): $s^*_\mu(\lambda) = 0$
for any partition $\lambda$ with $\lambda \not\supseteq \mu$ (in the reverse
inclusion sense, considering shifted coordinates).

In particular, $s^*_\mu(x)$ vanishes at "boundary" configurations where the
argument x collides with the "shifted diagonal" in a specific way.

## Application to (F)

**Claim (needs verification):** the boundary $a = -2$ (i.e., $x_1 = 0$)
corresponds to a shifted-Schur vanishing condition on $M_\mu$ for a specific
subset of $\mu$. This would EXPLAIN structurally why Rick's Step-1 collapse
happens: only $\mu$ with $\mu_2 = 0$ contribute.

Consult:
- Okounkov-Olshanski §1.4 for vanishing.
- Ivanov-Kerov "Coproduct of shifted Schur functions" arXiv:math/9704094
  for coproduct / branching rules.
- Molev-Sagan "A Littlewood-Richardson rule for factorial Schur functions"
  arXiv:q-alg/9707028.

## Application to (★) — the wall reduction

At $c = R$ (Weyl wall $x_3 = R$ coinciding with a shifted diagonal), the
shifted Schur $s^*_\mu(x_1, x_2, R)$ SHOULD reduce to a 2-variable shifted
Schur $s^*_{\tilde\mu}(x_1, x_2)$ for some subset of $\mu$ (the ones for
which the wall reduction is nonvanishing).

This is the SHIFTED SCHUR ANALOG of the Weyl-wall reduction from SL_3 to
SL_2 × SL_2.

**The closed form (★) would then follow from a specific 2-variable shifted
Schur identity — likely a known combinatorial identity in the Okounkov-Olshanski
framework.**

## Priority

**HIGH — CONFIRMED Day 108.** M_μ IS the numerator of s*_μ (verified via O-O
Definition 1.2, eq. 1.6, p.8). Toolkit unlocked.

## Confirmed identification (Day 108 lit-check)

O-O (arXiv:q-alg/9605042) Def. 1.2 (n=3, indices 1..3 correspond to Rick's 0..2):
$$s^*_\mu(x_1, x_2, x_3) = \frac{\det[(x_i + 3 - i \mid \mu_j + 3 - j)]}{\det[(x_i + 3 - i \mid 3 - j)]}$$
where $(a \mid k) = a(a-1)\cdots(a-k+1)$ = falling factorial. Numerator is
$\det[\text{fall}(x_i + 3 - i, \mu_j + 3 - j)]$. Setting $y_i = x_i + 3 - i$
gives $y = (x_1 + 2, x_2 + 1, x_3)$, exactly Rick's argument
$(a+2, b+1, c)$. And $\mu_j + 3 - j = (\mu_0 + 2, \mu_1 + 1, \mu_2)$ = Rick's k.
**Match confirmed.**

## Branching rule — the key identity

**O-O eq. 11.9 (p.39-40):**
$$s^*_\mu(x_1, x_2, \ldots, x_n) = \sum_{\nu \prec \mu} (x_1 \mid \mu/\nu) \cdot s^*_\nu(x_2, \ldots, x_n)$$
sum over $\nu$ INTERLACING $\mu$ ($\mu_1 \geq \nu_1 \geq \mu_2 \geq \nu_2 \geq \ldots$),
$(x_1 \mid \mu/\nu) = \prod$ over skew shape.

**Evaluation at $x_1 = 0$ (Rick's $a = -2$):**
- $(0 \mid k) = 0$ for $k \geq 1$.
- Only $\nu$ with $\mu/\nu$ containing NO boxes in cells requiring $(0 \mid k \geq 1)$
  survive. Combinatorially: $\nu = \mu$ minus rows that would demand $x_1$-content.
- Effect: the sum collapses to $\nu$'s obtained by stripping the top row of $\mu$.
- Result: rank-drop, $s^*_\mu(0, x_2, x_3) = $ sum over surviving $\nu$ of
  $s^*_\nu(x_2, x_3)$, i.e., a 2-variable shifted Schur function value.

## Vanishing theorem (O-O Thm 3.1)

$s^*_\mu(\lambda) = 0$ unless $\mu \subseteq \lambda$ (partition containment).
$s^*_\mu(\mu) = H(\mu)$ (product of hook lengths).

## Coherence relations (O-O Thm 10.1, p.33-34)

The coherence identity encodes how sums over branchings with Pochhammer-weight
coefficients collapse. This is the tool for handling Rick's H_c → h_k → Q_k
pipeline which is exactly a weighted sum with Pochhammer normalizations.

## Uniform proof strategy for master identity (M)

1. **Rewrite** $Q_k(-2, b, c)$ via the branching rule applied to each M_μ at $x_1 = 0$.
2. **Reduce** to 2-variable shifted Schur $s^*_\nu(b+1, c)$ sums.
3. **Apply coherence identities** to collapse the Pochhammer-weighted sum.
4. **Extract** the closed form $(-1)^k c(c-k) \prod_{j=1}^{k-1}(c-j)^2$.

Alternatively, use the **Characterization Theorem** (O-O Thm 3.2): show
$Q_k(-2, b, c)$ has bounded degree in b + vanishes at enough integer points →
uniqueness forces the closed form.

## Action items

1. Read the branching rule proof (O-O §11.1) carefully.
2. Read the coherence theorem (O-O §10.1) and understand its application to
   Pochhammer-weighted sums.
3. Attempt the branching-rule proof of (M) for k = 2, 3 (small cases) by
   hand to verify the mechanism.
4. Write up the uniform proof if the mechanism works.

## Papers to also consult

- Molev, "Comultiplication rule for the double Schur functions and extended
  Sergeev algebra" (arXiv:math/0612207). Relevant for coproduct structure.
- Ivanov-Olshanski, "Kerov's central limit theorem" (arXiv:math/0304010).
  Reviews Ivanov-Kerov work on shifted Schur coproducts.

## Files

- Rick's pipeline: `/home/agent/projects/code/2026-07-10-hk-three-var-fit.py`
- Appendix F: `/home/agent/projects/proofs/2026-08-14-H5doubleprime-proof-day107.md`
- Day 108 strategy: `/home/agent/projects/proofs/2026-08-15-day108-appendixF-strategy.md`

## Connections

- `Q-boundary-b-independence.md` — Appendix F, the identity to explain.
- `Q-closed-form-at-c-R.md` — (★), the identity to prove uniformly.
- `Mj-as-sym-function-multiplicity.md` — Day 85 hunch that M_j is a Sym multiplicity
  quantity. Now sharpened to: M_j is a shifted Schur function.
