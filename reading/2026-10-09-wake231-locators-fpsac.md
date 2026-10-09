# Wake 231 — first-hand locator audit of FPSAC draft + FPSAC 2027 rules + Penrose 1967

Date: 2026-10-09. Draft: work-in-progress/fpsac2027/fpsac2027-draft.tex @ 3f7d825.
PDFs fetched from arXiv (latest versions: Hikita 2503.23597v1; DFK 1505.01657v2; DFK 1704.00154v2;
Dołęga 1707.02656v2; Haglund–Tewari 2609.29957v1; Jing–Liu 2104.04411v2; Kirillov math/9803006v4),
pdftotext -layout. DLT94 from SLC (s32leclerc.pdf). Macdonald95 (book) NOT checked here.

## Locator table

| line | citation | claimed locator | verified? | evidence (≤2 lines) | fix |
|---|---|---|---|---|---|
| 73 | Hikita25 | Lemma 3.1, Cor 3.9 (q iso, compatible m→m−1) | OK | L3.1 "The map q(m) is an isomorphism as Q_{q,t}-vector spaces"; C3.9 "q(m′)(π_{m,m′}(F(Y))) = π_{m,m′}(q(m)(F(Y))) ... well-defined Q_{q,t}-linear isomorphism q" | none |
| 73 | Hikita25 | Def 3.4, Lemma 3.2, Cor 3.10 (⋆ defined, restricts to Λ) | OK | D3.4 "F⋆G := q(q⁻¹(F)·q⁻¹(G))"; L3.2 F(Y) symmetric iff q(F) symmetric; C3.10 "well-defined multiplication ⋆ on Q_{q,t}[X](∞) and Λ_{q,t}" | none |
| 73,256 | Hikita25 | Thm 3.12 Pieri | OK | "e1(X)⋆er(X) = (1−q⁻¹)[r+1]_t e_{r+1}(X) + q⁻¹ e1(X)er(X)" — matches with s=q⁻¹ | none |
| 81 | Hikita25 | Def 3.4, Lemma 3.3 (e_k⋆F = t^{-C(k,2)} e_k(Y)•F) | OK | after D3.4: "F⋆G = ... = q⁻¹(F)•G"; L3.3 "q(m)(e_r(Y)) = t^{r(r−1)/2} e_r(X)" | (the •-form is an unnumbered display right after Def 3.4 — fine) |
| 100 | Hikita25 | Lemma 6.3 (q→∞ degeneration) | OK | "lim_{q→∞} e_λ^{(q,t)}(X) = [n]_t!/∏[λ_i]_t! · e_n(X)" | none. Aside: Hikita's proof line "lim e1^{⋆r} = e_r/[r]_t!" looks inverted vs Thm 3.12 (gives [r]! e_r) — Hikita typo, not ours |
| 241 | Hikita25 | Prop 3.8, Cor 3.10 (stability) | OK | P3.8 "π_{m,m′}(F(Y)•G(X)) = π_{m,m′}(F(Y))•π_{m,m′}(G(X))" | none |
| 143 | DFK18 (=1505.01657) | eq (5.15), Cor 5.8, (5.25), Cor 5.18 (5.27), "numbering of v2" | OK (v2) | (5.15) "M_{α,n} = Σ_{|I|=α}(z_I)^n a_I(z) Γ_I"; (5.25) level-1 form "of Corollary 5.8"; C5.18 "χ_n(q⁻¹,z) = lim_{t→∞}P^{q,t}_λ(z) = P^{q⁻¹,0}_λ(z)" (5.27) | none. v1 numbering is DIFFERENT ((5.15),(5.25),(5.27) are unrelated eqs in v1) — keep "v2" qualifier; published Transform. Groups numbering not checked. "M_{k,1}=E_k|_{t=0}" is our identification, not stated by DFK |
| 241 | DFK19 (=1704.00154) | Rem 3.3 (SΓ_IS=Γ_I⁻¹, x↦x⁻¹) | OK | "if S denotes the involution ... x_i ↦ x_i⁻¹ ... then we have SΓ_I S = Γ_I⁻¹ and D^{q⁻¹,t⁻¹}_{α;−n} = S D^{q,t}_{α;n} S" | none |
| 53 | DFK19 | (no locator) "lose Schur positivity at generic t" | OK | §8.3: "M2·1 = t^{N−1}s2 − t^{N−2}s11, so Schur positivity is lost" | optional: add [§8.3] |
| 197 | Dolega19 (1707.02656v2) | Prop 2.1 and (11), Lemma 2.3 | OK | P2.1 = tree form (κ(T)=0 trees, [δ_T(w)]_q); (11) "c_G(q) := q^{#V−1}Tutte_G(1,q+1) = Σ_{H conn} q^{#E(H)}"; L2.3 "Tutte_G(1,q) = (q−1)^{1−#V} Σ_π (−1)^{#π−1}(#π−1)! ∏ q^{#E|B}" | none (note (11) sits inside the proof of Prop 2.1) |
| 197 | HaglundTewari26 (2609.29957v1) | Def 7.1, Thm 7.3 single-row cumulant | OK, notation | D7.1 "κ(a) := Σ_σ μ(σ,1̂)∏ h̃_{a(B)}, normalized κ := (q−1)^{1−r}κ"; T7.3 "(q^k−1)D_k κ(a1..ar) = κ(a1..ar,k)" | HT call it κ(a), not C_λ — say "their cumulant κ(λ) (we write C_λ)" or rename. The ⟨C_λ,e_n⟩ identity itself not checked here |
| 100–102 | Kirillov98 (math/9803006v4) | §3.2 e→HL matrix, positivity, d(1)=#0-1 matrices | OK | "if e_λ = Σ M(e,P)_{λμ}P_μ, then M(e,P)_{λμ} = Σ_ν K_{νλ}K_{ν′μ}(q) = R_{μλ}(q)"; "R_{λμ}(1) counts the number of (0,1)-matrices with row sums λ_i and column sums μ_j" | none (positivity is implicit via K-F ≥ 0 / fermionic (3.7), not stated as a sentence) |
| 146 | DLT94 | eq (11) | OK | "Q′_λ(X;q) := ∏_{i<j}(1−qR_ij)^{-1} s_λ(X)  (11)" | none |
| 294 | JingLiu21 (2104.04411v2) | (2.17), (2.20) | OK | (2.17) "H_{λ1}···H_{λl}.1 = Q_λ(t) = ∏(1−R_ij)/(1−tR_ij) q_λ"; (2.20) "X^λ_μ(t) = ⟨H_λ.1, p_μ⟩" | none |
| 294 | JingLiu21 | Thm 2.7 nested sum, all μ | OK | "X^λ_μ(t) = Σ_{{ρ^i},{τ^i}} ∏_{j=1}^{l(λ)−1} (−1)^{l(ρ^(j))}/z_{ρ^(j)}(t)" (2.33) | none |
| 294 | JingLiu21 | Thm 2.10, (2.37)–(2.40) restrict HL index λ | OK | superscripts (n−k,k), (k,1^{n−k}), (k1,k2,k3), (h1,h2,1^{n−h1−h2}) = HL index (p_μ = Σ X^λ_μ P_λ, (2.19)) | none |
| 294 fn | JingLiu21 | p.12, before Thm 3.2 (Morris scope) | LOCATOR OK, gloss imprecise | p.12: "The following is a Murnaghan-Nakayama rule for the Green polynomial. The result generalizes a formula of Morris [12] which corresponds to our result in the case of l(λ) = 2." [12] = LNM 579 pp.136–154 (1977) = our Morris77 | JL attribute to Morris the ℓ(λ)=2 case of their MN rule Thm 3.2, NOT of the closed forms Thm 2.10. Main text "the case ℓ(λ)=2 goes back to Morris" right after Thm 2.10 reads as if Morris = (2.37). Suggest: "an ℓ(λ)=2 Murnaghan–Nakayama-type formula goes back to Morris" |

## FPSAC 2027 (source: maths.universityofgalway.ie/fpsac2027/, "Last update 29/09/2026")

important_dates/ (timeline JS array in raw HTML):
- `date: [2026, 10, 1], event: 'Paper/poster/software submissions open'`
- `date: [2026, 11, 15], event: 'Deadline for paper/poster/software submissions'`
- decisions 2027-02-15; final version 2027-04-01; conference 2027-07-05.
- No time-of-day/time zone stated (the only time string on the page is stale "March 15, 2024 at 6 PM CET" template cruft; landing page "November 15, 2023" is inside an HTML comment).

submissions/:
- "All submissions must use 12pt font ... and be 6-12 pages in length, including the bibliography but excluding the AI declaration section."
- "Submitted extended abstracts must have between 6 and 12 pages. In addition, they must be accompanied by a detailed AI declaration section, which has no length limit and does not count toward the 12-page limit."
- "At the end of the extended abstract, authors are required to include a statement describing their use of AI tools ... exploration, brainstorming, coding, computation, mathematical reasoning, proving, writing, generating figures, proofreading ..."
- "Include your AI declaration ... at the end of the document, in the designated section of sample.tex."
- Final version: separate .bib, biblatex.

Draft status: PDF 14 pp = 12 pp body+refs (refs end p.12) + AI section pp.13–14 → compliant. Section titled "AI disclosure"; site calls it "AI declaration" — consider matching sample.tex's section name.

## Penrose 1967

- Sokal, cond-mat/0309352 (Scott–Sokal) ref [88]: "O. Penrose, Convergence of fugacity expansions for classical systems, in T.A. Bak (editor), Statistical Mechanics: Foundations and Applications, pp. 101–109 (Benjamin, New York–Amsterdam, 1967)."
- Sokal, cond-mat/9904146 ref [79]: identical, "pp. 101–109. Benjamin, New York–Amsterdam."
- Procacci–Yuhjtman 1508.07379 [16], Fernández–Procacci math-ph/0605041 [14], Morais–Procacci 1301.0107 [30]: same title, no pages.
- Open Library: volume "Statistical mechanics: foundations and applications", W. A. Benjamin, 582 p., LCCN 67028999 (proceedings of the IUPAP meeting, Copenhagen 1966).
- No TOC found first-hand; pages 101–109 rest on two Sokal bibliographies (same author line, so one source effectively).
- Fix: add `pages = {101--109}` to Penrose67; title confirmed by 5 independent bibliographies.
