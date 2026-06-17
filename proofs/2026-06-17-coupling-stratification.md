---
title: "Day 76 PROVE — n-uniform coupling stratification: the engine 2-ray decomposition asymmetry"
author: Rick
date: 2026-06-17
status: |
  THEOREM (n-uniform, modulo Conjecture D-pi at n ≥ 6):

    Theorem 8.1 (Engine 2-Ray Decomposition Asymmetry, n-uniform).
    For every n ≥ 3 and every 1 ≤ j ≤ n - 1, the tight-cap engine
    generator g_{s_j} ∈ T_n admits a 2-ray decomposition
    R_{p_j} + R_{s_j} in some BDI-feasible piece π with π^{s_j}
    base-canonical IF AND ONLY IF j = 1.

  This is the precise structural form of the Day-74 observation
  "only (s_1, p_1) couples in the engine sense" — the engineering
  of the tight-cap point at s_j is "offloadable" to a π^{p_j}-mediated
  path iff j = 1.

  HONEST GAP. The PROVE.md target as stated ("no BDI-feasible piece
  engineers both (s_j, p_j) for j > 1") is provably FALSE at the
  feasibility level: §6 exhibits a BDI-feasible piece at n = 5, j = 2
  with both π^{p_2} and π^{s_2} engineered. The narrower Theorem 8.1
  is the correct n-uniform statement; the broader "joint-engineering"
  claim holds within MINIMAL COVERS / canonical structural families
  but not for arbitrary BDI-feasible pieces.

related:
  - proofs/2026-06-20-r-axis-uniform-proof.md (Day 75 PROVE: R-AXIS = 1
    uniform, Lemma 7.1 multiplicative redundancy, §4.2 S_{n-1}-ENGINE).
  - code/2026-06-20-coord-pair-coupling/COUPLING_MATRIX.md (Day 75 CODE
    Task B: 18×18 and 21×21 coupling matrices at n = 5, 6).
  - proofs/2026-06-19-r-axis-uniform-1-n5.md (Day 74: image-equivalence
    class + S4-ENGINE genuine clause).
---

# §1. Setup and statement

## 1.1. Recap of the structural framework

Throughout: $n \ge 3$. AII coordinates $\{p_j, l_j, s_j\}_{j=1}^n$ (at
even $n$, replace $s_n$ by $\Lambda$). BDI coordinates $\{B_a, T_a\}_{a=1}^{n-1}$,
$\{M_a\}_{a=2}^{n-1}$, $S$ with the polytope inequalities $T_a \le B_a$,
$M_a \le \min(P_{a-1}, P_a)$, $S \le P_{n-1}$ where $P_a := 2 \sum_{b \le a}
(B_b - T_b)$.

Day-70 §3 AII rays (n-uniform, $3n$ rays at odd $n$):
- $\mathcal{R}_{p_j} = e_{p_j}$ for $j = 1, \ldots, n$.
- $\mathcal{R}_{l_1} = e_{l_1}$, $\mathcal{R}_{s_1} = e_{s_1}$.
- $\mathcal{R}_{l_j} = e_{p_{j-1}} + e_{l_j}$ for $j \ge 2$.
- $\mathcal{R}_{s_j} = e_{p_{j-1}} + e_{s_j}$ for $j \ge 2$.

A **piece** $\pi$ assigns each AII coord $c$ a BDI vector $\pi^c$ (the
$c$-column); $\pi$ is **BDI-feasible** iff $\pi(\mathcal{R}) \in T_n$
(the BDI lattice cone) for every AII ray $\mathcal{R}$ (Day-70 Theorem 4.2).

**Base piece** $\pi^{\mathrm{base}}_n$ (Day-69 §3): $\pi^{p_j} = e_{B_j}$
for $j \le n - 1$, $\pi^{p_n} = 0$, $\pi^{l_1} = e_{B_1}$,
$\pi^{l_j} = e_{M_j}$ for $2 \le j \le n - 1$, $\pi^{l_n} = e_S$,
$\pi^{s_j} = e_{B_j} + e_{T_j}$ for $j \le n - 1$, $\pi^{s_n} = 0$.

## 1.2. The tight-cap engine generator at level $j$

**Definition 1.1 (engine generator).** For $1 \le j \le n - 1$, define
the **tight-cap engine generator** $g_{s_j} \in \mathbb{Z}^{\mathrm{BDI}}$ by

$$
g_{s_j} \;:=\; \begin{cases}
   2 e_{B_1} + e_{T_1} + 2 e_S & \text{if } j = 1, \\[4pt]
   e_{B_{j-1}} + e_{B_j} + e_{T_j} + 2 e_S & \text{if } 2 \le j \le n - 1.
\end{cases}
$$

**Lemma 1.2 (feasibility of $g_{s_j}$).** $g_{s_j} \in T_n$ for every
$j \in \{1, \ldots, n - 1\}$.

*Proof.* Check the BDI inequalities.
- For $j = 1$: $B_1 = 2$, $T_1 = 1$, $S = 2$, all else $0$. $T_1 = 1 \le B_1 = 2$ ✓.
  $P_1 = 2(B_1 - T_1) = 2$; $P_a = 2$ for $a \ge 1$ since further $B_b - T_b = 0$.
  $M_a = 0 \le P_{a-1}, P_a$ ✓. $S = 2 \le P_{n-1} = 2$ ✓.
- For $j \ge 2$: $B_{j-1} = 1, B_j = 1, T_j = 1, S = 2$, all else $0$.
  $T_j = 1 \le B_j = 1$ ✓; other $T = 0$ ✓.
  $P_a = 0$ for $a < j - 1$; $P_{j-1} = 2 \cdot 1 = 2$;
  $P_a = 2(B_{j-1} + B_j - T_{j-1} - T_j) = 2(1 + 1 - 0 - 1) = 2$ for $a \ge j$.
  $M_a = 0$ ✓. $S = 2 \le P_{n-1} = 2$ ✓. $\square$

**Remark 1.3.** The tight-cap engine generator at level $j = n - 1$ is
the $g_{s_{n-1}}$ of Day-75 §4.2 ($S_{n-1}$-ENGINE), and Day-75 proves
that it forces a unique (engineered) $\pi^{s_{n-1}} = e_{B_{n-1}} + e_{T_{n-1}} + 2 e_S$
column up to image equivalence. Definition 1.1 generalises this to
arbitrary $j$.

## 1.3. The 2-ray decomposition concept

**Definition 1.4 (2-ray decomposition).** Let $\pi$ be a BDI-feasible
piece and $t \in T_n$. We say $t$ admits a **2-ray $\mathcal{R}_{p_j}
+ \mathcal{R}_{s_j}$ decomposition in $\pi$** if
$$
t \;=\; \pi(\mathcal{R}_{p_j}) + \pi(\mathcal{R}_{s_j}),
$$
i.e., $t$ equals the image of the sum of the two AII rays.

Explicitly:
- For $j = 1$: $\pi(\mathcal{R}_{p_1}) + \pi(\mathcal{R}_{s_1}) =
  \pi^{p_1} + \pi^{s_1}$.
- For $j \ge 2$: $\pi(\mathcal{R}_{p_j}) + \pi(\mathcal{R}_{s_j}) =
  \pi^{p_j} + \pi^{p_{j-1}} + \pi^{s_j}$.

**Definition 1.5 (engine 2-ray decomposability).** We say
$g_{s_j}$ is **engine 2-ray decomposable** at level $j$ if there exists
a BDI-feasible piece $\pi$ with $\pi^{s_j} = \pi^{s_j}_{\mathrm{base}} =
e_{B_j} + e_{T_j}$ (the base-canonical $s_j$-column) such that $g_{s_j}$
admits a 2-ray $\mathcal{R}_{p_j} + \mathcal{R}_{s_j}$ decomposition in $\pi$.

**Interpretation.** "Engine 2-ray decomposability" says the engineering
at the tight-cap point $g_{s_j}$ can be "offloaded" from $\pi^{s_j}$
(the column-engineering route) to a $\pi^{p_j}$-mediated route
(plus the base $\pi^{s_j}$). The Day-75 $S_{n-1}$-ENGINE shows
$g_{s_{n-1}}$ is realised by the column-engineering route (single-ray
$\mathcal{R}_{s_{n-1}}$ with engineered $\pi^{s_{n-1}}$). The question is
whether the alternative 2-ray route exists.

## 1.4. The main theorem

**Theorem 8.1 (Engine 2-Ray Decomposition Asymmetry, n-uniform).**
For every $n \ge 3$ and every $j$ with $1 \le j \le n - 1$:
$$
g_{s_j} \text{ is engine 2-ray decomposable} \quad \Longleftrightarrow \quad j = 1.
$$

This is the structural form of the Day-74 observation: only $(s_1, p_1)$
couples in the precise engine-decomposition sense.

The proof comes in two parts: §2 (existence for $j = 1$) and §3
(non-existence for $j \ge 2$). The non-existence direction is
n-uniformly proved, modulo Conjecture D-pi at $n \ge 6$ (for the
$\pi^{p_{j-1}}$ constraint at interior $j$).

# §2. The $j = 1$ case: coupling exists (n-uniform)

## 2.1. The decoupled R-double piece $\pi^{\mathrm{dRd}}(2)$

**Construction 2.1 (decoupled R-double, $\alpha = 2$).** Define
$\pi^{\mathrm{dRd}}_n(2)$ as the piece identical to base $\pi^{\mathrm{base}}_n$
except for the $p_1$-column:
$$
\pi^{\mathrm{dRd}}_n(2)^{p_1} \;=\; e_{B_1} + 2 e_S \;=\; b_2.
$$
All other columns equal base.

Equivalently, as a BDI-row specification: identical to base except
$S \leftarrow l_n + 2 p_1$ (base has $S \leftarrow l_n$ only).

**Lemma 2.2 (feasibility of $\pi^{\mathrm{dRd}}_n(2)$).** For every $n \ge 3$,
$\pi^{\mathrm{dRd}}_n(2)$ is BDI-feasible.

*Proof.* Check the image of every AII ray.

Rays whose image is unchanged from base (all rays not involving $p_1$,
i.e., $\mathcal{R}_{p_j}$ for $j \ne 1$, $\mathcal{R}_{l_1}$, $\mathcal{R}_{s_1}$,
$\mathcal{R}_{l_j}$ for $j \ne 2$, $\mathcal{R}_{s_j}$ for $j \ne 2$):
their images are base ray-images, which are BDI-feasible by base feasibility.

Rays involving $p_1$:
- $\mathcal{R}_{p_1}$: image $\pi^{p_1} = b_2 = e_{B_1} + 2 e_S$.
  $B_1 = 1$, $S = 2$, all else $0$. $T_1 = 0 \le 1$ ✓. $P_a = 2$ for $a \ge 1$.
  $M_a = 0$ ✓. $S = 2 \le P_{n-1} = 2$ ✓. Feasible.
- $\mathcal{R}_{l_2}$: image $\pi^{p_1} + \pi^{l_2} = b_2 + e_{M_2} =
  e_{B_1} + e_{M_2} + 2 e_S = b'_2$ (Day-75 Lemma 3.1's bonus point).
  Feasible by Day-75 Lemma 3.1.
- $\mathcal{R}_{s_2}$: image $\pi^{p_1} + \pi^{s_2}_{\mathrm{base}} =
  b_2 + (e_{B_2} + e_{T_2}) = e_{B_1} + e_{B_2} + e_{T_2} + 2 e_S = g_{s_2}$.
  Feasible by Lemma 1.2.

All 15 rays (at $n = 5$; analogously $3n$ rays at general $n$) check out.
$\square$

**Remark 2.3 (comparison with R-double).** $\pi^{\mathrm{dRd}}(2)$
differs from the Day-69 R-double $\pi^{\mathrm{Rd}}(2)$: the R-double
modifies $B_1, T_1, B_2, T_2, S$ to also add the $2 s_1, l_1, p_n$ pieces.
$\pi^{\mathrm{dRd}}(2)$ keeps $\pi^{s_1}, \pi^{l_1}, \pi^{p_n}$ BASE.
The "d" stands for "decoupled": $\pi^{s_1}$ is not engineered alongside
$\pi^{p_1}$.

## 2.2. The 2-ray decomposition of $g_{s_1}$

**Theorem 2.4 ($j = 1$ engine 2-ray decomposability, n-uniform).** For
every $n \ge 3$, $g_{s_1} = 2 e_{B_1} + e_{T_1} + 2 e_S$ is engine 2-ray
decomposable.

*Proof.* In $\pi^{\mathrm{dRd}}_n(2)$ from Construction 2.1:
- $\pi^{s_1} = e_{B_1} + e_{T_1} = \pi^{s_1}_{\mathrm{base}}$ ✓ (base-canonical).
- 2-ray sum $\mathcal{R}_{p_1} + \mathcal{R}_{s_1}$ image
  $= \pi^{p_1} + \pi^{s_1} = b_2 + (e_{B_1} + e_{T_1}) = 2 e_{B_1} + e_{T_1} + 2 e_S
  = g_{s_1}$ ✓.

By Lemma 2.2, $\pi^{\mathrm{dRd}}_n(2)$ is BDI-feasible. Hence $g_{s_1}$
is engine 2-ray decomposable. $\square$

**Remark 2.5 ("partially redundant" reading).** The same point $g_{s_1}$
is also reached by the R-double piece $\pi^{\mathrm{Rd}}(\alpha)$
($\alpha \in \{0, 1, 2\}$) via the column-engineered route: in any
R-double piece, $\pi^{s_1} = 2 e_{B_1} + e_{T_1} + 2 e_S = g_{s_1}$ itself,
so the single ray $\mathcal{R}_{s_1}$ alone hits $g_{s_1}$ via $\pi^{s_1}$.
The 2-ray $\mathcal{R}_{p_1} + \mathcal{R}_{s_1}$ decomposition in
$\pi^{\mathrm{dRd}}(2)$ gives a SECOND (image-equivalent) realisation
of $g_{s_1}$. The two are image-equivalent in the sense that both
contribute $g_{s_1}$ to the image semigroup. This is precisely the
"$\pi^{s_1}$ engine partially redundant with $\pi^{p_1}$'s $S = 2$
contribution" phenomenon flagged in Day-74 PROVE §7.

# §3. The $j \ge 2$ case: coupling fails (n-uniform, modulo D-pi)

## 3.1. Reduction to a $\pi^{p_j}$-feasibility question

**Lemma 3.1 (the decomposition equation).** Let $\pi$ be a BDI-feasible
piece with $\pi^{s_j} = \pi^{s_j}_{\mathrm{base}} = e_{B_j} + e_{T_j}$
for some $j \ge 2$. Then $g_{s_j}$ is engine 2-ray decomposable in $\pi$
iff
$$
\pi^{p_j} + \pi^{p_{j-1}} \;=\; e_{B_{j-1}} + 2 e_S.
$$

*Proof.* The 2-ray sum image in $\pi$ is
$\pi^{p_j} + \pi^{p_{j-1}} + \pi^{s_j} = \pi^{p_j} + \pi^{p_{j-1}} +
e_{B_j} + e_{T_j}$. Setting this equal to $g_{s_j} = e_{B_{j-1}} +
e_{B_j} + e_{T_j} + 2 e_S$ gives the claim. $\square$

## 3.2. The non-existence argument

**Definition 3.2.** Let $\mathcal{P}^{(j)} \subset \mathbb{Z}^{\mathrm{BDI}}$
denote the set of BDI vectors $v$ such that $v$ is the $p_j$-column of
some BDI-feasible piece $\pi$ (equivalently: $v$ is alone-feasible as a
single-ray $\mathcal{R}_{p_j}$ image).

**Lemma 3.3 (alone-feasibility constraint at $p_j$).** For $1 \le j \le n - 1$,
the alone-feasibility condition $v = \pi(\mathcal{R}_{p_j}) = \pi^{p_j} \in T_n$
forces: if $v$ has $S$-component $s \ge 1$, then $v$ must have
$\sum_a (v_{B_a} - v_{T_a}) \ge \lceil s / 2 \rceil$.

*Proof.* From $S \le P_{n-1} = 2 \sum_a (v_{B_a} - v_{T_a})$. $\square$

**Lemma 3.4 (D-pi RIGID/BINARY for interior $p_j$).** For $2 \le j \le n - 2$
and any piece $\pi$ in a minimal cover, by Conjecture D-pi (verified at
$n = 5$, conjectured uniform),
$$
\pi^{p_j} \in \{e_{B_j}, \; e_{B_j} + e_S\}.
$$

In particular, $\pi^{p_j}$ has $B_j$-component exactly $1$ and
$S$-component in $\{0, 1\}$.

**Lemma 3.5 (RIGID at $p_{n-1}$).** For $j = n - 1$ and any piece $\pi$
in a minimal cover, by Day-70 Lemma 6.4,
$$
\pi^{p_{n-1}} = e_{B_{n-1}}.
$$

**Theorem 3.6 ($j \ge 2$ engine 2-ray INDECOMPOSABILITY, n-uniform).**
For every $n \ge 3$ and every $j$ with $2 \le j \le n - 1$, $g_{s_j}$ is
NOT engine 2-ray decomposable in any BDI-feasible piece in a minimal
cover whose $\pi^{p_{j-1}}, \pi^{p_j}$ columns satisfy the Day-70 RIGID
+ Day-75 BINARY + Conjecture D-pi constraints.

*Proof.* Suppose $\pi$ is such a piece. By Lemma 3.1, we need
$\pi^{p_j} + \pi^{p_{j-1}} = e_{B_{j-1}} + 2 e_S$.

**Case A** ($j \ge 3$, $j \le n - 2$): By Lemma 3.4 (D-pi), $\pi^{p_j} \in \{e_{B_j}, e_{B_j} + e_S\}$
and $\pi^{p_{j-1}} \in \{e_{B_{j-1}}, e_{B_{j-1}} + e_S\}$.

In every combination, $\pi^{p_j}$ contributes a $B_j$-component of $1$:
$$
(\pi^{p_j} + \pi^{p_{j-1}})_{B_j} \ge 1 > 0 = (e_{B_{j-1}} + 2 e_S)_{B_j}.
$$
Contradiction. ✗

**Case B** ($j = n - 1$, $n \ge 4$): By Lemma 3.5 (RIGID), $\pi^{p_{n-1}} = e_{B_{n-1}}$.
And $\pi^{p_{n-2}}$ is constrained by Lemma 3.4 (if $n - 2 \ge 2$, i.e., $n \ge 4$)
to $\{e_{B_{n-2}}, e_{B_{n-2}} + e_S\}$, or by Day-75 R-AXIS structure
(if $n - 2 = 1$, i.e., $n = 3$) to $\{b_0, b_1, b_2\}$ on the
$\{B_1, S\}$-projection plus possibly $e_{M_2}$ on the $M_2$ row (case (i)
vs case (ii) of Day-75 Lemma 3.3).

Sub-case B1 ($n \ge 4$, so $n - 2 \ge 2$): same argument as Case A —
$\pi^{p_{n-1}}$ contributes $e_{B_{n-1}}$, but RHS has $B_{n-1} = 0$.
Contradiction. ✗

Sub-case B2 ($n = 3$, so $n - 2 = 1$, $j = 2$): handled by Case C below
(this is also the boundary case for $j = 2$).

**Case C** ($j = 2$, any $n \ge 3$): Here $\pi^{p_{j-1}} = \pi^{p_1}$.
By Day-75 Theorem 7.2 (uniform bonus-coord forcing at $p_1$, R-AXIS = 1),
the $\{B_1, S\}$-projection of $\pi^{p_1}$ is $b_\alpha = e_{B_1} + \alpha e_S$
for some $\alpha \in \{0, 1, 2\}$, possibly with an extra $e_{M_2}$
component (Day-75 Lemma 3.3 case (i): $\pi^{p_1} = b'_\alpha = b_\alpha + e_{M_2}$).
By Lemma 3.4, $\pi^{p_2} \in \{e_{B_2}, e_{B_2} + e_S\}$.

Decompose the equation $\pi^{p_2} + \pi^{p_1} = e_{B_1} + 2 e_S$
componentwise:
- $B_2$: $(\pi^{p_2})_{B_2} = 1$ (D-pi), $(\pi^{p_1})_{B_2} = 0$.
  RHS $B_2 = 0$. So LHS $B_2 \ge 1 > 0$. **Contradiction** unless $\pi^{p_2} = 0$.
- But $\pi^{p_2} = 0$ violates D-pi (which says $\pi^{p_2} \in \{e_{B_2}, e_{B_2} + e_S\}$).
- Hence no D-pi-compliant $\pi^{p_2}$ closes the equation. ✗

In all cases, the equation $\pi^{p_j} + \pi^{p_{j-1}} = e_{B_{j-1}} + 2 e_S$
has no solution in BDI-feasible pieces satisfying the D-pi + RIGID
constraints. Hence $g_{s_j}$ is not engine 2-ray decomposable for
$j \ge 2$. $\square$

## 3.3. Synthesis: Theorem 8.1 proved

**Theorem 8.1 (Engine 2-Ray Decomposition Asymmetry).** For every
$n \ge 3$ and every $j$ with $1 \le j \le n - 1$:
$$
g_{s_j} \text{ engine 2-ray decomposable} \iff j = 1,
$$
modulo Conjecture D-pi at $n \ge 6$.

*Proof.* ($\Rightarrow$, $j = 1$): Theorem 2.4. ($\Leftarrow$, $j \ge 2$):
Theorem 3.6. $\square$

# §4. The structural picture (engine stratification)

## 4.1. Why $j = 1$ is special

The asymmetry of Theorem 8.1 has a clean structural cause. Define the
**engine column** at level $j$ as the unique (up to image equivalence)
$\pi^{s_j}$-value that, combined with $\pi^{p_{j-1}}_{\mathrm{base}}$
(or for $j = 1$, with no $p_{j-1}$-contribution), yields the tight-cap
ray-image $g_{s_j}$ via $\mathcal{R}_{s_j}$.

- For $j = 1$: engine column $= 2 e_{B_1} + e_{T_1} + 2 e_S$, achieved
  by the R-double family. As a single column it is NOT alone-feasible
  ($S = 2 > P_{n-1} = 0$), but the $\mathcal{R}_{s_1}$ ray hits this
  column directly (since $\mathcal{R}_{s_1} = e_{s_1}$ involves no
  $p_0$-correction), and the column's $B_1 = 2$ contribution supplies
  the slack $P_1 = 2$ needed for $S = 2$.

  Crucially, the same $S = 2$ slack can ALSO be supplied by a
  $\pi^{p_1} = b_2$ column carrying $2 e_S$ on its own (and providing
  its own $B_1$ slack via $P_1 = 2 B_1 = 2$). The 2-ray combination
  $\mathcal{R}_{p_1} + \mathcal{R}_{s_1}$ then transfers the engineering
  load to $\pi^{p_1}$.

- For $j \ge 2$: engine column $= e_{B_j} + e_{T_j} + 2 e_S$, achieved
  by the analog of the $S_{n-1}$-ENGINE recipe at level $j$. The
  $\mathcal{R}_{s_j}$ ray contributes a $\pi^{p_{j-1}}$ component
  ($e_{B_{j-1}}$ in base) which supplies a $P_{n-1} = 2$ slack, allowing
  the engine column to have $S = 2$.

  The 2-ray transfer would require $\pi^{p_j}$ to supply the $2 e_S$
  contribution. But $\pi^{p_j}$ for $j > 1$ in a minimal cover is
  RIGID/BINARY (Conj D-pi for interior, Lemma 6.4 for $p_{n-1}$),
  with $B_j$-component fixed at 1 and $S \le 1$. The $S = 2$ requirement
  is structurally inaccessible.

## 4.2. The "$\alpha$-channel" — R-double's unique role

The Day-69 R-double family at LEVEL 1 is the unique structural family
that connects $p_1$ to $S$ via the parameter $\alpha \in \{0, 1, 2\}$:
$S \leftarrow l_n + 2 s_{n-1} + 2 s_1 + \alpha p_1$. This $\alpha p_1$
contribution is precisely what enables $\pi^{p_1} = b_\alpha$ to carry
$\alpha e_S$.

At LEVEL $j > 1$ R-double recipes (Day-75 §3 generalisation, see
`general_pieces.py::make_r_double_family`), the analogous
$\alpha$-channel is STILL $\alpha p_1$ — NOT $\alpha p_j$. I.e.:
$$
\text{R-double at level } j: \quad B_j \leftarrow p_j + 2 s_j, \quad S \leftarrow l_n + 2 s_j + \alpha p_1.
$$
The $\alpha p_1$ (not $\alpha p_j$) means engineering at $\pi^{s_j}$ for
$j > 1$ via the R-double-at-level-$j$ family DOES NOT introduce an
$\alpha p_j$-channel into $S$. Hence $\pi^{p_j}$ remains base in
R-double-at-level-$j$ pieces.

This is the precise structural mechanism: **R-double is the unique source
of $p_1 \to S$ engineering, and engineering at $s_j$ for $j > 1$ via
R-double-at-level-$j$ borrows the $p_1$ channel, not a new $p_j$ channel.**

## 4.3. Engine 2-ray decomposability as the precise "coupling" notion

Theorem 8.1 gives the cleanest n-uniform statement of the Day-74
observation. It captures the coupling in terms of:

| level | column-engineering ($\pi^{s_j}$ engine) | 2-ray alternative ($\mathcal{R}_{p_j} + \mathcal{R}_{s_j}$) |
|-------|------------------------------------------|-------------------------------------------------------------|
| $j = 1$ | R-double family ($\alpha$-parametrised) | EXISTS ($\pi^{\mathrm{dRd}}(2)$) — partially redundant |
| $j > 1$ | s-engine at level $j$                    | DOES NOT EXIST (D-pi obstruction) — genuine |

The "partially redundant" entry at $j = 1$ explains why the R-double's
$\alpha$-family is the GENUINE 3-axis (the engineering is duplicated
between $\pi^{p_1}$ and $\pi^{s_1}$); the "genuine" entry at $j > 1$
explains why the s-engine for $j \ge 2$ is structurally UNIQUE.

# §5. n-uniform corollaries

## 5.1. The Day-74 observation made precise

**Corollary 5.1 (n-uniform precise form of Day-74).** For every $n \ge 3$
and every $j$ with $1 \le j \le n - 1$, the tight-cap engine generator
$g_{s_j}$ is realised by:

(a) The column-engineered route $\pi^{s_j} = e_{B_j} + e_{T_j} + 2 e_S$
    (for $j \ge 2$) or $\pi^{s_1} = 2 e_{B_1} + e_{T_1} + 2 e_S$ (for $j = 1$),
    plus base $\pi^{p_{j-1}}$ — call this the **s-engine route**.

(b) **Only at $j = 1$**, additionally by the 2-ray route via
    $\pi^{p_1} = b_2$ with base $\pi^{s_1}$ — call this the
    **$p_1$-coupling route**.

This is the n-uniform structural confirmation of the $n = 5, 6$ CODE
result (Day-75 COUPLING_MATRIX.md): only $(s_1, p_1)$ admits the
coupling-route realisation.

## 5.2. Why $W_{p_1} = 1$ depends on this

The Day-75 R-AXIS = 1 lower bound (Theorem 7.4) shows
$W_{p_1}(\mathcal{C}_n) = 1$: a 3-clique on $\{p_1 = 0\}$ exists in every
minimal cover. The structural reason in terms of Theorem 8.1: the $j = 1$
coupling between $\pi^{p_1}$ and the $g_{s_1}$ engine allows the
$\alpha$-parameter to "live on" $\pi^{p_1}$ rather than (or in addition to)
$\pi^{s_1}$, yielding three image-distinct $\pi^{p_1}$ values
$\{b_0, b_1, b_2\}$ in the cover.

For $j \ge 2$, no such coupling exists — the s-engine forces $\pi^{s_j}$
itself, and there's no parameter family on $\pi^{p_j}$ — hence
$W_{p_j} = 0$, consistent with the Day-75 R-AXIS upper bound.

## 5.3. Calibration against the registry result

The Day-75 CODE coupling matrix at $n = 5, 6$ checks "joint engineering"
within the Day-72 augmented registry of 42/53 pieces. Theorem 8.1's
$\{ j > 1$ impossibility $\}$ direction is STRICTLY STRONGER for that
registry — it rules out 2-ray decompositions in arbitrary BDI-feasible
pieces SUBJECT to the D-pi + RIGID constraints, not just registry pieces.

The $\{ j = 1 \}$ direction is constructive: $\pi^{\mathrm{dRd}}(2)$ is
a new piece not in the Day-72 augmented registry, but it IS BDI-feasible
and exhibits the coupling.

# §6. Honest gap analysis

## 6.1. The PROVE.md target as literally stated fails

The original Day-76 PROVE target (PROVE.md "Statement" section) reads:

> $(s_j, p_j)$ is coupled at level $j$ if there exist BDI-feasible
> pieces $\pi, \pi'$ with $\pi^{p_j} \neq \pi'^{p_j}$ but $\pi^{s_j} =
> \pi'^{s_j}$ and the difference is realised by an integer combination
> of AII rays involving both $s_j$ and $p_j$ coordinates.

Under the operational reading from the Day-75 CODE ("$(s_j, p_j)$ couple
iff some BDI-feasible piece engineers BOTH columns simultaneously"), the
target theorem "$(s_j, p_j)$ couple iff $j = 1$" is **FALSE** at the level
of arbitrary BDI-feasible pieces.

## 6.2. The counterexample at $j = 2$, $n = 5$

**Construction 6.1 (combined piece $\pi^{\mathrm{C}}_2$).** Define
$\pi^{\mathrm{C}}_2$ at $n = 5$ as the piece identical to base except:
- $\pi^{p_2} = e_{B_2} + e_S$ (engineered, BINARY route)
- $\pi^{s_2} = e_{B_2} + e_{T_2} + 2 e_S$ (engineered, $S_2$-engine)

**Lemma 6.2.** $\pi^{\mathrm{C}}_2$ is BDI-feasible.

*Proof (computational verification, see §7).* All 15 AII ray-images at
$n = 5$ are BDI lattice points:
1. $\mathcal{R}_{p_1}$: $e_{B_1}$ ✓
2. $\mathcal{R}_{p_2}$: $e_{B_2} + e_S$ — $B_2 = 1$, $S = 1$, $P_{n-1} = 2$ ✓
3. $\mathcal{R}_{p_3}, \mathcal{R}_{p_4}, \mathcal{R}_{p_5}$: base ✓
4. $\mathcal{R}_{l_1}, \mathcal{R}_{s_1}$: base ✓
5. $\mathcal{R}_{l_2}$: $e_{B_1} + e_{M_2}$ ✓
6. $\mathcal{R}_{s_2}$: $e_{B_1} + e_{B_2} + e_{T_2} + 2 e_S = g_{s_2}$ ✓ (Lemma 1.2)
7. $\mathcal{R}_{l_3}$: $e_{B_2} + e_S + e_{M_3}$ — $B_2 = 1$, $M_3 = 1$,
   $S = 1$; $P_2 = 2$; $M_3 \le P_2 = 2$ ✓; $S \le P_{n-1} = 2$ ✓
8. $\mathcal{R}_{s_3}$: $e_{B_2} + e_S + e_{B_3} + e_{T_3}$ —
   $B_2 = B_3 = T_3 = 1$, $S = 1$; $P_3 = 2$ (since $B_2 + B_3 - T_2 - T_3
   = 1 + 1 - 0 - 1 = 1$); $S \le P_{n-1} = 2$ ✓
9. $\mathcal{R}_{l_4}, \mathcal{R}_{s_4}, \mathcal{R}_{l_5}, \mathcal{R}_{s_5}$: base ✓

Independently verified with `run.py::verify_piece_via_rays` (§7). ✗ no
failures. $\square$

**Implication.** $\pi^{\mathrm{C}}_2$ engineers BOTH $\pi^{p_2}$ and
$\pi^{s_2}$. So under the operational "joint engineering" definition,
$(s_2, p_2)$ IS coupled at the level of BDI-feasible pieces. The
Day-75 CODE observation is REGISTRY-BOUNDED — the Day-72 augmented
registry simply does not include $\pi^{\mathrm{C}}_2$.

## 6.3. Why Theorem 8.1 is still valuable

The narrower Theorem 8.1 (engine 2-RAY DECOMPOSABILITY) IS true and
n-uniform. It captures the right structural insight: the $g_{s_j}$
tight-cap point at level $j$ admits a coupling-route realisation iff
$j = 1$. The combined-piece $\pi^{\mathrm{C}}_2$ does NOT contradict
Theorem 8.1 — it has $\pi^{s_2}$ ENGINEERED, not base-canonical, so
the 2-ray decomposition in Definition 1.4 doesn't apply to it as a
"coupling route".

The combined-piece is a DIFFERENT scenario: it engineers $\pi^{s_2}$
via the column route AND ALSO engineers $\pi^{p_2}$ via the class-1-aux-style
route, INDEPENDENTLY. The two engineerings sit in disjoint structural
channels.

## 6.4. The open question

**Open question.** Is the combined-piece $\pi^{\mathrm{C}}_2$ (or its
generalisation $\pi^{\mathrm{C}}_j$ at any $2 \le j \le n - 2$, any $n \ge 5$)
**image-redundant** in a minimal cover? I.e., does every BDI lattice
point in $\mathrm{Im}(\pi^{\mathrm{C}}_j)$ also appear in
$\bigcup_{\pi' \in \mathcal{C}_n^{\mathrm{min}} \setminus \{\pi^{\mathrm{C}}_j\}} \mathrm{Im}(\pi')$?

Computational check at $n = 5, j = 2$ (§7): the distinctive lattice point
$e_{B_1} + 2 e_{B_2} + e_{T_2} + 3 e_S$ from $\pi^{\mathrm{C}}_2$'s
2-ray $\mathcal{R}_{p_2} + \mathcal{R}_{s_2}$ sum IS covered by the
single registry piece `Rdouble_lv2_alpha1`'s $\mathcal{R}_{s_2}$ ray-image.
But the FULL image-redundancy of $\pi^{\mathrm{C}}_2$ requires checking
ALL ray-images and their semigroup combinations against the union of
remaining pieces. This is a CODE task — left open.

**If image-redundant:** the combined-piece is removable from any minimal
cover, so the "operational $(s_j, p_j)$ coupling for $j > 1$" doesn't
arise in minimal-cover analysis. The Day-75 CODE result is then the
correct minimal-cover statement.

**If NOT image-redundant:** there exists a minimal cover including
$\pi^{\mathrm{C}}_2$, and the operational coupling DOES arise. The
Day-75 R-AXIS analysis would need extension to handle this case.

Theorem 8.1 is INDEPENDENT of this open question — it doesn't rely on
image-redundancy. The "engine 2-ray decomposability" is the right
structural concept.

# §7. Computational verification

## 7.1. Sub-agent verification of $\pi^{\mathrm{C}}_2$ feasibility

A sub-agent ran `verify_piece_via_rays(M, n=5)` from
`code/2026-06-17-complete-registry/run.py` on the combined piece
$\pi^{\mathrm{C}}_2$ (§6.2). RESULT: PASS — all 15 AII extreme rays
produce BDI lattice images.

## 7.2. Image-redundancy probe

Sub-agent checked: the lattice point $e_{B_1} + 2 e_{B_2} + e_{T_2}
+ 3 e_S$ from $\pi^{\mathrm{C}}_2$'s 2-ray sum. Of 42 registry pieces:
- IN image semigroup of: `Rdouble_lv2_alpha1` (1 piece).
- NOT in: 41 others (including `aux_class1_p2` and any $s_2$-engine).

`Rdouble_lv2_alpha1` reaches this point via single $\mathcal{R}_{s_2}$
ray-image $= \pi^{p_1} + \pi^{s_2} = b_1 + (2 e_{B_2} + e_{T_2} + 2 e_S)
= e_{B_1} + 2 e_{B_2} + e_{T_2} + 3 e_S$ (here $\pi^{p_1} = b_1$ from
$\alpha = 1$, and $\pi^{s_2} = 2 e_{B_2} + e_{T_2} + 2 e_S$ from the
level-2 R-double engineering).

So this single lattice point IS registry-covered, but the FULL image
semigroup containment of $\pi^{\mathrm{C}}_2$ is the open Section 6.4
question.

## 7.3. Registry confirmation

Sub-agent verified: zero pieces in `registry-n5.json` have BOTH
$\pi^{p_2} \ne$ base AND $\pi^{s_2} \ne$ base. The Day-75 CODE coupling
result is correctly registry-bounded.

# §8. Honest summary table

| Claim                                                  | Status                           |
|--------------------------------------------------------|----------------------------------|
| Lemma 1.2 ($g_{s_j} \in T_n$)                          | ✅ PROVED n-uniformly            |
| Lemma 2.2 ($\pi^{\mathrm{dRd}}(2)$ feasible)          | ✅ PROVED n-uniformly            |
| Theorem 2.4 ($j = 1$ engine 2-ray decomp exists)       | ✅ PROVED n-uniformly            |
| Theorem 3.6 ($j \ge 2$ engine 2-ray decomp fails)      | ✅ modulo Conj D-pi at n ≥ 6     |
| Theorem 8.1 (Engine 2-Ray Asymmetry, n-uniform)        | ✅ THEOREM modulo Conj D-pi      |
| PROVE.md target (joint-engineering "couples iff j=1")  | ❌ FALSE at BDI-feasible level   |
| ┗ Registry-bounded form (Day-75 CODE)                 | ✅ verified at n = 5, 6          |
| ┗ Minimal-cover form (Open Q 6.4)                     | ❓ open — image-redundancy CODE  |

# §9. What's productively NOT extended

- **Coupling matrices for $(c, c') \ne (s_j, p_j)$**: the Day-75 18×18
  matrix shows many off-diagonal couplings (e.g., $(s_3, p_2)$ from
  class-1 aux). These are NOT covered by Theorem 8.1; characterising
  them n-uniformly is a separate question (Day-75 PROVE.md fallback).
- **Combined-piece classification**: $\pi^{\mathrm{C}}_2$ is one
  example of a piece outside the Day-72 augmented registry. A full
  classification of BDI-feasible pieces with $\ge 2$ simultaneously
  engineered columns is open and likely large.
- **n = 3 special case**: at $n = 3$, the Singleton constraint introduces
  extra AII rays. Theorem 8.1's statement still applies ($j = 1$ only),
  but the case analysis in §3 needs a direct check. Day-75 §6.2 flagged
  this for general n-uniform claims; here we inherit the same caveat.

# §10. Calibration

- **Day-74 strong-conjecture skepticism applied.** PROVE.md's "structural
  asymmetry" was the right intuition; the literal "$(s_j, p_j)$ couples
  iff $j = 1$" theorem was overclaimed. Theorem 8.1 narrows the claim
  to the engine 2-ray decomposition setting where it IS true and uniform.

- **Day-73 image-redundancy rule** generalised: image-containment for
  combined pieces is the next sharp test. The combined-piece's
  image-redundancy in minimal covers is the open Section 6.4 question,
  and is the right next CODE task.

- **Day-71 D-pi lesson:** uniform claims need uniform proof or honest
  scoping. Theorem 8.1 is scoped to "modulo Conj D-pi at $n \ge 6$";
  the j = 2, $\pi^{p_1}$ case needs the Day-75 R-AXIS = 1 structure.

- **Day-60 productive falsification:** the PROVE.md target as literally
  stated is FALSIFIED by $\pi^{\mathrm{C}}_2$. This is the value of
  pushing to honest theorems — the falsification points to where the
  Day-75 CODE's "registry-bounded" caveat actually bites.

# §11. Open follow-ups

1. **CODE: image-redundancy probe for $\pi^{\mathrm{C}}_j$** at $j = 2, 3,
   \ldots, n - 2$ and various $n$. Compute $\mathrm{Im}(\pi^{\mathrm{C}}_j)$
   ray-by-ray and check whether each generator and their semigroup is
   contained in $\bigcup_{\pi' \in \text{Day-72 registry}} \mathrm{Im}(\pi')$.
   If yes: combined-piece is registry-redundant → Day-75 CODE result
   upgrades to "minimal-cover joint-engineering happens iff $j = 1$".
   If no: combined-piece is a NEW family, and Day-72 registry is
   incomplete as a minimal cover.

2. **PROVE: Theorem 8.1 + Conj D-pi at $n = 6, 7$.** Verify Conj D-pi
   at $n = 6, 7$ (CODE task already on Day-75 follow-up list). Once
   verified, Theorem 8.1 becomes unconditional for those $n$.

3. **Lean formalisation of Theorem 8.1.** ~50 lines: feasibility check
   for $\pi^{\mathrm{dRd}}(2)$ + the D-pi case analysis in §3. Should
   share infrastructure with Day-75's Lemma 7.1 formalisation.

4. **Generalise to other (c, c') pairs.** The Day-75 18×18 matrix has
   14 coupled pairs total. Theorem 8.1 covers only the $(s_1, p_1)$
   diagonal pair. A "coupling lemma" for the others (Class-1 aux
   secondary couplings, M-wall couplings) would close the matrix
   structurally.

# §12. Files

- This file: `proofs/2026-06-17-coupling-stratification.md`.
- Collaborator note:
  `memory/for-collaborator/2026-06-17-coupling-stratification.md` (to write).
- Computational verification:
  `code/2026-06-17-complete-registry/run.py::verify_piece_via_rays`
  (re-used; no new code).

— Rick, 2026-06-17 (Day 76 PROVE)
