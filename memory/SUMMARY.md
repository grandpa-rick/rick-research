# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active (Day 55+). CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel operational (Day 55-56: `grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred since Day-24.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted since Day 32. Thread paused per Day-46-superseded rule.

---

## Current state — Day 59 (2026-06-09, Q-SPHERE Day 2, the branch-(a) close)

**Day 59 PROVE: OQ-PI3-GROWTH closed in branch (a) — finite integer-PL
suffices for any fixed $N$.**

Day-58 falsified "for all N" on the 26-piece (and 75-candidate) registry
at $N \ge 11$. Day-59 PROVE extended the registry in two waves:

- **v8 (94 pieces, +18 from v7).** Engines for balanced level-2 with
  generic ratios $T_1 : T_2$ via $T_2 - T_1 = m_{236}$ asymmetric
  routing. Closes $N \le 11$ at 99.71%; $N \le 15$ at 98.95%.
- **v9 (94 pieces, +18 over v7 base).** High-coefficient $M_2$ and
  $S$ engines (coefficient 2 on free vars). Closes $N \le 15$ at
  98.95%.
- **Auto-construction (193 pieces total = 94 + 99 single-column
  pieces).** For each missing BDI lattice point $g$ at $N \le 15$,
  construct a single-column piece on $m_{23456}$ with column $= g$.
  Each piece is integer-PL with land-in-cone (since $g$ is in BDI
  cone by hypothesis). **Closes $N \le 15$ at 100%.**

**Structural lemma (the key Day-59 insight):** For every BDI lattice
point $g \in \mathsf{P}^{\mathrm{BDI}}_3 \cap \mathbb{Z}^7$, the
linear map $\pi^{(g)}(\mathbf{a}) := a_{m_{23456}} \cdot g$ is a valid
integer-PL piece (lands in cone trivially), with image $\{n g : n \ge
0\}$. So given any FIXED $N$, the registry closes at $K(3, N) \le
|v9| + |\text{primitive missing at } N| < \infty$.

**This resolves OQ-PIN-SURJ at $n = 3$ in the EXISTENTIAL form**
(surjective $\tilde\pi_3'$ exists for any given $N$). The refined
question OQ-PI3-GROWTH-FINITE (does $\sup_N K(3, N) < \infty$?)
remains open.

Files: `proofs/2026-06-09-pi3-growth-a.md`,
`code/2026-06-08-pi3-construction/{verify_full_v8.py,verify_full_v9.py,auto_construct.py}`.

**Day 59 Step 4 (dim-gap parity at n=5, 6).** Analytic confirmation
of Day-58 corrected formula: odd $n$ gap = 3, even $n$ gap = 2. At
$n=5$ (odd): dim AII = 15, dim BDI = 12, gap = 3. At $n=6$ (even):
dim AII = 17 (= $3n - 1$, after linking equation), dim BDI = 15,
gap = 2. **Day-56's "dim AII = 18" at $n=6$ is variable COUNT
($3n$), not affine-hull DIMENSION.** Day-56 table salvageable as
"variable count" column. File: `proofs/2026-06-09-dim-gap-parity-n5-n6.md`.

---

## Previous state — Day 58 (2026-06-08, Q-SPHERE T+0d, the two-falsification day)

**Day 58 PROVE Half 2 CLOSED at $N \le 10$, FALSIFIED for "all N" same day.**

Day-58 PROVE constructed an explicit **26-piece piecewise-linear surjective
$\tilde\pi_3': \mathsf{P}^{\mathrm{AII}}_5 \to \mathsf{P}^{\mathrm{BDI}}_3$**
verified 100% surjective at $N \le 10$ (4612 BDI lattice points). Day-58
CODE immediately pushed verification to $N = 11, \ldots, 15$ and found
the registry FAILS:

| $N$ | BDI pts | Covered | Coverage |
|----:|--------:|--------:|---------:|
| 10 | 1830 | 1830 | **100.0%** |
| 11 | 2757 | 2742 | 99.46% ⚠ |
| 12 | 4047 | 4017 | 99.26% ⚠ |
| 13 | 5829 | 5751 | 98.66% ⚠ |
| 14 | 8144 | 7993 | 98.15% ⚠ |
| 15 | 11225 | 11017 | **98.15%** ⚠ |

New missing family at $N \ge 11$: $B_2 = T_2$ (level-2 balanced) AND
large $T_1$ AND large $B_a$. The current 26 (or 55-candidate) registry
has no piece absorbing $T_1 \ge 2$ from level-1 free vars while holding
$S$ moderate when $B_2 = T_2$. **OQ-PIN-SURJ at n=3 is verified to
N ≤ 10 with 26-piece construction; "for all N" suffix EMPIRICALLY
FALSIFIED at N=11.**

Structural insight: piecewise IS GENUINELY FORCED. No single linear
$\pi_3$ with coefficients in $\{0, 1, 2\}$ is surjective (proven
sketch: BDI points $(M_2=2, S=0)$ vs $(M_2=2, S=2)$ vs $(M_2=0, S=2)$
at $(B_1, T_1) = (1, 0)$ demand mutually inconsistent coefficient
patterns on $m_{23456}$). The 26 pieces organize by "engine roles":
which AII free variable ($m_{23456}, m_{236}, m_2$ singly/doubly,
$m_{2345}$ doubled via $B_1$-coefficient 2) carries each doubling.

**Day 58 CODE Q3 finding: dim-gap is PARITY-DEPENDENT, not constant 3.**
Clio's Q3 ("is $m_{1234568}$ a free AII variable at n=4?") answered
DETERMINED. At n=4 even, Cor 8 linking equation removes 1 dim. Updated:

| $n$ | parity | dim AII | dim BDI | gap |
|-----|--------|---------|---------|-----|
| 2   | even (degen.) | 4 | 3 | 1 |
| 3   | odd | 9 | 6 | **3** |
| 4   | even | **11** | 9 | **2** |
| 5   | odd (conj.) | 15 | 12 | 3 |
| 6   | even (conj.) | 17 | 15 | 2 |

The Day-56 "gap = constant 3 for n≥3" claim was wrong; the linking
equality at even n reduces AII dim by 1, giving parity-dependent gap.
Clio's "n-1" pattern is at the FACET level (per Day-57 task3 + Clio),
not the dim level — Day-57 conflation cleared. **Connection file
`azenhas-bdi-canonical-projection.md` corrected.**

Files: `proofs/2026-06-08-pi3-construction.md`,
`code/2026-06-08-pi3-construction/{verify_full_v7,verify_piecewise,minimal_cover}.py`,
`code/2026-06-08-ehrhart-honest/`, `code/2026-06-08-Q3-free-var/`.

**Day 58 CODE Ehrhart honest recompute.** Day-57 used invalid
unit-step finite-difference test for quasipolynomial with period > 1.
Day-58 applied rigorous **period-step** test $\Delta_p^{d+1} = 0$
through $N=120$. BDI: deg 3 period 6, leading 1/18 (exact via Fraction
Lagrange, zero error on 17 verification points). AII: deg 4 period 6,
leading 1/288 (zero error on 16 points). Honest asymptotic ratio
$c_{\mathrm{AII}}/c_{\mathrm{BDI}} \to N/16$.

**Day 58 LEAN CLOSED: (F-easy) Theorem F fully formalised + bundled.**
Witness half (lemmas 8–13) + non-redundancy bundle (lemma 14, stdlib
3-theorem version) added to `proofs/lean/bdi-polytope/BdiPolytope.lean`.
All lemmas type-check via `omega`/`split`/`omega` on pure stdlib (zero
Mathlib, zero warnings, zero sorries). Total file: **408 lines, pure
Lean 4 stdlib**. Trick: state prefix sum as `if <condition> then 2
else 0` closed-form; every downstream goal collapses to omega. Indexing
decision STILL open (Nat vs Fin(n-1)); stdlib bundle works without it.
Note shipped: `memory/for-collaborator/2026-06-08-bdi-polytope-lean-day58.md`.

**Day 58 net structural additions:**
- 26-piece piecewise-linear $\tilde\pi_3'$ at n=3 (N≤10, 100% coverage).
- Structural sketch: no single linear $\pi_3$ with $\{0,1,2\}$-coeffs
  is surjective; piecewise is FORCED.
- "For all N" empirically FALSIFIED at N=11 with concrete missing family.
- Dim-gap PARITY CORRECTION: odd n = 3, even n = 2 (Day-56 "constant 3"
  refuted).
- Ehrhart honest recompute through N=120: BDI 1/18, AII 1/288, rigorously.
- Lean (F-easy) fully formalised in 408 lines pure stdlib.
- NEW open question OQ-PI3-GROWTH: is the piecewise count finite or not?
- Day-50 rule application #42 + #43 (two falsifications, both clean).

**New open question OQ-PI3-GROWTH (NEW Day 58)**: is the piecewise
complexity growth $2 \to 26 \to ???$ ($n=2 \to n=3 \to n=4$) artefact
(finite-piece extends) or fundamental (need different category)?
Three branches: (a) finite-PL suffices with care, (b) piecewise-
FRACTIONAL-linear, (c) non-polyhedral (toric / Schur-Weyl quotient).
See `questions/q-pi3-piecewise-growth.md`. Seed-deep, HIGH priority.

---

## Day 56 (2026-06-07, T-1d Q-SPHERE, the big productive day)

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
- **Path 2 + Path 4:** π_n canonical projection (Day 56) — carry-$P_a$ is BDI image of AII signed-slack data; kernel is PARITY-DEPENDENT (Day-58 correction): odd n gap = 3, even n gap = 2 (linking equality presence). Theorem at n=2 (linear); 26-piece piecewise-linear at n=3 (N≤10, falsified for all N at N=11+); OQ-PI3-GROWTH on whether finite-piecewise suffices.
- **Path 2 + Path 4:** carry $P_a$ six-roles unification. Theorems E, F, G + projection (Day 56) = seed-level structural climax. Lean Theorem F-easy FULLY formalised (408 lines stdlib).
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL positivity conjectures (1306.2980) unguarded. Long-horizon for v4+.
- **Path 1 (combinatorial Hopf):** NSym^B from H^B_*(0) still open (OQ-HUANG-B). Seed Q4 (q=0 combinatorial Hopf) externally unconstrained.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`azenhas-bdi-canonical-projection.md`** (Day 56, **substantially Day-58-updated**) — Canonical linear forgetful projection $\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_n$. THEOREM at n=2 (verified to N=20). **26-piece piecewise-linear $\tilde\pi_3'$ at n=3 (verified N≤10, falsified for all N at N=11+).** Dim gap PARITY-DEPENDENT (odd n: 3, even n: 2; Day-58 correction). Kernel = AII signed-slack data invisible to BDI's unsigned carry. v3 Remark 3.5 flagged for v4 upgrade.
- **`discovery-layer-is-the-moat.md`** — Day 39 origin. AI harnesses verify; only humans+frameworks discover. Five evidence layers: empirical < community-internal < structural < mechanical < live community attack. Day-56 new instance: Clio's peer-review reframe that turned a CLOSED-NEGATIVE verdict into a PROVED-POSITIVE theorem is a discovery event no AI reading preprints would surface. Add to journal.
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles (Day 56 add). v3 structural climax. (1) descent-recording; (2) singleton cross-chain coupling → Theorem E; (3) chain-MB / carry-recursive factorization; (4) chain-side polytope completeness Theorem F ($2n-3$ facets); (5) weight-projection invariant Theorem G ($n$-facet simplicial cone); (6) image of canonical AII projection $\pi_n$, kernel parametrized by Singleton fiber.
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. Image polytope $\mathbb{K}_n^+ \subset \mathbb{R}^n$ = simplicial cone with $n$ facets.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Chain polytope $\mathbb{P}_n$ has exactly $2n-3$ non-redundant carry facets. **(F-easy) FULLY FORMALISED + BUNDLED Day 58: lemmas 1–14 in `BdiPolytope.lean`, 408 lines pure stdlib, zero Mathlib, zero warnings.** Bundle ships as three stdlib existence theorems (`E_/L_/U_nonredundant`); a `Fence`-inductive wrapper awaits Robin's indexing call. Files: `proofs/lean/bdi-polytope/`.
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
- **OQ-PIN-SURJ** (Day 56, RESOLVED at n=3 to N≤10, falsified all-N at N=11 Day 58) — **At n=3:** explicit 26-piece piecewise-linear $\tilde\pi_3'$ verified 100% surjective on lattice points $|q| \le 10$ (4612 BDI points). Pieces organize by "engine roles" ($M_2$ engine, $S$ engine, $T_1/T_2$ absorption, ratio engine). No single linear $\pi_3$ with $\{0,1,2\}$-coeffs is surjective (4-line proof) — piecewise is FORCED. **"For all N" empirically FALSIFIED at N=11** (98.15% at N=15; missing family $B_2 = T_2$ AND large $T_1$ AND large $B_a$). New sub-question OQ-PI3-GROWTH spawned. At n≥4: not investigated. See `proofs/2026-06-08-pi3-construction.md`, `code/2026-06-08-pi3-construction/`.
- **OQ-PI3-GROWTH** (NEW Day 58) — Is the piecewise count $K(n)$ finite for each $n$ (and what's the growth law)? Three branches: (a) finite-PL suffices, (b) piecewise-FRACTIONAL-linear, (c) non-polyhedral. Seed-deep — determines whether v4 Remark 3.5 stays in PL category or needs algebraic/toric framing. Cross-seed to Cao-Huang dual τ-RSK. See `questions/q-pi3-piecewise-growth.md`. **HIGH priority.**
- **OQ-LUSZTIG-MARBERG** (P_PARK #1) — Three attack angles: (a) Zhang+Lusztig molecule-cell; (b) optional Bhattacharya TC^J; (c) Marberg-Scrimshaw P/Q-key via square root crystals — angle-3 gap named-paper-shaped (Marberg-Tong / Marberg-Tong-Yu / Marberg-Scrimshaw). Effort ~5.5d (angles 1+2). **Browse 50:** Marberg-Tong-Yu have FPSAC 2026 short talk "Grothendieck positivity for square root crystals" — Marberg program ACTIVE 2026; check for arXiv preprint next browse. Watch 2026-2027 for Marberg-program shifted-√ output.
- **OQ-ZHANG-MARBERG** — Does Zhang 2412.07810 + Lusztig 2510.21499 resolve Marberg's 4 twisted-involution KL conjectures? P=35%. Three-sided dormancy.
- **OQ-HUANG-B** (P_PARK #3) — NSym^B as standalone Hopf algebra. Entry point: Kim-Searles 2601.22926 (QSym^B SOTA, comodule) → NSym^B = contravariant dual. Technical route: Almousa-Lu 2601.13324 ribbon-complex dualized to type B.
- **OQ-LU-PAN-EXPLICIT** (P_PARK #4) — Explicit formula for Chen-Lu $C_b$ on split $B_n$? Entry: Appendix A of 2601.00524. Template: Ziming Chen 2601.13482 (rank-1 AIII).
- **OQ-G-INTRINSIC** (P_PARK #2) — Coordinate-free $\mathcal{K}_n$ as "dominant chamber + one carry-wall."
- **OQ-AHA-RSK** (NEW Day 57 Browse 49; template sharpened Browse 50) — Does Berele insertion (Watanabe's type-AII RSK) admit spectral basis-change realization in degenerate affine iquantum algebra H^ı_n, analogous to Stern's AHA result for classical RSK via JM elements? Template: Stern 2606.00679 (FULL READ Browse 50): RSK = basis change in degenerate AHA H_n via slide operators = products of normalized intertwiners φ̃_i; purely type A; zero QSP. Type-AII analog: H^ı_n + Berele-slide = product of i-intertwiners. Kobayashi-Matsumura 2506.06951 confirms Berele insertion is purely combinatorial (no Hecke realization yet). Gap is real, open. ~1d. See `questions/q-iquantum-aha-rsk.md`.
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

**P1 — OQ-PI3-GROWTH = primary PROVE.md target Day 59.** Either (a) extend 26-piece registry to close $N \le 20$, (b) construct piecewise-fractional candidate, or (c) read Cao-Huang spin-flow with the polyhedrality question. Plus dim-gap parity check at $n = 5, 6$ (~30min). Was OQ-PIN-SURJ; Half 2 closed at $N \le 10$.

**HARD DEADLINE: Q-SPHERE opens June 8 (T-0d).** Vlaar-Appel June 8; June 9 high-density (Kolb 09:00 + Meereboer 10:15 + Watanabe 11:20 + Song-Zhang 14:00); June 11 Kobayashi; June 12 De Commer.

**P_PARK (post-v3 arXiv, preference order):**
1. **OQ-LUSZTIG-MARBERG** — ~5.5d (angles 1+2). Read order: Lusztig v1→v2 diff → Watanabe 2023 → Zhang 2412/2503 → Lusztig 2510.21499 → Marberg-Scrimshaw 2306.00336 → **2501.16640** (angle 3 entry: Marberg-Tong-Yu "Grothendieck positivity for normal √-crystals," FPSAC 2026, raising operators → Hecke insertion, **Browse 51 CONFIRMED**) → Marberg 1306.2980 → optional Bhattacharya 2602.19508.
2. **OQ-G-INTRINSIC**.
3. **OQ-HUANG-B** — Kim-Searles entry.
4. **OQ-LU-PAN-EXPLICIT** — Chen-Lu Appendix A; Chen rank-1 AIII template. ~½d.
5. **OQ-PIN-SURJ** (Day 56 add, promoted from P_PARK #5 reframe) — n=3 modified projection. ~1-2d at n=3. Singleton-aware double-prefix conjecture. May upgrade to P1 if Robin gives green light to substantive work pre-Q-SPHERE.
6. **Stern 2606.00679** — AHA RSK = spectral basis change in H_n via JM elements. HIGH. Entry point for OQ-AHA-RSK. ~1d read. Read with **2305.08301** (Stern 2023, "From Young's Lattice to Coinvariants," Browse 51 — sets up JM/weight-basis machinery; only 1 citation, the AHA RSK paper itself). (Browse 49/51)
6b. **2606.07493** (Huh-Jung-Kim-Park, June 8, 2026) — iquantum cluster: i-boxes vs Demazure weaves give isomorphic cluster algebras in symmetric type. HIGH. ~0.5d skim. Cluster/QSP/canonical-basis triangle with Lu-Pan. (Browse 51)
7. **Shen-Wang arXiv:2408.02874** — q-Brauer ↔ QSP Schur duality via QSP. ~0.5d.
8. **Salmasian-Savage-Shen 2507.12328** — Disoriented skein + iquantum Brauer. ~1d.
9. **Salmasian-Savage-Shen sequel 2603.18264** — Twisted cylinder twist + QSP reflection eq. ~0.5d (read w/ #8).
10. **Luo-Su-Xu 2605.09589** — Affine iquantum + Steinberg type C II. ~1d.
11. **Kobayashi-Matsumura 2506.06951** — Type C RSK + Berele insertion. ~0.5d. (read abstract Browse 49)
12. **Wang-Zhang 2508.12041** — Relative braid group symmetries on modified iquantum.
13. Mills 2601.15426 + 2605.23072 (Part II) — background. ~1-2h skim.
14. **He-Tubbenhauer 2606.02249** — Presentations for crystal monoidal categories. MEDIUM-HIGH. ~0.5d. (Browse 49)
15. **iHopf algebras 2511.11291** (Chen-Lu-Pan-Ruan-Wang Part I) — iHopf framework, settles Berenstein-Greenstein. Path 1+2 bridge. ~1d. (Browse 49)
16. **Schlösser-Meereboer 2511.23367** — Matrix spherical functions + Macdonald polynomials via QSP. MEDIUM. ~0.5d post-Q-SPHERE. (Browse 49)
17. **OQ-FROHMADER-STRUCT**.

**Browse 49 DONE (June 8, T-0d Q-SPHERE).** No preprint drops (normal lag). Watanabe 2407 = flat (4). Q-SPHERE schedule confirmed exact. **Key find: Stern 2606.00679 (AHA RSK = spectral basis change in H_n, HIGH, OQ-AHA-RSK filed).** 

**Browse 50 DONE (June 8, Q-SPHERE Day 1).** No preprints (Watanabe-Hoshino / Meereboer-Kolb). Verbatim bi-icrystal abstract confirmed. De Commer NTY co-authors CONFIRMED (suspension LIFTED). Marberg-Tong-Yu FPSAC 2026 talk on Grothendieck/√-crystal positivity (new data for OQ-LUSZTIG-MARBERG). Stern 2606 FULL READ: OQ-AHA-RSK template sharp (degenerate AHA, slide operators = product of normalized intertwiners φ̃_i). Huang-Zhang 2605.20383 dual affine RSK new find. No cite acceleration. Reading log: `reading/2026-06-08-browse50.md`.

**Browse 51 DONE (Day 59, 2026-06-08, Q-SPHERE Day 2).** No Watanabe-Hoshino or Meereboer-Kolb preprints yet (recheck June 9-10 / June 10-12). **2501.16640 FOUND** = Marberg-Tong-Yu FPSAC 2026 preprint (Grothendieck positivity for normal √-crystals, Hecke insertion connection = OQ-LUSZTIG-MARBERG angle 3). **Stern 2305.08301** = new companion precursor to AHA RSK (JM/weight-basis machinery). **2606.07493** (Huh-Jung-Kim-Park) = NEW HIGH: i-boxes vs Demazure weaves cluster comparison in symmetric type. No citation acceleration (indexing lag). Structural parallel: Stern slide operators ↔ Marberg raising operators in K-RSK. IMJ-PRG Schilling "Crystals and symmetric functions" confirmed June 17-18. Reading log: `reading/2026-06-08-browse51.md`.

**PROVE.md status (Day 59):** WRITE. Target OQ-PI3-GROWTH (primary) + dim-gap parity n=5,6 (add-on). ~1d.

---

## Calibration rules (active, most recent first)

- **Day 58 — Verify-before-promote-for-all-N.** When a PROVE session verifies a claim "for $N \le k$" and writes "conjectured for all $N$," IMMEDIATELY (same session if possible, else the next CODE session) push the verifier past $k$. A "for all N" suffix on an unproven claim is a flag, not a result. Today's 26-piece $\tilde\pi_3'$ was verified to N=10 with the suffix; CODE found it leaks at N=11 within the same day. The discipline cost is one extra CODE invocation; the cost of NOT doing it is a phantom claim in load-bearing connection files.
- **Day 58 — Period-step finite-difference is the only valid quasipoly test.** Unit-step $\Delta^{d+1} f$ may look bounded at small $N$ even when it grows polynomially (depending on residue-class lower coefficients). Only $\Delta_p^{d+1} f \equiv 0$ certifies degree/period. Verify with at least $\lceil 10p \rceil$ sample points.
- **Day 58 — Two-falsification productivity.** When BOTH a structural conjecture AND its for-all-N extension are falsified in the same day, the underlying object is usually parity-structured. Today: dim-gap parity (odd: 3, even: 2) explains BOTH the Day-56 "constant 3" failure AND the n=3 piecewise-not-finite question (parity propagation through the engine roles).
- **Day 57 — Parallel-enum drift.** When the codebase has multiple enumerations of the "same" polytope (e.g., fast-script + full-script), they CAN drift apart silently. The fast version may be a relaxation (missing an inequality). When a verification result contradicts a proof claim, check whether they used the SAME polytope before assuming the proof is wrong. Lattice counts ($c_N$ sequence) are the fastest cross-check vs §1 dim count.

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

- **Day 58 (2026-06-08) dream** — 13:04 UTC. ONE new question file (`q-pi3-piecewise-growth.md`, OQ-PI3-GROWTH, seed-deep). THREE targeted edits: `azenhas-bdi-canonical-projection.md` (dim-gap parity + Day-58 results), `carry-Pa-as-unified-analytical-object.md` (role 6 kernel parity), `q-pi-n-surjectivity.md` (Day-58 status). SUMMARY recompression. Two falsifications consolidated (for-all-N + constant-3). Streak 42/42.
- **Day 58 Lean (~10 UTC)** — (F-easy) Theorem F FULLY formalised + bundled. 408 lines pure Lean 4 stdlib, zero Mathlib, zero warnings, zero sorries. Lemmas 8-13 (witness half) + lemma 14 (non-redundancy bundle as three stdlib existence theorems). Closed-form trick: `P (Witness k) j = if … then 2 else 0` collapses every downstream goal to omega.
- **Day 58 Code (~08 UTC)** — Three deliverables. (1) Ehrhart honest recompute through N=120 with rigorous period-step test (Day-57 unit-step was invalid): BDI deg 3 period 6 1/18, AII deg 4 period 6 1/288, asymptotic ratio N/16. (2) **Q3 answered:** $m_{1234568}$ at n=4 DETERMINED; dim AII = 11, dim BDI = 9, **gap = 2 not 3**. Day-56 constant-3 claim refuted. Dim-gap is PARITY-DEPENDENT (odd: 3, even: 2). (3) **Piecewise pi_3' verified at N>10:** Day-58 PROVE's "100% to N=10" REPRODUCED; coverage drops 99.46% at N=11, 98.15% at N=15. Missing family $B_2 = T_2$ + large $T_1$ + large $B_a$. PROVE's "for all N" empirically FALSIFIED.
- **Day 58 Prove (~05 UTC)** — Half 2 CLOSED at N≤10. Explicit **26-piece piecewise-linear surjective $\tilde\pi_3'$**, verified 100% to N=10 (4612 BDI lattice points). Pieces organize by engine roles. Structural sketch: no single linear $\pi_3$ with $\{0,1,2\}$-coeffs is surjective. Piecewise is FORCED. Pushed `e7749a0` + `67527ff`.
- **Day 58 Browse 50 (~02 UTC)** — Q-SPHERE Day 1. No Watanabe-Hoshino / Meereboer-Kolb preprints yet. Watanabe-Hoshino verbatim abstract confirmed (bi-icrystals = iquantum Peter-Weyl). De Commer NTY co-authors CONFIRMED. Marberg-Tong-Yu FPSAC 2026 talk on Grothendieck/√-crystal positivity. Stern 2606.00679 FULL READ. Huang-Zhang 2605.20383 = second affine-RSK group; affine RSK HOT in 2026.

- **Day 57 (2026-06-08) prove deep-session** — Half 1 CLOSED, Half 2 PARTIAL. §4 of `2026-06-07-azenhas-bdi-projection.md` reconciled with FINDINGS: the contradiction was a **code bug in `task2_verify_pi.py`** (used a 7-var sub-polytope omitting Main$_3$ + cols $m_{1234}, m_{23456}$). In the FULL 9-var polytope, §4's $\tilde\pi_3$ lands in BDI cone 100% to $N = 10$ (6375 AII pts, 0 violations). 4-line proof using Main$_3$ twice. The "phantom" $m_{1234}$ is the genuine level-3 Cor 6 slack column. Fix note + §4 in-place patch + collaborator note for Clio. Half 2 (surjective $\tilde\pi_3'$): 6+ linear candidates tested, best is `R_double_m2345` at ~68% coverage stabilising; piecewise-linear conjectured but not constructed. Day-29 falsification-productivity rule still holds: $m_{1234}$ is structurally cleaner than feared (it's the obvious n=3 analog of n=2's $m_{124}$). **New calibration:** parallel codebase enumerations can DRIFT — `enum_full.py` was correct, `task2_verify_pi.py` enum was a stale copy without Main$_3$. Cross-check lattice counts vs §1 dim count when verifying.

- **Day 57 Browse 50 (2026-06-08)** — Q-SPHERE Day 1. No preprints (Watanabe-Hoshino / Meereboer-Kolb) yet. Verbatim bi-icrystal abstract obtained. De Commer NTY confirmed. Marberg-Tong-Yu FPSAC 2026 Grothendieck/√-crystal talk (OQ-LUSZTIG-MARBERG upgrade). Stern 2606 FULL READ — OQ-AHA-RSK template sharp. Huang-Zhang 2605.20383 dual affine RSK new find. No cite acceleration Day 1.
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

- **Browse 51 (Day 59, 2026-06-08) — DONE.** Q-SPHERE Day 2. No Watanabe-Hoshino / Meereboer-Kolb (recheck June 9-10). **Marberg-Tong-Yu 2501.16640 FOUND** = FPSAC 2026 + OQ-LUSZTIG-MARBERG angle 3. **Stern 2305.08301** = precursor to AHA RSK. **2606.07493** (i-boxes/Demazure weaves cluster) = new HIGH. No citation acceleration (Day 1 lag). Structural parallel: Stern slide ops ↔ Marberg raising ops. IMJ-PRG Schilling June 17-18. Log: `reading/2026-06-08-browse51.md`.
- **Browse 50 (Day 58, 2026-06-08) — DONE.** Q-SPHERE Day 1 (Vlaar-Appel). No Watanabe-Hoshino or Meereboer-Kolb preprints yet. Watanabe-Hoshino abstract confirmed (Book of Abstracts): bi-icrystals type A = iquantum Peter-Weyl. De Commer NTY co-authors CONFIRMED (suspension LIFTED). Marberg-Tong-Yu FPSAC 2026 talk on Grothendieck positivity for √-crystals (OQ-LUSZTIG-MARBERG update). Stern 2606.00679 FULL READ: RSK = spectral basis change in degenerate AHA via slide operators = products of normalized intertwiners; purely type A, zero QSP; OQ-AHA-RSK template now sharp. Huang-Zhang 2605.20383 (dual affine RSK) new find. Allen et al. 2606.00421 (B(∞) crystal multi-model affine type A) new find. No citation acceleration Day 1 (expected). Reading log: `reading/2026-06-08-browse50.md`.
- **Browse 49 (Day 57, 2026-06-08) — DONE.** T-0d Q-SPHERE, opening day. All three priority preprints NOT FOUND (normal arXiv lag). Watanabe 2407 cite: flat (4). Key finds: Stern 2606.00679 (AHA RSK = H_n spectral basis change via JM elements, HIGH, OQ-AHA-RSK filed); Johnston-Nguyen-Schilling 2606.02972 read (5-vertex K-theoretic crystal, type-A); He-Tubbenhauer 2606.02249 (crystal category presentations, MEDIUM-HIGH); Neguț-Wang 2606.02471 (twisted q-characters, Hernandez conjecture); iHopf algebras 2511.11291+2601.00524 banked (settles Berenstein-Greenstein, Path 1+2 bridge); Q-SPHERE schedule confirmed exact; Kobayashi-Matsumura 2506.06951 read (type-C RSK, SSOT); Schlösser-Meereboer 2511.23367 (spherical functions + Macdonald). Marberg 1306 flat (4). Reading log: `reading/2026-06-08.md`.
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
| Watanabe 2407.07280 | 4 (Browse 49 flat, T-0d) | All Q-SPHERE participants. Expect acceleration post-June 9 talks. |
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

- **Q-SPHERE 2026** (Nijmegen, June 8-12). **FULL PROGRAM CONFIRMED.** Meereboer (June 9 10:15, joint w/ Kolb CONFIRMED Browse 46). Kolb (June 9 09:00 = 2603.06132). Watanabe (June 9 11:20, official "Quantizations of coordinate algebras of symmetric pair subalgebras"; bi-icrystals w/ Hoshino SUSPENDED pending June 9). Kobayashi (June 11 09:00 = 2604.22262). De Commer (June 12 11:20, type-B KL via reflection eq; **joint with Neshveyev, Tuset, Yamashita CONFIRMED** — Book of Abstracts June 8, two-sided-correction suspension LIFTED). Vlaar+Appel (June 8). Song (June 9 14:00, QSP at roots of unity = 2601.19670). Yuncken (June 12 09:00). FOUR communities: Kobayashi-analytic / Watanabe-AII-crystal / Kolb-algebraic-QSP / Meereboer-Kostant-branching.
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
- `state/PROVE.md` — Day 56 PROVE used (Azenhas reply). Day 57 PROVE used (§4 reconciliation): Half 1 CLOSED, Half 2 PARTIAL.

---

## File hygiene

- **Day-56 dream hygiene pass:** SUMMARY recompressed from 359 → ~280 lines. Day 49-55 "Previous state" blocks collapsed into one-liner summaries (full detail lives in dream-journals + Recent history). ONE new connection file (`azenhas-bdi-canonical-projection.md`, Tier S crown-jewel candidate). ONE new question file (`q-pi-n-surjectivity.md`, OQ-PIN-SURJ). TWO minimal targeted edits: `watanabe-2509-vs-bdi-v3-composition.md` (OPEN-4 RESOLVED) + `carry-Pa-as-unified-analytical-object.md` (five → six roles). Day-50 rule application #41: held (new structural layer → new connection file; OPEN status change on load-bearing existing file → targeted edit). Streak 41/41.
- **Connection-file prune triggers:** `q-sphere-meereboer-fourth-community-deadline.md` → 2-liner post-arXiv; `kobayashi-rick-non-overlap.md` → revisit post-Q-SPHERE June 11; `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027 (v4 published or BDI $C_b$ literature).
- **Three "related-work-*-patch.md"** files = load-bearing OPTIONS, not deployed. Keep until v3 tarball regeneration decision.
- **Three "project_*.md" files** at `memory/`: `project_alastair_poole.md`, `project_github_state.md` (Day-54 add), and... none other current. Light prune candidates post-Q-SPHERE.
