# Connection — Two independent combinatorial proof routes for (Re)

> **STATUS: PARTIALLY SUPERSEDED by Day 188 novelty audit.**
> (Re) is **Alexandersson-Panova 2018 Thm 38 eq (22)**, not Rick's. The identity is proved in AP2018 via LLT/Dyck-path combinatorics. Route A (Chow watershed) and Route B (GDL-W bond lattice) both aim at (Re) → they are now potentially machinery for the surviving $(q,t)$-lift arc, not new proofs of a Rick-owned identity.
>
> **What carries forward:** The two structural routes (watershed vs. bond lattice) may generalize to $(q,t)$-CQF. If either does, that would be a new theorem (AP2018's combinatorial model does not $(q,t)$-lift). See `2026-09-11-qt-slot-open-hikita-recipe-unused.md`.

**Date:** 2026-09-10 (Day 187 dream)
**Paths:** Path 3 (Ellzey-Wachs $q$-CQF, Hecke deformation) ↔ Path 4 (crystal / coproduct / combinatorial models on graphs)
**Registry anchors:**
- `path-graph-qGF.json` (Day 187 `checked-sober`)
- `chow-watershed` (2603.23879)
- `gdl-w-bond-lattice` (2608.08692)

## Setup

Day 187 promoted the empirical h-basis $(q)$-GF to `checked-sober` on $n=1..8$ with three algebraically-equivalent forms. The combinatorial / bijective proof of the recursion
$$X_{P_n}(q) = e_n + q \sum_{k=2}^n [k-1]_q\, e_k\, X_{P_{n-k}}(q) \tag{Re}$$
(or equivalently the manifestly-positive (Comp) formula) remains open.

Four combinatorial-proof angles tried Day 187, none closed. Browse 139 identified **two independent structural routes** into (Re) via different pieces of Path 4 machinery.

## Route A — Chow watershed (2603.23879)

**Mechanism.** Chow defines a random-permutation-driven process $W$ on the Hessenberg framework. Hikita's e-coefficients satisfy
$$\phi_c = P\{\mathrm{watershed}(\pi) = c\}$$
where $\pi$ is drawn from a specific distribution and $c$ ranges over compositions.

**Specialization to $P_n$.** The path graph has Hessenberg function $e(i) = i+1$ (Shareshian-Wachs notation). Chow's process $W$ has parameters $a_i, b_i$ depending on the Hessenberg data. **What are $a_i, b_i$ for $P_n$?** This is the blocking sub-question — Chow doesn't work out this specialization in the paper.

If tractable (educated guess: $a_i = 1$, $b_i = i$ or similar), then $\phi_c$ for path graphs becomes an explicit probability, and (Re) follows from a corresponding recurrence on random-permutation classes.

**Pro:** Direct — the coefficients of Rick's GF *are* the probabilities in Chow's model. If we can specialize the parameters, we have a bijective proof by construction.
**Con:** Requires reading Chow §2–3 carefully and doing the parameter reduction. Machinery-heavy.

## Route B — GDL-W bond lattice (2608.08692)

**Mechanism.** González D'León – Wachs define a multiweighted bond poset $B(G)$ for each graph $G$; the top Möbius invariant $M_G$ satisfies
$$(-1)^{n-1} \omega\, M_{P_n}(x) = \text{Haiman's parking function symmetric function on } n.$$
The h-expansion of $M_{P_n}$ can be computed from an EL-labeling on $B(P_n)$.

**Test.** Does $M_{P_n}$'s h-expansion (up to sign twist $(-1)^{n-1}\omega$) match Rick's $Z(z)|_{q=1}$? Both are formulas indexed by $n$ in the h-basis; comparing them for $n=1..5$ is a 20-minute sober script.

**If yes:** GDL-W's EL-labeling on the bond lattice IS the combinatorial mechanism behind (Re) at $q=1$. Extending to $q > 0$ (Ellzey-Wachs) is then a $q$-analogue of the EL-labeling statistic, which is exactly the kind of thing Wachs has worked out (see the ascent statistic on bond lattices).

**Pro:** Tractable in the short term — GDL-W provide an explicit Narayana formula for $P_n$. Comparison to Rick's $Z$ at $q=1$ is a direct polynomial-level check.
**Con:** Only gives the $q=1$ case directly. Need a $q$-lift of EL-labeling to get (Re) in full generality.

## Why both routes matter

The two routes are **structurally different** decompositions:
- **Route A is probabilistic** — partition permutations by a topological invariant (watershed).
- **Route B is order-theoretic** — EL-labeling on a poset of bonds.

**Meta-observation.** If *both* routes close, we get two independent combinatorial proofs of the same identity. That's better than one: it means (Re) has multiple structural homes, each linking to a different piece of Path 3/4 machinery. A **bijection between watershed classes and bond-lattice atoms** would unify them, and would be a new theorem in enumerative combinatorics (independent of the (Re) proof).

## Priority

**Route B first (Day 188 wake, ~30 min).** Cheap, tractable, and gives the $q=1$ case immediately.

If Route B matches Rick's $Z$ at $q=1$, proceed with Route B's $q$-lift as Day 188+ PROVE target.

If Route B doesn't match, fall back to Route A and read Chow §2–3.

## Seed connections

- Path 3 (Hecke deformation): The $q$ in (Re) is Ellzey-Wachs $q$, which is the Hecke parameter. Either route produces a $q$-statistic (ascent / weight).
- Path 4 (crystal / coproduct): The coproduct of $X_G(q)$ under disjoint union is what makes Huh's restricted modular law bite. Bond lattices carry a natural product structure that mirrors this.

## Follow-up

- `questions/q-chow-watershed-Pn-parameters.md` — Route A blocking sub-question.
- `questions/q-GDL-W-M-Pn-matches-Rick-Z.md` — Route B feasibility check.
- Combinatorial proof would close the FPSAC 2027 abstract as *proved*, not just *stated*.

## Not overclaiming

Neither route has been executed yet. Both are structural sketches. Route B's feasibility check is the cheapest test on the near horizon (Day 188). If neither route closes, the (Re) recursion still stands at `checked-sober` on $n=1..8$ + Stanley 1995 $q=1$ match — FPSAC-abstract-quality regardless.
