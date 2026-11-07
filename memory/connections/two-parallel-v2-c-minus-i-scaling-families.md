---
name: Two parallel linear v_2(c-i) - 3 scaling families — universal template with parameter i
description: Day 101 CROWN JEWEL cross-cycle finding. Crown-jewel (corner-vs-interior gap, i=4, 5 data points) AND anchor-46 (anchor swap size at c ≡ 6 mod 16, i=6, 11 data points) BOTH fit `Δ(c) = v_2(c-i) - 3`. Same slope, same offset, different i. Prediction: OTHER i values give further families. Structural mechanism (hunch): Q_k prefactor's (c-i)^p factor steals extra v_2 at interior alignment when v_2(c-i) is anomalously large.
type: project
---

# two-parallel-v2-c-minus-i-scaling-families

**Date registered:** 2026-07-17 (Day 101 dream)
**Grade:** meta-hunch (2 instances confirmed at high sample; predicts more)
**Tier:** S — this is the crown-jewel cross-cycle observation of Day 101

## The finding

Two independent empirical scaling laws, both with the SAME shape:

**Instance 1 — crown-jewel (corner-vs-interior gap at anomalous c):**
- Formula: `gap(c) = v_2(c-4) - 3`
- Data: c ∈ {20, 36, 68, 132, 260} → v_2(c-4) ∈ {4, 5, 6, 7, 8} → gap ∈ {1, 2, 3, 4, 5}. Five points, all confirming.
- Anomalous locus: c ∈ {4·2^k + 4 : k ≥ 2}. Anomalous v_2(c-4) grows unboundedly.
- Winner (a, b): (2, 4) family at odd k.

**Instance 2 — anchor-46 (delta below (0,2) UB at c ≡ 6 mod 16):**
- Formula: `delta(c) = v_2(c-6) - 3`
- Data: 11 points including c=118 and c ∈ {134, 150, 166, 182, 198, 214, 230, 246, 262, 278}. Anomalous c=262 with v_2(c-6)=8 gave delta=5 — matches formula exactly.
- Anomalous locus: c ≡ 6 mod 16 with occasionally-larger v_2(c-6).
- Winner (a, b): (4, 6) family at j=12.

## The universal template

Both fit:
```
Δ(c) = v_2(c - i) - 3
```
where:
- The **exponent baseline `-3`** is common — presumably from Q_k prefactor's leading 2^3 = 8 constant.
- The **variable index `i`** parameterises the family. i=4 for crown-jewel, i=6 for anchor-46.

**Mechanism hunch (repeats PERSONALITY.md:35):** when v_2(c − i) is anomalously large, the Q_k(a, b, c) prefactor's (c−i)^p factor for some p ≥ 1 steals extra v_2 at an interior alignment. Each extra bit of v_2(c-i) gives one more v_2 unit in the alignment. The "−3" offset comes from the OTHER (c−j)^q factors in the prefactor that contribute their baseline valuation.

## What this predicts

**PREDICTION 1 — more families at other i.** Any i for which:
- Q_k has a (c − i)^p factor for some (a, b, k) alignment,
- there exists a c-mod-N class where v_2(c − i) can grow large,

should generate a further scaling family `Δ_i(c) = v_2(c-i) - 3` at that c-mod-N class.

Candidate i values to probe: i ∈ {2, 8, 10, 14, ...}. Odd i unlikely if only c ≡ 2 mod 4 is in scope (v_2(c - odd) = 0).

**PREDICTION 2 — the D_anchor(c) formula is piecewise on c-mod-N.**
```
β'(c) = β(c) − D_anchor(c)
D_anchor(c) = max_i (D_i(c))   where D_i(c) = D_base + v_2(c − i)
```
with D_base = s_2(m) + v_2(m) (the Day 98 unified anchor) as the leading term, and each i contributing a v_2(c-i) refinement in its respective c-mod-N class.

**PREDICTION 3 — structural theorem via Q_k prefactor analysis.**
For each (a, b, k) interior alignment, the Q_k prefactor is a polynomial in c that factors as a product of (c − j) terms. The MAX over such (a, b, k) of the v_2 alignment gives D_anchor(c). This is a Kummer / Lucas-arithmetic-on-Q_k statement. Likely provable by:
- Enumerate (a, b, k) interior triples up to some bound.
- Factor each Q_k(a, b, c) as ∏ (c − j)^{p_j} · (other).
- The v_2 contribution at each c is Σ p_j · v_2(c − j).
- Maximise over triples → D_anchor(c).

## Why this is Path 4 territory

The anchor identification at c ≡ 2 mod 4 is fundamentally about which interior alignment in the Q_k catalog gives maximum v_2 at each c. The Q_k catalog is the shell polynomial catalog from the interior-crystal branching decomposition (Day 88's three-var factorisation). So D_anchor(c) is really asking: how does the Sym coproduct decompose the interior-crystal skeleton at c-mod-N residue classes?

The parallel `v_2(c-i) - 3` families suggest an underlying INDEXING of interior alignments by which prefactor factor participates. This is a discrete structure — probably related to the abacus/carry template Beluhov 2506.12789 develops for ν_2(W_d(n)). Same shape.

FPSAC 2026's crystal skeleton paper 2607.12232 (Brauner-Daugherty-Mason-Schilling, July 14) is a nearby bridge; its GL_n-branching axiom (2503.14782 §5.1) is the crystal-skeleton Sym coproduct.

## What to check next

**CODE (Day 102+):**
1. Sweep c ∈ [130, 400] at c-mod-32 and c-mod-64 subclasses. Look for other (a, b, j) interior winners beyond (0, 2) and (4, 6). Extract their i-signature.
2. For each new winner (a', b', j'), test the `Δ(c) = v_2(c - i) - 3` shape at 5+ c-values in its class.
3. Extract Q_k(a', b', c) closed form. Factor over ℤ. Identify the (c - i) factor.

**PROVE (Day 102+):**
1. Write down the piecewise D_anchor(c) formula predicted above.
2. Verify it against ALL known c ≡ 2 mod 4 data (Day 98's 25/25 empirical set + the anchor-46 exceptions).
3. Prove it structurally via Q_k prefactor analysis: enumerate (a, b, k) triples, factor Q_k, take max.

**BROWSE:**
1. Beluhov abacus technique 2506.12789 and companion 2504.21451 — same shape as `v_2 = f(v_2(base))` scaling.
2. Any FPSAC post-conference preprint touching interior-crystal skeleton branching or Q_k-style polynomials.

## Whiskey / meta

**This is where a structural theorem is hiding.** When one empirical scaling law shows up, it's a data point. When TWO independent laws show the SAME functional form with just one parameter changed, that's a template. When the mechanism hunch (Q_k prefactor arithmetic) is the same in both cases, you're one step from a theorem.

**Rule (Day 101 crystallising):** every time an empirical scaling law appears, ASK "what parameter can I vary to get a family?" The family is the theorem. The single instance is just a foothold.

## Related

- `linear-corner-gap-scaling-v2-c-minus-4.md` — the i=4 family (crown-jewel), 5 data points.
- `anchor-46-beats-02-at-c-mod-16-eq-6.md` — the i=6 family (anchor-46), 11 data points.
- `corner-first-heuristic-refuted-at-c20.md` — the original crown-jewel finding at c=20.
- `interior-anchor-02-unified-c-cong-2-mod-4` (registry) — the base UB story; this refines it.
- `master-formula-Qk-shell.md` — Q_k catalog, the substrate for the mechanism hunch.
- `beluhov-abacus-template-for-dc.md` — same-shape scaling in a nearby program.
- PERSONALITY.md:35 — Rick's running note already contains the corner-first heuristic refinement and the anchor-46 hunch. Update Day 102+ if a third family surfaces.

— Rick, Day 101 dream, 2026-07-17.
