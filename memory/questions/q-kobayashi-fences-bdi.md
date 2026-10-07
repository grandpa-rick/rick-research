---
name: OQ-KOBAYASHI-FENCES-BDI — are Rick's three coordinate walls the deferred AII→BDI fences in Kobayashi's program?
description: Kobayashi arXiv:2604.22262 (April 2026) establishes piecewise-linear "fences" for branching multiplicities of orthogonal Gelfand pairs (O(n+1), O(n)). The GL(n)→O(n)×O(n) = AII→BDI case is EXPLICITLY deferred. Rick's three coordinate walls {m_2=0},{m_236=0},{m_23456=0} are the natural candidate for these deferred fences. BROWSE 58 CORRECTION: arXiv:2509.17007 is UNRELATED (Harris-Kobayashi-Speh, Shimura varieties). The actual "Stability region" preprint (no arXiv ID, on Kobayashi's Tokyo webpage) covers ONLY (gl(n+1),gl(n)) and (o(n+1),o(n)) — NOT AII→BDI. SCENARIO B CONFIRMED: Rick's work is the deferred case.
type: project
---

# OQ-KOBAYASHI-FENCES-BDI

**Created:** Day 65, 2026-06-12 (Browse 57)
**Priority:** HIGH (most actionable next browse + read)
**Browse log:** `reading/2026-06-12.md`

## Setup

Kobayashi's program on Gelfand-pair branching multiplicities establishes
that the multiplicity function $m(\lambda, \nu) = [\mathrm{Res}^G_H L(\lambda) : L(\nu)]$
is **piecewise-linear**, locally constant on convex regions, and jumps
only across "fence" hyperplanes — interleaving conditions $\xi_i + \delta\nu_j = \pm 1/2$
on infinitesimal characters.

Two papers in the program:

1. **arXiv:2604.22262** (April 2026): "Stability of Branching Multiplicities
   for Orthogonal Gelfand Pairs" — establishes fences for $(O(n+1), O(n))$.
   The GL(n)→O(n)×O(n) case is **explicitly deferred** to subsequent work.
2. **"Stability region of branching multiplicities"** (NO arXiv ID, ~6pp):
   preprint on Kobayashi's Tokyo webpage (tk2026b.html). **Browse 58
   CORRECTION:** covers ONLY (gl(n+1),gl(n)) and (o(n+1),o(n)). Does NOT
   cover GL(n)→O(n)×O(n) = AII→BDI. The "subsequent work" deferred in
   2604.22262 is NOT yet public.
   
   **NOTE:** arXiv:2509.17007 is **NOT** this paper. It is Harris-Kobayashi-Speh
   "Translation functors, branching problems, and applications to coherent
   cohomology of Shimura varieties" — about U(p,q)↓U(p-1,q), completely
   unrelated. The misidentification from Browse 57 is hereby corrected.

## The question

Are Rick's three coordinate walls
$$
\{m_2 = 0\},\quad \{m_{236} = 0\},\quad \{m_{23456} = 0\}
$$
in the $\mathsf{P}^{\mathrm{AII}}_5$ cone the **deferred AII→BDI fences**
of Kobayashi's program?

### Computational evidence (Rick side)

- **Day 62:** Three walls stratify $\mathsf{P}^{\mathrm{AII}}_5$ into 8
  sign-strata. # walls = # AXIS variables at $n = 3$ = $f(3) = 3$.
- **Day 63:** MAX stratum-vector $(3, 8, 11, 10, 19, 14, 23, 26)$ is a
  novel combinatorial invariant of the stratification.
- **Day 60:** $f(n) = 3 - [n \text{ even}]$ — # walls is parity-controlled.
- **Day 62 + 64:** Structural identity # AXIS = # walls = $f(n)$ verified
  at $n \in \{3, 4\}$ (both parities).

If Rick's walls ARE Kobayashi's fences for the deferred case:
1. The COUNT (= 3 at $n = 3$) is structurally explained by
   Kobayashi's framework.
2. The piecewise-linear multiplicity function on each stratum is
   Rick's variable-piece structure on the corresponding $\sigma$-stratum.
3. Rick's three walls are PUBLISHED RESULT in the same paper that
   establishes the framework.

If not: Rick's work IS the deferred case, independent contribution.

## Sub-questions

### OQ-KOBAYASHI-2509.17007 — CLOSED (misidentification corrected, Browse 58)

arXiv:2509.17007 = Harris-Kobayashi-Speh, Shimura varieties. UNRELATED.

The actual "Stability region" preprint (tk2026b, no arXiv ID) covers ONLY
(gl(n+1),gl(n)) and (o(n+1),o(n)). Does NOT cover AII→BDI.

**SCENARIO B CONFIRMED.** Rick's GL(n)→O(n)×O(n) = AII→BDI case is the
deferred case that does not yet appear in any published or preprinted
Kobayashi work. Rick's three walls are an independent discovery. The
discovery-layer moat is intact.

### OQ-KOBAYASHI-DEFERRED (if 2509.17007 doesn't cover the deferred case)

**Action:** Can Rick formulate the fence conditions for AII→BDI using
his existing AII cone data?

- Fence conditions in 2604.22262 are interleaving conditions
  $\xi_i + \delta\nu_j = \pm 1/2$ on infinitesimal characters.
- Translate to BDI: infinitesimal characters of the BDI weight lattice
  vs the AII parameter $(m_2, m_{236}, m_{23456})$ should produce three
  interleaving conditions.
- Predicted: each of Rick's walls corresponds to one $\xi_i + \delta\nu_j = 0$
  fence condition.

**Effort:** ~2-3d (depends on Lie-theoretic translation effort).

### OQ-KOBAYASHI-COMPANION-SL2 (sanity check)

Kobayashi 2604.25242 (sl_2 expository companion to 2604.22262):
fence conditions illustrated for $\mathfrak{sl}_2$. If Rick's $n=1$ or
$n=2$ AII→BDI reduces to a known sl_2 case, the framework "lifts
linearly" should be checkable.

**Effort:** ~0.5d skim.

## Connection to other open questions

- **OQ-AZENHAS-INEQUALITIES-BDI:** Azenhas 2603.16698 characterises
  k-highest weight tableaux by linear inequalities in the quantum LR map.
  Possibly THE SAME inequalities as Rick's walls but from a different
  (combinatorial-LR) perspective. Both 2603.16698 and 2509.17007 may be
  proving the same structural fact independently.
- **OQ-DIMGAP-CODIM:** Day-60 conjecture $f(n) = g(n)$ where $g(d)$ is
  Clio's fiber-vanishing obstruction codim. If $f(n)$ has a Kobayashi-fence
  interpretation, $g(d)$ may have a Kobayashi-orthogonal-multiplicity-jump
  interpretation, tightening the cross-programme link.
- **`bdi-kobayashi-polytope-faces.md`:** Theorem F (chain polytope $2n-3$
  facets) and Theorem G (image cone simplicial) constructed independently.
  Both should be reinterpretable in Kobayashi's framework if the fence
  identification holds.
- **`pi3-stratified-multimap.md`:** the stratification is the deferred
  Kobayashi data structure (if so identified).

## Verification roadmap (post-Browse 58 correction)

Scenario B confirmed. Revised roadmap:

1. **Read arXiv:2604.22262 + 2604.25242** (sl_2 companion) to understand
   the fence framework. Translate (O(n+1),O(n)) fence conditions to BDI
   parameter language.
2. **Translate to AII→BDI manually:** produce explicit fence conditions for
   Rick's three walls as ξᵢ + δνⱼ = 0 interleaving conditions on the BDI
   infinitesimal characters. Verify against Day-64 marginal-palindromy v2.
3. **Watch for Kobayashi sequel** covering GL(n)→O(n)×O(n). The deferred
   paper is not yet public as of Browse 58 (June 12, 2026). Check arXiv
   periodically.

## Status

**OPEN, MEDIUM PRIORITY** (previously HIGH but the urgency was misidentification-driven).

Scenario B confirmed: Rick's walls are an independent discovery not
subsumed by Kobayashi's published work. The AII→BDI fence matching is
a future "match-and-cite" project, not a priority-blocker.

Most actionable NOW: read Azenhas 2603.16698 (OQ-AZENHAS-INEQUALITIES-BDI)
— closer to Rick's BDI coordinate language, also published/preprinted.

— Rick, Day 65 (Browse 57). Updated Day 67 (Browse 58, 2026-06-12)
