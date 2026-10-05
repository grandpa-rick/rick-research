# Day 191 PROVE: $e_2(X) \star e_2(X)$ in Hikita's quantum multiplication

**Date:** 2026-09-11
**Author:** Rick
**Status:** `computed` (SymPy at $m=4$ and $m=5$, stability verified; sanity checks pass)
**Registry:** `proofs/registry/hikita-star-e2-e2.json`

---

## Problem statement

Hikita's paper *"$(q,t)$-chromatic symmetric functions"* (arXiv:2503.23597,
Definition 3.4) introduces a commutative associative multiplication $\star$ on
$\Lambda_{q,t} = \Lambda \otimes \mathbb Q(q,t)$ via

$$
F \star G \;:=\; \mathfrak q_{(m)}\bigl(\mathfrak q_{(m)}^{-1}(F)\cdot \mathfrak q_{(m)}^{-1}(G)\bigr),
$$

where $\mathfrak q_{(m)}\colon \mathbb Q_{q,t}[Y]_{(m)} \to \mathbb Q_{q,t}[X]_{(m)}$
is the linear isomorphism $F(Y) \mapsto F(Y)\bullet 1$ under the level-one
polynomial representation of the affine Hecke algebra $H_m$. His **Theorem
3.12** gives the Pieri rule for $e_1 \star e_r$:

$$
e_1(X) \star e_r(X) \;=\; (1 - q^{-1})[r+1]_t\, e_{r+1}(X) \;+\; q^{-1}\, e_1(X) e_r(X). \qquad (\text{Thm 3.12})
$$

Hikita explicitly flags the general Pieri rule for $e_a(X) \star e_r(X)$ with
$a \ge 2$ as open (arXiv:2503.23597, page 6, remark after Theorem A(iii)).

**Goal.** Compute the simplest new case: $e_2(X) \star e_2(X)$ in explicit
closed form in the ordinary $e$-basis of $\Lambda_{q,t}$.

## Main result

$$
\boxed{\;\;
e_2 \star e_2 \;=\; \frac{1}{q^2}\, e_{2,2}
\;+\; \frac{1-q^{-1}}{q}\, [2]_t\, e_{3,1}
\;+\; (1 - q^{-1})\,\bigl(1+t^2\bigr)\!\left([3]_t - \frac{t}{q}\right) e_4.
\;\;}
$$

Equivalently, in polynomial form,

$$
e_2 \star e_2 \;=\; \frac{1}{q^2}\, e_{2,2}
\;+\; \frac{(q-1)(1+t)}{q^2}\, e_{3,1}
\;+\; \frac{(q-1)(1+t^2)\bigl(q\,[3]_t - t\bigr)}{q^2}\, e_4.
$$

The coefficients of $e_{2,1,1}$ and $e_{1^4}$ are **zero**.

## Verification (computational)

Direct SymPy computation using the polynomial representation of $H_m$
(Hikita 2.9):

- **$m=4$:** compute $e_2(Y_1,\dots,Y_4)\bullet e_2(X_1,\dots,X_4)$ as a
  Laurent polynomial in $X_1,\dots,X_4$; multiply by $t^{-1}$; expand in
  the $e_\lambda$-basis of $\Lambda^{(4)}$. Result: formula above.

- **$m=5$:** same procedure, at $m=5$. Result: identical formula. The
  coefficients of $e_{2,1,1}$ and $e_{1^4}$ (which vanish at $m=4$) remain
  zero at $m=5$. **Stability confirmed.**

Script: `proofs/scripts/day191/e2_star_e2.py`,
`proofs/scripts/day191/compute_general.py`.

## Sanity checks

**At $q = 1$:** by Proposition 3.6 in Hikita, $F \star G = F \cdot G$ when
$q = 1$ (and $F$ symmetric). So $e_2 \star e_2 |_{q=1} = e_2 \cdot e_2 =
e_{2,2}$. Checking our formula:

- coefficient of $e_4$: $(1-1)(\cdots) = 0$ ✓
- coefficient of $e_{3,1}$: $(1-1)(1+t)/1 = 0$ ✓
- coefficient of $e_{2,2}$: $1/1 = 1$ ✓

**As $q \to \infty$:** Hikita's Theorem C(ii) says
$\lim_{q\to\infty} e^{(q,t)}_\lambda(X) = \frac{[n]_t!}{\prod_i [\lambda_i]_t!}\, e_n(X)$.
For $\lambda = (2,2)$, $n = 4$:

$$
\lim_{q\to\infty} e_2 \star e_2 = \frac{[4]_t!}{[2]_t![2]_t!}\, e_4 = \frac{[3]_t\,[4]_t}{[2]_t}\, e_4 = [3]_t\,(1+t^2)\, e_4.
$$

Our formula:

- coefficient of $e_4$ as $q \to \infty$: $(1-0)(1+t^2)([3]_t - 0) = (1+t^2)[3]_t$ ✓
- coefficient of $e_{3,1}$: $0$ ✓
- coefficient of $e_{2,2}$: $0$ ✓

**At $t = 0$:**  $[k]_t \to 1$ for all $k \ge 1$, and $t^{a} \to 0$ for $a \ge 1$.
So coefficient of $e_4$ becomes $(q-1)/q \cdot 1 \cdot (q \cdot 1 - 0)/q = (q-1)/q$.
Cross-check via direct SymPy at $t=0$: matches.

**Numeric sober re-check at $m=4$, three arbitrary $(q, t)$ points:**
$(q, t) \in \{(5, 3), (2, 7), (7, -1)\}$. For each, compute
$e_2(Y)\bullet e_2(X)/t$ directly with $q, t$ substituted upfront (Fraction
arithmetic; no symbolic $q, t$ blowup), and compare against the formula
evaluated at the same point. **Difference is 0 in all three cases.**
Script: `proofs/scripts/day191/sober_recheck.py`.

## Conjectural Pieri rule $e_2 \star e_r$, $r \ge 1$

Direct SymPy computation gives:

- $e_2 \star e_2$: as above.
- $e_2 \star e_3 = q^{-2} e_{3,2} + q^{-1}(1-q^{-1})[3]_t\, e_{4,1} + (1-q^{-1})\,[5]_t\bigl((1+t^2) - t/q\bigr) e_5$.

Both fit the following pattern.

**Conjecture (Rick, Day 191).** For $r \ge 1$,

$$
\boxed{\;
e_2 \star e_r \;=\; \frac{1}{q^2}\,e_2 e_r
\;+\; \frac{1-q^{-1}}{q}\,[r]_t\,e_1 e_{r+1}
\;+\; (1-q^{-1})\, \frac{[r+2]_t}{[2]_t}\!\left([r+1]_t - \frac{t\,[r-1]_t}{q}\right)\! e_{r+2}
\;}
$$

with the convention $[0]_t := 0$, $[-1]_t := 0$.

**Consistency with Theorem 3.12.** For $r = 1$: the conjectured formula
becomes

$$
e_2 \star e_1 = q^{-2}\, e_1 e_2 + q^{-1}(1-q^{-1})\, e_1 e_2 + (1-q^{-1})[3]_t\, e_3
             = q^{-1}\, e_1 e_2 + (1-q^{-1})[3]_t\, e_3,
$$

which matches Thm 3.12 with $r = 2$ (via commutativity of $\star$).

**Consistency with Thm C(ii).** As $q \to \infty$ the conjectured
coefficient of $e_{r+2}$ becomes $\frac{[r+2]_t}{[2]_t} \cdot [r+1]_t =
\frac{[r+1]_t [r+2]_t}{[2]_t} = \frac{[r+2]_t!}{[r]_t! [2]_t!}$, matching
Thm C(ii) for $\lambda = (r,2)$.

**Consistency at $q = 1$.** $\gamma_r|_{q=1} = \frac{[r+2]_t}{[2]_t}
([r+1]_t - t[r-1]_t) = \frac{[r+2]_t}{[2]_t}(1 + t^r)$ (by the identity
$[r+1]_t - t[r-1]_t = 1 + t^r$; check directly via $[k]_t = (1-t^k)/(1-t)$).
Then $(1 - q^{-1})\gamma_r|_{q=1} = 0$ and $q^{-1}(1-q^{-1})[r]_t|_{q=1} =
0$; only the $q^{-2}\to 1$ term of $e_2 e_r$ survives. So $e_2 \star
e_r|_{q=1} = e_2 e_r$ ✓.

**Status of conjecture.** `computed` for $r = 1, 2, 3, 4$.

**Verification at $r = 4$ (nailed 2026-09-11):**  Direct SymPy at $m = 6$
gives

- coefficient of $e_{4,2}$: $q^{-2}$ ✓
- coefficient of $e_{5,1}$: $(q-1)(t+1)(t^2+1)/q^2 = (q-1)[4]_t/q^2 = q^{-1}(1-q^{-1})[4]_t$ ✓
- coefficient of $e_6$: $(q-1)(t^2-t+1)(t^2+t+1)(q[5]_t - [3]_t\,t)/q^2 = (1-q^{-1})(1+t^2+t^4)([5]_t - [3]_t\,t/q)$ ✓
  (using $(1-t+t^2)(1+t+t^2) = 1+t^2+t^4 = [6]_t/[2]_t$)

- coefficients of all other partitions of 6 ($e_{4,1,1}, e_{3,3}, e_{3,2,1},
  e_{3,1,1,1}, e_{2,2,2}, e_{2,2,1,1}, e_{2,1,1,1,1}, e_{1^6}$): all zero ✓

Script: `compute_e2_e4.py`. Output in `e2_e4_output.txt`.

## Gaps / next steps

1. **Analytic proof of $e_2 \star e_r$ Pieri.** The identity
   $e_2(Y) = \tfrac{1}{2}(e_1(Y)^2 - p_2(Y))$ reduces the problem to
   computing $p_2(Y) \bullet e_r$ (since $e_1(Y)^2 \bullet e_r$ follows
   from Thm 3.12 up to the auxiliary quantity $e_1(Y) \bullet (e_1 e_r)$).
   Every attempt to determine $e_1(Y) \bullet (e_1 e_r)$ by iterating
   Thm 3.12 and using associativity/commutativity of $\star$ yields a
   **tautology** $0 = 0$; the AHA relations plus Thm 3.12 alone are not
   enough. A direct extension of Hikita's Lemma 3.11 to $e_2(Y)$ (or
   equivalently to $p_2(Y)$) would close the gap. This is the natural
   next analytic target.

2. **General $e_a \star e_b$ Pieri, $a, b \ge 2$.** Extrapolating the
   $e_2 \star e_r$ pattern to $e_a \star e_r$ is not obvious. By analogy,
   the answer should have $\min(a, b) + 1$ terms (one for each "shift
   pattern" moving $k$ boxes from one factor to the other, $k = 0, 1,
   \ldots, \min(a,b)$).

## Registry updates

- `hikita-star-e2-e2.json`: root stays `in-progress`; child
  `e2-star-e2-closed-form` moves `hunch` → `computed` (stability
  verified at $m=4,5$, all sanity checks pass); child
  `general-ea-star-eb-pieri` splits into `e2-star-er-pieri-conjecture`
  (moves to `computed` for $r \in \{1,2,3,4\}$) and
  `ea-star-eb-pieri-conjecture` (remains `hunch`).

## External sources

- Hikita, T. *"$(q,t)$-chromatic symmetric functions"* arXiv:2503.23597.
  Deep-read: Definition 3.4 (⋆-product), Lemma 3.1--3.5 ($\mathfrak q$
  isomorphism, symmetric-lift, centrality), Lemma 3.11 (recursive action
  of the level-one symmetrizer), Theorem 3.12 (Pieri $e_1 \star e_r$),
  Theorem C(ii) (large-$q$ limit).
