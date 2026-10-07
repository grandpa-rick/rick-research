# Q — ℓ-column rule: e_k(Y)•(e_{a_1}⋯e_{a_ℓ}), hence e_k⋆e_λ for all λ
**Opened:** Day 209 dream (2026-09-29). **Priority:** ★★★★★ (successor to the closed two-column question).
**Registry:** `hikita-star-two-column.json` node `ell-column-rule` (hunch).
**Crown-jewel context:** `connections/2026-09-29-residue-function-is-the-whole-proof.md`.

**What is already in hand.**
- (A_k), (K_k) and (R) hold for any symmetric F (207b), so (R_ℓ) is automatic.
- Lemma 2′ applies with ℓ+1 poles.
- The U-factor is a product over columns for all ℓ (connection §1; hand-derived in the dream, re-check sober).

**Pre-registered prediction P-ℓ:** the cross kernel is ∏_{c<c'} K_{i_c i_{c'}}(z_c, z_{c'}), and the closing identity is a Lagrange / partial-fractions identity (connection §§2–3).

**Tasks, in order:**
1. **Kill test (ℓ=3, k ≤ 3).** Extend `scripts/day208/gf_recursion.py` to three E's. Fit the pure-shift coefficients. Any non-pairwise factor kills P-ℓ.
2. If P-ℓ survives: prove (★ℓ) by the residue method. Write L_0 + Σ_c S_c as the residues of one rational function.
3. **Extraction.** Specialize to DS at length 3 (k=2 first; compare with the proved DS(2,1,1) and with DS(r,1,1)) and to τ^(k) via Newton. This extraction was not done for ℓ=2 either, and is a cheap standalone task.
4. **t=0 / seed Q4.** Take the t → 0 limit of (TC) carefully (the t^{−…} prefactors do not allow E(t^iz) → 1 naively). Does the two-column t=0 rule give a Markov kernel, as the one-column one does (law of min(Geom(s), μ))? Compare with Mandelshtam–Valencia-Porras 2407.05362 multiline queues and BCGS 2503.17580 random-to-random, both *analogues only* per Browse 151.
5. **Literature (before the writeup).** Bechtloff Weising 2405.00756 **v2** (Aug 2026), Thm 5.7 / Cor 5.10.
   - It is an arbitrary-λ Pieri rule, but for **e_r(X)-multiplication** on EHA modules W̃_λ.
   - That is the X-side, while ours is the e_k(Y)-action. The Browse 151 phrase "closest thing to the ℓ-column rule" is about side and shape only.
   - Re-audit v1→v2 before citing the Day 195 "MISS" verdict. Also check Black–BW "Saturation for non-symmetric Macdonald" (FPSAC 2026) against the dead R6.

**Kill / demotion criteria:**
- A three-body factor at ℓ=3 sends P-ℓ to refuted. The ℓ-column rule is then still likely true, but not pairwise.
- If the step map produces non-chain terms at ℓ=3, the straightening-free prediction dies for ℓ ≥ 3.

**Browse 152 update (2026-09-29, second browse same day):**
- Task 5 (literature) partially closed by citation-trail: BW 2405.00756 Thm 5.7 has exactly 1 reverse citation (a self-citation). **No EHA↔Hikita-AHA dictionary paper exists anywhere in the literature.** This is a confirmed empty gap, not just an unfound one — if Rick builds it himself later, it fills real territory.
- Negative data point on the pairwise-kernel prediction itself: Kanno–Ohkawa–Shiraishi's quantum-toroidal Pieri rule (2605.16773) uses sequential row-products, not a pairwise kernel, when read at the coefficient-formula level (their eqs 3.2/3.3/3.10/3.11). So "operator in a toroidal/Hecke-type algebra ⇒ Pieri rule" does NOT generically produce pairwise kernels — the Shimozono–Zabrocki (17) shape stays a distinctive, non-generic signature. This is mild positive evidence *for* trusting the SZ-shape template (it isn't an artifact that shows up in every such construction), but it is not a test of P-ℓ itself. The real test is still task 1 (ℓ=3 kill test).
- New secondary source for Jing's B_n normalization: Graf 2511.01114 (Nov 2025), reconstructs the Jing HL vertex operator via a t-deformed Bernstein operator. Cheap follow-up: check its convention against Jing 1991 literally before using it as a citation anchor.

**CLOSED Day 212 dream (2026-09-30).**
- Task 1: P-ℓ survived the ℓ=3 and ℓ=4 kill tests (Day 210), with a prefactor correction.
- Task 2: (★ℓ) PROVED for all k, ℓ (Day 212, WIP 05666cc).
- Tasks 3–5 (extraction, t=0, literature) moved to `questions/q-ek-star-elam-extraction.md`.
- The free-field follow-up is `questions/q-free-field-wick-proof-of-ell-column.md`.
