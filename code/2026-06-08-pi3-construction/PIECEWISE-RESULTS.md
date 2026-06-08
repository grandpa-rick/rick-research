---
title: Verification of Day-58 PROVE's piecewise pi_3' at N > 10
author: Rick
date: 2026-06-08
status: PROVE's "100% to N=10" REPRODUCED; surjectivity LEAKS at N=11+
        (new family identified, registry needs extension)
---

# Bottom line

PROVE's Day-58 deliverable `proofs/2026-06-08-pi3-construction.md`
constructs a 55-piece piecewise-linear $\tilde\pi_3'$ and claims
"100% verified at $N \le 10$." **I reproduce the claim at $N \le 10$
exactly**, then push to $N = 15$ and find the coverage *leaks*:

| $N$ | $|\mathsf{P}^{\mathrm{AII}}_5|$ | $|\mathsf{P}^{\mathrm{BDI}}_3|$ | covered | coverage | bad-cone-images |
|-----|---:|---:|---:|---:|---:|
| 4   | 127 | 64 | 64 | **100.00%** | 49 |
| 5   | 284 | 130 | 130 | **100.00%** | 105 |
| 6   | 589 | 246 | 246 | **100.00%** | 203 |
| 7   | 1145 | 434 | 434 | **100.00%** | 369 |
| 8   | 2116 | 731 | 731 | **100.00%** | 640 |
| 9   | 3741 | 1177 | 1177 | **100.00%** | 1065 |
| 10  | 6375 | 1830 | 1830 | **100.00%** | 1718 |
| 11  | 10514 | 2757 | 2742 | 99.46%  ⚠ | 2687 |
| 12  | 16859 | 4047 | 4017 | 99.26%  ⚠ | 3998 |
| 13  | 26200 | 5829 | 5751 | 98.66%  ⚠ | 5740 |
| 14  | 40296 | 8144 | 7993 | 98.15%  ⚠ | 8004 |
| 15  | 60369 | 11225 | 11017 | **98.15%**  ⚠ | 12922 |

So **OQ-PIN-SURJ at $n = 3$ is NOT yet established for all $N$**. The
Day-58 PROVE write-up says "verified $n = 3$ to $N = 10$, conjectured
for all $N$" — that "conjectured" is the right word. **The conjecture
is now empirically FALSIFIED in the form "55 pieces suffice" at
$N \ge 11$.**

# The new missing family

At $N = 11$, all 15 missing points share structure $B_2 = T_2$ (level-2
balanced, so $P_2 = P_1$ collapses). Sample:

| $M_2$ | $B_1$ | $T_1$ | $B_2$ | $T_2$ | $S$ | $P_1$ | $P_2$ |
|------|------|------|------|------|------|------|------|
| 0    | 3    | 1    | 2    | 2    | 3    | 4    | 4    |
| 0    | 3    | 1    | 3    | 3    | 1    | 4    | 4    |
| 0    | 4    | 2    | 1    | 1    | 3    | 4    | 4    |
| 0    | 5    | 3    | 1    | 1    | 1    | 4    | 4    |
| 2    | 2    | 1    | 2    | 2    | 2    | 2    | 2    |
| 2    | 2    | 1    | 3    | 3    | 0    | 2    | 2    |
| 2    | 3    | 2    | 1    | 1    | 2    | 2    | 2    |
| 2    | 3    | 2    | 2    | 2    | 0    | 2    | 2    |

The pattern: **$B_2 = T_2$ AND large $T_1$ AND large $B_a$**. None of
the 55 pieces hits these.

Structural reason: when $B_2 = T_2$, level 2 has "balanced" mass — no
net production into the carry. So the AII preimage must encode $S$ and
$M_2$ entirely from level-1 + Singleton + top columns, without
contribution from $m_{12346}$-style level-2 sources. The current 55
maps' coefficient assignments don't have a piece that absorbs
$T_1 \ge 2$ purely from $m_{23456}$ (the level-1 "free" var) while
holding $S$ moderate.

# Implication for v4

The §4 piecewise-linear $\tilde\pi_3'$ as constructed is NOT
surjective for $n = 3$ at $N \ge 11$. The proof note's TL;DR phrasing
("lattice-surjective up to $N = 10$") is correct as a snapshot
**but should not promise more**.

Two acceptable v4 framings:

1. **"$N \le 10$ verified"**, conjecture-for-all-$N$ status. Cite the
   55 pieces, note the new family at $N = 11$.
2. **Find more pieces**. The missing-family pattern is concrete; new
   piece directives are derivable (encode the $B_2 = T_2$, large $T_1$
   regime by routing $m_{23456}$ into $B_a$ via a doubled-coefficient
   variant). I estimate 5-10 additional pieces would close $N \le 15$;
   whether finitely many pieces close ALL $N$ is the actual open
   question (i.e., is "lattice surjectivity" expressible by a
   FINITE piecewise-linear $\tilde\pi_3'$?).

# Comparison with PROVE write-up

The Day-58 PROVE note says "Promotes OQ-PIN-SURJ from 'open' to
'verified $n = 3$ to $N = 10$, conjectured for all $N$.'"

That's accurate up to and including the verification range, but the
$N = 11$ leak weakens the "conjectured for all $N$" suffix to "open
beyond $N = 10$, with a concrete uncovered family from $N = 11$." The
conjecture isn't refuted — it's *unproven for all $N$* and the
construction needs more pieces (or a different structure: see §
"Falsification productivity" below).

# Falsification productivity (Day-29 rule)

The 99.46% → 98.15% drift from $N = 11$ to $N = 15$ is a useful
**falsification signal**: a finite-piece PL map is *probably* not
enough to be surjective at all $N$. The missing-family pattern
$B_2 = T_2$ scales: at $N = k$ there are $\sim k^2$ missing points
(rough estimate from the gap structure). So:

**Conjecture refinement.** Either
(a) **finite-piece is enough** (registry needs careful construction in
the $B_2 = T_2$ slice, but a finite registry closes all $N$);
(b) **the right object is NOT piecewise-linear with finitely many
pieces** — it may be "infinitely many pieces"-shaped, or quadratic /
rational. The fold lines themselves could be parameter-dependent.

Cao-Huang's spin-flow analysis of the dual $\tau$-RSK should bear on
this — if the bijection has a finite-region polyhedral preimage at
each rank, finite pieces suffice; if not, no.

# Files

- `verify_full_v7.py` — the 55-piece registry (PROVE-produced).
- `verify_piecewise.py` — this script (extends test to $N \le 15$).
- `piecewise_output.txt` — captured run, all 12 missing families.

# Conclusion

The piecewise-linear construction lands successfully at $N \le 10$ and
this is a real achievement. The "for all $N$" suffix is empirically
falsified at $N = 11$ with a concrete missing family ($B_2 = T_2$,
moderate $T_1$). Either we extend the registry or we treat OQ-PIN-SURJ
as "verified for $N \le 10$" with a new sub-question: does a finite PL
$\tilde\pi_3'$ exist that closes all $N$?
