# PROVE 283: independent check of the twin verdicts for the (6,4,3,3) pairs 352, 353, 364, 365 (2026-11-08)

Grade: **certificate-replayed, conditional on one COMPUTED input**: μ(inst 0) = μ(inst 1) = 1 from `dyer2.c`
(`out_in0b.txt`, `out_in1b.txt`; Dyer formula, validated to S_6 only). Everything else is either star-certified and replayed
by the wake282/prove281 verifier, or checked by the extension described below. The recall-only KL inputs are the usual ones:
Lemma S, F1, P_{a,b} = P_{a⁻¹,b⁻¹}, and right-star invariance of μ.

Census index = index into `wake282/sieve16.json`. Cell Q_0 = [[1..6],[7..10],[11..13],[14..16]].

Files:
- `verifyn_ext.py`: a copy of `wake282/verifyn_u.py`. The only change is that a cert entry may carry an `ext` field (diff in §4).
- `certs16_6433_ext.json`: the 4 pair certificates.
- `tvc_findpath.py`, `tvc_rpaths.json`: the right-star path search (search only, not trusted).
- `out_verify_ext.txt`, `out_tvc_controls.txt`: the outputs.

## (a) Pairs 353 and 364 are TWIN. CONFIRMED, conditional on μ(inst 0/1) = 1.

| census | λ | A = Des P_x | P_x | P_z (Des) | l(x), l(z) |
|---|---|---|---|---|---|
| 353 | (6,4,3,3) | {2,3,4,6,7,8,12,13,14} | [[1,2,6,11,12,16],[3,7,10,13],[4,8,14],[5,9,15]] | [[1,2,3,7,12,13],[4,5,6,11],[8,9,10],[14,15,16]] ({3,7,13}) | 63, 81 |
| 364 | (6,4,3,3) | {2,3,4,8,9,10,12,13,14} | [[1,2,6,7,8,12],[3,9,13,16],[4,10,14],[5,11,15]] | [[1,2,3,7,8,9],[4,5,6,13],[10,11,12],[14,15,16]] ({3,9,13}) | 53, 73 |

**What a TWIN verdict needs.** The conditions come from Lemma A, the PROVE 280 Step 2 completeness argument and PROVE 281 §3.
1. x ≠ z are in one cell, ∅ ≠ L(z) ⊆ L(x) = A. The verifier asserts this. L(z) ⊆ int A was also checked: True for both pairs.
2. μ(y, z) ≥ μ(y, x) for every y in the cell with L(y) ⊄ A. Only y with μ(y, x) ≠ 0 matter, and those form the set (i) ∪ (ii):
   - (i) the elements s·x in the cell with L(sx) ⊄ A, which have μ = 1;
   - (ii) the elements (U, Q_0) with Des U ⊋ A and μ(y, x) ≠ 0.

   The verifier enumerates this set itself, using its own SYT enumeration and its own RSK, and requires it to match the cert's y-list.
3. Since every such μ(y, x) = 1, condition 2 says μ(y, z) = 1 for each y in the set.

**Status of each condition.**
- **353.** There are 5 (i)-elements (s = 1, 5, 8, 11, 14). Each has μ(y, z) = 1 from a left-star certificate (paths of length 17–19), as already in `wake282/certs16_6433.json`.
  - There is one (ii)-element, y = [1,5,9,11,15,16,4,8,10,14,3,7,13,2,6,12] with l = 58 and Des P_y = A ∪ {10}.
  - μ(y, x) = 1 is star-certified (Ucert path L1, L2, L3, L8).
  - μ(y, z) is the only missing entry, because the star orbit is exhausted. (P_y, P_z) is literally open26 inst 0.
- **364.** There are 6 (i)-elements, with μ(y, z) = 1 star-certified for 5 of them.
  - The sixth, s = 6, is y = [1,5,7,11,15,16,4,6,10,14,3,9,13,2,8,12] with l = 54 = l(x)+1.
  - The same y is also the unique (ii)-element: Des P_y = A ∪ {6}, and μ(y, x) = 1 holds with gap 1.
  - μ(y, z) is the missing entry. (P_y, P_z) is literally open26 inst 1.

**Linking the missing μ to the computed one, checked rather than assumed.**
- `tvc_findpath.py` found a **right-star path** from (y, z) in Q_0 to the exact dyer2 input pair:
  - 54 steps for inst 0, ending at `in0b.txt`, l = 34, 53;
  - 19 steps for inst 1, ending at `in1b.txt`, l = 35, 54.
- Right stars fix the P-tableaux. Both elements share Q, and D_R depends only on Q, so the pair stays in D_R at every step.
- By Lemma S applied to inverses, μ is constant along the path.
- `verifyn_ext.py` replays the path with the verifier's own rstar. It asserts that the endpoint equals the `in*b.txt` permutations literally, and reads the μ coefficient from `out_in*b.txt` after checking:
  - lx and lz against its own length function;
  - mu_index = (lz − lx − 1)/2;
  - that the coefficient list is consistent.
- Independently, P(xd) = open26 Px, P(zd) = open26 Pz, and Q(xd) = Q(zd), for both instances.

**Replay (`out_verify_ext.txt`).** All 4 certificates replay **OK**:

| census | μ(y, z) over (i) ∪ (ii) | verdict |
|---|---|---|
| 352 | [0,0,0,1,0,0,1] | NO |
| 353 | [1,1,1,1,1,1] | **TWIN** |
| 364 | [1,1,1,1,1,1,1] | **TWIN** |
| 365 | [0,0,0,0,0,1] | NO |

**Negative controls (`out_tvc_controls.txt`).** The verifier **rejects** each of these broken certificates:
- 353 flipped to NO, and 364 flipped to UNDECIDED (verdict mismatch);
- a truncated right-star path, and the inst-1 data substituted for inst 0 (endpoint ≠ ext pair);
- the ext y dropped (y-set mismatch);
- the dyer output edited to "mu 0" (coefficient inconsistency).

So, given μ(inst 0) = μ(inst 1) = 1, the census changes from 112/296/2 to **114/296/0**.

## (b) Pairs 352 and 365 refute Q68-ii-kills. CONFIRMED, conditional on the same μ.

| census | A | P_x | P_z | l(x), l(z) | parity |
|---|---|---|---|---|---|
| 352 | {2,3,4,6,7,8,12,13,14} | [[1,2,6,10,11,12],[3,7,13,16],[4,8,14],[5,9,15]] | as 353 | 57, 81 | OK |
| 365 | {2,3,4,8,9,10,12,13,14} | [[1,2,7,8,12,16],[3,6,9,13],[4,10,14],[5,11,15]] | as 364 | 57, 73 | OK |

**Both are genuine candidate pairs.**
- They are in one cell with Des P_x = A.
- L(z) = {3,7,13}, resp. {3,9,13}, is contained in int A. Both checks are True.

**The (ii)-elements.**
- **352.** The (ii)-element is the *same* y as for 353: y = s_10·x, with l(y) = 58 = l(x)+1.
  - It is therefore also an (i)-element. Des P_y = A ∪ {10}.
  - μ(y, x) = 1 holds with gap 1, comparable (path []).
- **365.** The (ii)-element is the *same* y as for 364, with l(y) = 54 < 57.
  - Des P_y = A ∪ {6}.
  - μ(y, x) = 1 via the left-star path L4.
- In both cases (P_y, P_z) equals open26 inst 0, resp. inst 1. The z is the same permutation as in 353, resp. 364, and so is y. So μ(y, z) **is** the instance value: it is the same (y, z) pair, not merely the same P-tableaux. The verifier gives μ(y, z) = 1 at the ext entries.
- **Q68-ii-kills says "for every candidate pair and every (ii)-element, μ(y, z) = 0". It is therefore FALSE.**

Remarks:
- **353 and 364 are counterexamples too.** They are parity-OK candidate pairs with the same (ii)-element and μ(y, z) = 1. So 352/365 are not needed as witnesses; they are simply the NO-verdict witnesses.
- **Small inaccuracy in q68-consequences.md.** It says inst 1 is "(ii), also (i) s=6" for both 364 and 365. In fact it is also an (i)-element only for **364** (l(y) = l(x)+1). For 365 it is (ii) only. Inst 0 is likewise also the (i) s = 10 element for **352**, which the note omits. No verdict changes.
- **352 and 365 stay NO, for a different reason.** Other (i)-elements carry certified μ(y, z) = 0. For 352 these are s = 1 (F1 kill) and s = 5, 8, 11, 14 (incomparable). For 365 they are 5 incomparable kills at path length 0.

## (c) Consistency

It is consistent; in fact, the two conclusions are logically linked.
- Lemma A needs μ(y, z) ≥ 1 at every element of the (i) ∪ (ii) set. If a candidate pair has a non-empty (ii)-set, it can be a twin only if its (ii)-element does *not* kill. So "353 is a TWIN" already implies "ii-kills is false".
- The same (y, z) with μ = 1 serves both 352 and 353 (and both 364 and 365), because the pairs share z and y.
- 352 and 365 are NO only because of *other* (i)-elements whose μ(y, z) = 0 is independently certified. ii-kills concerns only the (ii)-element, which is why the same μ = 1 refutes it there as well.
- Also consistent with Theorem 2: (y, z) is a parity-failing candidate pair (l(y) ≡ l(z)) with μ = 1, so Lemma I fails at it, exactly as Theorem 2's contrapositive requires.

## 4. Verifier diff (`verifyn_ext.py` vs `wake282/verifyn_u.py`)

The changes are:
- the docstring;
- a new `extmu(ext, a, b)`;
- `replay(y, z, path, ext=None)`, which, when `ext` is present, replays the path and returns `extmu`;
- the `vals=` line, which now passes `k.get('ext')`.

The y-set enumeration, the Ucert replay, the endpoint rules and the verdict logic are byte-identical.
