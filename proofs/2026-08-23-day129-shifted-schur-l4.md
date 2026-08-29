# Day 129 — Combinatorial τ-degree preservation for shifted Schur, ANY ℓ

**Date:** 2026-08-23
**Author:** Rick (deep-work session)
**Status:** PROVED — and *much* stronger than the target. The combinatorial identity holds for **all** partition lengths ℓ, not just ℓ = 4.

## What we were supposed to prove

Extend Day 127's ℓ ≤ 3 result to ℓ = 4:

> Let $\mu$ be a partition with $\ell(\mu) = 4$, $N \ge 4$. Let $s^*_\mu(u_1, \ldots, u_N)$ be the shifted Schur polynomial (Rick's convention: $s^*_\mu \cdot V(u) = \det[[u_i]_{k_j}]$ with $k_j = \mu_j + N - j$). Expand in ordinary Schur basis:
> $$s^*_\mu = \sum_\lambda c^\mu_\lambda \, s_\lambda.$$
> Set $d_\nu := \nu_1 + \lfloor (|\nu| - \nu_1)/2 \rfloor$. Claim:
> $$d_{s^*_\mu} \;\;:=\;\; \max\{d_\lambda : c^\mu_\lambda \ne 0\} \;\;=\;\; d_\mu.$$

## What I actually proved

The same statement, **for any partition $\mu$ (any $\ell$, any $N \ge \ell(\mu)$)**.

Rick's Day 127 machinery — the substitution $u_2 \to y, u_3 \to s-y$, the Chebyshev polynomials $v_d$, the antisymmetric orbit sums $Q_{m,n}$, and Cases A/B for handling top-τ collisions — was building up a *stronger* theorem: the **algebraic** τ-degree preservation

$$\tau\text{-deg}(S(s^*_\mu)) \;=\; d_\mu \qquad \text{(under a specific Char.\ Lemma substitution)}.$$

The stated **combinatorial** claim (max $d_\lambda$ over the Schur support) is much softer, and follows in half a page from the multilinear Stirling expansion Rick already carried out for the upper bound. He just missed the trivial lower bound.

## Main theorem

**Theorem (Day 129).** Let $\mu$ be a partition, $N \ge \ell(\mu)$, and pad $\mu$ with zeros to length $N$. Let $u_1, \ldots, u_N$ be indeterminates, $k_j := \mu_j + N - j$, $[y]_k := y(y-1)\cdots(y-k+1)$ the falling factorial, $V(u) := \prod_{i<j}(u_i - u_j)$. Define
$$s^*_\mu(u) \;:=\; \det[[u_i]_{k_j}] \big/ V(u).$$
This is a polynomial in $u_1, \ldots, u_N$; expand in the ordinary Schur basis
$$s^*_\mu(u) \;=\; \sum_\lambda c^\mu_\lambda \, s_\lambda(u).$$
Let $d_\nu := \nu_1 + \lfloor (|\nu| - \nu_1)/2 \rfloor$. Then
$$\max\{d_\lambda : c^\mu_\lambda \ne 0\} \;=\; d_\mu.$$

## Proof

### Multilinear Stirling expansion

Signed Stirling numbers of the first kind $s(k, \ell)$ are defined by $[y]_k = \sum_\ell s(k, \ell) \, y^\ell$; they satisfy $s(k, \ell) = 0$ unless $0 \le \ell \le k$, and $s(k, k) = 1$.

Multilinearity of the determinant in columns gives
$$\det[[u_i]_{k_j}] \;=\; \sum_{(\ell_1, \ldots, \ell_N)} \left(\prod_j s(k_j, \ell_j)\right) \det[u_i^{\ell_j}]_{i,j}.$$
Only tuples with distinct $\ell_j$ contribute. Sort each such tuple descending to $\ell'_1 > \cdots > \ell'_N \ge 0$; the associated partition is $\lambda_i := \ell'_i - (N - i)$. Then $\det[u_i^{\ell_j}] = \varepsilon(\pi) V(u) \, s_\lambda(u)$ where $\pi$ is the sorting permutation.

Regrouping by $\lambda$ and using $\varepsilon(\pi) \prod_j s(k_j, \ell'_{\pi(j)}) = $ one term of $\det[s(k_j, \ell'_i)]_{i,j}$:
$$\boxed{\;c^\mu_\lambda \;=\; \det[s(k_j, \ell'_i)]_{i,j}, \qquad \ell'_i = \lambda_i + N - i.\;}$$

### Upper bound: $d_\lambda \le d_\mu$ whenever $c^\mu_\lambda \ne 0$

Suppose $c^\mu_\lambda = \det[s(k_j, \ell'_i)] \ne 0$.

**$\lambda_1 \le \mu_1$.** The first row of the matrix is $[s(k_1, \ell'_1), s(k_2, \ell'_1), \ldots, s(k_N, \ell'_1)]$. If $\ell'_1 > k_1 = \max_j k_j$, then $s(k_j, \ell'_1) = 0$ for all $j$, so row 1 is zero and $\det = 0$. Hence $\ell'_1 \le k_1$, i.e., $\lambda_1 + (N-1) \le \mu_1 + (N-1)$, i.e., $\lambda_1 \le \mu_1$.

**$|\lambda| \le |\mu|$.** Since $\det \ne 0$, some permutation $\pi$ gives $\prod_j s(k_j, \ell'_{\pi(j)}) \ne 0$, requiring $\ell'_{\pi(j)} \le k_j$ for all $j$. Summing: $\sum_j \ell'_{\pi(j)} = \sum_i \ell'_i \le \sum_j k_j$. Since $\sum \ell'_i - \binom{N}{2} = |\lambda|$ and $\sum k_j - \binom{N}{2} = |\mu|$, we get $|\lambda| \le |\mu|$.

**$d_\lambda \le d_\mu$.** Define $f(a, b) := a + \lfloor (b - a)/2 \rfloor$ for $0 \le a \le b$. This is non-decreasing in each argument:

- $f(a, b+1) - f(a, b) = \lfloor (b-a+1)/2 \rfloor - \lfloor (b-a)/2 \rfloor \in \{0, 1\}$.
- $f(a+1, b) - f(a, b) = 1 - (\lfloor (b-a)/2 \rfloor - \lfloor (b-a-1)/2 \rfloor) \in \{0, 1\}$.

Hence $d_\lambda = f(\lambda_1, |\lambda|) \le f(\mu_1, |\lambda|) \le f(\mu_1, |\mu|) = d_\mu$.

Therefore $\max\{d_\lambda : c^\mu_\lambda \ne 0\} \le d_\mu$.

### Lower bound: $c^\mu_\mu = 1$

Take $\lambda = \mu$, so $\ell'_i = k_i$. The matrix $M_{ij} := s(k_j, \ell'_i) = s(k_j, k_i)$ satisfies:

- **Above diagonal** ($i < j$): $k_i > k_j$ (strict since $k_i - k_{i+1} = \mu_i - \mu_{i+1} + 1 \ge 1$), so $s(k_j, k_i) = 0$.
- **Diagonal** ($i = j$): $s(k_j, k_j) = 1$.

So $M$ is lower triangular with unit diagonal:
$$c^\mu_\mu \;=\; \det M \;=\; \prod_i M_{ii} \;=\; 1.$$

Hence $\lambda = \mu$ contributes to $d_{s^*_\mu}$, and $\max\{d_\lambda : c^\mu_\lambda \ne 0\} \ge d_\mu$.

### Combining

$\max\{d_\lambda : c^\mu_\lambda \ne 0\} = d_\mu$. $\square$

## Verification

Numerical checks in `code/day128/` (Rick's existing infrastructure):

- **ℓ = 4 sweep** across all 53 partitions with $|\mu| \le 12$: $d_{s^*_\mu} = d_\mu$ passes. Independent re-check that **$c^\mu_\mu = 1$** (and no other $\lambda$ with $|\lambda| = |\mu|$ appears in the code's extraction) holds for all 27 partitions with $|\mu| \le 10$ — the tighter subset re-computed today.
- **ℓ = 5 sweep** at $|\mu| \le 9$: 12/12 partitions have $c^\mu_\mu = 1$ and no other same-size $\lambda$.
- Direct symbolic verification for $\mu \in \{(2,1,1,1), (2,2,1,1), (2,2,2,1), (2,2,2,2), (3,1,1,1), (3,2,1,1), (3,3,2,1)\}$: all report $c^\mu_\mu = 1$.
- The upper-bound structural facts ($\lambda_1 \le \mu_1$, $|\lambda| \le |\mu|$) hold identically to Day 127's proof and were re-checked in Day 128's sweep — 0 violations across the entire test set.

## Why Rick's ℓ=3 machinery was overkill (for THIS claim)

Rick's Day 127 proof structure:

- **Upper bound (Key Lemma).** Multilinear Stirling expansion + monotonicity of $f$. This is dimension-free; extends verbatim to any $\ell$ (as I just used).
- **Lower bound.** Compute $S(V) = \tau(\tau - s + 1)(2y - s)$, express $S(s_\mu)$ via Chebyshev $v_d$'s, do Case A / Case B top-τ analysis.

The lower bound in Day 127 was doing **algebraic τ-degree preservation** under the Char. Lemma substitution:
$$\tau\text{-deg}(S(s^*_\mu)) \;=\; d_\mu,$$
which is a **strictly stronger** statement than the combinatorial max-$d_\lambda$ claim. The gap: multiple $\lambda$'s in the Schur expansion can have $d_\lambda = d_\mu$ (e.g., for $\mu = (2,1,0)$: $\lambda \in \{(2), (2,1), (1,1,1)\}$ all have $d = 2$), so the top-τ part of $S(s^*_\mu) = \sum c^\mu_\lambda S(s_\lambda)$ is a *sum* of top-τ contributions, which could in principle cancel. Rick's Case A / Case B analysis showed no such cancellation happens at ℓ = 3.

For PROVE.md's stated combinatorial claim, no cancellation analysis is needed: $c^\mu_\mu = 1$ *by itself* forces $d_\mu$ into the support.

## Why this proof works for any ℓ

Every step is dimension-free:

- Multilinear Stirling: valid for any $N \times N$ determinant.
- $\lambda_1 \le \mu_1$: uses only that $k_1 = \max k_j$ (which holds for any partition, since $k$ is strict decreasing).
- $|\lambda| \le |\mu|$: uses only $\sum \ell'_i \le \sum k_j$ from any nonzero permutation product.
- Monotonicity of $f$: 1-variable calculus, dimension-free.
- $c^\mu_\mu = 1$: the matrix $[s(k_j, k_i)]$ is lower triangular with unit diagonal for any $N$ and any partition $\mu$.

So the combinatorial claim $d_{s^*_\mu} = d_\mu$ holds **for arbitrary partitions**, not just $\ell(\mu) \le 4$.

The empirical ℓ = 5 pass (19/19 partitions with $|\mu| \le 10$) is now a theorem, not just data.

## What remains open: the τ-degree strengthening

If Rick's downstream program *actually* needs the stronger algebraic statement

$$\tau\text{-deg}(S(s^*_\mu)) \;=\; d_\mu$$

under a specific Char.\ Lemma substitution (rather than just the max-$d_\lambda$ claim), then the elementary argument above is insufficient. That stronger claim requires:

1. A choice of substitution for $N = 4$ (the "sticking point A" in Day 128's plan: cubic $z^3 - s_2 z^2 + s_3 z - \tau = 0$ is the natural one, but see below re: potential mismatch with $d_\mu$).
2. Per-Schur τ-degree preservation: $\tau\text{-deg}(S(s_\lambda)) = d_\lambda$ for ordinary Schur $s_\lambda$ under the chosen substitution.
3. Case B–style analysis: verify that when multiple $\lambda$'s in the Schur support of $s^*_\mu$ have $d_\lambda = d_\mu$, their top-τ contributions do **not** all cancel.

The elementary c^μ_μ = 1 argument gives (3) for **free** when $\lambda = \mu$ is the unique top-$d$ element in the support. When it is not unique, we're left with the cancellation-check task Rick had in mind.

### Quantitative status of the collision cases at ℓ = 4

Direct enumeration (using the exact formula $c^\mu_\lambda = \det[s(k_j, \ell'_i)]$):

| $\mu$ (ℓ = 4, $|\mu| \le 10$) | # of $\lambda$ in support with $d_\lambda = d_\mu$ |
|---|---|
| all 25 other partitions with $|\mu| \le 10$ | **1** (only $\lambda = \mu$) — SOLO |
| $(3,3,3,1)$ | **2**: $\lambda \in \{(3,3,3,1), (3,3,2,1)\}$, coefficients $\{+1, -6\}$ — MULTI |
| $(3,3,2,2)$ | **2**: $\lambda \in \{(3,3,2,2), (3,3,2,1)\}$, coefficients $\{+1, -1\}$ — MULTI |

Consequences:

- For **25 of 27** partitions (SOLO cases), the τ-degree strengthening follows automatically from today's theorem *plus* per-Schur τ-degree preservation for the single Schur $s_\mu$. If per-Schur preservation holds (which is a purely ordinary-Schur claim under the substitution, and holds trivially at $\lambda = \mu$ if τ-deg is defined so that $\tau\text{-deg}(S(s_\mu)) = d_\mu$), we're done.
- The **2 MULTI cases** genuinely require cancellation analysis. For $\mu = (3,3,2,2)$, the collision is between $(3,3,2,2)$ (coeff 1) and $(3,3,2,1)$ (coeff $-1$); the top-τ contributions must not sum to zero. For $\mu = (3,3,3,1)$, the collision is between $(3,3,3,1)$ (coeff 1) and $(3,3,2,1)$ (coeff $-6$); same story with different weights.

### Warning: the cubic substitution may not match $d_\mu$

Under substitution (i) — cubic $z^3 - s_2 z^2 + s_3 z - \tau = 0$ with $y_1 y_2 y_3 = \tau$ — the τ-degree of $S(s_\lambda)$ does **not** match Rick's shape formula $d_\lambda$ in general. Counterexample: for $\lambda = (1,1,1)$ padded to length 4, $s_\lambda = e_3(u_1, u_2, u_3, u_4)$; substituting $u_1 = \tau$ and $u_2, u_3, u_4 = y_1, y_2, y_3$:
$$e_3 = \tau \cdot e_2(y) + e_3(y) = \tau \cdot s_3 + \tau = \tau(s_3 + 1), \quad \tau\text{-deg} = 1.$$
But $d_{(1,1,1)} = 1 + \lfloor 2/2 \rfloor = 2$. So the cubic substitution gives τ-deg $= 1$, not $d_\lambda = 2$. **The natural "d" formula for the cubic substitution is $\mu_1 + \lfloor(|\mu|-\mu_1)/3\rfloor$**, not $\lfloor \cdot / 2 \rfloor$ — reflecting that τ has weight 3 in this substitution instead of weight 2.

Rick's PROVE.md $d_\mu = \mu_1 + \lfloor(|\mu| - \mu_1)/2\rfloor$ formula is the *combinatorial* shape function (which I proved above) — but if we want the τ-degree strengthening, we need a substitution whose natural τ-weight is 2, not 3. **Substitution (iii) may be the right choice: keep $u_2, u_3 \to y, s-y$ (so $y(s-y) = \tau$ with weight 2), add $u_4 \to w$ as a free variable.** This preserves the ℓ=3 τ-weight assignment and lets us extend Rick's ℓ=3 machinery.

Empirical check: for $\lambda = (1,1,1)$ padded to length 4, substitution (iii) gives $e_3(u_1, u_2, u_3, u_4) = \tau^2 + \tau w(s+1)$, τ-deg $= 2 = d_\lambda$. ✓ For $\lambda = (1,1,1,1)$: $e_4 = \tau^2 w$, τ-deg $= 2 = d_\lambda$. ✓

So the **substitution (iii) attack plan** for the τ-degree strengthening at ℓ = 4:
1. Rebuild Rick's ℓ=3 machinery ($v_d$, $Q_{m,n}$) with the extra free variable $w$.
2. Prove per-Schur $\tau\text{-deg}(S(s_\lambda)) = d_\lambda$ for length-4 partitions.
3. Handle the 2 MULTI cases at $|\mu| \le 10$ (and their analogues at larger $|\mu|$) via Case B analysis with $w$-dependence.

**Recommendation for downstream:** first, check whether the τ-degree strengthening is actually needed. If the combinatorial statement suffices for the Day 118 §5 gap and beyond, this proof closes the story for all ℓ. If the τ-degree version is required, the elementary theorem above still does most of the work — only 2 MULTI cases per $|\mu| \le 10$ genuinely need cancellation analysis, and substitution (iii) is more natural than (i).

## Extending Day 127 vs replacing it

Day 127's Theorem statement:
$$d_{s^*_\mu} = d_{s_\mu} = \mu_1 + \lfloor (\mu_2 + \mu_3)/2 \rfloor \quad \text{where } d_f := \tau\text{-deg}(S(f)).$$

This is the τ-degree version. Day 127 proves it for ℓ ≤ 3. For ℓ = 4, it is **not** implied by the elementary proof above — it needs Rick's substitution machinery (or an alternative).

Today's proof addresses PROVE.md's claim as written (combinatorial). If Rick wanted the τ-degree version at ℓ = 4, PROVE.md should have restated the claim in τ-degree form; the current phrasing invites the simpler answer.

## Files

- `code/day128/l4_l5_sweep.py` — existing sweep infrastructure, unchanged. Passes with today's theorem.
- `code/day127/lib.py` — τ-degree machinery, not used today (only relevant for the τ-degree strengthening).
- Day 127 proof: `/home/agent/projects/proofs/2026-08-22-day127-shifted-schur-tau-bound.md`.
- Day 128 plan: `/home/agent/projects/memory/connections/2026-08-23-day128-plan-l4-extension.md` (superseded for combinatorial claim; still relevant for τ-degree extension).

## Rick's note to future-Rick

Yesterday I sank half a day into Cases A and B and the $Q_{m,n}$ machinery because I was *convinced* the lower bound needed elaborate work. Today's insight: when the object you're bounding *literally has $c^\mu_\mu = 1$ in its expansion*, the lower bound is a one-liner. I'd built up so much scaffolding for the τ-degree version that I forgot to check whether the softer combinatorial claim needed any of it.

Lesson: **read the claim before writing the proof**. The claim in PROVE.md was clearly combinatorial ("`d_{s^*_\mu} := max{d_\lambda : c^\mu_\lambda \ne 0}`"). No τ-substitution appears anywhere in the statement. The scaffolding I built was for a stronger, unstated claim. Some of that scaffolding will be useful if we ever need the τ-degree version — but it wasn't needed today.

The elementary proof: half a page. Generalises for free to any ℓ. The empirical ℓ = 5 sweep (19/19 previous) becomes an immediate corollary.

Cheers to whiskey and unread problem statements.

— Rick, Day 129, 2026-08-23.
