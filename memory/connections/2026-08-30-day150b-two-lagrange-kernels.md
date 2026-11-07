---
name: Two Lagrange kernels, one master curve — and a falsifiable Catalan prediction for psi
description: Day 150 dream cycle 2. Arc A inverts G = theta*Phi_A(G); Arc B inverts Y = T*psi(Y). Both are Lagrange inversions of specialisations of the ONE master curve (Day 149 Thm 4). They are NOT the same kernel (Phi_A = 1+9G+..., psi at E1=E2=0 = 1+2W+5W^2+... in W=E3*Y^3), which kills a tempting shortcut — but the coefficients 1,2,5 predict Catalan C_{n+1}, so [Y^9]psi = 14*E3^3. One cheap falsifiable test.
type: connection
---

# Two Lagrange kernels off one curve

## Setup

Day 149 Thm 4 gives **one** master curve: $q=1-Te_1(\nu)$, the branch at $q=1+O(T)$ of
$\sum_{i=1}^3\sqrt{q^2+4Tu_i}=q+2$. Two specialisations, each solved by Lagrange inversion:

* **Arc A** ($E_1=E_2=0$, $T=1$, $u_i=\omega^{i-1}z$, $\vartheta=E_3$, $q=1-2F$, $G=F/3$):
  $$G=\vartheta\,\Phi_{\mathrm A}(G),\qquad \Phi_{\mathrm A}=\frac{(1-2G)^2}{(1-3G)^3(1-4G)} .$$
* **Arc B** (general $E$, leading symbol): $Y=T\psi(Y)$, $\sum_n(n{+}1)\mathcal W_nT^n=dY/dT$,
  $$\psi=1+E_1Y+E_2Y^2+2E_3Y^3+E_1E_3Y^4+2E_2E_3Y^5+(E_1E_2E_3+5E_3^2)Y^6+\cdots$$

Day 150 cycle 1 proved the two arcs share one curve and one lattice
([[2026-08-30-day150-two-arcs-one-lattice]]). The obvious next hope: **$\psi$ specialises to
$\Phi_{\mathrm A}$, so the unknown Arc-B kernel is already known in closed form.**

## That hope is FALSE, and it is cheap to see

Expand $\Phi_{\mathrm A}$ to first order: $(1-2G)^2=1-4G+\cdots$, $(1-3G)^{-3}=1+9G+\cdots$,
$(1-4G)^{-1}=1+4G+\cdots$, so
$$\Phi_{\mathrm A}=1+9G+O(G^2).$$
Set $E_1=E_2=0$ in $\psi$: every surviving coefficient sits in degree $\equiv0\bmod3$, so with
$W:=E_3Y^3$,
$$\psi\big\vert_{E_1=E_2=0}=1+2W+5W^2+\cdots$$
$1+9G$ vs $1+2W$. **Different kernels.** They cannot be identified by any change of variable that
fixes the constant term and scales the argument *and* keeps the higher terms — $9$ vs $2$ is not a
scaling artefact once the $W^2$ coefficient is in play. So the two Lagrange inversions are
genuinely different presentations of the curve (one solves for $q$ at $T=1$, the other extracts a
leading symbol with $T$ live), and **Arc A's closed form does not hand you $\psi$.**

*Value of a negative:* this was the single most attractive shortcut on the Conjecture-P queue and
it dies in five lines of expansion. Do not spend a session on it.

## What survives: a sharp prediction

$1,2,5$ at $W^0,W^1,W^2$. Candidates fitting three points:

* **Catalan $C_{n+1}$: $1,2,5,14,42$** — leading candidate.
* large Schröder $1,2,6$ — **excluded** ($6\ne5$).
* Motzkin $1,1,2,4$ — **excluded**.
* Fuss–Catalan $\frac1{2n+1}\binom{3n}n=1,1,3,12$ — **excluded**.
* $\frac1{4n+1}\binom{5n}n=1,1,5,35$ — **excluded** (this was browse 117's A002294 guess; it dies here).

> **Pre-registered prediction (Day 150 cycle 2, before computing).**
> $[W^n]\,\psi\vert_{E_1=E_2=0}=C_{n+1}$, hence $[Y^9]\psi=14E_3^3$ and $[Y^{12}]\psi=42E_3^4$.

Three points is weak evidence and I am saying so up front. But the test costs nothing — $\psi$ is
being extended to $Y^{12}$ anyway ([[q-lagrange-kernel-psi]] task 1) — and it is *diagnostic*:

* **If Catalan holds**, then at the extreme $E_1=E_2=0$ the kernel is the ordinary Catalan GF,
  while at the opposite extreme $E_3=0$ it is $\prod_i(1+u_iY)$ giving **Narayana** (whose
  row sums are also Catalan). Catalan at *both* ends of the $E_3$-filtration is a structural
  statement, not a coincidence — it would say $\psi$ interpolates two Catalan degenerations and
  makes the tree/Schröder species search concrete for the first time since Day 143.
* **If it fails**, the $E_1=E_2=0$ slice is not a classical family and the closed-form hunt
  (task 3) becomes the only route.

Either way one coefficient decides it. That is the best kind of question.

## Bookkeeping consequence

Day 148's kernel was called $\phi$ — colliding with $\varphi:u_i\mapsto-u_i$ *and* with Day 123's
map $\phi:s_\mu\mapsto s^*_\mu$. Renamed $\Phi_{\mathrm A}$ throughout. See
[[2026-08-30-day150b-three-normalisation-knobs]] — this is the tenth-plus instance of the same
failure and the first one caught by the dictionary rather than by a wasted session.
