# 2026-09-04 (Day 165) — Σ_0 ⟺ R^{(-1)} ⟺ Theorem B, unified via corrected (L3)

## Crown-jewel status

**PARTIAL CROWN JEWEL.** Day 164's stall on Missing Lemma (R) was
"$\Sigma_0$ = ? no closed form found." Day 165's diagnostic answered:
$\Sigma_0$ IS algebraic, with explicit closed form
$-\Sigma_0 = (q+1-u)(q^2-6q+6-6u)/(2q^4)$ (`checked-sober` N=24, 15 specs).

The downstream cascade: given this closed form, Day 162's R^{(-1)} closed
form is analytically forced by first-order-ODE uniqueness applied to the
corrected (L3). Symbolic sympy identity proves LHS = RHS. So R^{(-1)}
closed form and Σ_0 closed form are pairwise equivalent — and since
R^{(-1)} closed form was already known equivalent to Theorem B (via
Day 161 Thm 3), all three collapse into ONE equivalence class.

## What this means

Before Day 165: three separate `checked-sober`/`computed` conjectures in the
FPSAC §5 story (Σ_0 unknown source term, R^{(-1)} closed form, Theorem B).
Attacked independently.

After Day 165: **one equivalence class**. Proving ANY ONE proves ALL THREE.
Missing Lemma (R) is now a single named conjecture.

The strategic upshot: Rick's Day 166+ target is unambiguous. Prove the
cleanest of the three (probably Σ_0 via its P/Q-recurrence structure, or
R^{(-1)} via a direct nu-system computation, or Theorem B via its Lagrange
form). Any single successful proof upgrades all three from `checked-sober`
to `proved`, upgrading C.5 from `computed` to `proved`, and gives FPSAC §5
its third theorem.

## The Riccati-top-clean/sub-top-opaque pattern updated

Day 164 dream's crown-jewel meta-observation was: across 5 Riccati splits,
top layer is always algebraic in $Y, q$; sub-top is sometimes closable
(via linear system / Cramer), sometimes opaque ($R^{(-1)}$, $\Sigma_0$).

**Day 165 update**: the opaque sub-top *does* live in the algebraic ring —
just via a *different* algebraic mechanism than the linear-system route.
$\Sigma_0$ has a P/Q-recurrence structure (D-finite, satisfies a linear
ODE with polynomial coefficients whose solutions live in a specific
algebraic function field). The P/Q-recurrence hunt worked where the
linear-system hunt failed.

So the "sub-top opaque" pattern is not literally opaque — it just requires
a *different diagnostic* (P-recurrence hunt, not Cramer). This is a
methodological insight worth banking.

## The sign flip in Day 164 §5

Day 164 §5 boxed (L3) had a sign error on the middle term. The unboxed
derivation on the immediately preceding line is correct; only the box
transcription flipped the sign. Caught by two Day-165 compute agents
via numerical FP_coeffs check. Day 164 proof file annotated with the
correction (2026-09-04).

**Meta-lesson (feedback-rule candidate)**: transcribed-formula sign errors
happen when the derivation and the boxed final answer are separated in the
prose. When boxing a final formula that came from a multi-step derivation,
run a 3-line numerical sanity check as part of the boxing action.

## The FPSAC framing shift (from Siegl direct read, same session)

Independently, the Siegl 2509.02841 direct read (this session) settled a
long-standing framing question: **path-graph SW q-positivity was already
proved by Shareshian-Wachs themselves in 2016**. Siegl's Thm 1.10 just
repackages SW's own proof combinatorially. Rick's FPSAC novelty anchor
must shift from "the only path-graph SW attack" to "the ν-system
machinery, layer decomposition, closed forms, and algebraic-ring proof
technique — none of which are visible from SW/Siegl's combinatorial
approach."

Rick's Day 165 wins — a closed form for the sub-top layer of $L_A F_1/F_0$
(Σ_0), and the three-way equivalence — are exactly the kind of
"additional structure not visible from the combinatorial approach" that
justifies the FPSAC contribution.

## Registry state (post-Day 165)

**Proved (all new Day 165):**
- `LA-F1-Riccati-ODE-L3` (corrected sign)
- `R-minus-one-satisfies-L3` (symbolic sympy identity)
- `sigma0-Rminus1-algebraic-equivalence` (both directions via (L3))

**Checked-sober (all Day 165 with new context):**
- `LA-F1-sub-top-Sigma-0` — closed form found (N=24, 15 specs)
- `R-minus-one-closed-form` — Day 162 formula, now analytically forced from Σ_0
- `bar-D-closed-form-E3-zero` (Theorem B) — unchanged trust, now equivalent to Σ_0

**Still open:**
- Analytic proof of ANY ONE of Σ_0, R^{(-1)}, Theorem B closed form
  (equivalent target; any single proof closes all three)
- C.5 (`computed`) auto-upgrades to `proved` once any one closes

## OEIS hit — A032443

The $Q_k$ coefficient sequence
$$Q_k \;=\; 1, 3, 11, 42, 163, 638, 2510, 9908, 39203, 155382, 616666, 2449868, \ldots$$
matches **OEIS A032443**: $Q_k = \sum_{i=0}^{k}\binom{2k}{i} = \frac{4^k + \binom{2k}{k}}{2}$ (half-sum of Pascal's row 2k). Consistent with the closed form
$A_Q(W) = \frac{1}{2(1-4W)} + \frac{1}{2\sqrt{1-4W}}$ since
$\frac{1}{1-4W} = \sum_k 4^k W^k$ and $\frac{1}{\sqrt{1-4W}} = \sum_k \binom{2k}{k} W^k$.

**Interpretation-hunt hint for Day 166+.** A032443 has combinatorial
interpretations (lattice paths from (0,0) to (2n,0) with steps N/S/E,
or "no gain / no loss" in a random walk of length 2n biased at half).
If a natural bijection makes $Q_k$ count something in Rick's setting
(NC partitions? chromatic invariants of $P_n$?), it may lead to a direct
combinatorial proof of $\Sigma_0$'s closed form. Worth exploring.

## Files

- `proofs/2026-09-04-day165-sigma-0-closed-form.md` (this session's proof file)
- `proofs/2026-09-04-day164-LA-F1-riccati-split.md` (Day 164 file, sign-corrected)
- `scratch/day165/REPORT.md` (diagnostic)
- `scratch/day165/close-Rminus1/REPORT.md` (R^{(-1)} closure)
- `scratch/day165/sigma0-proof/REPORT.md` (Σ_0 symbolic proof attempt)
