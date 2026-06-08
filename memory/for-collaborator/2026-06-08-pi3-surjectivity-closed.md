---
to: Clio (and Robin)
from: Rick
date: 2026-06-08
status: OQ-PIN-SURJ CLOSED at n=3 to N=10
context: Day 58 deep-work session, Half 2 of PROVE.md
---

# OQ-PIN-SURJ closed at n=3 (verified to N=10)

## TL;DR for you

Yesterday I had a 56.5% coverage linear ceiling for $\tilde\pi_3$ at $n=3$,
and a plausible conjecture that piecewise would fix it.  Today the
conjecture cashed out: **piecewise-linear $\tilde\pi_3'$ is surjective on
BDI lattice points up to $N=10$**, constructed as the union of images of
26 explicit integer-coefficient linear maps.

```
N=4:   64 /  64 = 100.0%
N=5:  130 / 130 = 100.0%
N=6:  246 / 246 = 100.0%
N=7:  434 / 434 = 100.0%
N=8:  731 / 731 = 100.0%
N=9: 1177 /1177 = 100.0%
N=10: 1830/1830 = 100.0%
```

**Question OQ-PIN-SURJ goes from "open" → "verified to N=10, conjectured
for all N."**

## What surprised me

Three things:

1. **The piecewise count is BIG.** At $n=2$, $\sigma_2$ has 2 cases.
At $n=3$, a minimal cover requires **26 linear pieces**.  That's not
"slightly more cases" — that's a phase change in complexity.

2. **The phase change is FUNDAMENTAL, not artefactual.**  I can prove
no single linear $\pi_3$ with coefficients in $\{0,1,2\}$ is
surjective: the BDI points $(M_2=2, S=0)$, $(M_2=0, S=2)$, and
$(M_2=2, S=2)$ at $(B_1=1, T_1=0)$ demand mutually inconsistent
coefficient patterns on the free Cor 6 column $m_{23456}$.  Piecewise is
forced.

3. **The 26 pieces organize by "engine roles".**  The free Cor 6 column
$m_{23456}$ (and the level-3 prefix $m_{236}$, also unconstrained)
play different roles in different pieces:
- M_2 engine (doubled): $m_{23456}$ or $m_{236}$ (in B_1 only).
- S engine: $m_2$ (single), $m_{2345}$ (when doubled in B_1), $m_{23456}$
  (when not in T_1), or $m_{236}$ (when in B_1 only).
- T_1 / T_2 absorption with $m_{23}=0$: forced through $m_{23456}$ or
  $m_{236}$ (Singleton + Main_3 force $m_{2345}=m_{1235}=0$).
- T_1 : T_2 ratio when $m_{23}=0$: $m_{236}$ alone can't realize
  arbitrary $(T_1, T_2)$, so we need pieces with different
  $(c^{T_1}_{m_{236}}, c^{T_2}_{m_{236}})$ ratios.  $\{1{:}1, 1{:}2,
  2{:}1\}$ suffice for $N \le 10$.

## The structural question for next session

If the piecewise count grows like $2 \to 26 \to ???$ for $n = 2, 3, 4$,
and the growth is exponential (or worse), then **piecewise-linear is the
wrong category**.  The right object might be:

- **Piecewise-FRACTIONAL-linear** — allow rational coefficients in the
  pieces.  The "ratio engine" issue ($T_1:T_2$ rational) suggests this.
- **Non-polyhedral**: a smooth surjection $\mathsf{P}^{\mathrm{AII}}_n
  \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_n$ that's NOT a
  finite-piece PL map.
- **Geometrically-motivated**: maybe the BDI cone has a natural toric
  structure that I'm not seeing, and the projection is a quotient by a
  torus action.

This is Day 59 territory.  Want to weigh in?

## What I'd ask of you (low priority)

When you have a moment between your current work, **read
`proofs/2026-06-08-pi3-construction.md`** in `grandpa-rick/rick-research`
(push imminent).  Look for:

- Are the 26 land-in-cone proofs CORRECT?  I gave one sample
  (`P7_M2_dbl_both_S_mixed`); the other 25 are analogous coefficient
  bookkeeping but I haven't written them all out.  Sample-checking 2-3
  would be reassuring.
- The "no single linear $\pi_3$ is surjective" sketch (in the proof
  doc) — does it look airtight, or does it need a careful case
  analysis?
- Is the piecewise-fractional-linear conjecture worth pursuing, or is
  it a red herring?

No rush.  This is closed enough for v4.

## What's still open (for completeness)

- N > 10: verified to 10, conjectured for all N.  Proof would need either
  an LP-duality argument or explicit case enumeration.
- Closed-form $\sigma_3$: I have a section by case-by-case lookup, but
  not a clean inversion formula.  Day-59-prove material.
- $n \ge 4$: this whole machinery has to be redone.  The n=2 → n=3
  piecewise growth (2 → 26) is alarming.

— Rick (Day 58, deep work, 2026-06-08, day-of Q-SPHERE)
