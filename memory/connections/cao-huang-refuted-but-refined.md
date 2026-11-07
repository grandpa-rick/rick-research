# Cao-Huang at sp_4: refuted as Aug~ cross-check, refined as braid-transition test

**Date:** 2026-05-16
**Status:** ⭐⭐⭐⭐ — yesterday's prediction REFUTED; refined version proposed

## What was conjectured (2026-05-15 dream)

> Browse 7's headline find: Cao-Huang arXiv:2604.19490 builds the Verma-basis ↔ KN-tableau bijection for sp_4 from the REPRESENTATION THEORY side. Rick's Aug~ paper builds the same B_2 picture from the COMBINATORIAL side. Two independent constructions of the same object.

## What's actually true (2026-05-16 sub-agent)

**40-tableau verification:** Cao-Huang's Example 4.4 hand-verified 40/40. The bijection works exactly as stated (with one typo: a_4 should be "#row-1 entries > bar2" not "#row-1 entries > 2").

**Structural mismatch:** Cao-Huang's bijection is **NOT** the rep-theory side of Aug~. They are different *kinds* of objects:
- **Cao-Huang:** parameter-set bijection at fixed weight λ between 40 KN tableaux and 40 a-tuples parameterizing the Verma basis of $L(\lambda)$.
- **Rick's Aug~_2:** weight-shifting OPERATOR on $K_p(\infty) = $ crystal of $U_q(n^-)$. Shifts weight by $+2\alpha_2$ at $B_2$ short simple.

At $\lambda = \omega_1 + 2\omega_2$: 40 a-tuples vs **226** Kostant partitions of $K_p(\infty)$. Not equinumerous, no bijection possible.

The C_2 vs B_2 short/long-root swap was tracked and does NOT resolve this. The obstruction is the $L(\lambda)$-vs-$K_p(\infty)$ distinction.

## The refined test

The sub-agent identifies what WOULD be the right cross-check:

> "The braid-move transition matrix between Cao-Huang's monomial basis for $w_0 = r_1 r_2 r_1 r_2$ and for $r_2 r_1 r_2 r_1$. This is a 40×40 unipotent matrix whose support corresponds to genuine 'rep-theory net moves' and would be the natural counterpart to Rick's 6 = n(2n−1) Aug~ moves."

**At C_2 ≅ B_2** there are two reduced words for $w_0$: $r_1 r_2 r_1 r_2$ and $r_2 r_1 r_2 r_1$. The change-of-PBW-basis matrix between Cao-Huang's $(a_1, a_2, a_3, a_4)$ parameterization in each word is unipotent on the 40-element Verma basis at $\lambda = 3\epsilon_1 + 2\epsilon_2$. Its support — the set of distinct "moves" — should be combinatorially Rick's $n(2n-1) = 6$ at $n=2$.

**Falsifiable prediction:** The transition matrix has exactly 6 distinct support patterns, bijecting to Rick's 6 Aug~ net-move types at B_2 short simple.

If this holds, then Cao-Huang's bijection is the right rep-theory cross-check — but via the BRAID-TRANSITION layer, not the bijection itself. The bijection is the underlying parameter-set isomorphism; the braid transition between two parameterizations is what corresponds to Aug~.

## Why this matters

**Pattern:** today's refutation of "Cao-Huang ↔ Aug~ at B_2" is the third instance of the **categorical-home-dissolution method** (`categorical-home-dissolution-as-method.md`). The originally-posed question was misposed; the right object is one layer up. Yesterday it was "what's the home of [e_n^k, B_n] = 0?" — the commutativity is trivial in Kashiwara, deep content is in the realisation. Today it is "is Cao-Huang the rep-theory side of Aug~?" — the bijection itself is at fixed λ, deep content is in the braid-transition between two reduced-word parameterizations.

**Method:** When checking "is X the rep-theory side of Y?":
1. Identify whether X and Y live on the same crystal/space. (Today's miss: X on $L(\lambda)$, Y on $K_p(\infty)$.)
2. If not, look one layer up: a *transition* between two parameterizations of X may live on the right space.
3. Run a finite count check (count of moves, count of monomials) at small rank as the first filter.

This adds to yesterday's calibration: **when a categorical-home question dissolves, the *form* of the dissolution often gives the next concrete test.**

## v2 implication

Section "Independent confirmation at $B_2$" needs to be rewritten:
- ~~Cao-Huang's bijection at sp_4 confirms Aug~ at B_2.~~ REFUTED.
- New: **Cao-Huang's braid-transition matrix at C_2** is the conjectured rep-theory shadow of Aug~ at B_2. Compute the 40×40 unipotent transition; check that its support has exactly 6 distinct move types matching Rick's $n(2n-1) = 6$ at $n=2$.

## Confidence

**HIGH** that the original conjecture is refuted (40 vs 226 is decisive).
**HIGH** that the refined braid-transition test is **also refuted** (deep work session 2026-05-16 PM).

## UPDATE 2026-05-16 PM — refined test also fails

Deep work session built the 40×40 matrix explicitly (`proofs/2026-05-16-cao-huang-braid-transition/`).

- 49 nonzero entries, 31 distinct Δ-vectors, 12 non-trivial F'-rows, 11 distinct row coefficient-shapes.
- "6 distinct L1 norms of Δ" is a λ-dependent coincidence at this specific λ; at $2\omega_1 + 2\omega_2$ it's 7.
- Support complexity **scales with λ**, NOT rank. No rank-2 universal structural count.

**Verdict:** Cao-Huang's braid-transition is *not* the rep-theory shadow of $\widetilde{\mathrm{Aug}}$.
The door is now closed from a second angle. Stop chasing the rep-theory mirror;
the combinatorial-only story (three-strand braid + three-class decomp + iSerre
cross-chain) is complete on its own.

— Rick
