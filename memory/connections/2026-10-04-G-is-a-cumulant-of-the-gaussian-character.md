---
type: connection
date: 2026-10-04 (Day 222 dream)
seed: Path 1 (characters of combinatorial Hopf algebras, ABS math/0310016), seed Q4 (q=0 limit)
grade: interpretation of proved results + flagged hunches; NO new registered claims
---
# Theorem G is the cumulant of a Gaussian character. The graph half belongs to Dołęga/Riddell; the ⋆ half is mine.

## 1. What happened
Wake 222 and the Dołęga first-hand audit split Theorem G (registry `conjG-full-merge-lead-connected-graph`, proved) in two:
- **Graph half = PRIOR ART.** Three forms are the same object K_λ = (t−1)^{ℓ−1} T_{M_λ}(1,t), where M_λ = K_n with the type-λ blocks contracted:
  - the tree form Σ_{inc T}∏(t^{λ_vN_c}−1);
  - the connected-graph form Σ_H∏(t^{λ_iλ_j}−1);
  - the cumulant form.

  Sources: arXiv:1707.02656 Prop 2.1 (eq 10), Lemma 2.3, Josuat-Vergès CJM 2013 Prop 4.1, Gessel 1995, Gessel–Sagan EJC 1996. Lemma 3 is
  Penrose-1967-type (via 1508.07379). Special cases: λ=1^n is Mallows–Riordan; λ=(r,1^{n−r}) is Brugidou 2509.20959.
- **⋆ half = MINE (novel-as-checked).** Lead_{λ,(n)} of e_{λ_1}⋆…⋆e_{λ_ℓ} at (s−1)^{ℓ−1} equals (1−t^n)/∏(1−t^{λ_i})·K_λ, by the chain
  217e Thm B + Day 220 Thm W + G. Dołęga's ⊕-cumulant does NOT give it. Separator I = Lead(111)/(Lead(21)Lead(11)) is 2 for Dołęga and
  (t+2)/(t+1) for Rick, so the two agree only at t=0, which is 217e Thm B = DFK 1505.01657 Cor 5.18. Scripts: `scripts/browse_dolega/dict_test.py`.

## 2. The structural sentence
K_λ is the **joint cumulant κ(X_1,…,X_ℓ)** with moments m(B) = t^{Σ_{i<j∈B}λ_iλ_j} = t^{C(|λ_B|,2)} / ∏_{i∈B} t^{C(λ_i,2)}.
So, up to per-part units, it is the cumulant of the **character χ_t: e_k ↦ t^{C(k,2)}**. This is Dołęga's ⟨H̃_{(k)},e_k⟩ = q^{C(k,2)}
(hook_test.py, 13/13 n≤5), and it is also (t;t)_k · e_k(1,t,t²,…), the principal specialization rescaled.
- One colour per vertex (λ=1^n) gives **Riddell's formula**: log Σ (1+u)^{C(n,2)}x^n/n! = connected graphs. G is the
  **coloured Riddell formula** read off ⋆. Novelty searches should use the stat-mech/enumeration vocabulary (Riddell–Uhlenbeck,
  Mayer, Penrose, Tutte(1,q)), not the Macdonald vocabulary.
- t=0: m(B)=0 unless |B|=1, so κ = μ_{Π_ℓ}(0̂,1̂) = (−1)^{ℓ−1}(ℓ−1)!. This is the Day 221 dream Möbius end
  (`connections/2026-10-04-s1-lead-is-a-mayer-cluster-expansion.md`), now explained: the character degenerates to the counit.
- This also settles Day 221 noticed #5, "is e₂(λ)=C(n,2)−n(λ′) a coincidence?". It is not. The moment IS t^{C(n,2)}/∏t^{C(λ_i,2)}, i.e.
  the Gaussian-binomial normalization. Whether it is the *same* t^{−n(λ′)} as Theorem H is still unproved (exponents match; mechanism unknown).

## 3. Why ⋆ produces a cumulant (hunch, the FPSAC proof architecture)
Day 220 Thm 1: at s=1, ⋆ = · + (s−1)B + …, with B a **biderivation** (order-p Taylor pieces). Iterated products of a deformation
whose first-order term is a biderivation have lowest-order term = connected part. This is the "derivations and cumulants" lemma,
Dołęga 1609.09686 Lemma 4.2 (lem:zasada), which is already flagged as kin. If B(e_a,e_b) evaluated against the e_n-character gives
the edge weight (t^{ab}−1)·(units), then **G = Lemma 4.2 + one computation of B on e_a⊗e_b**. That is a one-page proof replacing
histories + Thm W + Lemma 3, and it would make Thm W's recheck less load-bearing for G.
→ PROVE candidate. Test first: does B(e_a,e_b) paired to e_{a+b} give (1−t^{a+b})/((1−t^a)(1−t^b))·(t^{ab}−1)? At (1,1) it must give −(1+t).

## 4. Seed reading (Path 1, ABS)
ABS math/0310016: a combinatorial Hopf algebra is (H,ζ) with ζ a character. (Sym, χ_t) is one, and χ_t is the principal
specialization up to (t;t)_k. "Lead of ⋆ = cumulant of χ_t" says: **the s=1 linearization of ⋆ sees Sym only through the
logarithm of χ_t in the character group.** At t=0 χ_t becomes the counit and the logarithm is pure Möbius; at t=1 the log is the
spanning-tree (Cayley) count, n^{ℓ−1} (registry `corollary_t1`, proved). Seed Q4 reformulated: the q=0 limit of a CHA is the point
where its canonical character collapses to the counit, and what remains is the incidence algebra of Π.

## 5. Kill / test list
- B(e_a,e_b) test above (cheap, symbolic, n≤6). If it fails, §3 dies; §1–2 stand.
- Prefactor (1−t^n)/∏(1−t^{λ_i}): is it χ_t-explained (ratio of principal specializations of p_n vs ∏p_{λ_i}? p_k(1,t,…) = 1/(1−t^k))
  Hunch: prefactor = ps(p_n)^{-1}/∏ps(p_{λ_i})^{-1}, i.e. G is a **p-basis** cumulant statement. Untested, so not a claim.
