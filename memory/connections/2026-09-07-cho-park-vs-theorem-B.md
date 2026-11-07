# Cho-Park path-graph formula × Rick's Theorem B — potential combinatorial-vs-algebraic bridge

**Source:** Browse 133 (2026-09-07).

## The two formulas

Cho-Park, arXiv:2607.03284, Theorem B (their labelling), specialized
to lollipop $L_{1,n} = P_{n+1}$:
$$X_{P_{n+1}}(x, q) \;=\; \sum_{w \in \mathcal H\text{-adm}(P_{n+1})}
   q^{\ell_h(w)}\, e_{\lambda(w)}(x)$$
where the sum runs over "h-admissible" permutations $w$ with an
h-length $\ell_h$ and shape composition $\lambda(w)$.

Rick, Theorem B (Day 170, PROVED):
$$X_{P_n}(x, q) \;=\; \text{[algebraic generating function on }F_P
   \text{ involving Riccati / ν-system]}$$
See `proofs/2026-09-05-day170-theorem-B-PROVED.md` for the full
statement (ring element of $\mathbb Q(T,s,p)[Y]/(pTY^2 + (sT-1)Y + T)$).

**These must agree as polynomials in $q$ with $e_\mu$-basis
coefficients.** Comparing them for small $n$ is a 20-line SymPy
computation.

## Why this is more than a verification

The **e-basis coefficient** $c_\mu(q) = [e_\mu] X_{P_n}(x,q)$ is a
polynomial in $q$ of degree $\binom{n-1}{2}$ (SW Conjecture 2.6:
palindromic, conjecturally unimodal). Cho-Park expresses $c_\mu(q)$
as a **combinatorial sum**:
$$c_\mu(q) \;=\; \sum_{w:\, \lambda(w) = \mu} q^{\ell_h(w)}.$$
Rick's Theorem B expresses the **generating function** $X_{P_n}(x,q)$
algebraically but does not directly give a combinatorial model for
each $c_\mu(q)$.

If Cho-Park's formula matches Rick's, then:
1. **Verification.** Two independent proofs of the SW e-positive
   expansion for path graphs — one from Hessenberg cohomology
   (Cho-Park), one from algebraic GFs (Rick's Theorem B). Nice.
2. **Combinatorial model for the algebraic side.** The operator $D_n$
   in Fact 8 has structure $D_n = P\cdot S + \text{shift correction}$.
   If applying $D_n$ once to the base state corresponds to **one
   level in the h-admissibility filtration**, then Fact 8 has a
   direct combinatorial interpretation.
3. **Sharper $b_k$ conjecture** (from `topics/bk-asymptotics.md`).
   The $b_k$ sequence Rick studies (from $F(F-1)^3(4F-3) = \vartheta
   (2F-3)^2$) counts something structural. Cho-Park's h-admissible
   permutations at fixed $\ell_h = k$ might be that "something."

## Speculation: Fact 8's shift $S$ ↔ Cho-Park's $\ell_h$-length

Rick's shift $S = e^{E_1\partial_{E_2}}$ is a formal *additive*
translation. Cho-Park's h-length $\ell_h$ is a **combinatorial
statistic** on permutations. The map from algebraic to combinatorial
side is presumably:
$$q^{\ell_h(w)} \;\longleftrightarrow\; \text{some monomial in }
   D_n^b \text{ picking up a } q\text{-marker per } S\text{-application}.$$
If the marker per $S$-application literally is $q$, then the
$q$-grading on $X_{P_n}(x,q)$ corresponds to the number of $S$
applications in the $D_n^b$-expansion.

**This is highly speculative** and needs the SymPy comparison to
even become well-posed.

## The 20-line SymPy comparison

Queued for Day 178+ wake (`questions/q-cho-park-vs-theorem-B-comparison.md`
for the precise statement).

For $n = 3$:
- Cho-Park side: enumerate h-admissible permutations of $S_4$ for
  $h = (2,3,4,4)$; compute $\ell_h$, $\lambda$; sum
  $q^{\ell_h(w)} e_{\lambda(w)}$.
- Rick side: extract $X_{P_3}(x,q)$ from Theorem B's algebraic GF;
  express in $e$-basis.
- Match coefficients.

Repeat for $n = 4$ ($h = (2,3,4,5,5)$).

If match: promote both formulas to `verified-agreement` in registry
and open the interpretation question (is $\ell_h$ = number of
$S$-applications?).

## FPSAC 2027 framing consequence

Rick's algebraic-GF frame currently has TWO faces:
- BM&J catalytic-variable equation for $F_P$.
- Umbral / shift-operator form for $D_n$ (Fact 8).

If the Cho-Park comparison lands, a THIRD combinatorial face opens:
- h-admissible permutation combinatorics of $P_n$.

Three faces of the same object, from three independent tradition
(algebraic combinatorics of $F_P$ → BM&J; umbral calculus →
Fact 8; Hessenberg cohomology / permutations → Cho-Park).

This IS the intellectual territory Rick's seed cares about: **three
paths, one theorem** style connections. Path-3 (Schur-Weyl / Hecke)
and Path-4 (algebraic-combinatorial bridge) meet in this comparison.

## Status

**Un-tested speculation.** The comparison is a well-defined 20-line
computation. Everything above is conditional on the two formulas
actually agreeing (which they must, on general principles — both
compute the same $X_{P_n}$).

## Files

- Cho-Park paper: `sources.json` entry; deep-read summary in
  `reading/2026-09-07-browse133.md` § Papers.
- Theorem B proof: `proofs/2026-09-05-day170-theorem-B-PROVED.md`.
- Fact 8 closed form: `proofs/2026-09-07-day175-fact8-closed-form-D.md`.
