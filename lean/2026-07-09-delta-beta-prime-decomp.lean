/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises the "Δβ' = Δβ − ΔD" bookkeeping identity of Day 84
(`~/projects/proofs/2026-07-08-d1-partial.md`, Theorem 4).  This is the
next brick after `DeltaBetaKummer.delta_beta_kummer` (Day 86) in the
Lean chain toward the D1 conjecture.
-/
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.NumberTheory.Padics.PadicVal.Basic

/-!
# `Δβ' = Δβ − ΔD` (a bookkeeping identity)

Let `β(c) := c + v₂(c!)` be Rick's shifted Kummer floor (Day 86,
`DeltaBetaKummer.beta`).  Given any function `D : ℕ → ℕ` representing
the "internal-channel loss" (see Day-84 `d1-partial` §5), set

    β'(c) := (β c : ℤ) − (D c : ℤ)     (integer-valued; no truncation).

Then the one-step difference `Δβ'(c+1) := β'(c+1) − β'(c)` satisfies

    Δβ'(c+1) = Δβ(c+1) − ΔD(c+1)
             = 1 + v₂(c+1) − ΔD(c+1).                                   (‡)

The rewriting `Δβ(c+1) = 1 + v₂(c+1)` is **Lemma 1** of Day 84, a.k.a.
`delta_beta_kummer` (Day 86, Lean-verified).

This is a *definitional* lemma — no math content beyond the Kummer
identity plus integer arithmetic.  Its role is to give the Day-88+
Lean chain a clean interface: once someone supplies a closed form for
`ΔD` (the Day-84 conjecture is piecewise in `c mod 4`), the closed
form for `Δβ'` follows by substitution.

## Main definitions

* `beta`      — Rick's shifted Kummer floor `c + v₂(c!)`.
* `betaPrime` — the integer-valued corrected floor `β − D`.
* `deltaD`    — the integer-valued one-step difference `D(c+1) − D(c)`.

## Main result

* `delta_beta_prime_decomp`:
  `βPrime D (c+1) − βPrime D c = 1 + v₂(c+1) − ΔD c`.

## Design notes

* We stay in `ℤ` for `betaPrime` and `deltaD` to avoid the
  `D c ≤ β c` hypothesis that a `ℕ`-valued version would require.
  Downstream users can `Int.toNat` when they know positivity.

* `beta` is duplicated from `DeltaBetaKummer.beta` so this file
  compiles stand-alone; the two are definitionally equal.
-/

namespace DeltaBetaPrime

open Nat

/-- Fact instance for the prime `2`, so the `padicValNat` API is available. -/
instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩

/-- Rick's shifted Kummer floor `β(c) := c + v₂(c!)`.

Duplicated verbatim from `DeltaBetaKummer.beta` so this file stands
alone.  See the Day-86 module for the Kummer/Legendre interpretation. -/
def beta (c : ℕ) : ℕ := c + padicValNat 2 c.factorial

/-- Kummer step for `β`, as a `ℕ`-equation.

Identical statement (and proof) to `DeltaBetaKummer.delta_beta_kummer`.
Restated locally to keep this module self-contained. -/
lemma beta_succ (c : ℕ) :
    beta (c + 1) = beta c + 1 + padicValNat 2 (c + 1) := by
  unfold beta
  rw [Nat.factorial_succ,
      padicValNat.mul (Nat.succ_ne_zero c) c.factorial_ne_zero]
  ring

/-- Kummer step for `β` cast to `ℤ` — the form actually used below. -/
lemma beta_succ_int (c : ℕ) :
    (beta (c + 1) : ℤ) = (beta c : ℤ) + 1 + (padicValNat 2 (c + 1) : ℤ) := by
  exact_mod_cast beta_succ c

/-- One-step difference of the "internal-channel loss" `D`, in `ℤ`. -/
def deltaD (D : ℕ → ℕ) (c : ℕ) : ℤ :=
  (D (c + 1) : ℤ) - (D c : ℤ)

/-- Integer-valued corrected floor `β'(c) := β(c) − D(c)`.

We work in `ℤ` so that the definition is total; no `D c ≤ β c` hypothesis
is needed.  Under Rick's Day-84 conjecture (`D c ≤ β c` for all c ≥ 4),
this coincides with the natural-number floor. -/
def betaPrime (D : ℕ → ℕ) (c : ℕ) : ℤ :=
  (beta c : ℤ) - (D c : ℤ)

/-- **Δβ' = Δβ − ΔD.**

The bookkeeping identity: for any `D : ℕ → ℕ`, the one-step difference
of `β' := β − D` decomposes into the Kummer step `1 + v₂(c+1)` minus
the D-step `ΔD(c+1)`.  Combines the Day-86 Kummer identity
(`beta_succ_int`) with plain integer arithmetic. -/
theorem delta_beta_prime_decomp (D : ℕ → ℕ) (c : ℕ) :
    betaPrime D (c + 1) - betaPrime D c
      = 1 + (padicValNat 2 (c + 1) : ℤ) - deltaD D c := by
  unfold betaPrime deltaD
  have h := beta_succ_int c
  linarith

end DeltaBetaPrime

-- Axiom audit (leave in place during review; comment out for library use).
#print axioms DeltaBetaPrime.delta_beta_prime_decomp
