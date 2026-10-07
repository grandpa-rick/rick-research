---
name: OQ-KIERS-BDI — Kiers extremal rays for GL(n) ⊆ SO(2n)
description: Does Kiers arXiv:1909.09262 "Extremal rays of the embedded subgroup saturation cone" give exactly 3 extremal rays for the branching cone of GL(n) ⊆ SO(2n)?
type: project
---

# OQ-KIERS-BDI

**Opened:** Browse 62 (2026-06-14)
**Priority:** HIGH — closest existing work to the GL(n) ⊆ SO(2n) branching eigencone computation

## The question

Kiers arXiv:1909.09262 ("Extremal rays of the embedded subgroup saturation cone," 2019) extends Belkale-Kumar and Ressayre-Richmond to general G ⊆ G-hat. It proves extremal ray formulas for the branching saturation cone LR(G, G-hat). The pair GL(n) ⊆ SO(2n) is a natural instance.

**Does Kiers' result, applied to GL(n) ⊆ SO(2n), give exactly 3 extremal rays?**

If yes: this may be the geometric proof of # AXIS(BDI) = 3 via branching Schubert calculus.

## Background

- **Ressayre-Richmond 0909.0865:** Gives a compact formulation of the branching eigencone for any G ↪ G-hat via the branching BK product. Applies in principle to GL(n) ⊆ SO(2n). But the actual computation is not done anywhere.
- **Kiers 1909.09262:** Extends this to the saturation cone (considers all integer multiples). Cites RR directly. Proves "type I" and "type II" extremal ray formulas for general pairs. 2 citations only — underread.
- **Rick's result:** # AXIS(BDI) = 3 proved (lower bound via Lemmas A/B/C, upper bound via Feasibility Ray-Characterisation + Conjecture D-pi). The geometry should be visible in the Schubert calculus of GL(n)/B ↪ SO(2n)/B.

## What to do

1. **Read Kiers 1909.09262 intro + main theorem (~1h).**
   - What is "type I" vs "type II" extremal ray?
   - Does the theorem give an explicit formula for the number of extremal rays?
   - Does it apply to GL(n) ⊆ SO(2n) specifically?

2. **Check if the pair GL(n) ⊆ SO(2n) is covered by their framework.**
   - Is this a "spherical" embedding? (It is — polar decomposition)
   - Is it a "symmetric" embedding? (It is — DIII symmetric pair)
   - Do they compute anything for symmetric pairs explicitly?

3. **If yes:** extract the extremal ray count for GL(n) ⊆ SO(2n) and check if it equals 3.

## Connection to Rick's work

**If Kiers gives exactly 3 extremal rays for GL(n) ⊆ SO(2n):** this is the geometric proof of # AXIS = 3, independent of the polyhedral/registry approach. The piecewise decomposition (Lemmas A/B/C) would then correspond to the 3 Kiers extremal rays — making the identification between the polyhedral and Schubert-calculus pictures explicit.

**Structural connection to Ressayre 1102.0196:** 3 extremal rays = 3 regular faces = 3 reduction rules for BDI branching multiplicities.

## Status

OPEN. Kiers 1909.09262 not yet read for this purpose.

**Why:** Browse 61 found RR 0909.0865 as the positive lead; Browse 62 found that Kiers 1909.09262 is the closest follow-up paper and handles general G ⊆ G-hat. This is a ~1h read that could close or substantially advance OQ-RESSAYRE-RICHMOND-BDI.
