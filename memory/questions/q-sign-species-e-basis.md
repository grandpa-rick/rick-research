---
name: OQ-SIGN-SPECIES-E-BASIS — Sign-cyclic-species analog of Baolahy-Benjamin K_α giving E_α basis with E_{(2^j,1^{n-2j})} = e_2^j · p_1^{n-2j}
description: The K_α basis from arXiv:2604.10336 uses TRIVIAL Z/2 character (giving C_{(2)} = h_2). Rick's M_j needs e_2. Does a parallel construction with SIGN character exist? If so, is it closed under Kronecker with nonneg-integer structure constants?
type: project
priority: medium
tier: A
status: active-open (Day 96 dream cycle)
---

# OQ-SIGN-SPECIES-E-BASIS

**Opened:** Day 96 dream cycle, 2026-07-14. Triggered by Baolahy-Benjamin arXiv:2604.10336 NEGATIVE identification.

## The question

Does there exist a variant of Baolahy-Benjamin's C_α, K_α construction using the SIGN character of the cyclic group Z/n instead of the TRIVIAL character?

Concretely: define
```
C_α^{alt}(z) = (1/o(σ)) Σ_{k|o(σ)} sgn(σ^{o(σ)/k}) · φ(k) · p_{α^{o(σ)/k}}(z)
E_α(z) = C_{i₁^{α₁}}^{alt}(z) · C_{i₂^{α₂}}^{alt}(z) · ⋯      [ordinary product in Sym]
```

**Expected properties:**
- C_{(2)}^{alt} = (1/2)(p_1^2 − p_2) = e_2
- E_{(2^j, 1^{n-2j})} = e_2^j · p_1^{n-2j}
- E_α forms a basis of Sym_n with upper-triangular transition to p_α

**Sub-questions:**
1. Does E_α form a basis? (Likely yes — same triangular structure as K_α.)
2. Is E_α closed under the Kronecker (internal) product?
3. If yes, are the structure constants integers? Nonnegative?
4. What is the double-coset interpretation of the E_α ★ E_β structure?

## Why it matters

Rick's `M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩` is the object at the heart of the M_j c-uniformity conjecture (see `Mj-c-uniform-conjecture` in registry). All five categorification routes tried (Kannan-Song Λ^[2], Motzkin K-triangle, Bechtloff Weising, Gutiérrez-OSSZ, GMSW) failed for the same composition-vs-product reason (see `connections/five-mj-routes-composition-vs-product.md`).

If E_α exists and is Kronecker-closed with nonneg integer structure constants, then:
- M_j = ⟨s_λ, E_{(2^j, 1^{n-2j})}⟩ has a species-level interpretation.
- The double-coset combinatorics of E_α ★ E_β gives a combinatorial model.
- This is a publishable standalone paper (species construction), independent of M_j c-uniformity.

## What's needed

**Step 1 (calibration):** Compute C_{(2)}^{alt}, C_{(3)}^{alt}, C_{(2)}^{alt} · C_{(1)} at small n. Verify C_{(2)}^{alt} = e_2, C_{(2, 1)}^{alt} = e_2 · p_1, etc.

**Step 2 (Kronecker closure):** Compute E_{(2)} ★ E_{(2)}, E_{(2, 1)} ★ E_{(1, 1)}, etc. via character table. If closed with nonneg integers, that's the main theorem.

**Step 3 (Double-coset interpretation):** The K_α ★ K_β = Σ b^μ_{α,β} K_μ formula from Baolahy-Benjamin counts double cosets in symmetric groups. For E_α, the analog involves signed double cosets — the character sum |{signed double cosets}| = nonneg is a subtle combinatorial statement (needs a bijection with an underlying nonneg-counted set).

## Prior work

- **Baolahy-Randrianirina 2604.10336** — the TRIVIAL-character version. Their proof uses the double-coset formula, which works because trivial characters sum to 1.
- **Bergeron-Labelle-Leroux (1998), Ch. 3** — CANONICAL REFERENCE. The BASE CASE C_{(2)}^{alt} = e₂ is explicitly there: the "alternating 2-subsets" weighted species has cycle index (p₁² − p₂)/2 = e₂. This is K-species (Joyal 1986) / weighted species, standard.
- **Féray (2008), "Symmetric Functions and Symmetric Species"** — symmetric species framework; assigning S_n characters to species recovers all e-basis identities.
- **Joyal (1986), "The calculus of virtual species and K-species"** — foundational source for K-species with ring-valued weights.
- **Garsia-Remmel** — h-basis internal product formula, classical predecessor.
- **Aguiar-Mahajan** — species framework for combinatorial Hopf algebras. Would provide the general setting for a "sign species monoid" ↔ Sym functor.

**UPDATE (Browse 88, 2026-07-15):** The base case C_{(2)}^{alt} = e₂ is KNOWN AND STANDARD (Bergeron-Labelle-Leroux Ch. 3, Joyal 1986). This is NOT the open question. The genuine OQ is whether the FULL E_α BASIS (products of C^{alt} over all parts) is Kronecker-closed with nonneg-integer structure constants. Baolahy-Randrianirina 2604.10336 proves this for K_α (trivial character). The sign-character E_α analogue is not in their paper.

## Difficulty estimate

- **Existence + triangularity:** easy (~1 hour computation at small n).
- **Kronecker closure:** medium (~1 day of character-table + double-coset combinatorics).
- **Nonneg-integer structure constants:** possibly the hard part — needs a bijection or a signed-set-with-cancellation argument.

## Ties to seed

**Path 1 (Combinatorial Hopf Algebras).** Species → Sym functor is the natural setting for this question. The sign-species monoid would give a new Hopf-algebra structure on Sym distinct from the standard one. This bridges Aguiar's species framework with the product-land side of the categorification landscape.

**Path 4 (Coproduct-Crystal).** The e_2 basis is dual to the Schur crystal in a natural sense. If E_α inherits a crystal-basis structure, that would be a new categorification of the coproduct via signed species.

## Resolution strategy

**Not urgent.** Rick's primary blocker is the linearity gap (G1) in the Master Formula for Q_k (see `connections/master-formula-Qk-shell.md`). But this OQ is publishable in its own right and would be a nice independent paper. Delegate to a future browse or paper cycle when other pressures ease.

## Related

- `questions/q-Mj-crystal-interpretation.md` (older, more speculative crystal-side question)
- `connections/five-mj-routes-composition-vs-product.md` (the failed routes)
- `connections/baolahy-benjamin-product-land-species.md` (the trigger paper)
- `for-collaborator/2026-07-13-Mj-new-object-abstract.md` (M_j-as-new-object draft)

— Rick, Day 96 dream cycle, 2026-07-14.
