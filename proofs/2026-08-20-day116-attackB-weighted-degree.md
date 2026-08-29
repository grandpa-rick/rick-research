---
title: Day 116 — Attack B (weighted-degree filtration on S_j) — PARTIAL: reformulated, empirically verified, structural proof open
status: HOLDS empirically for j <= 6 in every formulation. Reformulated in the "hidden Vandermonde" (u, y, c) = (a+2, b+1, c) variables. Individual factorial Schur summands VIOLATE the bound, so a term-by-term proof is IMPOSSIBLE; the bound is a genuine sum-level cancellation identity. Structural proof strategy is open.
---

# Attack B: weighted-degree filtration on S_j — Day 116

## §1. Goal

Close atomic gap **OQ-DEG-PI-A_P-BOUND** = input (C) of the Day 115 layer-shape reduction:
$$\deg_\pi A_p(b, c, j) \leq p \qquad \text{for all } p \leq j,$$
where $A_p := [a^{j-p}] S_j$ and $S_j := ds_j / V$ (Day 109/115 setup, see below).

Attack B's proposed lever: prove the WEIGHTED-DEGREE BOUND
$$\widetilde{\deg}(S_j) \leq j$$
where $\widetilde{\deg}$ has weights $(a, \pi, \sigma) \mapsto (1, 1, 0)$. Given the bound and $\deg_a A_p = j - p$, extraction gives $\deg_\pi A_p \leq p$ automatically.

## §2. Verdict

**Attack B is EQUIVALENT to (C), not stronger. Empirical status: HOLDS for $j \leq 6$.** A structural proof was not found. However, a strong REFORMULATION was discovered (§4) which is the cleanest angle to pursue.

Verification code: `/home/agent/projects/beta-prime/code/2026-08-20-day116-attackB-verify.py` (486 lines), output `.txt` (177 lines).

## §3. Restatement of setup

Following Day 115: $u := a + 2$, and for each partition $\mu$ with $|\mu| = 2j$, $\ell(\mu) \leq 3$ appearing in the "2-strip lattice" $bt(j)$ with multiplicity $\kappa_\mu$:
$$ds_j := \sum_\mu \kappa_\mu \cdot \det\Big[\, \mathrm{fall}(x_i, \mu_{\text{col}} + (2 - \text{col})) \,\Big]_{i, \text{col} = 0}^{2}, \qquad x_i \in (u, b+1, c),$$
where $\mathrm{fall}(x, m) := x(x-1)\cdots(x-m+1)$.
$$V(a, b, c) := (a - b + 1)(a - c + 2)(b - c + 1), \qquad S_j := ds_j / V.$$
Twist symmetry (Day 109 R2): $A_p(c - 1, b + 1, j) = A_p(b, c, j)$, so $A_p \in \mathbb{Q}[\pi, \sigma]$ where $\pi := (b+1)c$, $\sigma := b+c+1$.

## §4. Key structural discovery (Day 116)

**Setting** $u := a + 2$, $y := b + 1$. Then
$$V(a, b, c) \;=\; (u - y)(u - c)(y - c),$$
the **Vandermonde** in $(u, y, c)$. Combined with $ds_j = \sum \kappa_\mu \det[\mathrm{fall}(x_i, k_j)]$ with $x = (u, y, c)$:
$$\boxed{\;S_j(a, b, c) \;=\; \sum_\mu \kappa_\mu \cdot s^*_\mu(u, y, c) \;\in\; \mathbb{Q}[u, y, c]^{S_3},\;}$$
where $s^*_\mu(x_1, x_2, x_3) := \det[\mathrm{fall}(x_i, \mu_j + 3 - j)] / \det[x_i^{3 - j}]$ is the **factorial Schur** polynomial.

**Verified computationally** for $j \leq 6$: $S_j$ is symmetric in $(u, y, c)$.

Consequently $S_j$ lies in the ring of symmetric polynomials, hence in $\mathbb{Q}[e_1, e_2, e_3]$ where $e_i$ are the elementary symmetric functions of $(u, y, c)$:
- $e_1 = u + y + c = (a + 2) + \sigma$
- $e_2 = uy + uc + yc = (a + 2)\sigma + \pi$
- $e_3 = uyc = (a + 2)\pi$

Under weights $(a, \pi, \sigma) \mapsto (1, 1, 0)$: $\widetilde{\deg}(e_1) = 1$, $\widetilde{\deg}(e_2) = 1$, $\widetilde{\deg}(e_3) = 2$.

**Structural Attack B claim (equivalent to (C)):**
$$S_j \;=\; \sum_{i_1 + i_2 + 2 i_3 \leq j} c_{i_1, i_2, i_3}(j) \, e_1^{i_1} e_2^{i_2} e_3^{i_3}. \tag{StructB}$$

**Verified computationally** for $j \leq 6$ (Step 7 of verify script).

## §5. Why Attack B ≡ (C), not stronger

Writing $S_j = \sum_p a^{j-p} A_p(b, c)$ with $A_p \in \mathbb{Q}[\pi, \sigma]$:
$$\widetilde{\deg}(S_j) = \max_p \Big( (j - p) \cdot 1 + \widetilde{\deg}_{(\pi, \sigma) \to (1, 0)}(A_p) \Big) = \max_p (j - p + \deg_\pi A_p).$$
So $\widetilde{\deg}(S_j) \leq j$ iff $\deg_\pi A_p \leq p$ for all $p$. The two claims carry exactly the same information.

**Consequence:** Attack B does NOT reduce (C) to a genuinely different fact. It re-frames (C) in a way that MAKES the symmetric structure visible — but the algebraic content is identical.

## §6. Why term-by-term fails

The obvious hope — each $s^*_\mu$ individually satisfies wdeg $\leq j$ — is FALSE. Verified in Step 8:

| $j$ | $\mu$ | $\kappa_\mu$ | e-wdeg of $s^*_\mu$ | target $\leq$ |
|---|---|---|---|---|
| 2 | (2,2,0) | 1 | **3** | 2 |
| 2 | (2,1,1) | 1 | **3** | 2 |
| 3 | (3,3,0) | 1 | **4** | 3 |
| 3 | (3,2,1) | 2 | **4** | 3 |
| 3 | (2,2,2) | 1 | **4** | 3 |

Individual factorial Schur summands overshoot the bound. The claim (StructB) holds only for the specific $\kappa_\mu$-weighted SUM — it is a genuine algebraic cancellation identity.

**This kills a simple term-by-term proof of Attack B / (C).** Any successful proof must use a global property of the sum, likely tied to how $\kappa_\mu$ arises from the 2-strip lattice.

## §7. What (StructB) buys and open directions

The reformulation is real progress — it identifies $S_j$ as a symmetric polynomial in $(u, y, c)$, a much cleaner algebraic object than the mixed $(a, b, c)$ picture. Directions:

1. **Recursion.** $bt(j)$ recurses via adding a horizontal 2-strip. If a recursion $S_{j+1} = \Delta_{j+1}(S_j)$ can be identified where $\Delta_{j+1}$ preserves the weighting up to shift, induction on $j$ closes it. Requires understanding the 2-strip operator on symmetric polynomials.

2. **Character-theoretic / Pieri.** $\kappa_\mu$ is (empirically) the number of length-$j$ paths in the Young lattice via horizontal 2-strips landing at shape $\mu$. This is the coefficient of $s_\mu$ in $h_2^j$ (complete homogeneous $h_2$ to the $j$). So
$$\sum_\mu \kappa_\mu s_\mu(u, y, c) = h_2(u, y, c)^j.$$
   Verifying this identity numerically is a natural next test. If it lifts to factorial Schur functions — $\sum_\mu \kappa_\mu s^*_\mu(u, y, c) \overset{?}{=} h_2^*(u, y, c)^j$ or some closely related factorial expression — the wdeg bound becomes visible from $h_2$'s structure.

3. **Generating function.** Compute $\sum_j S_j t^j$ and hope for a closed form (e.g., a determinant of size $2 \times 2$).

## §8. Postmortem — what worked, what didn't

- **Worked:** Identifying the hidden Vandermonde structure $V = (u - y)(u - c)(y - c)$. This unlocks $S_j$'s symmetry in $(u, y, c)$ and reframes everything into the symmetric-function world where more tools are available.
- **Worked:** Recognizing that Attack B and (C) are logically equivalent — this saves future time avoiding wrong "Attack B is stronger" reasoning.
- **Didn't work:** No term-by-term proof (§6); no closed form emerged in the elementary-symmetric coefficient tables.
- **Next-move recommendation:** Pursue direction (2) above (Pieri / $h_2^j$ identity for $\kappa_\mu$) as a fresh Day-117 attack, OR pivot to a completely different route:
  - **Attack 4 (recursion on $j$):** derive $S_{j+1}$ from $S_j$ directly.
  - **Attack 3 (dimension count on Grassmannian / character):** if $A_p$ has a representation-theoretic origin, its $\pi$-degree may be a Weyl-dimension shift.
  - **Direct interpolation:** since we know $A_p$ vanishes at all $(b, c) = (\mu_1, \mu_2)$ partition points with $|\mu| < j$, use a partition-point Vandermonde argument on $\deg_\pi$ (mirroring the Day 115 divisibility proof).

## §9. Files

- `/home/agent/projects/beta-prime/code/2026-08-20-day116-attackB-verify.py` — 486 lines, verifies:
  - $\widetilde{\deg}(S_j) \leq j$ under $(a, \pi, \sigma) \to (1, 1, 0)$ for $j \leq 6$.
  - $S_j$ symmetric in $(u, y, c)$ for $j \leq 6$.
  - $S_j$ expansion in $(e_1, e_2, e_3)$ satisfies $i_1 + i_2 + 2 i_3 \leq j$ for $j \leq 6$.
  - Individual $s^*_\mu$ VIOLATES the wdeg bound (multiple counterexamples).
- `/home/agent/projects/beta-prime/code/2026-08-20-day116-attackB-verify.txt` — 177 lines of output.

## §10. Bottom line

Attack B — as stated — is not a NEW route to (C); it is a reformulation. But the reformulation is **valuable**: it exposes $S_j$'s hidden $S_3$-symmetry in $(a + 2, b + 1, c)$, moving the entire question into the ring of symmetric polynomials. Future work should exploit this symmetry rather than treat (C) as a bare $(b, c)$-polynomial claim.

**Status:** Attack B **partially closes (C)** — reformulation banked, structural proof deferred, empirical evidence extended and refined. **Not shippable as a proof of the atomic gap.**
