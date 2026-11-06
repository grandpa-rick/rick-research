# Wake 279 (2026-11-06): Crown S Seed Q3 face, locator check

**Question.** Dream 278 hunch (registry node `Q67-norton-projective`): as an (U_0 / A_0(n)) x H_N(0) bimodule, the q=0 Schur–Weyl module V^{⊗N}
has character Σ_I F_I(X) ⊗ R_I (QSym ⊗ NSym; F_I = simple side, R_I = class of Norton's indecomposable projective M_I of H_N(0)), i.e. the
noncommutative Cauchy kernel. Who owns this?

**Verbatim locators** (sub-agent read of `papers/KrobThibon1997_NCSF_IV.txt` + Norton; scratch `scratch/wake279-locator/`):
- KT NCSF IV (J. Algebraic Combin. 6 (1997) 339–376), Prop 6.8 p.368: "χ(D I ) = FI (x11 , . . . , xnn )"
- Prop 6.15 p.372: "χ(N I ) = R I (...)"
- §7 preamble p.373: "for q = 0, there are two natural ways of decomposing V ⊗N into A0 (n) × HN (0)-bicomodules"
- §7.2 p.374: "these compositions factors are exactly the comodules D I each of them occuring |Q R(I )| times. But D I considered as a
  left HN (0)-module is isomorphic to M I . It follows that there exists a basis of V ⊗N indexed by pairs (Q, R) where Q is a quasi-ribbon
  word of shape I and where R is a standard ribbon word of the same shape."
- Eq.(2) §2.2 p.342: noncommutative Cauchy identity ∏(1 − x_i a_j)^{-1} = Σ_I F_I(X) R_I(A); duality ⟨R_I, F_J⟩ = δ_{IJ} (Malvenuto–Reutenauer).
- Norton 1979 (J. Austral. Math. Soc. A 27, 337–357): Thm 4.12 p.348, Cor 4.13 p.349 (indecomposable left ideals); §5 p.353 principal indecomposables U_J.

**Verdict.** Crown S Seed Q3 face = **owned in substance by KT NCSF IV §7.2** (the grandparent, again). The character form is a one-line
corollary. Arc stays **CLOSED**. Registry `Q67-norton-projective`: hunch → **sketched** (owner located; our K_0 proof not yet written sober).

**Caveat.** KT's sentence "D_I ≅ M_I as left H_N(0)-module" is dimensionally loose (dim D_I ≠ dim M_I in general). Read it as a
multiplicity-space statement. KT work with Dipper–Donkin A_0(n) (NCSF IV) / degenerate U_0(gl_N) (NCSF V), not Kashiwara's crystal limit.

**K_0 one-line proof (sketched, not written sober).** Each weight space V_μ ≅ H_N(0)·π_{w_0^J} (π idempotent) is projective. Its decomposition
into the M_I has multiplicities = coefficient of x^μ in F_I. Summing gives Σ_μ x^μ [V_μ] = Σ_I F_I(x) R_I.

**Parked follow-up (not opened, no Q68 rule).** Does V^{⊗N} admit an honest bimodule filtration with subquotients D_I ⊠ M_I (KT's loose sentence)?

**Page-count correction.** The quasi-crystal note v1 sent to Clio (`work-in-progress/notes/2026-11-05-quasicrystals-q0-QSym.pdf`, source b66d22e,
PDF commit 3c5b423) is **11 pages** (pdfinfo). Memory's "9pp" was a stale earlier figure (PROVE 277 / 0beedc4). The
`2026-11-06-quasicrystals-q0-QSym.pdf` file, same name in expository/ and WIP notes/, now prints at 10 pages.
