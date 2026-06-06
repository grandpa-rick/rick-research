# Liao, Yang, Yu — Combinatorial equivalence of separable elements in types A and B

**Date skimmed:** 2026-05-12
**arXiv:** 2510.12046v1 (14 Oct 2025)
**Authors:** Yong Liao, Yuping Yang, Houyi Yu (Yu corresponding)
**Length:** ~30 pages, math.CO

## One-sentence abstract
Constructs a bijection phi_n : K(S_{n+1}) -> K(B_n) between separable permutations and separable signed permutations that preserves descents and induces a poset isomorphism under the *left weak order*; derives gamma-positivity of the descent polynomial and product formulas for principal ideals.

## Definition of "separable"
- **Type A (classical):** w in S_n is separable iff it avoids the patterns 3142 and 2413; equivalently, w can be built from the singleton 1 by iterated direct sum and skew sum operations.
- **Type B (after [21, Lemma 3.5] = Gao-Hong/related):** signed w in B_n is separable iff it avoids the (signed) patterns 21bar, 2bar1, 3142, 2413, 3bar1bar4bar2bar, 2bar4bar1bar3bar; equivalently, generated from {1, 1bar} by direct/skew sum.
- General Weyl-group definition: Gaetz-Gao [16] via root-system pattern avoidance (Billey-Postnikov framework).

## What the A<->B bijection preserves
| Structure | Preserved? |
|---|---|
| Cardinality (Schroeder numbers) | yes |
| Descent number (desA = desB) | yes |
| Double descents | yes |
| Left weak order (poset iso) | yes |
| **Length / rank** | **NO — domain has rank n(n+1)/2, codomain has rank n^2; bijection is NOT a graded poset map** |
| Bruhat order | not addressed |
| Right weak order | not addressed |

The fact that ranks differ (length(B-perm) = #Neg+#Inv+#Nsp vs length(A-perm) = #Inv only) is explicit in eq. (5). Figure 1 shows the parenthesised lengths and they do NOT match across the bijection.

## Representation-theory content
- **No mention of:** BGG resolutions, Verma modules, Kazhdan-Lusztig polynomials, Kostant partitions, q,t-weight multiplicities, sign-reversing involutions, derived categories, Lie algebra cohomology.
- **Only RT touch-point:** cites Gossow-Yacobi (Math. Z. 2025) on action of separable elements on canonical bases — used as motivation, not pursued. (Rick already has notes on Gossow-Yacobi.)
- Hopf-algebra mention is only in references [1] (Aguiar-Sottile) and [32] (Yu's own paper on weak order Hopf algebra).

## Lineage of "separable elements"
Bose-Buss-Lubiw 1998 (pattern matching) -> Gaetz-Gao 2020/2023 (general Weyl groups, root-pattern characterization) -> Gao-? [21] (type-B pattern characterization) -> this paper.

## Direct relevance to Aug~ / BGG-differential program
**TANGENTIAL.** The paper is purely combinatorial (descent statistics, weak order, rank generating functions). It does not engage with derived/BGG combinatorics, Verma supports, or any sign-reversing involution machinery. The A<->B bijection lives at the level of *coarse poset structure* (left weak order, descent), which is unrelated to the *fine bidegree-graded* data Aug~ acts on. Crucially, the bijection does NOT preserve length, so it cannot lift to a length-graded (=bidegree) map between BGG resolution complexes.

## Verdict — P3
**File under "interesting but not now."** Worth knowing this exists if Rick later wants enumerative input (Schroeder numbers, gamma-positivity) on type-B separable elements, but it does not provide an A<->B bridge that respects derived combinatorics. The Gossow-Yacobi reference [17] (canonical bases) is the more promising RT thread — already in Rick's notes.

## Unexpected connections
- The recursive direct-sum/skew-sum construction in type B uses **two** generators {1, 1bar} instead of one. If Aug~ ever needs a "type-B atomic generator" picture, this might suggest the bar-version of a base case.
- gamma-positivity of the type-B descent polynomial is a hallmark of nice cell decompositions; if Aug~-fixed-point sums turn out to be gamma-positive, that's a hint to look for an underlying cellular/CW-complex structure paralleling theirs.
- The left-weak-order poset iso (despite different lengths) is an example of a "shape-preserving but not graded" A<->B map. Possibly relevant as a cautionary example: a useful A<->B bridge need not be length-graded, but Aug~-respecting bridges presumably must be.
