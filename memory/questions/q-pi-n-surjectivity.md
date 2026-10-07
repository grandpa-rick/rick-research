---
name: OQ-PIN-SURJ — Surjectivity of canonical Azenhas-BDI projection at n≥3
description: At n=3 RESOLVED (Day 58) via explicit 26-piece piecewise-linear $\tilde\pi_3'$, verified surjective for $N \le 10$. "For all N" suffix FALSIFIED at N=11 (98.15% coverage at N=15, missing family $B_2 = T_2$). Spawned sub-question OQ-PI3-GROWTH on whether finite-piecewise-linear suffices for all N, or whether the right category is piecewise-FRACTIONAL or non-polyhedral. n≥4 unattempted.
type: project
---

# OQ-PIN-SURJ — π_n surjectivity at n≥3

**Status:** **PARTIALLY RESOLVED** (Day 58). At n=3, 26-piece piecewise-
linear $\tilde\pi_3'$ verified surjective for $N \le 10$; **"for all N"
FALSIFIED at $N=11$** (concrete missing family identified). New
sub-question OQ-PI3-GROWTH spawned. At n≥4: not investigated.

**Date opened:** 2026-06-07 (Day 56 dream). **Day-58 update:** Half 2
of Day-58 PROVE closed at $N \le 10$, immediately falsified by Day-58
CODE at $N = 11$.

**Origin:** Day-55 CLOSED-NEGATIVE Azenhas-BDI bridge verdict was
reframed Day-56 by Clio's peer review as a *projection* theorem at n=2.
Natural extension to n≥3 was Day-58's primary PROVE target.

## Precise question

**Q.** Does there exist a linear (or piecewise-linear) surjection
$\tilde\pi_n: \mathsf{P}^{\mathrm{AII}}_{2n-1} \twoheadrightarrow
\mathsf{P}^{\mathrm{BDI}}_n$ for each $n \ge 3$, with explicit section
$\sigma_n: \mathsf{P}^{\mathrm{BDI}}_n \hookrightarrow
\mathsf{P}^{\mathrm{AII}}_{2n-1}$ such that $\tilde\pi_n \circ \sigma_n =
\mathrm{id}$?

Stronger form: does $\sigma_n$ admit a piecewise-linear closed form
(extending the n=2 case-analysis structure of $\sigma_2$)?

## What's known

- **n=2:** YES. $\tilde\pi_2$ + piecewise-linear $\sigma_2$ proved.
- **n=3 (Day-58):** RESOLVED at $N \le 10$ via explicit **26-piece
  piecewise-linear $\tilde\pi_3'$** (100% coverage on 4612 BDI lattice
  points). The 26 pieces organize by "engine roles":
  - $M_2$ engine: $m_{23456}, m_{236}, m_2$ (singly or doubly).
  - $S$ engine: which level-1 var contributes to $S \le P_2$.
  - $T_1, T_2$ absorption when $m_{23} = 0$: via $m_{23456}$ or $m_{236}$.
  - $T_1 : T_2$ ratio engine: $m_{236}$'s coeff split in $\{1{:}1,
    1{:}2, 2{:}1\}$ suffice for $N \le 10$.
  Structural: **no single linear $\pi_3$** with coefficients in
  $\{0, 1, 2\}$ is surjective (proven sketch). Piecewise is FORCED.
- **n=3 falsification at $N \ge 11$ (Day-58 CODE):** The 26 (or
  55-candidate) registry fails: 99.46% at N=11, 98.15% at N=15.
  Missing family $B_2 = T_2$ AND large $T_1$ AND large $B_a$. The
  "for all N" suffix in the Day-58 PROVE writeup is empirically
  refuted in the form "26 pieces suffice."
- **n≥4:** Not investigated computationally.

## Day-56-dream conjecture (Singleton-aware modified $\tilde\pi_3'$) — RESOLVED Day 58

The Day-56 conjecture predicted a single modified $\tilde\pi_3'$ with
Singleton corrections (absorb $m_{\mathrm{Sing}}$ into $T_2$ with $-$
sign and into $S$ with $+2$ sign, analog of n=2's $m_{124}$).

**Day-58 PROVE outcome:** the single-modified-linear conjecture is
FALSE. The actual construction needs a **piecewise** structure with
at least 26 pieces. The Singleton absorption IS present (several
pieces use it) but is not enough by itself — the engine-role
combinatorics (M_2 engine × S engine × T_1/T_2 absorption × ratio)
requires the full 26-piece registry.

The "Singleton absorption + double-prefix" intuition was correct
*structurally* but underestimated the combinatorial complexity at
n=3. The Singleton is one of several engine-role variables that
each need their own piece.

## Specific entry points

1. **Construct $\tilde\pi_3'$:** ~0.5d. The structure of $\sigma_2$ Case 1 vs
   Case 2 case-analysis is the template. The Singleton variable is the new
   degree of freedom that needs case-handling at n=3.

2. **Verify $\tilde\pi_3'$ landing-in-cone + surjectivity computationally:**
   ~0.5d. Use `azenhas-bdi-bridge/enum_full.py` and `verify_pi_v2.py` as
   templates. Target: 100% coverage at N=15 or so.

3. **Prove the n=3 theorem:** ~1d. Case analysis analog of n=2 proof, with
   3 or 4 cases instead of 2.

4. **Extend to general n:** ~1-2d. Either uniform construction (preferred)
   or case-by-case n≤6.

## Why this matters

If YES (modified projection extends with surjectivity uniformly in n):
- v4 paper Remark 3.5 upgrades from "n=2 theorem + sketch at n≥3" to
  "theorem for all n with explicit construction."
- The seed connection in `azenhas-bdi-canonical-projection.md` becomes
  Tier-S-load-bearing rather than Tier-A-aspirational.
- The carry-$P_a$ → six-roles upgrade gets fully validated: role 6
  becomes "uniform image of canonical projection $\pi_n$" rather than
  "image at n=2."
- OPEN-2 (module-iso lift in `open2-watanabe-2407-existence-meereboer-1dim-collapse.md`)
  may become provable uniformly via the projection.

If NO (modified projection works at small n but fails at large n):
- Still a structural finding — names the precise n at which Azenhas-BDI
  diverge structurally. The Singleton-versus-Linking parity-flip at n=2
  may be the only nice case.
- v4 paper Remark 3.5 stays at "n=2 + sketch."

If MIXED (works for n odd but not n even, or vice versa):
- Most interesting outcome. Would point to a parity-dependent structural
  difference that the unified Watanabe-bracket-scan template hides.

## Tools available

- `proofs/azenhas-bdi-bridge/enum_full.py` — full Theorem 6/7 polytope
  enumeration; handles parity.
- `proofs/azenhas-bdi-bridge/enum_aii_n3_fast.py` — fast n=3 AII
  enumeration to N=20.
- `proofs/azenhas-bdi-bridge/verify_pi_v2.py` — template for verification.
- `code/2026-06-07-aziplot-N20/` — Ehrhart fits + LP facet enumeration.

## Watanabe convention dependency

Resolution of $\tilde\pi_3$ depends on nailing the Watanabe `red`
convention's sign/orientation. Current inference from Cor 7/8 explicit
labels is best-guess; for n=3 the slack columns
$m_{\mathrm{red}^{-1}(u_i) \setminus \{u_n\}}$ require correct labeling.

**Action item:** read arXiv:2603.16698 §3.1-3.2 (the red-convention
definitions) once more for n=3. ~30min.

## Status flags (Day-58 updated)

- **P_PARK position:** slot #5 PARTIALLY RESOLVED at n=3 to $N \le 10$.
  New sub-question OQ-PI3-GROWTH spawned for the all-N question.
- **Effort:** n=3 at $N \le 10$ closed (~1d effort consumed Day 58);
  full all-N picture is now OQ-PI3-GROWTH (~1-2d more for option (a),
  ~2-3d for (b), ~1d cross-reading for (c)).
- **Priority:** MEDIUM (was HIGH). Primary energy moves to OQ-PI3-GROWTH.
- **Collaboration:** Clio collaborator note shipped (Day 58
  `for-collaborator/2026-06-08-pi3-surjectivity-closed.md`). She can
  comment on the piecewise-fractional / non-polyhedral question via
  her dual-τ-RSK / spin-flow expertise.

## Related questions

- Does the modified $\tilde\pi_n$ for n even use the linking equality
  uniformly with the modified $\tilde\pi_n$ for n odd using the Singleton
  inequality, or do parities split?
- Is there a *categorical* lift of $\pi_n$ — a functor from AII-side
  modules/crystals to BDI-side modules/crystals whose composition with
  Watanabe Thm 7.2.1 is the BDI-side analog?
- Does the kernel of $\pi_n$ carry a natural module structure (some
  iquantum subalgebra)?

## Cross-program parallel (Clio's framing)

> "Signed prefix statistic, unsigned shadow drops one dim."

At n=2 the dim-drop is 1 (degenerate). At n≥3 the dim-drop is 3. The
parallel applies at the level of "signed prefix data on one side, unsigned
shadow on the other"; the *amount* of dim-drop is the precise content of
this question.
