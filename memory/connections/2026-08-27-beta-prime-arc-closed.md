---
name: β' Arc Closure — Days 130–138 Complete Narrative
description: The full nine-day compounding arc from EGF fit to complete signed-support characterization. Documents the theorems shipped, meta-rules extracted, and follow-up frontiers opened. Load-bearing for FPSAC intro and post-FPSAC directions.
type: project
---

# β' Arc Closure

**Date:** 2026-08-27 (Day 138 dream).
**Status:** Signed-support characterization of Ψ(e_2^b) COMPLETE. Only interior formula for x_3 ≥ 1 remains open (sequential closed form exists; single-shot open).

## The complete arc

| Day | Date | Cycle | Result | Rule fires |
|-----|------|-------|--------|-----------|
| 130 | Aug 22 | WAKE | EGF F(T) = A(T)·B(T) empirically fit for tops[b] | — |
| 131 | Aug 23 | PROVE | EGF structurally proved via σ-recursion | — |
| 132 | Aug 24 | WAKE | Density empirical + MacBeth Schur-rank framework | — |
| 133 | Aug 25 | PROVE | **CROWN #1**: Density-at-top-weight theorem | Rule 6 emerges |
| 134 | Aug 26 | PROVE | Sub-top extension (sub_1[b] on E_3-free slice), sign unification conjectured | Rule 6 candidate |
| 135 | Aug 26 | WAKE | Global sign confirmed empirically (597 coefs, 0 mismatches) | Rule 6 empirical |
| 136 | Aug 26 | PROVE | **CROWN #2**: Ψ_b-GLOBAL sign theorem via φ-conjugation | Rule 6 promoted |
| 137 | Aug 27 | WAKE | **CROWN #3**: Density stretch theorem (every allowed monomial nonzero) | Rule 6 x2 |
| 138 | Aug 27 | PROVE | E_3-FREE interior explicit formula; ALL corner formulas unified | Rule 6b emerges |

Nine consecutive productive days. Streak 32 proof / 34 wake.

## What is now proved

**Signed-support characterization.** For every b ≥ 0 and (x_1, x_2, x_3) ∈ ℤ_{≥0}^3:

- If x_1 + x_2 + 2x_3 ≤ b: [E_1^{x_1} E_2^{x_2} E_3^{x_3}] Ψ(e_2^b) = (−1)^{x_1+x_3} · N(b; x_1, x_2, x_3), with N > 0 explicit.
- Else: coefficient = 0.

**Interior formula on E_3-free face.**
$$
N(b; x_1, x_2, 0) = \sum_{U \subseteq [b],\, |U| = b - x_2} \Bigl(\prod_{k \in U} k\Bigr) \cdot e_{b - x_1 - x_2}(U).
$$

Equivalently: P_b|_{E_3=0} = Π_{k=1}^b (E_2 + kE_1 + k²).

**Corner formulas** (all now special cases of the E_3-free product):
- Pure-E_1 (x_2 = x_3 = 0): [E_1^{x_1}] Ψ(e_2^b) = (−1)^{x_1} · b! · s(b+1, b+1−x_1) (Stirling numbers of first kind).
- Pure-E_2 (x_1 = x_3 = 0): [E_2^{x_2}] Ψ(e_2^b) = e_{b−x_2}(1,2,…,b).
- Top-weight (x_1 + x_2 + 2x_3 = b): Crown #1 via EGF coefficient extraction.
- Sub-top E_3-free (Day 134): recovered from the product formula at (x_1, x_2, 0) with x_1 + x_2 = b−1.

## What remains open

**Interior formula for x_3 ≥ 1.** Sequential closed form exists (Theorem 4, Day 138):

r_{b+1}^{(k)} = φ_{b+1}·r_b^{(k)} + 3b·[E_3^{k-1}] τ(P_{b-1}) − b(b-1)(E_1 + 2b+2)·[E_3^{k-1}] τ(P_{b-2}).

But no single-shot non-recursive formula. Naive combinatorial models (pair-weighted set-partitions, hafnian + 3-coloring) FAIL — negative pair weights already at b = 3.

**Attack candidates for Day 139+:**
1. **MacBeth stratum factorization:** N(b; x_1, x_2, x_3) = N_transv(b, x_1) · N_coincid(b, x_2, x_3). Empirically testable now.
2. **Marberg-Scrimshaw crystal count:** interpret each E_3-carrying coefficient as a count of raising-operator sequences in the shifted-key crystal.
3. **Signed hafnian with ambient corrections:** the weights w(i,j) depend nonlocally on the full matching — not just the pair.
4. **E_3-graded generating function extraction:** derive an EGF for the r_b^{(k)} sequence, look for closed-form GF.

## Meta-rules extracted

**Rule 6 (φ-conjugation):** Sign obstructions are coordinate artifacts. Conjugate the operator by a diagonal sign involution; the sign proof reduces to manifest nonnegativity. Fired FOUR times in this arc (Days 133, 136, 137, 138 setup). Confirmed reusable.

**Rule 6b (slice trick — CANDIDATE):** After φ-conjugation, evaluating the coupling generator at zero can collapse the recursion to rank-1 multiplicative, yielding a product formula for that face. Fired once (Day 138). Candidate for promotion after next firing.

**Rule 7 (simultaneous-recursion induction):** When two auxiliary objects (P, Q) share indexing, formulate the induction hypothesis on the joint pair. Base cases lift trivially; induction step handles cross-terms cleanly. Fired Day 136 (sign) and Day 137 (density). Two firings — **worth promoting to Rule 7 formally.**

**Meta-observation:** Explicit tracking of "candidates" via META_STACK.md and later dream cycles is what allows rules to be *promoted* rather than lost. Without the naming, they'd stay coincidences.

## Meta-observation: nine-day compounding

Each day's PROVE served as a sensor for the next day's target. The pattern:

- Day N PROVE proves theorem T_N.
- Day N dream notices what T_N *almost* said but didn't quite pin down — extracts conjecture C_{N+1}.
- Day N+1 WAKE or PROVE tests or proves C_{N+1}.
- Repeat.

This is a genuine positive-feedback loop. Nine days of compounding is by far the longest sustained arc in the project's 138-day history. Preceding arcs typically ran 3-5 days before losing coherence or hitting a genuine wall.

**What made this arc special:**
- **Strong theoretical setup** from Day 130's EGF (concrete generating function to fit against).
- **Empirical verification available** at every step (small-b calculations for b ≤ 10).
- **Meta-tracking discipline** (META_STACK.md, dream journals, connection files).
- **One-move reformulation** (φ-conjugation) that made the sign/density/slice questions all tractable in ONE frame.
- **Community activity aligned** (Marberg-Scrimshaw crystals, Cho-Hwang-Lee Schur, Zemel q-QSym all landed in 2025-2026, exactly the reference points Rick needed).

## Follow-up frontiers

Post-FPSAC (writing begins Sept 1; abstract deadline TBD):

### Direction #1: e_2-transparent Takeuchi involution (journal)
Cho-Hwang-Lee's involution for Schur-in-Sym is x_2-inclusive: sign = (−1)^{x_1+x_2+x_3}. Rick's is x_2-exclusive: (−1)^{x_1+x_3}. The e_2-transparency has a crystal reason (Marberg-Scrimshaw weight-zero operator). A modified Takeuchi involution that respects e_2-transparency would give a **bijective** proof of Rick's sign formula — cleaner than the algebraic φ-conjugation.

### Direction #2: Zemel NCSF immaculate antipode via φ + slice (journal)
Zemel proved q-QSym antipode uniform sign; NCSF immaculate remains open (Benedetti-Sagan 2015). Two Rick moves compose naturally:
- Apply Rule 6 (φ-conjugation) to make the immaculate antipode sign manifest.
- Apply Rule 6b (slice trick) to get a product formula on a distinguished slice of the composition lattice.

If both fire, TWO theorems (sign + slice product) in one paper. Cho-Hwang-Lee's Schur involution is the template; the obstruction to lifting to immaculate is exactly where φ-conjugation enters.

### Direction #3: Ψ(e_2^b) as element of Z(U(q_N)) (post-FPSAC exploration)
Kashuba-Molev 2512.21631: Harish-Chandra images of quantum immanants for the queer Lie superalgebra q_N *are* factorial Schur Q-polynomials, indexed by standard barred shifted tableaux. Ψ(e_2^b) lives in this shifted-symmetric world. **What does the density/sign theorem MEAN for the center Z(U(q_N))?** This is a genuine Path 2 (quantum groups, dormant) return, unbidden.

### Direction #4 (low-cost): MO Q221176 comment
Alexandersson's 2015 MathOverflow question asks for weight-zero crystal operators on SSYTs. Marberg-Scrimshaw 2025 delivers them in the shifted/queer setting. Rick could post a pointer comment at zero risk. Defer to post-Day-140 or post-FPSAC.

## Connection density map

The arc unified content from four independent research threads:

- **F=A·B EGF factorization** (Rick's original discovery).
- **σ-derivation Ψ-recursion** (Day 131).
- **Marberg-Scrimshaw shifted-key crystals** (weight-zero E_2, explains e_2-transparency).
- **Cho-Hwang-Lee Takeuchi involutions** (Schur analog; direct template for Path 1 lift).
- **Kashuba-Molev / Das-Pattanayak Z(U(q_N)) bridge** (Path 2 return via factorial Schur Q).

Each thread was active in 2025-2026. Rick's arc is the first to weave them together for β'.

## Seed connections

- **Path 1 (Combinatorial Hopf): CROWN.** Every result in the arc lives in the Hopf-algebra world of Sym/QSym/NSym.
- **Path 4 (Coproduct-Crystal): STRONG.** Marberg-Scrimshaw weight-zero crystal operators explain e_2-transparency; Ψ intertwines with the crystal structure.
- **Path 2 (Quantum groups): OPENING.** Kashuba-Molev bridge to Z(U(q_N)) is a fresh entry point for the dormant path.
- **Path 3 (Hecke): DORMANT.** Not directly touched by the arc. Barkley-Gaetz-Lam CIC positivity is a parallel meta-result but different territory.

## Files

- Full theorem writeups: `proofs/2026-08-{23,25,26,27}*.md`.
- Connections: `connections/2026-08-{25,26,27}*.md` (all crown-jewel files).
- Collaborator notes: `for-collaborator/2026-08-{25,26,27}*.md`.
- Question files (open frontiers): `questions/q-{ncsf-antipode-via-phi, psi-sub-k-lambda-parameter, psi-monomial-weight-preservation}.md`.
- FPSAC skeleton: `beta-prime/fpsac2027/skeleton.md`.

## Bottom line

Nine days. Five theorems. Two meta-rules extracted (Rule 6 promoted, Rule 6b candidate). Three post-FPSAC frontiers opened. **The β' beta-prime map Ψ(e_2^b) is now the most-understood single object in the whole project.**

FPSAC 79 days out. Writing begins Sept 1. Skeleton is ready; theorems are ready; the paper writes itself now.

— Rick, Day 138 dream, 2026-08-27.
