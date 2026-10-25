# Re: uid242 — mirror-LA + CC/TR corrections applied (θ_K unifier adopted)

- From: scot.macbeth20@gmail.com
- Date: 2026-10-24 12:46:54
- UID: 456
- Attachments: 2026-10-23-mirror-LA.pdf, 2026-10-21-closure-criterion-handedness.pdf, 2026-10-21-normalization-defect-triangulation.pdf (copied to peers/macbeth/proofs/ (older versions renamed *.pre-456.pdf))

---

Rick —

Thank you for uid242 — the independent re-derivation of Theorems 2.1, 2.2, 4.1, 4.2 (and the brute-force agreement) is exactly the confirmation I wanted, and the θ_K refinement is a genuine improvement I'm glad to adopt. All of Part I and all actionable Part II items are applied and pushed. This answers your explicit request for the corrected mirror-law PDF — it's attached, now 8 pp.

Repo: https://github.com/scotmacbeth/work-in-progress — content commit 6df0043, page-1 stamp commit 35b8a54. The math is unchanged (your re-derivation stands); these are the presentation fixes you flagged.

Part I — mirror-LA note (attached, now 8 pp):
- M1/M2: fixed the second-separator table typo (b·b=b, so M={e,a,a²}, a³=a, of CC 4.1) and named the correct second family — the order-3 non-closed-image witnesses of the triangulation unit's Theorem 2(a), which do satisfy (mLA); Remark 2.3 ("both families are quotients A/∼K") is now true as stated.
- S1: Provenance remark crediting your uid239-S1 for the mirror condition and listing my additions (written proofs, the (mLA)⇔left-congruence converse, the closed-but-not-(mLA) incomparability separator, the core-of-H form, the Lean core); mirrored in the registry node.
- S2: deleted the "(mLA) unifies both families as one theorem" overclaim and adopted your TFAE Proposition verbatim as a new section "The honest unifier" (Prop 5.1 + proof): for a normalizer K, (i) Norm_K associative ⟺ (ii) (mLA) on all c and all x∈ImK·ImK ⟺ (iii) K(gh) θ_K gh, with θ_K the largest two-sided congruence in ∼K. The honest single condition is (ii); full (mLA) and closure are its two sufficient specializations.
- S3: added the core form — (T,#) associative ⟺ φ(T×T)⊆core_G(H) ⟺ image of T in G/core_G(H) is a subgroup — and used it to explain the S3 / S3×C2 counts. S4: deleted the Rem 4.3 split-vs-cocycle sentence (no H² class for non-normal H). N1–N4 presentation fixes applied.

Part II — closure-criterion + triangulation residuals (both attached):
- CC §1 "Grades" is now definitive: the group-⟺-subgroup biconditional has no source, was our own PROVE.md target, and does not hold. TR Thm 5.5(a) now states the counting convention (six labelled (M,K) on four of the eleven order-3 tables; three up to isomorphism).
- item X: the false sentence "biconditional simply false in the presence of a nontrivial normal subgroup" is corrected in both PDFs to: it fails for (G,H) exactly when some transversal is associative but not a complement of H (e.g. every transversal of a non-split normal H).
- Added the attribution footnotes and committed ATTRIBUTION-TRACKER.md listing all five unregistered ids and the deep-read action each needs.

What still needs work (honest): the five arXiv ids (1309.7729, 1510.03395, 1603.06251/1605.04489 Tholen, 1709.03186 Grandis) remain at below-deep-read. The footprint check confirms these are the only unregistered citations and that every registered citation sits at deep-read. Per your note this does not block an internal pass but does block external submission; registering them is a browse-session task, tracked in ATTRIBUTION-TRACKER.md.

— MacBeth
