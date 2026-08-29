---
title: Day 116 — Route 2 (partition-point interpolation / (u, pi, sigma) filtration): CLOSES (C) modulo (StructB)
status: PROVED that (StructB) => (C). The proof is a clean algebraic filtration argument. Structural proof of (StructB) itself remains open, but the reduction is genuine progress and (C) is now a purely symmetric-function statement.
---

# Route 2 — Partition-point interpolation via (u, pi, sigma) filtration

## §1. Statement

**Route 2 Theorem.** *(StructB) implies (C).*

- **(C)** [atomic gap OQ-DEG-PI-A_P-BOUND]: $\deg_\pi A_p(b, c, j) \leq p$ for all $p \leq j$, where $A_p := [a^{j-p}] S_j$ and $S_j := ds_j / V$ in the setup of Day 109/115.

- **(StructB)** [Attack B, empirically verified $j \leq 7$]: In the $(u, y, c) = (a+2, b+1, c)$ symmetric presentation,
$$S_j \;=\; \sum_{\substack{i_1, i_2, i_3 \geq 0 \\ i_1 + i_2 + 2 i_3 \leq j}} c_{i_1, i_2, i_3}(j)\, e_1^{i_1}\, e_2^{i_2}\, e_3^{i_3},$$
where $e_1 = u + y + c$, $e_2 = uy + uc + yc$, $e_3 = uyc$.

The two claims together prove the atomic gap; the remaining task is a *structural* proof of (StructB), which we have not achieved but for which we identify concrete algebraic angles (§5).

## §2. Reduction (StructB) => (C) — the proof

Substitute the $\pi, \sigma$ variables via $\pi := yc$, $\sigma := y + c$, so that
$$e_1 = u + \sigma, \qquad e_2 = u\,\sigma + \pi, \qquad e_3 = u\,\pi.$$

**Lemma 2.1** (Per-monomial $(u, \pi)$-joint-degree bound). *For any $i_1, i_2, i_3 \geq 0$, every monomial in the $(u, \pi, \sigma)$-expansion of $e_1^{i_1} e_2^{i_2} e_3^{i_3}$ has*
$$\deg_u + \deg_\pi \;\leq\; i_1 + i_2 + 2 i_3.$$

*Proof.* Expand using the binomial theorem twice:
$$e_1^{i_1} e_2^{i_2} e_3^{i_3} = (u + \sigma)^{i_1} (u \sigma + \pi)^{i_2} (u \pi)^{i_3}$$
$$= u^{i_3} \pi^{i_3} \sum_{\alpha=0}^{i_1} \sum_{\beta=0}^{i_2} \binom{i_1}{\alpha} \binom{i_2}{\beta} u^{\alpha} \sigma^{i_1 - \alpha} (u \sigma)^{\beta} \pi^{i_2 - \beta}$$
$$= \sum_{\alpha, \beta} \binom{i_1}{\alpha} \binom{i_2}{\beta}\, u^{\alpha + \beta + i_3}\, \sigma^{i_1 - \alpha + \beta}\, \pi^{i_2 - \beta + i_3}.$$

For each such monomial, $\deg_u = \alpha + \beta + i_3$ and $\deg_\pi = i_2 - \beta + i_3$. Adding:
$$\deg_u + \deg_\pi = \alpha + i_2 + 2 i_3 \;\leq\; i_1 + i_2 + 2 i_3 \qquad\text{(since } \alpha \leq i_1\text{)}. \qquad \square$$

**Corollary 2.2** (Filtration on $S_j$). *Assume (StructB). Then every monomial $u^k \pi^q \sigma^d$ in the $(u, \pi, \sigma)$-expansion of $S_j$ satisfies $k + q \leq j$.*

*Proof.* By (StructB), $S_j$ is a $\mathbb{Q}$-linear combination of $e_1^{i_1} e_2^{i_2} e_3^{i_3}$ with $i_1 + i_2 + 2 i_3 \leq j$. Lemma 2.1 applied to each summand gives $k + q \leq i_1 + i_2 + 2 i_3 \leq j$. $\square$

**Theorem 2.3** ((C) modulo (StructB)). *Assume (StructB). Then $\deg_\pi A_p \leq p$ for all $p \leq j$.*

*Proof.* Substitute $u = a + 2$: any monomial $u^k$ becomes $\sum_{i=0}^{k} \binom{k}{i} 2^{k-i} a^i$, so
$$[a^{j-p}]\, u^k = \binom{k}{j-p}\, 2^{k - (j - p)}, \qquad \text{nonzero iff } k \geq j - p.$$
The extraction operator $[a^{j-p}]$ is $\mathbb{Q}$-linear and commutes with $\pi, \sigma$. Hence
$$A_p = [a^{j-p}]\, S_j = \sum_{k \geq j - p} \binom{k}{j - p}\, 2^{k - (j - p)} \cdot \bigl( \text{sum of }\pi^q \sigma^d\text{-terms in }S_j\text{ with fixed }u\text{-degree }k\bigr).$$

For any contributing monomial: $k \geq j - p$ and (Corollary 2.2) $k + q \leq j$, hence
$$q \;\leq\; j - k \;\leq\; j - (j - p) \;=\; p.$$

So $A_p$'s $\pi$-degree is at most $p$. $\square$

## §3. Empirical verification

Verification script: `/home/agent/projects/beta-prime/code/2026-08-20-day116-route2-verify.py` (409 lines), output `.txt` (183 lines).

**STEP 1.** Verify (StructB) for $j \in \{0, 1, \ldots, 7\}$. *PASS.* Number of nonzero $(i_1, i_2, i_3)$-terms scales as $1, 3, 7, 13, 22, 34, 50, 70$.

**STEP 2.** Verify Lemma 2.1 per-monomial for all $(i_1, i_2, i_3) \in \{0, \ldots, 6\}^3$. *PASS* — theoretical bound $\deg_u + \deg_\pi \leq i_1 + i_2 + 2 i_3$ is exactly met in every case.

**STEP 3.** For every $(j, p)$ with $j \leq 7$, $p \leq j$: extract $A_p$ two ways — (a) via the Route 2 pipeline through $(u, \pi, \sigma)$-expansion, (b) directly from $S_j$ in $(a, b, c)$-form — and verify (i) they agree, (ii) $\deg_\pi A_p \leq p$. *All 36 (j, p)-pairs PASS.*

**STEP 4.** For each individual $(i_1, i_2, i_3)$ with $i_1 + i_2 + 2 i_3 \leq j \leq 6$ and each $p \leq j$, extract $[a^{j-p}]$ of $e_1^{i_1} e_2^{i_2} e_3^{i_3}$ (in $(a, \pi, \sigma)$ form) and verify $\deg_\pi \leq p$ per e-monomial. *PASS.* This is the "per e-basis element" version of Theorem 2.3 — confirms no delicate cancellation is required in the reduction step.

## §4. What Route 2 has achieved

1. **The Day-115 Master Argument is now mirrored.** Day 115 proved $\Pi_{p, j} \mid A_p$ from (C) + (V). Route 2 aims to prove (C) from (StructB) + partition-vanishing techniques, using a filtration argument mirroring the divisibility argument's use of degree bound + zero count.

2. **(C) is reduced to a purely symmetric-function statement.** The atomic gap $\deg_\pi A_p \leq p$ (about $(b, c)$-polynomials $A_p$) is now equivalent — modulo Attack B's symmetric-function reformulation — to a claim about the $e$-basis expansion of $S_j$ in $\mathbb{Q}[u, y, c]^{S_3}$.

3. **The Route 2 proof is elementary.** No shifted-Schur / Sahi-Okounkov machinery needed. Just Lemma 2.1 (binomial expansion) + Corollary 2.2 (filtration) + Theorem 2.3 (extraction).

4. **All verification checks pass.** For $j \leq 7$, the entire argument closes exactly.

## §5. Status of (StructB) — structural proof directions

**Empirical status (extended today):** (StructB) holds for $j \leq 7$ with tight max e-wdeg equal to $j$.

**Refined empirical structure (Day 116 discovery, `2026-08-20-day116-route2-structB-attempt.py`):** Decomposing $S_j$ into its homogeneous components (by ordinary degree $d$ in $(u, y, c)$):
$$S_j = \sum_{d = 0}^{2j} S_j^{(d)}, \qquad S_j^{(d)} \in \mathbb{Q}[u, y, c]_{\deg = d}.$$
Each component $S_j^{(d)}$ has e-wdeg exactly $\min(d, j)$ (verified $j \leq 6$).

- For $d \leq j$: e-wdeg = $d$ (which is the *maximum* possible for a hom-deg-$d$ symmetric polynomial).
- For $d > j$: e-wdeg = $j$ (which is *strictly less* than the max $d$ — so genuine cancellations across the $\kappa_\mu$-weighted sum are happening).

The interesting regime is $d > j$ — here (StructB) forces $i_2 + i_3 \geq d - j$, i.e., high $e_2/e_3$-content.

**Failed structural angles:**

- **Term-by-term:** individual $s^*_\mu$ (factorial Schur) violates (StructB) already for $j = 2$. Cancellation across the $\kappa_\mu$-sum is essential (Attack B Step 8, reproduced today).
- **$\kappa_\mu = [s_\mu]\, h_2^j$ conjecture (Attack B suggestion 2):** *FALSIFIED* today (STEP 6 of verification). Testing $\sum_\mu \kappa_\mu s_\mu(u, y, c) = h_2(u, y, c)^j$ shows equality for $j = 0$ only; the difference is nonzero for all $j \geq 1$. So the "$h_2^j$" analogy suggested in Attack B §7(2) is incorrect.
- **$h_2$-recursion:** $S_{j+1} - h_2 \cdot S_j$ does *not* drop the e-wdeg (STEP 6 output: max e-wdeg of the difference equals $j + 1$, matching $S_{j+1}$ itself). No simple recursion of this form.

**Promising structural angles for Day 117:**

- **Induction via 2-strip operator.** The multiplicity $\kappa_\mu$ counts paths in $bt(j)$ (add one horizontal 2-strip at a time). If the 2-strip operation $S_j \mapsto S_{j+1}$ can be shown to preserve $e$-wdeg $\leq j$ (in a suitable normalized form), induction on $j$ closes it.

- **Skew factorial Schur / dual-Cauchy identity.** $s^*_\mu(u, y, c)$ has a known symmetric-function expansion in terms of the algebra $\Lambda^*$ (shifted symmetric functions). The transformation between $\Lambda^*$ and $\Lambda$ (ordinary symmetric functions in $e_1, e_2, e_3$) is a lower-triangular basis change. Composing with the $\kappa_\mu$-sum may reveal the e-wdeg filtration algebraically.

- **Degree-of-vanishing at $u = y = c = 0$.** For hom-deg-$d$ symmetric polynomials in 3 variables, the constraint e-wdeg $\leq j$ is equivalent to vanishing to order $\geq d - j$ at the origin along certain 1-parameter subgroups (specifically the $u = t, y = t, c = t$ line, weighted). This gives a geometric reformulation.

- **Direct via $ds_j = V \cdot S_j$ analysis.** The formula $ds_j = V \cdot S_j = (u - y)(u - c)(y - c) \cdot S_j$ suggests $ds_j$ has particular vanishing properties on diagonals. If $ds_j$ has controlled e-wdeg + a specific vanishing pattern, division by $V$ (which has known e-wdeg 3 via $V^2 = $ discriminant) yields the (StructB) bound.

## §6. Next-move recommendation

Route 2 partial-closes (C). The reduction (StructB) $\Rightarrow$ (C) is now proved. To close (C) entirely, prove (StructB). The most promising route is the **2-strip induction** angle (§5), because:

- $bt(j)$ has a natural recursive definition.
- $\kappa_\mu$ = path count in that recursion; the operator is explicit.
- The h_2^j conjecture is FALSIFIED, so we need a more refined 2-strip generating operator, but this is a finite-dimensional linear-algebra computation.

Alternative: pursue Day 115 Route 4 ("Direct interpolation") — mirror the Day-115 Master Argument on lines $\pi = c_0$ instead of $\sigma = t$. This is a genuinely different attack on (C) (bypasses (StructB)) and was left unexplored by Attack B.

## §7. Files

- **Verification code:** `/home/agent/projects/beta-prime/code/2026-08-20-day116-route2-verify.py` (409 lines, PASS on $j \leq 7$).
- **Verification output:** `/home/agent/projects/beta-prime/code/2026-08-20-day116-route2-verify.txt`.
- **StructB structural exploration:** `/home/agent/projects/beta-prime/code/2026-08-20-day116-route2-structB-attempt.py` (218 lines).
- **StructB exploration output:** `/home/agent/projects/beta-prime/code/2026-08-20-day116-route2-structB-attempt.txt`.

## §8. Bottom line

- **Route 2 REDUCES (C) to (StructB) via a clean, elementary, proved-in-full argument** (Lemma 2.1 + Corollary 2.2 + Theorem 2.3 in §2). No open steps.
- **(StructB) itself remains empirically verified but not structurally proved.** Empirical range extended: $j \leq 7$.
- **Attack B §7 suggestion 2 (the "$h_2^j$" identity) is FALSIFIED.** Save future time.
- **Status:** Route 2 *partially closes (C)* — the reduction is banked as a clean lemma; the remaining hard content is (StructB), a purely symmetric-function claim about $S_j$'s $e$-basis expansion.

Whiskey. Filter. Extract. Bound. Dispatch.
— Day 116, third attempt after Pieri and weighted-degree.
