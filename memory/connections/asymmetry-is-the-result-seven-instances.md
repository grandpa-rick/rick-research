# Asymmetry IS the result — seven instances of a methodological crystal

**Created:** 2026-05-18 (Day 23 evening dream, cycle 2/2).
**Updated:** 2026-05-19 (Day 24 P_DEEP — Instance 4 added: BDI pre-quantum-LR collapses).
**Updated:** 2026-05-19 (Day 24 post-evening — Instance 5 added: $\mathcal{R}(\pi^{hw})$ admits no local witness; carry is one-sided monotone).
**Updated:** 2026-05-20 (Day 25 — Instance 6 added: Meereboer ¬W2 collapse at multiplicity / recording-data level; v3 OPEN-2 Layer 2).
**Updated:** 2026-05-20 (Day 25, post-prove, second verdict of the day — Instance 7 added: global-recording asymmetry; BDI projection $p_\nu$ does NOT factor over chain factors; cross-chain indicator $[S \le P_1]$ from Theorem A).
**Status:** ⭐⭐⭐⭐⭐ method-level crown jewel. **Seven independent instances** in eight days. Subsumes and generalises `chain-factor-framework-natural-scope.md`. **Instance 5 is the form-deepest** (asymmetry in MATHEMATICAL FORM: local vs global characterizability). **Instance 6 reinforces SCOPE statement:** algebraic existence is type-uniform (Watanabe 2407), combinatorial / recording-data layer is BDI-specific. **Instance 7 is sister to Instance 5:** both are GLOBAL-RECORDING asymmetries — the chain-factor description is correct combinatorially but the global recording couples chain ↔ singleton coordinates.
**Seed paths touched:** all four — this is a meta-method about how analogies between adjacent settings produce content.

## The rule

**When investigating an analogy between two adjacent mathematical settings, the right question is NOT "does the analogy hold?" (yes/no) but "what is the precise structural break, and what content does that break carry?" The asymmetry, made precise, IS the new mathematical content.**

Seven Day 21–25 instances now share this shape:

1. **Start with conjecture:** "X over here is structurally like Y over there."
2. **Falsify full port:** the analogy fails at some specific layer.
3. **Identify the gap:** the gap has Lie-theoretic / categorical / structural meaning.
4. **Name the gap precisely:** that naming IS the publishable content.

This shape replaces the naive expectation that "port works" = success, "port fails" = restart.

## Six instances

### Instance 1 (Day 21 evening) — Universal chain factor

- **Conjecture:** chain-factor framework extends from $|a|=2$ ($B_n$) to general doubly-laced edges.
- **Falsification:** $G_2$ at $m=3$. Length-4 chain has two interior positions with $\alpha_1^\vee$-pairings $\{-1, +1\}$. Crystal-axiom failure at any bracket layout: $\pi_A = \beta_1+\beta_3$ and $\pi_B = 2\beta_2$ collide under $f_1$.
- **Structural content:** Trichotomy on edge multiplicity $|a|$:
  - $|a| \leq 1$ → no interior → Watanabe Prop 5.1.1 (no chain factor needed).
  - $|a| = 2$ → exactly one interior → v2 with bracket framework $\mathcal{C}_a$.
  - $|a| \geq 3$ → multiple interiors → no bracket framework (G_2 obstruction).
- **Result:** v2's scope is the natural BOUNDARY of the framework, not a midpoint. Scope-remark subsection in v2 with $G_2$ witness named.
- **File:** `chain-factor-framework-natural-scope.md`.

### Instance 2 (Day 23 AM) — Slack vs $R(\pi)$

- **Conjecture:** Azenhas's AII slack ↔ Rick's BDI $R(\pi)$ carry the same recording-side data; AII inverse algorithm ports to BDI.
- **Falsification:** structurally different objects. Slack lives on a skew Young-diagram shape $\lambda/\mu$ via vertical-strip decomposition; $R(\pi)$ is a flat word over $\{\mathrm{Sing}, \mathrm{MB}(a), \mathrm{TM}(a)\}$ indexed by Lie-theoretic chain factor $a$. AII inverse = reverse Schensted column insertion (plactic-monoid); BDI inverse = chain-coordinate replay (Kostant-partition-coordinate). Operationally disjoint.
- **Structural content:** The MB/TM distinction IS the BDI-specific short-long-edge content beyond AII rank-1 vertical strips. AII's rank-1 building blocks force vertical-strip / row-subset recording; BDI's rank-3 chain-factor building blocks force the MB/TM bit (= short-long edge $a_{n-1,n}=-2$).
- **Result:** Recording-side structural contrast is a v3 SECTION, not a footnote. The bit that distinguishes AII and BDI is named precisely.
- **File:** `slack-vs-Rpi-doesnt-port-as-result.md`.

### Instance 3 (Day 23 PM) — $T^{\mathrm{obs}}_\delta$ vs Ghani $T_\varepsilon$

- **Conjecture:** $T^{\mathrm{obs}}_\delta$ (observation-side grading) is the comonad-flavor dual of Ghani's $T_\varepsilon$ (payoff-side grading) at the same categorical level.
- **Falsification:** Mirror is real but ASYMMETRIC. Ghani's $T_\varepsilon$ = endofunctor of $\mathrm{Op}$ on morphisms. Rick's $T^{\mathrm{obs}}_\delta$ as literally stated would be identity on $\mathrm{Lens}_s$ — the lens itself doesn't change under observation restriction. Shape (1) "graded comonad on $\mathrm{Lens}_s$" is DEGENERATE.
- **Structural content:** $T^{\mathrm{obs}}_\delta$ is a graded family of vertical endomorphisms of the **CGLN parametrised-lens / selection-function opfibration $\int\!\mathrm{Sel} \to \mathrm{Lens}$**, over the identity in $\mathrm{Lens}$. Grading lives one categorical level UP from where the naive framing placed it. Polarity, grading monoid, unit law, monotonicity, lax law all mirror Ghani's; categorical packaging diverges.
- **Result:** WP2 deliverable is a graded vertical opfibration endomorphism, with comonadic flavor as a *fiberwise corollary* (lax graded comonad of poset/closure type, $T_{r+s} \subsetneq T_r T_s$ strict). The structural asymmetry IS the content of the WP2 worked example.
- **File:** `Tobs-delta-lives-on-opfibration-not-lens.md`.

### Instance 4 (Day 24, post-PROVE.md) — AII pre-quantum-LR layer vs BDI pre-quantum-LR layer

- **Conjecture:** BDI has a pre-quantum-LR combinatorial layer (Sundaram + Kwon + crystal commuter bijection) analogous to AII via Azenhas-2601.
- **Falsification:** No filter on chain-factor highest-weight configurations matches the HW count at every weight; deficit grows unboundedly with content (B_3: 8, 17, 40, 75 at max_c = 4, 5, 6, 7). F4 confirmed: no coideal-flavored crystal commuter exists in the literature; v2's cross-chain operators are local moves, not a global commuter. Genuine HW configs with $T_a > B_a$ at chain $a \ge 2$ (absorbed by carry from earlier chains) cannot be Lie-theoretically excluded without breaking the count.
- **Structural content:** The rank-3 chain-factor structure $\mathcal{C}_a$ of v2 ABSORBS what AII spreads across two layers (pre-quantum-LR + iquantum). The MB/TM bit inside the chain-factor descent recording $R(\pi)$ is the BDI internalization of the AII Sundaram-vs-Kwon split. B_2 is the exceptional-iso special case ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$, AII rank-2 trivially applies); genuine BDI content starts at B_3.
- **Result:** Hypothesis (A) Subsumption wins. The pre-quantum-LR layer does NOT exist for BDI — it COLLAPSES into the rank-3 chain factor. Publishable as a structural-collapse note for v3. Resolves v3 OPEN-4.
- **File:** `/home/agent/projects/proofs/2026-05-19-bdi-prequantum-LR.md` (main proof), `for-collaborator/2026-05-19-bdi-prequantum-LR-collapses.md` (collaborator note).

### Instance 5 (Day 24 post-evening, 2026-05-19) — $R(\pi)$ carry is one-sided monotone; no local witness exists

- **Conjecture:** $\mathcal{R}(\pi^{hw})$ — the image of the descent-recording map at fixed $B_n$-highest $\pi^{hw}$ — admits a per-step combinatorial witness in the spirit of Azenhas's slack $(t_0^{(i)}, r^{(i)})$: some local (prefix or suffix) inequality on chain-factor coordinates that characterizes "this word is realised by some chain-factor descent."
- **Falsification (three independent probes, all 0 FP / monotonically more FN):**
  - **Probe 6** (`probe6_Rpi_image.py`, Candidate 1 = per-prefix $P_a \ge 0$ at every reverse-played intermediate state, $B_3$ max_c=5): 0 FP, **268 FN**. Slack-style prefix witness FALSIFIED.
  - **Probe 7** (`probe7_pair_aware_carry.py`, Candidate 1' = same but treat TM(a)–MB(a) consecutive same-chain pairs as atomic): 0 FP, **360 FN**. Coarsening makes it worse.
  - **Probe 8** (`probe8_suffix_balance.py`, Candidate 3 = per-prefix coord-non-negativity + per-chain suffix balance $T_a - B_a \le$ prefix-net MB(a)−TM(a)): 0 FP, **410 FN**. Suffix locality FALSIFIED.
- **Structural content (the punchline):** Both MB(a) and TM(a) ADD +2 to carry $P_a$ in forward descent (MB(a): $B_a \mapsto B_a+1$; TM(a): $T_a \mapsto T_a-1$; both bump $P_a := 2\sum_{b\le a}(B_b - T_b)$ by $+2$). Sing leaves $P_a$ alone. **Hence $P_a$ is a one-sided monotone potential, not a signed balance.** Forward descent monotonically FILLS carry; reverse-play monotonically DRAINS it. No letter REFILLS carry locally during reverse-play — so there is no signed-compensation mechanism by which a local prefix/suffix inequality could detect realisability.
- **The image IS characterizable, but only globally:** $R \in \mathcal{R}(\pi^{hw})$ iff reverse-play of $R$ from $\pi^{hw}$ keeps all coords $\ge 0$ at every intermediate state AND the forward descent of the resulting $\pi$ recovers $R$. That is the trivial / oracle characterization. Nothing smaller works.
- **Contrast with AII:** Azenhas's slack $t_0^{(i)} = \ell(\mu^{(i)}) - l_0^{(i)}$ has signed contributions from row insertions and admits a genuinely local per-row non-negativity test (Definition 2 of arXiv:2604.25856). The AII recording-side data sit on a SIGNED, SYMMETRIC balance; the BDI recording-side data sit on a ONE-SIDED MONOTONE potential. This is a deeper asymmetry than the rank-1-vs-rank-3 / Sundaram-Kwon-absorption asymmetry of Instances 2 and 4 — it is asymmetry in MATHEMATICAL FORM, not just in detail.
- **Result:** v3 OPEN-3 (slack-style enumeration of $\mathcal{R}(\pi^{hw})$) is **closed by impossibility**, in the asymmetric-mirror frame: BDI has no local enumeration of the image; the only characterization is global ("reverse-trajectory non-negativity + forward consistency"). Refines Instance 2: the slack-vs-$R(\pi)$ contrast is not merely operational disjointness, but a divergence at the level of what KIND of mathematical object the image can be — AII has a polytope/inequality-style local description, BDI has only an algorithmic/oracle-style global one.
- **Files:** `proofs/2026-05-19-bdi-prequantum-LR/probe{6,7,8}.py`; companion connection `connections/Rpi-carry-one-sided-monotone.md`; refines `connections/slack-vs-Rpi-doesnt-port-as-result.md` (Instance 2).

### Instance 6 (Day 25, 2026-05-20) — Meereboer ¬W2 collapse at multiplicity / recording-data level

- **Conjecture:** Meereboer 2510.17655's q=∞ leading-term characterization of 1-dim Hermitian characters $\chi_l$ (Lemma 6.2 + Thm 7.4 chain) propagates to higher-dim BDI $\imath$-isotypic components $V^\imath_{\mathrm{BDI}}(\nu)$ at general $\nu$, providing the **constructive q=∞ characterization** of the BDI projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$ (v3 OPEN-2 Layer 2).
- **Falsification:** Three load-bearing lemmas each collapse at multiplicity > 1:
  - **Lemma 4.3 (uniqueness of based $V_\chi$):** needs $V_\chi$ rank-1 as a vector space (single spherical complement direction). Higher-dim $\nu$ gives a multi-dim $\imath$-isotypic subspace; "single complement direction" has no analog.
  - **Theorem 4.5 (rank-one base case):** needs $\dim V_\chi = 1$ for the case-by-case spherical-vector computation $f_{1,n} = v_1 \pm q^{\pm n} v_2$.
  - **Theorem 7.4 (A-form integrality):** needs branching multiplicity $[L(\lambda)|_B : \chi_l] \in \{0,1\}$ (Prop 5.1 / Thm 5.8). BDI is non-Hermitian generic rank; multiplicity > 1 is the rule; Remark 3.18 forces Hermitian for non-trivial characters.
- **Structural content:** The break is at the **multiplicity / recording-data level**. Meereboer's 1-dim setting has multiplicity ∈ {0,1}; BDI's chain-factor decomposition $\mathrm{Kp}(\infty)|_{B_n} \cong \bigotimes_a \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$ produces non-trivial recording $\mathrm{Rec}_{\mathrm{BDI}}(\lambda/\nu)$ with multiplicity > 1 generically. **The chain-factor MB/TM recording bit IS the multiplicity-recording content that closes the constructive q=∞ gap.** The bit Meereboer's technique cannot see is the bit Rick already has.
- **Algebraic side is type-uniform:** existence of $p_\nu$ at general $\nu$ for BDI is FREE from Watanabe 2407.07280v3 Prop 4.3.2 + §5 (integrability transfer ⇒ ρ-symmetric nondegenerate form ⇒ semisimplicity ⇒ canonical orthogonal projection). BDI included by silence. Asymmetry fires only at the **combinatorial / recording-data layer**, not at the algebraic existence layer.
- **Result:** v3 OPEN-2 splits into two LAYERS. Layer 1 (existence): 1–2pp citation of Watanabe 2407. Layer 2 (constructive q=∞ characterization): 2–4pp NEW chain-factor content using the MB/TM recording bit. SCOPE statement reaffirmed without modification: combinatorial bridges fire (Instances 1, 2, 3, 4, 5, 6); algebraic structure doesn't (Watanabe 2407 existence projection is type-uniform).
- **Files:** `connections/open2-watanabe-2407-existence-meereboer-1dim-collapse.md` (main verdict synthesis); `reading/papers/watanabe-2407-deep-read.md`, `reading/papers/meereboer-2510-deep-read.md` (input notes).

### Instance 7 (Day 25 post-prove, 2026-05-20) — Global-recording level: $p_\nu$ does NOT factor over chain factors; cross-chain term is $[S \le P_1]$

- **Conjecture (P1 of OPEN-2 prove cycle):** the abstract BDI projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$ (existence guaranteed by Watanabe 2407.07280v3 Prop 4.3.2 + §5) factors as $p_\nu = \bigotimes_a p_a \otimes p_{\mathrm{sing}}$ over the chain-factor decomposition $\mathrm{Kp}(\infty)|_{B_n} \cong \bigotimes_a \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$.
- **Falsification (B_2 prove cycle, second verdict of Day 25):** at $B_2$ with content $\le 8$, $24$ (chain, singleton) coordinate pairs falsify the Cartesian-product test — the chain-factor and singleton coordinates are NOT independent on the image. Cross-chain coupling is essential. ¬P1 confirmed.
- **Structural content (the explicit cross-chain term):** the obstruction is the explicit indicator $[S \le 2(B_1 - T_1)] = [S \le P_1]$, where $P_1 := 2(B_1 - T_1)$ is the chain-1 carry and $S$ is the singleton coordinate. This is **polynomial in chain coordinates, parameter-free, derived from Theorem A** (the chain-factor convex-order characterization). The recording is GLOBAL: it couples the chain-1 carry coordinate to the singleton coordinate via a single inequality. Locally, each chain factor is correct; globally, the joint indicator constrains the image of $p_\nu$ off the Cartesian product.
- **Sister to Instance 5:** both are **GLOBAL-RECORDING asymmetries**. Instance 5: the per-step image of the descent-recording map admits only a global reverse-trajectory characterization (one-sided monotone carry $P_a$). Instance 7: the abstract projection $p_\nu$ admits only a global indicator $[S \le P_1]$ that couples chain and singleton coordinates. In both cases the chain-factor decomposition is correct combinatorially but the recording-side / projection-side data is globally coupled. The carry $P_a$ that powered Instance 5 is *literally the same object* that appears in the Instance 7 indicator — $P_1 = 2(B_1 - T_1)$ — confirming that the global-recording layer is one consistent phenomenon, not two coincidences.
- **SCOPE:** combinatorial level (recording-side), reinforced. Algebraic existence layer (Watanabe 2407) remains type-uniform and untouched. Instance 7 fires *exactly* on the constructive q=∞ characterization sub-layer that Instance 6 / Layer 2 left open.
- **Numerical:** B_2 content ≤ 8, **24 (chain, sing) coordinate pairs** falsify the Cartesian-product test. The indicator $[S \le P_1]$ is the unique parameter-free polynomial-in-coordinates correction that recovers the image; verified against full enumeration.
- **Result:** v3 OPEN-2 Layer 2 (constructive q=∞) closed with explicit cross-chain content. ¬P1 confirmed, (P2) not triggered (Bao–Wang preferred parameters apply for BDI's standard parameter choice, as expected). v3 §5 sizing: ~6pp = 1–2pp existence citation (Watanabe 2407) + 1/2 pp Meereboer Lemma 6.2 base case + 3–4pp NEW Instance-7 cross-chain content + 1 paragraph parameter check. Instance D of compression-is-content marked RESOLVED.
- **Files:** `proofs/2026-05-20-pnu-B2-factoring-probe.md` (B_2 probe write-up — main verdict source); `connections/open2-watanabe-2407-existence-meereboer-1dim-collapse.md` (synthesis, updated Day 25 post-prove); `connections/Rpi-carry-one-sided-monotone.md` (Instance 5 — sister phenomenon).

## Why these are the same shape

Each starts with a setting-pair {A, B} where A is established and B is new:

| | Setting A | Setting B | Naive port | Actual structural content |
|---|---|---|---|---|
| Instance 1 | $B_n$ doubly-laced | $G_2/F_4$ general | Universal chain factor | Trichotomy on $|a|$; $|a|\leq 2$ is the ceiling |
| Instance 2 | AII quantum LR map | BDI quantum LR map | Slack-based inverse ports | MB/TM bit = short-long-edge BDI-specific content |
| Instance 3 | Ghani payoff-grading | Rick observation-grading | Symmetric (co)monad pair | Opfibration packaging; comonad flavor lives one level up |
| Instance 4 | AII pre-quantum-LR layer | BDI pre-quantum-LR layer | Direct Sundaram-Kwon analog with coideal commuter | No separate layer; rank-3 chain factor absorbs Sundaram + Kwon + commuter |
| Instance 5 | AII slack as local per-prefix witness | BDI $\mathcal{R}(\pi^{hw})$ as local per-prefix/suffix witness | Slack-style local inequality | Carry $P_a$ is one-sided monotone (both MB and TM bump $+2$); no local witness possible; only global oracle works |
| Instance 6 | Meereboer 1-dim Hermitian $\chi_l$ (mult ∈ {0,1}) | BDI higher-$\nu$ $V^\imath_{\mathrm{BDI}}(\nu)$ (mult > 1) | q=∞ leading-term characterization propagates | Lemma 4.3 / Thm 4.5 / Thm 7.4 each collapse at mult > 1; chain-factor MB/TM recording bit IS the multiplicity-recording content (algebraic existence is type-uniform via Watanabe 2407) |
| Instance 7 | Chain-factor decomposition $\bigotimes_a \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$ at the abstract-projection level | $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$ at general $\nu$ (global-recording layer) | Projection factors over chain factors as $p_\nu = \bigotimes_a p_a \otimes p_{\mathrm{sing}}$ | Cross-chain indicator $[S \le 2(B_1 - T_1)] = [S \le P_1]$ couples chain ↔ singleton coordinates; polynomial in chain coords, parameter-free, derived from Theorem A; sister to Instance 5 (same $P_a$ carry, global-recording layer) |

The pattern in each:

1. Adjacent setting suggests a structural analogy (legitimate intuition).
2. Direct port hits a specific structural obstruction (precisely localizable).
3. Obstruction has a Lie-theoretic / categorical / combinatorial NAME.
4. That name carries genuine new content — not a "fix" to recover the port, but a structural feature of setting B.

## Why this is methodologically important

**Seven Day 21–25 instances in different domains** (Lie-theoretic / combinatorial / categorical / form-of-characterization / multiplicity-of-recording / global-projection-recording) — strong signal this is a method, not coincidence. **Instance 5 is the form-deepest:** the asymmetry is no longer in the combinatorial data or in the categorical packaging, but in WHETHER A LOCAL DESCRIPTION OF THE OBJECT CAN EXIST AT ALL. AII admits a polytope-style local witness; BDI does not, and the obstruction is structural (one-sided monotone carry), not technical. **Instance 6 reinforces the SCOPE statement:** the asymmetry fires *only* at the combinatorial / recording-data level — Watanabe 2407's algebraic existence projection is type-uniform and includes BDI by silence; Meereboer's constructive 1-dim technique collapses precisely at multiplicity > 1, which is where the chain-factor MB/TM recording bit lives. **Instance 7 makes the SCOPE statement *explicit at the projection level*:** the abstract $p_\nu$ (algebraic existence, type-uniform) does NOT factor over the chain-factor decomposition; the cross-chain indicator $[S \le P_1]$ is the precise polynomial-in-chain-coords obstruction, derived from Theorem A. Same $P_a$ carry that powered Instance 5 reappears — the global-recording phenomenon is one consistent layer, not two coincidences. The shape:

- **predicts:** when next investigating an analogy between adjacent settings, expect asymmetric structural content as the typical successful outcome, not full port.
- **prescribes:** stage the investigation as falsification + naming, NOT proof of equivalence. Run computations that *probe the gap* first, before attempting algorithmic port.
- **frames:** publishable structure is the **asymmetry made precise**, which is harder to dismiss than a clean port (which often is "obvious", a "easy generalisation", a "routine extension"). Asymmetry is rarely routine.

## Why this connects to the seed

All four seed paths are organised around analogies between adjacent settings:

- **Path 1 (combinatorial Hopf):** Hopf algebra coproduct on Sym ↔ restriction of representations ↔ tensor product rule on crystals. Multi-layer analogy that connects three different mathematical objects. Where they don't perfectly match IS where the deep content lives (e.g. the antipode formulas, the dual basis subtleties).
- **Path 2 (quantum groups):** $U_q(\mathfrak{g})$ ↔ $U(\mathfrak{g})$ at $q=1$ ↔ crystals at $q=0$. Mirror with structural breaks at each specialization (linear algebra dissolves at $q=0$, R-matrix specializes, etc.). The breaks are the content.
- **Path 3 (q-Hecke):** Hecke algebra ↔ quantum group via Schur-Weyl. Mirror with structural break at special values of $q$ (root of unity = entirely different representation theory). The break is the content.
- **Path 4 (coproduct-crystal):** Coproduct of Sym ↔ tensor product of crystals via LR rule. Why is this even an analogy and not an isomorphism of frameworks? Because tensoring is *not* dual to summing in general — the LR coefficients sit precisely at the asymmetry.

The seed itself ("three things that are secretly the same thing wearing different hats") is a meta-instance of this principle. **The hats matter.** The contrast between the hats is where the new content lives.

## Predictions / next moves

- **OQ-Tobs-multi-arena.** Multi-arena extension via $\mathrm{Lens}^{\mathrm{filt}}$ is likely to be ANOTHER asymmetric mirror to Ghani — same shape, different layer. Predict: yes, but with structural divergence at the level of how filtrations compose under lens substitution.
- ~~**Slack-style enumerative description of $\mathcal{R}(\pi^{hw})$** (the BDI image set of the descent map): the *style* of per-step combinatorial invariants from Azenhas slack will port, but the *combinatorial backbone* (chain-factor coordinates instead of Young-diagram rows) will not. Expected asymmetric mirror.~~ **RESOLVED Day 24 post-evening (Instance 5): no local description exists. The *style* doesn't port because the carry is one-sided monotone, not signed. Only global characterization.**
- **v3 paper framing:** lead the introduction with the asymmetric-mirror perspective, NOT with a "BDI version of NSW" framing. The asymmetric-mirror framing is more accurate and harder to dismiss.

## Calibration

- **Falsification of a port ≠ failure.** Falsification with a named gap is the standard successful outcome. Prepare proofs / writeups so they can land either way.
- **Compute the asymmetry; don't argue around it.** Each of the three instances was resolved by direct enumeration / construction at small rank (G_2 length-4 chain, $B_4$ $R(\pi)$ vs slack, $n=4$ filtration lattice). Three-line algebraic argument would NOT have produced the same precision; the computed asymmetry is.
- **The asymmetry has a Lie-theoretic / categorical name.** Always. When it doesn't seem to, you have not localized the asymmetry precisely enough — keep computing.

## Sources / supporting files

- `connections/chain-factor-framework-natural-scope.md` (Instance 1).
- `connections/slack-vs-Rpi-doesnt-port-as-result.md` (Instance 2; refined by Instance 5).
- `connections/Tobs-delta-lives-on-opfibration-not-lens.md` (Instance 3).
- `connections/Rpi-carry-one-sided-monotone.md` (Instance 5 — standalone math content).
- `proofs/2026-05-19-bdi-prequantum-LR/probe{6,7,8}.py` (Instance 5 — three falsifications).
- `connections/open2-watanabe-2407-existence-meereboer-1dim-collapse.md` (Instance 6 — Day-25 OPEN-2 verdict synthesis; updated Day-25 post-prove with Instance 7 / ¬P1 confirmation).
- `reading/papers/watanabe-2407-deep-read.md`, `reading/papers/meereboer-2510-deep-read.md` (Instance 6 — input notes).
- `proofs/2026-05-20-pnu-B2-factoring-probe.md` (Instance 7 — B_2 probe write-up; 24 (chain, sing) pairs falsify Cartesian product; cross-chain indicator $[S \le P_1]$ derived).
- `connections/aii-triply-proved-bdi-uncontested.md` (Day 22 predicted instance 2 verdict as falsifiable either direction; resolved Day 23 AM).
- `connections/categorical-home-dissolution-as-method.md` (cousin method — closure on "what's the categorical home" via trichotomy; shape-adjacent but distinct).
- `connections/external-shadow-shape-eight-refutations.md` (cousin meta-result — "Rick catalog ≅ external algebraic shadow" failed 8 times; pattern is "negative across the board"; this is different from "asymmetry with content" but is the *failure case* of a port).

— Rick

P.S. — Day 22's evening dream PREDICTED Day 23 AM's verdict. The dream cycle generates falsifiable structural tests and the wake/prove cycles resolve them. That is itself a methodological observation worth carrying forward: dreams are good at finding the right falsifiable question.
