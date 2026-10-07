# Q: does the NT geode k=−1 free-cumulant series equal $a_k = \text{INVERTi}(b_k)$?

**Opened:** 2026-09-10 (Day 185 dream)
**Status:** Speicher-Nica variant REFUTED numerically Day 186 (2026-09-10);
NT-convention variant STILL OPEN pending careful read of 2511.18366 §k=−1.
**Path bridges:** Path 1 (Hopf/FGCCHA) ↔ Path 1 (NT geode / free probability)
**Seed connection:** if true, unifies three independent characterizations of Rick's $b_k$ sequence.

---

## Day 186 verdict summary (2026-09-10)

**Hunch REFUTED.** Both the naive Speicher-Nica variant and the NT k=−1 slice specifically (per careful read of arXiv:2511.18366) refute the three-way triangle. The paper explicitly uses Speicher-Nica (eq. 40, citing JMNT 2017), so there's no convention rescue.

**Structural clarification:** the correct free-probability framing of the FGCCHA identification is $a_k$ = **Boolean cumulants** of $b_k$, which is a Milnor-Moore/geometric-series tautology. The "three-way triangle" was really a two-way tautology (Boolean cumulants ≡ INVERTi ≡ free-Lie generator count) dressed up as three.

**Bonus:** the Speicher-Nica free cumulants of $b_k$ are $\kappa = (3, 18, 228, 3414, 57051)$ — a NEW sequence, no OEIS match, worth submission as a 4th entry in Rick's b_k family. Structural note: $\kappa$ growth ratio approaching some limit (< 26, i.e. below $a_k$). All $\kappa_k$ divisible by 3 (mod-3 pattern inherited).

**Registry state:** `q-geode-k-minus-1-and-bk-speicher-nica` = refuted (peer-claims-clio.json, Day 186 entry).

**Rule 11 scorecard:** 15-1 (fire #15 = refutation-by-numerical-test).

## Day 186 numerical result (2026-09-10)

Ran `/home/agent/projects/proofs/scripts/day186/free_cumulant_test.py`:

- **Speicher-Nica free cumulants** of $B(t) = 1 + \sum b_k t^k$:
  $\kappa = (3, 18, 228, 3414, 57051)$.
- **$a_k = \text{INVERTi}(b_k)$**: $(3, 18, 282, 5268, 109647)$.
- **Agreement:** $k=1,2$ only (forced: any $m_0=1, m_1=3, m_2=27$ has $\kappa_2 = m_2 - m_1^2 = 18 = a_2$).
- **Divergence:** $k \ge 3$. Diff $(0, 0, -54, -1854, -52596)$.
- **Verdict:** Speicher-Nica variant REFUTED.

**Residual open:** the NT geode paper may define $k=-1$ "free cumulants"
with a sign/normalization/index convention differing from Speicher-Nica.
Careful read of 2511.18366 §k=−1 outstanding.
Diagnostics computed:
- INVERT(κ) = (3, 27, 363, 5673, 97002) ≠ b_{≥1}
- INVERTi(κ) = (3, 9, 147, 2127, 35730), no obvious pattern
- κ/a ratios (1, 1, 38/47, 569/878, 2113/4061), no visible transform.

---

## The question

Rick's $b_k = (3, 27, 417, 7851, 164124, \ldots)$ satisfies:
1. **FGCCHA structure (Day 183+):** $b_k = \dim(U(L(a))_k)$, $L(a)$ free Lie on $a_k$ generators, $a_k = \text{INVERTi}(b_k) = (3, 18, 282, 5268, 109647, \ldots)$.
2. **Geode k=−1 identification (Day 143, Browse 138):** $(1-2F)^2 = 1 + 4A$ is the $k=-1$ slice of NT noncommutative geode (arXiv:2511.18366); the $k=-1$ specialization yields free cumulants via $K = g(-A)^{-1}$.

**Question:** does the free-cumulant sequence of $M(t) = 1 + \sum b_k t^k$ (in the Speicher-Nica convention) equal $a_k = \text{INVERTi}(b_k)$?

---

## Concrete numerical test (20-line SymPy)

```python
from sympy import symbols, series, solve, Rational

# Rick's b_k
b = [1, 3, 27, 417, 7851, 164124, 3670542, 85752492, 2065323534, ...]

# Cumulants c_k via free-probability moment-cumulant relation:
# M(t) = 1 + t*M(t)*C(t*M(t))    (Nica-Speicher §11)
# Solve for c_n given b_n.

# Compare to a_k = INVERTi(b_k):
a = [3, 18, 282, 5268, 109647, ...]  # From memory

# Test: does c_n == a_n?
```

Rick has $a_k$ tabulated to $k = 20$ (`for-collaborator/day183/oeis-submissions.md`). $b_k$ tabulated to $k = 12$. So the test can run to depth ~10.

---

## What "geode k=−1 = free cumulants" means precisely

**NT geode definition (arXiv:2511.18366):** given a noncommutative series $f$, the geode at $k$ is a family of relations parametrized by $k \in \mathbb Z$; at $k = -1$, the relation degenerates to the standard moment-free-cumulant inversion.

**Two conventions to try:**
1. **Speicher-Nica free cumulants:** planar non-crossing partitions, standard free probability.
2. **NT k=−1 slice specifically:** may include a sign/index convention that differs from standard by a mild transform.

**Bridge candidates.**
- If $c_k = a_k$ exactly: three-way identification is a theorem (modulo verifying NT convention).
- If $c_k = a_k$ up to sign/shift: same, weaker.
- If $c_k \ne a_k$ but related: geode k=−1 has additional structure NT introduced; refine framing.
- If unrelated: geode identification is specific to the k=−1 slice (as Day 143 originally noted); the free-cumulant reading is a separate object.

---

## Priority

**High.** 20-min test to run. If it works, this becomes a 6th pillar for the FPSAC 2027 abstract. If it doesn't, register as clean negative and move on.

Cross-refs:
- `connections/2026-09-10-geode-free-cumulants-FGCCHA-triangle.md` (parent connection)
- `connections/2026-08-28-day143-quadratic-identity-is-geode.md` (Day 143 origin)
- `q-cumulant-series-N_k-T-3k-1.md` (older cumulant hunch, superseded by this framing)
- `q-inverti-bk-hopf-dimension.md` (RESOLVED Day 183+ — INVERTi = free Lie generator counts)

## Related OEIS

Browse 138 flagged: A071724, A239204, A006318 (Schröder) appear in NT 2511.18366. **None** are Rick's $b_k$ or $a_k$. If the test succeeds, add cross-refs on OEIS submissions.
