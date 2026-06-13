# Day 69 CODE Task 1 — Azenhas AII wall count, computed

## Goal

Substantiate the v4 §3 AII-vs-BDI structural contrast with explicit
facet counts from the published Azenhas Theorem D / Theorem E
inequalities (arXiv:2603.16698v5 sec 3, eq.107 at n=3).

Browse 59 (Day 68) seeded the prediction "$\sim 2(n-1)$ AII walls".
This computation **disconfirms that growth rate** — the true scaling
is $\Theta(n)$ but with leading coefficient **3**, not 2, and the
parity offset is $-[n\text{ even}]$.

## Method

For each $n \in \{3, 4, 5, 6, 7, 8\}$:

1. Build the AII cone H-representation in column-multiplicity
   coordinates (3n variables; see `make_vars`).
2. Encode Azenhas Theorem D (odd $n$) / Theorem E (even $n$) Main
   inequalities + positivity. Two parallel encodings:
   - **strict (eq. 107)**: (n-2) type-(97) + 2 type-(98) (the sandwich)
     + positivity. At even $n$, add the Cor 8 linking equation.
   - **aii_structure (Day-60)**: simplified Main_i form
     `long[i]+short[i] ≤ prefix[i-1]` for i=2..n,
     same linking equation at even n.
3. Build BDI cone H-representation (3n-3 variables; T,B,M,S vars +
   T≤B + partial-sum positivity + M ≤ both P bounds + S ≤ P_{n-1}).
4. **Count facets** via LP-based redundancy elimination: an
   inequality $a_i^T x \le b_i$ is a facet iff
   $\max\{a_i^T x : a_j^T x \le b_j \forall j \ne i, A_{eq} x = b_{eq},
   -1 \le x_k \le 1\}$ exceeds $b_i$ by a positive tolerance.

Both encodings give the same facet count — the (98) lower bound is
already implied by positivity + the (98) upper bound, so the strict
version has one more inequality but the same number of irredundant
facets.

## Results

| $n$ | AII strict | AII aii_str | BDI walls | $2(n-1)$ predict |
|----:|----:|----:|----:|----:|
| 3  |  9 |  9 |  7 |  4 |
| 4  | 11 | 11 | 11 |  6 |
| 5  | 15 | 15 | 15 |  8 |
| 6  | 17 | 17 | 19 | 10 |
| 7  | 21 | 21 | 23 | 12 |
| 8  | 23 | 23 | 27 | 14 |

## Quasi-polynomial fit

**Period-2 finite differences:**

| series | $\Delta^1$ vals | period-2 $\Delta^2$ | closed form |
|---|---|---|---|
| AII strict | $2, 4, 2, 4, 2$ | $6$ | $3n$ if $n$ odd, $3n-1$ if $n$ even |
| AII aii_str | $2, 4, 2, 4, 2$ | $6$ | same as above |
| BDI | $4, 4, 4, 4, 4$ | $8$ | $4n - 5$ |
| $2(n-1)$ | $2, 2, 2, 2, 2$ | $4$ | $2n - 2$ |

**Verification of closed forms** (Day-58 calibration: period-step
finite-diff is the only valid quasipoly test):

- AII odd $n \in \{3,5,7\}$: $9, 15, 21 = 3 \cdot \{3,5,7\}$ ✓.
- AII even $n \in \{4,6,8\}$: $11, 17, 23 = 3 \cdot \{4,6,8\} - 1$ ✓.
- BDI all $n$: $7, 11, 15, 19, 23, 27 = 4n - 5$ ✓.

The **parity-1 offset** at even $n$ in the AII count
($3n - 1$ instead of $3n$) is the same parity that drives
$f(n) = 3 - [n \text{ even}]$ in Day-58 dim-gap analysis: the
Cor 8 linking equation at even $n$ kills one positivity facet
(pos linkLHS, which is forced by sum of shorts).

## Comparison to Azenhas's claim

Browse 59 reported "$\sim 2(n-1)$ AII walls". That growth rate is
**wrong** (or at least wrong as a literal facet count). The truth:

- Facet count of AII cone = $3n - [n \text{ even}]$.
- Growth coefficient is 3, not 2.
- The "$2(n-1)$" heuristic might have been an undercount that missed
  the positivity facets entirely (since the (n-2) Main_i constraints
  + 2 type-(98) constraints sum to $n$ nontrivial walls).

## The right v4 §3 structural contrast

The "BDI has 3 walls uniformly" claim from the Day-67 proof note
(`proofs/2026-06-12-azenhas-inequalities-read.md`) does **not** refer
to the BDI cone's facet count — BDI cone has $4n - 5$ facets at level
$n$, which is also $\Theta(n)$. The 3 walls refer instead to the
three **piece-switching walls** of Rick's $\tilde\pi'_3$ projection
in the Day-62 piecewise-projection stack analysis, i.e., the three
AXIS variables $\{m_2, m_{236}, m_{23456}\}$ at $n = 3$.

So the v4 §3 paragraph should be rewritten:

> The AII multiplicity cone defined by Azenhas's Theorem D / E
> inequalities (arXiv:2603.16698v5 sec 3) has $\Theta(n)$ facets —
> computed $3n - [n \text{ even}]$ for $n = 3, \ldots, 8$ — of which
> $n$ are nontrivial Main inequalities (the long+short ≤ prefix walls
> plus the (98) sandwich). The BDI cone in Rick's $(M_a, B_a, T_a, S)$
> coordinates has $4n - 5$ facets, also $\Theta(n)$. But the
> piecewise projection $\tilde\pi'_n$ from BDI is governed by a
> **constant 3 piece-switching walls** independent of $n$ — the
> $\{m_2, m_{236}, m_{23456}\}$ AXIS variables of the Day-62
> stratification.
>
> The structural contrast is:
> - AII has $\Theta(n)$ Main inequalities (linear in $n$).
> - BDI's piecewise projection has $O(1) = 3$ piece-switching walls,
>   uniformly in $n$.
>
> i.e. **AII's algebraic complexity is per-level; BDI's piecewise
> structure is universal.**

## Sanity / calibration

- Period-2 finite differences are constant ($\Delta^2_{n,n+2} = 6$
  for AII, $= 8$ for BDI). Consistent with linear quasi-polynomial
  with period 2.
- The strict (eq.107) and Day-60 (aii_structure) encodings agree on
  the facet count, confirming the (98) lower bound is automatically
  implied by positivity + the (97) and (98)-upper.
- BDI facet count grows by 4 per step (matching addition of
  $T_n, B_n$ ineqs + $M_n$ pair + shift of $S \le P_{n-1}$).
- AII facet count grows by 2 from odd → next-even (parity offset) and
  by 4 from even → next-odd. Period-avg 3 = AII per-step growth rate.

## Files

- `azenhas_aii_walls.py` — wall enumeration code.
- `azenhas_aii_walls_results.json` — full results for $n = 3, \ldots, 8$.
- `azenhas_aii_walls_README.md` — this file.

## Status flags / open questions

- **Browse-59 heuristic "$\sim 2(n-1)$" DISCONFIRMED.** The true growth
  rate of AII facets is $3n$ (parity-corrected). Update browse note.
- **v4 §3 contrast rewritten** above to honest statement: AII has
  $\Theta(n)$ Main ineqs; BDI piecewise projection has $O(1) = 3$
  piece-switching walls.
- **OQ-AII-FACET-CLOSED-FORM CLOSED-AT-N=8:** AII facets =
  $3n - [n \text{ even}]$, BDI facets = $4n - 5$. Period-2 finite
  difference constant; closed form verified at $n = 3, \ldots, 8$.
- **Day-58 dim-gap parity $f(n) = 3 - [n \text{ even}]$ structurally
  matches the parity offset $-[n \text{ even}]$ in AII facets.** Both
  trace to the same Cor 8 linking equation at even $n$.
