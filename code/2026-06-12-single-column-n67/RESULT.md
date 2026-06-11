# OQ-PI3-GROWTH branch (a): single-column lemma at n=6, n=7

**Day 65, 2026-06-12. Task C.**

## Setting

Day-62 closed OQ-PI3-GROWTH branch (a) — the "single-column lemma" —
at $n \in \{2, 3, 4\}$. Day-64 extended to $n = 5$. Branch (a) says:
for every $g \in \mathsf{P}^{BDI}_n \cap \mathbb{Z}^{3n-3}$, the
"single-column piece"
$$\pi^{(g)}(p) \;:=\; p[\text{long}[1]] \cdot g$$
is a valid integer-PL piece, i.e. it maps every AII lattice point
to a BDI-feasible lattice point.

## Why it must hold (and why we test anyway)

$\mathsf{P}^{BDI}_n$ is a rational polyhedral cone: all defining
constraints
$$T_a \le B_a,\quad P_a := 2\textstyle\sum_{b\le a}(B_b - T_b) \ge 0,
\quad M_a \le \min(P_{a-1}, P_a),\quad S \le P_{n-1},\quad \text{all vars} \ge 0$$
are linear with integer coefficients, and there are no equations.
Hence the cone is closed under nonneg integer scaling: $g$ feasible
$\Rightarrow k\cdot g$ feasible for all $k\in\mathbb{Z}_{\ge 0}$.
Since $p[\text{long}[1]] \ge 0$ for AII lattice $p$, the lemma is
**structurally automatic** at every $n$.

The remaining check is that **long[1] is a free AII variable** —
appears in no Main$_i$ inequality and no Cor 8 linking equation — at
$n = 6, 7$. If so, $p[\text{long}[1]]$ can take any non-negative
integer value, and the construction is unconstrained.

## Free-variable check

| $n$ | parity | long[1] in any Main$_i$? | long[1] in link eq? | **is_free** |
|-----|--------|--------------------------|---------------------|-------------|
| 6   | even   | False                    | False               | **TRUE**    |
| 7   | odd    | False                    | False               | **TRUE**    |

At $n = 6$ (even), the Cor 8 linking equation is
$\text{linkLHS} = \sum_{i=1}^{n-1} \text{short}[i]$ — does not
involve long[1]. The Main$_i$ inequalities for $i = 2, \ldots, n$
involve $\text{long}[i] + \text{short}[i] \le \text{prefix}[i-1]$,
which never has $i = 1$. Verified directly via the
`aii_structure` matrices.

## Single-column sampling test

Procedure (see `single_column_n67.py`):

1. Sample 100 random BDI-feasible lattice points $g$ with
   $|g|_1 \le 10$, at each of $n = 6, n = 7$.
2. Verify each $g$ is itself BDI-feasible (sanity).
3. For each $g$ and each scaling $k \in \{0, 1, \ldots, 10\}$,
   verify $k \cdot g$ remains BDI-feasible via the explicit
   `bdi_n_feasible` predicate.

### Results

| $n$ | pass | fail |
|-----|------|------|
| 6   | **100 / 100** | 0 |
| 7   | **100 / 100** | 0 |

All 200 sampled $g$'s, scaled by $k \in [0,10]$, give BDI-feasible
$k g$. **The single-column lemma holds at $n = 6, 7$.**

This is now **confirmed for $n \in \{2, 3, 4, 5, 6, 7\}$**.

## Status of OQ-PI3-GROWTH branch (a)

Closed cleanly at $n \le 7$ by direct computation. The structural
explanation (BDI is a cone) makes this trivially true at all $n$;
the empirical extension just verifies the explicit predicate.

No Day-66 PROVE candidate from this task — the structural truth is
clean.

## Files

- `single_column_n67.py` — sampler + feasibility predicate
- `results.json` — full per-sample data
