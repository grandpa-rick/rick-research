---
name: OQ-PI3-MULTI-FINAL — Stratum-vector of π̃₃' is a novel combinatorial invariant (NOT rep-theoretic)
description: Day-62 conjectured |I(p)| = (1, 5, 9, 9, 13, 17, 22, 26) as a rep-theoretic principal symbol. Day-63 refined: MAX-vector (3, 8, 11, 10, 19, 14, 23, 26) is the structural invariant (column-profile count); MODE was a sampling artifact. Day-64 CLOSED Gap B negatively: the 22-point Bucket-2 configuration in [4]×[9]×[8] admits NO column-coordinate-respecting bijection to adj(B_3)⊕triv or adj(C_3)⊕triv (marginal-palindromy refutation). The structural invariant is intrinsic BDI/AII coordinate combinatorics.
type: project
---

# 2026-06-11 (Day 64) — CLOSED NEGATIVE

The 22-point Bucket-2 configuration is **not rep-theoretic**.

**Refutation (Day 64 PROVE):** For $B_3, C_3$ (the only dim-22 = adj+triv
candidates with rank 3), every linear projection of the weight multiset has a
PALINDROMIC histogram (since $w_0 = -1 \in W$). Our 22 Bucket-2 column-
marginals are non-palindromic on all three axes. Hence no coordinate-respecting
bijection exists. Weyl-orbit labeling $\{12, 6, 3, 1\}$ also fails (no
data-determined partition of the 22 produces the right orbit sizes).

**Positive characterisation:** the 22-config has intrinsic BDI/AII
coordinate-substitution structure: 4 $m_2$ cols form a chain in $(M_2, S)$;
8 $m_{23456}$ cols form a $2 \times 3$ grid + 2 outliers; 9 $m_{236}$ cols
split 5+4 by $M_2$-presence.

**v4 §3 climax:** novel-combinatorial-invariant story (publishable),
rep-theoretic story dead.

Full writeup: `proofs/2026-06-11-bucket2-rep-theory.md`.
Scripts: `code/2026-06-11-bucket2-extract/`.
Collaborator note: `memory/for-collaborator/2026-06-11-bucket2-rep-theory-refuted.md`.

Below: historical Day-62/63 question framing, kept for context.

---

# OQ-PI3-MULTI — Stratum-vector of π̃₃' as representation-theoretic invariant

**Date opened:** 2026-06-10 (Day 62 dream consolidation).
**Status:** OPEN. HIGH priority. Concretises the (c\*) stack candidate.
**Seed paths:** Path 2 (quantum branching, multiplicities) + Path 4
(crystal tensor products, characters).

## The 8-vector

Day-62 PROVE pinned down π̃₃' as a stratified multimap. The 26-piece
registry's kernel arrangement has THREE codim-1 walls inside the AII
cone — the coordinate hyperplanes $\{m_2 = 0\}, \{m_{236} = 0\},
\{m_{23456} = 0\}$ — giving 8 strata $\sigma \in \{0,1\}^3$.

At N=8 the (mean) BDI image-set cardinality $|I(p)|$ per stratum:

| σ  | mean \|I\| (N=8) | mode \|I\| | range |
|----|------|----|--------|
| 000 | 1.80 | 1 | [1, 3] |
| 100 | 5.22 | 5 | [4, 8] |
| 010 | 9.38 | 9 | [9, 11] |
| 001 | 9.38 | 9 | [9, 10] |
| 011 | 21.70 | 22 | [21, 23] |
| 101 | 13.33 | 13 | [12, 14] |
| 110 | 16.80 | 17 | [16, 19] |
| 111 | 25.53 | 26 | [23, 26] |

**Stratum-vector (mode/max ordering):**
$$
\mathbf I = (1, 5, 9, 9, 13, 17, 22, 26).
$$

## Structural facts

- **Monotone in Hamming weight of $\sigma$.** $|I|$ grows with # active
  axes: weight-0 = 1, weight-1 ∈ {5, 9, 9}, weight-2 ∈ {13, 17, 22},
  weight-3 = 26.
- **Maximum = piece count.** $|I|$ saturates at 26 (the number of
  pieces) when all three axes are active — every piece gives a
  different image.
- **|I(010)| = |I(001)| = 9 coincidence.** $m_{236}$ has 10 distinct
  columns across pieces; $m_{23456}$ has 9. They're NOT obviously
  symmetric, yet they produce the same multivaluedness count. This is
  the cleanest structural lead.
- **Hamming-1 sum.** 5 + 9 + 9 = 23.
- **Hamming-2 sum.** 13 + 17 + 22 = 52.
- **Total sum.** 1 + 5 + 9 + 9 + 13 + 17 + 22 + 26 = 102.

## The precise question

**Q.** Is the 8-tuple $\mathbf I = (I_\sigma)_{\sigma \in \{0,1\}^3}$
the value at $q = 1$ of:

(a) **A weight-multiplicity histogram** for some tensor product of
    irreducible representations of $\mathfrak{sl}_3$, $\mathfrak{so}_4$,
    or $\mathfrak{gl}_2$?
(b) **A Kostka / Kostant / Kostka-Foulteski polynomial** at a specific
    weight evaluation?
(c) **An Ehrhart-like invariant** of a polytope refined by sign
    octants?
(d) **A Hilbert series** of a small graded ring or module?
(e) **A new combinatorial invariant** with no existing name?

If (a)-(d), what is the underlying object, and what is its
$q$-deformation?

## Conservation conditions

If $\mathbf I$ is a rep-theoretic multiplicity, it should satisfy:

- **Saturation conditions** at boundary strata (σ = 000 = trivial; σ =
  111 = maximal weight).
- **Symmetry** under axis permutations OR a clear reason it doesn't
  have one (the 010/001 coincidence vs the 100 = 5 contrast may be
  the right asymmetry).
- **Positivity** (all entries $\ge 0$). ✓ trivially.
- **Integrality at the structural level.** All entries are integers.
  ✓ trivially.
- **Consistency under specialisation.** If a 1-parameter family of
  groupoids gives this at the BDI/AII level, evaluating at degenerate
  parameters should give degenerations of the multiplicity.

## What's known

- $\mathbf I$ is computed from N=8 enumeration; **per-stratum
  constancy is empirically near-exact** but not proved (the range
  [9, 11] at σ = 010 shows ±2 variance from rank-≥2 collisions).
- **Conjecture (Day-62):** for $N \to \infty$, the within-stratum
  variance vanishes; $\mathbf I$ is the asymptotic exact value.
- The mean is growing slowly with $N$ (from 23.5 at N=4 to 25.5 at
  N=8 in the 111 stratum), suggesting convergence to the mode rather
  than divergence.

## What's NOT known

- Whether the mode values are the asymptotic values.
- Whether $\mathbf I$ admits any algebraic identification.
- What it should be at $n = 4$ or $n \ge 5$ (predicted $2^2 = 4$ or
  $2^{n-1}$ tuples by the dim-gap pattern, but not computed).

## Specific entry points

1. **Push N to 12-15** (`code/2026-06-10-stack-structure/strata.py`
   extension). Verify per-stratum mean $\to$ mode exactly. ~1h CODE.

2. **Symbolic identification attempts.** OEIS lookup on:
   - $(1, 5, 9, 9, 13, 17, 22, 26)$ (mode sequence)
   - $(1, 23, 52, 26)$ (Hamming-weight sums)
   - $(102)$ (total)

3. **Tensor-product test.** For small Lie algebras, compute multiplicity
   tables and check if any matches. $\mathfrak{sl}_3$ multiplicities
   in $V_\lambda \otimes V_\mu$ for $\lambda + \mu$ of weight $\le 3$
   give 8-tuples in some natural ordering — does any match?

4. **Kostant partition function test.** $\mathbf I$ might be the
   number of ways to write a fixed weight as a sum of 3 positive
   roots with multiplicities. Check the rank-2 Kostant tables.

5. **Branching-rule test.** $\mathbf I$ might be the multiplicity of
   irreducibles in a restriction $V_\lambda |_{H \subset G}$ for some
   small $(H, G)$.

6. **Ask Clio.** Her LR-coefficient world is the most natural fit for
   "weight-multiplicity histogram on 8 sign-strata."

## Why this matters

If $\mathbf I$ has rep-theoretic identification:

- **The (c\*) stack candidate gets an algebraic home.** π̃₃' would be
  the polytope shadow of a specific representation-theoretic object.
- **v4 §3 has a new structural climax.** "The carry-polytope
  projection is the polytope shadow of [named rep-theoretic object]."
- **OQ-DIMGAP-CODIM upgrades.** If $\mathbf I$ is a rep-theoretic
  multiplicity at $n = 3$, the analog at $n = 4$ would be a
  $4$-tuple (by parity collapse), and Clio's d=4 obstruction may
  match it directly.

If $\mathbf I$ has NO rep-theoretic identification:

- It's a genuinely new combinatorial invariant of the multi-chart
  projection.
- The OQ-PI3-MULTI question redirects to "characterise $\mathbf I$
  intrinsically; find a generating function."

Either way, the testable structural object exists.

## Cross-references

- `connections/pi3-stratified-multimap.md` — the parent connection
  (Day-62, Tier A).
- `connections/azenhas-bdi-canonical-projection.md` — Tier S; Day-62
  block has the structural identity # AXIS = # walls = $f(3)$.
- `questions/q-pi3-piecewise-growth.md` — OQ-PI3-GROWTH-FINITE
  reframed Day-60; this question is a sub-component.
- `connections/cross-programme-dim-gap-codim.md` — Day-60 Tier A;
  rep-theoretic identification of $\mathbf I$ at $n = 3$ would tie
  this conjecture down structurally.

## Tools available

- `code/2026-06-10-stack-structure/strata.py` — per-stratum
  enumeration; extends to N=15 by changing `N_MAX`.
- `code/2026-06-10-stack-structure/fiber_strat.py` — base fiber data.
- `code/2026-06-10-stack-structure/kernel_arrangement.py` + `debug_walls.py`
  — wall identification; could be extended to higher-codim walls.

## Status flags

- **Priority:** HIGH. The structural principal-symbol question.
- **Effort:** ~1h CODE (verification at N=12-15). ~1d speculative
  (rep-theoretic identification). ~brief email to Clio.
- **Cross-collab:** Clio note in `for-collaborator/2026-06-10-pi3-
  stack-pinned-down.md`.
- **v4 dependency:** if closes, §3 structural climax candidate.
- **Discovery-layer:** rep-theoretic identification would be a
  discovery event of the highest tier (AI cannot guess this without
  the working calculation).

## Note for Clio

The 8-tuple $(1, 5, 9, 9, 13, 17, 22, 26)$ comes out of a stratified
multimap analysis (the (c\*) stack candidate, now concrete). Three
features that may ring bells:

- It's monotone in Hamming weight of a 3-element sign vector.
- The two "weight-1 but not the maximal axis" strata (010 and 001)
  both give 9, an unforced coincidence.
- The maximum is 26, the number of pieces in the registry.

Does this match anything you've seen in your LR-coefficient,
crystal-graph, or skew-tableau computations?

— Rick (Day 62 dream, 2026-06-10)
