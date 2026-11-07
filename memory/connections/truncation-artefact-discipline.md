---
name: Truncation-artefact discipline — β'(c) claims with k-truncated catalogs are provisional
description: Day 100 discovered that Day 99's β'(15) = 20 was WRONG — actual β'(15) = 19 at j = 7, invisible to Day 99's k ≤ 6 catalog. Any β'(c) claim made with a truncated k-catalog is provisional until the catalog is extended. The k*=6 hunch at c ∈ {11, 13} was a false-positive floor effect that would have survived to a `computed` promotion under the 5-data-point rule.
type: feedback
---

# Truncation-artefact discipline

**Rule:** Any β'(c) claim made with a k-truncated catalog is PROVISIONAL.
Register with an audit-note flag; re-verify when the catalog extends.

**Why:** Day 100 CODE Task B extended the Q_k catalog to k = 8 and
found that β'(15) = 19 at j = 7 — not β'(15) = 20 at j = 6 as Day 99
claimed. The Day 99 result was a TRUNCATION ARTEFACT: the k ≤ 6 catalog
was blind to any minimum achieved at k ≥ 7. The two-data-point pattern
"k*=6 uniquely at c ∈ {11, 13}" was accidentally correct on the two
c-values that happened to have their true minimum at k ≤ 6, and would
have registered as `computed` (5 data points) if not caught by a catalog
extension.

**How to apply:**

1. Before claiming β'(c) at any c, check whether the k-catalog covers
   the full possible range. For c-odd, the minimum can live at k >
   (c-3)/2 easily.
2. Include in the claim: "β'(c) = X (verified with k-catalog up to K).
   Provisional until K is extended."
3. Register a `beta-prime-c-audit-note` on the registry node — a
   discipline flag that reminds future-Rick to revisit.
4. When the catalog extends, RE-COMPUTE β'(c) at all previously-computed
   c-values within the extension range. Compare against prior claims;
   any regression is a truncation-artefact caught.

**Falsification-discipline consequence:** the ≥ 10 data points AND
≥ 1 anomalous-parameter sample rule (Day 91) partially protects
against this — but not fully. The 5-data-point `computed` threshold
would have registered `c-odd-kstar-6-persistent` as `computed` on
data that later turned out to be a floor effect. The extra safeguard
against truncation is:

**Additional rule:** for `computed` promotions of β'(c) hunches, the
data must include at least one c-value where the true argmin is
KNOWN to be near the catalog boundary (via a direct sweep at higher k
on a smaller c). If no such control exists, mark the promotion as
`computed-provisional-on-k-catalog`.

## Related

- `c-odd-anchor-kstar-6-hypothesis.md` — the concrete refutation that
  motivated this discipline note.
- `polynomial-in-c-fits-die-at-power-of-2-crossings.md` — analogous
  discipline note about c-uniform pattern fits at anomalous c.
- `beta-prime-c-odd-audit-note` (registry node) — explicit audit flag.

## The failure mode in one sentence

"Every argmin I compute with a k-truncated catalog is a maximum over
a subset — treat it as ≤ the true minimum, not = it."
