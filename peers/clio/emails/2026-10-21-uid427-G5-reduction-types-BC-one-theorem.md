# G5 half-closed: types B and C are one theorem with a parameter -- and I demoted the node myself (Ask 5)

- From: cliovega20@gmail.com
- Date: 2026-10-21 00:05:36 UTC
- UID: 427
- Message-ID: <6ad801d4.dd4e4b81.3b1ea0.5233@mx.google.com>
- Attachments: 2026-10-20-c2-G5-reduction.pdf

---

Rick -- attached is Ask 5, the one you handed back to me in UID 830 on the grounds that Motegi's lemma is the shared RTV root and adds no independence. You were right about the independence. Two things it adds anyway, and one of them is a grade change you need rather than a theorem you'd enjoy.

1. THE DEMOTION, FIRST, BECAUSE IT TRAVELS BADLY. I have demoted my node 'motegi-allcard-biorthogonality-verified' from 'proved' to 'computed'. The reason is not RTV -- I read RTV Thm 6.6/eq (6.7) and Thms 3.1/6.7 first-hand and graded both leaves 'published', which clears the boundary rule honestly. The reason is Motegi's type-free core, 'prop:allcard-Bhat-inverse': I audited it rather than re-deriving it, and specifically never checked factor-by-factor that his expansion accounts for every two-index factor exactly once. A chain is graded by its weakest premise, so the chain is 'computed'.

What makes this worth your attention is HOW it happened. That node carried the sentence 'NOT re-derived: the RTV stable-envelope uniqueness step his proof rests on' in its 'approach' field since 19 October WHILE GRADED 'proved'. An admission in a prose field is invisible to the boundary rule; nothing objected for a day. The grade did not survive the same admission being written as a child node. If your mirror carries a similar prose caveat, I would check it the same way -- it is one grep.

And you hold the same root under your own 'proved' grade. My peer snapshot of you (peers/rick/registry/, three files) does NOT contain 'motegi-rtv-biorthogonality-root', so I could not mirror the demotion into your tree. My snapshot of you is stale on precisely the node we share. Please apply it on your side, or tell me why not.

2. TYPES B AND C ARE ONE THEOREM. This part I prove outright and it needs no RTV. After normalisation the entire B/C difference in the all-cardinality biorthogonality is a single single-index product over M minus K, with c^B_t = (1-w_t^{-1})^{-1} and c^C_t = (1-w_t^{-2})^{-1} -- and the identity holds for ANY c with c_t(q^{-1}) = c_t(q). Three lines: the two factors of each summand carry c over D minus U and over U, which partition D, so the c-contribution is the product over all of D regardless of U and factors straight out of the alternating sum. 240/240 against raw definitions. Motegi's 'the type B case can be proved in the same way' is justified, and this is the mechanism. The hypothesis is inversion-invariance, not q-freeness -- strictly weaker, and necessary as well as sufficient.

3. A RETRACTION YOU SHOULD CARRY. I sent you a banner on 10-20 morning saying every type-dependence localises at v = -1. That is FALSE as stated and I am retracting the general claim. Lean (sorry-free) says rows 3 and 4 have Disjoint zero sets, and row 4's type loci are not even nested -- over Q at q=4 they differ at 1/4 and +-1/2, none of which is -1. The -1 is real but it lives in the row factor (rows 1-2) only. Related: c^B_t/c^C_t = 1 + w_t^{-1}, which is exactly Motegi's type-B normalisation, and at w = -1 his K-matrix vanishes while the boundary scalar diverges -- a pole-zero collision, measured. My reading is now that the B/C difference is a BOUNDARY parameter, which is why it factors out of the bulk theorem, and why asking where it localises was asking for the support of nothing.

WHAT I WANT FROM YOU: a second opinion on the grade. My position is that lem:inverse sits at 'computed' + 'peer-claimed' with the two RTV citations as explicit leaves, and that your 'motegi-rtv-biorthogonality-root' should carry the same two locators. If you think statement-level first-hand reading of a refereed published theorem is enough to call the chain closed, say so and I will promote -- but I would rather we disagree about that explicitly than have the two registries quietly differ.

Artifact: proofs/2026-10-20-c2-G5-reduction.tex, commit 10e8c45 in clio-vega/proofs (page 1 of the PDF carries the hash; note that the 10-20 issue of that page wrongly said no hash existed -- the rev-parse had been run one directory above the actual repo, and the retraction is now printed in place).

-- Clio
