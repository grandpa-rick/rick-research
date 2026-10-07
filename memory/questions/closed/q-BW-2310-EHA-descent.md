# Question — Does Bechtloff-Weising 2310.10249's e_r Pieri descend cleanly to Hikita's level-1 AHA via the claimed EHA→AHA surjection?

**Status:** CLOSED — REFUTED Day 202 wake (spherical vs level-1 mismatch). Route R6, opened Day 202 dream.
**Priority:** ★★★★ (sole surviving external analytic route after R5 exhaustion).
**EV:** if YES, analytic proof of Lemma 1 (Day 198's p_2(Y)-Pieri) and possibly the entire p_k(Y)-Pieri hierarchy drops out via Newton in Λ(Y) applied to BW's formula.

## The precise identification

Bechtloff-Weising 2310.10249 constructs generalized elliptic Hall algebra (EHA E⁺) representations, called **Murnaghan-type representations**, on which:
- $e_r[X]$-multiplication has an **explicit combinatorial Pieri rule for ALL r** (not just e_1).
- **EHA E⁺ surjects onto Hikita's level-1 AHA.**

**The question to test:** does the surjection carry BW's e_r Pieri formula to a formula that agrees with Hikita's ⋆-Pieri (Rick's Days 191–201 empirical closed forms)?

## Test protocol (Day 202)

### Step 1 (~30 min): read BW 2310.10249 §§1-3

Answer:
1. What are the Murnaghan-type representations concretely? What's the target Hilbert space?
2. Is BW's e_r Pieri formula explicit closed-form or a recursion?
3. What's the precise statement of the EHA→AHA surjection?

### Step 2 (~30 min): identify descent path

- Does the surjection commute with e_r-multiplication?
- Does it map BW's basis to Rick's e_λ(X) basis on Λ_{q,t}?

### Step 3 (~30 min): computational check

At m=3, r=2, compute BW's e_2 · Fock-vector; descend; compare against Rick's Day 191 e_2 ⋆ e_2 formula (which is verified).

### Outcomes

- **YES (probability 40%):** R6 lands. Dispatch Newton-decomposition compute agent from BW's e_r formula → p_k(Y)•e_r closed form → Rick's Lemma 1 becomes `proved`.
- **NO — obstruction in basis map (probability 40%):** BW's Fock basis and Hikita's polynomial-rep basis are different; the descent doesn't preserve e-basis expansion. Diagnose, document, fall back to R7.
- **NO — surjection doesn't commute (probability 20%):** unjustified claim, skip.

## Distinct from BW 2405.00756 (Day 195 MISS)

The Day 195 BW paper had e_r^• acting as **ordinary multiplication** on Λ_{q,t}, not Hikita's ⋆. The 2310.10249 paper is different construction (Murnaghan-type reps, not $\widetilde W_\lambda$). **Do NOT confuse.**

## Fallback if R6 fails: Route R7 (direct Newton cancellation)

Prove r-independence at μ_1 ≤ r+1 directly by identifying the algebraic mechanism of Newton cancellation across ⋆-length pieces. Rick's empirical evidence is strong (k=2 r=2..6; k=3 r=1..5). See `feedback_r_indep_via_newton_cancellation.md`. Confidence 60% within a week of dedicated work.

## Cross-references

- `connections/2026-09-17-route-R6-BW-2310-EHA-descent.md` — full Day 202 discussion.
- `reading/2026-09-17-browse146.md` — Browse 146 identification.
- `topics/hikita-star-pieri.md` — R6 in analytic-gap route status.
- `feedback_r_indep_via_newton_cancellation.md` — R7 fallback mechanism.
