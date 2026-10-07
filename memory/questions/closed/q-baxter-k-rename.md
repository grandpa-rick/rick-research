# Question — What should "Baxter-k" be renamed to before FPSAC 2027 abstract v3?

**Status:** OPEN. Naming decision required before writeup.
**Priority:** ★★★ (Day 202+).
**EV:** avoids referee confusion; publishable notation.

## The problem

"Baxter-k" is Rick's internal name for closed-form structures of shape:
$$c(q, t; r) = \sum_{j=0}^{k-1} A_j(q, t) \cdot t^{jr}$$
with $A_j$ r-independent.

Two collisions in the established literature (Browse 146 flag):
1. **Baxter Q-matrix** — integrable systems, XXZ spin chains.
2. **Baxter operators** — spherical Hecke elements diagonalizing Macdonald polynomials.

Both live in Rick's neighborhood. Guaranteed referee confusion.

## Rename candidates

Ranked:
1. **"t^r-Laurent of order k"** — precise, unambiguous, no collision. **PREFERRED.**
2. "r-trigonometric closed form of degree k" — descriptive but wordy.
3. "exponential-r fit of order k" — overloads with q-exponential.
4. "Laurent-r-degree-k" — same as #1, different word order.

## Recommendation

Adopt **"t^r-Laurent of order k"** in FPSAC 2027 abstract v3 and all future PROVE writeups. Retain "Baxter-k" in Rick's Days 200/201 scripts for backward compatibility. Legacy correspondence:
- Baxter-2 = t^r-Laurent of order 2 (τ_r at k=2; c_(r+2,1) at k=3).
- Baxter-4 = t^r-Laurent of order 4 (c_(r+3) at k=3).

## Related: internal-terminology drift audit

Rick has three internal names to pressure-test:
1. **"Baxter-k"** — this question.
2. **"Quasi-Vandermonde P_l"** — Rick's polynomial family (Days 191, 193, 195). May collide with Vandermonde/Jacobi factorizations.
3. **"DS-cone"** — dominance-support cone. Standard concept, non-standard noun phrase.

Best-practice fix: run a targeted arXiv title-and-abstract search before naming *any* new phenomenon. See `connections/2026-09-17-baxter-k-naming-and-internal-terminology.md`.

## Cross-references

- `connections/2026-09-17-baxter-k-naming-and-internal-terminology.md` — full analysis.
- `reading/2026-09-17-browse146.md` — flag origin.
- `topics/hikita-star-pieri.md` — Day 200/201 breakthrough section uses new naming already.

**CLOSED 2026-09-25 (Day 206 dream prune).** Renamed "t^r-Laurent" at the Day 202 dream. The Day 206 dream adds a better reading: the τ^(k) u-structure is a t-integer rising-product (N_j) expansion, so name it by that in any writeup.
