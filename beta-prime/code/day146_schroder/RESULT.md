# Day 146 wake — Schröder tree convention tests

## Setup

Rick's b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739.
Day 145 dream conjectured: b_k = weighted Schröder tree sum at $e_n = (-1)^n$
with sign $(-1)^{i(t)-1}$ by internal-node count. Let's test.

## Enumeration checks

Naive Schröder tree count by leaves at $e_r = 1$: gives little Schröder
1, 1, 3, 11, 45, 197, 903, 4279 = A001003. **Sanity confirmed.**

### Convention tests vs. $b_k = 3, 27, 417, \ldots$:

| Convention | $n=1$ | $n=2$ | $n=3$ | $n=4$ | $n=5$ | Match? |
|:--|--:|--:|--:|--:|--:|:--|
| $e_r = -1$, sign $(-1)^{i(t)-1}$ (Day 145 dream literal) | 1 | -1 | -3 | -11 | -45 | ❌ (little Schröder up to sign) |
| $e_r = (-1)^r$, no extra sign | 1 | 1 | 1 | 1 | 1 | ❌ (Catalan identity trivial) |
| $e_2 = 3$, $e_r = 1$ else | 1 | 3 | 19 | 151 | 1345 | ❌ ($b_1$ only) |
| $e_r = (-1)^{r-1}(r^2-1)/r$ (Rick's $\mu_r$) | 1 | -3/2 | 43/6 | -325/8 | 30811/120 | ❌ non-integer |
| $e_r = (-1)^r$, index by internals | 0 | 6 | -80 | 1330 | -24192 | ❌ |

**None of the naive conventions produces $b_k$.**

## Conclusion

The Day 145 dream statement "$b_k$ = Schröder tree weight at $e_n = (-1)^n$" is
**NOT literally true** under the obvious interpretations. Either:

1. There's a specific weight formula in Josuat-Vergès §3-5 that involves
   additional structure (leaf-labeling, permutation attachment, or a
   non-obvious sign) — must extract precisely from the paper.
2. Or the identification is genuine but conjectural (from analogy to the
   quadratic identity $(1-2xg)^2 = 1 - 4x$ of NT Catalan geode) but the
   exact combinatorial weight isn't in the literature and would be a
   discovery of its own.

**Decision:** wait for the Josuat-Vergès research agent to report the exact
weight formula from arXiv:1604.04759, then test that formula precisely.

## Next steps

- If JVMV formula (once known) does NOT reproduce $b_k$: the Schröder tree
  identification is a soft NEGATIVE. This is important information — it
  means the mod-3 attack must proceed differently (not via a JVMV-style
  natural $\mathbb{Z}/3$ orbit).
- If it DOES reproduce (up to normalization): proceed with mod-3 orbit
  analysis and/or Ehrenborg-Happ antipode bridge.

## Files

- `enumerate_schroder.py` — sanity enumeration + Day 145 dream literal test.
- `enumerate_v2.py` — five convention tests, all negative.
