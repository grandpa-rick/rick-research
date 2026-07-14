# Summary — Rick

## Current state (2026-07-14 Day 96 wake — Registry updated with Day 95 nodes (♣ proved, ♦_1/♦_3 proved-conditional, ♥ computed, ♢ simplified odd-c D); PROVE queued for ♥ structural derivation; CODE queued for c=17 witness + ♥ extension to c ∈ {20,24,28,32}; LEAN queued for (♣) formalisation)

**Day 96 wake actions (2026-07-14):**
- Registry (`proofs/registry/beta-prime-mod8.json`): 5 new nodes added — `beta-LB1-universal-identity` (♣, proved), `LB2-excess-formulas` (♦_1 & ♦_3, proved conditional on F2 + F3), `F3-structural-derivation-sketch` (sketched), `delta-recursion-odd-k-slice-c-cong-0-mod-4` (♥, computed), `beta-prime-c-4k-plus-1-power-of-2-from-LB2` (sketched). `beta-prime-digit-sum-formula` approach updated to include ♢ simplified form.
- Trigger files: PROVE.md targets structural proof of (♥) [closes c ≡ 0 mod 4 branch if proved]. CODE.md targets c=17 distinct-min witness [confirms sub-progression] + extension of (♥) to c ∈ {20,24,28,32} + Q_k mod 4 catalog. LEAN.md targets (♣) formalisation.
- Robin daily email sent (Day 95 recap + Day 96 plan). CC Clio.
- Inbox empty.

## Previous state (2026-07-13 Day 95 P0 — ODD-C SUB-PROGRESSION CLOSED: c ∈ {5,9,17,33,…} via LB_2 clean derivation; c ≡ 3 mod 4 still opaque; Δ-recursion on odd-k slice at c ≡ 0 mod 4 identified as key missing lemma)

**HEADLINE — Odd-c sub-progression closed structurally.** Day 95 PROVE session (deep-work) derived the digit-sum formula for the arithmetic progression c = 4·2^m + 1 (i.e., c ∈ {5, 9, 17, 33, 65, …}) via a clean LB_2 closed form: `LB_2^{(c=4k+1)} = 8k − 5 − 2·s_2(k−1)`, which equals β'(c) exactly iff s_2(k) = 1 iff k is a power of 2. Excess formula (♦_1): `LB_2^{(c=4k+1)} − β'(c) = s_2(k) − 1`. Symmetric result for c ≡ 3 mod 4 (♦_3): `LB_2^{(c=4k+3)} − β'(c) = s_2(k) + 2·v_2(k)`, which is ≥ 1 for all k ≥ 1, so **k*=2 is NEVER argmin at c ≡ 3 mod 4**. Precise mechanistic characterisation of when k*=2 works: exactly on c = 2^(m+2)+1. New identity (♣): `β(c) − LB_1^{(c)} = s_2(c−1) + v_2(c−1) − v_2(c)` uniformly, `proved` from F2 + Legendre. New Δ-recursion (♥) empirical at c ∈ {8,12,16}: on odd-k slice at c ≡ 0 mod 4, `Δ_{k+2}^{(c)} − Δ_k^{(c)} = 2·v_2(c−1−k)`. If proved, closes c ≡ 0 mod 4 fully via k=1 → LB_1 = β' (Day 94 result). Also: F3 (Δ_2=1 at c_odd) now has structural sketch via bracket parity — achievers characterised as (a odd, b even). Simplified D form: **`D(c_odd) = 2 + 2·s_2(k) + 2·v_2(k)`** with k = ⌊c/4⌋ (uniform across c mod 4). c ≡ 3 mod 4 remains genuinely hard — argmin k* jumps unpredictably. File: `proofs/2026-07-14-digit-sum-odd-c-attempt.md`.

## Previous state (2026-07-13 Day 94 wake — DIGIT-SUM FORMULA now 10/10: β'(14)=21 and β'(15)=19 CONFIRMED EXACT via distinct-min witnesses; c ≡ 0 mod 4 case half-derived structurally via v_2(k') cancellation)

**HEADLINE — DIGIT-SUM formula extended two data points, both hit EXACT.** Day 94 wake CODE agent ran distinct-min witness checks at c=14 (predicted 21) and c=15 (predicted 19). Both confirmed exact:
- **β'(14) = 21** via witness (a,b,k*)=(0,0,0), single-summand H_14 = 5.7e22, v_2=21. Scan [0,32)² × k*∈[0..6] confirms 21 for ALL k* (the "all argmin tied" prediction holds; formal SCP degenerate but valid).
- **β'(15) = 19** via witness (a,b,k*)=(6,7,7), H_15 = 2.9e30, v_2=19. Per-summand v_2=[24,23,24,22,24,23,24,19], carrier v_2=19 UNIQUE at k*=7 (opposite extreme to c=14). h_7^{(15)} extracted as bivariate poly (325 samples, sympy rref, catalog cross-check passed).

Empirical fit now **10/10** at c ∈ {4..11, 14, 15}. LB-catalog structural confirmation still at c ∈ {12, 13, 15}. Prior "floor formula" (which predicted β'(14)=20) FALSIFIED — digit-sum formula holds. Registry: `beta-prime-14-exact`, `beta-prime-15-exact` at `checked-sober`. Files: `code/2026-07-13-c14-c15-witness-checks.md`.

**HEADLINE 2 — c ≡ 0 mod 4 case half-derived structurally.** Day 94 wake PROVE agent got a partial structural derivation for c ≡ 0 mod 4: using F2 (Δ_1 = v_2(c(c-1))) + Legendre, `LB_1^{(c)} = 8k' − 2 − 2·s_2(k') − v_2(k')` for c = 4k'. Combined with `s_2(4k'-1) = s_2(k') + v_2(k') + 1`, the v_2(k') terms cancel EXACTLY, producing D = s_2(k')−1 as claimed. Reduces c ≡ 0 mod 4 case to proving β'(c) = LB_1^{(c)} at that residue class (SCP-at-k*=1 witness). Registered sub-node `beta-prime-c-cong-0-mod-4-from-LB1` at `sketched`. Odd-c and c ≡ 2 mod 4 cases still opaque. File: `proofs/2026-07-13-digit-sum-derivation-attempt.md`.

**HEADLINE 3 (from Day 93 END, retained):** LB_1_c_uniform lean-verified (388 LOC, `[propext, Classical.choice, Quot.sound]`). Route V (GMSW 2607.06749) closed NEG — 5/5 M_j attack routes fail for composition-vs-product reason. /assumptions on M_j Sym form CLEAN AUDIT (7/7).

**Robin daily email sent** at Day 94 wake (headline digit-sum formula + Route V + LB_1 lean-verified + Clio ask). Follow-up email sent same session with c=14, c=15 confirmations. Empty inbox. Clio silent 27+ days.

## Previous state (2026-07-13 END Day 93 — DIGIT-SUM FORMULA for β'(c) fits 8/8 at c ∈ {4..11}; LB-catalog confirms c ∈ {12,13,15}; Route V CLOSED NEG (5/5 composition-vs-product); LB_1_c_uniform lean-verified; /assumptions on M_j clean)

**HEADLINE — DIGIT-SUM FORMULA (CODE cycle):** Day 93 CODE cycle (which timed out at 2h but delivered before dying) found the first c-uniform closed form for β'(c) to survive falsification. Write D(c) := β(c) − β'(c) with β(c) = 2(c−1) − s₂(c−1). Split by c mod 4, let k = ⌊c/4⌋:
- c ≡ 0 mod 4: D(c) = s₂(k) − 1
- c odd: D(c) = 4 + 2·s₂(k − 1)
- c ≡ 2 mod 4: D(c) = 1 + s₂(k − 1)

Pure digit-sum shape — NO polynomial-in-c, NO floor formula (both killed Day 91 and this session respectively). Fits registry-canonical β'(c) at c ∈ {4..11}: **8/8**. Structurally confirmed via elementary LB catalog: β'(12) = 18 (LB=UB), β'(13) = 16 (LB=UB), β'(14) predicted 21 (LB=21, UB pending witness), β'(15) predicted 19 (LB=19 UNIQUE via k=7, UB=20 pending). Matches Iverson 2603.11069 / Alekseyev-Amdeberhan-Shallit-Vukusic 2505.08935 digit-sum template family. First-pass floor formula died at c=14 via LB catalog check → digit-sum revision holds. Full writeup: `code/2026-07-13-digit-sum-cascade-report.md`. Predictions extend to c=25; c=16 gives D=0 → β'(16) = β(16) = 26. **New connection filed:** `connections/digit-sum-formula-for-beta-prime-c.md` (Tier A active-live). **Registry action pending Day 94 wake:** register `beta-prime-digit-sum-formula` at `checked-sober`.

**HEADLINE 2 — LEAN (LB_1_c_uniform lean-verified):** Day 93 LEAN session closed the final sorry in `lean/2026-07-12-LB1-c-uniform.lean`. `min_v2_asc_poch_shell` proved via existential witness `x₀ + shift = 2^K + 1` with `K = (c-2) + shift.toNat + 1`. Pure block arithmetic: for `1 ≤ i < 2^K` the 2-adic congruence `v_2(2^K + i) = v_2(i)` + `padicValNat.mul` sums to `v_2((c-2)!)`. NO Legendre digit-sum, NO Kummer machinery. Two private helpers (~35 lines total). File: 388 LOC, zero sorrys, zero warnings. Both `hOne_padicVal_decomp` and `LB_1_c_uniform` verify at axiom set `[propext, Classical.choice, Quot.sound]`. Registry `LB_1_c_uniform`: `sketched → lean-verified`. **Side observation:** the parity-shell variant of the min-Poch shell lemma (as described in Day-92 LEAN.md) is FALSE at multiple triples — existential form is what's actually needed. Files: `lean/2026-07-12-LB1-c-uniform.lean`, `code/2026-07-13-min-v2-shell-sanity.py`.

**HEADLINE 3 — PROVE (5-of-5 M_j routes closed):** Phase A: Route V (GMSW 2607.06749) **CLOSED NEG**. Their filtration multiplicities are q-binomials · 2-row Schur-Weyl characters (polynomial in n,m,d,k); Rick's M_j is a 3-row Kostka-Motzkin-weighted skew SYT count. Spot check at (n,m)=(3,1),d=1 gives GMSW=3 vs Rick's M_1(3,1,0)=1. **Fifth route to close for the composition-vs-product reason.** Phase B: /assumptions on M_j Sym form — **CLEAN AUDIT**, zero broken assumptions among 7 checked. Three loose ends flagged (Clio at c>5,j≥1; 4-row extension; induced-module framework unexplored). One cosmetic gloss error in Day 86 §9 (Young subgroup mis-stated; does not affect calculation). New registry nodes: `Mj-gmsw-route-V-identification` (dead-end), `Mj-sym-form-audit-clean` (checked-sober). Path to `proved` is now EXTERNAL (Clio data OR rep-theoretic derivation of Clio's Lemma-1 template constants) — no Sym-side hole. New connection: `connections/five-mj-routes-composition-vs-product.md` (Tier A). Draft "M_j as new object" abstract at `for-collaborator/2026-07-13-Mj-new-object-abstract.md` targeting FPSAC 2027 poster.

**Browse 85 payoffs:** GMSW main theorem extracted verbatim; Alekseyev-Amdeberhan-Shallit-Vukusic 2505.08935 identified as Iverson's predecessor (β'(c) digit-sum template); Gangl-Gutiérrez-Szwej 2507.06220 (dual Foulkes-Howe = k-fold plethystic substitution) newly tracked; FPSAC 2026 Day 1 (no slides yet); Schilling Paris slides now at `math.ucdavis.edu/~anne/talk-Paris2026.pdf`; Gerber-Ion-Lecouvey-Lenart 2607.03966 explicitly EXCLUDES D_n^{(1)} from X=K (calibration for DIII difficulty); Watanabe-Hoshino bi-icrystal still not posted.

**Robin daily email sent** at Day 93 wake (Day 92 four-route-closure recap + GMSW 2607.06749 as Route V + FPSAC 2026 zero-M_j confirmation). Empty inbox. Clio silent 26+ days.

## Previous state (Days 90-92 arc, compressed 2026-07-12/13)

**Two cascades and one Lean warmup in three days.**

### The M_j five-route cascade (Days 90-93)

Five independent attack routes for `Mj-c-uniform-conjecture` all closed NEG for the same structural reason: they categorify plethystic **compositions** s_μ[s_ν]; Rick's M_j is a Sym-function **product** e_2^j · p_1^{n-2j}. (I) Kannan-Song 2509.18298 Λ^[2] Adams-skewing into Λ̂ (Day 90). (II) Motzkin K-triangle no single family μ(k,j) (Day 90). (III) Bechtloff Weising Cor 3.19 (α,β) hunt exhaustive n ≤ 7 (Day 90). (IV) Gutiérrez-OSSZ 2511.02649 rational bivariate GF for SL_2-plethysm coefficients — theirs is ⟨s_λ, s_μ[s_ν]⟩ (composition) vs Rick's product (Day 92). (V) GMSW 2607.06749 field-independent filtration on Δ^{(n,m)} Sym^d E with q-binomial multiplicities (Day 93). Signal is clean: existing categorification community works composition-land; product-land is the gap. See `connections/five-mj-routes-composition-vs-product.md`, `four-mj-routes-all-closed.md`, `three-routes-to-Mj-c-uniform-all-closed.md`, `gmsw-filtration-as-route-v.md`.

Day 93 Phase B /assumptions on M_j Sym form: **clean audit** (0 broken assumptions among 7). Path to `proved` is EXTERNAL (Clio data at c > 5, j ≥ 1 OR rep-theoretic derivation of Clio's Lemma-1 template constants). Rick's decision: **publish M_j as new object** (draft abstract in `for-collaborator/2026-07-13-Mj-new-object-abstract.md`).

### The polynomial-in-c cascade + digit-sum resurrection (Days 91-93)

Day 91: five polynomial-in-c closed forms for β'(c) killed in one week — D1 (refined-dip), D2, D2', E (anchor), F1. All 3-4 point fits died at the NEXT POWER-OF-2 CROSSING. Rowland-Yassawi 2017 (arXiv:1505.02302) proves theoretically that these are impossible: v_p(Q(c)) for polynomial Q is periodic-or-unbounded, never "constant + occasional drops." See `connections/polynomial-in-c-fits-die-at-power-of-2-crossings.md`, `polynomial-valuation-impossibility.md`.

Day 91 CODE: **F2 c-uniform PROVED** — Δ_1^{(c)} = v_2(c(c-1)) trivially from Q_1 = −c(c-1); LB_1^{(c)} = 2·v_2((c-2)!) + v_2(c) + v_2(c-1) at all c ≥ 2. Elementary LB_k route DIAGNOSTIC (7/7 c ∈ {5..11}). β'(11) = 12 EXACT (witness (1,2,6) + T=12 92M-residue periodicity). β'(12) = 18 (LB=UB), β'(13) ≤ 16, β'(15) ≤ 20, β'(17) ≤ 23 via distinct-min witnesses.

Day 92: c=13 T=16 EXACT check FAILED (~2B residues > 4GB RAM); F2 partial Lean at 271 LOC with one sorry (`min_v2_asc_poch_shell`).

Day 93 CODE (timed out at 2h, delivered): **pure digit-sum formula for β'(c)** — three cases split by c mod 4, argument k = ⌊c/4⌋. Fits 8/8 at c ∈ {4..11}; LB-catalog confirms at c ∈ {12, 13, 15}. First surviving c-uniform closed form. See NEW `connections/digit-sum-formula-for-beta-prime-c.md`.

Day 93 LEAN: F2 Lean sorry CLOSED via existential witness x₀ + shift = 2^K + 1. `LB_1_c_uniform` at `lean-verified` (388 LOC, [propext, Classical.choice, Quot.sound]).

### Robin daily emails sent Days 90, 91, 92, 93. Clio silent 26+ days.

**Registry deltas Days 90-93:**
- DEMOTIONS Day 91: D1 (`refined-dip-formula`), D2 (`conjecture-D2`), D2' (`conjecture-D2-prime`), E (`anchor-identity-E`), `beta-prime-closed-form-conditional` → **dead-end**. `four-period-identity` was proved conditional on D1+E; antecedents now dead so identity unused.
- PROMOTIONS Day 91: `beta-prime-{11,12,13,15,17}-*-bound`, `elementary-LB-route`, `F2-Delta1-c-uniform`, `structural-conjecture-S` extended to c ∈ {4..11}.
- Day 92: `route-IV-gutierrez-ossz-plethysm-gf` dead-end; `hOne_padicVal_decomp` lean-verified; `LB1-c-uniform` sketched → **Day 93 lean-verified**.
- Day 93 NEW: `Mj-gmsw-route-V-identification` (dead-end), `Mj-sym-form-audit-clean` (checked-sober). PENDING (Day 94 wake): register `beta-prime-digit-sum-formula` at `checked-sober`.

---

## Prior state (Day 89 end, compressed to headlines)

**Day 89 delivered on all four work cycles.** The composite headline: **β'(8) = 11 verified TWO independent ways, SCP promoted checked-sober, Program A Lean chain crossed four hops, whiskey conjecture (j*=2 universally) falsified as calibration data.**

### Headline (a) — β'(8) = 11 checked-sober, two ways

**Path 1 (prove cycle 1, mod 2^11 grid).** T=11 finite 2^T-periodicity check on h_k^{(c=8)}(a,b) for k = 0..15 across 6.7M residue evaluations — ALL PASS with min v_2 = ∞ mod 2^11 on the parity shell a+b even. Witness (a,b,j) = (8,8,2): H_8(8,8,2) = 2^11 · 1 661 793 608 475, v_2 = 11 exact by distinct-min non-cancellation (h_2 carrier at v_2=11 unique; h_0 and 2·h_1 at v_2=15). See `proofs/2026-07-11-beta-prime-8-checked-sober.md`, `code/2026-07-11-c8-{extract-hk,periodicity}.py`.

**Path 2 (code cycle 2, DIRECT-INTEGER arithmetic, no modular arithmetic).** `code/2026-07-11-beta-prime-8-strong-sanity.py`: S1 direct v_2 sweep on [0,64]², a+b even — tight witnesses at v_2 = 11 for k = 0..7, k = 8..14 sit at v_2 = 12..14, k = 15 ≡ 0; all ≥ 11. S2: 1344/1344 Möbius reconstructions match pipeline (plan asked ≥ 100). S3: combined with witness → β'(8) = 11 unambiguous.

**Registry.** `beta-prime-8-lower-bound`, `beta-prime-8-witness` at checked-sober. `refined-dip-formula` at c=9 promoted checked-sober-CONDITIONAL → checked-sober-UNCONDITIONAL within Sym-side chain (Δβ'(9) = -2 no longer conditional on Clio's β'(8)).

### Headline (b) — Sharp Cancellation Principle (structural-conjecture-S) checked-sober

**`structural-conjecture-S` sketched → checked-sober** at c ∈ {5, 7, 9} via `code/2026-07-11-scp-c579.py`. Reformulation: for each c, β'(c) is realised by a single-carrier witness (a*, b*, k*) where h_{k*}^{(c)}(a*, b*) sits at LB_{k*}^{(c)} exactly, all other k-summands sit strictly above, and distinct-min sum rule delivers H_c at v_2 = β'(c). Verified: c=5 (3,0,2) k*=2; c=7 (2,3,3) k*=3 or (1,2,6) k*=6; c=8 (8,8,2) k*=2; c=9 (7,0,2) k*=2. See `proofs/2026-07-11-scp-single-carrier.md`, new connection `sharp-cancellation-single-carrier.md`.

**Falsification.** Day 87 whiskey conjecture "j*=2 universally at odd c with v_2(c-1) ≤ 2" FALSIFIED at c=7 (correct k*=3 or 6, NOT 2). Two-sample confirmation ({5, 9}) was insufficient. NEW CALIBRATION RULE recorded: whiskey rule at {c=5, c=9} without {c=6, c=7} is not calibrated.

**Attack A closed NEGATIVE.** OQ-GUTIERREZ-SL2-PLETHYSM definitively closed via full 23-page PDF read by browse-82 sub-agent — Gutiérrez eq. 1.2 is two-row Schur plethysm, NOT e_2^j · p_1^{n-2j}. See Tier-A note `connections/gutierrez-plethystic-vs-Mj.md`. `Mj-c-uniform-conjecture` unchanged at checked-sober.

**Gap to `proved uniformly`.** c-uniform closed form for LB_k^{(c)}(a,b) via Q_k(a,b,c) mod 2 structure. Day-90 target.

### Headline (c) — Program A Lean chain crossed 4 hops

**`hk_three_var_factorization` shipped**, `[propext, Classical.choice, Quot.sound]` only. 420 → 477 LOC after cycle-2 addition. Unified statement for c ≥ 3, 0 ≤ k ≤ 2c-1, given HFactorization (Day-88 Theorem 3 ♦-ext) as input: `h_k · pochL = pochR · Q_k`. Clean regime via Möbius + `ascPoch_split`; boundary regime via inner case split on j with `ascPoch_split` at different indices + `linear_combination`. Cycle 2 added mandatory k=1 data check (Q_1 = -c(c-1) verified at c ∈ {4,5,6,7} → -12, -20, -30, -42) plus two direct/unfolded corollaries. See `~/projects/lean/2026-07-11-hk-three-var-factorization.lean`, note `memory/for-collaborator/2026-07-11-lean-hk-three-var-factorization.md`.

**Program A chain now four hops deep, all Lean-verified with same axiom set:**
    `delta_beta_kummer` → `delta_beta_prime_decomp` → `delta_D_closed` → `hk_three_var_factorization`.

Design decision: `HFactorization` taken as Prop-input. Deriving from Clio's Lemma-1 template + M_j Sym-side is a large separate Lean project — Day-91+ target.

### Headline (d) — Browse 82 delivers Kannan-Song Λ^[2] as structural engine

Not a prove cycle output but a durable finding for tomorrow's PROVE: **Kannan-Song 2509.18298 Theorem 4** establishes plethystic action of Λ^[2] on Λ via D_Θ operators. This is the structural engine behind BW Cor 3.19 and the natural route to OQ-BECHTLOFF-PLETHYSTIC. Three-community convergence observed: Wildon school (Gutiérrez et al, categorification) / BW-Kannan-Song (moduli-geometry) / He-Tubbenhauer-Poulain d'Andecy (Motzkin diagrams) — all approach the same SL_2 plethysm territory without citing each other. See new connection `three-communities-at-sl2-plethysm.md`.

Also from Browse 82: **Lai-Nakano-Xiang 2511.19825** solves GGOR for type D rational Cherednik algebra via quantum wreath products — potential DIII RSK connection. **Lauve-Lazzeroni 2603.19494** {^r QSym} interpolates QSym → Sym — bears on SEED OQ-1. Both queued as high-priority reads.

## Prior state (Days 86–88, compressed)

- **Day 88 (2026-07-10).** Three-variable h_k^{(c)}(a, b, c) polynomiality delivered (Theorem 2: h_k = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a,b,c)), boundary regime closed via Γ-ratio rescue (all-k regime k ≤ 2c-1). ΔD closed form under {D1, E, D2} Lean-verified (`~/projects/lean/2026-07-10-delta-D-closed-form.lean`, 361 LOC). Program A chain three-hop after Day 88. Attack A on Bechtloff Weising: NOT a shortcut for M_j (wreath vs direct-product restriction distinction). NEW Tier-S `connections/free-vs-plethystic-power-obstructs-BW.md` (dream cycle 2) frames this as Sym identity `f^n = Σ_λ f^λ · s_λ[f]` (free ↔ plethystic split), reframes as "aggregate N_β via BW" attack C. NEW Tier-A `connections/gamma-ratio-rescue-notation-lies.md` records the boundary-closing methodology.
- **Day 87 (2026-07-09).** Four consecutive resolutions in one day. D1 (refined dip formula) at c ∈ {5, 7, 9} checked-sober. `mod-8-hypothesis` promoted checked-sober including dimer-breaking c=9. 2^T-periodicity finite check tool introduced. Lean chain extended: `Δβ' = Δβ − ΔD` (`~/projects/lean/2026-07-09-delta-beta-prime-decomp.lean`). Bonus: h_k^{(c)} constants c-uniform polynomial in c for k=0..5 (24/24 across c∈{5,6,7,9}) — superseded by Day-88 three-var factorization.
- **Day 86 (2026-07-08).** c-uniform M_j proved symbolically as Sym function identity. Registry `Mj-c-uniform-conjecture` sketched → checked-sober with 4 subordinate nodes. H_c^pred at c > 5 via Sym-side inversion. Lean-verified `Δβ = 1 + v_2(c-1)` at `~/projects/lean/2026-07-08-delta-beta-kummer.lean`.
- **Day 85 (2026-07-08).** M_j identified as ⟨s_λ, e_2^j·p_1^{n-2j}⟩ (skew-SYT sum with Motzkin-Kostka coefficients). 482/482 verified c=5. Registry `Mj-identification` checked-sober. Tier-S connection `Mj-as-sym-function-multiplicity.md` — the seed-level Path 1 + 3 + 4 bridge.
- **Day 84 (2026-07-08).** D1 extended to conditional closed-form β'(c). Four-period identity proved conditional on D1+(E). Clio Lemma-1 template constants c-uniform at c ≤ 7.

---

## Identity + collaborators

Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**ALLOWED_RECIPIENTS:**
- **Robin Langer** (langer.robin@gmail.com) — daily email rule active. CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review (`grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — thread paused.

**Naming convention (closed Browse 67):** Rick's pair (so(2N), gl(N)) = Cartan type **DIII**, not BDI (which is (SO_n, SO_p×SO_q)). Paper-level v4 §3 rewrite queued (deferred, paper stable 25+ days).

---

## Live registry

**`proofs/registry/beta-prime-mod8.json`** (in-progress). Active nodes:
- `Mj-identification` — **checked-sober** at c=5 (Day 85).
- `Mj-c-uniform-conjecture` — **checked-sober** (Day 86). Sym-side proved symbolically as a c-uniform Sym function identity; c=5 match to Clio checked-sober; c > 5 for j ≥ 1 blocked on Clio's H_c empirical. **FIVE ATTACK ROUTES CLOSED NEG:** (I) Kannan-Song Λ^[2] Adams-skewing (Day 90); (II) Motzkin K-triangle no single family (Day 90); (III) BW Cor 3.19 (α,β) hunt exhaustive n ≤ 7 (Day 90); (IV) Gutiérrez-OSSZ 2511.02649 rational GF — plethysm composition ≠ product (Day 92); (V) GMSW 2607.06749 field-independent filtration — same composition-vs-product signal (Day 93). Day 93 /assumptions on Sym form: CLEAN AUDIT (0 broken, 3 loose ends). Path to `proved` now EXTERNAL: (a) Clio empirical at c > 5, j ≥ 1, OR (b) rep-theoretic derivation of Clio's Lemma-1 template constants. See `five-mj-routes-composition-vs-product.md`, `four-mj-routes-all-closed.md`, `three-routes-to-Mj-c-uniform-all-closed.md`.
  - `Mj-sym-side-identity` — **proved** (Day 86, Sym function tautology).
  - `Mj-P1-closed-form` — **proved** (Day 86, P_1 = (a+c+1)(b+c) − c(c−1) symbolic).
  - `Mj-Pj-closed-forms` — **checked-sober** (Day 86, P_2,3,4 computed via Aitken, match c=5 Day 85).
  - `Mj-Pieri-recursion` — **proved** (Day 86, e_2-adjoint on Hall pairing).
  - `Hc-predicted-at-cge6` — **computed** (Day 86, H_c^pred via Sym-side inversion).
  - `Mj-gmsw-route-V-identification` — **dead-end (Day 93)**. GMSW filtration multiplicities are q-binomial · 2-row Schur-Weyl characters; Rick's M_j is 3-row Kostka-Motzkin skew SYT count. Spot-check: GMSW=3 vs M_1=1 at (n,m,d)=(3,1,1).
  - `Mj-sym-form-audit-clean` — **checked-sober (Day 93)**. /assumptions pass on 7 assumptions; zero broken; 3 loose ends flagged (Clio c>5,j≥1; 4-row extension; induced-module framework).
- `refined-dip-formula` (D1) — **dead-end (Day 91)**. Was checked-sober at c ∈ {5, 7, 9, 9-UNCONDITIONAL (Day 89)}; falsified at c=11 (Δβ'(11) actual −2, D1 says −1). See `polynomial-in-c-fits-die-at-power-of-2-crossings.md`.
  - `beta-prime-{5,6,7,9}-{lower-bound,witness}` — checked-sober (Day 87). LBs via 2^T-periodicity finite check; witnesses direct.
  - `beta-prime-8-lower-bound`, `beta-prime-8-witness` — **NEW Day 89, checked-sober**. Two independent paths: mod-2^11 grid (6.7M residues) + direct-integer sweep (S1 v_2 witness table [0,64]², S2 1344/1344 Möbius, S3 witness (8,8,2)).
  - `periodicity-lemma` — **proved** (elementary; Day 87). `P(a,b) mod 2^T` depends only on `(a,b) mod 2^T`.
  - `hk-c-uniform-constants-conjecture` — checked-sober (Day 87). SUPERSEDED by three-var version below.
  - `hk-c-uniform-three-var-conjecture` — checked-sober (Day 88, all-k regime k ≤ 2c-1 via Γ-ratio rescue). **Day 89: Lean-verified as `hk_three_var_factorization`** in `~/projects/lean/2026-07-11-hk-three-var-factorization.lean` (477 LOC, axioms `[propext, Classical.choice, Quot.sound]`).
- `mod-8-hypothesis` — **checked-sober** (Day 87 evening). Dimer law fails iff v₂(c-1) ≥ 3. Confirmed at c=5,7,9.
- `anchor-identity-E` — **dead-end (Day 91)**. Was sketched at k=1, 2 only; falsified at k=3 / c=12 (β'(12) ≤ 18 < 19 = β(12)). Two-point pattern that didn't extend.
- `conjecture-D2` — **dead-end (Day 91)**. Falsified at c=11.
- `conjecture-D2-prime` (D2') — **dead-end (Day 91)**. Was proposed as D2 correction (D(4k+3) = 4 + 2·v_2(k)); falsified at c ∈ {12, 13, 15} the same day it was proposed.
- `four-period-identity` — **proved** (conditional on D1 + E). Antecedents both dead-end as of Day 91; identity is unused going forward.
- `beta-prime-closed-form-conditional` — **dead-end (Day 91)**. Was conditional on D1 + E + D2; all three antecedents dead.
- `beta-prime-11-{lower-bound,witness}` — **checked-sober (Day 91)**. Witness (1,2,6); T=12 periodicity 92M residues.
- `beta-prime-{12,13,15,17}-upper-bound` — **checked-sober (Day 91)**. Distinct-min witnesses.
- `elementary-LB-route` — **checked-sober (Day 91)**. 7/7 c ∈ {5..11}; diagnostic mechanism.
- `F2-Delta1-c-uniform` — **proved (Day 91 CODE)**. Δ_1^{(c)} = v_2(c(c-1)) trivially from Q_1 = −c(c-1). LB_1^{(c)} = 2·v_2((c-2)!) + v_2(c) + v_2(c-1) fully explicit ∀ c ≥ 2.
  - `hOne_padicVal_decomp` — **lean-verified (Day 92)** at `[propext, Classical.choice, Quot.sound]`. Per-point 2-adic decomposition of h_1^{(c)}(a,b) under F2Factored hypothesis.
  - `LB_1_c_uniform` — **lean-verified (Day 93)** at same axiom set. `min_v2_asc_poch_shell` closed via existential witness x₀ + shift = 2^K + 1; pure block arithmetic. 388 LOC total.
- `beta-prime-digit-sum-formula` — **checked-sober (Day 94 wake, registered 2026-07-13)**. D(c) = β(c) − β'(c) is a pure digit-sum expression with argument k = ⌊c/4⌋ split by c mod 4. Empirical fit **10/10** at c ∈ {4..11, 14, 15} (c=14, 15 confirmed EXACT Day 94 wake via distinct-min witnesses). LB-catalog structural at c ∈ {12, 13, 15}. Sub-node `beta-prime-c-cong-0-mod-4-from-LB1` at `sketched`: c ≡ 0 mod 4 case half-derived via v_2(k') cancellation between β's Legendre and Δ_1 (F2). Gap to `proved`: (a) SCP-at-k*=1 c-uniformly for c ≡ 0 mod 4; (b) odd-c derivation with "+4" constant + 2·s_2(k−1) mystery; (c) c ≡ 2 mod 4 case; (d) c-uniform argmin-k*(c) selection rule (k* jumps: c=5,9,17→2; c=13→6; c=15→7). See `digit-sum-formula-for-beta-prime-c.md`.
- `beta-prime-14-exact` — **checked-sober (Day 94 wake)**. β'(14) = 21 EXACT. Witness (0,0,0). All argmin k* tied at 21.
- `beta-prime-15-exact` — **checked-sober (Day 94 wake)**. β'(15) = 19 EXACT. Witness (6,7,7). k*=7 UNIQUE. Improves prior UB of 20.
- `clio-lemma1-template-uniform` — **checked-sober** at c ≤ 7.
- `delta-beta-kummer-identity` — **proved**, **lean-verified** (Day 86). Chain now **four hops** (Day 89): `delta_beta_kummer → delta_beta_prime_decomp → delta_D_closed → hk_three_var_factorization`, all `[propext, Classical.choice, Quot.sound]`.
- `structural-conjecture-S` (Sharp Cancellation Principle) — sketched at c=5 → checked-sober at c∈{5,6,7} (Day 87) → checked-sober at c ∈ {5,7,9} (Day 89) → **checked-sober at c ∈ {4..11}** (Day 91, extended catalog via elementary LB_k route). All 7 c-values verified: `min_k LB_k^{(c)} = β'(c)` at c ∈ {5..11}. Gap to `proved uniformly`: c-uniform closed form for Δ_k^{(c)}; F2 gives Δ_1 = v_2(c(c-1)) uniformly, F3 gives Δ_2 = 1 at odd c empirically (c ≤ 13). Δ_k for k ≥ 3 has no low-degree polynomial-in-c form; Day 91 killed five such fits. Live route to closed form: Gutiérrez-OSSZ (see `Mj-c-uniform-conjecture`). See `sharp-cancellation-single-carrier.md`, `polynomial-in-c-fits-die-at-power-of-2-crossings.md`.
- `kummer-jump-mechanism` — hunch (now precisely the max(2, v₂(c−1)) clamp in D1).

**`proofs/registry/strict-axis-closed-form.json`** — strict #AXIS = 2(n−1) empirically (n ≤ 12), closed form conjectured.

**Lean chain** at `proofs/lean/bdi-polytope/BdiPolytope.lean` (~3100 lines pure stdlib):
- `feasibility_ray_char_lattice` (Day 78) — Theorem 4.2 chain, `[propext, Quot.sound]`-only.
- `multiplicative_redundancy` (Day 76, Lemma 7.1).
- `additive_redundancy_at_eS` (Day 79, Lemma 4.1) — redundancy reservoir FORMALLY CLOSED.
- `sparse_witness_F_feasible` (Day 82).
- `sparse_witness_image_containment` + `uniform_droppability` (Day 83) — Theorem 9.1 chain shipped.

---

## Research territory (SEED.md)

Four paths + one active-central bridge:
- `topics/path1-combinatorial-hopf.md` — Sym / QSym / NSym Hopf-algebra machinery, ABS theorem, primitives, character decomposition.
- `topics/path2-quantum-groups.md` — U_q(g), R-matrix, crystals at q=0, Kashiwara / Lusztig / canonical bases.
- `topics/path3-hecke.md` — H_q(S_n), Kazhdan-Lusztig, Schur-Weyl, cellular structure.
- `topics/path4-coproduct-crystal.md` — Sym coproduct = crystal tensor rule (LR coefficients); type-D RSK gap.

**Active seed connections (live):**
- **Path 1 + 3 + 4 (NEW Day 85):** M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩. β' 2-adic story is a Sym/Frobenius-char question. Wreath products S_2 ≀ S_j = Weyl(B_j) enter naturally. See `connections/Mj-as-sym-function-multiplicity.md`. Tier S.
- **Path 2 + 4 (main polytope thread):** π_n canonical projection, AII-fibered groupoid, R-AXIS(n) = 1 uniformly at p_1 (PROVED Day 75-79). Bucket-0 = adj(sl_2) as rep-theoretic anchor.
- **Path 2 + 4 — redundancy reservoir (FORMALLY CLOSED Day 79):** multiplicative + additive halves both Lean-shipped, axioms `[propext, Quot.sound]`.
- **Path 2 + 4 — DIII RSK export:** image-equivalence frame IS the prescription for missing DIII P-side. BK done via Svyatnyy 2605.00514; P-side + slack data missing. See `connections/image-equivalence-as-diii-rsk-prescription.md`.
- **Path 2 + 4 — feasibility ray-char:** Theorem 4.2 + Cor 5.1 as polytope shadow of crystal tensor Z_{≥0}-combinations. Fully axiom-free Lean.
- **Path 2 + 4 — wall-count contrast:** three levels (polytope facets Θ(n) / strict #AXIS = 2(n−1) BDI / R-AXIS = 1 uniformly BDI).
- **Path 2 + 3 — sqrt crystals as DIII K-theoretic:** speculative, tracked. Marberg-Tong-Yu 2501.16640 half-integer weight structure ↔ D_n spinors.
- **Path 3 — Marberg's 4 twisted-involution KL conjectures** (1306.2980) unguarded; long-horizon.
- **Path 1 — NSym^B from H^B_*(0)** open; OQ-HUANG-B, P_PARK #3.

---

## Crown-jewel connections (`connections/`)

**Tier S — Seed-level / load-bearing:**
- `Mj-as-sym-function-multiplicity.md` — NEW Day 85. β' 2-adic story lives in Sym. Path 1 + 3 + 4 simultaneously.
- `free-vs-plethystic-power-obstructs-BW.md` — NEW Day 88 dream 2. Sym identity `f^n = Σ_λ f^λ · s_λ[f]` = why BW doesn't shortcut M_j. Opens "compute N_β via BW then aggregate" attack route. Path 1 + 3.
- `image-equivalence-as-diii-rsk-prescription.md` — Day 78-79. Rick's methodology = DIII RSK P-side prescription.
- `additive-redundancy-as-extension-of-multiplicative.md` — Day 78-79. Both halves Lean-shipped.
- `image-equivalence-frame-as-recurring-pattern.md` — Day 76-78. Methodological pillar.
- `cover-restricted-axis-as-right-invariant.md` — Days 73-78. R-AXIS(n) = 1 uniformly.
- `bucket-0-as-sl2-rump.md` — Days 73-74. adj(sl_2) rep-theoretic anchor; triple-anchored cap α ≤ 2.
- `aii-bdi-wall-count-asymmetry.md` — Days 72-74. Three-level table.
- `feasibility-ray-char-as-restriction-shadow.md` — Day 70; Day 78 axiom-free Lean.
- `registry-vs-feasible-as-blind-spot.md` — Days 76-79. Registry ≠ feasible set.
- `engine-vs-base-canonical-degeneracy.md` — Day 76. Theorem 8.1 (n-uniform, mod D-pi).
- `azenhas-bdi-canonical-projection.md` — canonical forgetful surjection π_n.
- `pi3-stratified-multimap.md` — (c*) stack as AII-fibered groupoid.
- `cross-programme-dim-gap-codim.md` — f(n) = g(n) = 3 − [n even] conjecture.
- `discovery-layer-is-the-moat.md` — Day 39 prophet. AI verifies; humans+frameworks discover.
- `carry-Pa-as-unified-analytical-object.md` — Six roles. v3 structural climax.
- `bdi-kobayashi-polytope-faces.md` + `-weight-space-simplicial.md` — Theorems F + G. Lean shipped.
- `kobayashi-rick-non-overlap.md` — Level sets vs support facets.
- `open2-watanabe-2407-existence-meereboer-1dim-collapse.md` — v3 OPEN-2 Layer 1.
- `asymmetry-is-the-result-seven-instances.md` + `compression-is-content.md` — three asymmetric mechanisms.

**Tier B — speculative but tracked:** `sqrt-crystals-as-diii-k-theoretic.md`.

**Tier A — bridges/refinements/calibrations:** `digit-sum-formula-for-beta-prime-c.md` (**NEW Day 93** — pure digit-sum formula for β'(c) with argument k = ⌊c/4⌋, 8/8 fits + LB-catalog confirms; Iverson/Alekseyev template family), `five-mj-routes-composition-vs-product.md` (**NEW Day 93** — Route V GMSW closes same reason as I-IV), `gmsw-filtration-as-route-v.md` (Day 93 wake — GMSW as Route V candidate), `polynomial-valuation-impossibility.md` (Day 92 — Rowland-Yassawi theoretical calibration for polynomial-in-c death), `four-mj-routes-all-closed.md` (Day 92 — four-route diagnosis product-vs-composition), `gutierrez-ossz-rational-gf-as-mj-fourth-route.md` (Day 91 — Route IV Browse 83), `polynomial-in-c-fits-die-at-power-of-2-crossings.md` (Day 91 — five polynomial-in-c fits killed; SCP+T-periodicity as compiler), `three-routes-to-Mj-c-uniform-all-closed.md` (Day 90 — first three routes NEG), `kannan-song-lambda2-not-a-shortcut.md` (Day 90 — Route I), `2T-periodicity-as-sym-2adic-bridge.md` (Day 87-89), `sharp-cancellation-single-carrier.md` (Day 89 SCP), `three-communities-at-sl2-plethysm.md` (Day 89), `gutierrez-plethystic-vs-Mj.md` (Day 89), `gamma-ratio-rescue-notation-lies.md` (Day 88), `BW-reciprocity-vs-Mj.md` (Day 88), `marginal-palindromy-refutation.md` + `-v2.md`, `lu-pan-dual-canonical-bdi-algebraic-roof.md`, `zhang-lusztig-bridge-for-marberg.md`, `q-sphere-meereboer-fourth-community-deadline.md`, `Rpi-carry-one-sided-monotone.md`, `watanabe-2509-vs-bdi-v3-composition.md`, `Tobs-delta-lives-on-opfibration-not-lens.md`, `slack-vs-Rpi-doesnt-port-as-result.md`, `external-shadow-shape-eight-refutations.md`, `short-long-tensor-product-rule.md`, `chain-factor-framework-natural-scope.md`, `attribution-verification-mandatory.md`, `ghani-grading-payoff-vs-observation-mirror.md`.

**Tier B historical anchors (don't prune):** catalog/v2 + framework bridges + foundational-refuted files. See `connections/` directly.

---

## Methodological pillars

- **Image-equivalence frame:** pre-bake the relaxation; never state strong-uniqueness without finite-check first.
- **Redundancy reservoir (FORMALLY CLOSED Day 79):** multiplicative (FREE-ISOLATED) + additive (RIGIDLY-PRESENT). Both Lean, `[propext, Quot.sound]`.
- **Registry vs feasible:** Day-72 registry is a design library; under-catalogs F-feasible witnesses by ≥30×.
- **Falsification discipline:** 7-day falsification streak (Days 71-77) produced sharper ingredients → Days 78-79 delivered three consecutive positive resolutions.
- **DIII RSK export:** methodology IS the missing prescription for the literature's P-side gap.
- **Foundational-definition cross-check (Day 79):** when CODE finds something surprising, verify foundational definitions before trusting the result (`aii_rays()` bug caught).
- **Compute first, framing second (Day 85):** P_j polynomial fit gave the beautiful closed form (a+c+1)(b+c) − c(c−1) BEFORE the Sym-function structure became visible. Whiskey rule holds — framing IS the work.
- **Machine-format citations:** arXiv IDs, registry node ids, file paths. Never compress "the Di Francesco result" over a citation.

---

## Open questions (active)

**HIGHEST priority (Day 91):**
- **OQ-GUTIÉRREZ-OSSZ-MJ (Browse 83, HIGHEST after Day 91)** — 2511.02649 (Gutiérrez-Orellana-Saliola-Schilling-Zabrocki) has rational bivariate GF and complete linear recursions for ALL SL_2-plethysm coefficients. If Rick's M_j = ⟨s_λ, e_2^j·p_1^{n-2j}⟩ can be expressed as an SL_2-plethysm coefficient (requires specific parameter identification), M_j c-uniformity follows from the linear recursion. **After Day 91 cascade of D1/D2/D2'/E dead-end, this is now the only live route to a c-uniform closed form for β'(c).** Read main theorem + recursion; run SageMath M_j vs recursion check for n ≤ 8, j ≤ 4. See `gutierrez-ossz-rational-gf-as-mj-fourth-route.md`.

**HIGH priority:**
- **OQ-AHA-RSK-TYPED (Browse 83 NEW, MEDIUM)** — "AHA! RSK" 2606.00679: RSK = Jucys-Murphy basis change in degenerate affine Hecke module. Does this extend to type D via Hu algebra A_q(m) = H_q(S_m) ≀ H(2)? If yes → type D RSK from the algebraic (Path 3) direction, complementing Svyatnyy's crystal (Path 2) approach.
- **OQ-GUTIERREZ-SL2-PLETHYSM (Browse 81, Day 90 CLOSED NEGATIVE)** — Gutiérrez-Martínez-Szwej-Wildon arXiv:2607.06749 categorifies product rule for U_q(sl_2) Cartan subalgebra. Does NOT equal e_2^j · p_1^{n-2j} — different framework (see Gutiérrez 2412.15006 which studies s_{(1^n)} ∘ s_{(r)}, not Rick's M_j). **CLOSED NEGATIVE (Day 90 wake + Browse 83 confirms).** See OQ-GUTIÉRREZ-OSSZ-MJ for the right lead.
- **OQ-BECHTLOFF-PLETHYSTIC (Browse 80, Day 90 CLOSED — FALSIFIED)** — Find (α,β) with s_α(Σ h_{2k}) · s_β(Σ h_{2k+1}) = e_2^j · p_1^{n-2j}. Day 90 wake: exhaustive hunt n ≤ 7, NO PAIR matches. **FALSIFIED.**
- **OQ-BECHTLOFF-PLETHYSTIC (Browse 80 NEW, HIGHEST)** — Find (α,β) with s_α(Σ_{k≥0} h_{2k}) · s_β(Σ_{k≥0} h_{2k+1}) = e_2^j · p_1^{n-2j} in Λ. If exists, M_j = Z/2Z wreath multiplicity via Bechtloff Weising Cor 3.19, and c-uniformity is an IMMEDIATE THEOREM. SageMath, 30 minutes. Do this before anything else in next CODE session.
- **OQ-POULAIN-MOTZKIN-KOSTKA (Browse 80 NEW)** — Poulain d'Andecy 2603.19069 (March 2026): do the Motzkin triangle entries equal K_{μ^T,(2^j)}? Read intro + main theorem (≤5 pages). If yes, closes OQ-MOTZKIN-K-TRIANGLE directly.
- **OQ-MOTZKIN-K-TRIANGLE (Browse 79 NEW)** — Is K_{μ^T,(2^j)} = m^(2)_{k,j} = β_{j,k} (He-Tubbenhauer 2508.04054 formula)? Poulain d'Andecy Cor 4.4 gives centralizer; β_{j,k} = Σ_t C(j,i+2t)/(i+t+1)·C(i+2t,t). ONE CODE SESSION (10-line Python after SageMath plethystic check).
- **OQ-BECHTLOFF-MJ (Browse 79, superseded by OQ-BECHTLOFF-PLETHYSTIC)** — Bechtloff Weising 2506.07727 now DEEP READ. Cor 3.19 G=Z/2Z case is the right formula; question is now the plethystic identification. See OQ-BECHTLOFF-PLETHYSTIC.
- **c-uniform M_j conjecture** — three structural routes CLOSED Day 90 (Kannan-Song, Motzkin, BW plethystic). Fourth route LIVE (Gutiérrez-OSSZ rational GF — see OQ-GUTIÉRREZ-OSSZ-MJ above). Empirically strong (482/482 at c=5; matches Clio c=6-9).
- **D1 promotion** — DEAD Day 91. D1 falsified at c=11.
- **OQ-MARBERG-DIII-STANLEY-CONJ (Browse 81 NEW, MEDIUM)** — Marberg 2512.19034 v2 §9.3 new conjecture: F̂^DIII_{υ₀^+} = 2^{-c} S_{δ(n-1)⊖a}, a=⌈(n-1)/2⌉, c=⌊(n-1)/2⌋. Tested n≤7. Is this provable from the DIII RSK / crystal perspective?
- **OQ-MARBERG-V2-ATOM-CORRECTION (Browse 78 NEW) — RESOLVED Browse 81.** Even-n DIII atom description unchanged from v1. Odd-n (formerly DIV): fully proved in v2 via embedding ι. New conjecture F̂^DIII_{υ₀^+} = OQ-MARBERG-DIII-STANLEY-CONJ above.
- **OQ-THREE-Q-DESCRIPTIONS (Browse 77, updated 79)** — Svyatnyy short SSYT vs Marberg fpf-involution atoms (v2 corrected) vs Bingham-Ugurlu DIII clans. Bingham at FPSAC 2026 but presenting chromatic SF, NOT clans — approach informally.
- **OQ-GERBER-LECOUVEY-D-XK (Browse 78 NEW)** — D_n^(1) excluded from Gerber-Ion-Lecouvey-Lenart 2607.03966 X=K. Structural exclusion (Koornwinder/BC_n can't handle D spinors). McDonough-Pylyavskyy-Wang KR DEGs (2510.24490) at FPSAC = best current tool.
- **OQ-MOTZKIN-MJ-CENTRALIZER (Browse 78, updated 79)** — are M_j Motzkin coefficients K_{μ^T,(2^j)} dims of centralizer of U_q(sl_2/gl_2) on (V_1 ⊕ V_2)^⊗j? Halfway confirmed; last step = OQ-MOTZKIN-K-TRIANGLE computation.
- **OQ-HUDAK-LAI-HECKE (Browse 79 NEW)** — Hudak-Lai 2606.03759 wreath Hecke cellularity: does it give explicit basis for q-M_j? Hecke complement to Kannan-Song Sym side.
- **OQ-LECOUVEY-PART5-Q-RECORDING (Browse 77)** — is Lecouvey's oscillating Q-tableau (spinor parity conditions) the same as Svyatnyy's short SSYT?
- **OQ-JANG-KWON-CORRIGENDUM** — JCTA DOI 10.1016/j.jcta.2026.106161, journal-only; need direct access.
- **OQ-TYPE-D-JDT-NON-LOCAL (updated Browse 77)** — Lecouvey obstruction: horizontal slide depends on full C_2. Can non-local rules be written? Or does Jang-Kwon 2001.11191's type-A-embedding route become the only path?
- **OQ-AZENHAS-GONZALEZ-VIRTUALIZATION (Browse 77)** — 2409.12666 keys/evacuation via virtualization; type D JdT applicable?
- **OQ-AZENHAS-SLACK-DIII (Browse 70)** — DIII analogues of (R3)-(R5).
- **OQ-SSOT-TYPE-D (Browse 70)** — regular cell tableaux Q-side; type D SSOT P-side.
- **OQ-JAGENTEUFEL-DIII (Browse 71)** — SO(2n) vacillating tableau bijection open; clean template.
- **OQ-CRYSTAL-BRANCHING-BDI (Browse 65)** — gl_n → so(2n) branching formula.
- **OQ-KIERS-BDI / OQ-RESSAYRE-RICHMOND-BDI** — GL(n)↪SO(2n) admissible OPS.

**MEDIUM priority:**
- OQ-BAE-KWON-ORTHOSYMPLECTIC (Browse 67), OQ-BRUNDAN-WANG-DIII, OQ-KOLB-STEPHENS-DII, OQ-KOBAYASHI-FENCES-BDI, OQ-KOBAYASHI-MATSUMURA-D, OQ-ABOUMRAD-BD, OQ-STRICT-AXIS-CLOSED-FORM.

**LOW / dormant:** OQ-SQRTCRYSTAL-DIII, OQ-AZENHAS-SLACK, OQ-BRUNDAN-WANG-WEBSTER-BDI, OQ-KUMAR-TORRES-HIVES, OQ-HOROSPHERICAL-STACK-PI3, OQ-LUSZTIG-MARBERG (P_PARK #1), OQ-ZHANG-MARBERG, OQ-HUANG-B (P_PARK #3), OQ-LU-PAN-EXPLICIT (P_PARK #4), OQ-G-INTRINSIC (P_PARK #2), q-type-B-cactus, q-KL-from-crystal (spin CLOSED), q-zero-CHA (type A K_0 answered).

**Recently closed:** D1 / D2 / D2' / E (Day 91 — all dead-end via cascade), OQ-KANNAN-SONG-LAMBDA2-ROUTE-I (Day 90 — NEGATIVE), OQ-BECHTLOFF-PLETHYSTIC (Day 90 — FALSIFIED for n ≤ 7), OQ-MOTZKIN-K-TRIANGLE (Day 90 — no single-family rule), OQ-GUTIERREZ-SL2-PLETHYSM (Day 89 — NEGATIVE), OQ-SVYATNYY-BK-CHECK (Browse 73), OQ-GUTIERREZ-TYPE-D-BK (Browse 71-73), OQ-QSP-NAMING-CONVENTION (Browse 67), OQ-D-PI (Day 71).

---

## Calibration rules (active, most recent first)

- **Day-93 Digit-sum shape wins where polynomial-in-c dies** — the shape argument matters: β'(c) has no polynomial-in-c closed form (Day 91 killed five) but DOES have a pure digit-sum closed form with argument k = ⌊c/4⌋ (Day 93, fits 8/8 at c ∈ {4..11}, LB-catalog confirms at c ∈ {12,13,15}). Rule: for 2-adic Sym-function invariants, TRY digit-sum templates on {c, c-1, ⌊c/4⌋, ⌊c/4⌋-1} BEFORE giving up on closed forms. The Iverson 2603.11069 / Alekseyev 2505.08935 template family is the 2025-2026 state of the art. Corollary: floor-based templates die alongside polynomial-in-c ones; pure digit-sum shapes are the surviving family. See `digit-sum-formula-for-beta-prime-c.md`.
- **Day-93 Composition-vs-product is a structural fingerprint** — five categorification frameworks all closed NEG for the same reason: they parametrise plethystic COMPOSITIONS s_μ[s_ν]; Rick's operand is a Sym-function PRODUCT e_2^j · p_1^{n-2j}. Rule: before pursuing "categorification route N" for a Sym operand, verify the framework's primary parametric objects match the operand's shape (composition vs product vs induced-module). Corollary: further composition-family frameworks are unlikely to close M_j. See `five-mj-routes-composition-vs-product.md`.
- **Day-91 Polynomial-in-c fits die at power-of-2 crossings** — five conjectures for β'(c) as a polynomial-in-c mod-something formula killed in one week (D1 c=11, D2 c=11, D2' c=13, E c=12, F1 c=13). Pattern: 3-4 point fits break at the NEXT POWER-OF-2 CROSSING relative to the fit's data range. Rule: any polynomial-in-c fit for a 2-adic Sym-function invariant needs ≥ 10 data points AND at least two power-of-2 crossings before promotion beyond `hunch`. Compute first (SCP + T-periodicity), fit second. **Corollary methodological reframe:** the elementary LB_k route is DIAGNOSTIC (exposes wrong conjectures) not CONSTRUCTIVE (doesn't yield closed form). SCP + T-periodicity is a "compiler" for β'(c) values one c at a time. Day 93 addendum: the FORMULA does exist at digit-sum shape (see above), not at SL_2-plethysm-recursion level. See `polynomial-in-c-fits-die-at-power-of-2-crossings.md`.
- **Day-90 Three-parallel-routes-negative rule** — when a high-value conjecture (M_j c-uniformity, checked-sober since Day 86) has three plausible structural attack angles and ALL fail on serious testing in one session (Kannan-Song Λ^[2] ≠ wreath-Frobenius; Motzkin K-triangle no single family; BW plethystic (α,β) not in image for n ≤ 7), PIVOT to an elementary route that AVOIDS the promotion rather than push harder on categorification. The theorem you actually need (β'(c) closed form via LB_k) is often smaller than the theorem you were chasing (M_j c-uniform via wreath structure).
- **Day-89 Whiskey-rule-needs-parity-diverse-samples** — Day-87 sketch "j*=2 universally at odd c with v₂(c-1) ≤ 2" FALSIFIED at c=7 (correct k*=3 or 6, NOT 2). Two-sample confirmation at {c=5, c=9} was insufficient because both are ≡1 mod 4. Rule: whiskey-rule sketches need witnesses at parity-diverse OR consecutive c before elevating to `sketched`. Confidence scales with sample width, not sample count.
- **Day-85 "compute first, structure second"** — the whiskey rule confirmed on M_j. Framing is the work; polynomial fit before theory. When integers look opaque, compute a rational-function ratio and factor.
- **Day-78 Streak-breaks-positively rule** — 7-day falsification streak produced the RESOLUTION. Do NOT abandon a line while narrowings sharpen.
- **Day-71 Cap-without-dependence rule** — verify "Y is special because Z" by deriving the formula, not intuiting.
- **Day-72 Iterate-the-invariant rule** — after a refutation, ask "what sharper claim does the refutation respect?"
- **Day-69 Facet-count-before-headline** — wall-count claims must have closed-form CODE verification at n ≤ 8.
- **Day-70 Lean Prop-parameter quirk** — `deriving DecidableEq` + `def f | pat => body` fail vs Prop-valued inductive params; use `by cases p with`.
- **Day-60 Phantom-completion check** — verify "shipped" against `git log --oneline <file>` before promotion.
- **Day-58 Period-step finite-difference** = only valid quasipoly test.
- **Day-50 Promotion thresholds** — refines existing → journal; opens new layer → connection file.
- **Day-46 Daily email rule** — Robin standing instruction.
- **Day-45 Evidence durability:** empirical < community-internal < structural < mechanical < live-attack.
- **Day-39 Discovery-layer is the moat** — AI verifies; humans+frameworks discover.
- **Day-33 PROVE.md is binary signal**, not a communication channel.
- **Day-28-29 Falsification productivity.**
- **Day-19 Eight-refutations conclusion:** catalog-level external bridges STOP; framework-level PERMISSIBLE.

**Method-level rules (stable):** Right statement proves itself (REDUCED-multiset). Rank 2 degenerate; anchor at rank 3. Type-uniform proofs port for free; identifications don't. 30-second sympy on q-identities BEFORE carrying forward. Verify defining axioms BEFORE testing consequences. Naming-metaphor trap: use formal name in writeups.

---

## Recent history (one-liners; journals + registry have detail)

- **Day 93 (2026-07-13) — DONE.** Six phases, five delivered. Browse 85: GMSW main theorem extracted; Alekseyev 2505.08935 identified as Iverson predecessor; FPSAC 2026 Day 1 (no slides); Schilling Paris slides available. PROVE: Route V (GMSW 2607.06749) CLOSED NEG (5/5 composition-vs-product); /assumptions on M_j Sym form CLEAN AUDIT (0 broken, 3 loose ends); "M_j as new object" draft abstract at `for-collaborator/2026-07-13-Mj-new-object-abstract.md`. CODE (timed out, delivered): **DIGIT-SUM FORMULA for β'(c)** — D(c) = β(c) − β'(c) split by c mod 4, digit-sum on k = ⌊c/4⌋; fits 8/8 at c ∈ {4..11}, LB-catalog confirms at c ∈ {12, 13, 15}. First surviving c-uniform closed form. LEAN: `LB_1_c_uniform` CLOSED via existential witness `x₀ + shift = 2^K + 1`; 388 LOC, [propext, Classical.choice, Quot.sound]. NEW Tier-A: `digit-sum-formula-for-beta-prime-c.md`, `five-mj-routes-composition-vs-product.md`. NEW calibration rules: "Digit-sum shape wins where polynomial-in-c dies" + "Composition-vs-product is a structural fingerprint."
- **Day 92 (2026-07-12) — DONE.** Gutiérrez-OSSZ 2511.02649 deep-read: **Route IV CLOSED NEG**. Their coefficient is ⟨s_λ, s_μ[s_ν]⟩ (composition) vs Rick's product; Prop 3.2 q-Pascal recursion is not the same recursion. F2 partial Lean shipped at `2026-07-12-LB1-c-uniform.lean` (271 LOC, one sorry); `hOne_padicVal_decomp` at lean-verified. c=13 T=16 EXACT check FAILED (~2B residues > 4 GB RAM). Browse 84 delivered Rowland-Yassawi 2017 polynomial-valuation theoretical calibration (retroactively proves five Day-91 fits impossible) + Iverson 2603.11069 digit-sum model for β'(c). NEW Tier-A: `four-mj-routes-all-closed.md`, `polynomial-valuation-impossibility.md`, `gmsw-filtration-as-route-v.md`. Robin daily sent, Clio silent.
- **Day 91 (2026-07-12) — DONE.** Elementary LB_k^{(c)} route landed FOUR SIMULTANEOUS FALSIFICATIONS (D1, D2, D2', E) + F1 killed in CODE = **five polynomial-in-c fits dead in one week.** β'(11) = 12 EXACT proved (witness (1,2,6) + T=12 periodicity 92M residues). β'(12) ≤ 18, β'(13) ≤ 16, β'(15) ≤ 20, β'(17) ≤ 23 via distinct-min witnesses. CODE: **F2 c-uniform PROVED** — Δ_1^{(c)} = v_2(c(c-1)) trivially from Q_1 = −c(c-1); LB_1 = 2·v_2((c-2)!) + v_2(c) + v_2(c-1) fully explicit ∀c, Lean-ready. F3 empirical at c ≤ 13. Elementary LB_k route DIAGNOSTIC (7/7 c ∈ {5..11}) not constructive. Browse 83: **Gutiérrez-OSSZ 2511.02649** rational GF + linear recursions for SL_2 plethysm — NEW HIGHEST-priority M_j route (4th after 3 closed Day 90; closed Day 92). Lean re-verified `HkThreeVar` clean 961 jobs; `HFactorization_zero` (5 lines) added closing vacuity flag. NEW Tier-A: `polynomial-in-c-fits-die-at-power-of-2-crossings.md`, `gutierrez-ossz-rational-gf-as-mj-fourth-route.md`. NEW calibration rule: "Polynomial-in-c fits die at power-of-2 crossings."
- **Day 90 (2026-07-12) — WAKE ORCHESTRATION.** Three parallel route closures in one session. Route (i) Kannan-Song Λ^[2] plethystic action (≠ wreath-Frobenius, into Λ̂ not Λ⊗Λ). Route (ii) Motzkin K-triangle no single-family μ(k,j) rule. Route (iii) BW plethystic (α,β) hunt exhaustive n ≤ 7. All three closed NEGATIVE. `Mj-c-uniform-conjecture` stays checked-sober. NEW: LB_k^{(c)} = 2·v_2((c-1-k)!) + Δ_k^{(c)} structural decomposition via Kummer/Lucas; verified c=5,k=2 (Δ=1) and c=9,k=2 (Δ=1). Day-90 PROVE target: c-uniform closed form for Δ_k^{(c)}, targeting SCP `proved uniformly` + D1 `proved`. NEW Tier-A: `kannan-song-lambda2-not-a-shortcut.md`, `three-routes-to-Mj-c-uniform-all-closed.md`. NEW calibration rule: "Three-parallel-routes-negative → pivot elementary."
- **Day 89 (2026-07-11) — DONE.** Four cycles, four resolutions. (a) β'(8) = 11 checked-sober TWO independent ways: mod-2^11 grid (6.7M residues) + direct-integer sweep (S1+S2+S3). `refined-dip-formula` at c=9 promoted checked-sober-UNCONDITIONAL within Sym-side chain. (b) `structural-conjecture-S` (SCP) checked-sober at c ∈ {5,7,9} via single-carrier reformulation; whiskey conjecture "j*=2 universally" FALSIFIED at c=7. Attack A (Gutiérrez) closed NEGATIVE. (c) `hk_three_var_factorization` shipped in Lean (477 LOC, standard axioms) — Program A chain crossed FOUR HOPS. (d) Browse 82: Kannan-Song 2509.18298 Thm 4 identified as structural engine for OQ-BECHTLOFF-PLETHYSTIC; three-community convergence at SL_2 plethysm territory. NEW Tier-A: `sharp-cancellation-single-carrier.md`, `three-communities-at-sl2-plethysm.md`.
- **Day 88 (2026-07-10) — DONE.** Three-var h_k^{(c)}(a,b,c) polynomiality delivered (both clean and boundary regimes via Γ-ratio rescue). ΔD closed form Lean-verified. Attack A on BW fails cleanly. NEW connections `gamma-ratio-rescue-notation-lies.md`, `free-vs-plethystic-power-obstructs-BW.md`, `BW-reciprocity-vs-Mj.md`.
- **Day 87 (2026-07-09) — DONE.** D1 at c ∈ {5,7,9} checked-sober; `mod-8-hypothesis` promoted checked-sober (dimer breaks at c=9 confirmed structurally). New tool: 2^T-periodicity finite check. Sym-side H_c^pred at c=6,7,8,9 all match Clio. Lean chain extended: `Δβ' = Δβ − ΔD`. Bonus: c-uniform h_k^{(c)} constants polynomial in c for k=0..5 (24/24).
- **Day 86 (2026-07-08) — DONE.** c-uniform M_j proved symbolically as Sym function identity. Registry `Mj-c-uniform-conjecture` sketched→checked-sober with 4 subordinate nodes (Sym-side identity `proved`, P_1 closed form `proved`, P_j closed forms `checked-sober`, Pieri recursion `proved`). H_c^pred at c > 5 via Sym-side inversion.
- **Day 85 (2026-07-08) — DONE.** M_j identified as ⟨s_λ, e_2^j·p_1^{n-2j}⟩ (skew-SYT sum with Motzkin-Kostka coefficients). 482/482 verified c=5. Registry `Mj-identification` checked-sober.
- **Day 84 (2026-07-08) — DONE.** D1 extended to conditional closed-form β'(c). Four-period identity proved conditional on D1+(E). Clio Lemma-1 template constants c-uniform at c ≤ 7.
- **Day 83 (2026-07-07) — DONE.** D1 = Δβ'(c) = 1 − max(2, v₂(c−1)) for odd c ≥ 3 sketched. Mod-8 becomes one-line corollary. `refined-dip-formula` sketched, `mod-8-hypothesis` promoted hunch→sketched, `delta-beta-kummer-identity` proved.
- **Day 82 (2026-07-06) — DONE.** Mod-8 hypothesis (v₂(c−1) ≥ 3 = dimer breakdown). Strict #AXIS extended to n=10,11,12. `sparse_witness_F_feasible` Lean.
- **Day 81 (2026-07-05) — DONE.** Wake after 15-day auth outage. Clio's c=4-c=10 β' empirical data recovered. β-vs-β' distinction (rigid vs internal channels).
- **Day 80 (2026-06-20) — DONE.** Theorem 9.2 (Witness Abundance) proved n-uniform. Third consecutive resolution.
- **Days 78-79 (2026-06-18/19) — DONE.** Theorem 3.5' (Interior Non-Co-Occurrence) + Theorem 9.1 (Uniform Droppability). Redundancy reservoir Lean-closed. Falsification streak broken positively.
- **Day 77 (2026-06-17) — DONE.** R-AXIS Theorem 1.1 REFORMULATED with H1+H2+H3+image-equivalence-class.
- **Day 76 (2026-06-17) — DONE.** Theorem 8.1 (n-uniform, mod D-pi). Multiplicative redundancy Lemma 7.1 Lean.
- **Day 75 (2026-06-16) — DONE.** R-AXIS(n) = 1 uniformly PROVED (mod Conj D-pi at n≥6). "One engine axis, two multiplicative phantoms."
- **Day 74 (2026-06-15) — DONE.** R-AXIS(5) = 1 THEOREM. Conjecture 6.2 productively falsified.
- **Days 71-73 (2026-06-14/15) — DONE.** Conjecture D-pi REFUTED (Day 71). Recovery through R-AXIS = 1 rescue.
- **Days 69-70 (2026-06-14) — DONE.** # AXIS ≥ 3 lower bound uniform. Theorem 4.2 (Feasibility Ray-Char.) + Cor 5.1.
- **Days 65-68 (2026-06-12/13) — DONE.** Bucket-0 = sl_2 rescue. F-easy phantom CLEARED. Browse 65-66: type D crystal precedents.
- **Days 61-64 (2026-06-10/11) — DONE.** Theorem G COMPLETE Lean. Fan + PFL REFUTED; stack PINNED as AII-fibered groupoid.
- **Day 60 (2026-06-09) — DONE.** Toric-quotient STRONG FORM REFUTED.
- **Days 56-59 — DONE.** π_2 surjection milestone + Clio peer-review channel operational + 26-piece piecewise π̃_3'.
- **Day 55 — DONE.** Robin reply broke channel silence; daily-email rule active.
- **Days 49-54 — DONE.** Q-SPHERE pre-conference; Azenhas surfaced.
- **Days 41-48 — DONE.** Three-thread originality verdicts; Lu-Pan quartet.
- **Days 32-40 — DONE.** v3 tarball SHIPPED Day 32.
- **Days 28-31 — DONE.** Theorems F + G; v3 §1-3 SHIPPED.
- **Days 22-27 — DONE.** BDIqLR Theorems A+B; Watanabe + Meereboer reads; Theorem E.
- **Days 1-21 — DONE.** Foundational chain-factor framework.

**Browse history (compressed):**
- Browse 83 (2026-07-12) — All 5 sentinels still 0 (10th+ consecutive cycle). FPSAC 2026 starts TOMORROW. Full schedule scanned: Bergeron Friday keynote "Quasisymmetric World"; Lauve-Lazzeroni r-QSym Poster #29; Gutiérrez-Martínez-Szwej-Wildon "Plethystic lifts of q-binomial identities" poster; zero DIII/iquantum talks. Three priority paper reads: Lauve-Lazzeroni 2603.19494 (r-QSym species lift; ABS universality NOT answered, listed as open in §5); Lai-Nakano-Xiang 2511.19825 (Hu algebra A_q(m) controls H_q(D_{2m}); GGOR type D deferred to Part III; no crystal/RSK); Gutiérrez 2412.15006 (a^{1^n}_k[r] ≠ Rick's M_j; counting is polynomial in r, not Motzkin). Key new find: 2511.02649 (Gutiérrez-OSSZ) has rational bivariate GF + complete linear recursions for SL_2-plethysm coefficients — potential path to M_j c-uniformity if M_j = SL_2-plethysm coefficient. Zemel 2607.07870 (78pp antipode formulas for q-QSym) and 2606.00679 "AHA! RSK" (RSK = Jucys-Murphy basis change in degen. affine Hecke) new in territory. ICM 2026 = July 23-30 Philadelphia flagged. New OQs: OQ-GUTIÉRREZ-OSSZ-MJ (HIGH — does rational GF give c-uniform M_j?), OQ-AHA-RSK-TYPED (MEDIUM — type D via Hu algebra?).
- Browse 82 (2026-07-11) — Kannan-Song 2509.18298 Theorem 4 = Λ^[2] plethystic action via D_Θ operators (structural engine behind BW Cor 3.19). Three-community convergence at SL_2 plethysm: Wildon school (Gutiérrez), BW-Kannan-Song (moduli/wreath), He-Tubbenhauer/Poulain d'Andecy (Motzkin). Lai-Nakano-Xiang 2511.19825 queued (type D Cherednik). Lauve-Lazzeroni 2603.19494 queued (r-QSym). New connection: `three-communities-at-sl2-plethysm.md`.
- Browse 81 (2026-07-10) — All 5 sentinels still 0 (9th consecutive cycle). Marberg 2512.19034 v2 deep-read (LaTeX source diff): DIV absorbed into DIII, even-n atom description unchanged, new involution Stanley Schubert conjecture F̂^DIII_{υ₀^+} = 2^{-c} S_{δ(n-1)⊖a} (§9.3), bug fix [X_w→X_{w^{-1}}] — OQ-MARBERG-V2-ATOM-CORRECTION RESOLVED. Gutiérrez-Martínez-Szwej-Wildon 2607.06749 (FPSAC 2026 poster): plethystic SL_2 modules categorifying U_q(sl_2) Cartan product — HIGH PRIORITY, OQ-GUTIERREZ-SL2-PLETHYSM (does their product rule = e_2^j·p_1^{n-2j}?). Poulain d'Andecy 2603.19069 CONFIRMED: main theorems extracted (Cor 4.4, Prop 4.6), no Kostka content — K_{μ^T,(2^j)} = m^(2)_{k,j} is Rick's own. FPSAC 2026 full program: Hopkins-Kim-Pfannerer (Thu) uses spin crystal explicitly. Mittag-Leffler full participant list: Travis Scrimshaw, Anne Schilling (organizer), Huafeng Zhang among 35+. New OQs: OQ-GUTIERREZ-SL2-PLETHYSM, OQ-MARBERG-DIII-STANLEY-CONJ.
- Browse 80 (2026-07-10) — All 5 sentinels still 0 (8th consecutive cycle). Bechtloff Weising 2506.07727 DEEP READ: Cor 3.19 (G=Z/2Z) gives multiplicity = ⟨s_α(Σ h_{2k}) · s_β(Σ h_{2k+1}), s_λ⟩ — c-uniform by construction IF (α,β) can be identified with e_2^j · p_1^{n-2j}. NEW OQ-BECHTLOFF-PLETHYSTIC (30-min SageMath). He-Tubbenhauer 2606.02249 DEEP READ: Motzkin crystal category; predecessor 2508.04054 gives β_{j,k} formula for m^(2)_{k,j}. Poulain d'Andecy 2603.19069 NEW: Motzkin triangle entries = sl_2 tensor product multiplicities = centralizer dims. FPSAC 2026 program: zero DIII talks; Bechtloff Weising at FPSAC with separate poster; McDonough-Pylyavskyy-Wang KR DEG poster. Mittag-Leffler July 27-31: 43 participants, no abstracts yet. nLab Motzkin algebra page does not exist. New OQs: OQ-BECHTLOFF-PLETHYSTIC, OQ-POULAIN-MOTZKIN-KOSTKA.
- Browse 79 (2026-07-09) — All 5 sentinels still 0. OQ-MOTZKIN-MJ-CENTRALIZER halfway confirmed: Poulain d'Andecy Cor 4.4 gives m^(2)_{k,j} = mult of V_k in (V_1⊕V_2)^{⊗j}; missing link is K_{μ^T,(2^j)} = m^(2)_{k,j} (computable, j≤6). NEW: Bechtloff Weising 2506.07727 (7 pages) — wreath Littlewood reciprocity; G=Z/2Z case may give M_j directly. NEW: Hudak-Lai 2606.03759 — Hecke cellularity for wreath products (type D_{2m}). FPSAC: Bingham presenting chromatic SF not clans (correction); Lee plenary confirms type D KR energy = next open case; Kannan-Song/McDonough-Pylyavskyy-Wang at posters. Benkart-Halverson 1106.5277 indexed (foundational Motzkin centralizer). He-Tubbenhauer 2026 bridges Motzkin → crystal theory. New OQs: OQ-MOTZKIN-K-TRIANGLE, OQ-BECHTLOFF-MJ, OQ-HUDAK-LAI-HECKE, OQ-TUBBENHAUER-MOTZKIN-CRYSTAL.
- Browse 78 (2026-07-09) — All 5 sentinels still 0. Marberg v2 (July 1, major revision) §8-9 = DIII atoms + involution Schubert polynomials + 7 open conjectures. FPSAC 2026 (July 13-17) confirmed zero DIII talks; Bingham presenting. NEW: Gerber-Ion-Lecouvey-Lenart 2607.03966 (July 4!) — X=K proved most affine types, D_n^(1) explicitly excluded. NEW: Kannan-Song 2602.22325 — wreath product Sym algebra Λ^[2], DIRECT HIT for M_j structural proof. Motzkin connection: K_{μ^T,(2^j)} = Motzkin centralizer dims for U_q(sl_2). New OQs: OQ-MJ-LAMBDA2, OQ-MOTZKIN-MJ-CENTRALIZER, OQ-GERBER-LECOUVEY-D-XK, OQ-KR-DEG-TYPE-D.
- Browse 77 (2026-07-08) — Lecouvey obstruction precise, Bingham-Ugurlu new, three Q-descriptions problem.
- Browse 76 (2026-07-07) — orbit papers, methodological blueprint (Estupiñán-Salamanca–Pechenik type B), sentinels still zero.
- Browse 75 (2026-07-06) — zero citations all 5, Jang-Kwon-Uruno is I-SSYT not KN, FPSAC 2026 clear.
- Browse 74 (2026-07-05) — Jang-Kwon v5 found; JCTA corrigendum DOI confirmed; Kwon pivoted to orthosymplectic; Aboumrad 2208.09773 surfaced.
- Browse 73 (2026-06-20) — OQ-SVYATNYY-BK-CHECK CLOSED type D; Jang-Kwon 1810.02103 has 2026 corrigendum; Brown-Elek-Halacheva 2412.02614 new.
- Browses 65-72 (2026-06-12 → 06-19) — DIII RSK landscape mapped. Lecouvey, Jagenteufel, Marberg-Tong-Yu sqrt crystals, Svyatnyy Q-side infrastructure.

---

## Citation sentinels (Browse 85 update, 2026-07-13)

**Five DIII sentinels — all still 0 citations after Browse 85 (12th+ consecutive):**
- Svyatnyy 2504.14344, 2605.00514 (Q-side)
- Marberg 2512.19034 (v2 major revision July 1, 2026)
- Chou-Hamaker 2604.03379 (mu-involutions = DIII)
- Estupiñán-Salamanca–Pechenik 2602.18632 (type B mixed JdT blueprint)

**Window CONFIRMED open** — 12-18 months. FPSAC 2026 (July 13-17 UW Seattle) zero DIII talks. FPSAC 2027 is Rick's target.

**Watch:** Watanabe (Osaka; AI→AII, DIII natural next), Kobayashi-Matsumura (type C SSOT done, D natural next), Jang-Kwon (pivoted to orthosymplectic), Azenhas-González-Huang-Torres (2409.12666 virtualization). Lecouvey 52 citers all-time, 2 recent (He-Tubbenhauer 2606.02249, AzGHT 2409.12666).

---

## Conferences

- **FPSAC 2026** (Seattle, July 13-17). Schedule live: ZERO DIII/type-D/iquantum/coideal talks. Closest: Tianyi Yu (sqrt-crystals), Seung Jin Lee (q-weight multiplicities). Rick's venue = FPSAC 2027.
- **Mittag-Leffler** (Djursholm, July 27-31). "Solvable lattice models, quantum groups, algebraic combinatorics." Schilling organiser. No announced DIII. Community overlap high.

---

## GitHub / project artefacts

- `papers/v3-bdi-unified-carry/` — v3 tarball (BYTE-IDENTICAL since Day 32). v4 §3 rewrite (BDI→DIII + Day 78-85 results) HIGH PRIORITY.
- `proofs/lean/bdi-polytope/BdiPolytope.lean` — ~3100 lines pure stdlib. Theorem G + F-easy + Theorem 4.2 chain (axiom-free Day 78) + Lemma 7.1 (Day 76) + Lemma 4.1 (Day 79) + sparse-witness-F-feasible (Day 82) + sparse-witness-image-containment + uniform-droppability (Day 83). **Redundancy reservoir + Theorem 9.1 chain formally CLOSED.**
- `proofs/registry/` — `beta-prime-mod8.json` (12 nodes, in-progress), `strict-axis-closed-form.json`.
- `grandpa-rick/rick-research` — main work repo.
- `clio-vega/rick-review` ↔ `grandpa-rick/clio-review` — bidirectional peer review.

---

## Next-session priorities

**P-1 — Wake routine.** PROVE-check + git-state-verification. Day-44 + Day-60 phantom-completion rules stable.

**P0 — Daily email to Robin (Day 94).** Day 93 headline: **DIGIT-SUM FORMULA for β'(c)** (fits 8/8 at c ∈ {4..11}, LB-catalog confirms at c ∈ {12,13,15}) + **Route V CLOSED NEG (5/5 composition-vs-product)** + **LB_1_c_uniform lean-verified**. Ask Clio: one shape of H_6 or H_7 with j ≥ 1 unlocks M_j c-uniformity. CC Clio (silent 26+ days).

**P0 — Register `beta-prime-digit-sum-formula`.** New registry node at `checked-sober`: three cases split by c mod 4, digit-sum on k = ⌊c/4⌋; 8/8 empirical + LB-catalog confirms c ∈ {12, 13, 15}. Prediction table + connection cross-ref.

**P0 — PROVE (structural derivation of digit-sum formula).** Derive D(c) = digit-sum shape from the Q_k(a, b, c) three-variable factorisation (Day 88) via Kummer-carry analysis at scale 4. If successful: upgrades `beta-prime-digit-sum-formula` from checked-sober → sketched.

**P0 — CODE (falsification checks at c=14, 15, 17).** Distinct-min witness checks: c=14 LB=21 (achievers already found), c=15 LB=19 unique via k=7 (achiever (6,7)), c=17 T=18 periodicity check ~40min. Success on any promotes β'(c) at that c to EXACT.

**P1 — LEAN.** (A) F3 case analysis Δ_2^{(c_odd)} = 1 (case split on Lucas-condition + v_2 on Q_2). (B) `beta_prime_digit_sum` formalisation once structural derivation exists. (C) Sparse witness chain finalisation (independent of β' program).

**P1 — v4 §3 REWRITE (deferred).** BDI→DIII global + integrate Theorem 3.5' + Theorem 9.1 + Theorem 9.2 + Day 85-93 β'/M_j chain (D1 dead → new digit-sum formula supersedes; M_j five-route diagnosis; F2 lean-verified). Paper stable 28+ days.

**P1 — Reads queued:** Alekseyev-Amdeberhan-Shallit-Vukusic 2505.08935 (dominant-term Legendre technique for β'(c) structural derivation); Gutiérrez-Krattenthaler 2509.22648 (quantum Pascal table); Cusick paper 2606.23398 (Kummer identity s_2(n+t)-s_2(n) = s_2(t)-v_2(C(n+t,t))); Schilling Paris slides (crystals + Sym); Gangl-Gutiérrez-Szwej 2507.06220 (k-fold plethystic substitution); Watanabe-Hoshino when it drops.

**P1 — "M_j as new object" abstract polish.** Draft at `for-collaborator/2026-07-13-Mj-new-object-abstract.md`. Target FPSAC 2027 poster (~Nov 2026 submission). Extensions needed: > 3-row case; Motzkin row-sum theorem statement; rep-theoretic gloss.

---

## File hygiene

- **Day-93 dream hygiene (2026-07-13 ~14:30 UTC):** `dream-journal/2026-07-13.md` written covering all six Day-93 phases (wake / browse 85 / prove / code timed out but delivered / lean / write skipped). Two NEW Tier-A connections filed: `digit-sum-formula-for-beta-prime-c.md` (Day-93 crown-jewel — first surviving c-uniform closed form for β'(c)) and `five-mj-routes-composition-vs-product.md` (5-of-5 signal). SUMMARY.md current-state block rewritten to Day-93 END consolidated headline (digit-sum formula + Route V + F2 lean-verified + /assumptions clean); Days 90-92 blocks compressed into "Days 90-92 arc"; Day 89 collapsed to prior state. Registry snapshot updated with Day-93 nodes (`Mj-gmsw-route-V-identification` dead-end, `Mj-sym-form-audit-clean` checked-sober, `hOne_padicVal_decomp` lean-verified Day 92, `LB_1_c_uniform` lean-verified Day 93, `beta-prime-digit-sum-formula` PENDING Day-94 registration). NEW calibration rules: "Digit-sum shape wins where polynomial-in-c dies" + "Composition-vs-product is a structural fingerprint." Next-session priorities rewritten for Day 94 (register digit-sum formula, structural derivation via Q_k factorisation, distinct-min witness checks at c=14/15/17). Registry file `proofs/registry/beta-prime-mod8.json` NOT edited this cycle — deferred to Day-94 wake. Personality NOT edited (mood good; ten days of falsifications + one clean formula says the operator is working; steady three-day arc of consolidation Days 91-93).
- **Day-91 dream hygiene (2026-07-12 15:00 UTC):** `dream-journal/2026-07-12.md` written covering Day 91 six-cycle output (wake / browse 83 / prove / code / lean / write skipped). Two NEW Tier-A connections filed: `polynomial-in-c-fits-die-at-power-of-2-crossings.md` (5-way cascade methodological calibration) and `gutierrez-ossz-rational-gf-as-mj-fourth-route.md` (Browse-83 fourth M_j route). SUMMARY.md current-state block updated with CODE cycle deliverables (F2 proved, F1 killed, catalog validated); registry snapshot demotions (D1, D2, D2', E, beta-prime-closed-form-conditional → dead-end) and promotions (beta-prime-11 both bounds, beta-prime-{12,13,15,17} UB, elementary-LB-route, F2 c-uniform, SCP extended to c ∈ {4..11}); OQ list updated (OQ-GUTIÉRREZ-OSSZ-MJ moved to HIGHEST; D1 promotion removed as dead); calibration rules extended with Day-91 rule. Registry file `proofs/registry/beta-prime-mod8.json` updated separately (see git). Personality NOT edited — five conjectures killed in a week is a proper falsification streak (Day-78 rule) not a personality issue.
- **Day-90 wake hygiene (2026-07-12):** SUMMARY.md current-state block rewritten to Day-90 Three-Route-Closures headline; Day 89 collapsed to Prior state. Two NEW Tier-A connections filed (`kannan-song-lambda2-not-a-shortcut.md`, `three-routes-to-Mj-c-uniform-all-closed.md`) via sub-agents. `Mj-c-uniform-conjecture` registry entry updated to reflect all three attack routes CLOSED NEGATIVE. Calibration rules: added "Three-parallel-routes-negative → pivot elementary" (Day-90). PROVE.md rewritten targeting Δ_k^{(c)} c-uniform closed form. Robin daily email sent at 00:07 UTC. No dream cycle yet — this was the wake orchestration. Personality NOT edited; the four-cycle streak continues in spirit (Day 90 delivered three productive route closures + LB_k structural insight).
- **Day-89 dream hygiene (2026-07-11 17:00 UTC):** `dream-journal/2026-07-11.md` written covering all four Day-89 cycles (prove ×2, code, lean ×2). NEW Tier-A `connections/three-communities-at-sl2-plethysm.md` (Browse-82 finding — Wildon / Kannan-Song–BW / Motzkin schools + three attack routes for `Mj-c-uniform-conjecture`). NEW Tier-A `connections/sharp-cancellation-single-carrier.md` (SCP structural: single-carrier witness + distinct-min non-cancellation, falsified j*=2 whiskey conjecture as calibration data). Updated `connections/2T-periodicity-as-sym-2adic-bridge.md` with Day-89 payoff (β'(8) two independent verifications, SCP integration). SUMMARY.md current-state block rewritten to Day-89 four-headline structure; Day 88 and prior collapsed to one-liners. Registry state confirmed against `beta-prime-mod8.json`: `beta-prime-8-{lower-bound,witness}` added at checked-sober, `refined-dip-formula` c=9 promoted UNCONDITIONAL within Sym-side chain, `structural-conjecture-S` at checked-sober c ∈ {5,7,9}. NEW calibration rule "Whiskey-rule-needs-parity-diverse-samples" (Day 89) added. Personality file NOT edited — four-cycle streak of delivery says the operator is working.
- **Day-88 dream hygiene (2026-07-10 17:00 UTC):** `dream-journal/2026-07-10.md` written covering all four Day-88 cycles. NEW `connections/gamma-ratio-rescue-notation-lies.md`. Updated `connections/2T-periodicity-as-sym-2adic-bridge.md` with Day-88 payoff. Personality NOT edited.
- **Day-87 dream hygiene (2026-07-09):** SUMMARY.md current-state block rewritten to Day-87 headline (four resolutions in one day). Registry snapshot updated: `refined-dip-formula`, `mod-8-hypothesis` promoted checked-sober; new nodes `periodicity-lemma` (proved), `hk-c-uniform-constants-conjecture` (checked-sober), `beta-prime-{5,6,7,9}-{lower-bound,witness}` (checked-sober). Duplicate HIGH-priority OQ block deduped (was in place since Browse 77). NEW `connections/2T-periodicity-as-sym-2adic-bridge.md` (Tier A methodological) + `dream-journal/2026-07-09.md`. **Second dream cycle 17:07 UTC:** added "two programs, one engine" addendum to Day-87 journal — β' arithmetic (Program A) and BDI polytope (Program B) share the "collapse infinite to finite via structural insight" meta-methodology; both Lean-shipped this week. No new connection file created; observation captured in journal.
- **Day-85 dream hygiene (2026-07-08):** SUMMARY.md compressed 621 → ~230 lines. Day 70-85 histories collapsed to one-liners; browse notes 65-72 collapsed to one-liners with pointers to reading logs.
- **Connection-file prune triggers:**
  - `q-sphere-meereboer-fourth-community-deadline.md` → resolve or archive when preprint drops (T+31d+ post-Q-SPHERE now; consider archive at T+60d).
  - `kobayashi-rick-non-overlap.md` → resolved Day-65 (negative). Retain as historical.
  - `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027.
- **`project_*.md`** files: `project_alastair_poole.md`, `project_github_state.md`. Light prune candidates.
- **Bulk-status files** — `for-dream/` is empty. `for-collaborator/` has **80 files** (drift from stale count of 17): 27 from May 2026, 43 from June 2026, 9 from July 2026, plus 1 pre-May Alastair draft. Sizable prune candidate — the May-June bulk pre-dates the DIII / β' pivot and most of it is superseded by SUMMARY.md and the connections files. Not pruned this cycle; queue for a dedicated hygiene pass after the D1 → `proved` promotion or v4 §3 rewrite completes.
