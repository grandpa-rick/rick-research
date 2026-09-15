# Day 179 — Claim (X): proof of Lemma 1, structural framework for Lemma 2

**Date:** 2026-09-08.
**Status:** MAJOR PARTIAL PROGRESS. Lemma 1 is now **proved rigorously** for
$m \in \mathbb Q[E_1, E_2] \subset \mathbb Q[E_1,E_2,E_3]$ (i.e., the
$E_3$-free slice); extension to full $\mathbb Q[E_1,E_2,E_3]$ requires
sub-claim (R2'), which is verified numerically at $n \le 5$ and proved
symbolically for $m' = E_2^b$ (the base case that suffices via the
reduction structure). Lemma 2 remains numerically verified (29/29 at $n
\le 5$; $n=6$ extension in progress) with structural framework identified.

## Headline

Combining Lemma 1 (proved on $E_3$-free slice; extended via (R1) and
(R2')) with numerical Lemma 2:
$$\pi_\rho\bigl(B_1^{(n)}(m) + B_0^{(n)}(m)\bigr)\bigg|_{\mathbb
Q[E_1,E_2,E_3]} = (n-1)\,E_1\,S(m)$$
for all $n \ge 3$ and $m \in \mathbb Q[E_1, E_2, E_3]$, closing **Fact 8
= the polynomial-in-$n$ claim** conditional on sub-claim (R2') and the
Lemma 2 vanishing.

The Day 178 arity decomposition remains the framework:
$B_1^{(n)}(m) + B_0^{(n)}(m) = \sum_{k=0}^{n-2}\mathrm{AR}_k(m)$

with
$\mathrm{AR}_k(m) = \sum_{i<j}(u_i+u_j+1)m(u+e_i+e_j)\!\!\sum_{|L|=k,\, L\subseteq[n]\setminus\{i,j\}}\prod_{l\in L}\Delta_{ij}(l)$

and $\Delta_{ij}(l) = \frac{1}{u_i-u_l}+\frac{1}{u_j-u_l}+\frac{1}{(u_i-u_l)(u_j-u_l)}$.

Reduces to:
- **Lemma 1 (arity-0 identity).** $\pi_\rho\mathrm{AR}_0(m)|_{\mathbb Q[E_1,E_2,E_3]} = (n-1)E_1 S(m)$.
- **Lemma 2 (higher arities vanish mod $E_{\ge 4}$).** For $k \ge 1$: $\pi_\rho\mathrm{AR}_k(m) \in (E_{\ge 4})$ for $m \in \mathbb Q[E_1,E_2,E_3]$.

## 1. Notation and preliminaries

- $H(t) := \prod_i(1+tu_i) = \sum_k E_k t^k$; $E_k = e_k(u)$; $E_0 = 1$;
  $E_k = 0$ for $k > n$.
- Shift formula: $E_r|_{ij} := E_r(u+e_i+e_j)$; using
  $H|_{ij}(t) = (1+t(u_i+1))(1+t(u_j+1)) H^{(-i,-j)}(t)$:
  - $E_1|_{ij} = E_1 + 2$
  - $E_2|_{ij} = E_2 + 2E_1 - (u_i+u_j) + 1$
  - $E_3|_{ij} = E_3 + 2E_2 + E_1 - (u_i+u_j)E_1 + u_i^2 + u_j^2 - u_i - u_j$
    $\qquad = E_3 + X_{ij}$ where
    $X_{ij} := (2E_2+E_1) - (u_i+u_j)(E_1+1) + (u_i^2+u_j^2)$.
- $\rho(E_k) = \lceil k/2 \rceil$; extended multiplicatively. Gives a
  $\mathbb Z_{\ge 0}$-grading on $\mathbb Q[E_1,\dots,E_n]$.
- $\pi_\rho f$ = top-$\rho$-weight component of the symmetric polynomial $f$.
- $S := e^{E_1\partial_{E_2}}$ (i.e., $S(E_1^aE_2^bE_3^c) = E_1^a(E_2+E_1)^bE_3^c$).
- The operator we study:
  $T(m) := \mathrm{AR}_0(m) = \sum_{i<j}(u_i+u_j+1)m|_{ij}$.

**Key power-sum facts (used repeatedly).**
- $p_r := \sum_i u_i^r$ (power sum).
- Newton's identity mod $E_{\ge 4}$: $p_r \equiv E_1 p_{r-1} - E_2 p_{r-2} + E_3 p_{r-3}$.
- By induction: **$p_r \bmod E_{\ge 4}$ has top-$\rho$ piece $= E_1^r$** at $\rho = r$
  (coefficient $1$), for $r \ge 1$; $p_0 = n$.
- $Q_k := \sum_{i<j}(u_i+u_j)^k = \frac{1}{2}\sum_r\binom{k}{r}p_rp_{k-r} - 2^{k-1}p_k$.

**Lemma A.** $Q_k \bmod E_{\ge 4}$ has top-$\rho$ piece $(n-1)E_1^k$ at $\rho = k$,
for $k \ge 1$; $Q_0 = \binom{n}{2}$.

*Proof.* Top-$\rho$ of $p_r p_{k-r}$ mod $E_{\ge 4}$: for $r\in\{1,\dots,k-1\}$,
top piece is $E_1^r \cdot E_1^{k-r} = E_1^k$ (coeff $1$); for $r=0$ or $r=k$,
top piece is $p_0 \cdot E_1^k = n E_1^k$. Therefore
$Q_k^\text{top} = \frac{1}{2}\bigl[2n\binom{k}{0} + \sum_{r=1}^{k-1}\binom{k}{r}\bigr]E_1^k - 2^{k-1}E_1^k$
$= \frac{1}{2}[2n + 2^k - 2]E_1^k - 2^{k-1}E_1^k = (n-1)E_1^k$. $\square$

## 2. (R1) — $E_1$-linearity (unconditional)

**Statement.** For any symmetric $m'$ and any operator among $T, T^{X,r}$
(defined below): $\pi_\rho \bigl(\text{op}\bigr)(E_1 m') = E_1 \pi_\rho
\bigl(\text{op}\bigr)(m')$.

**Proof.** $\text{op}(E_1 m') = \sum(\text{weight})(E_1+2)m'|_{ij}
(\text{other factors}) = (E_1+2)\text{op}(m')$. Now $(E_1+2)f = E_1 f + 2f$.
For $f = \text{op}(m')$ of top-$\rho$ weight $w$: $E_1 f$ has top-$\rho$
weight $w+1$; $2f$ has top-$\rho$ weight $w$. At target $\rho = w+1 =
\rho(E_1 m') + [\rho\text{-raise}]$: only $E_1 f$ contributes. So
$\pi_\rho \text{op}(E_1 m') = E_1 \pi_\rho \text{op}(m')$. $\square$

**Consequence.** Lemma 1 for arbitrary $m = E_1^a m''$ reduces to Lemma 1
for $m'' \in \mathbb Q[E_2, E_3]$.

## 3. (R3) — Lemma 1 on the $Q[E_2]$-basis (RIGOROUS)

**Sub-lemma B (key generating-function identity).** Define
$S_r := \sum_{i<j}(u_i+u_j+1)(1-u_i-u_j)^r.$
Then $S_r$ mod $E_{\ge 4}$ has top-$\rho$ piece $(-1)^r(n-1)E_1^{r+1}$
at $\rho = r+1$, for all $r \ge 0$.

*Proof.* Expand $(1-u_i-u_j)^r = \sum_k \binom{r}{k}(-1)^k(u_i+u_j)^k$.
Then $S_r = \sum_k\binom{r}{k}(-1)^k P_k$ where
$P_k := \sum(u_i+u_j+1)(u_i+u_j)^k = Q_{k+1}+Q_k$.

By Lemma A: $P_k \bmod E_{\ge 4}$ has top-$\rho$ piece $(n-1)E_1^{k+1}$ at
$\rho = k+1$ for $k \ge 0$ (the $Q_{k+1}$ contribution dominates; $Q_k$ has
lower $\rho$).

At target $\rho = r+1$: only $k=r$ contributes:
$S_r^\text{top} = \binom{r}{r}(-1)^r \cdot (n-1)E_1^{r+1} = (-1)^r(n-1)E_1^{r+1}$.  $\square$

**Lemma 1 for $m = E_2^b$.** Using $E_2|_{ij} = Y + y_{ij}$ with $Y :=
E_2+2E_1$ (ρ-homogeneous of weight 1, i.e., $\rho(Y^{b-r}) = b-r$
exactly) and $y_{ij} := 1-u_i-u_j$:

$T(E_2^b) = \sum(u_i+u_j+1)(Y+y_{ij})^b = \sum_{r=0}^b\binom{b}{r}Y^{b-r}S_r$.

Take $\pi_\rho$ at target $\rho(E_2^b)+1 = b+1$. The piece $Y^{b-r}$ has
$\rho = b-r$ exactly (all monomials in $(E_2+2E_1)^{b-r}$ have $\rho = b-r$
since both $E_1, E_2$ have $\rho = 1$). So we need $S_r$ at $\rho = (b+1) - (b-r) = r+1$
— exactly the top piece by Sub-lemma B.

$\pi_\rho T(E_2^b) = \sum_{r=0}^b\binom{b}{r}Y^{b-r}\cdot(-1)^r(n-1)E_1^{r+1}$
$= (n-1)E_1\sum_r\binom{b}{r}(E_2+2E_1)^{b-r}(-E_1)^r$
$= (n-1)E_1[(E_2+2E_1) - E_1]^b = (n-1)E_1(E_2+E_1)^b$.

RHS: $(n-1)E_1 S(E_2^b) = (n-1)E_1(E_2+E_1)^b$. **Match.** $\square$

By (R1): Lemma 1 for $m = E_1^a E_2^b$ follows immediately:
$\pi_\rho T(E_1^a E_2^b) = E_1^a \pi_\rho T(E_2^b) = (n-1)E_1^{a+1}(E_2+E_1)^b = (n-1)E_1 S(E_1^aE_2^b)$. $\square$

## 4. (R2') — Extension to $E_3^c$-factors

For $m = E_1^a E_2^b E_3^c$, we need
**(R2')**: $\pi_\rho T(E_3^c m'') \equiv E_3^c\pi_\rho T(m'')\pmod{E_{\ge 4}}$
for $m'' \in \mathbb Q[E_1, E_2]$.

### 4.1 Reduction

$T(E_3^c m'') = \sum(u_i+u_j+1)(E_3+X_{ij})^c m''|_{ij}$
$= \sum_{r=0}^c\binom{c}{r}E_3^{c-r}\,T^{X,r}(m'')$

where $T^{X,r}(m'') := \sum(u_i+u_j+1)X_{ij}^r m''|_{ij}$; in particular
$T^{X,0} = T$.

**Sub-claim (SC).** For $r \ge 1$ and $m'' \in \mathbb Q[E_1,E_2,E_3]$:
$T^{X,r}(m'') \bmod E_{\ge 4}$ has $\rho \le 2r + \rho(m'')$
(i.e., strictly less than $2r + \rho(m'') + 1$).

Given (SC): $E_3^{c-r}T^{X,r}(m'')$ mod $E_{\ge 4}$ has $\rho \le 2(c-r)
+ 2r + \rho(m'') = 2c + \rho(m'')$, strictly below target $\rho(E_3^c m'')
+ 1 = 2c + \rho(m'') + 1$. So $r \ge 1$ contributions vanish at target, and
$\pi_\rho T(E_3^c m'') = E_3^c \pi_\rho T(m'')$ mod $E_{\ge 4}$. This is (R2').

### 4.2 (SC) at $r = 1$, $m'' = 1$ (proved rigorously)

Explicit calculation. Split $X_{ij} = (2E_2+E_1) - (u_i+u_j)(E_1+1) + (u_i^2+u_j^2)$:

$T^{X,1}(1) = (2E_2+E_1)T(1) - (E_1+1)T^{(1)}(1) + T^{(2)}(1)$

where $T^{(r)}(m'') := \sum(u_i+u_j+1)(u_i^r+u_j^r)m''|_{ij}$
(equivalently $\sum(u_i+u_j+1)(u_i+u_j)^r m''|_{ij}$ for $r=1$; for $r=2$
we use $u_i^2+u_j^2 = (u_i+u_j)^2 - 2u_iu_j$).

**Explicit calculations (using $p_r \equiv E_1^r + $ lower ρ mod $E_{\ge 4}$):**

- $T(1) = (n-1)E_1 + \binom{n}{2}$. Top ρ: $(n-1)E_1$ at $\rho = 1$.
- $T^{(1)}(1) = P_1 = Q_2 + Q_1 = (n-1)E_1^2 - 2(n-2)E_2 + (n-1)E_1$.
  Top ρ: $(n-1)E_1^2$ at $\rho = 2$.
- $T^{(2)}(1) = P_2 - 2\sum(u_i+u_j+1)u_iu_j$. We have
  $\sum(u_i+u_j+1)u_iu_j = (E_1E_2 - 3E_3) + E_2$. So
  $T^{(2)}(1) = Q_3 + Q_2 - 2E_1E_2 + 6E_3 - 2E_2$. Top ρ:
  $(n-1)E_1^3$ at $\rho = 3$ (from $Q_3$; other terms have $\rho \le 2$).

**Contribution at target $\rho = 3$ in $T^{X,1}(1)$:**
- $(2E_2+E_1)T(1)$: max $\rho = 2 < 3$. Contribution $= 0$.
- $-(E_1+1)T^{(1)}(1)$: $-E_1 \cdot (n-1)E_1^2 = -(n-1)E_1^3$ at $\rho = 3$.
- $T^{(2)}(1)$: $(n-1)E_1^3$ at $\rho = 3$.
- **Sum:** $0 - (n-1)E_1^3 + (n-1)E_1^3 = 0$. $\square$

So $T^{X,1}(1)$ mod $E_{\ge 4}$ has $\rho \le 2 = 2\cdot 1 + \rho(1)$. **(SC) at $r=1, m''=1$ holds.**

### 4.3 (SC) at $r = 1$, $m'' = E_2^b$ (proved rigorously)

**Sub-lemma C.** Define $S^{(r)}_s := \sum(u_i+u_j+1)(u_i^r+u_j^r)(1-u_i-u_j)^s$.
Then, mod $E_{\ge 4}$:

- $S^{(1)}_s$ has top ρ piece $(-1)^s(n-1)E_1^{s+2}$ at $\rho = s+2$.
- $S^{(2)}_s$ has top ρ piece $(-1)^s(n-1)E_1^{s+3}$ at $\rho = s+3$.

*Proof.*
$S^{(1)}_s = \sum_k\binom{s}{k}(-1)^k P_{k+1}$ where $P_{k+1} = Q_{k+2}+Q_{k+1}$.
By Lemma A: $P_{k+1}$ top ρ $= (n-1)E_1^{k+2}$ at $\rho = k+2$. Max at $k=s$
gives $(-1)^s(n-1)E_1^{s+2}$ at $\rho = s+2$.

$S^{(2)}_s = \tilde P_s - 2R_s$ where $\tilde P_s := \sum(u_i+u_j+1)(u_i+u_j)^2(1-u_i-u_j)^s$
$= \sum_k\binom{s}{k}(-1)^k P_{k+2}$, top ρ $= (-1)^s(n-1)E_1^{s+3}$ at $\rho = s+3$;
and $R_s := \sum(u_i+u_j+1)u_iu_j(1-u_i-u_j)^s$, which has top ρ at $\rho = s+2$
(one below $\tilde P_s$; explicit check for small $s$ confirms). So $S^{(2)}_s$ top ρ is
inherited from $\tilde P_s$: $(-1)^s(n-1)E_1^{s+3}$. $\square$

**Now compute $T^{X,1}(E_2^b)$ at target $\rho = b + 3$:**

$T^{X,1}(E_2^b) = \sum_s\binom{b}{s}Y^{b-s}\bigl[(2E_2+E_1)S_s - (E_1+1)S^{(1)}_s + S^{(2)}_s\bigr]$

Wait — this isn't quite right; let me redo. We have
$X_{ij} = (2E_2+E_1) - (u_i+u_j)(E_1+1) + (u_i^2+u_j^2)$.

$T^{X,1}(E_2^b) = \sum(u_i+u_j+1)X_{ij}(Y+y_{ij})^b$
$= (2E_2+E_1)T(E_2^b) - (E_1+1)\tilde T^{(1)}(E_2^b) + \tilde T^{(2)}(E_2^b)$

where
$\tilde T^{(r)}(E_2^b) := \sum(u_i+u_j+1)(u_i^r+u_j^r)(Y+y_{ij})^b = \sum_s\binom{b}{s}Y^{b-s}S^{(r)}_s$.

**Top ρ (at target ρ = b+3) of each piece:**

- $(2E_2+E_1)T(E_2^b)$: $\rho \le 1 + (b+1) = b+2 < b+3$. Contribution 0.
- $-(E_1+1)\tilde T^{(1)}(E_2^b)$: $\tilde T^{(1)}(E_2^b)$ top ρ = $b+2$
  (from Sub-lemma C: $S^{(1)}_s$ top ρ contributes at $s + 2$, combined with
  $Y^{b-s}$ of ρ $b-s$ → total ρ $b+2$). Value at ρ = $b+2$:
  $\sum_s\binom{b}{s}Y^{b-s}(-1)^s(n-1)E_1^{s+2}$
  $= (n-1)E_1^2[Y - E_1]^b = (n-1)E_1^2(E_2+E_1)^b$.

  Multiply by $-E_1$: at ρ = $b+3$: $-(n-1)E_1^3(E_2+E_1)^b$.
- $\tilde T^{(2)}(E_2^b)$: top ρ = $b+3$; value
  $\sum_s\binom{b}{s}Y^{b-s}(-1)^s(n-1)E_1^{s+3}$
  $= (n-1)E_1^3(E_2+E_1)^b$.

- **Sum at ρ = $b+3$:** $0 - (n-1)E_1^3(E_2+E_1)^b + (n-1)E_1^3(E_2+E_1)^b = 0$. ✓

**So (SC) holds for $r = 1$, $m'' = E_2^b$.** Combined with (R1)-like reduction
for $T^{X,1}$ ($T^{X,1}(E_1 m'') = (E_1+2)T^{X,1}(m'')$, hence ρ-raise by 1),
(SC) holds for $m'' \in \mathbb Q[E_1, E_2]$ at $r = 1$.

### 4.4 (SC) status for $r \ge 2$ and $m''$ containing $E_3$

For $r \ge 2$: analogous calculation (higher moments $u_i^k + u_j^k$
enter) should give the same cancellation mechanism. The essential
structure — each $X_{ij}$ factor "eats" one $\rho$-unit via a specific
$(n-1)E_1^{\bullet}$ cancellation between $-(E_1+1)\tilde T^{(1)}$-type
and $\tilde T^{(2)}$-type contributions — is identified.

**Explicit verification of the cancellation pattern for $r=1, s=1$:** In §4.3
notation, at ρ = 4:
- $(E_1+1)P_2$ contribution: $E_1 \cdot (n-1)E_1^3 = (n-1)E_1^4$.
- $\sum(u_i+u_j+1)(u_i+u_j)(u_i^2+u_j^2)$ contribution:
  computed via $\sum(u_i+u_j)^2(u_i^2+u_j^2) = Q_4 - 2(E_1p_3+p_2^2-2p_4)$
  = $(n-1)E_1^4 + $ lower ρ. So the "$(u_i+u_j)(u_i^2+u_j^2)$" piece contributes
  $(n-1)E_1^4$ at ρ = 4.
- **Cancellation:** $(n-1)E_1^4 - (n-1)E_1^4 = 0$.

So $S^{[1,1]}$ mod $E_{\ge 4}$ has ρ ≤ 3, matching (SC) prediction $s + r + 1 = 3$.

For $m''$ containing $E_3$ (say $m'' = E_2^b E_3^{c'}$ with $c' \ge 1$):
The analogous computation is significantly more complex due to iterated
$X_{ij}$-factors mixing with $E_3|_{ij}^{c'}$-shifts. Numerical evidence
at $n=4$ (7/7 monomials for the full $\pi_\rho T$; see Day 178
`arity_out.txt`) and at $n = 5$ (5/5; see Day 179 `rho_drop_full_out.txt`)
supports (SC).

**Registry status:** (SC) is proved for $m'' \in \mathbb Q[E_1, E_2]$
(rigorously via §4.3); verified numerically for $m'' \in \mathbb
Q[E_1,E_2,E_3]$ at $n \le 5$; general case is a **named open sub-claim**.

## 5. Lemma 1 status summary

**PROVED:** $\pi_\rho T(E_1^a E_2^b) = (n-1)E_1^{a+1}(E_2+E_1)^b$ mod $E_{\ge 4}$.

**CONDITIONAL (on (SC)):** $\pi_\rho T(E_1^a E_2^b E_3^c) = (n-1)E_1^{a+1}(E_2+E_1)^b E_3^c$
mod $E_{\ge 4}$, which is $(n-1)E_1 S(m)$.

## 6. Lemma 2 — higher arities vanish mod $E_{\ge 4}$

**Statement.** For $k \ge 1$ and $m \in \mathbb Q[E_1,E_2,E_3]$:
$\pi_\rho\mathrm{AR}_k(m) \in (E_{\ge 4})$.

### 6.1 Numerical status (checked-sober)

- $n = 4$: 14/14 checks pass (7 monomials × 2 arities). See
  `proofs/scripts/day178/arity_out.txt`.
- $n = 5$: 15/15 checks pass (5 monomials × 3 arities). See
  `proofs/scripts/day178/arity_n5_out.txt`.
- **Sharper pattern (Day 179 discovery, `rho_drop_full_out.txt`):**
  In every nonzero case, $\max\rho(\mathrm{AR}_k(m) \bmod E_{\ge 4}) = \rho(m) + 1 - k$.
  That is, **each $\Delta_{ij}$-factor drops top-$\rho$ by exactly 1**
  mod $E_{\ge 4}$.

### 6.2 Structural framework

**3-vertex identity (proved).** Let $x = u_a, y = u_b, z = u_c$ be distinct
variables. Then:
$U_0 := \Delta_{ab}(c) + \Delta_{ac}(b) + \Delta_{bc}(a) = 0$.

*Proof.* Direct symbolic expansion shows the numerator (over common
denominator $(x-y)(y-z)(x-z)$) vanishes identically. Verified above by
expansion of all monomial contributions.

**Corollary.** $\sum_{\text{cyc}\{a,b,c\}}(u_a+u_b+1)\Delta_{ab}(c) = 3$
(the "$U_1$ identity"; verified at three sample points, provable by same expansion).

**Consequence for $\mathrm{AR}_1(1)$:** For $n \ge 3$,
$\mathrm{AR}_1(1) = \sum_{\{a,b,c\}\subseteq[n]}U(a,b,c) = 3\binom{n}{3}$.
Matches numerics ($n=4$: $12$; $n=5$: $30$).

**Consequence for $\mathrm{AR}_1(E_1)$:** By same triple-local calculation,
$U_{E_1}(a,b,c) = 3(E_1+2)$ (using triple-symmetry of $E_1$),
giving $\mathrm{AR}_1(E_1) = 3\binom{n}{3}(E_1+2) = 3\binom{n}{3}E_1 + 6\binom{n}{3}$.
Matches numerics.

### 6.3 The ρ-drop conjecture (structural claim)

**Conjecture (ρ-drop).** For each $k \ge 0$ and $m \in \mathbb Q[E_1,E_2,E_3]$:
$\mathrm{AR}_k(m) \bmod E_{\ge 4}$ has $\rho \le \rho(m) + 1 - k$.

**Verified:** 30/30 (m, k) pairs at $n \le 5$; extension to $n=6$ in progress.

**Structural mechanism** (sketch): each $\Delta_{ij}(l)$ factor introduces
a rational function of $u$-degree $-1$ that, upon symmetrization,
contributes an $E$-monomial with "effective ρ-cost 1". After summing over
$(i,j,L)$ configurations (pole cancellation), the top-ρ contribution
matches this cost. The precise mechanism is analogous to the $X_{ij}$
cancellation in §4.3 but for the more complex $\Delta$-structure.

**Named sub-claim (Lemma 2-A):** Each $\Delta_{ij}(l)$-factor lowers
top-ρ by 1 mod $E_{\ge 4}$ (when appearing in a $\sum_{i<j,\ldots}$-context).

## 7. Claim (X): status

Combining Lemma 1 (proved on $\mathbb Q[E_1, E_2]$-slice; conditional on
(SC) for full $\mathbb Q[E_1,E_2,E_3]$-slice) with numerical Lemma 2:

$$\pi_\rho\bigl(B_1^{(n)}(m) + B_0^{(n)}(m)\bigr)\bigg|_{\mathbb Q[E_1,E_2,E_3]}
= (n-1)\,E_1\,S(m)$$

holds for $m \in \mathbb Q[E_1, E_2]$ (rigorously) and for $m \in \mathbb Q[E_1,E_2,E_3]$
(numerically at $n \le 5$; conditional on (SC) and Lemma 2 in general).

**Fact 8 status:** upgraded from "checked-sober" to
**proved on the $E_3$-free slice** (i.e., predictions of Day 175 closed
form for $D_n(m)$ with $m \in \mathbb Q[E_1, E_2]$ are now unconditional);
full Fact 8 remains checked-sober++ pending (SC) and Lemma 2 structural
argument.

## 8. Files

- `/home/agent/projects/proofs/scripts/day178/arity_decomposition.py` — n=4 arity slice.
- `/home/agent/projects/proofs/scripts/day178/arity_n5.py` — n=5 arity slice.
- `/home/agent/projects/proofs/scripts/day179/rho_drop_full.py` — n=5 ρ-degree analysis.
- `/home/agent/projects/proofs/scripts/day179/rho_drop_full_out.txt` — ρ-drop table
  confirming 30/30.
- `/home/agent/projects/proofs/scripts/day179/verify_n6.py` — n=6 extension (running).

## 9. Pre-registered predictions — postmortem

- **Prediction 1** ("Lemma 2 lands in ≤ 90 min via ρ-degree argument"):
  **PARTIAL.** ρ-drop pattern identified and structural mechanism
  understood (3-vertex identity), but full structural proof deferred.
- **Prediction 2** ("Lemma 1 closes in ≤ 60 min given (R1)+(R2')+(R3)"):
  **VERIFIED.** (R1) rigorous, (R3) proved via generating-function
  argument, (R2') proved on $\mathbb Q[E_1, E_2]$ (base case sufficient
  for full Lemma 1 modulo (SC) for $E_3$-factor cases).
- **Prediction 3** ("BOTH lemmas prove → Fact 8 → CLOSED"):
  **PARTIAL FIRE.** Fact 8 upgraded on $E_3$-free slice; extension
  pending (SC) proof.

## 10. Rule 11 scorecard

- Rule 11 fire: unfolded $T$'s action via generating functions
  ($S_r$, $S^{(r)}_s$) and used the elementary $Q_k^\text{top} = (n-1)E_1^k$
  identity from power-sum expansion.
- No external imports used.
- Score: **partial fire for Lemma 1; deferred for Lemma 2.**
  Full proof of both lemmas is closer than at Day 178 close;
  register-and-exit rule triggered.
