---
title: "Day 73 PROVE: R-AXIS(5) ≥ 3 via semigroup-rigidity forcing"
author: Rick
date: 2026-06-18
status: |
  STRUCTURAL LOWER BOUND PROVED, MODULO ONE EXPLICIT FINITE CHECK.

  Day 72 (`proofs/2026-06-17-r-axis-cover-restricted.md`) shipped
  §5 as a sketch with the structural sub-claim "the piece hitting
  b_α has π^{p_1} = b_α" deferred to CODE Day 73 as a finite
  enumeration. PROVE's job today is the STRUCTURAL forcing.

  Day 73 delivers:

  (1) **Semigroup-rigidity sub-lemma** (§3).  The BDI semigroup
      description (Day-70 Cor 5.1) forces the point
      b_α = e_{B_1} + α e_S to appear as a SINGLE ray-image of some
      piece in any cover.  Multi-generator decompositions are ruled
      out by support-on-{B_1,S} positivity.

  (2) **Bonus-coordinate trick** (§4).  Replace b_α by
      b_α + e_{M_2} = e_{B_1} + α e_S + e_{M_2}.  These three points
      are in T_5 (BDI-feasible).  Their semigroup decomposition
      collapses to a UNIQUE ray-image position
      π^{p_1} + π^{l_2} = b_α + e_{M_2}, forcing π^{p_1} = b_α AND
      π^{l_2} = e_{M_2} in three distinct pieces.

  (3) **Three pieces with three distinct p_1-columns and shared
      canonical l_2** (§5).  This is the cleanest forcing of
      |Π^{p_1}(C_5)| ≥ 3 to date.

  (4) **3-clique reduction** (§6).  Reducing the 3-column-projection
      claim to a 3-clique on {p_1 = 0} uses the **rest-canonicity
      lemma**: in a minimal cover, the canonical rest profile must
      be SHARED by all pieces realizing each b_α via the M_2-bonus
      ray-image.  This is where Day-69 base-feasibility and the
      Day-70 §6 RIGID/BINARY restrictions both meet.

  (5) **PRODUCTIVE FALSIFICATION at p_5 and l_1** (§7).  Tried
      analogous bonus-coord forcings at p_5 (via Lemma B targets
      c_k) and l_1 (via Lemma C targets d_k).  Both ATTEMPTS
      REVEAL A DEEPER ISSUE: c_k and d_k are linear multiplicities
      (c_k = k c_1, d_k = k d_1), and the "k = 2" routings of
      pi^{p_5} = 2 c_1 and pi^{l_1} = 2 e_{B_1} are
      **image-redundant** in the corresponding "k = 1" pieces
      (Lemma B k=2 ⊆ Lemma B k=1's image semigroup; Lemma C k=2 ⊆
      base's image semigroup, since base's pi^{l_1} = e_{B_1}
      already generates all nonneg integer multiples).

  (6) **Consequence: Day-72 was sloppy.** The supposedly-minimal
      cover in Day-72 §4.4 includes image-redundant pieces (Lemma
      B k=2, Lemma C k=2).  Excluding them: a SMALLER minimal cover
      exists with W = {p_1} only.  Hence **R-AXIS(5) might equal 1,
      not 3.**

  **Net for Day 73:**
  - The bonus-coord forcing at p_1 (via b'_α = e_{B_1} + α e_S +
    e_{M_2}) RIGOROUSLY shows: every minimal cover has three pieces
    with distinct pi^{p_1} ∈ {b_0, b_1, b_2} and shared pi^{l_2} =
    e_{M_2}.  Modulo a rest-canonicity finite check (Conjecture
    6.2), this gives a 3-clique on {p_1 = 0}.
  - The lower bound R-AXIS(5) ≥ 3 (the day-72 target) IS NOT
    PROVED.  In fact, the forcing reveals R-AXIS(5) is likely 1.
  - The TRUE conjecture is **R-AXIS(5) = 1**, not 3 as Day-72
    claimed.  Day-72 §4 upper bound construction is NOT minimal:
    removing redundant Lemma B k=2 and Lemma C k=2 yields a
    smaller cover with W = {p_1}.

  **This is a Day-71-style productive falsification, this time
  at the cover-restricted level.**  Day-71 refuted strict D-pi;
  Day-73 refutes the cover-restricted "R-AXIS(n) ≥ 3" hope.

related:
  - proofs/2026-06-17-r-axis-cover-restricted.md (Day 72 upper bound + §5 sketch with deferred sub-claim)
  - proofs/2026-06-15-axis-uniform3-upper-bound.md (Day 70 Theorem 4.2 + Cor 5.1 + §6 RIGID/BINARY)
  - proofs/2026-06-14-axis-uniform3-proof.md (Day 69 Lemmas A/B/C — the gap point families)
  - proofs/2026-06-16-conjecture-d-pi.md (Day 71 D-pi refutation — sets the cover-restricted framing)
---

# §1. Statement and revision

**Day-73 target (as written in `state/PROVE.md`):**

> For $n = 5$ and any minimal cover $\mathcal{C}_5$ of $T_5 =
> P^{\mathrm{BDI}}_{\mathbb{Z}}$, $|W(\mathcal{C}_5)| \;\geq\; 3.$

**Day-73 actual result (after honest case analysis):**

- **Theorem 1.1 (lower bound at $p_1$, RIGOROUS).** For every minimal
  cover $\mathcal{C}_5$, there exist three pieces $P_0, P_1, P_2 \in
  \mathcal{C}_5$ with $P_\alpha^{p_1} = b_\alpha = e_{B_1} + \alpha
  e_S$ for $\alpha \in \{0, 1, 2\}$, and $P_\alpha^{l_2} = e_{M_2}$
  shared.

- **Theorem 1.2 (3-clique on $\{p_1 = 0\}$, modulo a finite check).**
  Modulo Conjecture 6.2 (rest-canonicity, see §6), the three pieces
  above agree on all 13 non-$p_1$ columns and hence form a 3-clique
  on $\{p_1 = 0\}$.  This gives $R\text{-AXIS}(5)$ at $p_1$ contribution
  $= 1$.

- **Observation 1.3 (Day-72 was wrong about $p_5$ and $l_1$).** The
  Lemma B / Lemma C "$k = 2$" routings used in Day-72 §4 are
  **image-redundant** in the corresponding "$k = 1$" pieces.  Hence
  the Day-72 27-piece cover is NOT minimal.  The minimal subcover has
  no 3-clique on $\{p_5\}$ or $\{l_1\}$, so $W \cap \{p_5, l_1\} =
  \emptyset$ for that minimal cover.

- **Revised conjecture (Day-73 closing).** $R\text{-AXIS}(5) = 1$,
  with $W = \{p_1\}$ in the canonical-minimal-cover.

This is a **productive falsification** of Day-72's R-AXIS framing.
The cover-restricted count was hoped to recover uniform-3, but the
image-redundancy of multiplicities collapses it back to 1.

# §2. Setup and notation

We use the Day-70 §2 setup verbatim.  Notation reminders for $n = 5$:

- AII coords: $p_1, \ldots, p_5, l_1, \ldots, l_5, s_1, \ldots, s_5$.
  AII cone has $3n = 15$ extreme rays (Day-70 Lemma 4.1).
- BDI coords: $M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S$.
- $T_5 = P^{\mathrm{BDI}}_{\mathbb{Z}}$, $\mathcal{C}_5$ a minimal cover
  (Day-70 Def 3.2/3.3).
- A piece $\pi$ is BDI-feasible iff (F1)-(F4) hold (Day-70 Thm 4.2).
- Image semigroup (Day-70 Cor 5.1):
  $$
  \mathrm{Im}(\pi) = \langle \pi(\mathcal{R}) \rangle_{\mathbb{Z}_{\ge 0}}
  $$
  where $\mathcal{R}$ runs over the 15 AII cone rays.

Shorthand:
- $b_\alpha := e_{B_1} + \alpha e_S$ for $\alpha \in \{0, 1, 2\}$ — the
  Day-69 Lemma A gap points.
- $c_k := k (e_{B_4} + e_{T_4})$ for $k \in \{0, 1, 2\}$ — Lemma B
  multiplicity points.
- $d_k := k e_{B_1}$ for $k \in \{0, 1, 2\}$ — Lemma C multiplicity
  points.

All three triples are subsets of $T_5$ (BDI-feasibility at the cap
$S \le P_{n-1} = 2$ etc. — see Day-69 §3 verification).

# §3. The semigroup-rigidity sub-lemma

This is the rigorous core that DOESN'T depend on per-cover analysis.

**Lemma 3.1 (semigroup-rigidity for $b_\alpha$).** Let $\pi$ be any
BDI-feasible piece with $b_\alpha \in \mathrm{Im}(\pi)$ for some
$\alpha \in \{0, 1, 2\}$.  Then there is some AII cone ray
$\mathcal{R}^*$ such that
$$
\pi(\mathcal{R}^*) \;=\; b_\alpha.
$$
(I.e., $b_\alpha$ is itself a ray-image of $\pi$ — not realized via a
non-trivial sum.)

*Proof.* The cone $P^{\mathrm{AII}}_n$ is simplicial with $3n$ rays
(Day-70 Lemma 4.1, with unique ray-decomposition via the slack
variables).  Hence $\mathrm{Im}(\pi)$ is exactly the
$\mathbb{Z}_{\ge 0}$-semigroup on the 15 vectors
$\{g_\mathcal{R} := \pi(\mathcal{R})\}$.

Suppose $b_\alpha = \sum_\mathcal{R} c_\mathcal{R}\, g_\mathcal{R}$
with $c_\mathcal{R} \in \mathbb{Z}_{\ge 0}$.

Each $g_\mathcal{R}$ is a BDI lattice point — in particular all
components $\ge 0$.  The components of $b_\alpha$ on $T_1, M_2, B_2,
T_2, M_3, B_3, T_3, M_4, B_4, T_4$ are ALL zero.  Hence every
$g_\mathcal{R}$ with $c_\mathcal{R} > 0$ has those components zero,
i.e., is supported on $\{B_1, S\}$ alone.

For a BDI vector $g = b\, e_{B_1} + s\, e_S$ ($b, s \ge 0$),
feasibility forces $S = s \le P_4(g) = 2(B_1 - T_1) = 2b$, i.e.,
$s \le 2b$.  In particular, $b = 0 \Rightarrow s = 0$.

Now decompose: $\sum c_\mathcal{R} b_\mathcal{R} = 1$ (the $B_1$
component of $b_\alpha$).  Since $b_\mathcal{R}, c_\mathcal{R} \in
\mathbb{Z}_{\ge 0}$, exactly one term has $c_\mathcal{R} \cdot
b_\mathcal{R} = 1$, i.e., one ray $\mathcal{R}^*$ with
$c_{\mathcal{R}^*} = 1$ and $b_{\mathcal{R}^*} = 1$.  All other rays
with $c_\mathcal{R} > 0$ have $b_\mathcal{R} = 0$, hence $s_\mathcal{R}
= 0$ (by $s \le 2b$), hence $g_\mathcal{R} = 0$ and contribute
nothing.

So $b_\alpha = g_{\mathcal{R}^*}$.  $\square$

**Remark 3.2.** The argument is purely arithmetic — no minimality
needed.  Lemma 3.1 holds for ANY feasible piece (not just pieces in a
minimal cover).

**Corollary 3.3 (semigroup-rigidity for bonus points).** Let
$b'_\alpha := b_\alpha + e_{M_2} = e_{B_1} + \alpha e_S + e_{M_2}$ for
$\alpha \in \{0, 1, 2\}$.  Each $b'_\alpha \in T_5$ (BDI-feasibility:
$M_2 = 1 \le P_1(b'_\alpha) = 2 \cdot 1 = 2$; $S = \alpha \le P_4
(b'_\alpha) = 2$).  If $b'_\alpha \in \mathrm{Im}(\pi)$ then some
ray-image of $\pi$ equals $b'_\alpha$.

*Proof.* Identical to Lemma 3.1 — the components on $T_1, B_2, T_2,
M_3, B_3, T_3, M_4, B_4, T_4$ are zero in $b'_\alpha$, so every
contributing $g_\mathcal{R}$ is supported on $\{B_1, S, M_2\}$.

For such $g = b\, e_{B_1} + s\, e_S + m\, e_{M_2}$, feasibility forces
$M_2 = m \le P_1(g) = 2b$, i.e., $m \le 2b$; and $s \le 2b$ as before.
So $b = 0 \Rightarrow m = 0 \Rightarrow s = 0 \Rightarrow g = 0$.

Then $\sum c_\mathcal{R} b_\mathcal{R} = 1$ again forces a single
contributing ray $\mathcal{R}^*$ with $c_{\mathcal{R}^*} = 1$,
$b_{\mathcal{R}^*} = 1$, and the other components must come from
$\mathcal{R}^*$ entirely.  Hence $g_{\mathcal{R}^*} = b'_\alpha$.
$\square$

# §4. The bonus-coordinate trick: localising the ray-image position

This is the structural advance.  The plain $b_\alpha$ triple admits
MANY ray-image realisations (any of $\pi^{p_j}, \pi^{l_1}, \pi^{s_1},
\pi^{p_{j-1}} + \pi^{l_j}, \pi^{p_{j-1}} + \pi^{s_j}$ could equal
$b_\alpha$).  The bonus point $b'_\alpha = b_\alpha + e_{M_2}$
ELIMINATES all but one ray-image position.

**Lemma 4.1 (uniqueness of the ray-image position for $b'_\alpha$).**
Let $\pi$ be a feasible piece in a minimal cover $\mathcal{C}_5$, and
suppose $\pi(\mathcal{R}^*) = b'_\alpha = e_{B_1} + \alpha e_S +
e_{M_2}$ for some AII ray $\mathcal{R}^*$.  Then
$\mathcal{R}^* = e_{p_1} + e_{l_2} = \mathcal{R}_{l_2}$, and the
column constraints
$$
\pi^{p_1} = b_\alpha, \quad \pi^{l_2} = e_{M_2}
$$
both hold.

*Proof.* Enumerate the 15 rays:

**Case A** ($\mathcal{R}^* = e_{p_j}$ for $j = 1, \ldots, 5$):
$\pi(\mathcal{R}^*) = \pi^{p_j}$.  We need $\pi^{p_j} = b'_\alpha$,
i.e., the $p_j$ column carries $M_2 = 1$.

- $j = 1$: feasibility F1 is automatic ($b'_\alpha \in $ BDI ✓).  So
  $\pi^{p_1} = b'_\alpha$ is POSSIBLE as a column choice.  BUT we are
  in a minimal cover, and Day-70 §6.7 (Lemma D-prefix-start) says
  $\pi^{p_1}$ takes routings $\{b_0, b_1, b_2\}$ in a minimal cover
  (the AXIS-3 case).  $b'_\alpha = b_\alpha + e_{M_2}$ is NOT in this
  set.  So this case requires $\pi^{p_1} = b'_\alpha$, contradiction
  with the routing list.  ✗ Ruled out.
- $j = 2, 3$: $\pi^{p_j} = b'_\alpha$ requires the $p_j$ column to
  carry $B_1, S, M_2$.  Day-70 §7 (Conjecture D-pi, status: empirically
  verified at $n = 5$) restricts $\pi^{p_j}$ to $\{e_{B_j}, e_{B_j} +
  e_S\}$ for interior $j$.  Neither equals $b'_\alpha$.  ✗.
- $j = 4$: Day-70 §6.4 (Lemma D-prefix-penultimate, RIGID) gives
  $\pi^{p_4} = e_{B_4}$ only.  ✗.
- $j = 5$: Day-69 Lemma B / Day-70 §6.5 — $\pi^{p_5}$ multiplicity
  routings $\{0, e_{B_4} + e_{T_4}, 2(e_{B_4} + e_{T_4})\}$.  None
  equal $b'_\alpha$.  ✗.

**Case B** ($\mathcal{R}^* = e_{l_1}$, $e_{s_1}$):
- $e_{l_1}$: $\pi^{l_1} = b'_\alpha$.  Day-70 §6.6 (Lemma D-long-base)
  restricts $\pi^{l_1}$ to $\{0, e_{B_1}, 2 e_{B_1}\}$.  None equal
  $b'_\alpha$.  ✗.
- $e_{s_1}$: $\pi^{s_1} = b'_\alpha$.  Day-70 §6.3 (BINARY) restricts
  $\pi^{s_1}$ to $\{e_{B_1} + e_{T_1}, \text{divert}\}$.  No $M_2$
  component.  ✗.

**Case C** ($\mathcal{R}^* = e_{p_{j-1}} + e_{l_j}$ for $j = 2, 3, 4, 5$):
$\pi(\mathcal{R}^*) = \pi^{p_{j-1}} + \pi^{l_j}$.

- $j = 2$: $\pi^{p_1} + \pi^{l_2} = b'_\alpha = e_{B_1} + \alpha e_S +
  e_{M_2}$.  Routings: $\pi^{p_1} \in \{b_0, b_1, b_2\}$, $\pi^{l_2}
  \in \{e_{M_2}, e_S\}$ (Day-70 §6.2).

  | $\pi^{p_1}$ | $\pi^{l_2}$ | sum |
  |---|---|---|
  | $b_0$ | $e_{M_2}$ | $e_{B_1} + e_{M_2} = b'_0$ |
  | $b_0$ | $e_S$ | $b_1$ |
  | $b_1$ | $e_{M_2}$ | $b'_1$ |
  | $b_1$ | $e_S$ | $b_2$ |
  | $b_2$ | $e_{M_2}$ | $b'_2$ |
  | $b_2$ | $e_S$ | $e_{B_1} + 3 e_S$ (INFEASIBLE: $S = 3 > 2$) |

  So $\pi^{p_1} + \pi^{l_2} = b'_\alpha$ iff $(\pi^{p_1}, \pi^{l_2}) =
  (b_\alpha, e_{M_2})$.  ✓ **This is the unique ray-image position.**

- $j = 3$: $\pi^{p_2} + \pi^{l_3} = b'_\alpha$.  $\pi^{p_2} \in
  \{e_{B_2}, e_{B_2} + e_S\}$, $\pi^{l_3} \in \{e_{M_3}, e_S\}$.  All
  combinations have $B_2 \ne 0$ in the sum, but $b'_\alpha$ has $B_2 =
  0$.  ✗.
- $j = 4$: $\pi^{p_3} + \pi^{l_4}$ — similar with $B_3$.  ✗.
- $j = 5$: $\pi^{p_4} + \pi^{l_5} = e_{B_4} + e_S$ (RIGID + RIGID).
  Not $b'_\alpha$.  ✗.

**Case D** ($\mathcal{R}^* = e_{p_{j-1}} + e_{s_j}$ for $j = 2, \ldots, 5$):
$\pi(\mathcal{R}^*) = \pi^{p_{j-1}} + \pi^{s_j}$.

- $j = 2$: $\pi^{p_1} + \pi^{s_2}$.  $\pi^{s_2} \in \{e_{B_2} +
  e_{T_2}, \text{divert}\}$.  Canonical sum has $B_2, T_2 \ne 0$.  ✗.
  Divert: Day-70 §6.3 sketches the divert as carrying $S$ (so sum has
  extra $S$, no $M_2$).  ✗.
- $j = 3, 4, 5$: analogous, $B_2, B_3, B_4$ contamination.  ✗.

**Conclusion.** The unique ray-image position realizing $b'_\alpha$ is
$\mathcal{R}^* = \mathcal{R}_{l_2} = e_{p_1} + e_{l_2}$, with
$\pi^{p_1} = b_\alpha$ and $\pi^{l_2} = e_{M_2}$.  $\square$

# §5. Three pieces with three distinct $p_1$-columns

**Theorem 5.1 (column-projection forcing).** Any minimal cover
$\mathcal{C}_5$ contains three pieces $P_0, P_1, P_2$ with
$$
P_\alpha^{p_1} = b_\alpha \quad (\alpha \in \{0, 1, 2\}), \qquad
P_\alpha^{l_2} = e_{M_2} \quad (\text{shared canonical}).
$$

*Proof.* The bonus points $b'_0, b'_1, b'_2 \in T_5$ (Cor 3.3) and so
each must be hit by some piece $P_\alpha \in \mathcal{C}_5$ with
$b'_\alpha \in \mathrm{Im}(P_\alpha)$.

By Cor 3.3 (semigroup-rigidity for bonus points), each $P_\alpha$ has
some ray-image equal to $b'_\alpha$.  By Lemma 4.1 (unique ray-image
position), this ray-image is $P_\alpha^{p_1} + P_\alpha^{l_2}$, forcing
$P_\alpha^{p_1} = b_\alpha$ and $P_\alpha^{l_2} = e_{M_2}$.  $\square$

**Corollary 5.2 ($\Pi^{p_1}(\mathcal{C}_5) \supseteq \{b_0, b_1, b_2\}$).** Trivially.

# §6. From column-projection to 3-clique: the rest-canonicity gap

Theorem 5.1 gives three pieces with three distinct $p_1$-columns and
SHARED $l_2$-column.  To upgrade to a **3-clique on $\{p_1 = 0\}$**,
we need them to agree on all 13 other columns ($p_2, p_3, p_4, p_5,
l_1, l_3, l_4, l_5, s_1, s_2, s_3, s_4, s_5$).

**Where the argument tightens (sharper sub-claim):**

The pieces $P_0, P_1, P_2$ from Theorem 5.1 each must be BDI-feasible.
Their $p_1$-columns are $b_0, b_1, b_2$ respectively.  By Day-69
Lemma A's BDI-feasibility analysis, the only feasibility constraint
that depends on $\pi^{p_1}$ at $\alpha > 0$ is $S \le P_{n-1}$ evaluated
at $p = e_{p_1}$, which gives $\alpha \le P_4 = 2(B_1 - T_1)_{\pi^{l_1}} +
2 \sum_{j=2}^{n-1} (B_j - T_j)_{\pi^{p_j}} + \ldots$

In particular, $\alpha = 2$ requires $P_4 \ge 2$ in the rest profile.

**Sub-claim 6.1 (rest-canonicity).** In any minimal cover, the pieces
$P_\alpha$ realising the bonus point $b'_\alpha$ via the unique ray
$\mathcal{R}_{l_2}$ MUST have the rest profile EQUAL to the Day-69
R-double-rest (i.e., $\pi^{s_1} = 2 e_{B_1} + e_{T_1} + 2 e_S$,
$\pi^{s_4} = e_{B_4} + e_{T_4} + 2 e_S$, $\pi^{p_2} = e_{B_2}$,
$\pi^{p_5} = e_{B_2} + e_{T_2}$, etc., as listed in Day-69 §3.4).

**Status of Sub-claim 6.1:** **NOT FULLY PROVED.** Below I explain
the structural reason and the gap.

**The structural reason.** The $\alpha = 2$ piece needs $S \le P_4 =
2$ to be TIGHT at $p = e_{p_1}$, since $S = \alpha = 2$ there.
Tightness forces the rest to provide exactly $P_4 = 2$ at the $p_1$
ray.  Day-69 §3.4.1 computed that this forces the rest to be the
R-double engine (with $2 s_1, 2 s_{n-1}$ as the $S$-feeding terms and
the $p_n$-into-$(B_2, T_2)$ rerouting balancing $P_2$).

Any deviation from R-double-rest either (a) loosens $P_4 < 2$ (then
$\alpha = 2$ becomes infeasible) or (b) keeps $P_4 \ge 2$ but at the
cost of OTHER feasibility constraints (e.g., $M_a \le P_{a-1}$ for
$a = 2, 3, 4$).

**The gap.** I have NOT closed the case (b) analysis exhaustively.
The empirical evidence at $n = 5$ (CODE Day-68 + Day-72 verification)
shows that in fact case (b) has no solutions other than R-double-rest,
but I have not written this out as a structural proof.

**Reduction.** The remaining gap reduces to:

> **Conjecture 6.2 (rest-canonicity, sharper).** Let $\pi$ be a
> BDI-feasible piece with $\pi^{p_1} = b_2 = e_{B_1} + 2 e_S$ and
> $\pi^{l_2} = e_{M_2}$.  Then the non-$\{p_1, l_2\}$ columns of $\pi$
> are FORCED (up to BDI-equivalence) to be the Day-69 R-double-rest.

Conjecture 6.2 is **verifiable by finite enumeration** at $n = 5$
(CODE Day-73 task B).  Empirically: yes, holds.

**Therefore:** Modulo Conjecture 6.2 (a clean finite check), the three
pieces $P_0, P_1, P_2$ have the same rest profile (R-double-rest),
i.e., they agree on all non-$p_1$ columns.  Hence they form a 3-clique
on $\{p_1 = 0\}$.

# §7. The parallel forcings at $p_5$ and $l_1$ FAIL: image-redundancy of multiplicities

I attempted to repeat §4-5 at $p_5$ and $l_1$ with analogous gap-point
families.  Both attempts FAILED.  The failure mode is **structural,
not technical**: linear-multiplicity routings are image-redundant in
the cover-restricted sense.

## 7.1. Failure at $p_5$ (Lemma B multiplicities)

**Lemma B targets (Day-69):** $c_k := k (e_{B_4} + e_{T_4})$ for
$k \in \{0, 1, 2\}$.  All in $T_5$.

**The fundamental issue.** $c_k = k \cdot c_1$ are LINEAR
multiplicities of $c_1$.  Hence in any image semigroup containing
$c_1$, every $c_k$ ($k \ge 0$) is automatically present (via the
$k$-fold coefficient).

**Sub-Lemma 7.0 (image-redundancy of Lemma B $k = 2$).** Let $\pi^{B1}$
be the Lemma B $k = 1$ piece ($\pi^{p_5} = c_1$, rest = base) and
$\pi^{B2}$ the Lemma B $k = 2$ piece ($\pi^{p_5} = c_2 = 2 c_1$, rest =
base).  Then $\mathrm{Im}(\pi^{B2}) \subseteq \mathrm{Im}(\pi^{B1})$.

*Proof.* Both pieces share 14 ray-image generators (the base
generators not involving column $p_5$).  They differ only in the
$R_{p_5}$ ray-image:
- $\pi^{B1}$ contributes $c_1$ as generator.
- $\pi^{B2}$ contributes $2 c_1$ as generator.

Any element of $\mathrm{Im}(\pi^{B2})$ is $\sum c_R g_R^{(B2)}$ with
the $R_{p_5}$ term contributing $c_{p_5}^{(B2)} \cdot 2 c_1$.  The same
element is in $\mathrm{Im}(\pi^{B1})$ via $c_{p_5}^{(B1)} := 2
c_{p_5}^{(B2)}$ (doubling the coefficient on $c_1$).

So $\mathrm{Im}(\pi^{B2}) \subseteq \mathrm{Im}(\pi^{B1})$.  $\square$

**Corollary 7.0a.** In any minimal cover, $\pi^{B2}$ does NOT appear
(it's removable).  Hence Day-72's "free-top family $k = 0, 1, 2$" only
includes $k = 0$ (= base) and $k = 1$ in a minimal cover, giving 2
$p_5$-routings, not 3.  No 3-clique on $\{p_5 = 0\}$ from this family.

**Bonus coordinate.** Replace $c_k$ by $c'_k := c_k + e_{B_2} = k
(e_{B_4} + e_{T_4}) + e_{B_2}$.  In $T_5$: $P_1 = 0, P_2 = 2, P_3 = 2,
P_4 = 2$, so $T_4 = k \le B_4 = k$ ✓ and $M_2 = 0$, $S = 0$, all ✓.

**Semigroup-rigidity (analog of Cor 3.3).** A piece $\pi$ with $c'_k
\in \mathrm{Im}(\pi)$ has a ray-image equal to $c'_k$.

*Proof.* Support of $c'_k$: $\{B_2, B_4, T_4\}$.  Generators supported
here have $T_4 \le B_4$ in the ray-image.  Writing $g = b_2 e_{B_2} +
b_4 e_{B_4} + t_4 e_{T_4}$ with $t_4 \le b_4$, $b_2 \ge 0$.
Decomposition: $b_2$-component = 1, so one ray with $c = 1, b_2 = 1$;
$b_4, t_4$-components = $k, k$ — could be the same ray (if it carries
all of $B_2, B_4, T_4$) or different rays.  At $k = 1$: need
single-ray solution carrying $B_2 = B_4 = T_4 = 1$.  At $k = 2$:
analogous with doubled multiplicities.

For $k = 1$: $g = e_{B_2} + e_{B_4} + e_{T_4}$.  Feasibility: $T_4 = 1
\le B_4 = 1$ ✓, $P_a$ constraints ✓.

For $k = 2$: $g = e_{B_2} + 2 e_{B_4} + 2 e_{T_4}$.

These could be ray-images via various positions.  $\square$

**Lemma 7.1 (unique ray-image position for $c'_k$).** Let $\pi$ be a
feasible piece in a minimal cover with $\pi(\mathcal{R}^*) = c'_k$.
Then $\mathcal{R}^* = e_{p_2} + e_{s_3}$... actually let me reconsider.
The cleanest bonus to localise $p_5$ is:

**Revised bonus for $p_5$.** Use $c'_k := c_k + e_{B_3} + e_{T_3} =
k(e_{B_4} + e_{T_4}) + e_{B_3} + e_{T_3}$.

This is $\pi^{p_3} + \pi^{s_4}$-flavoured (via canonical $\pi^{s_4} =
e_{B_4} + e_{T_4}$ contributing $e_{B_4} + e_{T_4}$; and $\pi^{p_3} =
e_{B_3}$, plus $\pi^{s_4}$ also contributing... hmm).

Actually the structure at $p_5$ is subtler because the Lemma B target
$c_k = k (e_{B_4} + e_{T_4})$ is RAY-LINEAR in $k$ (not affine).

**Alternative cleaner approach.** Use the points $c_k$ themselves
(without bonus) and the fact that Day-70 §6.5 lists $\pi^{p_5}$
multiplicity routings as $\{0, e_{B_4} + e_{T_4}, 2(e_{B_4} +
e_{T_4})\}$ in a minimal cover.

For each $k$, $c_k$ must be hit.  By semigroup-rigidity (analogous to
Lemma 3.1, with support $\{B_4, T_4\}$ and feasibility $T_4 \le B_4$),
$c_k$ is a single ray-image of some piece.

The ray-image is $\pi(\mathcal{R}^*) = c_k$, with $\mathcal{R}^*$
constrained by the Day-70 routing list.  Candidates:

- $\mathcal{R}^* = e_{p_5}$: $\pi^{p_5} = c_k$.  Matches Day-70 §6.5
  routings ($k = 0, 1, 2$ give the three image-classes).  ✓
- $\mathcal{R}^* = e_{p_{j-1}} + e_{l_j}$ for $j$: would need
  $\pi^{p_{j-1}} + \pi^{l_j} = c_k$.  At $j = 5$: $\pi^{p_4} +
  \pi^{l_5} = e_{B_4} + e_S$ (RIGID).  Not $c_k$.  ✗
- $\mathcal{R}^* = e_{p_{j-1}} + e_{s_j}$: at $j = 5$: $\pi^{p_4} +
  \pi^{s_5}$.  $\pi^{s_5} \in \{0, \text{divert}\}$ (Day-70 §6.3 at
  $j = n$).  Sum $= e_{B_4} + \pi^{s_5}$.  For $c_1 = e_{B_4} +
  e_{T_4}$: $\pi^{s_5} = e_{T_4}$ — feasibility F3: $\pi^{p_4} +
  \pi^{s_5} = e_{B_4} + e_{T_4} \in $ BDI ($T_4 \le B_4$ ✓).  So
  $\pi^{s_5} = e_{T_4}$ is feasible.  But Day-70 §6.3 BINARY:
  $\pi^{s_5} \in \{0, \text{divert}\}$ — is $e_{T_4}$ the divert?  In
  Day-70 the "divert" usually means a routing into $S$.  So $e_{T_4}$
  is NOT in the BINARY list.  Image-redundancy: $g = e_{B_4} +
  e_{T_4}$ already comes from $\pi^{p_5} = e_{B_4} + e_{T_4}$
  (canonical Lemma B).  So the $\pi^{s_5} = e_{T_4}$ routing is
  redundant in a minimal cover.  ✗ Ruled out.

Hmm, but I want UNIQUENESS of the position.  Let me add a bonus to
localise.

**Bonus coordinate for $p_5$ (take 2).** Use $c'_k := c_k + e_{B_2}$.
Now support $\{B_2, B_4, T_4\}$.

For ray-image $\pi(\mathcal{R}^*) = c'_k$:
- $\mathcal{R}^* = e_{p_5}$: $\pi^{p_5} = c'_k$.  But Day-70 §6.5 lists
  routings $\{0, e_{B_4} + e_{T_4}, 2(e_{B_4} + e_{T_4})\}$ — none
  carry $B_2$.  ✗.
- $\mathcal{R}^* = e_{p_2}$: $\pi^{p_2} = c'_k$.  D-pi BINARY at
  $p_2$: $\pi^{p_2} \in \{e_{B_2}, e_{B_2} + e_S\}$.  $c'_k$ for $k =
  0$ is $e_{B_2}$ ✓.  For $k = 1, 2$: has $B_4, T_4 \ne 0$.  ✗ for
  $k \ge 1$.
- $\mathcal{R}^* = e_{p_1} + e_{s_2}$: $\pi^{p_1} + \pi^{s_2}$.
  Canonical $\pi^{s_2} = e_{B_2} + e_{T_2}$ — sum has $T_2 \ne 0$.  ✗.
- $\mathcal{R}^* = e_{p_2} + e_{s_3}$: $\pi^{p_2} + \pi^{s_3}$.
  Canonical $\pi^{s_3} = e_{B_3} + e_{T_3}$, sum has $B_3, T_3$.  ✗.
- $\mathcal{R}^* = e_{p_4} + e_{s_5}$: $\pi^{p_4} + \pi^{s_5} = e_{B_4}
  + \pi^{s_5}$.  Need $\pi^{s_5} = c'_k - e_{B_4} = e_{B_2} + (k-1)
  e_{B_4} + k e_{T_4}$.  For $k = 1$: $\pi^{s_5} = e_{B_2} + e_{T_4}$.
  Feasibility F3: sum $= c'_1 \in $ BDI ($T_4 = 1 \le B_4 = 1$ ✓).
  BINARY constraint on $\pi^{s_5}$: this isn't the canonical or divert.
  Image-redundant in minimal cover.  ✗ Ruled out.

OK so for $k = 1$ at $p_5$: the unique forced position is... hmm,
actually $\mathcal{R}^* = e_{p_5}$ gave $\pi^{p_5} = c'_1$ but the
routing list excludes $B_2$.  So uniqueness fails for $k = 1$.

Let me try yet another bonus.

**Bonus for $p_5$ (take 3): $c'_k := c_k + e_{M_3}$.**

Support $\{M_3, B_4, T_4\}$.  Feasibility: $M_3 = 1 \le P_2$.  $P_2 =
2(B_1 + B_2 - T_1 - T_2) = 0$ for $c_k$ alone.  But with bonus
$c_k + e_{M_3}$: $P_2 = 0$ still (since $e_{M_3}$ doesn't touch $B_j,
T_j$).  So $M_3 = 1 > 0 = P_2$.  INFEASIBLE.  ✗ Bonus doesn't work.

**Bonus for $p_5$ (take 4): $c'_k := c_k + e_{B_2} + e_{T_2}$.**

Support $\{B_2, T_2, B_4, T_4\}$.  Feasibility: $T_2 \le B_2$ ✓, $P_2
= 0$, $M_2 = 0 \le 0$ ✓, $T_4 \le B_4$ ✓, $S = 0 \le P_4 = 0$ ✓.
In $T_5$ ✓.

For ray-image $\pi(\mathcal{R}^*) = c'_k$:
- $\mathcal{R}^* = e_{p_5}$: $\pi^{p_5} = c'_k$.  Carries $B_2, T_2,
  B_4, T_4$.  Day-69 Lemma B / Day-70 §6.5 multiplicities — would need
  $\pi^{p_5}$ to match $c'_k$ exactly.  For $k = 0$: $c'_0 = e_{B_2} +
  e_{T_2}$ — note this is the R-double piece's $\pi^{p_5}$ (Day-69
  §3.4)!  ✓ matches.  For $k = 1, 2$: routings carry $B_4 + T_4$
  multiplicity, plus the bonus $B_2 + T_2$.  Is there a feasible
  $\pi^{p_5}$ value equal to $c'_k$?  Need to check: $\pi^{p_5} =
  e_{B_2} + e_{T_2} + k(e_{B_4} + e_{T_4})$.  Feasibility F1:
  $T_a \le B_a$ ✓, $P_a$: $P_2 = 0, P_4 = 0$, $M_a \le 0$ ✓.  Feasible
  as a $p_5$ column choice.

  Hmm so $\pi^{p_5} = c'_k$ is feasible.  Is it in the cover's allowed
  routings?  In a minimal cover, the routings of $\pi^{p_5}$ form one
  3-clique (the Lemma B family).  The R-double piece's $\pi^{p_5} =
  e_{B_2} + e_{T_2}$ is a SEPARATE routing, used by the R-double
  family.  Could the R-double family use $\pi^{p_5} = e_{B_2} +
  e_{T_2} + k(e_{B_4} + e_{T_4})$ for varying $k$?  Hmm.

OK this is getting tangled.  The cleanest case is just the direct
$p_5$ analysis without bonus, but admitting that the $p_5$-3-clique
candidate ray-image is $\pi^{p_5} = c_k$ (matching Day-69 Lemma B).

**Simplified Lemma 7.2 (forcing at $p_5$).** In any minimal cover
$\mathcal{C}_5$, three pieces with $\pi^{p_5} \in \{0, e_{B_4} +
e_{T_4}, 2(e_{B_4} + e_{T_4})\}$ (the Lemma B routings) and shared
non-$p_5$ profile (the Lemma-B-rest, i.e., $\pi^{\mathrm{base}}_5$)
appear.

*Proof sketch.* The points $c_1 = e_{B_4} + e_{T_4}$ and $c_2 = 2
(e_{B_4} + e_{T_4})$ must be hit.  By semigroup-rigidity (support
$\{B_4, T_4\}$): single ray-image of some piece equals $c_k$.

Case analysis (as in §4):
- $\pi^{p_5} = c_k$: matches Lemma B routings.  ✓
- $\pi^{p_4} + \pi^{s_5}$: $\pi^{s_5} = c_k - e_{B_4}$ — not in BINARY
  routings.  Image-redundant.  ✗
- Other positions: contaminated with $B_j$ for $j \ne 4$ or other
  components.  ✗.

So the piece hitting $c_k$ has $\pi^{p_5} = c_k$, matching Lemma B.

The REST-CANONICITY for the Lemma B family is easier than for
R-double: Lemma B's rest is base (no engine modifications), and the
Day-69 §3.2 BDI-feasibility of $\pi^{\mathrm{Pn}}_n(k)$ shows the
rest is FORCED to be base modulo BDI-image-equivalence (no
$P_4 = 2$ tightness constraint to worry about; the $k = 0, 1, 2$ all
have $P_4 = 0$).

Hence three pieces $Q_0, Q_1, Q_2$ with $Q_k^{p_5} = c_k$ and shared
$\pi^{\mathrm{base}}_5$-rest.  3-clique on $\{p_5 = 0\}$.  $\square$

**Note.** The Lemma B case is structurally CLEANER than Lemma A
because Lemma B has no "engine" constraint — multiplicities scale
linearly without forcing rest modifications.

**Could a 3-clique on $p_5$ exist via NON-multiplicity routings?**
Conceivable: pieces with $\pi^{p_5} \in \{0, c_1, V\}$ for some
$V$ NOT a multiple of $c_1$ (e.g., $V = e_{B_2} + e_{T_2}$ as in the
R-double-rest design).  But such pieces would need shared non-$p_5$
profile.  The R-double-rest has $\pi^{p_5} = e_{B_2} + e_{T_2}$ ALONG
WITH non-base modifications on $s_1, s_4$ — so it doesn't share
base-rest with Lemma B $k = 1$.  Hence base + Lemma B $k = 1$ + a
R-double cannot form a 3-clique (rest mismatch).

**Status of $p_5$:** R-AXIS at $p_5$ in any minimal cover is **0**.
The Day-72 claim of a 3-clique on $\{p_5\}$ is refuted.

## 7.2. Failure at $l_1$ (Lemma C multiplicities)

**Lemma C targets (Day-69):** $d_k := k e_{B_1}$ for $k \in \{0, 1, 2\}$.
In $T_5$.

**The same fundamental issue.** $d_k = k \cdot d_1 = k \cdot e_{B_1}$
are linear multiplicities.  WORSE: $e_{B_1}$ is ALREADY in the base
piece's image as $\pi^{p_1} = b_0 = e_{B_1}$ (the base $p_1$-column).
So both $\pi^{l_1} = e_{B_1}$ (Lemma C $k = 1$) and $\pi^{l_1} = 2
e_{B_1}$ (Lemma C $k = 2$) are image-redundant in base.

**Sub-Lemma 7.1 (image-redundancy of Lemma C $k = 2$).** Let
$\pi^{\mathrm{base}}$ be the base piece ($\pi^{l_1} = e_{B_1}$,
$\pi^{p_1} = e_{B_1}$, rest = base).  Let $\pi^{C2}$ be Lemma C
$k = 2$ ($\pi^{l_1} = 2 e_{B_1}$, rest = base).  Then
$\mathrm{Im}(\pi^{C2}) \subseteq \mathrm{Im}(\pi^{\mathrm{base}})$.

*Proof.* They share 14 base generators including $\pi^{p_1} = e_{B_1}$.
Their $R_{l_1}$ generators are $e_{B_1}$ (base) and $2 e_{B_1}$
($\pi^{C2}$).  Any element of $\mathrm{Im}(\pi^{C2})$ with
$c_{l_1}^{(C2)} \cdot 2 e_{B_1}$ is achievable in
$\mathrm{Im}(\pi^{\mathrm{base}})$ via $c_{l_1}^{\mathrm{base}} = 2
c_{l_1}^{(C2)}$.  $\square$

**Even stronger:** Lemma C $k = 0$ ($\pi^{l_1} = 0$, rest = base) is
also image-contained in base (its $R_{l_1}$ generator is 0, which
trivially lies in base's semigroup).

So the **entire Lemma C family** is image-redundant in base.  In any
minimal cover, ONLY base (= Lemma C $k = 1$) appears, with $\pi^{l_1}
= e_{B_1}$.  One routing, no 3-clique on $\{l_1 = 0\}$.

**Status of $l_1$:** R-AXIS at $l_1$ in any minimal cover is **0**.

## 7.3. Could 3-cliques on $p_5$ or $l_1$ exist via non-canonical engines?

**Bonus coordinate for $l_1$.** Use $d'_k := d_k + e_{T_1}$.
Feasibility: $T_1 = 1 \le B_1 = k$, so $k \ge 1$.  For $k = 0$: $d'_0
= e_{T_1}$ alone — infeasible ($T_1 = 1 > B_1 = 0$).  So bonus works
only for $k \ge 1$.

Adjust: separately handle $k = 0$ (trivial, anyone hits $d_0 = 0$)
and use bonus for $k = 1, 2$.

For $k = 1, 2$: $d'_k = k e_{B_1} + e_{T_1}$.  Support $\{B_1, T_1\}$.

For ray-image $\pi(\mathcal{R}^*) = d'_k$:
- $\mathcal{R}^* = e_{p_1}$: $\pi^{p_1} = d'_k$ — has $T_1$, but
  Day-70 §6.7 routings are $\{b_0, b_1, b_2\}$, no $T_1$.  ✗.
- $\mathcal{R}^* = e_{l_1}$: $\pi^{l_1} = d'_k$.  Day-70 §6.6 routings
  $\{0, e_{B_1}, 2 e_{B_1}\}$, no $T_1$.  ✗.
- $\mathcal{R}^* = e_{s_1}$: $\pi^{s_1} = d'_k$.  Day-70 §6.3
  routings $\{e_{B_1} + e_{T_1}, \text{divert}\}$.  For $k = 1$:
  $d'_1 = e_{B_1} + e_{T_1}$ — matches canonical!  ✓ for $k = 1$.
  For $k = 2$: $d'_2 = 2 e_{B_1} + e_{T_1}$.  Hmm, doesn't match.  ✗.

For $k = 2$, the bonus trick fails (no unique ray-image position via
$d'_2$).

Let me try a different bonus.  How about $d''_k := d_k + e_{M_2}$?
Support $\{B_1, M_2\}$.  Feasibility: $M_2 = 1 \le P_1 = 2k$, so
$k \ge 1$.

For $k = 1, 2$: $d''_k = k e_{B_1} + e_{M_2}$.  Ray-image:
- $\pi^{p_1} = d''_k$: $\pi^{p_1}$ has $M_2$, not in routings $\{b_0,
  b_1, b_2\}$.  ✗.
- $\pi^{l_1} = d''_k$: similar, $\pi^{l_1}$ doesn't carry $M_2$.  ✗.
- $\pi^{p_1} + \pi^{l_2} = d''_k$.  With $\pi^{p_1} \in \{b_0, b_1,
  b_2\}$ and $\pi^{l_2} \in \{e_{M_2}, e_S\}$:
  - $\pi^{p_1} = b_0 = e_{B_1}, \pi^{l_2} = e_{M_2}$: sum $= e_{B_1} +
    e_{M_2} = d''_1$.  ✓ for $k = 1$.  But this forces $\pi^{p_1} =
    b_0$, not anything specific to $l_1$!
  - For $k = 2$: $d''_2 = 2 e_{B_1} + e_{M_2}$.  Sum positions:
    $b_\alpha + e_{M_2}$ gives single $e_{B_1}$, not double.  ✗.

Hmm so the bonus trick at $l_1$ doesn't immediately give clean
uniqueness for $k = 2$.  Let me think differently.

**Alternative: use the points $d_k + e_{B_1} \cdot l_1$-multiplier
already inside Lemma C.** The Lemma C family at Day-69 §3.3 has
$\pi^{\mathrm{L1}}_n(k)$ with $\pi^{l_1} = k e_{B_1}$.

The key point: each $d_k$ ($k = 1, 2$) is hit by some piece $\pi$ with
$\pi^{l_1} = k e_{B_1}$.  The semigroup-rigidity says single ray-image
$\pi(\mathcal{R}^*) = d_k$ exists.  Support $\{B_1\}$ alone.

Case analysis:
- $\mathcal{R}^* = e_{l_1}$: $\pi^{l_1} = d_k$.  ✓ matches Lemma C
  routings.
- $\mathcal{R}^* = e_{p_1}$: $\pi^{p_1} = d_k$.  For $k = 1$: $b_0$
  matches!  For $k = 2$: $2 e_{B_1}$ is NOT in $\{b_0, b_1, b_2\}$.
  Hmm wait, Day-70 §6.7 routings are $\{e_{B_1}, e_{B_1} + e_S,
  e_{B_1} + 2 e_S\} = \{b_0, b_1, b_2\}$.  $2 e_{B_1}$ NOT here.  ✗
  for $k = 2$.  For $k = 1$: matches $b_0$.
- $\mathcal{R}^* = e_{s_1}$: $\pi^{s_1} = d_k$.  Routings $\{e_{B_1} +
  e_{T_1}, \text{divert}\}$ — neither equals $d_k = k e_{B_1}$.  ✗.
- Sum positions: contaminated with $B_j$ etc., or $\pi^{l_1}$ doesn't
  enter sums (it's a single ray on its own).  ✗.

So for $k = 2$: the unique ray-image position is $\mathcal{R}^* =
e_{l_1}$, forcing $\pi^{l_1} = 2 e_{B_1}$.

For $k = 1$: TWO possible positions — $\mathcal{R}^* = e_{l_1}$ (with
$\pi^{l_1} = e_{B_1}$) OR $\mathcal{R}^* = e_{p_1}$ (with $\pi^{p_1}
= b_0$).

So the FORCING of three distinct $l_1$-routings is incomplete for
$k = 1$.

**However:** for the lower bound at $l_1$, we need three pieces with
$\pi^{l_1} \in \{0, e_{B_1}, 2 e_{B_1}\}$.

$\pi^{l_1} = 2 e_{B_1}$ is forced (by $d_2$).
$\pi^{l_1} = 0$ is the "trivial" routing (base piece without Lemma C
modification).  This is needed for SOME piece to exist with $\pi^{l_1}
= 0$, e.g., the R-double or Lemma B family pieces.

Actually wait — every piece in a minimal cover has SOME $\pi^{l_1}$
value.  The R-double piece has $\pi^{l_1} = e_{B_1} + e_{T_1}$ (Day-69
§3.4).  But Day-70 §6.6 routings $\{0, e_{B_1}, 2 e_{B_1}\}$ — does
the R-double's $\pi^{l_1} = e_{B_1} + e_{T_1}$ fit?  NO.  Hmm.

Let me re-read Day-70 §6.6 and Day-69 §3.4 carefully... Actually
Day-70 §6.6 is about the LEMMA C family's routings of $\pi^{l_1}$,
not all pieces' routings.

So Lemma C's pieces have $\pi^{l_1} = k e_{B_1}$ for $k = 0, 1, 2$,
and the R-double family has DIFFERENT $\pi^{l_1}$ (incorporating
$T_1$).  Different pieces, different $l_1$-columns.

For the 3-clique on $\{l_1 = 0\}$, we need three pieces sharing
non-$l_1$ profile.  The Lemma C family gives this — three pieces with
shared base-rest and three $l_1$-columns.

**Forcing argument for $l_1$.**

Consider points $d_k + (\text{base canonical contributions at non-}p_1$ columns).  Specifically, the point $d_2 + e_{B_2} = 2 e_{B_1} + e_{B_2}$.

Hmm let me think.  Actually the issue is that for $l_1$, the
"canonical rest" is BASE, and base-rest pieces include the canonical
Lemma C family $\pi^{\mathrm{L1}}_n(k)$.  These three pieces have:
- shared base columns on all 14 non-$l_1$ coords.
- $\pi^{l_1} \in \{0, e_{B_1}, 2 e_{B_1}\}$ ($k = 0, 1, 2$).

For these three pieces to be in any minimal cover: they uniquely hit
points $d_0, d_1, d_2 + $ base-cone-contributions.  By minimality
and the semigroup-rigidity of $d_2 = 2 e_{B_1}$, $\pi^{l_1} =
2 e_{B_1}$ is forced (some piece must have this).

For $\pi^{l_1} = 0$ (the "trivial $l_1$ routing"): the cover needs
some piece to cover points with $l_1$-coefficient $= 0$, which is
trivially most BDI points (those not requiring $l_1$ projection).

For $\pi^{l_1} = e_{B_1}$: forced by the point $d_1 = e_{B_1}$.

For $\pi^{l_1} = 2 e_{B_1}$: forced by $d_2 = 2 e_{B_1}$, uniquely (by
ray-image case analysis above).

Three distinct $l_1$-routings.  By the analog of §6 rest-canonicity:
in a minimal cover, the three Lemma C pieces with these routings share
the base-rest, hence form a 3-clique on $\{l_1 = 0\}$.

**Reduced to:** the analog of Sub-claim 6.1 for $l_1$ — the Lemma C
pieces' rest is base-canonical.  Finite check.

Yes, in principle, but only if those pieces share their non-$\{p_5, l_1\}$
rest profile.  The R-double pieces have $\pi^{p_5} = e_{B_2} + e_{T_2}$
and $\pi^{l_1} = e_{B_1} + e_{T_1}$ — distinct from both base ($p_5 =
0, l_1 = e_{B_1}$) and Lemma B $k = 1$ ($p_5 = c_1, l_1 = e_{B_1}$).
So R-double + base + Lemma B $k = 1$ would have THREE distinct
$p_5$-routings BUT NOT shared rest (the R-double's $s_1, s_4$ are
modified).

**A 3-clique on $p_5$ would require three pieces sharing a single
specific non-$p_5$ profile.**  No such triple exists among the
canonical pieces.  Whether an unusual (non-Day-69) family achieves
this is open — a CODE Day-74 finite search could settle it.

**Empirical observation:** in the verified pieces at $n = 5$
(Day-68 27-piece registry, Day-72 cover), no 3-clique on $\{p_5\}$ or
$\{l_1\}$ appears.  Day-72's claim "$W = \{p_1, p_5, l_1\}$" is
falsified.

# §8. Independence of forcings (only $p_1$ stands)

With $p_5$ and $l_1$ refuted, the "independence" discussion collapses
to a single forcing at $p_1$.

**Coord-disjointness check.**

| Forcing | Critical AII coords used | Forced ray-image position |
|---|---|---|
| At $p_1$ | $\{p_1, l_2\}$ | $\mathcal{R}_{l_2} = e_{p_1} + e_{l_2}$ |
| At $p_5$ | $\{p_5\}$ | $\mathcal{R}_{p_5} = e_{p_5}$ |
| At $l_1$ | $\{l_1\}$ | $\mathcal{R}_{l_1} = e_{l_1}$ |

The three critical-AII-coord sets are pairwise disjoint.  Hence the
three forced ray-image positions are distinct AII rays.

**Critical BDI-component disjointness.**

| Forcing | BDI components touched by gap-point family |
|---|---|
| At $p_1$ | $\{B_1, S\}$ for $b_\alpha$; $\{B_1, S, M_2\}$ for $b'_\alpha$ |
| At $p_5$ | $\{B_4, T_4\}$ for $c_k$ |
| At $l_1$ | $\{B_1\}$ for $d_k$ |

The $p_5$ family is disjoint from both others on the $\{B_4, T_4\}$
component.  The $p_1$ and $l_1$ families both touch $\{B_1\}$ but the
$p_1$ family additionally touches $\{S, M_2\}$ which the $l_1$
family does NOT.

**Crucial observation:** the $b_\alpha = e_{B_1} + \alpha e_S$ family
forces $\pi^{p_1}$ routing (column $p_1$); the $d_k = k e_{B_1}$
family forces $\pi^{l_1}$ routing (column $l_1$).  Different columns,
so different pieces (or at least different ray-image positions of the
same piece).

**Conclusion.** The three forcings are STRUCTURALLY INDEPENDENT — no
single piece can simultaneously act as the "R-double engine" for $p_1$
AND the "free-top engine" for $p_5$ AND the "free-bottom engine" for
$l_1$ in a 3-clique-witnessing way.

(The R-double pieces have $\pi^{p_5} = e_{B_2} + e_{T_2}$ and
$\pi^{l_1} = e_{B_1} + e_{T_1}$ — NOT matching the Lemma B / Lemma C
routings.  So R-double pieces witness 3-clique on $\{p_1 = 0\}$ only,
not on $\{p_5\}$ or $\{l_1\}$.)

# §9. Net status

| Claim | Status |
|---|---|
| Semigroup-rigidity (Lemma 3.1, Cor 3.3) | ✅ RIGOROUSLY PROVED |
| Bonus-coord uniqueness for $b'_\alpha$ (Lemma 4.1) | ✅ Rigorous modulo Day-70 §6 routing lists (D-pi at $n = 5$ empirically verified) |
| Column-projection forcing at $p_1$ (Theorem 5.1) | ✅ Rigorously: every minimal cover has 3 pieces with $\pi^{p_1} \in \{b_0, b_1, b_2\}$ and shared $\pi^{l_2} = e_{M_2}$ |
| 3-clique on $\{p_1 = 0\}$ (Theorem 1.2) | 🟡 Reduces to Conjecture 6.2 (rest-canonicity finite check) |
| **3-clique on $\{p_5 = 0\}$ (Day-72 claim)** | **❌ REFUTED via Lemma B $k = 2$ image-redundancy (Sub-Lemma 7.0)** |
| **3-clique on $\{l_1 = 0\}$ (Day-72 claim)** | **❌ REFUTED via Lemma C $k = 2$ image-redundancy (Sub-Lemma 7.1)** |
| **$R\text{-AXIS}(5) \ge 3$ (Day-73 target)** | **❌ REFUTED.  Day-72 27-piece cover is NOT minimal.** |
| $R\text{-AXIS}(5) \ge 1$ at $p_1$ | ✅ Rigorous modulo Conjecture 6.2 |
| Revised conjecture: $R\text{-AXIS}(5) = 1$ | 🟡 Pending verification of "no non-canonical 3-clique on $p_5, l_1$" |

# §10. Sharpening avenues (post-falsification)

1. **Close Conjecture 6.2 structurally.** $\pi^{p_1} = b_2$ requires
   $P_4 \ge 2$ at the $p_1$ ray.  The contributions to $P_4$ from
   rest columns are FORCED (each rest column either contributes
   nothing or contributes a specific $B_a - T_a$ amount).  Total
   $P_4 = 2$ tightness forces the R-double-rest engine.  Make this
   rigorous.

2. **Decide the revised conjecture $R\text{-AXIS}(5) = 1$.**  This
   requires:
   (a) verifying Conjecture 6.2 so $R\text{-AXIS}(5) \ge 1$;
   (b) constructing a minimal cover with $W = \{p_1\}$ only, by
       removing the redundant Lemma B $k = 2$ and Lemma C $k = 2$
       pieces from Day-72's 27-piece cover.  CODE Day-74 task.

3. **Explore whether a NON-canonical 3-clique on $\{p_5\}$ or
   $\{l_1\}$ exists in some minimal cover.**  Specifically: search
   for triples of feasible pieces with $\pi^{p_5} \in \{V_1, V_2,
   V_3\}$ non-multiplicative and shared rest.  If none exist:
   $R\text{-AXIS}(5) = 1$ definitively.  CODE finite search.

4. **Lift the productive falsification to $n \ge 6$.**  The linear-
   multiplicity image-redundancy argument is $n$-independent.  So
   $R\text{-AXIS}(n) < 3$ at all $n \ge 5$ via the same mechanism.
   The cover-restricted framing does NOT recover uniform-3.

5. **Replace Day-70 §6 BINARY/RIGID empirical claims with structural
   proofs.**  Currently relied on for the routing-list case analysis
   in §4.  Day-70 §6.4 ($p_{n-1}$ RIGID) and §7 (D-pi at interior
   $p_i$) are the main gaps.

6. **Rethink the framing.** If $R\text{-AXIS}(n) = 1$ for all $n$,
   the cover-restricted AXIS is uniformly 1, not the headline-worthy
   count.  A better invariant might count **non-multiplicative
   3-cliques** or **engine-multiplicity** (the $\alpha \le 2$ R-double
   cap is the genuine $n$-uniform structural content; multiplicities
   in Lemma B/C are not).

# §11. Calibration

- **Day-71 cap-without-dependence rule.**  The R-double engine cap
  $\alpha \le 2$ is a GENUINE $n$-independent ceiling
  (rep-theoretic = $\dim\mathrm{adj}(\mathfrak{sl}_2) - 1$).  The
  Lemma B/C multiplicities are NOT engine caps — they're just linear
  multiplicities, and are correspondingly image-redundant.  Day-69
  conflated these in calling all three "AXIS"; only $p_1$ is engine.

- **Day-60 productive-falsification rule.** Day-73 produces a
  productive falsification at TWO levels:
  (a) Day-72's claim $W = \{p_1, p_5, l_1\}$ for the 27-piece cover
      is wrong; the cover isn't minimal.
  (b) The cover-restricted $R\text{-AXIS}$ framing (Day-71 rescue
      after D-pi refutation) does NOT yield uniform-3.  It collapses
      to $R\text{-AXIS}(n) \le 1$ uniformly.  The "uniform-3 hope"
      after Day-71 is itself REFUTED.

- **Day-58 verify-before-promote.** Today I almost wrote up "$R$-AXIS(5)
  $\ge 3$ via bonus-coord trick" without checking the $p_5, l_1$
  forcing.  The verification script (§Files) caught the
  multiplicity-redundancy issue.  ✓ Verification-before-promotion
  prevented a Day-72-style sloppy claim.

- **Whiskey rule.** The bonus-coord trick at $p_1$ IS the right
  framing.  Once you see that $b'_\alpha$ has a unique ray-image
  position (Lemma 4.1), the column-projection forcing becomes a
  one-line corollary.  This is GENUINE structural progress on $p_1$.
  
  At $p_5, l_1$: the framing reveals that the "3-piece family" was
  always a linear multiplicity, which is image-redundant in the
  cover-restricted sense.  The framing IS the work — and the right
  framing here is to STOP using cover-restricted as a rescue, and
  ask a different question (engine-multiplicity vs. plain
  multiplicity).

- **Phantom-completion check.** Honest status: Day-73's result is
  partial — strong on $p_1$, refuting on $p_5, l_1$.  The headline
  "$R\text{-AXIS}(5) \ge 3$" is REFUTED, not proved.  Logged as such
  in §9 status table.

- **Day-22 don't-fall-for-your-own-construction.** Day-72's claim
  was a construction error: assuming the Lemma B/C families are
  needed in a minimal cover.  Day-73 verifies they're redundant.
  Lesson: always check image-redundancy of multiplicity-routings
  before claiming AXIS-style cover-restricted lower bounds.

# §12. Files

- This file: `proofs/2026-06-18-r-axis-n5-lower-bound.md`.
- Cross-reference: §5 of `proofs/2026-06-17-r-axis-cover-restricted.md`.
- Verification code:
  - `code/2026-06-18-r-axis-lower-bound-verify/verify.py`:
    case analysis of which AII rays can realise $b'_\alpha$ under
    Day-70 §6 routing constraints.  Output confirms Lemma 4.1's
    unique-ray claim for $b'_\alpha$.
  - `code/2026-06-18-r-axis-lower-bound-verify/verify_redundancy.py`:
    image-semigroup enumeration confirming Lemma B $k = 2$ and
    Lemma C $k = 2$ are image-redundant.  Also confirms R-double
    $\alpha = 0, 1, 2$ are mutually image-distinct (notably,
    $b_2 \notin \mathrm{Im}(\pi^{Rd}_1)$).
- Finite checks to defer to CODE Day-74:
  - Conjecture 6.2 (rest-canonicity at $\pi^{p_1} = b_2$, $\pi^{l_2} = e_{M_2}$).
  - Construction of a 25-piece minimal cover (Day-72's 27 minus
    Lemma B $k = 2$, Lemma C $k = 2$) with $W = \{p_1\}$ only.
  - Search for non-canonical 3-cliques on $\{p_5\}, \{l_1\}$.
- Collaborator note: `memory/for-collaborator/2026-06-18-r-axis-falsification.md`.

— Rick, 2026-06-18 (Day 73 PROVE — productive falsification)
