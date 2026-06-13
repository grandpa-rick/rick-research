# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active (Day 55+). CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel operational (Day 55-56: `grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred since Day-24.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted since Day 32. Thread paused per Day-46-superseded rule.

---

## Current state — Day 68 (2026-06-13, # AXIS conjecture REVISED: uniform 3 across $n \ge 3$)

**Day 68 PROVE: # AXIS conjecture revised to uniform 3.** Day-62
$\#\mathrm{AXIS}(n) = 3 - [n\text{ even}]$ refuted Day 67 at $n=4$
(R-double family was missed). Day-68 re-derived at $n=3$ from first
principles using the same kernel-arrangement methodology: full
26-piece cover (with R-double) gives # AXIS = 3; remove R-double
and # AXIS drops to 2. Same at $n=4$. **Uniform statement:**
$\#\mathrm{AXIS}(n) = 3$ for $n \ge 3$, AXIS triple
$\{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}$.
Decomposition: 1 (R-double / $\mathrm{adj}(\mathfrak{sl}_2)$,
head) + 2 (Bucket-2 free-extrusion, bulk). The dim-gap parity
$f(n) = 3 - [n\text{ even}]$ SURVIVES at AII-polytope-dim level
(Cor 8 linking eq) but is **decoupled** from # AXIS. v4 §3 narrative
needs to drop "# AXIS = dim-gap" identity. Files:
`proofs/2026-06-13-axis-conjecture-revision.md`;
`code/2026-06-13-axis-n3-verify/`;
`for-collaborator/2026-06-13-axis-conjecture-revision.md`;
`connections/cross-programme-dim-gap-codim.md` updated with Day-68
addendum. Open: $n=5$ verification (Day-68 CODE follow-up).

## Prior state — Day 65-66 (2026-06-12, mixed-structure result locked: head $\mathfrak{gl}_2$ + bulk novel; OQ-NAITOSAGAKI-BDI fully closed; F-easy phantom CLEARED)

**Day 66 CODE: OQ-NAITOSAGAKI-BDI fully closed-negative.**
Pure-Python $\mathfrak{sl}_6 \supset \mathfrak{so}_6$ branching via
exceptional iso $D_3 \cong A_3$ + Littlewood rule. Exhaustive sweep of
all 56 partitions $\lambda \subset (5^3)$ + sub-collection search +
basis-change marginal search. **Three independent obstructions:**
(i) dim gap (no $\lambda$ has $\dim V_\lambda = 22$; jumps 21 → 56);
(ii) branching obstruction (zero sub-collections sum to 22 across all
56 $\lambda$); (iii) marginal-pattern obstruction (none of 16 abstract
dim-22 decomps + $|coord| \le 10$ functionals match Bucket-2 marginals).
The $\mathfrak{so}_6$ loophole left at Day-65 is killed cold. Bucket-2
is genuinely novel combinatorics — not a $\mathfrak{so}_n$-branching
shadow at any rank ≤ 3. Files:
`code/2026-06-12-so6-branching-test/`;
`for-collaborator/2026-06-12-so6-branching-verdict.md`;
`questions/q-naitosagaki-bdi.md` CLOSED-NEGATIVE.

**Day 66 PROVE: Gap C closed POSITIVE.** The 3 R-double pieces of Bucket-0
are the weight multiset of $\mathrm{adj}(\mathfrak{sl}_2) = V(2\omega_1)$
under the natural $W(A_1) = \mathbb{Z}/2$ action $\alpha \mapsto 2 - \alpha$.
Combined with Bucket-1 (singleton = trivial $A_1$-rep), the
4 "special" pieces of the 26-piece cover decompose as $\mathfrak{gl}_2 = \mathfrak{sl}_2 \oplus \mathbb{C}$. Cap $\alpha \le 2$ comes from
BDI-feasibility of the R-double backbone — verified empirically at n=3
($\alpha = 3$ gives 69.3% land-in-cone vs 100% for $\alpha \le 2$) AND
n=4 ($\alpha = 3$ gives 81% vs 100%). **B0($n$) = 3 invariantly**, =
$\dim \mathrm{adj}(\mathfrak{sl}_2)$ — NOT an $n$-dependent count.

- **v4 §3 NEW STORY**: the head of the cover (B0 + B1 = 4 pieces) IS
  rep-theoretic (uniform $\mathfrak{gl}_2$), the bulk (B2 = 22) is
  intrinsic combinatorics. Cleaner than "all 26 combinatorial".
- **Day-64 n=4 AXIS-classification needs revisiting**: the 20-piece
  registry MISSED the R-double family. Adding it gives `prefix[1]` 3
  distinct columns, potentially flipping it from RIGID to AXIS at n=4.
  Flagged for follow-up.
- **Phase 3 bonus**: extended marginal-palindromy filter to v2 with
  diagram-twisted version for $w_0 \ne -1$ types ($A_n, D_{2k+1}, E_6$).
  For axis-length-distinct configs (like Bucket-2's (4,9,8)), twisted
  reduces to plain — so the $D_3 = A_3$ ($\mathfrak{so}_6$) loophole is
  REFUTED at direct-marginal level; only basis-change escape remains.
- Files: `proofs/2026-06-12-bucket0-algebraic-origin.md`;
  `connections/marginal-palindromy-refutation-v2.md`;
  `for-collaborator/2026-06-12-bucket0-gap-c.md`;
  scripts: `code/2026-06-12-bucket0-origin/`.

**Day 66 LEAN: Theorem F-easy formalised — Day-58 phantom flag CLEARED.**
Non-redundancy bundle (`E_nonredundant`, `L_nonredundant`,
`U_nonredundant`) shipped in `BdiPolytope.lean` (866 → 1106 lines,
+240).  Three witnesses (`EWitness`, `LWitness k`, `UWitness k`) with
closed-form `P`-lemmas, twelve satisfies/violates lemmas, plus the
bundle.  Axiom set `[propext, Quot.sound]` only — strictly cleaner
than the Theorem G headline which uses `Classical.choice`.  Pure
stdlib, zero sorrys, zero warnings.  Commit `b0a79b2` on
`prove-day-59`, pushed to origin.  Note:
`for-collaborator/2026-06-12-bdi-polytope-lean-f-easy-resolved.md`.
This is the FIRST phantom-completion flag closed by post-fix
re-derivation — the Day-60 calibration rule has now been validated
on the worst case.

**Day 65 PROVE: Naito-Suzuki-Watanabe arXiv:2502.07270 deep read +
AII→BDI sketch.** NSW v3 (50 pp). Extracted iquantum-crystal machinery
in 5 bullets ($U^\imath$, `suc` map, iquantum LR bijection,
$\mathrm{Res}/\mathrm{pr}$ operators, local→global to $\mathfrak{sp}_4$).
**Verdict:** OQ-NAITOSAGAKI-BDI mostly closed-negative. Marginal-
palindromy obstruction inherits to $\imath$-crystal level (components
carry $\mathfrak{k}$-irrep weight characters); rules out
$\mathfrak{sp}_{2n}, \mathfrak{so}_{2n+1}, \mathfrak{so}_{2(2k)}$
targets at all $n$. **Single surviving loophole:** $\mathfrak{so}_6
\cong D_3 = A_3$ at $n = 3$ via $w_0 \ne -1$. Day-66 CODE prescription
issued; Day-66 fully closed it (above). Side benefits banked:
NSW local-global structure portable to BDI (base case $\mathfrak{so}_4 =
\mathfrak{sl}_2 \oplus \mathfrak{sl}_2$ strictly easier than NSW's
$\mathfrak{sp}_4$). Files: `proofs/2026-06-12-naito-suzuki-watanabe-read.md`;
`for-collaborator/2026-06-12-naito-sagaki-bdi-sketch.md`.

**Day 65 CODE: three quick follow-ups.**
- **OQ-INVERTI-STRATUM CLOSED-NEGATIVE.** Both MODE
  $(1,5,9,9,13,17,22,26)$ (fails $n=4$, $b_4 = -20$) and MAX
  $(3,8,11,10,19,14,23,26)$ (fails $n=2$, $b_2 = -1$) FAIL INVERTi
  nonnegativity. Neither is the graded-dim sequence of a free
  noncommutative cocommutative connected Hopf algebra. Cleanest Hopf
  candidate ruled out.
- **OQ-PI3-INV5 CLOSED-COINCIDENTAL.** 26 piece marginals
  $[1,3,11,11]$ / $[1,1,1,1,1,2,3,3,4,9]$ / $[1,1,1,2,4,4,4,4,5]$ don't
  match $I(5)$ cycle types $[1,10,15]$ or RSK shapes $[1,1,4,4,5,5,6]$.
  Bonus: n=4 has 20 pieces ≠ $I(6) = 76$. $26 = |I(5)|$ is a numerical
  coincidence at $n=3$; $I(n+2)$-growth hypothesis killed already at
  $n=4$. Move on.
- **OQ-PI3-GROWTH branch (a) extended to n=6, 7.** Single-column lemma
  100/100 at each. Structural reason: BDI is rational polyhedral cone
  (no equations) → closed under nonneg integer scaling.
  **Branch (a) closed at $n \in \{2, 3, 4, 5, 6, 7\}$.**
- Files: `code/2026-06-12-{inverti-stratum,pi3-inv5,single-column-n67}/`;
  `for-collaborator/2026-06-12-code-results.md`.

**Browse 57 (Day 65, 2026-06-12)**: 4 agents. Keywords: iquantum crystal
branching BDI; Hopf INVERTi graded dimensions; degenerate AHA RSK
iquantum; Gelfand pair fence hyperplane stability.
- **NEW HIGH: Brundan-Wang-Webster arXiv:2505.22929** — "Categorification
  of quasi-split iquantum groups" (May 2025, 91pp). First uniform
  categorification of ALL quasi-split iquantum types via graded
  2-categories (extends KLR). BDI-type included. Natural stepping stone
  to icrystal bases for BDI. Watch for follow-ups.
- **~~NEW HIGH: Kobayashi arXiv:2509.17007~~** — **CORRECTION (Browse 58):**
  arXiv:2509.17007 is Harris-Kobayashi-Speh "Translation functors + Shimura
  varieties" — UNRELATED. The actual "Stability region of branching
  multiplicities" preprint has NO arXiv ID; it is ~6pp on Kobayashi's Tokyo
  webpage (tk2026b) and covers ONLY (gl(n+1),gl(n)) and (o(n+1),o(n)).
  **GL(n)→O(n)×O(n) = AII→BDI NOT covered. SCENARIO B CONFIRMED: Rick's
  walls are an independent discovery.** Discovery-layer moat intact.
- **CRITICAL FIND (citation trail): Azenhas arXiv:2603.16698**
  characterizes k-highest weight tableaux by **LINEAR INEQUALITIES** in
  the quantum LR map (AII = GL→Sp). These inequalities may be EXACTLY
  Rick's walls $\{m_2=0\},\{m_{236}=0\},\{m_{23456}=0\}$ for BDI.
  **Read before next PROVE session.** NEW OQ-AZENHAS-INEQUALITIES-BDI.
- **NEW: Azenhas arXiv:2604.25856** — companion "slack data" for inverse
  quantum LR map. Adjacent to BDI fence wall quantification.
- **Kobayashi fence clarification**: fence conditions = interleaving
  conditions $\xi_i + \delta\nu_j = \pm 1/2$ on infinitesimal characters.
  2604.22262 covers ONLY (O(n+1),O(n)). Extension to GL(n)→O(n)×O(n)
  **explicitly deferred** — Rick's work is the deferred case.
- **NEW MEDIUM: Colarusso-Erickson-Frohmader-Willenbring arXiv:2502.19505**
  — K-type multiplicities for $O(p)\times O(q) \hookrightarrow O(p+q)$
  via Howe duality. BDI-adjacent. Check stable-range formula vs. Rick's
  n=3 data.
- **NEW MEDIUM: Kumar-Torres 2024** — flagged hive polytopes for
  Kwon-Sundaram Sp branching (5 cites). Connects polyhedral approach to
  Sp branching; check if BDI branching cone is a hive polytope.
- **OQ-IQUANTUM-RSK-LIFT confirmed open**: both sides published (Stern
  2606.00679 GL/AHA side; Watanabe 2509.00853 AII/iquantum side);
  synthesis = iquantum JM-spectral elements absent from both.
- **OQ-NAITOSAGAKI-BDI confirmed open** (later CLOSED Day-66).
- **Q-SPHERE preprints STILL ABSENT** (conference ended June 12).
  Watch June 15-30 for De Commer type-B KL, Meereboer-Kolb branching,
  Watanabe-Hoshino bi-icrystal.
- **UPCOMING**: Anne Schilling lectures at IMJ-PRG (June 17-18,
  "Crystals and symmetric functions"). FPSAC 2026 (July 13-17):
  **Seung Jin Lee** (invited, q-weight multiplicities + KR crystals types B/C,
  arXiv:2412.20757). **NOTE: Kwon is NOT a FPSAC 2026 invited speaker** —
  that was FPSAC 2025 (Sapporo). Mittag-Leffler workshop July 27-31
  (Schilling organizer, "Solvable lattice models + quantum groups").
- Log: `reading/2026-06-12.md`.

**Browse 58 (Day 67, 2026-06-12)**: 4 agents. Keywords: iquantum crystal BDI
icrystal; combinatorial Hopf algebra quantum symmetric pair; Kobayashi stability
Gelfand pair fence; Azenhas quantum LR linear inequalities.
- **MAJOR CORRECTION: arXiv:2509.17007 misidentification.** Harris-Kobayashi-Speh
  = Shimura varieties paper, NOT "Stability region." Kobayashi's actual stability
  preprint = ~6pp, no arXiv ID, covers only (gl(n+1),gl(n)) and (o(n+1),o(n)).
  **GL(n)→O(n)×O(n) NOT covered. SCENARIO B CONFIRMED.** Discovery-layer moat intact.
- **Azenhas 2603.16698 abstract confirmed** — explicitly says "characterize by
  certain linear inequalities a family of k-highest weight semi-standard tableaux"
  in the AII (GL→Sp) quantum LR map. This IS the AII analogue of Rick's BDI walls.
  **OQ-AZENHAS-INEQUALITIES-BDI still OPEN — read 2603.16698 ASAP.**
- **Q-SPHERE preprints STILL ABSENT** (conference concluded June 12, Radboud
  University Nijmegen). De Commer type-B KL theorem talk was June 12 (final talk).
  Watanabe solo. Meereboer "work in progress." Watch arxiv.org June 13+.
- **FPSAC 2026 Kwon correction**: Kwon = FPSAC 2025 invited (Sapporo); FPSAC 2026
  relevant invited speaker = **Seung Jin Lee** (q-weight multiplicities via KR
  crystals, types B/C, arXiv:2412.20757).
- **NEW HIGH: arXiv:2510.24451 (Jang-Kwon-Uruno Oct 2025)** — crystal bases for
  quantum orthosymplectic superalgebra; "Burge correspondence of orthosymplectic
  type." Directly neighbors OQ-IQUANTUM-RSK-LIFT.
- **NEW: arXiv:2601.19670 (Song-Zhang Jan 2026)** — QSP at roots of unity; cites
  both Watanabe 2407.07280 and 2509.00853. Skim for roots-of-unity BDI structure.
- **Kobayashi 2604.22262 citations**: 1 (self-citation only). Azenhas 2603.16698
  citations: 2 (self only). Rick's 2407.07280: still 5 — no new citers post-Q-SPHERE.
- **Mittag-Leffler July 27-31**: Schilling organizer, 33 participants. RIGHT after FPSAC 2026.
- **nLab**: quantum symmetric pair page thin; coideal subalgebra page missing.
- **Grinberg-Reiner**: minor corrections update May 14, 2026.
- Log: `reading/2026-06-12-browse58.md`.

## Previous state — Day 63-64 (2026-06-11)

**Day 64 PROVE: Gap B closed in the negative via marginal-palindromy.**
The 22-point Bucket-2 configuration in $[4] \times [9] \times [8]$ admits
NO column-coordinate-respecting bijection to $\mathrm{adj}(B_3) \oplus
\mathrm{triv}$ or $\mathrm{adj}(C_3) \oplus \mathrm{triv}$.

- **Refutation argument**: extract 22 explicit triples; sorted axis
  marginals $i_2$: $\{1, 2, 9, 10\}$; $i_{236}$: $\{1,1,1,1,2,3,3,4,6\}$;
  $i_{23456}$: $\{1,1,1,2,4,4,4,5\}$. None palindromic. Every linear
  projection of $B_3$ or $C_3$ adj+triv has palindromic histogram
  (because $w_0 = -1 \in W$). $B_3$ axis multiset $\{5, 5, 12\}$, $C_3$
  $\{1,1,4,4,12\}$. **No match.** Weyl-orbit labelling $\{12, 6, 3, 1\}$
  also fails. **Calibration-grade refutation filter banked as
  `connections/marginal-palindromy-refutation.md`.**
- **OQ-PI3-MULTI-FINAL**: the MAX-stratum-vector $(3, 8, 11, 10, 19,
  14, 23, 26)$ is a NOVEL COMBINATORIAL INVARIANT of multi-chart
  projections, intrinsic BDI/AII coordinate-substitution structure
  (chain + grid + $M_2$-split). v4 §3 climax adjusted from rep-theory
  to "polytope-shadow combinatorics" — same publishability, different
  framing.
- Files: `proofs/2026-06-11-bucket2-rep-theory.md`; collaborator note:
  `memory/for-collaborator/2026-06-11-bucket2-rep-theory-refuted.md`;
  scripts: `code/2026-06-11-bucket2-extract/`.

**Day 64 LEAN: THEOREM G COMPLETE.** `BdiPolytope.lean` 552 → **866
lines**, pure stdlib, zero sorry, zero warnings, `#print axioms` ⊆
{propext, Classical.choice, Quot.sound}. Three commits shipped within-
session (`f708cfb`, `8a6eab9`, `96f032d`):
- **Lemma 4** (`Kone_two_in_cone_hull`, form b, N=2): every $v \in K_n$
  ($n \ge 3$) admits explicit nonneg integer linear combination of
  $n$ rays equal to $2v$. Constructive witness `coneCoeff n v`; clean
  facet ↔ coefficient bijection.
- **Lemma 5** (`rays_lin_indep_unique`): coordinate-descent uniqueness
  on $(c_k - c'_k)$.
- **`K_simplicial`** bundle: non-negativity + decomposition + uniqueness.
- **5/5 sub-lemmas + bundle DONE.** Theorem G's "BDI weight-space image
  cone is simplicial" is a verified Lean kernel fact (2nd complete
  Lean theorem after F-easy).
- Lattice-index-2 caveat baked into form (b) factor of 2; forms (a)
  [pure $\mathbb{Q}$] and (c) [explicit 2-torsion] deferred-but-buildable
  pending Robin's call.
- **Phantom-completion calibration HELD on Day-64**: first clean LEAN
  session post-STABLE-promotion. Procedural fix works.

**Day 64 CODE: n=4 # AXIS = 2 confirmed.** 20-piece n=4 piece registry
built by direct analog with n=3 minimal cover; Cor 8 linking variable
$\Lambda = s_1 + s_2 + s_3$ substituted out; kernel arrangement
computed on reduced 11-var AII space. **Exactly 2 codim-1 coord walls
in cone interior**: $\{\text{long}[1] = 0\}$ (44 collisions),
$\{\text{prefix}[4] = 0\}$ (21 collisions). `prefix[1]` collapsed
AXIS→RIGID at n=4. **Structural identity # AXIS = $f(n) = 3 - [n
\text{ even}]$ now verified at $n \in \{3, 4\}$ — both parities.**
File: `code/2026-06-12-n4-registry/`.

**Day 63 PROVE: OQ-PI3-MULTI refined, MODE → MAX.** The Day-62 8-vector
$(1, 5, 9, 9, 13, 17, 22, 26)$ was the MODE — sampling artifact (BDI-
feasibility contamination). Structural invariant is the MAX-vector
$(3, 8, 11, 10, 19, 14, 23, 26)$ with clean analytic identity
$\mathrm{MAX}_\sigma = \#\{\text{distinct $\sigma$-active column-profiles
among the 26 pieces}\}$. Bucket decomposition: B0 (3 R-double, sum 16)
+ B1 (M2_is_m236, sum 8) + B2 (22 generic, sum 90) = 114 = MAX-sum.
Both MODE and MAX vectors antipodally asymmetric ($I_{000} \ne I_{111}$)
→ neither is irrep weight multiplicity (Weyl-symmetry argument
universal). File: `proofs/2026-06-11-pi3-multi-investigation.md`.

**Browse 55 (Day 63, 2026-06-11)**: 7 candidate papers banked for
OQ-PI3-MULTI:
- **Andrews-Gagnon-Gélinas-Schlums-Zabrocki arXiv:2505.06941** —
  INVERTi transform for Hopf algebra graded dimensions. 5-min SageMath
  test on stratum-vector. (NEW OQ-INVERTI-STRATUM.)
- **Frohmader arXiv:2312.11295** — GL(2n) ↓ Sp(2n) Kostant-Rallis
  multiplicities on K-nilpotent cones. Structurally identical setup.
- **Naito-Suzuki-Watanabe arXiv:2502.07270** — iquantum-crystal proof
  of Naito-Sagaki AII→CI branching. Structural twin of Rick's AII→BDI.
  (NEW OQ-NAITOSAGAKI-BDI, live even post-Day-64.)
- **Horospherical stacks arXiv:2305.01571** — extends Geraschenko-
  Satriano to spherical varieties; alternative algebraic home for π̃₃'.
  (NEW OQ-HOROSPHERICAL-STACK-PI3.)
- Plus: Stern AHA! RSK (OQ-AHA-RSK template sharp), Chen-Lu-Pan-Ruan-
  Wang dual canonical bases ALL finite types, Lusztig "Strata and
  almost special reps," He-Tubbenhauer crystal category presentations,
  Caselli-Marietti type-A KL via special matchings.
- **OEIS confirmed (1,5,9,9,13,17,22,26) absent** — genuinely new.
- **26 = I(5)** = # involutions in $S_5$ (Browse 54 origin; Browse 55:
  running sum to σ=011 = 76 = I(6)). Even post-Bucket-2 refutation,
  the 26-piece registry might still be indexed by RSK-shape data of
  $S_5$ involutions. **NEW OQ-PI3-INV5** (~30min CODE check).
- **8 strata = LG(3,6) Schubert cells**, dim = 6 = dim BDI cone.
  Speculative; live alternative framework angle.
- Log: `reading/2026-06-11.md`.

**Browse 56 (Day 64 evening, 2026-06-11)**: 4 agents, headline discovery:
- **NEW OQ-KOBAYASHI-FENCES-BDI**: Kobayashi arXiv:2604.22262
  "Stability of Branching Multiplicities for Orthogonal Gelfand Pairs"
  — for (o(n+1), o(n)) pairs (= BDI type), branching multiplicities
  locally constant on convex regions, change only at "fences"
  (piecewise-linear hyperplane walls). Kobayashi's fences may be
  EXACTLY Rick's three coordinate walls {m₂=0}, {m₂₃₆=0},
  {m₂₃₄₅₆=0}. If so, stability theory EXPLAINS why exactly three
  walls exist. **HIGH PRIORITY: read in next PROVE session.**
- **OQ-HOROSPHERICAL-STACK-PI3 DOWNGRADED**: AII/BDI symmetric
  spaces are NOT horospherical (they're spherical but different
  subclass — stabilizer Sp(2n) or O(n)×O(n) does NOT contain maximal
  unipotent). Monahan's stacky-coloured-fan framework inapplicable.
  Bridge survives via **Kolb-Yakimov arXiv:2603.06132** (Q-SPHERE 2026):
  coideal subalgebras = short star products on quantum horospherical
  subalgebras. Algebraic connection preserved; geometric one absent.
  Status: "wait for spherical stacks framework."
- **OQ-INVERTI-STRATUM PRELIMINARY NEGATIVE**: a₁=1, a₂=4, a₃=0,
  a₄≈-16 for MODE vector (1,5,9,9,...). Stratum vector appears to
  FAIL INVERTi at degree 4. Need 5-min SageMath verification.
- **OQ-PI3-INV5 structural data**: RSK for S₅ involutions gives SYT
  shape-counts (1,4,5,6,5,4,1) for partitions (5),(4,1),(3,2),(3,1,1),
  (2,2,1),(2,1,1,1),(1⁵). Total = 26. Look for this 7-family
  decomposition in the 26-piece registry.
- **New watch name: Bárbara Muniz** — "Symplectic Branching through
  Crystals" (2025); independent GL→Sp branching via crystals; mutual
  citer of Naito-Suzuki-Watanabe 2502.07270.
- **Q-SPHERE preprints STILL ABSENT** (conference ended June 12).
  Watanabe-Hoshino bi-icrystal, Meereboer-Kolb, De Commer-Neshveyev
  KL-type-B: all no preprint. Watch June 15–30.
- **AHA-RSK mechanism now clear**: RSK = spectral basis change via JM
  eigenvalues in degenerate AHA. Iquantum lift = Stern (GL/q=1 side)
  + Watanabe 2509.00853 (Sp/AII side) + missing "quantum spectral
  basis change" via iquantum JM-type elements. **OQ-IQUANTUM-RSK-LIFT.**
- Log: `reading/2026-06-11-browse56.md`.

**Browse 57 (Day 65, 2026-06-12)**: 4 agents. Keywords: iquantum crystal branching BDI; Hopf INVERTi graded dimensions; degenerate AHA RSK iquantum; Gelfand pair fence hyperplane stability.
- **NEW HIGH: Brundan-Wang-Webster arXiv:2505.22929** — "Categorification of quasi-split iquantum groups" (May 2025, 91pp). First uniform categorification of ALL quasi-split iquantum types via graded 2-categories (extends KLR). BDI-type included. Natural stepping stone to icrystal bases for BDI. Watch for follow-ups.
- **NEW HIGH: Kobayashi arXiv:2509.17007** — full general fences paper ("Stability region of branching multiplicities") on Kobayashi's Tokyo website but NOT YET on arXiv. Contains the general treatment beyond (O(n+1),O(n)). **ACTION: fetch directly.**
- **CRITICAL FIND (citation trail): Azenhas arXiv:2603.16698** characterizes k-highest weight tableaux by **LINEAR INEQUALITIES** in the quantum LR map (AII = GL→Sp). These inequalities may be EXACTLY Rick's walls {m₂=0},{m₂₃₆=0},{m₂₃₄₅₆=0} for BDI. **Read before next PROVE session.** NEW OQ-AZENHAS-INEQUALITIES-BDI.
- **NEW: Azenhas arXiv:2604.25856** — companion "slack data" for inverse quantum LR map. Adjacent to BDI fence wall quantification.
- **Kobayashi fence clarification**: fence conditions = interleaving conditions ξᵢ + δνⱼ = ±½ on infinitesimal characters. 2604.22262 covers ONLY (O(n+1),O(n)). Extension to GL(n)→O(n)×O(n) **explicitly deferred** — Rick's work is the deferred case.
- **NEW MEDIUM: Colarusso-Erickson-Frohmader-Willenbring arXiv:2502.19505** — K-type multiplicities for O(p)×O(q)↪O(p+q) via Howe duality. BDI-adjacent. Check stable-range formula vs. Rick's n=3 data.
- **NEW MEDIUM: Kumar-Torres 2024** — flagged hive polytopes for Kwon-Sundaram Sp branching (5 cites). Connects polyhedral approach to Sp branching; check if BDI branching cone is a hive polytope.
- **OQ-IQUANTUM-RSK-LIFT confirmed open**: both sides published (Stern 2606.00679 GL/AHA side; Watanabe 2509.00853 AII/iquantum side); synthesis = iquantum JM-spectral elements absent from both.
- **OQ-NAITOSAGAKI-BDI confirmed open**: AII→CI proved (NSW + Muniz); AII→BDI genuinely open.
- **Q-SPHERE preprints STILL ABSENT** (conference ended June 12). Watch June 15–30 for De Commer type-B KL, Meereboer-Kolb branching, Watanabe-Hoshino bi-icrystal.
- **UPCOMING**: Anne Schilling lectures at IMJ-PRG (June 17-18, "Crystals and symmetric functions"). FPSAC 2026 (July 13-17): Jae-Hoon Kwon (invited, orthosymplectic crystals + affine RSK — highly relevant) + Seung Jin Lee (type B/C q-weight via KR crystals). Mittag-Leffler workshop July 27-31.
- Log: `reading/2026-06-12.md`.

**Day 63 CODE**: stratum-vector asymptotic to N=12 (per-stratum MAX-
constancy holds); codim-2 walls catalogued (108 + 126 pairs at ranks
2-3); n=5 single-column lemma 100/100 sampled pieces in BDI cone.
**OQ-PI3-GROWTH branch (a) closed at $n \in \{2, 3, 4, 5\}$.**

## Previous state — Day 62 (2026-06-10 deep-work, stack PINNED DOWN; Day-60 phantom fired 2nd instance)

**Day 62 PROVE: (c\*) stack candidate PINNED DOWN as concrete AII-
fibered groupoid.** Day 60: not polyhedral GIT. Day 61: not fan, not
PFL. Day 62: AII-fibered groupoid $G$ with three codim-1 walls $\{m_2 =
0\}, \{m_{236} = 0\}, \{m_{23456} = 0\}$ inside AII cone. 8 sign-strata;
MODE stratum-vector $(1, 5, 9, 9, 13, 17, 22, 26)$ (Day-63 → MAX-
refined). Variable taxonomy: 2 RIGID + 4 BINARY + 3 AXIS ($m_2$,
$m_{236}$, $m_{23456}$ with 4/10/9 distinct columns). Candidate B
(genuine multivaluedness) wins: 98.82% of N=8 AII points have
$|I(p)|>1$. **Structural identity # AXIS = # walls = $f(3) = 3$
ESTABLISHED.** Day-64 confirmed at n=4. Files: `proofs/2026-06-10-pi3-stack-structure.md`,
`code/2026-06-10-stack-structure/`, `connections/pi3-stratified-multimap.md` (Tier A),
`for-collaborator/2026-06-10-pi3-stack-pinned-down.md`.

**Day 62 CODE**: fiber-strat extended to N=10 (Candidate B confirmed
at 99.44%); single-column at n=4 (100/100); $f(5)=3, f(6)=2$
computationally confirmed.

**Day 62 LEAN: Theorem G Lemma 3 (linear independence) DONE.**
552 lines stdlib, four `partialSum_pair_*` lemmas + coordinate-descent
proof of `rays_lin_indep`. **4/5 sub-lemmas of Theorem G** — closed
Day-64. Bundled Day-60 ray-in-K_n lemmas (2nd phantom-completion
instance; rule PROMOTED to STABLE).

---

## Previous state — Day 61 (2026-06-09 evening + 2026-06-10 early, fan + PFL REFUTED + Browse 53)

**Day 61 PROVE: fan-reframe of $\tilde\pi_3'$ REFUTED both ways at finite
level.** Fan-in-AII dead (25/26 pieces have full AII domain; only
`M2_is_m236` has a nontrivial wall). Fan-in-BDI dead (367/650 ordered
pairs have 6-dim interior overlap of image cones). PFL ruled out
STRUCTURALLY: piece choice is NOT a function of $p$, so any
piecewise function fails. Multivaluedness is fundamental. Min cover
grows monotonically with N (8 → 25 from N=6 to N=10), unbounded with
Day-60's $\Theta(N^2)$. Stack (c\*) is the only candidate. Files:
`proofs/2026-06-09-pi3-fan-reframe.md`, `code/2026-06-09-pi3-fan-reframe/`,
`for-collaborator/2026-06-09-pi3-fan-reframe-refuted.md`.

**Day 61 BROWSE 53 (Q-SPHERE Day 4, conference ended): no preprint drops.**
**FPSAC 2026 proceedings live**: Marberg-Tong-Yu "Grothendieck positivity
for square root crystals" CONFIRMED short talk (OQ-LUSZTIG-MARBERG angle 3
community-live). **OQ-HMP-ACCELERATION CLOSED**: 4 new 2024-2026 HMP
citers, none cite Marberg 1306.2980. **Marberg program architecture**:
(a) twisted-involution KL positivity 1306.2980 DORMANT; (b) K-theoretic
Grothendieck/√-crystal ACTIVE (2512.23944 Dec 2025 + 2501.16640 FPSAC).
New HIGH: **Lu+Pan 2605.13578** (iHall algebra survey). New MEDIUM:
**Manon 1103.2484** (tropical branching = toric degenerations, GIT case;
gap confirms π₃ NOVELTY). **Heo 2504.12106** (polyhedral B(∞); Watanabe
bi-icrystal background). **Loho-Schymura tropical Ehrhart**: 8 citers, no
rep-theory; pioneer territory. **Lu 2311.16373**: 0 citations = clean
frontier. NEW OQ-MARBERG-PROGRAM-BRIDGE: does (b) provide route to (a)?
NEW OQ-PI3-TROPICAL: can Manon's tropical branching be adapted to non-GIT
case for AII→BDI? Log: `reading/2026-06-10.md`.

---

## Previous state — Day 60 (2026-06-09, toric-quotient NOT GIT day)

**Day 60 PROVE: Clio's toric-quotient hypothesis tested.** STRONG FORM
REFUTED at $n=3$: stack of 26 piece matrices is $156 \times 9$ with full
column rank 9; intersection of kernels = zero subspace. **AII → BDI is
NOT polyhedral GIT.** Routes OQ-PI3-GROWTH out of polyhedral category.
BDI = core BDI × $\mathbb{N}^{n-1}$ structurally true (vacuous "torus" on
BDI itself). **$f(n) = 3 - [n \text{ even}]$ closed form ESTABLISHED**
for $n \ge 3$. Verified $n=3,4,5,6$. Files:
`proofs/2026-06-10-toric-quotient-hypothesis.md`,
`code/2026-06-10-toric-quotient/`,
`for-collaborator/2026-06-10-toric-quotient-refuted-partial.md`.

**Day 60 LEAN: Theorem G start, 3/5 sub-lemmas (committed Day-62 in
bundle).** 109 → 371 lines pure stdlib. Added `partialSum`, `pairRay`,
`sumRay`, `eRay`, `InKone`, 9 sanity + 9 profile lemmas, three "ray ∈
K_n" theorems. Scoping doc 220 lines. **Day-58 (F-easy) phantom-
completion FLAGGED** (collaborator notes claim formalised; not in git).
NEW calibration rule. Day-62 bundled Day-60 ray-in-K_n lemmas in
commit. Note: `for-collaborator/2026-06-10-bdi-polytope-lean-day60-theoremG.md`.

**Day 60 REVIEW: Clio's two-row d=4 b ≡ 0 (mod 4) law CORRECT.**
Verified line-by-line + computationally at $b \in \{4,8,12,16\}$.
"Three odds sum to an odd" mechanism. Lean kernel builds (28s).
Two-row d=4 fiber-vanishing UNCONDITIONAL for half of all $b$
($b \equiv 0, 1 \pmod 4$). File: `reviews/2026-06-10-clio-d4-tworow-full-law.md`.

**Day 60 CROSS-PROGRAMME CONJECTURE** (NEW connection file
`cross-programme-dim-gap-codim.md`): same forgotten-dim count both
sides. Rick's $f(4) = 2$ = Clio's d=4 codim-2 imaginary-axis obstruction.
CONJECTURE: $f(n) = g(n) = 3 - [n \text{ even}]$. Testable at $n = 3,5,6,7$.

---

## Previous state — Day 59 (2026-06-08 evening, Q-SPHERE T+1d, the branch-(a) close)

**OQ-PI3-GROWTH at $n=3$ CLOSED in EXISTENTIAL form via single-column
auto-construction lemma.** For every BDI lattice point $g$, the linear
map $\pi^{(g)}(\mathbf{a}) := a_{m_{23456}} g$ is a valid integer-PL
piece (lands in cone trivially; image is the ray through $g$). 193-piece
registry (94 v9 multi-column + 99 single-column auto-pieces) closes
$N \le 15$ at 100% coverage:

| $N$ | $|\mathsf{P}^{\mathrm{BDI}}_3|$ | v9 cov | with auto |
|-----|---:|---:|---:|
| 11 | 2757 | 99.75% | 100% |
| 15 | 11225 | 98.95% | 100% |

Single-column construction unbounded as $N \to \infty$ ($\Theta(N^2)$
growth: 42 → 139 → 257 new primitives at $N = 16, 17, 18$). **Refined
open question OQ-PI3-GROWTH-FINITE**: $\sup_N K(3, N) < \infty$ at
the non-polyhedral level? Day-60 says probably YES at tropical/stacky.

**Day 59 Step 4: dim-gap parity at $n=5, 6$ analytically confirmed.**
$n=5$ (odd): dim AII = 15, gap = 3. $n=6$ (even): dim AII = 17 (= $3n
- 1$, linking eq), gap = 2. Day-56's "dim AII = 18 at $n=6$" was
VARIABLE count not affine-hull DIMENSION. Day-56 table salvageable
as "variable count" column.

**Day 59 Browse 51 (Q-SPHERE Day 2):** Marberg-Tong-Yu 2501.16640
FOUND (FPSAC 2026 preprint, OQ-LUSZTIG-MARBERG angle 3 entry). Stern
2305.08301 precursor to AHA RSK (JM/weight basis machinery). Huh-
Jung-Kim-Park 2606.07493 (i-boxes vs Demazure weaves cluster
equivalence in symmetric type, HIGH). Three structural parallels
banked: Stern slide ↔ Marberg raising; OQ-AHA-RSK template sharp;
cluster/QSP/canonical-basis triangle (Path 1 ↔ Path 2 ↔ Path 4 NEW).

Files: `proofs/2026-06-09-pi3-growth-a.md`,
`proofs/2026-06-09-dim-gap-parity-n5-n6.md`,
`reading/2026-06-08-browse51.md`,
`memory/for-collaborator/2026-06-09-pi3-growth-day59-clio.md`.

---

## Previous state — Day 58 (2026-06-08, Q-SPHERE T+0d, two-falsification day)

26-piece $\tilde\pi_3'$ verified 100% at $N \le 10$ (PROVE) →
"for all N" suffix EMPIRICALLY FALSIFIED at $N=11$ (CODE, 98.15% at
$N=15$; missing family $B_2 = T_2$ + large $T_1$). Dim-gap PARITY
CORRECTION: odd $n=3$, even $n=2$ (Day-56 "constant 3" refuted via
Clio's Q3 at $n=4$, $m_{1234568}$ determined by linking eq). Ehrhart
honest recompute through $N=120$: BDI deg-3 period-6 leading 1/18,
AII deg-4 period-6 leading 1/288, ratio $\to N/16$. Lean (F-easy)
purportedly fully formalised in 408 lines stdlib (Day-60 LEAN flagged
NOT IN GIT — phantom completion; need re-derivation). NEW question
OQ-PI3-GROWTH. Files: `proofs/2026-06-08-pi3-construction.md`,
`code/2026-06-08-*/`,
`memory/for-collaborator/2026-06-08-{pi3-surjectivity-closed,bdi-polytope-lean-day58}.md`.

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
- **Path 2 + Path 4:** π_n canonical projection (Day 56). Day-58 parity correction + Day-60 closed-form $f(n) = 3 - [n \text{ even}]$. Theorem at $n=2$ (linear); existential close at $n=3,4$ (single-column lemma); **Day-60 NOT polyhedral GIT**; **Day-61 NOT fan, NOT PFL**; **Day-62 (c\*) stack PINNED DOWN as AII-fibered groupoid** with three codim-1 walls + stratum-vector $(1,5,9,9,13,17,22,26)$ + structural identity # AXIS = # walls = $f(3) = 3$.
- **Path 2 + Path 4 NEW Day-62:** π̃₃' stratified multimap (`connections/pi3-stratified-multimap.md`). Concrete realisation of (c\*) stack candidate. Tier A; could promote to Tier S if OQ-PI3-MULTI surfaces rep-theoretic meaning.
- **Path 2 + Path 4 Day-60:** Cross-programme dim-gap = obstruction codim conjecture. $f(n) = g(n) = 3 - [n \text{ even}]$. Day-62 strengthened by structural identity at $n=3$. Testable at $n = 3,5,6,7$.
- **Path 2 + Path 4:** carry $P_a$ six-roles unification (Day 56). Theorems E, F, G + projection. **Lean Theorem F-easy COMPLETE Day-66** (`b0a79b2`, axiom set `[propext, Quot.sound]`); Theorem G COMPLETE Day-64 (`K_simplicial`, form (b), axiom set `[propext, Classical.choice, Quot.sound]`).
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL positivity conjectures (1306.2980) unguarded. Marberg-Tong-Yu 2501.16640 (Day-59 found) = OQ-LUSZTIG-MARBERG angle 3 entry. Long-horizon for v4+.
- **Path 1 (combinatorial Hopf):** NSym^B from H^B_*(0) still open (OQ-HUANG-B). Seed Q4 (q=0 combinatorial Hopf) externally unconstrained.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`azenhas-bdi-canonical-projection.md`** (Day 56, **Day-58 + Day-60 + Day-61 + Day-62 major updates**) — Canonical forgetful surjection $\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_n$. THEOREM at $n=2$ (verified to N=20). At $n \in \{3, 4\}$: OQ-PIN-SURJ EXISTENTIAL CLOSED (single-column auto-construction). **Day-60: NOT polyhedral GIT**. **Day-61: NOT fan, NOT PFL**. **Day-62: (c\*) stack PINNED DOWN as AII-fibered groupoid** with three codim-1 walls = three AXIS vars = $f(3) = 3$. v4 Remark 3.5 fully reframed.
- **`pi3-stratified-multimap.md`** (Day-62 origin, **Day-63/64 major updates**, Tier A) — (c\*) stack candidate concretely. AII-fibered groupoid $G$; MAX-vector $(3, 8, 11, 10, 19, 14, 23, 26)$ on 8 sign strata with analytic identity (# σ-active column-profiles); variable taxonomy (2 RIGID + 4 BINARY + 3 AXIS at n=3); structural identity # AXIS = # walls = $f(n) = 3 - [n \text{ even}]$ verified at $n \in \{3, 4\}$. **Day-64 OQ-PI3-MULTI-FINAL: Bucket-2 NOT rep-theoretic** (marginal-palindromy refutation); novel combinatorial invariant. Tier-S-promotion contingent (rep-theoretic meaning) DORMANT.
- **`cross-programme-dim-gap-codim.md`** (NEW Day-60) — Cross-programme conjecture $f(n) = g(n) = 3 - [n \text{ even}]$ at $n = d \ge 3$. Same forgotten-dim count both sides: Rick polytope side vs Clio fiber-vanishing side. Verified $n=4$. Testable. Tier A active; v4 §3 unifier if confirmed.
- **`discovery-layer-is-the-moat.md`** — Day 39 origin. AI harnesses verify; only humans+frameworks discover. Five evidence layers: empirical < community-internal < structural < mechanical < live community attack. Day-56 new instance: Clio's peer-review reframe that turned a CLOSED-NEGATIVE verdict into a PROVED-POSITIVE theorem is a discovery event no AI reading preprints would surface. Add to journal.
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles (Day 56 add). v3 structural climax. (1) descent-recording; (2) singleton cross-chain coupling → Theorem E; (3) chain-MB / carry-recursive factorization; (4) chain-side polytope completeness Theorem F ($2n-3$ facets); (5) weight-projection invariant Theorem G ($n$-facet simplicial cone); (6) image of canonical AII projection $\pi_n$, kernel parametrized by Singleton fiber.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Chain polytope $\mathbb{P}_n$ has exactly $2n-3$ non-redundant carry facets. **STATUS Day-66: F-easy RESOLVED.** Re-derived in `BdiPolytope.lean` commit `b0a79b2` (Day-66 LEAN), 240-line non-redundancy bundle (`E_/L_/U_nonredundant`), pure stdlib, axiom set `[propext, Quot.sound]`. Day-58 phantom-completion flag CLEARED.  Hard half (codim-1 verification using convex-polytope library) still future work, would need Mathlib.
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. Image polytope $\mathbb{K}_n^+ \subset \mathbb{R}^n$ = simplicial cone with $n$ facets. **Day-64 LEAN: COMPLETE.** 5/5 sub-lemmas + `K_simplicial` bundle. 866 lines pure stdlib, zero sorry, std axioms only. Form (b) shipped (factor of 2 = lattice-index obstruction); forms (a) [pure $\mathbb{Q}$] and (c) [explicit 2-torsion] deferred-but-buildable pending Robin's call. **Verified Lean kernel fact**: "BDI weight-space image cone is simplicial." Companion: Day-66 LEAN shipped Theorem F-easy non-redundancy (`b0a79b2`), so the F & G Lean ledger is now in sync with the Day-58/Day-60 collaborator-note claims.
- **`kobayashi-rick-non-overlap.md`** — Level sets ($\sim 4n^2$ in joint $(\lambda,\nu)$-space, Kobayashi) vs support ($n$ partial-sum facets, Rick). Complementary slicings.
- **`open2-watanabe-2407-existence-meereboer-1dim-collapse.md`** — v3 OPEN-2 Layer 1 FREE via Watanabe 2407 §5; Layer 2 → Theorem E. Re-examine post-OQ-PIN-SURJ resolution (may collapse uniformly).
- **`asymmetry-is-the-result-seven-instances.md`** — Crystal in EXPLOITATION mode.
- **`compression-is-content.md`** — Three asymmetric mechanisms (compression / re-allocation / structural-reorg).

### Tier A — Active

- **`bucket-0-as-sl2-rump.md`** (NEW Day-66) — PARTIAL REP-THEORETIC
  RESCUE of OQ-PI3-MULTI-FINAL. After Day-64 refuted "all 26 pieces are
  rep-theoretic," Day-66 PROVE showed the 4 special pieces (Bucket-0 +
  Bucket-1) form $\mathrm{adj}(\mathfrak{sl}_2) \oplus \mathbb{C} =
  \mathfrak{gl}_2$ as an $A_1$-module, uniform in $n$. B0 = 3 weights of
  $V(2\omega_1)$ via $\alpha \mapsto 2 - \alpha$ reflection on $S$-mass
  coordinate; B1 = trivial. Cap $\alpha \le 2$ is BDI-feasibility-forced
  AND equals $\dim V(2\omega_1) - 1$, invariant in $n$. v4 §3 now has
  mixed-structure climax: head $\mathfrak{gl}_2$ + bulk novel.
- **`marginal-palindromy-refutation.md`** (NEW Day-64) — Calibration-grade
  refutation filter: when testing whether a candidate combinatorial
  configuration realises a $B_n / C_n / D_{2k} / E_7 / E_8 / F_4 / G_2$
  representation, compute axis marginals first; $w_0 = -1$ forces
  palindromy. Day-64 fired to kill Bucket-2 ↔ adj($B_3 / C_3$)⊕triv in 5
  lines. General-purpose tool for cone-shadow / polytope-shadow combinatorics
  questions.
- **`marginal-palindromy-refutation-v2.md`** (NEW Day-66) — Twisted
  extension to $w_0 \ne -1$ types ($A_n, D_{2k+1}, E_6$). Twisted
  condition $H_{\ell_i}(k) = H_{\ell_{\sigma_0(i)}}(-k)$; for
  axis-length-distinct configs, reduces to plain palindromy.
  **Closes the catalogue: all simple Lie types covered.** Day-66 fired
  to refute the $D_3 = A_3$ ($\mathfrak{so}_6$) loophole at direct-marginal
  level *before* SageMath enumeration.
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
- **OQ-PIN-SURJ** (Day 56 opened; Day-59 EXISTENTIAL CLOSED at n=3; Day-62/63 EXTENDED at n=4, 5) — single-column auto-construction lemma 100% at $n \in \{2, 3, 4, 5\}$. Single-column unbounded $\Theta(N^2)$. OQ-PI3-GROWTH-FINITE pivots.
- **OQ-PI3-GROWTH** — **Polyhedral GIT REFUTED** (Day-60); **fan + PFL REFUTED** (Day-61); **(c\*) STACK PINNED DOWN as AII-fibered groupoid** (Day-62). Branch (a) existential closed at $n \in \{2, 3, 4, 5\}$.
- **OQ-PI3-MULTI-FINAL** (Day-62 opened; Day-63 refined MODE→MAX; Day-64 CLOSED NEGATIVE) — Bucket-2 22-point config in $[4] \times [9] \times [8]$ is NOT $\mathrm{adj}(B_3 / C_3) \oplus \mathrm{triv}$ via marginal-palindromy refutation. MAX-vector $(3, 8, 11, 10, 19, 14, 23, 26)$ is novel combinatorial invariant. v4 §3 climax: "polytope-shadow combinatorics" (publishable).
- **OQ-DIMGAP-CODIM** (Day-60 opened; Day-62 structural; Day-64 verified at n=4) — $f(n) = g(n) = $ # AXIS vars = # codim-1 walls = $3 - [n \text{ even}]$. Verified on Rick side at $n \in \{3, 4\}$ (both parities). Clio's $g(d)$ at $d \in \{3, 5, 6, 7\}$ still uncomputed. HIGH priority cross-programme conjecture.
- **OQ-PI3-INV5** (Day-64 opened; **Day-65 CLOSED-COINCIDENTAL**) — 26-piece registry marginals don't match $I(5)$ cycle types or RSK shapes; n=4 has 20 pieces ≠ $I(6) = 76$. Numerical coincidence at $n=3$ only.
- **OQ-NAITOSAGAKI-BDI** (Day-63 opened; Day-65 NSW deep read narrowed to so_6 loophole; **Day-66 fully CLOSED-NEGATIVE**) — three independent obstructions kill Bucket-2 ↔ $\mathfrak{so}_6$ branching: dim gap, branching obstruction, marginal-pattern. Bucket-2 is genuinely novel combinatorics, not a $\mathfrak{so}_n$-branching shadow at any rank ≤ 3.
- **OQ-INVERTI-STRATUM** (Day-63 opened; **Day-65 CLOSED-NEGATIVE**) — Both MODE and MAX vectors FAIL INVERTi nonnegativity. Cleanest Hopf candidate (free noncommutative cocommutative connected) ruled out for both stratum vectors.
- **OQ-KOBAYASHI-FENCES-BDI / OQ-KOBAYASHI-2509.17007** (NEW Day-65 Browse 57, HIGH) — Are Rick's three coordinate walls $\{m_2=0\}, \{m_{236}=0\}, \{m_{23456}=0\}$ the deferred AII→BDI fences in Kobayashi's program? Kobayashi 2604.22262 explicitly defers GL(n)→O(n)×O(n) case; Kobayashi 2509.17007 (on his Tokyo webpage, NOT YET on arXiv) may already cover it. **HIGHEST priority action: fetch 2509.17007 directly.** See `questions/q-kobayashi-fences-bdi.md`.
- **OQ-AZENHAS-INEQUALITIES-BDI** (NEW Day-65 Browse 57, HIGH) — Are Azenhas's linear inequalities for $k$-highest weight tableaux in the quantum LR map (arXiv:2603.16698) the same as Rick's three coordinate walls? Companion 2604.25856 on "slack data" adjacent. **Read both before next wall-structure PROVE.** See `questions/q-azenhas-inequalities-bdi.md`.
- **OQ-AZENHAS-SLACK** (NEW Day-65 Browse 57, MEDIUM) — Slack-data quantification of "distance to wall." Adjacent to Kobayashi stability regions. ~0.5d.
- **OQ-BRUNDAN-WANG-WEBSTER-BDI** (NEW Day-65 Browse 57, MEDIUM) — Does Brundan-Wang-Webster arXiv:2505.22929 (uniform categorification of quasi-split iquantum groups) produce BDI icrystal bases? Watch for follow-ups.
- **OQ-KUMAR-TORRES-HIVES** (NEW Day-65 Browse 57, MEDIUM) — Is BDI branching cone a hive polytope or face of one? Kumar-Torres 2024 polyhedral approach to Sp branching.
- **OQ-HOROSPHERICAL-STACK-PI3** (Day-63 opened; status DORMANT post-Browse 54-55, spherical-but-not-horospherical) — Bridge survives via Kolb-Yakimov but geometric connection absent. Wait for spherical stacks framework.
- **OQ-LUSZTIG-MARBERG** (P_PARK #1) — Three attack angles: (a) Zhang+Lusztig molecule-cell; (b) optional Bhattacharya TC^J; (c) Marberg-Scrimshaw P/Q-key via square root crystals — angle-3 gap named-paper-shaped (Marberg-Tong / Marberg-Tong-Yu / Marberg-Scrimshaw). Effort ~5.5d (angles 1+2). **Browse 53 architecture update:** Marberg program has TWO tracks: (i) K-theoretic Grothendieck positivity via sqrt-crystals [ACTIVE — 2512.23944 Dec 2025 + 2501.16640 FPSAC 2026 SHORT TALK confirmed in proceedings]; (ii) twisted involution KL positivity 1306.2980 [DORMANT — 0 citers 2016-2026; Marberg not attacking directly]. Track (i) may converge to track (ii) if a "shifted square root crystal" is built — not yet. Four conjectures of 1306.2980 **remain open and unguarded** (confirmed OQ-HMP-ACCELERATION check). Watch for Marberg-program shifted-√ output 2026-2027.
- **OQ-ZHANG-MARBERG** — Does Zhang 2412.07810 + Lusztig 2510.21499 resolve Marberg's 4 twisted-involution KL conjectures? P=35%. Three-sided dormancy.
- **OQ-HUANG-B** (P_PARK #3) — NSym^B as standalone Hopf algebra. Entry point: Kim-Searles 2601.22926 (QSym^B SOTA, comodule) → NSym^B = contravariant dual. Technical route: Almousa-Lu 2601.13324 ribbon-complex dualized to type B.
- **OQ-LU-PAN-EXPLICIT** (P_PARK #4) — Explicit formula for Chen-Lu $C_b$ on split $B_n$? Entry: Appendix A of 2601.00524. Template: Ziming Chen 2601.13482 (rank-1 AIII).
- **OQ-G-INTRINSIC** (P_PARK #2) — Coordinate-free $\mathcal{K}_n$ as "dominant chamber + one carry-wall."
- **OQ-AHA-RSK** (NEW Day 57 Browse 49; template sharpened Browse 50) — Does Berele insertion (Watanabe's type-AII RSK) admit spectral basis-change realization in degenerate affine iquantum algebra H^ı_n, analogous to Stern's AHA result for classical RSK via JM elements? Template: Stern 2606.00679 (FULL READ Browse 50): RSK = basis change in degenerate AHA H_n via slide operators = products of normalized intertwiners φ̃_i; purely type A; zero QSP. Type-AII analog: H^ı_n + Berele-slide = product of i-intertwiners. Kobayashi-Matsumura 2506.06951 confirms Berele insertion is purely combinatorial (no Hecke realization yet). Gap is real, open. ~1d. See `questions/q-iquantum-aha-rsk.md`.
- **OQ-TYPEB-AHA-RSK** (NEW Browse 52) — Does type-B degenerate AHA + type-B JM elements realize type-B RSK as a spectral basis change, analogous to Stern's type-A result? Lu 2311.16373 gives the Schur-Weyl anchor. Gap = ι-JM elements + ι-slide operators. ~0.5d once Lu stack is read.
- **OQ-HMP-ACCELERATION** (NEW Browse 52; **RESOLVED Browse 53**) — **CLOSED.** 4 new 2024-2026 HMP citers (Shevchenko 2511.23446, Green-Xu 2510.25041, Marberg-Wen 2412.18963, Kinser-Lanini-Rajchgot 2410.06929); **none cite Marberg 1306.2980.** Community cites HMP for involution word combinatorics, routes around KL positivity. Conjectures unguarded and open. Marberg himself has shifted to K-theoretic Grothendieck positivity (2512.23944, FPSAC 2026). See Browse 53 log.
- **OQ-MILLS-TYPEB** (horizon) — Mills Part III for $H_{(B_n, A_{n-1})}$? Mills 2605.23072 = Part II (Browse 48).
- **OQ-GhaniDual** — $T^{\mathrm{obs}}_\delta$ as graded comonad / opfibration map / profunctor.
- **OQ-G2 (parked)** — Non-bracket framework for $G_2$.
- **`q-type-B-cactus.md`** — Littelmann-path level CLOSED (Torres EJC 2024); KN-tableau level open.
- **`q-KL-from-crystal.md`** — Spin/acyclic CLOSED. Non-spin: 2-step bigraded complex required.
- **`q-zero-CHA.md`** — Type A K_0/derived levels answered. Type B NSym^B from H^B_*(0) still open.

**Closed:** OQ-K (Day 29: F+G), OQ-BDIqLR (Day 26-28), OQ-KOB-MATCH (Day 41), OQ-CHEN-LU (Day 42), OQ-BWB / OQ-PJ (Day 18), OQ-MUNIZ-CARRY (Browse 20), OQ-FROHMADER (Day 29), OQ-KOBAYASHI-SL2 (Day 29), OQ-LAUVE-RQSYM (Day 50), **OQ-PI3-MULTI-FINAL Gap B** (Day 64: Bucket-2 not rep theory at $B_3, C_3$), **Gap C** (Day 66: Bucket-0 + Bucket-1 = $\mathfrak{gl}_2$ POSITIVE), **OQ-NAITOSAGAKI-BDI** (Day 66: so_6 fully closed-negative), **OQ-INVERTI-STRATUM** (Day 65: both MODE and MAX fail), **OQ-PI3-INV5** (Day 65: 26 = I(5) coincidental). **OQ-AZENHAS-BDI (P_PARK #5):** verdict CLOSED-NEGATIVE Day 55; REFRAMED to canonical-projection theorem Day 56 (proved at n=2, open at n≥3 via OQ-PIN-SURJ).

---

## Next session priorities

**P-1 — Wake-routine PROVE-check + git-state-verification check** (Day 44 rule + Day-60 phantom-completion rule, STABLE; Day-64 LEAN session held discipline cleanly; Day-66 LEAN F-easy phantom CLEARED via re-derivation — calibration rule validated on its worst case).

**P0 — Fetch Kobayashi arXiv:2509.17007 directly from his Tokyo webpage** (Browse 58, ~June 13-15). Most actionable next move. May already contain the deferred GL(n)→O(n)×O(n) case Rick is computing.

**P0 — Read Azenhas arXiv:2603.16698 + 2604.25856.** Are the linear inequalities characterising k-highest weight tableaux in the AII quantum LR map the same as Rick's three coordinate walls? Most actionable PROVE move on wall structure.

**P0 — Robin endorsement decision STILL pending** (since Day 56). Daily email shipped Day-64 13:13 UTC. Day-67 outbound: Bucket-0 = $\mathfrak{sl}_2$ rescue note for Clio + cross-programme n=4 data point + n=4 R-double correction flag.

**P0 — Robin Lean form (a)/(c) call** for Theorem G — form (b) shipped Day-64. Forms (a) and (c) deferred-but-buildable refactors. Pending Robin.

**P0 — F-easy phantom-completion resolution.** **RESOLVED Day-66** via re-derivation in commit `b0a79b2` (`E_nonredundant`, `L_nonredundant`, `U_nonredundant`, axiom set `[propext, Quot.sound]`).  This was the oldest open phantom in the calibration ledger; closure validates the Day-60 commit-or-die discipline.

**P0 — Clio outbound** on Bucket-0 = $\mathfrak{sl}_2$ rescue + cross-programme n=4 data point + n=4 R-double correction flag. Day-67 morning.

**P1 — Day 67 PROVE.md target options:**
- **(A) Read Azenhas arXiv:2603.16698 + 2604.25856.** Are the linear inequalities Rick's three walls? Single most actionable PROVE move on wall structure. **PROBABLE PRIMARY TARGET.** ~1d.
- **(B) Fetch Kobayashi arXiv:2509.17007** from his Tokyo webpage and check for GL(n)→O(n)×O(n) case. ~2-4h. CODE/Browse-adjacent.
- **(C) Read Brundan-Wang-Webster arXiv:2505.22929 abstract+intro** for BDI icrystal infrastructure status. ~0.5d.
- **(D) Read Colarusso-Erickson-Frohmader-Willenbring 2502.19505** stable-range formula vs Rick's n=3 data. ~1d.

**P1 — Day 67 LEAN.md options:**
- **(E) Theorem G form (c) refactor** (explicit 2-torsion correction). ~1 LEAN session.
- **(F) `Fin (n-1)` Fence inductive wrapper** over F-easy + F lemmas. ~1 LEAN session.
- **(G) Move past polytope:** formalise Corollary 6 (Azenhas projection) or Day-66 Bucket-0 = $\mathfrak{sl}_2$ result.

**P1 — Day 67 CODE.md options:**
- **(H) n=4 R-double registry correction.** Re-classify `prefix[1]` with 3 R-double pieces added; check if # AXIS = 2 at n=4 still holds. ~30min.
- **(I) Single-column lemma at n=8+** (continuing the chain). ~30min.
- **(J) n=5 piece registry** (predicted # AXIS = 3, odd parity). ~2-3h.

**HARD DEADLINE: Browse 58 ~June 13-15.** PRIORITY: fetch Kobayashi 2509.17007. Plus Q-SPHERE preprint recheck (Watanabe-Hoshino, Meereboer-Kolb, De Commer); IMJ-PRG Schilling slides post-June-18.

**P_PARK (post-v3 arXiv, preference order):**
1. **OQ-LUSZTIG-MARBERG** — ~5.5d (angles 1+2). Read order: Lusztig v1→v2 diff → Watanabe 2023 → Zhang 2412/2503 → Lusztig 2510.21499 → Marberg-Scrimshaw 2306.00336 → **2501.16640** (angle 3 entry: Marberg-Tong-Yu "Grothendieck positivity for normal √-crystals," FPSAC 2026, raising operators → Hecke insertion, **Browse 51 CONFIRMED**) → Marberg 1306.2980 → optional Bhattacharya 2602.19508.
2. **OQ-G-INTRINSIC**.
3. **OQ-HUANG-B** — Kim-Searles entry.
4. **OQ-LU-PAN-EXPLICIT** — Chen-Lu Appendix A; Chen rank-1 AIII template. ~½d.
5. **OQ-PIN-SURJ** (Day 56 add, promoted from P_PARK #5 reframe) — n=3 modified projection. ~1-2d at n=3. Singleton-aware double-prefix conjecture. May upgrade to P1 if Robin gives green light to substantive work pre-Q-SPHERE.
6. **Stern 2606.00679** — AHA RSK = spectral basis change in H_n via JM elements. HIGH. Entry point for OQ-AHA-RSK. ~1d read. Read with **2305.08301** (Stern 2023, "From Young's Lattice to Coinvariants," Browse 51 — sets up JM/weight-basis machinery). Reference lineage: Ram 2004 (41 cit) = direct ancestor. (Browse 49/51)
6b. **Lu arXiv:2311.16373** (Browse 52, HIGH) — Schur-Weyl duality: degenerate AHA type BC ↔ twisted super Yangians type AIII. This is the **H^ι_n algebraic home** for OQ-AHA-RSK. ~1d. Read after Stern stack.
6c. **arXiv:2408.06981** (Browse 52, MEDIUM) — twisted Yangians as degenerations of affine iquantum groups. OQ-AHA-RSK architectural context. ~0.5d.
6d. **2606.07493** (Huh-Jung-Kim-Park, June 8, 2026) — quantum AFFINE cluster: i-boxes vs Demazure weaves give isomorphic cluster algebras. HIGH. ~0.5d skim. **NOTE:** "i-box" ≠ iquantum — paper is KKOP quantum affine school + Casals-Galashin-Lam braid variety school. Path 2 adjacent (quantum affine), NOT via iquantum symmetric pairs. Browse 51 "Path 1↔2↔4 triangle" claim RETRACTED. (Browse 52 correction)
6e. **Ming Lu + Pan arXiv:2605.13578** (May 2026, Browse 53, HIGH) — Survey of iHall algebra / dual canonical basis program, iquiver algebras, geometric positivity. **Essential survey for the iquantum canonical basis program.** Same research group as iHopf algebras 2511.11291 (Chen-Lu-Pan-Ruan-Wang Part I). ~1d. Read after current queue; before OQ-LUSZTIG-MARBERG engage for full iquantum context.
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
18. **Loho-Schymura arXiv:1908.07893** (Browse 52, MEDIUM) — Tropical Ehrhart theory. Counts integer points in tropical polytopes. Framework candidate for OQ-PI3-GROWTH-FINITE: if BDI cone has tropical polytope structure, this bounds K(3,N). ~0.5d.
19. **Geraschenko-Satriano arXiv:1107.1906** (Browse 52, LOW) — Toric stacks I. Stacky fans vs polyhedral GIT. Reference for AII→BDI multi-chart $T^{n-1}$-equivariant structure. ~0.5d.
20. **Bi arXiv:2606.05184** (Browse 52, MEDIUM) — Kac-Moody open Richardson in symmetric type. KKOP framework in symmetric type. Possible QSP/iquantum cluster bridge. ~0.5d.

**Browse 49 DONE (June 8, T-0d Q-SPHERE).** No preprint drops (normal lag). Watanabe 2407 = flat (4). Q-SPHERE schedule confirmed exact. **Key find: Stern 2606.00679 (AHA RSK = spectral basis change in H_n, HIGH, OQ-AHA-RSK filed).** 

**Browse 50 DONE (June 8, Q-SPHERE Day 1).** No preprints (Watanabe-Hoshino / Meereboer-Kolb). Verbatim bi-icrystal abstract confirmed. De Commer NTY co-authors CONFIRMED (suspension LIFTED). Marberg-Tong-Yu FPSAC 2026 talk on Grothendieck/√-crystal positivity (new data for OQ-LUSZTIG-MARBERG). Stern 2606 FULL READ: OQ-AHA-RSK template sharp (degenerate AHA, slide operators = product of normalized intertwiners φ̃_i). Huang-Zhang 2605.20383 dual affine RSK new find. No cite acceleration. Reading log: `reading/2026-06-08-browse50.md`.

**Browse 51 DONE (Day 59, 2026-06-08, Q-SPHERE Day 2).** No Watanabe-Hoshino or Meereboer-Kolb preprints yet (recheck June 9-10 / June 10-12). **2501.16640 FOUND** = Marberg-Tong-Yu FPSAC 2026 preprint (Grothendieck positivity for normal √-crystals, Hecke insertion connection = OQ-LUSZTIG-MARBERG angle 3). **Stern 2305.08301** = new companion precursor to AHA RSK (JM/weight-basis machinery). **2606.07493** (Huh-Jung-Kim-Park) = NEW HIGH: i-boxes vs Demazure weaves cluster comparison in symmetric type. No citation acceleration (indexing lag). Structural parallel: Stern slide operators ↔ Marberg raising operators in K-RSK. IMJ-PRG Schilling "Crystals and symmetric functions" confirmed June 17-18. Reading log: `reading/2026-06-08-browse51.md`.

**PROVE.md status (Day 59):** WRITE. Target OQ-PI3-GROWTH (primary) + dim-gap parity n=5,6 (add-on). ~1d.

---

## Calibration rules (active, most recent first)

- **Day 60 — Phantom-completion check (PROMOTED STABLE Day-62, 2 instances).** Before SUMMARY/journal/collaborator-note asserts "formalised," "shipped," or "completed," verify the claim against `git log --oneline <file>`. **Instance 1 (Day-58 F-easy):** 408-line claim NOT in git on Day-60. **Instance 2 (Day-60 Theorem G start):** three "ray ∈ K_n" lemmas on disk but NOT committed; Day-62 LEAN bundled them with Lemma 3 commit. Two instances in 4 days, same failure mode = LEAN sessions skip the commit step. **Operational rule: every LEAN session ends with `git push` or the work counts as phantom.** Day-62 collaborator note proposes "commit-or-die" convention to Robin. Companion to Day-58 verify-before-promote-for-all-N. Generic principle: **claims must be verified at the promotion layer.**
- **Day 60 — Productive-falsification of strong hypotheses.** When a collaborator-proposed structural hypothesis (e.g., "toric quotient") is testable by a single computational move (e.g., common-kernel computation across pieces), do the test even at the cost of one PROVE session. Refutation is cheap and structurally productive: today's toric-quotient refutation at $n=3$ routed OQ-PI3-GROWTH OUT of polyhedral category into Path 2/3 framings, which is the right structural direction. The alternative (assuming the hypothesis, building on it) would have wasted multiple cycles.
- **Day 58 — Verify-before-promote-for-all-N.** When a PROVE session verifies a claim "for $N \le k$" and writes "conjectured for all $N$," IMMEDIATELY (same session if possible, else the next CODE session) push the verifier past $k$. A "for all N" suffix on an unproven claim is a flag, not a result. Day-58's 26-piece $\tilde\pi_3'$ was verified to N=10 with the suffix; CODE found it leaks at N=11 within the same day. The discipline cost is one extra CODE invocation; the cost of NOT doing it is a phantom claim in load-bearing connection files.
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

- **Day 65-66 dream (2026-06-12) — DONE.** Day 65: NSW deep read + OQ-NAITOSAGAKI-BDI mostly closed-negative with so_6 loophole + INVERTi/26=I(5)/single-column n=6,7 follow-ups + Browse 57 (Kobayashi 2509.17007, Azenhas linear inequalities, Brundan-Wang-Webster categorification). Day 66: PROVE Gap C closed POSITIVE (B0 + B1 = $\mathfrak{gl}_2$ uniform in $n$) + LEAN F-easy phantom CLEARED (240 lines, axiom set [propext, Quot.sound]) + CODE OQ-NAITOSAGAKI-BDI fully closed via so_6 enumeration + marginal palindromy v2 (twisted, closes catalogue). ONE new connection (`bucket-0-as-sl2-rump.md`, Tier A — partial rep-theoretic rescue). TWO new questions (`q-kobayashi-fences-bdi.md`, `q-azenhas-inequalities-bdi.md`, both HIGH). THREE targeted edits (`pi3-stratified-multimap.md` head/bulk update; `azenhas-bdi-canonical-projection.md` Day-65/66 status; `bdi-kobayashi-polytope-faces.md` F-easy CLEARED). NO PERSONALITY EDIT. Streak 51/51.
- **Day 63-64 dream (2026-06-11) — DONE.** Day 63 OQ-PI3-MULTI refined MODE→MAX + Browse 55 surfaced 7 candidates + 26=I(5)/76=I(6)/LG(3,6) coincidences. Day 64 PROVE killed Bucket-2 ↔ adj($B_3 / C_3$) via marginal-palindromy + LEAN Theorem G COMPLETE 5/5 + CODE n=4 # AXIS = 2 confirmed. ONE new connection file (`marginal-palindromy-refutation.md`, Tier A) + ONE new question file (`q-26-piece-involutions.md`, OQ-PI3-INV5). THREE targeted edits (`pi3-stratified-multimap.md` MAX-refinement + Day-64 closure; `bdi-kobayashi-weight-space-simplicial.md` Theorem G COMPLETE; `cross-programme-dim-gap-codim.md` n=4 both-parity confirmation). q-pi3-multi-stratum-vector.md updated CLOSED-NEGATIVE. NO PERSONALITY EDIT. Streak 49/49 (Day-62 #47 → Day-63 #48 refinement + browse → Day-64 #49 Bucket-2 refutation + Lean closure + n=4 AXIS).
- **Day 61-62 dream (2026-06-10) — DONE.** Day 61 fan-reframe REFUTED + Browse 53 + Day 62 stack PINNED DOWN + single-column at $n=4$ + Lean Theorem G Lemma 3 consolidated. ONE new connection file (`pi3-stratified-multimap.md`, Tier A) + ONE new question file (`q-pi3-multi-stratum-vector.md`, OQ-PI3-MULTI, HIGH). THREE targeted edits. Day-60 phantom-completion PROMOTED to STABLE (2 instances). Streak 47/47.
- **Browse 53 (Day 61, 2026-06-10) — DONE.** Q-SPHERE Day 4 (conference ended). No preprint drops. **FPSAC 2026 proceedings LIVE**: Marberg-Tong-Yu confirmed SHORT TALK. **OQ-HMP-ACCELERATION RESOLVED**: 4 new HMP citers, none cite Marberg 1306.2980. **Marberg architecture**: K-theoretic ACTIVE (2512.23944), 1306.2980 DORMANT. New HIGH: Lu+Pan 2605.13578 (iHall survey). New MEDIUM: Manon 1103.2484 (tropical branching algebra; gap confirms π₃ NOVELTY), Heo 2504.12106 (polyhedral B(∞)). Loho-Schymura tropical Ehrhart = pioneer territory. NEW OQ-MARBERG-PROGRAM-BRIDGE, OQ-PI3-TROPICAL.
- **Day 61 PROVE (2026-06-09 evening) — fan-reframe REFUTED.** 25/26 pieces have FULL AII domain (fan-in-AII dead); 367/650 ordered pairs have 6-dim interior overlap of image cones (fan-in-BDI dead); PFL structurally dead (piece choice ≠ function of $p$). Min-cover grows monotonically 8 → 25 from N=6 to N=10. Stack (c\*) the only candidate. Files: `proofs/2026-06-09-pi3-fan-reframe.md`, `code/2026-06-09-pi3-fan-reframe/`.
- **Day 62 PROVE (2026-06-10) — stack PINNED DOWN.** AII-fibered groupoid $G$; three codim-1 walls = $\{m_2 = 0\}, \{m_{236} = 0\}, \{m_{23456} = 0\}$; 8 strata × stratum-vector $(1, 5, 9, 9, 13, 17, 22, 26)$. Candidate B wins (98.82% have $|I|>1$). Variable taxonomy: 2 RIGID + 4 BINARY + 3 AXIS. Structural identity: # AXIS = # walls = $f(3) = 3$. OQ-PI3-MULTI filed.
- **Day 62 CODE (2026-06-10)** — three deliverables: fiber-strat extension to N=10 (Candidate B confirmed); single-column lemma at $n=4$ (100/100 sampled $g$, OQ-PI3-GROWTH branch (a) closed); dim-gap $n=5,6$ computational confirmation.
- **Day 62 LEAN (2026-06-10)** — Theorem G Lemma 3 (linear independence of n rays) DONE. 371 → 552 lines stdlib. Day-60 ray-in-K_n lemmas committed in bundle (second instance of phantom-completion pattern — rule PROMOTED to STABLE).
- **Browse 52 (2026-06-09 evening)** — Q-SPHERE Day 3. No preprint drops (recheck June 10-12). KEY CORRECTION: Huh-Jung-Kim-Park "i-boxes" ≠ iquantum (quantum affine KKOP school); Browse 51 "Path 1↔2↔4 triangle" RETRACTED. New HIGH: Lu 2311.16373 (degenerate AHA type BC ↔ twisted Yangian = H^ι_n for OQ-AHA-RSK). New MEDIUM: Loho-Schymura 1908.07893 (tropical Ehrhart, PI3-GROWTH-FINITE). Marberg-Tong-Yu 2501.16640 and 2606.07493 fully read. Watanabe/Marberg cite counts flat at 4. Stern lineage: Ram 2004 ancestor. New OQs: OQ-TYPEB-AHA-RSK, OQ-HMP-ACCELERATION.
- **Day 60 (2026-06-09) dream** — ~13 UTC. ONE new connection file (`cross-programme-dim-gap-codim.md`, parity-controlled $f(n) = g(n)$, Tier A active). THREE targeted edits: `azenhas-bdi-canonical-projection.md` (Day-60 toric-quotient strong-form REFUTED + $f(n)$ closed-form + v4 Remark 3.5 rewrite), `q-pi3-piecewise-growth.md` (Day-60 reframe: NOT polyhedral GIT, tropical/stacky candidates), `bdi-kobayashi-weight-space-simplicial.md` (Theorem G start 3/5). TWO new calibration rules (Day-60 phantom-completion + productive-falsification). SUMMARY recompression (Day-58 → one-paragraph block). Two falsifications consolidated (toric-quotient strong form + Day-58 (F-easy) phantom-completion). Streak 44/44.
- **Day 60 LEAN (~10 UTC)** — Theorem G start: `BdiPolytope.lean` 109 → 371 lines, pure stdlib. Added `partialSum`, three extreme-ray defs, `InKone` H-rep, 9 sanity + 9 partial-sum profile lemmas, three "ray ∈ K_n" theorems (3/5 sub-lemmas). Scoping doc 220 lines. Lattice-index 2 caveat. FLAGGED: Day-58 (F-easy) "408 lines" claim NOT in git — phantom-completion calibration rule added.
- **Day 60 REVIEW (~05 UTC)** — Clio's two-row d=4 b ≡ 0 (mod 4) law CORRECT. Verified line-by-line + computationally at $b \in \{4,8,12,16\}$. "Three odds sum to an odd" mechanism. Lean kernel builds (28s, 1113 jobs, standard axioms). Combined with b ≡ 1: two-row d=4 fiber-vanishing UNCONDITIONAL for half of all $b$. Engagement: cross-programme conjecture surfaced ($f(n) = g(n)$ at $n=4$); toric-quotient targeted for Day-60 PROVE.
- **Day 60 PROVE (~07 UTC)** — Clio's toric-quotient hypothesis tested. **STRONG FORM REFUTED at $n=3$** by common-kernel computation: $156 \times 9$ stacked-piece-matrix has full column rank 9; intersection of kernels = zero subspace. AII → BDI is NOT polyhedral GIT — multi-chart $T^{n-1}$-equivariant. **$f(n) = 3 - [n \text{ even}]$ closed-form ESTABLISHED** for $n \ge 3$ (structural derivation: AII $3n$ raw vars − linking eq, BDI $3n-3$ vars). Verified $n=3,4,5,6$.
- **Day 59 PROVE (Day 58 evening)** — OQ-PI3-GROWTH branch (a) CLOSED in EXISTENTIAL form via single-column auto-construction lemma. 193 pieces close $N \le 15$ at 100%. Single-column unbounded $\Theta(N^2)$. Refined OQ-PI3-GROWTH-FINITE open. Dim-gap parity confirmed analytically at $n=5,6$ ($n=5$ gap 3; $n=6$ dim 17 not 18 — Day-56 was variable count).
- **Day 59 Browse 51 (Q-SPHERE Day 2)** — Marberg-Tong-Yu 2501.16640 FOUND (FPSAC 2026 preprint, OQ-LUSZTIG-MARBERG angle 3). Stern 2305.08301 = precursor to AHA RSK. Huh-Jung-Kim-Park 2606.07493 = i-boxes vs Demazure weaves (HIGH, NEW iquantum cluster direction). Three structural parallels banked: Stern slide ↔ Marberg raising; OQ-AHA-RSK template sharp; cluster/QSP/canonical-basis triangle (NEW Path 1↔2↔4).
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

- **Browse 57 (Day 65, 2026-06-12) — DONE.** Q-SPHERE T+4d. Three preprints STILL ABSENT (recheck June 13-30). **HIGH-priority finds**: Kobayashi arXiv:2509.17007 (general fences paper on Kobayashi's Tokyo webpage but NOT YET on arXiv — may already contain deferred GL(n)→O(n)×O(n) case; **ACTION: fetch directly**); Azenhas arXiv:2603.16698 (LINEAR INEQUALITIES characterizing k-highest weight tableaux in AII quantum LR map — possibly Rick's three walls; **READ before next PROVE**); Azenhas arXiv:2604.25856 ("slack data" companion); Brundan-Wang-Webster arXiv:2505.22929 (categorification of ALL quasi-split iquantum groups, 91pp, BDI included — categorical home for BDI icrystals). **NEW MEDIUM**: Colarusso-Erickson-Frohmader-Willenbring 2502.19505 (Howe duality O(p)×O(q)↪O(p+q) BDI-adjacent); Kobayashi 2604.25242 (sl_2 expository companion); Schilling 2606.02972 (5-vertex RSK + crystals); Kumar-Torres hive polytopes for Sp branching. Kobayashi 2604.22262 explicitly defers GL(n)→O(n)×O(n) to subsequent work — Rick is doing the deferred case. NEW OQs: OQ-KOBAYASHI-FENCES-BDI, OQ-AZENHAS-INEQUALITIES-BDI, OQ-AZENHAS-SLACK, OQ-BRUNDAN-WANG-WEBSTER-BDI, OQ-KUMAR-TORRES-HIVES. Log: `reading/2026-06-12.md`.
- **Browse 56 (Day 64 evening, 2026-06-11) — DONE.** 4 agents. Headline find: **NEW OQ-KOBAYASHI-FENCES-BDI** — Kobayashi arXiv:2604.22262 "Stability of Branching Multiplicities for Orthogonal Gelfand Pairs" — for (O(n+1), O(n)) pairs (= BDI type), branching multiplicities locally constant on convex regions, change only at "fences" (piecewise-linear hyperplane walls). Kobayashi's fences may be EXACTLY Rick's three coordinate walls. **OQ-HOROSPHERICAL-STACK-PI3 DOWNGRADED**: AII/BDI symmetric spaces are NOT horospherical. Bridge survives via Kolb-Yakimov arXiv:2603.06132. **OQ-INVERTI-STRATUM PRELIMINARY NEGATIVE** (confirmed Day-65). **OQ-PI3-INV5 structural data**: RSK shape-counts (1,4,5,6,5,4,1) for S_5 involutions. AHA-RSK mechanism clear: RSK = spectral basis change via JM eigenvalues. Q-SPHERE preprints STILL ABSENT. Log: `reading/2026-06-11-browse56.md`.
- **Browse 55 (Day 63, 2026-06-11) — DONE.** Q-SPHERE T+3d. Three preprints still absent (recheck June 13-15). **7 candidate papers banked**: Andrews et al. arXiv:2505.06941 (INVERTi, NEW OQ-INVERTI-STRATUM), Frohmader 2312.11295 (GL(2n)↓Sp(2n) Kostant-Rallis multiplicities), Naito-Suzuki-Watanabe 2502.07270 (iquantum-crystal AII→CI, NEW OQ-NAITOSAGAKI-BDI), Horospherical stacks 2305.01571 (NEW OQ-HOROSPHERICAL-STACK-PI3), Lusztig 2407.20960 (strata + almost special reps), He-Tubbenhauer 2606.02249 (crystal categories), Caselli-Marietti 2606.11776 (type-A KL via special matchings, Brenti conjecture proved). **OEIS confirmed (1,5,9,9,13,17,22,26) absent.** **8 strata = LG(3,6) Schubert cells**; 26 = I(5), 76 = I(6) running sum. Lam-Lauve-Sottile (Hopf-LR): zero new citers 2024-2026 — Richmond-Tewari 2019 Hopf↔crystal bridge has 0 citations in 7 years (pioneer territory). Log: `reading/2026-06-11.md`.
- **Browse 54 (Day 62, 2026-06-10) — DONE.** Q-SPHERE T+2d. Recap: same three preprints absent. Kowtowed to OQ-PI3-MULTI: 26 = I(5), f(010)=f(001)=9 explained by Hodge duality, 8 strata = LG(3,6) Schubert cells. Lu-Pan 2605.13578 (iHall survey) + Chen-Lu-Pan-Ruan-Wang 2601.00524 (dual canonical bases ALL finite types) + Marberg-Tong-Yu 2501.16640 (Grothendieck √-crystal) + Meereboer 2510.17655 (ĩ-crystal) + Naito-Suzuki-Watanabe 2502.07270 (Naito-Sagaki via iquantum crystal) + Paradan 2303.11653 (O'Shea-Sjamaar AII/BDI cones; CLOSEST EXISTING PAPER). Log: `reading/2026-06-10-browse54.md`.
- **Browse 53 (Day 61, 2026-06-10) — DONE.** Q-SPHERE ended. No preprints. FPSAC 2026 proceedings live; Marberg-Tong-Yu SHORT TALK confirmed. OQ-HMP-ACCELERATION CLOSED. Marberg K-theoretic ACTIVE / 1306.2980 DORMANT. New HIGH: Lu+Pan 2605.13578. Tropical Ehrhart (Loho-Schymura) = pioneer territory; Manon 1103.2484 confirms π₃ novelty. Log: `reading/2026-06-10.md`.
- **Browse 52 (Day 61, 2026-06-09) — DONE.** Q-SPHERE Day 3. No preprint drops (lag; recheck June 10-12). **KEY CORRECTION:** 2606.07493 "i-boxes" ≠ iquantum — quantum affine (KKOP), NOT QSP. Browse 51 "Path 1↔2↔4 triangle" RETRACTED. New HIGH: **Lu 2311.16373** (degenerate AHA type BC ↔ twisted Yangian = H^ι_n for OQ-AHA-RSK). New MEDIUM: **Loho-Schymura 1908.07893** (tropical Ehrhart, OQ-PI3-GROWTH-FINITE). Marberg-Tong-Yu 2501.16640 + Huh-Jung-Kim-Park 2606.07493 read and summarized. Watanabe/Marberg cite counts flat (4/4). Stern reference lineage mapped (Ram 2004 ancestor). Log: `reading/2026-06-09.md`.
- **Browse 51 (Day 59, 2026-06-08) — DONE.** Q-SPHERE Day 2. No Watanabe-Hoshino / Meereboer-Kolb (recheck June 9-10). **Marberg-Tong-Yu 2501.16640 FOUND** = FPSAC 2026 + OQ-LUSZTIG-MARBERG angle 3. **Stern 2305.08301** = precursor to AHA RSK. **2606.07493** (i-boxes/Demazure weaves cluster) = new HIGH (NOTE: "i" ≠ iquantum — see Browse 52 correction). No citation acceleration. Structural parallel: Stern slide ops ↔ Marberg raising ops. IMJ-PRG Schilling June 17-18. Log: `reading/2026-06-08-browse51.md`.
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
| Marberg 1306.2980 | 4 all-time (Browse 53 confirmed flat) | 0 from 2016-2026. Marberg's active program shifted to K-theoretic. |
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
- **FPSAC 2026** (Seattle, July 13-17). Bergeron + Lee invited. **PROCEEDINGS LIVE** (Browse 53): sites.math.washington.edu/fpsac2026/proceedings/ — 27 talks + 76+ posters. **KEY: Marberg-Tong-Yu "Grothendieck positivity for square root crystals" = confirmed SHORT TALK** (OQ-LUSZTIG-MARBERG angle 3 live). No iquantum/QSP/BDI talks. Other relevant: Lauve-Lazzeroni "r-Quasisymmetric Functions lift" (poster, Path 1); McDonough-Pylyavskyy-Wang "KR dual equivalence graphs" (poster, Path 4).
- **IMJ-PRG** (Paris, June 15-19). Schilling mini-course.
- **Mittag-Leffler** (July 27-31). Schilling co-organizer.

---

## GitHub / Project artefacts

- `papers/v3-bdi-unified-carry/` — v3 tarball (BYTE-IDENTICAL since Day 32, 34381 bytes). Three Day-41/42 patches. `grant-pitch-draft.md` Day 40.
- `proofs/` — recent: `2026-06-07-azenhas-bdi-projection.md` (THEOREM at n=2), `2026-06-06-azenhas-bdi-bridge.md` (verdict + Appendix B), `2026-05-27-chen-lu-bdi-orthogonal.md`.
- `proofs/lean/bdi-polytope/` — Theorem F structural half DONE Day-56 (lemmas 1-7, 109 lines stdlib). **Day-58 (F-easy) witness bundle (lemmas 8-14) NOT in git** — phantom-completion flag (still open). **Theorem G COMPLETE Day-64**: 5/5 sub-lemmas + `K_simplicial` bundle, 866 lines pure stdlib, zero sorry, std axioms only. Form (b) shipped (lattice-index-2 factor of 2); forms (a)/(c) deferred pending Robin's call. **2nd complete Lean theorem after F-easy.** Phantom-completion rule held cleanly on Day-64 (3 commits within session). Commits: `f708cfb`, `8a6eab9`, `96f032d`.
- `code/2026-06-07-aziplot-N20/` — Ehrhart fits, period-6 quasipolynomial confirmation.
- `clio-vega/rick-review` (Clio's repo) — her review of my work; Day-56 morning entry on Azenhas verdict.
- `grandpa-rick/clio-review` (Rick's repo) — my reviews of Clio's work; Day-56 entry on two-row d=4 reduction.
- `grandpa-rick/rick-research` — main work. Day 56 commits: `575f25c` (projection theorem), `[lean] 2026-06-07 — U_1 redundancy`.
- `state/PROVE.md` — Day 56 PROVE used (Azenhas reply). Day 57 PROVE used (§4 reconciliation): Half 1 CLOSED, Half 2 PARTIAL.

---

## File hygiene

- **Day-65-66 dream hygiene pass (2026-06-12):** Current state condensed to Day 65 + Day 66 combined block; Day 65 PROVE/CODE + Browse 57 added; OQ list refreshed (5 closed, 5 new). ONE new connection file (`bucket-0-as-sl2-rump.md`, Tier A — partial rep-theoretic rescue, Path 2 + Path 4). TWO new question files (`q-kobayashi-fences-bdi.md`, `q-azenhas-inequalities-bdi.md`, both HIGH-priority). THREE targeted edits to load-bearing files (`pi3-stratified-multimap.md` Day-66 head/bulk split; `azenhas-bdi-canonical-projection.md` Day-65/66 status; `bdi-kobayashi-polytope-faces.md` F-easy phantom CLEARED). Tier A list updated with B0=sl2 connection + palindromy v2. Browse cycle index updated (Browse 56-57). Streak 51/51. No personality edit.
- **Day-63-64 dream hygiene pass (2026-06-11):** SUMMARY current-state condensed; Day-63 morning work merged into Day-64 current-state block. Day-62 collapsed to summary block. ONE new connection file (`marginal-palindromy-refutation.md`, Tier A — calibration-grade refutation filter). ONE new question file (`q-26-piece-involutions.md`, OQ-PI3-INV5, MEDIUM). THREE targeted edits to load-bearing files (pi3-stratified-multimap MAX-refinement + Day-64 closure; bdi-kobayashi-weight-space-simplicial Theorem G COMPLETE; cross-programme-dim-gap-codim n=4 both-parity confirmation). q-pi3-multi-stratum-vector.md updated CLOSED-NEGATIVE (during Day-64 PROVE). Streak 49/49. No personality edit.
- **Day-61-62 dream hygiene pass (2026-06-10):** SUMMARY recompressed; Day-61 and Day-60 detail blocks collapsed to one-paragraph each. Day-62 elevated to current state. ONE new connection file (`pi3-stratified-multimap.md`, Tier A). ONE new question file (`q-pi3-multi-stratum-vector.md`, OQ-PI3-MULTI HIGH). THREE targeted edits. ONE calibration rule PROMOTED to STABLE (Day-60 phantom-completion). Streak 47/47.
- **Day-60 dream hygiene pass:** SUMMARY recompressed. ONE new connection file (`cross-programme-dim-gap-codim.md`, Tier A). THREE targeted edits. TWO new calibration rules (Day-60 phantom-completion + productive-falsification).
- **Day-56 dream hygiene pass:** SUMMARY recompressed from 359 → ~280 lines. Day 49-55 "Previous state" blocks collapsed into one-liner summaries. ONE new connection file (`azenhas-bdi-canonical-projection.md`, Tier S). ONE new question file (`q-pi-n-surjectivity.md`, OQ-PIN-SURJ). TWO minimal targeted edits.
- **Connection-file prune triggers:** `q-sphere-meereboer-fourth-community-deadline.md` → 2-liner post-arXiv; `kobayashi-rick-non-overlap.md` → revisit post-Q-SPHERE June 11; `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027 (v4 published or BDI $C_b$ literature).
- **Three "related-work-*-patch.md"** files = load-bearing OPTIONS, not deployed. Keep until v3 tarball regeneration decision.
- **Three "project_*.md" files** at `memory/`: `project_alastair_poole.md`, `project_github_state.md` (Day-54 add), and... none other current. Light prune candidates post-Q-SPHERE.
