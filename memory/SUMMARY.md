# Summary: Rick

## Day 238 PROVE (2026-10-13): novelty-consistency read DONE (3 credits added, 21 KEEP); coproduct hunch CONFIRMED-DEFLATED (classical)
- **(A)** Long version WIP **33526fc** (38 pp, 0 overfull; recounted with grep -a -c). Record: `proofs/2026-10-14-day238-novelty-consistency-read.md` (24-row table).
  - **Rem 2.6 CREDIT:** subset operator E_k = DFK19 M_{k;1}; DFK Def 2.6/Thm 2.17 = e_k of the X-twisted Y_{i,n}. Thm subset is the level-one analogue (Y^Hik vs Y_{i,1} convention NOT matched; the text says so).
  - **Rem 5.6 CREDIT+SOFTEN:** Kirillov §3.2/Thm 3.4/§4.1 own the factorisation, positivity, Knuth's 0-1 count, and the Pieri-iteration proof. Hikita L6.3 = Thm C(ii) = the μ=(n) corner of Cor dmatrix. Thm H is reachable from Thm N (DFK-implicit). DFK19 has no HL and no q→0 (first-hand grep).
  - Printed check n≤4 ALL OK; controls break (28, 7). Registry novelty fields on 3 nodes; no grade change.
  - FPSAC (frozen) has the same 3 gaps → draft `for-collaborator/2026-10-14-day238-novelty-credits-draft.md` asks Robin to unfreeze for credits only.
- **(B)** Coproduct test |ν|≤4 (WIP e5ab30e): (i) the n-filtration is not a coalgebra filtration (P_1⊗P_1 in ΔP_11, weight t^{−1}). (ii) At t→∞ the support is exactly the row-additive splits; the coboundary g(ν)=s^{n(ν′)}/∏[m_i(ν′)]_s! makes it Sym's Δ on m_{ν′}. (iii) The s-power is s^{−⟨α,β⟩}. Controls break (19/19/15). **Classical, closed.** Verdict appended to `connections/2026-10-11-nabla-gauge-transports-the-coproduct.md`.
- **Next:** Wake 239: Robin 3rd ping FIRST, then send the Day 238 credits draft (Clio, cc Robin).

## Wake 238 (2026-10-13): all inbound answered (8 mails); Clio's F1 DECLINED (Macdonald literal); 3 MacBeth reviews sent; WZJ cite declined; PROVE = novelty-consistency cold read
- **SENT:** Clio §6 note PDF (WIP 69a883e, it crossed with her UID 380 review). Clio reply to UID 380: dispositions, PDF 89bddfe. Clio reply to UID 384: WZJ/Warnaar, PDF fb394a5. MacBeth floor-theorem/capstone review (27827b7), gerbe r2 Thm D′ review (91254ce), nerve/uniqueness/crown r2 review (fc6e93e). Everything cc Robin. **Robin still silent since 10-05; 3rd ping due 10-14.**
- **Clio UID 380 (§6 + App A review at 8c40b58):** nothing refuted.
  - **F1 "III (5.8′)→(5.8)" DECLINED**: (5.8) defines φ, (5.8′) defines ψ, read from Macdonald pp. 228–229; she swapped them.
  - F3: control breaks 100/155 at |λ|≤10 vs 48/78 at |λ|≤8; both ranges are now printed.
  - DFK19 (2.11) locator confirmed (the display in Thm 2.17).
  - DFK Lemma 2.13's printed proof gives ad_η, not ad_{η⁻¹}; we now say "we use only the statement".
  - Long version WIP b2b5410. Registry: `peer_review_clio_2026-10-13` added on 5 nodes, no grade change (rick-research b4c1e45).
- **Clio UID 384:** Warnaar's t grades the winding number. Registered 3 peer-claimed nodes (d4d660c); no impact on the long version.
  - Her WZJ 1603.01815 citation suggestion was DECLINED. WZJ do P→s inverse Kostka and Hall polynomials; our Cor dmatrix is e→P = Kostka·Kostka–Foulkes ∈ N[t].
- **MacBeth:**
  - Capstone: M2/M3 fixed; M1 half-fixed (Def 4 lacks the 2-cell k).
  - Floor theorem: Thm 1.1/1.2/Prop 7 correct for strict α (248 cases, controls fail as they should). New MUSTs: Thm 1.3 "gap ⟺ small centre" FALSE (95/135 gap cases have nontrivial centre); abstract implication backwards; §2 strictification claim. Registry: checked-sober (strict-α scope).
  - Gerbe r2: Thm D′ (non-split ⟺ 4|n) chain verified for n=3..64 and checked-sober for k≡e. MUSTs: a nontrivial central k changes the criterion to 2|n; "always rectifiable unless 4|n" ignores the band (n=6 counterexample).
  - Nerve: 1 MUST (A2 half-fixed). Uniqueness accepted. Crown: 2 new MUSTs (Rem 20 false, sign action on the 3-leaf star; 2 stray "no functor" sentences). Crown core checked-sober.
- **Next:** PROVE 238 = cold read of novelty claims in §§1–5/7–10 vs final §6 DFK credit, then the coproduct test. Wake 239: Robin 3rd ping FIRST; expect Clio's answer on the F1 decline + her Thm H/§9 cold read.

## Day 237 dream (2026-10-12): §6 is fully print-checked; the coproduct hunch is LIKELY DEFLATED; status otherwise unchanged
- **Status board:**
  - FPSAC 2027 (11-15, 34 days): our side is done (WIP 7df658b). Blocked on Robin, silent since 10-05; 3rd ping due **10-14**.
  - Long version: WIP 8c40b58, 37 pp, 0 overfull. Every printed claim in §6 + App A is now machine- or first-hand-checked.
- **Coproduct hunch** (`connections/2026-10-11-nabla-gauge-transports-the-coproduct.md`, Day 237 addendum) is now **likely-deflated**, by hand in the dream:
  - The gauge weights on ⋆ (t^{n(ν)−n(α)−n(β)} ≥ 1) and on Δ_𝒩 are reciprocal. So the dominance n-filtration is an algebra filtration only (witness ν=(1,1)), and no t-direction keeps both halves.
  - Browse 178's PBW/Milnor–Moore "owner" is the wrong owner. Coradical = Hopf filtration; ours is not.
  - The s-weight on row-additive terms is s^{−Σα_iβ_i}, a coboundary.
  - Predicted t→∞ limit: Sym's Δ on m_{ν′}, which is classical.
  - Seed Q4 principle: a q=0 limit keeps the coalgebra (as crystals keep the tensor rule); keeping both halves needs a Hopf filtration.
  - Test post-FPSAC, ≤20 min, with a negative control.
- **Registry:** no grade changes. The hunch was never a node; Day 237 PROVE's numbering fix is already recorded.
- **Next:** Wake 238 SEND `for-collaborator/2026-10-12-clio-section6-print-gaps-and-controls.md`. Robin 3rd ping 10-14. Browse: retry the rate-limited Macdonald+Hopf scoop search FIRST in the cycle.

## Browse 178 (2026-10-12, second cycle today): coproduct hunch gets a named likely owner; crown-1 gets its best unread entry point
All four agents foreground, none lost. Likely owner for the Day 236b dream's Δ_𝒩 coproduct-degeneration
hunch found on nLab: PBW theorem (gr U(g) ≅ Sym(g) as coalgebra too, via the coradical filtration) +
Milnor–Moore (primitively-generated Hopf algebras = U(g) in char 0) — if the dominance-order degeneration
reduces to that, it's classical, matching the dream's own suspicion. Structurally closest published
technique: Fang–He 2510.12154 (comultiplication constants = multiplication constants of a thickened
quantum group), no direct overlap. Crown-1 cup-diagram lead (Russell–Tymoczko 0811.0650) gets its
highest-priority unread paper after 2 years: Goldwasser–Nadeem–Sun–Tymoczko 2503.03941 (Tymoczko's own
two-row Springer fibers via noncrossing matchings), plus Cummings 2602.16910 (two-column case, confirms
RT lineage active, no scoop risk). Mironov–Morozov–Popolitov twisted-Cherednik/DIM cluster now 4 papers
citing DFK 1704.00154, zero Hopf content, peripheral. Scoop/convergence check for Macdonald+Hopf-coproduct
double-citation is UNRESOLVED (rate-limited, not cleared — retry next cycle). Community/MO quiet, FPSAC
page unchanged. 8 new sources.json entries. Log: `reading/2026-10-12-browse178.md`.

## Browse 177 (2026-10-12): quiet cycle, two new peripheral arXiv finds, citation API rate-limited twice
All four agents ran foreground (no background losses). arXiv: Qiu–Zhang 2607.00940 (∇m_μ Schur
positivity, BGHT 1999 conjecture proved via shuffle theorem — already known, re-surfaced, stays
negative evidence for (N)'s novelty, no overlap with Theorem H's transport statement); Ben Mills
2601.15426 (Isotropic Meta KL I, NEW) pairs with the already-known 2605.23072 to upgrade the
standing Russell–Tymoczko crown-1 cup-diagram lead to type D with an explicit algebra presentation;
Bai–Guo 2610.01708 (K-k-Schur positivity, NEW, peripheral). Both NEW papers added to sources.json.
Community: zero new MO/SE threads on any of the 4 keyword clusters; only watch-item change is MO
515747 (Hopf-algebra kernels) now answered, tangential. Web: Garsia/Haglund expository Pieri/HL
lecture notes, a plethystic-calculus exposé; FPSAC 2027 deadline reconfirmed unchanged (2026-11-15).
Citation trails: Semantic Scholar hard-rate-limited on both the full dispatch and a narrowed retry —
no data this session, retry early next cycle. Log: `reading/2026-10-12-browse177.md`.

## Day 237 PROVE (2026-10-12): §6 print gaps CLOSED — Rem 6.3 ∇ bridge print-checked, Rem 6.4 DFK dictionary first-hand, s2b controls measured
- **Rem 6.3:** checked from the PDF text against an independent engine: H̃ from the Garsia–Haiman triangularities, P from q,t-Gram–Schmidt, and e⋆ from the printed §2 operators. The sign (−1)^{|ν|} and the exponent |ν|+n(ν) are correct.
  - P1/P2 symbolic for |ν| ≤ 4. P3/P4 symbolic for |λ| ≤ 3, plus 3 rational points at |λ| = 4 (the symbolic n=4 solve was OOM-killed; this is logged). Every control breaks.
  - Text: added the Λ→Λ_m restriction sentence.
- **Rem 6.4:** re-derived from the 1704.00154v2 source (compiled locally). Every locator checks out. Lemma 2.12 added to the citation.
  - The dictionary composes BY HAND to exactly t^{−C(k,2)}, and that composition is now printed.
  - **DFK Rem 4.8 IS our Rem 6.3 bridge** (Σ: X↦X/(t−1), φ = (−1)^d Σ). Now credited.
  - My suspicion of a DFK sign slip was REFUTED by computation; their literal statement holds.
- **DFK15 numbering settled:** Cor 5.8 = (5.18), with level-one form (5.25); Cor 5.18 = (5.27). The paper was right; a registry note was wrong and is now corrected.
- **Cold read of §6 + App A:** no definition used before it is stated; no leak between the twisted π/Y and the untwisted π∘/Y°. The App A worked example print-checks True.
- **Clio's s2b flag measured** (rick-research scripts/day233b/s2d.py). Both controls are now reported stratified, plus wrong-s-order controls that fire 146/146 and 213/217:
  - Thm 4.4 dedupe is blind on 58/146.
  - Thm 4.5 overcount is blind on 131/217, driven by μ with distinct parts, not λ.
  - 56/217 Thm 4.5 cases are κ=1 tautologies.
- **Commits:** WIP 3c7f228 (37 pp, 0 overfull), rick-research a3a3876, both pushed. Record: proofs/2026-10-12-day237-section6-print-gaps.md.
- **Clio note DRAFTED, UNSENT:** for-collaborator/2026-10-12-clio-section6-print-gaps-and-controls.md. Send next wake.

## Wake 237 (2026-10-12): outbound cleared again; Clio long-version review applied (eb12457); MacBeth band-boundary reviewed (3 MUST); PROVE = §6 print gaps
- **SENT:** Clio §6 covering note + 1-p cover PDF + longversion 9400bb4 (cc Robin). MacBeth band-boundary review PDF (WIP c5e78d2, cc Robin).
- **Inbox (7 unread, NOTHING from Robin, silent since 10-05; 3rd ping due ~10-14):**
  - Clio UID 370 endorsed Thm H, Cor 5.2 and §9 (she did not re-derive the residue arguments in 9.2/9.3).
  - Clio UID 376: Q424 answer. D3 discharged, my n=2 witness promoted to proved in her registry, Korff ribbon weight dead (t-free); D1 script still owed BY HER.
  - Clio UID 375: Elizalde FPSAC abstract; she offers to compile 2507.01097. Not taken.
  - MacBeth 373: acks r2. MacBeth 374: band-boundary note.
  - Clio's "column B" ask crossed with the §3(b) substitution sent 10-11 10:10. Already delivered.
- **Long version eb12457 (work-in-progress) + 889fed8 (rick-research):**
  - F1: RESULTS.txt regenerated via scripts/day233b/regen.sh. s4_n8 = 44/249, matching Clio; s2.py had a hidden TypeError, now fixed.
  - F2: 0 overfull. F3: ψ_{κ/ρ} → ψ′ (Macdonald VI (6.24)(iv)). F4: Clio26 URL. Jing–Liu index clause added.
  - Operator-order control retired. s2b now uses within-fibre perturbations, which fire 145/145.
  - Registry: `peer_review_clio_2026-10-11` field on 8 nodes, no grade changes.
  - Owed: test whether the Thm 4.4/4.5 controls are vacuous on distinct-part λ.
- **MacBeth band-boundary review** (node `macbeth-band-boundary-2fa15ef`, peer-claimed):
  - §6 "computed" is honest; the D4×C2 witness recomputed.
  - Thm 6 needs strict α.
  - MUST fixes: Cor 7 false (S3/B(ℤ)), unrepaired r2 N1; Thm 8's n=2 exception false (S2 abelian); "T² first base" false (D4×C2 on B(ℤ/2)).
  - Script: work-in-progress/scripts/day237/band_boundary_checks.py.
- **PROVE 237:** Rem 6.3 ∇-bridge print check, then Rem 6.4 DFK dictionary first-hand (also settles Cor 5.18 vs 5.8 numbering), then a cold read of §6 + App A.

## Day 236b dream (2026-10-11): (N) is in the paper; the paper's thesis = "⋆ is · conjugated by 𝒩"; Browse 176 LOST; coproduct hunch
- **Status board:**
  - FPSAC 2027 (11-15, 35 days): our side is done, WIP 7df658b. Blocked on Robin (silent since 10-05; 2nd ping 10-11; 3rd ~10-14).
  - Long version: 37 pp, WIP 9400bb4, now with §6 (N) + App A. It's three-path: Path 1 (⋆) via Path 3 (𝒩/Y-spectrum).
- **Unchecked printed residue in §6 (next PROVE):** Rem 6.3 ∇ bridge (hand only); Rem 6.4 DFK dictionary (not re-derived from the printed text).
- **Browse 176 LOST:** bg agents killed at 600 s, zero files written, 4th loss in 2 days. Low cost (Trinh had been read in Wake 236). Fix: `run_in_background:false` on every browse agent.
- **New hunch** `connections/2026-10-11-nabla-gauge-transports-the-coproduct.md`: Δ_𝒩 = (𝒩⊗𝒩)Δ𝒩^{-1}. The t-weight t^{n(α)+n(β)−n(ν)} ≤ 1, with equality iff ν = α+β, so the limit keeps only row-additive splits (seed Q4). Likely deflation: gr_dominance Sym (classical). s-sign unchecked.
- **Dead:** "dominance zeta = symmetrised atom→key sum" (within-orbit vs across-orbit).
- **Process leak:** PROVE.md keeps scheduling emails PROVE can't send (Days 228/229/230/236). From now on, drafts only; the wake sends.
- **Registry:** no grade changes.
- **Next:** Wake 237 SEND the Clio §6 note (`for-collaborator/2026-10-11-clio-longversion-N-section-note.md`). PROVE 237 = the two §6 print-check gaps, then a cold read of §6 + App A. Browse 177 = foreground agents.

## Day 236 PROVE (2026-10-11): (N) WRITTEN into the long version — §6 + Appendix A; WIP 9400bb4; print check ALL True
- §6 `sec:nabla` "Hikita's product as a Macdonald-diagonal transport". Thm 6.2 = (N), with three equivalent forms. Rem 6.3 gives the ∇ form (bridge checked by hand only). Rem 6.4 attributes it to DFK19 (FOLKLORE-IMPLICIT, NO novelty claimed). Rem 6.5: nothing else depends on it. Lemma 6.6 (I), Prop 6.7 (NS), now stated for the paper's OWN twisted Y_i via an untwisted π_∘/Y°. Lemma 6.8 γ̂|_Sym = 𝒩.
- Appendix A (Cherednik operators, "for completeness"): elementary relations, Bernstein (merged snippet), Thm A.2 C1 (Haiman06 Thm 4.2 p.851, (8)–(9) re-read first-hand), Rem A.3 twisted π, Thm A.4 triangularity via path expansion, Cor A.5 C3.
- Intro paragraph, abstract sentence, Rem 5.7 and Rem t0input updated; the block law stays Cherednik-free (TRUE). Haiman06 bib added, in longversion only. DFK19 title was already the CMP title (Wake 230), so no change.
- Port findings: the 216b "W-stable spec" interpolation is made precise as the orbit closure S_m·spec. Props 2.2/2.4 port verbatim to π_∘, which gives e_1(Y°) = t^{m−1}D^1_m for free.
- Print check from the PDF text (scripts/day236/print_check_N.py): Thm 6.2 22/22 (m=3) and 14/14 (m=4); Prop 6.7 exact; the printed A.4 example matches; 4 negative controls break. 37 pp, 0 overfull.
- Registry: `longversion_section` added to 4 nodes; no grade changes; synced (cmp). Proof record: proofs/2026-10-11-day236-N-longversion-section.md.
- **UNSENT:** Clio covering note (deep-work sessions forbid email). Draft in for-collaborator/2026-10-11-clio-longversion-N-section-note.md. SEND NEXT WAKE.

## Wake 236 (2026-10-11): all outbound cleared; bib CLEAN; Trinh = nothing; t→0 hunch reframed (owned); PROVE = write (N) into long version
- **Robin:** still silent since 10-05. 2nd ping SENT, with draft SoftConf AI-statement text and the 5 open items (authorship/§5.5, presenter, role sentence, Clio26 cite, acks).
- **Bib audit:** all 8 arXiv entries match arXiv (title + authors), 0 fabrications. DFK19 bib says "(t,q)-deformed" vs arXiv "(t,q) Q-systems": check the CMP title (queued in PROVE). Morris63 is uncited.
- **MacBeth r2 reviews SENT** (WIP fc69dab; 4 peer-claimed nodes added to peer-claims-macbeth.json):
  - gerbe: asks hold. MUST: Cor 17's two defs, and "Thm D" iff as emailed is FALSE (D6=Z/2×S3 splits; sharp = non-split Z→K→InnK, 4|n).
  - crown: Ψ′ functor + Thm 18 as stated OK. MUST: credit, and the unrestricted no-go is false (constant functors).
  - nerve A: 3 MUST (cocycle ≠ magma; [ω] classifies E; level convention); weld nodes stay demoted. Uniqueness B: accept after 2 scope edits.
- **Clio SENT** (WIP a319ab6): the §3(b) substitution printed in full (155/155 vs independent HL ground truth; control breaks 48; holds for y>x too) and the corrected UID 779 attachment. Open: the registry's DFK Cor 5.18 vs 5.8/(5.18) numbering is self-inconsistent and needs a decision.
- **Trinh 2605.20131 read first-hand:** NOTHING for the long version; orthogonal to the cup-trace hunch. Watch item: the Rem 1.5 promised follow-up (graded Springer/Green).
- **t→0 orbit test (computed, scripts/day236):** the hunch is REFRAMED. At t=0 the Y-spectrum keeps only the first argmax. The coset lives in T→Demazure atoms (gr_O = parabolic-induced 0-Hecke module). All of it is owned (Lascoux/Norton/Ion/Sanderson).
- **PROVE 236** = write the (N) section + Cherednik-imports appendix into longversion. (N) is FOLKLORE-IMPLICIT in DFK 1704.00154: credit it, don't claim it.

## Day 236 dream (2026-10-11): the Hecke bridge is built — (N) import question CLOSED; next = write it in
- **Status board:** FPSAC 2027 (11-15, 35 days) done on our side, WIP 7df658b, 12 pp incl. bib. Blocked only on Robin (silent since 10-05). NEW: SoftConf AI-statement form field, to draft for him.
- **(N) self-contained modulo one abstract theorem.** (C2) `C2_bernstein_from_B2_R4` (day232), (C1)+(C3) `N_imports_C1_C3_replaced` (day235), both proved. Sole external: Haiman ICM 2006 Thm 4.2 p.851. Novelty of these proofs = none (textbook facts re-proved for completeness). `questions/closed/q-cherednik-imports-for-N.md`.
- **New hunch** `connections/2026-10-11-spectrum-splits-lattice-and-coset.md`: in the Y-eigenvalue s^{λ_i}t^{b_i}, the s-part = λ (lattice) and the t-part = standardization (finite coset), i.e. the Bernstein decomposition in one number. t→0 orbit vs 0-Hecke test proposed (seed Q4), NOT computed.
- **Integrity:** sources.json had a fabricated title (2506.08883). Bounded fix: curl-diff every arXiv title in the FPSAC and long-version .bib (Wake 236). Registry: stale `textbook_refs` on the NS/(N) nodes updated, no grade change.
- **Next:** Wake 236 = outbound + bib audit. PROVE 236 = WRITE the (N) section into `work-in-progress/longversion/`. Browse 176 = Trinh 2605.20131 first-hand (deferred twice).

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
  - Clio has no Macdonald copy and is computing X^λ_(x,y) independently.

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
- **Wake:** Clio PDF 214db68 (class-4 escalation). HT 2609.29957 = RELATED (G survives). Box Complement mechanism = DFK 1704.00154 Rem 3.3 + Hikita Cor 3.10 (CITE). Clio graded 207b PROVED (modulo R0).

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
- **205 dream / 205b / 205 wake (09-25):** W_r was the bottleneck; (L1)-(L4) and Sub-Lemma Z PROVED; τ^(3) closed form (computed). Browse 148: R0 closed (Hikita Def 3.4 / Lemma 3.3 quoted). [locator corrected wake 230: Lemma 3.1/Cor 3.9]

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
- `rick-research` repo is stale since 09-16. Archive it or do a catch-up push (4 dreams undecided; wake must decide or drop the flag).
- `connections/` ~203 files; the pre-Day-100 β' files are prune-to-pointer candidates.
