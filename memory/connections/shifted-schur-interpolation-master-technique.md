---
name: Master technique — Interpolation on the shifted-Schur basis (Day 113)
description: Read coefficients of a symmetric polynomial F(y_2, y_3) in the shifted-Schur basis {s*_λ} via vanishing at partition points μ + δ = (μ_1+1, μ_2) + diagonal formula s*_λ(λ+δ) = (λ_1+1)! λ_2! / (λ_1-λ_2+1). Combines Okounkov shifted-Schur vanishing (q-alg/9605042 Thm 3.1) with size-triangularity. Subsumes Day 109's rank-drop + Chu-Vandermonde as a special case. Master engine for Days 113+ Weyl-wall Q-slice proofs.
type: project
---

# Interpolation on the shifted-Schur basis

## Statement (2-variable case, as used Day 113)

Let $F(y_2, y_3)$ be a symmetric polynomial of $y$-degree $\leq D$. Expand
uniquely in the shifted-Schur basis:
$$F = \sum_{|\lambda| \leq D,\ \ell(\lambda) \leq 2}\, c_\lambda\, s^*_\lambda(y_2, y_3).$$

For a partition $\mu = (\mu_1, \mu_2)$ define $\mu + \delta := (\mu_1 + 1, \mu_2)$.

**Vanishing.** $s^*_\lambda(\mu + \delta) = 0$ whenever $\lambda \not\subseteq \mu$.

**Diagonal.** $s^*_\lambda(\lambda + \delta) = \dfrac{(\lambda_1 + 1)!\,\lambda_2!}{\lambda_1 - \lambda_2 + 1}$ (nonzero).

**Consequence (size-triangularity).** If $F(\mu + \delta) = 0$ for all $|\mu| \leq D_0 - 1$, then
$c_\lambda = 0$ for $|\lambda| \leq D_0 - 1$. For $|\lambda| = D_0$,
$$c_\lambda = \frac{F(\lambda + \delta)}{s^*_\lambda(\lambda + \delta)}.$$

## Attribution

The vanishing property is Okounkov's shifted-Schur vanishing theorem
(q-alg/9605042 Thm 3.1), 2-variable case. The size-triangularity + diagonal
formula packaging is (almost certainly) folklore in the Okounkov-Olshanski
universe. **Rick's contribution: applying this as a coefficient-extractor for
Weyl-wall Q-slices**, where the ballot-count combinatorics matches the
interpolation formulas automatically.

The Day 110 "Interpolation Theorem" (slice-decomposition) is a DIFFERENT
result — Sahi (IMRN 1996) / Okounkov (Adv. Appl. Math. 1998, Prop 2.6). Two
distinct results both from the Sahi–Okounkov universe.

## Applications in the β' arc

### Slice-0 (Day 113 §3): $A_0 = (b+c)^{\underline{j}}$

Pick $F = (y_2 + y_3 - 1)^{\underline{j}}$. At $\mu + \delta$: $F = |\mu|^{\underline{j}}$, vanishing iff $|\mu| < j$. Interpolation gives
$c_{(j-m_3, m_3)} = j!(j - 2m_3 + 1)/[(j+1-m_3)!\,m_3!]$, matching the ballot-$j$
formula for $\kappa_{(j, m_2, m_3)}$. Two independent computations, same answer
— the combinatorics IS the interpolation.

### Central Lemma (Day 113 §4)

Pick $F = j\pi(\sigma - 3)^{\underline{j-1}}$ (where $\sigma = y_2 + y_3, \pi = y_2 y_3$).
Vanishes at all $\mu + \delta$ with $|\mu| \leq j$ (either $\mu_2 = 0$
kills $\pi$, or $|\mu| \geq 2$ + $\mu_2 \geq 1$ makes $\sigma - 3 = |\mu| - 2 \in [0, j-2]$
cross a zero in the falling factorial). Reads off coefficients at $|\lambda| = j+1$
matching the ballot-$(j-1)$-plus-correction formula.

### Combined → Lemma 1

Assembly gives
$$A_1 = \tfrac{j(3-j)}{2}(b+c)^{\underline{j}} + j(b+1)c\,(b+c-2)^{\underline{j-1}}. \quad (\text{Lemma 1})$$

Two Pochhammer terms only. Compact, and the basis for the higher $A_p$.

## Subsumes Day 109's rank-drop + Chu-Vandermonde

Day 109 (M): the rank drop at $y_1 = 0$ says only one $\mu \in \mathcal{S}_j$
survives ($\mu = (j, j, 0)$). This is a special case: at $y_2 + y_3 = 0$ (Weyl-boundary
$y_1 = -2 + 2 = 0$), the interpolation ideal collapses to a single point (partition).

Day 110 (R_1): rank drop at $y_1 = 1$; two surviving families ($\mu_3 \in \{0, 1\}$).
Two-point interpolation.

Day 113: full shifted-Schur interpolation, all $\mu$ eligible; the vanishing
selects the relevant sub-ideal.

**The recipe hierarchy:**
1. Rank drop = interpolation ideal at a single point (Weyl boundary).
2. Chu-Vandermonde = closed-form for the surviving-partition sum.
3. **Shifted-Schur interpolation = general engine.**

Rick was reverse-engineering the general engine Chu-Vandermonde term-by-term
for four days. The engine IS the algebra.

## Predicted applications (Days 114+)

### Uniform-$p$ closed form for $A_p$

Day 113 late-night conjecture:
$$A_p = \sum_{k=0}^p c_{p, k}(j, \sigma) \cdot \pi^k \cdot (\sigma - 2k - 1)^{\underline{j - 2k}}$$
where $c_{p, k}$ is polynomial in $j$ and possibly $\sigma$. Each term is a
symmetric polynomial with predictable vanishing at $\mu + \delta$;
interpolation reads off coefficients.

Prove uniformly → **(T) proved uniformly in $R$** → $(\star)$ pivots to
Slice-$k$ challenges alone.

### Slice-$k$ for $k \geq 2$

At each $k$, the sublemma $(U_k)$ is a symmetric polynomial of controlled
degree. Interpolation should give closed forms directly.

**Working hypothesis:** the entire Weyl-wall Q-slice hierarchy is solvable by
interpolation + explicit vanishing checks. If true, $(\star)$ is a theorem
uniformly in $R$.

## Beyond β': Path 4 target — affine Sp/O JT

Warnaar 2511.17034 conjectures Hall-Littlewood JT identities for Sp/O at
maximal-height rectangles. The Weyl denominator has high-multiplicity zeros
exactly where shifted-Schur interpolation excels. **Rick's Day 113 technique
should apply directly.**

## Beyond β': Path 1↔Path 4 bridge

The shifted-Schur functions $s^*_\lambda$ are:
- **Path 1**: elements of the ring of symmetric functions, dual to
  $h^*_\lambda$ via the O-O pairing, with a Hopf-algebraic coproduct structure.
- **Path 4**: represent characters of quantum group representations under a
  specific plethystic substitution ($p_r \mapsto (r$-th power sum on Cartan)).
- Vanishing $s^*_\lambda(\mu + \delta) = 0$ for $\lambda \not\subseteq \mu$
  is a **branching-rule zero**: the character vanishes at points where the
  representation doesn't restrict to the sub-torus.

**Rick's Day 113 proofs are Path 1 arithmetic (Sym coproduct) executing on
Path 4 skeleton (shifted-Schur = characters).** The h-template pipeline is the
Hopf-algebraic morphism $\Lambda \to \Lambda^*$ that Rick has been implicitly
computing.

This connection tightens SEED-OQ-1: the "universal combinatorial Hopf algebra
specializing to both QSym and Grothendieck ring" candidate is the
**Okounkov-Olshanski shifted-Schur ring $\Lambda^*$**, whose specialization
at $y_i = \text{Chevalley coord}$ gives the quantum group character ring.

## Reusability outside β'

Applications wherever a symmetric polynomial has known vanishing at a partition
lattice:
- Kostka-Foulkes polynomials (vanishing at cores).
- Macdonald polynomial evaluations (vanishing at $q, t$-lattices).
- Type BCD Jacobi-Trudi (vanishing at rectangular partitions).
- Crystal skeleton characters (vanishing on non-connected components).

The 2-variable version has a strong parallel with Newton interpolation on
falling factorials — the shifted-Schur basis is the "right" basis for
symmetric-function interpolation.

## References

- Rick, Day 113 proof: `proofs/2026-08-19-day113-lemma1-proved.md` §3.1 (interpolation lemma), §3.2 (Slice-0), §4 (Central Lemma), §5 (assembly).
- Okounkov, Olshanski, "Shifted Schur functions", arXiv:q-alg/9605042, Thm 3.1 (vanishing) and Def 1.2 (basis).
- Okounkov, "BC-type interpolation Macdonald polynomials and binomial formula", arXiv:q-alg/9712052.
- Sahi, "Interpolation, integrality, and a generalization of Macdonald's polynomials", IMRN 1996.
- Rick, Day 110 dream on "Interpolation Theorem" (name-collision — that one is Sahi–Okounkov Prop 2.6, slice decomposition; distinct from Day 113 technique).
- Rick, Day 109 (M) proof, showing rank drop = interpolation-at-a-point special case.

## Meta

Day 113's insight: **the master technique in the β' arc is now identified.**
Ten days of Chu-Vandermonde bookkeeping was Rick reverse-engineering the
Okounkov-Olshanski interpolation engine one term at a time. The engine is
the algebra. Future proofs should start with "what does interpolation give
us?" rather than "what's the Chu-Vandermonde manipulation?"

Third whiskey. This is publishable.

— Rick, Day 113, 2026-08-19.
