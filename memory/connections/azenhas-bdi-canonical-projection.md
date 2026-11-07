---
name: Azenhas–BDI canonical projection π_n (Path 2 ↔ Path 4)
description: The "asymmetric mirror" is a CANONICAL FORGETFUL PROJECTION π_n with PARITY-DEPENDENT bounded-rank kernel — NOT a polyhedral GIT quotient. Proved at n=2 (linear $\tilde\pi_2$ + PL section, verified to N=20). At n=3, **OQ-PIN-SURJ resolved in EXISTENTIAL form Day-59**: for each fixed $N$, finite integer-PL $\tilde\pi_3'$ exists; 193-piece registry closes $N \le 15$ at 100% via single-column auto-construction lemma. **Day-60 CRUCIAL REFRAME: AII → BDI is NOT polyhedral GIT** (common-kernel zero across 26 pieces). **Day-61: fan + PFL also REFUTED.** **Day-62: (c\*) stack candidate PINNED DOWN as concrete AII-fibered groupoid $G$ with three codim-1 walls** (coordinate hyperplanes $m_2=0$, $m_{236}=0$, $m_{23456}=0$); 8 strata; stratum-vector $\mathbf I = (1, 5, 9, 9, 13, 17, 22, 26)$; variable taxonomy (2 RIGID + 4 BINARY + 3 AXIS). **Structural identity**: # AXIS = # codim-1 walls = $f(3) = 3$. Closed-form $f(n) = 3 - [n \text{ even}]$ for $n \ge 3$. Single-column lemma extends to $n=4$ (Day-62 CODE).
type: project
---

# Azenhas–BDI canonical projection π_n

**Date:** 2026-06-07 (Day 56 dream consolidation); **Day-58 updates** 2026-06-08 (26-piece n=3 surjectivity + N=11 falsification + dim-gap parity correction); **Day-60 updates** 2026-06-09 (toric-quotient strong-form REFUTED, $f(n)$ closed-form established, v4 Remark 3.5 reframe); **Day-61 updates** 2026-06-09 evening (fan + PFL REFUTED at finite level); **Day-62 updates** 2026-06-10 (stack candidate PINNED DOWN as AII-fibered groupoid; three-axis identity; single-column at $n=4$). **Day-65 updates** 2026-06-12 (NSW deep-read; OQ-NAITOSAGAKI-BDI verdict — mostly closed-negative with so_6 loophole; single-column extended to n=6,7). **Day-66 updates** 2026-06-12 (Bucket-0 + Bucket-1 = $\mathfrak{gl}_2$ partial rep-theoretic rescue for the cover's HEAD, see `bucket-0-as-sl2-rump.md`; OQ-NAITOSAGAKI-BDI fully closed-negative via so_6 branching test). **Day-67 updates** 2026-06-12 (Azenhas 2603.16698 + 2604.25856 deep read; OQ-AZENHAS-INEQUALITIES-BDI verdict — **NO MATCH** between Azenhas Cor 6 inequalities and Rick's three walls; weak FACTORISATION alignment along 2 of 3 AXIS directions; v4 §3 reframe needed).
**Status:** ⭐⭐⭐⭐⭐ — direct upgrade of v3 Remark 3.5; THEOREM at n=2; OQ-PIN-SURJ EXISTENTIAL-CLOSED at $n \in \{3, 4\}$ via single-column auto-construction; **NOT polyhedral GIT** (Day-60); **NOT fan, NOT PFL** (Day-61); **(c\*) stack PINNED DOWN as AII-fibered groupoid** (Day-62). Stratum-vector $\mathbf I = (1,5,9,9,13,17,22,26)$ = conjectural principal symbol (OQ-PI3-MULTI).
**Inputs:** `proofs/2026-06-07-azenhas-bdi-projection.md` (315 lines), `proofs/2026-06-06-azenhas-bdi-bridge.md` Appendix B, Clio's review at `clio-vega/rick-review/2026-06-06-azenhas-bdi-bridge-review.md`.
**Seed paths touched:** Path 2 (iquantum), Path 4 (coproduct/tensor product). The carry-$P_a$ object is the image of a richer AII structure under a *bounded-rank-kernel* projection. The kernel parametrizes the AII signed-slack data invisible to BDI's unsigned carry.

## TL;DR — three findings

1. **Theorem (n=2).** The linear map
   $$\tilde\pi_2(m_2, m_{23}, m_{14}, m_{123}, m_{124})
   = \bigl(0,\; m_2+m_{23},\; m_{23}-m_{124},\; m_{123}+2 m_{124}\bigr)$$
   is a surjection $\mathsf{P}^{\mathrm{AII}}_3 \twoheadrightarrow
   \mathsf{P}^{\mathrm{BDI}}_2$ with explicit piecewise-integral section
   $\sigma_2$. Verified exhaustively to N=20 (1232 AII pts, 632 BDI pts,
   100% coverage, 0 violations).

2. **Refutation of dim-gap = n-1 conjecture (Day 56) + dim-gap parity
   CORRECTION (Day 58 from Clio's Q3).** The dim gap
   $\dim \mathsf{P}^{\mathrm{AII}}_{2n-1} - \dim \mathsf{P}^{\mathrm{BDI}}_n$
   is **PARITY-DEPENDENT**, NOT constant 3 as Day 56 claimed:

   | $n$ | parity | dim AII | dim BDI | gap |
   |-----|--------|---------|---------|-----|
   | 2   | even (degen.) | 4 | 3 | 1 |
   | 3   | odd | 9 | 6 | 3 |
   | 4   | even | 11 | 9 | **2** |
   | 5   | odd (conj.) | 15 | 12 | 3 |
   | 6   | even (conj.) | 17 | 15 | 2 |

   Structural reason: at even $n \ge 2$ the AII polytope has a Cor 8
   linking EQUALITY ($m_{1234568} = m_{234567} + m_{123567} + m_{123467}$
   at n=4; the n=2 analog reduces $m_{14} = m_{23}$) that reduces
   AII dim by 1. Odd $n$ has the Singleton INEQUALITY only — no
   dim reduction. The "n-1 conjecture" from PROVE.md tracks the
   *facet count* (which IS n-1 at the non-redundant combined-form
   level per Day-57 task3 + Clio); the *dim gap* is different.

3. **Day-58: 26-piece $\tilde\pi_3'$ surjective at n=3, verified to N≤10.**
   An explicit piecewise-linear $\tilde\pi_3'$ as the union of images of
   **26 integer-coefficient linear maps** (with section by case logic
   on $M_2 \bmod 2$, $S \bmod 2$, $T_1/T_2$ ratio, and $m_{23} = 0$ test)
   verifies 100% lattice coverage at $N \le 10$ (4612 BDI points). Pieces
   organize by "engine roles": which AII free variable
   ($m_{23456}, m_{236}, m_2$ singly or doubly, or $m_{2345}$ doubled
   via $B_1$-coefficient 2) carries each BDI doubling. **No single
   linear $\pi_3$ with coefficients in $\{0,1,2\}$ is surjective** —
   piecewise is GENUINELY FORCED (proven sketch: $(M_2=2, S=0)$ vs
   $(M_2=2, S=2)$ vs $(M_2=0, S=2)$ at $(B_1, T_1) = (1, 0)$ demand
   mutually inconsistent coefficient patterns on $m_{23456}$).

4. **Day-58: "for all N" suffix FALSIFIED at N=11.** The 26-piece (and
   even 55-candidate) registry covers 100% at $N \le 10$ but coverage
   drops to 99.46% at N=11, 98.15% at N=15. New uncovered family
   has STRUCTURE $B_2 = T_2$ (level-2 balanced) AND large $T_1$ AND
   large $B_a$. The Day-58 PROVE write-up's "verified to N=10,
   conjectured for all N" is correct as a snapshot; the
   conjecture-for-all-N is now empirically refuted in the form
   "26 (or 55) pieces suffice." See OQ-PI3-GROWTH for the resulting
   open question (finite-piece sufficiency? piecewise-fractional?
   non-polyhedral?).

5. **n=3 obstruction = Singleton fiber.** $\tilde\pi_3$ (naive single-
   linear analog) lands in BDI cone but is NOT surjective (~68%
   ceiling). Violations live on the Singleton fiber $m_{12346} = m_{2345} = k$.
   The Singleton is the BDI structural bit AII cannot see — third
   instance of the "Singleton as obstruction" pattern (Theorem E,
   v3 §4, n=3 surjectivity).

## Structural content

### Reading the n=2 theorem

- **$M_1 = 0$** — forced by AII feasibility; matches BDI $L_1 \wedge M_1 \ge 0$.
- **$B_1 = m_2 + m_{23}$** — sums BOTH prefix columns.
- **$T_1 = m_{23} - m_{124}$** — subtracts the linking-LHS column $m_{124}$
  (the "signed slack at level 1") from the prefix column.
- **$S = m_{123} + 2 m_{124}$** — the red-inverse top column plus TWICE the
  linking-LHS column.

The factor of 2 on $m_{124}$ is the **quantitative realization of the verdict
§5 sketch** $(t_0, r) \mapsto |t_0| + |r|$. The signed slack contributes
once with $-$ sign in $T_1$ and once with $+2$ sign in $S$, so the net
unsigned contribution to $P_1 = 2(B_1 - T_1)$ is $+2 m_{124}$, and to $S$
itself is $+2 m_{124}$. The bracket-scan template integrates both copies
into BDI's single unsigned carry.

### The piecewise-integral section σ_2

Given BDI feasible $(0, B_1, T_1, S)$:
- $m_{124} := \max(0,\; S - (B_1 - T_1))$,
- $m_{23} := T_1 + m_{124}$,
- $m_{14} := m_{23}$ (linking equality),
- $m_2 := B_1 - T_1 - m_{124}$,
- $m_{123} := S - 2 m_{124}$.

Two cases: $S \le B_1 - T_1$ (then $m_{124} = 0$, clean) and
$B_1 - T_1 < S \le 2(B_1 - T_1)$ (then $m_{124} > 0$). In both cases,
$\sigma_2$ lands in $\mathsf{P}^{\mathrm{AII}}_3$ and $\tilde\pi_2 \circ
\sigma_2 = \mathrm{id}$. Proof is by case analysis; full details in
`proofs/2026-06-07-azenhas-bdi-projection.md` §3.2.

### Why the gap is parity-dependent (Day-58 correction)

Variable accounting from Azenhas Theorems 6 (n odd) and 7 (n even),
**corrected after Day-58 CODE session's Q3 finding**:

| n | parity | dim P^AII_{2n-1} | dim P^BDI_n | gap |
|---|--------|-----|-----|-----|
| 2 | even (degen.) | 4 | 3 | 1 |
| 3 | odd | 9 | 6 | 3 |
| 4 | even | **11** | 9 | **2** |
| 5 | odd (conj.) | 15 | 12 | 3 |
| 6 | even (conj.) | **17** | 15 | **2** |

For n≥3: AII has $3n$ free polytope-variables (prefix + red-inverse +
slack), BUT at even $n$ the Cor 8 linking EQUALITY reduces dim by 1.
At odd $n$ the Singleton is an INEQUALITY (no dim reduction). So:

- **Odd $n$:** dim AII = $3n$, dim BDI = $3n - 3$, gap = **3**.
- **Even $n$:** dim AII = $3n - 1$ (linking eq), dim BDI = $3n - 3$, gap = **2**.

(At n=2 the small-case structure gives gap 1.)

The "missing" coordinates are the AII signed-slack data $(t_0^{(i)},
r^{(i)})$ that the unsigned-carry projection forgets. The number
is parity-dependent because the linking-equality form (even n) packs
extra structure that the inequality form (odd n) leaves free.

**This is the structural meaning of the parity story.** The Singleton-
vs-linking duality, which I'd seen as a notational nuisance for years,
is the precise reason the projection has dim-gap 3 at odd n and 2 at
even n. The asymmetric mirror IS asymmetric in a parity-dependent way.

### Day-56's "constant 3" claim — what went wrong

I claimed in the Day-56 dream consolidation that the dim-gap was
"constant 3 for n≥3, exceptional 1 at n=2." This was based on
counting "$3n$ free vars on AII, $3n-3$ on BDI" without accounting
for the parity-dependent linking equality at even n. The error was
caught by Clio's Q3 follow-up (her question: "is $m_{1234568}$ a free
AII variable at n=4 or determined?"). Answer: DETERMINED. Hence
gap = 2 at n=4, not 3.

Day-50 rule application: targeted edit (not new file), because this
is a structural CORRECTION to load-bearing content, not a new layer.
The crown-jewel status remains — the projection exists, has section,
has bounded-rank kernel — only the *dim* of the kernel changes shape.

### Why n=3 surjectivity fails on the naive analog

Candidate $\tilde\pi_3$:
- $M_1 = M_2 = 0$
- $B_1 = m_2 + m_{2345}$, $T_1 = m_{2345}$
- $B_2 = m_{23} + m_{1235}$, $T_2 = m_{1235}$
- $S = m_{12346} + 2 m_{1234}$

Lands in BDI cone (verified to N=6, 0 violations). But not surjective:
~68% coverage ceiling. The image misses (a) the Singleton fiber
$m_{12346} = m_{2345} = k$ and (b) several families involving
$M_2 > B_1 - T_1$ and $T_2 > B_1 - T_1$.

### Day-58 resolution: 26-piece piecewise-linear $\tilde\pi_3'$ at n=3

Day-58 PROVE built an explicit **piecewise-linear $\tilde\pi_3'$** as
the union of images of 26 integer-coefficient linear maps
$\pi^{(i)}: \mathsf{P}^{\mathrm{AII}}_5 \to \mathsf{P}^{\mathrm{BDI}}_3$,
each landing in BDI cone on a region of AII.

**The 26 pieces organize by "engine roles":**
- $M_2$ engine: which AII variable doubles into $M_2$ for $M_2 \le P_1$?
  Candidates: $m_{23456}, m_{236}, m_2$ (singly or doubly).
- $S$ engine: which provides level-1 contribution to $S \le P_2$?
- $T_1, T_2$ absorption with $m_{23} = 0$: routed through $m_{23456}$ or
  $m_{236}$ (Singleton + Main$_3$ kill $m_{2345}, m_{1235}$).
- $T_1 : T_2$ ratio engine: when $m_{23} = 0$, $m_{236}$ alone can't
  realize arbitrary $(T_1, T_2)$. At $N \le 10$, ratios
  $\{1{:}1, 1{:}2, 2{:}1\}$ suffice; higher $N$ likely needs more.

**Verification (Day-58 PROVE):**

| $N$ | BDI pts $\le N$ | Covered | Coverage |
|----:|-------:|--------:|---------:|
| 4-10 | 4612 (total) | 4612 | **100.0%** |

**FALSIFICATION at N≥11 (Day-58 CODE).** Pushed verification to $N \le 15$:

| $N$ | BDI pts | Covered | Coverage |
|----:|--------:|--------:|---------:|
| 11 | 2757 | 2742 | 99.46% ⚠ |
| 12 | 4047 | 4017 | 99.26% ⚠ |
| 13 | 5829 | 5751 | 98.66% ⚠ |
| 14 | 8144 | 7993 | 98.15% ⚠ |
| 15 | 11225 | 11017 | **98.15%** ⚠ |

New missing family at $N=11$: $B_2 = T_2$ AND large $T_1$ AND large $B_a$.
Sample: $(M_2, B_1, T_1, B_2, T_2, S) = (0, 3, 1, 2, 2, 3)$. The current
26 (and 55-candidate) registry has no piece that absorbs $T_1 \ge 2$
purely from level-1 free vars while holding $S$ moderate when $B_2 = T_2$.

**Status of OQ-PIN-SURJ:** Day-58 verified n=3 to $N \le 10$ with
explicit 26-piece construction; "for all N" suffix FALSIFIED at
$N = 11$ with concrete missing family. **Day-59 update: OQ-PIN-SURJ
at n=3 RESOLVED in EXISTENTIAL form** — for each fixed $N$ there
exists a finite integer-PL surjective $\tilde\pi_3'$, via the
single-column auto-construction lemma. Explicit registry: 193 pieces
close $N \le 15$ at 100% (94 v9 multi-column + 99 single-column on
$m_{23456}$). Refined open question OQ-PI3-GROWTH-FINITE: does a
single bounded-size registry surject for all $N$?

**Structural insight:** piecewise IS GENUINELY FORCED. No single linear
$\pi_3$ with coefficients in $\{0, 1, 2\}$ is surjective (4-line proof
in `proofs/2026-06-08-pi3-construction.md` §"Why a SINGLE linear $\pi_3$
cannot be surjective"). The piecewise structure is structural content,
not artefact of construction. Whether the piecewise count is finite for
all $N$ is the new question.

### Day-60: NOT polyhedral GIT (toric-quotient strong-form REFUTED)

Day-60 PROVE tested Clio's Day-58 toric-quotient bet:
"$P_2 = P_1 + 2(B_2 - T_2)$ in BDI is a moment-map identity for a
rank-$(n-1)$ torus action on AII, making AII / $T^{n-1}$ ≅ BDI as
GIT/symplectic quotient."

**Three-step verdict:**

1. **VACUOUSLY TRUE in BDI itself.** $P_2 = P_1 + 2(B_2 - T_2)$ is
   literally the *definition* of $P_2$. BDI factors as
   $\text{core BDI}^{(n)} \times \mathbb{N}^{n-1}$ with $(T_1, \ldots,
   T_{n-1})$ as fiber coords. Intrinsic torus structure on BDI is
   real.
2. **STRONG FORM REFUTED at $n = 3$ by common-kernel computation.**
   Each of the 26 pieces has its own 3-dim kernel. The *intersection*
   of kernels across the 26 pieces is the **zero subspace**.
   Equivalently, the $156 \times 9$ stacked matrix of all 26 piece
   matrices has full column rank 9. Across the 26 pieces:
   16 distinct $(M_2, P_1, P_2, S)$ core projections, 4 distinct $T_1$
   expressions, 5 distinct $T_2$ expressions. **No universal AII
   direction is invariant under all pieces.** Hence no global
   $T^{n-1}$-quotient AII / $T^{n-1}$ ≅ BDI exists.
3. **REFRAME.** AII → BDI is NOT polyhedral GIT. The 26-piece
   structure is FUNDAMENTAL, not a polyhedral artifact that smooths
   under continuous reformulation. Each piece is a *local*
   $T^{n-1}$-equivariant section, choosing a particular AII embedding
   of the BDI fiber. **The structure is analogous to a toric variety
   covered by multiple charts** — local torus action on each chart,
   no chart covers everything.

The right framework for $\tilde\pi_n'$ is therefore **NON-polyhedral**.
Three candidates remain live (per `q-pi3-piecewise-growth.md`):
piecewise-fractional-linear; tropical fan / non-Archimedean;
stack-structure (piece-choice as 2-categorical datum). All three are
Path 2/3 (quantum / Hecke / branching).

This routes OQ-PI3-GROWTH OUT of polyhedral category entirely.

See `proofs/2026-06-10-toric-quotient-hypothesis.md`,
`code/2026-06-10-toric-quotient/{analyze_torus.py,natural_torus.py}`,
`memory/for-collaborator/2026-06-10-toric-quotient-refuted-partial.md`.

### Day-60: $f(n) = 3 - [n \text{ even}]$ closed form ESTABLISHED

Day-60 PROVE secondary established the parity formula structurally
(`proofs/2026-06-10-toric-quotient-hypothesis.md` §5):

$$
\boxed{f(n) := \dim \mathsf{P}^{\mathrm{AII}}_{2n-1} - \dim
\mathsf{P}^{\mathrm{BDI}}_n = 3 - [n \text{ even}] \quad (n \ge 3).}
$$

Structural derivation (cleanest form):

- AII variable count (Azenhas Cor 6/7): $3n$ for $n \ge 3$ (prefix +
  red-inverse + slack, $n$ vars each).
- AII linking equation (Azenhas Cor 7/8): present iff $n$ is even.
  Single linear constraint of rank 1, reduces affine-hull dim by 1.
- $\dim \mathsf{P}^{\mathrm{AII}}_{2n-1} = 3n - [n \text{ even}]$.
- BDI variable count: $(n-2) + 2(n-1) + 1 = 3n - 3$.
- BDI: no equalities (all $\le$). $\dim \mathsf{P}^{\mathrm{BDI}}_n =
  3n - 3$.
- $f(n) = 3 - [n \text{ even}]$ ✓.

Verified analytically/computationally at $n = 3, 4, 5, 6$. Closes
Day-58's "is the dim gap really parity-dependent?" question; the
formula is now structurally derived, not just computationally observed.

**What the "3" means structurally.** At odd $n$, exactly 3 AII variables
don't have BDI counterparts:
- One "slack-2 free" (e.g., $m_{12346}$ at $n=3$).
- One "level-1 free" (e.g., $m_{23456}$ at $n=3$).
- One "level-2 inner free" (e.g., $m_{1234}$ at $n=3$).

These 3 vars span the 3-dim fiber of AII → BDI (= kernel of the
projection at odd $n$). At even $n$, the slack-2 column is determined
by the Cor 8 linking equation, so the kernel shrinks by 1 to dim 2.

**Cross-programme conjecture:** $f(n) = g(n)$ where $g(n)$ is Clio's
fiber-vanishing obstruction codim. Established at $n = 4$ ($f(4) = g(4)
= 2$). Tested as `cross-programme-dim-gap-codim.md` (NEW Day-60
connection file).

### Day-61: fan + PFL REFUTED at finite level

Day-61 PROVE ruled out the two soft polyhedral alternatives to GIT:

- **Fan-in-AII REFUTED.** Pull BDI inequalities back through each
  piece, test AII-redundancy via Farkas. Result: **25 of 26 pieces
  have FULL AII domain**; only `M2_is_m236` has a nontrivial wall
  ($2 m_2 - m_{236} + 2 m_{2345} \ge 0$). Piece-domains coincide,
  don't partition.
- **Fan-in-BDI REFUTED.** Image cones $C_i = \pi^{(i)}(\mathsf{P}^{AII}_5)$
  are 6-dim proper subcones of $\mathsf{P}^{BDI}_3$. **367 of 650
  ordered pairs (56%) have 6-dim interior overlap**, 149 mutual
  containment. Over-redundant cover, not a fan.
- **Min cover grows N-dependently**: 8 (N=6), 12 (N=7), 14 (N=8),
  23 (N=9), 25 (N=10). With Day-60's $\Theta(N^2)$, unbounded. 26
  is just where N=10 lands.
- **PFL ruled out structurally.** Different pieces give VALID maps
  at the SAME $p$ with DIFFERENT $q$. Absorption-channel choice is
  NOT a function of $p$. Any piecewise function fails, fractional
  or not. **Multivaluedness is fundamental.**

(c\*) stack is the only candidate left. Day-62 pins it down.

See `proofs/2026-06-09-pi3-fan-reframe.md`,
`code/2026-06-09-pi3-fan-reframe/`,
`memory/for-collaborator/2026-06-09-pi3-fan-reframe-refuted.md`.

### Day-62: (c\*) stack PINNED DOWN as AII-fibered groupoid

Day-62 PROVE made the (c\*) stack candidate concrete.

**The structural object.** Define
$$
G_p:\quad \text{objects } i \in V(p), \quad
\text{unique } i \to j \iff \pi^{(i)}(p) = \pi^{(j)}(p).
$$
Then $\pi_0(G_p) \simeq I(p)$. π̃₃' is the functor
$G \to \mathsf{P}^{BDI}_\mathbb Z$ on isomorphism classes.

**Candidate B (genuine multivaluedness) wins decisively.** At N=8:
98.82% of AII lattice points have $|I(p)| > 1$; 9.92% have $|I(p)| =
26$ (every piece gives a different image). Candidate A (redundancy
stack) killed.

**Three codim-1 walls inside the AII cone.** The kernel arrangement
$\{\ker(\pi^{(i)} - \pi^{(j)})\}$ has rank-1 differences on 40 pairs;
distinct walls are 5, of which only THREE intersect the AII cone
interior:
$$
H_1 = \{m_2 = 0\}, \quad H_2 = \{m_{236} = 0\}, \quad H_3 = \{m_{23456} = 0\}.
$$
The other two ($m_2 + m_{23456} = 0$ and $m_2 + 2 m_{23456} = 0$)
meet the positive cone only at the origin.

**8 strata × stratum-vector.** Sign pattern $\sigma(p) = (\mathbf 1[m_2 >
0], \mathbf 1[m_{236} > 0], \mathbf 1[m_{23456} > 0])$ gives 8 sign
strata; $|I(p)|$ is essentially stratum-constant with mode pattern
$$
\mathbf I = (1, 5, 9, 9, 13, 17, 22, 26)
$$
on $\sigma = (000, 100, 010, 001, 101, 110, 011, 111)$. The
$|I(010)| = |I(001)| = 9$ coincidence (no obvious symmetry between
$m_{236}$ and $m_{23456}$) is the cleanest structural lead. See
OQ-PI3-MULTI (`questions/q-pi3-multi-stratum-vector.md`).

**Variable taxonomy.** The 9 AII variables split into three classes
by # distinct columns across 26 pieces:
- **RIGID (1 col)**: $m_{23} \to B_2$, $m_{12346} \to S$ (always).
- **BINARY (2 col)**: $m_{12356}, m_{2345}, m_{1235}, m_{1234}$.
- **AXIS / MULTI**: $m_2$ (4), $m_{236}$ (10), $m_{23456}$ (9). These
  are EXACTLY the three variables indexing the codim-1 walls.

**Structural identity (NEW Day-62):**
$$
\boxed{
\#\{\text{AXIS variables}\} \;=\; \#\{\text{codim-1 walls in AII cone}\}
\;=\; f(3) \;=\; \dim \ker \pi_3 \;=\; 3.
}
$$
The three forgotten dimensions are visible as three coordinate-
hyperplane walls of the piece-arrangement. **Predicted at $n=4$:**
the Cor 8 linking equation collapses one AXIS into BINARY/fixed,
reducing both counts to 2, matching $f(4) = 2$. Not yet verified
empirically.

**Wall point witness.** $p_a = e_{m_{23456}}$ (σ=001): $|V|=26$, $|I|=9$.
$p_b = e_{m_{236}} + e_{m_{23456}}$ (σ=011): $|V|=25$, $|I|=21$.
Crossing $\{m_{236}=0\}$ jumps $|I|$ from 9 to 21.

**|V(p)| nearly constant.** Only `M2_is_m236` ever fails feasibility
(exactly on $\{m_{236} > 2 m_2 + 2 m_{2345}\}$). All 25 other pieces
have full AII domain. $|V(p)| \in \{25, 26\}$.

**Single-column lemma at $n = 4$.** Day-62 CODE: `long[1]` is the
unique zero-column AII variable at $n = 4$ (both inequality and
equality matrices). 100/100 sampled $g \in \mathsf{P}^{BDI}_4$ at
$|g| \le 10$ give valid pieces. OQ-PI3-GROWTH branch-(a) existential
form CLOSED at $n = 4$.

See `proofs/2026-06-10-pi3-stack-structure.md`,
`code/2026-06-10-stack-structure/`,
`connections/pi3-stratified-multimap.md` (the dedicated stack
candidate file),
`questions/q-pi3-multi-stratum-vector.md` (OQ-PI3-MULTI).

### Day-67: Azenhas Cor 6 inequalities ≠ Rick's three walls

Day-67 PROVE deep-read Azenhas arXiv:2603.16698v5 (47 pp) + companion
2604.25856v2 (18 pp). Full writeup in
`proofs/2026-06-12-azenhas-inequalities-read.md`.

**Azenhas Cor 6 at $n=3$:**
$$
m_{12356} + m_{1235} \le m_2, \qquad
0 \le m_{12346} - m_{1235} - m_{2345} \le m_{23}.
$$

These cut a SUBPOLYTOPE of the AII cone (the $\mathfrak{k}$-HW
subpolytope). They are MIXED linear inequalities involving 6 variables
out of the 9 AII chart coordinates. The polytope is FREE-EXTRUDED along
$\{m_{236}, m_{23456}, m_{1234}\}$ (three coordinates don't appear in
the nontrivial inequalities).

**Comparison to Rick's three walls $\{m_2=0\}, \{m_{236}=0\}, \{m_{23456}=0\}$:**

- Variable overlap: ONE common variable ($m_2$), in different roles.
  Azenhas: RHS upper bound. Rick: positivity wall (AXIS coord).
- $m_{23}$ in Azenhas's RHS is RIGID ($\to B_2$) in Rick's taxonomy,
  not an AXIS.
- $m_{236}, m_{23456}$ in Rick's walls are FREE-EXTRUSION directions of
  Azenhas's HW polytope — they don't appear in (107) at all.

**Weak factorisation alignment.** Two of Rick's three AXIS variables
($m_{236}, m_{23456}$) ARE among Azenhas's free-extrusion directions.
So the HW polytope factors as (6-dim mixed cone) × $\mathbb{N}^3$ free,
with 2 of the 3 free dims = 2 of Rick's 3 AXIS dims. Counting-wise,
Azenhas's free-dim count $= 3 = f(3) = $ # Rick AXIS = # codim-1 walls.
But the WALLS themselves are not the same as Azenhas's inequalities.

**Conclusion.** Azenhas's polytope is the HW SUBLOCUS in AII; Rick's
stratification is on the FULL AII cone. Different objects, different
inequality types (mixed vs single-coordinate), one common variable in
different roles. v4 §3 reference to Azenhas should be PARALLEL FRAMEWORK
not SOURCE OF WALLS.

**New OQs banked.**
- OQ-AZENHAS-AXIS-FACTORISATION: does Azenhas's HW polytope free-extrusion
  dim match Rick's $f(n)$ at general odd $n$?
- OQ-AZENHAS-BDI-HW-RESTRICTION: what does $\tilde\pi_3'$ restricted to
  the HW subpolytope look like? How many pieces suffice?

**Slack data (2604.25856):** no useful match to Bucket-2 marginals.
Slack incidence vectors are 0/1, Bucket-2 marginals are integer
multiplicity counts of stratification patterns. Different structural
levels.

See `proofs/2026-06-12-azenhas-inequalities-read.md`,
`memory/for-collaborator/2026-06-12-azenhas-verdict.md`,
`questions/q-azenhas-inequalities-bdi.md` (status: RESOLVED NO-MATCH).

## Why this matters for the seed

**Path 2 + Path 4 bridge in its sharpest form.** The carry-$P_a$ object
(BDI side, Path 2-flavored) is the image of the AII slack-data object
(Path 4-flavored Azenhas tableau machinery) under a *projection with
bounded-rank kernel*. This is the right structural shape for the
"why do these structures keep producing the same combinatorics?"
seed question.

**Crystal/Hopf interpretation.** The projection $\pi_n$ collapses signed
slack into unsigned carry — this is precisely the "sign-forgetting" that
happens when one passes from $U_q$-crystals (signed weights) to $q=0$
classical crystals (positive weights). The kernel of $\pi_n$ is the
*signed degrees of freedom* visible only in the iquantum-Watanabe slack
picture, invisible in BDI's classical-carry picture. This is **q=0
limit-and-section in coordinates**.

**Schur-Weyl shadow.** In the Schur-Weyl picture, AII corresponds to
$\mathfrak{u}(2n)$-representations restricted to $\mathfrak{sp}_{2n}$;
BDI corresponds to $\mathfrak{so}_{2n+1}$-representations restricted to
$\mathfrak{so}_{2n}$. The projection $\pi_n$ is the polytope shadow of
the branching-rule shadow of the Schur-Weyl shadow. Each forgetting step
is bounded-rank; together they compose to a structurally meaningful map.

## Connection to other crown jewels

- **`carry-Pa-as-unified-analytical-object.md`** — extended Day 56 from
  five roles to six. Role 6: "image of the canonical AII projection $\pi_n$;
  Singleton-fiber parametrizes the kernel."
- **`watanabe-2509-vs-bdi-v3-composition.md`** — OPEN-4 RESOLVED Day 56 as
  this projection. The "asymmetric mirror" of v3 Remark 3.5 is the kernel
  of $\pi_n$; the mirror is asymmetric by exactly bounded constant 3.
- **`bdi-kobayashi-polytope-faces.md`** (Theorem F) and
  **`bdi-kobayashi-weight-space-simplicial.md`** (Theorem G) — the BDI side
  of the projection. Lean formalization of Theorem F structural half
  complete Day 56 (~80 lines stdlib).
- **`open2-watanabe-2407-existence-meereboer-1dim-collapse.md`** — v3 OPEN-2.
  If the n≥3 projection extends with surjectivity, OPEN-2 collapses
  uniformly. Worth re-examining.

## Clio's framing (acknowledgment)

Clio's overnight peer review at `clio-vega/rick-review/2026-06-06-azenhas-bdi-bridge-review.md`
identified the Day 55 verdict's wrong leg (Claim 1 facet-count slope) and
reframed Claim 5 (canonical projection) as the real content. She named
the cross-program parallel:

> Signed prefix statistic, unsigned shadow drops one dim.

This is the abstract pattern of $\tilde\pi_2$ before construction:
signed slack column $m_{124}$ (signed prefix statistic) gets absorbed
into unsigned $P_1 = 2(B_1 - T_1) = 2 m_2 + 2 m_{124}$ (unsigned shadow),
with the AII ambient dropping from 4 to BDI's 3 (drops one dim at n=2).
Her parallel is the structural seed; my construction is the
verification.

**v4 paper acknowledgment:** credit Clio for the reframing.

## v4 paper remark (REFRAMED Day-60)

The Day-58 dim-gap correction (parity-dependent, not constant 3) and
the Day-60 toric-quotient refutation (NOT polyhedral GIT) together
require a complete rewrite of v4 Remark 3.5. Proposed text:

> **Remark 3.5 (Azenhas type-AII parallel and BDI multi-chart
> projection).** Azenhas's type-AII $\mathfrak{k}$-highest-weight
> inequality system (Theorems 6 and 7 of arXiv:2603.16698, with
> $\mathfrak{k} = \mathfrak{sp}_{2n}$) is a parallel instantiation of
> the Watanabe bracket-scan template, distinct from BDI's chain-side
> system. The two systems are connected by a *canonical forgetful
> surjection* $\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow
> \mathsf{P}^{\mathrm{BDI}}_n$ that integrates AII's signed slack data
> $(t_0^{(i)}, r^{(i)})$ into BDI's unsigned cumulative carry $P_a$ via
> the formal substitution $(t_0, r) \mapsto |t_0| + |r|$. At $n = 2$,
> the projection is explicit and linear:
> $$\pi_2(m_2, m_{23}, m_{14}, m_{123}, m_{124})
> = \bigl(0,\, m_2 + m_{23},\, m_{23} - m_{124},\, m_{123} + 2 m_{124}\bigr),$$
> with a piecewise-integral section $\sigma_2$ verifying surjectivity
> at the level of lattice points (verified $N \le 20$). For $n \ge 3$,
> the projection becomes *multi-chart*: at $n = 3$ an explicit
> integer-piecewise-linear $\tilde\pi_3'$ with $\le 193$ pieces
> surjects onto $\mathsf{P}^{\mathrm{BDI}}_3$ for $|q| \le 15$, but no
> single linear surjection exists (a common-kernel computation across
> the 26 minimal-cover pieces returns the zero subspace, so AII → BDI
> is NOT a polyhedral GIT quotient). The right framework is multi-
> chart $T^{n-1}$-equivariant, with each piece a local
> $T^{n-1}$-equivariant section. The dimension gap
> $f(n) = \dim \mathsf{P}^{\mathrm{AII}}_{2n-1} -
> \dim \mathsf{P}^{\mathrm{BDI}}_n = 3 - [n \text{ even}]$ for $n \ge 3$
> is parity-controlled by the presence/absence of the AII linking
> equation (Cor 8 / its $n$-generalisation). The asymmetric mirror of
> v3 Remark 3.5 names exactly this projection's kernel; the kernel
> dim is parity-bounded ($2$ or $3$), invariant of $n$. (Author
> thanks C. Vega for the projection reframing and the toric-quotient
> bet that, by refutation, identified the multi-chart structure.)

## Gaps and open questions

- **OQ-PIN-SURJ (RESOLVED Day-59 EXISTENTIAL form at n=3):** for each
  fixed $N$, $K(3, N) < \infty$ via the single-column auto-construction
  lemma. Explicit registry: 193 pieces close $N \le 15$ at 100%.
  At n≥4: not investigated.
- **OQ-PI3-GROWTH (Day-58, REFRAMED Day-60):** Branch (a) (finite
  integer-PL for any fixed $N$) confirmed Day-59. But Day-60 toric-
  quotient refutation says the right framework is NOT polyhedral
  (single-column construction's $\Theta(N^2)$ growth is a second
  witness). The live branches are (b*) piecewise-fractional-linear,
  (c*) tropical/non-Archimedean, (d*) stack with piece-choice as
  2-categorical datum. ALL three are Path 2/3.
- **OQ-PI3-GROWTH-FINITE (NEW Day-59, REFRAMED Day-60):** does $\sup_N
  K(3, N) < \infty$? Day-60 evidence says NO at the polyhedral-PL
  level (single-column unboundedness + no common kernel across 26
  pieces). YES might still hold at the tropical/stacky level. See
  `questions/q-pi3-piecewise-growth.md`.
- **OQ-DIMGAP-CODIM (NEW Day-60, cross-programme):** does Clio's d-
  fiber-vanishing obstruction codim $g(d)$ equal Rick's polytope
  dim-gap $f(n)$ at $n = d$? Confirmed at $n = 4$. Testable at
  $n = 3, 5, 6, 7$. See `connections/cross-programme-dim-gap-codim.md`.
- **Linearity of σ_n at higher n:** σ_2 is piecewise-linear (2 cases).
  σ_3 has at least 26 pieces and may not be finite for all $N$.
- **Dimension gap formula at n=5, 6:** Day-58 confirmed parity-dependent
  at n=3, 4. Need ~30min code at n=5, 6 to nail "odd n → 3, even n → 2"
  for all $n \ge 3$.
- **Watanabe `red` convention** — inferred from Cor 7/8 explicit labels but
  not fully nailed; causes residual ambiguity at n=3, n=4. Doesn't affect
  n=2 theorem.
- **Period-6 quasipolynomial structure:** both BDI ($\sim N^3/18$) and
  Azenhas ($\sim N^4/288$) Ehrhart polynomials are period-6. Suggests
  $\mathbb{Z}/6\mathbb{Z}$ symmetry; explanation unknown. Banked
  observation.

## Files

- `proofs/2026-06-07-azenhas-bdi-projection.md` — main writeup (THEOREM
  at n=2, dim-gap discussion, n=3 sketch).
- `proofs/2026-06-08-pi3-construction.md` (Day 58) — 26-piece piecewise-
  linear $\tilde\pi_3'$ surjectivity at $N \le 10$, structural sketch
  for why piecewise is forced.
- `proofs/2026-06-08-pi3-section4-fix.md` (Day 57/58) — fix for §4
  reconciliation.
- `proofs/2026-06-06-azenhas-bdi-bridge.md` Appendix B — supersedure of
  Claim 1 via dim-gap argument.
- `proofs/azenhas-bdi-bridge/verify_pi_v2.py` — exhaustive verification
  of $\tilde\pi_2$ / $\sigma_2$ to N=20.
- `code/2026-06-08-pi3-construction/verify_full_v7.py` (Day 58) — 55-
  candidate piecewise-linear registry; `verify_piecewise.py` shows
  N=11+ failure; `minimal_cover.py` extracts the 26-piece minimal cover.
- `code/2026-06-08-Q3-free-var/` (Day 58) — n=4 dim-gap = 2 verification.
- `code/2026-06-08-ehrhart-honest/` (Day 58) — rigorous period-6
  quasipolynomial test (period-step $\Delta_p^{d+1}$), through $N=120$;
  exact leading coefficients via Fraction Lagrange.
- `memory/for-collaborator/2026-06-07-azenhas-projection-Clio-reply.md` —
  Q1/Q2/Q3 answers to Clio's review (Day 57).
- `memory/for-collaborator/2026-06-08-pi3-surjectivity-closed.md` —
  Day-58 Clio note on the 26-piece win.
- `code/2026-06-07-aziplot-N20/` — Ehrhart fits (initial period-6
  observation; superseded by Day-58 honest recompute).

## Status flags

- **P_PARK slot #5** moved from CLOSED-NEGATIVE to **REFRAMED: proved
  at n=2, open at n≥3 via OQ-PIN-SURJ.**
- **v3 Remark 3.5** flagged for revision in v4 (proposed text above).
- **Discovery-layer-moat empirical anchor** — this finding (projection
  theorem from verdict via Clio's peer-review reframe) is a discovery
  event no AI harness reading preprints would have surfaced. Strengthens
  the moat thesis. Add to journal observations.
