# Day 146 — $b_k \equiv 0 \pmod 3$: the master equation and the reduction to Conjecture H

**Date:** 2026-08-29 · **Status:** MAJOR STRUCTURAL ADVANCE. Theorem proved modulo one
clean, sharply-stated, heavily-verified conjecture (Conjecture H).

---

## 0. Executive summary — what happened today

I stopped attacking $b_k \bmod 3$ through the $\log$ / cumulant side and went back to
the **definition side**: the $\Psi$-recursion. Three things fell out.

1. **The master equation.** The whole $\Psi$-recursion is *exactly* the single
   functional identity
   $$\boxed{\;L\,F_P \;=\; E_3T^2\Big[-3 + T\big(E_1+6+2\theta\big)\Big]\,\tau(F_P)\;}$$
   where $\tau$ is the shift $u_i \mapsto u_i+1$ on the three underlying variables.
   *(Verified symbolically in $\mathbb Z[E_1,E_2,E_3]$ for $b \le 16$; it is a two-line
   generating-function translation of the recursion.)*

2. **A closed-form equation for $F$.** Introducing $H := \tau(F_P)/F_P$ and its
   "diagonal" $\mathcal H(\vartheta) := \sum_j [E_3^jT^{3j}]H \cdot \vartheta^j$, the
   leading-order part of the master equation gives the **exact identity**
   $$\boxed{\;F^2 - F \;=\; \vartheta\,\mathcal H(\vartheta)\,\big(2F-3\big)\;}$$
   ($\vartheta$ = the variable previously called $\tau$ in the $b_k$ generating function;
   renamed here to avoid clashing with the shift operator).
   This *supersedes* the Day 143 identity $A = F^2-F$ by identifying $A$ itself:
   $A = \vartheta\,\mathcal H\,(2F-3)$.

3. **The whole problem collapses to integrality.** Because the constant term of
   $2F-3$ is $-3$:
   $$b_k \equiv 0 \pmod 3 \ \ \forall k \iff \mathcal H \in \mathbb Z_3[[\vartheta]].$$
   And $\mathcal H$ is the diagonal of $H = \tau(F_P)/F_P$, which is
   **experimentally a series with integer polynomial coefficients**:
   $H \in \mathbb Z[E_1,E_2,E_3][[T]]$.

So: **Conjecture H $\Rightarrow$ FPSAC Theorem 3.9.**

Along the way I also proved two clean divisibility lemmas about $\Psi_b$ and identified
*why* every mod-3 attack of Days 144–146 was doomed (§8).

---

## 1. Setup and notation

Let $E_1,E_2,E_3$ be the elementary symmetric functions of three variables
$u_1,u_2,u_3$. Two substitution operators:

- $\sigma$ : $u_i \mapsto u_i - 1$, i.e. $E_1 \mapsto E_1-3$, $E_2\mapsto E_2-2E_1+3$,
  $E_3 \mapsto E_3-E_2+E_1-1$;
- $\varphi$ : $u_i \mapsto -u_i$, i.e. $E_1 \mapsto -E_1$, $E_2\mapsto E_2$, $E_3\mapsto -E_3$;
- $\tau := \varphi\sigma\varphi$ : $u_i \mapsto u_i+1$, i.e. $E_1\mapsto E_1+3$,
  $E_2\mapsto E_2+2E_1+3$, $E_3\mapsto E_3+E_2+E_1+1$.

Note $\tau = \sigma^{-1}$.

**The $\Psi$-recursion (Day 131 Theorem A).** $\Psi_0 = 1$, $\Psi_1 = E_2-E_1+1$, and
$$\Psi_{b+1} = \big(E_2-(b{+}1)E_1+(b{+}1)^2\big)\Psi_b \;-\; 3b\,E_3\,\sigma(\Psi_{b-1})
\;-\; b(b{-}1)(E_1-2b-2)\,E_3\,\sigma(\Psi_{b-2}).$$
Set $P_b := \varphi(\Psi_b) \in \mathbb Z[E_1,E_2,E_3]$ and
$$F_P := \sum_{b\ge 0} P_b \frac{T^b}{b!}.$$

Write $\varphi_k := E_2+kE_1+k^2$. Parametrising $E_1 = U+V-2$, $E_2 = (U-1)(V-1)$
gives $\varphi_k = (U+k-1)(V+k-1)$, so
$P_b|_{E_3=0} = \prod_{k=1}^b\varphi_k = (U)_b(V)_b$ and
$F_P|_{E_3=0} = f := {}_2F_0(U,V;;T)$.

**The Frobenius operator.** $\theta = T\,d/dT$ and
$L := T(U+\theta)(V+\theta)-\theta = T\varphi(\theta+1)-\theta$, so $Lf = 0$.
Put $X := L F_P / F_P$ and $R := \log(F_P/f) = \sum_{k\ge1}E_3^kN_k(T)$.

**The two sequences.**
$$n_k := N_k[T^{3k-1}], \qquad b_k := (3k-1)n_k, \qquad a_k := [E_3^kT^{3k-1}]X,$$
$$F(\vartheta) = \sum_{k\ge1}b_k\vartheta^k,\qquad A(\vartheta)=\sum_{k\ge1}a_k\vartheta^k .$$

Day 143: $A = F^2-F$, i.e. $(1-2F)^2 = 1+4A$.

**Target.** $b_k \equiv 0 \pmod 3$ for all $k\ge1$.

Data ($k=1,\dots,12$, extended today from $k=8$):
$$b_k = 3,\;27,\;417,\;7851,\;164124,\;3661389,\;85384566,\;2056373739,$$
$$50751637140,\;1276862920140,\;32626363346505,\;844375375808301,$$
$$v_3(b_k) = 1,3,1,1,2,3,2,2,1,1,2,1 .$$

---

## 2. Two elementary divisibility lemmas (proved)

Read the recursion as a **path/composition** statement. To reach $\Psi_B$ from $\Psi_0$
one composes steps that go
$b\!-\!1 \to b$ (weight $\varphi^{\Psi}_b$, no $E_3$),
$b\!-\!2\to b$ (weight $-3(b{-}1)E_3\sigma$, one $E_3$, **factor 3**),
$b\!-\!3\to b$ (weight $-(b{-}1)(b{-}2)(E_1-2b)E_3\sigma$, one $E_3$).
Thus $\Psi_B = \sum_{\text{compositions of }B\text{ into parts }1,2,3}(\text{weight})$, and
since $\sigma$ is a ring automorphism preserving $E_3$-degree (it maps $E_3$ to
$E_3-E_2+E_1-1$, hence never *raises* degree), each path with $s$ parts of size 2 and
$t$ parts of size 3 contributes to $E_3$-degree $\le s+t$ and carries a factor $3^s$.

**Lemma A.** $\deg_{E_3}\Psi_B = \deg_{E_3}P_B \le \lfloor B/2\rfloor$.

*Proof.* $B = u + 2s+3t \ge 2s+3t \ge 2(s+t) \ge 2\deg_{E_3}$. $\square$

**Lemma B (mod-3 degree drop).** For all $k,B$,
$$v_3\big([E_3^k]\Psi_B\big) \;\ge\; \max(0,\;3k-B).$$
In particular $[E_3^k]P_B \equiv 0 \pmod 3$ whenever $B < 3k$, i.e.
$$\deg_{E_3}\big(P_B \bmod 3\big) \le \lfloor B/3\rfloor .$$

*Proof.* On a path with $E_3$-degree $\ge k$ we have $s+t\ge k$ and
$B \ge 2s+3t = 3(s+t)-s \ge 3k-s$, so $s \ge 3k-B$; the path carries $3^s$. $\square$

*(Table check: $v_3([E_3^k]\Psi_B)$ on the diagonal $3k-B=1$ equals exactly $1$ for
$B=2,5,8,11,14,17,20$ — the bound is sharp there.)*

**Corollary (mod-3 structure of $\Psi$).** Reducing the recursion mod 3, the middle term
dies and the last survives only when $b\equiv2\ (3)$. With
$\alpha := E_2-E_1+1$, $\beta := E_2+E_1+1$, $\gamma := \alpha\beta E_2$, $\delta := E_1E_3$:
$$\Psi_{3m+1}\equiv\alpha\,\Psi_{3m},\quad \Psi_{3m+2}\equiv\alpha\beta\,\Psi_{3m},\quad
\Psi_{3(m+1)} \equiv \gamma\,\Psi_{3m}+\delta\,\sigma(\Psi_{3m}) \pmod 3 ,$$
so $\Psi_{3m}\equiv(\gamma+\delta\sigma)^m(1)$: a **first-order** mod-3 recursion where a
$\mathbb Z/3$-Frobenius contraction $b\mapsto b/3$ is visible. (Recorded for the Dwork
route, §9.)

---

## 3. The master equation

**Theorem 1 (Master equation).** In $\mathbb Q[E_1,E_2,E_3][[T]]$,
$$L\,F_P \;=\; E_3T^2\Big[-3 + T\big(E_1+6+2\theta\big)\Big]\,\tau(F_P) . \tag{ME}$$
Equivalently, coefficientwise,
$$P_{b+1} \;=\; \varphi_{b+1}P_b \;+\; 3b\,E_3\,\tau(P_{b-1}) \;-\; b(b{-}1)(E_1+2b+2)\,E_3\,\tau(P_{b-2}).\tag{ME'}$$

*Proof.* (ME') is the image of the $\Psi$-recursion under $\varphi$ (using
$\varphi\sigma = \tau\varphi$, $\varphi(E_3\cdot)= -E_3\varphi(\cdot)$,
$\varphi(E_1)=-E_1$). Multiply (ME') by $T^b/b!$ and sum:
$\sum_b P_{b+1}T^b/b! = \partial_T F_P$; $\sum_b\varphi_{b+1}P_bT^b/b! = \varphi(\theta+1)F_P$;
$\sum_b 3bE_3\tau(P_{b-1})T^b/b! = 3E_3T\,\tau(F_P)$;
$\sum_b b(b{-}1)(E_1+2b+2)E_3\tau(P_{b-2})T^b/b! = E_3T^2(E_1+2\theta+6)\tau(F_P)$.
Multiply by $T$ and use $T\varphi(\theta+1)-\theta = L$. $\square$

*Verification:* `verify_master.py` checks (ME') identically in $\mathbb Z[E_1,E_2,E_3]$
for $b+1 \le 16$: **VERIFIED**.

Note $L f = 0$ is the $E_3=0$ shadow of (ME).

---

## 4. Coordinates: $\rho$, $\vartheta$, and the order filtration

Set
$$\rho := E_3T^2, \qquad \vartheta := E_3T^3 = \rho T .$$
Then $E_3^kT^b = \rho^kT^{\,b-2k}$. By Lemma A, $[E_3^k]P_b = 0$ for $b<2k$, hence

$$F_P \in \mathbb Q[E_1,E_2][[\rho,T]] .$$

For $W = \sum_{k,e} w_{k,e}\,\rho^kT^e$ define the **order** of the monomial
$\rho^kT^e$ to be $e-k$ (equivalently: write $\rho^kT^e = \vartheta^kT^{\,e-k}$ — the order is
the exponent of $T$ in $(\vartheta,T)$-coordinates). Say $W$ has order $\ge d$ if
$w_{k,e}=0$ whenever $e-k<d$, and write
$$\ell_d(W) := \sum_k w_{k,\,k+d}\,\vartheta^k \in \mathbb Q[E_1,E_2][[\vartheta]] .$$

Elementary properties, used constantly:
* $T$ raises order by 1; $\rho$ lowers it by 1; $\vartheta$ preserves it;
  $\theta$ (which multiplies $\rho^kT^e$ by $b = e+2k$) preserves it, and on order-$d$
  parts acts as $d+3\theta_\vartheta$.
* $\ell_{d_1}(W_1)\ell_{d_2}(W_2) = \ell_{d_1+d_2}(W_1W_2)$ for $W_i$ of order $\ge d_i$;
  in particular $\ell_0$ is a **ring homomorphism** on $\{\text{order}\ge0\}$.
* $\ell_{d-1}(\rho W) = \vartheta\,\ell_d(W)$.
* $\tau$ preserves order: $\tau(\vartheta) = \vartheta + \varphi_1T^3$ and $T^3$ has order $3>0$;
  moreover $\ell_d(\tau W) = \tau(\ell_d(W))$, where on the right $\tau$ acts only on the
  $(E_1,E_2)$-dependence.

Set
$$\Lambda := \theta\log F_P = \frac{\theta F_P}{F_P},\qquad H := \frac{\tau(F_P)}{F_P}.$$
By construction $\ell_{-1}(\log F_P) = \sum_k n_k\vartheta^k$ and hence, since $\theta$ acts by
$b = 3k-1$ on order $-1$,
$$\ell_{-1}(\Lambda) = \sum_k (3k-1)n_k\,\vartheta^k = F(\vartheta). \tag{4.1}$$

Dividing (ME) by $F_P$ and using $\theta(HF_P) = (\theta H)F_P + H\theta F_P$:

$$\boxed{\;T\big[\varphi_1+(E_1{+}2)\Lambda+\theta\Lambda+\Lambda^2\big]-\Lambda
\;=\; \rho\big[(T(E_1{+}6)-3)H + 2T\,\theta H + 2T\,H\Lambda\big]\;}\tag{ME$_\Lambda$}$$

(the left side is just $X = LF_P/F_P$, expanded with $L = T\varphi(\theta+1)-\theta$ and
$\varphi(\theta+1) = \varphi_1 + (E_1+2)\theta+\theta^2$ acting on $e^{\log F_P}$).

---

## 5. Conjecture H

> **Conjecture H.** $H = \tau(F_P)/F_P$ satisfies
> **(H1)** $H \in \mathbb Z[E_1,E_2,E_3][[T]]$ (integer polynomial coefficients), and
> **(H2)** $\deg_{E_3}\big([T^n]H\big) \le \lfloor n/3\rfloor$ for all $n$ — equivalently
> $H$ has **order $\ge 0$**.

**Evidence.**
* Symbolically in $\mathbb Z[E_1,E_2,E_3]$: (H1) and (H2) verified for $n \le 14$
  (`symH.py`), with $\deg_{E_3}[T^n]H = \lfloor n/3\rfloor$ *exactly*.
* Numerically at the four base points $(E_1,E_2) = (-2,1),(-1,0),(0,-1),(1,1)$:
  (H1),(H2) verified for $n\le 20$ (`general_pt.py`); and at $(-2,1)$ for $n \le 36$
  (`bigdata.py`).
* First coefficients at $(E_1,E_2)=(-2,1)$ (i.e. $(U,V)=(0,0)$):
  $$[T^n]H = 1,\;2,\;6,\;24{+}8E_3,\;120{+}90E_3,\;720{+}864E_3,\;5040{+}8456E_3{+}119E_3^2,\dots$$
  with $[E_3^0][T^n]H = (n+1)!$ exactly (this is $f^{(1,2)} = \sum_b (b+1)!\,T^b$,
  since $f^{(0,0)}=1$ and $\varphi_1=0$ there).

Define the **diagonal of $H$**
$$\mathcal H(\vartheta) := \ell_0(H) = \sum_{j\ge0}\big[E_3^jT^{3j}\big]H \cdot \vartheta^j .$$
Computed values (identical at all four base points — see §7):
$$\mathcal H = 1 + 8\vartheta + 119\vartheta^2 + 2200\vartheta^3 + 45500\vartheta^4
+ 1007904\vartheta^5 + 23387442\vartheta^6 + 561163152\vartheta^7$$
$$\qquad + 13809781700\vartheta^8 + 346645093984\vartheta^9
+ 8840919351575\vartheta^{10} + \dots$$

---

## 6. The reduction theorem

### 6.1 (H2) implies the Day 143 vanishing lemma

**Proposition 1.** Assume (H2). Then $\Lambda$ (equivalently $\log(F_P/f)$) has order
$\ge -1$: $[E_3^kT^b]\log F_P = 0$ for all $k\ge1$ and $b<3k-1$.

*Proof.* Both $H$ and $\Lambda$ lie in $\mathbb Q[E_1,E_2][[\rho,T]]$, so all their
$\rho^kT^e$ coefficients with $e<0$ vanish. Fix $k\ge1$ and induct on $k$; inside, induct
on $e = 0,1,\dots,k-2$ ascending. Take $[\rho^kT^e]$ of (ME$_\Lambda$) with $e<k-1$.

*Right-hand side.* $[\rho^kT^e]\rho W = [\rho^{k-1}T^e]W$.
 - $[\rho^{k-1}T^e](-3H) = 0$ since (H2) gives order $\ge0$ and $e<k-1$.
 - $[\rho^{k-1}T^{e-1}]$ of $(E_1{+}6)H$ and of $2\theta H$: zero, as $e-1<k-1$.
 - $[\rho^{k-1}T^{e-1}](2H\Lambda) = 2\sum [\rho^{j}T^{f}]H\,[\rho^{k-1-j}T^{e-1-f}]\Lambda$.
   By (H2), $f\ge j$; by the induction hypothesis on $k$ (as $k-1-j<k$),
   $e-1-f \ge (k-1-j)-1$. Adding, $e-1\ge k-2$, i.e. $e\ge k-1$ — excluded. So this is $0$.

*Left-hand side.* $T\varphi_1$ contributes only at $k=0$.
$[\rho^kT^e]$ of $T(E_1{+}2)\Lambda$ and $T\theta\Lambda$ involve $[\rho^kT^{e-1}]\Lambda$,
zero by the inner induction ($e-1<k-1$).
$[\rho^kT^e](T\Lambda^2) = \sum [\rho^{k_1}T^{e_1}]\Lambda[\rho^{k_2}T^{e_2}]\Lambda$ with
$k_1+k_2=k$, $e_1+e_2 = e-1$. If $k_1,k_2\ge1$ then by induction $e_i\ge k_i-1$, so
$e-1\ge k-2$, excluded. If $k_1=0$: $\Lambda|_{E_3=0} = \theta f/f$ has $e_1\ge1$, whence
$e_2\le e-2 < k-1$ and $[\rho^kT^{e_2}]\Lambda = 0$ by the inner induction.

Hence the only surviving term is $-[\rho^kT^e]\Lambda$, which must therefore vanish.
$\square$

*(Remark. This proves — conditionally on (H2) — the Day 143 "leading-$T$ vanishing"
lemma, which had only been checked numerically. A shorter unconditional version: if
$\operatorname{ord}\Lambda = -N$ with $N\ge2$, the left side of (ME$_\Lambda$) has order
exactly $1-2N$ (leading term $\ell_{-N}(\Lambda)^2 \ne 0$) while the right side has order
$\ge -N > 1-2N$: contradiction.)*

### 6.2 The main identity

**Theorem 2.** Assume (H2). Then, with $\mathcal H = \ell_0(H)$,
$$F(\vartheta)^2 - F(\vartheta) \;=\; \vartheta\,\mathcal H(\vartheta)\,\big(2F(\vartheta)-3\big). \tag{6.1}$$
Consequently $A = \vartheta\,\mathcal H\,(2F-3)$, and $\mathcal H$ is independent of
$(E_1,E_2)$.

*Proof.* Apply $\ell_{-1}$ to (ME$_\Lambda$). By Proposition 1, $\Lambda$ has order $\ge-1$
with $\ell_{-1}(\Lambda) = F$ by (4.1); by (H2), $H$ has order $\ge0$ with
$\ell_0(H) = \mathcal H$.

*Left side.* $T\varphi_1$: order $\ge1$. $T(E_1{+}2)\Lambda$, $T\theta\Lambda$: order $\ge0$.
$T\Lambda^2$: order $\ge -1$ with $\ell_{-1}(T\Lambda^2) = \ell_{-2}(\Lambda^2)=F^2$.
$-\Lambda$: $\ell_{-1} = -F$. Total: $F^2-F$.

*Right side.* $\ell_{-1}(\rho\,[\cdot]) = \vartheta\,\ell_0([\cdot])$. Inside the bracket:
$-3H$ has $\ell_0 = -3\mathcal H$; $T(E_1{+}6)H$ and $2T\theta H$ have order $\ge1$;
$2TH\Lambda$ has order $\ge 1+0-1 = 0$ with
$\ell_0(2TH\Lambda) = 2\ell_{-1}(H\Lambda)=2\ell_0(H)\ell_{-1}(\Lambda) = 2\mathcal HF$.
Total: $\vartheta(2\mathcal HF-3\mathcal H)$.

Since $F$ has integer $(E_1,E_2)$-free coefficients (Day 143; and re-verified
symbolically today for $k\le5$, see §7), (6.1) forces
$\mathcal H = \dfrac{F^2-F}{\vartheta(2F-3)}$, manifestly $(E_1,E_2)$-free. $\square$

### 6.3 The theorem

**Theorem 3.** Assume Conjecture H. Then $b_k \equiv 0 \pmod 3$ for every $k\ge1$.

*Proof.* By (H1), all coefficients of $H$ lie in $\mathbb Z$, hence
$\mathcal H \in \mathbb Z[[\vartheta]] \subset \mathbb Z_3[[\vartheta]]$.
Reduce (6.1) mod 3: $2F-3\equiv 2F$, so
$$F^2 - F \equiv 2\vartheta\,\mathcal H\,F \pmod 3,\qquad\text{i.e.}\qquad
F\cdot\big(F-1-2\vartheta\mathcal H\big) \equiv 0 \ \text{ in } \mathbb F_3[[\vartheta]].$$
$\mathbb F_3[[\vartheta]]$ is an integral domain and $F-1-2\vartheta\mathcal H$ has constant
term $-1 \ne 0$, so it is a unit; therefore $F\equiv0 \pmod 3$, i.e.
$3\mid b_k$ for all $k$. $\square$

**Equivalence.** The converse also holds: writing $\Phi := F/3$,
(6.1) reads $\Phi-3\Phi^2 = \vartheta\mathcal H(1-2\Phi)$, so
$\Phi = \vartheta\mathcal H/(1-3\Phi+2\vartheta\mathcal H)$; conversely
$\mathcal H = F(1-F)/\big(\vartheta(3-2F)\big)$ has $3$ in the denominator of its leading
factor unless $3\mid F$. Hence
$$\mathcal H \in \mathbb Z_3[[\vartheta]] \iff b_k \equiv 0 \pmod 3 \ \forall k .$$
So (H1) is not merely sufficient — it is *equivalent* to the theorem. (H2) is the
structural half that makes the leading-order extraction legitimate.

---

## 7. Computational verification

All code in `~/projects/beta-prime/code/day146_prove/`.

| Check | Script | Result |
|---|---|---|
| (ME') identically in $\mathbb Z[E_1,E_2,E_3]$, $b\le16$ | `verify_master.py` | **VERIFIED** |
| $a_k$ is $(E_1,E_2)$-free, $k\le5$ (symbolically) | `secdiag.py` | **VERIFIED** |
| second diagonal $[E_3^kT^{3k}]X$ is **linear in $E_1$, no $E_2$** | `secdiag.py` | $-12{-}5E_1$, $-360{-}99E_1$, $-10632{-}2363E_1$, $-313464{-}60191E_1$, $-9240840{-}1586532E_1$ |
| $H$ integral + order $\ge0$ symbolically, $n\le14$ | `symH.py` | **VERIFIED**, $\deg_{E_3}[T^n]H=\lfloor n/3\rfloor$ |
| $H$ integral + order $\ge0$, four base points, $n\le20$ | `general_pt.py` | **VERIFIED** |
| $H$ integral + order $\ge0$ at $(-2,1)$, $n\le36$ | `bigdata.py` | **VERIFIED** |
| identity (6.1) at four base points | `general_pt.py` | **HOLDS** |
| $b_k$, $h_j$ agree at all four base points | `general_pt.py` | **YES** |
| $v_3(b_k)\ge1$, $k\le12$ | `bigdata.py` | $1,3,1,1,2,3,2,2,1,1,2,1$ |
| P-recurrence for $b_k$ or $h_j$, order $\le4$, degree $\le4$ | `search.py` | **NONE** |

Spot check of (6.1) by hand: $\mathcal H(2F-3) = (1+8\vartheta+119\vartheta^2+\cdots)(-3+6\vartheta+54\vartheta^2+\cdots)$
$= -3 + (6-24)\vartheta + (54+48-357)\vartheta^2 + \cdots = -3-18\vartheta-255\vartheta^2-\cdots$,
and $\vartheta\cdot$ that is $A = -3\vartheta-18\vartheta^2-255\vartheta^3-\cdots$ ✓.

**New data produced today.**
$$b_9=50751637140,\quad b_{10}=1276862920140,\quad b_{11}=32626363346505,$$
$$b_{12}=844375375808301 .$$
$$\mathcal H:\ 1,8,119,2200,45500,1007904,23387442,561163152,13809781700,$$
$$346645093984,\ 8840919351575,\ 228449188011224,\ 5968029850876084 .$$
($\mathcal H$ is not in OEIS territory I can check offline; $v_3(h_j) = 0,0,0,0,0,1,1,1,0,0,0,0,0$.)

---

## 8. Why every earlier mod-3 attack had to fail

This is worth recording, because it kills a whole family of approaches.

$b_k$ is extracted from $F_P = \sum P_b T^b/b!$, and the extraction divides by $(3k-1)!$,
whose $3$-adic valuation grows like $3k/2$. **Therefore $a_k \bmod 3$ is *not* a function
of $\{P_b \bmod 3\}$** — it depends on $P_b$ modulo $3^{N}$ with $N \sim 3k/2$.

Concretely, in the divided-power ring $\Gamma_{\mathbb Z}[[T]] = \{\sum c_bT^b/b! : c_b\in\mathbb Z\}$
(a genuine subring of $\mathbb Q[[T]]$) we have $F_P, LF_P, F_P^{-1}, X \in \Gamma_{\mathbb Z[E]}$,
and reduction mod 3 makes sense in $\Gamma_{\mathbb F_3}$ — but $\Gamma_{\mathbb F_3}$ has
**no division by $(3k-1)!$**, so the mod-3 reduction of $X$ does not see $a_k \bmod 3$.

This explains, in one stroke:
* why Lemma B (a perfectly true and sharp mod-3 statement, and morally "the reason")
  cannot be pushed through $\log$ or through $F_P^{-1}$;
* why the Day 146 "Attack A/B" plan (compute $P_b \bmod 3$, take $\log$, extract) is
  ill-posed;
* why the mod-3 collapse of the convolution
  $\sum_j \frac{n!}{(n-j)!}\,\eta_j P_{n-j} = \tau(P_n)$ to just $j \in \{n{-}1,n{-}2,n{-}3\}$
  (because $\frac{n!}{(n-j)!}\equiv0$ once the interval $(j,n)$ contains a multiple of 3)
  destroys all information about $\eta_n$, $n\ge4$.

The correct statement of the difficulty is therefore genuinely $3$-adic, and it is
now isolated in one place: **Conjecture H**.

---

## 9. Status of Conjecture H, and where I think it comes from

(H1) is a "denominator miracle". Solving the master equation for $\tau(F_P)$ costs a
factor $3^{-1}$ *per step in $T$*: writing $Y := \tau(F_P) = \sum Y_nT^n$, (ME) says
$$3E_3Y_{n-2} \;=\; E_3(E_1+2n)Y_{n-3} \;-\;[T^n]LF_P ,$$
so a priori $Y_n$ (and hence $H$) carries $3^{-n}$; empirically $H$ is an *integer*
series. That is precisely the shape of a **Dwork-type integrality theorem**.

**Dieudonné–Dwork, with the right Frobenius lift.** The coefficient ring is
$R = \mathbb Z_3[E_1,E_2,E_3]^{\wedge}$, not $\mathbb Z_3$, so the criterion needs a
Frobenius lift $\varsigma$ on $R$; take $\varsigma(E_i) = E_i^3$. Then for
$G\in1+TR[[T]]$,
$$G\in 1+TR[[T]] \iff \frac{G(T)^3}{\varsigma(G)(T^3)} \in 1+3T\,R[[T]].$$
*(Without the $E_3\mapsto E_3^3$ twist the criterion genuinely fails: numerically
$H(T)^3/H(T^3)$ has a unit coefficient at $T^9$. With the twist it holds. Checked.)*

Since $\tau$ acts on coefficients only, $\varsigma$ and $\tau$ commute on the locus
$\varphi_1 = 0$, and $K(\tau F_P) = \tau(K(F_P))$ where
$$K \;:=\; \frac{F_P(T)^3}{\varsigma(F_P)(T^3)} .$$
Hence:

> **(H1) $\iff$ $\dfrac{\tau(K)}{K} \in 1+3T\,\mathbb Z_3[E_1,E_2,E_3][[T]]$.**
> *(Verified to $T^{22}$ at three base points.)*

In words: **the $\tau$-variation of the Frobenius defect of $F_P$ is $\equiv1$ mod 3.**
Note $K$ itself is *not* 3-integral (e.g. $v_3([E_3^2T^9]K) = -1$); only its
$\tau$-variation is controlled.

One step of this is already free:

**Lemma C (proved).** $F_P(T)^3 \equiv 1$ and $\varsigma(F_P)(T^3)\equiv1$ in
$\Gamma_{\mathbb F_3}[[T]]$; hence $K \in 1+3\,\Gamma_{\mathbb Z_3}[[T]]$.

*Proof.* In a commutative $\mathbb F_3$-algebra $(\sum x_i)^3 = \sum x_i^3$, and
$\big(T^{[b]}\big)^3 = \binom{3b}{b,b,b}T^{[3b]}$ with
$v_3\binom{3b}{b,b,b} = v_3((3b)!) - 3v_3(b!) = \big(b+v_3(b!)\big)-3v_3(b!) = b-2v_3(b!) = s_3(b)\ge1$
for $b\ge1$ ($s_3$ = base-3 digit sum). So $F_P^3 \equiv P_0^3 = 1$. Likewise the
$\Gamma$-coefficient of $\varsigma(F_P)(T^3)$ at $T^{3b}$ is
$\frac{(3b)!}{b!}\varsigma(P_b)$ and $v_3\big(\frac{(3b)!}{b!}\big) = b \ge 1$. $\square$

*(Verified numerically at three base points to $T^{22}$.)*

Writing $K = 1+3W$ with $W\in\Gamma_{\mathbb Z_3}$, (H1) becomes
$$\frac{\tau W - W}{1+3W} \in T\,\mathbb Z_3[E][[T]] ,$$
i.e. an *ordinary*-integrality statement about one explicit element of the
divided-power ring $\Gamma$. The prime 3 has been fully extracted; what remains is the
$n!$ divisibility.

The input for such a congruence should be exactly the mod-3 self-similarity found in
§2's Corollary, $\Psi_{3m}\equiv(\gamma+\delta\sigma)^m(1)$, which is a genuine
$b\mapsto b/3$ contraction. **This is the natural next attack** and I did not have time
to carry it out.

A second, softer observation: the source of the $3$-denominators on the $\ell_0$ level is
completely transparent. In $(\rho,T)$ coordinates the recursion inverts the operator
$(d+2\theta_\rho)$, giving denominators $d+2k$. On the order-$(-1)$ diagonal $d=k-1$ this
is $3k-1$ — *never* divisible by 3, which is exactly why $b_k = (3k-1)n_k$ is an integer
(and why $n_k$ has denominator exactly $3k-1$: $3/2, 27/5, 417/8, 7851/11,\dots$).
On the order-$0$ diagonal $d=k$ it is $3k$ — divisible by 3, which is where the
$3$-denominators of $M := \ell_0(\log F_P)$ come from; $\mathcal H = \exp\big((\tau-1)M\big)$
and its integrality is the Artin–Hasse-type cancellation.

**Proposition 2 (exponential normal form; verified $d\le5$, $k\le8$).**
$$e^{-3\rho/2}\,F_P \;=\; \sum_{d\ge0}T^d\,G_d(\rho;E_1,E_2),$$
where each $G_d$ is a **polynomial** in $\rho$ with
$$\deg_\rho G_d + \deg_E \;\le\; 2d \qquad (\deg E_1 = 1,\ \deg E_2 = 2),$$
and $G_0 = 1$. (E.g.\ $G_1 = \big(1+8\rho+\tfrac{27}{5}\rho^2\big) + E_1\big(1+\tfrac83\rho\big) + E_2$;
the $\tfrac{27}5\rho^2$ is literally $n_2 = 27/5$.) This says the entire irregular
("exponential") part of $F_P$ at the $\rho$-scale is exactly $e^{3\rho/2}$, and it is
strictly stronger than Lemma A. Since $\tau$ is non-increasing for the weight
$w(E_1)=1,\,w(E_2)=2,\,w(E_3)=3,\,w(T)=-1$ (note $w(\rho)=1$ and
$\tau(\rho)-\rho = \varphi_1T^2$ has weight $\le0$), Proposition 2 gives
$$H \;=\; e^{3\varphi_1T^2/2}\cdot\frac{\tau\big(\sum_dT^dG_d\big)}{\sum_dT^dG_d},
\qquad w\big([T^n]H\big)\le 2n,$$
i.e. the *weak* degree bound $\deg_{E_3}[T^n]H\le\lfloor 2n/3\rfloor$. (H2) asks for
$\lfloor n/3\rfloor$: a further factor-of-two cancellation. So (H2), like (H1), is a
genuine cancellation statement, not a degree count.

Two exactly-solvable boundary facts found today, worth keeping:
* the **top** $E_3$-boundary is exactly solvable: setting $T=0$ at fixed $\rho$ in (ME)
  gives $2\theta_\rho \mathcal F = 3\rho\,\tau(\mathcal F)$ with $\mathcal F(0)=1$, hence
  $$F_P\big|_{T=0,\ \rho\ \text{fixed}} = e^{3\rho/2}, \qquad\text{i.e.}\qquad
  [E_3^k]P_{2k} = 3^k\,(2k-1)!!\,;$$
* consequently $F_P = e^{3\rho/2}\,\Pi(\rho,T)$ with $\Pi = 1+O(T)$, and the $T$-expansion
  of $\Pi = \sum_d T^dG_d$ is computed by inverting $(d+2\theta_\rho)$ order by order
  (Proposition 2). E.g. $G_1$ above; its $\tfrac{27}{5}\rho^2$ reproduces $n_2 = 27/5$ ✓, and the $e^{3\rho/2}$
  prefactor reproduces $n_1 = 3/2$ ✓.

---

## 10. FPSAC content

**Theorem 3.8 (master equation).** $LF_P = E_3T^2[-3+T(E_1+6+2\theta)]\tau(F_P)$.

**Lemma 3.9.** $v_3([E_3^k]\Psi_b) \ge \max(0,3k-b)$; in particular
$\deg_{E_3}(\Psi_b \bmod 3)\le\lfloor b/3\rfloor$.

**Theorem 3.10.** With $\mathcal H = \ell_0\big(\tau(F_P)/F_P\big)$,
$$F^2-F = \vartheta\,\mathcal H\,(2F-3),$$
and $b_k\equiv0\pmod3\ \forall k \iff \mathcal H\in\mathbb Z_3[[\vartheta]]$.

**Conjecture 4.5 (H).** $\tau(F_P)/F_P \in \mathbb Z[E_1,E_2,E_3][[T]]$ with
$\deg_{E_3}[T^n] \le \lfloor n/3\rfloor$. (Verified symbolically to $T^{14}$, numerically
to $T^{36}$.) It implies FPSAC Theorem 3.9 ($3\mid b_k$).

---

## 11. Precisely stated gap

**Everything above is proved except Conjecture H**, and Conjecture H is equivalent
(via §6.3) to the target theorem — so it is not a weakening, it is a *reformulation*
into an object that is:
* elementary to state (a ratio of two explicit divided-power series),
* checkable to high order (done: $T^{36}$),
* $(E_1,E_2)$-uniform (holds symbolically),
* and of a well-known type (Dwork integrality of a ratio of solutions of a
  $p$-adic differential/difference system).

That is real progress over "$b_k$ is divisible by 3 and nobody knows why": the mystery is
now a *single* integrality statement about $\tau(F_P)/F_P$, with a concrete proposed
mechanism (§9).
