# Azenhas inequalities (arXiv:2603.16698 + 2604.25856) vs Rick's BDI walls

**Date:** 2026-06-12 (Day 67 PROVE)
**Papers:**
- Azenhas, *The recording tableaux in the quantum LR map, the orthogonal
  transpose symmetry map, and the computation of $\mathfrak{k}$-highest
  weight tableaux*, arXiv:2603.16698v5, 10 Jun 2026, 47 pp.
  Cached: `papers/azenhas-2603.16698.pdf`.
- Azenhas, *The slack data of the recording tableaux in the quantum LR
  map determines its inverse: some applications*, arXiv:2604.25856v2,
  27 May 2026, 18 pp. Cached: `papers/azenhas-2604.25856.pdf`.
- Companion to NSW (Naito–Suzuki–Watanabe arXiv:2502.07270, the
  Naito–Sagaki proof via iquantum branching).
- Goal: test whether Azenhas's linear inequalities characterising
  $\mathfrak{k}$-highest weight tableaux in the quantum LR map (AII)
  coincide with Rick's three coordinate walls $\{m_2 = 0\},\
  \{m_{236} = 0\},\ \{m_{23456} = 0\}$ from the Day-62 $\tilde\pi_3'$
  stack-structure analysis.

## TL;DR — verdict

**NO MATCH.** Azenhas's inequalities and Rick's walls describe DIFFERENT
structural objects:

- **Azenhas:** a SUBPOLYTOPE of the AII multiplicity cone cut by
  *mixed* linear inequalities. The inequalities characterise
  $\mathfrak{k}$-highest weight tableaux (a HW-restricted set, a tiny
  fraction of full AII).
- **Rick (Day-62):** a STRATIFICATION of the FULL AII cone by three
  coordinate hyperplanes (positivity facets of three AXIS variables).
  The walls are where the 26-piece $\tilde\pi_3'$ piecewise structure
  switches engine.

Out of ~9 AII chart variables, **exactly ONE** ($m_2$) appears in both
Azenhas's nontrivial inequalities and Rick's walls — and even there in
different roles (RHS of an upper bound vs. a coordinate axis whose
positivity facet is a piece-switching wall).

The two frameworks are LINEAR-INEQUALITY structures on the AII cone but
of different TYPE: Azenhas's polytope is a HW sublocus; Rick's
stratification is a piecewise-projection structure on the full cone.
v4 §3 can cite Azenhas as a "parallel linear-inequality framework for a
different aspect of the AII LR machinery", NOT as the source of Rick's
walls.

**Companion (2604.25856) slack data ≠ Rick's Bucket-2 marginals.**
Azenhas's slack incidence vectors are 0/1-valued indicator vectors
for vertical-strip gaps in recording tableaux. Bucket-2 marginals are
integer-valued projection-stratification counts on the BDI side. No
direct numerical correspondence.

---

## 1. Azenhas's linear-inequality structure (precise)

### 1a. The polytope: 9 column-multiplicity variables at $n=3$

A $\mathfrak{k}$-highest weight tableau $S \in SST^{\mathfrak{k}\text{-hw}}_{2n}(\lambda)$
is, by NSW Def 10 / Azenhas Def 10, a tableau in $SST_{2n}(\lambda)$
whose AII LR image $P^{AII}(S) \in SpT_{2n}(\mu)$ is the symplectic HW
tableau of shape $\mu$. At $n=3$ this means $P^{AII}(S)$ has the form

```
2 2 2 2 ... 2  ← row 1, m_2 + m_{23} + m_{236} copies of 2
3 3 3 ... 3    ← row 2, m_{23} + m_{236} copies of 3
6 6 ... 6      ← row 3, m_{236} copies of 6
```

so $\mu = (\mu'_1, \mu'_2, \mu'_3)$ with $m_2 = \mu'_1 - \mu'_2$,
$m_{23} = \mu'_2 - \mu'_3$, $m_{236} = \mu'_3$.

By Cor 6 (Azenhas v5 p.39), the $\mathfrak{k}$-HW tableaux at $n=3$
with 1-0-slack recording structure have shape $\lambda$ filled with
columns from the following list of **NINE distinct symplectic columns**
(plus the trivial full column $(123456)$ which carries weight 0 and
contributes only the Yamanouchi prefix $Y(M^{2n})$):

| Column                | Multiplicity        | Length | Role                                  |
|-----------------------|---------------------|--------|---------------------------------------|
| $(1,2,3,4,5,6)$       | $M$ (free, weight 0)| 6      | Yamanouchi prefix                     |
| $(2,3,4,5,6) = \mathrm{red}^{-1}(2)$ | $m_{23456}$ | 5 | red-inv engine column ($\bar\varepsilon_1$) |
| $(1,2,3,5,6) = \mathrm{red}^{-1}(3)$ | $m_{12356}$ | 5 | red-inv engine column ($\bar\varepsilon_2$) |
| $(1,2,3,4,6) = \mathrm{red}^{-1}(6)$ | $m_{12346}$ | 5 | red-inv engine column ($\bar\varepsilon_3$) |
| $(1,2,3,4)$           | $m_{1234}$          | 4      | weight-0 bumped tail                  |
| $(1,2,3,5)$           | $m_{1235}$          | 4      | $\bar\varepsilon_2 - \bar\varepsilon_3$ bumped   |
| $(2,3,4,5)$           | $m_{2345}$          | 4      | $\bar\varepsilon_1 - \bar\varepsilon_3$ bumped   |
| $(2,3,6)$             | $m_{236}$           | 3      | symplectic HW long col                |
| $(2,3)$               | $m_{23}$            | 2      | symplectic HW medium col              |
| $(2)$                 | $m_2$               | 1      | symplectic HW short col               |

This catalog is exhaustive at $n=3$ for the inverse $LR^{AII^{-1}}$
image restricted to HW recording data $(S^{H,\mu}, Q)$.

### 1b. The nontrivial inequalities at $n=3$ (Azenhas Cor 6, eq. 107)

The Cor 6 statement, rewriting Azenhas's notation $\mathrm{red}^{-1}(u_i)$
into column labels:

$$
\boxed{
m_{12356} + m_{1235} \;\le\; m_2, \qquad
0 \;\le\; m_{12346} - m_{1235} - m_{2345} \;\le\; m_{23}.
}
$$

Plus all 9 trivial positivity facets $m_C \ge 0$.

The structural reading:

- $m_2$ on the RHS = the SHORT (length-1) symplectic-column count. It
  UPPER-BOUNDS the LHS combination of red-inverse-3 and short-bumped
  columns $(m_{12356}, m_{1235})$. **"Number of red-inv-3 and bumped-3
  columns is bounded by the number of short symplectic columns."**
- $m_{23}$ on the RHS = the MEDIUM (length-2) symplectic-column count.
  It UPPER-BOUNDS $m_{12346} - m_{1235} - m_{2345}$. The lower bound
  $\ge 0$ says $m_{12346}$ must dominate the bumped-from-level-2 columns.

These inequalities derive from the reverse-Schensted insertion rules at
each step of the iterated $\mathrm{red}^{-1}$ in Theorem D (eq. 97-98).

### 1c. Theorem D for general odd $n$ (the inequality template)

For $n$ odd, $\{u_i\} = (u_1, \ldots, u_n)$ where $u_k = 2k$ if $k$
even, $u_k = 2k - 1$ if $k$ odd (so $u_1=2, u_2=3, u_3=6, u_4=7, u_5=10, \ldots$
ending in $u_n = 2n$):

$$
\begin{aligned}
m_{\mathrm{red}^{-1}(u_i)} + m_{\mathrm{red}^{-1}(u_i)\setminus\{2n\}}
&\le m_{u_1 \cdots u_{i-1}}, \quad i = 2, \ldots, n,                  \\
0 \;\le\; m_{\mathrm{red}^{-1}(u_n)} - \sum_{i=1}^{n-1}
m_{\mathrm{red}^{-1}(u_i)\setminus\{2n\}}
&\le m_{u_1 \cdots u_{n-1}}.
\end{aligned}
$$

Inequality count: $(n-1)$ type-(97) + 1 type-(98) = **$n$ inequalities**.

Plus an EQUALITY (the slack-sum identity) parametrised by $k \in [0, n]$:

$$
\sum_{j=n}^{k+1} m_{\mathrm{red}^{-1}(u_j)}
+ m_{\mathrm{red}^{-1}(u_k)}
+ \sum_{j=1}^{k} m_{\mathrm{red}^{-1}(u_j)\setminus\{2n\}}
\;=\; |\delta_{\underline r}|,
$$

where $|\delta_{\underline r}|$ is the total slack count of the
recording-tableau slack incidence vector.

### 1d. Theorem E for general even $n$ (with extra linking equality)

For $n$ even, $\{u_i\}$ ends in $u_n = 2n - 1$ (not $2n$). The same type
of inequalities hold, but in addition the COR-8 LINKING EQUALITY

$$
m_{12 \cdots (2n-2) 2n} \;=\; \sum_{i=1}^{n-1} m_{\mathrm{red}^{-1}(u_i)\setminus\{2n\}}
$$

reduces the polytope dimension by 1 (this is the source of Day-58's
$f(n) = 3 - [n \text{ even}]$ parity in the polytope dim-gap; see
`connections/azenhas-bdi-canonical-projection.md` §1d).

### 1e. The polytope is FREE in $m_{236}$ and $m_{23456}$

**Crucial structural observation.** At $n=3$, the inequalities (107)
involve only the 6 variables $\{m_2, m_{23}, m_{12356}, m_{12346},
m_{1235}, m_{2345}\}$. The variables $m_{236}, m_{23456}, m_{1234}$
do NOT appear in any nontrivial inequality.

So the $\mathfrak{k}$-HW polytope at $n=3$ factors as a (6-dim cone with
the inequalities) $\times$ ($\mathbb{N}^3$ free in $m_{236}, m_{23456},
m_{1234}$). The "free" directions are: long HW column, red-inv-engine
$\bar\varepsilon_1$, weight-0 bumped column.

This factorisation IS THE STRUCTURAL ANALOG of Rick's coordinate-wall
stratification — but on a DIFFERENT subset (HW only) and in a DIFFERENT
sense (free extrusion vs. piece-switching).

---

## 2. Rick's three coordinate walls (Day-62 stack-structure)

From `connections/azenhas-bdi-canonical-projection.md` §"Day-62: (c*)
stack PINNED DOWN as AII-fibered groupoid":

**The three codim-1 walls inside the AII positive cone:**
$$
H_1 = \{m_2 = 0\}, \qquad H_2 = \{m_{236} = 0\}, \qquad H_3 = \{m_{23456} = 0\}.
$$

These are coordinate hyperplanes — specifically, the positivity facets
of the three AXIS variables $(m_2, m_{236}, m_{23456})$ identified in
the Day-62 variable taxonomy:

- RIGID (1 col image across 26 pieces): $m_{23} \to B_2$, $m_{12346} \to S$.
- BINARY (2 col images): $m_{12356}, m_{2345}, m_{1235}, m_{1234}$.
- AXIS / MULTI (4-10 col images): $m_2, m_{236}, m_{23456}$.

The AXIS variables are the variables for which the $\tilde\pi_3'$
26-piece projection's "engine choice" changes when crossing the
coordinate hyperplane. Sign-pattern $\sigma(p) = (\mathbf 1[m_2 > 0],
\mathbf 1[m_{236} > 0], \mathbf 1[m_{23456} > 0])$ stratifies the AII
cone into 8 strata, with stratum-vector
$\mathbf I = (1, 5, 9, 9, 13, 17, 22, 26)$ on
$\sigma = (000, 100, 010, 001, 101, 110, 011, 111)$.

The structural identity (Day-62):

$$
\#\{\text{AXIS variables}\} = \#\{\text{codim-1 walls in AII cone}\}
= f(3) = \dim \ker \pi_3 = 3.
$$

---

## 3. Chart-translation attempt: do Azenhas's inequalities match Rick's walls?

### 3a. Variable overlap

Side-by-side, indexed by AII column-multiplicity variable at $n=3$:

| Variable        | Azenhas role (Cor 6) | Rick role (Day-62)           | Overlap? |
|-----------------|----------------------|------------------------------|----------|
| $m_2$           | RHS upper bound      | AXIS / wall $H_1$            | YES (different role)  |
| $m_{23}$        | RHS upper bound      | RIGID ($\to B_2$)            | NO       |
| $m_{236}$       | (free)               | AXIS / wall $H_2$            | NO       |
| $m_{23456}$     | (free)               | AXIS / wall $H_3$            | NO       |
| $m_{12356}$     | LHS                  | BINARY                       | NO       |
| $m_{12346}$     | LHS                  | RIGID ($\to S$)              | NO       |
| $m_{1235}$      | LHS                  | BINARY                       | NO       |
| $m_{2345}$      | LHS                  | BINARY                       | NO       |
| $m_{1234}$      | (free)               | BINARY                       | NO       |
| $m_{123456}$ (=$M$) | Y prefix         | (not in AII cone variables)  | --       |

**ONE OVERLAP**: $m_2$ appears in both. But Azenhas uses it as an upper
bound (constraint on a polytope), Rick uses it as a positivity wall
(switch-locus for a piecewise map). These are different ROLES on the
same variable.

### 3b. Trivial-overlap check: are Rick's walls faces of Azenhas's polytope?

Each Rick wall is a coordinate hyperplane $\{m_C = 0\}$. Each is
trivially a face of the positive cone, hence a face of any
subpolytope including Azenhas's $\mathfrak{k}$-HW polytope.

- $\{m_2 = 0\}$ ∩ HW polytope: the inequality $m_{12356} + m_{1235}
  \le m_2 = 0$ forces $m_{12356} = m_{1235} = 0$. So $\{m_2 = 0\}$
  inside the HW polytope is a 3-codim face (dim drops by 3), not just
  1-codim.
- $\{m_{236} = 0\}$ ∩ HW polytope: $m_{236}$ doesn't appear in (107),
  so the wall just slices off a 1-codim face. No additional collapse.
- $\{m_{23456} = 0\}$ ∩ HW polytope: same — $m_{23456}$ doesn't appear
  in (107), so 1-codim face.

So among Rick's three walls, $\{m_2 = 0\}$ has a SPECIAL meaning in
Azenhas's polytope (forces 3 variables to 0); the other two are
"free-axis" walls in Azenhas's setting.

### 3c. Are Azenhas's inequalities Rick's wall-EQUALITIES under change of variables?

No. Rick's walls are SINGLE-coordinate $\{m_C = 0\}$. Azenhas's
inequalities are MIXED $\{m_{C_1} + m_{C_2} \le m_{C_3}\}$. No linear
change of variables can turn the latter into the former (rank
mismatch).

### 3d. Are Rick's three walls the "AXIS" of Azenhas's polytope?

Yes, in the FACTORISATION sense (§1e): Azenhas's HW polytope at $n=3$
factors with free extrusion along $m_{236}, m_{23456}, m_{1234}$. Two of
these three free-extrusion directions ARE Rick's walls $H_2, H_3$.

But this is a WEAK structural alignment — it doesn't say the walls have
the same MEANING in both frameworks.

### 3e. Verdict

**The two frameworks describe DIFFERENT structural objects.**

- Azenhas's polytope: $\mathfrak{k}$-HW subpolytope, cut by *mixed*
  linear inequalities and (at even $n$) a linking equality.
- Rick's stratification: the AII positive cone stratified by *single*-
  coordinate hyperplanes corresponding to the AXIS variables of the
  26-piece projection $\tilde\pi_3'$.

The structural overlap is:
1. ONE common variable role: $m_2$ as an "interface" coordinate (both
   an Azenhas RHS and a Rick wall).
2. Both involve LINEAR data on the AII cone — the bulk of v4 §3's
   "polytope-shadow combinatorial story" is parallel in spirit to
   Azenhas, but not the same as.

---

## 4. Phase 2 — slack data vs Bucket-2 marginals

### 4a. What Azenhas's slack data IS

From Azenhas 2604.25856 §3.3: for a vertical strip $\lambda/\mu$ with
$\ell(\mu) \le n$, the slack $t_0 = \ell(\mu) - l_0$ counts gaps; the
slack row index vector $\mathbf r = \{r_1 < \cdots < r_{t_0}\} \subseteq
[1, \ell(\mu)]$ records gap positions. Slack incidence vector
$\delta_{\mathbf r} \in \{0, 1\}^{\ell(\mu)}$ is the 0/1 indicator.

For a multi-vertical-strip recording tableau, the slack data is a
sequence of slack vectors $\mathbf r^{(i)}$ for $i = 1, \ldots, N$
(where $N = \nu_1$), encoded as the slack incidence MATRIX
$[\delta_{\mathbf r^{(N)}}, \ldots, \delta_{\mathbf r^{(1)}}]$.

### 4b. What Bucket-2 marginals ARE

From `code/2026-06-11-bucket2-extract/bucket2_triples.json`:
22 distinct triples $(c_{m_2}, c_{m_{236}}, c_{m_{23456}})$ in BDI
coordinates $(M_1, M_2, B_1, T_1, B_2, T_2, S)$, with axis-marginals:

- $i_2$: $\{1, 2, 9, 10\}$ — multiplicity counts of distinct $c_{m_2}$
  vectors across 22 triples (length 4 axis).
- $i_{236}$: $\{1, 1, 1, 1, 2, 3, 3, 4, 6\}$ — length 9.
- $i_{23456}$: $\{1, 1, 1, 2, 4, 4, 4, 5\}$ — length 8.

These are INTEGER multiplicities of distinct *coefficient-vector
patterns* — discrete distributional data on Rick's stratification.

### 4c. Direct comparison

Slack incidence vectors are 0/1; Bucket-2 marginals are integer $\ge 1$.
Slack vectors live in $\{0,1\}^{\ell(\mu)}$; Bucket-2 marginals live in
$\mathbb{N}^{4}, \mathbb{N}^9, \mathbb{N}^8$ with no natural length match.

**No correspondence.** Different structural levels:
- Slack data is AII-side, attached to RECORDING TABLEAUX (parametrising
  the iterated $\mathrm{red}^{-1}$).
- Bucket-2 marginals are BDI-side, attached to PROJECTION-PIECE
  COEFFICIENT VECTORS (parametrising the $\tilde\pi_3'$ engine choice).

The two are separated by both the AII $\to$ BDI projection AND the
HW-restriction (Azenhas restricts to HW, Bucket-2 is the FULL
projection-piece coefficient catalog).

### 4d. Could slack data arise as projection data inside a Bucket?

Conceivable in principle: $\delta_{\mathbf r}$ vectors could in
principle be reinterpreted as coefficient incidence vectors of pieces
in the 26-piece registry. But the COUNT mismatch:

- Azenhas $\delta_{\mathbf r}$ at $n=3$: $0/1$ vector of length $\le 3$,
  so at most $2^3 = 8$ distinct values.
- Bucket-2 $c_{m_{23456}}$ vectors: 7-component integer vectors with
  values in $\{0, 1, 2\}$, so many more possibilities.

Even with an injective map $\delta \to c$, the slack-data side is much
coarser than the Bucket-side. So no useful structural correspondence.

---

## 5. v4 §3 citation impact

### 5a. What CAN be cited from Azenhas

- **The HW polytope's linear-inequality structure** — Azenhas Cor 6
  (eq. 107) at $n=3$, Theorem D/E for general $n$ — is the standard
  reference for "linear-inequality characterisation of $\mathfrak{k}$-HW
  tableaux in the quantum LR map".
- **The $\mathrm{red}/\mathrm{red}^{-1}$ machinery** (Azenhas Lemma 1,
  Theorem 1, 2, 3 + companion 2604.25856 §3.3) is the structural
  algorithm for the inverse LR map, parallel in spirit to Rick's
  piecewise projection-piece construction.
- **The slack data parametrisation of the inverse** — the
  HW-recording-tableau side $\leftrightarrow$ $\mathfrak{k}$-HW
  multiplicity data.
- **The dim-gap parity** (Day-58 result, confirmed by Theorem D vs E
  structural asymmetry) — Azenhas's linking-equality presence at even
  $n$ vs absence at odd $n$ is the source of $f(n) = 3 - [n \text{ even}]$.

### 5b. What should NOT be cited from Azenhas

- Azenhas's inequalities are NOT the same as Rick's three walls. v4 §3
  should NOT claim "Rick's walls = Azenhas's inequalities".
- Azenhas's polytope is the HW subpolytope; Rick's stratification is on
  the FULL cone. v4 §3 should distinguish these clearly.

### 5c. Suggested v4 §3 reference text

> The HEAD section ($\mathfrak{gl}_2$ rep-theoretic anchor, Day-66
> Bucket-0 structure) cites Bucket-0 dim-3 = $V(2) \oplus V(0)$
> directly.
>
> The BULK section's combinatorial structure runs parallel to but is
> not the same as Azenhas's $\mathfrak{k}$-HW polytope inequalities
> [Aze26 = arXiv:2603.16698]. Azenhas characterises the AII HW
> sublocus via mixed linear inequalities (Cor 6 at $n=3$). Rick's
> three coordinate walls (the AXIS variables of the Day-62 26-piece
> stratification) are a structurally DIFFERENT object: they describe
> where the piecewise projection $\tilde\pi_3'$ switches engine, on
> the FULL AII cone. The Cor 6 inequalities and the wall structure
> share ONE variable ($m_2$) in common but in different roles.
>
> The connection that survives: Azenhas's HW polytope factors as
> (6-dim mixed-inequality cone) $\times \mathbb{N}^3$ free, with the
> three free directions including $m_{236}$ and $m_{23456}$ — two of
> Rick's three AXIS variables. This factorisation is the closest
> structural alignment, but it is not an identification.

---

## 6. Open questions raised

### OQ-AZENHAS-AXIS-FACTORISATION (Day-67 NEW)

At general odd $n$, does Azenhas's $\mathfrak{k}$-HW polytope factor as
$(\text{nontrivial cone}) \times \mathbb{N}^{n}$ where the $\mathbb{N}^n$
factor's $n$ free directions include all but ONE of Rick's $n$ AXIS
variables? At $n=3$ the answer is YES with the one missing being $m_2$
(which is bound by the inequality). Test: at $n=5$ (odd), count free
directions in Azenhas's Theorem D polytope, compare to Rick's 5 AXIS
variables (if Rick's framework extends).

This is the structural form of the parallel between Azenhas's HW
polytope and Rick's piecewise-projection AXIS structure. **Not a
direct match, but a SHARED 3-vs-$f(n)$ counting.**

### OQ-AZENHAS-BDI-HW-RESTRICTION (Day-67 NEW)

What does $\tilde\pi_3'$ restricted to the $\mathfrak{k}$-HW
subpolytope of AII look like? Specifically: which of the 26 pieces are
necessary to cover the HW subpolytope's image in BDI?

Conjecture (UNTESTED): the HW subpolytope is so restricted that only
a small subset of the 26 pieces suffice (~5 or fewer). This would be a
structural simplification of the projection on the HW sublocus,
potentially useful for a "HW-projected" sub-result.

---

## 7. Files produced / updated

- This file: `proofs/2026-06-12-azenhas-inequalities-read.md`.
- Collaborator note: `memory/for-collaborator/2026-06-12-azenhas-verdict.md`
  (to be written).
- Question update: `memory/questions/q-azenhas-inequalities-bdi.md`
  (to be updated with verdict).
- Connection refinement: `memory/connections/azenhas-bdi-canonical-projection.md`
  (Day-67 addendum with "Azenhas walls do NOT match Rick walls" finding).

## Status flags

- **OQ-AZENHAS-INEQUALITIES-BDI** RESOLVED Day-67: **NO MATCH** between
  Azenhas Cor 6 inequalities and Rick's three coordinate walls. One
  variable shared ($m_2$), different roles. Factorisation alignment
  exists but is weak.
- **v4 §3** reference text REVISED (see §5c above): cite Azenhas as
  parallel framework, NOT as source of Rick's walls.
- **OQ-AZENHAS-AXIS-FACTORISATION** (NEW Day-67): test if the
  free-extrusion direction count matches Rick's $f(n)$ at general $n$.
- **OQ-AZENHAS-BDI-HW-RESTRICTION** (NEW Day-67): study $\tilde\pi_3'$
  restricted to HW subpolytope.
