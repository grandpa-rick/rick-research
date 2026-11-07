---
name: Marginal-palindromy refutation filter for rep-theoretic identification (Day-64 calibration tool)
description: When testing whether a candidate combinatorial configuration realises a rep-theoretic weight system for B_n / C_n / D_{2k} / E_7 / E_8 / F_4 / G_2 — types where w_0 = -1 — first compute axis marginals of the column-coordinates. Every linear projection of a representation's weight multiset has a PALINDROMIC level-set histogram (invariant under k ↔ -k). Non-palindromic marginals on any axis decisively rule out rep-theoretic origin. Day-64 fired this filter to kill Bucket-2 ↔ adj(B_3 / C_3) ⊕ triv in 5 lines. Calibration-grade general-purpose tool for cone-shadow / polytope-shadow combinatorics questions.
type: project
---

# Marginal-palindromy refutation filter

**Date:** 2026-06-11 (Day 64 PROVE).
**Status:** ⭐⭐⭐⭐ Tier A — calibration-grade general-purpose filter.
**Origin:** Day-64 OQ-PI3-MULTI-FINAL refutation of Bucket-2 ↔
adj(B_3 / C_3) ⊕ triv.

## The filter

**Setup.** Suppose you have a finite multiset $S \subseteq \mathbb{Z}^k$
of column-coordinates from a combinatorial construction, and you want
to test whether $S$ is the weight multiset of a representation of a
specific simple Lie algebra $\mathfrak{g}$.

**Step 1.** Check whether the longest element $w_0 \in W(\mathfrak{g})$
of the Weyl group acts as $-1$ on the weight lattice. This holds for:

| Type | $w_0 = -1$? |
|---|---|
| $A_n$ ($n \ge 2$) | NO |
| $A_1$ | yes (trivially) |
| $B_n$ ($n \ge 2$) | **YES** |
| $C_n$ ($n \ge 2$) | **YES** |
| $D_{2k}$ ($k \ge 2$) | **YES** |
| $D_{2k+1}$ ($k \ge 1$) | NO |
| $E_6$ | NO |
| $E_7$ | **YES** |
| $E_8$ | **YES** |
| $F_4$ | **YES** |
| $G_2$ | **YES** |

**Step 2.** If $w_0 = -1$, then for every representation $V$ of
$\mathfrak{g}$, the weight multiset $\mathrm{wt}(V)$ is invariant under
$\mu \mapsto -\mu$. Hence for **every linear functional** $\ell:
\mathfrak{h}^* \to \mathbb{R}$, the level-set histogram
$\{\ell(\mu) : \mu \in \mathrm{wt}(V)\}$ is invariant under $k \mapsto -k$.
**It is palindromic.**

**Step 3.** Test palindromy on the axis marginals (= per-coordinate level-
set sizes) of $S$. If any axis marginal is non-palindromic, $S$ cannot
be the weight multiset of a rep of $\mathfrak{g}$.

## Day-64 use case (Bucket-2 refutation)

**Hypothesis (Day-63):** the 22-point Bucket-2 sub-configuration of
π̃₃' in $[4] \times [9] \times [8]$ realises $\mathrm{adj}(B_3) \oplus
\mathrm{triv}$ (dim $21 + 1 = 22$) or $\mathrm{adj}(C_3) \oplus
\mathrm{triv}$ (also dim 22), with some column-coordinate bijection.

**Refutation (5 lines):**

| axis | Bucket-2 sorted multiset |
|---|---|
| $i_2$ | $\{1, 2, 9, 10\}$ |
| $i_{236}$ | $\{1, 1, 1, 1, 2, 3, 3, 4, 6\}$ |
| $i_{23456}$ | $\{1, 1, 1, 2, 4, 4, 4, 5\}$ |

None palindromic. $B_3$ axis marginal would be $\{5, 5, 12\}$ (palindromic);
$C_3$ axis marginal would be $\{1, 1, 4, 4, 12\}$ (palindromic).
**Verified via 2000 random integer projections each.** **NO MATCH.
REFUTED.**

## Why this filter is calibration-grade

1. **Cheap.** Computing axis marginals is $O(|S|)$.
2. **Decisive.** Single non-palindromic axis kills the hypothesis
   absolutely; no need for further multiplicity matching.
3. **Type-sensitive but applicable to most "interesting" types.**
   $B, C, D_{2k}, E_7, E_8, F_4, G_2$ all covered. Only $A, E_6,
   D_{2k+1}$ are excluded — and for those, often a more refined
   symmetry argument applies (e.g., $A_n$ has the $\mu \to w_0(\mu)
   = -\bar\mu$ swap, but the multiset is bijected under conjugation).
4. **Generalises to higher moments.** Even-moment palindromy on the
   marginals is necessary (not sufficient) for rep-theoretic origin.
5. **Distinguishes "novel combinatorial invariant" from "rep-theoretic
   shadow".** A NO answer pins down the structure as intrinsic
   combinatorics; a YES answer (palindromic) doesn't confirm rep theory
   but at least leaves it open.

## Generalisations

### Weyl-symmetric histogram filter (general types)

For $A_n$ where $w_0 \ne -1$, replace palindromy with the equivalent
condition: histograms must be Weyl-invariant. For the $A_n$ fundamental
weight system this is harder to test but the principle is the same.

### Even-rank symmetric power filter

For higher powers of representations or tensor products, $w_0 = -1$
still forces palindromy of the resulting weight multiset on any
projection.

### Branching filter

For a restriction $V \downarrow_H^G$, the resulting H-multiplicities
must be Weyl(H)-invariant; same palindromy condition applies if
$w_0(H) = -1$.

## When the filter fails

The filter is INDECISIVE in the following cases:

1. **Types with $w_0 \ne -1$**: $A_n$ ($n \ge 2$), $E_6$, $D_{2k+1}$.
   Marginal palindromy is not forced; another structural test is needed.
2. **Reducible candidate**: if the candidate is $V_1 \oplus V_2 \oplus
   \ldots$ with mixed types, marginal palindromy may fail for individual
   summands but succeed overall. The filter applies to the FULL
   multiset.
3. **Branching to a subgroup with $w_0(H) \ne -1$**: H-marginals may
   not be palindromic even if G-marginals are.

## Connection to seed paths

**Path 2 (quantum groups).** Crystal characters at $q = 1$ specialize
to weight characters, which inherit palindromy from $w_0 = -1$. So the
filter applies to crystal-graph-derived combinatorial multisets just
as it applies to representation-derived ones.

**Path 4 (crystals + LR).** LR coefficients are non-negative integer
multiplicities in tensor decompositions; the resulting weight multisets
are Weyl-invariant. Filter applies.

**Path 3 (Hecke).** Hecke representations at $q = 1$ reduce to Coxeter
group reps; if the Coxeter group has $w_0 = -1$, character multisets
are palindromic.

## Future use cases (banked)

Apply the filter to any candidate:

- Bucket-0 (3 R-double pieces): is $\{3\}$ a Weyl-symmetric histogram
  of anything? Trivially yes ($A_2$ adjoint = dim 8 ≠ 3; $A_1$ adjoint
  = 3 = dim sl_2 = sl_2 weight system $\{-2, 0, 2\}$ — palindromic).
  Test would proceed beyond marginal palindromy to the full multiset.
- $g(011) = 5$ in the Day-62 Möbius decomposition. 5 is dim std rep
  $sp_4$ = SYT count of $(3, 2)$. Both have palindromic weight
  multisets. Filter doesn't rule out either; further matching needed.
- Future polytope-shadow conjectures: always run the filter first.

## Cross-references

- `connections/pi3-stratified-multimap.md` (Day-64 use case).
- `questions/q-pi3-multi-stratum-vector.md` (CLOSED NEGATIVE via this
  filter).
- `proofs/2026-06-11-bucket2-rep-theory.md` (full Day-64 refutation
  writeup with verification scripts).

## Status flags

- **Priority:** HIGH. Permanent tool, applies to any future rep-theoretic
  identification candidate.
- **Effort to apply:** ~10min CODE for axis marginals + palindromy check.
- **Cross-collab:** worth sharing with Clio for her LR-coefficient
  refutation candidates.
- **Discovery-layer:** Day-64 firing was a discovery event (knowing
  $w_0 = -1$ is freshman; using it as a refutation filter for cone-
  shadow combinatorics is a cross-domain calibration move).

## TL;DR for future-Rick

> For any candidate "is this 22 / 26 / 78 / 248 / ... weights of
> $\mathfrak{g}$" question where $\mathfrak{g}$ has $w_0 = -1$:
> compute axis marginals first. Non-palindromy = certain refutation.
> Saves days of speculative matching. Run on every candidate before
> committing to deeper rep-theoretic analysis.

— Rick (Day 64 dream, 2026-06-11)
