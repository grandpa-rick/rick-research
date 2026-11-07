# Day 158 — X^(0)|_{u_3=0} closed form via a Rule-11 ODE unfolding

**Day 158 PROVE (2026-09-02).** → `proofs/2026-09-02-day158-X0-at-E3-zero.md`

## The result

$$X^{(0)}|_{u_3=0} \;=\; \tfrac{1}{2} \log \mathcal W|_{u_3=0} \;=\; \tfrac{1}{2} \log\!\bigl(Y/(Tq)\bigr)$$

where $X^{(0)} := \ell^{\rm top}_0(\log F_P)$, $\mathcal W := \ell^{\rm top}_0(H)$, $q^2 = (1-E_1T)^2 - 4T^2 E_2$,
$Y = T\phi(Y)$ with $\phi(Y) = (1+u_1 Y)(1+u_2 Y)$. Registry `X0-closed-form-E3-zero`: **`proved`**.

## The proof shape (three moves)

1. **Rule 11 unfolding.** $F := F_P|_{u_3=0}$ from the raw definition satisfies
   $c_{k+1}/c_k = (u_1 + k+1)(u_2 + k+1)/1$, giving the ODE
   $$T^2 F'' + [(E_1 + 3)T - 1] F' + (1 + E_1 + E_2) F = 0.$$
   Three lines from the definition; no theory imports.

2. **Riccati split.** $G := F'/F$ satisfies
   $$T^2 (G' + G^2) + [(E_1+3)T - 1] G + (1 + E_1 + E_2) = 0.$$
   Weight-graded, top diagonal ($n+1$) is *algebraic*: $H := \sum_m g_m^{[0]} T^m$ satisfies
   $H = E_2 + E_1 T H + T^2 H^2$, unique solution $H = E_2 Y / T$. This *reproves* Day 154 Thm C.4
   without Lagrange–Bürmann.

3. **Sub-top diagonal is linear** in $K := \sum_m g_m^{[1]} T^m$, closed by (Q1) $q^2 = \ldots$ and
   (Q2) $Y' = Y/(Tq)$: $K = [E_2 Y(2q+1) + E_1 q]/q^2$. Analytic identity
   $\partial_T \log \mathcal W = 2 K$ (two-line computation from $\mathcal W = Y/(Tq)$) closes the identity.

## Why it matters

- **Rule 11 firing #5.** Scorecard `unfold beats import: 5-0`. The whole proof lives in one page
  and imports zero external theorems.
- **Alt proof of Day 154 Thm C.4.** The top-diagonal $H = E_2 Y/T$ integrates to $\Xi_n = E_2 Y_n/n$,
  which is Day 154 Corollary 4.1 material in one line. Independent of Day 154's Lagrange-Bürmann proof.
- **Sets up Day 159's C.5 upgrade attempt.** With $X^{(0)}$ closed on the $u_3 = 0$ slice, the
  natural next step is to substitute into Day 156's decomposition lemma
  $M^{(-1)} = \partial X^{(0)} + \tfrac{1}{2}\partial^2 \Xi$.
- **The lift to full 3-variable $X^{(0)}$ is OPEN.** Day 158 gets the boundary value only.
  Extending to $\partial_{E_3} X^{(0)}|_{E_3=0}$ requires either (Route A) a 3-variable Riccati
  or (Route B) $\varrho$-decomposition on $\mathcal R/V(u)$. Both are Day 152 machinery, not Day 158.

## Naming caveat

Under the natural $u$-weight grading used here, "top" and "sub-top" of $\log F$ **SWAP** vs
the Day 152/154 tower convention (where the tower goes downward in $u$-weight from $\ell^{\rm top}_1$).
The chained identity "$X^{(0)} = (1/2) \log \mathcal W = (1/2) \partial \Xi$" from PROVE.md
collapses to the FIRST equality only at $u_3 = 0$; the second equality (requiring
$\log \mathcal W = \partial \Xi$ under the swapped naming) is FALSE. Feedback memory saved:
`feedback_top_layer_convention_swap.md`. Verify each equality directly at $n=2$, do not chain-derive.

## Style note

**This proof is a template.** "Write down the raw ODE from the definition, split by weight, close
each diagonal in ODE type appropriate to its weight" is the cleanest technique in the arc so far.
Every step is bookkeeping. Consider promoting to a technique memo if the Day 159 or 160 sessions
use the same shape.
