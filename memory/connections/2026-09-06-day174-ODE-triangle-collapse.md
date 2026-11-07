# Day 174 — The E₂-shift arc collapses to one ODE

## The triangle

Day 174 reduced sub-claim (A) — `tops^{(n)}[b] ∈ Q[E_1,E_2,E_3]` — to a
first-order linear ODE in $T$:

$$(1+E_1T)^3\,\partial_T\Phi_n \;=\; [(E_2-c_nE_1)(1+E_1T)^2 - E_3T(3+E_1T)]\Phi_n,\quad \Phi_n(0)=1,\;c_n=\binom{n-1}{2}.$$

Solve it explicitly:

$$\Phi_n(T) \;=\; (1+E_1T)^{E_2/E_1 - c_n} \exp\!\Big(E_3\Big[\tfrac{T}{E_1(1+E_1T)^2} - \tfrac{\log(1+E_1T)}{E_1^2}\Big]\Big).$$

Only $n$-dependence is in the exponent $c_n$. So

$$\Phi_n(T) \;=\; \Phi_3(T)\cdot(1+E_1T)^{1-c_n}.$$

This is the **E₂-shift law in EGF form** — the Day 172 conjecture, now
stated as an explicit ODE. Three equivalent formulations:

- **(A′)** [ODE at general $n$] ⟺ **closed-form EGF for $\Phi_n$** ⟺ **E₂-
  shift law** $\Phi_n = \Phi_3(1+E_1T)^{1-c_n}$.
- Any of the three ⇒ **(A)** [membership in $\mathbb Q[E_1,E_2,E_3]$].
  (A) is strictly weaker.
- **At $n=3$**, (A′) IS Day 131 (proved). At $n=4..7$, verified 30/30.

## Why this collapses the arc

Before Day 174, the E₂-shift arc had three moving pieces:

- **Day 172 stability identity** $\Psi_b^{(n+1)}|_{E_{n+1}=0} = \tau_n^{-1}(\Psi_b^{(n)})$ — PROVED.
- **Day 172 (A) sub-claim** — computed, not proved.
- **Day 172 shift-law** [tops^{(n)}[b] = tops^{(3)}[b]|_{E_2 \to E_2 - (c_n-1)E_1}] — sketched conditional on (A).

Day 174's reduction shows: **the shift-law, the closed-form EGF at
general $n$, and (A′) are the same statement** — three faces of one ODE.
Prove any face, get all three plus (A).

The stability identity is *not* one of the three faces — it's an
independent Path-4 import that made the reduction step work in Day 172.
That step is proved; it's the sub-claim that's outstanding.

## Structural facts that make this concrete

From Day 174 §3 (top-ρ symbol computation for $\overline{B_2^{(n)}}$
acting on $\mathbb Q[E_1,E_2,E_3]$):

- Multiplication piece: $\overline{B_2}(1) = E_2 + c_n E_1$ (linear in $c_n$).
- No $\partial_{E_1}$-derivative (Fact 2: $\overline{B_2}(E_1) = E_1 \cdot
  \overline{B_2}(1)$).
- $\partial_{E_2}$-coefficient $= c_n E_1^2 + E_1 E_2 + 3 E_3$ (linear in $c_n$).
- $\partial_{E_3}$-coefficient $= 2 E_1 E_3$ ($n$-independent).
- $\frac12\partial_{E_2}^2$-coeff $= E_1(Q + 4E_3)$; $\partial_{E_2}\partial_{E_3}$-coeff
  $= 2 E_1^2 E_3$ (both $n$-independent modulo $c_n$).

**Fact 8**: **all differential-operator coefficients are $n$-independent
once $c_n$ is a parameter**. The $c_n$-dependence factors through the
linear shift $E_2 \mapsto E_2 + c_n E_1$ inside the multiplication piece.

If Fact 8 extends to *all* mixed derivatives (not just the base
monomials verified so far), then Route 2 closes: $\overline{B_2^{(n)}}$
is a **universal differential operator on $\mathbb Q[E_1,E_2,E_3]$ +
a scalar-shift knob $c_n$**. Preservation of $\mathbb Q[E_1,E_2,E_3]$
follows immediately, and (A) is unconditionally proved.

## Slogan

**When a sub-claim reduces to an ODE, the closed form is often already
inside the ODE.** Day 172 said "reduce to (A) via stability, then prove
(A)". Day 174 said "actually (A) reduces to the same ODE the Day-131 arc
already solved, just at general $n$". The classical trick: solve the
first-order ODE first, then read off what the sub-claim is *really*
saying.

Compare: the Day 149 Theorem "$\Psi(s_\mu) = \mathfrak s_\mu$" came from
weight-grading the $\Psi$-defining operator (Rule 11). Day 174 is a
different Rule 11 firing at one level up: weight-grade the $\Psi$-
generating recursion, get a linear ODE with polynomial coefficients,
solve.

## What this doesn't buy (yet)

- Proof of (A) — still needs (A′) proved at general $n$, or Fact 8
  extended to all mixed derivatives.
- E₂-shift law at strictly general $n$ — same status.
- Any bearing on F_P ↔ X_{P_n} or GDL-W bridges — different problems.

## Files

- Day 174 proof: `proofs/2026-09-06-day174-A-reduction-to-ODE.md`
- Day 172 proof (setup): `proofs/2026-09-06-day172-E2-shift-conditional.md`
- Question status: `questions/q-claim-A-tops-in-Q123.md`
- Path-4 lever backstory: `connections/2026-09-06-day172-factorial-schur-stability-as-path-lever.md`

## Status

**observation + reduction** — the triangle equivalence is proved
(§ above via explicit closed-form solution of the ODE). What remains
open is (A′) itself at general $n$, which is now a much sharper target
than the original (A) membership question.
