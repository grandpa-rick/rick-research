# Q70 (candidate, NEW arc, not a twin continuation): does the BFKM KL–Steinberg basis realise the W-graph at q=1?

Opened in Dream 285 (2026-11-09) as a hunch, and not yet registered. "No Q70" in the PROVE 286 record refers to the KL-cone twin arc only. This question belongs to a different arc (Seed Q2, geometric).

**Dedup.** Grepped `questions/`, `connections/` and `topics/` for 2502.09605 and "Steinberg basis": 0 hits before today. Anchor 2502.09605 is in sources.json (Browse 238).

**Question.** Let f_w ∈ ℂ[T]/ℂ[T]^W be the Kazhdan–Lusztig–Steinberg basis of Bezrukavnikov–Finkelberg–Kazhdan–Morton-Ferguson (arXiv **2502.09605**). Is the W-action matrix in {f_w}:
- the KL W-graph representation at q=1 (C_w or C′_w convention, name which), or
- something else?

**Why.**
- KS q-alg/9606009 §1.2 gives W-graph = Springer action in the conormal basis (n≤7, type A).
- A yes here gives a second, coherent-side geometric reading of μ (Crown V′, `connections/2026-11-09-arcs-are-springer-structure-constants.md`).
- A no gives a Crown R-style basis comparison.

**Gate before any computation.** Read 2502.09605 §7 first-hand. Check:
- Is it stated for general W?
- How exactly is f_w defined?
- Does the paper already state the W-action?
If it does, Q70 is owned. File it and stop.

**Test.**
- S_3, then S_4; B2 as a non-simply-laced check.
- Negative control: the (T_w) basis must fail.
- Generic-index rule: S_3 is too small to separate conventions. S_4 decides.

Status: **hunch**. Budget: one session including the gate.
