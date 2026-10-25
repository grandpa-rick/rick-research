# Crown J — the half-step is a row deletion at cost 2^{−part} (Day 257 dream, 2026-10-25)

**Status:** (1) is checked by hand in this dream from the printed statements. (2) and (3) are hunches.
Registry: `q488-oc-half-step-T-ribbons` (proved, PROVE 257), `q488-oc-T-XP-identities` (proved), `q488-oc-T-mobius` (proved).
Draft: Prop 6.16 `prop:T`, §6.5 `ssec:halfstep`, Thm C `thm:C` (main.tex l.1337), WIP 45cf937.

## Claim
The move "delete one part κ_r and pay 2^{−κ_r}" has now turned up four times in the LG/OG arc:
- **Thm C** (PROVE 251/253): H_κ(−3/2) = 2^{−κ₁} H_{κ′}(−1).
- **Theorem HZ shift lemma** (PROVE 254): value 1 ↔ deletion shift.
- **Lemma C / Φ** (`proofs/2026-10-23-odd-zero-law.md` l.80–98): Φ = Π(1+y_i)^{−1}, Φ(0) = 2^{−m}. Each row contributes a factor (1+y)^{−1} → ½.
- **X/P of PROVE 257**: P(κ,ν) = δ + 2^{−κ_{r₀}}[ν ≺ κ], so P(κ,∅) = 2^{−κ₁}.

These four are one operator seen four ways.

## (1) Thm C is the ∅-column of Prop 6.16. Checked by hand, from print
Take x = 1 in (a), so s_{3/2} = T s_1. By Thm C, H_ν(−1) = δ_{ν∅}, so the vector s_1 is e_∅. Hence (−1)^{|κ|}H_κ(−3/2) = T(κ,∅).
Apply (b) with θ = D(κ):
- If ℓ(κ) ≥ 2, θ has ≥ 2 diagonal boxes, so the weight is 0. This matches Thm C's zero.
- If κ = (k), θ is a horizontal ribbon with one diagonal box, and ε = +1 for k ≥ 2. The weight is (−½)^k = (−1)^k·2^{−k}. This matches Thm C with H_∅ = 1.
- If κ = (1), the weight is ½ = (−1)·H_{(1)}(−3/2) = (−1)(−½). This matches.
So the paper contains Thm C twice and does not say so.
**Polish item:** add one sentence after Prop 6.16: "the column ν = ∅ of (b) at x = 1 recovers Theorem C".
This doubles as a free consistency check of the printed (b) at a non-degenerate index (k ≥ 2 tests ε).

## (2) Hunch: T is the K-theory matrix of "tensor with a square root of O(1)"
- T² = A_oA_e is the matrix of one hyperplane step x → x+1 (Lemma `lem:layers`(a)).
- Crown D (Day 251) and PROVE 251 give 2^m H(−a−½) = χ(∧^•U(−a)), with ∧^•U = O(−½) ⊗ spinor.
- So T should be the matrix of ⊗ 2^{−m}·(spinor-type class) in the X_κ basis. The weights 2^{−κ_r} are the Φ factors.
- Test (post-submission, Q43): for m = 2, 3, expand 2^{−m}[∧^•U]·[O_{X_κ}] in the basis {[O_{X_ν}]} (Euler pairing against the dual basis). Compare the coefficients with T, up to the sign gauge S.
- **Kill condition:** the expansion does not match T in any gauge (S, or the twist e^{−ω/2}). Commuting with A_oA_e is not a test, because every polynomial in T does that.

## (3) Seed reading (Path 1)
- ζ and ζ_o are zeta functions in the incidence algebra of the distributive lattice of shifted shapes. A_e and A_o are their signed Möbius inverses, by Lemma `lem:mobius`.
- T is the unique unitriangular square root of S ζ_o^{−1} ζ^{−1} S. That is the ABS uniqueness argument for characters of a graded connected object (math/0310016: the character group is pro-unipotent, so square roots are unique).
- X ζ = ζ_o P is an **intertwiner between the two zeta functions**: X carries the full order to the equal-length order, at the cost of one deleted row.
- Echo of the Day 214 crown (s=t=0 ⋆ = dominance zeta function). In this programme the hard operators keep collapsing to zeta/Möbius data of a poset plus one cheap correction.
- Lesson (already in feedback_conjugate_by_sign_and_zeta_before_sqrt): before taking a root, divide out the zetas.

## Why it matters
- (1) is a free referee-proof cross-check that costs one sentence.
- (2), if true, puts §6.5 inside the geometry instead of next to it, and explains the 2^{−k} weights.
- (3) is the Seed Path 1 framing for the eventual talk.
