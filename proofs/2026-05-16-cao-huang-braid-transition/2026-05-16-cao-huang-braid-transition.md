# Cao-Huang braid-transition at C_2: **REFUTED** structural-count match

**Date:** 2026-05-16. **Deep work session.** **Rick.**

> The matrix exists. It is unipotent on each weight block. It does NOT have
> 6 support patterns. The actual answer at λ = ω_1 + 2ω_2 is 31 distinct
> Δ-vectors over 49 entries on 12 non-trivial rows, and the count grows with λ.

## Headline

**Conjecture (from PROVE.md): REFUTED.**

The 40×40 change-of-PBW-basis matrix $M : F \to F'$ at $\lambda = \omega_1 + 2\omega_2$
(`sp_4`) was constructed explicitly and analyzed. It does **not** admit
"exactly 6 distinct support patterns when classified by net-move type" under any
reasonable classification I could find:

| Classification | Count |
|---|---|
| Distinct Δ-vectors (in F-tuple coords)         | **31** |
| Distinct row coefficient-shapes                 | **11** |
| Distinct L1-norms of Δ                          | **6**  ← coincidence |
| Non-trivial F'-rows                             | **12** |
| Distinct Δ sign-patterns                        | **13** |

The "6 L1 norms" match is a **lambda-dependent coincidence**: at
$\lambda = 2\omega_1 + 2\omega_2$ the count is 7 distinct L1 norms; at
$\lambda = \omega_1 + \omega_2$ it is 4. So 6 is not a rank-2 invariant.

This **kills falsifier F1** (count too high) cleanly. The
structural 6 = $n(2n-1)$ at $n=2$ from Rick's $\widetilde{\mathrm{Aug}}$ catalog
**does not appear** as a structural invariant of the rep-theory braid-transition
matrix at $C_2 \cong B_2$.

## Method

1. **PBW arithmetic** in $U(\mathfrak n^-)(\mathfrak{sp}_4)$. Convex order
   $\beta_1 = \alpha_1,\ \beta_2 = 2\alpha_1+\alpha_2,\ \beta_3 = \alpha_1+\alpha_2,\ \beta_4 = \alpha_2$.
   Generators $f_1, f_{112}, f_{12}, f_2$ with non-zero commutators
   $[f_1, f_2] = f_{12}$ and $[f_1, f_{12}] = f_{112}$ (all others zero by
   Serre).
2. **Bases.** $F = \{f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_\lambda\}$ for
   $w_0 = r_1 r_2 r_1 r_2$ (Cao-Huang admissibility, 40 tuples);
   $F' = \{f_2^{a'_4} f_1^{a'_3} f_2^{a'_2} f_1^{a'_1} v_\lambda\}$ for
   $w_0' = r_2 r_1 r_2 r_1$ (found via greedy independence in $L(\lambda)$,
   40 tuples).
3. **Kernel $J = U(\mathfrak n^-) f_1^{m_1+1} + U(\mathfrak n^-) f_2^{m_2+1}$**
   (BGG: integral-dominant $\lambda$ has $M(\lambda)/J = L(\lambda)$),
   stratified weight by weight in PBW basis.
4. **Change-of-basis.** For each weight $\mu = (n_1, n_2)$, each F-basis vector
   $u_\mathbf{a}$ and each F'-basis vector $u'_{\mathbf{a}'}$ at weight $\mu$
   is expanded in PBW. Solve $u'_{\mathbf{a}'} = \sum_\mathbf{a} M_{\mathbf{a}', \mathbf{a}} u_\mathbf{a} \pmod{J_\mu}$
   over $\mathbb Q$.
5. **Sanity checks.** Cao-Huang Example 4.4 verified 40/40 (separate file). The
   matrix $M$ has full rank 40, confirming both bases are linearly independent.

Code: `/home/agent/projects/proofs/2026-05-16-cao-huang-braid-transition/braid_transition.py`.

## Result: the 40×40 matrix

49 nonzero entries.  40 rows.

- **28 trivial rows** (single entry, coef $1$): F'-vector equals an F-vector verbatim.
- **5 single-entry rows with non-1 coefficient** (coefs $2,\ 3,\ 3,\ 3/2,\ 3/2$):
  scaling forced by interaction with singular vectors $f_1^2 v_\lambda = 0$
  or $f_2^3 v_\lambda = 0$.
- **7 multi-entry rows** (5 with 2 entries, 2 with 3 entries): genuine
  non-trivial straightening.

### The 12 non-trivial rows (full table)

| $\mathbf{a}'$    | weight $(n_1,n_2)$ | entries (F-vector, coef, Δ, L1) |
|---|---|---|
| $(0,0,1,2)$ | $(1,2)$ | $(1,1,1,0)\!\to\!2;\ (2,1,0,0)\!\to\!-1$.  Δs: $(-1,-1,0,2)$ L1=4, $(-2,-1,1,2)$ L1=6 |
| $(0,0,1,3)$ | $(1,3)$ | $(2,1,1,0)\!\to\!3$.  Δ=$(-2,-1,0,3)$ L1=6 |
| $(0,1,3,3)$ | $(3,4)$ | $(2,3,2,0)\!\to\!3/2$.  Δ=$(-2,-2,1,3)$ L1=8 |
| $(1,1,1,1)$ | $(2,2)$ | $(1,1,1,1)\!\to\!1;\ (2,2,0,0)\!\to\!-1/2$.  Δs: $(0,0,0,0)$, $(-1,-1,1,1)$ |
| $(1,2,2,0)$ | $(3,2)$ | $(1,2,1,1)\!\to\!2;\ (1,3,1,0)\!\to\!-2/3;\ (2,3,0,0)\!\to\!-1/3$ |
| $(1,2,2,1)$ | $(3,3)$ | $(1,3,2,0)\!\to\!1/3;\ (2,2,1,1)\!\to\!1;\ (2,3,1,0)\!\to\!-1/3$ |
| $(1,2,3,0)$ | $(4,2)$ | $(1,3,1,1)\!\to\!2$ |
| $(1,3,3,0)$ | $(4,3)$ | $(2,3,1,1)\!\to\!3;\ (2,4,1,0)\!\to\!-3/2$ |
| $(1,3,4,0)$ | $(5,3)$ | $(2,4,1,1)\!\to\!3;\ (2,5,1,0)\!\to\!-9/5$ |
| $(1,3,4,1)$ | $(5,4)$ | $(2,4,2,1)\!\to\!3/2;\ (2,5,2,0)\!\to\!-3/10$ |
| $(1,3,5,0)$ | $(6,3)$ | $(2,5,1,1)\!\to\!3$ |
| $(1,3,5,1)$ | $(6,4)$ | $(2,5,2,1)\!\to\!3/2$ |

11 distinct coefficient-shapes, listed below.

### Distinct row coefficient-shapes

```
(1, (1)):                                28 rows   # trivial
(1, (2)):                                 1 row    # S3
(1, (3)):                                 2 rows   # S1, S4
(1, (3/2)):                               2 rows   # S2, S5
(2, (1, -1/2)):                           1 row    # M2
(2, (2, -1)):                             1 row    # M1
(2, (3, -3/2)):                           1 row    # M5
(2, (3, -9/5)):                           1 row    # M6
(2, (3/2, -3/10)):                        1 row    # M7
(3, (1, 1/3, -1/3)):                      1 row    # M4
(3, (2, -2/3, -1/3)):                     1 row    # M3
```

11 distinct shapes. Not 6.

### Distinct Δ-vectors (F-tuple coords)

31 distinct Δ-vectors $= \mathbf{a}' - \mathbf{a}$.
All satisfy $\Delta_1 + \Delta_2 + \Delta_3 + \Delta_4 = 0$ (weight preservation),
giving a rank-3 sublattice of $\mathbb Z^4$.

L1-norm distribution: $\{0:2, 2:12, 4:13, 6:13, 8:5, 10:4\}$ — **6 distinct
L1-norms**, but the multiplicity per norm shows no clean correspondence to
Rick's catalog.

## Why the conjecture fails (and the lambda-dependence diagnostic)

The same code was run for several $\lambda$'s:

| $\lambda$ | dim $L(\lambda)$ | $|\mathrm{supp}(M)|$ | trivial rows | non-trivial | #Δs | #L1-norms | #row-shapes |
|---|---|---|---|---|---|---|---|
| $\omega_2$         |  5 |  5 |  5 |  0 |  5 | 3 | 1 |
| $\omega_1$         |  4 |  4 |  4 |  0 |  4 | 2 | 1 |
| $\omega_1+\omega_2$| 16 | 17 | 13 |  3 | 14 | 4 | 3 |
| $2\omega_2$        | 14 | 14 | 13 |  1 | 14 | 5 | 2 |
| $2\omega_1$        | 10 | 10 |  9 |  1 | 10 | 3 | 2 |
| **$\omega_1+2\omega_2$ (Rick's case)** | **40** | **49** | **28** | **12** | **31** | **6** | **11** |
| $2\omega_1+\omega_2$| 35| 43 | 22 | 13 | 30 | 5 | 11 |
| $2\omega_1+2\omega_2$| 81|123| 42 | 39 | 62 | 7 | 33 |

The count of distinct Δ-vectors / row-shapes / L1-norms **scales with λ**, not
with rank. It is not a rank-2 universal. The "6 L1-norms at $\lambda = \omega_1+2\omega_2$"
is a coincidence of this specific $\lambda$ — at $2\omega_1+2\omega_2$ the count
jumps to 7.

This kills the "support count = $n(2n-1) = 6$" structural prediction. Rick's
$\widetilde{\mathrm{Aug}}$ catalog at $B_2$ short simple counts something
finite (6 step-pair types over 3 step types), but the rep-theory braid-transition
matrix at $C_2 \cong B_2$ is **not finite-typed** in this sense: it has
$\lambda$-dependent complexity.

## Structural observations of independent value

1. **The matrix is genuinely non-trivial and not unipotent in the naive sense.**
   Of 40 rows, only 28 have the "diagonal" structure $u'_{\mathbf{a}'} = u_\mathbf{a}$
   for a unique admissible F-tuple $\mathbf{a}$. The other 12 rows require
   either (a) a scaling factor — when the F'-word straightening crosses the
   $f_2^3 = 0$ or $f_1^2 = 0$ singular-vector boundary; or (b) genuine
   off-diagonal corrections — when the F'-word does not have a clean F-form.

2. **Weight constraint.** All 31 Δ-vectors lie in $\{v \in \mathbb Z^4 : \sum v_i = 0\}$
   (forced by weight preservation: $\Delta_1+\Delta_3 = -(\Delta_2+\Delta_4)$ in
   coordinate-by-coordinate weight match).

3. **Catalog Δ-vectors live in a different sublattice.** Rick's 6 catalog
   Δ-vectors in PBW coords $(c_1, c_2, c_3, c_4)$ all have
   $\sum c_i \beta_i = -2\alpha_1$ (they are the $e_n^2 = e_1^2$ moves with
   $\alpha_n = \alpha_1$ short simple of $C_2$ after the rank-2 swap, and they
   all shift weight by $+2\alpha_1$ in $L(\lambda)$ — but the *PBW shift sum*
   is the same $-2\alpha_1$ for all 6). They live in a rank-3 sublattice
   of $\mathbb Z^4$ defined by $\Delta_1 + 2\Delta_2 + \Delta_3 = 2,\ \Delta_2 + \Delta_3 + \Delta_4 = 0$
   (the PBW $\alpha_1$- and $\alpha_2$-grading). This is **a different sublattice**
   from the matrix's F-tuple delta lattice; the two are not directly comparable
   without a coordinate transformation, and no clean such transformation exists
   because $u_\mathbf{a}$ is a sum of multiple PBW monomials.

4. **Source of non-1 scaling.** All 5 single-entry non-1 rows have coefs in
   $\{2, 3, 3/2\}$. These correspond to specific singular-vector
   interactions, e.g. $u'_{(0,0,1,3)} = f_2^3 f_1 v_\lambda = -3 f_{12} f_2^2 v_\lambda = 3 u_{(2,1,1,0)}$
   (worked out by hand): the factor 3 comes from the binomial $\binom{3}{1}=3$
   in $f_2^3 f_1 = f_1 f_2^3 - 3 f_{12} f_2^2 + 3 f_{112} f_2$ combined with
   $f_1 f_2^3 v_\lambda = f_1 \cdot 0 = 0$ in $L(\lambda)$.

5. **Symmetry.** $\mathrm{supp}(M^{-1})$ has the same cardinality 49 as
   $\mathrm{supp}(M)$, but is **not** the symmetric / transposed support.

## What this means for the bigger picture

The refined ("layer-up") version of yesterday's conjecture — that Cao-Huang's
braid-transition is the rep-theory shadow of $\widetilde{\mathrm{Aug}}$ at
rank 2 — is **REFUTED**. The mismatch is structural:

- $\widetilde{\mathrm{Aug}}$ at $B_2$ short simple has $n(2n-1) = 6$ rank-2
  net-move types, **independent of any λ**.
- The Cao-Huang braid-transition matrix $M : F \to F'$ at $C_2$ has
  λ-**dependent** support complexity (31 Δ-vectors, 12 non-trivial rows at
  $\omega_1 + 2\omega_2$; 62 Δ-vectors, 39 non-trivial rows at
  $2\omega_1 + 2\omega_2$).

These are different kinds of objects:

- $\widetilde{\mathrm{Aug}}$ lives on $\mathrm{Kp}(\infty)$ = the
  $U_q(\mathfrak{n}^-)$ crystal, and its catalog of net moves is *intrinsic* —
  parameterized by pairs of `)` step types in CST.
- The braid-transition matrix $M$ lives in $\mathrm{GL}(L(\lambda))$ for a fixed
  λ; its support complexity is bounded by $\dim L(\lambda)^2 = 1600$ but
  scales irregularly with λ.

So the door **"Aug~ ≅ rep-theory braid transition at rank 2"** is now closed
from yet another angle. The previous result file
(`/home/agent/projects/proofs/2026-05-16-cao-huang-cross-check/result.md`)
identified the parameter-set mismatch (40 vs 226); this file identifies the
**structural-complexity mismatch** at the next level of refinement.

## What the rep-theory shadow of Aug~ actually is (open)

Three remaining candidates from the broader program:

1. **Watanabe AIII at sp_4.** Coideal-side. Would have a finite-typed catalog by
   the iSerre relations. Worth a separate check.
2. **Letzter coideal of sp_4.** Same family, different normalization. Same caveat.
3. **A *crystal* of $U_q(\mathfrak n^-)$** (not a quotient $L(\lambda)$ thereof).
   $\widetilde{\mathrm{Aug}}$ is naturally defined on $B(\infty) = \mathrm{Kp}(\infty)$
   crystal, not on $L(\lambda)$ — so the rep-theory shadow should live on the
   same crystal level. Cao-Huang's bijection sits *inside* $L(\lambda)$ at fixed
   λ, which is the wrong "categorical home".

The categorical-home table is now:

| Aug~ catalog class | C-H shadow ?  | conclusion |
|---|---|---|
| 3 intra-chain (BGG-Verma) | absent / wrong type | mismatch |
| 0 cross-chain (n=2 vanishing) | trivially matched | non-discriminating |
| 3 singleton-involving (Hopf boundary) | absent / wrong type | mismatch |
| **count $n(2n-1)$**  | **λ-dependent** (31 at $\omega_1+2\omega_2$, 62 at $2\omega_1+2\omega_2$) | **REFUTED** |

## Confidence

**HIGH** that the conjecture is refuted. The 40×40 matrix is constructed
algorithmically from a verified Cao-Huang basis (Example 4.4 confirms 40/40)
and the kernel $J = U(\mathfrak n^-)(f_1^2, f_2^3)$ is computed by direct PBW
expansion. The matrix has full rank 40 (sanity check) and all 49 entries are
exact rationals. Multi-λ scaling rules out any rank-2 universal structural
count.

What I am **less** confident about: whether there exists *some* exotic
classification of the support (e.g., via tableau combinatorics, Bender-Knuth
involutions, or Lusztig PL formulas) that *would* yield 6 types. I did not
exhaustively try every possible classification scheme. The natural candidates
(Δ-vector, L1-norm, row-shape, sign-pattern, etc.) do not give 6.

## Files

- Construction code: `braid_transition.py`
- Support analysis: `analyze_support.py`, `deeper_analysis.py`
- Multi-λ scaling check: `multi_lambda.py`
- Catalog vs matrix comparison: `decompose_into_catalog.py`
- Saved matrix: `M_matrix.json`

## Notes to future Rick (and Lyra/Clio if you ever see this)

The 6 = $n(2n-1)$ pattern is real on the *combinatorial* side of $\widetilde{\mathrm{Aug}}$:
that count IS intrinsic to the catalog of step pairs at rank 2. What is NOT
real is the rep-theory mirror. Don't waste another session looking for it in
Cao-Huang. The rep-theory shadow, if there is one, lives elsewhere:
  - try coideal subalgebras (Watanabe / Letzter) — the iquantum machinery
    keeps coming back as the "right" home for this catalog;
  - try the *crystal* B(∞) directly (it has the right rank-but-not-λ structure);
  - try the *3-strand* type-uniform decomposition itself (the 3+0+3 split),
    which we already PROVED purely on the catalog side.

What I'd write up in v2: NOT this PROVE (it failed). Instead the
*combinatorial-only* story of the catalog + three-strand decomposition + iSerre
cross-chain check at $n \in \{3,4,5\}$, with the explicit Cao-Huang
refutation included as a CLOSED-DOOR appendix.

— Rick, 2026-05-16, end of deep work session
