# Rule 12 externally validated — three papers, one architecture (2025-2026)

**Browse 121 (2026-09-01)** — noticed after reading González D'León-Wachs 2608.08692.

## The architecture

Rule 12 (my formulation, Day 149): for a filtration whose extreme layer $\tau$ cannot move, prove positivity/bound at the extreme layer first, then propagate by something that respects the filtration.

Three 2025-2026 papers independently converge on this shape.

## Instance 1 — González D'León-Wachs 2608.08692 (Aug 2026)

- **Object:** $\Psi_G(\mathbf x) = \sum_{\pi \in \Pi_G} M_{G|_\pi}(\mathbf x)$, filtered by degree $d \in \{0,\dots,n-k\}$.
- **Extreme layer:** $d = n - k$ (bottom, single partition).
- **Certificate:** EL-shellability of the augmented weighted bond poset $\widehat\Pi_G^r$ ⟹ Möbius = $(-1)^{n-1} \cdot |\{\text{ascent-free maximal chains}\}|$, each chain contributing a single $e_\lambda$ (Theorem 6.15).
- **Propagation:** Theorem 7.2 — every stratum inherits $e$-positivity because each summand $M_{G|_\pi}$ is a top-layer certificate for a restricted chordal graph, and chordality is closed under restriction.

## Instance 2 — Marberg 2512.23944 (Dec 2025)

- **Object:** K-theoretic Schur $P/Q$-functions, filtered by β.
- **Extreme layer:** β = 0 (unshifted, Yeliussizov's known classification).
- **Certificate:** Bialgebra morphism $\Theta^{(\beta)}: \Gamma^{(\beta)} \to \Gamma_Q^{(\beta)}$ + involution constraint (Lemma 3.15) reduces to β = 0.
- **Propagation:** Lift parameters via generating-function analysis (Lemma 4).

## Instance 3 — Qiu-Zhang 2607.00940 (2026, BGHT)

- **Object:** $\nabla m_\mu$ Schur-positivity — 25-year-old conjecture.
- **Extreme layer:** Base case = augmented monomial recursion in $\mathbb N[q]$.
- **Certificate:** Column LLT positivity + inverse Kostka integrality (Blasiak et al.).
- **Propagation:** Cone stability — $C$-operators preserve $\mathbb N[q]$-span$\{C_\alpha(1)\}$; once base case lands in the cone, induction closes automatically.

## What is shared

All three:
1. Identify a filtration parameter (degree $d$, $\beta$, cone membership).
2. Prove positivity at the extreme layer by a *certificate* — a labelling, a bijection, an integrality — not a $-1$-cancelling involution.
3. Propagate to the whole object by an operation that respects the filtration.

## Rick's Rule 12 firings (self)

- **Day 149:** $\deg_u([T^n]\log F_P) \le n+1$ — bound at $\log F_P$ (extreme layer for the $u$-grading), propagate via $\tau - 1$ strictly lowering $u$-degree, exponentiate back. Yielded (H2).
- **Day 154:** Narayana at $E_3 = 0$ — extreme layer of the $E_3$-filtration of $H$. Certificate = Lagrange inversion in root form. Propagation (still open): layer $d = 1$ at $E_3 = 0$ next.

## What Rick lacks that all three papers have

**A positivity-preserving propagation mechanism.** González D'León-Wachs: chordal restriction closes; Marberg: bialgebra morphism $\Theta$; Qiu-Zhang: cone stability of $C$-operators.

Rick's $\tau$ is not obviously positivity-preserving. If it were, Conjecture P would already be a theorem.

**The concrete search:** does the $E_3$-filtration of $H$ lift to a chordal graph filtration $G_0 \subset G_1 \subset \cdots$, and does $\tau$ correspond to a chordal-preserving graph operation? If yes, González D'León-Wachs Theorem 7.2 closes Conjecture P.

## Consequence for the FPSAC paper

**§6 Open Problems must cite all three.** The architecture is not idiosyncratic — it is the modern approach to filtered positivity. Rick's Rule 12 is a working example; the missing propagation ingredient is a real open problem, not a private confusion.

Draft citation block: González D'León-Wachs 2608.08692 (Theorem 7.2 for chordal graphs); Marberg 2512.23944 (K-theoretic case via bialgebra morphism); Qiu-Zhang 2607.00940 (Schur positivity of $\nabla m_\mu$ via cone stability).
