---
name: Meta-pattern — positivity is provable at the extreme stratum and resists per-coefficient models
description: Day 150 dream. Four independent instances in one week (Rick's own (H2)/Rule 12, Alexandersson-Dai's aggregated-by-length positivity, Zemel's extreme-permutation-only antipode, Wang-Wang's certificates-instead-of-involutions). Naming it, because it predicts the shape of the right attack on Conjecture P and on the still-open NSym immaculate antipode.
type: connection
---

# Extreme-layer positivity

## The pattern

For Kostka-adjacent expansions in a **non-Schur basis**, positivity/cancellation is repeatedly

* **easy** at the extreme stratum of a natural filtration, or after aggregating over a coarser
  statistic, and
* **resistant** to a clean per-coefficient combinatorial model (a sign-reversing involution).

Four instances, all surfacing within one week:

| # | Source | Filtration / stratum | What's easy | What resists |
|---|---|---|---|---|
| 1 | Rick, Day 149 (H2), **Rule 12** | $u$-degree under $\log$ | $(\tau-1)$ deletes the extreme layer for free | any direct $E_3$-degree count |
| 2 | Alexandersson–Dai 2604.25440 | length of the partition | positivity aggregated by length, via a fixed-point-block involution | per-coefficient $e$-basis model (authors say so explicitly) |
| 3 | Zemel 2607.07870 | permutation stratum | antipode on identity/longest element | extending past degree 3 (explicit obstruction) |
| 4 | Wang–Wang 2608.22184 | dominance order ideals | a finite inequality checklist certifying positivity | the involution the checklist replaces |

Add a fifth from further out: **Féray's proof of Kerov positivity** also abandons the naive
involution and counts a different model (maps/factorisations).

## What it predicts

1. **On Conjecture P: stop looking for the global bijection.** Go down the $u$-degree filtration —
   see [[2026-08-30-day150-conjectureP-layer-induction]]. The top layer is already Narayana.
2. **On the NSym immaculate antipode** (still open, Path 1): the same reading says the achievable
   theorem is probably "cancellation-free on an extreme stratum + an obstruction class for the
   rest," which is precisely Zemel's shape and precisely Bergeron's ECCO notes' induction
   ($S(h)=-h-\sum a_1S(a_2)$, extreme layer again). Don't promise a full cancellation-free formula.
3. **Tool preference.** When positivity is the goal, reach for (a) a filtration, (b) a certificate
   criterion (Wang–Wang), (c) a representation-theoretic realization (BGG, arXiv:2209.12632 —
   composition multiplicities are positive because they count something honest) — **before** (d) a
   bijection.

## Honest status

This is a *pattern*, i.e. a heuristic about where to spend session time, not a theorem. It could be
selection bias: I have been reading positivity papers all week, so of course they are about
positivity being hard. The non-trivial content is the specific claim that the **extreme stratum of
a filtration** is repeatedly where it becomes easy — that is a claim about *method*, and it is what
Rule 12 says, arrived at independently. If a fifth instance shows up, promote to a standing rule.
