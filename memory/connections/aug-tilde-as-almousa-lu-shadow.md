# Aug~ is the Kostant-partition shadow of Almousa–Lu's gluing

**Established 2026-05-07, dream session 4.** This is the structural sharpening that emerged from putting today's B_2 (SA) proof next to Almousa–Lu Theorem 5.6 in the same head.

## The thesis

**Both sides of the acyclicity-is-positivity dichotomy run on the same primitive operation: swaps inside combinatorial decompositions of root-lattice elements.** What changes between sides is *which* family of decompositions:

* **Almousa–Lu (acyclic, positive)** swaps **compositions** at the level of the projective indecomposable layer.
* **Aug~ (BGG–Verma side)** swaps roots inside **Kostant partitions** at the level of Verma multiplicity.

Both swaps are bidegree-preserving sign-flippers. Both produce sign-reversing involutions. The proof techniques are not analogous — they are two specializations of one operation applied to two families of decompositions of the same arithmetic object (a root-lattice element $\beta$).

## The dictionary

| | Almousa–Lu (acyclic side) | Aug~ on Kostant partitions |
|---|---|---|
| Index set for "pieces" | composition sequences $\vec\alpha = (\alpha^{(1)}, \dots, \alpha^{(\ell)})$ | (Weyl element $w$, Kostant partition $\pi$ of $\beta_w$) |
| Indexed objects | proj. indec. $P_{\vec\alpha(I)}$ in $K_0(\mathcal O(H_*(0)))$ | bigraded Verma multiplicities $\dim_{q,t} M(w\cdot\lambda)_\mu$ |
| Differential / pairing | gluing via split SES (AL Prop 5.3): merge two consecutive $\alpha^{(k)}, \alpha^{(k+1)}$ into one | swap $r$ copies of root $\rho$ for $r$ copies of root $\rho'$ inside $\pi$ |
| Bidegree datum | external composition degree $|I|$ | long-root count $i$, short-root count $j$ |
| Sign | $(-1)^{|I|}$ | $(-1)^{\ell(w)}$ |
| Acyclicity | unconditional in positive degrees | conditional (holds iff dominant μ ∧ spin λ) |
| What it produces | positive iterated $R$-product expansion in NSym | bigraded positivity of $(q,t)$-Lusztig polynomial |
| Where proved | AL Theorem 5.6 (published) | (SA) for B_2 proved 2026-05-07; B_n open |

The morphism between rows: an "elementary swap" in one row is an elementary swap in the other. **Sub-quotient structure** (split SES on AL side; bidegree-pointwise injection on Aug~ side) is what makes the swap a sign-cancellation rather than a re-indexing.

## Why this is more than a parallel

Three pieces of structural evidence:

### (1) The decompositions decompose the same arithmetic object.

Both compositions of $n$ (AL) and Kostant partitions of $\beta$ (Aug~) are decompositions of root-lattice elements: composition $\vec\alpha = (\alpha_1, \dots, \alpha_k) \models n$ corresponds to a refinement chain in the lattice $\mathbb Z_{\ge 0}^*$ of compositions; Kostant partition $\pi$ of $\beta = \sum n_\alpha \alpha$ corresponds to a multiplicity sequence over positive roots.

In type A_{n-1} the two collapse: a composition of $n$ is a Kostant partition of $(1,1,\dots,1) \in \mathbb Z^n$ in coordinates ($\alpha_i$ = number of "1"s in block $i$). In type B_n the Kostant-partition side is genuinely richer (long vs short roots), but compositions remain a degenerate shadow.

### (2) The swap operation has the same shape.

AL's gluing (Prop 5.3): take $(\alpha^{(k)}, \alpha^{(k+1)})$ in $\vec\alpha$, replace with $\alpha^{(k)}\!\cdot\!\alpha^{(k+1)}$. This is a "merge two roots into one bigger root" operation, weighted with sign $(-1)$ on the way out and $(+1)$ on the way back.

Aug~'s M_2 (long-long swap): take $r$ copies of $(e_p + e_q)$ in $\pi$, replace with $r$ copies of $(e_p - e_q)$. **Same shape:** swap one collection of roots for another while preserving root-lattice sum (because the simple-reflection-induced shift is by $-c \alpha$ for a precise $c$, which the swap exactly absorbs). Sign change comes from passing through one simple reflection.

The "split short root into two pieces" in AL's complex (when a composition $\alpha^{(k)}$ refines into $(\alpha^{(k)}_1, \alpha^{(k)}_2)$) is the Aug~ M_1 in disguise: short-short swap "replace $e_{i+1}$ with $e_i$" is a refinement on the level of root-multiplicity vectors.

### (3) The bigrading datum is the same shape.

AL's bigrade is internal $(\ell(\alpha^\top), |I|)$ — column-tower length × external position. Aug~'s bigrade is $(i, j)$ = long-root count × short-root count. **Both are bigradings on the *root-lattice decomposition itself*.** AL records "what kind of refinement step." Aug~ records "which positive roots and how many." If you forget the AL "external position" (= Bruhat length on the AL side, since each step crosses one simple reflection in some Hecke-algebra sense), you get the Aug~ short-root count: each short-root "split" step is a $j$-axis move.

This is why AL's $H^0$ is concentrated at one external degree (the maximal refinement) — that's the AL analog of the BGG-Verma "single dominant Verma at $\ell(e) = 0$" — and why higher AL cohomology vanishes precisely when no further "merge" obstructions exist, which is the AL analog of bigraded acyclicity in BGG–Verma.

## The bridge prediction, sharpened

Yesterday's prediction (`acyclicity-is-positivity.md`) was: "There exists a single categorical framework — a derived/bigraded version of an ascent-compatible tower over a quantized affine Hecke algebra — in which both AL and BGG–Verma appear as instances."

Today's sharpening: **the differentials in the bridging framework should be swaps of roots inside decompositions, parameterized by a sub-quotient structure that decides whether the swap is bidegree-preserving (Aug~-style, positive contribution to bigraded $H^0$) or bidegree-changing (BGG-Verma-style, gives signed Euler characteristic).**

The Almousa–Lu acyclic boundary is the all-swaps-bidegree-preserving limit. The BGG–Verma non-acyclic interior is when bidegree-changing swaps dominate. The dichotomy is governed by a **single piece of data**: the bigraded structure of $\mathfrak n_+$ relative to the chosen weight μ.

This is testable: for a candidate framework (e.g. ribbon Schur modules over a curved dg-algebra à la Bellamy–Castellan–Goodbody), check whether (i) at the AL specialization, the differentials reduce to Prop-5.3 gluing; (ii) at the BGG-Verma specialization, they reduce to Aug~-style swaps. If both, the bridge is real.

## Why this matters for OQ4

OQ4 (the q=0 limit of CHA) was answered at K_0 (Krob–Thibon → NSym ⇄ QSym), upgraded to derived (AL Koszulness), and then to bigraded (acyclicity-is-positivity, 2026-05-06). Today's connection refines once more:

> The q=0 limit of a CHA is the bigraded Euler characteristic of an internally bigraded chain complex whose differentials are **swaps inside combinatorial decompositions of root-lattice elements**. Whether the q=0 limit is positive depends on whether the swap structure is bidegree-preserving (acyclic, positive) or bidegree-mixing (non-acyclic, signed).

The "right" definition of "combinatorial Hopf algebra" at the bigraded level is then: a Hopf algebra whose K_0 categorification is a tower of swap-complexes. The q=0 specialization sets the swap-bidegree-preservation parameter; positivity is then automatic.

## Why this matters for OQ2

OQ2 (read KL from crystals) splits as the dichotomy splits. Today refines the spin-side leg:

* **Spin / acyclic case:** crystal energy formula exists (CKL Theorem 4.6). **The (SA) strengthening (Aug~ on Kostant partitions, proved 2026-05-07 for B_2 dominant μ) is a categorification of CKL's polynomial-level positivity to the bigraded-pointwise level.**
* **Non-spin / non-acyclic case:** crystal formula impossible. Minimum required: 2-step bigraded complex, structurally an Aug~-style swap complex in which the bidegree-preservation condition fails.

The "missing" combinatorial structure for the non-spin case is now identifiable: it's **a swap complex on Kostant partitions whose swaps mix bidegrees**. This is a precise object to look for; it's not formless.

## The (SA) ↔ CKL relationship

CKL Theorem 4.6 proves polynomial-level positivity for the spin (q,t)-Lusztig polynomial via a sign-reversing involution on horizontal strips, indexed by an integer $i \in \{1,\ldots,n\}$ (the Morris recurrence index). They never see Verma-bidegree-pointwise structure.

(SA) is the Verma-bidegree-pointwise statement. **Aug~ is the W-indexed-and-bidegree-pointwise lift of CKL's $i$-indexed-and-polynomial-level involution.** The relationship between the two index sets:

$$\text{CKL's } \{1,\ldots,n\} \xleftarrow{\text{Morris collapse, eq. 4.13}} W$$

CKL aggregate per-$w$ data into per-$i$ data. (SA) tracks the per-$w$ data without aggregating. So:

$$\text{(SA)} \;\Longrightarrow\; \text{CKL Thm 4.6 (trivially, by summing over } w\text{)}$$

Converse open. The gap = "what the W-indexing remembers that the n-indexing forgets" = which Kostant-partition-decomposition is contributing where.

This is the **first instance** I've seen of a positive polynomial admitting two different proofs at two different index resolutions, with one proof refining the other. **Look for more.** Whenever a positive polynomial is proven via a collapsed-index involution, check the W-indexed lift. The lift may be provable by a structurally analogous involution.

## Concrete next moves

1. **Read AL Prop 5.3 carefully with this lens.** Verify that the SES merge is the same operation as Aug~'s long-long swap up to convention. Look for the bigraded-preservation criterion at the AL side — that's the AL analog of (SA)'s applicability lemma.

2. **Test the bridge conjecture on cyclotomic Hecke.** Bowman–Norton–Simental (JIMJ 2024) build BGG resolutions inside cyclotomic Hecke. Check: do their differentials look like Aug~-style swaps? Do they admit bidegree-preserving sub-types? If yes, the bridge has prior incarnation in cyclotomic Hecke land.

3. **Build the swap-complex framework formally.** The objects: pairs (root-lattice element $\beta$, family of decompositions $\mathcal D$, internal bigrading on each decomposition, swap-differential between decompositions). Specializations: Almousa–Lu (compositions, gluing) and Aug~ (Kostant partitions, root swaps). Look for other specializations.

4. **Test on type D.** Type-D BGG–Verma has its own short/long structure; the half-spin lattice is different. Aug~ should adapt with type-D-specific swap moves. Concrete: adapt `aug_tilde_B2.py` to D_3.

   **Refined prediction (2026-05-12, from the (B)/(B′) lesson at B_3), CORRECTED.** The (B′) refinement says: π′ − π is a sum of $s_i$-orbit swaps within ONE simple reflection, possibly splitting $|c_i|$ across multiple sub-orbits. The "mixed pair" phenomenon (2.44 % in B_3) arises when $|c_i|$ exceeds a single donor's multiplicity in π — NOT directly tied to double-lacing. (My first try at this entry claimed simply-laced ⟹ zero mixed pairs; that's wrong: D_4's $s_1$ has 4 orbits on positive roots {e_1±e_3, e_2±e_3}-style, so mixed pairs are *possible* in simply-laced types too.) **Refined prediction:** mixed-pair frequency in D_4 should be a function of $|c_i|$-distribution × orbit-size-distribution; could be comparable to B_3 or different by combinatorial factors. The doubly-laced feature that *is* special: $s_i$ for a *short* simple root (only in B/C/F/G) maps long-long pairs orthogonally instead of short-short — fewer orbits than long-root reflections (B_3's $s_3$ has 2 orbits vs $s_1, s_2$'s 3). So short-root reflections have **fewer** mixed-pair opportunities, not more. Net: D_4 will likely have *some* mixed pairs but their structure should be uniform per s_i (no short/long asymmetry). Test on D_4. The AL parallel is also more nuanced than I first wrote: AL compositions DO admit a "multi-block donor" analog when the boundary at position $i$ involves multiple sub-blocks that can be redistributed. The right test is whether AL's gluing has a phenomenon analogous to Aug~'s mixed pairs at high rank.

5. **Bigraded Morris recurrence as the inductive proof of (SA).** If the Aug~ + priority structure is really a W-indexed lift of CKL's Morris-strip involution, the inductive structure should be the same. Refine CKL eq. 4.13 to coefficient level.

## How this interacts with existing connections

* **`acyclicity-is-positivity.md`:** the parent. Today's connection fills in the *mechanism* of the dichotomy: not just "acyclic vs not," but "swaps preserve bidegree vs don't." The parent moves from structural-claim to structural-mechanism.

* **`derived-krob-thibon.md`:** AL is the acyclic endpoint. Today: AL's gluing differential is the acyclic limit of the swap operation. The Krob–Thibon iso at K_0 is the q=0 shadow of "all swaps bidegree-preserving."

* **`r-matrix-as-LR-symmetry.md`:** the R-matrix at q=0 becomes idempotent (= a projection in NSym ⊗ NSym → NSym). Today's swap operation is structurally the same kind of "merge two pieces into one piece" at the level of decompositions. R-matrix is the K_0 shadow of the AL gluing; both are q=0 limits of the same swap-complex differential.

* **`crystal-skeleton-as-qsym-crystal.md`:** the QSym-side crystal is the K_0^{fd}-level shadow of the AL acyclic side. Whether a "crystal of the BGG-Verma swap complex" exists is OPEN — that would be a finite combinatorial object whose statistics match (q,t)-Lusztig polynomial bidegrees. Today's framework gives a precise question: is there a crystal-graph-style structure on (W, Kostant partition) pairs with edges = Aug~ moves?

* **`q-zero-categorification-is-frobenius.md`:** the K_0 thesis (parabolic Frobenius reciprocity) is the q=0 shadow of the swap-complex framework. Frobenius reciprocity = "the swap structure is bidegree-preserving" at the level of inductions and restrictions.

## Status

The connection is structural. The **specializations are both rigorous**: AL Theorem 5.6 is published; Aug~ for B_2 is proved (2026-05-07). The **bridge framework itself is conjectural**: no candidate object has been written down whose differentials specialize to both AL gluings and Aug~ swaps.

**Falsifier:** if the AL gluing differential and the Aug~ swap differential have *incompatible* sub-quotient structures (e.g., AL is a quotient and Aug~ is a sub-object, or the bigrading conventions can't be reconciled), the bridge is wrong and the parallel is just a parallel. Worth checking carefully when reading AL §5.

**Confirmer:** finding any third instance — a third family of decompositions of root-lattice elements with a bidegree-preserving swap operation giving a sign-reversing involution — would strongly suggest the framework exists. The third instance would *force* the abstract formulation. Plausible candidates: KR-crystal energy on rigged configurations; canonical-basis transition matrices; horizontal-strip enumerations in CKL.

The (SA) ⟹ CKL implication is the first cross-instance evidence for the swap-complex framework, since (SA) and CKL Thm 4.6 are the same dichotomy at two different index resolutions.
