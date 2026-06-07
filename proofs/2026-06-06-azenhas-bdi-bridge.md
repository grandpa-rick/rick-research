---
title: "Azenhas–BDI bridge (P_PARK #5): the asymmetric mirror is not a polytope isomorphism"
author: Rick
date: 2026-06-06
status: NEGATIVE RESULT (with positive structural shadow)
---

# Azenhas–BDI bridge — verdict

**TL;DR.** The conjecture that Azenhas's (AII$_{2n-1}$) $\mathfrak{k}$-highest-weight
inequalities `match' the BDI ($B_n$) chain-HW polytope facets under an
asymmetric-mirror map is **FALSE as a polytope-facet identification**, but
**TRUE in spirit** as a *structural* Watanabe-template instantiation. The
correct statement: both inequality systems are instances of the same
*bracket-scan template* (level-$i$ mid-count bounded by cumulative-previous-level
count), but the AII inequalities live in a *different ambient lattice* (with a
linking equality that BDI does not have) and the inequality COUNTS differ.
The "asymmetric mirror" is asymmetric because the two systems have different
*dimensions*: BDI's rank-3 chain factor gives two facets per level
($L_a, U_a$), while AII's rank-1 vertical-strip recording-tableau gives one
two-term inequality per level (sometimes refining into two with different
prefix-RHS).

---

## 1. The two systems, precisely

### 1.1 BDI ($B_n$ split): Theorems F + G of v3-bdi-unified-carry

**Coordinates.** $(M_a, B_a, T_a)_{a=1}^{n-1} \in \mathbb{Z}_{\ge 0}^{3(n-1)}$
(chain multiplicities) and $S \in \mathbb{Z}_{\ge 0}$ (singleton multiplicity).

**Cumulative carry.** $P_a := \sum_{b=1}^{a} 2(B_b - T_b)$, $P_0 := 0$.

**Chain-HW polytope.** $\mathsf{P}_n := \{(M, B, T, S) \in \mathbb{Z}_{\ge 0}^{3(n-1)+1}
 : \pi \text{ is } B_n\text{-highest}\}$.

**Carry-derived inequalities** (Theorem A):
$$
\begin{aligned}
L_a &: M_a \le P_{a-1} \quad (1 \le a \le n-1) \\
U_a &: M_a \le P_a \quad (1 \le a \le n-1) \\
E &: S \le P_{n-1}
\end{aligned}
$$
Total: $2n - 1$ inequalities. Non-redundant facets (Theorem F):
$\{L_a, U_a : 2 \le a \le n-1\} \cup \{E\}$, total $\boxed{2n - 3}$.
$L_1$ is degenerate ($M_1 = 0$ forced), $U_1$ redundant.

**Chain–to–weight image is simplicial** (Theorem G): under
$\Phi: (M, B, T, S) \mapsto (\lambda_1, \ldots, \lambda_n)$,
all $L_a, U_a$ collapse, only $E$ survives; weight-image cone has $n$ facets,
contraction ratio $(2n-3)/n \to 2$.

### 1.2 Azenhas (AII$_{2n-1}$, $\mathfrak{k} = \mathfrak{sp}_{2n}$):
Theorems 6 (n odd) and 7 (n even) of arXiv:2603.16698

**Setup.** Tableaux on alphabet $\{1, 2, \ldots, 2n\}$. The
$\mathfrak{k}$-highest weight $u$-sequence:
$$
\{u_i\}_{i=1}^n = \begin{cases}
\{2, 3, 6, 7, 10, \ldots, 2(n-1)-1, 2n\}, & n \text{ odd} \\
\{2, 3, 6, 7, \ldots, 2(n-1), 2n-1\}, & n \text{ even}
\end{cases}
$$

**Coordinates.** Multiplicities $m_X$ of various columns $X \in
\mathrm{SST}_{2n}(\varpi_l)$, in particular:
- $m_{u_1 u_2 \cdots u_i}$ for $i = 1, \ldots, n$ — prefix symplectic
  columns of length $i$ ($n$ variables).
- $m_{\mathrm{red}^{-1}(u_i)}$ for $i = 1, \ldots, n$ — fixed length-$(2n-1)$
  columns reducing to single-entry column $(u_i)$ under Watanabe's reduction
  map `red`. ($n$ variables, but only the $i \ge 2$ ones appear in
  inequalities; the $i = 1$ slot is fixed via the equality.)
- $m_{\mathrm{red}^{-1}(u_i) \setminus \{2n\}}$ for $i = 1, \ldots, n-1$ —
  length-$(2n-2)$ columns obtained by deleting the entry $2n$.

**Inequalities (n even — Theorem 7).**
$$
\begin{aligned}
\text{Main}_i &: m_{\mathrm{red}^{-1}(u_i)} + m_{\mathrm{red}^{-1}(u_i) \setminus \{2n\}} \le m_{u_1 u_2 \cdots u_{i-1}} \quad (2 \le i \le n) \\
\text{Link}  &: m_{12 \cdots (2n-2) \cdot 2n} \;=\; \sum_{i=1}^{n-1} m_{\mathrm{red}^{-1}(u_i) \setminus \{2n\}}
\end{aligned}
$$
Total: $n-1$ inequalities + 1 equality.

The corollaries for small $n$ (Corollary 7 for $n=2$, Corollary 8 for $n=4$)
exhibit *refined* (split) forms where the LHS sum is broken into two
separate inequalities with *different* prefix-RHS, e.g. for $n=2$:
$$
m_{123} \le m_2 \quad \text{and} \quad m_{124} \le m_{23},
$$
not merely the combined $m_{123} + m_{124} \le m_2$.

**Inequalities (n odd — Theorem 6).**
$$
\begin{aligned}
\text{Main}_i &: m_{\mathrm{red}^{-1}(u_i)} + m_{\mathrm{red}^{-1}(u_i) \setminus \{2n\}} \le m_{u_1 u_2 \cdots u_{i-1}} \quad (2 \le i \le n) \\
\text{Singleton}&: 0 \le m_{\mathrm{red}^{-1}(u_n)} - \sum_{i=1}^{n-1} m_{\mathrm{red}^{-1}(u_i) \setminus \{u_n\}} \le m_{u_1 \cdots u_{n-1}}
\end{aligned}
$$
Total: $n - 1 + 2 = n + 1$ inequalities + 1 identity.

---

## 2. Side-by-side at $n = 2$

| Side | Variables | Inequalities |
|------|-----------|--------------|
| BDI ($B_2$) | $(M_1, B_1, T_1, S)$ | $L_1: M_1 \le 0$, $U_1: M_1 \le 2(B_1 - T_1)$, $E: S \le 2(B_1 - T_1)$ |
| Non-redundant BDI | $(B_1, T_1, S)$ | $E: S \le 2(B_1 - T_1)$ (with $T_1 \le B_1$ implicit) — **1 facet** |
| Azenhas (AII$_3$) | $(m_2, m_{23}, m_{14}, m_{123}, m_{124})$ | $m_{123} \le m_2$, $m_{124} \le m_{23}$, $m_{14} = m_{23}$ — **2 inequalities + 1 equality** |

**Dimensional mismatch already at $n = 2$.** The non-redundant BDI polytope has
*ambient dimension* 3 ($B_1, T_1, S$ with one inequality). The Azenhas polytope
after eliminating $m_{14}$ via the equality has *ambient dimension* 4
($m_2, m_{23}, m_{123}, m_{124}$ with two inequalities). They cannot be related
by a bijective polytope-facet identification because they live in different
dimensions.

**Counts at small total weight** (`enumerate_b2_hw.py`):

| $N$ | BDI ($|\pi| \le N$) | Azenhas (sum $\le N$) |
|-----|---------------------|------------------------|
| 0 | 1 | 1 |
| 1 | 2 | 2 |
| 2 | 5 | 5 |
| 3 | 9 | 9 |
| 4 | 15 | **16** ← bridge breaks here |
| 5 | 23 | 25 |
| 6 | 34 | 39 |
| 7 | 47 | 56 |

The counts agree through $N = 3$ by coincidence of small-weight degeneracy
($\le 3$ multiplicities total — too few cells for the extra Azenhas
$m_{124}$-direction to register). From $N = 4$ onward the Azenhas count grows
strictly faster, reflecting the extra Azenhas degree of freedom.

---

## 3. Facet counts at general $n$

| $n$ | BDI: $2n - 3$ | Azenhas $n$ odd: $n + 1$ | Azenhas $n$ even: $n - 1$ |
|-----|---------------|--------------------------|----------------------------|
| 2 | 1 | — | 1 |
| 3 | 3 | 4 | — |
| 4 | 5 | — | 3 |
| 5 | 7 | 6 | — |
| 6 | 9 | — | 5 |
| 7 | 11 | 8 | — |
| 8 | 13 | — | 7 |

**Asymptotically.** BDI: linear with slope 2. Azenhas: linear with slope 1.
The BDI facet count *strictly dominates* Azenhas for $n \ge 5$, with the
gap growing as $n - C$ for some constant $C$ depending on parity. No
asymmetric-mirror map can reconcile these counts: a map from BDI's $2n - 3$
facets to Azenhas's $\approx n$ inequalities is necessarily many-to-one.

---

## 4. Why the bridge fails: the rank-3-chain-factor vs rank-1-strip
   asymmetry

Rick's own v3 paper, Remark 3.5 (`Asymmetric mirror`), already names this
obstruction without naming Azenhas as a candidate match:

> The chain-factor alphabet is rank-3, but the carry sees only a
> $\{0, +2\}$ bit. The signed slack data $(t_0^{(i)}, r^{(i)})$ that
> Azenhas's type-AII recording exploits has **no chain-factor analogue**:
> $\MB(a)$ and $\TM(a)$ are distinct chain-factor bits but contribute
> identically to $P_a$. This is the
> rank-3-chain-factor-vs-rank-1-strip distinction of §scope at the
> analytic level.

Unpacking: in BDI the chain factor at level $a$ has *three* multiplicities
$(M_a, B_a, T_a)$, where $M_a$ is the "mid" coordinate constrained by $L_a$
and $U_a$ — two separate facets per level. The carry $P_a$ is an unsigned
scalar (it only sees the $B - T$ difference, not $B$ and $T$ separately
beyond that).

In Azenhas, the level-$i$ chain object is a *vertical strip*
(rank-1 from the perspective of a single bumping step) with **signed slack
data** $(t_0^{(i)}, r^{(i)})$. The slack data is *finer* than BDI's
unsigned $P_a$: it distinguishes which slots in the vertical strip carry a
slack vs not. This finer data is what enables the *split* form of the
Theorem-6/7 inequality (one per prefix length), captured in the
small-$n$ corollaries 7 and 8 (lines 4803–4807, 5089–5092 of
azenhas-2603.16698.txt).

So the BDI chain-3-factor and the Azenhas signed-slack-rank-1-strip
encode **complementary information**:
- BDI's $L_a, U_a$ split the mid-bound by $P_{a-1}$ vs $P_a$ (left- vs
  right-cumulative);
- Azenhas's main$_i$ splits the same mid-bound by prefix-length
  ($m_{u_1 \cdots u_{i-1}}$ vs $m_{u_1 \cdots u_i}$).

**These are different splittings of the same conceptual constraint.** No
linear bijection on facets exists because the facet poset of $\mathsf{P}_n$
($2n - 3$ facets indexed by $\{L_a, U_a\} \cup \{E\}$) does not match the
"refined" Azenhas facet poset ($\le n$ inequalities at most, with the
prefix-length refinement structure).

---

## 5. What DOES hold: the bracket-scan template

Both inequality systems instantiate the same *bracket-scan template*:

> At level $i$ (or $a$), the "current mid-count" is bounded above by a
> "cumulative function of previous bottom/top contributions."

This template is the Watanabe abstract framework. The two instantiations:

**BDI template instantiation** ($i$ = chain index $a$):
- Mid-count: $M_a$
- Cumulative previous: $P_{a-1} = \sum_{b < a} 2(B_b - T_b)$ — a
  $\mathbb{Z}$-valued *scalar*.
- Singleton cap: $S \le P_{n-1}$.

**AII template instantiation** ($i$ = $u$-sequence index):
- Mid-count: $m_{\mathrm{red}^{-1}(u_i)}$ (plus its $\setminus \{2n\}$
  partner).
- Cumulative previous: $m_{u_1 u_2 \cdots u_{i-1}}$ — a *column
  multiplicity*, not a sum.
- Singleton cap: at the boundary $i = n$ for $n$ odd; for $n$ even, a
  *linking equality* $m_{12 \cdots (2n-2) \cdot 2n} = \sum
  m_{\mathrm{red}^{-1}(u_i) \setminus \{2n\}}$.

The structural similarity is real: both have $(n-1)$-ish "main"
inequalities plus a boundary/singleton structure. But the
*algebraic content* of "cumulative previous" differs:
- BDI: a CARRY SCALAR (sum of $\pm 2$ contributions).
- AII: a COLUMN MULTIPLICITY (a separate variable per level).

So there is no linear transformation $\Theta: (\text{BDI vars}) \to
(\text{AII vars})$ that takes BDI inequalities to AII inequalities. The
"asymmetric mirror" in Rick's Remark 3.5 names exactly this absence: the
finer signed slack data of AII cannot be encoded in BDI's unsigned
single-bit carry.

---

## 6. Computational verification

Run `enumerate_b2_hw.py`:
```
BDI B_2 lattice counts (|π| ≤ N):
  N=0: 1, N=1: 2, N=2: 5, N=3: 9, N=4: 15, N=5: 23, N=6: 34, N=7: 47

Azenhas n=2 lattice counts (sum ≤ N):
  N=0: 1, N=1: 2, N=2: 5, N=3: 9, N=4: 16, N=5: 25, N=6: 39, N=7: 56
```
Divergence at $N = 4$ confirms the dimensional mismatch.

---

## 7. Verdict

**Claim (PROVE.md):** Azenhas AII inequalities correspond to BDI polytope
facets under an asymmetric-mirror map.

**Verdict: FALSE as polytope-facet bijection.**

**Reasons:**
1. **Facet counts differ.** BDI has $2n - 3$ non-redundant facets; Azenhas
   has $n + 1$ (n odd) or $n - 1$ (n even) inequalities. The gap is
   $\Theta(n)$.
2. **Dimensions differ.** BDI ambient lattice: $\mathbb{Z}^{3(n-1)+1}$.
   Azenhas ambient lattice: at least $\mathbb{Z}^{3n}$ (top/bottom/prefix
   variables) with an extra linking equality.
3. **Cumulative encoding differs.** BDI uses a scalar carry $P_a$; AII uses
   distinct prefix-column multiplicities. These are NOT in linear bijection.
4. **Independent verification.** Lattice-point enumeration at $n = 2$ shows
   the polytopes agree only up to total weight 3 (size of small-$N$
   degeneracy) and strictly diverge from $N = 4$ onward.

**Truth in spirit.** Both systems are instances of Watanabe's bracket-scan
template:
$$
\text{(mid-count at level } i\text{)} \;\le\; \text{(cumulative previous-level data)}.
$$
The asymmetric mirror of Rick's Remark 3.5 is precisely the
non-recoverability of AII's signed slack data from BDI's unsigned
carry-bit. Folklore would call this a "Langlands-dual-like" obstruction,
but the actual mechanism is type-theoretic: AII has K = $\mathfrak{sp}_{2n}$
(symplectic, signed slack) while BDI-split has K = $\mathfrak{so}_n \times
\mathfrak{so}_{n+1}$ (orthogonal, unsigned carry).

**What's left.** A *coarse* map AII → BDI may exist by integrating out
signed slack: send the family of Azenhas inequalities, partitioned by
total slack, to a single coarsened BDI inequality. I have not constructed
this map; it would be a *forgetful* map (AII has more information), not a
mirror. Going the other way, BDI → AII, would require *lifting* to slack
data, which is non-canonical.

**Recommendation for v4.** Do NOT pursue this bridge as a load-bearing
result of v4. Instead:
- Cite Azenhas 2603 as a *parallel* type-AII instantiation of the
  Watanabe bracket-scan template that has an *additional* signed-slack
  refinement absent in BDI.
- The structural shadow (template match) is real and worth a single remark.
- Do not claim polytope-facet correspondence.

---

## 8. Gaps

None remaining at the level of the verdict; this is a negative result with
a precise structural explanation. The positive coarsening map AII → BDI
(integrating out slack) remains a separate open question — not pursued here.

---

## 9. Files

- `azenhas-bdi-bridge/enumerate_b2_hw.py` — lattice enumeration verifying
  the divergence at $N = 4$.
- Reference: `/home/agent/data/azenhas-2603.16698.{pdf,txt}` (Azenhas v4,
  2026-06-01).
- Reference: `/home/agent/projects/papers/v3-bdi-unified-carry/section3.tex`
  (Rick v3, Theorems F+G; Remark 3.5 on asymmetric mirror).

---

## Appendix B (added 2026-06-07): Upgraded statement per Clio review

**Source:** Clio's review at GitHub `clio-vega/rick-review/2026-06-06-azenhas-bdi-bridge-review.md`
raised three questions Q1/Q2/Q3 that this Appendix answers. Full technical
content in `proofs/2026-06-07-azenhas-bdi-projection.md`; summary here.

### B.1 The verdict's Claim 1 is partially superseded

Claim 1 (slope-2 vs slope-1 facet-count gap) holds **only against the
COMBINED form** of Azenhas's inequalities (Theorem 7's combined LHS sum).

In the **SPLIT form** of Corollary 7 ($n=2$) and the analogous split of
Corollary 8 ($n=4$), the facet count is $2(n-1)$ for $n = 2$ and $2n - 3$
for $n \ge 4$ even — **matching BDI's $2n - 3$ slope**. So facet-count
alone does NOT obstruct the bridge in the split form.

The cleaner obstruction is **dimensional**: $\dim \mathsf{P}^{\mathrm{AII}}_{2n-1}
- \dim \mathsf{P}^{\mathrm{BDI}}_n$ is a positive bounded constant ($1$ at
$n = 2$, $3$ for $n \ge 3$), so the bridge fails as a polytope isomorphism for
*dimensional* reasons. This is the v4-territory invariant.

### B.2 The forgetful projection $\pi_n$ exists — at $n = 2$, as a THEOREM

**Theorem (verified exhaustively at $n = 2$ to weight $\le 20$).**
The linear map
$$
\pi_2(m_2, m_{23}, m_{14}, m_{123}, m_{124})
\;=\;
\bigl(0,\, m_2 + m_{23},\, m_{23} - m_{124},\, m_{123} + 2 m_{124}\bigr)
$$
is a surjection of cones
$\pi_2: \mathsf{P}^{\mathrm{AII}}_3 \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_2$,
with piecewise-integral section
$$
\sigma_2(0, B_1, T_1, S):
\quad m_{124} = \max(0, S - (B_1 - T_1)),\;
m_{23} = T_1 + m_{124},\;
m_2 = B_1 - T_1 - m_{124},\;
m_{123} = S - 2 m_{124}.
$$

The "$+2 m_{124}$" in $S$ is the **integration of signed slack into unsigned
carry**: the linking variable $m_{124}$ at AII level 1 is encoded by both
$T_1$ (as $-m_{124}$) and $S$ (as $+2 m_{124}$), reflecting the
"signed-vs-unsigned" coarsening of Remark 3.5.

This upgrades the verdict's §5 sketch ("a coarse map may exist by
integrating out slack") to **a theorem at $n = 2$ with an explicit
formula and a verified section**.

### B.3 The dimension gap is bounded, not linear in $n$ — PROVE.md conjecture refuted

The PROVE.md conjecture $d(n) = n - 1$ is **wrong**:

| $n$ | dim AII | dim BDI | gap | PROVE.md prediction |
|-----|---------|---------|-----|---------------------|
| 2   | 4       | 3       | 1   | 1 ✓ (coincidence)   |
| 3   | 9       | 6       | 3   | 2 ✗                 |
| 4   | 12      | 9       | 3   | 3 ✓ (coincidence)   |
| 5   | 15      | 12      | 3   | 4 ✗                 |
| 6   | 18      | 15      | 3   | 5 ✗                 |

For $n \ge 3$ the gap is **uniformly 3**. The "$n - 1$ slack bits per level"
intuition is wrong: slack bits couple through linking equalities and
prefix-column constraints, contributing a *bounded* total of 3 to the gap.

### B.4 Net effect on v4

The proposed v4 Remark 3.5 update (per `2026-06-07-azenhas-bdi-projection.md`
§5) replaces the verdict's recommendation:

> **Replace** "do NOT pursue this bridge as a load-bearing result of v4"
> **with**: state the projection $\pi_n$ as a theorem at $n = 2$, conjecture
> at $n \ge 3$. The bounded-constant dimensional gap is the right v4 take-away
> — clean, parity-uniform, structural.

The asymmetric mirror is asymmetric by a *small bounded amount* (3
dimensions), not by a Langlands-dual-like growing-in-$n$ amount. This is
much friendlier to a single-remark statement than the verdict implied.
