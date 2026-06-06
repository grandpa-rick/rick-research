# Other Faces of the BDI Kobayashi Polytope at $B_n$

**Date.** 2026-05-21 (Day-28 deep work)
**Author.** Rick.
**Status.** Verdict: refined-F3' (intermediate between F2 and F3 in the prior). T-verdict
**confirmed** with two type-uniform exceptions.

## Problem statement (recap)

Let $\pi$ be a Kostant partition at $B_n$ with chain-factor coordinates
$$(M_a, B_a, T_a)_{a=1}^{n-1}, \qquad S.$$
By Theorem A (v2 §1), $\pi$ is $B_n$-highest iff the carry-recursive system holds:
$$(\mathrm{HW})\quad
\begin{cases}
L_a : M_a \le P_{a-1} & (a=1,\dots,n-1)\\
U_a : M_a \le P_a     & (a=1,\dots,n-1)\\
E   : S \le P_{n-1}   &
\end{cases}
\qquad P_a = P_{a-1} + 2(B_a - T_a), \quad P_0 = 0.$$

So the HW chain polytope $\mathcal{P}_n \subset \mathbb{Z}_{\ge 0}^{3(n-1)+1}$ is defined by
$2n - 1$ candidate facet inequalities plus non-negativity.

**Kobayashi 2604.22262** asserts the BDI branching multiplicity function is piecewise-linear,
governed by a polyhedral system of "fences." The question is whether the $2n-1$
carry-derived inequalities of (HW) exhaust the chain-side description of that polytope.

## Theorem (BDI carry-fence facet structure).

Let $n \ge 2$. Among the $2n - 1$ carry-derived candidate fences:

1. **$L_1$** is a **dimension-collapsing constraint**: it is non-redundant in the
   inequality system, but on every HW chain configuration $M_1 = 0$. Equivalently,
   $\mathcal{P}_n$ lies in the affine subspace $\{M_1 = 0\}$ of codimension 1 in
   $\mathbb{R}^{3(n-1)+1}$.

2. **$U_1$** is **redundant**: it is implied by the conjunction of $L_1$, non-negativity
   of $M_2$ (for $n \ge 3$) or $S$ (for $n = 2$), and the corresponding fence ($L_2$ or $E$).

3. The remaining $2n - 3$ inequalities,
   $$\{L_a, U_a : 2 \le a \le n-1\} \cup \{E\},$$
   are **non-redundant facets** of $\mathcal{P}_n$ (codimension-1 faces of the full-dim
   polytope $\mathcal{P}_n \subset \{M_1 = 0\}$).

## Proof.

**(1) $L_1$ degenerate.** $L_1$ is $M_1 \le P_0 = 0$. Combined with $M_1 \ge 0$, this
forces $M_1 = 0$ for every HW configuration. $L_1$ itself is *non-redundant* as an
inequality: the configuration $M_1 = 1, B_1 = 1$ (all else zero) satisfies every other
inequality (computation: $P_1 = 2$, so $L_a, U_a$ for $a \ge 2$ have $M_a = 0 \le 2$ and
$E$ has $S = 0 \le 2$). So we *need* $L_1$, but on $\mathcal{P}_n$ it is always tight,
collapsing dimension 1.

**(2) $U_1$ redundant.** $U_1$ is $M_1 \le P_1 = 2(B_1 - T_1)$. By (1), $M_1 = 0$, so
$U_1$ becomes $P_1 \ge 0$.

- *Case $n = 2$.* Fence $E$ reads $S \le P_1$, and $S \ge 0$, so $P_1 \ge S \ge 0$.
- *Case $n \ge 3$.* Fence $L_2$ reads $M_2 \le P_1$, and $M_2 \ge 0$, so $P_1 \ge M_2 \ge 0$.

In both cases the other carry inequalities together with non-negativity force $P_1 \ge 0$,
hence $U_1$.

**(3) $L_a, U_a$ ($2 \le a \le n-1$), and $E$ are non-redundant facets.**

For each, we exhibit a chain configuration that satisfies all *other* inequalities of
(HW) ∪ {non-negativity} but violates the named one. (Existence of such a witness
implies the inequality is needed; the saturation locus is then a codim-1 face.)

- **Witness for $L_a$** ($2 \le a \le n-1$): set $M_a = 1$, $B_a = 1$, and all other
  coordinates 0. Then $P_b = 0$ for $b < a$ and $P_b = 2$ for $b \ge a$. Check:
  - $L_b, U_b$ for $b < a$: $M_b = 0 \le 0$. ✓
  - $L_a$: $M_a = 1 \le P_{a-1} = 0$? **No** — violated. ✓
  - $U_a$: $M_a = 1 \le P_a = 2$. ✓
  - $L_b, U_b$ for $b > a$: $M_b = 0 \le 2$. ✓
  - $E$: $S = 0 \le P_{n-1} = 2$. ✓

- **Witness for $U_a$** ($2 \le a \le n-1$): set $M_a = 1$, $B_{a-1} = 1$, $T_a = 1$, and
  all other coordinates 0. Then $P_b = 0$ for $b < a-1$, $P_{a-1} = 2$, and $P_b = 0$
  for $b \ge a$. Check:
  - $L_b, U_b$ for $b < a-1$: $M_b = 0 \le 0$. ✓
  - $L_{a-1}$: $M_{a-1} = 0 \le P_{a-2} = 0$. ✓
  - $U_{a-1}$: $M_{a-1} = 0 \le P_{a-1} = 2$. ✓
  - $L_a$: $M_a = 1 \le P_{a-1} = 2$. ✓
  - $U_a$: $M_a = 1 \le P_a = 0$? **No** — violated. ✓
  - $L_b, U_b$ for $b > a$: $M_b = 0 \le 0$. ✓
  - $E$: $S = 0 \le P_{n-1} = 0$. ✓

- **Witness for $E$**: set $S = 1$, all chain coordinates 0. Then $P_{n-1} = 0$:
  - All $L_a, U_a$: $M_a = 0 \le 0$. ✓
  - $E$: $S = 1 \le 0$? **No** — violated. ✓

For each fence, the witness exhibits exactly one violated inequality, proving
non-redundancy.

**Achievability of saturation.** The zero configuration $M = B = T = 0, S = 0$ satisfies
all $2n - 1$ candidate inequalities with equality, so each is *achievable* with equality
on $\mathcal{P}_n$.

**Facet (codim-1) verification.** Non-redundancy alone implies *some* face of dim
$\ge d - 1$ on the saturation locus, but we want the saturation locus to have a relative
interior point (the strongest form: full codim-1). Type-uniform interior witnesses for
$n \ge 3$:

- **$L_a$ interior** ($2 \le a \le n-1$): $B_b = 1$ for $1 \le b \le a-1$, $M_a = 2(a-1)$,
  $B_a = 1$, all else 0. Then $P_b = 2b$ for $0 \le b \le a-1$, $P_a = 2a$, $P_b = 2a$
  for $a \le b \le n-1$. $L_a$ saturated ($M_a = 2(a-1) = P_{a-1}$); all other inequalities
  strict.

- **$U_a$ interior** ($3 \le a \le n-1$): same prefix $B_b = 1$ for $1 \le b \le a-1$, then
  $M_a = 2(a-2), T_a = 1, B_a = 0$, all else 0. Then $P_{a-1} = 2(a-1), P_a = 2(a-1) - 2 = 2(a-2)$.
  $U_a$ saturated ($M_a = P_a$); $L_a$ strict ($M_a < P_{a-1}$); all others strict.

- **$U_2$ interior** (special case): $B_1 = 2, M_2 = 2, T_2 = 1$, all else 0.
  $P_1 = 4, P_2 = 2$. $U_2$ saturated; $L_2$ strict ($2 < 4$); others strict.

- **$E$ interior**: $B_b = 1$ for $1 \le b \le n-1$, $S = 2(n-1)$, all else 0. Then
  $P_{n-1} = 2(n-1) = S$; all $L_b, U_b$ have $M_b = 0$ and $P_b > 0$, so strict.

These witnesses (verified at $n = 3, ..., 7$ in `verify_facet_interiors.py`) place a HW
configuration in the relative interior of each facet, confirming each is genuinely
codim-1 in $\mathcal{P}_n$.

(For $n = 2$ only $E$ is a candidate facet, and the interior witness $B_1 = 1, S = 2$ has
$E$ saturated and all else strict.)

$\square$

## Computational verification.

The script `classify_fences.py` enumerates all chain configurations $(M, B, T, S)$ with
total content $\le C$ and classifies each candidate fence by:

  - `Sat`: # HW configs that saturate it;
  - `Strict`: # HW configs that strictly satisfy it;
  - `Nonred`: # configs that satisfy every *other* fence but violate this one
    (any positive count proves non-redundancy in the enumerated range).

Results:

| $n$ | $C$ | total configs | HW configs | $L_1$ | $U_1$ | $L_2$ | $U_2$ | $L_3$ | $U_3$ | $L_4$ | $U_4$ | $L_5$ | $U_5$ | $E$ |
|----:|----:|--------------:|-----------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|----:|
| 2   | 8   | 495           | 64         | deg   | red   |       |       |       |       |       |       |       |       | 31  |
| 3   | 6   | 1716          | 286        | deg   | red   | 51    | 9     |       |       |       |       |       |       | 44  |
| 4   | 6   | 8008          | 1366       | deg   | red   | 204   | 24    | 81    | 37    |       |       |       |       | 114 |
| 5   | 4   | 2380          | 530        | deg   | red   | 48    | 4     | 28    | 7     | 16    | 9     |       |       | 32  |
| 6   | 3   | 969           | 241        | deg   | red   | 13    | 1     | 10    | 2     | 7     | 3     | 4     | 4     | 18  |

(Cell entries = `Nonred` counts; "deg" = saturated by all HW configs; "red" = no
config violates ONLY this one.)

All non-redundancy witnesses are explicitly verified at $n = 2, \dots, 7$ in
`verify_witnesses.py`. At every checked $n$, the structure
{$L_1$ degenerate, $U_1$ redundant, all others facets} holds.

## Connection to Kobayashi's framework.

Kobayashi 2604.22262 §1–3 establishes that BDI branching multiplicities are governed by
piecewise-linear "fences" in parameter space, on the complement of which the multiplicity
function is locally a polynomial in the parameters.

Our theorem identifies the **chain-side description** of these fences: each non-redundant
carry-derived facet of $\mathcal{P}_n$ projects under the chain → weight map to a
candidate Kobayashi fence in weight space.

Theorem E (Day-26 result, $S \le P_{n-1}^{\text{cum}}$) is precisely the $E$-facet of
$\mathcal{P}_n$ — **one face out of $2n - 3$ carry-derived facets**. The other
$2n - 4$ are the "MB-bound" pairs $L_a, U_a$ for $a = 2, \dots, n-1$.

Counts:
- $B_2$: 1 carry-facet ($E$ only — degenerate base case).
- $B_3$: 3 carry-facets ($L_2, U_2, E$).
- $B_4$: 5 carry-facets ($L_2, U_2, L_3, U_3, E$).
- $B_n$: $2n - 3$ carry-facets.

**Verdict on F1 / F2 / F3 (PROVE.md priors).**

- F1 ("single-fence cone, P=15%"): refuted. $2n - 3 \ge 1$ facets exist.
- F2 ("partial framework, P=25%"): refuted. All non-redundant facets are carry-derived,
  none requires the NT block or algebra-side input.
- F3 ("full $2n - 1$ from carry, P=60%"): partially confirmed. The $2n - 1$ candidates
  do exhaust the carry-derived list, but two of them are special ($L_1$ degenerate,
  $U_1$ redundant), giving $2n - 3$ honest facets, not $2n - 1$.

Call it **F3'**: refined F3 with type-uniform exceptions at the first chain.

## Why does the first chain misbehave?

$L_1$ degenerate, $U_1$ redundant — this is a feature, not a bug. The carry recursion
**starts** at $P_0 = 0$, so the first chain has no incoming carry, and the constraints
$L_1: M_1 \le 0$ and $U_1: M_1 \le P_1$ become asymmetric:

- $L_1$ is the **strongest** form of the leading-paren bound ($M_1 \le 0$ is as tight
  as it gets); it forces $M_1 = 0$, removing the *mid* root $E_1$ from chain 1
  entirely.
- $U_1$ is then the **slack** form: $0 \le P_1$, which is "$\sum$-stays-non-negative" —
  enforced by the *next* constraint downstream ($L_2$ or $E$).

This is the boundary behavior of the recursion. Internally ($2 \le a \le n-1$), both
$L_a$ and $U_a$ are honest constraints because $P_{a-1}$ and $P_a$ can take a range of
positive values, neither universally tighter than the other.

## Additional facets (non-negativity).

The carry-derived count $2n - 3$ is *not* the full facet count of $\mathcal{P}_n$;
non-negativity contributes additional facets (each of $M_a \ge 0$ for $a \ge 2$,
$B_a \ge 0$, $T_a \ge 0$, $S \ge 0$ — modulo redundancies). E.g., at $B_2$ the polytope
has 3 facets total: $\{T_1 = 0\}, \{S = 0\}, \{S = 2(B_1 - T_1)\}$.

Whether all non-negativity facets are non-redundant for general $n$ is a separate
question, not addressed here. The PROVE focused on the carry-derived candidates and
that question is now settled.

## Type-uniform corollary.

**Corollary.** The chain-side carry framework predicts that the BDI Kobayashi polytope
at $B_n$ has exactly $2n - 3$ non-redundant carry-derived facets (plus non-negativity
boundary contributions). The Day-26 Theorem E ($E$-facet) is one of them; the other
$2n - 4$ split into $n - 2$ "leading" facets $L_a$ and $n - 2$ "upper" facets $U_a$
for $a = 2, \dots, n - 1$.

In particular: the chain-factor framework is *complete* for the carry-derived part of
the polytope — no extra fences from the NT block or algebra-side Watanabe multiplicity
are needed to fill in the carry-derived face structure. (Whether NT or algebra-side
contribute *additional* fences via weight-space projection is a separate question for
Day-29+.)

## Gaps.

1. **Weight-space projection.** Whether each of the $2n - 3$ chain-facets projects to a
   *distinct* Kobayashi fence in weight space, or whether some collapse, is not
   addressed here. Step 4 of the original PROVE strategy.

2. **Total facet count of $\mathcal{P}_n$.** The non-negativity facets are not
   classified for redundancy beyond the $B_2$ case.

3. **The NT block.** Since NT roots are free under the $B_n$ action, they do not
   contribute carry-derived constraints. But the weight-space projection mixes them
   in, possibly producing additional weight-space fences not captured by chain
   coordinates alone.

These three are Day-29+ stretch questions, downstream of the Day-28 verdict.

## Files.

- `2026-05-21-bdi-kobayashi-faces/classify_fences.py`: enumeration + classification.
- `2026-05-21-bdi-kobayashi-faces/verify_witnesses.py`: type-uniform non-redundancy witness verification ($n \le 7$).
- `2026-05-21-bdi-kobayashi-faces/verify_facet_interiors.py`: type-uniform facet-interior witness verification ($n = 3, ..., 7$).

## Whiskey rule.

Framing was the work. "The carry already lists the candidate fences; the question is
which survive" — and the answer is "all but two boundary-effect ones." Type-uniform,
parameter-free, derived directly from Theorem A. Same shape as Theorem E itself:
inevitable once you stare at the recursion long enough.

— Rick
