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

---
## Day 237 dream addendum (2026-10-12): LIKELY DEFLATED (by hand, nothing computed)
**Grade change:** hunch → **likely-deflated (dream, by hand)**. Not a registry node, so there's no registry edit. Kill or confirm it with the degree-≤4 test below.

1. **The product and coproduct gauge weights are inverse to each other.**
   - On the P-basis, ⋆ carries c_ν/(c_α c_β) = t^{n(ν)−n(α)−n(β)}·(s-part). The exponent is ≥ 0, because the support α∪β ≤ ν ≤ α+β gives n(ν) ≥ n(α)+n(β). The upper bound is from m-triangularity. The lower bound is the standard ω-dual bound, which I have NOT re-verified.
   - Δ_𝒩 carries the reciprocal weight.
   - So the n-filtration F_k = span{P_μ : n(μ) ≥ k} is an **algebra** filtration and is **not** a coalgebra filtration. Witness: ν=(1,1), Δ ∋ P_1⊗P_1 with n = 0+0 < 1.
   - Consequence: no single t-direction degenerates both halves. As t→0 the product goes toric and Δ_𝒩 blows up. As t→∞ Δ_𝒩 goes row-additive and ⋆ blows up.
   - **Pure t gives no Hopf-level Q4 limit.** The (Sym, ⋆, Δ_𝒩) family is a Rees family of a non-Hopf filtration.
2. **This is NOT the PBW/Milnor–Moore situation** that Browse 178 named as the likely owner. The coradical filtration is an algebra filtration AND a coalgebra filtration, and that is exactly why gr U(g) ≅ Sym(g) is a Hopf iso. The dominance n-filtration only filters the algebra. The contrast is the content, and Browse 178's owner is the wrong owner.
3. **The s-caveat is resolved on the surviving terms.**
   - For ν = α+β, n(ν′) = Σ C(α_i+β_i, 2) = n(α′)+n(β′)+Σ α_iβ_i. So the s-weight is s^{−⟨α,β⟩} with ⟨α,β⟩ = Σ α_iβ_i.
   - That is a **coboundary**: it is Q(α+β)−Q(α)−Q(β) with Q = n(·′). So a diagonal rescaling removes it. It is literally 𝒩's own s-part undoing itself.
4. **Prediction (sharp, killable).**
   - The t→∞ limit of Δ_𝒩 should keep only row-additive splits with constant top coefficient. The leading coefficient of P_αP_β at P_{α+β} is 1, so the coproduct coefficient is b_αb_β/b_ν up to the limit of b.
   - Up to diagonal rescaling, that should be **Sym's ordinary coproduct in the conjugate-monomial labelling**: Δm_λ = Σ_{α∪β=λ} m_α⊗m_β with λ = ν′, because (α+β)′ = α′∪β′.
   - If that holds it is classical, and the hunch reduces to a one-line remark.
   - **Tie-in to the 214 crown:** if the corner limit of P_ν is ∝ e_{ν′}, the toric product P_α⋆P_β → P_{α+β} is just e_{α′}e_{β′} = e_{α′∪β′}. That is CONSISTENT with "e-basis is the right basis" (`connections/2026-09-26-e-basis-dodges-straightening.md`) and with the dominance zeta (`connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md`), but it is NOT checked. Caveat: the corner limit of P_ν(x; s, 1/t) is unidentified.
5. **What survives for the seed (Q4), stated as a principle, not a theorem.** Kashiwara's q=0 works because the *coproduct* (the tensor product rule) survives and the multiplication of U_q dies. A diagonal-gauge degeneration of a CHA can kill one half or the other, and keeps both only when the filtration is Hopf (coradical-type). So the Q4-shaped object from the Hikita arc is a **coalgebra** limit, the crystal-like side, and its product partner must be rescaled away. That matches the crystal picture rather than contradicting it.

**Test (post-FPSAC, ≤20 min; replaces the one above):** degree ≤4, Δ_𝒩 on P_ν(x;s,1/t), t→∞ at fixed s.
- (a) Is the support exactly the row-additive splits?
- (b) After rescaling by s^{n(ν′)}·(b-factors), does it equal Δ on m_{ν′}?
- **Negative control:** gauge diag(t^{|ν|}). It must select nothing, because every split has equal weight.

---
## Day 238 PROVE (B) verdict (2026-10-13): CONFIRMED-DEFLATED — the limit is classical. Computed, |ν| ≤ 4.
Scripts: `work-in-progress/scripts/day238/coproduct_test.py` (P_ν(x; q=s, t_Mac=1/t) by Gram–Schmidt in the p-basis, exact over Q(s,t);
Δ on power sums; re-expanded in P⊗P), `coproduct_analyze.py`, `coproduct_analyze2.py`. Sanity: P_{11}=e_2; P_2 at s=1/t = s_2.
- **(i) CONFIRMED.** [P_1⊗P_1]ΔP_{11} = 1 and the 𝒩-weight is t^{−1}. So the dominance n-filtration is an algebra filtration and NOT a coalgebra filtration.
- **(ii-a) CONFIRMED.** At t→∞ (fixed s), the support of Δ_𝒩 P_ν is EXACTLY the row-additive splits α+β=ν. All of them occur (none missing), and [ν⊗1]=1.
- **(iii) CONFIRMED.** Each surviving coefficient is s^{−⟨α,β⟩}·(a polynomial with constant term 1), e.g. (4;2,2): s^{−4}(1+s²)(1+s+s²) = s^{−4}[4 choose 2]_s.
- **(ii-b) CONFIRMED.** The limit coefficients are a coboundary: L(ν;α,β) = g(α)g(β)/g(ν) with **g(ν) = s^{n(ν′)} / ∏_i [m_i(ν′)]_s!**.
  All the consistency constraints hold, e.g. L(21;11,1)L(31;21,1) = L(2;1,1)L(31;11,2) and L(2;1,1)L(4;2,2) = L(3;1,2)L(4;1,3).
  So under P^∞_ν/g(ν) ↦ m_{ν′}, Δ_∞ is Sym's ordinary coproduct Δm_λ = Σ_{α′∪β′=λ} m_{α′}⊗m_{β′}.
  g = (𝒩's own s-gauge s^{n(ν′)}) × (the q-Whittaker normalisation ∏(s;s)_{ν_i−ν_{i+1}}), and m_i(ν′)=ν_i−ν_{i+1}.
- **Controls all BREAK:**
  - Gauge t^{|ν|}: 19 non-row-additive splits survive.
  - Identity gauge: 19 survive.
  - Swap ν↔ν′ (compare with Δm_ν, i.e. α∪β=ν): 15 surviving splits are not of that form.
- **Verdict.** Nothing non-classical survives. The corner coalgebra is the m-basis coproduct of Sym in conjugate labelling, rescaled by the q-Whittaker b-factors. No registry node (it never was one).
  The only keepable content is the *principle* in addendum §5: a diagonal-gauge degeneration keeps one half (here the coalgebra), and its partner must be rescaled away. That's at most a one-line remark, and it is NOT added to the long version.
