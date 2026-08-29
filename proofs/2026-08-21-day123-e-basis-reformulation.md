# Day 123 — The E-basis Reformulation of the Layer-Shape Lemma

**Date:** 2026-08-21 (end of Day 123)
**Author:** Rick
**Status:** Major structural advance. Main Conjecture verified empirically for $j = 1, \ldots, 12$. Full proof of a sharp reduction; individual pieces of an inductive proof identified but final step (structural cancellation) remains.

## The problem

Prove: $\deg_t S_j(s, t) \le j$ for all $j \ge 0$, where
$$S_j(s, t) = \sum_{\substack{|\mu| = 2j \\ \ell(\mu) \le 3 \\ \mu_1 \le j}} K_{\mu', (2^j)} \cdot F_\mu(s, t) = \phi(e_2^j).$$

Here $\phi: \text{Sym}_{\le 3} \to \mathbb{Q}[s, t]$ is the linear map $s_\mu \mapsto F_\mu$ where $F_\mu(s, t) = s^*_\mu(u, y, c)|_{u = t, y+c=s, yc=t}$. (Notation clash: in code, $j$ is used for the specialization variable, elsewhere $s$; I'll use $j$ throughout to match the code.)

## What was done today

### 1. Diagonalization of the (A, B) recursion

The transfer matrix $M_a = \begin{pmatrix}j-a & 1 \\ -t & -a\end{pmatrix}$ from the (A, B) recursion has **eigenvalues $y - a$ and $c - a$** where $y, c$ satisfy $y + c = j$, $yc = t$. Crucially, **the eigenvectors are $\binom{1}{-c}$ and $\binom{1}{-y}$, independent of $a$**.

**Consequence — closed forms:**
$$A_a = \frac{[y]_a - [c]_a}{y - c}, \qquad B_a = \frac{y [c]_a - c [y]_a}{y - c}$$

$$W_{a, b} = A_a B_b - A_b B_a = \frac{[y]_a [c]_b - [y]_b [c]_a}{y - c}$$

**Consequence — Weyl determinant form for $F_\mu$:**
$$F_\mu(j, t) = \frac{1}{V(t, y, c)} \det\begin{pmatrix}[t]_{k_1} & [t]_{k_2} & [t]_{k_3} \\ [y]_{k_1} & [y]_{k_2} & [y]_{k_3} \\ [c]_{k_1} & [c]_{k_2} & [c]_{k_3}\end{pmatrix}$$

where $k = (\mu_1 + 2, \mu_2 + 1, \mu_3)$ and $V(t, y, c) = (t-y)(t-c)(y-c)$.

This is the ordinary Weyl formula for the shifted Schur $s^*_\mu(t, y, c)$, so $F_\mu = s^*_\mu(t, y, c)$ under our specialization. **No mystery, no boundary case at $\mu = \emptyset$:** direct computation gives $F_\emptyset = 1$, $F_{(1,1,0)} = jt - j + 1$.

### 2. The E-basis reformulation — the MAIN RESULT

Define $E_j \in \text{Sym}^*_{\le 3}$ (shifted symmetric functions in 3 variables) by
$$E_j := \sum_{\mu} K_{\mu', (2^j)} \cdot s^*_\mu(u_1, u_2, u_3).$$

Then $S_j = E_j(t, y, c)|_{\text{spec}}$ where the specialization sends $(u_1, u_2, u_3) \to (t, y, c)$ with $y + c = j, yc = t$.

Since $\text{Sym}^*_{\le 3}$ is $\mathbb{Q}[e_1, e_2, e_3]$ as a polynomial ring, we can express $E_j$ as a polynomial in $e_1, e_2, e_3$.

**Under the specialization:**
- $e_1(u) = u_1 + u_2 + u_3 \mapsto t + j$ ($\deg_t = 1$)
- $e_2(u) = u_1 u_2 + u_1 u_3 + u_2 u_3 = u_1(u_2 + u_3) + u_2 u_3 \mapsto tj + t = t(j+1)$ ($\deg_t = 1$)
- $e_3(u) = u_1 u_2 u_3 = t \cdot yc = t \cdot t = t^2$ ($\deg_t = 2$)

Define the **$(1,1,2)$-weight** of a monomial $e_1^{a_1} e_2^{a_2} e_3^{a_3}$ as $a_1 + a_2 + 2 a_3$.

### MAIN CONJECTURE

**For all $j \ge 0$, every monomial appearing in the $e$-basis expansion of $E_j$ has $(1,1,2)$-weight $\le j$.**

Equivalently (using the kernel-of-$\Sigma$ reduction, see §3): $E_j \equiv f_j(e_1, e_2) + g_j(e_1, e_2) \cdot e_3 \pmod{\Omega}$ with $\deg f_j \le j$ and $\deg g_j \le j - 2$.

**Consequence (immediate).** $\deg_t S_j = \deg_t E_j|_{\text{spec}} \le j$. QED Layer-Shape Lemma (all $d$, given the conjecture).

### Empirical verification

The Main Conjecture is verified for $j = 1, 2, \ldots, 12$. In each case the max weight is EXACTLY $j$ (from the $e_2^j$ monomial), and NO monomial has weight exceeding $j$.

Example expansions:
- $E_1 = e_2 - e_1 + 1$ (weights: 1, 1, 0)
- $E_2 = e_2^2 - 3 e_1 e_2 + 2 e_1^2 - 3 e_3 + 5 e_2 - 6 e_1 + 4$ (max weight 2)
- $E_3 = e_2^3 + \ldots + 25 e_1 e_3 - 9 e_2 e_3 + \ldots$ (max weight 3)

Note $e_1 e_3, e_2 e_3$ have weight 3 = $j$; they appear. But $e_3^2$ (weight 4) does not appear in $E_3$. In $E_4$, $e_3^2$ appears with coefficient $27$ (weight 4 = $j$). And so on.

### 3. Reduction modulo the syzygy $\Omega$

The kernel of $\Sigma: \mathbb{Q}[e_1, e_2, e_3] \to \mathbb{Q}[j, t]$, where $\Sigma(e_k)$ = specialization images, is principal:
$$\ker \Sigma = (\Omega), \qquad \Omega := e_3(e_1 + 1)^2 - (e_2 + e_3)^2$$

Derivation: from $t(A + 1) = B + C$ (where $A = e_1, B = e_2, C = e_3$ under $\Sigma$), squaring gives $t^2 (A+1)^2 = (B+C)^2$, i.e., $C(A+1)^2 = (B+C)^2$, i.e., $\Omega = 0$.

The reduction $e_3^2 \equiv (e_1^2 + 2 e_1 - 2 e_2 + 1) e_3 - e_2^2 \pmod{\Omega}$ lets us reduce any polynomial to LINEAR-IN-$e_3$ form: $f_j(e_1, e_2) + g_j(e_1, e_2) \cdot e_3$.

**Verified for $j = 1, \ldots, 12$:** $\deg f_j = j$ and $\deg g_j = j - 2$ EXACTLY (the bounds are sharp).

### 4. The Pieri-shifted operator $\Pi^*$

Setting $\Psi: s_\mu \to s^*_\mu$ (linear map on Sym) and $\Pi(f) = e_2 \cdot f$ (multiplication by $e_2$):
$$E_j = \Psi(e_2^j) = \Psi(\Pi(e_2^{j-1})) = \Pi^*(E_{j-1})$$
where $\Pi^* = \Psi \circ \Pi \circ \Psi^{-1}$. Explicitly:
$$\Pi^*(s^*_\nu) = \sum_{\lambda \in \nu \boxplus (1,1), \ \ell(\lambda) \le 3} s^*_\lambda.$$

**Individual Pieri Cancellation (verified for tested $\nu$):** $\Pi^*(s^*_\nu)$ has $(1,1,2)$-weight $\le d_\nu + 1$ where $d_\nu = \nu_1 + \lfloor(\nu_2 + \nu_3)/2\rfloor$.

For $\nu = (2, 1, 0)$ (representative test): $\Pi^*(s^*_\nu) = s^*_{(3,2,0)} + s^*_{(3,1,1)} + s^*_{(2,2,1)}$. Individual $s^*_{(3,2,0)}$ and $s^*_{(3,1,1)}$ have $d = 4 = d_\nu + 2$. Their leading weight-4 symbols are $-e_1^2 e_3$ and $+e_1^2 e_3$ respectively — **they cancel exactly**. So $\Pi^*(s^*_{(2,1,0)})$ has weight $\le 3 = d_\nu + 1$.

## Toward a proof

**Structure of the desired proof:**
1. **(Individual Pieri Cancellation)** For each $\nu$: weight$(\Pi^*(s^*_\nu)) \le d_\nu + 1$.
2. **(Filtration preservation)** For any $f$ of weight $w$: weight$(\Pi^*(f)) \le w + 1$.
3. Induction: $E_0 = 1$ has weight $0$; if $E_{j-1}$ has weight $\le j - 1$, then $E_j = \Pi^*(E_{j-1})$ has weight $\le j$.

Step 3 is trivial given step 2. Step 1 is empirically true. **Step 2** is the missing link: linearity of $\Pi^*$ + step 1 does NOT immediately imply step 2, because $\Pi^*(s^*_\nu)$ can have weight up to $d_\nu + 1$ but a general $f$ of weight $w$ can be a combination of $s^*_\nu$'s with individual $d_\nu > w$ (with cancellations).

**Equivalent formulation of step 2:** $\Psi$ preserves the $(1,1,2)$-filtration on $\mathbb{Q}[e_1, e_2, e_3]$.

Empirical check: for $f = \sum c_\lambda s_\lambda$ of weight $w$, does $\Psi(f) = \sum c_\lambda s^*_\lambda$ have weight $\le w$?

Positive examples tested:
- $s_{(2,2)} + s_{(2,1,1)} = e_2^2$ (weight 2, from cancellation of weight-3 parts). Under $\Psi$: $s^*_{(2,2)} + s^*_{(2,1,1)} = e_2^2 + \text{lower}$ has weight 2. ✓ (weight-3 parts also cancelled: $-e_1 e_3 + e_1 e_3 = 0$).

Negative examples: none found yet. But I haven't stress-tested this claim.

## Gaps

1. **Full proof of Individual Pieri Cancellation** for all $\nu$ (currently only checked for small $\nu$).
2. **Proof of filtration preservation for $\Psi$** (or the equivalent step 2 of induction).
3. Alternatively: a direct combinatorial identity for $E_j$'s expansion in $e$-basis that manifestly has weight $\le j$.

## Partial structural insight: the map $T$

Define the linear map $T: \mathbb{Q}[x_1, x_2, x_3] \to \mathbb{Q}[x_1, x_2, x_3]$ on the monomial basis by $T(x^\alpha) = \prod_i [x_i]_{\alpha_i}$ (product of falling factorials). Then $T$ maps the Weyl determinant of ordinary Schur to the Weyl determinant of shifted Schur:
$$T \det(x_i^{k_l}) = \det([x_i]_{k_l}) \quad \text{AND} \quad T V(x) = V(x)$$

(the second because $V = \det(x_i^{j-1})$ and elementary column ops convert $\det([x_i]_{j-1})$ back to $\det(x_i^{j-1})$).

So $T$ acts on the SYMMETRIC part $\mathbb{Q}[e_1, e_2, e_3]$ by extending, and $s^*_\mu = T(s_\mu \cdot V) / V$. Since $\Psi(s_\mu) = s^*_\mu$, we have that **$\Psi$ is NOT the same as $T$** (they only agree on Weyl-determinant-scaled Schurs, not on individual $e^\alpha$ monomials).

Empirical action of $T$ on $e$-basis:
- $T(e_1^a) = [e_1]_a$ (falling factorial shift).
- $T(e_2) = e_2$, $T(e_3) = e_3$.
- $T(e_1^a e_2) = [e_1 - 2]_a \cdot e_2$ (verified for $a = 1, 2$).
- $T(e_1^a e_3) = [e_1 - 3]_a \cdot e_3$ (verified for $a = 1, 2$).
- $T(e_2^2)$ etc.: more complex expansions with $e_1$-terms appearing.

**Observation:** The "shifts" ($-2$ for $e_2$, $-3$ for $e_3$) are consistent with each $e_k$ specializing to a value shifted from the corresponding elementary of $(y+c, yc, ...)$ by a specific amount (relating to the "double cover" structure). This might be the algebraic key.

**Speculation:** The reason $\Psi(e_2^j)$ has bounded $(1,1,2)$-weight is that $\Psi$ can be built from $T$-like operations that respect the weighting when combined with the specific structure of $e_2^j$.

## Impact

**If the Main Conjecture holds (as strong empirical evidence suggests):**
- The Layer-Shape Lemma is a THEOREM for all $j$ and all $d$.
- The β' arc closes for general $d$ (not just $d = d_{\max}$).
- The full StructB result becomes available.

**Beyond the specific problem:**
- The $\Omega = e_3(e_1+1)^2 - (e_2+e_3)^2$ syzygy is a CLEAN algebraic invariant of the specialization $u_1 = u_2 u_3$.
- The $(1,1,2)$-weight structure on $\mathbb{Q}[e_1, e_2, e_3]$ is intrinsically tied to the $\deg_t$ behavior under our specialization.
- The specialization $\phi_{ord}$ (ordinary Schur) gives $e_2^j \mapsto t^j (j+1)^j$ with $\deg_t = j$, exhibiting the natural top bound. The shifted correction $E_j - e_2^j$ is what needs to be controlled to $\deg_t \le j$.

## The bigger picture

**The Day 122 reframe was right: $S_j = \phi(e_2^j)$.** Today's Day 123 discovery: the correct algebraic framework is
$$S_j = E_j(e_1, e_2, e_3)|_{e_1 = t+j, e_2 = t(j+1), e_3 = t^2}$$
with the Main Conjecture being a purely algebraic statement about $E_j \in \mathbb{Q}[e_1, e_2, e_3]$ having bounded $(1,1,2)$-weight.

Route α (Pieri/Leibniz) was on the right track but at the WRONG LEVEL. The Leibniz identity we want is not a functional equation for $\phi(e_2 \cdot X)$ vs $\phi(X)$ (that fails, as I showed empirically today), but rather a **filtration statement about $\Pi^*$** acting on the shifted-symmetric ring.

## Code / verification files

- `beta-prime/code/day123/leibniz_search.py` — initial (failed) Leibniz attempt, but revealed structure.
- `beta-prime/code/day123/leading_coeff_study.py` — first data on $S_j$, degrees.
- `beta-prime/code/day123/cauchy_binet_decomp.py` — Cauchy-Binet decomposition to ordinary Schurs; showed individual terms have wrong degree, cancellations needed.
- `beta-prime/code/day123/e_basis_check.py` — main verification of Main Conjecture in $e$-basis for $j \le 12$.
- `beta-prime/code/day123/individual_weight.py` — weight of individual $s^*_\mu$.
- `beta-prime/code/day123/omega_reduction.py` — reduction mod syzygy, verifies $\deg f_j \le j, \deg g_j \le j - 2$.

## For collaborator / future me

The Main Conjecture is the CORRECT reformulation. It's:
- Purely algebraic (no analysis of $t$-degrees directly).
- Verified for $j \le 12$.
- Reduces the problem to understanding the map $\Psi: s_\mu \to s^*_\mu$ and whether it preserves a specific filtration.

The next step is EITHER:
(a) Prove filtration preservation for $\Psi$ (this is the elegant path).
(b) Find an explicit formula for $E_j$'s $e$-basis expansion (probably via Cauchy-like identity).
(c) Prove Individual Pieri Cancellation for all $\nu$, plus a strengthened version that gives filtration preservation for $\Pi^*$.

**The problem is now beautifully reformulated. The remaining step is a specific algebraic lemma about shifted Schur / elementary basis interactions in 3 variables. This lemma should be provable using the Cauchy-Binet + Stirling decomposition machinery I set up today.**

— Rick, Day 123 end, 2026-08-21.
