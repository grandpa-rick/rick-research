---
title: Day 120 — General-d Frontier for StructB
status: EXPLORATORY — numerical verification through j = 12, structural insights, no closed proof yet.
---

# Day 120 — General-d Frontier

## §0. Setup recap

For j ≥ 1, the slice polynomial

$$S_j = \sum_{\mu \,:\, |\mu| = 2j,\; \ell(\mu) \le 3} K_{\mu', (2^j)} \, s^*_\mu(u, y, c).$$

StructB claim: $\deg_{u,\pi}(S_j) \le j$, i.e.
$$[t^d]\, S_j(u = t,\; \sigma = s,\; \pi = t) = 0 \quad\text{for all } d > j,$$
as polynomials in $s$.

Day 118 established $d_\mu = \mu_1 + \lfloor(\mu_2 + \mu_3)/2\rfloor$.
Day 119 handled $d = d_{\max}$: the top-$t$ part is a pure combinatorial
identity split by parity of $\mu_2 - \mu_3$ into identities (A) even and
(B) odd, each vanishing separately.

**The Day 120 question:** what about $j < d < d_{\max}$?

## §1. Support geometry (the "d-staircase")

Systematic enumeration (`code/day120/d_level_support.py`) reveals:

For each $j \ge 4$, the support $\{\mu : |\mu|=2j, K_{\mu',(2^j)} > 0\}$ occupies
only 2 or 3 consecutive levels $d_\mu \in \{d_{\max}, d_{\max}-1, d_{\max}-2\}$.

| $j$ | $d_{\max}$ | levels present | 
|-----|-----------|-----------------|
| 4 | 6 | {6, 5} |
| 5 | 7 | {7} |
| 6 | 9 | {9, 8} |
| 7 | 10 | {10, 9} |
| 8 | 12 | {12, 11} |
| 9 | 13 | {13, 12} |
| 10 | 15 | {15, 14, 13} |
| 11 | 16 | {16, 15} |
| 12 | 18 | {18, 17, 16} |

**Consequence.** For each $d \in (j, d_{\max}]$, contributors are $\mu$ with
$d_\mu - d \in \{0, 1, 2\}$ only (typically 0 and 1, sometimes 0, 1, 2, or 1, 2).

This means the coupling is much less severe than feared: the identity $[t^d] S_j = 0$
couples at most **three consecutive d-layers** of the staircase.

## §2. Empirical verification

`code/day120/general_d_verification.py` verifies $[t^d] S_j = 0$ for all
$d > j$ empirically for $j \in \{3, 4, 5, 6, 7\}$, and `general_d_coupling.py`
prints the explicit coupled identity for $j \in \{3, 5, 7\}$.

**Example (j = 5, d = 6, delta_range = {1}):** All contributors have $d_\mu = 7$.
Their contributions $K \cdot [t^6] s^*_\mu$ sum to 0:

- $\mu=(4,3,3), K=5$: $[t^6]s^* = -2s - 10$
- $\mu=(4,4,2), K=6$: $[t^6]s^* = s^2 - 7s + 27$
- $\mu=(5,3,2), K=5$: $[t^6]s^* = 104 - 21s$
- $\mu=(5,4,1), K=4$: $[t^6]s^* = s^3 - 12s^2 + 86s - 249$
- $\mu=(5,5,0), K=1$: $[t^6]s^* = -4s^3 + 42s^2 - 187s + 364$

Sum weighted by $K$: $(-10s-50)+(6s^2-42s+162)+(520-105s)+(4s^3-48s^2+344s-996)
+(-4s^3+42s^2-187s+364) = 0$. ✓

**Example (j = 7, d = 8, delta_range = {1, 2}):** TWO layers couple.
Sum of $K \cdot [t^8]s^*_\mu$ over 8 shapes equals 0.

## §3. The **CRITICAL** finding: parity split FAILS below $d_{\max}$

`code/day120/parity_split.py`. Define
$$A_{sum}(j, d) := \sum_{\mu : (\mu_2 - \mu_3)\text{ even}} K \cdot [t^d] s^*_\mu,\qquad
B_{sum}(j, d) := \sum_{\mu : (\mu_2 - \mu_3)\text{ odd}} K \cdot [t^d] s^*_\mu.$$

Then $A_{sum} + B_{sum} = 0$ always (StructB claim), but for **$d < d_{\max}$**,
$$A_{sum}(j, d) = -B_{sum}(j, d) \ne 0.$$

Examples:
- $j=4, d=5$: $A_{sum} = 12 - 3s$, $B_{sum} = 3s - 12$.
- $j=5, d=6$: $A_{sum} = 6s^2 - 52s + 112$, $B_{sum} = -A_{sum}$.
- $j=7, d=8$: $A_{sum} = 15s^4 - 310s^3 + 2601s^2 - 10203s + 13631$, $B_{sum} = -A_{sum}$.

**This is the main structural change from the top-degree identity.** At
$d = d_{\max}$ the even/odd blocks vanish independently (Day 119). At $d < d_{\max}$,
they only cancel each other.

### s-degree structure

For offset $k = d_{\max} - d$:
- $k=0$: $A_{sum} \in \{0, \pm 1\}$.
- $k=1$: $A_{sum}$ has degree $\le 2$ in $s$.
- $k=2$: degree $\le 4$.
- $k=3$: degree $\le 6$.

The leading coefficient in $s$ scales like $\binom{j-1}{k}$-type numbers:
- j=6, k=1: leading 4; k=2: leading -10.
- j=7, k=1: leading -10; k=2: leading 15.
- j=8, k=1: leading -5; k=2: leading 20; k=3: leading -21.
- j=9, k=1: leading 15; k=2: leading -35; k=3: leading 28.

These are ballot-adjacent numbers (10 = C(5,3), 21 = C(7,2), 28 = C(8,2), etc.)
and suggest an underlying Catalan/ballot structure — but the exact closed form
is not yet identified.

## §4. Subleading expansion (partial closed forms)

`code/day120/subleading_expansion.py` and `subleading_family.py` compute
$[t^{d_\mu - k}] s^*_\mu(t, s, t)$ for many spine-type $\mu = (a, b, c)$.

### Family $\mu = (a, 0, 0)$, $d_\mu = a$

- $[t^{d-0}] = 1$ (top: Day 119).
- $[t^{d-1}] = s - T_a$ where $T_a = 3, 7, 11, 16, 22, 29, 37, 46, 56$ for $a=1,\ldots,9$.
  - For $a \ge 2$: $T_a = 1 + \binom{a+2}{2}$.
- $[t^{d-2}] = s^2 - (T_a+1) s + Q_a$ where $Q_a$ has a manageable pattern.

### Family $\mu = (a, 1, 1)$, $d_\mu = a + 1$

- $[t^{d-0}] = 1$.
- For $a \ge 3$: $[t^{d-1}] s^*_{(a,1,1)} = s - T_a$ **coincides** with $(a,0,0)$'s.
- $[t^{d-2}]$ also matches $(a,0,0)$'s for $a \ge 4$.

**This "stabilization" pattern** (subleading of $(a, 1, 1)$ = subleading of
$(a, 0, 0)$ for large enough $a$) is a strong hint of the coupling mechanism —
the "same" polynomial in $s$ appears from both a leading and a subleading contribution.

### Family $\mu = (a, 1, 0)$

- $[t^{d-0}] = s - 1$.
- $[t^{d-1}] = s^2 - T_a \cdot s + T_{a-1}?$ - has factor $(s-1)$ for $a \ge 5$:
  $[t^{d-1}] s^*_{(a,1,0)} = (s - T_a)(s - 1) + \text{small}$ pattern.

Full closed forms not yet extracted; these are exploratory.

## §5. Coupled system for small $j$

For $j = 3$ (`code/day120/general_d_coupling.py`): only one nontrivial $d$, namely
$d = 4 = d_{\max}$, which is Day 119's identity.

For $j = 5$: two nontrivial identities.
- $[t^7] S_5 = 0$ (top, Day 119).
- $[t^6] S_5 = 0$: all 5 contributors at delta=1.

For $j = 7$: three nontrivial identities at $d = 8, 9, 10$, with delta ranges
$\{1, 2\}, \{0, 1\}, \{0\}$ respectively.

Explicit polynomial equations are printed in `general_d_coupling.py` output.

## §6. Involution search results

`code/day120/involution_search.py` and `involution_v2.py` tested candidate
shape-pairings including:
- $(a,b,c) \leftrightarrow (a-1, b+1, c)$: row1→row2 slide.
- $(a,b,c) \leftrightarrow (a-1, b, c+1)$: row1→row3 slide.
- $(a,b,c) \leftrightarrow (a, b+1, c-1)$: row2→row3 slide.
- Bender-Knuth-style flips on $\mu'$.

**None of these give a fixed-point-free involution on the entire support with
parity-flip and $K$-preservation.** Each has 2-5 unpaired elements.

Kostka coincidences $K_\mu = K_\nu$ with different parity exist (e.g., j=5,
$K_{(4,3,3)} = K_{(5,3,2)} = 5$), but only sporadically — no global rule.

**Brick wall.** The vanishing $[t^d] S_j = 0$ (at $d < d_{\max}$) does NOT
appear to come from a shape-preserving Garsia-Milne involution at the level of
partitions with 3 parts. The vanishing must come from a deeper cancellation
involving both the Kostka numbers AND the polynomial coefficients $[t^d]s^*_\mu$.

## §7. Summary and what's open

**Positive findings:**
1. Support geometry: only 2-3 d-levels are populated per $j$; coupling is bounded.
2. Parity split fails: $A_{sum}(j, d) = -B_{sum}(j, d) \ne 0$ for $d < d_{\max}$.
   This is the essential coupling mechanism.
3. Subleading closed form: $[t^{d-1}] s^*_{(a,0,0)} = s - T_a$ with
   $T_a = 1 + \binom{a+2}{2}$ for $a \ge 2$. Similar for $(a,1,1)$, $(a,1,0)$.
4. General-$d$ verified empirically for $j \le 7$, and the coupled identity
   printed in `general_d_coupling.py`.

**Negative findings:**
- No simple shape involution explains the vanishing.
- Leading coefficients of $A_{sum}(j, d)$ suggest Catalan/ballot structure but
  the exact closed form is not yet found.

**Where to go next:**
- **Path A (recommended):** attack the identity $A_{sum}(j, d) + B_{sum}(j, d) = 0$
  directly. This is a polynomial identity in $s$ of controlled degree.
  Try: express both sides via generating functions in $(a, b, c)$-shape parameters.
- **Path B:** look for a Bender-Knuth-Krattenthaler-style involution on the
  larger set of SSYT/skew-tableaux underlying both $K_{\mu', (2^j)}$ AND the
  $[t^d] s^*_\mu$ substitution (both sides are combinatorial sums over
  tableau-like objects).
- **Path C:** prove StructB via a more direct manipulation of the determinantal
  formula for $s^*_\mu$ in the $(u, \sigma, \pi)$-substitution, avoiding the
  Kostka expansion entirely.

## §8. Files created (all in `code/day120/`)

- `general_d_verification.py` — verify $[t^d] S_j = 0$ empirically ($j \le 7$).
- `general_d_coupling.py` — print explicit coupled identity for $j = 3, 5, 7$.
- `d_level_support.py` — d-staircase enumeration for $j \le 12$.
- `subleading_expansion.py` — subleading coefficient tables.
- `subleading_family.py` — differences across $a$-family, closed-form hunt.
- `parity_split.py` — the crucial "parity split fails" experiment.
- `parity_partial_structure.py` — s-degree and leading-coef of $A_{sum}(j,d)$.
- `involution_search.py`, `involution_v2.py` — candidate pairings.
- `kostka_involution.py` — Kostka coincidences (sparse, not exploitable).

## §9. Honesty note

**This is a hard frontier.** The parity split at $d = d_{\max}$ turned out to be
special — it does NOT generalize. The general-$d$ case requires a genuinely
different kind of argument (or a deeper involution) that couples parities.
Progress today is largely **structural clarification**: we now know the
coupling is small (2-3 layers), we know the parity block sums are equal-and-
opposite (not zero), and we have closed forms for the "generic" subleading
terms. But an actual proof of $[t^d] S_j = 0$ for $d < d_{\max}$ remains open.

— Compute agent, Day 120.
