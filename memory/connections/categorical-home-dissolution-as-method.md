---
name: When a categorical-home question dissolves into a trichotomy
description: Method observation, 2026-05-15. When stuck on "what's the algebraic / categorical home of statement X?", check whether X is trivial in the natural crystal/combinatorial framework. The deep content is usually in the realisation of operators (combinatorial structure), not their commutator algebra. The algebra-level lift may exist but be standalone (no q=0 bridge). Today's close of the on-slice commutativity home is the concrete instance.
type: project
---

# When a categorical-home question dissolves into a trichotomy

**Status:** Method observation, born 2026-05-15 from the close of "what's the categorical home of $[\tilde e_n^k, B_n] = 0$ on slice?" — three sessions of categorical-home hunting refuted, and the answer was *the question was misposed.* Worth filing because the pattern is likely to recur.

## The pattern

A "what's the categorical home of statement X?" question often splits into three statements that were *implicitly conflated*:

1. **The crystal-level statement.** Often trivial in the natural Kashiwara framework — a one-line consequence of operator definitions on $\mathfrak{sl}_2$-strings. No "home" is needed beyond the definitions.

2. **The combinatorial realisation.** The genuinely deep content. The way the operator decomposes into a catalog of concrete moves on a combinatorial object. This is where the structure lives.

3. **An algebra-level identity.** True at generic $q$, standalone. May NOT bridge to (1) via naive $q \to 0$ limit, because the algebra-level operators ($E, F, K^{-1}$) generally don't preserve the lower crystal lattice.

If (1) is trivial, **no categorical home is needed for (1).** The home you should be looking for is for (2) — the combinatorial realisation — and that home is just the relevant crystal theory (e.g., $B(\infty)$ via Kashiwara, plus whichever combinatorial bijection makes the catalog visible, e.g., CST).

The algebra-level lift (3) is a separate animal. It can be true but unbridgeable to (1) at $q = 0$, and that's fine — it lives in its own world ($\dot{\widetilde{\mathbf{U}}}^\imath$-modules at generic $q$).

## The concrete instance: on-slice coideal commutativity at split type B

Statement X: $[\tilde e_n^k, \tilde e_n + \tilde f_n] = 0$ on $\{\varepsilon_n \geq k\}$ at $B_n$ short simple.

Three sessions of categorical-home hunting refuted three candidates:
- Wang-Zhang arXiv:2508.12041 (relative braid symmetries on iquantum groups)
- Stroppel-Wang arXiv:2601.18709 (BGG for QSP coideal of gl_4)
- Chen-Lu iHopf I+II (arXiv:2511.11291 + 2601.00524)

Then Phase 1 of the algebra-side compute: $(\mathrm{ALG})$ is true (with sign correction), Phase 2 ($q = 0$ limit) FAILS, Phase 3 insight: (1) is trivial.

The trichotomy:

| Statement | Status | Where it lives |
|---|---|---|
| (1) Crystal-level $[\tilde e_n^k, \tilde e_n + \tilde f_n] = 0$ on slice | **Trivial** — one-line | Kashiwara crystal definitions |
| (2) Three-strand braid realisation of $\tilde e_n^k$ at $B_n$ short simple | **Deep**, PROVED 2026-05-15 | $B(\infty)$ via CST bracketing |
| (3) $(\mathrm{ALG})$: $[E_n^{(k)}, B_n] v_\mu = \cdots$ at generic $q$ | **True**, standalone | $\dot{\widetilde{\mathbf{U}}}^\imath$-modules |

(3) does NOT have a naive $q \to 0$ bridge to (1) because $E, F, K^{-1}$ don't preserve the lower crystal lattice. (3) ↔ (1) via canonical / i-canonical basis MAY exist (Bao-Wang i-canonical basis is the right object) but is not necessary for either statement.

## When to apply the method

When you find yourself:
- Reading papers looking for "the algebraic home for [crystal-level identity X]," and three top candidates are refuted in a row;
- Constructing increasingly elaborate $q$-deformed structures to host X;
- Suspecting the right answer is "use the right [name of currently-fashionable framework]" — iHopf, Drinfeld double, dual canonical basis;

then *first ask*: is X trivial in the natural crystal framework? If yes, the deep content is *not* the commutator identity X but the *realisation* of the operators that appear in X. Look for the catalog of moves, the combinatorial decomposition, the bracketing structure — that's where the structure lives.

The algebra-level lift is a separate question. It may have an answer, but it's not gating the deep theorem.

## Why this is non-obvious

The instinct is: "if a crystal-level identity is interesting, it must be the $q = 0$ shadow of an algebra-level identity, and that algebra-level identity has a categorical home in some QSP / iQSP / iHopf / Drinfeld-double framework." This instinct is correct in *some* cases (e.g., Kashiwara's tensor product rule is the $q = 0$ shadow of the R-matrix). But it's not universal.

The counterexample today: $[\tilde e^k, \tilde e + \tilde f] = 0$ on slice is *too trivial* to need the lift. The deep theorem is the catalog of moves, which is purely combinatorial-crystal content.

## Connection to the calibration corpus

This is the structural realisation of two earlier calibration items:
- "When literature search keeps coming up empty, the next move is to compute the conjectured mechanism algebraically rather than read another paper" (browse-6 → wake calibration).
- "Closing a question by showing it doesn't need new machinery is a result, not a failure" (prove-cycle-2 close).

Both calibrations were operational. This connection promotes them from "calibration items" to a **named method**: the categorical-home dissolution.

## Falsifiability / when this method fails

The method's "first ask" is "is X trivial in the natural framework?" — but you have to know what the natural framework is. For statements that look crystal-level but are actually about *non-crystal* phenomena (e.g., positivity at intermediate $q$, structure of canonical basis transition matrices, dual cells), the natural framework is *not* Kashiwara crystals and the method gives no answer.

The method works specifically for statements like "operator $A$ commutes with operator $B$ on a crystal slice." It does not apply to statements about (q,t)-Lusztig polynomials, KL positivity, or BGG resolutions (which have genuine homological content).

## What this gives the program

- **One more arrow in the quiver** for closing "categorical home" questions. Today's close is reproducible.
- **A clean framing for v2 / future papers.** "The three-strand braid realisation of $\tilde e_n^k$ is the deep theorem; the commutativity is a one-line consequence; the algebra-level lift $(\mathrm{ALG})$ is standalone." This frames the v2 contribution precisely.
- **A way to STOP chasing categorical homes when the underlying object is trivial.** Today saved Rick from a fourth refuted iHopf hunt.

## Cross-references

- `connections/algebraic-home-and-crystal-home-are-independent.md` — the today-specific closure note.
- `for-collaborator/2026-05-15-categorical-home-closed-and-not.md` — what to tell Robin.
- `proofs/2026-05-15-algebraic-mechanism-Bn.md` — full writeup of $(\mathrm{ALG})$ + closure.
- `proofs/2026-05-15-three-strand-braid-Bn.md` — the deep theorem (combinatorial realisation).
- `connections/multiorbit-catalog-as-three-strand-braid.md` — the catalog whose realisation is the deep content.
