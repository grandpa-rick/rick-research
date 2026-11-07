# Connection — The $(q,t)$-CQF slot for path graphs is Rick's alone

**Date:** 2026-09-11 (Day 189 dream)
**Paths:** Path 3 (Ellzey-Wachs $q$-CQF, directed graphs) → Path 2 (Hikita $(q,t)$-CQF via level-one affine Hecke)
**Registry anchors:**
- `path-graph-qGF.json` — Day 187 $(q)$-forms (post-audit: prior art but Rick's algebraic rearrangement is still his).
- No $(q,t)$ registry file yet — to be created when n=2 compute lands.

## Three-way independent confirmation of the empty slot

Browse 140 (2026-09-11) established from three independent verification paths:

1. **Ellzey 1709.00454 citation list (29 papers):** zero attempts at $(q,t)$-extension of eq (6.7).
2. **Hikita 2503.23597 citation list (3 papers):** Thm 3.12 has **ZERO citing papers**. Colmenarejo-Klein 2026 (total CQF variants), Hikita 2024 (parent), Kato 2024 (geometric) — none apply the recipe to path graphs.
3. **Semantic Scholar search for "(q,t) chromatic quasisymmetric":** Hikita is the only result.

**No paper in the literature computes $X_{P_n}(x;q,t)$ explicitly.**

## What Hikita provides (the input)

**Theorem 3.12 (verbatim, quantum Pieri rule):**
$$e_1(X) \star e_r(X) = (1 - q^{-1})[r+1]_t\, e_{r+1}(X) + q^{-1}\, e_1(X) e_r(X)$$

**⋆-product definition:**
$$F \star G := q_{(m)}\bigl(q_{(m)}^{-1}(F) \cdot q_{(m)}^{-1}(G)\bigr)$$

where $q_{(m)}$ is the level-one Hecke specialization map. Reduces to ordinary multiplication at $q=1$.

**Hecke relation:** $(T_i - t)(T_i + 1) = 0$ (quadratic), braid relations.

**Recipe from abstract:** "a recipe to produce $(q,t)$-CQFs from CQFs for any oriented graphs."

**What Hikita explicitly flags open** (Section 3, verbatim): "It seems likely that similar Pieri type formula exists for more general quantum multiplication of $e_r(X)$ and Schur functions, but we do not pursue this direction here."

## What Rick can supply (the specific slot)

- **Explicit $X_{P_n}(x;q,t)$ for small $n$** via Hikita's recipe applied to Ellzey's directed path $P_n^\to$.
- **The $e_r \star e_s$ Leibniz-like rule** (or a path-concatenation variant) — necessary for a recursion in $n$.
- **The $(q,t)$-GF** — a functional equation involving $E(qz)$, $E(z)$, and the ⋆-product. Rick's Day 187 form $F[E(qz) - qE(z)] = (1-q)E(z)$ is the natural entry point.

**Consistency constraints (checks the $(q,t)$-formula must satisfy):**
- At $q=1$: recover Stanley 1995 GF for $X_{P_n}$.
- At $t=0$: recover Rick's Day 187 (Re) recursion (= AP2018 eq 22 = Ellzey 2017 eq 6.7).
- (If Kim-Lee-Yoo 2506.23082 specializes tractably to $P_n$:) HL expansion at $t=0$.
- Griffin-Mellit $\mathbb A_{q,t}$: e-coefficients $c_\lambda(P_n; q, t)$ are $q$-independent (Hikita B(iv), Browse 135).

## Why this is seed-load-bearing

- **Path 3 → Path 2 bridge.** Ellzey-Wachs $q$-CQF ($t=0$ side) deforms via Hikita's recipe into the $\mathbb A_{q,t}$-Macdonald world (Griffin-Mellit). This is the same "quantize the parameter, watch the combinatorics deform" pattern from the quantum group seed core.
- **The ⋆-product is a level-one affine Hecke construction.** So Path 3 (Hecke) → Path 2 (quantum group) via the ⋆-product is *the* seed-canonical bridge.
- **Path 4 candidate: Tom-Vailaya vertex-gluing formula** as a candidate Leibniz-rule mechanism. If it $(q,t)$-lifts via Hikita's recipe, it gives the coproduct/deletion-contraction side of the recursion.

## Concrete FPSAC anchor path

**Minimum viable FPSAC 2027 abstract:**
- Statement 1: Explicit closed form for $X_{P_2}(x;q,t)$ and $X_{P_3}(x;q,t)$ via Hikita's recipe. (Certainly first in literature.)
- Statement 2: Recursion conjecture for general $n$ (analogue of AP2018 eq 22 in $(q,t)$).
- Statement 3: Verification against $q=1$, $t=0$, and (if tractable) Kim-Lee-Yoo at $t=0$.
- Statement 4 (stretch): $(q,t)$-analogue of the GF form $F[E(qz) - qE(z)] = (1-q)E(z)$.

Even n=3 explicit + recursion conjecture = abstract-worthy.

## Concrete test path (Day 190 PROVE, 20 min compute)

1. Write out Ellzey's directed path CQF for $P_2^\to$, $P_3^\to$ (well-known from eq 6.7).
2. Apply Hikita's $q_{(m)}$ map (level-one Hecke specialization) to obtain $X_{P_n}(x;q,t)$.
3. Verify Thm 3.12 as a sanity check: iterate $e_1 \star (\cdot)$ starting from $e_r$ and compare.
4. Extract the "$e_r$ coefficient recursion" that generalizes Rick's Day 187 (Re) to $(q,t)$.

## Community context (for calibration)

**Active parallel programs (all Path 2 territory):**
- Griffin-Mellit 2504.06936 (14 citers). $\mathbb A_{q,t}$-machinery, Macdonald basis.
- HHKKO 2504.09123 (3 citers). Restricted modular law, classical (not $(q,t)$).
- Hikita 2503.23597 (3 citers). $(q,t)$-CQF framework, quantum Pieri, recipe.
- Cho-Oh 2609.03840 (0 citers, Sep 2026). $\mathbb A_{q,t}$ K-theory of parabolic flag Hilbert schemes.
- Kim-Lee-Yoo 2506.23082 (3 citers). HL expansion via linked rook placements ($t=0$).

**FPSAC 2027 speaker list (confirmed):** Bouvel, Fink, Haiman, Iyama, Marietti, Mishna, Yip.
- **Haiman** = Macdonald expert. Directly relevant.
- **Yip** = CQF/Hessenberg. Directly relevant.

**Deadline:** not yet posted; historical pattern Oct-Dec for July conference. Rick should monitor `fpsac2027@universityofgalway.ie`.

## Not overclaiming

- The $(q,t)$-lift of Ellzey's eq (6.7) is an *open* question, not a proven identity. Rick has line-of-sight, not a result.
- Griffin-Mellit's $\mathbb A_{q,t}$ machinery is Macdonald-basis-oriented; the connection to the e-basis Pieri rule (Thm 3.12) is not fully worked out in the literature.
- Novelli-Thibon 2502.09072's "all modular relations from KL product formula" claim may contain an implicit ⋆-multiplication identity — should be checked before claiming novelty for the Leibniz rule.
- Kravitz 2606.10176 (universality of hook partitions for e-coefficient nonnegativity) is a structural result orthogonal to the $(q,t)$-picture.

## Predecessor connections

- `2026-09-08-hikita-B-iv-closes-qt-question.md` — the $q$-independence result that clarified where the $(q,t)$-arc could/couldn't go.
- `2026-09-10-h-basis-GF-universal-atomic-data.md` — SUPERSEDED by HHKKO Thm 3.7 (Day 189), but the "Path 3 → Path 2 via Hikita" framing carries over.
- `2026-09-11-novelty-check-kill-arc-2for2.md` — the sanity-check protocol that must accompany this work.
