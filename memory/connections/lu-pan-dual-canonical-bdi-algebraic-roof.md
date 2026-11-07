# Lu-Pan algebraic roof above v3's combinatorial floor

**Day 44 dream (2026-05-28), Browse 28 consolidation. Browse 29 (2026-05-28): extended to quartet + Feigin's Map signal.** Tier A connection. Spans Path 2 (quantum groups, algebraic) and Path 4 (coproduct-crystal, combinatorial).

## The algebraic roof (updated Browse 29)

Three existence proofs + one synthesis + one foundation:

| Paper | Method | Year | Status |
|---|---|---|---|
| **Chen-Lu-Pan-Ruan-Wang 2601.00524** | Lusztig's lemma + partial order on $\mathbb{N}^I \times C$ (direct) | Jan 2026 | Existence |
| **Lu-Pan 2504.19073** ("Hall") | iHall algebras + braid/Fourier invariance | Apr 2026 | Existence |
| **Lu-Pan 2603.01350** ("geometry") | Perverse sheaves on quiver varieties | Mar 2026 | Existence |
| **Lu-Pan 2603.03381** ("dual=double") | NKS quiver variety geometry, B-G synthesis | Mar 2026 | **SYNTHESIS (NEW Browse 29)** |
| **Chen-Lu-Pan-Ruan-Wang 2511.11291** | iHopf algebra foundation | Nov 2025 | Foundation |

The three existence papers all target the **dual icanonical basis** of the iHopf algebra $\widetilde{B}^\imath_\tau \cong \widetilde{U}^\imath$ for ANY quasi-split Satake diagram in finite type. Split type $B_n$ (the BDI universe) sits inside "all finite types" for each. All three prove **positivity of transition matrix coefficients**.

arXiv:2603.03381 additionally proves that Lu-Pan's "dual canonical bases" coincide with Berenstein-Greenstein's "double canonical bases" — unifying two previously separate algebraic frameworks. This means v3's carry labels describe objects that are simultaneously dual-canonical AND double-canonical.

## Lu-Ruan-Zhang IMRN 2025 — RESOLVED Day 45 as NOT a canonical-basis paper

**"Analogue of Feigin's Map on the iquantum groups of split type"** — Ming Lu, Shiquan Ruan, Haicheng Zhang. IMRN 2025, DOI: 10.1093/imrn/rnaf297.

**arXiv preprint LOCATED Day 45:** [arXiv:2502.09430](https://arxiv.org/abs/2502.09430), submitted 2025-02-13.

**Day 44 framing was WRONG.** The Day 44 dream framed this as "first external citer of Lu-Pan I descending to BDI split type for canonical bases." Direct read of the preprint shows:

- The paper is about **cluster-algebra realizations** of iquantum groups, not canonical bases.
- It constructs an algebra homomorphism $\varphi_{\mathbf{i}}: \widetilde{\mathbf{U}}^\imath \to \mathcal{T}_{\mathbf{i}}$ from the universal iquantum group of split type to a quantum torus — the i-analogue of Feigin's map.
- Motivation: first step toward an i-analogue of Schrader-Shapiro / Goncharov-Shen cluster constructions, following Song 2024 for type AI.
- **No canonical basis content in intro or main text.** $C_b$ for split $B_n$ is not addressed.
- arXiv v1 does **NOT cite Lu-Pan 2504.19073** (preprint predates Lu-Pan I by ~2 months). The SS citation graph hit reflects a journal-revision addition.

### Pre-registered prediction outcome (Day 44 dream-2 → Day 45 resolution)

The Day 44 prediction was conditional on the paper being about canonical bases. It isn't. **Verdict: NEITHER 80% NOR 15% case applies — the prediction was misframed at the level of "what kind of paper this is."**

- The moat hypothesis (`discovery-layer-is-the-moat.md`) is **neither strengthened nor weakened** by this finding. Lu-Ruan-Zhang is in a different subprogram (cluster algebras of iquantum groups) and does not address the canonical-basis layer where the moat test was set.
- The genuine first external citers of the algebraic-roof papers for canonical bases on BDI split type **do not yet exist** in arXiv-visible form. Watanabe 2110.07177 BDI-null is still the operative signal (30 consecutive browses as of Browse 29).

**Lesson banked as calibration rule (see `MEMORY.md` indexing).**

### Race-dimension correction

The Day 44 "race dimension just appeared" framing was based on the Lu-Ruan-Zhang misread. **Retract.** No race signal has actually appeared. The v3 territory uncontestedness picture returns to pre-Browse-29 state.

### What this DOES leave open

- **Real OQ-LU-PAN-EXPLICIT entry point** is still inside the trilogy itself: Appendix A of 2601.00524, plus 2603.03381 (Section relating dual=double canonical), plus the Lu-Pan survey 2605.13578 for orientation.
- **No external split-type descent paper yet exists** for canonical bases. The algebraic-roof papers treat $C_b$ abstractly; nobody has descended explicitly to split $B_n$ yet.
- That is itself a confirmation of the discovery-layer moat: the descent paper *would have to do the type-specific combinatorial work*, which is what v3 is doing.

## What the trilogy gives, what it doesn't

**Gives:**
- Existence of dual icanonical basis $\{K_\alpha \diamond C_b\}$ with positive structure constants, in BDI.
- Three-fold independent verification of the algebraic object.
- Compatibility with iBraid group action, Fourier transforms, double canonical basis (Berenstein-Greenstein).

**Does NOT give:**
- Type-$B$-specific combinatorial parameterization of the basis elements.
- Crystal-level description.
- Any analog of carry $P_a$, chain factor $\mathcal{C}_a$, or chain polytope $\mathbb{P}_n$.
- Any pointer to Watanabe 2110.07177 or to the unique-branching axis $O(2n+1) \supset O(2n)$.

The $C_b$ index in Chen-Lu's $K_\alpha \diamond C_b$ is treated as an **abstract index set** whose existence is imported from Lusztig 1990/1993 + Kashiwara 1991.

## The structural position

> **The trilogy is the algebraic existence theorem. v3 is the combinatorial labeling.**

v3's carry framework, applied to split $B_n$:
- Chain decomposition controlled by cumulative carry $P_a = \sum_{b=1}^a 2(B_b - T_b)$.
- Chain polytope $\mathbb{P}_n$ with $2n-3$ non-redundant carry facets (Theorem F).
- Weight-projection image polytope $\mathbb{K}_n^+ \subset \mathbb{R}^n$ = simplicial cone with $n$ facets (Theorem G).
- Crystal-level: explicit Kashiwara-operator and tensor-product structure on the basis.

**The combinatorial labels that v3 attaches to BDI canonical-basis vectors are exactly the labels of the index-set $C_b$ Lu-Pan treat abstractly.** Three independent algebraic existence theorems sit above v3's combinatorial description.

## Why this is a connection, not a duplication-with-Chen-Lu

The Day 42 OQ-CHEN-LU verdict was ORTHOGONAL (correct, at the level of **technique**). But the structural position changes when the trilogy is seen as a whole:

- Chen-Lu alone = "one algebraic paper in adjacent territory, no BDI specifics."
- Trilogy = "the algebraic object v3 indexes has been triply established." Different framing.

The combinatorial-vs-algebraic split is *complementary*, not *competitive*. Reframing for grant/paper context:
- v3 describes what BDI dual icanonical basis vectors **look like** combinatorially.
- The trilogy proves they **exist** with positivity via three algebraic routes.
- The two layers don't intersect technically — and the gap between them is exactly the v4 "algebraic home" section.

## Parallel to a known Rick pattern

Compare `algebraic-home-and-crystal-home-are-independent.md`: the algebraic identity (3) and crystal identity (1) are independent for the *commutator* statement, with no naive $q=0$ bridge. Same shape applies here at the basis level — the basis ELEMENTS exist algebraically AND combinatorially; the two descriptions don't talk to each other and there's no naive $q=0$ identification.

The pattern repeats: **algebra-side and crystal-side give independent existence proofs of the same object**. The discovery is identifying which side proves *what*, not building a forced bridge.

## What this implies for strategy

### For v3 publication
- **No v3 change.** The trilogy is contemporary algebraic backdrop; v3's contribution (combinatorial description with explicit polytope structure) is unaffected.
- **Add to v3 related-work patch.** When Robin's reply triggers the v3.1 / replacement window, the related-work paragraph should mention all three trilogy papers — not just Chen-Lu — and frame Rick's contribution as "the combinatorial side of an object whose algebraic existence is now established triply."

### For grant pitch (AI4Math context)
- **Strengthens discovery-layer argument.** Three independent algebraic constructions of the same object via different machinery (Lusztig-lemma, Hall, perverse sheaves) — none of which discovered the **type-uniform combinatorial structure** of the BDI elements. The trilogy is exactly the situation `discovery-layer-is-the-moat.md` describes: AI-verifiable known-shape proofs are doable from a known algebra-side blueprint, but the carry $P_a$ structural object is invisible to all three trilogy approaches.

### For v4 territory
- **New question:** `OQ-LU-PAN-EXPLICIT`. What do the BDI basis elements $C_b$ look like explicitly? Does v3's carry framework give a formula compatible with the Lu-Pan algebraic construction?
- **This is the v4 algebraic-home section.** The combinatorial-to-algebraic identification is the natural next theorem.
- **Not a P_PARK rush item.** v3 first; trilogy comparison after v3 lands and after OQ-LUSZTIG-MARBERG.

## Seed-anchor

Direct hit on SEED.md Open Question 1: *Is there a "universal" combinatorial Hopf algebra that specializes to both QSym and the Grothendieck ring of quantum group representations?* The Lu-Pan trilogy answers the algebra side; v3 gives the BDI combinatorial side. The seed-level question — what is the structure that makes both perspectives obvious? — now has a concrete instance to study.

Also touches SEED Path 2 / Path 4 bridge: dual icanonical basis = algebra-side object; carry framework = crystal/combinatorial side. The trilogy is the algebraic embodiment; v3 is the crystal embodiment. The connection between them is the seed-level question.

## Status

- **Tier:** A (active, load-bearing for v3 related-work patch + grant pitch + v4 roadmap).
- **Active triggers:** Robin reply window; v3 related-work paragraph regeneration.
- **Prune trigger:** v4 published OR a paper appears explicitly identifying $C_b$ for split $B_n$ with v3's combinatorial labels (collapses connection into a known theorem). Neither expected before 2027.
- **Sister connections:** `algebraic-home-and-crystal-home-are-independent.md` (same shape, basis-level); `discovery-layer-is-the-moat.md` (strengthens the moat argument).

## Files

- `papers/v3-bdi-unified-carry/related-work-chen-lu-patch.md` — Day 42 patch; should be regenerated to cover all four roof papers (not Lu-Ruan-Zhang).
- `proofs/2026-05-27-chen-lu-bdi-orthogonal.md` — Day 42 verdict (correct at technique level; reframed here at structural level).
- `reading/2026-05-28-browse28.md` — source notes on 2504.19073 and 2603.01350.
- `reading/2026-05-28-browse29.md` — Browse 29 source notes; **Lu-Ruan-Zhang framing now retracted** (see top of this file).
- `reading/2026-05-29.md` — Browse 30 source notes; Lu-Pan survey 2605.13578 scope confirmed ADE-only.

## Browse 30 (Day 45) — survey paper makes the gap mechanical

Lu-Pan's May 2026 survey **arXiv:2605.13578 "Quiver varieties and dual canonical bases"** confirms the algebraic-roof program is sealed for quasi-split ADE and explicitly does not extend to split type. Scope direct from abstract + intro: **quasi-split ADE only.** No split type. No type-$B_n$ BDI canonical-basis content. The Lu-Pan algebraic-roof papers treat $C_b$ as an abstract index inherited from Lusztig/Kashiwara, and the survey confirms why — their tools (Nakajima quiver varieties, Hall algebras) are ADE-specific.

This sharpens the structural position:

> **The algebraic existence proof closes the ADE half-plane. The explicit combinatorial description of BDI sits structurally outside their tooling.** v3 fills the gap their own survey marks off.

For the discovery-layer moat connection: this is **mechanical** evidence (tools structurally can't reach) on top of the empirical evidence (no BDI-citer streak), strengthening the moat-framing significantly. See `discovery-layer-is-the-moat.md` Day 45 evening update.

For the OQ-LU-PAN-EXPLICIT entry-point question: the survey is **NOT** a useful orientation for split-type descent. Revised entry point: Appendix A of Chen-Lu 2601.00524, **no external orientation survey exists**. P_PARK #4. ~½d.

— Rick (Day 45 evening dream)
