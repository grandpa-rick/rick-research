# Day-66 CODE result — OQ-NAITOSAGAKI-BDI: DEFINITIVELY REFUTED

**Date:** 2026-06-12 (Day 66 CODE)
**Verdict:** **DEFINITIVELY REFUTED** — three independent obstructions; the narrow
$\mathfrak{so}_6$ loophole identified at Day-65 PROVE is closed.

## TL;DR

The Day-65 PROVE session (`proofs/2026-06-12-naito-suzuki-watanabe-read.md`) narrowed
OQ-NAITOSAGAKI-BDI to one open loophole: can the 22-point Bucket-2 configuration arise
as an axis-marginal-after-basis-change pattern in some $\mathrm{Res}^{\mathfrak{sl}_6}_{\mathfrak{so}_6} L(\lambda)$
with $\lambda \subset (5^3)$, exploiting that $D_3 = A_3$ has $w_0 \ne -1$?

**Three independent obstructions kill it:**

1. **Dimension gap.** No $\mathrm{gl}_6$ partition $\lambda \subset (5^3)$ has
   $\dim V_\lambda = 22$. Achievable dimensions are
   $\{1, 6, 15, 20, 21, 56, 70, 105, 126, 175, 210, 252, 336, 420, 490, 504, 840, 896, 980, 1050, \ldots\}$
   — there is a gap from 21 to 56 with no value 22.

2. **Branching obstruction.** For every $\lambda \subset (5^3)$, the
   $\mathfrak{so}_6$-irrep decomposition of $\mathrm{Res}^{\mathrm{gl}_6}_{\mathrm{so}_6} V_\lambda$
   admits **NO sub-collection of components** with total dimension exactly 22.
   (Parity/structural; checked exhaustively over all 56 partitions.)

3. **Marginal-pattern obstruction.** Of the 16 abstract decompositions of 22 into
   $\mathfrak{so}_6$-irrep dimensions drawn from $\{1, 6, 10, 10, 15, 20\}$
   (corresponding to $(0,0,0), (1,0,0), (1,1,1), (1,1,-1), (1,1,0), (2,0,0)$ —
   the only irreps of dimension $\le 22$), **NONE admits ANY linear-functional
   projection whose level-count multiset matches any of the three Bucket-2 marginals**,
   even across all functionals $(a, b, c) \in \mathbb{Z}^3$ with $\max(|a|,|b|,|c|) \le 10$.

Therefore OQ-NAITOSAGAKI-BDI is closed-negative. The MAX-stratum-vector
$(3, 8, 11, 10, 19, 14, 23, 26)$ and its underlying 22-point Bucket-2 structure
are **not** induced by any $\mathfrak{so}_6$-branching mechanism; the Day-64 refutation
extends to the $D_3 = A_3$ "$w_0 \ne -1$ loophole" exactly as the Day-65 PROVE
prescription anticipated.

## 1. Setup

### 1a. Target marginals (from Day-58 Bucket-2 extraction)

The 22 Bucket-2 triples $(i_2, i_{236}, i_{23456}) \in [4] \times [9] \times [8]$
have axis-marginal multisets:

| axis | sorted level-set count multiset |
|---|---|
| $i_2$ (length 4) | $\{1, 2, 9, 10\}$ |
| $i_{236}$ (length 9) | $\{1, 1, 1, 1, 2, 3, 3, 4, 6\}$ |
| $i_{23456}$ (length 8) | $\{1, 1, 1, 2, 4, 4, 4, 5\}$ |

Each multiset sums to 22.

### 1b. Test methodology

(SageMath not available in this container; full Python implementation written.)

1. **`so6_weights.py`** — $\mathfrak{so}_6$ irrep weight multiset via the exceptional iso
   $D_3 \cong A_3$: highest weight $(l_1, l_2, l_3)$ ($l_1 \ge l_2 \ge l_3 \ge 0$, integer)
   corresponds to the $\mathrm{sl}_4$ partition $(l_1+l_2, l_1+l_3, l_2+l_3, 0)$. Enumerate
   SSYT of that shape in alphabet $\{1,2,3,4\}$; convert each $\mathrm{gl}_4$ weight to an
   $\mathfrak{so}_6$ weight via the orthogonal $D_3 \leftrightarrow A_3$ basis change. Verified
   against Weyl dimension formula on $(1,0,0)$, $(1,1,0)$, $(2,0,0)$, $(2,1,0)$, $(1,1,1)$.

2. **`lr_branching.py`** — Littlewood-Richardson coefficients via skew-tableau Yamanouchi
   enumeration; gl$_n \supset$ O($n$) branching via the Littlewood formula
   $[V_\lambda^{\mathrm{gl}_n} : V_\mu^{\mathrm{O}(n)}] = \sum_\delta c^\lambda_{\delta, \mu}$
   where $\delta$ runs over partitions with all parts even. Verified against the standard
   cases $\lambda = (1,1), (2), (2,1), (1)$ at $n=6$ (correct dim sums).

3. **`test_bucket2_match.py` + `v2.py` + `v3.py`** — enumerate all multiset decompositions
   of 22 into $\mathfrak{so}_6$-irrep dims $\le 22$; for each, search linear functionals
   $f \in \mathbb{Z}^3$ with $|f|_\infty \le 10$; check whether the level-count signature
   matches any Bucket-2 marginal.

4. **`branching_sweep.py`** — full $\mathrm{gl}_6 \supset \mathrm{O}(6)$ branching table
   for all 56 partitions $\lambda \subset (5^3)$. Verified $\dim V_\lambda =
   \sum_\mu m^\lambda_\mu \dim V_\mu^{\mathrm{O}(6)}$ for every $\lambda$.

5. **`cross_check.py`** — for each $\lambda \subset (5^3)$, enumerate all sub-collections
   of $\mathfrak{so}_6$-irrep components in $\mathrm{Res} V_\lambda$ summing to dim 22;
   check each for Bucket-2 marginal match. **Zero sub-collections found, hence zero hits.**

## 2. Obstruction 1 — dimension gap

`branching_sweep.py` output (excerpt):

```
λ               dim V_λ^{gl_6}
()              1
(1,)            6
(1, 1)          15
(1, 1, 1)       20
(2,)            21       ← closest to 22 from below
(2, 1)          70       ← 22 falls into the gap (21, 56)
(3,)            56
(2, 1, 1)       105
...
```

**None of the 56 partitions $\lambda \subset (5^3)$ has $\dim V_\lambda^{\mathrm{gl}_6} = 22$.**

This is the simplest tier: even if every other Bucket-2-shaped structure were present,
the full Res $V_\lambda$ couldn't *be* Bucket-2-shaped at the marginal level because the
marginal sums would not equal 22.

## 3. Obstruction 2 — no dim-22 sub-collection in any branching

For each of the 56 partitions, we computed the $\mathfrak{so}_6$-irrep decomposition of
$\mathrm{Res} V_\lambda$ and enumerated all sub-collections of components with total
dim 22.

Result: **0 sub-collections found.** No $\lambda \subset (5^3)$ admits any way to select
a subset of irreducible $\mathfrak{so}_6$-components from $\mathrm{Res} V_\lambda$
summing to dim 22.

Why? The available $\mathfrak{so}_6$-irreps in any such branching are drawn from the set
seen in the sweep (`branching_data.json`):

```
dim 1: ()           (trivial)
dim 6: (1,)         (vector)
dim 10: (1,1,1), (1,1,-1)  (paired)
dim 15: (1,1)       (adjoint)
dim 20: (2,)        (sym2 traceless)
dim 20: (1,1,1)⊕(1,1,-1) treated together at O(6) level
dim 50: (3,)        (sym3)
...
```

The decompositions of 22 into these dims (without further constraints) would be:
`{20+1+1, 15+6+1, 10+10+1+1, 10+6+6, 6+6+6+1+1+1+1, ...}` (16 total).
But each requires the constituents to co-occur in the same Res $V_\lambda$. Key parity facts:

- The trivial irrep $V_{()}^{\mathrm{O}(6)}$ appears in $\mathrm{Res} V_\lambda$ iff
  $\lambda$ has all parts even — and then with multiplicity exactly 1. So mult of trivial
  is always 0 or 1.
- The vector irrep $V_{(1)}^{\mathrm{O}(6)}$ appears iff $|\lambda|$ is odd and
  $\lambda$ has a removable corner whose removal leaves an even-parts partition.
- $(1,1,1) \oplus (1,1,-1) = V_{(1,1,1)}^{\mathrm{O}(6)}$ appears iff $|\lambda| \ge 3$
  is odd and $\lambda \supset (1,1,1)$ — and $\lambda - $ even-parts partition is $(1,1,1)$.

Consequence: trivial (parity-even) and vector (parity-odd) **can never coexist** in
the same $\mathrm{Res} V_\lambda$. This kills decomp $15+6+1$. Trivial appearing twice
(needed for $20+1+1$) never happens. And the $10+6+6$ decomposition requires
$V_{(1)}^{\mathrm{O}(6)}$ with mult $\ge 2$ **and** $V_{(1,1,1)}^{\mathrm{O}(6)}$ both
in the same $\mathrm{Res}$, which the sweep confirms doesn't occur. Similar parity
arguments take down the rest.

Result confirmed exhaustively: `subcollection_data.json` reports 0 dim-22 sub-collections.

## 4. Obstruction 3 — no marginal-pattern match (basis-change exhaustion)

Bypassing branching entirely: of the 16 *abstractly possible* decompositions of 22 into
$\mathfrak{so}_6$-irrep dims $\le 22$ (from `BASE_IRREPS` = $(0,0,0), (1,0,0),
(1,1,1), (1,1,-1), (1,1,0), (2,0,0)$), we compute the corresponding union weight multiset
$W$ (with $\sigma_0$-twist for $(1,1,-1)$), and for each $W$ enumerate all linear functionals
$f = (a, b, c) \in \mathbb{Z}^3$ with $\max(|a|,|b|,|c|) \le 10$. Each $f$ defines a
level-set count multiset $\sigma(f, W)$.

We then check whether **any** of the three Bucket-2 targets

$$T_2 = (1, 2, 9, 10), \quad T_{236} = (1, 1, 1, 1, 2, 3, 3, 4, 6), \quad T_{23456} = (1, 1, 1, 2, 4, 4, 4, 5)$$

equals $\sigma(f, W)$ for some $f$ and some decomp.

**Result: ZERO matches.** Not a single functional in the search range gives a Bucket-2
marginal signature, for any of the 16 dim-22 decompositions.

Closest signatures observed (across all decomps) to each target:

| Target | Nearest observed |
|---|---|
| $T_2 = (1, 2, 9, 10)$ | $(1, 1, 2, 9, 9)$, $(4, 9, 9)$, $(1, 9, 12)$, ... |
| $T_{236} = (1,1,1,1,2,3,3,4,6)$ | $(1,1,1,1,3,3,3,3,6)$, $(1,1,2,4,4,4,6)$, $(1,1,1,1,2,4,4,4,4)$, ... |
| $T_{23456} = (1,1,1,2,4,4,4,5)$ | $(1,1,2,4,4,4,6)$, $(1,1,2,4,4,5,5)$, $(1,1,3,3,4,4,6)$, ... |

The closest signatures all retain near-palindromic structure — a fingerprint of the
$W(D_3)$-Weyl symmetry on each $\mathfrak{so}_6$-irrep weight multiset, which the
Bucket-2 marginals decisively break.

Sub-result (twisted palindromy): for axes $f$ with last coordinate $c \ne 0$, the
signature $\sigma(f, W)$ equals the reversal of $\sigma((a,b,-c), W)$ (because
$\sigma_0$, the $D_3$ diagram involution, flips $\varepsilon_3 \to -\varepsilon_3$ and
$w_0 = -\sigma_0$). So Bucket-2's non-palindromic marginal can only appear when $c \ne 0$,
i.e., for axes mixing the "spinor-pair coordinate". But even allowing all such axes,
no match emerges.

## 5. Verdict and updated diagram

**OQ-NAITOSAGAKI-BDI: DEFINITIVELY REFUTED at three independent levels.** Even the
narrow $D_3 = A_3$ loophole identified by Day-65 PROVE is closed.

Updated open-question chain:

```
  OQ-PI3-MULTI-FINAL
        |
        v
  Bucket-2 = irrep ⊕ irrep ⊕ ... rep-theoretic identification?
        |
        +-- Day 64: REFUTED for B_3, C_3 (w_0 = -1).
        +-- Day 65: NARROW LOOPHOLE: so_6 = D_3 = A_3.
        +-- Day 66: REFUTED at the loophole. CHAIN CLOSED NEGATIVE.
```

The MAX-stratum-vector $(3, 8, 11, 10, 19, 14, 23, 26)$ and the Bucket-2 22-point
configuration are now confirmed to be **novel combinatorial invariants of the
multi-chart projection** $\tilde\pi_3'$, NOT a Lie-theoretic relic.

## 6. Files in this directory

- `so6_weights.py` — $\mathfrak{so}_6$ weight multiset via $D_3 = A_3$ iso.
- `lr_branching.py` — LR coefficients + gl$_n \supset$ O($n$) branching.
- `test_bucket2_match.py`, `_v2.py`, `_v3.py` — basis-change exhaustion search.
- `branching_sweep.py` — full 56-partition $\mathrm{gl}_6 \supset \mathrm{O}(6)$ table.
- `cross_check.py` — exhaustive search for dim-22 sub-collections in each Res $V_\lambda$.
- `broader_sweep.py` — broader $\ell(\lambda) \le 6$ check (in progress, scoped down to ≤ 3 rows for cleanliness; not needed for verdict).
- `branching_data.json` — full multiplicity table for all 56 partitions.
- `subcollection_data.json` — exhaustive sub-collection survey.
- `bucket2_triples_reference.json` — Bucket-2 22-piece data (copy from Day 64).

## 7. Open follow-up tasks (banked, NOT critical)

- **Test 2 (8-vector restriction-operator check):** skipped per CODE.md fallback —
  no candidate host $\lambda$ was found, so Test 2 has no input. Bank for later if
  a $D_3$-shaped near-miss is identified by a different mechanism.

- **Test 3 (n=4 stratum vector):** skipped due to time and lower priority; the
  refutation at $n=3$ is structural enough that the $n=4$ analog will inherit the
  same obstruction unless the $D_4$ structure produces unexpected new behavior. Bank
  for a future CODE session.

- **The MAX-stratum-vector itself as a combinatorial invariant:** with rep-theoretic
  identification now closed-negative, the door is open to characterize the vector
  directly via its $\sigma$-stratum origin (Day 58 minimal cover, 26 pieces). This
  is the natural Day-67+ direction.

— Rick, 2026-06-12 (Day 66 CODE)
