# Bucket-2 22-point configuration is NOT rep-theoretic

**Date:** 2026-06-11 (Day 64 PROVE, Q-SPHERE T+3d)
**Status:** **Refutation** — the Day-63 rep-theoretic hypothesis fails decisively. The 22-point Bucket-2 configuration in $[4] \times [9] \times [8]$ admits NO bijection to $\mathrm{adj}(B_3) \oplus \mathrm{triv}$ or $\mathrm{adj}(C_3) \oplus \mathrm{triv}$ that respects the column-index axis structure.

## TL;DR

1. The 22 Bucket-2 triples have explicit marginals
   $$
   |M_2\text{-cols}| = 4,\quad |M_{236}\text{-cols}| = 9,\quad |M_{23456}\text{-cols}| = 8.
   $$
   Per-index counts (number of pieces at each column value), as sorted multisets:
   - $i_2$: $\{1, 2, 9, 10\}$
   - $i_{236}$: $\{1, 1, 1, 1, 2, 3, 3, 4, 6\}$
   - $i_{23456}$: $\{1, 1, 1, 2, 4, 4, 4, 5\}$
2. Every $B_3$ or $C_3$ adj $\oplus$ triv weight system gives a **palindromic** axis-marginal (level-set sizes invariant under $k \leftrightarrow -k$), because $-1 \in W(B_3) = W(C_3)$.
   - $B_3$ axis marginal: $\{5, 5, 12\}$ (sorted: $\{5, 5, 12\}$)
   - $C_3$ axis marginal: $\{1, 1, 4, 4, 12\}$
3. Our marginals are **non-palindromic** on every axis. Therefore no axis-coordinate-respecting bijection exists. **Refutation.**
4. Weyl-orbit *labelling* (12+6+3+1) is also refuted: no single- or pairwise-projection of the data produces a $\geq 6$-sized natural class.
5. Quick scan of non-Lie alternatives (3D polytope vertex counts, $p(8) = 22$ partition statistics) finds **no clean match either**.

This **resolves Day-63 Gap B in the negative**: the 22-point Bucket-2 configuration is intrinsic combinatorics from the BDI/AII coordinate substitution structure, not rep theory. **OQ-PI3-MULTI-FINAL** refines accordingly: the MAX-stratum-vector is a novel combinatorial invariant of $\tilde\pi_3'$, with origin in the 26-piece minimal cover, not in a Lie algebra.

## 1. The 22 explicit triples

For each of the 22 Bucket-2 pieces in the Day-58 minimal cover, the column (= 7-vector of coefficients $(M_1, M_2, B_1, T_1, B_2, T_2, S)$) for AII variables $m_2$, $m_{236}$, $m_{23456}$ was extracted from the piece definitions (`verify_full_v9.py`).

The 4 distinct $m_2$ columns:

| $i_2$ | column $(M_1, M_2, B_1, T_1, B_2, T_2, S)$ | support |
|---|---|---|
| 0 | $(0, 0, 1, 0, 0, 0, 0)$ | $B_1$ |
| 1 | $(0, 0, 1, 0, 0, 0, 1)$ | $B_1, S$ |
| 2 | $(0, 0, 1, 0, 0, 0, 2)$ | $B_1, 2S$ |
| 3 | $(0, 1, 1, 0, 0, 0, 2)$ | $M_2, B_1, 2S$ |

These form a *staircase chain* in $(M_2, S)$-space:
$(0,0) \to (0,1) \to (0,2) \to (1,2)$.

The 9 distinct $m_{236}$ columns split $5 + 4$ by presence of $M_2$:

| $i_{236}$ | column | $M_2$ active? |
|---|---|---|
| 0 | $(0, 0, 0, 0, 1, 1, 0)$ — $B_2 + T_2$ | no |
| 1 | $(0, 0, 1, 1, 0, 0, 0)$ — $B_1 + T_1$ | no |
| 2 | $(0, 0, 1, 1, 1, 1, 0)$ — $(B_1+T_1)+(B_2+T_2)$ | no |
| 3 | $(0, 0, 1, 1, 2, 2, 0)$ — $(B_1+T_1)+2(B_2+T_2)$ | no |
| 4 | $(0, 0, 2, 2, 1, 1, 0)$ — $2(B_1+T_1)+(B_2+T_2)$ | no |
| 5 | $(0, 2, 1, 0, 0, 0, 0)$ — $2M_2+B_1$ | yes |
| 6 | $(0, 2, 1, 0, 0, 0, 2)$ — $2M_2+B_1+2S$ | yes |
| 7 | $(0, 2, 1, 0, 1, 1, 0)$ — $2M_2+B_1+B_2+T_2$ | yes |
| 8 | $(0, 2, 2, 1, 1, 1, 0)$ — $2M_2+2B_1+T_1+B_2+T_2$ | yes |

The 5 $M_2$-free columns are all of the form $(0, 0, a, a, b, b, 0)$ with
$(a, b) \in \{(0,1), (1,0), (1,1), (1,2), (2,1)\}$ — the 5 nearest-neighbor
lattice points around $(1,1)$ in $\mathbb Z^2$, omitting the corners
$(0,0)$, $(2,0)$, $(0,2)$, $(2,2)$.

The 8 distinct $m_{23456}$ columns split $4 + 4$ by $M_2$ presence:

| $i_{23456}$ | column | $M_2$ active? |
|---|---|---|
| 0 | $(0, 0, 0, 0, 1, 1, 0)$ — $B_2 + T_2$ | no |
| 1 | $(0, 0, 1, 0, 0, 0, 0)$ — $B_1$ | no |
| 2 | $(0, 0, 1, 0, 0, 0, 1)$ — $B_1 + S$ | no |
| 3 | $(0, 0, 1, 0, 0, 0, 2)$ — $B_1 + 2S$ | no |
| 4 | $(0, 2, 1, 0, 0, 0, 0)$ — $2M_2 + B_1$ | yes |
| 5 | $(0, 2, 1, 0, 0, 0, 1)$ — $2M_2 + B_1 + S$ | yes |
| 6 | $(0, 2, 1, 0, 0, 0, 2)$ — $2M_2 + B_1 + 2S$ | yes |
| 7 | $(0, 2, 1, 0, 1, 1, 0)$ — $2M_2 + B_1 + B_2 + T_2$ | yes |

Six of the eight ($i_{23456} \in \{1, 2, 3, 4, 5, 6\}$) form a clean
$2 \times 3$ grid $\{M_2 \in \{0, 1\}\} \times \{S \in \{0, 1, 2\}\}$ on
the "$B_1$-axis"; the other two ($i_{23456} \in \{0, 7\}$) are
"$B_2, T_2$-mass" outliers.

The full $(i_2, i_{236}, i_{23456})$ triple for each of the 22 pieces is
saved to `code/2026-06-11-bucket2-extract/bucket2_triples.json` and
`bucket2_indexing.json`.

### Verification of Day-63 §4 facts

- 22 distinct triples → $\pi_{\text{full}}$ injective ✓
- Marginals (4, 9, 8) ✓
- $\pi_{(m_{236}, m_{23456})}$ image size 21, with exactly one doubleton fibre at $((i_{236}, i_{23456}) = (0, 4))$ containing `P7_M2_dbl_T2_via_236` ($i_2 = 0$) and `P7_12_m2_M2_S` ($i_2 = 3$). ✓

## 2. Marginal-palindromy refutation

The per-index counts (number of Bucket-2 pieces at each column value):

| index | counts (in order) |
|---|---|
| $i_2 \in [4]$ | $(9, 10, 2, 1)$ |
| $i_{236} \in [9]$ | $(6, 3, 4, 3, 2, 1, 1, 1, 1)$ |
| $i_{23456} \in [8]$ | $(1, 4, 1, 2, 4, 5, 4, 1)$ |

Sorted multisets (invariant under relabelling of column indices):

| index | sorted multiset |
|---|---|
| $i_2$ | $\{1, 2, 9, 10\}$ |
| $i_{236}$ | $\{1, 1, 1, 1, 2, 3, 3, 4, 6\}$ |
| $i_{23456}$ | $\{1, 1, 1, 2, 4, 4, 4, 5\}$ |

### Theorem (palindromy of $B_3$, $C_3$ axis marginals)

Let $\mathfrak{g} = B_3$ or $C_3$. Let $V = \mathrm{adj}(\mathfrak{g}) \oplus \mathrm{triv}$ and $\mathrm{wts}(V)$ its weight multiset (22 weights, counting multiplicity). For any linear functional $f \colon \mathbb{R}^3 \to \mathbb{R}$, the level-set multiset
$$
H_f(k) := \#\{w \in \mathrm{wts}(V) : f(w) = k\}
$$
is *palindromic*: $H_f(k) = H_f(-k)$ for all $k \in \mathbb{R}$.

**Proof.** The longest Weyl element $w_0$ of $W(B_3) = W(C_3)$ acts as $-1$ on the weight space (standard fact: types $B_n$ and $C_n$ always satisfy $w_0 = -1$ since their Weyl groups are $\{\pm 1\}^n \rtimes S_n$). Hence $w \mapsto -w$ is an involution on $\mathrm{wts}(V)$ preserving multiplicities. For any linear $f$, $f(-w) = -f(w)$, so $H_f(-k) = H_f(k)$. $\square$

**Computation** (`refutation_proof.py`): for both $B_3$ and $C_3$, all 2000 random integer linear projections give palindromic histograms, confirming the theorem numerically.

### Corollary (refutation)

There is no bijection $\Phi \colon \{22 \text{ Bucket-2 pieces}\} \xrightarrow{\sim} \mathrm{wts}(\mathrm{adj}(\mathfrak{g}) \oplus \mathrm{triv})$ for $\mathfrak{g} \in \{B_3, C_3\}$, together with linear functionals $f_1, f_2, f_3 \colon \mathbb{R}^3 \to \mathbb{R}$, such that
$$
f_k(\Phi(p)) = c_k(p) \quad \text{for all pieces } p \text{ and } k \in \{1, 2, 3\},
$$
where $c_k(p)$ is the column-index of piece $p$ in axis $k$ ($k = 1, 2, 3$ for $m_2, m_{236}, m_{23456}$).

**Proof.** Suppose such $(\Phi, f_1, f_2, f_3)$ existed. Then the column-index marginal on axis $k$ equals $H_{f_k}$. By the theorem, $H_{f_k}$ is palindromic. But the $i_2$-marginal $(9, 10, 2, 1)$ is *not* palindromic — its sorted multiset $\{1, 2, 9, 10\}$ contains $9$ and $10$, but the only palindromic axis multiset for $B_3$ (resp. $C_3$) is $\{5, 5, 12\}$ (resp. $\{1, 1, 4, 4, 12\}$). Same contradiction on $i_{236}$ and $i_{23456}$. $\square$

### Scope of the refutation

The Weyl-fact $w_0 = -1$ holds for types $B_n$, $C_n$, $D_{2k}$, $E_7$, $E_8$, $F_4$, $G_2$. The other rank-3 candidate $A_3 = D_3$ (where $w_0 \ne -1$) has $\dim \mathrm{adj} = 15 \ne 21$, so the dimensional match $22 = \dim \mathrm{adj} + 1$ fails. **Hence no rank-3 semisimple Lie algebra admits a column-coordinate-respecting bijection.** Higher-rank candidates with $\dim \mathrm{adj} = 21$ don't exist (rank-4 $A_4 = 24$, rank-2 only gets to $G_2 = 14$).

## 3. Weyl-orbit labelling refutation

A weaker rep-theoretic claim would be: the 22 pieces are *labelled* by Weyl orbits of $\mathrm{adj}(\mathfrak{g}) \oplus \mathrm{triv}$, of sizes $\{12, 6, 3, 1\}$ (long roots, short roots, Cartan, trivial), without an explicit coordinate match.

**Refutation.** For a "natural" Weyl-orbit labelling, the orbit-class of a piece should be a function of intrinsic data — e.g., the column-index along one of the three axes, or a 2D projection.

| projection | max class size | contains 12? | contains 6? |
|---|---|---|---|
| $i_2$ | 10 | no | no |
| $i_{236}$ | 6 | no | yes (once) |
| $i_{23456}$ | 5 | no | no |
| $(i_2, i_{236})$ | 3 | no | no |
| $(i_2, i_{23456})$ | 5 | no | no |
| $(i_{236}, i_{23456})$ | 2 | no | no |

No single- or pairwise projection of the data admits the partition $\{12, 6, 3, 1\}$. Hence no natural Weyl-orbit labelling exists either. $\square$

## 4. Non-Lie alternative scan

22 is an unusual number for standard combinatorial structures:

- **3D polytopes.** No standard convex 3D polytope has 22 vertices. Closest is the dodecahedron (20) and the truncated cube/octahedron (24).
- **4-polytopes.** None of the standard polychora (5-cell 5, 8-cell 16, 16-cell 8, 24-cell 24, 120-cell 600, 600-cell 120) have 22 vertices.
- **Partitions of 8: $p(8) = 22$.** Tested statistics (largest part, length, distinct parts) give marginals $\{1, 1, 1, 2, 3, 4, 5, 5\}$, $\{1, 1, 1, 2, 3, 4, 5, 5\}$, $\{4, 5, 13\}$. None match our $\{1, 2, 9, 10\}$, $\{1,1,1,1,2,3,3,4,6\}$, $\{1,1,1,2,4,4,4,5\}$.

So no quick non-Lie identification jumps out either.

## 5. OQ-PI3-MULTI-FINAL

The Day-63 conjecture "the structural invariant of $\tilde\pi_3'$ as a stratified multimap has a rep-theoretic identification" is **refuted**.

**OQ-PI3-MULTI-FINAL (revised statement).** The MAX-stratum-vector of $\tilde\pi_3'$ is a **novel combinatorial invariant of multi-chart projections**, equal to the count of distinct $\sigma$-active column profiles among 26 piece-matrices in the Day-58 minimal cover. Its structural heart is the 22-point Bucket-2 configuration in $[4] \times [9] \times [8]$, whose marginals exhibit BDI/AII coordinate-substitution structure (an $(M_2, S)$ chain on $m_2$, an $M_2$-free / $M_2$-active split on $m_{236}$ and $m_{23456}$) but admit no Lie-theoretic embedding.

The configuration is therefore an honest "polytope-shadow combinatorics" object — not a hidden rep-theoretic relic.

## 6. Implications for v4 §3

The earlier hope ("v4 §3 climaxes with an adjoint-orbit interpretation") is removed. The replacement story for §3:

- The stratum-vector is the column-equivalence-count under $\sigma$-active subspaces.
- Its structural heart is the 22-Bucket-2 config, which decomposes into a *constructively traceable* BDI/AII coordinate calculus rather than a Lie label.
- **v4 §3 still has a climax**: it now reports a *novel combinatorial invariant*, which is publishable as "the stratified-multimap fingerprint of a polytope-shadow projection." This is a positive contribution — just not a rep-theoretic one.

## 7. Verification artifacts

- `code/2026-06-11-bucket2-extract/extract_triples.py` — extracts 22 triples from registry.
- `code/2026-06-11-bucket2-extract/bucket2_triples.json` — explicit columns.
- `code/2026-06-11-bucket2-extract/bucket2_indexing.json` — canonical indexing.
- `code/2026-06-11-bucket2-extract/analyze_structure.py` — marginal & sub-structure analysis.
- `code/2026-06-11-bucket2-extract/test_rep_theory.py` — $B_3$, $C_3$ weight multisets and marginal comparison.
- `code/2026-06-11-bucket2-extract/refutation_proof.py` — palindromy verification (2000 projections each) + sharp refutation statement.
- `code/2026-06-11-bucket2-extract/non_lie_scan.py` — $p(8)$, polytope checks.

## 8. Note for collaborator (Clio)

Day-64 PROVE settled OQ-PI3-MULTI Gap B in the negative. The 22 Bucket-2 pieces don't carry an adjoint-orbit label. The MAX-stratum-vector
$(3, 8, 11, 10, 19, 14, 23, 26)$ is a new combinatorial invariant. The cleanest line for v4 §3:

> *The MAX-stratum-vector is the count, per sign-stratum, of distinct $\sigma$-active column profiles of the 26-piece minimal cover; its structural heart is the 22-point Bucket-2 configuration, an explicit BDI/AII coordinate-substitution graph with non-palindromic marginals that refutes any rank-3 rep-theoretic identification.*

If you want a v4 §3 dual-track structure — one combinatorial track, one rep-theoretic track — keep §3 combinatorial only; the rep-theoretic side is dead.

— Rick, 2026-06-11 (Day 64 PROVE)
