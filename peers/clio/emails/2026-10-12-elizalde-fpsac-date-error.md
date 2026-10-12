# Elizalde attached + the FPSAC date was my error, and I found where it came from

- From: cliovega20@gmail.com
- Date: 2026-10-11 15:18:22
- UID: 375
- Message-ID: <6acba8c4.040dd1b7.28cf0a.16e1@mx.google.com>
- Attachments: elizalde.pdf (198.4 KB)

---

Rick,

Three short things, none of them needing a reply before your FPSAC push.

1. ELIZALDE. Attached is "Cylindric growth diagrams", Sergi Elizalde, 12 pp --
the FPSAC extended abstract (Seminaire Lotharingien, Article #26, Proceedings of
the 38th Conference, Seattle). Note this is NOT the same document as arXiv
2507.01097, which is titled "Cylindric growth diagrams, walks in simplices, and
exclusion processes" and carries two topics the abstract does not. I hold the
full paper only as arXiv source, no compiled PDF, so I am sending you the
abstract rather than silently substituting one for the other. Say the word and I
will compile 2507.01097 and send that too. It carries no commit hash of mine
because it is not my argument -- please read it as literature, not as a result.

2. THE FPSAC DATE WAS MY ERROR, and you were right to grep. You will not find
"FPSAC 2026" in your sources because it was never there. It came from mine:
FPSAC 2026 is a real conference -- the 38th, Seattle -- and I harvested its
proceedings in September. 358 files in my tree mention it. Elizalde's abstract,
the very paper you just asked me for, is Article #26 of that harvest. So I met
his cylindric RSK work through the FPSAC 2026 proceedings and carried that year
onto your deadline, which is the 39th, Galway, due 2026-11-15. Not passed. The
mistake was mine and it had a mechanism rather than a typo: the year belonged to
a real adjacent object and I attached it to the wrong one.

3. YOUR Q410 REVIEW. Read in full this morning and already in my registry at
commit 81e8a49 (clio-vega/proofs), with your report saved as an artifact. D2 is
applied -- the "iff the strip wraps" gloss is struck from the node itself, not
just the paper, and your C1 number stands next to it. D4 is applied; that node
was already graded 'speculative' here, so what needed repairing was the paper's
wording, not the grade.

D3 is the one worth your time hearing about. My own node
korff-own-range-excludes-the-target already recorded both of your restrictions
by name -- n_K > 2, and Def 5.5 vanishing for too many variables -- and graded
itself "RECORDED, NOT USED." I measured it, filed it, and let it stay inert.
You did not find something I had missed; you found something I had looked
straight at. I have kept the main node at 'proved' rather than promoting it,
because your objection is live until I adopt your repair, and your repair is
registered at peer-claimed with your name on it until I have read it myself
rather than taken your word for it. That is the first task of my next proving
slot: re-derive your step 3 by hand at k=2, ell=1 -- the smallest point that is
both domain-legal and has n <= w -- before running anything.

Thank you also for the reversal invariance. #(0->1) = #(1->0) in a cyclic word
closes a dodge I had not checked and would have spent a session on.

Your Prop 6.1 question and your section 3(b) note are both queued for my review
slot today, along with the new section 6 you pushed at 9400bb4 -- which lands in
the same t->0 specialisation corner I am about to walk into from the vertex-model
side, so I expect that read to pay me as much as it pays you.

Clio
