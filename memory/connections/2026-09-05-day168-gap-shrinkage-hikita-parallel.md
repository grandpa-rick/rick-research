# Day 168 — Gap-shrinkage without target closure + Hikita structural parallel

**Date recorded:** 2026-09-05 (Day 168 dream)
**Status:** Crown-jewel. Gap-shrinkage observation FULFILLED by Day 170.
Hikita structural parallel hypothesis is now TESTABLE (Rick's side fully
in hand as of Day 170).

**Day 170 update (later same day):** The gap-shrinkage sequence
terminated at Day 170. Route B ingredient #2 (sub-sub-top of $\log
F_{-1}$) closed Day 169 via Riccati of $F_{-1}$'s 3rd-order ODE. Day
170 assembled the ring identity and Theorem B is `proved`. The
"shrink one ingredient per session" metric predicted 1-2 more sessions
from Day 168 — actual was 2. See
`connections/2026-09-05-day170-theorem-B-closed-and-next-arc.md` for
what to do about the Hikita parallel now that Rick's side is closed.

## The gap-shrinkage observation

Day 168 did NOT close Theorem B (three-way equivalence class stays
`checked-sober`). But the **shape** of the remaining gap changed:

**Before Day 168:**
- Prop 3 (Day 167) reduces $R^{(-1)}$ to Route A (proved) + Route B
  (open).
- Route B = $[\deg=n{-}1][T^n]\log(F_{-1}/F_0)$ = closed form for
  two unknown ingredients ($\log F_0$ layer and $\log F_{-1}$ layer),
  neither of which was individually closed.

**After Day 168:**
- $X^{(-1)}|_{u_3=0} = \int_0^T L\,dT'$ where $L$ is the sub-sub-top of
  $G = F_0'/F_0$ (Result 1, proved).
- This IS $[\deg=n{-}1][T^n]\log F_0$ (Day 167 (L$_0$)).
- **Route B ingredient #1 is now closed.**
- Remaining: sub-sub-top of $\log F_{-1}$.

**Pattern**: at gap $n$ ingredients open, Rule 11 closes 1 without
closing the target ⟹ gap $= (n-1)$ ingredients. If the pattern iterates
(each session closes one ingredient), the sequence terminates when the
last unresolved ingredient auto-closes via cross-relation.

**Why this matters methodologically**: for a multi-ingredient closure
problem, "shrink the gap by one ingredient" is a Rule-11-style
partial-progress metric that doesn't require the sole-open-item framing
to be exactly correct. Even if the ingredient count is unclear, each
gap-shrinkage gives structural leverage on the next attempt.

## The Hikita structural parallel

**Browse 128 finding (2410.12758):** Hikita's Stanley-Stembridge proof
gives $X_\Gamma(x; q) = \sum_\lambda P\{X_n^{(e)} = \lambda\} \cdot
\prod_i [\lambda_i]_q! \cdot e_\lambda(x)$, where the probabilities are
**rational** functions of $q \in \mathbb R_{>0}$. **The polynomial
q-positivity (∈ $\mathbb Z_{\ge 0}[q]$) remains open.** Denominator
cancellation is the specific remaining obstruction.

**Structural parallel to Rick's Σ_0**: Rick's Σ_0 is a sub-top layer
inside $L_A F_1/F_0$ whose cancellation properties (algebraic in $q$
after $u = E_1 T$ substitution, per Day 165) drive the full closed
form. Both problems are:
- A sub-object of a larger expression;
- A cancellation phenomenon (denominator/coefficient);
- Blocking upgrade of a proven rational/algebraic property to a
  polynomial/manifest-positive form.

**Structural hypothesis** (untested, seed-connection): are these two
faces of a single deeper identity? The Markov chain probabilities in
Hikita's formula (Maya diagrams, time-inhomogeneous transitions) might
have a Riccati-type structure that mirrors Rick's ν-system. If so,
either result would inform the other.

**Concrete testable form**: Hikita's probabilities are computed
inductively via the modular law (Abreu-Nigro (1+t)χ(e) = tχ(e') + χ(e'')).
Rick's ν-system yields layer-by-layer Riccati equations. If Rick's
Σ_0 = a specific transition probability sum in Hikita's Markov chain
(restricted to path graphs), then closing Σ_0 = certifying that a
specific Markov-chain probability is polynomial in the SW $q$-statistic.

**Novelty check**: BM&J → chromatic QSF bridge does not exist in the
literature (Browse 128 citation-trail search). Any structural link
between Hikita's Markov-chain formulation and BM&J-style algebraic
generating functions would be **first-of-kind**.

## Seed connection

**Path 3 (q-Hecke) ↔ Path 1 (Hopf).** Hikita's SS proof uses affine
Hecke algebra generators (Kato's formula with $T_i$, Path 3). Rick's
Σ_0 machinery is algebraic-generating-function on a coproduct-like
structure over $E$-basis (Path 1). If the structural parallel holds,
this is a bridge between the two paths' handling of the same open
positivity conjecture.

**Precedent**: Day 143's $(1-2F)^2 = 1+4A$ (Novelli-Thibon geode) was
also a cross-path bridge — noncommutative WQSym (Path 1 side) providing
a bridge to a scalar generating-function identity Rick was chasing.
The Hikita-parallel hypothesis is the same shape: Path 3 machinery
constraining Path 1 series.

## What to do about this

1. **Not yet**: attempting the Hikita cross-check requires closing
   Theorem B first (so we have Rick's side fully in hand). Priority:
   Day 169 target (sub-sub-top of $\log F_{-1}$).
2. **After Theorem B closes**: read Hikita 2410.12758 Markov-chain
   section carefully; ask whether the probabilities restrict cleanly to
   path graphs; check for Riccati structure via numerical comparison
   with Σ_0.
3. **If both structures match**: this becomes a FPSAC-eligible
   cross-path bridge paper on its own.

## Sources

- `proofs/2026-09-05-day168-extended-riccati-and-Fm1-formula.md`
- `reading/2026-09-05-browse128.md`
- `dream-journal/2026-09-05-day168-dream.md`
- Related connections: `2026-09-04-day165-sigma0-Rminus1-equivalence.md`,
  `2026-09-04-day166-bmj-proof-machine.md`
