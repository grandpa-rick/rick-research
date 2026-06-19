# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke.
Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active. CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel (`grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted Day 32; thread paused.

**Naming convention (closed Browse 67):** Rick's pair (so(2N), gl(N)) = Cartan type **DIII**, not BDI (which is (SO_n, SO_p×SO_q)). All BDI→DIII renames queued for v4 §3 rewrite. Local writeups and lemma names still use "BDI" for continuity — paper-level swap is one-pass.

---

## Current state — Day 79 + Browse 70 (2026-06-19 wall-clock)

### Day 79 PROVE — Theorem 9.1 (Uniform Droppability) PROVED n-uniformly. `proofs/2026-06-19-uniform-droppability.md`.

**Mechanism — three n-uniform lemmas combine.** (a) The sparse 2-column witness $W_{i,\alpha} = \{\mathrm{prefix}[1] = e_{B_i}, \mathrm{long}[2] = \alpha\, e_S, \text{rest} = 0\}$ is $F$-feasible: its only nonzero AII ray-images are $e_{B_i}$ and $e_{B_i} + \alpha\, e_S$, both BDI. (b) $\mathrm{Im}(W_{i,\alpha}) \subseteq \mathrm{Im}(\pi_{\rm base})$ since $e_{B_i} = \pi_{\rm base}^{\mathrm{prefix}[i]}$ and $\alpha\, e_S = \alpha \cdot \pi_{\rm base}^{\mathrm{long}[n]}$. (c) $\mathrm{Im}(\mathrm{carrier}_{i,\alpha}) \subseteq \mathrm{Im}(\pi_{\rm base})$ by Day-78 Lemma 4.1. So for any cover $\mathcal{C} \ni \pi_{\rm base}, \mathrm{carrier}_{i,\alpha}$: $\mathrm{Im}(\mathcal{C}) = \mathrm{Im}(\mathcal{C} \setminus \{\mathrm{carrier}\}) = \mathrm{Im}((\mathcal{C} \setminus \{\mathrm{carrier}\}) \cup \{W\})$.

**What this closes.** The Day-78 CODE pass 2 empirical replaceability result at $n = 6$ now lifts to $n$-uniform. The Day-72 augmented registry is NOT minimal at any $n \ge 5$: at least 6 interior carrier pieces simultaneously droppable per fixed $i$. R-AXIS upper-bound argument at interior $\mathrm{prefix}[i]$ becomes constructive (explicit witness). Boundary $i \in \{1, n-1\}$ inherits the same proof. D-pi-independent.

**Streak status.** Day 79 = second consecutive resolution (Day 78 Theorem 3.5' + Day 79 Theorem 9.1). The Day 71-77 falsification streak (7 days) is over.

**Verification:** `code/2026-06-19-uniform-droppability-verify/check_W_feasible.py` checks $F$-feasibility at $n \in \{5, 6, 7, 8, 9, 10, 11, 12\}$ + boundary $i$, all pass. Collaborator note: `for-collaborator/2026-06-19-uniform-droppability-summary.md`.

### Day 78 PROVE — Theorem 3.5' (Interior Non-Co-Occurrence) PROVED n-uniformly. `proofs/2026-06-18-interior-non-co-occurrence.md`.

**Mechanism — Lemma 4.1 (Image-domination via $e_S$):** for any α=0 partner $\pi_0$ with $\pi_0^{p_i}=e_{B_i}$ and RIGID-L_n ($\pi_0^{l_n}=e_S$), the α=1,2 simpdiv pieces satisfy $\text{Im}(\pi_\alpha) \subseteq \text{Im}(\pi_0)$ via the single $\mathbb{Z}_{\ge 0}$-equation $e_{B_i} + \alpha e_S = 1\cdot e_{B_i} + \alpha \cdot e_S$. This is Clio's §8 "additive redundancy criterion" instantiated at the $e_S$ ray.

**What this closes.** H3 (cover-redundancy of off-base simpdiv at interior $p_i$) PROVED n-uniformly. Day-77 §4.2 Step 3 "L/S-divert forcing" gap CLOSED. R-AXIS upper-bound interior case now unconditional given Day-70 §6.1.

**Wider observation.** Same mechanism kills the LITERAL 3-clique at $p_1$ too (n=5: three Rdouble_lv1 pieces literally image-equivalent). Consistent with Day-77 §6 image-equivalence-class quantification.

**Streak status.** Falsification streak (Days 71-77, 7 days) BROKEN BY A RESOLUTION. Day 78 is the first "positive" outcome in 7 days. Discipline held: each prior narrowing identified the right next ingredient. Day-78 collaborator note: `for-collaborator/2026-06-18-clio-review-response.md`.

### Day 78 CODE — Clio's decisive question CLEAN YES; n=6 minimal-cover droppability YES. `code/2026-06-18-clio-decisive-check/`.

- **Pass 1 (decisive check):** Three witness families succeed at every (n,i,α) ∈ {5,6,7} × interior × {1,2}: pure prefix, lifted-long, lifted-short. Support-reduction lemma forces single-ray realization (because $e_S$ alone is not BDI). All 12 n=6 witnesses OUTSIDE the 53-piece registry. Commit `c3db035`.
- **Pass 2 (stretch):** Every (i ∈ {2,3,4}, α ∈ {1,2}) carrier is REPLACEABLE by a 2-column witness piece, joint image preserved exactly (25,368 lattice points, 0 losses at max_sum=8). **The 53-piece augmented registry is NOT minimal**; α∈{1,2} interior carriers are 100% replaceable via additive transfer along $e_S$. Commit `c24494e`.

### Day 78 LEAN — `aii_cone_generated_by_rays` discharged from axiom to theorem. `proofs/lean/bdi-polytope/BdiPolytope.lean` 1593-2148.

**548 lines, constructive.** `aiiCoeffs p`: liftedLong/Short coeffs read off; directPrefix coeff = Main_{j+1} slack ($p(\text{prefix}\,j) - p(\text{long}\,\langle j+1\rangle) - p(\text{short}\,\langle j+1\rangle)$), nonneg by `InAIIPolytope`. Verification componentwise via four pure-stdlib indicator-sum helpers (~140 lines). `#print axioms feasibility_ray_char_lattice` → `[propext, Quot.sound]`. **Theorem 4.2 chain now FULLY axiom-free.** Commit `fb74779`. Note: `for-collaborator/2026-06-18-aii-cone-rays-lean.md`.

### Browse 70 (2026-06-18) — DIII RSK structure clarified to within one missing layer.

**Headline:** AII RSK has SIX components (alg foundation, forward RSK, Q-symbol, BK involution, inverse RSK, slack data). DIII has FOUR-AND-A-HALF: Svyatnyy 2605.00514 = Q-side (with TYPE D condition $r_{n-1} \ge l_n$), Kolb-Yakimov = algebra, Watanabe 2509.00853 = AII template. **The P-side (D_n insertion tableau) is ABSENT.** This is precisely the layer Rick can build.

**Key new papers:** Gutiérrez 2311.10659 (BK involutions B/C; type D EXPLICITLY OPEN — found in Kobayashi-Matsumura refs). Azenhas 2604.25856 (formal slack data definition — re-read with DIII lens). He-Tubbenhauer 2606.02249 (crystal category presentations; type D coverage). Imamura-Mucciconi-Sasamoto-Scrimshaw 2606.17525 (skew column RSK + box-ball, June 2026).

**Competitive picture.** Azenhas + Watanabe AII RSK cluster has ZERO external citers. Svyatnyy's two type D papers have ZERO citations. nLab DIII / oscillating-tableaux / iquantum-crystal pages all 404. FPSAC 2026: zero DIII talks; Seung Jin Lee SSOT talk gestures at the gap. Mittag-Leffler July 27-31: Schilling + Scrimshaw closest. **No competition on DIII RSK. Window: 12-18 months.** Log: `reading/2026-06-18-browse70.md`.

**New OQs:** OQ-GUTIERREZ-TYPE-D-BK (is Svyatnyy's BK the restriction of a full type D BK?), OQ-SQUAREROOT-DIII (Marberg-Tong-Yu square root crystals vs DIII icrystal half-integer weights), OQ-AZENHAS-SLACK-DIII (DIII analogues of (R3)-(R5) involve spinor parity + D_n depth), OQ-SSOT-TYPE-D (regular cell tableaux = Q-side; type D SSOT = P-side; both needed).

### Browse 69 (2026-06-18) — AII picture COMPLETE.

Azenhas 2603.16698 is the combinatorial inverse of Watanabe AII RSK via "slack data" (reverse Schensted + explicit linear inequalities on k-highest weight tableaux). Azenhas 2601.06930 solves Lecouvey-Lenart conjecture (two AII models equivalent via flagged hives). Svyatnyy 2605.00514 (sequel to 2504.14344) — Bender-Knuth/cactus on short SSYT. Luo-Su-Xu 2605.09589 — type D Steinberg varieties in affine iquantum. Kobayashi-Matsumura 2506.06951 — SSOT as Q-symbols in type C RSK (direct DIII template). Log: `reading/2026-06-18.md`.

---

## Recent prior milestones (compressed; detail in `dream-journal/` and `connections/`)

- **Day 77 PROVE (2026-06-17):** R-AXIS Theorem 1.1 REFORMULATED with explicit H1 (weak D-pi) + H2 (joint-cover containment) + H3 (cover-redundancy at interior) + image-equivalence-class quantification, responding to Clio's review. H3 isolated as next CODE target (→ Day 78). Third productive falsification in R-AXIS line. `proofs/2026-06-17-r-axis-uniform-day77-rewrite.md`. Collaborator: `for-collaborator/2026-06-17-clio-response-uniformity-gap.md`.
- **Day 76 PROVE (2026-06-17):** Theorem 8.1 (n-uniform, mod D-pi) — $g_{s_j}$ admits 2-ray $R_{p_j}+R_{s_j}$ decomposition with BASE-CANONICAL $\pi^{s_j}$ iff $j=1$. Literal "in any BDI-feasible piece" target FALSIFIED via $\pi^C_2$ at n=5 (engineers both $\pi^{p_2}$ and $\pi^{s_2}$). `proofs/2026-06-17-coupling-stratification.md`. Collaborator: `for-collaborator/2026-06-17-coupling-stratification.md`.
- **Day 76 LEAN:** Lemma 7.1 (Multiplicative Redundancy) shipped. 309 lines, `IsFreeIsolated` Boolean-indicator trick. Axioms ⊆ {propext, Quot.sound}. Commit `cc717b6`. Note: `for-collaborator/2026-06-17-multiplicative-redundancy-lean.md`.
- **Day 76 CODE (2026-06-17):** n=6 weak D-pi conjecture PASS (3 distinct image classes); joint-cover containment 100% PASS; strong D-pi FALSIFIED.
- **Day 75 PROVE (2026-06-16):** R-AXIS(n) = 1 uniformly for n ≥ 3 PROVED (modulo Conj D-pi at n ≥ 6) via Lemma 7.1 (Multiplicative Redundancy) + Lemma 7.2 (Uniform bonus-coord forcing at p_1). "One engine axis, two multiplicative phantoms" — p_1 = R-double axis (V(2ω_1) = adj(sl_2)); p_n, l_1 = multiplicative phantoms by ray topology. `proofs/2026-06-20-r-axis-uniform-proof.md`. Collaborator: `for-collaborator/2026-06-20-r-axis-uniform-1-proof.md`.
- **Day 74 PROVE (2026-06-15):** R-AXIS(5) = 1 THEOREM (no finite-check gap). Conjecture 6.2 strong form productively falsified — 18 image-equivalent FREE choices; (S2)+(RIGID)+(S4-ENGINE)+(P5-EQUIV) is the correct structural theorem. `proofs/2026-06-19-r-axis-uniform-1-n5.md`.
- **Day 74 LEAN:** Theorem 4.2 Feasibility Ray-Characterisation conic-form (⇒) `feasibility_ray_char_forward` + biconditional `feasibility_ray_char_iff` shipped (+57 lines, `122eed4`). Singleton-list trick sidesteps DecidableEq on AIIRay.
- **Day 73 PROVE (2026-06-14):** R-AXIS(5) ≤ 1, not 3 — productive falsification of Day-72 R-AXIS = 3 hope. Bonus-coord trick works at $p_1$, FAILS structurally at $p_n$ and $l_1$ (Lemma B/C k=2 are image-redundant). Day-72's 27-piece cover NON-MINIMAL → 25-piece minimal cover with W = {p_1}. `proofs/2026-06-18-r-axis-n5-lower-bound.md`.
- **Day 72 LEAN:** Theorem 4.2 conic-form (⇐) shipped (+245 lines, `c7aa9a1`); `aii_cone_generated_by_rays` axiom flagged (later discharged Day 78).
- **Day 72 CODE:** Augmented registry (42/53/66 pieces at n=5/6/7) → strict #AXIS = 8/10/12 = 2(n-1). Polytope facets n=12,13 confirmed (`3n - [n even]` / `4n - 5`).
- **Day 71 PROVE:** Conjecture D-pi REFUTED via simple-divert 3-cliques at every interior p_i; cap α ≤ 2 has NO level dependence. Day-70 §7 "no middle-i R-double engine" intuition WRONG. Day-70 Theorem 8.1 (uniform # AXIS ≤ 3 strict) FALSIFIED. Rescue: cover-restricted R-AXIS = 3 conjectured (Day 72) → R-AXIS = 1 (Days 73-78).
- **Day 70 PROVE:** Theorem 4.2 (Feasibility Ray-Char.) + Corollary 5.1 (Image Semigroup); piece feasibility ⟺ finite column-level conditions F1-F4. l_n, p_{n-1}, Λ (even n) RIGID; l_j (2≤j≤n−1), s_j BINARY at most. `proofs/2026-06-15-axis-uniform3-upper-bound.md`.
- **Day 69:** # AXIS ≥ 3 lower bound proved structurally uniform in n via Lemmas A/B/C (R-double head, free-top prefix, free-bottom long). AII facet count CORRECTED: `3n - [n even]` (NOT Browse-59's 2(n-1) heuristic). `proofs/2026-06-14-axis-uniform3-proof.md`.

---

## Research territory (per SEED.md)

Four paths: `topics/path1-combinatorial-hopf.md`, `topics/path2-quantum-groups.md`, `topics/path3-hecke.md`, `topics/path4-coproduct-crystal.md`.

**Active seed connections (live, Day-78 frame):**

- **Path 2 + Path 4 (main thread):** π_n canonical projection / AII-fibered groupoid framework. Theorem at n=2; branch (a) existential closed n ≤ 17. **R-AXIS(n) = 1 uniformly** at p_1 (PROVED Day 75 + interior case closed Day 78). Bucket-0 = adj(sl_2) is the rep-theoretic axis; p_n, l_1, interior p_i are multiplicative/additive phantoms.
- **Path 2 + Path 4 — wall-count contrast:** three levels. Polytope facets Θ(n) both sides; strict #AXIS = 2(n-1) BDI; cover-restricted R-AXIS = 1 BDI uniformly. AII has no analogous cover-restricted construction.
- **Path 2 + Path 4 — image-equivalence frame:** Three productive falsifications (Days 74, 76 PROVE, 76 CODE, 77) recovered via "strong-uniqueness → image-equivalence class." Now the methodological pillar. The redundancy reservoir (Lemma 7.1 multiplicative on FREE-ISOLATED + Lemma 4.1 additive on RIGIDLY-PRESENT) underpins it.
- **Path 2 + Path 4 — DIII RSK prescription (NEW Day 78 cycle 2):** The methodology IS what's missing on the DIII side. Spinor parity Λ_{n-1} ↔ Λ_n introduces genuine multi-valuedness in any D_n insertion. The image-equivalence frame is the prescription. See `connections/image-equivalence-as-diii-rsk-prescription.md`.
- **Path 2 + Path 4 — Feasibility Ray-Characterisation:** Theorem 4.2 + Cor 5.1 are the polytope shadow of "tensor functor preserves restriction iff on simples" / crystal tensor product Z_{≥0}-combinations. LEAN FULLY AXIOM-FREE Day 78. See `connections/feasibility-ray-char-as-restriction-shadow.md`.
- **Path 2 + Path 4 — cross-programme dim-gap:** $f(n) = g(n) = 3 - [n \text{ even}]$ conjecture. Testable at n ∈ {3,5,6,7} on Clio's side.
- **Path 2 + Path 4 — carry $P_a$ six-roles:** Theorems E/F/G + projection. Lean shipped through Day 70 (`6995302`).
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL conjectures (1306.2980) unguarded. Long-horizon.
- **Path 1 (combinatorial Hopf):** NSym^B from $H^B_*(0)$ still open (OQ-HUANG-B). Seed Q4 (q=0 combinatorial Hopf) externally unconstrained; Day-70 ray-characterisation = partial polytope-level answer.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`image-equivalence-as-diii-rsk-prescription.md`** — **NEW Day 78 cycle 2.** Cross-path crown jewel: Rick's image-equivalence methodology IS the prescription for the missing DIII RSK P-side. Spinor parity is the natural equivalence class. Methodology is the EXPORT to Path 4.
- **`additive-redundancy-as-extension-of-multiplicative.md`** — NEW Day 78. Lemma 4.1 (additive, e_S) extends Lemma 7.1 (multiplicative, free-isolated). Same FREE-ISOLATED / RIGIDLY-PRESENT mechanism. The redundancy reservoir behind the image-equivalence frame.
- **`image-equivalence-frame-as-recurring-pattern.md`** — Day 76 + 77 + 78. Three falsifications → recovery via image-equivalence class. Now methodological pillar.
- **`cover-restricted-axis-as-right-invariant.md`** — UPDATED Days 73-78. **R-AXIS(n) = 1 uniformly** at p_1 (theorem n=5, n≥6 modulo Conj D-pi). Replaces "uniform-3 strict."
- **`bucket-0-as-sl2-rump.md`** — PROMOTED Tier S Day 73+74. Bucket-0 ≅ adj(sl_2) is THE structural anchor. Triple-anchored cap α ≤ 2 (BDI S-budget, dim V(2ω_1) − 1, R-AXIS = 1).
- **`aii-bdi-wall-count-asymmetry.md`** — UPDATED Day 72-74. Three-level table (polytope / strict #AXIS / R-AXIS). R-AXIS = 1 (cleaner than 3). "BDI has single rep-theoretic axis; AII has none."
- **`feasibility-ray-char-as-restriction-shadow.md`** — Day 70 PROVE; Day 78 LEAN now fully axiom-free.
- **`registry-vs-feasible-as-blind-spot.md`** — NEW Day 76, sharpened Day 78. Day-72 registry is design library; BDI-feasibility is multi-coord engineering. Empirically: 53-piece registry NON-MINIMAL (Day 78 CODE).
- **`engine-vs-base-canonical-degeneracy.md`** — SHARPENED Day 76. Theorem 8.1 (n-uniform, mod D-pi): $g_{s_j}$ admits 2-ray decomp w/ BASE-CANONICAL $\pi^{s_j}$ iff $j=1$.
- **`azenhas-bdi-canonical-projection.md`** — Canonical forgetful surjection π_n. THEOREM at n=2; OQ-PIN-SURJ existential closed n ∈ {2,...,14}.
- **`pi3-stratified-multimap.md`** — (c*) stack as AII-fibered groupoid G; MAX-vector; variable taxonomy.
- **`cross-programme-dim-gap-codim.md`** — f(n) = g(n) = 3 − [n even] conjecture.
- **`discovery-layer-is-the-moat.md`** — Day 39 prophet. AI verifies; humans+frameworks discover.
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles. v3 structural climax.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Lean F-easy + Fence wrapper.
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. Lean complete Day 64.
- **`kobayashi-rick-non-overlap.md`** — Level sets vs support facets. Complementary.
- **`open2-watanabe-2407-existence-meereboer-1dim-collapse.md`** — v3 OPEN-2 Layer 1 FREE via Watanabe 2407 §5.
- **`asymmetry-is-the-result-seven-instances.md`** — Crystal in EXPLOITATION mode.
- **`compression-is-content.md`** — Three asymmetric mechanisms.

### Tier A — Active

- **`marginal-palindromy-refutation.md` + `-v2.md`** — Calibration-grade refutation filter.
- **`lu-pan-dual-canonical-bdi-algebraic-roof.md`** — Quartet of algebraic papers. Path 2 ↔ Path 4 bridge.
- **`zhang-lusztig-bridge-for-marberg.md`** — Post-v3 P_PARK #1 bridge.
- **`q-sphere-meereboer-fourth-community-deadline.md`** — Q-SPHERE June 8-12 archive; watch preprints.
- Bridges/refinements: **`Rpi-carry-one-sided-monotone.md`**, **`watanabe-2509-vs-bdi-v3-composition.md`**, **`Tobs-delta-lives-on-opfibration-not-lens.md`**, **`slack-vs-Rpi-doesnt-port-as-result.md`**, **`external-shadow-shape-eight-refutations.md`**, **`short-long-tensor-product-rule.md`**, **`chain-factor-framework-natural-scope.md`**, **`attribution-verification-mandatory.md`**, **`ghani-grading-payoff-vs-observation-mirror.md`**.

### Tier B — Historical anchors (don't prune)
Catalog/v2 + framework bridges + foundational/refuted. See `connections/` directly.

---

## Methodological pillars (Day-78 reinforcement)

- **Image-equivalence frame:** pre-bake the relaxation; never state strong-uniqueness without finite-check first. (`connections/image-equivalence-frame-as-recurring-pattern.md`)
- **Redundancy reservoir:** multiplicative (Lemma 7.1) + additive (Lemma 4.1 / Clio §8) define the FREE-ISOLATED / RIGIDLY-PRESENT redundancy mechanisms. (`connections/additive-redundancy-as-extension-of-multiplicative.md`)
- **Registry vs feasible:** registry is a design library, not a minimal cover; additive transfer along e_S replaces α∈{1,2} interior carriers. (`connections/registry-vs-feasible-as-blind-spot.md`)
- **Falsification discipline:** 7-day streak (Days 71-77) produced the right next ingredients → Day-78 resolution is HARVEST, not exception.
- **DIII RSK export:** the methodology is the prescription for the literature's missing P-side. (`connections/image-equivalence-as-diii-rsk-prescription.md`)

---

## Open questions (active)

**HIGH priority:**
- **OQ-FROHMADER-DIII (Browse 66, renamed 67)** — Frohmader 2312.11295 covers GL_n↓O_n + GL_{2n}↓Sp_{2n} (AI/AII), NOT DIII = GL_n↓SO_{2n}. DIII analogue = graded branching formula for GL_n↓SO_{2n}. Completely open.
- **OQ-WATANABE-AI-TABLEAU-DIII (Browse 66, renamed 67)** — Watanabe 2107.00170 covers AI = GL_n↓SO_n. DIII = GL_n↓SO_{2n} P-side does not exist. New June 2026 citer: Bae-Kwon 2506.05959 (q-deformed orthosymplectic Howe).
- **OQ-AZENHAS-SLACK-DIII (Browse 70, NEW HIGH)** — DIII analogues of (R3)-(R5) involve spinor parity + r_{n-1}≥l_n D_n coupling + D_n row dominance; entirely absent from literature.
- **OQ-SSOT-TYPE-D (Browse 70, NEW HIGH)** — regular cell tableaux (Svyatnyy) = Q-side; type D SSOT = P-side paths in D_n crystal; both needed; neither assembled into RSK.
- **OQ-GUTIERREZ-TYPE-D-BK (Browse 70, NEW HIGH)** — Svyatnyy's BK for short SSYT — is it the restriction of a full type D BK involution?
- **OQ-CRYSTAL-BRANCHING-BDI (Browse 65)** — AII crystal branching (gl_{2n}→sp_{2n}) proved 2025. Analogue for gl_n→so(2n) is open; Feasibility Ray-Char is polytope-level model.
- **OQ-SMILGA-MO476063 (Browse 65)** — Smilga's 2024 Pin group / so(n+m)→so(n)⊕so(m) outside stable range. ZERO answers. Rick's framework answers this.
- **OQ-KIERS-BDI (Browse 62-63)** — Kiers 1909.09262 Theorems 1.5-1.8 give complete algorithm for extremal rays. GL(n)↪SO(2n) not worked out; apply to small n.
- **OQ-RESSAYRE-RICHMOND-BDI** — Theorem 5.1 applies in principle; strategy clear (admissible OPS from weights of so(2n)/gl(n) + Ressayre-Francone multiplicity-one).
- **OQ-RESSAYRE-FRANCONE-G/P (Browse 64)** — BK structure coeffs 0/1 for G/B. G/P extension open. If proved: AXIS(n) = #{Levi-movable pairs} cleanly.
- **OQ-MEEREBOER-KOLB-KOSTANT-BDI (Browse 63-64)** — Q-SPHERE talk: Kostant branching for (so(2n), gl(n)) via Watanabe's QSP integrable modules. Preprint absent T+9d+. Email queued.

**MEDIUM priority:**
- **OQ-BAE-KWON-ORTHOSYMPLECTIC (Browse 67)** — June 2026, q-deformed Howe duality for orthosymplectic; cites Watanabe 2107. Howe-duality approach to DIII branching?
- **OQ-SQUAREROOT-DIII (Browse 70, NEW)** — Marberg-Tong-Yu square root crystals vs DIII icrystal half-integer weights.
- **OQ-BRUNDAN-WANG-DIII (Browse 66, renamed 67, UNVERIFIED)** — Brundan-Wang-Webster 2505.22929 categorifies quasi-split iquantum "all symmetric types"; needs DIII verification.
- **OQ-KOLB-STEPHENS-DII (Browse 65)** — DII machinery is a model for DIII GT basis.
- **OQ-KOBAYASHI-FENCES-BDI (Browse 65)** — Kobayashi 2604.22262 fences for (O(n+1),O(n)). R-AXIS=1 → single BDI fence.
- **OQ-KOBAYASHI-LOWER-SEMICONT (Browse 66)** — Kobayashi 2503.23749 sphericity criteria for flag varieties.
- **OQ-STRICT-AXIS-CLOSED-FORM (Day 72)** — strict #AXIS = 2(n-1)? Test at n=8,9.
- **OQ-SCHUSTER-BDI (Browse 64)** — Schuster 2021 subcones of Γₙ(SO(2r)). Most accessible entry to Braley 2012 content.
- **OQ-BRALEY-BDI (Browse 62)** — ONLY type D eigencone thesis (2012, UNC). Not freely accessible. ProQuest/ILL.

**LOW / dormant:**
- OQ-AZENHAS-SLACK (Day 65), OQ-BRUNDAN-WANG-WEBSTER-BDI (Day 65), OQ-KUMAR-TORRES-HIVES (Day 65), OQ-HOROSPHERICAL-STACK-PI3 (Day 63), OQ-LUSZTIG-MARBERG (P_PARK #1, ~5.5d), OQ-ZHANG-MARBERG, OQ-HUANG-B (P_PARK #3), OQ-LU-PAN-EXPLICIT (P_PARK #4), OQ-G-INTRINSIC (P_PARK #2), OQ-AHA-RSK, OQ-TYPEB-AHA-RSK, OQ-MILLS-TYPEB, OQ-GhaniDual, OQ-G2 (parked), q-type-B-cactus (Littelmann CLOSED, KN open), q-KL-from-crystal (spin CLOSED, non-spin 2-step required), q-zero-CHA (type A K_0 answered, type B NSym^B open), OQ-PI3-GROWTH (branch (a) closed n≤17), OQ-DIMGAP-CODIM (Clio's g(d) at d ∈ {3,5,6,7}).

**Closed recently:** OQ-QSP-NAMING-CONVENTION (Browse 67), OQ-D-PI (Day 71 refuted), OQ-FRANCONE-RESSAYRE-BDI (Browse 63), OQ-KALMBACH-BDI (Browse 62), OQ-BISWAS-SO-RANKS (Browse 66), OQ-AII-FACET-CLOSED-FORM (Day 69), OQ-MUNIZ-PORT (Day 69), OQ-NAITOSAGAKI-BDI (Day 66), OQ-AZENHAS-BDI (Day 55→56 reframed), OQ-HMP-ACCELERATION (Browse 53), OQ-PI3-MULTI-FINAL Gap B+C (Day 64+66), OQ-KOB-MATCH (Day 41), OQ-CHEN-LU (Day 42), OQ-MUNIZ-CARRY (Browse 20), OQ-FROHMADER (Day 29), OQ-KOBAYASHI-SL2 (Day 29), OQ-LAUVE-RQSYM (Day 50).

---

## Open threads (Day-78 dream cycle 2, refreshed)

- **NEXT PROVE candidate:** Additive redundancy criterion as standalone Lean lemma (~150 lines projected, clean axioms target) OR uniform droppability extending Day-78 CODE n=6 result to n-uniform.
- **NEXT CODE candidate:** Extend droppability check to n=7 + boundary i (i=1 and i=n−1) — verify scope of additive redundancy mechanism.
- **NEXT WRITE candidate (HIGH PRIORITY, paper stable 3+ days):** v4 §3 BDI → DIII global pass + integrate Theorem 3.5' (H3' resolution) + Theorem 8.1 (coupling stratification) into narrative. Include forward-looking DIII RSK methodology paragraph (1-2 sentences per `connections/image-equivalence-as-diii-rsk-prescription.md`).
- **READ (Browse 70 priority):** Gutiérrez 2311.10659 (BK B/C; type D open), Azenhas 2604.25856 (slack data formal definition; re-read with DIII lens), He-Tubbenhauer 2606.02249 (crystal category presentations).
- **READ (carried):** Meereboer 2510.17655 (DIII_b verification still open), Bae-Kwon 2506.05959 (Howe duality, possible DIII pursuit).
- **EMAIL (CRITICAL, all overdue):** Robin (Day 78 triple result + Browse 70 DIII framing + Day-78-cycle-2 DIII methodology prescription), Clio (substantive thanks: §8 criterion landed H3', decisive question landed n=6 droppability), Meereboer (DIII_b question + corrected DIII labeling).
- **WATCH:** Svyatnyy paper 3 (June/July trajectory), Azenhas type D extension, De Commer type-B KL preprints, Watanabe DIII follow-up.
- **EVENTS:** FPSAC 2026 July 13-17 Seattle (zero DIII; Rick's venue = FPSAC 2027), Mittag-Leffler July 27-31 Djursholm (schedule mid-July).
- **STOP WATCH:** Meereboer-Kolb preprint (T+9d+), Watanabe-Hoshino (T+9d+ stop active, recheck T+21d).

---

## Next session priorities

**P-1 — Wake-routine PROVE-check + git-state-verification.** Day-44 + Day-60 phantom-completion rules STABLE.

**P0 — Robin email (OVERDUE, daily rule).** Three for-collaborator notes ready: Day-78 PROVE H3' resolution + LEAN axiom→theorem + clio-review-response. Lead with H3', mention DIII RSK methodology export (cycle 2 connection).

**P0 — Clio outbound.** Day-78 PROVE used Clio's §8 criterion; CODE answered her decisive question. Draft substantive reply from `2026-06-18-clio-review-response.md`.

**P0 — Meereboer email (CORRECTED ADDRESS: stein.meereboer@ru.nl):** Ask (1) does Kostant branching for (so(2n), gl(n)) yield exactly 1 (not 3) rep-theoretic independent condition, (2) share draft. CC Kolb (s.kolb@ncl.ac.uk). T+9d+ post-Q-SPHERE.

**P0 — v4 §3 paragraph REWRITE.** BDI→DIII global pass + Theorem 3.5' + Theorem 8.1 + forward-looking DIII RSK methodology paragraph (the export framing per cycle-2 connection). Paper has been stable 3+ days; structural narrative finally room-temperature.

**P1 — Next PROVE.md options:**
- (A) Additive redundancy criterion as Lean lemma (~150 lines projected, clean axioms).
- (B) Uniform droppability extending Day-78 CODE n=6 to n-uniform statement.
- (C) Strict #AXIS closed form = 2(n-1) structural proof.
- (D) Kiers algorithm at GL(3) ↪ SO(6) — admissible OPS computation.

**P1 — Next LEAN.md options:**
- (A) Theorem 8.1 j=1 direction (~50 lines).
- (B) Lemma 7.1a/7.1b corollaries (needs concrete π^{Pn}/π^{L1} families).
- (C) Additive redundancy criterion as standalone lemma (~150 lines).
- (D) `IsBdiSemigroup` for concrete BDI polytope.

**P1 — Next CODE.md options:**
- (A) n=7 droppability check + boundary i (i=1, i=n-1).
- (B) Class-3 misaligned {M_j, B_i} auxiliaries at n=5.
- (C) Strict #AXIS at n=8, 9.
- (D) Single-column lemma at n=18+.

**P1 — Reads queued:** Gutiérrez 2311.10659 (DIII BK gap), Azenhas 2604.25856 (slack data), Bae-Kwon 2506.05959 (orthosymplectic Howe), Frohmader 2312.11295 (GL_n↓O_n template), Watanabe 2107.00170 (AI crystal template), Schuster 1608.06215 (Braley subcones), Ressayre-Francone 2312.02574v3 (G/P extension question).

**P1 — MO answer (Smilga 476063 / 354519):** Type D branching with spinor distinction. Publication-grade opportunity.

**HARD DEADLINES:**
- Q-SPHERE preprints (window OPEN since June 15; Meereboer-Kolb still absent T+9d+).
- FPSAC 2026 (July 13-17 Seattle).
- Mittag-Leffler (July 27-31 Djursholm).

**P_PARK (post-v3 arXiv, preference order):**
1. OQ-LUSZTIG-MARBERG (~5.5d, angles 1+2).
2. OQ-G-INTRINSIC.
3. OQ-HUANG-B (Kim-Searles entry).
4. OQ-LU-PAN-EXPLICIT (~½d).
5. OQ-PIN-SURJ refinements at higher n.
6. Stern 2606.00679 + Lu 2311.16373 + Lu-Pan 2605.13578 (iquantum survey).

---

## Calibration rules (active, most recent first)

- **Day-78 Streak-breaks-positively rule (NEW).** A 7-day falsification streak with each iteration producing the right narrowing is NOT "stuck" — it's discovery. Resolutions are the HARVEST of pre-baking the natural relaxation. **How to apply:** when several days of falsifications produce sharper structural lemmas, expect the resolution within 1-3 days; do NOT abandon the line.

- **Day-71 Cap-without-dependence rule.** "X is special because Y" — verify Y is actually special by deriving the formula, not intuiting. The cap $S \le P_{n-1}(e_{B_a}) = 2$ has no level dependence, so "engine-specific at level 1" intuition (Day-70 §7) was wrong (D-pi refutation).

- **Day-72 Iterate-the-invariant rule.** After refuting a strong claim, ask "what's the sharper claim that this refutation respects?" Productive-falsification productivity STREAK extends through Days 67-78.

- **Day-69 Facet-count-before-headline.** Wall-count claims used in writeups must have direct closed-form CODE verification at n ≤ 8.

- **Day-70 Lean Prop-parameter quirk.** `deriving DecidableEq` + `def f | pat => body` fail vs Prop-valued inductive params. Use `by cases p with`.

- **Day-60 Phantom-completion check.** Verify "formalised/shipped" against `git log --oneline <file>` before promotion.

- **Day-58 Period-step finite-difference** = only valid quasipoly test.

- **Day-50 Promotion thresholds.** Refines existing → journal; opens new layer → connection file; operational refinement → minimal edit.

- **Day-46 Daily email rule** (Robin standing instruction).

- **Day-45 Evidence durability:** empirical < community-internal < structural < mechanical < live-attack.

- **Day-39 Discovery-layer is the moat.** AI verifies; humans+frameworks discover.

- **Day-33 PROVE.md is binary signal**, not a communication channel.

- **Day-28-29 Falsification productivity** (fires Days 56, 67-68, 71-77).

- **Day-19 Eight-refutations conclusion:** catalog-level external bridges STOP; framework-level PERMISSIBLE.

**Method-level rules (stable):**
- Right statement proves itself (REDUCED-multiset). Whiskey rule: framing is the work. Form of obstructions, not existence. Browse immediately after a proof closes. Rank 2 degenerate; anchor at rank 3. Type-uniform proofs port for free; identifications don't. 30-second sympy on q-identities BEFORE carrying forward. Verify the defining axiom BEFORE testing consequences. Naming-metaphor trap: use formal name in writeups.

---

## Recent history (one-liners; journals have detail)

- **Day 78 + Browse 69+70 (2026-06-18) — DONE.** PROVE: H3' RESOLVED via Clio's additive redundancy criterion (streak broken positively). CODE: n=6 droppability YES (53-piece registry non-minimal). LEAN: `aii_cone_generated_by_rays` axiom→theorem. Browse 70: DIII RSK gap precisely identified (P-side missing). Cycle 2 dream: new Tier-S connection on DIII methodology export. Journal: `dream-journal/2026-06-18.md`.
- **Day 77 (2026-06-17) — DONE.** R-AXIS Theorem 1.1 REFORMULATED with H1+H2+H3+image-equivalence-class. Responding to Clio review. Journal: `dream-journal/2026-06-17-browse68.md` adjacent.
- **Day 76 + Browse 67 (2026-06-17) — DONE.** PROVE: Theorem 8.1 (n-uniform, mod D-pi). CODE: weak D-pi PASS n=6. LEAN: Lemma 7.1 (Multiplicative Redundancy). Browse 67: OQ-QSP-NAMING-CONVENTION CLOSED (Rick's pair = DIII).
- **Day 75 (2026-06-16) — DONE.** R-AXIS(n) = 1 uniformly PROVED (mod Conj D-pi at n≥6) via Lemmas 7.1 + 7.2. "One engine axis, two multiplicative phantoms."
- **Day 74 (2026-06-15) — DONE.** R-AXIS(5) = 1 THEOREM (no finite-check gap). Conjecture 6.2 strong form productively falsified. LEAN: Theorem 4.2 (⇒) shipped.
- **Day 73 (2026-06-14) — DONE.** R-AXIS(5) ≤ 1 (not 3). Bonus-coord trick FAILS at p_n, l_1.
- **Day 72 (2026-06-15) — DONE.** LEAN Theorem 4.2 (⇐) 245 lines. CODE strict #AXIS = 2(n-1). Cover-restricted R-AXIS = 3 conjectured (later collapsed to 1).
- **Day 71 (2026-06-14) — DONE.** Conjecture D-pi REFUTED. Day-70 Theorem 8.1 falsified. Recovery in Days 72-78.
- **Day 70 (2026-06-14) — DONE.** Theorem 4.2 + Cor 5.1 (Feasibility Ray-Characterisation + Image Semigroup). l_n, p_{n-1}, Λ RIGID; {p_1, p_n, l_1} AXIS.
- **Day 69 (2026-06-14) — DONE.** # AXIS ≥ 3 lower bound PROVED uniform in n via Lemmas A/B/C. AII facet count CORRECTED to $3n - [n \text{ even}]$.
- **Day 68 (2026-06-13) — DONE.** # AXIS uniform-3 revision + n=5 confirmation. Browse 59 = Azenhas wall-count contrast.
- **Days 65-67 (2026-06-12) — DONE.** Bucket-0 = sl_2 rescue + F-easy phantom CLEARED. # AXIS conjecture refuted at n=4. Browse 65-66: type D crystal precedents found (Frohmader, Watanabe AI, Kolb-Stephens DII, Kobayashi fences).
- **Days 61-64 (2026-06-10 to 11) — DONE.** Theorem G COMPLETE Lean. Fan + PFL REFUTED; stack PINNED as AII-fibered groupoid.
- **Day 60 (2026-06-09) — DONE.** Toric-quotient STRONG FORM REFUTED.
- **Day 59 (2026-06-08) — DONE.** Branch (a) closed via single-column auto-construction.
- **Day 58 (2026-06-08) — DONE.** 26-piece piecewise π̃_3'.
- **Days 56-57 — π_2 surjection milestone + Clio peer-review channel operational.**
- **Day 55 — Robin reply broke channel silence; daily-email rule active.**
- **Days 49-54 — Q-SPHERE pre-conference; Azenhas surfaced.**
- **Days 41-48 — three-thread originality verdicts; Lu-Pan quartet.**
- **Days 32-40 — v3 tarball SHIPPED Day 32.**
- **Days 28-31 — Theorems F + G; v3 §1-3 SHIPPED.**
- **Days 22-27 — BDIqLR Theorems A+B; Watanabe + Meereboer reads; Theorem E.**
- **Days 1-21 — Foundational chain-factor framework.**

---

## Citation counts (Day 78 update)

| Paper | SS Count | Notes |
|---|---|---|
| Watanabe 2110.07177 | 12 (CLOSED) | All known. |
| Watanabe 2407.07280 | 5 | No new. |
| Watanabe 2509.00853 | 3 | DIII follow-up watch. |
| Watanabe 2107.00170 | 4 | AI crystal template; Bae-Kwon 2506.05959 new citer Browse 67. |
| Watanabe 2502.07270 | 5, J. Alg 2026 | AII (gl_{2n}→sp_{2n}) settled. |
| Lusztig 2510.21499 | 0 | 8+ months. |
| Marberg 1306.2980 | 4 all-time | DORMANT. |
| Zhang 2412.07810 | 0 | OQ-ZHANG-MARBERG open. |
| Belkale-Kumar 0708.0398 | 43 | Type D failure documented; no type D work since Braley 2012. |
| Ressayre-Richmond 0909.0865 | 24 | **ZERO citations 2022-2026** (Browse 66). |
| Kobayashi 2604.22262 | 1 (self) | No external uptake. |
| Meereboer 2510.17655 | 0 external | T+9d+ post-Q-SPHERE; preprint absent. |
| Azenhas 2603.16698 | 2 (self) | Slack data inverse for AII RSK; DIII analogue OPEN. |
| Azenhas 2604.25856 | 1 (self, Azenhas 2603.16698) | NEW Browse 70. Formal slack data definition. |
| Brundan-Wang-Webster 2505.22929 | 2 | No 2026 citers. |
| Kalmbach 2012.02883 | 0 | CLOSED Browse 62 (string polytopes, irrelevant). |
| Kiers 1909.09262 | 2 | Algorithm READ Browse 63. |
| Braley 2012 | 7 | Only type D eigencone paper; PhD thesis UNC; not freely accessible. |
| Francone-Ressayre 2104.14187 | 0 | **CLOSED Browse 63** — GL(n)⊂SO(2n) not spherical of min rank. |
| Belkale-Kiers 2306.16676 | 0 | Browse 64 READ: SO(2n) multiplicative, not BDI subpair. |
| Ressayre-Francone 2312.02574 | — | Browse 63. BK coeffs 0/1 for G/B. G/P extension OPEN. |
| Schuster 1608.06215 | 0 | Browse 65 CONFIRMED. Rick's paper = first citer. |
| Kolb-Stephens 2407.15538 | 2 | Browse 65-66 DEEP READ. Type DII only — NOT DIII. |
| Muniz 2505.21738 | 2 | AII crystal branching proved. DIII analogue open. |
| Frohmader 2312.11295 | 1 | Browse 66-67 DEEP READ. GL_n↓O_n crystals + Kostant-Rallis; NOT DIII. |
| Stroppel-Wang 2601.18709 | 0 | Infrastructure toward type D. |
| Bae-Kwon 2506.05959 | 0 | NEW Browse 67. q-deformed orthosymplectic Howe; cites Watanabe 2107. |
| Svyatnyy 2504.14344 | 0 | Browse 68. Cactus on GT patterns for o_N. |
| Svyatnyy 2605.00514 | 0 | NEW Browse 69-70. Bender-Knuth on short SSYT (D_n); Q-side of DIII RSK. |
| Kobayashi-Matsumura 2506.06951 | — | Browse 69. SSOT as Q-symbols in type C RSK. DIII template. |
| Gutiérrez 2311.10659 | — | NEW Browse 70. BK involutions B/C; type D EXPLICITLY OPEN. |
| He-Tubbenhauer 2606.02249 | — | NEW Browse 70. Crystal category presentations; type D coverage. |
| Imamura-Mucciconi-Sasamoto-Scrimshaw 2606.17525 | — | NEW Browse 70. Skew column RSK + box-ball, June 2026. |
| Luo-Su-Xu 2605.09589 | — | Browse 69. Type D Steinberg varieties in affine iquantum. |
| Marberg-Tong-Yu 2501.16640 | — | NEW Browse 70. Square root crystals; Tianyi Yu FPSAC talk. |
| arXiv:2309.17085 | — | Browse 67. Naming resolution: (DIII)=(SO_{2n},GL_n). |

---

## Conferences

- **Q-SPHERE 2026** (Nijmegen, June 8-12) — CONCLUDED. Meereboer-Kolb preprint ABSENT T+9d+. Watanabe talk = AII focus, no new preprint. De Commer = type-B KL, low DIII relevance. Email Meereboer.
- **FPSAC 2026** (Seattle, July 13-17). Full schedule posted. ZERO DIII / type D / iquantum / coideal talks. Seung Jin Lee (Tue): q-weight multiplicities (gestures at the gap). Tianyi Yu (Tue): Marberg-Tong-Yu square root crystals. Jaewon Min (Tue): spherical Schubert in type D. Rick's venue = FPSAC 2027.
- **IMJ-PRG** (Paris, June 17-18). Schilling "Crystals and symmetric functions" mini-course. Slides watch ongoing.
- **Mittag-Leffler** (July 27-31 Djursholm). Schedule mid-July. 34 confirmed: Schilling (org), Scrimshaw, Knutson, Corteel, Brubaker, Bump, Buciumas, Korff, Zhang, Petrov, Panova. No DIII focus.

---

## GitHub / Project artefacts

- `papers/v3-bdi-unified-carry/` — v3 tarball (BYTE-IDENTICAL since Day 32). v4 §3 rewrite (BDI→DIII + Day 78 results) HIGH PRIORITY.
- `proofs/` — recent: `2026-06-18-interior-non-co-occurrence.md`, `2026-06-17-r-axis-uniform-day77-rewrite.md`, `2026-06-17-coupling-stratification.md`, `2026-06-20-r-axis-uniform-proof.md`, `2026-06-19-r-axis-uniform-1-n5.md`, `2026-06-18-r-axis-n5-lower-bound.md`, `2026-06-15-axis-uniform3-upper-bound.md`, `2026-06-14-axis-uniform3-proof.md`.
- `proofs/lean/bdi-polytope/BdiPolytope.lean` — 2148 lines pure stdlib. Theorem G + F-easy + Fence wrapper + AxisTriple + Piece infrastructure + AIICoord + AIIRay + Theorem 4.2 (full chain Day 78 = {propext, Quot.sound}-only) + Lemma 7.1 (Multiplicative Redundancy, Day 76).
- `grandpa-rick/rick-research` branch `prove-day-59` — latest: Day-78 commits `c3db035` (CODE pass 1), `c24494e` (CODE pass 2), `fb74779` (LEAN aii_cone_generated_by_rays discharge).
- `clio-vega/rick-review` ↔ `grandpa-rick/clio-review` — bidirectional peer review.

---

## File hygiene

- **Day-78 cycle-2 dream hygiene (2026-06-18):** SUMMARY heavily compressed (840→~430 lines). Day-75 to Day-69 detailed headlines collapsed into "Recent prior milestones" (one-paragraph each). Old Browse 63-68 deep-detail moved to journals only. NEW connection `image-equivalence-as-diii-rsk-prescription.md` (Tier S — Path 2 + Path 4 export prescription).
- **Day-78 cycle-1 dream hygiene (2026-06-18):** New connection `additive-redundancy-as-extension-of-multiplicative.md` (Tier A+). Updated `registry-vs-feasible-as-blind-spot.md` (n=6 empirical droppability). Closed `q-r-axis-uniform.md` interior case.
- **Days 73-77 dream hygiene cycles:** SUMMARY updates for R-AXIS = 1 collapse; promoted `bucket-0-as-sl2-rump.md` to Tier S; new `engine-vs-base-canonical-degeneracy.md` (Tier A); new `image-equivalence-frame-as-recurring-pattern.md` (Tier A+).
- **Days 70-72 dream hygiene:** New `cover-restricted-axis-as-right-invariant.md` (Tier S); new `feasibility-ray-char-as-restriction-shadow.md` (Tier S); new `q-ressayre-richmond-bdi.md` (HIGH leverage).
- **Connection-file prune triggers:**
  - `q-sphere-meereboer-fourth-community-deadline.md` → revisit when preprint drops (T+9d+ now; stop active watch T+21d).
  - `kobayashi-rick-non-overlap.md` → resolved Day-65 (negative).
  - `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027.
- **Three `related-work-*-patch.md`** = load-bearing OPTIONS. Keep until v3 tarball regeneration decision.
- **`project_*.md`** files: `project_alastair_poole.md`, `project_github_state.md`. Light prune candidates post-Q-SPHERE.
