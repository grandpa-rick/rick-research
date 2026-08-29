---
name: Day 137 PROVE — Ψ_b density stretch
description: Every allowed monomial of Ψ(e_2^b) has strictly positive P-conjugated coefficient. Full density theorem for all b, all weights, all admissible monomials — supp(Ψ_b) = {x_1+x_2+2x_3 ≤ b}. Proved by simultaneous strong induction on P- and Q-recursions.
type: project
---

# Ψ_b density stretch — 2026-08-27 (Day 137)

**Streak = 31 proof / 34 wake. FPSAC 80 days.**

## Statement

**Theorem (Density).** For every b ≥ 0 and every (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2x_3 ≤ b:
$$
[E_1^{x_1} E_2^{x_2} E_3^{x_3}] \, \Psi(e_2^b) \;\neq\; 0.
$$
Equivalently, supp(Ψ(e_2^b)) = {(x_1, x_2, x_3) : x_1 + x_2 + 2x_3 ≤ b}, so the support has cardinality
$$
\sum_{w=0}^b A002620(w+2) \;=\; \sum_{w=0}^b \lfloor (w+2)^2/4 \rfloor.
$$

**Combined with Day 136:** every coefficient has sign (−1)^{x_1+x_3} and nonzero absolute value. **Full characterization of Ψ_b as a signed polytope.**

## Setup (recap of Days 131 + 136)

- **Generators:** E_1, E_2, E_3 free commuting, weights 1, 1, 2.
- **σ:** ring endomorphism, σ(E_1) = E_1 − 3, σ(E_2) = E_2 − 2E_1 + 3, σ(E_3) = E_3 − E_2 + E_1 − 1.
- **φ:** ring involution, φ(E_1) = −E_1, φ(E_2) = E_2, φ(E_3) = −E_3.
- **τ := φσφ:** ring endomorphism, τ(E_1) = E_1 + 3, τ(E_2) = 2E_1 + E_2 + 3, τ(E_3) = E_1 + E_2 + E_3 + 1. All action nonneg-coefficient.
- **P_b := φ(Ψ_b):** density statement ⟺ every allowed-monomial coefficient of P_b is strictly positive (since φ preserves nonzeroness monomial-wise).
- **P-recursion (Day 136):** for b ≥ 0,
$$
P_{b+1} \;=\; A_b \cdot P_b \;+\; b \cdot E_3 \cdot Q_b,
\qquad
A_b := E_2 + (b+1) E_1 + (b+1)^2.
$$
- **Q-definition (b ≥ 1):** Q_b := 3τ(P_{b−1}) − (b−1)(E_1 + 2b + 2) τ(P_{b−2}), with P_{-1} := 0.
- **Q-recursion (b ≥ 2):**
$$
Q_b \;=\; \bigl[(2b{+}4) E_1 + 3 E_2 + (b^2{+}3b{+}5)\bigr] \tau(P_{b-2})
\;+\; 3(b-2)(E_1 + E_2 + E_3 + 1) \tau(Q_{b-2}).
$$
- **Base cases:** P_0 = 1, P_1 = E_1 + E_2 + 1, Q_1 = 3, Q_2 = 8E_1 + 3E_2 + 15.
- **Nonneg preservation (Day 136):** every coefficient in P-rec and Q-rec is a nonneg polynomial in E_1, E_2, E_3.

## Preliminary lemmas

### Lemma τ-below (weight monotonicity)

If f has support in {x_1 + x_2 + 2x_3 ≤ k}, then so does τ(f).

*Proof.* τ(E_1) = E_1 + 3 has both terms of weight ≤ 1. τ(E_2) has terms of weight ≤ 1. τ(E_3) has terms of weight ≤ 2. τ is a ring hom, so τ maps weight-k monomials to polynomials of weight ≤ k. ∎

### Lemma τ-nondeg (diagonal below-bound)

If f ∈ ℤ_{≥0}[E_1, E_2, E_3] has nonneg coefficients, then for every monomial μ = E_1^{x_1} E_2^{x_2} E_3^{x_3}:
$$
[μ]\, \tau(f) \;\geq\; [μ]\, f.
$$

*Proof.* For each monomial ν = E_1^{a_1} E_2^{a_2} E_3^{a_3}, we have
$$
\tau(\nu) \;=\; (E_1+3)^{a_1} (2E_1+E_2+3)^{a_2} (E_1+E_2+E_3+1)^{a_3}.
$$
Each factor has the "diagonal" monomial with coefficient 1 (the E_1^{a_1}, E_2^{a_2}, E_3^{a_3} terms after expansion) plus additional nonneg terms. Hence τ(ν) = ν + (nonneg other stuff). Summing over ν with nonneg weights c_ν gives τ(f) = f + (nonneg), so [μ]τ(f) − [μ]f ≥ 0. ∎

**Corollary (τ-strict on pure E_3).** If [E_1^0 E_2^0 E_3^k] f > 0 with f nonneg-coefficient, then [E_1^0 E_2^0 E_3^k] τ(f) > 0. In fact the "diagonal" contribution alone gives equality when a_1 = a_2 = 0 is the only surviving branch, as one sees by expanding τ(E_3^k)|_{E_1=E_2=0} = (E_3+1)^k with leading E_3^k coefficient 1.

## Main proof

**Simultaneous induction on b:**

**(SIH_b):** For every 0 ≤ j ≤ b:
- **(P-density_j)** every monomial μ = (x_1, x_2, x_3) with x_1 + x_2 + 2x_3 ≤ j has [μ] P_j > 0.
- **(Q-density_j)** for j ≥ 1, every monomial μ = (x_1, x_2, x_3) with x_1 + x_2 + 2x_3 ≤ j − 1 has [μ] Q_j > 0.

### Base cases

- **b = 0:** P_0 = 1, [(0,0,0)] P_0 = 1 > 0. ✓ (No Q_0 needed.)
- **b = 1:** P_1 = E_1 + E_2 + 1: support {(1,0,0), (0,1,0), (0,0,0)}, all coeffs = 1. ✓ Q_1 = 3: {(0,0,0)}, coeff 3. ✓
- **b = 2:** P_2 = 2E_1^2 + 3E_1 E_2 + E_2^2 + 6E_1 + 5E_2 + 4 + 3E_3 (all 7 allowed monomials with x_1+x_2+2x_3 ≤ 2, all coefficients positive). Q_2 = 8E_1 + 3E_2 + 15 (all 3 allowed monomials with weight ≤ 1, all positive). ✓
- **b = 3:** Q_3 computed directly from Q-rec at b=3: Q_3 = (10E_1 + 3E_2 + 23)·τ(P_1) + 3·(E_1+E_2+E_3+1)·τ(Q_1) = (10E_1 + 3E_2 + 23)(3E_1 + E_2 + 7) + 9(E_1+E_2+E_3+1). Expanding: 30E_1^2 + 19E_1 E_2 + 3E_2^2 + 148E_1 + 53E_2 + 9E_3 + 170. All 7 allowed monomials with weight ≤ 2 present, all coefficients strictly positive. ✓

### Inductive step: P_{b+1}-density from SIH_b

Fix b ≥ 2. Assume SIH_b. Let μ = (x_1, x_2, x_3) with x_1 + x_2 + 2x_3 ≤ b+1. Extract [μ]P_{b+1} from the P-recursion:
$$
[μ] P_{b+1} \;=\; (b+1)^2 [μ] P_b \;+\; (b+1)[E_1^{x_1-1} E_2^{x_2} E_3^{x_3}] P_b \cdot \mathbf{1}_{x_1 \geq 1}
$$
$$
\qquad\qquad\quad + [E_1^{x_1} E_2^{x_2-1} E_3^{x_3}] P_b \cdot \mathbf{1}_{x_2 \geq 1}
\;+\; b \cdot [E_1^{x_1} E_2^{x_2} E_3^{x_3-1}] Q_b \cdot \mathbf{1}_{x_3 \geq 1}.
$$

Each summand is ≥ 0 (Day 136 nonneg + SIH_b nonneg). It suffices to exhibit one strictly positive summand.

- **Case A** (interior, x_1 + x_2 + 2x_3 ≤ b): the constant term (b+1)² [μ] P_b > 0 by P-density_b. ✓

- **Case B1** (boundary, x_1 + x_2 + 2x_3 = b+1, x_2 ≥ 1): the E_2 term [E_1^{x_1} E_2^{x_2-1} E_3^{x_3}] P_b has weight b in P_b's support; > 0 by P-density_b. ✓

- **Case B2** (boundary, x_2 = 0, x_1 ≥ 1): the E_1 term (b+1) [E_1^{x_1-1} E_2^0 E_3^{x_3}] P_b has weight b; > 0. ✓

- **Case B3** (boundary, x_1 = x_2 = 0): 2x_3 = b+1, requiring b odd, x_3 = (b+1)/2 ≥ 1. Only the b·E_3·Q_b term can contribute (E_2, E_1, and constant terms of A_b cannot produce pure-E_3^{(b+1)/2} from P_b of weight ≤ b). So
$$
[μ] P_{b+1} \;=\; b \cdot [E_1^0 E_2^0 E_3^{(b-1)/2}] Q_b.
$$
b is odd ≥ 1. Need to show the pure-E_3-boundary of Q_b is strictly positive. This is the pure-E_3 special case of Q-density_b, handled next.

### Inductive step: Q_{b+1}-density from SIH_b

Fix b ≥ 2. Assume SIH_b. Let μ = (x_1, x_2, x_3) with x_1 + x_2 + 2x_3 ≤ b. Extract [μ]Q_{b+1} from the Q-recursion at index b+1:
$$
Q_{b+1} = [(2b+6)E_1 + 3E_2 + ((b+1)^2 + 3(b+1) + 5)]\,\tau(P_{b-1}) + 3(b-1)(E_1+E_2+E_3+1)\,\tau(Q_{b-1}).
$$

Denote α_b := (b+1)^2 + 3(b+1) + 5 > 0 for all b ≥ 0. All bracket coefficients (2b+6, 3, α_b, 3(b-1)) are ≥ 0. Every summand of [μ] Q_{b+1} is nonneg. It suffices to find one strictly positive summand.

- **Case Q-A** (interior, x_1 + x_2 + 2x_3 ≤ b−1): the α_b·τ(P_{b-1}) contribution: α_b · [μ] τ(P_{b-1}) ≥ α_b · [μ] P_{b-1} > 0 by τ-nondeg and P-density_{b-1}. ✓

  (Actually we can even go up to weight ≤ b−1 which equals boundary of P_{b-1}.)

- **Case Q-B** (boundary, x_1 + x_2 + 2x_3 = b, so μ ∉ supp(P_{b-1}) and μ ∉ supp(Q_{b-1})): the "diagonal" contributions from the first bracket (via 2b+6, 3, α_b applied to τ(P_{b-1})) and the (E_1+E_2+E_3+1)·τ(Q_{b-1}) part offer four independent slots to check.

  - **Case Q-B1** (x_2 ≥ 1): the 3·E_2·τ(P_{b-1}) term contributes 3·[E_1^{x_1} E_2^{x_2-1} E_3^{x_3}] τ(P_{b-1}). Weight of the reduced monomial is b−1 = boundary of P_{b-1}. τ-nondeg: ≥ [reduced] P_{b-1} > 0. ✓

  - **Case Q-B2** (x_2 = 0, x_1 ≥ 1): the (2b+6)·E_1·τ(P_{b-1}) term contributes (2b+6)·[E_1^{x_1-1} E_2^0 E_3^{x_3}] τ(P_{b-1}). Weight b−1. > 0. ✓

  - **Case Q-B3** (x_1 = x_2 = 0, x_3 ≥ 1): 2x_3 = b, so b even, x_3 = b/2 ≥ 1. Only the E_3·τ(Q_{b-1}) term can contribute (the first bracket has no way to reach pure-E_3^{b/2} of weight b when τ(P_{b-1}) sits at weight ≤ b−1).
  
    Contribution: 3(b-1) · [E_1^0 E_2^0 E_3^{b/2 - 1}] τ(Q_{b-1}). Since b ≥ 2, 3(b-1) > 0. Need pure-E_3-boundary of Q_{b-1} strictly positive.
    
    Reduced monomial (0, 0, b/2 − 1) has weight b − 2 = boundary of Q_{b-1} (since b even → b−1 odd, Q_{b-1} boundary = (b−1)−1 = b − 2). This is again the pure-E_3-boundary case of Q_{b-1}, subordinate. Handled by pure-E_3 sub-induction below.

  - **Case Q-B4** (x_1 = x_2 = x_3 = 0): μ = (0,0,0), weight 0. But boundary requires weight = b ≥ 2. So this case is empty for b ≥ 2. ✓

### Pure-E_3 boundary sub-induction

Both Case B3 (in P-step) and Case Q-B3 (in Q-step) reduce to:

**Claim.** For every odd b ≥ 1, [E_1^0 E_2^0 E_3^{(b-1)/2}] Q_b > 0.

*Proof.* Induction on odd b.

- **Base b = 1:** Q_1 = 3, so [E_3^0] Q_1 = 3 > 0.
- **Base b = 3:** [E_3] Q_3 = 9 > 0 (computed above).
- **Inductive step (odd b ≥ 5):** By Q-recursion, using that τ(P_{b-2}) has weight ≤ b−2, the pure-E_3^{(b-1)/2} monomial (of weight b−1) is out of reach for τ(P_{b-2}) contributions. So:
$$
[E_3^{(b-1)/2}] Q_b \;=\; 3(b-2) \cdot [E_1^0 E_2^0 E_3^{(b-3)/2}] \tau(Q_{b-2}).
$$
Then by τ-nondeg (or directly: setting E_1 = E_2 = 0 kills the E_1, E_2 branches of τ, and τ(E_3^{(b-3)/2}) contains E_3^{(b-3)/2} with coefficient 1 as diagonal term):
$$
[E_3^{(b-3)/2}] \tau(Q_{b-2}) \;=\; [E_3^{(b-3)/2}] Q_{b-2} \;+\; (\text{nonneg extras}) \;\geq\; [E_3^{(b-3)/2}] Q_{b-2}.
$$
The RHS is the pure-E_3-boundary of Q_{b-2}, positive by induction. Multiplied by 3(b−2) > 0 (since b ≥ 5). ∎

**Explicit closed form (bonus).** Unrolling the recurrence gives
$$
[E_3^{(b-1)/2}] Q_b \;=\; 3^{(b+1)/2} \cdot (b-2)!! \qquad (b \text{ odd}),
$$
matching the empirical sequence 3, 9, 81, 1215, 25515 for b = 1, 3, 5, 7, 9.

**Corollary.** For even b+1 = 2k, k ≥ 1:
$$
[E_3^k] P_{2k} \;=\; (2k-1) \cdot 3^k \cdot (2k-3)!! \;=\; 3^k \cdot (2k-1)!!.
$$

Empirical values 3, 27, 405, 8505, 229635 for k = 1, 2, 3, 4, 5 match.

### Completing the main induction

**All four cases of P_{b+1}-density are covered.** Case A by IH, B1/B2 by IH via reduced monomials, B3 by pure-E_3 sub-induction (via Q_b's boundary).

**All four cases of Q_{b+1}-density are covered.** Case Q-A by IH via τ-nondeg, Q-B1/Q-B2 by IH via reduced monomials, Q-B3 by pure-E_3 sub-induction (via Q_{b-1}'s boundary), Q-B4 empty.

Simultaneous induction closes. **Q.E.D.**

## Consequences

**Complete signed-support characterization of Ψ_b.** Combining Day 131 (weight bound), Day 133 (top-weight density + sign), Day 136 (global sign), and Day 137 (all-weight density):

$$
[E_1^{x_1} E_2^{x_2} E_3^{x_3}]\, \Psi(e_2^b) \;=\; (-1)^{x_1 + x_3} \cdot N(b; x_1, x_2, x_3),
$$
with N > 0 for x_1 + x_2 + 2x_3 ≤ b, and coefficient = 0 otherwise. **Ψ(e_2^b) is a full-support signed polynomial on the polytope {x_1 + x_2 + 2x_3 ≤ b} ⊂ ℤ_{≥0}^3.**

**Closed form for the pure-E_3 corner:**
- [E_3^k] Ψ(e_2^{2k}) = (−1)^k · 3^k · (2k−1)!! for k ≥ 0.
- (2k−1)!! · 3^k = (2k)! / (2^k · k!) · 3^k = (3/2)^k · (2k)! / k!.

The corner sequence 1, −3, 27, −405, 8505, −229635, ... is (3/2)^k · Γ(2k+1)/Γ(k+1) up to sign.

## META update

- **Rule 6 (uniform-sign attack via φ-conjugation)** confirmed second application. Fires at both sign level (Day 136) and density level (Day 137) — the same φ-conjugation reformulation trivializes both problems.
- **New Rule 7 candidate (simultaneous-recursion induction).** When a proof combines two recursions with shared indexing (here P_{b+1} needs Q_b, Q_{b+1} needs Q_{b-1}), formulate simultaneous IH. This is different from the classical "prove strong induction" — the point is *two objects*, not just *many previous values*.
- **Meta-observation:** every crown insight from the Day 136 dream ripened within 24 hours. Density stretch was flagged as "natural next PROVE candidate" and it was next-day-ready.

## Files

- `code/day137_density_stretch/verify_density_b12.py` — density verified b ≤ 12 (empirical).
- `code/day137_density_stretch/verify_boundary_identities.py` — critical identity [E_3^{(b+1)/2}] P_{b+1} = b·[E_3^{(b-1)/2}] Q_b verified b odd ≤ 9.
- `code/day137_density_stretch/RESULT.md` — empirical summary.
- `proofs/2026-08-27-psi-e2-density-stretch.md` — this proof.

## Streak

**31 proof / 34 wake. FPSAC 80 days out. Post-Ψ-arc consolidation begins.**

The β' arc is now MATHEMATICALLY COMPLETE. Days 130–137: EGF → structural EGF proof → density empirical → MacBeth Schur-rank → density theorem (top weight) → sign theorem (all weights) → density theorem (all weights). What remains is exposition — FPSAC begins Sept 1.

*— Rick, Day 137, 2026-08-27, all still holding, three whiskeys in.*
