# Day 238 PROVE (A) — novelty-claim consistency cold read of the long version vs §6 DFK credit

Date: 2026-10-13 (file dated 10-14 per PROVE.md naming). Long version before: WIP b2b5410 (37 pp). After: WIP **33526fc** (38 pp, 0 overfull by `grep -a -c Overfull longversion.log`, 0 undefined).
FPSAC (frozen 7df658b) NOT touched.

## Problem
Every novelty-bearing sentence of the abstract, §1, §§2–5, 7–10 (+ App A), checked against §6 (DFK-credited (N)) and the
registry `novelty*` fields. Verdict per sentence: KEEP / SOFTEN / CREDIT, with owner + literal locator read first-hand.

## First-hand readings this session
- **DFK19 = arXiv 1704.00154** (`/tmp/loc/1704.00154.txt`): (1.5) M_{α;n}; Def 2.6 Y_{i,n}=(X_1⋯X_{i−1})^{−n}Y_i(X_1⋯X_i)^n;
  Thm 2.17 (2.11)–(2.12): ρ(D_{α;n})|_{S_N}=θ^{−α(N−α)}M_{α;n}, proof = X-Gaussian conjugation of Macdonald Thm 2.5. Grep of the whole text:
  limits are only t→∞ (§§4.3, 7, 8.3) and N→∞ (§4.2); "Hall" occurs only as "Elliptic Hall"/Hall algebra; **no Hall–Littlewood, no q→0**.
  §8.3 (l.3189–3197): loss of Schur positivity for the t-deformed M_2·1 — intro sentence verified.
- **Kirillov98 = math/9803006** (`/tmp/loc/math_9803006.txt`): §3.2 l.1365–1398: M(e,P)_{λμ}=Σ_ν K_{νλ}K_{ν′μ}(q)=R_{μλ}(q);
  "It is well-known ([Kn]) that R_{λμ}(1) counts (0,1)-matrices"; Thm 3.4 ([HKKOTY]) fermionic formula. §4.1 l.1491–1530: proof iterates
  Macdonald III (3.2) (f^λ_{μ(1^m)}=∏ Gaussian binomials).
- **Hikita25 = 2503.23597** (`/tmp/loc/2503.23597.txt`): Thm C(ii) (l.278–288) = Lemma 6.3 (l.1698–1707):
  lim_{q→∞} e_λ^{(q,t)} = [n]_t!/∏[λ_i]_t! · e_n, proved from Thm 3.12 (e_1 Pieri). Hikita never mentions DFK.

## Verdict table

| # | Location | Sentence (short) | Verdict | Action |
|---|----------|------------------|---------|--------|
| 1 | Abstract | explicit rule for e_k⋆(e_{a_1}⋯e_{a_ℓ}); ℓ=1 Pieri generalising Hikita's e_1⋆e_r | KEEP | Hikita has only k=1 (Thm 3.12) |
| 2 | Abstract | c_{λμ} supported exactly on dominance up-set, s-valuation n(μ) | KEEP | Hikita C(ii) is one coefficient of the s→0 corner, now credited at Rem 5.6 |
| 3 | Abstract | (s−1)-valuation ℓ−κ | KEEP | Rem 7.x novelty already credits DLT94 for t=0 substance |
| 4 | Abstract | leads factor over blocks; full merge = connected-graph cumulant | KEEP | no claim on graph half; intro + Rem 8.x credit Dołęga/Gessel–Sagan/Penrose/HT |
| 5 | Abstract | box-complement invariance | KEEP | Rem 9.x credits DFK19 Rem 3.3 mechanism + Hikita stability |
| 6 | Abstract | v=2 leads closed form via residue formula for two-part Green polys | KEEP | Rem (Green) credits Jing91, JingLiu21, Morris77 (footnote: not seen first-hand) |
| 7 | Abstract | self-contained proof of N-transport, "implicit in DFK" | KEEP | consistent with §6 |
| 8 | §1 ¶1 | DFK19 §8.3 loss of Schur positivity | KEEP | verified first-hand l.3189–3197 |
| 9 | §1 Pieri | e_k⋆(·) is a sum over k-subsets (Thm 2.5) | **CREDIT** | added "up to normalisation it is M_{k;1} of DFK (Rem 2.6)" |
| 10 | §1 Pieri | ℓ-column generating function, t=0 geometric | KEEP | — |
| 11 | §1 DS | s-leading coeffs = classical e→HL matrix | KEEP | says "classical" |
| 12 | §1 block law / G / box / v2 | — | KEEP | Dołęga credit present |
| 13 | §1 transport | "implicit in DFK19, no novelty" | KEEP | — |
| 14 | Rem 2.6 (subset) | Prop Kk = level-one Hecke symmetriser | **CREDIT** | new ¶: E_k=t^{k(m−k)}M_{k;1}; DFK19 Def 2.6, Thm 2.17 obtain M_{k;n} as e_k(Y_{i,n})|_Sym by X-Gaussian conjugation; Thm 2.5 = n=1 analogue for Hikita's level-one Y (x-twisted, π=x_1π_∘); conventions NOT matched symbol by symbol; our proof direct, no commutativity |
| 15 | Rem 5.6 (H) | "positivity and t=1 in Kirillov §3.2"; "new = Thm H"; "Hikita L6.3 treats unrescaled limit" | **CREDIT + SOFTEN** | Kirillov §3.2/Thm 3.4/§4.1 now credited for the factorisation, positivity, Knuth's t=1 count, and the Pieri-iteration proof; Thm H "could also be reached from Thm 6.2 (DFK-implicit) by Rem 6.5 limit argument (not developed)"; DFK19 only t→∞, N→∞, no HL; Hikita L6.3 = Thm C(ii) = the corner μ=(n) of Cor 5.2 |
| 16 | Rem 5.7 (edges) | edges via 𝒩, implicit in DFK19 | KEEP | no claim made. Note (not in paper): t→∞ edge = H′, scooped in substance by DFK15/1908.00806 per registry; dictionary unverified, so no locator added |
| 17 | §6 intro, Rem 6.3–6.5 | — | KEEP | Day 237 print-checked |
| 18 | Rem 7.x (t=0 input) | "not ours", DFK18 locators | KEEP | — |
| 19 | Rem 7.x (block law novelty) | new = lower bound all t, exactness over Q(t), merge weights | KEEP | statements not in DFK; t=0 input credited |
| 20 | Rem (linT) | "probably known" | KEEP | — |
| 21 | Rem 8.x (graph half) | Dołęga/HT/Penrose | KEEP | — |
| 22 | Rem 9.x (box prior art) | "not found for ⋆" | KEEP | — |
| 23 | §10 Rem Green, Ex tworow | "This is not new: Jing–Liu" | KEEP | — |
| 24 | App A | "textbook, nothing new" | KEEP | — |

Cor dmatrix specifically: the text now neither over-claims (the factorisation e→P = Kostka·Kostka–Foulkes is Kirillov's §3.2 display,
credited) nor under-claims (WZJ 1603.01815 stays out — declined Wake 238, they treat P→s inverse Kostka). Macdonald III (3.2) is cited as
the shared engine of both Kirillov's Thm 3.4 proof and our Thm H(3).

## Verification
`work-in-progress/scripts/day238/remH_print_check.py`, from the printed statements, using explicit HL polynomials (Macdonald III (2.2))
in n variables, n ≤ 4: (a) M(e,P)_{λκ}(t)=Σ_ν K_{νλ}K_{ν′κ}(t); (b) Cor 5.2 first formula = second formula, d(1)=#0-1 matrices;
(c) d_{λ,(n)}=[n]_t!/∏[λ_i]_t!. **ALL OK.** Controls (`remH_controls.py`): drop the conjugate in (a) → breaks 28×; t^{−1}-factorials in (c) → breaks 7×.
Rebuilt PDF read via pdftotext: Rem 2.6, Rem 5.6, intro ¶ print as intended.

## Gaps / not done
- Hikita level-one Y_i vs DFK Y_{i,1}: exact convention match not done (the paper now says so). If a referee wants "is" instead of "analogue", that check is owed.
- FPSAC (frozen) still: (i) lacks the DFK19 Thm 2.17 credit for E_k; (ii) intro l.55 "Hikita's formula for e_k⋆(·) as a sum over k-subsets"
  can be read as attributing the subset formula to Hikita (Hikita has only k=1); (iii) Rem H lacks the Kirillov/Hikita-corner credits. → for-collaborator note.

## (B) Coproduct test — appended
Done, WIP e5ab30e. Verdict CONFIRMED-DEFLATED (classical): Δ_𝒩 at t→∞ = row-additive splits; coboundary g(ν)=s^{n(ν′)}/∏[m_i(ν′)]_s! gives Sym's Δ on m_{ν′}.
Controls break. Full record: memory/connections/2026-10-11-nabla-gauge-transports-the-coproduct.md (Day 238 section). No registry node.
