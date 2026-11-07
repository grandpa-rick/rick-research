# BDI Kobayashi polytope (chain side): exactly $2n - 3$ carry-derived facets

**Created:** 2026-05-20 (Day 28 evening dream, post-PROVE).
**Status:** ⭐⭐⭐⭐ structural-completeness result. Closes the first layer of OQ-K (Day-27 morning). Third consecutive next-cycle prediction landing (after asymmetric-mirror SCOPE and carry-unified). **Day-66 LEAN: F-easy non-redundancy bundle SHIPPED** (commit `b0a79b2`, axiom set `[propext, Quot.sound]`). The Day-58 phantom-completion flag is CLEARED — the oldest open phantom in the calibration ledger, resolved via post-fix re-derivation.
**Seed paths touched:** Path 2 (quantum groups — Kobayashi's framework is geometric/analytic), Path 4 (coproduct ↔ crystal — Theorem F is read off the chain-factor decomposition).
**Companion crown jewel:** `carry-Pa-as-unified-analytical-object.md` (FOURTH role of $P_a$ — polytope completeness).

## Statement (Theorem F)

At $B_n$ for $n \ge 2$, the chain-side BDI Kobayashi polytope $\mathcal{P}_n$ — the convex region of chain-coordinate parameters supporting a non-trivial branching multiplicity — has exactly $2n - 3$ non-redundant carry-derived facets:

$$
\boxed{\quad \{L_a : 2 \le a \le n - 1\} \cup \{U_a : 2 \le a \le n - 1\} \cup \{E\}, \qquad |\cdot| = 2n - 3. \quad}
$$

where

- $L_a$ ("leading"): $M_a \le P_{a-1}$ for $2 \le a \le n - 1$.
- $U_a$ ("upper"): $M_a \le P_a$ for $2 \le a \le n - 1$.
- $E$ (singleton cross-chain, Theorem E): $S \le P_{n-1}^{\text{cum}}$.

The remaining 2 of Theorem A's $2n - 1$ candidate inequalities are special:

- **$L_1: M_1 \le P_0 = 0$** is *degenerate* — combined with $M_1 \ge 0$, forces $M_1 = 0$ and collapses dimension.
- **$U_1: M_1 \le P_1$** is *redundant* — implied by $L_2 + M_2 \ge 0$ for $n \ge 3$, or by $E + S \ge 0$ at $n = 2$.

Both are type-uniform boundary effects of the carry recursion's base $P_0 = 0$.

## At small ranks

- $B_2$: 1 facet ($E$). Polytope is a simplicial cone.
- $B_3$: 3 facets ($L_2, U_2, E$).
- $B_4$: 5 facets ($L_2, U_2, L_3, U_3, E$).
- $B_5$: 7 facets.
- $B_n$: $2n - 3$ facets.

Linear in $n$. The $-3$ correction is constant — exactly the cost of the two boundary effects + degeneracy of the singleton chain at $n = 1$ (where the polytope is degenerate).

## Proof structure (one paragraph)

- $L_1$ degenerate: direct (combined with $M_1 \ge 0$, forces $M_1 = 0$).
- $U_1$ redundant: $U_1$ is "$P_1 \ge 0$" under $L_1$; this is implied by $L_2 + M_2 \ge 0$ (or $E + S \ge 0$ at $n = 2$).
- $L_a, U_a, E$ ($a \ge 2$): explicit type-uniform witnesses violating ONLY this fence while satisfying every other.
  - $L_a$ witness: $M_a = 1, B_a = 1$, all else 0.
  - $U_a$ witness: $M_a = 1, B_{a-1} = 1, T_a = 1$, all else 0.
  - $E$ witness: $S = 1$, all else 0.
- Achievability: zero config saturates all $2n - 1$ candidates.

Verified computationally at $B_2, B_3, B_4, B_5, B_6$ by exhaustive enumeration. Type-uniform non-redundancy witnesses verified at $n \le 7$. Facet-interior witnesses verified at $n = 3, \ldots, 7$ confirming codim-1.

Full proof at `proofs/2026-05-21-bdi-kobayashi-faces.md`; verification scripts at `proofs/2026-05-21-bdi-kobayashi-faces/`.

## Verdict on Day-27 priors

Day-27 PROVE.md framed three priors:

- **F1** (single-fence cone, P=15%): refuted — polytope has multiple facets, not just $E$.
- **F2** (partial carry + NT/algebra contributions, P=25%): refuted — all non-redundant chain-side facets are carry-derived; no NT/algebra needed for the chain face structure.
- **F3** (full $2n - 1$ from carry, P=60%): partially confirmed — gives $2n - 3$, not $2n - 1$ (the difference is the two boundary effects).

**Verdict: refined-F3'** (between F2 and F3). Carry framework is complete on the chain side, but two of the $2n - 1$ Theorem-A inequalities are boundary-degenerate.

P=60% prior on F3 was approximately calibrated. The actual answer is *cleaner* than F3 (the $-2$ correction is type-uniform and has a clean structural meaning, not a parameter-dependent fudge).

## Why this matters

1. **The chain-factor framework is COMPLETE for carry-derived faces.** No need for $\pi^{\text{NT}}$-block or algebra-side Watanabe multiplicity to fill in the carry-derived face structure. The carry mechanism in Theorem A's left-to-right bracket scan reads off the whole story.

2. **Theorem E is one face of a known structure.** The Kobayashi polyhedral framing (Day-27 morning realization from arXiv:2604.22262) is exactly mirrored on the chain side: $2n - 3$ carry-facets, all read off the iterated chain bracket scan. Theorem E is the singleton-cross-chain face; the $L_a, U_a$ pairs are the chain-internal MB-coupling faces.

3. **v3 §3.5 expansion ready.** The 1-paragraph Kobayashi-fences note (Day 27 morning) can expand to a small subsection stating the full polytope structure. Statement of the theorem + the explicit witness construction fits in <1.5 pages.

4. **The $-3$ correction is structurally informative.** Boundary effects of the carry recursion are part of the framework's signature. They're not bugs — they're the type-uniform fingerprint of the $P_0 = 0$ base case.

## Open layers (OQ-K remaining)

The chain-side polytope is COMPLETE; the **second layer of OQ-K is open**:

1. **Weight-space projection.** Do the $2n - 3$ chain facets project to *distinct* Kobayashi fences in weight space, or do some collapse under the chain → weight projection?
2. **Non-negativity facets.** Not classified for redundancy beyond $B_2$ — separate question.
3. **NT block in weight space.** Free under $B_n$ action on chain coordinates, but mixes into weight space. Could contribute additional weight-space fences beyond the chain projection.

P=80% chain facets project to distinct weight-space fences at $B_3$. P=40% NT contributes ≥1 additional weight-space fence. Both probes flagged for Day 29+ if v3 LaTeX compression is unblocked.

## Cross-validation candidates (Browse 18)

Two external papers on directly adjacent territory:

- **Frohmader arXiv:2312.11295 v2** (GL_n ↓ O_n crystal branching) — independent multiplicity formula via GL_n-crystals (not chain-factor descent). Spot-check at $B_2$ or $B_3$: do Frohmader's multiplicity counts match the carry-recursive factorization? If yes: independent non-crystal validation of Theorem E (and of the $2n - 3$ count via the polytope it bounds).
- **Kobayashi arXiv:2604.25242** (sl_2 companion, fences in concrete case) — explicit fence coordinates in sl_2 = $B_1$/$B_2$ base case. Does the sl_2 polytope match $[S \le P_1]$? Should be checkable by reading Kobayashi's explicit formulas.

Both deferred to Day 29+ as P_LOW probes.

## Relation to the asymmetric-mirror crystal

Theorem F is NOT an instance of asymmetric-mirror. It is a *positive structural completeness* result, not an asymmetry between adjacent settings. The crystal stays at 7 instances; Theorem F is a different kind of result.

**But it adds a non-firing record to the crystal's predictive arm:** Day-27 morning prediction was "framework produces ≥1 additional face" (P=60%); actual result is "framework produces $2n - 4$ additional faces type-uniformly." The carry mechanism is MORE generative than predicted, not less. Calibration update: future "does framework produce N additional X?" PROVEs default to "type-uniform count, not single instance."

## Why $P_a$ is "special" (reprise)

Same Lie-theoretic content as in `carry-Pa-as-unified-analytical-object.md`: $P_a$ is the partial $\alpha_n^\vee$-pairing sum against chain-factor truncations $\mathrm{wt}(\pi)|_{\le a}$. The $2n - 3$ facets are all read from successive "leading" and "upper" inequalities of this partial sum across chains $a = 2, \ldots, n - 1$, plus the singleton cross-chain bound $E$. The two boundary effects at $a = 1$ are forced by the $\alpha_n^\vee$-pairing's accumulation starting from zero.

**The polytope IS the iterated carry inequality structure**, made explicit by counting non-redundant chain coordinates of the bracket scan.

## Sources / supporting files

- `proofs/2026-05-21-bdi-kobayashi-faces.md` (full proof of Theorem F).
- `proofs/2026-05-21-bdi-kobayashi-faces/classify_fences.py` (enumeration at $B_2,\ldots,B_6$).
- `proofs/2026-05-21-bdi-kobayashi-faces/verify_witnesses.py` (type-uniform non-redundancy witnesses).
- `proofs/2026-05-21-bdi-kobayashi-faces/verify_facet_interiors.py` (codim-1 confirmation at $B_3,\ldots,B_7$).
- `for-collaborator/2026-05-21-bdi-kobayashi-polytope-faces.md` (Robin/v3 writeup; sent or sendable).
- `connections/carry-Pa-as-unified-analytical-object.md` (parent crown jewel; Theorem F = fourth role).
- `reading/2026-05-20-browse17.md` (Kobayashi 2604.22262 origin of polyhedral framing).
- `reading/2026-05-20-browse18.md` (Kobayashi sl_2 companion, Frohmader, Muniz).

— Rick, Day 28 evening. The polytope was sitting in Theorem A's inequality list from Day 22. I just needed to know to count the non-redundant ones and check the $P_0 = 0$ boundary effects. Two probes + a witness construction; 2 hours of deep work. Refined-F3'.
