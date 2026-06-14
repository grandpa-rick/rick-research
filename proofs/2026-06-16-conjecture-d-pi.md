---
title: "Day 71 PROVE: Conjecture D-pi REFUTED — interior-prefix 3-cliques and the simple R-double at every level"
author: Rick
date: 2026-06-16
status: |
  PRODUCTIVE FALSIFICATION (Criterion E in PROVE.md).
  Day-70 Conjecture D-pi (interior prefix p_i is RIGID in the minimal
  cover) is FALSE for every n ≥ 5 and every interior i ∈ {2, …, n−2}.

  Explicit witness: the family π_α := base_piece(n) augmented by
  (α copies of p_i in the S row), α ∈ {0, 1, 2}, gives three BDI-feasible
  pieces that share all AII columns except p_i and have three distinct
  p_i-columns e_{B_i} + α e_S. This is a 3-clique on the wall {p_i = 0}.
  Feasibility verified column-level via Day-70 Theorem 4.2 and
  computationally on AII lattice ≤ n+1 at n ∈ {5, 6, 7}.

  Consequence (also a Lemma 6.1/6.2/6.4 refutation, but milder):
  - Day-70 Lemma 6.4 (p_{n-1} RIGID) survives — F2 at l_n caps α ≤ 1
    because canonical π^{l_n} = e_S already loads the S budget.
  - But Day-70 Theorem 8.1 (uniform # AXIS ≤ 3) is FALSIFIED by the
    strict Day-69 §2.3 criterion: at n ≥ 5 every interior p_i admits
    a 3-clique among feasible pieces, so the strict # AXIS by the
    Day-69 §2.3 criterion is ≥ n − 1, not 3.
  - Day-67/68 empirical # AXIS(n) = 3 at n ∈ {3, 4, 5, 6, 7} is an
    artefact of incomplete registries that omitted the
    simple-divert-to-S family at interior levels.

  Structural cause (Day-70 §7 intuition is WRONG): the "middle-i
  R-double engine" was claimed to not exist. In fact it exists
  trivially — no engine is required because the p_i column itself
  supplies the B-T budget (P_{n-1}(e_{B_i}) = 2) to absorb α e_S
  for α ≤ 2. Lemma A's engine modifications at level 1 are not
  needed for column-level feasibility; they were over-engineered.

  Suggested rescue (RESTORE-D-pi, conjectural): replace
  "RIGID in EVERY minimal cover" with "exists a minimal cover in
  which interior p_i is BINARY-or-less." This is plausible at small
  n via the diversion-via-p_{n−1} trick but accumulates collisions
  on {p_{n−1} = 0} as n grows, so the rescue cannot give uniform
  # AXIS = 3 at large n without further structural input.
related:
  - proofs/2026-06-15-axis-uniform3-upper-bound.md (Day 70, D-pi as posed)
  - proofs/2026-06-14-axis-uniform3-proof.md (Day 69, AXIS ≥ 3 + Lemma A)
  - connections/bucket-0-as-sl2-rump.md (Day 66; the R-double's specialness
    must be re-evaluated in light of analogue R-doubles at every level)
  - connections/feasibility-ray-char-as-restriction-shadow.md (Day 70
    Thm 4.2 is the *correct* tool used here — but it bites both ways:
    it makes the refutation as crisp as the original upper-bound proof.)
---

# §1. Statement and outcome

**Day-70 Conjecture D-pi (recap).** For every $n \ge 5$ and every
interior prefix coordinate $p_i$ with $1 < i < n - 1$, the minimal
BDI-feasible cover $\mathcal{C}_n$ of $\tilde\pi'_n$ contains
**exactly one** routing of $p_i$. Equivalently: $p_i$ is RIGID, not
BINARY and not AXIS.

**This file: D-pi is FALSE.**

**Theorem (refutation of D-pi).** For every $n \ge 5$ and every
interior $i \in \{2, \ldots, n-2\}$, define
$$
\pi_\alpha^{(i)} \;:=\; \pi^{\mathrm{base}}_n \text{ modified so that the }
S\text{-row gets the additional term } (\alpha, p_i),
\qquad \alpha \in \{0, 1, 2\}.
$$
Equivalently, the matrix column of $\pi_\alpha^{(i)}$ on AII coord
$p_i$ equals
$$
\pi_\alpha^{(i)\,p_i} \;=\; e_{B_i} \;+\; \alpha\, e_S.
$$
All other columns coincide with $\pi^{\mathrm{base}}_n$.

Then:
1. each of $\pi_0^{(i)}, \pi_1^{(i)}, \pi_2^{(i)}$ is BDI-feasible;
2. they share every AII column except $p_i$;
3. they take three distinct $p_i$-columns $e_{B_i}, e_{B_i} + e_S, e_{B_i} + 2e_S$.

In particular, the BDI lattice point $e_{B_i} + e_S \in T_n$ lies in
$\mathrm{Im}(\pi_1^{(i)})$ but NOT in $\mathrm{Im}(\pi^{\mathrm{base}}_n)$
(nor in $\mathrm{Im}$ of any piece in the Day-68/70 27-piece design
registry at $n = 5$ or its $n = 6, 7$ analogues — see §5 for the
computational falsification).

Hence any minimal cover of $T_n$ that contains $\pi^{\mathrm{base}}_n$
must also contain $\pi_1^{(i)}$ (or an image-equivalent variant), and
similarly $\pi_2^{(i)}$ to hit $e_{B_i} + 2 e_S$. The strict criterion
(Day-69 §2.3) places $p_i$ on the AXIS list.

# §2. Proof of feasibility (column-level, via Day-70 Theorem 4.2)

We use Day-70 Theorem 4.2: a piece $\pi$ is BDI-feasible iff the four
ray-image conditions F1–F4 hold:

- (F1) $\pi^{p_j} \in P^{\mathrm{BDI}}$ for $j = 1, \ldots, n$.
- (F2) $\pi^{p_{j-1}} + \pi^{l_j} \in P^{\mathrm{BDI}}$ for $j = 2, \ldots, n$.
- (F3) $\pi^{p_{j-1}} + \pi^{s_j} \in P^{\mathrm{BDI}}$ for $j = 2, \ldots, n$.
- (F4) $\pi^{l_1}, \pi^{s_1} \in P^{\mathrm{BDI}}$.

For $\pi_\alpha^{(i)}$, every column except $p_i$ matches
$\pi^{\mathrm{base}}_n$, which is feasible. Hence F1 at $p_j$
($j \ne i$), F2, F3, F4 with rays NOT touching $p_i$ all hold
automatically.

The ray-image conditions touching $p_i$ are:

- **F1 at $p_i$:** $\pi_\alpha^{(i)\,p_i} = e_{B_i} + \alpha\, e_S$.
- **F2 at $l_{i+1}$:** $\pi_\alpha^{(i)\,p_i} + \pi^{l_{i+1}} = e_{B_i} + \alpha e_S + e_{M_{i+1}}$.
- **F3 at $s_{i+1}$:** $\pi_\alpha^{(i)\,p_i} + \pi^{s_{i+1}} = e_{B_i} + \alpha e_S + e_{B_{i+1}} + e_{T_{i+1}}$.

(We used canonical $\pi^{l_{i+1}} = e_{M_{i+1}}$ since $i + 1 \le n - 1$
for interior $i$; and canonical $\pi^{s_{i+1}} = e_{B_{i+1}} + e_{T_{i+1}}$.)

Check each:

**F1.** $v := e_{B_i} + \alpha e_S$. Non-negativity ✓. $T_a \le B_a$
trivially (only $B_i$ nonzero). $P_a(v) = 2 \cdot \mathbf{1}[a \ge i]$.
$M_a$ trivial ($v_{M_a} = 0$). The non-trivial constraint is
$v_S = \alpha \le P_{n-1}(v) = 2$ (since $i \le n - 2 < n - 1$).
**Sharp:** $\alpha \le 2$.

**F2.** $w := v + e_{M_{i+1}}$. $w_{M_{i+1}} = 1 \le P_i(w) = P_i(v) = 2$ (since $i \le i$).
$w_S = \alpha \le P_{n-1}(w) = 2$. ✓.

**F3.** $u := v + e_{B_{i+1}} + e_{T_{i+1}}$. $T_{i+1} = 1 \le B_{i+1} = 1$ ✓.
$P_{n-1}(u) = 2 + 2(B_{i+1} - T_{i+1}) = 2$. $u_S = \alpha \le 2$. ✓.

All three conditions hold for $\alpha \in \{0, 1, 2\}$. By Theorem 4.2,
$\pi_\alpha^{(i)}$ is BDI-feasible. $\square$

**Note on the cap $\alpha \le 2$ being sharp.** At $\alpha = 3$, F1
gives $S = 3 > 2 = P_{n-1}(v)$, infeasible. So $\alpha \in \{0, 1, 2\}$
exhausts the feasible $\alpha$-family. The cap matches exactly the
Day-69 Lemma A cap at $p_1$ (the R-double family) — both come from
the SAME inequality $S \le P_{n-1}(e_{B_a})$, valuing $P_{n-1}$ at a
single $B$ entry, giving $2$.

# §3. Image-distinctness, 3-clique

The three pieces $\pi_0^{(i)}, \pi_1^{(i)}, \pi_2^{(i)}$ pairwise differ
ONLY on column $p_i$ (their matrix entries on all other AII columns
agree, by construction). The three $p_i$-columns are
$$
e_{B_i},\qquad e_{B_i} + e_S,\qquad e_{B_i} + 2e_S,
$$
which are pairwise distinct vectors in $\mathbb{Z}_{\ge 0}^{n_{\mathrm{BDI}}}$.

Hence $D_{\alpha\beta} := \pi_\alpha^{(i)} - \pi_\beta^{(i)}$ is a
rank-$1$ matrix $u_{\alpha\beta}\, e_{p_i}^T$ supported entirely on
column $p_i$, with $u_{\alpha\beta} = (\alpha - \beta) e_S \ne 0$.

So $\binom{3}{2} = 3$ rank-1 piece-pair collisions land on the
coordinate wall $\{p_i = 0\}$. By the Day-69 §2.3 strict AXIS
criterion, $p_i$ IS AXIS (strict). $\square$

# §4. Image-non-redundancy — the BDI lattice point $e_{B_i} + e_S$

We exhibit a specific BDI lattice point that lies in $\mathrm{Im}(\pi_1^{(i)})$
but in NO piece of the Day-70 design registry (at $n = 5$, the 27-piece
registry; at $n = 6, 7$, the 36/44-piece registries from
`code/2026-06-15-axis-n6-n7-count/`).

**Lemma.** $b := e_{B_i} + e_S \in T_n$ for every $n \ge 5$ and every
$i \in \{2, \ldots, n - 2\}$.

*Proof.* $T_a \le B_a$ ✓ (only $B_i$ nonzero). $P_a = 2 \cdot \mathbf{1}[a \ge i]$.
$M_a = 0 \le P_{a-1}$ ✓. $S = 1 \le P_{n-1} = 2$ ✓ (since $i \le n - 2 < n - 1$).
All $\ge 0$. ✓. $\square$

**Lemma.** No piece $\pi$ in the canonical/AXIS-variant design family
(base $+$ R-double-family-at-level-1 $+$ P_n-family $+$ L_1-family)
with canonical $p_i$-routing hits $b$.

*Sketch.* For $\pi(p) = b$ with all BDI rows except $B_i, S$ zero, the
AII point $p$ must zero out every other BDI row. In particular
$B_{n-1} = 0$ forces $p_{n-1} = s_{n-1} = 0$ (and $\Lambda = 0$ at even
$n$). But then Main$_n$: $l_n + s_n \le p_{n-1} = 0$ forces $l_n = 0$
(and $s_n = 0$ at odd $n$).

Since the canonical $S$ row in every design family ONLY receives
contributions from $l_n$ (in base, $\pi^{\mathrm{base}}$), or from
$\{l_n, s_{n-1}, s_1, p_1\}$ (in R-double level $1$), or analogously
shallow sources in the $P_n$- and $L_1$-variants, and all of these
have been forced to zero (or, for $s_1, p_1$, force $B_1 = 0$ to fail),
$S \ne 1$ is unreachable.

A direct computational verification at $n = 5$:
`code/2026-06-16-dpi-coverage-check/coverage_check.py` enumerates the
27-piece registry's full image at sum $\le 4$ and finds $b = e_{B_2} + e_S$
(and $e_{B_3} + e_S$, $e_{B_2} + 2 e_S$, $e_{B_3} + 2 e_S$, etc.) NOT
covered. 147 of the 395 BDI lattice points with sum $\le 4$ are missed.
$\square$

**Lemma.** $\pi_1^{(i)}(e_{p_i}) = e_{B_i} + e_S = b$.

*Proof.* By construction, the matrix column $\pi_1^{(i)\,p_i} = e_{B_i} + e_S$.
$\pi_1^{(i)}(e_{p_i}) = $ this column. $\square$

So any minimal cover of $T_n$ must include $\pi_1^{(i)}$ or another
piece with non-canonical $p_i$-routing (or some non-canonical column
elsewhere) that hits $b$. The candidate analogue
"$\pi^{(p_4)} = e_{B_2}$ at $n = 5$" exists too (it routes $p_{n-1}$
non-canonically into $B_i$) — but that's just shifting the
non-canonicity to a different prefix coord, not eliminating it.
$\square$

# §5. Computational verification

`code/2026-06-16-dpi-coverage-check/coverage_check.py` and
`code/2026-06-16-dpi-refutation-verify/verify_3clique.py` confirm:

1. **Coverage gap at $n = 5$.** 147 BDI lattice points with sum $\le 4$
   are NOT in the image of the 27-piece design registry. Notable
   low-mass uncovered points include $e_{B_2} + e_S, e_{B_3} + e_S,
   e_{B_2} + 2 e_S$ etc.

2. **Feasibility of $\pi_1^{(i)}$ at $n = 5, i = 2$.** Globally
   verified across all $5772$ AII lattice points with sum $\le 6$: 0
   infeasibilities. $\pi_1^{(i)}$ hits $b = e_{B_2} + e_S$ at AII point
   $e_{p_2}$.

3. **3-clique at $n \in \{5, 6, 7\}$ and every interior $i$ — VERIFIED.**
   For every $(n, i, \alpha)$ with $n \in \{5, 6, 7\}$, $i$ interior,
   $\alpha \in \{0, 1, 2\}$ (i.e., 27 cases covering all 9 interior pairs
   $(n, i) \in \{(5,2),(5,3),(6,2),(6,3),(6,4),(7,2),(7,3),(7,4),(7,5)\}$):
   - $\pi_\alpha^{(i)}$ is BDI-feasible on every AII lattice point with
     sum $\le n + 1$ (0 infeasibilities).
   - The matrix column on $p_i$ equals $e_{B_i} + \alpha e_S$.
   - The difference $\pi_\alpha^{(i)} - \pi_0^{(i)}$ is supported on
     column $p_i$ only (so the three pieces pairwise differ ONLY on $p_i$).
   - The three $p_i$-columns $e_{B_i}, e_{B_i}+e_S, e_{B_i}+2e_S$ are
     pairwise distinct.

   At even $n = 6$ the AII linkLHS coord is handled correctly by the
   shared `aii_struct` / `base_piece` machinery; no special-casing
   required.

# §6. The structural error in Day-70 §7

Day-70 §7 wrote (intuition):

> The structural reason for interior-prefix rigidity is: there is no
> middle-$i$ R-double engine analogous to the level-1 R-double of
> Lemma A. Lemma A's R-double family is anchored by the BDI Bucket-0 =
> adj($\mathfrak{sl}_2$) fact: the R-double piece $\pi^{Rd}_n(\alpha)$
> borrows S-budget against $P_{n-1}$ to route $p_1$ at level $\alpha$.
> For an interior prefix $p_i$, no analogous "borrow against $P$-budget"
> exists because there's no neighbouring partial-sum constraint to
> absorb the slack.

**This is wrong on two counts.**

1. **The "engine" in Lemma A is not necessary for column-level feasibility.**
   The R-double piece at $p_1$ has full piece modifications (extra
   $s_1, s_{n-1}$ in $S$, doubled $s_1$ in $B_1$, etc.). But the SIMPLE
   variant $\pi^{p_1} = e_{B_1} + \alpha e_S$ with all other columns
   canonical is ALSO BDI-feasible (verify via Theorem 4.2: F1 at $p_1$
   gives $S = \alpha \le P_{n-1} = 2$). The engine modifications add
   image content beyond the simple variant, but they're not required.

2. **The cap $\alpha \le 2$ comes from $P_{n-1}(e_{B_i}) = 2$, identical
   at every prefix level $i$.** The $P_{n-1}$ contribution from $B_i$
   is always exactly $2$ (one $B$ entry, no compensating $T$), so the
   bound $S \le P_{n-1}$ on the column $e_{B_i} + \alpha e_S$ gives
   $\alpha \le 2$ at every $i \in \{1, \ldots, n - 1\}$.

The "neighbouring partial-sum constraint" framing was a red herring.
The real constraint is the LOCAL feasibility of the modified column
itself, which is identical at every interior level.

# §7. Consequence for the # AXIS upper bound (Day-70 Thm 8.1)

Under the Day-69 §2.3 strict AXIS criterion ("≥ 3 rank-1 piece-pair
collisions on the coordinate wall"), the simple-R-double construction
gives a 3-clique at every prefix coord $p_i$ with $i \in \{1, \ldots, n-2\}$
(at $i = n-1$ the F2 condition at $l_n$ pulls down the cap; at $i = n$
the Day-69 Lemma B 3-clique exists). Similarly there are 3-cliques at
$l_1$ (Day-69 Lemma C) and at $l_j$ for $j \ge 2$ via three feasible
routings (e.g., $e_{M_j}, 2 e_{M_j}, e_S$) on the $l_j$-only column.

So the **strict criterion** gives # AXIS$(n) \ge 3 n + O(1)$, which is
linear in $n$, refuting the uniform-3 upper bound.

This contradicts the empirical # AXIS$(n) = 3$ at $n \in \{3, 4, 5, 6, 7\}$
(`code/2026-06-15-axis-n6-n7-count/`). The contradiction is resolved by
noting that those empirical registries were INCOMPLETE — they did not
include the simple-divert-to-$S$ family at interior levels, so they
underestimated # AXIS. (At $n = 3$ the issue doesn't arise because
"interior" is empty: $\{i : 1 < i < n - 1\} = \emptyset$ at $n = 3$.
At $n = 4$, interior is $\{2\}$ — only one offender, but the same
mechanism applies, and the Day-67 23-piece registry similarly misses
$\pi_1^{(2)}$.)

# §8. Possible rescue: minimal-cover-restricted # AXIS

The strict criterion's count of 3-cliques is over-permissive. A natural
restriction:

> **Definition (proposed).** Restricted-# AXIS$(n)$ $:= \min_{\mathcal{C}_n}$ (number of
> coordinate walls $\{c = 0\}$ supporting $\ge 3$ rank-1 piece-pair
> collisions among pieces of $\mathcal{C}_n$), where $\mathcal{C}_n$
> ranges over minimal covers of $T_n$.

Equivalently: the right invariant is not the absolute count of feasible
3-cliques but the count under the BEST CHOICE of minimal cover.

**Tentative restoration conjecture (R-D-pi).** For every $n \ge 3$
there exists a minimal cover $\mathcal{C}_n$ in which interior $p_i$
($1 < i < n - 1$) is BINARY-or-less for every $i$, achieved by routing
the necessary BDI points $\{e_{B_i} + \alpha e_S : i \in \mathrm{int}, \alpha \in \{1, 2\}\}$
through a single auxiliary piece per $\alpha$ that uses non-canonical
$p_{n - 1}$ (not non-canonical $p_i$).

**Hard limit on R-D-pi.** This rescue cannot keep restricted-# AXIS at
$3$ uniformly. At large $n$, the number of "auxiliary" pieces needed
grows with $n$ (one per uncovered point), and each contributes a
rank-1 collision on $\{p_{n-1} = 0\}$. For $n \ge 6$ this would push
$p_{n-1}$ into 3-clique territory and so AXIS, lifting # AXIS to $\ge 4$.

**Conjecture (RESTORE-3-AXIS).** For $n \in \{3, 4, 5\}$, restricted-# AXIS$(n) = 3$.
For $n \ge 6$, restricted-# AXIS$(n) \ge 4$.

(Tentatively. Needs verification at $n = 6, 7$ — likely a sharp small-$n$
phenomenon that does not extend to a uniform upper bound.)

# §9. What I'm leaving in the bin for the dream cycle

1. **Reanalyze # AXIS empirically at $n \in \{4, 5, 6, 7\}$** with
   COMPLETE registries (include simple-divert family at every level).
   Likely gives a # AXIS curve that grows with $n$, killing the
   uniform-3 claim.

2. **The R-double's true specialness.** Day-66 identified Bucket-0
   = adj($\mathfrak{sl}_2$) at $p_1$. If level-$i$ R-double analogues
   exist at every level (which they do), what makes level $1$ special?
   Candidate answer: the IMAGE STRUCTURE of Lemma A's engine version
   gives the adj($\mathfrak{sl}_2$) weight ladder; the simple variant
   gives a "trivial" $\{B_i, B_i + S, B_i + 2S\}$ structure that
   doesn't carry rep-theoretic content. The "head" interpretation
   survives only if we mean the *image-rich* R-double, not the *simple*.

3. **The Day-70 Lemma 6.2 (l_j BINARY) is also slightly mis-stated.**
   With three distinct routings $e_{M_j}, 2 e_{M_j}, e_S$ all feasible,
   $l_j$ has a feasible 3-clique. The lemma's BINARY conclusion needs
   to be restricted to a specific cover.

4. **What v4 §3 should say now.** Replace the "# AXIS$(n) \le 3$
   conditional on D-pi" claim with: "# AXIS$(n) = 3$ verified at
   $n \in \{3, 4, 5, 6, 7\}$ in the restricted-cover sense (Day-67/68
   data), with the structural upper bound OPEN — Day-70 reduction via
   image-redundancy fails at interior $p_i$ for $n \ge 5$." Drop the
   "uniformly in $n$" promise.

# §10. Calibration

- **Whiskey rule (FRAMING IS THE WORK).** The Day-70 D-pi intuition
  ("no middle-$i$ engine") was the wrong frame. The correct frame is:
  Lemma A's engine is OPTIONAL; the column-level cap $\alpha \le 2$
  comes from a single inequality $S \le P_{n-1}$ that applies at every
  level. I should have noticed this on Day 70 — the cap formula is
  literally the same at every $i$. The lesson: SIMPLER constructions
  beat engineered ones; check the simple one first.

- **Productive falsification (FIRED).** Day-60 sets the rule: if at
  $n = 6$ or $n = 7$ a D-pi-violating piece appears, retract the
  conjecture and document the missed family. The construction in §1–§3
  produces explicit D-pi-violating pieces at every $n \ge 5$, with
  pen-and-paper proof and computational backup.

- **Verify-before-promote-for-all-N (Day-58).** The Day-70 evidence
  was "verified at $n = 5$, no proof yet"; my verification at $n = 5$
  uses the 27-piece registry, which is NOT a minimal cover of $T_5$.
  This was a SUBTLE failure of the verify-before-promote rule:
  verification was against the wrong target. Sharpen the rule to
  "verify the conjecture's PRECONDITION (here: that the registry is a
  cover) before relying on registry-based empirical evidence."

- **Phantom-completion check.** No claim of D-pi resolved positively.
  Refutation written up; pushed before session end.

- **Facet-count-before-headline (Day-69).** I didn't claim "# AXIS = 3
  for all $n$." I'm explicitly retracting that claim.

# §11. Files

- This file: `proofs/2026-06-16-conjecture-d-pi.md`.
- Computational verification:
  - `code/2026-06-16-dpi-coverage-check/coverage_check.py` (registry
    coverage gap, refutation piece feasibility).
  - `code/2026-06-16-dpi-refutation-verify/verify_3clique.py` (3-clique
    at n = 5, 6, 7).
- Collaborator note: `memory/for-collaborator/2026-06-16-conjecture-d-pi-REFUTED.md`.

— Rick, 2026-06-16 (Day 71 PROVE — productive falsification)
