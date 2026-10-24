# Q32 owner search — SR_LG / SR_OG / half-integer window (2026-10-24)

Literature sub-agent for Rick. Gate: write-up of (SR_LG) H_κ(−j) = (−1)^{|κ|} #{strict maps P_κ → [2j−1], diagonal values even}.

Sanity check done by hand (not a source): κ=(2,1) (full LG(2,4)), H(j)=dim V_{Sp4}(jω_2)=(j+1)(j+2)(2j+3)/6.
H(−1)=H(−2)=0, H(−3)=−1. SR_LG: chain of 3 boxes, strict into {1..5}, both ends (diagonal) even ⇒ only 2<3<4 ⇒ 1, sign (−1)^3. Matches.
Note: H_LG is NOT the order polynomial of P_κ (that would give C(j+3,3)), so Hibi/Stanley reciprocity does not apply directly to LG.

Search channels: WebSearch (standard + extended), arXiv API (abs: keyword queries incl. "Lagrangian Grassmannian"+Hilbert/Ehrhart/Gorenstein, Schubert+enriched, Schubert+"Hilbert polynomial", Ehrhart+"Schubert varieties", "symplectic Grassmannian"+Hilbert; author Chirivì), Semantic Scholar (mostly rate-limited after query 1), MathOverflow via api.stackexchange search/advanced + search/excerpts (4 queries; nothing relevant).

## Item 1 — Stembridge, Enriched P-partitions, TAMS 349 (1997) 763–788
Read first-hand (author's enriched.ps.gz from umich, converted).
- §4 "The enriched order polynomial". Verbatim: "In the theory of ordinary P-partitions, there is a Reciprocity Theorem ... In the enriched case, order polynomials enjoy self-reciprocity. Proposition 4.2. We have Ω′(P,γ)(t) = (−1)^n Ω′(P,γ)(−t); i.e., Ω′(P,γ)(t) is either an even or an odd function of t."
- Remark 4.7: enriched order polynomial of shifted diagram = Q_λ(1^m) (e.g. Q_3(1^m)=2m(2m²+1)/3).
- No Schubert varieties, no Grassmannians, no Hilbert functions (grep: 0 hits for schubert/grassmann/lagrang).
- Petersen math/0508041 Prop 4.4 adds left-enriched shifted self-reciprocity Ω^(ℓ)(P;−x−½)=(−1)^n Ω^(ℓ)(P;x−½); type B versions Prop 4.13. Also self-reciprocity only.
VERDICT: related, does not state. (Self-reciprocity of an enriched polynomial, not H(−j) = strict-diagonal-even count.)

## Item 2 — De Concini 1979 / SMT for LG / Hilbert function of LG Schubert / Gorenstein
- De Concini, "Symplectic standard tableaux", Adv. Math. 34 (1979) 1–27: NOT CHECKED first-hand (paywalled, not on arXiv). Known content: standard monomial (admissible-pair) basis — owns the POSITIVE side (H_κ(j) = standard monomial count), not reciprocity as far as known.
- Ghorpade–Raghavan math/0409338 (TAMS 358 (2006)): Hilbert function of the TANGENT CONE at a T-fixed point (local), not the projective Hilbert polynomial. Related, does not state. Same for Upadhyay–Ray 1903.11093 (bounded RSK), Ikeda–Naruse 1112.5223 (grep "Hilbert": only the GR citation).
- Chirivì, "LS algebras and application to Schubert varieties", Transform. Groups 5 (2000): NOT CHECKED first-hand; per abstracts: semi-toric degeneration of any Schubert variety to a union of normal toric varieties, LS-path (bond) basis — this is the framework in which the "LS parity" positive count lives.
- Chirivì 1809.10191 "On some properties of LS algebras": abstract — discrete LS algebra over a chain = invariant ring of finite abelian group; "used to study the Gorenstein property for LS algebras"; Koszul. Related, does not state.
- Chirivì–Fang–Littelmann 2112.03776 (Seshadri stratifications and SMT), Prop 13.8 (read): "If the Seshadri stratification is normal, then the Hilbert function H_R(t) ... is an alternating sum of Ehrhart quasi-polynomials. ... H_R(t) = Σ (−1)^{ℓ−1} Ehr_{Δ_{C_{i1}}∩...∩Δ_{C_{iℓ}}}(t)." No reciprocity / negative values (grep "reciproc": 0). Related, does not state; but it is the natural machinery a referee might point to.
- **Chirivì–Costa Cesari–Fang–Littelmann 2609.03195 "Lecture hall polytopes and Lakshmibai–Seshadri paths" (2026-09-02) — NEW, closest neighbour.** Read first-hand. LS paths with bonds b ↔ lattice points of b-lecture hall polytopes; components of the semi-toric degeneration of X_w (one per maximal chain, bonds b_j=⟨w_j(λ),β_j^∨⟩) are LH-toric varieties (§7). Thm 5.2 Gorenstein criterion; Cor 5.4 verbatim: "If A(b) is Gorenstein then Π°(b) = π⁰ + Π(b), where π⁰=(1/N_1,…,1/N_{n+1}) is the unique L-S path of minimal degree in Π°(b)" (Π° = LS paths with all a_j>0 = interior). Per-component (per maximal chain) interior-point statements only; nothing on χ(X_w,O(−j)) of the (non-toric) Schubert variety, nothing on LG/type C specifically (grep lagrang/symplectic/type C: 0). Related, does not state — but cite it: LG has bonds 1,2, so its chain components are lecture-hall-type and this paper is the per-component analogue of the interior-point side.
- Conca (symmetric determinantal / ladder rings, Hilbert series, a-invariant): NOT CHECKED first-hand; affine/local (opposite cell = symmetric matrices), not projective H_κ.
- Regularity literature (Rajchgot–Robichaux–Weigandt 2202.03995; 2202.06362; P-Grothendieck degrees for skew-symmetric matrix Schubert) — affine patches; related to the zero window via a-invariant only. Related, does not state.
VERDICT: positive side owned (De Concini / LS / Chirivì). Negative side SR_LG: not stated in anything checked.

## Item 3 — Proctor d-complete / Ikeda–Naruse / Naruse–Okada
- Ikeda–Naruse 1112.5223 (read, grep): K-theoretic factorial P/Q, excited Young diagrams; no Hilbert/χ(O(j))/reciprocity. Related, does not state.
- Naruse–Okada 1802.09748 skew hook formula (read, grep): no Hilbert/reciprocity hits. Related, does not state.
- Proctor d-complete: shifted shapes are the d-complete family attached to type D (minuscule OG), not type C — so Proctor's minuscule P-partition = Demazure dimension theory covers OG, not LG. Proctor 1984 (Europ. J. Combin. 5, "Bruhat lattices, plane partition generating functions, and minuscule representations"): NOT CHECKED first-hand.
- Ilango–Pechenik–Zlatin 1805.02287 (unique rectification): title/abstract only; K-theory jdt, no Hilbert function. Not relevant.
- Hamaker–Patrias–Pechenik–Williams 1602.05535 Doppelgängers (grep): LG appears only as cominuscule example §4.3.2; no Hilbert. Related, does not state.

## Item 4 — keyword sweep 2023–2026
arXiv/WebSearch/MO: "Lagrangian Grassmannian"+Hilbert → only cohomology-filtration (2011.03179, 2610.28780), quasimaps 0806.0834; +Ehrhart → 0 hits; Schubert+enriched → only A¹-enriched counts (irrelevant); Boming Jia 2310.14302 (Hilbert series of highest weight varieties, adjoint/Narayana; grep lagrang/symplectic 0). Ardila–Bliem–Salazar 1008.2365: type C GT polytopes as marked order polytopes, Ehrhart — full flag reps, no Schubert reciprocity. Nothing states SR_LG.

## Item 5 — Serre duality route
Standard (Ramanathan; Brion–Kumar book Thm 3.4.x — not re-read): X_w CM, ω_{X_w} = O(−∂X_w)⊗L(−ρ); and H^0(X_w, L(−∂X_w)) has the standard-monomial basis of monomials with top element w. Hence H_κ(−j) = (−1)^{dim} #{standard monomials of degree j − a with initial index κ} is "formally" classical. The content of SR_LG = identification of that set with strict diagonal-even maps (and the value of the twist a for LG). No source found doing this for LG. Not checked first-hand (book).

## OG analogue (SR_OG)
Owned as a composite of classical results: minuscule Schubert coordinate ring = ASL/Hodge algebra on distributive lattice J(P_κ) (Seshadri; Lakshmibai–Musili–Seshadri; Gonciulea–Lakshmibai 1996 toric degeneration to Hibi toric variety) ⇒ H^OG(j)=Ω(P_κ, j+1); then Stanley order-polynomial reciprocity Ω(P,−n)=(−1)^{|P|}Ω̄(P,n) (Stanley 1970; EC1 1st ed. Thm 4.5.7 / Cor 4.5.15 as cited by Stembridge §4 — 2nd-ed numbering not verified) and Hibi 1987 (canonical module of Hibi ring = strict maps). No single paper found stating "H^OG_κ(−j) = (−1)^{|κ|}Ω̄(P_κ, j−1)" literally, but it is a one-line corollary — VERDICT: owned (credit Hibi/Stanley/Gonciulea–Lakshmibai/Proctor); first-hand read of these not done this session.

## Half-integer values / zero window a ≤ ⌈r′/2⌉
Nothing found. Not owned as far as checked.

## Overall
- SR_LG: NOT STATED in anything checked. Positive side owned (De Concini; LS/Chirivì). Formal Serre-duality shape classical.
- SR_OG: owned (composite corollary).
- Closest new risk: 2609.03195 (CCFL, Sept 2026) — per-component interior LS paths in lecture hall polytopes; watch for a sequel on Schubert varieties.
- Unchecked first-hand: De Concini 1979, Chirivì 2000, Proctor 1984, Hibi 1987, Conca, Brion–Kumar.
