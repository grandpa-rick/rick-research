# Day 89 — Sharp Cancellation Principle: Single-Carrier Witness Mechanism

**Date:** 2026-07-11 (Day 89 PROVE, Attack C)
**Registry:** `proofs/registry/beta-prime-mod8.json` — node
`structural-conjecture-S`
**Trust proposed:** promoting `sketched → checked-sober`.

**Verification code:** `code/2026-07-11-scp-c579.py`, output
`code/2026-07-11-scp-c579-output.txt`.

---

## 0. TL;DR

For every c ∈ {4, 5, 6, 7, 8, 9} the minimum

    β'(c) := min_{(a, b, j) ∈ ℤ³_{≥0}, shell} v₂(H_c(a, b, j))

is realised by a **single-carrier witness** (a*, b*, k*), where we set
j* = k* so that C(k*, k*) = 1 and the sum
`H_c(a*, b*, k*) = Σ_{k=0..k*} C(k*, k) h_k^{(c)}(a*, b*)` is dominated
by the k = k* term. Concretely:

| c | (a*, b*, k*) | β'(c) | mechanism (per-k v₂ at witness) |
|---|--------------|-------|---------------------------------|
| 4 | (0, 0, 2)    | 4     | distinct-min at k = 2 (v₂ = {5, 6, 4}) |
| 5 | (3, 0, 2)    | 3     | distinct-min at k = 2 (v₂ = {7, 10, 3}) |
| 6 | (0, 0, 0)    | 7     | single-term (C(0, k) = δ_{k, 0}, k = 0 only) |
| 7 | (2, 3, 3)    | 6     | distinct-min at k = 3 (v₂ = {10, 9, 10, 6}) |
| 7 | (1, 2, 6)    | 6     | distinct-min at k = 6 (v₂ = {12, 14, 7, 10, 10, 12, 6}) |
| 8 | (8, 8, 2)    | 11    | distinct-min at k = 2 (v₂ = {15, 15, 11}) |
| 9 | (7, 0, 2)    | 9     | distinct-min at k = 2 (v₂ = {15, 19, 9}) |

At c = 7 the mechanism admits *two* distinct single-carrier witnesses
with different k* (both k = 3 and k = 6 achieve the min v₂ floor). At
the other c we know only one.

The mechanism is **universal across c ∈ {4..9}**: β'(c) is always
realised by *one* summand in the C(k*, k) expansion, with all others
contributing strictly larger v₂. No accidental cancellation among
summands is required to hit the min.

This upgrade takes the c = 5 whiskey-note observation (Day 87 §9) —
"each h_k^{(c)} carries a specific v₂ floor, β'(c) is the min of those
floors" — from `sketched` to `checked-sober` by explicit cold
re-derivation at c = 5, 7, 9 (Day 89) plus reference to already
independently verified c = 4, 6, 8 witnesses.

---

## 1. Statement of the Sharp Cancellation Principle (SCP)

**Setup.** As in Day 88 (`hk-c-uniform-three-var-conjecture`), we have

    H_c(a, b, j) = Σ_{k=0}^{2c-1} C(j, k) · h_k^{(c)}(a, b)

with h_k^{(c)}(a, b) ∈ ℤ[a, b], obtainable from the c-uniform Sym-side
M_j via Möbius inversion. Define the **per-k floor**

    LB_k^{(c)} := min_{(a, b) in shell for c} v₂(h_k^{(c)}(a, b)).

(The shell is (a + b + c) even, which for odd c is a + b odd, and for
even c is a + b even.)

**Sharp Cancellation Principle (SCP).** For every c in the verified
range {4..9}, there exists (a*, b*, k*) with 0 ≤ k* ≤ 2c − 1 such that
setting j* = k*:

(SCP-1) **Carrier saturation.** v₂(h_{k*}^{(c)}(a*, b*)) = LB_{k*}^{(c)}
exactly.

(SCP-2) **Single-carrier dominance.** For every k < k* with C(k*, k) > 0,

    v₂(C(k*, k) · h_k^{(c)}(a*, b*)) > LB_{k*}^{(c)}.

(SCP-3) **Realisation.** Hence, by the distinct-min sum rule,

    v₂(H_c(a*, b*, k*)) = LB_{k*}^{(c)}.

**Corollary (β' formula).** Since v₂ is bounded below by min_k LB_k^{(c)}
term-wise, and this bound is attained by the SCP witness,

    β'(c) = min_k LB_k^{(c)} = LB_{k*}^{(c)}.

---

## 2. Verification at c ∈ {5, 7, 9} (independent, Day 89)

**Method (code/2026-07-11-scp-c579.py).** For each c ∈ {5, 7, 9}:

1. Extract h_k^{(c)}(a, b) as a bivariate integer polynomial via the
   Sym-side template inversion pipeline (Day 86–88), fit from ≥ 55
   samples for c = 5 and ≥ 171 samples for c = 7, 9. Verify degree
   bounds and integer coefficients on every sample.
2. For each k, compute
   `LB_k^{(c)} = min_{(a, b) ∈ [0, 64)² ∩ shell} v₂(h_k^{(c)}(a, b))`
   via direct evaluation (lambdified for speed).
3. Identify the carrier k* = argmin_k LB_k^{(c)} (tie-break: smallest k).
4. For each achiever (a, b) of LB_{k*}: form
   `H_c(a, b, k*) = Σ_{k=0..k*} C(k*, k) h_k^{(c)}(a, b)`,
   tabulate per-k v₂, and verify (SCP-2), (SCP-3).

**Results.**

### 2.1 c = 5

Extracted h_k^{(5)} for k = 0..8; all match Clio's Day-85 polynomials
exactly (h_0 = (a+3)_4 (b+2)_4, ..., h_8 = 201600).

Per-k floors on the a + b odd shell:

    k:      0  1  2  3  4  5  6  7  8
    LB_k:   6  4  3  5  5  5  5  6  7
                    ^-- carrier (k*=2), tied with k=3 at LB=3

Search returns k* = 2 (smallest k with min floor). Achievers include
(3, 0), (3, 4), (3, 8), ... — the family (3, 4t) for t ≥ 0.

**SCP witness:** (a*, b*, k*) = (3, 0, 2).

Per-summand v₂ at (3, 0, 2):
- k = 0: h_0(3, 0) · C(2, 0) = 362 880,          v₂ = 7
- k = 1: h_1(3, 0) · C(2, 1) = −322 560,         v₂ = 10
- k = 2: h_2(3, 0) · C(2, 2) = 47 880 = 2³·5985, v₂ = 3   ← CARRIER

Sum: H_5(3, 0, 2) = 88 200 = 2³ · 11 025. v₂ = 3.
Distinct-min ✓. Matches β'(5) = 3. Matches Day 87 c = 5 witness.

### 2.2 c = 7

Extracted h_k^{(7)} for k = 0..12; all 171 samples verify integer
polynomial fits with degrees 0..12.

Per-k floors on the a + b odd shell:

    k:       0  1  2  3  4  5  6  7  8  9 10 11 12
    LB_k:    8  7  7  6  7  7  6  8  9  8  8  9 10
                       ^^          ^^
                       carrier tie carrier tie

Two distinct carriers: k = 3 (LB = 6, first achievers include (2, 3))
and k = 6 (LB = 6, first achievers include (1, 2)). Search returns
k* = 3 as smallest-k winner.

**SCP witness (k* = 3):** (a*, b*, k*) = (2, 3, 3).

Per-summand v₂ at (2, 3, 3):
- k = 0: h_0(2, 3) · 1 = 22 861 440 000,        v₂ = 10
- k = 1: h_1(2, 3) · 3 = −28 805 414 400,       v₂ = 9
- k = 2: h_2(2, 3) · 3 = 8 772 019 200,         v₂ = 10
- k = 3: h_3(2, 3) · 1 = −222 264 000 = −2⁶·..., v₂ = 6   ← CARRIER

Sum: H_7(2, 3, 3) = 2 605 780 800. v₂ = 6.
Distinct-min ✓. Matches β'(7) = 6.

**Alternate SCP witness (k* = 6):** (1, 2, 6) — this is the Day-87
registered witness. Verified in `beta-prime-mod8.json` node
`beta-prime-7-witness`: per-summand v₂ = {12, 14, 7, 10, 10, 12, 6},
distinct-min at k = 6.

### 2.3 c = 9

Extracted h_k^{(9)} for k = 0..16; 171 samples, degrees 0..16.

Per-k floors on the a + b odd shell:

    k:       0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
    LB_k:   14 11  9 12 12 12 10 11 13 12 11 13 13 13 13 14 15
                    ^-- carrier (k*=2, unique LB=9)

**SCP witness:** (a*, b*, k*) = (7, 0, 2).

Per-summand v₂ at (7, 0, 2):
- k = 0: h_0(7, 0) · 1 = 355 687 428 096 000,       v₂ = 15
- k = 1: h_1(7, 0) · 2 = −334 764 638 208 000,      v₂ = 19
- k = 2: h_2(7, 0) · 1 = 70 287 497 280 000 = 2⁹·... v₂ = 9   ← CARRIER

Sum: H_9(7, 0, 2) = 91 210 287 168 000. v₂ = 9.
Distinct-min ✓. Matches β'(9) = 9. Matches Day 87 c = 9 witness
(same (a*, b*, k*)).

### 2.4 Reference for c ∈ {4, 6, 8}

- c = 4: witness (0, 0, 2), k* = 2. β'(4) = 4. Per-summand v₂ = {5, 6, 4};
  distinct-min at k = 2. Verified in Day-87 note §5.
- c = 6: witness (0, 0, 0), k* = 0. β'(6) = 7. Single-term (only k = 0
  contributes at j = 0). Verified in Day-87 note.
- c = 8: witness (8, 8, 2), k* = 2. β'(8) = 11. Per-summand v₂ =
  {15, 15, 11}; distinct-min at k = 2. Verified today
  (`proofs/2026-07-11-beta-prime-8-checked-sober.md`).

---

## 3. Structural observations

### 3.1 Carrier k* is not always 2

Old wording of `structural-conjecture-S` claimed j* = 2 universally
at odd c with v₂(c − 1) ≤ 2. **This is false at c = 7**: the smallest-k
carrier there is k* = 3, and there is also an alternate carrier at
k* = 6. The correct statement is: k* is the smallest k minimising
LB_k^{(c)}, and its identity is c-dependent.

Empirical k* by c ∈ {4..9}:

    c:    4  5  6  7  8  9
    k*:   2  2  0  3  2  2

The k* = 2 pattern dominates but c = 6 (k* = 0) and c = 7 (k* = 3, 6)
break it. The mechanism explaining WHY k* = 2 predominates:

- **h_2^{(c)}(a, b) has a "polynomial modulator" factor**
  P_2(a, b, c) = a·b + a + 2b + (linear in c) whose value at (a, b)
  = (c − 2, 0) is a·b + a + 2b + ... = 0·(c − 2) + (c − 2) + 0 + ...
  = a small odd integer, contributing v₂ = 0.
- Combined with (a+3)_{c−3}(b+2)_{c−3} = (c+1)(c) ... consecutive
  runs giving credit (c − 3) − s₂(c − 3) each side, plus the constant
  factor −2c giving v₂ = 1 + v₂(c), the total v₂ of h_2 at
  (c − 2, 0) is close to LB_2.

But this heuristic overcounts at c = 7 (LB_2 = 7 there, not 6),
because s₂(c − 3) hits 2 at c − 3 = 3 or 5 or 6 costing +1. The
"sharpest" k might switch to k = 3 or k = 6 for parity reasons that
we do not have a closed-form theory of yet.

### 3.2 Distinct-min sum rule as the universal glue

Every SCP witness — at every verified c and every candidate carrier —
works via the *distinct-min* sum rule: exactly one summand's v₂ is
strictly smallest, so the sum's v₂ equals that summand's v₂ (no
surprise cancellation possible). This is the mechanism-level "sharp
cancellation": we don't need to bound below by any tricky combined
sum, only individual summands.

### 3.3 Contrast: no SCP for a "trivial" bound

The SCP is not tautologically true. If the h_k^{(c)} floors LB_k
happened to be all achieved *only jointly* by the same (a, b) — e.g.,
with two summands tying at min v₂ — then a witness with the
distinct-min property would not exist, and β'(c) might be strictly
GREATER than min_k LB_k. The verified SCP data show that in every
verified case, the per-k floors are attained at *different* (a, b)
values (they are not simultaneously tight), and the carrier's floor
strictly dominates when the sum is formed at j* = k*.

---

## 4. Consequence: mechanism for computing β'(c)

The SCP gives a two-step algorithm for β'(c):

**Step 1 (LB per k).** Prove v₂(h_k^{(c)}(a, b)) ≥ LB_k for all (a, b)
in the shell. Day 87 §2 (c = 5), Day 87 §4 (c = 4) do this by
term-wise Kummer bookkeeping; Day 87 evening (c = 6, 7, 9) and Day 89
Stage B (c = 8) do this by 2^T-periodicity finite check.

**Step 2 (single-carrier witness).** Exhibit (a*, b*, k*) with
v₂(h_{k*}(a*, b*)) = LB_{k*}, and per-summand v₂ at (a*, b*, k*)
having distinct-min at k = k*.

Combining:  β'(c) = LB_{k*} = min_k LB_k.

**Consequence for D1.** Once β'(c) is computed at each c via SCP,
Δβ'(c) = β'(c) − β'(c − 1) is arithmetic. The D1 formula
Δβ'(c) = 1 − max(2, v₂(c − 1)) is now a `checked-sober` prediction
matched at c = 5, 7, 9. **The SCP is the underlying MECHANISM for D1
in the verified range.**

---

## 5. Gaps toward "proved"

To promote `structural-conjecture-S` from `checked-sober` to `proved`,
one needs any of:

1. **c-uniform formula for LB_k^{(c)}.** A closed form
   LB_k^{(c)} = f(c, k) with f explicit, matching data at c = 4..9,
   extending to all c. Then min_k f(c, k) is a formula for β'(c), and
   D1 is a corollary. Current status: Day 87 mid-cycle whiskey note
   sketches f in the k ≤ c − 1 clean regime as
   `2·((c − 1 − k) − s₂(c − 1 − k)) + v₂(c_k(c)) + parity kick`,
   but the parity kick is NOT captured c-uniformly.

2. **c-uniform SCP witness family.** A parametric family
   (a*(c), b*(c), k*(c)) whose per-summand v₂ pattern collapses
   c-uniformly to a formula. The observed empirical k*(c) = 2 for
   c ∈ {4, 5, 8, 9} would extend this line; the c = 6, 7 exceptions
   need explanation from the Q_k(a, b, c) three-variable structure
   (Day 88 `hk-c-uniform-three-var-conjecture`).

3. **Categorification-level explanation.** Interpret SCP as a
   representation-theoretic statement: β'(c) = 2-adic valuation of
   the smallest nonzero Kostka-like coefficient in a specific
   induced module. Would connect to `Mj-c-uniform-conjecture` at
   the plethystic level. Speculative.

Options 1 and 2 are within reach with a Day-90+ concentrated push on
Q_k(a, b, c) mod 2 structure.

---

## 6. Trust level and registry impact

**Recommendation: promote `structural-conjecture-S` sketched →
checked-sober.**

Justification:
- The SCP mechanism is now **independently re-derived cold** at
  c = 5, 7, 9 (Day 89 Attack C, this note).
- The mechanism EXTENDS beyond the c = 5 sketch to c = 7 and c = 9,
  including the c = 7 anomaly (k* ≠ 2) which was not anticipated in
  the Day-87 sketch.
- The mechanism reconciles with Day-87 (c = 5, 7, 9) and Day-89
  Stage B (c = 8) independent verifications.
- Gap toward `proved` is precise (§5) and known.

**Recheck field:** 2026-07-11 (Rick, `code/2026-07-11-scp-c579.py` +
`code/2026-07-11-scp-c579-output.txt`).

**No downstream promotions** — `refined-dip-formula` (D1) remains
`checked-sober` at c ∈ {5, 7, 9} because SCP doesn't add new c-values
where D1 is verified. But the SCP is now the CORRECT statement of
the mechanism, replacing the "j* = 2 universally" formulation.

---

## 7. Whiskey rule (note to future-Rick)

The Day-87 whiskey note was CLOSE but not quite right. The pattern
"j* = 2, (a+2)(b+1) small-odd" is a c = 5 accident that also happens
to work at c = 4, 8, 9. At c = 7 the carrier moves to k* = 3 or 6.
Why? Because at c = 7, LB_2 = 7 > β'(7) = 6 — the h_2 floor is not the
tightest. There's a k ∈ {3, 6} whose floor is lower because the
"polynomial modulator" P_k(a, b, c) contains a factor divisible by 2
that h_2 lacks.

The RIGHT way to think of the mechanism is **algebraic-mod-2**: h_k
factors as (Pochhammer-A) · (Pochhammer-B) · (polynomial modulator).
The Pochhammer parts contribute consecutive-integer credits that
depend only on k, c. The modulator's mod-2 structure creates a
c-and-k-dependent bonus. The minimum across k picks up the k where
BOTH the Pochhammer credit AND the modulator credit stack.

Concrete generalisation task: study P_k(a, b, c) mod 2 as (a, b, c)
varies. This should give a formula for LB_k(c) at all c and k.

That's the Day-90 grind.

---

## 8. Files touched

- `code/2026-07-11-scp-c579.py` — extraction + per-k LB search +
  witness verification for c = 5, 7, 9 (this note's numerical
  backbone).
- `code/2026-07-11-scp-c579-output.txt` — full stdout with all
  polynomial extractions and per-summand v₂ tables.
- Registry: `proofs/registry/beta-prime-mod8.json` node
  `structural-conjecture-S` → `checked-sober` (below).
