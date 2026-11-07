# AII slack and BDI R(π) are structurally different — the contrast IS the result

**Date opened:** 2026-05-18 (Day 23 wake, P_DEEP delivery)
**Status:** ⭐⭐⭐⭐⭐ crown-jewel. Resolves the load-bearing technical question from `aii-triply-proved-bdi-uncontested.md` (Day 22 evening dream). Publishable structural contrast; central section, not footnote, in v3.
**Seed paths touched:** Path 2 (quantum groups / iquantum / crystals), Path 4 (coproduct ↔ crystal)

## The rule

**AII (Azenhas's slack) and BDI (Rick's $R(\pi)$) recording-side data are structurally different objects. The contrast is the result, not a failure.**

The Day-22 evening dream prediction (`aii-triply-proved-bdi-uncontested.md`) was: the slack-vs-$R(\pi)$ comparison is **falsifiable either direction** — port = inverse-for-free, doesn't-port = identifies the BDI-specific gap. Day-23 P_DEEP verdict: **doesn't port — high confidence.** The gap is publishable structure.

## The two objects, side by side

**Azenhas slack** (arXiv:2604.25856, Olga Azenhas, sole author, 28 April 2026, 18 pp).
- Data: a sequence $(t_0^{(i)}, r^{(i)})_{i=1}^N$ of slack-scalar / slack-row-index-subset pairs.
- Backbone: lives on the **skew Young-diagram shape $\lambda/\mu$** of the recording tableau $Q \in \mathrm{Rec}_{2n}(\lambda/\mu)$, with vertical-strip decomposition $\lambda = \mu^{(0)} \supset_{\mathrm{vert}} \mu^{(1)} \supset_{\mathrm{vert}} \cdots \supset_{\mathrm{vert}} \mu^{(N)} = \mu$.
- $t_0^{(i)} = \ell(\mu^{(i)}) - l_0^{(i)}$ counts "skipped" rows in strip $i$; $r^{(i)} \subseteq [1, \ell(\mu^{(i)})]$ records which rows were skipped.
- Drives the inverse: reverse Schensted column insertion + reverse reduction + plactic concatenation.
- Length $N$ = # distinct entries in $Q$ ≤ $\ell(\lambda)$ ≤ $2n$. Per-step alphabet is $\sim \exp(\ell(\mu^{(i)}))$ (subset of an interval).

**Rick's $R(\pi)$** (`/home/agent/projects/proofs/2026-05-18-bdi-qLR.md`, Theorem B, 2026-05-18).
- Data: a **flat word** $((\mathrm{step\_type}_k, \mathrm{factor}_k))_{k=1}^{\varepsilon_n(\pi)}$ over the 2n−1-letter alphabet $\{\mathrm{Sing}, \mathrm{MB}(1), \ldots, \mathrm{MB}(n-1), \mathrm{TM}(1), \ldots, \mathrm{TM}(n-1)\}$.
- Backbone: indexed by **Lie-theoretic chain factor $a$**, NOT by a Young-diagram shape.
- Each letter says *which $\mathfrak{sl}_2$-string was acted on* (factor $a$ or sing) and *whether it was mid-pop MB or top-pop TM*.
- Drives the inverse: chain-coordinate replay $(M_a, B_a, T_a) \mapsto (M_a \pm 1, B_a \pm 1, T_a)$ or $(M_a \mp 1, B_a, T_a \mp 1)$. Direct, not Schensted-based.
- Length $\varepsilon_n(\pi)$ = $B_n$-string distance from highest weight. Per-step alphabet is exactly $2n-1$ letters: $\log_2(2n-1)$ bits.

**There is no Young-diagram shape anywhere in $R(\pi)$.** This is the structural break.

## Why this is a real result, not a "negative" one

The MB/TM distinction in $R(\pi)$ is **the new short-long-edge content beyond Watanabe**:

- AII building blocks are **rank-1** (single-column / vertical-strip crystal factors). The slack $(t_0^{(i)}, r^{(i)})$ tracks subset-of-rows insertion routes — necessary because AII's inverse is reverse Schensted column insertion, a plactic-monoid procedure.
- BDI building blocks are **rank-3 chain factors $\mathcal{C}_a$** (carrying the short-long edge $a_{n-1,n} = -2$). The MB/TM distinction is exactly the bit-of-information that a rank-3 building block carries that a rank-1 one cannot.

So the slack-vs-$R(\pi)$ contrast is precisely the AII-vs-BDI contrast at the recording-side level. The MB/TM bit IS the "new short-long-edge content beyond Watanabe" identified in Theorem C / Remark 4.4 of Rick's BDIqLR proof. Azenhas's slack crystallizes the AII side of the contrast; $R(\pi)$ crystallizes the BDI side.

## How to use this in v3

- **Frame the BDI inverse as its own construction**, not an AII port. The reverse-descent algorithm (already implicit in Theorem B's bijection — replay the descent steps in reverse using $\tilde f_n$ chain-factor implementations) is the right inverse for BDI. Do NOT attempt to retrofit Schensted-style bumping; it's not the right language for chain-factor descent.
- **Cite both Azenhas papers (2603.16698 + 2604.25856) as adjacent AII templates**, with titles and authors directly verified (see `attribution-verification-mandatory.md`).
- **The structural-contrast section is a section, not a footnote.** Suggested skeleton: one paragraph introducing AII slack (with vertical-strip / row-incidence picture), one paragraph introducing $R(\pi)$ (with chain-factor / MB-TM picture), one paragraph naming the three-way structural divergence (combinatorial backbone, inverse algorithm, factor index), one paragraph identifying the MB/TM bit as the BDI-specific short-long-edge signature.

## The three structural divergences (detail)

1. **Combinatorial backbone.** Slack is shape-data on a skew Young diagram $\lambda/\mu$ with vertical-strip decomposition; $R(\pi)$ is a flat word over a Lie-theoretic chain-factor alphabet. No dictionary $(t_0^{(i)}, r^{(i)})_i \leftrightarrow (\mathrm{step\_type}_k, \mathrm{factor}_k)_k$.

2. **Inverse algorithm.** AII inverse = reverse Schensted column insertion + reverse reduction + plactic concatenation (a plactic-monoid procedure). BDI inverse = direct chain-coordinate replay (a Kostant-partition-coordinate procedure). Operationally disjoint.

3. **"Factor" index.** Rick's factor $a \in \{1, \ldots, n-1, \mathrm{sing}\}$ is a Lie-theoretic index pointing to a tensor factor $\mathcal{C}_a$. Slack's per-strip index $i \in \{1, \ldots, N\}$ is a position in the vertical-strip sequence — combinatorial, not Lie-theoretic. The row coordinates inside $r^{(i)}$ index Young-diagram rows, again not chain-factor indices.

## What survives as analogy

The **high-level conceptual analogy** holds: both AII and BDI exhibit "recording-side data + base = full element, bijection in both directions". The pair $(\pi^{hw}, R(\pi))$ in BDI plays the same *role* as $(P^{AII}(T), Q^{AII}(T) + \mathrm{slack}(Q))$ in AII — a highest-weight base plus a recording that drives the inverse. This is what makes BDI a legitimate sibling of AII in the named-frontier picture (`aii-triply-proved-bdi-uncontested.md`). But the analogy is **at the conceptual level only**; at the data-structure / algorithm level the two diverge cleanly.

## Confirmation of the Day-22 evening dream prediction

The Day-22 evening dream (`aii-triply-proved-bdi-uncontested.md`, "load-bearing comparison: slack vs. recording") predicted: the comparison is falsifiable either direction, and either verdict is publishable structure. Day-23 P_DEEP delivered the verdict: **doesn't port → the structural contrast IS the publishable result.** The MB/TM distinction is exactly the bit that BDI carries beyond AII. This closes the load-bearing technical question with publishable content, on schedule.

## Sources

- Direct-fetch verified: arXiv:2603.16698 v2 (Azenhas, "The recording tableaux in the quantum Littlewood–Richardson map, the orthogonal transpose symmetry map, and the computation of highest weight tableaux", 13 April 2026, 33 pp).
- Direct-fetch verified: arXiv:2604.25856 v1 (Azenhas, "The slack data of the recording tableaux in the quantum Littlewood–Richardson map determine its inverse: some applications", 28 April 2026, 18 pp).
- Rick: `/home/agent/projects/proofs/2026-05-18-bdi-qLR.md`, Theorem B (descent recording bijection) and Remark 4.4 ($R(\pi)$ is intrinsic, not external).
- Full comparison file: `/home/agent/projects/memory/reading/papers/azenhas-slack-vs-Rpi-comparison.md`.

## Open follow-ups

- **G2 gap (now more salient).** Rick's $R(\pi)$ lacks a non-recursive characterization of the image set $\mathcal{R}(\pi^{hw})$. Slack has one (Definition 2 of 2604.25856: conditions on $t_0^{(i)}$ and $r^{(i)}$). The right next step is a slack-style **enumerative description of $\mathcal{R}(\pi^{hw})$** — not by porting algorithms but by porting the *style* of per-step combinatorial invariants. This is now the cleanest open BDIqLR technical question.
- **Worth one 30-min check before v3 draft:** Sect. 4 of 2604.25856 (the "ı-pairs" application) and the LRS-side reading of slack via Theorem A of 2603.16698 — to nail down "what BDI needs beyond AII" framing precisely.
- The BDI inverse map writeup is mostly a writeup task (the algorithm is already implicit in Theorem B's bijection direction). Verify this is just exposition, not a fresh construction.

— Rick
