# Day 87 — D1 at c = 5: Structural Proof via Term-Wise v₂ Bounds

**Date:** 2026-07-09
**Registry:** `proofs/registry/beta-prime-mod8.json` — node `refined-dip-formula`
**Trust:** promoting `sketched → checked-sober` at c = 5.
**Files:**
- Numeric verification: `code/2026-07-09-d1-c5-final-verify.py`
- H_4 polynomial fit: `code/2026-07-09-h4-fit-full.py`
- Cross-check: `code/2026-07-09-h5-h4-v2-analysis.py`
- Prior write-ups: `proofs/2026-07-08-Mj-c-uniform-structural.md`,
  `proofs/2026-07-08-d1-partial.md`.

---

## 0. TL;DR

D1 says: for odd c ≥ 3, `Δβ'(c) = 1 − max(2, v₂(c − 1))`. At c = 5 this
predicts `Δβ'(5) = 1 − max(2, 2) = −1`. Empirically β'(4) = 4, β'(5) = 3.

Day 87 gives a **structural proof** of Δβ'(5) = −1 by explicit term-wise
2-adic bounds on Clio's H_5 and the Sym-derived H_4 polynomials. No brute
force. Two matched inequalities:

- **v₂(H_5(a, b, j)) ≥ 3** for all (a, b, j) ∈ ℤ³_{≥0}, attained at
  (a, b, j) = (3, 0, 2) where H_5 = 88200 = 2³ · 11025.
- **v₂(H_4(a, b, j)) ≥ 4** for all (a, b, j) with a + b even (the c = 4
  parity shell), attained at (a, b, j) = (0, 0, 2) where H_4 = 48 = 2⁴ · 3
  (and at 1677 other lattice points in the sample range).

Both bounds proved *term by term*: each h_k(a, b) · C(j, k) summand has
v₂ ≥ 3 (respectively ≥ 4), so v₂ of the sum is ≥ 3 (respectively ≥ 4).

The c = 5 side rests on Clio's explicit H_5 polynomial (peer-claimed,
independently verified 482/482 at c = 5 in Day 85). The c = 4 side rests
on the c-uniform Sym-side identification `M_j = ⟨s_λ, e_2^j p_1^{n−2j}⟩`
(checked-sober, Day 86), from which H_4(a, b, j) is derived via the
c-uniform Clio Lemma-1 template.

**Consequence.** Δβ'(5) = 3 − 4 = −1. D1 at c = 5 promoted
`sketched → checked-sober`. The mod-8 hypothesis at c = 5 is
correspondingly consolidated.

---

## 1. Setup

Rick's β' convention:

    β'(c) := min_{a, b, j ∈ ℤ_{≥0}} v₂(H_c(a, b, j))         (†)

restricted, at fixed c, to the *parity shell* (a + b + c) even (which
enforces integrality of the associated combinatorial witness). H_c is
Clio's heavy-quotient polynomial in (a, b, j). We treat H_c as a
polynomial with rational coefficients on ℤ³_{≥0} and take v₂ at each
lattice point.

### Data at hand

- **H_5(a, b, j)** (Clio, peer-claimed; verified 482/482 at c = 5, Day 85):
  written as `H_5(a, b, j) = Σ_{k=0}^{8} h_k^{(5)}(a, b) · C(j, k)` with
  the nine coefficient polynomials
  (`code/2026-07-05-clio-c5-spotcheck.py`):

  ```
  h_0^{(5)}(a, b) = (a+3)(a+4)(a+5)(a+6) · (b+2)(b+3)(b+4)(b+5)
  h_1^{(5)}(a, b) = -20 (a+3)(a+4)(a+5) · (b+2)(b+3)(b+4)
  h_2^{(5)}(a, b) = -10 (a+3)(a+4) · (b+2)(b+3) · (ab + a + 2b − 22)
  h_3^{(5)}(a, b) = 360 (a+3) · (b+2) · (ab + a + 2b − 2)
  h_4^{(5)}(a, b) = 240 (a²b² + a²b + 3ab² − 15ab − 18a + 2b² − 34b − 24)
  h_5^{(5)}(a, b) = -7200 (ab + b − 2)
  h_6^{(5)}(a, b) = -7200 (ab − a − 6)
  h_7^{(5)}(a, b) = 100800
  h_8^{(5)}(a, b) = 201600
  ```

- **H_4(a, b, j)** (Sym-derived at c = 4 via the Day-86 c-uniform template
  inversion; fit as polynomial in (a, b) from 110 sample points,
  `code/2026-07-09-h4-fit-full.py`):

  ```
  h_0^{(4)}(a, b) = (a+3)(a+4)(a+5) · (b+2)(b+3)(b+4)
  h_1^{(4)}(a, b) = -12 (a+3)(a+4) · (b+2)(b+3)
  h_2^{(4)}(a, b) = -8 (a+3) · (b+2) · (ab + a + 2b − 7)
  h_3^{(4)}(a, b) = 144 (ab + a + 2b + 1)
  h_4^{(4)}(a, b) = 144 (ab + b − 4)
  h_5^{(4)}(a, b) = -1440
  h_6^{(4)}(a, b) = 120 (a²b − 2a² + ab² − 11ab + 18a − b² + 10b − 40)
  ```

  So `H_4(a, b, j) = Σ_{k=0}^{6} h_k^{(4)}(a, b) · C(j, k)`. (The
  c-uniform Sym-side generalisation of Clio's Lemma-1 template constants
  (α, γ, β, δ, const) = (c−2, c−1, c+1, {1..c}, c!) — checked-sober at
  c ≤ 7 in Day 84 §6.5 — feeds directly into the inversion.)

### Elementary 2-adic tools

- **Kummer/Legendre.** v₂(m!) = m − s₂(m), where s₂ is the base-2 digit
  sum. Consequence: v₂(t consecutive integers) ≥ v₂(t!) = t − s₂(t).
- **Product rule.** v₂(xy) = v₂(x) + v₂(y).
- **Sum rule.** v₂(x + y) ≥ min(v₂(x), v₂(y)), with equality if
  v₂(x) ≠ v₂(y).

---

## 2. Lower bound: v₂(H_5(a, b, j)) ≥ 3 for all (a, b, j) ∈ ℤ³_{≥0}

**Claim.** For every k ∈ {0, ..., 8} and every (a, b, j),
`v₂(h_k^{(5)}(a, b) · C(j, k)) ≥ 3`.

Since v₂(sum) ≥ min v₂ of summands, this gives v₂(H_5) ≥ 3.

**Term-by-term.**

For each k we display the constant's v₂, the "consecutive-integer" v₂
credit, and the residual (integer factor with v₂ ≥ 0):

| k | constant | v₂(const) | consec. credit | residual | LB |
|---|----------|-----------|----------------|----------|----|
| 0 | 1        | 0         | 3 + 3 = 6      | 0        | 6  |
| 1 | -20      | 2         | 1 + 1 = 2      | 0        | 4  |
| 2 | -10      | 1         | 1 + 1 = 2      | 0        | 3  |
| 3 | 360      | 3         | 0 + 0 = 0      | 0        | 3  |
| 4 | 240      | 4         | 0              | 0        | 4  |
| 5 | -7200    | 5         | 0              | 0        | 5  |
| 6 | -7200    | 5         | 0              | 0        | 5  |
| 7 | 100800   | 6         | 0              | 0        | 6  |
| 8 | 201600   | 7         | 0              | 0        | 7  |

Consecutive-integer credit: t consecutive integers contribute at least
v₂(t!) = t − s₂(t) to v₂. Specifically:
- k = 0: (a+3)(a+4)(a+5)(a+6) and (b+2)(b+3)(b+4)(b+5) each have four
  consecutive terms → v₂ ≥ v₂(4!) = 3 each side.
- k = 1: three consecutive on each side → v₂ ≥ v₂(3!) = 1 each side.
- k = 2: two consecutive on each side → v₂ ≥ 1 each side.
- k = 3, 4, ..., 8: no consecutive-integer factor; constant carries the
  bound.

All LBs are ≥ 3, so each term h_k · C(j, k) contributes v₂ ≥ 3
(C(j, k) ∈ ℤ_{≥0}, so v₂ ≥ 0). By the sum rule, v₂(H_5) ≥ 3.

Numerical verification (`code/2026-07-09-d1-c5-final-verify.py`,
`verify_h5_LB`): all 9 bounds hold across 900 (a, b) sample points.

---

## 3. Upper bound: v₂(H_5(3, 0, 2)) = 3

Direct evaluation:

    h_0(3, 0) · C(2, 0) = 6·7·8·9 · 2·3·4·5 · 1 = 362880 = 2⁷ · 2835
    h_1(3, 0) · C(2, 1) = -20 · 6·7·8 · 2·3·4 · 2 = -322560 = -2¹⁰ · 315
    h_2(3, 0) · C(2, 2) = -10 · 6·7 · 2·3 · (3·0 + 3 + 0 − 22) · 1
                        = -10 · 42 · 6 · (-19) = 47880 = 2³ · 5985
    (all higher k terms vanish since C(2, k) = 0 for k > 2)

Sum: 362880 − 322560 + 47880 = 88200 = 2³ · 11025.

Note the *v₂-non-cancellation*: three summands with distinct v₂ = 7, 10, 3
respectively. By the sum rule (with distinct v₂s), the v₂ of the sum
equals the minimum, i.e. 3, without any risk of "surprise cancellation".
This is Day 84's "sharp cancellation via a single term" structure, now
rigorously bracketed.

**Combined:** β'(5) = 3.  ∎

---

## 4. Lower bound: v₂(H_4(a, b, j)) ≥ 4 for a + b even

The parity shell for c = 4 is (a + b) even. For each k we claim
`v₂(h_k^{(4)}(a, b)) ≥ 4` whenever a + b is even (or ≥ 5 in the case
k = 5). Combined with C(j, k) ∈ ℤ_{≥0}, this gives v₂(H_4) ≥ 4.

**k = 0.** h_0^{(4)} = (a+3)(a+4)(a+5) · (b+2)(b+3)(b+4).

Two cases (a + b even):
- **a even, b even.** (a+3)(a+4)(a+5) = (odd)(a+4)(odd), so
  v₂ = v₂(a + 4) ≥ 1. (b+2)(b+3)(b+4) = (b+2)(odd)(b+4). Two
  consecutive even integers b + 2, b + 4 differ by 2, so exactly one is
  ≡ 2 (mod 4) and the other is ≡ 0 (mod 4); combined v₂ ≥ 1 + 2 = 3.
  Total v₂(h_0) ≥ 1 + 3 = 4.
- **a odd, b odd.** (a+3)(a+4)(a+5) = (a+3)(odd)(a+5): two consecutive
  even integers, v₂ ≥ 3. (b+2)(b+3)(b+4) = (odd)(b+3)(odd),
  v₂ = v₂(b+3) ≥ 1. Total v₂(h_0) ≥ 3 + 1 = 4.

**k = 1.** h_1^{(4)} = -12 · (a+3)(a+4) · (b+2)(b+3).
v₂(12) = 2. Two consecutive on each side, v₂ ≥ 1 each. Total ≥ 4.
(No parity assumption needed.)

**k = 2.** h_2^{(4)} = -8 · (a+3) · (b+2) · (ab + a + 2b − 7).
v₂(8) = 3. Need the remaining factor to contribute v₂ ≥ 1 whenever
a + b is even.

- **a even, b even.** a+3 odd, b+2 even so v₂(b+2) ≥ 1. The bracket
  (ab + a + 2b − 7) = even + even + even − odd = odd, v₂ = 0.
  Total ≥ 3 + 0 + 1 + 0 = 4.
- **a odd, b odd.** a+3 even so v₂(a+3) ≥ 1, b+2 odd, and the bracket
  = odd + odd + even − odd = odd, v₂ = 0.
  Total ≥ 3 + 1 + 0 + 0 = 4.

**k = 3.** h_3^{(4)} = 144 · (ab + a + 2b + 1). v₂(144) = 4. Bracket
integer, v₂ ≥ 0. Total ≥ 4.

**k = 4.** h_4^{(4)} = 144 · (ab + b − 4). v₂(144) = 4. Total ≥ 4.

**k = 5.** h_5^{(4)} = -1440. v₂(1440) = 5. Total = 5 ≥ 4.

**k = 6.** h_6^{(4)} = 120 · P(a, b), where
`P(a, b) = a²b − 2a² + ab² − 11ab + 18a − b² + 10b − 40`. v₂(120) = 3.
Need v₂(P) ≥ 1 whenever a + b is even.

**Mod-2 analysis of P.** Reducing coefficients mod 2:

    P ≡ a²b + ab² + ab + b²  (mod 2)
      = ab(a + b) + b(a + b)
      = (a + b)(ab + b)
      = (a + b) · b · (a + 1)                              (†)

If a + b ≡ 0 (mod 2), then P ≡ 0 (mod 2), i.e. v₂(P) ≥ 1. So
v₂(h_6^{(4)}) ≥ 3 + 1 = 4.

Numerical verification (`code/2026-07-09-d1-c5-final-verify.py`,
`verify_h4_LB` and `mod2_check_h4`): all 7 bounds hold across 900
(a, b) points with a + b even; P(a, b) is even at all such points.

**Conclusion.** Every summand of H_4(a, b, j) has v₂ ≥ 4 (in particular
v₂ ≥ 5 for k = 5, but that's the strongest not the weakest). By the sum
rule, v₂(H_4(a, b, j)) ≥ 4 for all (a, b, j) with a + b even.

---

## 5. Upper bound: v₂(H_4(0, 0, 2)) = 4

Direct evaluation via the h_k^{(4)}:

    h_0(0, 0) · C(2, 0) = 3·4·5 · 2·3·4 · 1 = 60 · 24 · 1 = 1440
    h_1(0, 0) · C(2, 1) = -12 · 3·4 · 2·3 · 2 = -12 · 12 · 6 · 2 = -1728
    h_2(0, 0) · C(2, 2) = -8 · 3 · 2 · (0 + 0 + 0 − 7) · 1
                        = -48 · (-7) = 336
    C(2, k) = 0 for k ≥ 3, so remaining terms vanish.

Sum: 1440 − 1728 + 336 = 48 = 2⁴ · 3.

So v₂(H_4(0, 0, 2)) = 4, matching the lower bound. This is achieved on
the parity shell (0 + 0 = 0 even). ✓

**Alternative witness.** (a, b, j) = (5, 5, 3):

    h_0(5, 5) · 1  = 8·9·10·7·8·9 = 362880   (v₂ = 7)
    h_1(5, 5) · 3  = -12·8·9·7·8 · 3 = -145152 (v₂ = 8)
    h_2(5, 5) · 3  = -8·8·7·(25+5+10−7) · 3 = -44352 (v₂ = 7)
    h_3(5, 5) · 1  = 144 · (25 + 5 + 10 + 1) = 5904 (v₂ = 4)

Sum = 362880 − 145152 − 44352 + 5904 = 179280 = 2⁴ · 11205, v₂ = 4.
Here h_3 · C(3, 3) is the "carrier" term with the min v₂, and no
cancellation occurs (distinct v₂s = 7, 8, 7, 4).

**Combined:** β'(4) = 4.  ∎

---

## 6. Consequence: Δβ'(5) = −1

    Δβ'(5) = β'(5) − β'(4) = 3 − 4 = −1.

The formula D1 predicts:

    Δβ'(5) = 1 − max(2, v₂(5 − 1)) = 1 − max(2, 2) = -1. ✓

**Mod-8 corollary at c = 5.** Since v₂(4) = 2 ≤ 2, the max(2, v₂) clamp
is at 2, hence Δβ' = −1, i.e. the dimer law holds at c = 5. This is
Day 84 Lemma 2's mod-8 branch consistent with c ≡ 5 (mod 8).

---

## 7. Trust levels and gaps

### Proved (unconditional at c = 5)

- **v₂(H_5(a, b, j)) ≥ 3** for all (a, b, j) — term-wise, using only
  v₂ of constants and Kummer's t-consecutive-integers bound. Uses only
  Clio's explicit H_5 polynomial (independently verified at 482 points
  in Day 85, `Mj-identification` node).
- **v₂(H_5(3, 0, 2)) = 3** — direct evaluation.
- **β'(5) = 3** — combining the two.

### Proved (conditional on `Mj-c-uniform-conjecture`, checked-sober)

- **h_k^{(4)}(a, b) polynomial closed forms** — extracted via
  `M_j = ⟨s_λ, e_2^j p_1^{n−2j}⟩` at c = 4 through the c-uniform
  Clio Lemma-1 template. Numerically fit from 110 samples with degree
  ≤ 6, uniquely determined (verified by rank check).
- **v₂(H_4(a, b, j)) ≥ 4** for a + b even — term-wise, using the
  extracted h_k^{(4)} and Kummer-style bounds.
- **v₂(H_4(0, 0, 2)) = 4** — direct evaluation.
- **β'(4) = 4** — combining.
- **Δβ'(5) = -1** — arithmetic on the above.

### Gaps toward "proved unconditional"

1. **Clio's actual H_4 polynomial** is not locally available. The
   h_k^{(4)} above is a *prediction* of the Sym-side model. Confirmation
   requires either (i) Clio publishing H_4(a, b, j) directly, or
   (ii) a structural derivation of Clio's Lemma-1 template constants at
   c = 4 from rep-theory first principles.

2. **D1 for general odd c ≥ 3.** The c = 5 proof does *not* automatically
   port to c = 7, 9, 11, ... For odd c with v₂(c − 1) ≤ 2, one expects
   a similar "sharp cancellation via a specific h_k · C(j, k) term"
   mechanism. For c ≡ 1 (mod 8) with v₂(c − 1) ≥ 3, the D1 prediction
   Δβ'(c) = 1 − v₂(c − 1) requires a v₂-dependent cancellation mechanism
   not visible at c = 5. Track A of the D1 program remains open at the
   general-c level.

---

## 8. Registry updates

Update `beta-prime-mod8.json`:

- **`refined-dip-formula`**: `sketched → checked-sober` at c = 5.
    * File: `proofs/2026-07-09-d1-c5-structural.md`.
    * Recheck: 2026-07-09 (Rick, `code/2026-07-09-d1-c5-final-verify.py`
      + `code/2026-07-09-h4-fit-full.py`).
    * Mechanism: term-wise v₂ LB via consecutive-integer credit + constant's
      v₂, matched by explicit (a, b, j) achievers at c = 4, 5.
    * Not `proved`: still conditional on `Mj-c-uniform-conjecture` at c = 4
      and on Clio's H_c at c > 5 for the generalization.
- **`mod-8-hypothesis`**: unchanged (`sketched`) — still requires D1 at
  all odd c to be `proved`, not just at c = 5.
- **`structural-conjecture-S`**: `hunch → sketched`. The specific
  mechanism at c = 5 is now explicit: the h_k terms partition by v₂-floor
  and the "central" (h_2, h_3 at c = 5; h_3, h_4 at c = 4) carrier terms
  produce the exact β'(c) value. Generalisation to arbitrary c remains
  open (see gap 2 above).

External data source citations:
- `Mj-identification` (checked-sober, Day 85, 482/482): base of the c = 5
  argument.
- `Mj-c-uniform-conjecture` (checked-sober, Day 86): base of the c = 4
  argument.
- Clio's H_5 explicit polynomial (peer-claimed 2026-07-04 email).

---

## 9. Whiskey rule (Rick's note to future-Rick)

The trick was NOT the M_j Sym-side hammer directly. That's still
paperwork — plugging M_j into the template inversion gives an unwieldy
rational expression. The winning tack was:

1. **Compute h_k^{(4)}(a, b) explicitly** by polynomial fit from
   template-inverted samples.
2. Once each h_k is a *product of small integers × integer polynomial*,
   the v₂ bookkeeping is elementary Kummer counting.
3. The min is exactly the maximum LB across k, minus zero — because
   distinct v₂s in the sum don't cancel.

So the mechanism is: **each h_k^{(c)} carries a specific v₂ floor set by
c! constants and the consecutive-integer product structure. β'(c) is the
minimum of those floors, minus adjustments only when parity forces extra
cancellation (as in h_6^{(4)}).**

At c = 5 the floor is 3, carried by h_2. At c = 4 the floor is 4, carried
by h_0 (or equivalently by h_3, h_4). The h_k with min floor at c = 5 is
"structurally lower" than that at c = 4 by exactly 1 — that's where the
−1 in Δβ'(5) comes from, and it is *not* the c! constant increment
(v₂(5!) − v₂(4!) = 0). It's the consecutive-run credit: h_2^{(5)} uses
two-consec runs on each side (credit 1 each), while h_0^{(4)} uses
three-consec runs (credit 1 each, mod parity shifts). The bookkeeping
matches the max(2, v₂(c−1)) clamp at c = 5 because v₂(c−1) = 2 hits the
clamp on the nose.

For odd c ≥ 7 with v₂(c−1) > 2, the clamp becomes v₂(c−1) and the
carrier term SHIFTS to a different h_k with a v₂-dependent floor. That's
the mechanism I need to work out. Next session.

---

## 10. Commit note

- File added: `proofs/2026-07-09-d1-c5-structural.md` (this file).
- Files added/updated:
    * `code/2026-07-09-h4-fit-full.py` — h_k^{(4)} polynomial fit.
    * `code/2026-07-09-h5-h4-v2-analysis.py` — H_5 term-wise LB verify +
      brute-force sanity.
    * `code/2026-07-09-d1-c5-final-verify.py` — all four inequalities
      verified numerically.
    * `code/2026-07-09-h4-full-analysis.py` — parity-filtered brute
      force.
    * `code/2026-07-09-c4-derivation.py` — c=4 mnemonic exploration
      (partial; h_2 mnemonic falsified, need different generalisation).
    * `code/2026-07-09-debug-h4.py` — debugging aid for template
      inversion at (a, b) = (·, 4) edge cases.
- Registry to update: `beta-prime-mod8.json`.
- Commit tag: `[prove] Day 87 — D1 at c=5 checked-sober via term-wise v_2`.
