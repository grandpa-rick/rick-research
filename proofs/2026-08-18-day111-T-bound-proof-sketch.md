---
title: Day 111 — Proof sketch of (T) via top-degree annihilation
status: SKETCH — needs a technical lemma about degree of ds_j/V coefficients in j
---

# (T) Total-degree bound — proof sketch

## Statement

**Theorem (T).** For every $R \geq 1$, $Q_{2R}(a, b, c) \in \mathbb{Q}[a, b, c]$ has
total $(a, b)$-degree $\leq 2R$.

## Setup

Recall $H_c(a, b, j) = (a+3)_{c-1-j}(b+2)_{c-1-j} \cdot (ds_j/V)(a, b, c)$, and
$h_{2R}(a, b, c) = \sum_{j=0}^{2R}(-1)^{2R-j}\binom{2R}{j} H_c(a, b, j)$.
Finally $Q_{2R}(a, b, c) = h_{2R}(a, b, c) / [(a+3)_{c-1-2R}(b+2)_{c-1-2R}]$.

For $j \in \{0, 1, \ldots, 2R\}$, $H_c(a, b, j)$ is a polynomial in $(a, b)$ of
total degree exactly $2(c-1-j) + 2j = 2(c-1) = 2c - 2$ (the Pochhammer prefactor
contributes $2(c-1-j)$ and $ds_j/V = \sum_\mu \kappa_\mu s^*_\mu$ contributes at
most $|\mu| = 2j$, achieved by $\mu = (j, j, 0)$).

Since the denominator $(a+3)_{c-1-2R}(b+2)_{c-1-2R}$ has $(a, b)$-degree
$2(c-1-2R)$, showing $Q_{2R}$ has total $(a, b)$-degree $\leq 2R$ amounts to
showing $h_{2R}$ has total $(a, b)$-degree $\leq 2(c-1-2R) + 2R = 2c-2-2R$.

Equivalently: **the top $2R$ layers of $h_{2R}$ in $(a, b)$-degree vanish** —
i.e., the layer at $(a, b)$-degree $2c-2-d$ vanishes for $d = 0, 1, \ldots, 2R-1$.

## Key annihilation principle

**Lemma A** (finite-difference annihilation). For a polynomial $P(j) \in \mathbb{Q}[j]$
with $\deg P < N$:
$$\sum_{j=0}^N (-1)^{N-j}\binom{N}{j} P(j) = \Delta^N P(0) = 0.$$

## Structural claim

**Claim (⋆).** For each $d \in \{0, 1, \ldots, 2R-1\}$, the coefficient of the
$(a, b)$-layer at total degree $2c-2-d$ in $H_c(a, b, j)$, viewed as a monomial
in $\mathbb{Q}[c][a, b]$ times a scalar in $\mathbb{Q}[j][c]$, is polynomial in
$j$ of degree $< 2R$ (in fact, degree $\leq d$).

Combined with Lemma A applied with $N = 2R$: the $d$-th layer of $h_{2R}$ vanishes
for $d < 2R$, so $h_{2R}$ has $(a, b)$-degree $\leq 2c-2-2R$, hence $Q_{2R}$ has
$(a, b)$-degree $\leq 2R$.

## Proof of Claim (⋆)

Write $H_c(a, b, j) = P_j(a) \cdot Q_j(b) \cdot S_j(a, b, c)$ where
$P_j(a) := (a+3)_{c-1-j}$, $Q_j(b) := (b+2)_{c-1-j}$, and $S_j := (ds_j/V)$.

**Step 1: expand Pochhammer.** $P_j(a) = \sum_{i \geq 0} p_i^{(j)}(c) \cdot a^{c-1-j-i}$
where the coefficient of the $i$-th layer down from top is
$p_i^{(j)}(c) = [\text{elementary symmetric of shifts in } \{3, 4, \ldots, c-1-j+2\}]$.

Explicitly, if we let $e_i(z_1, \ldots, z_m) $ be the elementary symmetric polynomial,
then $p_i^{(j)}(c) = e_i(3, 4, \ldots, c-1-j+2)$. This is a polynomial in $j$ (with
$c$ fixed) of degree $i$: the leading term in $j$ comes from taking large factors
$c-1-j+2$, and $\binom{c-1-j}{i}$ analysis gives a degree-$i$ polynomial in $j$.

Similarly $Q_j(b) = \sum_{i' \geq 0} q_{i'}^{(j)}(c) \cdot b^{c-1-j-i'}$ with
$q_{i'}^{(j)}(c)$ polynomial in $j$ of degree $i'$.

**Step 2: expand $S_j$.** $S_j = \sum_\mu \kappa_\mu s^*_\mu(y_1, y_2, y_3) = \sum_\mu \kappa_\mu s^*_\mu(a+2, b+1, c)$.
Since $s^*_\mu$ has total degree $|\mu| = 2j$, and each surviving $\mu \in \mathcal{S}_j$
gives an $(a, b)$-polynomial with $(a, b)$-degree $\leq 2j - \mu_3 \leq 2j$
(equality when $\mu_3 = 0$), the layer at $(a, b)$-total-degree $2j - r$ in $S_j$
is a polynomial in $(a, b, c)$ whose coefficients (as functions of $j$) come from
enumerating $\mathcal{S}_j$-partitions with $\mu_3 = r$.

**Sub-claim (⋆⋆):** the layer at $(a, b)$-degree $2j - r$ in $S_j$ has coefficients
that are polynomial in $j$ of degree $\leq r$ (for each fixed $r$).

*This is the technical heart.* The number of $\mu \in \mathcal{S}_j$ with $\mu_3 = r$
is O(1) as $j \to \infty$ (they are parameterized by $(\mu_1 - \mu_2)$ with
$\mu_1 + \mu_2 = 2j - r$, so $\mu_2$ ranges over $\lceil (2j-r)/2 \rceil, \ldots, ?$).
Their contributions $\kappa_\mu \cdot s^*_\mu$ evaluate to polynomials in $(b, c)$ and
$(a, c)$ whose top-$(a,b)$-degree parts are polynomial in $j$ of degree $\leq r$
(specifically the top-$(a, b)$-part of $s^*_\mu(y_1, y_2, y_3)$ at $\mu = (\mu_1, \mu_2, r)$
is $y_1^{\mu_1 - 2} y_2^{\mu_2 - 1} y_3^r + \ldots$, but wait, that's not right in
$(a, b)$-degree because $y_1 = a+2, y_2 = b+1$ contribute $\deg_a(y_1^{\mu_1-2}) = \mu_1 - 2$
and $\deg_b(y_2^{\mu_2-1}) = \mu_2 - 1$, giving total $(a, b)$-degree $\mu_1 + \mu_2 - 3 = 2j-r-3$).

Hmm — sub-claim needs a careful re-check.

**Step 3: convolution.** The layer at $(a, b)$-degree $2c-2-d$ in $H_c(a, b, j)$
comes from convolutions $(i, i', r)$ with
$$(c-1-j-i) + (c-1-j-i') + (2j - r) = 2c-2-d \implies i + i' + r = d.$$

By Steps 1 & 2 (and Sub-claim (⋆⋆)), the coefficient at this layer is a sum over
$(i, i', r)$ with $i + i' + r = d$, of products of polynomials in $j$ of degrees
$i$, $i'$, and $\leq r$. So the total degree in $j$ is $\leq i + i' + r = d$.

Since $d < 2R$, Lemma A applies with $N = 2R$: the sum
$\sum_j (-1)^{2R-j}\binom{2R}{j} [\text{this coefficient}]$ vanishes. $\square$

## Status

- **Lemma A**: standard.
- **Steps 1, 3**: elementary (Pochhammer expansion and convolution counting).
- **Sub-claim (⋆⋆)**: needs verification. Rick's calibrated recipe would delegate
  this to a compute agent, verifying for small $r$ that the top-$(a, b)$-part of
  the $r$-th sub-family of $s^*_\mu$ in $S_j$ has $j$-polynomial degree $\leq r$.

## Empirical evidence

Day 111 agent (a5ec7e85eae64f7f7) confirmed:
- $(a, b)$-degree of $Q_{2R}$ is exactly $2R$ for $R = 2, 3, 4, 5$.
- The interpolation ansatz $Q_{2R} = \sum_k \tilde P_R^{(k)}(c)(a+2)^{\underline k}(b+1)^{\underline k}$
  is an identity for $R = 2, 3$.
- Top form of $H_c(a, b, j)$ is $1 \cdot a^{c-1} b^{c-1}$, $j$-independent, matching
  the $d = 0$ case of Sub-claim (⋆⋆).

## Next steps

1. Verify Sub-claim (⋆⋆) computationally for $r = 0, 1, 2, 3, 4$ at multiple $j$
   values. Fit $j$-degree of the top-$(a, b)$-part of each $\mu_3 = r$ sub-family.
2. If verified: state Sub-claim (⋆⋆) as a lemma and prove it structurally via
   the shifted-Schur specialization $s^*_\mu(a+2, b+1, c) = $ polynomial with
   controlled $j$-dependence in leading $(a, b)$-coefficients.
3. Combined with Slice-$k$ lemmas $(U_k)$ for $k \leq R$, this closes uniform (R)
   and hence $(\star)$.
