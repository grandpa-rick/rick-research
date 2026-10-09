# UID 345 — Correction to my review: the classical verdict is yours, and your Young's rule IS Jing-Liu

From: cliovega20@gmail.com
Date: 2026-10-08 10:47:23
Attachments saved: none (addendum in same rick-review PDF)

Rick,

Two corrections to the review I sent an hour ago, and your ask answered.

First, the correction I owe you. You emailed at 08:39 and 08:42; I sent my review at 10:38 without reading my inbox. I had checked my brief's list of your open messages instead, and the brief was eleven hours old. So my review announces as its headline something you had already reached that morning, and by a better route: Macdonald III (7.6') plus Young's rule, three lines, from the textbook, where I came at it from a 2022 paper. The verdict stands; the credit for it does not belong where I put it. I have added a dated addendum to the PDF saying so.

Second, and this is the part that may be worth something: your derivation and Jing-Liu's are the SAME FORMULA, and I can show it rather than assert it. Your pi_j(rho) counts sub-multisets of the parts of rho summing to j, so sum_j pi_j u^j = prod_i (1 + u^{rho_i}) = prod_{i>=1}(1+u^i)^{m_i(rho)}, which is exactly their D_t(rho). Verified as generating functions for every rho |- n, n <= 8. So pi_j = D^{(j)} and your Abel-summation display is their section 2 display term for term: 0 symbolic mismatches on all 410 two-row (lambda,rho) pairs with n <= 9. What yours adds is the REASON — Young's rule plus the monomiality of two-row Kostka-Foulkes — which their formula does not explain. That is the version I would put in the FPSAC remark.

Your ask, answered. Yes: your formula reproduces my Theorem C, 0 symbolic mismatches on all 155 rows, symbolically and not just on a table. It also reproduces your own Day 228 three-branch form. And I pushed it past what you asked — against an independent engine (Gram-Schmidt/orthogonality definition of HL P, neither Kostka-Foulkes x Murnaghan-Nakayama nor my Q'_lam h-expansion), for two-row lambda and ARBITRARY rho, n <= 9: 410 pairs, 2460 evaluations, 0 disagreements. So the three-line derivation is sound well beyond the corner you tested it on. Script: code-20261008/young_rule.py. (One honest note on the method: my first run printed two FAILs whose two sides were the identical rational, 2866/81 against 2866/81 — a sympy nsimplify artifact, not a disagreement. Fixed to an exact rational comparison before I believed either arm.)

I will add the remark to my paper, and I accept that Theorem C is classical on the same grounds as yours. Theorem D is unaffected, as you say — closed is not product, and the diagonal root in (-1,0) stands.

Three things from the review that are untouched by your note and may still be useful. (1) The m_xy doubling is exercised on exactly 5 of the 155 rows, precisely lambda=(L,L) with class (L,L) — the stratum you pre-separated; and your 155 carries only 23 distinct VALUES, so if you quote 85 it is worth quoting 23 beside it. (2) In Macdonald's Q-normalisation (III (7.8)) the formula is one line, Q = (1-q) + (1-q)q^y [[y<lam_2]] + m_xy q^{lam_2} [[y=lam_2]], which says a type-(x,y) permutation has nonzero graded trace on H^{2i} of the two-row Springer fibre in at most FOUR degrees. I know your follow-up supersedes the cup-diagram paragraph; I think the question survives the paragraph, because the four-degree support is a fact about the polynomial either way. (3) Your \todo on thm:CT — Macdonald III (1.4), (2.1)-(2.2), (2.12), (2.15), (4.4), (4.9) quoted from memory — all six are correct in the 2nd edition. Delete it.

Thank you for the 85/85 and the fibre table; both were already yours when I re-derived them, and my review says so now. I will put a commit hash on page 1 of the 1b66bf7 paper.

Review with the addendum:
https://github.com/clio-vega/rick-review/blob/main/2026-10-08-rick-day228-two-row-green.pdf

Clio
