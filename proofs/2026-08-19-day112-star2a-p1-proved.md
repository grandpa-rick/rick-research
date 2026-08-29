---
title: Day 112 — (⋆⋆-a'')_{p=1} — Closed form + reduction, empirical PASS
status: STRUCTURALLY PROVED given closed form for $A_1$ (which is verified for $j = 1, \ldots, 15$ symbolically but not yet proved). The MECHANISM is clean.
---

# (⋆⋆-a'')_{p=1}: closed form for $A_1$ and reduction to (⋆⋆-a'')

## Statement (recap)

We want to show: for each integer $c$ sufficiently large and integer $j \geq 1$,
$$Q_j(b) \cdot A_1(b, c, j) = (b+2)_{c-3} \cdot R_1(b, c, j) \tag{$DIV\text{-}1$}$$
where
- $Q_j(b) := (b+2)_{c-1-j}$ is the rising Pochhammer $(b+2)(b+3)\cdots(b+c-j)$,
- $A_1(b, c, j) := [a^{j-1}] S_j(a, b, c)$ where $S_j = ds_j / V$ is the shifted-Schur sum,
- $R_1(b, c, j)$ is a polynomial with per-$b$-slot $j$-degree $\leq 2$.

## The mechanism (proved modulo the closed form)

### Lemma 1 (closed form for $A_1$). For every integer $j \geq 2$,
$$A_1(b, c, j) = (b+c-2)^{\underline{j-2}} \cdot P_j(b, c) \tag{$CF\text{-}1$}$$
where
$$P_j(b, c) = \frac{j}{2}\Bigl[(b+c)(2bc + 3b + 5c - 3) - j \cdot (b^2 + 4bc + c^2 - b + c)\Bigr]. \tag{$P\text{-}form$}$$

**For $j = 1$:** $A_1(b, c, 1) = bc + b + 2c$, which equals $P_1(b, c)/(b + c - 1)$ (since $P_1 = (b+c-1)(bc + b + 2c)$). The formula ($CF\text{-}1$) extends formally to $j = 1$ if one interprets $(b+c-2)^{\underline{-1}} = 1/(b+c-1)$; equivalently, at $j = 1$ the polynomial identity ($DIV\text{-}1$) still holds with $R_1 = P_1/(b+c-1)$, which is a polynomial because $(b+c-1) \mid P_1$.

**Status of Lemma 1:** Verified for $j = 1, 2, \ldots, 15$ symbolically in $(b, c)$ — see `2026-08-19-star2a-p1-Pj-fit.py` and `2026-08-19-star2a-p1-interp.py`. A structural proof is sketched below (§Proof approach), but not yet completed.

### Lemma 2 (Pochhammer factorization). For every integer $j$ with $1 \leq j \leq c-2$,
$$(b+2)_{c-1-j} \cdot (b+c-2)^{\underline{j-2}} = (b+2)_{c-3}. \tag{$POCH$}$$

*Proof.* Expand both sides as products of linear factors in $b$.

**LHS:**
$$(b+2)_{c-1-j} = (b+2)(b+3)\cdots(b+c-j).$$
This is the product over $r \in \{2, 3, \ldots, c-j\}$ of $(b+r)$.

$$(b+c-2)^{\underline{j-2}} = (b+c-2)(b+c-3)\cdots(b+c-j+1).$$
This is the product over $r \in \{c-j+1, c-j+2, \ldots, c-2\}$ of $(b+r)$.

**Concatenation:** the sets $\{2, \ldots, c-j\}$ and $\{c-j+1, \ldots, c-2\}$ are disjoint and their union is $\{2, 3, \ldots, c-2\}$. Hence
$$\text{LHS} = \prod_{r=2}^{c-2}(b+r) = (b+2)_{c-3} = \text{RHS}. \qquad \square$$

### Corollary (⋆⋆-a'')_{p=1} given Lemma 1.

Assuming ($CF\text{-}1$) and ($POCH$), substitute:
$$Q_j(b) \cdot A_1(b, c, j) = (b+2)_{c-1-j} \cdot (b+c-2)^{\underline{j-2}} \cdot P_j(b, c) = (b+2)_{c-3} \cdot P_j(b, c).$$

So $R_1(b, c, j) = P_j(b, c)$. Its $b$-degree is $\leq 2$ and its per-$b$-slot $j$-degree is $\leq 2$ **by explicit formula ($P\text{-}form$)**: the highest power of $j$ in $P_j$ is $j^2$ (in the term $-\frac{j^2}{2}(b^2 + 4bc + c^2 - b + c)$). Split by $b$-slot:

| $b$-slot | coefficient (function of $c$, $j$) | $j$-degree |
|:---:|:---|:---:|
| $b^0$ | $\frac{j}{2}[5c^2 - 3c - j(c^2 + c)] = \frac{-j^2 c^2 - j^2 c + 5jc^2 - 3jc}{2}$ | 2 |
| $b^1$ | $\frac{j}{2}[(2c^2 + 8c - 3) - j(4c - 1)] = \frac{-4j^2 c + j^2 + 2jc^2 + 8jc - 3j}{2}$ | 2 |
| $b^2$ | $\frac{j}{2}[(2c + 3) - j] = \frac{-j^2 + 2jc + 3j}{2}$ | 2 |

All $\leq 2$. QED (⋆⋆-a'')_{p=1}, modulo Lemma 1.

## Proof approach for Lemma 1

The proof of ($CF\text{-}1$) is the main remaining piece. Here is the roadmap.

Decompose $[a^{j-1}] S_j = A_1^{\text{top}} + A_1^{\text{next}}$ where
- $A_1^{\text{top}} := \sum_{\mu \in \mathcal{S}_j,\, \mu_1 = j} \kappa_\mu \cdot [a^{j-1}] s^*_\mu(a+2, b+1, c)$
- $A_1^{\text{next}} := \sum_{\mu \in \mathcal{S}_j,\, \mu_1 = j-1} \kappa_\mu \cdot [a^{j-1}] s^*_\mu(a+2, b+1, c)$

(Partitions with $\mu_1 \leq j - 2$ have $[a^{j-1}] s^*_\mu = 0$.)

### Step A: Ballot-number formula for $\kappa_\mu$ when $\mu_1 = j$.

**Sub-lemma.** For $\mu = (j, m_2, m_3) \in \mathcal{S}_j$ with $m_2 + m_3 = j$ and $m_2 \geq m_3$,
$$\kappa_\mu = \binom{j}{m_3} \cdot \frac{m_2 - m_3 + 1}{m_2 + 1}.$$

*Proof.* Every walk with $\mu_1 = j$ adds one cell to row 1 at each of the $j$ steps; the "second cell" of each vertical 2-strip goes to row 2 or row 3. Row 3 additions must not exceed row 2 additions at every prefix (else the intermediate diagram is not a valid partition). This is exactly the ballot problem: the number of sequences of $m_2$ R2-additions and $m_3$ R3-additions with the ballot constraint is the ballot number $\frac{m_2 - m_3 + 1}{m_2 + 1}\binom{m_2 + m_3}{m_3}$. $\square$

**Empirical:** matches for $j = 1, \ldots, 8$ (all $\mu$ with $\mu_1 = j$). See `2026-08-19-star2a-p1-per-mu.py`.

### Step B: Explicit shifted-Schur values.

For $\mu = (j, m_2, m_3)$, the shifted Schur $s^*_\mu(y_1, y_2, y_3)$ (with $y_1 = a+2, y_2 = b+1, y_3 = c$) is a specific determinant divided by $V$. We need $[a^{j-1}] s^*_\mu$. Since $\deg_a s^*_\mu \leq \mu_1 = j$, this is the "sub-leading" coefficient.

By Vandermonde-Weyl, $s^*_\mu = \det[(y_i)^{\underline{\mu_j + 3 - j}}] / V$, and the top-$a$ coefficient is easily extracted; the sub-leading is a specific derivative-like operation on the shifted-Schur representation.

The explicit form for $[a^{j-1}] s^*_{(j, m_2, m_3)}$ can be computed via the Jacobi-Trudi-like formula and factoring out $(y_2)^{\underline{\cdot}}(y_3)^{\underline{\cdot}}$ contributions.

### Step C: Sum over $\mu$ with ballot weights.

Assemble
$$A_1^{\text{top}} = \sum_{m_3 = 0}^{\lfloor j/2 \rfloor} \frac{m_2 - m_3 + 1}{m_2 + 1}\binom{j}{m_3} \cdot [a^{j-1}] s^*_{(j, m_2, m_3)}$$
where $m_2 = j - m_3$. This is a hypergeometric sum over $m_3$, expected to telescope to the closed form ($CF\text{-}1$) via a Chu-Vandermonde or Zeilberger-type identity.

### Step D: Sub-leading contributions from $\mu_1 = j - 1$.

For $\mu_1 = j - 1$, we have $|\mu| = 2j$ so $m_2 + m_3 = j + 1$ with $m_2 \geq m_3 \geq 1$ (row 3 must be occupied since row 1 didn't take all $j$ steps, forcing at least one 2-strip to add to rows 2 and 3 simultaneously). Explicitly: $\mu \in \{(j-1, j-1, 2), (j-1, j-2, 3), \ldots\}$.

Their contribution is smaller (empirically visible in `per-mu` output) and combines with $A_1^{\text{top}}$.

### Step E: Interpolation shortcut.

**Alternative proof by interpolation:** Both sides of ($CF\text{-}1$) are polynomials in $(b, c)$ for each fixed $j$, of $(b, c)$-total degree $j + 1$. For the identity to hold, it suffices to verify it at sufficiently many $(b, c)$ values. This gives an **effective** proof of ($CF\text{-}1$) up to any fixed $j$, but does not give a $j$-uniform proof.

**A $j$-uniform proof would need**: (i) the ballot-weighted sum in Step C, evaluated in closed form, plus (ii) the Step-D correction summed in closed form, plus (iii) match against ($CF\text{-}1$).

## Empirical verification

Script `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-verify.py` verifies (⋆⋆-a'')_{p=1}:
- Divisibility: $Q_j \cdot A_1$ is divisible by $(b+2)_{c-3}$;
- Per-$b$-slot $j$-degree of $R_1$ is $\leq 2$;

for $c \in \{6, 8, 10, 12, 15, 20\}$ and $j \in \{1, \ldots, \min(c-1, 9)\}$. **All PASS.**

Script `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-Pj-fit.py` derived the closed form ($CF\text{-}1$) for $A_1$ and verified it for $j = 2, \ldots, 10$ symbolically.

Script `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-interp.py` verified ($CF\text{-}1$) for $j = 1, \ldots, 15$ symbolically.

## What extends to general $p$?

The closed-form approach should generalize. The pattern is:

$$A_p(b, c, j) = (b+c-2p)^{\underline{j-2p}} \cdot P^{(p)}_j(b, c) \tag{$CF\text{-}p$?}$$

where $P^{(p)}_j$ is a polynomial in $(b, c, j)$ of joint $(b, c)$-degree $\leq (2p+1)$ (needed for the per-$b$-slot count $\leq 2p$ plus the $j$-dependence bounded by $2p$). Given ($CF\text{-}p$), the Pochhammer factorization
$$(b+2)_{c-1-j} \cdot (b+c-2p)^{\underline{j-2p}} = (b+2)_{c-1-2p}$$
still holds by concatenation (same argument as Lemma 2), and $R_p = P^{(p)}_j$.

**The technique for proving ($CF\text{-}p$) is the harder part.** It requires:
- A per-$\mu$ decomposition of $[a^{j-p}] S_j$ over $\mu$ with $\mu_1 \in \{j, j-1, \ldots, j-p\}$;
- Explicit weight formulas ($\kappa_\mu$) for these strata (ballot numbers generalize to $p+1$-fold Catalan-type walk counts);
- A telescoping identity summing the ballot-weighted shifted-Schur values.

**Key structural insight**: the falling-factorial prefactor $(b+c-2p)^{\underline{j-2p}}$ is EXACTLY the missing "middle" part of $(b+2)_{c-1}$ after removing $(b+2)_{c-1-j}$ from the left and $(b+2)_{c-1-2p} / (b+2)_{c-1-j-?}$ from the right — a purely arithmetic bookkeeping observation. Once ($CF\text{-}p$) is established, everything falls into place.

## Files

- Proof draft: this file.
- Verification: `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-verify.py` + `.txt`.
- Closed form derivation: `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-Pj-fit.py`.
- Per-mu analysis: `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-per-mu.py`.
- Interpolation check: `/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-interp.py`.

## Honest status

**What's proved:**
- Lemma 2 (Pochhammer factorization): fully proved.
- Corollary: (⋆⋆-a'')_{p=1} holds **provided** Lemma 1 ($CF\text{-}1$) holds.
- All ingredients cleanly verified empirically up to $j = 15$ and $c = 20$.

**The gap:** Lemma 1 ($CF\text{-}1$) is not yet proved. It is verified for $j \leq 15$ (symbolically in $b, c$). A closed-form proof requires evaluating the ballot-weighted sum of shifted-Schur sub-leading terms — this is a concrete hypergeometric identity that should yield to a Zeilberger-style algorithmic proof, but it hasn't been carried out here.

**Realistic remaining effort:**
1. Compute $[a^{j-1}] s^*_{(j, m_2, m_3)}$ explicitly (a 2-page shifted-Schur exercise).
2. Sum against ballot weights (a hypergeometric identity, feasible via Zeilberger or by matching leading terms of both sides at each $j$-monomial slot).
3. Add the $\mu_1 = j-1$ correction (analogous but shorter).

This is genuine work, but nowhere near intractable. The Day 112 (T-a) writeup can safely cite ($DIV\text{-}1$) as "proved modulo the closed-form Lemma 1, verified symbolically for $j \leq 15$."
