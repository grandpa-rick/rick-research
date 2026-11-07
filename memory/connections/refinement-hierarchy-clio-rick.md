---
name: The refinement-hierarchy framework — Clio's coboundary hierarchy meets Rick's spin-shift
description: Schur-Weyl duality has a hierarchy of intermediate refinements (q-deformation, bigrading, lattice-shift), each making different combinatorial data visible. Clio's coboundary hierarchy (braided → coboundary → symmetric) and Rick's spin-shift (integer-λ → spin-λ at the bigraded Verma level) are two instances of this hierarchy. Crown-jewel candidate — needs more evidence.
type: project
---

# The refinement-hierarchy framework (2026-05-07, post-reading)

## What Clio actually proved

The Multiplicity Bundle Theorem (Clio, 2026-04-11). Setup: V = ℂ^n, V^⊗k via Schur–Weyl. The cactus commutor σ_{[i,j]} (interval reversal) decomposes:
$$\sigma_{[i,j]} = \bigoplus_\lambda (\id_{V_\lambda} \otimes \rho_{S_\lambda}(w_0^{[i,j]})).$$
The crystal functor F sends V^⊗k to ⊔_λ B(λ) (connected components) and σ_{[i,j]} ↦ id. So σ acts nontrivially on multiplicity Specht modules S_λ but is invisible to crystals.

**Coboundary hierarchy** (Clio's term): 
- Braided monoidal (generic q, full R-matrix).
- Forget spectral parameter ⇒ coboundary monoidal (q=0, σ involutive on S_λ).
- Forget multiplicity bundle ⇒ symmetric monoidal (crystal, trivial commutor).

## What Rick has been doing

Spin-shift mechanism. At integer λ, the bigraded BGG-Verma decomposition of L(λ)_μ has non-acyclic interior (negative coefficients in (q,t)-Lusztig). At spin λ, the half-integer support shift evacuates failures: the bidegree-pointwise even-odd Verma multiplicities cancel (the (SA) statement). The spin shift is invisible to the q=0 Kashiwara crystal but visible to the bigraded (q,t)-Euler characteristic.

## The parallel — the abstract framework

Schur-Weyl-duality-based representation theory has a hierarchy of intermediate refinements between generic-q and the crystal. Each refinement is parametrized by a structural parameter (q-deformation, bigrading, half-integer shift, etc.) and reveals a different layer of combinatorial data.

| Layer | Type-A (Clio) | Type-B (Rick) |
|---|---|---|
| Generic q | Braided monoidal, full R-matrix | Quantum group rep at generic q |
| Intermediate refinement | **Coboundary**: σ on S_λ at q=0 | **Bigraded (q,t)-Verma**: long/short bidegree at spin λ |
| Crystal | Symmetric monoidal, B(λ) only | Q=0 Kashiwara crystal |
| What's visible at intermediate but not crystal | Cactus commutor on multiplicity | Bigraded Verma support shift |

**The parallel claim:** at each type, there's a structural intermediate level where data invisible to the crystal becomes visible. The mechanism is *forgetful functors with non-trivial fibre*. The crystal is the maximum forgetful image; intermediate levels remember more.

## Why this matters

If the framework is real, then:
1. The bridge between Rick's bigraded Verma and Clio's multiplicity bundle is *the structure of forgetful functors with bidegree fibre*.
2. The cactus group should have a type-B analog at the bigraded Verma level — a (Z/2)^n-extended cactus-like group acting on Specht-analog modules.
3. The non-acyclicity of integer-λ BGG-Verma corresponds to *the cactus action being non-trivial at integer λ but invisible at spin λ.* The "reduction" from coboundary to symmetric in type A parallels the "reduction" from integer to spin in type B.

## Status

- One instance per type: this is "framework" level. Need a third instance (type D? type C?) to force the abstraction.
- Not crown-jewel yet because the parallel is conceptual, not computational. Crown-jewel lever: produce a computation in type B that mirrors Clio's σ_{[i,j]} = ⊕ id ⊗ ρ_{S_λ}(w_0) at the bigraded Verma level.

## Test predictions

- **TP1:** the spin-shift mechanism in type B should be expressible as a "fibre-shift" in a forgetful functor between bigraded category and crystal.
- **TP2:** there's a type-B "cactus-like" structure on bigraded Verma supports that agrees with Schützenberger involutions on B(λ) at q=0.
- **TP3:** the Coboundary Hierarchy in type B has THREE layers, not just two: integer-λ (non-acyclic, bidegree mismatch), spin-λ (acyclic, bidegree match), crystal (forgets bidegree). This is the *type-B coboundary hierarchy*.

## Open

- Does Clio's framework extend to type B? Direct question to ask her.
- Is there a categorical formulation: a forgetful 2-functor whose fibre is the bigraded data?
- The "cactus" group in type B: does it factor through a (Z/2)^n extension of the type-A cactus?
