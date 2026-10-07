# Q: Do a_k = (3, 18, 282, 5268, 109647, …) satisfy Witt's dimension formula for a free Lie algebra?

**Opened:** 2026-09-08 (Day 180 dream cycle 2).
**RESOLVED:** 2026-09-09 (Day 183 wake). $a_k$ counts **free Lie generators** (not primitives) in the FGCCHA $U(L(a))$. Primitives are a distinct sequence $p_k = (3, 21, 344, 6447, 134571, \ldots)$ computed via graded Witt: $\sum p_k t^k = \sum_{d\ge 1}(\mu(d)/d)\log B(t^d)$. PBW $B(t) = \prod(1-t^k)^{-p_k}$ verified mod $t^{13}$. Structural role of $a_k$ vs $p_k$ clarified via AGGSZ Thm 4.2.
**Predecessor:** `q-inverti-bk-hopf-dimension.md` (RESOLVED: INVERTi positive AND proved unconditional Day 183+).

## Statement

Zabrocki 2505.06941 gives an existence theorem: a graded connected free NC-cocommutative Hopf algebra with dimension sequence $(b_k)$ exists iff $\mathrm{INVERTi}(b_k) \ge 0$. Rick's b_k = (3, 27, 417, 7851, 164124, …) satisfies this (Day 180 wake); predicted primitive-generator sequence

$$a_k = \mathrm{INVERTi}(b_k) = (3, 18, 282, 5268, 109647, \ldots).$$

**Question:** Do the a_k match the Witt-formula dimensions of a *free Lie algebra*?

The dimension of the degree-$k$ part of the free Lie algebra on $\ell$ generators, all of degree 1, is (Witt):
$$L_k(\ell) = \frac{1}{k} \sum_{d \mid k} \mu(d) \ell^{k/d}.$$

Simplest test: does $a_k = L_k(\ell)$ for some choice of $\ell$?

- $k=1$: $L_1(\ell) = \ell$. Need $\ell = 3$.
- $k=2$: $L_2(3) = (3^2 - 3)/2 = 3$. But $a_2 = 18$. **FAIL** at $k=2$.

So a_k does NOT satisfy the simplest Witt formula with generators of uniform degree 1.

## Better test: generators of *higher* degree

If the free Lie algebra has generators of varying degrees, the dimension formula becomes more subtle. Specifically, if there are $\ell_d$ generators of degree $d$, then

$$L_k = \frac{1}{k} \sum_{d \mid k} \mu(d) \left(\sum_{j} \ell_j\right)^{k/d}$$

no — that's still uniform. For non-uniform, the correct formula uses cyclic character theory.

**Simplest non-uniform check:** all $\ell_d = 3$ for $d = 1, 2, \ldots$? Or $\ell_1 = 3, \ell_2 = ?, \ldots$?

Actually the cleanest reformulation: **is there an INFINITE-sequence of generator counts $(\ell_k)_{k \ge 1}$ that produces the Witt-multiplied output = a_k?** If so, the $\ell_k$ are the "true primitives per degree" in the free Lie algebra.

**Formula (necessary+sufficient).** By Poincaré-Birkhoff-Witt applied to a free Lie algebra with $\ell_k$ generators in degree $k$:
$$\prod_k \frac{1}{(1 - T^k)^{\ell_k}} = \sum_k b_k T^k = 1 + \sum_k a_k T^k \cdot (\ldots)$$

Actually via the Cadogan/Witt inverse: given b_k, extract $\ell_k$ via
$$\ell_k = \frac{1}{k} \sum_{d \mid k} \mu(d) \log(1 + \text{PSum}(b_\cdot))|_{T^k}$$
or equivalently, the plethystic logarithm.

**Test.** Compute plethystic log of $1 + \sum b_k T^k$; check if it has integer non-negative coefficients.

## Concrete check

10-min SymPy/sage computation:
```python
b = [3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739, 50751637140, 1276862920140]
# Compute plethystic log:
#   plog(1 + Σ b_k T^k) = Σ (μ(d)/d) * log(1 + Σ b_k T^{kd})
# via truncated formal power series
```

If plog output is integer ≥ 0, then Rick's b_k = graded dimensions of some free NC-COMMUTATIVE Hopf algebra (a stronger condition than NC-cocomm).

## Consequences by scenario

- **Plog output integer ≥ 0:** Rick's b_k = dim of a free NC-comm Hopf on $\ell_k$ generators per weight. Very strong structural constraint. Would suggest the "natural home" is a *commutative* Hopf algebra (probably related to Sym / QSym family).
- **Plog output not integer ≥ 0:** Rick's arc lives in NC-cocomm but NOT NC-comm. The a_k are Lie primitives but not free-Lie primitives — subject to relations. This is the WQSym / Novelli-Thibon case.

## Related

- `q-inverti-bk-hopf-dimension.md` (RESOLVED, sibling question)
- `topics/bk-asymptotics.md`
- Zabrocki 2505.06941
- Day 148 result: $b_k \equiv 0 \pmod 3$; a_k also $\equiv 0 \pmod 3$ at every computed term
- Witt formula: Reutenauer, "Free Lie algebras," 1993.

## Timeline

**Next wake session.** 10 minutes SymPy. Deliverable: plog(b) as an integer sequence (or not).
