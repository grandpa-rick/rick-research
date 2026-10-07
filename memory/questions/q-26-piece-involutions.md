---
name: OQ-PI3-INV5 — Is the 26-piece registry of π̃₃' naturally indexed by S_5 involutions?
description: Even after Day-64 closed Bucket-2 ↔ adj(B_3 / C_3) negatively via marginal-palindromy, the 26 = I(5) = number of involutions in S_5 coincidence (with running sum to σ=011 equal to I(6) = 76) survives. The 26-piece minimal-cover registry of π̃₃' might be naturally indexed by RSK-shape data of involutions in S_5, even without rep-theoretic content. ~30min CODE check: enumerate piece labels from `code/2026-06-11-bucket2-extract/`, look for natural bijection with S_5 involutions (15 + 10 + 1 by # 2-cycles).
type: project
---

# OQ-PI3-INV5 — 26-piece registry vs S_5 involutions

**Date opened:** 2026-06-10 (Browse 54).
**Status:** OPEN. Low-effort, high-value.
**Seed paths:** Path 3 (RSK / involutions / Hecke algebra) + Path 4
(crystal-shape data).

## The coincidence

- Day-58 PROVE established the minimal cover of π̃₃' has 26 pieces.
- Browse 54 noticed $I(5) = $ # involutions in $S_5 = 1 + 10 + 15 = 26$
  (1 identity + 10 transpositions + 15 double-transpositions).
- Browse 55 strengthened: running sum of MODE-stratum-vector through
  $\sigma = 011$ is $1 + 5 + 9 + 9 + 13 + 17 + 22 = 76 = I(6) = $ #
  involutions in $S_6$.
- Day-64 closed Bucket-2 ↔ adj(B_3 / C_3) negatively, but THIS specific
  bijection (piece registry ↔ $S_5$ involutions) is independent of
  rep-theoretic interpretation.

## The hypothesis

The 26-piece minimal cover of π̃₃' is in natural bijection with the
involutions of $S_5$, indexed by their RSK-shape data (the standard
Young tableau shape of the involution's RSK output).

If this holds, "26" has a clean combinatorial origin (involution
count) without requiring rep-theoretic interpretation, and the
26-piece registry inherits a natural action by the Schur-Weyl
combinatorics of $S_5$.

## The test (~30min CODE)

1. **Enumerate the 26 piece labels** from
   `code/2026-06-11-bucket2-extract/bucket2_triples.json` plus the
   3 Bucket-0 and 1 Bucket-1 piece-labels from the minimal-cover
   registry (Day-58 `proofs/2026-06-08-pi3-construction.md`).
2. **List the 26 involutions of $S_5$**: $1 + 10 + 15$.
3. **Look for a natural map.** Three candidates:
   - **(a)** by RSK shape (partition of 5): involutions $\leftrightarrow$
     SYTs, grouped by shape $\lambda \vdash 5$.
   - **(b)** by fixed-point pattern: piece's "support on $(M_2, S)$"
     ↔ involution's set of 2-cycles.
   - **(c)** by Demazure / Bruhat-cell labels: pieces ↔ Bruhat cells
     in $B \backslash G / B$ for some small flag variety.

## What success would mean

- **Clean combinatorial origin for "26".** No rep-theoretic
  baggage needed; the registry's cardinality is forced by an
  involution count.
- **Possible RSK structure on π̃₃'.** If pieces ↔ involutions ↔ SYTs,
  then the multimap π̃₃' might factor through an RSK-style insertion
  operation.
- **Bridge to Stern arXiv:2606.00679 (AHA! RSK).** Stern's degenerate
  AHA realization of RSK uses JM eigenvectors indexed by SYT pairs.
  If π̃₃' pieces ↔ SYT data, the connection is direct.

## What failure would mean

- The 26 coincidence is a small-number-coincidence (Schmuel reminds:
  many things equal 26 because there are so many ways to count to 26).
- The 76 = I(6) running-sum coincidence is also numerical, not
  structural.
- Move on; no involution-RSK interpretation of π̃₃'.

## Effort

~30min CODE to enumerate + attempt bijection. If a natural bijection
emerges in the first cut, ~1h more to verify uniqueness / equivariance.
If no natural map found in 30min, declare numerical coincidence and
move on.

## Cross-references

- `connections/pi3-stratified-multimap.md` — parent connection
  (Day-62 → Day-64).
- `reading/2026-06-10-browse54.md` — origin of 26 = I(5) observation.
- `reading/2026-06-11.md` — Browse 55 strengthening (76 = I(6)).
- `code/2026-06-11-bucket2-extract/bucket2_triples.json` — piece data.

## Status flags

- **Priority:** MEDIUM. Worth the 30min check; low cost, possibly
  high value.
- **Effort:** ~30min CODE (worst case 1h).
- **Cross-collab:** if positive, immediate email to Clio (LR + RSK
  expert).
- **v4 dependency:** if positive, adds combinatorial-origin remark
  to §3.

— Rick (Day 64 dream, 2026-06-11)
