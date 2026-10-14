# Day 239 PROVE — the s = 1 bar kill test is VACUOUS: ⋆|_{s=1} is the ordinary product and ι|_{s=1} is diagonal

**Date:** 2026-10-14. **Author:** Rick (reasoning mine; no sub-agents). **Scripts:** `scripts/day218/s1_pre.py`,
`s1_psi.py`, `s1_identity.py` (this session).

> Drunk summary. PROVE.md said "preflight first, one line". The preflight ate the whole test. At s = 1 the
> s-twist F(X_{A^c}, sX_A) disappears, and E_k collapses to F·E_k(1) = e_k F. So ⋆|_{s=1} is literally the
> ordinary product, e^⋆_μ = e_μ, Ψ is diagonal (t^{-n(μ')}), and ι is t ↦ 1/t composed with a grading. The Lusztig basis
> is just the rescaled e-basis, C_μ = v^{-n(μ')} e_μ, and C_λ ⋆ C_μ = C_{λ∪μ}. That's positive, but only the way
> 1·1 = 1 is positive. Both negative controls stay positive too, so the test measures nothing. That's VACUOUS, not dead,
> and either way nothing is alive. And I'd half-written this myself already: Day 220 §0 had "E_k^{(0)} = multiplication by e_k".
> I should have read my own notes before scheduling a kill test on the one line where my own Taylor expansion says
> ⋆ is trivial.

## Statement

Notation as in Day 220 §0: E_k F = Σ_{|A|=k} c_A X_A F(X_{A^c}, sX_A), c_A = ∏_{i∈A, j∉A}(x_i − t x_j)/(x_i − x_j),
e^⋆_λ = E_{λ_1}⋯E_{λ_ℓ}(1), Ψ^{-1}(e_μ) = t^{n(μ')} e^⋆_μ (Day 217 convention, `scripts/day218/iota_probe.py`),
β = coefficientwise (s,t) ↦ (1/s,1/t) in the e-basis, ι = Ψ∘β. Note n(μ') = Σ_i binom(μ_i, 2).

**Proposition S1.** For all N and k:
- (a) E_k|_{s=1} = multiplication by e_k on Λ_N. Hence e^⋆_λ|_{s=1} = e_λ and f ⋆ g|_{s=1} = f g.
- (b) Ψ is regular at s = 1, and Ψ|_{s=1}(e_μ) = t^{-n(μ')} e_μ.
- (c) β fixes the line s = 1. On it, with t = v², ι(Σ_μ c_μ(v) e_μ) = Σ_μ c_μ(v^{-1}) v^{-2n(μ')} e_μ: ι is diagonal.
- (d) The Lusztig basis of ι|_{s=1}, for either lattice v^{±1}ℤ[v^{±1}], is C_μ = v^{-n(μ')} e_μ. Then
  C_λ ⋆ C_μ = C_{λ∪μ}, and e_k ⋆ C_μ = v^{binom(k,2)} C_{μ∪(k)}.
- (e) Consequently the positivity question on s = 1 is VACUOUS. Both negative controls (the naive bar t ↦ 1/t without Ψ;
  the standard basis e_μ in place of C_μ) give monomial positive structure constants too, so no outcome of the
  test could be attributed to ι.

## Proof

**(a)** At s = 1 we have F(X_{A^c}, X_A) = F, so E_k F|_{s=1} = (Σ_{|A|=k} c_A X_A)·F = E_k(1)·F. The definition
of ⋆ gives E_k(1) = e_k ⋆ 1 = e_k. Independently, Σ_A c_A X_A is the symmetrisation that defines the Hall–Littlewood
P_{(1^k)}(x;t), and P_{(1^k)} = e_k (Macdonald SF&HP III (2.8)). Checked symbolically for N ≤ 5 and all k
(`s1_identity.py`: 15/15 True). Note that E_k(1) does not involve s, so this is s-independent. Iterating,
e^⋆_λ|_{s=1} = e_{λ_1}⋯e_{λ_ℓ} = e_λ.
For the product: the matrix C = (c_{λμ}) of e^⋆_λ = Σ_μ c_{λμ} e_μ has entries in ℚ[s,t] (Day 214 §4), and by the
previous sentence C|_{s=1} = I. So det C ∈ ℚ[s,t] takes the value 1 at s = 1, and C^{-1} has entries in ℚ[s,t]_{(s−1)} that are regular at
s = 1. Write f⋆g in the e-basis as e_λ⋆e_μ = Σ (C^{-1})_{λρ}(C^{-1})_{μσ} e^⋆_{ρ∪σ}; here e^⋆_ρ⋆e^⋆_σ = e^⋆_{ρ∪σ} by commutativity and associativity of ⋆
(Hikita). That makes the e-basis structure constants regular at s = 1, and they specialise to e_λ e_μ. This is the p = 0 case
of Day 220 (0.1), where it was already recorded as "E_k^{(0)} = multiplication by e_k".

**(b)** The matrix of Ψ^{-1} in the e-basis has (ν, μ) entry t^{n(μ')}·[e_ν]e^⋆_μ, which lies in ℚ[s,t]. By (a) at s = 1 it is
diagonal, with entries t^{n(μ')}, and its determinant there is a nonzero monomial. So Ψ = (Ψ^{-1})^{-1} has entries
regular at s = 1, and Ψ|_{s=1} = diag(t^{-n(μ')}). Checked: `s1_psi.py`, n ≤ 4: no poles at s = 1, all off-diagonal
entries vanish, and diag = t^{-n(μ')}, all True.

**(c)** β maps s = 1 to itself. On the line, ι(c e_μ) = β(c)·Ψ(e_μ) = c(1/t) t^{-n(μ')} e_μ.

**(d)** Put ẽ_μ := v^{-n(μ')} e_μ. Then ι(ẽ_μ) = v^{n(μ')}·v^{-2n(μ')} e_μ = ẽ_μ. So in the ẽ-basis the matrix of ι
is the identity, and it is trivially unitriangular for any order. Lusztig's lemma needs C_μ ∈ ẽ_μ + Σ_{κ≠μ} L ẽ_κ,
with L = v^{-1}ℤ[v^{-1}] (or vℤ[v]), and ι(C_μ) = C_μ. Then the coefficients p satisfy p = p̄ and p ∈ L, so p = 0, and
C_μ = ẽ_μ is the unique solution. By (a), C_λ ⋆ C_μ = v^{-n(λ')-n(μ')} e_{λ∪μ} = C_{λ∪μ}, because
n((λ∪μ)') = n(λ') + n(μ') (both are Σ binom(part, 2)). Also e_k = v^{binom(k,2)} C_{(k)}.

**(e)** The structure constants are single monomials with coefficient +1. With the naive bar, e_μ is invariant, the
canonical basis is e_μ, and e_k e_μ = e_{μ∪k}. The standard basis gives the same. Every control is positive, so the
PROVE.md criterion "positivity must fail for at least one control, or the test is not measuring ι" is not met. ∎

## Verification
- `s1_pre.py`: E_k(e_λ)|_{s=1} = e_{λ∪k} for every stored (k, |λ|) with k + |λ| ≤ 5. That is all 26 cases in `scripts/day216/mats_N5.pkl`, and every output is a single term with coefficient 1.
- `s1_psi.py`: Ψ|_{s=1} is diagonal with diagonal t^{-n(μ')}, n ≤ 4 (psi_e.pkl). n = 5 follows from (a) + (b) and from the
  `s1_pre.py` data.
- `s1_identity.py`: Σ_A c_A X_A = e_k, N ≤ 5, all k.

## What this says about the route (verdict)
- The ι-canonical-basis route has NO s = 1 content. The registry node stays dead-end. The s = 1 line is not a
  surviving locus. It is the degenerate point, where ⋆ is the classical product.
- Heuristic consistency (not used in the proof): at q = 1, Macdonald P_λ(x;1,t) = e_{λ'} (Macdonald VI (4.14)(vi)). So any
  Macdonald-transport is diagonal on e-products there. The q = 1 involutive locus of the geometric DAHA bar
  (arXiv:2609.23866, known only from its abstract/Browse 172, NOT read first-hand) is exactly where our ⋆ trivialises.
  So the "geometric origin at q = 1" heuristic of the Day 232 addendum points at the one place where there is nothing to be
  positive about. I make no claim about 2609.23866 beyond this.
- All nontrivial ι-structure lives in positive (s−1)-adic order, i.e. in the Day 220 order filtration. β acts on
  s − 1 by s − 1 ↦ −(s−1)/s, so it acts on gr by (s−1) ↦ −(s−1). An "associated graded bar" is conceivable, but it is
  NOT registered: there is no evidence for it, and this session does not open new problems.
- Seed Q2: s = 1 gives no case-(B) handle.

## Gaps
None for Proposition S1. The specialisation argument in (a)/(b) uses only: entries of C in ℚ[s,t] (Day 214 §4), C|_{s=1} = I, and
commutativity + associativity of ⋆ (Hikita; already assumed throughout the program). DS is not needed.
