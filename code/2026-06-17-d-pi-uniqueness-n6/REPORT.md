---
title: "Day 76 CODE Task A — D-pi uniqueness half at n = 6"
author: Rick
date: 2026-06-17
status: **PRODUCTIVE OUTCOME** — weak D-pi (3 distinct image classes
        per interior) PASSES; joint-cover containment PASSES at 100 %;
        strong D-pi (every F-feasible image ⊆ simpdiv image) FALSIFIED.
---

# TL;DR

At $n = 6$, for every interior coord $p_i$ ($i \in \{2, 3, 4\}$):

1. **Weak D-pi** (3 distinct image classes among the simple-divert
   pieces $\pi_\alpha^{(i)}$, $\alpha \in \{0, 1, 2\}$): **PASS**.

2. **Joint-cover containment**: every F-feasible piece (under Day-70 §6
   RIGID/BINARY restrictions, extended to include R-double level-$j$
   engines) has image semigroup contained in the joint image of the
   53-piece Day-72 augmented cover: **PASS (100 %)**.

3. **Strong D-pi** (every F-feasible piece's image lies in the
   simpdiv-$\alpha^{(i)}$ image alone, *not* the broader cover):
   **FALSIFIED** — pieces that engineer non-$p_i$ positions
   (e.g., $p_6 \to e_{B_1}+e_{T_1}$ via Lemma B variants) produce
   generators not in $\mathrm{Im}(\pi_\alpha^{(i)})$.

Combined with Day-75's existence verification, the weak D-pi + joint-
cover-containment results give the conditional input the Day-75 PROVE
R-AXIS$(n) = 1$ theorem needs at $n = 6$. The strong D-pi failure is
the n = 6 analog of the Day-74 falsification of Conjecture 6.2 at $n = 5$:
the right statement is the WEAK form ("3 distinct image classes per
interior, all covered jointly"), not the strong form.

# Setup

## n = 6 BDI vars (registry ordering)

$$M_2, M_3, M_4, M_5,\ B_1, \ldots, B_5,\ T_1, \ldots, T_5,\ S$$
(15 vars). Polytope: $T_a \le B_a$, $P_a := 2 \sum_{b \le a} (B_b - T_b)
\ge 0$, $M_a \le \min(P_{a-1}, P_a)$, $S \le P_5$.

## n = 6 AII rays (linkLHS = 0 gauge)

17 rays per Day-72 `run.py::aii_rays`:

1. Pure prefix: $e_{p_j}$ for $j = 1, \ldots, 6$ (6 rays).
2. Pure long[1]: $e_{l_1}$ (1 ray).
3. Coupled $e_{s_1} + e_{\text{linkLHS}}$, gauged to $e_{s_1}$ alone
   (1 ray).
4. Pairs $e_{p_{j-1}} + e_{l_j}$ for $j = 2, \ldots, 6$ (5 rays).
5. Triples $e_{p_{i-1}} + e_{s_i} + e_{\text{linkLHS}}$, gauged to
   $e_{p_{i-1}} + e_{s_i}$ for $i = 2, \ldots, 5$ (4 rays).

**Important corrective note.** The rays in
`code/2026-06-17-complete-registry/registry.py::aii_rays(6)` (which the
`enumerate_pieces_even` enumeration is built on) include an erroneous
$e_{\text{long}[n]}$ contribution in the $s_i$-coupling rays — this
violates the AII constraint $\text{long}[n] \le \text{prefix}[n-1]$.
The correct ray set is `run.py::aii_rays(6)`, used by the
`build_augmented_registry` flow that produced `registry-n6.json`. All
F-checks below use the corrected ray set.

## F-feasibility check

For piece $\pi$ in linkLHS = 0 gauge:
- $\pi^{p_j} \in \mathrm{BDI}$ for $j = 1, \ldots, 6$.
- $\pi^{l_1} \in \mathrm{BDI}$.
- $\pi^{s_1} \in \mathrm{BDI}$.
- $\pi^{p_{j-1}} + \pi^{l_j} \in \mathrm{BDI}$ for $j = 2, \ldots, 6$.
- $\pi^{p_{i-1}} + \pi^{s_i} \in \mathrm{BDI}$ for $i = 2, \ldots, 5$.

(NO $\pi^{l_6}$ contribution to $s_i$-coupling rays.)

## Candidate column set (Day-70 §6 RIGID/BINARY + R-double engines)

For the D-pi check at interior $i$:

- **Fixed**: $\pi^{p_i} = e_{B_i} + \alpha e_S$ for each $\alpha \in
  \{0, 1, 2\}$. $\pi^{p_j} = e_{B_j}$ RIGID for $j \in \{1, \ldots, 5\},\
  j \ne i$. $\pi^{l_6} = e_S$ RIGID.

- **Variable** (per Day-70 §6, extended with R-double level-$j$ engines):

  | column | candidates | count |
  |---|---|---|
  | $\pi^{p_6}$ | base + Lemma B trio + R-double engines + S-divert | 7 |
  | $\pi^{l_1}$ | Lemma C trio + R-double engine | 4 |
  | $\pi^{l_2}, \ldots, \pi^{l_5}$ | BINARY $\{e_{M_j}, e_S\}$ | 2 each |
  | $\pi^{s_1}$ | base + R-double-lv1 engine + S-divert | 3 |
  | $\pi^{s_2}, \ldots, \pi^{s_5}$ | base + S-divert + R-double-lv$j$ engine | 3 each |

Total candidate count per (interior $i$, $\alpha$):
$7 \cdot 4 \cdot 2^4 \cdot 3 \cdot 3^4 = 108{,}864$.

# Results

## Three distinct simpdiv image classes per interior

For each interior $i \in \{2, 3, 4\}$, the three pieces
$\pi_\alpha^{(i)}$ (base piece with $\alpha\,e_S$ added to the $p_i$
column) all F-feasible (re-confirming Day 75). The three image
semigroups $\mathrm{Im}(\pi_\alpha^{(i)})$ are PAIRWISE
INEQUIVALENT — verified by bidirectional semigroup-containment check
(`max_coef = 4`).

| $i$ | $\mathrm{Im}(\pi_0) \simeq \mathrm{Im}(\pi_1)$ | $\mathrm{Im}(\pi_1) \simeq \mathrm{Im}(\pi_2)$ | $\mathrm{Im}(\pi_0) \simeq \mathrm{Im}(\pi_2)$ | classes |
|---|---|---|---|---|
| 2 | False | False | False | 3 |
| 3 | False | False | False | 3 |
| 4 | False | False | False | 3 |

**Weak D-pi (3 image classes per interior): PASS.**

## Joint-cover containment

For each interior $i \in \{2, 3, 4\}$ and each $\alpha \in \{0, 1, 2\}$,
enumerate all F-feasible pieces under the candidate set above, then
check whether each piece's image is contained in the joint semigroup
of the Day-72 augmented cover (53 pieces).

| $i$ | $\alpha = 0$ | $\alpha = 1$ | $\alpha = 2$ | Joint cover-contained |
|---|---|---|---|---|
| 2 | 93,312 | 62,208 | 15,552 | 171,072 / 171,072 (**100 %**) |
| 3 | 93,312 | 62,208 | 15,552 | 171,072 / 171,072 (**100 %**) |
| 4 | 93,312 | 62,208 | 15,552 | 171,072 / 171,072 (**100 %**) |

**Joint-cover D-pi (every F-feasible piece's image ⊆ Im(joint cover)):
PASS, 100 %.**

Day-72's augmented cover is sufficient: no F-feasible piece (under §6
RIGID/BINARY restrictions, with R-double engine extensions) produces a
ray-image direction outside the cover's joint semigroup.

This is the analog of Day-74's $n = 5$ figure "3456 / 4320 pieces
image-contained in cover" — and it's STRONGER (100 % vs 80 %), because
my $n = 6$ candidate set is somewhat narrower around the cover
generators.

## Strong D-pi (per-α image containment): FALSIFIED

For each (interior $i$, $\alpha$), enumerate F-feasible pieces with
$\pi^{p_i} = e_{B_i} + \alpha e_S$, then check whether each piece's
image is contained in $\mathrm{Im}(\pi_\alpha^{(i)})$ ALONE (not the
broader joint cover). Result:

| $i$ | $\alpha = 0$ | $\alpha = 1$ | $\alpha = 2$ | image ⊆ $\mathrm{Im}(\pi_\alpha)$ |
|---|---|---|---|---|
| 2 | 93,312 | 62,208 | 15,552 | 18 / 171,072 (0.01 %) |
| 3 | 93,312 | 62,208 | 15,552 | 18 / 171,072 (0.01 %) |
| 4 | 93,312 | 62,208 | 15,552 | 18 / 171,072 (0.01 %) |

The 18 pieces per interior that pass are the trivial subimage pieces
($\pi$ with no off-cover engineering on non-$p_i$ positions). All other
F-feasible pieces have at least one generator outside
$\mathrm{Im}(\pi_\alpha^{(i)})$ — for example, the R-double-lv-$j$
engine at $s_j$ adds $e_{B_j} + e_{T_j} + 2 e_S$, which lies outside
$\mathrm{Im}(\pi_\alpha^{(i)})$ but inside the joint cover (via
`Rdouble_lvj_alpha2` piece).

**Strong D-pi (per-α image containment) at $n = 6$: PRODUCTIVELY
FALSIFIED.**

This is the direct analog of Day-74 Conjecture 6.2 falsification at
$n = 5$: the strong "rest uniquely forced" form does not hold, but the
weak "image-equivalent up to cover-restricted freedom" form DOES.

## Registry-restricted check

Test on the 53 cover pieces directly. For each cover piece, identify
its $\pi^{p_i}$ column for each interior $i$; check
$\mathrm{Im}(\text{piece}) \subseteq \mathrm{Im}(\pi_\alpha^{(i)})$ for
the implied $\alpha$.

| $i$ | applicable | PASS (image-contained in simpdiv) | FAIL |
|---|---|---|---|
| 2 | 53 / 53 | 17 | 36 |
| 3 | 53 / 53 | 18 | 35 |
| 4 | 53 / 53 | 17 | 36 |

The failing pieces are P_n-routing variants (e.g.,
`P6_Pn_in_BT1, P6_Pn_in_BT3, P6_Pn_in_BT4, P6_Pn_in_BT5`) and
L_1-routing variants (e.g., `P6_L1_in_B*, P6_L1_in_M*`). They have
$\pi^{p_i} = e_{B_i}$ (trivial routing at $p_i$, hence $\alpha = 0$),
but they engineer OTHER positions (`p_n`, `l_1`), producing generators
not in $\mathrm{Im}(\pi_0^{(i)}) = \mathrm{Im}(\text{base})$.

# Why the strong claim fails (and why it doesn't matter)

The strong D-pi statement attempted in Day-72 §7 wanted: "the image
class at $p_i$ is determined ENTIRELY by $\pi^{p_i}$." This would mean
the 3 simpdiv pieces represent the only 3 image classes one can
construct, regardless of what other columns do.

But this isn't true — the OTHER columns (especially $p_n$ and $l_1$,
which have their own routing families in the cover) contribute
INDEPENDENTLY to the image, producing combinations not captured by
any single simpdiv piece.

The CORRECT (weaker) statement that the Day-75 PROVE actually uses is:
the 3 simpdiv pieces give the 3 distinct $p_i$-axis classes (in the
sense of axis-equivalence: two pieces are $p_i$-axis-equivalent iff
their $p_i$ columns are equal); and the joint cover absorbs any extra
generators that other engineering introduces. This weak form is what
the verifications above confirm.

# Connection to Day-75 PROVE rescue

The Day-75 PROVE theorem "R-AXIS$(n) = 1$ uniformly for $n \ge 3$"
takes D-pi (in some form) as conditional input. The strong form was
known dead at $n = 5$ (Day-74). The weak form — "3 distinct image
classes per interior, all in the joint cover" — is what's needed.

This script verifies that weak form at $n = 6$. Combined with Day-75
existence (the 3 simpdiv pieces are all F-feasible), the conditional
input to Day-75 PROVE is now established at $n = 6$.

The extension from $n \ge 5$ (Day-75) to $n \ge 6$ in the PROVE
theorem is now unblocked at $n = 6$.

# Files

- `d_pi_uniqueness_n6.py` — broad F-feasibility enumeration +
  strong-D-pi check (counterexamples to strong form).
- `registry_check.py` — registry-restricted simpdiv containment check.
- `cover_joint_check.py` — joint-cover containment check (the
  conclusive verification).
- `results.json` — broad enum + strong-D-pi-check JSON output.
- `registry_results.json` — registry check JSON output.
- `cover_joint_results.json` — joint-cover check JSON output.
- `run_log_v2.txt`, `registry_check.log`, `cover_joint.log` — full stdouts.

# Calibration

- Day-71/74 registry-vs-cover distinction respected: "augmented
  registry" ≠ "minimal cover"; strong claims about "exhausted minimal
  cover" require the JOINT image, not the simpdiv image.
- Day-73 image-redundancy: groupings are by IMAGE-equivalence, not
  generator-set-difference.
- Day-74 strong-conjecture skepticism: 4320-style empirical check at
  $n = 6$ shows what the strong claim CAN and CAN'T say.

# Verdict

**PRODUCTIVE OUTCOME at $n = 6$:**

- Weak D-pi (3 distinct image classes per interior): **PASS**.
- Joint-cover containment of all F-feasible pieces: **PASS, 100 %**.
- Strong D-pi (per-α single-image-class confinement): **FALSIFIED**
  (productive — the right replacement is the joint-cover form).

The Day-75 PROVE R-AXIS$(n) = 1$ theorem can now extend from
"$n \ge 5$" to "$n \ge 6$" using this verified conditional input.

— Rick, Day 76 CODE Task A, 2026-06-17
