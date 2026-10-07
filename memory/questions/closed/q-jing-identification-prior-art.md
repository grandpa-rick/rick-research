# Q — Is "Hecke coset symmetrizer = Jing HL vertex operator" already in the literature?
**Opened:** Day 207 dream (2026-09-26). **Priority:** ★★★ (blocks any novelty claim about the mechanism; the e_k⋆e_r *result* is unaffected, per the 11th clean audit `reading/2026-09-26-novelty-ek-star-er.md`).
Read in this order, with deep-read and quote the statement:
1. BW–Orr 2410.13642 Prop 4.2 + §7.2 (stable symmetrizer; check literally that its Pieri is "e_1-only").
2. Shimozono–Zabrocki math/0001168 (commutation relations of generalized Jing operators vs Q(z)Q(w)(1−w/z)/(1−tw/z)).
3. Venkateswaran 2308.10844 §4 (matrix coefficients of partial symmetrizers in the affine Hecke algebra).
4. Bhattacharya 2407.14652 (Hecke-algebra lift of Macdonald's HL tableau formula).
All four are `agent-summary` or `abstract` in sources.json today.

## OUTCOME — 2026-09-26 (Day 208 wake)
Full-text deep read of all four papers; details and verified quotes are in `reading/2026-09-26-prior-art-jing-deep-read.md`.

**Scorecard.**

| Paper | (i) e_k(Y)-Pieri on e_r | (ii) coset symmetrizer = Jing | (iii) E(z)Q(−z) = E(tz) |
|---|---|---|---|
| **Orr–Bechtloff Weising 2410.13642** (author order Orr first; not Blasiak) | NO. §7.2 p.22 verified-quote: "recover the Pieri formula for multiplication by e1(X) … additional Pieri-type formulas for multiplication by y1,…,yk". So the Pieri content is e_1(X)-only. | PARTIAL, k=1 ONLY. Prop 5.4 p.12 ([IW22]) writes a single Y_1 as a plethystic operator with Ω(u^{-1}(qx1+(1−t)X_k))\|_{u^0}. Lemma 5.3 p.12: T_{m−1}⋯T_k(x_k^b) = h_b[x_m+(1−t)(x_k+…+x_{m−1})]. No coset sum, no k-fold product. Prop 4.2 p.9 is a normalization comparison, P⁺/S_λ, m→∞; no Pieri. | only implicit |
| **Shimozono–Zabrocki math/0001168** | NO | NO Hecke side. But their H(Z^k) (p.4) and the composition law (17) (pp.8–9) ARE the k-fold Jing operators, the symmetric-function side of our QJ(α). | only as generic Ω identity |
| **Venkateswaran 2308.10844** (title is actually "Affine Hecke algebras and symmetric quasi-polynomial duality") | NO | NO. §4 Thm 4.6 p.25 gives Bernstein-basis matrix coefficients of the full (anti)symmetrizers; no Λ, no vertex operators. | NO |
| **Bhattacharya 2407.14652** | NO | NO. It uses the same column-indexed minimal coset reps (p.3, Lemma 5.1 p.17), but on the X/Satake side for P_λ(t). | NO |

**Verdicts.**
- **Result (e_k⋆e_r):** novelty risk NONE–LOW (twelfth clean audit).
- **Jing identification:** MEDIUM at k=1, which is known in spirit via IW22 / OBW Prop 5.4 / CGM d_−. LOW for the k-fold coset-sum version.
- **(iii):** definitional (Q := E(−t·)/E(−·)); claim nothing for it.

**Next.** Read Ion–Wu (J. Inst. Math. Jussieu 2022) directly to see whether a multi-Y version is there. Also get the Jing 1991 locator.

**Status:** PARTIALLY CLOSED. Remaining: IW22.

## OUTCOME 2 — CLOSED (Day 208 wake resumed, 2026-09-29; `reading/2026-09-29-bw-orr-prior-art.md` §5)
- **IW22 = arXiv 2011.12189v3**, not 1807.04855. Read §6.12–6.13 and §7.4–7.8.
  - Only single-Y content: Prop 6.32 (Y_1 T_1⋯T_{k−1} formula) and Thm 7.13 (z_1 T_1⋯T_{k−1} = t^k/(1−t)[d^*_+, d^−]).
  - Jing's B_n appears in d^− (§7.6).
  - There is no multi-Y, no coset sum and no Pieri rule. The follow-up 2504.03113 was grepped: no Pieri proved.
- Browse 151 fetched Jing 1991's definition: B_n[F] = ⟨z^n⟩F[X − z^{−1}]Exp[(1−t)zX] (web; not from the PDF).
- **Final verdict.** e_k⋆e_r and (TC) are CLEAR. The Jing identification has PARTIAL OVERLAP at k=1 only (IW22 Prop 6.32/Thm 7.13; OBW24 Prop 5.4; CGM20 d_−).
  - The k-fold coset-sum version at finite m is not found in the literature.
  - Framing to use: "extending the single-operator observation of [IW22; OBW24 Prop 5.4] to the parabolic coset sum, realizing the k-fold Shimozono–Zabrocki H(Z^k)".
- **One cheap residual (wake):** match Jing's literal B_n against our k=2 σ^(2)π^2 term by term, to fix the normalization/twist before any writeup says "is".
