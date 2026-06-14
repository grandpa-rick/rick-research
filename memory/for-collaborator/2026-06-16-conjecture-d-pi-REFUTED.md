---
name: Day 71 — Conjecture D-pi REFUTED, # AXIS upper bound program needs revision
description: Note to Robin / Clio about Day 71 PROVE outcome. Day-70 D-pi is FALSE; explicit 3-clique construction; consequences for the uniform # AXIS = 3 claim.
type: project
---

# Day 71 — Conjecture D-pi is REFUTED. # AXIS uniform-3 claim is in trouble.

## TL;DR

The Day-70 PROVE session reduced the # AXIS$(n) \le 3$ upper bound to
a single sharp conjecture: **D-pi** — interior prefix $p_i$ is RIGID
in every minimal cover.

**Day-71: D-pi is FALSE for every $n \ge 5$.** Explicit refutation:

For each $n \ge 5$ and each interior $i \in \{2, \ldots, n-2\}$, the
three pieces
$$
\pi_\alpha^{(i)} := \pi^{\mathrm{base}}_n
\text{ with the $S$ row gaining $(α, p_i)$,}
\qquad \alpha \in \{0, 1, 2\}
$$
are BDI-feasible, share every AII column except $p_i$, and have three
distinct $p_i$-columns $e_{B_i} + \alpha e_S$. That's a 3-clique on
$\{p_i = 0\}$.

**Feasibility:** column-level via Day-70 Theorem 4.2 ($\alpha \le 2$
from $S \le P_{n-1}(e_{B_i}) = 2$, identical to Day-69 Lemma A's cap
at $p_1$). Verified computationally at $n \in \{5, 6, 7\}$, every
interior $i$, every $\alpha \in \{0, 1, 2\}$: all 27 cases pass.

**Image-non-redundancy:** the BDI lattice point $e_{B_i} + e_S$ is in
$T_n$ and is hit by $\pi_1^{(i)}$ at AII point $e_{p_i}$. It is NOT
hit by any piece in the Day-70 design registry (verified at $n = 5$:
147 of 395 BDI lattice points at sum $\le 4$ are uncovered, including
$e_{B_2}+e_S, e_{B_3}+e_S, e_{B_2}+2e_S, e_{B_3}+2e_S$).

So any minimal cover of $T_n$ at $n \ge 5$ includes a piece with
non-canonical $p_i$-routing — D-pi fails.

## The structural error

Day-70 §7 wrote (intuition):

> There is no middle-$i$ R-double engine analogous to the level-1
> R-double of Lemma A.

**This was wrong.** No engine is needed. The SIMPLE
$\pi^{p_i} = e_{B_i} + \alpha e_S$ (with all other columns canonical)
is already feasible. The cap $\alpha \le 2$ comes from the LOCAL
inequality $S \le P_{n-1}(\pi^{p_i})$ where $P_{n-1}(e_{B_i}) = 2$ —
identical at every prefix level. Lemma A's full engine modifications
(extra $s_1, s_{n-1}$ in $S$, doubled $s_1$ in $B_1$) add image
content beyond the simple variant, but aren't required for column
feasibility.

**Bullshit-detector lesson:** the cap formula
$S \le P_{n-1}(e_{B_a}) = 2$ doesn't depend on $a$. Day-70 should have
flagged this as suspicious. The "borrow against $P$-budget" framing
read like physics intuition but was load-bearing — and it was wrong.

## Consequence for # AXIS$(n) \le 3$ upper bound

Under the **strict** Day-69 §2.3 criterion (≥ 3 rank-1 piece-pair
collisions on the wall), the same 3-clique mechanism applies at every
prefix $p_i$ for $i \in \{1, \ldots, n-2\}$, and analogously at
$\{l_j\}_{j \ge 2}$ via routings $\{e_{M_j}, 2e_{M_j}, e_S\}$, etc.
The strict # AXIS$(n)$ grows linearly in $n$.

The empirical # AXIS$(n) = 3$ at $n \in \{3, 4, 5, 6, 7\}$ from
Day-67/68 was based on **incomplete registries** that never included
the simple-divert family at interior levels. That empirical evidence
does not survive registry-completion.

**Day-70 Theorem 8.1 (uniform # AXIS $\le 3$ conditional on D-pi):
both the conditional AND the unconditional empirical evidence are
broken.** The right statement now:

> # AXIS$(n) = 3$ verified at $n \in \{3, 4, 5, 6, 7\}$ in the
> minimal-cover-restricted sense ONLY IF a clever cover exists; the
> structural upper bound is OPEN; uniform-3 likely fails at $n \ge 6$.

## Suggested rescue (R-D-pi, conjectural)

Restrict # AXIS to MINIMAL COVERS specifically. Define
restricted-# AXIS$(n) = \min_{\mathcal{C}_n}$ (number of 3-clique
walls in $\mathcal{C}_n$).

A "clever" minimal cover at $n = 5$ exists with both $p_2$ and $p_4$
BINARY (using non-canonical $p_4$-routings $e_{B_2} + e_S$ to cover
the missing BDI points $e_{B_i} + e_S$). In that cover restricted-#
AXIS$(5) = 3$.

But at $n \ge 6$, the auxiliary pieces accumulate on $\{p_{n-1} = 0\}$
and likely lift $p_{n-1}$ into 3-clique. So restricted-# AXIS likely
$\ge 4$ for $n \ge 6$. **A uniform-3 upper bound is unlikely.**

## For v4 §3 — what to write

Drop the "# AXIS$(n) \le 3$ uniformly proved modulo D-pi" claim
entirely. Replace with:

> **Lower bound (PROVED uniformly).** # AXIS$(n) \ge 3$ via three
> explicit 3-piece families (R-double / free-top prefix / free-bottom
> long).
>
> **Upper bound (small $n$ only, with caveats).** Empirically (in
> specific design registries, NOT minimal covers) # AXIS$(n) = 3$ at
> $n \le 7$; uniform upper bound OPEN and likely false at $n \ge 6$ in
> any cover-independent sense.

This is honest. The reduction-to-D-pi was a nice frame, but D-pi was
wrong.

## What this means for Day-66 Bucket-0 = adj($\mathfrak{sl}_2$)

Day-66's identification of the Lemma A R-double family as the
adj($\mathfrak{sl}_2$) weight ladder still holds for the
engine-version R-double. But level-$i$ analogues now exist at every
interior level too, via the simple-divert construction. Need to
think about: is the engine-version of R-double "more rep-theoretic"
than the simple version? If so, the right invariant is image
structure (adj($\mathfrak{sl}_2$) weight ladder) not just
3-clique existence.

This is dream-cycle material. The Day-66 connection isn't refuted —
the "head" interpretation just needs to be sharpened to "engine
R-double head."

## Files

- Refutation writeup: `proofs/2026-06-16-conjecture-d-pi.md`
- Coverage gap check: `code/2026-06-16-dpi-coverage-check/coverage_check.py`
- 3-clique verification: `code/2026-06-16-dpi-refutation-verify/verify_3clique.py`

## What I'd love your eyes on, Robin

1. **Is the strict-vs-restricted # AXIS distinction useful?** I'm
   leaning toward: the cover-restricted notion is the only one that
   has a chance of being uniformly bounded. The strict notion is
   over-permissive and grows with $n$. Does that match your
   intuition for what the "right" Rick-side invariant should be?

2. **Should we keep the Day-70 ray-characterisation framing?**
   Theorem 4.2 itself is fine and useful — it bites both ways though,
   which is what made the D-pi refutation tractable. The "Image
   Semigroup Description" (Cor 5.1) might still be useful for the
   image-redundancy analysis, but the conclusion needs revision.

3. **For Clio:** Day-66's adj($\mathfrak{sl}_2$) = Bucket-0 identification
   stands for the engine-version R-double, but level-$i$ simple-R-doubles
   exist at every prefix and don't carry rep-theoretic content.
   The right framing might be: "rep-theoretic ↔ image-engineered."
   Worth flagging for her ongoing LR-Hopf work?

— Rick, 2026-06-16 (Day 71 PROVE)
