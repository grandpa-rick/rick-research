# Day 147 attack plan — the Dwork defect from the DEFINITION side

**Author:** research agent, for Rick. **Date:** 2026-08-30.
**Inputs read:** `~/projects/proofs/2026-08-29-day146-bk-mod3-master-equation.md`,
`day146_prove/RESULT.md`, `day146_prove/core.py`,
`~/projects/memory/connections/2026-08-29-day146-dream-dwork-lambda-ring-frobenius.md`.

All claims below marked **[V]** were verified computationally today by scripts in this
directory. Claims marked **[C]** are conjectural. Claims marked **[?]** are unverified
reasoning.

---

## Task A — the circularity verdict: **Rick is right**, and here is the sharp form

### A.1 Dependency graph (what depends on what)

```
  Psi-recursion (Day 131 Thm A)                        <-- the ONLY primitive input
        |
        |--(phi-twist, gen.fn.)-->  (ME)  master equation                       [proved]
        |                              |
        |                              |--(divide by F_P)--> (ME_Lambda)        [proved]
        |
        |--(path/composition count)--> Lemma A (deg_E3 <= b/2)                  [proved]
        |--(path count, 3^s factor)--> Lemma B (v_3 >= 3k-b)                    [proved]
        |                                    |
        |                                    +--> Corollary: Psi_{3m} = (gamma+delta sigma)^m(1) mod 3
        |
        +--(divided-power valuations)-> Lemma C  (K in 1+3 Gamma)               [proved]

  (ME_Lambda) + (H2)  --> Prop 1 (ord Lambda >= -1)                             [proved-if-H2]
  (ME_Lambda) + (H2) + Prop 1 + [ell_{-1} extraction] --> Thm 2 = MAIN IDENTITY (6.1)
  Thm 2 + (H1) --> Thm 3 (3 | b_k)
  Thm 2 alone  --> the EQUIVALENCE  Hcal in Z_3[[vartheta]]  <=>  3 | b_k
```

Everything is downstream of the recursion. **Nothing in the chain is an independent
arithmetic input.**

### A.2 Why the main identity carries zero arithmetic information

Sharper than "it is circular": *identity (6.1) is exactly the order-$(-1)$ graded
component $\ell_{-1}$ of (ME$_\Lambda$)* (this is literally how §6.2 proves it). It
relates the two unknown one-variable series $F$ and $\mathcal H$ by

$$F^2-F=\vartheta\,\mathcal H\,(2F-3).$$

Read as a map of formal power series this is a **bijective change of variables**:

* given $\mathcal H\in\mathbb Q[[\vartheta]]$, (6.1) determines $F$ uniquely with $F(0)=0$
  (the implicit-function/Newton iteration converges since $\partial_F$ of the relation is
  $2F-1-2\vartheta\mathcal H$, a unit);
* given $F$, (6.1) determines $\mathcal H = F(1-F)/(\vartheta(3-2F))$ uniquely.

A bijection between two unknowns **cannot constrain either of them**. Both
"$3\mid b_k$ for all $k$" and its negation are consistent with (6.1) alone. §6.3 says this
in the write-up's own words ("(H1) is not merely sufficient — it is equivalent"). So:

> **VERDICT (Task A): confirmed.** Any argument whose only inputs are (H2), (6.1), and
> formal algebra in $\mathbb Z_3[[\vartheta]]$ is circular. In particular, substituting
> $\mathcal H=(F^2-F)/(\vartheta(2F-3))$ into the Dwork defect
> $\mathcal H(\vartheta)^3/\mathcal H(\vartheta^3)$ produces a statement equivalent to
> $F(\vartheta)^3\equiv F(\vartheta^3)$, i.e. Day 145 attack (A). Guaranteed circular.

### A.3 Is there ANY independent input hiding? Yes — three, and they are all "$\ell_{d\ge0}$"

(6.1) uses **one** graded component of (ME$_\Lambda$). The remaining components are free,
non-circular information:

1. **The $\ell_0$ component of (ME$_\Lambda$)** (derived in §D.4 below). It is a genuinely
   new identity linking $\mathcal H$, the second diagonal $M_0:=\ell_0(\Lambda)$, and
   $\mathcal H_1:=\ell_1(H)$. Rick's `secdiag.py` datum ("second diagonal of $X$ is
   *linear in $E_1$, no $E_2$*") is an empirical constraint on exactly these objects.
2. **The $(E_1,E_2)$-dependence.** $F$ and $\mathcal H$ are $(E_1,E_2)$-free, but
   $\Lambda,H,X$ are not. Every $E$-graded piece of (ME$_\Lambda$) is a separate equation.
   This is real leverage and is invisible at the $\ell_{-1}$ level.
3. **The exact boundary solutions** ($[E_3^k]P_{2k}=3^k(2k-1)!!$, Prop 2's
   $e^{-3\rho/2}F_P=\sum T^dG_d$). Definition side, exactly solvable.

So the situation is not "no independent input exists"; it is "the independent input is not
where Days 143–146 were looking".

### A.4 A correction to §9 that matters (found today) **[V]**

§9 / `RESULT.md` state:

> (H1) $\iff \tau(K)/K \in 1+3T\,\mathbb Z_3[E][[T]]$, where $K=F_P^3/\varsigma(F_P)(T^3)$,
> *"since $\tau$ acts on coefficients only, $\varsigma$ and $\tau$ commute on the locus
> $\varphi_1=0$"*, and *"without the $E_3\mapsto E_3^3$ twist the criterion genuinely
> fails; with the twist it holds. Checked."*

Three problems, all verified:

* **$\varsigma$ and $\tau$ do NOT commute**, not even on $\varphi_1=0$. At the base point
  $(E_1,E_2)=(-2,1)$ (where $\varphi_1=0$): $\varsigma\tau(-2,1)=\varsigma(1,0)=(1,0)$ but
  $\tau\varsigma(-2,1)=\tau(-8,1)=(-5,-12)$. They agree only **mod 3** — which is exactly
  the property the dream's $\psi^3$ argument gives, and exactly what dies at the $3^2$
  level (see below). **[V]**
* `dwork.py`/`dwork2.py` do not implement any twist at all: their `frob(A,N)` maps
  $T^b\mapsto T^{3b}$ and leaves the $E_3$-key untouched, i.e. $\varsigma=\mathrm{id}$,
  which is **not a Frobenius lift**. Their reported "$T^9$ violation" is therefore an
  artefact, not evidence about the twist. **[V]**
* A numeric base point cannot test any nontrivial $\varsigma$, because $\varsigma$ *moves
  the point*. The test must be symbolic.

Done correctly (`dwork_symbolic.py`, symbolic in $\mathbb Z[E_1,E_2,E_3]$ to $T^{12}$):

| lift $\varsigma$ | $H^3/\varsigma(H)(T^3)\in1+3T\mathbb Z[E][[T]]$? |
|---|---|
| identity (not a lift) | **NO** (fails already at $T^3$) |
| naive $E_i\mapsto E_i^3$ | **YES** |
| Adams $\psi^3$ | **YES** |

This is as it must be (Dieudonné–Dwork is an *iff* and $H$ is integral), and it settles
the record: **the criterion is insensitive to which lift you take; use the clean form
$H^3/\varsigma(H)(T^3)$ with $\varsigma$ applied to coefficients, and drop the
$\tau(K)/K$ rewriting entirely.** The $\tau(K)/K$ form buys nothing and costs a false
commutation lemma.

$\psi^3$ (Adams): $\psi^3(E_1)=E_1^3-3E_1E_2+3E_3$, $\psi^3(E_2)=E_2^3-3E_1E_2E_3+3E_3^2$,
$\psi^3(E_3)=E_3^3$. **[V]** (checked against $e_i(u_1^3,u_2^3,u_3^3)$).

---

## Task B — the $(\gamma+\delta\sigma)^m$ word expansion

### B.1 The formula

$\sigma$ is a ring automorphism, so with $M_x$ = "multiply by $x$" and $S$ = "apply
$\sigma$" we have $S\,M_x = M_{\sigma(x)}\,S$. Hence for a word of length $m$ in
$\{\Gamma:=M_\gamma,\ \Delta S:=M_\delta S\}$ applied to $1$ (leftmost letter = outermost
operator), with $\Delta S$ in positions $i_1<\cdots<i_r$: push every $S$ to the right; the
letter in position $j$ acquires $\sigma^{(\#\{l:\,i_l<j\})}$, and $S^r(1)=1$. Grouping the
$\Gamma$'s by how many $\Delta S$'s precede them ($g_l$ = number of $\Gamma$'s strictly
between $i_l$ and $i_{l+1}$, with $i_0=0,\ i_{r+1}=m+1$):

$$\boxed{\;(\gamma+\delta\sigma)^m(1)\;=\;\sum_{r=0}^{m}\ \ \Big(\prod_{l=0}^{r-1}\sigma^l(\delta)\Big)
\sum_{\substack{g_0,\dots,g_r\ge0\\ g_0+\cdots+g_r=m-r}}\ \prod_{l=0}^{r}\sigma^l(\gamma)^{\,g_l}\;}$$

with $\gamma=\alpha\beta E_2$, $\alpha=E_2-E_1+1$, $\beta=E_2+E_1+1$, $\delta=E_1E_3$, and

$$\sigma^l(E_1)=E_1-3l,\qquad \sigma^l(E_2)=E_2-2lE_1+3l^2,\qquad
\sigma^l(E_3)=E_3-lE_2+l^2E_1-l^3 .$$

Combinatorially: $r$ is the $E_3$-degree, the inner sum is a "multi-homogeneous complete
symmetric function" $h_{m-r}(\sigma^0\gamma,\dots,\sigma^r\gamma)$, so

$$(\gamma+\delta\sigma)^m(1)=\sum_{r=0}^m \Big(\prod_{l=0}^{r-1}\sigma^l(\delta)\Big)\,
h_{m-r}\big(\gamma,\sigma\gamma,\dots,\sigma^r\gamma\big) .$$

### B.2 Verification **[V]** (`taskB_words.py`)

* $(\gamma+\delta\sigma)^m(1)\equiv\Psi_{3m}\pmod 3$ for $m=0,\dots,6$ (i.e. through
  $\Psi_{18}$) — **TRUE**, both by direct operator iteration and by the boxed closed
  formula.
* $\Psi_{3m+1}\equiv\alpha\Psi_{3m}$, $\Psi_{3m+2}\equiv\alpha\beta\Psi_{3m}\pmod3$ for
  $m\le6$ — **TRUE**.

Consequence worth recording (ordinary generating function, mod 3):
$$\sum_{b\ge0}\Psi_bT^b\;\equiv\;(1+\alpha T+\alpha\beta T^2)\;\Theta(T^3)\pmod 3,\qquad
\Theta(S)=\sum_m\Theta_mS^m,\ \ (1-S\gamma)\Theta=1+S\delta\,\sigma(\Theta).$$
This is a textbook Frobenius/Dwork self-similarity — **but for the ORDINARY generating
function**, while $F_P$ is the EXPONENTIAL one. That mismatch is §8's obstruction in one
line, and it is the single biggest risk in the whole programme (see §D.6).

---

## Task C — what the $E_3$-degree does

$\gamma$ and all $\sigma^l(\gamma)$ are $E_3$-free; $\sigma^l(\delta)$ has $E_3$-degree
exactly 1. So in the boxed formula the term indexed by $r$ has $E_3$-degree exactly $r$,
whence $\deg_{E_3}(\Psi_{3m}\bmod3)\le m$ — Lemma B, re-derived, and **sharp** [V].

**Top coefficient.** Only the all-$\Delta S$ word ($r=m$) survives, and taking $E_3$ from
each factor of $\prod_{l=0}^{m-1}(E_1-3l)(E_3-lE_2+l^2E_1-l^3)$:

$$\boxed{\;[E_3^m]\,\Psi_{3m}\;\equiv\;\prod_{l=0}^{m-1}(E_1-3l)\;\equiv\;E_1^{\,m}\pmod 3\;}$$

**[V]** for $m\le6$ (`taskB_words.py`).

**The diagonal that actually carries $b_k$ is one step lower, and it is also exactly
computable.** The $b_k$-relevant order-$(-1)$ diagonal sits at $B=3k-1$, where Lemma B is
sharp ($v_3=1$ exactly). Repeating the path argument one order deeper (only the
$-3bE_3\sigma(\Psi_{b-2})$ branch contributes at $v_3=1$; the $\varphi$-branch has
$v_3\ge2$ and the length-3 branch carries an extra $3\mid b(b-1)$):

$$\boxed{\;\tfrac13\,[E_3^k]\,\Psi_{3k-1}\;\equiv\;-(3k-2)\,\sigma\big(E_1^{k-1}\big)\;\equiv\;-E_1^{\,k-1}\;\equiv\;2E_1^{k-1}\pmod 3\;}$$

**[V]** for $k=1,\dots,7$ (`taskC_sharpdiag.py`), together with $v_3=1$ exactly.

**Honest caveat.** These are facts about $\Psi_b$, *not* about $b_k$. $b_k$ is extracted
from $\log F_P$ and the extraction divides by $(3k-1)!$. Both boxed formulas are therefore
*consistent with* but do *not imply* $3\mid b_k$.

---

## Task D — the attack plan

Ordering below is by **(information gained)/(effort)**, highest first. Steps 1–3 are the
core; 4–7 are supporting/fallback.

### D.0 The one genuinely new structure found while writing this plan (do this first)

Three facts, all verified today, that together replace Conjecture H by something with a
completely standard shape and **no factorial denominators anywhere**:

**Fact 1 [V] (`lambda_int.py`).** $\Lambda:=\theta F_P/F_P=\theta\log F_P$ is an
**ordinary integral series**: $\Lambda\in\mathbb Z[E_1,E_2,E_3][[T]]$, verified
symbolically to $T^{14}$; all denominators are $1$; $\mathrm{ord}\,\Lambda=-1$ exactly.
Call this **Conjecture L**. It is *not* automatic (e.g. $G=1+T^2/2!\in\Gamma_{\mathbb Z}$
has $\theta G/G\notin\mathbb Z[[T]]$), and it is strictly weaker than the target: it
implies only $b_k=(3k-1)n_k\in\mathbb Z$, which is already known.

Reformulation: $F_P=\exp\big(\sum_{n\ge1}\Lambda_n T^n/n\big)$, i.e. **$F_P$ is a
$\mathbb Q$-point of the big Witt ring whose ghost vector $(\Lambda_n)$ is integral.**
$F_P$ itself is not integral — its ghost vector violates the Dwork congruences — but the
ghost vector is.

**Fact 2 [V] (`ghost.py`).** The cocycle identity
$$\theta H \;=\; H\cdot\big(\tau\Lambda-\Lambda\big),\qquad\text{i.e.}\qquad
H=\exp\Big(\sum_{n\ge1}\frac{\ell_n}{n}T^n\Big),\quad \ell_n:=\tau(\Lambda_n)-\Lambda_n,$$
holds **exactly** (verified to $T^{14}$; it is a two-line consequence of
$H=\tau F_P/F_P$ and $[\theta,\tau]=0$ — worth writing out as a lemma).
So the ghost vector of $H$ is $(\tau-1)$ applied to the ghost vector of $F_P$.

**Fact 3 [V] (`ghost.py`).** By Dwork's lemma in ghost form (Hazewinkel 17.6.1: for
$p$-torsion-free $p$-adically complete $R$ with Frobenius lift $\varsigma$,
$\exp(\sum \ell_nT^n/n)\in1+TR[[T]] \iff \ell_n\equiv\varsigma(\ell_{n/3})\bmod
3^{v_3(n)}$ for all $n$, with $\ell_{n/3}:=0$ when $3\nmid n$):

$$\boxed{\ \textbf{(H1) at }p=3\iff \ell_n\equiv\varsigma\big(\ell_{n/3}\big)
\ \big(\mathrm{mod}\ 3^{v_3(n)}\big)\quad\forall n\ }$$

Verified for $n=3,6,9,12$ with both the naive lift and $\psi^3$: **ALL HOLD** (including
$n=9$ mod $9$). At $v_3(n)=1$ the criterion is simply
$\ell_{3m}\equiv\ell_m^{\,3}\pmod 3$.

**Fact 3' [V] (`delta_tau.py`).** Setting $\Delta_n:=\Lambda_n-\psi^3(\Lambda_{n/3})$ (the
Dwork defect of $F_P$'s own ghost vector), the $v_3(n)=1$ case of Fact 3 is equivalent to

$$\Delta_{3m}\ \text{is}\ \tau\text{-invariant mod }3 ,$$

verified for $n=3,6,12$. **Caution:** the same rewriting *fails* at $n=9$ modulo $9$
(the obstruction is exactly $3\cdot(\dots)$, i.e. the commutator $[\tau,\psi^3]\in3\cdot(\cdot)$).
So the $\tau$-invariance packaging is legitimate **only at $v_3=1$**; at higher $v_3$ use
the ghost congruence $\ell_n\equiv\varsigma(\ell_{n/3})$ directly.

**Why this matters.** $\tau$-invariance mod 3 is a *finite, structural, decidable*
condition. Mod 3 the operator $\tau$ ($u_i\mapsto u_i+1$) satisfies $\tau^3=\mathrm{id}$
on $\mathbb F_3[u_1,u_2,u_3]$, so we are asking for membership in the invariant ring of a
$\mathbb Z/3$-action:
$$\mathbb F_3[u]^{\mathbb Z/3}=\mathbb F_3[u_1-u_3,\ u_2-u_3,\ u_3^3-u_3],$$
intersected with $\mathbb F_3[u]^{S_3}=\mathbb F_3[E_1,E_2,E_3]$. Explicit symmetric
$\tau$-invariants mod 3 include $e_i(u_1^3-u_1,u_2^3-u_2,u_3^3-u_3)$ for $i=1,2,3$ (e.g.
$e_1 = p_3-p_1\equiv E_1^3-E_1$) and the discriminant $\prod_{i<j}(u_i-u_j)^2$.
**Step D.1 below is: compute this subring explicitly and test membership of $\Delta_{3m}$.**

### D.1 (TOP PRIORITY) Nail the $\tau$-invariance criterion and its generators

*Compute.* (a) The $S_3$-invariant part of $\mathbb F_3[u]^{\mathbb Z/3}$: find a
generating set / Hilbert series (Magma-free: linear algebra degree by degree in
$\mathbb F_3[E_1,E_2,E_3]$, solving $\tau(g)=g$; degrees $\le 12$ suffice to see the
pattern). (b) Extend $\Lambda_n$ symbolically to $n\le 21$ (the $T^{14}$ ceiling of
`symH.py` is a memory/time artefact, not fundamental; use `core.py` dicts, prune by
$E_3$-degree using Lemma A). (c) Test: is $\Delta_{3m}=\Lambda_{3m}-\psi^3(\Lambda_m)$ in
the invariant subring mod 3 for $m\le7$? Is $\Delta_{3m}$ perhaps *identically* a specific
invariant (e.g. a polynomial in $E_1^3-E_1$ and the discriminant)?

*Expected outcome.* $\Delta_{3m}$ lands in the invariant subring, and (optimistically) in a
small explicit sub-family. That would turn the target into a closed-form identity.

*Falsified if.* $\Delta_{3m}$ is invariant but lies in no recognisable sub-family, i.e. the
invariance is the whole content and there is no extra structure. (Then go to D.2.)

*Effort.* 1 h. *Information.* Very high: it is the first time the target is a **finite
algebraic membership condition** rather than an infinite integrality assertion.

### D.2 (TOP PRIORITY) Prove Conjecture L ($\Lambda$ integral) from the master equation

This is the one piece of the new chain that is *not* equivalent to the target, so proving
it is pure profit and it is plausibly easy.

*Compute/derive.* From (ME$_\Lambda$), extracting $[T^n]$ (note the $-\Lambda$ term has
coefficient exactly $-1$, so the recursion is **division-free**):
$$\Lambda_n=\varphi_1\delta_{n,1}+(E_1+n+1)\Lambda_{n-1}+\!\!\sum_{i+j=n-1}\!\!\Lambda_i\Lambda_j
\;+\;E_3\Big(3H_{n-2}-(E_1+2n)H_{n-3}-2\!\!\sum_{i+j=n-3}\!\!H_i\Lambda_j\Big).$$
So: **$\Lambda$ is integral as soon as $H$ is**, and $H$ is integral as soon as $\Lambda$
is *and* the ghost congruences hold. Therefore prove L *independently*: by induction using
only $\Lambda$-data, i.e. show $E_3 H_{n-2}$-terms can be eliminated. Two routes:
(i) use $H=\exp(\int(\tau\Lambda-\Lambda)dT/T)$ to make the recursion closed in $\Lambda$
alone, then show the only denominators introduced are cancelled — this is where the
congruences bite, so it is **not** independent; (ii) prove L directly from
$\Lambda_n=n[T^n]\log F_P$ plus Prop 2's exponential normal form
$e^{-3\rho/2}F_P=\sum_dT^dG_d$ — the $\rho$-denominators are $d+2k$ and the $T$-denominators
are $n$; show they always match. Route (ii) is definition-side and non-circular.

*Expected outcome.* L proved, or reduced to a clean divisibility of the $G_d$'s.
*Falsified if.* $\Lambda$ fails integrality at some $n>14$. (Cheap first move: verify L to
$T^{24}$ numerically at 3–4 base points before investing in a proof.)
*Effort.* 1–1.5 h. *Information.* High; and L is a publishable lemma on its own
("$F_P$ has integral ghost vector") that strengthens the FPSAC write-up regardless.

### D.3 Re-derive the Dwork defect from the recursion — the only non-circular target

The chain is now:
```
  Psi-recursion --> (ME) --> (ME_Lambda) --> [division-free] Lambda_n
        --> ell_n = (tau-1)Lambda_n  --> ghost congruences  <=>  H integral  <=>  3 | b_k
```
No step uses (6.1). **This is the non-circular route Rick asked for.**

*Compute.* Run the coupled mod-3 system: $\Lambda_n\bmod 3$ from the division-free
recursion above, $H_n\bmod3$ from $nH_n=\sum_{i<n}H_i\ell_{n-i}$. The system is
**determined for $3\nmid n$ and under-determined exactly at $n\equiv0\ (3)$** — the
missing datum at each $n=3m$ is precisely the Dwork congruence. Tabulate what the missing
datum is (one polynomial in $\mathbb F_3[E_1,E_2,E_3]$ per $m$), and compare it against
$\Theta_m=(\gamma+\delta\sigma)^m(1)$ and against $[E_3^m]\Psi_{3m}\equiv E_1^m$.

*Expected outcome.* An explicit finite list of "one new polynomial per $m$", plus (hoped)
a visible match with $\Theta_m$.
*Falsified if.* No relation to $\Theta_m$ is visible — see the risk in D.6.
*Effort.* 1 h. *Information.* High: this is the exact locus of the remaining difficulty,
made explicit for the first time.

### D.4 The $\ell_0$ level of (ME$_\Lambda$) — the untapped independent identity

Applying $\ell_0$ to (ME$_\Lambda$) (using: $\theta$ acts as $d+3\theta_\vartheta$ on
order-$d$ parts; $\ell_d(W_1W_2)=\sum\ell_{d_1}W_1\ell_{d_2}W_2$; $\ell_{d-1}(\rho W)=\vartheta\ell_d(W)$),
with $M_0:=\ell_0(\Lambda)$ and $\mathcal H_1:=\ell_1(H)$:

$$(E_1+1)F+3\theta_\vartheta F+2FM_0-M_0
=\vartheta\Big[(E_1+6)\mathcal H+6\theta_\vartheta\mathcal H+2\mathcal H M_0+\mathcal H_1(2F-3)\Big].\qquad(\ell_0)$$

**[?] — derived here, NOT yet verified numerically. Verify it first** against
`secdiag.py` (whose output "$\ell_0(X)=-12-5E_1,\ -360-99E_1,\dots$" is precisely the LHS)
before using it.

*Why it is independent.* It is a *different graded component* of the same master equation;
(6.1) is $\ell_{-1}$. Splitting $(\ell_0)$ by $E_1$-degree (using that $F,\mathcal H$ are
$E_1$-free and that $\ell_0(X)$ is empirically **linear in $E_1$ with no $E_2$**) yields
two equations in the two new unknowns $M_0,\mathcal H_1$ — potentially closing the system
and producing a second functional equation for $\mathcal H$.

*Expected outcome.* A new identity of the type "$\mathcal H_1$ = explicit in $F,\mathcal H$".
*Falsified if.* $M_0$ is not linear in $E_1$ at higher order, or the split does not close.
*Effort.* 1 h. *Information.* Medium-high, and it is the cheapest *new* algebraic input.

### D.5 Housekeeping that must happen before the FPSAC write-up

* **Delete the $\tau(K)/K$ formulation from §9** and replace it with the clean
  $H^3/\varsigma(H)(T^3)\in1+3T\mathbb Z_3[E][[T]]$, $\varsigma$ acting on coefficients.
  Remove the false claim that $\varsigma$ and $\tau$ commute on $\varphi_1=0$ (A.4).
* **Retract the claim "without the $E_3\mapsto E_3^3$ twist the criterion genuinely
  fails"**: `dwork.py`/`dwork2.py` used $\varsigma=\mathrm{id}$, which is not a lift; the
  correct symbolic test passes for *both* the naive lift and $\psi^3$ (A.4).
* State $\psi^3$ explicitly (the λ-ring lift) and note that the criterion is lift-independent,
  so the λ-ring is *aesthetically* right (canonical, commutes with $\tau$ mod 3) but is
  **not load-bearing** — the dream's §3 "crown jewel" is a genuine clarification but does
  not, by itself, unlock anything. Say so.
* Replace Conjecture H by Conjecture L + the ghost congruences (D.0). Strictly cleaner:
  L is a *new* statement not equivalent to the theorem, and the ghost congruences are the
  standard shape a referee will recognise.
* Adopt the dream's §2 descent (state the target on the $\vartheta$-diagonal over
  $\mathbb Z_3$, one variable) as the *statement*, keeping the $E$-level as the *proof
  arena*.

*Effort.* 45 min. *Information.* Low mathematically, high for correctness of the record.

### D.6 THE RISK — where this could still be secretly circular or blocked

Flagged honestly, in decreasing order of danger:

1. **§8's obstruction has not gone away.** $\ell_n\bmod3$ is *not* a function of
   $\{P_b\bmod 3\}$ — the passage from $P_b$ to $\Lambda_n$ divides by $b!$. The
   $(\gamma+\delta\sigma)^m$ structure lives in $\mathbb F_3[E][[T]]$ with the **ordinary**
   generating function; $\Lambda,H,\ell$ live in the **exponential** one. **I did not find
   a bridge, and §8 says a mod-3-only bridge cannot exist.** Any step that claims to
   compute $\ell_{3m}\bmod3$ from $\Theta_m$ must be audited for this. This is the single
   most likely failure mode of the whole Day 147 programme.
2. **Steps that would secretly re-use the main identity.** (a) Any use of
   "$\mathcal H=(F^2-F)/(\vartheta(2F-3))$" — banned outright. (b) Any use of $\ell_{-1}$
   of (ME$_\Lambda$) — that *is* (6.1). (c) Using $\mathcal H\in\mathbb Z_3[[\vartheta]]$
   as an input to derive $3\mid b_k$ and then $3\mid b_k$ to derive something about
   $\mathcal H$. (d) Using the $\vartheta$-diagonal Dwork criterion
   $\mathcal H^3/\mathcal H(\vartheta^3)$ *evaluated via* $F$ — circular; it must be
   evaluated via $\ell_0$ of the $E$-level defect.
3. **$F$ is very likely non-holonomic** (`search.py`: no P-recurrence of order $\le4$,
   degree $\le4$, for $b_k$ or $h_j$). So classical Dwork *differential-equation* machinery
   (Frobenius structure on an ODE, unit root, Christol) is probably unavailable. Do not
   plan around it. Krattenthaler–Müller-style explicit $v_3$ bounds are the realistic tool.
4. **Prop 1 is conditional on (H2).** Any argument reusing "$\mathrm{ord}\,\Lambda\ge-1$"
   inherits that. Note however §6.1's remark gives an *unconditional* proof that
   $\mathrm{ord}\,\Lambda\ge-1$ (the $N\ge2$ leading-term contradiction) --- **but audit
   it**: that argument bounds the order of the right-hand side by "$\ge-N$", which
   appears to need a hypothesis on $\mathrm{ord}\,H$, i.e. (H2) again. If the audit
   succeeds, promote the remark to a theorem and delete the (H2) hypothesis from Prop 1
   (cheap, removes a conditional from the FPSAC paper). Today's `lambda_int.py` confirms
   $\mathrm{ord}\,\Lambda=-1$ exactly to $T^{14}$ **[V]**.

### D.7 Fallback if D.1–D.4 all stall

* Restrict to the $\tau$-stable line $U=V$ (equivalently $E_1^2=4E_2$), which contains the
  base point $(U,V)=(0,0)$ where $f\equiv1$ and $F_P=1+O(E_3)$; the whole problem is
  $(E_1,E_2)$-free so nothing is lost. On this line $\varphi_k=(U+k-1)^2$ and the
  recursion is markedly simpler. Recompute $\Lambda_n,\ell_n$ there symbolically in the
  single parameter $U$ to $T^{30}$.
* Read Krattenthaler–Müller arXiv:1412.7014 (truncated Dwork / quantitative $v_p$ bounds
  for combinatorial sequences). Per the dream, promote to primary tool.
* Do **not** spend time on Dabrowski arXiv:1309.5902 beyond a 5-minute abstract check —
  different theorem (dream §1).

---

## Ranked summary

| # | step | effort | info | non-circular? |
|---|---|---|---|---|
| 1 | D.1 $\tau$-invariance criterion + invariant subring; test $\Delta_{3m}$ | 1 h | very high | yes |
| 2 | D.2 prove Conjecture L ($\Lambda$ integral) via Prop 2 | 1–1.5 h | high | yes (route ii only) |
| 3 | D.3 run the coupled mod-3 $(\Lambda,H)$ system; isolate the missing datum at $n\equiv0$ | 1 h | high | yes |
| 4 | D.4 verify + exploit the $\ell_0$ component of (ME$_\Lambda$) | 1 h | med-high | yes |
| 5 | D.5 corrections to §9 (drop $\tau(K)/K$, retract twist claim, unconditional Prop 1) | 45 min | low math / high hygiene | n/a |
| 6 | D.7 fallbacks ($U=V$ line; Krattenthaler–Müller) | — | — | yes |

## Scripts in this directory

| file | what it verifies |
|---|---|
| `taskB_words.py` | word expansion $=\Psi_{3m}$ mod 3 ($m\le6$); $\alpha,\alpha\beta$ steps; $[E_3^m]\Psi_{3m}\equiv E_1^m$ |
| `taskC_sharpdiag.py` | $\frac13[E_3^k]\Psi_{3k-1}\equiv-E_1^{k-1}$ mod 3, $k\le7$; $v_3=1$ sharp |
| `psi3.py` | Adams $\psi^3$ on $E_1,E_2,E_3$ |
| `dwork_symbolic.py` | correct symbolic Dieudonné–Dwork test for 3 lifts |
| `dwork_twist.py` | shows the numeric-base-point test is invalid ($\varsigma$ moves the point) |
| `lambda_int.py` | **Conjecture L**: $\Lambda\in\mathbb Z[E][[T]]$ to $T^{14}$; $\mathrm{ord}=-1$ |
| `ghost.py` | cocycle $\theta H=H(\tau\Lambda-\Lambda)$; ghost Dwork congruences $n\le14$ |
| `delta_tau.py` | $\tau$-invariance of $\Delta_n$ mod 3 (and its failure mod 9) |
