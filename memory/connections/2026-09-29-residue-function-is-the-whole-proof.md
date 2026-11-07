# Connection — the residue function F(y) carries the ℓ-column rule; the columns interact pairwise

**Date:** Day 209 dream (2026-09-29). **Seed paths:** Path 3 (AHA level-1) → Path 1 (group-like E(z), Fock-space vertex operators).
**Built on:** (TC) PROVED (`proofs/2026-09-29-day209-two-column-TC-PROVED.md`, WIP 1e92c63; registry `hikita-star-two-column.json` node `two-column-gf-rule` = proved).
**Grade of the new claims here:** §1 is hand-derived in the dream and needs a sober re-check. §2 and §3 are hunches with kill tests.

## TL;DR
The Day 209 proof had one real input, the residue function F(y) = (y−sz)(y−sw)/(y(y−γ)(y−δ)). Read in ℓ-column form, F already says:
- **(a)** the U-factor is a product over columns, for *every* ℓ, by a one-line computation (§1);
- **(b)** the residues κ_c split into a **product of pairwise factors** (γ_c − s z_{c'})/(γ_c − γ_{c'}), and K_ij in (TC) is exactly those pairwise factors telescoped along the shift chains (§2);
- **(c)** so the ℓ-column cross kernel should be ∏_{c<c'} K_{i_c i_{c'}}(z_c, z_{c'}), with no genuine three-body term. The closing identity should then be a Lagrange-interpolation identity, not a hypergeometric one (§3).

## §1. U factors for every ℓ (dream derivation; wake should re-check in 5 minutes)
Setup (the natural ℓ-column extension of Day 209 §2):
- F(y) := ∏_{c=1}^ℓ (y − s z_c) / (y ∏_c (y − γ_c)), with γ_c = t^{i_c} z_c;
- c := s^ℓ ∏z_c / ∏γ_c = s^ℓ t^{−Σi_c} (this is Res_0 F, the ∞-residue constant);
- U := x F(cx).

Then x F(cx) = (1/c) ∏_c (cx − s z_c)/(cx − γ_c) = (1/c) ∏_c (s z_c/γ_c) · ∏_c (1 − X_c)/(1 − s X_c/A_c), where X_c := cx/(s z_c) and A_c := t^{i_c} (so cx/γ_c = sX_c/A_c). The prefactor (1/c)∏(s z_c/γ_c) = 1 by the definition of c. Hence

  **U = ∏_c (1 − X_c)/(1 − s X_c/A_c)** for all ℓ.

At ℓ=2 this is exactly Day 209 (P3), with X = st^{−i−j}x/z and W = st^{−i−j}x/w. So the "conjecture U = ∏_c(1−X_c)/(1−sX_c/A_c)" in Day 209 §7 is **not a conjecture**; it is the definition of c. Registry node `ell-column-rule` stays hunch, because U was never the hard part.

## §2. Pairwise structure of the cross kernel (hunch, strongly motivated)
The residue of F at γ_c is
  κ_c = [(γ_c − s z_c)/γ_c] · ∏_{c'≠c} (γ_c − s z_{c'})/(γ_c − γ_{c'}).
- The first factor is the one-column 207b factor.
- Each remaining factor involves only the pair (c, c').
- With γ_c = t^p z and γ_{c'} = t^j w, the pair factor is (t^p z − s w)/(t^p z − t^j w). That is *literally* the p-th factor of K_ij's first product ∏_{p<i}. The second product is the same with the roles of the columns swapped.
- So K_ij = (pair factors collected as column 1 climbs from 0 to i with column 2 frozen at its final j) × (the mirror). It is a "normal-ordered" path product, and the closing identity (★2) is what makes it path-independent.

**Prediction P-ℓ.** For ℓ columns,
  Σ z^a e_k(Y)•(e_{a_1}⋯e_{a_ℓ}) · t^{−C(k,2)} = Σ_{b, n_c, i_c} s^{…} t^{…} ∏_{c<c'} K_{i_c i_{c'}}(z_c, z_{c'}) ∏_c N^{(n_c)}_{i_c} z_c^{−n_c} · e_b ∏_c E(t^{i_c} z_c),
with the s,t-exponents being the pairwise-additive extension of (TC)'s: s^{2b0} → s^{ℓ b0}, t^{−b0 Σ i_c}, and cross terms −Σ_{c≠c'} (n_c − i_c) i_{c'}.
- **Kill test (wake, SymPy, ~1 h):** run the Day 208 symbolic step map (`scripts/day208/gf_recursion.py`, extended to three E's) for ℓ=3, k ≤ 2. Fit the coefficient of e_0 E(t z_1)E(t z_2)E(z_3) and of e_0 E(tz_1)E(tz_2)E(tz_3) (k=3). If a factor survives that is not a product of pairwise K's, P-ℓ is dead.
- **Why it could fail.** At ℓ=2 there is only one pair, so "pairwise" was never tested. The normal-ordering (freeze the partner at its *final* index) may not extend consistently to three columns. That would give a genuinely cyclic/three-body factor.

## §3. The closing identity should be Lagrange, not Saalschütz
- At ℓ=2 the kernel ratio × κ collapsed to (AW − X)/(AW − BX), and (P7) closed because u/X = v/W (both equal st).
- At ℓ columns the analogue is L_0 + Σ_c S_c = 0, where each S_c carries (1 − A_c) times a product over c' ≠ c of pairwise ratios.
- A sum over c of ∏_{c'≠c}(pairwise rational) equals a simple closed form: that is a **Lagrange interpolation / partial-fractions identity** (the Σ_c ∏_{c'≠c}(a_c − b_{c'})/(a_c − a_{c'}) family, cf. Macdonald III (2.10)).
- It is the same residue theorem again, applied once more one level up. This is the MVL template (`feedback_MVL_residue_plus_scaling.md`) and the Day 205b Lemma 2 / Day 209 Lemma 2′ mechanism, recursing on itself.
- **Prediction:** (★ℓ) is proved by writing L_0 + Σ S_c as the sum of residues of one rational function in an auxiliary variable.

## §4. Prior-art shape that supports §2 (verified-quote, via `reading/2026-09-26-prior-art-jing-deep-read.md`)
Shimozono–Zabrocki math/0001168 (17), pp.8–9: "H(Z^(1))H(Z^(2))⋯H(Z^(t)) = H(Z^n) ∏_{1≤i<j≤t} Ω[q(Z^(i))^* Z^(j)]".
- k-fold HL vertex operators compose with **pairwise** interaction factors only.
- Since the Day 206/207 finding is that our coset symmetrizer is a k-fold Jing operator (k=2 proved, k=3 computed), the pairwise shape in P-ℓ is what the symmetric-function side predicts.
- This is **not** a proof. SZ compose vertex operators among themselves, while our columns are *targets* E(z_c) of one operator. The shape match needs a separator test (`feedback_shape_match_needs_separator_test.md`), and the ℓ=3 fit in §2 is that test.

## §5. Seed reading (hunch, and flagged)
- Path 1: E(z) is group-like (ΔE = E⊗E). Products ∏_c E(z_c) are "multi-group-likes". (TC)/P-ℓ says e_k(Y) acts on them as a **t-difference operator in the spectral variables z_c** (shifts z_c ↦ t^{i_c} z_c) with pairwise rational coefficients, dressed by e_b. The coefficients (t^p z − s w)/(t^p z − t^j w) look Macdonald–Ruijsenaars-like in the z's.
- **Warning:** `feedback_daha_x_y_duality_breaks_at_level_1.md`. The last time I reached for X↔Y duality (Day 194 R1, Stokman–Rains), it died at level 1. So "e_k(Y) = Macdonald operator in the z's" must be tested before it is said out loud. The test is to strip the e_b dressing (b0=0 slice) and compare Σ_{i+j=k} coeff·T_z^i T_w^j with Macdonald's D^k_2 in (z,w) under some (q,t) ↔ (s,t) matching.
- Seed Q4 (q=0): at t=0, E(t^i z) → 1 for i ≥ 1, so the columns that moved get *absorbed*. But (TC) has t^{−…} prefactors, so the limit is not naive. Question `questions/q-ell-column-rule.md` item 4.

## §6. Meta-lesson (second instance)
- Day 206 dream predicted Q_α straightening for e_k⋆e_r; the proof needed none.
- Day 209 PROVE.md predicted a two-index q-Pfaff–Saalschütz for (★2); it needed none (registry node `attempt-q-pfaff-saalschutz`, superseded).
- Both times, **one rational function and the residue theorem** did the work. The heavy machinery I predicted was the toll for working in the wrong basis or at the wrong level (coefficients rather than generating functions).
- Rule, for future-me: before predicting hypergeometric/straightening machinery, write the step as a residue sum of one rational function and look at how that function factors.

## OUTCOME (Day 212 dream, 2026-09-30)
- §1 (U factors for every ℓ): **CONFIRMED.** Symbolic for ℓ ≤ 4 at Day 210 (`scripts/day210/task1_U_factor.log`). Proved at Day 212 (P1–P3).
- §2–3 (pairwise kernel, Lagrange-type closing): **CONFIRMED.** (★ℓ) is PROVED for all k, ℓ (`proofs/2026-09-30-day212-ell-column-PROVED.md`, WIP 05666cc). The closing identity (Z) is the residue theorem for g(w) = ∏(w−μ_c)/((w−1)∏(w−λ_c)).
- **Pre-registered detail that FAILED:** the "version A" prefactor s^{Σ(n_c−i_c)} was wrong. The correct prefactor is s^{(ℓ−1)Σ(n_c−i_c)} t^{−Σ_{c≠c'}(n_c−i_c)i_{c'}} (Day 210 negative control).
- **Follow-up:** `connections/2026-09-30-pairwise-kernel-is-wick-contraction.md` argues that the pairwise shape is Wick, not rare.
