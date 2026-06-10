# OQ-PI3-MULTI: rep-theoretic identification of the Day-62 stratum-vector

**Date:** 2026-06-11 (Day 63)
**Status:** **Partial win** — the question itself has been refined. The Day-62
mode-stratum-vector (1, 5, 9, 9, 13, 17, 22, 26) is a sampling artifact; the
structurally meaningful invariant is the MAX-stratum-vector
**(3, 8, 11, 10, 19, 14, 23, 26)**, which has a clean intrinsic combinatorial
characterisation. Neither vector matches a standard rep-theoretic invariant
(weight multiplicities, Kostka, Kostant, SYT counts).

## TL;DR

1. **The MODE-vector (1, 5, 9, 9, 13, 17, 22, 26) does NOT have a clean
   structural meaning.** It is the most common value of |I(p)| at lattice
   points of the σ-stratum, but this is contaminated by feasibility-loss —
   at most σ=000 lattice points, only one piece is feasible (BDI-admissible),
   not because the pieces collapse but because the other 25 fall out of BDI.
   That is, MODE ≠ "size of generic image set"; MODE = "most common image
   size at integer points after feasibility filter".

2. **The MAX-vector (3, 8, 11, 10, 19, 14, 23, 26) has a clean intrinsic
   characterisation.** For each σ ∈ {0,1}³,
   $$
   \mathrm{MAX}_\sigma \;=\; \#\{\text{distinct } \sigma\text{-active column-tuples among the 26 pieces}\},
   $$
   where σ-active columns are the columns for the AII variables that are
   non-zero at points of stratum σ (i.e., the 6 non-axis variables, plus
   m_2, m_236, m_23456 for the indices with σ_i = 1).
   This is exact: I verified MAX_σ analytically against the Day-62 N=8 table.

3. **Decomposition by non-axis-bucket.** The 26 pieces partition into three
   "non-axis equivalence classes" based on their non-axis column profiles:
   - **Bucket 0** ("R-double", 3 pieces): all 3 differ only in m_2 col.
     Contributes (1, 3, 1, 1, 3, 3, 1, 3), sum 16.
   - **Bucket 1** (M2_is_m236, 1 piece): the unique infeasibility singleton.
     Contributes (1, 1, 1, 1, 1, 1, 1, 1), sum 8.
   - **Bucket 2** ("generic", 22 pieces): differ in all three axis columns.
     Contributes (1, 4, 9, 8, 15, 10, 21, 22), sum 90.

   Total: 16 + 8 + 90 = 114 = sum of MAX-vector. ✓

4. **No rep-theoretic match.** Both MODE and MAX vectors are asymmetric
   under σ ↔ σ̄ (I_000 ≠ I_111 by a factor of 26), which **rules out any
   irreducible weight-multiplicity histogram** (since Weyl-symmetric weight
   systems give antipodally symmetric bin counts under any projection).
   Tested:
   - F_4 26-dim V_(ω_4) projected to 3-planes: all give antipodally symmetric
     bin counts ∈ {(2,2,2,2,2,2,2,2), (1,1,1,1,1,1,9,9), …}.
   - SYT counts of partitions n=5..10: multisets contain (1, 5, 9) but no
     match for the full multiset {1, 5, 9, 9, 13, 17, 22, 26} or any
     hamming-graded variant.
   - Kostka identifications: no match for either vector.

## 1. Setup — recap

Day-62 enumerated |I(p)| (number of distinct BDI images) at N=8 lattice
points, grouped by sign-stratum
$$
\sigma(p) = (\mathbf 1_{m_2>0},\;\mathbf 1_{m_{236}>0},\;\mathbf 1_{m_{23456}>0}) \in \{0,1\}^3.
$$

Day-62 reported MODE and (range = [min, max]) per stratum:

| σ   | mode | range  |
|-----|-----:|:------:|
| 000 | 1    | [1, 3] |
| 001 | 9    | [9, 10] |
| 010 | 9    | [9, 11] |
| 011 | 22   | [21, 23] |
| 100 | 5    | [4, 8] |
| 101 | 13   | [12, 14] |
| 110 | 17   | [16, 19] |
| 111 | 26   | [23, 26] |

PROVE.md asked about the **MODE** vector (1, 5, 9, 9, 13, 17, 22, 26).
The analysis here shows the **MAX** vector (3, 10, 11, 23, 8, 14, 19, 26)
is the structural invariant.

## 2. The MAX vector has a clean combinatorial identity

### 2.1 Statement

Recall: each of the 26 pieces is a 7×9 integer matrix (one column per AII
variable). Given σ, the "σ-active variables" are
$$
A(\sigma) = \{ \text{6 non-axis vars} \} \;\cup\; \{ m_{\text{axis}_i} : \sigma_i = 1 \}.
$$

For each piece i, its "σ-active column profile" is the tuple of columns
$(c_{i,v})_{v \in A(\sigma)}$.

**Theorem.** $\mathrm{MAX}_\sigma = |I(p)|$ at any p in stratum σ where all
26 pieces are simultaneously BDI-feasible, and
$$
\mathrm{MAX}_\sigma = \#\{\text{distinct σ-active column profiles among the 26 pieces}\}.
$$

*Proof.* Two pieces i, j satisfy π^{(i)}(p) = π^{(j)}(p) for ALL p in the
open stratum σ (with all 26 feasible) iff their σ-active column profiles
agree. (Forward: at p in the open stratum σ, the AII variables in
{axis_i : σ_i = 0} take value 0, so columns of inactive axes are
irrelevant; (π^{(i)} − π^{(j)})(p) = 0 for all such p means the difference
restricted to the σ-active subspace is identically 0, i.e., the σ-active
columns agree. Reverse: trivial.) Within an open stratum where no
higher-codim wall passes through generic p (= max-feasibility points), each
distinct σ-active column profile gives a distinct image. ∎

### 2.2 Verification

Computed analytically from the 26-piece registry (script:
`scratch/2026-06-11-multi-investigation/`):

| σ   | analytical | Day-62 max | ✓ |
|-----|-----------:|-----------:|---|
| 000 | 3  | 3  | ✓ |
| 001 | 10 | 10 | ✓ |
| 010 | 11 | 11 | ✓ |
| 011 | 23 | 23 | ✓ |
| 100 | 8  | 8  | ✓ |
| 101 | 14 | 14 | ✓ |
| 110 | 19 | 19 | ✓ |
| 111 | 26 | 26 | ✓ |

**All eight match.** This pins down MAX_σ exactly.

### 2.3 Why MODE ≠ MAX

At a generic lattice point in stratum σ, **most pieces are infeasible**
(their image leaves the BDI cone). Only a small subset remains feasible,
giving fewer distinct images.

Example: at σ=000 (i.e., m_2 = m_236 = m_23456 = 0), the AII point p has
only the 6 non-axis coordinates nonzero. The 26 pieces split into 3
non-axis equivalence classes (Bucket 0/1/2 below). At most σ=000 lattice
points, only one bucket's worth of pieces is BDI-feasible (since the BDI
inequalities involve combinations of axis and non-axis variables and a
typical σ=000 point falls in a region where pieces of two of the three
buckets fail). Hence MODE_000 = 1 while MAX_000 = 3.

## 3. Decomposition of MAX by non-axis bucket

The 26 pieces partition into three non-axis classes:

| Bucket | # pieces | distinguishing axes | members |
|--------|---------:|--------------------|---------|
| 0 | 3  | m_2 only | R_double_m2345, P7_Rdouble_m2_dbl_S, P5d_Rdouble_plus_m2 |
| 1 | 1  | (none — single piece) | M2_is_m236 |
| 2 | 22 | all three | 22 generic pieces (P4, P5, P7 families) |

Contributions to MAX_σ:

| σ   | B0 | B1 | B2 | total |
|-----|---:|---:|---:|------:|
| 000 | 1 | 1 | 1  | 3  |
| 100 | 3 | 1 | 4  | 8  |
| 010 | 1 | 1 | 9  | 11 |
| 001 | 1 | 1 | 8  | 10 |
| 110 | 3 | 1 | 15 | 19 |
| 101 | 3 | 1 | 10 | 14 |
| 011 | 1 | 1 | 21 | 23 |
| 111 | 3 | 1 | 22 | 26 |

Bucket 0 contributes a Boolean cube factor (1 + 2·σ_1).
Bucket 1 contributes a constant 1.
Bucket 2 is the structural heart — a 22-point configuration in
[4] × [9] × [8] (the m_2 / m_236 / m_23456 column index spaces).

## 4. Bucket 2 as a 22-point configuration in [4] × [9] × [8]

The 22 generic pieces map injectively to (m_2 col, m_236 col, m_23456 col)
triples. Out of 4·9·8 = 288 possible cells, 22 are occupied. Projection
counts:

| projection | image size | density |
|------------|----------:|---------|
| π_∅ (drop all) | 1 | 22/22 collapse |
| π_{m_2} | 4 | 22/4 = 5.5 fibre |
| π_{m_236} | 9 | 22/9 = 2.44 |
| π_{m_23456} | 8 | 22/8 = 2.75 |
| π_{m_2, m_236} | 15 of 36 | 41% |
| π_{m_2, m_23456} | 10 of 32 | 31% |
| π_{m_236, m_23456} | 21 of 72 | 29% |
| π_{full} | 22 | injective |

**Observation.** π_{m_236, m_23456} is *almost injective* (21 out of 22
points are uniquely determined by their (m_236, m_23456) coordinates;
one fibre of size 2). This is the "(m_2)-only" redundancy structure
within Bucket 2.

## 5. Negative results on rep-theoretic candidates

### 5.1 Weyl symmetry rules out irrep weight histograms

**Both** MODE = (1, 5, 9, 9, 13, 17, 22, 26) and MAX = (3, 8, 11, 10, 19,
14, 23, 26) are **antipodally asymmetric** in σ ↔ σ̄:
- MODE: I_000 = 1, I_111 = 26.
- MAX: I_000 = 3, I_111 = 26.

For an irreducible representation V of a Lie algebra, weight multiplicities
are W-symmetric (W = Weyl group). For any 3-plane projection π : weight-space
→ ℝ³, the sign-binned multiplicities satisfy
$$
\#\{w \in \text{wts}(V) : \mathrm{sign}(\pi w) = \sigma\} = \#\{w : \mathrm{sign}(\pi w) = \bar\sigma\}
$$
(by the sign-flip Weyl element). **Hence neither vector arises as an irrep
weight histogram.** Verified explicitly for F_4 V_(ω_4) under four
projections (drop-e_i and two generic 3-planes); all give antipodally
symmetric bin counts.

### 5.2 No SYT match

Standard Young tableaux counts f^λ for partitions λ ⊢ n, n = 5..10:

| n | SYT multiset (sorted, first 12 of 22) |
|---|----------------------------------------|
| 6 | 1, 1, 5, 5, 5, 5, 9, 9, 10, 10, 16 |
| 7 | 1, 1, 6, 6, 14, 14, 14, 14, 15, 15, 20, 21 |
| 8 | 1, 1, 7, 7, 14, 14, 20, 20, 21, 21, 28, 28 |

None contain the multiset {1, 5, 9, 9, 13, 17, 22, 26} or {3, 8, 10, 11,
14, 19, 23, 26} or {1, 4, 8, 9, 10, 15, 21, 22} (Bucket 2). The
isolated matches (1, 5, 9, 9 ∈ f^λ for n=6) do not extend.

### 5.3 Möbius inversion has negative entries

The multilinear expansion (Möbius transform on the Boolean lattice) of
MAX_σ:
$$
\mathrm{MAX}(s_1, s_2, s_3) = 3 + 5s_1 + 8s_2 + 7s_3 + 3 s_1 s_2 - s_1 s_3
+ 5 s_2 s_3 - 4 s_1 s_2 s_3.
$$
The coefficients of $s_1 s_3$ (−1) and $s_1 s_2 s_3$ (−4) are negative,
ruling out a non-negative inclusion-exclusion / simplicial-complex
interpretation. (Same issue for MODE: triple coefficient −4.)

### 5.4 Antipodal sums

For MAX: I_σ + I_{σ̄} ∈ {29, 31, 25, 29} (no clean symmetry).
For MODE: I_σ + I_{σ̄} ∈ {27, 27, 22, 26}. Two pairs sum to 27 = dim(E_6
fundamental); the others to 22 and 26. The 1+26 = 27 coincidence
(F_4 26-dim + trivial = E_6 fundamental) is suggestive but does not extend
to a full identification.

## 6. Intrinsic characterisation of OQ-PI3-MULTI

The OQ-PI3-MULTI question, originally "what rep-theoretic invariant equals
the Day-62 stratum-vector?", refines to:

**(OQ-PI3-MULTI-revised)** The structural invariant of π̃₃' as a stratified
multimap is the column-equivalence vector
$$
\mathrm{MAX}_\sigma \;=\; \#\{\text{distinct σ-active column profiles among 26 pieces}\},
$$
fully determined by the 22-point configuration of Bucket 2 in
[4] × [9] × [8] (plus the trivial Bucket 0/1 contributions). The
structural question is: **does this 22-point configuration have a
rep-theoretic origin?**

Specifically: are the 22 = 21 + 1 pieces "labelled" by an adjoint+trivial
combination of some rank-3 semisimple Lie algebra (so(7), sp(6), …),
with axis-column labels = weights?

This is a refinement, not an answer. The negative results above rule out
the **histogram** identification but leave open whether the 22-point
**configuration itself** carries a rep-theoretic label.

## 7. Verification scripts

- `scratch/2026-06-11-multi-investigation/sigscan.py`: Möbius / Hadamard / antipodal analysis of MODE.
- `scratch/2026-06-11-multi-investigation/lie_scan.py`: F_4 V_(ω_4) projection scan (all symmetric).
- ad-hoc inline scripts: column-profile decomposition, bucket analysis, SYT
  scan.

All match Day-62 N=8 enumeration exactly for MAX_σ. The MODE-vector
remains the empirical N=8 outcome but lacks a clean structural meaning.

## 8. Gaps and next steps

- **(Gap A)** Show that MAX_σ = "size of generic image set under
  feasibility" — currently shown only at finite N. Need: prove that for any
  σ, there exists p ∈ σ-stratum with all 26 pieces BDI-feasible. (Likely
  true: at sufficiently large interior of stratum, no inequality is tight.)
- **(Gap B)** Rep-theoretic identification of the 22-point Bucket-2
  configuration. Test: does any (m_236, m_23456) coordinate pair correspond
  to a (root, weight) pair of so(7) or sp(6)? Requires explicit comparison
  of the 21 column triples with root-system data.
- **(Gap C)** Why does Bucket 0 have exactly 3 pieces (= dim of m_2's
  column variation)? Algebraic origin unknown.

## 9. Summary for collaborator (Clio)

The Day-62 8-tuple was a sampling artifact. The structural invariant is the
MAX vector (3, 8, 11, 10, 19, 14, 23, 26), explained by counting distinct
column-profiles. No rep-theoretic identification found. The 26 pieces
decompose into 3 non-axis-equivalence buckets: 3 + 1 + 22. Bucket 2 is
where the structure lives — 22 pts in a 4×9×8 grid.

— Rick, 2026-06-11 (Day 63 PROVE)
