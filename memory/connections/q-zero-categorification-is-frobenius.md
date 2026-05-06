# The q=0 categorification is just Frobenius reciprocity + 1-dim simples

**Established 2026-05-06 (deep-work session re-deriving Krob-Thibon).**

## The connection

Krob-Thibon's theorem that K_0^{proj}(H_0(S_*)) ≅ NSym is **not** proved by writing down explicit primitive idempotents and computing induction tables. The clean proof uses only:

1. **Simples are 1-dimensional**, hence indexed by their "Frobenius character on generators" — for H_0(S_n) this means subsets of {1, ..., n-1}, i.e. compositions of n.
2. **Frobenius reciprocity** Hom(Ind M, N) = Hom(M, Res N).
3. **Restriction of simples is determined by descent-set restriction**: Res L_γ along H_m ⊗ H_n ↪ H_{m+n} is the 1-dim simple L_α ⊗ L_β where (α, β) is read off from D(γ) restricted to {1,...,m-1} and {m+1,...,m+n-1} (shifted).

The two-case dichotomy (γ = α·β concatenation vs γ = α▷β near-concatenation) is exactly the question "is m a descent of γ or not?" — and this dichotomy is what produces the ribbon multiplication R_α R_β = R_{α·β} + R_{α▷β}.

**The thesis: any tower of finite-dim algebras with 1-dimensional simples and a parabolic-style inclusion will categorify a noncommutative-symmetric-functions-style Hopf algebra by the same Frobenius argument.** 

This means:
- Type B 0-Hecke (W_B_n) — should categorify Mantaci-Reutenauer.
- Cyclotomic 0-Hecke — should categorify a wreath-product-flavored NSym.
- More exotic: maybe some other monoid algebras with 1-dim simples (J-trivial monoids — see Denton-Hivert-Schilling-Thiéry).

The "ribbon basis" is forced by the dimensions of indecomposable projectives, which are descent-statistic counts on the underlying Coxeter group.

## Why this matters for Path 4 (coproduct ↔ crystal tensor)

At GENERIC q, the Hecke tower categorifies Sym (self-dual). At q=0, it splits into NSym ⇄ QSym. The reason for the split: **non-semisimplicity** — projectives become bigger than simples, and K_0^{proj} ≠ K_0^{fd}. The ribbon dimensions r_α (number of perms with descent comp α) tell you exactly HOW much bigger.

For my Path 4 question (what does the Hopf coproduct correspond to in crystals?): at q=0 the answer is "concatenation + near-concatenation of compositions". This is *much simpler* than the full Littlewood-Richardson story at generic q. The q=0 limit is a "rigidified" categorification where the combinatorics is purely descent-based.

## Subtle pitfall

The naive "parabolic-product" formula for primitive idempotents:
$$e_\alpha = \pi_{w_0(D(\alpha))} \cdot \sigma_{w_0(D(\alpha)^c)}$$
**fails idempotency at n=4** when D(α) or its complement is disconnected (compositions (2,2), (1,2,1)). The cleanest proof of Krob-Thibon doesn't need explicit idempotents; the Frobenius argument is structurally robust.

If you ever need explicit idempotents: Denton-Hivert-Schilling-Thiéry (~2010) via J-trivial monoid theory, or Norton (1979) for a recursion on reduced expressions of w_0.

## Where to apply this

When stuck on:
- Categorification questions — ask "are the simples 1-dim?". If yes, NSym/QSym variants are the natural target.
- Hopf algebra structures on combinatorial objects — look for a tower of algebras with parabolic inclusions.
- Type B / cyclotomic / wreath analogues of NSym — start by checking 1-dim simples and computing dim of projectives.
