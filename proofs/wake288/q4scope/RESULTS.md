# Wake 288 Seed Q4 scoping: which 0-Hecke tower K_0 identities lift to module level

Scoping agent, 2026-11-10. Everything here is **computed** (mod p = 1000003, with exact relation checks for N≤4) unless it is marked otherwise. Not committed.

## Dedup
- The highest numbered question is **Q71** (Q96/Q99 are Clio-arc labels). "Q72" appears only in Dream 287 l.25, as "don't open Q72 on mirrored convention". The number is free, but that line's warning is relevant.
- No question or connection file treats Mackey, Res∘Ind, or Ind of simples at the module level.

## Step 2: obvious formulations are empty
1. **Mackey / Hopf compatibility Δ(xy)=Δx·Δy: trivially SPLIT.** At q=0 we have π_i T_w ∈ {T_{s_i w}, T_w}, which stays in the double coset W_J w W_K. So H_N = ⊕_D span{T_w : w∈D} as an (H_J,H_K)-bimodule, and Res Ind is a *direct sum* over double cosets. This is a basis-level argument, valid at any q. Computed check: for every Ind(C_I⊠C_J), N≤6, and every Res to H_{a'}⊗H_{N−a'}, no generator crosses double cosets (0 failures). Candidates (b) and (c) are dead.
2. **Shuffle product F_I·F_J: trivially FILTERED.** The span of {T_w : ℓ(w) ≥ k} is a submodule. This gives a canonical length filtration with 1-dim layers C_{Des(w)}, which is the weak-Bruhat-interval structure (JKLO 2105.14169). Candidate (a) is tautological.
3. **Projectives: trivially SPLIT.** Ind(P_I⊠P_J) = P_{I·J} ⊕ P_{I⊙J}, which is the NSym product R_I R_J = R_{I·J}+R_{I⊙J}.

## Chosen question: the simples side of R_I R_J
**Q (proposed Q72).** Let I⊨a and J⊨b, and set M_{I,J} = Ind_{H_a(0)⊗H_b(0)}^{H_{a+b}(0)}(C_I⊠C_J), whose character is F_I·F_J.
- (i) Is M_{I,J} indecomposable unless both C_I and C_J are projective (I, J ∈ {(m), (1^m)})?
- (ii) Describe End(M_{I,J}).

Why this is non-trivial:
- The projective cover of M_{I,J} is Ind(P_I⊠P_J) = P_{I·J}⊕P_{I⊙J}, which is decomposable.
- So M_{I,J} is a quotient of a 2-summand projective. Its 2-dim top C_{I·J}⊕C_{I⊙J} must be glued.
- This is the q=0 "K_0-only" phenomenon again: the identity R_I R_J = R_{I·J}+R_{I⊙J} splits on projectives, but its simple-side image F_I·F_J does not split.
- It is the Q71 pattern turned around. There, an identity held in K_0 with no filtered lift. Here, the obvious filtration exists, and the question is the splitting.

## Computed evidence (scripts `ind.py`, `modp.py`, `run.py`, `run3.py`, `frob.py`; outputs `out_*.txt`)
| N | Ind(C_I⊠C_J) not both-proj | indecomposable | bricks (End=k) | top = C_{I·J}⊕C_{I⊙J} | soc = C_{J·I}⊕C_{J⊙I} |
|---|---|---|---|---|---|
| 4 | 4 | 4 | 4 | yes (all) | yes (all) |
| 5 | 20 | 20 | 20 | yes | yes |
| 6 | 64 | 64 | 58 | yes | yes |
| 7 | 172 | 172 | 168 | n/c | n/c |
| 8 | 424 | 424 | 406 | n/c | n/c |
- Both-projective cases: always exactly 2 summands (N≤6, 31 cases), as predicted.
- "#summands" is the number of distinct eigenvalues of a generic endomorphism. Two seeds agree for N≤6.
- N=7,8 use the Frobenius-reciprocity End = {v ∈ M : π_i v = ε_i v, i≠a}.
- n/c = not computed.

**Hunch for (ii):**
- For N≤6, dim End = 1 + |{top labels} ∩ {soc labels}| holds in 88/88 cases. The extra endomorphisms are top→socle maps.
- **The formula DIES at N=7**: 14 mismatches across N=7,8. Examples: (3)⊠(2,2) has dim End 2 with overlap 0, and (2,2)⊠(2,2) has dim End 4 with overlap 2.
- So End is not just top-to-socle. Non-brick cases cluster where J ∈ {I·I', I⊙I'}-type relations hold.

Loewy data (N≤5, `run2.py`): M_{I,J} is generally **not rigid** (radical layers ≠ socle layers), and its Loewy length is shorter than the inversion grading. The length filtration is therefore not the radical filtration.

## Owner check (authors copied from arxiv.org meta tags)
- **2105.14169** (Jung, Kim, Lee, Oh): B(σ,ρ)⊠B(σ′,ρ′) ≅ B(σ∗σ′, ρ∗ρ′). §5 lists "decompose B(σ,ρ) into indecomposables" as OPEN.
- **2311.10068** (Bardwell, Searles): Prop 3.8 says B(w,v_I) and B(u_I,w) are indecomposable. It does **not** cover M_{I,J}, because M_{I,J} has a 2-dim top and a 2-dim socle, while those modules are sub/quotients of a single P_I.
- **2310.20571** (Kim, Lee, Oh): nearest neighbour.
  - Prop 7.3: a regular Schur skew-poset module whose shape contains two adjacent ribbons is decomposable, via P_α⊠P_β.
  - Conj 7.5: for disconnected shapes, indecomposable ⟺ no disconnected ribbon. Verified to |P|≤6 via End idempotents.
  - Simples C_I with I not in {(m),(1^m)} are not ribbon-shaped there, so M_{I,J} looks outside RSP_n. **This needs a careful read.**
- **2308.10456** (Choi, Kim, Oh): poset modules (DHT). Induction is a disjoint union of posets. M_{I,J} = M_{chain_I ⊔ chain_J}. I saw no indecomposability criterion for disconnected posets.
- No such statement in 1501.05250 (Huang, tableau approach), 2201.13252 (Choi, Kim, Nam, Oh), or math/0407218 (Hivert, Novelli, Thibon).
- sources.json already has 2601.13324, 2601.22926, 1211.3349, 2609.10911, 2509.26194. None of them was checked for this statement.
- **Verdict: (i) not found stated, but it sits squarely in the Oh-school programme (KLO Conj 7.5 is its sibling). The scoop risk is real.** Grade (i): computed, N≤8.
