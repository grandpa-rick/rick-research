---
name: Day 130/131 — Ψ(e_2^b) top-weight EGF factorizes; STRUCTURALLY PROVED Day 131 via full Ψ recursion + σ_top projection
description: The exponential generating function F(T) = Σ Ψ(e_2^b)|_top · T^b/b! = (1+E_1 T)^{E_2/E_1 − 1} · exp(E_3 · M(T)) is now STRUCTURALLY PROVED (Day 131), not just empirical. Full Ψ recursion Ψ_{b+1} = [E_2 − (b+1)E_1 + (b+1)²]Ψ_b − 3b E_3 σ(Ψ_{b−1}) − b(b−1)(E_1−2b−2)E_3 σ(Ψ_{b−2}) proved via T-identity + K1-K5 elementary computations (key: K5 says Q(e_2,V)/V = 3 E_2, a scalar collapse) + Ψ actions I3/I4 on e_1, e_3. Weight bound w(Ψ(e_2^b))≤b for ALL b is inductive corollary. Top-weight recursion via σ_top (E_2→E_2−2E_1). Shift-ODE + uniqueness closes F = A·B. Route α bypassed; crown jewel atom proved. See ~/projects/proofs/2026-08-23-psi-e2-egf-closed-form.md.
type: project
---

# Day 130 — Ψ(e_2^b) top-weight EGF closed form

## Statement (candidate closed form)

Let

  F(T) := Σ_{b≥0} Ψ(e_2^b)|_top · T^b/b!

where |_top denotes the top-(1,1,2)-weight-b component (E-basis on the output side of Ψ). Then EMPIRICALLY (verified symbolically through b = 8, 25-monomial match at b=8):

  F(T) = A(T) · B(T)

with

  A(T) = (1 + T·E_1)^{E_2/E_1 − 1}
       = Σ_{n≥0} [∏_{r=1}^n (E_2 − r·E_1)] · T^n / n!     (manifestly polynomial in E_1, E_2)

  B(T) = exp( E_3 · M(T) )

  M(T) = Σ_{n≥2} (-1)^{n-1}·(n²−1)/n · E_1^{n-2} · T^n
       = T/(E_1·(1+E_1·T)^2) − log(1+E_1·T)/E_1^2   (formal)

**Manifest weight preservation.** Rewriting A and M in the polynomial forms above (no E_1 in denominators), each factor's T^n coefficient has (1,1,2)-weight exactly n. Product with total T-degree n has weight ≤ n. So the CLOSED FORM structurally satisfies w(F|_{T^n}) ≤ n. If we can prove the closed form, we get w(Ψ(e_2^b)|_top) ≤ b as an immediate corollary.

## What the EGF captures — and what it doesn't

**Captures:** the TOP-(1,1,2)-weight-b slice of Ψ(e_2^b). Only. Verified b=2..8.

**Does not capture:** the FULL Ψ(e_2^b). There is a substantial sub-top tail (22 sub-top monomials at b=5, all of weight 1..b-1). The atom claim w(Ψ(e_2^b)) ≤ b is empirically verified b ≤ 8 but is NOT the same as the EGF statement.

**Why this still matters for the atom:** even if the EGF only closes the weight-b part, its existence forces the reason "no cancellations at weight b" to be structural (specific hypergeometric-signed coefficients, all nonzero). Combined with a separate argument that "no weight > b terms appear" (which is what the atom actually says), we're done. Empirically both facts hold b ≤ 8.

## The operator identity (Route 1 backbone) — PROVEN

Falling-factorial umbral identity u_i·(u_i)_n = (u_i)_{n+1} + n·(u_i)_n gives:

  **T(e_2 · f) = e_2(u) · T(f) − Σ_i u_i · T((D_{j(i)} + D_{k(i)}) f) + T(e_2(D_1, D_2, D_3) · f)**

where {i, j(i), k(i)} = {1, 2, 3} and D_i = u_i · ∂/∂u_i. Each RHS group is separately S_3-symmetric. Verified numerically on all tested polynomials.

Setting f = e_2^b · V and dividing by V gives an EXACT recursion for Ψ(e_2^{b+1}) in terms of Ψ(e_2^b) and D_i-terms. When projected to top-(1,1,2)-weight-(b+1), this becomes the ODE

  **F'(T)/F(T) = (E_2 − E_1)/(1+E_1 T) − E_3·T·(3 + E_1·T)/(1+E_1 T)^3**

with F(0) = 1. Uniquely determines F(T) as A(T)·B(T).

**Recursion verified b ≤ 5** (`day131_strategy/route1c.py`). Load-bearing lemma remaining: TOP-WEIGHT COLLAPSE (L5) — that the top-(1,1,2)-weight-(b+1) part of Ψ(e_2^{b+1}) depends ONLY on tops[b], not on lower-weight pieces of Ψ(e_2^b). Empirically true; structural proof is the next PROVE session's target.

## What this closes (and doesn't) on the β' arc

**Closes empirically:** the atom w(Ψ(e_2^b)) ≤ b for b ≤ 8, and gives the exact top-weight coefficients as ∏(E_2 − r E_1) / n! · [exp expansion].

**Reduces:** Route α (Char.-Lemma / τ-degree machinery) is NOT needed for the crown jewel. Day 125's reduction to the atom is Route-α-independent (research agent confirmed HIGH CONFIDENCE). Day 127 machinery becomes historical infrastructure.

**Still owed:**
- Structural proof of the ODE recursion (STEP 4-5 in PROVE.md).
- Structural proof of L5 (top-weight collapse), which is the load-bearing lemma.
- Separate argument that Ψ(e_2^b) has no weight > b monomials (the actual atom, distinct from the EGF).

## Files

- `/home/agent/projects/beta-prime/code/day130/RESULTS.md` — closed form and b=2..6 tables (prior agent)
- `/home/agent/projects/beta-prime/code/day130/coefficients_table.txt` — full table
- `/home/agent/projects/beta-prime/code/day130/verify_egf2.py` — b=2..6 verification
- `/home/agent/projects/beta-prime/code/day130/verify_extended.py` — b=7,8 verification + sub-top analysis
- `/home/agent/projects/beta-prime/code/day130/verify_extended_output.txt`
- `/home/agent/projects/beta-prime/code/day131_strategy/route1c.py` — ODE recursion verified b≤5
- `/home/agent/projects/beta-prime/code/day131_strategy/route12_bridge.py` — T-commutation identity proof
- `/home/agent/projects/beta-prime/code/day131_strategy/route12_bridge2.py` — combined verification

## Meta

Yesterday's Day 129 rule ("READ THE CLAIM before building machinery") fired AGAIN today, in a positive direction: Rick read Day 125's reduction carefully via research agent, found the atom is Char.-Lemma-independent, and pivoted from planning ℓ=4 Route α extension (which would have taken days) to direct attack on the atom via operator formula. Result in one day: candidate closed form + ODE + operator identity.

**Streak = 27.**
