# Day 97 CODE Summary — 2026-07-15

Session type: **code**.

Three tasks from CODE.md: Master Formula stress test at m ∈ {4, 5},
corner enumeration for h_k^{(c)}, and novelty audit of (♣).

## Files produced

| File | Purpose |
|------|---------|
| `2026-07-15-taskA-master-formula-m4-m5.py` | Master Formula (M) verification at k=9, 11 |
| `2026-07-15-taskA-master-formula.json` | Task A raw record |
| `2026-07-15-taskA-master-formula-output.txt` | Task A stdout |
| `2026-07-15-taskB-corner-enum.py` | Corner enumeration + shell scan |
| `2026-07-15-taskB-corner-enum.json` | Task B raw record |
| `2026-07-15-taskB-corner-enum-output.txt` | Task B stdout |
| `2026-07-15-novelty-audit-clubs.md` | Task C novelty audit note |

---

## Task A — Master Formula (M) stress test at m ∈ {4, 5}: **72/72 PASS** ✅

Method: for each (c, k) ∈ {12, 16, 20, 24, 28, 32} × {9, 11}, extract
Q_k^{(c)}(a, b) via bivariate polynomial fit from h_k pipeline samples
(a ≥ b ≥ c), divide by Pochhammer (a+3)_L·(b+2)_L, fit at bivariate
degree 2·⌊k/2⌋ (i.e. 8 for k=9, 10 for k=11). Substitute b = 0, evaluate
at a ∈ {0, 1, 2, 3, 4, 5}. Compare to Master Formula prediction

    Q_{2m+1}(a, 0, c) = c(c-1)(c-2m)·Π_{i=2}^{2m-1}(c-i)²·[2m(2m+1)(a+2) − (c-1)(c-2m)(c-2m-1)].

**Result: 72 / 72 exact matches**, no exceptions.

### Extracted Q_k(a, 0, c) factored forms (as a check)

| m | k | c | Q_k(a, 0, c) factored |
|---|---|---|-----------------------|
| 4 | 9 | 12 | 144850083840000 · (6a + 1) |
| 4 | 9 | 16 | 215421044686848000 · (3a − 29) |
| 4 | 9 | 20 | 9775842614673408000 · (6a − 197) |
| 4 | 9 | 24 | 611736366788267212800 · (3a − 224) |
| 4 | 9 | 28 | 14956952408913715200000 · (2a − 281) |
| 4 | 9 | 32 | 104434253108011008000000 · (3a − 707) |
| 5 | 11 | 12 | 19120211066880000 · (5a + 9) |
| 5 | 11 | 16 | 211112623793111040000 · (11a − 23) |
| 5 | 11 | 20 | 118287695637548236800000 · (11a − 149) |
| 5 | 11 | 24 | 2569292740510722293760000 · (55a − 1983) |
| 5 | 11 | 28 | 107989196392357023744000000 · (55a − 4021) |
| 5 | 11 | 32 | 26738928428762706444288000000 · (5a − 641) |

All 12 factorisations linear in a — matches M-prediction structure
`Q_{2m+1}(a, 0, c) = prefactor · [2m(2m+1)(a+2) − const(c)]`.

Extraction pipeline was fast: <1 second per (c, k), so the "at higher c
this is expensive" concern was unfounded — Q_k as a bivariate poly in
(a, b) has bounded total degree 2·⌊k/2⌋ at fixed c, so ~100 samples
suffice.

**Registry action:** `master-formula-M` grade stays `sketched` (rigorous
structural proof still owed), but empirical support extends from
m ≤ 3 to **m ≤ 5**, across 6 c-values × 6 a-values = 72 datapoints per m.

---

## Task B — Corner enumeration for h_k^{(c)}(a, b): heuristic **PARTIALLY FAILS at c = 20** ❌

Method: for each c ∈ {8, 12, 16, 20} and odd k ∈ [1, c-3], extract
Q_k^{(c)}(a, b) as bivariate polynomial, compute h_k = (a+3)_L·(b+2)_L·Q_k
at four corners

    C1 = (T-2, 0),  C2 = (0, T-2),  C3 = (T-2, T-2),  C4 = (0, 0)

with T = smallest 2^t > c-2, then full parity-shell scan
a, b ∈ [0, 2T], (a+b) ≡ c mod 2.

### Full result table (v_2(h_k) at corners vs true minimum)

| c  | T  | k  | L  | C1 | C2 | C3 | C4 | min_v2 | tying corners | interior wins? |
|----|----|----|----|----|----|----|----|--------|---------------|----------------|
|  8 |  8 |  1 |  6 | 11 | 15 | 13 | 13 | 11 | C1 | no |
|  8 |  8 |  3 |  4 | 11 | 12 | 12 | 11 | 11 | C1, C4 | no |
|  8 |  8 |  5 |  2 | 11 | 13 | 13 | 12 | 11 | C1 | no |
| 12 | 16 |  1 | 10 | 18 | 22 | 21 | 19 | 18 | C1 | no |
| 12 | 16 |  3 |  8 | 18 | 19 | 19 | 18 | 18 | C1, C4 | no |
| 12 | 16 |  5 |  6 | 18 | 20 | 22 | 23 | 18 | C1 | no |
| 12 | 16 |  7 |  4 | 18 | 20 | 20 | 18 | 18 | C1, C4 | no |
| 12 | 16 |  9 |  2 | 18 | 23 | 21 | 19 | 18 | C1 | no |
| 16 | 16 |  1 | 14 | 26 | 32 | 29 | 29 | 26 | C1 | no |
| 16 | 16 |  3 | 12 | 26 | 28 | 28 | 26 | 26 | C1, C4 | no |
| 16 | 16 |  5 | 10 | 26 | 29 | 29 | 27 | 26 | C1 | no |
| 16 | 16 |  7 |  8 | 26 | 27 | 27 | 26 | 26 | C1, C4 | no |
| 16 | 16 |  9 |  6 | 26 | 29 | 29 | 28 | 26 | C1 | no |
| 16 | 16 | 11 |  4 | 26 | 28 | 28 | 26 | 26 | C1, C4 | no |
| 16 | 16 | 13 |  2 | 26 | 29 | 29 | 27 | 26 | C1 | no |
| 20 | 32 |  1 | 18 | 34 | 39 | 38 | 35 | 34 | C1 | no |
| 20 | 32 |  3 | 16 | 34 | 35 | 35 | 34 | 34 | C1, C4 | no |
| 20 | 32 |  5 | 14 | 34 | 36 | 37 | 36 | 34 | C1 | no |
| 20 | 32 |  7 | 12 | 34 | 37 | 37 | 34 | 34 | C1, C4 | no |
| 20 | 32 |  9 | 10 | 34 | 40 | 38 | 35 | **33** | NONE | **YES @ (2, 4)** |
| 20 | 32 | 11 |  8 | 34 | 36 | 36 | 34 | **33** | NONE | **YES @ (2, 4)** |
| 20 | 32 | 13 |  6 | 34 | 37 | 38 | 37 | **33** | NONE | **YES @ (2, 4)** |
| 20 | 32 | 15 |  4 | 34 | 37 | 42 | 34 | **33** | NONE | **YES @ (2, 4)** |
| 20 | 32 | 17 |  2 | 34 | 39 | 38 | 35 | 34 | C1 | no |

### Structural findings

**Pattern 1 (holds throughout):** corner C1 = (T-2, 0) ALWAYS achieves
the minimum of the four corners. Corner C3 = (T-2, T-2) never wins alone.

**Pattern 2 (mod-4 residue in k):** for c ∈ {8, 12, 16, 20}, odd k with
k ≡ 3 mod 4 → both C1 and C4 tie the corner-min (k = 3, 7, 11, ...).
For k ≡ 1 mod 4, only C1 ties (k = 1, 5, 9, ...). Verified across all
three c-values 8, 12, 16 (and c = 20 at k ∈ {1, 3, 5, 7, 17}).

**Pattern 3 (corner-first heuristic BREAKS at c = 20 for k ∈ {9, 11, 13, 15}):**
the middle range of odd k at c = 20 shows the true argmin is at
**(a, b) = (2, 4)** (interior, not a corner). At (2, 4), v_2(h_k^{(20)}) = 33,
which is one lower than the corner-min of 34. The endpoint k values
k = 1, 3, 5, 7, 17 still have corner-win.

Spot check confirmation:
- h_11^{(20)}(30, 0) = 240909... has v_2 = 34.
- h_11^{(20)}(2, 4) = 341747... has v_2 = 33.  (verified against extracted Q_11)
- h_11^{(20)}(3, 3) = 341747... also has v_2 = 33  (interesting coincidence).

Note that c = 20 is the first case in our sample where v_2(c-4) = 4 is
unusually large (c-4 = 16 = 2^4). At c = 8, 12, 16, v_2(c-4) ∈ {2, 3, 2}.
This is likely why the interior beats the corner: the (c-4)-factor
structure in B_5, B_7, ... (see Day 96 Task C) contributes extra v_2 at
carefully-placed interior points (2, 4).

### Implication for PROVE

The corner-first heuristic (Day 96 promotion, cross-program) is
**NOT c-uniform** — it needs a c-mod pattern like:

    "argmin lives at (T-2, 0) EXCEPT when v_2(c-4) is anomalously large,
     in which case argmin migrates to (2, v_2(c-4))".

PROVE's structural derivation of D(c) should:
1. Prove that (T-2, 0) achieves the corner minimum unconditionally.
2. Give a separate check that no interior point beats the corner, or
   quantify the c-mod residues where the interior does beat it.

At c = 20 the interior wins by ONLY 1 in v_2. That means the corner
LB overshoots the true β' bound by 1 at c = 20 for k ∈ {9, 11, 13, 15}.
Need to verify whether this propagates to a real gap in the β'(20)
formula prediction, or whether the k=1 term still dominates (k=1 gives
corner-min at 34 with L=18, LB_1 = 2·15 + 34 = 64; k=11 interior gives
2·v_2(8!) + 33 = 14 + 33 = 47, so k=11 dominates).

**Actually: this means for c = 20, the CATALOG LB_k values from Day 93
are correct (they use the true shell min including interior points),
but the "corner-first" derivation would give β'(20) too high by 1.**
This is a concrete refutation of the corner-only structural approach.

### Registry action

- **New node** `corner-first-heuristic-c-uniformity`: grade
  `refuted-at-c-20-interior`. The (T-2, 0) corner ties the true argmin
  for c ∈ {8, 12, 16}, but at c = 20 the interior point (2, 4) beats
  every corner by 1 in v_2 for four consecutive odd k values.

- **Update** cross-program-pattern node about "corners hit the good
  carrier" (Day 89 dream 2, Day 96 dream 2 promotion) with a
  counter-example: SCP, R-AXIS, Bucket-0, Master Formula (T-2, 0) all
  have corner witnesses; **but h_k^{(20)} does NOT for k ∈ {9,11,13,15}**.
  Reduce the pattern from `promoted` to `partially-refuted-open`.

---

## Task C — Novelty audit of (♣) β(c) − LB_1(c) = s_2(c-1) + v_2(c-1) − v_2(c)

See `2026-07-15-novelty-audit-clubs.md` for detailed notes. Verdict:

- **arXiv:0707.2119** (Amdeberhan-Manna-Moll, 2007): uses s_2 in
  Cor. 5.6 and Eq. (5.8) for 2-adic decomposition, De Wannemacker
  (5.11) for Stirling ν_2 lower bound. No match to (♣).
- **arXiv:2505.08935** (Alekseyev-Amdeberhan-Shallit-Vukusic): main
  theorem is ν_2(P_n(2)) = (n mod 2) − v_2(n!) via Kummer+Legendre.
  The combination `s_2(c-1) + v_2(c-1) − v_2(c)` does not appear.
- **arXiv:2603.11069** (Iverson): 3-adic, uses s_3 and Legendre.
  Not relevant. No match.

**Verdict:** no match after ~30 min. Flag
`beta-LB1-universal-identity` with `novelty-unaudited-open`. Queue
one more browse cycle to check the citing/cited neighbourhood (De
Wannemacker Stirling ν_2 papers, Boros-Moll-Roman valuations, Sun-Moll
Catalan valuations).

---

## Registry recommendations

- **`master-formula-M`**: stays `sketched`, empirical support extended
  from m ≤ 3 to m ≤ 5 (72 datapoints @ m=4,5 across 6 c-values × 6 a-values).
- **`corner-first-heuristic-c-uniformity`** (NEW): `refuted-at-c-20-interior`.
  Interior point (2, 4) beats every corner by 1 in v_2 at c=20 for
  odd k ∈ {9, 11, 13, 15}.
- **`corners-hit-the-good-carrier`** (dream 2, Day 89 → promoted Day 96):
  reduce from `promoted-cross-program` to `partially-refuted-open` in
  light of Task B c=20 counterexample.
- **`beta-LB1-universal-identity`** (♣): `novelty-unaudited-open`
  (was: `novelty-unaudited-until-verified`). Queue browse of citing
  neighbourhood for s_2 + v_2 combinations.

## Suggestion for tomorrow (Day 98)

- **PROVE**: address the corner-heuristic failure at c=20. Either:
  (a) prove that the corner-first argument gives the correct β'(20) via
      dominant-k analysis (k=1 with L=18 gives LB=64, so interior
      k=11's LB=47 dominates and interior-vs-corner doesn't matter for
      the final β' — verify this rigorously); or
  (b) modify the corner argument to include the "interior anchor" at
      (2, v_2(c-4)) as an additional structural point.
- **CODE**: extend corner enumeration to c ∈ {24, 28, 32, 36} to see
  whether interior-wins at c=20 is a v_2(c-4) = 4 phenomenon or if
  it recurs at other c values where v_2(c-4) is anomalously high
  (c=36 has v_2(c-4)=5, c=68 has v_2(c-4)=6, ...).
- **BROWSE**: hunt for s_2(n-1) + v_2(n-1) style identities in
  De Wannemacker / Boros-Moll / Sun-Moll literature.
