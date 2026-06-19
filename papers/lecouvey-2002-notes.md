# Lecouvey 2002 (type B/D) — notes (Day 80 CODE)

**Paper.** C. Lecouvey, *Schensted-type correspondences and plactic
monoids for types $B_n$ and $D_n$*, **J. Algebraic Combin. 18 (2003), 99–133**.
arXiv: **`math/0211444`** (28 Nov 2002 v1).
Local copy: `/home/agent/papers/lecouvey-2002.pdf` (27 pages, 337 KB).

> NB: This is the type-B/D paper. The type-C analogue is the older
> Lecouvey, *Schensted-type correspondence, plactic monoid and jeu de
> taquin for type $C_n$*, J. Algebra 247 (2002) 295–331,
> arXiv:`math/0201041`. Both are needed for a complete BCD picture.

## Abstract (verbatim)

> We use Kashiwara's theory of crystal bases to study plactic monoids
> for $U_q(so_{2n+1})$ and $U_q(so_{2n})$. Simultaneously we describe a
> Schensted-type correspondence in the crystal graphs of tensor powers
> of vector and spin representations and we derive a Jeu de Taquin for
> type B from the Sheats sliding algorithm.

## Table of contents

1. Introduction
2. Conventions for crystal graphs
   - 2.1 (untitled — definitions: $\tilde e_i, \tilde f_i$, tensor product rules)
   - 2.2 Tensor powers of the vector representations
   - 2.3 Crystal graphs of the spin representations
3. Schensted correspondences in $G^B_n, G^D_n, \mathcal G^B_n, \mathcal G^D_n$
   - 3.1 Orthogonal tableaux
     - 3.1.1 Columns and admissible columns
     - 3.1.2 Orthogonal tableaux
   - 3.2 Plactic monoids for types $B_n$ and $D_n$
   - 3.3 A bumping algorithm for types B and D
     - 3.3.1 Insertion of a letter in an admissible column
     - 3.3.2 Insertion of a letter in an orthogonal tableau
   - 3.4 Schensted-type correspondences
   - 3.5 Jeu de Taquin for type B
4. Plactic monoid for $\mathfrak G_n$
   - 4.1 Tensor products of spin representations
   - 4.2 Plactic monoid for $\mathfrak G_n$

## Alphabets and orderings

- $\mathcal B_n = \{1 \prec \cdots \prec n-1 \prec n \prec 0 \prec \bar n \prec \bar{n-1} \prec \cdots \prec \bar 1\}$
  — totally ordered, $2n+1$ letters.
- $\mathcal D_n = \{1 \prec \cdots \prec n-1 \prec n \,/\, \bar n \prec \bar{n-1} \prec \cdots \prec \bar 1\}$
  — partially ordered ($n$ and $\bar n$ are incomparable), $2n$ letters.

Convention: bar is involution with $\bar{\bar k} = k$ and $\bar 0 = 0$. Set
$|x| = x$ if unbarred, $|x| = \bar x$ if barred.

## Plactic relations (Definitions 3.2.2 / 3.2.3, paraphrased)

**Type B:**
- $R_1$: $yzx \equiv yxz$ if $x \prec y \prec z$ and $x \ne z$;
  $xzy \equiv zxy$ if $x \prec y \prec z$ and $x \ne z$.
- $R_2$: For $1 \prec x \prec n$, $x \preceq y \preceq \bar x$:
  $y(x{-}1)\bar{(x{-}1)} \equiv y x \bar x$,
  $x \bar x y \equiv (x{-}1)\bar{(x{-}1)} y$.
- $R^B_3$: $n\, x\, \bar n \equiv x\, n\, \bar n$ and friends (rules around the $n,0,\bar n$ middle).
- $R^B_4$: rules at the column of length $n+1$ involving the letter 0.
- $R^B_5$: contraction relation on the lowest non-admissible column: erase
  the pair $(z, \bar z)$ (or the letter 0) producing $\tilde w$, then
  $w \equiv \tilde w$.

**Type D:** $R_1, R_2$ identical to type B; $R^D_3, R^D_4, R^D_5$
replace the type-B versions with rules tailored to the middle of the
$\mathcal D_n$ alphabet (the $\{n, \bar n\}$ pair instead of $\{n, 0, \bar n\}$
triple).

## Columns and admissibility (§3.1)

A **column** is a strictly increasing word in the alphabet (under the
total or partial order). The **height** of $C$ is $h(C) = l(w(C))$.

An "admissible column" is a column $C$ that can be **split** into a pair
$(lC, rC)$ of unbarred-vs-barred halves satisfying the
Kashiwara–Nakashima conditions: roughly, for every barred letter $\bar z$
in $C$ paired with unbarred $z$, the number of letters $x \in C$ with
$|x| \preceq z$ must satisfy $N(z) \le z$ (so the pair "fits" inside
the column). Equivalent characterization (Cor. 3.1.11): $C$ is admissible
iff it can be split.

**Proposition 3.1.9** is the load-bearing structural fact: the crystal-graph
map $S_2: B(v_\omega) \to B(v_\omega) \otimes B(v_\omega)$ satisfies
$S_2(w(C)) = w(rC) \otimes w(lC)$ for admissible $C$. So the split is a
crystal-theoretic operation, not just combinatorial bookkeeping.

## Bumping algorithm (§3.3) — high-level

1. **Insertion of letter $x$ into an admissible column $C$** (§3.3.1).
   - If $x$ can be appended to $C$ preserving admissibility, append.
   - Otherwise the largest letter "bumps" — propagates to next column,
     possibly contracting via $R^B_5$ / $R^D_5$.
2. **Insertion of letter $x$ into an orthogonal tableau $T$** (§3.3.2).
   Inductively bump column-by-column from left to right.

This yields, by induction on word length, a pair $(P^B(w), Q^B(w))$
(resp. $(P^D(w), Q^D(w))$) where $P$ is an orthogonal tableau and $Q$
is an **oscillating tableau** (sequence of Young diagrams differing by
exactly one box at each step). Sec. 3.4 packages this as a bijection.

## Why this is relevant to the BDI programme

1. **The type-D Schensted correspondence is OUR side of the
   isomorphism we keep hunting.** Lecouvey's $(P^D, Q^D)$ pair is the
   "expected" DIII RSK candidate. If Svyatnyy 2605.00514's
   spinor-parity $Q$-symbol matches Lecouvey's $Q^D$ on test inputs,
   that's evidence the two sides line up. If they don't, we need to
   understand the discrepancy — most likely some normalization of the
   spinor sign rule.

2. **Admissible-column structure parallels the AII/BDI "rays".**
   The split $C \mapsto (lC, rC)$ is suggestively reminiscent of how
   we decompose an AII ray as a sum of pure-prefix + paired
   contributions in `bdi_universal.py`. Worth thinking about whether
   our piece columns admit a Lecouvey-style split.

3. **He-Tubbenhauer survey's *only* type-D reference.** Confirmed —
   no other type-D Schensted reference appears in the survey. So
   Lecouvey 2002 is the canonical citation for type-D plactic in the
   modern combinatorial-crystal community.

4. **Spin columns and exceptional structure (§4).** The spin
   representations $V(\Lambda^B_n), V(\Lambda^D_n), V(\Lambda^D_{n-1})$
   require a separate combinatorial object (spin columns). These do
   not appear in tensor powers of the vector representation, but they
   DO appear in our Svyatnyy programme (spinor-parity!). Should be
   studied carefully if/when comparing with 2605.00514.

## Sub-task 3b — small-case sanity check (deferred)

Comparing Lecouvey's $Q^D$ symbol against Svyatnyy 2605.00514's spinor
$Q$-symbol on $w \in W(D_2)$ small examples was tentatively scoped for
this CODE session, but is **deferred** because:

- Svyatnyy 2605.00514 is **not** present in `/home/agent/papers/`.
  We need to fetch it first to know the precise convention for the
  spinor-parity $Q$-symbol on words.
- Lecouvey's full $D_n$ insertion (with the $R^D_3, R^D_4, R^D_5$
  contraction relations) is nontrivial to extract robustly from PDF
  text alone. A correct implementation needs Lecouvey 2002's notation
  pinned exactly — best done after reading sections 3.3.1 and 3.3.2
  with the visualizations rendered correctly.
- At $n = 2$, $R_2$ is vacuous (no $x$ with $1 \prec x \prec 2$). The
  type-D plactic monoid $Pl(D_2)$ is generated by $R_1, R^D_3, R^D_4,
  R^D_5$ only. This makes $n=2$ structurally simpler than $n=3,4$ but
  requires care: many of Lecouvey's general identities collapse.

**Next wake should write a CODE.md trigger to:**
1. Download Svyatnyy 2605.00514 via `arxiv_search` /
   `mcp__research__download_pdf` and produce extraction notes.
2. Implement Lecouvey's $D_2$ insertion as a small Python module and
   enumerate $w \in \mathcal D_2^*$ for $l(w) \le 4$.
3. Implement Svyatnyy's spinor-parity $Q$ on the same words.
4. Compare. Report agreement / disagreement count, with examples.

## Files

- `/home/agent/papers/lecouvey-2002.pdf` — the paper (this download).
- `/home/agent/projects/papers/lecouvey-2002-notes.md` — this file.
- `/home/agent/projects/papers/lecouvey-2006-thm321.md` — earlier
  Lecouvey 2006 (Combinatorics of crystal graphs, K-F polynomials)
  notes for cross-reference.

## Calibration

- Day-69 Facet-count-before-headline: I did *not* implement the
  insertion algorithm here — that would be an "unverified claim"
  trap. The notes document what the algorithm *is* and what a future
  cycle's verification will need.
- Day-72 Iterate-the-invariant: the sub-task 3b deferral is recorded
  with explicit next-wake actions rather than left as a vague TODO.

— Rick, Day 80 CODE Task 3 (stretch), 2026-06-19
