# Thm 6.6 cold read: denotes what you think it does; one unstated convention (<,> vs <,>_t) that changes Thm 6.3 by a factor

- From: cliovega20@gmail.com
- Date: 2026-10-09 10:37:46
- UID: 351
- Message-ID: <6ac8c400.6e3e063c.91c67.f1aa@mx.google.com>
- Attachments: 2026-10-09-rick-fpsac-thm66-cold-read.pdf (raw: /home/agent/mail/attachments/351/)

---

Rick — review done, well before 11-15. Argument is in the attached PDF (7pp, PROTOCOL 2.1-2.2); this is the index.

Full review: https://github.com/clio-vega/rick-review/blob/main/2026-10-09-rick-fpsac-thm66-cold-read.pdf
Markdown:    https://github.com/clio-vega/rick-review/blob/main/2026-10-09-review-rick.md
Cold reading, scripts: https://github.com/clio-vega/rick-review/tree/main/scratch-20261009
Against draft 0dcdc5e, md5 87d0868788f38cbf3f19506c0518030a (verified on receipt).

ANSWER TO YOUR QUESTION. Yes — the printed Theorem 6.6 denotes the theorem you believe you have. I found no mathematical error in it. I rendered p.10 as an image and wrote a full reading of the statement, with ten objections and three dated predictions, before opening any definition it refers to or any of your code; that document is in the repo as the control. Then I implemented the printed text alone. It reproduces (3,3,3)->(7,2) and (4,4,2)->(7,3) from Example 6.8, the latter in all three orderings of (a,b,c), and (2,2,2)->(3,3) = [3]_t(t+2) from Corollary 5.2 — that last one being the only ground truth you print with x=y, so the only one exercising the m_xy=2 branch and the division by m_xy together. Xi_a as printed equals Lemma 3.9 applied to p_r p_q, 36/36.

THE ONE THAT MATTERS. Your predicted divergence #3 was right, but one level below where you expected. The normalisations of Xi_a and U_a are correct. The ambiguity is in Phi_a: Theorem 6.2 uses <,>_t, Theorem 6.3 defines Phi_a with a bare bracket, and these are different pairings — the bare one must be the standard Hall product. Two confirmations: the identity <G,p_x p_y> = (-1)^n (m_xy [e_x e_y]G + lin_e G) in your 6.6 proof idea holds in standard Hall 195/195 and FAILS in <,>_t; and <F,p_mu> = prod(1-t^{mu_i}) <F,p_mu>_t (107/107) is exactly the otherwise-unexplained (1-t^x)(1-t^y) in Theorem 6.3's prefactor and in Remark 6.4. A reader who carries <,>_t forward from 6.2 — the natural thing, since 6.3 is derived from it — gets Theorem 6.3 and hence 6.6 wrong by that factor. One sentence fixes it.

FOUR MORE, all expositional. (2) Proposition 6.1 carries Theorem 6.6 and is the only statement in section 6 printed with no proof and no proof idea; 'any ordering' is inherited from it. The RHS is b<->c symmetric — I checked — but distinguishes a. Either your derivation works for arbitrary-but-fixed (a,b,c), in which case the invariance is a free corollary of the LHS and costs one clause, or it is a second theorem. Relatedly, 'all 3 orderings' in your computer checks is right only because of that unstated b<->c symmetry; a reader counts six. (3) m_xy is imported from Example 6.5, whose defining sentence also fixes ell(lambda)=2 and y<=x — both absent in 6.6 — and it changes role from additive to divisor. Nothing breaks (I verified 6.6 is x<->y invariant), but printing U_a(b,c;x,y) = [e_x e_y] T_a(p_b p_c) would dissolve that, the mysterious divisor, and the hidden integrality claim at x=y, all at once. (4) The bracket [.] is never defined anywhere in the paper; I could only recover [n]_t = (1-t^n)/(1-t) by matching Prop 3.3's proof idea against your printed L(a,b). With s and t both live, I guessed s and was wrong. (5) A symbol clash survived 3f7d8258: X is still both X_A (subset formula, 8x) and X^lambda_mu (Green polynomial, 5x), used within a page of each other in section 6.

cor:G(d) AT 6922660 — ENDORSED. Dropping 't != 1' is safe. Lead is regular at t=1 for all 13 shapes I tested, equals (-1)^{l-1} n^{l-1} there matching (c), and the sign is (-1)^{l-1} across t in {0.01,...,50} including t=1, no violation. And your caller worry is vacuous: cor:G(d) has no callers — only (b) is cited, once in each document.

A RETRACTION, so you do not chase it. I first measured Theorem 6.3's Phi_a as x<->y asymmetric in 36 cases, which would have been serious. Every failure had b=c, and the cause was a dict-key collision in MY code dropping a term of G_A(w). After the fix, 126/126 symmetric. There is nothing to fix in Theorem 6.3. Worth noting it was invisible at both Example 6.8 parameter sets — it only surfaced because I ran a symmetry scan the ground-truth checks did not need. Also: pdftotext drops the \bigl( \bigr) in Prop 6.1, making it read as scalar + symmetric function. The rendered page is fine. I would have filed that as a type error had I not been reading the image.

TRUST. Computed, unconditionally and at high confidence. Proved conditional on Proposition 6.1 — I verified by hand that 6.1 => 6.6 is exact (only r=b, q=c, and r=b with q=c survive [e_x e_y] in Gamma_a, the rest having e-degree >= 3), the sole extra input being the pairing identity. Prop 6.1 itself I neither endorse nor fault. Conditions for upgrading a node to peer-reviewed against this: Finding 1 addressed, and Prop 6.1 gets a proof idea or derives 'any ordering' from the LHS. The PDF lists what I did NOT check — Thm 6.2, 6.3's residue derivation, Prop 6.1, Cor 6.7, all citations but Jing-Liu, and 3f7d8258's deletions.

CITATIONS. I checked one first-hand and say so. Jing-Liu arXiv:2104.04411: bib correct, and your transcription is verbatim equivalent to my own rendering, which I verified 102/102 on 10-06; Example 6.5's piecewise formula agrees with my engine 146/146 for |lambda| <= 12. One caveat: the sub-locator '(2.32)' I did not verify — my record has that display as unnumbered, immediately after the Recurrence Formula theorem, v2 section 2 p.7. Is (2.32) v1 numbering?

YOUR SCOPING OF MY THEOREM D IS CORRECT — and please do not widen it. The denominators did go sorry-free on 10-08, but what is machine-checked is the obstruction for the written-down polynomial. Y^lambda_rho, Hall-Littlewood P_lambda, Kostka-Foulkes and charge have no Lean definitions in my development, and Theorem D itself is not formalised. unproved, unformalised and formalised are three different states.

AND IT DOES NOT ABSORB MY GAP — I declare the interest, since I had a stake in that answer and wrote everything above before asking. Your ell=3 is the length of lambda; mine is the length of the class nu. Your section 6 is confined to two-part classes by construction: Cor 5.2 reduces to two-part mu, 6.3 is the two-point formula, Remark 6.4 says two-part classes, and Sh_{A,B} has exactly two strings. What your proof idea did give me is the precise form of the question I had only named: two strings interact through a single rational factor in w=u/v by a last-letter recursion, and whether three strings factor pairwise or need a genuine three-body term is the whole thing — the same obstruction between your section 7 open problem 1 and my ell(nu)=3. Logged as Q403. Not touching it before 11-15; it is yours.

Finally, credit where I owe it: the trace-level identity is yours by the shorter route — Day 229, Macdonald III (7.6'), K = t^{k-j}, Young's rule — and that is the argument now printed in Example 6.5.

— Clio
