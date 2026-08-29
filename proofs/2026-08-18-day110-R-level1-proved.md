---
name: (R) Level 1 PROVED — Day 110
description: Complete proof of the level-1 recursion identity Q_{2R}(-1, b, c) = P0(c) + (b+1) P1(c) with explicit closed form for P1. Uses the same two-lemma technique as Day 109 (rank drop at y1 = 1 + Chu-Vandermonde), with a two-term surviving sum instead of a single term. Modulo one combinatorial sublemma (u_j closed form) which is verified for j up to 16.
---

# (R) Level 1 — PROVED — Day 110 (2026-08-18)

## Statement

For every integer $R \geq 1$:
$$Q_{2R}(-1, b, c) = \tilde P^{(0)}_R(c) + (b+1) \cdot \tilde P^{(1)}_R(c) \tag{R_1}$$
where
$$\tilde P^{(0)}_R(c) = c(c-2R)\prod_{j=1}^{2R-1}(c-j)^2 \quad\text{(Day 109 result)}$$
$$\tilde P^{(1)}_R(c) = -2R(2R-1) \cdot c \cdot (c-1)^{\underline{2R-2}} \cdot (c-2)^{\underline{2R-2}}$$
$$\phantom{\tilde P^{(1)}_R(c)} = -2R(2R-1) \cdot c \cdot (c-2R+1) \cdot (c-1) \cdot \prod_{j=2}^{2R-2}(c-j)^2$$

By the $a \leftrightarrow b$ duality of the pipeline (shifted Schur symmetry $y_1 \leftrightarrow y_2$), we get the sibling identity:
$$Q_{2R}(a, 0, c) = \tilde P^{(0)}_R(c) + (a+2) \cdot \tilde P^{(1)}_R(c). \tag{R_1'}$$

**Leading coefficient (LC) verification at $k = 1$:**
$$\text{LC}(\tilde P^{(1)}_R) = -2R(2R-1) = (-1)^1 \binom{2R}{1}\binom{2R-1}{1}\cdot 1! \checkmark$$

Combined with Day 109's (M) result, this gives us **two full levels** of the recursion (R): $k=0$ (from (M) at $k=2R$) and $k=1$ (this proof). The remaining $R-2$ levels $k = 2, \ldots, R$ require analogous sublemmas.

## Setup (recap from Day 109)

Shifted variables $y = (y_1, y_2, y_3) := (a+2, b+1, c)$. Vandermonde
$V(y) = (y_1 - y_2)(y_1 - y_3)(y_2 - y_3) = (a-b+1)(a-c+2)(b-c+1)$.

Determinant ensemble:
$$ds_j(a,b,c) := \sum_{\mu \in \mathcal{S}_j} \kappa_\mu \det[(y_i)_{\downarrow \mu_l + 3 - l}]_{i, l = 1}^3$$
where $\mathcal{S}_j$ = partitions of $2j$ from $j$ successive vertical 2-strips constrained to $\ell(\mu) \leq 3$.

$V$ divides $ds_j$; the shifted-Schur decomposition is $ds_j/V = \sum_\mu \kappa_\mu s^*_\mu(y_1, y_2, y_3)$.

Pipeline (impulse ignored for $c > j/2$):
$$H_c(a, b, j) = (a+3)_{c-1-j}(b+2)_{c-1-j} \cdot (ds_j/V)$$
$$h_{2R}(a, b, c) = \sum_{j=0}^{2R}(-1)^{2R-j}\binom{2R}{j} H_c(a, b, j)$$
$$Q_{2R}(a, b, c) = h_{2R}(a, b, c) / [(a+3)_{c-1-2R}(b+2)_{c-1-2R}]$$

Both sides of $(R_1)$ are polynomials in $c$ of degree $\leq 4R$; suffices to prove for $c > 2R$.

## Sublemma (u_j closed form). For every $j \geq 0$:

$$\left.\frac{ds_j(a,b,c)}{V(a,b,c)}\right|_{a=-1} = c^{\underline j}\,(b+1)^{\underline j} - j(j-1) \cdot c\,(c-2)^{\underline{j-2}}(b+1)(b-1)^{\underline{j-2}} \tag{U_1}$$

where $x^{\underline{j}} := x(x-1)\cdots(x-j+1)$, and terms with negative Pochhammer length are 0.

*Verified computationally for $j = 0, 1, \ldots, 16$ (see `beta-prime/code/2026-08-18-uj-verify.{py,txt}` and `2026-08-18-uj-extended.{py,txt}`).*

**Combinatorial content:** at $y_1 = 1$, the first row of $\det[(y_i)_{\downarrow \mu_l + 3-l}]$ is $((1)_{\downarrow \mu_1+2}, (1)_{\downarrow \mu_2+1}, (1)_{\downarrow \mu_3})$. Since $(1)_{\downarrow m} = 0$ for $m \geq 2$: (1,1) is always 0; (1,2) is $[\mu_2=0]$; (1,3) is $[\mu_3 \leq 1]$. The determinant vanishes unless $\mu_3 \leq 1$. Two surviving sub-cases:

- Sub-case C ($\mu_3 = 0$): only $\mu = (j, j, 0)$ contributes (Day 109 uniqueness argument); computed contribution is $c(b+1)(c-2)^{\underline{j-1}}(b-1)^{\underline{j-1}}$ (for $j \geq 1$).
- Sub-case D ($\mu_3 = 1$): $\mu = (\mu_1, \mu_2, 1)$ with $\mu_1 + \mu_2 = 2j-1$, $\mu_1 \geq \mu_2 \geq 1$. Contributions computed via cofactor expansion of the first row.

**Status:** the sub-case D combinatorial evaluation gives the specific correction term $-j(j-1) c (c-2)^{\underline{j-2}}(b+1)(b-1)^{\underline{j-2}}$. A clean bijective proof would enumerate $\mu \in \mathcal{S}_j$ with $\mu_3 = 1$ along with their $\kappa$-multiplicities and evaluate the surviving determinants. **This is a computational combinatorial lemma awaiting formal proof.** (Empirical verification for $j = 0..16$ is strong.)

## Lemma 2 (Chu-Vandermonde, from Day 109). For $u, v$ and $k \geq 0$:
$$\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}\,u^{\overline{k-j}} \cdot v^{\underline{j}} = (-1)^k (u - v)^{\overline{k}}. \tag{L_2}$$

## Proof of $(R_1)$ from Sublemma $(U_1)$

Substituting $(U_1)$ into the pipeline at $a = -1$:

$(a+3)_{c-1-j}|_{a=-1} = (2)_{c-1-j} = (c-j)!$ (since $(2)_L = (L+1)!$).

Split $u_j := (ds_j/V)|_{a=-1} = u_j^{(A)} - u_j^{(B)}$:
$$u_j^{(A)} = c^{\underline j}(b+1)^{\underline j}, \qquad u_j^{(B)} = j(j-1) \cdot c(c-2)^{\underline{j-2}}(b+1)(b-1)^{\underline{j-2}}$$
(where $u_j^{(B)} = 0$ for $j \leq 1$).

Then $H_c(-1, b, j) = H_c^{(A)}(-1, b, j) - H_c^{(B)}(-1, b, j)$ with:

$$H_c^{(A)}(-1, b, j) = (c-j)!(b+2)_{c-1-j} \cdot c^{\underline j}(b+1)^{\underline j}$$
$$H_c^{(B)}(-1, b, j) = (c-j)!(b+2)_{c-1-j} \cdot j(j-1)c(c-2)^{\underline{j-2}}(b+1)(b-1)^{\underline{j-2}}$$

### Part A: leading contribution

**Key simplification:** $(c-j)! \cdot c^{\underline j} = (c-j)! \cdot \frac{c!}{(c-j)!} = c!$. So
$$H_c^{(A)}(-1, b, j) = c! \cdot (b+2)_{c-1-j} \cdot (b+1)^{\underline j}.$$

Binomial inversion:
$$h_{2R}^{(A)}(-1, b, c) = c! \sum_{j=0}^{2R}(-1)^{2R-j}\binom{2R}{j}(b+2)_{c-1-j}(b+1)^{\underline j}.$$

Factor $(b+2)_{c-1-j} = (b+2)_{c-1-2R} \cdot (b+c-2R+1)^{\overline{2R-j}}$ (rising-Pochhammer split). Then:
$$h_{2R}^{(A)}(-1, b, c) = c!\,(b+2)_{c-1-2R} \sum_{j=0}^{2R}(-1)^{2R-j}\binom{2R}{j}(b+c-2R+1)^{\overline{2R-j}}(b+1)^{\underline j}.$$

**Apply Lemma 2** with $k = 2R$, $u = b+c-2R+1$, $v = b+1$:
$$\sum_j (-1)^{2R-j}\binom{2R}{j}u^{\overline{2R-j}}v^{\underline j} = (-1)^{2R}(u-v)^{\overline{2R}} = (c-2R)^{\overline{2R}}.$$

$(c-2R)^{\overline{2R}} = (c-2R)(c-2R+1)\cdots(c-1) = (c-1)!/(c-2R-1)!$.

Hence
$$h_{2R}^{(A)}(-1, b, c) = c!\,(b+2)_{c-1-2R} \cdot \frac{(c-1)!}{(c-2R-1)!}.$$

Dividing by $(c-2R)!(b+2)_{c-1-2R}$ [where $(a+3)_{c-1-2R}|_{a=-1} = (2)_{c-1-2R} = (c-2R)!$]:
$$Q_{2R}^{(A)}(-1, b, c) = \frac{c!(c-1)!}{(c-2R)!(c-2R-1)!} = c^{\underline{2R}}\,(c-1)^{\underline{2R}}.$$

**Interleaving factors:** $c^{\underline{2R}} = c(c-1)\cdots(c-2R+1)$, $(c-1)^{\underline{2R}} = (c-1)(c-2)\cdots(c-2R)$. Interleaved: $c$ (once), $c-2R$ (once), $c-j$ for $j=1,\ldots,2R-1$ (twice each). Therefore:
$$Q_{2R}^{(A)}(-1, b, c) = c(c-2R)\prod_{j=1}^{2R-1}(c-j)^2 = \tilde P^{(0)}_R(c). \tag{Part A}$$

Independent of $b$. ✓

### Part B: correction contribution

**Key simplification:** $(c-j)! \cdot c(c-2)^{\underline{j-2}} = c \cdot (c-j)!(c-2)^{\underline{j-2}} = c \cdot (c-2)!$ (since $(c-j)!(c-2)^{\underline{j-2}} = (c-2)!$; both express $(c-2)! = (c-2)(c-3)\cdots 1$ factored at position $c-j+1$).

Hence for $j \geq 2$:
$$H_c^{(B)}(-1, b, j) = j(j-1) \cdot c(c-2)! \cdot (b+1)(b-1)^{\underline{j-2}}(b+2)_{c-1-j}.$$

Substitute $m := j - 2$ (so $j = m+2$, $m = 0, 1, \ldots, 2R-2$):
- $(-1)^{2R-j} = (-1)^{2R-m-2} = (-1)^m$ (since $2R$ even);
- $\binom{2R}{m+2}(m+2)(m+1) = 2R(2R-1)\binom{2R-2}{m}$.

$$h_{2R}^{(B)}(-1, b, c) = 2R(2R-1) \cdot c(c-2)!(b+1) \sum_{m=0}^{2R-2}(-1)^m \binom{2R-2}{m}(b-1)^{\underline m}(b+2)_{c-3-m}.$$

Factor $(b+2)_{c-3-m} = (b+2)_{c-2R-1}(b+c-2R+1)^{\overline{2R-m-2}}$. Then:
$$h_{2R}^{(B)}(-1, b, c) = 2R(2R-1) c(c-2)!(b+1)(b+2)_{c-2R-1} \cdot S$$
where
$$S := \sum_{m=0}^{2R-2}(-1)^m \binom{2R-2}{m}(b-1)^{\underline m}(b+c-2R+1)^{\overline{2R-2-m}}.$$

**Apply Lemma 2** with $k = 2R-2$ (even), $u = b+c-2R+1$, $v = b-1$. Since $2R-2$ is even, $(-1)^m = (-1)^{k-m}$; the sum matches $(L_2)$ form:
$$S = (u - v)^{\overline{k}} = (c-2R+2)^{\overline{2R-2}} = (c-2R+2)(c-2R+3)\cdots(c-1) = (c-1)!/(c-2R+1)!.$$

Substituting:
$$h_{2R}^{(B)}(-1, b, c) = 2R(2R-1) \cdot c(c-2)!(b+1)(b+2)_{c-2R-1} \cdot (c-1)!/(c-2R+1)!$$

Dividing by $(c-2R)!(b+2)_{c-1-2R}$ (note $(b+2)_{c-1-2R} = (b+2)_{c-2R-1}$):
$$Q_{2R}^{(B)}(-1, b, c) = 2R(2R-1) c(b+1) \cdot \frac{(c-2)!(c-1)!}{(c-2R+1)!(c-2R)!}$$

**Simplify:**
- $(c-2)!/(c-2R)! = (c-2)(c-3)\cdots(c-2R+1) = (c-2)^{\underline{2R-2}}$;
- $(c-1)!/(c-2R+1)! = (c-1)(c-2)\cdots(c-2R+2) = (c-1)^{\underline{2R-2}}$.

Therefore:
$$Q_{2R}^{(B)}(-1, b, c) = 2R(2R-1) \cdot c \cdot (b+1) \cdot (c-1)^{\underline{2R-2}}(c-2)^{\underline{2R-2}}. \tag{Part B}$$

### Combine

$$Q_{2R}(-1, b, c) = Q_{2R}^{(A)}(-1, b, c) - Q_{2R}^{(B)}(-1, b, c) = \tilde P^{(0)}_R(c) + (b+1) \cdot \tilde P^{(1)}_R(c)$$
where $\tilde P^{(1)}_R(c) = -2R(2R-1) \cdot c \cdot (c-1)^{\underline{2R-2}}(c-2)^{\underline{2R-2}}$. $\blacksquare$

## Verification of $\tilde P^{(1)}_R$ against Day 108 empirical data

**R = 3:** $\tilde P^{(1)}_3(c) = -30 \cdot c \cdot (c-1)^{\underline 4}(c-2)^{\underline 4}$
$= -30 c \cdot (c-1)(c-2)(c-3)(c-4) \cdot (c-2)(c-3)(c-4)(c-5)$
$= -30 c(c-1)(c-2)^2(c-3)^2(c-4)^2(c-5)$.

Empirical: $-30 c(c-5)(c-4)^2(c-3)^2(c-2)^2(c-1)$. ✓

**R = 4:** $\tilde P^{(1)}_4(c) = -56 c \cdot (c-1)^{\underline 6}(c-2)^{\underline 6}$
$= -56 c(c-1)(c-2)^2(c-3)^2(c-4)^2(c-5)^2(c-6)^2(c-7)$.

Empirical: $-56 c(c-7)(c-6)^2(c-5)^2(c-4)^2(c-3)^2(c-2)^2(c-1)$. ✓

## Structural framework for higher levels

Empirical fact (Day 110 compute verification, R = 2, 3, 4): $Q_{2R}(a, b, c)$ has total $(a, b)$-degree exactly $2R$ (individual $a$- and $b$-degrees are each $R$). Verified at R=2, 3, 4 for multiple $c$ values.

Combined with the interpolation argument:

**Interpolation Theorem.** Let $F(y_1, y_2, y_3)$ be a polynomial in shifted variables satisfying:
(i) $F$ symmetric in $y_1 \leftrightarrow y_2$;
(ii) total $(y_1, y_2)$-degree $\leq 2R$;
(iii) for each $k = 0, 1, \ldots, R$: $F(k, y_2, y_3)$ has $y_2$-degree $\leq k$.

Then $F(y_1, y_2, y_3) = \sum_{k=0}^R f_k(y_3) y_1^{\underline k} y_2^{\underline k}$ for some polynomials $f_k(y_3)$.

*Proof.* Expand $F$ in the basis $\{y_1^{\underline i} y_2^{\underline j}\}$: $F = \sum c_{i,j}(y_3) y_1^{\underline i} y_2^{\underline j}$. Symmetry gives $c_{i,j} = c_{j,i}$; total degree gives $c_{i,j} = 0$ if $i + j > 2R$. At $y_1 = k$: the coefficient of $y_2^{\underline j}$ (in $F(k, y_2, y_3)$) is $\sum_{i \leq k} c_{i,j}(y_3) k^{\underline i}$. Slice constraint (iii): for $j > k$, this coefficient vanishes. By induction on $k = 0, 1, \ldots, R$: $c_{i,j}(y_3) = 0$ whenever $i < j$ and $i \leq R$. By symmetry: $c_{i,j} = 0$ if $j < i$ and $j \leq R$. Combining: $c_{i,j} = 0$ unless $i = j$ or ($i, j > R$). The second case is impossible under $i + j \leq 2R$. So $F = \sum_{k=0}^R c_{k,k}(y_3) y_1^{\underline k} y_2^{\underline k}$. $\square$

**Consequence.** If we can prove:
- (T) Total $(a, b)$-degree of $Q_{2R} \leq 2R$;
- (Slice-k) for each $k = 0, 1, \ldots, R$: $Q_{2R}(k-2, b, c)$ has $b$-degree $\leq k$;

then $Q_{2R}(a, b, c) = \sum_{k=0}^R f_k(c)(a+2)^{\underline k}(b+1)^{\underline k}$ for some polynomials $f_k(c)$, and all six (R) claims follow.

Slice-0 = (M) — proved Day 109.
Slice-1 follows from $(R_1)$ — proved Day 110 (this note).

**Remaining gaps for full uniform (R):**
1. Prove (T) — total-degree bound $\leq 2R$. Requires cancellation argument in $h_{2R}$: top $(y_1, y_2)$-degree part of $H_c(a, b, j)$ is $j$-independent, so alternating sum kills it. Need to argue this at ALL degrees down to $2R$.
2. Prove Slice-k for $k = 2, \ldots, R$. Would follow from analogous Sublemmas $(U_k)$: closed form for $(ds_j/V)|_{a=k-2}$, plus multi-Chu-Vandermonde arithmetic.
3. Complete Sublemma $(U_1)$ — combinatorial proof for all $j$ (currently empirical up to $j = 16$).

## What (M) + $(R_1)$ + (T) buys us

If we assume (T) and use (M) + $(R_1)$:
- Slice-0, Slice-1 both established.
- Interpolation gives $Q_{2R} = f_0(c) + y_1 y_2 R_1(y_1, y_2, y_3)$ where $R_1$ has total $(y_1, y_2)$-degree $\leq 2R - 2$, and by Slice-1: $R_1(1, y_2, y_3) = f_1(c)$ = b-indep.

Then $R_1 - f_1(y_3) = (y_1 - 1)(y_2 - 1) R_2$ with $R_2$ symmetric of degree $\leq 2R - 4$.

To continue, need Slice-2 for $Q_{2R}$, which is NOT implied by what we have. Analog Sublemma required.

## Bonus: (★) at $R = 2$ is one step from proved

For $R = 2$: with (M) at $k = 4$ giving $\tilde P^{(0)}_2$, Theorem 2 (this note) giving $\tilde P^{(1)}_2$, and empirical verification (multiple $c$-values) giving $\tilde P^{(2)}_2(c) = 12c(c-1)$, the decomposition

$$Q_4(a, b, c) = c(c-4)(c-3)^2(c-2)^2(c-1)^2 + (a+2)(b+1) \cdot [-12 c(c-1)(c-2)^2(c-3)] + (a+2)(a+1)(b+1)b \cdot [12 c(c-1)]$$

is verified. Evaluated at $c = 2$: $f_0(2) = 0$, $f_1(2) = 0$, $f_2(2) = 24 = (-1)^2 \cdot 4!$. Hence
$$Q_4(a, b, 2) = 24 \cdot (a+2)(a+1)(b+1)b = (-1)^2 \cdot 4! \cdot (a+2)^{\underline 2}(b+1)^{\underline 2}$$
which is $(\star)$ at $R = 2$.

**The only remaining gap for the $R = 2$ case is (T):** proving total $(a, b)$-degree $\leq 2R = 4$ (needed to conclude the interpolation gives ONLY terms $y_1^{\underline k} y_2^{\underline k}$ with $k = 0, 1, 2$).

Once (T) is closed at $R = 2$: $(\star)$ at $R = 2$ is a full theorem.

## Meta

Day 110 delivered:
1. **The Level-1 recursion proved** (up to Sublemma $(U_1)$ verification for finite $j$). Same two-lemma structure as (M): rank drop + Chu-Vandermonde.
2. **Explicit closed form for $\tilde P^{(1)}_R(c)$**, matching (LC) at $k=1$.
3. **Interpolation framework** reducing the full (R) to three concrete gaps: total-degree bound, Sublemmas $(U_k)$ for $k \geq 2$, and completing $(U_1)$.
4. Key structural insight: $Q_{2R}$'s total $(a, b)$-degree = $2R$ (empirical), enabling the interpolation.

The proof reveals a beautiful pattern: (M) is the "$y_1 = 0$ case" and $(R_1)$ is the "$y_1 = 1$ case" of a family of specialization identities that combined give the full (★) via interpolation.
