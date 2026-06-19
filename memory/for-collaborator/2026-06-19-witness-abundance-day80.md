# Day 80 PROVE — Witness Abundance (Theorem 9.2)

**Date:** 2026-06-19
**Status:** PROVED, n-uniform, n >= 5.
**Files:**
- Proof: `proofs/2026-06-19-witness-abundance-day80.md`.
- Verification: `code/2026-06-19-witness-abundance-day80/verify_single_column_witness.py`.

## One-paragraph summary

Theorem 9.2 lifts Day-79 CODE Task 3's empirical "17 of 17 AII
rays at n=6, 21 of 21 at n=7 support an F-feasible single-ray
witness" finding to a structural, n-uniform theorem — and reveals
that the right witness is even simpler than expected. For every
piece column c at level n, every interior or boundary i, every
alpha in {1, 2}, the **single-column witness** W with W^c =
T_{i,alpha} = e_{B_i} + alpha*e_S (rest zero) is F-feasible AND
has Im(W) = Z_>=0 . T_{i,alpha} contained in Im(pi_base). Hence
every AII extreme ray r supports a witness — pick any column c in
r and use W^c = T.

## What's new vs. Day 79 Theorem 9.1

Theorem 9.1 used a SPECIFIC 2-column witness (prefix[1] = e_{B_i},
long[2] = alpha*e_S). Theorem 9.2 says: EVERY column placement of
T_{i,alpha} works, including all 3n - 1 (even) or 3n (odd) AII
piece columns. The witness construction is more permissive, the
image is smaller (Z_>=0 . T vs. Z_>=0 . e_{B_i} + Z_>=0 . alpha . e_S),
and the proof is shorter.

The Day-79 theorem 9.1 droppability conclusion goes through with
ANY of the new 1-column witnesses, by the same argument
(Day-78 Lemma 4.1 + image containment).

## Structural punchline

The PROVE.md hypothesis suggested ray-specific structure:
"each AII ray r has the property r(prefix i) in {0, e_{B_i},
e_{B_i} +/- e_S}, and r(long j) in {0, e_S}..."

The proof bypasses this. The only ingredients are:

1. **T_{i,alpha} BDI for interior/boundary i + alpha <= 2**
   (Day-79 §3, no n-dependence beyond i <= n-1 giving P_{n-1} = 2).
2. **T_{i,alpha} = pi_base^{prefix[i]} + alpha * pi_base^{long[n]}**
   (RIGID-L_n + base canonical, both proved n-uniformly).
3. **Every piece column appears in >= 1 AII ray** (combinatorial,
   trivially n-uniform).

No ray-specific structure required. The single-column witness
realises ray-image(r) = T for every r containing c, and 0 for
every r missing c. Both are BDI.

## Implications for Lyra & Clio

**For Clio (LR coefficients / symmetric functions side):**
The Day-79 CODE Task 3 "abundance" statistic is now structural,
not coincidental. Whenever a target lattice point T is BDI AND is
a Z_>=0-combo of base-canonical columns, EVERY column hosts a
single-column witness. This pattern likely generalises beyond the
AII / BDI setting — to any coverage problem where the target is
a small lattice point and the base piece's columns generate the
target. Worth looking for analogues in the symmetric-function /
LR-coefficient setting.

**For Lyra (systems side):**
The verification script `verify_single_column_witness.py` checks
~3500 individual single-column witnesses across n=5..12; the
runtime is sub-second because each check is "is this BDI?" on at
most 2 lattice points (T_{i,alpha} and 0). The structural
simplification is also a computational simplification — Theorem
9.2 is what you'd want to formalise in LEAN first.

## Open follow-ups (Day 81+)

1. **Joint multi-alpha replacement.** Can a single 1-column piece
   replace ALL alpha in {0, 1, 2} carriers at one (n, i)?
   First guess: probably not with one column, because the image is
   Z_>=0 . T_{i,alpha} and you can't reach T_{i,1} from T_{i,2}
   via nonneg combinations. But two columns might. Open.

2. **Image-essentiality without pi_base.** The H3-OP question from
   Day 76 §6.4. Theorem 9.2 doesn't address this — it assumes
   pi_base in the cover.

3. **LEAN target.** Lemma 9.2.A (single-column witness F-feasibility)
   is the immediate next LEAN target — estimated ~50 lines on top of
   the BdiPolytope.lean scaffolding. Even shorter than Day-79's
   Lemma 3.A target (the 2-column version), and a strict
   strengthening.

## Send to Robin?

This is a clean, well-bounded result. Worth a brief end-of-day note
saying "Day-80 PROVE closed: Theorem 9.2 is a 5-line corollary of
Theorem 9.1's algebraic content. Single-column witnesses everywhere,
n-uniformly verified at n in {5..12}." No urgent action item.

— Rick, Day 80 PROVE, 2026-06-19
