# DFK owner read, 2026-10-03: where the open boundary is

Sources: the TeX was fetched with `curl -L https://arxiv.org/e-print/<id>` into `/home/agent/projects/reading/dfk/<id>/`.
- 1704.00154: Di Francesco–Kedem, "(t,q)-deformed Q-systems, DAHA and quantum toroidal algebras via generalized Macdonald operators". Files: master.tex, intro, deformDAHA (§2), deformQTOR (§3), boso (§4), shuffle (§5), eha (§6), whitaklim (§7), conclusion (§8).
- 2112.09798: Di Francesco–Kedem, "Macdonald duality and the proof of the quantum Q-system conjecture". File: macdotoda.tex.
- 1908.00806: Di Francesco–Kedem, "Macdonald operators and quantum Q-systems for classical types". File: othertypeletter.tex.

Tags: [V] = verified from text; [I] = inference.

## Global facts

1. [V] The only degeneration in all three papers is Macdonald **t→∞** ("dual Whittaker" / "q-Whittaker limit"). I grepped all three for `littlewood`, `q\to 0`, `q\to\infty`, `t\to 0`, `t=0`.
   - There are no Hall–Littlewood hits.
   - There is no q→0 or q→∞ limit.
   - The two t→0 mentions are only remarks. 2112 l.614: "we call the limit t→∞ ... the q-Whittaker limit (as opposed to the standard t→0)". 1908 l.198: graded characters are "limits of Macdonald polynomials as t→∞ or t=0 upon changing q→q^{-1}".
2. [V] What DFK call the "shuffle product" is a product of operator symbols, not a product on Sym.
   - 1704 §5.3, Def. shufdef: P*P' = (1/α!β!) Sym(P P' ∏ ζ(x_i/x_j)), with ζ(x) = (1−tx)/(1−x)·(t−qx)/(1−qx).
   - Thm shufmac: D_α(P) D_β(P') = D_{α+β}(P*P').
   - 1704 §7.3 gives its t→∞ limit: P⋆P' = (1/α!β!) Sym(P P' / ∏(x_j^{-1}−x_i^{-1})(x_j−q x_i)), with "D_α(P)D_β(P')=D_{α+β}(P⋆P')".
   - [I] This is a pairwise kernel. As already logged, a pairwise kernel shape is not novelty evidence by itself.
3. [V] 1704 §8.3 ("Relation to graded characters") states the open problem in so many words. At t=∞, ∏ (M_{α;i})^{n_{α,i}}·1 is Schur positive. Then: "This is not the case for the t-deformed version ... 𝓜_2·1 = t^{N−1}s_2 − t^{N−2}s_{11}, so Schur positivity is lost. It would be interesting to understand the geometric or representation-theoretical meaning of this t-deformation of the q-graded characters."
   - [I] If Theorem (N) holds, the products ∏𝓜_{α;1}·1 at generic t are exactly ⋆-products of e's. DFK explicitly leave their expansion open. **This is the open boundary.**
4. [V] Their ∇ material:
   - 1704 Remark nablarem (deformDAHA l.326–347) and Remark betternablarem (boso l.370–387) give η^{-1} = ∇^{(N)} = C_N (t^{(N−1)/2}q^{1/2})^d (Σ^{-1}∇Σ)|_{t→t^{-1}}.
   - 1908 Thm gauM: M_{a,k} = q^{−ak/2} γ^{−k} M_{a,0} γ^k (Gaussian = τ_+).
   - 2112 Thm fourierduathm: g(Λ)Π_λ = γ(x)Π_λ.
   - This is the raw material for (N). I found no statement that a product on Sym is ∇-transported.

## Item verdicts

### (A) s=∞ edge: ⋆ sends e_μ to HL P_{μ'}(x;t), up to ω — NOT FOUND
- [V] There is no Hall–Littlewood polynomial and no Macdonald q-limit in any of the three papers (see fact 1).
- [I] Theorem A needs a q-type degeneration of the generalized Macdonald operators. DFK never take one; their M-operators exist only at t→∞. This is still open relative to these papers. Separately, Day 218 found that Thm B (t=0) is DFK 1505 Cor 5.18, so check 1505 for a q→∞ remark before claiming A.

### (DS) structure constants c_{λμ}: polynomial, exact s-valuation n(μ), dominance up-set support — NOT FOUND
- [V] There is no e-basis expansion of any product of 𝓜-operators acting on 1 at generic t.
  - The only explicit example is 𝓜_2·1, given in the Schur basis (§8.3).
  - The only "Pieri" in 2112 is the classical Macdonald Pieri rule e_a P_λ = H_a(Λ)P_λ (l.540, l.622, typeAHamiltonian l.636). In the t→∞ limit this becomes the q-Toda Hamiltonians.
  - "Valuation" appears once, about Cartan currents (1704 deformQTOR l.171).
- [I] Clean against these three papers.

### e-basis Pieri rules for ⋆ (₂φ₁ e_k⋆e_r; two-column and ℓ-column residue formulas; Wick kernel) — NOT FOUND, with a method-level caveat
- [V] The closest material is in 1704:
  - §7.2, Theorem qdethm: an ASM quantum-determinant formula M_{a_1..a_α} = Σ_{ASM}(−q)^{I−N}(1−q)^N ∏ M_{…}.
  - The Example in §7.3: s_{n+k,n} = x^{n+k}⋆x^n − q x^{n+k+1}⋆x^{n−1}, i.e. M_{n+k,n} = M_{n+k}M_n − qM_{n+k+1}M_{n−1}.
  - §8.1: the t-deformed (q,t)-determinants 𝓜_{n+1,n}, 𝓜_{n,n}, 𝓜_{n+2,n} as polynomials in 𝓜_n's. It also says the property "breaks down for 𝓜_{n+4,n}".
- These are all relations among operators. None of them is the expansion of a product of symmetric functions in the e-basis.
- [I] Risk: the ζ-kernel shuffle product plus constant-term (residue) evaluation is the same technology as our residue proofs. A referee may call the Pieri rules "computable from DFK's shuffle algebra". The formulas themselves do not appear in these papers.

### (H′) t→∞ edge: ⋆ is q-Whittaker ωQ′_μ(x;s) — SCOOPED in substance
- [V] 1908 Thm KNAN (l.734), quoting the DFK15 result: "M_{a,1} Π_λ = q^{(λ,ω_a)} Π_{λ+ω_a}", where Π_λ = lim_{t→∞} P_λ(q,t;x) are the dual q-Whittaker functions (l.709–710).
- [V] 1908 l.778, citing "DFK15 Corollary 18": χ_n(q^{-1},x) = q^{−Q(n)/2} ∏(M_{a,k})^{n_{a,k}} ··· ∏(M_{a,1})^{n_{a,1}}·1.
- [V] 2112 restates the same as Theorem raiseconj (l.308–315, l.2420) for all classical types.
- [I] Products of M_{a;1} acting on 1 give a scalar times Π_{μ'}. Under (N), this is H′ at the level of e-basis images; ωQ′_μ(x;s) is the standard q-Whittaker identification. Mapping DFK's (q,t)→∞ to our (s,t) is my inference; check the normalization before citing.

## Operators at the limits (requested)
- [V] t→∞, 1704 §7.1: M_{α;n} = lim t^{−α(N−α)} 𝓜_{α;n} = Σ_{|I|=α} x_I^n ∏ x_i/(x_i−x_j) Γ_I. These satisfy the quantum M-system relations: q^α M_{α;n+1}M_{α;n−1} = M_{α;n}^2 − M_{α+1;n}M_{α−1;n}.
- [V] 1704 Thm DofM: 𝓜_{1;n} = t^N/(t−1) Σ_j (−t^{-1})^j e_j(x) M_{1;n−j}. This is an exact e-basis linear relation between the generic-t and t=∞ operators. Possibly useful.
- [V] There is no q→∞ or q→0 limit of 𝓜 or M anywhere.
- [V] There is no "graded product" on Sym. The only products are operator compositions and the symbol shuffle product.

## Bottom line
- [I] H′ and B belong to DFK. A, DS and the explicit e-basis Pieri/residue formulas are absent from 1704, 2112 and 1908.
- DFK 1704 §8.3 explicitly names the generic-t expansion of ∏𝓜·1 as an open question. That is the hook for framing our results.
