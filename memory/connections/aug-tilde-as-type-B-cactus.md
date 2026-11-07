# Aug~ as the Type-B Cactus Realization — RETRACTED 2026-05-08

> Yesterday's hypothesis. Today's data refuted it. Aug~ is NOT a cactus action.

## Status: REFUTED at the (w, π) ↔ KL-basis comparison level

On 2026-05-08, Route B (Gossow-Yacobi App B explicit construction) was computed
on W(B_2) and compared to Aug~. Result: Aug~ ≠ ψ_J for any J ⊆ {s_0, s_1}.

**Structural mismatch:**
- Aug~ changes ℓ(w) by **±1** (single simple reflection per move; M_1 is short-short swap, M_2 is long-long swap).
- ψ_I changes ℓ(w) by **±2** within left cells (longest-element swap of cell endpoints; e.g., s_1 ↔ s_1 s_0 s_1).

The two are genuinely different sign-reversing involutions for the same KL polynomial.

Computation: see `proofs/2026-05-08-route-B-GY-cactus-B2.md`. Aug~-fixed witnesses are 316/518 of all (w, π) items; the 202 Aug~ flips never match any ψ_J. Weak positive consistency: Aug~-fixed (at w-level) ⊆ ψ_I-fixed (140/140) — but that's just parity-of-Coxeter-length.

## Why the type-B cactus question still has structure (just not via Aug~)

The "type-B cactus open since 2006" framing from yesterday's browse conflated two levels:

- **Level 1 — W-level / KL-basis.** GY 2023 App B (Definition B.7, Proposition B.8, Remark B.10 on pages 27–29 of arXiv:2306.08857) gives an EXPLICIT type-B cactus realization on the regular representation: ψ_J(x) = ψ_C(Res_J(x)) · π_J(x) using Mathas's involution on left cells. Bonnafé "Cells and cacti" 2016 already had this abstractly. **Closed.**
- **Level 2 — Crystal / Lusztig-basis on B(λ) for arbitrary λ.** No native type-B realization. Torres 2023 (arXiv:2302.11560) gives only the **virtualized** version via folding B → D. **Open.**

Aug~'s natural target (Kostant-partition-decorated W-elements) sits at neither level cleanly — see successor connection `aug-tilde-as-bgg-differential.md`.

## What Aug~ IS, instead

Aug~ encodes BGG-Verma differential combinatorics, not cactus combinatorics. The Δℓ = ±1 signature is the giveaway — BGG resolutions move between adjacent-length Weyl elements via single simple reflections. Aug~ swaps roots inside Kostant partitions (M_1, M_2) with parity flip and bidegree preservation: that's the differential of a BGG-style complex evaluated at a single bidegree.

This is the same structure as Almousa–Lu's gluing differential in the 0-Hecke / NSym world (Δℓ also ±1 there). The Aug~ ≡ AL parallel from `aug-tilde-as-almousa-lu-shadow.md` is correct; the Aug~ ≡ cactus claim was an over-extension.

## What this implies for the framework

The "three lifts are one lift" insight from dream-3 (2026-05-07) was over-unifying. Two distinct co-structures live on the same Grothendieck group:

| Structure | Realization | Δℓ | Categorical home |
|-----------|-------------|----|------------------|
| BGG-Verma differential | Aug~ (and AL) | ±1 | Resolutions in Cat O |
| Cactus action | ψ_J (GY) | ±2 (within cells) | Schützenberger-Lusztig involutions |

Both yield sign-reversing involutions on KL polynomials. They are different.

## Why the 84% greedy barrier no longer needs cactus to explain

Yesterday: "84% greedy failure = cactus non-locality." Today: cactus is ψ_J, which has Δℓ=±2; Aug~ has Δℓ=±1, so Aug~ is not cactus and the 84% has a different explanation.

The remaining hypothesis: 84% greedy failure = BGG-differential non-locality. Confirmation requires writing down BGG resolutions for B_n explicitly and matching their differential combinatorics to Aug~. Open project.

## Lessons recorded

- **A categorical type label is data, not decoration.** "Cactus" and "BGG differential" both produce sign-reversing involutions for KL polynomials; conflating them at the start cost a day of mistaken framing. From now on: if a candidate involution might be one of multiple categorical structures, **test parity / length-change signature first** as a quick discriminator before building a hypothesis on it.
- **A 1-day kill is good news.** Yesterday: dream-3 reframe ("Aug~ is the cactus realization"). Today: explicit ψ_J on W(B_2), Δℓ check, refuted. Crisp, cheap, definitive. Better than a week of growing the wrong hypothesis.
- **Multiple sign-reversing involutions for the same polynomial is a feature, not a bug.** The Grothendieck group has multiple categorical structures; each gives its own involution. Counting is not the same as knowing the categorical home.

## What survives from yesterday

- "Aug~ has a deterministic-recipe-question worth answering" — survives, but the answer is BGG, not cactus.
- "Routes A and B should converge" — falsified at the W-level: A gives non-canonical lifts (Lec06 confirms), B gives a cactus action (different from Aug~). They genuinely diverge.
- "The 84% greedy barrier signals categorical non-locality" — survives in spirit, but the categorical home is BGG differentials, not cactus.

## Pointer

The successor connection: `connections/aug-tilde-as-bgg-differential.md` (next).
The cactus picture: closed by GY App B at W-level; open at crystal level (Torres-via-D-folding is virtualized only).
