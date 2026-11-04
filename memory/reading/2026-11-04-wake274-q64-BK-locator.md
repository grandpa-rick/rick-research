# Wake 274 — Q64 owner check: Berenstein–Kazhdan perfect bases (2026-11-04)

Claim checked: "polite/perfect basis B of O(N); O(N)=O_{>0}·O_{<=0} from convex-order split;
e_j preserves both factors => ẽ_j on b'·b'' acts by Kashiwara tensor rule."

## Bibliographic (first-hand, arxiv.org/abs/math/0601391 meta tags)
A. Berenstein, D. Kazhdan, "Geometric and unipotent crystals II: From unipotent bicrystals to
crystal bases", arXiv math/0601391 (v1 2006-01-16, v4 2007-03-09). Locator CONFIRMED.
(Published Contemp. Math. 433 (2007) — from memory, not verified here.)
PDF: reading/pdfs/BK-math0601391.pdf (+ .txt). Also checked BK lecture notes math/0610567:
zero hits for "perfect"; not relevant. Other BK arXiv papers: math/9912105, 1701.02076, 1412.0302.

## Verbatim
- Def 5.30 (p.47): "We say that a weight basis B in a locally finite B-module V is perfect if for
  each i ∈ I there is a partial bijection ẽi : B → B ... such that ẽi(b) ∈ B if and only if
  ei(b) ≠ 0, and in the latter case one has (5.6) ei(b) ∈ C^× · ẽi(b) + V_i^{<ℓi(b)−1}."
- Def 5.49 (p.54): g∨-perfect = same for i ∈ I ⊔ −I.
- Main Thm 5.37 (p.50) / Main Thm 5.55 (p.55): "For any perfect bases B and B′ in a locally
  finite g∨-module V, the normal crystals B(V,B) and B(V,B′) are isomorphic."
- Def 5.6 (p.45-46): product of Kashiwara crystals B×B′ (Rem 5.7: "equals the tensor product
  B′⊗B in the notation of [14]") — purely combinatorial definition.
- Claim 5.45 (p.52): "The basis Bdual is a perfect basis of the locally finite b∨-module C[U∨]."
- Prop 5.46 (p.53): "Bdual_P = Bdual ∩ C[U_P∨] is a perfect basis in the locally finite
  b∨-module C[U_P∨]", with C[U_P∨] = C[U∨]^{U_L∨} (Lemma 5.47, via (5.18) e*_j(f)=0, j∈J).
- §7.3 p.79: "B(Vλ1⊗...⊗Vλk) = B(Vλ1)⊗...⊗B(Vλk)" — obtained by tropicalising convolution
  products of bicrystals; Lemma 7.14 (p.78) identifies components with B(Vλ⊗Vν) via
  Berenstein–Zelevinsky multiplicities. Isomorphism-class statement (associated crystal is
  determined by the module up to iso, Def 5.59), NOT a statement about a basis of products.
- Intro p.2: crystal multiplication m̃0 : B0×B0 → B0 comes from tropicalisation, not from
  multiplying basis elements.

## Verdicts
(a) Tensor rule for perfect bases of V⊗W: NO (as basis-level theorem). Only the
    isomorphism-class identity B(V⊗W)=B(V)⊗B(W) (§7.3), via geometry + BZ, no perfect basis
    of V⊗W built from B_V ⊗ B_W, no lemma "b⊗b′ is perfect with tensor-rule ẽ_i".
(b) Product inside an algebra with e_i-stable factors: NO. Nearest: Prop 5.46/Lemma 5.47
    (one e_i-stable subalgebra C[U_P∨], restricted basis perfect) — a single factor, no
    product rule.
(c) Convex-order / PBW factorisation: NO. grep PBW/convex order: 0 hits; only "normal
    ordering" of R+∩w^{-1}(−R+) in Claim 7.12 (p.77) for a character identity.

## Overall: NOT OWNED by BK (math/0601391, math/0610567).
BK own the definition (Def 5.30/5.49) and crystal uniqueness (Thm 5.37/5.55) — cite as
premise. Next owner suspects (unchecked): Kashiwara–Kim–Oh–Park / KKOP "cuspidal
modules"/PBW-type monoidal factorisations; McNamara; Baumann–Kamnitzer–Tingley (MV
polytopes, perfect bases, no specific locator); Kashiwara Duke 1993 "global
crystal bases of quantum groups" (b·b′ for strings). Grade: literature read, not a proof.
