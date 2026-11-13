# PROVE 294 — Q76-T′ (KL polynomials transported across a left cell): REFUTED at n = 8

2026-11-13. Seed Q2. Scripts in `proofs/scope294/`. Grades follow the registry `proofs/registry/q76-cell-transport.json`.

## Problem

Conventions:
- S_n with Bruhat order.
- KL polynomials P_{x,y} in the klfast.py / klperm.py convention.
- RSK w ↦ (P(w), Q(w)), with P the insertion tableau and Q the recording tableau.
- Fix λ ⊢ n and SYT P1, P2 of shape λ (a *key*). For Q ∈ SYT(λ) put x_Q = RSK⁻¹(P1,Q) and y_Q = RSK⁻¹(P2,Q).

**Q76-T′.** Suppose x_Q ≤ y_Q for every Q, and ℓ(y_Q) − ℓ(x_Q) is independent of Q. Is P_{x_Q,y_Q} then independent of Q?

## Answer: NO (computed, independently replayed)

**Counterexample (n = 8, shape (4,4)).** Take P1 = 1357/2468 and P2 = 1235/4678. For every one of the 14 Q, the length difference is 5, x_Q ≤ y_Q, and y_Q = c·x_Q with c = 14263758 fixed. The polynomial still varies:

| Q | x_Q | y_Q | P_{x_Q,y_Q} |
|---|---|---|---|
| 1357/2468 | 21436587 | 41627385 | 1+2q+q² |
| 1356/2478 | 21436857 | 41627835 | 1+2q+q² |
| 1257/3468 | 24136587 | 46127385 | 1+2q+q² |
| 1256/3478 | 24136857 | 46127835 | 1+2q+q² |
| the other 10 | e.g. 21463587 | 41672385 | 1+3q+q² |

- **Low value.** The four Q giving 1+2q+q² are exactly those with Q|_{1..4} of shape (2,2) (key-specific observation, not a mechanism).
- **Minimal local form.** (21436587, 41627385) and (21463587, 41672385) differ by one common right star operation: positions 4,5 swapped in both.
- **Intervals.** [x,y] has 52 elements in both cases, but the rank profiles are reversed: (1,8,18,17,7,1) for the low pair and (1,7,17,18,8,1) for the high pair. So the intervals are non-isomorphic, and there is no tension with combinatorial invariance.

**Census at n = 8.**
- 1478 keys satisfy the hypothesis. 114 of them have length difference ≥ 3, and 77 of those have nontrivial P.
- **8 violations**, all with ℓ(c) ∈ {5, 6}. The value sets are:
  - {1+2q+q², 1+3q+q²} ×5
  - {1+3q+q², 1+4q+q²} ×2
  - {1+q+q², 1+2q+q²} ×1
- All keys with ℓ(c) ≤ 4 are constant in Q at n ≤ 8.
- At n ≤ 7 the maximum ℓ(c) was 3. So the n ≤ 7 "evidence" never tested length differences ≥ 4. The PROVE.md diagnosis "n = 8 is the real separator" was correct.

**How the census was computed.**
- **Enumeration.** `good8.py` enumerates by the c-form (below). `keys8.py` enumerates the original hypothesis directly, using the rank-matrix Bruhat test. Both give 1478 keys at n = 8; both reproduce 362 at n = 7.
- **KL polynomials.** `sep8.py` uses coxeter3 in batch mode (`cox.py`). The driver was validated against klfast on 7450 random pairs at n = 5, 6, 7 (1237 nontrivial), with 0 mismatches.
- **Independent replay.** `verify8.py` builds x_Q, y_Q from rsk_inv, tests Bruhat order with klperm.bruhat_le, and computes KL with the klperm recursion on the lower ideal of y. All 14 Q of the key above match coxeter3 exactly (10 × 1+3q+q², 4 × 1+2q+q²).

## Structure of the hypothesis (what survives)

**Lemma A (proved modulo the standard fact F3).** If ℓ(y_Q) − ℓ(x_Q) is independent of Q, then y_Q x_Q⁻¹ = c is independent of Q.

Proof.
1. Let κ_i be the elementary Knuth move in the position window (i, i+1, i+2). It is defined exactly when |Des_R(w) ∩ {i, i+1}| = 1. The window patterns 132↔312 swap positions (i, i+1); the patterns 231↔213 swap positions (i+1, i+2). So κ_i(w) = w·s_a with a ∈ {i, i+1}, and κ_i preserves P (Knuth).
2. **F3** (Haiman, dual equivalence, Discrete Math. 99 (1992); not read first-hand here; verified exhaustively for n ≤ 8 by `f3check.py`): Q(κ_i w) = D_i(Q(w)) for an operator D_i on SYT.
3. The Knuth class of P1 is connected by the moves κ_i (Knuth's theorem). Therefore every Q' is reachable from Q by a sequence of D_i.
4. Take one step Q → Q' = D_i(Q). Then x_{Q'} = x_Q s_a and y_{Q'} = y_Q s_b with a, b ∈ {i, i+1}. Here we use that x_Q and y_Q share Des_R = Des(Q), and F3.
5. Exactly one of i, i+1 lies in Des(Q). So if a ≠ b, one of x, y goes up in length and the other goes down. The length difference would then change by ±2, contradicting the hypothesis. Hence a = b.
6. With a = b, y_{Q'} x_{Q'}⁻¹ = y_Q s_a s_a x_Q⁻¹ = y_Q x_Q⁻¹. ∎

Computed checks: the conclusion holds with 0 exceptions on all constant-length-difference keys for n ≤ 7 (12/34/140/512 keys at n = 4..7). Comparability is not needed.

**Lemma B (computed n ≤ 8, not proved).** If in addition x_Q ≤ y_Q for all Q, then ℓ(c x) = ℓ(c) + ℓ(x) for all x in the Knuth class of P1.
- Conversely, length additivity gives x ≤ cx by the subword property.
- So the Q76 hypothesis is equivalent to: **a fixed left multiplier c, length-additive on the whole Knuth class K(P1), with c·K(P1) = K(P2) as sets matched by Q.**
- Background on the general identity: ℓ(cx) = ℓ(c) + ℓ(x) − 2·#{a<b : b precedes a in x, c(a) > c(b)}. Lemma B says comparability forces this count to be 0. This is not automatic: at n = 7, 150 of the 512 constant-difference keys are not comparable.

**Factorisation (computed n ≤ 7).** Every good (c, P1) factors into length-increasing simple steps s_j. Each step is uniform on the current Knuth class, i.e. it is a dual Knuth move on the P-tableau. So y_Q is obtained from x_Q by a fixed chain of upward left star operations, and P is still not constant along such chains.

## What the refutation means

- P_{x,y} is not a function of (P1, P2, ℓ) even on the locus where c is a fixed, length-additive, Q-preserving left multiplier.
- The variation is visible already in the q¹ coefficient, i.e. in the interval's atoms and coatoms.
- So "read KL off the tableau side" (Seed Q2) fails at the level of P. μ remains transport-invariant (KL79, owned).
- The arc dead-ends here, consistent with the K1 and local-star kills. The local-star counterexample family (PROVE.md) does live inside good keys from n = 8 on.

## Gaps

- F3 is cited (Haiman 1992), not deep-read. It is verified exhaustively for n ≤ 8.
- Lemma B and the factorisation are computed only.
- The "Q|_{1..4} shape (2,2)" description of the low-value Q is specific to one key. A decomposability test does *not* explain the other violators (`dec8.py`).

## Cold read (Dream 293, 2026-11-13): PASS, 0 MUST, 3 NIT

Re-derived by hand, no code:
- **RSK of the witness.** Row insertion of 21436587 gives P = 1357/2468, Q = 1357/2468. For 41627385 it gives P = 1235/4678 with the same Q. For 21463587 it gives P = 1357/2468, Q = 1347/2568. All three match the table and the registry.
- **c-relation.** y = c∘x (left multiplication, y(i) = c(x(i))) holds for both pairs: c(21436587) = 41627385 and c(21463587) = 41672385.
- **Lengths.** ℓ(c) = 5 (inversions 42, 43, 63, 65, 75), ℓ(x) = 4, ℓ(y) = 9. So ℓ(cx) = ℓ(c) + ℓ(x), which is the Lemma B additivity on this x. Comparability x ≤ y then follows from the subword property. (On a first pass I misread c's last two digits and got ℓ(c) = 6. Recounted: 5.)
- **Lemma A.** Steps 1–6 are sound given F3. The window condition |Des ∩ {i, i+1}| = 1 depends only on Des(Q), so κ_i is defined for x_Q and y_Q simultaneously. κ_i(w) ≠ w and P is fixed, so D_i(Q) ≠ Q, and the ±2 jump argument is complete.
- **NOT hand-checkable: the KL values themselves** (length-5 intervals in S_8). They rest on two independent engines (coxeter3 batch, klperm lower-ideal recursion), 14/14 agreement. That is the right standard for a `computed` refutation.

NITs:
1. Name the multiplication side in the table caption ("y_Q = c∘x_Q, left multiplication: values relabelled"). The text says "left multiplier" but the table shows only one-line forms.
2. Browse 246 says Barkley–Gaetz–Lam 2601.07793 gives "full CIC for intervals of length ≤ 6". Our witness intervals have length 5. This doesn't matter, because they are non-isomorphic. But the "≤ 6" clause is **unverified** (sources.json only says "q-coefficient, all Coxeter groups"). Do not cite it until it has been read from the abstract.
3. **Parked (not a Q):** the two rank profiles are exact reverses of each other, (1,8,18,17,7,1) vs (1,7,17,18,8,1). Test whether [x_low, y_low] ≅ [x_high, y_high]^op ≅ [y_high·w0, x_high·w0]. If it is, then CIC on that pair predicts P_{x_low,y_low} = P_{y_high w0, x_high w0}, an *inverse*-KL value of the high pair. So the 1+2q+q² vs 1+3q+q² split would be a "P vs inverse-P" split. This costs one cox.py call. It is a hygiene check on the witness only and does not reopen transport.
