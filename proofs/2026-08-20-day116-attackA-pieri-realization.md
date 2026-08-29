---
title: Day 116 -- Attack A (Pieri realization for A_p): POSTMORTEM (F)
status: FAILED. The naive Pieri identity A_p = h^*_p . A_0 is FALSE at p = 1 (and every higher p). Numerical differences are large and grow with j. Postmortem below documents what was tried, what the closest attainable statement is, and pivots to Attacks 2/4.
---

# Attack A postmortem — Day 116 (2026-08-20)

## Claim tested

**Attack A (naive form):** In the Okounkov-Olshanski shifted-Schur Hopf algebra $\Lambda^*(y_2, y_3)$,
$$A_p \;=\; h^*_p \cdot A_0, \qquad A_0 = (b + c)^{\underline j}, \qquad h^*_p = s^*_{(p, 0)}(b, c). \tag{Attack A}$$
If true, since $\deg_\pi h^*_p = \lfloor p/2 \rfloor \le p$ and $\deg_\pi A_0 = 0$, we would get $\deg_\pi A_p \le p$ (closing OQ-DEG-PI-A_P-BOUND).

## Verification setup

Code: `beta-prime/code/2026-08-20-day116-attackA-pieri-verify.py` (352 lines).
Range: $p \in \{1, 2, 3, 4\}$, $j \in \{1, \ldots, 10\}$. Fully symbolic sympy verification. All computations pass sanity: (i) $A_0(b, c, j) = (b+c)^{\underline j}$ (verified for $j \le 10$), (ii) $A_p$ extraction matches Day 114 machinery.

## §1. Main negative result

**Attack A fails at $p = 1$.** For every $j \ge 1$:
$$A_1(b, c, j) - h^*_1(b, c) \cdot A_0(b, c, j) \;\ne\; 0.$$

Sample failures at $p = 1$:

| $j$ | $A_1 - h^*_1 A_0$ (shifted-Schur difference; nonzero coefficients) |
|-----|--------------------------------------------------------------------|
| 1   | $-1 \cdot s^*_{(2,0)}$                                             |
| 2   | $-s^*_{(1,1)} - s^*_{(2,0)} - s^*_{(3,0)}$                        |
| 4   | $-12 s^*_{(2,2)} - 18 s^*_{(3,1)} - 6 s^*_{(4,0)} + 3 s^*_{(3,2)} - s^*_{(5,0)}$ |
| 6   | $-75 s^*_{(3,3)} - 135 s^*_{(4,2)} - 75 s^*_{(5,1)} - 15 s^*_{(6,0)} + 16 s^*_{(4,3)} + 10 s^*_{(5,2)} - s^*_{(7,0)}$ |

The differences involve nearly every $\lambda$ in the support of $A_p$, with growing integer coefficients. No sign of an error-term structure that would make Attack A "almost true modulo a small correction."

**Falsification is decisive:** if a naive multiplicative Pieri identity fails at $p = 1$, we quit and pivot (per Rick's rule).

## §2. What the closest attainable statement is

### 2.1 $A_p$ is NOT divisible by $A_0$

Test: divide $A_p$ by $A_0 = (b+c)^{\underline j}$ in $\mathbb{Q}[b, c]$. **Nonzero remainder** for every $(p, j)$ with $p \ge 1$ (verified $p \in \{1, \ldots, 4\}$, $j \in \{p, \ldots, 10\}$). So even "$A_p = P \cdot A_0$ for some poly $P$" is false.

### 2.2 The Layer-Shape divisor is $\Pi_{p, j}$, not $A_0$

$$\Pi_{p, j} := \prod_{t = 2p+1}^{j} (\sigma - t), \qquad A_0 = \prod_{t = 1}^{j}(\sigma - t).$$
$A_0$ carries $j$ linear $\sigma$-factors; $\Pi_{p, j}$ carries only $j - 2p$. So $A_0 = \Pi_{p, j} \cdot \prod_{t = 1}^{2p}(\sigma - t)$. The extra $2p$ factors *do not* divide $A_p$ (for $p \ge 1$, verified by division). So the Layer-Shape divisor is genuinely $\Pi_{p, j}$, not $A_0$.

### 2.3 What IS true (empirically): $Q_p := A_p / \Pi_{p, j}$ has $\deg_\pi Q_p = p$ EXACTLY

Verified $p \in \{1, 2, 3, 4\}$, $j \in \{2p, \ldots, 8\}$: $\deg_\pi(A_p / \Pi_{p, j}) = p$ and $\deg_\sigma(A_p / \Pi_{p, j}) = 2p$. This is exactly the (C) + (D2), (D3) content of the Layer-Shape lemma, empirically confirmed.

So the *statement* to prove is right; the *proposed proof route* (Attack A) is wrong.

### 2.4 Why Attack A was appealing but wrong

Seed data (Day 114 pieri-hunt4): at $|\lambda| = j$ level, for even $j = 2k, m = 2i$,
$$c^{\text{seed}}_{(k+i, k-i)}(A_p, j = 2k) = R_p(k, i) \cdot T(2k, k-i)$$
with $T$ the ballot triangle = Sahi-Stanley Pieri multiplicity for square partitions. This *suggested* a Pieri form.

**But**: the factors $R_p(k, i)$ do NOT match any Pieri-multiplicity for $s^*_{\lambda_0} \cdot h^*_p$. Rick's Day 114 fits give:

- $R_1(k, i) = -k(2k - 3)$ (independent of $i$).
- $R_2(k, i) = i^2 + i + A_2(k)$ where $A_2 = -7, 13, 134, 480, 1223$ at $k = 2, 3, 4, 5, 6$ — a *degree-5 polynomial in $k$*.
- $R_3(k, i)$: bivariate polynomial with $\deg_k = 4$; does not factor.
- $R_4(k, i)$: bivariate polynomial with $\deg_k = 4$ and $\deg_i = 4$; does not factor.

If Attack A held, $R_p(k, i)$ would be a Pieri weight — a rational function of small binomials in $(k, i)$. Instead they are **degree-4-in-$k$ polynomials with irregular coefficients**. This alone (before any $h^*_p \cdot A_0$ comparison) is a red flag against Attack A.

### 2.5 The Pieri decomposition ACTUALLY has variable coefficients

Ansatz-check performed: does $A_p$ lie in $\text{span}\{h^*_r \cdot A_0 : 0 \le r \le p\}$ over $\mathbb{Q}$? The seed data alone kills this: at $|\lambda| = j$, we would need the *only* contribution to be $r = 0$ (since $h^*_r$ raises $|\lambda|$ by $r$), forcing $A_0 = A_p$. False.

The extended ansatz $A_p = \sum_r c_r(j) \cdot h^*_r \cdot \Pi_{p, j} \cdot (\text{factor})$? This is essentially the Layer-Shape statement re-decorated. Doesn't add new leverage.

## §3. What the correct "shape" of a proof should look like

**Genuine cancellation is required.** In the shifted-Schur expansion $A_p = \sum_\lambda c_\lambda(j, p) s^*_\lambda$, individual $s^*_\lambda$ has $\deg_\pi = \lfloor |\lambda| / 2 \rfloor$ (verified for $\lambda \in \{(p, q) : 0 \le q \le p \le 5\}$). For $|\lambda| \sim j$ this gives $\deg_\pi \sim j/2 \gg p$. The observed $\deg_\pi A_p = p$ means the individual $\pi$-degree-$\lfloor|\lambda|/2\rfloor$ terms across $\lambda$ MUST cancel down to degree $p$.

This cancellation cannot be seen from any one $\lambda$; it's an integrated statement across the whole shifted-Schur expansion. Attack A tried to bypass this by expressing $A_p$ as a *single* structured object whose $\deg_\pi$ is bounded. That failed because no single Pieri-type product carries the right coefficients.

## §4. Pivot recommendation

The remaining Attacks (from Rick's Day 115 workplan) reordered by promise:

**(Attack 5) Direct joint-degree bound on $S_j$ [most promising].** Claim (C') from Day 115 §8: $S_j(a, b, c)$ has weighted degree $\le j$ under the grading $\widetilde{\deg}(a^\alpha \pi^\beta \sigma^\gamma) = \alpha + \beta$. This is a statement directly about $S_j = ds_j / V$ and the walk ensemble $\mathcal{S}_j$. Reduction sketch is already in the Day 115 layer-shape reduction. Would need to show: the walk-ensemble determinantal form has $(a, \pi)$-weight $\le j$. This is a *combinatorial* statement about $\mathcal{S}_j$, which Rick has extensive machinery for.

**(Attack 4) Vandermonde deformation.** Since $A_p = [a^{j-p}] S_j$ and $S_j$'s $a$-degree is $j$, one may hope that specializing $a \to$ some clever value transports the $\pi$-degree bound. E.g., specialize $a = b + c - t$ for suitable $t$, killing the $a$-dependence and reducing to a pure $(b, c)$-statement. Rick's Day 108-113 work has $a$-specializations that worked.

**(Attack 6) Coalgebra / comultiplication.** The shifted-Schur ring $\Lambda^*$ has a comultiplication $\Delta$. If $\Delta A_p$ has a controlled expression in $\Delta h^*_p$, one could derive $\pi$-degree bounds coalgebraically. But this is heavier machinery and Attack A already invoked (and failed) the algebra structure; the coalgebra is unlikely to be easier.

**(Attack 2) Direct polynomial identity via ds_j / V restriction.** $A_p$ is a specific extraction from $ds_j$. Compute $\deg_{y_2 y_3}$-part-restricted-by-$\pi$ directly on the determinantal expansion. Concretely: in the walk-ensemble expansion of $ds_j$, control how many $\pi$-factors can arise per term.

**Strongest single recommendation:** **pursue Attack 5 (joint-degree bound on $S_j$)**. It is the most direct restatement of the target, exploits the walk-ensemble structure Rick has fluency with, and does not require any Pieri machinery.

## §5. Files created

- `beta-prime/code/2026-08-20-day116-attackA-pieri-verify.py` (352 lines) — Attack A verification code.
- `beta-prime/code/2026-08-20-day116-attackA-pieri-verify.txt` (585 lines) — full transcript.
- `proofs/2026-08-20-day116-attackA-pieri-realization.md` (this file).

## §6. Coordinates for Rick

- Layer-Shape lemma (Day 115) status unchanged: PROVED conditional on (A), (B), (C).
- (A), (B) still routine.
- (C) still open. Attack A does NOT close it. Attack A was a plausible but wrong route.
- The Layer-Shape reduction and its use of (C) are UNAFFECTED — this postmortem doesn't touch any other proof.

## §7. Meta

Rick's rule: "If it doesn't work at $p = 2$, quit and pivot." Attack A doesn't even work at $p = 1$. Quit.

Negative results are shippable. Attack A was worth trying because the seed-level Sahi-Stanley Pieri match was *strongly* suggestive. The lesson: the Pieri match at the *seed* level is a coincidence, not a structural identity — the higher $|\lambda|$-levels don't extend it.

The layer-shape lemma will close, but not this way.

— Day 116, morning, sober coffee.
