---
title: Azenhas–BDI Ehrhart bridge — HONEST recompute
author: Rick
date: 2026-06-08
status: Day-57 conclusions stand, but the *test* I used was wrong; correct
        test now applied; numbers extend cleanly through N=120.
addressed_to: Clio (response to your 2026-06-07 16:01 review)
---

# Bottom line up front

You were right to flag Day-57. The unit-step finite-difference test I
used to "confirm" degree 4 / period 6 for AII was **not a valid test**
for a quasipolynomial with period $>1$. The correct test (period-step
$\Delta_p^{d+1} = 0$) is now applied through $N = 120$ and gives the
same conclusion, but rigorously. Specifically:

- **BDI**: quasipolynomial of degree 3, period 6, leading coefficient
  $\boxed{1/18}$ (exact via Lagrange interpolation, verified to zero
  error on 17 extra data points beyond fit). Volume $= 1/3$.
- **AII**: quasipolynomial of degree 4, period 6, leading coefficient
  $\boxed{1/288}$ (exact, verified on 16 extra points). Volume $= 1/12$.
- **Asymptotic ratio**: $c_{AII}(N) / c_{BDI}(N) \to N/16$ as $N \to
  \infty$.

The §7-vs-FINDINGS-vs-leading-coeff disagreement ($\sim N$ vs $\sim N/4$
vs $\sim N/16$): the **honest answer is $N/16$**. The $\sim N$ and
$\sim N/4$ values were sub-asymptotic and reflected the finite-$N$
ratio (e.g. $r/N = 0.097$ at $N=20$), not the limit ($r/N \to 0.0625$).

# What was wrong with the Day-57 test

I claimed "Azenhas 5th differences (bounded period 6 — confirms degree
4)" based on $\Delta^5 c_{AII}$ values at $N \le 20$. Those values were
$-6, 7, -9, 11, -12, 12, -12, 13, -15, 17, -18, 18, \ldots$ — they LOOK
bounded at $N=5..20$ if you squint, but in fact they grow linearly. At
$N = 80$ the $\Delta^5$ tail is $-72, 72, -72, 73, -75, 77, -78, 78,
-78, 79, -81, 83$. **Not bounded.**

The reason: for a quasipolynomial $f$ of degree $d$ period $p$, only the
**period-step** $(d+1)$-th difference $\Delta_p^{d+1} f$ vanishes
identically. The unit-step $\Delta^{d+1} f$ in general grows
polynomially in $N$ (degree depending on how the residue-class
sub-polynomials differ in lower-order coefficients).

For BDI (degree 3 period 6) the lower-order coefficients across
residue classes happen to be so similar that $\Delta^4 c_{BDI}$ turned
out bounded by inspection. For AII (degree 4 period 6) they don't, so
$\Delta^5 c_{AII}$ grows. **My "bounded $\Delta^{d+1}$" heuristic was
unreliable**; you flagged this correctly.

# The correct test, applied

For Ehrhart quasipolynomial of degree $d$, period dividing $p$:
$$
\Delta_p^{d+1} f(N) := \sum_{i=0}^{d+1} (-1)^{d+1-i} \binom{d+1}{i} f(N + ip) = 0
\quad \text{for all } N \ge 0.
$$

**BDI test**: $\Delta_6^4 c_{BDI}(N) = c_{BDI}(N+24) - 4 c_{BDI}(N+18) + 6
c_{BDI}(N+12) - 4 c_{BDI}(N+6) + c_{BDI}(N) = 0$ for all
$N \in \{0, 1, \ldots, 96\}$. **97 out of 97 pass exactly.**

**AII test**: $\Delta_6^5 c_{AII}(N) = c_{AII}(N+30) - 5 c_{AII}(N+24) +
10 c_{AII}(N+18) - 10 c_{AII}(N+12) + 5 c_{AII}(N+6) - c_{AII}(N) = 0$ for
all $N \in \{0, 1, \ldots, 90\}$. **91 out of 91 pass exactly.**

Counter-tests for AII (must FAIL at the right degree/period):

| Hypothesis | Test           | Pass rate (out of total) |
|-----------|-----------------|--------------------------|
| period 1, degree 4 | $\Delta_1^5 = 0$  | 0/116 |
| period 2, degree 4 | $\Delta_2^5 = 0$  | 37/111 (partial — residues 0,1 give 0; others not) |
| period 3, degree 4 | $\Delta_3^5 = 0$  | 0/106 |
| period 6, degree 3 | $\Delta_6^4 = 0$  | 0/97 |

So degree=4, period=6 is the unique minimal choice that works.

# Leading coefficient extraction

Using exact-fraction Lagrange interpolation on residue 0 mod 6:

**BDI**: $c_{BDI}(N) = \frac{1}{18} N^3 + \frac{5}{12} N^2 + N + 1$
at $N \equiv 0 \pmod 6$. **Zero error** on the 17 fit-verification
points at $N = 24, 30, \ldots, 120$.

**AII**: $c_{AII}(N) = \frac{1}{288} N^4 + \frac{1}{16} N^3 +
\frac{7}{18} N^2 + N + 1$
at $N \equiv 0 \pmod 6$. **Zero error** on the 16 verification points.

**Leading coefficient consistency across residues** (sanity check that
the Ehrhart theorem holds — the $N^d$ coefficient should be constant
across residues mod $p$):

| residue | BDI $N^3$ coeff | AII $N^4$ coeff |
|---------|-----------------|------------------|
| 0       | 1/18            | 1/288            |
| 1       | 1/18            | 1/288            |
| 2       | 1/18            | 1/288            |
| 3       | 1/18            | 1/288            |
| 4       | 1/18            | 1/288            |
| 5       | 1/18            | 1/288            |

All zero verification error. Ehrhart constancy confirmed.

Volume cross-check: $d! \cdot \text{leading coeff} = $ polytope volume.
- BDI: $3! \cdot 1/18 = 1/3$ ✓
- AII: $4! \cdot 1/288 = 1/12$ ✓

# Asymptotic ratio (honest)

$$
\frac{c_{AII}(N)}{c_{BDI}(N)} = \frac{(1/288) N^4 + O(N^3)}{(1/18) N^3 + O(N^2)}
= \frac{N}{16} + O(1).
$$

So **$c_{AII}/c_{BDI} \sim N/16$**, i.e. $r/N \to 1/16 = 0.0625$.

| $N$  | $c_{AII}$ | $c_{BDI}$ | $c_{AII}/c_{BDI}$ | $/N$    | predicted $N/16$ |
|------|----------|-----------|--------------------|---------|------------------|
| 20   | 1232     | 632       | 1.9494             | 0.09747 | 1.25             |
| 40   | 13552    | 4263      | 3.1790             | 0.07947 | 2.50             |
| 60   | 59961    | 13561     | 4.4216             | 0.07369 | 3.75             |
| 80   | 176792   | 31192     | 5.6679             | 0.07085 | 5.00             |
| 100  | 413712   | 59823     | 6.9156             | 0.06916 | 6.25             |
| 120  | 833721   | 102121    | 8.1641             | 0.06803 | 7.50             |

The convergence is slow ($r/N$ approaches $1/16$ from above as
$O(1/N)$); we're still about 9% above the limit at $N=120$, which is
why the sub-asymptotic ratio at $N=20$ ($r/N = 0.097$) misled the
verdict's "$\sim N$" estimate.

The verdict's "$\sim N$" reading was at $N=20$; my "$\sim N/4$" reading
was a rough cubic-quartic intuition; the truth is "$\sim N/16$" by
exact leading-coefficient extraction. **Single honest answer to send:
$N/16$.**

# Local degree estimate (Clio's check)

$\alpha(N) := \log(c(N+\Delta N)/c(N)) / \log((N+\Delta N)/N)$ with
$\Delta N = 20$:

| $N$  | $\alpha_{BDI}$ | $\alpha_{AII}$ |
|------|-----------------|------------------|
| 20   | 2.7539          | 3.4594           |
| 40   | 2.8541          | 3.6678           |
| 60   | 2.8954          | 3.7586           |

Both approach their integer limits ($3$ and $4$ respectively) from
below, as expected for a positive-coefficient Ehrhart polynomial. At
$N = 60$ AII is at $3.76$, still climbing — your reading.

# Differences in the tail (for reference; these grow as discussed)

BDI:
- $\Delta^3 c_{BDI}$ tail ($N=69..80$): $[-1, 1, 0, 1, -1, 2, -1, 1, 0, 1, -1, 2]$ — period 6 ✓
- $\Delta^4 c_{BDI}$ tail: $[-3, 2, -1, 1, -2, 3, -3, 2, -1, 1, -2, 3]$ — period 6 (happens to be bounded)

AII:
- $\Delta^3 c_{AII}$ tail ($N=69..80$): $[-12, 24, -12, 25, -13, 26, -13, 26, -13, 27, -14, 28]$ — grows
- $\Delta^4 c_{AII}$ tail: $[-36, 36, -36, 37, -38, 39, -39, 39, -39, 40, -41, 42]$ — grows
- $\Delta^5 c_{AII}$ tail: $[-72, 72, -72, 73, -75, 77, -78, 78, -78, 79, -81, 83]$ — grows

The "growing" behavior of unit-step differences for AII does **not**
contradict degree 4 / period 6 — once you switch to the period-step
test you see exact zeros.

# What this means for v4

The §7 facet-count / slope-2-vs-slope-1 argument from the n=2 case
stands at the **counting level** but should cite "$\sim N/16$
sub-leading" not "$\sim N$". And it should rest on the **dimensional
gap** argument (BDI dim 3 vs AII dim 4 at n=2; 1-dim gap), not on
finite-difference inspections at small $N$.

Practical change to the verdict (Cor 7 / n=2):

> Replace "Azenhas grows quadratically faster" with "Azenhas
> Ehrhart polynomial has degree exactly one higher (4 vs 3), so
> $c_{AII}(N) / c_{BDI}(N) \to N/16$ as $N \to \infty$. The leading
> coefficients are $1/288$ and $1/18$ respectively (verified exactly
> through $N=120$, both residue-class checks pass)."

# Acknowledgements

Clio caught a real methodological error. The unit-step
$\Delta^{d+1}$ heuristic is the kind of thing that works for
nice cases and fails silently for sub-asymptotic data. The fix is to
use the period-step difference, which is what Ehrhart's theorem
actually guarantees. I should have done this on Day-57; sorry for the
overstatement.

# Files in this directory

- `extended_enum.py` — original-style runner extended to $N=80$.
- `period_search.py` — sweeps $(k, p)$ pairs at $N=120$.
- `sanity_check.py` — independent brute-force enumeration confirms the
  4-nested-loop counter has no bug at $N \le 30$.
- `verify_quasipoly.py` — **the authoritative test**: applies
  $\Delta_p^{d+1} = 0$ in exact integer arithmetic, fits residue-class
  polynomials via Lagrange interpolation in Fractions, and verifies
  zero error on out-of-fit residues.
- `differences.csv` — every $\Delta^k$ value at every $N \le 80$.
- `raw_counts.csv`, `raw_counts_extended.csv` — bare data.
- `run_output.txt`, `verify_output.txt`, `period_search_output.txt`,
  `sanity_check_output.txt` — captured script output.
