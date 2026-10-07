---
name: "[CLOSED Day 151 — FAIL] Question — is Conjecture P a Kerov-type positivity, and is M=1-2F a transition measure?"
description: Day 150 dream. Kerov character polynomials express normalized S_n characters (elements of the shifted symmetric algebra Lambda*) in the free cumulants R_j of the transition measure, and Feray proved their coefficients are non-negative integers. Rick has both objects. Three sharp tests, in order of cost.
type: project
---

> **CLOSED 2026-08-31 (Day 151), verdict FAIL.** T1 fails, T2 fails, T3 not worth
> running. Scroll to the bottom for the verdict block. Do **not** re-open this on the
> strength of the name match.

# Q: Kerov polynomials as the template for Conjecture P

**Status:** ~~OPEN, new (Day 150 dream)~~ → **RESOLVED / CLOSED, Day 151, FAIL.** Full argument in
[[2026-08-30-day150-two-arcs-one-lattice]].

## The three tests, cheapest first

**T1 (frame, ~30 min).** Rick's ring is the **3-variable** factorial Schur ring
$\Lambda_3=\mathbb Z[E_1,E_2,E_3]$, $\mathfrak s_\mu=s_\mu(u|a)$ at $a_l=1-l$. Kerov's $R_j$ live
in the **stable** $\Lambda^*$ (Okounkov–Olshanski inverse limit). Does the 3-variable
specialisation receive $R_2,R_3,R_4$ nontrivially, or does truncation destroy the structure?
**If it destroys it, the whole bridge is decorative and this question closes.**

**T2 (compute, ~1 session).** Assuming T1 passes: expand $P_b=\sum_\mu K_{\mu'(2^b)}\mathfrak s_\mu$
for $b\le6$ in $R_2,R_3,R_4,\dots$. **Are the coefficients non-negative?**
* YES ⟹ Conjecture P's $E$-positivity is plausibly the shadow of a Kerov-type positivity, and
  Féray's counting model (maps/factorisations) is the technique to transplant.
* NO ⟹ the two positivities are unrelated; close this leg and go back to the layer induction
  ([[2026-08-30-day150-conjectureP-layer-induction]]), which does not depend on it.

**T3 (the deep one).** Is $M=1-2F$ the Cauchy transform (equivalently: are $\kappa_n(M)$ the
$R$-transform coefficients) of the **transition measure of some Young diagram**, possibly a
continuous one in Kerov's sense? If yes, $\kappa_n(M)\in6\mathbb Z$ / $b_k\equiv0\bmod3$ becomes a
statement about that diagram, at **every** prime, and Arc A and Arc B are literally the same object.
The Day 148 quintic $F(1-F)^3(3-4F)=\vartheta(3-2F)^2$ gives $M$ algebraically — so the diagram, if
it exists, has an algebraic transition measure. Kerov's continuous diagrams with algebraic
transition measures are a classified-ish family; check there.

## Discipline

Rule 6 v2 (object hygiene between frames) has fired **nine** times, most recently on a
theorem-level name collision. "Free cumulants" here and "free cumulants" there are **not** the same
object until a numerical identity says so. T3 is the identity that would say so. Do not write
"Kerov" in the FPSAC draft until T1 and T2 pass.

---

## VERDICT — Day 151, 2026-08-31. **CLOSED. FAIL.** The bridge is dead.

Evidence: [[2026-08-31-day151-kerov-T1]] (`~/projects/scratch/2026-08-31-day151-kerov-T1.md`),
code in `~/projects/scratch/day151_kerov/`. Grade: `computed`, exact rational arithmetic.
Not circular: T1/T2 test a specialisation map and the positivity of Kerov's $\Sigma_k$, which is
**Féray's theorem** — an external truth, not Conjecture P.

**Short version: Kerov positivity does not survive Rick's 3-variable truncation.** You wrote the
kill criterion yourself ("if it destroys it, the whole bridge is decorative and this question
closes"). It destroys it. Question closed.

### T1 — FAIL

$\Lambda_3\otimes\mathbb Q=\mathbb Q[R_2,R_3,R_4]$ (Jacobian $-6$, so they *are* coordinates over
$\mathbb Q$) — but that is all that survives:
* integrality dies at $R_3$ (Jacobian $-6\ne\pm1$, so $\mathbb Z[R_2,R_3,R_4]\subsetneq\Lambda_3$);
* **free generation dies at $R_5$** — in 3 variables $R_5,\dots,R_8$ are dependent, so "the
  expansion in the $R$'s", *unique* in $\Lambda^*$, is **ill-posed** in $\Lambda_3$;
* rewriting the $\Sigma_k$ — the very objects Féray proved positive — in $R_2,R_3,R_4$ gives
  **mixed signs and denominators** from $k=4$ on:

  | $k$ | 4 | 5 | 6 | 7 |
  |---|---|---|---|---|
  | negative coeffs / terms | **5/10** | **6/14** | **10/22** | **12/26** |
  | integral? | no ($/6$) | no | no | no ($/36$) |

  ($\Sigma_1,\Sigma_2,\Sigma_3$ survive only because they use nothing above $R_4$.)

### T2 — FAIL (in the *repaired*, well-posed form)

T2 as originally written is ill-posed by T1(d), so it was run in the fair place: lift to
$\Lambda^*$, where the $R$-expansion is unique and where Féray positivity actually lives.
Both lifts (full $\Psi^+(e_2^b)$, and the $\ell(\mu)\le3$-only minimal lift) restrict to Rick's
$P_b$. Negative coefficients, full lift:

| $b$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| negative / terms | **2/3** | **5/9** | **11/20** | **20/39** |
| integral? | no | no | no | no |

(minimal lift: 2/3, 5/11, 6/13, 28/56 — same story.) It fails at the smallest case **in closed
form**:
$$P_1=\mathfrak s^*_{(1,1)}=\tfrac12\bigl(R_2^2-R_2-R_3\bigr).$$
Roughly half the coefficients are negative and **none** of the expansions is integral.

### Why the negative is trustworthy

**The pipeline was validated FIRST.** Before touching $P_b$, `T2stable.py` reproduced Biane's
$\Sigma_1,\dots,\Sigma_7$ — **all coefficients non-negative integers**, including
$\Sigma_7=R_8+70R_6+84R_2R_4+56R_3^2+14R_2^3+469R_4+224R_2^2+180R_2$ (a recalled value was *wrong*
and the exact fit corrected it). So the machinery **does** detect Kerov positivity when it is
there. It then reports negatives for $P_b$. That ordering is what makes this a real negative and
not a bug. (Same for the frame: `frscheck.py`/`framecheck.py`/`kostkacheck.py` verified
$\mathfrak s_\mu(u)|_{u=-a(\lambda)}=(-1)^{|\mu|}s^*_\mu(\lambda)$ and Corollary B in the
$\lambda$-frame before anything was concluded — and caught a Kostka-generator bug in the process.)

### The ONE keeper

T1(a) is a genuine structural fact, obtained without importing anything, and it belongs in the
object dictionary:

> Under $u_i=-(\lambda_i+3-i)$ the **Kerov filtration and Rick's $u$-degree filtration
> COINCIDE**: $\deg_uR_j=j-1$ exactly, $\mathrm{lead}(R_j)=(-1)^{j-1}p_{j-1}(u)$ (verified
> $j=2..8$), and the Jacobian $\partial(R_2,R_3,R_4)/\partial(E_1,E_2,E_3)=-6$, a nonzero
> constant.

I.e. the $E_3=0$ / Narayana top layer sits at Kerov's top layer too. That is a statement about
**Rick's own $u$-grading** — the grading the Day 150 layer-induction attack runs on. The
layer-induction route never depended on Kerov and is **untouched**.

### Discipline

**Rule 6 v2 firing #11.** Free cumulants here $\ne$ free cumulants there — again. The sharper
lesson this time: the *name* matched, the *ring* matched (both are shifted-symmetric), and the
structure **still** did not transfer. Import scorecard now ~9 attempts, 0 theorems.

**"Kerov" must NOT appear in the FPSAC draft** — per your own pre-registration in this file
("do not write 'Kerov' in the FPSAC draft until T1 and T2 pass"). They did not pass.

T3 (is $M=1-2F$ the transition measure of a Young diagram?) is **not** worth running on this
account: $P_b$ is not $R$-positive even where $R$-positivity is a *theorem* for the characters, so
there is nothing left for T3 to buy. If you ever want it, it must be re-motivated from scratch.
