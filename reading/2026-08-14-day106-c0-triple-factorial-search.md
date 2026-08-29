# Day 106 — Identifying N(R) = R!·(R+1)!·(2R)!

Task from Rick: what does N(R) = R!·(R+1)!·(2R)! count, and does it
identify Q_{2R}(R−2, R, R) via a known identity?

## Values (R = 1..8)

    R=1:                                 4
    R=2:                               288
    R=3:                           103,680
    R=4:                       116,121,600
    R=5:                   313,528,320,000
    R=6:             1,738,201,006,080,000
    R=7:        17,715,744,653,967,360,000
    R=8:   306,128,067,620,555,980,800,000

## OEIS

No hit. Queried the sequence with 3, 4, 5, 6, 7 consecutive terms and
with a leading `1` prepended. All returned "No results". The individual
`(2R)!`, `R!(R+1)! = A010790` etc. of course exist, but not the product.
So this sequence — as an object of study — appears to be new to OEIS.

## Clean factorizations

The most striking rewrite:

    N(R) = Cat(R) · [H(R,R)]²             (*)

where Cat(R) = (2R)!/(R!(R+1)!) is the Catalan number and
H(R,R) = R!·(R+1)! is the hook-length product of the 2×R rectangle
(equivalently, H(R,R) = (2R)! / f^{(R,R)}).

Equivalent forms:

    N(R) = (2R)! · H(R,R)                 = (2R)! · R!·(R+1)!
    N(R) = f^{(R,R)} · [H(R,R)]²          = (# SYT of (R,R)) · [hook prod]²
    N(R) = (R+1) · C(2R,R) · (R!)⁴
    N(R) = C(2R+1, R) · (R!)⁴  · [via (R+1)C(2R,R) = C(2R+1,R)]

So the "SL_3 flavor" is misleading; the natural home for this number is
the **2-row rectangle (R,R)**, not a 3-row shape.

## Combinatorial interpretations

The cleanest reading is via (*):

  * Cat(R) is the number of standard Young tableaux (SYT) of the 2×R
    rectangle (equivalently, Dyck paths of length 2R, non-crossing
    matchings of 2R points, etc.).
  * H(R,R) = R!·(R+1)! is the product of hook lengths of the 2×R
    rectangle.

Thus N(R) counts

    { (T, φ, ψ) : T ∈ SYT(R,R),  φ, ψ : cells of (R,R) → ℤ chosen from
                  the hook-product measure },

or, equivalently, pairs (σ, ψ) where σ ∈ S_{2R} and ψ is a labeling of
the cells of (R,R) by a hook-product ordering — since (2R)! = f^{(R,R)}·H(R,R)
means N(R) = (2R)!·H(R,R) is |S_{2R}| times a hook product.

None of these interpretations is *canonical* enough to yield an
immediate closed-form identity; N(R) is not a "named" combinatorial
number.

## What N(R) is NOT

  * NOT the # SYT of any 3-row rectangle (R+1, R+1, R+1) or (R, R, R):
    those grow much more slowly (A005789 / A005791 family:
    f^{(R,R,R)} = 2(3R)!/(R!(R+1)!(R+2)!) → 1, 5, 42, 462, …).
  * NOT the Weyl dimension of any small SL_3 highest-weight module.
    For SL_3, dim V_{(a,b,c)} = (a−b+1)(b−c+1)(a−c+2)/2 is a cubic,
    while N(R) grows like (2R)!.
  * NOT the Mehta / Macdonald constant for A_2 at k=R:
    that constant is (2R)!(3R)!/(R!)², which is a *different* triple
    product.
  * NOT a Selberg-integral value at (a,b,c) = (1,1,R) for N=3.
  * NOT any Barnes G-function value G(k) for a simple k.

## Reading of Rick's Q_{2R}(R−2, R, R)

Rick's polynomial Q_j (the `M_j_sym` in
`/home/agent/projects/code/2026-07-10-hk-three-var-fit.py`, lines 89–119)
is built from a Jacobi–Trudi-style determinant

    det[ (x_i)_{k_j} ]_{i,j=1..3},        x = (a+2, b+1, c),

weighted-summed over 3-row partitions μ contributing to a specific
e_2-power expansion. At (a,b,c) = (R−2, R, R) the arguments become

    x = (R, R+1, R)

which has **x_1 = x_3 = R**. The bare Jacobi–Trudi determinant with two
coinciding rows/columns vanishes; the non-vanishing value of Q comes
from the sum structure and the (2R)! prefactor cancels the near-zero
Vandermonde. This is exactly the mechanism by which a Weyl-character
evaluation "at the wall" — a formally singular point on the
representation-theoretic parameter space — can be finite and factorial.

The specific product N(R) = (2R)! · R! · (R+1)! looks like

    (2R)! · [hook product of (R,R)]

with the (2R)! coming from the normalization in M_j and the H(R,R)
coming from the surviving 2×R sub-determinant after the R↔R coincidence
degeneration. A concrete proof path:

  1. Recognize x = (R, R+1, R) as a doubly-degenerate specialization of
     the Jacobi–Trudi/character determinant.
  2. Expand the determinant by *the two rows i=1, i=3* which share x=R;
     one gets a factor (x_1 − x_3) = 0 in a generic direction and a
     residue (∂/∂x_1) contribution.
  3. The residue reduces the 3×3 determinant to a 2×2 determinant in the
     surviving pair (R, R+1), which is exactly the SL_2 Jacobi–Trudi for
     the shape (R, R). Its evaluation gives Cat(R) up to normalization.
  4. Combined with the (2R)! and hook-normalizations already present in
     M_j, this reproduces (2R)!·R!·(R+1)!.

If Rick can trace the degeneration in step 2 explicitly, he should end
up with N(R) = f^{(R,R)} · H(R,R)² automatically.

## Recommended follow-up

  * Try (a,b,c) = (R−1, R, R) and (R, R, R) at Q_{2R} numerically. If
    the values are (R!)²(R+1)!(2R+1)!/… or similar, we have a
    two-parameter family suggesting a **degeneration on a codimension-1
    wall** of the SL_3 parameter space.
  * Look for the same product in the Naruse/Morales–Pak–Panova
    hook-length formulas for *skew* shapes — the factor H(R,R)²
    is suggestive of the shape (R,R) / ∅ appearing twice, e.g.
    in a d-complete or piecewise-linear formula.
  * Since no OEIS hit exists, if the identity holds it may be
    publishable as a new evaluation of an SL_3 Jacobi–Trudi determinant
    at a wall.

## Summary

  * OEIS: no match.
  * Cleanest factorization: **N(R) = Cat(R) · [R!(R+1)!]²**, i.e.
    (# SYT of 2×R rectangle) × (hook product of 2×R)².
  * Best interpretation: this is not a "named" 3-row / SL_3 count; it is
    the natural product one gets when a 3×3 Jacobi–Trudi determinant
    degenerates to a 2×2 (i.e. two of the three x_i coincide), leaving
    behind the 2-row hook data of shape (R,R) plus the (2R)! prefactor.
  * Candidate proof path: identify (a,b,c)=(R−2,R,R) as a wall in Rick's
    Q polynomial, apply an "l'Hôpital / row-expansion" degeneration
    argument, and use the SL_2 Jacobi–Trudi for (R,R) to close.
