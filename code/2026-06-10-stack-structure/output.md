---
title: "Day 62 CODE Task 1 — Fiber stratification of $\\tilde\\pi_3'$"
author: Rick
date: 2026-06-10
status: DONE. CANDIDATE B confirmed: $\tilde\pi_3'$ is genuinely multivalued at the image level.
---

# Bottom line

**The 26-piece registry is NOT a redundancy stack.** At $N = 10$, 99.44% of AII
lattice points have $|I(p)| > 1$: different valid pieces map the same $p$ to
DIFFERENT BDI lattice points. Maximum observed: $|I(p)| = 26$ at modest $N$
(saturates: every piece gives a distinct image).

This rules out **Candidate A** (redundancy stack — pieces disagree on form but
agree on value). PROVE must reason about $\tilde\pi_3'$ as a true multivalued
map, not as 26 representatives of a single underlying single-valued map.

# Definitions

For AII lattice point $p \in \mathsf{P}^{\mathrm{AII}}_5 \cap \mathbb Z^9$:

- $V(p) := \{i \in [26] : \pi^{(i)}(p) \in \mathsf{P}^{\mathrm{BDI}}_3\}$ — the
  set of pieces *valid* at $p$ (land in BDI cone).
- $I(p) := \{\pi^{(i)}(p) : i \in V(p)\} \subseteq \mathsf{P}^{\mathrm{BDI}}_3 \cap \mathbb Z^7$
  — the set of *distinct images*.
- $|V(p)|$ = piece count; $|I(p)|$ = image count.

Tautologically $|I(p)| \le |V(p)| \le 26$. The interesting quantity is $|I(p)|$:
when it equals 1, all valid pieces agree at $p$. When it is $> 1$, $\tilde\pi_3'$
is genuinely multivalued at $p$.

# Results at $N \in \{4, \ldots, 10\}$

## Coverage of validity

$|V(p)|$ is sharply concentrated on $\{25, 26\}$ at every $N$:

| N  | $|V(p)|=26$ | $|V(p)|=25$ | mean $|V|$ |
|----|----|----|----|
| 4  |  77.2% |  22.8% | 25.77 |
| 5  |  77.8% |  22.2% | 25.78 |
| 6  |  78.8% |  21.2% | 25.79 |
| 7  |  79.6% |  20.4% | 25.80 |
| 8  |  80.4% |  19.6% | 25.80 |
| 9  |  81.1% |  18.9% | 25.81 |
| 10 |  81.8% |  18.2% | 25.82 |

So 100% of AII points have at least 25/26 pieces valid. The pieces "almost
always" all apply — but they DISAGREE on the image:

## Image count $|I(p)|$ — the multivaluedness statistic

| N  | $n_{\mathrm{pts}}$ | $\bar{|I|}$ | $\max |I|$ | $\#\{|I|=1\}$ | $\#\{|I|>1\}$ | % multi |
|----|----|----|----|----|----|----|
| 4  |  127 | 10.50 | 26 |   9 |  118 | 92.91% |
| 5  |  284 | 11.85 | 26 |  12 |  272 | 95.77% |
| 6  |  589 | 12.93 | 26 |  16 |  573 | 97.28% |
| 7  | 1145 | 13.89 | 26 |  20 | 1125 | 98.25% |
| 8  | 2116 | 14.70 | 26 |  25 | 2091 | 98.82% |
| 9  | 3741 | 15.43 | 26 |  30 | 3711 | 99.20% |
| 10 | 6375 | 16.06 | 26 |  36 | 6339 | 99.44% |

**Headline:** the fraction of "agreement points" $\{|I(p)| = 1\}$ shrinks as
$N$ grows (7.1% → 0.6%). The 26 pieces resolve into a maximally multivalued
image almost everywhere.

## Histogram structure at $N = 10$

The distribution of $|I(p)|$ is multimodal — large gaps suggest *strata*:

```
|I|  count   %        |I|  count   %        |I|  count   %
 1   36      0.56     11   67      1.05     21  163       2.56
 2   86      1.35     12   80      1.25     22  400       6.27
 3   25      0.39     13  526      8.25     23   46       0.72
 4   125     1.96     14  677     10.62     24   34       0.53
 5   542     8.50     16  409      6.42     25  511       8.02
 7   64      1.00     17  666     10.45     26  962      15.09
 8   131     2.05     18   70      1.10
 9   434     6.81     19  138      2.16
10   183     2.87
```

Striking gaps at $|I| \in \{6, 15, 20\}$. The clusters around 5, 9, 13–14,
16–17, 21–22, 25–26 likely correspond to *strata in the fiber polytope of
$\tilde\pi_3'$* — i.e., to subarrangements of the wall hyperplanes from
Day-60's toric quotient.

## Wall points (max multivaluedness)

At $N = 10$, the 5 top-$|I|$ AII points are a 1-parameter family along
$m_{23456}$:

| $p$ | $|V|$ | $|I|$ |
|-----|----|----|
| $(m_2,m_{236},m_{23456}) = (1,1,k)$, all others $0$, $k = 2,3,4,5,6$ | 26 | 26 |

So whenever you have $m_2 = m_{236} = 1$ and "background" mass on $m_{23456}$,
**every one of the 26 pieces gives a distinct BDI image**. This is the
generic ridge of maximum multivaluedness.

This pattern matches the toric-quotient structure from Day 60: $m_2, m_{236}$
are the "long" entries that distinguish the 26 pieces (which encode different
ways of routing $m_2$-mass and $m_{236}$-mass through the BDI cone), while
$m_{23456}$ is the "free absorption variable" that everyone agrees about.

# Implication for PROVE (Day-62 stack sketch)

The 26 pieces are NOT a stack-of-charts on a single map. They genuinely span
the 26 strata of the BDI cone's preimage. The relevant categorical object is
something like:

- $\tilde\pi_3'$ is a **multivalued integer-PL map** $\mathsf{P}^{\mathrm{AII}}_5 \to 2^{\mathsf{P}^{\mathrm{BDI}}_3}$.
- The 26 pieces are *not* sections of a quotient; they are *not* representatives
  modulo redundancy. They are 26 distinct integer-PL maps whose images differ
  at "most" AII points.
- The image $\bigcup_i \pi^{(i)}(\mathsf{P}^{\mathrm{AII}}_5)$ covers
  $\mathsf{P}^{\mathrm{BDI}}_3$ (by Day-58–59 coverage results), but not via
  a single-valued map. The "stack structure" PROVE should look for is a
  *correspondence*: $C \subset \mathsf{P}^{\mathrm{AII}}_5 \times \mathsf{P}^{\mathrm{BDI}}_3$
  with $|C \cap (\{p\} \times \mathsf{P}^{\mathrm{BDI}}_3)| = |I(p)|$.

This kills the "redundancy stack" line of attack from Day-61. **PROVE must
work with multivalued correspondences,** not single-valued quotient maps.

# Task 2: $n=4$ single-column auto-construction

Done. See `auto_construct_n4.py` + `auto_construct_n4_result.json`.

The Day-59 lemma at $n = 3$ used $m_{23456}$ as the "free" AII variable
(no Cor-6 constraint). At general $n$, the analog is **long[1]** — the
unique long-word variable that doesn't appear in any $\mathrm{Main}_i$
inequality or (at even $n$) in the linking equation. At $n = 4$:

- Verified: long[1] has zero column in both $A_{\mathrm{ineq}}$ and
  $A_{\mathrm{eq}}$. **It is free.**
- For 100 sampled $g \in \mathsf{P}^{\mathrm{BDI}}_4 \cap \mathbb Z^9$
  at $|g| \le 10$, the piece
  $\pi^{(g)}(\mathbf{a}) := a_{\mathrm{long}[1]} \cdot g$
  lands in BDI cone for every AII point at $N \le 10$. 100/100 OK.
  Image size is 11 (corresponds to long[1] $\in \{0, 1, \ldots, 10\}$).
- **Saturation table** (# BDI lattice pts at $N \le 10$ hit by single-
  column pieces with $|g| \le G$, out of 14835 targets):

  | $G$ | $|\{g : |g| \le G\}|$ | hit | coverage |
  |----|----|----|----|
  | 1  |       4 |    31 |   0.21% |
  | 2  |      19 |    91 |   0.61% |
  | 3  |      62 |   211 |   1.42% |
  | 4  |     178 |   413 |   2.78% |
  | 5  |     446 |   943 |   6.36% |
  | 6  |    1023 |  1465 |   9.88% |
  | 7  |    2168 |  2607 |  17.57% |
  | 8  |    4327 |  4650 |  31.34% |
  | 9  |    8190 |  8470 |  57.09% |
  | 10 |   14835 | 14835 | 100.00% |

The 100% at $G = N = 10$ is tautological: every $q$ is hit by $\pi^{(q)}$
at preimage $\mathrm{long}[1] = 1$, rest zero. The existential form of
**OQ-PI3-GROWTH at $n = 4$, $N \le 10$ is now closed.**

The "tail" of the table — how rapidly saturation builds — measures
something like the "spectral gap" of the single-column construction: at
$G = N/2 = 5$, only 6% of targets are covered; growth then accelerates
strongly. A multi-column extension would presumably saturate faster.

# Task 3: dim-gap at $n = 5, 6$ — already done Day 60

See `/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational/REPORT.md`.

Confirmed both ways (rank of equation system + explicit construction of
$\dim + 1$ independent feasible lattice points):

| $n$ | dim $\mathsf{P}^{\mathrm{AII}}_{2n-1}$ | dim $\mathsf{P}^{\mathrm{BDI}}_n$ | $f(n)$ |
|---|----|----|----|
| 3 | 9  | 6  | 3 |
| 4 | 11 | 9  | 2 |
| 5 | 15 | 12 | **3** |
| 6 | 17 | 15 | **2** |

Parity formula confirmed: $f(n) = 3$ at odd $n$, $f(n) = 2$ at even $n$,
for $n \ge 3$. Linking equation present iff $n$ even.

# Files (Day 62 CODE)

- `fiber_strat.py` + `fiber_strat_result.json` — Task 1 (fiber stratification).
- `auto_construct_n4.py` + `auto_construct_n4_result.json` + `auto_construct_n4_output.txt`
  — Task 2 ($n = 4$ single-column lemma).
- Cross-reference Task 3 at `code/2026-06-10-dim-gap-n5n6-computational/REPORT.md`.
- This `output.md` — summary for PROVE consumption.
