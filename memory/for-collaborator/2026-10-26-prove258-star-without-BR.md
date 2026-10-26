# PROVE 258 — the half-integer results no longer need Buch–Ravikumar

For Clio (cc Robin). Draft WIP d118e27, `papers/lg-og-negative-degree/main.pdf` (27 pp).

**Claim.** On LG, the negative-degree recursion (★) (Prop 4.12), s_{x+1}(κ) = s_x(κ) + Σ_{ρ⊊κ} V(θ) s_x(ρ),
follows from the LS proof of Thm 1.1 alone. There is no BR, no G0 and no Prop 4.6 in it.

**Proof (four lines).** Thm 1.1(b), proved in §3 from (G1)+(LS), gives s_j(κ) = N_κ(j) for every integer j ≥ 1 and every κ.
Lemma 4.13 (peeling the top two values, a pure count) is exactly (★) at every integer j ≥ 1. For fixed κ, both sides are
polynomials in x, so they agree everywhere. This is not circular, as long as the second proof of Thm 1.1 keeps the K-theoretic proof of (★).

**What changes.** Theorem HZ, Cor 1.6 (Thm B), Prop 6.16(a), Thm Z and both proofs of the window theorem on LG now depend only on
(G1)+(LS). Lemmas 5.1/5.2 and Thm Z are restated with the coefficient V(θ) of (★): "V(θ) ≠ 0 ⇒ no 3-chain" is Lemma 4.4,
which is pure combinatorics. Remark `rem:deps` at the start of §6 says this. Prop 4.6 is now used only for Thm 4.8 (the closed
form of the K-theoretic Pieri coefficients c_ρ) and for the second proof of Thm 1.1.

(★) does NOT give Thm 4.8 back. Combining it with the hyperplane recursion gives only Σ (c_ρ − ±V) H_ρ ≡ 0, and the H_ρ
for ρ ⊊ κ are linearly dependent already at κ = (3,1): there are five of them, each of degree ≤ 3.

**Checks.** (★) checked as a polynomial identity against Demazure Hilbert polynomials for m ≤ 4, with 0 failures. Negative
control: adding 1 to any single coefficient V(θ) breaks (★) at some integer j ≤ m, and all 143/143 perturbations were caught.

For the FPSAC cut, the risk item "HZ / Cor 1.6 hinge on Prop 4.6" is gone. Only Thm 4.8 still needs the per-result AI flag.
Thm Z is unaffected in content: what you endorsed (uid451) still stands, and its proof now cites (★) instead of the Pieri support.

## Dream 258 addendum (optional, one line in the email at most)
Why the cheap proof stops at Thm 4.8: (★) is Q30 pushed to a point (χ), and the Hilbert polynomials of the ρ⊊κ are
dependent, so χ can't pin down the c_ρ. A T-equivariant (LS-character) version of the peel lemma might recover Thm 4.8
without BR too. That's a hunch for after submission, not for this paper.
