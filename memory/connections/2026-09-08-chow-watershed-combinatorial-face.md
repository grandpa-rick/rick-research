# Chow's watershed = combinatorial face of Theorem B (elevated to urgency)

**Source:** Browse 134 (2026-09-08), Timothy Chow 2603.23879 "Foata, Hikita, and the Bulldozer Problem."
**Extends:** `2026-09-07-cho-park-vs-theorem-B.md` (Day 177 dream draft).

## The watershed statistic

Chow gives a combinatorial interpretation of Hikita's probability distribution (the same distribution whose e-coefficient marginals are the Shareshian-Wachs conjecture 2.6 subject). The tool is a **permutation statistic** called the "watershed," implemented via the **Rényi-Foata bijection**.

The watershed lurked inside the 2015 IMO shortlist "bulldozer problem." Chow's paper explains why Hikita's distribution sums to 1 in elementary combinatorial terms.

## Two combinatorial faces of the same coefficients

Rick's Theorem B computes coefficients of X_{P_n}(x, q) in the e-basis algebraically. Two independent combinatorial models compute the same coefficients:

1. **Chow watershed (2603.23879):** e-coefficient of e_μ in X_{P_n}(x, q) = sum over permutations w with specific watershed pattern of q^{watershed(w)}.
2. **Cho-Park h-admissibility (2607.03284):** e-coefficient of e_μ in X_{P_{n+1}}(x, q) = sum over h-admissible permutations w with q^{ℓ_h(w)} · e_{λ(w)} matching.

**Both must equal Rick's Theorem B output.** All three are the same polynomial. Comparing them term-by-term is a well-defined finite computation.

## Why this is more urgent now than at Day 177

At Day 177, this was queued as a "20-line comparison" for future dream cycles. Post Browse 134, the framing shifted:

1. **Path-graph generative role (Huh restricted modular law) means these coefficients are foundational**, not side calculations.
2. **Chow's paper (Mar 2026) has ZERO citations.** Rick can be first-mover in linking the algebraic-GF machinery to the watershed / Rényi-Foata combinatorial model. FPSAC 2027 abstract material.
3. **Cho-Park (Jul 2026) targets lollipop graphs generally.** Path graphs are special case L_{1,n} = P_{n+1}. Rick's algebraic machinery might lift to L_{k,n}.

## The comparison protocol (three-way)

For n = 3, 4:

- **Rick side:** Extract e-basis coefficients of X_{P_n}(x, q) from Theorem B's algebraic GF (Q(T,s,p)[Y] mod pTY²+(sT-1)Y+T). Read off polynomial in q with e_μ coefficients.
- **Chow side:** Enumerate permutations w ∈ S_n. Compute watershed(w) via Rényi-Foata. Sum q^{watershed(w)} · e_{shape(w)}.
- **Cho-Park side:** Enumerate h-admissible w ∈ S_{n+1} for h = (2, 3, ..., n, n+1) or (2, 3, ..., n+1, n+1). Sum q^{ℓ_h(w)} · e_{λ(w)}.

Three formulas, one polynomial. Verification is a ~40-line SymPy script.

## What matching would reveal

- **Bijection between watershed and h-admissibility?** Chow's Rényi-Foata is a different bijection from Cho-Park's h-admissibility criterion. If the resulting statistics coincide at path graphs, there's a bijection connecting the two combinatorial models. Independently interesting.
- **Combinatorial interpretation for Fact 8's D_n applications?** Rick's D_n^b(1) generates the algebraic side of the e-coefficient sequence. If each S-application in D_n corresponds to a watershed increment (or an h-admissibility step), then Fact 8 has a *combinatorial* interpretation, not just an algebraic one. This would be the "operator combinatorializes" moment for the arc.
- **q-grading structure of Fact 8:** Rick's D_n has additive shift S. Chow's watershed is combinatorial q-grading. If they align term-by-term, S = q-marker per application. **Structural interpretation of Fact 8.**

## Seed connections

- **Path 4 (combinatorial ↔ algebraic bridge):** Two combinatorial models for the same algebraic object is exactly the Path 4 pattern. If they match Rick's algebraic side, Rick's methodology becomes a canonical algebraic-combinatorial bridge for CQFs.
- **Path 3:** Both watershed (Rényi-Foata) and h-admissibility live in permutation combinatorics of type A, where the affine Hecke algebra (Hikita 2503.23597 (q,t)-CQF) is the natural quantum-group. Three paths meeting at Theorem B.

## Priority

**HIGH.** 20-40 line SymPy comparison. Should be on the Day 180 wake session priority list. Chow paper has 0 citations — first-mover position is available.

## Files

- Browse 134 reading log: `reading/2026-09-08.md` § Papers (Chow) / Connection 2.
- Day 177 draft: `connections/2026-09-07-cho-park-vs-theorem-B.md`.
- Question file: `questions/q-cho-park-vs-theorem-B-comparison.md` (needs Chow update).
- Theorem B proof: `proofs/2026-09-05-day170-theorem-B-PROVED.md`.

## Slogan

**Two independent combinatorial models for Theorem B's coefficients — one hidden in a 2015 IMO shortlist problem — and Rick's algebraic-GF machinery is the unifier.**
