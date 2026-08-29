# Day 124 — T-shift pattern extends to k = 4, 5

**Date:** 2026-08-22
**Author:** Compute agent (for Rick)
**Status:** Prediction VERIFIED for all tested cases.

## The prediction (Day 123)

Recall $T: \mathbb{Q}[x_1, \ldots, x_n] \to \mathbb{Q}[x_1, \ldots, x_n]$ defined on
monomials by
$$T(x_1^{a_1} \cdots x_n^{a_n}) = [x_1]_{a_1} \cdots [x_n]_{a_n},$$
where $[x]_m = x(x-1)\cdots(x-m+1)$ is the falling factorial.  Restricted to
symmetric polynomials (equivalently, viewed in the $e$-basis via re-symmetrization),
Rick observed on Day 123:
$$T(e_1^a \cdot e_k) = [e_1 - k]_a \cdot e_k \qquad \text{for } k = 2, 3.$$

**Prediction to test:** the same holds for $k = 4$ and $k = 5$.

## Method

Script: `/home/agent/projects/beta-prime/code/day124/t_shift_verify.py`
Log:    `/home/agent/projects/beta-prime/code/day124/t_shift_verify.txt`

For each $(k, n, a)$:
1. Form $f = e_1(x_1,\ldots,x_n)^a \cdot e_k(x_1,\ldots,x_n)$ as a polynomial
   in the $x_i$.
2. Apply $T$ monomial-by-monomial.
3. Symmetrize the result back into the $e$-basis using SymPy's `symmetrize`.
4. Compare to $[e_1 - k]_a \cdot e_k$.

## Results

| k | n | a range | outcome |
|---|---|---------|---------|
| 2 | 2 | 0..4 | all MATCH |
| 2 | 3 | 0..4 | all MATCH |
| 3 | 3 | 0..4 | all MATCH |
| 3 | 4 | 0..4 | all MATCH |
| **4** | **4** | **0..4** | **all MATCH** |
| **4** | **5** | **0..4** | **all MATCH** |
| **5** | **5** | **0..4** | **all MATCH** |
| **5** | **6** | **0..4** | **all MATCH** |

**40 / 40** $(k, n, a)$ triples match.  No discrepancies, no correction terms
required.

Sample outputs (matches exactly to the predicted $[e_1 - k]_a \cdot e_k$):

- $T(e_1^3 e_4) = e_1^3 e_4 - 15 e_1^2 e_4 + 74 e_1 e_4 - 120 e_4
    = [e_1 - 4]_3 \cdot e_4$.
- $T(e_1^4 e_5) = e_1^4 e_5 - 26 e_1^3 e_5 + 251 e_1^2 e_5 - 1066 e_1 e_5 + 1680 e_5
    = [e_1 - 5]_4 \cdot e_5$.

## Structural observations

1. **Independence from $n$.**  The $e$-basis expansion of $T(e_1^a e_k)$ is
   *identical* in $n = k$ and $n = k+1$ variables (compare, e.g., the $k=4$
   entries at $n=4$ vs. $n=5$: byte-for-byte identical polynomials in
   $e_1, e_k$).  This is exactly what one expects if the identity truly lives
   in the stable ring $\Lambda$ of symmetric functions and only refers to
   $e_1$ and $e_k$ — it does not depend on how many other $e_j$'s are
   available.

2. **Falling-factorial shift is exactly $-k$.**  The coefficients form the
   *signed Stirling numbers of the first kind* (weighted): expanding
   $[e_1 - k]_a$ in $e_1$, we get $\sum_j s(a, j) (-k)^{a-j} e_1^j$ (up to
   sign convention).  E.g., $k = 5$, $a = 4$:
   $[e_1 - 5]_4 = e_1^4 - 26 e_1^3 + 251 e_1^2 - 1066 e_1 + 1680$.
   The pure-scalar term $1680 = 5 \cdot 6 \cdot 7 \cdot 8 = [-5]_4 \cdot (-1)^4 = 5!/1! \cdot \binom{...}{}$
   which factors as $\frac{8!}{4!}$ — the fourth falling factorial of $8$.
   No surprises; the arithmetic is the "double-Pochhammer" pattern
   suggested by queer content.

3. **Only $e_1$ and $e_k$ appear.**  In every tested case, $T(e_1^a e_k)$
   involves only $e_1$ and $e_k$ (no $e_j$ for $1 < j \neq k$).  This is a
   nontrivial cancellation given that expanding
   $x^{a_1} \cdots x^{a_n}$ and multiplying by falling factorials naively
   creates many cross-terms.

4. **Queer content shift, doubled.**  Rick's Day 123 speculation: the shift
   sequence $(0, -2, -3, -4, -5, \ldots)$ — where $-k$ is the shift for
   $e_k$ — is exactly (twice) the *queer content shift* for the queer
   superalgebra $U(\mathfrak{q}_N)$'s Harish-Chandra isomorphism.  The
   present verification extends the pattern by two more values (matching
   $k = 4, 5$), consistent with this identification.  This is not proof,
   but the coincidence hardens.

## Interpretation

- **The pattern extends.**  There is no reason to doubt the identity
  $T(e_1^a \cdot e_k) = [e_1 - k]_a \cdot e_k$ for all $k \geq 2$ and all
  $a \geq 0$.  A proof should be sought — the fact that $e_j$'s with
  $j \neq 1, k$ don't appear suggests a slick combinatorial or generating-
  function argument.

- **Impact on $\Psi$.**  This constrains $T$ (and by extension the
  associated map that produces $\Psi$ on Weyl-determinant-scaled Schurs)
  quite tightly.  Combined with Day 123's algebraic setup, the ansatz
  "$\Psi$ is a Harish-Chandra map for $U(\mathfrak{q}_N)$" is now
  substantially more plausible.

## Suggested next steps

1. **Prove the identity** $T(e_1^a e_k) = [e_1 - k]_a e_k$ for all $k \geq 2$.
   Candidate approach: view $T$ via the umbral operator
   $x_i \to x_i \partial_i$ acting on $e^{x_i \cdot \log(\cdot)}$; or use the
   generating function
   $\sum_a \frac{e_1^a}{a!} e_k = e_k \exp(e_1)$ and its image.

2. **Test mixed products** $T(e_1^a e_j e_k)$ for $j, k \geq 2$.
   The Day 123 note says these are more complex — this needs empirical mapping
   before making any $U(\mathfrak{q}_N)$-style guess.

3. **Test in the shifted-power basis.**  If $T$ corresponds to the
   change-of-variables from power basis to falling-factorial basis, then
   $T$ should be diagonal (or nearly so) on shifted power sums or
   Frobenius characteristics of queer supersymmetric functions.  Check.

## Files

- Script:  `/home/agent/projects/beta-prime/code/day124/t_shift_verify.py`
- Log:     `/home/agent/projects/beta-prime/code/day124/t_shift_verify.txt`
- Notes:   `/home/agent/projects/beta-prime/notes/2026-08-22-day124-t-shift-extended.md` (this file)
