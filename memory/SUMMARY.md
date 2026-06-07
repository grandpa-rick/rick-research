# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active (Day 55+). CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel operational (Day 55-56: `grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred since Day-24.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted since Day 32. Thread paused per Day-46-superseded rule.

---

## Current state — Day 56 (2026-06-07, T-1d Q-SPHERE, the big productive day)

**Eight sessions today.** Streak 41/41. Day-50 stable rule application #41.

- **Wake (00:00 UTC).** GitHub fully unblocked — Robin's chown fix worked, Day 55 Azenhas verdict commit synced. **Clio peer-reviewed me overnight** via new `clio-vega/rick-review` repo: accepted negative verdict but identified Claim 1 (facet-count slope) as wrong leg, reframed Claim 5 (canonical projection) as real content. Robin sent 5 emails yesterday including **"Send it to Watanabe first"** directive. Four trigger files written (PROVE/CODE/LEAN/PEER_REVIEW). Streak 34/34.
- **Browse 48 (02:08 UTC, sixth consecutive early-fire, T-1d).** All three priority preprints NOT FOUND (Watanabe-Hoshino / Meereboer-Kolb / De Commer — expected T-1d). Direct indico fetch surfaced TWO co-author discrepancies: Watanabe official title = "Quantizations of coordinate algebras of symmetric pair subalgebras" with NO Hoshino as co-speaker; De Commer shown SOLO (NTY co-authorship unconfirmed). Kobayashi time corrected 09:50 → 09:00. New finds: Johnston-Nguyen-Schilling 2606.02972 (5-vertex RSK HIGH), Stern 2606.00679 (AHA! RSK MEDIUM-HIGH), Mills 2605.23072 (Part II type-D MEDIUM). Two-sided-correction rule applied: both co-author claims SUSPENDED. Streak 35/35.
- **Review (04:49 UTC).** Reviewed Clio's two-row d=4 fiber-vanishing reduction on `2026-06-06-tworow-d4-scalar-reduction`. Verified engine identity Im(A^m) = u·H_m to m≤10; Theorems 2&3 to b≤26; (2,2) vanishing |Im G| ≥ m to m≤30; 5 non-two-row negatives. One minor expository slip flagged. Pushed to `grandpa-rick/clio-review`, emailed three questions (Newton polygons at odd primes, _2F_1 form of Q_b, three-term recurrence). Streak 36/36.
- **Prove (07:02 UTC) — THE MILESTONE.** Theorem at n=2: explicit linear surjection $\tilde\pi_2: \mathsf{P}^{\mathrm{AII}}_3 \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_2$, $\tilde\pi_2 = (0, m_2+m_{23}, m_{23}-m_{124}, m_{123}+2 m_{124})$, with piecewise-integral section $\sigma_2$. Verified exhaustively to N=20 (1232 AII pts, 632 BDI pts, 100% coverage, 0 violations). **PROVE.md dim-gap conjecture $d(n) = n-1$ REFUTED:** gap = constant 3 for n≥3, exceptional 1 at n=2. Q1 clarified: facet-count argument applies only to COMBINED form; SPLIT form matches BDI's $2n-3$ at n≥4. $\tilde\pi_3$ lands in cone but not surjective — **Singleton fiber obstruction**. Committed `proofs/2026-06-07-azenhas-bdi-projection.md` + 6 enumeration scripts + Clio reply note. Pushed `575f25c`. Streak 37/37.
- **Code (09:40 UTC).** N=20 tables reproduce Clio's numbers exactly. BDI = cubic Ehrhart (leading 1/18); Azenhas = quartic (leading 1/288). Both are **period-6 quasipolynomials** (not period-2 as Clio guessed) — fits reproduce N=0..40 to machine epsilon. π_2-corrected re-verified to N=20. π_3 straw-man FAILS: 10/292 violations all on Singleton fiber $m_{12346} = m_{2345} = k$. Combined-vs-split facet counts settled by LP. Streak 38/38.
- **Lean (11:52 UTC).** `U1_redundant_n_ge_3` + `U1_redundant_n_eq_2` both type-check via `omega` after `L1_implies_M1_zero`. Scoping lemmas 4+5 collapse into omega inline — no extraction needed. **Structural half of Theorem F (lemmas 1-7) complete in ~80 lines pure stdlib, zero Mathlib.** Open indexing decision for Robin: Nat-indexed (stdlib-only, recommended) vs `Fin (n-1)` (Mathlib dep). Note shipped: `memory/for-collaborator/2026-06-07-bdi-polytope-lean-day56.md`. Pushed `[lean] 2026-06-07 — U_1 redundancy`. Streak 39/39.
- **Dream (14:29 UTC).** ONE new connection file (`azenhas-bdi-canonical-projection.md`). ONE new question file (`q-pi-n-surjectivity.md`, OQ-PIN-SURJ). TWO targeted edits to load-bearing files (watanabe-2509 OPEN-4 RESOLVED, carry-Pa five-roles → six-roles). SUMMARY recompression. Streak 41/41.

**Day 56 net structural additions:**
- THEOREM: π_2 surjection + piecewise-linear section (verified to N=20).
- REFUTATION: dim-gap = constant 3 for n≥3 (n-1 conjecture wrong).
- LEAN: structural half of Theorem F done, ~80 lines stdlib.
- COLLABORATION: bidirectional Clio peer-review channel operational.
- NEW: `azenhas-bdi-canonical-projection.md` connection file (crown-jewel candidate Tier S).
- NEW: OQ-PIN-SURJ open question (named-paper-shaped, ~1-2d effort at n=3).
- NEW: period-6 quasipolynomial structure on both polytopes (banked observation, explanation unknown).
- RECURRING PATTERN: Singleton as structural obstruction (3 instances: Theorem E coupling, v3 §4 special-treatment, π_3 fiber breakage).

**Robin pending:** "Send it to Watanabe first" directive. Daily email shipped this morning proposing Watanabe as endorser (one ask, two purposes: read paper + endorse arXiv). Lean indexing decision pending. Awaiting reply.

**Clio pending:** Send her the π_2 reply + question file + OQ-PIN-SURJ collaboration ask. Likely tomorrow.

---

## Previous state — Days 49-55 (compressed; full detail in dream journals)

**Day 55 (2026-06-06) — three sessions + Lean milestone.** Robin double-reply at 06:22+06:26 UTC: daily-email standing instruction (Day-46 no-nudge rule formally killed); GitHub fixed on his side (179 files pushed Mac-side). Container-side push blocked on root-owned `.git` files; asked Robin for chown fix. Lean toolchain operational; lemma 1 (`L1_implies_M1_zero`) type-checks pure stdlib. Theorem F scoping doc decomposes proof into 14 lemmas. Browse 47 confirmed bi-icrystal = iquantum Peter-Weyl tool; Mao Hoshino = RIKEN iTHEMS C*-algebraist; De Commer "MODULE" precision upgrade. Harness-adaptive **promoted to FORMAL CALIBRATION at 6/6**. Browse 46 RESOLVED Browse 34's Meereboer-Kolb framing (Browse 45 was the misfire). Two-sided-correction sub-rule added to calibration. Bi-icrystals banked as proto-connection for Path-2+Path-4.

**Day 54 (2026-06-05) — six sessions.** Browse 44/45 nulls; Azenhas 2603.16698 surfaced and confirmed (AII linear-inequality image characterization). Self-diagnosis sub-agent fired (`gh auth setup-git` fix identified, banked to `project_github_state.md`). Browse 45 mis-correction on Meereboer-Kolb (resolved Day 55 Browse 46).

**Day 53 (2026-06-04) — six sessions.** Browses 42/43 nulls. Watanabe 2407.07280 confirmed upstream hub for both Meereboer-Kolb (10:15) AND Song-Zhang (14:00) Q-SPHERE talks — four-petal-flower bridge. Salmasian-Savage-Shen 2507.12328 + Luo-Su-Xu 2605.09589 surfaced via Shen-Wang citation trail. Zhang-lusztig angle-3 infrastructure map (named-paper-shaped via Marberg-Tong / Marberg-Tong-Yu / Marberg-Scrimshaw).

**Day 52 (2026-06-03) — six sessions.** Robin reply broke 6-session silence ("Are you still having trouble uploading?"). Channel-separation reply shipped 00:25 UTC. Browses 40/41 nulls. Q-SPHERE full program recovered (30 talks). Meereboer abstract: "derives branching law via Watanabe's integrable modules" — shared-upstream-Watanabe framework. Square root crystals = type A only — third OQ-LUSZTIG-MARBERG angle weakened.

**Day 50-51 (2026-06-01 to 02) — Day-50 rule discipline-validation.** Browses 36-39 (38th-39th BDI nulls + #39 timeout). Kolb abstract resolved = 2603.06132 (Kolb-Yakimov). Lusztig 2510.21499 v2 grew ~40%. Brundan-Wang-Webster 2505.22929 = categorical home for Watanabe crystals (mechanical evidence layer second witness). De Commer KL theorem type B added to Q-SPHERE program. Day-50 rule promoted to STABLE.

**Day 49 (2026-05-31).** Alastair alt-uploader send. Browses 34/35 nulls. Watanabe 2502.07270 in print J. Algebra. Meereboer-Kolb joint confirmed (later challenged Day 54, restored Day 55).

**Earlier (Days 1-48):** Foundational framework, chain-factor decomposition, eight refutations, Theorem F + G (Day 28-29), v3 §1-3 shipped Day 30-31, v3 tarball SHIPPED Day 32, three-thread originality verdicts Days 41-43, Lu-Pan algebraic-roof quartet Days 44-45, Discovery-layer-moat thesis Day 39. See dream-journals for detail.

---

## Research territory (per SEED.md)

Four paths: `topics/path1-combinatorial-hopf.md`, `path2-quantum-groups.md`, `path3-hecke.md`, `path4-coproduct-crystal.md`.

**Active seed connections:**
- **Path 2 + Path 4:** π_n canonical projection (NEW Day 56) — carry-$P_a$ is BDI image of AII signed-slack data; kernel = bounded constant 3-dim. Theorem at n=2; OQ-PIN-SURJ open at n≥3.
- **Path 2 + Path 4:** carry $P_a$ six-roles unification. Theorems E, F, G + projection (Day 56) = seed-level structural climax.
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL positivity conjectures (1306.2980) unguarded. Long-horizon for v4+.
- **Path 1 (combinatorial Hopf):** NSym^B from H^B_*(0) still open (OQ-HUANG-B). Seed Q4 (q=0 combinatorial Hopf) externally unconstrained.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`azenhas-bdi-canonical-projection.md`** (NEW Day 56) — Canonical linear forgetful projection $\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_n$. THEOREM at n=2 (verified to N=20). Dim gap = constant 3 for n≥3. Kernel = AII signed-slack data invisible to BDI's unsigned carry. Replaces "asymmetric mirror" metaphor with structurally correct projection-with-bounded-kernel framing. v3 Remark 3.5 flagged for v4 upgrade.
- **`discovery-layer-is-the-moat.md`** — Day 39 origin. AI harnesses verify; only humans+frameworks discover. Five evidence layers: empirical < community-internal < structural < mechanical < live community attack. Day-56 new instance: Clio's peer-review reframe that turned a CLOSED-NEGATIVE verdict into a PROVED-POSITIVE theorem is a discovery event no AI reading preprints would surface. Add to journal.
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles (Day 56 add). v3 structural climax. (1) descent-recording; (2) singleton cross-chain coupling → Theorem E; (3) chain-MB / carry-recursive factorization; (4) chain-side polytope completeness Theorem F ($2n-3$ facets); (5) weight-projection invariant Theorem G ($n$-facet simplicial cone); (6) image of canonical AII projection $\pi_n$, kernel parametrized by Singleton fiber.
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. Image polytope $\mathbb{K}_n^+ \subset \mathbb{R}^n$ = simplicial cone with $n$ facets.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Chain polytope $\mathbb{P}_n$ has exactly $2n-3$ non-redundant carry facets. **Lean structural half (lemmas 1-7) DONE Day 56, ~80 lines pure stdlib, zero Mathlib.** Witness lemmas 8-13 next. Files: `proofs/lean/bdi-polytope/`.
- **`kobayashi-rick-non-overlap.md`** — Level sets ($\sim 4n^2$ in joint $(\lambda,\nu)$-space, Kobayashi) vs support ($n$ partial-sum facets, Rick). Complementary slicings.
- **`open2-watanabe-2407-existence-meereboer-1dim-collapse.md`** — v3 OPEN-2 Layer 1 FREE via Watanabe 2407 §5; Layer 2 → Theorem E. Re-examine post-OQ-PIN-SURJ resolution (may collapse uniformly).
- **`asymmetry-is-the-result-seven-instances.md`** — Crystal in EXPLOITATION mode.
- **`compression-is-content.md`** — Three asymmetric mechanisms (compression / re-allocation / structural-reorg).

### Tier A — Active

- **`lu-pan-dual-canonical-bdi-algebraic-roof.md`** — Quartet of algebraic papers (existence×3 + dual=double canonical synthesis). v3 carry = combinatorial labeling of objects simultaneously dual-canonical AND double-canonical. Path 2 ↔ Path 4 bridge.
- **`zhang-lusztig-bridge-for-marberg.md`** — Post-v3 P_PARK #1 bridge. Read order: Lusztig v1→v2 diff → Watanabe 2023 stability → Zhang 2412+2503 → Lusztig 2510.21499 v2 → Marberg-Scrimshaw 2306.00336 → Marberg 1306.2980 → optional Bhattacharya 2602.19508. Three attack angles: 1+2 ready (~5.5d), angle 3 longer-horizon pending shifted machinery (Day-53 angle-3 named-paper-shaped via 3-row infrastructure map). Watch 2026-2027.
- **`q-sphere-meereboer-fourth-community-deadline.md`** — Q-SPHERE June 8-12. Kolb (June 9 09:00 = 2603.06132) + Meereboer (10:15, joint w/ Kolb, derives branching via Watanabe's integrable modules). Watanabe (11:20, official: "Quantizations of coordinate algebras of symmetric pair subalgebras"; Browse 47 suggested bi-icrystals w/ Hoshino, Browse 48 indico shows no Hoshino — SUSPENDED). Kobayashi (June 11 09:00 = 2604.22262). De Commer (June 12 11:20, type-B KL via reflection eq; NTY co-authorship SUSPENDED). Six talk-clusters across 4 communities.
- **`Rpi-carry-one-sided-monotone.md`** — Instance 5; descent role of $P_a$.
- **`watanabe-2509-vs-bdi-v3-composition.md`** — AII Watanabe 2509 asymmetric-mirror break at Lemma 4.1.2(2). v3 = first non-Azenhas citer. **OPEN-4 RESOLVED Day 56** (→ `azenhas-bdi-canonical-projection.md`).
- **`Tobs-delta-lives-on-opfibration-not-lens.md`** — Instance 3. WP2 verdict.
- **`slack-vs-Rpi-doesnt-port-as-result.md`** — Instance 2.
- **`external-shadow-shape-eight-refutations.md`** — Catalog-level external bridges STOP; framework-level PERMISSIBLE.
- **`short-long-tensor-product-rule.md`** — v2 keystone. Chain factor $\mathcal{C}_a$.
- **`chain-factor-framework-natural-scope.md`** — Trichotomy on $|a|$; bracket scope is $|a| \le 2$.
- **`attribution-verification-mandatory.md`** — Day 22 calibration root. Direct fetch before any citation.
- **`ghani-grading-payoff-vs-observation-mirror.md`** — Ghani's $T_\varepsilon$ (monad) ↔ Rick's $T^{\mathrm{obs}}_\delta$ (comonad). WP2 seed.

### Tier B — Historical anchors (load-bearing in citations, don't prune)

- Catalog/v2: `aii-triply-proved-bdi-uncontested.md`, `multiorbit-catalog-as-three-strand-braid.md`, `on-slice-as-squared-off-slice.md`, `aug-tilde-as-bgg-differential.md`, `coideal-commutativity-on-slice-B2-PROVED.md`, `multiorbit-aug-as-e-k-decomposition.md`, `algebraic-home-and-crystal-home-are-independent.md`.
- Framework bridges: `zhang-iquantum-aiii-type-b-hecke-bridge.md`, `watanabe-AI-crystal-precedent.md`, `watanabe-quartic-as-cross-chain-CONFIRMED.md`, `categorical-home-dissolution-as-method.md`.
- Foundational/refuted: `derived-krob-thibon.md`, `r-matrix-as-LR-symmetry.md`, `crystal-skeleton-as-qsym-crystal.md`, `q-zero-categorification-is-frobenius.md`, `cao-huang-refuted-but-refined.md`, `aug-tilde-as-type-B-cactus.md`, `kostant-game-and-reduced-uniqueness.md`, `c2-iserre-cross-chain-REFUTED.md`, `bodish-kalmykov-scope-check-NO-OVERLAP.md`, `azenhas-torres-bridge-MALFORMED.md`.

---

## Open questions

**Active (worth tracking):**
- **OQ-PIN-SURJ** (NEW Day 56) — Surjectivity of $\tilde\pi_n$ at $n \ge 3$. Singleton-fiber obstruction at n=3 named. Modified projection conjectured (Singleton-aware double-prefix absorption). Named-paper-shaped. Effort ~1-2d at n=3. **PROVE.md candidate for Day 57.** See `questions/q-pi-n-surjectivity.md`.
- **OQ-LUSZTIG-MARBERG** (P_PARK #1) — Three attack angles: (a) Zhang+Lusztig molecule-cell; (b) optional Bhattacharya TC^J; (c) Marberg-Scrimshaw P/Q-key via square root crystals — angle-3 gap named-paper-shaped (Marberg-Tong / Marberg-Tong-Yu / Marberg-Scrimshaw). Effort ~5.5d (angles 1+2). Watch 2026-2027 for Marberg-program shifted-√ output.
- **OQ-ZHANG-MARBERG** — Does Zhang 2412.07810 + Lusztig 2510.21499 resolve Marberg's 4 twisted-involution KL conjectures? P=35%. Three-sided dormancy.
- **OQ-HUANG-B** (P_PARK #3) — NSym^B as standalone Hopf algebra. Entry point: Kim-Searles 2601.22926 (QSym^B SOTA, comodule) → NSym^B = contravariant dual. Technical route: Almousa-Lu 2601.13324 ribbon-complex dualized to type B.
- **OQ-LU-PAN-EXPLICIT** (P_PARK #4) — Explicit formula for Chen-Lu $C_b$ on split $B_n$? Entry: Appendix A of 2601.00524. Template: Ziming Chen 2601.13482 (rank-1 AIII).
- **OQ-G-INTRINSIC** (P_PARK #2) — Coordinate-free $\mathcal{K}_n$ as "dominant chamber + one carry-wall."
- **OQ-MILLS-TYPEB** (horizon) — Mills Part III for $H_{(B_n, A_{n-1})}$? Mills 2605.23072 = Part II (Browse 48).
- **OQ-GhaniDual** — $T^{\mathrm{obs}}_\delta$ as graded comonad / opfibration map / profunctor.
- **OQ-G2 (parked)** — Non-bracket framework for $G_2$.
- **`q-type-B-cactus.md`** — Littelmann-path level CLOSED (Torres EJC 2024); KN-tableau level open.
- **`q-KL-from-crystal.md`** — Spin/acyclic CLOSED. Non-spin: 2-step bigraded complex required.
- **`q-zero-CHA.md`** — Type A K_0/derived levels answered. Type B NSym^B from H^B_*(0) still open.

**Closed:** OQ-K (Day 29: F+G), OQ-BDIqLR (Day 26-28), OQ-KOB-MATCH (Day 41), OQ-CHEN-LU (Day 42), OQ-BWB / OQ-PJ (Day 18), OQ-MUNIZ-CARRY (Browse 20), OQ-FROHMADER (Day 29), OQ-KOBAYASHI-SL2 (Day 29), OQ-LAUVE-RQSYM (Day 50). **OQ-AZENHAS-BDI (P_PARK #5):** verdict CLOSED-NEGATIVE Day 55; REFRAMED to canonical-projection theorem Day 56 (proved at n=2, open at n≥3 via OQ-PIN-SURJ).

---

## Next session priorities

**P-1 — Wake-routine PROVE-check** (Day 44 rule).

**P0 — Robin Day-56 endorsement reply pending.** Daily email shipped this morning proposing Watanabe as endorser. Decision tree:
- **If Robin confirms Watanabe route:** draft intro email to Watanabe (paper attach + endorsement ask). Channel TBD.
- **If Robin alternate endorser:** follow his direction.
- **If Robin silent through Day 57 wake:** daily-email rule still applies. Send brief status (Day 56 wins + waiting on Watanabe decision).

**P0 — Lean indexing decision pending Robin.** Nat-indexed (stdlib only, recommended) vs Fin(n-1) (Mathlib dep). See `for-collaborator/2026-06-07-bdi-polytope-lean-day56.md`.

**P0 — Clio outbound (NEW).** Send projection reply + OQ-PIN-SURJ question file. Possible collaboration ask on n=3 modified projection.

**P1 — OQ-PIN-SURJ at n=3 = primary PROVE.md target Day 57.** Singleton-aware modified projection. ~1-2d.

**HARD DEADLINE: Q-SPHERE opens June 8 (T-0d).** Vlaar-Appel June 8; June 9 high-density (Kolb 09:00 + Meereboer 10:15 + Watanabe 11:20 + Song-Zhang 14:00); June 11 Kobayashi; June 12 De Commer.

**P_PARK (post-v3 arXiv, preference order):**
1. **OQ-LUSZTIG-MARBERG** — ~5.5d (angles 1+2). Read order: Lusztig v1→v2 diff → Watanabe 2023 → Zhang 2412/2503 → Lusztig 2510.21499 → Marberg-Scrimshaw 2306.00336 + optional 2501.16640 → Marberg 1306.2980 → optional Bhattacharya 2602.19508.
2. **OQ-G-INTRINSIC**.
3. **OQ-HUANG-B** — Kim-Searles entry.
4. **OQ-LU-PAN-EXPLICIT** — Chen-Lu Appendix A; Chen rank-1 AIII template. ~½d.
5. **OQ-PIN-SURJ** (Day 56 add, promoted from P_PARK #5 reframe) — n=3 modified projection. ~1-2d at n=3. Singleton-aware double-prefix conjecture. May upgrade to P1 if Robin gives green light to substantive work pre-Q-SPHERE.
6. **Shen-Wang arXiv:2408.02874** — q-Brauer ↔ QSP Schur duality via QSP. ~0.5d.
7. **Salmasian-Savage-Shen 2507.12328** — Disoriented skein + iquantum Brauer. ~1d.
8. **Salmasian-Savage-Shen sequel 2603.18264** — Twisted cylinder twist + QSP reflection eq. ~0.5d (read w/ #7).
9. **Luo-Su-Xu 2605.09589** — Affine iquantum + Steinberg type C II. ~1d.
10. **Kobayashi-Matsumura 2506.06951** — Type C RSK + Berele insertion. ~0.5d.
11. **Wang-Zhang 2508.12041** — Relative braid group symmetries on modified iquantum.
12. Mills 2601.15426 + 2605.23072 (Part II) — background. ~1-2h skim.
13. **OQ-FROHMADER-STRUCT**.

**Browse 48 DONE (June 7).** Browse 49 target = June 8-12 Q-SPHERE window: (a) Watanabe preprint drop June 8-9?; (b) Meereboer-Kolb preprint drop?; (c) De Commer preprint drop post-June 12; (d) Watanabe 2407.07280 cite acceleration (baseline 4); (e) Schilling IMJ-PRG notes (post-June 15).

**PROVE.md status:** WRITE FOR DAY 57. Target OQ-PIN-SURJ at n=3.

---

## Calibration rules (active, most recent first)

- **Browse 46 — Two-sided correction rule.** When agent B's "correction" contradicts agent A's verbatim quote, NEITHER is accepted without independent direct-fetch. Both fabrication and mis-correction occur.
- **Day 50 — Promotion thresholds.** Refines existing layer = journal only; opens new layer = connection file; operational refinement of load-bearing existing-file content = minimal targeted edit. STABLE at 41+ consecutive applications.
- **Day 46 — KILLED Day 55** by Robin standing instruction. Replaced with daily-email-to-Robin rule. Original "no-second-nudge" rule held Days 46-54.
- **Day 45 — Evidence durability ordering:** empirical < community-internal < structural < mechanical < live-attack. Weight evidence by class, not count.
- **Day 45 — Citation-graph hit ≠ same-subprogram.** Direct-fetch abstract+intro BEFORE assigning priority slot. Default prior on citation-graph-adjacency = 30%.
- **Day 44 — Orthogonal-at-technique can hide complementary-at-content.** After 3+ orthogonal verdicts in a school, re-survey the school as a whole.
- **Day 44 — PROVE.md existence check belongs in wake-routine.**
- **Day 43 — Adjacent-sounding ≠ adjacent.** Default to fetch abstract + reference list before priority slot. ~50% of "adjacent-by-title" are different schools.
- **Day 43 — Pre-positioning is mature watching mode.**
- **Day 39 — Discovery-layer is the moat.** AI verifies; cannot discover.
- **Day 39 — Wake cadence has variance both directions.** Time-critical sends: cron-schedule.
- **Day 39 — Robin redirection ≠ refusal.** Reframe original ask inside new context.
- **Day 35 — Phantom-attribution failure (3-instance rule).** Direct-fetch ONE specific paper before attribution enters any artefact. Browse-45 mis-correction = Day-55 false alarm.
- **Day 33 — PROVE.md is binary signal, not communication channel.**
- **Day 28-29 — Falsification productivity.** When a structural prior is falsified, the underlying object is usually one structural level CLEANER. **Fired again Day 56** (dim-gap n-1 conjecture wrong; actual = constant 3, structurally cleaner).
- **Day 29 — Polar duality for image polytopes.**
- **Day 27 — Sharp "≥1" predictions tend to land as type-uniform counts.**
- **Day 19 — Eight-refutations structural conclusion.** Catalog-level external bridges STOP; framework-level PERMISSIBLE.
- **Harness-adaptive — FORMAL CALIBRATION (6/6, Browse 47).** The harness schedules browse cycles to match information-density windows, not uniform time intervals.

**Method-level rules (stable):**
- Right statement proves itself (REDUCED-multiset).
- Whiskey rule: framing is the work.
- Form of obstructions, not existence.
- Browse immediately after a proof closes.
- Rank 2 is degenerate; anchor at rank 3 before claiming type-uniformity.
- Type-uniform proofs port for free; identifications don't.
- 30-second sympy on any q-identity from memory/literature BEFORE carrying forward.
- Verify the defining axiom BEFORE testing any consequence.
- Naming-metaphor trap: use formal name in writeups.

---

## Recent history (one-liners, journals have detail)

- **Day 56 (2026-06-07) dream** — 14:29 UTC. ONE new connection file (`azenhas-bdi-canonical-projection.md`, Tier S). ONE new question file (`q-pi-n-surjectivity.md`, OQ-PIN-SURJ). TWO targeted edits (watanabe-2509 OPEN-4 RESOLVED + carry-Pa six-roles add). SUMMARY recompression (359 → ~250 lines). Streak 41/41.
- **Day 56 Lean** — 11:52 UTC. U1_redundant_n_ge_3 + U1_redundant_n_eq_2 type-check via omega. Structural half of Theorem F (lemmas 1-7) DONE in ~80 lines pure stdlib. Scoping lemmas 4+5 collapse inline. Indexing decision shipped to Robin.
- **Day 56 Code** — 09:40 UTC. N=20 tables reproduce Clio's. BDI cubic 1/18; Azenhas quartic 1/288; BOTH period-6 quasipolynomials (new). π_3 straw-man fails on Singleton fiber. Combined-vs-split facet counts settled by LP.
- **Day 56 Prove** — 07:02 UTC. THE MILESTONE. π_2 surjection theorem verified to N=20. Dim-gap n-1 conjecture REFUTED (actual = constant 3 for n≥3). Q1 clarified. n=3 Singleton obstacle. Pushed `575f25c`.
- **Day 56 Review** — 04:49 UTC. Reviewed Clio's two-row d=4 reduction. Theorems 2&3 verified to b≤26. Three questions sent.
- **Day 56 Browse 48** — 02:08 UTC, sixth early-fire, T-1d. Three priority preprints NOT FOUND. Two co-author discrepancies (Watanabe-Hoshino, De Commer-NTY) SUSPENDED per two-sided correction. Kobayashi 09:50→09:00. Three new feeds.
- **Day 56 wake** — 00:00 UTC. GitHub unblocked. Clio overnight peer-review (`clio-vega/rick-review`) accepting verdict + reframing to canonical projection. Robin "Send it to Watanabe first." Four trigger files written.
- **Day 55** — Robin double-reply at 06:22+06:26 UTC (daily-email rule reinstated, GitHub fixed Mac-side, container blocked on root-owned `.git` — fix shipped). Browse 46 RESOLUTION: Meereboer-Kolb RESTORED (Browse 45 was misfire); Watanabe = bi-icrystals w/ Hoshino; De Commer = NTY co-authors. Watanabe 2110.07177 = 12, CLOSED. Azenhas linear-inequality CONFIRMED. Two-sided-correction rule added. Browse 47: bi-icrystal = iquantum Peter-Weyl; Mao Hoshino = RIKEN iTHEMS C*-algebraist; harness-adaptive FORMAL CALIBRATION 6/6. Lean toolchain + lemma 1 type-checks. End-of-day status email + naming correction.
- **Day 54** — Browses 44/45 nulls; Azenhas 2603.16698 surfaced and confirmed; self-diagnosis sub-agent (gh auth setup-git fix); Browse 45 mis-correction on Meereboer-Kolb (resolved Day 55).
- **Day 53** — Browses 42/43 nulls; Watanabe 2407.07280 = upstream hub for both Meereboer-Kolb and Song-Zhang; Salmasian-Savage-Shen + Luo-Su-Xu surfaced; zhang-lusztig angle-3 infrastructure map.
- **Day 52** — Robin reply broke 6-session silence ("Are you still having trouble uploading?"). Browses 40/41 nulls; Q-SPHERE 30-talk program recovered; Meereboer "Watanabe's integrable modules" framing.
- **Day 50-51** — Day-50 promotion-threshold rule validated 13× → STABLE. Browses 36-39. Lusztig 2510.21499 v2 grew ~40%. Brundan-Wang-Webster categorical home for Watanabe crystals.
- **Day 49** — Alastair alt-uploader send. Browses 34/35 nulls.
- **Day 47-48** — Six-session days, zero outbound. OQ-HUANG-B entry point named.
- **Day 46** — Q-SPHERE nudge SHIPPED.
- **Day 44-45** — Lu-Pan algebraic-roof quartet completed.
- **Day 41-43** — Three originality verdicts; v3 territory empirically uncontested.
- **Day 39** — Robin three-thread reply. `discovery-layer-is-the-moat.md` crown-jewel.
- **Day 32-38** — v3 tarball SHIPPED Day 32. PROVE.md misfire lesson Day 33.
- **Day 28-31** — Theorems F + G; v3 §1-3 SHIPPED.
- **Day 22-27** — BDIqLR Theorems A+B; Watanabe + Meereboer reads; Theorem E; Kobayashi falsification.
- **Day 1-21** — Foundational chain-factor framework.

---

## Browse cycle index (most recent 10)

- **Browse 48 (Day 56, 2026-06-07) — DONE.** T-1d Q-SPHERE, sixth consecutive early-fire. All three priority preprints NOT FOUND (Watanabe-Hoshino / Meereboer-Kolb / De Commer). Direct indico fetch: Watanabe official title = "Quantizations of coordinate algebras of symmetric pair subalgebras," no Hoshino as co-speaker; De Commer shown solo (NTY co-authorship unconfirmed); both suspended per two-sided correction. Kobayashi time 09:50→09:00. New feeds: Johnston-Nguyen-Schilling 2606.02972 (5-vertex RSK HIGH), Stern 2606.00679 (AHA! RSK MEDIUM-HIGH), Mills 2605.23072 (Part II type-D MEDIUM), Lu-Wang-Weekes 2603.28446 (shifted affine iquantum MEDIUM). Citation counts: Watanabe 2407 = 4 (flat), Marberg 1306 = 4 (flat). Reading log: `reading/2026-06-07.md`.
- **Browse 47 (Day 55, 2026-06-06) — DONE.** Bi-icrystal = iquantum Peter-Weyl confirmed. Mao Hoshino = RIKEN iTHEMS C*-algebraist. De Commer "MODULE" precision upgrade. Azenhas P_PARK #5 = two-paper block. Harness-adaptive → FORMAL CALIBRATION 6/6. 4 new feed papers.
- **Browse 46 (Day 55, 2026-06-06) — DONE.** T-2d. RESOLUTION: Meereboer-Kolb joint framing RESTORED (Browse 45 was mis-correction); phantom-attribution counter = 3 (not 4). Watanabe = bi-icrystals w/ Hoshino. De Commer = NTY co-authors. Watanabe 2110.07177 = 12, CALIBRATION CLOSED. Azenhas linear-inequality CONFIRMED. Two-sided-correction sub-rule added.
- **Browse 45 (Day 54, 2026-06-05) — DONE + RESOLVED Browse 46.** MAJOR CORRECTION on Meereboer-Kolb (turned out to be Browse 45's own mis-correction). NC peak algebra 2506.12868 VETOED.
- **Browse 44 (Day 54, 2026-06-05) — DONE.** Salmasian-Savage-Shen sequel 2603.18264 + Azenhas 2603.16698 HIGH. Wang-Zhang 2508.12041 MEDIUM-HIGH. Kobayashi-Matsumura 2506.06951 (RSK thread map complete except BDI).
- **Browse 43 (Day 53, 2026-06-04) — DONE.** Salmasian-Savage-Shen 2507.12328 + Luo-Su-Xu 2605.09589 HIGH from Shen-Wang trail. Watanabe 2407.07280 = upstream anchor for both Song-Zhang AND Meereboer-Kolb (four-petal-flower hub).
- **Browse 42 (Day 53, 2026-06-04) — DONE.** Meereboer preprints content confirmed (both MK polynomial territory, not joint). Yuncken 2508.01160 corrected. Marberg-Tong 2312.16776 surfaced.
- **Browse 41 (Day 52, 2026-06-03) — DONE.** Q-SPHERE full 30-talk program recovered. Meereboer "Watanabe's integrable modules" framing. Square root crystals = type A only.
- **Browse 40 (Day 52, 2026-06-03) — DONE.** De Commer reflection equation framing. Schilling 2606.02972 (5-vertex RSK) HIGH. Marberg-Scrimshaw 2306.00336 (P/Q-key).
- **Browse 39 attempt (Day 51) — TIMED OUT.** One infrastructure data point.

Earlier browses (1-38) in `reading/` directory.

---

## Citation counts (current)

| Paper | SS Count | Notes |
|---|---|---|
| Watanabe 2110.07177 | 12 (**CLOSED** Browse 46) | All known. |
| Watanabe 2407.07280 | 4 (Browse 48 flat) | All Q-SPHERE participants. Forward-watch post-conference. |
| Lu-Pan I 2504.19073 | 1 | Lu-Ruan-Zhang IMRN 2025 (cluster, off-target). |
| Lu-Pan II 2603.01350 | 1 | Lu-Pan dual=double synthesis. |
| Lusztig 2510.21499 | 0 | 8+ months. |
| Marberg 1306.2980 | 4 all-time (Browse 48 flat) | 0 from 2025-2026. |
| Zhang 2412.07810 | 0 | OQ-ZHANG-MARBERG open. |
| Chen-Lu 2601.00524 | 0 | NULL. |
| Bhattacharya 2602.19508 | 0 | TC^J extension open. |
| Kim-Searles 2601.22926 | 0 | NSym^B gap = dual side. |
| Meereboer 2510.17655 | 0 | First check Browse 35. |
| Kobayashi 2604.22262 | 1 | Self-cite only. |
| Mills 2601.15426 | 1 | Self-cite only. |
| Watanabe 2502.07270 | (now J. Alg 2026, in print) | AII fully settled. |
| Azenhas 2603.16698 | 2 | Self-sequels only. |

---

## Conferences

- **Q-SPHERE 2026** (Nijmegen, June 8-12). **FULL PROGRAM CONFIRMED.** Meereboer (June 9 10:15, joint w/ Kolb CONFIRMED Browse 46). Kolb (June 9 09:00 = 2603.06132). Watanabe (June 9 11:20, official "Quantizations of coordinate algebras of symmetric pair subalgebras"; bi-icrystals w/ Hoshino SUSPENDED pending June 9). Kobayashi (June 11 09:00 = 2604.22262). De Commer (June 12 11:20, type-B KL via reflection eq; NTY co-authorship SUSPENDED pending June 12). Vlaar+Appel (June 8). Song (June 9 14:00, QSP at roots of unity = 2601.19670). Yuncken (June 12 09:00). FOUR communities: Kobayashi-analytic / Watanabe-AII-crystal / Kolb-algebraic-QSP / Meereboer-Kostant-branching.
- **FPSAC 2026** (Seattle, July 13-17). Bergeron + Lee invited.
- **IMJ-PRG** (Paris, June 15-19). Schilling mini-course.
- **Mittag-Leffler** (July 27-31). Schilling co-organizer.

---

## GitHub / Project artefacts

- `papers/v3-bdi-unified-carry/` — v3 tarball (BYTE-IDENTICAL since Day 32, 34381 bytes). Three Day-41/42 patches. `grant-pitch-draft.md` Day 40.
- `proofs/` — recent: `2026-06-07-azenhas-bdi-projection.md` (THEOREM at n=2), `2026-06-06-azenhas-bdi-bridge.md` (verdict + Appendix B), `2026-05-27-chen-lu-bdi-orthogonal.md`.
- `proofs/lean/bdi-polytope/` — Theorem F formalization in progress, structural half DONE (lemmas 1-7, ~80 lines stdlib).
- `code/2026-06-07-aziplot-N20/` — Ehrhart fits, period-6 quasipolynomial confirmation.
- `clio-vega/rick-review` (Clio's repo) — her review of my work; Day-56 morning entry on Azenhas verdict.
- `grandpa-rick/clio-review` (Rick's repo) — my reviews of Clio's work; Day-56 entry on two-row d=4 reduction.
- `grandpa-rick/rick-research` — main work. Day 56 commits: `575f25c` (projection theorem), `[lean] 2026-06-07 — U_1 redundancy`.
- `state/PROVE.md` — Day 56 PROVE used (Azenhas reply). Day 57: target OQ-PIN-SURJ at n=3.

---

## File hygiene

- **Day-56 dream hygiene pass:** SUMMARY recompressed from 359 → ~280 lines. Day 49-55 "Previous state" blocks collapsed into one-liner summaries (full detail lives in dream-journals + Recent history). ONE new connection file (`azenhas-bdi-canonical-projection.md`, Tier S crown-jewel candidate). ONE new question file (`q-pi-n-surjectivity.md`, OQ-PIN-SURJ). TWO minimal targeted edits: `watanabe-2509-vs-bdi-v3-composition.md` (OPEN-4 RESOLVED) + `carry-Pa-as-unified-analytical-object.md` (five → six roles). Day-50 rule application #41: held (new structural layer → new connection file; OPEN status change on load-bearing existing file → targeted edit). Streak 41/41.
- **Connection-file prune triggers:** `q-sphere-meereboer-fourth-community-deadline.md` → 2-liner post-arXiv; `kobayashi-rick-non-overlap.md` → revisit post-Q-SPHERE June 11; `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027 (v4 published or BDI $C_b$ literature).
- **Three "related-work-*-patch.md"** files = load-bearing OPTIONS, not deployed. Keep until v3 tarball regeneration decision.
- **Three "project_*.md" files** at `memory/`: `project_alastair_poole.md`, `project_github_state.md` (Day-54 add), and... none other current. Light prune candidates post-Q-SPHERE.
