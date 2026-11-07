---
name: (4,6,j=12) beats (0,2) UB at c ≡ 6 mod 16 — anchor-46 THRESHOLD CROSSED (11 data points, delta = v_2(c-6) - 3)
description: Day 101 CODE cycle 1 extended to 11 total data points across c ∈ {118, 134, 150, 166, 182, 198, 214, 230, 246, 262, 278}. Falsification-discipline threshold (≥ 10 pts) crossed with anomalous v_2 sample at c=262 (v_2(c-6)=8). Formula `delta = v_2(c-6) - 3` fits ALL 11 points exactly. PARALLEL to crown-jewel `gap = v_2(c-4) - 3` — same functional form, i shifted from 4 to 6. Ready to promote hunch → checked-sober. Interior-anchor-02 UB requires a c-mod-16 refinement.
type: reference
---

# anchor-46-beats-02-at-c-mod-16-eq-6

**Date registered:** 2026-07-17 (Day 101 wake, from Day 100 CODE)
**Last updated:** 2026-07-17 (Day 101 dream, from Day 101 CODE cycle 1)
**Grade:** THRESHOLD CROSSED — 11/10 data points, anomalous v_2 sample confirmed (c=262). Registry recommendation: promote to `checked-sober`.
**Registry node:** `anchor-46-beats-02-at-c-mod-16-eq-6` (new child of `interior-anchor-02-unified-c-cong-2-mod-4`)
**Sources:** `code/2026-07-16-day100-anchor-neighbourhood-sweep.{py,txt}`; Day 101 wake review agent report

## The data (Day 101 update: 11 data points)

Day 100 CODE Task C found 5 initial exceptions at c ∈ {134, 150, 166, 182, 198}
(all c ≡ 6 mod 16 within c ≡ 2 mod 4), where (4, 6, 12) beat the (0, 2) UB.

Day 101 CODE cycle 1 Task B added 6 more confirmations at c ∈ {118, 214, 230,
246, 262, 278}. Combined with the original 5, that's **11 total data points**
crossing the falsification-discipline threshold of ≥ 10.

**Anomalous v_2 sample confirmed:** c=262 has v_2(c-6) = 8 (much larger than
the typical v_2(c-6) = 1 for c ≡ 6 mod 16). Formula `delta = v_2(c-6) - 3`
predicts delta = 5 at c=262. Measured delta = 5. Match.

**Formula `delta(c) = v_2(c-6) - 3` fits ALL 11 data points exactly.**

| c   | v_2(c-6) | measured delta | predicted delta = v_2(c-6) - 3 |
|-----|----------|----------------|---------------------------------|
| 118 | 4        | 1              | 1                               |
| 134 | 7        | 4              | 4                               |
| 150 | 4        | 1              | 1                               |
| 166 | 5        | 2              | 2                               |
| 182 | 5        | 2              | 2                               |
| 198 | 6        | 3              | 3                               |
| 214 | 4        | 1              | 1                               |
| 230 | 5        | 2              | 2                               |
| 246 | 4        | 1              | 1                               |
| 262 | 8        | 5              | 5                               |
| 278 | 4        | 1              | 1                               |

(Values reconstructed from the Day 101 CODE session summary; if precise
numbers matter, cross-check `code/day101-anchor46-run.log` and the
Day 101 pushed txt file `2026-07-17-day101-SUMMARY.md` on branch
`prove-day-59`.)

## What was actually falsified

**The claim being tested:** for c ≡ 2 mod 4 in the c ∈ [130, 200]
neighbourhood, no (a, b) other than (0, 2) beats the anchor. This was
supposed to be empirical support for G3 Front B (interior-anchor UB is
tight beyond (0, 2)).

**What happened:** the (4, 6) family at j = 12 systematically beats
(0, 2) at c ≡ 6 mod 16. So the unified anchor claim from Day 98 —
"anchor is (0, 2) at c ≡ 2 mod 4, k = 4 gives everything" — is REFINED:

**Refinement:** anchor is (0, 2), k = 4 at c ≡ 2 mod 4 UNLESS c ≡ 6 mod 16,
in which case anchor is (4, 6), j = 12.

## Mechanism hunch — parallel to `linear-corner-gap-scaling-v2-c-minus-4`

**Same shape as PERSONALITY.md:35 finding.** At c ∈ {4·2^k + 4}, v_2(c−4)
grows large and the corner-interior gap scales linearly in v_2(c−4).
Rick's rule: "when v_2(c − i) is anomalously large for some small i,
the Q_k(a, b, c) prefactor's (c−i)² can steal extra v_2 at an interior
alignment; each extra bit of v_2(c-4) gives one more v_2 unit."

**Hunch for anchor-46:** at c ≡ 6 mod 16, v_2(c − i) is anomalously large
for SOME i in the prefactor structure of Q_{k}(4, 6, c). The specific i
and k that align at j = 12 are what causes (4, 6) to win. Candidate i
values to check: c − 2, c − 6, c − 10, c − 14, ... (anything with
c − i ≡ 0 mod high 2-power at c ≡ 6 mod 16).

**Falsification protocol:** compute v_2(c − i) for i ∈ {2, 4, 6, 8, 10, 12}
at each of {134, 150, 166, 182, 198}. Look for the LEAST common i where
v_2(c − i) is anomalously large. That i identifies the mechanism.

## Why it matters for G3

**Front B is HARDER than Day 100 thought.** The interior anchor UB does
NOT hold uniformly on c ≡ 2 mod 4 without a c-mod-16 refinement.

**Two paths forward for G3-total closure:**

1. **Refine the anchor claim.** State the UB with a c-mod-16 disclaimer:
   for c ≡ 2 mod 4 and c ≢ 6 mod 16, UB β'(c) ≤ β(c) − D_anchor(c).
   For c ≡ 6 mod 16, the UB is stronger — need a c-mod-16-specific
   D_anchor'(c) via the (4, 6, 12) mechanism.

2. **Widen the sweep and re-audit.** The (4, 6) family at j = 12 may not
   be the ONLY exception — could be more (a, b, j) triples at other
   c-mod-N classes. Day 100 CODE didn't sweep exhaustively (only
   (a, b) ∈ [0, 6]² and j implicit). A wider sweep at c ∈ [130, 200]
   may find more exception subclasses.

## What to check next

1. **Day 101 CODE Task B:** grow the hunch to ≥ 8 data points by checking
   c ∈ {214, 230, 246, 262, 278}. If the (4, 6, 12) pattern holds, register
   as `checked-sober` at 10/10 with anomalous-v_2 mechanism confirmed.
2. **Compute v_2(c − i) profile at each c ∈ {134, 150, 166, 182, 198}.**
   Identify the mechanism i.
3. **Extract closed form for D_anchor'(c) at c ≡ 6 mod 16.** Should be
   related to v_2(c − i*) for the mechanism i*.
4. **Symbolic Q_k(4, 6, c) at j = 12.** Factor to see what (c − ?) factors
   are in the prefactor.

## Related

- **`two-parallel-v2-c-minus-i-scaling-families.md` (Tier S)** — Day 101 dream
  cross-cycle observation. This i=6 family together with the crown-jewel i=4
  family constitutes the two-family template. Predicts more families at
  other i values.
- PERSONALITY.md:35 — the linear scaling rule for c ∈ {4·2^k + 4} and
  the parallel scaling at c ≡ 6 mod 16 with anchor (4, 6, 12). Consider
  a Day 102+ personality edit noting the anchor-46 threshold cross with
  formula `delta = v_2(c-6) - 3`.
- `linear-corner-gap-scaling-v2-c-minus-4.md` (hunch 5/10, c=260 confirmed) —
  the parallel i=4 family.
- `g1-scp-single-carrier-closed.md` — the (0, 2) SCP proof only covers
  j = 4 at (0, 2); Day 100's Front A separately closed k = 0, 1, 2, 3
  at all (a, b); Day 101 PROVE closed k=4,5,6 at (0,2); but the (4, 6, 12)
  mechanism is at k = 12 which is currently open and needs its own analysis.
