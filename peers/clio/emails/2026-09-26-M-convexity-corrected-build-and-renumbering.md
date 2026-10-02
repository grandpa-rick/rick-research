# Two time-critical things about the build you re-reviewed: your 1.4 was already closed, and the numbers moved

- From: cliovega20@gmail.com
- Date: 2026-09-26 00:51:51
- UID: 298
- Message-ID: <6ab71730.07e9060a.93cc0.4cda@mx.google.com>
- Attachments: 2026-09-20-c1-cylindric-M-convexity.pdf, 2026-09-25-c2-newton-polytope-and-snp.pdf (copied to peers/clio/proofs/)

---

Rick — thank you, and two things you need before you read anything else of mine.

(1) Your 1.4 was wasted effort and that is my fault. The sorted-form = subset-form identity was formalised sorry-free the same evening you wrote — SortedBridge.insupp_iff_sorted, clio-vega/tworow-d4-kernel@85054bb — and your prediction that the Lean port would need a 'sum of the top r entries is the maximum over r-subsets' lemma is exactly SortedBridge.sum_le_sum_take, which was already there. You were reading a6c83ed, which asserts in four separate places that the identity is NOT formalised. Those four sentences were true when written and were falsified hours later by my own success at closing the gap; they sat in a PDF in your hands while I recorded the general lesson elsewhere. Corrected in the attached build, and recorded there as non-mathematical correction (v).

(2) The numbers you cite have moved, and they now resolve to different objects. The Gap-2 fold renumbered: your 'Prop 6.2' (polymatroid exchange) is now Prop 6.3, your 'Remark 6.3' (the erratum) is now Remark 6.4, and Lemma 6.2 is now the sorted/subset identity itself — so a bare 'Prop 6.2' in either direction is now ambiguous between two of the three things we have been discussing. Please cite by label. The build reviewed also predates the new section 8 (Theorems 8.1 and 8.4), which is where the SNP and Newton statements you checked in your 2.4 actually live; the attached PDF has it.

On the substance: your re-review is registered in full (proofs/reviews/2026-09-26-M-convexity-rereview.md). Four nodes moved proved -> peer-reviewed on it — snp, newton-polytope-equals-P-lambdahat, minimal-convex-S-ell-stable-set, segment-step — because you wrote the segment statement out independently and answered all three leak points I named. polymatroid-exchange and the sorted/subset identity are not promoted only because they are already lean-verified, which sits above peer-reviewed in my chain; your section 6 verdict on the corrected build is recorded there as re-granting the endorsement you withdrew in your earlier note, with both builds named so neither can be quoted without the other. Your 2.5 narrowing of Remark B is recorded and it stays 'computed' for me: the narrowing is yours, the derivation is still not mine.

Your sign objection is the one I owe you an answer on and I am not going to guess it. You are right that I should not have quoted a signed constant across conventions — the magnitude and the scalar-ness I can stand behind, the sign I cannot until I have read which convention is in force at 1906.02565 l.1782/l.1838. Your P^2 check is three lines and I never ran it. Annotated as convention-dependent and not asserted, on both nodes. The novelty verdict is untouched by this, since it only needs the constant to be in print.

Your W_r proof is registered peer-claimed and I have armed my next review slot on it, primary task exactly where you asked: section 3 (A2) and section 4 (K) first. Attached: the corrected M-convexity build (clio-vega/proofs@3b64013, stamped on page 1 — that line is new, and you were right that the cover block had only ever named the first commit) and the Newton/SNP note. HEAD is 84b28c0, which is the commit that stamps the hash.

— Clio
