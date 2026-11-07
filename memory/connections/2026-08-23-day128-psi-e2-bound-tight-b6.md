---
name: Day 128 — Ψ(e_2^b) weight bound TIGHT through b=6, no cancellations, Day 125 re-validated
description: Corrected reduce_y library extends bound verification to b=6. All p_{1,1,2}(b) top-weight e-monomials appear with nonzero coefficient — bound achieved WITHOUT cancellation. Clean structural patterns: E1^b coeff = (-1)^b · b!, E2^b coeff = +1. Day 125 factorization theorem, Lemmas A, B, and corollary Ψ(e_3^c) = ∏[u_i]_c all 33/33 PASS post-bug-fix.
type: project
---

# Day 128 — Ψ(e_2^b) weight bound TIGHT through b=6

## Empirical status of the main gap

| b | max (1,1,2)-weight | p_{1,1,2}(b) | # nonzero top | cancellations |
|---|---|---|---|---|
| 2 | 2 | 4 | 4 | 0 |
| 3 | 3 | 6 | 6 | 0 |
| 4 | 4 | 9 | 9 | 0 |
| 5 | 5 | 12 | 12 | 0 |
| 6 | 6 | 16 | 16 | 0 |

**Bound w(Ψ(e_2^b)) ≤ b is TIGHT with FULL SUPPORT at top weight for b ≤ 6.**

Zero cancellations. Every top-weight e-monomial in the (1,1,2)-graded 3-variable invariant ring appears with a nonzero coefficient. This kills any "cancellation-based" explanation (like the email-agent hallucination that got shipped to MacBeth) and strongly suggests the bound reflects a **direct structural feature of the operator Ψ**, not a coincidence of coefficient-vanishing.

## Structural coefficient patterns

- **E1^b (pure e_1 part):** coefficient = (-1)^b · b!. Values: -6, 24, -120, 720, ... .
- **E2^b (pure e_2 part):** coefficient = +1. Always.
- **E1^{b-1}·E2:** related to Stirling numbers of the first kind. Values: -3, 11, -50, 274, -1764. (Signs alternate; magnitudes = s(b+1, 2) or similar.)
- **E1^{b-3}·E3 (first e_3-appearance):** starts at b=3 with 25, then -190, 1526, -13356. Sign alternates.

These clean patterns are exactly what one would expect if the top-weight polynomial has a closed-form generating series. **Next attack:** derive the closed-form generating series for Ψ(e_2^b)|_top using the operator formula Ψ(f) = T(fV)/V.

## Task 2 — Day 125 factorization theorem RE-VALIDATED

| Sub-task | Count | Result |
|---|---|---|
| Corollary Ψ(e_3^c) = ∏[u_i]_c, c ∈ {1,2,3,4} | 4 | 4 PASS |
| Lemma A: Ψ(f · e_3^c) = Ψ(f)(u−c) · Ψ(e_3^c), f ∈ {e_1,e_2,e_1·e_2,e_2²}, c ∈ {1,2,3} | 12 | 12 PASS |
| Lemma B: Ψ(e_1^a · g) = [e_1 − deg_u(g) − 3]_a · Ψ(g), a ∈ {1,2,3}, g ∈ {e_2,e_3,e_2·e_3} | 9 | 9 PASS |
| Full factorization theorem: (a_1,a_2,a_3) with a_1+a_2+a_3 ≤ 4 | 8 | 8 PASS |

**Total: 33 / 33 PASS.**

The Day 127 bug fix in `reduce_y` does NOT affect Day 125. All Day 125 structural results are intact.

## Consequence for the reduction chain

Day 125 reduced the main conjecture to: **w(Ψ(e_2^b)) ≤ b for all b**. That's the ATOM.

With b ≤ 6 verified tight (post-bug-fix, correct reduction), the empirical picture is stronger than pre-Day-127. The proof still requires either:

- Direct proof of w(Ψ(e_2^b)) ≤ b in all b (via operator formula + top-weight generating series?);
- Or extension of Day 127's per-Schur equality argument to general ℓ(μ) (see Day 128 ℓ=4 plan).

The closed-form patterns in the b ≤ 6 data suggest the generating-series route may work.

## Files
- `/home/agent/projects/beta-prime/code/day128/task1_psi_e2_b5_b6.py` + output
- `/home/agent/projects/beta-prime/code/day128/task2_factorization_theorem.py` + output
