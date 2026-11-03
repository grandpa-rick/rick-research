# Wake 273b — Crown R first-hand locators (2026-11-03)

All metadata fetched from export.arxiv.org API; PDFs from arxiv.org/pdf, read with pdftotext. Everything quoted below is copied verbatim from those sources.

## (A) Droschl / Lapid IDs — ALL CONFIRMED (no hallucination)

### arXiv 2508.13817 — https://arxiv.org/abs/2508.13817
- Title: "Poles of intertwining operators in terms of irreducible components of Lusztig's characteristic variety in type A"
- Authors: Johannes Droschl (sole author)
- Submitted 2025-08-19 (v1); last updated 2026-08-29
- Abstract: "In this paper, we propose a conjectural formula for the order of the poles of intertwining operators in the context of the representation theory of general linear groups over $p$-adic fields. More specifically, we conjecturally relate the order of the pole to the dimension of a Hom-space associated with irreducible components of Lusztig's characteristic variety in type $A$. We verify the conjecture in a wide range of cases."

### arXiv 2608.29312 — https://arxiv.org/abs/2608.29312
- Title: "Generalized Jantzen filtration, hyperbolic restriction, and characteristic cycles"
- Authors: Johannes Droschl (sole author)
- Submitted 2026-08-29 (v1); last updated 2026-09-10
- Abstract: "In this paper we give a geometric description of the behavior of analytic intertwining operators between parabolically induced representations of $\mathrm{GL}_n(\mathrm{F})$, where $\mathrm{F}$ is a local non-archimedean field, in terms of hyperbolic localization functors of Braden. As a consequence, we can show that the image of an intertwining operator is always semi-simple and give a lower bound on the order of its pole, which is conjectured to be an equality as well as an upper bound in terms of the singular support of certain perverse sheaves. Moreover, we are able to reduce the conjecture of Lapid and Mínguez on the shape of irreducible subrepresentations of induced representations to a computation of characteristic cycles. The theory of mixed Hodge modules plays a crucial role in the proofs."

### arXiv 2608.14413 — https://arxiv.org/abs/2608.14413
- Title: "A greedy open-orbit criterion for solvable algebraic group actions, with applications to Lusztig's nilpotent varieties"
- Authors: Erez Lapid (sole author)
- Submitted 2026-08-14 (v1, no later versions)
- Abstract: "Let $G$ be a connected solvable algebraic group acting rationally on a finite-dimensional vector space $U$. Using a $G$-stable complete flag, we formulate a successive-quotient procedure that decides whether $U$ contains an open $G$-orbit. When the procedure succeeds, it constructs an open-orbit vector of minimum support cardinality and determines the image of a generic stabilizer in the maximal torus quotient. We also give an infinitesimal version detecting open separable orbits. We apply the criterion to the action of $Aut_Q(M)$ on $Ext^1_Q(M,M)^*$ where $M$ is a multiplicity-free representation of a Dynkin quiver. Rigidity of the corresponding component of Lusztig's nilpotent variety is thereby reduced to a rank test together with an acyclicity condition on a graph of active extension coordinates; the connected components of the resulting forest determine the generic indecomposable decomposition. For equioriented type $A$ this yields an explicit algorithm for a family of multisegments encoded by incidence matrices, including nonregular examples with repeated beginnings or ends."

## (B) Smallest type-A case: dual canonical vs dual semicanonical

### ID CORRECTION: Leclerc is arXiv **math/0202148**, NOT math/0202058
https://arxiv.org/abs/math/0202148 (v2). Title "Imaginary vectors in the dual canonical basis of $U_q(n)$", sole author Bernard Leclerc, submitted 2002-02-15.
Abstract: "Let $n$ be the maximal nilpotent subalgebra of a simple complex Lie algebra $g$. We introduce the notion of imaginary vector in the dual canonical basis of $U_q(n)$, and we give examples of such vectors for types $A_n (n\ge 5)$, $B_n (n\ge 3)$, $C_n (n\ge 3)$, $D_n (n\ge 4)$, and all exceptional types. This disproves a conjecture of Berenstein and Zelevinsky about $q$-commuting products of vectors of the dual canonical basis. It also shows the existence of finite-dimensional irreducible representations of quantum affine algebras whose tensor square is not irreducible."

Def 1 (p.1): "We say that b ∈ B∗ is real if b2 ∈ q^Z B∗ . Otherwise, we say that b is imaginary."
Intro p.1: types A_n (n<=4) and B2: "From these descriptions one sees that all vectors of B∗ are real if g is of type An (n ⩽ 4) or B2."

§2.7 (pp.5–6), type A5, reduced word w0 = s1 s2 s3 s4 s5 s1 s2 s3 s4 s1 s2 s3 s1 s2 s1 (PBW/Lusztig coordinates):
  "b = b(0,1,0,0,0,0,0,1,0,1,0,0,0,1,0),
   z = b(0,1,0,1,0,0,1,0,1,0,1,0,0,1,0).
   We have b2 = q−2 (b[2] + z), hence b is imaginary."
I computed the weight from the stated root ordering:
  wt(b) = (α1+α2)+(α2+α3+α4)+α3+(α4+α5) = α1+2α2+2α3+2α4+α5 (degree 8)
  wt(z) = wt(b^2) = 2α1+4α2+4α3+4α4+2α5 (degree 16)
§4.2 (p.8): "Consider the example of 2.7 for type A5 . The vector b has principal degree 8." Multisegment [1,2],[2,3,4],[3],[4,5], with dim 252 (H_8 module). M⊙M has 2 composition factors.
Remark 1 (p.6): "In [KS], Kashiwara and Saito prove that t is a counterexample to a problem of Lusztig [L2] ... SS(Lt) = Λt ∪ Λc", where (c, b[2]) = (t, z) = 1.
Leclerc himself does NOT mention the semicanonical basis.

### Where "dual canonical ≠ dual semicanonical" is actually stated: GLS math/0402448
https://arxiv.org/abs/math/0402448 (v2), "Semicanonical bases and preprojective algebras", Geiss–Leclerc–Schröer, 2004-02-27.
(Note: math/0404554 is an unrelated G2-structures paper. Don't use it.)
- Thm 1.2 (p.4): "The bases S∗ and B∗ coincide if and only if g is of type An with n ≤ 4."
- §1.2 eq (1) (p.3): "In particular in type A5 , for a certain V of dimension 8 one can find an irreducible component Z of ΛV such that (1) (b∗Z)2 = q−2 (b∗Z′ + b∗Z′′) where Z′ = Z ⊕ Z and Z′′ are two irreducible components of ΛV⊕V ... This seems to be the smallest counterexample to the BZ-conjecture in type A."
- §1.5 eq (2) (p.4): "For example in type A5 , we deduce from Equation (1) and Theorem 1.1 that (2) ρZ′ = b∗Z′ + b∗Z′′"
- §1.5 eq (3): "(3) bO′′ = fΛO′ + fΛO′′ , and this is probably the smallest example in type A for which the canonical and semicanonical bases differ."
- §1.3 (p.3): KS "exhibited two orbits O′, O′′ for type A5 such that SS(LO′′) = ΛO′ ∪ ΛO′′. The corresponding vectors bO′ and bO′′ of Bq have principal degree 16, and apparently this is the smallest counterexample in type A." "...this counterexample is dual to the counterexample above for Bq∗ , in the sense that ΛO′ = Z′ and ΛO′′ = Z′′ , see [31, Remark 1]."
- Thm 7.6 proof (p.15): "it was shown in [31] that for the cases A5 and D4 there exist elements of B∗ whose square is not in B∗ . They are called imaginary vectors of B∗ . This shows that B∗ and S∗ are different in these cases." (In tame A5/D4 the square of any S∗ vector is again in S∗.)
=> The difference B∗ ≠ S∗ shows up at weight 2α1+4α2+4α3+4α4+2α5 (dim V⊕V = 16), the weight of b^2. The imaginary vector b sits at weight α1+2α2+2α3+2α4+α5 (dim 8). "Smallest" is hedged ("seems", "probably", "apparently") and is NOT a theorem.

## Kashiwara–Saito q-alg/9606009 — https://arxiv.org/abs/q-alg/9606009
"Geometric Construction of Crystal Bases", Masaki Kashiwara, Yoshihisa Saito, 1996-06-08.
Abstract: "We realize the crystal associated to the quantized enveloping algebras with a symmetric generalized Cartan matrix as a set of Lagrangian subvarieties of the cotangent bundle of the quiver variety. As a by-product, we give a counterexample to the conjecture of Kazhdan--Lusztig on the irreducibility of the characteristic variety of the intersection cohomology sheaves associated with the Schubert cells of type A and also to the similar problem asked by Lusztig on the characteristic variety of the perverse sheaves corresponding to canonical bases."
(The abstract gives no type or degree. The PDF does.)
§7.2 (p.18): "we shall present a counterexample of Problem 1 when the underlying graph is of type A5 ... Let ν = −2α1 − 4α2 − 4α3 − 4α4 − 2α5 . Set b = f̃2 f̃1 f̃3 f̃2 f̃4^2 f̃3^2 f̃2 f̃1 f̃5^2 f̃4^2 f̃3 f̃2 u∞ and b′ = f̃2^2 f̃1^2 f̃3^2 f̃4^2 f̃3^2 f̃2^2 f̃5^2 f̃4^2 u∞" (orientation 1←2←3←4←5).
Theorem 7.2.1 (p.19): "SS(π COb,Ω ) ⊃ Λb ∪ Λb′ ." Remark 1: "In fact, although we don't give a proof ..., they coincide."
§8.3: Prop 8.3.1 "Conjecture 2 is true for 1 ≤ n ≤ 7" (computer check; this is KL irreducibility for Schubert cells in SL_n). Example 8.3.1: a counterexample at n = 8 (Schubert varieties of SL(8)), derived from Thm 7.2.1.
