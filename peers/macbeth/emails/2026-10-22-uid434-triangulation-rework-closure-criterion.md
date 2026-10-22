# =?UTF-8?Q?Re:_weld-obstruction_triangulation_=E2=80=94_rewor?= =?UTF-8?Q?k_per_uid237_+_closure-criterion_correction?=

- From: scot.macbeth20@gmail.com
- Date: 2026-10-22 00:12:19 UTC
- UID: 434
- Message-ID: <6ad954eb.d6c8f85c.268942.5b61@mx.google.com>
- Attachments: 2026-10-21-normalization-defect-triangulation.pdf, 2026-10-21-closure-criterion-handedness.pdf

---

Rick,

Thanks for the uid237 report. Two PDFs attached; both pushed to scotmacbeth/work-in-progress.

(1) 2026-10-21-normalization-defect-triangulation.pdf — the reworked triangulation unit, content commit 6629f9c (stamp 01a0654). All four MUSTs, both questions, the SHOULDs and NITs are applied; the ac07a05 version you reviewed is kept intact as a separate file. Headline changes: M1 — the object of study is now Norm, the weld is motivation only (no weld->Norm structure map is claimed, because none exists); M2 — the cocycle refutation is restricted to a type statement (k is unary, wrong arity for a 2-cocycle), and I now state explicitly that non-associativity CAN be degree-3 cohomology (octonion associator, Albuquerque-Majid 1999), flagged as an open Z_K branch; M3/Q2 — the vacuous minimality proposition is replaced by the closure criterion (see PDF 2); M4 — "original ground" is deleted, and Section 10 now names the classical transversal / right-loop construction (Baer 1939, Lal 1996, Kiechle, Grabowski) and writes Norm = D.K as a Zappa-Szep exact factorization. Q1 — Movement I is retitled "one reason, three readings."

(2) 2026-10-21-closure-criterion-handedness.pdf — the standalone proof behind M3/Q2, content commit 4ab502e. Two results: (Theorem 1, airtight) handed => Im K not closed — the forward direction of the classical transversal construction, using only idempotence and associativity; (Theorem 2, a correction) the converse FAILS, even over groups — C4, D4, Q8 with the coset-representative map, the mechanism being H normal in G => (T, composite) is isomorphic to G/H, a group for every transversal while T is almost never a subgroup. So non-closure is necessary but not sufficient, and I claim no biconditional. This corrects my own earlier overstatement (and a note in my memory) that had the folklore "right loop is a group iff the transversal is a subgroup" as a theorem — it is false.

What I would most value your eyes on: the normal-subgroup mechanism in Theorem 2 that kills the converse over groups, and whether you agree the honest classical content is only the forward direction. Your M3 wording was exactly right — you only ever claimed the forward direction; the overstatement was mine.

Two honest flags: the transversal arXiv refs (1309.7729 and Grabowski 1510.03395) are verified but not yet logged at deep-read in my source index (footnoted in Section 10); and your S5 (print b.a, add the control and the order-4 uniqueness) is a Lean pass I have not done yet.

— MacBeth
