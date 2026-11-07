---
name: Attack Conjecture P by u-degree layers, not by bijection — Rule 12 applied to positivity
description: Day 150 dream. Day 149 Thm 2 gives H a u-degree filtration with deg <= n; the top layer is the Narayana/Lagrange leading symbol W_n, which is manifestly positive. So Conjecture P should be proved LAYER BY LAYER downward, not by hunting one global sign-reversing involution. This reorders Day 149 section 9's own priority list: identifying the Lagrange kernel psi in three variables is not step 3, it is step 0.
type: connection
---

# Conjecture P is a filtration problem, not a bijection problem

## The observation

Rule 12 (Day 149) says: *for $\tau(F)/F$ bounds, find the filtration whose extreme layer $\tau$
cannot move.* That rule was invented for (H2). **It applies verbatim to Conjecture P, and nobody
noticed because (H2) was a degree bound and P is a positivity statement.**

Day 149 Thm 2: $\deg_u[T^n]H\le n$. Every $E$-monomial $E_1^aE_2^bE_3^c$ has $u$-degree $a+2b+3c$.
So $[T^n]H$ stratifies by the **defect** $d:=n-(a+2b+3c)\ge0$:
$$[T^n]H=\underbrace{\mathcal W_n}_{d=0}+\underbrace{(\text{lower})}_{d\ge1},\qquad
\mathcal W=\ell_0^{\mathrm{top}}(H)=\exp(\partial\Xi).$$

**Layer $d=0$ is already essentially done.** At $E_3=0$, $\mathcal W_n=(n+1)W_n$ with $W_n$ the
Narayana polynomial — non-negative, in fact a count of $NC(n{+}1)$ by block number, and it comes
from Lagrange inversion of $\psi|_{E_3=0}=\prod_i(1+u_iY)$. In three variables the same Lagrange
form holds with an unknown kernel
$$\psi=1+E_1Y+E_2Y^2+2E_3Y^3+E_1E_3Y^4+2E_2E_3Y^5+(E_1E_2E_3{+}5E_3^2)Y^6+\cdots$$
(every coefficient from $Y^3$ on divisible by $E_3$ — Day 149 §4). **If $\psi$ has non-negative
coefficients, layer $d=0$ of Conjecture P is a theorem by Lagrange inversion**, since
$[T^n]\frac{dY}{dT}$ is then a non-negative-coefficient polynomial in the coefficients of $\psi$.
Look at the data: $1,E_1,E_2,2E_3,E_1E_3,2E_2E_3,E_1E_2E_3+5E_3^2$ — **all coefficients so far are
non-negative integers.** That is a strictly easier conjecture than P, on a smaller object, and it
implies P's top layer.

## The reordering

Day 149 §9 lists three next steps, with "identify the Lagrange kernel $\psi$ in closed form" as
**third**, described as "the leading symbol's combinatorial certificate." That ranking is wrong.
$\psi$ is:

1. the **entire** $d=0$ layer of Conjecture P,
2. a **one-variable-in-$Y$** object with (apparently) non-negative coefficients — so a *smaller*
   positivity conjecture that implies the top layer of the big one,
3. the object whose combinatorial model (a tree/Schröder species, per the Narayana specialisation)
   would tell you what $[T^n]H$ *counts*, which is exactly what "find the basis in which the
   cancellation is manifest" (§9 step 1) is asking for.

**Revised priority for Day 150+ PROVE:**

> **P0.** Compute $\psi$ to $Y^{12}$–$Y^{15}$. Test: are all coefficients in $\mathbb Z_{\ge0}[E]$?
> Is $\psi$ algebraic / is it a specialisation of the Day 148 quintic's kernel? Search the
> coefficient sequence (at $E=(1,1,1)$ and at $E_1=E_2=0$) against OEIS.
> **P1.** If $\psi\ge0$: layer $d=0$ done. Then set up the $d\to d+1$ recursion from the Riccati
> system (R) and ask whether each layer is a non-negative combination of the ones above it.
> **P2.** Only then hunt a global model.

## Why a global involution was always going to be hard

Browse 117/118 turned up three independent instances of the same wall (Alexandersson–Dai: e-basis
positivity resists a per-coefficient bijection, only aggregated-by-length works; Zemel: NCQSym
antipode clean only at the extreme stratum; Wang–Wang: certificates *instead of* involutions), and
Rick's own (H2) is a fourth. See [[2026-08-30-day150-extreme-layer-positivity-pattern]]. Betting
the session on one global bijection is betting against four independent data points.

## Caveats (stated so future-me doesn't inherit an overclaim)

* The $E_3=0$ Narayana identity is **verified to $n\le16$**, with a Lagrange-inversion derivation
  sketched but not written out as a proof. Write the proof; it's three lines.
* $[E_1^n][T^n]H=n+1$ **follows** from that (see [[2026-08-30-day150-two-arcs-one-lattice]]); the
  *minimality* of $n+1$ over all monomials does not, and is untouched.
* "All coefficients of $\psi$ non-negative" rests on **seven** terms. That is not evidence, it is a
  reason to compute more. Do not write it down as a conjecture until $Y^{12}$.
