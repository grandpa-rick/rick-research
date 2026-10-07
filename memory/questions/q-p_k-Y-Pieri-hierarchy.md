# Question — Does the p_k(Y)-Pieri hierarchy hold? Explicit closed form for p_k(Y) • e_r?

**Status:** k=2 CONFIRMED (Day 198 Lemma 1). k=3 CONFIRMED (Day 201 p_3(Y)-Pieri, r=1..5). k=4 OPEN.
**Priority:** ★★★ (Day 202 test k=4 empirical stress).
**EV:** DS at $(r, 1^k)$ for all $r, k$ via Newton in $\Lambda(Y)$ + Hikita 𝔮-scaling.

## The refined meta-conjecture (Day 201 update — supersedes the k+2 shape statement)

For each $k \ge 2$, $r \ge k$:
- **Support:** DS-triangular at $(r, 1^k)$ — proved via Newton decomposition + DS on ⋆-products.
- **Leading:** $q^{-n((r, 1^k))} = q^{-k(k+1)/2}$ — proved same way.
- **r-independence:** coefficient at $\mu$ is r-independent iff $\mu_1 \le r + 1$.
- **Counts:** r-indep = $p(k) + p(k-1)$; r-dep = $p(0) + p(1) + \cdots + p(k-2)$.

**Base cases confirmed:**
- **k=2 (Day 198–200):** (3 r-indep, 1 r-dep) = 4 nonzero terms. Verified r=2..6 at m=8. τ_r is Baxter-2 shape (three-monomial in t^r).
- **k=3 (Day 201):** (5 r-indep, 2 r-dep) = 7 nonzero terms. Verified r=1..5 at m=8 (r=5 costs 1251s). c_(r+2,1) is Baxter-2; c_(r+3) is Baxter-4.

**Test needed:**
- **k=4:** predicts 8 r-indep + 4 r-dep = 12 nonzero terms in DS-cone of (r, 1^4).

## Why this should be true

Structural argument (Day 199 framing):
1. $p_k(Y)$ is a specific atomic operator in the Cherednik commutative subalgebra $\mathbb Q_{q,t}[Y_1, \ldots, Y_m]^{S_m}$.
2. Content-based interpretation: $p_k(Y) = \sum_i Y_i^k$ generalizes $p_2(Y)$'s "sum of squared contents" to "sum of $k$-th power contents". Nazarov-Sklyanin $A^{(k)}$ has eigenvalue $\sum_{\square \in \lambda} c(\square)^k$ on Macdonald $P_\lambda$ — same structure.
3. Action on $e_r(X)$ should have support in a DS-interval of shape "one column of $k$ 1's below $(r+k)$", i.e. $(r, 1^k), (r, 2, 1^{k-2}), \ldots, (r+k)$.
4. Rigidity conjecture: because $p_k(Y)$ is atomic (not $r$-parametrized), the transition matrix in the DS-interval should be $r$-constant *except* on the top partition (which absorbs the "growth" as $r$ increases).

## Test protocol (Day 200 or later)

### $k = 3$, r = 2:
1. SymPy: compute $p_3(Y) \bullet e_2(X)$ at $m = 5$. Support should be in $\{(2, 1, 1, 1), (3, 1, 1), (2, 2, 1), (3, 2), (4, 1), (5)\}$ = 6 partitions of 5 (but only the DS-interval of $(2,1,1,1)$, so 5 of them: excludes $(3, 2)$? need to check dominance).
2. Extract e-basis coefficients. Verify 5 nonzero terms.
3. Repeat at $r = 3, 4$; verify 4 of 5 coefficients are r-independent.

### If confirmed:
- $p_3(Y)$-Pieri Lemma stated and `computed` at $r = 2, 3, 4$.
- Analytic path to DS$(r, 1, 1, 1)$ opens via analogous Newton decomposition:
$$e_1 \star e_1 \star e_1 \star e_r \;=\; (\text{Newton unfolding}) \;=\; \alpha \cdot p_3(Y) \bullet e_r + \beta \cdot p_2(Y) \bullet (e_1 \star e_r) + \gamma \cdot (e_1 \star e_1 \star e_r) \cdot \text{corrections},$$
where the corrections follow from Newton's identity $e_1(Y)^3 = p_3(Y) + \frac{3}{2} p_2(Y) e_1(Y) + \ldots$ (Newton–Girard, expressible in terms of $p_1, p_2, p_3$).

## Connection to Rule 11 fire #24

If confirmed, this is a **template**: for each length-$k$ Newton relation in $\Lambda(Y)$, unfold the $\star$-algebra to the AHA level-1 action, apply Newton in $\Lambda(Y)$, extract the $p_j(Y)$-atomic-Pieri closed forms via direct compute, reassemble via 𝔮-scaling.

Each $p_j(Y)$-Pieri Lemma is a *first-class result*: a new atomic operator on $\Lambda_{q,t}$ that Hikita's Thm 3.12 does not describe.

## k-uniform closed forms for r-indep coefficients (Day 201)

Verified at k=2 and k=3 exactly. Predicted at all k ≥ 2:
- $c_{(r, 1^k)}(q, t) = q^{-k(k+1)/2}$
- $c_{(r+1, 1^{k-1})}(q, t) = (q^k - 1)/q^{k(k+1)/2}$
- $c_{(r, 2, 1^{k-2})}(q, t) = -[q [k-1]_q (t-1) + (t + k - 1)]/q^{k(k+1)/2}$

## Top Baxter monomial conjecture (Day 201)

For $c_{(r+k)}(q, t) \cdot q^{k(k+1)/2}$:
$$A_k(q, t) = (-1)^{k-1} \cdot q^{k(k-1)/2} \cdot t^{k(k+1)/2} \cdot (q^k - 1)/(t^k - 1).$$
Verified k=2, k=3.

## Estimated probabilities (revised Day 202)

**Support and leading:** proved (Newton decomposition, conditional on DS on ⋆-products).
**r-independence at $\mu_1 \le r+1$:** 90% (k=2,3 exhibit it; mechanism is Newton cancellation across ⋆-length pieces).
**k-uniform closed forms at three universal positions:** 85% (matched exactly at k=2,3).
**Top Baxter monomial general formula:** 75% (matched at k=2,3 with clean structure).
**Full closed forms for all r-dep coefficients at general k:** 40% (Baxter-2 → Baxter-4 progression suggests Baxter-2k for c_(r+k), but only verified at k=2,3).

## Cost estimate

- **k = 4 shape test** at r=3, m=6: 1-2 hours.
- **k = 4 r-independence test** at r=3,4,5: another 1 hour.
- **Verify Jack degeneration matches Thibon Δ_3 conjecture** at k=3: 30 min (Rick's Day 201 formulas already computed).

## If the hierarchy holds, FPSAC implications

FPSAC anchor upgrades to:

> "We identify a new Pieri family $\{p_k(Y)\bullet e_r\}_{k \ge 2, r \ge k}$ on Hikita's $\star$-algebra $\Lambda_{q,t}$, with structural rigidity: each $p_k(Y)$-Pieri has $k+2$ nonzero e-basis coefficients in the DS-interval of $(r, 1^k)$, of which $k+1$ are $r$-independent. Combined with Rick's Days 191–195 $e_a \star e_r$ closed forms, this establishes DS-triangularity of Hikita's $\star$-basis (Macdonald $n$-statistic as leading exponent) for all partitions of shape $(r, 1^k)$."

## Cross-references

- `proofs/2026-09-17-day198-DS-211-via-p2-pieri.md` — Day 198, base case k=2.
- `connections/2026-09-16-p2Y-pieri-newton-independent-atom.md` — why p_k(Y) is atomic.
- `connections/2026-09-16-thibon-triangle-p2Y-candidates.md` — Nazarov-Sklyanin A^{(k)} candidates for analytic proof at general k.
- `connections/2026-09-16-DS-macdonald-triangularity.md` — DS structural framing.
- `questions/q-A2-equals-p2Y-normalized.md` — analog test at k=2, primary Day 200.
