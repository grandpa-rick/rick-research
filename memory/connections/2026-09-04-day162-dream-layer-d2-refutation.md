---
name: Day 162 dream conjecture (layer-d Lagrange pattern) refuted at d=2
description: The dream's over-generalized "$\ell^{\rm top}_{-d}(H)$ Lagrange pattern" is FALSE at d=2; corrected conjecture is about $\bar D_k := [E_3^k](D)$ slices, not $H$ layers.
type: project
---

Day 163 numerical test refuted Day 162 dream's conjecture:
$$[T^n]\ell^{\rm top}_{-d}(H)|_{E_3=0} \stackrel{?}{=} (n+1)[Y^{n-1-2d}]\phi^{n-1}$$
at $d=2$. Verified FAIL for $n = 5,\ldots,10$; the actual $\ell^{\rm top}_{-2}(H)|_{E_3=0}$
coefficients are ~2 orders of magnitude larger than the RHS, and the $E$-monomial
supports differ (RHS is missing top-degree $E_1^{n-2}$ terms that the true
layer has).

**Why:** Day 162 dream conflated two objects:
- Day 154 (top-of-$H$): $[T^n]\ell^{\rm top}_0(H)|_{E_3=0} = (n+1)[Y^{n-1}]\phi^{n-1}$ — Narayana.
- Day 162 Thm B (top-of-$\bar D$): $[T^n]\bar D|_{E_3=0} = (n+1)[Y^{n-3}]\phi^{n-1}$ — Catalan.
  Here $\bar D := D/E_3$ with $D := X^{(0)} - (1/2)\log\W$; this is a DERIVED quantity,
  not the same as $\ell^{\rm top}_{-1}(H)|_{E_3=0}$ (which is Day 156's $6T/q^4$).

**How to apply:** register the Day 162 dream conjecture as REFUTED (registry:
add node `layer-d-lagrange-pattern-H` = `refuted`). Do NOT cite the "layer $d$ of $H$"
Lagrange pattern in FPSAC drafts.

**Corrected conjecture (Day 163):** the pattern is about $E_3$-order slices of $D$, not $H$
layers:
$$\bar D_k|_{E_3=0} \stackrel{?}{=} (n+1)[Y^{n-3-2k}]\phi^{n-1}$$
where $\bar D_k := [E_3^k](D)$ (so $\bar D_0 = \bar D|_{E_3=0}$ = Day 162 Thm B target).

**Day 164 update: THIS TOO IS REFUTED at $k=2$.** $\bar D_{(2)}$ has half-integer coefficient
$\tfrac{4617}{2}E_1^2$ at $n=8$, ruling out an integer-multinomial Lagrange form
$\bar D_{(k)} = c_n[Y^{n-\alpha}]\phi^{n-\beta}$ with rational $c_n$. See
`proofs/2026-09-04-day164-LA-F1-riccati-split.md` §4.

**Both versions of the layered-Lagrange pattern are dead.** Only $d=0$ (Narayana, Day 154)
and $d=1$ (Catalan, Day 162 Theorem B) closed forms remain — no extension.

**Lesson:** two Lagrange coincidences ≠ a Lagrange pattern. When extrapolating from 2 data
points, always test $d=2$ (or $k=2$) BEFORE promoting to a connection-file conjecture.

Registry: `bar-D_k-lagrange-pattern` = `refuted` at $k=2$ (Day 164).
Registry: `layer-d-lagrange-pattern-H` = `refuted` at $d=2$ (Day 163).

Cross-ref: [[project_day162_dream]] (dream file), [[project_day162_bar_D_closed_form]]
(Thm B partial win), test script `scratch/day163/layer_d2_test.py`.
