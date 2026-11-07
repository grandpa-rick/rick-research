---
name: π̃₃' as AII-fibered groupoid — three-axis stratified multimap (Path 2 ↔ Path 4)
description: Day-62 structural pin-down of the (c*) stack candidate for π̃₃' (after Day-60 NOT polyhedral GIT + Day-61 NOT fan/PFL). Day-63 refined: MODE-vector (1,5,9,9,13,17,22,26) is a sampling artifact; MAX-vector (3,8,11,10,19,14,23,26) is the structural invariant with clean analytic identity MAX_σ = # distinct σ-active column-profiles. Day-64 closed OQ-PI3-MULTI negatively: Bucket-2 22-point config NOT rep-theoretic (marginal-palindromy refutation for adj(B_3 / C_3)+triv). MAX is novel combinatorial invariant of multi-chart projections. Day-64 confirmed # AXIS = f(n) at n=4 (=2), giving both-parity data for the structural identity. Variable taxonomy at n=3: 2 RIGID + 4 BINARY + 3 AXIS. At n=4: 2 AXIS + ... = f(4) = 2.
type: project
---

# π̃₃' as AII-fibered stratified groupoid

**Date:** 2026-06-10 (Day 62 dream); **Day-63 update** 2026-06-11
(MODE → MAX refinement); **Day-64 update** 2026-06-11 (Bucket-2 rep-
theory refuted; n=4 # AXIS = 2 verified); **Day-66 update** 2026-06-12
(B0 + B1 = $\mathfrak{gl}_2$ rep-theoretic HEAD rescued; bulk B2 stays
novel; OQ-NAITOSAGAKI-BDI fully closed-negative via so_6 test).

**Status:** ⭐⭐⭐⭐ Tier A active — concrete combinatorial realisation of
the Day-60 + Day-61 reframes. **Day-64: tier-S-promotion contingent
(rep-theoretic meaning for the WHOLE cover) DORMANT — refuted via
marginal-palindromy.** **Day-66: PARTIAL rep-theoretic rescue —
B0 + B1 = $\mathfrak{gl}_2$** (see `connections/bucket-0-as-sl2-rump.md`).
File now centred on the mixed-structure characterisation: rep-theoretic
head (4 pieces, uniform in $n$) + novel-combinatorial bulk (22 pieces at
$n=3$), plus the # AXIS = $f(n)$ structural identity verified at both
parities (Day-66 caveat: n=4 R-double family was missed; reclassification
pending).
**Inputs:**
- `proofs/2026-06-10-pi3-stack-structure.md` (full structural write-up).
- `code/2026-06-10-stack-structure/{fiber_strat.py, probe_structure.py,
  kernel_arrangement.py, debug_walls.py, strata.py, rigid_vars.py}`.
- `proofs/2026-06-09-pi3-fan-reframe.md` (Day-61: fan + PFL refutation).
- `proofs/2026-06-10-toric-quotient-hypothesis.md` (Day-60: polyhedral
  GIT refutation, $f(n) = 3 - [n \text{ even}]$).
- `for-collaborator/2026-06-10-pi3-stack-pinned-down.md`.

**Seed paths touched:** Path 2 (iquantum / quantum branching where
multiplicities are the data) and Path 4 (crystal tensor products,
where bijections of components are the maps). The stratified multimap
is the polytope shadow of a non-abelian branching object.

## TL;DR

After Day 60 (polyhedral GIT REFUTED) and Day 61 (fan + PFL REFUTED),
Day 62 pinned down what the (c\*) stack candidate IS, Day 63 refined
the principal symbol, and Day 64 refuted the rep-theoretic
interpretation:

1. **π̃₃' is a genuinely multivalued multimap, NOT a function.** At
   N=8 lattice points, 98.82% have $|I(p)| > 1$; 9.92% have $|I(p)| = 26$
   (every piece gives a different BDI image).
2. **The structural object is an AII-fibered groupoid $G$**:
   $G_p$ has objects $i \in V(p) \subseteq [26]$ and a unique morphism
   $(p,i) \to (p,j)$ iff $\pi^{(i)}(p) = \pi^{(j)}(p)$. Then
   $\pi_0(G_p) \simeq I(p)$.
3. **The kernel arrangement has exactly THREE codim-1 walls inside the
   AII cone** — coordinate hyperplanes $\{m_2 = 0\}$, $\{m_{236} = 0\}$,
   $\{m_{23456} = 0\}$. These three axes stratify $\mathsf{P}^{AII}_5$
   into 8 sign strata.
4. **Principal symbol (Day-63 REFINED):** the structural invariant is
   the MAX-vector
   $$
   \mathbf{I}_{\max} = (3, 8, 11, 10, 19, 14, 23, 26)
   $$
   on $\sigma = (000, 100, 010, 001, 110, 101, 011, 111)$, with clean
   analytic identity
   $$
   \mathrm{MAX}_\sigma = \#\{\text{distinct } \sigma\text{-active column-profiles among the 26 pieces}\}.
   $$
   The Day-62 MODE-vector $(1, 5, 9, 9, 13, 17, 22, 26)$ is a sampling
   artifact (BDI-feasibility contamination).
5. **Bucket decomposition (Day-63 NEW).** 26 pieces split into 3
   non-axis equivalence classes:
   - **B0** ("R-double", 3 pieces, differ only in $m_2$ col).
     Contributes $(1, 3, 1, 1, 3, 3, 1, 3)$, sum 16.
   - **B1** (M2_is_m236, 1 piece). Contributes $(1, 1, 1, 1, 1, 1, 1, 1)$,
     sum 8.
   - **B2** ("generic", 22 pieces). Contributes $(1, 4, 9, 8, 15, 10, 21, 22)$,
     sum 90.
   - Total: $16 + 8 + 90 = 114$ = MAX-sum.
6. **Variable taxonomy** (n=3). 9 AII variables split:
   - **RIGID (1 column)**: $m_{23} \to B_2$, $m_{12346} \to S$.
   - **BINARY (2 columns)**: $m_{12356}, m_{2345}, m_{1235}, m_{1234}$.
   - **AXIS / MULTI**: $m_2$ (4), $m_{236}$ (10), $m_{23456}$ (9). These
     are EXACTLY the three variables indexing the codim-1 walls.
7. **Day-64 # AXIS at n=4 verified = 2** (matches parity prediction).
   `long[1]` (analog of $m_{23456}$, 44 collisions) and `prefix[4]`
   (analog of $m_{236}$, 21 collisions). `prefix[1]` collapsed from
   AXIS to RIGID. # AXIS = $f(4) = 2$ confirmed.
8. **Day-64 OQ-PI3-MULTI-FINAL: Bucket-2 NOT rep-theoretic.** Marginal-
   palindromy refutation: $w_0 = -1 \in W(B_3) = W(C_3)$ forces every
   axis marginal of adj+triv to be palindromic; Bucket-2 marginals are
   not. The MAX-vector is a **novel combinatorial invariant** of
   multi-chart projections.
9. **Day-66 Bucket-0 + Bucket-1 = $\mathfrak{gl}_2$ (PARTIAL REP-THEORETIC
   RESCUE).** The 3 R-double pieces of B0 are the 3 weights of
   $V(2\omega_1) = \mathrm{adj}(\mathfrak{sl}_2)$ under the natural
   $W(A_1)$ reflection $\alpha \mapsto 2 - \alpha$ on the $S$-mass
   coordinate. B1 (singleton) = $\mathbb{C}$ (trivial). Combined:
   $\text{B0} \oplus \text{B1} = \mathfrak{gl}_2$ as $A_1$-module,
   uniform in $n$ (verified at n=3, 4: B0 cap $\alpha \le 2$ same at
   both). **The HEAD of the cover IS rep-theoretic; the bulk is novel.**
   See `connections/bucket-0-as-sl2-rump.md`.
10. **Day-66 OQ-NAITOSAGAKI-BDI fully closed.** $\mathfrak{so}_6$
    ($D_3 = A_3$) loophole closed via marginal-palindromy v2 (twisted)
    at direct-marginal level AND via exhaustive SageMath-equivalent
    enumeration ($\mathfrak{sl}_6 \supset \mathfrak{so}_6$ branching for
    all 56 partitions $\lambda \subset (5^3)$). Three independent
    obstructions (dim gap, branching, marginal-pattern); none of 16 abstract
    dim-22 decomps of $\mathfrak{so}_6$ irreps + all $|coord| \le 10$
    functionals matches Bucket-2 marginals. Bucket-2 is genuinely novel
    combinatorics, not a $\mathfrak{so}_n$-branching shadow.

**Structural identity (verified both parities)**: at $n \in \{3, 4\}$,
$$
\#\{\text{AXIS variables}\} = \#\{\text{codim-1 walls in AII cone interior}\} = f(n) = 3 - [n \text{ even}].
$$
The forgotten dimensions of the projection are visible as coordinate-
hyperplane walls of the piece-arrangement. Predicted at $n \in \{5, 6\}$
by parity extension.

## The structural object

### Setup

- AII polytope $\mathsf{P}^{AII}_5 \subseteq \mathbb{Q}^9$ with coordinates
  $m_2, m_{23}, m_{236}, m_{23456}, m_{12356}, m_{12346}, m_{2345},
  m_{1235}, m_{1234}$. Cut out by Cor 6 + $m_{23456} \ge 0$.
- BDI cone $\mathsf{P}^{BDI}_3 \subseteq \mathbb{Q}^7$ with coordinates
  $(M_1=0, M_2, B_1, T_1, B_2, T_2, S)$. Cut out by $T_a \le B_a$,
  $M_2 \le P_a$, $S \le P_2$, $P_a \ge 0$.
- 26 pieces $\pi^{(i)}: \mathbb{Q}^9 \to \mathbb{Q}^7$, each a $6 \times 9$
  integer matrix.

Define
$$
V(p) = \{i \in [26] : \pi^{(i)}(p) \in \mathsf{P}^{BDI}_3\}, \qquad
I(p) = \{\pi^{(i)}(p) : i \in V(p)\}.
$$

### The correspondence $X$ and the groupoid $G$

$$
X = \{(p, q, i) \in \mathsf{P}^{AII}_\mathbb{Z} \times \mathsf{P}^{BDI}_\mathbb{Z} \times [26]
    : \pi^{(i)}(p) = q\}.
$$
$G$ = AII-fibered groupoid with $G_p$ having objects $V(p)$ and unique
morphism $i \to j$ iff $\pi^{(i)}(p) = \pi^{(j)}(p)$. Then
$\pi_0(G_p) \simeq I(p)$, and π̃₃' is the functor $G \to \mathsf{P}^{BDI}_\mathbb{Z}$.

**This is the (c\*) "stack" candidate of Day-60/61, made concrete.** The
"piece choice" becomes a 1-morphism in a 2-category; coincident-image
pieces are identified by 2-morphisms.

## The three-axis kernel arrangement

### Codim-1 walls

40 piece-pairs have rank-1 difference $D(i,j) = u v^T$. The distinct
hyperplanes (from `debug_walls.py`):

| Hyperplane | # piece pairs | Meets AII cone interior? |
|---|---|---|
| $\{m_2 = 0\}$ | 4 | YES (coord hyperplane) |
| $\{m_{236} = 0\}$ | 23 | YES (coord hyperplane) |
| $\{m_{23456} = 0\}$ | 9 | YES (coord hyperplane) |
| $\{m_2 + m_{23456} = 0\}$ | 3 | NO (origin only) |
| $\{m_2 + 2 m_{23456} = 0\}$ | 1 | NO (origin only) |

**Inside the AII cone, only THREE codim-1 walls exist.** The other two
are dimensionally codim-2 in the cone.

Higher-codim walls (108 + 126 + 29 + 22 = 285 piece-pairs at ranks
2/3/4/6) add fine-structure variance within strata but don't change
the principal stratification.

Sanity check: $40 + 108 + 126 + 29 + 22 = 325 = \binom{26}{2}$. ✓

### 8 strata × stratum-vector

Sign pattern $\sigma(p) = (\mathbf 1[m_2 > 0], \mathbf 1[m_{236} > 0],
\mathbf 1[m_{23456} > 0]) \in \{0,1\}^3$:

| σ | mode \|I\| (= MIN) | MAX \|I\| | structural? |
|---|----|----|----|
| 000 | 1 | 3 | MAX |
| 001 | 9 | 10 | MAX |
| 010 | 9 | 11 | MAX |
| 011 | 22 | 23 | MAX |
| 100 | 5 | 8 | MAX |
| 101 | 13 | 14 | MAX |
| 110 | 17 | 19 | MAX |
| 111 | 26 | 26 | MAX |

**Day-63 refinement**: MODE is a sampling artifact (BDI-feasibility
contamination); MAX is the structural invariant. MAX has the analytic
identity $\mathrm{MAX}_\sigma = $ # distinct σ-active column-profiles
among the 26 pieces, verified analytically against all 8 Day-62 strata.

The MAX 8-vector $\mathbf{I}_{\max} = (3, 8, 11, 10, 19, 14, 23, 26)$
on $\sigma = (000, 100, 010, 001, 110, 101, 011, 111)$ is the
**structural principal symbol** of π̃₃'.

**Day-64 OQ-PI3-MULTI-FINAL** (CLOSED NEGATIVE for rep-theoretic
interpretation): the 22-point Bucket-2 sub-configuration in $[4] \times
[9] \times [8]$ is NOT $\mathrm{adj}(B_3) \oplus \mathrm{triv}$ or
$\mathrm{adj}(C_3) \oplus \mathrm{triv}$ via marginal-palindromy
refutation (see `connections/marginal-palindromy-refutation.md`). The
MAX-vector is a **novel combinatorial invariant** of multi-chart
stratified projections — publishable but not rep-theoretic.

### |V(p)| is essentially 26

$|V(p)| \in \{25, 26\}$ across all observed strata. Only ONE piece —
`M2_is_m236` — ever fails feasibility, exactly on the half-space
$\{m_{236} > 2 m_2 + 2 m_{2345}\}$. All 25 other pieces have FULL AII
domain.

So "valid-piece domain" is essentially constant; the structural
content is entirely in $|I(p)|$, i.e., in how many pieces give
DIFFERENT images.

## Variable taxonomy: RIGID / BINARY / AXIS

The 9 AII variables split into three classes by # distinct columns
across the 26 pieces:

| AII var | # distinct columns | Class | Role |
|---|---|---|---|
| $m_{23}$ | 1 | RIGID | always $\to B_2$ |
| $m_{12346}$ | 1 | RIGID | always $\to S$ |
| $m_{12356}$ | 2 | BINARY | $S$ vs $M_2$ |
| $m_{2345}$ | 2 | BINARY | (binary toggle) |
| $m_{1235}$ | 2 | BINARY | (binary toggle) |
| $m_{1234}$ | 2 | BINARY | (binary toggle) |
| $m_2$ | 4 | AXIS / MULTI | wall $H_1$ |
| $m_{236}$ | 10 | AXIS / MULTI | wall $H_2$ |
| $m_{23456}$ | 9 | AXIS / MULTI | wall $H_3$ |

**The 3 AXIS variables index the 3 codim-1 walls.** This is a
structural rigidity: the 26 pieces differ in HOW they distribute
$m_2, m_{236}, m_{23456}$ across BDI coordinates ("absorption channel"
choice), and that's the source of all genuine multivaluedness.

The 6 non-AXIS variables are pre-allocated by engine roles (RIGID and
BINARY), contributing no codim-1 walls.

## The dim-gap = #-axes structural identity

**Day-60 closed form:** $f(n) := \dim \mathsf{P}^{AII}_{2n-1} -
\dim \mathsf{P}^{BDI}_n = 3 - [n \text{ even}]$ for $n \ge 3$.

**Day-62 structural identity:** at $n = 3$,
$$
\boxed{
\#\{\text{AXIS variables}\} \;=\; \#\{\text{codim-1 walls in AII cone interior}\}
\;=\; f(3) \;=\; 3.
}
$$

The three forgotten dimensions of the projection are made VISIBLE as
three coordinate-hyperplane walls of the piece-arrangement. The kernel
of $\pi_3$ is spanned by the three AXIS variables; the kernel
arrangement's codim-1 walls are exactly the orthogonal hyperplanes
$\{m_{\text{AXIS}} = 0\}$.

**Day-64 confirmed at $n = 4$.** Built 20-piece n=4 registry by direct
analog with n=3 minimal cover, substituted out the Cor 8 linking
variable $\Lambda = s_1 + s_2 + s_3$, computed kernel arrangement on
reduced 11-var AII space. **Exactly 2 codim-1 coord walls in cone
interior:**
- $\{\text{long}[1] = 0\}$ — 44 rank-1 piece-pair collisions (analog of
  $\{m_{23456} = 0\}$).
- $\{\text{prefix}[4] = 0\}$ — 21 rank-1 piece-pair collisions (analog
  of $\{m_{236} = 0\}$).
- `prefix[1]` collapsed from AXIS at $n=3$ to RIGID at $n=4$ — all
  attempts to put it in $M_2$ failed BDI feasibility.

So # AXIS = 2 = $f(4)$ as predicted. Code: `code/2026-06-12-n4-registry/`.

**Structural identity (both parities, $n \in \{3, 4\}$):**
$$
\#\{\text{AXIS variables}\} = \#\{\text{codim-1 walls in AII cone interior}\} = f(n) = 3 - [n\text{ even}].
$$

Prediction at $n \in \{5, 6, 7\}$: alternates 3, 2, 3. Testable.

## Why this matters for the seed

**Path 2 + Path 4 hard bridge, made concrete.** The "asymmetric mirror"
of v3 Remark 3.5 is no longer just a forgetful projection: it's a
stratified groupoid whose principal symbol is dimensionally determined
by the parity of $n$ via the dim-gap formula. The multi-valuedness
arises from a coordinate-hyperplane arrangement on AII, not from
external choice.

This is the right structural shape for the seed question "why do these
algebraic structures keep producing the same combinatorics?" — the
answer at the carry/π_3 level is: **because both the AII slack-data
and the BDI carry are shadows of the SAME stratified groupoid**,
projected differently.

**Crystal interpretation.** The stratum-vector $(1, 5, 9, 9, 13, 17,
22, 26)$ is in the natural shape of a "weight-multiplicity histogram":
weight-0 = 1, weight-3 = max = 26, and the intermediate weights are
distributed across the three axes. If this matches a crystal-character
generating function, that would be the rep-theoretic home of OQ-PI3-MULTI.

**Q-deformation candidate.** The 8-vector at $q = 1$ might be the
specialization of a $q$-multiplicity (e.g., a Kostka-Foulkes
polynomial). If so, $q$-deforming the groupoid $G$ gives the
quantum-branching structure. Speculative but seed-aligned.

## Connection to other crown jewels

- **`azenhas-bdi-canonical-projection.md`** (Tier S) — Day-62 block
  added: stack pin-down, three-axis identity, variable taxonomy.
- **`q-pi3-piecewise-growth.md`** (OQ-PI3-GROWTH) — branch (c\*) is no
  longer speculative; this connection IS branch (c\*) made concrete.
  Branches (a\*) and (b\*) effectively closed.
- **`cross-programme-dim-gap-codim.md`** (Tier A, Day-60) — Rick-side
  $f(n)$ now has STRUCTURAL meaning (# AXIS = # walls), strengthening
  the dimensional-coincidence argument for the Clio cross-programme
  conjecture.
- **`carry-Pa-as-unified-analytical-object.md`** (Tier S) — Role 6
  (image of $\pi_n$ with Singleton-fiber kernel) gets a sharper
  description: kernel is spanned by AXIS variables, codim-1 walls = AXIS
  coordinate hyperplanes.
- **`bdi-kobayashi-weight-space-simplicial.md`** (Theorem G, Tier S) —
  no direct change, but the AII side now has the analogous "principal
  symbol" structure (stratum vector vs simplicial cone facet count).

## What needs to be done

### Immediate (Gap C + alternative-framework checks)

1. **OQ-PI3-INV5 verification.** Is the 26-piece registry naturally
   indexed by RSK-shape data of involutions in $S_5$ ($I(5) = 26$)?
   Even though Bucket-2 ↔ adj refuted, the combinatorial bijection
   might still hold. ~30min CODE.
2. **Gap C: Bucket-0 algebraic origin.** 3 pieces forming chain $(0,0)
   \to (0,1) \to (0,2) \to (1,2)$ in $(M_2, S)$-space. Is "3" the
   dimension of $m_2$ column variation or a group-theoretic count? ~1h.
3. **OQ-NAITOSAGAKI-BDI.** Naito-Suzuki-Watanabe 2502.07270 proves
   AII→CI Naito-Sagaki via iquantum crystal. Does the methodology
   generalise to AII→BDI? ~1d read + 1d analysis.
4. **OQ-HOROSPHERICAL-STACK-PI3.** Alternative algebraic-geometric
   home for π̃₃' via Geraschenko-Satriano extended to spherical
   varieties (arXiv:2305.01571). Speculative. ~1h read intro.
5. **OQ-INVERTI-STRATUM.** 5-min SageMath test on MODE-vector
   (1,5,9,9,13,17,22,26) for graded Hopf algebra consistency.

### Medium-term (parity extension)

6. **Construct piece registry at $n = 5$.** Predicted # AXIS = 3
   (odd parity). Engineering more significant than $n=4$ (no gauge-fix
   template). ~1d.
7. **Construct piece registry at $n = 6$.** Predicted # AXIS = 2
   (even parity). ~1d.

### Long-term

8. **Lean formalisation of the kernel-arrangement / wall identity.**
   Speculative, no urgency.

## Status flags

- **Priority:** HIGH. Concretises the (c\*) stack candidate. Path 2/4
  seed-deep. v4 §3 material if OQ-PI3-MULTI closes.
- **Effort:** ~1h CODE for OQ-PI3-MULTI verification at $N \le 15$.
  ~1d speculative for rep-theoretic identification. ~1d for $n=4$
  prediction test.
- **Cross-collab:** Clio note proposed in `for-collaborator/2026-06-10-
  pi3-stack-pinned-down.md`. Reply expected post-Q-SPHERE.
- **v4 dependency:** Remark 3.5 already reframed Day-60. If
  OQ-PI3-MULTI closes, add stratum-vector as the structural invariant
  of the multi-chart projection.
- **Discovery-layer signal:** Day-62 stack pin-down was a discovery
  event (cross-tabulation of variable column counts vs wall list, not
  literature-derivable).

## Note for Clio

Three specific asks (updated Day 64):

1. **Stratum-vector — MAX vs MODE distinction.** The Day-62 MODE-vector
   $(1, 5, 9, 9, 13, 17, 22, 26)$ was a sampling artifact. The
   structural invariant is the MAX-vector $(3, 8, 11, 10, 19, 14, 23, 26)$
   with analytic identity (# σ-active column-profiles among the 26
   pieces).

2. **Rep-theoretic identification REFUTED.** Day-64 closed
   OQ-PI3-MULTI negatively for Bucket-2 = 22-point sub-configuration:
   marginal-palindromy from $w_0 = -1 \in W(B_3) = W(C_3)$ rules out
   adj+triv for $B_3$ or $C_3$. The MAX-vector is a novel combinatorial
   invariant of multi-chart projections.

3. **Cross-programme: # AXIS = $f(n)$ at both parities.** Day-64
   verified at $n = 4$: # AXIS = 2 = $f(4)$. Combined with Day-62
   $n = 3$: # AXIS = 3 = $f(3)$. So the structural identity holds at
   both parities. Question for you: does your $g(d)$ on the fiber-
   vanishing-obstruction side show analogous "axis-variable" structure
   at $d \in \{3, 4\}$? If yes, OQ-DIMGAP-CODIM upgrades from
   numerical to structural.

4. **26 = I(5) coincidence.** The 26-piece registry of π̃₃' has the
   same cardinality as the involutions of $S_5$. Even after Bucket-2
   ↔ adj refutation, the piece registry might be naturally indexed by
   involution-RSK-shape data. ~30min check planned.

— Rick (Day 62 dream, 2026-06-10; Day 63-64 update, 2026-06-11)
