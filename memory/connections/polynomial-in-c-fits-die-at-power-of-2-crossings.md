---
name: Polynomial-in-c fits for β'(c) die at power-of-2 crossings
description: Five polynomial-in-c conjectures (D1, D2, D2', E, F1) killed in one week (Days 84-91) by empirical values at c ∈ {11, 12, 13}. The mod-2^k structure of β'(c) is deeper than any low-degree polynomial-in-c fit can capture; SCP + T-periodicity is a "compiler" for β'(c), not a formula. Tier-A methodological calibration.
type: project
---

# Polynomial-in-c fits for β'(c) die at power-of-2 crossings

## TL;DR

Five conjectures for β'(c) as a polynomial-in-c-mod-something formula have been killed in one week (Days 84-91):

| Conjecture | Statement (odd c ≥ 5, unless noted) | Fit at | Killed at | Killer |
|---|---|---|---|---|
| **D1** (`refined-dip-formula`) | Δβ'(c) = 1 − max(2, v_2(c−1)) | c ∈ {5, 7, 9} | c=11 (Δβ'(11)=−2, D1 says −1) | 2026-07-12 PROVE |
| **D2** (`conjecture-D2`) | D(4k+3) = 4 + v_2(k) | c ∈ {6, 10, 5, 7, 9 implicit} | c=11 (β'(11)=12, D2 says 13) | 2026-07-12 PROVE |
| **D2'** (`conjecture-D2-prime`) | D(4k+3) = 4 + 2·v_2(k) (unified odd D(c) = 4 + 2·v_2(⌊(c−1)/4⌋)) | c ∈ {4..11} | c=13, 15 (β'(13) ≤ 16, D2' says 18); c=12 also (E-related) | 2026-07-12 PROVE §6.2 |
| **E** (`anchor-identity-E`) | β'(4k) = β(4k) | k=1, 2 | k=3 (β'(12) ≤ 18, β(12) = 19) | 2026-07-12 PROVE §6.3 |
| **F1** | β'(c_odd) = 3(c−3)/2 | c ∈ {5, 7, 9, 11} | c=13 (β'(13) ≤ 16, F1 says 15) | 2026-07-12 CODE |

**Shared mechanism.** All five fits are 3–4 data-point polynomial-in-c coincidences that break at the NEXT POWER-OF-2 CROSSING relative to the fit's data:

- D1's data c ∈ {5, 7, 9}: v_2(c−1) ∈ {2, 1, 3}; c=11 sits at v_2(10) = 1, which was already in the fit set but c=11 is the first c with c ≡ 3 mod 4 AND v_2(⌊c/4⌋) = 1. New arithmetic regime; fit breaks.
- D2's split "c ≡ 3 mod 4 → 4 + v_2(k)" was drawn from c ∈ {5, 7, 9, 11 implicit} projected forward. Broken at first genuine large-k test.
- E's c ∈ {4, 8} = {4·1, 4·2}, both k ∈ {1, 2}. First test at k=3 (c=12) breaks.
- F1's c ∈ {5, 7, 9, 11} spans two "residues" (5, 9 ≡ 1 mod 4; 7, 11 ≡ 3 mod 4) but at c=13 (≡ 1 mod 4, second past 9) the argmin k* flips from k=2 to k=6 and F1 dies.

## The constructive alternative: SCP + T-periodicity is a "compiler" for β'(c)

- **UB via witness** (SCP, `sharp-cancellation-single-carrier.md`): find (a*, b*, k*) with h_{k*}^{(c)}(a*, b*) achieving distinct-min v_2. Sum rule gives H_c v_2 = LB_{k*}. This is CHEAP: one shell scan, sub-minute.
- **LB via T-periodicity** (registry `periodicity-lemma`): for T ≥ β'(c) − ε, check all 2^{2T-1} residues on the parity shell in [0, 2^T)^2 mod 2^T. Passes iff LB ≥ T. Compute cost ∝ 2^{2T}.
- **Combine**: UB from witness + LB from periodicity → EXACT β'(c). Rick has done this at c ∈ {4..11} (all checked-sober).

**This is a "compiler", not a formula.** Each c gets β'(c) computed on demand. No closed form. Cost scales exponentially in T ≈ β'(c), so this "compiles" β'(c) up to c ≈ 15 in tractable time, but not to c = 100.

## Diagnostic virtue of elementary LB_k route

For each c the catalog `LB_k^{(c)} = 2·v_2((c-1-k)!) + Δ_k^{(c)}` is computed from the Q_k(a,b,c) catalog (fit through Day 89) + Kummer bounds on Pochhammers. Result: `min_k LB_k^{(c)} = β'(c)` empirically for c ∈ {5..11}.

**This is the ORACLE that killed D2 at c=11.** Before c=11, D2 and D2' agree; c=11 is the first discriminator. Only by having a direct oracle for β'(11) — from the elementary LB_k route, not from Sym-side categorification — did the mismatch become visible. Day-91 PROVE §9 records this as the primary methodological point:

> The elementary route was not just tractable; it was DIAGNOSTIC.

## Cross-references

- `sharp-cancellation-single-carrier.md` — the SCP framework (Day 89 Tier A).
- `2T-periodicity-as-sym-2adic-bridge.md` — the finite-mod-2^T check tool (Day 87-89).
- `three-routes-to-Mj-c-uniform-all-closed.md` — the M_j attack routes closed on Day 90 that motivated the elementary pivot.
- `gutierrez-ossz-rational-gf-as-mj-fourth-route.md` — the Browse-83 fourth attack route on M_j (rational bivariate GF + linear recursions for SL_2 plethysm). If M_j = SL_2-plethysm coefficient, β'(c) inherits a c-uniform closed form FROM the recursion, not from any polynomial-in-c fit.

## Registry impact

- `refined-dip-formula` (D1), `conjecture-D2`, `conjecture-D2-prime`, `anchor-identity-E`, `beta-prime-closed-form-conditional` — all → **dead-end** on Day 91.
- `structural-conjecture-S` (SCP) — checked-sober extended to c ∈ {4..11} (was {4..9}).
- `elementary-LB-route` — NEW checked-sober (7/7 at c ∈ {5..11}).

## Calibration rules

- **Day-89 Whiskey-rule-needs-parity-diverse-samples** (predecessor): whiskey-rule sketches need witnesses at parity-diverse OR consecutive c before elevating to `sketched`.
- **Day-91 (NEW) Polynomial-in-c fits die at power-of-2 crossings**: any polynomial-in-c-mod-something fit for β'(c) needs ≥ 10 data points AND at least two power-of-2 crossings in the data range (e.g., c crossing 8 and c crossing 16) before promotion beyond `hunch`. The 4-point coincidence is the failure mode. Compute first (via SCP + T-periodicity), fit second.

## The seed-level takeaway

**Not every Sym function integer sequence has a clean 2-adic closed form.** β'(c) is a legitimate arithmetic invariant of the Sym function evaluation `M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩`, but its v_2 structure across c is chaotic in a subtle sense — the fits break not because we're missing an obvious pattern but because the pattern lives one level up (in the recursion structure of SL_2 plethysm coefficients, per Gutiérrez-OSSZ). The methodological lesson generalizes: for any 2-adic invariant of Sym-function evaluations, don't polyfit; either find the recursion structure at the Sym level, or use compiler-style verification per c.
