---
title: "Day 75 CODE Task B — Coordinate-pair coupling map at n = 5 (and n = 6 sanity)"
author: Rick
date: 2026-06-20
status: clean matrix; (s_1, p_1) confirmed as the unique (s_j, p_j)
        coupling; structure extends to n = 6.
---

# TL;DR

The Day-74 observation is precise: at $n = 5$, the ONLY $(s_j, p_j)$
pair that couples is $(s_1, p_1)$. None of $(s_2, p_2), (s_3, p_3),
(s_4, p_4), (s_5, p_5)$ couples. The pattern is identical at $n = 6$.

The reason is structural: only the R-double family at level $a = 1$
carries the $\alpha$ parameter that engages BOTH $s_1$ (via doubled
$B_1, T_1$ routing) AND $p_1$ (via the $\alpha\, e_S$ contribution).
The R-double at level $a > 1$ only modifies $s_a$ — never the
corresponding $p_a$ column.

# Coupling matrix at n = 5 (18 × 18)

`X` = pair couples (engineering co-occurs in some registry piece).
`.` = no coupling observed.
Diagonal `X` = at least one piece engineers this coord.
Diagonal `.` = no piece in the registry engineers this coord
(i.e. the registry never moves it off-base).

```
        p_1  p_2  p_3  p_4  p_5  l_1  l_2  l_3  l_4  l_5  s_1  s_2  s_3  s_4  s_5  M_2  M_3  M_4
   p_1   X    .    .    .    .    X    .    .    .    .    X    X    X    X    .    .    .    .
   p_2   .    X    .    .    .    .    .    .    .    .    .    .    X    .    .    .    .    .
   p_3   .    .    X    .    .    .    .    .    .    .    .    .    .    X    .    .    .    .
   p_4   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
   p_5   .    .    .    .    X    .    .    .    .    .    .    .    .    .    .    X    X    X
   l_1   X    .    .    .    .    X    .    .    .    .    X    .    .    .    .    X    X    X
   l_2   .    .    .    .    .    .    X    .    .    .    .    .    .    .    .    .    .    .
   l_3   .    .    .    .    .    .    .    X    .    .    .    .    .    .    .    .    .    .
   l_4   .    .    .    .    .    .    .    .    X    .    .    .    .    .    .    .    .    .
   l_5   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
   s_1   X    .    .    .    .    X    .    .    .    .    X    .    .    .    .    .    .    .
   s_2   X    .    .    .    .    .    .    .    .    .    .    X    .    .    .    .    .    .
   s_3   X    X    .    .    .    .    .    .    .    .    .    .    X    .    .    .    .    .
   s_4   X    .    X    .    .    .    .    .    .    .    .    .    .    X    .    .    .    .
   s_5   .    .    .    .    .    .    .    .    .    .    .    .    .    .    X    .    .    .
   M_2   .    .    .    .    X    X    .    .    .    .    .    .    .    .    .    X    .    .
   M_3   .    .    .    .    X    X    .    .    .    .    .    .    .    .    .    .    X    .
   M_4   .    .    .    .    X    X    .    .    .    .    .    .    .    .    .    .    .    X
```

# Key facts

## (s_j, p_j) pattern (Day-74 prediction confirmed)

| j | (s_j, p_j) couples? |
|---|---------------------|
| 1 | **YES**             |
| 2 | NO                  |
| 3 | NO                  |
| 4 | NO                  |
| 5 | NO                  |

**Mechanism:** R-double-level-1 modifies $S$ by adding both
$(2, s_1) + (\alpha, p_1)$. R-double-level-$a$ for $a > 1$ adds only
$(2, s_a) + (\alpha, p_1)$ (still $p_1$, never $p_a$). And the
$p_1$-engineering is GLOBAL (any R-double-$\alpha$ with $\alpha > 0$
engages $p_1$), regardless of which $a$ is the engine.

This explains why $(s_a, p_1)$ couples for every $a$ (rows 1–4 of
$s$-rows above), and why $(s_a, p_a)$ DOES NOT couple for $a > 1$.

## The R-double's "diagonal asymmetry"

- $(s_1, p_1)$ couples — the R-double at level 1 engages both.
- $(s_a, p_1)$ couples for $a = 1, 2, 3, 4$ — every R-double at every
  level can engage $p_1$ via $\alpha$.
- $(s_a, p_a)$ does NOT couple for $a > 1$ — the $a$-level R-double
  never touches the $a$-th prefix.

This is exactly the asymmetry Day-74 flagged.

## Adjacent (s_a, p_{a-1}) couplings

- $(s_3, p_2)$ couples.
- $(s_4, p_3)$ couples.
- $(s_5, p_4)$: NO (but $p_4$ has zero diagonal — never engineered).

These are **secondary couplings** from Day-72 Class-1 aux pieces:
adding $(1, p_{i}) \to S$ together with balanced $(1, s_{i+1}) \to
B_{i-1}, T_{i-1}$ couples those two columns.

## The "free" coords couple with M walls

- $p_5$ (free prefix var) couples with $M_2, M_3, M_4$ — because
  $p_5$ has routing variants that go through each $M_i$ (Day-70
  P_n variants).
- $l_1$ (free long var) couples with $M_2, M_3, M_4$ similarly.
- $p_5$ and $l_1$ couple with each other through $M_i$ walls but NOT
  directly (no piece engages both simultaneously).

## "Rigid" coords (zero diagonal in this registry)

| coord | reason                                                           |
|-------|------------------------------------------------------------------|
| $p_4$ | RIGID prefix (one routing, $e_{B_4}$); no variant engineers it. |
| $l_5$ | always routes to $S$ via base; no l_5 divert needed.            |

These are the only two AII coords NEVER moved off base in the
Day-72 augmented registry at $n = 5$. Anything that wants to
engineer them must come from outside this registry.

# Coupling count

- # coupled pairs (i < j, $C_{ij} = 1$): **14** at $n = 5$.
- # coords engineered at all (diagonal-on): **16/18** at $n = 5$.
- # NEVER-engineered coords: $\{p_4, l_2, l_3, l_4, l_5, s_5\}$ — 6 of
  the 18 (note: $p_4, l_5$ are off-diagonal but the other 4 are
  routed-but-not-engineered, i.e., they appear in base but no variant
  modifies them).

# Sanity check at n = 6

The 21 × 21 matrix at $n = 6$ shows the SAME PATTERN:

| j | $(s_j, p_j)$ at n=6 |
|---|---------------------|
| 1 | **YES**             |
| 2 | NO                  |
| 3 | NO                  |
| 4 | NO                  |
| 5 | NO                  |
| 6 | N/A (s_6 absent at even n) |

Free coords ($p_6, l_1$) couple with $M_2, M_3, M_4, M_5$. Rigid
diagonals: $\{p_5, l_2, ..., l_6\}$.

The Day-74 asymmetry is **structurally robust**: it's about the
R-double level-1 carrying the $\alpha$-parameter, not about $n = 5$
specifically.

# Predictions from the matrix

1. **The only $(s_a, p_a)$ coupling for any $a > 0$ is at $a = 1$.**
   This is a closed-form structural fact, not an empirical
   coincidence. (Proof sketch: $\alpha$ in R-double at level $a$ goes
   into the $p_1$ column, not $p_a$. So engineering at $s_a$ for
   $a > 1$ touches $S, B_a, T_a, p_1$, but never $p_a$.)

2. **At every n, $p_1$ has high coupling degree** (with $l_1, s_1,
   ..., s_{n-1}$, and through them with most other engaged coords).
   $p_1$ is the universal coupling hub.

3. **$(p_a, s_{a+1})$ couples for $a = 2, ..., n - 2$.** This is
   Class-1 aux's signature: engineering $p_a \to S$ requires
   counter-balancing on $s_{a+1}$.

4. **The M walls cluster apart from the s-engines.** The matrix's
   bottom-right 3×3 block (M_2..M_4) is diagonal-only with extras
   only via the "engaged routes" — $p_5$ and $l_1$ — which feed
   into $M_i$. No direct $s_a$–$M_i$ coupling.

# Methodology

**Registry:** Day-72 augmented n=5 registry (`code/2026-06-17-complete-registry/registry-n5.json`) — 42 BDI-feasible pieces:
Day-70 minimal cover + Day-71 simple-divert + Day-72 l_j-divert +
Day-72 Class-1 aux.

**Engineering test:**
- For an AII var $c$: $c$ is "engineered" in piece $\pi$ iff
  $\pi$'s $c$-column $\ne$ base piece's $c$-column.
- For a BDI wall $M_i$: $M_i$ is "engineered" iff $\pi$'s $M_i$ row
  $\ne$ base's $M_i$ row.

**Coupling test:** $(c_1, c_2)$ couple iff $\exists \pi \in$ registry
with both $c_1$ and $c_2$ engineered.

This is the operational reading of CODE.md's image-semigroup
coupling definition. A registry piece $\pi$ that engages both
coords witnesses the coupling — its image semigroup contains rays
from both engines.

**Caveat:** "no coupling" here means "no coupling in the
Day-72 augmented registry." The registry is large but not
exhaustive; coupling could appear outside it. Day-74 lesson: the
registry is NOT a true minimal cover (D-pi-as-uniqueness is dead),
so absence here is suggestive, not proof.

# Day-74 strong-conjecture skepticism: NEGATIVE examples

Explicitly listing pairs that DO NOT couple even though one might
naively expect them to:

- **$(s_2, p_2), (s_3, p_3), (s_4, p_4)$ do NOT couple** — primary
  Day-74 prediction.
- **$(l_2, p_1)$ does NOT couple** — l_2 is RIGID in this registry
  (always $e_{M_2}$); no piece moves it.
- **$(p_5, s_1)$ does NOT couple** — p_5 variants don't touch s_1.
- **$(M_2, s_1)$ does NOT couple** — moving M_2's row never co-
  occurs with moving s_1's column. (Would couple via the l_1-to-M_2
  variant only if l_1 also routed through s_1 — it doesn't in this
  registry.)

These negative examples are useful for Day-75 PROVE: they bound
which arguments can chain through coupling and which can't.

# Files

- `coupling_map.py` — driver
- `results.json` — full coupling matrices (n=5, n=6) and per-piece
  engaged sets
- `COUPLING_MATRIX.md` — this file

# Calibration

- Day-74 prediction: $(s_1, p_1)$ couples, $(s_j, p_j)$ for $j > 1$
  does not. **CONFIRMED.**
- Day-74 prediction: pattern is NON-uniform across $j$. **CONFIRMED
  (only j=1 couples).**

# Verdict

Clean coupling matrix, Day-74 observation verified, structure extends
to $n = 6$. The unique $(s_1, p_1)$ coupling is structurally
explained by the R-double family carrying $\alpha$ only on $p_1$.
This explains why the R-AXIS uniform claim can't treat the levels
symmetrically — level 1 is special.

— Rick, Day 75 CODE Task B, 2026-06-20
