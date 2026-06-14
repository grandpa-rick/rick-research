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

/-! ## Theorem F-easy — non-redundancy of the surviving fences

For `n ≥ 3` the BDI carry polytope has three families of fence inequalities:

* `L_k` : `M_k ≤ P_{k - 1}` for `k = 1, …, n - 1`,
* `U_k` : `M_k ≤ P_k`       for `k = 1, …, n - 1`,
* `E`   : `S ≤ P_{n - 1}`.

`L_1` is the degenerate fence `M_1 ≤ 0` (forces `M_1 = 0` by non-negativity,
see `L1_implies_M1_zero`). `U_1` is redundant (see `U1_redundant_n_ge_3` /
`U1_redundant_n_eq_2`). For every other fence we exhibit an explicit
`ChainConfig` that satisfies every other fence but violates the named one.
Hence the surviving `2 (n - 2) + 1` inequalities are pairwise non-redundant.

**Indexing.** We continue with `Nat → Int` total-function coordinates, so the
math index `k + 1` corresponds to the Lean index `k`. Concretely the Lean
form of the fences is:

* `L k` : `c.M k ≤ P c k`       (math `L_{k+1}: M_{k+1} ≤ P_k`),
* `U k` : `c.M k ≤ P c (k + 1)` (math `U_{k+1}: M_{k+1} ≤ P_{k+1}`),
* `E i` : `c.S ≤ P c i`         (math `E: S ≤ P_{n-1}` taken with `i = n - 1`). -/

/-! ### E witness: `S = 1`, all chain coordinates zero -/

/-- Witness for non-redundancy of the end-fence `E`: `S = 1`, every chain
coordinate set to `0`.  Then `P j = 0` for all `j`, so every `L`- and
`U`-fence is satisfied trivially, but every candidate end-fence
`S ≤ P i` becomes `1 ≤ 0`. -/
def EWitness : ChainConfig where
  M := fun _ => 0
  B := fun _ => 0
  T := fun _ => 0
  S := 1
  M_nonneg := fun _ => by omega
  B_nonneg := fun _ => by omega
  T_nonneg := fun _ => by omega
  S_nonneg := by omega

@[simp] theorem EWitness_M (j : Nat) : EWitness.M j = 0 := rfl
@[simp] theorem EWitness_B (j : Nat) : EWitness.B j = 0 := rfl
@[simp] theorem EWitness_T (j : Nat) : EWitness.T j = 0 := rfl
@[simp] theorem EWitness_S         : EWitness.S = 1 := rfl

/-- Closed form for the prefix sum of `EWitness`: identically zero. -/
@[simp] theorem P_EWitness (j : Nat) : P EWitness j = 0 := by
  induction j with
  | zero => rfl
  | succ n ih =>
    show P EWitness n + 2 * (EWitness.B n - EWitness.T n) = 0
    rw [ih, EWitness_B, EWitness_T]
    omega

/-- The E witness satisfies every `L`-fence (reduces to `0 ≤ 0`). -/
theorem EWitness_satisfies_L (j : Nat) : EWitness.M j ≤ P EWitness j := by
  rw [EWitness_M, P_EWitness]
  decide

/-- The E witness satisfies every `U`-fence (reduces to `0 ≤ 0`). -/
theorem EWitness_satisfies_U (j : Nat) : EWitness.M j ≤ P EWitness (j + 1) := by
  rw [EWitness_M, P_EWitness]
  decide

/-- The E witness violates every end-fence `S ≤ P i`: it asks `1 ≤ 0`. -/
theorem EWitness_violates_E (i : Nat) : ¬ (EWitness.S ≤ P EWitness i) := by
  rw [EWitness_S, P_EWitness]
  decide

/-! ### L witness: `M k = 1`, `B k = 1`, otherwise zero -/

/-- Witness for non-redundancy of `L_{k+1}`: `M k = 1`, `B k = 1`, all
other coordinates and `S` zero.  The prefix sum then has closed form
`P j = 2` for `k < j` and `P j = 0` for `j ≤ k`. -/
def LWitness (k : Nat) : ChainConfig where
  M := fun j => if j = k then 1 else 0
  B := fun j => if j = k then 1 else 0
  T := fun _ => 0
  S := 0
  M_nonneg := fun j => by
    show (0 : Int) ≤ if j = k then 1 else 0
    split <;> omega
  B_nonneg := fun j => by
    show (0 : Int) ≤ if j = k then 1 else 0
    split <;> omega
  T_nonneg := fun _ => by omega
  S_nonneg := by omega

@[simp] theorem LWitness_M (k j : Nat) :
    (LWitness k).M j = if j = k then 1 else 0 := rfl
@[simp] theorem LWitness_B (k j : Nat) :
    (LWitness k).B j = if j = k then 1 else 0 := rfl
@[simp] theorem LWitness_T (k j : Nat) : (LWitness k).T j = 0 := rfl
@[simp] theorem LWitness_S (k : Nat)   : (LWitness k).S = 0 := rfl

/-- Closed form for the prefix sum of `LWitness k`. -/
@[simp] theorem P_LWitness (k j : Nat) :
    P (LWitness k) j = if k < j then 2 else 0 := by
  induction j with
  | zero => rfl
  | succ n ih =>
    show P (LWitness k) n + 2 * ((LWitness k).B n - (LWitness k).T n) = _
    rw [ih, LWitness_B, LWitness_T]
    omega

/-- `LWitness k` satisfies every `L`-fence except possibly `L_{k+1}`. -/
theorem LWitness_satisfies_L (k j : Nat) (h : j ≠ k) :
    (LWitness k).M j ≤ P (LWitness k) j := by
  rw [LWitness_M, P_LWitness, if_neg h]
  split <;> omega

/-- `LWitness k` satisfies every `U`-fence. -/
theorem LWitness_satisfies_U (k j : Nat) :
    (LWitness k).M j ≤ P (LWitness k) (j + 1) := by
  rw [LWitness_M, P_LWitness]
  split <;> split <;> omega

/-- `LWitness k` satisfies every candidate end-fence `S ≤ P i`. -/
theorem LWitness_satisfies_E (k i : Nat) :
    (LWitness k).S ≤ P (LWitness k) i := by
  rw [LWitness_S, P_LWitness]
  split <;> omega

/-- `LWitness k` violates `L_{k+1}: M_k ≤ P_k` (recall `M k = 1`, `P k = 0`). -/
theorem LWitness_violates_L (k : Nat) :
    ¬ ((LWitness k).M k ≤ P (LWitness k) k) := by
  rw [LWitness_M, P_LWitness, if_pos rfl, if_neg (show ¬ k < k by omega)]
  decide

/-! ### U witness: `M k = 1`, `B (k - 1) = 1`, `T k = 1` (needs `k ≥ 1`) -/

/-- Witness for non-redundancy of `U_{k+1}` (uses `1 ≤ k` downstream).
Set `M k = 1`, `B (k - 1) = 1`, `T k = 1`, all other coordinates and `S`
zero.  We use the Nat-friendly encoding `B j = 1 ↔ j + 1 = k`, which
silently makes `B` identically `0` at the corner case `k = 0`. -/
def UWitness (k : Nat) : ChainConfig where
  M := fun j => if j = k then 1 else 0
  B := fun j => if j + 1 = k then 1 else 0
  T := fun j => if j = k then 1 else 0
  S := 0
  M_nonneg := fun j => by
    show (0 : Int) ≤ if j = k then 1 else 0
    split <;> omega
  B_nonneg := fun j => by
    show (0 : Int) ≤ if j + 1 = k then 1 else 0
    split <;> omega
  T_nonneg := fun j => by
    show (0 : Int) ≤ if j = k then 1 else 0
    split <;> omega
  S_nonneg := by omega

@[simp] theorem UWitness_M (k j : Nat) :
    (UWitness k).M j = if j = k then 1 else 0 := rfl
@[simp] theorem UWitness_B (k j : Nat) :
    (UWitness k).B j = if j + 1 = k then 1 else 0 := rfl
@[simp] theorem UWitness_T (k j : Nat) :
    (UWitness k).T j = if j = k then 1 else 0 := rfl
@[simp] theorem UWitness_S (k : Nat)   : (UWitness k).S = 0 := rfl

/-- Closed form for the prefix sum of `UWitness k` (requires `1 ≤ k`).
`P j = 2` when `j = k`, else `0`. -/
theorem P_UWitness (k j : Nat) (hk : 1 ≤ k) :
    P (UWitness k) j = if j = k then 2 else 0 := by
  induction j with
  | zero =>
    show (0 : Int) = if 0 = k then 2 else 0
    rw [if_neg (show (0 : Nat) ≠ k by omega)]
  | succ n ih =>
    show P (UWitness k) n + 2 * ((UWitness k).B n - (UWitness k).T n) = _
    rw [ih, UWitness_B, UWitness_T]
    omega

/-- `UWitness k` satisfies every `L`-fence. -/
theorem UWitness_satisfies_L (k j : Nat) (hk : 1 ≤ k) :
    (UWitness k).M j ≤ P (UWitness k) j := by
  rw [UWitness_M, P_UWitness k j hk]
  split <;> omega

/-- `UWitness k` satisfies every `U`-fence except possibly `U_{k+1}`. -/
theorem UWitness_satisfies_U (k j : Nat) (hk : 1 ≤ k) (h : j ≠ k) :
    (UWitness k).M j ≤ P (UWitness k) (j + 1) := by
  rw [UWitness_M, P_UWitness k (j + 1) hk, if_neg h]
  split <;> omega

/-- `UWitness k` satisfies every candidate end-fence `S ≤ P i`. -/
theorem UWitness_satisfies_E (k i : Nat) (hk : 1 ≤ k) :
    (UWitness k).S ≤ P (UWitness k) i := by
  rw [UWitness_S, P_UWitness k i hk]
  split <;> omega

/-- `UWitness k` violates `U_{k+1}: M_k ≤ P_{k+1}` (`M k = 1`, `P (k+1) = 0`). -/
theorem UWitness_violates_U (k : Nat) (hk : 1 ≤ k) :
    ¬ ((UWitness k).M k ≤ P (UWitness k) (k + 1)) := by
  rw [UWitness_M, P_UWitness k (k + 1) hk, if_pos rfl,
      if_neg (show k + 1 ≠ k by omega)]
  decide

/-! ### Theorem F-easy — non-redundancy bundle -/

/-- **Theorem F-easy (E non-redundancy).** There exists a `ChainConfig`
that satisfies every `L`-fence and every `U`-fence but violates every
candidate end-fence `S ≤ P i`.  Witness: `EWitness`. -/
theorem E_nonredundant :
    ∃ c : ChainConfig,
      (∀ j, c.M j ≤ P c j) ∧
      (∀ j, c.M j ≤ P c (j + 1)) ∧
      (∀ i, ¬ (c.S ≤ P c i)) :=
  ⟨EWitness, EWitness_satisfies_L, EWitness_satisfies_U, EWitness_violates_E⟩

/-- **Theorem F-easy (L non-redundancy).** For every `k ≥ 1` there exists
a `ChainConfig` that satisfies every other `L`-fence, every `U`-fence and
every candidate end-fence, but violates `L_{k+1}: M_k ≤ P_k`. -/
theorem L_nonredundant (k : Nat) (_hk : 1 ≤ k) :
    ∃ c : ChainConfig,
      (∀ j, j ≠ k → c.M j ≤ P c j) ∧
      (∀ j, c.M j ≤ P c (j + 1)) ∧
      (∀ i, c.S ≤ P c i) ∧
      ¬ (c.M k ≤ P c k) :=
  ⟨LWitness k,
   LWitness_satisfies_L k,
   LWitness_satisfies_U k,
   LWitness_satisfies_E k,
   LWitness_violates_L k⟩

/-- **Theorem F-easy (U non-redundancy).** For every `k ≥ 1` there exists
a `ChainConfig` that satisfies every `L`-fence, every other `U`-fence and
every candidate end-fence, but violates `U_{k+1}: M_k ≤ P_{k+1}`. -/
theorem U_nonredundant (k : Nat) (hk : 1 ≤ k) :
    ∃ c : ChainConfig,
      (∀ j, c.M j ≤ P c j) ∧
      (∀ j, j ≠ k → c.M j ≤ P c (j + 1)) ∧
      (∀ i, c.S ≤ P c i) ∧
      ¬ (c.M k ≤ P c (k + 1)) :=
  ⟨UWitness k,
   fun j => UWitness_satisfies_L k j hk,
   fun j h => UWitness_satisfies_U k j hk h,
   fun i => UWitness_satisfies_E k i hk,
   UWitness_violates_U k hk⟩

/-! ## Theorem F-easy — `Fin (n - 1)` Fence wrapper

Re-packages the F-easy bundle (`E_nonredundant`, `L_nonredundant`,
`U_nonredundant`) as a single uniform indexed family of `BdiPolytopeFace n`
values, one per non-redundant facet of the BDI carry polytope.

Indexing:
* `Fence_L n` : `Fin (n - 1) → BdiPolytopeFace n` — all `n - 1` `L` facets
  (math `L_1, …, L_{n-1}`).  `L_1` is non-redundant as a half-space (it
  collapses to `M_1 = 0` only after combining with non-negativity).
* `Fence_U n` : `Fin (n - 2) → BdiPolytopeFace n` — the `n - 2` surviving `U`
  facets (math `U_2, …, U_{n-1}`).  Math `U_1` is eliminated by Theorem F,
  Lemma 4 (`U1_redundant_n_ge_3`), and is therefore absent from this family.
* `Fence_E n` : `BdiPolytopeFace n` — the singleton end fence.

Total face count: `(n - 1) + (n - 2) + 1 = 2 n - 2`. -/

/-- Kind tag for the three fence families of the BDI carry polytope at
parameter `n`.  Each constructor carries enough indexing data to determine the
underlying half-space via `FenceKind.halfspace`. -/
inductive FenceKind (n : Nat) where
  /-- `L_{k+1}` (math): the half-space `M_{k+1} ≤ P_k`, Lean `c.M k ≤ P c k`. -/
  | L : Fin (n - 1) → FenceKind n
  /-- `U_{k+2}` (math): the half-space `M_{k+2} ≤ P_{k+1}`, Lean
  `c.M (k + 1) ≤ P c (k + 2)`.  The `+1` shift on the `Fin` index reflects
  the omission of the redundant math `U_1`. -/
  | U : Fin (n - 2) → FenceKind n
  /-- End fence `E` (math): the half-space `S ≤ P_{n-1}`. -/
  | E : FenceKind n
  deriving DecidableEq

namespace FenceKind

/-- The half-space cut out by a fence kind. -/
def halfspace {n : Nat} : FenceKind n → ChainConfig → Prop
  | .L k, c => c.M k.val ≤ P c k.val
  | .U k, c => c.M (k.val + 1) ≤ P c (k.val + 2)
  | .E,   c => c.S ≤ P c (n - 1)

end FenceKind

/-- A face of the BDI carry polytope at parameter `n`: a fence kind together
with a witness configuration that violates this fence while satisfying every
other fence.  This is the Mathlib-style uniform packaging of the three F-easy
non-redundancy theorems. -/
structure BdiPolytopeFace (n : Nat) where
  /-- The fence kind. -/
  kind : FenceKind n
  /-- Witness configuration for non-redundancy. -/
  witness : ChainConfig
  /-- The witness violates this face's fence. -/
  violates : ¬ kind.halfspace witness
  /-- The witness satisfies every other fence in the polytope. -/
  satisfies_others : ∀ k : FenceKind n, k ≠ kind → k.halfspace witness

/-- L-fence family: `Fence_L n hn i` packages `L_{i.val + 1}` (math) as a
`BdiPolytopeFace n`.  Witness: `LWitness i.val`. -/
def Fence_L (n : Nat) (_hn : 3 ≤ n) (i : Fin (n - 1)) : BdiPolytopeFace n where
  kind := .L i
  witness := LWitness i.val
  violates := LWitness_violates_L i.val
  satisfies_others := by
    intro k hk
    cases k with
    | L j =>
      have hji : j.val ≠ i.val := fun heq =>
        hk (congrArg FenceKind.L (Fin.ext heq))
      exact LWitness_satisfies_L i.val j.val hji
    | U j =>
      exact LWitness_satisfies_U i.val (j.val + 1)
    | E =>
      exact LWitness_satisfies_E i.val (n - 1)

/-- U-fence family: `Fence_U n hn i` packages `U_{i.val + 2}` (math) as a
`BdiPolytopeFace n`.  Witness: `UWitness (i.val + 1)`.  The `+1` shift
on the `Fin` index is the omission of math `U_1`, which is redundant
by Theorem F, Lemma 4 (`U1_redundant_n_ge_3`). -/
def Fence_U (n : Nat) (_hn : 3 ≤ n) (i : Fin (n - 2)) : BdiPolytopeFace n where
  kind := .U i
  witness := UWitness (i.val + 1)
  violates := UWitness_violates_U (i.val + 1) (by omega)
  satisfies_others := by
    intro k hk
    cases k with
    | L j =>
      exact UWitness_satisfies_L (i.val + 1) j.val (by omega)
    | U j =>
      have hji : j.val ≠ i.val := fun heq =>
        hk (congrArg FenceKind.U (Fin.ext heq))
      have hji' : j.val + 1 ≠ i.val + 1 := fun h => hji (by omega)
      exact UWitness_satisfies_U (i.val + 1) (j.val + 1) (by omega) hji'
    | E =>
      exact UWitness_satisfies_E (i.val + 1) (n - 1) (by omega)

/-- End-fence singleton: `Fence_E n hn` packages the end fence `E` (math
`S ≤ P_{n-1}`) as a `BdiPolytopeFace n`.  Witness: `EWitness`. -/
def Fence_E (n : Nat) (_hn : 3 ≤ n) : BdiPolytopeFace n where
  kind := .E
  witness := EWitness
  violates := EWitness_violates_E (n - 1)
  satisfies_others := by
    intro k hk
    cases k with
    | L j => exact EWitness_satisfies_L j.val
    | U j => exact EWitness_satisfies_U (j.val + 1)
    | E   => exact absurd rfl hk

/-! ### Fence kind extraction (defeq sanity) -/

/-- The kind of `Fence_L n hn i` is `.L i`. -/
@[simp] theorem Fence_L_kind (n : Nat) (hn : 3 ≤ n) (i : Fin (n - 1)) :
    (Fence_L n hn i).kind = .L i := rfl

/-- The kind of `Fence_U n hn i` is `.U i`. -/
@[simp] theorem Fence_U_kind (n : Nat) (hn : 3 ≤ n) (i : Fin (n - 2)) :
    (Fence_U n hn i).kind = .U i := rfl

/-- The kind of `Fence_E n hn` is `.E`. -/
@[simp] theorem Fence_E_kind (n : Nat) (hn : 3 ≤ n) :
    (Fence_E n hn).kind = .E := rfl

/-! ### Fence distinctness

Distinct `Fin (n-1)`/`Fin (n-2)` indices yield distinct face kinds within each
family; across families the kinds differ via `noConfusion` on `FenceKind`. -/

/-- Within the L family: distinct indices produce distinct face kinds. -/
theorem Fence_L_distinct (n : Nat) (hn : 3 ≤ n) {i j : Fin (n - 1)} (hij : i ≠ j) :
    (Fence_L n hn i).kind ≠ (Fence_L n hn j).kind := by
  simp only [Fence_L_kind]
  intro h
  exact hij (FenceKind.L.inj h)

/-- Within the U family: distinct indices produce distinct face kinds. -/
theorem Fence_U_distinct (n : Nat) (hn : 3 ≤ n) {i j : Fin (n - 2)} (hij : i ≠ j) :
    (Fence_U n hn i).kind ≠ (Fence_U n hn j).kind := by
  simp only [Fence_U_kind]
  intro h
  exact hij (FenceKind.U.inj h)

/-- Cross-family L vs U: the face kinds always differ. -/
theorem Fence_L_kind_ne_Fence_U_kind (n : Nat) (hn : 3 ≤ n)
    (i : Fin (n - 1)) (j : Fin (n - 2)) :
    (Fence_L n hn i).kind ≠ (Fence_U n hn j).kind := by
  intro h
  rw [Fence_L_kind, Fence_U_kind] at h
  cases h

/-- Cross-family L vs E: the face kinds always differ. -/
theorem Fence_L_kind_ne_Fence_E_kind (n : Nat) (hn : 3 ≤ n) (i : Fin (n - 1)) :
    (Fence_L n hn i).kind ≠ (Fence_E n hn).kind := by
  intro h
  rw [Fence_L_kind, Fence_E_kind] at h
  cases h

/-- Cross-family U vs E: the face kinds always differ. -/
theorem Fence_U_kind_ne_Fence_E_kind (n : Nat) (hn : 3 ≤ n) (j : Fin (n - 2)) :
    (Fence_U n hn j).kind ≠ (Fence_E n hn).kind := by
  intro h
  rw [Fence_U_kind, Fence_E_kind] at h
  cases h

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

/-! ## Theorem G — Lemma 4: cone-hull surjection (form (b), `N = 2`)

For `n ≥ 3`, every `v ∈ K_n` admits an explicit non-negative integer linear
combination of the `n` rays equal to `2 · v`.  The factor of `2` is the
lattice-index obstruction (§4 of `TheoremG-scoping.md`): the ray lattice has
index `2` in `ℤⁿ`, so an arbitrary integer `v ∈ K_n` need not be a
non-negative integer combination of the rays — but `2 v` always is.

This is statement form (b) of the three options discussed in `TheoremG-scoping.md`
§4 / `LEAN.md`.  Forms (a) (pure rational) and (c) (integer with explicit
2-torsion correction) are deferred to Robin's lattice-index call.

### Coefficient closed form

* `c k = 2 · partialSum v (k + 1)`      for `0 ≤ k ≤ n - 3` (pair-ray coeffs),
* `c (n - 2) = partialSum v n`          (sum-ray coeff),
* `c (n - 1) = partialSum v (n - 1) - v (n - 1)` (E-ray coeff).

All three are non-negative on `K_n` by the three facet inequalities. -/

/-- Coefficient function witnessing Lemma 4 (form (b), `N = 2`). -/
def coneCoeff (n : Nat) (v : Nat → Int) (k : Nat) : Int :=
  if k + 3 ≤ n then 2 * partialSum v (k + 1)
  else if k + 2 = n then partialSum v n
  else partialSum v (n - 1) - v (n - 1)

/-- `coneCoeff` on the pair-ray range `0 ≤ k ≤ n - 3`. -/
theorem coneCoeff_low (n : Nat) (v : Nat → Int) (k : Nat) (hk : k + 3 ≤ n) :
    coneCoeff n v k = 2 * partialSum v (k + 1) := by
  unfold coneCoeff; rw [if_pos hk]

/-- `coneCoeff` at the sum-ray slot `k = n - 2`. -/
theorem coneCoeff_n_minus_two (n : Nat) (hn : 2 ≤ n) (v : Nat → Int) :
    coneCoeff n v (n - 2) = partialSum v n := by
  unfold coneCoeff
  rw [if_neg (show ¬ (n - 2 + 3 ≤ n) by omega),
      if_pos (show (n - 2) + 2 = n by omega)]

/-- `coneCoeff` at the `E`-ray slot `k = n - 1`. -/
theorem coneCoeff_n_minus_one (n : Nat) (hn : 2 ≤ n) (v : Nat → Int) :
    coneCoeff n v (n - 1) = partialSum v (n - 1) - v (n - 1) := by
  unfold coneCoeff
  rw [if_neg (show ¬ (n - 1 + 3 ≤ n) by omega),
      if_neg (show ¬ (n - 1 + 2 = n) by omega)]

/-- Each `coneCoeff` value is `≥ 0` when `v ∈ K_n`. -/
theorem coneCoeff_nonneg (n : Nat) (hn : 3 ≤ n) (v : Nat → Int) (h : InKone n v)
    (k : Nat) (hk : k < n) : 0 ≤ coneCoeff n v k := by
  obtain ⟨h1, h2, h3⟩ := h
  by_cases hca : k + 3 ≤ n
  · -- Pair-ray slot: c k = 2 · partialSum v (k + 1), with k + 1 ∈ {1, …, n - 2}.
    rw [coneCoeff_low n v k hca]
    have hp : 0 ≤ partialSum v (k + 1) := h1 (k + 1) (by omega) (by omega)
    omega
  · by_cases hcb : k + 2 = n
    · -- Sum-ray slot: c (n - 2) = partialSum v n ≥ 0 (full-sum facet).
      have hk_eq : k = n - 2 := by omega
      rw [hk_eq, coneCoeff_n_minus_two n (by omega) v]
      exact h2
    · -- E-ray slot: c (n - 1) = partialSum v (n - 1) - v (n - 1) ≥ 0 (E facet).
      have hk_eq : k = n - 1 := by omega
      rw [hk_eq, coneCoeff_n_minus_one n (by omega) v]
      omega

/-! ### Bridge: rewriting `partialSum` under pointwise equality -/

/-- If `f` and `g` agree on `{0, …, m - 1}`, their partial sums up to `m` agree. -/
theorem partialSum_congr {f g : Nat → Int} (m : Nat)
    (h : ∀ k, k < m → f k = g k) :
    partialSum f m = partialSum g m := by
  induction m with
  | zero => rfl
  | succ p ih =>
    show partialSum f p + f p = partialSum g p + g p
    have h_lt : ∀ k, k < p → f k = g k := fun k hk => h k (by omega)
    have ih_val : partialSum f p = partialSum g p := ih h_lt
    have hp : f p = g p := h p (by omega)
    rw [ih_val, hp]

/-- "Telescoping" step: when `n ≥ 1`, `partialSum v n = partialSum v (n - 1) + v (n - 1)`.

This is the variant of `partialSum_succ` we need when the predecessor is given by
`n - 1` (Nat subtraction) rather than by destructuring `n = k + 1`. -/
theorem partialSum_step (v : Nat → Int) (n : Nat) (hn : 1 ≤ n) :
    partialSum v n = partialSum v (n - 1) + v (n - 1) := by
  cases n with
  | zero => omega
  | succ m => rfl

/-- For any coordinate `j` and any upper bound `m ≤ n - 2`, the partial sum of the
pair-ray contributions using `coneCoeff n v` equals the partial sum using the
"low" closed form `2 · partialSum v (k + 1)`.

Reason: all indices `k < m ≤ n - 2` satisfy `k + 3 ≤ n`, so `coneCoeff` lands in
its pair-ray branch. -/
theorem partialSum_pair_coneCoeff_eq (n : Nat) (v : Nat → Int) (j m : Nat)
    (hm : m + 2 ≤ n) :
    partialSum (fun k => coneCoeff n v k * pairRay k j) m =
    partialSum (fun k => 2 * partialSum v (k + 1) * pairRay k j) m := by
  apply partialSum_congr
  intro k hk
  have hk_n : k + 3 ≤ n := by omega
  rw [coneCoeff_low n v k hk_n]

/-! ### Theorem G — Lemma 4 -/

/-- **Theorem G, Lemma 4 (form (b), `N = 2`).**  For `n ≥ 3`, every `v ∈ K_n`
admits an explicit non-negative integer linear combination of the `n` extreme
rays equal to `2 · v`.  Witness: `coneCoeff n v`.

Statement: there exists `c : Nat → Int` with
* `c k ≥ 0` for `k < n`, and
* `2 · v j = linComb n c j` for all `j < n`.

The factor of `2` is the lattice-index obstruction (§4 of scoping doc): the ray
lattice has index `2` in `ℤⁿ`.  See `Kone_two_in_cone_hull`'s body for the
constructive witness and `TheoremG-scoping.md` §4 for the math context. -/
theorem Kone_two_in_cone_hull (n : Nat) (hn : 3 ≤ n) (v : Nat → Int)
    (h : InKone n v) :
    ∃ c : Nat → Int,
      (∀ k, k < n → 0 ≤ c k) ∧
      (∀ j, j < n → 2 * v j = linComb n c j) := by
  refine ⟨coneCoeff n v, coneCoeff_nonneg n hn v h, ?_⟩
  intro j hj
  unfold linComb
  rw [partialSum_pair_coneCoeff_eq n v j (n - 2) (by omega),
      coneCoeff_n_minus_two n (by omega) v,
      coneCoeff_n_minus_one n (by omega) v]
  -- Goal:
  -- 2 * v j = partialSum (fun k => 2 * partialSum v (k + 1) * pairRay k j) (n - 2)
  --        + partialSum v n * sumRay n j
  --        + (partialSum v (n - 1) - v (n - 1)) * eRay n j
  by_cases hj0 : j = 0
  · -- Coordinate j = 0: only `pairRay 0` contributes; sumRay, eRay vanish at 0.
    subst hj0
    rw [partialSum_pair_at_zero (fun k => 2 * partialSum v (k + 1)) (n - 2)
          (by omega),
        sumRay_off n 0 (by omega) (by omega),
        eRay_off n 0 (by omega) (by omega)]
    -- Goal:
    --   2 * v 0 = 2 * partialSum v (0 + 1)
    --           + partialSum v n * 0
    --           + (partialSum v (n - 1) - v (n - 1)) * 0
    rw [partialSum_succ, partialSum_zero]
    omega
  · by_cases hjm2 : j = n - 2
    · -- Coordinate j = n - 2: pair part = -c (n - 3), sumRay = 1, eRay = 1.
      subst hjm2
      rw [partialSum_pair_at_j (fun k => 2 * partialSum v (k + 1)) (n - 2)
            (by omega),
          sumRay_at_n_minus_two n,
          eRay_at_n_minus_two n]
      -- After β: pair part = -(2 * partialSum v ((n - 2 - 1) + 1)).
      have h_nm21 : n - 2 - 1 + 1 = n - 2 := by omega
      rw [h_nm21]
      -- partialSum v n unfolds via n = (n - 1) + 1 (using partialSum_step).
      have hpn : partialSum v n = partialSum v (n - 1) + v (n - 1) :=
        partialSum_step v n (by omega)
      -- partialSum v (n - 1) unfolds via (n - 1) = (n - 2) + 1.
      have hpn1 : partialSum v (n - 1) = partialSum v (n - 2) + v (n - 2) :=
        partialSum_step v (n - 1) (by omega)
      omega
    · by_cases hjm1 : j = n - 1
      · -- Coordinate j = n - 1: pair part = 0 (all k ≤ n - 3 are "below"),
        --   sumRay = 1, eRay = -1.
        subst hjm1
        rw [partialSum_pair_below (fun k => 2 * partialSum v (k + 1)) (n - 1)
              (n - 2) (by omega),
            sumRay_at_n_minus_one n (by omega),
            eRay_at_n_minus_one n (by omega)]
        -- Goal: 2 * v (n - 1) = 0 + partialSum v n * 1
        --                     + (partialSum v (n - 1) - v (n - 1)) * (-1)
        have hpn : partialSum v n = partialSum v (n - 1) + v (n - 1) :=
          partialSum_step v n (by omega)
        omega
      · -- Coordinate j with 1 ≤ j ≤ n - 3: pair part = c j - c (j - 1),
        --   sumRay = 0, eRay = 0.  This is the "interior" range.
        have hj_pos : 1 ≤ j := by omega
        have hj_le : j + 1 ≤ n - 2 := by omega
        rw [partialSum_pair_above (fun k => 2 * partialSum v (k + 1)) j (n - 2)
              hj_pos hj_le,
            sumRay_off n j (by omega) (by omega),
            eRay_off n j (by omega) (by omega)]
        -- Goal: 2 * v j = 2 * partialSum v (j + 1) - 2 * partialSum v ((j - 1) + 1)
        --              + (...) * 0 + (...) * 0
        have h_jm1 : j - 1 + 1 = j := by omega
        rw [h_jm1, partialSum_succ]
        omega

/-! ## Theorem G — Lemma 5: uniqueness of coefficients

If two integer coefficient sequences `c, c'` both produce the same vector via
`linComb`, they must agree on `{0, …, n - 1}`.  This is the "rays are a basis
of their span" content of Lemma 3 phrased as uniqueness of decomposition.

The proof mirrors `rays_lin_indep` but is phrased directly on the difference
`c - c'` without invoking `Int` distributivity (the case-by-case linComb
evaluation gives a linear system on differences that `omega` closes). -/

/-- **Theorem G, Lemma 5 (uniqueness).** Coordinate-wise injectivity of
`linComb n c` on `{0, …, n - 1}` viewed as a function of `c`.

If `linComb n c j = linComb n c' j` for every `j < n`, then `c k = c' k` for
every `k < n`. -/
theorem rays_lin_indep_unique (n : Nat) (hn : 3 ≤ n) (c c' : Nat → Int)
    (h : ∀ j, j < n → linComb n c j = linComb n c' j) :
    ∀ k, k < n → c k = c' k := by
  -- Step 1: c k = c' k for k ≤ n - 3, by induction on k (coordinate-descent).
  have hc_low : ∀ k, k ≤ n - 3 → c k = c' k := by
    intro k hk
    induction k with
    | zero =>
      have h0 := h 0 (by omega)
      unfold linComb at h0
      have e1c  : partialSum (fun k => c k * pairRay k 0) (n - 2) = c 0 :=
        partialSum_pair_at_zero c (n - 2) (by omega)
      have e1c' : partialSum (fun k => c' k * pairRay k 0) (n - 2) = c' 0 :=
        partialSum_pair_at_zero c' (n - 2) (by omega)
      have e2 : sumRay n 0 = 0 := sumRay_off n 0 (by omega) (by omega)
      have e3 : eRay   n 0 = 0 := eRay_off   n 0 (by omega) (by omega)
      rw [e1c, e1c', e2, e3] at h0
      omega
    | succ p ih =>
      have ih_val : c p = c' p := ih (by omega)
      have hj := h (p + 1) (by omega)
      unfold linComb at hj
      have e1c : partialSum (fun k => c k * pairRay k (p + 1)) (n - 2) =
          c (p + 1) - c p :=
        partialSum_pair_above c (p + 1) (n - 2) (by omega) (by omega)
      have e1c' : partialSum (fun k => c' k * pairRay k (p + 1)) (n - 2) =
          c' (p + 1) - c' p :=
        partialSum_pair_above c' (p + 1) (n - 2) (by omega) (by omega)
      have e2 : sumRay n (p + 1) = 0 :=
        sumRay_off n (p + 1) (by omega) (by omega)
      have e3 : eRay n (p + 1) = 0 :=
        eRay_off n (p + 1) (by omega) (by omega)
      rw [e1c, e1c', e2, e3] at hj
      omega
  -- Step 2: c (n - 3) = c' (n - 3) (special case).
  have hcnm3 : c (n - 3) = c' (n - 3) := hc_low (n - 3) (by omega)
  -- Step 3: c (n - 2) + c (n - 1) = c' (n - 2) + c' (n - 1) from j = n - 2.
  have hsum : c (n - 2) + c (n - 1) = c' (n - 2) + c' (n - 1) := by
    have hj := h (n - 2) (by omega)
    unfold linComb at hj
    have e1c  : partialSum (fun k => c k * pairRay k (n - 2)) (n - 2) =
        -c (n - 3) :=
      partialSum_pair_at_j c (n - 2) (by omega)
    have e1c' : partialSum (fun k => c' k * pairRay k (n - 2)) (n - 2) =
        -c' (n - 3) :=
      partialSum_pair_at_j c' (n - 2) (by omega)
    have e2 : sumRay n (n - 2) = 1 := sumRay_at_n_minus_two n
    have e3 : eRay   n (n - 2) = 1 := eRay_at_n_minus_two   n
    rw [e1c, e1c', e2, e3] at hj
    omega
  -- Step 4: c (n - 2) - c (n - 1) = c' (n - 2) - c' (n - 1) from j = n - 1.
  have hdiff : c (n - 2) - c (n - 1) = c' (n - 2) - c' (n - 1) := by
    have hj := h (n - 1) (by omega)
    unfold linComb at hj
    have e1c  : partialSum (fun k => c k * pairRay k (n - 1)) (n - 2) = 0 :=
      partialSum_pair_below c (n - 1) (n - 2) (by omega)
    have e1c' : partialSum (fun k => c' k * pairRay k (n - 1)) (n - 2) = 0 :=
      partialSum_pair_below c' (n - 1) (n - 2) (by omega)
    have e2 : sumRay n (n - 1) = 1 := sumRay_at_n_minus_one n (by omega)
    have e3 : eRay   n (n - 1) = -1 := eRay_at_n_minus_one   n (by omega)
    rw [e1c, e1c', e2, e3] at hj
    omega
  -- Conclude: solve the 2x2 system for c (n - 2), c (n - 1).
  intro k hk
  by_cases hk_low : k ≤ n - 3
  · exact hc_low k hk_low
  · by_cases hk_eq : k = n - 2
    · rw [hk_eq]; omega
    · have hk_eq2 : k = n - 1 := by omega
      rw [hk_eq2]; omega

/-! ## Theorem G — Headline bundle: `K_simplicial`

The headline result of Theorem G, bundling Lemmas 1–5: for `n ≥ 3`, every
`v ∈ K_n` admits a unique non-negative integer linear combination of the `n`
extreme rays equal to `2 v` (the factor of 2 is the lattice-index obstruction
from `TheoremG-scoping.md` §4).

This is the formal Lean witness that `K_n` is a simplicial cone (the rays are
a basis of `K_n` as a rational cone, with explicit lattice-index-2 caveat). -/

/-- **Theorem G (form (b) bundle):** `K_n` is a simplicial cone in the sense
that every `v ∈ K_n` admits a unique non-negative integer combination of the
`n` rays equal to `2 v`.

Combines:
* Lemma 4 (`Kone_two_in_cone_hull`) — existence and non-negativity,
* Lemma 5 (`rays_lin_indep_unique`) — uniqueness on `{0, …, n - 1}`. -/
theorem K_simplicial (n : Nat) (hn : 3 ≤ n) (v : Nat → Int) (h : InKone n v) :
    ∃ c : Nat → Int,
      (∀ k, k < n → 0 ≤ c k) ∧
      (∀ j, j < n → 2 * v j = linComb n c j) ∧
      (∀ c' : Nat → Int,
         (∀ j, j < n → 2 * v j = linComb n c' j) →
         ∀ k, k < n → c k = c' k) := by
  obtain ⟨c, hc_nn, hc_eq⟩ := Kone_two_in_cone_hull n hn v h
  refine ⟨c, hc_nn, hc_eq, ?_⟩
  intro c' hc'_eq k hk
  apply rays_lin_indep_unique n hn c c' _ k hk
  intro j hj
  have h1 : 2 * v j = linComb n c j := hc_eq j hj
  have h2 : 2 * v j = linComb n c' j := hc'_eq j hj
  omega

/-! ### Sanity check: kernel axioms -/

#print axioms Kone_two_in_cone_hull
#print axioms rays_lin_indep_unique
#print axioms K_simplicial
#print axioms E_nonredundant
#print axioms L_nonredundant
#print axioms U_nonredundant
#print axioms Fence_L
#print axioms Fence_U
#print axioms Fence_E
#print axioms Fence_L_distinct
#print axioms Fence_U_distinct
#print axioms Fence_L_kind_ne_Fence_U_kind
#print axioms Fence_L_kind_ne_Fence_E_kind
#print axioms Fence_U_kind_ne_Fence_E_kind

/-! ## Day 69 — # AXIS = 3 statement: `BdiCoord` and `AxisTriple`

Skeletal Lean formalization of the Day 69 PROVE result
`# AXIS(n) = 3, AXIS(n) = {prefix[1], prefix[n], long[1]}`
(1-indexed math; 0-indexed Lean: `prefix[0], prefix[n-1], long[0]`).

This section pins down the **statement** of the result: a 3-element
`List (BdiCoord n)` with no duplicates and length 3.  The matching
predicate `IsAxis : BdiCoord n → Prop` (three rank-1 piece-pair
collisions on the coordinate wall) and the structural equality
`{c | IsAxis n c} = AxisTriple` are deferred to Day 70+, pending the
`Piece` / BDI-feasibility infrastructure and the proof of Lemma D
(exhaustion: no further AXIS coordinates).

The current skeletal `BdiCoord n` carries only the `prefix` and `long`
families, which are the two families touched by the AXIS triple at
uniform `n`.  Extending the type with the `short` family and the
even-n `linkLHS` coordinate is a deliberate next step. -/

/-- AII coordinate index at parameter `n`.  Skeletal: only the prefix
and long families are recorded.  TODO Day 70: extend with `short`
and (even-n) `linkLHS`. -/
inductive BdiCoord (n : Nat) where
  | prefix (i : Fin n) : BdiCoord n
  | long   (i : Fin n) : BdiCoord n
  deriving DecidableEq

/-- The AXIS triple at parameter `n ≥ 3`:
`[prefix[0], prefix[n-1], long[0]]` (0-indexed; math: prefix[1],
prefix[n], long[1]).  Represented as a `List` since this project is
stdlib-only; combine with `AxisTriple_nodup` to read off "3 distinct
elements." -/
def AxisTriple (n : Nat) (hn : 3 ≤ n) : List (BdiCoord n) :=
  [BdiCoord.prefix ⟨0, by omega⟩,
   BdiCoord.prefix ⟨n - 1, by omega⟩,
   BdiCoord.long   ⟨0, by omega⟩]

/-- The AXIS triple has length 3, uniformly in `n ≥ 3`. -/
theorem AxisTriple_length (n : Nat) (hn : 3 ≤ n) :
    (AxisTriple n hn).length = 3 := by
  rfl

/-- The AXIS triple has no duplicates: `prefix[0], prefix[n-1], long[0]`
are pairwise distinct in `BdiCoord n` whenever `n ≥ 3`.
Combined with `AxisTriple_length`, this is the Lean-level statement of
"# AXIS ≥ 3 with the explicit triple." -/
theorem AxisTriple_nodup (n : Nat) (hn : 3 ≤ n) :
    (AxisTriple n hn).Nodup := by
  simp [AxisTriple, List.Nodup]
  intro h
  omega

/-- **# AXIS = 3 — Lean-level statement (skeletal).**
The AXIS triple is a 3-element list of pairwise distinct
`BdiCoord n` values, uniformly in `n ≥ 3`.  This is the stdlib-only
analogue of `Finset.card (AxisTriple n) = 3` — without Mathlib's
`Finset` we package the claim as the conjunction of `length = 3`
(by `rfl`) and `Nodup` (by constructor disjointness + omega). -/
theorem AxisTriple_card (n : Nat) (hn : 3 ≤ n) :
    (AxisTriple n hn).length = 3 ∧ (AxisTriple n hn).Nodup :=
  ⟨AxisTriple_length n hn, AxisTriple_nodup n hn⟩

#print axioms AxisTriple
#print axioms AxisTriple_length
#print axioms AxisTriple_nodup
#print axioms AxisTriple_card

/-! ## Day 70 — `Piece n hn` and basic projections

Day-70 LEAN scaffolding for Lemmas A/B/C of the Day-69 PROVE writeup
(`proofs/2026-06-14-axis-uniform3-proof.md`).  Each AXIS coordinate is
forced by a **uniform 3-piece family**:

| Lemma | Family       | Wall coordinate          | Multiplicity `k` |
|-------|--------------|--------------------------|------------------|
| A     | R-double     | `prefix[0]`              | `k = 0, 1, 2`    |
| B     | free-top     | `prefix[n-1]`            | `k = 0, 1, 2`    |
| C     | free-bottom  | `long[0]`                | `k = 0, 1, 2`    |

`Piece n hn` is the disjoint union of these three families; the
constructor index `k : Fin 3` plays the role of the multiplicity that
ranges through `{0, 1, 2}` in the informal proof.  This is the
infrastructure layer — later sessions will attach BDI-feasibility
content (Lemmas A, B, C, D) on top.  Stdlib only. -/

/-- A Day-69 piece: one of three uniform 3-piece families, indexed by
multiplicity `Fin 3`.  Constructors correspond to Lemmas A / B / C of
the Day-69 PROVE writeup. -/
inductive Piece (n : Nat) (hn : 3 ≤ n) where
  | RDouble     (α : Fin 3) : Piece n hn
  | FreeTop     (k : Fin 3) : Piece n hn
  | FreeBottom  (k : Fin 3) : Piece n hn

/-- The AXIS coordinate that a piece projects onto.  R-double pieces
collide on `prefix[0]`; free-top on `prefix[n-1]`; free-bottom on
`long[0]`.  This matches the column shape of the Day-69 proof: pieces
within a family agree on every AII column except their AXIS coord. -/
def Piece.axisCoord {n : Nat} {hn : 3 ≤ n} (p : Piece n hn) : BdiCoord n := by
  cases p with
  | RDouble    _ => exact BdiCoord.prefix ⟨0, by omega⟩
  | FreeTop    _ => exact BdiCoord.prefix ⟨n - 1, by omega⟩
  | FreeBottom _ => exact BdiCoord.long   ⟨0, by omega⟩

/-- The multiplicity attached to a piece: literally the constructor's
`Fin 3` index, as a `Nat`.  By construction `mult ∈ {0, 1, 2}`. -/
def Piece.mult {n : Nat} {hn : 3 ≤ n} (p : Piece n hn) : Nat := by
  cases p with
  | RDouble    α => exact α.val
  | FreeTop    k => exact k.val
  | FreeBottom k => exact k.val

/-- Every piece's AXIS coordinate is one of the three AxisTriple
entries.  Discharged by case analysis on the piece. -/
theorem Piece.axisCoord_in_AxisTriple
    {n : Nat} {hn : 3 ≤ n} (p : Piece n hn) :
    p.axisCoord ∈ AxisTriple n hn := by
  cases p <;> simp [Piece.axisCoord, AxisTriple]

/-- **Three multiplicities on each AXIS coord.**  For every AXIS
coordinate `c`, the matching family produces three pieces with
multiplicities `0`, `1`, `2` (all projecting onto `c`).  This is the
Lean-side packaging of Lemmas A, B, C of Day-69: "each AXIS coord
admits three distinct rank-1 piece-pair collisions." -/
theorem Piece.three_mults_on_axisCoord
    (n : Nat) (hn : 3 ≤ n) (c : BdiCoord n) (hc : c ∈ AxisTriple n hn) :
    ∃ p0 p1 p2 : Piece n hn,
      p0.axisCoord = c ∧ p1.axisCoord = c ∧ p2.axisCoord = c ∧
      p0.mult = 0 ∧ p1.mult = 1 ∧ p2.mult = 2 := by
  simp [AxisTriple] at hc
  rcases hc with hc | hc | hc
  · exact ⟨Piece.RDouble 0, Piece.RDouble 1, Piece.RDouble 2,
      hc.symm, hc.symm, hc.symm, rfl, rfl, rfl⟩
  · exact ⟨Piece.FreeTop 0, Piece.FreeTop 1, Piece.FreeTop 2,
      hc.symm, hc.symm, hc.symm, rfl, rfl, rfl⟩
  · exact ⟨Piece.FreeBottom 0, Piece.FreeBottom 1, Piece.FreeBottom 2,
      hc.symm, hc.symm, hc.symm, rfl, rfl, rfl⟩

#print axioms Piece.axisCoord
#print axioms Piece.mult
#print axioms Piece.axisCoord_in_AxisTriple
#print axioms Piece.three_mults_on_axisCoord

end BdiPolytope
