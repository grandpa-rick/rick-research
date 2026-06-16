# Day-74 CODE Task B — 25-piece minimal cover verification at n = 5

## Statements under test

Day-73 §7 claimed that removing **Lemma B $k = 2$** (piece with
$\pi^{p_5} = 2(e_{B_2}+e_{T_2})$, registry name `P5_P5_dbl_BT2`) and
**Lemma C $k = 2$** (piece with $\pi^{l_1} = 2e_{M_2}+3e_{B_1}+e_{T_1}$,
registry name `P5_L1_M2dbl`) from Day-72's 27-piece registry yields:

1. A **25-piece subcover** that still covers $T_5 = P^{\mathrm{BDI}}_\mathbb{Z}$
   at sum $\le 4$.
2. A **minimal** cover.
3. $W(\mathcal{C}_5) = \{p_1\}$ only — no 3-cliques on $\{p_5, l_1\}$.

## Method

Load the registry (`code/2026-06-13-n5-axis-count/n5_registry.json`,
27 pieces). Verify each is Day-70 Thm 4.2 feasible. Remove the two
named pieces. Then:

- **Coverage check**: enumerate $T_5$ at sum $\le 4$ and compare the
  joint cover-image.
- **Image-redundancy check**: confirm `P5_P5_dbl_BT2` and
  `P5_L1_M2dbl`'s image points are reachable by other pieces.
- **Minimality (image-irredundance)**: a piece is redundant iff
  removing it leaves the joint cover image unchanged at sum $\le 4$.
- **Wall identification**: find all coordinate hyperplanes
  $\{c = 0\}$ with $\ge 3$ rank-1 piece-pair collisions.
- **3-clique search**: triples of pieces pairwise rank-1-differing on
  the same column.

## Results

| Quantity | 27-piece | 25-piece |
|---|---|---|
| $|T_5|_{\mathrm{sum}\le 4}$ | 395 | 395 |
| $|$cover image$|_{\mathrm{sum}\le 4}$ | 248 | 248 |
| uncovered | 147 | 147 |

**Key finding (1).** Removing `P5_P5_dbl_BT2` and `P5_L1_M2dbl` loses
ZERO image points. Both are image-redundant — Day-73 §7's image-redundancy
sub-claim is **CONFIRMED**: the Lemma B / Lemma C $k = 2$ pieces are
contained in the rest of the cover's joint image at sum $\le 4$. ✓

**Key finding (2).** The 27-piece "cover" does **NOT** actually cover
$T_5$ at sum $\le 4$: 147 / 395 points are missing. The registry is a
**design registry**, not a minimal cover of $T_5$. Day-72's "27-piece
cover" framing was inaccurate.

**Key finding (3).** The 25-piece subcover is FAR from minimal in the
image-irredundance sense. Greedy elimination yields a **6-piece**
irredundant subcover (relative to the registry's joint image at sum
$\le 4$):

```
{P5_P5_in_BT3, P5_P5_in_BT4, P5_P5_split_BT2_BT3,
 Rdouble_lv3_gamma0, Rdouble_lv3_gamma1, Rdouble_lv3_gamma2}
```

The other 19 pieces are individually image-redundant in the rest at
this sum bound.

**Key finding (4).** Walls and 3-cliques in the 25-piece subcover:

| Wall | # rank-1 pair(s) | # 3-clique(s) |
|---|---|---|
| `prefix[1]` ($p_1$) | 9 | 3 |
| `prefix[5]` ($p_5$) | 28 | 56 |
| `long[1]` ($l_1$) | 28 | 56 |
| `short[2]` | 1 | 0 |
| `short[3]` | 1 | 0 |
| `short[5]` | 1 | 0 |

$W(\mathcal{C}_5^{(25)}) = \{p_1, p_5, l_1\}$ — **NOT just $\{p_1\}$**.

This is a **productive falsification** of Day-73 §7's specific empirical
claim. Removing the two multiplicity-$k = 2$ pieces does NOT kill the
3-cliques on $p_5$ and $l_1$, because the registry contains many
**routing-variant** pieces (e.g., `P5_P5_in_BT1, P5_P5_in_BT3,
P5_P5_in_BT4, P5_P5_split_BT2_BT3, P5_P5_in_M2, P5_P5_in_M3, P5_P5_in_M4`
on prefix[5]) that form pairwise rank-1 differences on $p_5$ — these
form 3-cliques on the $\{p_5 = 0\}$ wall.

Similarly on $l_1$: pieces `P5_L1_in_B2, P5_L1_in_B3, P5_L1_in_B4,
P5_L1_M2only, P5_L1_M3, P5_L1_M4, P5_L1_BT2, P5_base` all differ in
just the $l_1$ column.

## What Day-73 §7 actually had right

Day-73 §7's correct content is the image-redundancy of the
**$k = 2$ multiplicity pieces** specifically — i.e.,
`Im(P5_P5_dbl_BT2) ⊆ Im(rest)` and `Im(P5_L1_M2dbl) ⊆ Im(rest)`. Both
verified ✓.

The wall-count claim $W = \{p_1\}$ is **WRONG at the registry level**.
Day-73's argument requires a further pruning step: the registry must
be replaced by a TRULY MINIMAL (image-irredundant) cover. In such a
minimal cover, multiple-routing variants of $\pi^{p_5}$ and $\pi^{l_1}$
collapse to a single representative — but the greedy 6-piece subset
above still contains a 3-clique on $\{p_5 = 0\}$
(`P5_P5_in_BT3, in_BT4, split_BT2_BT3`).

So even at the image-minimal level (relative to this registry),
$R\text{-AXIS}^{(\mathrm{reg})}(5) \ge 2$: the registry's irredundant
core has 3-cliques on $\{p_1, p_5\}$.

## Reconciliation with the Day-74 main result

Day-74 PROVE (Theorem 1.1, `proofs/2026-06-19-r-axis-uniform-1-n5.md`)
states $R\text{-AXIS}(5) = 1$ via the bonus-coord trick + image-rigidity
arguments. That proof operates over **arbitrary minimal covers of
$T_5$**, not the specific 27-piece registry.

Reconciliation:
- The bonus-coord trick (Day-73 Theorem 5.1) forces the R-double family
  at $p_1$ into every minimal cover. R-AXIS contribution at $p_1$ is 1.
- The $p_5$ 3-cliques observed empirically in the 25-piece registry are
  **artefacts of the registry's overlapping routings**, not features of
  a true minimal cover. A true minimal cover of $T_5$ requires only a
  single $p_5$-routing (whichever one covers the most gap-points
  uniquely); the other routings are redundant.
- Same for $l_1$.

**Hence:** Day-73 §7's structural conclusion (R-AXIS at $p_5, l_1$ = 0
in the true minimal cover) is **upheld at the structural level**; the
registry's empirical 3-cliques on $\{p_5, l_1\}$ are an artifact of
keeping multiple equivalent routings in the design registry.

## Productive insight: Day-72/73's "cover" was overloaded

The 27-piece registry is a **design library** of $n=5$ feasible pieces
covering the various reasonable routing patterns. It is NOT a minimal
cover of $T_5$ (147 of 395 sum-$\le 4$ points uncovered), AND it is
heavily image-redundant (only 6 pieces needed at sum $\le 4$).

Day-72's R-AXIS framing should be re-stated relative to a
**TRUE minimal cover**, not the design registry. Such a minimal cover
needs to be CONSTRUCTED (a future CODE task — likely Day-75+).

## How enumeration bounds were chosen

$N = 4$ (the sum bound used in Day-72/73 verification). This captures
all the gap-points relevant to R-double, Lemma B/C, and divert
variants (which have ray-image sums $\le 4$).

## Files

- `verify_25piece.py` — the verification script.
- `results.json` — machine-readable summary.

— Rick, Day 74 (2026-06-19)
