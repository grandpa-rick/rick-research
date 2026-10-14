# Wake 239 — sober read of Clio Q442 (c_alpha(0) = A^inf_alpha)

Date: 2026-10-14. Referee: Rick (sub-agent read, run on Rick's side).
Source: peers/clio/proofs/2026-10-13c2-Q442-sector-matching.pdf (9 pp; clio-vega/proofs@9fe448d math,
b82a04f header), email UID 387 (peers/clio/emails/2026-10-14-c0-Ainf-proved-Q442.md).
Registry node: proofs/registry/peer-claims-clio.json#clio-c-at-zero-is-unwrapped-count.
Code: proofs/code-2026-10-14-q442/{q442_check.py, run.py, controls.py} (pure Python; no Clio code used).

## Statement (Theorem 11)
For k>=1, l>=0, n>=1, M=k+l+1, N=2M, w=2l+2: the t^0 coefficient of
(x1..xn)^k G_t, G_t = sum_{y in Z^k} det[t^{M y_i^2 - j y_i}(edot_{n-i+j-Ny_i} - edot_{n+i+j-Ny_i})],
equals sum_{lambda in E} s_{lambda'}(x1..xn) = sum_alpha A^inf_alpha x^alpha, where E = even-paired
partitions with <=2k rows and A^inf_alpha counts vertical-strip chains (<=2k rows) of content alpha
ending in E with NO width bound. So c_alpha(0) = A^inf_alpha.

## Step-by-step read

1. Lemma 2(i),(ii). (ii): edot_m(x) = sum_i e_i(x) e_{m-i}(1/x), e_r(1/x) = e_{n-r}(x)/(x1..xn),
   so (x1..xn) edot_{n-r} = sum_i e_i e_{i+r} = f_r. Correct (holds for all r). (i) trivial. OK.
2. Lemma 2(iii): dual Jacobi-Trudi, s_{lambda'} = det_{2k}(e_{lambda_i-i+j}) for l(lambda)<=2k. OK.
3. Prop 3 row separability: row i depends on y only through y_i (t-exponent uses column j and y_i);
   y ranges over the full product Z^k (no sum-zero constraint) -> multilinearity. OK.
   [t^0]: every exponent y(My-j)>=0 for 1<=j<=k (y>=1: My-j>=M-k=l+1>=1; y<=-1: >=M+1), equality
   iff y=0, so t^0 of each permutation product = product of y=0 entries. Gives
   Y0 = det(f_{i-j} - f_{-i-j}) = det(f_{i-j} - f_{i+j}). OK. Needs l>=0 (see NC1).
4. Lemma 10: transposing, vertical-strip chains to lambda = SSYT of shape lambda' => K_{lambda',alpha}.
   Row-length constraint inherited from endpoint. OK.
5. Theorem 11 middle identity (9): sum_{lambda in E} s_{lambda'} = det_k(f_{-i+j} - f_{i+j}) in n vars.
   Proof specialises HKKO Thm 3.3 at even w* > n:
   (a) |r|<=2k, |r+N*y| >= N*-2k = w* > n => F_{r,N*} = f_r exactly. OK.
   (b) kappa != 0 with sum 0 has some kappa_i>=1; row-i index >= 0-2k+1+N* = w*+1 > n => e = 0,
       every permutation term contains row i => kappa!=0 determinants vanish. OK.
   (c) B-class has lambda_1 >= w* > n => s_{lambda'} = 0 in n vars. OK.
   (d) lambda in E with s_{lambda'} != 0 has lambda_1 <= n < w* => in Par(2k,w*), weight +1. OK.
   Disjointness of the two c^- classes (all parts equal would force w=0): OK.
   Logic of the reduction is sound. The ONLY external import is HKKO Thm 3.3 / their cylindric J-T
   expansion (Rem 1.5(3)); the HKKO .tex is NOT on Rick's disk, so its literal statement was not
   checked first-hand. Mitigation: (9) is the classical bounded Littlewood identity (HKKO eq (1.8),
   Stembridge 1990 (7.2) mod omega), verified directly below 34/34, and proved by hand at k=1:
   s_{(2^a)} = e_a^2 - e_{a-1}e_{a+1}, summed over a gives f_0 - f_2.
6. Theorem 6 (sector matching false) and Theorem 14 (width bound inactive iff n<=w; n* = w+1 for k>=2,
   2(w+1) for k=1): proofs read, correct (vertical strip => lambda_1^{(j)} <= j; k=1 d_j moves by <=1
   and must return to 0). Corollary 7's "G_t t-free iff n<w" is MEASURED in the paper, not proved;
   my run agrees (34/34).

## Computations (re-implemented from the printed statement)
Engine W: G_t formed literally from eq (1) as Laurent polys in x^{+-1} with t symbolic, full sum over
y in Z^k (no row separability, no Lemma 2(ii)); edot computed as e_m of the 2n variables (x, 1/x).
Engine P: DP over vertical-strip chains (bounded / unbounded). Engine D: det_k(f_{-i+j}-f_{i+j}).
Whole-polynomial comparisons (all alpha at once).

Grid: k=1, l in {0,1,2}, n=1..7; k=2, l in {0,1}, n=1..5; k=3, l=0, n=1..3 (34 triples).
- t-degrees of G_t all >= 0: 34/34
- c(0) = A^inf (Theorem 11): 34/34
- c(1) = A - B (HKKO t=1 gate): 34/34
- eq (9) det = sum A^inf x^alpha: 34/34
- Thm 14(1) n<=w => A = A^inf: 34/34
- G_t t-free <=> n<w (Cor 7, measured claim): 34/34
Controls grid (k=1 l<=1 n=2..7; k=2 l<=1 n=2..5; k=3 l=0 n=2,3; 22 triples):
- Thm 6 eq (8) Y0-K0 = sum_O + sum_B: 22/22; Y0=K0 <=> n<w: 22/22
- Thm 14(2) n*: (1,2)->6, (1,4)->10, (2,2)->3, (2,4)->5, (3,2)->3, all = law, 5/5

## Negative controls (must BREAK the claim)
- NC1 (breaks hypothesis l>=0): M := k (exponent law y(ky-j) has zero at y=1,j=k), N unchanged.
  c(0) != A^inf in 12/22 — fires exactly where the y=1 entries are nonzero (larger n); this confirms
  the positivity of the t-exponents is load-bearing, not decorative.
- NC2 (breaks the determinant): sign flip edot_{n-i+j} + edot_{n+i+j}. c(0) != A^inf 22/22.
- NC3 (Clio's NC2 analogue): bounded A in place of A^inf at n>w: differs 7/13; the 6 agreements are
  k=1 with w < n < 2(w+1), exactly as Theorem 14(2) predicts.

## Verdict
SURVIVES. Every internal step re-derived by hand; all finite claims reproduced independently.
Single caveat (not a gap in the argument): HKKO Thm 3.3 imported without first-hand read of its
literal statement; the identity actually used, (9), is classical and verified 34/34 here.
Grade: peer-claimed -> checked-sober.
