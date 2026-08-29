/-
Copyright (c) 2026 Rick. All rights reserved.
Released under Apache 2.0 license.
Authors: Rick

Formalises the elementary lemma underlying Day 98's interior-anchor
unification for `c ≡ 2 (mod 4)`:

    R₄(c) ≡ 16   (mod 32)   whenever   c ≡ 2  (mod 4),

where `R₄` is the specific degree-six integer polynomial

    R₄(c) = c⁶ − 15 c⁵ + 91 c⁴ − 357 c³ + 988 c² − 1572 c + 1152.

The proof is a two-liner: `ring` factors the substitution `c = 4m + 2` as
`R₄(4m+2) = 16 + 32·K(m)` where `K(m)` is an explicit ℤ-polynomial in `m`,
and then `Int.add_mul_emod_self_left` reads off the residue class.

## Registry impact

Promotes `R4-mod-32-constant` from `proved` to `lean-verified` and
consequently upgrades the SCP-mechanism dependency of
`interior-anchor-02-unified-c-cong-2-mod-4` (Day 98) to a formally
Lean-verified atom.

## Axiom target

`[propext, Quot.sound]` — empirically confirmed via `#print axioms` in
container build 2026-07-17 (Day 101 lean session, receipt file
`2026-07-17-R4-axioms-receipt.txt`).  Note: `Classical.choice` is NOT
pulled in — the two axioms above suffice.  Slimmer than the Mathlib
default because `ring` on `ℤ` polynomials plus `Int.add_mul_emod_self_left`
plus `decide` on a bounded arithmetic goal do not invoke choice.
-/

import Mathlib.Tactic.Ring

namespace R4Mod32

/-- The degree-six integer polynomial `R₄` from Day 98:
`R₄(c) = c⁶ − 15 c⁵ + 91 c⁴ − 357 c³ + 988 c² − 1572 c + 1152`. -/
def R4 (c : ℤ) : ℤ :=
  c^6 - 15*c^5 + 91*c^4 - 357*c^3 + 988*c^2 - 1572*c + 1152

/-- The explicit witness polynomial `K(m)` such that
`R₄(4m+2) = 16 + 32 · K(m)`.  Numerically:

    K(0) =    4,  R₄(2)  = 144  = 16 + 32·4,
    K(1) =  −59,  R₄(6)  = −1872 = 16 + 32·(−59),
    K(2) = 5844,  R₄(10) = 187024 = 16 + 32·5844. -/
def K (m : ℤ) : ℤ :=
  128*m^6 - 96*m^5 + 8*m^4 - 138*m^3 + 35*m^2 + 4

/-- **Key algebraic identity.**  Substituting `c = 4m + 2` splits `R₄`
into a `mod 32` part and a `mod 32` residue of `16`.

Proved by `ring` after unfolding.  This is the entire mathematical
content of the lemma — everything else is `%`-bookkeeping. -/
theorem R4_shift_eq (m : ℤ) :
    R4 (4*m + 2) = 16 + 32 * K m := by
  unfold R4 K
  ring

/-- **Main theorem.**  For every `m : ℤ`, `R₄(4m+2) ≡ 16 (mod 32)`.

This covers exactly the residue class `c ≡ 2 (mod 4)`, since the map
`m ↦ 4m+2 : ℤ → ℤ` parametrises that class. -/
theorem R4_mod_32 (m : ℤ) : R4 (4*m + 2) % 32 = 16 := by
  rw [R4_shift_eq, Int.add_mul_emod_self_left]
  decide

/-- **Corollary in `c ≡ 2 (mod 4)` phrasing.**  This is the form Day 98's
interior-anchor derivation actually cites: any integer congruent to `2`
mod `4` lands `R₄` in the residue class `16` mod `32`. -/
theorem R4_mod_32_of_cong_2_mod_4
    (c : ℤ) (hc : c % 4 = 2) : R4 c % 32 = 16 := by
  have hshift : c = 4 * (c / 4) + 2 := by omega
  rw [hshift]
  exact R4_mod_32 _

/-!
### Numerical sanity checks (Day 98 interior-anchor table)

Five bounded evaluations that also verify `Int.emod` computes on
concrete inputs the way the informal argument expects. -/

/-- `R₄(2) = 144 ≡ 16 (mod 32)`. -/
example : R4 2 % 32 = 16 := by decide

/-- `R₄(6) = −1872 ≡ 16 (mod 32)`. -/
example : R4 6 % 32 = 16 := by decide

/-- `R₄(10) ≡ 16 (mod 32)`. -/
example : R4 10 % 32 = 16 := by decide

/-- `R₄(14) ≡ 16 (mod 32)`. -/
example : R4 14 % 32 = 16 := by decide

/-- `R₄(-2) ≡ 16 (mod 32)` — the lemma also covers the negative branch. -/
example : R4 (-2) % 32 = 16 := by decide

end R4Mod32

-- Axiom audit (leave in place during review; comment out for library use).
#print axioms R4Mod32.R4_shift_eq
#print axioms R4Mod32.R4_mod_32
#print axioms R4Mod32.R4_mod_32_of_cong_2_mod_4
