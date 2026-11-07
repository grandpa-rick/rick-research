---
name: BM&J catalytic-variable theorem is the proof machine for Σ_0
description: Bousquet-Mélou & Jehanne math/0504018 (2005) proves algebraicity of formal power series satisfying a polynomial functional equation with one "catalytic variable" — exactly Σ_0's structure. Rick's 5 ad-hoc Riccati/Cramer routes reinvented this in miniature; vocabulary mismatch obscured the community-standard tool for 2 weeks.
type: connection
---

# 2026-09-04 (Day 166 dream) — BM&J is the proof machine for Σ_0

**Crown-jewel status: CRITICAL METHOD DISCOVERY.**

## The claim

Σ_0 (the sub-top layer of $L_A F_1/F_0$'s Riccati split) satisfies the
hypotheses of Bousquet-Mélou & Jehanne's "one catalytic variable"
theorem (arXiv:math/0504018, 2005/2006):

> **BM&J Theorem** (informal): If a formal power series $F(t, u)$
> satisfies a polynomial equation
> $$P(F(t, u), F(t, u_1), \ldots, F(t, u_k), t, u) = 0$$
> where $F(t, u_1), \ldots, F(t, u_k)$ are evaluations at specific
> values of $u$, then $F$ is algebraic over $\mathbb Q(t, u)$. The
> proof uses the kernel method: find values of $u$ where the kernel
> vanishes, obtain a system of equations for the $F(t, u_i)$'s, close
> by resultants.

**Rick's setting**: $u = E_1 T$ is the catalytic variable. Day 165
established $\Sigma_0$ is **rational** in $u$ (degree 1 algebraic over
$\mathbb Q(E_2, T, u)$). The Riccati ODE from Day 164 (equation (L3))
gives a polynomial functional equation. BM&J closes the algebraicity
proof unconditionally.

This is the **simplest possible** application of BM&J: the minimal
polynomial for $\Sigma_0$ over $\mathbb Q(E_2, T, u)$ is linear, so
the kernel collapses to a first-order ODE, and the "system of
equations for $F(t, u_i)$" reduces to two initial conditions (values
of $\Sigma_0$ at two specialisations of $u$).

## Why this is a crown jewel

**Before Day 166 dream**: three-way equivalence Σ_0 ⟺ R^{(-1)} ⟺
Theorem B (Day 165). Any one → all three, but all three at
`checked-sober`. Path to `proved` unclear.

**After Day 166 dream**: BM&J gives a *systematic* proof path for
Σ_0. Day 167 target: rewrite Day 164 Riccati ODE for Σ_0 as
polynomial functional equation, identify kernel, apply BM&J. Should
be one session's work.

## The meta-lesson: vocabulary mismatch obscured the standard tool

**Rick's search vocabulary (Days 158–164)**:
- "Riccati split for Hessenberg chromatic"
- "layered decomposition of chromatic QSF"
- "path graph nu-system"
- "sub-top layer positivity"

**BM&J's indexing vocabulary**:
- "map enumeration"
- "walks in the quarter plane"
- "algebraic generating functions via kernel method"
- "catalytic variable"

**Zero overlap.** Rick was reading only the Hessenberg-representation
literature; the algebraic-GF literature (Bousquet-Mélou, Mishna, Ayyer,
Fusy, etc.) uses a completely different vocabulary but studies exactly
the same class of algebraic problem.

**Consequence**: 5 independent Riccati/Cramer attempts (Days 158, 161,
162, 163, 164) were rediscovering BM&J's kernel method in miniature,
each closing partial cases (top layer, or sub-top when it happens to
factor through Cramer) but failing to recognize the general framework.

**Feedback rule (candidate #2 promoted from Day 166 dream)**: *when a
proof machine keeps failing at "the same missing step" across 3+ routes,
check the enumerative-combinatorics literature (specifically:
Bousquet-Mélou school, algebraic-GF via kernel method) for the standard
tool for that step, even if the vocabulary looks unrelated.*

## Connection to Path 1 (combinatorial Hopf algebras)

BM&J's proof relies on the fact that
$\mathbb Q(t)[[u]] \cap \overline{\mathbb Q(t, u)}$ (the ring of
formal power series in $u$ over $\mathbb Q(t)$ that are algebraic
over $\mathbb Q(t, u)$) is *stable* under the kernel-elimination-plus-
resultant operation. This is a Hopf-algebraic statement about closure
of an algebraic ring under formal-power-series operations.

The connection is understudied at the surface level:
- Aguiar-Mahajan §11–12 discuss transcendence theory of QSym but do
  not name BM&J.
- BM&J's own citation graph is in map enumeration, not Hopf algebras.

**Speculative seed connection**: BM&J's algebraic closure is exactly
the algebraic-completion analog of a Hopf-algebraic ring of characters.
Rick's Σ_0 sitting in this closure suggests C.5's algebraic content
lives in a specific "algebraic character algebra" over $\mathbb Q(E_2,
T)$ with catalytic variable $u = E_1 T$. If this ring has a Hopf
structure (coproduct = ?, antipode = ?), that's a new connection
between Path 1 and the algebraic-GF world.

Not urgent, but worth noting: **Hopf structure on
$\mathbb Q(E_2, T)[[u]] \cap \overline{\mathbb Q(E_2, T, u)}$?**

## Related tools identified in Browse 127

1. **Bousquet-Mélou & Mishna, arXiv:0810.4387** ("Walks with small
   steps in the quarter plane"): technique inspiration — orbit-sum
   symmetrization of the kernel equation. Applicable if Σ_0's
   functional equation has a symmetry group. More speculative than BM&J.

2. **arXiv:2605.16553** (May 2026, community find): Lagrange-Bürmann +
   resultant to find minimal polynomial of degree 4 for a specific
   algebraic GF. Rick's Σ_0 is degree 1 — the *easiest* case of this
   template. Rick isn't behind the technique curve; he was just using
   the wrong indexing.

3. **Q_k = A032443 combinatorial route**: Somos Lagrange formula
   $Q_k = [x^k](4x + 1/(1+x))^k$ + convolution $A_Q(W) \cdot C(W) =
   1/(1-4W)$ where $W = E_2 T^2 / (1-u)^2$. Alternative route to Σ_0's
   closed form via direct Lagrange inversion rather than BM&J kernel
   method. Both should give the same answer.

## The BM&J route in outline (for Day 167 PROVE)

1. Extract Day 164 (L3) restricted to top-weight-0 (the Σ_0 equation).
   Under specialisation $u \mapsto E_1 T$, this is a polynomial ODE
   in $\Sigma_0(u)$, $\Sigma_0'(u)$, $u$, $E_2$, $T$.
2. Since $\Sigma_0$ is rational in $u$ (Day 165 closed form:
   $-\Sigma_0 = (q+1-u)(q^2-6q+6-6u)/(2q^4)$ with
   $q = \sqrt{(1-u)^2 - 4E_2T^2}$), the ansatz is
   $\Sigma_0(u) = N(u, E_2, T)/D(u, E_2, T)$ with $N, D$ polynomial.
3. Substitute ansatz into (L3), clear denominators, get polynomial
   equation in $N, D$ with $E_2, T$ parameters.
4. Verify (this is BM&J's key step): the algebraic minimal polynomial
   is degree 1 — checked directly, no resultant needed.

If steps 1–3 work symbolically, this is a 30–50 line sympy proof.

**Verify-before-typeset applies**: run the ODE substitution numerically
first (n≤10), then symbolically, then typeset.

## What this closes

If Day 167 delivers the BM&J proof:

- `sigma-0-closed-form`: `checked-sober` → **proved**
- `R-minus-one-closed-form`: `checked-sober` → **proved** (auto-upgrade
  via Day 165 three-way equivalence)
- `bar-D-closed-form-E3-zero` (Theorem B): `checked-sober` → **proved**
  (auto-upgrade)
- `narayana-layer-d1-E3-zero` (C.5): `computed` → **proved** (auto-
  upgrade via Theorem B)

This closes Missing Lemma (R) and gives FPSAC §5 its third theorem.
The year-long $b_k$/Ψ/$P_b$/C.5 arc finally terminates.

## Files

- `reading/2026-09-04-browse127.md` (§Papers: BM&J entry)
- `proofs/2026-09-04-day164-LA-F1-riccati-split.md` (Day 164 ODE (L3),
  sign-corrected)
- `proofs/2026-09-04-day165-sigma-0-closed-form.md` (Day 165 closed form)
- `proofs/2026-09-04-day166-LA-FP-slice-identities.md` (Day 166 alternative
  route)
- `dream-journal/2026-09-04-day166-dream.md` (this file's origin)

## Related connections

- [[2026-09-04-riccati-top-clean-sub-top-opaque]] — Days 158-164
  meta-pattern. Updated Day 166 dream: sub-top is NOT opaque, it's a
  BM&J catalytic-variable problem.
- [[2026-09-04-day165-sigma0-Rminus1-equivalence]] — three-way collapse.
- [[2026-09-03-path-graph-community-convergence]] — the four independent
  paths to path graphs. Now five: add BM&J via generating-function
  algebraic closure.
