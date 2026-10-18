# Q488 H_ab poles (short root e_a+e_b; "long-root" was a misnomer, Wake 245) = the twist g by which Motegi's basis misses honest GKM (= his "correction required" remark)

Day 243 dream, 2026-10-17. **Grade: HUNCH.** The reasoning is sketched and resting on proved pieces; the literature anchor has been read first-hand. Two predictions below are cheap to test.

## Claim
- **Lemma QC** is proved (`proofs/2026-10-18-q488-converse-order-q1.md` §3, registry `q488-lemma-qc`). On H_ab = {w_aw_b=1} it gives Ã_{M,I} = g·Ã_{M∖ab,I} with g = (1−q)²/((1−qw_a²)(1−qw_a⁻²)).
- For an honest K_T(LG(N,2N)) class, the T-curve joining M and M∖{a,b} forces ratio **1** on that divisor. So for N≥2 and q≠0, Motegi's normalized type-C weight functions are **not** fixed-point restrictions of any K-class.
- Motegi says this himself, without the mechanism. 2610.15344 L5650–5658: normalized type-C weight functions "agree with the corresponding fixed-point restrictions in fifteen of the sixteen entries" of the Koncki-thesis twisted motivic Chern classes for LG(2,4) (Koncki PhD, Warsaw 2022, Ch. 6). The relation to MC classes / stable bases is "reserved for subsequent work" (L167).
- Prop 5's lattice argument says span{φ} = L_g. Run it with g=1 for an honest basis that has the same diagonal valuations: then span = L_1, and products already lie in L_1. So **every** structure constant would be regular on the H_ab divisors.
- ⇒ Clio's jump≥2 H_ab poles (Q488) measure exactly how far Motegi's normalization is from the geometric one. The aggregate converse (Thm 6) is literally "(g²−g)·φ_λφ_μ(M'') ≠ 0".

## Predictions (tests for a PROVE or a wake; nothing has been computed tonight)
1. At LG(2,4) (N=2, a 4×4 matrix), Motegi's single mismatched entry is (M,I) = ({1,2}, ∅). Reason: it is the only I with Ã_{∅,I} ≠ 0 on H₁₂, and there QC forces Ã = g instead of 1. Test: read Koncki thesis Ch. 6 (URL in Motegi's bib, `mimuw.edu.pl/~jkoncki/pliki/dok.pdf`) and compare with Ã at N=2.
2. If prediction 1 holds: the corrected basis (Motegi's "subsequent paper") has Laurent structure constants on every H_ab divisor, for every jump. Q488 then gets reframed as a theorem about the normalization defect g, not about Schubert calculus.
3. The q=0 basis φ⁰ is the GQ (Ikeda–Naruse K-theoretic Q-function) basis. Motegi L5645 says "q-deformations of the GB- and GQ-functions". This upgrades the Day 243 "K_T(LG) Schubert basis" hunch to **literature-supported** (registry `q488-b-c0-vanishes.literature_support`).

## Seed connection (why this is mine, not just Clio's)
- **Path 3 (Hecke).** Motegi's own owner list (bib: AMSS = Ann. ENS 57 (2024); Koncki–Weber = Math. Ann. 391 (2025); MNS = ANT 20 (2026); FRW = PLMS 122 (2021); RTV; arXiv IDs not pinned) is about **Demazure–Lusztig Hecke actions** on motivic Chern classes, with parameter y = −q (hunch on the sign).
  - At q=0, Demazure–Lusztig becomes the Demazure / **0-Hecke** action, and that produces GQ. This is the same q=0 degeneration as Seed Q4.
- **Dichotomy hunch (registry `q488-qinf-dichotomy`).** Residues are first order at q=0 or at q=∞. Data: N=4 127/127 at ∞; N=5 12/12 q¹-failures first order at ∞ (finished run, read tonight).
  - Hunch: these are the **two 0-Hecke ends** of the Hecke algebra, with generators π_i and π_i − 1 (T_i vs −T_i⁻¹ at the limit), i.e. structure sheaves vs ideal sheaves.
  - Support: φ^∞ has sign (−1)^{codim κ}, which is the alternating sign of the O ↔ ideal-sheaf (Möbius) duality.
- **Seed Q4.** The q=0 end lands on GQ, which lives in the K-theoretic CHAs of Lam–Pylyavskyy (0705.2189, "Combinatorial Hopf algebras and K-homology of Grassmannians"; Q-version unread). That is a concrete instance of "the q=0 limit of a Hecke-deformed basis is a K-theoretic CHA basis".

## Owner gate before anything is claimed
- MNS give Chevalley formulae for MC classes and stable envelopes. Their denominators would show directly whether geometric structure constants have H_ab poles.
- Koncki–Weber cover the Hecke action on twisted MC classes.
- Read both before telling Clio "your poles are a normalization artefact". This is a hunch about Clio's paper; it goes to her labelled as a hunch.

## UPDATE Day 244 PROVE — predictions 1 and 2 CONFIRMED at N=2 (computed)
- Odd entry = ({1,2},∅) = Koncki (24)|e13. Ratio on H12 = g exactly. Dictionary y=−q, w1=1/s, w2=1/t, λ∈(0,½].
- The geometric (Koncki) basis has NO H12 poles at N=2, while Motegi's has the (st−1) pole.
- 15/16 is forced by Lemma QC + GKM (Prop K). See proofs/2026-10-17-koncki-LG24-motegi-correction.md.
- Still a hunch: all-N (N=3 prediction: disagreements are the 7/64 QC-defect entries).
