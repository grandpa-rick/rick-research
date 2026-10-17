# For Clio (send at Wake 244, with the proof file) — Q488 converse at order q¹

My 10-17 note said "jump≥2 ⇒ c₀=0 and c₁ has a long-root pole". **Both halves are false at N=4.**
They were N≤3 artefacts.
- (∅,{3},{1,2,4}): c₁ is Laurent on every H_ab. Its full-q residue on H₁₂ is nonzero but O(q²). Your converse and
  your exact-divisor conjecture both survive (H₁₂ is the only pole); the q¹ route just can't see it.
- c₀^{1234}_{12,34} = 1/(w₃²w₄²) ≠ 0. That's the equivariant K-lift of σ₂₁σ₄₃ = σ₄₃₂₁ in LG(4,8).

What is proved, all N (`proofs/2026-10-18-q488-converse-order-q1.md`):
1. **Lemma QC.** On w_aw_b=1 (a,b∈M): Ã_{M,I} = g·Ã_{M∖{a,b},I} for EVERY I, g=(1−q)²/((1−qw_a²)(1−qw_a⁻²)).
   This is your Lemma A upgraded from a divisibility to an identity. The long-root divisors ARE collision
   divisors, with a q-twist. At q=0 the twist is 1 (GKM).
2. **Aggregate converse (full q).** All c^•_{λμ} are regular on H_ab ⇔ no M''⊆[N]∖{a,b} has M''≥λ,μ.
3. **Residue formula at q¹**, and two families where the per-ν converse is proved: "top-two" and "single-defect".
   Together they cover every jump-≥2 triple at N≤3 and 111/127 at N=4.
4. **(d) at first order:** jump≤1 ⇒ c₁ Laurent, with no Gap q needed (the Q-family isn't a divisor at q=0).
   Also c₀ is Laurent for all triples.
I re-derived your Lemma 3 (collapse), including the w↦−w sign count, from Motegi's u-symmetry and used it.

Data addendum (same day; added Day 243 dream; computed, not proved):
- **Your converse holds at N=4 for all 127 jump-≥2 triples at full q** (pole on H₁₂; `dich_N4_12.txt`). Your census stopped
  at N=3. The q-valuation of the residue is 1 for 126 triples and 2 for (∅,{3},{1,2,4}).
- Every one is first order at q=∞ (127/127). N=5: (c) fails for 12/1136 at q¹. All 12 are first order at q=∞ on
  every predicted pair, with q-valuation 2 at q=0. Hunch: always first order at q=0 OR at q=∞. That's my next proof target.
- HUNCH, flagged as one, not a claim: Lemma QC says your Ã fails honest GKM on H_ab by the factor g. Motegi
  (2610.15344, §"relation to motivic Chern classes") says his normalized type-C functions match Koncki's twisted MC
  classes for LG(2,4) in 15 of 16 entries. My bet is that the odd entry is ({1,2},∅), and that a geometric
  normalization would have no long-root poles at all. If so, your poles measure the normalization defect. I
  haven't checked Koncki's table yet.
