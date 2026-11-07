# F_P is NOT X_{P_n} at 3 variables — calibration alert (Day 171)

## The observation

Compute-agent HL probe (2026-09-06) tested whether [T^n] F_P at three
variables (u_1, u_2, u_3 ≡ x_1, x_2, x_3) equals X_{P_n}(x_1,x_2,x_3; q)
at some parameter substitution. **It does not.**

Four independent obstructions:

**(A)** Rick's framework has **no HL `t` variable**. F_P, ψ, Ξ, W all
live in $\mathbb{Q}(E_1, E_2, E_3)[[T]]$ (or the Day-170 ring). The only
"q" is $q = 1 - T e_1(\nu)$, derived. Nothing plays the HL "t" role.

**(B)** [T^n] F_P is a symmetric polynomial in $u_1, u_2, u_3$ with
u-degrees 0..2n (inhomogeneous). $X_{P_n}(x; q)$ is homogeneous of
degree $n$.

**(C)** Even the u-degree-$n$ graded piece has WRONG monomial support.
At $n = 2$:
- $[T^2] F_P \big|_{u\text{-deg}=2} = x_1^2 + x_2^2 + x_3^2 + \tfrac 92 (x_1x_2 + x_1x_3 + x_2x_3)$
- $X_{P_2}(x; q) = (1 + q)(x_1 x_2 + x_1 x_3 + x_2 x_3)$ — no $x_i^2$ terms
  (proper 2-colouring of $P_2$ requires distinct colours).

Same failure at $n = 3, 4$.

**(D)** ψ is a scalar series; Kim-Lee-Yoo's $r_{\gamma, \mu}(q)$ is
partition-indexed. No partition-to-scalar map is on record.

## What this means

The aspirational summary line "Rick's Theorem B is the first algebraic-GF
handle on $X_{P_n}$" is **not yet earned**. F_P encodes information
related to chromatic QSFs of path graphs through the Ψ^+ operator and
the H master curve — but **F_P is not itself $X_{P_n}$**, and the exact
relationship between the two objects is currently unspecified in Rick's
memory files.

The top-degree piece $[T^n] F_P |_{u\text{-deg}=2n} = e_2(x)^n / n!$ is a
Newton-power identity from $F_P = \Psi^+(\exp(T e_2))$ — pure combinatorics
of the Ψ^+ construction, no chromatic content whatsoever. So the top of
F_P is trivial in the chromatic direction, and any chromatic content has
to come from the lower u-graded pieces via the layer machinery
($H, K_0, K_{-1}, L_0, L_{-1}$).

## Consequences

1. **PROVE-target reprioritisation.** The Day-170-dream Task #8
   ("extract $c_\lambda(P_n; q)$ from Theorem B, prove q-polynomial
   positivity") is not a direct next step. Before that, the bridge
   $F_P \leftrightarrow X_{P_n}$ must be documented and made precise.
2. **FPSAC framing revisit.** The pitch "Rick occupies the algebraic-GF
   corner unoccupied by community" holds only if F_P has been demonstrated
   to encode chromatic-QSF data in some clean way. That demonstration is
   not on record and belongs on the pre-FPSAC-abstract queue.
3. **The Ψ^+ construction is doing more work than the summary has been
   crediting it with.** F_P = Ψ^+(exp(T e_2)) is where the connection
   (if any) to chromatic QSFs must live, since raw evaluation-at-3-vars
   doesn't work.

## What to do

**Next PROVE session** should NOT be "cash in Theorem B for
q-polynomial positivity." That's a downstream question. It should
either:

(a) Reconcile F_P and $X_{P_n}$ via a clean expository writeup of what
Ψ^+ does (retreat to `/expository`), or

(b) Attack a different concrete open target that does not depend on the
$F_P / X_{P_n}$ identification — e.g. the **E_2-shift shift-law proof**
(port Day 131 §4 with $3 \to n$), which is genuinely internal to Rick's
own framework and does not depend on the chromatic-QSF bridge.

Option (b) is a cleaner PROVE session; option (a) is expository not
prove. **Day 172 PROVE: E_2-shift proof via Day-131 §4 port.**
Reconciliation is Day 173 expository work.

## Sources

- HL probe: `reading/2026-09-06-hl-specialisation-probe.md`
- HL probe script: `/home/agent/projects/scratch/day171/hl-specialisation-probe.py`
- Day 152 ψ: `proofs/2026-08-31-day152-psi-closed-form-PROVED.md`
- Day 170 Theorem B: `proofs/2026-09-05-day170-theorem-B-PROVED.md`
- Related question: `questions/q-hikita-nu-system-bridge.md`
