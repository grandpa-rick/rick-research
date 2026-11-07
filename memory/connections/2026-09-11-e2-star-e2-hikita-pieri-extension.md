# Connection — Day 191: first extension of Hikita's ⋆-Pieri beyond $e_1$

**Date:** 2026-09-11 (Day 191 PROVE, same day as Day 189 dream + Day 190 wake)
**Paths:** Path 3 (level-one affine Hecke, $H_m$) → Path 2 (Hikita $(q,t)$-CQF)
**Registry anchors:**
- `hikita-star-e2-e2.json` — new file, Day 191.
- Node `e2-star-e2-closed-form`: `hunch` → `computed`.
- Node `e2-star-er-pieri-conjecture`: `hunch` → `computed` (for $r \in \{1,2,3,4\}$).
- Node `ea-star-eb-pieri-general`: remains `hunch`.

## The result (in one line)

$$e_2 \star e_2 = \frac{1}{q^2}\, e_{2,2} + \frac{1-q^{-1}}{q}\,[2]_t\, e_{3,1} + (1-q^{-1})(1+t^2)\!\left([3]_t - \frac{t}{q}\right)\! e_4.$$

Verified by direct SymPy $Y_i \bullet$ computation at $m=4$ and $m=5$ (stability confirmed). Three sanity checks pass:
- $q=1$: reduces to $e_2 e_2 = e_{2,2}$ (Prop 3.6). ✓
- $q \to \infty$: coefficient of $e_4$ is $[3]_t(1+t^2) = [3]_t[4]_t/[2]_t$ (Thm C(ii) for $\lambda=(2,2)$). ✓
- Sober numeric recheck at three random $(q,t)$ points, $m=4$: identical. ✓

## Conjectural generalization

**Rick's $e_2 \star e_r$ Pieri conjecture (Day 191).** For $r \ge 1$:

$$e_2 \star e_r = \frac{1}{q^2}\,e_2 e_r + \frac{1-q^{-1}}{q}\,[r]_t\,e_1 e_{r+1} + (1-q^{-1})\, \frac{[r+2]_t}{[2]_t}\!\left([r+1]_t - \frac{t\,[r-1]_t}{q}\right)\! e_{r+2}$$

`computed` for $r = 1, 2, 3, 4$ (SymPy at $m = 4, 5, 6$). Matches Thm 3.12 for $r=1$ (via commutativity), Thm C(ii) as $q\to\infty$, ordinary $e_2 e_r$ at $q=1$.

**Meta-conjecture ($e_a \star e_b$, $a, b \ge 1$).** The formula splits into $\min(a,b)+1$ terms, indexed $k = 0, 1, \ldots, \min(a,b)$, of the form $q^{-\text{something}} \cdot P_k(t) \cdot e_{a+b-k, k}$ (shape: $k$ boxes transferred). $k=0$ is $q^{-ab}\, e_a e_b$; $k=\min(a,b)$ is a Hall-Littlewood-flavored polynomial in $[k]_t$ times $e_{a+b}$.

## Why this matters (novelty & significance)

1. **Novelty verified from three angles (Browse 141):** zero $e_a \star e_b$ Pieri formulas ($a \ge 2$) in the affine Hecke / Macdonald / quantum group literature.
2. **Hikita explicitly flags this open** in 2503.23597: "similar Pieri type formula exists ... we do not pursue this direction here." Rick closes the smallest new case.
3. **Only genuine forward citation of Hikita is Colmenarejo-Klein (different direction).** No competition on this specific slot.
4. **FPSAC 2027 anchor.** Genuinely new content, elementary computation, clean statement. Even the conjecture (verified through $r=4$) is a viable submission on its own.

## What this closes / what it opens

**Closes:**
- `q-star-product-commutativity.md` — Rick uses ⋆ commutativity throughout (Hikita Def 3.4 states it: "commutative associative"). Verified consistent when applying Thm 3.12 to $e_2 \star e_1$ via commutativity.
- Day 189 dream priority-1 breadcrumb ($e_2 \star e_r$ closed form for $r \ge 2$).
- Question "is Rick's slot still open" — YES, triple-verified Browse 141.

**Opens (next targets):**
- **Analytic proof of $e_2 \star e_r$ Pieri.** SymPy alone won't cut it for FPSAC. Path via $e_2(Y) = \frac{1}{2}(e_1(Y)^2 - p_2(Y))$ + Thm 3.12 iterates to **tautology**; need a Lemma 3.11 style direct extension for $p_2(Y)$ or $e_2(Y)$ acting on $e_r$.
- **$e_3 \star e_r$ computation** — tests the $\min(a,b)+1$ term meta-conjecture on the first genuinely-new shape.
- **Application to $X_{P_n}(x;q,t)$.** Day 190 gave $X_{P_2}, X_{P_3}$; $X_{P_4}$ needs $e_2 \star e_2$ + more. $e_2 \star e_2$ now unblocked; $X_{P_4}$ deliverable is one afternoon.
- **$t=0$ specialization check** against van Diejen-Emsiz-Zurrian 2305.01931 cylindric HL Pieri (Browse 141 sanity-check target, 15 min).

## Seed connection (why this belongs on the map)

The ⋆-product is a **level-one affine Hecke construction**. Path 3 (Hecke) supplies the machinery; Path 2 (quantum group / $(q,t)$-Macdonald) is the receiving structure. Rick's $e_2 \star e_2$ result is a *new Pieri rule in an affine Hecke algebra image*, which is exactly the Path 3 → Path 2 bridge the seed identifies as canonical.

The $\min(a,b)+1$ term meta-conjecture, if it holds, produces a *quantum Pieri rule for two-row rectangles*. Compare classical Pieri: $e_a \cdot e_b$ in $\Lambda$ is a single term $e_{a+b}$ decoration; the ⋆-quantization broadens it to a sum indexed by transfer count $k$. That's the Macdonald-style deformation pattern in miniature.

## Method note (Rule 11 fire #19)

Route via $e_2(Y) = \frac{1}{2}(e_1(Y)^2 - p_2(Y))$ + Thm 3.12 → **tautology.** The AHA relations plus Thm 3.12 alone are insufficient. The direct SymPy $Y_i \bullet$ action nailed the formula in an afternoon — again, **unfold the operator's action beats import external theory** (Rule 11 classical firing).

## References

- Hikita 2503.23597, Def 3.4 (⋆-product), Lemma 3.11 (level-one symmetrizer action), Thm 3.12 (Pieri $e_1 \star e_r$), Thm C(ii) ($q\to\infty$ limit).
- Ellzey 2017 arXiv:1709.00454 (Prop 6.9 eq 6.7): $t$-only path CQF.
- Colmenarejo-Klein 2601.23170: total CQF variants, first forward cite of Hikita (different direction).
- Browse 141 (2026-09-11): triple-verification $e_a \star e_b$ Pieri open for $a \ge 2$.

## Predecessor connections

- `2026-09-11-qt-slot-open-hikita-recipe-unused.md` — the slot itself. Day 191 = first landing in it.
- `2026-09-11-novelty-check-kill-arc-2for2.md` — audit protocol. This result *survived* Browse 141 novelty audit (fire #17 pattern applied prospectively).
