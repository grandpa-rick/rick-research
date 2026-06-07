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

end BdiPolytope
