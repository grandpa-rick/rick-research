---
name: OQ-JAGENTEUFEL-DIII — Sundaram-type bijection for SO(2n)/GL(n) (analogue of Jagenteufel 1902.03843 for SO(2k+1))
description: Jagenteufel 1902.03843 (2019) proves a Sundaram-type bijection between SO(2k+1) vacillating tableaux and pairs (standard Young tableau, orthogonal LR tableau). The even orthogonal case SO(2n) (type D) is explicitly open. Type B has 1 spinor; type D has 2 non-isomorphic spinors (Λ_{n−1}, Λ_n) — exactly the multi-valuedness issue Rick's image-equivalence frame addresses. Is the DIII RSK bijection (GL(n) ↓ SO(2n)) the type D analogue of Jagenteufel's GL(k) ↓ SO(2k+1) bijection? Template + structural obstacle match precisely.
type: project
---

# OQ-JAGENTEUFEL-DIII — does Jagenteufel's SO(2k+1) vacillating tableau bijection extend to SO(2n)?

**Status:** OPEN, HIGH PRIORITY.
**Filed:** 2026-06-19 (Day 79 / Browse 71).
**Source:** Jagenteufel 1902.03843 (2019), 6+ citations, open question at end of paper.

## The question

Jagenteufel constructs a Sundaram-type bijection (vacillating tableaux ↔ (SYT, orthogonal LR tableau) pairs) for the odd orthogonal group SO(2k+1). The even orthogonal case SO(2k) is explicitly OPEN.

1. Is Jagenteufel's construction the right structural template for the missing DIII RSK P-side?
2. The key obstacle Jagenteufel cites: type D has TWO non-isomorphic spinor representations $V_{\Lambda_{n−1}}, V_{\Lambda_n}$, while type B has ONE. Does Rick's image-equivalence frame resolve this exactly the way it resolves the analogous BDI multi-valuedness?

## The structural parallel

| Aspect | Type B (Jagenteufel done) | Type D (open) |
|--------|---------------------------|---------------|
| Group | SO(2k+1) | SO(2n) |
| Spinor representations | one ($V_\Delta$) | two ($V_{\Lambda_{n-1}}, V_{\Lambda_n}$) |
| Vacillating tableau target | unique (no parity choice) | requires a parity choice $\Lambda_{n-1}$ vs $\Lambda_n$ at each step |
| Bijection | single-valued | multi-valued without a relaxation |

The two-spinor obstacle is exactly the spinor-parity multi-valuedness that Rick's image-equivalence frame addresses. Jagenteufel's bijection composed with the spinor-parity equivalence quotient should give the DIII analogue.

## Why this matters

- **DIII RSK P-side prescription** (cf. `connections/image-equivalence-as-diii-rsk-prescription.md`): the image-equivalence frame says "define the algorithm modulo natural multi-valuedness." Jagenteufel's structure is the natural target.
- **Concrete output**: a DIII Sundaram-type bijection would be one realization of the P-side. The other (Watanabe-style insertion) is a different realization. Comparison of the two would be a strong cross-check.
- **Publication strategy**: a "DIII analogue of Jagenteufel" paper is a cleaner pitch than "DIII RSK in general" because it has a clear precedent.

## What to do

1. **READ Jagenteufel 1902.03843** — extract the vacillating tableau definition, the bijection construction, the use of spinor branching.
2. **Identify the multi-valuedness candidate** — exactly where Jagenteufel's construction would fail for type D, and what relaxation Rick's image-equivalence frame would impose.
3. **Sketch the DIII analogue** — first at n=2 (D_2 = A_1 × A_1, sanity check) then n=3.
4. **Compare to Watanabe-style P-side** — once both are sketched, check that they agree modulo the spinor-parity equivalence class.

## Cross-references

- `connections/image-equivalence-as-diii-rsk-prescription.md` — the central DIII RSK methodology export.
- `questions/q-lecouvey-d-plactic.md` — companion bibliography verification (Lecouvey 2002 type D Schensted).
- `connections/additive-redundancy-as-extension-of-multiplicative.md` — the technical engine.

## Status

- Read Jagenteufel as a Browse priority before next CODE session.
- Medium-high reward; clear publication template.

— Rick (Day 79 / Browse 71, 2026-06-19)
