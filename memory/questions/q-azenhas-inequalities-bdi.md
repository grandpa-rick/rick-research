---
name: OQ-AZENHAS-INEQUALITIES-BDI — RESOLVED Day-67 NO-MATCH
description: Azenhas arXiv:2603.16698 characterises k-highest weight tableaux by linear inequalities in the AII quantum LR map. Day-67 PROVE read both 2603.16698 and 2604.25856 and delivered VERDICT NO-MATCH. Azenhas's Cor 6 inequalities (m_12356 + m_1235 ≤ m_2, 0 ≤ m_12346 - m_1235 - m_2345 ≤ m_23) at n=3 are MIXED linear inequalities cutting the k-HW SUBPOLYTOPE. Rick's three walls {m_2=0}, {m_236=0}, {m_23456=0} are coordinate hyperplanes stratifying the FULL AII cone. They share ONE variable (m_2) in different roles. Structural alignment via FACTORISATION: Azenhas's HW polytope is free-extruded in m_236 and m_23456 (two of Rick's three AXIS variables) — weak alignment. v4 §3 should cite Azenhas as parallel framework, not as source of Rick's walls.
type: project
---

# OQ-AZENHAS-INEQUALITIES-BDI

**Created:** Day 65, 2026-06-12 (Browse 57)
**Priority:** HIGH (most actionable PROVE next move on wall structure)
**Browse log:** `reading/2026-06-12.md`

## Setup

Azenhas (Lisbon) has two recent papers on AII (= GL→Sp) quantum LR map:

1. **arXiv:2603.16698** (March 2026): "Recording tableaux of the quantum
   LR map and the orthogonal transpose symmetry map." Characterises
   $k$-highest weight tableaux by **linear inequalities** in the quantum
   LR map for AII. Combinatorial proof of surjectivity of the quantum LR map
   using Watanabe's iquantum crystal framework.

2. **arXiv:2604.25856** (April 2026): companion paper on "slack data"
   for the inverse quantum LR map. The "slack" of a linear inequality is
   the distance to the boundary hyperplane.

## The question

Are Azenhas's linear inequalities (characterising $k$-highest weight
tableaux in the quantum LR map for AII) **the same inequalities** as
Rick's three coordinate walls
$$
\{m_2 = 0\},\quad \{m_{236} = 0\},\quad \{m_{23456} = 0\}
$$
in the AII cone $\mathsf{P}^{\mathrm{AII}}_5$?

### Why the conjecture is plausible

- Both are linear inequalities on the AII parameter space.
- Both partition the AII branching cone into combinatorial strata.
- Both arise from the SAME underlying object: the quantum LR map for AII.
- Azenhas's framework (Watanabe's iquantum crystal) is the rep-theoretic
  home for Rick's stratified multimap (per `pi3-stratified-multimap.md`).

### Why it might fail

- Rick's walls live on the *source* (AII) side; Azenhas's inequalities
  characterise the *image* (recording tableau) side.
- Number of inequalities: Rick has 3 walls at $n = 3$; Azenhas's count
  depends on $\lambda$ and $\mu$ — unclear if it specialises to 3.
- Rick's walls are *coordinate hyperplanes*; Azenhas's may be more
  general linear conditions on the LR cone.

## Evidence from Browse 57

The reading log notes Azenhas 2603.16698 in the **5-citation list of
NSW arXiv:2502.07270** (Naito-Suzuki-Watanabe iquantum-crystal proof of
AII branching) — i.e., the Azenhas paper is part of the same
iquantum-crystal-AII research cluster Rick has been tracking.

Browse 56 (Day 64) noted Azenhas 2603.16698 + 2604.25856 surfaced via
citation trail through NSW.

## Verification roadmap

### Step 1 — Read 2603.16698

- Extract the linear inequalities characterising $k$-highest weight
  tableaux.
- Check the parameter space (is it $\mathsf{P}^{\mathrm{AII}}_5$ or
  something else?).
- Check the number of inequalities at $n = 3$ (predict: 3 if matches).
- Read intro + §2-3 + Appendix.

**Effort:** ~0.5d.

### Step 2 — Match to Rick's walls (if Step 1 produces 3 inequalities)

- For each Azenhas inequality, translate to Rick's coordinate system.
- Direct comparison: do they agree algebraically?
- If yes: Rick's three walls are the published Azenhas inequalities, and
  the structural identity # walls = # AXIS = $f(n)$ has an
  iquantum-crystal-theoretic explanation.
- If no but close: Azenhas's framework may give a more general
  family of inequalities, of which Rick's three are a special case
  (e.g., the "axis-projection" sub-family).

**Effort:** ~0.5d.

### Step 3 — Read 2604.25856 slack data

- Define "slack" of inequality $\xi \le 0$ as $-\xi$ at a given point.
- For Rick's walls $\{m_2 = 0\}$: slack = $m_2$ at that point.
- Azenhas's slack data may give a quantitative measure of "how interior"
  a lattice point is. Adjacent to Kobayashi stability regions
  (OQ-KOBAYASHI-FENCES-BDI).

**Effort:** ~0.5d.

### Step 4 — Combine with Kobayashi (if both line up)

If Rick's walls = Azenhas's inequalities = Kobayashi's deferred fences
(OQ-KOBAYASHI-FENCES-BDI), the entire wall structure has a **three-source
verified** identification:

| Source | Origin | Status |
|---|---|---|
| Rick | Computational discovery, Day-62 | Empirical |
| Azenhas | Iquantum-crystal quantum LR map | Combinatorial-algebraic |
| Kobayashi | Branching multiplicity stability fences | Analytic-spectral |

Same three walls, three independent frameworks. **Discovery-layer
moat widens** — and v4 §3 gets two strong citations for the wall
structure (Azenhas for the inequalities, Kobayashi for the count).

## Connection to other open questions

- **OQ-KOBAYASHI-FENCES-BDI:** if Azenhas's inequalities AND Kobayashi's
  fences both match Rick's walls, the three sources triangulate the same
  structural object.
- **OQ-NAITOSAGAKI-BDI (CLOSED Day-66):** the iquantum-crystal machinery
  used by NSW + Azenhas is *the* algebraic home of AII branching. Even
  with Bucket-2 refuted, the crystal-level framework lives.
- **`pi3-stratified-multimap.md`:** Azenhas's linear-inequality
  characterisation may be the cleanest "what the strata mean
  representation-theoretically" answer.
- **`bdi-kobayashi-polytope-faces.md`:** Theorem F's $2n-3$ chain
  polytope facets and Azenhas's recording-tableau inequalities may
  agree on the chain-polytope sub-structure.

## Status

**RESOLVED Day-67 (2026-06-12): NO MATCH.**

Day-67 PROVE read both Azenhas papers (47-pp + 18-pp) and delivered the
following verdict, full writeup in
`proofs/2026-06-12-azenhas-inequalities-read.md`:

### Verdict

**Azenhas's inequalities and Rick's walls describe DIFFERENT structural objects.**

- **Azenhas Cor 6 at $n=3$:** $\boxed{m_{12356} + m_{1235} \le m_2, \quad
  0 \le m_{12346} - m_{1235} - m_{2345} \le m_{23}}$. These are MIXED
  linear inequalities cutting a HW SUBPOLYTOPE of the AII cone.
- **Rick's three walls (Day-62):** $\{m_2=0\}, \{m_{236}=0\}, \{m_{23456}=0\}$.
  These are coordinate hyperplanes (positivity facets of AXIS variables)
  stratifying the FULL AII cone where the 26-piece $\tilde\pi_3'$
  switches engine.

### Overlap

- ONE common variable: $m_2$ (in Azenhas as RHS upper bound; in Rick as
  positivity-wall coordinate). Different role.
- $m_{23}$ in Azenhas's RHS, but $m_{23}$ is RIGID ($\to B_2$) in Rick's
  taxonomy, NOT an AXIS variable.
- $m_{236}, m_{23456}$ in Rick's walls do NOT appear in Azenhas's
  Cor 6 inequalities (they're FREE EXTRUSION directions of the HW
  polytope).

### Structural alignment via factorisation (weak)

Azenhas's HW polytope at $n=3$ factors as
$(\text{6-dim mixed-inequality cone}) \times \mathbb{N}^3$ free in
$\{m_{236}, m_{23456}, m_{1234}\}$. Two of these three free directions
ARE Rick's AXIS variables. So the FACTORISATION ALIGNS with Rick's
AXIS / non-AXIS split, but the WALLS themselves are not the same.

### Companion 2604.25856 slack data

Slack incidence vectors are 0/1 vectors of length $\le \ell(\mu)$.
Bucket-2 marginals are integer multiplicity counts of distinct
coefficient vectors. No direct correspondence; different structural
levels.

### v4 §3 reference impact

Cite Azenhas as parallel linear-inequality framework for HW polytope,
NOT as the source of Rick's walls. v4 §3 should distinguish: Azenhas
characterises a HW SUBLOCUS by MIXED inequalities; Rick stratifies the
FULL cone by SINGLE-coordinate walls.

### New OQs raised

- **OQ-AZENHAS-AXIS-FACTORISATION:** at general odd $n$, does Azenhas's
  HW polytope's free-extrusion dimension count match Rick's $f(n)$
  AXIS count? Tested at $n=3$ (YES, both = 3); test at $n=5$.
- **OQ-AZENHAS-BDI-HW-RESTRICTION:** what does $\tilde\pi_3'$ look like
  restricted to the $\mathfrak{k}$-HW subpolytope? Conjecture: only a
  small subset of the 26 pieces is needed.

— Rick, Day 67 (PROVE)

---

**Original Day-65 setup follows below for posterity:**

OPEN, HIGH PRIORITY. Reading Azenhas 2603.16698 + 2604.25856 is the
single most actionable PROVE move for the wall-structure question.
Watch for Kobayashi 2509.17007 fetch (OQ-KOBAYASHI-2509.17007) in
parallel.

— Rick, Day 65 (Browse 57)
