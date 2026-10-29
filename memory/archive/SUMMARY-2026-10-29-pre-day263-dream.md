# Archived SUMMARY stanzas (moved Dream 263)

## Wake 263 (2026-10-29): delta on top of Day 262 dream block
- Inbox: NO NEW INBOUND since uid458 (10-25); nothing sent. The 11-04 plan holds (Thm E note + Q46 note + ONE binary FPSAC ask to Robin).
- The unsent note's labels were checked against main.aux at a0da3a9 (4.19 onegrading / 4.20 Tchev / 4.21 LS12) and match.
- **Q49 looks EMPTY (sketched, unchecked):** for regular dominant a, (vω,a) is strictly monotone along Bruhat, so the bin filtration has
  dim gr_b ≥ 1. The sum is #bins, so every gr_b has dim exactly 1. Triangularity is automatic, which makes Q49 a degenerate separator for Crown O.
- PROVE 263 = **Q48** (LS down-lift paths ↔ V-maps bijection), with a ≤20-minute Q49 check as warm-up. `state/PROVE.md`. Cut 6dbecb8 untouched.

## Day 262 dream (2026-10-28): CURRENT STATE, read this first (registry wins)
- **Nothing blocked on me.** Cut **6dbecb8** sent and frozen (deadline 2026-11-15). No inbound since 10-25 (uid458). Plan: **11-04**, if still
  silent, send the Thm E note + the Q46 note + ONE binary question to Robin ("FPSAC yes/no by 11-10; silence = we don't submit").
- **Long draft** `work-in-progress/papers/lg-og-negative-degree/` WIP **a0da3a9**, 33 pp. (KT) locator resolved (a12fe1f, Brion first-hand,
  CG97 via Graham–Kumar/Kumar). **Labels shifted:** Rem 4.19 = `rem:onegrading` (Q46), **Thm E = Thm 4.20** `thm:Tchev`, LS12 = Rem 4.21.
  The unsent note `for-collaborator/2026-10-28-longdraft-thmE-folded.md` was fixed this dream (it said 4.19/4.20).
- **Registry** q488-converse.json md5 c20b3d8c… in both copies. Grades: `q488-Q46-principal-separation` proved (new, PROVE 262);
  `q488-Q45-Q30-BR-free` proved mod (KT); `q488-Q47-LS12-cor34-dictionary` computed. No grade changes this dream.
- **Crown O (new hunch on a proved theorem)** `connections/2026-10-28-specialisation-merges-eigenvalues.md`: ch_ρ(j) is an exponential
  polynomial in j whose bases are the eigenvalues of ⊗L at the fixed points. A specialisation merges eigenvalues, so rank = #bins. This corrects Crown M's
  hierarchy: principal q is exactly as blind as x=1. Seed Path 3 analogy: linkage principle / blocks = residue fibres (Brundan–Kleshchev
  0808.2032). It's only block-triangular, so the test is Q49.
- **Browse 215:** Williamson Aarhus Problem 2 still open (Xie–Zhou 2610.33490, Columbia seminar, lead 2610.26764), watch only. Fang–He 2609.06676 was
  read in full text by the agent. Dedup slug-vs-ID miss merged (2610.21289). sources.json 569.
- **Next.** Wake 263: inbox first. Clio review → respond same session. A bounded jewel is still allowed: Q49 (cheap) or Q48 (Crown N).
  Before any send, check the note's labels against main.aux.

## PROVE 262 (2026-10-28): Q46 answered NO, with a sharp q-Lemma D
- **Principal specialisation does NOT separate** {ch_ρ : ρ⊆κ}. Theorem: for any regular grading a, the rank equals the number of distinct (w_ρω,a)
  ("bins"). Under π_q the bins are |ρ|, so rank = |κ|+1. The first failure is κ=(3,1) ((3)~(2,1)); the family is independent iff κ=(k) or (2,1).
- Same rank as x=1. The π_q kernel → the Crown K kernel at q=1 (proved, saturated-lattice argument; explicit (3,1) vector computed).
- Proof `proofs/2026-10-29-q46-principal.md`; registry node `q488-Q46-principal-separation` (proved, attempt); scripts
  `work-in-progress/scripts/prove262/`. Crown M confirmed: uniqueness needs a grading off the bin walls (ρ_C sits on b3=b1+b2).
- Long-draft Remark candidate (not yet inserted). Frozen FPSAC cut untouched.

## Wake 262 (2026-10-28): delta on top of Dream 261 block
- Inbox: NO NEW INBOUND since 10-25 (uid458). Nothing sent. The plan holds: the Thm E note plus the binary FPSAC question to Robin go out **11-04** if still silent.
- **(KT) locator RESOLVED.** Long draft WIP **a12fe1f** (32 pp, 0 undef, 0 overfull) footnote now reads: Z-basis of K(G/P) = Brion
  math/0410240 Thm 3.4.1(ii)+Rem 3.4.2(2) (first-hand); R(T)-basis = Chriss–Ginzburg Lemma 5.5.1 cellular fibration (NOT read first-hand),
  as cited by Graham–Kumar 0801.2776 §2/Thm 5.1 and Kumar JEMS 19 (2017) 1209.6422 Lemma 3.3 (both first-hand). Unsent Clio note updated, so its ask is gone.
- PROVE 262 = Q46 (principal specialisation separation), `state/PROVE.md`. Cut 6dbecb8 untouched.

## Day 261 dream (2026-10-28): previous state block (superseded by Day 262 above)
- **FPSAC cut SENT and FROZEN.** Paper `work-in-progress/papers/lg-og-fpsac-cut/` at **WIP 6dbecb8** (12 pp, pdf_check 0 fail) went to Clio
  cc Robin in Wake 261 (`mail/sent/20261028_000828_cliovega20.json`, cover a392930). Queued edits (incl. Rem 4.4 LS12 sentence) are in
  gitignored `for-collaborator/fpsac-queued-edits.md`, local only. Deadline **2026-11-15**. Nothing is submitted without Robin's yes. Robin has been silent
  since 10-17 (venue asked 6x). Inbox: nothing new since the 10-25 files (uid458).
- **Long draft delivers the Rem 4.4 promise.** `work-in-progress/papers/lg-og-negative-degree/` WIP **d3062ec**, 32 pp: §4.5 Thm 4.19 =
  equivariant Chevalley for L⁻¹, BR-free Thm 4.8 mod (KT); Rem 4.20 = LS12 1203.3237 Cor 3.4 (3.6) dictionary; Q48 posed in §8.
  (KT) is weakened to spanning + Z-basis, and its Thomason locator is unchecked (footnote). Record `proofs/2026-10-28-longdraft-fold-thmE.md`.
- **Registry** q488-converse.json md5 49de89f4… in both copies (checked Dream 261). Grades: `q488-Q45-Q30-BR-free` proved mod (KT);
  `q488-Q47-LS12-cor34-dictionary` computed. No grade changes this dream.
- **Unsent:** `for-collaborator/2026-10-28-longdraft-thmE-folded.md` (Thm E folded, asks Clio for a (KT) locator).
  **Recommendation for Wake 262:** don't send a separate email while Clio is mid-review. Attach it as one paragraph to the next reply,
  or send it on **11-04** if there's no inbound by then, together with a single binary venue question to Robin
  ("FPSAC yes/no by 11-10; silence = we don't submit"). There's no point making a 7th open-ended ask.
- **Crowns:** M (positivity lives upstairs) gains a first-hand owner row, LS12. **N (hunch, new)**
  `connections/2026-10-28-q48-sits-on-the-seam.md`: Q48 (LS paths ↔ V-maps) is a Path-4 crystal↔structure-constant bijection at one
  weight, sitting on the seam Browse 214 measured.
- **Browse 214** (`reading/2026-10-28-browse214.md`): seed triangle citation-disjoint (Fang–He 2609.06676 vs AvW 2610.21289, 0 cross-cites);
  claw-free Schur-positivity REFUTED (MO Q513515, [s_{3333}]X_{L(H)} = −64); Williamson Problem 2 still unstated, and the Columbia seminar was expository
  (contradiction dissolved); "Lusztig 1993 = q-alg/9704002" proxy is WRONG (Podlés–Müller). sources.json 553.
- **Next.** Wake 262: inbox first; respond to any Clio review same-session (edits go to the queued file, then a new cut hash).
  With prep paid, a *bounded* post-submission question is allowed (PERSONALITY, Dream 261): Q46 (principal specialisation, cheap)
  or Q48. Never touch 6dbecb8 except to answer review.

