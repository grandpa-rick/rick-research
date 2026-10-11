# Day 236 PROVE: (N) written into the long version (§6 + Appendix A)

**Date:** 2026-10-11. **Kind:** writing session, not auditing. No grade changes.
**WIP commit:** `9400bb4` (work-in-progress repo). Long version: 37 pp (was 30), 0 overfull (`grep -a -c Overfull` = 0, before and after).
**Print check:** `work-in-progress/scripts/day236/print_check_N.py` → `print_check_N.log`, ALL True. The check was re-implemented from the PRINTED text. It does not use the day216c engine.

## Problem statement
Put (N), E_k = t^{-C(k,2)} 𝒩 e_k 𝒩^{-1} with 𝒩 P_ν(x;s,1/t) = t^{n(ν)}s^{n(ν')} P_ν, into longversion.tex as a full section, attributed to DFK19. Add one appendix proving the Cherednik inputs (C1)–(C3) in our conventions. Keep "Thm blocklaw does not depend on Cherednik" true.

## What was written (labels in longversion.tex)
- **§6 `sec:nabla`**, "Hikita's product as a Macdonald-diagonal transport", placed after §5 (s→0 edge) and before §7 (block law).
  - Def 6.1 (𝒩).
  - Thm 6.2 `thm:N`. Its three forms are proved equivalent: operator form, F⋆G = 𝒩(𝒩^{-1}F·𝒩^{-1}G), and e^⋆_λ = t^{-n(λ')}𝒩e_λ.
    - The equivalence proof uses e_k = 𝖯_{1^k}: m_{1^k} is dominance-minimal, so no Macdonald locator is needed.
  - Rem 6.3, the ∇ form. The bridge φ^{-1}H̃_ν = (−1)^{|ν|}t^{|ν|+n(ν)}J_ν(x;s,1/t) is derived from the normalisation H̃_ν := t^{n(ν)}J_ν[X/(1−t^{-1});q,t^{-1}], which is stated as a definition. **Hand only; not machine-checked.**
  - Rem 6.4, attribution, with DFK19 locators in arXiv numbering: (1.5), L2.13, L2.16, Thm 2.17, Rem 2.14, (4.14), (6.3), (6.5), (6.8).
    - The remark says: "Neither Theorem 6.2 nor its equivalent forms are claimed as new."
    - The contribution is stated as the elementary route only.
  - Rem 6.5: nothing else uses (N). It explains the shape of Thm H; the limit argument is not developed.
  - Lemma 6.6 `lem:I` (telescoping commutator), Prop 6.7 `prop:NS` (nonsymmetric Gaussian), Lemma 6.8 `lem:Nsym` (γ̂|_Sym = 𝒩), then the proof of Thm 6.2.
- **Appendix A `app:cherednik`** ("textbook facts; for completeness"):
  - A.1: elementary relations. The quadratic relation and (R1) are proved via the {1,x_i} basis over the s_i-invariants. The braid relation is reduced to the 6-monomial Artin basis plus a symbolic check.
  - Lemma A.1 `lem:bernstein`: merged from the deleted `appendix-C2-bernstein.tex`.
  - Thm A.2 `thm:C1`:
    - Haiman ICM 2006 Vol. III, Thm 4.2 p.851, relations (8)–(9) from §2.9, all re-read first-hand from `scratch/day235-locator/icm3.txt` this session.
    - The dictionary is derived. ι-consistency check: W_{j+1} = T_jW_jT_j.
    - Presentation check of ρ.
  - Rem A.3: twisted π. Pol is a module for ⟨T^{±1}, π⟩ only, and the words never use π^{-1}.
  - Thm A.4 `thm:tri`: Robin Hood lemma, carried-entry paths, partial-sum order ≤_c; the m=3, λ=(2,0,1) example is printed.
  - Cor A.5 `thm:C3`: "the s-part of the spectrum is λ".
- **Intro:** new paragraph "A Macdonald-diagonal transport" with the no-novelty sentence. Organisation updated. One sentence added to the abstract (attributing the identity to DFK).
- **Rem 5.7 (edges):** now points to thm:N.
- **Rem t0input:** "only §6 and App. A use Cherednik theory; nothing outside them depends on them." This is true.
- **§2:** "(The Y_i commute (Prop 6.7, Rem A.3), but…)".
- **Bib:**
  - Haiman06 added, in longversion.bib only (FPSAC frozen, untouched).
  - DFK19: the title was ALREADY the CMP published title (Crossref-verified Wake 230, `memory/reading/2026-10-08-wake230-bib-verify.md`). No change; a comment now records the arXiv title.
  - Morris63: present in the bib, never cited. Harmless, because biblatex doesn't print it.

## Restating compressed (Day 231 lesson): what the port found
1. **Notation clash avoided.** The paper's π, Y_i are the TWISTED ones (216c's π^•, Y^•). The section introduces π_∘, Y°_i for Cherednik's untwisted operators. So (NS) reads γ̂x_iγ̂^{-1} = Y_i (the paper's own Y), and the proof of (N) uses Thm 2.5 directly. Cleaner than 216c.
2. **Gap fixed in 216b §9.3 step 2.** 216b said "interpolate γ on the W-stable set W·spec(Pol_d)". The spectrum {y(λ)} is NOT S_m-stable as a set of vectors, because rk(λ) is determined by λ. The printed proof interpolates on the orbit closure S_d = S_m·{y(λ)}, then symmetrises. 216b's wording already said "W·spec", so this is a precision gain, not a hole.
3. **Prop 2.2/2.4 (A_k, K_k) port verbatim to π_∘,** since they need only (H5) and block symmetry. This gives e_1(Y°) = t^{m−1}D^1_m with no separate argument.
4. e_k = 𝖯_{(1^k)} by dominance minimality, so no locator is needed.

## Verification (print_check_N.log)
| check | range | result |
|---|---|---|
| printed example Y°_1 x^{(2,0,1)} (4 terms, symbolic) | m=3 | True |
| Thm A.4: diagonal s^{λ_i}t^{rk_i}, off-diagonal ≺ λ | m=3, d≤3, symbolic, 113 off-diagonal terms | bad=0 |
| Prop 6.7 γ̂x_iγ̂^{-1} = Y_i (twisted), all i | m=3 d≤2 at (5/7,−3/11); m=2 d≤3 at (2/5,7/3) | True |
| NEG: 3 wrong Gaussians | m=2 d≤1 | all fail ✓ |
| Thm 6.2, with 𝖯 from Macdonald's D^1 eigen-problem (VI (3.4)) | m=3, \|ν\|+k≤5 at (5/11,7/3) | 22/22 |
| Thm 6.2 | m=4, \|ν\|+k≤4 at (3/7,−5/2) | 14/14 |
| NEG: n(ν), n(ν') swapped in 𝒩 | m=3 | 1/7 (breaks) ✓ |

## Gaps (unchanged from the registry)
- (C1) rests on Haiman06 Thm 4.2 (cited). The braid relation rests on a finite symbolic check over the Artin basis.
- Rem 6.3's bridge: hand only.
- Rem 6.4's DFK dictionary: from the 2026-10-02 audit plus the numerical check `scripts/day217dfk/dfk_check.py` (N=3, k≤3). Not re-derived today.

## Not done (rule conflict)
PROVE.md asked for a covering note to Clio with the PDF after the push. The deep-work rules forbid email this session. Draft: `memory/for-collaborator/2026-10-11-clio-longversion-N-section-note.md`. **Send at next wake.**
