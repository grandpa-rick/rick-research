# OQ-INVERTI-STRATUM — RESULT

**Day 65, 2026-06-12. Task A.**

## Question

Per Robin's Day-64 reply: Andrews et al. (arXiv:2505.06941) characterize
sequences $(a_n)_{n\ge 0}$ with $a_0 = 1$ that arise as the graded
dimension sequence of some free noncommutative cocommutative connected
Hopf algebra (equivalently: $U(L)$ for some free / Lie-like graded
$L$) — they must satisfy **INVERTi**-nonneg: the sequence $(b_n)$
defined by
$$1 + \sum_{n\ge 1} a_n t^n \;=\; \frac{1}{1 - \sum_{n\ge 1} b_n t^n}$$
must satisfy $b_n \ge 0$ for all $n \ge 1$. When it holds, $b_n$ equals
the count of *primitives* in degree $n$.

We test the Day-62 MODE stratum vector and the Day-63 MAX stratum
vector.

## Computation

Convention: input vector is $a_1, a_2, \ldots, a_8$, with $a_0 = 1$.

Recurrence: $b_n \;=\; a_n - \sum_{k=1}^{n-1} b_k\, a_{n-k}$.

| n         | 1 | 2  | 3  | 4    | 5    | 6    | 7    | 8     |
|-----------|---|----|----|------|------|------|------|-------|
| $a^{MODE}$| 1 | 5  | 9  | 9    | 13   | 17   | 22   | 26    |
| $b^{MODE}$| 1 | 4  | 0  | **-20** | -12 | 80  | 113 | -289  |
| $a^{MAX}$ | 3 | 8  | 11 | 10   | 19   | 14   | 23   | 26    |
| $b^{MAX}$ | 3 | **-1** | -10 | 15 | 35  | -148 | 99  | 513   |

Forward-INVERT sanity check on both $b$-sequences reproduces the input
$a$-sequence exactly. Computation correct.

## Verdict — both fail

- **MODE** fails at $n=4$: $b_4 = -20$.
- **MAX**  fails at $n=2$: $b_2 = -1$.

Therefore:

> Neither the MODE stratum vector nor the MAX stratum vector arises as
> the graded-dimension sequence of a free noncommutative cocommutative
> connected Hopf algebra.

The obstruction lands **earlier and harder for MAX** ($n=2$, single
negative dimension) than for MODE ($n=4$, after passing the $n=1,2,3$
checks). MODE at least admits the interpretation "1 primitive at
degree 1, 4 at degree 2, 0 at degree 3" before breaking at degree 4.

## What this rules out

We had been entertaining the idea that the stratum dimensions might
factor through "free cocommutative connected Hopf" land — i.e. that
the stratum is the graded $U(L)$ for some free-ish graded Lie algebra
$L$, with the strata dims being primitive counts plus their PBW
descendants. **This is now ruled out** for both MODE and MAX.

That doesn't kill the broader Hopf-algebra picture: the stratum can
still come from a cocommutative connected Hopf algebra that is **not**
of the free form (e.g. has nontrivial relations among primitives, or
quotient of $U(\text{free})$), and the Andrews et al. INVERTi-nonneg
criterion specifically is for *free*. But it does eliminate the
cleanest candidate, and the failure-locations (n=4 for MODE, n=2 for
MAX) point to where structural relations must enter if Hopf is the
right framework at all.

## Alternate convention check

If MODE's leading 1 is interpreted as $a_0 = 1$ (so the input vector
is $a(0),\ldots,a(7)$ instead of $a(1),\ldots,a(8)$), then
$a_1,\ldots,a_7 = 5,9,9,13,17,22,26$ and
$b = 5, -16, 44, -108, 240, -479, 823$ — still fails (at $n=2$),
even worse. The MAX vector cannot use this convention since $a(0) = 3$
would mean non-connected. The original convention is the right one
and MODE still fails.

## Files

- `inverti.py` — computation
- `inverti_results.json` — JSON of $a, b$ pairs and verdicts
