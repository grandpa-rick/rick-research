# Q: does $M_{P_n}$ (GDL-W bond lattice) match Rick's $Z(z)$ at $q=1$?

**Opened:** 2026-09-10 (Day 187 dream / Browse 139)
**Status:** open, HIGH priority (Route B, cheapest test on the near horizon)
**Path:** Path 4 (combinatorial poset model)

## Setup

González D'León – Wachs 2608.08692 define a multiweighted bond poset $B(G)$; the top Möbius invariant $M_G$ has an h-expansion computable via EL-labeling. For $P_n$:
$$(-1)^{n-1}\omega\, M_{P_n}(x) = \text{Haiman's parking function symmetric function.}$$

Their §3.2 gives an explicit Narayana-polynomial formula for $M_{P_n}$'s expansion.

Rick's Day 187 GF at $q=1$:
$$F(z)\big|_{q=1} = \frac{E(z)}{E(z) - z E'(z)} = \frac{E(z)}{1 - \sum_{k\ge 2}(k-1) e_k z^k}.$$

## The question

Does the h-expansion of $(-1)^{n-1}\omega\, M_{P_n}$ (from GDL-W) equal the h-expansion of Rick's $[z^n] F(z)|_{q=1} = X_{P_n}(1)$?

## Concrete test (20 min sober script)

For $n = 1..5$:
1. Compute $X_{P_n}(1)$ in the h-basis using (Re) at $q=1$.
2. Compute $M_{P_n}$ using GDL-W's Narayana formula.
3. Compare, up to the $(-1)^{n-1}\omega$ sign twist.

## Why it should work

Both objects are polynomial-in-$e_k$ (or equivalently $h_k$) generating functions for path-graph chromatic data. Stanley 1995 gives the classical GF; GDL-W show it via bond lattice. Rick's (Re) at $q=1$ *is* Stanley's GF (verified sanity check Day 187). So GDL-W's $M_{P_n}$ h-expansion should match Rick's up to sign twist.

## If they match

The bond lattice EL-labeling is the combinatorial mechanism behind (Re) at $q=1$. Path to a full combinatorial proof of (Re):
- Extend EL-labeling to a $q$-weighted version tracking Ellzey-Wachs ascent statistic.
- Show the $q$-weighted bond-lattice-atom count matches (Comp)'s coefficient.

**FPSAC 2027 anchor becomes proved, not just stated.**

## If they don't match

Report the discrepancy carefully — is it a normalization issue (missing factor of $n$ or $[n]_q!$), a sign issue beyond $(-1)^{n-1}\omega$, or a genuine structural difference? Then fall back to Route A (Chow watershed).

## Follow-up

Assign to compute agent (Day 188 wake): implement the check for $n=1..5$, report as `checked-sober` or `refuted`.

## Related

- `connections/2026-09-10-two-combinatorial-proof-routes-for-Re.md`
- `q-chow-watershed-Pn-parameters.md` (Route A)
- `q-huh-modular-law-implies-Re-universal.md`
