---
title: "OQ-IQUANTUM-RSK-LIFT — natural first technical move"
author: Rick
date: 2026-06-12
status: SCOPING. One sentence: define the iquantum JM elements via the affine ι-Hecke polynomial part.
---

# The first move (in one sentence)

**Identify the polynomial part $\mathbb{C}[y_1, \ldots, y_n]$ of the
degenerate affine ι-Hecke algebra of Bao–Wang as the "iquantum
Jucys–Murphy" commuting subalgebra, and compute its joint spectrum on
$V^\iota(\nu) \otimes V(1)^{\otimes N}$ at small $n$ to verify that
joint eigenvalues are indexed by oscillating tableaux.**

# Why this move

Stern's whole spectral mechanism rests on **one fact**: the degenerate
AHA $H_n$ has a polynomial subalgebra $\mathbb{C}[x_1, \ldots, x_n]$
whose generators commute, whose joint eigenbasis on $V^{\otimes n}$ is
the GZ basis labelled by standard tableaux, and which act on the symmetric
group by the JM elements. **Everything else in his paper is unpacking
that spectral statement combinatorially.**

The type-AII analog therefore reduces to identifying the right
**commuting polynomial subalgebra** in the right **affine Hecke
analogue**. The candidates:

| Candidate algebra | Centralizer of | "JM-like" subalgebra |
|---|---|---|
| Degenerate AHA $H_n^{\mathrm{deg}}$ (Drinfeld) | $U(\mathfrak{gl}_n)$ on $V^{\otimes n}$ | $\mathbb{C}[x_1, \ldots, x_n]$ |
| Brauer algebra $\mathrm{Br}_N(-2n)$ | $\mathfrak{sp}_{2n}$ on $V(1)^{\otimes N}$ | Nazarov–Leduc–Ram |
| Affine Wenzl / Nazarov–Brauer | $\mathfrak{sp}$ central extension | Nazarov |
| **Affine ι-Hecke** (Bao–Wang) | **$U^\iota(\mathfrak{sp}_{2n})$ on $V(1)^{\otimes N}$** | **YES — type-B Murphy polynomial part** |
| Degenerate affine ι-Hecke | $U^\iota$ classical limit | THE TARGET |

The third row (Brauer / Nazarov) corresponds to $U_q(\mathfrak{sp})$, not
$U^\iota$. Wrong centralizer. The right object is in the fourth row.

# What I actually need to verify

## Step 1 (sanity, 1 day).

Look up: does **Bao–Wang [arXiv:1610.09271]** or its sequels
([arXiv:1603.01524], [arXiv:1907.13362]) give an explicit polynomial
commuting subalgebra in their affine ι-Hecke? Spelled-out generators?
The Murphy elements in the type-B Hecke algebra
$H(W(B_N), q^{1/2}, Q^{1/2})$ are well-known (Dipper–James–Murphy);
their lift to affine ι-Hecke should be in Bao–Wang.

If yes: write them down explicitly. Call them $y_1, \ldots, y_N$. They
satisfy:
- $[y_i, y_j] = 0$ (commutativity, the load-bearing structural fact),
- $y_i$ is a polynomial in the generators of the affine ι-Hecke,
- Under Schur–Weyl, $y_i$ acts on $V^\iota \otimes V^{\otimes N}$ as a
  diagonalisable operator with rational spectrum.

If no (Bao–Wang doesn't write them down): the Murphy elements of $H(B_N)$
extend to affine ι-Hecke automatically via Drinfeld's argument
(the affine version is a semidirect product
$H(W) \ltimes \text{polynomial}$ on the abstract level — the same
construction works mutatis mutandis for any quasi-affine extension of
finite Hecke).

## Step 2 (computation, 2-3 days).

Take **$n = 1$, $N = 2$**: $V^\iota(\nu) = V^\iota(0) \cong \mathbb{C}$
(trivial), $V(1)$ = 2-dim vector rep of $U_q(\mathfrak{sp}_2) \cong U_q(\mathfrak{sl}_2)$.

$V^\iota(0) \otimes V(1) \otimes V(1)$ decomposes (Watanabe's
RSK$^{A\mathrm{II}}$ at $\nu = \emptyset$, $N = 2$) into
$\bigoplus_{\xi} V^\iota(\xi) \otimes \mathrm{OT}_{1,2}(\emptyset, \xi)$
which at $n=1$ is just two pieces.

Verify: the "iquantum JM" $y_1, y_2$ (after restriction to this 4-dim
space) has joint eigenbasis indexed by the two OT walks
$\emptyset \to (1) \to \emptyset$ and $\emptyset \to (1) \to (2)$.

## Step 3 (next case, 3-4 days).

$n = 2$, $N = 2$. $V^\iota(0) = \mathbb{C}$, but $V^\iota(1)$ is now
4-dim (analog of vector rep of $\mathfrak{sp}_4$). Take $V^\iota(0) \otimes V(1)^{\otimes 2}$ — should decompose into $V^\iota(0)
\otimes \mathbb{Q}(q)\mathrm{OT}_{2,2}(\emptyset, \emptyset) \oplus
V^\iota(\square) \otimes \mathrm{OT}_{2,2}(\emptyset, \square) \oplus
V^\iota(\square\square) \otimes \mathrm{OT}_{2,2}(\emptyset, \square\square)
\oplus V^\iota({\stackrel{\square}{\square}}) \otimes \mathrm{OT}_{2,2}(\emptyset, {\stackrel{\square}{\square}})$
(with appropriate multiplicities — OT walks of length 2).

Verify the JM eigenvalues label these multiplicity spaces.

## Step 4 (sanity at the q→∞ limit, 1 day).

The eigenvalues should reduce to integer "GZ-like" coordinates labelling
each OT step. Confirm they recover the King-tableau combinatorics at the
classical limit.

## Step 5 (general statement, 1 week).

If Step 1–4 work: state and prove

**Theorem (target).** *The joint eigenbasis of the commuting family
$\{y_1, \ldots, y_N\}$ on $V^\iota(\nu) \otimes V(1)^{\otimes N}$ is
canonically indexed by $\bigsqcup_\xi \mathrm{OT}_{n,N}(\nu, \xi)$, with
the joint eigenvalue determined by the OT walk.*

This is the spectral version of (SYN).

# Sanity check: does Stern's argument adapt?

Stern §4 uses two ingredients:
1. The polynomial part of $H_n$ acts as commuting external translations.
2. JdT slides = switching operators = Hecke-algebra commutation relations
   acting on the regular representation.

For (1) in the AII setting: same construction with affine ι-Hecke
polynomial part. **Should work**.

For (2): we need the AII analog of switching to correspond to **boundary
switching** — i.e., the K-matrix appears in addition to the R-matrix.
**Concern**: Watanabe's row-insertion of type AII goes via the
intermediate $P$-tableau algorithm; the switching content is hidden.
This is the **technical sticking point** of the synthesis.

Most likely workaround: realise the K-matrix action as a "boundary
switching operator" and decompose Watanabe's $P$ algorithm into a
sequence of R-switches + one K-switch per row. **This is the hardest
step.**

# Bottom-line risk assessment

| Step | Risk | Failure mode |
|---|---|---|
| (B1) algebra exists | low | Bao–Wang already does it. |
| (B2) JM family | low | Murphy of type B is well-studied. |
| (B3) OT eigenbasis | medium | Need explicit branching computation; possibly hard at $n \ge 3$. |
| (B4) embedding into bigger group | medium | Type-AII has hyperoctahedral combinatorics, more degrees of freedom than $S_n$. |
| Step 2 (Stern's switching) | high | K-matrix decomposition of Watanabe's $P$ is the technical heart. |

If the K-matrix-as-boundary-switching analysis works, the synthesis is
~3 weeks of focused work. If it doesn't, the synthesis becomes a
multi-month project requiring fresh combinatorial input.

# Immediate next action (if I were to start)

1. Email Watanabe-san to ask: does he see the OT walks as eigenvalues
   of a commuting family? If yes, he might already know the answer to
   (B3) without writing it down.
2. Read Bao–Wang's affine ι-Hecke paper carefully for the explicit
   commuting subalgebra (1 day).
3. Code up Step 2 ($n=1$, $N=2$) by hand. Confirm the spectral picture.

— Rick, Day 67 CODE scoping, 2026-06-12
