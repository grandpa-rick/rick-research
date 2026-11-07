# Bechtloff Weising 2506.07727 vs M_j — Tier-A Connection

**Date:** 2026-07-10 (Day 88)
**Status:** Read, understood, NOT a shortcut.

## The paper

Milo Bechtloff Weising, "Wreath Generalization of Littlewood Reciprocity"
(arXiv:2506.07727v2, Aug 2025, 10 pp).

Generalizes Littlewood's 1958 reciprocity formula for restricting a
GL_n(C) rep V^λ to the symmetric group S_n:

    dim Hom_{S_n}(S^μ, Res V^λ) = ⟨s_μ(Σ_k h_k), s_λ⟩

to the setting of restricting a GL_{nm}(C) rep to a wreath product
G^n ⋊ S_n embedded via an m-dim rep η: G → U(m). The main theorem 3.18:

    dim Hom_{G^n⋊S_n}(W_ρ, η^{(n)}_* Res V^λ)
      = ⟨Π_{γ∈G_*} s_{ρ(γ)}(Σ_μ dim Hom_G(γ, S_μ(η)) s_μ), s_λ⟩ .

Cyclic special case (Cor 3.19) for G = μ_m, η identity: recovers a
hyperoctahedral-style formula for restricting to (μ_m)^n ⋊ S_n.

## Why it isn't a shortcut for M_j

**M_j definition (Day 86 checked-sober).** For λ = (a, b, c),

    M_j(a, b, c) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩
                 = dim Hom_{S_n}(V^λ, Ind_{S_2^j × S_{n-2j}}^{S_n} (sgn^⊗j ⊠ triv))

The induced representation is from a **DIRECT PRODUCT** Young subgroup

    (S_2)^j × S_{n-2j}   ≤   S_n

with sgn on each of the j copies of S_2.

**BW's target.** BW's Theorem 3.18 (specialized G = Z/2, m = 2, η = sgn)
gives branching to the **WREATH PRODUCT**

    B_n = (Z/2)^n ⋊ S_n   ≤   GL_n(C)   [hyperoctahedral].

Reps of B_n are indexed by pairs of partitions (ρ_+, ρ_-) with
|ρ_+| + |ρ_-| = n — different combinatorial data than M_j's (λ, j).

**The gap.** (S_2)^j is NOT wreath-preserved by S_j — the wreath adds a
permutation of the j copies. In representation terms:

    Ind_{S_2^j × S_{n-2j}}^{S_n}(sgn ⊗ triv)
      = Ind_{(S_2 ≀ S_j) × S_{n-2j}}^{S_n} ⊕_β f^β · (W_{(∅, β)} ⊗ triv)

where β runs over partitions of j and W_{(∅, β)} is the wreath irrep with
"sgn slots" indexed by β. So M_j MIXES multiplicities of many wreath-labels,
weighted by dim S^β = f^β. BW gives the wreath-labeled multiplicities;
extracting M_j requires the additional aggregation.

Aggregation:

    M_j(λ) = Σ_β f^β · dim Hom_{S_2≀S_j × S_{n-2j}}(W_{(∅, β)} ⊗ triv,
                                                    Res^{S_n}_{(S_2≀S_j)×S_{n-2j}} V^λ)

The RHS is expressible via BW-style symbols but the sum over β doesn't
collapse to a single BW multiplicity.

## What BW does give us — Tier-A observations

1. **c-uniform Sym-side is generic.** BW's formula is c-uniform by
   construction (RHS involves only h_k plethysms, no c-specific constants).
   Same phenomenon we see for M_j: c-uniformity of Sym-function multiplicities
   is a NATURAL feature of the plethystic branching framework, not a
   coincidence specific to our M_j. Rick's intuition confirmed.

2. **The pattern generalises.** BW's Theorem 3.18 is a CLASS of Sym-function
   identities where "one side is a specific plethystic exponential and the
   other is a Schur pairing." This is EXACTLY the shape of Day 86's
   Sym-side identity for M_j. Different subgroup lattice (wreath vs Young),
   same conceptual structure.

3. **Possible cousin construction.** If we replace the Young subgroup
   S_2^j × S_{n-2j} with the wreath (S_2 ≀ S_j) × S_{n-2j}, and the sgn
   twist with the trivial rep, we get a QUOTIENT of M_j. Whether that
   quotient is easier to handle via BW is a separate question — hasn't
   been checked.

## Filing

- No proof step depends on BW.
- BW-derived facts about wreath multiplicities may appear in future
  connection files if we open a "wreath cousin of M_j" line of attack.
- Extraction level: **deep-read** (all 10 pages of the paper read in
  Day 88 prove cycle). Registered in `memory/reading/sources.json` at
  that level.
