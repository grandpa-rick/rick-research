/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises §5 of `~/projects/proofs/2026-07-08-d1-partial.md` (Day 84):
Rick's closed form for the carry gap `D(c) := β(c) − β'(c)` under three
conditional hypotheses D1, (E), D2 on the internal-channel floor `β'`.
-/
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Closed form for `D(c) := β(c) − β'(c)` under {D1, (E), D2}

Let `β(c) := 2(c-1) − s₂(c-1) = (c-1) + v₂((c-1)!)` be Rick's ambient
Kummer floor (paper convention: `β(1) = 0`, `β(2) = 1`, `β(5) = 7`, …).
Rick's Day 84 memo (§5) proves that under three empirical/conjectural
hypotheses on `β' : ℕ → ℕ`,

* **D1** (Day 83): for every odd `c ≥ 3`,
  `β'(c) − β'(c-1) = 1 − max(2, v₂(c-1))`;

* **(E)** (Day 84 anchor): for every `k`, `β'(4k) = β(4k)`;

* **D2** (Day 84 quadratic residue): for every `k ≥ 1`,
  `β'(4k+2) = β(4k+2) − 1 − v₂(k)`,

the carry gap `D(c) := β(c) − β'(c)` obeys the piecewise closed form

    D(4k)   = 0,
    D(4k+1) = 4 + 2 v₂(k)     (k ≥ 1),
    D(4k+2) = 1 + v₂(k)       (k ≥ 1),
    D(4k+3) = 4 + v₂(k)       (k ≥ 1).

The `ΔD` case-split follows by subtraction.

## Main definitions

* `beta`  — paper-β: `β(0) := 0`, `β(c+1) := c + v₂(c!)`.
* `HypD1 bp`, `HypE bp`, `HypD2 bp` — the three hypothesis interfaces.
* `D bp c` — integer-valued carry gap `β(c) − bp(c)`.

## Main results

* `D_at_4k` : `D bp (4*k) = 0` (from `HypE` alone).
* `D_at_4k_add_2` : `D bp (4*k + 2) = 1 + v₂(k)` (from `HypD2` alone).
* `D_at_4k_add_1` : `D bp (4*k + 1) = 4 + 2 * v₂(k)` (from `HypD1 + HypE`, k ≥ 1).
* `D_at_4k_add_3` : `D bp (4*k + 3) = 4 + v₂(k)` (from `HypD1 + HypD2`, k ≥ 1).

## Corollary (ΔD case-split)

* `deltaD_at_4k`, `deltaD_at_4k_add_1`, `deltaD_at_4k_add_2`,
  `deltaD_at_4k_add_3` — piecewise forward differences derived by
  subtracting the four `D_at_…` lemmas.

## Design notes

* The paper's `β(c)` is one index shifted from the Lean-native form
  `c + v₂(c!)` used in `DeltaBetaKummer.beta`. We reintroduce the paper
  convention here because the D1/E/D2 hypotheses are stated in that
  convention, and the `(mod 4)` case-split becomes clean.

* We work in `ℤ` for `D` so that no `bp ≤ β` positivity hypothesis is
  needed; downstream users can `Int.toNat` when convenient.

* Only three lemmas about the 2-adic valuation are actually used:
  `v₂(4k) = 2 + v₂(k)` (for `k ≥ 1`), `v₂(4k+2) = 1`, and the Kummer
  step `β(c+2) − β(c+1) = 1 + v₂(c+1)`.
-/

namespace DeltaDClosed

open Nat

/-- Fact instance for the prime `2`, so the `padicValNat` API is available. -/
instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩

/-- Paper-β: `β(0) := 0`, `β(c+1) := c + v₂(c!)`.

Equivalently, `β(c) = (c-1) + v₂((c-1)!)` for `c ≥ 1`. This matches
Rick's `β(5) = 7`, `β(4) = 4`, `β(6) = 8`, etc. -/
def beta : ℕ → ℕ
  | 0     => 0
  | c + 1 => c + padicValNat 2 c.factorial

/-- Forward Kummer step: `β(c+2) − β(c+1) = 1 + v₂(c+1)`. -/
lemma beta_step_int (c : ℕ) :
    (beta (c + 2) : ℤ) - (beta (c + 1) : ℤ)
      = 1 + (padicValNat 2 (c + 1) : ℤ) := by
  change (((c + 1) + padicValNat 2 (c + 1).factorial : ℕ) : ℤ)
        - ((c + padicValNat 2 c.factorial : ℕ) : ℤ) = _
  rw [Nat.factorial_succ,
      padicValNat.mul (Nat.succ_ne_zero c) c.factorial_ne_zero]
  push_cast
  ring

/-- **D1**: Rick's Δβ' closed form at odd c ≥ 3.
`β'(c) − β'(c-1) = 1 − max(2, v₂(c-1))`. -/
def HypD1 (bp : ℕ → ℕ) : Prop :=
  ∀ c, Odd c → 3 ≤ c →
    (bp c : ℤ) - (bp (c - 1) : ℤ)
      = 1 - (max 2 (padicValNat 2 (c - 1)) : ℤ)

/-- **(E)**: `β'(4k) = β(4k)`. -/
def HypE (bp : ℕ → ℕ) : Prop :=
  ∀ k, bp (4 * k) = beta (4 * k)

/-- **D2**: `β'(4k+2) = β(4k+2) − 1 − v₂(k)` for k ≥ 1. -/
def HypD2 (bp : ℕ → ℕ) : Prop :=
  ∀ k, 1 ≤ k →
    (bp (4 * k + 2) : ℤ)
      = (beta (4 * k + 2) : ℤ) - 1 - (padicValNat 2 k : ℤ)

/-- Integer-valued carry gap `D(c) := β(c) − β'(c)`. -/
def D (bp : ℕ → ℕ) (c : ℕ) : ℤ := (beta c : ℤ) - (bp c : ℤ)

/-! ### Auxiliary 2-adic facts -/

/-- `v₂(4k) = 2 + v₂(k)` for `k ≥ 1`. -/
lemma v2_four_mul (k : ℕ) (hk : 1 ≤ k) :
    padicValNat 2 (4 * k) = 2 + padicValNat 2 k := by
  have h4 : (4 : ℕ) = 2 ^ 2 := by norm_num
  have hkn : k ≠ 0 := Nat.one_le_iff_ne_zero.mp hk
  rw [h4, padicValNat.mul (by norm_num) hkn, padicValNat.prime_pow]

/-- `v₂(4k+2) = 1`. Because `4k+2 = 2 · (2k+1)` and `2k+1` is odd. -/
lemma v2_four_mul_add_two (k : ℕ) :
    padicValNat 2 (4 * k + 2) = 1 := by
  have hfact : 4 * k + 2 = 2 * (2 * k + 1) := by ring
  have hodd : ¬ (2 ∣ 2 * k + 1) := by
    intro h; omega
  rw [hfact,
      padicValNat.mul (by norm_num) (Nat.succ_ne_zero _),
      padicValNat_self,
      padicValNat.eq_zero_of_not_dvd hodd]

/-! ### The four `D` closed-form lemmas -/

/-- **D at `c = 4k`.**  From `HypE` alone: `D bp (4k) = 0`. -/
theorem D_at_4k (bp : ℕ → ℕ) (hE : HypE bp) (k : ℕ) :
    D bp (4 * k) = 0 := by
  unfold D
  rw [hE k]
  ring

/-- **D at `c = 4k+2`.**  From `HypD2` alone: `D bp (4k+2) = 1 + v₂(k)`. -/
theorem D_at_4k_add_2 (bp : ℕ → ℕ) (hD2 : HypD2 bp) (k : ℕ) (hk : 1 ≤ k) :
    D bp (4 * k + 2) = 1 + (padicValNat 2 k : ℤ) := by
  unfold D
  rw [hD2 k hk]
  ring

/-- **D at `c = 4k+1`.**  From `HypD1 + HypE` (with k ≥ 1):
`D bp (4k+1) = 4 + 2 · v₂(k)`. -/
theorem D_at_4k_add_1 (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hE : HypE bp) (k : ℕ) (hk : 1 ≤ k) :
    D bp (4 * k + 1) = 4 + 2 * (padicValNat 2 k : ℤ) := by
  -- Apply D1 at c := 4k+1 (odd, ≥ 3 since k ≥ 1).
  have hc_odd : Odd (4 * k + 1) := ⟨2 * k, by ring⟩
  have hc_ge : 3 ≤ 4 * k + 1 := by omega
  have hD1' : (bp (4 * k + 1) : ℤ) - (bp (4 * k + 1 - 1) : ℤ)
        = 1 - (max 2 (padicValNat 2 (4 * k + 1 - 1)) : ℤ) :=
    hD1 (4 * k + 1) hc_odd hc_ge
  have hpred : 4 * k + 1 - 1 = 4 * k := by omega
  rw [hpred] at hD1'
  -- v₂(4k) = 2 + v₂(k) ≥ 2, so max 2 (v₂(4k)) = v₂(4k) = 2 + v₂(k).
  have hv : padicValNat 2 (4 * k) = 2 + padicValNat 2 k := v2_four_mul k hk
  have hv_int : ((padicValNat 2 (4 * k)) : ℤ) = 2 + (padicValNat 2 k : ℤ) := by
    exact_mod_cast hv
  have hmax : max (2 : ℤ) ((padicValNat 2 (4 * k)) : ℤ) = 2 + (padicValNat 2 k : ℤ) := by
    rw [hv_int, max_eq_right]
    have : (0 : ℤ) ≤ (padicValNat 2 k : ℤ) := by positivity
    linarith
  rw [hmax] at hD1'
  -- Substitute β'(4k) = β(4k) via (E).
  have hE' : bp (4 * k) = beta (4 * k) := hE k
  -- Reformulate: bp(4k+1) = bp(4k) + (1 - (2 + v₂ k)) = β(4k) - 1 - v₂ k
  -- and D(4k+1) = β(4k+1) - bp(4k+1) = β(4k+1) - β(4k) + 1 + v₂ k
  --             = (1 + v₂(4k)) + 1 + v₂ k = 4 + 2 v₂ k.
  have hbeta_step :
      (beta (4 * k + 1) : ℤ) - (beta (4 * k) : ℤ)
        = 1 + (padicValNat 2 (4 * k) : ℤ) := by
    -- beta_step_int with c := 4k - 1: (4k-1)+2 = 4k+1, (4k-1)+1 = 4k.
    have hbase := beta_step_int (4 * k - 1)
    have h1 : 4 * k - 1 + 2 = 4 * k + 1 := by omega
    have h2 : 4 * k - 1 + 1 = 4 * k := by omega
    rw [h1, h2] at hbase
    exact hbase
  unfold D
  push_cast
  push_cast at hbeta_step
  push_cast at hD1'
  push_cast at hv
  linarith

/-- **D at `c = 4k+3`.**  From `HypD1 + HypD2` (with k ≥ 1):
`D bp (4k+3) = 4 + v₂(k)`. -/
theorem D_at_4k_add_3 (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hD2 : HypD2 bp) (k : ℕ) (hk : 1 ≤ k) :
    D bp (4 * k + 3) = 4 + (padicValNat 2 k : ℤ) := by
  -- Apply D1 at c := 4k+3 (odd, ≥ 3).
  have hc_odd : Odd (4 * k + 3) := ⟨2 * k + 1, by ring⟩
  have hc_ge : 3 ≤ 4 * k + 3 := by omega
  have hD1' : (bp (4 * k + 3) : ℤ) - (bp (4 * k + 3 - 1) : ℤ)
        = 1 - (max 2 (padicValNat 2 (4 * k + 3 - 1)) : ℤ) :=
    hD1 (4 * k + 3) hc_odd hc_ge
  have hpred : 4 * k + 3 - 1 = 4 * k + 2 := by omega
  rw [hpred] at hD1'
  -- v₂(4k+2) = 1, so max 2 1 = 2 (at ℤ).
  have hv : padicValNat 2 (4 * k + 2) = 1 := v2_four_mul_add_two k
  have hv_int : ((padicValNat 2 (4 * k + 2)) : ℤ) = 1 := by exact_mod_cast hv
  have hmax : max (2 : ℤ) ((padicValNat 2 (4 * k + 2)) : ℤ) = 2 := by
    rw [hv_int]; decide
  rw [hmax] at hD1'
  -- β'(4k+2) = β(4k+2) - 1 - v₂ k (by D2, k ≥ 1).
  have hD2' := hD2 k hk
  -- Kummer step: β(4k+3) - β(4k+2) = 1 + v₂(4k+2) = 2.
  have hbeta_step :
      (beta (4 * k + 3) : ℤ) - (beta (4 * k + 2) : ℤ)
        = 1 + (padicValNat 2 (4 * k + 2) : ℤ) := by
    have := beta_step_int (4 * k + 1)
    have h1 : 4 * k + 1 + 2 = 4 * k + 3 := by ring
    have h2 : 4 * k + 1 + 1 = 4 * k + 2 := by ring
    rw [h1, h2] at this
    exact this
  unfold D
  push_cast
  push_cast at hbeta_step
  push_cast at hD1'
  push_cast at hD2'
  push_cast at hv
  linarith

/-! ### Corollary: `ΔD` case-split -/

/-- One-step forward difference of `D`. -/
def deltaD (bp : ℕ → ℕ) (c : ℕ) : ℤ := D bp (c + 1) - D bp c

/-- **ΔD at `c = 4k` (k ≥ 1):** `ΔD(4k) = 4 + 2 v₂(k)`. -/
theorem deltaD_at_4k (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hE : HypE bp) (k : ℕ) (hk : 1 ≤ k) :
    deltaD bp (4 * k) = 4 + 2 * (padicValNat 2 k : ℤ) := by
  unfold deltaD
  have h1 : D bp (4 * k + 1) = 4 + 2 * (padicValNat 2 k : ℤ) :=
    D_at_4k_add_1 bp hD1 hE k hk
  have h2 : D bp (4 * k) = 0 := D_at_4k bp hE k
  linarith

/-- **ΔD at `c = 4k+1` (k ≥ 1):** `ΔD(4k+1) = -3 - v₂(k)`. -/
theorem deltaD_at_4k_add_1 (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hE : HypE bp) (hD2 : HypD2 bp) (k : ℕ) (hk : 1 ≤ k) :
    deltaD bp (4 * k + 1) = -3 - (padicValNat 2 k : ℤ) := by
  unfold deltaD
  have h1 : 4 * k + 1 + 1 = 4 * k + 2 := by ring
  rw [h1]
  have hA : D bp (4 * k + 2) = 1 + (padicValNat 2 k : ℤ) :=
    D_at_4k_add_2 bp hD2 k hk
  have hB : D bp (4 * k + 1) = 4 + 2 * (padicValNat 2 k : ℤ) :=
    D_at_4k_add_1 bp hD1 hE k hk
  linarith

/-- **ΔD at `c = 4k+2` (k ≥ 1):** `ΔD(4k+2) = 3`. -/
theorem deltaD_at_4k_add_2 (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hD2 : HypD2 bp) (k : ℕ) (hk : 1 ≤ k) :
    deltaD bp (4 * k + 2) = 3 := by
  unfold deltaD
  have h1 : 4 * k + 2 + 1 = 4 * k + 3 := by ring
  rw [h1]
  have hA : D bp (4 * k + 3) = 4 + (padicValNat 2 k : ℤ) :=
    D_at_4k_add_3 bp hD1 hD2 k hk
  have hB : D bp (4 * k + 2) = 1 + (padicValNat 2 k : ℤ) :=
    D_at_4k_add_2 bp hD2 k hk
  linarith

/-- **ΔD at `c = 4k+3` (k ≥ 1):** `ΔD(4k+3) = -4 - v₂(k)`.

Uses `D(4(k+1)) = 0` in the numerator. -/
theorem deltaD_at_4k_add_3 (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hE : HypE bp) (hD2 : HypD2 bp) (k : ℕ) (hk : 1 ≤ k) :
    deltaD bp (4 * k + 3) = -4 - (padicValNat 2 k : ℤ) := by
  unfold deltaD
  have h1 : 4 * k + 3 + 1 = 4 * (k + 1) := by ring
  rw [h1]
  have hA : D bp (4 * (k + 1)) = 0 := D_at_4k bp hE (k + 1)
  have hB : D bp (4 * k + 3) = 4 + (padicValNat 2 k : ℤ) :=
    D_at_4k_add_3 bp hD1 hD2 k hk
  linarith

/-! ### Bundled top-level ΔD closed form

Packages the four `deltaD_at_4k*` corollaries into a single statement
indexed by `c` (not `k, r`), matching the shape of the LEAN.md target
theorem `delta_D_closed`.  The proof case-splits on `c % 4`.
-/

/-- Uniform closed form for `ΔD` as a function of `c`.

For `c ≥ 4`, `deltaD bp c = closedFormΔD c` under {D1, E, D2}. The
residue class of `c` mod 4 selects one of four cases; `k := c / 4` is
the shared "period index". -/
def closedFormΔD (c : ℕ) : ℤ :=
  if c % 4 = 0 then 4 + 2 * (padicValNat 2 (c / 4) : ℤ)
  else if c % 4 = 1 then -3 - (padicValNat 2 (c / 4) : ℤ)
  else if c % 4 = 2 then 3
  else -4 - (padicValNat 2 (c / 4) : ℤ)

/-- **Bundled ΔD closed form (`c ≥ 4`).**  Under {D1, E, D2},

    deltaD bp c = closedFormΔD c   for every `c ≥ 4`.

The lower bound `4 ≤ c` is exactly what one needs to guarantee `c/4 ≥ 1`
in every residue class (needed by `deltaD_at_4k_*` for `hk : 1 ≤ k`). -/
theorem delta_D_closed (bp : ℕ → ℕ)
    (hD1 : HypD1 bp) (hE : HypE bp) (hD2 : HypD2 bp)
    {c : ℕ} (hc : 4 ≤ c) :
    deltaD bp c = closedFormΔD c := by
  set k := c / 4 with hk_def
  have hk : 1 ≤ k := (Nat.one_le_div_iff (by norm_num : (0 : ℕ) < 4)).mpr hc
  have hrlt : c % 4 < 4 := Nat.mod_lt _ (by norm_num)
  -- Case-split on the residue r := c % 4 ∈ {0, 1, 2, 3}.
  interval_cases hr : (c % 4)
  · -- r = 0 : c = 4k, apply deltaD_at_4k.
    have hceq : c = 4 * k := by omega
    have h1 : (4 * k) % 4 = 0 := by omega
    have h2 : (4 * k) / 4 = k := by omega
    rw [hceq, deltaD_at_4k bp hD1 hE k hk]
    simp [closedFormΔD, h1, h2]
  · -- r = 1 : c = 4k + 1.
    have hceq : c = 4 * k + 1 := by omega
    have h1 : (4 * k + 1) % 4 = 1 := by omega
    have h2 : (4 * k + 1) / 4 = k := by omega
    rw [hceq, deltaD_at_4k_add_1 bp hD1 hE hD2 k hk]
    simp [closedFormΔD, h1, h2]
  · -- r = 2 : c = 4k + 2.
    have hceq : c = 4 * k + 2 := by omega
    have h1 : (4 * k + 2) % 4 = 2 := by omega
    have h2 : (4 * k + 2) / 4 = k := by omega
    rw [hceq, deltaD_at_4k_add_2 bp hD1 hD2 k hk]
    simp [closedFormΔD, h1]
  · -- r = 3 : c = 4k + 3.
    have hceq : c = 4 * k + 3 := by omega
    have h1 : (4 * k + 3) % 4 = 3 := by omega
    have h2 : (4 * k + 3) / 4 = k := by omega
    rw [hceq, deltaD_at_4k_add_3 bp hD1 hE hD2 k hk]
    simp [closedFormΔD, h1, h2]

end DeltaDClosed

-- Axiom audit (leave in place during review; comment out for library use).
#print axioms DeltaDClosed.D_at_4k
#print axioms DeltaDClosed.D_at_4k_add_1
#print axioms DeltaDClosed.D_at_4k_add_2
#print axioms DeltaDClosed.D_at_4k_add_3
#print axioms DeltaDClosed.deltaD_at_4k
#print axioms DeltaDClosed.deltaD_at_4k_add_1
#print axioms DeltaDClosed.deltaD_at_4k_add_2
#print axioms DeltaDClosed.deltaD_at_4k_add_3
#print axioms DeltaDClosed.delta_D_closed
