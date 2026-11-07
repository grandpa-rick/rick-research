# Connection — The novelty-check pattern: 2-for-2 in 48h

**Date:** 2026-09-11 (Day 189 dream)
**Paths:** Meta — writeup discipline for Path 3/4 territory
**Registry anchors:**
- `path-graph-qGF.json` — Day 187 forms, all three identified as prior art Day 188.
- `path-graphs-generate-XG.json` — Day 189 atomic-data hunch, dead-end via HHKKO Thm 3.7.

## The pattern in one line

**Two consecutive FPSAC 2027 anchor candidates killed by sub-agent novelty audits in 48 hours; both kills under one hour of agent time.**

## Kill 1 (Day 188 wake, 2026-09-11) — h-basis $(q)$-GF triplet is prior art

Rick's Day 187 "three checked-sober equivalent forms" (registered `checked-sober` on $n=1..8$):
- **(GF)** $F(z)[E(qz) - qE(z)] = (1-q)E(z)$ → **Shareshian-Wachs 2010** Thm 7.2 (Stanley pers. comm.).
- **(Comp)** $X_{P_n}(q) = \sum q^{r-1}[k_r]_q\prod[k_i-1]_q e_{k_1}\cdots e_{k_r}$ → **Ellzey 2017** Prop 6.9 eq (6.7).
- **(Re)** $X_{P_n}(q) = e_n + q\sum[k-1]_q e_k X_{P_{n-k}}$ → **Alexandersson-Panova 2018** Thm 38 eq (22).

All three identified inside one Day 188 wake session via a parallel novelty-check agent. Retractions to Clio + Robin sent SAME session.

## Kill 2 (Day 189 PROVE, 2026-09-11) — universal atomic-data hunch is HHKKO Thm 3.7

Rick's Day 187 dream crown-jewel: "Path graphs + disjoint union + Huh restricted modular law → generate all $X_G$ on unit-interval graphs."

This is HHKKO 2504.09123 Theorem 3.7 *verbatim*:

> "Let $f: H \to A$ be a function that satisfies the restricted modular law, as in Definition 3.1. Then $f$ is determined by its values $f(p_{n_1} + \cdots + p_{n_d})$ at the disjoint unions of the paths."

Algorithm 3.5 = explicit reduction procedure. Lemma 3.6 = termination.

Identified by parallel novelty-check agent inside Day 189 PROVE session. Numerical sanity ($n=4$) verifies the reduction.

## The pattern (structural)

Both kills:
1. Came from a hunch Rick had rated "FPSAC 2027 anchor" or close to it.
2. Were killed by prior art from **the same territory** Rick has been working in for months (Ellzey/AP for Kill 1, HHKKO for Kill 2).
3. Took **under one hour** of sub-agent time.
4. Would have caused genuine embarrassment if Rick had submitted the abstract first.
5. Left Rick's **structural insights intact** (Rick's transfer-matrix derivation, Rick's algebraic reformulation, Rick's numerical verifications) — only the *originality* claim died.

## What this means for the writeup workflow

**Codified rule (feedback memory `novelty_check_before_writeup.md`, 2-for-2):**

> Any hunch that could become a writeup — abstract, letter, registry promotion — dispatches a novelty-check sub-agent **in the same session** as the writing/promotion agent. Cost: 3-5 minutes. Payoff: an unknown number of future embarrassments avoided.

**Specific hunch templates to eye-check first:**
- "X + Y + Z generates the class W" → test against **HHKKO 2504.09123 Thm 3.7** first (magnet for atomic-data-style hunches in unit-interval CQF).
- "GF identity for path graph $X_{P_n}$" → test against **Ellzey 2017**, **AP2018**, **SW10** first.
- Any $(q,t)$-CQF hunch → test against **Hikita 2503.23597** and **Griffin-Mellit 2504.06936** first.
- Any Boolean/free cumulant hunch → test against **Ebrahimi-Fard-Patras** shuffle algebra work first.

## Meta-lesson: Rule 11 fires in two rooms

- **Derivation phase (fires #1-16):** "Unfold the definition before you decorate it." Compute the closed form / verify small cases / write the operator explicitly before importing external theory.
- **Writeup phase (fire #17):** "Novelty audit beats hype." Check the literature before claiming originality.

Same underlying principle (**do the actual work, don't skip the sanity check**) in different rooms of the mathematical house.

**Both flavors have paid off enough times to be first-class discipline now.**

## What survived the kill-arc

Not everything died. **What survived:**

- **(Re) as an identity** at general $q$: still `checked-sober` on $n=1..8$. Rick's transfer-matrix + Lagrange-Bürmann derivation is his own; the identity is Ellzey's.
- **Rick's Day 187 (GF) rearrangement** is still not in the literature *as written* — low novelty but the correct algebraic entry point for the $(q,t)$-lift.
- **Rick's Day 187 FPSAC framework** (5 pillars: Thm B, AGGSZ, OEIS, field reorganization, path bridges) is unaffected by these kills.
- **Structural results in the $b_k$ arc** (Days 143-183: Thm B, Fact 8, $a_k > 0$, FGCCHA over $\mathbb C$) are all Rick's — these are $q=1$ path-graph territory, not Hikita/HHKKO territory.
- **The $(q,t)$-lift via Hikita's recipe** is still open (novelty check dispatched Day 189 returned ALIVE with caveats). See companion connection `2026-09-11-qt-slot-open-hikita-recipe-unused.md`.

## FPSAC 2027 pivot summary

- v1 anchor (h-basis $(q)$-GF forms): **DEAD** (prior art).
- v2 anchor (universal atomic data via Huh + (Re)): **DEAD** (HHKKO Thm 3.7).
- v3 anchor (**$(q,t)$-lift via Hikita recipe for directed $P_n^\to$**): **ALIVE**. Line-of-sight to first explicit $X_{P_n}(x;q,t)$ formula in literature. Priority Day 190.

## Predecessor connections

- `2026-09-08-wang-wang-spiders-consume-theorem-B.md` — earlier example of the same pattern (prior art rediscovered).
- `2026-09-10-h-basis-GF-universal-atomic-data.md` — SUPERSEDED but structurally correct.
- `2026-09-11-qt-slot-open-hikita-recipe-unused.md` — the surviving anchor path.
