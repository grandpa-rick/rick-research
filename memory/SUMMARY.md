# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active (Day 55+). CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel operational (Day 55-56: `grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred since Day-24.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted since Day 32. Thread paused per Day-46-superseded rule.

---

## Current state — Day 62 (2026-06-10 deep-work, stack pinned down)

**Day 62 PROVE (deep work): pinned down the (c*) stack from the 26-piece data.**
$\tilde\pi_3'$ is now a concrete combinatorial object — the AII-fibered groupoid
$G$ of (p, valid-piece) pairs, modulo 2-morphisms identifying same-image pieces.

- **Verdict: Candidate B (genuine multivaluedness) wins decisively.** 98.82% of
  AII lattice points at N=8 have $|I(p)| > 1$; 9.92% have $|I(p)| = 26$ (all
  pieces give different BDI images).
- **Only ONE piece — `M2_is_m236` — ever fails feasibility**, exactly on the
  half-space $\{m_{236} > 2 m_2 + 2 m_{2345}\}$. Other 25 pieces have full AII
  domain. So $|V(p)| \in \{25, 26\}$.
- **Kernel arrangement has only THREE codim-1 walls inside the AII cone**:
  $\{m_2 = 0\}, \{m_{236} = 0\}, \{m_{23456} = 0\}$. 8 strata, $|I(p)|$
  essentially constant per stratum: pattern $(1, 5, 9, 9, 13, 17, 22, 26)$
  on $\sigma = (000, 100, 010, 001, 101, 110, 011, 111)$.
- **Three "axis" variables** $(m_2, m_{236}, m_{23456})$ are exactly the AII
  variables with MULTIPLE distinct columns across pieces (4, 10, 9). The
  remaining 6 AII variables are either RIGID (m_23, m_12346) or BINARY
  (m_12356, m_2345, m_1235, m_1234).
- **Explicit wall point**: $p_b = e_{m_{236}} + e_{m_{23456}}$ has $|V|=25$,
  $|I|=21$. Crossing wall $\{m_{236}=0\}$ from neighbour $p_a = e_{m_{23456}}$
  ($|V|=26$, $|I|=9$): jump $9 \to 21$.

**Next testable question (`OQ-PI3-MULTI`)**: Is the stratum-vector
$(1, 5, 9, 9, 13, 17, 22, 26)$ a representation-theoretic multiplicity sequence?
Need to push to $N \ge 12$ to verify per-stratum constancy is exact.

Files: `proofs/2026-06-10-pi3-stack-structure.md`,
`code/2026-06-10-stack-structure/` (fiber_strat.py, probe_structure.py,
kernel_arrangement.py, debug_walls.py, strata.py, rigid_vars.py).

---

## Previous state — Day 61 (2026-06-09 deep-work, fan-reframe REFUTED)

**Day 61 PROVE (deep work): fan-reframe of $\tilde\pi_3'$ — BOTH candidate fan
locations REFUTED at finite level.** Tropical fan (b*) and PFL (a*) both dead;
stack (c*) remains.

- **Fan-in-AII REFUTED.** Pulled BDI inequalities back through each of the
  26 piece matrices; Farkas-LP tested AII-redundancy. **25/26 pieces have
  FULL AII DOMAIN** — only `M2_is_m236` has a nontrivial wall
  ($2 m_2 - m_{236} + 2 m_{2345} \ge 0$). Piece-domains coincide, not partition.
- **Fan-in-BDI REFUTED.** Computed image cones $C_i = \pi^{(i)}(\mathsf{P}^{AII}_5)$;
  all 6-dim proper subcones of $\mathsf{P}^{BDI}_3$. **367 of 650 ordered
  pairs (56%) have 6-dim interior overlap**, 149 mutual. Image cones overlap
  in interior, fail fan condition.
- **Min-cover grows monotonically with $N$**: 8 (N=6), 12 (N=7), 14 (N=8),
  23 (N=9), 25 (N=10). Combined with Day-60's $\Theta(N^2)$ growth at $N\ge16$,
  the cover is **unbounded**. 26 is just where $N=10$ lands — not a structural constant.
- **PFL structurally ruled out.** Different pieces give VALID linear maps at
  the SAME $p$ with DIFFERENT $q$. The "absorption channel" choice is NOT a
  function of $p$. A piecewise function can't model it, PFL or otherwise.
  Multivaluedness is fundamental.
- **Stack (c*) is the only candidate left.** Pieces are 1-morphisms, not
  functions; absorption labels are objects; the structure is 2-categorical.
  Possible soft form: parametrised tropical-fan family $\{A(p)\}_p$ where
  $A(p)$ = absorption polytope at $p$. (Conjectural, not proved.)

Files: `proofs/2026-06-09-pi3-fan-reframe.md`,
`code/2026-06-09-pi3-fan-reframe/` (wall_catalog.py, fan_test.py,
pairwise_fan.py, essential_pieces.py, minimal_cover_recompute.py),
`memory/for-collaborator/2026-06-09-pi3-fan-reframe-refuted.md`.

---

## Day 61 BROWSE — same date (2026-06-09 evening, Q-SPHERE T+2d, Browse 52 done)

**Browse 52 done.** No Q-SPHERE preprint drops (lag expected; recheck June 10-12). **KEY CORRECTION:**
Huh-Jung-Kim-Park 2606.07493 "i-boxes" ≠ iquantum — "i" = index interval in braid word; paper is quantum
affine (KKOP), NOT iquantum symmetric pairs. **Browse 51 "cluster/QSP/canonical-basis triangle (Path 1↔2↔4
NEW)" is RETRACTED.** New HIGH finds: Lu arXiv:2311.16373 (degenerate AHA type BC ↔ twisted Yangian =
H^ι_n candidate for OQ-AHA-RSK), Loho-Schymura 1908.07893 (tropical Ehrhart theory, OQ-PI3-GROWTH-FINITE
framework candidate), Fu 2606.08937 (quantum current algebra canonical bases, June 8). Citation counts flat
(Watanabe 4, Marberg 4). Stern AHA-RSK reference lineage confirmed: Ram 2004 "Skew shape reps irreducible"
(41 cit) is the direct ancestor. New OQ: Hamaker-Marberg-Pawlowski 2015 (46 cit) reverse-citation check
flagged for Browse 53. Added P_PARK: Lu 2311.16373, 2408.06981, Loho-Schymura 1908.07893.

---

## Previous state — Day 60 (2026-06-09, Q-SPHERE T+2d, the toric-quotient-NOT-GIT day)

**Day 60 PROVE: Clio's toric-quotient hypothesis — strong-form REFUTED at $n=3$;
$f(n)$ closed form ESTABLISHED.** AII → BDI is **NOT polyhedral GIT**.

- **VACUOUSLY TRUE in BDI itself.** $P_2 - P_1 - 2(B_2 - T_2) = 0$ is
  the definition of $P_2$. BDI factors as core BDI $\times \mathbb{N}^{n-1}$
  with $(T_1,\ldots,T_{n-1})$ as fiber coords — genuine intrinsic torus
  structure on BDI.
- **STRONG-FORM REFUTED at $n=3$.** Stack of 26 piece matrices is
  $156 \times 9$ with full column rank 9. Intersection of kernels
  across 26 pieces = zero subspace. No universal AII direction invariant
  under all pieces ⇒ no global $T^{n-1}$-quotient AII / $T^{n-1}$ ≅ BDI.
- **DIFFERENT pieces give DIFFERENT cores**: 16 distinct
  $(M_2, P_1, P_2, S)$ projections, 4 distinct $T_1$ expressions, 5
  distinct $T_2$ expressions across the 26 pieces. The 26-piece
  structure is FUNDAMENTAL, not a polyhedral artifact.
- **REFRAME:** AII → BDI is multi-chart $T^{n-1}$-equivariant
  (analogous to toric variety covered by multiple charts), NOT GIT
  quotient. Routes OQ-PI3-GROWTH OUT of polyhedral category into
  Path 2/3 (tropical / stacky / quantum-branching).

**$f(n)$ ESTABLISHED** (Day-60 secondary):
$$\boxed{f(n) := \dim \mathsf{P}^{\mathrm{AII}}_{2n-1} - \dim
\mathsf{P}^{\mathrm{BDI}}_n = 3 - [n \text{ even}] \quad (n \ge 3).}$$
Structural derivation: AII has $3n$ raw vars minus $[n \text{ even}]$
linking eq; BDI has $3n - 3$ vars. Verified analytically $n=3,4,5,6$.

Files: `proofs/2026-06-10-toric-quotient-hypothesis.md`,
`code/2026-06-10-toric-quotient/`,
`memory/for-collaborator/2026-06-10-toric-quotient-refuted-partial.md`.

**Day 60 LEAN: Theorem G start, 3/5 sub-lemmas DONE.**
`BdiPolytope.lean` 109 → 371 lines, pure stdlib. Added `partialSum`,
extreme-ray defs (`pairRay`, `sumRay`, `eRay`), `InKone` H-rep
predicate, 9 sanity-eval + 9 partial-sum profile lemmas, and the three
"each ray ∈ K_n" theorems. Scoping doc `TheoremG-scoping.md` (220
lines). Remaining: lemma 3 (lin-indep), lemma 4 (cone hull surj, HARD),
lemma 5 (uniqueness), bundle. ETA 4 LEAN sessions. Lattice-index 2
caveat → Robin's call on statement form. **FLAGGED**: Day-58 (F-easy)
"408-line formalization" is NOT in git — phantom completion. New
calibration rule below. Note:
`memory/for-collaborator/2026-06-10-bdi-polytope-lean-day60-theoremG.md`.

**Day 60 REVIEW: Clio's two-row d=4 b ≡ 0 (mod 4) law CORRECT.**
Theorem 1 (V) verified line-by-line + computationally at $b \in
\{4,8,12,16\}$, $m$ up to $100003$. "Three odds sum to an odd"
mechanism rescues parity-counting closure. Lean kernel builds (28s,
1113 jobs, standard axioms). **Combined: two-row d=4 fiber-vanishing
law unconditional for $b \equiv 0, 1 \pmod 4$** (half of all $b$).
Engagement: accepted Clio's strengthening of Ehrhart claim
($\Delta_p^{d+1} = 0$ *proves* not *verifies*); downgraded $\{0,1,2\}$-
coeff sketch to "heuristic"; agreed toric-quotient was right PROVE
target. File: `reviews/2026-06-10-clio-d4-tworow-full-law.md`.

**Day 60 CROSS-PROGRAMME CONJECTURE surfaced (NEW connection file):**
Same forgotten-dim count both sides. Rick's $f(n)$ = 2 at $n=4$ even =
Clio's d=4 fiber-vanishing codim on imaginary axis. CONJECTURE
$f(n) = g(n) = 3 - [n \text{ even}]$ for $n \ge 3$. Parity controls
both sides (linking eq vs parity-counting closure). Testable at
$n = 3, 5, 6, 7$. See `connections/cross-programme-dim-gap-codim.md`.
If confirmed, v4 §3 cross-programme unifier.

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
- **Path 2 + Path 4:** π_n canonical projection (Day 56) — carry-$P_a$ is BDI image of AII signed-slack data; kernel is PARITY-DEPENDENT (Day-58 correction, Day-60 closed-form $f(n) = 3 - [n \text{ even}]$). Theorem at $n=2$ (linear); 193-piece auto-construction at $n=3$ (Day-59 existential close at any $N$; Day-60 NOT polyhedral GIT); multi-chart $T^{n-1}$-equivariant framework, NOT GIT quotient.
- **Path 2 + Path 4 NEW Day-60:** Cross-programme dim-gap = obstruction codim conjecture. $f(n) = g(n) = 3 - [n \text{ even}]$ at $n = d \ge 3$. Verified at $n=4$; testable at $n = 3,5,6,7$. If confirmed = v4 §3 unifier.
- **Path 2 + Path 4:** carry $P_a$ six-roles unification (Day 56). Theorems E, F, G + projection. Lean Theorem F-easy CLAIMED in Day-58 collaborator note but NOT in git (Day-60 phantom-completion flag); Theorem G 3/5 sub-lemmas in git (Day-60).
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL positivity conjectures (1306.2980) unguarded. Marberg-Tong-Yu 2501.16640 (Day-59 found) = OQ-LUSZTIG-MARBERG angle 3 entry. Long-horizon for v4+.
- **Path 1 (combinatorial Hopf):** NSym^B from H^B_*(0) still open (OQ-HUANG-B). Seed Q4 (q=0 combinatorial Hopf) externally unconstrained.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`azenhas-bdi-canonical-projection.md`** (Day 56, **Day-58 + Day-60 major updates**) — Canonical forgetful surjection $\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_n$. THEOREM at $n=2$ (verified to N=20). At $n=3$: OQ-PIN-SURJ EXISTENTIAL CLOSED Day-59 (193 pieces, $N\le 15$); **Day-60: NOT polyhedral GIT** (common-kernel = zero subspace across 26 pieces; multi-chart $T^{n-1}$-equivariant framework). **$f(n) = 3 - [n \text{ even}]$ closed-form** (Day-60). v4 Remark 3.5 REWRITTEN.
- **`cross-programme-dim-gap-codim.md`** (NEW Day-60) — Cross-programme conjecture $f(n) = g(n) = 3 - [n \text{ even}]$ at $n = d \ge 3$. Same forgotten-dim count both sides: Rick polytope side vs Clio fiber-vanishing side. Verified $n=4$. Testable. Tier A active; v4 §3 unifier if confirmed.
- **`discovery-layer-is-the-moat.md`** — Day 39 origin. AI harnesses verify; only humans+frameworks discover. Five evidence layers: empirical < community-internal < structural < mechanical < live community attack. Day-56 new instance: Clio's peer-review reframe that turned a CLOSED-NEGATIVE verdict into a PROVED-POSITIVE theorem is a discovery event no AI reading preprints would surface. Add to journal.
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles (Day 56 add). v3 structural climax. (1) descent-recording; (2) singleton cross-chain coupling → Theorem E; (3) chain-MB / carry-recursive factorization; (4) chain-side polytope completeness Theorem F ($2n-3$ facets); (5) weight-projection invariant Theorem G ($n$-facet simplicial cone); (6) image of canonical AII projection $\pi_n$, kernel parametrized by Singleton fiber.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Chain polytope $\mathbb{P}_n$ has exactly $2n-3$ non-redundant carry facets. **STATUS Day-60 PHANTOM-COMPLETION FLAG:** Day-58 collaborator note documents lemmas 1-14 fully formalised (408 lines pure stdlib), but Day-60 LEAN found the on-disk file at 109 lines (Day-56 base; last commit `fed238c`). The Day-58 witness-bundle work is NOT in git. Either container-lifecycle data loss or undocumented incompleteness. Day-60 calibration rule added. Re-derivation ~1 LEAN session.
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. Image polytope $\mathbb{K}_n^+ \subset \mathbb{R}^n$ = simplicial cone with $n$ facets. **Day-60 LEAN start: 3/5 sub-lemmas DONE.** 109 → 371 lines pure stdlib. Remaining: lin-indep (lemma 3), cone hull surj (lemma 4, HARD), uniqueness (lemma 5), bundle. ETA 4 LEAN sessions. Lattice-index 2 caveat — Robin's call on statement form.
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
- **OQ-PIN-SURJ** (Day 56 opened; Day-59 RESOLVED EXISTENTIAL form at n=3) — for each fixed $N$, $K(3, N) < \infty$ via single-column auto-construction lemma (`proofs/2026-06-09-pi3-growth-a.md`). 193-piece registry closes $N \le 15$ at 100%. Single-column construction grows $\Theta(N^2)$ as $N \to \infty$. At $n \ge 4$: not investigated.
- **OQ-PI3-GROWTH** (NEW Day 58; REFRAMED Day-60) — **Polyhedral GIT REFUTED at $n=3$** (common-kernel = zero across 26 pieces). Right framework is NOT polyhedral: candidates are (b*) piecewise-fractional-linear, (c*) tropical / non-Archimedean, (d*) stack with piece-choice as 2-categorical datum. All three are Path 2/3. Seed-deep. HIGH priority. See `questions/q-pi3-piecewise-growth.md`, `proofs/2026-06-10-toric-quotient-hypothesis.md`.
- **OQ-PI3-GROWTH-FINITE** (NEW Day-59, REFINED Day-60) — Does $\sup_N K(3, N) < \infty$ at any non-polyhedral level? NO at polyhedral-PL (single-column unbounded). Likely YES at tropical/stacky; specifics open.
- **OQ-DIMGAP-CODIM** (NEW Day-60, cross-programme) — Does $f(n) = g(n) = 3 - [n \text{ even}]$ where $g$ is Clio's d-fiber-vanishing obstruction codim? Verified $n=4$. Testable at $n = 3, 5, 6, 7$. If confirmed = v4 §3 unifier. HIGH priority. See `connections/cross-programme-dim-gap-codim.md`.
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

**Closed:** OQ-K (Day 29: F+G), OQ-BDIqLR (Day 26-28), OQ-KOB-MATCH (Day 41), OQ-CHEN-LU (Day 42), OQ-BWB / OQ-PJ (Day 18), OQ-MUNIZ-CARRY (Browse 20), OQ-FROHMADER (Day 29), OQ-KOBAYASHI-SL2 (Day 29), OQ-LAUVE-RQSYM (Day 50). **OQ-AZENHAS-BDI (P_PARK #5):** verdict CLOSED-NEGATIVE Day 55; REFRAMED to canonical-projection theorem Day 56 (proved at n=2, open at n≥3 via OQ-PIN-SURJ).

---

## Next session priorities

**P-1 — Wake-routine PROVE-check + git-state-verification check** (Day 44 rule + Day-60 phantom-completion rule).

**P0 — Robin endorsement decision STILL pending** (since Day 56). Daily email today.

**P0 — Lean indexing decision pending Robin** (Day 56+). Now also Theorem G's lattice-index 2 statement form (a/b/c) decision (Day 60). See `for-collaborator/2026-06-10-bdi-polytope-lean-day60-theoremG.md`.

**P0 — F-easy phantom-completion resolution.** Either re-derive Day-58 witness bundle (lemmas 8-14) and ship to git (~1 LEAN session given Day-58 collaborator note has the details), OR accept the flag and document F-easy as "future work" in v4. Decision needed Day 61.

**P0 — Clio outbound on cross-programme conjecture (NEW Day-60).** Email asking her to compute $g(d)$ at $d=3, 5, 6, 7$ from her fiber-vanishing setup. If she's already done it: cross-conjecture closes in one cycle. v4 §3 unifier.

**P0 — Browse 52 correction propagation.** Browse 51's "cluster/QSP/canonical-basis triangle (Path 1↔2↔4 NEW)" is RETRACTED. Huh-Jung-Kim-Park 2606.07493 is quantum affine, NOT iquantum. Any connection files referencing this Browse 51 claim should be updated.

**P1 — Day 61 PROVE.md target options:**
- **(A) OQ-DIMGAP-CODIM verification** (~30min Rick side already done; ~1d Clio side if she hasn't).
- **(B) Tropical/stacky reframe of $\tilde\pi_3'$** (speculative, ~1-2d sketch).
- **(C) Single-column lemma extension to $n=4$** (~30min, quick test).
- **(D) Read Stern 2305.08301 + 2606.00679 stack for OQ-AHA-RSK** (~1d, Path 3 deepening).

**HARD DEADLINE: Q-SPHERE opens June 8 (T-0d).** Vlaar-Appel June 8; June 9 high-density (Kolb 09:00 + Meereboer 10:15 + Watanabe 11:20 + Song-Zhang 14:00); June 11 Kobayashi; June 12 De Commer.

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

- **Day 60 — Phantom-completion check.** Before SUMMARY/journal/collaborator-note asserts "formalised," "shipped," or "completed," verify the claim against `git log --oneline <file>`. If the file's last commit doesn't reference the asserted work, downgrade to "documented; git verification pending." Day-58 (F-easy) "408 lines fully formalised" was described in detail in the collaborator note + journal + SUMMARY but the on-disk file at Day-60 start was 109 lines (Day-56 base). Either container-lifecycle data loss or undocumented incompleteness. Generic rule: **claims must be verified at the promotion layer.** Companion to Day-58 verify-before-promote-for-all-N.
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

- **Browse 53 (Day 61, 2026-06-10) — DONE.** Q-SPHERE Day 4 (conference ended). No preprint drops (Watanabe-Hoshino, Meereboer-Kolb, De Commer NTY all absent; recheck June 11-14). **FPSAC 2026 proceedings LIVE**: Marberg-Tong-Yu "Grothendieck positivity for square root crystals" = confirmed SHORT TALK. **OQ-HMP-ACCELERATION RESOLVED**: 4 new 2024-2026 HMP citers, none cite Marberg 1306.2980; KL conjectures unguarded. **Marberg program architecture**: K-theoretic ACTIVE (2512.23944 Dec 2025), 1306.2980 DORMANT. New HIGH: Lu+Pan 2605.13578 (iHall algebra survey). Loho-Schymura 1908.07893: 8 citers, no rep-theory; tropical Ehrhart for OQ-PI3-GROWTH-FINITE = pioneer territory. Manon 1103.2484: confirms Rick's π₃ is novel (toric-degeneration theory doesn't cover non-GIT case). Lu 2311.16373: 0 citations (frontier). Log: `reading/2026-06-10.md`.
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
- `proofs/lean/bdi-polytope/` — Theorem F structural half DONE Day-56 (lemmas 1-7, 109 lines stdlib, last commit `fed238c`). **Day-58 (F-easy) witness bundle (lemmas 8-14) NOT in git** — phantom-completion flag per Day-60 calibration rule. **Theorem G start Day-60: 109 → 371 lines stdlib**; 3/5 sub-lemmas DONE (rays ∈ K_n) + 220-line scoping doc. Remaining ~4 LEAN sessions.
- `code/2026-06-07-aziplot-N20/` — Ehrhart fits, period-6 quasipolynomial confirmation.
- `clio-vega/rick-review` (Clio's repo) — her review of my work; Day-56 morning entry on Azenhas verdict.
- `grandpa-rick/clio-review` (Rick's repo) — my reviews of Clio's work; Day-56 entry on two-row d=4 reduction.
- `grandpa-rick/rick-research` — main work. Day 56 commits: `575f25c` (projection theorem), `[lean] 2026-06-07 — U_1 redundancy`.
- `state/PROVE.md` — Day 56 PROVE used (Azenhas reply). Day 57 PROVE used (§4 reconciliation): Half 1 CLOSED, Half 2 PARTIAL.

---

## File hygiene

- **Day-60 dream hygiene pass:** SUMMARY recompressed from 516 → ~460 lines. Day-58 detail block collapsed to one paragraph (full detail in dream journal 2026-06-08.md). Day-56 detail collapsed earlier (Day-58 dream). Day-59 + Day-60 elevated to detail blocks. ONE new connection file (`cross-programme-dim-gap-codim.md`, Tier A active, parity-controlled $f(n) = g(n)$). THREE targeted edits: `azenhas-bdi-canonical-projection.md` (Day-60 toric-quotient REFUTED + $f(n)$ closed form + v4 Remark 3.5 rewrite), `q-pi3-piecewise-growth.md` (Day-60 reframe NOT polyhedral GIT), `bdi-kobayashi-weight-space-simplicial.md` (Theorem G start 3/5). TWO new calibration rules (Day-60 phantom-completion + productive-falsification). Day-50 rule application #44: held. Streak 44/44.
- **Day-56 dream hygiene pass:** SUMMARY recompressed from 359 → ~280 lines. Day 49-55 "Previous state" blocks collapsed into one-liner summaries. ONE new connection file (`azenhas-bdi-canonical-projection.md`, Tier S). ONE new question file (`q-pi-n-surjectivity.md`, OQ-PIN-SURJ). TWO minimal targeted edits.
- **Connection-file prune triggers:** `q-sphere-meereboer-fourth-community-deadline.md` → 2-liner post-arXiv; `kobayashi-rick-non-overlap.md` → revisit post-Q-SPHERE June 11; `lu-pan-dual-canonical-bdi-algebraic-roof.md` → revisit ~2027 (v4 published or BDI $C_b$ literature).
- **Three "related-work-*-patch.md"** files = load-bearing OPTIONS, not deployed. Keep until v3 tarball regeneration decision.
- **Three "project_*.md" files** at `memory/`: `project_alastair_poole.md`, `project_github_state.md` (Day-54 add), and... none other current. Light prune candidates post-Q-SPHERE.
