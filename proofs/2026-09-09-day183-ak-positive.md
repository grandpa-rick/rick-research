# Day 183 — $a_k > 0$ for all $k \ge 1$

**Date:** 2026-09-09
**Author:** Rick
**Status:** proved (elementary; one page)

---

## Problem

Let $F(\vartheta) = \sum_{k \ge 1} b_k \vartheta^k \in \mathbb Z[[\vartheta]]$ be the unique power-series solution of
$$F(1-F)^3(3-4F) \;=\; \vartheta\,(3-2F)^2. \tag{$\dagger$}$$
Define $a_k$ by $A(\vartheta) := F/(1+F) = \sum_{k \ge 1} a_k \vartheta^k$. Prove $a_k > 0$ for every $k \ge 1$.

## Result

**Theorem.** $a_k > 0$ for every $k \ge 1$.

By Andrews–Gagnon–Gélinas–Schlums–Zabrocki (arXiv 2505.06941, Thm 4.2), this is equivalent to the statement that $(b_k)_{k \ge 0}$ (with $b_0 := 1$) is the graded-dimension sequence of a Free Graded Connected Cocommutative Hopf Algebra over $\mathbb C$; the FGCCHA is unique up to Hopf isomorphism and equals $U(L(a))$ where $L(a)$ is the free graded Lie algebra with $a_k$ generators in degree $k$.

## Proof

### Step 1 — Lagrange form for $A$

Substituting $F = A/(1-A)$ into $(\dagger)$:
- $1 - F = (1-2A)/(1-A)$,
- $3 - 4F = (3 - 7A)/(1-A)$,
- $3 - 2F = (3 - 5A)/(1-A)$.

$(\dagger)$ becomes
$$\frac{A}{1-A} \cdot \frac{(1-2A)^3}{(1-A)^3} \cdot \frac{3-7A}{1-A} \;=\; \vartheta \cdot \frac{(3-5A)^2}{(1-A)^2},$$
which rearranges to
$$A \;=\; \vartheta \,\varphi(A), \qquad \varphi(A) \;:=\; \frac{(3-5A)^2 (1-A)^3}{(1-2A)^3 (3-7A)}. \tag{L}$$
Since $\varphi(0) = 9/3 = 3 \ne 0$, Lagrange inversion applies:
$$a_k \;=\; \frac{1}{k}\,[A^{k-1}]\,\varphi(A)^k, \qquad k \ge 1. \tag{L*}$$

### Step 2 — $\varphi$ has strictly positive Taylor coefficients

Take logarithms. Using $\log(3 - cA) = \log 3 - \sum_{n \ge 1} (c/3)^n A^n / n$ and $\log(1 - cA) = -\sum_{n \ge 1} c^n A^n / n$:

$$\log \varphi(A) \;=\; 2\log(3-5A) + 3\log(1-A) - 3\log(1-2A) - \log(3-7A)$$
$$\;=\; \log 3 + \sum_{n \ge 1} \frac{\ell_n}{n}\,A^n,$$
where
$$\boxed{\;\ell_n \;=\; 3 \cdot 2^n + \left(\tfrac{7}{3}\right)^n - 2 \left(\tfrac{5}{3}\right)^n - 3.\;}$$

**Claim.** $\ell_n > 0$ for every $n \ge 1$.

Multiplying by $3^n$, this is equivalent to
$$3 \cdot 6^n + 7^n \;>\; 2 \cdot 5^n + 3^{n+1}. \tag{$\ast$}$$

*Case $n = 1$:* $18 + 7 = 25 > 19 = 10 + 9$. ✓
*Case $n = 2$:* $108 + 49 = 157 > 77 = 50 + 27$. ✓
*Case $n \ge 3$:* Two inequalities:
- $3 \cdot 6^n > 3^{n+1}$, i.e. $6^n > 3^n$: holds strictly for all $n \ge 1$.
- $7^n \ge 2 \cdot 5^n$: since $(7/5)^3 = 343/125 > 2$, we have $(7/5)^n \ge 2$ for $n \ge 3$.

Adding, $3 \cdot 6^n + 7^n > 3^{n+1} + 2 \cdot 5^n$.

Hence $\ell_n > 0$ for all $n \ge 1$. $\square$

**Consequence.** Write $L(A) := \sum_{n \ge 1} (\ell_n / n) A^n$. Then $\varphi(A)/3 = \exp(L(A))$ as formal power series, and $L$ has strictly positive coefficients.

For any formal power series $L$ with $L(0)=0$ and non-negative Taylor coefficients,
$$\exp(L) \;=\; \sum_{k \ge 0} \frac{L^k}{k!}$$
has non-negative Taylor coefficients (each $L^k$ is a product of non-negative series, and non-negative reals are closed under addition). In particular
$$[A^m]\exp(L) \;\ge\; [A^m] L \;=\; \frac{\ell_m}{m} \;>\; 0 \quad (m \ge 1).$$
Therefore every Taylor coefficient of $\varphi(A) = 3 \exp(L)$ is strictly positive:
$$\varphi(A) \;=\; \sum_{n \ge 0} c_n A^n, \qquad c_n > 0 \text{ for all } n \ge 0. \tag{P}$$

### Step 3 — Conclusion

Let $k \ge 1$. Since $\varphi$ has all-positive Taylor coefficients (by (P)), so does $\varphi^k$:
$$[A^m] \varphi(A)^k \;=\; \sum_{i_1 + \cdots + i_k = m} c_{i_1} \cdots c_{i_k} \;>\; 0 \qquad (m \ge 0).$$
In particular $[A^{k-1}]\varphi(A)^k > 0$, so by $(L^*)$,
$$a_k \;=\; \frac{1}{k}\,[A^{k-1}]\,\varphi(A)^k \;>\; 0. \qquad \blacksquare$$

---

## Corollaries

**Corollary 1 (FGCCHA structure).** $(1, b_1, b_2, \ldots) = (1, 3, 27, 417, 7851, \ldots)$ is the graded-dimension sequence of a Free Graded Connected Cocommutative Hopf Algebra over $\mathbb C$, unique up to Hopf iso: $U(L(a))$ with $L(a)$ the free graded Lie algebra on $a_k$ generators in degree $k$. *(AGGSZ Thm 4.2 + Theorem above.)*

**Corollary 2 ($p_k > 0$ unconditional).** The graded Lie-primitive dimensions $p_k$ (i.e. graded dims of $L(a)$) satisfy $p_k > 0$ for all $k \ge 1$. *(Witt formula: $p_k = \frac{1}{k}\sum_{d | k}\mu(k/d)\left(\sum_{n_1 + 2 n_2 + \cdots = d}\frac{d!}{n_1! n_2! \cdots} \prod a_j^{n_j}\right)$ — or by direct free-Lie counting: any Lyndon word in $a_j$-alphabets exists at each degree since $a_1 = 3 > 0$.)*

**Corollary 3 (structural stability of the arc).** The whole Day 148 → Day 183 arc is now, over $\mathbb C$, unconditionally a FGCCHA statement about a specific algebra $U(L(a))$.

---

## Verification

Computational checks (see `scratch/day183_ak_positive/verify.py`):

- $\ell_n > 0$ for $n = 1..40$. Sample: $\ell_1 = 2$, $\ell_2 = 80/9$, $\ell_5 = 1228/9$.
- Taylor coefficients $c_n = [A^n]\varphi$ verified positive for $n = 0..30$; first few: $c_0 = 3$, $c_1 = 6$, $c_2 = 58/3$, $c_3 = 496/9$, ...
- $a_k$ computed for $k = 1..20$ via the recursion $a_k = b_k - \sum_{j=1}^{k-1} a_j b_{k-j}$, with $b_k$ obtained by direct power-series solution of $(\dagger)$ (`scratch/day183_ak_positive/verify_direct.py`). All 20 are strictly positive; first 12 match tabulated $a_1..a_{12}$ exactly. Extension:
$$a_{13} = 14{,}599{,}169{,}971{,}317{,}714, \quad a_{20} = 148{,}792{,}125{,}808{,}270{,}433{,}731{,}987{,}944.$$
- Lagrange formula $a_k = (1/k)[A^{k-1}]\varphi^k$ separately verified for $k = 1..7$ (matches recursion output; `verify.py`).

---

## Method notes (for future-me)

- **Rule 11 fires again.** The problem asked for global positivity of an algebraic power series. The instinct to reach for Furstenberg diagonals / Roques / combinatorial witnesses was wrong. The elementary answer: Lagrange puts everything on $\varphi$, and $\varphi$'s log has an obvious four-term signed-exponential structure that anyone can bound.
- **Why log-positivity is the natural test.** $\varphi$ is a ratio of two-linear polynomials in $A$. Every such expression's log expands as $\sum (\pm r_i^n) A^n / n$ for finitely many $r_i$. Positivity of $\ell_n$ is then a finite comparison of exponentials — trivial once written down.
- **The four exponents $\{2, 7/3, 5/3, 1\}$ and their weights $\{3, 1, -2, -3\}$.** The "worst" balance point is at small $n$ where the largest positive exponent $(2)$ has not yet dominated. The proof handles $n = 1, 2$ directly and lets asymptotics win from $n = 3$.
- **Comparison to $b_k$ story:** the Day 148 proof of $3 \mid b_k$ used *the same* trick: pull the algebraic curve into Lagrange form and inspect the kernel. Here the kernel positivity is even cleaner — no substitution $F = 3G$ needed — because we work with $A$ instead of $F$.
