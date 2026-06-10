/-
  BdiPolytope.lean

  Minimal Lean 4 (stdlib-only) formalization of the first lemma of
  Theorem F (BDI carry-polytope facet structure).

  Design choices (per SCOPING-theorem-F.md):
  * Use `Int` for M, B, T, S so prefix sums `P_a` (which can be negative
    in intermediate computations) live naturally in `ℤ`.
  * Use `Nat` (plain natural number) indexing for the position `a`,
    rather than `Fin (n-1)`, to avoid Mathlib and Fin gymnastics.
  * Non-negativity is bundled as hypotheses on the `ChainConfig` structure.
  * `P` is defined by the recursion `P 0 = 0`, `P (a+1) = P a + 2*(B a - T a)`.
  * The lemma `L1_implies_M1_zero` is proved by `omega` after unfolding `P 0 = 0`.
-/

namespace BdiPolytope

/-- A chain configuration on `n` carry positions.

The math has fields `M_a, B_a, T_a` indexed by `a ∈ {1, ..., n-1}` and a
scalar `S`. Here `n` is implicit: we model the fields as total functions
`Nat → Int` and the user is responsible for using indices in range.
Non-negativity is enforced for every index. -/
structure ChainConfig where
  /-- Mass coordinate `M_a`. -/
  M : Nat → Int
  /-- Birth coordinate `B_a`. -/
  B : Nat → Int
  /-- Termination coordinate `T_a`. -/
  T : Nat → Int
  /-- Final scalar `S`. -/
  S : Int
  /-- Non-negativity of `M`. -/
  M_nonneg : ∀ a, 0 ≤ M a
  /-- Non-negativity of `B`. -/
  B_nonneg : ∀ a, 0 ≤ B a
  /-- Non-negativity of `T`. -/
  T_nonneg : ∀ a, 0 ≤ T a
  /-- Non-negativity of `S`. -/
  S_nonneg : 0 ≤ S

/-- Prefix sum `P_a = ∑_{b=0}^{a-1} 2 * (B b - T b)`, defined by recursion.

`P c 0 = 0`, and `P c (a+1) = P c a + 2 * (c.B a - c.T a)`. -/
def P (c : ChainConfig) : Nat → Int
  | 0       => 0
  | (a + 1) => P c a + 2 * (c.B a - c.T a)

/-- Definitional unfold: `P c 0 = 0`. -/
@[simp] theorem P_zero (c : ChainConfig) : P c 0 = 0 := rfl

/-- Definitional unfold: `P c (a+1) = P c a + 2 * (B a - T a)`. -/
@[simp] theorem P_succ (c : ChainConfig) (a : Nat) :
    P c (a + 1) = P c a + 2 * (c.B a - c.T a) := rfl

/-- **Lemma 1 of Theorem F.**

The fence inequality `L_1` says `M_1 ≤ P_0`. Since `P_0 = 0` and
`M_1 ≥ 0` (non-negativity), we conclude `M_1 = 0`.

Concretely: `c.M 0` is the `M_1` of the math (we 0-index the array). -/
theorem L1_implies_M1_zero (c : ChainConfig)
    (hL1 : c.M 0 ≤ P c 0) : c.M 0 = 0 := by
  have hP : P c 0 = 0 := P_zero c
  have hM : 0 ≤ c.M 0 := c.M_nonneg 0
  omega

/-- **Lemma 4 of Theorem F: `U_1` is redundant when `n ≥ 3`.**

The upper-fence inequality `U_1` says `M_1 ≤ P_1`. We show it is implied
by `L_1` (which forces `M_1 = 0` via lemma 1) together with `L_2 : M_2 ≤ P_1`
and the non-negativity `M_2 ≥ 0`.

Chain:
* `L_1` plus nonneg ⇒ `M_1 = 0`               (lemma 1)
* `L_2` says `M_2 ≤ P_1`
* `M_2 ≥ 0` (structural)
* Hence `0 ≤ M_2 ≤ P_1`, so `M_1 = 0 ≤ P_1`.

**Indexing note.** In our `ChainConfig`, `M, B, T` are total functions on `Nat`,
so there is no explicit `n` constraint; the meaning "`n ≥ 3`" is captured by
the fact that `L_2 : M_2 ≤ P_1` (a hypothesis here) only appears among the
fences when `n ≥ 3`. The companion result `U1_redundant_n_eq_2` will replace
`hL2` with the end-fence `E : S ≤ P_{n-1}`. -/
theorem U1_redundant_n_ge_3 (c : ChainConfig)
    (hL1 : c.M 0 ≤ P c 0)
    (hL2 : c.M 1 ≤ P c 1) :
    c.M 0 ≤ P c 1 := by
  have h0 : c.M 0 = 0 := L1_implies_M1_zero c hL1
  have h2 : 0 ≤ c.M 1 := c.M_nonneg 1
  omega

/-- **Companion lemma: `U_1` is redundant when `n = 2`.**

The same statement as `U1_redundant_n_ge_3`, but using the end-fence `E`
instead of `L_2` to witness `P_1 ≥ 0`. In the `n = 2` case the polytope has
no `L_2` (math has fences only for `a ∈ {1, ..., n-1}`, so for `n = 2`
the only `L` fence is `L_1`). Instead, the end-fence `E : S ≤ P_{n-1}`
specialises to `S ≤ P_1`, and `S ≥ 0` gives `P_1 ≥ 0`. -/
theorem U1_redundant_n_eq_2 (c : ChainConfig)
    (hL1 : c.M 0 ≤ P c 0)
    (hE  : c.S ≤ P c 1) :
    c.M 0 ≤ P c 1 := by
  have h0 : c.M 0 = 0 := L1_implies_M1_zero c hL1
  have hS : 0 ≤ c.S := c.S_nonneg
  omega

/-! ## Theorem G — Weight-space simplicial cone (definitions + first lemmas)

For `n ≥ 2`, the weight-space image cone `K_n ⊆ ℝ^n` is the rational polyhedral
cone with H-representation

* `λ_1 + ⋯ + λ_k ≥ 0`     for `k = 1, …, n - 2`,
* `λ_1 + ⋯ + λ_n ≥ 0`,
* `λ_n ≤ λ_1 + ⋯ + λ_{n-1}`.

These `n` inequalities are pairwise non-redundant facets; equivalently `K_n` is a
**simplicial cone**.  The `n` extreme rays are explicit: `n - 2` pair rays
`e_k - e_{k+1}` (math 1-indexed `k = 1, …, n - 2`), a sum ray `e_{n-1} + e_n`,
and an `E` ray `e_{n-1} - e_n`.

We follow the F-easy convention of working with total functions `Nat → Int`
and `Nat` indexing, staying pure-stdlib.  See `TheoremG-scoping.md`. -/

/-- Partial sum: `partialSum v k = v 0 + v 1 + ⋯ + v (k - 1)`, with
`partialSum v 0 = 0`. -/
def partialSum (v : Nat → Int) : Nat → Int
  | 0      => 0
  | k + 1  => partialSum v k + v k

@[simp] theorem partialSum_zero (v : Nat → Int) : partialSum v 0 = 0 := rfl

@[simp] theorem partialSum_succ (v : Nat → Int) (k : Nat) :
    partialSum v (k + 1) = partialSum v k + v k := rfl

/-- "Pair ray" `r_k = e_k - e_{k+1}` (0-indexed: math `r_{k+1} = E_{k+1} - E_{k+2}`).
For `0 ≤ k ≤ n - 3` these are `n - 2` of the `n` extreme rays of `K_n`. -/
def pairRay (k : Nat) (j : Nat) : Int :=
  if j = k then 1 else if j = k + 1 then -1 else 0

/-- "Sum ray" `r_{sum} = e_{n-2} + e_{n-1}` (0-indexed: math `e_{n-1} + e_n`). -/
def sumRay (n : Nat) (j : Nat) : Int :=
  if j = n - 2 then 1 else if j = n - 1 then 1 else 0

/-- "`E` ray" `r_E = e_{n-2} - e_{n-1}` (0-indexed: math `e_{n-1} - e_n`). -/
def eRay (n : Nat) (j : Nat) : Int :=
  if j = n - 2 then 1 else if j = n - 1 then -1 else 0

/-- Cone-membership predicate for `K_n`.  See file-level doc above. -/
def InKone (n : Nat) (v : Nat → Int) : Prop :=
  (∀ k : Nat, 1 ≤ k → k ≤ n - 2 → 0 ≤ partialSum v k)
  ∧ (0 ≤ partialSum v n)
  ∧ (v (n - 1) ≤ partialSum v (n - 1))

/-! ### Sanity-evaluation lemmas for the rays -/

theorem pairRay_at_k (k : Nat) : pairRay k k = 1 := by
  simp [pairRay]

theorem pairRay_at_succ (k : Nat) : pairRay k (k + 1) = -1 := by
  simp [pairRay]

theorem pairRay_off (k j : Nat) (h1 : j ≠ k) (h2 : j ≠ k + 1) :
    pairRay k j = 0 := by
  simp [pairRay, h1, h2]

theorem sumRay_at_n_minus_two (n : Nat) : sumRay n (n - 2) = 1 := by
  simp [sumRay]

theorem sumRay_at_n_minus_one (n : Nat) (hn : 2 ≤ n) :
    sumRay n (n - 1) = 1 := by
  unfold sumRay
  have h : (n - 1 : Nat) ≠ n - 2 := by omega
  simp [h]

theorem sumRay_off (n j : Nat) (h1 : j ≠ n - 2) (h2 : j ≠ n - 1) :
    sumRay n j = 0 := by
  simp [sumRay, h1, h2]

theorem eRay_at_n_minus_two (n : Nat) : eRay n (n - 2) = 1 := by
  simp [eRay]

theorem eRay_at_n_minus_one (n : Nat) (hn : 2 ≤ n) :
    eRay n (n - 1) = -1 := by
  unfold eRay
  have h : (n - 1 : Nat) ≠ n - 2 := by omega
  simp [h]

theorem eRay_off (n j : Nat) (h1 : j ≠ n - 2) (h2 : j ≠ n - 1) :
    eRay n j = 0 := by
  simp [eRay, h1, h2]

/-! ### Partial sums of the rays

The bulk of the work: compute `partialSum (· Ray) k` at every relevant `k`. -/

/-- For any `k ≤ n - 2`, the partial sum of `sumRay n` up to `k` is zero
(all the nonzero entries lie at positions `n - 2, n - 1`, both `≥ k`). -/
theorem partialSum_sumRay_low (n k : Nat) (h : k ≤ n - 2) :
    partialSum (sumRay n) k = 0 := by
  induction k with
  | zero => rfl
  | succ m ih =>
    have h_m  : m ≤ n - 2 := by omega
    have h_ne1 : m ≠ n - 2 := by omega
    have h_ne2 : m ≠ n - 1 := by omega
    have ih_val : partialSum (sumRay n) m = 0 := ih h_m
    show partialSum (sumRay n) m + sumRay n m = 0
    rw [ih_val, sumRay_off n m h_ne1 h_ne2]
    rfl

/-- Partial sum of `sumRay n` at `n - 1` is `1` (one nonzero entry at position
`n - 2`, value `1`). -/
theorem partialSum_sumRay_n_minus_one (n : Nat) (hn : 2 ≤ n) :
    partialSum (sumRay n) (n - 1) = 1 := by
  -- (n - 1) = (n - 2) + 1
  have h_eq : n - 1 = (n - 2) + 1 := by omega
  rw [h_eq]
  show partialSum (sumRay n) (n - 2) + sumRay n (n - 2) = 1
  rw [partialSum_sumRay_low n (n - 2) (Nat.le_refl _),
      sumRay_at_n_minus_two n]
  rfl

/-- Partial sum of `sumRay n` at `n` is `2` (two nonzero entries at `n - 2, n - 1`). -/
theorem partialSum_sumRay_n (n : Nat) (hn : 2 ≤ n) :
    partialSum (sumRay n) n = 2 := by
  have h_eq : n = (n - 1) + 1 := by omega
  rw [h_eq]
  show partialSum (sumRay n) (n - 1) + sumRay n (n - 1) = 2
  rw [partialSum_sumRay_n_minus_one n hn, sumRay_at_n_minus_one n hn]
  rfl

/-- For any `k ≤ n - 2`, the partial sum of `eRay n` up to `k` is zero. -/
theorem partialSum_eRay_low (n k : Nat) (h : k ≤ n - 2) :
    partialSum (eRay n) k = 0 := by
  induction k with
  | zero => rfl
  | succ m ih =>
    have h_m  : m ≤ n - 2 := by omega
    have h_ne1 : m ≠ n - 2 := by omega
    have h_ne2 : m ≠ n - 1 := by omega
    have ih_val : partialSum (eRay n) m = 0 := ih h_m
    show partialSum (eRay n) m + eRay n m = 0
    rw [ih_val, eRay_off n m h_ne1 h_ne2]
    rfl

theorem partialSum_eRay_n_minus_one (n : Nat) (hn : 2 ≤ n) :
    partialSum (eRay n) (n - 1) = 1 := by
  have h_eq : n - 1 = (n - 2) + 1 := by omega
  rw [h_eq]
  show partialSum (eRay n) (n - 2) + eRay n (n - 2) = 1
  rw [partialSum_eRay_low n (n - 2) (Nat.le_refl _),
      eRay_at_n_minus_two n]
  rfl

theorem partialSum_eRay_n (n : Nat) (hn : 2 ≤ n) :
    partialSum (eRay n) n = 0 := by
  have h_eq : n = (n - 1) + 1 := by omega
  rw [h_eq]
  show partialSum (eRay n) (n - 1) + eRay n (n - 1) = 0
  rw [partialSum_eRay_n_minus_one n hn, eRay_at_n_minus_one n hn]
  rfl

/-! ### Each ray lies in `K_n` -/

/-- **Lemma G-5.** The sum ray `e_{n-1} + e_n` lies in `K_n`. -/
theorem sumRay_in_Kone (n : Nat) (hn : 2 ≤ n) :
    InKone n (sumRay n) := by
  refine ⟨?_, ?_, ?_⟩
  · -- ∀ k, 1 ≤ k → k ≤ n - 2 → 0 ≤ partialSum (sumRay n) k
    intro k _ hk_le
    rw [partialSum_sumRay_low n k hk_le]
    decide
  · -- 0 ≤ partialSum (sumRay n) n
    rw [partialSum_sumRay_n n hn]
    decide
  · -- sumRay n (n - 1) ≤ partialSum (sumRay n) (n - 1)
    rw [sumRay_at_n_minus_one n hn, partialSum_sumRay_n_minus_one n hn]
    decide

/-- **Lemma G-6.** The `E` ray `e_{n-1} - e_n` lies in `K_n`. -/
theorem eRay_in_Kone (n : Nat) (hn : 2 ≤ n) :
    InKone n (eRay n) := by
  refine ⟨?_, ?_, ?_⟩
  · intro k _ hk_le
    rw [partialSum_eRay_low n k hk_le]
    decide
  · rw [partialSum_eRay_n n hn]
    decide
  · rw [eRay_at_n_minus_one n hn, partialSum_eRay_n_minus_one n hn]
    decide

/-! ### Pair-ray partial sums and membership

The pair ray `pairRay k = e_k - e_{k+1}` has a piecewise partial-sum profile:
zero up to index `k`, jumps to `1` at index `k + 1`, then drops back to `0` at
index `k + 2` and stays there.  These three lemmas formalise the three
regimes. -/

/-- Partial sum of `pairRay k` at any `j ≤ k` is zero. -/
theorem partialSum_pairRay_le_k (k j : Nat) (h : j ≤ k) :
    partialSum (pairRay k) j = 0 := by
  induction j with
  | zero => rfl
  | succ m ih =>
    have h_m : m ≤ k := by omega
    have h_ne1 : m ≠ k := by omega
    have h_ne2 : m ≠ k + 1 := by omega
    have ih_val : partialSum (pairRay k) m = 0 := ih h_m
    show partialSum (pairRay k) m + pairRay k m = 0
    rw [ih_val, pairRay_off k m h_ne1 h_ne2]
    rfl

/-- Partial sum of `pairRay k` at `k + 1` is `1`. -/
theorem partialSum_pairRay_at_succ (k : Nat) :
    partialSum (pairRay k) (k + 1) = 1 := by
  show partialSum (pairRay k) k + pairRay k k = 1
  rw [partialSum_pairRay_le_k k k (Nat.le_refl _), pairRay_at_k k]
  rfl

/-- Partial sum of `pairRay k` at any `j ≥ k + 2` is zero. -/
theorem partialSum_pairRay_ge_k_plus_two (k j : Nat) (h : k + 2 ≤ j) :
    partialSum (pairRay k) j = 0 := by
  induction j with
  | zero => omega
  | succ m ih =>
    by_cases hm : k + 2 ≤ m
    · -- inductive step: partialSum p (m+1) = partialSum p m + pairRay k m = 0 + 0 = 0
      have h_ne1 : m ≠ k := by omega
      have h_ne2 : m ≠ k + 1 := by omega
      have ih_val : partialSum (pairRay k) m = 0 := ih hm
      show partialSum (pairRay k) m + pairRay k m = 0
      rw [ih_val, pairRay_off k m h_ne1 h_ne2]
      rfl
    · -- base case: m = k + 1, so partialSum p (k+2) = 1 + (-1) = 0
      have h_eq : m = k + 1 := by omega
      rw [h_eq]
      show partialSum (pairRay k) (k + 1) + pairRay k (k + 1) = 0
      rw [partialSum_pairRay_at_succ k, pairRay_at_succ k]
      rfl

/-- **Lemma G-4.** Each pair ray `e_k - e_{k+1}` lies in `K_n` (for `0 ≤ k`
and `k + 3 ≤ n`). -/
theorem pairRay_in_Kone (n k : Nat) (h_n : 3 ≤ n) (h_k : k + 3 ≤ n) :
    InKone n (pairRay k) := by
  refine ⟨?_, ?_, ?_⟩
  · -- ∀ j, 1 ≤ j → j ≤ n - 2 → 0 ≤ partialSum (pairRay k) j
    intro j _ hj_le
    by_cases hjk : j ≤ k
    · rw [partialSum_pairRay_le_k k j hjk]
      decide
    · by_cases hjk' : j = k + 1
      · rw [hjk', partialSum_pairRay_at_succ k]
        decide
      · have h_ge : k + 2 ≤ j := by omega
        rw [partialSum_pairRay_ge_k_plus_two k j h_ge]
        decide
  · -- 0 ≤ partialSum (pairRay k) n
    have h_ge : k + 2 ≤ n := by omega
    rw [partialSum_pairRay_ge_k_plus_two k n h_ge]
    decide
  · -- pairRay k (n - 1) ≤ partialSum (pairRay k) (n - 1)
    have h_ne1 : (n - 1 : Nat) ≠ k := by omega
    have h_ne2 : (n - 1 : Nat) ≠ k + 1 := by omega
    have h_ge : k + 2 ≤ n - 1 := by omega
    rw [pairRay_off k (n - 1) h_ne1 h_ne2,
        partialSum_pairRay_ge_k_plus_two k (n - 1) h_ge]
    decide

/-! ## Theorem G — Lemma 3: Linear independence of the n extreme rays

For `n ≥ 3` the `n` rays `pairRay 0, …, pairRay (n - 3), sumRay n, eRay n` are
linearly independent over `ℤ` (equivalently, over `ℚ`).

Coordinate-descent: at coordinate `j` the linear combination
`∑_{k < n - 2} c_k * (pairRay k) j + c (n - 2) * (sumRay n) j +
 c (n - 1) * (eRay n) j`
forces

* `j = 0`         → `c 0 = 0`,
* `1 ≤ j ≤ n - 3` → `c j = c (j - 1)`, so `c j = 0` by induction,
* `j = n - 2`     → `c (n - 2) + c (n - 1) = c (n - 3) = 0`,
* `j = n - 1`     → `c (n - 2) = c (n - 1)`,

so `c (n - 2) = c (n - 1) = 0` as well. -/

/-- Linear combination of the `n` candidate extreme rays with integer
coefficients `c`, evaluated at coordinate `j`.  The first `n - 2` rays are pair
rays `pairRay 0, …, pairRay (n - 3)`; the last two are the sum ray
`e_{n-2} + e_{n-1}` and the `E` ray `e_{n-2} - e_{n-1}`. -/
def linComb (n : Nat) (c : Nat → Int) (j : Nat) : Int :=
  partialSum (fun k => c k * pairRay k j) (n - 2)
  + c (n - 2) * sumRay n j
  + c (n - 1) * eRay n j

/-! ### Partial-sum closed forms for the pair-ray family

For fixed coordinate `j`, the integrand `k ↦ c k * pairRay k j` is supported on
`{j - 1, j}` (when these indices exist).  The four lemmas below cover the four
regimes of `(j, m)` we need. -/

/-- For `m + 1 ≤ j`, every index `k < m` satisfies `pairRay k j = 0`, so the
weighted partial sum vanishes. -/
theorem partialSum_pair_below (c : Nat → Int) (j m : Nat) (h : m + 1 ≤ j) :
    partialSum (fun k => c k * pairRay k j) m = 0 := by
  induction m with
  | zero => rfl
  | succ p ih =>
    have hp : p + 1 ≤ j := by omega
    have ih_val : partialSum (fun k => c k * pairRay k j) p = 0 := ih hp
    have h_ne1 : j ≠ p := by omega
    have h_ne2 : j ≠ p + 1 := by omega
    show partialSum (fun k => c k * pairRay k j) p + c p * pairRay p j = 0
    rw [ih_val, pairRay_off p j h_ne1 h_ne2]
    omega

/-- At coordinate `0`, for any `m ≥ 1`, the weighted partial sum equals `c 0`
(only `k = 0` contributes, with value `c 0 * 1`). -/
theorem partialSum_pair_at_zero (c : Nat → Int) (m : Nat) (hm : 1 ≤ m) :
    partialSum (fun k => c k * pairRay k 0) m = c 0 := by
  revert hm
  induction m with
  | zero => intro hm; omega
  | succ p ih =>
    intro _
    by_cases hp : 1 ≤ p
    · have ih_val : partialSum (fun k => c k * pairRay k 0) p = c 0 := ih hp
      have h_ne1 : (0 : Nat) ≠ p := by omega
      have h_ne2 : (0 : Nat) ≠ p + 1 := by omega
      show partialSum (fun k => c k * pairRay k 0) p + c p * pairRay p 0 = c 0
      rw [ih_val, pairRay_off p 0 h_ne1 h_ne2]
      omega
    · have h_eq : p = 0 := by omega
      rw [h_eq]
      show partialSum (fun k => c k * pairRay k 0) 0 + c 0 * pairRay 0 0 = c 0
      rw [partialSum_zero, pairRay_at_k 0]
      omega

/-- At coordinate `j` (with `j ≥ 1`), the partial sum up to `m = j` equals
`-c (j - 1)` — only the `k = j - 1` term contributes, with value `c (j-1) * -1`. -/
theorem partialSum_pair_at_j (c : Nat → Int) (j : Nat) (hj : 1 ≤ j) :
    partialSum (fun k => c k * pairRay k j) j = -c (j - 1) := by
  cases j with
  | zero => omega
  | succ j' =>
    -- `j = j' + 1`, so `j - 1` reduces to `j'`, and the partial sum unfolds
    -- to `partialSum f j' + c j' * pairRay j' (j' + 1)`.
    show partialSum (fun k => c k * pairRay k (j' + 1)) j' +
         c j' * pairRay j' (j' + 1) = -c j'
    have h_low : partialSum (fun k => c k * pairRay k (j' + 1)) j' = 0 :=
      partialSum_pair_below c (j' + 1) j' (by omega)
    rw [h_low, pairRay_at_succ j']
    omega

/-- At coordinate `j` (with `j ≥ 1`) and `m ≥ j + 1`, the partial sum equals
`c j - c (j - 1)` — the only contributions are `c (j-1) * -1` at `k = j - 1`
and `c j * 1` at `k = j`. -/
theorem partialSum_pair_above (c : Nat → Int) (j m : Nat)
    (hj : 1 ≤ j) (hm : j + 1 ≤ m) :
    partialSum (fun k => c k * pairRay k j) m = c j - c (j - 1) := by
  revert hm
  induction m with
  | zero => intro hm; omega
  | succ p ih =>
    intro hm
    by_cases hp : j + 1 ≤ p
    · have ih_val : partialSum (fun k => c k * pairRay k j) p = c j - c (j - 1) :=
        ih hp
      have h_ne1 : j ≠ p := by omega
      have h_ne2 : j ≠ p + 1 := by omega
      show partialSum (fun k => c k * pairRay k j) p + c p * pairRay p j =
        c j - c (j - 1)
      rw [ih_val, pairRay_off p j h_ne1 h_ne2]
      omega
    · have h_eq : p = j := by omega
      rw [h_eq]
      show partialSum (fun k => c k * pairRay k j) j + c j * pairRay j j =
        c j - c (j - 1)
      rw [partialSum_pair_at_j c j hj, pairRay_at_k j]
      omega

/-! ### Theorem G — Lemma 3 -/

/-- **Theorem G, Lemma 3.** The `n` candidate extreme rays of `K_n` are linearly
independent over `ℤ`.

If a linear combination of the rays with integer coefficients `c k`
(for `k < n`) vanishes at every coordinate `j < n`, then every coefficient
`c k = 0`. -/
theorem rays_lin_indep (n : Nat) (hn : 3 ≤ n) (c : Nat → Int)
    (h : ∀ j, j < n → linComb n c j = 0) :
    ∀ k, k < n → c k = 0 := by
  -- Step 1: c k = 0 for k ≤ n - 3, by induction on k.
  have hc_low : ∀ k, k ≤ n - 3 → c k = 0 := by
    intro k hk
    induction k with
    | zero =>
      have h0 := h 0 (by omega)
      unfold linComb at h0
      have e1 : partialSum (fun k => c k * pairRay k 0) (n - 2) = c 0 :=
        partialSum_pair_at_zero c (n - 2) (by omega)
      have e2 : sumRay n 0 = 0 := sumRay_off n 0 (by omega) (by omega)
      have e3 : eRay n 0 = 0 := eRay_off n 0 (by omega) (by omega)
      rw [e1, e2, e3] at h0
      omega
    | succ p ih =>
      have ih_val : c p = 0 := ih (by omega)
      have hj := h (p + 1) (by omega)
      unfold linComb at hj
      have e1 : partialSum (fun k => c k * pairRay k (p + 1)) (n - 2) =
          c (p + 1) - c p :=
        partialSum_pair_above c (p + 1) (n - 2) (by omega) (by omega)
      have e2 : sumRay n (p + 1) = 0 :=
        sumRay_off n (p + 1) (by omega) (by omega)
      have e3 : eRay n (p + 1) = 0 :=
        eRay_off n (p + 1) (by omega) (by omega)
      rw [e1, e2, e3] at hj
      omega
  -- Step 2: c (n - 3) = 0.
  have hc_nm3 : c (n - 3) = 0 := hc_low (n - 3) (by omega)
  -- Step 3: c (n - 2) + c (n - 1) = 0 from linComb at j = n - 2.
  have hsum : c (n - 2) + c (n - 1) = 0 := by
    have hj := h (n - 2) (by omega)
    unfold linComb at hj
    have e1 : partialSum (fun k => c k * pairRay k (n - 2)) (n - 2) =
        -c (n - 3) :=
      partialSum_pair_at_j c (n - 2) (by omega)
    have e2 : sumRay n (n - 2) = 1 := sumRay_at_n_minus_two n
    have e3 : eRay n (n - 2) = 1 := eRay_at_n_minus_two n
    rw [e1, e2, e3] at hj
    omega
  -- Step 4: c (n - 2) - c (n - 1) = 0 from linComb at j = n - 1.
  have hdiff : c (n - 2) - c (n - 1) = 0 := by
    have hj := h (n - 1) (by omega)
    unfold linComb at hj
    have e1 : partialSum (fun k => c k * pairRay k (n - 1)) (n - 2) = 0 :=
      partialSum_pair_below c (n - 1) (n - 2) (by omega)
    have e2 : sumRay n (n - 1) = 1 := sumRay_at_n_minus_one n (by omega)
    have e3 : eRay n (n - 1) = -1 := eRay_at_n_minus_one n (by omega)
    rw [e1, e2, e3] at hj
    omega
  -- Conclude.
  intro k hk
  by_cases hk_low : k ≤ n - 3
  · exact hc_low k hk_low
  · by_cases hk_eq : k = n - 2
    · rw [hk_eq]; omega
    · have hk_eq2 : k = n - 1 := by omega
      rw [hk_eq2]; omega

end BdiPolytope
