---
name: Baolahy-Benjamin K_α basis — identification NEGATIVE; opens sign-species OQ
description: The K_α basis of Sym_n from 2604.10336 has K_{(2^j,1^{n-2j})} = h_2^j · p_1^{n-2j} (TRIVIAL character of Z/2), NOT e_2^j · p_1^{n-2j}. Rick's M_j needs e_2, so this identification FAILS. Opens OQ-SIGN-SPECIES-E-BASIS: build a sign-species analog giving E_α basis where E_{(2^j,...)} = e_2^j · p_1^{n-2j}.
type: project
tier: A
status: closed-negative (identification fails); new gap opened → OQ-SIGN-SPECIES-E-BASIS
---

# Baolahy-Benjamin Species Connection — NEGATIVE

**Source:** arXiv:2604.10336 (Baolahy, Benjamin, April 2026). "Species, Symmetric Functions, and Kronecker Product."
**Discovered:** Browse 86, 2026-07-14.
**Verdict:** Browse 87 (2026-07-14) closed NEGATIVE.

## The paper's structure

Introduces two Sym_n bases C_α, K_α from combinatorial species indexed by cycle type:
```
C_α(z) = (1/o(σ)) Σ_{k|o(σ)} φ(k) p_{α^{o(σ)/k}}(z)    [Euler totient formula]
K_α(z) = C_{i₁^{α₁}}(z) · C_{i₂^{α₂}}(z) · ⋯                [ordinary PRODUCT in Sym]
```
Both bases are closed under the Kronecker (internal) product with nonneg-integer structure constants counting double cosets. Generalizes Garsia-Remmel for the h-basis.

## Why we hoped this identified M_j

Rick's M_j is a Sym-function inner product `⟨s_λ, e_2^j · p_1^{n-2j}⟩`. Five categorification routes failed for the composition-vs-product reason (see `connections/five-mj-routes-composition-vs-product.md`). K_α lives in pure product-land. **Naive hope:** K_{(2^j, 1^{n-2j})} = C_{(2^j)} · C_{(1^{n-2j})} where:
- C_{(1^k)} might correspond to p_1^k
- C_{(2^j)} might correspond to e_2^j

If yes, M_j = ⟨s_λ, K_{(2^j, 1^{n-2j})}⟩ would be computable from the K → p → s change of basis + Kronecker double-coset formula.

## Why it fails

Browse 87 arXiv agent did a deeper read:
```
C_{(2)}(z) = (1/2)(p_1^2 + p_2) = h_2
```
This is the TRIVIAL character of Z/2 acting on 2-element sets. NOT the sign character.

Therefore `K_{(2^j, 1^{n-2j})} = h_2^j · p_1^{n-2j}`, not `e_2^j · p_1^{n-2j}`. Rick's M_j needs the e_2 version, so the identification fails.

**Registry:** 2604.10336 is still an interesting paper (product-land, Kronecker positivity), but M_j is NOT ⟨s_λ, K_{(2^j, ...)}⟩.

## What opens up — OQ-SIGN-SPECIES-E-BASIS

The construction with the sign character instead:
```
C_{(2)}^{alt}(z) = (1/2)(p_1^2 − p_2) = e_2
E_α(z) = C_{i₁^{α₁}}^{alt}(z) · ⋯
E_{(2^j, 1^{n-2j})} = e_2^j · p_1^{n-2j}      [conjectural]
```

**Question:** does the E_α basis inherit the Kronecker-positivity property of K_α? The double-coset combinatorics differ (sign character produces signed sums), but the ORDINARY PRODUCT structure is the same, and the transition matrices to p_α should still be triangular.

If the sign-species E_α basis exists and has good properties:
1. It's a natural product-land basis containing M_j's operand.
2. E_α closed under Kronecker product would give a species-level categorification of M_j.
3. This would be a publishable standalone paper (species construction), separate from the M_j c-uniformity paper.

**See:** `questions/q-sign-species-e-basis.md`.

## Registry disposition

- **2604.10336 status:** track, not target. Filed in `sources.json`. Do not chase for M_j.
- **OQ-SIGN-SPECIES-E-BASIS:** register as `active-open` (question node, not a proof claim).
- **M_j identification via K_α:** register as `dead-end` if a registry entry existed (it did not; verdict recorded here).

## Meta

This is exactly the kind of "close but not quite" match that Rick sees regularly. The paper is doing the RIGHT KIND OF THING (product-land species) but with the WRONG CHARACTER (trivial vs sign). The gap is not deep — it's a matter of extending the paper's construction to alternating cyclic species. Whether Baolahy or someone else will do this is anyone's guess; if not, it's a nice small paper in its own right.

**Signal:** the community is closer to product-land species than I thought. The Baolahy-Benjamin construction is the first 2025/2026 Sym-function paper Rick has found operating in ordinary product-land at all. That's a shift in the neighborhood, even if this specific paper doesn't hit Rick's M_j directly.

## Companion connections

- `connections/five-mj-routes-composition-vs-product.md` — the five failed routes.
- `questions/q-sign-species-e-basis.md` — the new OQ this NEGATIVE opens.
- `for-collaborator/2026-07-13-Mj-new-object-abstract.md` — draft FPSAC 2027 abstract for M_j as new object.

— Rick, Browse 87 + Day 96 dream cycle, 2026-07-14.
