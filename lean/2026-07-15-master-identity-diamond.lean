/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises the **master identity (◊)** of Day 96 §11 of Rick's β'(c) program:
for all natural numbers `c, k, j` with `j ≤ k ≤ c`,

    (c − k + 1)_{k − j} · c^{↓j} = c^{↓k},

where
* `(a)_n = a · (a+1) · (a+2) · ⋯ · (a+n-1)` is the ascending Pochhammer
  (Mathlib's `Nat.ascFactorial`);
* `c^{↓j} = c · (c-1) · ⋯ · (c-j+1)` is the descending factorial
  (Mathlib's `Nat.descFactorial`).

## Why this identity

Both sides equal `c! / (c-k)!` when reduced to ordinary factorials. The
identity is the algebraic engine that reduces the `Q_k(a, 0, c)` linearity
step in Theorem 11.5 (Day 96) to `L_j(c) = c^{↓j}`, and hence unlocks the
`Qk-leading-a-vanishing` chain.

## The Lean proof (two rewrites)

Mathlib already has both ingredients:

1. `Nat.add_descFactorial_eq_ascFactorial'`
       `(n + k - 1).descFactorial k = n.ascFactorial k`
   Applied with `n = c - k + 1, k' = k - j`, and combined with the
   ℕ-arithmetic identity `(c - k + 1) + (k - j) - 1 = c - j` (`omega`
   under `j ≤ k ≤ c`), this rewrites the ascending Pochhammer as
   `(c - j).descFactorial (k - j)`.

2. `Nat.descFactorial_mul_descFactorial`
       `(n - k').descFactorial (m - k') * n.descFactorial k' = n.descFactorial m`  (for `k' ≤ m`)
   Applied with `n = c, k' = j, m = k`, and hypothesis `j ≤ k`, this
   closes the goal.

The proof is *literally* these two rewrites plus one `omega`. No induction,
no clever bijection — the reindexing lemma we need is exactly the
Mathlib-canonical descending-times-descending law.

Registry impact: promotes `master-identity-diamond` from `proved` to
`lean-verified`. Axiom set target: `[propext, Classical.choice, Quot.sound]`
(Mathlib default; no extra axioms).
-/

import Mathlib.Data.Nat.Factorial.Basic

namespace MasterIdentityDiamond

/-!
### The master identity (◊)
-/

/-- **Master identity (◊).** For `j ≤ k ≤ c` in ℕ,
    `(c − k + 1)_{k − j} · c^{↓j} = c^{↓k}`,
    where `(a)_n = Nat.ascFactorial a n` and `c^{↓j} = Nat.descFactorial c j`.

The proof is:
* rewrite the ascending Pochhammer as `(c - j).descFactorial (k - j)` via
  `Nat.add_descFactorial_eq_ascFactorial'`;
* apply `Nat.descFactorial_mul_descFactorial` at `n = c, k = j, m = k`. -/
theorem master_identity_diamond
    {c k j : ℕ} (hjk : j ≤ k) (hkc : k ≤ c) :
    Nat.ascFactorial (c - k + 1) (k - j) * Nat.descFactorial c j
      = Nat.descFactorial c k := by
  -- Step 1: rewrite the ascending Pochhammer as a descending factorial.
  have heq : (c - k + 1) + (k - j) - 1 = c - j := by omega
  have hAsc :
      Nat.ascFactorial (c - k + 1) (k - j)
        = (c - j).descFactorial (k - j) := by
    have h := Nat.add_descFactorial_eq_ascFactorial' (c - k + 1) (k - j)
    -- h : ((c - k + 1) + (k - j) - 1).descFactorial (k - j)
    --       = (c - k + 1).ascFactorial (k - j)
    rw [heq] at h
    exact h.symm
  -- Step 2: apply the descending-times-descending law.
  rw [hAsc]
  exact Nat.descFactorial_mul_descFactorial hjk

/-!
### Numerical sanity checks (Day 96 table §11)

These `example`s just re-verify the paper-table cases and do not extend the
API. They cost nothing to keep and give a fast-fail signal if `descFactorial`
or `ascFactorial` are ever redefined upstream.
-/

/-- `c=5, k=3, j=1`: `(3)_2 · 5^{↓1} = 12 · 5 = 60 = 5^{↓3}`. -/
example : Nat.ascFactorial (5 - 3 + 1) (3 - 1) * Nat.descFactorial 5 1
    = Nat.descFactorial 5 3 :=
  master_identity_diamond (by decide) (by decide)

/-- `c=6, k=4, j=2`: `(3)_2 · 6^{↓2} = 12 · 30 = 360 = 6^{↓4}`. -/
example : Nat.ascFactorial (6 - 4 + 1) (4 - 2) * Nat.descFactorial 6 2
    = Nat.descFactorial 6 4 :=
  master_identity_diamond (by decide) (by decide)

/-- `c=8, k=5, j=0`: `(4)_5 · 8^{↓0} = 6720 · 1 = 6720 = 8^{↓5}`. -/
example : Nat.ascFactorial (8 - 5 + 1) (5 - 0) * Nat.descFactorial 8 0
    = Nat.descFactorial 8 5 :=
  master_identity_diamond (by decide) (by decide)

/-- `c=7, k=3, j=3`: `(5)_0 · 7^{↓3} = 1 · 210 = 210 = 7^{↓3}` (trivial `j = k`). -/
example : Nat.ascFactorial (7 - 3 + 1) (3 - 3) * Nat.descFactorial 7 3
    = Nat.descFactorial 7 3 :=
  master_identity_diamond (by decide) (by decide)

/-!
### A convenience alias

Downstream `Q_k(a, 0, c)`-linearity arguments (Day 96 §11) prefer the
identity in the form solving for `c^{↓k}`. This is definitionally the same
statement, packaged for `rw`-friendly use. -/

/-- `c^{↓k} = (c − k + 1)_{k − j} · c^{↓j}`, the (◊) identity rearranged
to expose `descFactorial c k` on the LHS for `rw`ing. -/
theorem descFactorial_split
    {c k j : ℕ} (hjk : j ≤ k) (hkc : k ≤ c) :
    Nat.descFactorial c k
      = Nat.ascFactorial (c - k + 1) (k - j) * Nat.descFactorial c j :=
  (master_identity_diamond hjk hkc).symm

end MasterIdentityDiamond
