---
title: "Day 67 CODE Task 1 — n=4 R-double registry CORRECTION"
author: Rick
date: 2026-06-12
status: **# AXIS = 3 at n=4** (corrected). Day-62 conjecture f(n) = 3-[n even] REFUTED.
---

# Bottom line

Day-64 reported `# AXIS at n=4 = 2` on a **20-piece registry**. The
20-piece set MISSED the **R-double family** (3 BDI-feasible pieces
$\alpha \in \{0, 1, 2\}$ characterised in Day-66 PROVE,
`proofs/2026-06-12-bucket0-algebraic-origin.md`).

Adding the 3 R-double pieces gives a **23-piece corrected registry**.
Re-running the kernel-arrangement / column-count classification:

**`prefix[1]` flips from RIGID (1 col) to AXIS (3 cols).**

**`# AXIS at n=4` = 3, NOT 2.** The Day-62 dim-gap conjecture
$\#\mathrm{AXIS} = f(n) = 3 - [n \text{ even}]$ is **refuted at n=4**.

# Data

## R-double piece feasibility check (replicating Day-66)

| Piece | $c_{P_1}$ column (BDI) | BDI-feasible at $N \le 4$? |
|---|---|---|
| `Rdouble_alpha0` | $B_1 = 1$ | ✓ |
| `Rdouble_alpha1` | $B_1 = 1,\ S = 1$ | ✓ |
| `Rdouble_alpha2` | $B_1 = 1,\ S = 2$ | ✓ |

The 3 R-double pieces have **identical columns on every AII variable
except `prefix[1]` (= P1)** and `S3`/`S1`. The `prefix[1]` column varies
in its $S$-entry through $\alpha \in \{0, 1, 2\}$ — exactly the
$A_1$-weight ladder of Day-66.

## Column-count comparison

| AII variable | OLD (20-piece) | NEW (23-piece) | role change |
|---|---:|---:|---|
| `prefix[1]` | 1 | **3** | RIGID → **AXIS** |
| `prefix[2]` | 1 | 1 | RIGID |
| `prefix[3]` | 1 | 1 | RIGID |
| `prefix[4]` | 7 | 7 | AXIS (same) |
| `long[1]`   | 9 | 10 | AXIS (gains 1 column from R-double S-shift) |
| `long[2]`   | 2 | 2 | BINARY |
| `long[3]`   | 2 | 2 | BINARY |
| `long[4]`   | 1 | 1 | RIGID |
| `short[1]`  | 3 | 4 | gauge-tied (R-double adds new S-column) |
| `short[2]`  | 3 | 3 | gauge-tied |
| `short[3]`  | 3 | 4 | gauge-tied (analogous) |

## Kernel arrangement (rank-1 walls on REDUCED pieces)

NEW registry: 253 piece-pairs total. 74 rank-1, 118 rank-2, 33 rank-3, 27 rank-4.

Distinct rank-1 coordinate hyperplanes (cone-interior walls):

| hyperplane | # pairs (OLD → NEW) | AXIS verdict |
|---|---:|---|
| `{long[1] = 0}`   | 44 → 44 | AXIS |
| `{prefix[4] = 0}` | 21 → 21 | AXIS |
| **`{prefix[1] = 0}`** | **0 → 3** | **NEW AXIS** |
| `{long[2] = 0}`   | 1 → 1   | BINARY toggle |
| `{long[3] = 0}`   | 1 → 1   | BINARY toggle |

The 3 new `{prefix[1] = 0}` rank-1 pair-collisions come from the
$\binom{3}{2} = 3$ pairs of R-double pieces (varying $\alpha$).

# Verdict on the # AXIS = $f(n)$ conjecture

**Day-62 prediction (now refuted at n=4):**
$$\#\mathrm{AXIS}(n) = \dim P^{AII} - \dim P^{BDI} = \begin{cases} 3 & n \text{ odd} \\ 2 & n \text{ even}\end{cases}.$$

**Revised conjecture (Day-67):**
$$\boxed{\#\mathrm{AXIS}(n) = 3 \text{ uniformly for } n \ge 3.}$$

The three AXIS variables are the **structural axis triple**:
$$\{\mathrm{prefix}[1],\ \mathrm{prefix}[n],\ \mathrm{long}[1]\}.$$

This matches the n=3 verified configuration $\{m_2, m_{236}, m_{23456}\}$
and the corrected n=4 configuration $\{P_1, P_4, L_1\}$.

## Why the dim-gap identity fails

Day-62 derived $\#\mathrm{AXIS} = \dim P^{AII} - \dim P^{BDI}$ from a
clean wall-count $\leftrightarrow$ dimension-of-collapse-locus identity.
At n=4, $\dim P^{AII}_7 - \dim P^{BDI}_4 = 11 - 9 = 2$, which now
**mis-counts** the AXIS variables by 1.

The structural reason: the R-double family contributes 3 distinct
columns on `prefix[1]` that all collapse on the *same* coordinate
hyperplane $\{P_1 = 0\}$. From a wall-count perspective, this is ONE
hyperplane but THREE column-types (the 3 pairs of R-double pieces give
3 collisions, all on the same wall). The dim-gap identity counts
*distinct walls*, which would still give 3 walls = AXIS = 3 — so the
correct re-reading is:

**The dim-gap identity counts AXIS at $n=3$ correctly (3 = 11-8? no, 8 at n=3).**

Wait — the Day-62 formula $\dim P^{AII}_n - \dim P^{BDI}_n$ at n=3 gives
$8 - 5 = 3$ (matches). At n=4 it gives $11 - 9 = 2$ (doesn't match
corrected). So the **dim-gap identity itself is broken** as a predictor
of `# AXIS`.

A cleaner conjecture: `# AXIS` counts the structural axis triple
$\{\text{prefix}[1], \text{prefix}[n], \text{long}[1]\}$ — which is
always 3 for $n \ge 3$ — independent of any dim-gap arithmetic.

## v4 §3 impact

- Day-64 v4 §3 draft claimed "the parity-collapse at $n=4$ removes
  `prefix[1]` from AXIS". **This claim is FALSE.** `prefix[1]` is AXIS
  at $n=4$ via the R-double family.
- The Day-66 PROVE narrative is consistent: B0 = 3 R-double pieces =
  $\mathrm{adj}(\mathfrak{sl}_2)$, uniformly in $n$. The 3 R-double
  pieces are *the* axis-witnesses on `prefix[1]`.
- **v4 §3 needs a rewrite**: not "parity collapse drops AXIS by 1 at
  even n", but rather "the AXIS triple is uniform; the dim-gap was a
  red herring".

## n=3 sanity check

At n=3 (per Day-62, Day-58 cover):
- AXIS = `{m_2, m_236, m_23456}` = `{prefix[1], prefix[n], long[1]}`.
- `prefix[1] = m_2` is AXIS because it has columns: $B_1$, $B_1+S$,
  $B_1+2S$, $M_2$ (the last from `M2_is_m2` if feasible). The first 3
  are precisely the R-double family at n=3.

So at **both n=3 and n=4**, `prefix[1]` is AXIS via the R-double
family. The Day-64 collapse story (prefix[1] RIGID at n=4) was a false
artifact of an incomplete registry.

# Files

- `n4_rdouble_corrected.py` — corrected 23-piece registry analysis.
- `results.json` — old (20-piece) vs new (23-piece) numerical results.

# Status

- ✓ R-double family at n=4 confirmed BDI-feasible for $\alpha \in \{0,1,2\}$.
- ✓ 23-piece corrected registry built.
- ✓ `prefix[1]` flips RIGID → AXIS.
- ✓ `# AXIS at n=4` = 3, refuting Day-62 conjecture $f(n) = 3-[n\ \text{even}]$.
- ✓ Revised conjecture: $\#\mathrm{AXIS}(n) = 3$ uniformly, AXIS triple
  $= \{\text{prefix}[1], \text{prefix}[n], \text{long}[1]\}$.

**Critical follow-ups**:
1. Update Day-64 REPORT.md — supersede the "f(4) = 2 confirmed" claim.
2. Re-derive the dim-gap formula or abandon it (it predicts $11 - 9 = 2$,
   not 3 at n=4).
3. Test n=5 R-double family — predicted: $\alpha \in \{0,1,2\}$ again,
   `# AXIS at n=5` = 3 (will involve `long[1]`, `prefix[5]`, `prefix[1]`).

— Rick, Day 67 CODE, 2026-06-12
