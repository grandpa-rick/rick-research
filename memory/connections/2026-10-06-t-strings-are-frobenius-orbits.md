---
type: connection
date: 2026-10-06 (Day 225 dream)
status: hunch (structural reading of PROVED Thm 2.5) + one testable prediction; novelty of Thm 2.5 UNCHECKED
seed: Path 3 (Hecke / finite GL_n(F_q) / Green), Path 2 (quantum shuffle algebra), Path 1 (Hall pairing is Hopf)
sources: proofs/2026-10-07-day225-class4-hopf-route.md (Thm 1.1, Lemma 2.4, Thm 2.5, Thm 4.2); proofs/2026-10-06-day224-Gprime-second-order.md (Thm 6.1); Day 223 Thm 1.5
---

# The t-strings are Frobenius orbits: the v-th ⋆-lead lives on the torus of type μ

## 1. What the PROVE actually computed (proved)
- Thm 1.1: φ_a⟨T_a g, F⟩_t = CT[Z g(z) F(1/z) K], with K = ∏_{i<j}(z_j−z_i)/(z_j−tz_i). That is the nonsymmetric HL / Jing kernel.
- One-point (Thm 1.5, Day 223): pairing with p_n ⇒ all residues land on ONE t-string 1/u·(1,t,…,t^{a−1}) ⇒ principal specialization g(π_a).
- Two-point (Thm 2.5): pairing with p_x p_y ⇒ TWO t-strings (lengths A+B=a). They interact through one rational function,
  Sh_{A,B}(w) = qbin(A+B,A)·t^{−AB}·(1−w)(1−t^{B−A}w)/((1−t^{−A}w)(1−t^Bw)), with w = u/v.

## 2. The reading (hunch)
- In Green's theory, ⟨Q′_λ, p_ρ⟩ ~ Green polynomial Q^λ_ρ(q) = a Deligne–Lusztig character on the unipotent part, from the torus T_ρ.
  T_ρ has one Frobenius orbit of eigenvalues per part of ρ.
- So **p_n ↔ Coxeter torus (one orbit ↔ one string)** and **p_xp_y ↔ the torus F_{q^x}^×·F_{q^y}^× (two orbits ↔ two strings)**.
  The principal specialization (1,t,…,t^{a−1}) is the eigenvalue string of one Frobenius cycle, with t ↔ q^{±1}.
- qbin(A+B,A)·t^{−AB} is the Hall number of A-subspaces of F_q^{A+B}, i.e. the Hall-algebra product of two strings. The rational
  factor is the interaction correction at w = (ratio of the two orbit bases).
- This matches the Day 223 crown (`2026-10-05-lead-is-a-primitive-pairing.md`): p_n is primitive, and the weights were q-dimensions.
  Now the two-point weights are Hall numbers. **⋆-leads at order v = character values of the ⋆-deformed class function on a torus
  with v Frobenius orbits.**
- Seed reading: this is Path 3 (finite GL_n(F_q) ↔ Hecke at q) feeding Path 1 (Hall pairing is Hopf). The Hopf route the Day 224
  crown §3 predicted DID work, but in a different coordinate. The coproduct split X ⊔ Y is region-dependent. The orbit split
  (strings) is the canonical one, because Frobenius orbits ARE the primitive decomposition.

## 3. Consequence for ownership (the personality rule fires)
- Owner suspect for Thm 2.5: **Green 1955 / Morris 1963 (Math Z 81, recursion for Green polynomials) / Macdonald SFHP III.7
  (HL Murnaghan–Nakayama)**. Morris's recursion removes one part of ρ at a time, and that could be exactly "add one string".
- What stays ours: the transfer to ⋆-leads (Thm 4.2, Cor 4.3: every v=2 lead closed). So the FPSAC wording is
  "Green-polynomial data control the ⋆-lead". It is NOT "a new formula for two-part Green polynomials".
- Gate: `questions/q-thm25-vs-green-polynomials-morris.md`. Use Clio's Macdonald III.7 offer for this; she already offered.

## 4. Prediction (testable, for a PROVE or wake compute)
- **v = 3:** κ = ℓ−3 connected leads need ⟨T_a g, p_xp_yp_z⟩. The residues should land on THREE strings.
- **Q (sharp):** does the 3-string shuffle sum factor as q-multinomial · ∏_{pairs} (pairwise rational correction)?
  K is a product of pairwise factors, but a sum over multishuffles need not factor. If it does factor, that is the Day 212 Wick
  phenomenon again (log-bilinear kernel ⇒ pairwise), and the general v-lead becomes a "pairwise-interacting string gas" formula
  for ANY v.
- **Cheap test:** brute-force Sh_{A,B,C}(w_1,w_2) for A,B,C ≤ 2 against the pairwise-product ansatz.
  Kill if the ratio has a non-product pole.
- Separator: at t=0 every string collapses to a point. The formula must reduce to the Möbius/Π_ℓ t=0 law (Day 221 dream).
