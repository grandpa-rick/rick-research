/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises the (♣) universal identity from Day 95 §4 of Rick's
β'(c) program: for every `c ≥ 2`,

    β(c) − LB_1(c) = s_2(c−1) + v_2(c−1) − v_2(c)

where
* `β(c)      = 2(c−1) − s_2(c−1)`                (Kummer/Legendre floor),
* `LB_1(c)   = 2·v_2((c−2)!) + v_2(c) + v_2(c−1)` (Day 93 F2 formula,
                lean-verified as `LB_1_c_uniform`),
* `s_2(n)    = digit-sum of n in base 2`,
* `v_2(n)    = 2-adic valuation of n`.

## Proof outline

Two elementary ingredients:

1. **Legendre for `p = 2`.** `v_2(n!) = n − s_2(n)`. Follows from Mathlib's
   `sub_one_mul_padicValNat_factorial` since `p − 1 = 1` at `p = 2`.

2. **Digit-shift.** For `n ≥ 1`, `s_2(n) = s_2(n − 1) + 1 − v_2(n)`.
   Derived from Legendre applied to `n! = n · (n − 1)!`:
       `v_2(n!) = v_2(n) + v_2((n − 1)!)`,
   i.e. `n − s_2(n) = v_2(n) + (n − 1) − s_2(n − 1)`,
   which rearranges to the shift identity.

Both identities cast to `ℤ` for the subtractions; the main theorem
then follows by `linarith` on the linear cast identities.

## Registry impact

Closes `beta-LB1-universal-identity` from `proved` to `lean-verified`.
Axiom set target: `[propext, Classical.choice, Quot.sound]`.
-/

import Mathlib.Data.Nat.Digits.Defs
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace BetaLB1Identity

open Nat

/-- Fact instance for the prime `2`, so the `padicValNat` API is available. -/
instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩

/-! ### The `s_2` binary digit sum -/

/-- `s_2(n) = sum of the base-2 digits of n`. -/
def s2 (n : ℕ) : ℕ := (Nat.digits 2 n).sum

/-- The base-2 digit sum is bounded by `n`. -/
lemma s2_le (n : ℕ) : s2 n ≤ n := Nat.digit_sum_le 2 n

/-! ### Legendre's formula at `p = 2` -/

/-- **Legendre for `p = 2`** (ℕ form): `v_2(n!) = n − s_2(n)`. -/
lemma padicValNat_two_factorial (n : ℕ) :
    padicValNat 2 n.factorial = n - s2 n := by
  have h := sub_one_mul_padicValNat_factorial (p := 2) n
  simpa [s2] using h

/-- **Legendre for `p = 2`** (ℤ form): `(v_2(n!) : ℤ) = (n : ℤ) − s_2(n)`. -/
lemma padicValNat_two_factorial_int (n : ℕ) :
    (padicValNat 2 n.factorial : ℤ) = (n : ℤ) - s2 n := by
  have h := padicValNat_two_factorial n
  have hle : s2 n ≤ n := s2_le n
  rw [h, Nat.cast_sub hle]

/-! ### Digit-shift lemma -/

/-- **Digit-shift lemma.** For `n ≥ 1`,
`s_2(n) = s_2(n − 1) + 1 − v_2(n)` (as integers).

Proof: from `n! = n · (n−1)!` and multiplicativity of `padicValNat`,
we get `v_2(n!) = v_2(n) + v_2((n−1)!)`. Substituting Legendre on both
sides and rearranging gives the identity. -/
lemma s2_shift (n : ℕ) (hn : 1 ≤ n) :
    (s2 n : ℤ) = (s2 (n - 1) : ℤ) + 1 - padicValNat 2 n := by
  have hn0 : n ≠ 0 := Nat.one_le_iff_ne_zero.mp hn
  -- Legendre applied at n and at (n − 1).
  have hLn  : (padicValNat 2 n.factorial : ℤ) = (n : ℤ) - s2 n :=
    padicValNat_two_factorial_int n
  have hLn1 : (padicValNat 2 (n - 1).factorial : ℤ)
              = ((n - 1 : ℕ) : ℤ) - s2 (n - 1) :=
    padicValNat_two_factorial_int (n - 1)
  -- Factorial recursion: n! = n · (n − 1)!.
  have hfact : n.factorial = n * (n - 1).factorial := by
    obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hn0
    simp [Nat.factorial_succ]
  -- Multiplicativity of the 2-adic valuation.
  have hnm1fact_ne : (n - 1).factorial ≠ 0 := Nat.factorial_ne_zero _
  have hsplit : padicValNat 2 n.factorial
                  = padicValNat 2 n + padicValNat 2 (n - 1).factorial := by
    rw [hfact, padicValNat.mul hn0 hnm1fact_ne]
  have hsplit_z : (padicValNat 2 n.factorial : ℤ)
                    = (padicValNat 2 n : ℤ) + padicValNat 2 (n - 1).factorial := by
    exact_mod_cast hsplit
  -- Cast helper: ((n − 1 : ℕ) : ℤ) = (n : ℤ) − 1 when n ≥ 1.
  have hcast : ((n - 1 : ℕ) : ℤ) = (n : ℤ) - 1 := by
    rw [Nat.cast_sub hn]; simp
  -- Combine linearly.
  linarith [hLn, hLn1, hsplit_z, hcast]

/-! ### Definitions of β and LB_1 -/

/-- Rick's shifted Kummer floor `β(c) = 2(c − 1) − s_2(c − 1)` (as `ℤ`). -/
def beta (c : ℕ) : ℤ := 2 * ((c : ℤ) - 1) - s2 (c - 1)

/-- The F2 warm-up bound `LB_1(c) = 2·v_2((c − 2)!) + v_2(c) + v_2(c − 1)`
(as `ℤ`). Matches the closed form proved in `LB_1_c_uniform`
(Day 93 lean-verified). -/
def LB1 (c : ℕ) : ℤ :=
  2 * padicValNat 2 (Nat.factorial (c - 2))
    + padicValNat 2 c
    + padicValNat 2 (c - 1)

/-! ### Main theorem: the (♣) identity -/

/-- **(♣) The universal β − LB_1 identity.** For every `c ≥ 2`,
`β(c) − LB_1(c) = s_2(c−1) + v_2(c−1) − v_2(c)`. -/
theorem beta_minus_LB1_identity (c : ℕ) (hc : 2 ≤ c) :
    beta c - LB1 c
      = (s2 (c - 1) : ℤ) + padicValNat 2 (c - 1) - padicValNat 2 c := by
  unfold beta LB1
  -- Legendre at (c − 2): v_2((c−2)!) = (c−2) − s_2(c−2).
  have hLc2 : (padicValNat 2 (Nat.factorial (c - 2)) : ℤ)
                = ((c - 2 : ℕ) : ℤ) - s2 (c - 2) :=
    padicValNat_two_factorial_int _
  -- Digit-shift at n = c − 1: s_2(c−1) = s_2(c−2) + 1 − v_2(c−1).
  have hshift : (s2 (c - 1) : ℤ)
                  = (s2 (c - 2) : ℤ) + 1 - padicValNat 2 (c - 1) := by
    have h1 : 1 ≤ c - 1 := by omega
    have hrw : (c - 1 - 1 : ℕ) = c - 2 := by omega
    have hstep := s2_shift (c - 1) h1
    rw [hrw] at hstep
    exact hstep
  -- Cast helper: ((c − 2 : ℕ) : ℤ) = (c : ℤ) − 2.
  have hc2z : ((c - 2 : ℕ) : ℤ) = (c : ℤ) - 2 := by
    rw [Nat.cast_sub hc]; simp
  -- Linear combination gives the result.
  linarith [hLc2, hshift, hc2z]

end BetaLB1Identity

/-! ### Axiom audit -/

#print axioms BetaLB1Identity.padicValNat_two_factorial
#print axioms BetaLB1Identity.s2_shift
#print axioms BetaLB1Identity.beta_minus_LB1_identity
