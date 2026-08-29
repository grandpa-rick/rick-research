/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

# Δ₀ ≥ 2 from the G1 single-carrier proof (Day 99)

Formalises the first of the four strict gap inequalities in Day 99's proof
that at `(a, b) = (0, 2)`, `c ≡ 2 (mod 4)`, `c ≥ 6`, the interior anchor
`j = 4` in the H₄ expansion is the unique v₂-minimising carrier.

## Informal statement

For `c ≡ 2 (mod 4)`, `c ≥ 6`, and `m := (c - 2) / 4 ≥ 1`, the informal
proof reduces (via the Q_k catalog, Pochhammer AMM valuations, and the
Kummer digit-sum identity) the raw difference

    Δ_0(c) := v_2(h_0^{(c)}(0, 2)) - v_2(h_4^{(c)}(0, 2))

to the closed form

    Δ_0(m) = 1 + v_2(m) + v_2(m + 1).

Since `m` and `m + 1` are consecutive naturals, at least one is even, so
`v_2(m) + v_2(m + 1) ≥ 1`, hence `Δ_0(m) ≥ 2`.

## Formalisation scope (this file)

We prove the FINAL numerical inequality:

    for `m ≥ 1`, `1 + padicValNat 2 m + padicValNat 2 (m + 1) ≥ 2`.

The upstream reduction — closed forms for `v_2(h_0)`, `v_2(h_4)`, and the
`s_2` / Kummer bookkeeping that collapses their difference to the RHS —
lives in the informal proof
(`proofs/2026-07-16-day99-G1-scp-single-carrier.md`, §4.1) and is not
formalised here.  Companion to `R4Mod32.lean` (Day 99), which formalises
the mod-32 residue of the `R_4` polynomial used inside `v_2(h_4)`.

## Registry impact

Promotes `delta0-final-consecutive-v2` (new leaf lemma) to
`lean-verified`, giving one Lean-checked step of the G1 SCP argument.
The Q/Poch/s_2 reduction remains `proved` (informal).

## Axiom target

`[propext, Classical.choice, Quot.sound]` — the full Mathlib default set,
empirically verified via `#print axioms` (Day 101 lean session, receipt
`2026-07-17-day101-delta0-axioms-receipt.txt`).  `Classical.choice`
enters through the `padicValNat` machinery (it is defined via
`Nat.find` on a classical existential in `Mathlib.NumberTheory.Padics`),
not through the combinatorial argument itself.  Contrast with Day 99
`R4Mod32` whose slimmer `[propext, Quot.sound]` audit reflects a pure
polynomial `ring` + `Int.emod` calculation with no measure-theoretic
imports.
-/

import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Algebra.Ring.Parity
import Mathlib.Tactic.Ring

namespace Delta0

/-- The reduced closed form of `Δ_0`: after the s_2 / Kummer collapse,
`Δ_0(m) = 1 + v_2(m) + v_2(m + 1)`.  This is the RHS whose informal
`≥ 2` bound powers the `j = 4` uniqueness half of the Day 99 SCP proof. -/
def delta0 (m : ℕ) : ℕ :=
  1 + padicValNat 2 m + padicValNat 2 (m + 1)

/-- **Key combinatorial lemma.**  Among two consecutive positive naturals
`m` and `m + 1`, at least one is even, hence `v_2(m) + v_2(m + 1) ≥ 1`.

This is the entire mathematical content of `Δ_0 ≥ 2` after the informal
reduction. -/
lemma one_le_v2_add_v2_succ (m : ℕ) (hm : 1 ≤ m) :
    1 ≤ padicValNat 2 m + padicValNat 2 (m + 1) := by
  rcases Nat.even_or_odd m with he | ho
  · -- `m` even: `2 ∣ m` and `m ≠ 0`, so `v_2(m) ≥ 1`.
    have hm0 : m ≠ 0 := Nat.one_le_iff_ne_zero.mp hm
    have hdvd : (2 : ℕ) ∣ m := he.two_dvd
    have := one_le_padicValNat_of_dvd (p := 2) hm0 hdvd
    omega
  · -- `m` odd: `2 ∣ (m + 1)`, so `v_2(m + 1) ≥ 1`.
    have hm1 : m + 1 ≠ 0 := Nat.succ_ne_zero m
    have hdvd : (2 : ℕ) ∣ (m + 1) := (Odd.add_one ho).two_dvd
    have := one_le_padicValNat_of_dvd (p := 2) hm1 hdvd
    omega

/-- **Main theorem.**  `Δ_0(m) ≥ 2` for every `m ≥ 1`.

This is the strict-gap conclusion Day 99's G1 proof needs at the `k = 0`
carrier to promote `j = 4` to the unique v₂-minimum among `k ∈ {0,…,4}`
in the expansion `H_c(0,2,4) = ∑ C(4,k) h_k^{(c)}(0,2)`. -/
theorem delta0_ge_two (m : ℕ) (hm : 1 ≤ m) : 2 ≤ delta0 m := by
  unfold delta0
  have h := one_le_v2_add_v2_succ m hm
  omega

/-- **Corollary in `c` phrasing.**  For any `c ≡ 2 (mod 4)` with `c ≥ 6`,
`Δ_0` evaluated at `m = (c - 2) / 4` satisfies `Δ_0 ≥ 2`.

This is the form Day 99's G1 derivation cites at (a, b) = (0, 2). -/
theorem delta0_ge_two_of_c (c : ℕ) (hc4 : c % 4 = 2) (hc6 : 6 ≤ c) :
    2 ≤ delta0 ((c - 2) / 4) := by
  apply delta0_ge_two
  -- `c ≥ 6` and `c ≡ 2 mod 4` give `(c - 2) / 4 ≥ 1`.
  omega

/-!
### Numerical sanity checks (Day 99 (Δ₀) column)

Six values matching the `Δ_0` column of the numerical table in §4.5 of
the Day 99 proof.  These pin down the closed form on small inputs.

| m | m+1 | v₂(m) | v₂(m+1) | Δ_0 |
|---|-----|-------|---------|-----|
| 1 |  2  |   0   |    1    |  2  |
| 2 |  3  |   1   |    0    |  2  |
| 3 |  4  |   0   |    2    |  3  |
| 4 |  5  |   2   |    0    |  3  |
| 7 |  8  |   0   |    3    |  4  |
| 8 |  9  |   3   |    0    |  4  |

Notation: `v2n n k := padicValNat 2 n = k` proven from the relevant
`padicValNat.prime_pow` (for `n = 2^k`) or `padicValNat.eq_zero_of_not_dvd`
(for odd `n`).  `padicValNat` does not reduce by `decide`, so each fact
is packaged as its own tiny `have`. -/

/-- `v₂(1) = 0`. -/
private lemma v2_1 : padicValNat 2 1 = 0 := padicValNat_one_right 2
/-- `v₂(2) = 1`. -/
private lemma v2_2 : padicValNat 2 2 = 1 := padicValNat_self
/-- `v₂(3) = 0`. -/
private lemma v2_3 : padicValNat 2 3 = 0 :=
  padicValNat.eq_zero_of_not_dvd (by decide)
/-- `v₂(4) = 2`. -/
private lemma v2_4 : padicValNat 2 4 = 2 := by
  have : (4 : ℕ) = 2 ^ 2 := by decide
  rw [this]; exact padicValNat.prime_pow 2
/-- `v₂(5) = 0`. -/
private lemma v2_5 : padicValNat 2 5 = 0 :=
  padicValNat.eq_zero_of_not_dvd (by decide)
/-- `v₂(7) = 0`. -/
private lemma v2_7 : padicValNat 2 7 = 0 :=
  padicValNat.eq_zero_of_not_dvd (by decide)
/-- `v₂(8) = 3`. -/
private lemma v2_8 : padicValNat 2 8 = 3 := by
  have : (8 : ℕ) = 2 ^ 3 := by decide
  rw [this]; exact padicValNat.prime_pow 3
/-- `v₂(9) = 0`. -/
private lemma v2_9 : padicValNat 2 9 = 0 :=
  padicValNat.eq_zero_of_not_dvd (by decide)

example : delta0 1 = 2 := by
  unfold delta0; rw [v2_1, v2_2]
example : delta0 2 = 2 := by
  unfold delta0; rw [v2_2, v2_3]
example : delta0 3 = 3 := by
  unfold delta0; rw [v2_3, v2_4]
example : delta0 4 = 3 := by
  unfold delta0; rw [v2_4, v2_5]
example : delta0 7 = 4 := by
  unfold delta0; rw [v2_7, v2_8]
example : delta0 8 = 4 := by
  unfold delta0; rw [v2_8, v2_9]

end Delta0

-- Axiom audit (leave in place during review; comment out for library use).
#print axioms Delta0.one_le_v2_add_v2_succ
#print axioms Delta0.delta0_ge_two
#print axioms Delta0.delta0_ge_two_of_c
