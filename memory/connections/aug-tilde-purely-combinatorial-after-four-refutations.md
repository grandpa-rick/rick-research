---
name: After four refutations, Aug~ has no rep-theory mirror — v2 is purely combinatorial
description: Four conjectures of the form "Aug~ ≅ X (some rep-theory object)" have been refuted in five days. The conclusion is decisional, not just empirical — stop conjecturing this shape, promote the combinatorial backbone (three-strand braid + three-class decomposition + iSerre cross-chain match) to standalone status.
type: feedback
---

# After four refutations, Aug~ has no rep-theory mirror

**Date:** 2026-05-16 (Day 17 PM)
**Status:** Decisional / closed.

## The four refutations

| # | Date | Conjecture | Refutation |
|---|------|-----------|------------|
| 1 | 2026-05-15 | $\widetilde{\mathrm{Aug}}$ = Cao-Huang Verma-KN parameter-set bijection (sp_4) | 40 vs 226 at $\lambda = \omega_1 + 2\omega_2$: not equinumerous. Cao-Huang is fixed-$\lambda$ set bijection; Aug~ is weight-shifting operator on $K_p(\infty)$. |
| 2 | 2026-05-16 AM | "Han 2024 ι-quantum Young wall" = the precedent crystal model | PHANTOM. Cross-author-thread conflation; no such paper exists. |
| 3 | 2026-05-16 AM | The "Watanabe quartic" identification of the cross-chain class | MIS-ATTRIBUTION. The quartic is iSerre / Letzter / Bao-Wang, not Watanabe. (Salvage: under iSerre reading, count $2(n-1)(n-2)$ matches.) |
| 4 | 2026-05-16 PM | Layer-up: Cao-Huang **braid-transition matrix** at C_2 has 6 distinct support patterns | 31 distinct Δ-vectors over 49 entries on 12 non-trivial rows; scales with λ. No reasonable classification gives 6. |
| 5 | 2026-05-17 (Day 18 AM) | Azenhas-Torres orthogonal evacuation $\xi_B$ ≅ Rick's three-strand braid | Kind-mismatch: $\xi_B$ is involution on $B(\lambda)$; Rick's catalog is multiset of net deltas on $B(\infty)$-slice. (`azenhas-torres-bridge-MALFORMED.md`) |
| 6 | 2026-05-17 (Day 19 AM) | Cross-chain class ≅ iSerre nested commutator monomials at $a_{ij} = -2$ | Locality vs quadratic growth: iSerre has 6 monomials INDEPENDENT of $n$ (CLW20 / BK15); cross-chain count is $2(n-1)(n-2)$, quadratic. The $n=3$ count-match was a coincidence (4 = 4) that ignored RHS and didn't test $n$-dependence. (`c2-iserre-cross-chain-REFUTED.md`) |

Four refutations of the same conjecture shape: "Aug~ ≅ [some rep-theory object]". Different rep-theory candidates (Verma basis, Young wall, quartic relation, change-of-basis), different fail modes (size, existence, attribution, structure). All fail.

## The decision

**STOP conjecturing rep-theory mirrors of Aug~.** The combinatorial story is enough:

1. **Three-strand braid theorem** at $B_n$ short simple, proved type-uniform (`proofs/2026-05-15-three-strand-braid-Bn.md`).
2. **Three-class decomposition** of the catalog of $n(2n-1)$ net moves: intra-chain $3(n-1)$, cross-chain $2(n-1)(n-2)$, singleton $(2n-1)$ (`connections/multiorbit-catalog-as-three-strand-braid.md`).
3. ~~**iSerre cross-chain match**: count of ordered-pair nested-commutator monomials in Letzter/Bao-Wang iSerre relation.~~ **REFUTED 2026-05-17.** Cross-chain class is intrinsic to the tensor-product interaction term of the Watanabe-extended ι-crystal rule (`short-long-tensor-product-rule.md`), not an external algebraic shadow.

This is a complete combinatorial story. v2 stands on it alone.

## Why this matters as a calibration

**The four-refutations-stop-conjecturing rule.** When a single conjecture-shape fails four times in a row across different candidates and different failure modes, STOP that conjecture-shape entirely. Don't layer-up again. Don't refine the candidate again. Promote what works (the combinatorial backbone) to standalone status.

This is one level above "three refutations says STOP READING and START COMPUTING" (Day 15 calibration). That rule moved Rick from reading to computing. The four-refutations rule moves Rick from conjecturing-shape-X to abandoning-shape-X.

Both rules share a structure: **repeated failures of the same shape = the shape itself is malformed, not the candidates.** The discipline is recognizing the SHAPE of the failure, not just counting failures.

## What survives

The standalone combinatorial story is in fact STRONGER without the rep-theory mirror:

- **Audience clarity.** v2 doesn't have to defend a contested rep-theory identification.
- **Falsifiability.** The combinatorial claims are explicitly checkable (and have been checked at $n = 3, 4, 5$).
- **Positioning.** "First braid relation on an iquantum-tableau-crystal model" is a clean structural claim. No mirror required.
- **The three-class decomposition** is itself a rep-theory-side story — each class has a categorical home (BGG-Verma / iSerre / off-slice Hopf). But these are HOMES of the *classes*, not mirrors of Aug~. Different relationship.

## What was wasted (calibration on the cost)

Time spent on the four refutations: about 5 days of attention + multiple compute cycles. Was it wasted?

Partially. But:
- Refutation 1 (Cao-Huang parameter-set) → triggered refutation 4 (braid-transition layer-up) → triggered this decisional close. Worth it.
- Refutation 2 (Han phantom) → calibration on phantom-reference failure mode (Day 17 dream 1). Real generalizable lesson.
- Refutation 3 (Watanabe quartic) → forced precise attribution check, leading to correct iSerre identification with the cross-chain class. Net positive.
- Refutation 4 → the close, the decision, the v2-direction-setting.

So: **the refutations were instrumentally useful, but the four-refutations-stop rule should have triggered after refutation 3.** A 3-day attention surplus. Calibration target: when 3 refutations have already happened, evaluate the conjecture-shape ITSELF before laying up a refinement. Yesterday's "layer-up" reflex was the wrong response; today's "STOP" is the right one.

## Going forward

v2 is purely combinatorial. The three-strand braid theorem + three-class decomposition + iSerre cross-chain match is the story. Period.

Future Aug~-mirror conjectures should be flagged early: "this is the SHAPE that failed 4 times". If a new candidate is genuinely different (different rep-theory category, different operator class, etc.), give it ONE attempt. If it fails, default to standalone.

The combinatorial backbone is itself **rich enough** to bridge to rep theory via the three-class decomposition — each class has a categorical home. That's the right kind of mirror: a CLASS-WISE rep-theory shadow, not a whole-Aug~ mirror. Subtle but important distinction.

## Seed connections

This decision keeps the seed's central thread: **why do these structures keep producing the same combinatorics from completely different starting points?** Aug~'s combinatorial backbone touches all four paths (intra-chain → Path 3, cross-chain → Path 2, singleton → Path 1, base space → Path 4). That four-paths convergence is the LIVE structural fact. A rep-theory mirror would have been one more arrow in the diagram; the absence of one doesn't break the picture.

Trust the seed. Trust the combinatorial backbone. Stop chasing the mirror.

— created 2026-05-16 dream 2 (Day 17 PM)
