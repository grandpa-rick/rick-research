---
title: Day 118 — Molev-Sagan verification and proof of the Strong per-term shifted-Pieri claim (**)
status: STRONG PROGRESS — (**) verified for |mu| <= 10 (67 cases, 100% pass) AND a complete proof outline via a new closed-form formula for d_mu. Only the identity d_{s*_mu} = d_{s_mu} (Day 117 §4 empirical observation) remains as a gap.
---

# Day 118 — Molev-Sagan Verification and Proof of (**)

## §0. Setup

The Strong per-term shifted-Pieri claim (**) from Day 117:

> In s*_{(1,1)} · s*_mu = Σ_lambda c^lambda_mu · s*_lambda, every "lower"
> lambda appearing (i.e., lambda NOT obtained from mu by a vertical 2-strip)
> satisfies d_lambda <= d_mu + 1, where d_lambda = (u,pi)-wdeg(s*_lambda).

Recall d is measured under weights (u, sigma, pi) = (1, 0, 1) — equivalently
(e_1, e_2, e_3) has weights (1, 1, 2) — and by Char. Lemma this is captured
by the t-degree of the substitution e_1 = t+s, e_2 = (s+1)t, e_3 = t^2
(corresponding to u = pi = t, sigma = s).

## §1. Numerical extension: |mu| <= 10

Extended Rick's verification from |mu| <= 6 (23 cases) to |mu| <= 10
(67 cases). ALL PASS.

- Code: `code/day118/verify_pieri_extended.py`.
- Log (|mu| <= 10): `/tmp/day118_verify_10.log` (67 cases, 280 s total).
- Full output shows every mu with |mu| <= 10 and ell(mu) <= 3 satisfies (**).

**No failures found.**

Optimization vs. Day 117: restrict basis to the a priori Molev-Sagan support
supp(s*_{(1,1)} · s*_mu) = { lambda : mu ⊆ lambda, |lambda|-|mu| in {0,1,2},
ell(lambda) <= 3 } (14 or fewer lambdas per mu, vs. all partitions of size
<= |mu|+2 in Day 117). This cut wall time roughly 3x.

## §2. NEW CLOSED FORM for d_mu

**Theorem (verified for |mu| <= 10).**
$$d_\mu \;=\; \mu_1 + \left\lfloor \frac{\mu_2 + \mu_3}{2} \right\rfloor \quad \text{for } \ell(\mu) \le 3.$$

- Code verifying against SymPy: `code/day118/d_mu_conjecture.py`. 67 cases, all match.

### Derivation (proof of d_mu formula for ordinary Schur)

Under the Char. Lemma substitution, (u, y, c) are roots of
$z^3 - (t+s)z^2 + (s+1)tz - t^2 = (z - t)(z^2 - sz + t)$.
So one root is u = t; the other two (y, c) satisfy y+c = s, yc = t.

Applied to the ORDINARY Schur s_mu(u, y, c), branching rule gives:
$$s_\mu(t, y, c) = \sum_{\substack{\mu' \subseteq \mu \\ \mu/\mu' \text{ horiz strip} \\ \ell(\mu') \le 2}} t^{|\mu| - |\mu'|} \cdot s_{\mu'}(y, c).$$

For a 2-part $\mu' = (p, q)$, by the Jacobi-Trudi determinant:
$$s_{(p, q)}(y, c) = (yc)^q \cdot h_{p-q}(y, c) = t^q \cdot h_{p-q}(y, c).$$

Since $y + c = s, yc = t$: $\sum_k h_k(y,c) z^k = 1/(1 - sz + tz^2)$, so
$h_k(y,c)$ is a polynomial in $s, t$ with terms $s^a t^b$ where $a + 2b = k$.
Hence $\deg_t h_k(y, c) = \lfloor k/2 \rfloor$.

The t-degree of a summand for $\mu' = (p, q)$ is
$$(|\mu| - p - q) + q + \lfloor (p - q)/2 \rfloor = |\mu| - p + \lfloor (p-q)/2 \rfloor.$$

Constraints on $\mu' = (p, q)$ from "mu/mu' is a horizontal strip" (each column
loses at most 1 cell); working these out for $\mu = (a, b, c)$ with $a \ge b \ge c$:
$b \le p \le a$, $c \le q \le b$.

Maximizing $|\mu| - p + \lfloor (p-q)/2 \rfloor$ over these:
- Minimize $q$ (increases $\lfloor(p-q)/2\rfloor$) → $q = c$.
- Then minimize $p$ subject to $p \ge b$, i.e., $p = b$.
- Value: $|\mu| - b + \lfloor (b-c)/2 \rfloor = a + c + \lfloor (b-c)/2 \rfloor$.

By elementary casework:
$c + \lfloor (b-c)/2 \rfloor = \lfloor (b+c)/2 \rfloor.$
(Case b+c even: b, c same parity, so (b-c)/2 is exact; c + (b-c)/2 = (b+c)/2.
Case b+c odd: (b-c)/2 loses 1/2, so c + (b-c-1)/2 = (b+c-1)/2 = ⌊(b+c)/2⌋.)

Therefore
$$d_{s_\mu} \;=\; a + \lfloor (b + c) / 2 \rfloor \;=\; \mu_1 + \lfloor (\mu_2 + \mu_3)/2 \rfloor. \qquad \Box$$

### From ordinary to shifted Schur

The shifted Schur $s^*_\mu = s_\mu + \sum_{|\lambda| < |\mu|} c^\mu_\lambda s_\lambda$
in the ordinary Schur basis. Day 117 §4 empirical fact:
$$d_\lambda \le d_\mu \quad \text{whenever } c^\mu_\lambda \ne 0 \text{ in this expansion}.$$

Given this, $d_{s^*_\mu} \le \max(d_{s_\mu}, \max_\lambda d_\lambda) = d_{s_\mu}$.
Conversely, $d_{s^*_\mu} \ge d_{s_\mu}$ because $s_\mu$ is the top polynomial-
degree part of $s^*_\mu$, and (u, pi)-wdeg respects this. So
$$d_{s^*_\mu} = d_{s_\mu} = \mu_1 + \lfloor (\mu_2 + \mu_3)/2 \rfloor.$$

Verifying the "empirical fact" $d_\lambda \le d_\mu$ for the shifted-to-ordinary
transition is currently an OPEN GAP (a Day 117 empirical observation for
|mu| <= 6, hasn't been rigorously derived here). See §5.

## §3. Proof of (**) using the d_mu formula

Enumerate all "lower" lambdas in supp(s*_{(1,1)} · s*_mu).

For mu = (a, b, c) with a >= b >= c >= 0:

### Sub-case (a) — |nu| = |mu| + 2, non-vertical 2-strip

Only horizontal 2-strips remain to consider (i.e., both boxes in the same row).

**Molev-Sagan / classical fact.** The |nu|=|mu|+2 coefficient in
$s^*_{(1,1)} \cdot s^*_\mu$ equals the CLASSICAL Littlewood-Richardson
coefficient $c^\nu_{(1,1), \mu}$ (Molev-Sagan Thm 3.1: the top-degree part
is the ordinary Schur multiplication). The classical Pieri rule for $s_{(1,1)}$
gives $s_{(1,1)} \cdot s_\mu = \sum_{\nu/\mu \text{ vert 2-strip}} s_\nu$
(no horizontal 2-strips). Hence for any horizontal-2-strip nu,
$$c^\nu_{(1,1), \mu} = 0.$$

**Empirical confirmation.** `code/day118/inspect_horiz_row1.py`: for all mu
with |mu| <= 8, the coefficient of $s^*_{(a+2, b, c)}$ in
$s^*_{(1,1)} \cdot s^*_\mu$ is 0. Also 0 for $s^*_{(a, b+2, c)}$ and
$s^*_{(a, b, c+2)}$ when these are valid partitions.

So sub-case (a) contributes nothing to the sum and is trivially OK. ✅

### Sub-case (b) — |nu| = |mu| + 1, add one box

The three candidates (row 1, 2, 3):

**Row 1:** nu = (a+1, b, c). d_nu = (a+1) + ⌊(b+c)/2⌋ = d_mu + 1.
Bound d_nu <= d_mu + 1 holds with equality. ✅

**Row 2:** nu = (a, b+1, c). d_nu = a + ⌊(b+c+1)/2⌋.
$$\lfloor (b+c+1)/2 \rfloor - \lfloor (b+c)/2 \rfloor = \begin{cases} 1 & b+c \text{ even} \\ 0 & b+c \text{ odd} \end{cases}$$
So d_nu ∈ {d_mu, d_mu + 1}. Bound d_nu <= d_mu + 1 holds. ✅

**Row 3:** nu = (a, b, c+1). Same as row 2 by symmetry (b, c enter the formula
symmetrically). Bound holds. ✅

### Sub-case (c) — nu = mu

d_nu = d_mu. Trivially d_nu <= d_mu + 1. ✅

**Molev-Sagan coefficient.** By Molev-Sagan Vanishing Thm 2.1, this coefficient
equals $s^*_{(1,1)}$ evaluated at the shifted point $\mu = (a_{\mu_1}, a_{\mu_2}, ...)$:
$$c^\mu_\mu = s^*_{(1,1)}(\mu) = (\mu_1 + n - 1)(\mu_2 + n - 2) - (\text{...})$$
(explicit formula from Vanishing Thm; nonzero as long as (1,1) ⊆ mu).

But since d_mu <= d_mu + 1 trivially, no computation of the coefficient is
needed for (**). ✅

### Conclusion

Combining sub-cases (a), (b), (c):

$$\boxed{\text{(**)} \text{ is PROVED for } \ell(\mu) \le 3 \text{ from:}}$$
1. Closed form $d_\mu = \mu_1 + \lfloor (\mu_2 + \mu_3)/2 \rfloor$ (proved
   above from Char. Lemma + branching + Jacobi-Trudi + $y+c=s, yc=t$
   substitution) — modulo the identity $d_{s^*_\mu} = d_{s_\mu}$.
2. Classical Pieri: only vertical 2-strips appear in the top-degree part
   of $s_{(1,1)} \cdot s_\mu$.
3. Molev-Sagan Thm 3.1: the top-degree part of $s^*_{(1,1)} \cdot s^*_\mu$
   equals the classical $s_{(1,1)} \cdot s_\mu$ (in ordinary Schur / LR terms).
4. Arithmetic (floor formula): $\lfloor (b+c+1)/2 \rfloor \le \lfloor (b+c)/2
   \rfloor + 1$ (always).

## §4. Surprising patterns in coefficients

Symbolic output (`code/day118/molev_sagan_direct.py`) reveals the following:

**Coefficient of "add box row 1"** (i.e., $c^{(a+1,b,c)}_\mu$): equals 0 when
$\mu_2 = 0$, and appears to depend on $\mu_2$ otherwise. Small cases:
- mu=(1,1,0): 1;   mu=(2,1,0): 1;   mu=(2,2,0): 2
- mu=(3,1,0): 1;   mu=(3,2,0): 2;   mu=(3,3,0): 3
- mu=(2,1,1): 2;   mu=(3,1,1): 2;   mu=(3,2,1): 3
- mu=(1,1,1): 2;   mu=(2,2,2): ?

Conjecturally $c^{(a+1,b,c)}_\mu = b + c \cdot [\text{indicator}]$ or similar
— not yet crystallized.

**Coefficient of ν=μ (bottom):** equals $s^*_{(1,1)}(\mu; n)$, a symmetric
polynomial in the μ_i of degree 2, always positive. Small cases:
- mu=(1,1,0): 2;   mu=(2,1,0): 3;   mu=(2,2,0): 6
- mu=(3,1,0): 4;   mu=(3,2,0): 8;   mu=(3,3,0): ...
- mu=(1,1,1): 6;   mu=(2,1,1): 8;   mu=(2,2,1): 12
- mu=(3,1,1): 10;  mu=(3,2,1): 15

Values match $s^*_{(1,1)}(\mu_1, \mu_2, \mu_3) = h_2(\mu) - e_2(\mu)$ perhaps
— to be checked.

## §5. Remaining gap

The formula $d_{s^*_\mu} = d_{s_\mu}$ requires that in the ordinary-Schur
expansion of $s^*_\mu$, every coefficient $c^\mu_\lambda \ne 0$ satisfies
$d_\lambda \le d_\mu$. This is Day 117 §4 (empirically verified |mu| <= 6).

A path to close this: use the explicit formula
$s^*_\mu = \det[(x_i | a)^{k_j}] / V(x)$ where $(x|a)^k = (x - a_0)(x - a_1)
\cdots (x - a_{k-1})$ with $a_i = i - 1$. Expand each falling factorial as
$(x|a)^k = x^k - \binom{k}{2} x^{k-1} + \dots$; the correction terms lower
polynomial degree by 1, 2, etc. This gives $s^*_\mu = s_\mu + \sum
(\text{lower Schurs}) \cdot (\text{integers})$; controlling which Schurs
appear is combinatorial. The Okounkov–Olshanski formula / vanishing theorem
should give a clean handle.

## §6. Files

- `code/day118/verify_pieri_extended.py` — extended numerical verification of
  (**), covers |mu| <= 10. All 67 cases pass.
- `code/day118/d_mu_formula.py` — dumps d_mu for all mu with |mu| <= 10.
- `code/day118/d_mu_conjecture.py` — verifies closed-form d_mu formula.
- `code/day118/prove_bound_from_formula.py` — structural test showing that
  the ONLY structural failure is horizontal 2-strips in row 1 (which are
  killed by classical Pieri).
- `code/day118/inspect_horiz_row1.py` — confirms horizontal-2-strip-row-1
  coefficients are 0 empirically.
- `code/day118/analyze_cases_bc.py` — verifies (b), (c) sub-cases hold
  structurally up to |mu| <= 15.
- `code/day118/molev_sagan_direct.py` — dumps coefficient tables for all mu.
- `code/day118/prove_d_formula.py` — Derivation of the d_mu formula
  (docstring); numerical verification.
- `/tmp/day118_verify_10.log` — verification log for |mu| <= 10.

## §7. Meta

Day 118 achieved:
1. **Numerical**: (**) now verified through |mu| <= 10 (67 cases). No failures.
2. **New closed form** for $d_\mu$: cleanest possible statement, immediately
   testable, and reveals structure of the (u, pi)-degree filtration.
3. **Complete proof outline** for (**), reducing to two known facts
   (Char. Lemma + branching for the d formula; classical Pieri + Molev-Sagan
   Thm 3.1 for the top-degree coefficient) plus one remaining gap
   ($d_{s^*_\mu} = d_{s_\mu}$).

The critical insight: the "dangerous" case (a) horizontal 2-strip in row 1
DOES give a lambda with $d_\lambda = d_\mu + 2 > d_\mu + 1$, but its coefficient
VANISHES by classical Pieri. This is the pivot point of the whole argument.

**Streak continues:** Day 117 + Day 118 together reduce StructB to the identity
$d_{s^*_\mu} = d_{s_\mu}$ and (**) is otherwise fully proved.

— Compute agent for Rick, Day 118.
