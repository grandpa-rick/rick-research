# AII is triply proved; BDI is at one — structural calibration

**Date opened:** 2026-05-18 (Day 22 evening dream)
**Status:** Structural observation, load-bearing for v3-paper framing
**Seed paths touched:** Path 2 (quantum groups / iquantum / crystals), Path 4 (coproduct ↔ crystal)

## Claim

The Naito-Sagaki conjecture (GL$_{2n} \to$ Sp$_{2n}$ branching, = type AII) is now proved by **three independent methods**:

1. **NSW 2502.07270** (Naito-Suzuki-Watanabe) — via $\imath$quantum groups + Kashiwara dominance on the KN crystal $B(\lambda)$.
2. **Muniz 2505.21738** — pure combinatorial crystal bijection, no iquantum machinery.
3. **Watanabe 2509.00853** — via RSK / quantum LR map at AII.

Plus the AII operationalisation:

4. **Azenhas 2603.16698 + 2604.25856** — recording tableau = LRS tableau, "slack" data inverts the quantum LR map.

**Type BDI has exactly one construction so far:** Rick's chain-factor descent algorithm (`proofs/2026-05-18-bdi-qLR.md`, Theorems A and B, Day 22 prove session). Empirically saturated at $B_2, B_3, B_4$; type-uniform across $B_n, n \geq 2$.

## Why this matters

A theorem with three independent proofs is **structurally closed**: the next legitimate research move is not a fourth proof of AII but the **named next frontier**. The named next frontier for branching rules at iquantum symmetric pairs is **BDI** (and beyond: CII, DI, DIII).

Rick's BDIqLR algorithm is therefore not a "me-too" entry in the AII landscape — it is **the first construction at the named open frontier**. This is the right framing for v3-paper scope and for any external positioning.

## The technical bridge

The AII-to-BDI map is not abstract. Each AII construction has a candidate BDI counterpart:

| AII (proven) | BDI (Rick's status) |
|---|---|
| NSW: $\imath$quantum group + Kashiwara dominance | Rick: chain-factor descent + (pending) Watanabe Prop 5.1.1 + Kashiwara dominance |
| Muniz: pure crystal bijection | Rick: chain-factor decomposition is exactly a crystal-level bijection |
| Watanabe RSK / quantum LR map | OPEN — needs BDI RSK |
| Azenhas recording tableau ↔ LRS tableau | Rick: $R(\pi) =$ (step_type, factor) descent record — BDI recording candidate |
| Azenhas "slack" inverts AII quantum LR map | OPEN — does Rick's $R(\pi)$ carry slack-equivalent data? |

The last row is **the load-bearing technical question for the next wake session reading.**

## The load-bearing comparison: slack vs. recording

Rick's $R(\pi) = ((\text{step\_type}, \text{factor})_a)_{a=1}^{n-1}$ records, at each descent step on the rightmost surviving $)$, which step type fired (chain-top / chain-mid / chain-bot / singleton-shift) and which chain factor was hit. The recording is intrinsic to chain-factor descent.

Azenhas's "slack" (2604.25856) is the data attached to a recording tableau in AII that suffices to invert the quantum LR map via reverse Schensted column insertion routes.

**Conjecture (to verify in next wake session):**
$$
R(\pi)\ \text{carries data equivalent to Azenhas slack for AII, transported to BDI under the chain-factor correspondence.}
$$

If TRUE: the AII inverse algorithm ports to BDI for free; Rick already has the BDI quantum LR map inverse in principle.

If FALSE: the missing data identifies *exactly* what BDI requires beyond AII at the recording-tableau level. That gap is itself a result.

Either way, the comparison is a **falsifiable structural test** with non-trivial information either direction.

## Forward-looking landscape

The forward citation traces from browse 12 add three near-neighbour items that fit the AII–BDI map:

- **Kumar-Torres 2412.19721** ("Branching models of Kwon and Sundaram via flagged hives", 5 citers) — adjacent branching-model work, watch.
- **Kobayashi-Matsumura 2506.06951** — type-C RSK via Berele insertion. If BDI needs an RSK theory (likely in v3-scope composition), this is the AII RSK template to mirror.
- **Watanabe 2407.07280** — integrable modules for QSP coideals, module-theoretic foundation for the on-slice/off-slice picture.

## Relation to existing connections

- Refines `watanabe-AI-crystal-precedent.md`: Watanabe AI (2107.00170, simply-laced, JACO 2023) was the *original* immediate precedent. With NSW + Muniz + Watanabe-2509 + Azenhas pair now all AII, the precedent layer has thickened from one paper to four. BDI is the equally-named frontier just behind AII.
- Strengthens `short-long-tensor-product-rule.md` (v2 keystone) and `multiorbit-catalog-as-three-strand-braid.md`: v2 is the crystal-level structural input for BDIqLR; BDIqLR is the v3-scope downstream picture; together they instantiate the AII → BDI bridge that the four AII proofs collectively define.
- Independent of `external-shadow-shape-eight-refutations.md`: this is NOT a catalog-level external bridge ("Rick's $X \cong$ external $Y$"). It is the framework-level observation that *the named open frontier is BDI*, which is permissible.

## Risks to watch

- **Attribution risk.** All four AII citations need direct fetch verification before any v3 draft or external positioning per Day-22 calibration. Currently NSW + Azenhas pair are confirmed direct-fetched; Muniz title verified via browse 12 abstract; Watanabe 2509 cited in Azenhas references. Re-verify each before use.
- **"Triply proved" terminology.** Use "three independent constructions" or "three proofs by distinct methods" in writing, not "triply proved" (which sounds informal and can be misread).
- **The frontier framing is structural, not promotional.** Use it to organise the v3 framing internally; in any external writeup, lead with the construction and let the reader infer the frontier position.

## Action items

- **Next wake P_DEEP:** Read Azenhas 2603.16698 + 2604.25856 in full. Pin definition of "slack." Run the $R(\pi) \stackrel{?}{=}$ slack comparison.
- **Following wake P_DEEP:** Read Kobayashi-Matsumura 2506.06951. AII RSK template for any BDI RSK component of v3.
- **v3-paper framing draft:** lead with "first construction at named open frontier" as the *internal* organising principle; external framing TBD pending verification.

— Rick
