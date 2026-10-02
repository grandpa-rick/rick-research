# Erratum: corrected PDF of the M-convexity note (bibliography), and a cylindric-RSK paper I had never seen

- From: cliovega20@gmail.com
- Date: 2026-09-23 00:34:32 UTC
- UID: 289
- Attachments: 2026-09-20-c1-cylindric-M-convexity.pdf (saved /home/agent/mail/attachments/289/)

---

Rick,

This was written two days ago and did not go out — the mail tooling was unavailable in that session and I did not notice until this morning. My fault, and the delay is the reason I am leading with it.

Attached is the corrected PDF of 2026-09-20-c1-cylindric-M-convexity — the first of the three I sent you at 00:34 on 22 September. Please replace the copy you have.

ERRATUM. Its bibliography was missing four papers it leans on by name. It names Postnikov eight times, including Corollary 3.3, which is titled 'Cylindric Bender-Knuth; Postnikov's symmetry theorem' and which claims to reprove that theorem — and Postnikov, Affine approach to quantum Schubert calculus, Duke Math. J. 128 (2005) 473-509, was not in the reference list at all. Gessel-Krattenthaler (Trans. AMS 349 (1997) 429-479, where cylindric partitions come from), McNamara (Adv. Math. 205 (2006) 275-312) and Neyman were missing too. Fixed and recompiled; nothing mathematical changed, and the cover block now says so precisely rather than claiming, as it did, that nothing below it had changed at all. Commit clio-vega/proofs@eb9d081. If you are reading section 5 as I asked, the copy you already have is fine for that purpose — the defect was entirely in the front and back matter.

I found this the way one usually does: by reading somebody else's reference list.

THE PAPER IN QUESTION. Eric Neyman, Cylindric Young Tableaux and their Properties, arXiv:1410.5039 (2015) — an MIT PRIMES paper, mentored by Grinberg, subject suggested by Postnikov, apparently never journal-published, and therefore invisible to eleven years of my searching. It is the original cylindric RSK. I spent a session checking whether it contains anything I have written up as mine.

It does not. The census over the full 2366-line source returns zero for M-convex, Newton polytope, polytope, support, dominance, saturation and matroid. Neyman's subject is bijections between tableaux; mine is the support of the resulting polynomial. The one apparent collision is a name: his section 5.3 'Symmetry Property of CRSK' is the transpose-symmetry of his bijection, not S_ell-invariance of the generating function — he never states that cylindric skew Schur functions are symmetric, and his Cauchy identity is written with two variable sets precisely so that it does not need to be.

Since I had it open I verified the two identities Dobner points at, which as far as I can tell nobody had: his cylindric Cauchy identity in 494 of 494 instances, and his Corollary 5.21 in 205 of 205. I validated the instrument first — chain model against brute-force filling of the cylinder, 684 of 684 — so the agreement is not two bugs shaking hands. One presentational point for any revision: both identities are sums over infinitely many cylindric partitions, so they live in a completion and not in the 'power series of bounded degree' his definition names. Degreewise the sums are finite, so nothing breaks.

Then a small gift. Translating his coordinates into my bead model and combining his Corollary 5.21 with my support theorem gives a statement I would not have guessed and cannot yet prove directly: the dominance-maximal greedy weights over the shapes alpha/mu with |alpha/mu| = d coincide with those over the shapes lambda/alpha with |lambda/alpha| = d — an up/down symmetry about alpha. 812 instances, no failures. It is a corollary, not an independent test, and I say so in the review; what interests me is that a direct proof from the greedy recursion would be a support-level shadow of his bijection, obtained without the bijection.

Full review, with code:
https://github.com/clio-vega/rick-review/blob/main/2026-09-22-c2-q223-neyman.md

The sharpest thing in it is section 6, and it is an objection to my own work rather than to yours. A gap in my crystal-edges note asserted that a certain reduced pair 'need not be additive'. That assertion was never checked and appears to be false: zero failures in 82044 instances, while the neighbouring unbracketed statement is false from n=3, so the range does cross the regime where it could break. It turns into a clean conjecture whose proof closes the gap, and it is today's proof session.

Nothing here is time-critical except replacing the PDF.

— Clio
