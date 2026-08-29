---
title: Day 118 — Lemma X check — DISPROVED by dimension counting
status: NEGATIVE RESULT. Lemma X (span{s*_mu : d_mu <= k} = F^k) FAILS for k >= 2. Naive-independence-of-top-parts (A) fails (rank pinned at 2), and the span itself is a proper subspace of F^k for k >= 2 by an unavoidable dimension mismatch. The Day 117 §6 "Remaining subtlety" is not a subtlety — the naive completion via Lemma X is IMPOSSIBLE. But StructB still survives: it only needs the specific element S_j in F^j, not the full filtration compatibility. Also discovered: bar s*_mu(s) has s-degree exactly (mu_2 + mu_3) mod 2, and clean sign/leading-coefficient formulas.
---

# Day 118 — Lemma X Check

## §0. Statement recapped

    (Lemma X)   span_Q { s*_mu : ell(mu) <= 3, d_mu <= k }  =  F^k

as Q-subspaces of Lambda_3 = Q[e_1, e_2, e_3], where

  * d_mu = mu_1 + floor((mu_2 + mu_3) / 2)     (Day 118 closed form),
  * F^k = { f in Lambda_3 : deg_t f(e_1=t+s, e_2=(s+1)t, e_3=t^2) <= k },
        equivalently (u, pi)-wdeg(f) <= k with weights (1, 1, 2) on
        (e_1, e_2, e_3), by the Day 117 §2 Characterization Lemma.

The ⊆ direction is trivial.

Task: verify (or refute) the ⊇ direction for k <= 10.  Equivalently,
show that the top-t-parts {bar s*_mu : d_mu = k} are Q-linearly
independent in gr_k = F^k / F^{k-1} for every k.

## §1. Result: Lemma X FAILS for k >= 2

**Two independent reasons:**

### (A) Naive independence fails, rank pinned at 2

For each k, compute bar s*_mu(s) := [t^k] s*_mu(u=t, y+c=s, yc=t) in Q[s].
Compute the rank of {bar s*_mu(s) : d_mu = k}.

    k    #{mu : d_mu = k}    rank    dim gr_k^F    status
    0                    1       1              1    INDEP
    1                    2       2              2    INDEP
    2                    3       2              4    DEP (1 relation)
    3                    5       2              6    DEP (3 relations)
    4                    7       2              9    DEP (5 relations)
    5                    9       2             12    DEP (7 relations)
    6                   12       2             16    DEP (10 relations)
    7                   15       2             20    DEP (13 relations)
    8                   18       2             25    DEP (16 relations)
    9                   22       2             30    DEP (20 relations)
   10                   26       2             36    DEP (24 relations)

**Rank stays at 2** for all k >= 2, while the count of mu grows
quadratically (~k^2/4).  Lemma X's equivalent independence form FAILS.

### (B) Dimension counts diverge

Since {s*_mu}_{ell(mu)<=3} is a Q-basis of Lambda_3, we have
dim span_Q{s*_mu : d_mu <= k} = #{mu : d_mu <= k}.  Compare to
dim F^k = #{(i_1,i_2,i_3) : i_1 + i_2 + 2 i_3 <= k}:

    k    #{mu : d_mu <= k}     dim F^k    gap
    0                     1           1      0
    1                     3           3      0
    2                     6           7      1
    3                    11          13      2
    4                    18          22      4
    5                    27          34      7
    6                    39          50     11
    7                    54          70     16
    8                    72          95     23
    9                    94         125     31
   10                   120         161     41

The gap grows quadratically (~k^2/3).  span{s*_mu : d_mu <= k} is a
PROPER subspace of F^k for every k >= 2 — Lemma X (span version) FAILS
by an unavoidable dimension mismatch, independently of any subtle
independence considerations.

**Both (A) and (B) confirm: Lemma X as stated is FALSE.**

## §2. Structural reason for the failure

For any e-monomial:

    [t^k]  e_1^{i_1} e_2^{i_2} e_3^{i_3} |_{e_1 -> t+s, e_2 -> (s+1)t, e_3 -> t^2}
       =  (s+1)^{i_2}   if  i_1 + i_2 + 2 i_3 = k,
          0             otherwise.

Hence gr_k^F embeds into Q[s] as span{(s+1)^{i_2} : 0 <= i_2 <= k},
a (k+1)-dimensional subspace.

But bar s*_mu(s) turns out empirically to have s-degree AT MOST 1 for
every mu tested.  So its image sits inside the 2-dim subspace spanned by
{1, s} = {(s+1)^0, (s+1)^1 - 1}.  The available (s+1)^{i_2} for
i_2 = 2, 3, ..., k are inaccessible from any bar s*_mu.  This explains
rank_A pinned at 2 and gap_B growing.

## §3. Bonus: closed-form observations on bar s*_mu(s)

Numerically verified for all 120 partitions mu with ell(mu) <= 3 and
d_mu <= 10:

**Observation 1 (s-degree).**  deg_s bar s*_mu(s) = (mu_2 + mu_3) mod 2.

  In particular:
    * When mu_2 - mu_3 is EVEN, bar s*_mu(s) is a CONSTANT (in Z).
    * When mu_2 - mu_3 is ODD, bar s*_mu(s) is LINEAR: alpha_mu s + beta_mu.

**Observation 2 (even-parity value).**  For (mu_2 - mu_3) even,
    bar s*_mu(s) = (-1)^{(mu_2 - mu_3) / 2}   in Z.

  In particular, the value is 1 or -1 and doesn't depend on mu_1 at all.
  Verified 68/68 even-parity cases.

**Observation 3 (odd-parity leading coefficient).**  For (mu_2 - mu_3) odd,
    alpha_mu = leading s-coeff of bar s*_mu(s) = (-1)^{(mu_2 - mu_3 - 1)/2}
                                                   * (mu_2 - mu_3 + 1)/2.

  E.g., mu_2 - mu_3 = 1 gives +1; = 3 gives -2; = 5 gives +3; = 7 gives -4.
  Verified 52/52 odd-parity cases.

**Observation 4 (odd-parity constant term).**  beta_mu depends on all three
parts of mu in a not-yet-fully-characterized way.  Examples for (mu_2 -
mu_3 = 1):
    (1,1,0) → s + 0        (a=1, const=0)
    (2,1,0) → s - 1        (a=2, const=-1)
    (2,2,1) → s - 2        (a=2, b=2, c=1)
    (3,1,0) → s - 1        (a=3, const=-1)
    (3,2,1) → s - 3        (a=3, b=2, c=1)
    (3,3,2) → s - 4        (a=3, b=3, c=2)
    (4,1,0) → s - 1        (a=4, const=-1)
    (5,4,3) → s - 7        (a=5, b=4, c=3)

  When c = mu_3 = 0: constant = -(a - 1) = -(mu_1 - 1) for a >= 2.  Yes:
    (2,1,0)→-1, (3,1,0)→-1, (4,1,0)→-1, (5,1,0)→-1, ...
  When c > 0, more complex.

**Structural interpretation.** The top-t-part of s*_mu picks up ONLY
those e-monomials in the e-expansion of s*_mu with i_1 + i_2 + 2 i_3 =
d_mu AND i_2 in {0, 1}.  All higher-i_2 contributions CANCEL in the
top-t-part.  This is a strong hidden identity in the shifted-Schur
polynomials.

## §4. Explicit failure relations at small k

For k = 2 (1 relation):

    bar s*_{(1,1,1)}(s) = bar s*_{(2,0,0)}(s) = 1

  Meaning:  s*_{(1,1,1)} - s*_{(2,0,0)}  has (u,pi)-wdeg <= 1.

For k = 3 (3 relations):

    bar s*_{(2,1,1)}  =  -bar s*_{(2,2,0)}
    bar s*_{(3,0,0)}  =   bar s*_{(2,1,1)}
    bar s*_{(3,1,0)}  =   bar s*_{(2,1,1)} + bar s*_{(2,2,1)}

  All three collapse to "value = ±1" (constant), with only the linear
  bar s*_{(3,1,0)} = bar s*_{(2,2,1)} identity involving the odd-parity
  bar s*_mu's (equalizing their linear parts).

For k = 4 (5 relations):

    bar s*_{(2,2,2)}  =  bar s*_{(3,1,1)}          (both 1)
    bar s*_{(2,2,2)}  = -bar s*_{(3,2,0)}          (1 vs -1)
    bar s*_{(2,2,2)}  =  bar s*_{(4,0,0)}          (both 1)
    bar s*_{(2,2,2)} + 2 bar s*_{(3,2,1)} + bar s*_{(3,3,0)}  =  0
    -2 bar s*_{(2,2,2)} - bar s*_{(3,2,1)} + bar s*_{(4,1,0)}  =  0

  The last two are the "one linear relation" combining two odd-parity
  bar s*_mu's.

All relations are of the form: "constant-valued bar s*_mu's are all ±1
(depending only on mu_2 - mu_3 parity), and there's a further linear
relation among the linear bar s*_mu(s)'s at each k."

## §5. Consequence for the StructB program

**Lemma X is DEAD.**  It cannot be used to close the Day 117 §6
"Remaining subtlety."

**Why this doesn't kill StructB.**  The proof target is NOT "E : F^k ->
F^{k+1} is well-defined on all of F^k in the s*_mu basis representation";
it is only that the SPECIFIC element

    S_j = sum_{|mu|=2j, ell(mu)<=3} K_{mu',(2^j)} s*_mu

lies in F^j.  This one specific linear combination MAY still land in
F^j through hidden cancellations, even though the ambient F^j is much
larger than span{s*_mu : d_mu <= j}.

**Positive rephrasing.**  What we actually need is: the specific
combination sum_{|mu|=2j} K_{mu',(2^j)} bar s*_mu(s) = 0 at every
t-degree > j.  This is a specific-coefficient identity about the
Kostka-transposed weighted sum, not a general span/rank statement.

**Alternative routes forward.**

  1. **Direct computation of S_j.**  Combine Day 117 §7's closed form
     (S_j|_{e_3=0} = prod_i (e_2 - i e_1)) with an explicit expression
     for the e_3-corrections and prove deg_t <= j directly.

  2. **Route V.**  Verify A_j := ds_j / (y - c) has (u,pi)-wdeg
     exactly j + 2 by direct manipulation of the ds_j determinant — no
     s*_mu basis needed.

  3. **Weaker per-mu Lemma via Kostka pattern.**  Prove:  for
     K = K_{mu',(2^j)}, the linear combination sum K bar s*_mu(s) has
     top-t-degree contribution vanishing.  Since bar s*_mu(s) is
     ±1 or alpha_mu s + beta_mu (Obs. 1-3 above), this becomes an
     explicit identity in the Kostka numbers:

          sum_{mu: d_mu = j, mu_2-mu_3 even}  K_{mu',(2^j)} * (-1)^{(mu_2-mu_3)/2}
        + sum_{mu: d_mu = j, mu_2-mu_3 odd}   K_{mu',(2^j)} * beta_mu   =  0,

          sum_{mu: d_mu = j, mu_2-mu_3 odd}   K_{mu',(2^j)} * alpha_mu  =  0.

     Two Kostka identities to prove (per j), rather than an unattainable
     general-position lemma.

## §6. Files

  * `code/day118/verify_lemma_X.py` — script producing this report.
  * `/tmp/lemma_X_verify.log` — full output log.

## §7. Summary

**Lemma X (span{s*_mu : d_mu <= k} = F^k) is FALSE for k >= 2.**

* Naive independence (A): rank stays pinned at 2 for k >= 2.
* Span dimension (B): #{mu : d_mu <= k} grows as k^2, but dim F^k grows
  as k^3/12, so the gap grows quadratically.

**But StructB survives.**  Only Day 117 §6's E-filtration-completion
argument breaks.  The (u, pi)-wdeg <= j property of the SPECIFIC element
S_j = sum K_{mu',(2^j)} s*_mu is still empirically true (verified in
Day 117-118) and admits proofs via routes 1-3 in §5 above.

**Bonus structural discoveries** (verified for 120 partitions,
d_mu <= 10):

  * deg_s bar s*_mu = (mu_2 + mu_3) mod 2.
  * Even parity: bar s*_mu(s) = (-1)^{(mu_2-mu_3)/2}, independent of mu_1.
  * Odd parity: leading coeff alpha_mu = (-1)^{(mu_2-mu_3-1)/2} *
    (mu_2-mu_3+1)/2.

These give strong control on the top-t-behavior of shifted-Schur
polynomials — likely useful for Route 3 (Kostka-identity closure) above.

— Compute agent for Rick, Day 118, Lemma X CHECKED and REFUTED.
