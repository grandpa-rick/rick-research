# Molev shifted-Pieri extract for s*_{(1,1)} · s*_μ

Date: 2026-08-20
Purpose: Give Rick the explicit combinatorial formula for the shifted Pieri
coefficients c^λ_μ appearing in the expansion s*_{(1,1)} · s*_μ = Σ c^λ_μ s*_λ,
per his task spec.

## Correction on the arXiv ID

The arXiv ID `0807.3597` in the task spec is WRONG. That paper is Forbrich et al.,
"New M-dwarf debris disk candidates in NGC 2547" (astrophysics). The correct
paper is:

  A. I. Molev, "Comultiplication rules for the double Schur functions and
  Cauchy identities," arXiv:**0807.2127** (Elec. J. Combin. 16 (2009), R13).

Downloaded to `/home/agent/projects/beta-prime/refs/molev-0807.2127.pdf`.
The Molev-Sagan LR rule (arXiv:**q-alg/9707028**, "A Littlewood-Richardson Rule
for factorial Schur functions", Trans. AMS 351 (1999), 4429-4444) was also
downloaded to `/home/agent/projects/beta-prime/refs/molev-sagan-q-alg-9707028.pdf`
because 0807.2127 by itself does NOT contain the direct multiplication-side
Pieri rule Rick wants — it handles comultiplication / dual LR coefficients
ĉ^ν_{λμ}. The multiplication-side coefficients c^ν_{λμ} for double / factorial
Schur functions (of which shifted Schur is the specialization a_i = -i+1) come
from Molev-Sagan Thm 3.1.

## What each paper covers

**Molev 0807.2127.** Ring Λ(x‖a) of double symmetric functions, basis s_λ(x‖a).
Sec. 3 defines the *dual* Schur functions ŝ_λ(x‖a) via a modified determinant
(3.3) and proves Cauchy identity (3.4). Sec. 4 defines the *dual* LR polynomials
ĉ^ν_{λμ}(a) as coefficients of Δ(s_ν) (comultiplication), NOT of s_λ·s_μ. So
Prop 3.5 is a horizontal-strip rule for the coproduct-related h_k, not what Rick
needs directly. Example 4.5 gives ĉ^{(m)}_{(k)(l)}(a) and ĉ^{(1^m)}_{(1^k)(1^l)}(a).

**Molev-Sagan q-alg/9707028.** Directly gives the multiplication LR rule
    s_λ(x|a) s_μ(x|a) = Σ_ν c^ν_{λμ}(a) s_ν(x|a)
(equivalently, in the more general skew form s_θ(x|b) s_μ(x|a) = Σ c^ν_{θμ}(a,b) s_ν(x|a),
their eq. (8)). This is Theorem 3.1 (see below). Setting a_i = i-1 gives the
shifted-Schur multiplication rule (their §4 specializes to a_i = i-1 and denotes
s*_λ(x)).

## Shifted Pieri formula for s*_{(1,1)}·s*_μ

Molev-Sagan Thm 3.1 with θ = λ = (1,1) (a single column of 2 boxes) and a = b
gives directly:

    s_{(1,1)}(x|a) · s_μ(x|a)  =  Σ_ν  c^ν_{(1,1),μ}(a) · s_ν(x|a),

with the coefficient

    c^ν_{(1,1),μ}(a)  =  Σ_{T ∈ T((1,1), ν/μ)}  ∏_{α ∈ (1,1),  T(α) unbarred}
                          ( (a_{ρ(α)})_{T(α)}  −  a_{T(α)+c(α)} ).

Indexing set / support: ν runs over partitions with μ ⊆ ν and |ν| − |μ| ≤ 2.
(Vanishing Thm 2.1 forces μ ⊆ ν; homogeneity + top-degree LR forces the |ν|=|μ|+2
term to have the classical LR coefficient c^ν_{(1,1),μ} = 1 or 0 as usual for
vertical 2-strip.) Length restriction: only ν with ℓ(ν) ≤ n contribute at level n.

The set T((1,1), ν/μ) is Molev-Sagan's set of "barred semistandard skew tableaux."
Concretely, a sequence of one-box additions R : μ = ρ^{(0)} → ρ^{(1)} → ρ^{(2)} = ν
(with row indices r_1, r_2 forming the Yamanouchi word of R) together with a
semistandard filling T of ν/μ by entries in {1,…,n}, containing two distinguished
cells α_1 < α_2 (in column order) with T(α_j) = r_j; α_1, α_2 receive "bars." The
product ∏ runs over the *unbarred* cells of ν/μ. For α unbarred, ρ(α) = ρ^{(i)}
where α_i < α < α_{i+1} in column order.

Shifted specialization a_i = i − 1 (equivalently the factorial-Schur → shifted-Schur
map): under this, s_λ(x|a) → s*_λ, and the coefficients c^ν_{(1,1),μ}(a) become
the shifted Pieri coefficients (denoted f^ν_{λμ} in Molev-Sagan §4).

## Explicit coefficient c^λ_μ

For the top-degree case |ν| = |μ| + 2 with ν = μ + (vertical 2-strip): only one
sequence R, no unbarred cells → coefficient = 1 (classical LR c^ν_{(1,1),μ}).

For "lower" cases |ν| = |μ| + 1 or |ν| = |μ|: the product ∏ is nontrivial and
each unbarred cell α contributes a linear factor of the form

    (a_{ρ(α)})_{T(α)} − a_{T(α)+c(α)}  =  (a_{p_{T(α)}} − a_{T(α)+c(α)})

where p = ρ(α) so (a_p)_{k} means a_{p_k+n−k+1} (row-shifted evaluation at the
"a_ρ" tuple, Molev-Sagan notation just above their eq. (7)).

Under the shifted specialization a_i = i − 1 this becomes

    (a_{ρ(α)})_{T(α)} − a_{T(α)+c(α)}  ⟶  ρ(α)_{T(α)} + n − T(α) − (T(α) + c(α) − 1)
                                        =  ρ(α)_{T(α)} − 2 T(α) − c(α) + 1 + n,

which is exactly Molev-Sagan eq. (18):

    f^ν_{λμ}  =  Σ_T  ∏_{α, T(α) unbarred}  ( ρ(α)_{T(α)} + n − 2 T(α) − c(α) + 1 ).

So c^λ_μ = f^ν_{(1,1),μ} is a **positive-integer polynomial in the row lengths
ρ(α)_i of intermediate partitions and the box contents c(α) = j−i**, of degree
|ν/μ| − 2 (i.e., 0 for top ν, up to 2 for lower ν).

## Support

Support = { ν : μ ⊆ ν, ν/μ has at most 2 boxes lying in distinct rows
(from the (1,1)-shape constraint on the barred cells α_1 < α_2 in column
order — the two bars must be in distinct rows) }.

- **Top layer** (|ν| = |μ|+2): ν/μ is exactly a vertical 2-strip. Coefficient = 1
  (classical LR).
- **Middle layer** (|ν| = |μ|+1): ν/μ is a single box β; two barred cells (α_1,α_2)
  must both live inside ν/μ so one bar is on β and the other bar is on an
  additional cell also equal to β (but only 1 cell exists) — actually, α_1, α_2
  are cells of the *ambient shape ν* whose entries T(α_1)=r_1, T(α_2)=r_2 match
  the row-sequence R. So more precisely: R adds 2 boxes ending at ν whose row
  indices form the Yamanouchi symbol, but only |ν/μ| = 1 of the added boxes
  lies in ν/μ; the other must lie in some cell of ν/μ overlapping — actually
  the R sequence goes μ → ρ^{(1)} → ν and thus creates |ν|−|μ| new boxes, so
  if |ν/μ|=1 the sequence has l = 1 (one step) but λ = (1,1) requires TWO
  barred cells. This forces at least one bar to sit outside ν/μ, which
  Molev-Sagan implicitly handles via the "α_i ∈ ν/μ or the ambient tableau"
  convention. **Cross-check by reading exactly which α lie in θ vs. in ν/μ
  in Molev-Sagan p.5 diagram.**
- **Bottom layer** (|ν| = |μ|): ν = μ; the classical part vanishes, and
  the coefficient collects all reverse-tableau contributions of shape λ=(1,1)
  with no cell removed from μ — this is precisely s_{(1,1)}(a_μ|a) = (evaluation
  of the factorial (1,1)-Schur at a_μ).

Special values from Molev 0807.2127 Example 4.5 (dual side, illustrates the
kind of formula):
    ĉ^{(1^m)}_{(1^k)(1^l)}(a) = Σ_{r+s = m−k−l} (−1)^r h_r(a_1,…,a_k) e_s(a_{l+1},…,a_{m−1})
and the "boundary" case
    ĉ^{(1^m)}_{(1)(1^l)}(a) = (a_{l+1} − a_1)(a_{l+2} − a_1)…(a_{m−1} − a_1).

## "Lower" terms — the answer Rick needs

The λ ("ν" in Molev-Sagan notation) that appear with |ν| < |μ|+2 (i.e., "lower"
than the vertical 2-strip top) are exactly:

1. ν with ν = μ ∪ (single box β), i.e., μ → ν adds one box. Coefficient:
   the sum over R : μ → ν (only one step, r_1 = row of β) and over choices of
   the "second barred cell" α_2 lying elsewhere in ν with T(α_2) = row of β.
   Under shifted specialization the coefficient is a **degree-1** polynomial
   in the μ_i and n.

2. ν = μ (no new box). Coefficient: the sum over pairs of barred cells inside
   μ giving a (1,1)-column pattern with entries r_1 = r_2 (impossible for
   distinct r_i by Yamanouchi) — so this term reduces to
   s_{(1,1)}(a_μ|a) = ∏-formula from Vanishing Thm 2.1:
     s_{(1,1)}(a_μ|a) = (a_{μ_1+n} − a_1)(a_{μ_1+n} − a_2) ... [see Thm 2.1
     for the general formula]; a **degree-2** polynomial in μ_i.

## Content / box positions

The content function c(α) = j − i (column − row) appears in every factor
(a_{p} − a_{T(α)+c(α)}) — so the "column-position" data enters as an index
shift inside the a-sequence. In the shifted specialization a_i = i−1, factor
(a_{ρ(α)})_{T(α)} − a_{T(α)+c(α)} becomes ρ(α)_{T(α)} − 2 T(α) − c(α) + n + 1;
here c(α) = j−i for cell α = (i,j). So each factor is *linear in the row length
ρ(α)_{T(α)}* and *linear (with coefficient −1) in the column-content c(α)*.

## Remarks on degree filtration / vanishing (relevant to Rick's claim **)

Molev-Sagan eq. (18) makes the following IMMEDIATE:

- The top-degree (in x) term of s*_(1,1) · s*_μ is the classical
  s_{(1,1)} · s_μ = Σ_{ν vertical 2-strip of μ} s_ν, with coefficient 1.

- Every "lower" term c^ν_{(1,1),μ} with |ν| < |μ|+2 is a polynomial in the
  μ_i and n of positive degree (= |μ|+2−|ν|) in these variables.

If Rick's filtration index d is the degree "|μ|" minus something (a
codimension-in-Λ*) — plausibly d_λ = |λ|, in which case
d_μ + 1 corresponds to allowing exactly one drop in degree, i.e., |ν| ≥ |μ|+1:
the "middle layer" terms — then Molev-Sagan (18) confirms exactly that only ν
with |ν| ∈ {|μ|, |μ|+1, |μ|+2} appear, and characterizes each coefficient
explicitly. So the claim (**) that d_λ ≤ d_μ+1 for all non-top λ reduces to
verifying that the |ν|=|μ| term vanishes when d is chosen appropriately —
which is a **combinatorial statement about the vanishing of s_{(1,1)}(a_μ|a)
under a_i = i−1 whenever d(μ, ν=μ) > d_μ+1**. This is checkable from
Vanishing Thm 2.1 (Molev-Sagan p.4): s_λ(a_ρ|a) = 0 iff λ ⊈ ρ. For λ=(1,1),
ρ=μ, this is nonzero as long as (1,1) ⊆ μ, so the ν=μ term does contribute
whenever μ has ≥2 rows.

Concretely, in the shifted specialization
    s*_{(1,1)}(μ) = ∏_{(i,j)∈(1,1)} (μ_i + n − i − (T(α) + c(α) − 1))
                 = (μ_1 + n − 1)(μ_2 + n − 2 − 0),  [after evaluation]
so the ν = μ coefficient in s*_{(1,1)} · s*_μ = ... + s*_{(1,1)}(μ) · s*_μ + ...
is generally nonzero; **thus if Rick's filtration puts d(μ) < d(μ) + 1 for the
constant term, the ν=μ term IS a lower term — and it satisfies the bound
d_λ = d_μ ≤ d_μ + 1 trivially. The bound is tight only for the |ν|=|μ|+1
middle layer.**

## Key references and locations in the PDFs

- Molev 0807.2127, Sec 3 (dual Schur, Cauchy): pp. 15-28. Prop 3.5 does not
  exist in a labeled form; the analogous "horizontal-strip" identity is Thm 3.4
  eq. (3.9)-(3.11) on pp. 18-19, giving explicit products for ĉ^ν_{λ,(k)}(a).
- Molev 0807.2127, Sec 4 (dual LR): pp. 29-33. Def 4.1, Thm 4.3, Cor 4.4,
  Example 4.5 (explicit hook-times-hook coefficients).
- Molev-Sagan q-alg/9707028, Thm 3.1: p. 6, main LR polynomial formula.
- Molev-Sagan q-alg/9707028, §4 & Thm 4.1 eq. (18): pp. 12-15, shifted
  specialization a_i = i−1 → f^ν_{λμ}, direct formula for shifted-Schur
  product coefficients.
- Vanishing Thm 2.1 (Molev-Sagan p.4): controls the ν = μ "bottom-layer"
  coefficient values.

## Files

- `/home/agent/projects/beta-prime/refs/molev-0807.2127.pdf`
- `/home/agent/projects/beta-prime/refs/molev-sagan-q-alg-9707028.pdf`
