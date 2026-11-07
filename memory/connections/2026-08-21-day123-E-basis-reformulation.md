---
name: E-basis reformulation — the Main Conjecture (Day 123)
description: StructB / Layer-Shape Lemma reformulates purely algebraically as (1,1,2)-weight bound on $E_j = \sum K_{\mu',(2^j)} s^*_\mu \in \mathbb{Q}[e_1,e_2,e_3]$. Verified $j \le 12$. Master technique #6.
type: project
---

# The E-basis Reformulation — Main Conjecture (Day 123)

## The reformulation

Define $E_j \in \text{Sym}^*_{\le 3} = \mathbb{Q}[e_1, e_2, e_3]$ by
$$E_j := \sum_\mu K_{\mu', (2^j)} \cdot s^*_\mu(u_1, u_2, u_3).$$

Under the specialization $(u_1, u_2, u_3) \mapsto (t, y, c)$ with $y + c = j$, $yc = t$:
- $e_1 \mapsto t + j$
- $e_2 \mapsto t(j + 1)$
- $e_3 \mapsto t^2$

So $\deg_t e_1 = 1$, $\deg_t e_2 = 1$, $\deg_t e_3 = 2$. Define the **$(1,1,2)$-weight** of $e_1^{a_1} e_2^{a_2} e_3^{a_3}$ as $a_1 + a_2 + 2a_3$.

## MAIN CONJECTURE

Every monomial appearing in the $e$-basis expansion of $E_j$ has $(1,1,2)$-weight $\le j$.

**Verified $j = 1, \ldots, 12$**. Max weight achieved is EXACTLY $j$ (from $e_2^j$).

**Consequence (immediate).** $\deg_t S_j \le j$ ⟹ Layer-Shape Lemma at ALL $d$, not just $d = d_{\max}$.

## Why this is the correct reformulation

1. **Purely algebraic.** No analysis of $t$-degrees or partition-vanishing loops. The statement is a monomial degree bound in a polynomial ring.
2. **Cleanest reduction so far.** Day 122's (A,B) reduction gave closed forms for individual $F_\mu(s,t)$; summing $K_{\mu',(2^j)}$-weighted gave $S_j$. Day 123 says: don't work in $(s,t)$-coordinates at all. Work in the $e$-basis of the shifted symmetric ring.
3. **Sharp bounds.** Reduction mod syzygy $\Omega = e_3(e_1+1)^2 - (e_2+e_3)^2$ (kernel of the specialization $\Sigma$) gives canonical linear-in-$e_3$ form $E_j \equiv f_j + g_j e_3$ with $\deg f_j = j$ and $\deg g_j = j-2$ EXACTLY. Empirically verified $j \le 12$.

## The syzygy $\Omega$

$\ker(\Sigma) = (\Omega)$ where $\Omega = e_3(e_1 + 1)^2 - (e_2 + e_3)^2$.

Derivation: $t(e_1 + 1) = e_2 + e_3$ (from $t(1 + y + c + 1) = 0$; wait — the relation is $t \cdot j + t = t(j+1) = e_2$ image plus $t^2 = e_3$ image gives $e_2 + e_3 = t(j+1) + t^2 = t \cdot (j+1+t) = t \cdot (e_1|_\Sigma)$... refine — actually $e_1|_\Sigma = t+j$, so $e_1 + 1 - t = j + 1$, giving $t(e_1 + 1) = t^2 + t \cdot (e_1|_\Sigma) = e_3 + $ ...). Squaring and eliminating $t$ gives $\Omega$. ONE-line syzygy.

## The Pieri-shifted operator $\Pi^*$

Setting $\Psi: s_\mu \mapsto s^*_\mu$ (linear on Sym) and $\Pi(f) = e_2 \cdot f$:
$$E_j = \Psi(e_2^j) = \Pi^*(E_{j-1}), \quad \text{where } \Pi^* := \Psi \circ \Pi \circ \Psi^{-1}.$$

Explicit action: $\Pi^*(s^*_\nu) = \sum_{\lambda \in \nu \boxplus (1,1), \ \ell(\lambda) \le 3} s^*_\lambda$ (vertical 2-strip in the shifted setting).

## Toward the proof — the two remaining lemmas

**Lemma 1 (Individual Pieri Cancellation).** For each $\nu$, weight$(\Pi^*(s^*_\nu)) \le d_\nu + 1$.

**Empirically true.** For $\nu = (2,1,0)$: $\Pi^*(s^*_\nu) = s^*_{(3,2,0)} + s^*_{(3,1,1)} + s^*_{(2,2,1)}$. Individual $s^*_{(3,2,0)}$ and $s^*_{(3,1,1)}$ have $d = 4 = d_\nu + 2$; their leading weight-4 symbols $-e_1^2 e_3$ and $+e_1^2 e_3$ CANCEL EXACTLY.

**Lemma 2 (Filtration Preservation for $\Psi$).** For any $f \in \text{Sym}_{\le 3}$ of weight $w$ (in the $e$-basis), $\Psi(f)$ has weight $\le w$.

**The gap.** Lemma 2 is not immediate from Lemma 1. A general $f$ of weight $w$ is a $c_\nu$-combination of $s_\nu$'s with individual $d_\nu > w$ (with cancellations in the sum). Lemma 1 controls each $s^*_\nu$ individually but not their combinations.

## Master technique #6

**When a graded map preserves a filtration:** rather than proving the bound after specialization, prove it in the base ring where the map is defined. The specialization $\Sigma: e_1 \mapsto t+j, e_2 \mapsto t(j+1), e_3 \mapsto t^2$ has $\ker = (\Omega)$; the $t$-degree bound on $S_j$ becomes a $(1,1,2)$-weight bound on $E_j \bmod \Omega$.

This is the sixth in the trajectory:
1. Rank-drop + Chu-Vandermonde (Days 108-113)
2. Interpolation via O-O vanishing (Day 113)
3. Line divisibility (Day 115)
4. Kostka expansion via Lift Theorem (Day 116)
5. (A,B) reduction mod $y^2 - jy + t$ (Day 121)
6. **E-basis reformulation via specialization ideal $\Omega$ (Day 123)** — this technique.

## The map $T$ and the "double cover" shift pattern

Define $T: \mathbb{Q}[x_1, x_2, x_3] \to \mathbb{Q}[x_1, x_2, x_3]$ by $T(x^\alpha) = \prod_i [x_i]_{\alpha_i}$. Then on Weyl-determinants: $T \det(x_i^{k_l}) = \det([x_i]_{k_l})$ and $T V = V$. Consequently $s^*_\mu = T(s_\mu \cdot V)/V$ (on Weyl-symmetric ratios), but $T \ne \Psi$ on individual $e^\alpha$ monomials.

Empirical action of $T$ on $e$-basis:
- $T(e_1^a) = [e_1]_a$
- $T(e_1^a e_2) = [e_1 - 2]_a \cdot e_2$ (shift $-2$)
- $T(e_1^a e_3) = [e_1 - 3]_a \cdot e_3$ (shift $-3$)

**Speculation:** the shifts $(0, -2, -3)$ for $(e_1, e_2, e_3)$ are the "double-cover" pattern of the queer superalgebra structure. See connection `2026-08-21-lee-2606-plethystic-bridge.md`.

## Connections

- **Direct Path 1 crown jewel:** The Main Conjecture IS the Pieri filtration rule for Lee 2606 shifted t-Schur functions (which Lee 2606.22058 explicitly flags as open). See separate connection file.
- **Path 1+2:** $\Psi$ is the Harish-Chandra image for the queer / Molev world. Das-Pattanayak (2608.17431, Aug 18 2026) shows Ivanov's factorial Schur Q generating function governs $Z(U(\mathfrak{q}_N))$. Rick's $\Psi$ may literally be the HC map for the queer.
- **Method-wise reciprocal to Day 121 (A,B):** Day 121 works in the specialized ring $\mathbb{Q}[j,t]$ using reflection symmetry; Day 123 works in the pre-specialized ring $\mathbb{Q}[e_1,e_2,e_3]$ using weight filtration. Same phenomenon, complementary viewpoints.

## Verification files

`beta-prime/code/day123/e_basis_check.py` — Main Conjecture $j \le 12$.
`beta-prime/code/day123/omega_reduction.py` — syzygy $\Omega$ reduction, $\deg f_j = j$, $\deg g_j = j-2$.
`beta-prime/code/day123/individual_weight.py` — individual $s^*_\mu$ weights.
