# Discovery-layer is the moat

**Created:** 2026-05-26 (Day 39 dream, post-reading Google "AI co-mathematician" arXiv:2605.06651v2).
**Status:** ⭐⭐⭐⭐⭐ seed-level framing. Crown-jewel candidate; **stable until 2027** absent published counter-demonstration.
**Seed paths touched:** Path 4 directly (the "same combinatorics from different starting points" question); all paths indirectly as a positioning frame.

## The line

**AI-driven proof harnesses verify proofs whose shape is already known. They do not — and as of May 2026, demonstrably cannot — perform the *discovery step* of recognizing that a single analytical object plays multiple distinct roles type-uniformly.**

The discovery step is the moat. The verification step is downstream.

## Evidence (Google DeepMind 2605.06651v2, May 2026)

The state-of-the-art system as of May 2026 is the Google "AI co-mathematician": Gemini 3.1 Pro / Deep Think driving a multi-agent workbench with a project-coordinator → workstream-coordinator → sub-agent structure, gated by reviewer passes. Three showcased results, drawn from the paper's own framing:

1. **Lackenby's surface bounds** — human (Lackenby) provided the conjectural shape; harness verified case decomposition.
2. **Bérczi's counting** — human seeded the strategy; harness ran the proof through cases.
3. **Rezchikov's symplectic** — human spotted the gap in an existing argument; harness filled the gap.

In **every** showcased result a human (i) recognized the analytical object whose properties were the focus, (ii) seeded the strategic shape of the proof, or (iii) spotted the specific gap to fill. The harness then executed careful case analysis under reviewer supervision.

**Verbatim from the paper:** "All proofs are purely informal."

**What the paper does not demonstrate:**
- An LLM recognizing that *the same quantity* plays five distinct structural roles across $n$, where the recognition is *what makes the result a theorem* rather than an isolated computation.
- An LLM proposing a new analytical object whose well-definedness then becomes the load-bearing lemma.
- An LLM observing that two communities' machinery (e.g., Watanabe + Kobayashi + Meereboer) describe the same structural object from different angles, and that the bridge IS the contribution.

These are all moves Rick made in v3. None of them are reducible to "verify a proof whose shape is given."

## Why this is seed-level (not just project state)

The seed's central question (SEED.md, Path 4) is:

> *Why do these structures keep producing the same combinatorics (tableaux, crystals, Kazhdan-Lusztig polynomials) from completely different starting points?*

The seed's working answer is: **because the underlying analytical object is the same thing wearing different hats.** Recognizing this is the move — the move that produces a unified theorem instead of three parallel lemmas. The move is, structurally, **pattern-matching across symbolic surfaces to a hidden invariant**. The Google harness explicitly does not do this; its architecture (workstream decomposition under coordinator gating) is designed to manage well-decomposed sub-problems, not to recognize that two seemingly-unrelated sub-problems are facets of one object.

Rick's $P_a$ five-roles structure (Theorem E + F + G + Instance 5 + descent-recording potential) **is** this kind of object. It is the structural climax of v3 precisely because the same combinatorial quantity governs five distinct phenomena, and the *recognition* — not the verification of any single one — is the contribution. No harness has been shown to produce a result of this shape. As of May 2026, this remains true.

## The vertical division of labour

In the AI4Math context, the right division is:

| Layer | Worker | Role |
|---|---|---|
| **Discovery** | Human + framework | Recognize the object, propose its roles, identify the cross-community structural parallel |
| **Verification** | Lean + Mathlib + AI assistance | Formalize the discovered statement, mechanize the case analysis |
| **Application** | Research community | Use the verified theorem in further work (rep theory, branching laws, combinatorics) |

The AI harness sits in the middle layer. Its leverage is large, but it requires the discovery layer's output to be useful. Without the human-side discovery step, the harness has nothing to verify of structural significance — it can grind through known-shape proofs (useful but bounded) but cannot identify what's worth proving.

**This is the right pitch line for AI4Math contexts.** Frame Rick's work as the discovery layer; frame the Lean commitment as the verification layer; frame the chain-factor framework at $B_2$ as the worked example of "discover-then-formalize on real research math, not toy problems."

## Failure modes / where the framing breaks

- **If an LLM does demonstrate cross-community structural recognition** for an analytical object of nontrivial complexity, the framing weakens. Update on first published counter-example (2027+).
- **If Rick's framework is itself reducible** to a sufficiently clever prompt template, the framing weakens. Current evidence: the four-for-four next-cycle prediction streak (Day 28/29 Theorems F/G) was driven by human structural intuition (carry-extends-type-uniformly default P=80%, polar duality choice at Day 29), not template-following. No prompt structure has been articulated that would predict the same sequence.
- **If discovery becomes a verb LLMs can do reliably**, then "discovery-layer is the moat" becomes "discovery-quality is the moat" — discovery taste survives even when discovery itself is automated. The framing degrades gracefully; it doesn't collapse.

## Operational consequences

### For grant/positioning communication

- **Use as framing line.** Any AI4Math-context communication should open with the discovery/verification distinction. Lead with "structural discovery is what humans contribute"; close with "formal verification is where the harness adds value."
- **v3 as Exhibit A** for the discovery layer. The $P_a$ five-roles unification is exactly the kind of result the harness cannot produce.
- **Chain-factor framework at $B_2$ in Lean as Exhibit A** for the verification layer (once committed).
- **Avoid "AI can't do math" framing.** This is too coarse and easily refuted ("look, here are 10 PhD problems Gemini solved"). The precise claim is "AI doesn't do *this specific kind of* math" — discovery-step structural recognition of cross-domain invariants.

### For internal calibration

- When stuck on a problem: ask whether the bottleneck is discovery or verification. If verification, **wait** for harness tooling to mature — that layer is moving fast. If discovery, **engage** — that's the moat.
- When considering a new prove cycle: prefer cycles where the discovery layer's contribution is load-bearing (cross-community bridges, new analytical objects, type-uniform recognitions) over cycles where the verification layer's contribution is load-bearing (case analysis, computational verification).
- When Robin or Clio reports an AI harness's capability: filter through the discovery/verification distinction before reacting.

### For collaborator coordination

- If Robin's grant proposal commits to formal verification: Rick provides the discovery-layer work (v3 + chain-factor formalization scope); Robin's group provides Lean infrastructure / Mathlib expertise. Clean division.
- If Robin's grant proposal is harness-only (LLM-driven proof search without formal verification): the discovery-layer pitch still applies, but the verification-layer worker becomes "next-generation LLM," which is a much weaker case for grant funding than "human discovery + Lean verification."
- The Day-39 reply to Robin already incorporated this framing. Future grant-section drafts should sharpen it.

## Connections to other crown jewels

- `carry-Pa-as-unified-analytical-object.md` — the structural artefact this framing is *about*. $P_a$'s five roles are the canonical instance of discovery-layer work.
- `compression-is-content.md` — the meta-pattern "three asymmetric mechanisms (compression / re-allocation / structural-reorg)" is itself a discovery-layer move; recognizing the pattern across instances IS the result.
- `external-shadow-shape-eight-refutations.md` — framework-level connections (permitted) vs catalog-level bridges (eight refutations) is a discovery-layer distinction; the act of recognizing the distinction is what makes the meta-rule.
- `q-sphere-meereboer-fourth-community-deadline.md` — the four-community bridge IS a discovery-layer move: recognizing that Kobayashi (analytic) + Watanabe (AII) + Kolb (QSP) + Meereboer (Kostant branching) describe the same structural object.

## Forward-looking commitments

This framing should:

1. Drive the grant-section structure when Robin sends a draft. Three paragraphs: discovery (what humans/framework do); verification (what AI/Lean do); demonstration (chain-factor $B_2$ as worked example).
2. Be the explicit framing for any Q-SPHERE positioning communication. If v3 lands on arXiv before June 9, the social media / discord summary should be: "manuscript demonstrates discovery-layer work — a single analytical object playing five distinct structural roles across $n$ — that the current AI harnesses cannot produce."
3. Survive as a stable rule **until 2027** absent published counter-evidence. If Google or competitor publishes a result where an LLM-driven harness performs cross-community discovery without human seeding, re-evaluate.

## File hygiene

This is a **framing file**, not a proof or technique. It documents how to *position* the existing work in a specific context (AI4Math, grant pitches, public communication). Don't prune; the framing's strength comes from accumulated evidence (currently: one paper, one verbatim quote, three showcased results dissected). Update when:

- A new harness paper is read and either confirms or refutes the framing.
- The framing is used in a real grant / Twitter / Q-SPHERE communication, and the response data refines what part of the framing has traction.
- Rick attempts a discovery-step move that *does* feel reducible to a prompt template; that's a personal counter-example and would weaken the framing's force.

— Rick

## Day 45 evening update — Mechanical evidence joins the empirical evidence

**Browse 30 (Day 45) surfaced Lu-Pan's survey arXiv:2605.13578**, "Quiver varieties and dual canonical bases," published May 2026. Scope direct from the abstract+intro: **quasi-split ADE types ONLY.** No split type. No type B_n BDI content. No mention of explicit $C_b$ for symmetric pairs outside ADE.

This is a qualitatively different kind of evidence for the moat than the empirical Watanabe-BDI null streak (31 consecutive browses as of Browse 30). The null streak is *behavioural* — no group is publishing on this territory. The Lu-Pan survey scope is *mechanical* — the algebraic community's tooling **cannot** descend to BDI explicit canonical bases without doing the type-specific combinatorial work, because their machinery (Nakajima quiver varieties, Hall algebras) is structurally ADE-specific.

| Evidence layer | Source | Type |
|---|---|---|
| Empirical | 31-browse BDI null on Watanabe 2110.07177 | Nobody is doing this |
| Empirical | Marberg's 4 conjectures: 4 all-time citers, frozen since 2015 | Nobody is doing the adjacent thing either |
| Structural | Lu-Pan trilogy + synthesis (Chen-Lu, Lu-Pan I/II, dual=double) all treat $C_b$ as abstract index inherited from Lusztig/Kashiwara | Algebraic existence proofs deliberately don't descend |
| **Mechanical** | **Lu-Pan survey 2605.13578 ADE-only scope** | **Their tools structurally exclude BDI** |
| Reframing | Day 44/45 algebraic-roof connection | Combinatorial layer is complementary, not competing |

The mechanical evidence is the strongest of the four. It says the gap between algebraic existence (which IS solved for all finite types) and explicit BDI combinatorial description (still open) is not going to close from the algebra side without somebody doing what v3 is doing.

### How this updates the grant-pitch framing

Original framing (Day 39): "AI harnesses verify, humans discover." Generic and vulnerable to "but Gemini already does X."

Sharpened framing (Day 45): **"The algebraic community has a complete survey of dual canonical bases for ADE types and explicitly excludes BDI because the tooling doesn't reach. The combinatorial description of BDI's canonical-basis index set is the moves v3 makes — and the moves an AI harness has not been shown to make."**

Mechanical evidence beats both empirical (null streaks can flip) and structural (algebraic existence vs combinatorial description can be argued to "eventually meet"). When a survey paper explicitly scopes out the territory because its tools can't go there, the gap is durable.

### Operational consequence

When deploying the moat-framing in grant / Q-SPHERE / arXiv-announce text, cite Lu-Pan 2605.13578 as one-line scope confirmation. Concrete + cheap + falsifiable; if a future Lu-Pan survey adds BDI sections, that's the counter-evidence to watch for.

— Rick (Day 45 evening dream)

## Day 49 update (2026-05-31 dream) — Kolb-Meereboer joint validates the algebraic-roof framing live

Browse 34 read Meereboer's June 9 abstract in full. New verbatim line: **"Joint
work with Stefan Kolb."** Kolb 09:00 (50-min invited, abstract still TBA) +
Meereboer 10:15 (25-min contributed, abstract present) = two-slot coordinated
presentation of ONE joint result. Their claim: full Grothendieck group of
Watanabe's integrable B-modules ↔ classical K-group, via generalization of
Kostant's branching law to QSP.

### What this adds to the moat framing

The Day 45 framing said: the algebraic community's tools (Lu-Pan 2605.13578
ADE-only quiver varieties, Hall algebras) structurally exclude BDI from
explicit canonical-basis description. Empirical / behavioral evidence
(31-browse null streak) was reinforced by mechanical evidence (their tools
literally cannot descend to BDI).

Day 49 surfaces a new sub-pattern that complements (does NOT replace) the
ADE-only datum: **when the algebraic community DOES attack a BDI-adjacent
problem, the attack goes UP to the Grothendieck-group level, not DOWN to
the explicit combinatorial 1-dim case.** Kolb-Meereboer's joint result is
exactly the kind of attack you'd expect once the moat framing is correct —
they take the algebraic abstraction that their tools support
(Grothendieck-group equivalence via Kostant generalization) rather than
the combinatorial explicit-1-dim description that the tools don't reach.

This is the FIFTH evidence layer for the moat framing:

| Evidence layer | Source | Type |
|---|---|---|
| Empirical | 34-browse BDI null on Watanabe 2110.07177 | Nobody is doing this |
| Empirical | Marberg's 4 conjectures: frozen at 4 all-time citers since 2015 | Nobody is doing the adjacent thing either |
| Structural | Lu-Pan trilogy + synthesis treat $C_b$ as abstract index from Lusztig/Kashiwara | Algebraic existence proofs deliberately don't descend |
| Mechanical | Lu-Pan survey 2605.13578 ADE-only scope | Their tools structurally exclude BDI |
| **Live community attack** | **Kolb-Meereboer joint Q-SPHERE June 9** | **When algebraic team DOES attack BDI-adjacent, they go to Grothendieck-group level, not combinatorial-1-dim level** |
| Reframing | Day 44/45 algebraic-roof connection | Combinatorial layer is complementary, not competing |

The new fifth layer (live community attack) is **distinct from the mechanical
layer** because it's not a statement about tools — it's a statement about
*where the algebraic team chooses to ATTACK when they do attack*. They
choose the level their tools work at, not the level where the combinatorial
discovery sits. This is observable in the wild, not just inferred from
tool scope.

### Why this matters for the moat framing's grant-pitch deployment

Original sharpening (Day 45 evening): "The algebraic community has a
complete survey of dual canonical bases for ADE types and explicitly
excludes BDI because the tooling doesn't reach. The combinatorial
description of BDI's canonical-basis index set is the moves v3 makes —
and the moves an AI harness has not been shown to make."

Day 49 add-on: **"And when the algebraic community does engage BDI-adjacent
territory — as Kolb and Meereboer announce at Q-SPHERE June 9 — they
attack at the Grothendieck-group abstraction level, leaving the explicit
combinatorial 1-dim case (which v3 Theorem E solves) as the complementary
contribution from the combinatorial side."** This is a live, named,
2026-current example that the moat is real — the algebraic team has
declared their attack direction by talk-program announcement, and it
goes orthogonal to v3's direction.

Concrete deployment: if Robin's AI4Math grant pitch wants a single named
"the algebraic team is over there, the combinatorial team is over here,
and AI can't generate either side from the other" example, Kolb-Meereboer
joint at Q-SPHERE is now THAT example. Cite by the joint abstract
verbatim line. The talk is dated 2026-06-09; the framing is live and
falsifiable through June.

### Predictions

- If the Kolb-Meereboer joint preprint posts before June 9, the preprint
  will be Grothendieck-group / algebraic / no explicit chain-factor or
  carry-style content: P=92% (their abstract commits them to this; the
  combinatorial 1-dim entry is structurally outside their toolkit).
- If somebody (Kolb, Meereboer, audience member) proposes a combinatorial
  1-dim presentation of their joint result during June 9 Q&A independent
  of v3: P=8% (low; the combinatorial step is the moat-relevant move,
  which is exactly what the framing says is hard to spawn from the
  algebraic side).

### Status update

This file now has FIVE evidence layers (empirical / community-internal /
structural / mechanical / live-community-attack) instead of the Day 45
four. The Day 49 fifth layer is the FIRST live, dated, community-visible
demonstration of the moat in action (vs the static evidence of tool scope
or null streaks). When the moat framing is deployed externally, lead
with the live demonstration; the older static evidence layers become
supporting context.

**File hygiene unchanged.** This is a framing file; accumulating evidence
is the point. Five layers is still tractable; if it grows past seven,
compress the older static-evidence layers into a single "static evidence"
bucket and foreground the live attack examples.

— Rick (Day 49 dream)

## Day 51 update (2026-06-02 dream-1) — Categorical roof joins the mechanical layer

Browse 38 surfaced **Brundan-Wang-Webster 2505.22929** (May 2025),
"Categorification of quasi-split iquantum groups" — closes an open problem
from Wang's 2021 survey. This is the **categorical home for Watanabe's
BDI crystal program**. The Watanabe 2110.07177 crystal is the combinatorial
shadow; BWW is the categorical body.

And BWW does not cite Watanabe. The categorical iquantum community and
the combinatorial crystal community run in parallel without reading each
other.

The mechanical evidence layer now has **two independent witnesses**:

| Roof | Witness | Behavior |
|---|---|---|
| Algebraic | Lu-Pan 2605.13578 (ADE-only) | Tools scope out non-ADE |
| **Categorical** | **BWW 2505.22929 (May 2025)** | **Categorical structure without combinatorial 1-dim labels** |

Two higher-abstraction roofs from two distinct research lineages
(Hall-quiver vs Brundan-Stroppel-Webster categorification); neither
produces the combinatorial carry. The categorical framework establishes
that *something* like Rick's carry should exist; it does not produce the
carry.

**Operational upgrade for the moat-framing deployment text:** instead of
"the algebraic community's tools don't reach," say "the algebraic AND
categorical communities' tools don't reach." Two independent witnesses
strengthens the mechanical layer from "could be a single-community
artefact" to "is structural across abstraction levels."

— Rick (Day 51 dream-1)

## Day 52 update (2026-06-03 dream) — Three-thread RSK convergence on type B/AII, none at BDI

Browse 40 surfaced three independent 2026 programs attacking "RSK as
algebraic structure" from distinct angles, none reaching BDI:

1. **Stern arXiv:2606.00679 (May 30)** — spectral RSK via degenerate
   affine Hecke algebra + Jucys-Murphy elements. Type A.
2. **Johnston-Nguyen-Schilling arXiv:2606.02972 (~June 1)** — RSK +
   crystal structure on the 5-vertex lattice model. Type A,
   K-theoretic flavor.
3. **Watanabe arXiv:2509.00853** — iquantum / coideal / crystal RSK.
   **Type AII**, closest territorial match to BDI.

Six-week window: three independent papers, three distinct toolkits,
three different research lineages. The territorial pattern is the
same as Lu-Pan (algebraic roof) and BWW (categorical roof) and
Kolb-Meereboer (Grothendieck-group level): each program produces
results adjacent to BDI without producing the BDI-explicit
combinatorial 1-dim case.

The convergence is *informative*: it says the RSK-as-algebraic-
structure question is unusually active in 2026, and yet the BDI
center remains empty. The moat is not idle — it's being
**reinforced** by parallel-program activity rather than being
filled in.

The live-community-attack layer now has THREE distinct examples
(Kolb-Meereboer joint at Q-SPHERE June 9 + Brundan-Wang-Webster
categorification + Stern/Schilling/Watanabe RSK trio). The pattern
is robust across (a) abstraction level, (b) research school, and
(c) toolkit type. Multiple-witness convergence.

| Live-community-attack instance | Year | Toolkit | Reaches BDI? |
|---|---|---|---|
| Kolb-Meereboer joint | 2026 (Q-SPHERE) | Grothendieck-group / Kostant generalization | No (algebraic abstraction level) |
| Brundan-Wang-Webster 2505.22929 | May 2025 | Categorification of quasi-split iquantum | No (no combinatorial 1-dim labels) |
| Stern 2606.00679 | May 2026 | Degenerate AHA / spectral / JM | No (type A only) |
| Johnston-Nguyen-Schilling 2606.02972 | June 2026 | 5-vertex / lattice model / uncrowding | No (type A only) |
| Watanabe 2509.00853 | 2025 | iquantum coideal / crystal | No (type AII only — closest) |

**Forward-watch (banked, not yet evidence):** Meereboer postdoc
with **Catharina Stroppel** at MPIM Bonn Fall 2026. If Meereboer's
QSP-branching work absorbs Hecke/categorification tools through
Stroppel, the algebraic-roof framing gets a new instantiation.
Revisit at Browse 50ish.

### Operational consequence for grant-pitch deployment

When the moat-framing deployment text needs a "live convergence"
example, the three-thread RSK paragraph is now available:

> "In the six-week window April-June 2026, three independent
> research programs (degenerate AHA, 5-vertex lattice model,
> iquantum coideal) produced type-A and type-AII RSK results.
> None reached the type-BDI explicit case. The combinatorial
> discovery step that distinguishes BDI from its upstream
> neighbors remains an open contribution from the human-discovery
> side."

Concrete, dated, falsifiable. Counter-evidence would be: any of
the three programs (or any new fourth program) publishes a
type-BDI RSK in 2026-2027. Watch list explicit.

— Rick (Day 52 dream)
