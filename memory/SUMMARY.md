# Summary: Rick

## Dream 294 (2026-11-13): CURRENT STATE. Read this first (registry wins).
- **Live arc: Q77 (Seed Q3, MO 406152): q=0 reverse Schur–Weyl centraliser.**
  - Registry `proofs/registry/q77-zero-schur-weyl-dc.json`; proof `proofs/2026-11-13-q77-zero-schur-weyl-dc-fails.md`.
  - **THEOREM (proved, cold read PASS Dream 294, 0 MUST/4 NIT):** A ⊊ B for all n ≥ 2, N ≥ 2n+1. Witness (v·1_C)·h with h = π̄_{w0[1,n−1]}π̄_{w0[N−n+1,N−1]}; dim B/A ≥ C(N−n−1,n−1)−1.
  - Computed, exact: A ⊊ B at (3,6) and (4,8) (N=2n bridge family a_n; B-half proved, ∉A half computed).
  - Computed: A = B at (2,≤4), (3,4), (3,5), (4,5). Proved: A = B for n ≥ N.
  - Undecided: (4,6) (fastB OOM) and (4,7).
  - Hunches: H1 A=B ⟺ N ≤ n+2; H2 A=B ⟺ N ≤ 2n−1 (n ≥ 3).
  - n=2: dim A = Catalan(N); dim B = 43, 142, 493, 1768, 6475, 24052 (N=5..10).
  - Owner gate: NOT FOUND. Deng–Yang JPAA 216 (2012) §4 and Donkin are unread; KSX J. Algebra 240 (2001) is unread.
- **Crown AB** (`connections/2026-11-13-det-sandwich-two-q0s.md`): the failure lives on det ⊗ V^{⊗(N−2n)} ⊗ det.
  - S_0 can't move weight through a det end; H sees the sandwich through one local top.
  - The crystal q=0 (det trivial) and the 0-Hecke q=0 (det a wall) disagree exactly there.
  - Hunch-grade beyond the proved reformulation.
- **Seed scoreboard (most recent first):**
  - Q3: one-sided at q=0 (Q77).
  - Q2: answered negatively at every testable level (Crown AA; Q68/Q69/Q76 closed).
  - Q4: 0-Hecke glues what K_0 splits (Crown X/X′; Q71–Q74 closed).
  - Path 1: Cut Lemma = coproduct as cutting (Crown Z; Q75 closed).
- **External.**
  - Clio: endorsed Q72(i)/Q73 (uid 468); P1b add-on sent (8f29f50); no reply yet.
  - Q77 note `for-collaborator/2026-11-13-q77-reverse-schur-weyl-q0.md` is cold-read and UNSENT. Wake sends it to Clio cc Robin, never MacBeth.
  - An MO post needs Robin's yes.
  - FPSAC is OFF. Publishable-result is held on Robin's `\robin{}` placeholders.
- **Next.**
  - Wake: inbox, then send the Q77 note, then one binary question to Robin (MO answer yes/no by 11-20).
  - PROVE 296 = Q77-b: (4,6) then (4,7) dim B with a chunked sparse Hom solver (harness background); then the partial-sandwich sweep; then the a_n ∉ A proof.
  - Journal: `dream-journal/2026-11-13-day294-dream.md`.

## 11-11 → 11-13 stanzas, compressed (full text in `archive/SUMMARY-2026-11-13-pre-day294-dream.md`)
- **PROVE 295 (11-13).**
  - Q77 Theorem (A ⊊ B, N ≥ 2n+1).
  - (3,6) cert36.py; (4,8) shape.py.
  - fastB/fastA2 engines; n=2 to N=10.
  - Pitfall: 0-Hecke reachability = instance weak order, not Bruhat.
- **Wake 294 (11-13).** Q77 opened. First failure (2,5) 42<43, replayed exactly. The Wake-286 "DC(S_0,H) general" hunch is REFUTED. Ā ≠ Catalan monoid. Harness background beats nohup.
- **Dream 293 (11-13).** Q76-T′ cold read PASS. Crown AA (tableaux see cells, not intervals). BGL 2601.07793 "CIC length ≤6" is UNVERIFIED, don't cite.
- **PROVE 294 (11-13).** Q76-T′ REFUTED n=8 (c=14263758, (1+q)² vs 1+3q+q²). Lemma A/B. coxeter3 driver `proofs/scope294/cox.py`. Q76 CLOSED.
- **Wake 293 (11-13).** Clio 468 review filed (`review` fields, grades stay proved). Cut Lemma owner gate NOT FOUND. P1b add-on SENT (8f29f50/96a2dae). Q76 opened.
- **Dream 292 (11-12).** P1b cold read PASS. Q75 CLOSED. Crown Z.
- **PROVE 293 (11-12).** Q75 P1b PROVED (r_2=1 ⟺ constant/even-alternating) via the NSym Cut Lemma.
- **Wake 292 (11-12).** Q75-R REFUTED (G_{(2^k)} ≇ H*Gr(2,k+2), k=3,4,5). Q75 note sent (4bd8dd7).
- **Dream 291 / PROVE 292 (11-12).** Q75 P1a PROVED + cold read (Hilb = [k+2 choose 2]_q).
- **Wake 291 (11-12).** Clio 466 endorsed the LG cut. Q74 gate NOT FOUND. Q584 conceded.
- **Dream 290 (11-11).** Q74 PROVED + cold read (one-box criterion). Arc Q71→Q74 FINISHED. Crown X′. MO 255757 "mistracked" flag RETRACTED. FPSAC OFF.

## 11-09 → 11-11 stanzas, compressed into pointer lines (full text in `archive/SUMMARY-2026-11-11-pre-day290-dream.md`)
- **PROVE 291 (11-11).** Q74 one-box criterion + Prop S. Corrected Wake 290's mmax=4 artifact (58 special modules at m=5). The 4 special Y are □⊠S.
- **Browse 243 (11-11).** Clean run. Gonzales–Le–Lowen 2609.30257 (toric Richardson H* = QSym / H_* = NSym, Crown X scenery) and Presniakov–Tiskin 2610.26700. sources.json 779→781. The MO flag is retracted (above).
- **Wake 290 (11-11).** FPSAC OFF. Pass C fixes applied (WIP 9fa6b0c). Clio sent the bundle 3ab7f44 + review 2564542 (her 3 notes sound; `peer-claims-clio.json` checked-sober). Q73 owner gate NOT FOUND ×2 (log `reading/2026-11-11-wake290-q73-owner-gate.md`; Liao–Yang–Yu 2410.07990 = KLO Conj 7.2, a different conjecture). Commit 5c2d4a9.
- **Dream 289 (11-11).** Q73 cold read PASS (2 NITs). Its FPSAC GO is superseded by Wake 290.
- **PROVE 290 (11-11).** Q73 = KLO 2310.20571 Conj 7.5 PROVED all n + strong form (∏2^{r−1} summands), eed1cb3, registry `klo-conj75.json`. (G*) is false (56 counterexamples), now explained by Q74.
- **Dream 288 (11-10).** Q72(i) cold read PASS (NIT: the Mackey split is direct at all q, fixed in 5c2d4a9). Crown X born.
- **Browse 241 (11-10).** Q72 owner gate negative: Tewari–vW 1403.1527 is restriction-only (1403.5327 is a different paper). Hackney–Kock–Steinebrunner 2611.08063, Lau–Tan 2601.13555. The OEIS gap 4,20,64,172,424 is a submission candidate.
- **PROVE 289 (11-10).** Q72(i) PROVED all N: Ind(C_I⊠C_J) is indecomposable unless I, J ∈ {(m),(1^m)}. 89f7b44, registry `seedQ4-zero-hecke-induction.json`.
- **Wake 288 / Dream 287 / Wake 287 / Dream 286 / Browse 239 / PROVE 287 / Wake 286 (11-09..10).** MacBeth round-3 verdict sent 31c3fb5. Q71 (⇒) + Q71-U0 PROVED (c0cc6d9, 4d1a94b). Q70 owned by BFKM 2502.09605 L3.7(3). Symmetrisable-crystal 3-way race (HJV 2607.17301 / Lan–Wu–Xiao 2411.09188 / Fei 2610.29051).


## Older history (Days 22–290): pointer
- All pre-11-11 pointer blocks (Days 205–289 per-session pointer lines; Days 22–204 arc paragraphs; the stale Day-212 "Live registry" list) are preserved verbatim in `archive/SUMMARY-2026-11-13-pre-day294-dream.md` lines 168–814, with older full stanzas in the `archive/SUMMARY-*` files they name. Headline results per era are also indexed in the harness MEMORY.md archive blocks. The registry in `proofs/registry/` wins over all of them.

## Identity + collaborators

Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients, type A) and Lyra (systems).

**ALLOWED_RECIPIENTS:**
- **Robin Langer** (langer.robin@gmail.com) — daily email rule active. CC Clio on substantive.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review. Day-190 correction PDF drafted.
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred.
- **Alastair Poole** — thread paused.
- **Scot MacBeth** (scot.macbeth20) — active thread (revision v2 §5).

**Naming:** Rick's pair (so(2N), gl(N)) = Cartan type **DIII**, not BDI.

---

## Streak

- Days 104–212: ~105 wake sessions.
- Arc 2 (b_k/FGCCHA, Days 143–183) closed with a_k > 0.
- Arc 3 (Hikita ⋆-Pieri, Days 189–212): e_2⋆e_2 (191), e_3/e_4 closed forms (193/195), DS launched (196), W_r (206b), **e_k⋆e_r all k (207b)**, **(TC) two-column (209)**, **(★ℓ) ℓ-column (212)**.
- Rule 11 scorecard: 27-1 (last recorded at Day 203; no new fires logged since).

---

## Calibration rules (top hits — full history in git)

- **Rule 11 (Day 148, sharpened Day 161, extended Day 188):** *Unfold the definition before you decorate it.* Now fires in three rooms: derivation (unfold beats import), writeup (novelty audit beats hype), retraction (locator audit beats novelty audit).
- **Rule 12 (Day 149):** *Filtration whose extreme layer τ cannot move.* Externally validated by GDL-W, Marberg, Qiu-Zhang.
- **Rule 13 (Day 150b):** *Name the knob, not "up to normalisation."*
- **Rule 6 v2 (Day 143):** *Object hygiene between frames.*
- **Rule 9 (Day 141):** *Change coordinates when machinery balloons.*
- **Rule 10 (Day 147):** *Integrality-as-target.*
- **Pre-register predictions** (Day 151). **Compute-before-typeset** (Day 157). **Operator respects slice** (Day 159). **Check enumerative-comb literature (BM&J school)** (Day 166). **Prescribed imports need 30-min fit-check** (Day 169). **Weight-grading beats constructive machinery** (Day 167). **Never trust the writeup, only running code** (Day 170). **Convolution ≠ composition** (Day 185). **Log-positivity of Lagrange kernel = unfold for algebraic-GF positivity** (Day 183). **Novelty check same session as writing** (Day 188). **Verify locators in retraction letters** (Day 190). **Residue before machinery** (Day 209 dream; 3/3 by Day 212): I keep predicting straightening or q-Saalschütz, and the proof keeps needing only one rational function plus the residue theorem. **Know the direction of a bug** (Day 212 dream): a cancel-failure can only fake nonzeros, so "vanishes"/"support ⊆" verdicts survive it. **Outbound first in wakes** (Day 212 dream): two wakes died at the 600 s background ceiling with the email unsent.

---

## Compression log
- 2026-11-13 Dream 294: 884 lines / 99 KB → top block + compressed 11-11→11-13 pointer lines + one pointer for Days 22–290; evergreen sections kept (archive `archive/SUMMARY-2026-11-13-pre-day294-dream.md`).
- 2026-10-26 Day 258 dream: PROVE 258 → Day 256 dream stanzas → one top block + pointer lines; Days 240–249 stanzas → 5 pointer lines (74.4 KB → 57.8 KB; archive `archive/SUMMARY-2026-10-26-pre-day258-dream.md`).
- 2026-10-23 Day 253 dream: PROVE 253 / Wake 253 / Day 252 dream / PROVE 252 / Wake 252 stanzas → pointer lines under a new Day 253 dream top block (69.0 KB → 64.6 KB; archive `archive/SUMMARY-2026-10-23-pre-day253-dream.md`).
- 2026-10-16 Day 242 dream: Browse 184–186, Day 241 PROVE/dream, Day 242 PROVE, Wake 241–242 stanzas → pointer lines; new Day 242 dream top block (archive `archive/SUMMARY-2026-10-16-pre-day242-dream.md`).
- 2026-10-09 Day 231 dream: Days 229–230 stanzas → pointer lines (archive `archive/SUMMARY-2026-10-09-pre-day231-dream.md`).

- **Day 217 dream (2026-10-02):** 367 → ~285 lines. Day 215 dream through 216 dream stanzas collapsed to pointer lines. Day 217e/217 wake were tightened. A Day 217 dream top block was added. Pre-prune copy: `archive/SUMMARY-2026-10-02-pre-day217-dream.md`.
- **Day 212 dream (2026-09-30):** the Day 212 PROVE and Day 209 dream blocks were merged into one Day 212 dream top block. Day 209 and Browse 152 moved to pointer lines. Live registry refreshed. Pre-prune copy is in `archive/`.

- **Day 209 dream (2026-09-29):** the Day 207 dream, Day 208 and Day 209 stanzas were merged into one top block. Day 207 dream and 208 moved to pointer lines. Live registry refreshed to the Day 209 state. Pre-prune copy is in `archive/`.

- **Day 207 dream (2026-09-26):** Day 205–207 stanzas collapsed to pointer lines. The Live registry was rewritten from its stale Day 196 state; it had listed e3/e4⋆e_r as computed and their analytic proof as open. Pre-prune copy is in `archive/`. Two questions were closed (q-ek-star-er-via-k-fold-kernel, q-DS-211-promotion).
- **Day 205 dream (2026-09-25):** 90 KB → ~22 KB. Days 190-204 collapsed to pointer lines; the full pre-prune text is in `archive/`. A Day 205 dream stanza with the proof-chain table was put on top. Stale D'Adderio OPEN item removed (refuted Day 197). 4 closed questions moved to `questions/closed/`.

- **Day 196 dream (2026-09-16):** SUMMARY.md +~40 lines (Day 196 dream stanza at top; Live registry updated Day 195→196; Streak + Rule 11 scorecard bumped to 22-1; DS-related fields updated in OPEN and COMPUTED sections). No compression yet — Days 191–195 stanzas preserved in full detail.
- **Day 195 wake (2026-09-16):** SUMMARY.md +~110 lines (Day 195 stanza inserted at top; Live registry updated to Day 195 state with SP/BW/AP-Thm-38 additions; Streak + Rule 11 scorecard bumped to 21-1). No compression yet — Days 191–194 stanzas preserved in full detail.
- **Day 191 dream (2026-09-11):** SUMMARY.md 1633 → ~280 lines. Days 165-184 arc collapsed to arc-paragraphs; Days 130-142 β'-week compressed to bullets; Days 22-129 deep archive kept as pointers. Day 191 PROVE + Day 191 dream + Day 190 wake preserved in full detail (fresh work). Registry section rewritten to reflect post-Day-183 state (arc closed) + Day 190-191 additions.
- **Day 175 dream (2026-09-07):** Quadrilateral collapse crown jewel. Rule 11 scorecard arc-2: 3-0 partial.
- **Day 170 dream (2026-09-05):** Theorem B PROVED stanza added. Days 158-169 arc paragraphs. 1039 → ~340 lines.
- **Day 161 dream (2026-09-03):** 736 → 250 lines.
- **Day 140 dream (2026-08-27):** 675 → 250 lines.
- Prior: Days 118, 127, 133, 136, 138, 157, 159.


## File hygiene notes

- **Registry drift (Dream 294):** `q76-cell-transport.json` and `q77-zero-schur-weyl-dc.json` exist only in `proofs/registry/`, not in the WIP copy. For these two the local copy is the live one; sync to WIP when the Q77 note is pushed.

- **sources.json** `read` paths are now `memory/reading/…`, resolving against the projects root (Day 207 dream fix). Use that prefix for new entries.
- **Registries.** Two copies exist, `work-in-progress/registry/` (pushed) and `proofs/registry/` (local). They were synced Day 207 dream. The WIP copy is canonical; copy local → WIP only when the local file is newer, and check mtimes before copying.
- `rick-research` = the `/home/agent/projects` repo itself, committed every session (e.g. 31329e6, 0591776 Day 242). The old "stale since 09-16" flag was itself stale; dropped Day 242 dream.
- `connections/` ~249 files; the pre-Day-100 β' files are prune-to-pointer candidates.
