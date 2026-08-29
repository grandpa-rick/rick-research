# Day 94 PROVE — Digit-Sum Formula for β'(c): Structural Derivation Attempt

**Date:** 2026-07-13
**Registry target:** `beta-prime-digit-sum-formula` (currently `checked-sober`).
**Goal:** attempt derivation from the Day-88 three-variable Pochhammer factorisation.
**Style meta-rule:** be honest about gaps. Do not paper over.

---

## 0. Bottom line up front

I did **not** derive any of the three c mod 4 cases from the Sym-side
factorisation. The obstacle is not a missing lemma — it is a **structural
mismatch** between what the Day-88 factorisation gives us (LB_k as a
Legendre-formula-plus-Δ_k expression) and what the digit-sum formula
demands (a *particular* k* whose 2-adic count of "carries" at scale 4 is
exactly s_2(⌊c/4⌋) or s_2(⌊c/4⌋ − 1)).

**What I found:** the argmin k* is *not* c-uniform mod 4. It varies with
c in a way that is not simply periodic. The best I can offer this session
is an **enumeration of the structural obstacles** and a targeted diagnosis
of what the derivation would actually need.

**Registry recommendation:** stay `checked-sober`. Do not upgrade to
`sketched`. Details in §7.

---

## 1. What we have vs what we need

### 1.1 What the factorisation gives (Day 88, Lean-verified)

For 0 ≤ k ≤ c − 1 (clean regime):
```
h_k^{(c)}(a, b) = (a+3)_{c-1-k} · (b+2)_{c-1-k} · Q_k(a, b, c)      (★)
```
Setting L := c − 1 − k, Kummer/Lucas gives on any joint-Lucas-min (a, b):
```
v_2(h_k^{(c)}(a, b)) = 2 · v_2(L!) + v_2(Q_k(a, b, c))
                     = 2 · (L − s_2(L)) + v_2(Q_k(a, b, c))
                     [Legendre]
```
Define Δ_k^{(c)} := min v_2(Q_k(a, b, c)) over joint-Lucas-min shell.
Then LB_k^{(c)} = 2·(L − s_2(L)) + Δ_k^{(c)}.

### 1.2 What Day 91 F2 gives us as closed form

The k = 1 Delta:
```
Δ_1^{(c)} = v_2(c(c − 1)) = v_2(c) + v_2(c − 1).
```
Combined with L = c − 2:
```
LB_1^{(c)} = 2·((c − 2) − s_2(c − 2)) + v_2(c) + v_2(c − 1).
```

### 1.3 The claim

```
β(c) − β'(c) = D(c), where:
  c ≡ 0 (4):  D(c) = s_2(⌊c/4⌋) − 1
  c odd:      D(c) = 4 + 2 · s_2(⌊c/4⌋ − 1)
  c ≡ 2 (4):  D(c) = 1 + s_2(⌊c/4⌋ − 1)
```
Rewriting via β(c) = 2(c − 1) − s_2(c − 1):
```
β'(c) = 2(c − 1) − s_2(c − 1) − D(c).
```

### 1.4 What we'd need to derive it

For the SCP argmin k*(c), a c-uniform closed form
```
LB_{k*(c)}^{(c)} = β(c) − D(c) = 2(c − 1) − s_2(c − 1) − D(c),
```
followed by proof that this is the actual β'(c) (via distinct-min sum rule + witness UB).

---

## 2. The empirical argmin k* pattern

Reading off from the LB catalogs (Day 91 for c ∈ {5..11}, Day 93 extend
for c ∈ {12..17}) and SCP report (Day 89):

| c  | c mod 4 | ⌊c/4⌋ | k*(SCP argmin)      | L*=c−1−k*  | v_2(L*!)     | Δ_{k*}^{(c)} | LB=β' |
|----|---------|-------|---------------------|------------|--------------|--------------|-------|
|  5 | 1       | 1     | 2                   | 2          | 1            | 1            | 3     |
|  6 | 2       | 1     | 1                   | 4          | 3            | 1            | 7     |
|  7 | 3       | 1     | 3 (and 6)           | 3          | 1            | 4            | 6     |
|  8 | 0       | 2     | 1                   | 6          | 4            | 3            | 11    |
|  9 | 1       | 2     | 2                   | 6          | 4            | 1            | 9     |
| 10 | 2       | 2     | 5                   | 4          | 3            | 8            | 14    |
| 11 | 3       | 2     | 6                   | 4          | 3            | 6            | 12    |
| 12 | 0       | 3     | odd (1,3,5,7,9,11)  | various    | —            | —            | 18    |
| 13 | 1       | 3     | 6 (and 10)          | 6          | 4            | 8            | 16    |
| 14 | 2       | 3     | (many)              | various    | —            | —            | 21    |
| 15 | 3       | 3     | 7 (UNIQUE!)         | 7          | 4            | 11           | 19    |
| 16 | 0       | 4     | (many)              | various    | —            | —            | 26    |
| 17 | 1       | 4     | 2                   | 14         | 11           | 1            | 23    |

### 2.1 Immediate observations

**No c-uniform k* mod 4.** For c ≡ 3 mod 4:
- c=7: k*=3, 6
- c=11: k*=6
- c=15: k*=7 (unique)
The k* jumps unpredictably. Any hope of "k* = constant depending on c mod 4" is dead.

**For c ≡ 1 mod 4:**
- c=5: k*=2; c=9: k*=2; c=17: k*=2 — but c=13: k*=6, 10.
So k*=2 doesn't work uniformly either.

**c ≡ 0 mod 4:** multiple k* — many ties. This is consistent with D being small (D=0 at c=4,8,16; D=1 at c=12) — many carriers all sit at the same floor.

### 2.2 Structural interpretation

The argmin k* is **realised by whichever k minimises**
```
2·(c − 1 − k − s_2(c − 1 − k)) + Δ_k^{(c)}.
```
The Legendre part 2·(c − 1 − k − s_2(c − 1 − k)) decreases with k (up to the digit sum wobble). The Δ_k part varies unpredictably with k (per Rowland-Yassawi, Δ_k as a function of k has non-polynomial structure).

The argmin is therefore where **Δ_k is small enough to overcome the k-loss in the Legendre part**, and this crossover depends on c mod various powers of 2.

---

## 3. Case: c ≡ 0 mod 4 — the "simplest" case

D(4k) = s_2(k) − 1. Predicted β'(4k) = 2(4k − 1) − s_2(4k − 1) − s_2(k) + 1.

At c = 4k, β(4k) = 8k − 2 − s_2(4k − 1). Note s_2(4k − 1) = s_2(k − 1) + 2 (since 4k − 1 in binary is (k−1) followed by "11"). So:
```
β(4k) = 8k − 2 − s_2(k − 1) − 2 = 8k − 4 − s_2(k − 1).
```
And D = s_2(k) − 1, so:
```
β'(4k) = 8k − 4 − s_2(k − 1) − s_2(k) + 1 = 8k − 3 − s_2(k − 1) − s_2(k).
```

Verification at c = 4 (k=1): 8 − 3 − s_2(0) − s_2(1) = 5 − 0 − 1 = 4. ✓
At c = 8 (k=2): 16 − 3 − s_2(1) − s_2(2) = 13 − 1 − 1 = 11. ✓
At c = 12 (k=3): 24 − 3 − s_2(2) − s_2(3) = 21 − 1 − 2 = 18. ✓
At c = 16 (k=4): 32 − 3 − s_2(3) − s_2(4) = 29 − 2 − 1 = 26. ✓

So the closed form on odd c ≡ 0 mod 4:
```
β'(4k) = 8k − 3 − s_2(k − 1) − s_2(k).                       (♠)
```

### 3.1 What structural argument would give (♠)?

Reading the c=12 catalog: **every odd k gives LB = 18.**
- k=1: L=10, 2·v_2(10!)=16, Δ_1 = v_2(12·11) = 2. Sum 18. ✓
- k=3: L=8, 2·v_2(8!)=14, Δ_3 = 4. Sum 18. ✓
- k=5: L=6, 2·v_2(6!)=8, Δ_5 = 10. Sum 18. ✓
- k=7: L=4, 2·v_2(4!)=6, Δ_7 = 12. Sum 18.
- k=9: L=2, 2·v_2(2!)=2, Δ_9 = 16. Sum 18.
- k=11: L=0, 2·v_2(0!)=0, Δ_{11} = 18. Sum 18.

**Every odd k gives EXACTLY 18** = β'(12).

Even k give infinity (joint-Lucas-min set empty on the shell a+b≡0 mod 2 when L is odd).

**Key structural observation.** In the case c ≡ 0 mod 4, the closed-form conjecture reduces to proving:
```
For c ≡ 0 mod 4 and any odd k ≤ c-1:
   2·v_2((c-1-k)!) + Δ_k^{(c)} = 8k' − 3 − s_2(k'−1) − s_2(k')
   where k' := c/4.
```
This is a **c-uniform closed form for Δ_k on the odd-k slice at c ≡ 0 mod 4**. It says the LB is **k-independent on odd k** — a much stronger structural claim than we currently have proved.

**Explicit form:** at k=1, Δ_1 = v_2(c(c-1)) = v_2(c) since c-1 odd. For c=4k', v_2(c) = v_2(4k') = 2 + v_2(k'). And 2·v_2((c-2)!) = 2(c-2-s_2(c-2)) = 2(4k'-2-s_2(4k'-2)) = 8k'-4-2s_2(4k'-2). Now s_2(4k'-2) = s_2(2(2k'-1)) = s_2(2k'-1) = s_2(k'-1) + 1 (since 2k'-1 is odd, 1 lower bit + s_2(k'-1) in higher bits — actually more carefully: 2k'-1 has bit expansion of k'-1 shifted, plus a low 1... let me just check).

For k'=3: 4k'-2 = 10 = 1010. s_2 = 2. And s_2(k'-1) = s_2(2) = 1. So s_2(4k'-2) = s_2(k'-1) + 1 ✓.
For k'=4: 4k'-2 = 14 = 1110. s_2 = 3. s_2(k'-1) = s_2(3) = 2. s_2(4k'-2) = s_2(k'-1) + 1 ✓.
For k'=2: 4k'-2 = 6 = 110. s_2 = 2. s_2(k'-1) = s_2(1) = 1. ✓.

Good. So 2·v_2((c-2)!) = 8k' - 4 - 2(s_2(k'-1) + 1) = 8k' - 6 - 2s_2(k'-1).

Combining: LB_1 = 8k' - 6 - 2s_2(k'-1) + 2 + v_2(k') = 8k' - 4 - 2s_2(k'-1) + v_2(k').

Compare to target: 8k' - 3 - s_2(k'-1) - s_2(k').

Difference (target − LB_1) = 1 + s_2(k'-1) - s_2(k') + v_2(k').

Using s_2(k') = s_2(k'-1) - v_2(k') + 1 (standard identity: incrementing by 1 clears v_2(k') trailing 1s and adds one bit — wait, going k'-1 to k'): actually the standard identity is s_2(k'-1) = s_2(k') + v_2(k') - 1 (subtracting 1 from k' flips v_2(k') low zeros to 1s and clears the lowest 1). Rearranging: s_2(k') - s_2(k'-1) = 1 - v_2(k').

So target − LB_1 = 1 + (v_2(k') - 1) + v_2(k') = 2 v_2(k').

Hmm, this suggests LB_1 = target − 2v_2(k'), i.e., **LB_1 ≠ β' in general at c = 4k'**. It's off by 2v_2(k').

Check c=12 (k'=3, v_2(k')=0): LB_1 = 18 = target = 18. ✓ (2v_2(3) = 0)
Check c=8 (k'=2, v_2(k')=1): LB_1 should be 11 − 2 = 9. But catalog says LB_1(c=8) = 11. Contradiction!

Let me recompute LB_1 at c=8 directly. L = c-2 = 6, 2·v_2(6!) = 2·4 = 8. Δ_1 = v_2(8·7) = 3. Sum = 11. ✓

And target at c=8: 8·2 − 3 − s_2(1) − s_2(2) = 16 − 3 − 1 − 1 = 11. ✓

So both LB_1 = 11 and target = 11 at c=8. My arithmetic above was wrong. Let me redo it.

At c=8, k'=2: LB_1 formula gives 8·2 - 4 - 2s_2(1) + v_2(2) = 16 - 4 - 2 + 1 = 11 ✓.
Target: 8·2 - 3 - s_2(1) - s_2(2) = 16 - 3 - 1 - 1 = 11 ✓.

Difference: 0. But I derived target − LB_1 = 2v_2(k') = 2. Error in my algebra somewhere.

Redoing: LB_1 = 8k' - 4 - 2s_2(k'-1) + v_2(k'). Target = 8k' - 3 - s_2(k'-1) - s_2(k'). At k'=2: LB_1 = 16 - 4 - 2·1 + 1 = 11. Target = 16 - 3 - 1 - 1 = 11. Equal. Then:

Target − LB_1 = -3 + 4 - s_2(k'-1) + 2s_2(k'-1) - s_2(k') - v_2(k')
             = 1 + s_2(k'-1) - s_2(k') - v_2(k')
             = 1 + (v_2(k') - 1) - v_2(k')     [using s_2(k')-s_2(k'-1) = 1-v_2(k')]
             = 0.

So actually **LB_1 = target at c = 4k' for all k' ≥ 1** (when c ≥ 4). This gives:
```
For c ≡ 0 mod 4:  β'(c) ≤ LB_1^{(c)} = 8k' - 4 - 2s_2(k'-1) + v_2(k')                    (♣)
```
and by the identity s_2(k'-1) = s_2(k') + v_2(k') - 1:
```
LB_1^{(c)} = 8k' - 4 - 2(s_2(k') + v_2(k') - 1) + v_2(k')
          = 8k' - 2 - 2s_2(k') - v_2(k').
```

Hmm let me sanity: c=12 (k'=3, s_2(k')=2, v_2(k')=0): LB_1 = 24 - 2 - 4 - 0 = 18. ✓
c=8 (k'=2): 16 - 2 - 2 - 1 = 11. ✓
c=16 (k'=4): 32 - 2 - 2 - 2 = 26. ✓
c=4 (k'=1): 8 - 2 - 2 - 0 = 4. ✓

**Excellent — LB_1^{(c ≡ 0 mod 4)} = 8k' − 2 − 2s_2(k') − v_2(k'), and this equals the target β'(c).**

### 3.2 What remains to close case c ≡ 0 mod 4

To turn this into a proof of D(c) = s_2(k) − 1 for c = 4k:

1. **UB:** show LB_1^{(c)} is achieved by an actual witness (distinct-min sum). At joint-Lucas-min (a,b) for k=1 with L = c−2, and j*=1, need the k=1 term to dominate. This is a witness computation — check c=12 already done (achievers listed). Needs verification at c=16, 20, 24, ...

2. **LB (the harder side):** show **β'(c) ≥ LB_1^{(c)}** at c ≡ 0 mod 4. From the c=12 catalog, min_k LB_k = LB_1 (tied across odd k). But we need **for ALL k not just the catalog range**, and more importantly, for all shell (a,b), v_2(H_c(a,b,j)) ≥ LB_1. This is the Day-91 style **periodicity-based LB proof**, which for c=11 required a mod-2^12 exhaustive check over 2^{23} residues. It doesn't scale without a structural argument.

3. **The pure closed form.** LB_1 = 8k' − 2 − 2s_2(k') − v_2(k') is NOT a pure digit sum — it has a v_2(k') term. But β(c) = 2(c−1) − s_2(c−1). At c=4k', s_2(c−1) = s_2(4k'-1) = s_2(k'-1) + 2 = s_2(k') + v_2(k') + 1. So β(c) = 8k' - 2 - s_2(k') - v_2(k') - 1 = 8k' - 3 - s_2(k') - v_2(k').

Then D = β − LB_1 = (8k' - 3 - s_2(k') - v_2(k')) − (8k' - 2 - 2s_2(k') - v_2(k')) = s_2(k') − 1. **CONFIRMED.**

**So the case c ≡ 0 mod 4 REDUCES to: prove β'(c) = LB_1^{(c)}.**
The digit-sum formula D(c) = s_2(k) − 1 is then a direct consequence of Legendre + F2's v_2(c(c-1)) formula for Δ_1.

---

## 4. Case c ≡ 2 mod 4: what's needed

D(c) = 1 + s_2(k − 1) where c = 4k + 2, k ≥ 1.

At c=6 (k=1): D=1+0=1. β=8. β'=7.
At c=10 (k=2): D=1+1=2. β=16. β'=14.
At c=14 (k=3): D=1+1=2. β=23. β'=21.

Catalog argmin at c=6: k*=1 (LB=7). At c=10: k*=5 (LB=14). At c=14: many k* achieve 21.

**k* is NOT constant.** But at every c ≡ 2 mod 4 in the catalog, MULTIPLE k give the SAME LB, similar to c ≡ 0 mod 4. Let's check if LB_1 hits the target at c ≡ 2 mod 4.

At c=6: LB_1 = 2·v_2(4!) + v_2(6·5) = 6 + 1 = 7. ✓ = β'(6).
At c=10: LB_1 = 2·v_2(8!) + v_2(10·9) = 14 + 1 = 15. But β'(10) = 14. **LB_1 overshoots.**

So at c=10, LB_1 = 15 ≠ 14 = β'. The argmin is at k=5, not k=1.

Reading c=10 catalog: k=5, Δ=8, LB=14.
Reading c=14 catalog: k=1, Δ=1, LB=21. k=5, Δ=7, LB=21. k=7, Δ=13, LB=21. All tied at 21.

**At c=14, LB_1 = 21 does match β'.** But at c=10, LB_1 = 15 misses.

Why? At c=10, k'=2 so v_2(k') = 1. The Δ_1 = v_2(c(c-1)) = v_2(10·9) = 1 gives more "cushion" than we can afford. We need to go to a HIGHER k where the Legendre loss is compensated by even smaller Δ. Specifically at c=10, k=5, Δ_5 = 8 vs Legendre 6, sum 14; vs k=1 Legendre 14 + Δ_1 = 1, sum 15. The k=5 branch beats k=1 by 1.

**This is the crux of the derivation problem:** the argmin k* depends on the c mod 8 (and higher) structure, not just c mod 4. There's no c-uniform k* selection formula. The best we can do is:
```
β'(c) = min_k LB_k^{(c)},
```
and prove the min equals a digit-sum expression by simultaneous k-optimisation.

---

## 5. Case c odd

D(c) = 4 + 2s_2(k−1), k = ⌊c/4⌋.

At c=5 (k=1): D=4. β=7. β'=3.
At c=7 (k=1): D=4. β=10. β'=6.
At c=9 (k=2): D=6. β=15. β'=9.
At c=11 (k=2): D=6. β=18. β'=12.
At c=13 (k=3): D=6. β=22. β'=16.
At c=15 (k=3): D=6. β=25. β'=19.
At c=17 (k=4): D=8. β=31. β'=23.

SCP data: k*=2 at c=5, 9, 17. k*=3 or 6 at c=7. k*=6 at c=11. k*=6 or 10 at c=13. k*=7 at c=15. k*=2 at c=17.

At c=5, k*=2, L=2. LB_2 = 2·1 + Δ_2 = 2 + 1 = 3 = β'. ✓
At c=9, k*=2, L=6. LB_2 = 2·4 + 1 = 9 = β'. ✓
At c=17, k*=2, L=14. LB_2 = 2·11 + 1 = 23 = β'. ✓

**For c ≡ 1 mod 4, k*=2 works at c=5,9,17 but NOT c=13.**

At c=13, LB_2 = 17, but β' = 16. Some other k (k=6 or 10) beats it.

**Sub-pattern:** k*=2 is dominant when v_2(k−1) is small (k=1, 2, 4 give k'*=2 argmin), but fails when k has bigger v_2 structure (k=3 at c=13).

Actually, ⌊c/4⌋ − 1 values:
- c=5: k−1=0, s_2=0 → D=4
- c=9: k−1=1, s_2=1 → D=6
- c=13: k−1=2, s_2=1 → D=6
- c=17: k−1=3, s_2=2 → D=8

At c=13, k−1=2 has v_2 = 1, which explains why k*=2 fails but k*=6 (a shifted version) succeeds. The k*=6 vs k*=2 shift is congruent to a "carry propagation at scale 4."

This case is even messier than c ≡ 2 mod 4. Not derivable this session.

---

## 6. Enumeration of structural obstacles

The derivation of the digit-sum formula requires each of the following:

**Obstacle A (missing).** A c-uniform closed form for Δ_k^{(c)} at k = 3, 5, 7, ... — beyond just k = 1, 2. We currently have F2 (k=1) proved. Higher-k formulas are "messier" per Day 91 §3.

**Obstacle B (missing).** Even given closed forms for all Δ_k, we need to prove min_k LB_k = β'(c) — the SCP + distinct-min sum rule. Currently `checked-sober` at c ∈ {4..11}, unproved in general.

**Obstacle C (partially resolved).** For c ≡ 0 mod 4 specifically, we've shown LB_1 = target closed form (this session, §3). But we still need to prove β'(c) = LB_1^{(c)} — i.e., no other k gives a strictly smaller value and there exists a witness.

**Obstacle D (fundamental).** For c ≡ 2 mod 4 and c odd, the argmin k* is NOT the same k across c mod 4 classes. It shifts based on finer 2-adic properties (roughly c mod 8 or mod 16). Deriving β'(c) from a fixed k* is impossible; one must argue about the min itself.

**Obstacle E (Rowland-Yassawi barrier).** Even if all Δ_k had closed forms as functions of c, their min over k is combinatorial. By Rowland-Yassawi, no polynomial-in-c form for v_2 of a fixed polynomial can produce this shape. The digit-sum shape can only arise from **combining multiple k-branches with carry cancellations** — the "s_2(k-1)" in the formula is enumerating carries in a k-shift argument that jumps between argmin branches.

---

## 7. Registry recommendation

**Stay at `checked-sober`.** Do NOT upgrade to `sketched`.

Justification: the closest we came to a derivation is the c ≡ 0 mod 4 case (§3), where I showed LB_1^{(c)} = 8k' − 2 − 2s_2(k') − v_2(k') and this equals the target β(c) − D(c). But **LB_1 = β'** requires an additional argument (SCP + witness UB + LB from periodicity) that is NOT provided by the Day-88 factorisation alone. Currently that argument is empirical / mod-2^{c} exhaustive at c=11 only.

The formula is *consistent* with the Day-88 factorisation in the sense that LB_1 evaluates to the right closed form at c ≡ 0 mod 4. That is a genuine partial derivation. But claiming a `sketched` proof requires either (a) a UB witness family c-uniformly, or (b) a c-uniform LB argument that doesn't require exhaustive residue checks. Neither is done.

For the c ≡ 2 mod 4 and c odd cases, we don't even have the closed form step — the argmin k* moves and I couldn't identify a single-k explicit form.

**Path forward:**
- **Immediate:** derive Δ_3, Δ_5 closed forms structurally (via Q_3, Q_5 catalog). See if any of them collapse to a c-uniform "digit-sum" form.
- **Medium:** prove Δ_k^{(c)} + 2·v_2((c-1-k)!) is k-independent on the odd-k slice for c ≡ 0 mod 4 (this is what makes the c=12 catalog have all-tied odd-k LB). This would give the c ≡ 0 mod 4 case cleanly.
- **Long:** derive a c-uniform k* selection rule for c ≡ 2 mod 4 and c odd, or reformulate the derivation as "min over multiple k-branches whose telescoping is a digit sum".

---

## 8. Surprising structural facts noticed

1. **LB_1^{(c)} = target β'(c) at c ≡ 0 mod 4.** This is a genuine closed form for the case c ≡ 0 mod 4, proved using only F2 + Legendre. Not previously noted in the Day-93 report. Half a derivation.

2. **The c=12 catalog has LB tied across all odd k.** Every odd k gives EXACTLY LB = 18. This is a very strong structural pattern — it suggests a **k-independent LB on the odd-k slice at c ≡ 0 mod 4**. Would love to see this proved from Q_k structure.

3. **At c=15, k*=7 uniquely** (nothing else achieves LB=19). This is diametrically opposite to c=12's degenerate tied-min. The two extremes suggest that c ≡ 3 mod 4 with s_2(k-1) high produces sharp discrimination.

4. **The k* jump from k*=2 at c ∈ {5, 9, 17} to k*=6 at c=13 is exactly a shift of +4.** Consistent with a "scale-4 Kummer carry" — when the low nibble of c changes structure, the argmin shifts by 4.

5. **The v_2(k') term in LB_1 exactly cancels a v_2(k') in β(c).** So the pure digit-sum form of D(c) emerges from a v_2-cancellation between the Legendre part of β(c) and the Δ_1 part of LB_1. Beautiful, but not derivable without noticing s_2(4k'-1) = s_2(k') + v_2(k') + 1.

---

## 9. Assumptions audit (short version)

Did I secretly assume:
- **k* is c-uniform mod 4?** No — I saw it isn't and adjusted.
- **LB_k is a smooth function of k?** No — Rowland-Yassawi prevents this.
- **Δ_k has a closed form in c for all k?** Yes, for k=1 (proved). For k ≥ 2, unproved. This is Obstacle A.
- **min_k LB_k = β'(c)?** Yes, this is SCP, `checked-sober` at c ∈ {4..11}.
- **UB by witness = LB?** Empirically yes at c ∈ {12..15}. Not proved.

The most fragile assumption is **min_k LB_k = β'(c)** as a general statement. The LB catalog gives β'(c) ≥ min_k LB_k^{(c)} (via the sum rule). Equality requires a witness. This is the SCP, and while it fits at c ∈ {4..15}, it is not derived from Day-88 alone.

---

## 10. Bottom line for Rick

I got **one case half-derived** (c ≡ 0 mod 4 via LB_1). The other two cases require closed forms for Δ_k at k ≥ 2 that I don't have. The formula does NOT derive cleanly from Day-88; it requires either (a) Δ_k closed forms for many k, or (b) a c-uniform argmin selection rule that respects Kummer-carry structure at scale 4.

**Registry:** stay at `checked-sober`. Consider adding a sub-node
`beta-prime-c-cong-0-mod-4-from-LB1` at grade `sketched`: I have shown
LB_1 = target for c ≡ 0 mod 4, modulo the SCP LB=UB step.

— Rick's prove-agent, Day 94 P0, 2026-07-13.
