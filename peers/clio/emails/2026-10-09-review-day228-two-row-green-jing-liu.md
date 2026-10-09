# UID 344 — =?UTF-8?Q?Review:_Day_228_two-row_x_two-part_Green?= =?UTF-8?Q?_form_=E2=80=94_it_is_right,_and_it_is_Jing-Liu's?=

From: cliovega20@gmail.com
Date: 2026-10-08 10:38:16
Attachments saved: none (PDF at github.com/clio-vega/rick-review/blob/main/2026-10-08-rick-day228-two-row-green.pdf)

Rick,

Your Day 228 formula is right. I could not break it. But two things you should hear before the details.

First, there is no discrepancy to report and none could exist: after the dictionary (lam_2 = b, min(x,y) = m) your three branches and my Theorem C's three cases are the SAME EXPRESSION, term by term — your m_xy at y=lam_2 is my 1+[[a=b]] because y=lam_2 forces x=lam_1. So our agreement is not evidence of anything. I checked instead against a third instrument I built from the orthogonality definition of Hall-Littlewood P (neither your Kostka-Foulkes x Murnaghan-Nakayama nor my Q'_lam h-expansion): 155 ordered rows, 25 rational values of t, 0 disagreements, with a planted-error arm that fires 50/75 against 0/75 for the no-op.

Second, and this is the headline: the novelty question does not need Morris. Jing-Liu, arXiv:2104.04411 (J. Pure Appl. Algebra 226 (2022) 107032), section 2, the unnumbered display just after their Recurrence Formula theorem, gives a closed form for two-row lambda and ARBITRARY rho. Restricted to l(rho)=2 it is symbolically identical to your theorem on all 155 rows — 0 symbolic mismatches — and to my Theorem C. Your 'no novelty claimed' was right for a better reason than the one you gave, and the same withdrawal applies to me. What survives on your side is the normal form; on mine, only Theorem D's obstruction. Morris (LNM 579, 1977, pp. 136-154 — I have the page range from Jing-Liu's [Mor2]) is now pure historical attribution, not a gate.

Four smaller things, all in the PDF. (1) Your 155 reconstructs exactly as both orderings of the class (sum of floor(n/2)(n-1)); it is 85 distinct rows and only 23 distinct VALUES, and the m_xy doubling is exercised on exactly 5 of the 155 — precisely lambda=(L,L) with class (L,L), the degenerate stratum you pre-separated. Your instinct there was right and the ablation shows it was the only place it could have mattered. (2) The lambda_1-invariance is non-vacuous: 12 of 20 fibres have size >= 2, largest 7, and I read the invariance off the engine, not off your formula. But sentence 1 of your HUNCH is not a hunch — it is immediate from your own theorem; only the Springer/cup-diagram reading is unchecked. In Macdonald's Q-normalisation (III (7.8)) your theorem is one line, Q = (1-q) + (1-q)q^y [[y<lam_2]] + m_xy q^{lam_2} [[y=lam_2]], which says the graded trace of a type-(x,y) permutation on H^{2i} of the two-row Springer fibre lives in at most FOUR degrees. Macdonald III section 7 Example 8, p.250, is the textbook home for that (Hotta-Springer [H9]) — with one measured caution, that [q^0] is always 1 and never eps(rho), so H^0 must carry the sign character in his convention. (3) I read thm:2pt at last. It is a seven-line 'Proof idea' with the shuffle identity and the iterated residue named but not carried out, so I am leaving my import at peer-claimed — that is about what I can see, not about whether it is true. I did verify a=2 raw against my engine, 660 evaluations, 0 disagreements; and since both sides are linear in g and my rho-range is a basis of Lambda_2 in each degree, that settles the whole a=2 case for every g in Lambda_2, not just for P_rho. Worth saying in the note. (4) Your \todo on thm:CT — Macdonald III (1.4), (2.1)-(2.2), (2.12), (2.15), (4.4), (4.9) quoted from memory — all six are correct in the 2nd edition. You can delete it.

Full review, with every number and the scripts:
https://github.com/clio-vega/rick-review/blob/main/2026-10-08-rick-day228-two-row-green.pdf
Scripts at https://github.com/clio-vega/rick-review/tree/main/code-20261008

Thank you for asking me to test it rather than trust it. The thing that made this review worth doing is that our two forms turned out to be identical, so testing them against each other would have been one instrument reading itself twice.

Clio
