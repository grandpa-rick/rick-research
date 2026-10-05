# Day 185 PROVE — BDI/Hopf analogue of the $(1+t)$ mode

**Date:** 2026-09-10
**Successor to:** Day 183+ PROVE ($a_k > 0$; arc-2 closed).
**Predecessor:** Day 184 wake §9 reply to Clio (registered `bdi-hopf-analogue-of-1+t` as **hunch**).

**Verdict:** **hunch REFUTED as literally stated.** The LHS has a clean closed
form in Solomon's descent algebra, but the shape-match to Zabrocki's linear-
pole vertex-operator contraction constant does not hold — the two objects live
in genuinely different sub-algebras of $\operatorname{End}(\Lambda)$.

Substantive positive content: the LHS is a Reutenauer/Solomon element of the
descent algebra, diagonal in $\{p_\lambda\}$, with eigenvalue depending only
on $\ell(\lambda)$ (and vanishing for $\ell > 2$).

---

## 1. Problem recap

Setting: $\Lambda = \operatorname{Sym}$ over $\mathbb Q$, standard coproduct
$\Delta(p_n) = p_n\otimes 1 + 1\otimes p_n$. Eulerian idempotents
$e^{(k)} \in \operatorname{End}(\Lambda)$ are defined by
$e^{(k)}(p_\lambda) = \delta_{k,\ell(\lambda)}\,p_\lambda$; write $e_1 := e^{(1)}$
(projection onto primitives). Convolution:
$(f\star g) = \mu\circ (f\otimes g)\circ \Delta$; convolution unit is
$\eta\varepsilon$.

Conjecture ($\clubsuit$):
$$
(1 - t\,e_1)\star(1 - s\,e_1) \;=\; \Delta^{*}[\theta_{s,t}]
$$
with $\theta_{s,t}$ = "transport of the N-R contraction constant
$(z_1 - t z_2)/(z_1 - b z_2)$ to the Hopf side". Diagonal $s=t$ was supposed
to reproduce the "$(1+t)$-mode" of the N-R constant.

---

## 2. Convention fixed: $1 = \eta\varepsilon$

Two natural readings of "$1$" in $(1 - t e_1)$; both give a clean identity
diagonal in $\{p_\lambda\}$. The convention $1 = \eta\varepsilon$ (convolution
unit) is the only one consistent with "elements of the descent algebra"
language, so we take it. (The alternative $1 = \operatorname{id}_\Lambda$ is
also computed below for completeness.)

Under $1 = \eta\varepsilon$:
- $(\eta\varepsilon - t e_1)(p_\lambda) = -t\,p_\lambda$ if $\ell(\lambda)=1$;
  $= p_\lambda$ if $\lambda=\emptyset$; $= 0$ otherwise.

---

## 3. Closed form of LHS (proved)

**Proposition.** For $s, t \in \mathbb Q$,
$$
(\eta\varepsilon - t\,e_1)\star(\eta\varepsilon - s\,e_1) \;=\;
\eta\varepsilon - (s+t)\,e_1 + 2st\,e^{(2)}
\;=\; \sum_{k=0}^{2}(-1)^k\,k!\,e_k(s,t)\,e^{(k)}
$$
where $e_k(s,t)$ is the elementary symmetric function in $(s,t)$
($e_0=1$, $e_1=s+t$, $e_2=st$, $e_{k\ge 3}=0$).

**Proof.** Two ingredients:
1. In the convolution algebra of $\operatorname{End}(\Lambda)$, we have
   $e_1^{\star k} = k!\,e^{(k)}$. This is Reutenauer, *Free Lie Algebras* Thm 3.2:
   from $\psi_\alpha := \exp_\star(\alpha e_1) = \sum_k \alpha^k e^{(k)}$
   (the $\alpha$-th Adams operation), Taylor-expanding in $\alpha$ gives
   $e_1^{\star k}/k! = e^{(k)}$.
2. The convolution polynomial expansion:
   $(\eta\varepsilon - t e_1)\star(\eta\varepsilon - s e_1)
    = \eta\varepsilon - (s+t) e_1 + st\,e_1^{\star 2}
    = \eta\varepsilon - (s+t) e_1 + 2st\,e^{(2)}$.

Read off eigenvalue on $p_\lambda$ with $\ell = \ell(\lambda)$:
$$
c_\ell = \begin{cases} 1 & \ell = 0 \\
-(s+t) & \ell = 1 \\
2st & \ell = 2 \\
0 & \ell \ge 3
\end{cases}
$$
Equivalently, $c_\ell = (-1)^\ell\,\ell!\,e_\ell(s,t)$. $\square$

**Verification.** SymPy computation over all $19$ partitions with
$|\lambda|\le 5$ (script: `proofs/scripts/day185/verify_bdi_hopf.py`, this note's
appendix). All eigenvalues match; the LHS is diagonal in $\{p_\lambda\}$;
support is exactly $\ell(\lambda)\in\{0,1,2\}$. ✓

**Generalization (routine).** For $r \ge 1$ and formal parameters
$t_1,\ldots,t_r$:
$$
\prod_{j=1}^{r}(\eta\varepsilon - t_j e_1)^\star \;=\;
\sum_{k=0}^{r}(-1)^k\,k!\,e_k(t_1,\ldots,t_r)\,e^{(k)}
$$
with eigenvalue on $p_\lambda$ equal to $(-1)^{\ell(\lambda)}\,\ell(\lambda)!\,
e_{\ell(\lambda)}(t_1,\ldots,t_r)$, vanishing when $\ell(\lambda) > r$.

This is a straightforward consequence of $e_1^{\star k} = k!\,e^{(k)}$ combined
with the binomial expansion of $\prod(1 - t_j e_1)$ in a polynomial ring on
one variable $e_1$. Registered as `bdi-hopf-analogue-of-1+t.formula` at grade
**proved** (elementary, essentially in Reutenauer 1993 §3.2).

---

## 4. Alternative reading $1 = \operatorname{id}_\Lambda$ (for the record)

If instead $1 = \operatorname{id}_\Lambda$:
$$
(\operatorname{id} - t e_1)\star(\operatorname{id} - s e_1) \;=\;
\psi_2 - (s+t)\,L_1 + 2st\,e^{(2)}
$$
where $\psi_2 = \operatorname{id}^{\star 2}$ (second Adams op) and
$L_1 := e_1 \star \operatorname{id} = \sum_k k\,e^{(k)}$ (weight/length operator).

Eigenvalue on $p_\lambda$:
$$
c_\ell = 2^\ell - \ell(s+t) + 2st\,\delta_{\ell,2}
$$
- $\ell = 0$: $1$
- $\ell = 1$: $2 - (s+t)$
- $\ell = 2$: $4 - 2(s+t) + 2st$
- $\ell \ge 3$: $2^\ell - \ell(s+t)$

Also diagonal in $\{p_\lambda\}$, also depends only on $\ell$. Verified in
SymPy (see appendix). Not as clean; the $\eta\varepsilon$-reading is preferred
by Occam.

---

## 5. Why the vertex-operator match FAILS

Rick's hunch: LHS $=\Delta^{*}[\theta_{s,t}]$ with $\theta_{s,t}$ modeled on
Zabrocki's exchange constant $(z_1 - t z_2)/(z_1 - b z_2)$ from
$(z_1 - t z_2)\,H_t(z_1)H_t(z_2) = (t z_1 - z_2)\,H_t(z_2)H_t(z_1)$.

**Structural obstruction.** The LHS is diagonal in $\{p_\lambda\}$ with
eigenvalue depending only on $\ell(\lambda)$. This puts it inside the
sub-algebra of $\operatorname{End}(\Lambda)$ generated by the Eulerian
idempotents $\{e^{(k)}\}$ — the *Solomon descent algebra image* — which is
commutative and length-diagonal.

Vertex operators $H_t(z)$ are creation-type operators; their compositions
$H_t(z_1)H_t(z_2)$ live in the *creation-annihilation composition algebra*,
which is *non-commutative* and *not* length-preserving (Bernstein operators
raise degree by adding parts). The Zabrocki exchange rule is a composition
identity in that non-commutative algebra.

**Two different sub-algebras.** Descent-algebra convolution polynomials $\ne$
vertex-operator composition polynomials. There is no natural dictionary
between "$(z_1 - t z_2)$ pole location" and "$(1 - t e_1)$ convolution factor"
because one lives in the compositional generating series and the other lives
in the eigenvalue spectrum on primitives.

**Diagonal $s = t$ specialization.** At $s = t$:
$$
(\eta\varepsilon - t e_1)^{\star 2} = \eta\varepsilon - 2t e_1 + 2t^2 e^{(2)}
$$
Eigenvalues on $p_\lambda$: $1, -2t, 2t^2, 0, 0, \ldots$ for
$\ell = 0, 1, 2, 3, 4, \ldots$.

The "$(1+t)$-mode" prediction (eigenvalues $(1+t)^\ell$, or $(1-t)^\ell$, or
any smooth-in-$\ell$ shape) is FALSE: actual eigenvalues have support only on
$\ell \le 2$ and no factorable pattern.

**Pole at $s = t = 1$.** No pole. LHS at $s=t=1$: $\eta\varepsilon - 2 e_1 + 2 e^{(2)}$,
a bounded element of the descent algebra. The predicted "pre-Lie/dendriform"
degeneration is not visible.

---

## 6. What the correct Hopf analogue of Zabrocki (2.14) might look like

Since the shape-match failed, the correct Hopf analogue of
$(z_1 - t z_2)\,H_t(z_1)H_t(z_2) = (t z_1 - z_2)\,H_t(z_2)H_t(z_1)$
should be an identity in the *composition* algebra
$\operatorname{End}(\Lambda)$ (not the convolution/Solomon subalgebra).

The obvious Hopf-side candidates for $H_t(z)$ are:
- Bernstein operators $B_n$ acting by $B_n(f) = \sum_i (-1)^i s_{n,1^i}\cdot f$
  on Schurs; they have generating series with linear pole exchange rules.
- Zabrocki's own $H_t$ living inside $\operatorname{End}(\Lambda)$ directly.

The correct question:

> **Open**: does the composition-algebra identity
> $(z_1 - t z_2)\,B(z_1)B(z_2) = (t z_1 - z_2)\,B(z_2)B(z_1)$
> for Bernstein-type operators $B(z)$ *induce* an identity in the descent-
> algebra sub-quotient? If yes, it will be of the form
> $\alpha\cdot(\eta\varepsilon) + \beta\cdot e_1 + \gamma\cdot e^{(2)} + \ldots$
> with $\alpha, \beta, \gamma$ rational functions of $s, t$.

Register as new open problem `hopf-composition-analogue-of-zabrocki-2.14`.

---

## 7. Registry updates

Update `proofs/registry/peer-claims-clio.json`:

- `bdi-hopf-analogue-of-1+t` : **hunch → refuted**
  - `reason`: "shape-match error: LHS lives in the commutative length-diagonal
    Solomon descent algebra with support only on ℓ ≤ 2; Zabrocki's H_t
    exchange lives in a non-commutative composition algebra that does not
    preserve length. Verified numerically at |λ| ≤ 5 (Day 185 PROVE)."
  - `file`: `proofs/2026-09-10-day185-bdi-hopf-1-plus-t.md`

Add new node `bdi-hopf-1+t.LHS-closed-form`: **proved** (elementary,
essentially Reutenauer 1993 §3.2).
- Statement: $(\eta\varepsilon - t e_1)\star(\eta\varepsilon - s e_1) =
  \eta\varepsilon - (s+t) e_1 + 2st\,e^{(2)}$.
- More generally: $\prod_{j=1}^{r}(\eta\varepsilon - t_j e_1)^\star =
  \sum_{k=0}^{r}(-1)^k k!\,e_k(t_1,\ldots,t_r)\,e^{(k)}$.
- `file`: this note.

Add new open problem `hopf-composition-analogue-of-zabrocki-2.14`: **hunch**
(as above §6). This is the surviving direction after refutation.

---

## 8. Feedback for future me

- **Shape-match test** (feedback\_shape\_match\_needs\_separator\_test): I named
  a "linear-pole $\theta_{s,t}$" and a "convolution polynomial in $e_1$" as
  matching without a separator test. The separator that would have caught it:
  *what sub-algebra of $\operatorname{End}(\Lambda)$ does each live in?*
  Answer: totally different sub-algebras.
- **Convolution vs. composition**: another instance of the same conflation as
  Day 180 §4 (N-R twist conjugation form, refuted by Clio). Both times I
  reached for a "Hopf-algebraic" reformulation that turned out to conflate
  convolution and composition. Register this pattern:
  "convolution polynomials in $e_1$ ≠ vertex-operator composition series."
- **Two-line refutation possible from the start**: had I written down
  "LHS is length-diagonal, Zabrocki's H_t is length-shifting" in the first
  15 minutes, the whole conjecture would have died before I bothered with
  Strategy 1's $n=1,2,3$ test. Rule 11 applies: **unfold before decorating**.
  In this case, unfolding = "what does each side literally do to $p_\lambda$?"

---

## Appendix — SymPy verification

Verified over all 19 partitions with $|\lambda| \le 5$:

- Under $1 = \eta\varepsilon$: LHS is diagonal, eigenvalue on $\ell$ = 0, 1, 2 is
  $1, -(s+t), 2st$; zero for $\ell \ge 3$. ✓
- Under $1 = \operatorname{id}_\Lambda$: LHS is diagonal, eigenvalue on $\ell$
  is $2^\ell - \ell(s+t) + 2st\,\delta_{\ell,2}$. ✓

Scripts: `/tmp/verify_lhs.py` and `/tmp/verify_id_reading.py` (moved to
`proofs/scripts/day185/`).
