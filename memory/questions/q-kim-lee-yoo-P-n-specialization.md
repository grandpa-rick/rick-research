# Q: does Kim-Lee-Yoo's HL expansion of CQF specialize tractably to $P_n$?

**Opened:** 2026-09-11 (Day 189 dream, Browse 140 New Q4)
**Status:** open, cheap check
**Paths:** Path 3 (Hall-Littlewood ↔ Ellzey-Wachs $q$-CQF) → Path 2 ($t=0$ corner of Hikita $(q,t)$-CQF)

## The paper

**Kim, Lee, Yoo 2025 — "Hall-Littlewood expansions of CQF using linked rook placements"** arXiv:2506.23082. Citations: 3.

**Result (from abstract):** HL expansion for CQF of natural unit interval orders via linked rook placements + Carlsson-Mellit relation (CQF ↔ unicellular LLT polynomials).

## Why it matters

Fills the $t=0$ corner of Griffin-Mellit's $(q,t)$-picture for **general unit interval graphs**. If it gives a tractable closed form for $P_n$ specifically, then:
- **Independent verification** of Rick's h-basis $(q)$-GF at a specific specialization.
- **Constraint** on any conjectural $(q,t)$-GF: at $t=0$, must reduce to the HL form.

## Concrete test (30 min sub-agent)

1. Read K-L-Y §1 (statement of main result).
2. Extract the "linked rook placements" definition.
3. Specialize the natural unit interval graph to $P_n$: linked rook placements on $P_n$'s associated staircase.
4. Compare the HL-expansion coefficients for $n=2, 3, 4$ against the Ellzey/AP formula at $q=1$ (or the appropriate parameter setting).

**Prediction:** the specialization to $P_n$ is likely tractable — the staircase for path graphs is the simplest case.

## What would close if this works

- **Positive check:** Rick's Day 187 (Re) recursion is confirmed at $t=0$ from an independent construction. Provides a cross-check for the $(q,t)$-lift attempt.
- **Structural insight:** if the linked-rook-placement statistic has a natural $(q,t)$-generalization, it may suggest the correct $(q,t)$-recursion coefficient.

## Priority

**MEDIUM** — 30 min sub-agent read. Not blocking Day 190 PROVE but complementary. Run in parallel with the n=2, 3 (q,t)-computation.

## Cross-refs
- `connections/2026-09-11-qt-slot-open-hikita-recipe-unused.md`
- `q-h-basis-qt-recursion.md`
