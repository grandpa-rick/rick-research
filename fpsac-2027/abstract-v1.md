# FPSAC 2027 Abstract — outline (v1)

**Title (working):** *A manifestly q-positive compositional formula for the chromatic quasisymmetric function of the path graph*

**Alternate titles considered:**
- *The path-graph chromatic quasisymmetric function: a closed q-positive expansion*
- *A generating function identity for X_{P_n}(q) and a compositional e-positive formula*

## Top-of-document abstract (target 300-400 words)

We give three equivalent proved forms for the Ellzey-Wachs / Shareshian-Wachs
chromatic quasisymmetric function X_{P_n}(q) of the path graph P_n:

- A generating function identity F(z)[E(qz) - qE(z)] = (1-q)E(z);
- A positive e-basis recursion X_{P_n}(q) = e_n + q sum_{k=2}^n [k-1]_q e_k X_{P_{n-k}}(q);
- A closed compositional formula X_{P_n}(q) = sum over compositions (k_1,...,k_r) vDash n
  with k_i >= 2 for i < r of q^{r-1} [k_r]_q prod_{i<r} [k_i-1]_q  e_{k_1}...e_{k_r}.

The compositional formula is manifestly q-positive in the elementary basis
and gives a fully explicit e-expansion for the entire family of path graphs,
sharpening (for this specific family) the general q-positivity theorems of
Ellzey-Wachs and complementing Hikita's recent quantum-Pieri stochastic
interpretation. We recover Stanley's 1995 GF for X_{P_n} at q=1 and the
descending-coloring identity X_{P_n}(0) = e_n at q=0.

We sketch two proofs of equivalence between the three forms
(algebraic Lagrange-style unfolding), verify checked-sober agreement on
n = 1..8, and match Hikita's Markov chain on n = 1..6. We discuss the
role of the path graph as generative set for e-positivity under
disjoint union and the restricted modular law
(Huh-Hwang-Kim-Kim-Oh, 2025), and pose the conjecture that (Comp) is
the "universal atomic data" from which the entire post-Stanley-Gasharov
positive program can be assembled.

## Introduction outline (~1.5 pp)

- Motivation: Stanley 1995 / Stanley-Stembridge 1993; e-positivity conjecture
  for unit interval graphs; state of the art post-Matherne-Morales /
  Wang-Zhang-Zhao disproof of Stanley-Gasharov (2026).
- q-refinement: Shareshian-Wachs 2016 chromatic quasisymmetric functions;
  Ellzey-Wachs e-positivity for path graphs via P-tableaux.
- Rick's contribution: three equivalent closed forms for X_{P_n}(q),
  culminating in a manifestly q-positive compositional formula (Comp)
  that admits no known analogue in the literature. Verified checked-sober
  through n = 8; matches Hikita Markov chain through n = 6.
- Structural payoff: (Re) is the simplest possible q-lift of the
  Stanley 1995 GF and slots directly into the disjoint-union structure;
  path graphs generate under restricted modular law
  (Huh-Hwang-Kim-Kim-Oh 2504.09123), so (Re) is a candidate universal
  atomic data.
- Roadmap.

## Section outline for the 12-page extended abstract

1. **Introduction** (1.5 pp)
2. **Background** (1 pp) — Stanley CSF; Shareshian-Wachs CQF;
   Ellzey-Wachs q-positivity; disjoint union + restricted modular law.
3. **Main theorem** (1 pp) — statement of the three equivalent forms
   with a worked example at n = 4.
4. **Proof of equivalence** (3 pp) — (R) => (GF) via H(-z) = 1/E(z) and
   [k+1]_q = (1 - q^{k+1})/(1 - q); (GF) => (Re) by extracting z^n;
   (Re) => (Comp) by iteration.
5. **Verification / examples** (1.5 pp) — n = 1..4 tables of coefficients;
   q = 0 and q = 1 sanity checks; disjoint-union check
   X_{K_2 sqcup P_2}(q) = X_{P_2}(q)^2.
6. **Comparison with the literature** (1 pp) — Ellzey P-tableau formula;
   Alexandersson-Sulzgruber / Alexandersson-Panova composition method;
   Hikita quantum Pieri and Markov chain identification (Route A verification).
7. **The universal-atomic-data hunch** (1 pp) —
   restricted modular law + path-graph generative set (Huh et al. 2504.09123);
   (Re) as candidate atomic data for the post-Stanley-Gasharov
   positive program.
8. **Open questions and future work** (1 pp) — combinatorial / bijective
   proof of (Comp); (q,t)-lift via Hikita Pieri; extension beyond path graphs.
9. **References** (~30 items).

## Beliefs to verify before v2 (Rick's action items)

- Verify (Comp) is not implicit in
  Ellzey (arXiv:1709.00454) or Ellzey PhD thesis (P-tableau formula for P_n).
- Verify (Comp) is not implicit in the
  Alexandersson-Sulzgruber composition method (SD Adv. in Appl. Math. 2025).
- Verify (Re) does NOT appear in Athanasiadis Powersum-in-e / Guay-Paquet CQF work.
- Decide title.
- Decide whether Section 7 (universal atomic data hunch) belongs
  in the FPSAC abstract or should be deferred to the full journal paper
  (FPSAC audience is friendly to hunches labeled as such).
- Decide whether to include a proof-sketch of Route A Markov-chain match
  or defer to the journal version.

## Prior-art check (this session, ~15 min)

- Ellzey (arXiv:1709.00454, 2017) gives a generating function for the
  e-basis expansion of the directed CYCLE, NOT the undirected path
  graph P_n in the closed compositional form (Comp).
- Ellzey's thesis / arXiv (P-tableau formula) gives an e-positive
  expansion for path graphs but as a sum over P-tableaux, not as the
  closed composition sum (Comp).
- Alexandersson-Sulzgruber "composition method" (Adv. Appl. Math. 2025)
  is a general framework; it may specialize to (Comp) for P_n but Rick
  believes not identically. Requires careful comparison for v2.
- No search hit gives (Comp) verbatim. Novelty holds pending v2 verification.
