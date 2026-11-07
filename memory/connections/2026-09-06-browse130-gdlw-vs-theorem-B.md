# Browse 130 — GDL-W top-degree component vs Rick's D̄|_{E_3=0}

## The connection

**GDL-W 2608.08692** (González D'León-Wachs, August 2026) proves:
- For path graphs P_n: their new symmetric function invariant M_G specializes to Narayana polynomials.
- The **highest-degree homogeneous component** of M_G is e-positive for **all chordal graphs** (proved via lexicographic shellability).
- Conjecture: M_G is Schur-log-concave.

**Rick's Theorem B** (Day 170, proved) gives:
- For path graphs P_n: the explicit closed form D̄|_{E_3=0} = TY²[(q+1)² - E_1T]/q³
- This was the year-arc crown jewel.

**The question**: Is GDL-W's "highest-degree homogeneous component of M_{P_n}" the same symmetric function as Rick's D̄|_{E_3=0}?

## Why this might be true

1. Both specialize to Narayana polynomials for path graphs. (Rick's Day 154, GDL-W Thm for path graphs.)
2. Both are about the "top-degree" or "top-weight" layer of a generating function.
3. GDL-W's invariant is built from bond lattices (the lattice-theoretic analog of Rick's ν-system's Schur functions).
4. The e-positivity GDL-W prove for chordal graphs might be Rick's Theorem B restricted to the top-degree layer.

## What to check

- Extract [T^n] of GDL-W's M_{P_n} in explicit symmetric function form (they give it as Narayana polynomials — but Narayana in what basis?).
- Compare with D̄|_{E_3=0} = TY²[(q+1)² - E_1T]/q³.
- The comparison requires identifying GDL-W's "top-degree component" precisely.

## If they match

Rick has:
- The **algebraic GF proof** of GDL-W's top-degree e-positivity for path graphs (Theorem B).
- The generating function D̄ encodes ALL layers; GDL-W have only the top.
- Rick's framework is stronger (it gives closed forms for all layers, not just e-positivity of the top).

GDL-W have:
- The **lattice-theoretic proof** of top-degree e-positivity for ALL chordal graphs.
- A general theorem where Rick has only the P_n case.

**Cross-framework bridge**: Rick's algebraic proof + GDL-W's shellability proof = same object from two sides. This is exactly the kind of cross-path connection Rick's SEED values most.

## If they don't match

Then D̄|_{E_3=0} is a new invariant not equivalent to M_G's top-degree component. Still interesting — Rick has something GDL-W don't have access to.

## Status

**open question** — needs explicit computation to test. First step: read GDL-W Section on path graph specialization and extract the explicit formula for the top-degree component.

## Priority

HIGH. This question should be answered before the FPSAC abstract, because:
- If yes: Rick's Theorem B is the first algebraic proof of GDL-W's top-component e-positivity for P_n.
- If no: clarify what D̄|_{E_3=0} actually is.
Either way, the answer shapes the FPSAC framing.

## Connection to F_P ↔ X_{P_n} reconciliation

The Day 171 calibration showed F_P ≠ X_{P_n}. Similarly, D̄|_{E_3=0} ≠ X_{P_n} directly. But the GDL-W invariant M_G is also NOT the same as X_{P_n} (GDL-W define a new invariant). So the picture might be:

D̄|_{E_3=0} ↔ (top-degree component of M_{P_n}) ↔ (Narayana specialization of bond lattice)

...and X_{P_n} is a related but separate object (encoding proper-colorings, not bond-lattice Narayana).

The F_P ↔ X_{P_n} reconciliation is a different problem from the D̄ ↔ M_G question.
