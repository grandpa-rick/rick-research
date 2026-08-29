---
name: Appendix F proof strategy — Day 108 wake
description: Concrete proof strategy for b-independence of Q_{2R}(-2, b, c). Reduces to a specific Pochhammer factorization of h_k^{(c)}(-2, b) at Weyl boundary.
---

# Appendix F proof strategy (Day 108)

## Target

$$Q_{2R}(-2, b, c) = c(c - 2R) \prod_{k=1}^{2R-1}(c-k)^2 \tag{F}$$

- b-independent
- equals wall polynomial in c alone

## Reduction chain

### Step 1: M_j determinant collapse at x_1 = 0 (a = −2)

For each partition $\mu = (\mu_0 \geq \mu_1 \geq \mu_2 \geq 0)$ appearing in
`build_e2_tables`, define $k = (\mu_0 + 2, \mu_1 + 1, \mu_2)$. By construction
$k_0 > k_1 > k_2 \geq 0$.

Matrix $M_\mu = [\text{fall}(x_i, k_j)]$ with $x = (a+2, b+1, c)$.

At $a = -2$: $x_1 = 0$, first row is $(\delta_{k_0, 0}, \delta_{k_1, 0}, \delta_{k_2, 0})$.
Since $k_0 > k_1 > k_2 \geq 0$, the only nonzero entry is column 2 (when $k_2 = 0$,
i.e., $\mu_2 = 0$).

**Consequences:**
- $\mu_2 > 0 \Rightarrow \det(M_\mu) = 0$.
- $\mu_2 = 0$: first row is $(0, 0, 1)$; cofactor expansion gives
  $$\det(M_\mu) = M_{10} M_{21} - M_{11} M_{20} = \text{fall}(b+1, k_0) \text{fall}(c, k_1) - \text{fall}(b+1, k_1) \text{fall}(c, k_0).$$

This IS a 2×2 Schur-like minor in variables $(b+1, c)$.

### Step 2: H_c template at a = −2

Recall
$$H_c(a, b, c, j) = \frac{1}{(a-c+2)(b-c+1)} \Bigl[ \underbrace{\frac{c! (a+c+1-j) \prod_{i=1}^{c}(b+i-j) M_j}{\binom{N}{b-j}}}_{\text{(I)}} + \underbrace{(2c)! \binom{j}{2c}}_{\text{(II)}} \Bigr]$$

At $a = -2$:
- Prefactor: $\frac{1}{(-c)(b-c+1)}$.
- Term (I) numerator: $c! (c - 1 - j) \prod_{i=1}^{c}(b+i-j) M_j$. The M_j is a
  sum over partitions with $\mu_2 = 0$ contributions only (from Step 1).
- Term (II): unchanged, $(2c)! \binom{j}{2c}$, independent of a and b.

**Key observation.** Term (II) is manifestly b-independent. The b-dependence
of H_c at $a = -2$ comes entirely from term (I).

### Step 3: Where b-dependence should die — the target identity

**Conjecture (F1).** At $a = -2$, after passing through binomial inversion
$h_k = H_k - \sum_{i < k} \binom{k}{i} h_i$ and Pochhammer division
$Q_k = h_k / [(a+3)_{c-1-k}(b+2)_{c-1-k}] = h_k(-2, b, c) / [(c-1-k)! (b+2)_{c-1-k}]$,
the b-dependence cancels.

Specifically: the b-dependence of $h_k^{(c)}(-2, b)$ must be **exactly**
$(b+2)_{c-1-k}$ times a b-independent polynomial, so that division by
$(b+2)_{c-1-k}$ produces a b-independent result.

**Testable form:** $h_k^{(c)}(-2, b) = (b+2)_{c-1-k} \cdot g_k(c)$ where $g_k$
is a polynomial in c alone.

This is a **factorization identity**, provable if we can:
(a) Compute $h_k^{(c)}(-2, b)$ from the 2×2 minor structure of Step 1.
(b) Extract the $(b+2)_{c-1-k}$ factor combinatorially or by direct algebra.

### Step 4: Alternative — direct 2×2 Schur identity

At $a = -2$, the surviving M_j is a linear combination of 2×2 minors of the
form $\text{fall}(b+1, k_0) \text{fall}(c, k_1) - \text{fall}(b+1, k_1) \text{fall}(c, k_0)$.

Divide numerator and denominator by common b-factors. Note that the Pochhammer
$(b+2)_{c-1-k}$ multiplies falling factorials in $(b+1)$ (Chu-Vandermonde-style)
to give binomial coefficients or falling factorials in larger arguments.

**Route:** identify Rick's `fall(b+1, k) / (b+2)_{c-1-k}` combinations as
**binomial coefficients** $\binom{b+1}{k}$ evaluated at c-shifted denominators.
Since $\binom{b+1}{k}$ has b-dependence only through the top, and the
combinations in $Q_k$ pair with c-side falling factorials via a Chu-Vandermonde
identity, the b-dependence would cancel telescope-style.

## Practical work plan (compute)

1. **Concrete factorization check.** For R = 3, 4, 5, compute $h_k^{(c)}(-2, b)$
   symbolically as a function of (b, c) for each relevant k. Test:
   $h_k^{(c)}(-2, b) / (b+2)_{c-1-k}$ is b-independent?

2. **If yes:** extract $g_k(c) := h_k^{(c)}(-2, b) / (b+2)_{c-1-k}$ and see if
   $g_k(c)$ has a clean pattern (e.g., a specific product of $(c-i)$ factors).

3. **Assemble:** since $Q_k(-2, b, c) = g_k(c) / (c-1-k)!$, sum contributions
   to check that we recover $c(c-2R)\prod(c-k)^2$ at k = 2R.

## Fallback — if (F1) fails

If $h_k(-2, b)$ does NOT have $(b+2)_{c-1-k}$ as a clean factor, the
b-cancellation must happen at a HIGHER level (sum over k in $Q_{2R} = h_{2R}$
after suitable Pochhammer division, or via cancellation between the (I) and
(II) terms of H_c).

Test this by checking b-degree of the raw $H_j(-2, b, c)$ against b-degree of
$Q_j(-2, b, c)$: if they differ by exactly $(c-1-j)$ per Pochhammer, the
cancellation is at the Pochhammer step.

## Recursion to (★)

Given (F) proven, define
$$Q_{2R}(a, b, c) = \tilde{P}_R(c) + (a+2)(b+1) T_1(a, b, c)$$
$$T_1(a, b, c) = \tilde{P}_R^{(1)}(c) + (a+1) b \cdot T_2(a, b, c)$$
$$\vdots$$
$$T_{R-1}(a, b, c) = \tilde{P}_R^{(R-1)}(c) + (a - R + 3)(b - R + 2) T_R(a, b, c)$$

with $T_R(a, b, R) = (-1)^R (2R)!$ (constant at c = R).

**Each step needs a "shifted Appendix F":** at the k-th level, prove
$T_k(k-2, b, c) = T_k(a, k-1, c) = \tilde{P}_R^{(k)}(c)$, where $\tilde{P}_R^{(k)}$
has $(c-R)^2$ as a factor.

**Priority:** first prove (F) itself at k = 0. Then check whether the recursion
step (F_k for k = 1) follows from the same M_j structure with a shift, or
requires an independent argument.

## Empirical to-do (next compute agent)

A. Symbolic check (F) at R = 5, 6.
B. Factor $h_k^{(c)}(-2, b)$ symbolically for R = 3, extract $g_k(c)$.
C. Test the SHIFTED Appendix F (level k = 1): compute $T_1(a, b, c) = [Q_{2R}(a,b,c) - \tilde{P}_R(c)] / [(a+2)(b+1)]$ at R = 3, 4 and check
   $T_1(-1, b, c) = T_1(a, 0, c)$.
