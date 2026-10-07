# Q: Can the ν-system be q-deformed to attack Shareshian-Wachs at $E_3 = 0$?

**Opened:** 2026-09-03 (Browse 124 + Day 161 PROVE synthesis).
**Priority:** HIGH — the natural next major arc after Day 170 Theorem B.

## 2026-09-05 Day 170 update — PROMOTED to primary post-arc target

Theorem B is proved (three-way collapse arms all `proved`). The
FPSAC §5 open list is empty. **This question is now the natural next
research arc.**

**Refined statement**: nobody has an approach to q-polynomial
positivity of e-coefficients $c_\lambda(P_n; q)$ at the algebraic
GF level. Rick's Theorem B gives the first handle — extract
e-coefficients from the closed form and check if they lie in
$\mathbb{Z}_{\ge 0}[q]$.

**Two independent probes** (Day 172+):
1. **10-line sympy**: does Rick's ψ at $t = 0$ reproduce Kim-Lee-Yoo
   2506.23082's Hall-Littlewood expansion for path graphs? If yes,
   subsumes their result as a corollary.
2. **20-line sympy**: Hikita q-independence check (Thm B.iv of
   2503.23597) — do Rick's e-coefficients agree with Hikita's
   for $P_n$, $n \le 5$?

**Post-arc medium-term**: Extract $c_\lambda(P_n; q)$ from Theorem B
in the E-basis and prove positivity. If successful: **first
q-polynomial positivity result** for path graphs (SW's refined
conjecture, open for a decade).

See also: `connections/2026-09-05-day170-theorem-B-closed-and-next-arc.md`.

---

## Original context (pre-Day-170)

**Day 166 dream update (novelty FULLY CLEARED):**

Three independent Day-165/Day-166 findings converged:
1. **Path-graph SW q-positivity was closed by SW in 2016** (Day 165 Siegl
   direct read). Siegl 2509.02841 Thm 1.10 repackages SW's own 2016
   proof. The specific path-graph case is NOT open.
2. **Guay-Paquet 2507.05614 (deep read Browse 127)**: works in
   equivariant cohomology H_T*(X(h)) with Tymoczko dot action; categorifies
   the Abreu-Nigro modular law via divided differences.
   **ZERO OVERLAP** with Rick's generating-function / Riccati / ν-system
   machinery. No novelty risk.
3. **SW q-positivity in general STILL OPEN** — confirmed by three sources
   as of September 2026: Hikita FPSAC 2025 slides, arXiv:2210.03803
   updated May 2025, Mathematical Gemstones exposition.

**Consequence**: this question retargets from "attack path-graph SW"
(already solved 2016) to "attack SW in general using path-graph
ν-system machinery as a template." Rick's ν-system + Riccati layer
decomposition + BM&J-style closed forms is genuinely novel machinery
for the still-open general problem.

**FPSAC framing shift**: the path-graph SW result is NOT Rick's
contribution — the *machinery* is. FPSAC pitch: "we can compute
sub-top layers of L_A F_1 in closed form via a systematic proof
machine (BM&J + Riccati split), demonstrated at $E_3 = 0$ (path
graphs), extending to the general Hessenberg case via [...]" —
where [...] is the post-FPSAC arc.

- **Hikita's $q$ is NOT SW's $q$**: Hikita's $q$ deforms basis, not
  coefficients (e-coefficients are $q$-independent). So Bridge 2 (Hikita
  quantum Pieri → path-graph recursion) needs to track SW's $q$ =
  inversion statistic separately. Bridge remains untested but interesting.

## Context

Browse 124 nailed down the status map of the chromatic-symmetric-function literature:

- **Stanley-Stembridge:** PROVED (Hikita 2410.12758, Oct 2024).
- **Stanley-Gasharov:** DISPROVED (Matherne-Morales 2607.21508, Jul 2026).
- **Shareshian-Wachs q-positivity:** OPEN — **the main surviving problem**. The claim is that
  the e-expansion coefficients of the chromatic quasisymmetric function of a unit interval graph
  lie in $\mathbb Z_{\ge 0}[q]$, not just be nonneg at $q=1$.

Hikita's probabilistic method gives positivity at $q=1$ (rational functions whose denominators
cancel in the sum) but no manifestly polynomial-in-$q$ formula.

## The idea

At $E_3 = 0$, the path graph is the natural chromatic-community stratum, and Rick has:
- Day 154 Narayana closed form (proved).
- Day 158 $X^{(0)}$ closed form (proved).
- Day 156 layer-$d=1$ closed form $6T/q^4$ (computed n≤16, near-proved via Day 161 reduction).
- Day 161 transverse derivatives (proved).

All via the Day 152 **ν-system**: $T\nu_i^2 + q\nu_i = u_i$, $q = 1 - Te_1(\nu)$.

**Question:** Can this ν-system be q-deformed (in the Shareshian-Wachs / Hall-Littlewood /
Macdonald sense, not Rick's $q^2 = (1-E_1T)^2 - 4E_2T^2$ sense!) to produce path-graph
Shareshian-Wachs coefficients in $\mathbb Z_{\ge 0}[q_{\rm SW}]$?

## Candidates for the q-deformation

Ranked after Browse 125 (2026-09-03):

1. **Hikita's affine Hecke construction** (arXiv:2503.23597). ★★★ TOP CANDIDATE. Level-1 affine
   Hecke type A gives $(q,t)$-chromatic $X_\Gamma(q,t)$ with quantum Pieri rule
   $e_1 \star e_r = (1-q^{-1})[r+1]_t e_{r+1} + q^{-1} e_1 e_r$. Applied to path graphs $P_n$,
   the generating function $\sum_n X_{P_n}(q,t) y^n$ might satisfy an algebraic equation over
   $\mathbb Q(q,t)$ — that IS the q-deformed ν-system. Nobody has computed this. Next wake:
   read in full + apply Pieri to $P_n$.
2. **Griffin-Mellit A_{q,t} expansion** (arXiv:2504.06936). ★★ Uses A_{q,t} Dyck path algebra;
   at $t=0$ gives Hall-Littlewood expansion (= GDL-W bridge). No explicit path-graph
   formula in the paper; would need to compute from raising/lowering ops $d_+, d_-$.
3. **Thibon triple composition** (arXiv:2608.30791). ✗ DROPPED after Browse 125 deep read.
   No path graphs / Riccati / SW. Validates Day 149 Ψ=F at $(q,t)$ level but does not
   bridge to ν-system.

## Load-bearing test

If the ν-system deforms, the first test is: does the deformed Narayana series produce Shareshian-Wachs
coefficients at $E_3=0$? These are computable from Hikita's formula at $q_{\rm SW}=1$ but Rick would
need to check polynomial-in-$q_{\rm SW}$ structure.

## Why medium priority

- Not blocking FPSAC 2027 (the paper is on b_k/Ψ/ψ arc, not on chromatic-community open problems).
- Would open a post-FPSAC research arc that unifies Rick's ν-system with the Macdonald/A_{q,t}
  machinery — potentially big.
- Requires reading Griffin-Mellit and Thibon in depth first. Both are on the browse queue.

## Followup

- **Priority 1**: Read Hikita 2503.23597 in full. Apply quantum Pieri rule
  $e_1 \star e_r = (1-q^{-1})[r+1]_t e_{r+1} + q^{-1} e_1 e_r$ to path graphs. If
  $\sum_n X_{P_n}(q,t) y^n$ satisfies an algebraic equation, that IS the q-deformed ν-system.
- **Priority 2**: 20-line sympy — GDL-W Bridge 1: does Rick's Y at some specialization satisfy
  $F(1+F)(1+qF) = T$? Likely no at trivial corner, but the near-miss will be informative.
- Read Griffin-Mellit 2504.06936 (deep). Compute path-graph C_{e,μ}(q,t) at $t=0$.
- If Hikita bridge fires: draft note comparing ν-system with quantum Pieri, check path-graph
  Shareshian-Wachs coefficients against Rick's closed forms at $E_3=0$.
- Thibon 2608.30791 — DROPPED after Browse 125.
