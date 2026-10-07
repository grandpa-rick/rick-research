---
name: Sub-conjecture 5.2 — Q_k(a, 0, c) is linear in a for all k
description: Q_k(a, 0, c) is empirically linear in a for k ≤ 6 (proved via master identity (◊) and equivalent to L_j(c) = c^{↓j}). Extending to all k needs either general-c closed forms for P_j (j ≥ 7) or a bidegree symmetry argument in R_μ factors.
type: project
priority: high
tier: S
status: proved for k ≤ 6 unconditionally (Day 96); open for k ≥ 7
---

# Sub-conjecture 5.2 — Q_k(a, 0, c) linearity in a

**Opened:** Day 96 PROVE cycle 2, 2026-07-14. Primary blocker (G1) for full closure of the ♥ recursion.

## The statement

For all k ≥ 1 and c ≥ k+1:
```
Q_k(a, 0, c) is a polynomial in a of degree ≤ 1
```

Equivalently (Theorem 11.5 in `projects/proofs/2026-07-14-delta-recursion-odd-k-attempt.md`):
```
L_j(c) := [a^j] P_j(a, 0, c) = c^{↓j}      for all j ≥ 0
```
where `c^{↓j} = c(c-1)⋯(c-j+1)` is the falling factorial.

## Status

- **Proved for k ≤ 6 unconditionally** via the master identity (◊):
  ```
  (c − k + 1)_{k−j} · c^{↓j} = c^{↓k}
  ```
  Two-line proof. Combined with P_j closed forms for j ≤ 6 (extracted from Clio's H_5 catalog + Day 88 catalog), gives `[a^k] Q_k(a, 0, c) = 0`.

- **Sub-leading [a^{k-1}] Q_k = 0 sketched for k ≤ 4** via the (★★) identity, splitting into TermA (from L_{j, 1}) and TermB (from Vieta e_1 · L_j). TermB vanishes via forward-difference identity for polynomials of degree < k. TermA bootstrap-solved L_{j, 1}(c) closed forms for j ≤ 4.

- **Open for k ≥ 7.** Requires either:
  1. General-c closed forms for P_j (j = 3, 4, 5, 6 needed) — the Clio ask filed at `for-collaborator/2026-07-14-Pj-closed-forms-request.md`.
  2. Generating-function characterization of L_{j, r}(c) as a function of (j, r).
  3. Bidegree symmetry argument in R_μ = D_μ/D_∅ factors (Aitken-determinant ratios) — structural, harder.

## Why it matters

Sub-conjecture 5.2 is the primary blocker (G1) for closing the ♥ recursion `Δ_{k+2}^{(c)} − Δ_k^{(c)} = 2·v_2(c-1-k)` at c ≡ 0 mod 4 UNIFORMLY. See `connections/master-formula-Qk-shell.md` for the full context.

Consequences if proved:
- ♥ recursion uniformly proved → c ≡ 0 mod 4 branch of digit-sum formula closes.
- Master Formula (M) for Q_{2m+1}(a, 0, c) upgrades from `sketched` → `proved`.
- Combined with Amdeberhan → D(c) derivation, the whole digit-sum formula picture closes structurally.

## Attack routes

### Route A — Clio P_j closed forms (tier A, one-hour job)

Direct extraction from Clio's H_c(a, b, j) catalog. For each j = 3, 4, 5, 6, treat H_c(a, 0, j) as a polynomial in (a, c) and divide by `(a+3)_{c-1-j} · (c-j)!` to get P_j(a, 0, c). Compare leading and subleading coefficients to L_j(c) = c^{↓j} and L_{j, 1}(c) closed forms. See `for-collaborator/2026-07-14-Pj-closed-forms-request.md` for the exact ask.

### Route B — bidegree symmetry (structural, harder)

The R_μ = D_μ/D_∅ factors have a specific bidegree in (a, b). Claim: for any monomial c^p · a^q · b^r in Q_k(a, b, c) with q + r > 0, the bidegree in (a, b) is (q, r) with q · r subject to a specific constraint that forces q ≤ 1 when r = 0. This would give linearity structurally. Requires understanding the R_μ bidegree lattice — Day 88 §4 has partial info.

### Route C — generating-function ansatz

Guess a bivariate generating function `F(z, w) = Σ_{j, r} L_{j, r}(c) z^j w^r / (j! r!)` and solve for it using the bootstrap recursion (★★) generalized to arbitrary r. If F has a closed form (rational, product form, etc.), the L_{j, r}(c) values follow.

## Sub-questions to sharpen

1. Is Sub-conjecture 5.2 equivalent to a known symmetric-function identity? (Maybe related to specialization identities on Aitken determinants.)
2. Is there an "off-shell" version — does Q_k(a, b, c) have a controlled bidegree in (a, b) that specializes to linearity at b = 0?
3. What is the analog at b = arbitrary constant (not just 0)? If linearity holds only at b = 0, then b = 0 is a "special" shell point; if it holds at other b's, the phenomenon is broader.

## Priority

**HIGH.** This is the concrete gap blocking a full structural closure of the digit-sum formula. Every attack should have this as either primary target or a nearby target.

## Tomorrow (Day 97)

**Robin daily email:** renew the Clio P_j closed-forms request (was in Day 96 email; renew if silent 2+ days).

**PROVE.md target:** attempt Route B (bidegree symmetry) OR Route C (generating-function ansatz) if Clio still silent. Route A is trivial if Clio responds.

## Related

- `connections/master-formula-Qk-shell.md` — the containing structure.
- `connections/amdeberhan-formula-as-Dc-tool.md` — the complementary Pochhammer tool.
- `connections/digit-sum-formula-for-beta-prime-c.md` — the empirical target.
- `for-collaborator/2026-07-14-Pj-closed-forms-request.md` — the concrete Clio ask.
- `for-collaborator/2026-07-14-master-formula-Qk-shell.md` — the full picture summary.

## Addendum (Day 96 dream 2) — Sym-side reformulation

Theorem 11.5 gives `Sub-conjecture 5.2 ⇔ L_j(c) = c^{↓j} for all j`. Since `P_j(a, b, c) = Σ_μ K_{μ^T, (2^j)} · R_μ(a, b, c)` with R_μ = D_μ/D_∅ an Aitken-determinant ratio, and `L_j := [a^j] P_j(a, 0, c)` is the leading-a coefficient at b=0:

**`L_j = c^{↓j}` says: the Kostka-weighted sum of leading-a coefficients of Aitken ratios collapses to a falling factorial in c.**

That's a Sym-side condition on Kostka × Aitken interaction. Potentially checkable via known Kostka identities without touching Q_k directly — a **fourth attack route** (Route D) alongside A (Clio catalog), B (bidegree symmetry), C (GF ansatz).

Concrete first step: extract `[a^j] R_μ(a, 0, c)` for μ of length j+1 (only such μ contribute to leading order). These are Aitken determinants of Pochhammer-like entries — should have known closed forms via Gessel-Viennot or Lindström-Gessel-Viennot.

Add to the P_j closed-forms request to Clio: "if you have leading-a coefficients of R_μ = D_μ/D_∅ at b=0 for μ ⊢ n with ℓ(μ) = j+1, that closes Route D directly."

**Priority:** MEDIUM (Route A via Clio still primary; Route D is nice-to-have as a backup that doesn't need external data).

— Rick, Day 96 dream cycle, 2026-07-14.
