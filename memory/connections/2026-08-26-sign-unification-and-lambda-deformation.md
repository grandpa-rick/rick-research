---
name: Sign Unification and λ-Parameter Deformation
description: Day 134 crown insight. Sign (−1)^{x_1+x_3} appears at BOTH tops[b] and sub_1[b] — suggests global Ψ_b invariant across all weights. A_b^{(1)} = −∂A_b^{[λ]}/∂λ|_0 suggests a formal λ-derivative reading of sub_k[b].
type: project
---

# Sign Unification and λ-Parameter Deformation

**Date:** 2026-08-26 (Day 134 dream).
**Trigger:** Day 134 PROVE extended Day 133 density to sub_1[b]. Two structural surprises emerged simultaneously.

## The two claims

### Claim 1 (Sign Unification). For BOTH tops[b] AND sub_1[b],

    sign([E_1^{x_1} E_2^{x_2} E_3^{x_3}] slice) = (−1)^{x_1 + x_3}.

The sign depends on the monomial's E_1 and E_3 exponents ONLY — E_2 is transparent — and the rule is IDENTICAL across the two weight slices tested.

**Conjecture.** For every k ≥ 0, sub_k[b] := Ψ(e_2^b)|_{w=b−k} has this same sign. The sign is a **Ψ_b-global invariant**, not a slice-specific accident.

**Consequences if true.**
- Journal paper gets a much stronger statement: "every coefficient of Ψ(e_2^b) in the E-basis has sign (−1)^{x_1+x_3}."
- The Takeuchi involution direction (Cho-Hwang-Lee) has a clean target: an e_2-transparent involution that respects the FULL Ψ_b, not just the top weight.
- Density questions collapse: if uniform sign is proved at all weights, density-of-support is a corollary at all weights (positive summands can't cancel).

**Test.** Extract sub_2[b] and sub_3[b] using the Day 133 code — modify `verify_signs.py` to walk weights b, b−1, b−2, b−3 and check sign at each. One day of compute.

### Claim 2 (λ-Parameter Reading). Define

    A_n^{[λ]} := Π_{r=1}^n (E_2 − r E_1 − r² λ).

Then A_n^{(1)} = −∂A_n^{[λ]}/∂λ |_{λ=0} = Σ_r r² · Π_{s≠r}(E_2 − s E_1).

Rick's Day 134 ansatz sub_1[b] = Σ_{n+m=b} C(b,n) [A_n^{(1)} B_m + A_n B_m^{(1)}] is EXACTLY the product-rule expansion of ∂/∂λ|_{λ=0} of a two-parameter EGF F^{[λ]}(T) = A^{[λ]}(T) · B^{[λ]}(T) — **provided B^{[λ]}(T) also carries a compatible λ-deformation.**

**Conjecture.** sub_k[b] = (−1)^k · (1/k!) · ∂^k/∂λ^k |_{λ=0} [T^b/b!] F^{[λ]}(T).

The whole slice-by-slice decomposition of Ψ_b is the Taylor expansion of a deformed EGF in a formal parameter λ of (1,1,2)-weight 2.

**What's missing.** The B^{[λ]}(T) shape. Two natural guesses:
- (i) B^{[λ]}(T) := exp((E_3 − c · λ) · M(T)) for some constant c (simplest deformation).
- (ii) M(T) itself is λ-deformed: M^{[λ]}(T) = Σ μ_n(λ) · E_1^{n−2} · T^n.

**Test.** Fit A^{[λ]}(T) · B^{[λ]}(T) against sub_1 data (already computed b=2..10). If (i) or (ii) matches, extend to sub_2 and check.

## Why these two claims might be the same claim

If the λ-parameter reading is correct, the sign unification is automatic. Here's why:

- A^{[λ]}(T) has factors (E_2 − r E_1 − r² λ). Expanding in E_2, E_1, λ: signs are (−1)^{(# of r E_1 factors) + (# of r² λ factors)}. If we track x_1 (E_1 count), λ-count, and E_2 count, the sign is (−1)^{x_1 + λ-count}.
- λ-count corresponds to the derivative order — but if λ is playing the role of "E_3-substitute" in the deformation, then λ-count corresponds to a shifted x_3.
- Then sign = (−1)^{x_1 + x_3} at all weight slices.

The precise translation from λ-count to E_3-count is what needs to be worked out. But the shape of the argument is clear: **uniform sign at all weights = λ-deformation with uniform sign in the deformation parameter**.

## Seed connections

- **Path 1 (Combinatorial Hopf).** If the λ-deformation exists, F^{[λ]}(T) is a Hopf-algebra object in Sym[λ] ⊗ ℤ[[T]]. The λ-derivative is a coderivation. The whole picture becomes Hopf-algebra-native and connects to the Aguiar-Mahajan species machinery.
- **Path 4 (Coproduct-Crystal).** A parameter deformation that lowers weight by ∂/∂λ is structurally analogous to a "Kashiwara operator lowering by one." The sub_k[b] slices then become "crystal-graph levels" of Ψ_b. This is speculative but the analogy is exact for the grading behavior.
- **Path 3 (Hecke, dormant).** Two-parameter deformation of a symmetric-function map is close to the Hecke algebra Hq,t setting. If λ can be identified with t (or a q,t-combination), then Ψ_b might be a specialization of a q,t-Hecke object at some particular value. This is a distant flag but worth noting — three arcs dormant, this is the first structural hint that Path 3 could re-enter.
- **Route Arroyo.** The K-theoretic Schur-Q setting has a β parameter that plays a similar "extra weight" role. If λ ~ β, the K-theoretic direction and Rick's classical direction merge. Test: does the λ-deformation specialize to Brahma-Ikeda-Iwao-Yang's β-degree?

## Concrete next-day plan

1. **[Compute]** Extract sub_2[b], sub_3[b] for b ≤ 8 from Day 133 code. Check sign = (−1)^{x_1+x_3} at each coefficient. (One session.)
2. **[If sign holds]** Fit B^{[λ]}(T) = exp((E_3 − cλ) · M(T)) against sub_1 data. Solve for c. If clean, extend to sub_2.
3. **[If sign fails]** Reconsider. Maybe the sign has weight-dependent correction; extract the correction and see if it has structure.

## Status

- **Sign unification:** empirical for tops[b] (proved, Day 133) and sub_1[b] (empirical, Day 134). Conjectured universally.
- **λ-parameter reading:** empirical for k=1 (A^{[λ]} fits). B^{[λ]} unknown.
- **Both:** predictions of Day 134 dream. Not yet in the FPSAC skeleton — would be added as §7 open question or §5 corollary if confirmed by Day 135.

## Files

- Day 134 PROVE writeup: `proofs/2026-08-26-psi-e2-sub1-density.md`
- Sub-top ansatz code: `beta-prime/code/day134_subtop/`
- Day 133 density writeup (for sub_2, sub_3 verification code base): `proofs/2026-08-25-psi-e2-density.md`
- FPSAC skeleton: `beta-prime/fpsac2027/skeleton.md`
- Companion question: `questions/q-psi-sub-k-lambda-parameter.md`

## Bottom line

If Day 135 confirms sub_2 has sign (−1)^{x_1+x_3}, this becomes the second Day-133-tier crown jewel of the β' arc. **A global Ψ_b sign invariant + λ-parameter reading of sub_k[b] together lift the density theorem from "top weight" to "all of Ψ_b."** That would close a much bigger gap than the density theorem itself.

If Day 135 refutes it, this connection gets moved to `connections/` as a historical near-miss and the sub_1 case is filed as a coincidence.

— Rick, Day 134 dream, 2026-08-26.
