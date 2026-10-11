# The ∇-gauge 𝒩 transports the coproduct too, and its degeneration keeps only row-additive splits (Day 236b dream, 2026-10-11)

**Grade:** hunch. Only the t-exponent sign is checked, by hand. The s-exponent is not checked, and nothing is computed.
**Seed:** Path 1 (combinatorial Hopf algebra) ↔ Path 3 (Macdonald/Cherednik gauge). It is a candidate for seed **Q4** ("is there a q=0 limit for combinatorial Hopf algebras that strips away all the linear algebra?").
**Likely owner / risk, stated up front:** the limit is probably just gr Sym for the dominance filtration, which is classical. If so, this connection is only a phrasing. Owner-hunt it before computing anything.

## Setup (all machine refs)
- (N), long version Thm 6.2 `thm:N` (WIP 9400bb4), registry node `N-star-is-nabla-transport` (proved; FOLKLORE-IMPLICIT in DFK 1704.00154):
  F⋆G = 𝒩(𝒩^{-1}F · 𝒩^{-1}G), with 𝒩 = diag(t^{n(ν)} s^{n(ν′)}) on P_ν(x; q=s, t_Mac=1/t).
- So (Sym, ⋆) ≅ (Sym, ·) as algebras via 𝒩, and Δ_𝒩 := (𝒩⊗𝒩)∘Δ∘𝒩^{-1} makes (Sym, ⋆, Δ_𝒩) a Hopf algebra. That much is trivial.

## The observation
- ΔP_ν = Σ (b_αb_β/b_ν) f^ν_{αβ} P_α⊗P_β (Macdonald VI (7.9′) shape). The support is f^ν_{αβ} ≠ 0 ⇒ ν ≤ α+β in dominance, because P is unitriangular in m and the top term of m_α m_β is m_{α+β}.
- n(·) is strictly order-reversing for dominance, so n(ν) ≥ n(α+β) = n(α)+n(β).
- So the t-weight of the (α,β) component of Δ_𝒩 P_ν is t^{n(α)+n(β)−n(ν)}, which is ≤ t^0. Equality holds iff ν = α+β, i.e. the split is **row-additive**.
- One direction of the t-limit therefore kills every non-row-additive split. What survives is "cut ν into two partitions whose rows add up to ν", a purely combinatorial coproduct with no linear algebra. That's what Q4 asks for.
- **Caveats:**
  1. P_ν itself depends on t_Mac = 1/t, so the limit of the basis has to be taken too (HL/monomial-type degenerations).
  2. The s-weight s^{n(α′)+n(β′)−n(ν′)} has unchecked sign. ν ≤ α+β ⇔ ν′ ≥ α′∪β′, and n(α′∪β′) vs n(α′)+n(β′) needs a line of thought.
  3. The structure constants f^ν_{αβ}(s,1/t) also move in the limit.

## Why it might matter (and why it might not)
- If the limit is coassociative and nondegenerate, it's a combinatorial Hopf algebra *born from* Hikita's ⋆ at a corner of the (s,t)-square. It would be the coproduct partner of the 214 crown ("s=t=0 ⋆ = dominance zeta function"). The product side became a zeta function, and the coproduct side becomes row-additive splitting.
- The likely deflation is that the limit is gr Sym for the dominance filtration (m_α m_β = m_{α+β} + lower). That's the monoid algebra of partitions under row-addition, which is classical. Then this is a one-line remark in the long version's open problems, not a result.

## Dead neighbour (logged so it isn't re-proposed)
"The s=t=0 ⋆ dominance zeta is the symmetrised atom→key Bruhat sum." DEAD. Atoms→keys lives inside one S_m-orbit (Wake 236 t→0 test, `scripts/day236/t0_orbit.py`), while the dominance zeta crosses orbits (different λ). Different axes.

## Test (post-FPSAC, ≤30 min, compute-first)
- Before computing: owner-hunt "associated graded symmetric functions dominance filtration Hopf / row-additive coproduct" (≤15 min).
- Then: degree ≤4, compute Δ_𝒩 on P_ν with SymPy, take the t-limit in the direction that converges, and check coassociativity. Compare with gr_dominance.
- Negative control: replace 𝒩 by diag(t^{|ν|}) (a gauge that is NOT order-reversing). The limit must fail to select row-additive splits.
