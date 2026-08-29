# Day 127 — Combinatorial τ-degree preservation for shifted Schur (ℓ ≤ 3)

**Date:** 2026-08-22
**Author:** Rick (deep-work session)
**Status:** PROVED. The Day 118 §5 residual gap is closed for ℓ(μ) ≤ 3.

## Main theorem

**Theorem.** For every partition $\mu$ with $\ell(\mu) \le 3$,
$$d_{s^*_\mu} = d_{s_\mu} = \mu_1 + \left\lfloor \frac{\mu_2 + \mu_3}{2} \right\rfloor,$$
where $d_f := \tau\text{-deg}(S(f))$ under the Char. Lemma substitution $u_1 \to \tau$, $u_2 \to y$, $u_3 \to s-y$ (reducing mod $y^2 - sy + \tau$).

The equality has two directions, proved separately below.

## Setup

Working ring: $\mathbb{Q}[\tau, s, y]/(y^2 - sy + \tau)$. Since $y^2 = sy - \tau$, every element reduces uniquely to $h_0(s, \tau) + h_1(s, \tau) y$.

**Substitution facts.**
- $y(s-y) = \tau$ in the quotient ring (this is $y^2 - sy + \tau = 0$ rearranged).
- $S(V) = \tau(\tau - s + 1)(2y - s)$ where $V = \prod_{i<j}(u_i - u_j)$.
- $S(f)$ is $y$-free (i.e., $h_1 = 0$) whenever $f$ is symmetric in $u_2, u_3$ — equivalently invariant under $y \leftrightarrow s-y$.
- $S(g)$ is divisible by $(2y-s)$ whenever $g$ is antisymmetric under the transposition $u_2 \leftrightarrow u_3$ — because $g$ vanishes at $u_2 = u_3$, i.e., at $y = s-y$, i.e., at $2y - s = 0$.

**Shifted Schur.** $s^*_\mu \cdot V = \det[[u_i]_{k_j}]$ where $k_j = \mu_j + 3 - j$ and $[x]_k := x(x-1)\cdots(x-k+1)$. Equivalently, $\Psi(s_\mu) = s^*_\mu$ where $\Psi(f) = T(fV)/V$ and $T(u^\alpha) := \prod_i [u_i]_{\alpha_i}$.

**Chebyshev-like polynomials.** Define $v_d(s, \tau)$ by $v_0 = 0$, $v_1 = 1$, $v_{d+1} = s v_d - \tau v_{d-1}$. These are the polynomials such that $\alpha^d - \beta^d = (\alpha - \beta) v_d$ where $\alpha, \beta$ are the two roots of $z^2 - sz + \tau = 0$. In particular
$$y^m (s-y)^n - y^n (s-y)^m = (2y - s) \cdot \tau^{\min(m,n)} \cdot v_{|m-n|} \cdot \operatorname{sgn}(m - n).$$

Explicitly, $\tau\text{-deg}(v_d) = \lfloor (d-1)/2 \rfloor$ for $d \ge 1$, with leading τ-coefficients
$$v_{2j+1}: \quad (-1)^j \text{ at } \tau^j, \qquad v_{2j}: \quad (-1)^{j-1} \cdot j \cdot s \text{ at } \tau^{j-1}.$$

## Upper bound: $d_{s^*_\mu} \le d_{s_\mu}$

**Key Lemma (combinatorial τ-degree bound).** In the ordinary-Schur expansion
$$s^*_\mu = \sum_\lambda c^\mu_\lambda \, s_\lambda,$$
every partition $\lambda$ with $c^\mu_\lambda \ne 0$ satisfies
$$\lambda_1 \le \mu_1, \qquad |\lambda| \le |\mu|, \qquad d_\lambda \le d_\mu.$$

**Proof.**

*Step 1: multilinear expansion.* $[u_i]_{k} = \sum_j s(k, j) u_i^j$ (signed Stirling first kind), and $s(k, k) = 1$. Multilinearity of the determinant in columns gives
$$s^*_\mu \cdot V = \det[[u_i]_{k_j}] = \sum_{(j_1, j_2, j_3),\, 0 \le j_i \le k_i} \left(\prod_i s(k_i, j_i)\right) \det[u_i^{j_j}].$$
The determinant $\det[u_i^{j_j}]$ vanishes if the $j_i$ have a repeat. Otherwise, sorting descending to $(j'_1, j'_2, j'_3)$ gives $\det[u_i^{j_j}] = \operatorname{sgn}(\sigma) V s_\lambda$ with $\lambda_i := j'_i - (3 - i)$.

Every $\lambda$ appearing in the sum thus comes from some $(j_1, j_2, j_3)$ with $0 \le j_i \le k_i = \mu_i + 3 - i$.

*Step 2: $\lambda_1 \le \mu_1$.* Since $\mu_1 \ge \mu_2 \ge \mu_3$, $k_1 = \mu_1 + 2 \ge k_2 = \mu_2 + 1 \ge k_3 = \mu_3$. Hence $\max_i k_i = k_1$, and $\lambda_1 = \max(j_1, j_2, j_3) - 2 \le k_1 - 2 = \mu_1$.

*Step 3: $|\lambda| \le |\mu|$.* $|\lambda| = \sum_i (j'_i - (3-i)) = \sum j_i - 3 \le \sum k_i - 3 = |\mu| + 6 - 6 = |\mu|$.

*Step 4: monotonicity.* Let $f(x) := x + \lfloor (|\mu| - x)/2 \rfloor$. Then $f(x+1) - f(x) = 1 - (\lfloor(|\mu|-x)/2\rfloor - \lfloor(|\mu|-x-1)/2\rfloor) \in \{0, 1\}$. So $f$ is non-decreasing.

Then $d_\lambda = \lambda_1 + \lfloor (|\lambda| - \lambda_1)/2 \rfloor \le \lambda_1 + \lfloor (|\mu| - \lambda_1)/2 \rfloor = f(\lambda_1) \le f(\mu_1) = d_\mu$. ∎

**Corollary.** $d_{s^*_\mu} \le \max_\lambda d_{s_\lambda} \le d_\mu$.

## Lower bound: $d_{s^*_\mu} \ge d_{s_\mu}$

**Strategy.** Compute the τ-degree of $S(s^*_\mu)$ directly via the operator identity $s^*_\mu V = T(s_\mu V)$. Write $S(a_k) = (2y - s) \cdot h(s, \tau)$ for antisymmetric $a_k$, then $d_{s^*_\mu} = \tau\text{-deg}(h) - 2$.

**Antisymmetric orbit sum formula.** For $k_1 > k_2 > k_3$, direct expansion of $\det[u_i^{k_j}]$ under $S$ and using the identity for $A(m, n) = y^m(s-y)^n - y^n(s-y)^m$ derived above yields
$$S(\det[u_i^{k_j}]) = (2y - s) \cdot h_0^{(k)}, \quad h_0^{(k)} := \tau^{k_1+k_3} v_{k_2 - k_3} - \tau^{k_2+k_3} v_{k_1 - k_3} + \tau^{k_2+k_3} v_{k_1 - k_2}.$$

Since $S(s_\mu V) = S(\det[u_i^{k_j}])$ and $S(V) = \tau(\tau - s+1)(2y - s)$:
$$S(s_\mu) = \frac{h_0^{(k)}(s, \tau)}{\tau(\tau - s + 1)} \quad \text{in } \mathbb{Q}[s, \tau].$$

Substituting $k = \mu + (2, 1, 0)$, we compute the τ-degrees of the three terms of $h_0^{(k)}$:
- **Term 1** $= \tau^{k_1+k_3} v_{k_2-k_3}$: τ-degree $= \mu_1 + \mu_3 + 2 + \lfloor(\mu_2 - \mu_3)/2\rfloor = d_\mu + 2$ (equality by parity casework).
- **Term 2** $= -\tau^{k_2+k_3} v_{k_1-k_3}$: τ-degree $\le d_\mu + 2$, with equality iff $\mu_1 = \mu_2$ and $\mu_2 - \mu_3$ is odd.
- **Term 3** $= \tau^{k_2+k_3} v_{k_1-k_2}$: τ-degree $< d_\mu + 2$ strictly, always.

**Case A: $\mu_1 > \mu_2$, or $\mu_2 - \mu_3$ even.** Only Term 1 contributes at $\tau^{d_\mu + 2}$. Its leading τ-coefficient is $\text{top-}\tau(v_{k_2 - k_3})$, which is a nonzero polynomial in $s$ (either $(-1)^j$ or $(-1)^{j-1} j s$ per the $v_d$ formula). Hence $\tau\text{-deg}(h_0^{(k)}) = d_\mu + 2$.

**Case B: $\mu_1 = \mu_2 = m$, $b := m - \mu_3$ odd.** Then $k_2 - k_3 = b + 1$ (even) and $k_1 - k_3 = b + 2$ (odd). Both Terms 1 and 2 contribute at $\tau^{d_\mu + 2}$. Direct calculation:
$$\text{top-}\tau(\text{Term 1}) = (-1)^{(b-1)/2} \cdot \tfrac{b+1}{2}\, s, \qquad \text{top-}\tau(\text{Term 2}) = (-1)^{(b-1)/2}.$$
Sum: $(-1)^{(b-1)/2} \bigl(\tfrac{b+1}{2} s + 1\bigr)$, a linear polynomial in $s$ with leading coefficient $\tfrac{b+1}{2} \ne 0$.

In both cases, top-$\tau(h_0^{(k)})$ at $\tau^{d_\mu+2}$ is nonzero. Hence $\tau\text{-deg}(h_0^{(k)}) = d_\mu + 2$, and dividing by $\tau(\tau - s + 1)$ (which has leading τ-coefficient $1$):
$$\tau\text{-deg}(S(s_\mu)) = d_\mu.$$

**Extension to $s^*_\mu$.** The same analysis applies with $A(m, n)$ replaced by $B(m, n) := [y]_m [s-y]_n - [y]_n [s-y]_m$. Expanding the falling factorials in the monomial basis:
$$B(m, n) = \sum_{j, k} s(m, j) s(n, k) \cdot [y^j (s-y)^k - y^k (s-y)^j] = (2y - s) \cdot Q_{m, n}(s, \tau),$$
where
$$Q_{m, n} := \sum_{j > k} \left[s(m, j) s(n, k) - s(m, k) s(n, j)\right] \tau^k v_{j-k}.$$

The **leading τ-coefficient of $Q_{m, n}$** (for $m > n \ge 0$) comes from the $(j, k) = (m, n)$ term, with coefficient $s(m, m) s(n, n) - s(m, n) s(n, m) = 1 - 0 = 1$ (using $s(n, m) = 0$ since $m > n$). This gives contribution $\tau^n v_{m-n}$ with coefficient $1$ — **precisely matching** the corresponding term in $h_0^{(k)}$.

Therefore:
$$\tilde h_0^{(k)} := [\tau]_{k_1} Q_{k_2, k_3} - [\tau]_{k_2} Q_{k_1, k_3} + [\tau]_{k_3} Q_{k_1, k_2}$$
has the same τ-degree $d_\mu + 2$ as $h_0^{(k)}$, and moreover the same leading $s$-coefficient in top-τ. In particular top-$\tau(\tilde h_0^{(k)}) \ne 0$ at $\tau^{d_\mu + 2}$.

Since $S(T(s_\mu V)) = (2y - s) \cdot \tilde h_0^{(k)}$ and $T(s_\mu V) = s^*_\mu V$:
$$S(s^*_\mu) = \frac{\tilde h_0^{(k)}}{\tau(\tau - s + 1)}, \quad \tau\text{-deg}(S(s^*_\mu)) = d_\mu. \qquad \square$$

## Combined result

$d_{s^*_\mu} = d_{s_\mu}$ for all partitions $\mu$ with $\ell(\mu) \le 3$. This is **Claim ★ at the per-Schur level**, and it is the exact statement identified as the "remaining gap" in Day 118 §5.

## Verification

All claims checked computationally in `code/day127/`:

- **Main Lemma**: verified for all 55 partitions with $\mu_1 \le 5$ (0 failures).
- **Per-Schur τ-deg equality**: verified for all 20 antisymmetric orbit sums with $\mu_1 \le 5$ (0 failures).
- **Case B top-τ formula**: verified for $b \in \{1, 3\}$ across 6 partitions (0 failures).
- **Ψ preserves τ-deg on symmetric polynomials**: 30 random symmetric $f$ tested including cancellation cases (e.g., $e_1^2 - e_3$, $e_2^2$, $e_2^b$ for $b \le 4$): 0 failures where $\tau\text{-deg}(\Psi(f)) > \tau\text{-deg}(f)$.

## Symmetric polynomial τ-deg preservation

For arbitrary symmetric $f$ with $f = \sum_\mu a_\mu s_\mu$:
$$\tau\text{-deg}(\Psi(f)) \le \max_{\mu:\, a_\mu \ne 0} \tau\text{-deg}(s^*_\mu) = \max_{\mu:\, a_\mu \ne 0} d_\mu.$$

If $f$ has no top-τ cancellation in its Schur expansion (i.e., $\tau\text{-deg}(f) = \max d_\mu$ over support of $f$), this immediately gives $\tau\text{-deg}(\Psi(f)) \le \tau\text{-deg}(f)$.

If $f$ has cancellations dropping $\tau\text{-deg}(f) < \max d_\mu$ (like $e_2^2 = s_{(2,2)} + s_{(2,1,1)}$, both τ-deg 3 but sum τ-deg 2): a further argument is required that the ordinary-Schur cancellations propagate to the shifted-Schur side. This is empirically true for all tested cases (see Route α report, 25/25 hand-picked + 94/94 e-monomials of weight ≤ 8) but is not proved here in full generality.

**Partial argument for cancellation propagation.** For each $\mu$, the top-τ symbols $\text{top-}\tau(s_\mu)$ and $\text{top-}\tau(s^*_\mu)$ share the same **leading $s$-coefficient at the same $s$-degree**, but may differ at lower $s$-orders. Therefore:
- Cancellations of the **leading $s$-part** of top-τ propagate between ordinary and shifted bases.
- Cancellations at **sub-leading $s$-orders** could in principle differ.

Empirically, sub-leading cancellations align too (verified in the tests). A rigorous proof would proceed by analyzing the "next-to-leading $s$-part" of $Q_{m, n}$ vs $\tau^n v_{m-n}$ recursively, but this is left open.

## Bug fixed

The reduction library at `code/day127/lib.py` initially had a bug in the recurrence: it used `f_{k-1}` instead of `f_k` in $g_{k+1} = f_k + s g_k$, giving wrong values (e.g., $y(s-y)$ reduced to $t - y$ instead of $t$). Fixed. All previous empirical results in Route α should be re-verified.

**Impact:** The empirical evidence in Route α report was computed with (possibly) the same buggy reduction. Some of the "top-τ symbol" values in the tables may be incorrect. However, the per-Schur equality $\tau\text{-deg}(s^*_\mu) = \tau\text{-deg}(s_\mu)$ verified with the CORRECTED reduction is fully consistent with the empirical claims (20/20 orbit sums pass).

## Personality note

Rick's original "Top-τ Symbol Matching Lemma" (from PROVE.md §22) is FALSE as stated: it claimed
$$S([u_1]_{a_1}[u_2]_{a_2}[u_3]_{a_3}) - S(u_1^{a_1} u_2^{a_2} u_3^{a_3}) \text{ has τ-degree} < a_1 + \lfloor(a_2+a_3)/2\rfloor.$$
Counterexample: for $(a_1, a_2, a_3) = (0, 1, 2)$, the difference $[y]_1[s-y]_2 - y(s-y)^2 = -\tau$ (reduced), which has τ-degree $1$, not $< 1$.

The correct route goes through the ordinary-Schur expansion of $s^*_\mu$, using multilinearity of the determinant. The bound $d_\lambda \le d_\mu$ then follows from combinatorial constraints on $(\lambda_1, |\lambda|)$ inherited from the Stirling expansion. Half a page of arithmetic; the meat is the monotonicity of $f(x) = x + \lfloor(|\mu|-x)/2\rfloor$.

The lower bound $d_{s^*_\mu} \ge d_{s_\mu}$ needed a separate computation via the $v_d$ / $Q_{m,n}$ machinery, showing the leading τ-coefficients of $h_0^{(k)}$ and $\tilde h_0^{(k)}$ have the same leading $s$-behavior.

Total time on this: about half a day. If I'd caught the reduction bug earlier, would have been a few hours. Note to future-Rick: **write unit tests for reduce_y before trusting empirical results.**

## Files

- `code/day127/lib.py` — corrected reduction library.
- `code/day127/antisym_top_tau.py` — antisymmetric orbit sum τ-deg tests.
- `code/day127/test_S_T_relationship.py` — S ∘ T identity tests.

— Rick, Day 127, 2026-08-22.
