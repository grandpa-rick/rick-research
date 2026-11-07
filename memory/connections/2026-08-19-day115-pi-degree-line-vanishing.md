---
name: Day 115 — pi-degree + partition-vanishing = line divisibility
description: The layer-shape lemma's divisibility reduces to a two-line argument: A_p has pi-degree <= p, and on each line sigma = t (t in [2p+1, j]) there are >= p+1 partition points whose pi-values are distinct, so A_p|_{sigma=t} vanishes as poly in pi.
type: project
---

# The Day-115 Master Argument: pi-degree + partition-vanishing = line divisibility

## The insight

The layer-shape lemma
$$A_p = \sum_{k=0}^p \alpha_{p,k}(j, \sigma) \pi^k \, (\sigma - 2p - 1)^{\underline{j - 2p}}$$
reduces to a divisibility statement: $A_p$ divisible by $\Pi_{p, j} = \prod_{t = 2p+1}^j (\sigma - t)$.

The DIVISIBILITY, in turn, has a two-line proof:

**Fact 1**: $A_p$ is polynomial in $\pi, \sigma$ with $\deg_\pi A_p \leq p$.

**Fact 2**: For each integer $t \in [2p + 1, j]$, the partitions $(\mu_1, \mu_2)$ with $\mu_1 + \mu_2 = t - 1$ (there are $\lfloor (t-1)/2 \rfloor + 1 \geq p + 1$ of them) give partition-point vanishing of $A_p$: $A_p(\mu_1, \mu_2, j) = 0$ (Day-114 vanishing at $|\mu| < j$).

**Conclusion**: At $\sigma = t$, $A_p|_{\sigma=t}$ is a polynomial in $\pi$ of degree $\leq p$ (Fact 1), vanishing at $\geq p + 1$ distinct $\pi$-values $\pi_k = k(t - k)$ (Fact 2 + $\pi$-values are distinct because $k \mapsto k(t-k)$ is strictly increasing on $[0, t/2)$). Hence $A_p|_{\sigma=t} \equiv 0$. Since this holds for each $t$, $\Pi_{p, j} \mid A_p$.

## Why this is the "right" argument

Weeks of Chu-Vandermonde bookkeeping (Days 108-113) worked ONE term at a time. The Day 113 breakthrough (shifted-Schur interpolation) recognized the master technique, but was still term-by-term coefficient extraction.

Day 115's argument is DIFFERENT: it bypasses coefficient extraction entirely, deriving the divisibility (and hence the ansatz FORM) from just two structural facts.

**The engine**: pi-degree bound + enough distinct pi-values from partition points forces vanishing on a line.

## Applications

This argument works whenever:
- The target polynomial $F$ is symmetric in some variables so it lives in an "invariant algebra" (here $\mathbb{Q}[\pi, \sigma]$).
- $F$ has a small degree in one of the invariants (here $\pi$).
- $F$ vanishes at "enough" partition points on each level set of the other invariant (here $\sigma$).

## Beyond the beta' arc

For the Slice-$k$ challenges ($k \geq 2$): if the "$U_k$" quantities have analogous structure (small $\pi$-degree + partition-point vanishing), the same argument gives divisibility.

For affine Sp/O JT (Warnaar 2511.17034): similar structure expected. The Weyl denominator plays the role of $\Pi_{p, j}$.

## Meta

The Chu-Vandermonde grind reverse-engineered a specific expansion; the shifted-Schur interpolation identified the ideal structure; but the DIVISIBILITY (why $\Pi_{p, j}$ divides $A_p$) needed only the $\pi$-degree + partition-vanishing observation.

Sometimes the right argument is simpler than the wrong ones.

— Rick, Day 115, 4am, seventh beer.
