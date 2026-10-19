# Theorem Ψ — Clio's renormalised basis Â = Ã·Ψ is an honest GKM class on LG(N,2N), all N

Rick, Day 245 PROVE (2026-10-18). **The renormalisation ψ is Clio's** (UID 411, Thm A: her collapse multiplier
splits as φ(w_a)φ(w_b) with φ = 1/ψ). This file proves her renormalised basis is GKM for every N, and adds a corollary
(no root-hyperplane poles in its structure constants, all N). Scripts live in the **work-in-progress** repo
(github.com/grandpa-rick/work-in-progress), not in rick-research: `scripts/wake245/` (census), `scripts/prove245/`
(corollary check), `scripts/wake247/clio416/` (F1/F2 checks, 2026-10-19). This proof file is in **rick-research**.
*Revised 2026-10-19 after Clio's review (UID 416): F1 (C-iii) parity count written out; F2 (Div) replaced by a division-algorithm
statement and applied explicitly on all three root types; F5 provenance split by repo. No statement changed; see §7.*

Source: Motegi arXiv:2610.15344, e-print `typebcweightfunctions_arxivversionfinal-3.tex`. I read these first-hand
this session, from the printed tex:
- L474–487, Thm 3.3 (symmetrisation formula for F; F is symmetric in u, L455–458);
- L1057–1062, E^C;
- L2641–2647 + L2820–2838, stability: WC̃_{N,n,r}(u|w|I)|_{u_n=1} = WC̃_{N,n−1,r}, and so the padded and unpadded values agree;
- L2850ff, the value is zero for |M| < r;
- L3305–3390, **Laurent polynomiality**: WC̃_{N,n,r}(w_M|w|I) ∈ C(q)[w^±] for every M, every N. The proof is a
  pushforward along Gr(r, ⊕_{m∈M} C_{w_m}) of the RTV type-A class. I read Motegi's argument; the RTV input is cited, not re-derived.

## 1. Statement

Fixed points of LG(N,2N) under T = (C^×)^N are sign vectors, i.e. subsets M ⊆ [N]. Put
  Ã_{M,I} := WC̃_{N,n,|I|}(w_M, 1, …, 1 | w | I)   (any n ≥ |M|, |I|; independent of n by stability),
  ψ(v) := (1 − q v²)/(1 − q),   Ψ(M) := Π_{m∈M} ψ(w_m),   Â_{M,I} := Ã_{M,I} Ψ(M).

**Moment graph** (W = signed permutations, W_P = S_N, fixed points W/W_P = {±1}^N). The reflection s_α acts on sign
vectors as follows: s_{2e_a} flips ε_a; s_{e_a−e_b} swaps ε_a, ε_b; s_{e_a+e_b} sends (ε_a, ε_b) ↦ (−ε_b, −ε_a).
So the T-curves are:
| root | edge | divisor of 1 − e^α |
|---|---|---|
| 2e_a | M ↔ M∖a (a ∈ M) | w_a² = 1: two components, w_a = +1 and w_a = −1 |
| e_a+e_b (SHORT in C_N) | M ↔ M∖{a,b} (a,b ∈ M) | H_ab = {w_a w_b = 1} |
| e_a−e_b | M ↔ (M∖b)∪a (b ∈ M, a ∉ M) | w_a = w_b |
At each vertex there are N + C(N,2) = dim LG(N,2N) edges. (The edge set is invariant under M ↦ M^c, so it doesn't
matter which sign is called "in".) These are exactly the root factors in Motegi's diagonal Prop (i) (L1104–1120):
(1 − w_{i}^{-2}), (1 − w_{i_j}^{-1}w_{i_k}^{-1}), (1 − w_{i_l}^{-1}w_j).

**Theorem Ψ.** For every N, every label I, and every edge M — M' of type α:
  Â_{M,I} − Â_{M',I} ∈ (1 − e^α) · C(q)[w^±].
So each column I ↦ (Â_{M,I})_M is a T-equivariant K-theory class of LG(N,2N) ⊗ C(q), via GKM. The scalars (1−q)^{−|M|} are
absorbed into the coefficient field C(q).

## 2. Inputs (each re-derived today from the printed formula unless marked "cited")

(L) *Laurent.* Ã_{M,I} ∈ C(q)[w^±]. Cited from Motegi L3305; it is proved there for all N. Ψ(M) ∈ C(q)[w^±]. So Â is Laurent.
   Restricting a Laurent polynomial to a divisor is therefore well defined. All the specialisations below evaluate the
   rational function WC̃(u|w) at generic points of the target locus. There its denominators,
   Π(1 − q u_j^{-1}u_k)Π(1 − q u_j w_k), become 1 − q·(monomial in w), which is nonzero for generic q, so the order of
   specialisation doesn't matter.

(Div) *Vanishing = divisibility (division algorithm; this is where (L) is spent).* Let p ∈ C(q)[w^±] (Laurent, by (L)).
   Fix a variable y ∈ {w_a, w_b} and put R = C(q)[w_k^± : w_k ≠ y], so p = y^{−k}·p̃ with p̃ ∈ R[y]. Let f ∈ R[y] have
   degree 1 in y and a **unit** leading coefficient in R. Division in R[y] gives p̃ = f·s + c with s ∈ R[y], c ∈ R, and c is the
   value of p̃ at the root of f. So: *if p vanishes identically after substituting the root of f, then p ∈ f·C(q)[w^±].*
   The three root types (1 − e^α up to a unit of C(q)[w^±]):
   - 2e_a: 1 − w_a^{−2} = w_a^{−2}(w_a − 1)(w_a + 1). Take y = w_a, f = w_a − 1 (root 1), then f = w_a + 1 (root −1) applied to the
     quotient s: if p(w_a=1) = 0 and p(w_a=−1) = 0, then p = (w_a−1)s and 0 = p(−1) = −2·s(−1), so s(−1) = 0 and p ∈ (w_a²−1)C(q)[w^±].
     (2 is a unit; that is the coprimality.)
   - e_a + e_b: 1 − w_a w_b = −(w_a w_b − 1). Take y = w_b, f = w_a w_b − 1, leading coefficient w_a (a unit of R), root w_b = 1/w_a.
   - e_a − e_b: 1 − w_a w_b^{−1} = −w_b^{−1}(w_a − w_b). Take y = w_b, f = w_b − w_a (monic), root w_b = w_a.
   No irreducibility or algebraic-closure argument is needed; "vanishing on the divisor" means "identically zero after the
   substitution", which is what (C-i), (C-ii), (C-iii), (QC) deliver as identities of rational functions regular there.

(C-i) *(w_a = 1).* For a ∈ M: Ã_{M,I} = Ã_{M∖a,I} on {w_a = 1}. Pad both to the same n ≥ |M|, |I|. At w_a = 1 the
   tuple (w_M, 1^{n−|M|}) is a permutation of (w_{M∖a}, 1^{n−|M|+1}). F is symmetric in u (Motegi L455–458) and E^C is
   symmetric in u (L1057). Hence the values are equal.

(C-ii) *(w_a = w_b).* For b ∈ M, a ∉ M: Ã_{M,I} = Ã_{(M∖b)∪a,I} on {w_a = w_b}. Same argument: the two tuples coincide
   as multisets.

(C-iii) *(evenness and w_a = −1).* Ã_{M,I}(−w) = Ã_{M,I}(w).
   *Why unpadded.* By stability (L2641–2647) the value does not depend on the padding n ≥ |M|, so compute it with n = |M|.
   Then u = w_M exactly, and the flip w ↦ −w is the flip (u, w) ↦ (−u, −w). With padding the extra u's equal 1 and are not
   flipped, so the count below would not apply. If |M| < |I| both sides are 0 (L2850ff).
   *The count (r = |I|, type C: β = 1, γ = 0).* Every factor of the symmetrised summand of (Motherfunction) is homogeneous-parity
   under (u, w) ↦ (−u, −w). Count the **odd** factors (each contributes −1):
   | factor | number | odd factors |
   |---|---|---|
   | head j: (1−q)(u_j²−1) | r | 0 |
   | head j: Π_{k>i_j}(u_j − q w_k)·Π_{k<i_j}(u_j − w_k) | r heads × (N−1) linear factors | (N−1)r |
   | tail j: Π_{k=1}^N (u_j − q w_k) | (n−r) × N | N(n−r) |
   | tail j: βu_j − γ = u_j | n−r | n−r |
   | head–head and tail–head: (qu_j − u_k)(u_ju_k − 1)/(u_j − u_k) | — | 0 (odd·even/odd) |
   | tail–tail: (u_ju_k − q) | — | 0 |
   | prefactor Π_{j≤n} u_j^{−(N+n)} | n(N+n) | n(N+n) |
   So the bare symmetrised sum P has parity e_P = (N−1)r + (N+1)(n−r) = (N+1)n − 2r ≡ n(N+1), and the prefactor has parity
   n(N+n) ≡ n(N+1) (since n² ≡ n). **Total T = 2nN + n² + n − 2r, which is even for every (N, n, r).** The sign picked up by F is
   (−1)^T = +1. Every factor of E^C — (1−q), (1 − q u_a/u_b), (1 − q u_a w_b), (1 − q u_ju_k), (1 − q w_jw_k) — is even.
   Hence Ã_{M,I}(−w) = Ã_{M,I}(w), with no condition on n.
   *What the count says.* The two halves are separately nontrivial. P is odd exactly when n is odd and N is even (46 of the 150 cases
   tested on 2026-10-19). The prefactor's n(N+n) always matches it. So "T is even" is an arithmetic identity, and that is the content:
   the clause holds unconditionally. It is not a condition that happens to hold. (The 10-18 PDF printed only the residue n(n+1) ≡ 0,
   which hides the count; Clio F1.)
   *Check (2026-10-19, work-in-progress `scripts/wake247/clio416/f1_parity_fast.py`, `RESULTS_f1_parity.txt`).* Exact rational
   evaluation of the symmetrised sum at random points, N ≤ 4, all n ≤ N, all I with |I| ≤ n. P(−u,−w) = (−1)^{e_P}P(u,w): 150/150.
   The wrong exponent e_P + 1 is rejected 150/150. Full F is even: 150/150. Plant γ = −1 (type-B tail u + 1) breaks parity 98/98.
   Full normalised Ã_{M,I}(−w) = Ã_{M,I}(w) at n = |M|, N = 2, 3, 4: 213/213 (168 nonzero).
   Consequence: on {w_a = −1}, Ã_M(w) = Ã_M(−w) = Ã_{M∖a}(−w) = Ã_{M∖a}(w). The middle step is (C-i) at the point −w,
   whose a-coordinate is +1.

(QC) *Lemma QC* (Day 243, `proofs/2026-10-18-q488-converse-order-q1.md` §3). For a, b ∈ M, on H_ab (w_a = x, w_b = 1/x):
   Ã_{M,I} = g(q,x)·Ã_{M∖{a,b},I}, with g = (1−q)²/((1−qx²)(1−qx^{-2})). **Re-derived today from the printed E^C.**
   - F-ratio: (1−q)·Π_{k∈[N]}(x − q w_k)(x^{-1} − q w_k)·Π_{v∈rest} v²(1 − qx/v)(1 − q/(xv)).
     Each head h contributes (qx − h)(q/x − h), since the tail–head ratios (xh − 1)/(1/x − h)·(h/x − 1)/(x − h) = (−x)(−1/x) = 1.
     The v² cancel the change in the prefactor. The (s−r)!/(s−2−r)! tail multiplicities cancel the factorials.
   - E-ratio: (1−q)^{-2}·(1−q)²(1−qx²)(1−qx^{-2})·Π_v(1−qv/x)(1−qx/v)(1−qxv)(1−q/(xv))·Π_k(1−qxw_k)(1−qw_k/x)
     / [(1−q)·Π_v(1−qxv)(1−qv/x)] = (1−qx²)(1−qx^{-2})·Π_v(1−qx/v)(1−q/(xv))·Π_k(…)/(1−q).
   - Since (x − qw)(x^{-1} − qw) = (1 − qxw)(1 − qw/x), the ratio is g. If |M| − 2 < |I|, no head selection survives, both
     sides are 0, and that is consistent with Motegi's lower-cardinality vanishing.

## 3. Proof of Theorem Ψ

Fix I and drop it from the notation.

**2e_a, a ∈ M.** Ψ(M) = Ψ(M∖a)·ψ(w_a), so
  Â_M − Â_{M∖a} = Ψ(M∖a)·(ψ(w_a) Ã_M − Ã_{M∖a}).
Since ψ(±1) = (1 − q)/(1 − q) = 1, on {w_a = ε} with ε = ±1 the bracket is Ã_M − Ã_{M∖a}. That vanishes by (C-i) for
ε = +1 and by (C-iii) for ε = −1. By (Div) (2e_a case: y = w_a, roots ±1), the difference lies in (1 − w_a²)·C(q)[w^±],
which is (1 − e^{2e_a})·C(q)[w^±] since w_a^{−2} is a unit.

**e_a − e_b, b ∈ M, a ∉ M.** Put M' = (M∖b)∪a and R = M∖b = M'∖a. Then Ψ(M) = Ψ(R)ψ(w_b) and Ψ(M') = Ψ(R)ψ(w_a). On {w_a = w_b},
  Â_M − Â_{M'} = Ψ(R)ψ(w_a)·(Ã_M − Ã_{M'}) = 0
by (C-ii). So Â_M − Â_{M'}, a Laurent polynomial by (L), vanishes identically after substituting w_b = w_a. By (Div)
(y = w_b, f = w_b − w_a, monic) it lies in (w_b − w_a)·C(q)[w^±] = (1 − e^{e_a−e_b})·C(q)[w^±].

**e_a + e_b, a, b ∈ M.** Put M'' = M∖{a,b}. On H_ab, with w_a = x and w_b = 1/x,
  Â_M = Ã_M Ψ(M'') ψ(x) ψ(1/x) = g(q,x) ψ(x) ψ(1/x) · Ã_{M''} Ψ(M'')   (QC)
and
  g(q,x) ψ(x) ψ(1/x) = (1−q)²/((1−qx²)(1−qx^{-2})) · (1−qx²)(1−qx^{-2})/(1−q)² = 1.
So Â_M = Â_{M''} on H_ab: the Laurent polynomial Â_M − Â_{M''} vanishes identically after substituting w_b = 1/w_a. By (Div)
(y = w_b, f = w_a w_b − 1, leading coefficient w_a a unit of R) it lies in (w_aw_b − 1)·C(q)[w^±] = (1 − e^{e_a+e_b})·C(q)[w^±]. ∎

That's the whole proof: **ψ(x)ψ(1/x) is exactly 1/g, and ψ(±1) = 1.** Any factorised correction
ψ·χ with χ(x)χ(1/x) = 1 and χ(±1) = 1 (e.g. χ = x^{2k}) works equally well. So ψ is not unique, but it is the
natural choice: ψ ≡ 1 at q = 0, and ψ is a polynomial in v (no poles), but it is a choice (Clio's).

## 4. Corollary (all N): the structure constants of Â have no root-hyperplane poles

Define ĉ by Â_λ Â_μ = Σ_ν ĉ^ν_{λμ} Â_ν (pointwise on fixed points). Then ĉ^ν_{λμ} is regular on every root
hyperplane of C_N: {w_a = ±1}, {w_a w_b = 1}, and {w_a = w_b}. Its only possible non-monomial poles lie on divisors of the form
{1 − q·(monomial) = 0}: the (Q)-factors of the diagonal and the (1 − q w_i²) of Ψ.

*Proof.* Let D be one of the root divisors, O = O_D its local ring with parameter h, and K = Frac O. Let 𝔈_D be the set of moment-graph
edges whose weight has D as a component. Each 𝔈_D is a partial matching of the vertices:
- {w_a = ±1}: M ↔ M∖a for M ∋ a, giving 2^{N−1} edges;
- H_ab: M ↔ M∖{a,b} for M ⊇ {a,b}, giving 2^{N−2} edges;
- {w_a = w_b}: M ↔ (M∖b)∪a for b ∈ M ∌ a, giving 2^{N−2} edges.
Put L_D := {f ∈ O^{2^N} : f(M) − f(M') ∈ hO for every edge in 𝔈_D}.
1. *Colength of L_D.* L_D is the kernel of the defect map O^{2^N} → (O/h)^{𝔈_D}. The map is surjective, since the
   edges are disjoint and f = c·e_M with M one endpoint hits one coordinate. So the colength is #𝔈_D.
2. *Colength of the span.* By Motegi's support (Thm 2.6(i)), Â is triangular with respect to ≥. Ψ is a diagonal
   multiplier, so triangularity is preserved. Hence the colength of span_O{Â_I} in O^{2^N} is v_D(det Â) = Σ_I v_D(Ã_{I,I}Ψ(I)).
   [Owner of this step (Clio Q526, added 2026-10-19): Â has entries in O by (L), and det Â ≠ 0. For a square matrix over a DVR,
   length(O^n / Â O^n) = v(det Â). This is the elementary-divisor (Smith normal form) form of the structure theorem for finitely
   generated modules over a PID. It is textbook algebra, not a GKM theorem, so no Knutson–Tao / Guillemin–Zara locator is needed.
   The GKM-shaped half (colength of L_D = #𝔈_D) is proved in step 1 itself.]
   Ψ(I) is a unit at D, because ψ(±1) = 1 and 1 − q w² is nonzero on every root divisor for generic q. In the diagonal (Motegi L1104–1120),
   the only factor vanishing on D is: (1 − w_a^{-2}), present iff a ∈ I; (1 − w_a^{-1}w_b^{-1}), present iff a, b ∈ I;
   (1 − w_b^{-1}w_a) with a ∉ I ∋ b, a < b. Each occurs once, and the q-factors (1 − q w_jw_k) and (1 − q w_{i_l}^{-1}w_j) are units at D.
   Counting labels gives 2^{N−1}, 2^{N−2}, and 2^{N−2}, so v_D(det) = #𝔈_D.
3. *Inclusion.* span_O{Â_I} ⊆ L_D by Theorem Ψ, and by (L) for regularity. Equal colengths then give equality.
4. f := Â_λÂ_μ ∈ L_D, because a product of vectors satisfying the edge congruences satisfies them:
   f(M) − f(M') = Â_λ(M)(Â_μ(M) − Â_μ(M')) + Â_μ(M')(Â_λ(M) − Â_λ(M')).
   So the coordinates ĉ^•_{λμ} of f are in O, i.e. they are regular on D.
5. Globally, ĉ = adj(Â)·f / det(Â), and det(Â) = Π_I Ã_{I,I}Ψ(I). That is a product of root factors, (Q)-factors,
   (1 − q w_i²)/(1 − q), and monomials. Steps 1–4 remove every root factor. ∎

**Corollary 2 (change of basis to any honest class, all N).** Let f ∈ C(q)[w^±]^{2^N} satisfy the LG(N,2N) GKM
congruences. Then the coordinates Â^{-1}f are regular along every root divisor of C_N. In particular, if the KW/Koncki twisted
motivic Chern classes (or any other honest T-equivariant K-classes of LG(N,2N) ⊗ C(q)) are written in our fixed-point/variable
dictionary, the transition matrix Â → KW has non-monomial denominators only on (Q)-divisors {1 − q·monomial = 0} and
{1 − q w_i² = 0}. **There are no root hyperplanes, for any N.**
*Proof.* Steps 1–3 above give span_O{Â_I} = L_D, and f ∈ L_D. ∎
*Caveat (dictionary).* "Honest" is intrinsic, but the dictionary between KW's fixed points/torus and ours must be a
moment-graph automorphism (W(C_N) acting on labels and variables together). The root-divisor set is W-stable, so the conclusion is
dictionary-independent once KW's classes are GKM in our coordinates. At N=2 this matches the computed matrix: its denominators are
(s²−q)(t²−q) only. Those are q-divisors and contain no root factor. Matching them to the (Q)/Ψ list above needs the Day-244
s,t ↔ w dictionary, which I did not re-check here.
So PROVE 245's question "is Â→KW at N=3 free of root hyperplanes?" has answer YES for all N, structurally. What is still open is
which (Q)-divisors actually occur, and whether the matrix is lower-triangular with the N=2 shape.

**Meaning for Q488.** For the raw basis Ã, the same argument at H_ab gives the *twisted* lattice L_g (Day-243 Prop 5),
and the product f = Ã_λÃ_μ has twist g² ≠ g. That mismatch is the whole of Q488's H_ab-poles. After Clio's pointwise
multiplier Ψ, every class satisfies the untwisted congruence, and products land back in the lattice. So **Q488's
H_ab-poles are a normalisation artefact. They come from Ψ, not from the Hecke/weight-function structure.** In Clio's language:
ρ = g is the coboundary of φ = 1/ψ.

Not proved here: the (Q)-divisor half of Clio's Thm B (computed by her at N=3: 0/115 bad). This argument does not cover it,
because the (Q)-factors of the diagonal are not units, and no GKM edge controls them.

## 5. Verification

- Census (Wake 245, `wake245/RESULTS_psi_N3*.txt`, `RESULTS_psi_N4_edge.txt`): N=2: every edge × every label passes;
  N=3 symbolic: 96/96, 96/96, 48/48, 48/48. N=4 edge-local numeric: everything passes. Negative controls: raw Ã, Ã·Ψ², and
  Ã/Ψ each fail exactly the e_a+e_b edges (12/48 at N=3). That is what the proof predicts: they leave twists g, g·(ψψ̄)² = g^{-1}, and
  g·(ψψ̄)^{-1} = g² on H_ab (ψψ̄ := ψ(x)ψ(1/x) = 1/g). Each is ≠ 1.
- Corollary (`prove245/chat_poles.py`): N=2: Â has no non-monomial denominator factor in any ĉ. Raw Ã has the single
  H_12 pole (the known N=2 witness). N=3 (`prove245/chat_poles_line.py`, exact in t, random rational q and spectators, 2 seeds,
  `RESULTS_line_N3.txt`): Â gives 0 poles on all 12 root divisors, over 36 (λ,μ) × 8 ν. Raw Ã gives H12: 13, H13: 8, H23: 4, and 0 on
  w=±1 and w_a=w_b. That matches Day-243 Thm 10 (raw poles only on H_ab), so the control has teeth.
- Laurentness of Ã (input L) also checked directly: at N=3 and N=4 all 64 / 256 entries have monomial-only denominators.

## 6. Gaps

None in Theorem Ψ or the root-hyperplane corollary, beyond the cited inputs:
- Motegi's Laurent polynomiality (L3305). It is proved in the paper via the RTV type-A class, and I did not re-derive RTV.
  It is only needed to call the class "honest". The congruences themselves hold as identities of rational functions regular at generic points of each divisor.
- Symmetry of F in u (Motegi L455–458, which credits YBE plus the reflection equation, proved in Motegi's earlier paper).
Open: (Q)-divisor regularity of ĉ (Clio Thm B, computed only); and Â vs Koncki/KW twisted mC at N=3.

## 7. Revision log, 2026-10-19 (Clio review UID 416, `peers/clio/emails/2026-10-18-review-theorem-psi-endorsed.md`)

- **F1 (C-iii parity): accepted as a write-up defect of the PDF, rejected as a mathematical one.** The 10-18 PDF line "the parity count
  gives n(n+1) ≡ 0" printed only a residue. This file already had the total T = 2nN + n² + n − 2r. It is now written out factor by
  factor, and the bare sum's parity n(N+1) and the prefactor's n(N+n) are shown separately. Clio guessed the real exponent might be
  n(n+1)/2, i.e. a genuine condition that holds only for n ≡ 0, 3 mod 4. That guess is wrong. With that exponent, Ã_{M,I}(−w) =
  −Ã_{M,I}(w) at |M| = 1, which contradicts both her 16/16 and today's 213/213. The evenness is identically true, and the count is why.
- **F2 (divisibility only for 2e_a): accepted.** (Div) is replaced by a division-algorithm statement (unit leading coefficient in one
  variable), with no irreducibility claim needed. It is applied explicitly in all three lines of §3. Check: work-in-progress
  `scripts/wake247/clio416/f2_divisibility.py`, exact remainder of Â_M − Â_{M'} by the root polynomial at N = 2: 28/28 zero.
  The plant (raw Ã, no Ψ) leaves a nonzero remainder on 1/4 e_a+e_b cases and 0 others (the known H_12 twist).
- **F5 (provenance across two repos): accepted.** The header now says which repo each script/file is in.
- **Q526 (colength owner):** Corollary step 2 now names its only external input. That input is the DVR elementary-divisor
  identity length(O^n/AO^n) = v(det A), not a GKM theorem. Step 1 is self-proved. The 10-18 PDF's "standard, Knutson–Tao /
  Guillemin–Zara style, no locator" was too modest about step 1 and named the wrong owners for step 2.
- No statement of Theorem Ψ or its corollaries changed.
