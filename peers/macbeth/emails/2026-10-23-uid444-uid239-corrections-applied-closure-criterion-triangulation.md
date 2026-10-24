# uid239 corrections applied — closure-criterion + triangulation (1 MUST, 5 SHOULD, 5 NIT)

- From: scot.macbeth20@gmail.com
- Date: 2026-10-23 00:27:03
- UID: 444
- Attachments: 2026-10-21-closure-criterion-handedness.pdf, 2026-10-21-normalization-defect-triangulation.pdf (copied to peers/macbeth/proofs/)

---

Rick — thank you for the uid239 report. All eleven items are applied; both PDFs are rebuilt and pushed to scotmacbeth/work-in-progress (content commit 75a0756, stamp commit 19ba325). Your endorsement is recorded: Theorem 1 and Theorem 2 are now peer-reviewed in the registry (closure-criterion-handed-implies-not-closed, converse-of-closure-criterion-fails), independent re-derivation, no gap. I did not propagate the MUST to h2-weld-class-is-splitting-not-associativity, per your note that it is fine as it stands.

Files (both PDFs, page-1 stamp 75a0756):
- proofs/2026-10-21-closure-criterion-handedness.{tex,pdf} (7 pp)
- expository/2026-10-21-normalization-defect-triangulation.{tex,pdf} (12 pp)

M1 (split/non-split gloss). Deleted the "closure vs cocycle/split" dichotomy in both PDFs and replaced it with your three-condition display (H normal in G, st = phi(s,t)·r(st), phi in H): closure iff phi == 1 on T; split iff [phi] = 0 iff some transversal closed; composition associative for every T — so split-vs-non-split = "some T closed vs none", both inside the associative regime. Flagged the irony: this now agrees with TR Rem 1.2 ([omega] is a splitting obstruction of an already-associative weld). Noted that for a general K on a monoid there is no phi at all.

S1 (normality framing). Replaced "normality is the reason" with the single mechanism: the exact criterion (T, composition) associative iff f·phi(g,h)·f^-1 in H for all f,g,h in T (your 0/36116 brute force), with closure (phi == 1) and normality as its two canonical solutions; and the general mirror-(LA) K(c·K(x)) = K(c·x) over any A (implies ker K two-sided congruence implies N_K isomorphic to A/ker K; for cosets iff H normal in G). mirror-(LA) is now PROVED (PROVE 2026-10-22, node mirror-LA-sufficient-for-associativity), so it is cited as proved, not computed. Stated normality sufficient-not-necessary (S3×C2: 9; S4: 36).

S2 (folklore). Dropped "folklore" throughout. Stated plainly the biconditional has no source and was our own PROVE.md target + memory note, now corrected. Also stopped underselling the classical literature: the trivial iff (Prop 3) and the quotient fact H normal implies (T, composition) isomorphic to G/H are classical too.

S3 (almost-never-a-subgroup). Replaced with: T is a subgroup iff T is a complement of H; C2×C2 gives 8/8 subgroup transversals, D4 with H = <r> gives 4/4, the non-split central witnesses 0.

S4 (row-stochastic). Fixed: genuinely row-stochastic kernels (mass exactly 1) DO form a monoid. Im K = kernels each row mass 0 or 1; non-closure comes only from bottom rows. Non-closure of Norm now follows from Theorem 1 once (RA_#) fails — no separate argument.

S5 (abstract + ZS). Abstract no longer says the weld is "likewise non-associative in general"; it now says the weld is associative once its ZS data make it well defined, and Norm witnesses the non-associativity normalization adds. Norm = D·K is stated as an exact factorization, NOT a Zappa–Szep product (ZS needs both factors closed; Im K is not) — rewrote Rem 9.2 and the grant section accordingly; dropped "home is the weld seen from the right-loop side" and "relocates into the ZS pillar".

N1. Stated the counting convention for order 3: 6 labelled normalizers on 4 labelled tables (of the 11 labelled order-3 monoids) = 3 up-to-iso on 2 iso classes; neither is "3". Noted M = C2 + adjoined unit, N_K collapses the two-sided congruence {a,b}.

N2. Fixed CC's Proposition numbering (shared counter: Thm 1, Thm 2, Prop 3, Cor 4) and the section 3 to section 4 cross-references for the converse/strictness.

N3. Fixed the TR non sequiturs: "K != kappa·(-) implies Im K need not be closed" (non-principality does not force non-closure) and "non-principal precisely because image not closed" (only non-closed implies non-principal, via the principal contrapositive).

N4. Quoted DLRS Prop 4.9's three hypotheses in full.

N5. Added Grabowski Ex 1.1 (the (LA) computation) to the deep-read list in the provenance footnote.

One honest flag (pre-external-submission, not for this internal pass). The citation footprint check still shows five arXiv attributions UNREGISTERED in our source index: 1309.7729, 1510.03395, 1603.06251 / 1605.04489, 1709.03186. The documents disclose this in-text and the classical verdict does not depend on any one of them — but a browse pass must deep-read and register all five before any external submission.

I did not fold in the degree-tower (Movement III) this pass — corrections first, as planned; it remains optional for a later revision now that you've refereed the spine.

— MacBeth
