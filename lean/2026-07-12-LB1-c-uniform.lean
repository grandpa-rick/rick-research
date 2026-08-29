/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises the F2 warm-up bound `LB_1_c_uniform` of the β'(c) program,
using the Day-91 CODE-cycle result that `Q_1(a,b,c) = -c(c-1)`
uniformly in `(a,b)` (see registry node `F2-Delta1-c-uniform`).

## What this file proves (honestly)

The upstream chain (Day 88's HK three-variable factorization + Day 91's
constant-Q_1 discovery) gives, at k = 1 (clean regime, `c ≥ 3`),

    h_1^{(c)}(a,b) = (a+3)_{c-2} · (b+2)_{c-2} · Q_1(a,b,c)         (★)

with

    Q_1(a,b,c) = -c(c-1)     (uniformly in a, b — Day 91 CODE result).

Taking `v_2` of (★) and using multiplicativity of `padicValInt` gives the
per-point 2-adic decomposition

    v_2(h_1^{(c)}(a,b)) = v_2(c) + v_2(c-1)
                       + v_2((a+3)_{c-2}) + v_2((b+2)_{c-2}) .        (F2)

That decomposition — `hOne_padicVal_decomp` — is fully proved here, no
sorrys, minimum axiom set. It is the "F2 warm-up" ingredient.

## Day 93 update: LB_1_c_uniform closed, `lean-verified`

The existential shell-achievability lemma `min_v2_asc_poch_shell` is
now proved from scratch (no Kummer, no Legendre digit-sum) via the
witness `x₀ + shift = 2^K + 1` with `K = (c-2) + shift.toNat + 1`.
For each `i ∈ {1,…,c-2}`, since `i < 2^K` and `v_2(i) < K`, we have
`v_2(2^K + i) = v_2(i)` — a clean 2-adic congruence lemma. Summing
gives `v_2(∏ (2^K + i)) = ∑ v_2(i) = v_2((c-2)!)`.

Both `hOne_padicVal_decomp` and `LB_1_c_uniform` now depend on axioms
`[propext, Classical.choice, Quot.sound]` — the Lean-4 default.

### Python sanity check (K = c witness, from
    projects/code/2026-07-13-min-v2-shell-sanity.py):

    c=3  L=1 shift=2  K=3  x₀=7    v_2=0=v_2(1!)  ✓
    c=4  L=2 shift=2  K=4  x₀=15   v_2=1=v_2(2!)  ✓
    c=5  L=3 shift=2  K=5  x₀=31   v_2=1=v_2(3!)  ✓
    c=6  L=4 shift=2  K=6  x₀=63   v_2=3=v_2(4!)  ✓
    c=7  L=5 shift=2  K=7  x₀=127  v_2=3=v_2(5!)  ✓
    c=8  L=6 shift=2  K=8  x₀=255  v_2=4=v_2(6!)  ✓
    (shift=3 witnesses = shift=2 witness − 1; all pass identically.)
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Nat.Factorial.BigOperators
import Mathlib.Data.Nat.Log
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace LB1CUniform

open Finset

/-! ### Ascending Pochhammer product (duplicated from Day 88 for self-containment) -/

/-- Rising factorial `(x)_n = x(x+1)⋯(x+n-1)`. -/
def ascPoch (x : ℤ) (n : ℕ) : ℤ := ∏ i ∈ range n, (x + (i : ℤ))

@[simp] lemma ascPoch_zero (x : ℤ) : ascPoch x 0 = 1 := by
  simp [ascPoch]

lemma ascPoch_succ (x : ℤ) (n : ℕ) :
    ascPoch x (n + 1) = ascPoch x n * (x + n) := by
  simp [ascPoch, prod_range_succ]

/-! ### `p`-adic prime-2 fact instance -/

/-- Fact instance for the prime `2`, so the `padicValInt` API is available. -/
instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩

/-! ### F2 core: h_1 factored form and its v₂ decomposition

We do **not** re-derive the HK three-variable factorization here; we take
its k = 1 (clean-regime) output and the Day-91 `Q_1 = -c(c-1)` result as
a hypothesis on the value of `h_1`. This isolates the arithmetic bound
from the (already proved) algebra. -/

/-- **Hypothesis form of the Day-91 F2 factorization.** Says the k=1
Möbius transform `h_1^{(c)}(a,b)` factors as `(a+3)_{c-2} · (b+2)_{c-2}`
times the constant `-c(c-1)`. Downstream: instantiate with the value
`h_1^{(c)}(a,b)` extracted from Clio's H_c / P_j formalisation. -/
def F2Factored (hOne : ℕ → ℕ → ℤ) (c : ℕ) : Prop :=
  ∀ a b : ℕ,
    hOne a b
      = ascPoch ((a : ℤ) + 3) (c - 2)
        * ascPoch ((b : ℤ) + 2) (c - 2)
        * (-(c : ℤ) * ((c : ℤ) - 1))

/-! ### Non-vanishing of the Pochhammer and the constant `-c(c-1)` -/

/-- `(x)_n` is a product of consecutive integers starting at `x`. In our
setting `x = a + 3` or `x = b + 2` with `a, b : ℕ`, so `x ≥ 2 > 0` and
every factor is strictly positive. -/
lemma ascPoch_pos_of_pos (x : ℤ) (hx : 0 < x) (n : ℕ) : 0 < ascPoch x n := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [ascPoch_succ]
    have hfac : 0 < x + (k : ℤ) := by
      have : (0 : ℤ) ≤ (k : ℤ) := Int.natCast_nonneg k
      linarith
    exact mul_pos ih hfac

lemma ascPoch_a_plus_three_pos (a : ℕ) (n : ℕ) :
    0 < ascPoch ((a : ℤ) + 3) n := by
  apply ascPoch_pos_of_pos
  have : (0 : ℤ) ≤ (a : ℤ) := Int.natCast_nonneg a
  linarith

lemma ascPoch_b_plus_two_pos (b : ℕ) (n : ℕ) :
    0 < ascPoch ((b : ℤ) + 2) n := by
  apply ascPoch_pos_of_pos
  have : (0 : ℤ) ≤ (b : ℤ) := Int.natCast_nonneg b
  linarith

lemma ascPoch_a_plus_three_ne_zero (a : ℕ) (n : ℕ) :
    ascPoch ((a : ℤ) + 3) n ≠ 0 :=
  ne_of_gt (ascPoch_a_plus_three_pos a n)

lemma ascPoch_b_plus_two_ne_zero (b : ℕ) (n : ℕ) :
    ascPoch ((b : ℤ) + 2) n ≠ 0 :=
  ne_of_gt (ascPoch_b_plus_two_pos b n)

lemma neg_c_mul_c_sub_one_ne_zero {c : ℕ} (hc : 2 ≤ c) :
    (-(c : ℤ) * ((c : ℤ) - 1)) ≠ 0 := by
  have hc1 : (c : ℤ) ≠ 0 := by exact_mod_cast (by omega : c ≠ 0)
  have hc2 : (c : ℤ) - 1 ≠ 0 := by
    have : (2 : ℤ) ≤ (c : ℤ) := by exact_mod_cast hc
    intro h; linarith
  intro h
  rcases mul_eq_zero.mp h with h1 | h2
  · exact hc1 (by linarith)
  · exact hc2 h2

lemma c_int_ne_zero {c : ℕ} (hc : 2 ≤ c) : (c : ℤ) ≠ 0 := by
  exact_mod_cast (by omega : c ≠ 0)

lemma c_sub_one_int_ne_zero {c : ℕ} (hc : 2 ≤ c) : ((c : ℤ) - 1) ≠ 0 := by
  have : (2 : ℤ) ≤ (c : ℤ) := by exact_mod_cast hc
  intro h; linarith

lemma neg_c_int_ne_zero {c : ℕ} (hc : 2 ≤ c) : (-(c : ℤ)) ≠ 0 := by
  have := c_int_ne_zero hc
  intro h
  apply this
  linarith

/-! ### v₂ of `-c` reduces to v₂ of `c`.

`padicValInt` is defined via `natAbs`, so absolute-value / negation
does not shift it. -/

lemma padicValInt_neg_natCast (c : ℕ) :
    padicValInt 2 (-(c : ℤ)) = padicValNat 2 c := by
  unfold padicValInt
  rw [Int.natAbs_neg, Int.natAbs_natCast]

/-! ### F2 core theorem: 2-adic decomposition of `h_1^{(c)}(a,b)`

Under the `F2Factored` hypothesis (which packages Day 88 + Day 91), the
`v_2` of `h_1^{(c)}(a,b)` splits additively over the four factors of
`(a+3)_{c-2} · (b+2)_{c-2} · (-c) · (c-1)`.

This is the "F2 warm-up" lemma — Rick's registry `F2-Delta1-c-uniform`
at the point-wise (not min-over-shell) level. -/

theorem hOne_padicVal_decomp
    {hOne : ℕ → ℕ → ℤ} {c : ℕ} (hc : 2 ≤ c)
    (hyp : F2Factored hOne c) (a b : ℕ) :
    padicValInt 2 (hOne a b)
      = padicValInt 2 (ascPoch ((a : ℤ) + 3) (c - 2))
        + padicValInt 2 (ascPoch ((b : ℤ) + 2) (c - 2))
        + padicValNat 2 c
        + padicValInt 2 ((c : ℤ) - 1) := by
  rw [hyp a b]
  -- non-vanishing of each factor
  have hA := ascPoch_a_plus_three_ne_zero a (c - 2)
  have hB := ascPoch_b_plus_two_ne_zero b (c - 2)
  have hNegC := neg_c_int_ne_zero hc
  have hCm1 := c_sub_one_int_ne_zero hc
  -- (a+3)_{c-2} · (b+2)_{c-2} ≠ 0
  have hAB : ascPoch ((a : ℤ) + 3) (c - 2) * ascPoch ((b : ℤ) + 2) (c - 2) ≠ 0 :=
    mul_ne_zero hA hB
  -- (a+3)_{c-2} · (b+2)_{c-2} · (-c) ≠ 0
  have hABC : ascPoch ((a : ℤ) + 3) (c - 2) * ascPoch ((b : ℤ) + 2) (c - 2)
                * (-(c : ℤ)) ≠ 0 :=
    mul_ne_zero hAB hNegC
  -- Reassociate the RHS factorisation:
  --   (a+3)_{c-2} · (b+2)_{c-2} · (-c · (c-1))
  -- = ((a+3)_{c-2} · (b+2)_{c-2} · (-c)) · (c-1)
  have hRewrite :
      ascPoch ((a : ℤ) + 3) (c - 2) * ascPoch ((b : ℤ) + 2) (c - 2)
          * (-(c : ℤ) * ((c : ℤ) - 1))
        = ascPoch ((a : ℤ) + 3) (c - 2) * ascPoch ((b : ℤ) + 2) (c - 2)
          * (-(c : ℤ)) * ((c : ℤ) - 1) := by ring
  rw [hRewrite]
  rw [padicValInt.mul hABC hCm1]
  rw [padicValInt.mul hAB hNegC]
  rw [padicValInt.mul hA hB]
  rw [padicValInt_neg_natCast]

/-! ### Shell achievability of `v_2((x + shift)_{c-2}) = v_2((c-2)!)`

The Day-91 F2 factorisation lower bound requires that the 2-adic
valuation of `(a+3)_{c-2}` (and `(b+2)_{c-2}`) can be made as small
as `v_2((c-2)!)` at *some* shell point. This is the existential form:
we exhibit a concrete `x₀` with `v_2((x₀ + shift)_{c-2}) = v_2((c-2)!)`.

**Witness.** Take `x₀ + shift = 2^K + 1` for `K` sufficiently large
(specifically `K = c + shift.toNat + 1`, so `2^K > c-2` and
`2^K > shift.toNat`). Then

    (x₀+shift)(x₀+shift+1)⋯(x₀+shift+(c-3))
      = (2^K + 1)(2^K + 2)⋯(2^K + (c-2))

and for each `i ∈ {1,…,c-2}`, since `i < 2^K` and `v_2(i) < K`, we have
`v_2(2^K + i) = v_2(i)` (Lemma `padicValNat_two_pow_add`). Summing
over `i`,

    v_2(∏ (2^K + i)) = ∑ v_2(i) = v_2((c-2)!).

No Legendre digit-sum, no Kummer's theorem — pure block arithmetic
on the 2-adic valuation. -/

/-- **Helper (2-adic congruence).** For `k ≠ 0` and `K` strictly greater
than the 2-adic valuation of `k`, adding `2^K` to `k` does not shift its
2-adic valuation. Intuitively: `2^K` is divisible by a higher power of
`2` than `k`, so `2^K + k ≡ k (mod 2^(v_2(k) + 1))`. -/
private lemma padicValNat_two_pow_add {K k : ℕ}
    (hk : k ≠ 0) (hK : padicValNat 2 k < K) :
    padicValNat 2 (2 ^ K + k) = padicValNat 2 k := by
  set v := padicValNat 2 k with hv_def
  have h2K : 2 ^ (v + 1) ∣ 2 ^ K := pow_dvd_pow 2 hK
  have hvk : 2 ^ v ∣ k := pow_padicValNat_dvd
  have hvk' : ¬ 2 ^ (v + 1) ∣ k := pow_succ_padicValNat_not_dvd hk
  have hpow_pos : 0 < 2 ^ K := Nat.two_pow_pos K
  have hsum_ne : 2 ^ K + k ≠ 0 := by
    intro h
    exact absurd h (Nat.add_pos_left hpow_pos k).ne'
  refine Nat.le_antisymm ?upper ?lower
  case upper =>
    by_contra hcon
    have hle : v + 1 ≤ padicValNat 2 (2 ^ K + k) := Nat.lt_of_not_le hcon
    have hdvd : (2 : ℕ) ^ (v + 1) ∣ (2 ^ K + k) :=
      (padicValNat_dvd_iff_le hsum_ne).mpr hle
    have hdvd_k : (2 : ℕ) ^ (v + 1) ∣ k := (Nat.dvd_add_right h2K).mp hdvd
    exact hvk' hdvd_k
  case lower =>
    apply (padicValNat_dvd_iff_le hsum_ne).mp
    exact Nat.dvd_add (pow_dvd_pow 2 (Nat.le_of_lt hK)) hvk

/-- **Helper (block product identity).** The product of `n` consecutive
integers starting at `2^K + 1` (with `n < 2^K`, so no carries in base 2)
has the same 2-adic valuation as `n!`. Proof by induction on `n`. -/
private lemma padicValNat_prod_two_pow_shifted {K : ℕ} :
    ∀ {n : ℕ}, n < 2 ^ K →
      padicValNat 2 (∏ i ∈ range n, (2 ^ K + (i + 1))) =
        padicValNat 2 (Nat.factorial n) := by
  intro n
  induction n with
  | zero => intro _; simp
  | succ m ih =>
    intro hK
    have hK' : m < 2 ^ K := lt_trans (Nat.lt_succ_self m) hK
    have ih' := ih hK'
    rw [Finset.prod_range_succ, Nat.factorial_succ]
    have hne1 : ∏ i ∈ Finset.range m, (2 ^ K + (i + 1)) ≠ 0 := by
      refine Finset.prod_ne_zero_iff.mpr (fun i _ => ?_)
      have : 0 < 2 ^ K + (i + 1) := Nat.add_pos_left (Nat.two_pow_pos K) _
      exact this.ne'
    have hne2 : (2 ^ K + (m + 1) : ℕ) ≠ 0 :=
      (Nat.add_pos_left (Nat.two_pow_pos K) _).ne'
    have hne3 : (m + 1 : ℕ) ≠ 0 := Nat.succ_ne_zero m
    have hne4 : Nat.factorial m ≠ 0 := Nat.factorial_ne_zero m
    rw [padicValNat.mul hne1 hne2, ih']
    rw [padicValNat.mul hne3 hne4]
    have hbd : padicValNat 2 (m + 1) < K := by
      calc padicValNat 2 (m + 1)
          ≤ Nat.log 2 (m + 1) := padicValNat_le_nat_log _
        _ < K := Nat.log_lt_of_lt_pow hne3 hK
    rw [padicValNat_two_pow_add hne3 hbd]
    ring

/-- **Cast helper.** Rewriting `ascPoch (2^K + 1) n` as the ℤ-cast of a
Nat product. -/
private lemma ascPoch_two_pow_succ_eq (K n : ℕ) :
    ascPoch ((2 ^ K : ℕ) + 1 : ℤ) n =
      ((∏ i ∈ range n, (2 ^ K + (i + 1)) : ℕ) : ℤ) := by
  unfold ascPoch
  push_cast
  refine Finset.prod_congr rfl (fun i _ => ?_)
  ring

/-- **The shell achievability lemma.** There exists a natural number
`x₀` at which the 2-adic valuation of the ascending Pochhammer
`(x₀ + shift)_{c-2}` equals `v_2((c-2)!)`. Concretely, take
`x₀ = 2^K + 1 - shift.toNat` for `K = c + shift.toNat + 1`. -/
lemma min_v2_asc_poch_shell (c : ℕ) (_hc : 2 ≤ c) (shift : ℤ) (hshift : 0 < shift) :
    ∃ x₀ : ℕ, padicValInt 2 (ascPoch ((x₀ : ℤ) + shift) (c - 2))
              = padicValNat 2 (Nat.factorial (c - 2)) := by
  set s : ℕ := shift.toNat with hs_def
  have hs_cast : (s : ℤ) = shift := Int.toNat_of_nonneg hshift.le
  have hs_pos : 0 < s := by
    have : (0 : ℤ) < (s : ℤ) := by rw [hs_cast]; exact hshift
    exact_mod_cast this
  -- L = c - 2
  set L : ℕ := c - 2 with hL_def
  -- Choose K = L + s + 1 (so 2^K > L and 2^K > s).
  set K : ℕ := L + s + 1 with hK_def
  have hK_pos : 0 < K := by positivity
  have hK_gt_L : L < 2 ^ K := by
    have : K < 2 ^ K := Nat.lt_two_pow_self
    omega
  have hK_gt_s : s < 2 ^ K := by
    have : K < 2 ^ K := Nat.lt_two_pow_self
    omega
  have hs_le_pow : s ≤ 2 ^ K := le_of_lt hK_gt_s
  -- Define the witness x₀ = 2^K + 1 - s (as a Nat).
  set x₀ : ℕ := 2 ^ K + 1 - s with hx₀_def
  refine ⟨x₀, ?_⟩
  -- Key: (x₀ : ℤ) + shift = 2^K + 1.
  have hcast : (x₀ : ℤ) + shift = (2 ^ K : ℕ) + 1 := by
    rw [← hs_cast]
    have hs' : s ≤ 2 ^ K + 1 := by omega
    have hsub : ((2 ^ K + 1 - s : ℕ) : ℤ) = ((2 ^ K + 1 : ℕ) : ℤ) - (s : ℤ) :=
      Nat.cast_sub hs'
    change ((2 ^ K + 1 - s : ℕ) : ℤ) + (s : ℤ) = ((2 ^ K : ℕ) : ℤ) + 1
    rw [hsub]
    push_cast
    ring
  rw [hcast]
  -- Now: padicValInt 2 (ascPoch (2^K + 1) L) = padicValNat 2 L!.
  rw [ascPoch_two_pow_succ_eq]
  -- padicValInt 2 (Int.ofNat m) = padicValNat 2 m
  rw [padicValInt.of_nat]
  exact padicValNat_prod_two_pow_shifted hK_gt_L

/-! ### F2 warm-up lemma: `LB_1^{(c)}` uniform bound

Combines the point-wise `hOne_padicVal_decomp` with the shell-min
Kummer step `min_v2_asc_poch_shell` (twice — once for `a`, once for
`b` — the `b` shell has the same structure, so we reuse the same
existential lemma).

Statement: there exist shell points `(a₀, b₀)` at which the 2-adic
valuation of `h_1^{(c)}(a₀, b₀)` equals the claimed uniform lower
bound `v_2(c) + v_2(c-1) + 2·v_2((c-2)!)`. -/

theorem LB_1_c_uniform
    {hOne : ℕ → ℕ → ℤ} {c : ℕ} (hc : 2 ≤ c)
    (hyp : F2Factored hOne c) :
    ∃ a₀ b₀ : ℕ,
      padicValInt 2 (hOne a₀ b₀)
        = padicValNat 2 c
          + padicValInt 2 ((c : ℤ) - 1)
          + 2 * padicValNat 2 (Nat.factorial (c - 2)) := by
  -- a-coordinate: shift = 3 (`(a+3)_{c-2}`), Day-88 clean regime.
  obtain ⟨a₀, hA⟩ := min_v2_asc_poch_shell c hc 3 (by norm_num)
  -- b-coordinate: shift = 2 (`(b+2)_{c-2}`), Day-88 clean regime.
  obtain ⟨b₀, hB⟩ := min_v2_asc_poch_shell c hc 2 (by norm_num)
  refine ⟨a₀, b₀, ?_⟩
  rw [hOne_padicVal_decomp hc hyp a₀ b₀, hA, hB]
  ring

/-! ### Axiom audit

Both `hOne_padicVal_decomp` and `LB_1_c_uniform` should now depend on
exactly `[propext, Classical.choice, Quot.sound]` — the Lean 4 default. -/

end LB1CUniform

#print axioms LB1CUniform.hOne_padicVal_decomp
#print axioms LB1CUniform.LB_1_c_uniform
