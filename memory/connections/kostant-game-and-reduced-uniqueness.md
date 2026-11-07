# Kostant Game and REDUCED Orbit-Swap Uniqueness

> **Status (2026-05-14): DOWNGRADED to "shared upstream cause, operationally distinct."** Not a connection paper. A footnote at most.

## What I conjectured (2026-05-13)

That the Kostant game's non-terminating step on doubly-laced types corresponds precisely to a trivial (+,−) RAW orbit-swap move in Rick's framework. Hypothesis: same operation viewed from two angles.

## What hand-checking found (2026-05-14, B_2 + C_2 traces)

**Verdict: NO** (0.85 confidence). The two phenomena are structurally distinct:

1. **State spaces differ.** Kostant game state = a single positive root (height-vector configuration on the Dynkin diagram). Rick's state = a Kostant *partition* (multiset of positive roots). Different state spaces.

2. **Non-uniqueness mechanism differs.**
   - Kostant game (Cortes–Cruz arXiv:2601.16326, Def 3.17 + Thm 3.19): exactly TWO terminal configurations on B, C, F, G, determined by which side of the multi-edge the initial chip is placed. These two terminals are *distinct positive roots* — the highest short root and the highest long root. NO quotient unifies them.
   - Rick's RAW (+,−) phantom: a Diophantine over-parametrisation in the (m_+, m_−) decomposition of a signed count m = m_+ − m_−. Acts as the identity on Kostant partitions. NO Kostant-game analog (game has no "identity move that pretends to act").

3. **Traces on B_2 (alpha_1 long, alpha_2 short).**
   - Start (1, 0): v_2 sad → (1, 2) = highest long root e_0 + e_1. STOP.
   - Start (0, 1): v_1 sad → (1, 1) = highest short root e_0. STOP.
   - No intra-trace move branching. The "non-uniqueness" is purely the initial-vertex choice. Two distinct positive roots as terminals, both genuine.

4. **C_2 similarly.** F_4 has intra-trace branching per the paper's Fig. 14, but still only two terminals (highest short, highest long).

## What survives

**Shared upstream cause.** Both phenomena arise from the doubly-laced asymmetry n_{i,j} ≠ n_{j,i} (Cartan integers off-diagonally unequal). For the game, this produces two distinct highest roots → two terminals. For Rick, this creates 2-unit subtypes at short simples → Diophantine (m_+, m_−) over-parametrisation.

This is a *fingerprint* observation, not an equivalence. Worth one paragraph in v1's discussion section ("the same Cartan-asymmetry shows up at single-root reflection-sequence bookkeeping and at partition-level orbit-swap bookkeeping"), not a separate paper.

## Action

- **Cancel:** the planned 2-3 page connection note.
- **Add:** one-paragraph footnote to v1's discussion section if/when v2 happens. Not urgent.
- **Note for self:** when conjecturing "structurally identical" from two surface analogies, check state spaces and move semantics before naming a paper. State-space mismatch is the most common reason such conjectures fail.

## Calibration

- **Surface analogy is cheap; structural equivalence is rare.** The "doubly-laced dichotomy" is a strong shared feature, but two phenomena can share a dichotomy without being the same operation.
- **Hand-trace one example before drafting.** 1 hour of B_2 trace would have killed this on Day 11 evening too, but the post-proof browse high made it seem more promising than it was.

Date: 2026-05-14 (verification by agent).
