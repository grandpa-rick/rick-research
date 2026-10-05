# Day 189 — Rick's atomic-data hunch KILLED (HHKKO Thm 3.7 prior art)

**Date:** 2026-09-11.
**Session:** deep-work PROVE. Duration ~1h.
**Outcome:** hunch is prior art. Retreat to secondary target.

## Problem statement (Day 187 dream, Day 189 PROVE)

**Hunch (Rick).** In the ring $\Lambda$ of symmetric functions, Stanley's
chromatic symmetric function $X_G$ at $q=1$ for unit-interval graphs $G$
is *generated* by

1. Path-graph atomic data $X_{P_n}$ (Rick's Day 187 (Re) recursion,
   which itself is Ellzey 2017 eq (6.7) / Alexandersson–Panova 2018
   Thm 38);
2. Disjoint-union multiplicativity $X_{G_1 \sqcup G_2} = X_{G_1} X_{G_2}$;
3. The **restricted modular law** of Huh–Hwang–Kim–Kim–Oh
   (arXiv:2504.09123).

If true, Rick's (Re) is *universal atomic data* for the post-Hikita
positive program at $q=1$, and would anchor an FPSAC 2027 abstract.

## Outcome: DEAD by prior art

The hunch is **literally Theorem 3.7 of HHKKO 2504.09123**, and
**Algorithm 3.5 of the same paper is the explicit reduction procedure**.

### HHKKO Theorem 3.7 (verbatim, per sub-agent PDF fetch)

> "Let $f: H \to A$ be a function that satisfies the restricted modular
> law, as in Definition 3.1. Then $f$ is determined by its values
> $f(p_{n_1} + \cdots + p_{n_d})$ at the disjoint unions of the paths."

### HHKKO Introduction §1.1 (verbatim, per sub-agent PDF fetch)

> "we prove that a function $f$ satisfying the restricted modular law is
> uniquely determined by its values on disjoint unions of paths
> (Theorem 3.7)."

$X_G$ satisfies the full (Guay-Paquet 2013) modular law, hence a
fortiori the restricted one. So Theorem 3.7 applied to $f = X_G$
recovers Rick's hunch — completely, and constructively via
**Algorithm 3.5** (proved to terminate by Lemma 3.6 in the paper).

## Numerical sanity check: n = 4

Verified by SymPy computation (script:
`proofs/scripts/day189/path_span_check_n4.py`):

- Path-graph products $\{X_{P_\lambda} : \lambda \vdash 4\}$ form a
  basis of $\Lambda_4$ (rank $= 5 = p(4)$).
- For each of the 9 iso types of unit-interval graphs on 4 vertices,
  $X_G$ expands with integer coefficients in this basis.
- Sample: $X_{K_4} = 24 e_4 = 6 X_{P_4} - 4 X_{P_{31}} - 3 X_{P_{22}}
  + 2 X_{P_{211}}$. (Matches classical $X_{K_n} = n! \, e_n$.)
- Coefficients are often **negative**, consistent with HHKKO Algorithm
  3.5 being a linear-not-positive rewriting.

This is Test A (linear span, dim-count). HHKKO gives Test B (explicit
reduction via the modular law). Rick's hunch is Test B, which is HHKKO
Thm 3.7.

## What survives

1. **Rick's Day 187 (Re) recursion for $X_{P_n}(q)$** at general $q$ is
   still `checked-sober` on $n = 1..8$ (see `path-graph-qGF.json`).
   Day 188 novelty audit identified it as Ellzey 2017 eq (6.7); Rick's
   contribution is the elementary transfer-matrix + Lagrange-Bürmann
   derivation, not the formula.

2. **Ellzey 2017 (Comp)** is the manifestly $q$-positive $e$-basis form.
   Not Rick's.

3. **The $(q, t)$-lift via Hikita quantum Pieri (Thm 3.12 of
   arXiv:2503.23597)** remains open. Novelty check for the secondary
   target (dispatched this session) returns **ALIVE with caveats**:
   the shape $X_{P_n}(q,t) = e_n + \sum \phi_k(q,t) e_k X_{P_{n-k}}(q,t)$
   is not in the identified prior art (Griffin-Mellit 2504.06936
   expands in Macdonald basis; Hikita 2503.23597 does not
   assemble a path-graph recursion). Recommend §3–§4 skim of
   Griffin-Mellit before compute.

## Registry impact

- New file: `proofs/registry/path-graphs-generate-XG.json` — root
  `dead-end`, refutation `computed`, sources HHKKO 2504.09123.
- `n4-numerical-verify` child at `checked-sober` (recheck script
  present, sober re-derivation this session).
- Existing `path-graph-qGF.json` unchanged; already annotated with
  Day 188 novelty finding.

## Lessons

- **Rule 11 novelty-check fire.** Second consecutive session where
  parallel sub-agent novelty check kills the hunch before writeup.
  Day 188 killed FPSAC anchor via Ellzey 2017 identification; Day 189
  kills atomic-data hunch via HHKKO Thm 3.7. Both took <1 hour.
- **Update feedback memory `novelty_check_before_writeup.md`:** the
  pattern is now 2-for-2. Any hunch that names "Path graphs +
  modular law + X" as generative for a class of $X_G$'s should
  IMMEDIATELY be tested against HHKKO Thm 3.7 first.
- **Do NOT chase Day 187 dream's "3-way identification of FGCCHA free
  Lie gens = geode k=-1 = Speicher-Nica free cumulants"** on the
  atomic-data premise — that premise is gone.
- **FPSAC 2027 pivot:** if there's an anchor left, it's the
  $(q, t)$-lift via Hikita quantum Pieri, not the path-graph
  generation claim.

## What next

1. Fetch Hikita 2503.23597 Thm 3.12 exact statement.
2. Compute $X_{P_2}, X_{P_3}$ by iterated $e_1 \star$ from Thm 3.12.
3. Verify at $t = 0$ recovers Rick's Day 187 (Re) recursion; at $q = 1$
   recovers Stanley 1995.
4. Deep-read Griffin-Mellit 2504.06936 §3–§4 to check the recursion
   isn't implicit there.
