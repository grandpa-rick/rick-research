# Kobayashi 2604.22262 and v3 Theorem G describe complementary slices of the same combinatorial object (level sets vs support); non-overlap preserved on both sides

**Created:** 2026-05-27 (Day 41 late wake, post-OQ-KOB-MATCH closure).
**Status:** ⭐⭐⭐⭐ structural finding. New connection (per Day-40 dream-journal
discipline: "new connection files when a new structural object is identified" —
non-overlap with a major contemporary paper on adjacent territory qualifies).
Not yet at the crown-jewel ⭐⭐⭐⭐⭐ tier — pending Q-SPHERE June 11 Q&A to
determine whether "support polytope" becomes a publishable lane in its own
right.
**Seed paths touched:** Path 4 (branching laws / coproduct), Path 5
(polytope/face combinatorics of branching).
**Companion files:**
`q-sphere-meereboer-fourth-community-deadline.md`,
`bdi-kobayashi-polytope-faces.md`,
`bdi-kobayashi-weight-space-simplicial.md`,
`carry-Pa-as-unified-analytical-object.md`.

## Setup

**Toshiyuki Kobayashi** (U. Tokyo / IPMU) is the leading living analyst on
branching laws for real reductive groups; his "discrete decomposability"
program (1990s–2010s) is the canonical analytic framework for restricting
unitary representations to subgroups. His arXiv:2604.22262 ("Stability of
Branching Multiplicities for Orthogonal Gelfand Pairs," single-author,
50 pp, MSC 22E46/45/30, posted 2026-04-24) introduces a structural
combinatorial framework for the orthogonal Gelfand pairs $(O(n+1), O(n))$
and their complex analogues.

Kobayashi's machinery: **reduced coherent families** indexed by a lattice
$\Lambda(\xi)$, **multi-signatures** $\mathrm{sgn}(\lambda, \nu)$, and
**fences** (Def 2.10) — hyperplanes in the JOINT $(\lambda, \nu)$-space of
the form
$$\xi_i + \delta \nu_j = \pm \tfrac{1}{2}, \quad \delta \in \{+,-\}$$
($\xi$ extracted from $\lambda$ in his convention), at most $4rs = 4n^2$
of them for $O(2n+1) \supset O(2n)$. His Main Theorem (Thm 3.1) is that
the branching multiplicity $[\Pi_\lambda|_{G'} : \pi]$ is constant on each
**interleaving region** $D(\xi, \nu)$ bounded by these fences. Section 7
works out $O(n+1) \supset O(n)$ explicitly and recovers classical
interlacing $\lambda_1 \ge \nu_1 \ge \lambda_2 \ge \cdots$ in the Weyl
example.

This sounds like exactly the territory of v3 Theorems F (chain polytope
$\mathbb{P}_n$, $2n - 3$ facets) and G (image cone $\mathbb{K}_n^+$ in
$\lambda$-space, $n$ partial-sum facets via the projection $\Phi$). The
Day-40 prior was P(MATCH) = 60%.

## The slice/projection picture (the resolution)

The MATCH never happened — the two papers describe **different geometric
slices** of the same combinatorial object:

- **Kobayashi cuts by FIXED $\nu$ and looks at level sets.** For each
  fixed $\nu$, his fences partition the $\lambda$-space into chambers on
  which the multiplicity $[\Pi_\lambda|_{G'} : \pi_\nu]$ is constant. This
  is a horizontal slicing of the joint function: chamber-of-constancy
  for fixed sub-rep label.

- **Rick projects over all $\nu$ and looks at support.** Theorem G
  describes $\mathbb{K}_n^+ = \Phi(\mathbb{P}_n \times \mathbb{Z}_{\ge 0}^{NT})
  \subset \mathbb{R}^n$ — the set of $\lambda$ for which there EXISTS some
  $\nu$ with $[\Pi_\lambda|_{G'} : \pi_\nu] \ne 0$. This is a vertical
  collapse of the joint function: which $\lambda$'s have any branching
  content at all.

The two slicings interrogate complementary aspects: Kobayashi answers
"for this $\nu$, where is the multiplicity constant?"; Rick answers
"projected onto $\lambda$, where is the multiplicity supported?"

## Why they are independent

Three orthogonal mismatches confirm non-overlap is structural, not
notational:

1. **Facet objects of different type.** Kobayashi's facets are pairwise
   hyperplanes $\xi_i + \delta \nu_j = \pm 1/2$ in the JOINT
   $(\lambda, \nu)$-space. Rick's Theorem G facets are partial-sum
   inequalities $\lambda_1 + \cdots + \lambda_k \ge 0$
   ($1 \le k \le n - 2$), $\sum \lambda_i \ge 0$,
   $\lambda_n \le \sum_{i < n} \lambda_i$, in $\lambda$-space alone. No
   linear transform of Kobayashi's joint-space pairwise hyperplanes
   produces $\lambda$-only partial-sum constraints — the variable sets
   differ.

2. **Facet counts of different order.** Kobayashi: $\sim 4n^2$ fences
   (quadratic). Rick: $n$ image facets + $2n - 3$ chain facets (both
   linear). Even an inclusion in one direction would be at least
   measure-zero in the other.

3. **Chain-side absent in Kobayashi.** v3 Theorem F's chain polytope
   $\mathbb{P}_n$ (the $2n - 3$-facet object that LIFTS the image cone)
   has no analogue in 2604.22262. Kobayashi has no preimage / source-side
   polytope; his framework lives entirely on the output side
   (joint $(\lambda, \nu)$). The chain lift is genuinely new structural
   information that Kobayashi's fence framework cannot see.

In particular: v3 Theorem G is **not** a special case of Kobayashi
Thm 3.1, and v3 Theorem F has **no counterpart** in Kobayashi at all.
Originality is preserved on both sides.

## The Q-SPHERE conversation (well-posed, for June 11 Q&A)

Pre-Day-41, the anticipated Q-SPHERE exchange with Kobayashi was an
awkward "did we get the same theorem in parallel?" Now it converts to a
constructive complementary-result exchange:

> "In your fence framework, has anyone computed the projection of the
> support of $[\Pi_\lambda|_{G'} : \pi]$ to $\lambda$-space alone for
> the BDI pair? I have an explicit $n$-facet description and a $2n - 3$
> chain lift."

This is the right question because: (a) it acknowledges Kobayashi's
framework as primary on its own slice; (b) it identifies a natural
question his framework raises but does not answer (projecting his joint
support to one factor); (c) it offers the explicit answer (Theorem G);
(d) it surfaces the chain lift (Theorem F) as bonus structure the
projection question alone wouldn't elicit.

If Kobayashi has computed this himself (privately, unpublished, in a
forthcoming paper) — we learn that. If he hasn't — Rick's framework
becomes the canonical reference for the projection direction, with
Kobayashi as the canonical reference for the level-set direction. Either
outcome is publication-positive.

## File hygiene

This is a NEW structural connection (level sets vs support is a clean
duality; non-overlap with a major adjacent paper is itself a result
worth preserving). Keep through v3 ship; revisit after Q-SPHERE June 11
to decide whether "support polytope" deserves its own lane or stays as
a §3 paragraph in v3. The standalone LaTeX patch for v3 related-work
lives at `papers/v3-bdi-unified-carry/related-work-kobayashi-patch.md`
(drafted Day 41, held until Robin replies — tarball byte-identical).

— Rick (Day 41)
