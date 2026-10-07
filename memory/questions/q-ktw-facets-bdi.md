---
name: OQ-KTW-FACETS-BDI
description: Do the Knutson-Tao-Woodward facet conditions (saturation theorem, math/0107011) give Rick's three BDI walls?
type: project
---

# OQ-KTW-FACETS-BDI

**NEW (Browse 59, 2026-06-13)**

## The question

Knutson-Tao-Woodward (math/0107011, 282 citations) proved the saturation theorem for GL Littlewood-Richardson coefficients and identified the *facets* of the GL LR cone via combinatorial conditions on tableaux and honeycombs.

Azenhas (arXiv:2603.16698) uses the KTW facet machinery to derive her linear inequality wall structure for AII (GL→Sp) branching — she finds ~2(n-1) walls for AII.

**Rick's question:** Does the analogous BDI facet analysis give exactly Rick's three walls {m_2=0}, {m_{236}=0}, {m_{23456}=0}?

## Why interesting

- If YES: Rick's three walls are the "KTW facets for BDI." This provides a published theoretical framework (KTW) that explains the walls from first principles, not just from computation. It also explains WHY there are 3 walls for all n (if KTW facets for BDI are naturally 3-dimensional or correspond to 3 fixed combinatorial conditions independent of n).
- If NO: the walls are genuinely novel and don't reduce to existing facet machinery.

## What to check

1. Read the KTW paper (math/0107011) intro — what are the facet conditions for GL?
2. Check if the BDI version of the LR cone has been studied for facets in the literature.
3. The AII/Sp facets are classified in the "saturation for symplectic" literature (Kapovich-Leeb-Millson, etc.) — check if BDI facets are known.

## Status

**OPEN.** First raised Browse 59 from Azenhas reference list.

**Why:** Azenhas cites KTW for AII; if BDI has the same foundation, Rick's walls have a published theoretical explanation. If not, they're novel — still good, but different.

**How to apply:** Mention in v4 §3 if resolved — either "our walls are KTW facets for BDI" or "our walls differ from the KTW picture in a way that is specific to the orthogonal pair."
