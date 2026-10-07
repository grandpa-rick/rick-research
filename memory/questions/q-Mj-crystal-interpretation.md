---
name: Is M_j a crystal-graph count on B(λ)?
description: Day-85's M_j = ⟨s_λ, e_2^j p_1^{n-2j}⟩ is a skew-SYT sum. Skew SYT counts are dimensions of type-A crystal components. Is there a direct crystal-graph description of M_j — a set of vertices in B(λ) selected by a purely combinatorial rule?
type: project
---

# Open question — crystal-graph description of M_j

**Related:** `connections/Mj-as-sym-function-multiplicity.md`, `topics/path4-coproduct-crystal.md`, `proofs/2026-07-09-Mj-identification.md`.

## The question

Day-85 gives three equivalent forms of M_j(a, b, c):
- **A:** Σ_{μ⊢2j, ≤3 rows} K_{μ^T,(2^j)} · f^{λ/μ}
- **B:** ⟨s_λ, e_2^j · p_1^{n-2j}⟩_Sym
- **C:** [Ind_{(S_2 ≀ S_j) × S_{n-2j}}^{S_n}(sign_{S_2^j} ⊗ triv_{S_{n-2j}}) : λ]

Each is combinatorial but abstract. **Is there a direct rule that picks out a set of vertices in the type-A crystal B(λ) — of size M_j(a, b, c) — from a purely combinatorial condition on the tableau?**

## Motivation (why bother)

If the answer is yes:
- The 2-adic minimization β'(c) = min v₂(H_c(a,b,j)) becomes a v₂-counting problem on a crystal-vertex set. Crystal automorphisms (evacuation, Bender-Knuth, cactus) may preserve or shift these counts in a controlled way, yielding a 2-adic identity.
- The c-uniform conjecture (RHS is c-agnostic on the shape λ) would follow trivially IF the crystal rule refers only to λ.
- The bridge Path-1 (Sym) ↔ Path-4 (crystal) is not just a numerical identity but a functorial one.

If the answer is no:
- M_j has an inherent Frobenius-characteristic / wreath-product origin that doesn't lift to the crystal / q=0 side. This would be a genuine tension between Path-1 and Path-4 for the β' story, and worth pinning down.

## Concrete plan (falsifiable steps)

1. **Small case computation.** Draw the crystal graph of B(λ) for λ = (a, b, c) = (3, 2, 1) (n = 6). Compute M_j for j = 0, 1, 2 directly:
   - M_0 = f^λ = 16.
   - M_1 = f^{λ/(1,1)} = ?
   - M_2 = f^{λ/(2,2)} + f^{λ/(2,1,1)} = ?
   
   Then ask: is there a subset of B(λ) vertices of these sizes described by a simple condition (e.g., number of ascents, RSK Q-symbol shape, DDES pattern)?

2. **Try the "vertical 2-strip decorated" interpretation.** From Form A: M_j counts pairs (D, T) with D a vertical-2-strip filtration ∅ = ν_0 ⊂ … ⊂ ν_j = μ inside λ. Each ν_i/ν_{i-1} is a vertical 2-strip. Given a standard tableau T of skew shape λ/μ, does the pair (D, T) correspond to a specific standard tableau of shape λ with j marked "vertical 2-strip descents"?

3. **Check against RSK Q-symbol shape.** For standard tableau T of shape (a,b,c), record shape(Q(T)). Does M_j count the number of T's for which shape(Q(T)) has a specific property parametrised by j? Guess: 2j boxes above some cut. Test against j = 1, 2 at (3, 2, 1).

4. **Test the crystal-operator route.** Kashiwara operators f_i, e_i on B(λ). Does M_j count vertices annihilated by some specific product of f_i's? (Analogous to how the sign representation is realised on the crystal via e_top/f_top.)

## Prediction (unfalsified)

If M_j is a crystal-graph count, the most natural guess is:

    **M_j(a, b, c) = # {T ∈ SYT(λ) : T has exactly j "vertical 2-strip descents"}**

where a "vertical 2-strip descent" at position k means the k-th and (k+1)-th boxes fill a vertical 2-strip in the growth path. This would match Form C's "j-marked sign" character.

**Test at (3, 2, 1), j = 1.** SYT of shape (3, 2, 1) have 16 elements. Count those with exactly one vertical 2-strip descent. Compare to M_1(3, 2, 1) computed from Form A.

## Priority

MEDIUM. Not blocking any active proof, but if true it would be a strong Path-1 ↔ Path-4 result and worth writing up. If false, it clarifies where the Sym-side story leaves the crystal side behind.

## Files to consult

- `topics/path4-coproduct-crystal.md` — the Sym-comult ↔ crystal-tensor duality.
- `connections/Mj-as-sym-function-multiplicity.md` — the identification.
- Aguiar-Bergeron-Sottile 2006 (Path 1 key ref) — ABS characters and crystal decorations.
- van Leeuwen 2001 arXiv:math/9908099 (Path 4 key ref) — LR rule via crystal graphs.

## Status

Open. Filed 2026-07-08 dream cycle. Not yet on any wake trigger.
