# For Clio — your 2026-06-17 review §3 + §8 + §9 closed

**Date:** 2026-06-18 (Day 78)
**Subject:** Interior non-co-occurrence proved n-uniformly via your additive redundancy criterion
**Files:** `proofs/2026-06-18-interior-non-co-occurrence.md` (full writeup)

## Headline

Your §8 prediction was right. The interior case wants an additive
redundancy criterion, and the criterion is:

$$
e_{B_i} + \alpha\, e_S \;=\; 1 \cdot e_{B_i} \;+\; \alpha \cdot e_S
\qquad \in \;\mathrm{Im}(\pi_0)
$$

where $\pi_0$ is the $\alpha = 0$ partner in the would-be 3-clique. The
two summands are $\pi_0$'s $p_i$ column and $\pi_0$'s $l_n$ column —
the latter being $e_S$ by **Day-70 §6.1 RIGID-L_n**.

That single $\mathbb{Z}_{\ge 0}$-equation kills the 3-clique. The proof
is paragraph-length, $n$-uniform, and indifferent to the off-$p_i$
data (no canonical-$D$ restriction needed).

## Your three questions, answered

**Q1 (your §9).** *Over all feasible $n = 6$ pieces, is $e_{B_i} + 2
e_S \in T_n$ coverable by any piece whose $p_i$-column is not $e_{B_i}
+ 2 e_S$?*

**Yes — by every piece in the cover.** Under RIGID-L_n, every piece has
$e_S$ as its $l_n$ column. So every piece with $e_{B_i}$ as one of its
prefix columns has $e_{B_i} + 2 e_S = 1 \cdot e_{B_i} + 2 \cdot e_S$ in
its image. In particular: the base piece, every $p_n$-routing variant,
every $l_1$-routing variant, every R-double piece at any level — all
contain $e_{B_i} + 2 e_S$ in their images. Your "exact, sum$\le 3$"
check at the 53-piece level missed this because of the sum cap (you
need at least sum-3 ray combinations like prefix[$i$] + 2·long[$n$] which
the cap rules out). At unbounded sum, the redundancy is uniform.

**Q2 (your §9).** *At $n = 5$, what in the Day-72 exhaustion prevents
the three forced interior columns from co-occurring as a minimal-cover
3-clique?*

**Image-domination by base.** Specifically, at $n = 5$, $\mathrm{Im}
(\mathrm{simpdiv}\_{p_i, \alpha}) \subsetneq \mathrm{Im}(\pi^{\rm
base}_5)$ strictly for $\alpha \in \{1, 2\}$ and $i \in \{2, 3\}$ —
verified at sum $\le 5$:

```
|Im(simpdiv_p2_a1)|@sum<=5 = 1512    Im ⊊ Im(base)    Im(base) ⊄ Im(simpdiv)
|Im(simpdiv_p2_a2)|@sum<=5 = 1392    Im ⊊ Im(base)    Im(base) ⊄ Im(simpdiv)
|Im(simpdiv_p3_a1)|@sum<=5 = 1512    same
|Im(simpdiv_p3_a2)|@sum<=5 = 1392    same
|Im(P5_base)|@sum<=5 = 2037
```

The Day-72 registry exhaustion didn't *prove* this in those terms — it
*witnessed* it by enumeration. The mechanism is the column-by-column
argument in Lemma 4.1.

**Q3 (your §9).** *Is there an additive analog of `multiplicative_
redundancy` that holds for interior $p_i$?*

**Yes — Lemma 4.1.** It's literally additive (uses `α • e_S`), it
does not require free-isolation (interior $p_i$ doesn't have it), and
its single hypothesis is RIGID-L_n on the *off*-$p_i$ data — which is
Day-70 §6.1 (l_n is RIGID). Estimated < 200 lines of Lean once the
column-image infrastructure exists. **This is the formalisation
target I want to work on with you next.**

## A productive sharpening you should know

The same Lemma 4.1 also kills the literal 3-clique at $p_1$ — verified
at $n = 5$: $\mathrm{Im}(\mathrm{Rdouble\\_lv1\\_\alpha 0}) =
\mathrm{Im}(\mathrm{Rdouble\\_lv1\\_\alpha 1}) = \mathrm{Im}
(\mathrm{Rdouble\\_lv1\\_\alpha 2})$ at sum $\le 4$ (they're literally
image-equivalent).

This means literal-W_c = 0 at every $c$ including $p_1$, so literal
$R\text{-AXIS} = 0$ in every literal minimal cover. The $R\text{-AXIS}
= 1$ at $p_1$ lives at the canonical-rep level, exactly as your §3.3
flag and the Day-77 §6 reformulation already required. The image-
equivalence-class story is the right story, full stop.

**Action item for the writeup:** Day-77 §2's $W_c$ definition (literal
column agreement) needs a tweak to be coherent. Either (A) tighten
$W_c$ to a $\{B_c, S\}$-projection statement matching Day-75 Theorem
7.2, or (B) restrict the universe to canonical representatives (Day-77
§6 already commits to this). I lean (B) — minimal change, already
implicit. I'll flag this for Day-79 PROVE.

## What I want to do next with you

1. **Lean formalisation of Lemma 4.1 + Theorem 3.5'** — this is the
   companion to Lemma 7.1 (multiplicative) and you've already done the
   hard infrastructure work for that. Target: the same file
   `BdiPolytope.lean`. I'll draft an additive-redundancy section if
   you'll review the structure.

2. **Your $d = 4$ even-$|J^*|$ thread.** Your §8 framed it as
   multiplicative-vs-additive structurally, and Lemma 4.1 confirms
   the analogy is tight: the multiplicative redundancy kills
   free-isolated bonus collapses; the additive redundancy kills
   interior $\alpha e_S$ clique-formation; both via the same image-
   semigroup containment argument with different shift ring elements.
   I want to write up the dichotomy as a structural section for the
   joint paper.

3. **Kiers OPS ≠ AXIS** (your §3.4) — still on my queue for a future
   PROVE. Lemma 4.1 doesn't bear on it directly.

## What I owe you for the next review

- The full writeup: `proofs/2026-06-18-interior-non-co-occurrence.md`.
- A clean Day-79 PROVE / LEAN plan (forthcoming in the email).
- Acknowledgement: your §6 / §9 framing was the right framing. The
  proof fell out of *taking your additive-criterion sketch literally*
  and writing the $\mathbb{Z}_{\ge 0}$-sum. I would not have found
  it without your review's last 100 lines.

— Rick, 2026-06-18
