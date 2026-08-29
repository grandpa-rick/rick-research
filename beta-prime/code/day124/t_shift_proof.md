# Proof of the T-shift identity

**Claim.** Let $T: \mathbb{Q}[x_1,\ldots,x_n]\to\mathbb{Q}[x_1,\ldots,x_n]$ act on
monomials by
$$T(x_1^{a_1}\cdots x_n^{a_n}) = [x_1]_{a_1}\cdots [x_n]_{a_n},$$
where $[x]_m = x(x-1)\cdots(x-m+1)$.  Let $e_k = e_k(x_1,\ldots,x_n)$.  For all
$a\ge 0$ and $k\ge 1$,
$$T(e_1^a\cdot e_k) = [e_1-k]_a\cdot e_k.$$

**Proof (exponential generating function, single page).**

*Step 1: A single-variable EGF.*  For any variable $x$ and formal parameter $t$,
$$\sum_{a\ge 0}[x]_a\frac{t^a}{a!} = (1+t)^x.$$
(Newton's binomial for the falling factorials.)

*Step 2: Factor $e^{t e_1}$ across variables.*  Since $e_1 = x_1+\cdots+x_n$,
$$e^{te_1} = \prod_{i=1}^n e^{t x_i} \qquad\text{and}\qquad
\sum_{a\ge 0}\frac{t^a}{a!}e_1^a\cdot g = e^{t e_1}\cdot g$$
for any polynomial $g$.

*Step 3: Compute $T(e^{te_1}\cdot x^\beta)$ for a single monomial $x^\beta$.*
The operator $T$ is $\mathbb{Q}[[t]]$-linear (it acts monomial-wise), and it
factors across variables because $T(x_1^{a_1}\cdots x_n^{a_n}) =
\prod_i [x_i]_{a_i}$.  Thus
$$T\!\left(\prod_i e^{tx_i} x_i^{\beta_i}\right)
= \prod_i T\!\left(e^{tx_i}\cdot x_i^{\beta_i}\right)
= \prod_i \sum_{m\ge 0}\frac{t^m}{m!}[x_i]_{m+\beta_i}.$$
Using the elementary identity $[x_i]_{m+\beta_i} = [x_i]_{\beta_i}\cdot
[x_i-\beta_i]_m$ and Step 1 (applied to $x_i-\beta_i$),
$$\sum_{m\ge 0}\frac{t^m}{m!}[x_i]_{m+\beta_i}
= [x_i]_{\beta_i}\sum_{m\ge 0}\frac{t^m}{m!}[x_i-\beta_i]_m
= [x_i]_{\beta_i}(1+t)^{x_i-\beta_i}.$$
Therefore
$$T(e^{te_1}\cdot x^\beta)
= \prod_i [x_i]_{\beta_i}(1+t)^{x_i-\beta_i}
= (1+t)^{\sum_i(x_i-\beta_i)}\prod_i [x_i]_{\beta_i}
= (1+t)^{e_1-|\beta|}\cdot T(x^\beta).$$

*Step 4: Extend to any homogeneous $g$ of degree $d$.*  By linearity in $\beta$
(all $|\beta|=d$ contribute the same shift), for any homogeneous $g$ of degree
$d$,
$$\sum_{a\ge 0}\frac{t^a}{a!}T(e_1^a\cdot g) = (1+t)^{e_1-d}\cdot T(g).$$

*Step 5: Specialize to $g = e_k$.*  Note $T(e_k) = e_k$: every monomial in $e_k$
is squarefree, and $[x_i]_0 = 1$, $[x_i]_1 = x_i$, so $T$ fixes each squarefree
monomial.  With $d = k$,
$$\sum_{a\ge 0}\frac{t^a}{a!}T(e_1^a\cdot e_k) = (1+t)^{e_1-k}\cdot e_k
= e_k\cdot \sum_{a\ge 0}\frac{[e_1-k]_a}{a!}t^a.$$
Comparing coefficients of $t^a/a!$,
$$T(e_1^a\cdot e_k) = [e_1-k]_a\cdot e_k. \qquad\blacksquare$$

## Remarks

1. The proof needs $g$ to be *multilinear* only in Step 5 (to give $T(g) = g$).
   For any homogeneous $g$ of degree $d$, we get
   $$T(e_1^a\cdot g) = \sum_{j=0}^a s(a, j)\, e_1^j\cdot (-d)^{a-j}\cdot T(g)
     + \text{(lower-order corrections from $T(g)\neq g$)}.$$
   More precisely: **the full identity**
   $$\boxed{\;\sum_a\frac{t^a}{a!}T(e_1^a\cdot g) = (1+t)^{e_1-\deg g}\cdot T(g)\;}$$
   holds for any homogeneous $g$.  When $g = e_k$, $T(g)=g$, giving the clean
   form.

2. The shift by $-\deg g$ (rather than by, say, $-\text{something-else}$) is the
   *content* of the identity: multiplying $g$ by $e_1$ shifts the falling
   factorial's argument down by exactly the number of variables that already
   consumed a "slot" in $g$.

3. The identity also implies $T(e_1^a\cdot m_\lambda) = [e_1-|\lambda|]_a\cdot
   T(m_\lambda)$ where $m_\lambda$ is a monomial symmetric function *only if*
   $T(m_\lambda)$ is a scalar multiple of $m_\lambda$ (which it is not in
   general).  The cleanness for $e_k$ comes from multilinearity.

## Corollary (falling-factorial form).

Since $[e_1-k]_a = \sum_j s(a,j)(-k)^{a-j}[e_1]_j$ or equivalently
$[e_1-k]_a = \sum_j\binom{a}{j}(-k)^{a-j}[e_1]_{a-j}\cdot\text{(no, wait)}$—the
cleanest statement is:
$$T(e_1^a\cdot e_k) = (e_1-k)(e_1-k-1)\cdots(e_1-k-a+1)\cdot e_k.$$
