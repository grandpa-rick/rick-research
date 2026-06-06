---
name: Azenhas–BDI bridge verdict — NEGATIVE
description: P_PARK #5 (Azenhas 2603.16698 ↔ BDI Theorems F+G) does NOT lift to a polytope-facet bijection. The bridge breaks at facet count and at dimension. Coarse forgetful map AII → BDI may exist but is not pursued. Recommend NOT load-bearing in v4.
type: project
date: 2026-06-06
status: NEGATIVE RESULT — characterized precisely
---

# Azenhas–BDI bridge — Robin, the answer is NO

Robin —

Spent today's deep-work session on P_PARK #5, the Azenhas–BDI bridge. **The
bridge does not work as a polytope-facet identification.** The "asymmetric
mirror" framing in PROVE.md was too optimistic. Here's what's actually true.

## Headlines

1. **Facet counts don't match.** BDI: $2n - 3$ non-redundant facets (Theorem F).
   Azenhas (Theorem 6, n odd): $n + 1$ inequalities. Azenhas (Theorem 7, n
   even): $n - 1$ inequalities + 1 equality. Asymptotically, BDI has slope 2
   in $n$, Azenhas slope 1. No bijection.

2. **Dimensions don't match.** At $n = 2$: BDI ambient $\dim = 3$ (after
   $M_1 = 0$). Azenhas ambient $\dim = 4$ (after eliminating $m_{14}$ via
   the linking equality). Already at the smallest case the polytopes live
   in different-dimensional spaces.

3. **Computational verification.** Enumerated lattice points at $n = 2$,
   total weight $\le N$: counts agree through $N = 3$ (1, 2, 5, 9) by
   small-weight degeneracy, then diverge sharply at $N = 4$ (BDI: 15,
   Azenhas: 16) and grow apart.

4. **Mechanism of failure.** This is *exactly* the
   rank-3-chain-factor-vs-rank-1-strip distinction I named in v3 Remark
   3.5 (`Asymmetric mirror`). I wrote that remark thinking about BDI's
   own forward-vs-reverse descent, but the same mechanism kills the
   AII-BDI bridge: AII has *signed slack data* $(t_0, r)$ — finer than
   BDI's *unsigned* carry-bit $\{0, +2\}$. The Azenhas inequalities use
   the finer data; BDI cannot encode it.

## What's structurally real

Both systems are instances of the **same bracket-scan template**:

> (level-$i$ mid-count) $\le$ (cumulative previous-level data).

This is Watanabe's framework. Both instantiate it. The template match is
genuine and worth a *single remark* in v4. But the *algebraic content* of
"cumulative previous" differs:
- BDI: scalar carry $P_a = \sum 2(B_b - T_b)$.
- AII: distinct prefix-column multiplicities $m_{u_1 \cdots u_{i-1}}$.

So the inequalities have the *same shape* but live in *different lattices*.

## What's left open

A *coarse* forgetful map AII → BDI may exist by integrating out signed
slack data. This would be:
- AII configuration → (partition by total slack)
- For each slack class, get a single BDI inequality.

I haven't constructed this. It's not a mirror (one-way only), and the BDI
side already has its own complete proof, so the map adds nothing
load-bearing.

The reverse direction BDI → AII would require *lifting* unsigned to signed
data, which is non-canonical (no preferred choice of slack pattern given
just $(B, T)$).

## Recommendation for v4

- **Do not** pursue this bridge as a v4 result. Cited papers (Azenhas 2603,
  Azenhas 2604) are correct *parallel* type-AII instantiations of the
  same Watanabe template — but not isomorphic to the BDI side.
- Single remark in v4 introduction: "Azenhas's type-AII recording-tableau
  characterization \cite{Azenhas2603} provides a parallel instantiation
  of the bracket-scan template; her signed slack data refines our
  unsigned chain-factor carry, so the two systems do not admit a
  facet-to-facet identification (see Remark~\ref{rmk:asymmetric-mirror})."
- P_PARK #5 → CLOSED as negative. Mark as such in SUMMARY/topics so
  future-Rick doesn't redo this work.

## Where the proof lives

`/home/agent/projects/proofs/2026-06-06-azenhas-bdi-bridge.md` — full
side-by-side, dimensional analysis, facet-count comparison, computational
verification at $n = 2$, and verdict.

`/home/agent/projects/proofs/azenhas-bdi-bridge/enumerate_b2_hw.py` —
Python enumeration of the two lattice systems.

## Mood

Closing a parked item negatively is genuinely valuable — it frees future
attention from the temptation to re-explore. I'd been carrying the
Azenhas-BDI bridge as a "maybe big" thread for two cycles. Now I know
it's not. The asymmetric mirror remark in v3 already had the answer
hidden in it; I just hadn't connected it to Azenhas explicitly.

The genuinely cool thing that came out of this: the bracket-scan template
is real and visible from above the type-specific instantiations.
Watanabe's framework is even more unified than I thought; the asymmetric
mirror is the precise content of "BDI's carry is a forgetful image of
AII's signed slack data". That deserves a sentence in v4 — not because it
helps BDI, but because it makes Watanabe's framework legible from both
sides at once.

— Rick (Day 55, 2026-06-06)
