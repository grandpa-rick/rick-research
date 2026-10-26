# For Clio / Robin: PROVE 259, the weighted peel, and Q30 without Buch–Ravikumar

Full proof: `rick-research/proofs/2026-10-27-weighted-peel.md`.

1. Give each shifted box (a,b) the weight β = ε_m on the diagonal and ε_{m−d} − ε_{m+1−d} at offset d = b−a. Along a
   row these telescope to ε_{m+1−p}, so the LS weight π(1) is linear in the order-preserving map. That gives
   ch_κ(j) = Σ_G x^{j w_κω + ΣGβ}. Stanley's cone reciprocity then gives the strict side,
   (−1)^{|κ|}ch_κ(−j) = Σ_f x^{−j w_κω − Σfβ}. This is a T-equivariant version of thm:main(b).
2. lem:peel is weight-preserving. The top layer contributes x^{−w_κω − Σ_{o-boxes}β}, independent of j.
3. The torus-equivariant characters ch_ρ are linearly independent, although the Hilbert polynomials H_ρ are not
   (κ = (3,1)). So the equivariant hyperplane recursion pins down the coefficients of [L^{−1}]·[O_κ] in K_T, and
   forgetting T gives c_ρ = (−1)^{|θ|−1}V(θ), i.e. Theorem Q30 (Thm 4.8), without (BR). The inputs are (G0), (G1), (LS),
   and the R(T)-span of Schubert classes.
Owner caveat: the K_T-Chevalley formula (Lenart–Shimozono, Lenart–Postnikov) must agree by uniqueness. What's new is
the route and the shifted-diagram form. Not for the FPSAC cut; at most a post-submission remark.
