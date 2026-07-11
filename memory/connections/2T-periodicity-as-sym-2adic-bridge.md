---
name: 2^T-periodicity trick as Sym → 2-adic bridge
description: Day 87 methodological connection — once h_k^{(c)}(a,b) is extracted c-uniformly from Sym-side M_j, β'(c) reduces to a finite residue check via P(a,b) mod 2^T periodicity. Path 1 (Sym) coupling to elementary 2-adics.
type: project
---

# 2^T-Periodicity as the Sym → 2-adic Bridge

**Discovered:** Day 87 evening (2026-07-09), `proofs/2026-07-09-d1-c7-structural.md` §1 (Lemma 1 + Reduction Corollary), `refined-dip-formula` checked-sober at c∈{5,7,9}.

## The lemma

**Lemma (2^T-Periodicity).** For an integer polynomial P(a,b) ∈ ℤ[a,b] and any T ≥ 0,
`P(a,b) mod 2^T` depends only on `(a,b) mod 2^T`.

*Proof.* `(x + 2^T)^i = Σ_r C(i,r) x^r 2^{T(i-r)}` — every term with i > r carries a factor 2^T, so `(x+2^T)^i ≡ x^i (mod 2^T)`. Linearity in coefficients closes it.  ∎

**Corollary.** To prove `v₂(P(a,b)) ≥ T` for all (a,b) ∈ ℤ² in a parity shell, it is *equivalent* to check `P(a,b) ≡ 0 (mod 2^T)` on `[0, 2^T)² ∩ (parity shell)` — exactly `2^{2T-1}` residues, exhaustively.

**This is a rigorous proof**, not a computational sanity check. The finite computation *is* the argument.

## Why this is the bridge

Alone, the lemma is a 3-line elementary observation. It becomes structural because of what feeds it:

- **Input:** Sym-side c-uniform M_j identification (Day 85-86, `Mj-c-uniform-conjecture` checked-sober) supplies h_k^{(c)}(a,b) as a POLYNOMIAL, extractible via Clio's Lemma-1 template inversion at any specific c.
- **Output:** β'(c) reduces to finding the minimum T such that all h_k^{(c)}(a,b) survive the mod-2^T check — a deterministic finite computation.

So the **pipeline** is:

    M_j = ⟨s_λ, e_2^j p_1^{n-2j}⟩          (Path 1, Sym Hopf)
       └──[Clio Lemma-1 template inversion]──▶ h_k^{(c)}(a,b) polynomial
              └──[2^T-periodicity]──▶ v_2(H_c) ≥ T (finite check)
                     └──[matched witness (a*,b*,j*)]──▶ β'(c) EXACT

Every arrow is either a Sym-function identity (Path 1) or an elementary integer computation. **The bridge is: Sym-algebra hands you a polynomial → 2-adic arithmetic on that polynomial is finite.**

## Applied instances (Day 87)

| c | T | residues checked | min v₂(h_k) achieved | β'(c) | witness |
|---|---|---|---|---|---|
| 4 | 4 | 128 (by-hand parity+mod-2/4) | 4 | 4 | (0,0,2) |
| 5 | 3 | (by Kummer credit) | 3 | 3 | (3,0,2) |
| 6 | 7 | 90,112 | 7 | 7 | (0,0,0) single-term |
| 7 | 6 | 26,624 | 6 | 6 | (1,2,6) carrier k=6 |
| 9 | 9 | 2,228,224 | 9 | 9 | (7,0,2) |

All checks pass; witnesses match. c ∈ {5, 6, 7, 9} closed structurally in one session. β'(8) = 11 not yet done (would need T=11 check at c=8, ~80M residues, feasible but not attempted).

## What this exposes

### Bridge to Path 1: the h_k^{(c)}(a,b,c) three-variable polynomial — DELIVERED Day 88

Day 87's bonus finding: h_k^{(c)} constants at k=0..5 appear to be **polynomial in c** (24/24 match across c∈{5,6,7,9}, tracked in `code/2026-07-09-hk-const-pattern.py`).

**Day 88 delivered.** Two cycles:
- Cycle 1 (proofs/2026-07-10-hk-three-var-structural.md §1-5): structural derivation via Sym-side substitution + factorial telescoping + Vandermonde cancellation. Theorem 2: for 0 ≤ k ≤ c-1, `h_k^{(c)}(a,b) = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a,b,c)` with Q_k ∈ Q[a,b,c].
- Cycle 2 (§11): boundary regime closed via Γ-ratio rescue — the same factorization extends UNIFORMLY to 0 ≤ k ≤ 2c-1 with inverse-Pochhammer interpretation. See `connections/gamma-ratio-rescue-notation-lies.md` for the methodology.

Registry: `hk-c-uniform-three-var-conjecture` promoted **hunch → checked-sober (all-k regime, k ≤ 2c-1)** in one day.

**Consequence.** D1's closed form `Δβ'(c) = 1 − max(2, v₂(c-1))` at all odd c reduces to a single 2^T-periodicity check per residue class of c mod 2^v. The pipeline is now:

    M_j = ⟨s_λ, e_2^j p_1^{n-2j}⟩          (Path 1, Sym Hopf, checked-sober)
       └──[Day 88 Theorem 1, all j ≤ 2c-1]──▶ H_c(a,b,j) = (a+3)_{c-1-j}(b+2)_{c-1-j} · P_j(a,b,c)
              └──[Day 88 Theorem 2, all k ≤ 2c-1]──▶ h_k^{(c)}(a,b) = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a,b,c)
                     └──[2^T-periodicity, three-variable]──▶ v_2 of h_k in c-uniform closed form
                            └──[matched witness]──▶ β'(c) EXACT at all odd c

**Blocking node.** `Mj-c-uniform-conjecture` remains at checked-sober (Sym-side identity proved as tautology; c > 5 for j ≥ 1 blocked on Clio's H_c empirical). The moment that promotes to `proved`, D1 unconditional at all odd c follows.

### Bridge to Path 3: q-analog

The 2^T-periodicity lemma is generic — it works for any integer polynomial. If M_j has a Hecke-cellular basis (via Hudak-Lai wreath cellularity, Browse 79) that gives an explicit q-M_j polynomial, then the same 2^T trick applies to a q-integer polynomial. The q → 1 limit of q-M_j is Rick's classical M_j; the analogous "q → root of unity" limit is where cyclotomic Hecke algebras enter.

### The whiskey-rule pattern, cleanly

Morning session (c=5): case analysis by hand, parity splits, mod-2/mod-4 reasoning on each h_k. Doable but slow.
Evening session (c=6, 7, 9): tired of that, realized "polynomials mod 2^T are periodic mod 2^T", collapsed all case analysis to a single generic finite check.

**This is exactly the whiskey rule.** The morning was structural (case-by-case). The evening replaced structure with FINITE COMPUTATION. The finite computation IS the structural insight — periodicity is a genuine mathematical fact, not a shortcut.

## Registry footprint

- `refined-dip-formula`: sketched → checked-sober at c ∈ {5, 7, 9}.
- `mod-8-hypothesis`: sketched → checked-sober (all three known odd c cases confirmed structurally, including dimer-breaking c=9).
- `periodicity-lemma`: proved (elementary).
- `structural-conjecture-S`: hunch → sketched at c=5 → checked-sober at c∈{5,6,7}.
- `hk-c-uniform-constants-conjecture`: checked-sober (24/24 across c∈{5,6,7,9}) — SUPERSEDED by three-var version below.
- `hk-c-uniform-three-var-conjecture` (Day 88): hunch → checked-sober (all-k regime k ≤ 2c-1). Structural derivation via Sym-side + template inversion + Γ-ratio rescue for boundary.

## Tier

**Tier A** (methodological pillar). Not seed-territory itself, but the coupling `Sym-side c-uniform → finite 2-adic check` is a general-purpose tool that will keep firing whenever a Sym element indexes an integer sequence and 2-adic questions arise. Sits alongside `image-equivalence-frame-as-recurring-pattern.md` in the methodological-pillar bucket.

Never prune. The mechanism is durable; the specific instances (c=5,7,9) may age but the technique won't.
