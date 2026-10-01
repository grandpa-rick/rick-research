# Theorem H novelty audit — 2026-10-01

Claim: s→0 (q→∞) limit of Hikita ⋆ (2503.23597) in basis b_μ = s^{n(μ)} e_μ is HL multiplication:
φ∘L_k = t^{-C(k,2)} e_k∘φ, φ(b_μ)=t^{-n(μ')}P_{μ'}(x;t^{-1}). Corollary d_{λμ}(t)=t^{-n(λ')}⟨e_λ,H̃_{μ'}(x;t)⟩.

Notes appended per source below.

## 1. Hikita 2503.23597 (only v1, 30 Mar 2025; text /tmp/hikita.txt)
Lemma 6.3 (p.28, §6.3) verbatim: "For any partition λ = (λ1,...,λl), we have lim_{q→∞} e^{(q,t)}_λ(X) = [n]_t! / ∏_{i=1}^l [λ_i]_t! · e_n(X)." Proof: "By Theorem 3.12, we obtain lim_{q→∞} e_1(X)^{⋆r} = e_r(X)/[r]_t!."
Theorem C(ii) restates this; intro remarks the Pieri formula "e1(X) ⋆ er(X) = (1 − q^{-1})[r+1]_t e_{r+1}(X) + q^{-1} e1(X)er(X)" and "It seems likely that similar Pieri type formula exists for more general quantum multiplication of er(X) and Schur functions, but we do not pursue this direction here."
=> Hikita's q=∞ limit is the UNRESCALED one: everything collapses onto the line Q(t)·e_n (t-multinomial). No rescaled basis s^{n(μ)}e_μ, no Hall–Littlewood, no Kostka–Foulkes anywhere in the text (grep: only "Hall" hit is the Macdonald book title in refs). Theorem H's limit lives in the leading-order coefficients after rescaling — strictly finer information, invisible in Lemma 6.3. NOT prior art; Lemma 6.3 is recoverable from Theorem H only as the coarse "top-degree" shadow (should double-check consistency: d_{λ,(n)}... the (1^n)-direction coefficient).

## 2. Bechtloff Weising corpus (14 arXiv papers listed via API; 10 full texts grepped, /tmp/aud/*.txt)
Grepped for hall-littlewood / q→∞ / q→0 / q=0 / Kostka-Foulkes / cocharge / Pieri.
- 2410.13642 (BW–Orr, parabolic flag Hilb): no HL, no q-limits. §7.2 "Pieri formulas" only: "our Theorem 6.12 enables one to recover the Pieri formula for multiplication by e1(X) on partially-symmetric Macdonald polynomials which was proved in [Goo23]..." — e_1 ordinary multiplication on Macdonald side, not a deformed product, no limit.
- 2310.10249 / 2405.00756 (Murnaghan-type EHA reps): Pieri rule Cor 5.4 for e_r[X]• on generalized Macdonald fns P_T; the only q→∞ / q→0 occurrences (2405.00756 pp.~40, ~48) are eigenvalue/weight arguments (q→0 to compare diagonal contents; q→∞ in an inversion-product). Not a product degeneration.
- 2307.05864 / 2302.08211 (stable-limit nonsym Macdonald): HL appears only as a basis (Jing creation ops B_n; expansions "in the Hall-Littlewood basis P_λ"), and eq.(6) "ε^{(n)}(x^λ) = [n−k]_t!/[n]_t! v_λ(t) P_λ[x1+...+xn;t]" (t-symmetrizer of monomial = HL P, Macdonald III). That is the classical symmetrizer fact, not a q→∞ product limit. Relevant only as the standard ingredient Theorem H's proof also uses (HL as t-symmetrization).
- 2508.00336 (saturation): q=0 specialization of Dyck-path quasisymmetric Φ_δ — unrelated.
- 2502.10965, 2512.01835, 2402.02843, 2405.09846: no hits.
Verdict for BW: nothing equivalent.

## 3. González–Gorsky–Simental 2502.16113 (EHA ⊂ double Dyck path algebra), v1
§1.3 "Future Directions" lists 8 questions (lifting calibrated reps of B_{q,t}; Dyck-path elements of E_{q,t}; Blasiak et al. elements; other Dynkin types; faithfulness; integral form; SL2(Z)). Grep of the full text for hall-littlewood / q→∞ / q→0 / q=0 / Kostka / cocharge: ZERO hits. No HL limit anywhere. Not prior art. (Note: the "Open Problem 4" referenced in Browse 153 is item (4) here: Blasiak et al. elements Y_{m1..mn}; unrelated to q→∞.)

## 4a. Orr–Shimozono 1310.0279v2 "Specializations of nonsymmetric Macdonald–Koornwinder polynomials"
Intro p.2 verbatim: "At q → ∞, the Eλ(X;∞;t) for untwisted affine root systems are the p-adic Iwahori-Whittaker functions of Brubaker, Bump, and Licata [1]. ... We also consider the limit q → 0 ... Pλ(X;0;t) is the spherical function known as the Hall-Littlewood polynomial". §6.2 Theorem 6.2 = alcove-path formula for E_λ(X;∞;v^{-1}). Remark 5.6: "P_λ(X;q;v) = P_λ(X;q^{-1};v^{-1}) [25,(5.3.2)]. Hence the specializations of P_λ at v=0 and v=∞ (resp. q=0 and q=∞) are identical, up to the substitution q↦q^{-1} (resp. v↦v^{-1})."
Grep for product / multiplication / Pieri: no product-structure statements; everything is about individual polynomials E_λ, P_λ. NOT the ⋆-product limit. Relevance: Remark 5.6 is the polynomial-level reason one expects HL with t^{-1} at q=∞ (cf. φ(b_μ) = t^{-n(μ')}P_{μ'}(x;t^{-1}) in Theorem H) — this is the "folklore shadow", but it concerns Macdonald P_λ, whereas Hikita's ⋆ is transported from Y-multiplication via Ψ_q(F) = F(Y)•1 in the LEVEL-ONE rep (Hikita Thm B), and e_λ^⋆ are not Macdonald polynomials. The identification of the rescaled q=∞ limit of Ψ_q(e_μ(Y)) with HL P_{μ'} is not stated here.

## 5a. arXiv API keyword searches
- abs/all "Hall-Littlewood" AND "level one": 0 hits. "Hall-Littlewood" AND "q to infinity": 0 hits. "quantum multiplication" AND chromatic: 0. "Hall-Littlewood" AND "affine Hecke" AND "polynomial representation": 0.
- "(q,t)-chromatic" / Hikita+chromatic: surfaced 2504.06936, 2609.33124, 2509.02841, 2504.09123, 2509.22946 (checked below).

## 6a. Griffin–Mellit–Romero–Weigl–Wen 2504.06936v1 "On Macdonald expansions of q-chromatic symmetric functions and the Stanley–Stembridge conjecture" — CLOSEST RELATIVE FOUND
Abstract verbatim: "Using the A_{q,t} algebra, we give an expansion of these q-chromatic symmetric functions into Macdonald polynomials. Upon setting t = 1, we obtain another proof of the Stanley–Stembridge conjecture and rederive Hikita's formula. Upon setting t = 0, we obtain an expansion into Hall–Littlewood symmetric functions."
§4 "A Hall–Littlewood expansion" verbatim: "Combining Equation (1) with [16, VI.8.4.ii], we find that H̃_λ[(q − 1)X; q, 0] = q^{|λ'|+n(λ')} J_{λ'}[X; 0, q^{-1}] = q^{|λ'|+n(λ')} Q_{λ'}[X; q^{-1}]."
Intro verbatim: "It would be interesting to see if there is any connection between this formula and the (q, t)-chromatic symmetric functions very recently defined by Hikita [15]."
Assessment: here (their q) = (Hikita's t) = chromatic parameter, and HL appears with INVERTED parameter and CONJUGATE index (Q_{λ'}[X;q^{-1}]) — same fingerprint as Theorem H's φ(b_μ)=t^{-n(μ')}P_{μ'}(x;t^{-1}). But: (i) it is an expansion of χ_e, not a statement about any deformed product; (ii) their degeneration is Macdonald t→0, not Hikita q→∞; (iii) they explicitly flag the link to Hikita's (q,t)-chromatic as OPEN. So PARTIAL-RELATIVE, not prior art. Action: Theorem H should cite this and probably say whether Theorem H + Hikita Thm B(iii) (X_Γ = Ψ_q(Y_Γ)) recovers/relates to GMRWW §4 at the rescaled q→∞ level — that would answer their open remark (bonus, not a threat).

## 6b. 2609.33124 (Vailaya, circular arc e-positive), 2509.02841 (Siegl, lower bounds e-basis): cite Hikita's SS paper (2410.12758) tableaux/probabilities only; no ⋆, no q→∞ product, no HL. Irrelevant.

## 4b. Cherednik–Orr 1302.4094v3 "Nonsymmetric difference Whittaker functions"
Abstract: spinor q-Whittaker functions, q-Toda-Dunkl operators as limits of difference Dunkl operators (Ruijsenaars procedure), nil-DAHA. Grep: no "Hall-Littlewood", no Pieri; "products" hits are all G-products / reduced words / inner products. No product-structure degeneration to HL multiplication. Not prior art.

## 4c. Macdonald book VI §8 — NOT read directly (no copy on disk). Known statement P_λ(x;0,t) = HL P_λ(x;t) is quoted second-hand: Orr–Shimozono p.2 ("Pλ(X;0;t) is the spherical function known as the Hall-Littlewood polynomial") and GMRWW §4 citing "[16, VI.8.4.ii]" for H̃_λ[(q−1)X;q,0] = q^{|λ'|+n(λ')} Q_{λ'}[X;q^{-1}]. These are polynomial-level facts about Macdonald P/H̃, not about Hikita's ⋆.

## 5b. Kirillov math/9803006v4 "New combinatorial formula for modified Hall-Littlewood polynomials" (Contemp. Math. 254, 2000) — THE COROLLARY'S OBJECT IS CLASSICAL
§3.2 "New combinatorial formula for the transition matrix M(e,P)" verbatim: "R_{λμ}(t) = Σ_η K_{ημ} K_{η'λ}(t). This sum is the (λ,μ)-entry of the matrix transposed to the transition matrix between elementary and Hall–Littlewood polynomials, namely, if e_λ = Σ_μ M(e,P)_{λμ} P_μ, then M(e,P)_{λμ} = Σ_ν K_{νλ} K_{ν'μ}(q) = R_{μλ}(q). It is well-known ([Kn]) that R_{λμ}(1) counts the number of (0,1)-matrices with row sums λ_i and column sums μ_j." Theorem 3.4 ([HKKOTY]) gives a fermionic formula for R_{λμ}(t); abstract also mentions a "dual mahonian statistic on the set of transport (0,1)-matrices".
=> The Corollary of Theorem H (d_{λμ}(t) = t^{-n(λ')}⟨e_λ,H̃_{μ'}(x;t)⟩ ∈ ℕ[t], d(1) = #0-1 matrices) identifies d with (a normalization/t↦t^{-1} variant of) the classical e→HL transition matrix M(e,P) = R^T. That object, its positivity, and d(1) = 0-1 matrix count are KNOWN (Kirillov §3.2 + Knuth). Rick must present the corollary as "d equals the known e-to-HL transition matrix" and cite Kirillov §3.2 / HKKOTY Thm, not as a new positivity/counting result. Exact normalization match (t vs t^{-1}, P vs Q', μ vs μ') NOT verified here — do the sober check before citing.

## 6c. Forward citations of 2503.23597
Semantic Scholar (35s, returned): only 3 — 2601.23170 (Colmenarejo et al., total chromatic quasisym; grep: no HL / q→∞), 2410.12758 (Hikita SS proof), 2410.12231. S2 is INCOMPLETE (misses GMRWW 2504.06936, which cites [15]=2503.23597). Google Scholar not tried. Local cached papers 2504.09123, 2508.19704, 2608.14836, 2608.30791, 2609.10284, 2604.25440 grepped: HL appears only in unrelated roles (Catalanimals, HL Cauchy, LLT), no ⋆ q→∞ limit.

## VERDICT: NOVEL-AS-FAR-AS-CHECKED for the product-level statement (Theorem H: rescaled q→∞ limit of Hikita ⋆ = HL multiplication via φ(b_μ)=t^{-n(μ')}P_{μ'}(x;t^{-1})); PARTIALLY-KNOWN for the Corollary's object.
- Hikita's own q=∞ result (Lemma 6.3 / Thm C(ii), p.28) is the unrescaled collapse onto e_n — strictly coarser; no HL.
- Closest relative: GMRWW 2504.06936 §4 (HL Q_{λ'}[X;q^{-1}] at Macdonald t=0 for q-chromatic; flags link to Hikita's (q,t)-chromatic as open). Cite it; possibly Theorem H answers their remark.
- Corollary d_{λμ}: classical e→HL transition matrix, Kirillov math/9803006 §3.2 + Thm 3.4 [HKKOTY], t=1 count [Knuth]. Downgrade the corollary to "identification with known object".
- Folklore risk remains moderate: the t↦t^{-1}/conjugate-index fingerprint is the polynomial-level shadow (Orr–Shimozono Remark 5.6; Macdonald VI.8.4). An expert (Orr, Mellit, Hikita) might consider the product statement "expected"; no written statement found.
NOT CHECKED: Macdonald book text directly; Google Scholar forward cites; Ion's q→∞/nonsymmetric HL papers; Garsia–Haiman / Haglund e_k Pieri at q=0 (only keyword searched, 0 hits); Blasiak et al. EHA papers; HKKOTY original; any non-arXiv literature.
Addendum: Hikita 2410.12758 (SS proof) grepped — no q→∞, no HL (only a Lascoux–Leclerc–Thibon ref title), Kostka numbers only. Clean.
