# Watanabe AI-crystal as precedent (and contrast)

**Date:** 2026-05-16
**Status:** ⭐⭐⭐⭐⭐ — keystone positioning insight for v2

## What Watanabe has (arXiv:2107.00170, JACO 2023)

For $\mathfrak{so}_n \subset \mathfrak{gl}_n$ (type AI), Watanabe builds:

- **Tableau model:** $\mathrm{SST}_n^{\mathrm{AI}}(\rho) \subset \mathrm{SST}_n(\rho)$ — subset of ordinary semistandard tableaux satisfying an AI-condition (column-length bound + first-column inequality).
- **AI-crystal operators (Def 2.3.1):**
  $$ \widetilde B_i \, b = \begin{cases} \widetilde E_i \, b & \varphi_i(b) \text{ even} \\ \widetilde F_i \, b & \varphi_i(b) \text{ odd} \end{cases} $$
  plus $\deg_i(b) \in \mathbb{Z}_{\ge 0}$, derived from $\varepsilon_i$ + parity bit.
- **Relations:**
  - $\widetilde B_i^2 = \mathrm{id}$ (involution),
  - $\widetilde B_i \widetilde B_j = \widetilde B_j \widetilde B_i$ for $|i-j| > 1$ (commutation; Prop 2.3.10),
  - $\pm 1$ degree-shift at $|i-j| = 1$.
- **Character / branching:** $\mathrm{ch}\,V^{\mathfrak{so}_n}(\rho)$, $\mathfrak{gl}_n \downarrow \mathfrak{so}_n$ via $\mathfrak{so}_n$-oscillating tableaux.
- **K-matrices** $K^{(k)}$ (bar-complementation) used as bijections, *not* as braid generators.

## What Watanabe does NOT have

- **No braid relation.** No three-strand-braid, no longer-than-Coxeter relation. Only $\widetilde B_i \widetilde B_j = \widetilde B_j \widetilde B_i$ for $|i-j| > 1$.
- **No cactus action.**
- **No catalog of moves.** No $n(2n-1)$-style decomposition.
- **No type BDI extension.** Setup is entirely $A_{n-1}$ Dynkin. Intro explicitly says "no general theory unifying" his two iquantum crystal constructions (AI and AIII$_{2r}$).
- **No bidegree.** Pure crystal-level structure, no $(q, t)$-grading.

## Rick's three-strand braid theorem in this map

Rick at type BDI = $B_n$ short simple has:
- **Catalog of $n(2n-1)$ distinct net moves** of $\widetilde{\mathrm{Aug}} = e_n^{k(n)}$ on (w, π) pairs.
- **Three-class decomposition:** $3(n-1)$ intra-chain + $2(n-1)(n-2)$ cross-chain + $(2n-1)$ singleton-involving.
- **On-slice = squared off-slice** structurally.
- **PROVED type-uniform 2026-05-15.**

The braid relation that organizes this catalog is at depth $k$ (the on-slice exponent) — squaring is what bridges the chains and produces the cross-chain class. Watanabe's commutation $\widetilde B_i \widetilde B_j$ for $|i-j| > 1$ is *adjacent-Dynkin commutation between distinct nodes*. Rick's catalog is *non-trivial structure at a single node at depth $k$*. They are not in conflict — Rick's structure sits at depth $k$, Watanabe's at depth 1 between different nodes.

**The structural positioning:** Rick's theorem is the first braid-theoretic ("higher-than-commutation") result on an iquantum-tableau-crystal model. Watanabe AI-crystal is rank-uniform at depth-1; Rick BDI-crystal has higher-depth braid structure.

## The Z/2-folding analogy

Watanabe's $\widetilde B_i$ is a *parity-controlled collapse* of $(\widetilde E_i, \widetilde F_i)$ on a string. Rick's "on-slice as squared off-slice" is a Z/2-folding of off-slice two-strand primitives into on-slice unordered pairs. Both are Z/2-refinements of Kashiwara crystal — but at *different levels*:
- Watanabe: Z/2-folding of $E_i, F_i$ into $B_i$ at depth 1 between distinct nodes.
- Rick: Z/2-folding of off-slice $e_n, f_n$ into on-slice $e_n^k$ at depth $k$ at a single node.

This suggests the right framework is a **graded Z/2-refinement** indexed by depth $k$, with Watanabe at $k = 1$ and Rick's catalog appearing at higher $k$. A natural conjecture: at $k = 1$ in Rick's setup, the catalog collapses to Watanabe's commutation relations. **Falsifiable: check whether $\widetilde{\mathrm{Aug}}$ at $k = 1$ at type BDI reduces to a commutation relation between Watanabe-style $\widetilde B_i$ operators.**

## V2 positioning

Frame Rick's paper as:
1. **The first braid relation on an iquantum-tableau-crystal model.** (Contrast: Watanabe AI-crystal only has commutation.)
2. **The first ι-crystal structure at type BDI.** (Watanabe explicitly notes the gap.)
3. **A graded refinement of Kashiwara crystal at higher depth.** (Watanabe = depth 1; Rick = arbitrary depth $k$.)

Cite Watanabe 2107.00170 as the precedent in the introduction. Position Rick's catalog as the natural depth-$k$ extension.

## Action items

1. Test the $k = 1$ collapse hypothesis: does Rick's $\widetilde{\mathrm{Aug}}$ at $k = 1$ at $B_n$ short simple reduce to a commutation relation, matching Watanabe AI?
2. Find whether Watanabe's AI-crystal axioms admit a depth-$k$ generalization — if yes, Rick's catalog should be expressible in those terms.
3. Email Watanabe (post-v1 reception) with the depth-$k$ framing? Plausible bridge for a co-author / referee chain.

— Rick
