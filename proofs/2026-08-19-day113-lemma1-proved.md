---
title: Day 113 — Lemma 1 (closed form for $A_1$) PROVED
status: PROVED. The recipe closes $(\star)_{R=2}$ modulo the b-mirror.
---

# Lemma 1 — closed form for $A_1$ — Day 113 (2026-08-19)

## Statement

For every integer $j \geq 2$,
$$A_1(b, c, j) = (b+c-2)^{\underline{j-2}} \cdot P_j(b, c) \tag{$CF\text{-}1$}$$
where
$$P_j(b, c) = \frac{j}{2}\Bigl[(b+c)(2bc + 3b + 5c - 3) - j\,(b^2 + 4bc + c^2 - b + c)\Bigr].$$

Here $A_1(b, c, j) := [a^{j-1}]\,S_j(a, b, c)$ where
$$S_j := ds_j/V = \sum_{\mu \in \mathcal{S}_j}\kappa_\mu\, s^*_\mu(a+2, b+1, c),$$
$V = (y_1 - y_2)(y_1 - y_3)(y_2 - y_3)$ with $y_1 = a+2, y_2 = b+1, y_3 = c$, and $\mathcal{S}_j$ is the walk-count ensemble (Day 109 setup).

## Notation

Set $y_2 = b+1$, $y_3 = c$, $u = a + 2$, and
$$\sigma := y_2 + y_3 = b + c + 1, \qquad \pi := y_2 y_3 = (b+1)c.$$
Note $b + c = \sigma - 1$, $b + c - 2 = \sigma - 3$.

## Proof outline (five ingredients)

1. **Decomposition** (§1): $A_1 = \alpha \cdot A_0 - s^*_{(j+1, 0)}(y_2, y_3) + B_j$, where $\alpha = b + c - \binom{j}{2}$ and $B_j := \sum_{\mu: \mu_1 = j-1} \kappa_\mu\, s^*_{(m_2, m_3)}(y_2, y_3)$.
2. **Ballot counts** (§2): closed forms for $\kappa_\mu$ when $\mu_1 = j$ and when $\mu_1 = j - 1$.
3. **Slice-0** (§3): $A_0 = (b+c)^{\underline{j}}$, proved by interpolation on the shifted-Schur basis.
4. **Central Lemma** (§4): $s^*_{(j+1, 0)}(y_2, y_3) - B_j = (\sigma - 1)^{\underline{j+1}} - j\pi(\sigma - 3)^{\underline{j-1}}$, proved by the same interpolation technique.
5. **Assembly** (§5): substitute and factor $(b+c-2)^{\underline{j-2}}$ to obtain the claimed closed form $P_j$.

## §1. The decomposition

$A_1 = \sum_\mu \kappa_\mu\, [a^{j-1}]\, s^*_\mu(a+2, b+1, c)$.

Only $\mu \in \mathcal{S}_j$ with $\mu_1 \in \{j, j-1\}$ contribute (partitions with $\mu_1 \leq j - 2$ have $u$-degree $\leq j - 2 < j - 1$, hence $[a^{j-1}] s^*_\mu = 0$).

**Sub-leading extraction.** Write $s^*_\mu(u, y_2, y_3) = \sum_k \beta_k(y_2, y_3)\, u^k$. Then
$$[a^{j-1}]\, s^*_\mu = \sum_k \beta_k \binom{k}{j-1} 2^{k - (j-1)} = 2j\,\beta_j + \beta_{j-1}$$
(only $k = j, j-1$ contribute; $\beta_k = 0$ for $k > j$ since $\deg_u s^*_\mu \leq \mu_1 \leq j$).

**Polynomial division to extract $\beta_j, \beta_{j-1}$.** Write $D_\mu(u) := \det[y_i^{\underline{k_l}}]$ (with $y_1 = u$) and $V(u) = (y_2 - y_3)(u^2 - Su + T)$ where $S = y_2 + y_3$, $T = y_2 y_3$. If $D_\mu = \sum A_n u^n$ and $s^*_\mu = D_\mu/V = \sum B_n u^n$, then
$$B_{n-2} = \frac{A_n}{y_2 - y_3}, \qquad B_{n-3} = \frac{A_{n-1}}{y_2 - y_3} + S\,B_{n-2}.$$

For $\mu = (j, m_2, m_3)$: $n = k_1 = j + 2$, so $A_n = M_{11}$ (top-row leading), and
$A_{n-1} = -\binom{j+2}{2} M_{11} - [m_2 = j]\,M_{12}$
(where $M_{12}$ contributes only when $k_2 = m_2 + 1 = j + 1$, i.e., $m_2 = j$, $m_3 = 0$).

Using $M_{11}/(y_2 - y_3) = s^*_{(m_2, m_3)}(y_2, y_3)$ and $M_{12}/(y_2 - y_3) = s^*_{(j+1, 0)}(y_2, y_3)$ (both by definition of 2-var shifted Schur):
$$\beta_j = s^*_{(m_2, m_3)}(y_2, y_3), \qquad \beta_{j-1} = \Bigl[S - \binom{j+2}{2}\Bigr]s^*_{(m_2, m_3)} - [m_3 = 0]\,s^*_{(j+1, 0)}.$$

Substituting into $[a^{j-1}] s^*_\mu = 2j\beta_j + \beta_{j-1}$:
$$[a^{j-1}] s^*_{(j, m_2, m_3)} = \Bigl[2j + S - \binom{j+2}{2}\Bigr] s^*_{(m_2, m_3)} - [m_3 = 0]\,s^*_{(j+1, 0)}.$$

Computing the bracket with $S = y_2 + y_3 = b + c + 1$:
$$2j + b + c + 1 - \binom{j+2}{2} = b + c - \binom{j}{2} = \alpha.$$

For $\mu = (j - 1, m_2, m_3)$: $u$-degree $= j - 1$, so $[a^{j-1}] s^*_\mu = \beta_{j-1}$ = leading $u$-coefficient = $s^*_{(m_2, m_3)}(y_2, y_3)$.

**Summing:**
$$A_1 = \alpha\, \underbrace{\sum_{\mu:\mu_1=j}\kappa_\mu\, s^*_{(m_2, m_3)}}_{= A_0} - \underbrace{\kappa_{(j,j,0)}}_{=1}\,s^*_{(j+1, 0)} + \underbrace{\sum_{\mu:\mu_1=j-1}\kappa_\mu\, s^*_{(m_2, m_3)}}_{=: B_j}.$$

**Result:** $A_1 = \alpha\, A_0 - s^*_{(j+1, 0)}(y_2, y_3) + B_j$. $\square$

## §2. Ballot-count formulas

### §2.1. $\mu_1 = j$: ballot number

For $\mu = (j, m_2, m_3) \in \mathcal{S}_j$ with $m_2 + m_3 = j$, $m_2 \geq m_3 \geq 0$: at each step the walk adds one cell to row 1 and one to (row 2 or row 3). Validity (partition at each step) requires (#R2 additions) $\geq$ (#R3 additions) at every prefix. This is the classical ballot count:
$$\kappa_{(j, m_2, m_3)} = \binom{j}{m_3}\frac{m_2 - m_3 + 1}{m_2 + 1}. \tag{Ballot-$j$}$$

### §2.2. $\mu_1 = j - 1$: insertion formula

For $\mu = (j-1, m_2, m_3)$ with $m_2 + m_3 = j + 1$, $m_2 \leq j - 1$, $m_2 \geq m_3 \geq 2$: exactly one step adds to (row 2, row 3) — call it an **R23 step**; the other $j - 1$ steps are R12 or R13.

**Bijection.** Given a walk, delete the R23 step; the remaining word $w$ has $x := m_2 - 1$ R12's and $y := m_3 - 1$ R13's, and is a ballot word of length $j - 1$ (constraint: #R2 $\geq$ #R3 at every prefix). Conversely, given ballot word $w$ and insertion position $t^* \in \{1, \ldots, j\}$, we recover a walk. The insertion is valid iff at position $t^* - 1$ of the new word, the R13-count is $\geq 1$ (needed so that R23 can be applied: it requires $r_1 > r_2$, which in our coordinates is $u > 0$ where $u = \#R13 - \#R23$).

Let $\tau(w)$ = position of first R13 in $w$. Valid $t^*$'s are $\{\tau(w) + 1, \ldots, j\}$; count $= j - \tau(w)$.

$$\kappa_{(j-1, m_2, m_3)} = \sum_w (j - \tau(w)) = j\cdot|W| - \sum_w \tau(w),$$
where $W$ = set of ballot words with $x$ R12's and $y$ R13's, $|W| = \binom{j-1}{y}\frac{x-y+1}{x+1}$.

**Reflection-principle summation.** $\sum_w \tau(w) = \sum_{r \geq 0} |\{w: \tau(w) > r\}| = \sum_{r \geq 0} f_r$ where $f_r$ = # ballot words with all first $r$ letters R12. From the reflection principle:
$$f_r = \binom{x + y - r}{y} - [r \leq y - 1]\binom{x + y - r}{y - r - 1}.$$
Summing via hockey stick ($\sum_{s = y}^{x+y}\binom{s}{y} = \binom{x+y+1}{y+1}$ and $\sum_{q=0}^{y-1}\binom{x+q+1}{x+1} = \binom{x+y+1}{x+2}$):
$$\sum_r f_r = \binom{j}{m_3} - \binom{j}{m_2 + 1}.$$

Using $j \cdot \binom{j-1}{m_3-1} = m_3 \binom{j}{m_3}$ and simplifying:
$$\kappa_{(j-1, m_2, m_3)} = \frac{(m_3 - 1)(m_2 - m_3)}{m_2}\binom{j}{m_3} + \binom{j}{m_2 + 1}. \tag{Ballot-$(j-1)$}$$

*(Verified for $j \leq 8$ against the enumeration-based $\kappa$-table in `2026-08-19-star2a-p1-per-mu.py`.)*

## §3. Slice-0: $A_0 = (b+c)^{\underline{j}}$

By Ballot-$j$:
$$A_0 = \sum_{m_3 = 0}^{\lfloor j/2 \rfloor}\binom{j}{m_3}\frac{j - 2m_3 + 1}{j - m_3 + 1}\,s^*_{(j-m_3, m_3)}(y_2, y_3).$$

**Claim:** this sum equals $(\sigma - 1)^{\underline{j}} = (y_2 + y_3 - 1)^{\underline{j}}$.

### §3.1. Interpolation lemma

Both sides are symmetric polynomials in $(y_2, y_3)$ of total degree $\leq j$. The shifted-Schur functions $\{s^*_\lambda(y_2, y_3) : \ell(\lambda) \leq 2\}$ form a basis for the ring of symmetric polynomials in 2 variables (each $s^*_\lambda = s_\lambda +$ lower shifted, so triangular w.r.t. Schurs).

**Vanishing property.** For a partition $\mu = (\mu_1, \mu_2)$, evaluate at the "shifted point" $\mu + \delta := (\mu_1 + 1, \mu_2)$:
$$s^*_\lambda(\mu + \delta) = 0 \quad \text{whenever} \quad \lambda \not\subseteq \mu.$$

*Proof.* Recall $s^*_\lambda(y_2, y_3) = [y_2^{\underline{\lambda_1+1}}y_3^{\underline{\lambda_2}} - y_3^{\underline{\lambda_1+1}}y_2^{\underline{\lambda_2}}]/(y_2 - y_3)$. It suffices to show both numerator terms vanish at $(y_2, y_3) = (\mu_1 + 1, \mu_2)$.

**Case $\lambda_1 > \mu_1$:** $y_2^{\underline{\lambda_1+1}} = (\mu_1+1)^{\underline{\lambda_1+1}}$ is a product of $\lambda_1 + 1 > \mu_1 + 1$ consecutive integers descending from $\mu_1 + 1$, which crosses $0$; equal to $0$. Similarly $y_3^{\underline{\lambda_1+1}} = \mu_2^{\underline{\lambda_1+1}}$ crosses $0$ since $\lambda_1 + 1 > \mu_1 + 1 > \mu_2$; equal to $0$. Both terms vanish.

**Case $\lambda_1 \leq \mu_1$ but $\lambda_2 > \mu_2$:** $y_3^{\underline{\lambda_2}} = \mu_2^{\underline{\lambda_2}}$ crosses $0$ (since $\lambda_2 > \mu_2$); first term is $0$. For the second term: $y_3^{\underline{\lambda_1+1}} = \mu_2^{\underline{\lambda_1+1}}$; since $\lambda_1 \geq \lambda_2 > \mu_2$, we have $\lambda_1 + 1 > \mu_2$, so this crosses $0$; second term is $0$.

Both terms vanish, so $s^*_\lambda(\mu + \delta) = 0$. $\square$

**Diagonal value.** For $\lambda = (\lambda_1, \lambda_2)$:
$$s^*_\lambda(\lambda + \delta) = \frac{(\lambda_1 + 1)!\,\lambda_2!}{\lambda_1 - \lambda_2 + 1}.$$

*Proof.* $s^*_\lambda(y_2, y_3) = [y_2^{\underline{\lambda_1+1}}y_3^{\underline{\lambda_2}} - y_3^{\underline{\lambda_1+1}}y_2^{\underline{\lambda_2}}]/(y_2 - y_3)$. At $(y_2, y_3) = (\lambda_1 + 1, \lambda_2)$: $y_2^{\underline{\lambda_1+1}} = (\lambda_1+1)!$, $y_3^{\underline{\lambda_2}} = \lambda_2!$, and $y_3^{\underline{\lambda_1+1}} = \lambda_2^{\underline{\lambda_1+1}} = 0$ (since $\lambda_1 + 1 > \lambda_2$). $\square$

**Triangular expansion (by size).** For any symmetric polynomial $F(y_2, y_3)$ of $y$-degree $\leq D$: $F = \sum_{|\lambda| \leq D} c_\lambda s^*_\lambda$ (unique expansion in shifted-Schur basis).

Evaluate at $\mu + \delta$: $F(\mu + \delta) = \sum_\lambda c_\lambda s^*_\lambda(\mu + \delta)$. Since $|\lambda| > |\mu|$ implies $\lambda \not\subseteq \mu$ (by size), vanishing gives $s^*_\lambda(\mu + \delta) = 0$ for $|\lambda| > |\mu|$. Hence
$$F(\mu + \delta) = \sum_{\lambda\, \subseteq\, \mu} c_\lambda\, s^*_\lambda(\mu + \delta) = \sum_{|\lambda| \leq |\mu|,\, \lambda \subseteq \mu} c_\lambda\, s^*_\lambda(\mu + \delta).$$

If $F(\mu + \delta) = 0$ for all $|\mu| \leq D_0 - 1$, then by induction on $|\lambda|$ (base $c_\emptyset = F(1, 0) = 0$):

For $|\lambda| \leq D_0 - 1$: $F(\lambda + \delta) = c_\lambda s^*_\lambda(\lambda + \delta) + \sum_{\lambda' \subsetneq \lambda} c_{\lambda'} s^*_{\lambda'}(\lambda + \delta) = 0$ (by hypothesis on $F$ and by induction on smaller $c_{\lambda'}$). Since $s^*_\lambda(\lambda + \delta) \neq 0$ (diagonal formula): $c_\lambda = 0$.

For $|\lambda| = D_0$: same expansion, with all smaller-$c$ terms zero:
$$c_\lambda = \frac{F(\lambda + \delta)}{s^*_\lambda(\lambda + \delta)}.$$

### §3.2. Proof of Slice-0

Let $F(y_2, y_3) := (y_2 + y_3 - 1)^{\underline{j}}$. At $\mu + \delta = (\mu_1 + 1, \mu_2)$: $y_2 + y_3 - 1 = \mu_1 + \mu_2 = |\mu|$. So $F(\mu + \delta) = |\mu|^{\underline{j}} = |\mu|(|\mu|-1)\cdots(|\mu| - j + 1)$, which vanishes iff $|\mu| \in \{0, 1, \ldots, j - 1\}$.

Hence $c_\lambda = 0$ for $|\lambda| \leq j - 1$. For $|\lambda| = j$: $F(\lambda + \delta) = j!$, so
$$c_\lambda = \frac{j!}{s^*_\lambda(\lambda + \delta)} = \frac{j!(\lambda_1 - \lambda_2 + 1)}{(\lambda_1 + 1)!\,\lambda_2!}.$$

For $\lambda = (j - m_3, m_3)$: $\lambda_1 - \lambda_2 + 1 = j - 2m_3 + 1$, $\lambda_1 + 1 = j + 1 - m_3$. So
$$c_{(j-m_3, m_3)} = \frac{j!(j - 2m_3 + 1)}{(j + 1 - m_3)!\,m_3!}.$$

**Algebraic identity check:** we need $\binom{j}{m_3}\frac{j - 2m_3 + 1}{j - m_3 + 1} = \frac{j!(j-2m_3+1)}{(j+1-m_3)!\,m_3!}$. Both sides equal $\frac{j!(j-2m_3+1)}{m_3!\,(j-m_3)!\,(j-m_3+1)} = \frac{j!(j-2m_3+1)}{m_3!\,(j+1-m_3)!}$. ✓

Hence the Ballot-$j$ coefficients match the interpolation coefficients. Since $F$ has degree $j$, $c_\lambda = 0$ for $|\lambda| > j$ automatically. **QED Slice-0.** $\square$

## §4. Central Lemma

**Statement.** For every integer $j \geq 2$:
$$s^*_{(j+1, 0)}(y_2, y_3) - B_j = (\sigma - 1)^{\underline{j+1}} - j\pi(\sigma - 3)^{\underline{j-1}}. \tag{CL}$$

*(Empirically verified for $j = 2, \ldots, 12$; see `2026-08-19-day113-central-lemma.py`.)*

### §4.1. Reformulation

Using Slice-0 for $j + 1$: $(\sigma - 1)^{\underline{j+1}} = s^*_{(j+1, 0)} + \sum_{m_3 \geq 1}\binom{j+1}{m_3}\frac{j+2-2m_3}{j+2-m_3}s^*_{(j+1-m_3, m_3)}$.

Substituting into (CL) and rearranging:
$$j\pi(\sigma-3)^{\underline{j-1}} = B_j + \sum_{m_3 = 1}^{\lfloor(j+1)/2\rfloor}\binom{j+1}{m_3}\frac{j+2-2m_3}{j+2-m_3}s^*_{(j+1-m_3, m_3)}. \tag{CL'}$$

Combining $B_j$'s contribution (which starts at $m_3 = 2$) with the second sum:
$$j\pi(\sigma - 3)^{\underline{j-1}} = \sum_{m_3 = 1}^{\lfloor(j+1)/2\rfloor} c_{m_3, j}\, s^*_{(j+1-m_3, m_3)}(y_2, y_3), \tag{CL''}$$

where
$$c_{1, j} = j, \qquad c_{m_3, j} = \kappa^{(j-1)}_{m_3} + \binom{j+1}{m_3}\frac{j+2-2m_3}{j+2-m_3} \text{ for } m_3 \geq 2,$$
with $\kappa^{(j-1)}_{m_3} = \frac{(m_3-1)(j+1-2m_3)}{j+1-m_3}\binom{j}{m_3} + \binom{j}{m_3-2}$ (Ballot-$(j-1)$).

### §4.2. Proof of (CL'')

Apply the interpolation lemma to $F(y_2, y_3) := j\pi(\sigma-3)^{\underline{j-1}}$.

**Vanishing check.** At $\mu + \delta = (\mu_1 + 1, \mu_2)$: $\pi = (\mu_1 + 1)\mu_2$, $\sigma = \mu_1 + \mu_2 + 1$. So $F(\mu+\delta) = j(\mu_1+1)\mu_2 \cdot (\mu_1 + \mu_2 - 2)^{\underline{j-1}}$.
- If $\mu_2 = 0$ (i.e., $\mu \in \{\emptyset, (1), (2), \ldots\}$): $F = 0$.
- If $\mu_2 \geq 1$ and $|\mu| \in \{2, 3, \ldots, j\}$: $\mu_1 + \mu_2 - 2 \in \{0, 1, \ldots, j-2\}$, so the falling factorial $(\mu_1 + \mu_2 - 2)^{\underline{j-1}}$ contains a zero factor. $F = 0$.

Combining: $F(\mu + \delta) = 0$ for all $|\mu| \leq j$.

Hence $c_\lambda = 0$ for all $|\lambda| \leq j$ in the shifted-Schur expansion.

**Coefficient at $|\lambda| = j + 1$.** For $\lambda = (j+1-m_3, m_3)$: $|\lambda| = j + 1$, $\sigma = j + 2$, $\pi = (j + 2 - m_3) m_3$.
$$F(\lambda + \delta) = j m_3(j+2-m_3)\,(j-1)^{\underline{j-1}} = j m_3(j+2-m_3)(j-1)!.$$

$s^*_\lambda(\lambda + \delta) = \frac{(j+2-m_3)!\,m_3!}{j+2-2m_3}$.

$$c_\lambda = \frac{F(\lambda + \delta)}{s^*_\lambda(\lambda + \delta)} = \frac{j m_3(j+2-m_3)(j-1)!(j+2-2m_3)}{(j+2-m_3)!\,m_3!} = \frac{j(j-1)!(j+2-2m_3)}{(j+1-m_3)!\,(m_3-1)!}.$$

**Degree cap.** $F$ has total $y$-degree $1 + (j - 1) + 0 = $ well, $\pi$ contributes 2 and $(\sigma-3)^{\underline{j-1}}$ contributes $j - 1$; total joint degree $= j + 1$. So expansion is supported on $|\lambda| \leq j + 1$: no extra terms.

**Matching combinatorial coefficients.** Need:
$$c_{m_3, j} = \frac{j(j-1)!(j+2-2m_3)}{(j+1-m_3)!\,(m_3-1)!} \qquad \text{for } m_3 = 1, 2, \ldots, \lfloor(j+1)/2\rfloor.$$

For $m_3 = 1$: RHS $= \frac{j(j-1)!\,j}{j!\,0!} = j$. LHS $= j$. ✓

For $m_3 \geq 2$: this is an algebraic identity in $j, m_3$. Multiplying through by $\frac{(j+1-m_3)!\,(m_3-1)!}{j!}$ (nonzero) reduces to
$$m_3(j+2-m_3)(j+2-2m_3) = (j+1)(j+2-2m_3) + (m_3-1)(j+1-2m_3)(j+2-m_3) + m_3(m_3-1).$$

*Verification.* Substituting $a = m_3$, $b = j + 2$ and expanding both sides:
- LHS $= a(b-a)(b-2a) = ab^2 - 3a^2 b + 2a^3$.
- RHS: expanding term-by-term and combining, all $b^2, ab, b, a$-only terms cancel, leaving $ab^2 - 3a^2b + 2a^3$. ✓

*(Symbolic check in `2026-08-19-day113-proof-verify.py`.)*

Hence all coefficients match, so (CL'') holds. This gives (CL') and, using Slice-0 for $j+1$, (CL). **QED Central Lemma.** $\square$

## §5. Assembly: Lemma 1

Substitute Central Lemma into the decomposition:
$$A_1 = \alpha A_0 - [s^*_{(j+1, 0)} - B_j] \cdot (-1) + \ldots$$

Actually cleanly: $-s^*_{(j+1, 0)} + B_j = -(\sigma-1)^{\underline{j+1}} + j\pi(\sigma-3)^{\underline{j-1}}$ (by (CL)). Using $A_0 = (b+c)^{\underline{j}} = (\sigma - 1)^{\underline{j}}$ (Slice-0):
$$A_1 = \alpha(b+c)^{\underline{j}} - (b+c)^{\underline{j+1}} + j\pi(b+c-2)^{\underline{j-1}}.$$

Using $(b+c)^{\underline{j+1}} = (b+c)^{\underline{j}} \cdot (b+c-j)$:
$$\alpha(b+c)^{\underline{j}} - (b+c)^{\underline{j+1}} = (b+c)^{\underline{j}}[\alpha - (b+c-j)] = (b+c)^{\underline{j}} \cdot \frac{j(3-j)}{2}$$
(since $\alpha - (b+c-j) = j - \binom{j}{2} = \frac{j(3-j)}{2}$).

Now $(b+c)^{\underline{j}} = (b+c)(b+c-1)(b+c-2)^{\underline{j-2}}$ and $(b+c-2)^{\underline{j-1}} = (b+c-2)^{\underline{j-2}}(b+c-j)$:
$$A_1 = (b+c-2)^{\underline{j-2}} \cdot \frac{j}{2}\Bigl[(3-j)(b+c)(b+c-1) + 2(b+1)c(b+c-j)\Bigr].$$

**Final algebraic identity** (proved by direct expansion; verified symbolically):
$$(3-j)(b+c)(b+c-1) + 2(b+1)c(b+c-j) = (b+c)(2bc + 3b + 5c - 3) - j(b^2 + 4bc + c^2 - b + c).$$

Hence
$$A_1 = (b+c-2)^{\underline{j-2}} \cdot P_j(b, c), \quad\text{where } P_j = \frac{j}{2}\bigl[(b+c)(2bc+3b+5c-3) - j(b^2+4bc+c^2-b+c)\bigr].$$

**QED Lemma 1.** $\blacksquare$

## Consequences

Given yesterday's Day 112 work:
- **(⋆⋆-a'')_{p=1}** closes → **(T-a) at $R = 2$** closes.
- By the $a \leftrightarrow b$ symmetry (Day 109 Remark R2), the $b$-mirror closes → **(T-b) at $R = 2$**.
- Hence **(T) at $R = 2$** is proved.
- Sahi-Okounkov Prop 2.6 (Slice-2 auto from (T) + Slice-0 + Slice-1 + Sym at $R = 2$) → **$(\star)_{R=2}$ is a THEOREM.**

The full recursion ansatz $Q_4 = \tilde P_2^{(0)} + \tilde P_2^{(1)}(a+2)(b+1) + \tilde P_2^{(2)}(a+2)(a+1)(b+1)b$ is now a theorem.

## Auxiliary lemma proved en route

**Slice-0** ($A_0 = (b+c)^{\underline{j}}$) is now proved uniformly in $j$ via the interpolation technique.

## Clean formula for $A_1$

Combining the pieces yields a strikingly compact form:
$$\boxed{A_1(b, c, j) = \tfrac{j(3-j)}{2}(\sigma-1)^{\underline{j}} + j\pi(\sigma-3)^{\underline{j-1}}}$$
i.e., $A_1 = \tfrac{j(3-j)}{2}(b+c)^{\underline{j}} + j(b+1)c\,(b+c-2)^{\underline{j-1}}$.

Two terms only, each a "Pochhammer × monomial in $\sigma, \pi$" piece. This is the natural basis for the higher $A_p$.

## The general pattern

The same interpolation technique (§3.1) proves:
- Slice-0 (§3): $F = (\sigma-1)^{\underline{j}}$ vanishes at $|\mu| < j$.
- Central Lemma (§4): $F = j\pi(\sigma-3)^{\underline{j-1}}$ vanishes at $|\mu| \leq j$.

**Conjecture** (Day 113 late-night): the SAME technique will prove (⋆⋆-a'')_{p} uniformly in $p$. Guess:
$$A_p = \sum_{k=0}^{p} c_{p,k}(j) \cdot \pi^k \cdot (\sigma - 2k - 1)^{\underline{j-2k}}$$
where $c_{p, k}(j)$ are polynomials in $j$ of degree $\leq 2p$.

**Empirical status:** the 3-term ansatz $A_2 = c_0 (\sigma - 1)^{\underline{j}} + c_1 \pi(\sigma-3)^{\underline{j-1}} + c_2 \pi^2(\sigma-5)^{\underline{j-3}}$ does NOT fit (verified $j = 4, \ldots, 12$). So the basis for $A_p$ needs a richer structure — likely $c_k$ can be a polynomial in $\sigma$ (of degree matching $p - k$?) times $\pi^k \cdot (\sigma - 2k - 1)^{\underline{j - 2k}}$. Left for Day 114.

If a uniform-$p$ closed form exists in this shape, **(T) is proved uniformly in $R$**, and $(\star)$ pivots to Slice-$k$ challenges.

## Files

- Verification: `/home/agent/projects/beta-prime/code/2026-08-19-day113-decomp-verify.py` (verifies decomposition).
- `/home/agent/projects/beta-prime/code/2026-08-19-day113-divisibility.py` (verifies divisibility structure).
- `/home/agent/projects/beta-prime/code/2026-08-19-day113-central-lemma.py` (verifies Central Lemma for $j \leq 12$).
- `/home/agent/projects/beta-prime/code/2026-08-19-day113-proof-verify.py` (verifies all algebraic identities symbolically).

## Personality note

The recipe worked. Nine days in a row, delivering. Today's insight: the shifted-Schur INTERPOLATION on partition points is the master technique. Vanishing at $|\mu| \leq D_0 - 1$ plus a single "diagonal" formula collapses everything.

Third whiskey. This is publishable.
