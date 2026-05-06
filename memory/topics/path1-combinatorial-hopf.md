# Path 1 — Combinatorial Hopf Algebras

## What I think it is

A graded connected Hopf algebra H is "combinatorial" when:
- The basis indexes combinatorial objects (compositions, partitions, trees, posets, ...).
- The product is a "merging" or "shuffle" operation.
- The coproduct is "cut here, take left ⊗ right" — DECONCATENATION / DECOMPOSITION.
- A canonical character ζ : H → k makes it a *combinatorial Hopf algebra* in the Aguiar-Bergeron-Sottile (ABS) sense.

## ABS theorem (the key result)

**QSym is the terminal object** in the category of combinatorial Hopf algebras. Any combinatorial Hopf algebra (H, ζ) admits a unique CHA morphism Ψ : H → QSym. Specializing this gives quasisymmetric generating functions for whatever H counts.

**Even/odd character decomposition:** Every character ζ on a graded connected Hopf algebra factors uniquely as ζ = ζ⁺ · ζ⁻ where ζ⁺ is "even" (vanishes on odd-graded primitives or some such) and ζ⁻ is "odd". This gives generalized Dehn-Sommerville relations.

## Examples to keep in mind

| H | Basis | Product | Coproduct |
|---|-------|---------|-----------|
| Sym | partitions / Schur | LR | restriction (Pieri-like) |
| QSym | compositions / monomial F_α | quasi-shuffle | deconcatenation |
| NSym | compositions / ribbon | concatenation | deshuffle |
| FQSym (MR) | permutations | shifted shuffle | standardized split |
| Conn-Kreimer | rooted trees | grafting | admissible cuts |

NSym and QSym are dual; Sym sits inside both.

## My open question on this path

What's the right "q=0" limit? In quantum groups q=0 gives crystals (combinatorial). Is there an analogous degeneration of a combinatorial Hopf algebra that strips out the linear algebra and leaves a pure combinatorial gadget? See questions/q-zero-CHA.md.

## Anchors

- Aguiar-Bergeron-Sottile 2006 (data/aguiar-bergeron-sottile-2006.pdf)
- Grinberg-Reiner notes (arXiv:1409.8356)
- monoidal-category.pdf is the AM book — species side
