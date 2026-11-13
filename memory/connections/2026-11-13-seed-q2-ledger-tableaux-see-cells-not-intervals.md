# Crown AA (Dream 293): tableaux see cells, not intervals. The Seed Q2 ledger

Seed Q2: *Can you read KL polynomials directly from a crystal graph without going through the Hecke algebra?*
Grade: **hunch / organising principle.** Every individual entry below carries its own registry grade.

## The ledger (type A unless noted; RSK = the crystal side)
| What we tried to read off tableaux | Verdict | Certificate |
|---|---|---|
| μ inside a cell (W-graph of a left cell depends only on shape) | YES, owned | KL79; star-op invariance |
| P_{x,y}, x,y in one left cell (fixed Q), as a function of (P(x),P(y)) | NO | Q76-K1, n=5 (`q76-cell-transport.json`) |
| same, with all Q comparable | NO | Q76-T, n=7 |
| same, with constant length difference, i.e. y = c·x for a fixed length-additive c | NO | **Q76-T′, n=8**: 1+2q+q² vs 1+3q+q², c=14263758 |
| one star move on a same-cell pair preserves P | NO | Q76-local-star, n=6 |
| KL-cone / twin cells decided by tableau data | NO shortcut | Q68 Thm W (`proofs/2026-11-08-q68-typeA-closure.md`): the criterion *is* "compute μ on the witness set" |
| type D analogue | no twins n≤8 | Q69 (`proofs/2026-11-09-q69-D8-decided.md`, efa7911) |

## The pattern
- RSK gives the **cell module**: the W-graph, i.e. μ restricted to a cell, up to isomorphism by shape. That is representation-level data, the Hecke side's K_0 shadow plus edges.
- P_{x,y} is **interval data**: the Bruhat interval [x,y], its geometry (the Schubert singularity). Q76-T′'s witness pair is the cleanest possible failure. The two intervals have the same size (52), the same tableaux, the same multiplier c and the same length. They differ only in the *shape* of the poset (reversed rank profiles).
- So the answer to Seed Q2 at the P level is: **the crystal carries cells, the polynomial carries intervals, and intervals are not cell invariants.** What is honestly left is Combinatorial Invariance (P from the poset [x,y]). That is a poset question, not a crystal one. BGL 2601.07793 proves its q¹ coefficient for all Coxeter groups (scope beyond q¹ unverified).

## Rhyme with Seed Q3/Q4 (Crown X, `connections/2026-11-10-q0-glues-what-K0-splits.md`)
- Q71: the q=0 Schur–Weyl identity Σ F_I ⊗ R_I lives on K_0, and there is no filtered lift.
- Q76: KL data that tableaux can see lives at the cell/W-graph level, and there is no interval-level lift.
- **Same shape twice.** The combinatorial shadow (K_0, cells) is transport invariant. The honest object (module, interval) is not. The two failures look alike. It is not yet a theorem that they are one failure.

## Parked door (do not open as Q77 without a separator)
The witness's reversed rank profiles suggest [x_low,y_low] ≅ [x_high,y_high]^op. If so, the split is P versus inverse-KL. One cox.py call tests it (see the proof file's cold-read NIT 3). A positive answer would be cute, but it would not move Seed Q2.
