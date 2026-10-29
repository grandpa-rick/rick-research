# For Clio (fold into the 11-04 send, NOT a separate email): the LS12 matching is explicit

Long draft WIP 85a6fc1, new **Remark 4.22** (`rem:LSbij`). Full proof: `proofs/2026-10-30-q48-ls-vmap.md`.

Rem 4.21 used to say that LS12's antidominant Chevalley rule (Cor 3.4, (3.6)) matches our Thm 4.20 "once down-lift paths are matched
with V-maps — not in LS12, checked by machine m ≤ 4". That matching is now a theorem, for all m:

- The LS paths of shape ω_m with ι ≤ z_ρW_P and down-lift z_κ are exactly the paths (κ∖g⁻¹(o); κ) with a = ½ (straight if g has no o),
  one for each V-map g on θ = κ/ρ. The weight −p(1) is v_κ + Σ_{g(x)=o} β(x), and the sign is (−1)^{|θ|}.
- The key lemma: for ρ ⊆ λ, the Deodhar down-lift of z_ρ to the λ-coset is z_λ iff λ/ρ is an antichain. Proof by induction on
  boxes, using Deodhar's property Z (Björner–Brenti 2.2.7) and the add/remove/neutral trichotomy for s_c w_μ.
- Consequence: a second proof of the Thm 4.20 formula from LS12 + (KT) alone, with no reciprocity and no BR12.
- Machine m ≤ 5: 0 failures; without the w0 twist it fails (14/45 at m = 3/4).

If you're reviewing the long draft: the remark is ~20 lines, and Rem 4.21's last sentence now points to it. Nothing in the FPSAC cut
(6dbecb8) changed.
