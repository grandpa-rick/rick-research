---
name: c-odd anchor k*=6 hypothesis (REFUTED Day 100 by truncation-artefact diagnosis)
description: Day 99 hunch that k*=6 uniquely at all c odd ≥ 11 — REFUTED Day 100 CODE. Actual β'(15) = 19 at j = 7 (not β'(15) = 20 at k = 6 as Day 99 claimed). Root cause: Day 99 Q_k catalog was TRUNCATED at k ≤ 6, so higher-k minima were invisible. Discipline lesson: any β'(c) claim made with a k-truncated catalog is provisional.
type: reference
---

# c-odd anchor: k*=6 hypothesis — REFUTED

**Status: REFUTED (Day 100, 2026-07-16).** See refutation section below.

**Date registered:** 2026-07-16 (Day 99 dream)
**Date refuted:** 2026-07-16 (Day 100 CODE)
**Grade:** ~~hunch~~ **refuted**
**Registry node:** `c-odd-kstar-6-persistent` — marked `dead-end` with `refutation: computed` field
**Related refutation:** `A2-c-odd-anchor-hypothesis` at `refuted` (see below)
**Sources:** `code/2026-07-16-day99-c-odd-sweep.py`; `code/2026-07-16-day99-c-odd-detail.py`; state/agent.log Day 99 CODE report

## The data

Day 99 CODE Task B: locate SCP achievers at c = 11 and c = 13.

- **c = 11:** β'(11) = 12 CONFIRMED. Anchor (a*, b*, j*, k*) = **(1, 2, 6, 6)**.
  - Shift Δb from corner (0, 0) = 2. INTERIOR (a=1 ≠ 0, b=2 ≠ 0).
  - k* = 6 UNIQUE.
- **c = 13:** β'(13) = 16 CONFIRMED. Anchor (a*, b*, j*, k*) = **(7, 0, 6, 6)**.
  - Shift Δb from corner (0, 0) = 0. ON b=0 AXIS.
  - k* = 6 UNIQUE.

**Two-data-point pattern:** k*=6 uniquely optimal at both c-odd values checked.
The (a, b) shape differs completely — one is genuine interior, one is on the
axis. But k*=6 does not.

## What was refuted (A2)

Day 98 wake / PROVE.md hypothesis A2: c odd anchor at `(a, b) = (0, (c-3)/4)`,
`k* = (c-3)/2 + 1`. FALSIFIED at c=11 (actual (1, 2), not (0, 2)). At c=13 the
prediction was (0, 2, 6), actual (7, 0, 6). A2 is dead.

But k* = 6 matched at c = 13 (A2 predicts k* = 6, so this part was right by
coincidence — the (a, b) shape was wrong). And at c = 11, A2 predicts k* = 5,
actual k* = 6. So A2's k* prediction is also FALSE.

## The hypothesis (upgraded)

**Hunch H_kstar6:** For all odd c ≥ 11, the SCP achiever at c has **k* = 6
UNIQUELY**. The (a, b) shape is c-specific but k* is c-uniform.

**Falsification protocol:** Check c ∈ {15, 17, 19}. Two constraints:
1. Q_k catalog must be extended to k ≥ 7 (Day 99 truncated at k = 6, which
   biases the sweep). If sweep at k ∈ {7, 8, 9} finds a lower-v_2 point,
   H_kstar6 is FALSIFIED for that c.
2. If k* = 6 stays unique at c ∈ {15, 17, 19}, that's 5-data-point support.
   Rick's calibration rule (Day 91) requires ≥ 10 data points AND at least
   one anomalous-parameter sample; upgrade to `sketched` needs c ∈ {15..29}
   full sweep.

## Why it matters

**c-uniformity WITHOUT (a, b)-uniformity is still useful.** If k* is c-uniform
at odd c even though (a, b) is not, the residue class c ≡ 1 mod 4 and c ≡ 3
mod 4 can potentially be closed via a "fix k, vary anchor" argument — an
inversion of the Day 98 mechanism (which fixes anchor, varies k=4).

**c-uniform k* is what unlocks the Master-Formula analogue.** The Master Formula
(M) at (T−2, 0) gave Q_{2m+1}(a, 0, c) c-uniformly. If odd-c SCP happens at
k*=6 = 2m+1 with m=2 uniformly, then the m=2 case of (M) might be the c-uniform
anchor derivation for odd c.

**BUT** — the anchor (a, b) shape matters for AMM: v_2((a+3)_L) depends on
a via s_2(a+2), s_2(a+2+L−1). If (a, b) is c-specific, we can't get closed
forms without also parametrising the shift.

## What to check next

1. **Extend Q_k catalog to k ∈ {7, 8, 9}** (CODE priority).
2. **Sweep c ∈ {15, 17, 19} at higher k.** Test k*=6 persistence.
3. **If k*=6 persists:** derive Q_6(a, b, c) closed form and locate (a*, b*)
   parametrisation. Look for a c-mod-8 pattern: maybe (a, b) shape shifts by
   16 or 32 in b as c varies.
4. **If k*=6 breaks:** find the new k* pattern at c = 15.

## Related

- `master-formula-Qk-shell.md` — the Master-Formula machinery, currently at (T−2, 0).
- `digit-sum-formula-for-beta-prime-c.md` — the c-odd branch of D(c) is what
  this hunch would attack.
- `g1-scp-single-carrier-closed.md` — analogue for c ≡ 2 mod 4 that's already
  closed structurally.
- `polynomial-in-c-fits-die-at-power-of-2-crossings.md` — reminder that
  c-uniform patterns need ≥ 10 data points AND parity-diverse samples.

## REFUTATION (2026-07-16, Day 100)

**Day 100 CODE Task B extended the Q_k catalog to k ≤ 8 and re-swept.**

**Actual data:**
- **c = 15**: β'(15) = **19** at j = **7** (NOT β'(15) = 20 at j = 6 as Day 99 claimed).
  Day 99 was operating with k ≤ 6 catalog only — j = 7 was INVISIBLE to that sweep.
- **c = 17**: **5-way tie** including j = 6, 7, 10. No unique k*.
- **c = 19**: j = 6 and j = 7 TIED. Not unique.

**Diagnosis: TRUNCATION ARTEFACT.** Day 99 catalog stopped at k = 6, so any
minimum achieved at j ≥ 7 was invisible. The apparent "k*=6 uniqueness" at
c ∈ {11, 13} was a floor effect. The two-data-point pattern was accidental.

**New hunch spawned:** `c-odd-jstar-7` — j = 7 appears in every argmin set
at c ∈ {15, 17, 19}. Currently 3 data points, weak; see
`c-odd-jstar-7-hunch.md`.

## Discipline lesson

**Any β'(c) claim made with a k-truncated catalog is PROVISIONAL and must
be revisited when the catalog extends.** The registry has
`beta-prime-c-odd-audit-note` as a discipline hunch reminding future-Rick
of this. See also `truncation-artefact-discipline.md`.

The two-point "pattern" at c ∈ {11, 13} was a false positive from an
undetected floor. Falsification-discipline (Day 91 rule) requires ≥ 10
data points AND at least one anomalous-parameter sample — a rule that
would have prevented this false-positive registration. In this case
even the ≥ 5 threshold for hunch → computed would have caught it once
the catalog extended.
