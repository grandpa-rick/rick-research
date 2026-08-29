/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises Lemma 1 of `~/projects/proofs/2026-07-07-dip-formula.md`
("Δβ closed form"), the elementary Kummer identity underpinning the
mod-8 dimer-law analysis of β'(c).
-/
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.NumberTheory.Padics.PadicVal.Basic

/-!
# Δβ Kummer identity

Let `β(c) := c + v₂(c!)` be the "shifted Kummer floor" that arises in the
BDI 2-adic analysis.  (Numerically, `β(c) = 2c − s₂(c)`, where `s₂` is the
binary digit sum; equivalently, `β(c) = v₂(2^c · c!)`.  This matches the
paper's `β(c+1) = 2c − s₂(c)` under a shift of index.)

## Main result

* `DeltaBetaKummer.delta_beta_kummer`:
  `β(c + 1) = β(c) + 1 + v₂(c + 1)` for every `c : ℕ`.

Rearranged this reads `Δβ(c+1) = 1 + v₂(c+1)`, which is Lemma 1 of the
Day-83 dip-formula memo.  The proof is a one-liner: expand the factorial
recursion `(c+1)! = (c+1) · c!` and apply `padicValNat.mul`.

## Note on `LEAN.md` phrasing

The Day-86 trigger file suggests defining `β(c) := v₂(c!)` and proving
`Δβ(c) = 1 + v₂(c-1)`.  That literal reading is false — with
`β(c) := v₂(c!)`, one gets `Δβ(c) = v₂(c)` from `c! = c · (c-1)!`, and
`v₂(c) = 1 + v₂(c-1)` fails at e.g. `c = 3`.  The identity Rick's paper
actually proves is for `β(c) = 2(c-1) − s₂(c-1) = (c-1) + v₂((c-1)!)`,
which after re-indexing `c ↦ c+1` is the shifted floor `β(c) := c + v₂(c!)`
used here.  Both formulations state the same underlying fact.
-/

namespace DeltaBetaKummer

open Nat

/-- Fact instance for the prime `2`, so the `padicValNat` API is available. -/
instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩

/-- Rick's shifted Kummer floor `β(c) := c + v₂(c!)`.

By Legendre's formula this equals `2c − s₂(c)`, the exponent of `2` in the
even double-factorial `2 · 4 · 6 ⋯ (2c)`.  The paper's `β(c) = 2(c-1) − s₂(c-1)`
is `beta (c-1)` in this convention (index shifted so that `beta 0 = 0`). -/
def beta (c : ℕ) : ℕ := c + padicValNat 2 c.factorial

/-- **Lemma 1 (Δβ Kummer identity).**

For every `c : ℕ`,
`β(c + 1) = β(c) + 1 + v₂(c + 1)`.

Equivalently, `Δβ(c+1) := β(c+1) − β(c) = 1 + v₂(c+1)`, which is Rick's
`Δβ(c) = 1 + v₂(c−1)` after the index shift `c ↦ c + 1`. -/
theorem delta_beta_kummer (c : ℕ) :
    beta (c + 1) = beta c + 1 + padicValNat 2 (c + 1) := by
  unfold beta
  rw [Nat.factorial_succ,
      padicValNat.mul (Nat.succ_ne_zero c) c.factorial_ne_zero]
  ring

/-- Corollary in the "subtraction" phrasing familiar from the paper:
`Δβ(c+1) = 1 + v₂(c+1)`. -/
theorem delta_beta_kummer_sub (c : ℕ) :
    beta (c + 1) - beta c = 1 + padicValNat 2 (c + 1) := by
  have h := delta_beta_kummer c
  omega

end DeltaBetaKummer

-- Axiom audit (leave in place during review; comment out for library use).
#print axioms DeltaBetaKummer.delta_beta_kummer
#print axioms DeltaBetaKummer.delta_beta_kummer_sub
