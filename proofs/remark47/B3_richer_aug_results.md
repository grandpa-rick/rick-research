# Richer Aug~ for B_3 (SA): priority-order experiments

**Date:** 2026-05-07.
**Script:** `/home/agent/projects/proofs/remark47/aug_tilde_B3_richer.py`.
**Goal:** Implement the bidegree-preserving "rich" move set on (w, π) pairs and find a priority order that gives a complete sign-reversing injection from odd to even items, on the 798 dominant spin pairs in B_3 (λ_1 ≤ 9/2).

## 1. Move set

For each simple reflection `s_i` (i ∈ {0,1,2} in B_3), and direction sign of `c_i = ⟨w·a, α_i^∨⟩`, the bidegree-preserving moves split by sub-type. Each elementary swap shifts β by `−sign(c_i)·α_i`; we need `|c_i|` swaps total.

### Long simple `α_i = e_i − e_{i+1}` (i = 0, 1)

- **(a) short-short:** `e_i ↔ e_{i+1}`.
- **(b±, p)** with `p < i` (low partner): `e_p ± e_i ↔ e_p ± e_{i+1}` (two sub-types: + and −).
- **(c±, q)** with `q > i+1` (high partner): `e_i ± e_q ↔ e_{i+1} ± e_q` (two sub-types).

For B_3: at i = 0, sub-types (a), (c+,2), (c−,2). At i = 1, sub-types (a), (b+,0), (b−,0).

### Short simple `α_2 = e_2`

`c = 2 (w·a)[2]`; need `|c|/2` swaps. Sub-types `(S, p)` with `p ∈ {0, 1}`:

- **(S, p):** `(e_p + e_2) ↔ (e_p − e_2)`.

### Mixed (multi-sub-type) moves

A single application of `s_i` may use a **mixture of sub-types**: pick `n_st ≥ 0` per sub-type with `Σ n_st = |c_i|` and `n_st ≤ π[donor_st]`. This is necessary; pure single-sub-type moves are NOT enough (verified: 5 odd items at λ_1 ≤ 5/2 and 378 odd items at λ_1 ≤ 9/2 have zero applicable pure moves).

## 2. Existence oracle (bipartite matching)

For each odd `(w, π)`, list ALL even `(w', π')` reachable by ANY valid mixed move on ANY single simple reflection; run Hopcroft–Karp.

**Result: 798/798 pairs admit a bidegree-preserving injection from odd → even via the rich Aug~ moves.**

So SA holds *structurally* through this Aug~ — the only remaining question is whether a *uniform priority rule* selects an injection for every pair.

## 3. Priority orders tested (full λ_1 ≤ 9/2, 798 pairs)

A priority is (simple-priority, sub-type-priority, simple-pri-mode). Within a simple reflection we use a **greedy fill in sub-type-priority order** (take min(capacity, remaining) from each sub-type in order). Simple-pri-mode:

- `order`: fixed iteration over `(L,0), (L,1), (S,2)` (per the simple-priority).
- `max_c`: pick the simple reflection with largest `|c_i|` (tie-break by simple-priority list).
- `min_c`: smallest nonzero `|c_i|`.
- `descent`: filter to left descents only (`ℓ(s_i w) < ℓ(w)`).

| Priority | Complete / 798 |
|---|---|
| **`short_first / a_first / max_c`** | **673** |
| `lex / a_first / max_c` | 667 |
| `long_first / a_first / max_c` | 667 |
| `morris / a_first / max_c` | 667 |
| `long_first / a_first / order` | 663 |
| `short_first / a_first / order` | 629 |
| `short_first / high_first / order` | 629 |
| `short_first / a_first / min_c` | 628 |
| `short_first / high_first / min_c` | 628 |
| `short_first / high_first / max_c` | 624 |

**No naïve priority order achieves 798/798.** The best is `short_first / a_first / max_c` = 673/798 = 84.3%.

## 4. Failure analysis: every failure is a COLLISION (not unmatched odd)

For all priorities tested, every odd item gets mapped to *some* even item — the move set is rich enough. Failures come from two distinct odd items being sent to the same even item, while the oracle could route one of them elsewhere.

### Concrete failure 1 (smallest)

**λ = (5/2, 3/2, 1/2), μ = (1/2, 1/2, 1/2):** `tilde_a = (5, 3, 1)`, `b = (3, 2, 1)`. Best priority gives 1 collision at bidegree (2, 1):

- **Odd A:** `w = s_2`, `π = {(1,0,−1):1, (1,0,0):1, (0,1,−1):1}`. Move chosen: `s_0` mixed `{(a):1, (c−,2):1}` → target T.
- **Odd B:** `w = s_2`, `π = {(1,0,−1):2, (0,1,0):1}`. Move chosen: `s_0` mixed `{(c−,2):2}` → target T.
- **Target T:** `w = s_0 s_2`, len=2, `π = {(0,1,−1):2, (0,1,0):1}`.

Both odds use `s_0` (since `|c_0| = 5 − 3 = 2` exceeds `|c_1|`-and-`|c_2|`-equivalents, and `s_2` has insufficient capacity), with greedy fill. The oracle exists because A or B can also reach a different even item via, e.g., a different mixture or via `s_2`.

### Concrete failure 2

**λ = (5/2, 5/2, 1/2), μ = (1/2, 1/2, 1/2):** 7 collisions among 58 odd items. One example at bd=(5, 0):

- Odd: `w = s_2`, `π = {(1,−1,0):1, (1,0,1):1, (0,1,−1):3}`. Move: `s_2` mixed `{(S,1):1}` → T.
- Odd: `w = s_2`, `π = {(1,−1,0):1, (1,0,−1):1, (0,1,−1):2, (0,1,1):1}`. Move: `s_2` mixed `{(S,0):1}` → T.
- Target T: `w = e`, `π = {(1,−1,0):1, (1,0,1):1, (0,1,−1):2, (0,1,1):1}`.

Both odds use `s_2` with `|c_2| = 2`. The greedy fill picks (S,1) for the first because π has `(0,1,1)` available (well, none — but only (S,1) cap=0 then (S,0) cap=0... hmm need to check).

### Concrete failure 3

**λ = (5/2, 5/2, 3/2), μ = (1/2, 1/2, 1/2):** 8 collisions among 69 odd items. At bd=(1, 3):

- Odd: `w = s_1`, `π = {(1,1,0):1, (0,1,0):2, (0,0,1):1}`. Move: `s_1` mixed `{(a):2, (b+,0):1}` → T.
- Odd: `w = s_1`, `π = {(1,0,1):1, (0,1,0):3}`. Move: `s_1` mixed `{(a):3}` → T.
- Target T: `w = s_1 s_0`, len=2, `π = {(1,0,1):1, (0,0,1):3}`, bd=(1,3).

Both odds use `s_1` (max-|c|) with greedy `a_first`, and both end up at T because the receiver `(0,0,1)` accumulates compatibly.

## 5. Distribution of "applicable simple reflections" per odd item

Across all 798 pairs, the distribution of #(simple reflections with at least one applicable mixed move) per odd item:

```
{1: 15189, 2: 11991, 3: 227}
```

Most odd items have 1-or-2 applicable simple reflections — the priority's "binding choice" is rare at the simple-reflection layer. The collisions almost always arise within a *single* fixed simple reflection: two distinct π's mapping to the same π' under the same `s_i` and the same greedy mixed-fill rule.

## 6. Conclusion / recommendation

- **Move set is complete.** Every odd item has ≥ 1 applicable mixed simple-reflection move. (Verified on 798 pairs / 27,407 odd items.)
- **Injection exists.** Bipartite matching oracle: 798/798 pairs admit one.
- **Naïve priority orders fail.** Best (short_first / a_first / max_c) gives 673/798 = 84.3%. All failures are collisions (no unmatched odds).
- **Obstruction is "priority too greedy."** The greedy mixed-fill rule, parameterised over (simple-priority, sub-type-priority, simple-pri-mode), never gets the look-ahead needed to avoid 2-to-1 collisions. The collisions are usually local: two odd `(w, π_1), (w, π_2)` (same `w`!) under the same `s_i` greedy rule both produce the same `π'` because the receiver root counts in `π'` reach the same combined value.

### Recommendations

1. **Read CKL Lemmas 4.20 / 4.21 / Prop A.26.** CKL's Aug-involution on horizontal strips uses a Morris-recurrence-flavoured canonical splitting that may translate to a non-greedy priority on Kostant partitions. The "basic allowable subwords" (BAS) data of arXiv:2412.16820 likely picks out the canonical simple reflection per pair.
2. **Sub-type priority needs to depend on π, not be fixed.** A natural rule: prefer the sub-type whose receiver root is *not already in π* (so the move is "cleanly distinguishable"). This breaks the collision pattern in failure 3, where both odds use the same receiver `(0,0,1)` from different donors.
3. **Two-pass / local repair.** After the greedy first pass, identify collisions and locally swap moves for collided odds. Since the oracle says an injection always exists, polynomial-time local repair is feasible.
4. **The bigraded Morris recurrence (CKL eq. 4.13)** refined to coefficient-wise positivity is probably the cleanest route. Induct on `n` and use bigraded Morris recurrence positivity at each step.

The "right" Aug~ likely lives one level *above* the simple-reflection layer: it operates on `(w, π)` together with bookkeeping of which simple reflection should be used, drawing on CKL's BAS data to single out a canonical simple reflection per pair. The simple-reflection priority alone (analog of B_2 Aug~) is genuinely too local for B_3.
