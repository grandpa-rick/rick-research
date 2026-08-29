# Novelty Audit Round 2 — Identity (♣)

**Date:** 2026-07-16
**Identity under audit:**
```
β(c) − LB_1(c) = s_2(c−1) + v_2(c−1) − v_2(c)     (♣)
```
where β(c) = 2(c−1) − s_2(c−1) is Legendre's formula for v_2((c−1)!),
and LB_1(c) := v_2((2)_{c−2}) = v_2(2·3·…·(c−1)) is the 2-adic valuation
of the ascending Pochhammer starting at 2.

## Search methodology

Both `mcp__research__search_papers` (Semantic Scholar: HTTP 429 throughout)
and `mcp__research__arxiv_search` (broken by an unfollowed 301 redirect) were
non-functional during this session. Fell back to `WebFetch` against arXiv
listings and Google Scholar.

Angles queried:
1. Author sweep — Dirk (Stefan A. G.) De Wannemacker (full arXiv author list).
2. Amdeberhan / Manna / Moll on 2-adic valuation.
3. Zhi-Wei Sun on 2-adic / p-adic valuation.
4. Sun-Moll joint work on p-adic valuation.
5. Boros-Moll on 2-adic factorial identities.
6. Direct term search: "Pochhammer" + "2-adic", "rising factorial" + "2-adic".
7. Direct term search: `v_2` + Pochhammer + `s_2` (Google Scholar, 6 hits total).
8. Direct term search: `v_2((a)_k)` / `v_2((2)_n)` (Google Scholar).

## Candidate papers surfaced (≈8 distinct)

| # | Paper | arXiv id | Verdict |
|---|-------|----------|---------|
| 1 | S.A.G. De Wannemacker, *Annihilating polynomials for quadratic forms and Stirling numbers of the second kind*, 2007 | math/0702817 | **Does not match.** Gives a **new lower bound on v_2(S(n,k))** for Stirling numbers of the 2nd kind. Not Pochhammer, no s_2+v_2−v_2 identity. |
| 2 | Amdeberhan, Manna, Moll, *The 2-adic valuations of Stirling numbers*, 2007 | 0707.3104 | **Does not match.** Conjectural periodicity of v_2(S(n,k)) mod 2^r. Stirling, not Pochhammer. |
| 3 | Amdeberhan, Manna, Moll, *The 2-adic valuation of a sequence arising from a rational integral*, 2007 | 0707.2119 | **Does not match.** (Confirmed again — already checked Day 97.) |
| 4 | Beyerstedt, Moll, Sun, *The p-adic valuation of ASM numbers* (and companion *An analytic formula …*), J. Integer Seq. 2011 | — | **Does not match.** ASM counting function T(N); uses periodic sums (à la Legendre) but no Pochhammer, no LB_1 analogue. |
| 5 | Heuberger, Prodinger, *A precise description of the p-adic valuation of the number of ASM*, 2009 | 0908.0149 | **Does not match.** Same ASM setting; Mellin-Perron / digit-sum fluctuations for v_p(T(N)). |
| 6 | D. Villamizar, *Combinatorial and arithmetical properties of families of sequences*, ProQuest 2021 | — (thesis) | **Does not match.** Studies v_2 of B_{n,≥2}-type numbers via Stirling-of-1st-kind coefficients of the rising factorial polynomial — related terrain, but no formula matching (♣). |
| 7 | Kim et al., *Degenerate & zero-truncated degenerate Poisson r.v.'s*, 2021 | 2106.13481 | **Does not match.** Rising factorial moments in probability; not number-theoretic v_2. |
| 8 | De Wannemacker's other papers (1602.04675, 1407.4288, 1103.2877, math/0701830, math/0608085) | various | **Do not match.** Antichains / Dedekind / Witt-ring structure — no 2-adic Pochhammer content. |

## Notable dead ends

- Google Scholar for `"v_2" "Pochhammer" "s_2"` returned **6 total results**, none containing the identity (top hits were Nerattini-Brauchart-Kiessling on sphere configurations, Borodin-Corwin Macdonald processes, Belousov et al. on Baxter operators — all unrelated).
- Google Scholar for `"Boros" "Moll" "2-adic" factorial` — **zero results**.
- Google Scholar for `"v_2((a)_k)"` / `"v_2((2)_n)"` — no matching-formula papers.
- arXiv full-text `"Pochhammer 2-adic valuation"` — no results.
- Direct verification that De Wannemacker's Pochhammer-facing work is nil: his six-paper arXiv corpus concerns Stirling-of-2nd-kind bounds and antichain combinatorics only.

## Verdict

Across two independent audit rounds (Day 97 + today) covering the four
research programmes that could plausibly host (♣) — De Wannemacker (Stirling
2-adic bounds), Amdeberhan-Moll-Manna (2-adic factorial/Stirling sequences),
Sun-Moll (p-adic valuation of combinatorial numbers), and Boros-Moll
(hypergeometric integrals) — **the identity**
```
β(c) − v_2((2)_{c−2}) = s_2(c−1) + v_2(c−1) − v_2(c)
```
**was not located.** The `s_2 + v_2 − v_2` combination on the RHS, and in
particular its identification with the "Legendre−LB_1" defect, does not
appear.

**Recommendation:** upgrade status to
`novelty-original-pending-final-audit`.

Residual risk: (a) the identity may sit in an older unindexed paper (Kummer
1852, Legendre 1830, or a Ribenboim/Granville expository); (b) it may be
implicit as a two-line calculation in a textbook (Robert's *Course in
p-adic Analysis*, Koblitz, Amdeberhan-Moll monograph chapter). A tertiary
check against those printed sources is worthwhile before final publication,
but no online arXiv/Scholar hit exists.
