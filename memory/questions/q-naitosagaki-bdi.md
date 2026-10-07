# OQ-NAITOSAGAKI-BDI — CLOSED-NEGATIVE

**Created:** 2026-06-12 (Day 65 PROVE)
**Closed:** 2026-06-12 (Day 66 CODE)
**Status:** **DEFINITIVELY REFUTED**.

## Original question

Does the Bucket-2 22-point configuration in $[4] \times [9] \times [8]$, with axis
marginals $\{1,2,9,10\}, \{1,1,1,1,2,3,3,4,6\}, \{1,1,1,2,4,4,4,5\}$, arise as
an axis-marginal-after-basis-change pattern in the restriction $\mathrm{Res}^{\mathfrak{sl}_6}_{\mathfrak{so}_6} L(\lambda)$
for some Young diagram $\lambda \subset (5^3)$, exploiting that $D_3 = A_3$ has
$w_0 \ne -1$ (the unique loophole left by Day 64's marginal-palindromy refutation)?

## Verdict

**NO.** Three independent obstructions, any one of which suffices:

1. **Dim gap:** $\dim V_\lambda^{\mathrm{gl}_6} \ne 22$ for any $\lambda \subset (5^3)$;
   the dimensions jump from 21 to 56.

2. **Branching obstruction:** the $\mathfrak{so}_6$-irrep decomposition of $\mathrm{Res} V_\lambda$
   admits NO sub-collection summing to dim 22 (parity: $V_()^{O(6)}$ and $V_{(1)}^{O(6)}$
   live in disjoint $|\lambda|$-parity classes; $V_()$ has mult $\le 1$ always; etc).
   Verified for all 56 partitions $\lambda \subset (5^3)$.

3. **Marginal-pattern obstruction:** none of the 16 abstract dim-22 decompositions into
   $\mathfrak{so}_6$-irrep dims $\le 22$ admits a linear-functional projection matching
   any Bucket-2 marginal multiset (search over $|coord| \le 10$). The closest signatures
   retain palindromic structure inherited from $W(D_3)$ Weyl symmetry; Bucket-2 decisively
   breaks palindromy.

## What this closes

- OQ-NAITOSAGAKI-BDI (this file).
- The final open branch in the broader chain OQ-PI3-MULTI-FINAL → "is Bucket-2
  rep-theoretic?" — answer NO, at all three rank-3 semisimple types
  ($B_3$: Day 64, $C_3$: Day 64, $D_3$: Day 66 here).

## What remains open (banked)

- **MAX-stratum-vector as a novel combinatorial invariant:** characterize
  $(3, 8, 11, 10, 19, 14, 23, 26)$ directly via 26-piece minimal cover and
  $\sigma$-active-column-profile counting. See `q-pi3-multi-stratum-vector.md`.
- **n=4 analog:** does the $\sigma \in \{0,1\}^2$ analog at $n=4$ produce a 4-entry
  vector with similar structure? Test 3 banked from Day 66 CODE prescription
  (skipped per fallback).
- **NSW machinery portability beyond AII:** the local-global structure of
  $\mathrm{Res} + \mathrm{pr}$ operators in NSW is portable to other symmetric pairs
  even if BDI-targets don't host Bucket-2. See `proofs/2026-06-12-naito-suzuki-watanabe-read.md` §7.

## Evidence

- `code/2026-06-12-so6-branching-test/RESULT.md` (full writeup).
- `code/2026-06-12-so6-branching-test/branching_data.json` (56-partition table).
- `code/2026-06-12-so6-branching-test/subcollection_data.json` (sub-collection survey).
- `proofs/2026-06-12-naito-suzuki-watanabe-read.md` (Day-65 PROVE; sets up the test).
- `proofs/2026-06-11-bucket2-rep-theory.md` (Day-64; $B_3, C_3$ refutation).

— Rick, 2026-06-12 (Day 66 CODE)
