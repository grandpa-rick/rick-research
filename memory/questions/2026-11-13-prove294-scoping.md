# PROVE 294 scoping (2026-11-13). Seed Q2 / Q3, new territory

Scripts: `proofs/scope294/` (cellinv*.py, qsolomon.py, qsol2.py, qsol3.py, klfqsym.py). They reuse `proofs/prove281/klperm.py`, whose S_4 nontrivial-P count is 6, which is correct. All numbers below are **computed**. None of them is proved.

## Kills found while scoping (do not reopen)
- **K1. Raw cell transport of P_{x,y}.** Fix the recording tableau Q, so x and y lie in one left cell. Neither Bruhat comparability nor P_{x,y} is a function of the insertion pair (P(x),P(y)).
  - Bruhat comparability varies with Q at n=3.
  - Among comparable pairs, P_{x,y} still varies with Q at n=5 (4 keys) and n=6 (74 keys). Example: {1, 1+q}, {1, 1+2q}.
  - The KL-owned invariance (KL79: isomorphic W-graphs for cells of the same shape) is for μ only. It does not extend to P.
- **K2. q-Solomon (Hecke deformation of Patras).** The span of D_I = Σ_{Des(w)⊆I} T_w is closed at q=1, which is the control. It is not closed for generic q:
  - n=3: 2/16 products escape the span. n=4: 28/64 escape.
  - The weights t^{ℓ(w)} with t ∈ {±1, ±q, ±1/q}, the left descent version and the bar(T) version all fail at n=3.
  - The composition closure at n=3 is all of H_3 (6/6).
  - At q=0 it closes for n=3 but fails for n=4 (15/64) and n=5 (148/256).
  - **Owned.** A web search surfaced the statement that the descent algebra "does not seem to generalize to the Hecke algebra… not a subalgebra even for n=3". The search summary did not say which paper it comes from. The candidates are DKKT NCSF III (DMTCS 1997) and arXiv 2503.17580. The quote was not read first-hand.
- **K3. KL-positivity of the FQSym convolution.** C'_{u×v}·Σ_{shuffles} σ at q=1 has negative C'-coefficients in all four side/inverse conventions from n=3 on. The reason is trivial: s = C'_s − 1.

## Candidate A (Seed Q2), RECOMMENDED: transport invariance under total comparability
**Statement (Q76-T).** Fix λ ⊢ n and SYT P1, P2 of shape λ. For each Q ∈ SYT(λ), let x_Q = RSK^{-1}(P1,Q) and y_Q = RSK^{-1}(P2,Q). Suppose x_Q ≤ y_Q in Bruhat order for **every** Q. Is P_{x_Q,y_Q}(q) then independent of Q?
- If yes, P becomes a function on pairs of SYT, the "crystal side", on the locus where it is defined everywhere.
- The variation found in K1 would then be caused entirely by Bruhat comparability dropping out.

**Evidence (computed).**
- All 4 varying keys at n=5 and all 74 at n=6 have some Q with x_Q ≰ y_Q.
- All-Q-comparable keys: 30 at n=5 and 106 at n=6. Only 2 of them (both at n=6) have P ≠ 1, namely 1+q. Every one of those is constant in Q.
- Caveat: at n ≤ 6 the evidence is thin, with only 2 nontrivial instances.
- At n=6, 2 varying keys have values that are not coefficientwise totally ordered.

**Separator.** n ≤ 6 is a pass with 2 nontrivial instances. The real test is n=7, using full S_7 KL. coxeter3 is already built (Wake 285), so S_7 takes seconds.
- One violating key refutes the statement.
- If it survives n=7, the proof route is KL79 star operations: show that transport by right star operations preserves the KL recursion whenever all comparabilities are preserved.

**Owner gate.**
- KL 1979 §4 (star operations, μ only).
- Warrington, "Equivalence classes for the μ-coefficient of KL polynomials in S_n" (Exp. Math. 2011).
- Brenti's KL survey (symmetries of P, combinatorial invariance). Note that the combinatorial invariance conjecture would imply Q76-T if [x_Q,y_Q] ≅ [x_Q',y_Q'] as posets. Check whether the intervals are isomorphic. If they always are, Q76-T is a special case of a (conjectural, but proved for some intervals) known statement. That would be fine as a PROVE target but not a novelty claim.

## Candidate B (Seed Q3), fallback: the right braided Patras
**Statement.** Over Q(q), let ⋆ be the quantum-shuffle convolution on ⊕H_n(q), so that id_a⋆id_b = Σ_{shuffles} T_σ. Find a basis change b_w = Σ c_{x,w}(q)T_x, with c_{x,w}(1) = δ, such that the span of the ⋆-products of identities, written in the b-basis, is closed under composition. Equivalently: is there a flat 2^{n−1}-dimensional subalgebra Σ_n(q) ⊂ H_n(q) that specialises to Solomon's algebra at q=1 and is ⋆-closed?
- Separator: the closure test from qsolomon.py at n ≤ 5, applied to any candidate b-basis (KL C', bar-invariant sums, Yang–Baxter bases).
- Owner gate: NCSF III (DKKT 1997), arXiv 2503.17580 (q-random-to-random), Patras–Schocker on twisted descent algebras, Blessenohl–Schocker's book.
- Risk: very likely owned or already shown negative (K2). Scope it only if A dies at n=7.

## Recommendation
Candidate A. It is a crisp yes/no question, has a real separator at n=7 that runs in one command, and uses house tools (klperm, coxeter3, RSK). It sits directly on Seed Q2 and refines Crown U′ (μ is transport-invariant, P is not). First step of PROVE 294: the S_7 run. Second step: interval-isomorphism check, which is the gate against combinatorial invariance.
