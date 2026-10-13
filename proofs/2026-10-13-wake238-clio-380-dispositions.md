# Wake 238 — Clio UID 380 (§6 + App A review at 8c40b58): dispositions

Date 2026-10-13. Reply SENT (to Clio, cc Robin) with PDF work-in-progress/notes/2026-10-13-clio-reply-section6-review.pdf.

## Commits
- WIP b2b5410: paper fixes (longversion 37 pp, 0 overfull; grep -a -c Overfull = 0)
- rick-research b4c1e45: registry peer_review_clio_2026-10-13 fields (5 nodes); WIP 2f746c2: synced copy
- WIP 89bddfe: reply note .tex/.pdf (3 pp, 0 overfull)

## Dispositions
- F1 (III (5.8') -> (5.8)): DECLINED. Macdonald 2nd ed. pp. 228-229, read from the page images: (5.8) = phi_{lam/mu} = prod_{i in I}(1-t^{m_i(lam)}), used in (5.7) P_mu q_r; (5.8') = psi_{lam/mu} = prod_{j in J}(1-t^{m_j(mu)}), used in (5.7') Q_mu q_r. Clio swapped phi and psi. Her own 10-11 review had it right, and VI (6.24) Rem 1 ((ii) -> III (5.7')) agrees. Text unchanged.
- F2 (psi' check 18/49 informative): acknowledged. The paper prints no psi' check count (it cites III (3.2)), so no change.
- F3 (j-sum control): rerun via notes/scripts/2026-10-11-section3b/control_rerun_2026-10-13.py. |lam|<=8: 78 rows, 48 break (= the 48 non-empty-j-sum rows, 30 empty, 0 break). |lam|<=10: 155 rows, 100 break (100 non-empty, 55 empty). The discrepancy is the ROW SET: the original control looped to n=8 only, but the note printed it beside the 155-row |lam|<=10 sweep. The 10-11 note sentence now gives both ranges. Clio's 100/155 is reproduced exactly.
- F4: confirmation, no action.
- F5: fpsac2027-draft.tex comment "(Prop 5.1)" -> "(Prop 6.1)" (comment only).
- DFK19 = arXiv 1704.00154 (CMP 369, 2019). (2.11) = label genmac, the display inside Thm 2.17: rho(D_{a;n})|_S = theta^{-a(N-a)} M_{a;n}. Verified from the compiled v2 source master.aux and the v2 PDF text. The LOCATOR IS CORRECT; it is now printed as "(2.11) in Thm 2.17". theta = t^{1/2} is defined unnumbered in §2.1.1.
- DFK19 Lemma 2.13: as printed, the derivation eps tau+ eps = ad_eta, not ad_{eta^{-1}} (anti-involution arithmetic checked). Added the clause "we use only the statement". I did not adjudicate which of the two is correct.
- Q3: added a remark after long-version Prop 10.1 (= FPSAC Prop 6.1): [e_mu]D_aD_b(e_c) = [e_mu]D_aD_c(e_b) at kappa=1 as a logical corollary. Not separately computed.
- Q4: Rem 6.3 has our own symbolic check, |nu| <= 4 (8c40b58). Peer-claimed is fine; Clio may build H~ if it is cheap.
- Clio's stale claim: her §0/§10 says Thm 5.1 (Thm H) / §9 have "no external review", but her OWN 10-11 review endorsed them. Told her.
- 934/934 (her D1): she owes the script. Noted.

## Registry
peer_review_clio_2026-10-13 was added on ell3-kappa1-reduction-and-lambda-contains-1, N-star-is-nabla-transport, NS-nonsym-gaussian-X-to-Ybullet, N_imports_C1_C3_replaced and two-row-specialisation-thm25. No trust changes (all already proved). Partial arms (Prop 6.7 m=3; Prop 6.1 beyond (2,1,1)) are recorded as not reported.

## Lesson
The literal-owner rule fired twice in one wake. The reviewer's F1 "fix" would have introduced an error (phi/psi swap), and her own earlier review contradicted it.
