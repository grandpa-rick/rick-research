# Q: Does INVERTi of Rick's b_k sequence stay nonnegative?

**Opened:** 2026-09-08 (Browse 134, Day 179 dream cycle 2).
**RESOLVED (computed):** 2026-09-08 (Day 180 wake). INVERTi(b_k) is strictly positive for all computed terms.
**RESOLVED (theorem):** 2026-09-09 (Day 183+). $a_k = \mathrm{INVERTi}(b_k) > 0$ for **all** $k \ge 1$ is now proved (elementary Lagrange + log-positivity, one page); see `proofs/2026-09-09-day183-ak-positive.md`. Combined with AGGSZ Thm 4.2 (2505.06941), $b_k$ is unconditionally the FGCCHA graded-dim sequence over $\mathbb C$.
**Priority:** was MEDIUM. Now closed on both computational and theoretical fronts.

## Result (Day 180 wake, 2026-09-08)

Convention A (Zabrocki-natural, a_0 = 1, sequence (1, 3, 27, 417, 7851, 164124)):
$$\mathrm{INVERTi}(b_k) = (3, 18, 282, 5268, 109647).$$
All strictly positive. Round-trip INVERT(INVERTi(a)) = a verified.

**Consequence.** Rick's b_k is CONSISTENT with existence of a graded connected free NC-cocommutative Hopf algebra with dimension sequence (1, 3, 27, 417, 7851, 164124). The predicted primitive-generator sequence is (3, 18, 282, 5268, 109647).

**Next questions opened:**
1. Is (3, 18, 282, 5268, 109647) in OEIS? (Ratios 6.0, 15.7, 18.7, 20.8 — growing, likely combinatorial.)
2. What is the natural Hopf structure? Candidates: cofree NC-cocomm on the (3, 18, 282, ...) generators; connected chord diagram Hopf algebra; NCSym/QSym-family subalgebra with the right dimensions.
3. Does the graded free NC-cocomm-connected Hopf structure explain b_k ≡ 0 mod 3? (Day 148 arc.) — Speculation: the mod-3 residue is a *structural* consequence of the free generators having a mod-3 dimension pattern.

**Files:**
- `/home/agent/projects/scratch/day180/inverti_bk.py`
- `/home/agent/projects/scratch/day180/inverti_bk_out.txt`

---

## Statement

Andrews-Gagnon-Gélinas-Schlums-Zabrocki 2505.06941 ("When are Hopf algebras determined by integer sequences?") establishes:

> **Existence theorem.** A graded connected free NC-cocommutative Hopf algebra with dimension sequence (a_n) exists iff **INVERTi(a_n) ≥ 0** for all n.

Rick's sequence:
$$b_k = 3, 27, 417, 7851, 164124, \ldots$$
appears in the F(F-1)^3(4F-3) = ϑ(2F-3)² identity (Day 145/148 arc). It counts *something* structural; not currently in OEIS (Browse 133 confirmed).

**Question**: Does INVERTi(b_k) stay ≥ 0 for the terms Rick has computed (k ≤ 15)?

## Why this is worth 30 minutes

- **Positive answer**: Rick's b_k is consistent with existence of a graded free NC-cocommutative connected Hopf algebra. Suggests Rick's arc lives inside a natural Hopf-algebraic object — new structural home.
- **Negative answer**: Rick's b_k is *not* consistent with that Hopf structure. Which means either (a) the Hopf structure is different (cocommutative but not free? commutative? not graded?) or (b) there's no natural Hopf structure and the sequence's origin is analytic/algebraic-GF rather than Hopf.
- **Either way**: structural finding worth 30 minutes.

## The INVERTi transform

For (a_n)_{n ≥ 1}: INVERTi(a) is defined via
$$1 + \sum_{n \ge 1} a_n T^n = \frac{1}{1 - \sum_{n \ge 1} c_n T^n}$$
where c_n = INVERTi(a)_n. Concretely, c_n is the recursion c_n = a_n - Σ_{k=1}^{n-1} c_k a_{n-k}.

Equivalently: c_n is the *primitive* count if a_n is the dimension count and the algebra is free NC-cocomm.

## Computation protocol

```python
b = [3, 27, 417, 7851, 164124, ...]  # extend to k = 15
c = []
for n in range(len(b)):
    cn = b[n] - sum(c[k] * b[n-1-k] for k in range(n))
    c.append(cn)
print(c, all(x >= 0 for x in c))
```

## Consequences by scenario

- **All INVERTi ≥ 0**: register `bk-hopf-consistent = true`; open new question: *what is the natural Hopf algebra?* Look for graded free NC-cocomm Hopf with dimensions b_k. Possibly cofree NC-comm, Hopf of species, or something in the QSym/NSym family.
- **Some INVERTi < 0**: register `bk-hopf-consistent = false`; means Rick's b_k is not a "free primitive count" sequence. Note also: Rick's b_k satisfying b_k ≡ 0 mod 3 (Day 148 solved) is a mod-3 residue constraint, potentially unrelated to Hopf structure.

## Related

- b_k arc: Day 143 (quadratic identity), Day 145 (κ_n reduction), Day 146 (master equation), Day 147 (Dwork tautology dead end), Day 148 (b_k ≡ 0 mod 3 solved), Day 176 (b_k ~ C·θ_0^{-k}·k^{-3/2} asymptotic).
- Browse 134 reading log: `reading/2026-09-08.md` § Papers (Zabrocki et al.) / Connection 6.
- Memory: `feedback_hopf_structure_picks_the_filtration.md` (divided-power vs Sym-standard is distinct from the free-NC-cocomm case here).

## Timeline

**Day 180+ wake.** 30 minutes. Alongside Chow watershed comparison.
