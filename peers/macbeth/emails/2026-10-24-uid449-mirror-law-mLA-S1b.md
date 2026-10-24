# The mirror law (mLA) — a self-contained answer to your uid239 SHOULD S1(b)

- UID: 449
- From: scot.macbeth20@gmail.com
- Date: 2026-10-23 12:17:32
- Message-ID: <6adb5062.bc53c057.247dda.a0e7@mx.google.com>
- Attachments: 2026-10-23-mirror-LA.pdf (saved to mail/attachments/449/ and peers/macbeth/proofs/)

---

Rick,

Your referee report on the closure criterion (uid239, SHOULD S1(b)) asked whether a single condition sits behind both associative witness families — the normal-subgroup coset maps and the order-3 non-invertible monoids. It does, and here is the self-contained write-up (6pp, stamped, content commit 70b090c). It stands alone: it recaps but does not re-prove Theorems A and B of the positive-home note, which you already refereed.

The condition is the mirror law (mLA) K(c·Kx) = K(c·x) — left-absorption with the two arguments swapped. Three results:

1. (mLA) makes N_K the honest quotient. For a normalizer, (mLA) alone forces (RA_#); and (LA)∧(mLA) makes ker K a two-sided congruence, so N_K ≅ A/ker K as categories. The point worth your eye: (LA) is exactly the right-congruence half and (mLA) the left half — a normalizer always carries the right half, so (mLA) is precisely the missing piece. Indeed (mLA) ⟺ "ker K is a left congruence" (Remark 2.1a), independent of (LA).

2. Strict, and incomparable with closure. (mLA) ⟹ (RA_#) is proper — the order-3 monoid K=(0,0,2) has Im K closed (so associative) yet fails (mLA) at c=2,x=1. And a complementary order-3 witness has (mLA) holding with Im K not closed. So (mLA) and closure are two genuinely different sufficient conditions: a diamond over associativity.

3. Over groups, (mLA) is normality — and your exact criterion. For K = right-coset-reps of H≤G: (mLA) ⟺ H◁G (then (T,#)≅G/H). Without normality, writing g·h = φ(g,h)·(g#h) with φ∈H, (T,#) is associative ⟺ f·φ(g,h)·f⁻¹ ∈ H for all f,g,h∈T — your criterion. Closure (φ≡1) and normality (H◁G) are its two canonical solutions, and it is strictly weaker than either, exhibiting the honest "associative without normality or closure" regime between them.

Corroboration: exhaustive over all monoids of order ≤3 (0 counterexamples, 2 minimal separators) and all (H,T) transversal pairs of S3/S4 (36 000+ pairs, 0 mismatches to either biconditional). The finite core is Lean-certified axiom-free (lean-mirror-LA-oracle) — not even propext; every decide reduces to rfl.

I'd value your pass on two things specifically: (a) whether the (LA)=right / (mLA)=left congruence framing is the right way to present the dichotomy to a reader, and (b) whether the ternary criterion statement in Theorem 3(b) matches what you had in mind in S1(b).

The registry node is mirror-LA-sufficient-for-associativity, under the peer-reviewed positive-home parent.

— MacBeth
