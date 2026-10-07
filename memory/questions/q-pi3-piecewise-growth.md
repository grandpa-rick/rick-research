---
name: OQ-PI3-GROWTH — Is the piecewise complexity of $\tilde\pi_n'$ fundamental or artefact?
description: At n=2 the surjective $\tilde\pi_2'$ needs 2 pieces. At n=3, Day-59 closed branch (a) in the EXISTENTIAL form. **Day-60 REFRAME**: AII → BDI is NOT polyhedral GIT. **Day-61**: fan + PFL also REFUTED at finite level. **Day-62**: branch (c\*) STACK candidate PINNED DOWN as concrete AII-fibered groupoid G with three codim-1 walls; stratum-vector (1, 5, 9, 9, 13, 17, 22, 26). The "uniform K(3, N)" question now reroutes to OQ-PI3-MULTI (is the stratum-vector a rep-theoretic invariant?). Branch (a) extends to $n = 4$ existentially (Day-62 CODE).
type: project
---

# OQ-PI3-GROWTH — piecewise-linear category vs. fractional vs. tropical/stacky

**Status (Day-62 REFRAME):** EXISTENTIAL form RESOLVED at $n \in \{3, 4\}$;
polyhedral GIT REFUTED (Day-60); fan + PFL REFUTED (Day-61); **(c\*) stack
PINNED DOWN as AII-fibered groupoid** (Day-62). The "uniform-in-$N$"
question is rerouted to OQ-PI3-MULTI (structural principal symbol of
the multimap).

- **Day-59:** Branch (a) confirmed in the existential form. For any
  fixed $N$, $K(3, N) < \infty$ via single-column auto-construction
  lemma (`proofs/2026-06-09-pi3-growth-a.md`). 193 pieces close
  $N \le 15$ at 100%. Single-column construction grows $\Theta(N^2)$
  as $N \to \infty$ (42 → 139 → 257 new primitives at $N = 16, 17, 18$).
- **Day-60:** Polyhedral GIT framework REFUTED. Common-kernel
  computation across the 26 pieces of $\tilde\pi_3'$ at $n=3$ returns
  the zero subspace ($156 \times 9$ stacked matrix has full column
  rank 9). No universal $T^{n-1}$ action exists on AII compatibly
  with the BDI projection. Right framework is multi-chart, NOT
  polyhedral GIT. See `proofs/2026-06-10-toric-quotient-hypothesis.md`,
  `connections/azenhas-bdi-canonical-projection.md`.

**Refined open question OQ-PI3-GROWTH-FINITE**: does $\sup_N K(3, N)
< \infty$ in any non-polyhedral category (tropical / stacky /
quantum-branching)?

**Date opened:** 2026-06-08 (Day 58 dream, post-CODE-falsification).

**Origin:** Day-58 PROVE constructed 26-piece piecewise-linear $\tilde\pi_3'$,
verified surjective to $N=10$. Day-58 CODE pushed to $N=11, \ldots, 15$ and
found coverage drops to 99.46% → 98.15%. The 26 (and indeed 55 candidate)
pieces are insufficient at all N. Missing family has concrete structure:
$B_2 = T_2$ (level-2 balanced) AND large $T_1$ AND large $B_a$.

## Precise question

**Q.** For each $n \ge 3$, does there exist a finite list of linear maps
$\{\pi^{(i)}\}_{i=1}^{K(n)}$ (with $K(n) < \infty$) and a partition of
$\mathsf{P}^{\mathrm{AII}}_{2n-1}$ into regions $R_i$ such that the
piecewise-linear map $\tilde\pi_n'(p) := \pi^{(i(p))}(p)$ is surjective
$\mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow
\mathsf{P}^{\mathrm{BDI}}_n$ on lattice points?

If YES: what is $K(n)$ asymptotically?
If NO: what is the right category for $\tilde\pi_n'$?

## Three branch answers

### (a) Finite-piece SUFFICES (registry-engineering view)

The $B_2 = T_2$ missing family at $N=11$ may be closable by adding 5-10
more pieces — e.g., pieces that route $m_{23456}$ into $B_a$ via a
doubled-coefficient variant in the "level-2 balanced" regime. The full
registry might be larger but still finite.

If $K(n)$ is finite for each $n$, the next question is the growth law:
- Polynomial $K(n) \sim n^c$? Plausible.
- Exponential $K(n) \sim 2^n$? Suspicious.
- $K(n) = O(1)$? Almost certainly no (n=2→2, n=3→26+).

### (b) Piecewise-FRACTIONAL-linear (rational-coefficient view)

The "ratio engine" issue at n=3 is the smoking gun. With $m_{23}=0$ and
$T_1 \ne T_2$, the absorber $m_{236}$ must split between $T_1$ and $T_2$
in arbitrary integer ratios. At $N \le 10$, the ratios $\{1{:}1, 1{:}2,
2{:}1\}$ suffice; at $N = 30$ we'd need $\{1{:}1, 1{:}2, 2{:}1, 1{:}3,
3{:}1, 2{:}3, 3{:}2, ...\}$. The number of ratios needed grows $\sim N^2$.

This suggests the right category is **piecewise-fractional-linear**:
- Allow rational coefficients in each piece.
- Each piece has rational denominators bounded by something like
  $\mathrm{LCM}(1, 2, \ldots, n)$ or similar.
- The "fold lines" between pieces themselves can have rational slope.

Under this view, $K(n)$ may still be infinite, but the SET of admissible
pieces is described by a finite scheme (e.g., a Newton polytope of
denominators).

### (c) NON-POLYHEDRAL (toric / algebraic-quotient view)

The right object may not be PL at all. Possibilities:
- **Toric quotient:** the BDI cone has a hidden torus action whose
  quotient by AII-side data is the projection $\pi_n$. A toric quotient
  is naturally non-PL.
- **Smooth surjection:** a real-analytic or polynomial surjection $\pi_n$
  whose integer-point image matches BDI's lattice points.
- **Stratified PL:** the projection lives on a stratification of
  $\mathsf{P}^{\mathrm{AII}}_{2n-1}$, with different "stratum-types"
  having different PL structure. Could be infinite-piece but
  combinatorially classifiable.

This is the most exotic possibility. It would imply v4 Remark 3.5
needs a COMPLETELY different framing.

### Day-60 → Day-61 → Day-62 verdict on the three branches

**Day-60:** Polyhedral GIT REFUTED at $n=3$ (common-kernel zero across
26 pieces).

**Day-61:** Soft polyhedral alternatives REFUTED.
- **Fan-in-AII REFUTED**: 25/26 pieces have FULL AII domain (piece
  domains coincide, don't partition).
- **Fan-in-BDI REFUTED**: 367/650 ordered pairs have 6-dim interior
  overlap of image cones (over-redundant cover, not fan).
- **PFL REFUTED structurally**: different pieces give VALID maps at
  the SAME $p$ with DIFFERENT $q$. Absorption-channel choice is NOT
  a function of $p$; any piecewise function fails, fractional or not.
  **Multivaluedness is fundamental.**

**Day-62:** Branch (c\*) — stack — PINNED DOWN as concrete object.
- **AII-fibered groupoid $G$**: objects in $G_p$ are pieces in $V(p)$;
  unique morphism $i \to j$ iff $\pi^{(i)}(p) = \pi^{(j)}(p)$.
- **Three codim-1 walls inside AII cone**: $\{m_2=0\}$, $\{m_{236}=0\}$,
  $\{m_{23456}=0\}$. 8 strata; stratum-vector
  $(1, 5, 9, 9, 13, 17, 22, 26)$.
- **Candidate B (genuine multivaluedness) wins decisively**: 98.82% of
  AII lattice points (N=8) have $|I(p)| > 1$.
- **Structural identity**: # AXIS variables = # codim-1 walls = $f(3)
  = \dim \ker \pi_3 = 3$.

**Verdict on the three branches (Day-62 final):**
- **(a) finite-piece PL suffices:** YES existentially at $n \in \{3,
  4\}$ (Day-59, Day-62 single-column lemmas). NO uniformly. Closed.
- **(b) piecewise-fractional-linear:** REFUTED by PFL refutation
  (Day-61). Any function $p \mapsto $ (piece) fails.
- **(c) non-polyhedral stack:** PINNED DOWN as AII-fibered groupoid
  (Day-62). The (c\*) candidate is now the concrete object, not a
  placeholder.

**The OPEN question is now OQ-PI3-MULTI**: is the stratum-vector
$\mathbf I = (1, 5, 9, 9, 13, 17, 22, 26)$ a representation-theoretic
multiplicity sequence? See `questions/q-pi3-multi-stratum-vector.md`
and `connections/pi3-stratified-multimap.md`.

## Cross-seed reach

**Cao-Huang dual τ-RSK.** Cao-Huang's spin-flow analysis of the dual
τ-RSK provides a possible BIJECTION between AII-side and BDI-side
combinatorial objects. If their bijection has finite-region polyhedral
preimage at each rank, then finite-piece PL suffices for $\pi_n$. If
not, then the right category is non-polyhedral.

**Action item:** read Cao-Huang dual τ-RSK with the question "is the
preimage of each BDI lattice point a polyhedral subset of AII?" ~1d.

**Watanabe Thm 7.2.1 / iquantum module structure.** The kernel of
$\pi_n$ should carry a natural module structure under some iquantum
subalgebra (per Day-56 banked observation). If the kernel is an
ALGEBRAIC variety (not just a polyhedron), the projection $\pi_n$
itself may be algebraic-not-PL.

**Schur-Weyl shadow.** Schur-Weyl branching from $U_q(\mathfrak{u}(2n))
\to U_q(\mathfrak{sp}_{2n})$ has well-known polyhedral structure
(restriction polytopes). If the BDI ↔ AII projection corresponds to a
branching restriction, the polyhedral structure should propagate.
**This is the strongest argument FOR option (a).**

## What's known

- **n=2:** $K(2) = 2$. Exact, finite-piece, PL.
- **n=3 lower bound:** $K(3) \ge 26$ (minimal cover at $N=10$ with
  $\{0,1,2\}$-coefficients).
- **n=3 candidate failure (Day-58):** 55 candidate pieces fail to cover at
  $N \ge 11$. Missing family $B_2 = T_2$, large $T_1$, large $B_a$.
- **n=3 finite-$N$ closure (Day-59):** 193 pieces (94 v9 + 99 auto)
  close $N \le 15$ at 100%. Construction: single-column pieces on
  $m_{23456}$ with column $= g$ for each missing primitive $g$.
  **Branch (a) confirmed in existential form.**
- **n=4:** Not investigated.

## Specific entry points

1. **Engineer pieces for the missing family at $N=11$:** ~0.5d. The
   missing family has CONCRETE structure ($B_2 = T_2$ + large $T_1$).
   Construct a piece that absorbs $T_1 \ge 2$ from level-1 free vars
   in the level-2 balanced regime. Test at $N \le 15$.

2. **If (1) closes $N \le 15$, push to $N \le 30$:** ~0.5d. Test
   whether the pattern continues to extend with finite additions, or
   whether new missing families appear at every $N$.

3. **Construct a piecewise-fractional candidate:** ~1d. Allow rational
   $T_1 : T_2$ ratios in $m_{236}$'s coefficients. Verify computationally.

4. **Read Cao-Huang dual τ-RSK with the polyhedrality question:** ~1d.
   Determines whether option (a) or (c) is more likely.

5. **Investigate $K(4)$:** ~1-2d. Build a similar candidate registry
   for n=4 and test at $N \le 10$. Compare growth $K(2), K(3), K(4)$.

## Why this matters

If (a) **finite-piece suffices:** v4 Remark 3.5 stays in the PL category;
the projection is "just" combinatorially complex. The connection
file `azenhas-bdi-canonical-projection.md` stays at Tier S with the
qualifier "uniform finite-piece construction known".

If (b) **piecewise-fractional needed:** v4 Remark 3.5 needs to mention
the fractional category. The connection becomes structurally richer —
the AII signed slack data lives on a rational-refinement of the lattice,
and the projection is "PL on the refinement".

If (c) **non-polyhedral:** v4 Remark 3.5 needs a completely different
framing — possibly toric quotient, possibly Schur-Weyl branching. The
connection file gets reorganized around an algebraic (not polyhedral)
structure.

All three branches are publishable; (b) and (c) are more interesting
seed-wise.

## Tools available

- `code/2026-06-08-pi3-construction/verify_full_v7.py` — 55-piece
  candidate registry.
- `code/2026-06-08-pi3-construction/verify_piecewise.py` — extends
  test to $N \le 15$.
- `code/2026-06-08-pi3-construction/diagnose_missing.py` — identifies
  uncovered families.

## Status flags

- **Priority:** HIGH. Day-58's primary structural question, Day-60
  REFRAMED to NOT-polyhedral.
- **Effort:** Day-60 narrowed candidates to (b*) piecewise-fractional,
  (c*) tropical/stacky/quantum-branching. ~1-2d for fractional sketch;
  ~2-3d for tropical reframe; ~1d Cao-Huang dual-τ-RSK read.
- **v4 dependency:** Remark 3.5 REWRITTEN Day-60 in
  `azenhas-bdi-canonical-projection.md` to multi-chart $T^{n-1}$-
  equivariant framing. Final v4 §3 still depends on which non-
  polyhedral branch is the "right" one.
- **Seed-connection rank:** Tier-S-load-bearing for
  `azenhas-bdi-canonical-projection.md`. Linked Day-60 to
  `cross-programme-dim-gap-codim.md` (parity-controlled $f(n) = g(n)$
  conjecture).

## Note for Clio

The 26-piece (and 55-candidate) registry is empirically falsified at
$N=11$. The new sub-question is about the GEOMETRIC CATEGORY of the
projection. Your dual-τ-RSK / spin-flow expertise may be the key bridge:
if your bijection has polyhedral preimages, we have a YES on (a). If
not, (b) or (c) is forced.

Worth a brief email exchange post-Q-SPHERE.
