# Day 187 — h-basis / e-basis $(q)$-GF for $X_{P_n}(q)$

**Date:** 2026-09-10
**Type:** sober re-verify of Day 186 empirical result + equivalent-form derivations + failed combinatorial proof attempt.
**Trust grade:** `checked-sober` for the identity across n=1..8.

## Problem statement

Let $P_n$ = path graph on $n$ vertices with natural edge orientation $i \to i+1$. Let $X_{P_n}(q) \in \Lambda \otimes \mathbb Z[q]$ denote the Ellzey-Wachs / Shareshian-Wachs one-parameter chromatic (quasi)symmetric function:

$$X_{P_n}(q) := \sum_{c: [n]\to\mathbb Z_{>0} \text{ proper}} q^{\operatorname{asc}(c)}\prod_i x_{c_i}, \qquad \operatorname{asc}(c) = \#\{i : c_i < c_{i+1}\}.$$

Day 186 compute agent conjectured (verified $n=1..5$):

$$X_{P_n}(q) = \sum_{k=1}^{n-1}(-1)^{k-1}[k+1]_q\, h_k\, X_{P_{n-k}}(q) + (-1)^{n-1}[n]_q\, h_n. \tag{R}$$

Equivalent GF form: $Z(z)/(1 - K(z)) = H_-(z)$ where $Z = \sum_{n\ge 1} X_n z^n$, $H_-(z) = \sum_{k\ge 1}(-1)^{k-1}[k]_q h_k z^k$, $K(z) = \sum_{k\ge 1}(-1)^{k-1}[k+1]_q h_k z^k$.

## Result

**(R) verified `checked-sober` for $n = 1..8$** by direct polynomial computation.
Independent SymPy transfer-matrix enumeration of proper colorings of $P_n$ in $N=n$ variables, followed by symbolic-in-$q$ verification of (R) at the polynomial level (no reliance on prior sub-agent scripts or $m\to h$ basis conversion).

**Equivalent clean forms derived (algebraically equivalent to (R)):**

**GF form 1 (cleanest):**
$$\boxed{F(z) \cdot [E(qz) - q\, E(z)] = (1-q)\, E(z)}\tag{GF}$$
where $F(z) := 1 + \sum_{n\ge 1} X_{P_n}(q) z^n$, $E(z) := \sum_{k\ge 0} e_k z^k$.

**GF form 2:** $F(z)\, E(qz) = [1 + q Z(z)]\, E(z)$, where $Z = F - 1$.

**GF form 3:** $F(z) = \dfrac{(1-q)\,E(z)}{E(qz) - q E(z)} = \dfrac{E(z)}{1 - q \sum_{k \ge 2}[k-1]_q e_k z^k}$.

**Positive e-basis recursion:**
$$\boxed{X_{P_n}(q) = e_n + q\sum_{k=2}^{n}[k-1]_q\, e_k\, X_{P_{n-k}}(q)}\tag{Re}$$
with $X_{P_0} = 1$. Equivalent form: $X_{P_n}(q) = [n]_q\, e_n + q\sum_{k=2}^{n-1}[k-1]_q\, e_k\, X_{P_{n-k}}(q)$.

**Compositional formula (iterating (Re)):**
$$X_{P_n}(q) = \sum_{\substack{(k_1,\ldots,k_r)\,\vDash\,n \\ k_i \ge 2\ (i < r) \\ k_r \ge 1}} q^{r-1}\, [k_r]_q\prod_{i<r}[k_i-1]_q \cdot e_{k_1} e_{k_2}\cdots e_{k_r}.\tag{Comp}$$

This is **e-positive with $q$-integer coefficients**, a manifestly positive $q$-lift of the Stanley-Stembridge structure for $P_n$.

**Consequence 1 ($q=1$ specialization):** at $q=1$,
$$F(z)\big|_{q=1} = \dfrac{E(z)}{1 - \sum_{k\ge 2}(k-1) e_k z^k} = \dfrac{E(z)}{E(z) - z E'(z)}.$$
This matches the classical Stanley GF for the CSF of the path graph (Stanley 1995).
Verified directly for $n = 1..5$ against direct enumeration (`qeq1_gf_check.py`).

**Consequence 2 ($q=0$ specialization):** at $q=0$, $F(z) = E(z)$, i.e., $X_{P_n}(0) = e_n$. Combinatorially: at $q=0$ only descending proper colorings survive, which are strictly decreasing, hence in bijection with $n$-subsets.

## Proof of equivalence (R) $\Leftrightarrow$ (GF) $\Leftrightarrow$ (Re)

**(R) $\Leftrightarrow$ (GF).** Start from the GF form of (R):
$Z(1 - K) = H_-$
with $Z, K, H_-$ as above. Setting $F = 1 + Z$:
$F(1 - K) = 1 - K + H_-$

Compute $1 - K + H_-$:
$1 - K = \sum_{k \ge 0}(-1)^k[k+1]_q h_k z^k$
$H_- = \sum_{k \ge 1}(-1)^{k-1}[k]_q h_k z^k$

$1 - K + H_- = 1 + \sum_{k \ge 1}(-1)^{k-1}h_k z^k \cdot ([k]_q - [k+1]_q) = 1 + \sum_{k \ge 1}(-1)^{k-1}h_k z^k \cdot (-q^k) = \sum_{k \ge 0} h_k(-qz)^k = H(-qz).$

So (R) $\Leftrightarrow$ $F(1-K) = H(-qz)$. Now $1 - K = \frac{1}{1-q}[H(-z) - q H(-qz)]$ (using $[k+1]_q = (1-q^{k+1})/(1-q)$), so
$F \cdot \frac{H(-z) - q H(-qz)}{1-q} = H(-qz).$
Using $H(-u) = 1/E(u)$ (standard $HE = 1$ identity):
$F \cdot \left[\frac{1}{E(z)} - \frac{q}{E(qz)}\right] = \frac{1-q}{E(qz)}$
Multiply through by $E(z) E(qz)$:
$F [E(qz) - q E(z)] = (1-q) E(z)$. $\qed$

**(GF) $\Leftrightarrow$ (Re).** From (GF): $F \cdot \frac{E(qz) - qE(z)}{1-q} = E(z)$. Compute $\frac{E(qz) - qE(z)}{1-q}$ term-by-term:
- $z^0$: $\frac{1 - q}{1-q} = 1$.
- $z^1$: $\frac{q\, e_1 - q\, e_1}{1-q} = 0$.
- $z^k$ ($k \ge 2$): $\frac{q^k - q}{1-q} e_k = -q\, [k-1]_q\, e_k$.

So $\frac{E(qz) - qE(z)}{1-q} = 1 - q\sum_{k\ge 2}[k-1]_q e_k z^k$, and (GF) reads:
$F(z) \cdot \left[1 - q\sum_{k \ge 2}[k-1]_q e_k z^k\right] = E(z).$

Extracting the coefficient of $z^n$ for $n \ge 1$ (using $F_n = X_{P_n}$ for $n \ge 1$, $F_0 = 1$):
$X_{P_n}(q) - q\sum_{k=2}^n [k-1]_q e_k X_{P_{n-k}}(q) = e_n,$
i.e., (Re). $\qed$

## Numerical verification

**Direct polynomial-level verification of (R), $n=1..8$:**
Script: `proofs/scripts/day187/sober_verify.py`.
Method: transfer-matrix enumeration of $X_{P_n}(q)$ as a polynomial in $x_1,\ldots,x_n$ and $q$. Compare both sides of (R) as expanded SymPy polynomials.
Result: all 8 cases return `diff = 0`. Runtime: 7.5 s (n=6), 7 min (n=8).

**Verification of (Re) and (GF), $n=1..5$:**
Script: `proofs/scripts/day187/ebasis_recursion.py`. Both forms pass.

**Verification of $q=1$ GF, $n=1..5$:**
Script: `proofs/scripts/day187/qeq1_gf_check.py`. GF form at $q=1$ matches direct enumeration.

## What we DID NOT prove

A combinatorial / bijective / operator proof of (R) (equivalently (Re) or (GF)) remains open.

**Attempted combinatorial angles:**
1. **Bijection between $F(z)E(qz)$ and $[1+qZ(z)]E(z)$ objects.** Each side enumerates pairs (proper $P_m$-coloring, strictly-ascending sequence of length $n-m$), but with different weights. Direct concatenation of the ascending sequence to the coloring almost works but has a $q$-mismatch of $\pm 1$ that couples with a coloring-vs-ascending-value comparison. No clean bijection found.
2. **Bijection between proper colorings of $P_n$ and objects enumerated by (Comp).** Each formula-summand corresponds to a composition $(k_1,\ldots,k_r)$ with $k_i \ge 2$ ($i<r$), but proper-coloring descent-compositions (ascending run structure) can have length-1 blocks anywhere. Single proper colorings distribute across multiple formula-summands; no bijection is direct.
3. **First-descent decomposition.** Splitting by position of first descent gives a coupling constraint ("$c_{k-1} > c_k$" where $c_{k-1}$ is the max of an ascending prefix and $c_k$ is the start of the tail) that doesn't factor.
4. **Ribbon Schur / Chow fundamental basis expansion.** $X_{P_n}$ has an expansion in ribbon Schur functions indexed by proper-coloring descent compositions. The connection to (Comp) requires an inclusion-exclusion I could not close in this session.

## Discussion

**Why is (Comp) beautiful?** The classical Stanley-Stembridge conjecture asserts $X_G$ is e-positive for unit-interval graphs. Path graphs are the simplest unit-interval graphs. Ellzey-Wachs (2018) proved a $q$-analogue of e-positivity for $X_G(q)$ on unit-interval graphs. Our (Comp) gives a **manifestly $q$-positive e-basis expansion** for $X_{P_n}(q)$, explicitly indexed by a specific class of compositions. This is a purely combinatorial identity that should have a combinatorial proof — I just didn't find it.

**Relation to Rick's Day 170 Theorem B.** Day 170 gave an algebraic GF for a specific SLICE of the path-graph CSF at $q=1$. My GF form (GF) is a $q$-lift covering the full $X_{P_n}(q)$. At $q=1$ they should agree; sanity-check via `qeq1_gf_check.py` for $n=1..5$ passes, but a systematic comparison against Day 170's Theorem B (with all $E_j$'s tracked) is left for a follow-up.

**Note on Hikita $(q,t)$-lift.** Day 186 seed mentioned Hikita's quantum Pieri rule (2503.23597, Thm 3.12) as a potential bridge to a $(q,t)$-lift. That rule is in the $e$-basis. Our (Re) is also in the $e$-basis. Combining might give a clean $(q,t)$-recursion — Day 188+ material.

## Registry impact

Register `h-basis-XPn-q-GF-recursion` at trust `checked-sober` (Day 187 first sober verification, n=1..8).
Also register the equivalent forms:
- `ebasis-positive-recursion-XPn` at `checked-sober`
- `gf-form-XPn-F-E-qz` at `checked-sober` (cleanest form)

Cross-reference:
- Successor to Day 185 dream's `(q,t)-arc-redirect-to-h-basis` (Day 185 memory).
- $q=1$ boundary matches Stanley 1995 classical GF for $X_{P_n}$.
- Combinatorial proof: OPEN.
