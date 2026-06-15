# Day 73 CODE Task C — Kiers admissible OPS for GL(3) ↪ SO(6)

## Headline

**Zero nontrivial admissible OPS for GL(3) ↪ SO(6).**

The prediction (Browse 63 reply to Robin) is confirmed:
- Weights of `so(6) / gl(3)` as a `gl(3)`-module: 6 weights of the
  form `±(e_i + e_j)` for `1 ≤ i < j ≤ 3` (3 from `Λ²V`, 3 from
  `Λ²V*`).
- Admissibility (Kiers Def 1.4) requires `<τ, w> ≥ 0` for every
  weight `w`.  The pair of opposite weights `±(e_i + e_j)` forces
  `a_i + a_j = 0` for all `i < j`.
- Combined with dominance `a_1 ≥ a_2 ≥ a_3`: only `τ = (0, 0, 0)`.

Numerical enumeration over `|a_i| ≤ 5, 10, 20` confirms this: every
dominant primitive admissible OPS is `(0, 0, 0)`.

## Structural consequence

By **Kiers Thm 1.5** (Type-I extremal rays of the saturation cone
come from admissible OPS), GL(3) ↪ SO(6) has **NO Type-I rays**.

Any AXIS extremal rays for GL(3) ↪ SO(6) (i.e. the boundary of the
saturation cone `C(GL(3) ↪ SO(6))`) must therefore come from
**Kiers Thm 1.8 Type-II rays** — induction from a parabolic
boundary.

This **pivots Day-74 PROVE** away from the "find the 3 admissible
OPS" strategy and toward Type-II enumeration:
1. Identify the standard parabolic boundaries of GL(3) and SO(6).
2. For each pair `(P_H, P_G)` with `P_H = H ∩ P_G`, compute the
   induced ray from the lower-rank saturation cone.
3. The Day-71 conjectured `AXIS(n) = 3` (for n=3 specifically here)
   should be exactly the count of these induced rays.

## Files

- `admissible_ops.py` — weight list, admissibility predicate,
  symbolic solution, brute-force enumeration, sanity expand-the-box
  check.
- `results.json` — weight list + constraint table + admissible OPS
  list + structural conclusion.

## Why this is informative (not negative)

A result of "zero admissible OPS" is not a failure — it's a
**structural fact** about the embedding GL(3) ↪ SO(6).  It means
the embedding is "balanced" (the normal bundle has weights coming
in opposite pairs), so the OPS-extremal cone collapses to a point.
This is consistent with `so(6)/gl(3) ≅ Λ²V ⊕ Λ²V*` being a
self-dual `gl(3)`-module.

For comparison:
- GL(2) ↪ SO(4) (analogous "rank 2" case): also `Λ²V ⊕ Λ²V*` but
  with only one `±e_1 + e_2`.  Same self-duality => same result.
- For `Sp(2) ↪ SL(4)`: the normal bundle is `Sym²V`, NOT self-dual.
  Many admissible OPS exist.

So self-duality of the normal bundle is the obstruction here.

## Reproducing

```bash
python3 admissible_ops.py
```
