# Marberg + Scrimshaw, "Square root crystals and the square root of B(∞)"
## arXiv 2608.11009 (posted 2026-08-11, 54pp)

**Read:** 2026-08-13 — abstract + introduction + section index via arXiv HTML.

## One-sentence summary

They introduce a monoidal category of "N-root crystals" (crystals whose ε, φ statistics take values in (1/N)ℤ), specialise to *square root* gl_n-crystals (N_i = 2), and construct a square-root analog of the direct limit crystal B(∞), giving it a marginally-large-tableau model, a Lusztig/PBW parameterisation, a Nakashima–Zelevinsky polyhedral model, a simple product character formula, and a nontrivial Demazure filtration.

## What "square root" means here

Categorical / combinatorial: the Kashiwara operators f_i, e_i are split into "half-steps", so ε_i, φ_i live in (1/2)ℤ rather than ℤ. It is **not** a 1/2 power of the monoidal product, **not** a square root of a linear operator, **not** a categorification move. The "square root of B(∞)" is a specific object SetTab_n(∞) in this new N=2 category.

Character formula (1.1):
    ch(SetTab_n(∞)) = ∏_{i<j} (1 + β x_j) / (1 - x_j x_i^{-1})

Related to Yu's semistandard *set-valued* tableau crystals after taking appropriate tensor products.

## Main theorems (Section 1.3)

- Thm 3.31 — SetTab_n(∞) exists as direct limit of weight-shifted sqrt-crystals.
- Thm 3.33 — nontrivial Demazure filtration.
- Thm 4.7  — Lusztig/PBW-type vector parameterisation.
- Thm 4.18 — polyhedral model via looped path crystals.
- Thm 4.23 — Kashiwara-type embedding.

## Cross-check against Rick's Path 4 program

| Feature Rick cares about | In this paper? |
|---|---|
| "crystal skeleton" construction (Sk) | **No mention** |
| ref to Brauner-Daugherty-Mason-Schilling 2607.12232 | **Not cited** |
| ref to Braun-Nevin-Rey 2503.14782 | **Not cited** |
| Sym coproduct on characters | Not discussed |
| Hopf-morphism / coalgebra morphism of char map | Not discussed |
| LR rule from crystals via Hopf morphism | Not discussed |
| The functor K_0 : Fund(sl_n-Crys) → Sym | Not discussed |
| Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2) | **Not proven, not stated** |

The only character statement is the classical multiplicative one:
    ch(B ⊗ C) = ch(B) · ch(C)
proven for regular crystals with well-defined character (Prop 2.14) — this is the standard product-on-characters, not a Sym coproduct / □ statement.

## Assessment

The paper lives in an adjacent but disjoint corner of crystal theory: it enlarges the category of crystals (introducing fractional Kashiwara operators) and reworks the B(∞) machinery inside that enlargement. It does **not** touch the crystal skeleton construction, does **not** discuss Sym's Hopf structure, and does **not** address any Hopf-morphism / □-coproduct question.

## Scoop-risk verdict: LOW

Orthogonal. The paper does not preempt any theorem in Rick's Path 4 target. It could in principle *complement* the program later (one could ask what Sk does on sqrt crystals), but as written it neither states nor implies the Sk(B_1 ⊗ B_2) = Sk(B_1) □ Sk(B_2) result nor any equivalent Hopf-morphism statement.
