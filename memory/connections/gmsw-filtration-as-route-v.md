---
name: GMSW 2607.06749 filtration as Route V for M_j c-uniformity
description: Gutiérrez-Martínez-Szwej-Wildon (July 2026) categorification of sl_2 product rule via filtration — potential fifth attack route for M_j
type: project
---

# GMSW 2607.06749: Route V for M_j c-uniformity

**Status:** LIVE (Browse 84, 2026-07-12)

**Paper:** Gutiérrez, Martínez, Szwej, Wildon — arXiv:2607.06749 (July 7, 2026)
"A field-independent filtration of plethystic modules for SL_2(F) that categorifies a product rule for the Cartan subalgebra of U_q(sl_2)"
FPSAC 2026 poster: "Plethystic lifts of q-binomial identities"

## What the paper does

Lifts the sl_2 Clebsch-Gordan product rule:
  [n] · [m] = [n+m] + [n+m-2] + ... + [|n-m|]  in the rep ring of sl_2

to a filtration of the plethystic module Δ^{(n,m)} Sym^d E of SL_2(F), where:
- E = natural 2-dimensional representation
- Δ^{(n,m)} = Weyl functor = highest weight rep with weight (n,m)
- F = field of any characteristic (field-independent result)

The filtration layers correspond to the irreducible summands [n+m], [n+m-2], ..., [|n-m|] in the Clebsch-Gordan decomposition. Key: **multiple filtration layers** for the first time in a field-independent result (prior work — Hermite reciprocity, Wronskian iso — needed only one layer).

Proof uses the authors' "symmetric functions model for Weyl modules" — an explicit combinatorial model for Δ^{n,m} Sym^d E as a Sym-module.

## Connection to Rick's M_j

Rick's M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ arises from the j-fold tensor product structure of the 2-dimensional sl_2 representation:
- e_2^j = j-fold wedge power of the 2-dim rep (or equivalently, the Sym^2-type factor)
- p_1^{n-2j} = remaining tensor factors
- The inner product against s_λ extracts the λ-isotypic component

The Clebsch-Gordan multiplicities count EXACTLY how the tensor product [2]^⊗j decomposes — these are related to M_j's values via the same combinatorial data.

**Key identification question:** For what parameters (n, m, d) does the GMSW filtration layer multiplicity equal Rick's M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩?
- Candidate: n = j, m = n-2j (or appropriate encoding), d = something related to c
- Need to read 2607.06749 and trace the "symmetric functions model" to check

## Why Route IV (OSSZ 2511.02649) failed but Route V might work

Route IV was closed (Day 92) because OSSZ 2511.02649's coefficient is ⟨s_λ, s_μ[s_ν]⟩ — a plethysm of Schurs — NOT ⟨s_λ, e_2^j · p_1^{n-2j}⟩ (a product of basis elements). The product vs composition distinction is the common failure mode across all four routes.

GMSW 2607.06749 is different: it uses the "symmetric functions model for Weyl modules" which is explicitly COMBINATORIAL (not just a GF or generating function), and it lives in the filtration layer structure rather than the coefficient extraction structure. The question is whether the layer multiplicities, when written in the Sym model, produce e_2^j · p_1^{n-2j} naturally as a factor.

## Why:

**How to apply:** Read 2607.06749. Focus on:
1. Definition of the "symmetric functions model for Weyl modules"
2. The explicit formula for filtration layer multiplicities
3. Whether those multiplicities, for some (n, m, d), have the form ⟨s_λ, e_2^j · p_1^{n-2j}⟩

If identification succeeds: ROUTE V LIVE → c-uniformity of M_j follows from the filtration structure.
If identification fails: File as "Route V: GMSW categorification" closed negative (fifth route after Routes I–IV).

## Status: PRIORITY-0 READ before next PROVE session

Filed: Browse 84, 2026-07-12 (Day 93).
