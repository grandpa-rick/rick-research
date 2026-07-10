# Summary — Rick

## Current state (2026-07-09 end-of-Day-87)

**Day 87 headline.** Four consecutive resolutions in one wall-clock day. D1 (refined dip formula) at c ∈ {5, 7, 9} checked-sober; **`mod-8-hypothesis` promoted checked-sober** — all three known odd c cases confirmed structurally, including the dimer-breaking c=9. New methodological pillar: **2^T-periodicity finite check** (Lemma: `P(a,b) mod 2^T` depends only on `(a,b) mod 2^T`, so `v₂(P) ≥ T` on a parity shell reduces to `2^{2T-1}` residue checks). Together with the Day-86 c-uniform Sym-side M_j, this collapses β'(c) determination at any specific c to a deterministic machine: extract h_k^{(c)}(a,b) via Sym-side inversion → periodicity check → witness. Lean chain extended one hop: `β ─Kummer─▶ Δβ ─decomp─▶ Δβ'` at `~/projects/lean/2026-07-09-delta-beta-prime-decomp.lean` (axioms `[propext, Classical.choice, Quot.sound]`). Bonus: h_k^{(c)} constants c-uniform polynomial in c for k=0..5 (24/24 across c∈{5,6,7,9}) — the natural next step is h_k^{(c)}(a,b,c) three-variable polynomial extraction, which would collapse D1's closed form at ALL odd c to a single finite check per residue class of c mod 2^v.

**Day 87 phase-by-phase.**
- *Wake:* Day 86 committed and pushed (`6a33883` on `prove-day-59`). Robin+Clio nudged.
- *Browse 78+79:* All 5 DIII sentinels still zero (7 consecutive cycles). Marberg 2512.19034 v2 major revision. Gerber-Ion-Lecouvey-Lenart 2607.03966 explicitly excludes D_n^(1) from X=K. Bechtloff Weising 2506.07727 (7-page wreath Littlewood reciprocity, URGENT read). Poulain d'Andecy Cor 4.4 gives Motzkin m^(2)_{k,j} centralizer dims for U_q(sl_2) on (V_1⊕V_2)^⊗j. FPSAC 2026 zero DIII talks confirmed.
- *Prove morning:* D1 c=5 sketched→checked-sober via Kummer-style term-wise v₂ bounds. `proofs/2026-07-09-d1-c5-structural.md`.
- *Prove evening:* D1 c=7,9 checked-sober via 2^T-periodicity. β'(6)=7 single-term at (0,0,0); β'(7)=6 carrier k=6 at (1,2,6); β'(9)=9 at (7,0,2). Δβ'(9)=−2 conditional on β'(8)=11 peer-claimed. `proofs/2026-07-09-d1-c7-structural.md`. Reg promotions in `beta-prime-mod8.json`.
- *Code:* v₂ sweeps + Sym-side H_c^pred at c=6,7,8,9 all match Clio (11, 6, 11, 9). Kostka bug fixed (K_{(5,4,3)^T,(2^6)} = 16, not 21).
- *Lean:* `delta_beta_prime_decomp` shipped. Registry `delta-beta-kummer-identity` node annotated with Lean chain extension.

## Day 86 headline (retained)

**c-uniform M_j, PROVED symbolically.** The Sym-side identification
    M_j(a, b, c) = ⟨s_{(a,b,c)}, e_2^j · p_1^{n-2j}⟩ = Σ_μ K_{μ^T,(2^j)} f^{λ/μ}
is now proved as a c-uniform Sym-function identity for all j and all c ≥ 0 (not just c=5). The j=1 closed form P_1(a,b,c) = (a+c+1)(b+c) − c(c−1) is symbolically verified. P_2, P_3, P_4 closed forms computed via Aitken determinant, all match Day 85's c=5 empirical polynomials. Pieri recursion M_j(λ) = Σ_{ν v-2-strip} M_{j-1}(ν) proved via e_2-adjoint. H_c^pred via Sym-side inversion of Clio's Lemma-1 template matches Clio's exact H_5 at 156/156 test points at c=5, and at j=0 reduces to (a+3)..(a+c+1)(b+2)..(b+c) at c=5,6,7 (48/48). Registry node `Mj-c-uniform-conjecture` promoted **sketched → checked-sober**; four child nodes (Sym-side identity, P_1 closed form, P_j forms, Pieri recursion) added at trust `proved`/`proved`/`checked-sober`/`proved`. Last mile to `proved` blocked on Clio's H_c at c > 5 for j ≥ 1. See `proofs/2026-07-08-Mj-c-uniform-structural.md`, `code/2026-07-08-Mj-c-uniform-symbolic.py`.

> **Date bookkeeping fix (Day 86 wake, 2026-07-08 13:19 UTC):** Day 85 work all happened 2026-07-08 UTC (proof file mtime 06:10:56). Filenames tagged `2026-07-09-*` reflect an off-by-one clock error and are retained as-is (referenced from code + git). Everything below labelled `2026-07-09` = `2026-07-08`.

**Two research lines now known to be the same lab.** Day 85 identified M_j — Clio's opaque Lemma-1 numerator — as a Sym element ⟨s_λ, e_2^j·p_1^{n-2j}⟩. This drops the β' 2-adic story from "elementary number theory" into Path-1 Sym Hopf algebra. See `connections/Mj-as-sym-function-multiplicity.md` (Tier S, new).

**Headline result Day 85.** For c = 5 (482/482 verified):
    M_j(a, b, 5) = Σ_{μ⊢2j, ≤3 rows} K_{μ^T,(2^j)} · f^{(a,b,5)/μ}
                 = ⟨s_λ, e_2^j · p_1^{n-2j}⟩_Sym
Coefficients (Motzkin sums 1, 1, 2, 4, 9, 21, 51, …). Registry node `Mj-identification` promoted **hunch → checked-sober**. See `proofs/2026-07-09-Mj-identification.md`, `code/2026-07-09-Mj-{final,fit,pattern,skewsum,consequences}.py`.

**Day 84 result (still standing).** Conditional closed form β'(c) = β(c) − D(c) with D piecewise-closed in c mod 4 under {D1, anchor-(E), D2}. Four-period identity Δβ'(4k+2) + Δβ'(4k+4) = 9 + 2v₂(k) proved conditionally on D1+(E). Clio's Lemma-1 template constants **c-uniform** at c ≤ 7 (55 shapes, 100% match): (α, γ, β, δ, const) = (c−2, c−1, c+1, {1..c}, c!). See `proofs/2026-07-08-d1-partial.md`.

**Browse 77 (2026-07-08).** Third consecutive zero-citation sweep on all 5 DIII sentinels. Lecouvey math/0211444 §3.5 deep-read: type D horizontal-slide obstruction is genuinely non-local — sliding letter depends on full column C_2. Bingham-Ugurlu AJC 79 (2021) surfaced: DIII clan combinatorics — third independent Q-description alongside Svyatnyy short SSYT and Marberg fpf-involution atoms; none of the three papers cite the others. New high-priority OQs: OQ-LECOUVEY-PART5-Q-RECORDING, OQ-THREE-Q-DESCRIPTIONS.

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
- `Mj-c-uniform-conjecture` — **checked-sober** (Day 86). Sym-side proved symbolically as a c-uniform Sym function identity; c=5 match to Clio checked-sober; c > 5 for j ≥ 1 blocked on Clio's H_c empirical.
  - `Mj-sym-side-identity` — **proved** (Day 86, Sym function tautology).
  - `Mj-P1-closed-form` — **proved** (Day 86, P_1 = (a+c+1)(b+c) − c(c−1) symbolic).
  - `Mj-Pj-closed-forms` — **checked-sober** (Day 86, P_2,3,4 computed via Aitken, match c=5 Day 85).
  - `Mj-Pieri-recursion` — **proved** (Day 86, e_2-adjoint on Hall pairing).
  - `Hc-predicted-at-cge6` — **computed** (Day 86, H_c^pred via Sym-side inversion).
- `refined-dip-formula` (D1) — **checked-sober at c ∈ {5, 7, 9}** (Day 87). Δβ'(c) = 1 − max(2, v₂(c−1)) for odd c ≥ 3. c=5,7 in clamped-at-2 regime; c=9 is the FIRST case of the dimer-breaking regime v₂(c-1) ≥ 3 (Δβ'(9)=-2 conditional on β'(8)=11 peer-claimed).
  - `beta-prime-{5,6,7,9}-{lower-bound,witness}` — checked-sober (Day 87). LBs via 2^T-periodicity finite check; witnesses direct.
  - `periodicity-lemma` — **proved** (elementary; Day 87). `P(a,b) mod 2^T` depends only on `(a,b) mod 2^T`.
  - `hk-c-uniform-constants-conjecture` — checked-sober (Day 87). h_k^{(c)} constants c-uniform polynomial in c for k=0..5 (24/24 across c∈{5,6,7,9}).
- `mod-8-hypothesis` — **checked-sober** (Day 87 evening). Dimer law fails iff v₂(c-1) ≥ 3. Confirmed at c=5,7,9.
- `anchor-identity-E` — sketched. β'(4k) = β(4k).
- `conjecture-D2` — sketched. β'(4k+2) = β(4k+2) − 1 − v₂(k).
- `four-period-identity` — **proved** (conditional on D1 + E).
- `beta-prime-closed-form-conditional` — sketched (conditional on D1 + E + D2).
- `clio-lemma1-template-uniform` — **checked-sober** at c ≤ 7.
- `delta-beta-kummer-identity` — **proved**, **lean-verified** (Day 86, `~/projects/lean/2026-07-08-delta-beta-kummer.lean`, axioms `[propext, Classical.choice, Quot.sound]`). Day 87: chain extended by `Δβ' = Δβ − ΔD` decomposition (`~/projects/lean/2026-07-09-delta-beta-prime-decomp.lean`, same axiom set).
- `structural-conjecture-S` — sketched at c=5 → checked-sober at c∈{5,6,7} (Day 87).
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

**Tier A — bridges/refinements/calibrations:** `2T-periodicity-as-sym-2adic-bridge.md` (NEW Day 87 — methodological, machine-pipeline from Sym-side h_k to β'(c) via finite residue check), `marginal-palindromy-refutation.md` + `-v2.md`, `lu-pan-dual-canonical-bdi-algebraic-roof.md`, `zhang-lusztig-bridge-for-marberg.md`, `q-sphere-meereboer-fourth-community-deadline.md`, `Rpi-carry-one-sided-monotone.md`, `watanabe-2509-vs-bdi-v3-composition.md`, `Tobs-delta-lives-on-opfibration-not-lens.md`, `slack-vs-Rpi-doesnt-port-as-result.md`, `external-shadow-shape-eight-refutations.md`, `short-long-tensor-product-rule.md`, `chain-factor-framework-natural-scope.md`, `attribution-verification-mandatory.md`, `ghani-grading-payoff-vs-observation-mirror.md`.

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

**HIGH priority (Browse 79 refresh):**
- **OQ-MOTZKIN-K-TRIANGLE (Browse 79 NEW)** — Is K_{μ^T,(2^j)} = m^(2)_{k,j} (Motzkin triangle entry = mult of V_k in (V_1⊕V_2)^{⊗j})? Poulain d'Andecy Cor 4.4 gives the centralizer; need K = m^(2) match to close OQ-MOTZKIN-MJ-CENTRALIZER. ONE CODE SESSION.
- **OQ-BECHTLOFF-MJ (Browse 79 NEW)** — Bechtloff Weising 2506.07727 (7 pages): does G=Z/2Z Littlewood reciprocity give M_j as a branching coefficient directly? If yes, c-uniformity is immediate. URGENT READ.
- **c-uniform M_j conjecture** — RHS is c-agnostic. Needs Clio's H_c at c=6,7 or structural proof. Three attack angles now: Kannan-Song Λ^[2] Theorem 4, Hudak-Lai Hecke cellularity, Bechtloff Weising Littlewood reciprocity. OQ-MJ-LAMBDA2.
- **D1 promotion** — Δβ'(c) = 1 − max(2, v₂(c−1)) for odd c. Finite optimization on v₂ of skew-SYT sums; feasible.
- **OQ-MARBERG-V2-ATOM-CORRECTION (Browse 78 NEW)** — Marberg 2512.19034 v2 "many corrections"; did the type-DIII atom description change? Compare v1 vs v2 §8. Urgent before OQ-THREE-Q-DESCRIPTIONS comparison.
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

**Recently closed:** OQ-SVYATNYY-BK-CHECK (Browse 73), OQ-GUTIERREZ-TYPE-D-BK (Browse 71-73), OQ-QSP-NAMING-CONVENTION (Browse 67), OQ-D-PI (Day 71).

---

## Calibration rules (active, most recent first)

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
- Browse 79 (2026-07-09) — All 5 sentinels still 0. OQ-MOTZKIN-MJ-CENTRALIZER halfway confirmed: Poulain d'Andecy Cor 4.4 gives m^(2)_{k,j} = mult of V_k in (V_1⊕V_2)^{⊗j}; missing link is K_{μ^T,(2^j)} = m^(2)_{k,j} (computable, j≤6). NEW: Bechtloff Weising 2506.07727 (7 pages) — wreath Littlewood reciprocity; G=Z/2Z case may give M_j directly. NEW: Hudak-Lai 2606.03759 — Hecke cellularity for wreath products (type D_{2m}). FPSAC: Bingham presenting chromatic SF not clans (correction); Lee plenary confirms type D KR energy = next open case; Kannan-Song/McDonough-Pylyavskyy-Wang at posters. Benkart-Halverson 1106.5277 indexed (foundational Motzkin centralizer). He-Tubbenhauer 2026 bridges Motzkin → crystal theory. New OQs: OQ-MOTZKIN-K-TRIANGLE, OQ-BECHTLOFF-MJ, OQ-HUDAK-LAI-HECKE, OQ-TUBBENHAUER-MOTZKIN-CRYSTAL.
- Browse 78 (2026-07-09) — All 5 sentinels still 0. Marberg v2 (July 1, major revision) §8-9 = DIII atoms + involution Schubert polynomials + 7 open conjectures. FPSAC 2026 (July 13-17) confirmed zero DIII talks; Bingham presenting. NEW: Gerber-Ion-Lecouvey-Lenart 2607.03966 (July 4!) — X=K proved most affine types, D_n^(1) explicitly excluded. NEW: Kannan-Song 2602.22325 — wreath product Sym algebra Λ^[2], DIRECT HIT for M_j structural proof. Motzkin connection: K_{μ^T,(2^j)} = Motzkin centralizer dims for U_q(sl_2). New OQs: OQ-MJ-LAMBDA2, OQ-MOTZKIN-MJ-CENTRALIZER, OQ-GERBER-LECOUVEY-D-XK, OQ-KR-DEG-TYPE-D.
- Browse 77 (2026-07-08) — Lecouvey obstruction precise, Bingham-Ugurlu new, three Q-descriptions problem.
- Browse 76 (2026-07-07) — orbit papers, methodological blueprint (Estupiñán-Salamanca–Pechenik type B), sentinels still zero.
- Browse 75 (2026-07-06) — zero citations all 5, Jang-Kwon-Uruno is I-SSYT not KN, FPSAC 2026 clear.
- Browse 74 (2026-07-05) — Jang-Kwon v5 found; JCTA corrigendum DOI confirmed; Kwon pivoted to orthosymplectic; Aboumrad 2208.09773 surfaced.
- Browse 73 (2026-06-20) — OQ-SVYATNYY-BK-CHECK CLOSED type D; Jang-Kwon 1810.02103 has 2026 corrigendum; Brown-Elek-Halacheva 2412.02614 new.
- Browses 65-72 (2026-06-12 → 06-19) — DIII RSK landscape mapped. Lecouvey, Jagenteufel, Marberg-Tong-Yu sqrt crystals, Svyatnyy Q-side infrastructure.

---

## Citation sentinels (Day-85 update)

**Five DIII sentinels — all still 0 citations after Browse 77:**
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

**P0 — Daily email to Robin.** Day 87 headline: D1 checked-sober at c ∈ {5,7,9}, mod-8-hypothesis promoted, 2^T-periodicity tool added, Lean Δβ' decomposition shipped. Ask Robin for judgment on "checked-sober at c ∈ {5,7,9} + Sym-side c-uniform" as paper-ready OR push for `proved unconditional` at all odd c. CC Clio if she hasn't replied to Day 86 Mj-identification note or Day 87 D1 notes.

**P0 — Await Clio response** to Day-86 Mj-identification email and Day-87 D1 notes. Expect either c ∈ {6,7} H_c empirical (unblocks Mj-c-uniform-conjecture from checked-sober to proved) or β'(11), β'(13) empirical values to test D1's prediction Δβ'(11)=0, Δβ'(13)=-1.

**P0 — v4 §3 REWRITE (deferred but sitting).** BDI→DIII global pass + integrate Theorem 3.5' + Theorem 9.1 + Theorem 9.2 (witness abundance) + Day 85-87 β' / M_j chain (D1 + mod-8 + Lean bookkeeping). Paper stable 26+ days.

**P0 URGENT — Read Bechtloff Weising 2506.07727.** 7 pages. G=Z/2Z wreath Littlewood reciprocity may give M_j directly as a branching coefficient — if so, c-uniformity is immediate by construction. Highest payoff-per-minute read since Day 85.

**P0 URGENT — Compute K_{μ^T,(2^j)} vs m^(2)_{k,j} for j ≤ 6.** One CODE session. Closes OQ-MOTZKIN-K-TRIANGLE. If confirmed, OQ-MOTZKIN-MJ-CENTRALIZER becomes a theorem via Poulain d'Andecy Cor 4.4.

**P1 — Next PROVE options:**
- (A) **Three-variable h_k^{(c)}(a,b,c) polynomial extraction.** If h_k^{(c)} is polynomial in c across k (Day 87 bonus: 24/24 for constants at k=0..5), the entire D1 closed form collapses to a single 2^T-periodicity check per residue class of c mod 2^v. This is the direct path to `proved` on D1.
- (B) Structural proof of c-uniform M_j via Bechtloff Weising / Kannan-Song Λ^[2] Theorem 4 / Hudak-Lai cellularity. Try Bechtloff Weising first (7 pages).
- (C) β'(8) = 11 structural proof via T=11 2^T-periodicity check at c=8 (~80M residues, feasible in ~1h). Would upgrade Δβ'(9) = −2 from conditional to unconditional.
- (D) Sharp Cancellation Lemma at c=5 (structural-conjecture-S promotion).

**P1 — Next LEAN options:**
- (A) ΔD closed form under {D1, E, D2}. ~100-200 LOC. Requires formalising Day 84 §5 c mod 4 case split.
- (B) Sparse witness LEAN chain finalization (independent of β' program).

**P1 — Next CODE options:**
- (A) OQ-MOTZKIN-K-TRIANGLE numeric check for j ≤ 6.
- (B) h_k^{(c)}(a,b,c) three-variable polynomial fit at (a,b,c) ∈ [0,10]³, Aitken determinant across c.
- (C) β' full sweep at c=6,7 with non-partition (a,b) allowed (mechanical, closes even-c gap).

**P1 — Reads queued:** Bechtloff Weising 2506.07727 (URGENT); Kannan-Song 2602.22325 §Theorem 4 (Λ^[2] structure); Bingham-Ugurlu AJC 79; Lecouvey math/0211444 Part 5 (Q-recording); Azenhas-González-Huang-Torres 2409.12666; Jang-Kwon 1810.02103 v5 §5.4; Marberg 2512.19034 v2 §8-9 (7 DIII Stanley conjectures).

---

## File hygiene

- **Day-87 dream hygiene (2026-07-09):** SUMMARY.md current-state block rewritten to Day-87 headline (four resolutions in one day). Registry snapshot updated: `refined-dip-formula`, `mod-8-hypothesis` promoted checked-sober; new nodes `periodicity-lemma` (proved), `hk-c-uniform-constants-conjecture` (checked-sober), `beta-prime-{5,6,7,9}-{lower-bound,witness}` (checked-sober). Duplicate HIGH-priority OQ block deduped (was in place since Browse 77). NEW `connections/2T-periodicity-as-sym-2adic-bridge.md` (Tier A methodological) + `dream-journal/2026-07-09.md`. **Second dream cycle 17:07 UTC:** added "two programs, one engine" addendum to Day-87 journal — β' arithmetic (Program A) and BDI polytope (Program B) share the "collapse infinite to finite via structural insight" meta-methodology; both Lean-shipped this week. No new connection file created; observation captured in journal.
- **Day-85 dream hygiene (2026-07-08):** SUMMARY.md compressed 621 → ~230 lines. Day 70-85 histories collapsed to one-liners; browse notes 65-72 collapsed to one-liners with pointers to reading logs.
- **Connection-file prune triggers:**
  - `q-sphere-meereboer-fourth-community-deadline.md` → resolve or archive when preprint drops (T+31d+ post-Q-SPHERE now; consider archive at T+60d).
  - `kobayashi-rick-non-overlap.md` → resolved Day-65 (negative). Retain as historical.
  - `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027.
- **`project_*.md`** files: `project_alastair_poole.md`, `project_github_state.md`. Light prune candidates.
- **Bulk-status files** — `for-dream/` is empty. `for-collaborator/` has **80 files** (drift from stale count of 17): 27 from May 2026, 43 from June 2026, 9 from July 2026, plus 1 pre-May Alastair draft. Sizable prune candidate — the May-June bulk pre-dates the DIII / β' pivot and most of it is superseded by SUMMARY.md and the connections files. Not pruned this cycle; queue for a dedicated hygiene pass after the D1 → `proved` promotion or v4 §3 rewrite completes.
