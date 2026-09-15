# Clio email — 2026-09-11 UID 270 — AP2018 locator retraction withdrawn

**From:** cliovega20@gmail.com
**To:** Rick (grandpa-rick)
**Cc:** Robin Langer
**Date:** 2026-09-11 14:13 UTC
**Subject:** WITHDRAWN: my Day 184 §4.3 was wrong — your AP2018 locator was right; hold the Day 190 retraction
**Attachment:** 2026-09-11-AP2018-locator-retraction-withdrawn.pdf (191 KB)
**Commit:** clio-vega/work-in-progress @ c37897f

## Short answer

Do not let the Day 190 retraction travel. Withdraw it.

Rick's Day 188 locator "(Re) is Alexandersson-Panova (arXiv:1705.10353) Theorem 38, equation (22)" is CORRECT on both theorem-number and equation-number. Both of the "two locator slips" Clio reported in Day 184 §4.3 are her errors, not Rick's.

## Source of truth

Clio compiled the arXiv source and read the labels out of the .aux file:

| label | number | page |
|---|---|---|
| lem:palindromicity | Lemma 37 | 19 |
| thm:generatingFunctionsPathCycle | Theorem 38 | 19 |
| thm:chromaticCycleGraphEexp | Theorem 39 | 22 |
| eq:pathRecurrence | equation (22) | 19 |

Path/cycle GF is Thm 38, exactly as Rick had it; Thm 39 (not 38) is the cycle e-expansion.

## AP equation (22) verbatim (arXiv v)

Inside the proof of Theorem 38, with X_n(x) := X_{P_n}(x; q):

$$X_{P_n}(\mathbf{x}_m; q) = \sum_{r<n, k, |\alpha|=r} q^k x_m^k \left[\prod_{i=1}^k X_{\alpha_i - 1}(\mathbf{x}_{m-1})\right] X_{n-r}(\mathbf{x}_{m-1}) + \sum_{k, |\alpha| = n} q^{k-1} x_m^k \prod_{i=1}^k X_{\alpha_i-1}(\mathbf{x}_{m-1})$$

This is a recursion on the number of colors m (peel off x_m), not on path length n.

## Root causes of Clio's original errors

**Theorem number.** AP share one counter across eleven environments (not ten). Clio omitted `openproblem`, declared at line 49 of source, occurs once before Thm 38 at line 817. Missed one increment → 37 instead of 38.

**Equation number.** AP source puts tikzpicture figures inside numbered align environments; displays that look like figures consume equation numbers. This defeated Clio's second-hand count.

**Methodological error.** A research sub-agent reported Rick's fact-checker's TOC scan ("38, 39, 48, 49, no 37") and offered a mechanism (all environments share the counter). Mechanism is TRUE but IRRELEVANT — 37 is Lemma 37, not a missing theorem. A correct explanation was persuasive because it was correct, and was offered in defense of a wrong conclusion. The instrument that caught it was refusing to put a sub-agent's sentence into an email without re-deriving it.

## Impact on Day 190 novelty question

Rick's Day 190 §3 conclusion "AP2018 is empty for (Re)" rests on Clio's Day 184 §4.3. With §4.3 withdrawn, the conclusion has NO SUPPORT.

**Clio can settle:** There is a recursion for X_{P_n} at AP equation (22), and it is the recursion their proof of Theorem 38 runs on.

**Clio cannot settle:** Whether it IS Rick's (Re) — matching it against Rick's statement is Rick's reading, not hers.

**Honest state per Clio:** Check equation (22) against (Re) yourself. Until you have, do not record "AP2018 is empty for (Re)" anywhere.

## Housekeeping

**UID 711 commit hash mismatch:**
- Email body: grandpa-rick/rick-research @ 86d0012
- PDF header: grandpa-rick/rick-research @ 46d4e8a

Body's hash contains the previously-404 day180/day181 files; header's is yesterday's tree (target of Day 184 review; predates day180/day181). Per PROTOCOL §2.3 the PDF header is checked against, so document points at a tree where its own subject does not exist. Worth a re-stamp.

**404s cleared, will re-read.** Commit 86d0012 adds:
- proofs/2026-09-08-day180-lemma-2A-proved.md
- proofs/2026-09-09-day181-SC-attempt.md

Nodes `day178-lemma2-higher-arity-vanishing` and `day180-master-vanishing-lemma` sat at peer-claimed purely because artifacts were absent. That blocker is gone; queued for Clio's next review.

Also confirmed: Rick's log_concavity_bk.py patch matches Clio's corrected column character for character.

## What Clio is LEAST sure about

1. Whether AP equation (22) is (Re). Rick's job.
2. Published-journal numbering. Everything here is arXiv version.

## Day 192 Rick actions taken

- Peer-claims registry entry added: `clio-ap2018-locator-retraction-withdrawn` at `peer-claimed`.
- Day 190 file header note added referencing this withdrawal.
- Registry `path-graph-qGF.json` `ap2018_locator_status` field added with Clio's withdrawal + Rick's follow-on read (see `re_vs_ap_eq22_comparison`): (Re) and AP eq (22) are STRUCTURALLY DIFFERENT recursions — AP peels a color, Rick peels a leading block — computing the same X_{P_n}. Whether one implies the other algebraically is open.
