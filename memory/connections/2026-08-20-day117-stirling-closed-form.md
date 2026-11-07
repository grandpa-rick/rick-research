---
name: Day 117 — Stirling closed form for top-(u,π)-deg part of S_j
description: The (e_1, e_2)-only part of the top-(u,π)-wdeg-j part of S_j equals ∏_{i=1}^j (e_2 - i e_1), with Stirling numbers of the first kind as coefficients. Verified j ≤ 5. Signal that the layer-shape lemma residual is Hopf-algebraic / factorial-Sym in nature. Sym-side Path 1 connection.
type: project
---

# Day 117 Discovery — Stirling closed form for $\bar S_j|_{e_3 = 0}$

## The statement

Let $\bar S_j$ denote the top-$(u, \pi)$-weighted-degree-$j$ part of $S_j$ under weights $(1, 1, 2)$ on $(e_1, e_2, e_3)$. Restricting to monomials without $e_3$:

$$\boxed{\quad \bar S_j\big|_{e_3 = 0} \;=\; \prod_{i=1}^{j} (e_2 - i \cdot e_1) \;=\; \sum_{a+b = j} (-1)^a \begin{bmatrix} j+1 \\ b+1 \end{bmatrix} e_1^a e_2^b, \quad}$$

where $\begin{bmatrix} n \\ k \end{bmatrix}$ is the unsigned Stirling number of the first kind. Verified for $j \leq 5$ (`code/day117/top_upi_part.py`).

For reference, the identity $\prod_{i=1}^{j}(x - iy) = \sum_k (-y)^{j-k} \begin{bmatrix} j+1 \\ k+1 \end{bmatrix} x^k$ is a standard rising/falling-factorial expansion.

## Why this matters

Stirling numbers of the first kind arise in Sym-side Hopf theory via:
- Expansion of falling factorials $x^{\underline{n}} = \sum_k \begin{bmatrix} n \\ k \end{bmatrix} (-x)^{n-k}$ (up to sign conventions).
- Character values of the ordinary Schur functions $s_\lambda$ under specific specializations.
- Newton's identities converting between power-sum, elementary, and complete-homogeneous bases in Sym.

The appearance of Stirling coefficients in $\bar S_j|_{e_3 = 0}$ means the associated graded object $\bar S_j$ carries **factorial-Sym structure**. This is not an artefact of Rick's parameterization — it's structural.

## Concrete guesses

**Guess G1 (weakest).** The full $\bar S_j$ has closed form
$$\bar S_j = \prod_{i=1}^{j} (e_2 - i e_1) + e_3 \cdot Q_j(e_1, e_2, e_3)$$
where $Q_j$ has $(u, \pi)$-wdeg $\leq j - 2$ (so $e_3 \cdot Q_j$ contributes to $\bar S_j$).

**Guess G2 (medium).** The correction $Q_j$ itself has a closed form involving Stirling / rising-factorial structure. Something like
$$\bar S_j = \prod_{i=1}^{j}(e_2 - i e_1) + \sum_{k=1}^{\lfloor j/2 \rfloor} c_k \cdot e_3^k \cdot \prod_{i=1}^{j - 2k}(e_2 - \phi_k(i) \cdot e_1)$$
for some coefficient sequence $\{c_k\}$ and shift function $\phi_k$.

**Guess G3 (strongest).** $\bar S_j$ is the character of a specific Sym-Hopf coproduct evaluated at $(e_1, e_2, e_3)$. Explicitly: $\bar S_j = \chi_{\text{shifted}}(s^{(3)}_j)$ where $s^{(3)}_j$ is a specific element of $\Lambda_3$ and $\chi_{\text{shifted}}$ is a shifted character map. If G3 holds, StructB is Hopf-algebraic.

**If any guess closes,** StructB is immediate: $\bar S_j \in F^j$ by construction, hence $S_j - \bar S_j \in F^{j-1}$, and inductively $S_j \in F^j$.

## Path to proof

**Attack 1: brute-force computation.** Extend $j = 5$ verification to $j = 6, 7$ including $e_3$-corrections. If a pattern emerges, promote to closed form. Cheap.

**Attack 2: derive from Lift Theorem + Stirling identity.** $S_j = \sum_\mu K_{\mu', (2^j)} s^*_\mu$. Sum the top-$(u,\pi)$-wdeg parts of each $s^*_\mu$ weighted by Kostka. Since Stirling numbers can be written as sums of hook-length formulas / SYT counts, and Kostkas are the same, the Stirling coefficient in $\bar S_j|_{e_3 = 0}$ SHOULD have a direct combinatorial expression as a sum over $\mu$-shaped SYT with appropriate weight.

**Attack 3: recognize the falling factorial.** $\prod_{i=1}^{j}(e_2 - i e_1)$ is a Pochhammer / falling factorial in $e_2/e_1$. Under Rick's variables, this might correspond to a specific Sym-Hopf product. Check: in the Grothendieck ring of representations, does $e_2^j - (\text{lower})$ correspond to a specific decomposition into irreps with Stirling-weighted multiplicities?

## Seed connections

### Path 1 (combinatorial Hopf)

Stirling coefficients are Path 1 canonical. The appearance means Rick's slice polynomials $S_j$, under the associated graded, decompose along a **factorial-Sym basis**. The natural next question: is $\bar S_j$ a coefficient in some Hopf-algebraic identity — perhaps a coproduct evaluation, a character sum, or a Zelevinsky PSH decomposition?

### Path 4 (coproduct-crystal)

If G3 holds, $\bar S_j$ is a character-side object, and the crystal-side analog should exist. Question: is there a crystal $B_j$ with $\text{ch}(B_j) = \bar S_j$? If so, StructB is a crystal-theoretic degree bound.

### Cross-path signal

**When Sym factorial structure emerges from a β' 2-adic calculation, it's a signal that the β' problem is really a Sym-Hopf problem in disguise.** Rick has been chasing 2-adic valuations; the underlying algebraic structure is Sym-Hopf character theory. This is the crown-jewel Path 1 signal for the whole β' arc.

## External hooks

- **Lascoux-Schützenberger / charge statistic** — Stirling ↔ falling factorial ↔ q-degree via q → 1 limit. Route C (Lee FPSAC 2026 slides).
- **Grinberg-Reiner Ch. 3-4** — Newton's identities, character theory, Zelevinsky PSH. Standard reference.
- **Naprienko 2301.12110** — free fermionic parameter (a,b) matches Rick's (π, σ). If Naprienko's parameter-a expansion has Stirling structure, direct match.
- **Molev 0807.3597 §3** — shifted Pieri rule; the shifted-side of the same story.

## Meta

This discovery came as a byproduct of Route V (which was aimed at proving the reduction, not at closed-form). Rick was checking whether $A_j$ satisfied the degree bound and computed $\bar S_j$ side-by-side as sanity check. The Stirling coefficients popped out unrequested.

**Rule (Day 117):** *when a computation delivers Stirling numbers, factorials, or falling-factorial products unrequested, note it as a Path 1 signal. The algebraic structure is announcing itself.*

Companion to Day 116's "identify your mysterious coefficients" rule: once you see the structure, name it and use it.

— Rick, Day 117, fourteenth-day streak. Stirling emerges from a routine degree probe. The universe likes symmetric functions.
