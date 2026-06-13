# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke.
Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active (Day 55+). CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel (Day 55-56: `grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred since Day-24.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted Day 32; thread paused.

---

## Current state — Browse 60 (2026-06-14)

**Headline (Browse 60):** Three-way wall-count comparison now possible:
AII $\sim 2(n-1)$ (Azenhas), $(O(n+1),O(n))$ dynamically varying (Kobayashi
2604.22262), BDI **3 constant** (Rick). v4 §3 gains a third data point for
free. NEW leads: Kalmbach 2012.02883 (PhD thesis, D_n vs C_n wall counts —
potential theoretical explanation); Belkale-Kumar SO$(2n)$ eigencone failure
(candidate geometric mechanism). Kobayashi 2509.17007 RESOLVED = U(p,q) paper,
NOT BDI. KTW-FACETS-BDI gap definitively confirmed (282 KTW cites, zero QSP
overlap). Q-SPHERE preprints still absent; Meereboer-Kolb confirmed "expected
summer 2026." Watanabe Q-SPHERE talk was SOLO (no Hoshino), topic = quantizations
of symmetric pair subalgebras (not bi-icrystals). Log: `reading/2026-06-14.md`.

**Headline (Day 68):** # AXIS = 3 uniform (revised from $3 - [n\text{ even}]$);
Fence wrapper shipped in Lean; Azenhas confirms AII has $\sim 2(n-1)$
walls vs BDI's 3 — publishable structural contrast for v4 §3.

**PROVE — # AXIS conjecture revised to uniform 3.**
Day-62 conjecture refuted Day 67 at $n=4$ (R-double family missed in
the 20-piece registry). Day 68 re-derived at $n=3$ from first
principles: full 26-piece cover (with R-double) gives # AXIS = 3.
Uniform theorem: $\#\mathrm{AXIS}(n) = 3$ for $n \ge 3$, AXIS triple
$\{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}$.
Head-bulk decomposition: 1 R-double / $\mathrm{adj}(\mathfrak{sl}_2)$
head + 2 Bucket-2 free-extrusion bulk. The dim-gap parity $f(n) = 3
- [n\text{ even}]$ SURVIVES at AII polytope dim level (Cor 8 linking
eq) but is now **decoupled** from # AXIS. v4 §3 narrative drops the
"# AXIS = dim-gap" identity. Files:
`proofs/2026-06-13-axis-conjecture-revision.md`,
`code/2026-06-13-axis-n3-verify/`,
`for-collaborator/2026-06-13-axis-conjecture-revision.md`. Commit `8868201`.

**PROVE Day 69 — # AXIS(n) ≥ 3 uniform LOWER BOUND PROVED structurally.**
Three explicit 3-piece families (R-double / free-top prefix / free-bottom
long), uniform in $n \ge 3$, force $\{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}$
to be AXIS at every $n \ge 3$. R-double cap $\alpha \le 2$ is BDI-feasibility-sharp
(= $\dim \mathrm{adj}(\mathfrak{sl}_2) - 1$) — the rep-theoretic head. The 2 bulk
AXIS coords use multiplicity-0/1/2 routings of $p_n$ in balanced $(B_{n-1}, T_{n-1})$
and $l_1$ in $B_1$ respectively. Upper bound (# AXIS $\le 3$) empirical at
$n \le 5$; abstract proof (Lemma D) open, articulated as cover-minimality /
image-redundancy argument in writeup §4. **v4 §3 upgrade: structural "for all n"
lower bound now locked in.** Files:
`proofs/2026-06-14-axis-uniform3-proof.md`,
`code/2026-06-14-axis-uniform3-verify/`,
`for-collaborator/2026-06-14-axis-uniform3-proof.md`.

**CODE — n=5 confirmation + single-column n=9.**
27-piece BDI-feasible registry at $n=5$: # AXIS = 3, same AXIS triple.
**Uniform-3 confirmed at $n \in \{3, 4, 5\}$.** Single-column lemma
extended; OQ-PI3-GROWTH branch (a) closed at $n \in \{2, \ldots, 9\}$.
Files: `code/2026-06-13-n5-axis-count/`, `code/2026-06-13-single-column-n9/`.
Commit `5fb7d17`.

**LEAN — Fence wrapper shipped.**
F-easy bundle re-packaged as uniform $\mathrm{Fin}(n-1) \to
\mathrm{BdiPolytopeFace}\ n$ indexed family with `FenceKind` sum
type (L over $\mathrm{Fin}(n-1)$, U over $\mathrm{Fin}(n-2)$ skipping
redundant $U_1$, E singleton). 6 distinctness lemmas via kind
injection. All 8 new declarations: axiom set `{propext, Quot.sound}`.
NO Classical.choice. `BdiPolytope.lean` 1106 → 1276 lines (+170).
Commit `1c42a05`. Note: `for-collaborator/2026-06-13-fence-wrapper.md`.

**Browse 59 — AII vs BDI wall count contrast (CROWN JEWEL).**
Full LaTeX read of Azenhas arXiv:2603.16698 (7987 lines). Linear
inequalities in multiplicity space (same coords Rick uses). For AII
(GL→Sp): **~$2(n-1)$ walls growing linearly in n**. For BDI (Rick):
**3 walls for all n**. **Structural simplicity is the finding.** Filed
`connections/aii-bdi-wall-count-asymmetry.md` (Tier S candidate);
publishable as v4 §3 paragraph + Azenhas citation. Kobayashi NOT
cited; BDI NOT mentioned — clean gap. Side finds: Muniz arXiv:2505.21738
(Sundaram-model proof of Naito-Sagaki, check BDI portability); new
OQ-KTW-FACETS-BDI (do KTW facets give Rick's 3 walls?); Meereboer
arXiv:2510.17655 = iota crystal 1-dim foundational; Q-SPHERE preprints
STILL ABSENT at T+1d (watch June 15-30). Watanabe affiliation: Rikkyo
Univ, not RIKEN iTHEMS. Log: `reading/2026-06-13.md`.

---

## Research territory (per SEED.md)

Four paths: `topics/path1-combinatorial-hopf.md`, `path2-quantum-groups.md`,
`path3-hecke.md`, `path4-coproduct-crystal.md`.

**Active seed connections:**
- **Path 2 + Path 4 (main thread):** $\pi_n$ canonical projection /
  AII-fibered groupoid framework. Theorem at $n=2$; branch (a)
  existential close at $n \in \{2, \ldots, 9\}$; **Day-60 NOT polyhedral
  GIT**; **Day-61 NOT fan, NOT PFL**; **Day-62 (c\*) stack PINNED DOWN**
  as AII-fibered groupoid; **Day-68 # AXIS = 3 uniform** with R-double
  head + Bucket-2 bulk decomposition.
- **Path 2 + Path 4 — wall count asymmetry (Day-68; UPGRADED Browse 60):**
  THREE-WAY comparison: AII $\sim 2(n-1)$ (Azenhas), $(O(n+1),O(n))$
  dynamic (Kobayashi 2604.22262), BDI **3 constant** (Rick). Publishable
  v4 §3 table + 2 citations (Azenhas + Kobayashi). `connections/aii-bdi-wall-count-asymmetry.md`.
- **Path 2 + Path 4 — cross-programme dim-gap:** $f(n) = g(n) =
  3 - [n\text{ even}]$ conjecture (Day-60). Day-68 dropped the
  "# AXIS = $f(n)$" clause; $f = g$ alone survives. Testable at
  $n \in \{3, 5, 6, 7\}$ on Clio's side.
- **Path 2 + Path 4 — carry $P_a$ six-roles:** Theorems E, F, G +
  projection. **Lean Theorem F-easy COMPLETE Day-66** (`b0a79b2`,
  `[propext, Quot.sound]`); **Theorem G COMPLETE Day-64** (`K_simplicial`,
  form (b), `[propext, Classical.choice, Quot.sound]`).
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL conjectures
  (1306.2980) unguarded. Marberg-Tong-Yu 2501.16640 = FPSAC 2026 short
  talk, OQ-LUSZTIG-MARBERG angle 3 entry. Long-horizon for v4+.
- **Path 1 (combinatorial Hopf):** NSym^B from $H^B_*(0)$ still open
  (OQ-HUANG-B). Seed Q4 (q=0 combinatorial Hopf) externally unconstrained.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`aii-bdi-wall-count-asymmetry.md`** (Day-68; Browse-60 upgrade) —
  THREE-WAY: AII $\sim 2(n-1)$ (Azenhas), $(O(n+1),O(n))$ dynamic
  (Kobayashi 2604.22262), BDI **3 constant** (Rick). Tier S; v4 §3
  table + Azenhas + Kobayashi citations. Potential explanation: Kalmbach
  D_n vs C_n (OQ-KALMBACH-BDI); Belkale-Kumar SO$(2n)$ failure
  (OQ-BELKALE-KUMAR-BDI).
- **`azenhas-bdi-canonical-projection.md`** — Canonical forgetful
  surjection $\pi_n$. THEOREM at $n=2$; OQ-PIN-SURJ EXISTENTIAL CLOSED
  at $n \in \{2, \ldots, 9\}$. Day-60: NOT polyhedral GIT. Day-61:
  NOT fan, NOT PFL. Day-62: (c*) stack PINNED DOWN as AII-fibered
  groupoid. Day-68: # AXIS = 3 uniform.
- **`pi3-stratified-multimap.md`** — (c*) stack candidate concretely.
  AII-fibered groupoid $G$; MAX-vector $(3,8,11,10,19,14,23,26)$;
  variable taxonomy (2 RIGID + 4 BINARY + 3 AXIS at n=3); Day-64
  OQ-PI3-MULTI-FINAL: Bucket-2 NOT rep-theoretic (marginal-palindromy);
  Day-66 partial rep-theoretic rescue (B0+B1 = $\mathfrak{gl}_2$ head);
  Day-68 # AXIS structure uniform.
- **`cross-programme-dim-gap-codim.md`** — $f(n) = g(n) = 3 - [n\text{ even}]$
  conjecture. Day-68 addendum: # AXIS clause dropped; $f = g$ survives.
- **`discovery-layer-is-the-moat.md`** — Day-39. AI verifies; humans+frameworks
  discover. Five evidence layers.
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles. v3
  structural climax.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Day-66 F-easy
  RESOLVED in Lean (commit `b0a79b2`, axiom set `[propext, Quot.sound]`).
  Day-68 Fence wrapper API (commit `1c42a05`).
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. **Day-64
  LEAN COMPLETE.** 866 → 1276 lines (with Day-66 F-easy + Day-68 Fence).
- **`kobayashi-rick-non-overlap.md`** — Level sets ($\sim 4n^2$,
  Kobayashi) vs support ($n$ partial-sum facets, Rick). Complementary.
- **`open2-watanabe-2407-existence-meereboer-1dim-collapse.md`** —
  v3 OPEN-2 Layer 1 FREE via Watanabe 2407 §5; Layer 2 → Theorem E.
- **`asymmetry-is-the-result-seven-instances.md`** — Crystal in
  EXPLOITATION mode.
- **`compression-is-content.md`** — Three asymmetric mechanisms.

### Tier A — Active

- **`bucket-0-as-sl2-rump.md`** (Day-66) — B0+B1 = $\mathrm{adj}(\mathfrak{sl}_2)
  \oplus \mathbb{C} = \mathfrak{gl}_2$ as $A_1$-module, uniform in $n$.
  Partial rep-theoretic rescue of OQ-PI3-MULTI-FINAL. Cap $\alpha \le 2$
  BDI-feasibility-forced.
- **`marginal-palindromy-refutation.md` + `-v2.md`** (Day-64, Day-66) —
  Calibration-grade refutation filter; $w_0 = -1$ types + twisted
  extension for $A_n, D_{2k+1}, E_6$. Closes catalogue.
- **`lu-pan-dual-canonical-bdi-algebraic-roof.md`** — Quartet of
  algebraic papers. Path 2 ↔ Path 4 bridge.
- **`zhang-lusztig-bridge-for-marberg.md`** — Post-v3 P_PARK #1 bridge.
  Three attack angles; angles 1+2 ready ~5.5d.
- **`q-sphere-meereboer-fourth-community-deadline.md`** — Q-SPHERE
  June 8-12 archive. Watch preprints June 15-30.
- **`Rpi-carry-one-sided-monotone.md`**, **`watanabe-2509-vs-bdi-v3-composition.md`**,
  **`Tobs-delta-lives-on-opfibration-not-lens.md`**, **`slack-vs-Rpi-doesnt-port-as-result.md`**,
  **`external-shadow-shape-eight-refutations.md`**, **`short-long-tensor-product-rule.md`**,
  **`chain-factor-framework-natural-scope.md`**, **`attribution-verification-mandatory.md`**,
  **`ghani-grading-payoff-vs-observation-mirror.md`**.

### Tier B — Historical anchors (don't prune)
Catalog/v2 + framework bridges + foundational/refuted. See `connections/`.

---

## Open questions

**Active (worth tracking):**
- **OQ-PIN-SURJ** — single-column auto-construction 100% at $n \in
  \{2, \ldots, 9\}$ via Day-68 CODE. Branch (a) closed range extended.
- **OQ-PI3-GROWTH** — polyhedral GIT REFUTED (Day-60); fan + PFL
  REFUTED (Day-61); (c*) stack PINNED (Day-62). Branch (a) existential
  closed at $n \le 9$.
- **OQ-DIMGAP-CODIM** — Day-68 corrected to $f(n) = g(n) = 3 - [n\text{ even}]$
  (# AXIS clause dropped). Clio's $g(d)$ at $d \in \{3, 5, 6, 7\}$
  still uncomputed. HIGH priority cross-programme.
- **OQ-KOBAYASHI-FENCES-BDI** (Day-65; 2509.17007 RESOLVED Browse 60) —
  Are Rick's 3 walls the deferred AII→BDI fences from Kobayashi? 2509.17007
  IS on arXiv (Harris-Kobayashi-Speh, 100pp) but covers U(p,q)→U(p-1,q) —
  NOT BDI. Kobayashi 2604.22262 deferred GL(n)→O(n)×O(n) to "elsewhere"
  (future work). BDI gap REMAINS CLEAN. OQ survives.
- **OQ-AZENHAS-INEQUALITIES-BDI** (Day-65) — Day-68 Browse 59 RESOLVED
  POSITIVE direction: Azenhas's inequalities ARE in the same multiplicity
  coord system, but with $\sim 2(n-1)$ walls vs Rick's 3. Filed in
  `aii-bdi-wall-count-asymmetry.md`.
- **OQ-KTW-FACETS-BDI** (Browse 59; Browse-60 gap CONFIRMED) — Do KTW
  facets (math/0107011) give Rick's 3 BDI walls? Browse-60 citation scan:
  282 KTW cites, **ZERO overlap** with QSP/iota-crystal community. Gap is
  definitively novel. KTW facets = n-dependent rigid puzzles, NOT a fixed
  formula — contrast to Rick's constant 3. No existing literature bridges
  these worlds.
- **OQ-KALMBACH-BDI** (NEW Browse 60) — Kalmbach 2012.02883 PhD thesis
  computes branching cones for B_n, C_n, D_n over A_{n-1}. Do D_n cones
  have fewer walls than C_n? If yes, theoretical precedent for BDI = 3
  vs AII = $2(n-1)$. HIGH priority read. `questions/q-kalmbach-bdi.md`.
- **OQ-BELKALE-KUMAR-BDI** (NEW Browse 60) — Belkale-Kumar eigencone for
  Sp(2n) coincides with SU(2n) but fails for SO(2n). Does this structural
  failure explain BDI wall simplicity? MEDIUM priority. Quick read §1 of
  arXiv:0708.0398.
- **OQ-AZENHAS-SLACK** (Day-65, MEDIUM) — Slack-data quantification.
- **OQ-BRUNDAN-WANG-WEBSTER-BDI** (Day-65, MEDIUM) — Does 2505.22929
  produce BDI icrystal bases?
- **OQ-KUMAR-TORRES-HIVES** (Day-65, MEDIUM) — Is BDI cone a hive
  polytope?
- **OQ-HOROSPHERICAL-STACK-PI3** (Day-63, DORMANT) — AII/BDI not
  horospherical; bridge survives via Kolb-Yakimov but geometric
  connection absent.
- **OQ-LUSZTIG-MARBERG** (P_PARK #1) — Three attack angles; ~5.5d.
- **OQ-ZHANG-MARBERG**, **OQ-HUANG-B** (P_PARK #3),
  **OQ-LU-PAN-EXPLICIT** (P_PARK #4), **OQ-G-INTRINSIC** (P_PARK #2),
  **OQ-AHA-RSK**, **OQ-TYPEB-AHA-RSK**, **OQ-MILLS-TYPEB**, **OQ-GhaniDual**,
  **OQ-G2 (parked)**, **q-type-B-cactus** (Littelmann CLOSED, KN open),
  **q-KL-from-crystal** (spin CLOSED, non-spin 2-step required),
  **q-zero-CHA** (type A K_0/derived answered, type B NSym^B open).

**Closed:** OQ-K (Day 29), OQ-BDIqLR (Day 26-28), OQ-KOB-MATCH (Day 41),
OQ-CHEN-LU (Day 42), OQ-BWB / OQ-PJ (Day 18), OQ-MUNIZ-CARRY (Browse 20),
OQ-FROHMADER (Day 29), OQ-KOBAYASHI-SL2 (Day 29), OQ-LAUVE-RQSYM (Day 50),
**OQ-PI3-MULTI-FINAL Gap B** (Day 64), **Gap C** (Day 66 POSITIVE),
**OQ-NAITOSAGAKI-BDI** (Day 66 NEGATIVE), **OQ-INVERTI-STRATUM** (Day 65),
**OQ-PI3-INV5** (Day 65 coincidental), **OQ-AZENHAS-BDI** (Day 55 →
Day 56 reframed), **OQ-HMP-ACCELERATION** (Browse 53).

---

## Next session priorities

**P-1 — Wake-routine PROVE-check + git-state-verification check**
(Day-44 + Day-60 phantom-completion rules STABLE).

**P0 — v4 §3 rewrite (UPDATED):** Drop "# AXIS = dim-gap" narrative; add
THREE-WAY wall count comparison table (AII Azenhas, O(n+1)/O(n) Kobayashi,
BDI Rick) + 2 citations; keep dim-gap parity at AII polytope dim level.
Browse 60 adds a third comparison point at zero cost.

**P0 — Robin endorsement + Lean form (a)/(c) call** still pending.

**P0 — Clio outbound** on Day-68 # AXIS revision + cross-programme
conjecture update.

**P1 — OQ-KALMBACH-BDI:** Read Kalmbach 2012.02883 intro (~45 min).
Does D_n branching cone over A_{n-1} have fewer walls than C_n? This is
the highest-leverage new lead for a theoretical explanation.

**P1 — Next PROVE.md options:**
- (A) OQ-KALMBACH-BDI read + comparison to BDI framework.
- (B) Read Meereboer arXiv:2510.17655 — iota crystal 1-dim foundational.
- (C) Belkale-Kumar 0708.0398 §1 — SO(2n) eigencone failure mechanism.
- (D) Read Brundan-Wang-Webster arXiv:2505.22929 intro for BDI icrystal status.

**P1 — Next LEAN.md options:**
- (E) Theorem G form (c) refactor (explicit 2-torsion).
- (F) Move past polytope: Corollary 6 (Azenhas projection) or Bucket-0 = $\mathfrak{sl}_2$ result.

**P1 — Next CODE.md options:**
- (G) Wall verification at n=4, 5 against Azenhas's prediction ($\sim 2(n-1)$ for AII).
- (H) Single-column lemma at n=10+.

**HARD DEADLINE: Browse 61 ~June 15-17.** Q-SPHERE preprint recheck;
Schilling IMJ-PRG slides post-June-18; FPSAC 2026 short talk list expected late June.

**P_PARK (post-v3 arXiv, preference order):**
1. OQ-LUSZTIG-MARBERG (~5.5d, angles 1+2).
2. OQ-G-INTRINSIC.
3. OQ-HUANG-B (Kim-Searles entry).
4. OQ-LU-PAN-EXPLICIT (~½d).
5. OQ-PIN-SURJ refinements at higher $n$.
6. Stern 2606.00679 + Lu 2311.16373 + Lu-Pan 2605.13578 (iquantum survey).

---

## Calibration rules (active, most recent first)

- **Day-60 Phantom-completion check (STABLE).** Verify "formalised / shipped"
  against `git log --oneline <file>` before promotion. Day-58 (F-easy
  408 lines NOT in git) + Day-60 (Theorem G "ray ∈ K_n" lemmas) = 2
  instances. Rule: every LEAN session ends with `git push` or work
  counts as phantom. **Day-66 Day-58 F-easy phantom CLEARED** by re-derivation.
- **Day-60 Productive-falsification of strong hypotheses.** Refutation
  is cheap and structurally productive; test before assuming.
- **Day-58 Verify-before-promote-for-all-N.** "For all $N$" suffix
  on a partial verification is a flag, not a result.
- **Day-58 Period-step finite-difference is the only valid quasipoly test.**
- **Day-58 Two-falsification productivity.** Both-falsification-day usually
  means the underlying object is parity-structured.
- **Browse-46 Two-sided correction rule.** Both fabrication and
  mis-correction occur; independent direct-fetch required.
- **Day-50 Promotion thresholds.** Refines existing → journal; opens
  new layer → connection file; operational refinement → minimal edit.
  STABLE at 50+ consecutive applications.
- **Day-46 KILLED Day-55** by Robin standing instruction → daily-email rule.
- **Day-45 Evidence durability:** empirical < community-internal <
  structural < mechanical < live-attack.
- **Day-45 Citation-graph hit ≠ same-subprogram.** Default prior 30%;
  direct-fetch abstract before priority slot.
- **Day-44 Orthogonal-at-technique can hide complementary-at-content.**
- **Day-44 PROVE.md existence check** belongs in wake-routine.
- **Day-43 Adjacent-sounding ≠ adjacent.**
- **Day-43 Pre-positioning is mature watching mode.**
- **Day-39 Discovery-layer is the moat.**
- **Day-39 Robin redirection ≠ refusal.**
- **Day-35 Phantom-attribution failure** (3-instance rule).
- **Day-33 PROVE.md is binary signal**, not communication channel.
- **Day-28-29 Falsification productivity.** Fired again Day-56, Day-67-68.
- **Day-19 Eight-refutations structural conclusion.** Catalog-level external
  bridges STOP; framework-level PERMISSIBLE.
- **Harness-adaptive FORMAL CALIBRATION (6/6, Browse 47).**

**Method-level rules (stable):**
- Right statement proves itself (REDUCED-multiset). Whiskey rule: framing
  is the work. Form of obstructions, not existence. Browse immediately after
  a proof closes. Rank 2 degenerate; anchor at rank 3. Type-uniform proofs
  port for free; identifications don't. 30-second sympy on q-identities
  BEFORE carrying forward. Verify the defining axiom BEFORE testing
  consequences. Naming-metaphor trap: use formal name in writeups.

---

## Recent history (one-liners; journals have detail)

- **Browse 60 (2026-06-14).** Three-way wall comparison (AII/O(n+1)O(n)/BDI).
  OQ-KALMBACH-BDI + OQ-BELKALE-KUMAR-BDI filed. 2509.17007 resolved (wrong paper).
  KTW gap confirmed. Q-SPHERE preprints still absent. Log: `reading/2026-06-14.md`.
- **Day 68 (2026-06-13) — DONE.** # AXIS uniform-3 revision + n=5 confirmation +
  single-column n=9 + Fence wrapper Lean + Azenhas wall-count contrast.
  Streak 54/54. See `dream-journal/2026-06-13.md`.
- **Day 67 (2026-06-12 evening) — # AXIS conjecture refuted at n=4** (R-double family
  missed in 20-piece registry).
- **Day 65-66 (2026-06-12) — DONE.** Day 65: NSW deep read +
  OQ-NAITOSAGAKI-BDI narrowed; Day 66: Bucket-0 = $\mathfrak{sl}_2$ rescue +
  F-easy phantom CLEARED + so_6 fully closed-negative + palindromy v2.
- **Day 63-64 (2026-06-11) — DONE.** Bucket-2 ↔ adj($B_3/C_3$) refuted via marginal-palindromy;
  Theorem G COMPLETE 5/5; n=4 # AXIS = 2 (DAY-67 LATER REFUTED).
- **Day 61-62 (2026-06-10) — DONE.** Fan + PFL REFUTED; stack PINNED DOWN as AII-fibered groupoid.
- **Day 60 (2026-06-09) — DONE.** Toric-quotient STRONG FORM REFUTED; $f(n) = 3 - [n\text{ even}]$ closed form.
- **Day 59 (2026-06-08) — DONE.** Branch (a) closed via single-column auto-construction; dim-gap parity $n=5,6$.
- **Day 58 (2026-06-08) — DONE.** 26-piece piecewise $\tilde\pi_3'$ + dim-gap parity correction + Ehrhart honest recompute.
- **Day 56-57 (2026-06-07-08) — π_2 surjection theorem milestone** + Lean toolchain + Clio peer-review channel operational.
- **Day 55 (2026-06-06) — Robin reply broke channel silence; daily-email rule active; Browse 47 bi-icrystal.**
- **Days 49-54 (2026-05-31 to 06-05) — Q-SPHERE pre-conference; Azenhas surfaced; Watanabe upstream hub confirmed.**
- **Days 41-48 (2026-05-23 to 30) — three-thread originality verdicts; Lu-Pan quartet; discovery-layer-moat thesis.**
- **Days 32-40 — v3 tarball SHIPPED Day 32; PROVE.md misfire lesson Day 33.**
- **Days 28-31 — Theorems F + G; v3 §1-3 SHIPPED.**
- **Days 22-27 — BDIqLR Theorems A+B; Watanabe + Meereboer reads; Theorem E; Kobayashi falsification.**
- **Days 1-21 — Foundational chain-factor framework.**

---

## Citation counts (most recent check Browse 60 — 2026-06-14)

| Paper | SS Count | Notes |
|---|---|---|
| Watanabe 2110.07177 | 12 (CLOSED Browse 46) | All known. |
| Watanabe 2407.07280 | 5 (Browse 60, unchanged) | No new citers. |
| Watanabe 2509.00853 | 3 (Browse 59) | S2 dedup not actual drop. |
| Lusztig 2510.21499 | 0 | 8+ months. |
| Marberg 1306.2980 | 4 all-time | DORMANT — Marberg shifted to K-theoretic. |
| Zhang 2412.07810 | 0 | OQ-ZHANG-MARBERG open. |
| Kobayashi 2604.22262 | 1 (Browse 60, unchanged) | Self-cite only. 3-way wall comparison. |
| Meereboer 2510.17655 | 0 external (Browse 60) | iota crystal 1-dim; 0 external citers 8mo. |
| Azenhas 2603.16698 | 2 (Browse 60, unchanged) | Self-sequels only. Community hasn't noticed. |
| Watanabe 2502.07270 | (J. Alg 2026, in print) | AII fully settled. |

---

## Conferences

- **Q-SPHERE 2026** (Nijmegen, June 8-12) — CONCLUDED. Preprints ABSENT
  T+2d. **Meereboer-Kolb** = "expected summer 2026" (WIP). **De Commer
  "type B KL"** = reflection equation / braided monoidal category — NOT
  Coxeter KL polynomials. **Watanabe spoke SOLO** (no Hoshino as co-speaker);
  topic = quantizations of symmetric pair subalgebras. Watch June 15-30.
  Watanabe affiliation: Rikkyo University.
- **FPSAC 2026** (Seattle, July 13-17). Marberg-Tong-Yu "Grothendieck
  positivity for square root crystals" = confirmed SHORT TALK
  (OQ-LUSZTIG-MARBERG angle 3 live). Seung Jin Lee invited (q-weight via
  KR crystals, types B/C). Short talk list expected late June.
- **IMJ-PRG** (Paris, June 17-18). Schilling mini-course "Crystals
  and symmetric functions." Slides post-June-18.
- **Mittag-Leffler** (July 27-31). Schilling co-organizer, "Solvable
  lattice models + quantum groups." **Allen Knutson attending** (K of KTW).
  Natural venue to socialize OQ-KTW-FACETS-BDI. 32 participants confirmed.

---

## GitHub / Project artefacts

- `papers/v3-bdi-unified-carry/` — v3 tarball (BYTE-IDENTICAL since Day 32). Three Day-41/42 patches. `grant-pitch-draft.md` Day 40.
- `proofs/` — recent: `2026-06-13-axis-conjecture-revision.md`, `2026-06-12-bucket0-algebraic-origin.md`, `2026-06-12-naito-suzuki-watanabe-read.md`.
- `proofs/lean/bdi-polytope/` — **Theorem G COMPLETE** (Day-64, 866 lines).
  **F-easy COMPLETE** (Day-66 commit `b0a79b2`, +240 lines, `[propext, Quot.sound]`).
  **Fence wrapper API** (Day-68 commit `1c42a05`, +170 lines). Total: 1276 lines pure stdlib.
- `grandpa-rick/rick-research` branch `prove-day-59` — Day-68 commits:
  `8868201` (PROVE), `5fb7d17` (CODE), `1c42a05` (LEAN).
- `clio-vega/rick-review` (Clio's repo) ↔ `grandpa-rick/clio-review` (Rick's repo) — bidirectional peer review.

---

## File hygiene

- **Day-68 dream hygiene pass (2026-06-13):** SUMMARY aggressively compressed
  from 912 → ~270 lines. Day 55-67 history pushed to dream journals. ONE new
  connection file (`aii-bdi-wall-count-asymmetry.md`, Tier S candidate).
  Browse 59 + Day-68 PROVE/CODE/LEAN merged into current state. q-naitosagaki-bdi
  confirmed CLOSED-NEGATIVE; q-ktw-facets-bdi current. Streak 54/54.
- **Connection-file prune triggers:** `q-sphere-meereboer-fourth-community-deadline.md`
  → revisit when preprints drop (June 15-30); `kobayashi-rick-non-overlap.md` →
  revisit post-Kobayashi 2509.17007 fetch; `lu-pan-dual-canonical-bdi-algebraic-roof.md`
  → revisit ~2027.
- **Three "related-work-*-patch.md"** files = load-bearing OPTIONS. Keep until v3 tarball regeneration decision.
- **Three "project_*.md"** files: `project_alastair_poole.md`, `project_github_state.md` (Day-54). Light prune candidates post-Q-SPHERE.
