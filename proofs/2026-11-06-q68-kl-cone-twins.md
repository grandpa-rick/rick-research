# Q68 — dominated twins and the KL cone beyond type A (PROVE 279, 2026-11-06)

Scripts: `proofs/wake279/` (coxkl.py, twin_criterion.py, survivors.py, interior.py, syt_interior.py,
dominance_star.py, a13_caseB.py, a13_caseB2.py, thmB_check.py, bn_both.py, bn_irr_twins.py).

## Setting and conventions

W is a finite Coxeter group with simple reflections S. L(w) = {s ∈ S : sw < w} is the left descent set.
μ(x,y) = μ(y,x) is the KL μ-function, and μ ≥ 0 (Elias–Williamson 2014 in general; KL for Weyl groups).
Γ is a left cell. M_Γ is the cell module at v=1 with basis {e_x : x ∈ Γ}, in the Goertzen–Williamson W-graph
convention (arXiv 2604.18894, Ex. 4.7):

    (1+s) e_x = 0                                   if s ∈ L(x),
    (1+s) e_x = 2 e_x + Σ_{y∈Γ, s∈L(y)} μ(x,y) e_y   if s ∉ L(x).

C_KL = cone{e_x}. "Maximal" means maximal among pointed {1+s}-invariant cones.

Standard facts used:

- **(F1)** (KL79 (2.3.e)). Let y < w, s ∈ L(w) and s ∉ L(y). If μ(y,w) ≠ 0, then y = sw.
  Proof: sw < w gives P_{y,w} = P_{sy,w}. If sy ≠ w, then sy < w, and
  deg P_{sy,w} ≤ (l(w) − l(y) − 2)/2 < (l(w) − l(y) − 1)/2, so μ(y,w) = 0.
- **(F2)** If μ(y,w) ≠ 0 and s ∈ L(y) \ L(w), then y ≤_L w. This is because C_y occurs in C_s C_w; by (F1) either y = sw or y < w.
  In particular, if both L(y) ⊄ L(w) and L(w) ⊄ L(y) hold and μ ≠ 0, then y ~_L w.
- **(F3)** Subword property: if u ≤ w ∈ W_J, then u ∈ W_J, so L(u) ⊆ J.

## (a) Dominated-twin lemma — PROVED

**Lemma A.** Let x ≠ z ∈ Γ with L(z) ⊆ L(x), and suppose μ(y,z) ≥ μ(y,x) for every y ∈ Γ with L(y) ⊄ L(x).
Put v = e_z − e_x. Then K = cone({e_w : w ≠ z} ∪ {v}) is simplicial, {1+s}-invariant, and strictly contains C_KL.
Hence C_KL is not maximal.

*Proof.* The set {e_w (w ≠ z), v} is a basis, so K is simplicial and hence pointed.
Since e_z = v + e_x, we have C_KL ⊆ K. Also v ∉ C_KL, because its e_x-coefficient is −1, so the containment is strict.
For w ≠ z, (1+s)e_w ∈ C_KL ⊆ K. Now check (1+s)v case by case.

1. s ∈ L(z). Then s ∈ L(x), so both terms are killed and (1+s)v = 0.
2. s ∈ L(x) \ L(z). Then (1+s)v = (1+s)e_z ∈ C_KL.
3. s ∉ L(x). Then s ∉ L(z) as well, and (1+s)v = 2v + Σ_{y∈Γ, s∈L(y)} (μ(z,y) − μ(x,y)) e_y.
   Every such y has s ∈ L(y) \ L(x), so L(y) ⊄ L(x) and the coefficient is ≥ 0.
   Also y ∉ {x, z}, because s lies in neither L(x) nor L(z). So (1+s)v ∈ K. ∎

## (b) Every m ≥ 4 bond produces a twin — PROVED (irreducibility only computed)

**Theorem B.** Let W be a finite Coxeter group, and let s, t ∈ S with m(s,t) ≥ 4. Put J = S \ {t}, x = w_J, z = stw_J.
Then x and z lie in one left cell Γ, and (x, z) is a dominated twin.
So C_KL(Γ) is not a maximal invariant cone.

*Proof.*

1. *Shape of x.* Write x = a·u with a ∈ ⟨s,t⟩, u minimal in ⟨s,t⟩u, and lengths adding.
   Every reduced word of x uses only letters from J, and t ∉ J, so a ∈ {e, s}. Since s ∈ J = L(x), we get a = s and x = su.
2. *z is reduced, with L(z) ⊆ J.* tx = tsu and z = stsu have lengths l(u)+2 and l(u)+3, because sts is reduced in a
   dihedral group of order 2m ≥ 8. In I_2(m) with m ≥ 4, L(sts) = {s}, so t ∉ L(z). Since J = S \ {t}, this gives L(z) ⊆ J = L(x). Also z ≠ x.
3. *Same left cell.* μ(x,tx) = μ(tx,z) = 1, because each pair is related by one left multiplication.
   t ∈ L(tx) \ L(x) and s ∈ L(x) \ L(tx), so (F2) gives x ~_L tx.
   s ∈ L(z) \ L(tx) and t ∈ L(tx) \ L(z), so tx ~_L z.
4. *Twin condition.* Let y ∈ Γ with L(y) ⊄ J and μ(y,x) ≠ 0. Then t ∈ L(y).
   If y < x, then (F3) gives L(y) ⊆ J, which is impossible.
   So y > x, and t ∈ L(y) \ L(x). By (F1), with x below y, we get x = ty, i.e. y = tx.
   So tx is the only y that needs checking, and μ(tx,z) = 1 ≥ 1 = μ(tx,x).
   For every other y, μ(y,x) = 0 ≤ μ(y,z). Lemma A then applies. ∎

Notes.
- The B_3 witness from Wake 279 is this theorem with (s,t) = (s1,s2) in the code labelling, where s1–s2 is the 4-bond.
  There x = s3s1 = w_{13} and z = s1s2s3s1.
- The dihedral middle cells are the case J = {s}.
- Computer check (`thmB_check.py`): I2(4,5,6), B3, H3, B4 and F4, for every ordered m≥4 pair, gave a twin each time.
  The only y with μ(y,w_J) ≠ 0 and L(y) ⊄ J was tw_J each time, as the proof predicts.

**Irreducibility (asked in (b)) — computed, not proved.**

| | cell of w_{S∖{s2}} (J = A1×A_{n−2}) | cell of w_{S∖{s1}} (J = A_{n−1}) |
|---|---|---|
| B3 | dim 3, irreducible | dim 3, irreducible |
| B4 | dim 6, irreducible | dim 10, commutant 2 |
| B5 | dim 30, commutant 2 | dim 10, irreducible |

H3, cell of w_{S∖{s2}}: dim 5, irreducible. So for n = 3, 4, 5 an irreducible left cell with a twin exists (computed).
Census of irreducible cells with a twin (`bn_irr_twins.py`, `irr_twin.py`):
- B4: 6 cells of dim 6 and 8 cells of dim 8.
- B5: 10 cells of dim 10 and 15 cells of dim 15.
- F4 (stretch): 32 irreducible 8-dim cells, every one of which has a twin.
In most of these B_n cells the twin has the form z = s1 s2 x, with x of type {s1} at the bottom of its ⟨s1,s2⟩-string. The exceptions are some B4 8-dim cells, e.g. (z,x) = (43212341231, 432123431).
Dim C(n,2) shows up for n = 3, 4, 5 (3, 6, 10), but it comes from the cell of w_{134} in B4 and from the cell of
w_{2345} in B5.
A *uniform* irreducible family for all n is still a GAP (see Gaps).
Irreducibility only matters for uniqueness of C^max. Theorem B gives non-maximality of C_KL in every cell of the form
Γ(w_{S∖{t}}), reducible or not.

## (c) Simply-laced: partial result plus an obstruction to the natural route

**Proposition C1 (star kill).** Let W be arbitrary, (x,z) a dominated twin in Γ, s ∈ L(x), t ∉ L(x), m(s,t) = 3.
Then s ∉ L(z).

*Proof.* Use KL star operations for the pair {s,t}. Let D_L(s,t) = {w : |L(w) ∩ {s,t}| = 1}.
Write w = au with a ∈ ⟨s,t⟩ ≅ S_3 and u minimal. The elements of type {s} (that is, L ∩ {s,t} = {s}) are su and stu.
The elements of type {t} are tu and tsu.
For type-{s} w, exactly one of sw, tw has type {t}; call it *w. Here *(su) = tsu and *(stu) = tu.
The map * is an involution of D_L(s,t), and μ(w,*w) = 1.

*Claim:* if y has type {t}, z has type {s}, and μ(y,z) ≠ 0, then z = *y.
- If y < z, apply (F1) with s ∈ L(z) \ L(y): y = sz.
- If z < y, apply (F1) with t ∈ L(y) \ L(z): z = ty.
So z ∈ {sy, ty}, and z has type {s}. Hence z = *y.

Now set x' = *x. By (F2), x' ∈ Γ. Since t ∈ L(x') \ L(x), the twin hypothesis gives μ(x',z) ≥ μ(x',x) = 1.
We have t ∉ L(z), because L(z) ⊆ L(x). If also s ∈ L(z), then z has type {s} and x' has type {t}.
The claim gives z = *x' = x, a contradiction. ∎

*Attribution remark (Wake 280, Stembridge gate closed).* The pairing step of the Claim (for m(s,t) = 3, a type-{t}
element and a type-{s} element joined by an edge are star partners, with μ = 1) is Stembridge's: Bonding Rule,
Prop. 4.4 (p = 3 clause), pp. 358–359, together with the Simplicity Rule, Prop. 4.2, p. 357 (incomparable τ-sets
give a simple edge of weight 1); see Remark 4.3, p. 357, for the simply-laced case. Thm. 3.4, p. 355 (rank-2 admissible
cells have no multiplicities > 1) is the underlying reason. [Stembridge, *Admissible W-graphs*, Represent. Theory 12
(2008) 346–368.] The statement that exactly one of sy, ty has type {s} is classical KL 1979 §4 star-operation theory.
Stembridge has no twin, dominated-pair or cone result. Applying this to dominated twins (C1–C3, Thm B, Lemma A) is ours.
Context: on p. 365 Stembridge shows the B3 cell {1}—{2}—{1,3} on the m = 4 bond, noting {1} ⊂ {1,3}. He uses it only for a
Polygon Rule argument, but it is the same configuration as our B3 dominated twin.

**Corollary C2.** Let W be simply laced, and let int L(x) = {r ∈ L(x) : every neighbour of r lies in L(x)}.
If (x,z) is a dominated twin, then ∅ ≠ L(z) ⊆ int L(x).
(L(z) ≠ ∅ because |Γ| ≥ 2 rules out z = e.)
So twins are excluded in every cell satisfying

> (★)  there are no x ≠ z ∈ Γ with ∅ ≠ L(z) ⊆ int L(x).

**Theorem C3 (type A, n ≤ 13).** For S_n with n ≤ 13, (★) holds for every left cell. So no left cell of S_n (n ≤ 13)
contains a dominated twin.

*Proof.* In S_n we have L(w) = Des(P(w)), and Γ = {Q fixed}. So the descent sets occurring in a cell of shape λ are
exactly {Des(T) : T ∈ SYT(λ)}. Standardisation gives #{T : Des(T) ⊆ B} = K_{λ, comp(B)}. Transposition gives
#{T : Des(T) ⊇ A} = K_{λ′, comp(Aᶜ)}. Since int is monotone, (★) fails for some cell iff there are A ⊆ [n−1]
and λ with K_{λ′,comp(Aᶜ)} > 0 and K_{λ,comp(int A)} > 0.
The cases A = ∅ and A = [n−1] are excluded: for the first, L(z) = ∅; for the second, λ = (1ⁿ) has one tableau.
For A ≠ ∅, [n−1], int A ⊊ A, so z ≠ x automatically.
By K_{μ,ν} > 0 ⟺ μ ⊵ sort(ν), and since conjugation reverses ⊵, such a λ exists iff β ⊴ α′.
Here α = sort comp(int A) and β = sort comp(Aᶜ). `dominance_star.py` checks all A for n ≤ 13 and finds no violation.
This is exhaustive and in exact integer arithmetic.
Cross-check: `syt_interior.py` enumerates the SYT directly for n ≤ 11 and agrees. ∎

**Computed:** (★) also holds in all left cells of D4 and D5 (`interior.py`; star-kill survivors 0).
Twin scans find 0 twins in A3–A6, D4 and D5. The controls do find twins: B4 in 24/50 cells, F4 in 44/72.

**(★) is FALSE in general: first failure at S_14.** Take λ = (4,4,3,3) and

    P  = [[1,2,6,10],[3,7,11,14],[4,8,12],[5,9,13]]   Des P  = {2,3,4,6,7,8,10,11,12}
    P' = [[1,2,3,7],[4,5,6,11],[8,9,10],[12,13,14]]    Des P' = {3,7,11} = int Des P.

λ = (5,3,3,3) gives a second instance. So the star-kill route alone cannot prove (c) for all ADE.
For this pair, a twin would need μ(*x, z) ≥ 1 for each of the six boundary pairs; these give 4 distinct x′.
Computed in all 12012 left cells of shape (4,4,3,3): each such x′ has L(x′) ⊇ L(z) = {3,7,11}, x′ < z in Bruhat order,
and l(z) > l(x′). The cheap necessary conditions from (F1) therefore pass. `a13_caseB3.py` covers every y = sx in Γ with L(y) ⊄ L(x); these are exactly the 4 star images, and (F1) parity, Bruhat order and the r-descent test pass for each of them in all 12012 (resp. 15015) cells. Deciding the case needs μ inside a
12012-dimensional cell (l(z) ≥ 46), which was out of reach this session.

**Lemma C4 (Case-B constraints, proved).** Let W be simply laced, (x,z) a twin, and (s,t) a boundary pair of x
(s ∈ L(x), t ∉ L(x), m = 3). Put x′ = *x. Then:
- either z = t x′, which forces x = stu, x′ = tu, z = u and l(z) = l(x) − 2;
- or x′ < z, and every r ∈ L(z) \ L(x′) satisfies x′ = rz.
If x has at least two boundary pairs, only the second alternative occurs for every pair, and l(z) ≥ l(x).

*Proof.* By C2, s, t ∉ L(z), and μ(x′,z) ≥ 1. If z < x′, apply (F1) with t ∈ L(x′) \ L(z): z = tx′.
If x′ = tx, this gives z = x, which is impossible; so x′ = sx and x = stu.
If x′ < z, apply (F1) for each r ∈ L(z) \ L(x′).
For two pairs, the first alternative gives z = tsx = t₂s₂x, so (s,t) = (s₂,t₂). It also fixes l(z) = l(x) − 2, while
the second alternative for the other pair needs l(z) > l(x′) ≥ l(x) − 1. ∎

## (d) H3 5_2 non-twin mechanism — not attempted.

## Gaps (precise)

1. **(c) open in general.** No twins is proved for S_n with n ≤ 13 and computed for D4, D5 and A6. The proof route
   (C1 ⇒ (★)) breaks at S_14. The concrete undecided instance is the pair (P, P′) above: is
   μ(x′_i, z) ≥ 1 for the 4 star images, together with every other y having L(y) ⊄ L(x)?
2. **(b) irreducible family for all n.** Twins in B_n are proved for all n (Theorem B). An irreducible left cell with
   a twin is computed only for n ≤ 5, and neither natural w_J family is irreducible for every n.
   Possible tools: Lusztig's description of the cell of w_J via j-induction, or the criterion
   "the sign_A-isotypic part is 1-dimensional and e_{y0} generates M_Γ ⇒ M_Γ is irreducible".
3. **Correction to the Wake 279 narrative.** "The characterisation is a simply-laced phenomenon" overstates things.
   GW Ex. 4.21 already shows maximality failing in S_9 at (4,4,1), without a twin. Q68(c) is about the twin
   mechanism only.
