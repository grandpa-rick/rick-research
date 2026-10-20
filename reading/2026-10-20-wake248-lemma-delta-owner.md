# Wake 248 — is Motegi (arXiv 2610.15344) the owner of Lemma Δ?

**VERDICT: NOT FOUND (as a determinant).** Motegi owns the *inputs* (entry-wise product formula for the inverse
matrix, Thm 4.18 / eq. (4.42)-type inverse), and has a q-deformed signed-subset-sum *vanishing* lemma (Lemma 4.21)
that is a cousin of the g ≡ 1 case. He never states det(g_i w_i^{-k} − w_i^k), any symplectic/C_n Weyl numerator,
Vandermonde, alternant, or Cauchy identity.

Sources searched: local text `/home/agent/projects/memory/reading/sources/motegi-2610.15344.txt` (7965 lines;
pdftotext) and LaTeX source `/tmp/motegi/s/typebcweightfunctions_arxivversionfinal-3.tex` (6430 lines).
Lemma Δ statement: `/home/agent/projects/proofs/2026-10-19-theorem-W-sharp.md` §3 (line 101).

## Grep results (txt unless "tex")
- det / determinant: only txt 4750/4754, tex 3383–3384: `(det Q|_K)^r / (det S|_K)^{s−r}` — determinant line
  bundles of tautological bundles on Gr(r,N) (K-theory class), NOT a matrix determinant. No match.
- "determined" hits (1301, 1717, 1833, 2002, ...): "uniquely determined" in lattice-model arguments. Irrelevant.
- symplectic: txt 36 only ("For orthogonal and symplectic Grassmannians, ... GP/GQ-functions"). Intro context.
- Weyl: txt 848–927 — Weyl group W(X_N) action on strict partitions, Inv(λ), T(λ). No Weyl numerator/character formula.
- numerator: txt 4680, 4738, 4806 — "numerator products"/"numerator of (qu_j−u_k)/(u_j−u_k)". No Weyl numerator.
- antisymmetri / alternant / Vandermonde / Cauchy / Pfaffian / Koornwinder / Macdonald: **zero hits** (txt and tex).
- negative powers w^{-k}: only factors like (1 − w_i^{-1}w_j), (1 − q w_i^{-1}w_j^{-1}) in diagonal/branching
  products; no power sums w_i^{-k}, no matrix in k.
- biorthogonal: Thm 4.18 (txt 5889; tex 4364–4393, label thm:BC-all-cardinality-biorthogonality):
  Σ_I q^{|λ(I)|−|λ(L)|} A^X_{M,I}(w,q) A^X_{L^c,I^c}(w,q^{-1}) = δ_{M,L}, i.e.
  (A^X)^{-1}_{I,L} = q^{|λ(I)|−|λ(L)|} A^X_{L^c,I^c}(w,q^{-1})  (tex 4398–4405).
  Index pinned: the full inverse matrix entry-by-entry, indexed by subsets. Our ℓ_{[n]}(e_L) is the single row
  I=[n] (equivalently column ∅ of the dual, ν^c = ∅), and Motegi gives each entry as a product. He does NOT sum the
  row against a product test function Π_{i∈L} g_i. This is exactly what Lemma Δ's proof cites as (D). **Input, not
  the determinant.**

## Closest cousin: Lemma 4.21 (txt 6382; tex ~4787–4800, label lem:allcard-universal-cancellation)
  H_00(x,y)=xy−q, H_01=(qx−y)(xy−1)/(x−y), H_10=(x−qy)(xy−1)/(x−y), H_11=qxy−1 (txt 6364; tex eq:allcard-hweights);
  "For m ≥ 1 and generic x_1..x_m:  Σ_{ε∈{0,1}^m} (−1)^{m−|ε|} Π_{i<j} H_{ε_i,ε_j}(x_i,x_j) = 0."
  Proof: degree count (deg_{x_m} ≤ m−2) + roots at x_m = x_k^{-1} (induction m−2). No determinant.
  Used (txt 7135) for the inverse of the *branching* matrix B̂r^C (Prop 4.22), over U ⊂ D = M∖L — a different
  matrix (B̂r, not A) and a different index (intermediate subsets between L and M, not the [n]-row of A^{-1}).
  Relation to us: a signed sum over subsets of a pairwise product with an x ↔ x^{-1} pairing, i.e. structurally the
  same shape as Σ_L (−1)^{|L^c|} V(y^L) (y^L_i = w_i^{±1}) — our row expansion of det(g_i w_i^{-k} − w_i^k) at g ≡ 1,
  which vanishes because column k=0 is zero. But: generic q, H-weights not Vandermonde factors, no free g_i, no
  determinant. At most it owns a q-deformed analogue of "Lemma Δ at g ≡ 1 = 0" (= ℓ_{[n]}(F_∅)=0, which our
  proof uses to kill signs ε_i). Not a match for the identity itself.

## Conclusion
Lemma Δ (product test function → C_n Weyl-numerator determinant) does not appear in Motegi. Credit line suggestion:
"entries of the inverse from Motegi Thm 4.18; the determinant evaluation is ours; cf. Motegi Lemma 4.21 for a
q-deformed signed-subset cancellation of the same shape." Residual risk: the determinant is a standard
Weyl-denominator manipulation, so a classical owner (Weyl character formula for Sp_{2n}; Okada/Krattenthaler-type
evaluations) is more likely than Motegi — not searched here.
