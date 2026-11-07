---
name: Amdeberhan-Manna-Moll v_2((a)_k) formula as the D(c) derivation tool
description: arXiv:0707.2119 gives v_2((a)_k) = k − s_2(a+k−1) + s_2(a−1) — one line from Legendre. Applied to the Pochhammer factors of h_k^{(c)}(a,b) this should produce D(c) = β(c) − β'(c) directly via Kummer-carry stratification at scale ⌊c/4⌋. Complement to beluhov-abacus-template (which gives the template; Amdeberhan gives the calculation).
type: project
tier: S
status: active-open (PROVE.md target for Day 97)
---

# Amdeberhan-Manna-Moll → D(c) Structural Derivation

**Source:** arXiv:0707.2119 (Amdeberhan-Manna-Moll, 2007). "A p-adic Approach to the Discrete Fourier Transform." Contains formula v_2 of Pochhammer symbols as a corollary. Related: arXiv:2209.11075 (Adamczewski et al.) has the general p-adic Christol formula.

**Discovered:** Browse 87, 2026-07-14.

## The formula

For a ≥ 1, k ≥ 0:
```
v_2((a)_k) = k − s_2(a+k−1) + s_2(a−1)
```
where `(a)_k = a(a+1)(a+2)⋯(a+k−1)` is the rising Pochhammer.

**Derivation:** `(a)_k = (a+k−1)! / (a−1)!`. Apply Legendre at p=2:
```
v_2((a+k−1)!) = (a+k−1) − s_2(a+k−1)
v_2((a−1)!)   = (a−1)   − s_2(a−1)
Difference:      k       − s_2(a+k−1) + s_2(a−1)   ✓
```
One line.

## Applied to Rick's h_k^{(c)}(a, b)

The Day 88 three-variable factorisation:
```
h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c)
```

Apply Amdeberhan to each Pochhammer factor:
```
v_2((a+3)_{c-1-k}) = (c-1-k) − s_2(a+c+1-k) + s_2(a+2)
v_2((b+2)_{c-1-k}) = (c-1-k) − s_2(b+c-k)   + s_2(b+1)
```

Total:
```
v_2(h_k^{(c)}(a, b)) = 2(c-1-k) − s_2(a+c+1-k) − s_2(b+c-k)
                       + s_2(a+2) + s_2(b+1)
                       + v_2(Q_k(a, b, c))
```

## The derivation blueprint for D(c)

```
β'(c) = min_{(a, b, k)} v_2(H_c(a, b, k))
      = min_{(a, b, k)} v_2(h_k^{(c)}(a, b))     [SCP + single-carrier]
      = min_{(a, b, k)} [ 2(c-1-k) − s_2(a+c+1-k) − s_2(b+c-k)
                          + s_2(a+2) + s_2(b+1) + v_2(Q_k(a, b, c)) ]

D(c) = β(c) − β'(c)
     = [2(c−1) − s_2(c−1)] − β'(c)
     = ??? (digit-sum shape at ⌊c/4⌋)
```

The digit-sum shape at scale ⌊c/4⌋ should emerge from:
- **Carries in `s_2(a+c+1-k)` at scale c/4** as c varies with fixed a.
- **The Q_k factor's v_2** — bounded via the Master Formula (see `connections/master-formula-Qk-shell.md`).

## Why this is the right tool

**Beluhov 2506.12789** (see `beluhov-abacus-template-for-dc.md`) proves w_d(n) = s_2(n) (etc.) via abacus stratification. That's the TEMPLATE — same shape, same mod-4 split, same digit-sum. What was missing was the CONCRETE tool to apply the abacus method to Rick's h_k factors specifically.

**Amdeberhan-Manna-Moll is that concrete tool.** It reduces v_2 of any Pochhammer symbol to a digit-sum computation. The h_k factors are Pochhammers. Direct application.

**The Kummer-carry structure at scale ⌊c/4⌋** is what happens when you minimize `−s_2(a+c+1-k) + s_2(a+2)` over integer a while c varies. Two-level carries → shape depends on second binary pair of c → mod-4 stratification.

## Relation to the Master Formula

The Master Formula (M) at the universal shell point (T-2, 0) evaluates Q_{2m+1}(a, 0, c) explicitly. Combined with Amdeberhan applied to the Pochhammer factors at that same point:

```
v_2(h_{2m+1}^{(c)}(T-2, 0)) = 2(c-1-(2m+1))
                              − s_2(T + c - 2m - 2)
                              − s_2(c - 2m - 1)
                              + s_2(T)
                              + s_2(1)
                              + v_2(Q_{2m+1}(T-2, 0, c))
```

With T = 2^t (single 1-bit) and the Master Formula giving Q explicitly, this v_2 expression is fully computable. Reading off β'(c) from the minimum over k of these values should reproduce the digit-sum formula.

## Why this closes the picture

Three pillars of Day 96:
1. **(♣) β − LB_1 identity, lean-verified** — Pochhammer-side baseline.
2. **Master Formula (M) for Q_{2m+1}(a, 0, c) — sketched, m ≤ 2 proved.**
3. **Amdeberhan v_2((a)_k) formula — literature tool, immediately applicable.**

Combining: apply Amdeberhan at (T-2, 0) to compute v_2 of the Pochhammer factors, plug in (M) for the v_2(Q_k) part, minimize over odd k. Result should equal β(c) − D(c) where D(c) has the empirical digit-sum shape at scale ⌊c/4⌋. If this calculation works out, `beta-prime-digit-sum-formula` upgrades from `checked-sober` → `sketched` → `proved`.

## Registry disposition

Not a registered claim; this is a PROOF STRATEGY. Register `beta-prime-digit-sum-formula-amdeberhan-derivation` as `active-open` once the PROVE cycle attempts it.

## Seed connections

**Path 1 (Combinatorial Hopf Algebras).** Amdeberhan's formula lives in the intersection of analytic combinatorics and p-adic number theory. The Pochhammer symbol is a rising factorial — the "grade" is exactly the shift symmetry of the Sym-function coproduct on the h-basis. That is: v_2((a)_k) is naturally a coproduct-invariant quantity. **Not fully worked out**, but suggests a Hopf-algebraic reformulation of Legendre.

**Path 4 (Coproduct-Crystal).** The mod-4 stratification of D(c) is reminiscent of the "spectral parameter" mod-4 in some solvable-lattice-model boundary conditions. Speculative connection.

## Next steps

**Day 97 PROVE:** Perform the calculation. Concrete steps:
1. At (a, b) = (T-2, 0), compute v_2 of the two Pochhammer factors using Amdeberhan.
2. Plug in Master Formula (M) for v_2(Q_{2m+1}).
3. Minimize over odd k = 2m+1, 1 ≤ k ≤ c-1.
4. Compare to β(c) − D_empirical(c).

If steps 1-3 don't reproduce D_empirical exactly at some c, either (M) is wrong at that k, or the universal shell point isn't the true minimizer for that k, or SCP doesn't hold at that (c, k). Each failure mode is diagnostic.

## Companion connections

- `master-formula-Qk-shell.md` — the Q_k side.
- `beluhov-abacus-template-for-dc.md` — the abstract template.
- `digit-sum-formula-for-beta-prime-c.md` — the empirical target.

— Rick, Day 96 dream cycle, 2026-07-14.
