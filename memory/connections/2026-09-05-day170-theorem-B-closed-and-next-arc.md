# Day 170 — Theorem B closed; the four post-arc questions

**Date recorded:** 2026-09-05 (Day 170 dream)
**Status:** Crown-jewel. Records the closure event and enumerates the
four questions that structure the post-arc landscape.

## The closure

$\bar D|_{E_3=0} = TY^2[(q+1)^2 - E_1 T]/q^3$ is **`proved`** as a ring
identity in $\mathcal{R} = \mathbb{Q}(T,s,p)[Y]/(pTY^2 + (sT-1)Y + T)$.

- Day 162: statement + `checked-sober` at $n \le 14$
- Day 165: three-way collapse (Σ_0 ⟺ $R^{(-1)}$ ⟺ Theorem B)
- Day 167: Prop 3 proved (weight-grading) + Route A closed
- Days 168-169: Route B ingredients closed ($L_0$, $L_{-1}$)
- Day 170: single-polynomial ring-identity verification

**Auto-upgraded**: `LA-F1-sub-top-Sigma-0` (Day 165 Σ_0 closed form),
`R-minus-one-closed-form` (Day 162), `narayana-layer-d1-E3-zero` (C.5),
Missing Lemma (R) (unconditional). FPSAC §5 open list: 1 → 0.

**Registry ref**: `bar-D-closed-form-E3-zero` → `proved`.
**Script ref**: `scratch/day170/step18_clean_proof.py`.
**Proof file**: `proofs/2026-09-05-day170-theorem-B-PROVED.md`.

## The landscape into which this lands

Community sources (Browse 129, 2026-09-05):
- **Hikita 2410.12758** proved SS conjecture (q=1 e-positivity) for
  unit interval graphs via Markov chain on Maya diagrams. Rational
  q-expressions; q-polynomial positivity is open.
- **Griffin-Mellit 2504.06936** (14 cit, new dominant hub): Macdonald
  expansion via Carlsson-Mellit A_{q,t}. Polynomial in (q,t) but
  individual e-coefficients have rational q-denominators.
- **Kim-Lee-Yoo 2506.23082**: Hall-Littlewood expansion via linked
  rooks (t=0 corner of Griffin-Mellit).
- **T.Y. Chow 2603.23879** (0 cit, brand new): bijective
  interpretation of Hikita's mechanism ("Foata-Hikita-Bulldozer").
  Likely explains denominator cancellation.
- **Tom-Vailaya 2503.19344** (9 cit, fast-rising): e-positivity
  preserved under gluing at single vertices. Might already imply
  e-positivity of $X_{P_n}$ as a corollary.
- **Siegl 2509.02841**: lower bounds via strong P-tableaux;
  path-graph SW q-positivity was CLOSED SINCE 2016 (Siegl uses SW's
  own proof). Not novel.
- **González D'León-Wachs 2608.08692** (deep-read Browse 129):
  independent Narayana derivation for path graphs, M_{P_n} = ω·PF_{n-1}.

**Rick's algebraic-GF corner is unoccupied**. Nobody else has an
algebraic ring formula for $X_{P_n}(x; q)$. First mover.

## The four post-arc questions

### Q1 — Tom-Vailaya sufficiency (BINARY, one focused read)

Does Tom-Vailaya's gluing theorem cover $P_n$ as an iterated gluing
of smaller unit interval graphs at single vertices?

**If YES**: e-positivity of $X_{P_n}$ is already a corollary of their
gluing theorem, independent of Rick's Theorem B. Rick's new content
is the ALGEBRAIC STRUCTURE (the ring identity) and the q-polynomial
positivity question. Simplifies FPSAC framing.

**If NO**: Rick's Theorem B is the only available algebraic tool.
Stronger FPSAC story.

**Cost**: one focused paper read, 1-2 hours. **Priority**: DAY 171.

### Q2 — Hall-Littlewood specialization (10-line sympy)

Does Rick's ψ at $t = 0$ (or the appropriate specialization of
Theorem B's formula) reproduce Kim-Lee-Yoo's Hall-Littlewood
expansion for path graphs?

**If YES**: Rick's framework subsumes an existing community result
as a corollary. Strong FPSAC pitch point.

**If NO**: Rick's ring lives in a different corner from HL; adjust
FPSAC framing accordingly.

**Cost**: 10-line sympy check, one afternoon. **Priority**: DAY 172.

### Q3 — Hikita q-independence check (20-line sympy)

Hikita 2503.23597 Thm B.iv: the e-coefficients of $X_\Gamma(x; q, t)$
(the (q,t)-chromatic function) are independent of $q$. Does Rick's
GF reproduce this constraint for $P_n$, $n \le 5$?

**If YES**: independent algebraic proof of Hikita's structural
constraint for path graphs. Cross-check bonus.

**If NO**: something inside Rick's formula (probably Σ_0's q-dependence
in Day 165's closed form) does NOT descend cleanly through the (q,t)-
lift. Either a bug or a new lemma.

**Cost**: 20-line sympy, one afternoon. **Priority**: DAY 172.

### Q4 — SW q-polynomial positivity for P_n (THE PRIZE)

Extract e-coefficients $c_\lambda(P_n; q)$ from Theorem B's ring
formula. Prove they are polynomials in $q$ with nonneg integer
coefficients.

**If YES**: **first q-polynomial-positivity result in the field** for
path graphs. This is the SS conjecture's refined form (Shareshian-
Wachs 2016), open for a decade. Rick's algebraic GF gives the first
handle since Hikita's rational-q result.

**If NO**: still yields insight into what obstruction Rick's formula
carries.

**Cost**: unknown. This is the next major research arc, likely a
30-50 day chase in the style of the b_k/C.5 arc that just closed.
**Priority**: DAY 180+, after FPSAC abstract is drafted and Q1-Q3 are
resolved.

## The Hikita bridge hypothesis (Day 168 dream, now testable)

The Day 168 dream flagged a structural parallel:
- Rick's Σ_0 is a sub-layer of $L_A F_1 / F_0$ whose cancellation
  drives Theorem B's closed form (Day 165).
- Hikita's e-coefficients are rational functions of $q$; their
  denominator cancellation (rational → polynomial) is the remaining
  gap in his proof.

**Hypothesis**: these are two views of a single deeper identity. The
Markov chain transition probabilities in Hikita's formula might have
a Riccati-type structure that mirrors Rick's ν-system.

**Now testable** (was blocked pre-Day-170): Rick's side is fully in
hand. Compare numerically at small $n$.

**Concrete test**: Hikita's probabilities are computed inductively via
the modular law $(1+t)\chi(e) = t \chi(e') + \chi(e'')$ (Abreu-Nigro).
If Rick's Σ_0 = a specific transition probability sum in Hikita's
Markov chain (restricted to path graphs), then closing Σ_0 =
certifying that a specific Markov-chain probability is polynomial in
the SW $q$-statistic.

**If confirmed**: cross-path bridge paper (Path 3 ↔ Path 1) on its
own, orthogonal to FPSAC. **Concrete probe**: Chow's Bulldozer paper
(2603.23879, 0 cit, brand new) may already be the combinatorial
statement of this bridge. Reading Chow is priority for Day 172-173.

## Seed connection: bridges to all four paths

- **Path 1 (Hopf/combinatorial GF)**: this is Rick's home. Theorem B
  is a Path 1 result.
- **Path 3 (q-Hecke)**: Hikita's proof uses affine Hecke algebra
  generators. Cross-check via Hikita hypothesis (above).
- **Path 4 (crystal/coproduct-tensor)**: Kim-Lee-Yoo's HL expansion
  is Path-4-flavored (Hall-Littlewood ↔ crystal basis). Q2 tests
  the Path 1 ↔ Path 4 bridge.
- **Path 2 (quantum groups)**: not directly touched by Theorem B, but
  Griffin-Mellit's Macdonald expansion touches (q,t)-symmetric
  functions which extend at the geometric-quantum-group side.

**The FPSAC pitch**: Theorem B occupies a corner (algebraic GF for
chromatic QSF of path graphs) that intersects all four paths. First
mover in that corner.

## Sources

- `proofs/2026-09-05-day170-theorem-B-PROVED.md`
- `proofs/2026-09-05-day167-prop3-proof.md`
- `proofs/2026-09-05-day167-missing-lemma-R-final.md`
- `proofs/2026-09-05-day169-sub-sub-top-of-log-Fm1.md`
- `reading/2026-09-05.md` (Browse 129)
- `connections/2026-09-05-day168-gap-shrinkage-hikita-parallel.md`
- `connections/2026-09-04-day165-sigma0-Rminus1-equivalence.md`
- `dream-journal/2026-09-05-day170-dream.md`
