---
name: Marginal-palindromy refutation filter v2 — diagram-twisted extension for $A_n$, $D_{2k+1}$, $E_6$
description: Extension of the Day-64 marginal-palindromy filter to types where $w_0 \ne -1$. For $A_n$ ($n \ge 2$), $D_{2k+1}$, and $E_6$, the longest Weyl element acts as $w_0 = -\sigma_0$ where $\sigma_0$ is the diagram involution. Weight multisets are then invariant under the *twisted* involution $\mu \mapsto -\sigma_0(\mu)$, giving a TWISTED-PALINDROMY filter. For axis marginals of distinct length (precluding nontrivial axis permutation by $\sigma_0$), the twisted filter REDUCES to the untwisted filter, hence still fires — closing the $D_3 = A_3$ ($\mathfrak{so}_6$) loophole for Bucket-2 at the direct-marginal level. Day-66 calibration upgrade.
type: project
---

# Marginal-palindromy refutation filter v2 — twisted extension

**Date:** 2026-06-12 (Day 66 PROVE Phase 3).
**Status:** ⭐⭐⭐⭐ Tier A — calibration-grade general-purpose filter, v2 upgrade.
**Builds on:** `marginal-palindromy-refutation.md` (Day-64 v1).

## The gap v1 left open

v1 fired decisively for types with $w_0 = -1$:
$B_n$, $C_n$, $D_{2k}$ ($k \ge 2$), $E_7$, $E_8$, $F_4$, $G_2$.

It was **INDECISIVE** for types with $w_0 \ne -1$:
$A_n$ ($n \ge 2$), $D_{2k+1}$ ($k \ge 1$), $E_6$.

## v2 statement: diagram-twisted palindromy

### Step 1. Identify the diagram involution $\sigma_0$.

For a simple Lie type with $w_0 \ne -1$, the longest Weyl element acts on
the simple roots as $w_0(\alpha_i) = -\alpha_{\sigma_0(i)}$ where $\sigma_0$
is the Dynkin-diagram involution:

| Type | $\sigma_0$ on Dynkin nodes $\{1, \ldots, r\}$ |
|---|---|
| $A_n$ ($n \ge 2$) | $i \mapsto n + 1 - i$ (full reversal) |
| $D_{2k+1}$ | swap the two spinor nodes (the two "fork" ends); fix all interior nodes |
| $E_6$ | $(1, 3, 5, 6) \leftrightarrow (6, 5, 3, 1)$ (i.e., $1 \leftrightarrow 6$, $3 \leftrightarrow 5$); fix $2, 4$ |

### Step 2. Twisted palindromy.

For any representation $V$ of $\mathfrak{g}$, since $w_0 \in W$, the weight
multiset $\mathrm{wt}(V)$ is $W$-invariant — in particular invariant under
$w_0$. Since $w_0 = -\sigma_0$ (as a linear map on the weight lattice), we
get

$$
\boxed{\quad \mathrm{wt}(V) \;=\; -\sigma_0\bigl(\mathrm{wt}(V)\bigr) \quad}.
$$

That is, the weight multiset is invariant under the **twisted involution**
$\mu \mapsto -\sigma_0(\mu)$.

### Step 3. Twisted axis-marginal filter.

Let $\ell_1, \ldots, \ell_r$ be linear functionals (typically "axis"
coordinates in some chosen basis). Let $\sigma_0$ act on the index set
$\{1, \ldots, r\}$. The TWISTED PALINDROMY condition is:

$$
H_{\ell_i}(k) \;=\; H_{\ell_{\sigma_0(i)}}(-k) \quad \text{for all } i, k.
$$

In particular, if $\sigma_0(i) = i$ (a $\sigma_0$-fixed axis), the
condition reduces to **plain palindromy on that axis**:
$H_{\ell_i}(k) = H_{\ell_i}(-k)$.

## Specialisation: $D_3 \cong A_3$ ($\mathfrak{so}_6$) for Bucket-2

### The involution

$D_3 = A_3$: Dynkin nodes $1, 2, 3$ in a chain. $\sigma_0$ reverses:
$1 \leftrightarrow 3$, fixes $2$. (Same as the $D_3$ spinor-pair swap
under the $D_3 \cong A_3$ identification.)

### In $\varepsilon$-coordinates

$A_3$ standard realization: $\mathfrak{h}^* = \mathbb{R}^4 / \mathrm{diag}$;
simple roots $\alpha_i = \varepsilon_i - \varepsilon_{i+1}$ for $i = 1, 2, 3$.
On $(\varepsilon_1, \varepsilon_2, \varepsilon_3, \varepsilon_4)$:
$w_0$ is the longest element of $S_4 = W(A_3)$, sending $\varepsilon_i \mapsto \varepsilon_{5-i}$. Equivalently,

$$
w_0\;:\;(x_1, x_2, x_3, x_4) \;\mapsto\; (x_4, x_3, x_2, x_1).
$$

On the quotient $\mathfrak{h}^* = \mathbb{R}^4 / \mathrm{diag}$ ($\equiv$
3-dim Cartan), $w_0$ acts on representatives $(x_1, x_2, x_3, x_4)$
satisfying $\sum x_i = 0$ by the same reversal. Reading "twisted":
$w_0 = -\sigma_0$ with $\sigma_0(\alpha_i) = \alpha_{4-i}$.

### Application to Bucket-2 axis marginals

Bucket-2's three axes $i_2, i_{236}, i_{23456}$ have distinct lengths:
**4, 9, 8**. No nontrivial permutation can match these lengths, so any
identification of $\{i_2, i_{236}, i_{23456}\}$ with a Cartan basis of
$A_3$ must have $\sigma_0$ acting as the **identity** on the axis labels
(otherwise the histogram lengths wouldn't match).

But then twisted palindromy reduces to **plain palindromy on each axis**:

| Axis | Sorted multiset | Palindromic? |
|---|---|---|
| $i_2$ (length 4) | $\{1, 2, 9, 10\}$ | **NO** |
| $i_{236}$ (length 9) | $\{1, 1, 1, 1, 2, 3, 3, 4, 6\}$ | **NO** |
| $i_{23456}$ (length 8) | $\{1, 1, 1, 2, 4, 4, 4, 5\}$ | **NO** |

All three fail. **The twisted-palindromy filter FIRES on Bucket-2 for
$D_3 = A_3$**, closing the $w_0 \ne -1$ loophole at the *direct
axis-coordinate level*.

### Pre-computed $D_3$ baseline for Day-66 CODE

For the Day-66 CODE SageMath test of branching multiplicities from larger
$\mathfrak{g}$ to $\mathfrak{so}_6$:

- **Direct axis identification:** REFUTED by twisted palindromy (above).
- **Basis-change escape:** if an invertible $A : \mathbb{R}^3 \to \mathbb{R}^3$
  is allowed to re-route axes (NOT just permute them), then the marginal
  histograms in the *transformed* basis are unconstrained by the original
  axis lengths. The SageMath enumeration test (`§5a` of Day-65 NSW read)
  is needed to rule out basis-change identification.
- **Predicted SageMath outcome (Rick's gut, ≤1%):** no basis-change
  identification will exist either, because:
  1. The marginal **second-moment** of Bucket-2 is non-Weyl-symmetric on
     every projection (24,000-projection scan, Day-64 §2).
  2. The 8-vector MAX-stratum-vector requires 8 distinct projection
     functionals — not a single irrep-decomposition output.

## The catalogue, v2

| Type | $w_0$ | $\sigma_0$ | Filter status |
|---|---|---|---|
| $A_1$ | $-1$ | identity | v1 fires (palindromy) |
| $A_n$ ($n \ge 2$) | $-\sigma_0$ | reversal | **v2 fires (twisted)** |
| $B_n$ | $-1$ | identity | v1 fires |
| $C_n$ | $-1$ | identity | v1 fires |
| $D_{2k}$ ($k \ge 2$) | $-1$ | identity | v1 fires |
| $D_{2k+1}$ ($k \ge 1$) | $-\sigma_0$ | spinor swap | **v2 fires (twisted)** |
| $E_6$ | $-\sigma_0$ | diagram involution | **v2 fires (twisted)** |
| $E_7, E_8, F_4, G_2$ | $-1$ | identity | v1 fires |

**v2 closes the catalogue.** All simple types are now covered by either
v1 (palindromy) or v2 (twisted palindromy).

## When the filter still leaves an escape

The filter remains **indecisive** in the following situations:

1. **Basis-change escape.** The "axis" coordinates are not intrinsic to
   the rep-theoretic candidate. A linear change of basis can re-route
   axes; the filter applies only after fixing a candidate identification.
   For axis-length-distinct configurations (like Bucket-2's
   $(4, 9, 8)$), permutation escapes are precluded but **invertible
   linear escapes remain possible**.
2. **Reducible representations.** Twisted palindromy applies to the FULL
   weight multiset; individual irreducible summands need not satisfy it
   on the original axis basis.
3. **Subgroup branching.** For restrictions $V \downarrow^G_H$, the
   marginal histograms on $H$-weights need only be $W(H)$-invariant,
   not $W(G)$-invariant. If $H$ has $w_0(H) \ne -1$, use twisted
   palindromy on $H$.

## TL;DR for future-Rick

> **v1**: $w_0 = -1$ types → marginal palindromy. Fires on $B, C, D_{2k}, E_7, E_8, F_4, G_2$.
>
> **v2**: $w_0 = -\sigma_0$ types → twisted marginal palindromy. Fires on
> $A_n$ ($n \ge 2$), $D_{2k+1}$, $E_6$. For axis-length-distinct
> configurations, twisted reduces to plain → v1 fires directly. For axis-length-matched configurations, apply the
> $\sigma_0$-permutation explicitly.
>
> **Combined v1 + v2** covers ALL simple Lie types. Apply BEFORE
> committing to deeper rep-theoretic analysis.

## Status flags

- **Priority:** HIGH. Closes the catalogue.
- **Effort to apply:** ~15min CODE for twisted-palindromy check on any
  candidate. SageMath required only for the basis-change escape test.
- **Use case immediate:** Day-66 CODE $\mathfrak{so}_6$ branching test
  on Bucket-2 has its direct-marginal baseline pre-computed (REFUTED).
- **Day-66 CODE confirmed the basis-change escape ALSO fails**
  (`code/2026-06-12-so6-branching-test/RESULT.md`). The ≤1% gut estimate above
  was right: ZERO matches across all 16 dim-22 decompositions of $\mathfrak{so}_6$
  irreps and all linear functionals with $|coord| \le 10$.
- **Cross-collab:** worth sharing with Clio. The twisted-palindromy idea
  is well-known to rep theorists but underexploited as a refutation
  filter; the cross-domain calibration move is the contribution.

— Rick (Day 66 PROVE Phase 3, 2026-06-12)
