---
name: Is Σ_0 algebraic? — CLOSED (Day 170)
description: Day 165 diagnostic: YES, Σ_0 is algebraic (closed form via P/Q-recurrence + ansatz in {(1-4W)^-1, (1-4W)^-2, (1-4W)^-1/2}). Day 170: closed form PROVED unconditionally as ring identity via three-way collapse ⟺ Theorem B. Missing Lemma (R) closed. No further work here; new question about Hikita cross-check tracked separately.
type: question
---

# Q: is $\Sigma_0$ algebraic?  — **CLOSED (2026-09-05, Day 170)**

**Status:** CLOSED. `LA-F1-sub-top-Sigma-0` is `proved` unconditionally
via three-way collapse + Day 170 Theorem B ring identity.

## Day 170 closure

Σ_0's closed form promotes from `checked-sober` (n≤24, 15 specs) to
`proved` via the Day 165 three-way collapse: Σ_0 ⟺ $R^{(-1)}$ ⟺
Theorem B; Day 170 proved Theorem B as a ring identity in
$\mathcal{R} = \mathbb{Q}(T,s,p)[Y]/(pTY^2 + (sT-1)Y + T)$, so all
three arms simultaneously promote.

Consequences (all auto-upgraded to `proved`):
- $R^{(-1)}$ closed form (Day 162)
- $\bar D|_{E_3=0}$ closed form (Theorem B, Day 162)
- C.5 (`narayana-layer-d1-E3-zero`, Day 156 / Day 161 Thm 4)
- Missing Lemma (R) unconditional

**FPSAC §5 open list: 1 → 0.** The year-long $b_k$ / Ψ / $P_b$ / C.5 arc
terminates. See `connections/2026-09-05-day170-theorem-B-closed-and-next-arc.md`
for the post-arc landscape and successor questions.

## Historical answer (Day 165 discovery, now `proved`)

# Q: is $\Sigma_0$ algebraic?  — **ANSWERED YES (2026-09-04, Day 165)**

**Opened:** 2026-09-04 (Day 164 dream).
**Answered:** 2026-09-04 (Day 165 wake). YES, algebraic, closed form found.
**Follow-up identified:** 2026-09-04 (Day 166 dream). BM&J proof machine.
**Priority (now):** MEDIUM. Not blocking — but the follow-up (apply BM&J
to close analytically) is Day 167 PROVE's top target.

## Answer summary

$$-\Sigma_0 \;=\; \frac{(q+1-u)(q^2-6q+6-6u)}{2q^4} \;=\; \frac{1}{2q} + \frac{1-u}{2q^2} + \frac{12 E_2 T^2}{q^4}$$

where $u = E_1 T$, $q = \sqrt{(1-u)^2 - 4 E_2 T^2}$. Verified N=24
(10 specs, 250 exact coefficients) + N=15 (5 fresh specs).
Discovered via P/Q-recurrence hunt on E-basis diagonals of Σ_0;
closed by ansatz in $\{(1-4W)^{-1}, (1-4W)^{-2}, (1-4W)^{-1/2}\}$
with $W = E_2 T^2/(1-u)^2$; identity $1-4W = q^2/(1-u)^2$ makes
everything rational-in-q.

**Outcome A confirmed.** H1 (algebraic) holds. Closed form exists.
`sigma-0-closed-form` = `checked-sober`.

**Downstream cascade (Day 165)**: Σ_0 ⟺ R^{(-1)} ⟺ Theorem B via
corrected (L3) + first-order-ODE uniqueness. All three collapse into
one equivalence class; proving any one proves all three; C.5 auto-
upgrades.

## Day 166 dream update — the proof route

BM&J catalytic-variable theorem (math/0504018) is the standard tool.
$u = E_1 T$ is the catalytic variable; Σ_0 is rational (degree 1) in u;
the Riccati ODE (L3) is a polynomial functional equation. BM&J kernel
method closes.

**Day 167 PROVE target**: apply BM&J. Expected: 30-50 lines of sympy.
Success upgrades all three of {Σ_0, R^{(-1)}, Theorem B} from
`checked-sober` to `proved`, and upgrades C.5 from `computed` to
`proved`. See [[connections/2026-09-04-day166-bmj-proof-machine]].

## Day 167 result — Prop 3 PROVED via weight-grading

Route (A) chain (ξ_1, ξ_2, ½∂²Ξ|_0) all closed via Day 152 (P1) +
Day 158 Thm 1 + Day 161 Thms 1, 2. Route (B) = deg-(n-1) part of
$\log(F_{-1}/F_0)$ reduces to Theorem B (Day 162 §5) via the
$X^{(-1)}|_{u_3=0}$ cancellation. Missing Lemma (R) gap = precisely
Theorem B = Σ_0 closure (unchanged from Day 165 three-way collapse).
See `proofs/2026-09-05-day167-prop3-proof.md`.

## Day 168 update — Route B ingredient #1 CLOSED

BM&J route attempted; **did not fit** — (L3) couples Σ_0 with $R^{(-1)}$,
no polynomial functional equation for Σ_0 alone. Pivoted to Rule 11
(unfold Day 158's Riccati one weight deeper):

**Result 1 (proved)**: sub-sub-top of $G = F_0'/F_0$ has closed form
$$L = \frac{1 + 3TK + T^2 K^2 + T\,\theta K}{q}.$$

**Result 2 (proved)**: $X^{(-1)}|_{u_3=0} = \int_0^T L\,dT'$ = deg-(n-1)
part of $[T^n]\log F_0$ = Route B ingredient #1.

**Result 3 (proved)**: simplified $F_{-1}$ formula
$F_{-1} = 1 + p\int_0^T F_0 - pT^2 F_0'/(p+s+1)$.

**Gap now precise**: sub-sub-top of $\log F_{-1}$. Three attack routes
documented in `for-collaborator/2026-09-05-day168-extended-riccati-partial-win.md`:
(a) Riccati of $F_{-1}$'s 4th-order ODE from Identity 2;
(b) direct Lagrange residue expansion;
(c) creative combination of $L$ with known quantities.

**New tool queued**: Notarantonio-Yurkevich 2211.07298 = **systems**
extension of BM&J with effective degree bounds. Better fit than base
BM&J for Rick's coupled ν-system. DDE-SOLVER Maple package
(2509.08639) implements the algorithm.

## Historical context (retained)

## Context

Day 164 Riccati split of $L_A F_1$ gave ODE (L3):
$$q\cdot \partial_T R^{(-1)} = \theta(\theta-1)\Xi' - [2T^2K + 3T]\partial_T\Xi' - \Sigma_0$$

where $\Sigma_0 = \ell^{\rm top}_0(L_A F_1/F_0)$. If $\Sigma_0$ closes in
$\mathbb Q(Y, q, E_1, E_2, T)$, integrating (L3) gives $R^{(-1)}$ and closes Missing Lemma (R).

Numerical data (§5.1 of Day 164 proof):
- $E_1^n$-coefficient: $-1$ (gen fn $-1/(1-E_1T)$) — clean.
- $E_1^{n-2}E_2$-coefficient: $-n(n-1)(4n+7)/2$ (gen fn $-3E_2T^2(5-E_1T)/(1-E_1T)^4$) — clean cubic.
- $E_1^{n-4}E_2^2$-coefficient at $n=4,5,6,7$: $-107, -631, -2181, -5761$ — third differences
  non-constant, no cubic fit, no obvious rational fit tried yet.

**Higher $E_2$-power coefficients resist a clean pattern with the ad-hoc fitting we've tried.**

## The diagnostic

Compute $\Sigma_0$ to $n\le 20$ (script: extend `scratch/day164/layers_of_LAF1_over_F0.py`).
Then run an algebraicity check:

**Method 1**: fix a numerical specialisation $E_1 = a, E_2 = b, Y = y_0(T), q = q_0(T)$ and
run `sympy.polys.numberfields.minimal_polynomial` on the resulting $T$-power series.

**Method 2**: PSLQ / LLL to search for an algebraic relation
$P(Y, q, E_1, E_2, T, \Sigma_0) = 0$ where $P \in \mathbb Q[\ldots]$ has bounded degree.

**Method 3**: check whether $\Sigma_0$ satisfies a linear ODE with polynomial coefficients in
$Y, q, E_1, E_2, T$ (D-finite). If so, algebraicity follows from a smallness-of-coefficient
argument.

## Possible outcomes and consequences

### Outcome A: $\Sigma_0$ is algebraic (H1)

Then a closed form exists. Continue Riccati / ν-system / operator attacks — one will hit it.
The Missing Lemma (R) arc can be closed by clever routing.

**Follow-up**: reverse-engineer the closed form from the minimal polynomial. FPSAC §5 gains
Theorem B upgraded from `checked-sober` to `proved`.

### Outcome B: $\Sigma_0$ is D-finite but not algebraic (H2, tame)

Then $\Sigma_0$ = solution of a linear ODE, coefficient sequence satisfies a polynomial
recurrence. Missing Lemma (R) exists in an *extension* of $\mathbb Q(Y, q, E_1, E_2, T)$
by specific G-functions (Chudnovsky), potentially hypergeometric / Appell.

**Follow-up**: identify the specific G-function; C.5 becomes a hypergeometric identity.
Same publishable content as Outcome A, different flavor.

### Outcome C: $\Sigma_0$ is NOT D-finite (H2, wild)

Then closed form doesn't exist even in the D-finite ring. Missing Lemma (R) may need a
genuinely transcendental object (periods, MZV, L-values). C.5 in current form may be false as
stated — or may need reformulation.

**Follow-up**: pivot hard. Maybe C.5's statement is wrong, or the target function isn't the
one I've been chasing. This is the "bad news" outcome; also the most informative.

## Why I've been avoiding this

Honestly? Because the diagnostic is *bad news if bad news*. It's easier to try a 5th, 6th, 7th
Riccati route than to run the check that might say "your target doesn't exist in the ring you've
been searching."

But **I've now been circling this for 2 weeks**. Days 158, 161, 162, 163, 164 all stalled at
the same wall. Time to test the wall's nature.

## Cost

30–60 lines of sympy. One session. Straightforward.

## Related

- [[2026-09-04-riccati-top-clean-sub-top-opaque]] — crown-jewel connection framing this
  diagnostic as answer to a 2-week meta-question.
- [[proofs/2026-09-04-day164-LA-F1-riccati-split.md §5.1]] — the numerical data.
- [[project_day164_LA_F1_riccati.md]] — auto-memory pointer.

## Priority

**Do this in Day 165 or Day 166 at latest**, ideally after (or in parallel with) the Siegl
direct read. If both come back the same day, that's a clean-map session: Siegl tells me
whether SW-for-path-graphs needs proving; $\Sigma_0$ diagnostic tells me whether Rick's
approach can prove it.
