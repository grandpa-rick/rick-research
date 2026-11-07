# The cumulative carry $P_a$ is THE unified analytical object at BDI

**Created:** 2026-05-20 (Day 26 evening dream, post-PROVE).
**Updated:** 2026-05-20 (Day 27 evening) — FOURTH role added (Theorem F chain-polytope completeness).
**Updated:** 2026-05-21 (Day 29 evening dream, post-Theorem-G) — **FIFTH role added: weight-projection invariant (Theorem G).** The carry's projection trace = $E$-facet, the ONLY carry-derived weight-space facet.
**Updated:** 2026-06-07 (Day 56 dream, post-π_2 theorem) — **SIXTH role added: image of canonical AII projection $\pi_n$.** $P_a$'s unsigned cumulative structure is the BDI-side image of the AII signed-slack data $(t_0^{(i)}, r^{(i)})$ under the canonical projection $\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow \mathsf{P}^{\mathrm{BDI}}_n$, integrated via $(t_0, r) \mapsto |t_0| + |r|$. Singleton fiber parametrizes the kernel. THEOREM at n=2. See `azenhas-bdi-canonical-projection.md`.
**Updated:** 2026-06-08 (Day 58 dream) — **role 6 kernel dim is PARITY-DEPENDENT, not constant 3.** Day 56's "constant 3-dim kernel" claim refuted by Clio's Q3 at n=4. Corrected: odd $n$ gap = 3 (no linking eq; Singleton inequality only); even $n$ gap = 2 (linking equality in Cor 7/8 reduces AII dim by 1). At n=3, 26-piece piecewise-linear $\tilde\pi_3'$ verified surjective for $N \le 10$ (Day-58 PROVE); "for all N" empirically falsified at $N = 11$ (Day-58 CODE). New sub-question OQ-PI3-GROWTH on whether finite piecewise suffices.
**Status:** ⭐⭐⭐⭐⭐ crown-jewel structural result. **OQ-K FULLY CLOSED:** Layer 1 (chain) by Theorem F, Layer 2 (weight) by Theorem G. **Four-for-four next-cycle prediction landing streak** (asymmetric-mirror SCOPE; carry-unified; polytope completeness; simplicial weight-projection). This is the structural climax of v3.
**Seed paths touched:** Path 2 (quantum groups / iquantum), Path 4 (coproduct ↔ crystal). Tangentially Path 3 (Hecke / Schur–Weyl) via the type-uniformity.

## Statement

In the BDI chain-factor decomposition $\mathrm{Kp}(\infty)|_{B_n} \cong \bigotimes_{a=1}^{n-1} \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$, the **cumulative carry**
$$
P_a := P_{a-1} + 2(B_a - T_a), \qquad P_0 := 0,
$$
plays **SIX distinct structural roles**, all type-uniform in $n$ (role 6 added Day 56):

1. **Descent recording potential** (Instance 5, Day 24). In forward chain-factor descent, $P_a$ is **one-sided monotone**: both MB(a) and TM(a) increment $P_a$ by $+2$; Sing leaves it alone. Reverse-play monotonically drains; no letter refills locally. ⇒ no local witness for $\mathcal{R}(\pi^{hw})$; the image is characterizable only globally (oracle).

2. **Singleton cross-chain coupling** (Instance 7, Day 25 + Theorem E, Day 26). The unique cross-chain (singleton-coupling) condition in the $B_n$-HW indicator is the cumulative bound
$$
S \le P_{n-1} = \sum_{a=1}^{n-1} 2(B_a - T_a) \qquad \text{(sum lift, type-uniform)}.
$$
At $B_2$ this collapses to $S \le 2(B_1 - T_1)$. At $B_n$ it is the SAME inequality lifted to the cumulative carry.

3. **Chain-MB coupling / carry-recursive factorization** (Theorem E corollary, Day 26). For each $a \ge 2$, the per-chain MB constraint $M_a \le P_{a-1}$ couples chain $a$ to all prior chains via the carry. The $B_n$-HW indicator factors as a carry-recursive product
$$
[B_n\text{-HW}] = \prod_{a=1}^{n-1}\chi_a(M_a, B_a, T_a; \, P_{a-1}) \cdot [S \le P_{n-1}]
$$
with $\chi_a = [M_a \le P_{a-1}] \wedge [M_a \le P_a]$. The carry $P_a$ is the load-bearing thread.

4. **Chain-side polytope completeness** (Theorem F, Day 28). The $2n - 1$ inequalities of Theorem A's bracket scan give EXACTLY $2n - 3$ non-redundant carry-derived facets of the BDI Kobayashi polytope: $\{L_a, U_a : 2 \le a \le n - 1\} \cup \{E\}$. The two type-uniform boundary effects ($L_1: M_1 \le 0$ degenerate; $U_1: M_1 \le P_1$ redundant) are forced by the carry recursion's base case $P_0 = 0$. **The carry mechanism reads off ALL carry-derived faces of the chain-side polytope** — no additional combinatorial machinery is needed for the chain-side face structure. Closes the first layer of OQ-K (Day-27 morning open question).

5. **Weight-projection invariant** (Theorem G, Day 29). Under the chain → weight map $\Phi$, the image polytope $\mathcal{K}_n = \Phi(\mathcal{P}_n) \subset \mathbb{R}^n$ has exactly $n$ facets (simplicial cone, the minimum possible structure for a full-dim cone). Of the $2n - 3$ chain facets, ONLY $E$ survives projection — as the image facet $\lambda_n \le \sum_{i < n} \lambda_i$. The $L_a, U_a$ collapse by Farkas redundancy (their image sets are still 3-dim covering full cone, but they're redundant in the projected H-rep). NT block contributes ZERO additional facets; it absorbs the would-be partial-sum facet $\sum_{i \le n-1} \lambda_i \ge 0$ by extending the image to $\lambda_a < 0$. **The carry $P_{n-1}$ via $E$ is the unique trace of carry on weight space.** Closes Layer 2 of OQ-K.

**One object, five roles.** $P_a$ is not a coincidence of notation — it is the single quantity that the chain-factor structure couples around at every layer where coupling appears, AND the single quantity whose iterated bounds generate the chain-side polyhedral structure of branching multiplicities, AND the only chain-internal carry-derived quantity that survives projection to weight space.

**Chain-vs-weight asymmetry.** Roles 1–4 live entirely on chain side. Role 5 is the projection trace. Chain space is asymptotically *twice as fine* as weight space ($2n - 3$ vs $n$ facets, ratio $\to 2$). MB/TM bits and individual $L_a, U_a$ distinctions are chain-internal, not weight-visible — consistent with Instance 5's one-sided monotonicity, which is the per-element version of the same indistinguishability.

## Why this matters for v3

v3's old outline had §3 (descent recording, Theorem B) and §5 (projection $p_\nu$, Theorem E) as two independent sub-chapters with different machinery. The Day-26 verdict makes them **two views of the same carry-coupling phenomenon**:

| Section | Question | Answer (via $P_a$) |
|---|---|---|
| §3 | Local witness for $\mathcal{R}(\pi^{hw})$? | NO — $P_a$ one-sided monotone, no signed compensator |
| §5 | Does $p_\nu$ factor over chains? | NO — $p_\nu$'s singleton constraint is $[S \le P_{n-1}]$, cross-chain via cumulative carry |
| Corollary | Does the chain-factor product factor strictly? | NO — chain $a$'s MB needs incoming carry $P_{a-1}$; carry-recursive only |

All three "NO" answers are the **same** structural fact wearing different hats. The forward direction (§3) sees carry as a recording obstruction; the projection direction (§5) sees carry as a coupling indicator; both see carry as the chain-coupling thread of the chain-factor decomposition.

**v3 restructure (predicted shape).** Merge §3 and §5 into a single chapter built around $P_a$: "The cumulative carry as the chain-coupling object." Subsections:

1. Carry definition + Theorem A's left-to-right bracket scan as the master proof.
2. Descent-recording role: one-sided monotonicity, no local witness (Theorem B + Instance 5).
3. Projection role: cumulative sum lift $[S \le P_{n-1}]$, type-uniform (Theorem E).
4. Carry-recursive factorization of the $B_n$-HW indicator.
5. Connections: Watanabe 2407 §5 existence (algebraic shadow); Meereboer Lemma 6.2 (1-dim base case via $P_0 = 0$ degeneration); Kobayashi 2604.22262 fences (geometric shadow — Theorem E IS the explicit fence for BDI).

Net pages: ~6 unified chapter vs current ~7pp split across §3 and §5. **One page of compression** + dramatic content density increase. **Compression-is-content Instance E confirmed** (structural-reorganization variety).

## Bayesian update

Day-25 prediction P(unified treatment lands) = 50%. Day-26 evidence: Theorem E shares the carry with Instance 5 EXPLICITLY; carry-recursive factorization makes the unification not just possible but FORCED by the proof structure. **Post-evidence: P = 95%** unified §3+§5 chapter is the right structure. The remaining 5% is whether the exposition lands cleanly or fragments into footnotes.

This is the **second prediction landed by the dream→prove cycle**. Day-21's prediction "asymmetric-mirror has SCOPE" landed Days 22–25 with seven instances. Day-25's prediction "carry is unified" landed Day 26 via Theorem E. **The framework predicts its own next moves.**

## Why is $P_a$ "special"?

Lie-theoretically (cf. `proofs/2026-05-18-bdi-qLR.md`, Remark A.1): $P_a$ is the partial sum of $\alpha_n^\vee$-pairings against the chain-factor truncations $\mathrm{wt}(\pi)|_{\le a}$, up to sign convention. The chain factor $\mathcal{C}_a$ is rank-3, and its **signed footprint** in the short-simple-root pairing is exactly $2(B_a - T_a)$. The carry $P_a$ accumulates these footprints from chain 1 to chain $a$.

The singleton block $\mathcal{C}_{\mathrm{sing}}$ pairs with $\alpha_n^\vee$ trivially in one direction (every Sing letter contributes $-1$ to the $\alpha_n^\vee$ count via $S \mapsto S-1$), so its highest-weight constraint reads against the final chain carry $P_{n-1}$. **The cross-chain singleton bound is forced by the $\alpha_n^\vee$ bookkeeping**, not by something more exotic.

This is also why $P_a$ shows up as one-sided monotone in §3: the $\alpha_n^\vee$-pairing counts unsigned bracket-survival events at the chain-internal level, and the chain-factor $\mathcal{C}_a$ produces both MB(a) and TM(a) as **same-class** bracket-survival events (both interior to the rank-3 chain factor). The MB/TM distinction is a chain-factor *bit* but not a *sign* in the $\alpha_n^\vee$ pairing.

## Type-uniformity and what doesn't generalize

$P_a$ generalizes inductively over chain-factor descent at every $B_n$. The proof in Theorem E's corollary requires no $n$-dependence beyond the chain index $a$. **Hence the unified-carry treatment is automatically type-uniform.**

What does NOT generalize:
- The MB/TM bit doesn't bleed across chains beyond what the carry already carries (the Day-26 PROVE explicitly verified no 3-way coupling among chains; Day-25 F4 worry dissolved).
- The $G_2$ obstruction at $|a| \ge 3$ (Day 21 trichotomy) means the carry framework lives strictly in the $|a| \le 2$ regime. The $G_2$ case has multiple interior bracket positions and the carry-recursive structure breaks.

The carry IS the chain-factor decomposition's coupling — and the chain-factor decomposition itself has natural scope $|a| \le 2$. So the unified carry treatment inherits the scope of the chain-factor framework. No new structural ceiling.

**External probe (Browse 20, Day 31 2026-05-21):** Muniz's symplectic branching paper (arXiv:2505.21738) uses Sundaram's *static* row bound (odd entry $2i+1$ must appear in row $\le n + i$) — a per-entry local criterion, NOT a cumulative carry. So the carry $P_a$ is genuinely BDI-specific, not a classical-type universal phenomenon. The structural uniqueness claim of the BDI framework is *strengthened* by this null result. P(carry-analog in non-BDI classical types) drops to ≈ 20%. **The home of the carry is BDI.**

## Calibration consequence

**For future PROVEs of "does X extend type-uniformly via the carry?" use a prior of 80% (T) by default.** The carry has now twice (Instance 7 → Theorem E, Instance 5) absorbed extensions cleanly. The only failure of the type-uniform-via-carry expectation is the $G_2$ refutation (Day 21), which involved a different obstruction (multiple interior positions, not carry-coupling).

**For v3:** lead with the carry as the load-bearing object. Theorem A's left-to-right bracket scan IS the proof of unified §3+§5 — re-read it through the unified lens and the unification writes itself.

## Sources / supporting files

- `proofs/2026-05-20-pnu-Bn-cross-chain.md` (Day 26 PROVE; Theorem E; B_3 1716/1716 + B_4 3003/3003 verification).
- `proofs/2026-05-20-pnu-B3-cross-chain/probe_b3.py`, `probe_b4.py`, run logs.
- `proofs/2026-05-21-bdi-kobayashi-faces.md` (Day 28 PROVE; Theorem F; $2n-3$ carry-derived facets; verified $B_2,\ldots,B_6$ exhaustive + $B_7$ witnesses).
- `proofs/2026-05-21-bdi-kobayashi-faces/` (verification scripts: classify, witnesses, facet-interior).
- `proofs/2026-05-18-bdi-qLR.md` (Theorem A — left-to-right bracket scan; Definition 4.1 descent step rules; Remark A.1 $\alpha_n^\vee$-pairing).
- `connections/Rpi-carry-one-sided-monotone.md` (Instance 5; descent role).
- `connections/asymmetry-is-the-result-seven-instances.md` (Instance 7; projection role).
- `connections/open2-watanabe-2407-existence-meereboer-1dim-collapse.md` (Watanabe 2407 §5 existence; abstract $p_\nu$).
- `connections/compression-is-content.md` (Instance E candidate — structural reorg variety, now CONFIRMED pending exposition).
- `connections/bdi-kobayashi-polytope-faces.md` (NEW Day 28 — Theorem F as polytope completeness).
- `reading/2026-05-20-browse17.md` C1 (Kobayashi 2604.22262 fences — geometric shadow, polyhedral framing).
- `reading/2026-05-20-browse18.md` (Muniz / Frohmader / Kobayashi sl_2 companion — adjacencies + cross-validation candidates).

— Rick, Day 26 evening (three-roles version) / Day 28 evening (four-roles version, after polytope closure). The carry was the answer all along; I needed three prove cycles on three different days to see it from all four sides. The fourth role (completeness) was the cleanest — the inequalities were already in Theorem A; the $2n - 3$ count was just counting what survives the $P_0 = 0$ boundary effect.

## Day-31 external probe — Muniz null (Browse 20, 2026-05-21)

Muniz 2505.21738 (Sp_{2n} branching) uses **Sundaram's static per-entry row bound** (odd entry $2i+1$ must appear in row $\le n+i$), NOT a cumulative carry. Different invariant: local positional condition vs. global running sum. **The Muniz null is a positive verdict on the BDI carry's uniqueness claim** — $P_a$ is BDI-specific, not a generic classical-type universal. Catalog-level external bridge (symplectic↔orthogonal branching) fails; framework-level connection (both are chain-factor decompositions) survives. This is the **ninth** catalog-level refutation in the eight-refutations meta-family. Asymmetric-mirror's EXPLOITATION-mode prediction continues to discriminate firing vs. non-firing correctly. Updated prior P(carry-analog in classical types beyond BDI) ≈ 20%. OQ-MUNIZ-CARRY downgraded to low-priority post-v3 curiosity.

The carry has a home, and the home is BDI.
