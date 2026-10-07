# Q — With p_2(Y)-Pieri proved, is DS(2,1,1) now proved?  [CLOSED 2026-09-26, Day 207: YES — DS(r,1,1) PROVED all r ≥ 2]
**Opened:** Day 206 dream (2026-09-25). **Priority:** ★★★ (cheap: a re-read, no compute).
- Registry `ds-lambda-211-via-p2Y-pieri` is still `computed`. Its premises: `p2Y-pieri-lemma` (PROVED Day 206b §6) and `newton-decomposition-analytic` (proved). The children τ^(3)/τ^(4) are unrelated extras.
- Day 198 derived DS(2,1,1) via C = p_2(Y)•e_2 + 2tD (`proofs/2026-09-17-day198-DS-211-via-p2-pieri.md`, in rick-research only).
- **Task:** re-read cold. Is D itself proved? [Correction Day 207: D = e_2⋆e_2 = W_2, NOT "e_1⋆(e_1⋆e_2)-type"; it is covered by W_r (Day 206b), not Sub-Lemma Z.] If so, write the 1-page proof and promote. This would be the first DS instance at length 3 that is a theorem.

## CLOSED — 2026-09-26 (Day 207)
- **Answer: yes.** DS(r,1,1) is proved for all r ≥ 2 (sharpened form: support = {(r+2),(r+1,1),(r,2),(r,1,1)}, leading q^{-3}, off-diagonal ∝ (1−q^{-1})). Self-proved, not peer-checked.
- **Proof:** `proofs/2026-09-26-day207-DS-r11-proved.md` (also in WIP repo `proofs/`).
  - Route 1 (direct, preferred): C_r = e_1(Y)•(e_1(Y)•e_r) = (1−s)[r+1]·e_1(Y)•e_{r+1} + s·e_1(Y)•(e_1e_r); Thm 3.12 (operator form) + Sub-Lemma Z. No W_r / p_2(Y) needed.
  - Route 2 (Day 198): C_r = p_2(Y)•e_r + 2t·W_r; all inputs proved (Newton, Lemma 1 incl. τ_r, W_r).
- **Checks:** `proofs/scripts/day207/ds_r11_direct_check.py` (r=2..5, m=r+2,r+3, exact, ALL OK); `ds_r11_route_consistency.py` (both routes = closed form symbolically in r).
- **Registry:** `ds-lambda-211-via-p2Y-pieri` → proved; new node `ds-lambda-r11-all-r` (proved); τ^(3)/τ^(4) computed extras moved under `pk-Y-pieri-meta-conjecture` (boundary rule).
- **Next:** (r,2,1) needs only a "Sub-Lemma Z₂": e_1(Y)•(e_2e_r).

## CLOSED (Day 207 dream): DS(r,1,1) PROVED for all r≥2 on Day 207 (`proofs/2026-09-26-day207-DS-r11-proved.md`, WIP e99cb59). Registry `hikita-star-dominance-support.json` synced (paths fixed, WIP ab8caef).
