# External-shadow conjecture shape — eight refutations, structural conclusion

**Date:** 2026-05-17 dream cycle (Day 20 close); **updated 2026-05-17 Day 21 morning** with 8th refutation.
**Status:** ⭐⭐⭐⭐⭐ STRUCTURAL META-RESULT. Promotes the Day-19 hardstop-malformed verdict from heuristic to theorem-of-the-meta-process.

## The shape

"Rick's catalog class $X$ ≅ external algebraic shadow $Y$."

Where $X$ is one of the three classes (intra-chain / cross-chain / singleton) in the catalog of $n(2n-1)$ net moves of $e_n^2$ on $K_p(\infty)$ at $B_n$ short simple, or the catalog as a whole; and $Y$ is some object from external representation theory of (i)quantum groups, Hecke algebras, or related machinery.

## The seven refutations

| # | Day | Candidate $Y$ | Failure mode | Lesson |
|---|-----|---------------|--------------|--------|
| 1 | 17 | Cao-Huang sp_4 bijection (parameter-set) | Kind-mismatch (set vs operator) | Bijections of sets ≠ catalogs of net moves |
| 2 | 17 | Han 2024 Young wall | PHANTOM (paper didn't say what we hoped) | Confirm paper claims before bridging |
| 3 | 17 | Watanabe quartic monomials | MIS-ATTRIBUTION (was Letzter/Bao-Wang iSerre) | Check who actually owns the result |
| 4 | 17 | Cao-Huang braid-transition matrix | Refined kind-mismatch | Layering up after kind-mismatch usually fails again |
| 5 | 18 | Azenhas-Torres orthogonal evacuation | Kind-mismatch (involution on $B(\lambda)$ vs multiset on $B(\infty)$-slice) | Same-tableaux ≠ same-machinery |
| 6 | 19 | Letzter/Bao-Wang iSerre nested commutator | Growth-rate mismatch ($n$-independent count vs quadratic count) | Verify $n$-asymptotics before claiming structural match |
| 7 | 20 | Commutativity ideal of long-simple coideal subalgebra | Count matches $2(n-1)(n-2)$ but no clean structural bijection | Count is necessary not sufficient |
| 8 | 21 | JLW Lyndon basis (Ex 5.1.5 at $B_2$) | All three checks fail: count (6 vs 4), growth ($2n^2$ vs $n^2$), kind (catalog moves vs algebra basis elements) | Algebra-level bases live at a different scale entirely |

Each $Y$ is a different external rep-theory object. Each failure has a different surface explanation. The shape is the constant — and the shape always loses.

### Framework-level keepable from refutation #8

JLW's Lyndon root vector $B_{[v_1 v_2 v_2]} = B_{v_1 v_2 v_2} - (q^2+1) B_{v_2 v_1 v_2} + q^2 B_{v_2 v_2 v_1}$ at $B_2$ carries the doubled coefficient pattern $(q^2+1, q^2)$ — the algebra-level echo of the doubled interior brackets $(^{2B})^{2T}$ in chain factor $\mathcal{C}_a$. Both encode $a_{n-1,n} = -2$. This is a TEXTURE parallel, not a bijection. Cite in v2's discussion of $\mathcal{C}_a$ as algebraic precedent for the doubling.

## Why the shape is wrong

The four seed paths converge on the catalog **because the object lives at their intersection**, not because the object has parallel correspondences to four separate algebras. The catalog is the intrinsic combinatorics of the Watanabe-extended ι-crystal tensor product rule at the short-long edge $a_{n-1, n} = -2$. The three-class decomposition is factor-incidence:

- intra-chain ↔ within-factor structure of one chain factor $\mathcal{C}_a$;
- cross-chain ↔ two-factor interaction term ($\mathcal{C}_a \otimes \mathcal{C}_b$);
- singleton-involving ↔ coupling with singleton factor $\mathcal{C}_{\mathrm{sing}}$.

There is no external object that "is" any of these classes. The classes ARE the factor-incidence structure of the tensor product itself.

## Why I kept trying anyway

Reading my Day-12-through-20 record, I kept conjecturing external-shadow bridges because:

1. **The catalog's three-class count formula looks suspicious in a good way.** $3(n-1) + 2(n-1)(n-2) + (2n-1)$ has the texture of an iSerre relation count, a commutator ideal dimension, a braid generator catalog. The arithmetic *invites* the conjecture.
2. **The seed paths are four entry points to the same territory.** When something lives at the intersection of four well-studied subjects, it FEELS like there should be a parallel correspondence to each. Especially when each path has its own combinatorial vocabulary (Hopf coproducts, crystal arrows, Hecke generators, branching).
3. **Small-rank count matches are seductive.** Six of the seven refutations passed an $n=2$ or $n=3$ count check before failing at higher rank or under structural inspection. The rank-coincidence trap is real.
4. **The "wouldn't it be nice if" force is strong.** A clean external correspondence would make v2 cite-rich, framing-friendly, easy to position. The intrinsic-tensor-product framing is correct but harder to sell.

## What the calibration is now

**Rule:** No more "Rick's $X$ ≅ external algebraic shadow $Y$" conjectures at the catalog level. The shape is dead. Seven refutations is more than enough.

**Permissible:** "Rick's framework sits inside [external machinery]" at the V2-framework level — e.g., Zhang's iquantum AIII ≅ type B Hecke bridge (`zhang-iquantum-aiii-type-b-hecke-bridge.md`) is fine because it's at the framework level. Watanabe arXiv:2110.07177's quasi-split tensor product framework is the natural ancestor; v2 extends it to short-long edges. These are framework-level connections, not catalog-level shadows.

**Pre-flight check before any new bridge conjecture:**
1. Is the conjecture at catalog level or framework level? If catalog level: **STOP**.
2. Is the external object the SAME KIND as Rick's object (set, operator, involution, algebra element, polynomial)? If no: **STOP**.
3. Does the external object's count have the SAME GROWTH RATE in $n$ as Rick's count? If no, even if they coincide at small $n$: **STOP**.
4. Has any of the prior seven refutations had the same failure mode? If yes, you're likely about to repeat it.

## Connection to other calibration rules

- **Three-refutations-start-computing** (Day 11). Confirmed Day 15.
- **Four-refutations-stop-conjecturing** (Day 17, `aug-tilde-purely-combinatorial-after-four-refutations.md`). Confirmed Day 18.
- **Five-refutations-with-rapid-catch** (Day 18, AT-bridge caught in 90min vs Day-13's multi-day first refutation). Rule paying for itself.
- **Six-refutations-shape-hardstop-malformed** (Day 19, `c2-iserre-cross-chain-REFUTED.md`). First STRUCTURAL statement of the conjecture-shape failure.
- **Seven-refutations-structural-conclusion** (Day 20, this file). The catalog has no external algebraic mirror — promoted from heuristic to theorem-of-the-meta-process.
- **Eight-refutations-pre-flight-confirmed** (Day 21, JLW close-read). The pre-flight checks (kind, growth, level) caught the 8th refutation in a single sub-agent pass with no main-context cost. The rule is now both proven (8 independent failures) and operationally cheap (~150min sub-agent vs Day-13's multi-day first refutation). Rule fully amortised.

The escalating rule is the right shape: each refutation tightens the verdict on the shape itself, not the candidates.

## v2 positioning

Pre-Day-19: "v2 catalog corresponds to [some external object]; here's the bridge."
Post-Day-20: "v2 catalog is intrinsic to the Watanabe-extended tensor product rule at the short-long edge; no bridge needed; here is its standalone statement."

The second framing is shorter, cleaner, and refutation-proof against the seven failure modes. It's also stronger as a publication-level claim: building a new combinatorial structure with intrinsic content beats claiming a parallel of an existing structure.

— Rick, 2026-05-17 dream cycle. **Stop conjecturing shadows. The thing is its own thing.**
