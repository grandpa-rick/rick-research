---
title: "Day 61: Fan reframe of $\\tilde\\pi_3'$ — both fan candidates REFUTED at finite level; the 26 pieces are NOT cells of any polyhedral subdivision"
author: Rick
date: 2026-06-09
status: |
  REFUTATION of fan-in-AII (25/26 pieces have FULL DOMAIN).
  REFUTATION of fan-in-BDI (367 6-dim interior overlaps).
  Minimal cover grows from 8 (N=6) to 25 (N=10) -> unbounded growth confirmed.
  The 26-piece structure is a TRUNCATION of an infinite family, not a fan.
  Path A (PFL) ruled out structurally: piece choice cannot be a function of p alone.
related:
  - proofs/2026-06-10-toric-quotient-hypothesis.md  (Day 60 verdict)
  - proofs/2026-06-08-pi3-construction.md  (Day 58 26-piece construction)
  - proofs/2026-06-09-pi3-growth-a.md  (single-column lemma, Day 59)
  - code/2026-06-09-pi3-fan-reframe/  (this analysis)
---

# Bottom line

PROVE.md asked: **can the 26 pieces of $\tilde\pi_3'$ be identified
with the maximal cones of a fan?**

Answer at $n=3$: **NO, on BOTH candidate fan locations.**

1. **Fan-in-AII REFUTED**: 25 of the 26 pieces have **full AII
   domain**.  Only one piece (`M2_is_m236`) imposes a nontrivial
   pullback constraint; the other 25 land in $\mathsf{P}^{BDI}_3$
   automatically on all of $\mathsf{P}^{AII}_5$.  So the piece-domains
   $D_i \subseteq \mathsf{P}^{AII}_5$ are NOT a polyhedral subdivision;
   they all coincide (or nearly so).
2. **Fan-in-BDI REFUTED**: the 26 image cones $C_i := \pi^{(i)}(\mathsf{P}^{AII}_5)$
   are all 6-dimensional and **all proper subcones** of $\mathsf{P}^{BDI}_3$.
   367 out of 650 ordered pairs (56%) have a 6-dim interior overlap,
   and 149 pairs have **mutual interior overlap**.  So the $C_i$ are
   NOT a fan; they're an over-redundant cover.
3. **The 26-piece count is N-dependent**:

   | $N$  | # BDI points | # essential pieces | greedy min cover |
   |------|------------:|------------------:|-----------------:|
   | 6    | 306         | 4                 | 8                |
   | 7    | 537         | 8                 | 12               |
   | 8    | 896         | 9                 | 14               |
   | 9    | 1434        | 21                | 23               |
   | 10   | 2216        | 24                | 25               |

   Combined with Day-60's $\Theta(N^2)$ growth at $N \ge 16$, the
   piece count is **unbounded**: 26 is not a structural constant, it
   is just where the cover happens to land at $N = 10$.

4. **Path A (piecewise-fractional-linear) ruled out structurally**.
   The 26 pieces differ in HOW they distribute AII variables across
   BDI coordinates (the "absorption channel" choice for $m_{236}$,
   $m_{23456}$ between $T_1, T_2, M_2, S$).  This choice is **not a
   function of $p \in \mathsf{P}^{AII}_5$** — different pieces give
   valid maps at the SAME $p$ with DIFFERENT BDI images.  Hence no
   piecewise function $p \mapsto $ (choice) can encode the structure,
   regardless of whether the pieces are linear, fractional-linear, or
   anything else.

**Verdict**: the right object for $\tilde\pi_3'$ is **multivalued by
nature**.  Neither (a*) PFL nor (b*) tropical fan in finite form is
adequate.  Candidate (c*) **stack** (or a similar 2-categorical /
groupoid structure where the piece choice is a 1-morphism and pieces
themselves are objects) is the structural ground truth.

# Detailed analysis

## §1. Setup

The Day-58 piecewise-linear $\tilde\pi_3' : \mathsf{P}^{AII}_5 \to
\mathsf{P}^{BDI}_3$ is a multivalued (but lattice-surjective) map
realized by 26 integer-linear pieces $\pi^{(i)}$, each a $6 \times 9$
matrix.  At a given AII point $p$, the user picks any $i$ for which
$\pi^{(i)}(p) \in \mathsf{P}^{BDI}_3$; multiple $i$ may work.

For a FAN structure, we need a polyhedral subdivision.  Two candidates:

- **Fan in AII (source)**: pieces partition $\mathsf{P}^{AII}_5$ into
  maximal cones $D_i$, with $\tilde\pi_3' |_{D_i} = \pi^{(i)}$.
- **Fan in BDI (target)**: image cones $C_i = \pi^{(i)}(\mathsf{P}^{AII}_5)$
  partition $\mathsf{P}^{BDI}_3$, with $\sigma_3 |_{C_i} = $ inverse of $\pi^{(i)}$.

Both candidates fail.

## §2. Fan-in-AII: REFUTED

For each piece $i$, define $D_i = \{p \in \mathsf{P}^{AII}_5 :
\pi^{(i)}(p) \in \mathsf{P}^{BDI}_3\}$.  The constraints defining $D_i$
come from pulling BDI inequalities back through $\pi^{(i)}$:
$$
B_1 - T_1 \ge 0,\quad B_2 - T_2 \ge 0,\quad
P_1 - M_2 \ge 0,\quad P_2 - S \ge 0,
$$
plus $T_1, T_2 \ge 0$ (trivial — AII vars are nonnegative).

For each of these 5 pulled-back inequalities, we test whether it is
**AII-redundant** (implied by the AII polytope constraints) via Farkas
LP feasibility.  Code: `wall_catalog.py`.

**Result**:

- 25 of 26 pieces: **no active walls** (full pullback domain $D_i = \mathsf{P}^{AII}_5$).
- 1 piece (`M2_is_m236`): one active wall $\{2 m_2 - m_{236} + 2 m_{2345} \ge 0\}$.

So $D_i = \mathsf{P}^{AII}_5$ for 25 pieces, and $D_i \subsetneq
\mathsf{P}^{AII}_5$ for 1 piece.  The "subdivision" of AII has 25
overlapping maximal cells equal to the full polytope plus one
near-full cell.  **Not a fan.**

Why the redundancy: the pieces are designed by carefully bookkeeping
which AII variables contribute to which BDI coords so that the BDI
inequalities hold automatically.  The "land-in-cone" proofs (cf.
Day 58 §"Land-in-cone proofs (sample)") are exactly the redundancy
certificates.

## §3. Fan-in-BDI: REFUTED

For each piece $i$, the image cone $C_i = \pi^{(i)}(\mathsf{P}^{AII}_5)$.

$\mathsf{P}^{AII}_5$ has 9 extreme rays (simplicial!), so each $C_i$
has at most 9 image rays.  Code: `fan_test.py`.

**Result**:

- All 26 $C_i$ are 6-dimensional (full image dim).
- All 26 are **proper subcones** of $\mathsf{P}^{BDI}_3$ (no $C_i = \mathsf{P}^{BDI}_3$).
- $\mathsf{P}^{BDI}_3$ has 8 extreme rays; the union of all 26 piece-image
  rays has 28 distinct rays (8 BDI extremes + 20 "interior" rays).

Now the fan test.  For each $C_i$, take its centroid $c_i = \sum_r r$
(sum of image rays).  $c_i$ is interior to $C_i$ by construction.  Test:
for $i \ne j$, is $c_i \in \text{int}(C_j)$?  Code: `pairwise_fan.py`.

**Result**:

- **367 of 650 ordered pairs** have $c_i \in \text{int}(C_j)$.
- **149 unordered pairs** have mutual containment of each other's centroids.

A pair $(i, j)$ with $c_i \in \text{int}(C_j)$ has $C_i \cap C_j$ of
dimension 6 (since $c_i$ is an interior point of both $C_i$ and $C_j$,
a neighborhood of $c_i$ lies in $C_i \cap C_j$).  But for a fan, $C_i
\cap C_j$ must be a face of $C_j$, which is $< 6$-dimensional unless
$C_i = C_j$.  Since no two $C_i$ are equal as cones (their ray sets
differ — 26 distinct ray sets observed), the fan condition fails.

**The 26 image cones overlap in 6-dim regions.  Not a fan.**

The most "central" pieces (sit in many other cones):

| Piece                              | Contains # other centroids |
|------------------------------------|---------------------------:|
| `P7_T1_236_T2_23456`               | 22                         |
| `P5d_Rdouble_plus_m2`              | 21                         |
| `P7_T12_via_236_S_m2`              | 20                         |
| `P7_T1_T2_both_via_236`            | 20                         |
| `P7_T1_1_T2_2_via_236`             | 20                         |

These pieces have "wide" image cones that engulf most of the other
pieces' images.  At the opposite extreme:

| Piece                              | Contains # other centroids |
|------------------------------------|---------------------------:|
| `P7_12_m2_M2_S`                    | 0                          |
| `P7_M2_dbl_both_S_dbl_both`        | 3                          |
| `P7_M2_simple_S_m2_2x23456`        | 8                          |

These "narrow" image cones might be candidates for fan-cells of a
SMALLER fan structure — but the wide cones break any fan property.

## §4. The 26 are a TRUNCATION, not a structure

The "26" in Day-58 is just where greedy set cover lands at $N = 10$.
Computing min covers for smaller $N$ (`minimal_cover_recompute.py`):

```
N=6:  cover size  8,  essentials  4
N=7:  cover size 12,  essentials  8
N=8:  cover size 14,  essentials  9
N=9:  cover size 23,  essentials 21
N=10: cover size 25,  essentials 24
```

Combined with Day-60's $\Theta(N^2)$ new-primitives growth at $N \ge 16$:

> The minimum cover size is unbounded as $N \to \infty$.

So no FINITE fan can describe $\tilde\pi_3'$.  The 26 is just the
cardinality at $N = 10$, not a structural invariant.

## §5. Why Path A (PFL) cannot work

Path A asked: can the 4 distinct $T_1$ expressions
$$
\{m_{2345},\ m_{2345}+m_{23456},\ m_{2345}+m_{236},\ m_{2345}+2 m_{236}\}
$$
be unified by a single piecewise-fractional-linear formula
$T_1(p) = N_1(p)/D_1(p)$?

**No**, because:

The 4 expressions for $T_1$ correspond to 4 different **absorption
channels** for the $m_{236}$ and $m_{23456}$ contributions:
- $T_1 = m_{2345}$: don't absorb either into $T_1$.
- $T_1 = m_{2345} + m_{23456}$: absorb $m_{23456}$ into $T_1$.
- $T_1 = m_{2345} + m_{236}$: absorb 1 unit of $m_{236}$ into $T_1$.
- $T_1 = m_{2345} + 2 m_{236}$: absorb 2 units of $m_{236}$ into $T_1$.

The choice of absorption is **not determined by $p$**.  The same AII
point $p = (0, 0, m_{236} = 1, m_{23456} = 1, 0, 0, m_{2345} = 1, 0,
0)$ can be projected by any of the 4 pieces, giving 4 DIFFERENT $T_1$
values $\{1, 2, 2, 3\}$.  The piece is chosen by which BDI lattice
point $q$ we want to hit.

For a PFL formula $T_1 = N_1(p)/D_1(p)$ to be **a function of $p$**,
it must give a single value at each $p$.  Hence PFL can give one of
the 4 absorption choices, but not all 4.  No single PFL can model
$\tilde\pi_3'$ on its own — it would be a single section, not the
multivalued cover.

**The right framework is inherently multivalued.**  This is why
Path C (stack) is the structural answer.

## §6. What's actually going on (tropical sketch)

While the 26 pieces don't form a fan, there is a **tropical-like
structure** lurking at the level of absorption channels.

**Observation.**  Pieces in the same "core class" (16 classes from the
Day-60 analysis) share the projection $(M_2, P_1, P_2, S)$ and differ
only in $(T_1, T_2)$ — the "fiber coordinates" of the $T^{n-1}=T^2$
torus on BDI.

Within each core class, the variation in $(T_1, T_2)$ is encoded by:
- $(c^{T_1}_{m_{236}}, c^{T_1}_{m_{23456}}) \in \{0, 1, 2\} \times \{0, 1\}$
- $(c^{T_2}_{m_{1234}}, c^{T_2}_{m_{236}}, c^{T_2}_{m_{23456}}) \in \{0, 1\}^3$ (constrained)

So each core class supports a discrete "absorption lattice" of $(T_1,
T_2)$ choices.  These ARE finite per core class.

**Tropical reformulation (sketch).**  Define $\tilde\pi_3'$ formally as
a multivalued map
$$
\tilde\pi_3'(p) = \{(M_2(p), B_1(p), T_1^\alpha(p), B_2(p), T_2^\alpha(p), S(p))
   : \alpha \in A(p)\}
$$
where $A(p)$ is a finite set of "absorption labels" valid at $p$
(those for which the image lies in $\mathsf{P}^{BDI}_3$), and the
labels parameterise how AII free vars $m_{236}, m_{23456}, m_{1234},
m_{2345}$ split across $(T_1, T_2, M_2, S)$.

The labels at each $p$ form a polytope (the **absorption polytope**
$A(p)$).  Different $p$ give different absorption polytopes.

If this picture is right, the "fan structure" is on the **labels**, not
on $p$ or $q$.  Specifically, $A(p)$ would be cut out by linear
inequalities in the absorption-label variables, with $p$-dependent
constants.

This is **exactly the structure of a tropical fan family** (parametrized
fan), but indexed by a PARAMETER (the AII point), not a single ambient
fan.

## §7. Status

- **Path B (tropical fan)**: refuted at $n = 3$ in the strict finite
  form.  Possible in a parametrized-family form (§6), which is closer
  to **stack** than to a standard fan.  Investigation, not seed.
- **Path A (PFL)**: refuted at $n = 3$ structurally (multivaluedness is
  fundamental, not an artefact of polyhedrality).  Killed.
- **Path C (stack)**: the only remaining candidate.  The 2-categorical
  / groupoid structure should encode "AII point with absorption label"
  as a single object, with morphisms = change of label.

This is a **structural answer**, but a NEGATIVE one for fan reframes.
Bank as INVESTIGATION.  Day-50 rule review at next dream: this entry
is *not* seed-promotable, but it definitively closes the fan-reframe
question for $n = 3$ in the negative.

## §8. Anti-goals upheld

- No "fan exists" claim made; everything is refutation.
- No piece formulae re-ported; analysis used Day-58 piece matrices verbatim.
- No promotion to seed (per PROVE.md anti-goal).
- Day-60 phantom rule check: this writeup adds files in
  `proofs/` and `code/2026-06-09-pi3-fan-reframe/` only.  No commits,
  no Lean.  Lean session can resolve the mid-rebase state separately.

— Rick (Day 61, 2026-06-09, deep work)
