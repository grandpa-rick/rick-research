# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke.
Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**Collaborators (`ALLOWED_RECIPIENTS`):**
- **Robin Langer** (langer.robin@gmail.com) — primary. Daily email rule active. CC Clio on substantive sends.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review channel (`grandpa-rick/clio-review` ↔ `clio-vega/rick-review`).
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred.
- **Alastair Poole** (alastair.poole@strath.ac.uk) — allowlisted Day 32; thread paused.

---

## Current state — Days 69-78 + Browse 63-70 (2026-06-18 wall-clock)

**Day 78 PROVE headline: Interior 3-clique non-co-occurrence PROVED n-uniformly via additive redundancy criterion — Conjecture H3' RESOLVED.** `proofs/2026-06-18-interior-non-co-occurrence.md`.

- **Mechanism identified.** Lemma 4.1 (Image-domination via $e_S$): for any α=0 partner $\pi_0$ with $\pi_0^{p_i}=e_{B_i}$ and RIGID-L_n ($\pi_0^{l_n}=e_S$), the α=1,2 simpdiv pieces satisfy $\text{Im}(\pi_\alpha) \subseteq \text{Im}(\pi_0)$ via the single $\mathbb{Z}_{\ge 0}$-equation $e_{B_i} + \alpha e_S = 1\cdot e_{B_i} + \alpha \cdot e_S$. This is Clio's §8 "additive redundancy criterion" instantiated at the $e_S$ ray.
- **Theorem 3.5'.** No minimal cover at any $n \ge 3$ contains a literal 3-clique at interior $p_i$. Modulo Day-70 §6.1 RIGID-L_n (verified empirically: 42/42, 53/53, 66/66 pieces at $n=5,6,7$).
- **Wider observation (productive).** Same mechanism kills the LITERAL 3-clique at $p_1$ too (verified at $n=5$: the three Rdouble_lv1 pieces are literally image-equivalent). Consistent with Day-77 §6 image-equivalence-class quantification — $R\text{-AXIS}=1$ at $p_1$ lives at the canonical-rep level (Day-75 Theorem 7.2 ray-level forcing), not at literal-minimal-cover level. Day-79 flag: tighten Day-77 §2 $W_c$ definition.
- **What this closes.** Day-77 H3 (cover-redundancy of off-base simpdiv at interior $p_i$) PROVED n-uniformly. Day-77 §4.2 Step 3 "L/S-divert forcing" gap CLOSED. R-AXIS upper-bound interior case now unconditional given Day-70 §6.1.
- **Falsification streak (Days 71, 73, 74, 75, 76, 77) BROKEN BY A RESOLUTION.** Day 78 is the first "positive" outcome in 7 days. Discipline held: each prior narrowing identified the right next ingredient.

Day-78 collaborator note: `for-collaborator/2026-06-18-clio-review-response.md`.

---

**Day 77 PROVE headline: R-AXIS Theorem 1.1 REFORMULATED — H1 + H2 + H3 + image-equivalence-class, responding to Clio's review.** `proofs/2026-06-17-r-axis-uniform-day77-rewrite.md`.

- **Clio's review (2026-06-17)** flagged three load-bearing concerns in Day-75 (§3.1 D-pi uniqueness gap, §3.2 §5.2 feasibility-vs-cover conflation, §3.3 "every minimal cover" overquantification). All three CORRECT.
- **Day-77 response.** Theorem 1.1' restated with explicit hypotheses H1 (weak D-pi, verified at n=5,6), H2 (joint-cover containment, verified at n=5,6), H3 (cover-image-redundancy of off-base simpdiv at interior p_i, OPEN at n ≥ 6). §5.2 rewritten with cover-redundancy mechanism. Remark 4.1 promoted into Theorem 1.1' statement (image-equivalence-class quantification).
- **H3 isolated as the next CODE target.** Day-77 §3.3, §7.3 specify the verification: enumerate `Im(simpdiv) ⊆ Im(cover - simpdiv)` for interior i, α > 0. Reuses Day-76 `cover_joint_check.py` infrastructure.
- **Third productive falsification in the R-AXIS line** (Day 74, Day 76, Day 77): strong → narrower with explicit ambient conditions. Discipline producing genuine progress.

Day-77 collaborator note: `for-collaborator/2026-06-17-clio-response-uniformity-gap.md`.

---

**Browse 70 headline (2026-06-18):** DIII RSK structure clarified — Svyatnyy 2605.00514 deep-read: regular cell tables (with TYPE D CONDITION r_{n−1} ≥ l_n) are the Q-side of DIII RSK; P-side (D_n insertion tableau) is ABSENT from all literature. AII recording tableau conditions (R1)-(R5) extracted precisely from Azenhas 2603.16698: DIII analogues involve spinor parity + D_n depth inequality. Azenhas 2604.25856 re-read note: relevant NOW from DIII angle (previously read as "no BDI content"). Gutiérrez 2311.10659 NEW (BK involutions types B/C; type D explicitly open) — found in Kobayashi-Matsumura refs. Imamura-Mucciconi-Sasamoto-Scrimshaw 2606.17525 NEW (skew column RSK dynamics + box-ball system, June 2026). Kolb-Yakimov 2603.06132 covers ALL types uniformly including DIII — first solid DIII bar involution. nLab: DIII page, oscillating tableaux page, iquantum crystal page all ABSENT. FPSAC: zero DIII talks; Seung Jin Lee's SSOT talk gestures at gap. Mittag-Leffler (July 27-31): no schedule yet, Schilling + Scrimshaw closest. Citation audit: AII RSK cluster (Azenhas + Watanabe) has ZERO external citers; Svyatnyy's two type D papers have ZERO citations. No competition on DIII RSK. NEW OQ: OQ-GUTIERREZ-TYPE-D-BK (is Svyatnyy's BK the restriction of a full type D BK?). NEW OQ: OQ-SQUAREROOT-DIII (Marberg-Tong-Yu square root crystals vs DIII icrystal half-integer weights). Log: `reading/2026-06-18-browse70.md`.

**Browse 69 headline (2026-06-18):** AII picture COMPLETE — Azenhas 2603.16698 is the combinatorial inverse of Watanabe's AII RSK via "slack data" (reverse Schensted + explicit linear inequalities on k-highest weight tableaux). Azenhas 2601.06930 solves Lecouvey-Lenart conjecture (two AII models equivalent via flagged hives). Svyatnyy 2605.00514 NEW PAPER (sequel to zero-citation 2504.14344) — Bender-Knuth/cactus on short SSYT; Svyatnyy is active and fast. Luo-Su-Xu 2605.09589 — type D Steinberg varieties in affine iquantum (geometry arriving). Kobayashi-Matsumura 2506.06951 — SSOT as Q-symbols in type C RSK (direct DIII template). FPSAC 2026 full program: no DIII talks; Seung Jin Lee type B/C invited (Tue), Tianyi Yu square root crystals. Mittag-Leffler July 27-31. NEW OQ: OQ-AZENHAS-SLACK-DIII (what is the DIII slack statistic?), OQ-SSOT-TYPE-D (type D SSOT = Svyatnyy regular cell tables?). Watanabe-Hoshino: stop active watch (T+9d, not found).

**Browse 68 headline:** New finds: Watanabe 2509.00853 (AII RSK via iquantum, THE template for DIII program), Svyatnyy 2504.14344 (NEW — cactus on GT patterns for o_N via (O_N, so_{2n}) Howe duality; "regular cell tables" as DIII-tableaux precursor; 0 citations), Meereboer 2510.17655 covers **DIII_b** in ι-crystal theory (needs verification). Bae-Kwon 2506.05959 DEEP READ: NOT DIII directly (AI/AII), but is the template for DIII q-Howe duality. NAME CORRECTION: Stein Meereboer (not Lucas). KL breakthrough week: Barkley-Gaetz-Lam 2601.07793 proves CIC for coefficient of q → CIC holds for all intervals ≤ length 6. Meereboer-Kolb and Watanabe-Hoshino preprints still absent (T+8d post-Q-SPHERE).

**Open threads (day/browse priority):**
- **H3 verification (Day-77 isolated)**: simpdiv image-redundancy at interior p_i, n=6 → next CODE task
- PAPER REWRITE: BDI → DIII global pass → next WRITE task
- **READ (Browse 70 priority):** Gutiérrez 2311.10659 (BK involutions B/C; type D open — NEW), Azenhas 2604.25856 (re-read with DIII lens; formal slack data definition), He-Tubbenhauer 2606.02249 (crystal category presentations; type D coverage)
- **READ (carried):** Meereboer 2510.17655 (DIII_b check — OQ-MEEREBOER-DIII-B still open)
- **OQ-AZENHAS-SLACK-DIII (HIGH):** DIII analogues of (R3)-(R5) involve spinor parity + r_{n−1}≥l_n D_n coupling + D_n row dominance; entirely absent from literature
- **OQ-SSOT-TYPE-D (HIGH):** regular cell tableaux (Svyatnyy) = Q-side; type D SSOT = P-side paths in D_n crystal; both needed; neither assembled into RSK
- **OQ-GUTIERREZ-TYPE-D-BK (NEW, HIGH):** Svyatnyy's BK for short SSYT — is it the restriction of a full type D BK involution?
- **OQ-SQUAREROOT-DIII (NEW, MED):** Marberg-Tong-Yu square root crystals adjacent to DIII icrystal half-integer weight structure
- EMAIL: Robin (overdue), Clio (Day-77 response + H3-OP cross-check), Meereboer (DIII_b question)
- WATCH: Svyatnyy (paper 3, June/July), Azenhas (type D), De Commer type-B KL preprints; Watanabe-Hoshino check in 2 weeks
- EVENTS: FPSAC 2026 July 13-17 Seattle (zero DIII talks; Rick's venue = FPSAC 2027), Mittag-Leffler July 27-31 Djursholm (schedule mid-July)
- STOP WATCH: Meereboer-Kolb preprint, Watanabe-Hoshino (T+9d stop active, recheck T+21d)

**Previous headline (Day 76 + Browse 67):**

**Headline (Day 76 PROVE): Engine 2-Ray Decomposition Asymmetry — n-uniform coupling theorem proved; broader literal target FALSIFIED.** `proofs/2026-06-17-coupling-stratification.md`.

- **Theorem 8.1 (n-uniform, modulo Conj D-pi).** Tight-cap engine generator g_{s_j} ∈ T_n admits 2-ray (R_{p_j} + R_{s_j}) decomposition in a piece with base-canonical π^{s_j} iff j = 1. PROVED uniformly. The j=1 direction is constructive: the decoupled R-double π^{dRd}(2) (base + S ← l_n + 2 p_1) is BDI-feasible and yields 2-ray sum = g_{s_1}. The j ≥ 2 direction: D-pi RIGID/BINARY forces π^{p_j} to have B_j-component 1, contradicting RHS's B_j = 0.

- **Honest gap.** The literal PROVE.md target ("(s_j, p_j) couple iff j = 1 in BDI-feasible pieces") is **FALSE** at the abstract-feasibility level. Construction 6.1 exhibits a BDI-feasible piece π^C_2 at n = 5 that engineers BOTH π^{p_2} and π^{s_2}. Day-75 CODE's clean "(s_1, p_1) only" matrix is registry-bounded — π^C_2 is OUTSIDE the Day-72 augmented registry.

- **Open Q (next CODE):** image-redundancy probe for π^C_j (j ≥ 2). If redundant in registry, then Day-75 CODE result extends to "minimal-cover joint-engineering iff j = 1." If not, registry is incomplete as minimal cover.

Day-76 collaborator note: `for-collaborator/2026-06-17-coupling-stratification.md`.

**Day 76 LEAN: Lemma 7.1 (Multiplicative Redundancy) shipped.** `proofs/lean/bdi-polytope/BdiPolytope.lean` lines ~1720–2028. `IsFreeIsolated` (Boolean-indicator predicate, sidesteps the missing `DecidableEq AIIRay`), the three concrete `free_isolated_l1/s1/pn` instances by `cases r`, and `multiplicative_redundancy : Im π ⊆ Im π'` via `coniclyCombine_pointwise_congr`. Axioms ⊆ {propext, Quot.sound} — no Classical.choice, no sorry. Collaborator note: `for-collaborator/2026-06-17-multiplicative-redundancy-lean.md`.

---

**Earlier headline (Day 75 PROVE): R-AXIS(n) = 1 uniformly for n ≥ 3 is now a THEOREM** (modulo Conjecture D-pi at n ≥ 6).
`proofs/2026-06-20-r-axis-uniform-proof.md`. Two structural lemmas, both n-uniform:

- **Lemma 7.1 (Multiplicative Redundancy).** If π, π' differ only on a column c ∈ {l_1, s_1, p_n} with π^c = k π'^c, then Im(π) ⊆ Im(π'). Reason: those three columns are **free-isolated** in the AII ray structure (each appears in exactly one ray, and that ray's image equals the column itself). Verified by enumeration at n = 3, 5, 7. Consequence: Lemma B k = 2 and Lemma C k = 2 routings are image-redundant in any minimal cover, so no 3-clique at p_n or l_1.

- **Lemma 7.2 (Uniform bonus-coord forcing at p_1).** Every minimal cover C_n contains three pieces P_α with {B_1, S}-projection of P_α^{p_1} = b_α. Proof: b'_α = b_α + e_{M_2} ∈ T_n; semigroup-rigidity forces single ray-image; case analysis localises to R_{p_1} or R_{l_2}, both giving the same {B_1, S}-projection.

**The clean structural story (v4 §3 ready):** "one engine axis, two multiplicative phantoms" — p_1 hosts the genuine rep-theoretic R-double axis (V(2ω_1) = adj(sl_2)); p_n and l_1 host multiplicative phantoms collapsing to BINARY by Lemma 7.1. The asymmetry is encoded in the AII ray topology: p_1 appears in 3 rays, p_n / l_1 in 1 ray each.

Day-75 collaborator note: `for-collaborator/2026-06-20-r-axis-uniform-1-proof.md`.

---

**Earlier headline (Day 74 PROVE): R-AXIS(5) = 1 is now a THEOREM (no finite-check gap).**
`proofs/2026-06-19-r-axis-uniform-1-n5.md`. Day-73's Conjecture 6.2 in its strong form
("rest is uniquely forced") is **productively falsified** by the Day-74 finite check:
4320 F-feasible pieces satisfy pi^{p_1}=b_2, pi^{l_2}=e_{M_2}, with only ONE column
(pi^{s_2}) uniquely F-forced. **18 of them** are image-equivalent to R-double-α=2.

The CORRECT structural theorem (Day-74 Theorem 6.2):
(a) **(S2)** pi^{s_2} = e_{B_2} + e_{T_2} FORCED via F3 + tight S = P_4 = 2 cap on pi^{p_1}.
(b) **(RIGID)** pi^{p_2}, pi^{p_3}, pi^{p_4}, pi^{l_5} canonical (Day-70 §6).
(c) **(S4-ENGINE)** tight-cap point g_{s_4} = e_{B_3}+e_{B_4}+e_{T_4}+2e_S in T_5 has
    UNIQUE ray-image realisation at R_{s_4} with pi^{s_4} = e_{B_4}+e_{T_4}+2e_S (engine).
(d) **(P5-EQUIV)** point e_{B_2}+e_{T_2} forces pi^{p_5} = e_{B_2}+e_{T_2}.
(e) **(FREE)** pi^{l_1}, pi^{s_1}, pi^{s_5} have 3×2×3 = 18 image-equivalent choices.

Surprising structural insight: the pi^{s_1} "engine" of Day-69 R-double is partially
REDUNDANT with pi^{p_1}=b_2's S=2 contribution. The pi^{s_4} engine, by contrast, is
GENUINELY needed (no 2-ray decomposition reaches g_{s_4}).

n=6 sanity check confirms the bonus-coord trick + tight-cap arguments extend.
Conjecture: R-AXIS(n) = 1 uniformly for n ≥ 3.

Code: `code/2026-06-19-conjecture-6-2-verify/{finite_check.py, finite_check_v2.py, n6_sanity.py}`.
Collaborator note: `for-collaborator/2026-06-19-r-axis-uniform-1.md`.

---

**Earlier headline (Day 73 PROVE, R-AXIS RESCUE *REFUTED*): R-AXIS(5) ≤ 1, not 3.**
`proofs/2026-06-18-r-axis-n5-lower-bound.md`. Productive falsification of Day-72's
R-AXIS(n) = 3 hope. Two findings:
(1) **Bonus-coord trick at $p_1$ WORKS rigorously:** $b'_\alpha = e_{B_1} + \alpha e_S +
e_{M_2}$ has unique ray-image position $\mathcal{R}_{l_2}$ under Day-70 §6 routings,
forcing every minimal cover to contain three pieces with $\pi^{p_1} \in \{b_0, b_1, b_2\}$
and shared $\pi^{l_2} = e_{M_2}$. Modulo rest-canonicity (Conjecture 6.2, finite check):
3-clique on $\{p_1\}$ in every minimal cover.
(2) **At $p_5$ and $l_1$ the analogous trick FAILS structurally.** Lemma B $k = 2$
($\pi^{p_5} = 2 c_1$) is image-redundant in Lemma B $k = 1$; Lemma C $k = 2$
($\pi^{l_1} = 2 e_{B_1}$) is image-redundant in base. Verified computationally.
**Consequence:** Day-72's 27-piece cover IS NOT MINIMAL. Removing the two redundant
pieces gives a 25-piece minimal cover with $W = \{p_1\}$ only. Hence
**$R\text{-AXIS}(5) = 1$**, refuting Day-72's claim. Cover-restricted framing does NOT
recover uniform-3. The genuine $n$-uniform structure is the R-double engine at $p_1$ (cap
$\alpha \le 2$ = $\dim\mathrm{adj}(\mathfrak{sl}_2) - 1$); $p_5, l_1$ "3-cliques" were
multiplicative combinatorial artifacts. Collaborator note:
`for-collaborator/2026-06-18-r-axis-falsification.md`.

**Status of v4 §3 (revised after Day-73):** The headline "$\#\mathrm{AXIS}(n) = 3$
uniform" is gone at both strict (Day-71) and cover-restricted (Day-73) levels. Replace
with: $R\text{-AXIS}(n) = 1$ for all $n \ge 3$, single AXIS coord $p_1$, corresponding to
Bucket-0 $\cong \mathrm{adj}(\mathfrak{sl}_2)$. Lemma B/C "axes" $p_n, l_1$ are
multiplicative artifacts (image-redundant in cover).

**Headline (Day 72 CODE): Strict #AXIS = 2(n-1) empirically; Theorem 4.2 in Lean.**
`code/2026-06-17-{complete-registry,strict-axis,facets-n12-n13,r-axis-verify}/`
(commit `b451eab`). Augmented registry (42/53/66 distinct pieces at n=5/6/7) → strict
#AXIS = 8, 10, 12 at n=5,6,7. Pattern: $2(n-1)$, exceeding Day-71 lower bound n+1.
Coincidentally matches Browse-59's original incorrect AII heuristic but applied to a
*different object* (BDI strict piecewise). Polytope facets at n=12,13 still match closed
forms ($3n - [n \text{ even}]$ / $4n - 5$). AII rays n=8: 23 = 3n-1 ✓ (even-n Λ collapse).

**Headline (Day 72 + 74 LEAN): Theorem 4.2 Feasibility Ray-Characterisation BOTH DIRECTIONS SHIPPED.**
`proofs/lean/bdi-polytope/BdiPolytope.lean` 1418 → 1720 lines.
- Day 72 (commit `c7aa9a1`, +245 lines): three families AIICoord + 5 ray constructors AIIRay
  + `IsBdiSemigroup` typeclass + conic-form (⇐) `feasibility_ray_char` axioms ⊆ {propext,
  Quot.sound}. Lattice form `feasibility_ray_char_lattice` + axiom
  `aii_cone_generated_by_rays` (deferred Lemma 4.1).
- Day 74 (commit `122eed4`, +57 lines): conic-form (⇒) `feasibility_ray_char_forward` +
  biconditional `feasibility_ray_char_iff`. Axioms ⊆ {propext, Quot.sound} — same clean set.
  Singleton-list trick sidesteps DecidableEq on AIIRay (Prop-arg constructors).
- Outstanding: `aii_cone_generated_by_rays` axiom (Lemma 4.1, ~50-80 lines mechanical).
No sorry. No Classical.choice. Stdlib only. Note to Robin:
`for-collaborator/2026-06-19-feasibility-ray-char-forward-lean.md`.

**Headline (Day 71 PROVE, PRODUCTIVE FALSIFICATION): Conjecture D-pi REFUTED.**
`proofs/2026-06-16-conjecture-d-pi.md` (commit `b1643a0`). For every n ≥ 5 and interior
i ∈ {2, …, n−2}, π_α^(i) := base + (α copies of p_i in S row), α ∈ {0,1,2}, are BDI-feasible,
share every AII column except p_i, and have three distinct p_i-columns e_{B_i} + α e_S.
3-clique on {p_i = 0}. Verified at (n, i) ∈ {(5,2),(5,3),(6,2),(6,3),(6,4),(7,2),(7,3),(7,4),(7,5)},
all α ∈ {0,1,2}. **Day-70 §7 intuition ("no middle-i R-double engine") was WRONG** — no
engine needed; SIMPLE column-modification works, cap α ≤ 2 from S ≤ P_{n−1}(e_{B_i}) = 2
(identical to Lemma A's cap at p_1, but the cap formula has NO LEVEL DEPENDENCE).
**Day-70 Theorem 8.1 (uniform # AXIS ≤ 3 strict) is FALSIFIED**: # AXIS strict grows linearly
(Day-72 CODE: 2(n-1)). Empirical # AXIS = 3 at n ≤ 7 was based on incomplete registries.
**Rescue:** cover-restricted R-AXIS = 3 uniformly conjectured (Day 72 PROVE — see above).
Note to Robin: `for-collaborator/2026-06-16-conjecture-d-pi-REFUTED.md`.

**Headline (Day 70): # AXIS ≤ 3 SUBSTANTIALLY PROVED via Feasibility Ray-Characterisation.**
Two new tools in `proofs/2026-06-15-axis-uniform3-upper-bound.md` (commit `e40be2d`):
- **Theorem 4.2 (Feasibility Ray-Char.):** piece feasibility ⟺ finite column-level conditions F1–F4
  on the 3n AII cone rays.
- **Corollary 5.1 (Image Semigroup):** Im(π) = Z_{≥0}-semigroup generated by π's ray images.
Using these: l_n, p_{n-1}, Λ (even n) RIGID; l_j (2≤j≤n−1), s_j BINARY at most;
{p_1, p_n, l_1} AXIS with exactly 3 routings each. Interior p_i (1<i<n−1) RIGID conditional
on clean Conjecture D-pi, verified at n=5 (p_2, p_3 RIGID across all 27 feasible pieces).
**Day-69's "verified at n≤5, conjectural otherwise" UPGRADES to "proved modulo Conjecture D-pi."**
**[DAY 71 RETRACTION: the "n=5 verification" was against an INCOMPLETE registry that wasn't
a minimal cover of T_5. Conjecture D-pi is REFUTED — see Day 71 headline above.]**

**Headline (Day 69 PROVE): # AXIS ≥ 3 LOWER BOUND PROVED structurally, uniform in n.**
`proofs/2026-06-14-axis-uniform3-proof.md` (commit `3fce838`). Three explicit 3-piece families:
- **Lemma A (R-double head):** π^Rd_n(α), α ∈ {0,1,2}; cap α ≤ 2 is BDI-S-budget-sharp
  (S ≤ P_{n−1}) AND dim V(2ω_1) − 1 sharp (the two ceilings coincide — joint structural content
  of Bucket-0 = adj(sl_2)).
- **Lemma B (free-top prefix):** π^Pn_n(k), k ∈ {0,1,2}, modifies B_{n−1}, T_{n−1} symmetrically.
- **Lemma C (free-bottom long):** π^L1_n(k), k ∈ {0,1,2}, modifies B_1 only.
Each family gives 3 rank-1 piece-pair collisions on its coord wall. AXIS triple = {p_1, p_n, l_1}.

**Headline (Day 69 CODE): AII facet count CORRECTED — Browse 59 heuristic refuted.**
`code/2026-06-14-azenhas-aii-walls/` (commit `33b1a0b`). Closed forms verified at n = 3..11:
$$
\#\{\text{AII facets}\} = 3n - [n \text{ even}], \qquad
\#\{\text{BDI facets}\} = 4n - 5.
$$
Both sides Θ(n). **At even n ≥ 6, BDI has MORE facets than AII.** Browse 59's "AII ~2(n−1)"
was an undercount missing positivity walls. **The publishable contrast lives at the PIECEWISE
PROJECTION level (BDI = 3 walls = # AXIS uniformly; AII has no analogous structure built),
not at the polytope-facet level.** `connections/aii-bdi-wall-count-asymmetry.md` reframed.
Day 70 CODE confirmed at n=9, 10, 11 (commit `72b57dd`).

**Headline (Browse 66): TYPE D CRYSTAL PRECEDENTS FOUND; KOBAYASHI FENCES DEEP-READ; NAMING COLLISION ALERT.**
Kolb-Stephens deep read: DII only, NOT Rick's BDI. **NAMING COLLISION (CRITICAL):** In QSP literature "BDI" = (so(p+q), so(p)×so(q)); Rick's pair (so(2N), gl(N)) = "DIII" in some notations. Must resolve before submission. Kobayashi fences deep read: {ξ_i + δν_j = ±½}, covers (O(n+1),O(n)) only — NOT GL(n)↪SO(2n). Rick's R-AXIS=1 → single active BDI fence (simpler than Kobayashi's case). **NEW PAPERS:** Frohmader 2023 (arXiv:2312.11295, GL_n↓O_n crystals + Kostant-Rallis, 1 citation) + Watanabe 2107.00170 (AI crystal / GL_n↓SO_n tableaux, 4 cites) = two underappreciated type AI/AI crystal branching precedents; BDI analogue does not exist. **Stroppel-Wang 2026 (arXiv:2601.18709):** weight modules for QSP type (gl_4,gl_2×gl_2) — infrastructure moving toward type D. **Azenhas = hottest AII worker** (2 papers March-April 2026 mining Watanabe's AII result); BDI is open and next. Ressayre-Richmond 0909.0865: ZERO citations 2022-2026 CONFIRMED. Meereboer-Kolb preprint: still not on arXiv (7 days post-Q-SPHERE). **OQ-BISWAS CLOSED** (Biswas 2402.01436 covers SO(q)⊂SO(p) same-type, NOT GL(n)↪SO(2n)). **NEW OQ-FROHMADER-BDI (HIGH), OQ-WATANABE-AI-TABLEAU-BDI (HIGH), OQ-KOBAYASHI-LOWER-SEMICONT (MED).** FPSAC 2026 full schedule now posted — no BDI/type D talks. Q-SPHERE Book of Abstracts fetchable (Liu + Meereboer abstracts inside). Log: `reading/2026-06-16-browse66.md`.

**Headline (Browse 65): TYPE D EIGENCONE CONFIRMED OPEN; NEW QSP BRANCHING LEADS.**
Kolb-Stephens arXiv:2407.15538 (2024) = **TYPE DII QSP** for (so(2N), so(2N-1)); GT bases for U_q(so(2N)) irreps now proved via DII. **Adjacent to BDI** — can DII GT basis machinery adapt? **NEW OQ-KOLB-STEPHENS-DII (HIGH).** Kobayashi arXiv:2604.22262 "fences" for orthogonal Gelfand pairs (O(n+1),O(n)) = Rick's axis walls in disguise — **NEW OQ-KOBAYASHI-FENCES-BDI (MEDIUM-HIGH).** AII crystal branching (gl_{2n}→sp_{2n}) now proved by TWO methods (Muniz 2505.21738; Naito-Suzuki-Watanabe 2502.07270); type DIII/BDI analogue **wide open** — **NEW OQ-CRYSTAL-BRANCHING-BDI (HIGH).** Schuster 1608.06215 has **ZERO citations ever** (published 2021) — Rick's paper = first citer. Ressayre-Richmond 0909.0865 last cited 2021; zero 2022-2026. **SMILGA MO 476063 (NEW, 2024):** follow-up to MO 354519 on Pin group branching, score 16, ZERO answers — Rick should answer. **Email confirmed:** stein.meereboer@ru.nl (not s.meereboer). Meereboer-Kolb preprint NOT yet on arXiv (4 days post-Q-SPHERE). Q-SPHERE also had Liu on "very non-standard quantum so(2N)" (watch for preprint). Log: `reading/2026-06-16.md`.

**Headline (Browse 64): OQ-BELKALE-KIERS-2023 CLARIFIED + NEW OQ-RESSAYRE-FRANCONE-G/P + OQ-SCHUSTER-BDI.**
Belkale-Kiers 2306.16676 READ: addresses MULTIPLICATIVE Horn problem for G = SO(2n) (not the BDI subpair GL(n)↪SO(2n)). Still relevant background but does not directly give AXIS(n). **NEW KEY OPENING:** Ressayre-Francone 2312.02574v3 proves BK coefficients are 0 or 1 for G/B (all G uniform). Extension to G/P (BDI-relevant flag variety) is OPEN — if proved, gives AXIS(n) = #{Levi-movable pairs} with no redundancy cleanly. **NEW OQ-SCHUSTER-BDI (MEDIUM):** Schuster arXiv:1608.06215 (Transformation Groups 2021) describes subcones of Γₙ(SO(2r)) via Braley-Lee cohomology — most recent published work touching type D eigencone. Read to understand how BDI fits into Γₙ(SO(2n)). **GAP CONFIRMED AGAIN:** No paper post-Braley 2012 addresses GL(n)↪SO(2n) eigencone. Zero citers of Kiers 1909.09262 or Ressayre-Richmond 0909.0865 work on type D. **OQ-MEEREBOER-KOLB CONFIRMED WIP:** Q-SPHERE abstract retrieved — "Kostant's branching law for symmetric pairs via Watanabe's integrable modules," joint Meereboer-Kolb. Not yet on arXiv. Email Meereboer. Smilga MO 354519 (unanswered 5 years) = Rick's publication opportunity. Kobayashi 2604.22262 "fences" vocabulary matches Rick's axis walls (different pair). Log: `reading/2026-06-15-browse64.md`.

**Headline (Browse 63): NEW HIGH-PRIORITY LEADS — Belkale-Kiers 2023 + Meereboer-Kolb WIP.**
**OQ-FRANCONE-RESSAYRE-BDI CLOSED** (GL(n) ⊂ SO(2n) not spherical of minimal rank — definitively ruled out by Francone-Ressayre's classification list). **NEW OQ-BELKALE-KIERS-2023 (HIGHEST PRIORITY):** Belkale-Kiers arXiv:2306.16676 "Vertices in multiplicative eigenvalue problem for arbitrary groups" (2023) is a Belkale-Kiers collaboration treating ALL reductive groups including D_n. May contain first post-Braley type D eigencone vertices. Read ASAP. **NEW OQ-MEEREBOER-KOLB-KOSTANT-BDI (HIGH):** Meereboer-Kolb Q-SPHERE talk (June 9 2026) derives Kostant's branching law for (so(2n), gl(n)) — exactly BDI branching — using Watanabe's QSP integrable modules. Preprint "work in progress," expected summer 2026. **KIERS ALGORITHM CONFIRMED (OQ-KIERS-BDI UPGRADED):** Kiers 1909.09262 Theorems 1.5–1.8 give complete algorithm for extremal rays of C(GL(n) ↪ SO(2n)); not worked out in paper but directly applicable. Strategy: compute admissible OPS from weights of so(2n)/gl(n) for n=3, then type I/II rays. **RESSAYRE-FRANCONE 2312.02574v3 (NEW, STRUCTURAL):** All BK structure coefficients for ⊙₀ are 0 or 1 (proven uniformly). Applied to BDI: every Levi-movable pair in Ressayre-Richmond Theorem 5.1 is a distinct non-redundant inequality. AXIS(n) = #{admissible OPS Levi-movable pairs}, no cancellations. Community confirmation: MO 354519 (Smilga 2020) asks exactly for SO(n+m) → SO(n)×SO(m) branching outside stable range — unanswered for 5 years. Rick's work answers this. Zero MO awareness of Ressayre or BDI eigencone = genuinely open territory. New 2026 paper by Besson-Jeralds-Kiers (arXiv:2602.13966) on Demazure module reduction rules — check for type D. Log: `reading/2026-06-15.md`.

**Headline (Browse 61): BK type D failure = documented mechanism for BDI piecewise simplicity.**
Belkale-Kumar arXiv:0708.0398 explicitly states their eigencone intersection theorem FAILS
for SO(2n) (type D). Ressayre 0908.4557 similarly omits type D. Types A/B/C handled; type D
is the exception. **NEW OQ-RESSAYRE-RICHMOND-BDI (HIGHEST LEVERAGE):** Ressayre-Richmond
arXiv:0909.0865 ("Branching Schubert calculus and the BK product on cohomology", PAMS 2011)
is the branching BK product for general G ⊃ G̃ that avoids the isotropic Grassmannian. If
applied to G = SO(2n) ⊃ G̃ = GL(n), might give exactly 3 branching eigencone facets =
geometric proof of Rick's piecewise walls. See `questions/q-ressayre-richmond-bdi.md`.
**OQ-KALMBACH-BDI DOWNGRADED** (string polytopes, not wall counts).
Log: `reading/2026-06-14-browse61.md`.

**LEAN Day 70: Piece n hn infrastructure shipped.**
`inductive Piece n hn` with three constructors (RDouble, FreeTop, FreeBottom) parametrised by
`Fin 3`. `axisCoord`, `mult` defs; `Piece.axisCoord_in_AxisTriple` and
`Piece.three_mults_on_axisCoord` theorems. 75 lines, 4 declarations, axioms ⊆ {propext, Quot.sound},
no Classical.choice, no sorry. `BdiPolytope.lean` 1343 → 1418. Commit `6995302`.
**Lean micro-rule discovered:** `deriving DecidableEq` and `def f | pat => body` shorthand both
fail with "Pattern contains metavariables" against Prop-valued parameter `hn : 3 ≤ n`. Use
tactic mode (`by cases p with`). Lean 4.30.0 elaborator quirk.

**LEAN Day 69: AxisTriple List + cardinality bundle (`AxisTriple_card`).**
`AxisTriple n hn = [prefix[0], prefix[n-1], long[0]]`. Length=3 by `rfl`; Nodup by
`simp; intro h; omega`. Stdlib-only adaptation (List + Nodup, not Mathlib Finset). Commit `b0acd98`.

**CODE Day 69 ALSO: Muniz arXiv:2505.21738 SKIM verdict CLOSED for BDI portability.**
Symplectic-only, per-rank, no orthogonal analogue, no partial-sum structure.
`proofs/2026-06-14-muniz-sundaram-skim.md`.

---

## Research territory (per SEED.md)

Four paths: `topics/path1-combinatorial-hopf.md`, `path2-quantum-groups.md`,
`path3-hecke.md`, `path4-coproduct-crystal.md`.

**Active seed connections:**
- **Path 2 + Path 4 (main thread):** π_n canonical projection / AII-fibered groupoid framework.
  Theorem at n=2; branch (a) existential closed at n ∈ {2, ..., 17} (Day-71 CODE). Day-62 stack
  PINNED DOWN as AII-fibered groupoid. **Day-69 # AXIS ≥ 3 LOWER BOUND PROVED uniformly.**
  **Day-71: strict #AXIS upper bound DEAD (D-pi refuted; Day-72 CODE shows strict = 2(n-1)).**
  **Day-72: cover-restricted R-AXIS = 3 uniformly CONJECTURED, n=5 partial + n=6 sketch.**
- **Path 2 + Path 4 — wall-count contrast (UPDATED Day 72):** three levels. Polytope facets
  Θ(n) both sides; strict #AXIS = 2(n-1) BDI (Day-72 empirical); cover-restricted R-AXIS = 3
  uniformly conjectured (Day-72). AII has no analogous cover-restricted construction.
  Browse 61 mechanism: BK type-D failure for SO(2n) (Belkale-Kumar 0708.0398). Tier S.
- **Path 2 + Path 4 — cover-restricted R-AXIS as right invariant (NEW Day 71+72):**
  Strict criterion was over-permissive; the cover-restricted notion (R-AXIS) is uniformly 3
  conjecturally. Strict-vs-restricted distinction IS the Azenhas-vs-Rick wall-count asymmetry.
  Tier S. See `connections/cover-restricted-axis-as-right-invariant.md`.
- **Path 2 + Path 4 — Feasibility Ray-Characterisation (Day 70; LEAN SHIPPED Day 72):**
  Theorem 4.2 + Corollary 5.1 are the polytope shadow of "tensor functor preserves restriction
  iff it does so on simples" and the crystal tensor product rule's Z_{≥0}-combination structure.
  Lean form: 245 lines, axioms ⊆ {propext, Quot.sound} for conic. Tier S.
  See `connections/feasibility-ray-char-as-restriction-shadow.md`.
- **Path 2 + Path 4 — cross-programme dim-gap:** $f(n) = g(n) = 3 - [n \text{ even}]$ conjecture.
  Day-68 dropped the "# AXIS = f(n)" clause; f = g alone survives. Testable at n ∈ {3, 5, 6, 7}
  on Clio's side.
- **Path 2 + Path 4 — carry $P_a$ six-roles:** Theorems E, F, G + projection. Lean Theorem F-easy
  COMPLETE Day-66 (`b0a79b2`); Theorem G COMPLETE Day-64; Fence wrapper Day-68 (`1c42a05`);
  AxisTriple Day-69 (`b0acd98`); Piece infrastructure Day-70 (`6995302`). Total 1418 lines pure stdlib.
- **Path 3 (Hecke):** Marberg's 4 twisted-involution KL conjectures (1306.2980) unguarded.
  Long-horizon for v4+.
- **Path 1 (combinatorial Hopf):** NSym^B from $H^B_*(0)$ still open (OQ-HUANG-B).
  Seed Q4 (q=0 combinatorial Hopf) externally unconstrained; Day-70 ray-characterisation
  partial polytope-level answer.

---

## Crown-jewel connections (most → least live)

### Tier S — Seed-level / load-bearing

- **`cover-restricted-axis-as-right-invariant.md`** — UPDATED Day 73+74. **R-AXIS(n) = 1 uniformly**
  at p_1 (theorem at n=5, conjecture n ≥ 6). Five-iteration sharpening from "uniform-3 strict"
  through three productive falsifications. Cap α ≤ 2 triple-anchored. Replaces "uniform-3
  cover-restricted" as the structural headline.
- **`bucket-0-as-sl2-rump.md`** — PROMOTED to Tier S Day 73+74. After R-AXIS collapsed to 1,
  Bucket-0 ≅ adj(sl_2) is THE structural anchor. Triple-anchored cap α ≤ 2 (BDI S-budget,
  dim V(2ω_1) − 1, R-AXIS multiplicity = 1). Single rep-theoretic axis.
- **`aii-bdi-wall-count-asymmetry.md`** — UPDATED Day 72 with three-level table (polytope /
  strict #AXIS / R-AXIS). Day 73+74: R-AXIS = 1 (cleaner than 3). The structural contrast
  is "BDI has a single rep-theoretic axis; AII has none."
- **`feasibility-ray-char-as-restriction-shadow.md`** — Day-70 PROVE; LEAN SHIPPED Day 72
  (245 lines, axioms ⊆ {propext, Quot.sound} for conic form).
- **`azenhas-bdi-canonical-projection.md`** — Canonical forgetful surjection π_n. THEOREM at n=2;
  OQ-PIN-SURJ EXISTENTIAL CLOSED at n ∈ {2, ..., 14} (Day-70 CODE).
- **`pi3-stratified-multimap.md`** — (c*) stack as AII-fibered groupoid G; MAX-vector
  (3,8,11,10,19,14,23,26); variable taxonomy (2 RIGID + 4 BINARY + 3 AXIS at n=3).
  Day-69/70 # AXIS structure now uniformly proved.
- **`cross-programme-dim-gap-codim.md`** — f(n) = g(n) = 3 - [n even] conjecture; # AXIS clause
  dropped Day-68.
- **`discovery-layer-is-the-moat.md`** — Day-39. AI verifies; humans+frameworks discover.
  Day-69 wall-count correction strengthens (Azenhas hopes, Rick BUILDS piecewise structure).
- **`carry-Pa-as-unified-analytical-object.md`** — Six roles. v3 structural climax.
- **`bdi-kobayashi-polytope-faces.md`** — Theorem F. Day-66 F-easy + Day-68 Fence wrapper in Lean.
- **`bdi-kobayashi-weight-space-simplicial.md`** — Theorem G. Day-64 LEAN COMPLETE.
- **`kobayashi-rick-non-overlap.md`** — Level sets vs support facets. Complementary.
- **`open2-watanabe-2407-existence-meereboer-1dim-collapse.md`** — v3 OPEN-2 Layer 1 FREE via
  Watanabe 2407 §5.
- **`asymmetry-is-the-result-seven-instances.md`** — Crystal in EXPLOITATION mode.
- **`compression-is-content.md`** — Three asymmetric mechanisms.

### Tier A — Active

- **`engine-vs-base-canonical-degeneracy.md`** — SHARPENED Day-76. Day-74 observation became
  Day-76 Theorem 8.1 (n-uniform, mod D-pi): g_{s_j} admits a 2-ray decomp with BASE-CANONICAL
  π^{s_j} iff j = 1. Literal "in any BDI-feasible piece" form is FALSE (π^C_2 counterexample).
- **`image-equivalence-frame-as-recurring-pattern.md`** — NEW Day-76. Three productive
  falsifications (Day 74, Day 76 PROVE, Day 76 CODE) share the same recovery: strong-uniqueness
  → image-equivalence class / explicit ambient conditions. Methodological pattern.
- **`registry-vs-feasible-as-blind-spot.md`** — NEW Day-76. Day-72 registry is a design library
  (single-perturbation families); BDI-feasibility is closed under multi-coord engineering. π^C_2
  is the canonical example. Image-redundancy probe is the canonical level-shift (next CODE).
- **`marginal-palindromy-refutation.md` + `-v2.md`** (Day-64, Day-66) — Calibration-grade
  refutation filter.
- **`lu-pan-dual-canonical-bdi-algebraic-roof.md`** — Quartet of algebraic papers. Path 2 ↔ Path 4 bridge.
- **`zhang-lusztig-bridge-for-marberg.md`** — Post-v3 P_PARK #1 bridge.
- **`q-sphere-meereboer-fourth-community-deadline.md`** — Q-SPHERE June 8-12 archive.
  Watch preprints June 15-30.
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
- **OQ-FROHMADER-DIII (Browse 66 → renaming Browse 67, HIGH)** — Frohmader 2312.11295 DEEP READ: covers GL_n↓O_n + GL_{2n}↓Sp_{2n} (AI/AII). NOT DIII = GL_n↓SO_{2n}. Gap confirmed: different pair, different degree statistic (ceiling function in d(T) from Kostant-Rallis). DIII analogue = graded branching formula for GL_n↓SO_{2n}. Completely open. Sole citer: Frohmader-Heaton arXiv:2402.16198 (Kostant-Rallis → cyclic quivers). Related: Colarusso-Erickson-Frohmader-Willenbring arXiv:2502.19505 (Howe duality K_R-types).
- **NEW OQ-BAE-KWON-ORTHOSYMPLECTIC (Browse 67, MEDIUM)** — Bae-Kwon arXiv:2506.05959 (June 2026): "q-deformed Howe duality for orthosymplectic Lie superalgebras." Cites Watanabe 2107.00170 (AI crystal). Connects Watanabe's SO_n-tableau model to orthosymplectic Howe duality. Does this give a Howe-duality approach to DIII branching? What is the orthosymplectic partner in the q-deformed setting for the AI → DIII step?
- **OQ-WATANABE-AI-TABLEAU-DIII (Browse 66 → renamed Browse 67, HIGH)** — Watanabe 2107.00170 DEEP READ: covers type AI = GL_n↓SO_n (same rank, ⌊n/2⌋ target rank). NOT DIII = GL_n↓SO_{2n}. AI-tableaux with K(C_1)≤C_2 column condition; crystal operators B_i; branching via P^{AI} insertion. DIII analogue (DIII-tableaux, DIII-crystal, P^{DIII} insertion) does not exist. Rick's Feasibility Ray-Characterisation is the polytope shadow; crystal lift is open. New citer (Browse 67): Bae-Kwon arXiv:2506.05959 (June 2026, q-deformed orthosymplectic Howe duality).
- **OQ-KOBAYASHI-LOWER-SEMICONT (NEW Browse 66, MEDIUM)** — Kobayashi arXiv:2503.23749 "Lower semicontinuity of bounded property in the branching problem and sphericity of flag variety" — could give sphericity criteria for SO(2n)/GL(n). Read for BDI relevance.
- **OQ-QSP-NAMING-CONVENTION — CLOSED (Browse 67).** Rick's pair (so(2N), gl(N)) = Cartan type **DIII** (confirmed by arXiv:2309.17085 and 1407.5247). BDI = (SO_n, SO_p×SO_q) is a DIFFERENT pair. Paper must use DIII throughout; add a note mapping Rick's local "BDI" label to the standard "DIII." Kolb-Stephens' "DII" = (so(2N), so(2N-1)) is yet a third distinct pair.
- **OQ-BRUNDAN-WANG-DIII (Browse 66 → renamed Browse 67, MEDIUM, UNVERIFIED)** — Brundan-Wang-Webster 2505.22929 categorifies quasi-split iquantum groups "in all symmetric types." Abstract claim almost certainly includes DIII = (so_{2N}, gl_N) but needs direct verification in paper. Citers (2): Brundan-Savage-Webster-Shen 2508.14378 + Salmasian-Savage-Shen 2507.12328; no 2026 citers. Direct read of relevant sections needed to confirm DIII coverage. If confirmed: most important categorification infrastructure paper for Rick's quantum program.
- **OQ-KOLB-STEPHENS-DII (NEW Browse 65, HIGH)** — Kolb-Stephens 2407.15538 proves GT bases for ALL U_q(so(2N)) irreps via type DII QSP (so(2N), so(2N-1)). **DEEP READ Browse 66:** DII machinery only — Rick's pair (so(2N), gl(N)) does not appear. GT basis construction is a model for BDI. Open: BII type for complete GT story.
- **OQ-CRYSTAL-BRANCHING-BDI (NEW Browse 65, HIGH)** — AII crystal branching conjecture (gl_{2n}→sp_{2n}) proved by two methods in 2025. What is the analogous conjecture for gl_n→so(2n)? Rick's Feasibility Ray-Characterisation gives the polytope-level model; can it be lifted to a crystal statement?
- **OQ-KOBAYASHI-FENCES-BDI (NEW Browse 65, MEDIUM-HIGH)** — Kobayashi 2604.22262 proves branching multiplicities for (O(n+1),O(n)) are governed by "fences" (piecewise-linear walls, stability theorem). Rick's axis walls = fences for BDI? Can the stability theorem be proved for (SO(2n),GL(n))?
- **OQ-SMILGA-MO476063 (NEW Browse 65, HIGH)** — Smilga posted MO 476063 (July 2024, score 16, ZERO answers) about Pin group branching and so(n+m)→so(n)⊕so(m) outside stable range. Rick's BDI results may answer this. Publication-grade MO answering opportunity.
- **OQ-R-AXIS-UNIFORM (REVISED Day 74, HIGH)** — Is R-AXIS(n) = **1** uniformly at W = {p_1}?
  PROVED at n=5 (Day-74 Theorem 6.2 modulo D-pi at n=5, verified). n=6 sanity check confirms
  extension; rigorous proof conditional on D-pi at n=6 (CODE Day-75). The R-AXIS = 3 conjecture
  was refuted Day-73 by image-redundancy of Lemma B/C k=2 multiplicities. See
  `questions/q-r-axis-uniform.md` (UPDATED Day 74).
- **OQ-D-PI** (Day 70) — **REFUTED Day 71.** Interior prefix $p_i$ admits feasible 3-cliques via
  simple-divert; cap α ≤ 2 has no level dependence. CLOSED. See refutation
  `proofs/2026-06-16-conjecture-d-pi.md`.
- **OQ-STRICT-AXIS-CLOSED-FORM (NEW Day 72, MEDIUM)** — Empirically strict #AXIS = 2(n-1) at
  n=5,6,7. Conjectured closed form: 2(n-1) at every n ≥ 5. Test at n=8,9.
- **OQ-BELKALE-KIERS-2023 (Browse 63-64, CLARIFIED)** — arXiv:2306.16676 "Vertices in
  multiplicative eigenvalue problem for arbitrary groups" (Belkale-Kiers 2023). READ Browse 64.
  CLARIFICATION: addresses multiplicative Horn problem for G = SO(2n) (ambient group), NOT the
  BDI subpair GL(n)↪SO(2n). Different object. Still relevant: type D multiplicative eigencone
  vertices now known. Next: check if BDI cone embeds in SO(2n) eigencone (see OQ-SCHUSTER-BDI).
- **OQ-RESSAYRE-FRANCONE-G/P (NEW Browse 64, HIGH)** — Ressayre-Francone 2312.02574v3 proves
  BK structure coefficients 0 or 1 for G/B (all G). Extension to G/P (parabolic for GL(n) flag)
  is OPEN. If proved: AXIS(n) = #{Levi-movable pairs} cleanly. Best remaining path to Schubert proof.
- **OQ-SCHUSTER-BDI (NEW Browse 64, MEDIUM)** — Schuster arXiv:1608.06215 (Transformation Groups
  2021) describes subcones of Γₙ(SO(2r)) via Braley-Lee. Can BDI eigencone = a specific subcone
  of Γₙ(SO(2n))? Read next. Most accessible entry to Braley 2012 content.
- **OQ-MULTIPLICATIVE-BDI (NEW Browse 64, MEDIUM)** — Belkale-Kiers 2306.16676 gives
  multiplicative eigencone vertices for all G including SO(2n). Can BDI (additive) eigencone be
  extracted from SO(2n) multiplicative eigencone by restricting to a face?
- **OQ-MEEREBOER-KOLB-KOSTANT-BDI (Browse 63-64, HIGH)** — Meereboer-Kolb Q-SPHERE talk
  June 9 2026: "Kostant's branching law for quantum symmetric pairs" via Watanabe's QSP integrable
  modules. When (g, k) = (so(2n), gl(n)) this IS BDI branching. Preprint "work in progress,"
  expected summer 2026. Does their formula yield exactly 3 independent conditions? Email Meereboer.
- **OQ-RESSAYRE-RICHMOND-BDI** (Browse 61, HIGH, STRATEGY UPGRADED Browse 63) — Theorem 5.1
  applies in principle to GL(n) ↪ SO(2n). Strategy now clear: compute admissible OPS from weights
  of so(2n)/gl(n), count Levi-movable pairs. Combined with Ressayre-Francone multiplicity-one
  (arXiv:2312.02574v3), gives AXIS(n) = #{Levi-movable pairs} with no redundancy.
  See `questions/q-ressayre-richmond-bdi.md`.
- **OQ-BELKALE-KUMAR-BDI** (Browse 61, HIGH) — MECHANISM FOUND: BK 0708.0398 Theorem 2 fails
  for SO(2n). Connection file pending.
- **OQ-PIN-SURJ** — single-column auto-construction 100% at n ∈ {2, ..., 17} via Day-71 CODE.
- **OQ-PI3-GROWTH** — polyhedral GIT REFUTED (Day-60); fan + PFL REFUTED (Day-61); (c*) stack
  PINNED (Day-62). Branch (a) existential closed at n ≤ 17 (Day-71).
- **OQ-DIMGAP-CODIM** — f(n) = g(n) = 3 - [n even] (# AXIS clause dropped Day-68). Clio's g(d)
  at d ∈ {3, 5, 6, 7} still uncomputed. HIGH priority cross-programme.
- **OQ-KOBAYASHI-FENCES-BDI** (Day-65) — BDI gap REMAINS CLEAN; Kobayashi 2509.17007 covers
  U(p,q), NOT BDI; 2604.22262 deferred BDI to future work.
- **OQ-KTW-FACETS-BDI** (Browse 59) — Do KTW facets give Rick's 3 walls? Now repositioned:
  the question is about the BRANCHING KTW (= Ressayre-Richmond) for the orthogonal involution
  + type-D filter. See OQ-RESSAYRE-RICHMOND-BDI for the positive form.
- **OQ-KIERS-BDI** (Browse 62, HIGH, UPGRADED Browse 63) — Kiers arXiv:1909.09262 "Extremal rays
  of the embedded subgroup saturation cone." Read and confirmed: Theorems 1.5–1.8 give complete
  algorithm (type I rays from D(v) divisors; type II from Ind; off-face = (0, ω̂ⱼ)). GL(n) ↪ SO(2n)
  not worked out explicitly but machinery directly applies. Compute admissible OPS from weights of
  so(2n)/gl(n) for n=3 to find pattern. See `questions/q-kiers-bdi.md`.
- **OQ-BRALEY-BDI** (NEW Browse 62, HIGH) — Braley 2012 "Eigencone Problems for Odd and Even
  Orthogonal Groups" is the ONLY paper ever on type D eigencone. 7 citations; likely PhD thesis
  UNC Chapel Hill (Belkale's group). No type D eigencone work since 2012. Must track down.
- **OQ-BESSON-JERALDS-KIERS (NEW Browse 63, MEDIUM)** — arXiv:2602.13966 (2026) "Reduction rules
  for Demazure modules." Kiers-authored 2026 paper, cites Ressayre 1102.0196. Check for type D
  content given Kiers' established interest in BDI.
- **OQ-REDUCTION-RULE-BDI** (NEW Browse 62, MEDIUM) — Ressayre 1102.0196: each regular face
  of lr(G,G-hat) gives a reduction rule. AXIS = 3 → exactly 3 reduction rules for BDI
  multiplicities. Write down what these reduction rules look like explicitly.
- **OQ-AZENHAS-SLACK** (Day-65, MEDIUM) — Slack-data quantification.
- **OQ-BRUNDAN-WANG-WEBSTER-BDI** (Day-65, MEDIUM) — Does 2505.22929 produce BDI icrystal bases?
- **OQ-KUMAR-TORRES-HIVES** (Day-65, MEDIUM) — Is BDI cone a hive polytope?
- **OQ-HOROSPHERICAL-STACK-PI3** (Day-63, DORMANT) — AII/BDI not horospherical; bridge survives
  via Kolb-Yakimov but geometric connection absent.
- **OQ-LUSZTIG-MARBERG** (P_PARK #1) — Three attack angles; ~5.5d.
- **OQ-ZHANG-MARBERG**, **OQ-HUANG-B** (P_PARK #3), **OQ-LU-PAN-EXPLICIT** (P_PARK #4),
  **OQ-G-INTRINSIC** (P_PARK #2), **OQ-AHA-RSK**, **OQ-TYPEB-AHA-RSK**, **OQ-MILLS-TYPEB**,
  **OQ-GhaniDual**, **OQ-G2 (parked)**, **q-type-B-cactus** (Littelmann CLOSED, KN open),
  **q-KL-from-crystal** (spin CLOSED, non-spin 2-step required), **q-zero-CHA** (type A
  K_0/derived answered, type B NSym^B open).

**Closed:** **OQ-QSP-NAMING-CONVENTION (Browse 67)** — Rick's pair = DIII. BDI ≠ Rick's pair. Paper update queued. | OQ-K (Day 29), OQ-BDIqLR (Day 26-28), OQ-KOB-MATCH (Day 41), OQ-CHEN-LU (Day 42),
OQ-BWB / OQ-PJ (Day 18), OQ-MUNIZ-CARRY (Browse 20), OQ-FROHMADER (Day 29),
OQ-KOBAYASHI-SL2 (Day 29), OQ-LAUVE-RQSYM (Day 50), **OQ-PI3-MULTI-FINAL Gap B** (Day 64),
**Gap C** (Day 66 POSITIVE), **OQ-NAITOSAGAKI-BDI** (Day 66 NEGATIVE), **OQ-INVERTI-STRATUM**
(Day 65), **OQ-PI3-INV5** (Day 65 coincidental), **OQ-AZENHAS-BDI** (Day 55 → Day 56 reframed),
**OQ-HMP-ACCELERATION** (Browse 53), **OQ-AII-FACET-CLOSED-FORM** (Day-69), **OQ-MUNIZ-PORT** (Day-69),
**OQ-KALMBACH-BDI** (Browse 62 CONFIRMED CLOSED) — Kalmbach 2012.02883 = string polytopes /
PBW bases for G_classical → A_{n-1}. NOT branching cone wall counts. Confirmed irrelevant.
**OQ-FRANCONE-RESSAYRE-BDI** (Browse 63 CONFIRMED CLOSED) — Francone-Ressayre 2104.14187
gives complete list of spherical pairs of minimal rank; GL(n) ⊂ SO(2n) does NOT appear. Route
definitively ruled out. (Closest item on the list: (SL_{2n}, Sp_{2n}) = AII, not BDI.)
**OQ-D-PI** (Day 71 REFUTED) — interior prefix p_i admits feasible 3-cliques via simple-divert;
cap α ≤ 2 has no level dependence. Reduced to cover-restricted R-AXIS rescue (Day 72 PROVE).
**OQ-BISWAS-SO-RANKS** (Browse 66 CLOSED) — Biswas 2402.01436 covers SO(q)⊂SO(p) same-type all-rank, NOT GL(n)↪SO(2n). Different object entirely.

---

## Next session priorities

**P-1 — Wake-routine PROVE-check + git-state-verification check** (Day-44 + Day-60 phantom-completion rules STABLE).

**P0 — Robin email (OVERDUE, daily rule).** Two for-collaborator notes ready to summarize:
D-pi refutation + R-AXIS program. CC Clio on rep-theoretic vs image-engineered distinction.

**P0 — v4 §3 paragraph REWRITE — THIRD PASS (UPDATED Day-72).** Replace any "uniform-3 strict"
claim with three-level structure: (i) AII and BDI polytope facets both Θ(n), (ii) **strict #AXIS
for BDI = 2(n-1)** empirical Day-72 CODE, (iii) **cover-restricted R-AXIS = 3 uniformly**
conjectured Day-72 (n=5 partial + n=6 sketch), (iv) AII has no analogous cover-restricted
construction, (v) BK-type-D-failure mechanism (Belkale-Kumar 0708.0398) anchors geometric
reason. ~1 day.

**P0 — Robin endorsement + Lean form (a)/(c) call** still pending. Day-72 upgraded narrative
(cover-restricted) should land before tarball regeneration.

**P0 — Clio outbound** on Day-69 # AXIS lower bound + Day-72 R-AXIS sharpening + Day-71
engine-vs-simple R-double distinction (rep-theoretic ↔ image-engineered).

**P0 — Email Meereboer (Browse 64 ACTION):** s.meereboer@math.ru.nl — ask: (1) does Kostant
branching for (so(2n), gl(n)) yield exactly 3 independent conditions on highest weights, (2) can
they share a preprint draft. CC Kolb (s.kolb@ncl.ac.uk). Do in WAKE session.

**P0 — Email Meereboer (CORRECTED ADDRESS: stein.meereboer@ru.nl):** Ask (1) does Kostant branching for (so(2n),gl(n)) yield exactly **1** (REVISED from 3) rep-theoretic independent condition, (2) share draft. CC Kolb (s.kolb@ncl.ac.uk). T+7d post-Q-SPHERE — preprint not on arXiv.

**P0 — Resolve QSP naming convention (Browse 66 ACTION):** In QSP literature "BDI" = (so(p+q), so(p)×so(q)) ≠ Rick's pair (so(2N), gl(N)). Rick's pair may be "DIII" in that community. Verify before paper submission to avoid confusion with QSP readers.

**P1 — Read Kolb-Stephens 2024 (DONE Browse 66 deep read):** DII only — NOT Rick's BDI. GT basis via multiplicity-free DII chain. Naming collision alert (see above). Model for BDI but different pair.

**P1 — Read Kobayashi 2604.22262 (DONE Browse 66 deep read):** Fences = {ξ_i + δν_j = ±½}, (O(n+1),O(n)) only. BDI absent. R-AXIS=1 → single BDI fence. Read 2604.25242 (sl_2 expository, 38pp) for accessible framework entry.

**P1 — Read Frohmader arXiv:2312.11295 (NEW Browse 66, HIGH):** GL_n↓O_n branching via crystals + Kostant-Rallis. Closest existing paper to OQ-CRYSTAL-BRANCHING-BDI. 1 citation. Read to find the gap to BDI.

**P1 — Read Watanabe 2107.00170 (NEW Browse 66, HIGH):** AI crystal / GL_n↓SO_n tableaux. 4 citations. What's the gap to GL(n)↓SO(2n)? The BDI analogue does not exist.

**P1 — Draft MO answer for question 476063 (NEW Browse 65, HIGH):** Smilga's 2024 Pin group branching question. Zero answers. Rick's piecewise framework may answer the type D branching with spinor distinction.

**P1 — Read Schuster arXiv:1608.06215 (Browse 64, MEDIUM, ~45 min):** "Maximal rank subgroups and
strong functoriality of the additive eigencone" (Transformation Groups 2021). Describes subcones of
Γₙ(SO(2r)) via Braley-Lee cohomology — most accessible entry into Braley 2012 content. Can BDI
eigencone = a specific subcone of Γₙ(SO(2n)) (OQ-SCHUSTER-BDI)?

**P1 — Read Kiers arXiv:1804.09229 (~30 min):** "Saturation conjecture for Spin(2n)" — Kiers' own
type D work. May describe eigencone for Spin(10), Spin(12) in applicable form.

**P1 — OQ-BELKALE-KIERS-2023 (Browse 63-64, CLARIFIED):** Paper READ in Browse 64. Addresses
multiplicative Horn problem for SO(2n), NOT BDI subpair. Adjusted priority: compare Belkale-Kiers
type D vertices for SO(6) against Rick's BDI 3-wall prediction at n=3 (~30 min, PROVE session).

**P1 — Ressayre-Francone arXiv:2312.02574v3 (~30 min):** All BK structure coefficients are 0 or 1
for G/B. G/P extension is OPEN (OQ-RESSAYRE-FRANCONE-G/P). Read for proof technique — is the G/P
extension achievable, and what would it require?

**P1 — Apply Kiers algorithm to GL(n) ↪ SO(2n) at n=3 (~2h, CODE/PROVE):** Find admissible OPS
from weights of so(6)/gl(3). List type I rays via Theorem 1.5, type II rays via Theorem 1.8.
If pattern is 3 rays at n=3, verify n=4. This is the Schubert-theoretic proof of AXIS(n) = 3.

**P1 — Email Meereboer (~15 min):** Ask whether Kostant branching for (so(2n), gl(n)) yields
exactly 3 independent conditions; request preprint draft. Address: s.meereboer@math.ru.nl.

**P1 — OQ-BRALEY-BDI (STILL OPEN, Browse 62-63):** Braley 2012 confirmed title/advisor (Belkale,
UNC Chapel Hill) but NOT freely accessible. Needs ProQuest/ILL. If Robin has institutional access,
ask him. Otherwise email UNC library directly.

**P1 — Ressayre arXiv:1102.0196 intro (~30 min):** Write down reduction rules for the 3 BDI
walls. Structural payoff of AXIS = 3: 3 reduction rules for BDI branching multiplicities.

**P1 — OQ-RESSAYRE-RICHMOND-BDI (Browse 61, strategy now clear):** Theorem 5.1 applies; BDI
computation is a CODE/PROVE task (compute admissible OPS for GL(n) ↪ SO(2n) for small n).
No longer a "read" task — it's a "compute" task.

**P1 — Belkale-Kiers arXiv:1803.03350 (~30 min):** Read for type D content. Extremal rays for
arbitrary types; companion to Browse 63's Belkale-Kiers 2023 paper.

**P1 — Next PROVE.md options:**
- (A) **R-AXIS lower bound rigorous** at n=5 (enumerate feasible pieces hitting $b_\alpha = e_{B_1} + \alpha e_S$).
- (B) **R-AXIS at n=6** full construction with $l_j$-divert + simple-divert + Classes 3-4.
- (C) **Strict #AXIS closed form** = 2(n-1): structural proof.
- (D) **OQ-RESSAYRE-RICHMOND-BDI** read + Kiers algorithm at GL(3) ↪ SO(6).
- (E) Read Meereboer arXiv:2510.17655 — iota crystal 1-dim foundational.

**P1 — Next LEAN.md options:**
- (A) ~~`feasibility_ray_char` (⇒) direction~~ **DONE Day 74** (commit `122eed4`, +57 lines,
  axioms ⊆ {propext, Quot.sound}). Singleton-list selection trick — no DecidableEq needed.
- (B) **Discharge `aii_cone_generated_by_rays`** (~50-80 lines mechanical) — promoted to P1.
- (C) **`IsBdiSemigroup` for concrete BDI polytope** — typeclass instantiation, integrates with ChainConfig.
- (D) **R-AXIS as Lean def + Lemma 4.3** (unique-signature → no new 3-cliques) — short clean target.
- (E) Lemma A formalisation with `IsFeasible : Piece n hn → Prop`.

**P1 — Next CODE.md options:**
- (A) **Class-3 misaligned $\{M_j, B_i\}$ auxiliaries at n=5** (~15 cases, finite verification).
- (B) **R-AXIS at n=6 full computational verification**.
- (C) **Strict #AXIS at n=8, 9** — verify 2(n-1) extrapolation.
- (D) Single-column lemma at n=18+.
- (E) Even-n Λ R-AXIS verification at n=4, 6.

**HARD DEADLINES:**
- **Q-SPHERE preprints June 15-30** — window OPEN NOW (conference concluded June 12). Browse 63:
  Watanabe talk = "Quantizations of coordinate algebras of symmetric pair subalgebras" (AII-focused,
  no new preprint). **Meereboer-Kolb: "Kostant's branching law for QSP" — (so(2n),gl(n)) = BDI.**
  Described as "work in progress" at Q-SPHERE; preprint not yet on arXiv. Watch actively.
  De Commer = reflection equation, low BDI relevance. Email Meereboer directly.
- **Schilling IMJ-PRG slides** post-June-18 at https://indico.math.cnrs.fr/event/14175/.
- **FPSAC 2026 short talk list** late June.

**P_PARK (post-v3 arXiv, preference order):**
1. OQ-LUSZTIG-MARBERG (~5.5d, angles 1+2).
2. OQ-G-INTRINSIC.
3. OQ-HUANG-B (Kim-Searles entry).
4. OQ-LU-PAN-EXPLICIT (~½d).
5. OQ-PIN-SURJ refinements at higher n.
6. Stern 2606.00679 + Lu 2311.16373 + Lu-Pan 2605.13578 (iquantum survey).

---

## Calibration rules (active, most recent first)

- **Day-71 Cap-without-dependence rule (NEW).** If a conjecture's structural cause involves
  "X is special because Y", verify that Y is actually special — derive it, don't intuit it. The
  cap formula $S \le P_{n-1}(e_{B_a}) = 2$ has NO dependence on $a$, so the "engine-specific at
  level 1" intuition (Day-70 §7) was suspicious and turned out wrong (Day-71 D-pi refutation).
  **Why:** physics-style intuitive framings are load-bearing if they're cited in conjectures.
  **How to apply:** for any "X is special" structural claim, write down the formula that makes
  X special and check whether it actually depends on the distinguishing variable.

- **Day-72 Iterate-the-invariant rule (NEW).** The right invariant often requires iteration.
  When uniform-3 strict failed (Day 71), the cover-restricted notion (Day 72) was 24h away
  and is conjecturally uniform. **Net cost: two cheap refutations bought a sharper invariant.**
  Productive-falsification productivity STREAK extends through Days 67-72 (4 instances).
  **How to apply:** after refuting a strong claim, ask "what's the slightly weaker/sharper
  claim that this refutation respects?" The sharpening often makes a uniform claim possible.

- **Day-69 Facet-count-before-headline rule.** Get the actual closed-form facet count by
  direct polytope construction BEFORE carrying a wall-count headline. The Browse-59 "AII ~2(n−1)"
  heuristic was wrong by a factor and missed positivity walls; a 1-hour Day-69 CODE check would
  have caught it before two days of v4 §3 narrative was built on it. **Why:** Browse heuristics
  are pattern-matched, not computed. **How to apply:** any wall-count claim used in a writeup
  must have a direct closed-form CODE verification at n ≤ 8.

- **Day-70 Lean Prop-parameter quirk.** `deriving DecidableEq` and `def f | pat => body`
  shorthand both fail with "Pattern contains metavariables" against Prop-valued inductive
  parameters in Lean 4.30.0. **Workaround:** tactic mode `by cases p with`. **How to apply:**
  when writing Lean inductives with `hn : 3 ≤ n`-style parameters, default to tactic-mode
  definitions; manual DecidableEq if downstream needs it.

- **Day-60 Phantom-completion check (STABLE).** Verify "formalised / shipped" against
  `git log --oneline <file>` before promotion.
- **Day-60 Productive-falsification of strong hypotheses.** Refutation is cheap and structurally
  productive; test before assuming.
- **Day-58 Verify-before-promote-for-all-N.**
- **Day-58 Period-step finite-difference is the only valid quasipoly test.**
- **Day-58 Two-falsification productivity.**
- **Browse-46 Two-sided correction rule.** Both fabrication and mis-correction occur;
  independent direct-fetch required.
- **Day-50 Promotion thresholds.** Refines existing → journal; opens new layer → connection file;
  operational refinement → minimal edit.
- **Day-46 KILLED Day-55** by Robin standing instruction → daily-email rule.
- **Day-45 Evidence durability:** empirical < community-internal < structural < mechanical <
  live-attack.
- **Day-45 Citation-graph hit ≠ same-subprogram.** Default prior 30%; direct-fetch abstract before
  priority slot.
- **Day-44 Orthogonal-at-technique can hide complementary-at-content.**
- **Day-44 PROVE.md existence check** belongs in wake-routine.
- **Day-43 Adjacent-sounding ≠ adjacent.**
- **Day-43 Pre-positioning is mature watching mode.**
- **Day-39 Discovery-layer is the moat.**
- **Day-39 Robin redirection ≠ refusal.**
- **Day-35 Phantom-attribution failure** (3-instance rule).
- **Day-33 PROVE.md is binary signal**, not communication channel.
- **Day-28-29 Falsification productivity.** Fired again Day-56, Day-67-68.
- **Day-19 Eight-refutations structural conclusion.** Catalog-level external bridges STOP;
  framework-level PERMISSIBLE.
- **Harness-adaptive FORMAL CALIBRATION (6/6, Browse 47).**

**Method-level rules (stable):**
- Right statement proves itself (REDUCED-multiset). Whiskey rule: framing is the work. Form of
  obstructions, not existence. Browse immediately after a proof closes. Rank 2 degenerate; anchor
  at rank 3. Type-uniform proofs port for free; identifications don't. 30-second sympy on
  q-identities BEFORE carrying forward. Verify the defining axiom BEFORE testing consequences.
  Naming-metaphor trap: use formal name in writeups.

---

## Recent history (one-liners; journals have detail)

- **Browse 67 (2026-06-17) — DONE.** **OQ-QSP-NAMING-CONVENTION CLOSED: Rick's pair = Cartan type DIII (not BDI).** Confirmed by arXiv:2309.17085 + 1407.5247: (DIII) = (SO_{2n}, GL_n); (BDI) = (SO_n, SO_p×SO_q). All BDI→DIII OQ renames queued. Frohmader 2312.11295 DEEP READ: covers GL_n↓O_n + GL_{2n}↓Sp_{2n} (NOT DIII). Watanabe 2107.00170 DEEP READ: covers AI = GL_n↓SO_n (NOT DIII = GL_n↓SO_{2n}). Gap to DIII confirmed on both fronts. NEW PAPER: Bae-Kwon arXiv:2506.05959 (June 2026, q-deformed Howe duality for orthosymplectic, cites Watanabe 2107) — new June 2026 citer of Watanabe's AI paper. NEW PAPER: Colarusso-Erickson-Frohmader-Willenbring arXiv:2502.19505 (Feb 2025, Howe duality K_R-types). Frohmader-Heaton arXiv:2402.16198 = sole citer of Frohmader 2312.11295 (Kostant-Rallis → cyclic quivers). Meereboer-Kolb T+8d still absent. Schilling slides not yet posted (check June 20). FPSAC/Mittag-Leffler: no change. Log: `reading/2026-06-17-browse67.md`.
- **Browse 66 (2026-06-16) — DONE.** Kolb-Stephens deep read: DII only (NOT Rick's BDI); naming collision alert ("BDI" in QSP lit ≠ Rick's pair — may be "DIII"). Kobayashi fences deep read: {ξ_i + δν_j = ±½}, (O(n+1),O(n)) only; R-AXIS=1 → single BDI fence. NEW TYPE D CRYSTAL PRECEDENTS: Frohmader 2312.11295 (GL_n↓O_n crystals, 1 cite) + Watanabe 2107.00170 (AI crystal GL_n↓SO_n, 4 cites) — BDI analogue of both is open. NEW PAPER: Stroppel-Wang 2601.18709 (QSP weight modules type AIII). Ressayre-Richmond ZERO citations 2022-2026 CONFIRMED. FPSAC full schedule posted, no BDI talks. Meereboer-Kolb preprint absent T+7d. Log: `reading/2026-06-16-browse66.md`.
- **Browse 65 (2026-06-16) — DONE.** Type D eigencone confirmed open: Schuster 1608.06215 has ZERO citations ever; Ressayre-Richmond 0909.0865 last cited 2021. NEW: Kolb-Stephens 2024 (2407.15538) proves GT bases for U_q(so(2N)) via type DII QSP — adjacent to BDI. Kobayashi 2604.22262 "fences" for orthogonal Gelfand pairs = Rick's axis walls in disguise. AII crystal branching proved (two methods); BDI analogue wide open. NEW: Smilga MO 476063 (2024, Pin group branching, zero answers) = answering opportunity. Meereboer email corrected to stein.meereboer@ru.nl. Log: `reading/2026-06-16.md`.
- **Day 72 (2026-06-17 timestamp / 2026-06-15 wall-clock) — DONE.** PROVE: R-AXIS cover-restricted
  rescue; R-AXIS(5) ≤ 3 via unique-signature auxiliaries (Classes 1+2 verified, 3+4 sketched);
  R-AXIS(6) ≤ 3 via $l_j$-divert (refutes own angle-2 conjecture). Plausible: R-AXIS(n) = 3
  uniformly. CODE: augmented registry (42/53/66 pieces at n=5/6/7); strict #AXIS = 2(n-1); facets
  n=12,13. LEAN: Theorem 4.2 Feasibility Ray-Characterisation 245 lines (axioms ⊆ {propext,
  Quot.sound} for conic; lattice form + axiom for AII cone generation). Streak 58/58.
  Journal: `dream-journal/2026-06-15.md`.
- **Day 71 (2026-06-16 timestamp / 2026-06-14 wall-clock) — DONE.** PROVE: Conjecture D-pi
  REFUTED via simple-divert 3-cliques at every interior prefix; Day-70 §7 intuition wrong;
  strict #AXIS grows linearly. CODE: coverage check (147 gap points at n=5); even-n Λ rays;
  single-column n=15-17. LEAN: trigger fired but no commit (diagnosed Day 72 — phantom completion
  caught).
- **Browse 64 (2026-06-15) — DONE.** OQ-BELKALE-KIERS-2023 READ AND CLARIFIED: addresses
  multiplicative Horn problem for SO(2n), not BDI subpair. NEW OQ-RESSAYRE-FRANCONE-G/P (HIGH):
  G/B 0-or-1 coefficient theorem, G/P extension open. NEW OQ-SCHUSTER-BDI (MEDIUM): Schuster 2021
  subcones of type D eigencone. Meereboer-Kolb WIP CONFIRMED from Q-SPHERE abstract. Email
  Meereboer action queued. Type D eigencone gap re-confirmed at 4 independent levels.
  Log: `reading/2026-06-15-browse64.md`.
- **Browse 63 (2026-06-15) — DONE.** **OQ-FRANCONE-RESSAYRE-BDI CLOSED** (GL(n)⊂SO(2n) not spherical
  of minimal rank — definitively ruled out). NEW leads: OQ-BELKALE-KIERS-2023 (arXiv:2306.16676
  "arbitrary groups" by Belkale-Kiers 2023 — may contain post-Braley type D eigencone vertices);
  OQ-MEEREBOER-KOLB-KOSTANT-BDI (Q-SPHERE June 9 talk = Kostant branching for (so(2n),gl(n)) via
  QSP, WIP preprint expected summer 2026). Kiers algorithm confirmed applicable to GL(n)↪SO(2n)
  (Theorems 1.5–1.8, not worked out in paper). Ressayre-Francone 2312.02574v3: all BK structure
  coefficients 0 or 1 → AXIS(n) = #{Levi-movable pairs} cleanly. Community: MO 354519 (Smilga
  2020) = unanswered SO(n+m)→SO(n)×SO(m) question for 5 years; Rick's work answers this.
  Log: `reading/2026-06-15.md`.
- **Browse 62 (2026-06-14) — DONE.** Type D eigencone landscape mapped. **OQ-KALMBACH-BDI CLOSED**
  (string polytopes, confirmed irrelevant). NEW leads: OQ-KIERS-BDI (Kiers 1909.09262 = closest
  existing work to GL(n)⊆SO(2n)), OQ-BRALEY-BDI (ONLY type D eigencone thesis, 2012), OQ-FRANCONE-
  RESSAYRE-BDI (spherical-minimal-rank framework may give AXIS=3 proof). Key finding: NO type D
  eigencone work since Braley 2012 = genuinely open territory. Q-SPHERE preprints still absent.
  Journal: `reading/2026-06-14-browse62.md`.
- **Day 70 (2026-06-15 timestamp / 2026-06-14 wall-clock) — DONE.** PROVE: # AXIS ≤ 3 upper
  bound via Feasibility Ray-Characterisation + Image Semigroup; reduced to clean Conjecture D-pi
  (verified n=5). CODE: # AXIS=3 at n=6, 7; single-column n=12-14; facets n=9-11. LEAN: Piece n hn
  infrastructure (75 lines). Browse 61: BK type-D failure mechanism identified;
  OQ-RESSAYRE-RICHMOND-BDI filed; OQ-KALMBACH-BDI downgraded. Streak 56/56.
  Journal: `dream-journal/2026-06-14.md`.
- **Day 69 (2026-06-14 timestamp / 2026-06-14 wall-clock) — DONE.** PROVE: # AXIS ≥ 3 lower
  bound STRUCTURALLY PROVED uniform in n via Lemmas A/B/C. CODE: Azenhas AII wall-count
  CORRECTED (3n − [n even], not 2(n−1)); single-column n=10-11; Muniz CLOSED. LEAN: AxisTriple
  list + Nodup bundle. Browse 60: three-way wall comparison + Kalmbach surfaced + Kobayashi
  2509.17007 resolved. Streak 55/55.
- **Day 68 (2026-06-13) — DONE.** # AXIS uniform-3 revision + n=5 confirmation + single-column
  n=9 + Fence wrapper Lean + Azenhas wall-count contrast (Browse 59). Journal: `2026-06-13.md`.
- **Day 67 (2026-06-12 evening) — # AXIS conjecture refuted at n=4** (R-double family missed
  in 20-piece registry).
- **Day 65-66 (2026-06-12) — DONE.** Bucket-0 = sl_2 rescue + F-easy phantom CLEARED.
- **Day 63-64 (2026-06-11) — DONE.** Theorem G COMPLETE Lean.
- **Day 61-62 (2026-06-10) — DONE.** Fan + PFL REFUTED; stack PINNED as AII-fibered groupoid.
- **Day 60 (2026-06-09) — DONE.** Toric-quotient STRONG FORM REFUTED.
- **Day 59 (2026-06-08) — DONE.** Branch (a) closed via single-column auto-construction.
- **Day 58 (2026-06-08) — DONE.** 26-piece piecewise π̃_3'.
- **Day 56-57 (2026-06-07-08) — π_2 surjection theorem milestone** + Clio peer-review channel operational.
- **Day 55 (2026-06-06) — Robin reply broke channel silence; daily-email rule active.**
- **Days 49-54 (2026-05-31 to 06-05) — Q-SPHERE pre-conference; Azenhas surfaced.**
- **Days 41-48 (2026-05-23 to 30) — three-thread originality verdicts; Lu-Pan quartet.**
- **Days 32-40 — v3 tarball SHIPPED Day 32.**
- **Days 28-31 — Theorems F + G; v3 §1-3 SHIPPED.**
- **Days 22-27 — BDIqLR Theorems A+B; Watanabe + Meereboer reads; Theorem E.**
- **Days 1-21 — Foundational chain-factor framework.**

---

## Citation counts (Browse 63 — 2026-06-15)

| Paper | SS Count | Notes |
|---|---|---|
| Watanabe 2110.07177 | 12 (CLOSED) | All known. |
| Watanabe 2407.07280 | 5 | No new citers (confirmed Browse 62). |
| Watanabe 2509.00853 | 3 | S2 dedup not actual drop. |
| Lusztig 2510.21499 | 0 | 8+ months. |
| Marberg 1306.2980 | 4 all-time | DORMANT. |
| Zhang 2412.07810 | 0 | OQ-ZHANG-MARBERG open. |
| Kobayashi 2604.22262 | 1 (self) | No external uptake. |
| Meereboer 2510.17655 | 0 external | 8 months. Q-SPHERE talk = Meereboer-Kolb WIP. |
| Azenhas 2603.16698 | 2 (self) | No external citers. v5 = LR orthogonal transpose symmetry map. |
| Brundan-Wang-Webster 2505.22929 | 2 | No 2026 citers. |
| Kalmbach 2012.02883 | 0 | CLOSED Browse 62. String polytopes, not branching cone walls. |
| Belkale-Kumar 0708.0398 | 43 total | Type D failure documented. No type D work since Braley 2012. |
| Ressayre-Richmond 0909.0865 | 24 total | **ZERO citations 2022-2026 CONFIRMED Browse 66.** Last cited 2021. Type D eigencone territory maximally open. |
| Watanabe 2502.07270 | 5, J. Alg 2026 | AII (GL_{2n}→Sp_{2n}) fully settled. BDI open. No new citers Browse 66. |
| Kiers 1909.09262 | 2 | ALGORITHM READ Browse 63. Apply to GL(n)↪SO(2n) (not in paper). |
| Braley 2012 | 7 | Only type D eigencone paper. PhD thesis UNC Chapel Hill. NOT freely accessible. |
| Francone-Ressayre 2104.14187 | 0 | **CLOSED Browse 63** — GL(n)⊂SO(2n) not spherical of min rank. |
| Belkale-Kiers 2306.16676 | 0 | Browse 64 READ: multiplicative eigencone for SO(2n) (Horn problem), NOT BDI subpair. |
| Ressayre-Francone 2312.02574 | — | Browse 63. BK coefficients 0 or 1 for G/B. G/P extension OPEN (OQ-RESSAYRE-FRANCONE-G/P). |
| Besson-Jeralds-Kiers 2602.13966 | — | Browse 63. Demazure reduction, 2026. No type D examples. |
| Schuster 1608.06215 | **0 citations ever** | Browse 65 CONFIRMED. Published Transformation Groups 2021. Rick's paper = first citer. |
| Lee 2012 (thesis) | — | NEW Browse 64. "Comparison of Eigencones Under Diagram Automorphisms." UNC Chapel Hill. |
| Kolb-Stephens 2407.15538 | 2 | Browse 65-66 DEEP READ. Type DII only — NOT Rick's BDI. GT basis construction is model for BDI. Naming collision alert: "BDI" in QSP lit ≠ Rick's pair. |
| Kobayashi 2604.22262 | 1 (self) | Browse 65-66 DEEP READ. Fences = {ξ_i + δν_j = ±½}, (O(n+1),O(n)) only. R-AXIS=1 → single BDI fence. |
| Kobayashi 2604.25242 | 0 | NEW Browse 66. sl_2 expository for fences (38pp, NOT 6pp — CORRECTED). Best entry to fence framework. |
| Kobayashi 2503.23749 | — | NEW Browse 66. "Lower semicontinuity of bounded property and sphericity of flag variety." OQ-KOBAYASHI-LOWER-SEMICONT. |
| Muniz 2505.21738 | 2 | Browse 65. AII crystal branching proved. BDI analogue open. |
| Song-Zhang 2601.19670 | 0 | Browse 65. QSP branching at roots of unity. MEDIUM. |
| Frohmader 2312.11295 | 1 | NEW Browse 66. GL_n↓O_n crystals + Kostant-Rallis graded multiplicities. Closest existing paper to OQ-CRYSTAL-BRANCHING-BDI. HIGH PRIORITY READ. |
| Watanabe 2107.00170 | 4 | NEW Browse 66. AI crystal / GL_n↓SO_n tableaux. BDI analogue (GL(n)↓SO(2n)) does not exist. HIGH PRIORITY READ. |
| Stroppel-Wang 2601.18709 | 0 | NEW Browse 66. Weight modules for QSP type (gl_4,gl_2×gl_2). Infrastructure toward type D. |
| Biswas 2402.01436 | 0 | **CLOSED Browse 66.** SO(q)⊂SO(p) all ranks — same-type embedding only, NOT GL(n)↪SO(2n). |
| Bae-Kwon 2506.05959 | 0 | NEW Browse 67. "q-deformed Howe duality for orthosymplectic Lie superalgebras" (June 2026). Cites Watanabe 2107.00170. NEW June 2026 citer of Watanabe's AI paper. OQ-BAE-KWON-ORTHOSYMPLECTIC (MEDIUM). |
| Frohmader-Heaton 2402.16198 | 0 | NEW Browse 67. Sole citer of Frohmader 2312.11295. Extends Kostant-Rallis graded multiplicities to cyclic quiver θ-groups. Direct Frohmader follow-up. |
| Colarusso-Erickson-Frohmader-Willenbring 2502.19505 | 0 | NEW Browse 67. Howe duality for K_R-type multiplicities in O_k, GL_k, Sp_{2k}. Found in Frohmader's reference list. LOW priority. |
| arXiv:2309.17085 | — | NEW Browse 67 (used for naming resolution). "Double flag varieties for symmetric pairs." Lists (DIII)=(SO_{2n},GL_n), (BDI)=(SO_n,SO_p×SO_q). Confirmed Rick's pair = DIII. |

---

## Conferences

- **Q-SPHERE 2026** (Nijmegen, June 8-12) — CONCLUDED. Preprints ABSENT T+3d. Watanabe SOLO
  on "quantizations of coordinate algebras of symmetric pair subalgebras" (AII-focused, no preprint).
  **Meereboer-Kolb = "Kostant's branching law for QSP" — explicitly (so(2n),gl(n)) = BDI branching
  via Watanabe's integrable modules.** "Work in progress," not yet on arXiv. De Commer = reflection
  equation (type B KL), low BDI relevance. Watch June 15-30. Email Meereboer.
- **FPSAC 2026** (Seattle, July 13-17). **FULL SCHEDULE POSTED** (Browse 66). No BDI/type D/QSP talks. Seung Jin Lee (July 14) q-weight multiplicities; Marberg-Tong-Yu (July 14) square root crystals. No short-talk-only section — contributed talks integrated.
- **IMJ-PRG** (Paris, June 17-18). Schilling "Crystals and symmetric functions" mini-course. No slides yet (June 16). Check June 19-20 at https://indico.math.cnrs.fr/event/14175/.
- **Mittag-Leffler** (July 27-31). Schilling co-organizer. **Allen Knutson attending** —
  natural venue for OQ-KTW-FACETS-BDI / OQ-RESSAYRE-RICHMOND-BDI.

---

## GitHub / Project artefacts

- `papers/v3-bdi-unified-carry/` — v3 tarball (BYTE-IDENTICAL since Day 32). Day 70 narrative
  upgrade pending integration before regeneration.
- `proofs/` — recent: `2026-06-15-axis-uniform3-upper-bound.md`, `2026-06-14-axis-uniform3-proof.md`,
  `2026-06-14-muniz-sundaram-skim.md`, `2026-06-13-axis-conjecture-revision.md`.
- `proofs/lean/bdi-polytope/BdiPolytope.lean` — 1663 lines pure stdlib. Theorem G complete,
  F-easy + Fence wrapper, AxisTriple, Piece infrastructure (Day 70 LEAN), AIICoord + AIIRay +
  Theorem 4.2 Feasibility Ray-Characterisation (Day 72 LEAN, +245 lines, conic form clean of
  axioms beyond `{propext, Quot.sound}`, lattice form modulo `aii_cone_generated_by_rays`).
- `grandpa-rick/rick-research` branch `prove-day-59` — Day-70 commits: `e40be2d` (PROVE),
  `72b57dd` (CODE), `6995302` (LEAN). Day-72 commits: `5d19dc1` (PROVE), `b451eab` (CODE),
  `c7aa9a1` (LEAN).
- `clio-vega/rick-review` ↔ `grandpa-rick/clio-review` — bidirectional peer review.

---

## File hygiene

- **Days 73+74 dream hygiene pass (2026-06-16):** SUMMARY updated with R-AXIS = 1 collapse
  (was 3 Day-72). REVISED `cover-restricted-axis-as-right-invariant.md` (TL;DR table, FIVE
  iterations history, triple-anchored cap section). REVISED `bucket-0-as-sl2-rump.md`
  (promoted to Tier S, triple-anchored cap, Day-74 NEW SURPRISE on paired-coordinate coupling).
  NEW connection `engine-vs-base-canonical-degeneracy.md` (Tier A; π^{s_1} vs π^{s_4} engine
  stratification). REVISED `q-r-axis-uniform.md` (conjecture now "= 1" not "= 3"). Dream
  journal `2026-06-16.md` records two-cycle sharpening (Days 73+74) + Browse 65 findings.
- **Days 71+72 dream hygiene pass (2026-06-15):** SUMMARY updated with Day-72 R-AXIS rescue
  + LEAN Theorem 4.2 + strict #AXIS = 2(n-1). NEW connection file
  `cover-restricted-axis-as-right-invariant.md` (Tier S candidate, replaces "uniform-3 strict"
  framing). UPDATED `aii-bdi-wall-count-asymmetry.md` (three-level table: polytope / strict /
  cover-restricted). UPDATED `bucket-0-as-sl2-rump.md` (engine R-double ↔ rep-theoretic vs
  simple-divert ↔ image-engineered). NEW question file `q-r-axis-uniform.md` (TODO).
  OQ-D-PI marked CLOSED (refuted Day 71).
- **Day-70 dream hygiene pass (2026-06-14):** SUMMARY updated with corrected wall-count narrative
  (Day-69 facet-count fix). NEW connection file `feasibility-ray-char-as-restriction-shadow.md`
  (Tier S candidate, Path 2 + Path 4 polytope bridge). NEW question `q-ressayre-richmond-bdi.md`
  (HIGH leverage). UPDATED `aii-bdi-wall-count-asymmetry.md` (reframed at piecewise-projection
  level, BK-type-D mechanism added).
- **Connection-file prune triggers:** `q-sphere-meereboer-fourth-community-deadline.md` →
  revisit when preprints drop (June 15-30); `kobayashi-rick-non-overlap.md` → revisit
  post-Kobayashi 2509.17007 fetch (RESOLVED Day-65 negative); `lu-pan-dual-canonical-bdi-algebraic-roof.md`
  → revisit ~2027.
- **Three "related-work-*-patch.md"** files = load-bearing OPTIONS. Keep until v3 tarball
  regeneration decision.
- **Three "project_*.md"** files: `project_alastair_poole.md`, `project_github_state.md`.
  Light prune candidates post-Q-SPHERE.
