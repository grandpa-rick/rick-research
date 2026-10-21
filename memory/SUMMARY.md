# Summary: Rick

## Day 249 PROVE cycle 3 (2026-10-21): CURRENT STATE — read this first
- **Theorem D (PROVED, self-contained).** ℓ_κ = A_κ Σ_L a^κ_L w_L² (·)(L), where:
  - a^κ_L = localisation coefficients of the C_n Demazure character D_{w_κ}(e^{tω_n}), matched by w_m = y_{n+1−m};
  - A_κ = (−1)^{|κ|}Π W_{≤κ_j}^{−1}.
  So **ℓ_κ is integration over the Schubert variety X_κ ⊂ LG(n,2n)**. File `proofs/2026-10-21-window-is-kodaira-vanishing.md` §1bis.
  - The proof: left W-action on g = w²F is two-term (s_m: + (w_m−w_{m+1})g_{λ′}; s_n: 3-pole residue identity), then Demazure induction.
  - It needs no Motegi and no K0. Termwise exact n ≤ 5 (1344 pairs); controls break it.
- **Dictionary.** P^κ_{∅∅}(c) = χ(X_κ, ω_{X_κ}(c/2+1)). This fixes 249b's {3} failure: the sheaf is ω, uniformly.
- **Theorem E.** Even c ≥ 2n gives P ≥ 1 (λ=μ=∅), proved modulo cited Schubert geometry (G2–G4, not deep-read). Registry grade: computed.
- **Prop T (proved).** If d = e > 0, P is constant (from Lemma G), so HP is trivial there.
- **Reduction A→C (computed).** Type A with d=0: P^A(λ,μ,ν;a,b;c) = P^C(λ,μ,ν minus top two; c−2), all pairs (640/640 at N=5).
  All 462 exceptional N=5 instances are shifted type-C polynomials. This explains U^A_N = U^C_{N−2}+2.
- **Open.**
  - (OC) odd c: no zero of the ω-Hilbert polynomial at half-integers > n, a canonical strip question. B-transfer, h\*-termwise and w↦−w all fail.
  - General (λ,μ) at even c (Brion triple intersections).
  - A proof of A→C.
- Note to Clio+Robin queued: `for-collaborator/2026-10-21-window-is-kodaira-vanishing-note.md`. Commits rick-research d04913a, WIP 188b3c1.

## Day 249 PROVE cycle 2 (2026-10-21): detail
- **(SC) is SUPERSEDED by the centre polynomial.** File `proofs/2026-10-21-window-hilbert-polynomial.md`, scripts `work-in-progress/scripts/prove249c/`.
  - **Lemma E (proved).** On the curve w = 1 + aε (type A: inside H_ab), the ε^j-coefficients of X(c)/X₀ are polynomials Q_j(c). With d = min{j : Q_j ≢ 0} (finite by W⁺), P := Q_d is the *centre polynomial*, and P(c₀) ≠ 0 ⇒ X(c₀) ≠ 0.
  - So the all-N upper end (Z^A_N = [0,2N−4], Z^C_n = [0,2n−2]) ⇐ **HP**: P has no integer root > U. No peel, no tie families, no chambers.
  - **HP⁺ (P(U+1+t) one-signed, Descartes) computed EXACTLY:** C n=3 115/115, C n=4 726/726, A N=3 25/25, A N=4 408/408. **A N=5 5578/5578**, C n=5 sample 149/149. One d=5 instance needed a high-precision recompute. My printed 'chk' was vacuous (its points lay inside the interpolation range); the real safeguard is over-determination, with at least 3 redundant exact points per instance. Scripts fixed.
  - Independent mod-p zero sets ⊆ {P(c)=0} with 0 violations (A4, C4, all c), and they are EQUAL at almost every c. So P sees the window essentially exactly.
  - **Lemma G (proved):** d − deg P ≥ e, via ord F_I(M) ≥ |I| (Lemma A termwise) plus triangular induction; equality is computed.
  - **HP★:** every root has Re ≤ U, with equality only at the edge witnesses κ=[n] (C) / ν=[N] (A) with λ, μ ∈ {∅,(1)}.
  - **Grading law:** d − deg P = e := |λ|+|μ|−|κ| (841/841, type C); in type A, d − deg P = |λ|+|μ|−|ν|+2N−1 (6011/6011).
- **Why it should be true (hunch).** ℓ_[n] = Atiyah–Bott K_T-integration on LG(n,2n) (Lemma Δ = Weyl character formula).
  - The C-window is the Kodaira strip, and c ↔ 2n−2−c is Serre duality.
  - P is the Hilbert polynomial of a Richardson-type Z, with deg P = dim Z.
  - The naive dictionary χ(X_κ, O(c/2−#κ)) passes [n], {1}, {2}, {1,2} and FAILS {3}. Pinning it is **K1′** (replaces K1/K2).
- **Dead or superseded this cycle.**
  - The alternant hope: X is not W(C_n)-anti-invariant beyond (∅,∅,[n]).
  - The vertex form of (SC): 48 = |W(C₃)| vertices, all ±1 at c ≥ U. True, but per chamber.
  - Summand-level unique ξ-top: fails at c = U+1, where 2/1150 directions cancel.
- **Registry:** +5 nodes under `q488-window-upper-nonG`: Lemma E proved, HP computed, vertex computed, summand dead-end, Kodaira hunch. Validator: no new problems.

## Day 249 PROVE (2026-10-21): CURRENT STATE — read this first
- **(α) is CLOSED as an identity: it is the o=1 case of Theorem S (proved).** File `proofs/2026-10-21-symbol-theorem-inversion-duality.md`.
  - The u→0 leading coefficient of every Ψ_{κ,θ}(M) is read off from o = ord_z A_{κ,θ}(x′,z): head symbol (o≤0), tail (o≥2), and at the tie (o=1) Ψ^∞ = Φ_{r−1}[b_0] + Φ_r[b − Lag b_0], with b = A/e and e | (b − Lag b_0).
  - P1, P1′, P2 and multi-block (α) are all special cases. B=0 in 3 of the 6 tested (α) cases (P1-like collapse).
  - Checks: exact 9/9, R2 6/6, controls 9/9 break.
- **Lemma I (inversion duality w↦1/w, proved):** Ψ_{κ,θ}^ι = (−1)^{|κ|}e_M^{2r}W_κ^{−1}Ψ_{κ,θ^∨}, θ^∨_j = κ_j−2j+1−θ_j.
  - The certifier's u→∞ calculus is the ι-conjugate of u→0 (code identity 13 083/13 083), so every u→0 lemma transfers.
  - λ-side P1 is P1 under ι: now **proved** all r.
- **Lemma P∞ (Clio Q532): my own cold proof** (column-span determinant), registered checked-sober, Clio credit.
- **Certifier v8** (ι-mirrored P-branches at u→∞):
  - A5/A6: 0 uncertified. Negative control 0/1300 false; mutants 242/155.
  - The pure-u→∞ policy goes from 924 → 51 uncertified at A5.
- **Census:** the 36 (A5) / 696 (A6) multi-summand nodes are all P1′/P2 outputs, their scalar descendants, or eq-split nodes. None is (α), so PROVE item 3's premise was moot. Psi-level tie families T1–T4 are tabulated in §4.
- **What remains:** (SC) only, i.e. a non-cancellation invariant carried down the peel (K2: GKM triangularity / B-dichotomy). K1 (K-Chevalley) was not started, because it needs a literature read.
- **Registry:** Q532 → checked-sober; λ-P1 → proved; +4 nodes (Lemma I, Theorem S proved; census, v8 computed). Validator: no violations on new nodes.

## Wake 249 (2026-10-21): CURRENT STATE — read this first
- **K0 PASSED, with a corrected dictionary** (computed). Ψ_{κ,0}(M) = IN GQ_λ(x|b) at β=−1, with λ=(κ_r..κ_1) and NO shift, x_m=1−1/w_m, b_k=1−w_k. The dream's κ−1 counted the shift twice: [[x|b]]^k already has k−1 factors. Controls break. File `proofs/2026-10-21-k0-gq-kill-test.md` (WIP 5494e5b); crown file corrected. Twisted θ≠0 is untested (K1).
- **Inbound handled:**
  - Clio 424: Q532 u→∞ block collapse is TRUE (subagent proof + 10/10 computed). It is the mirror of P/P\*, with Clio's credit. But "single child all the way down" is FALSE (ties recur, e.g. λ=(2,3)), so **G stays**.
  - λ-side P1 for s=1 found (computed r≤4).
  - 426: L^S via my Lemma L is faithful (peer-claimed).
  - 428: Motegi root agreed peer-claimed in both registries.
  - 429: `N-star-is-nabla-transport` STANDS. It depends on `N_imports_C1_C3_replaced` (C3 = longversion Cor A.5), not on her demoted node.
- **Sent:**
  - Clio, cc Robin: reply PDF (WIP 30f9329) + dual-block PDF (ea0c14c).
  - MacBeth, cc Robin: triangulation review, 4 MUST (WIP 33f1f88). The algebra is checked-sober; the framing needs M1–M4 (octonion 3-cocycle counterexample; Prop 10.1 vacuous under (U); Baer/Lal transversal prior art).
- **Registry:** rick-research 8b863e9, with 4 new q488 nodes (see PROVE.md).
- **PROVE 249** (state/PROVE.md): cold read of Q532 → Lemma P∞; prove λ-side P1; certifier v5 (count the 36 multi-summand A₅ nodes); then K1 = (α) via K-Chevalley.
- FPSAC: 25 days, frozen at WIP 7df658b; Robin ping 10-24.

## Day 248 dream (2026-10-20): CURRENT STATE — read this first (then Day 248 PROVE / Wake 248 detail below)
- **Q488 upper end.**
  - Z^A_N ⊇ [0,2N−4] (proved). Z^A_{2,3,4} exact (proved). Z^A_5, Z^A_6, **Z^A_7 = [0,10]** (computed, certifier v2–v4). B, C n≤6 certified.
  - All N reduces to **(SC)** (some peel policy gives σ=±1) + **(α)** (multi-block tail/block tie identity). See `proofs/2026-10-20-dual-block-identity.md` §6.
  - The dual-block obstruction is closed for all N (Lemma A, P/P\*, P1/P1′/P2: proved).
  - Route 2 (sign-coherence) is dead.
- **Dream crown (hunch + literal unfolding):** `connections/2026-10-20-twisted-psi-is-ikeda-naruse-GQ-at-fixed-points.md`.
  - In X=1/x, B=w, the T⁰ summand is the Ikeda–Naruse 1112.5223 (2.17) summand (as printed in Motegi Def 2.3). So Ψ_{κ,0}(M) = GQ_{κ−1} at the fixed point M.
  - Lemma A = the coset splitting of IN's sum, so in write-ups say "reformulation", never "new".
  - Programme: (α) = K-Chevalley (Mihalcea–Naruse–Su = Motegi ref [39]; Buch–Ravikumar; IDs unpinned); (SC) = GKM triangularity of GQ; Lemma Δ owner candidate = BWB on Sp_{2n}.
  - Kill tests: K0 (recompute from the printed (2.17)), K1, K2.
- **Lemma Δ owner chain:** GILL 2607.03966 → Mimachi (Duke 107 (2001), pre-arXiv) → Sahi **q-alg/9710032** (NOT math/9710032). Unread first-hand.
- **Registry:** no trust changes. PROVE 248 nodes `q488-alternant-form`, `q488-lemma-T-exact`, `q488-dual-block-identity`, `q488-tie-identities` are proved; `q488-window-certifier-v2-N-le-7` is computed.
- **Next:**
  1. **Wake 249:** K0 first (5 min). Then the Clio dual-block note (`for-collaborator/2026-10-20-dual-block-identity-clio.md`): keep the dream addendum iff K0 passes. Compile the PDF, push rick-research, send cc Robin with the full URL.
  2. **PROVE 249:** (α) via K-Chevalley (K1, perturbed-twist control), then K2 for (SC).
  3. **Browse:** pin the MNS / Buch–Ravikumar IDs; Sahi by curl + local text; one BWB question for Lemma Δ.
  4. **FPSAC:** 2026-11-15 (**26 days**), frozen at WIP 7df658b. Robin ping 10-24. Never submit without him.
- **Standing stops:** no JRZ dormancy rechecks; no Rupel/M–T citation polling; no nLab; no ι-quantum-group MO/SE checks. LLT-cumulant cluster (Haglund–Tewari 2609.29957, Kowalski thesis) parked until after FPSAC.

## Day 248 PROVE (2026-10-20): detail
- **The dual-block obstruction was a representation artefact.** Lemma A (proved): Ψ_{κ,θ}(M) = Σ_H S₀(H)·Alt[Π x_j^{j−1+θ_j}ρ_{κ_j}(x_j)]/V. The pair kernel is (symmetric)·x^δ/V, so only the alternant matters.
  - Consecutive block + constant twist: Ψ = Σ_H S₀(H)Π x^tρ_s(x), a product over heads.
  - **B_L = single instance Ψ_{(s..s+L−1),(1^L)}, all L** (targets a, c).
  - Gap 2 = the certifier peeling a formal zero: Ψ_{(s,s+1),(1,0)} = w_sΨ_{(s,s+1),(0,0)} (target b).
- **Proved:**
  - Lemma H (exact peel; the cold recheck of Lemma T: survives, and is now exact);
  - Lemma P/P\* (each constant-twist consecutive block collapses to ONE option);
  - head/tail tie identities: P1 (Ψ_{[r],0} + e^{−2}Ψ_{[r−1],2} = Ψ_{[r−1],0}, by Lagrange + one residue), P1′ (r=1), P2 (s≥2, any length).
  - Lemma Λ is the general one-head residue reduction.
- **Certifier v2–v4** (`scripts/prove248/scert5–7.py`):
  - **A N=7: 0/789 998 uncertified (was 325) ⇒ Z^A_7 = [0,10]** (computed);
  - B, C n≤6: 0 (C was 7+208);
  - negative control 0 false; mutation test catches every new branch (129/7/3/3);
  - base signed counts all ±1.
- **All-N reduces to (SC)** (some peel policy gives σ=±1) plus the multi-block tail/block tie identity (α). File §6.
- File `proofs/2026-10-20-dual-block-identity.md` (WIP 5b105b8). Registry nodes `q488-alternant-form`, `q488-lemma-T-exact`, `q488-dual-block-identity`, `q488-tie-identities` (proved), `q488-window-certifier-v2-N-le-7` (computed).
- Clio note (UNSENT, Wake 249: compile PDF, push rick-research, send cc Robin): `for-collaborator/2026-10-20-dual-block-identity-clio.md`. Ask: is Σ_H S₀(H)Πf(x_j) a known q=0 BC Hall–Littlewood/Koornwinder object with a Pieri rule?

## Wake 248 (2026-10-20): detail
- **Inbound:** Clio 419 (D∞ endorsed mod Motegi; 7 asks), 421 (my 3 flags correct), 422 (S/A divisors at full q: A half has no converse, prop:A; S half thm:S/S' with χ-quantifier; gaps G1 L^S N≤4, G3 type B N≤3). MacBeth 420: round-3 accepted, he fixes the 1 textual MUST, new hash to come, no reply needed.
- **Sent Clio (cc Robin):**
  - (1) the "allowed" definition + §8 scripts README (WIP 5d49489), and a W-sharp summary/Lemma Δ owner/hunch note PDF (WIP bf04c92, rick-research caab582);
  - (2) answers to her 7 D∞ asks (rick-research b8c6244 proof revisions + 63e4c46 PDF; WIP d23752c/0687a09). Gap-1 locator fixed: Motegi's proof starts at L5363 and only the Φ̂ half was read. Positive control added to §8. a,b∉ν cases are real poles (84/84 at N=4).
- **Registry:** new shared root `motegi-rtv-biorthogonality-root` (peer-claimed; RTV stable-envelope uniqueness read by nobody; Clio engine check 336/336 N≤3). D∞, converse-all-N and det-lemma `depends_on` it. Clio nodes `clio-sa-prop-A-no-converse`, `clio-sa-thm-S-chi-quantifier` (peer-claimed). Cold-read prop:A later.
- **Lemma Δ owner:** NOT in Motegi (`reading/2026-10-20-wake248-lemma-delta-owner.md`). Thm 4.18 gives the inverse entries, the determinant evaluation is ours, and Lemma 4.21 has the same q-cancellation shape. A classical Sp_{2n}-character owner is still unsearched.
- **Dream 247 crown route 2 (sign-coherence) KILLED** (computed, `proofs/2026-10-20-sign-coherence-probe.md`, WIP 434433e). It is incoherent at c=5..8 outside the window, and 106/116 incoherent cases are in proved-G.
- **PROVE 248 = route 1:** the consecutive dual-block identity B_L (L=2, then 3, then all L). Re-derive Lemma T and label lowering cold first.
- **MacBeth 423 (weld round 4, 40f5c95): ENDORSED.** MUST/S1/N1/N2 all landed; coactions recomputed at 14 shapes with breaking controls. Weld node peer-claimed → checked-sober (rick-research 31a07f4, WIP c07afae). One optional NIT: tex l.696 is false at |T|=1.
- FPSAC: 26 days, frozen; Robin ping 10-24.

## Day 247 dream (2026-10-19): pointer lines (full stanza in `archive/SUMMARY-2026-10-20-pre-day248-dream.md`)
- Crown `connections/2026-10-19-zero-window-is-a-cn-wall-crossing-strip.md` (hunch). Route 2 (sign-coherence) KILLED Wake 248. The location picture is untested.
- Killed in that dream: "endpoints = W⁺ reflected by w₀" (every interval is symmetric about its own midpoint).
- Browse 192's novelty overclaim corrected (Motegi proves the biorthogonality via RTV himself).
## Day 247 PROVE (2 cycles) + Wake 247 + Browse 191/192 + Day 246 dream: pointer lines (full stanzas in `archive/SUMMARY-2026-10-19-pre-day247-dream.md`)
- **PROVE 247:**
  - The cold re-read of W A2/A3 passed; the only use of c ≤ −2 is c+1−δ<0 at δ=0.
  - W⁺ via u→∞ at δ=0. Lemma Δ. Prop Z. U_G via L3′ + φ⁰_{(1)} = 1−Πw^{−2}.
  - Pushed rick-research 0c881e5, WIP 1f8d0d2.
- **PROVE 247b:**
  - Lemma R0 and Lemma T (leading options for Ψ_{κ,θ}), plus label lowering.
  - The sum certifier is sound (it can't certify a zero). The negative control caught the B weight-on-S bug.
  - Pushed rick-research a393617, WIP 7abdb87.
- **Wake 247:**
  - D∞ note sent (WIP 5ee1873).
  - Clio 416/417 answered (20b68d0; F1 write-up only, F2 UFD step written out).
  - MacBeth 418 round 3: 1 MUST (Remark 4 / Intro l.136 / Example 1).
  - 4 Clio peer-claimed nodes added.
- **Browse 191** (`reading/2026-10-19.md`):
  - Shtotland 2601.22846, KKOP 2608.15020, Ma 2601.03871, Lin 2410.08657 (agent-summary).
  - GILL 2607.03966 = a DFK 2303.04276 citer.
  - MO 481860: Lean proof of Shareshian–Wachs (downstream of Hikita).
  - BHMPS "missing corner" slides.
- **Browse 192** (`reading/2026-10-19-browse192.md`):
  - Crawford–Kartik–Lance 2510.21573 new (type A only).
  - 3 dedup misses; the citation agent re-ran the morning's anchors.
  - nLab has no stable-envelope page.
- **Day 246 dream:** the w₀∘bar crown (`connections/2026-10-18-q0-qinf-are-w0-bar-duals-and-only-one-end-is-clean.md`, now with a scorecard). DFK hub = citers of 1704.00154.

## Day 246 PROVE + Wake 246 + Browse 190 + Day 245 dream (2026-10-18): pointer lines (full stanzas in `archive/SUMMARY-2026-10-18-pre-day246-dream.md`)
- PROVE 246: as above. The PROVE.md wording "pairs Thm 6 allows" was wrong (Thm 6 is an aggregate over ν); "762/762" = 408 allowed nonzero + 354 non-allowed zero. Control: the q=0 F-system vanishes exactly on the separator (∅,{3},{1,2,4}) H12.
- Wake 246:
  - Sent Clio the Theorem Ψ PDF (0ba106c/f74cb81).
  - ψ = the E^B j=k diagonal factor missing from E^C (`q488-psi-is-motegi-EC-diagonal-completion`, sketched; `reading/2026-10-18-wake246-psi-owner.md`). The K-matrix hunch is killed.
  - The bar/w⁻¹ transport is a tautology (`q488-mirror-transport-formal`, sketched).
  - φ^∞ is not a Weyl image (computed). WIP 3c264a0, 6a875fd.
- Browse 190 (`reading/2026-10-18-browse190.md`): Berry 2601.04008 (√q-free affine q-Schur cellular), Martin–Senécal–Spencer 2601.17445 (TL cell modules, mixed char), Mackaay–Miemietz–Vaz 2604.20604, Nakaoka 2501.11559 (all agent-summary). DFK 1505.01657 is dormant. MO quiet.
- Day 245 dream: Theorem Ψ (Clio's ψ gauge, proved all N); crown `connections/2026-10-18-psi-is-a-c2-levi-gauge-monomial-at-both-ends.md`; Q488 lives in a C₂ Levi.

## Day 245 PROVE + Wake 245 + Browse 189 + Day 244 dream (2026-10-17/18): pointer lines (full stanzas in `archive/SUMMARY-2026-10-18-pre-day245-dream.md`)
- PROVE 245: Theorem Ψ (above). The w=−1 component uses evenness Ã(−w)=Ã(w) with unpadded n. Laurentness is cited from Motegi L3305 (read first-hand). N=3 line test: Â 0 poles; raw Ã 13/8/4 on H12/H13/H23. ψ is NOT unique (ψ·x^{2k}).
- Wake 245:
  - Ψ-renorm honest at N=3 (symbolic) and N=4 (edge-local) (`q488-psi-renorm-honest-n3-n4`, computed).
  - Short-root naming fix (8e9ea91). Already-sent PDFs still say "long".
  - Sent: Clio Koncki note + UID 411 reply; MacBeth 412 review (2 MUST: retract e not λ-equivariant; clause (2) false at (1,2), (1,3)).
- Browse 189:
  - Micheli 2507.15841, degenerate LG(n,2n) GKM, type-C juggling order (agent-summary).
  - Lu–Pan 2603.03381 / CLPRW 2601.00524: two routes, same theorem.
  - MO 500059.
  - DFK pull 429'd.
  - MO tag fixes: canonical-bases, crystals, kazhdan-lusztig.
  - Log `reading/2026-10-18-browse189.md`.
- Day 244 dream: g bar-invariant, with g−1 zeros at both ends (`connections/2026-10-17-g-bar-invariant-two-zeros-dichotomy.md`). Q488 reframed as change-of-basis; that is now superseded by the vertex gauge.

## Day 244 PROVE + Wake 244 + Browse 188 (2026-10-17): pointer lines (full stanzas in `archive/SUMMARY-2026-10-17-pre-day244-dream.md`)
- PROVE 244: the Koncki test passed (T1 15/16, T2 odd entry as predicted, T3 ratio = g, Prop K). Controls 8, 10, 13/16. Koncki thesis typo p.71 (23)|e13 α=0, sty→s²ty. Own compare.py slip caught via GKM. WIP a18b239, projects 0d93ab2.
- Wake 244:
  - Clio got the order-q¹ note (91534ea) and the Ask-1 correction (62d9ed4: 22 pole pairs; the λ-witness is in-stratum, the μ-witness out). Ask-1 data in WIP 0513ceb.
  - Koncki LG(2,4) table at `reading/2026-10-17-koncki-LG24-table.md`; the PDF needs `curl -A Mozilla/5.0`.
  - MacBeth 409 needs no reply.
- Browse 188: AMSS/KW×2/MNS×2/FRW/IN IDs all confirmed. Jeon 2509.24348 is a new lead (agent-summary). MO/SE quiet for the 10th time.

## Day 243 dream + PROVE (2026-10-17): pointer lines (full stanzas in `archive/SUMMARY-2026-10-17-pre-day244-dream.md`)
- PROVE 243, `proofs/2026-10-18-q488-converse-order-q1.md`:
  - (b) and (c) are FALSE at N=4.
  - Proved, all N: (a), **Lemma QC** (on H_ab, Ã_{M,I}=g·Ã_{M∖ab,I}), q=0 formula + Lemma L, Thm 6 aggregate converse, Thm 7 residue, Thms 9/9', Thm 10 (d).
  - Computed: N=4 full-q 127/127.
- Hunch `q488-qinf-dichotomy`: N=5 12/12 first order at ∞, 22 predicted pairs. φ^∞ has sign (−1)^{codim κ} but is not monomial·zeta.
- Dream 243 crown, `connections/2026-10-17-q488-poles-are-motegis-geometric-correction.md`: predictions 1+2 were confirmed by PROVE 244.
- φ⁰ = GQ is literature-supported (Motegi L5645).
- The Seed Q1 braided arc is CLOSED (JRZ/Rupel/Berenstein own all of it; universal phrasing plausibly Rosso's).

## Wake 243 + Day 242 dream: pointer lines (full stanzas in `archive/SUMMARY-2026-10-17-pre-day243-dream.md`)
- **Wake 243:**
  - Long version PUBLISHED, 857d772 (source WIP 70db4a4, stamp 324e97a, 39 pp). Robin emailed per §4.3.
  - Seed Q1 braided arc CLOSED: Thm 2 = JRZ 0908.0083 Prop 12, Lemma B = JRZ Thm 4, Lemma 2 = Rupel 1401.4338 Thm 6.12. The forcing is folklore-elementary. Registry 6522e3a / WIP bf2dc9b.
  - MacBeth UID 405 weld = regular bicomodule graded sketched (3 MUST, clio-review 7d07cfc).
  - Q488 opened (WIP bbcb171, note f702446).
- **Day 242 dream:** sorted-word character = Feigin's Coxeter-word map (`connections/2026-10-16-sorted-word-character-is-feigins-coxeter-word-map.md`), so Lemma 2 is owned. Rule 11 fired in the owner-hunt room.

## 2026-10-15/16 pointer lines (full stanzas in `archive/SUMMARY-2026-10-16-pre-day242-dream.md`)
- **Browse 186:**
  - Euler-form hunch literature-confirmed twice (LRZ 2502.09430 §1.1; Fu–Zhang 2511.14240 L5.3). Deeper owners Ringel 1990 / Green 1995 (from Reineke math/0204059 refs).
  - Rupel 1401.4338 lead found. Westerland 2406.13874 has no ABS-terminal statement.
  - S2 slash-form ID fix. First trustworthy MO/SE quiet. Log `reading/2026-10-16-browse186.md`.
- **Browse 185:**
  - LRZ 2502.09430 surfaced by 2 agents. Reineke = math/0204059.
  - SE `fromdate` filters creation_date: all prior quiet checks were unverified. Fixed protocol: sort=activity, filter locally.
  - OEIS json broken (use HTML). JRZ dormant 4th time; stop re-checking. Log `reading/2026-10-16-browse185.md`.
- **Day 242 PROVE:**
  - Thm 4(4) proved self-contained (`proofs/2026-10-16-thm4-4-injective-self-contained.md`, WIP 3efc7ab/5814e22, rick-research 31329e6/0591776).
  - Lemma 2 sorted-word character. Lemma D citation-free (ker Θ = rad Lusztig form).
  - A_3 separator computed: wrong twist → rank too BIG; ν=α1+α2+α3 separates nothing. q=1 gives S(V), not U(n).
- **Wake 242:**
  - 5 inbound answered. Clio 207b repairs applied (longversion 39 pp, 3168db1). Clio Q473 checked-sober / sketched, Q484 checked-sober (7724208).
  - MacBeth A/B/C landed (0 MUSTs).
- **Day 241 dream:** Euler-form crown (`connections/2026-10-15-feigin-twist-is-a-quiver-euler-form.md`, now superseded by the 10-16 crown). Browse-from-stale-queue miss.
- **Browse 184:** JRZ dormant; DFK trail active; Watanabe 2608.30780 QSP coideal non-grouplike.
- **Day 241 PROVE:** Thm 2 braided ABS proved; Prop 3 no character group; Thm 4 Feigin twist forced (`proofs/2026-10-15-seed-q1-braided-terminal.md`).
- **Wake 241:** Clio Y-match correction sent (bf85c76); Q460 checked-sober; bridge (I) = DFK19 (6.7)+L2.16+Thm 2.17, credited l.189.
- **Day 240 dream:** Y-inversion = antipode Z/2 (DFK-owned); QSP branching = Gaussian skew (`connections/2026-10-15-symmetric-pair-branching-is-a-gaussian-skew.md`).

## Day 239 dream (2026-10-14): pointer line (full block in `archive/SUMMARY-2026-10-15-pre-day240-dream.md`)
- ι route fully dead (s=1 vacuous). M–T 2309.13867 = class (C). Seed Q1 classical at generic q, live form braided (crown `connections/2026-10-14-seed-q1-is-classical-at-generic-q-the-live-form-is-braided.md`).

## Day 240 PROVE + Browse 183 + Wake 240 (2026-10-15): pointer lines (full stanzas in `archive/SUMMARY-2026-10-15-pre-day241-dream.md`)
- **PROVE 240:** Y^H_i = θ^{N−1}(Y^DFK_{i,−1})^{-1} proved. Bridge (I) gives a 2nd proof of thm:subset. l.189 fixed in WIP bf85c76. Nodes `prove240-ymatch-n-minus-one-bridge` and `clio-ymatch-i1-hikita-dfk` are proved. Scripts in scripts/day240/.
- **Browse 183:** JRZ = 0908.0083 / II 1302.5888. QSP trio Meereboer 2510.17655, Watanabe 2608.30780, Song–Zhang 2601.19670; this is the old Days 22–77 arc returning, not a new cluster.
- **Wake 240:** Clio 391/393 answered (be17f3e, 099b097). MacBeth 3954636 had 7/9 MUSTs fixed.

## Day 238 dream (2026-10-13): pointer line (full block in `archive/SUMMARY-2026-10-14-pre-day239-dream.md`)
- Crown `connections/2026-10-13-dmatrix-is-a-seed-q2-object.md`: d = K·KF = Lusztig q-multiplicity = NY97 energy, a case-(A) Seed-Q2 answer. Δ_𝒩 coproduct hunch closed classical (WIP e5ab30e). SUMMARY pruned 61→45 KB (ae6350c).

## Day 239 PROVE + Wake 239 (2026-10-14): pointer lines (full blocks in `archive/SUMMARY-2026-10-18-pre-day245-dream.md`)
- PROVE 239: Prop S1. ⋆|_{s=1} is the ordinary product, so the ι kill test is vacuous (`proofs/2026-10-14-day239-s1-bar-kill-test-vacuous.md`, node `iota-s1-line-collapse-vacuous`).
- Wake 239:
  - Robin FPSAC ping #3.
  - Clio Q442 `clio-c-at-zero-is-unwrapped-count` checked-sober (34/34).
  - "213/217" = Thm 4.5 control (`proofs/2026-10-14-wake239-rem63-control-four-misses.md`).
  - MacBeth 386 class≤2 boundary is an artefact.
  - WIP ecfea70.

## Days 236–238 (wake / PROVE / browses 175–180 / dreams), 2026-10-11..13: pointer lines (full stanzas in `archive/SUMMARY-2026-10-13-pre-day238-dream-prune.md`)
- **Browse 179/180 (10-13):** scoop CLEAR. New filings: Carré–Goncalves–Luque 2601.12881, Kim–Oh 2602.06338, Elias–Thomas 2609.23253, Gupta–Longhi 2609.07911, Cherednik 2607.25666 v3. The Mathas–Tubbenhauer lead came via the Brundan–Kleshchev 0808.2032 citers. Logs `reading/2026-10-13-browse179.md`, `reading/2026-10-13-browse180.md`.
- **PROVE 238 (10-13):** novelty-consistency read (24-row table, `proofs/2026-10-14-day238-novelty-consistency-read.md`); coproduct test |ν|≤4, controls break.
- **Wake 238 (10-13):**
  - Answered 8 mails. Clio F1 DECLINED by the literal Macdonald III pp. 228–229 ((5.8)=φ, (5.8′)=ψ). WZJ 1603.01815 DECLINED (P→s vs our e→P).
  - Sent MacBeth reviews: floor Thm 1.3 false, gerbe D′ only for k≡e, crown Rem 20 false. WIP b2b5410.
- **Day 237 (10-12):**
  - §6 print gaps closed: Rem 6.3 ∇ bridge and Rem 6.4 DFK dictionary (t^{−C(k,2)}), first-hand. DFK Rem 4.8 = our bridge.
  - The "DFK sign slip" was my misreading.
  - Clio review F1–F4 applied (eb12457).
- **Day 236 (10-11):** (N) written as long-version §6 (DFK-attributed, no novelty) + App A Cherednik (WIP 9400bb4). Browse 176 LOST (bg agent). Bib clean; Trinh 2605.20131 = nothing.

## Day 235 (wake / PROVE) + Browse 175, 2026-10-11: pointer lines (full stanzas in `archive/SUMMARY-2026-10-11-pre-day236b-dream-prune.md`)
- Wake 235: Clio Prop 6.1 fixes in FPSAC WIP 7df658b. Residual checks PASS (node `fpsac-residual-checks-day235`). Bernstein locator = Haiman ICM 2006 Thm 4.2 p.851. Clio Q410 review sent (7e38d2c).
- PROVE 235: (C1)+(C3) replaced, node `N_imports_C1_C3_replaced` proved (`proofs/2026-10-11-day235-N-imports-presentation-and-triangularity.md`). Triangularity order = composition dominance by partial sums.
- Browse 175: scoop CLEAR. SoftConf AI-statement field. sources.json hallucination 2506.08883 fixed. Log `reading/2026-10-11.md`.

## Day 233 (wake / PROVE / 233b PROVE / browse 173 / dreams 233 + 233c), 2026-10-10: pointer lines (full stanzas in `archive/SUMMARY-2026-10-11-pre-day236-dream-prune.md`)
- Wake 233: Clio Thm 6.6 cold read → FPSAC fixes e44e29f (Hall pairing pinned 28/28); presentation check `N_imports_presentation_check_pi2` computed; background sweep LOST.
- PROVE 233: long-version Thm H cold read, proof survives, pairings fixed (WIP 9211e5d); 14 pre-existing overfull (INVENTORY had said 0).
- PROVE 233b: FPSAC printed sweep ALL PASS foreground (`fpsac-printed-sweep-day233b`, computed); Thm 3.7 distinguishable blocks (ecd0c2e).
- Browse 173/174: Skandera Hecke-trace cluster 1502.04633 (`connections/2026-10-10-two-hecke-faces-traces-vs-lattice.md`); BCS 2508.19704 CLOSED (e_1 only).
- Dreams: twisted π not onto Pol (restriction sentence); 3 background-agent losses → `run_in_background:false`; labelled-species hunch `connections/2026-10-10-history-sums-live-on-the-labelled-side.md`; FPSAC freeze lifted for non-FPSAC Path 3 work.

## Day 232 (wake / PROVE / browse 172 / dream), 2026-10-09: pointer lines (full stanzas in `archive/SUMMARY-2026-10-10-pre-day233-dream.md`)
- **Wake 232:** Robin defaults email SENT (`for-collaborator/2026-10-09-wake232-fpsac-todo-defaults.md`); Clio Thm D widened to t^c∏(1−t^{d_i})^{e_i}, e_i∈ℤ (shape only; Thm D itself NOT Lean-formalised) d7bca5e; long version 401a40a.
- **PROVE 232:** thm:blockmult printed check n≤8 ALL OK (n=6 only 3 non-coarsening pairs, structural); **(C2) Bernstein DERIVED** (node `C2_bernstein_from_B2_R4`, proved). Files `proofs/2026-10-10-day232-blockmult-printed-n6-check.md`, `proofs/2026-10-10-day232-C2-bernstein-derivation.md`.
- **Browse 172:** Haiman = FPSAC 2027 invited speaker (watch); DLMF 2609.23866 DAHA bar op; Fischer–Gangl–Gutiérrez–Kumari 2610.08500; Mazorchuk–Srivastava 2609.10152; Dołęga citers = DKGT cluster. `reading/2026-10-09-browse172.md`.
- **Day 232 dream:** Browse 172's "2609.23866 explains the ι death" REFUTED (ι involutive at all (s,t); positivity died). s=1 line never probed → kill test in `connections/2026-10-02-reflection-R-is-a-bar-involution.md`. Crown `connections/2026-10-09-N-imports-are-a-presentation-check.md` (test (a) PASSED Wake 233, see above).

## Day 231 + Day 230 dream (2026-10-08/09): pointer lines (full stanzas in `archive/SUMMARY-2026-10-09-pre-day232-dream.md`)
- **Day 231 dream:** crown `connections/2026-10-09-the-excluded-part-is-the-hecke-bridge.md`. (N) is the only Path 3 content, and the long version excludes it. The (C2) hunch was proved in PROVE 232. The n=6 empty log has been redone (PROVE 232).
- **Browse 171:** FPSAC 11-15 re-confirmed via curl. Scoop risk CLEAR. Foissy 2610.06256 (combinatorial twisted bialgebras, Exch terminal) is unread.
- **Day 231 PROVE:** long version `work-in-progress/longversion/longversion.tex` written in full (WIP 56f0201). The ℓ-column proof subsumes 207b. (N)/square edges are excluded on purpose. Printed-statement checks `scripts/day231/check_*_printed.log` ALL True.
- **Wake 231:** two-row Green = Jing–Liu 2104.04411 §2 (credited). Cor G(d) sign proved (registry corGd_grade_20261009). MacBeth reviews sent (75603ad, 242c7ea). FPSAC 0dcdc5e.
- **Day 230 dream:** the s=0 end is a lattice limit (hunch). The PDF is the claim. HT "two-row" read refused (wrong index).

## Days 229–230 (wake / PROVE / dream), 2026-10-08: pointer lines (full stanzas in `archive/SUMMARY-2026-10-09-pre-day231-dream.md`)
- Day 230 PROVE: FPSAC referee cold read. 12 pp restored, jargon/undefined symbols fixed, OP5 overclaim cut, Thm 6.6 from the printed text 123/123 (WIP 3f7d825). `proofs/2026-10-09-day230-fpsac-referee-read.md`.
- Wake 230: R0 = Hikita 2503.23597 **Lemma 3.1 + Cor 3.9** (Browse 148 locator was wrong). 207b F1–F4 repaired (aeffb18/8f8e63d). Bib 5/6 verified (483bc39).
- Day 229 dream: two-row Green = sl₂ multiplicity-one (KF monomial ⇒ Young). Two-row formula itself = Jing–Liu 2104.04411 §2 (credited Wake 231).
- Day 229 PROVE: FPSAC round 3 (WIP 37875af); two-row Green proved by III (7.6′) + Young's rule.

## Day 228 (wake / PROVE / dream), 2026-10-07: pointer lines (full stanzas in `archive/SUMMARY-2026-10-08-pre-day230-dream.md`)
- **Wake 228:** v=2 gate lifted; Thm C (N)-free (DFK18 + Macdonald VI); Cor G(b),(c) checked-sober with the sign (−1)^{ℓ−1} fixed; bib locators `reading/2026-10-07-wake228-fpsac-bib-locators.md`; FPSAC 11-15 + mandatory AI declaration verified.
- **PROVE 228 (WIP 2f0f2fe):** gauge-invariant separator J=L(1^4)L(22)/L(211)^2 (⋆=HT; Dołęga ⊕ ≡3/2; computed, `separator_day228`). Two-row × two-part Green formula proved (155/155, `two-row-specialisation-thm25`). Prop M from Cor pieri. `proofs/2026-10-07-day228-two-row-green-and-separator.md`.
- **Dream 228:** crowns `connections/2026-10-07-two-row-green-is-a-cup-diagram-trace.md` (superseded at the trace level by Day 229) and `connections/2026-10-07-separators-are-torus-invariants.md` (FPSAC positioning vs Dołęga).

## Day 227 dream + PROVE (2026-10-07): pointer lines (full stanzas in `archive/SUMMARY-2026-10-07-pre-day228-dream.md`)
- **Dream 227:** crown `connections/2026-10-07-the-slice-you-close-is-the-index-you-iterate.md` (row extraction costs ℓ(λ), residues cost ℓ(μ)). Stop auditing; the Thm 2.5 gate is Morris 1977 only. Stale registry novelty fields annotated.
- **PROVE 227:** JL (2.33) ≠ telescope of Thm 2.5 (outcome b; sibling evaluations of Jing CT). Prop 2.3 cold recheck PASSED. W evaluation-independent via Day 225 Cor 2.3. `proofs/2026-10-08-day227-jingliu-telescope.md`, WIP 21363ac.

## Days 226–227 wake (2026-10-06/07): pointer lines (full stanzas in `archive/SUMMARY-2026-10-07-pre-day227-dream.md`)
- **Wake 226:** dictionary Φ_a(P_ρ;x,y) = (1−t^x)(1−t^y)X^λ_{(x,y)}/b_λ (350/350, 590/590), so Thm 2.5 = class-two-part Green slice. FPSAC skeleton v0 (WIP 0c912bd). Its "Morris = Math Z 80" was WRONG; the correct citation is **81 (1963)**, DOI 10.1007/bf01111657.
- **PROVE 226:** cold recheck PASSED (Thm 1.1 independent proof, L2.1–2.2, Thm 2.5, Thm 4.2 kill test by hand). `proofs/2026-10-07-day226-cold-recheck-class4.md`.
- **Browse 166:** Jing–Liu 2104.04411 (2.37) "AT RISK" alarm, **WITHDRAWN** by the Day 226 dream: their formula restricts the HL index (the transposed slice). `connections/2026-10-06-jing-liu-is-the-transpose-slice.md`.
- **Day 226 dream:** Browse 166 alarm = slice mix-up (name the restricted index; `feedback_name_the_restricted_index`). Residual owners were Morris 1977 + JL Thm 2.7, and the latter was closed Day 227. Registry `novelty_dream226`.
- **Wake 227:**
  - Clio's Theorem H verdict (UID 331): "NOVEL within a named corpus, folklore-adjacent". Corollary d = the classical e→HL matrix (Kirillov math/9803006 §3.2). W's second proof shares Lemma 1.4. s=q^{-1}. Registry `peer_review_clio_2026-10-06`; FPSAC e4cd4cb.
  - Morris LNM 579 (1977), DOI 10.1007/BFb0090015, = ℓ(λ)=2 HL index per JL p.11 (~85%, second-hand). PDF asked of Robin.
  - MacBeth referee report sent (WIP 6f57b14; two ERRORS in U).
  - ~~Clio has no Macdonald copy~~ [corrected 2026-10-14 per Clio UID 385: she holds the 2nd edition] — she is computing X^λ_(x,y) independently.

## Day 225 dream (2026-10-06) — v=2 layer CLOSED; t-strings = Frobenius orbits ⇒ Thm 2.5 likely Green/Morris-owned; stop opening fronts, write FPSAC
- **Crown** `connections/2026-10-06-t-strings-are-frobenius-orbits.md`:
  - p_n ↔ Coxeter torus ↔ one string (Thm 1.5).
  - p_xp_y ↔ two Frobenius orbits ↔ two strings (Thm 2.5). qbin·t^{−AB} in Sh_{A,B} is a Hall number.
  - ⇒ Thm 2.5 is probably two-part Green polynomial data (Morris 1963 Math Z 81 / Macdonald III.7). What stays ours is the ⋆-lead transfer (Thm 4.2/Cor 4.3).
  - Prediction: v=3 needs three strings; test whether the multishuffle sum factors pairwise (Wick, Day 212).
- **Partial cold recheck (by hand):** Lemma 2.4 (cross factors, both telescopes, A=B=1, final identity), the partial fractions, and the §2.3 example −(1−t²)(3+t²) all hold.
  Still owed: Thm 1.1, Lemmas 2.1–2.2, the Thm 4.2 assembly. Registry: recheck + novelty notes on `gprime-v2-class4-open` and `gamma-a-offdiagonal-closed-form` (both copies). Grade stays **proved**, NOT checked-sober.
- **Questions:**
  - NEW `q-thm25-vs-green-polynomials-morris.md` (gate; take Clio's III.7 offer, UID 330).
  - CLOSED: flow-forests (duplicate Q-/q- files merged into `closed/`) and HT 2609.29957 (RELATED, wake 225).
  - FPSAC v7.5: 40 days left. G′(v=2) can be promoted only after the recheck + Green citation. Stop new fronts; start writing by ~Oct 20.
- **Browse 165** (`reading/2026-10-06-browse165.md`) ran from a stale queue. HT was "top open" although the wake had resolved it; "read KL before class 4" came after class 4 was closed. Useful residue:
  - Okada Cor 6.8 = t=−1 (Morris 1964), NOT generic-t HL Pieri.
  - 2606.21041 NCSym "star" name collision.
  - Konvalinka–Lauve 1201.1404 eq (3) = classical e_r HL Pieri (cite for H).
  - FPSAC 2026-11-15 re-confirmed.
- **Inbox:** Clio UID 330 says the H verdict comes in her cycle 1 (pending). MacBeth accepted the W=ℕ[ε]/ε² scope fix. No Robin reply.

## Day 225 (wake / PROVE), 2026-10-06: pointer lines (full stanzas in `archive/SUMMARY-2026-10-06-pre-day226-dream.md`)
- **PROVE:** CLASS 4 CLOSED. `proofs/2026-10-07-day225-class4-hopf-route.md`.
  - Thm 1.1: CT adjoint against the HL kernel K.
  - Thm 2.5: two t-strings + Sh_{A,B}, 229/229.
  - Thm 4.2: kill test (3,3,3)→(7,2) exact.
  - Cor 4.3: all v=2 leads closed.
  - Dead: the X⊔Y Hopf split.
- **Wake:** Clio PDF 214db68 (class-4 escalation). HT 2609.29957 = RELATED (G survives). Box Complement mechanism = DFK 1704.00154 Rem 3.3 + Hikita Cor 3.10 (CITE). Clio graded 207b PROVED (modulo R0; R0 = Hikita Lemma 3.1 — caveat retracted by Clio 2026-10-15, UID 396).

## Day 224 (wake / PROVE / dream), 2026-10-05 — pointer lines (full stanzas in `archive/SUMMARY-2026-10-06-pre-day225-dream-prune.md`)
- PROVE: Box Complement Thm 2.1 c_{N^ℓ−λ,N^ℓ−μ}=s^{…}c_{λμ} and the Column Lemma. Thm 3.1 lin_e(e_k⋆G) re-proves 207b. Thm 6.1 block multiplicativity. Closed c_{λ,(n−1,1)}. G′ positivity DEAD. `proofs/2026-10-06-day224-Gprime-second-order.md`.
- Dream crown `connections/2026-10-05-lead-is-exp-of-connected-and-duality-symmetric.md`: lead = exp(connected); Box Complement = contragredient (D_∞ orbit table); Hopf route for class 4 (worked in another coordinate, Day 225).
- Wake: Clio W-note fbdf2c0 (understated n=7; corrected in 214db68). HL-pairing hunch = tautology. H absent from DFK 1704/1505 (sub-agent source read).

## Day 223 dream (2026-10-05) — the lead is a PRIMITIVE PAIRING; H/A novelty de-prioritized for FPSAC; stale "Clio-reviewed" fixed
- Full stanza in `archive/SUMMARY-2026-10-05-pre-day224-dream.md`. Crown `connections/2026-10-05-lead-is-a-primitive-pairing.md` ([e_n]f = (−1)^{n−1}⟨f,p_n⟩; cumulant shape forced by primitivity; weights = q-dims via Day 223 Thm 1.5). A/H go to FPSAC with no novelty claim. "207b Clio-reviewed" inflation fixed (her read still owed).

## Day 223 PROVE (2026-10-05) — STAR LEMMA == Theorem W (misidentified); W gets a (KF)-free 2nd proof + cold recheck PAID; B-matrix PROVED
- Full stanza in archive (pre-day224-dream). `proofs/2026-10-06-day223-G-by-vertex-deletion.md`, WIP 305bf47. Star lemma = Thm W verbatim. New: (KF)-free W proof, Thm 1.5 lin_e T_k f = (−1)^d[n]/[k]·f(1,…,t^{k−1}) (folklore-level), W cold recheck closed, Thm 7.1 B-matrix. Nodes thmW-second-proof-KF-free, G-by-vertex-deletion-day223, B-matrix-M_kr-closed-form (proved).

## Day 222 dream (2026-10-04) — pointer lines (full stanza in `archive/SUMMARY-2026-10-05-pre-day223-dream.md`)
- G graph half = PRIOR ART: Dołęga 1707.02656 Prop 2.1 (eq 10) + Lemma 2.3, also Josuat-Vergès CJM 2013, Gessel–Sagan, Penrose 1967, Cadogan JCTB 11 (1971). CITE.
  Ours (novel-as-checked): Lead_{λ,(n)} = pref·K_λ (217e Thm B + W + G), Thm F, Thms A/C. Separator I = 2 (Dołęga ⊕) vs (t+2)/(t+1) (⋆).
- Crown `connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md` (character e_k ↦ t^{C(k,2)}; t=0 → Möbius Π_ℓ). t=1 Cayley corollary proved (8f9cac1).
- G′ v=ℓ−κ 35/35 n≤5 (computed; `questions/q-general-mu-lead-flow-forests.md`). FPSAC deadline 2026-11-15, AI declaration mandatory.

## Day 221 (PROVE / dream), 2026-10-04 — pointer lines (full stanzas in `archive/SUMMARY-2026-10-04-pre-day222-dream.md`)
- **PROVE:** Thms G, F proved (`proofs/2026-10-05-day221-lead-cumulant.md`): histories = increasing trees, W telescopes, Lemma 3 tree–graph
  bijection (now known to be classical). Checks 37/37 symbolic, 220/220 exact.
- **Dream:** the proof file had been committed TRUNCATED (5b73f01, 1230 B). It was restored by re-derivation (d32be4d); the W recheck text was lost. Crown
  `connections/2026-10-04-s1-lead-is-a-mayer-cluster-expansion.md` (Mayer/Ursell; t=0 Möbius ↔ Day 214 zeta; DLT flows = increasing trees).
- **Wake 221:** Clio s=1 block-law PDF + DS-from-(N) reply sent. DFK15 1505.01657 Cor 5.18 first-hand MATCH ⇒ Thm C (N)-free. t=0 block
  law LIKELY-FOLKLORE (DLT SLC 32 eq (11)). Conj G/F computed (58/58, 123/123). FPSAC v7 outline.

## Day 220 (wake / PROVE / dream), 2026-10-03 — pointer lines (full stanzas in `archive/SUMMARY-2026-10-04-pre-day221-dream.md`)
- **PROVE:** s=1 edge solved, `proofs/2026-10-03-day220-s1-carre-du-champ.md`. Thm 1: biderivation (order-p Taylor pieces). Thm A:
  v ≥ ℓ−κ. Thm C: equality. Thm B: coarsenings. Thm W: W_k(J)=(−1)^p[n]_t∏[k]_{t^j}/[k]_t. All `proved`; the max(1,ℓλ−ℓμ) guess is FALSE.
- **Dream:** s=1 is an order filtration; two valuations survive lost positivity (n(μ) at s=0, ℓ−κ at s=1). The t=0 law unfolds to the
  inverse HL P→m matrix. (N)-free route via DFK15. Crown `connections/2026-10-03-s1-is-an-order-filtration.md`.
- **Wake:** Clio reply 185aaa3; FPSAC 2026-11-15 recorded as verified (now disputed, Browse 161); biderivation test computed.

## Day 219 dream (2026-10-03) — pointer lines (full stanza in `archive/SUMMARY-2026-10-03-pre-day220-dream.md`)
- H′ scooped (DFK 1908 Thm KNAN). FPSAC frame = DFK 1704 §8.3 "positivity lost", DS survives (crown `connections/2026-10-03-DS-is-what-survives-DFK-lost-positivity.md`). Clio UID 316: (N) statement peer-reviewed, C3-nonsym locator open. Lemma ER proved (no computation). e-basis survivor λ=1^n. Hunch max(1,ℓλ−ℓμ) → refuted and replaced Day 220.

## Day 218 dream (2026-10-02) — pointer lines (full stanza in `archive/SUMMARY-2026-10-03-pre-day219-dream.md`)
- Thm B = DFK 1505.01657 Cor 5.18 (erratum sent, WIP 55f86c6). ι canonical basis dead (mixed signs). DS from (N) in 15 lines (`proofs/2026-10-02-day218-DS-from-N.md`, n≤4). Crown `connections/2026-10-02-transport-sees-valuation-not-integrality.md` (KN integrality is operator-side — confirmed first-hand Day 219). Browse 158: BFJ math/9806151 template; MO 296383, MO 337891 leads.

## Day 217 (wake / 217e PROVE / dream), 2026-10-02 — pointer lines (full stanzas in `archive/SUMMARY-2026-10-02-pre-day218-dream.md`)
- **217e PROVE:** (s,t)-square CLOSED. Lemma R Ψ_{1/s,1/t}=Ψ^{-1}; Thm A (s=∞ → HL P_{μ'}(x;t)); Thm B (t=0 → ωH̃_μ(x;s), now = DFK15); Prop C collapse coefficient (gives Hikita Thm C(ii)); Cor D op form (b). `proofs/2026-10-02-day217e-boundary-of-the-st-square.md`, node `square-theorem-all-edges-day217e`. PDF to Clio (WIP dd35498).
- **217 wake:** (N) folklore-implicit (DFK 1704.00154; BGHT (I.12)(iii); BGLX 1405.0316 Conj 2.1). t=1/s line proved. ⋆-positivity dead in natural bases. GGS OP4 dead as target. MacBeth torsor review sent (fails at Z/8).
- **217 dream:** ι bar-involution hunch (now dead); ∇-avatar novelty search (now moot). Validator: `python3 code/registry_validate.py <registry.json> --proofs-dir /home/agent/projects`; trust enum stale (`sketched`, `peer-claimed`, `checked-sober` flagged, pre-existing).

## Days 215 dream – 216 dream (pointer lines; full stanzas in `archive/SUMMARY-2026-10-02-pre-day217-dream.md`)
- **216 dream:** (Sym,⋆)≅(Sym,·) via 𝒩. Crown: t=1/s is LR × ribbon monodromy (since proved as a corollary, Day 217 wake). Hopf hunch, unregistered: Δ_⋆ = (𝒩⊗𝒩)Δ𝒩^{-1}, so on t=1/s the failure of 𝒩 to be a coalgebra map is R₂₁R. Is it a braided Hopf algebra?
- **216c PROVE:** (N) PROVED for all k. Lemma (I) [e_1(Y),X_1]=(s−1)X_1Y_1 → nonsymmetric Gaussian γ̂X_iγ̂^{-1}=Y^•_i → 207b. Cherednik facts C1–C3 are machine-checked, but their locators are unverified. WIP f223c5d.
- **216b PROVE:** (N) found. Theorem H′ (t→∞ edge = q-Whittaker ωQ′_μ(x;s)). (KF) E_kF = Σ P_{ρ+1^k}(x;t)(Q′_ρ[(s−1)X;t])^⊥F, proved. `proofs/2026-10-01-day216b-theorem-H-prime-nabla-transport.md`.
- **216 wake:** Ψ_s is not a Macdonald *basis* (Groebner [1]), but the *operator* is Macdonald-diagonal. Theorem H's corollary matrix d is the classical e→HL transition (HKKOTY; Kirillov math/9803006 Thm 3.4), so present it as an identification only. A peer's grade comes from their registry, not their review table.
- **215 dream:** Theorem H sober re-read holds. Crown: ⋆ interpolates e-multiplication (s=1) and HL multiplication (s=0); at s=t=0 it is the dominance zeta function. Negative controls need the involution sweep.
- **Browse 156/157:** the arXiv+citation sweep for (N)/H′ is clean. MO/SE work via `curl api.stackexchange.com` (WebFetch is blocked). FPSAC deadline reconfirmed. Hikita 2503.23597 still has 3 citers. GGS has a self-citation 2601.22287 (unchecked vs OP4).

## Days 214 dream – 215 PROVE (pointer lines; full stanzas in `archive/SUMMARY-2026-10-01-pre-day216-dream.md`)
- **Day 215 PROVE: Theorem H PROVED.** The s→0 limit of ⋆ in the b-basis (b_μ = s^{n(μ)}e_μ) is t^{−C(k,2)}·HL e_k-multiplication. Corollary: d_{λμ} ∈ ℕ[t] is the e→HL transition, which is CLASSICAL (HKKOTY; Kirillov math/9803006 Thm 3.4).
  - `proofs/2026-10-01-day215-theorem-H-s0-limit-is-HL.md`. Nodes `theorem-H-s0-star-is-HL-pieri` and `d-equals-hall-littlewood-transition` are proved.
- **Day 215 wake:** d(t) = t^{−n(λ')}⟨e_λ, H̃_{μ'}⟩ computed for n ≤ 7. The DS novelty audit is clean on Hikita (`reading/2026-10-01-DS-novelty-audit.md`). Clio UID 306 endorses (TC), conditional on 207b.
- **Day 214 dream:** at s=t=0, ⋆ = the dominance zeta function (seed Q4); `connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md`.
  - The arc table: 207b e_k⋆e_r, 206b W_r/τ_r, 209 (TC), 212 (★ℓ), 214 DS all lengths. All are proved; review status is in the registry.
  - FPSAC 2027 abstracts are due **2026-11-15** (SLC format, 6–12 pp, AI declaration). `questions/q-fpsac-2027-writeup.md`.
- **Day 214 PROVE:** DS for all lengths, with exact up-set support and val_s c_{λμ} = n(μ). `proofs/2026-09-30-day214-DS-all-lengths-PROVED.md`.

## Days 212–214 (pointer lines; full stanzas in `archive/SUMMARY-2026-09-30-pre-day214-dream.md`)
- **214 PROVE (09-30):** DS for all lengths plus the Theorem 2 stretch (WIP 5ff6da3, b5ccc50).
  - Lemma A: a Gauss-valuation bound. Lemma B: the t=0 peel recursion (Ryser); the Peel Lemma was brute-forced on 10,788 triples with n ≤ 11.
  - Lesson: `feedback_termwise_bound_basis_choice`. Scripts in `scripts/day214/`.
- **Browse 154 (09-30):** FPSAC deadline is live. Wick audit clean. `reading/2026-09-30-browse154.md`.
- **213 wake (09-30):**
  - (TC) and (★ℓ) PDFs sent to Clio (ca17c82; the (TC) node is `two-column-gf-rule`).
  - MacBeth o_ν slices registered peer-claimed (7d58ead).
  - DS length 2 proved from 207b (46b691a, `proofs/2026-09-30-day213-DS-length2-from-207b.md`).
  - Wick bilinearity computed: B_n = (Y−S)(1−X)/(1−1/T) + (X−1/S)(1−Y)/(1−T), `scripts/day213/wick_kernel_check.py`, node `pairwise-kernel-wick-bilinear`.
- **212 dream / PROVE (09-30):**
  - (★ℓ) proved; (Z) is the residue theorem for ∏(w−μ_c)/((w−1)∏(w−λ_c)) (WIP 05666cc).
  - The Day 210 ℓ=3/4 kill test survived with negative controls; the version-A prefactor was WRONG.
  - Day 211: the aha_221 "mismatch" was a float-exponent harness bug, which can only fake NONZEROS (DS caveat in WIP 2d6c02c).
  - Hunch: the pairwise kernel is a Wick contraction (`connections/2026-09-30-pairwise-kernel-is-wick-contraction.md`), so the pairwise shape is NOT novelty evidence.
  - Clio UID 301: W_r and e_k⋆e_r stand.

## Days 205–211 (pointer lines; full stanzas in `archive/SUMMARY-2026-09-26-pre-day207-dream.md`, `…-2026-09-29-pre-day209-dream.md`, `…-2026-09-30-pre-day212-dream.md`)
- **209 dream (09-29):** straightening-free promoted to proved as a corollary of (TC) (WIP 6f00fb9). `connections/2026-09-29-residue-function-is-the-whole-proof.md` predicted P-ℓ; confirmed Day 212.
- **209 PROVE (09-29):** (TC) two-column rule PROVED for all k (`proofs/2026-09-29-day209-two-column-TC-PROVED.md`, WIP 1e92c63). The t=0 one-column law min(Geom(s),μ) was PROVED for all k, r (Day 208).
- **Browse 152 (09-29):** Graf 2511.01114 (Jing operator via a deformed Bernstein operator); KOS 2605.16773 row-product coefficients; BW 2405.00756 has only a self-citation, so the EHA↔AHA dictionary gap is confirmed empty. `reading/2026-09-29-browse152.md`.
- **208 wake (09-26 → 09-29):**
  - (TC) conjectured (fit on Γ_1..Γ_3, blind-exact at k=4,5); straightening-free kill test survived; t=0 corollary proved for all k, r; 12th audit clean. WIP 300eb31.
  - Mail 09-26: Day 207b PDF to Clio; MacBeth answered on cross-equation (c), which is not always solvable (|G|=8, 16).
- **Browse 151 (09-29):** BW 2405.00756 v2 (e_r(X) side); MVP 2407.05362 (t=0 multiline queues, precedent in shape for Q4); MO 411889 contrast (t=0 HL straightening gives one term); Jing 1991 B_n; FPSAC deadline unposted. `reading/2026-09-29-browse151.md`.
- **207 dream (09-26):** the e-basis dodges straightening (`connections/2026-09-26-e-basis-dodges-straightening.md`); t=0 mixture; registry paths and sync fixed (WIP ab8caef/2932947).
- **207 wake (09-26):** k-fold kernel passes k=3,4,5; general formula fit on k ≤ 4 and blind-confirmed at k=5; ₂φ₁ form of F_n (computed n ≤ 6); **DS(r,1,1) PROVED** all r ≥ 2 (`proofs/2026-09-26-day207-DS-r11-proved.md`, WIP e99cb59). Clio M-convexity re-review PDF sent (73bb200/bb48fa1).
- **Browse 150 (09-26):** BW–Orr 2410.13642 Prop 4.2 = stable symmetrizer, §7.2 e_1-only Pieri; prior-art risk list (Shimozono–Zabrocki math/0001168, Venkateswaran 2308.10844, Bhattacharya 2407.14652); Fu–Hu 2609.19608 affine quantum Schur–Weyl (Path 3); FPSAC 2027 Galway Jul 5–9, deadline unpublished; Hikita 2503.23597 still 3 citers. MO blocked for agents. `reading/2026-09-26-browse150.md`.
- **206 dream / 206b PROVE (09-25):** W_r = e_2⋆e_r PROVED; Lemma 1 / τ_r PROVED; the coset symmetrizer is Jing's operator at k=2 (proved), `computed` at k=3.
- **205 dream / 205b / 205 wake (09-25):** W_r was the bottleneck; (L1)-(L4) and Sub-Lemma Z PROVED; τ^(3) closed form (computed). Browse 148: R0 closed (Hikita Lemma 3.1 [+ Cor 3.9]; Browse 148 had quoted Def 3.4 / Lemma 3.3, corrected wake 230).

## Days 190-204 — Hikita ⋆-Pieri arc (pointer lines; full text in `archive/SUMMARY-2026-09-25-pre-day205-dream-prune.md`)
- **204 wake (09-18):** Clio's factorization τ_r = −(q²−1)[r+2]_t(q t^{r+1} − q + t + 1)/(q³[2]_t) verified sober. Prediction 1 at k=3 refuted (superseded by the Day 205 template). Sub-Lemma Z reduced to (L1)-(L4). WIP push 2885dcb.
- **203 dream + PROVE (09-17/18):** R7 identity proved (Newton + intertwiner). Sub-Lemma Z checked-sober. Thibon B_1² = αΔ_2 + αB_1 + 2B_2 is the stable-limit template.
- **202 wake + dream (09-17):** R5 exhausted. R6 (BW 2310.10249) opened then REFUTED (spherical vs level-1). Thibon-Δ_3 corollary RETRACTED. R7 is the sole route.
- **201 PROVE:** Vertex B (Jack) refuted. p_3(Y)-Pieri: 5 r-indep + 2 r-dep coefficients. r-independence comes from Newton cancellation.
- **200 wake:** τ_r closed form. A^{(2)} = p_2(Y) refuted. Five-defect PDF to Clio.
- **196-199:** DS (Dominance-Support) conjecture 22-for-22, leading q^{-n(λ)}. p_2(Y)-Pieri Lemma. D'Adderio route (D_(a) = e_a(Y)) REFUTED Day 197.
- **193-195:** e_3⋆e_r and e_4⋆e_r full closed forms (quasi-Vandermonde P_a). R1 (Stokman–Rains) refuted. BW 2405.00756 MISS. (Re) anchor retracted (AP Thm 38).
- **190-192:** X_{P_2}, X_{P_3}(q,t) via the Hikita recipe. e_2⋆e_2 closed; e_2⋆e_r conjectured (= W_r, still computed only). Clio retraction-of-retraction. MVL/Lemma 2A proved. Browse 141: the e_a⋆e_b (a ≥ 2) slot is open.

## Days 185-188 arc (2026-09-10 – 2026-09-11) — BDI/Hopf and h-basis $(q)$-GF hunches KILLED; retractions sent same day

- **Day 185 PROVE (2026-09-10):** BDI/Hopf $(1+t)$ hunch REFUTED. LHS is length-diagonal (support $\ell \le 2$); Zabrocki H_t exchange is length-shifting composition → different sub-algebras of $\mathrm{End}(\Lambda)$; no dictionary. Registry: `bdi-hopf-analogue-of-1+t = refuted`.
- **Day 185 dream:** BDI/Hopf consolidated as refuted; NC-geode/free-cumulants/FGCCHA triangle surfaces; free-cumulant hunch for $b_k$ queued.
- **Day 186 wake (Rule 11 fire #15):** free-cumulant hunch REFUTED numerically. Speicher-Nica $\kappa(b) = (3,18,228,3414,57051)$ ≠ $a_k = (3,18,282,5268,109647)$. Correct framing: $a_k = \mathrm{INVERTi}(b_k)$ = **Boolean** cumulants of $b_k$ (Milnor-Moore tautology). Silver lining: $\kappa$ is NOT in OEIS — new 4th sequence in Rick's $b_k$ family. Empirical h-basis $(q)$-GF $Z(z) = H_-(z)/(1-K(z))$ found (seed for Day 187 PROVE).
- **Day 187 PROVE (Rule 11 fire #16):** three h-basis $(q)$-GF forms upgraded `computed`→`checked-sober` on $n=1..8$. **All three later killed by Day 188 novelty audit** (SW 2010, Ellzey 2017, AP 2018).
- **Day 187 dream:** FPSAC anchor v1 hung on "manifestly $q$-positive $e$-basis expansion" — LATER KILLED. Two combinatorial proof routes for (Re) queued.
- **Day 188 wake (Rule 11 fire #17):** novelty audit KILLS Day 187 FPSAC anchor. All three forms are literature. Retractions same session to Clio + Robin. Route A (Chow watershed + Hikita Markov specialization) `checked-sober` on $n=1..8$. Multiplicativity check PASS. $\kappa_k$ extended to $k=12$: 3-adic valuations palindromic. OEIS Sequence 3 ($p_k$) hold sent (Clio flagged mod-3 $\%C$ REFUTED with six counterexamples; Sequences 1, 2 unaffected). MacBeth reply sent.

**Feedback memory added:** `feedback_novelty_check_before_writeup.md` (2-for-2 in 48h).

---

## Days 182-184 (2026-09-09 – 2026-09-10) — Fact 8 arc TERMINATES; a_k > 0 PROVED; Sprout ruled out; OEIS package sent

- **Day 182 dream:** Fact 8 pentagon (Days 175–180) checked-sober on Q[E_1,E_2,E_3]. **b_k arc structurally closes.**
- **Day 183 wake:** OEIS package sent to Robin (three sequences: $b_k, a_k, p_k$ — all confirmed new). AGGSZ = Andrews-Gagnon-Gélinas-Schlums-Zabrocki 2505.06941. Sprout SF ruled out.
- **Day 183+ PROVE (arc closes):** $a_k > 0$ PROVED via elementary Lagrange + log-positivity: $A = \vartheta\varphi(A)$, $\log(\varphi/3) = \sum(\ell_n/n)A^n$ with $\ell_n = 3\cdot 2^n + (7/3)^n - 2(5/3)^n - 3 > 0$; hence $\varphi^k$ has all-positive Taylor coeffs, hence $a_k > 0$. **AGGSZ FGCCHA structure for $b_k$ now unconditional theorem.**
- **Day 183 dream:** 40-day arc (Days 143→183) structurally closes with 2 theorems on $b_k$. Stanley-Gasharov DISPROVED (Matherne-Morales + Wang-Zhang-Zhao 2607.*). Restricted modular law + path graphs = surviving positive program. New arc queued: $(q,t)$-lift of (†).
- **Day 184 wake:** Q8(b) closed via FP_coeffs.py. **$b_k$ is log-CONVEX** (not concave; growth ratios → ~26-30). Wang-Wang 2608.22184 cites SW 2016 correctly (Browse 137 was WRONG, Browse 136 was right). Clio reply PDF sent (D1/D4 corrections, §4 e=2 parity WITHDRAWN). MacBeth referee reply. **BDI/Hopf $(1+t)$ hunch registered** — later refuted Day 185.

**Feedback memory added:** `feedback_convolution_vs_composition.md` (Day 185), `feedback_log_positivity_lagrange_kernel.md` (Day 183).

---

## Days 172-181 (2026-09-06 – 2026-09-09) — Fact 8 gap closed via MVL; Theorem B peer-verified by Clio; Day 180 §4 WITHDRAWN

- **Day 172 dream:** E_2-shift reduced to (A) via factorial-Schur stability.
- **Days 173-175:** Fact 8 arc. Day 175 D_n closed form via shift operator ($d_k = 2^k + 2k - 1$); Day 174 (A) reduced to (A′) 3-term recursion / ODE.
- **Day 176 wake:** Fact 8 gap SHRUNK to polynomial-in-n structural claim.
- **Day 176/177 PROVE:** polynomial-in-n reduced to Claim (X); new stability identity PROVED (7/7 sober).
- **Day 178 wake:** Theorem B PEER-VERIFIED by Clio (UID 257). Claim (X) reduced to arity-0.
- **Day 179 PROVE:** Lemma 1 proved on Q[E_1,E_2]; Lemma 2 ρ-drop mechanism identified.
- **Day 180 PROVE:** LEMMA 2-A PROVED via Master Vanishing Lemma. **Fact 8 → proved on Q[E_1, E_2] slice.**
- **Day 181 PROVE:** (SC) attempt returns `checked-sober`. **a_k ≡ b_k (mod 9) PROVED.** Day 180 §4 Wick claim WITHDRAWN (Clio refutation).

**Feedback memories added:** MVL residue+scaling template, top-ρ via Newton + $Q_k^{top}$, operator-stability beats trajectory-stability, second-differences reveal shifts.

---

## Days 165-171 (2026-09-04 – 2026-09-06) — Route B closed; Theorem B PROVED (year-arc terminates)

- **Days 165-167:** Σ_0 IS algebraic (closed form); three-way collapse (Σ_0 ⟺ $R^{(-1)}$ ⟺ Theorem B); BM&J catalytic-variable identified as community-standard tool; Prop 3 PROVED via weight-grading. Route A closed.
- **Days 168-169:** Route B closed layer-by-layer via extended Riccati. $L_0$, $L_{-1}$ closed forms; $F_{-1}$ 3rd-order ODE derived.
- **Day 170 (CROWN):** **THEOREM B PROVED** unconditionally. Prop 3 verified as ring element; 18 $T^3 H^2 K$ missing term identified and fixed. **Year-arc terminates.** Rule 11 fire #12.
- **Day 171 wake:** post-arc plumbing; Tom-Vailaya verdict.

**Feedback memories added:** `never_trust_the_writeup.md`, `prescribed_import_test_before_trust.md`, `weight_grading_beats_prop2.md`, `check_enumerative_combinatorics_literature.md`.

---

## Days 143-164 (2026-08-28 – 2026-09-04) — b_k SOLVED; H2 PROVED; ψ closed form; Narayana; Riccati era

**Day 143:** Quadratic identity $(1-2F(\tau))^2 = 1+4A(\tau)$ PROVED (FPSAC §5 Thm 3.7). $b_k$ = NC-geode $k=-1$ slice.
**Day 148 CROWN:** $b_k \equiv 0 \pmod 3$ PROVED. **Rule 11 born.**
**Day 149:** (H2) $\deg_{E_3}[T^n]H \le \lfloor n/3\rfloor$ PROVED. $\Psi(s_\mu) = \mathfrak s_\mu$ (Schur → factorial-Schur), $\tau = $ mult by $e_3$.
**Day 152:** ψ closed form PROVED (degree 5 minimal polynomial); ν-system introduced.
**Day 154:** **Narayana at $E_3 = 0$ PROVED** (Theorem C.4). González D'León-Wachs external validation (Rule 12).
**Days 156-164:** layer-by-layer closed forms via Riccati era ($X^{(0)}$, transverse derivatives, $\bar D$ closed form).

Details in dream journal + `proofs/2026-08-{28..31}-*.md`, `proofs/2026-09-{02..04}-*.md`.

---

## Days 22-142 (deep archive, one-line pointers)

- **Days 130-142 (β' construction week):** F = A·B EGF; **Full Density Theorem** (Day 133); Ψ_b-global sign (Day 136); $x_3=0$ product formula; Interior closure; Leading closed form; Frobenius identity $L \cdot F_P = F_P \cdot X$.
- **Days 116-129:** Lift Theorem $S_j = \sum K_{\mu',(2^j)} s^*_\mu$; operator formula $\Psi(f) = T(fV)/V$.
- **Days 104-115:** H3/H5 anchors → (★) verified $R \le 5$; Sahi-Okounkov interpolation; Master Argument.
- **Days 91-101:** β'(c) 2-adic launch; digit-sum formula; G1/G3 closed.
- **Days 78-89:** Polytope Lean closure; $M_j = \langle s_\lambda, e_2^j p_1^{n-2j}\rangle$.
- **Days 22-77:** BDI → DIII polytope program; Theorems E/F/G; Lean bucket-0 = sl_2.

---

## Live registry (Day 212 dream state; the registry JSON in `work-in-progress/registry/` wins over this list)

**PROVED (major, chronological):**
- b_k arc: Day 148 b_k ≡ 0 mod 3; Day 149 (H2); Day 152 ψ closed form; Day 154 Narayana at E_3=0; **Day 170 Theorem B**; Days 180/182 Fact 8; Day 181 a_k ≡ b_k mod 9; **Day 183+ a_k > 0**.
- Hikita ⋆ arc:
  - Day 205b (L1)-(L4) and Sub-Lemma Z.
  - Day 206b W_r = e_2⋆e_r, and Lemma 1 / τ_r.
  - Day 207 DS(r,1,1).
  - **Day 207b e_k⋆e_r all k**, with instances e2⋆e2, e3⋆e2, e3⋆e3, e4⋆e3, e4⋆e4, e4⋆e5, and e3/e4⋆e_r for all r.
  - Day 208 t=0 one-column corollary, all k, r.
  - **Day 209 (TC) two-column rule, all k**, and as a corollary straightening-free at the GF level (`hikita-star-two-column.json`).
  - **Day 212 (★ℓ) ℓ-column rule, all k, ℓ** (node `ell-column-rule`), with closing identity (Z) (node `ell-column-closing-identity-Z`).
  - Peer-reviewed by Clio (UID 301): W_r and e_k⋆e_r.

**CHECKED-SOBER:** (SC) (Day 181).

**COMPUTED:**
- The (TC) e-expansion tail.
- DS for length ≥ 3 beyond (r,1,1): 22-for-22 on Day 196, plus the Day 211 clean-engine length-3 runs. The Day 196 nonzero/sharpness claims are unaudited (float bug).
- DS length 2 (`ds-length-2-slice-is-SP`): promotion candidate as a corollary of 207b.
- Exactness of min(a,b)+1 (unaudited, same float-bug caveat).
- ₂φ₁ form of F_n (n ≤ 6).
- (1−t)³R_α = QJ(α) at k=3.
- τ^(3), τ^(4).
- X_{P_2}, X_{P_3}(q,t).
- κ_k (k ≤ 12).

**HUNCH (unregistered):** (★ℓ) = Wick contraction for a free-field realization (`connections/2026-09-30-pairwise-kernel-is-wick-contraction.md`). Register it after the B_n check.

**OPEN (major):**
- Explicit e_k⋆e_λ coefficients, DS at length ℓ, τ^(k), and t=0 at ℓ columns (`questions/q-ek-star-elam-extraction.md`).
- Novelty audit of (★ℓ) and (Z), including a free-field / DIM search.
- GGS 2502.16113 Open Problem 4 vs (★ℓ).
- s_λ⋆e_r (Hikita flags it as open).
- Carlsson–Mellit ↔ Hikita dictionary (GMRWW 2504.06936: OPEN).
- Tom–Vailaya (q,t)-lift.
- **FPSAC 2027 abstract.** Anchor: e_k⋆e_r + (TC) + (★ℓ) + the t=0 law. Deadline unposted; recheck mid-October.

**REFUTED / DEAD (curated):**
- Day 207 dream: "Q_α straightening is the core" (wrong in spirit).
- Day 202 R6 (BW 2310.10249).
- Day 201 Vertex B.
- Day 200 A^{(2)} = p_2(Y).
- Day 197 D_(a) = e_a(Y).
- Day 195 BW 2405.00756 v1 MISS. That verdict is on **v1 only**; v2 needs recheck.
- (Re) anchor (AP Thm 38).
- Day 194 Stokman–Rains.
- Day 188/189 novelty kills.
- Day 185 BDI/Hopf.
- Day 186 free-cumulant.
- Day 180 §4 Wick.
- Stanley–Gasharov (external).

---

## Identity + collaborators

Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**ALLOWED_RECIPIENTS:**
- **Robin Langer** (langer.robin@gmail.com) — daily email rule active. CC Clio on substantive.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review. Day-190 correction PDF drafted.
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred.
- **Alastair Poole** — thread paused.
- **Scot MacBeth** (scot.macbeth20) — active thread (revision v2 §5).

**Naming:** Rick's pair (so(2N), gl(N)) = Cartan type **DIII**, not BDI.

---

## Streak

- Days 104–212: ~105 wake sessions.
- Arc 2 (b_k/FGCCHA, Days 143–183) closed with a_k > 0.
- Arc 3 (Hikita ⋆-Pieri, Days 189–212): e_2⋆e_2 (191), e_3/e_4 closed forms (193/195), DS launched (196), W_r (206b), **e_k⋆e_r all k (207b)**, **(TC) two-column (209)**, **(★ℓ) ℓ-column (212)**.
- Rule 11 scorecard: 27-1 (last recorded at Day 203; no new fires logged since).

---

## Calibration rules (top hits — full history in git)

- **Rule 11 (Day 148, sharpened Day 161, extended Day 188):** *Unfold the definition before you decorate it.* Now fires in three rooms: derivation (unfold beats import), writeup (novelty audit beats hype), retraction (locator audit beats novelty audit).
- **Rule 12 (Day 149):** *Filtration whose extreme layer τ cannot move.* Externally validated by GDL-W, Marberg, Qiu-Zhang.
- **Rule 13 (Day 150b):** *Name the knob, not "up to normalisation."*
- **Rule 6 v2 (Day 143):** *Object hygiene between frames.*
- **Rule 9 (Day 141):** *Change coordinates when machinery balloons.*
- **Rule 10 (Day 147):** *Integrality-as-target.*
- **Pre-register predictions** (Day 151). **Compute-before-typeset** (Day 157). **Operator respects slice** (Day 159). **Check enumerative-comb literature (BM&J school)** (Day 166). **Prescribed imports need 30-min fit-check** (Day 169). **Weight-grading beats constructive machinery** (Day 167). **Never trust the writeup, only running code** (Day 170). **Convolution ≠ composition** (Day 185). **Log-positivity of Lagrange kernel = unfold for algebraic-GF positivity** (Day 183). **Novelty check same session as writing** (Day 188). **Verify locators in retraction letters** (Day 190). **Residue before machinery** (Day 209 dream; 3/3 by Day 212): I keep predicting straightening or q-Saalschütz, and the proof keeps needing only one rational function plus the residue theorem. **Know the direction of a bug** (Day 212 dream): a cancel-failure can only fake nonzeros, so "vanishes"/"support ⊆" verdicts survive it. **Outbound first in wakes** (Day 212 dream): two wakes died at the 600 s background ceiling with the email unsent.

---

## Compression log
- 2026-10-16 Day 242 dream: Browse 184–186, Day 241 PROVE/dream, Day 242 PROVE, Wake 241–242 stanzas → pointer lines; new Day 242 dream top block (archive `archive/SUMMARY-2026-10-16-pre-day242-dream.md`).
- 2026-10-09 Day 231 dream: Days 229–230 stanzas → pointer lines (archive `archive/SUMMARY-2026-10-09-pre-day231-dream.md`).

- **Day 217 dream (2026-10-02):** 367 → ~285 lines. Day 215 dream through 216 dream stanzas collapsed to pointer lines. Day 217e/217 wake were tightened. A Day 217 dream top block was added. Pre-prune copy: `archive/SUMMARY-2026-10-02-pre-day217-dream.md`.
- **Day 212 dream (2026-09-30):** the Day 212 PROVE and Day 209 dream blocks were merged into one Day 212 dream top block. Day 209 and Browse 152 moved to pointer lines. Live registry refreshed. Pre-prune copy is in `archive/`.

- **Day 209 dream (2026-09-29):** the Day 207 dream, Day 208 and Day 209 stanzas were merged into one top block. Day 207 dream and 208 moved to pointer lines. Live registry refreshed to the Day 209 state. Pre-prune copy is in `archive/`.

- **Day 207 dream (2026-09-26):** Day 205–207 stanzas collapsed to pointer lines. The Live registry was rewritten from its stale Day 196 state; it had listed e3/e4⋆e_r as computed and their analytic proof as open. Pre-prune copy is in `archive/`. Two questions were closed (q-ek-star-er-via-k-fold-kernel, q-DS-211-promotion).
- **Day 205 dream (2026-09-25):** 90 KB → ~22 KB. Days 190-204 collapsed to pointer lines; the full pre-prune text is in `archive/`. A Day 205 dream stanza with the proof-chain table was put on top. Stale D'Adderio OPEN item removed (refuted Day 197). 4 closed questions moved to `questions/closed/`.

- **Day 196 dream (2026-09-16):** SUMMARY.md +~40 lines (Day 196 dream stanza at top; Live registry updated Day 195→196; Streak + Rule 11 scorecard bumped to 22-1; DS-related fields updated in OPEN and COMPUTED sections). No compression yet — Days 191–195 stanzas preserved in full detail.
- **Day 195 wake (2026-09-16):** SUMMARY.md +~110 lines (Day 195 stanza inserted at top; Live registry updated to Day 195 state with SP/BW/AP-Thm-38 additions; Streak + Rule 11 scorecard bumped to 21-1). No compression yet — Days 191–194 stanzas preserved in full detail.
- **Day 191 dream (2026-09-11):** SUMMARY.md 1633 → ~280 lines. Days 165-184 arc collapsed to arc-paragraphs; Days 130-142 β'-week compressed to bullets; Days 22-129 deep archive kept as pointers. Day 191 PROVE + Day 191 dream + Day 190 wake preserved in full detail (fresh work). Registry section rewritten to reflect post-Day-183 state (arc closed) + Day 190-191 additions.
- **Day 175 dream (2026-09-07):** Quadrilateral collapse crown jewel. Rule 11 scorecard arc-2: 3-0 partial.
- **Day 170 dream (2026-09-05):** Theorem B PROVED stanza added. Days 158-169 arc paragraphs. 1039 → ~340 lines.
- **Day 161 dream (2026-09-03):** 736 → 250 lines.
- **Day 140 dream (2026-08-27):** 675 → 250 lines.
- Prior: Days 118, 127, 133, 136, 138, 157, 159.


## File hygiene notes

- **sources.json** `read` paths are now `memory/reading/…`, resolving against the projects root (Day 207 dream fix). Use that prefix for new entries.
- **Registries.** Two copies exist, `work-in-progress/registry/` (pushed) and `proofs/registry/` (local). They were synced Day 207 dream. The WIP copy is canonical; copy local → WIP only when the local file is newer, and check mtimes before copying.
- `rick-research` = the `/home/agent/projects` repo itself, committed every session (e.g. 31329e6, 0591776 Day 242). The old "stale since 09-16" flag was itself stale; dropped Day 242 dream.
- `connections/` ~249 files; the pre-Day-100 β' files are prune-to-pointer candidates.
