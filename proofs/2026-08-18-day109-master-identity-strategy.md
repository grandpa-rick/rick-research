---
name: (M) Master Identity — proof strategy via O-O shifted Schur (Day 109)
description: Structural strategy for proving Q_k(-2, b, c) = (-1)^k c(c-k) prod_{j=1}^{k-1}(c-j)^2 uniformly in k. Reduces the identity to a shifted-Schur rank-drop plus a claimed b-independence of a specific Pochhammer-weighted sum in the surviving 2-variable shifted Schur functions.
---

# (M) Master Identity — proof strategy — Day 109 (2026-08-18)

## The identity

For all $k \geq 1$:
$$Q_k(-2, b, c) = (-1)^k \cdot c \cdot (c - k) \cdot \prod_{j=1}^{k-1}(c - j)^2 \quad (M)$$

Verified empirically Day 108-109 at k = 1..9 on BOTH slices (a=-2 with b free, and b=-1 with a free — same c-polynomial), R = 3, 4. No FAIL cases.

## Setup — Rick's pipeline as native shifted Schur

Let $y = (y_1, y_2, y_3) := (a+2, b+1, c)$ be Rick's "shifted variables". These are
exactly the shifted variables in Okounkov-Olshanski's Def 1.2 (with $n=3$).

**Vandermonde denominator:**
$$V(y_1, y_2, y_3) := (y_1 - y_2)(y_1 - y_3)(y_2 - y_3) = (a-b+1)(a-c+2)(b-c+1).$$

**Shifted Schur function (O-O Def 1.2, $n = 3$):**
$$s^*_\mu(y_1, y_2, y_3) = \frac{\det[(y_i)_{\downarrow \mu_j + 3 - j}]}{V(y_1, y_2, y_3)}.$$

**Rick's $M_j$ (from pipeline decoding):**
$$M_j(a, b, c) = \frac{(n - 2j)!}{(a+2)!(b+1)!c!} \sum_{\mu \in \mathcal{S}_j} \kappa_\mu \cdot \det[(y_i)_{\downarrow \mu_j + 3 - j}]$$
where $\mathcal{S}_j$ = partitions of $2j$ built by $j$ vertical 2-strips fitting
in $\leq 3$ rows, with multiplicities $\kappa_\mu$ recording walk count.

**Dividing by V:**
$$\frac{M_j}{V} = \frac{(n - 2j)!}{(a+2)!(b+1)!c!} \sum_{\mu \in \mathcal{S}_j} \kappa_\mu \cdot s^*_\mu(y_1, y_2, y_3). \quad (*)$$

**Rick's $H_c$ template** (impulse term dropped, valid for $c > k/2$):
$$H_c(a, b, j) = \underbrace{\frac{c!(a + c + 1 - j)\prod_{i=1}^c (b + i - j)}{\binom{N}{b-j}(a-b+1)(a-c+2)(b-c+1)}}_{=: W_j(a, b, c)} \cdot M_j.$$

Using $V = (a-b+1)(a-c+2)(b-c+1)$ and (*):
$$H_c(a, b, j) = \frac{c!(a+c+1-j)\prod_{i=1}^c (b+i-j)}{\binom{N}{b-j}} \cdot \frac{(n-2j)!}{(a+2)!(b+1)!c!} \sum_{\mu \in \mathcal{S}_j} \kappa_\mu \cdot s^*_\mu(y).$$

**Simplify the scalar coefficient.** With $N = n - 2j$, $\binom{N}{b-j} = \frac{(n-2j)!}{(b-j)!(a+c-j)!}$:
$$\frac{c!(a+c+1-j)\prod_{i=1}^c(b+i-j)(n-2j)!}{\binom{N}{b-j}(a+2)!(b+1)!c!} = \frac{(a+c+1-j)(b-j)!(a+c-j)!\prod_{i=1}^c(b+i-j)}{(a+2)!(b+1)!}.$$

Note $\prod_{i=1}^c(b + i - j) = (b + 1 - j)(b + 2 - j) \cdots (b + c - j) = (b + 1 - j)_c$ (rising) $= (b + c - j)!/(b - j)!$.

So $\prod_{i=1}^c(b+i-j) \cdot (b - j)! = (b + c - j)!$ (assuming $b - j \geq 0$; else read as Pochhammer). And $(a+c+1-j)(a+c-j)! = (a+c+1-j)!$.

Coefficient reduces to:
$$\alpha_j(a, b, c) := \frac{(a + c + 1 - j)! (b + c - j)!}{(a+2)!(b+1)!}. \quad (\alpha)$$

**Cleaned $H_c$:**
$$H_c(a, b, j) = \alpha_j(a, b, c) \cdot \sum_{\mu \in \mathcal{S}_j} \kappa_\mu \cdot s^*_\mu(y_1, y_2, y_3). \quad (H)$$

This is the compact form: $H_c$ is a Pochhammer-weighted sum of shifted Schurs.

## The rank drop at $a = -2$ ($y_1 = 0$)

By shift symmetry of shifted Schurs (O-O Ex 3.5, transported to any variable):
$$s^*_\mu(0, y_2, y_3) = \begin{cases} s^*_\mu(y_2, y_3) & \text{if } \ell(\mu) \leq 2, \\ 0 & \text{if } \ell(\mu) = 3. \end{cases}$$

**Consequence.** Only $\mu \in \mathcal{S}_j$ with $\ell(\mu) \leq 2$ contribute at $a = -2$:
$$H_c(-2, b, j) = \alpha_j(-2, b, c) \cdot \sum_{\substack{\mu \in \mathcal{S}_j \\ \ell(\mu) \leq 2}} \kappa_\mu \cdot s^*_\mu(b + 1, c). \quad (H^-)$$

The 2-variable shifted Schur $s^*_\mu(y_2, y_3) = s^*_{(\mu_1, \mu_2)}(b+1, c)$ has an explicit formula:
$$s^*_\nu(y_2, y_3) = \frac{(y_2)_{\downarrow \nu_1 + 1} \cdot y_3 - y_2 \cdot (y_3)_{\downarrow \nu_1 + 1}}{y_2 - y_3} \cdot (\text{lower shifts})$$
or more usefully via the branching rule again:
$$s^*_\nu(y_2, y_3) = \sum_{\mu_2 \leq \tau \leq \mu_1} \prod_{\alpha \in \nu/\tau}(y_2 - c(\alpha)) \cdot s^*_\tau(y_3).$$

And $s^*_\tau(y_3) = y_3(y_3 - 1)\cdots(y_3 - \tau + 1) = (y_3)_{\downarrow \tau}$.

## The b-independence claim

The formula $(H^-)$ shows $H_c(-2, b, j)$ is manifestly $b$-dependent through
both $\alpha_j(-2, b, c)$ and $s^*_\mu(b+1, c)$. The MIRACLE (M) says that after
the binomial inversion and the final Pochhammer division, **all $b$-dependence
cancels**.

Since the impulse term is 0 for $c > k/2$, and both sides of (M) are polynomials
in $c$ of degree $2k$, it suffices to prove (M) for $c$ generic (equivalently
$c \geq k$).

The cancellation must come from an identity of the form:
$$\text{(cross terms in } h_k = \sum_i (-1)^{k-i}\binom{k}{i} H_i) \equiv 0 \pmod{\text{b-terms}}$$
after dividing by $(a+3)_{c-1-k}(b+2)_{c-1-k}$.

**The polynomial coincidence to prove.** Writing $\beta_j := \alpha_j(-2, b, c)$
and $T_j(b, c) := \sum_{\mu \in \mathcal{S}_j, \ell(\mu) \leq 2} \kappa_\mu s^*_\mu(b+1, c)$:

$$\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j} \beta_j T_j(b, c) = (a+3)_{c-1-k}(b+2)_{c-1-k} \Big|_{a=-2} \cdot (-1)^k c(c-k) \prod_{i=1}^{k-1}(c-i)^2$$

Let $L = c - 1 - k$. At $a = -2$: $(a+3)_L = (1)_L = L! = (c-1-k)!$.

**RHS:**
$$(c-1-k)! \cdot (b+2)_{c-1-k} \cdot (-1)^k c(c-k)\prod_{i=1}^{k-1}(c-i)^2$$

So the LHS is a polynomial in b that, after dividing by $(b+2)_{c-1-k}$, becomes
b-independent. This is the CORE claim.

## Route 1: Coherence relations (O-O Thm 10.1)

The coherence theorem gives identities like:
$$\text{Avr}_n^N s^*_\mu|_n = \frac{(n \uparrow \mu)}{(N \uparrow \mu)} s^*_\mu|_N$$

where $(n \uparrow \mu) = \prod_{\alpha \in \mu}(n + c(\alpha))$ is the "generalised Pochhammer".

The binomial inversion $h_k = \sum_i (-1)^{k-i}\binom{k}{i} H_i$ over $j$
resembles a **finite-difference operator** $\Delta^k$ applied to $H_c(a, b, \cdot)$
at $j = 0$. Coherence-type identities may allow us to compute $\Delta^k H_c$ in
closed form, because $H_c$ is a Pochhammer-weighted sum of shifted Schurs and
finite differences act nicely on Pochhammer symbols.

**Concrete tactic.** For each $\mu$, $\Delta_j^k [\alpha_j \cdot s^*_\mu(y)]$ can
be expanded via Leibniz for finite differences:
$$\Delta^k[\alpha_j \cdot s^*_\mu(y)] = \sum_{i+l=k}\binom{k}{i}\Delta^i \alpha_j \cdot \Delta^l s^*_\mu(y_\bullet)$$
if $s^*_\mu$ depended on $j$; but $s^*_\mu(y)$ is $j$-independent (only $\alpha_j$
depends on $j$). So the entire $j$-dependence is in $\alpha_j$, and:
$$h_k = \sum_{\mu} \kappa_\mu s^*_\mu(y) \cdot \Delta_j^k \alpha_j\big|_{j=0}.$$

Wait — that's a MASSIVE simplification! Let me redo this.

**Restatement.** From $(H)$: $H_c(a, b, j) = \alpha_j \cdot \sum_\mu \kappa_\mu s^*_\mu(y)$.
The RHS factors as: (something depending on $j$) times (something not depending on $j$).
So the binomial inversion $h_k = \Delta_j^k H_c\big|_{j=0}$ is:
$$h_k(a, b, c) = \left(\Delta_j^k \alpha_j(a, b, c)\Big|_{j=0}\right) \cdot \sum_{\mu \in \mathcal{S}_?} \kappa_\mu s^*_\mu(y).$$

**But wait** — $\mathcal{S}_j$ depends on $j$! Not the same partition set for each $j$.
So the decomposition is:
$$H_c(a, b, j) = \alpha_j(a, b, c) \cdot \Sigma_j(y), \quad \Sigma_j(y) := \sum_{\mu \in \mathcal{S}_j} \kappa_\mu s^*_\mu(y).$$

Both factors are j-dependent, so Leibniz gives:
$$h_k = \sum_{i=0}^{k} \binom{k}{i}(-1)^{k-i} \left(\Delta_j^? \alpha_j\right) \cdot \Sigma_{?}$$

Full Leibniz for forward differences: $\Delta^k(f \cdot g)(x) = \sum_{i=0}^k \binom{k}{i} \Delta^i f(x) \cdot \Delta^{k-i} g(x + i)$.
For our operator $\Delta_j^k f = \sum_{i}(-1)^{k-i}\binom{k}{i} f(i)$ at $j = 0$ (Newton
finite difference at 0):
$$h_k = \sum_{i=0}^{k} \binom{k}{i}(-1)^{k-i} \alpha_i \Sigma_i.$$

**This is the same as the original.** So the Leibniz simplification doesn't
immediately apply. However, since we can split the coefficient into a product:
$$\alpha_j = \frac{(a+c+1-j)!(b+c-j)!}{(a+2)!(b+1)!}$$
both factors are $j$-dependent, and there might still be a clean form via the
Vandermonde-Chu identity or the Chu-Vandermonde convolution.

## Route 2: Characterization theorem (O-O Thm 3.2)

Show that $Q_k(-2, b, c)$:
- is a polynomial in $b$ of degree $\leq d(k)$ for some small $d$;
- vanishes at $b = 0, 1, ..., d(k)$ (or similar);
- has known values at $b = -1$ or another anchor.

Then by uniqueness, $Q_k(-2, b, c)$ is determined.

**Empirical:** $\deg_b Q_k = 2\lfloor k/2 \rfloor$. So for k=1: $\deg_b = 0$
(constant, matches (M)). For k=2: $\deg_b = 2$; but (M) says $Q_2(-2, b, c) = c(c-2)(c-1)^2$
which has $\deg_b = 0$! So there's a MASSIVE degree drop at $a = -2$.

**This is a concrete route.** Show $Q_k(a, b, c)|_{a=-2}$ has $b$-degree 0 by
degree counting after the pipeline collapse.

## Route 3: Small-case induction

Prove (M) at k = 1, 2, 3 by direct computation (delegated to compute agent).
Extract the induction pattern.

## Status at end of Day 109

- **k = 1, k = 2 by-hand derivation:** dispatched to compute agent, in progress.
- **Route 2 (Characterization / degree drop):** most promising short-term
  route. Concrete step: prove $Q_k(-2, b, c)$ has $b$-degree 0 by counting
  the b-degree in $(H^-)$ after cancellations.
- **Route 1 (Coherence):** cleanest long-term route. Requires more O-O
  identity-fu than I have loaded right now.

## Next PROVE session priorities

1. Finish the k=1, k=2 detailed derivations (compute agent).
2. Extract the b-cancellation MECHANISM from the k=2 case.
3. Formulate the induction step precisely.
4. If the induction pattern is clean → attempt uniform proof via Coherence.
5. Else → attempt Route 2 (degree drop) and prove degree bound uniformly.

## Bonus insight — a↔b duality is a shifted-Schur symmetry

Rick observed empirically: $Q_k(-2, b, c) = Q_k(a, -1, c)$. Both slices are the
same c-polynomial. This is EXPLAINED by shifted-Schur symmetry: setting $y_1 = 0$
vs $y_2 = 0$ triggers the same rank drop (since $s^*_\mu$ is symmetric in the
$y_i$'s). What ISN'T automatic is that Rick's $\alpha_j$ coefficient (which is
NOT $y$-symmetric — it's manifestly asymmetric in a and b) doesn't spoil the
symmetry after the binomial inversion and Pochhammer division. **The
b-independence of (M) is a stronger claim than a↔b duality**; duality follows
FROM b-independence (both slices are constant in the free variable, and if
they're equal at any one shared point, they're equal everywhere).
