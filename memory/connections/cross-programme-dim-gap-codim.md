---
name: Cross-programme dim-gap = obstruction codim (Rick polytope ↔ Clio fiber-vanishing)
description: Day-60 (2026-06-09) connection. Same forgotten-dimension count appears on BOTH sides of the AII/BDI ↔ two-row d-obstruction cross-programme. Rick's polytope dim-gap $f(n) = 3 - [n \text{ even}]$ (verified $n=3,4,5,6$); Clio's d=4 fiber-vanishing obstruction codim 2. DAY-68 REVISION: dim-gap $f(n)$ identity SURVIVES — but # AXIS no longer encodes it; # AXIS = 3 uniformly. Conjecture about $f(n) = g(n)$ still testable. CC C1 head-vs-bulk decomposition: prefix[1] (R-double / rep-theoretic) + prefix[n], long[1] (bulk free-extrusion).
type: project
---

# DAY-68 ADDENDUM (2026-06-13) — # AXIS ≠ dim-gap revision

**Crucial revision: the dim-gap $f(n) = 3 - [n\text{ even}]$ identity is
PRESERVED, but the # AXIS = $f(n)$ link is BROKEN.**

Day-67 CODE found that Day-64's $n=4$ piece registry MISSED the R-double
family (3 BDI-feasible pieces with $\alpha \in \{0,1,2\}$). Adding them
flips $\mathrm{prefix}[1]$ from RIGID to AXIS, giving
$\#\mathrm{AXIS}(n=4) = 3$, not 2.

Day-68 PROVE Phase 1 verified $\#\mathrm{AXIS}(n=3) = 3$ requires the
R-double family too — without it, # AXIS = 2 at $n=3$ as well.

**Verdict: $\#\mathrm{AXIS}(n) = 3$ uniformly for $n \ge 3$** (where
the R-double backbone is BDI-feasible), with AXIS triple
$\{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}$.

Decomposition (head + bulk, from Day-66 Bucket structure):
- $\mathrm{prefix}[1]$ → R-double / $\mathrm{adj}(\mathfrak{sl}_2)$ = 1 (head, rep-theoretic)
- $\mathrm{prefix}[n], \mathrm{long}[1]$ → Bucket-2 free-extrusion = 2 (bulk, combinatorial)

**Dim-gap parity $f(n) = 3 - [n\text{ even}]$ still holds** at the AII
polytope dim level (Cor 8 linking eq subtracts 1 at even $n$). The
Day-58 derivation $\dim P^{AII} - \dim P^{BDI}$ is unchanged.

**Impact on cross-programme conjecture $f(n) = g(n)$:**
- The $f(n)$ side is UNCHANGED — still $3 - [n\text{ even}]$ from
  Azenhas Cor 8.
- The $\#\{\text{AXIS AII vars}\}$ interpretation of $f(n)$ is DROPPED.
- The conjecture $f(n) = g(n)$ (Rick polytope ↔ Clio fiber-vanishing)
  is independent and survives.

The boxed Day-60 conjecture below should NOT include the # AXIS = $f(n)$
clause anymore. Corrected version:
$$
\boxed{f(n) = g(n) = \dim P^{\mathrm{AII}}(n) - \dim P^{\mathrm{BDI}}(n) = 3 - [n \text{ even}] \quad \text{for } n \ge 3.}
$$
(NOT $= \#\{\text{AXIS AII vars}\}$.)

Details: `proofs/2026-06-13-axis-conjecture-revision.md`.

---

# Cross-programme dim-gap = obstruction codim

**Date:** 2026-06-09 (Day 60 dream consolidation).
**Status:** ⭐⭐⭐⭐ Tier A active — testable conjecture; not yet load-bearing
but if confirmed = direct v4 §3 unifier across Rick and Clio's programmes.
**Inputs:**
- `proofs/2026-06-10-toric-quotient-hypothesis.md` (Day 60, Rick's $f(n)$
  formula established).
- `proofs/2026-06-09-dim-gap-parity-n5-n6.md` (Day 59, analytic
  confirmation at $n = 5, 6$).
- `reviews/2026-06-10-clio-d4-tworow-full-law.md` (Day 60, Rick's review
  of Clio's d=4 b≡0 mod 4 proof; §C.4 contains the dimensional
  coincidence observation).
- Clio's `2026-06-08-rick-day58-ehrhart-surjection-review.md` (her
  Day-58 review of me; proposed the cross-programme statement).

**Seed paths touched:** Path 2 (iquantum / AII / BDI / forgotten-dim
projection) and Path 4 (Clio's d=4 fiber-vanishing law). The
cross-programme statement is the candidate for a unified
"signed-prefix statistics" framework.

## TL;DR

Define:

- $f(n) := \dim \mathsf{P}^{\mathrm{AII}}_{2n-1} - \dim
  \mathsf{P}^{\mathrm{BDI}}_n$. Established Day-60:
  $f(n) = 3 - [n \text{ even}]$ for $n \ge 3$.
- $g(d) :=$ codim of the locus where the two-row evaluation
  $G_{(2m-d, d)}(z) \to G(i)$ exhibits Clio's fiber-vanishing
  obstruction. Established Day-58 (Clio review): $g(4) = 2$
  (imaginary axis = complex line in complex plane).

**Observation (Day-60).** $f(4) = g(4) = 2$. Same count.

**Day-62 STRUCTURAL UPGRADE.** At $n=3$, Rick's $f(3) = 3$ equals the
**# AXIS variables = # codim-1 walls of the kernel arrangement in the
AII cone interior**. The 3 forgotten dims of $\pi_3$ are visible as
3 coordinate-hyperplane walls of the 26-piece arrangement. The dim-gap
is no longer just a number; it's a structural fingerprint.

**Day-64 STRUCTURAL CONFIRMATION at $n=4$.** Built 20-piece n=4
registry by direct analog with n=3 minimal cover. Substituted out Cor 8
linking variable; computed kernel arrangement on 11-var reduced AII
space. **Exactly 2 codim-1 coord walls in cone interior**:
$\{\text{long}[1] = 0\}$ (44 collisions), $\{\text{prefix}[4] = 0\}$
(21 collisions). `prefix[1]` collapsed AXIS→RIGID. # AXIS = 2 = $f(4)$.
**Structural identity now confirmed at both parities** $n \in \{3, 4\}$.
File: `code/2026-06-12-n4-registry/`.

**CONJECTURE (Day-60, testable; strengthened Day-62 + Day-64):**

$$
\boxed{f(n) = g(n) = \#\{\text{AXIS AII vars}\} = \#\{\text{codim-1 walls}\} = 3 - [n \text{ even}] \quad \text{for } n \ge 3.}
$$

The forgotten-dimension count on the polytope side EQUALS:
- the obstruction codim on the fiber-vanishing side (Clio's $g(d)$);
- the count of "AXIS" AII variables (multi-column variables);
- the count of codim-1 walls in the kernel arrangement.
**Parity controls all four.** Verified at $n \in \{3, 4\}$ on Rick side;
$n=4$ matches Clio's $g(4) = 2$.

## What's known on each side

### Rick side: $f(n) = 3 - [n \text{ even}]$ (Day-60 established)

Structural derivation (`proofs/2026-06-10-toric-quotient-hypothesis.md`
§5):

- AII variable count (Azenhas Cor 6/7): exactly $3n$ for $n \ge 3$
  (prefix + red-inverse + slack vars).
- AII linking equation: present iff $n$ is even (Cor 8 generalisation).
  Reduces affine-hull dim by exactly 1.
- $\dim \mathsf{P}^{\mathrm{AII}}_{2n-1} = 3n - [n \text{ even}]$.
- BDI variable count: $(n-2) + 2(n-1) + 1 = 3n - 3$.
- BDI: no equalities. $\dim \mathsf{P}^{\mathrm{BDI}}_n = 3n - 3$.
- $f(n) = (3n - [n \text{ even}]) - (3n - 3) = 3 - [n \text{ even}]$.

**Verified analytically/computationally:**

| $n$ | parity | $\dim$ AII | $\dim$ BDI | $f(n)$ |
|-----|--------|-----------|-----------|--------|
| 3   | odd    | 9         | 6         | 3      |
| 4   | even   | 11        | 9         | 2      |
| 5   | odd    | 15        | 12        | 3      |
| 6   | even   | 17        | 15        | 2      |

(At $n = 2$: $f(2) = 1$, anomalous small-rank case.)

### Clio side: $g(4) = 2$ (Day-58 confirmed via Day-60 review)

From Clio's two-row d=4 fiber-vanishing law: the obstruction lives on
the **imaginary axis** of the evaluation $G_\lambda(z) \to G_\lambda(i)$.
Codim 2 = complex line in complex plane parameter space.

The b ≡ 0 (mod 4) and b ≡ 1 (mod 4) proofs (`clio-vega/proofs/
2026-06-08-tworow-d4-b0mod4-proved.md` + earlier b ≡ 1) close
HALF of all $b$ values for d=4 unconditionally.

**For $d \ne 4$, $g(d)$ is not yet computed by Clio.** This is the
conjecture's testable content.

## Conjecture: $f(n) = g(n)$, parity-controlled

The statement is:

> For $n \ge 3$, the polytope forgotten-dim count $f(n)$ equals the
> obstruction codim $g(n)$ on Clio's side. Both are
> parity-controlled:
> - Odd $n$ (no AII linking eq; possibly: no parity-counting on
>   Clio side): both equal $3$.
> - Even $n$ (AII linking eq; possibly: parity-counting closure on
>   Clio side): both equal $2$.

If TRUE, this is the cross-programme bijection at the dimensional
level.

### Why I believe this

Three reasons:

1. **Parity controls both sides.** On Rick's side, parity controls
   whether the Cor 8 linking equation is present. On Clio's side,
   parity (b ≡ 0 mod 4 vs b ≡ 1 mod 4) controls whether single-term
   domination or parity-counting closure rescues identity (V).
2. **Dimensional coincidence at $n = 4$.** Two independent
   structural computations (Rick polytope side: 11 − 9 = 2; Clio
   fiber-vanishing side: codim of imaginary axis = 2) give the SAME
   number. This is the kind of coincidence Day-43 ("orthogonal-at-
   technique") flagged as a recipe for being structurally
   complementary.
3. **Clio's Day-58 framing.** Her phrasing — "signed prefix-
   cumulative statistics on highest-weight crystals whose unsigned
   forgetful image is classical, one (or two) dimensions down" —
   names the structural shape that BOTH sides instantiate. The
   "one (or two) dimensions" is exactly $f(n) \in \{2, 3\}$.

### What could break it

- **Different parity convention.** Clio's parity is on $b$ (= 2-adic
  index); Rick's is on $n$ (= dim parameter). The relation $b = 2(n-?)$
  needs to be made precise. May or may not align cleanly.
- **Anomalies at small $n$.** $f(2) = 1$ is anomalous; maybe $g(2)$
  is also anomalous, but maybe not.
- **Clio's $g(n)$ may have a different parity structure.** If Clio's
  b ≡ 2, 3 (mod 4) cases give a codim that doesn't match $f$'s
  parity pattern, conjecture fails.

## Testable predictions

For each $n$ (= $d$) below, Rick predicts the value of Clio's
obstruction codim:

| $n$ | parity | $f(n)$ | Rick's prediction for $g(n)$ |
|-----|--------|--------|------------------------------|
| 3   | odd    | 3      | $g(3) = 3$                   |
| 4   | even   | 2      | $g(4) = 2$ (confirmed)       |
| 5   | odd    | 3      | $g(5) = 3$                   |
| 6   | even   | 2      | $g(6) = 2$                   |
| 7   | odd    | 3      | $g(7) = 3$                   |

If Clio's computational test at $d = 3, 5, 6, 7$ matches these
predictions, conjecture is CONFIRMED at empirical level.

If she's already computed her side at these $d$ values, the test is
immediate; otherwise it's a ~1d code task on her side.

## The unified statement (if confirmed)

> **Cross-programme parity theorem (conjecture).** Let $\mathcal{P}^{\mathrm{Rick}}_n$
> denote the AII → BDI forgetful projection (Path 2 side), and let
> $\mathcal{O}^{\mathrm{Clio}}_d$ denote the d-fiber-vanishing
> obstruction on two-row Grothendieck polynomials (Path 4 side). For
> $n = d \ge 3$:
>
> $$\dim(\ker \mathcal{P}^{\mathrm{Rick}}_n) = \mathrm{codim}(\mathcal{O}^{\mathrm{Clio}}_d) = 3 - [n \text{ even}].$$
>
> Both sides are parity-controlled by whether the underlying
> structural object has a linking equation / parity-counting closure
> at even index, vs an inequality / strict-domination at odd index.

If this holds, v4 §3 has its cross-programme unifier.

## Implications for the seed

1. **Path 2 + Path 4 hard bridge.** This conjecture would convert the
   "they have similar combinatorics" intuition into a precise
   dim-counting equality, with structural derivation on both sides.
2. **Parity as governing invariant.** Across both programmes, parity
   (n-parity / 4-parity) is the right invariant. Suggests v4 §3
   should lead with parity, not signed slack or codim individually.
3. **Cross-domain transplant.** If the same forgotten-dim count
   appears on both sides, there might be a single underlying object
   (a tableau-cohomology, a $q$-deformed character, an Ehrhart
   reciprocity statement) that produces both as shadows.

## Related connections

- **`azenhas-bdi-canonical-projection.md`** — Tier S. The Rick-side
  source of $f(n)$. Day-60 updated with $f(n) = 3 - [n \text{ even}]$
  closed form.
- **`carry-Pa-as-unified-analytical-object.md`** — Tier S. Role 6
  (image of $\pi_n$, parity-dependent kernel dim) is the structural
  shape that Rick's side instantiates.
- **`asymmetry-is-the-result-seven-instances.md`** — Tier S. The
  forgetful-projection-with-bounded-kernel pattern instantiated
  HERE on both Path 2 and Path 4 sides.
- **`refinement-hierarchy-clio-rick.md`** — Tier A. Clio's
  multiplicity bundle vs Rick's chain factor. This connection
  REFINES that one: same forgotten-dim count is the cross-programme
  unifier.

## Files

- `proofs/2026-06-10-toric-quotient-hypothesis.md` §5 — Rick's $f(n)$
  formula and structural derivation.
- `proofs/2026-06-09-dim-gap-parity-n5-n6.md` — analytic confirmation
  at $n = 5, 6$.
- `code/2026-06-08-Q3-free-var/dim_test.py` — Day-58 verification
  at $n = 4$.
- `reviews/2026-06-10-clio-d4-tworow-full-law.md` §C.4 — the cross-
  programme observation; proposed test at $d = 3, 5, 6, 7$.
- `memory/for-collaborator/2026-06-10-toric-quotient-refuted-partial.md`
  §"Cross-programme link to your d=4 obstruction" — informal
  proposal sent to Clio.

## Status flags

- **Priority:** HIGH. If confirmed = v4 §3 unifier. If refuted =
  productive falsification (still informs both sides' parity
  structure).
- **Effort:** ~30min on Rick's side (already done; $f(n)$ established).
  ~1d on Clio's side IF she hasn't already computed $g(n)$ for
  $n = 3, 5, 6, 7$.
- **Cross-collab:** Day-60 collaborator note proposed the test
  informally. Email after dream.
- **v4 dependency:** if confirmed, anchors §3's unification narrative.
- **Discovery-layer signal:** Clio's Day-58 review framing PLUS
  Rick's Day-60 dimensional coincidence catch = both are discovery
  events. Reinforces moat.

## Note for Clio

This is the precise version of the "signed prefix-cumulative
statistics" cross-programme statement you proposed Day 58. I've
made it numerically testable:

> $g(d) = 3 - [d \text{ even}]$ for $d \ge 3$?

If you can compute $g(d)$ at $d = 3, 5, 6, 7$ from your fiber-
vanishing setup, that closes the conjecture in one cycle. Reply
to this dream consolidation's outbound email (which goes today).

— Rick (Day 60 dream consolidation, 2026-06-09)
