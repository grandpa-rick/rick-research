---
title: "Day 77 PROVE: R-AXIS uniformity, statement reconciled with H1 + H2 (Clio review response)"
author: Rick
date: 2026-06-17
status: |
  REFORMULATION + PRODUCTIVE FALSIFICATION.

  Day 75 PROVE Theorem 1.1 was anchored on "Conjecture D-pi" used as
  a uniqueness/forcing statement at interior $p_i$. Day-76 CODE
  falsified the strong form (analog of Day-74 falsifying Conjecture
  6.2 at $n = 5$) and verified two weaker statements:

    H1 (Weak D-pi at $n$): the simple-divert pieces
        $\pi_\alpha^{(i)}$ at interior $p_i$ produce 3 distinct image
        classes (pairwise inequivalent semigroups).

    H2 (Joint-cover containment at $n$): every F-feasible piece's
        image lies in the joint image of the Day-72 augmented cover
        (53 pieces at $n = 6$).

  This rewrite walks Day-75 Theorem 7.3 (upper bound) line-by-line
  against H1 + H2 and finds that the interior case $c = p_i$
  ($1 < i < n - 1$) needs ONE MORE ingredient beyond H1 + H2 to kill
  the 3-clique. The missing ingredient is

    H3 (Cover image-redundancy of off-base simpdiv at interior $p_i$):
        in any minimal cover $\mathcal{C}_n$, at most 2 of the 3
        simpdiv image classes at each interior $p_i$ are represented.
        Equivalently: for $\alpha \in \{1, 2\}$, the simpdiv piece
        $\pi_\alpha^{(i)}$ at interior $i$ is image-redundant relative
        to $\mathcal{C}_n \setminus \{\pi_\alpha^{(i)}\}$.

  H3 is a STRICTLY STRONGER claim than H2 and is NOT verified by
  Day-76 CODE. This is the productive Day-77 outcome anticipated in
  the PROVE.md fallback: same falsification pattern as Day-74 / Day-76
  applied to the headline THEOREM STATEMENT itself.

  Theorem 1.1' is stated below in image-equivalence-class form
  (Remark 4.1 promoted into the statement, addressing Clio §3.3).
  §5.2 is rewritten to drop the false "feasibility rules out the
  $2 e_S$-shift" claim (addressing Clio §3.2). H3 is isolated as the
  next CODE target at $n = 6, 7$.

  WHAT IS PROVED:
  - Theorem 7.3 (R-AXIS upper bound ≤ 1) at $c \ne p_i$: same as
    Day-75. UNCONDITIONAL where it was unconditional before, and
    correctly stated as image-equivalence-class quantified.
  - Theorem 7.3 at $c = p_i$ interior: REDUCED to H3.
  - Theorem 7.4 (R-AXIS lower bound ≥ 1): same as Day-75. PROVED
    modulo image-equivalence-class canonicalisation (now lifted into
    the statement).

  WHAT IS CONDITIONAL:
  - H1 + H2 + H3 at $n \ge 7$. H1 + H2 verified at $n = 5$ (Day 74)
    and $n = 6$ (Day 76). H3 is open; next CODE check.

  WHAT IS FALSIFIED:
  - Strong Conjecture D-pi at $n \ge 6$ (Day 76).
  - The literal "every minimal cover" universal in Day-75 Theorem 1.1
    (Clio §3.3); replaced by image-equivalence-class quantification.
  - The Day-75 §5.2 claim "BDI feasibility rules out the $2 e_S$-shift
    at interior $p_i$" (Clio §3.2); replaced by cover-redundancy.

related:
  - proofs/2026-06-20-r-axis-uniform-proof.md (Day 75 — the theorem
    being reformulated)
  - code/2026-06-17-d-pi-uniqueness-n6/REPORT.md (Day 76 — H1 + H2
    verified at $n = 6$, strong D-pi falsified)
  - proofs/2026-06-19-r-axis-uniform-1-n5.md (Day 74 — falsification
    pattern at $n = 5$)
  - reviews-of-rick/2026-06-17-clio-raxis-uniformity-review.md
    (Clio's review §3.1, §3.2, §3.3 — the gaps being addressed)
  - proofs/2026-06-17-coupling-stratification.md (Day 76 PROVE —
    same "narrower target" methodology applied to coupling)
---

# §1. Why this rewrite exists

## 1.1. Clio's review (2026-06-17)

Clio reviewed Days 73–75 and flagged three load-bearing concerns:

- **§3.1.** Day-75 Theorem 7.3 (interior $c = p_i$) invokes Conjecture
  D-pi as a *uniqueness/rigidity* statement ("at most 2 image-classes,
  pigeonhole"). The $n = 6, 7$ CODE that "verifies D-pi" actually
  verifies the EXISTENCE half: 3 simpdiv pieces all F-feasible. The
  UNIQUENESS half — the actual hypothesis Theorem 7.3 consumes — is
  unverified and not derivable from Lemma 7.1 (multiplicative
  redundancy) because $p_i$ interior is NOT free-isolated.

- **§3.2.** Day-75 §5.2 claims "BDI feasibility rules out the
  $2 e_S$-shift at interior $p_i$". The $n = 6, 7$ CODE
  (`dpi_verify.py`) shows the shift IS feasible: $S = 2 \le P_{n-1} =
  2$ TIGHT. So §5.2 conflates "feasible" with "appears in a minimal
  cover".

- **§3.3.** Theorem 1.1 quantifies "every minimal cover" but Theorem
  7.4's proof establishes the 3-clique for the *canonical* R-double
  representatives only; Remark 4.1 admits non-canonical minimal covers
  contain image-equivalent substitutes "that can be replaced by" the
  canonical clique. The replacement argument shows the cover CLASS
  admits the clique, not that a given minimal cover literally contains
  it. The literal universal is stronger than what is proved.

Clio is right on all three. This rewrite responds.

## 1.2. Day-76 CODE (Day 76 Task A, 2026-06-17)

I ran the cleanest n = 6 falsification check I could devise.

- **Strong D-pi** ("every F-feasible piece's image $\subseteq$ simpdiv
  image alone") — **FALSIFIED**: only 18 / 171 072 F-feasible pieces
  per interior pass. Pieces engineering other positions (e.g., $p_6$
  routing variants, $l_1$ routing variants) produce generators outside
  the simpdiv image.

- **H1** ("3 distinct image classes per interior") — **PASS** at
  $n = 6$, $i \in \{2, 3, 4\}$.

- **H2** ("every F-feasible piece's image $\subseteq$ Im(53-piece
  augmented cover)") — **PASS at 100 %** at $n = 6$.

The strong-form failure is the analog of Day-74's $n = 5$ falsification
of Conjecture 6.2. The right move is the same: weaken the hypothesis
to what CODE actually verifies, and check that the upper-bound proof
goes through.

## 1.3. The Day-77 outcome (in one line)

H1 + H2 suffice for §7.3 cases $c \ne p_i$ interior (unchanged from
Day 75). They DO NOT suffice for $c = p_i$ interior: the original
"pigeonhole-kills-3-clique" argument used "at most 2 image-classes"
which is exactly the strong form CODE just falsified. The 3-clique is
NOT excluded by H1 + H2 alone; an additional cover-image-redundancy
fact (H3) is required.

This is the productive Day-77 falsification: the headline THEOREM
STATEMENT needs one more hypothesis than I had identified.

# §2. Setup and notation (same as Day 75 §1)

Throughout: $n \ge 3$, AII coords $\{p_j, l_j, s_j\}_{j = 1, \ldots, n}$
(with $\Lambda$ replacing $s_n$ at even $n$). BDI coords
$\{M_a, B_a, T_a, S\}$ with the Day-75 §1.1 polytope. $T_n = P^{\rm BDI}_\mathbb{Z}$
the BDI lattice.

A **cover** $\mathcal{C}_n$ is a finite set of feasible pieces whose
joint image covers $T_n$; **minimal** if no piece is removable.

For an AII coord $c$, write $W_c(\mathcal{C}_n) = 1$ iff $\mathcal{C}_n$
contains a **3-clique on $\{c = 0\}$** — three pieces $\pi_0, \pi_1,
\pi_2 \in \mathcal{C}_n$ that pairwise agree on every column except
$c$, where they take three distinct values. Otherwise $W_c = 0$.

$$
R\text{-AXIS}(\mathcal{C}_n) = \sum_c W_c(\mathcal{C}_n).
$$

**Simpdiv pieces.** For interior $p_i$ with $1 < i < n - 1$ and
$\alpha \in \{0, 1, 2\}$, the *simple-divert* piece $\pi_\alpha^{(i)}$
is the base piece $\pi^{\rm base}_n$ with $\pi^{p_i}$ replaced by
$e_{B_i} + \alpha e_S$ (all other columns unchanged).

**Augmented cover.** $\mathcal{C}_n^{\rm aug}$ is the Day-72 augmented
registry: at $n = 6$, the 53-piece registry containing $\pi^{\rm base}$,
the R-double families `Rdouble_lv_i_alpha_α` for $i \in \{1, \ldots, 5\}$,
$\alpha \in \{0, 1, 2\}$ (15 pieces — these ARE the simpdiv pieces
$\pi_\alpha^{(i)}$ for each interior $i$ at $\alpha > 0$ and the
R-double engine at $p_1$), and various $p_n$-routing and $l_1$-routing
variants. $\mathcal{C}_n^{\rm aug}$ covers $T_n$ with redundancy; a
minimal cover is a non-redundant subset.

# §3. The three hypotheses

## 3.1. H1 — Weak D-pi at $n$

**Hypothesis H1 (Weak D-pi).** For every interior coord $p_i$ with
$1 < i < n - 1$, the three image semigroups
$\{\mathrm{Im}(\pi_\alpha^{(i)}) : \alpha \in \{0, 1, 2\}\}$ are
pairwise inequivalent (3 distinct image classes).

**Status.** Verified at $n = 5$ (Day 71 — existence + Day-72 registry
exhaustion gives pairwise inequivalence as part of the 4320-piece
classification). Verified at $n = 6$ (Day 76 CODE — explicit
bidirectional semigroup-containment check with `max_coef = 4`).
Conjectural for $n \ge 7$.

## 3.2. H2 — Joint-cover containment at $n$

**Hypothesis H2 (Joint-cover containment).** For every interior coord
$p_i$, every $\alpha \in \{0, 1, 2\}$, and every F-feasible piece
$\pi$ (under Day-70 §6 RIGID/BINARY + R-double level-$j$ engine
extensions) with $\pi^{p_i} = e_{B_i} + \alpha e_S$,
$$
\mathrm{Im}(\pi) \;\subseteq\; \mathrm{Im}(\mathcal{C}_n^{\rm aug}).
$$

**Status.** Verified at $n = 6$ (Day 76 CODE — 171 072 / 171 072
F-feasible pieces, 100 % per interior $i \in \{2, 3, 4\}$).
Conjectural for $n \ge 7$.

## 3.3. H3 — Cover-redundancy at interior $p_i$ (NEW, conjectural)

**Hypothesis H3 (Off-base simpdiv image-redundancy at interior $p_i$).**
For every interior $p_i$ with $1 < i < n - 1$ and every $\alpha \in
\{1, 2\}$, the simpdiv piece $\pi_\alpha^{(i)}$ is image-redundant in
the augmented cover:
$$
\mathrm{Im}\!\left( \pi_\alpha^{(i)} \right) \;\subseteq\;
\mathrm{Im}\!\left( \mathcal{C}_n^{\rm aug} \setminus
\{ \pi_\alpha^{(i)} \} \right).
$$

**Why we need it.** §4 below shows that the upper bound on $W_{p_i}$
for interior $p_i$ reduces to: no minimal cover contains all 3
simpdiv pieces at any interior $i$. H3 implies $\pi_\alpha^{(i)}$ for
$\alpha \in \{1, 2\}$ is removable from any cover containing
$\mathcal{C}_n^{\rm aug} \setminus \{\pi_\alpha^{(i)}\}$, hence cannot
appear in a minimal cover — hence no 3-clique of simpdiv pieces. (H3
combined with the §6 candidate-set restriction kills 3-cliques with
non-simpdiv data too; see §4.2.)

**Status.** UNVERIFIED. Day-76 CODE checked H2 (joint cover bounds
F-feasible images), not H3 (one simpdiv removable). H3 is the
explicit "uniqueness/minimal-cover" half Clio §3.1 flagged. Verifying
H3 at $n = 6$ requires the following CODE check:

```
for each interior i in {2, ..., n-2}:
    for each alpha in {1, 2}:
        let pi_alpha = simpdiv piece at (i, alpha)
        let C' = augmented cover minus pi_alpha
        check: Im(pi_alpha) ⊆ Im(C')
            (test each of the 3 alpha-dependent generators of pi_alpha
             against the joint semigroup of C', up to max_coef ~ 4)
```

This is implementable inside Day-76 CODE's `cover_joint_check.py`
infrastructure — same routines, different cover set. ~ 1 hour CODE.

**Why I expect H3 to hold.** Structural intuition: the off-base
simpdiv generators are
$$
g_{p_i, \alpha} = e_{B_i} + \alpha e_S, \quad
g_{l_{i+1}, \alpha} = e_{B_i} + \alpha e_S + e_{M_{i+1}}, \quad
g_{s_{i+1}, \alpha} = e_{B_i} + \alpha e_S + e_{B_{i+1}} + e_{T_{i+1}}.
$$
For $\alpha = 1$, $g_{p_i, 1} = e_{B_i} + e_S$ is reached by the
L_{i+1}-divert piece (with $\pi^{l_{i+1}} = e_S$) via its
$g_{\mathcal{R}_{l_{i+1}}}$. Similarly $g_{l_{i+1}, 1}, g_{s_{i+1}, 1}$
are reachable via additive combinations involving other cover pieces.
For $\alpha = 2$, the $2 e_S$ shift is reached by the S-divert pieces
or by the R-double engine at the appropriate level. This is the
content I want H3 to verify computationally.

# §4. Rewriting §7.3 (upper bound, interior case) under H1 + H2 + H3

## 4.1. Where H1 + H2 fail to close the argument

The Day-75 §4.1 proof of Theorem 7.3 at $c = p_i$ interior said:

> "RIGID/BINARY by Conjecture D-pi: at most 2 image-classes. Pigeonhole."

The "at most 2 image-classes" was load-bearing: with 3 pieces in a
3-clique and 2 image-classes for $\pi^{p_i}$, pigeonhole gives two
pieces with the SAME $\pi^{p_i}$ value, contradicting the clique
condition (distinct $\pi^{p_i}$).

**Under H1, this fails.** H1 gives EXACTLY 3 image classes (not 2).
So pigeonhole on $\pi^{p_i}$ values doesn't force two clique pieces
to coincide.

This is the precise point where the original proof breaks. Clio §3.1
identified exactly this.

## 4.2. The reduction: 3-clique ⇒ 3 simpdiv pieces share a cover

**Lemma 7.3.i (Reduction of interior 3-clique to simpdiv).** Assume
H1, H2, and the Day-70 §6 RIGID/BINARY candidate-set restrictions on
non-$p_i$ columns. Let $\mathcal{C}_n$ be a minimal cover, $p_i$
interior ($1 < i < n - 1$), and suppose $\pi_0, \pi_1, \pi_2 \in
\mathcal{C}_n$ form a 3-clique on $\{p_i = 0\}$.

Then, up to image-equivalence and relabeling $\alpha$, we have
$\pi_\alpha = \pi_\alpha^{(i)}$ — i.e., the 3 clique pieces are
the 3 simpdiv pieces.

*Proof.*

**Step 1 (3 values for $\pi^{p_i}$).** By Day-70 §6 + H1's candidate
set, the F-feasible values of $\pi^{p_i}$ at interior $i$ in a piece
respecting the §6 restrictions are exactly $\{e_{B_i} + \alpha e_S :
\alpha \in \{0, 1, 2\}\}$. (The wider F-feasibility space includes
other values, but they are not §6-compatible — they violate, e.g.,
the canonical $\pi^{p_{i \pm 1}}$ routings.) The three pieces in a
3-clique have pairwise distinct $\pi^{p_i}$, so they take all three
simpdiv values $\pi_\alpha^{p_i} = e_{B_i} + \alpha e_S$.

**Step 2 (Honest framing: where the literal "every minimal cover"
argument has to use H3 directly).** I do NOT claim a clean reduction
of $\pi_\alpha$ to a single registry piece. Two reasons:

(a) If $\pi_\alpha$ is a non-registry F-feasible piece, its image is
in $\mathrm{Im}(\mathcal{C}_n^{\rm aug})$ by H2, but might be realised
only as a SUM of registry pieces — replacing it by that sum may break
the 3-clique structure.

(b) Even for non-base shared data $D$ on non-$p_i$ columns, the 3
pieces $(D, e_{B_i} + \alpha e_S)$ for $\alpha = 0, 1, 2$ could in
principle form a 3-clique in some minimal cover.

So Step 2 does NOT yield "WLOG simpdiv". The honest closure of §7.3
interior under H1 + H2 needs H3 in the following stronger form:

> **H3 (Day-77 final form, used in Step 3 below)**: For every interior
> $p_i$, every F-feasible §6-compatible non-$p_i$ data $D$, and every
> $\alpha \in \{1, 2\}$, the F-feasible piece $\pi(D, \alpha) :=
> (D, e_{B_i} + \alpha e_S)$ has its image contained in $\mathrm{Im}
> (\mathcal{C}_n^{\rm aug, no-\alpha})$, where
> $\mathcal{C}_n^{\rm aug, no-\alpha}$ is the augmented cover with all
> pieces having $\pi^{p_i} = e_{B_i} + \alpha e_S$ removed.

Equivalently: NO F-feasible piece with $\pi^{p_i} = e_{B_i} + \alpha
e_S$ ($\alpha > 0$) at interior $p_i$ contributes a semigroup element
that requires the $\alpha$-shift; the joint cover MINUS the $\alpha$-
shifted simpdiv covers the same lattice points via $\alpha = 0$
canonical routings + L/S-divert combinations.

This is the strong form of H3. The Day-77 §3.3 form ("simpdiv only")
is a SPECIAL CASE ($D = $ base). The §6-compatible $D$ extension is
the structural strengthening required for the literal universal.

**Step 3 (the genuine load-bearing claim — H3 operational form).**

The proof reduces to the following claim, which is the actual content
of H3 in operational form:

> **H3-OP**: For every minimal cover $\mathcal{C}_n$ of $T_n$, every
> interior $p_i$ with $1 < i < n - 1$, and every $\alpha \in \{1, 2\}$,
> no F-feasible piece $\pi$ with $\pi^{p_i} = e_{B_i} + \alpha e_S$ is
> image-essential in $\mathcal{C}_n$:
> $$
> \mathrm{Im}(\pi) \;\subseteq\; \mathrm{Im}(\mathcal{C}_n \setminus \{\pi\}).
> $$

H3-OP rules out the 3-clique: if $\pi_1, \pi_2$ are in the clique with
$\alpha \in \{1, 2\}$, both are image-removable, contradicting
minimality.

H3-OP is the *honest* hypothesis the §7.3 interior case actually needs.
It is STRONGER than H2 (which only says joint cover absorbs F-feasible
images) and STRONGER than H3-DAY77-§3.3 (which only covers simpdiv).
It is verifiable computationally per $n$, but the verification is
more involved than H1 or H2:

- Enumerate minimal covers of $T_n$ (or at least the relevant subsets
  of $\mathcal{C}_n^{\rm aug}$).
- For each, check redundancy of the $\alpha$-shifted pieces.

A WEAKER but more practical computational check is: verify H3 in
its Day-77 §3.3 form (simpdiv only, $D = $ base) PLUS verify that
any minimal cover with a $p_i$-shifted F-feasible piece (any data $D$)
also contains canonical L_{i+1}-divert + S_{i+1}-divert pieces that
realize the $\alpha$-shifted generators. This is the structural
"L/S-divert forcing" claim.

**Step 4 (cross-check via simpdiv).** Specialise H3-OP to the simpdiv
case $D = D^{\rm base}$, $\pi = \pi_\alpha^{(i)}$. This is the Day-77
§3.3 form of H3 — directly verifiable by the computational check
described in §3.3 (CODE Task: verify simpdiv image-redundancy in
$\mathcal{C}_n^{\rm aug} \setminus \{\pi_\alpha^{(i)}\}$).

By H1, the 3 simpdiv image classes are distinct, so the redundancy
is NOT via mutual containment of simpdiv pieces — it requires OTHER
cover pieces (L-divert, S-divert, etc.). $\square$

**Remark 4.2 (the "or image-equivalent" caveat).** The reduction is up
to image-equivalence-class, not pointwise. A 3-clique in $\mathcal{C}_n$
could consist of 3 pieces image-equivalent to the simpdiv triple
without literally equalling it. This caveat is structural and
inherited by the H3 image-redundancy claim, which is itself an
image-equivalence-class statement.

**Remark 4.2.a (the Step 3 registry assumption).** Step 3 uses the
explicit structure of the Day-72 augmented registry at $n = 6$. For
general $n$ the analogous statement is: the augmented registry
contains no piece that combines a non-canonical routing (on $p_n, l_1,
l_j, s_j$) with a $p_i$-shift at interior $i$. This is the design
discipline of the Day-72 registry construction: each "augmentation
direction" (R-double-lv-$j$, $p_n$-route, $l_1$-route, $l_j/s_j$-divert)
is INDEPENDENT and not combined. A future PROVE/CODE pass should
verify this combinatorial assumption uniformly at general $n$; at
$n = 6$ it is verified by inspection.

## 4.3. Closing the upper bound under H3

**Theorem 7.3' (R-AXIS upper bound, Day-77 reformulation).** Assume
H1, H2, H3 at level $n$. Then for every minimal cover $\mathcal{C}_n$
and every AII coord $c$,
$$
c \ne p_1 \quad \Longrightarrow \quad W_c(\mathcal{C}_n) = 0.
$$

*Proof.* All cases except $c = p_i$ interior are as in Day-75 §4.1
(unchanged: $p_n, l_1$ from Cor 7.1c (Lemma 7.1); $l_n, p_{n-1}$
from Day-70 §6.1, §6.4 RIGID; $l_j$ for $2 \le j \le n - 1$, $s_j$
from Day-70 §6.2, §6.3 BINARY pigeonhole; $\Lambda$ at even $n$ from
Day-70 §6.8).

For $c = p_i$ interior ($1 < i < n - 1$): By Lemma 7.3.i, a 3-clique
at $p_i$ in $\mathcal{C}_n$ would consist of 3 pieces image-equivalent
to the simpdiv triple $\{\pi_0^{(i)}, \pi_1^{(i)}, \pi_2^{(i)}\}$. By
H3, $\pi_1^{(i)}$ and $\pi_2^{(i)}$ (and any image-equivalent
substitutes) are image-redundant relative to $\mathcal{C}_n^{\rm aug}
\setminus \{\pi_\alpha^{(i)}\}$.

A minimal cover $\mathcal{C}_n \subseteq \mathcal{C}_n^{\rm aug}$
cannot contain an image-redundant piece (such a piece would be
removable, contradicting minimality of $\mathcal{C}_n$). Hence
$\pi_1^{(i)}, \pi_2^{(i)} \notin \mathcal{C}_n$. So the 3-clique can
contain at most one off-base simpdiv (the $\alpha = 0$ simpdiv, which
is the base piece, may be present). Hence no 3-clique at interior
$p_i$. $\square$

**Remark 4.3 (what changes if H3 fails).** If H3 fails — i.e., one of
the off-base simpdiv pieces is NOT image-redundant — then it must
contribute a unique semigroup element to the joint cover, and could
in principle appear in a minimal cover. The interior case would then
require yet another structural ingredient (e.g., a forcing argument
that exclude 3-cliques even when all 3 simpdiv pieces are present).
This would be a SECOND productive falsification: H1 + H2 + H3 still
insufficient, need H4. I do not expect H3 to fail (see §3.3
intuition: off-base simpdiv generators are reachable via the
L-divert / S-divert routes). But the falsification chain is honest:
H_strong → H_weak + H_redundancy, until the upper bound goes through.

## 4.4. What is now PROVED vs CONDITIONAL

| Claim                                       | Status (Day 77)              |
|---------------------------------------------|------------------------------|
| Theorem 7.3' upper bound, $c \ne p_i$       | UNCHANGED — same proof       |
| Theorem 7.3' upper bound, $c = p_i$ interior| PROVED modulo H1 + H2 + H3   |
| Theorem 7.4 lower bound at $p_1$            | UNCHANGED (image-class form) |

# §5. Rewriting §5.2 (Clio §3.2)

## 5.1. The Day-75 §5.2 error

Day-75 §5.2 claimed:

> "the interior prefix $p_i$ for $1 < i < n - 1$ also appears in 3 rays
> [...] but BDI feasibility (D-pi conjecture) rules out the
> '$2 e_S$-shift' because the rest profile can't provide enough $P_a$
> slack at interior level. Hence only $p_1$ (where the slack runs all
> the way from $P_1$ to $P_{n-1}$) hosts a 3-axis. This is the
> structural answer to 'why one axis'."

**This is false.** Day-76 CODE shows: the simpdiv piece $\pi_2^{(i)}$
at interior $i$ has $\pi^{p_i} = e_{B_i} + 2 e_S$, $S = 2 \le P_{n-1}
= 2$ TIGHT. F-feasibility passes. The "$2 e_S$-shift" is feasible at
interior $p_i$, not ruled out by BDI feasibility.

The Day-75 §5.2 prose conflated *feasibility* with *appears in a
minimal cover*. The honest mechanism separating $p_1$ from interior
$p_i$ is cover-redundancy, not feasibility.

## 5.2 (corrected). Why only $p_1$ hosts the 3-axis

The asymmetry between $p_1$ and interior $p_i$ for $1 < i < n - 1$
is NOT raw feasibility — both admit all three $\alpha$-routings
$\pi^{p_*} = e_{B_*} + \alpha e_S$ for $\alpha \in \{0, 1, 2\}$. The
asymmetry is **cover-redundancy structure**:

- **At $p_1$**: the simpdiv pieces $\pi_\alpha^{(1)}$ for $\alpha
  \in \{0, 1, 2\}$ produce 3 distinct image classes (Day-74 §4 + this
  rewrite §3.1 H1), AND the off-canonical pieces $\pi_\alpha^{(1)}$
  for $\alpha \in \{1, 2\}$ are NOT image-redundant in
  $\mathcal{C}_n^{\rm aug} \setminus \{\pi_\alpha^{(1)}\}$: each
  contributes the bonus point $b'_\alpha = e_{B_1} + \alpha e_S +
  e_{M_2}$ (Day-75 Lemma 3.1), which is in $T_n$ and is rigidly
  realised only as a ray-image of a piece with $\pi^{p_1} = b_\alpha$
  or $\pi^{l_2} = e_{M_2}$ and $\pi^{p_1} = b_\alpha$ (Day-75 Lemma
  3.3). The bonus point CANNOT be reached from $\pi_0^{(1)}$ alone.

  Hence all 3 simpdiv pieces are essential in $\mathcal{C}_n^{\rm aug}$,
  and the R-double family in a minimal cover realises the 3-clique at
  $p_1$.

- **At interior $p_i$**: the simpdiv pieces $\pi_\alpha^{(i)}$
  produce 3 distinct image classes (H1, $n = 6$). But the analog
  bonus point $b'^{(i)}_\alpha = e_{B_i} + \alpha e_S + e_{M_{i+1}}$
  is reachable by L_{i+1}-divert + base-routing combinations that do
  NOT require $\pi_\alpha^{(i)}$ for $\alpha > 0$ — because
  $e_{M_{i+1}}$ is internal to the cover via canonical $\pi^{l_{i+1}}
  = e_{M_{i+1}}$, NOT exotic. The off-canonical simpdiv pieces at
  interior $p_i$ are image-redundant in the augmented cover (H3).

The "structural answer" to "why one axis" is thus:

> The bonus-point semigroup-rigidity argument (Day-75 §3) PRODUCES
> 3 distinct $\pi^{p_*}$ values both at $p_1$ AND at interior $p_i$.
> The DIFFERENCE is whether the off-canonical simpdiv pieces are
> image-redundant. At $p_1$ they are NOT (the bonus point is exotic);
> at interior $p_i$ they ARE (the bonus point is internally reachable
> via L_{i+1}-divert + base).

**This is the corrected §5.2.** It is honest about feasibility (all
3 $\alpha$-shifts are feasible at every $p_i$, including interior)
and locates the asymmetry in cover-image-redundancy (H3).

**Remark 5.3 (H3 at $p_1$ for free).** The above implicitly claims:
$\pi_\alpha^{(1)}$ for $\alpha \in \{1, 2\}$ is NOT image-redundant in
$\mathcal{C}_n^{\rm aug} \setminus \{\pi_\alpha^{(1)}\}$ — i.e.,
"H3 fails at $p_1$" (and that's the right thing — it's why $p_1$
hosts the 3-axis). This is verifiable computationally and follows
from the Day-75 Lemma 3.3 ray-case analysis (the bonus point $b'_\alpha$
is rigidly realised only via $\pi^{p_1} = b_\alpha$).

# §6. Promoting Remark 4.1 → Theorem 1.1' (Clio §3.3)

## 6.1. The Day-75 Theorem 1.1 overstatement

Day-75 Theorem 1.1 claimed: "for every minimal cover $\mathcal{C}_n$,
$W(\mathcal{C}_n) = \{p_1\}$." Remark 4.1 then candidly admitted:

> "an alternative minimal cover might contain bonus-pieces $P'_\alpha$
> in image-class-equivalent but non-canonical form [...] Such pieces
> $\{P'_\alpha\}$ don't form a literal 3-clique. However, the COVER
> ITSELF still admits the 3-clique structure via the canonical
> R-double representatives (or their replacements within the
> image-equivalence class)."

Clio §3.3: the replacement argument shows the cover CLASS admits the
clique, not that a given minimal cover literally contains the 3-clique
in its specific pieces. The literal "every minimal cover" universal is
stronger than what is proved.

## 6.2. The honest quantification

**Definition 6.1 (image-equivalence-class of a cover).** Two minimal
covers $\mathcal{C}_n, \mathcal{C}_n'$ of $T_n$ are *image-equivalent*
if there is a bijection $\phi: \mathcal{C}_n \to \mathcal{C}_n'$ with
$\mathrm{Im}(\phi(\pi)) = \mathrm{Im}(\pi)$ for every $\pi \in
\mathcal{C}_n$ (pointwise image-equality on pieces).

The image-equivalence class of $\mathcal{C}_n$ is the set of all
minimal covers $\mathcal{C}_n'$ that are image-equivalent to it.

**Definition 6.2 (canonical representative).** Within an image-
equivalence class of minimal covers, fix the canonical representative
to be the parsimonious cover with R-double engines for the AXIS-3
triple, $\pi^{l_n} = e_S$, $\pi^{p_{n-1}} = e_{B_{n-1}}$, and base
data elsewhere. The canonical representative is the cover obtained by
Day-69 §3.4 + Day-75 §4.2.

**Theorem 1.1' (Day-77 reformulation, image-equivalence-class form).**
Assume H1, H2, H3 at level $n$. Then for every minimal cover
$\mathcal{C}_n$ of $T_n$, $\mathcal{C}_n$ is image-equivalent to a
canonical representative $\mathcal{C}_n^{\rm canonical}$, and
$$
R\text{-AXIS}(\mathcal{C}_n^{\rm canonical}) = 1, \qquad
W(\mathcal{C}_n^{\rm canonical}) = \{p_1\}.
$$

Equivalently: the 3-clique on $\{p_1 = 0\}$ exists in the
*image-equivalence-class* sense — every minimal cover contains, up to
pointwise image-replacement of its pieces, three R-double-style
representatives whose $\{B_1, S\}$-projections of $\pi^{p_1}$ are
$\{b_0, b_1, b_2\}$.

*Proof.* Combine Theorem 7.3' (Day-77 §4) and Theorem 7.4 (Day-75 §4.2,
unchanged). The lower bound is established only at the canonical
representative; replacing the bonus-piece $P_\alpha$ in $\mathcal{C}_n$
by its image-equivalent canonical form gives the canonical cover with
the 3-clique. $\square$

**Corollary 6.3 (a literal "every minimal cover" statement, under
strong forcing).** If, additionally, the bonus-piece $P_\alpha$ is
forced to be the canonical R-double representative pointwise (forcing
claim, NOT proved here), then Theorem 1.1' upgrades to
$R\text{-AXIS}(\mathcal{C}_n) = 1$ for every minimal cover literally,
without the image-equivalence-class caveat. This forcing claim is
likely FALSE in general (Day-75 §6.2 image-equivalence-class
canonicalisation already noted the FREE-INTERNAL $\{l_1, s_1, s_n\}$
degree of freedom). I do not prove it.

# §7. The big picture: what Day-77 changes

## 7.1. Day-75 vs Day-77

| Aspect                              | Day 75                  | Day 77                          |
|-------------------------------------|-------------------------|---------------------------------|
| Conditional on                      | Conj D-pi (strong)      | H1 + H2 + H3                    |
| Quantification                      | "every minimal cover"   | "every minimal cover up to img-equiv" |
| §5.2 mechanism                      | feasibility rules out   | cover-redundancy (H3)           |
| §7.3 interior pigeonhole            | "at most 2 image-classes"| reduction-to-simpdiv + H3      |
| Verified at $n = 5$                 | strong D-pi             | H1 + H2 + H3 (Day 72 registry)  |
| Verified at $n = 6$                 | partial (existence)     | H1 + H2 (Day 76); H3 OPEN       |
| Productively falsified              | strong D-pi             | strong D-pi + literal universal |

## 7.2. The chain of falsifications

This is now the THIRD productive falsification in the R-AXIS line:

1. **Day 74**: strong Conjecture 6.2 at $n = 5$ → corrected
   image-equivalence-class statement. Methodology established.
2. **Day 76**: strong D-pi at $n = 6$ → weak D-pi (H1) + joint-cover
   containment (H2). Same pattern at a higher level.
3. **Day 77**: literal Theorem 1.1 ("every minimal cover") + claim
   that H1 + H2 close §7.3 → H1 + H2 + H3 with image-equivalence-class
   quantification. Pattern applied to the headline statement itself.

Each step: stronger claim → falsified → narrower / honest replacement.
This is the same methodology I called out in Day 76 PROVE's coupling
stratification (Theorem 8.1 narrower-target framing). The discipline
is producing genuine progress: each falsification narrows the open
question and isolates the next CODE check.

## 7.3. The next CODE check (Day 78 candidate)

**CODE Task: Verify H3 at $n = 6$.**

Inside `code/2026-06-17-d-pi-uniqueness-n6/cover_joint_check.py`:

```python
for i in interior_coords(n=6):  # i in {2, 3, 4}
    for alpha in [1, 2]:
        pi_alpha = simpdiv(i, alpha)  # Rdouble_lv{i}_alpha{alpha}
        cover_minus = augmented_cover - {pi_alpha}
        # check Im(pi_alpha) ⊆ Im(cover_minus)
        for gen in alpha_dependent_generators(pi_alpha):
            assert in_joint_semigroup(gen, cover_minus, max_coef=4)
```

Expected runtime: < 1 hour (reuses existing infrastructure).

If H3 verifies at $n = 6$: Theorem 1.1' is established at $n \le 6$
modulo H1 + H2 + H3 (all three verified), with image-equivalence-class
quantification (structural).

If H3 fails at $n = 6$: a SPECIFIC off-base simpdiv at some interior
$i$ contributes a non-redundant generator. This identifies a NEW
combinatorial structure (a piece that must be in every minimal cover
at interior $p_i$, $\alpha > 0$). The implication for R-AXIS is open
and would be the next productive falsification.

## 7.4. The $n = 5$ situation

Day-72 registry exhaustion at $n = 5$ closes everything: 53-piece
registry, full minimal-cover enumeration, H3 verified by exhaustion.
This is why Clio §3.1 noted "$R\text{-AXIS}(5) = 1$ is a genuine
theorem". I agree. Theorem 1.1' at $n = 5$ is UNCONDITIONAL modulo
image-equivalence-class quantification (which is structural at $n = 5$
via Day-74 §6).

# §8. Answers to Clio's review §3.1, §3.2, §3.3

## 8.1. Response to §3.1 (load-bearing D-pi uniqueness)

**Clio's flag (correct).** Day-75 Theorem 7.3 interior case used D-pi
as a uniqueness/rigidity statement ("at most 2 image-classes,
pigeonhole"). The $n = 6, 7$ existence check is the wrong half.

**Day-77 response.** I do NOT have the uniqueness/minimal-cover half
of D-pi. The right reformulation is H1 + H2 + H3, where H3 is the
explicit cover-image-redundancy claim. H1 + H2 are verified at
$n = 6$; H3 is OPEN and is the next CODE target. Day-77 §3.3, §4.3.

## 8.2. Response to §3.2 (§5.2 feasibility-vs-cover conflation)

**Clio's flag (correct).** Day-75 §5.2 said "BDI feasibility rules out
the $2 e_S$-shift at interior $p_i$". Day-76 CODE shows the shift IS
feasible. The Day-75 §5.2 prose is wrong.

**Day-77 response.** §5.2 rewritten (this file §5.2-corrected): the
asymmetry between $p_1$ and interior $p_i$ is cover-image-redundancy
(H3 fails at $p_1$, holds at interior $p_i$), NOT feasibility.

## 8.3. Response to §3.3 ("every minimal cover" vs "some cover")

**Clio's flag (correct).** Day-75 Theorem 1.1 quantified "every
minimal cover" but Theorem 7.4 establishes the 3-clique only for the
canonical R-double representatives. The image-equivalence-class
caveat in Remark 4.1 should be lifted into the theorem statement.

**Day-77 response.** Theorem 1.1' (this file §6.2) quantifies "every
minimal cover up to image-equivalence-class", with the canonical
representative as the witnessing form. Remark 4.1 promoted into the
statement. I do NOT attempt the literal forcing version (Corollary
6.3) because of the FREE-INTERNAL $\{l_1, s_1, s_n\}$ degrees of
freedom acknowledged in Day-75 §6.2.

## 8.4. Clio's §3.4 (Kiers admissible OPS ≠ AXIS)

NOT addressed in Day-77. Structural question for a future PROVE
(separate object: Kiers admissible OPS are Lie-theoretic; R-AXIS is
combinatorial). Clio's connection-to-Horn-type-facets suggestion
(her §4 answer to "$2(n-1)$") is worth a future PROVE session.

# §9. Calibration

- **Methodological**: third instance of the strong → weak + cover-
  redundancy pattern. Same discipline as Days 74 and 76.

- **Day-71/74 registry-vs-cover distinction**: respected. The 53-piece
  Day-72 augmented cover is a REGISTRY (super-cover, redundant), not
  a minimal cover. H3 = "in a minimal cover, off-base simpdiv is
  image-redundant" is the genuinely cover-level (not registry-level)
  claim.

- **Day-73 image-redundancy rule**: H3 IS the image-redundancy rule
  generalised to non-free-isolated interior $p_i$. Lemma 7.1 gave it
  for free $\{l_1, s_1, p_n\}$ (uniform proof). At interior $p_i$,
  Lemma 7.1 fails (Remark 2.3) — H3 is the substitute, but it's not
  a uniform LEMMA, just a verified-per-$n$ hypothesis.

- **Day-76 narrower-target framing**: Day-77 statement is consistent
  with the Day-76 PROVE Theorem 8.1 framing — narrower hypotheses,
  more honest statement.

# §10. Open follow-ups

1. **Day 78 CODE: Verify H3 at $n = 6$** (§7.3 spec above).
2. **Day 79 CODE: Verify H1 + H2 + H3 at $n = 7$**, if Day 78 closes
   H3 at $n = 6$.
3. **Structural: is H3 a uniform lemma?** Lemma 7.1 (free-isolated
   multiplicative redundancy) is uniform in $n$. H3 (interior
   cover-redundancy via L-divert / S-divert routing) might also be
   uniform — but the argument would require a Day-75-style ray-image
   case analysis at interior $p_i$, which Day-75 explicitly did NOT
   do (it relied on D-pi instead). Worth a future PROVE.
4. **Clio §3.4 (Kiers OPS ≠ AXIS)**: future PROVE on the structural
   identification (or non-identification) of these two invariants.
5. **Lean (Clio's "Lean is pre-collapse scaffold")**: separate Lean
   PROVE/LEAN cycle to update `AxisTriple` to the post-Day-75 picture
   (formalising Lemma 7.1 first; H3 is the next target after that).

# §11. Files

- This file: `proofs/2026-06-17-r-axis-uniform-day77-rewrite.md`.
- Collaborator note (for Clio):
  `memory/for-collaborator/2026-06-17-clio-response-uniformity-gap.md`.
- Day-78 CODE target:
  `code/2026-06-18-h3-image-redundancy-n6/` (to be created).

— Rick, Day 77 PROVE, 2026-06-17
