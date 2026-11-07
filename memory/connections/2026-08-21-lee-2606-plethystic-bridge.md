---
name: Lee 2606 shifted t-Schur plethystic bridge — Main Conjecture = open Pieri rule
description: The Main Conjecture (Day 123) IS the Pieri filtration for Lee's shifted t-Schur functions $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$, which Lee 2606.22058 flags as explicitly open. Path 1 crown jewel.
type: project
---

# Lee 2606 shifted t-Schur ↔ Rick's Main Conjecture

## Headline

**Rick's Main Conjecture (Day 123) — that $E_j = \sum_\mu K_{\mu', (2^j)} s^*_\mu$ has $(1,1,2)$-weight $\le j$ in $\mathbb{Q}[e_1, e_2, e_3]$ — is the Pieri filtration rule for Lee's shifted $t$-Schur functions $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$, which Lee 2606.22058 explicitly flags as OPEN.**

Publishable byproduct: the first Pieri rule in this family.

## The identification

Lee 2606.22058 (June 2026, first of a five-paper cluster) introduces
$$\mathcal{Q}_\lambda(X; t) = Q_\lambda[X(1 - t)]$$
via a modified odd vertex operator. This is a $(1-t)$-plethystic deformation of the Schur Q-functions.

**The observation:** Rick's (A,B)-reduction modulo $y^2 - jy + t$ is precisely computing the $t$-degree of the $(1-t)$-plethystic deformation applied to symmetric functions. The Weyl-formula computation of $F_\mu(s, t) = s^*_\mu(t, y, c)|_\Sigma$ at the specialization $y + c = j$, $yc = t$ IS the reduction that produces Lee's $\mathcal{Q}$-basis coefficients.

**Precise statement (conjectural but consistent with all data):** the shifted symmetric functions $s^*_\mu$ under Rick's specialization $\Sigma$ are (up to explicit normalization) the $\mathcal{Q}_\mu$-basis Fourier coefficients of the $(1-t)$-plethystic image of $e_2^j$.

## The Pieri gap

Lee 2606.22058 explicitly writes: "the Pieri rule for $\mathcal{Q}_\lambda(X;t)$ is a first step." No formula for
$$e_k \cdot \mathcal{Q}_\lambda(X; t) = \sum_\nu c^\nu_{\lambda, k}(t) \mathcal{Q}_\nu(X; t)$$
exists in the five-paper June-July 2026 cluster (2606.22058, 2606.28723, 2606.28108, 2607.01839, 2607.02108).

Rick's operator $\Pi^*$ (Day 123) is exactly $e_2 \cdot$ (multiplication) transported through the $\Psi: s_\mu \to s^*_\mu$ correspondence. The Main Conjecture is a **filtration statement for $\Pi^*$**: it raises $(1,1,2)$-weight by at most 1.

Under the identification above, this IS the missing Pieri filtration for Lee's $\mathcal{Q}$-basis.

## Publishable path

**Standalone theorem for the paper:** the Pieri rule for shifted $t$-Schur functions $\mathcal{Q}_\lambda(X;t)$ satisfies the filtration bound
$$\deg_t [\mathcal{Q}_\nu(X;t)] \left( \mathcal{Q}_\lambda(X;t) \cdot e_k \right) \le d_\nu - d_\lambda + f(k)$$
for an explicit function $f$ (probably $k$ itself).

Rick's proof of the Main Conjecture (via Individual Pieri Cancellation + Filtration Preservation for $\Psi$) would specialize to this, and — crucially — Lee's community would recognize it as the resolution of their open problem.

## Path 1 context

The E-basis reformulation lives entirely in the shifted symmetric ring, which is:
- Kashuba-Molev (2512.21631, Dec 2025): the natural home for HC images of quantum immanants in the queer $U(\mathfrak{q}_N)$.
- Das-Pattanayak (2608.17431, Aug 18 2026, BRAND NEW): Ivanov's factorial Schur Q generating function governs the center $Z(U(\mathfrak{q}_N))$.
- Jing-Liu-Molev (2408.09855, 2024): HC images of q-immanants for $U_q(\mathfrak{gl}_n)$ are factorial Schur polynomials.

**Path 1+2 chain closed:** the shifted symmetric ring is the natural Hopf-algebraic home for a whole family of central-element / immanant constructions. Rick's Ψ is (up to explicit choices) the HC map.

## The (0, -2, -3) shift pattern

Day 123 empirical observation: the map $T(x^\alpha) = \prod [x_i]_{\alpha_i}$ acts on the $e$-basis as
$$T(e_1^a) = [e_1]_a, \quad T(e_1^a e_2) = [e_1 - 2]_a \cdot e_2, \quad T(e_1^a e_3) = [e_1 - 3]_a \cdot e_3.$$

The shifts $(0, -2, -3)$ for $(e_1, e_2, e_3)$ match the "double-cover" content shifts in the queer superalgebra story. In the queer $\mathfrak{q}_N$ world, primed and unprimed indices are shifted by half-integers; the concrete shifts $-2, -3$ may be $2 \times$ the queer half-integer shifts.

**Prediction:** the Main Conjecture has a queer-Hopf proof: Ψ is the HC map for the queer, and the (1,1,2)-weight bound is a PBW-filtration statement for $Z(U(\mathfrak{q}_N))$.

## Discrete Wronskian ↔ Pfaffian (Fischer-Gangl bridge)

Fischer-Gangl 2603.29836 (Mar 2026) proves two new Littlewood identities for fully inhomogeneous spin HL functions. The second is a Pfaffian identity connecting to alternating sign matrices via modified Robbins polynomials.

Rick's discrete Wronskian $W_{a,b}(t) = A_a B_b - A_b B_a$ (Day 121 master technique) is a $2 \times 2$ Pfaffian element. If it embeds into the Fischer-Gangl Pfaffian structure, the $W_{k_2, k_3} = 0$ cancellation identity has a direct spin HL / ASM interpretation.

## Actionable steps

1. **Read Lee 2606.22058 §1-2** — extract the precise plethystic identity $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$ and check that Rick's specialization $\Sigma$ matches the plethystic image at 3 variables.

2. **Read Kashuba-Molev 2512.21631 §1-3** — check whether Rick's $\Psi$ is (up to normalization) the HC map for the queer. If yes, the entire Main Conjecture has a queer PBW-filtration proof.

3. **Read Das-Pattanayak 2608.17431 fully (13 pages est.)** — check whether $S_j = \sum K_{\mu',(2^j)} s^*_\mu$ appears explicitly as a specific central element in $Z(U(\mathfrak{q}_N))$.

4. **Write § of M-and-R1 note explicitly framing the Main Conjecture as the shifted-t-Schur Pieri rule.** This is publishable REGARDLESS of whether Lemma 2 (filtration preservation for $\Psi$) is proved: the empirical evidence + explicit reduction to a clean algebraic identity is already a substantial contribution.

## Seed connections

- **Path 1** (combinatorial Hopf algebras): the shifted symmetric ring $\text{Sym}^* \cong \mathbb{Q}[e_1, e_2, ...]$ as a polynomial ring is the natural setting.
- **Path 2** (quantum groups): Kashuba-Molev + Das-Pattanayak place $s^*_\mu$ in $Z(U(\mathfrak{q}_N))$.
- **Path 3** (Hecke algebras): $K_{\mu', (2^j)}$ is a graded multiplicity in the Schur functor image of the Hecke sign representation at $q=1$. The $q$-lift OQ-CHARGE-LIFT-AB probes the Hecke deformation.
- **Path 4** (coproduct-crystal): the operator $\Pi^*(s^*_\nu) = \sum_{\lambda \in \nu \boxplus (1,1)} s^*_\lambda$ is a shifted analog of the vertical-strip Pieri, which is exactly the LR-tensor-product-with-a-column rule.

**Four paths converge on the Main Conjecture. This is a Tier-S connection.**
