/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises Theorem 4 (extended ★) of
`~/projects/proofs/2026-07-10-hk-three-var-structural.md` (Day 88):
the three-variable structural factorization of `h_k^{(c)}(a,b)` in its
unified (clean + boundary) form, expressed as a polynomial identity using
positive-power Pochhammer factors on both sides.

Day-89 mandatory pre-Lean k=1 data check (per LEAN.md meta-rule):

  Test: at c ∈ {4, 5, 6, 7}, k = 1 (clean regime, k ≤ c-1), the quotient
    h_1^{(c)}(a,b) / [(a+3)_{c-2} · (b+2)_{c-2}]
  must equal a constant (a,b-independent) matching D_1(c) = −c(c−1).

  Verified numerically via `code/2026-07-10-hk-three-var-verify.py`:
      c=4 → −12  ✓ = −4·3
      c=5 → −20  ✓ = −5·4
      c=6 → −30  ✓ = −6·5
      c=7 → −42  ✓ = −7·6
  Matches D_1(c) = −c(c−1) predicted by Day-88 §4 Corollary. All 91/78/66/55
  sample (a,b) points respectively give the same quotient — `Q_1` is a
  constant, as it collapses via the two-term Möbius sum. Compatibility with
  this file: in the clean regime, `hk_three_var_factorization` combined
  with `pochL_clean, pochR_clean` reads
    h_k = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k
  which is (★) of Day-88 §3 verbatim, and the k=1 check confirms that our
  `Q_k` definition matches Day-88's `Q_k`.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# `h_k^{(c)}(a,b)` three-variable Pochhammer factorization (Day 89)

Let `H : ℕ → ℕ → ℕ → ℤ` denote Clio's Lemma-1 template numerator
`H_c(a,b,j)` (Sym-side heavy quotient). Its Möbius transform in the third
argument,

    h_k^{(c)}(a,b) := ∑_{j=0..k} (-1)^{k-j} · C(k,j) · H a b j ,

admits a structural factorization: on Sym-side there is a polynomial
`P_j(a,b,c) ∈ ℤ[a,b,c]` such that for all `0 ≤ j ≤ 2c-1`,

*   `j ≤ c-1` (clean regime):
        `H a b j · (a+3)_{c-1-j} · (b+2)_{c-1-j} = P_j a b c`,
*   `j > c-1` (boundary regime; `m := j - c + 1`):
        `H a b j = (a+c-j+2)_m · (b+c-j+1)_m · P_j a b c`.

Both sides of each equation are polynomials in `(a,b,c)`; the "boundary"
is notational, not algebraic (see §11 of the Day-88 proof file).

Applying Möbius inversion + Pochhammer telescoping,

    h_k^{(c)}(a,b) · pochL c k a b = pochR c k a b · Q_k c k a b ,

with `Q_k` the analogous polynomial in `P_j`.

## Main definitions

* `ascPoch x n : ℤ` — rising-factorial product `x(x+1)⋯(x+n-1)`.
* `pochL`, `pochR` — the two Pochhammer bundles for the `h_k` identity.
* `pochHL`, `pochHR` — the analogous bundles for the `H_c` identity.
* `HFactorization H P c` — hypothesis that `H_c` factors as (♦-ext).
* `h_k_c H k a b` — Möbius transform in `j`.
* `Q_k P c k a b` — Q_k from P_j via (Q_k formula).

## Main results

* `ascPoch_split` — Pochhammer telescoping `(x)_{m+n} = (x)_m · (x+m)_n`.
* `hk_three_var_factorization_k_zero` — the `k = 0` special case, a direct
  consequence of the H-factorization at `j = 0`.
* `hk_three_var_factorization_clean` — clean regime `k ≤ c-1`, proved.
* `hk_three_var_factorization_boundary` — boundary regime `c ≤ k ≤ 2c-1`,
  proved. Inner case split on `j ≤ c-1` vs `j > c-1` handles both regimes
  of the H-hypothesis.
* `hk_three_var_factorization` — unified `0 ≤ k ≤ 2c-1` statement,
  proved. No `sorry`.

## Design notes

Both regimes reduce to term-wise Pochhammer telescoping via `ascPoch_split`.
* Clean regime `k ≤ c-1`: every summand's `j ≤ k ≤ c-1` sits in the clean
  H-regime, so the split of `(c-1-j) = (c-1-k) + (k-j)` factors out the
  common `(a+3)_{c-1-k}(b+2)_{c-1-k}` and reveals the `Q_k` sum.
* Boundary regime `k > c-1`: the Möbius sum mixes clean `j ≤ c-1` and
  boundary `j > c-1` terms. Inner case split:
    - `j ≤ c-1`: split `(k-j) = (k-c+1) + (c-1-j)` and use the clean H;
    - `j > c-1`: split `(k-c+1) = (k-j) + (j-c+1)` and use the boundary
      H via `linear_combination`.

Day-88 §11.6 (Rick, second cycle): "the boundary was never a genuine
mathematical obstruction — only a notational choice." The Lean formalisation
confirms: the same `ascPoch_split` identity, applied at different indices,
closes all sub-cases.
-/

namespace HkThreeVar

open Finset

/-! ### Ascending Pochhammer product -/

/-- Rising factorial `(x)_n = x(x+1)⋯(x+n-1)`. -/
def ascPoch (x : ℤ) (n : ℕ) : ℤ := ∏ i ∈ range n, (x + (i : ℤ))

@[simp] lemma ascPoch_zero (x : ℤ) : ascPoch x 0 = 1 := by
  simp [ascPoch]

lemma ascPoch_succ (x : ℤ) (n : ℕ) :
    ascPoch x (n + 1) = ascPoch x n * (x + n) := by
  simp [ascPoch, prod_range_succ]

@[simp] lemma ascPoch_one (x : ℤ) : ascPoch x 1 = x := by
  simp [ascPoch_succ]

/-- Pochhammer telescoping: `(x)_{m+n} = (x)_m · (x+m)_n`. -/
lemma ascPoch_split (x : ℤ) (m n : ℕ) :
    ascPoch x (m + n) = ascPoch x m * ascPoch (x + m) n := by
  induction n with
  | zero => simp
  | succ k ih =>
    have : m + (k + 1) = (m + k) + 1 := by ring
    rw [this, ascPoch_succ, ih, ascPoch_succ]
    push_cast
    ring

/-! ### Pochhammer bundles

We define two Pochhammer factors depending on whether the index is in the
"clean" regime `≤ c-1` or the "boundary" regime `> c-1`. -/

/-- `pochL c k a b`: LHS Pochhammer for the `h_k` identity.
Equals `1` in the clean regime `k ≤ c-1`.
In the boundary regime `k > c-1`, with `m := k - c + 1`, equals
`(a+c-k+2)_m · (b+c-k+1)_m`. -/
def pochL (c k a b : ℕ) : ℤ :=
  if k ≤ c - 1 then 1
  else
    let m := k - c + 1
    ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) m
      * ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) m

/-- `pochR c k a b`: RHS Pochhammer for the `h_k` identity.
Equals `1` in the boundary regime `k > c-1`.
In the clean regime `k ≤ c-1`, equals `(a+3)_{c-1-k} · (b+2)_{c-1-k}`. -/
def pochR (c k a b : ℕ) : ℤ :=
  if k ≤ c - 1 then
    ascPoch ((a : ℤ) + 3) (c - 1 - k) * ascPoch ((b : ℤ) + 2) (c - 1 - k)
  else 1

/-- `pochHL c j a b`: LHS Pochhammer for the `H_c` identity.
Equals `1` in the clean regime `j ≤ c-1`.
In the boundary regime, equals `(a+c-j+2)_{j-c+1} · (b+c-j+1)_{j-c+1}`. -/
def pochHL (c j a b : ℕ) : ℤ :=
  if j ≤ c - 1 then 1
  else
    let m := j - c + 1
    ascPoch ((a : ℤ) + (c : ℤ) - (j : ℤ) + 2) m
      * ascPoch ((b : ℤ) + (c : ℤ) - (j : ℤ) + 1) m

/-- `pochHR c j a b`: RHS Pochhammer for the `H_c` identity.
Equals `1` in the boundary regime `j > c-1`.
In the clean regime `j ≤ c-1`, equals `(a+3)_{c-1-j} · (b+2)_{c-1-j}`. -/
def pochHR (c j a b : ℕ) : ℤ :=
  if j ≤ c - 1 then
    ascPoch ((a : ℤ) + 3) (c - 1 - j) * ascPoch ((b : ℤ) + 2) (c - 1 - j)
  else 1

/-! ### Hypothesis: `H_c` factorization (Day-88 Theorem 3 (♦-ext))

We take the H_c factorization as a hypothesis; formalising it from
Clio's Lemma-1 template is a separate (larger) piece of work. -/

/-- `HFactorization H P c` says that `H_c(a,b,j) · pochHL = pochHR · P_j(a,b,c)`
holds for all `j ≤ 2c-1`, `a`, `b`. This is Theorem 3 (♦-ext) of Day-88. -/
def HFactorization (H P : ℕ → ℕ → ℕ → ℤ) (c : ℕ) : Prop :=
  ∀ j a b : ℕ, j ≤ 2 * c - 1 →
    H a b j * pochHL c j a b = pochHR c j a b * P a b c

/-! ### `h_k^{(c)}` and `Q_k` -/

/-- Möbius transform of `H_c` in the third argument. -/
def h_k_c (H : ℕ → ℕ → ℕ → ℤ) (k a b : ℕ) : ℤ :=
  ∑ j ∈ range (k + 1), (-1 : ℤ) ^ (k - j) * (Nat.choose k j : ℤ) * H a b j

/-- `Q_k(a,b,c)` as defined by (Q_k formula). -/
def Q_k (P : ℕ → ℕ → ℕ → ℤ) (c k a b : ℕ) : ℤ :=
  ∑ j ∈ range (k + 1),
    (-1 : ℤ) ^ (k - j) * (Nat.choose k j : ℤ)
      * ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - j)
      * ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - j)
      * P a b c

/-! ### Sanity: k=0 unfolds correctly -/

lemma h_k_c_zero (H : ℕ → ℕ → ℕ → ℤ) (a b : ℕ) :
    h_k_c H 0 a b = H a b 0 := by
  simp [h_k_c]

lemma Q_k_zero (P : ℕ → ℕ → ℕ → ℤ) (c a b : ℕ) :
    Q_k P c 0 a b = P a b c := by
  simp [Q_k]

/-! ### Clean-regime `pochL`, `pochR` when `k ≤ c-1` -/

lemma pochL_clean {c k : ℕ} (hk : k ≤ c - 1) (a b : ℕ) :
    pochL c k a b = 1 := by
  simp [pochL, hk]

lemma pochR_clean {c k : ℕ} (hk : k ≤ c - 1) (a b : ℕ) :
    pochR c k a b = ascPoch ((a : ℤ) + 3) (c - 1 - k)
                    * ascPoch ((b : ℤ) + 2) (c - 1 - k) := by
  simp [pochR, hk]

lemma pochHL_clean {c j : ℕ} (hj : j ≤ c - 1) (a b : ℕ) :
    pochHL c j a b = 1 := by
  simp [pochHL, hj]

lemma pochHR_clean {c j : ℕ} (hj : j ≤ c - 1) (a b : ℕ) :
    pochHR c j a b = ascPoch ((a : ℤ) + 3) (c - 1 - j)
                     * ascPoch ((b : ℤ) + 2) (c - 1 - j) := by
  simp [pochHR, hj]

/-! ### Boundary-regime unfolding lemmas -/

lemma pochL_boundary {c k : ℕ} (hk : ¬ k ≤ c - 1) (a b : ℕ) :
    pochL c k a b = ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - c + 1)
                    * ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - c + 1) := by
  simp [pochL, hk]

lemma pochR_boundary {c k : ℕ} (hk : ¬ k ≤ c - 1) (a b : ℕ) :
    pochR c k a b = 1 := by
  simp [pochR, hk]

lemma pochHL_boundary {c j : ℕ} (hj : ¬ j ≤ c - 1) (a b : ℕ) :
    pochHL c j a b = ascPoch ((a : ℤ) + (c : ℤ) - (j : ℤ) + 2) (j - c + 1)
                     * ascPoch ((b : ℤ) + (c : ℤ) - (j : ℤ) + 1) (j - c + 1) := by
  simp [pochHL, hj]

lemma pochHR_boundary {c j : ℕ} (hj : ¬ j ≤ c - 1) (a b : ℕ) :
    pochHR c j a b = 1 := by
  simp [pochHR, hj]

/-! ### `k = 0` warm-up (clean regime)

The `k = 0` case is a direct consequence of the `H_c` hypothesis at `j = 0`.
-/

theorem hk_three_var_factorization_k_zero
    {H P : ℕ → ℕ → ℕ → ℤ} {c : ℕ} (_hc : 3 ≤ c)
    (hyp : HFactorization H P c) (a b : ℕ) :
    h_k_c H 0 a b * pochL c 0 a b = pochR c 0 a b * Q_k P c 0 a b := by
  have h0c : (0 : ℕ) ≤ c - 1 := by omega
  rw [h_k_c_zero, Q_k_zero, pochL_clean h0c, pochR_clean h0c]
  rw [Nat.sub_zero]
  have h0c2 : (0 : ℕ) ≤ 2 * c - 1 := by omega
  have hH := hyp 0 a b h0c2
  rw [pochHL_clean h0c] at hH
  rw [pochHR_clean h0c] at hH
  rw [Nat.sub_zero] at hH
  linarith

/-! ### Clean-regime general `k` -/

/-- Nat-to-Int cast for `c - 1 - k` when `1 ≤ c` and `k ≤ c - 1`. -/
lemma cast_c_sub_one_sub_k {c k : ℕ} (hc : 1 ≤ c) (hk : k ≤ c - 1) :
    ((c - 1 - k : ℕ) : ℤ) = (c : ℤ) - 1 - (k : ℤ) := by
  rw [Nat.cast_sub hk, Nat.cast_sub hc]
  push_cast
  ring

/-- Nat-to-Int arithmetic bridge: when `1 ≤ c` and `k ≤ c - 1`,
`(a : ℤ) + 3 + ((c - 1 - k : ℕ) : ℤ) = (a : ℤ) + c - k + 2`. -/
lemma cast_shift_a {c k : ℕ} (hc : 1 ≤ c) (hk : k ≤ c - 1) (a : ℕ) :
    (a : ℤ) + 3 + ((c - 1 - k : ℕ) : ℤ) = (a : ℤ) + (c : ℤ) - (k : ℤ) + 2 := by
  rw [cast_c_sub_one_sub_k hc hk]; ring

lemma cast_shift_b {c k : ℕ} (hc : 1 ≤ c) (hk : k ≤ c - 1) (b : ℕ) :
    (b : ℤ) + 2 + ((c - 1 - k : ℕ) : ℤ) = (b : ℤ) + (c : ℤ) - (k : ℤ) + 1 := by
  rw [cast_c_sub_one_sub_k hc hk]; ring

/-- Nat-to-Int cast for `k - c + 1` when `c ≤ k`. -/
lemma cast_k_sub_c_plus_one {c k : ℕ} (hk : c ≤ k) :
    ((k - c + 1 : ℕ) : ℤ) = (k : ℤ) - (c : ℤ) + 1 := by
  rw [Nat.cast_add, Nat.cast_sub hk]
  push_cast; ring

/-- Bridge: shifting `(a+c-k+2)` by the boundary length `(k-c+1)` gives `(a+3)`. -/
lemma boundary_bridge_a {c k : ℕ} (hk : c ≤ k) (a : ℕ) :
    (a : ℤ) + (c : ℤ) - (k : ℤ) + 2 + ((k - c + 1 : ℕ) : ℤ) = (a : ℤ) + 3 := by
  rw [cast_k_sub_c_plus_one hk]; ring

/-- Bridge: shifting `(b+c-k+1)` by the boundary length `(k-c+1)` gives `(b+2)`. -/
lemma boundary_bridge_b {c k : ℕ} (hk : c ≤ k) (b : ℕ) :
    (b : ℤ) + (c : ℤ) - (k : ℤ) + 1 + ((k - c + 1 : ℕ) : ℤ) = (b : ℤ) + 2 := by
  rw [cast_k_sub_c_plus_one hk]; ring

/-- Bridge: shifting `(a+c-k+2)` by `(k-j)` gives `(a+c-j+2)`. -/
lemma shift_j_bridge_a {c j k : ℕ} (hj : j ≤ k) (a : ℕ) :
    (a : ℤ) + (c : ℤ) - (k : ℤ) + 2 + ((k - j : ℕ) : ℤ) = (a : ℤ) + (c : ℤ) - (j : ℤ) + 2 := by
  rw [Nat.cast_sub hj]; ring

/-- Bridge: shifting `(b+c-k+1)` by `(k-j)` gives `(b+c-j+1)`. -/
lemma shift_j_bridge_b {c j k : ℕ} (hj : j ≤ k) (b : ℕ) :
    (b : ℤ) + (c : ℤ) - (k : ℤ) + 1 + ((k - j : ℕ) : ℤ) = (b : ℤ) + (c : ℤ) - (j : ℤ) + 1 := by
  rw [Nat.cast_sub hj]; ring

/-- Clean-regime factorization: when `k ≤ c - 1`, the Möbius transform
`h_k^{(c)}(a,b)` equals `(a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k`. This is the
special case where every `j` in the Möbius sum lies in the clean regime of
the `H_c` factorization. -/
theorem hk_three_var_factorization_clean
    {H P : ℕ → ℕ → ℕ → ℤ} {c k : ℕ} (hc : 3 ≤ c) (hk : k ≤ c - 1)
    (hyp : HFactorization H P c) (a b : ℕ) :
    h_k_c H k a b * pochL c k a b = pochR c k a b * Q_k P c k a b := by
  rw [pochL_clean hk, pochR_clean hk, mul_one]
  unfold h_k_c Q_k
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.mem_range] at hj
  have hjk : j ≤ k := Nat.lt_succ_iff.mp hj
  have hjc : j ≤ c - 1 := le_trans hjk hk
  have hjc2 : j ≤ 2 * c - 1 := by omega
  -- Apply the H_c hypothesis
  have hH := hyp j a b hjc2
  rw [pochHL_clean hjc, mul_one, pochHR_clean hjc] at hH
  -- Split c-1-j = (c-1-k) + (k-j) and apply Pochhammer telescoping
  have hsplit : c - 1 - j = (c - 1 - k) + (k - j) := by omega
  rw [hsplit, ascPoch_split, ascPoch_split] at hH
  have hc1 : 1 ≤ c := by omega
  rw [cast_shift_a hc1 hk, cast_shift_b hc1 hk] at hH
  -- Now hH: H a b j = (ascPoch(a+3)(c-1-k) * ascPoch(a+c-k+2)(k-j)) *
  --                   (ascPoch(b+2)(c-1-k) * ascPoch(b+c-k+1)(k-j)) * P a b c
  rw [hH]
  ring

/-! ### Boundary regime `k > c-1`

Day-88 §11 rescue: the "boundary" is notational, not algebraic. The
same term-wise Pochhammer telescoping used in the clean regime applies
here; the Möbius sum contains both `j ≤ c-1` (clean H) and `j > c-1`
(boundary H) terms, so the term-wise identity requires an inner case
split on `j`. -/

/-- Boundary-regime factorization: when `c ≤ k ≤ 2c - 1`, the identity
`h_k * pochL = pochR * Q_k` holds, with `pochL` carrying the Pochhammer
weight and `pochR = 1`. The proof splits each summand by `j ≤ c-1`
(clean H) vs `j > c-1` (boundary H), and applies `ascPoch_split` at the
appropriate telescoping index in each case. -/
theorem hk_three_var_factorization_boundary
    {H P : ℕ → ℕ → ℕ → ℤ} {c k : ℕ} (hc : 3 ≤ c)
    (hk_lb : c ≤ k) (hk_ub : k ≤ 2 * c - 1)
    (hyp : HFactorization H P c) (a b : ℕ) :
    h_k_c H k a b * pochL c k a b = pochR c k a b * Q_k P c k a b := by
  have hkc : ¬ k ≤ c - 1 := by omega
  rw [pochR_boundary hkc, one_mul, pochL_boundary hkc]
  unfold h_k_c Q_k
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.mem_range] at hj
  have hjk : j ≤ k := Nat.lt_succ_iff.mp hj
  have hjc2 : j ≤ 2 * c - 1 := by omega
  have hH := hyp j a b hjc2
  by_cases hjc : j ≤ c - 1
  · -- Case BC: j clean, k boundary.
    -- H hypothesis reduces to: H a b j = ascPoch(a+3)(c-1-j) * ascPoch(b+2)(c-1-j) * P a b c
    rw [pochHL_clean hjc, mul_one, pochHR_clean hjc] at hH
    -- Prove telescoping identity for a-part
    have hkj : k - j = (k - c + 1) + (c - 1 - j) := by omega
    have ha_split :
        ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - j)
          = ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - c + 1)
            * ascPoch ((a : ℤ) + 3) (c - 1 - j) := by
      rw [hkj, ascPoch_split, boundary_bridge_a hk_lb]
    have hb_split :
        ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - j)
          = ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - c + 1)
            * ascPoch ((b : ℤ) + 2) (c - 1 - j) := by
      rw [hkj, ascPoch_split, boundary_bridge_b hk_lb]
    rw [hH, ha_split, hb_split]
    ring
  · -- Case BB: j boundary, k boundary.
    -- H hypothesis: H a b j * (ascPoch(a+c-j+2)(j-c+1) * ascPoch(b+c-j+1)(j-c+1)) = P a b c
    rw [pochHR_boundary hjc, one_mul, pochHL_boundary hjc] at hH
    have hj_lb : c ≤ j := by omega
    have hkc1 : k - c + 1 = (k - j) + (j - c + 1) := by omega
    -- Split ascPoch(a+c-k+2)_{k-c+1} = ascPoch(a+c-k+2)_{k-j} * ascPoch(a+c-j+2)_{j-c+1}
    have ha_split :
        ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - c + 1)
          = ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - j)
            * ascPoch ((a : ℤ) + (c : ℤ) - (j : ℤ) + 2) (j - c + 1) := by
      rw [hkc1, ascPoch_split, shift_j_bridge_a hjk]
    have hb_split :
        ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - c + 1)
          = ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - j)
            * ascPoch ((b : ℤ) + (c : ℤ) - (j : ℤ) + 1) (j - c + 1) := by
      rw [hkc1, ascPoch_split, shift_j_bridge_b hjk]
    rw [ha_split, hb_split]
    linear_combination
      ((-1 : ℤ)^(k - j) * (Nat.choose k j : ℤ)
        * ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - j)
        * ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - j)) * hH

/-! ### Unified statement (main theorem) -/

/-- **Main theorem (Day-88 Theorem 4, ★-ext)**: for every `0 ≤ k ≤ 2c-1`
and `c ≥ 3`, given the `H_c` factorization hypothesis, the Möbius transform
`h_k^{(c)}(a,b)` satisfies

    h_k^{(c)}(a,b) · pochL c k a b = pochR c k a b · Q_k(a,b,c).

Clean regime `k ≤ c-1`: reads `h_k = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k`.
Boundary regime `k > c-1` (with `m := k - c + 1`):
`h_k · (a+c-k+2)_m · (b+c-k+1)_m = Q_k`.

Both sides are polynomials in `(a,b,c)`; `Q_k` is defined uniformly via
`P_j` by (Q_k formula).

The proof dispatches on `k ≤ c-1` to `hk_three_var_factorization_clean`
or `hk_three_var_factorization_boundary`. Both branches are proved. -/
theorem hk_three_var_factorization
    {H P : ℕ → ℕ → ℕ → ℤ} {c k : ℕ} (hc : 3 ≤ c) (hk : k ≤ 2 * c - 1)
    (hyp : HFactorization H P c) (a b : ℕ) :
    h_k_c H k a b * pochL c k a b = pochR c k a b * Q_k P c k a b := by
  by_cases hkc : k ≤ c - 1
  · exact hk_three_var_factorization_clean hc hkc hyp a b
  · have hklb : c ≤ k := by omega
    exact hk_three_var_factorization_boundary hc hklb hk hyp a b

/-! ### Direct (unfolded) corollaries

The `hk_three_var_factorization*` theorems above phrase both regimes via a
uniform `pochL, pochR` pair, so the statement matches (★-ext). For a
consumer that only cares about one regime, the direct forms are cleaner:
the `pochL = 1` clean form and the `pochR = 1` boundary form. -/

/-- Clean-regime **direct** form of (★): when `k ≤ c-1`,
`h_k^{(c)}(a,b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k`.
This is Day-88 §3 Theorem 2 verbatim. -/
theorem hk_three_var_factorization_clean_direct
    {H P : ℕ → ℕ → ℕ → ℤ} {c k : ℕ} (hc : 3 ≤ c) (hk : k ≤ c - 1)
    (hyp : HFactorization H P c) (a b : ℕ) :
    h_k_c H k a b
      = ascPoch ((a : ℤ) + 3) (c - 1 - k)
        * ascPoch ((b : ℤ) + 2) (c - 1 - k)
        * Q_k P c k a b := by
  have h := hk_three_var_factorization_clean hc hk hyp a b
  rw [pochL_clean hk, pochR_clean hk] at h
  linarith

/-- Boundary-regime **direct** form of (★): when `c ≤ k ≤ 2c-1`,
`h_k^{(c)}(a,b) · (a+c-k+2)_{k-c+1} · (b+c-k+1)_{k-c+1} = Q_k`.
This is Day-88 §11 boundary rescue in polynomial (positive-power) form. -/
theorem hk_three_var_factorization_boundary_direct
    {H P : ℕ → ℕ → ℕ → ℤ} {c k : ℕ} (hc : 3 ≤ c)
    (hk_lb : c ≤ k) (hk_ub : k ≤ 2 * c - 1)
    (hyp : HFactorization H P c) (a b : ℕ) :
    h_k_c H k a b
        * ascPoch ((a : ℤ) + (c : ℤ) - (k : ℤ) + 2) (k - c + 1)
        * ascPoch ((b : ℤ) + (c : ℤ) - (k : ℤ) + 1) (k - c + 1)
      = Q_k P c k a b := by
  have h := hk_three_var_factorization_boundary hc hk_lb hk_ub hyp a b
  have hkc : ¬ k ≤ c - 1 := by omega
  rw [pochL_boundary hkc, pochR_boundary hkc] at h
  linarith

end HkThreeVar
