# Chain factor framework — natural maximum-$|a|$ scope is $|a|=2$

**Date:** 2026-05-17 (Day 21 evening prove cycle).
**Status:** ⭐⭐⭐⭐ STRUCTURAL META-RESULT. The bracket framework has a structurally-determined ceiling, established by Phase 1 (T1 $C_n$), Phase 2 (T2 $F_4$) ✓ and Phase 3 (T3 $G_2$) ✗.
**Artifacts:** `proofs/2026-05-17-universal-chain-factor.md` (main proof + obstruction), `g2_bracket.py` (9 empirical layouts tested), `cn_check.py` ($C_n$ structural lift), `for-collaborator/2026-05-17-universal-chain-factor-OBSTRUCTED.md`.

## The trichotomy

For a doubly-laced edge $a_{ji} = -m$ between simple roots, the chain factor $\mathcal{C}_a$ of v2 generalises as:

| $m$ | Type | Interior length | Mid framing | Bracket framework |
|-----|------|-----------------|-------------|--------------------|
| 0, 1 | simply-laced (Watanabe (S1)–(S3)') | 0 (no interior) | trivial | trivial (Watanabe Prop 5.1.1) |
| 2 | doubly-laced ($B_n, C_n, F_4$) | 1 (single mid) | $)^M\,(^{2B}\,)^{2T}\,(^M$ | **v2's chain factor — clean** |
| ≥ 3 | triply-laced+ ($G_2$, hyperbolic) | $\geq 2$ (two+ mids) | no clean framing | **STRUCTURALLY OBSTRUCTED** |

Watanabe's $|a| \leq 1$ boundary corresponds to "no interior." v2's $|a| = 2$ corresponds to "one interior, framed by mid." Past $|a| = 2$ there is no analogous framing — the chain has two interior positions with non-zero $\alpha^\vee$-pairings ($-1$ and $+1$ at $G_2$), and any bracket layout collides under Kashiwara axioms.

## The $G_2$ obstruction (concrete witness)

At $G_2$, the length-4 chain through $\alpha_1$-action runs $\{3\beta_1+\beta_2,\ 2\beta_1+\beta_2,\ \beta_1+\beta_2,\ \beta_2\}$. Pairings with $\alpha_1^\vee$ are $\{-3, -1, +1, +3\}$ — two interior positions with non-zero pairings.

Consider two partitions at weight $4\alpha_1 + 2\alpha_2$:
$$
\pi_A = \beta_1 + \beta_3 \quad\text{(low-mid + top)}, \qquad \pi_B = 2\beta_2 \quad\text{(2 × hi-mid)}.
$$
Both carry 4 closers + 2 openers in any layout where $\beta_k$ contributes $k$ closers + $(m-k)$ openers per copy. In any layout where neither set cancels:
- $f_1\pi_A \to \beta_2 + \beta_3$ (cancel one `(` at low-mid level),
- $f_1\pi_B \to \beta_2 + \beta_3$ (cancel one `(` at hi-mid level).

Kashiwara injectivity for $f_1$ is violated. Empirically: 9 candidate layouts, 0 valid Kashiwara crystals. The "best" layouts (NESTED, the natural v2 generalisation) achieve 110/110 eps-drop but only 100/126 $e_i f_i = \mathrm{id}$ — failures clustered on the $\pi_A, \pi_B$ obstruction pair.

## Why this is the right kind of result

This is not "v2 doesn't extend." It's **"v2 sits at the natural boundary of a clean framework."** The boundary is structurally determined: it corresponds exactly to "interior length 1 in the chain." This is itself a clean publication-grade observation — the chain factor framework's scope is precisely doubly-laced.

Compare to the algebraic-level jump documented in JLW Ex 5.1.5 (8th refutation note): $m=2$ iSerre relations have 3 monomials, $m=3$ has 4 monomials. The crystal-level jump is **qualitative**, not just quantitative — the framework doesn't merely become more complex, it breaks.

## What this kills, what it preserves

**Killed:** v3 sequel paper covering $G_2$ via "universal chain factor." The natural extension dies at $m=3$. Bao-Wang $\psi$-crystals, depth-labeled bracket alphabets, or Kolb coideal categorification might recover $G_2$ — but in a fundamentally different framework, not as an extension of v2.

**Preserved:** v2 ($B_n$, $m=2$, short-long edge) and its lifts to $C_n$ (E↔F relabeling) and $F_4$ middle-edge are completely unaffected. The chain factor framework is now also explicitly type-symmetric (position-independent in the diagram).

## Calibration

- **Whiskey rule reinforced:** The framing was the work. Once the framing was right ($m$-fold doubled brackets in the natural extension), the obstruction came out clean: 9 layouts tested, structural reason identified, all in one prove cycle. The "right framing" sometimes means "right framing for the natural negative result."
- **PROVE.md F-pitfall hit:** F5 (the rule dissolves at higher rank) WAS triggered for the conjecture (universal chain factor). Caught at $m=3$, not arbitrarily large $m$ — and the reason is structural, not technical. This is the cleanest possible F5 hit.
- **Watanabe's stopping point is now interpretable.** Watanabe stopped at $|a| \leq 1$ for what looked like a methodological choice (the (S1)-(S3)' axiomatic framing requires it). The Day-21 result shows it's a **structural inevitability**: the bracket framework simply doesn't generalise past $|a|=2$. The choice was forced.

## What it adds to v2

**A "scope remark" can now go into v2.** Something like:

> *Remark (Scope of the bracket framework).* The chain factor $\mathcal{C}_a$ generalises across the family of doubly-laced edges ($|a_{ji}| = 2$): the same bracket block describes the chain ι-crystal at $B_n, C_n, F_4$ middle edge, under the obvious relabelling. It does not extend to $G_2$ ($|a| = 3$): the length-4 chain has two interior positions with non-zero simple-coroot pairings, and any natural generalisation of the bracket layout forces injectivity violations under $f_i$. The bracket framework's natural scope is exactly the doubly-laced case.

Adds ~half a page; situates v2 as the *natural extension to the structural ceiling* rather than an arbitrary stopping point.

## Open question for v3 (if ever)

**OQ-G2:** Is there a *non-bracket* framework for $G_2$ chain factor? Candidates: (i) depth-labeled bracket alphabets (one bracket type per interior position); (ii) Bao-Wang $\psi$-crystals (one categorical level up); (iii) Kolb coideal categorification (2-categorical). All would be fundamentally different machines, not v3-as-extension. **Not on the active roadmap.**

— Rick, 2026-05-17 Day-21 evening.
