# PROVE 283: what μ = 1 at open26 instances 11, 13, 14 means for Q68 (2026-11-08)

Grade: **computed** cross-references, plus one-line proofs where marked. The μ = 1 values come from
`estimate-results.md` (Dyer formula, validated only to S_6). They are **not** independently verified here.
Scripts: `q68xref.py` (output `q68xref.json`), `q68feat.py`.

Indexing: the instances are 0-based indices into `prove282/open26.json`. I confirmed this from the `mu_inst*.json` files.
For each one, rsk(x)[0] = Px, rsk(z)[0] = Pz, Q(x) = Q(z), and l(z) − l(x) is 15, 13 and 13.

## Q1. What the instances are in Q68 terms

Each instance (x, z) is itself a **census candidate pair**: it is in `pfail.json`, the 206 parity-failing pairs.
- inst 11 is census pair 319, λ = (5,5,4,2).
- inst 13 is census pair 94, λ = (4,4,4,3,1).
- inst 14 is census pair 103, λ = (4,4,4,3,1).

All three are verdict NO by parity. Census full-cell lengths are 59/82, 71/90 and 67/88.

**None of them is a (ii)-instance, or an (i)-instance, of any S_16 candidate pair.**
- The full-key join on (λ, P_y, P_z) over every (i) and (ii) element in `sieve16.json` gives no hit for 11, 13 or 14.
- The only open26 instances that are (ii)-instances are **0 and 1**.
  - Inst 0 is the (ii)-element of pairs 352 (NO) and 353 (UNDECIDED); for **352** it is also the (i), s = 10 element.
  - Inst 1 is the (ii)-element of pairs 364 (UNDECIDED) and 365 (NO); it is also the (i), s = 6 element for **364 only**.
  - [Corrected PROVE 284 per twin-verdict-check.md §b; no verdict changes.]
  - These are the (6,4,3,3) pairs.

**Proof that 11, 13, 14 cannot be (ii)-instances.** All three are *tight*: A = N[L(z)].
- inst 11: N[{1,5,10,15}] = A.
- inst 13: N[{1,5,9,13}] = A.
- inst 14: N[{3,7,11,15}] = A.

A (ii)-instance (y, z) for a candidate pair (x′, z) needs N[L(z)] ⊆ L(x′) ⊊ L(y). So L(y) ⊋ N[L(z)], which means the pair is never tight.
As an independent check, direct SYT enumeration finds no T of shape λ with Des T ⊊ A and L(z) ⊆ int Des T. The count is 0 for all three.

**So Q68-ii-kills is NOT falsified.** Only the x-free Lemma I is (pending verification).

**Sharpening (one-line proof).** Theorem 2 only needs Lemma I on **non-tight** parity-failing pairs, i.e. L(x) ⊋ N[L(z)]. Call this Lemma I′.
- At S_16, 37 of the 206 pairs are non-tight: 35 are toolkit-killed and 2 are open.
- The 2 open ones are exactly instances 0 and 1.
- Lemma I′ is untouched by the new data.

## Q2. The S_16 census

No verdict depends on Lemma I or on ii-kills.
- TWIN verdicts are star-certified: every relevant y has μ(y, z) = 1.
- NO verdicts come from parity (Lemma P), from (i)/(ii) kills with certified μ(y, z) = 0, or from the 5 toolkit certificates for (5,5,3,3). Those certificates use the Layer Lemma, Lemma S and incomparability, not Lemma I.
- The 2 UNDECIDED pairs were never declared NO by Theorem 2.

The value μ(x, z) for a census pair never enters its own verdict.
- Lemma A quantifies over y with L(y) ⊄ L(x), which excludes x and z.
- Lemma P's proof does not use μ(x, z).

So pairs 319, 94 and 103 stay NO, and **no verdict changes. The census stays 112 / 296 / 2.**

The two undecided pairs hinge on exactly one μ each. All their other elements have μ(y, z) = 1:
- pair 353 is TWIN ⟺ μ(inst 0) = 1;
- pair 364 is TWIN ⟺ μ(inst 1) = 1.

Instances 0 and 1 are evacuation mirrors of each other, so μ(inst 0) = μ(inst 1) and the two pairs get the same verdict.
- If that μ is 1, then 352/365 show that **ii-kills is false**: a genuine (ii)-element of a genuine parity-OK pair has μ(y, z) = 1. The census would become 114 / 296 / 0.
- If it is 0, both pairs are NO and the census becomes 112 / 298.

The prior that the answer is 0 is weaker now: the evidence "every decided Lemma-I instance is 0" is gone. **Computing inst 0 is the decisive next run.** Its min gap is 19 (estimate table); the interval size has not been measured.

## Q3. Theorem 1

Theorem 1 is not contradicted. It concerns (ii)-elements y of parity-failing pairs, where l(y) ≡ l(z), and it uses only "μ ≠ 0 ⇒ odd gap".
The new instances have odd gaps: 15, 13 and 13 in the chosen cells, and 23, 19 and 21 in the census cells. Parity is cell-independent. So μ = 1 is allowed.
Remark 2(b) is also consistent: |L(x)∖L(z)| = 6, 7 and 7, and x < z.

## Q4. Structure

**Mirror pairs.** Evacuation (w₀-conjugation) pairs up open26 as 0↔1, 2↔3, 4 (self), 5↔6, …, 11↔12, 13↔14, …, 25 (self).
- So 13 and 14 are *one* datum. Their identical P and interval profiles are a free consistency check.
- μ(inst 11) = 1 implies μ(inst 12) = 1 (mirror; not separately computed).
- Net: 2 independent orbits, 4 instances with μ = 1.

**Shared features.** All three are tight, L(z) consists of 4 singleton runs including an end node, and the runs of A are (2,3,3,2) or (2,3,3,3).
None of this separates them:
- Tightness also holds for 145 of the 180 killed pairs.
- At the same (A, L(z)) there are toolkit-killed pairs of the same shape. For example, (4,4,4,3,1) at inst 13's (A, L(z)) has one KILL and one OPEN.
- There are also other open pairs: 2/3 for 11, and 9/10, 19–22 for 13.

**What actually separates them.** Only "primitive", which holds by construction of open26: x < z in every cell and no Young layer coincides.
The 3 instances were chosen for their small gap, so this is a selection, not a pattern. The other 21 open instances are uncomputed.

## Status changes to propagate (for Rick)

- Lemma I as stated: FALSE at S_16 if the Dyer computation is confirmed.
- Q68-ii-kills: still open.
- Lemma I′ (the non-tight version): still open, and sufficient for ii-kills.
- The "Crown U: Lemma I = Stembridge arc-exclusion" identification (Dream 282) needs re-examination.
