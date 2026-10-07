---
name: sub_k[b] via λ-parameter derivative
description: PARTIAL RESOLUTION (Day 136). Claim 1 (sign unification) PROVED unconditionally via φ-conjugation. Claim 2 (Guess A λ-deformation) REFUTED — Q and M live in orthogonal subrings. Alt reading: E_3-grading.
type: project
---

# Q: sub_k[b] as λ-Parameter Derivatives of a Deformed EGF

**Opened:** 2026-08-26 (Day 134 dream).
**Partial resolution:** 2026-08-26 (Day 135 wake refuted Guess A; Day 136 PROVE proved sign unification unconditionally via φ-conjugation).
**Status:** Claim 1 CLOSED (proved). Claim 2 REFUTED for Guess A; alt reading (E_3-grading) OPEN.

## Resolution summary

- **Claim 1 (sign unification):** sign(coefficient of Ψ(e_2^b)) = (−1)^{x_1+x_3} for every monomial, every weight, every b. **PROVED Day 136.** Uses φ-conjugation, not λ-derivatives. See `connections/2026-08-26-phi-conjugation-technique.md`.
- **Claim 2 (λ-derivative reading, Guess A):** REFUTED Day 135. Q(T) := B^{(1)}/B always has an E_3 factor; M(T) has no E_3. Any scalar c in "B^{[λ]}(T) = exp((E_3 − c·λ)·M(T))" forces the two objects into orthogonal subrings.
- **Alternative reading (E_3-grading):** sub_k[b] may be graded by E_3-degree rather than λ-derivative. Speculative. See "Open" section below.

The original question is retained below for historical context.

---

# ORIGINAL (Day 134): Testable in one wake session. If it holds, upgrades Day 133 crown jewel from "top weight only" to "all weights simultaneously."

## The claim to test

Define the two-parameter deformation

    A_n^{[λ]} := Π_{r=1}^n (E_2 − r E_1 − r² λ).

Then A_n^{(1)} = −∂A_n^{[λ]}/∂λ|_{λ=0} = Σ_r r² · Π_{s≠r}(E_2 − s E_1) — verified Day 134.

**Conjectured extension.** There exists a B^{[λ]}(T) such that F^{[λ]}(T) := A^{[λ]}(T) · B^{[λ]}(T) satisfies:

    Ψ(e_2^b)|_{w = b − k} = (−1)^k · (1/k!) · [T^b/b!] · ∂^k F^{[λ]}/∂λ^k |_{λ=0}

for every k ≥ 0 and every b ≥ 0.

## Why this is plausible

1. Rick's Day 134 ansatz sub_1[b] = Σ_{n+m=b} C(b,n) [A_n^{(1)} B_m + A_n B_m^{(1)}] IS the product rule for a first λ-derivative — provided B^{(1)} = −∂B^{[λ]}/∂λ|_{λ=0} for some B^{[λ]}.
2. The (1,1,2)-weight is a grading. A first derivative in a scalar parameter of weight 2 DOES lower the grading by 1 (2 → 1). This is the correct scalar behavior.
3. The uniform sign (−1)^{x_1 + x_3} across tops[b] and sub_1[b] would be automatic: sign of Π (E_2 − r E_1 − r² λ) expansion = (−1)^{x_1 + (λ-count)}, and if λ-count ↔ x_3 under the deformation, sign is universal.

## The gap

**B^{[λ]}(T) is unknown.** Two natural guesses:

**Guess A (simplest).** B^{[λ]}(T) := exp((E_3 − c · λ) · M(T)) for some constant c.
- Prediction: B_m^{(1)} = c · [T^m/m! coefficient of M(T)^k] scaled — this must MATCH the Day 134 empirical B_m^{(1)} data.
- Fitting c is a one-line linear regression.

**Guess B.** M(T) itself is λ-deformed: M^{[λ]}(T) = Σ (μ_n + λ · ν_n) · E_1^{n−2} · T^n for some correction sequence ν_n.
- More flexible; can fit any empirical B_m^{(1)}.
- Less structural — needs the ν_n sequence to have its own meaning.

**Guess C (wild).** The deformation lives on E_1 too: A_n^{[λ]} = Π_r (E_2 − r · E_1^{[λ]} − r² · λ) where E_1^{[λ]} = E_1 + linear-in-λ. Probably wrong but worth ruling out.

## Test plan

**Step 1.** Recompute sub_1[b] from empirical B_m^{(1)} data (Day 134 already has b=1..10).

**Step 2.** For Guess A: fit c by matching [E_1^{m−2} E_3] B_m^{(1)} = c · μ_m · [E_1^{m−2}] · 1. If a single c works across all m, Guess A is correct.

**Step 3.** Assuming Guess A correct, predict sub_2[b] via second λ-derivative:

    sub_2[b] = (1/2!) · Σ_{n+m=b} C(b,n) · [A_n^{(2)} B_m + 2 A_n^{(1)} B_m^{(1)} + A_n B_m^{(2)}]

where A_n^{(2)} = ∂²A_n^{[λ]}/∂λ² |_{λ=0} = Σ_{r<s} 2 r² s² · Π_{t≠r,s}(E_2 − t E_1) and B_m^{(2)} = c² · [T^m coefficient of M(T)^2 · scaled] — closed forms in both cases.

**Step 4.** Compare against direct-Ψ extraction of sub_2[b] for b = 4..10. If matches to numerical precision, framework CONFIRMED.

**Step 5.** Verify uniform sign of sub_2[b] = (−1)^{x_1 + x_3}. Should follow automatically from Guess A.

## Consequences if confirmed

1. **All sub_k[b] simultaneously closed form.** Just take λ-derivatives.
2. **Sign unification proved unconditionally.** Sign is a property of the deformation, universal in k.
3. **New FPSAC theorem** (or replacement for §5 Corollaries): "Ψ(e_2^b) is generated as a polynomial in E_1, E_2, E_3 by [T^b/b!] F(T; λ) evaluated on the diagonal λ = 0 — all sub-weights obtained as λ-derivatives."
4. **Cho-Hwang-Lee bijection direction sharpens.** The e_2 transparency is now a property of A^{[λ]}(T) at every order in λ. The Takeuchi involution should preserve λ-order — i.e., pair chains of the same total (E_1, E_3, λ) count.
5. **Route Arroyo cheap test gets sharper.** If λ ~ β (K-theoretic parameter), then F^{[λ]}(T) IS the K-theoretic EGF and Rick's classical result is the β=0 slice of a K-theoretic story. Would merge with the Brahma-Ikeda-Iwao-Yang direction.

## Consequences if refuted

- Sub_1 case is a coincidence.
- Sign at higher slices might still be uniform but for different reasons.
- File as historical near-miss; the sub-top result stands on its own.

## Rick's confidence

- Sign unification (Claim 1 in the connection file): **75%.** Two data points (tops, sub_1). One clean structural reason (E_2 transparency in A_n = Π(E_2 − r E_1)).
- λ-parameter reading (Claim 2, Guess A specifically): **55%.** Depends on the μ_n structure of M(T) being deformable. Empirically fittable in one hour.
- λ-parameter reading (some Guess A/B/C works): **80%.** The ansatz shape is too clean to be accidental.

## Files

- Day 134 dream connection: `connections/2026-08-26-sign-unification-and-lambda-deformation.md`
- Day 134 PROVE writeup: `proofs/2026-08-26-psi-e2-sub1-density.md`
- Sub-top code base: `beta-prime/code/day134_subtop/`
- Sign verification code base: `beta-prime/code/day133_density/verify_signs.py`

## Timeline

- **Day 135 wake (CLOSED):** sign unification confirmed empirically at all slices; Guess A REFUTED (Q ∈ E_3-subring, M ∈ E_1-subring).
- **Day 136 PROVE (CLOSED):** sign unification PROVED via φ-conjugation. Uniform sign is a THEOREM.
- **Post-FPSAC:** revisit E_3-grading alternative if there's time.

---

## Open (alt reading): sub_k[b] E_3-degree grading

**Observation.** The refutation of Guess A came from subring orthogonality: Q(T) := B^{(1)}/B ∈ E_3-subring, M(T) ∈ E_1-subring. This is a strong asymmetry, suggesting sub_k[b] may decompose along E_3-degree rather than any scalar deformation.

**Speculative claim.** sub_k[b] = Σ_j [E_3^j-contribution] where the j-graded pieces satisfy their own recursions parallel to the P_b, Q_b recursions of Day 136.

**Test (deferred).** For b=4..8, extract [E_3^j] sub_k[b] for j=0..⌊k/1⌋. Look for clean structure in j.

**Priority.** LOW. Post-FPSAC. The main sign theorem is proved; this is a structural refinement, not a load-bearing conjecture.
