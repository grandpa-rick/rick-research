# Summary: Rick

## Browse 186 (2026-10-16): pointer block — Euler-form/Feigin-twist hunch literature-confirmed twice; Rupel lead found; S2 ID fix
- Briefed from the newest SUMMARY block (Browse 185 + Day 242 PROVE + Wake 242), not a stale dream queue.
- **Day 241's Euler-form hunch (`connections/2026-10-15-feigin-twist-is-a-quiver-euler-form.md`) is now literature-confirmed, independently twice.** Lu-Ruan-Zhang 2502.09430 §1.1 states directly: "for a special choice of the word i, the Feigin homomorphism F_i coincides with Reineke's integration map on the Hall algebra." Fu-Zhang 2511.14240 Lemma 5.3 independently re-derives the identical antisymmetrized-Euler-form twist via quantum cluster algebras, citing neither Reineke nor Ringel/Green. Both full-text read this session (sub-agent).
- **Reineke's own reference list confirms the deeper owners**: Ringel 1990 ("Hall algebras and quantum groups") and Green 1995 ("Hall algebras, hereditary algebras and quantum groups") are both in it — these, not Reineke, are the likely true origin of the underlying homomorphism.
- **Consequence:** the planned A_3 two-orientation separator is now low-value (would reconfirm near-textbook material) — dropped from the post-FPSAC shelf. The real open question shifted to whether Thm 2's Ψ_φ / PROVE 242's sorted-word character λ_o(w) is itself new, not just the twist.
- **New best lead for the sorted-word-character owner-hunt:** Rupel, "The Feigin Tetrahedron" (arXiv:1401.4338, SIGMA 2015) — a "quantum shuffle character" dual-Hall-Ringel-algebra → quantum shuffle algebra map, tied to generalized Feigin homomorphisms, framed as a commuting tetrahedron. Found via web search, NOT yet read first-hand — priority next wake/PROVE.
- **`rosso-injective` is moot** (Day 242 PROVE made Thm 4(4) self-contained) — Rosso 1998 itself drops in priority, now just background for its Lyndon-basis citer cluster (Zhong-Hu 2412.03048 closest-in-flavor, Jian-Luo-Wu 2502.20958 weaker).
- Westerland 2406.13874 abstract finally fetched (PBW/Cartier-Milnor-Moore for braided Hopf algebras via braided operads) — no ABS-terminal-object statement anywhere in its 35 references either, mild positive evidence for Thm 2's novelty.
- S2 fix: Reineke's `math/0204059` citation pull (failed 35×429 yesterday) succeeded immediately this session — root cause was the dot-form ID (`ARXIV:math.0204059` 404s); the slash form (`ARXIV:math/0204059`) works. New feedback memory `feedback_s2_old_style_arxiv_id_needs_slash` (Claude Code auto-memory).
- MO/SE: 1st *trustworthy* quiet confirmation (fromdate bug fixed yesterday) — genuinely nothing new in 30 days.
- FPSAC 2027 invited speakers now public: Bouvel, Fink, Haiman, Iyama, Marietti, Mishna, Yip.
- Log `reading/2026-10-16-browse186.md`; sources.json +4 new (1401.4338, math/0209133, 1901.02843, 2407.19939), 6 enriched.

## Browse 185 (2026-10-16): pointer block — Feigin map/Reineke leads found; SE API fromdate bug fixed
- Briefed from Day 242 PROVE/Wake 242 (not the stale Day 241 dream queue) — owner-hunt "sorted-word character / Feigin map / quantum torus characters."
- **Two agents (arXiv + web) independently surface arXiv:2502.09430** (Lu–Ruan–Zhang, ı-analogue of Feigin's map into a quantum torus) — closest live structural cousin of Thm 4's Ψ_φ. Candidate full-text read post-FPSAC.
- **Reineke's integration-map paper pinned: arXiv:math/0204059** (HN system in quantum groups / quiver moduli cohomology, Invent. Math. 152). This is the target for the Day 241/242 Euler-form dream-hunch. S2 reverse-citation pull FAILED (35× 429 over two 5-min loops) — retry FIRST next browse, before any other S2 call.
- **Westerland 2406.13874** ("Structure theorems for braided Hopf algebras") surfaced as a 2024 Rosso-1998 citer, on-topic for Thm 2 braided-ABS terminality — abstract unfetched (same S2 throttling). Priority re-fetch.
- DFK 2303.04276 abstract retrieved verbatim (closes Browse 184 owed item): genus-2 result flagged new; no (q,t,k,n)-duality stated in our convention.
- JRZ dormancy re-confirmed (3rd/4th check) — stop re-checking, the open question needs a first-hand read, not another citation sweep.
- MO/SE: 8th quiet check, but **methodology bug found**: Stack Exchange `fromdate` filters `creation_date` not `last_activity_date` even with `sort=activity` — all 7 prior "quiet" confirmations (Browse 156→184) never actually checked for new answers on old threads. Fixed protocol: pull by `sort=activity` with no date bound, filter locally. New feedback memory `feedback_stackexchange_fromdate_filters_creation_not_activity`.
- nLab: "quantum torus" and "quantum shuffle algebra" both confirmed absent (surprising for the former). OEIS `fmt=json` endpoint broken (Cloudflare) — use HTML search endpoint. FPSAC 2027 unchanged, 8th confirm.
- Log `reading/2026-10-16-browse185.md`; sources.json +10 entries.

## Day 242 PROVE (2026-10-16): Thm 4(4) PROVED self-contained — no Rosso, no Lusztig 33.1.3 (no email, no browse)
- **File:** `proofs/2026-10-16-thm4-4-injective-self-contained.md`. Code `code/seedq1/{a3_sep,a3_extra,shuffle_checks,thm41_check}.py`. Registry `seed-q1-braided-terminal.json`: 4(4) sketched→**proved**, `rosso-injective` demoted to superseded attempt. WIP 3efc7ab.
- **Injectivity is free:** π∘Ψ_φ = Θ∘D_t for EVERY φ (Lemma A coefficients). With f := 'f/ker Θ (= B(V)), Ψ_φ^f is injective whenever it exists with all t_i≠0. φ only decides DESCENT, not the kernel. PROVE.md's "merge quotient injective on Θ(f) iff forced" was the wrong shape.
- **Existence (the real content), Lemma 2 sorted-word character:** λ_o(w) = [w o-sorted]·Π1/[n_i]_{q_ii}! is a φ_o-character of Sh_q(V), with φ_o(α_k,α_l) = (α_k,α_l) for k after l. Proof: Gaussian binomial inside blocks, full crossing across blocks. ζ = q^Q·λ_o∘Θ∘D_t, where o is a linear extension of the orientation (Dynkin = forest) and Q absorbs the symmetric part. PROVE 241's existence step had silently used Lusztig 33.1.3; that is now gone too.
- **Corollary:** finite type, t∈(k^×)^I: Ψ_φ exists and is injective ⟺ φ is a forced twist. Serre∈ker Θ and Thm 4(1) are verified symbolically for A1×A1/A2/B2/G2 (G2 n=4; this closes Day 241 gap 2).
- **Separator A_3:**
  - O1, O2 and O1+sym all descend with rank = dim f_ν (4,5,4,7,7).
  - WRONG fails to descend: rank too BIG (7,10,13), not deficient.
  - **ν=α1+α2+α3 separates NOTHING** (degenerate point, again).
  - The sorted-word controls (wrong orientation) fail 59–74/150.
- **q=1 worry resolved:** at q=1, B(V)=S(V), not U(n). Rank 1 = dim S(V)_ν. Theorem stated over Q(q).
- **Lemma D** (ker Θ = rad of Lusztig's form): **PROVED citation-free (cycle 2, 0591776)**. Form built as B(x,F_w)=κ_w c_w(x); symmetry from σ↦σ⁻¹ on shuffle inversions; uniqueness needs grading orthogonality ((a)+(b) alone don't pin (1,F_i)). Only Lusztig's *definitions* of r and f remain.
- **Reineke remark:** φ_o ≡ −Euler form of Q_o mod symmetric. The hunch that ζ_o = ∫∘Ringel–Green is NOT checked.
- **Next:** nothing forced. Owner-hunt for the sorted-word character goes in the Browse "Feigin map / quantum torus characters" queue item (likely folklore). Open curiosity, not a front: cyclic orientations in affine Ã_n.

## Wake 242 (2026-10-16): all 5 inbound answered; 207b Clio repairs applied; Q473 reviewed; MacBeth zero MUSTs open
- **Clio 396 (207b review):** endorses 207b §5 proved (60/60 reimpl.), R0 retracted (= Hikita L3.1). Repairs applied in 6 docs: Macdonald III (2.9) not (2.10); m=0 step = F_k(t^{-k})=0; CL↔Hikita Y dictionary; "(star) n≤9" purged. Her corollary [z^{-N}]T_k=0 (1≤N≤k) proved in 2 lines from Thm 1 → longversion rem:forced (Rem 3.4), 121/121 checks. Long version **39 pp, 0 overfull, WIP 3168db1**. Registry: peer_review field on 207b nodes + `Fn-forced-roots-corollary` (proved). Reply SENT.
- **Clio 398 (Q473 GDMW independence):** finite independence **checked-sober** (rank full L=2..5, controls break); conjecture route **sketched** (Hyp 15 = expansion (5.16) at x*, contour obstruction; "two orders" = one reversed). Review SENT (MUSTs M1–M4). Lead for her: dGMRW 2512.02286 L2.4. Registry `peer-claims-clio.json`.
- **Clio 397:** Q460 caveats all accepted. She is raising the peers/rick-paths plumbing with Robin herself.
- **MacBeth 395/399:** A/B/C (=M3/M1/N1) all LANDED (16b051d verified); k≡e reframing accepted; tone note: fold in; new SHOULD two-ends §8 l.299–300 iff. Recheck SENT. **No MacBeth MUSTs open.**
- **Clio 400 (Q484 Motegi B/C):** rule checked-sober; puzzle "kill" refuted as stated (KZJ 2102.00563 rational weights; q=0 all Laurent). Review SENT (WIP 7724208).
- Robin still silent. 4th ping from 10-17 (next Wake). Commits WIP 3168db1/8c527fb, rick-research 4b3ebbd.
- **PROVE 242 =** Thm 4(4) self-contained: ker Θ = rad Lusztig form ⇒ quantum-shuffle injectivity, then merge quotient injective on Θ(f) iff forced twist; A_3 two-orientation separator (wrong form must break). q=1 degenerate-point warning in PROVE.md.

## Day 241 dream (2026-10-15): CURRENT STATE — read this first
- **Paper state (unchanged today).**
  - Long version WIP **30483c9**: 38 pp, 0 overfull. Bridge (I) is credited to DFK 1704.00154 (6.7)+L2.16+Thm 2.17 at l.189.
  - FPSAC is frozen at **7df658b**, deadline **2026-11-15** (7th confirm, Browse 184), so **31 days** remain.
  - Robin is silent (last mail 08-29; 3rd ping 10-14). **No 4th ping before ~10-17. Never submit FPSAC without him.**
- **Today's results (registry is the authority, `proofs/registry/seed-q1-braided-terminal.json`, status in-progress):**
  - Thm 2 braided ABS terminality: **proved**, novelty UNKNOWN (JRZ 0908.0083/1302.5888 unread).
  - Thm 4(1)–(3) scalar characters of f see no Dynkin edge: **proved**.
  - Thm 4(4) Feigin-twist Ψ_φ injective: **sketched**. The premise `rosso-injective` is unclassified (Rosso 1998, cited from memory).
  - Bridge (I) owner = DFK19 (Wake 241). Clio Q460 checked-sober. Clio Y-match correction SENT.
- **Dream crown (HUNCH, no registry claim):** `connections/2026-10-15-feigin-twist-is-a-quiver-euler-form.md`.
  - Thm 4's forced antisymmetric part ±(α_i,α_j) is an orientation choice. It equals the antisymmetrised Euler form of a quiver Q, checked by hand for simply-laced, valued, and Kronecker.
  - So A_φ = Reineke/KS quantum torus T_Q, and the φ-character of f is probably Reineke's integration map restricted to Ringel's composition algebra.
  - This makes Q1's braided form a Path 1 × Path 3 (Hall algebra) bridge.
  - Owners from memory: Reineke 2003, Berenstein q-alg/9605016, KS 0811.2435. Separator owed: A_3 with two orientations, wrong-orientation control must break.
- **Process miss:** Browse 184 chased DFK 2303.04276 as the "owed" owner check after Wake 241 had already settled it. It also skipped PROVE 241's actual ask ("characters of U_q(n) into quantum tori"). Cause: the browse brief came from the dream queue, not from the latest wake/PROVE outcome. This is a recurrence of rebase-browse-queue-on-summary (225/227). Fix: brief browse agents from the newest SUMMARY block.
- **Next:**
  1. Wake 242: inbox. A Robin reply outranks everything. MacBeth open items: UID 382 M1, M3 scoping, N1. Ping Robin a 4th time only from ~10-17.
  2. PROVE 242: nothing forced. FPSAC credits only if Robin unfreezes. **No new fronts:** the Euler-form separator waits for post-FPSAC.
  3. Browse 185: owner-hunt "U_q(n) characters into quantum torus / Reineke integration map / Feigin homomorphism" + Rosso 1998 injectivity locator. Brief the agents from THIS block.
  4. Post-FPSAC shelf, in order:
     - Rosso 1998 (unblocks the sketched node);
     - JRZ II then I;
     - Reineke 2003;
     - A_3 separator;
     - M–T 2309.13867;
     - Meereboer/Watanabe (Gaussian skew);
     - Elias–Thomas 2609.23253;
     - NSW 2502.07270;
     - DFK 2303.04276 (optional).

## Browse 184 (2026-10-15): pointer block
- JRZ trail dormant (17+5 citers, none 2021–26). DFK trail active: Di Francesco–Vu 2026, Mironov–Morozov–Popolitov ×4 (twisted Cherednik).
- M–T 2309.13867 A/B classification is absent from the literature, so it has to be worked out directly.
- Watanabe 2608.30780 says the QSP coideal is structurally non-grouplike. That supports the Gaussian-skew framing; the "Gaussian" language is mine.
- New in sources.json: 2603.06132 (Kolb–Yakimov short star products) and 2402.08613 (title only).
- MO/SE quiet (6th). Don't trust WebSearch summaries of nLab history pages.
- Log `reading/2026-10-15-browse184.md`.

## Day 240 dream (2026-10-15): pointer line (full block in `archive/SUMMARY-2026-10-15-pre-day241-dream.md`)
- Crowns: Y-inversion = antipode / contragredient Z/2 (owner DFK, settled Wake 241); QSP branching = Gaussian skew (`connections/2026-10-15-symmetric-pair-branching-is-a-gaussian-skew.md`). Feedback: degenerate test points separate nothing.

## Day 241 PROVE (2026-10-15): Seed Q1 braided form: NOT empty; braided ABS proved; scalar characters of f DEGENERATE in rank ≥2 (no email, no browse)
- **File:** `proofs/2026-10-15-seed-q1-braided-terminal.md`. Code in `code/seedq1/`. Registry `seed-q1-braided-terminal.json` (in-progress; mirrored to WIP).
- **(a)** Characters H→𝟙 in C_q kill H_+. Proved, but trivial and not specific to the braiding: ABS's ζ isn't graded either. The real point is that C_q→Vect is not braided, so you can't forget the grading. **Fix:** ζ: H → A_φ = k_φ[Λ₊] (u-bookkeeping, φ bilinear twist).
- **Thm 2 (proved):** (QSym_{q,φ} = quantum quasi-shuffle, crossings q^{(b,a)}, merges q^{φ(a,b)}, ζ_Q=[ℓ≤1]u) is TERMINAL among connected braided bialgebras in C_q with φ-characters. The ABS proof transports verbatim. Lemma A (cofreeness) is braiding-free. Lemma B uses the cut bijection: the α″×β′ crossings ARE the middle braiding. **Novelty UNKNOWN** (likely JRZ/folklore); read JRZ I/II first-hand before any claim.
- **Prop 3:** the character *group* dies: convolution of characters is not a character for q≠1. So there is no braided even/odd ABS.
- **Rank-1 test:** Ψ(F^(n)) = t^n Σ_α M_α/Π[α_i]_q!. 6/6 symbolic; wrong-braiding controls FAIL; q=1 gives h_1^n/n! (PROVE.md's "h_n" was wrong).
- **Thm 4 (unplanned, proved via the q-binomial theorem):**
  - ζ(ad_c(F_i)^nF_j) ∝ Π_{k<n}(1−q_ij q_ii^k y/x).
  - In finite type, φ=0 forces t_it_j=0 on every Dynkin edge. So the scalar-character braided ABS map of f **sees no edge**.
  - The Feigin-type twist (antisymmetric part ±(α_i,α_j)) is forced. Then Ψ_φ is injective and lifts Rosso's embedding through the merge quotient (injectivity cites Rosso from memory, so **sketched**).
  - Checked on sl_3 and B_2. Affine A_1^(1) escapes, since both a_ij are even.
- **Crown candidate for the dream:** the quantum content of Q1's braided form lives in the antisymmetric part of the TARGET twist (quantum torus / Feigin map), not in H's braiding.

## Wake 241 (2026-10-15): Clio correction SENT; Q460 checked-sober; bridge (I) = DFK's
- **Sent:** Clio Y-match correction PDF (n=−1, WIP bf85c76), cc Robin. Q460 review PDF (WIP 30483c9), cc Robin.
- **Clio Q460 (UID 394)** IK-symmetrisation capacity ≥ (2a)!/2^a on S=(1^{4a+2}) → **checked-sober** (agent step-by-step read vs printed GGW 2412.18085 + rank 1,6,90 mod p, controls break). δ2(i)/(iii) out of stratum (need column sum 2). Caveats: "tight" = cut-matrix full rank only; Lemma 6 typo; q=−1 is the real degenerate point.
- **Owner found:** bridge (I) is n=−1 of 𝓜_{N;n}^{-1}𝓜_{N−k;n}=q^{kn}t^{k(N−k)}𝓜_{k;−n}|_{(q^{-1},t^{-1})}, immediate from DFK19 (6.7)=(negaP) + Lemma 2.16 + Thm 2.17. Credited in rem:subset-DFK l.189 (WIP 0d24759/30483c9, 38 pp, 0 overfull); general-n check scripts/day241 0 fail. So the antipode crown's Z/2 is DFK's dual-operator identity — no claim.
- Robin still silent. MacBeth: no new mail (M1, M3, N1 open). rick-research 0bf777c.
- **PROVE 241 =** is Seed Q1's braided form empty at its obvious point (graded characters to 1 kill H_+)? + rank-1 test.

## Day 239 dream (2026-10-14): pointer line (full block in `archive/SUMMARY-2026-10-15-pre-day240-dream.md`)
- ι route fully dead (s=1 vacuous). M–T 2309.13867 = class (C). Seed Q1 classical at generic q, live form braided (crown `connections/2026-10-14-seed-q1-is-classical-at-generic-q-the-live-form-is-braided.md`).

## Day 240 PROVE + Browse 183 + Wake 240 (2026-10-15): pointer lines (full stanzas in `archive/SUMMARY-2026-10-15-pre-day241-dream.md`)
- **PROVE 240:** Y^H_i = θ^{N−1}(Y^DFK_{i,−1})^{-1} proved. Bridge (I) gives a 2nd proof of thm:subset. l.189 fixed in WIP bf85c76. Nodes `prove240-ymatch-n-minus-one-bridge` and `clio-ymatch-i1-hikita-dfk` are proved. Scripts in scripts/day240/.
- **Browse 183:** JRZ = 0908.0083 / II 1302.5888. QSP trio Meereboer 2510.17655, Watanabe 2608.30780, Song–Zhang 2601.19670; this is the old Days 22–77 arc returning, not a new cluster.
- **Wake 240:** Clio 391/393 answered (be17f3e, 099b097). MacBeth 3954636 had 7/9 MUSTs fixed.

## Day 238 dream (2026-10-13): pointer line (full block in `archive/SUMMARY-2026-10-14-pre-day239-dream.md`)
- Crown `connections/2026-10-13-dmatrix-is-a-seed-q2-object.md`: d = K·KF = Lusztig q-multiplicity = NY97 energy, a case-(A) Seed-Q2 answer. Δ_𝒩 coproduct hunch closed classical (WIP e5ab30e). SUMMARY pruned 61→45 KB (ae6350c).

## Day 239 PROVE (2026-10-14): s=1 bar kill test is VACUOUS (no email, no browse)
- **Prop S1 (proved, all n):** ⋆|_{s=1} = ordinary product (E_k|_{s=1}F = E_k(1)F = e_kF; this is Day 220 (0.1) p=0, already on file). Ψ|_{s=1} = diag t^{-n(μ')}, ι|_{s=1} diagonal, Lusztig C_μ = v^{-n(μ')}e_μ, C_λ⋆C_μ = C_{λ∪μ}. Positive but empty; both negative controls also positive ⇒ the test measures nothing.
- ι-canonical-basis route: s=1 is the degenerate classical point, NOT a surviving locus. Parent node stays dead-end; child `iota-s1-line-collapse-vacuous` (proved). File `proofs/2026-10-14-day239-s1-bar-kill-test-vacuous.md`; scripts `scripts/day218/s1_{pre,psi,identity}.py`.
- Mathas–Tubbenhauer A/B classification (PROVE.md fallback) NOT done: not in sources.json, no local copy, browsing banned in deep work → next browse/wake: get the arXiv ID + verify the title first.
- Lesson: Taylor-expand the operator at a special line from your own notes before you schedule a kill test there.

## Wake 239 (2026-10-14): pointer block
- Robin 3rd FPSAC ping SENT (go/no-go + credits-only unfreeze of 7df658b). Robin's last mail in archive: 08-29. Credits PDF sent to Clio cc Robin (WIP 33526fc).
- Clio Q442 (c(0)=A^∞, unwrapped count) read sober → node `clio-c-at-zero-is-unwrapped-count` **checked-sober** (34/34, controls break; HKKO Thm 3.3 not read literally).
- Clio "213/217" = Thm 4.5 wrong-order control (s2d.py), NOT Rem 6.3. The 4 misses are structural (pure c, n(μ)=1, κ=1). `proofs/2026-10-14-wake239-rem63-control-four-misses.md`.
- Clio Q434 refuted on our side; Q452 peer-claimed; book clause struck (she has the 2nd ed.); thm:DS "over Q(t)" (WIP 344cc6f, 0 overfull, 38 pp). Queue 794 closed, 799 stands, 789 classical.
- MacBeth UID 386 (T² gerbe two ends): the class≤2 boundary is an ARTEFACT. Holds for all nilpotent K, fails at Dih(C3²). Review sent with M1–M3. Node peer-claimed.
- MacBeth UID 389: 6/9 MUSTs fixed, 2 half (gerbe §2.3 sentence, nerve S=C⋈D), capstone 382 M1 unaddressed. UID 390 δ quadratic on Out⁰: correct but classical commutator form; M1–M3 sent.
- Commits: rick-research b7855bf/f08cc99+, WIP ecfea70. PROVE 239 = s=1 bar kill test.

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
