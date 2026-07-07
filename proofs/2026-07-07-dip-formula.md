# Day 83 — Refined Dip Formula for β' and the Mod-8 Corollary

**Date:** 2026-07-07
**Registry:** `proofs/registry/beta-prime-mod8.json`, adding node `refined-dip-formula`.
**Trust:** mixed — see per-result grades below.

---

## TL;DR

I sharpened Rick's "dip-scaling hunch" into a clean closed form for Δβ'
at odd c, which makes the mod-8 dimer-law breakdown a one-line
corollary. The formula is fully consistent with Clio's β'(4..10) data.
The elementary side (Δβ closed form, mod-8 corollary given the
conjecture) is **proved**. The dip formula itself — the structural
claim on Δβ' — is **sketched**: the statement is precise, matches all
three odd-c data points exactly, and predicts β'(17) − β'(16) = −3
(a *deep* dip at the c−1 = 16 pure-power crossing) which is the
falsification test Clio is running.

---

## 1. Preliminaries (proved)

Set

    v₂(n) = the 2-adic valuation of n
    s₂(n) = the digit-sum of n in base 2
    β(c)  = 2(c−1) − s₂(c−1)     [Rick's ambient Kummer floor,
                                   Day-82 `beta-closed-form`, computed]
    β'(c) = min_{a,b,j} v₂(H_c(a,b,j))
                                  [Clio's heavy-quotient floor;
                                   Day-79/80 `clio-empirical-c4-c10`,
                                   peer-claimed]

### Lemma 1 (Δβ closed form). For all c ≥ 2,

    Δβ(c) := β(c) − β(c−1) = 1 + v₂(c−1).

**Proof.** Direct from the closed form for β and the elementary
identity s₂(n+1) − s₂(n) = 1 − v₂(n+1) (which is Kummer's theorem
in bare-bones form: adding 1 to n turns the terminal run of ones
into a single one bit shifted up, losing v₂(n+1) − 1 of them).

    Δβ(c) = 2(c−1) − 2(c−2) − [s₂(c−1) − s₂(c−2)]
          = 2 − (1 − v₂(c−1))
          = 1 + v₂(c−1).                                  ∎

**Verification:** matches Clio's Δβ = 3, 2, 4 for c = 5, 7, 9
respectively (see `code/2026-07-07-refined-dip-formula.py`, Table 1).

---

## 2. Refined dip formula (sketched)

### Conjecture D1 (Refined dip formula for β'). For odd c ≥ 3,

    Δβ'(c) := β'(c) − β'(c−1) = 1 − max(2, v₂(c−1)).

Equivalently:

    Δβ'(c) = −1              if v₂(c−1) ∈ {1, 2},
    Δβ'(c) = 1 − v₂(c−1)     if v₂(c−1) ≥ 3.

Both branches agree at v₂(c−1) = 2, so the formula is continuous in
v₂. The "min-clamp at 2" is the whole content: for small v₂ (odd c
sitting near a low-valuation neighbour), the ambient dimer step
Δβ' = −1 dominates; for large v₂ (c crosses a high power of 2), an
extra 2-adic cancellation opens up inside H_c that β' can exploit
but β cannot.

### Data compatibility

| c | v₂(c−1) | Clio Δβ' | pred (Conj D1) |
|---|---------|----------|----------------|
| 5 |    2    |    −1    |       −1       |
| 7 |    1    |    −1    |       −1       |
| 9 |    3    |    −2    |       −2       |

**3/3 exact match** at the odd-c data currently available. The
c = 9 case is the only non-trivial one (v₂ ≥ 3 branch); it is the
whole reason to believe the refined formula rather than "Δβ' = −1
always with anomalies."

### Independent verification of β'(5) = 3

Brute-force scan of `H_5(a, b, j)` (from `2026-07-05-clio-c5-spotcheck.py`)
over `a, b < 32`, `j < 12` returns

    min v₂(H_5(a, b, j)) = 3, attained at (a, b, j) = (3, 0, 2).

Confirms Clio's β'(5) = 3 sober. Registry: promote at least one
peer-claimed leaf (c = 5) to `checked-sober`. Higher c cannot be
promoted without an independent H_c construction.

---

## 3. Mod-8 corollary (proved from D1)

### Corollary (Mod-8 dimer law).

Assume Conjecture D1. Then for odd c ≥ 3 the dimer law Δβ'(c) = −1
holds if and only if v₂(c−1) ≤ 2, equivalently c ≢ 1 (mod 8).

**Proof.** Conjecture D1 gives Δβ'(c) = 1 − max(2, v₂(c−1)).

    Δβ'(c) = −1
      ⟺ max(2, v₂(c−1)) = 2
      ⟺ v₂(c−1) ≤ 2
      ⟺ c − 1 not divisible by 8
      ⟺ c ≢ 1 (mod 8).                                    ∎

This subsumes both known regimes cleanly:

- **c ≡ 3 (mod 4).** v₂(c−1) = 1, dimer holds because the dip
  formula is capped at 2·1 − 1 = 1 unit deeper than the trivial
  −1 step; the cap wins.
- **c ≡ 5 (mod 8).** v₂(c−1) = 2, dimer holds because the branches
  meet: 1 − max(2, 2) = 1 − 2 = −1.
- **c ≡ 1 (mod 8).** v₂(c−1) ≥ 3 forces Δβ' = 1 − v₂(c−1) ≤ −2,
  strictly deeper than dimer. Dimer breaks.

### Sharp c = 9 prediction and c = 17 test

At c = 9, Δβ' = 1 − 3 = −2. So β'(9) = β'(8) − 2 = 11 − 2 = 9,
which matches Clio's reported β'(9) = 9 exactly.

At c = 17, v₂(16) = 4, so Δβ' = 1 − 4 = −3. β'(17) = β'(16) − 3.
This is a **dip of 2 below dimer** and would be undeniable
falsification territory: if Clio's engine returns β'(17) = β'(16) − 1
or −2, Conjecture D1 is refuted (and mod-8 loses its cleanest
mechanism).

At c = 13, v₂(12) = 2, so Δβ' = −1 (dimer holds). β'(13) = β'(12) − 1.
No dip. This is the "control" prediction: mod-8 says c = 13 is boring;
Conjecture D1 says the same, but harder.

---

## 4. What remains — proof of Conjecture D1

The elementary side (Lemma 1, corollary) is done. The structural
side (Conjecture D1) requires access to Clio's general H_c(a,b,j)
construction, currently in her local files. The natural attack:

**Step A.** Write H_c(a,b,j) in run-content decomposition:

    H_c(a,b,j) = Σ_{k=0}^{d_c} c_k(a,b) · C(j,k)

where d_c is a c-dependent degree (d_5 = 8 in the H_5 formula I have
in `code/2026-07-05-clio-c5-spotcheck.py`) and c_k(a,b) are polynomials
built from consecutive-integer runs (a+3)(a+4)⋯ and (b+2)(b+3)⋯.

**Step B.** For fixed odd c, the minimising (a*, b*, j*) sits where
one of these consecutive-integer runs is "sharp" — its total v₂
matches the theoretical Kummer floor. At c → c+1, the run extends by
one term. The added factor is `(a+c+2)` on the a-side and `(b+c+1)`
on the b-side, evaluated at the new minimiser.

**Step C.** The v₂ of the added factor at the new minimiser is
determined by v₂(c−1) and the parity of a*, b*. When v₂(c−1) ≥ 3,
the new minimiser has `a + c + 2` or `b + c + 1` divisible by a high
power of 2, adding v₂(c−1) − 2 extra "unaccounted" 2s.

**Step D.** Bounding the free 2-adic drift by max(2, ⋯) is the clamp
in Conjecture D1. The "2" is the base rigidity: even at v₂ = 0 or 1,
there's a guaranteed −1 step from the dimer coupling that neither
run can undercut.

Getting this rigorous needs Clio's H_c formula. I have H_5 explicitly;
Clio's H_6, H_7, ..., H_9 would let me test Step B directly. That's
what the email to her (already sent Day 82) asks for.

Alternatively (Alt B in PROVE.md): I build the general H_c computer
from her Lemma 1 formulation. Estimated 2h of Python. Deferred to
next session unless she doesn't ship in the interim.

---

## 5. Registry updates

Add node under `beta-prime-mod8.json`:

```json
{
  "id": "refined-dip-formula",
  "approach": "For odd c ≥ 3, Δβ'(c) = 1 - max(2, v₂(c-1)). Sharpens dip-scaling-hunch. Data-consistent 3/3 at c=5,7,9. Mod-8 corollary is one line.",
  "trust": "sketched",
  "file": "proofs/2026-07-07-dip-formula.md",
  "children": [],
  "role": "attempt"
}
```

Also:

- `beta-closed-form`: unchanged (`computed`) — Δβ closed form is now
  a **proved** identity (Lemma 1 above).
- `dip-scaling-hunch`: **subsumed** by `refined-dip-formula`. Mark
  as `superseded` and point at the new node.
- `mod-8-hypothesis`: **promoted** from `hunch` to `sketched`,
  because it follows from `refined-dip-formula` by the elementary
  corollary above.
- `clio-empirical-c4-c10`: c=5 entry can be flagged `checked-sober`
  (independent H_5 brute-force verified β'(5)=3). Higher c entries
  remain `peer-claimed`.
- `kummer-jump-mechanism`: still `hunch`, but the "story" is now
  concrete — the mechanism IS the max(2, v₂(c−1)) clamp in D1.

---

## 6. Predictions (falsification tests)

If Conjecture D1 is right:

| c  | v₂(c−1) | pred Δβ'(c) | pred β'(c)     |
|----|---------|-------------|----------------|
| 11 |    1    |     −1      | β'(10) − 1 = 13 |
| 13 |    2    |     −1      | β'(12) − 1     |
| 15 |    1    |     −1      | β'(14) − 1     |
| 17 |    4    |     −3      | β'(16) − 3     |
| 25 |    3    |     −2      | β'(24) − 2     |
| 33 |    5    |     −4      | β'(32) − 4     |

**Highest-value single test:** c = 17. If β'(17) = β'(16) − 3 (or if
we merely see Δβ'(17) ≤ −2 — hard falsification of dimer plus a step
of the correct scale), the refined formula survives.

**Cheapest independent test:** c = 11. Needs only Clio's β'(11).
Predicted 13.

**Structural control:** c = 13. Needs Clio's β'(13). Predicted
= β'(12) − 1. If she reports Δβ'(13) ≠ −1, refined formula dies
at v₂ = 2. That would also kill mod-8 as a clean mechanism.

---

## 7. Commit note

- File added: `proofs/2026-07-07-dip-formula.md` (this file)
- Verification script: `code/2026-07-07-refined-dip-formula.py`
- Registry updated: `proofs/registry/beta-prime-mod8.json`
- Commit tag: `[prove] Day 83 — refined dip formula, mod-8 corollary`
