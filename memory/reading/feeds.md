# Reading Feeds

## Browse 158 updates (2026-10-02, second browse session)

### arXiv:2508.07255 novelty-audit CLOSED — confirmed false positive
Full HTML read, targeted string search: no "Hall-Littlewood," no "t=0"/"q=0," no `E_k` operator.
Actual content is Kirillov–Noumi (1998) Dunkl-operator column-creation for Schur/Jack/Macdonald.
The earlier Semantic-Scholar abstract-level match was a mis-paraphrase. Theorem B's operator
formula currently has **no live arXiv novelty-audit lead** — the closest remaining threads both
point off-arXiv: the dormant MO 296383 (Schiffmann–Vasserot Z_{1,l} lemma, secondhand/unread)
and Fayers' unpublished HL-Pieri dual (MO 337891, would need an email).

### New standing reference for the bar-involution/canonical-basis hunch: Beck–Frenkel–Jing, arXiv:math/9806151
Surfaced independently by both the arXiv and web sub-agents this session — a strong signal.
"Canonical Basis and Macdonald Polynomials" (1998, Adv. Math.): bar involution + Macdonald
polynomials (at t=q²) + canonical-basis unitriangularity + positivity/integrality discussion, in
U_q(ŝl₂)'s basic representation realized on symmetric functions. This is the direct intellectual
ancestor of the Day 217 dream's ι=Ψ∘β idea. **Read before further PROVE investment on that
hunch** — paired with Peter Tingley's lecture notes (webpages.math.luc.edu/~ptingley/lecturenotes/
Lusztig-basis.pdf), which give the clean general template: prove bar-involution unit-triangularity
first (existence/uniqueness, crystal-compatible, "elementary"), treat positivity as a separate,
harder fact that doesn't automatically follow — not a failure if Rick's version is "only"
triangular.

### GGS Open Problem 4 — standing TODO closed, still wide open
2601.22287 (the self-citation on GGS 2502.16113 found last session) read at theorem level: it
cites 2502.16113 only once, to name-check B_{q,t} as the object generalized to arbitrary quivers;
the paper itself is pure quiver-variety geometry and defers all algebra (including any contact
with Open Problem 4 / Blasiak et al.'s Y_{m_1,...,m_n} elements) to an unposted companion paper.
No threat, no progress. **Titling correction for the log**: 2502.16113's real title is "The
elliptic Hall algebra and the double Dyck path algebra," not "Smooth correspondences between
quiver varieties" — that title belongs to the citing paper 2601.22287 (same three authors).

### D'Adderio–Interdonato–Iraci–Pagaria 2608.14836 picked up 2 new citations
Interdonato–Iraci's "The Theta Conjecture" (2609.17744) is a direct algebraic sequel (bivariate
Θ-operator refinement, Schröder case proved) — worth a theorem-level read next session, closest
live activity to the standing novelty-risk anchor. Huang–Lau–Ono's Rogers–Ramanujan paper
(2609.20567) cites it only as elliptic-Hall/Negut background; opened a new, fast-moving but
tangential 2026 torus-knot/Rogers–Ramanujan/shuffle-algebra cluster (2608.16086 looks like its
hub) downstream of the compositional rational shuffle theorem, not of Hikita's AHA-level-1 line.

### MO 337891 (Fayers) — live dangling lead
Self-answered "Pieri-type rule for Schur P-functions" thread; a Feb-2021 edit claims an unposted
Hall-Littlewood-function Pieri dual "using duality," dual to Macdonald III.5.7 — "e-mail me for
details." Directly in Rick's HL-Pieri territory if it overlaps.

### FPSAC 2027 — new submission requirement
Confirmed still live, deadline 2026-11-15 unchanged. New this session: submissions require a
mandatory, uncapped "AI declaration" section (excluded from the 12-page cap) — draft this
alongside any eventual abstract, don't leave it to the last week.

### Priority queue (Browse 158)
1. ★★★★★ Read Beck–Frenkel–Jing math/9806151 in full before further bar-involution/canonical-basis PROVE work
2. ★★★ Read Interdonato–Iraci 2609.17744 at theorem level (Theta/Negut novelty-risk watch)
3. ★★★ Read Schiffmann–Vasserot's actual EHA/DAHA paper for the Z_{1,l} lemma (MO 296383 has nothing more to give)
4. ★★ Decide whether to email Matt Fayers about MO 337891's unpublished HL-Pieri dual
5. ★ Retry Matvieievskyi's EHA lecture notes PDF (TLS cert was broken this session)
6. Standing: draft FPSAC 2027's AI-declaration section whenever a submission is prepared

---

## Browse 157 updates (2026-10-02)

### MathOverflow/SE API workaround CONFIRMED WORKING AGAIN — stop treating as permanently blocked
`curl https://api.stackexchange.com/2.3/search/advanced?...` against `site=mathoverflow`/`site=math`
worked cleanly this session (~15 queries, quota 134→117, full bodies via `filter=withbody`).
Browse 156's "permanently blocked" note was about WebFetch/WebSearch directly on the domains —
that block still holds — but the API path (also confirmed in Browse 149) is unaffected and
reliable. Default to the API for MO/SE from now on instead of re-testing the blocked path.

### Top open novelty-audit lead: arXiv:2508.07255 "Non-commutative creation operators for symmetric polynomials"
Surfaced via Semantic Scholar search (Aug 2025, 0 citations, abstract not yet fetched —
rate-limited out). Title is the closest semantic match yet to Rick's Day 217e Theorem B /
operator form (b) target (E_k = sum over k-subsets A of a Vandermonde-prefactor x Hecke-twist
operator producing modified HL at t=0). Fetch and diff term-by-term next session — this is now
the single highest-priority open item from the novelty audit.

### Two near-miss "same genre, different mechanism" structural cousins for the E_k audit
Garsia math/0008188 Thm 16/Eq.(55) (constant-term-in-auxiliary-variables + Vandermonde prefactor,
no explicit Hecke twist) and the classical Negut shuffle-algebra kernel (arXiv:1209.3349,
1004.2575 — subset/block symmetrization with a Vandermonde-type rational kernel, but acting via
the shuffle algebra, not a Hecke element). Neither is a literal match; both are the best
"nothing found" evidence so far that E_k's exact mechanism (subset of actual variables + explicit
T_{s,A}) is not already in the literature.

### MO 296383 — open community question, directly on-territory
"Explicit form of raising and lowering operators in spherical gl(n) DAHA" (score 9, unanswered)
asks for exactly the kind of explicit box-adding Pieri operator Rick's (★ℓ)/E_k program produces.
A comment cites a Schiffmann–Vasserot "hard computational lemma" giving Z_{1,l} explicitly — worth
reading directly if the BGHT ∇-conjugation residual risk needs closing. Possible venue to post to
once the (s,t)-square writeup is public.

### GGS 2502.16113 got its first reverse citation — a self-citation
González–Gorsky–Simental, "Smooth correspondences between quiver varieties" (arXiv:2601.22287,
2026). Unread (rate-limited). Check next session whether it engages their own Open Problem 4 /
§1.3(4) — the closest named external target to Rick's e_a⋆e_λ program.

### Bechtloff Weising standing watch: quiet this cycle
Full 13-paper author sweep shows no new output in 2-3 weeks; still just 1 (self-)citation on
2405.00756. First quiet cycle after 5+ consecutive browses of active output — not necessarily
meaningful, just noting the pattern break.

### FPSAC 2027 deadline reconfirmed directly from raw HTML (not just nav)
maths.universityofgalway.ie/fpsac2027/important_dates/ — submissions open 1 Oct 2026, **deadline
15 Nov 2026** (now ~6.5 weeks out), decisions 15 Feb 2027, conference 5-9 Jul 2027. No topic/
session content related to this arc on either FPSAC 2026 or 2027 pages.

---

## Browse 156 updates (2026-10-01)

### MathOverflow / math.StackExchange: CONFIRMED PERMANENT CRAWLER BLOCK, not transient
`WebSearch`/`WebFetch` on mathoverflow.net and math.stackexchange.com now return an explicit
Anthropic-crawler-block API error (citing Anthropic's own support article on robots-level
blocking). This is a site-owner-level block, not rate-limiting — retrying each browse cycle
wastes budget. Playwright MCP, the standing fallback noted in earlier browses, was **not
available in this session type** (checked via ToolSearch, not registered). Until a Playwright
MCP server is attached to this session type, treat MO/SE as unreachable and skip the community
agent's site-restricted searches (or redirect it to unrestricted WebSearch only).

### New standing reference: symmetricfunctions.com HL and Kostka-Foulkes catalog pages
https://www.symmetricfunctions.com/hallLittlewood.htm and
https://www.symmetricfunctions.com/kostkaFoulkes.htm — dense, well-cited (55+ refs) reference-
wiki pages, directly on-target for the HL-Pieri and cocharge-KF (d_{λμ}(t)) threads of the
Hikita ⋆-Pieri arc. Worth citing in the eventual Theorem H writeup instead of re-deriving
standard facts.

### FPSAC 2027 SoftConf submission portal CONFIRMED LIVE
https://softconf.com/p/fpsac2027/ — active login/registration interface, not a placeholder.
Account creation can happen any time before the Nov 15 2026 abstract deadline. Submissions
require `FPSAC2027.cls`, 12pt, 6-12pp extended abstracts, and a mandatory AI-usage-declaration
section (uncapped length) — directly relevant given this is AI-agent-assisted research.

### Three unrelated "Gaussian"s now live in the same literature corner — disambiguate before writeup
(1) Rick's Theorem (N): a Cherednik-style Gaussian SL2 *commutator* relation. (2) Etingof-Ma
(rational Cherednik algebras, arXiv:1001.0432): a Gaussian *inner product* γ_c(v,v'). (3)
Shakirov (arXiv:2605.25908, elliptic CMM): Gaussian-type *integral evaluation* identities. All
three are in Rick's current search neighborhood; a referee could easily conflate them.

## Browse 154 updates (2026-09-30, second browse session)

### HEADLINE 1: FPSAC 2027 CfP IS NOW LIVE — abstract deadline Nov 15, 2026
`maths.universityofgalway.ie/fpsac2027/important_dates/` updated 2026-09-29. Submissions open Oct 1, 2026; **deadline Nov 15, 2026**; decisions Feb 15, 2027; conference Jul 5-9, 2027. 6-12pp extended abstracts, mandatory AI-declaration section, PC co-chairs D'Adderio/Pilaud/Rajchgot. This has been "still unposted" for 5+ consecutive browses (140 through 153) — the wait is over. Raise explicitly next wake/dream: decide what the Hikita ⋆-Pieri submission looks like with a real ~6.5-week clock running.

### HEADLINE 2: Wick-contraction novelty audit — clean across all four channels, one concrete benchmark found
Dispatched all four browse agents specifically at the Day 212 crown jewel (ℓ-column kernel K_ij = Wick contraction for a free-field realization). Result: **zero direct hits anywhere** (arXiv, MathOverflow/math.SE/physics.SE all clean; citation trails on 4 anchors all quiet). Best structural relative: **Bourgine–Cassia–Stoyan 2508.19704** — has a "generalized Macdonald kernel" + vertex operators + Pieri rule in one paper, but the kernel factors as a power-sum EXPONENTIAL (not a pairwise product over particle indices) and the Pieri rule is e_1-only. This gives a precise, citable novelty statement for a future writeup ("we generalize their e_1 result to general e_ℓ with a genuinely pairwise kernel") — stronger than the vague "pairwise shape looks distinctive" framing from Browse 152/153. Two threads still need direct reads before the audit can be called complete: arXiv:2504.17508 (Chen, six-free-boson DIM realization, unread at theorem level) and the 2013 Saito et al. elliptic-DIM papers (1301.4912, 1309.7094, search-snippet depth only).

**Disambiguation for future searches:** "Macdonald kernel" in the literature (Cherednik q-alg/9610014, Romero-Wen's Cauchy kernel, superspace kernels) means the classical two-alphabet reproducing kernel under the Hall inner product — a different object from Rick's particle-index K_ij. Search "pairwise" + specific operator language instead, not "Macdonald kernel."

**Etingof-Ma Cherednik-algebra lecture notes ruled out** as a home for free-field technology (full-text grep: zero hits on "free field"/"vertex operator"/"Wick"). That technology lives entirely in the Awata-Kanno-Shiraishi-Odake physics lineage; no clean textbook/nLab bridge exists for Rick's specific computation.

**Romero-Wen 2505.15606 deep-read (theorem-level via HTML):** confirmed genuinely different proof technique from Rick's residue-theorem route (plethystic operator algebra + triangularity/degree-counting, no vertex operators/Wick/residue anywhere) — mild positive evidence of technique distinctiveness, not a scoop.

**GGS "Open Problem 4" located precisely:** it's §1.3 item (4) of "Future Directions" (not a literally-titled "Open Problems" section) — cite it that way in future writeups. No answering follow-up found; slot still open.

**Citation trails:** all four anchors (GGS 2502.16113, Hikita 2503.23597, Bechtloff Weising 2405.00756, Graf 2511.01114) completely static since Browse 153 — no new citers anywhere, only self-citations by anchor authors on unrelated directions.

**MathOverflow access confirmed working** via the `curl api.stackexchange.com` workaround again. **Reddit now hard-blocked** at the network level (new, distinct from prior rate-limiting).

### Priority queue (Browse 154)
1. ★★★★★ Decide FPSAC 2027 submission scope — real deadline now, Nov 15, 2026
2. ★★★★ Read arXiv:2504.17508 (Chen, six-boson DIM realization) at theorem level — top remaining novelty-audit gap
3. ★★★ Fetch and check the 2013 Saito et al. elliptic-DIM papers (1301.4912, 1309.7094) directly
4. ★★ Skim Bourgine 2001.04607 / 1905.07087 for technique-transfer (free-fermion/Wick machinery applied to a different target)
5. Standing: email Clio (TC)+(★ℓ) PDFs — now 4+ sessions overdue, do FIRST in next wake

---

## Browse 153 updates (2026-09-30)

### HEADLINE: González–Gorsky–Simental (2502.16113) confirmed as the field's single strongest citation hub — it's the only paper citing both Ion–Wu (stable limit DAHA) and Bechtloff Weising–Orr (parabolic flag Hilbert schemes); its Open Problem 4 is the closest NAMED open problem in the literature to Rick's e_a⋆e_λ program

**GGS 2502.16113** independently surfaced by the arXiv agent AND the citation-trail agent this session (converging evidence, not a coincidence of overlapping search terms — one found it by direct search, the other by literally tracing who cites both anchor papers). Embeds $\mathcal E_{q,t}^{>}$ (positive elliptic Hall algebra) as the spherical subalgebra of Carlsson–Mellit's $\mathbb B_{q,t}$ via Ding–Iohara–Miki generators; constructs a doubled algebra $\mathbb{DB}_{q,t}$ with a Drinfeld-double-style involution to recover the full EHA. **Open Problem 4** (explicit $\mathbb B_{q,t}$-formulas for Blasiak et al.'s generalized $Y_{m_1,\dots,m_n}$ elements, which control shuffle-conjecture Pieri coefficients) reads as the closest existing dated, external, named open problem to Rick's own $e_a\star e_\lambda$ program — a stronger novelty/impact claim than an internal conjecture if the residue-theorem machinery turns out to answer it. Read this paper in full next wake/dream, not just the open-problems list.

**Kernel-shape discriminator holds for a second straight browse.** Kanno–Ohkawa–Shiraishi (2605.16773, re-surfaced) still shows sequential row-product coefficients, not the pairwise/Lagrange-interpolation kernel of Shimozono–Zabrocki (17) that the now-PROVED ℓ-column rule (★ℓ, Day 212) rests on. Best available outside evidence the pairwise-kernel shape is a genuine structural signature, not a generic artifact of "deform an algebra, read off Pieri."

**NEW paper (not previously in sources.json):** Romero–Wen, "Five-Term Relations for Wreath Macdonald Polynomials and Tableau Formulas for Pieri Coefficients" (arXiv:2505.15606, May 2025). Five-term relations (à la Garsia–Mellit) give tableau formulas for wreath-Macdonald Pieri coefficients — structurally close to Rick's "residue-before-machinery" habit (compact identity + specialization beats long straightening). Only abstract read this session; queue a deep-read to compare its $r=1$ case against Rick's residue-theorem route.

**Bechtloff Weising centrality — now a 5-browse-running pattern** (148→150→151→152→153). Most prolific junior author across all three citation-trail anchor networks this session (5+ papers, 2023-2026, solo and with Orr). Treat as a standing watch, not a recurring surprise.

**MathOverflow/math.stackexchange blocked for the third session running** via WebFetch/WebSearch — but Browse 149 found MO reachable via direct `curl api.stackexchange.com` calls, and that workaround was NOT retried this session. Don't conclude MO access is gone until that specific route is retried.

**FPSAC 2027: still no CfP** (checked fpsac.org directly again — dates only). No change since Browse 140.

### Priority queue (Browse 153)
1. ★★★★ Read GGS 2502.16113 in full — field's strongest hub, Open Problem 4 is the closest named external target for e_a⋆e_λ
2. ★★★ Deep-read Romero–Wen 2505.15606, compare five-term-relation route to residue-theorem route at r=1
3. ★★ Retry MO via direct `curl api.stackexchange.com` (Browse 149's working route) before concluding it's blocked again
4. ★★ Continue standing watch on Bechtloff Weising's output
5. ★ FPSAC 2027 — recheck early-to-mid October
6. Standing (not from this browse): email Clio the (TC)+(★ℓ) PDF — outstanding since Day 209/212

---

## Browse 152 updates (2026-09-29, second browse session)

### HEADLINE: EHA↔Hikita-AHA dictionary confirmed genuinely absent from the literature (not just unfound); pairwise-kernel signature confirmed non-generic

**Citation-trail result:** BW 2405.00756 (Thm 5.7, the EHA-side arbitrary-λ Pieri rule) has exactly **1** reverse citation, a self-citation. Nobody has connected it to Hikita's AHA-level-1 side. Hikita 2503.23597 itself is still stuck at 3 reverse citations, no growth since Day 209. The field has not yet noticed either side of Rick's territory.

**Negative result strengthens the ℓ-column template.** Kanno–Ohkawa–Shiraishi's quantum-toroidal super-Macdonald Pieri rule (2605.16773, already known from Browse 144) was kernel-checked properly this session: its coefficients are sequential row-products, NOT the pairwise/Lagrange-interpolation kernel of Shimozono–Zabrocki (17). So the pairwise shape Rick is betting the ℓ-column conjecture on is not a cheap artifact that shows up in every "deform an algebra, read off Pieri" construction — it's a real, distinctive signature, worth more confidence (though this is not itself a test of P-ℓ; the ℓ=3 kill test is still the actual test).

**NEW paper, found independently by 3 of 4 sub-agents:** John Graf, "Constructing Hall-Littlewood Functions via a Deformation of the Bernstein Operator" (arXiv:2511.01114, Nov 2025). Reconstructs the Jing HL vertex operator via a t-deformed Bernstein operator. Single-operator, not k-fold — doesn't touch the ℓ-column frontier — but is a live secondary source for Jing's B_n normalization convention. Cheap follow-up: compare its convention to Jing 1991 literally.

**MathOverflow confirmed empty for the second session running** (19 queries, zero on-territory hits) — don't re-run the identical query set again immediately; territory is stably unclaimed.

**FPSAC 2027: still no CfP.** New find: a dedicated Galway site `maths.universityofgalway.ie/fpsac2027/important_dates/`, actively edited today (stamped 29/09/2026) but still empty. Watch this specific URL, not just fpsac.org.

### Priority queue (Browse 152)
1. ★★★ Continue the ℓ=3 kill test for the pairwise-kernel prediction (PROVE-session work, `q-ell-column-rule.md` task 1) — this browse found no shortcut, only mild supporting context.
2. ★★ Compare Graf 2511.01114's Jing-operator normalization against Jing 1991's original B_n[F] convention — cheap, 15 min.
3. ★ Skim the Shimozono–Zabrocki generalized-Kostka follow-up paper (found via web agent) if the ℓ-column kernel work wants a combinatorial-side hint.
4. ★ FPSAC 2027 — check `maths.universityofgalway.ie/fpsac2027/important_dates/` in October.
5. Standing (not from this browse): email Clio the (TC) proof note — still outstanding since Day 209.

---

## Browse 151 updates (2026-09-29)

### HEADLINE: BW 2405.00756 got a v2 (Aug 2026) with Theorem 5.7 — an explicit ℓ-column/arbitrary-λ Pieri rule on the elliptic Hall algebra side. Day 195's "MISS" verdict on this paper is now STALE — it was checked against v1.

**Bechtloff Weising 2405.00756 v2 (SIGMA 22 (2026) 076).** Theorem 5.7/Cor 5.10: e_r(X)·P_T = Σ_S d^(r)_{S,T} P_S for **arbitrary partition λ** (not single row/column), on graded 𝓔⁺-modules W̃_λ. Combinatorial (sum over tableaux), not a closed GF — different flavor from Rick's level-1 AHA work, but structurally the ℓ-column generalization. No Jing/coset-symmetrizer language. Candidate target: does it collapse to Rick's two-column GF rule under an EHA↔Hikita-level-1 dictionary (not yet checked to exist)?

**Independent re-confirmation: Orr–Weising 2410.13642 Prop 4.2 / §7.2 are NOT a source** for the ℓ-column gate or Jing-identification — confirmed by a browse-agent read today, matching this morning's PROVE-session (Day 209) novelty audit verdict exactly (two independent reads, same day, same conclusion).

**Jing's actual 1991 formula located:** B_n[F] = ⟨z^n⟩F[X−z⁻¹]Exp[(1−t)zX], P_λ = B_{λ1}⋯B_{λr}(1) (Adv. Math. 1991). Never pattern-matched against Rick's k=2,3 coset-symmetrizer computations directly — cheap next step.

**t=0/crystal hunch gets a real literature home:** Mandelshtam–Valencia-Porras 2407.05362 (twisted multiline queues) proves genuine Kashiwara-crystal-operator + TASEP-stationary-measure structure at Macdonald t=0 — structural precedent (not a ready formula) for Rick's "t=0 ⋆-product = geometric mixture" corollary. Contrast case: MO 411889 (HL straightening at t=0) collapses to a single signed term, not a mixture — different phenomenon, worth being precise about when writing up.

**Closest published analogue to the t=0-Markov-chain pattern:** Brauner–Commins–Grinberg–Saliola 2503.17580 (FPSAC 2026) — q-deformed random-to-random shuffle on Iwahori-Hecke algebra, q-positive eigenvalues. S_n/Iwahori-Hecke setting, not level-1 AHA, but worth an actual read before the t=0 writeup (still abstract-only in sources.json).

**MO still has zero threads on Hikita 2503.23597 or AHA Pieri at level 1** — genuinely unclaimed territory. Five tangential open threads found (raising/lowering ops in spherical DAHA MO 296383, HL straightening MO 411889/479825, non-symmetric key-polynomial charge MO 482721, Bernstein operator MO 488867).

**Citation counts static:** Hikita 2503.23597 still 3 reverse cites (unchanged since Browse 150); BW–Orr 2410.13642 still 4, nothing new in 3 days.

**FPSAC 2027 deadline: still not posted** (checked fpsac.org + Galway site directly).

### Priority queue (Browse 151)
1. ★★★★★ Pattern-match Jing 1991 (B_n[F] formula) against k=2,3 coset-symmetrizer computations — decisive, cheap
2. ★★★★ Re-audit BW 2405.00756 v1→v2 diff properly; check if Thm 5.7 collapses to Rick's two-column GF form under an EHA↔level-1 dictionary
3. ★★★ Read BCGS 2503.17580 in full (not abstract) before writing up the t=0 mixture conjecture
4. ★★ Retry third citation-trail seed (Jing vertex operators) — Semantic Scholar 429'd today
5. ★★ Novelty-check Black–Bechtloff Weising "Saturation for Non-symmetric Macdonald Polynomials" (FPSAC 2026) against refuted Route R6
6. ★ FPSAC 2027 deadline — check monthly, not weekly, until it appears

---

## Browse 149 updates (2026-09-25)
- **MathOverflow WORKS via curl to api.stackexchange.com** (1-3 word queries, ~300 anon calls/day); WebSearch/WebFetch on MO are blocked. Helper scripts were /tmp/browse/q.sh, body.sh (ephemeral; recreate).
- **Di Francesco-Vu 2606.12796** upgraded: same parabolic kernel; Lemma A.1/A.2/Thm B.1 candidates for |A|=k residue.
- **MO 296383** (symmetrized power sums of Y-operators matrix elements) and **MO 411889/479825** (non-dominant HL straightening) = community threads closest to my programme.
- **Cautis-Ollivier 2503.21097** (center of generic affine Hecke algebra) - check centrality of e_k(Y)/p_k(Y).
- **Dunkl-Gorin 2412.01938** - degenerate Newton sums of HP operators.
- **Drop** Huang-Lau-Ono 2609.20567 (Rogers-Ramanujan, unrelated).
- FPSAC 2027 (Galway, Jul 5-9): still no CfP; invited incl. Haiman. Announcements list: lists.ruhr-uni-bochum.de/mailman/listinfo/fpsac-announcements.
- WebFetch summarizer can fabricate paper content - verify with PDF.

## Browse 147 updates (2026-09-17)

### HEADLINE: Thibon 2609.10284 — B_1² = α·Δ_2 + α·B_1 + 2·B_2 is the stable-limit template for Sub-Lemma Z; Thibon's Δ_3 now proved (but Jack-level only); Rick's (q,t) is stronger

**2609.10284 (Thibon, Sept 9 2026) — HIGHEST PRIORITY READ.** Proves Δ_2(α) and Δ_3(α) in spherical degenerate DAHA / stable limit. Key Newton identities: α·Δ_2 = B_1² - α·B_1 - 2·B_2 and α·Δ_3 = B_1³ - 3B_2·B_1 + 3B_3 - 3α·B_1² + 6α·B_2 + 2α²·B_1. Rick's R7 = level-1 specialization of k=2 formula (with α·B_1 cross-term VANISHING at level-1 — this is the key theorem to prove for Sub-Lemma Z). Rick's k=3 formula also matches Thibon's k=3 template.

**Thibon's Δ_3 is NOW PROVED** (in 2609.10284, not just conjectured). But at the Jack/degenerate level only. Rick's p_3(Y)-Pieri is at the full (q,t)-Macdonald level — strictly stronger. Update FPSAC framing: cite 2609.10284 as context, state Rick's (q,t) result as extension.

**Hikita 2503.23597 slot confirmed clear (eighth novelty audit).** Zero genuine forward cites. Hikita himself flags Schur-Pieri and depth-2 as open in the paper. Rick's Sub-Lemma Z is the natural next step per the author.

**D'Adderio as FPSAC 2027 PC Chair.** Same D'Adderio as Route-2 paper (2608.14836). Rick's FPSAC 2027 abstract should clearly distinguish Rick's level-1 polynomial closed forms from D'Adderio's A_{q,t} Macdonald expansion approach.

**t^r-Laurent naming: confirmed novel, safe to use.** No standard term exists. "Polynomial in t^r" is the cleanest existing language.

**Crystal r-stability: NOT a match to Rick's phenomenon.** Kirillov-Shimozono level-restricted Kostka stability (math/0001114) is about truncation-cutoff irrelevance at high level, not AHA Newton cancellation. Rick's r-independence is novel.

### Priority queue (Browse 147)
1. ★★★★★ Sub-Lemma Z via Thibon's quadratic relation — specialize B_1² = α·Δ_2 + α·B_1 + 2·B_2 to Hikita level-1; identify why α·B_1 vanishes applied to e_r; this = analytic proof of Sub-Lemma Z
2. ★★★★ Read Di Francesco-Vu 2606.12796 (k-th powers of Macdonald operators, June 2026) — background on k-th power hierarchy structure
3. ★★★ Verify Thibon 2609.10284 Thm 8.2 Δ_3 formula at q=1, t→t^α against Rick's k=3 Day 201 closed forms
4. ★★★ BHMPS 2025 raising operator paper — find arXiv ID, check for AHA-level content
5. ★★★ Hikita 2410.12758 Dec 2025 revision — read survey section for star-product/AHA exposition
6. ★★ FPSAC 2027 abstract v3: update to cite 2609.10284; clarify (q,t) vs Jack framing; distinguish from D'Adderio
7. ★ Subscribe to FPSAC announcements list; check deadline weekly from October 1

---

## Browse 146 updates (2026-09-17)

### HEADLINE: Route R6 candidate (Bechtloff Weising EHA); Thibon's Δ_3 conjectured ← Rick's k=3 is theorem; r-independence confirmed novel; "Baxter-k" naming conflict

**2310.10249 (Bechtloff Weising, Oct 2023) — Route R6 candidate.** EHA (Elliptic Hall Algebra) representations with explicit e_r Pieri for ALL r. EHA surjects onto Hikita level-1 AHA. If e_r formula descends cleanly through the surjection, Newton's p_k(Y) decomposition gives an analytic proof of Lemma 1. Read §§1-3 directly. **Highest priority new read after R5 exhaustion.**

**2608.25651 (Thibon, Aug 2026) — Δ_k(α) operators.** Jack degeneration of Rick's p_k(Y). Δ_2 explicit; Δ_3 and Δ_4 CONJECTURED. Rick's k=3 computation (5 r-indep + 2 r-dep, verified r=1..4) constitutes a THEOREM where Thibon has a conjecture. Read Δ_2 formula against Lemma 1 at q=1 for consistency check.

**r-independence novelty confirmed (seventh audit).** Survey of all comparable Pieri papers (Baratta 0806.2695, 1008.0892; van Diejen 1209.3291, 1009.4486; Jing-Liu 2310.15730): every one has weight-dependent coefficients. Rick's r-independence is new across all literature.

**Newton at operator level not done before.** Lassalle-Schlosser use Newton in classical Λ — nobody uses it at the Y-operator level inside an AHA.

**"Baxter-k" naming conflict.** "Baxter" means (a) XXZ Q-matrix, (b) spherical Hecke Macdonald diagonalizer — both different from Rick's t^{jr} monomial count. Rename before writeup.

### Priority queue (Browse 146)
1. ★★★★ Read Bechtloff Weising 2310.10249 §§1-3 — assess Route R6 feasibility
2. ★★★★ Download 2608.25651 — compare Δ_2 with Lemma 1 at Jack degeneration; Δ_3 vs k=3 empirical
3. ★★★ Verify c_{r+3} Baxter-4 at r=5 (computational, in progress)
4. ★★★ Test k=4 p_k(Y)-Pieri predictions
5. ★★ Rename "Baxter-k" notation before FPSAC 2027 abstract v3
6. ★ FPSAC 2027 deadline — check mid-October 2026

---

## Browse 145 updates (2026-09-16)

### HEADLINE: Thibon 2608.30791 resurfaces as p_2(Y)-Pieri proof route; novelty sixth audit clean

**Thibon 2608.30791 — new connection.** Deep-read in Browse 125 for Psi=F validation. NOW relevant for the p_2(Y)•e_r arc (Day 198). Triple composition Thm 2.3 (f̂ = D_t ∘ Cauchy ∘ nabla(f)) + Nazarov-Sklyanin A^{(2)} eigenvalues give the q,t-Δ_2. KEY QUESTION: is A^{(2)} = p_2(Y) in Hikita's level-1 normalization? If yes → analytic proof of Lemma 1 (p_2(Y)-Pieri) from Thm 2.3 directly.

**Triangle confirmed:** D'Adderio 2608.14836 Negut D_{(2,0)} ↔ Theta operators ↔ Thibon A^{(2)}. All are q,t-analogs of p_2(Y). Rick's p_2(Y) in AHA level-1 sits on this triangle.

**Thibon 2609.10284 §7.1:** P_2^{(N)} = Σ p_{i+j} D_i D_j + θ Σ p_i p_j D_{i+j} + Σ ((1-θ)k+θN) p_k D_k. Applying to e_r in stable limit → Jack version of Rick's Pieri Lemma. q,t-deformation lives in 2608.30791.

**NEW paper: Chen-Lu-Ruan 2601.13497** — "Double Hall-Littlewood symmetric polynomials." Jan 2026. Pieri rules via Jordan quiver Hall algebra. Different from Rick's AHA level-1 but same Pieri-via-Hall-algebra pattern. Not competing.

**0806.2695** — "Pieri-type formulas for nonsymmetric Macdonald polynomials" (2008, author unverified). Community agent flagged as potentially pushing DAHA Pieri down to Hikita's quotient. VERIFY before relying on.

### FPSAC 2027 — University of Galway, July 5–9, 2027. No deadline yet (Important Dates 404).
Check fpsac.org October 2026 or email fpsac2027@universityofgalway.ie. Historical pattern: deadline mid-to-late November 2026.

### Sixth novelty audit — clean
- Hikita 2503.23597: still 3 cites, none on Pieri
- "Pieri affine Hecke level 1": ZERO arXiv results
- "quantum toroidal Pieri Macdonald explicit": ZERO arXiv results
- DS conjecture (e_λ^{(q,t)} dominance-triangular with q^{-n(λ)} leading coeff): NOT IN LITERATURE
- p_2(Y)•e_r formula: gap confirmed, Rick is filling it

### Priority queue (Browse 145)
1. ★★★★ Re-read Thibon 2608.30791 Thm 2.3 — compute A^{(2)}•e_r explicitly; check if c(e_{r,1,1}) = 1/q³ comes out
2. ★★★ Apply Thibon 2609.10284 §7.1 P_2^{(N)}•e_r → stable limit → compare with Rick's 4-term empirical Pieri
3. ★★★ Download 0806.2695, verify title/authors, check for e_2-type DAHA Pieri
4. ★★ FPSAC 2027 deadline: monitor October 2026
5. ★ Chen-Lu-Ruan 2601.13497: note for future Hall-algebraic Pieri unification arc

---

## Browse 143 updates (2026-09-16)

### HEADLINE: Two analytic routes identified for Lemma-3.11-analogue

**Stokman-Rains Lemma 10 (2307.02385):** $e_r(Y_1,\ldots,Y_N) = \frac{1}{[N-r]_t![r]_t!} S^t_N Y_{N-r+1}\cdots Y_N$ for ALL $r$. Check: does $Y_{m-1}Y_m = t^{-1}(\Pi T_1\cdots T_{m-2})^2$ hold in Hikita's AHA? 30-min SymPy. If yes: Lemma-3.11-analogue for $e_2$ falls out directly.

**Thibon 2609.10284 (Sept 9, 2026):** Degree-2 content operator $\Delta_2(\alpha)$ in degenerate DAHA. Priority read: if lifts to Hikita's $(q,t)$ level-1 AHA, gives $p_2(Y)$ closed form and closes the Newton's-identity route to $e_2 \star e_r$ analytically.

### FPSAC 2027 — deadline STILL NOT POSTED (as of 2026-09-11)
Important Dates page blank. Expect October 2026 opening, November deadline. Subscribe to announcements list.

### Novelty status (Browse 143)
Hikita 2503.23597 still at 3 SS entries (unchanged from Browse 142). Zero papers building on $\star$-product structure. Colmenarejo-Klein 2601.23170 = background cite only (total CQF, no $(q,t)$, no Pieri). Kim-Lee-Yoo 2506.23082 = HL via linked rooks, single-$q$ SW framework, no Hikita cite. **Rick's $e_a \star e_b$ slot fully clear.**

### Griffin-Mellit et al. (FPSAC 2026) — arXiv:2504.06936
Uses $\mathbb{A}_{q,t}$ to expand $q$-CQF into Macdonald polynomials. PARALLEL (not competing) to Rick's approach. Must cite prominently in FPSAC 2027 abstract. Key framing: their $\mathbb{A}_{q,t}$ framework doesn't produce $e_a \star e_b$ Pieri; Rick's $\star$-product does.

---

## Browse 141 updates (2026-09-11, second browse same day)

### HEADLINE: $e_a \star e_b$ Pieri ($a \ge 2$) = genuinely open, zero competition confirmed
Day 191 closed $e_2 \star e_2$ and conjectured $e_2 \star e_r$ (computed, $r \le 4$). Browse 141 confirms: ALL established Pieri rules in affine Hecke / Macdonald / quantum group literature are $e_1$-type only. Hikita explicitly flags $e_a \star e_b$ ($a \ge 2$) as open. Rick has genuinely novel content. Hikita 2503.23597 now has 1 genuine forward citation (Colmenarejo-Klein 2601.23170, different direction — total CQF, no (q,t)). (q,t)-path-graph slot still open.

### FPSAC 2027 — deadline NOT posted (as of 2026-09-11)
Historical pattern: submission opens ~October 1, deadline mid-to-late November. **Check fpsac.org in early October 2026.** Program committee: D'Adderio/Pilaud/Rajchgot. FPSAC 2026 proceedings now online: sites.math.washington.edu/fpsac2026/proceedings/

### Kim-Lee-Yoo 2506.23082 — DOES NOT SPECIALIZE TRACTABLY TO P_n
Confirmed Browse 141: focuses on Dyck-path unit interval orders (not P_n explicitly); works in one-parameter Hall-Littlewood (different parameter regime from Hikita's (q,t)). No tractable P_n specialization worked out. LOW PRIORITY for Rick.

### Tom-Vailaya follow-up — "Tutte symmetric matrix" already in sources.json (2603.27129)
Their gluing formula is q=1 only. No (q,t)-lift. Matrix multiplication structure is a potential TARGET for (q,t)-lift but not done in either paper. 9 citations stable.

### NEW LIMITING-CASE CONSTRAINT: van Diejen-Emsiz-Zurrian 2305.01931
Affine Pieri for periodic Macdonald → at $t=0$ = cylindric HL Pieri. All $e_1$-type. Potential sanity check: does $t \to 0$ of Rick's $e_2 \star e_r$ formula recover anything here? 15-min check.

### PRIORITY QUEUE (Browse 141)
1. **Compute $e_3 \star e_2$, $e_3 \star e_3$** ★★★ — validates $\min(a,b)+1$ term conjecture; strengthens FPSAC anchor
2. **Analytic proof of $e_2 \star e_r$** ★★★ — Lemma-3.11-style extension (Day 191 identified this as next route)
3. **Sanity check: $t \to 0$ of $e_2 \star e_r$ vs. cylindric HL Pieri** ★★ — van Diejen-Emsiz-Zurrian 2305.01931
4. **FPSAC deadline: check fpsac.org in early October** ★★★ — historical pattern = October opening
5. **FPSAC 2026 proceedings browse** ★★ — sites.math.washington.edu/fpsac2026/proceedings/ — any (q,t)-CQF talks?
6. **Trinh "Haiman's Conjecture and Springer's Representations"** ★ — already in sources.json (2605.20131); abstract fetch for Hikita-Springer fiber connection

---

## Browse 140 updates (2026-09-11)

### HEADLINE: Rick has the (q,t)-path-graph slot to himself
Hikita 2503.23597 gives (q,t)-CQF for unit interval graphs + "recipe for oriented graphs" (Ellzey input). Thm 3.12 (quantum Pieri: e_1 ⋆ e_r = (1−q⁻¹)[r+1]_t e_{r+1} + q⁻¹e_1·e_r) has ZERO citing papers. Nobody has computed X_{P_n}(x;q,t) explicitly or applied the recipe to directed paths. Rick's FPSAC 2027 angle is clear.

### ELLZEY AUTHOR CORRECTION
Brittney Ellzey (not "Melody"). arXiv:1709.00454. Eq (6.7) = Rick's (Comp) formula, short subsidiary result for directed P_n (Section 6 is primarily about C_n). GF form F[E(qz)−qE(z)]=(1−q)E(z) NOT in Ellzey or SW10.

### NEW PAPER: Kim-Lee-Yoo 2506.23082
"Hall-Littlewood expansions of CQF using linked rook placements" — fills t=0 corner of (q,t)-picture for unit interval graphs. Check if it specializes to path graphs tractably.

### FPSAC 2027 — DEADLINE IMMINENT
July 5–9, Galway. Committee: D'Adderio/Pilaud/Rajchgot. Deadline NOT posted but historical pattern = Oct–Dec 2026. Monitor fpsac.org urgently. Abstract anchor = explicit X_{P_n}(q,t) + recursion conjecture.

### PRIORITY QUEUE (Browse 140)
1. **Compute X_{P_2}(q,t), X_{P_3}(q,t) via Hikita recipe** ★★★ — apply recipe to Ellzey's directed P_n CQF. First explicit (q,t)-formula in the literature.
2. **/expository Hikita §2** ★★★ — understand ⋆-product, q_{(m)} map, affine Hecke mechanics (Day 190 agenda)
3. **Kim-Lee-Yoo 2506.23082 check** ★★ — does HL expansion specialize to P_n tractably?
4. **Tom-Vailaya 2503.19344 vertex-gluing** ★★ — 9 citations, may give Leibniz mechanism for ⋆
5. **OEIS submit κ_k = (3,18,228,3414,57051)** ★ — still absent, send Robin for confirmation

---

## Browse 134 updates (2026-09-08, post-Day 179 PROVE / Lemma 1)

### HEADLINE: Stanley-Gasharov conjecture DISPROVED (July 2026)
Matherne-Morales 2607.21508 + Wang-Zhang-Zhao 2607.27166: claw-free does NOT imply Schur-positive. e-positivity (SW program) survives unaffected. FPSAC abstract should explicitly frame around e-positivity, not chromatic positivity generally.

### STRUCTURAL UPGRADE: Path graphs are the generative set
Huh et al. 2504.09123 (restricted modular law): e-positivity of X_G for all unit interval graphs REDUCES to e-positivity for all path graphs P_n. Rick's Theorem B (algebraic GF for X_{P_n}) is therefore the key building block for the post-Hikita program — not just a test case. This is the most important structural positioning result for Rick in this browse.

### TOP ACTION ITEM: Chow 2603.23879 "Bulldozer" comparison
Chow's watershed statistic gives a combinatorial model for the same e-coefficients Theorem B generates algebraically. 20-line SymPy test: compare watershed formula vs Theorem B output for P_3, P_4. If match: first combinatorial model for Fact 8 / Claim (X).

### Priority queue update (Browse 134 additions)

1. **Chow 2603.23879 comparison** ★★★ — 20-line SymPy, watershed vs Theorem B (supercedes Cho-Park comparison as top item; both should run)
2. **Cho-Park 2607.03284 comparison** ★★★ — 20-line SymPy, path-graph CQF vs Theorem B (still queued)
3. **Huh et al. 2504.09123 deep-read** ★★★ — restricted modular law; path graph centrality
4. **Guay-Paquet 2507.05614 structural check** ★★ — does D_n sit in divided-difference algebra?
5. **INVERTi check for b_k** ★★ — Zabrocki 2505.06941; 30-min computation
6. **"Modular law through GKM theory (2024)"** ★★ — find this unindexed preprint (in Guay-Paquet refs)
7. **FPSAC 2027 abstract draft** ★★★ — call expected Nov/Dec 2026; ~2 months to prepare

### Landscape update (Browse 134)
- Stanley-Gasharov dead → field bifurcated: (a) survive and prove e-positivity, (b) find more counterexamples
- Carlsson-Mellit A_{q,t} is the dominant algebraic engine (Griffin-Mellit, Theta conjecture, Cho-Oh, Trinh)
- Nabla/BGHT conjecture burst: Qu, Qiu-Zhang, anon closed old conjectures via LLT
- Hikita 2503.23597: (q,t)-chromatic via affine Hecke algebras — Path 3 applied directly
- Buchacher 2512.21753: best catalytic variable lecture notes (no BM survey exists)

---

## Browse 133 updates (2026-09-07, post-Day 177 PROVE / Claim X)

### TOP NEW ACTION ITEM: Cho-Park path-formula comparison

**arXiv:2607.03284** (Cho-Park) proves explicit e-positive formula for lollipop graph CQF; **path graphs P_{n+1} = L_{1,n}** are special cases. Formula: Σ_{h-admissible w} q^{ℓ_h(w)} e_{λ(w)}. Must compare with Theorem B for n=3, 4 (20-line SymPy). If they match: (a) Theorem B is verified from an orthogonal direction; (b) may illuminate Fact 8's operator structure.

### FPSAC 2027 speaker list (updated)

Now 7 confirmed invited speakers: Bouvel (BM&J), Alex **Fink** (matroid/tropical), Haiman, **Iyama** (cluster algebras), **Marietti** (KL-Coxeter), Mishna (D-finite), Yip (symmetric fn). No deadline yet.

### Guay-Paquet 2507.05614: revised assessment

Browse 127 noted: "ZERO overlap with ν-system/Riccati." STILL TRUE for that machinery. **New question (Browse 133)**: does Guay-Paquet's divided-difference algebra (categorifying the modular law) contain Rick's shift operator D_n as a natural element? Browse 127's "no overlap" was for the BM&J side; the Fact 8 / Schubert calculus side is a new question. 20-minute structural check queued.

### Priority queue update (Browse 133 additions)

1. **Cho-Park 2607.03284 comparison** ★★★ — 20-line SymPy, path-graph CQF vs Theorem B
2. **BM's SLC67 catalytic survey** ★★ — read before writing FPSAC abstract (URL: http://www.mat.univie.ac.at/~slc/wpapers/s67vortrag/bousquet.pdf)
3. **Guay-Paquet 2507.05614 structural check** ★ — does D_n sit in his divided-difference algebra?
4. **b_k OEIS submission** ★ — sequence 3, 27, 417, 7851, 164124, ... still novel; submit eventually

### Landscape update

Three-level Schur positivity hierarchy now established (Schur-pos ⊊ strongly-nice ⊊ nice). Multiple 2026 conjectures falling to computation. GDL-W Schur-log-concavity (0 citations, too new) is the only remaining Narayana-adjacent open conjecture.

---

## Browse 129 updates (2026-09-05, post-Theorem B / Day 170)

### STATUS: THEOREM B PROVED (Days 169-170). Year arc complete.

The central result of the year is proved. The field landscape for next steps:

### Shareshian-Wachs q-positivity — CONFIRMED OPEN, Rick's next target

Hikita Conjecture 2.6 (2410.12758): c_λ(Γ;q) ∈ ℤ≥0[q] as polynomials. This is the
only remaining major open problem in chromatic QSF theory. Nobody has a GF-level approach.
Rick's Theorem B is the first algebraic structure that could yield this for P_n.

### PRIORITY READ QUEUE (Browse 129)

1. **arXiv:2503.19344** (Tom-Vailaya) ★★★ — "Graphs Glued at Single Vertex." Does their
   e-positivity gluing theorem cover P_n? If yes, e-positivity of X_{P_n} is a corollary.
   9 citations, fast-rising. READ FIRST.

2. **arXiv:2603.23879** (T.Y. Chow) ★★★ — "Foata, Hikita, and the Bulldozer Problem."
   Combinatorial interpretation of Hikita's denominator-cancellation mechanism. May illuminate
   Rick's q-positivity gap via algebraic-vs-bijective comparison.

3. **arXiv:2509.22946** (Beck-Braun-Cornejo) ★★ — "Generating Functions of q-Chromatic
   Polynomials." Closest community paper to Rick's GF approach. Different invariant, but
   parallel structure.

4. **arXiv:2504.09123** (Huh-Hwang-D.Kim-J.Kim-Oh) ★★ — "Refinement of Hikita's
   e-positivity via g-functions." The q-positivity refinement paper; 3 cit. Strong P-tableaux
   are the current community handle on e-coefficients.

5. **Hikita q-independence check** ★★ — 20-line sympy. Verify Rick's GF reproduces Hikita
   Thm B.iv (e-coefficients independent of q) for P_n. 

6. **Kim-Lee-Yoo HL expansion check** ★★ — 10-line sympy. Verify Rick's GF at t=0 matches
   Hall-Littlewood expansion of CQF (arXiv:2506.23082) for small n.

7. **arXiv:2609.03840** (Cho-Oh, Sep 2026) ★ — "HHL formula via Carlsson-Mellit Algebra."
   Brand new (0 cit). Technical extension of Griffin-Mellit. Rick's ψ might be recoverable.

8. **Siegl strong P-tableaux check** ★ — Does Rick's ν-system count strong P-tableaux?
   If yes, proves Siegl's new (Sep 2026) lower bound conjecture for P_n.

### CORRECTIONS from Browse 127/128

- **arXiv:2408.14455** (Aliniaeifard et al.): Browse 127 called this "Rick's exact object."
  CORRECTED: symmetry characterization only. No GF, no Riccati. REMOVE from high-priority.
- **arXiv:2502.09072** (Novelli-Thibon JCTA 2025): Browse 127 called this ★★★ PRIORITY.
  CORRECTED: NC Macdonald, no path-graph GF. DOWNGRADE to low-priority.
- **Siegl 2509.02841**: Browse 127 said "SW q-positivity was proved by SW 2016; Siegl repackages."
  CORRECTED: Siegl's 2026 paper proves LOWER BOUNDS for e-coefficients via strong P-tableaux.
  The "Siegl" in Browse 126 was a different paper (Thm 1.10). The new Siegl is a new result.

### FPSAC 2027

July 5-9, Galway. Deadline ~April 2027 (call for papers Nov/Dec 2026). PC: D'Adderio,
Pilaud, Rajchgot. Invited: Haiman, Martha Yip. Rick's submission framing: Theorem B fills
the GF gap that Hikita/Griffin-Mellit leave open. Cite Griffin-Mellit 2504.06936 prominently.

### NEW dominant hub: Griffin-Mellit 2504.06936 (14 cit in 5 months)

Proves SS via A_{q,t} algebra. Hall-Littlewood at t=0. Does NOT prove q-polynomial positivity.
No path-specific GF. Deep-read complete (Browse 129). Rick's techniques are orthogonal.

---

## Browse 127 updates (2026-09-04, post-Day-165)

### PROOF MACHINE FOR Σ_0 — Bousquet-Mélou & Jehanne math/0504018

Canonical algebraicity tool: polynomial equation P(F(u), F₁,...,Fₖ, t, u) = 0 with "catalytic variable" u → F algebraic (kernel method: find zero of kernel, close by resultants). Σ_0 is rational in u = E₁T (degree 1 algebraic) → kernel collapses trivially → first-order ODE suffices. **Day 166 PROVE: rewrite Day 164's Riccati ODE for Σ_0 as P(Σ_0(u), Σ_0(0), u, E₂, T) = 0 and apply BM&J.** This is the path from "checked-sober" to "proved."

### FPSAC novelty — FULLY CLEARED

- **Guay-Paquet 2507.05614**: DEEP-READ in Browse 127. Works in equivariant cohomology (Schubert calculus / divided differences). ZERO technical overlap with Rick's ν-system/Riccati/GF machinery. Remove from priority read queue.
- **Siegl 2509.02841**: RESOLVED in Day 165 direct read. SW q-positivity was proved by SW 2016; Siegl repackages. Remove from urgent queue.
- **SW q-positivity CONFIRMED OPEN** (Hikita FPSAC 2025 slides; arXiv:2210.03803 May 2025 update). Rick's approach is the only GF-level attack.

### CRITICAL UNLOGGED PAPER — arXiv:2408.14455

Aliniaeifard, Asgarli, Esipova, Shelburne, van Willigenburg, Whitehead McGinley (2024). "Chromatic Quasisymmetric Functions of the Path Graph." Annals Combinatorics 2025. Rick's **exact object**. Characterizes when X_{P_n}(x,t) is symmetric (different from SW positivity). No GF methods. Must read for: (a) knowing what's proved; (b) e-coefficient cross-checks for Σ_0; (c) van Willigenburg group awareness. ★★ PRIORITY.

### NEW Novelli-Thibon paper — arXiv:2502.09072

"Noncommutative chromatic quasisymmetric functions, Macdonald polynomials, and the Yang-Baxter equation." JCTA 2025. Unlogged. Novelli-Thibon's geode paper (2511.18366) gave Rick's quadratic identity bridge; this NEW paper does chromatic QSF in NSym/QSym + Macdonald + Yang-Baxter. Could carry analogous structural leverage. ★★★ PRIORITY.

### OEIS A032443 — algebraic identity for Σ_0 proof

A_Q(W) · C(W) = 1/(1-4W), i.e., Σ Q_k · Cat_{n-k} = 4^n. Somos formula: Q_k = [x^k](4x+1/(1+x))^k — Lagrange inversion kernel φ(x) = 4x+1/(1+x). Combinatorial: 4-ary words where #1's ≤ #0's (Scambler 2012). These may give a direct combinatorial proof of the Σ_0 form, independent of BM&J.

### Cigler 2604.24207 — FULLY READ (Browse 127)

Four J-fraction theorems at q=-1. Key identity (Sec 6): c(t,z)·c(-t,-z) = C(t²,z²) where φ(t,z)=1+(1+t)z. **Rick's test: ψ(Y,-1,...) vs Cigler's c(t,z) — 20-line sympy.** Paper is now sources.json `deep-read`; remove from "need to read" queue, add to "need to test" queue.

### Updated priority queue (Browse 127)

1. **Day 166 PROVE: BM&J Σ_0 attack** — rewrite Riccati ODE as catalytic variable equation, apply kernel method. FIRST priority.
2. **arXiv:2502.09072** (Novelli-Thibon JCTA 2025) ★★★ — NEW: noncommutative chromatic QSF.
3. **arXiv:2408.14455** (Aliniaeifard et al., 2024) ★★ — Rick's exact object, unlogged.
4. **20-line Cigler q=-1 test** ★★ — check ψ at q=-1 vs c(t,z).
5. **arXiv:2503.23597** (Hikita) ★★ — check quantum Pieri rule → Riccati recursion for Σ_n X_{P_n} y^n.
6. **arXiv:2401.01027** (Wang-Zhou "neat formulas") ★ — 11 citations; closed-form CSF expressions.
7. **arXiv:2604.24207** (Cigler) ✓ READ — only test remaining.
8. **arXiv:2507.05614** (Guay-Paquet) ✓ READ — ZERO overlap, novelty safe. Remove queue.
9. **arXiv:2509.02841** (Siegl) ✓ READ (Day 165) — resolved. Remove queue.

### FPSAC 2027 update

PC co-chairs confirmed: D'Adderio, Pilaud, **Rajchgot** (Rajchgot = new, not in prior notes). **Martha Yip** (chromatic symmetric functions) is an invited speaker — means expert eyes on Rick's submission from the start. Deadline: TBD, check October 2026.

---

## Browse 128 updates (2026-09-05, after Day 168 PROVE)

### UPGRADE: Use Notarantonio-Yurkevich SYSTEMS extension, not base BM&J

arXiv:2211.07298 (Notarantonio-Yurkevich 2022) extends BM&J from a single catalytic equation to SYSTEMS of n≥1 discrete differential equations in one catalytic variable. Gives **effective degree bounds** for minimal polynomials — computable before guessing the closed form. Rick's ν-system = multiple coupled equations → this is the right tool. Follow-up: arXiv:2310.12812 (FPSAC 2023 version). DDE-SOLVER Maple package: arXiv:2509.08639. **Strategy: compute Notarantonio-Yurkevich degree bound for Σ_0 before guessing closed form.**

### CORRECTED: arXiv:2408.14455 is symmetry characterization only

Browse 127 called 2408.14455 (Aliniaeifard et al.) "Rick's exact object unlogged." HTML deep-read confirms: the paper proves X(P_n; x, q) is symmetric iff the labeling is natural or reversed. **NO generating function, no Riccati, no catalytic variables.** Low direct relevance for Rick's GF program. Remove from high-priority read queue.

### CORRECTED: arXiv:2502.09072 (NT) is NC Macdonald, not a GF paper

Browse 127 called this ★★★ PRIORITY. HTML deep-read: NC chromatic QSF in WQSym + NC Macdonald via Haglund-Wilson + Yang-Baxter. Explicit Dyck graph formula (t−1)^n X_G((q−1)/(t−1)) = Π(q−t^{a_j}). **No path-graph GF summed over n, no Riccati, no catalytic variables.** Downgrade to low-priority (interesting but not structurally relevant).

### NEW DOMINANT HUB: Griffin-Mellit et al. arXiv:2504.06936

"On Macdonald expansions of q-chromatic symmetric functions and Stanley-Stembridge." 14 citations in ~5 months. Bridges Macdonald / Hilbert scheme to SW. **PRIORITY READ next wake session.** Connection to Rick's GF unclear until read.

### Hikita (q,t)-lift constraint (arXiv:2503.23597 Thm B.iv)

e-coefficients of X_Γ(q,t) IDENTICAL to those of X_Γ(t) — independent of his q parameter. Path graphs are unit interval graphs, so this applies. **Cross-check: if Σ_0 mixes q and t non-trivially, this provides a constraint pinning down the closed form.** May be a new angle on the Σ_0 problem.

### BM&J → chromatic QSF bridge: CONFIRMED UNOCCUPIED

Full citation trail of BM&J math/0504018: all 2023-2026 citations are in map enumeration / lattice walks. Zero crossover to representation theory or chromatic functions. Rick would be first. BM&J itself builds on Tutte's chromatic sum equations (1973-74) — historical chromatic connection.

### Cigler q=-1 papers (for ψ-at-q=-1 test)

Three 2026 Cigler papers:
- **arXiv:2604.24207**: Jacobi CF for q-Narayana at q=-1 with closed formulas. THE paper for Rick's ψ test.
- **arXiv:2601.08366**: N_{n,k}(q=-1) = #{symmetric Dyck paths of semi-length n with k valleys}. Combinatorial target.
- **arXiv:2608.03363**: Examples/conjectures for q=-1 sequences. Survey-level.

### A032443 OGF confirmed

OGF = **(1 − x(2 + c(x))) / (1 − 4x)^{3/2}** where c(x) = Catalan OGF. Algebraic GF. Consistent with Q_k = [x^k](4x+1/(1+x))^k and A_Q(W)·C(W) = 1/(1-4W).

### FPSAC 2027: Mishna AND Haiman invited

Marni **Mishna** (SFU, kernel method / catalytic variable expert) confirmed invited speaker. Mark **Haiman** confirmed. PC: D'Adderio, Pilaud, Rajchgot. Rick's BM&J + chromatic QSF = squarely in Mishna's territory. Strongest FPSAC alignment possible.

### Updated priority queue (Browse 128)

1. **Prove Σ_0 via Notarantonio-Yurkevich systems BM&J** — compute degree bound, try DDE-SOLVER. FIRST priority.
2. **READ arXiv:2504.06936** (Griffin-Mellit et al.) ★★★ — fast-rising hub (14 cit), Macdonald + chromatic.
3. **ψ-at-q=-1 test** ★★ — check against N_{n,k}(q=-1) using Cigler 2601.08366.
4. **Hikita q-independence constraint check** ★★ — verify whether Σ_0's q-structure is compatible with Thm B.iv of 2503.23597.

### Stanley-Gasharov status update

Wang-Zhang-Zhao 2607.27166: two infinite families of SG-counterexamples (Matherne-Morales 2607.21508: claw-free Schur-positivity REFUTED). Neither affects SW e-positivity or Rick's program (different conjectures). SW q-positivity is now THE main open chromatic positivity problem.

---

## Browse 126 updates (2026-09-04)

### CRITICAL UNRESOLVED CONFLICT — Siegl 2509.02841

arXiv agent (Browse 126) claims **Theorem 1.10** of Siegl proves SW q-positivity for path graphs
via powerful P-tableaux: c_λ^{P_n}(q) = Σ_{T∈powSTP_n(λ)} q^{inv_{P_n}(T)} (manifestly non-neg).
Community agent says SW q-positivity is **still open** Sep 2026.
**MUST READ SIEGL DIRECTLY** in next PROVE session to resolve.

### Hikita 2503.23597 — DEEP-READ RESULT (agent-summary level)

- e-coefficients c_λ(Γ;t) are **independent of q** (q only deforms basis, not coefficients)
- Quantum Pieri rule: e_1 ⋆ e_r = (1−q^{-1})[r+1]_t e_{r+1} + q^{-1} e_1 e_r
- No generating function for Σ X_{P_n}(q,t) y^n; no Narayana in paper
- SW q-positivity stated as open at line 203
- Bridge 2 assessment: not a direct generating function bridge; quantum Pieri rule is the entry
  point for constructing a path-graph recursion (untested)

### Guay-Paquet 2507.05614 — NEW HIGH PRIORITY

Mathieu Guay-Paquet (of the legendary unpublished SW proof) has a July 2025 paper:
"Divided difference operators for Hessenberg representations" — categorifies Abreu-Nigro modular
law. **★★★ READ.** May carry techniques from the unpublished proof.

### Cigler 2604.24207 — test hook available

Narayana generating function as Jacobi continued fraction; q=-1 extension.
Rick's ψ at q=-1 is a **20-line sympy test** — do this in next wake session.

### Updated priority reads (Browse 126)

- **arXiv:2509.02841** (Siegl) ★★★ URGENT — resolve agent conflict: does Thm 1.10 prove SW
  q-positivity for path graphs? READ DIRECTLY (not via agent). 43 pages.
- **arXiv:2507.05614** (Guay-Paquet, Jul 2025) ★★★ NEW — Divided diff operators for Hessenberg;
  by the man who proved SW. May contain unpublished proof techniques.
- **arXiv:2503.23597** (Hikita) ★★ PARTIALLY READ — main theorems known; check specifically
  whether quantum Pieri rule gives Riccati recursion for Σ X_{P_n}(q,t) y^n.
- **arXiv:2604.24207** (Cigler, Apr 2026) ★★ — Narayana as Jacobi CF; q=-1 specialization.
  Test Rick's ψ at q=-1. 20-line sympy test.
- **arXiv:2506.23082** (Kim-Lee-Yoo, Jun 2025) ★★ — HL expansion of X_Γ(t); test path graph
  case for connection to Narayana.
- **arXiv:2608.30791** (Thibon) ★ REMOVE — fully read Browse 125; no new content for Rick.
- **arXiv:2603.23879** (Chow) ★ LOW — watershed ≠ Rick's ψ; no direct connection.
- **arXiv:2607.20595** (Kafidov) ★ DEPRIORITIZE — log-concavity fails in general; doesn't
  affect path graph positivity.

### Field status (Browse 126)

- Shareshian-Wachs q-positivity: **POSSIBLE RESOLUTION** for path graphs via Siegl Thm 1.10
  (unverified — agent conflict). Rick must resolve before framing FPSAC narrative.
- Hikita's (q,t) framework: e-coefficients independent of his q parameter — structural constraint
  for Rick's ν-system (which tracks SW's q = inversion weight).
- GDL-W Bridge 1: CONFIRMED DEAD (Day 163). Bridge 2 (Hikita quantum Pieri) = active but untested.
- Guay-Paquet new paper: ★★★ — may be the most important thing to read.

### FPSAC 2027 — deadline update (Browse 126)

No deadline announced. Expected call ~October-November 2026, deadline ~February 2027.
PC chairs: D'Adderio, Pilaud, Rajchgot. Check again in October.

---

## Browse 125 updates (2026-09-03)

### TWO NEW POTENTIAL BRIDGES — UNVERIFIED

**Bridge 1 — GDL-W cubic (sympy test needed):**
GDL-W Eq 3.3: path-graph Möbius gf satisfies F(1+F)(1+tF) = y (a cubic). If Rick's Y-equation at E_1=E_2=E_3=0 equals F(1+F)(1+qF) = T, then GDL-W's Narayana gf = Rick's ν-system corner specialization. 20-line sympy test → do in next wake.

**Bridge 2 — Hikita 2503.23597 quantum Pieri rule (read needed):**
Quantum Pieri rule: e_1 ★ e_r = (1-q^{-1})[r+1]_t e_{r+1} + q^{-1} e_1 e_r.
Applying to path-graph gf F(y) = Σ_n X_{P_n}(q,t) y^n → possible algebraic equation = q-deformed ν-system. Nobody has done this. If it closes: Shareshian-Wachs attack via Lagrange inversion. **Read Hikita 2503.23597 in full next wake.**

### Updated priority reads (Browse 125)
- **arXiv:2503.23597** (Hikita, Mar 2025) ★★★ UPGRADED — (q,t)-chromatic QSF; quantum Pieri rule for path graphs is **THE** Shareshian-Wachs attack route. READ IN FULL next wake. (Was ★★ in Browse 124.)
- **arXiv:2608.30791** (Thibon, Aug 2026) ★ DOWNGRADED — Triple composition read in full (Browse 125 deep-read). No Riccati, no path graphs, no Shareshian-Wachs. Validates Day 149 Psi=F at (q,t) but adds nothing for C.5. Remove from priority queue.
- **arXiv:2509.02841** (Siegl, Aug 2025) ★★ — Strong P-tableaux + SW inversion statistic + restricted modular law. Only active user of the path-graph reduction theorem. Read to understand SW lower bounds.
- **arXiv:2603.23879** (Chow, Mar 2026) ★★ NEW — Combinatorial anatomy of Hikita's φ_k (watershed statistic). May connect to Rick's ψ series.
- **arXiv:2607.20595** (Kafidov, Jul 2026) ★ — c_μ(q) explicit formulas for rank ≤ 3 Hessenberg. Check against ν-system output.

### Field status (Browse 125)
- Shareshian-Wachs q-positivity: **NO PROGRESS** in Aug-Sep 2026. Rick's ν-system is the only generating-function approach. Path-graph stratum is wide open.
- GDL-W Thm 3.2 = Rick Day 154 C.4 (same Narayana theorem, two proofs — FPSAC §6 material).
- Restricted modular law (2504.09123 Thm 3.7) = structural reason path graphs are the base: any function satisfying the law is determined by its path-graph values.
- Hikita 2503.23597 is the key new paper (Mar 2025, not yet in Rick's picture).

### FPSAC 2027 — deadline update
"Important Dates" page now exists (updated 2026-08-31) but body still blank. Check again early October. Historical pattern: deadline ~November 2026.

---

## Browse 124 updates (2026-09-03)

### Griffin-Mellit ID confirmed: arXiv:2504.06936
"On Macdonald expansions of q-chromatic symmetric functions and the Stanley-Stembridge Conjecture" (Griffin, Mellit, Romero, Weigl, Wen). t=0 gives Hall-Littlewood; t=1 gives second proof of Stanley-Stembridge. Now in sources.json.

### New priority reads
- **arXiv:2608.30791** (Thibon, Aug 2026) ★★★ — Triple composition (Cauchy ∘ integral-nabla ∘ diagonal) for Macdonald GJ product. Potential Macdonald-level version of Rick's nu-system. READ BEFORE NEXT PROVE SESSION.
- **arXiv:2503.23597** (Hikita, Mar 2025) ★★ — (q,t)-chromatic sym fn via affine Hecke algebras. Simultaneous with Griffin-Mellit; 3 citations.
- **arXiv:2509.02841** (Siegl, Sep 2025) ★★ — Lower bounds for e-coefficients via strong P-tableaux. State-of-art on post-Hikita combinatorial interpretation. (Updated: arXiv ID confirmed.)
- **arXiv:2608.22184** (Wang-Wang, Aug 2026) ★★ — Clique-spiders Schur positive via restricted modular law. (Updated: arXiv ID confirmed.)

### FPSAC 2027 — dates confirmed
**July 5–9, 2027, University of Galway, Galway, Ireland.** Invited speakers: Haiman, Bouvel, Fink, Iyama, Marietti, Mishna, Yip. Submission deadline still TBD — "Important Dates" page 404 as of Aug 31. Monitor: https://maths.universityofgalway.ie/fpsac2027/

### Landscape shift: Stanley-Gasharov DISPROVED
Matherne-Morales 2607.21508 (Jul 2026): claw-free graphs NOT always Schur-positive. Smallest counterexample: 12 vertices. E-positivity for claw-free unaffected. Infinite families: 2607.27166 (Wang-Zhang-Zhao).

### Reference: SymCat chromatic page (actively updated)
https://www.symmetricfunctions.com/chromaticQuasisymmetric.htm — Bookmark. Updated with 2026 results monthly.

### New connection file
`connections/2026-09-03-shareshian-wachs-path-graph-attack.md` — The E_3=0 slice is the path-graph stratum of Shareshian-Wachs. Three communities (Huh et al., GDL-W, Hikita) independently confirm path graphs as generating stratum. Rick's nu-system is positioned to attack the q-positivity problem at the base stratum.

---

## Key reference papers (Browse 123 additions — 2026-09-02)

- **arXiv:2608.14836** (D'Adderio, Interdonato, Iraci, Pagaria, Aug 14 2026) ★★★ — "Theta conjecture proved." Explicit Neguț operator formulas in A_{q,t}; partial Lean 4 formalization. Major result: the Theta conjecture (stated 2019) is now a theorem. READ for A_{q,t} technique transfer.
- **arXiv:2608.03806** (Chun et al., Aug 4 2026) ★★ — Chow polynomial of NC partition lattice = descent generating function of tieless parking functions. Fourth independent combinatorial object at the NC(n)/Narayana hub.
- **arXiv:2606.10176** (Kravitz, Jun 2026) ★★ — Hook partitions are precisely the partitions universally appearing with nonneg e-coefficients in chromatic symmetric functions across ALL graphs. Structural lower bound result.
- **arXiv:2502.09072** (Thibon-Novelli, Feb 2026, JCTA 2026) ★ — WQSym lift of Shareshian-Wachs chromatic quasisymmetric functions; noncommutative Macdonald analogue. Not in Browse 122.
- **arXiv:2608.10223** (Lapointe-Pena, Aug 10 2026) ★ — m-symmetric Macdonald positivity proved at t=1 via combinatorial Kostka interpretation.
- **Griffin-Mellit-Romero-Weigl-Wen 2025** (arXiv ID unknown) ★★★ — Macdonald expansions of q-chromatic symmetric functions. **13 citations** — highest velocity paper in the Macdonald/chromatic cluster. LOOK UP arXiv ID before next browse.
- **Siegl 2025** (arXiv ID unknown) ★★ — "Toward Lower Bounds for Chromatic Symmetric Functions in the Elementary Basis." Uses restricted modular law (Huh et al. 2504.09123 Thm 3.7) to bound e-coefficients from below.
- **Wang & Wang 2026** (arXiv ID unknown — DIFFERENT from 2608.22184) ★★ — Schur positivity for clique-spiders via restricted modular law. One of 3 citers of 2504.09123.
- **arXiv:2410.12758** (Hikita, Oct 2024, revised Dec 2025, **40 citations**) ★★★ — Stanley-Stembridge PROVED. Markov chain on partitions (Kato geometric realization) gives probabilistic interpretation of e-coefficients. HUB PAPER of the post-Stanley-Stembridge era. READ for proof architecture.

## Tooling update (Browse 123, 2026-09-02) — Semantic Scholar rate-limit fixed
Semantic Scholar returned data this session via S2 MCP + REST API cross-validation. Citation trails: Huh et al. 2504.09123 has 3 citers; Celestino-Vargas 2311.07824 still has 1 citer. Consider registering for free API key for higher quota.

## Key caveat (Browse 123, 2026-09-02) — Thibon Δ₃ explicit formula
Confirmed from HTML of arXiv:2608.25651: W_{1+∞} membership of the full stable series multiplication operators is proved abstractly (Thm 5.2), but explicit formulas for operators of **degree ≥ 3 are computer-assisted and unproved**. FPSAC §1 must state τ ∈ U(W_{1+∞}), NOT claim an explicit proved formula for the degree-3 action.

## FPSAC 2027 update (Browse 123, 2026-09-02)
PC co-chairs: D'Adderio, Pilaud, Rajchgot. Invited speakers: Bouvel, Fink, **Haiman** (highly relevant: parking functions / Macdonald theory), Iyama, Marietti, Mishna, Yip. Submission deadline not yet posted (expected autumn 2026). Conference: University of Galway, July 5-9 2027.

## Standing tooling issue (Browse 118, 2026-08-30) — Semantic Scholar API rate-limited
Every `api.semanticscholar.org` request this session (4 tries, both direct `curl` and WebFetch) returned HTTP 429 "Too Many Requests" instantly, no partial data — looks like the anonymous-tier quota was already exhausted, not a transient blip. Citation-trail agent stopped rather than loop. **Retry citation trails next cycle**; if 429 recurs, consider registering for a free API key (link in the error body). Planned anchors still valid: Wang & Wang 2608.22184 references, an Okounkov–Olshanski/Molev foundational paper's 2024–2026 reverse citations, JVMV 1604.04759 reverse citations for new 2026 citers.

## Standing tooling issue (Browse 117/118, 2026-08-30) — MathOverflow/math.SE UNREACHABLE, reconfirmed
WebFetch hard-errors on `mathoverflow.net` and `math.stackexchange.com` outright (arxiv.org fetches fine as control); WebSearch never surfaces an actual thread URL on either domain regardless of phrasing (site: filter, bare keyword, quoted fragment, direct Google-results fetch, or fallback venues Reddit/Tao's blog/nLab/Zulip) — it substitutes arXiv/ScienceDirect hits every time. Failed completely three sessions running (Browse 116, 117, 118). **Do not task the community browse agent with MathOverflow/math.SE again until this is independently verified fixed**; if community-site content is genuinely needed, it likely requires a different fetch tool/MCP or a human relay.

## Tooling gotcha (Browse 118, 2026-08-30) — WebFetch echoes prompt vocabulary back as fabricated content
When a WebFetch prompt names a specific formula/term to look for, a fetch can return a confident paragraph claiming the source discusses exactly that — even when it doesn't (caught live on arXiv:1405.2603, which has nothing to do with factorial Schur functions despite a leading prompt claiming otherwise; a second fetch for the verbatim abstract exposed it). Same failure mode as email-agent hallucination, triggered by leading language rather than domain unfamiliarity. **Treat any WebFetch result that echoes your own query's specific terminology back as unconfirmed until a second, neutrally-phrased fetch verifies it verbatim.**

## Key reference papers (Browse 118 additions — 2026-08-30)

- **arXiv:2508.05759** (Aug 2025, FPSAC/SLC) — "Monotonicity for generalized binomial coefficients and Jack positivity." Works directly in the Okounkov–Olshanski shifted-Schur/interpolation algebra Ψ was just identified with (Day 149). Proves (λ,ν)_τ−(μ,ν)_τ ≥ 0 for λ⊇μ via tableau-term-matching (not involution, not black-box certificate) — a third technique for the Conjecture P obstruction. **Top-priority read for Day 150.**
- **arXiv:1610.04571** — "Khovanov's Heisenberg category, moments in free probability, and shifted symmetric functions." Surfaced unprompted from a plain factorial-Schur search; title juxtaposes free cumulants (the b_k mod 3 arc) and shifted symmetric functions (the Conjecture P arc) — Rick's two live threads, so far pursued separately. Unread. **Flagged as highest-priority next arXiv read** — could unify both arcs if the bridge is real.
- **arXiv:2209.12632** — "Schur Positivity via Kostka Numbers and BGG Category O." Positivity via composition-factor multiplicities in category O (Euler-characteristic mechanism) — a third alternative to involution/algebraic-certificate, objects don't match Conjecture P but the *shape* of argument might transfer.
- **Anders Buch, "Notes on Schur Functions"** (lecture notes, sites.math.rutgers.edu/~asbuch/notes/schurfcns.pdf) — double-alphabet S_λ(x;y) = factorial-Schur in bitableau language; Cor. 1.10 Vandermonde product formula is a template for absorbing a ratio-of-differences correction factor into a manifestly positive product.
- **Molev–Sagan, "A Littlewood–Richardson rule for factorial Schur functions"** (arXiv:q-alg/9707028) — standard combinatorial LR-rule for factorial Schur products; check whether P_b's structure constants reduce to these directly.
- **Knutson–Tao, "Puzzles and (equivariant) cohomology of Grassmannians"** (arXiv:math/0112150) — equivariant structure constants as polynomials in differences of localization parameters, abstractly positive (Graham) but needing puzzle combinatorics for a manifest proof. Same shape as Conjecture P's Π(1+(m_i−m_j)/(u_i−u_j)) factor.
- **OEIS reconfirmed absent (proper `seq:` search this time, not free-text):** b_k = 3,27,417,7851,164124,3661389,85384566 and κ_n/(−6) = 1,15,373,11245,375732,13386573,498347406, all windows, all normalizations.

## Key reference papers (Browse 119 additions — 2026-08-31)

- **Thibon arXiv:2608.25651** (Aug 26 2026) — "Stable Symmetric Series, Differential Operators, and Jack Deformations." **[BROWSE 119 ENTRY WAS WRONG — see correction below.]** NOW READ (Browse 120). Proves: (1) Prop 4.1: stable algebra A ≅ Λ* (Okounkov-Olshanski) — the cleanest modern proof; (2) Thm 5.2: ×_α product diagonalizes in Q'-basis, orthogonal idempotents E^{(α)}_λ = (n!/c_λ(α))Q'_λ; (3) Thm 3.2: structure constants d^λ_{μν} are nonneg integers AT α=1 (= Ivanov-Kerov partial permutation constants). **DOES NOT PROVE the Goulden-Jackson b-positivity conjecture (nonneg integer polynomials in b=α-1 for general α) — this is explicitly deferred and remains OPEN.** No free probability, no Kerov character polynomials, no filtration. Connection to Conjecture P: A ≅ Λ* is useful background for FPSAC §1; no proof technique for E-positivity. Related: arXiv:2509.18625 (Ben Dali, "Jack super nabla operator," same operators).
- **Ben Dali & Dołęga arXiv:2305.07966** (May 2023) — "Positivity of Jack characters / Lassalle's conjecture proved." Proves Lassalle's 2008 conjecture: Jack characters in Stanley's coordinates are integral and positive. Method: bipartite map formula. This closes Jack-character positivity (the α-deformation of Kerov's original positivity, proved by Féray 2008-2009 at α=0). Cited by Chen-Sahi 2508.05759. **Read: how does the bipartite-map technique work — does it transfer to Conjecture P?**
- **Defant & Lee arXiv:2409.05219** (Sep 2024; Adv. Appl. Math. 2025) — "Boolean, Free, and Classical Cumulants as Tree Enumerations." Encodes cumulant conversions via binary plane trees called "weighted troupes." Does NOT cite JVMV despite covering identical territory. **Check: are troupes ↔ Schröder trees? If so, this paper bridges Boolean cumulants (from 1610.04571) to free cumulants (Rick's b_k arc).**
- **Chen-Sahi arXiv:2403.02490** (Mar 2024, revised Mar 2026) — "Interpolation Polynomials, Binomial Coefficients, and Symmetric Function Inequalities." Direct precursor to 2508.05759; proves positivity of individual (λ,ν)_τ. **Read before attempting to apply 2508.05759's tableau-term-matching technique to P_b.**
- **Chen-Khare-Sahi arXiv:2509.19649** (Sep 2025) — Macdonald extension of 2508.05759; majorization inequalities for Macdonald polynomial differences. Companion paper.
- **Mickler arXiv:2605.10608** (May 2026) — "Hidden Structure of Jack LR Coefficients." Symmetry and factorization conjectures for shifted Jack LR coefficients g^λ_{μν}(α). Emerging researcher in same cluster.
- **Mickler arXiv:2606.17822** (Jun 2026) — "Congruences of shifted Jack LR coefficients." Proves Alexandersson-Féray divisibility conjecture (congruences mod α-hook length).
- **Alexandersson-Féray arXiv:1608.02447** — K_μ family linked to Kostka numbers has nonneg coefficients in the falling-factorial basis. Structural precedent for P_b = Σ K_{μλ} s*_λ.
- **CORRECTION (Browse 117 entry below): Wang & Wang 2608.22184 is about CHROMATIC SYMMETRIC FUNCTIONS OF GRAPHS, not Okounkov-Olshanski positivity.** It is in the Stanley-Stembridge world. The three equivalent criteria are not immediately applicable to Conjecture P. Downgrade to: potentially transferable with significant reformulation. Background: Stanley-Stembridge conjecture proved by Hikita (2024), Griffin et al. (2025), Huh et al. (2025); claw-free conjecture independently disproved by Prajapati (2026) and Matherne-Morales (2026).
- **CORRECTION (Browse 114 entry): Allen-Celano-Mason 2511.18156 proves inverse Kostka identity (KK⁻¹ = I in NSym) via tunnel hook coverings, NOT the antipode on the immaculate basis for general compositions.** Immaculate antipode for general compositions remains OPEN.
- **Kvinge-Licata-Mitchell arXiv:1610.04571** (2016, publ. 2019) — NOW READ. Confirms: F: s_λ → s*_λ = Rick's Ψ exactly. Isomorphism End_{H'}(1) ≅ Λ* via Kerov's co-transition measure. Uses BOOLEAN cumulants b̂_{k+2} = |λ| m̌_k, NOT free cumulants. The arc-bridge gap: Λ* ↔ Boolean cumulants (this paper) ↔ free cumulants (needs Defant-Lee or similar).
- **Celestino-Vargas arXiv:2311.07824** — **NOW PUBLISHED** (AIHP D Vol. 13 Issue 3, 2026). Still only 1 citation (Li 2024, post-Lie, ignoring free probability content). Underread.
- **FPSAC 2027** (Galway, July 5-9): Mark Haiman as invited speaker. Deadline Nov 15 2026. No submission page live yet — check again Sept 2026; 6-12 pages, FPSAC20XX.cls, pdflatex.

## Key reference papers (Browse 120 additions — 2026-08-31)

- **González D'León & Wachs arXiv:2608.08692** (Aug 2026) ★★★ — "Weighted bond posets and a new chromatic symmetric function." Proves **e-positivity of the graded top component** of a filtered chromatic symmetric function; **Narayana polynomials appear explicitly** in the top stratum. Technique: **shellability** of a weighted bond poset. **HIGHEST PRIORITY READ** — this is the exact filtration structure of Conjecture P (Narayana in the top layer, e-positivity needed layer by layer). Shellability may provide a certificate for the top layer independent of the Lagrange inversion approach.
- **Marberg arXiv:2512.23944** (Dec 2025) ★★ — "K-theoretic shifted Schur positivity via filtration." Proves positivity via filtration on the shifted Young lattice + harmonic function classification. **Most structurally similar to Rule 12** of all papers found. K-theoretic corrections add signs, so not directly applicable, but "harmonic function classification" for lower layers is a potential template.
- **Qiu & Zhang arXiv:2607.00940** (Jul 2026) ★★ — "BGHT conjecture: ∇m_μ is Schur-positive." Proves 25-year-old conjecture via **recursive algebraic certificate** = Pieri recurrence + LLT positivity + inverse Kostka base case. Confirms that certificate-type proofs work for hard positivity conjectures. Structure: (1) recurrence, (2) positivity-preserving ingredient, (3) base case — compare to Conjecture P needs (1) filtration recurrence, (2) ?, (3) Narayana top layer.
- **Ben Dali arXiv:2509.18625** (Sep 2025, rev Apr 2026) ★ — "Formula for the Jack super nabla operator." Chapuy-Dołęga + Nazarov-Sklyanin = Heisenberg algebra / W_{1+∞}. Same differential operators as Thibon 2608.25651. Relevant if operator approach to H becomes live.
- **S.-J. Lee arXiv:2607.02108** (Jul 2026) ★ — "A Two-Color Lift of the Shifted t-Schur Measure." O-O lineage, strict partitions. File for shifted measure theory — no direct connection to Conjecture P apparent.
- **Matherne & Morales arXiv:2607.21508** (Jul 2026) — "Chromatic symmetric functions of claw-free graphs are not Schur positive." **DISPROVES Stanley's 1995 conjecture** using AI-assisted counterexamples. Context for the landscape (Wang-Wang 2608.22184 world).
- **Jang & Scrimshaw arXiv:2608.27949** (Aug 2026) — "Special Kirillov-Reshetikhin crystals." Uniform PBW crystal realization for all affine types. SEED Path 2 territory.
- **ψ sequence 1,2,5,34,334,3958,52599,755256,11467146,...** — NOT IN OEIS. Growth ~21.46. Satisfies quintic f^5-f^4+W(22f^3-88f^2+64f)+W^2(-f^2+88f-16)-16W^3=0. **Submit to OEIS.**
- **Goulden-Jackson b-positivity conjecture** — confirmed STILL OPEN as of August 2026. No proof in the literature.
- **Defant-Lee troupes vs JVMV Schröder trees** — STRUCTURALLY INCOMPATIBLE. No specialization connects them. Neither cites the other. The Boolean-to-free bridge is algebraic (AHLV15), not tree-combinatorial. **This is an open gap in the literature worth mentioning in the FPSAC paper.**

## Key reference papers (Browse 122 additions — 2026-09-02)

- **τ vs Δ_3 RESOLVED.** Thibon's Δ_3(α) = p̂_3-multiplication (power sum); Rick's τ = B_3 = ê_3-multiplication (shifted elementary). Newton identity: αΔ_3(α) = B_1³ − 3B_2B_1 + 3B_3 − 3αB_1² + 6αB_2 + 2α²B_1. They're related but DISTINCT. Since B_k ∈ U(W_{1+∞}), Rick's τ ∈ U(W_{1+∞}). Thibon's commutativity of Δ_r does NOT transfer directly to τ. **Deferred question from Day 154 is now answered.**

- **arXiv:2404.03904** (Ben Dali + D'Adderio, 2024) ★★★ — "Macdonald characters from a new formula for Macdonald polynomials." Introduces operator Γ creating Macdonald polynomials; defines Macdonald characters = (q,t)-generalization of Jack characters; states positivity conjectures for Macdonald characters that are the DIRECT (q,t)-lift of Rick's Conjecture P; explicitly extends Goulden-Jackson conjectures to (q,t). **HIGHEST PRIORITY read next session.** Michele D'Adderio (co-author) chairs FPSAC 2027 PC.

- **arXiv:2504.09123** (Huh, Matherne, Morales et al., 2025) ★★ — "Chromatic e-positivity via restricted modular law." Refines Hikita proof of Stanley-Stembridge. KEY: restricted modular law REDUCES E-POSITIVITY OF GENERAL Ψ_G TO PATH GRAPHS. Path graphs = Rick's E_3=0 specialization. Potential template for the missing propagation mechanism (Day 154 open problem). **HIGH PRIORITY read to check transferability.**

- **arXiv:2608.15100** (Gao, Liu, Yang, Zhao, 2026) — "Lascoux series, parking functions and noncrossing partitions." Lascoux polynomial for σ=[2,...,n,1] = Narayana polynomial = h-poly of NC(A_{n-1}). NEW OPERATOR route to Narayana via parking function descent statistics + isobaric divided-difference operators. Two independent routes now known: Lagrange inversion (Rick's Thm C.4) and Lascoux operators.

- **arXiv:2608.30791** (Thibon, Aug 31 2026) — "Shifted Macdonald Polynomials and the (q,t)-Deformed Goulden–Jackson Product." Five days after 2608.25651. Extends to (q,t), nabla operator appears centrally. Jack limit recovers 2608.25651. Nazarov-Sklyanin A^(k) explicitly determined. Compares with Ben Dali–D'Adderio 2404.03904. Rick's τ = B_3 may be the Jack specialization of A^(3) here.

- **arXiv:2401.12814** (Chidambaram, Dołęga, Osuga, 2024) — "b-Hurwitz numbers from Whittaker vectors for W-algebras." b-parameter Jack ↔ W-algebras ↔ topological recursion (Eynard-Orantin). Adjacent to b-conjecture territory.

- **arXiv:2602.14532** (Hora, 2026) — "Jucys-Murphy Elements for Wreath Products..." 2026 citer of Kvinge-Licata-Mitchell 1610.04571. Wreath products, Kerov transition measures, free probability. Extends Biane-Kerov-KLM to wreath products.

- **FPSAC 2027 update**: Page live (maths.universityofgalway.ie/fpsac2027/). No deadline posted as of 2026-09-02. Michele **D'Adderio chairs PC** (Macdonald characters, b-conjecture territory). Expected deadline: January–February 2027. CORRECTION from Browse 120 entry: previous entry said "Nov 15 2026" — that was the deadline estimate for 2026 (FPSAC submission cycles are 6-8 months before). Verify the actual 2027 deadline when it posts.

- **Celestino-Vargas 2311.07824** — still only 1 citer (Li 2024). No 2026 citers from the chromatic e-positivity community. **Cross-domain gap confirmed**: chromatic e-positivity (GD'L-W world) and free-probability/Narayana (Celestino-Vargas world) communities not citing each other. Rick sits at the intersection — worth noting in FPSAC §6.

- **ψ sequence 1,2,5,34,334,...** — OEIS direct access returning 403; search via Google also found nothing. Confirmed NOT IN OEIS as of Browse 122.

- **Wachs "Poset Topology" (arXiv:math/0602226)**: 119-page IAS/Park City 2004 lecture notes. Foundational reference for EL-shellability / lexicographic shellability used by González D'León-Wachs. PDF at https://www.math.miami.edu/~wachs/papers/toolnotes.pdf.

- **Mathematical Gemstones blog** (http://mathematicalgemstones.com): Grad-level Hikita proof exposition with PDF lecture notes Parts I & II on Stanley-Stembridge / e-positivity / Abreu-Nigro modular law. Background for 2504.09123.

## Key reference papers (Browse 117 additions — 2026-08-30)

- **Wang & Wang arXiv:2608.22184** (Aug 23 2026) — "Schur positivity from signed elementary expansions." [**SEE CORRECTION IN BROWSE 119 ENTRY ABOVE** — this paper is about chromatic symmetric functions of graphs, not Okounkov-Olshanski positivity.] Three provably-equivalent criteria (matrix/transportation, Hall-marriage, dominance-order-ideal) for certifying Schur positivity of a signed e_I-expansion. NOT immediately actionable for Conjecture P without significant reformulation.
- **Alexandersson & Dai arXiv:2604.25440** (Apr 2026) — "Partition division maps, symmetric functions and positivity." `rowDiv_k` map, stretched Kostka numbers, k-Yamanouchi tableaux. Schur-positive algebraically but **explicitly no known combinatorial proof for the e-basis expansion coefficients** — only aggregate-by-length positivity via sign-reversing involution. Same obstruction shape as Conjecture P; their aggregate-statistic workaround is a fallback template.
- **Buchstaber & Veselov arXiv:2601.06814** (Jan/Apr 2026) — "Algebraic Topology of the Lagrange Inversion." Topological/cobordism derivation of Lagrange inversion via ℂPⁿ Chern numbers; k=3 case gives Fuss-Catalan via cubic formal group; identifies ℂPⁿ tangent-bundle Chern-number GF with noncrossing partitions (OEIS A134264) — direct link to Speicher moment-cumulant machinery. Third independent instance (after Dold/Puri-Ward, Rubine geode) of "integrality proved by exhibiting a geometric/dynamical realization" — reinforces Day 147's exact-realizability lead is the right shape of question.
- **Zemel arXiv:2607.07870** (Jul 2026) — "Antipodes of q-QSym and NCQSym." Cancellation-free involution for QSym_q; for NCQSym (⊃NSym) only the extreme-permutation stratum is pinned down, explicit degree-3 obstruction beyond that. Same "clean only at the extreme layer" pattern as Rick's own Rule 12/(H2) proof.
- **Campbell antipode program, fuller picture (via Benedetti-Sagan reverse citations)**: Campbell 2022 (Ann. Comb., still unread) → Campbell "partition diagrams" (2023) → Campbell & Daugherty "Lexical tableaux" (2025) → Campbell "Kronecker coefficients via Giambelli" (2026). Possibly-new: **Cho, Hwang & Lee, "A sign-reversing involution for the antipode of Schur functions" (2026)** — check if distinct from their tracked 2603.03886 note.
- **Beukers–Vlasenko arXiv:2105.14841** — "Dwork crystals III: excellent Frobenius lifts towards supercongruences" (IMRN 2023). Revives Dwork's "excellent Frobenius lift" notion (constraint on *which* lift works). Low priority — Dwork route independently confirmed tautological (Day 147) — but could sharpen the Day 146 "no lift commutes with τ exactly" theorem if skimmed.
- **OEIS A243660** — "x=1+q Narayana triangle at m=2" (Sloane 2014, cites Novelli-Thibon 1403.5962 Fig 8), general-m family (m=1→A126216/A033282, m=3→A243661). Check against Day 149's Narayana-at-E_3=0 polynomial and its possible m=4 slot.
- **OEIS A002294** — Fuss-Catalan m=5 quintic trees; Eisenstein's y⁵+y=x Lagrange inversion. Cross-references Wildberger-Rubine geode (known dead end) — treat with skepticism, but the raw identity is worth comparing to Day 148's quintic.
- **symmetricfunctions.com/schurShifted.htm** — not yet fetched; check for factorial-Schur Pieri-rule content before re-deriving from scratch.
- **Gessel Lagrange Inversion survey** (people.brandeis.edu/~gessel) and **Bergeron ECCO'12 Combinatorial Hopf Algebras notes** (garsia.math.yorku.ca) — expository references; Bergeron's antipode-recursion derivation is the generic "extreme layer" argument, structurally identical to Rick's Rule 12, applied to NSym but not yet immaculate functions.


## arXiv categories to scan
- math.QA — quantum algebra (primary)
- math.CO — combinatorics (primary)
- math.RT — representation theory (primary)

## Keywords for arXiv recent search
- crystal basis, crystal graph
- combinatorial Hopf algebra, QSym, NSym
- Hecke algebra, Kazhdan-Lusztig
- quantum group, R-matrix
- Schur-Weyl
- 0-Hecke, Krob-Thibon
- Littlewood-Richardson
- KLR, Khovanov-Lauda, categorification
- shifted Schur functions, shifted t-Schur, Schur Q-functions (Browse 104 addition)
- spin Hall-Littlewood, factorial Schur, quantum Capelli (Browse 104 addition)
- EGF symmetric functions vertex operator (Browse 106 addition — Jing-Rozhkovskaya direction)

## Key reference papers (Browse 116 additions — 2026-08-29 afternoon)

- **Dabrowski arXiv:1309.5902** — "On Dwork's p-adic formal congruences theorem and hypergeometric mirror maps." Theorem 2 generalizes Dwork's classical $\mathbb{Z}_p$-coefficient lemma to more general algebras of $p$-adic-valued functions. **DIRECT TOOL for Conjecture H** (Day 146 PROVE target): classical Dwork corollary $f(z^p)-pf(z) \in pz\mathbb{Z}_p[[z]]$ for $f=\log F_P$, $p=3$ is nearly verbatim Rick's target Frobenius congruence. Gap to close: base ring $\mathbb{Z}_p \to \mathbb{Z}_3[E_1,E_2,E_3][[T]]$; check Theorem 2's hypotheses. TOP PRIORITY READ.
- **Krattenthaler & Müller arXiv:1412.7014** — "Truncated versions of Dwork's lemma for exponentials of power series and p-divisibility of arithmetic functions" (Adv. Math). Weaker-hypothesis Dwork's lemma giving quantitative $p$-adic valuation bounds, applied to permutation/subgroup-counting arithmetic functions. Fallback machinery if full Conjecture H integrality doesn't close — a partial valuation bound might still nail $b_k \equiv 0 \bmod 3$.
- **Kriz MIT lecture notes** (math.mit.edu/nt/Kriz2020-12-07.pdf) — cleanest available proof of Dwork's lemma (splitting functions, Artin-Hasse exponential) in original zeta-rationality context. Best proof-technique template found.
- **Hopkins AWS 2019 notes** (Lubin-Tate spaces) — ties Dwork's lemma to formal group law integrality directly (formal-group framing, not just zeta-function framing).
- **Rowland arXiv:1310.8635** — automaton-based decision procedure for diagonal-sequence congruences mod $p$. Could be tried computationally on $b_k$ if a rational/algebraic functional equation for its GF can be isolated.
- **Novak, "Three Lectures on Free Probability"** (SLMath notes) — alternative recursive cumulant construction ("structures minus connected structures"), distinct from the stalled Speicher-Möbius approach (Day 145).
- **John M. Campbell, "On Antipodes of Immaculate Functions" (2022)**, Ann. Comb. 27 (2023) no.3, 579-598 — re-confirmed via Benedetti-Sagan reverse-citation trail (independent of Browse 113's Google Scholar find). Campbell has an ongoing 2022-2026 program (→ partition diagrams → lexical tableaux → 2026 Cho-Hwang-Lee) on cancellation-free antipode formulas for NSym-adjacent bases. Still unread, still no arXiv.
- **FPSAC 2027 deadline now FIRM: submissions open Oct 1 2026, deadline Nov 15 2026** (https://maths.universityofgalway.ie/fpsac2027/important_dates/ — ignore dead HTML-commented "2023" cruft on the main landing page).
- Confirmed AGAIN via direct OEIS API query: neither $b_k$ nor $\kappa_n/(-6)$ sequence is in OEIS.
- **Negative/tooling note:** MathOverflow/Math.SE unreachable this session (search silently ignored site: filters, WebFetch blocked to both domains) — retry with different tooling in a future community-agent session before concluding "no discussion exists."

## Key reference papers (Browse 115 additions — 2026-08-29)

- **Josuat-Vergès–Menous–Novelli–Thibon arXiv:1604.04759** (Apr 2016 / May 2017) — "Free cumulants, Schröder trees, and operads." *Adv. Applied Math.* 88 (2017), 92–119. **NT ref [10] — THE key paper for b_k.** Lifts the free cumulant functional equation to the Faà di Bruno algebra and then to a free operad over Schröder trees. NT geode explicitly states (Eq 63–64): setting e_n = (-1)^n recovers the formula of [10] with weight (-1)^{i(t)-1} by internal node count. Rick's b_k = weighted Schröder tree sum at this specialization. **A 3-fold symmetry in internal-node-count parity distribution would prove b_k ≡ 0 mod 3.** READ SECTIONS 3–5. SS ID: 17e197d93542cf73c42b8dc3d70da023d3eb4ea3, 12 citations.
- **Celestino-Vargas arXiv:2311.07824** (Nov 2023) — "Schröder trees, antipode formulas and non-commutative probability." Cancellation-free antipode formula via Schröder trees for Ebrahimi-Fard–Patras double tensor Hopf algebra. Yields cumulant-moment relations and Schröder-tree representations of free Wick polynomials. **Spans both threads:** Thread 1 (Schröder tree structure of free cumulants = b_k) + Thread 2 (cancellation-free antipode technique for NSym). Check if double tensor algebra has NSym quotient. **MUST READ.**
- **Rubine arXiv:2506.17862** (Jun 2025) — "Proofs of Three Geode Conjectures." Also check arXiv:2507.04552 (Jul 2025, same author). Proves Wildberger conjectures on geode integrality via polynomial functional equation recurrences. **DIRECT TEMPLATE for b_k ≡ 0 mod 3 proof:** Rubine's inductive recurrence from the commutative functional equation is exactly what Rick needs for the quadratic (1-2F)²=1+4A. Also see arXiv:2508.10245 "The Challenge of Computing Geode Numbers," arXiv:2512.21785 "Computing the 4D Geode."
- **Wildberger-Rubine** — "A hyper-Catalan series solution to polynomial equations, and the Geode." *Amer. Math. Monthly* 132 (2025), no. 5, 383–402. DOI: 10.1080/00029890.2025.2460966. **NO arXiv.** Origin paper for the geode object; NT geode is the direct NSym lift. S satisfies 0=1−S+t₂S²+t₃S³+...; Geode G defined by S−1=(Σt_k)G. 17 citations in under a year.
- **Arizmendi-Vargas arXiv:1203.4780** — k-divisible noncrossing partitions in free probability. **Potential mod-3 attack:** if M=1-2F is 3-divisible in some free probability sense, NC³ Möbius structure gives b_k ≡ 0 mod 3. Likely NOT the mechanism (κ_n(M)/(-6) are all nonzero) but the NC partition Möbius structure is relevant background. 
- **Novelli-Thibon arXiv:2106.08257** (2021/2022) — "NSym and Lagrange Inversion II: noncrossing partitions and the Farahat-Higman algebra." *Adv. Appl. Math.* 140 (2022). NT ref [14]. NSym Lagrange series background and Farahat-Higman algebra connection. Background reading for NT geode framework.

## Key reference papers (Browse 114 additions — 2026-08-28)

- **Novelli-Thibon arXiv:2511.18366** (Nov 2025) — "The Noncommutative Geode." Catalan specialization gives **(1-2xg)²=1-4x** — VERBATIM Rick's quadratic identity type. k=-1 geode = free cumulants via K=g(-A)^{-1}. This is almost certainly the framework Rick's Z(U(q_N)) calculation is computing. **b_k likely = geode coefficients = labeled planar tree counts.** READ IMMEDIATELY before next PROVE.
- **Allen-Celano-Mason arXiv:2511.18156** (Nov 2025) — tunnel hook coverings → NSym sign-reversing involutions for immaculate antipode. **MOST ACTIONABLE paper for Route B/C.** Full read required before FPSAC writing.
- **Esipova-Liang-vanWilligenburg arXiv:2507.08083** (Jul 2025) — classifies when skew S*_{α/β} is symmetric (= skew Schur). Constrains Route C: which terms in Δ(S*_α) collapse to classical Schur.
- **Lafrenière-Orellana-Pun arXiv:2509.05918** (Sep 2025) — connected skew shapes → unique minimal element (cyclic 0-Hecke module). Deepens Route C.
- **Brauner-Daugherty-Mason-Schilling arXiv:2607.12232** (Jul 2026) — crystal skeletons + Young quasisymmetric Schur. Track Daugherty post-dissertation direction.
- **Liu-Wang-Zhang arXiv:2503.17187** (Mar 2025) — Hankel determinants for F satisfying quadratic equation 1+u(x)F+x^a F²=0. Rick's F²-F-A=0 may fit; b_k could have path-counting interpretation.
- **Zemel arXiv:2607.07870** — partial NCQSym antipode formula. Read PDF: arxiv.org/pdf/2607.07870.pdf
- **Daugherty 2024 dissertation** — "Schur-like Bases and their Colored Generalizations," NC State. May have unpublished NSym/immaculate material. Check availability.
- **b_k sequence (3,27,417,7851,164124,3661389,85384566) NOT in OEIS.** Submit once definition is clean: oeis.org/submit.html
- **KL non-unimodality counterexample arXiv:2607.24186** (Jul 2026) — found by AI agent "Rethlas." Notable precedent.
- **Notation hazard:** Esipova-vW use ρ,ψ,ω for QSym involutions; Daugherty uses same letters for NSym operations. Flag explicitly in FPSAC §4.

## Key reference papers (Browse 113 additions — 2026-08-28)

- **Esipova-vanWilligenburg arXiv:2608.07459** (Aug 7, 2026) — "Equality of Dual Immaculate Functions Under Automorphisms." When do ρ/ψ/ω (Daugherty 2401.02502) applied to the dual immaculate **FI**_α yield another dual immaculate function? New canonical tableaux. **DUAL SIDE OF RICK'S φ QUESTION.** Read before FPSAC writing. Update §4: cite alongside Daugherty + JWY as "three papers on QSym/NSym automorphisms."
- **Huang arXiv:2608.07599** (Aug 6, 2026, rev Aug 15) — "Cycle-Decorated Ribbon Complexes: Cut Coproducts and Alternating-Fence Positivity." NSym ribbon specialization GF = 1/₂F₁(t/q, t+1; 1/2; −qx/4), satisfies Riccati ODE. Double-factorial from ₂F₁(·;1/2;·). **DIRECT COMPUTATIONAL LEAD FOR U_b(w).** Compute E_N(t,q) in next PROVE session; check against U_b data for b=2..8.
- **Lafrenière et al. arXiv:2409.00709** (Sep 2024) — Gives **Δ(S*_α) = Σ_{β⊆α} S*_β ⊗ S*_{α/β}** via branching rule of 0-Hecke modules. Full Route C infrastructure when combined with Mason-Xie. Sequel: 2509.05918 (minimal elements, *Advances in Applied Mathematics* 2026).
- **Allen-Celano-Mason arXiv:2511.18156** (Nov 2025) — Sign-reversing Garsia-Milne involutions work in NSym (inverse Kostka). Mason is also skew immaculate author. **Establishes that NSym sign-reversing involutions are viable.** Route C infrastructure.
- **Cho-Hwang-Lee arXiv:2603.03886** (Mar 2026, 6 pages) — Closes Sym/Schur half of Benedetti-Sagan. **READ alongside Allen-Celano-Mason** for Route C planning post-Nov 15.
- **Novelli-Thibon arXiv:2511.18366** — "The noncommutative geode." NSym Lagrange inversion; correction-term structure γ = (g−1)/(f−1) mirrors P_b = p_b + E_3·U_b. Check if Ψ = their Lagrange map under specialization.
- **arXiv:2507.02539** (July 2026) — "Semisimple algebras related to immaculate tableaux." Title suggests direct relevance to Rick's Schur-rank dichotomy. Not yet read.
- **Daugherty arXiv:2412.11013** — New Hopf algebra in partially commutative variables with explicit antipode. Technique transfer candidate for Route B.
- **Campbell 2022** — CONFIRMED: *Annals of Combinatorics* **27** (2023), no. 3, pp. 579–598. DOI: 10.1007/s00026-022-00632-0. No arXiv. S2 ID: 0688f5cc7ff55e2e0190b5f226dd2e5349a9d836. 3 citations (Daugherty 2401.02502, Campbell-Daugherty 2511.00713, Campbell 2308.03187). Extends Benedetti-Sagan beyond hooks and ≤2-row; scope requires PDF (Springer-paywalled).

## Key reference papers (Browse 112 additions — 2026-08-27)

- **Daugherty arXiv:2401.02502** (Jan 2024) — "Extended Schur functions and bases related by involutions." ~~HIGHEST PRIORITY READ before FPSAC writing~~ **READ (Day 141 wake).** φ falls outside ρ,ω classification. JWY rigidity does not constrain φ (degree-mixing). Cite in FPSAC §4.
- **Mason-Xie arXiv:2402.04219** (Feb 2024, published Involve 2026) — Classifies nonzero skew immaculate functions via Hall's Matching Theorem. **Directly relevant to Route C**: which S_{α/β} are nonzero for the antipode recursion?
- **Campbell 2022 "On Antipodes of Immaculate Functions"** — ~~Find via Google Scholar~~ **LOCATED (Browse 113): Annals of Combinatorics 27(2023) no. 3, pp. 579-598.** See Browse 113 additions above.
- **Campbell-Daugherty arXiv:2511.00713** (Nov 2025) — Lexical tableaux; new NSym/QSym bases. Cycle indicator signs. May give cleaner immaculate antipode sign description.
- **Lafrenière-Orellana-Pun-Sundaram arXiv:2409.00709** (2024) — ~~New work, check~~ **CHECKED (Browse 113).** Provides Δ(S*_α) explicitly. See Browse 113 additions.
- **FPSAC 2026 proceedings**: sites.math.washington.edu/fpsac2026/proceedings/ — **CHECKED (Browse 113).** No immaculate antipode or NSym automorphism papers. Marberg-Tong-Yu #20 = Grothendieck positivity for square root crystals (commutative world only).
- **Das-Pattanayak arXiv:2608.17431** — Newton identity for Z(U(q_N)), companion to Kashuba-Molev 2512.21631.

## Key reference papers (Browse 109 additions)
- **Iwao 2023 arXiv:2301.12741** (CONFIRMED) — "Generating functions of dual K-theoretic P/Q-functions and boson-fermion correspondence." Published Journal of Algebra 2026. 3 citations. β-deformed neutral-fermion VEV approach. **F=A·B IS NOVEL RELATIVE TO THIS PAPER** — Iwao's products are infinite products over alphabet, not EGF in degree variable b. Cite as K-theoretic background. READ DONE (Browse 109).
- **Cho-Hwang-Lee 2603.03886** (March 2026, READ Browse 109) — sign-reversing involution for antipode of Schur functions. Their sign = (−1)^{|λ|} = (−1)^{x_1+x_2+x_3}. Rick's sign = (−1)^{x_1+x_3}. **NOT directly applicable** — different map (S not Ψ) and different sign exponent. Journal paper direction: "e_2-transparent" Takeuchi modification. Cite as related work on Takeuchi sign involutions.
- **Bump-Hardt-Scrimshaw arXiv:2502.02841** (Feb 2025) — "Algebraic boson-fermion correspondence for factorial Schur functions." Classical (non-K-theoretic) boson-fermion. **READ NEXT** — does it contain a classical F=A·B?
- **Benedetti-Sagan arXiv:1410.5023** (2014/2016) — foundational sign-reversing involutions for nine combinatorial Hopf algebras. NSym immaculate case still open. Background for FPSAC sign discussion.
- **de Gier–Kenyon–Wheeler–Zhou arXiv:2606.22004** — "The asymmetric five vertex model on a rectangle." Integrable systems entering K-theoretic Schur P/Q space. Wheeler's vertex-model methods on GQ/GP territory. Watch for follow-up.
- **Brahma solo arXiv:2604.07352** (April 2026) — twisted factorial Grothendieck polynomials via weighted Grassmann orbifolds. Extension of BIAY framework. Route Arroyo data point. 0 citations.
- **Graf-Jing arXiv:2409.01479** — plethysm stability of Schur Q-functions. "Linear increase exception" may explain why Rick's sign is x_2-free. Read in journal paper investigation.
- **Iwao solo arXiv:2508.14484** (Aug 2025) — elementary construction of K-Q-cancellation ring. Next step in Iwao 2023 program. Background for β' paper introduction.
- **Arroyo–Hamaker–Hawkes–Pan arXiv:2503.16641** (March 2026) — Type C K-Stanley symmetric functions and Kraszkiewicz-Hecke insertion. 2 citations. Arroyo continuing his K-theoretic Schur Q program.
- **FPSAC 2027:** Website https://maths.universityofgalway.ie/fpsac2027/ — 7 invited speakers (Haiman, Yip, Bouvel, Fink, Iyama, Marietti, Mishna). No submission deadline posted yet. Watch for call (~Oct-Nov 2026).

## Key reference papers (Browse 108 additions)
- **Iwao 2023** — ~~PRIORITY READ~~ **READ (Browse 109).** arXiv:2301.12741. F=A·B novel relative to Iwao. See Browse 109 additions above.
- **Cho-Hwang-Lee 2603.03886** (March 2026) — ~~Read to check Takeuchi mechanism~~ **READ (Browse 109).** Sign (−1)^{|λ|} ≠ (−1)^{x_1+x_3}. Not directly applicable. Journal paper direction.
- **Brahma 2604.07352** (April 2026) — solo follow-up: twisted factorial Grothendieck polynomials via weighted Grassmann orbifolds. Alternating β-signs structurally matching Rick's sign pattern. Route Arroyo data point.
- **Marberg 2512.23944** (Dec 2025) — Positive specializations of K-theoretic Schur P/Q (K-theoretic Edrei-Thoma for GQ/GP). Current frontier of K-theoretic Schur-Q, directly adjacent to Arroyo's territory.
- **FPSAC 2027 website confirmed:** https://maths.universityofgalway.ie/fpsac2027/ Haiman + Yip invited. ~81 days from 2026-08-26.

## Key reference papers (Browse 107 additions)
- **Fernelius-Rozhkovskaya 2511.02710** (Nov 2025, revised Feb 2026) — W_{1+∞} action on Schur and Schur Q via formal distributions. READ in Browse 108: Rick's Ψ does NOT appear as W_{1+∞} specialization — ψ±(u) are free fermion fields. Paper is ambient context only. 0 citations.
- **Greaves-Jing-Zhu 2602.14190** (Feb 2026, 6 cites) — boson-fermion correspondence for t-Schur; hub connecting Jing-Rozhkovskaya to Lee cluster.

## Key reference papers (Browse 106 additions)
- **Jing-Rozhkovskaya 1610.03396** (J. Combinatorics 2019) — vertex operator Ψ± EGF for maps Sym → shifted-Sym. CLOSEST LITERATURE PARALLEL to Rick's EGF factorization F(T) = A(T)·B(T). Priority read.
- **Seelinger Schur Q lecture notes** (ghseeli.github.io) — classical Q(t)=E(t)·H(t) EGF parallel.
- **FPSAC 2027** (Galway, July 5–9) — Haiman invited. Target venue for β' paper. Watch for submission deadline ~November 2026.
- **Schilling Mittag-Leffler workshop lecture notes** (July 27–31 2026) — not yet posted; watch.

## People whose preprints are worth a look (updated Browse 104, 2026-08-21)
- **Seung Jin Lee (SNU)** — MOST URGENT WATCH. Five-paper June-July 2026 cluster on shifted t-Schur functions (2606.22058, 2606.28723, 2606.28108, 2607.01839, 2607.02108). StructB is the missing Pieri/degree result in his framework. Pieri rule for shifted t-Schur explicitly open.
- **Iryna Kashuba + Alexander Molev** — 2512.21631 (Dec 2025): HC images of queer Lie superalgebra quantum immanants = factorial Schur Q-polynomials. Path 1+2 bridge now extends to shifted/Q world.
- **Das, Pattanayak** — 2608.17431 (Aug 18 2026, brand new). Newton identity for q_N; Ivanov factorial Schur Q governs Z(U(q_N)). Watch for follow-up.
- **Naihuan Jing + Ming Liu** — Active: 2408.09855 (quantum Capelli, 11 cites), 2606.15138 (skew MN rule for Hopf dual pairs + skew (q,t)-Kostka ribbon expansion, Jun 2026). Both relevant to OQ-CHARGE-LIFT-AB.
- **Ilse Fischer + Moritz Gangl** — 2603.29836 (two Littlewood identities for spin HL, ASM/Pfaffian connection). Gangl at Lattice Path Conference 2026 (TU Wien Jul 2026). Watch for follow-up on ASM/spin HL.
- **Diego Plaza + Sebastián Sagurie** — 2608.07703 (Aug 7 2026): new algorithm for Kostka-Foulkes via Hecke pre-canonical bases. Watch for follow-up.
- **Aguiar, Lauve, Sottile, Reiner, Grinberg**
- Kashiwara, Lusztig, Schilling, Vazirani, Mathas
- Brundan, Kleshchev, Khovanov
- Assaf, Lam (Thomas), Williams (Lauren), Bergeron (Nantel/François)
- Seung Jin Lee — KR crystals, Lusztig q-weight multiplicities; FPSAC 2026 invited speaker
- Han Yang, Houyi Yu — weak Bruhat interval module classification
- Almousa, Lu — homological 0-Hecke algebra (ribbon complexes, Koszulness)
- Choi, Kim, Oh, Nam (Korean school) — poset modules of H_0(S_n)
- Young-Hun Kim — extremely active; arXiv:2604.24454 (Apr 2026) solo: 0-Hecke → Grassmannian K-theory
- Dominic Searles — type B 0-Hecke-Clifford, 0-Hecke-Clifford supermodules
- Sun-Young Nam — Choi-Nam-Oh group; descent Bruhat intervals, QSym Q-functions
- Spencer Daugherty — extended Schur functions, colored NSym/QSym, lexical tableaux
- Maas-Gariépy, Brauner, Corteel, Daugherty — crystal skeletons / quasicrystals
- Cain, Malheiro, Rodrigues — quasi-crystal graphs (hypoplactic monoid, NSym world)
- Hicks, Miller-Brown — quasisymmetric compatibility S_n / H_0(S_n)
- Barkley, Gaetz, Lam — KL combinatorial invariance conjecture; arXiv:2601.07793 PROVES CIC for coefficient of q (Jan 2026), CIC holds for all intervals ≤ length 6; BBDVW hypercube decompositions
- Riche, Situ — equivariant Koszul duality, category O, periodic KL (arXiv:2511.18518)
- Fujita, Qin — freezing operators, (q,t)-characters all classical types (arXiv:2601.00687)
- Ben Mills — isotropic meta-KL, type D Khovanov arc algebra (arXiv:2601.15426 Part I + 2605.23072 Part II); **diagrammatic Hecke school (Bowman-Stroppel-Williamson), NOT Marberg positivity**; scope = H_{(D_n,A_{n-1})} arc algebra isomorphism
- Bowman, Norton, Simental — BGG resolutions in cyclotomic Hecke algebras (JIMJ 2024) ⭐ BRIDGE PAPER
- Marberg — twisted-involution KL positivity, type B/D (arXiv:1306.2980 — 4 open conjectures)

## People to watch (added 2026-05-16, updated 2026-08-28)

- **Maria Esipova + Stephanie van Willigenburg** — **NEW Browse 113.** 2608.07459 (Aug 7, 2026): when do Daugherty's ρ/ψ/ω preserve dual immaculate functions? DUAL SIDE of Rick's φ question. High priority watch for follow-ups on immaculate automorphisms.
- **Pyuyi Chufeng Huang** — **NEW Browse 113.** 2608.07599 (Aug 6/15, 2026): NSym ribbon specialization GF = 1/₂F₁ satisfying Riccati ODE. Double-factorial connection to U_b(w). New voice in the NSym/combinatorial area.
- **Kyle Celano** — **NEW Browse 113.** Co-author with Allen and Mason (2511.18156): sign-reversing Garsia-Milne involutions in NSym. Mason's collaborator; watch for follow-ups on NSym involutions and skew immaculate.
- **Younggwang Cho, Byung-Hak Hwang, Hojoon Lee** — **NEW Browse 113.** 2603.03886 (Mar 2026): Resolved Sym/Schur half of Benedetti-Sagan. Korean group; 6-page technique is the model for Route B lift to NSym.

- **Akito Uruno** — NEW Browse 74. Found the error in Jang-Kwon 1810.02103 Section 5; became co-author on 2510.24451 (orthosymplectic crystal base + Burge RSK). Student/postdoc in Kwon group. Watch for follow-up on type D specifically.
- **Masahide Kobayashi + Hiroshi Matsumura** — NEW Browse 74. Two type C SSOT papers (2506.06951 "King tableaux with Berele insertion" + 2601.17603 "SSOT symmetry"). Cite Heo-Kwon. Building SSOT + Berele + BK framework for type C — the exact toolkit that would yield type D if they push there. Watch for type D extension.
- **Willie Aboumrad** — NEW Browse 74. arXiv:2208.09773 "Skew Howe duality for types BD via q-Clifford algebras" (2022, UNPUBLISHED). Multiplicity-free decomp of U_q(so_{2n}) spin tensor powers. Directly relevant to DIII RSK algebraic foundation. Why unpublished after 4 years?
- **Luis Cardenas** — NEW Browse 74. MO511324 (May 2026): working on right key tableaux for type C/D KN tableaux, no answers. Active researcher in adjacent territory. Check if any arXiv preprints.
- Igor Svyatnyy — cactus on GT patterns for o_N (2504.14344) and short SSYT/spinor crystal (2605.00514); both type D orthogonal via Howe duality; working toward type B-adjacent cactus; watch for next paper. **Browse 69 note: two papers in 2 months — active trajectory. Natural next step = iquantum crystal structure on regular cell tables. HIGH WATCH.**
- **Olga Azenhas** (Univ. Coimbra) — **NEW Browse 69.** Two 2026 papers on AII combinatorics: 2603.16698 (combinatorial inverse of Watanabe AII RSK via "slack data", v5 June 10 2026) and 2601.06930 (Lecouvey-Lenart conjecture solved via flagged hives). Her group is developing the combinatorial inverse / bijective RSK direction for AII. The DIII analogue of her "slack data" is a high-priority open question. Watch for type D extension.
- **Stefan Kolb** (Newcastle) + Milen Yakimov — **NEW Browse 69.** 2603.06132 "Short star products" (March 2026) — cleaner foundations for bar involution and quasi K-matrix in QSP. Core QSP foundational work. Kolb is the main source for QSP algebra foundations (alongside Letzter). Watch for further simplifications of iquantum RSK machinery.
- Iva Halacheva — type D cactus via RPP toggles (2412.02614 with Brown-Elek); her group is the most active on cactus for orthogonal types; type B = natural next target; gave "Categorical braid group actions" at ICMS Edinburgh Nov 2025 (slides may be posted)
- Jacinta Torres — only 1 arXiv citer (2409.12666 with Azenhas-Gonzalez-Huang); her group IS working on type B KN-tableau cactus via virtualization/orthogonal evacuation; watch
- **Bodish & Kalmykov (2025)** — "Orthogonal Howe Duality and Dynamical Split Symmetric Pairs" (Comm. Math. Phys. 2025, DOI: 10.1007/s00220-025-05482-4); ⛔ SCOPED OUT — no BDI/crystal content; cite Watanabe once in Remark 1.5 speculatively
- Hideya Watanabe — **Rikkyo University, Tokyo** (CORRECTED Browse 59). Q-SPHERE talk (June 9): "Quantizations of coordinate algebras of symmetric pair subalgebras." No new 2026 preprint. Most recent: arXiv:2502.07270 (AII, J. Algebra 2026, 5 cites — no new citers Browse 66). **KEY PRIOR PAPER: arXiv:2107.00170 (2021)** DEEP READ Browse 67: Type AI = GL_n↓SO_n (same-rank, NOT DIII = GL_n↓SO_{2n}). AI-tableaux with K(C_1)≤C_2 condition; AI-crystal; P^{AI} insertion algorithm. 4 cites. New June 2026 citer: Bae-Kwon arXiv:2506.05959 (q-deformed orthosymplectic Howe duality). DIII analogue completely open — **OQ-WATANABE-AI-TABLEAU-DIII (HIGH, renamed from BDI).** Watch for Watanabe-Hoshino bi-icrystal preprint June-August 2026.
- **Mao Hoshino** (RIKEN iTHEMS; Kawahigashi group alum) — **NOT a Q-SPHERE 2026 speaker** (Browse 54 confirmed). Watanabe presented solo. Hoshino's collaboration may produce a preprint rather than a Q-SPHERE contribution. Watch for preprint June-August 2026. C*-algebras / operator algebras background.
- **Weinan Zhang** (Wang group; now at Univ. Hong Kong) — arXiv:2509.18982 "Quantum Howe duality type AIII / type B Hecke": proves iquantum AIII weight spaces ≅ type B Hecke modules; **PUBLISHED: Math. Z. 312, article 53 (2026)**. HIGH relevance for NSym^B + Paths 2↔3 bridge; update citation in any draft to journal ref. **COMPANION:** arXiv:2508.12041 (Wang-Zhang, Aug 2025) "Relative braid group symmetries on modified iquantum groups and their modules" — cited by Song-Zhang 2601.19670 as core reference; 3 cites. **NEW Browse 44.**
- **Yingjin Bi** — extending KKOP bosonic extensions to cluster structures (arXiv:2506.00882) and twisted flag varieties (arXiv:2602.11559); LOW relevance to coideal territory for now; watch
- **Shen-Su-Xiong** — arXiv:2510.12118 "Quivers with Involutions and Shifted Twisted Yangians via Coulomb Branches" (2025, 6 cites); coideal subalgebras meeting Coulomb branch geometry; fastest-moving adjacent paper in Browse 43 sweep; **NEW Browse 43**
- **Euiyong Park** (KKOP co-author) — "Crystals and quantum twist automorphisms" (ICMS Edinburgh Nov 2025 talk); unknown scope; check slides
- **Bárbara Muniz** — arXiv:2505.21738 "Symplectic Branching through Crystals" (May 27, 2025); independent proof of Naito-Sagaki conjecture via crystal tableau bijection with Sundaram's model; complementary to Watanabe-Naito-Suzuki 2502.07270 (mutual citation). **arXiv ID FOUND (Browse 59).** 2 cites. Read intro — Sundaram model for GL→Sp; check if ports to BDI.
- **Toshiyuki Kobayashi** — **DEEP READ (Browse 66).** arXiv:2604.22262 "Stability of Branching Multiplicities for Orthogonal Gelfand Pairs" (2026, 50pp): fences = {ξᵢ + δνⱼ = ±½} in inf-char space; (O(n+1),O(n)) only — NOT GL(n)↪SO(2n). Rick's R-AXIS=1 → single BDI fence. Companion: arXiv:2604.25242 (38pp sl_2 expository — **CORRECTED: NOT 6pp without arXiv ID**; this IS on arXiv). NEW: arXiv:2503.23749 "Lower semicontinuity of bounded property in the branching problem and sphericity of flag variety" (March 2026) — OQ-KOBAYASHI-LOWER-SEMICONT. Full Kobayashi program: 2509.17007 (Sep 2025) → 2604.22262 (Apr 2026) → 2604.25242 (Apr 2026) → 2503.23749 (March 2026, separate thread). None cover GL(n)↪SO(2n).
- **Olga Azenhas** — arXiv:2603.16698 "Recording tableaux of quantum LR map" (Mar 2026): characterizes k-highest weight tableaux by **linear inequalities** in the quantum LR map (AII/GL→Sp). **FULL READ (Browse 59):** Inequalities are in multiplicity space — same coordinate system as Rick's BDI walls. AII has ~2(n-1) walls GROWING with n; BDI has exactly 3 walls for ALL n. Structural contrast is a publishable remark. Azenhas explicitly "hopes a geometrical object will emerge" (line 469) — Rick has computed this for BDI. Cites KTW math/0107011 (facet machinery). OQ-AZENHAS-INEQUALITIES-BDI: **POSITIVE** — confirmed AII analogue of Rick's BDI walls. Companion: arXiv:2604.25856 "slack data."
- **Jonathan Brundan, Weiqiang Wang, Ben Webster** — arXiv:2505.22929 "Categorification of quasi-split iquantum groups" (May 2025, 91pp): first uniform categorification of ALL quasi-split types via graded 2-categories. BDI type included. Natural stepping stone to BDI icrystal bases. **NEW Browse 57. MEDIUM priority.**
- **Masatoshi Kitagawa** — arXiv:2503.23749 "Lower semicontinuity of bounded multiplicity" (Mar 2025): bounded multiplicity → sphericity of partial flag variety. Structural context for Kobayashi fences. **NEW Browse 57.**
- **Kumar-Torres 2024** — "Branching models of Kwon and Sundaram via flagged hives" (5 cites): hive polytopes for Sp branching. Check if BDI branching cone is a hive polytope. **OQ-KUMAR-TORRES-HIVES. NEW Browse 57.**
- **Jae-Hoon Kwon** — invited speaker at FPSAC **2025** (Sapporo), NOT 2026. He is on the FPSAC 2026 program committee. ~~FPSAC 2026 invited speaker~~ — **CORRECTED Browse 58.** Watch for orthosymplectic crystal / affine RSK preprints. FPSAC 2026 relevant invited speaker is Seung Jin Lee (q-weight multiplicities, types B/C).
- **Seung Jin Lee** — FPSAC 2026 invited speaker (Seattle, July 13-17): "Lusztig's q-weight multiplicities and their refinements." Result (arXiv:2412.20757 with Choi and Kim): energy functions of KR crystals give q-weight multiplicities in types B and C. Directly adjacent to BDI. **NEW Browse 58.**
- **Jang** (with Kwon and Uruno) — arXiv:2510.24451 "Crystal base of the negative half of quantum orthosymplectic superalgebra" (Oct 2025, 55pp). Introduces "Burge correspondence of orthosymplectic type." Directly neighbors BDI crystal problem. **HIGH — NEW Browse 58.**
- **Heo** — arXiv:2504.12106 "A New Description of the Bicrystal B(∞) and the Extended Crystal" (Apr 2025). "Sliding diamond rule" for bicrystal; potential prerequisite for Watanabe-Hoshino bi-icrystal paper. **NEW Browse 58.**
- **Song** (with Zhang) — arXiv:2601.19670 "Representations of quantum symmetric pairs at roots of unity" (Jan 2026). Extends iquantum branching to roots of unity. Cites Watanabe 2407.07280 and 2509.00853. **NEW Browse 58.**
- **Stein Meereboer** (NOT Lucas — corrected Browse 68) — arXiv:2510.17655 "Based morphisms for characters of QSP" (Oct 2025); covers Hermitian types including **DIII_b** — CHECK whether DIII_b = (so(2n), gl(n)). Second paper: arXiv:2502.19232 (Macdonald-Koornwinder polynomials direction). Announced "Kostant's branching law for QSP" (joint with Kolb) at Q-SPHERE June 9 — no arXiv preprint T+8d. Moving to MPIM Bonn (Stroppel) Fall 2026. **Watch: preprint expected summer 2026. Email: stein.meereboer@ru.nl. NEW Browse 59; UPDATED Browse 68.**
- **Catharina Stroppel and Liao Wang** — arXiv:2601.18709 "Weight modules for quantum symmetric pair subalgebras" (Jan 2026, 0 cites): Verma modules, HC isomorphism, Clebsch-Gordan for QSP type (gl_4, gl_2×gl_2). Cites Kolb-Stephens. Infrastructure building toward type D. **NEW Browse 66.**
- **Johannes Frohmader** — arXiv:2312.11295 "Graded Multiplicities in the Kostant-Rallis Setting" (2023, 1 cite): DEEP READ Browse 67. Covers GL_n↓O_n (type AI) + GL_{2n}↓Sp_{2n} (type AII). NOT DIII = GL_n↓SO_{2n}. Degree statistic d(T) uses ceiling function ⌈φ_i(T)⌉ from Kostant-Rallis. Sole citer: Frohmader-Heaton arXiv:2402.16198 (2024, cyclic quivers). Related: Colarusso-Erickson-Frohmader-Willenbring arXiv:2502.19505 (2025, Howe duality K_R-types). **DIII analogue completely open — OQ-FROHMADER-DIII (HIGH). UPDATED Browse 67.**
- **Jae-Hoon Kwon / Bae-Kwon** — arXiv:2506.05959 "q-deformed Howe duality for orthosymplectic Lie superalgebras" (June 2026, accepted Letters Math. Phys.). DEEP READ Browse 68: covers (osp(2m|2n), O_ℓ)/(osp(2m|2n), Sp_{2ℓ}) via AI/AII iquantum groups. NOT DIII directly. Special cases include (so_{2n}, O_ℓ) — adjacent. Template for DIII q-Howe duality. Only 2025/2026 citer of Watanabe 2107.00170. **UPDATED Browse 68. OQ-BAE-KWON-ORTHOSYMPLECTIC (MEDIUM).**
- **Svyatnyy** — arXiv:2504.14344 "On the action of the cactus group on Gelfand-Tsetlin patterns for orthogonal Lie algebras" (Apr 2025, 0 cites). Uses **(O_N, so_{2n}) Howe duality** from crystal side. Introduces "regular cell tables" as SSYT-analogs for o_{2n} — potential DIII-tableaux precursor. Crystal commutors on (Λ C^n)^{⊗N}. **NEW Browse 68. HIGH — OQ-SVYATNYY-REGULAR-CELL-TABLES.**
- **Salmasian, Savage, Shen** — arXiv:2507.12328 "The disoriented skein and iquantum Brauer categories" (published Forum of Mathematics: Sigma 2025). Categorical/diagrammatic approach to iquantum algebras; cites Brundan-Wang-Webster 2505.22929. Check if BDI covered. **NEW Browse 59. MEDIUM priority.**
- **Lu, Pan** — arXiv:2504.19073 "Dual canonical bases for iquantum groups via Hall algebras" (Apr 2025). Foundational for U^ι canonical basis / dual crystal basis theory. Adjacent to OQ-IQUANTUM-RSK-LIFT. **NEW Browse 59.**
- **De Commer, Neshveyev, Tuset, Yamashita** — arXiv:2009.06018 "A KL theorem for quantum groups" (published Forum Math. Pi 2023). Foundational KL result. Q-SPHERE June 12 talk announced a **type B strengthening in progress** — watch for new preprint June-August 2026. **HIGH PRIORITY watch.**
- **Álvaro Gutiérrez + Martínez + Szwej + Wildon group (Bristol/Columbia)** — NEW Browse 82 (2026-07-11). Three connected programs: (1) 2607.06749 "field-independent filtration categorifying U_q(sl₂) Cartan product rule" (full paper FPSAC 2026 poster); (2) 2412.15006 "Towards plethystic sl₂ crystals" (counting formulas for SL₂ plethystic coefficients); (3) 2511.02649 (with Orellana-Saliola-Schilling-Zabrocki) geometric/Ehrhart approach to plethysm. OQ-GUTIERREZ-PLETHYSTIC-CRYSTAL: do their counting formulas for a^{n,m}_k = Rick's M_j? Direct connection plausible. Watch for new papers.
- **Josaphat Baolahy + Randrianirina Benjamin** — NEW Browse 86 (2026-07-14). arXiv:2604.10336 "Species, Symmetric Functions, and Kronecker Product" (Apr 2026). Introduce K_α basis = PRODUCT of C-molecules (ordinary product in Sym, not plethystic composition). PRODUCT-LAND — first 2025/2026 paper in this territory. URGENT: does K_{(2^j,1^{n-2j})} = e_2^j · p_1^{n-2j}? If yes → M_j identified via species. Watch for follow-up.
- **Nikolai Beluhov** — NEW Browse 86 (2026-07-14). arXiv:2506.12789 "Powers of 2 in High-Dimensional Lattice Walks" (ECA 2026). ν₂ of lattice walk counts splits by d mod 4 as pure digit-sum via ABACUS METHOD (Kummer carry stratification by paired binary digits). Structural template for D(c) derivation. HIGH relevance to beta-prime-digit-sum-formula structural proof.
- **Yifeng Zhang** (South China Normal) — NEW Browse 96 (2026-08-13). arXiv:2608.03792 "Molecules of an affine FPF W-graph and a labelled row-Beissinger reconstruction" (Aug 8, 2026). Classifies FPF W-graph molecules via affine matrix-ball construction; bridges FPF involution combinatorics to KL cells. Three papers 2023-2026 in FPF / type B/D W-graph territory. **Watch for type D / DIII extension. OQ-ZHANG-FPF-WGRAPH-DIII.**
- **Bergeron + Gagnon + Nadeau + Spink + Tewari** — NEW Browse 96 (2026-08-13). arXiv:2508.12171 "The quasisymmetric flag variety" (Aug 2025) + arXiv:2604.24903 "The Quasisymmetric Grassmannian" (Apr 2026). Geometric foundations for QSym coinvariants; parallel to classical flag variety / Schubert calculus. May give geometric home to crystal skeleton tensor products. Path 1+4 bridge. Medium priority.
- **Pak, Panova, Swanson** — NEW Browse 86 (2026-07-14). arXiv:2511.02312 "A combinatorial interpretation for certain plethysm and Kronecker coefficients" (2025). Explicit #P (marked trees) formula for ⟨s_μ[s_ν], s_λ⟩ when λ ≤ 2 rows. Check: M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ with λ two-row — does it fall in scope?
- **Gutiérrez + Krattenthaler** — NEW Browse 86 (2026-07-14). arXiv:2509.22648 "Schur log-concavity and the quantum Pascal triangle" (2025). Quantum Pascal triangle = sl_2 Clebsch-Gordan table. Likely contains M_j table explicitly. Priority read next session.
- **Bergeron-Gagnon-Nadeau-Spink-Tewari group** — NEW Browse 86 (2026-07-14). Four-paper series 2025-2026 building a geometric theory of quasisymmetry: quasisymmetric flag variety (2504.15234, 2508.12171), Coxeter flag variety (2601.23111), quasisymmetric Grassmannian (2604.24903). Cohomology rings = QSym coinvariants. Noncrossing partitions replace permutations. Bergeron giving FPSAC 2026 plenary Friday. Watch for Hecke/crystal interpretations.
- **Emily Gunawan** — NEW Browse 82 (2026-07-11). April 2026 talk "Box-ball systems, RSK tableaux, and the Motzkin numbers" (egunawan.github.io). Someone connecting RSK tableaux to Motzkin numbers via box-ball systems. Potentially same phenomenon as Rick's K_{μ^T,(2^j)} = m^(2)_{k,j}. LOW-MEDIUM watch; check for arXiv paper.
- **Sam Johnston + Khoa Nguyen + Anne Schilling** — NEW Browse 82 (2026-07-11). arXiv:2606.02972 "RSK and crystal structures via 5-vertex model uncrowding" (2026). Schilling's new approach to RSK via 5-vertex lattice model uncrowding. OQ-SCHILLING-RSK-5VERTEX: does 5-vertex model extend to type D? Watch for type D extensions.
- **Barnard + McConville** — arXiv:**1808.05670** (CONFIRMED Browse 94). 2018 paper "Lattices from graph associahedra and subalgebras of the Malvenuto-Reutenauer algebra" (21 cites), CITED in 2607.12232 as reference [1]. The MR Hopf algebra subalgebra structure is in the crystal skeleton references but NO connection is drawn to Hopf structure. Follow-up: **Dahlberg-Fishel arXiv:2409.13898** (2024) — cited as [7] in 2607.12232, connects tubing lattice to crystal skeletons for Stanley sym fns. READ BOTH for Hopf morphism route.
- **Loic Poulain d'Andecy** — arXiv:2603.19069 **DEEP READ (Browse 94).** sl_2 multiplicity tables are the Catalan/Motzkin/order-d triangles: c_{k,n}^{(d)} = b_{k-1,n}^{(d)} - b_{k+1,n}^{(d)}. M_j connection: if M_j = dim Hom_{sl_2}(trivial, V_2^{otimes 2j}), then M_j = c_{1,2j}^{(2)} = Catalan(j). TRANSLATION NEEDED (Frobenius formula; one computation). Paper uses q-number / Pascal language, not Sym inner products.
- **Yu (arXiv:2607.09157)** — **CONFIRMED IRRELEVANT (Browse 94 deep read).** Math NT paper (multiple zeta/Eisenstein series) using Young tableaux as index sets. Coproduct = deconcatenation, not alphabet-doubling. No crystal content. Discard.
- **Lai, Nakano, Xiang** — NEW Browse 82 (2026-07-11). arXiv:2511.19825 "Quantum wreath products and Schur-Weyl duality II" (Nov 2025). Constructs wreath modules for Ariki-Koike, Hu algebra, affine Hecke. **SOLVES GGOR for Type D rational Cherednik algebra** via Hu algebra wreath modules. OQ-LAI-NAKANO-XIANG-TYPE-D filed: does their Type D Category O connect to DIII RSK/crystal? The Hu algebra is H_q(D_{2m}); its modules should be DIII-adjacent.
- **Vidas Regelskis** — NEW Browse 94 (2026-07-18). arXiv:2607.14692 "Twisted Yangians of types BI, CI, DI" (July 2026). DI = type D Yangian; Drinfeld-type current presentations; coideal coproducts. First type D quantum group paper in post-FPSAC wave. OQ-DI-YANGIAN-DIII-RSK. Watch for follow-up papers.
- **Bodish + Elias + Rose** — NEW Browse 94 (2026-07-18). arXiv:2607.13252 "Type B Webs" (July 2026). Solves Kuperberg 1996 for type B; ι-quantum group braid symmetries. Path 2+3 categorification infrastructure.
- **Cai, Jiang, Jing, Li, Ye** — NEW Browse 94 (2026-07-18). arXiv:2607.14362 "Measures and Generalizations of Dual Littlewood Identities" (July 2026). Types B, C, D dual Littlewood identities; Fock space; type D explicit. Path 1+2.
- **Goertzen + Williamson** — Browse 94 URGENT, Browse 97 ID FOUND. arXiv:**2604.18894** "Kazhdan-Lusztig Basis and Optimization" (Apr 20, 2026). KL basis = maximal (1+s)-invariant cone in Specht modules. Proved: hooks, two-column, (n-2,2). Type A only — no type D anywhere. **OQ-2 territory: type D analogue completely open and uncrowded.** Williamson is the strongest KL group; type D extension is Rick's potential.
- **Tom Goertzen** — NEW Browse 97 (2026-08-14). Postdoc at U Sydney (Williamson group). First author on 2604.18894. Watch for follow-up on KL optimization beyond type A.
- **Lauve + Lazzeroni** — sequel arXiv:2604.10816 "Hopf substitutions in Species" (Apr 2026). NEW Browse 97. Asks which species substitutions preserve Hopf monoid structure. Direct sequel to OQ-1 (2603.19494). Read alongside the FPSAC proceedings paper.
- **Marberg + Scrimshaw** — arXiv:2608.11009 "Square root crystals and the square root of B(∞)" (Aug 11, 2026, 54pp). NEW Browse 97. Monoidal category of N-root crystals; square root of B(∞). Marberg is Rick's primary DIII watch; this paper is about monoidal tensor structure on new crystal categories — Path 2+4 bridge.
- **Yifeng Zhang** — arXiv:2503.21215 "Cell classification of the row Gelfand S_n-graph" v2 August 12, 2026. NEW Browse 97. Cell=molecule result in type A via Greene + Nguyen orderedness. Open type D analogue via Garfinkle insertion.
- **Lapointe + Pena** — arXiv:2608.13276 (Aug 13, 2026). New characterization of right keys via decreasing subwords. NEW Browse 97.
- **Nguyen-Dang** — arXiv:2608.10516 (August 2026). Lorentzian conjecture for skew Schur functions via Richardson varieties. Cites Lam-Lauve-Sottile 0908.3714 — new external community (Lorentzian polynomials) pulling on Hopf-algebraic skew LR. NEW Browse 97.
- **Kashiwara, Kim, Oh, Park** — arXiv:2608.15020 "Monoidal seeds of the categories C_{w,v} over quiver Hecke algebras" (Aug 15, 2026, 3 days old at Browse 98). New quantum monoidal seeds for C_{wv} using reflection functors K_i, F_i. Proves K(C_{wv}) lies between cluster algebra and upper cluster algebra on coordinate ring of open Richardson variety. **Interfaces directly with 2601.07793 (Barkley-Gaetz-Lam) via Richardson variety cluster structure.** KKOP group hitting Path 2+3 intersection. **HIGH PRIORITY — read next wake.** NEW Browse 98.
- **Jing, Liu (Naihuan Jing + Ning Liu)** — arXiv:2606.15138 "A skew Murnaghan-Nakayama rule for Hopf dual pairs" (Jun 2026). Generalizes Lam-Lauve-Sottile from LR rules to MN rules for arbitrary Hopf dual pairs including (Λ^(k), Λ_(k)) = k-Schur/affine Grassmannian Hopf pair. **THE Path 1↔4 gap**: nobody has connected the abstract skew MN for k-Schur to explicit KR crystal tensor products. **OQ-JING-LIU-KR-CRYSTAL-MN.** NEW Browse 98.

- **Bump + Hardt + Scrimshaw** — arXiv:2410.06582 "Factorial Fock Free Fermions" (Oct 2024) + arXiv:2502.02841 "Boson-Fermion Correspondence for Factorial Schur Functions" (Feb 2025). **HIGHEST PRIORITY for OQ-DEG-J-ALPHA-BOUND.** Cor. 6.15 of 2410.06582 has explicit factorial Schur Pieri expansion s_λ · h_r in double supersymmetric Schur basis. Section 7 of 2502.02841 = "Skew-Pieri rule" with no cancellations at β=0. The two-alphabet parameter structure matches Rick's π=(b+1)c, σ=b+c+1. Six-vertex model / transfer matrix approach may give degree bounds. **Read Cor. 6.15 first in next PROVE session.** NEW Browse 100.
- **Houcine Ben Dali + Lauren Williams** — arXiv:2510.02587 "Combinatorial formula for Interpolation Macdonald polynomials" (Oct 2025, FPSAC 2026 talk). + arXiv:2602.13492 "Interpolation t-Push TASEP" (Feb 2026). **Gap confirmed Browse 100:** Pieri rule M*_μ · h_p = Σ c^ν M*_ν not stated explicitly anywhere. My ballot/Catalan seed observation is a direct approach at q=t=1. NEW Browse 100.
- **Takeshi Ikeda + Shinsuke Iwao + Mark Shimozono** — arXiv:2511.20966 "Equivariant homology of symplectic affine Grassmannian and dual affine Schur P-functions" (Nov 2025, 50pp). Dual factorial P-functions via affine nil-Hecke; open Pieri problem explicitly stated; degree-bounded polynomial coefficients = symplectic analogue of Rick's α_{p,k}(j,σ). Hopf algebra structure on H^T_*(GrSp_{2n}) deferred to future work. NEW Browse 100.
- **Joshua Arroyo** — arXiv:2511.05734 "Pieri rule for GQ functions via strict decomposition tableaux" (Nov 2025). K-theoretic Pieri for strict partitions; ballot/Catalan structure = leading β term. NEW Browse 100.
- **Ryan Mickler** — arXiv:2606.17822 "Congruences of Shifted Jack LR Coefficients" (June 2026). Open problem: extend to shifted Macdonald functions. NEW Browse 100.
- **Khai-Hoan Nguyen-Dang** — arXiv:2608.10516 "Richardson volume models for skew Schur P/Q-functions" (Aug 2026). Richardson variety approach to shifted skew LR; cites Lam-Lauve-Sottile and Jing-Liu. NEW Browse 100.
- **Loic Poulain d'Andecy + Jeremie Guilhot** — arXiv:2602.20861 "KL bases of parabolic Hecke algebras + Schur-Weyl duality" (Feb 2026). RSK indexing of KL cells; Schur-Weyl kernel via KL basis. NEW Browse 100.
- **Shaolong Han** — arXiv:2607.20934 "Closed formulas for energy functions on tensor squares of perfect crystals in classical affine types" (Jul 2026). Explicit piecewise-linear energy formulas for all seven classical affine types at all levels. Fills long-standing gap; RR identities emerge. NEW Browse 100.

- **Stepan Naprienko** — arXiv:2301.12110 "Free fermionic Schur functions" (2023, 8 citations). **HUB PAPER (Browse 101).** Unifies factorial, supersymmetric, and dual Schur functions via free fermionic six-vertex model with (a,b)-parameters. Key upstream reference for Bump-Hardt-Scrimshaw 2410.06582. The (a,b)-parameter structure matches Rick's (π,σ) = ((b+1)c, b+c+1) — **Route N for StructB.** Cited by Panova-Petrov (2409.17842), Gunna-Wheeler-Zinn-Justin (2504.19205). Watch for follow-ups on degree-bounded expansions. NEW Browse 101.
- **Lucas Teyssier** — arXiv:2508.06770 "Bounds on skew dimensions and characters via thick hook decompositions" (2025, 2 citations). **StructB-adjacent (Browse 101).** Uses Naruse hook-length formula to prove degree bounds for standard tableaux of skew shapes; improves Féray-Śniady bounds. Methodology directly adjacent to StructB degree bound. NEW Browse 101.
- **David Plaza + Yamil Sagurie** — arXiv:2608.07703 "Positivity of pre-canonical bases for spherical Hecke algebras — Kostka-Foulkes" (Aug 7, 2026). New Schur-positive basis via Satake isomorphism + pre-canonical Hecke transitions. Kostka-Foulkes positivity proved. Hecke-Sym bridge exactly what Rick needs for StructB. NEW Browse 101.
- **Richmond + Tewari** — arXiv:1905.10942 "Noncommutative LR coefficients and crystal reflection operators" (2019, **0 citations** after 7 years). **URGENT READ (Browse 101).** Directly at Path 1+4 intersection: NC Schur + crystal reflection operators = explicit LLS coproduct-crystal connection. Zero citations despite being precisely on target. Either has the answer or is completely overlooked. NEW Browse 101.
- **Hong Chen + Siddhartha Sahi** — arXiv:2403.02490 "Interpolation Polynomials, Binomial Coefficients, and Symmetric Function Inequalities" (2024, 7 citations); series of 4 papers 2024-2025 extending Knop-Sahi-Okounkov interpolation polynomial program. LR positivity and monotonicity for shifted basis Ω_λ(1+x;τ). Adjacent to Rick's shifted-Schur interpolation master technique. NEW Browse 101.
- **D'Adderio, Interdonato, Iraci, Pagaria** — arXiv:2608.14836 "Theta conjecture proved" (Aug 14, 2026). Explicit Negut operator formula in Dyck path algebra; proves 2019 Theta conjecture; Lean-verified. Major q,t-combinatorics event this week. Not directly adjacent to Rick's work but significant. NEW Browse 101.
- **Guo, Kang, Xiong** — arXiv:2608.11543 "Butler's positivity conjecture" (Aug 12, 2026). Proves Butler's 1994 conjecture: $(T_\lambda H̃_\mu - T_\mu H̃_\lambda)/(T_\lambda-T_\mu)$ is Schur positive. Another 32-year-old conjecture resolved this week. NEW Browse 101.

- **Brahma, Ikeda, Iwao, Yang** — arXiv:2603.20865 "Neutral-Fermion Constructions of Factorial gp- and gq-Functions" (March 2026). **HUB FOR ARROYO ROUTE (Browse 105).** Neutral-fermionic vacuum expectation values for factorial GQ-functions; Pfaffian formula for factorial gq. "Remarkable coincidence": all four transition coefficient families (gp, gq, GP, GQ) equal, expressible via factorial Grothendieck type A. Setting equivariant parameter → 0 should be compared to Rick's (1,1,2)-weight computation. This is the algebraic backbone of Arroyo's SDT. **COMPUTE THIS WEEK.** NEW Browse 105.
- **Zachary Hamaker** — coauthor on Arroyo-Hamaker-Hawkes-Pan 2025 "Type C K-Stanley symmetric functions and Kraskiewicz-Hecke insertion." Active in K-theoretic insertion / type C K-theory. Direct predecessor to Arroyo 2511.05734. Watch for new papers on K-theoretic shifted tableaux. NEW Browse 105.
- **HUB: Ikeda + Naruse 2011** — "K-theoretic analogues of factorial Schur P- and Q-functions" (Advances in Mathematics, 121 citations). Foundational paper for GQ-functions. The beta-deformation structure that produces Arroyo's intrinsic degree bound originates here. Rick must read this to understand Route Arroyo. **PRIORITY READ.** Identified Browse 105.

- **Allen + Mason** — arXiv:2511.18156 "Tunnel Hook Coverings and the Garsia-Milne Involution" (Nov 2025). **HIGHEST for OQ-KOSTKA-CANCELLATION-A-B (Browse 102).** Combinatorial proof of K⁻¹K = I via Garsia-Milne involution on SSYT with sign = (−1)^{height(rim hook)} — structurally parallel to Rick's (−1)^{(μ_2−μ_3)/2} parity signs. NSym-first-then-Sym strategy. Read §2-3 to check if involution restricts to K_{μ',(2^j)} and pairs by (μ_2−μ_3) parity.
- **(unknown)** — arXiv:2505.10783 "Local Framework for Rectangular Kostka Matrix Inversion" (May 2025). **HIGH for OQ-KOSTKA-CANCELLATION-A-B (Browse 102).** Bijective proof for rectangular Kostka matrix inversion; K_{μ',(2^j)} explicitly in scope. Read §3-4 for the involution filtration structure.
- **S.-J. Lee** — arXiv:2607.02108 "A Two-Color Lift of the Shifted t-Schur Measure" (July 2026). **NEW Browse 102.** Cites O-O q-alg/9605042; half-vertex operators on strict partitions via $Q_\mu(qX)$; Pfaffian correlation kernels; two-color grading may correspond to parity of (μ_2−μ_3) in Rick's shifted Schur filtration. Path 3 + shifted Schur.
- **Gunna + Wheeler + Zinn-Justin** — arXiv:2504.19205 "Structure Constants for Spin Hall-Littlewood Functions" (Apr 2025). Main 2025 citer of Naprienko 2301.12110. Honeycomb + Yang-Baxter lattice model for spin HL structure constants. Context for Route N (Naprienko). NEW Browse 102.
- **Cho + Hwang + Lee** — arXiv:2603.03886 "Sign-Reversing Involution for Schur Antipode" (Mar 2026). Resolves Benedetti-Sagan question on Takeuchi expansion of Schur functions; free quasi-symmetric monoid involution. Methodology adjacent to Rick's Kostka cancellation involution. NEW Browse 102.
- **[Update]** Marberg arXiv:2512.19034 — **MAJOR REVISION July 2026**: added type D Brion atoms + involution Schubert polynomials for all classical types. Substantive new content; reread before FPSAC 2027 submission. DIII sentinel but now richer.

- **Marc van Leeuwen** — arXiv:math/0602357 "Schur Functions and Alternating Sums" (2006, Memoirs AMS). **HIGHEST for OQ-KOSTKA-CANCELLATION-A-B (Browse 103).** Canonical reference for sign-reversing involutions in symmetric function theory. Rick's identities (A)/(B) are shape-indexed variants of this framework; read §2-3 to model the (μ₂-μ₃)-parity involution on SSYT(μ',(2^j)). New to feeds: not previously in Browse reading logs.
- **Jing + Liu + Molev (Naihuan Jing, Ning Liu, Alexander Molev)** — arXiv:2408.09855 "The q-Immanants and Higher Quantum Capelli Identities" (2024). **NEW Browse 103.** Factorial Schur polynomials appear as Harish-Chandra images in Z(U_q(gl_n)); proves quantum Capelli identities. Best existing bridge between Rick's O-O master technique (shifted-Schur interpolation) and Hopf algebra filtration structure (center of U_q). OQ-HARISH-CHANDRA-STRUCTB: if S_j ∈ Z(U_q(gl_n)) via Harish-Chandra, StructB follows from center structure.
- **Estupiñán-Salamanca + Pechenik** — arXiv:2503.14609 "Shifted LR Rule via Shifted Plactic Monoid" (March 2025). **NEW Browse 103.** First algebraic proof of shifted LR via shifted plactic monoid + "constructed tableaux" rule. Adjacent to Molev-Sagan barred/unbarred switch Rick wants for identities (A)/(B). (NB: different from their 2602.18632 which is a DIII sentinel.)
- **FPSAC 2026 Proceedings** — LIVE at https://sites.math.washington.edu/fpsac2026/proceedings/ (confirmed Browse 103, July 27, 2026 per web agent). Check for Lauve-Lazzeroni r-QSym, Seung Jin Lee invited talk notes (q-weight multiplicities, types B/C via KR crystals + Catalan functions), Chueluecha-Morse (skew Catalan + Genocchi), Ruizhen Liu (Best Student Paper, Deligne-Lusztig + q-Klyachko).

## MathOverflow / StackExchange — PERMANENTLY BLOCKED

**Browse 18 (2026-05-20) confirmed: MathOverflow and Math StackExchange are blocked at the Anthropic API level (HTTP 400), NOT a Cloudflare JS challenge.** No workaround exists via any available tool. Remove from all future browse plans. Do NOT retry.

## Upcoming events to watch for lecture notes
- **✅ Q-SPHERE 2026, Radboud University Nijmegen, June 8-12, 2026** — **CONCLUDED (Browse 56, June 11). T+1d (Browse 59, June 13): zero new preprints.** KEY PENDING PREPRINTS to watch (June 16–30): (1) **Watanabe-Hoshino bi-icrystals** (Watanabe @ Rikkyo University, not RIKEN — corrected Browse 59; no preprint yet; abstract mentions bicrystals; watch for joint Watanabe-Hoshino preprint); (2) **Meereboer-Kolb "Kostant's branching law for QSP"** (Meereboer solo precursor = 2510.17655 iota crystal 1-dim; joint paper in progress); (3) **De Commer-Neshveyev-Tuset-Yamashita "KL theorem in type B"** (June 12 talk confirmed this is in progress; based on arXiv:2009.06018 Forum Math. Pi 2023). Already-posted relevant preprint: **Kolb-Yakimov arXiv:2603.06132** (short star products for QSP). Details: `connections/q-sphere-meereboer-fourth-community-deadline.md`.
- IMJ-PRG Integrable Combinatorics Summer School, Paris, **June 15-19, 2026** — Anne Schilling mini-course "Crystals and symmetric functions" (June 17-18 lectures + exercise class); indico.math.cnrs.fr/event/14175/. No slides yet. Check after June 18.
- FPSAC 2026, Seattle, July 13-17, 2026 — **CONCLUDED (Browse 92, July 17)**. Bergeron plenary (Fri July 17): "Crossing, or Not, in the Quasisymmetric World" — forest polynomials, geometric QSym via noncrossing partitions; slides not yet posted. Seung Jin Lee plenary (Tue July 14): q-weight multiplicities + KR crystals (arXiv:2412.20757). Notable: Lauve-Lazzeroni poster on species lift of r-QSym Hopf algebra; Pfannerer "Cyclic sieving via crystals + electrical networks" (arXiv:2607.14028). Zero DIII content. **Post-FPSAC arXiv wave expected July 18-25** — watch math.CO/math.QA daily.
- Mittag-Leffler workshop "Solvable Lattice Models, Rep Theory of Quantum Groups, and Algebraic Combinatorics," July 27-31, 2026 — **Schedule LIVE (Browse 94, July 18).** Schilling, Scrimshaw, Knutson, Corteel ALL confirmed. Talk titles TBA — check July 24-25. No DIII content announced. Bergeron FPSAC plenary slides NOT posted (check bergeron.math.yorku.ca early August).

## Expository resources (Browse 24 — new)
- **BIMSA course: "Introduction to Quantum Symmetric Pairs"** — Bart Vlaar, Oct–Nov 2025. Public videos + lecture notes. URL: https://www.bimsa.cn/research_detail/Inttoquasympai.html. Best new expository QSP resource since Kolb's survey.
- **ICMS Edinburgh Oct 2025** — Kolb on Letzter map + Jian-Rong Li on q-characters for affine QSP. Slides may be at icms.ac.uk.

## nLab updates (Browse 18)
- **quantum symmetric pair** page now exists: ncatlab.org/nlab/show/quantum+symmetric+pair (created Oct 11, 2024; real content on right coideal subalgebras + Letzter citation)
- **coideal subalgebra** standalone page still missing (only bare "coideal" page from 2019)

## Key papers to read next (flagged 2026-05-06)

### Already read (this session):
- arXiv:2601.22926 (Kim-Searles 2026) — type B 0-Hecke poset modules → QSym^B; NSym^B absent (READ)
- arXiv:1911.08732 (Morse-Pan-Poh-Schilling 2020) — ★-crystal on 0-Hecke monoid, K-theoretic (READ)

### Previously read:
- arXiv:2601.13324 (Almousa-Lu 2026) — Koszulness of H_0 tower (READ, close-read day 2)
- arXiv:2412.20757 (Choi-Kim-Lee 2025) — energy on KR crystals → Lusztig multiplicities (READ, close-read day 2)
- arXiv:2503.14782 (Brauner-Corteel-Daugherty-Schilling 2025) — crystal skeleton axioms (READ, session 1)

### Priority for next session (Browse 59 additions — 2026-06-13):

- **arXiv:2603.16698 (Azenhas Mar 2026)** "Recording tableaux of quantum LR map" ✅ **FULLY READ (Browse 59).** OQ-AZENHAS-INEQUALITIES-BDI RESOLVED POSITIVE. AII has ~2(n-1) walls; BDI has 3 walls for all n. Structural contrast belongs in v4 §3.
- **arXiv:2604.25856 (Azenhas Apr 2026)** "Slack data" ✅ READ. Slack = gap invariant of recording tableau. Technical machinery for 2603.16698. No BDI content.
- **arXiv:2505.21738 (Muniz May 2025)** "Symplectic Branching through Crystals" — alternative proof of Naito-Sagaki via Sundaram model. Read intro: is Sundaram model portable to BDI? ⭐⭐
- **arXiv:2510.17655 (Meereboer Oct 2025)** "Iota crystal theory for 1-dim modules" — foundational for Meereboer-Kolb branching law for QSP. Skim intro. ⭐⭐
- **arXiv:2510.24451 (Jang-Kwon-Uruno Oct 2025)** "Crystal base of the negative half of quantum orthosymplectic superalgebra" (55pp). Orthosymplectic Burge correspondence. HIGH for OQ-IQUANTUM-RSK-LIFT. ⭐⭐
- **math/0107011 (Knutson-Tao-Woodward)** "The honeycomb model" / facet machinery. Azenhas uses this for AII walls; check if BDI analogue exists. NEW OQ-KTW-FACETS-BDI. ⭐⭐
- **arXiv:2507.12328 (Salmasian-Savage-Shen 2025)** "Disoriented skein and iquantum Brauer categories" (Forum Math. Sigma). Categorical iquantum. Check BDI coverage. ⭐
- **arXiv:2601.19670 (Song-Zhang Jan 2026)** QSP at roots of unity. Skim for BDI structure.
- **arXiv:2412.20757 (Choi-Kim-Lee 2024)** KR crystals → Lusztig q-weight multiplicities types B/C. FPSAC 2026 invited talk.
- **arXiv:2504.12106 (Heo Apr 2025)** Bicrystal B(∞) sliding diamond rule. Low priority until Watanabe-Hoshino drops.
- **arXiv:2603.06132 (Kolb Mar 2026)** Star products on quantum symmetric pairs — skim for BDI content.
- **arXiv:2507.12328 (Salmasian-Savage-Shen 2025)** "Disoriented skein + iquantum Brauer categories" — published FMS. Check if BDI type appears explicitly.

### Priority for next session (Browse 55 additions — HIGH, 2026-06-11):
- **arXiv:2606.00679 (Stern May 2026)** "AHA! RSK" — RSK = JM eigenspace spectral decomposition in degenerate AHA; slide operators on regular representation of S_N are JdT. **Direct hit OQ-AHA-RSK.** CLOSE READ URGENTLY.
- **arXiv:2505.21738 (Muniz May 2025)** "Symplectic Branching through Crystals" — GL_{2n}→Sp_{2n} branching via crystal bijection with Sundaram model. AII pair, crystal-explicit. **For OQ-CRYSTAL-FIBER-MATCH: enumerate fiber components at n=2.**
- **arXiv:2312.11295 (Frohmader 2023/pub. 2025)** — GL(2n)↓Sp(2n) Kostant-Rallis K-type multiplicities on K-nilpotent cones. Exact structural analogue. **For OQ-KOSTANT-RALLIS-MATCH: compare tables with stratum vector (1,5,9,9,13,17,22,26).**
- **arXiv:2505.06941 (Andrews et al. May 2025)** "When are Hopf algebras determined by integer sequences?" INVERTi test. **Run INVERTi(1,5,9,9,13,17,22,26) immediately (5-min SageMath).**
- **arXiv:2606.02972 (Schilling et al. June 2026)** "Uncrowding the 5-vertex model: RSK and crystal structures" — fresh paper; likely related to IMJ-PRG course. READ.
- **arXiv:2305.01571 (2025, Trans. AMS)** "Horospherical stacks and stacky coloured fans" — extends Geraschenko-Satriano to horospherical varieties (includes flag varieties). **OQ-HOROSPHERICAL-STACK-PI3: is π̃₃' a horospherical stack?** SKIM.
- **arXiv:2407.20960 (Lusztig Jul 2024)** "Strata and almost special representations" — strata of reductive groups ↔ almost-special Weyl group representations. Check if 8-stratum decomposition fits. SKIM.

### Priority for next session (Browse 54 additions — HIGH):
- **arXiv:2303.11653 (Paradan 2023/v2 2024)** — O'Shea-Sjamaar and AII/BDI eigenvalue/singular value cones; CLOSEST EXISTING PAPER to Rick's setup; v2 adds "matrix identities" for cone structure. READ for v4 §3.
- **arXiv:2502.07270 (Naito-Suzuki-Watanabe Feb 2025)** — Naito-Sagaki conjecture (AII→CI branching) proved via iquantum crystals; STRUCTURAL ANALOGUE of Rick's AII→BDI problem. READ for OQ-NAITOSAGAKI-BDI.
- **arXiv:2601.00524 (Chen-Lu-Pan-Ruan-Wang Jan 2026)** — dual canonical bases ALL finite types via iHopf; covers type BDI. READ for algebraic context of BDI cone.
- **arXiv:2606.00679 (Stern June 2026)** "AHA! RSK" — RSK in degenerate AHA using KN crystals; cites Steinberg 1988 (RSK + symmetric pairs). READ for OQ-AHA-RSK thread.
- **arXiv:2601.19670 (Song-Zhang 2026)** — QSP at roots of unity (cites Watanabe 2407.07280); NOT YET in notes. SKIM.

### Priority for next session:
- **arXiv:2509.00853 (Watanabe Aug 2025)** — Berele row-insertion and QSP; AII RSK capstone; direct template for OQ-BDIqLR — **URGENT P_DEEP READ, BEFORE v3 DRAFT**
- **arXiv:2601.06930 (Azenhas Jan 2026)** — Symplectic left companion + Kwon property; Lecouvey-Lenart resolved; paper #0 in AII quantum LR series — READ AFTER 2509.00853
- arXiv:2404.04961 (Defant-Searles CJM 2026) — type B 0-Hecke, domino tableaux, type-B 0-Hecke-Clifford; technical foundation for Kim-Searles — MUST READ BEFORE NSym^B work
- arXiv:2308.10456 (Choi-Kim-Oh 2023) — current hub paper; poset modules → QSym Hopf; 7 citations — READ
- arXiv:2409.02341 (Lee 2024) — SSOT + type C energy formula; companion to Choi-Kim-Lee — READ AS PAIR

### Must read next (flagged 2026-05-07):
- Bowman-Norton-Simental (JIMJ 2024) — BGG resolutions in cyclotomic Hecke; potential bridge paper — FIND ARXIV ID
- arXiv:2412.16820 (Dec 2024) — Kostant alternation sets are order ideals in weak Bruhat; structural input for Aug~ involution
- arXiv:1306.2980 (Marberg 2014) — 4 open positivity conjectures for twisted-involution KL type B/D; may follow from (SA)
- ~~arXiv:2601.00687 (Fujita-Qin 2026)~~ — DEPRIORITIZED. Quantum *loop* algebras (Hernandez conjecture), NOT iquantum groups. Type B covered implicitly via folding but peripheral to BDI program.
- arXiv:0712.1324 — Koszul DG algebras and BGG correspondence; derived BGG dictionary

### Must read next (flagged 2026-05-07 Browse 4):
- Torres 2023, "The Virtual Cactus Group and Littelmann Paths" — best type-general cactus extension; does it cover type B? does it agree with Aug~? ⭐⭐⭐
- Gossow-Yacobi 2023, "On the action of the Weyl group on canonical bases" — canonical bases ↔ cactus group; lift to bigraded Verma? ⭐⭐⭐
- Rouquier-White arXiv:2408.16922 (2024) — abstract cactus morphism for ALL Coxeter types to J-ring; what does it say for type B (hyperoctahedral)? ⭐⭐
- Shen-Wang arXiv:2108.00630 (Adv. Math. 2023) — iSchur duality; iquantum group AIII ↔ type B Hecke; quasi-parabolic KL positivity; closest paper to type-B KL positivity ⭐⭐
- Alqady-Stroinski 2025 — coboundary Temperley-Lieb category for sl2-crystals; type B analog?
- Yuan Chai arXiv:2604.21731 (2026) — twisted KL conjecture p-adic GL_n (geometric proof; informational)

### New additions from Browse 86 (2026-07-13):
- **arXiv:2607.07870 (Zemel, July 2026)** NEW — Antipodes of q-QSym and NCQSym. S(F_α^{(q)}) = (−1)^n q^{inv(α^t)} F̃_{α^t}^{(q)} for braided QSym. The q^{inv} weight may connect to Hecke deformation of descent algebra (OQ-ZEMEL-HECKE-BRIDGE). Path 1 + Path 3 bridge candidate.
- **arXiv:2406.01166 (Grinberg-Vassilieva, June 2024)** — q-fundamental QSym functions interpolating Gessel ↔ Stembridge, giving QSym expansion of Hall-Littlewood at t = -q. Crystal-QSym bridge via HL. Not previously tracked.
- **arXiv:2404.04512 (Orellana-Saliola-Schilling-Zabrocki, 2024)** EMERGING HUB — "From QSym to Schur expansions with applications to symmetric chain decompositions and plethysm." 9 citations; being cited by plethysm community (Gutiérrez), combinatorics (Pak-Panova-Swanson), and quantum complexity (Christandl et al.). The dominant-term QSym→Schur technique in this paper is foundational infrastructure for computing M_j. FPSAC 2026 follow-up: **Castellano-Orellana-Zabrocki** poster "Transition matrices for character bases of the symmetric group" — those matrices may give M_j directly as entries. Read 2404.04512 soon.
- **Lam-Lauve-Sottile arXiv:0908.3714 (2009) — CONFIRMED DORMANT.** Zero citations from 2024-2026. The Hopf-coproduct → skew LR-rule thread (Path 4) is wide open. Rick's M_j programme implicitly builds this Hopf ↔ LR ↔ crystal bridge. A short paper making it explicit would be uncompeted.
- **Aquilino-Reischuk arXiv:1503.09152 + 1503.05108 (2017-18)** NEW — strict polynomial functors, internal ⊠ product, Schur functor monoidal → Kronecker. CLOSEST categorical framework to M_j structure. M_j = Hom_{S_n}(V_λ, GL-rep of outer product) is representable on Pol_n. OQ-AQUILINO-REISCHUK-MJ: Route VI candidate for M_j categorification.
- **Allouche-Shallit p-regular sequences** — OQ-BETA-PRIME-4-REGULAR: is β(c) 4-regular? If yes, D(c) digit-sum formula derives structurally. Test in Sage: split β(c) into 4 arithmetic progressions, check Berlekamp-Massey linear recurrence.
- **Hsiao-Petersen arXiv:math/0610976 (2006)** — BQSym Hopf algebra; BSym = NSym^B as dual. OQ-NSYMB-STRUCTURE: freeness + ribbon basis + antipode all open.
- **Lee arXiv:2506.06951 (June 2025)** — type C RSK complete (King tableaux + SSOT). Type D RSK Q-tableau **explicitly open** (noted by Heo-Kwon 2008.05093). Type D needs oscillating tableaux for so(2N)→so(2N-2) branching including spinors s+/s−.

### On radar (not yet prioritized):
- **arXiv:2507.12328 (Salmasian-Savage-Shen 2025)** ⭐⭐⭐ **HIGH — post-v3 priority read** — "The disoriented skein and iquantum Brauer categories." Iquantum groups + Brauer categorical machinery. Thread-3-adjacent (BDI RSK infrastructure). **Browse 43.**
- **arXiv:2605.09589 (Luo-Su-Xu May 2026)** ⭐⭐⭐ **HIGH** — "Affine iquantum groups and Steinberg varieties of type C, II." Geometric realization quasi-split AIII via equivariant K-groups. Adjacent to Lu-Pan algebraic-roof. **Browse 43.**
- **arXiv:2510.12118 (Shen-Su-Xiong 2025)** ⭐⭐ **MEDIUM-HIGH** — "Shifted Twisted Yangians via Coulomb Branches." 6 cites, fastest-moving adjacent paper. **Browse 43.**
- arXiv:2412.08413 (Choi-Nam-Oh 2024) — projective covers / injective hulls for parabolic descent Bruhat intervals
- arXiv:2404.04246 (Barkley-Gaetz 2024) — three variants of CIC are equivalent (Selecta Math. 2025)
- arXiv:2412.10256 (Barkley-Gaetz Dec 2024) — BBDVW for lower intervals [e,v] (IMRN 2026)
- arXiv:2504.20622 (Hao-Zhu 2025) — ParQSym from partition diagrams; new CHA construction
- arXiv:2511.05140 (2024) — non-homogeneous Koszul duality; q as curvature in dual curved dg-algebra
- arXiv:2511.18518 (Riche-Situ Nov 2025) — equivariant Koszul duality, modular category O, periodic KL
- arXiv:2601.15426 (Mills Jan 2026) — isotropic meta-KL, type D Hecke category Ext-quiver ⭐ (P3)
- arXiv:2604.24454 (Young-Hun Kim Apr 2026) — 0-Hecke modules → Grassmannian K-theory (genomic Schur)
- arXiv:2604.24903 (Bergeron-Gagnon-Spink-Tewari Apr 2026) — Quasisymmetric Grassmannian via positroid varieties
- arXiv:2602.19508 (Bhattacharya-Mishra-Srivastava Feb 2026) — KL matrix factors into nonneg pieces

---

### Browse 71 additions (2026-06-19) — DIII RSK landscape

**TYPE D BK NOW COMPLETE:** Svyatnyy 2605.00514 resolves Gutiérrez's open type D BK problem via spinor crystal B_S = B_{Λ_{n-1}} ⊕ B_{Λ_n}, three cases (Thms A/B/C). OQ-GUTIERREZ-TYPE-D-BK → **CLOSED**.

**HIGH PRIORITY reads (DIII RSK prerequisite):**
- **Lecouvey (2002)** "Schensted-Type Correspondences and Plactic Monoids for Types B_n and D_n" — 52 citations; ONLY paper in entire citation survey engaging type D combinatorics; He-Tubbenhauer cite it; potentially MISSING from Rick's bibliography. Contains type D Schensted correspondence. **READ IMMEDIATELY — OQ-LECOUVEY-D-PLACTIC.**
- **Jagenteufel 1902.03843** "Vacillating tableaux for SO(2k+1)" — Sundaram-type bijection for odd orthogonal; even case SO(2n) EXPLICITLY OPEN. Direct structural template for DIII RSK. **OQ-JAGENTEUFEL-DIII (HIGH).**
- **Kobayashi-Matsumura-Sugimoto 2601.17603** "Symmetry of the generating function of semistandard oscillating tableaux" — new companion in K-M type C RSK series (0 external citers); type D analogue needed.
- **RETRY Azenhas 2604.25856** — HTML 404 in Browse 71; PDF not extractable. Try Playwright or direct PDF download.

**NEW OQ-SQRTCRYSTAL-DIII (MEDIUM):** Marberg-Tong-Yu square root crystals have (φ_i - ε_i)/2 = wt_i - wt_{i+1} structure. D_n spinors have half-integer weights. Structural parallel: a "square root D_n crystal" might encode DIII RSK K-theoretically (characters = symmetric Grothendieck polynomials).

**DIII component count (Browse 71 upgrade):** Five components: alg foundation ✓, Q-symbol ✓ (Svyatnyy), BK involution ✓ (Svyatnyy), **P-side ✗**, **inverse RSK / slack data ✗**.

**New papers to watch:**
- **Luo-Xu-Yang 2606.15722** — K-theoretic affine iquantum groups of type AIII with three parameters; verify not already logged from Browse 68 notes.
- He-Tubbenhauer 2606.02249 — crystal category presentations; only sl_2/sl_3/sp_4/G_2 covered; type D_n ABSENT; methodology (cactus crossings + atoms) IS the right framework to eventually extend to type D.
- Kwon 1908.11041 "Flagged LR Tableaux and Branching Rules for Classical Groups" — spinor model + separation algorithm for type D crystals; check if relevant to DIII P-side.
- Carlini-Shen arXiv:2305.12290 (2024, JPAA) — quasi-parabolic KL bases type B; adjacent to twisted involutions

### Found 2026-06-06 (browse cycle 47 — sixth early-fire, T-2d pre-Q-SPHERE, same-day second browse):

- **NULL #47.** All Q-SPHERE preprints still absent (expected T-2d). All citation counts flat. bi-icrystal has zero mathematical web presence — confirmed new coinage appearing for the first time at Q-SPHERE June 9. Harness-adaptive hypothesis → **FORMAL CALIBRATION** (6/6 consecutive early-fires before June 13).
- **arXiv:2604.25856 (Azenhas et al., April 2026) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — AII RSK sequel paper. Continuation of arXiv:2603.16698 (recording tableaux / linear inequalities). Found via citation trail (generates both self-cites of 2603.16698). P_PARK slot #5 = TWO-PAPER BLOCK: 2603.16698 + 2604.25856. Read as pair post-v3-arXiv.
- **arXiv:2605.20383 (Huang-Zhang, May 2026) NEW TO FEEDS** ⭐⭐ **MEDIUM-HIGH** — Dual affine RSK. Adjacent to the three-RSK-threads framework. Not directly Thread 3 (BDI/coideal) but monitors surrounding dual-affine territory.
- **arXiv:2504.14042 (Li-Przezdziecki, April 2026) NEW TO FEEDS** ⭐⭐ **MEDIUM-HIGH** — "Boundary q-characters for split affine quantum symmetric pairs." q-character theory for split affine coideal subalgebras. Directly adjacent to the QSP/affine programme (Vlaar, Appel).
- **arXiv:2602.20861 (Guilhot-Poulain d'Andecy, Feb 2026) NEW TO FEEDS** ⭐⭐ **MEDIUM** — Hecke algebra paper, Path 3 territory.
- **Mao Hoshino — PROFILE ESTABLISHED (Browse 47).** RIKEN iTHEMS (Wako). PhD from Kawahigashi group (University of Tokyo). C*-algebras, von Neumann algebras, operator algebras. Personal site: mao-hoshino.github.io. **Watanabe's Q-SPHERE collaborator on bi-icrystals.** Operator-algebra bridge: same community as Neshveyev-Tuset-Yamashita and De Commer. Add to people-to-watch.

### Found 2026-06-05 (browse cycle 44 — third early-fire, T-3d pre-Q-SPHERE):

- **NULL #44.** Watanabe 2407.07280 still 4 citers (unchanged). All 4 citers = Q-SPHERE participants (Song-Zhang 2601.19670, Song 2512.01398, Meereboer 2510.17655, Kolb-Stephens 2407.15538). Meereboer-Kolb joint preprint NOT on arXiv. Citation counts stable across all watches (Lusztig=0, Song-Zhang=0, Meereboer=0, Salmasian-Savage-Shen=1, Kobayashi=1). Third consecutive early-fire (Browse 42+43+44 all pre-June-13); calibration thread started.
- **⚠️ SS ID CALIBRATION — Watanabe 2110.07177:** SS ID `f51b027ffdc9fd0471c3af3ff5e8c5b91d14e27f` (banked Browse 41) resolves to "Crystal Bases of Modified iquantum Groups of Certain Quasi-Split Types" (different Watanabe paper, 2023, 12 cites) — NOT 2110.07177. The "NULL #XX" streak may have been tracking the wrong paper. Actual 2110.07177 citer count unverified. Verify via Google Scholar or arXiv abstract page post-Q-SPHERE.
- **arXiv:2603.18264 (Salmasian-Savage-Shen, March 2026) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "Classifying submodules over monoidal categories." Sequel to 2507.12328. Classifies submodules of disoriented skein category via twisted cylinder twist tied to QSP reflection equation. iquantum Brauer cluster is now 3-paper arc: Shen-Wang 2408.02874 → Salmasian-Savage-Shen 2507.12328 → 2603.18264. Thread-3 BDI RSK categorical infrastructure solidifying; BDI RSK paper still the missing element.
- **arXiv:2603.16698 (Azenhas, March 2026, revised June 1 2026) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "Recording tableaux in the quantum LR map / k-highest weight tableaux." Proves surjectivity of Watanabe's AII RSK map; constructs inverse; characterizes k-highest weight SSYT by **linear inequalities**. Template paper: if Rick's carry polytope facets (Theorems F+G) correspond to Azenhas's linear inequalities for AII RSK, this is a Path 4 ↔ v3 bridge at the deepest level. First non-Azenhas citer of Watanabe 2509 is Rick v3 — this 2026 Azenhas paper continues her AII RSK program in the direction closest to Rick's. Post-v3 read.
- **arXiv:2508.12041 (Wang-Zhang, Aug 2025) NEW TO FEEDS** ⭐⭐ **MEDIUM-HIGH** — "Relative braid group symmetries on modified iquantum groups and their modules." Braid group actions on modified iquantum groups. 3 cites. Core reference in Song-Zhang 2601.19670. Wang-Weinan Zhang paper (same Zhang as Math. Z. 2026 iquantum Howe duality). Part of the iquantum group symmetry infrastructure.
- **arXiv:2512.19034 (Marberg, Dec 2025) NEW TO FEEDS** ⭐⭐ **MEDIUM** — "Brion atoms for classical types B, C, D." Marberg's 2025 program shifted K-theoretically; 4 open conjectures from 1306.2980 still unguarded. OQ-ZHANG-MARBERG P=35% updated: Marberg's active program is K-theoretic crystals + Brion atoms, NOT directly attacking twisted-involution KL positivity.
- **arXiv:2506.12868 (June 2025, older) NEW TO FEEDS** ⭐⭐ **MEDIUM — OQ-HUANG-B candidate** — "Peak Algebra in Noncommuting Variables." NC-Pi as Hopf algebra with Schur Q-functions in NC variables. Best current candidate for NSym^B dual to QSym^B (Kim-Searles 2601.22926). Whether full combinatorial Hopf axioms hold = remaining question.
- **arXiv:2506.06951 (Kobayashi-Matsumura, June 2025, older) NEW TO FEEDS** ⭐⭐ **MEDIUM** — "Type C RSK for King tableaux with Berele insertion." King tableaux + semistandard oscillating tableaux as Q-symbol for type C. Kobayashi = Q-SPHERE speaker. RSK thread map: AII ✓ (Watanabe 2509) / AIII ✓ (Muniz 2505) / type C ✓ (this) / BDI = remaining gap.
- **Kolb-Stephens 2407.15538 (July 2024) IDENTIFIED** — "Very non-standard quantum so(2N-1)." One of the 4 citers of Watanabe 2407.07280. Kolb-adjacent. Low relevance to BDI crystal program.

### Found 2026-07-09 (Browse 78):

- **arXiv:2607.03966 (Gerber-Ion-Lecouvey-Lenart, July 4, 2026) NEW TO FEEDS** ⭐⭐⭐⭐ **HIGH** — "Quantized Howe-type dualities via Koornwinder polynomials and the X=K phenomenon." Proves X=K for KR column crystal 1D-sums in most classical affine types via Koornwinder polynomial dual Cauchy. **Explicitly excludes B_n^(1) and D_n^(1).** Lecouvey co-author. Confirms type-D X=K is known open at the highest level. OQ-GERBER-LECOUVEY-D-XK. Upstream of McDonough-Pylyavskyy-Wang KR DEGs (2510.24490).

- **arXiv:2602.22325 (Kannan-Song, Feb 2026) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "Pólya enumeration, wreath product symmetric functions, and moduli spaces of curves." FPSAC 2026 poster. Develops Λ^[2] = Grothendieck ring of polynomial functors on symmetric sequences; action on Sym via Adams + power-sum skewing. **Direct hit for M_j structural proof:** M_j = Frobenius-char of Ind_{S_2 ≀ S_j × S_{n-2j}}^{S_n} lives in Λ^[2]. OQ-MJ-LAMBDA2.

- **arXiv:2603.19069 (March 2026) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "Pascal, Catalan, Motzkin triangles and tensor product multiplicities." Motzkin numbers as tensor product multiplicities in quantum groups. OQ-MOTZKIN-MJ-CENTRALIZER: K_{μ^T,(2^j)} = Motzkin centralizer dims for U_q(sl_2) on (V_1 ⊕ V_2)^{⊗j}? See also Benkart-Halverson 1106.5277 (Motzkin algebra).

- **arXiv:2512.19045 (Marberg, Dec 2025) UPGRADED PRIORITY** ⭐⭐⭐ **HIGH** — "Classical double Grothendieck transitions." MISSED until Browse 78 (same submission date as 2512.19034). K-type-D Stanley functions expand positively in K-Schur P/Q-functions. K-theoretic DIII RSK program: this is the K-level version of the atom expansion question. Was in feeds at ⭐ LOW from Browse 17 — now upgraded.

- **arXiv:2406.09057 (Du-Li-Zhao, 2024) NEW TO FEEDS** ⭐⭐ **MEDIUM-HIGH** — "q-Schur algebras of type D and Schur-Weyl-Hecke duality." Journal of Algebra 2025. Resolves 30-year open problem: Schur-Weyl-Hecke duality for type D. Part I only. Rick's SEED Q3 = Hopf-algebraic formulation of this functor. OQ-DU-LI-ZHAO-HOPF.

- **arXiv:2510.24490 (McDonough-Pylyavskyy-Wang, Oct 2025) UPGRADED** ⭐⭐⭐ **HIGH (upgraded from LOW)** — KR dual equivalence graphs, FPSAC 2026 poster. Upgraded because: Gerber-Ion-Lecouvey-Lenart 2607.03966 explicitly leaves D_n^(1) X=K open; KR DEGs = natural tool to close this gap. OQ-KR-DEG-TYPE-D.

- **Marberg 2512.19034 v2 (July 1, 2026) MAJOR REVISION** — "Brion atoms for classical types." §8 = type DIII atom proofs; §9 = involution Schubert polynomials + 7 open DIII conjectures. "Many corrections" may have changed atom description. Bingham at FPSAC 2026 (July 13-17) — ask him whether DIII clans = fpf-involution atoms. OQ-MARBERG-V2-ATOM-CORRECTION, OQ-THREE-Q-DESCRIPTIONS.

- **All 5 DIII sentinels still 0 citations.** Window confirmed open. Browses 73-78 = sixth consecutive zero sweep.

- **Anne Schilling Paris slides available:** https://www.math.ucdavis.edu/~anne/talk-Paris2026.pdf — "Crystals and Symmetric Functions," IMJ-PRG June 2026. Fetch next browse.

### Found 2026-06-18 (Browse 70):

- **arXiv:2311.10659 (Gutiérrez, Nov 2023) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "Bender-Knuth involutions for types B and C." Types B and C BK involution algorithms, fully explicit. **Type D explicitly stated as open.** Surfaced from Kobayashi-Matsumura 2506.06951 references. Svyatnyy 2605.00514 partially answers type D for short SSYT; Gutiérrez is the baseline. **OQ-GUTIERREZ-TYPE-D-BK (NEW HIGH).** Read alongside Svyatnyy.

- **arXiv:2606.17525 (Imamura-Mucciconi-Sasamoto-Scrimshaw, June 2026) NEW TO FEEDS** ⭐⭐ **MEDIUM** — "Skew column RSK dynamics and the box-ball system." RSK dynamics recast as box-ball system via two commuting affine D_n^{(1)} crystal structures on skew tableaux. Template for type D RSK. Scrimshaw is Mittag-Leffler participant (July 27-31).

- **Azenhas 2604.25856 RE-READ FLAG:** Previously read (Browse ~59) with note "no BDI content." Now HIGHLY RELEVANT — formally defines slack data and proves LR^{AII−1} formula. Re-read with DIII lens: DIII slack conditions (spinor parity + D_n depth + D_n row dominance) are the key derivation target.

- **Citation audit (Browse 70):** AII RSK cluster (Azenhas 2603.16698 + 2601.06930 + Watanabe 2509.00853) has ZERO external citers. Svyatnyy 2504.14344 + 2605.00514 both have ZERO citations. **No external competition on DIII RSK confirmed.** Window: ~12-18 months.

### Found 2026-06-04 (browse cycle 43 — second run, early-fired T-4 pre-Q-SPHERE):

- **NULL #43.** Watanabe 2110.07177 still 12 citers. 43rd consecutive null. Plateau holding. Active watch now: **Watanabe 2407.07280** ("Integrable modules over QSP coideal subalgebras", July 2024/revised May 2025, 4 cites) — confirmed upstream anchor for BOTH Song-Zhang roots-of-unity extension AND Meereboer-Kolb branching. Discovery-layer-moat: both Q-SPHERE June 9 talks (Kolb-Meereboer 09:00 + Song 14:00) draw from 2407.07280 in independent directions.
- **arXiv:2507.12328 (Salmasian-Savage-Shen, Jul 2025) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "The disoriented skein and iquantum Brauer categories." Explicitly combines iquantum groups (coideal subalgebra machinery) with Brauer categorical techniques. Closest existing paper to Thread 3 (BDI RSK) infrastructure: the categorical home for JM/coideal intersection. Surfaced from Shen-Wang 2408.02874 citation trail. Post-v3 priority read.
- **arXiv:2510.12118 (Shen-Su-Xiong, Oct 2025) NEW TO FEEDS** ⭐⭐ **MEDIUM-HIGH** — "Quivers with Involutions and Shifted Twisted Yangians via Coulomb Branches." Coideal subalgebras → Coulomb branch geometry. 6 cites = fastest-moving adjacent paper in this sweep. Shen (Wang school) + Su (geometric/Yangian) collaboration.
- **arXiv:2605.09589 (Luo-Su-Xu, May 2026) NEW TO FEEDS** ⭐⭐⭐ **HIGH** — "Affine iquantum groups and Steinberg varieties of type C, II." Geometric realization of quasi-split iquantum groups of type AIII_{2n}^{tau} via equivariant K-groups of Steinberg varieties of type C; type-D Steinberg for AIII_{2n-1} in appendix. Adjacent to Lu-Pan algebraic-roof quartet.
- **Thread 3 (BDI RSK) confirmed open.** AII = Watanabe 2509.00853 (done). AIII branching = 2505.21738 (done). BDI (GL_{2n+1}/O_{2n+1}) = specific visible gap, one remaining classical symmetric pair type without QSP-RSK.
- **Song-Zhang 2601.19670: 0 citers, Q-SPHERE engagement target.** 47-page roots-of-unity paper. Reference stack includes Watanabe 2407.07280. Song presents June 9 14:00. Unclaimed territory.
- **FPSAC 2026 update:** Marberg-Tong-Yu presenting 2501.16640 as TALK (not just poster). Seung Jin Lee invited talk on type-B/C KR crystals + q-weight multiplicities (joint Choi-Kim). Short talk list still unpublished.
- **Milionis 2512.17458 — BMW center = Wheel Laurent polynomials.** OV spectral approach for BMW. Zero QSP crossover. Open question: BMW Wheel Laurent polynomial / iquantum Brauer center analog.

### Found 2026-06-04 (browse cycle 42 — new):

- **NULL #42.** Watanabe 2110.07177 still 12 (~10 unique) SS citers. 42nd consecutive BDI null. All secondary watches frozen (Lusztig=0, Meereboer 2510.17655=0, Zhang 2412.07810=0, Chen-Lu=0, Marberg 1306.2980=4 all-time/0 new).
- **arXiv:2502.19232 (Meereboer, Feb 2025) content confirmed:** "Quantum spherical functions of type χ as Macdonald-Koornwinder polynomials." Weyl-group-invariant χ-spherical functions of Hermitian QSPs = Macdonald-Koornwinder polynomials for reduced root systems / type AIII_a. Meereboer's harmonic-analysis program; **NOT the Meereboer-Kolb joint branching paper.** Both Meereboer preprints now identified. Joint Q-SPHERE result = new work.
- **YUNCKEN CORRECTION (Browse 42):** arXiv:2508.01160 is **NOT a Yuncken paper** — it is Das-Dey-Pal, "Quantized Weyl algebras at roots of unity" proving the Matassa-Yuncken conjecture. Yuncken's Q-SPHERE talk paper is arXiv:2208.13201 (Matassa-Yuncken, Crelles 2023) only. Corrected in events section and Browse-42 target list.
- **Song-Zhang arXiv:2601.19670 Q-SPHERE CONFIRMATION:** Already in feeds (Browse 12 with ICMS slides detail). Confirmed as Song's Q-SPHERE June 9 14:00 talk paper. θ-twisted conjugacy class parametrization of irreps; Weinan Zhang (AIII/type B Hecke, Math. Z. 2026) co-author.
- **arXiv:2312.16776 (Marberg-Tong, Dec 2023) NEW TO FEEDS** ⭐⭐ **MEDIUM-HIGH** — "K-theoretic crystal for shifted tableaux via square root operators." Extends Marberg's square root crystal program to the shifted tableau setting (K-theoretic / Grothendieck polynomial context). Adjacent infrastructure for OQ-LUSZTIG-MARBERG angle 3: Marberg-Tong 2312.16776 (shifted K-crystal ✓) + Marberg-Tong-Yu 2501.16640 (square root crystals, type A unshifted ✓) + Marberg-Scrimshaw 2306.00336 (P/Q-key via crystal ✓) → needed synthesis "shifted square root crystal" is still unwritten. Add to `zhang-lusztig-bridge-for-marberg.md` angle-3 infrastructure (dream).
- **Three-thread RSK convergence — Thread 2 role clarified:** Stern 2606.00679 ("AHA! RSK") explicitly identified as the template for BDI-RSK extension via type-B JM elements + type-B degenerate AHA. Thread 3 (QSP/BDI coideal) still missing from literature.
- **Browse 42 = DONE June 4 (harness-fired T-5 pre-Q-SPHERE).** Primary targets for post-Q-SPHERE Browse 43: Meereboer-Kolb preprint (if dropped around June 9), De Commer preprint (after June 12), Schilling IMJ-PRG notes (after June 18). Reading log at `reading/2026-06-04.md`.

### Found 2026-06-03 (browse cycle 40 — new):

- **arXiv:2606.02972 (Johnston-Nguyen-Schilling, ~June 1 2026)** ⭐⭐⭐ **HIGH** — "Uncrowding the 5-Vertex Model: RSK and Crystal Structures." Synthesizes uncrowding algorithm on set-valued tableaux with the 5-vertex lattice model (Motegi-Sakai / Buciumas-Scrimshaw-Weber); defines RSK and crystal structure directly on 5-vertex model states. Schilling on watch list. **Path 4 territory.** Fresh paper.
- **arXiv:2606.00679 (Stern, May 30 2026)** ⭐⭐⭐ **HIGH (upgraded from MEDIUM)** — "AHA! RSK." Spectral realization of RSK via degenerate affine Hecke algebra H_n + Jucys-Murphy elements. Type A only. Deep dive confirmed: no crystal/Hopf/iquantum content; spectral approach complementary to crystal theory. **New open question raised:** Can JM elements for BDI coideal subalgebra yield spectral RSK for (GL_{2n+1}, O_{2n+1})? Molev-type JM for Brauer algebras exist in literature. Post-v3 investigation.
- **arXiv:2606.03759 (Hudak, Chun-Ju Lai, ~June 3 2026)** ⭐⭐ **MEDIUM-HIGH** — "Cellularity of Hecke Algebras for Wreath Products." Hu algebra + Hecke type D_{2m} + bipartitions; Chun-Ju Lai is iquantum group community adjacent. Path 3.
- **arXiv:2606.02249 (He, Tubbenhauer, ~June 1 2026)** ⭐ **LOW-MEDIUM** — "Presentations for Categories of Crystals." Generators+relations for monoidal categories of crystals of fundamental crystals. Path 2 background.
- **arXiv:2606.02471 (Negutu, Wang, ~June 1 2026)** ⭐ **LOW-MEDIUM** — "Folding Shuffle Algebras and Twisted q-Characters." Proves Hernandez conjecture on equality of q-characters via folding. Path 2 adjacent.
- **arXiv:2606.03436 (Hao, Zhu, ~June 2 2026)** ⭐⭐ **MEDIUM** — "Chromatic Noncommutative Symmetric Function of Oriented Trees." Proves chromatic NSym can distinguish non-isomorphic oriented trees. NSym territory.
- **arXiv:2306.00336 (Marberg, Scrimshaw — June 2023, Algebras & Rep Theory 2025)** ⭐⭐⭐ **MEDIUM (NEW TO FEEDS)** — "Crystals for Shifted Key Polynomials." Crystal interpretations of P/Q-key polynomials; involution Schubert decomposition conjecture (crystal reformulation of twisted-KL positivity, arXiv:1306.2980) is **STILL OPEN.** Using Marberg's own square root crystal machinery (2501.16640) to prove the P/Q-key conjecture would likely resolve all 4 twisted-KL conjectures. **Best new attack angle for OQ-LUSZTIG-MARBERG.** Add to P_PARK read order (after Lusztig 2510.21499).
- **De Commer "KL theorem in type B" abstract framing:** type-A KL = Yang-Baxter equation; type-B KL = **reflection equation**; braided monoidal unitary category equivalence. Operator-algebra tradition (distinct from Bao-Wang/Rick's approach). No preprint; watch post-June 12. Details in `connections/q-sphere-meereboer-fourth-community-deadline.md`.
- **NULL #40 confirmed.** Watanabe 2110.07177 still at 12 SS citers. Forty consecutive browse cycles with zero new BDI citers.
- **Brundan-Wang-Webster 2505.22929 now at 2 citers:** Brundan-Savage-Webster self-cite + Salmasian-Savage-Shen 2507.12328 (already in feeds). No external attention yet.
- **Browse 40 = DONE June 3** (04:17 UTC). **Browse 41 = DONE June 3** (harness-fired same-day). Next: **Browse 42 = June 13+ post-Q-SPHERE.** Primary targets: Meereboer-Kolb preprint (if appeared post-June-9), De Commer preprint (post-June-12), Meereboer preprints 2511.23367 + 2502.19232 (**Browse 42: content confirmed** — see below; neither is the joint Kolb result), Schilling IMJ-PRG lecture notes (post-June-18). [Yuncken 2508.01160 target REMOVED — Browse 42: that paper is Das-Dey-Pal, not Yuncken.]

### Found 2026-06-03 (browse cycle 41 — new):

- **Q-SPHERE FULL PROGRAM RECOVERED (30 talks).** Browse 40 had 5 talks. See events section (updated Browse 41). New notable: Vlaar+Appel two-part (June 8), Wang/Song/Liu (June 9), Terwilliger (June 10), Yuncken (June 12).
- **Meereboer abstract confirmed:** derives branching law **via Watanabe's integrable modules** — Kolb+Watanabe bridge in joint result. TWO MORE Meereboer preprints not previously in feeds: arXiv:2511.23367 (with Schlösser, Nov 2025) and arXiv:2502.19232 (Feb 2026, solo). Check Browse 42.
- **arXiv:2408.02874 (Shen-Wang, Comm. Math. Phys. 2025)** ⭐⭐ **ON RADAR** — "Schur duality for q-Brauer and q-ortho-symplectic via quantum supersymmetric pairs." Brauer algebra (JM side) ↔ coideal/QSP. KEY infrastructure for OQ-BDI-SPECTRAL-RSK. Authors: Yaolong Shen, Weiqiang Wang.
- **arXiv:2512.17458 (Milionis, Dec 2024)** ⭐ **ON RADAR** — "Okounkov-Vershik approach for BMW algebras." JM spectral for type B/C (BMW); does not construct RSK. Closest existing type-B analog of Stern's spectral RSK.
- **Square root crystals 2501.16640 = strictly type A symmetric.** NOT involution/shifted/type B. Path 2306.00336 + 2501.16640 → 4 twisted-KL conjectures requires "shifted square root crystal" (not yet constructed). Third OQ-LUSZTIG-MARBERG attack angle less direct than Browse 40 suggested. Minimal targeted edit to `zhang-lusztig-bridge-for-marberg.md` (dream).
- **Marberg-Scrimshaw 2306.00336 = 0 SS citers** (published Algebras & Rep Theory 2025). No attack on P/Q-key conjecture in literature.
- **SS meta-note — Watanabe 2110.07177:** SS paper ID = `f51b027ffdc9fd0471c3af3ff5e8c5b91d14e27f` (DOI: 10.1007/s10468-023-10207-z). Use DOI-based query, not ARXIV: prefix (returns 404 on published papers).
- **NULL #41.** Watanabe 12 citers. Lusztig 2510.21499 = 0. Zhang 2412.07810 = 0. Bhattacharya 2602.19508 = 0.

### Found 2026-06-01 (browse cycle 37 — new):

- **Q-SPHERE Kolb abstract CONFIRMED (appeared between Browse 36 and 37, same day):** "Short star products for quantum symmetric pairs" = arXiv:2603.06132 (Kolb-Yakimov). His 50-min slot = existing published paper (algebraic infrastructure). Meereboer 10:15 = joint new result (no preprint). **All Q-SPHERE June-9 morning TBAs resolved.**
- **arXiv:2510.24490 (McDonough-Pylyavskyy-Wang, Oct 2025)** ⭐ **LOW** — "Kirillov-Reshetikhin dual equivalence graphs." FPSAC 2026 POSTER. Adjacent to Lee's KR crystals invited talk. Path 4 landscape.
- **arXiv:2503.17580 (Brauner-Commins-Grinberg-Saliola, March 2025)** ⭐ **LOW** — "The q-deformed random-to-random family in the Hecke algebra." FPSAC 2026 POSTER. **NOT 2503.14782** (crystal skeletons — different Brauner paper, different collaboration). Random-to-random q-deformation, Path 3 landscape, probability direction.
- **arXiv:2503.21215 (Yifeng Zhang, v4 April 2026)** ⭐⭐⭐ **NEW** — "Cell Classification of Gelfand S_n-graphs." **DIFFERENT paper from 2412.07810** (a-functions). Builds out molecular/cellular structure of Marberg's quasiparabolic Hecke framework in type A. v4 updated substantively. Add to OQ-LUSZTIG-MARBERG read order as second entry point alongside 2412.07810.
- **arXiv:2604.10816 (Lauve-Lazzeroni, April 2026)** ⭐ **LOW** — "Hopf substitutions in Species." Sequel to 2603.19494. Characterizes Hopf-monoid structure under species substitution. Type-A only. Off-thread for BDI/type-B/q=0.
- **arXiv:2510.27209 (Daugherty + 6 authors, 2025)** ⭐⭐ **ON RADAR** — "Tableaux algebra is Koszul and Cohen-Macaulay." Associated variety = toric degeneration of flag varieties; **injective crystal embeddings** as tool. Adjacent to crystal skeleton program.
- **Marberg FPSAC 2026 = TALK #13** (not just poster): "Grothendieck positivity for square root crystals." K-theory program has FPSAC talk-level profile. Further confirms four-sided dormancy on 1306.2980 twisted-involution KL.
- **Browse 37 = NULL #38.** All watches frozen. No new BDI/NSym^B/twisted-KL papers.

### Found 2026-06-01 (browse cycle 36 — new):

- **FPSAC 2026 proceedings page NOW ACCESSIBLE** — sites.math.washington.edu/fpsac2026/proceedings/. Short-talk PDFs live. Four relevant finds:
  - **McDonough et al. — "KR dual equivalence graphs"** — arXiv ID TBD. Adjacent to Lee's KR crystals invited talk.
  - **Brauner et al. — q-deformed Hecke** — likely connected to arXiv:2503.14782 (crystal skeleton). Confirm arXiv ID.
  - **Marberg et al. — square root crystals** — K-theoretic direction (Marberg K-Stanley program). NOT twisted-involution KL (1306.2980 conjectures remain unguarded).
  - **Lauve-Lazzeroni — r-QSym Hopf algebra** ⭐⭐ **UNFAMILIAR** — new QSym variant. "r-QSym" = unknown (ribbon? rank-restricted?). Path 1 territory. Lauve is on key researcher list. Confirm arXiv ID in Browse 37.
- **Browse 36 = NULL #37.** Watanabe 2110.07177 still 12 SS citers. All other watches frozen. Kolb abstract STILL TBA (7 days to Q-SPHERE). No Meereboer-Kolb preprint. No new papers in primary territory — all arXiv agent finds were already in feeds.

### Found 2026-05-31 (browse cycle 35 — new):

- **Watanabe arXiv:2502.07270 NOW IN PRINT** — Journal of Algebra 2026 (accepted Oct 2025). "A proof of the Naito–Sagaki conjecture via iquantum crystal bases." Type AII (GL_{2n}→Sp_{2n}). AII program fully settled at crystal level (two independent proofs: this + Muniz 2505.21738). BDI gap more conspicuous than ever.
- **NEW WATCH: Meereboer arXiv:2510.17655** — added to citation watch. First SS check (Browse 35) = 0 citers. Will track to see if Q-SPHERE talk generates attention.
- **Watanabe 2407.07280 reference chain confirmed:** Kolb-Stephens 2407.15538 appears in its reference list. Ancestry: Kolb 2012 → Bao-Wang 2016 → Watanabe AI 2021 → Watanabe integrable 2024 → Kolb-Meereboer Q-SPHERE result. Rick's v3 = combinatorial-1-dim layer of this chain.
- **Browse 35 ALL NULLS:** No new BDI crystal, no NSym^B Hopf, no twisted-involution KL positivity, no Meereboer-Kolb preprint, Kolb indico still TBA.

### Found 2026-05-31 (browse cycle 34 — new):

- **arXiv:2602.20861 (Guilhot, Poulain d'Andecy — Feb 2026)** ⭐ **LOW** — "KL bases of parabolic Hecke algebras and applications to Schur-Weyl duality." Two KL bases for type-A parabolic Hecke; RSK cell description; irreps classification; quantum GL(N) Schur-Weyl. Type A only. No twisted involutions, no type B/D. Path 3 landscape background.
- **arXiv:2506.00380 (Bergeron et al. — Jun 2025)** ⭐ **LOW** — "Convex Geometries via Hopf Monoids." Hopf monoid of convex geometries; quasisymmetric invariants. Confirms Bergeron's current program ≠ NSym^B or antipode. Path 1 landscape background.
- **arXiv:2506.00738 (Grinberg — May 2025, v2)** ⭐ **EXPOSITORY** — "An Introduction to Algebraic Combinatorics." 703-page graduate textbook. Type A foundational material. No type B NSym, no QSP, no 0-Hecke type B. Good stable reference for type-A foundational definitions.
- **arXiv:2506.08883 (Brauner et al. — Jun 2025)** ⭐ **LOW** — "Factorizations in Hecke algebras I." q-deformations of long-cycle factorizations; type-A Hecke algebra. Schilling-group adjacent (Brauner co-author). Low relevance to BDI or type-B territory.
- **Q-SPHERE BROWSE 34 UPDATE:** Meereboer June 9 10:15 abstract confirms "Joint work with Stefan Kolb." The two-slot (Kolb 09:00 invited + Meereboer 10:15 contributed) = one coordinated result: Grothendieck group of Watanabe's integrable B-modules ↔ classical K-group, via Kostant branching generalization. No preprint as of 2026-05-31. Kolb abstract STILL TBA. Check indico ~June 7.

### Found 2026-05-29 (browse cycle 31 — new):

- **arXiv:2602.19508 (Bhattacharya–Mishra–Srivastava — Feb 2026)** ⭐⭐⭐ **POST-V3 BACKGROUND** — "On factorization of matrix of Kazhdan-Lusztig polynomials." KL polynomial matrix factorizes into |S| nonneg matrices (one per Coxeter generator) using Grojnowski–Haiman hybrid bases TC^J; nonnegativity via parabolic restriction with geometric justification. **Standard KL matrices, NOT twisted-involution KL** — not a direct resolution of OQ-ZHANG-MARBERG. But the parabolic-restriction + hybrid-basis approach is the most structural positivity argument since Elias–Williamson, and the natural question is whether it extends to the twisted-involution setting. Post-v3 background read before attacking Marberg 1306.2980. P_PARK support material.
- **arXiv:2511.00713 (Spencer Daugherty + Campbell — Nov 2025)** ⭐ **LOW** — "Lexical tableaux and quasisymmetric functions." New QSym/NSym bases via lexical tableaux; Kostka-like coefficients. Type A only. Path 1 landscape background.
- **arXiv:2412.11013 (Spencer Daugherty — Dec 2024)** ⭐ **LOW** — "NSym in partially commutative variables." Seven-algebra diagram of Hopf morphisms. Type A only. Path 1 landscape.
- **arXiv:1008.1037 (Rains–Vazirani — 2010, 37 cites)** ⭐ **RADAR** — "Deformations of permutation representations of Coxeter groups." Appears in Zhang 2412.07810 reference list in quasiparabolic context. Check for type B relevance to OQ-ZHANG-MARBERG.
- **arXiv:2506.16953 (Jia Huang — June 2025)** ⭐ **LOW** — Projective indecomposable modules of 0-Hecke algebra with dimensions modulo primes, extending to other Coxeter groups. Counting, not Hopf structure. OQ-HUANG-B unaffected.
- **Browse 31 Q-SPHERE update:** Total talks now 30 (was 29). **Liu (Kolb Newcastle group) abstract posted:** "Representation Theory of very non-standard quantum so(2N)" (Tue Jun 9, 14:50) — Kolb–Stephens 2407.15538 territory; already in feeds. Kolb+Kobayashi still TBA. Check indico June 5–7.
- **Meereboer first name:** Community agent reports "Stein Meereboer." Feeds.md previously had no first name. **Verify on arXiv/indico before updating records formally.**

### Found 2026-05-29 (browse cycle 30 — new):

- **arXiv:2605.13578 (Lu-Pan — May 2026)** ⭐ **SCOPED** — "Quiver varieties and dual canonical bases." Survey of quiver-variety + Hall-algebra approach to dual canonical bases for quantum groups and iquantum groups. ADE (quasi-split) types ONLY — no split type, no type B_n BDI, no explicit $C_b$ discussion. **LOW priority for OQ-LU-PAN-EXPLICIT.** Confirms algebraic roof is sealed for ADE; BDI explicit $C_b$ remains completely out of scope for this community.
- **arXiv:2605.04043 (Ferroni-Larson — May 2026)** ⭐ **NEW** — "KL polynomials of Dowling geometries." Combinatorial formula for KL coefficients of Dowling geometries (type-B braid matroids, group-labelled partition lattices). Positivity confirmed. **LOW** — matroid KL ≠ representation-theoretic twisted-involution KL (Marberg 1306.2980). Not a route to OQ-ZHANG-MARBERG.
- **Q-SPHERE abstracts update (Browse 30):** Meereboer abstract NOW POSTED "Kostant's branching law for quantum symmetric pairs" (June 9 10:15); Watanabe abstract confirmed "Quantizations of coordinate algebras..." (June 9 11:20). Kolb (June 9 09:00) + Kobayashi (June 11 09:50) STILL TBA. Check indico June 5-7.
- **Schilling ICERM 2025 crystal-skeleton slides:** https://www.math.ucdavis.edu/~anne/talk-ICERM2025.pdf — slides on crystal skeleton axioms (arXiv:2503.14782, Brauner-Corteel-Daugherty-Schilling). Connects crystal combinatorics to QSym. Path 4 + seed question 4 direction. Read in future browse.
- **Browse 30 citation update:** Watanabe 2110.07177 = **31st consecutive BDI null** (12 SS entries, ~10 unique — 2 duplicate pairs identified: Jian-Luo-Wu arXiv+DOI, Watanabe-stability arXiv+journal). All other watched papers frozen: Zhang=0, Lusztig=0, Marberg=4 all-time, Chen-Lu=0, Lu-Pan I still 1 citer.

### Found 2026-05-28 (browse cycle 29 — new):

- **arXiv:2603.03381 (Lu-Pan — March 2026)** ⭐⭐⭐⭐ **NEW** — "Dual and double canonical bases of quantum groups." Posted 2026-03-05 (3 days after Part II). Proves Lu-Pan dual canonical bases = Berenstein-Greenstein double canonical bases via NKS quiver variety geometry. Resolves multiple Berenstein-Greenstein conjectures. **FOURTH paper in the algebraic roof above v3** (extends trilogy to quartet). Connection file updated.
- **Lu, Ruan, Haicheng Zhang — IMRN 2025 (DOI: 10.1093/imrn/rnaf297)** ⭐⭐⭐⭐ **NEW** — "Analogue of Feigin's Map on the iquantum groups of split type." No arXiv ID found. **Only citer of Lu-Pan I (2504.19073) as of Browse 29.** Split type = $\tau = \text{id}$ = BDI territory for $B_n$. Feigin's map analogue for split-type iquantum potentially gives explicit $C_b$ in BDI. **Direct entry point for OQ-LU-PAN-EXPLICIT.** Find preprint/PDF via DOI.
- **Bowman, de Visscher, Farrell, Hazi, Norton — CJM April 2026** ⭐⭐⭐ **NEW** — "Oriented Temperley-Lieb algebras and combinatorial Kazhdan-Lusztig theory." Proves KL positivity for all Hermitian symmetric pairs including $(B_n, B_{n-1})$ via graded decomposition numbers in anti-spherical Hecke category. No arXiv ID found. **NOT a resolution of Marberg 1306.2980 positivity conjectures** (those are twisted-involution KL, not Hermitian symmetric pair anti-spherical). Companion: arXiv:2208.02584 (Adv. Math. 2025).
- **arXiv:2508.01795 (Lusztig — July 2025)** ⭐⭐ **NEW** — "Canonical bases in Lie theory and total positivity." ICBS 2025 survey/talk paper. Video: youtube.com/watch?v=T9vtljCIkio. Orientation resource for canonical bases + total positivity; confirms no new BDI-specific content.
- **Browse 29 citation update:** Watanabe 2110.07177 = **30th consecutive BDI null** (still 12 citers). Lu-Pan I (2504.19073) = 1 citer (Lu-Ruan-Zhang). Lu-Pan II (2603.01350) = 1 citer (2603.03381). All watching-mode nulls unchanged.

### Found 2026-05-28 (browse cycle 28 — new):

- **arXiv:2504.19073 (Lu-Pan — April 2026)** ⭐⭐⭐⭐ **NEW** — "Dual canonical bases of quantum groups and iquantum groups I: Hall algebras." Constructs dual icanonical bases via iHall algebras; integral + positive structure constants; invariance under braid group actions + Fourier transforms. Part of Lu-Pan trilogy with 2601.00524 + 2603.01350. **BDI covered via arbitrary finite type.** The trilogy = algebraic existence + positivity for what v3 describes combinatorially. **ADD TO P_PARK read list (post-v3).**
- **arXiv:2603.01350 (Lu-Pan — March 2026)** ⭐⭐⭐⭐ **NEW** — "Dual canonical bases of quantum groups and iquantum groups II: geometry." Geometric construction via perverse sheaves on quiver varieties; two methods (Hall 2504.19073 + geometry) coincide; positivity of transition matrix coefficients proved geometrically. BDI included. Completes the trilogy with 2601.00524 + 2504.19073. **ADD TO P_PARK read list (post-v3).**
- **arXiv:2511.00882 (Lu-Pan-Wang-Zhang — November 2025)** ⭐⭐⭐ **NEW** — "Braid group action on quasi-split affine iquantum groups III." 33pp. Completes Drinfeld presentation for ALL quasi-split affine iquantum groups (final case: type AIII^(τ)_{2r} with triple relative root lengths). Structural background; not BDI directly. Background context.
- **arXiv:2603.28446 (Lu-Wang-Weekes — March 2026)** ⭐⭐ **NEW** — "Shifted affine iquantum groups of quasi-split ADE types." Drinfeld presentations + GKLO-type reps via difference operators; quantization of affine Grassmannian islices. **ADE only — not type B/C.** Low priority, background.
- **arXiv:2506.12868 (Aliniaeifard-Li — June 2025)** ⭐⭐ **NEW** — "The peak algebra in noncommuting variables." Introduces NCQSym descent-to-peak map + peak algebra in noncommuting variables; connects to Schur Q-functions in noncommuting variables. Path 1 territory (NSym world). May hint at techniques for OQ-HUANG-B.
- **Browse 28 citation update:** Watanabe 2110.07177 = **29th consecutive BDI null** (still 12 citers, 0 from 2026). Kobayashi 2604.22262 = first citation (self-cite companion 2604.25242). Zhang 2412.07810 + Lusztig 2510.21499 + Marberg 1306.2980 + Meereboer 2510.17655 all still at 0 new citers.
- **Browse 28 confirms:** Mills 2605.23072 = type D arc algebra isomorphism (Bowman-Stroppel-Williamson school), NOT Marberg positivity. Day-43 demotion to P_PARK #4-5 correct.
- **Q-SPHERE update (Browse 28, May 28):** 15/29 TBA unchanged. Kolb + Kobayashi still TBA. Meereboer + Watanabe confirmed. Next check June 5-7.

### Found 2026-05-26 (browse cycle 25 — new):

- **arXiv:2605.23072 (Ben Mills — May 2026)** ⭐⭐ **NEW** — "Isotropic Meta Kazhdan-Lusztig Combinatorics II: Isomorphism to the generalised Khovanov arc algebra." Establishes isomorphism between type D Khovanov arc algebras and basic algebras of anti-spherical Hecke category for $W(D_n)/W(A_{n-1})$. Part II of series (Part I = arXiv:2601.15426). Type D Hecke categorification. Adjacent to Marberg 1306.2980 territory (type D KL) but doesn't directly attack positivity conjectures. Post-v3 scope check.
- **arXiv:2604.03071 (Apr 2026)** ⭐⭐⭐ **GRANT CONTEXT** — "Formalizing a Graduate Algebraic Combinatorics Textbook in Lean4." Reports 30,000 Claude 4.5 Opus agents formalized a 500+ page algebraic combinatorics textbook in one week: 130K lines, 5,900 declarations. Open-source but NOT in Mathlib. Key framing for AI4Math grant: AI handles verification of known-shape proofs at scale; discovery of new structural objects (like $P_a$) is the moat. Lean4 context: Mathlib has Hopf algebras + Young tableaux but lacks Hecke algebras, crystal bases, Coxeter groups, quantum groups. Chain-factor $B_2$ formalization = months-long from-scratch project.
- **Q-SPHERE 2026 UPDATED (Browse 25):** 39 talks total (was 30). Kolb (June 9, 09:00) STILL TBA. Kobayashi (June 11, 09:50) STILL TBA. **Watanabe title now confirmed:** "Quantizations of coordinate algebras of symmetric pair subalgebras." New talks confirmed: Vlaar+Appel (quantum affine QSP, two-part, Day 1), Wang "Weight modules for gl₂×gl₂" (June 9, 09:40), Song "QSP at roots of unity" (June 9, 13:15), Terwilliger "q-Onsager algebra" (June 10, 13:15).
- **Browse 25 correction:** arXiv:2605.20383 (Huang-Zhang) actual scope = affine RSK in type A, not "bridge between Hopf algebra and Marberg KL communities" as Browse 24 claimed. Downgraded to ⭐.

### Found 2026-05-26 (browse cycle 24 — new):

- **arXiv:2605.17844 (Dai, Zhang — May 18 2026)** ⭐⭐⭐ **NEW** — "Recursive structures of molecules and cells in Gelfand S_n-graphs." Continues Marberg quasiparabolic/Gelfand W-graph program in type A. Cites Marberg 1408.0589 and/or 2212.13373, NOT 1306.2980. Does NOT attack type B/D positivity conjectures. Scan references for type B/D activity. Post-v3 read alongside Zhang 2412.07810.
- **arXiv:2605.20383 (Daoji Huang + Sylvester Zhang — May 2026)** ⭐ **SCOPE CORRECTED (Browse 25)** — Actual title: "Dual Affine Robinson-Schensted Correspondence." Affine RSK paper parametrizing KL cells in affine type A via Shi's correspondence and Fomin-Viennot. No Hopf algebra content, no Marberg connection. Browse 24 description was wrong (phantom-attribution instance #4). LOW relevance to Rick.
- **arXiv:2601.07793 (Barkley-Gaetz-Lam — Jan 2026)** ⭐⭐⭐ **UPGRADED** (was ⭐ LOW) — "Combinatorial invariance of q-coefficient in KL polynomials for all Coxeter groups." Also proves Gabber-Joseph conjecture (second-highest Ext between Vermas). Big KL result, seed Q2. **2 citers (Browse 25):** Zannoni (hypercube decompositions) + Gorsky-Kim-Sherman-Bennett (toric Richardson varieties) — both combinatorics/geometry, not quantum-groups content. Post-v3 read.
- **Q-SPHERE 2026 UPDATED (Browse 24):** Kolb now confirmed June 9 09:00; Kobayashi June 11 09:50. See Conferences section above for full update.
- **Browse 24 calibration:** Zhang 2412.07810 does NOT cite Marberg 1306.2980. OQ-ZHANG-MARBERG bridge is structural parallel, not citation chain. P-estimates adjusted downward in zhang-lusztig-bridge-for-marberg.md.

### Found 2026-05-22 (browse cycle 23 — new):

- **arXiv:2412.07810 (Yifeng Zhang, Dec 2024)** ⭐⭐⭐⭐ **NEW** — "Lusztig a-functions for Marberg's quasiparabolic S_n-graphs; every molecule is a cell." Direct follow-up to Marberg arXiv:1306.2980. Establishes a-function theory for quasiparabolic Hecke setting (type A). Bridge toward OQ-LUSZTIG-MARBERG. Read before attacking Marberg 4 conjectures post-v3.
- **arXiv:2507.12328 (Salmasian-Savage-Shen, Jul 2025)** ⭐⭐⭐ **NEW** — "Disoriented skein and iquantum Brauer categories for orthosymplectic pairs." Categorical Schur-Weyl / Howe duality for BDI at the diagrammatic level. No crystal content. Seed question 3 reference (Hopf-algebraic Schur-Weyl functor for BDI). Post-v3 read.
- **arXiv:2511.23367 (Meereboer-Schlösser, Nov 2025)** ⭐ — "Quantum Matrix Spherical Functions." Framework for matrix-spherical functions via dual Hopf algebras + right coideal subalgebras → **Intermediate Macdonald polynomials**. Meereboer's MK polynomial/harmonic-analysis thread running in parallel to his crystal/branching work. **NOT the Meereboer-Kolb joint Kostant branching paper.** Browse 42: CONFIRMED content. The joint paper = new unpublished work to be announced at Q-SPHERE June 9.
- **ATTRIBUTION CORRECTION:** "Bao-Song 2023 rank-one stability" (Meereboer's engine) is a phantom. Correct: **Watanabe 2023 alone** — "Stability of icanonical bases of irreducible finite type of real rank one" (DOI:10.1090/ert/639, Representation Theory 2023, 7 SS citers). Bao-Song arXiv:2402.08258 = separate coordinate rings paper. Fix any mention of "Bao-Song rank-one stability."
- **SS API fix for Watanabe 2110.07177:** SS indexes this by DOI (10.1007/s10468-023-10207-z), SS ID f51b027ffdc9fd0471c3af3ff5e8c5b91d14e27f. The ARXIV: prefix returns 404. The SS=12/GS=13 gap is structural (GS has one journal-only citer). Do not retry ARXIV: prefix.
- Q-SPHERE 12/29 talks unchanged (Kobayashi/Kolb not listed). Marberg 1306.2980 = 0 citers 2025-2026. Lusztig 2510.21499 = 0 citers. All watching-mode nulls confirmed.

### Found 2026-05-21 (browse cycle 20 — new):

- **⭐⭐⭐⭐ Hideya Watanabe confirmed Q-SPHERE 2026 speaker (Browse 20).** Previously only Kobayashi + Kolb noted. Now ALL THREE of Kobayashi (analytic/fence), Watanabe (AII/icrystal), and Kolb (algebraic QSP) will be at the same workshop. Rick's v3 bridges all three. Urgency of pre-Q-SPHERE submission upgraded to maximum.
- **OQ-MUNIZ-CARRY verdict: likely NEGATIVE (Browse 20 deep read).** Muniz 2505.21738 uses Sundaram's positional condition (static per-entry row bounds, not cumulative carry). Her branching criterion is structurally different from Rick's P_a. P(carry-analog in symplectic branching) ≈ 20%. Downgrade OQ-MUNIZ-CARRY to low post-v3 priority.
- **Jia Huang arXiv:1501.05250 scope: NSym^B ABSENT.** Only QSym^B side (comodule over type-A Hopf). Companion paper **arXiv:1506.02962** ("A Uniform Generalization of Some Combinatorial Hopf Algebras") may have NSym^B Hopf structure. **Read 1506.02962 abstract in Browse 21.** If also absent, OQ-HUANG-B = genuinely open.
- **Q-SPHERE 2026 schedule: NOT YET POSTED** as of 2026-05-21. Confirmed speakers: Kobayashi, Kolb, Watanabe (newly confirmed), Koornwinder, Opdam, Stokman. No program details. Check Browse 21 (~May 28).
- **Watanabe 2110.07177: 20th consecutive BDI null.** Still 12 citers, no new ones. BDI slot uncontested.

### Found 2026-05-21 (browse cycle 19 — new):

- **⭐⭐⭐⭐ OQ-KFENCE (new open question):** Kobayashi's fence conditions ξ_i + δν_j = ±1/2 for (O(n+1), O(n)) branching stability may be the analytic description of Rick's carry-wall inequalities ($L_a, U_a, E$). If yes, Rick's Theorem F is the first combinatorial proof of Kobayashi's stability for the BDI case. Verify in v3 §3.6 by translating fence conditions to highest-weight language.
- **arXiv:2410.21654 (Appel-Vlaar, Oct 2024, Indag. Math. 2025)** ⭐ — "Boundary transfer matrices arising from QSP of finite and affine type." NEW citer of Watanabe 2110.07177 not previously in notes. Integrable systems / boundary transfer matrix direction. Low relevance to BDI branching per se.
- **arXiv:2407.00189 (Bodish-Elias-Rose, Jul 2024)** ⭐⭐ — "Spin Link Homology." Categorifies spin-colored so_{2n+1} quantum link polynomial; makes contact with iquantum groups at type B. Most relevant type-B/orthogonal paper from the categorification program. Related to Bodish-Kalmykov territory. Skim abstract.
- **arXiv:1501.05250 (Jia Huang, 2015, Annals of Combinatorics)** ⭐⭐ — "0-Hecke algebras of type B/D and noncommutative symmetric functions." Claims "correspondence between type B/D 0-Hecke and NSym type B/D" but likely as NSym-modules not standalone Hopf algebra. **READ to determine whether NSym^B Hopf algebra level is prior work or genuinely open.**
- **Kobayashi does NOT cite Frohmader, Watanabe, or any crystal/combinatorial paper.** Three isolated communities (analytic/crystal/GL-crystal) all attacking orthogonal branching with zero mutual awareness. Rick's v3 can bridge all three.
- **Watanabe 2110.07177: still 12 citers (no increase).** 19th consecutive BDI null. BDI territory uncontested.

### Found 2026-05-20 (browse cycle 18 — new):

- **Muniz arXiv:2505.21738** ⭐⭐⭐ MEDIUM-HIGH — "Symplectic Branching through Crystals" (May 2025, 17pp). Alternative proof of Naito–Sagaki conjecture (GL_{2n} ↓ Sp_{2n}) using **pure crystal tableaux bijections** — no iquantum groups. Constructs explicit bijection: crystal HW elements ↔ Sundaram's LR-Sundaram tableaux. AII/CI parallel to Rick's Theorem B for BDI. Comparing Muniz's bijection vs. chain-factor descent may reveal whether Theorem B is part of a uniform classical-type family.
- **Frohmader arXiv:2312.11295 v2** ⭐⭐ MEDIUM — "Graded Multiplicities in the Kostant-Rallis Setting" (v2 May 2025). Combinatorial GL_n ↓ O_n and GL_{2n} ↓ Sp_{2n} branching rules via GL_n-crystal combinatorics. **GL_n ↓ O_n is directly in the BDI setting** (GL_{2n+1} ↓ O_{2n+1}). Graded multiplicities on K-nilpotent cone + Schmid-Vilonen connection to Kobayashi polytope geometry. Check: does his formula at B_2/B_3 match Theorem E?
- **Kobayashi arXiv:2604.25242** ⭐⭐ MEDIUM — "Stability of Multiplicities in Symmetry Breaking: The sl_2 Case" (Apr 2026; Springer Proceedings). Expository companion to 2604.22262, posted 4 days later. Explicit "fence" polytope coordinates in the sl_2 case: Pieri rule, K-type formulas, Verma tensor products. **Directly preparatory for OQ-K** — the sl_2 case should be checkable against $[S \le P_1]$ at $B_1/B_2$.
- **Harris-Kobayashi-Speh arXiv:2509.17007** ⭐⭐ MEDIUM — "Translation functors, branching problems, and Shimura varieties" (2025, 3 cites). Technical predecessor to Kobayashi 2604.22262; introduces coherent families and the fence framework. Read if pursuing OQ-K at the analytic level.
- **Jian-Luo-Wu arXiv:2502.20958** ⭐ LOW-MEDIUM — "Lyndon bases of split imath quantum groups" (Feb 2025; J. Algebraic Combin. 2025). PBW/Lyndon basis for split iquantum groups. BDI is split-type; this is the algebraic PBW foundation above which Rick's crystal lives. Structural reference.
- **Ziming Chen arXiv:2601.13482** ⭐ LOW-MEDIUM — "iCanonical basis, quasi-split rank-one iquantum group" (Jan 2026, 0 cites). Explicit transition matrices between icanonical / monomial / standardized canonical bases at rank-one. Check: consistent with chain-factor descent at $B_1$?
- **arXiv:2601.07793** ⭐ LOW — "Combinatorial invariance of coefficient of q in KL polynomials, all Coxeter groups" (Jan 2026). Partial answer to seed question 2 (can you read KL from crystal graph?). Peripheral for now.
- **Bodish-Kalmykov** (Comm. Math. Phys. 2025) — see existing entry below; **Browse 18 update:** possibly relevant to seed question 3 (Hopf-algebraic Schur-Weyl functor for BDI) via orthogonal Howe duality for split symmetric pairs. Confirm scope more carefully.
- **Stroppel-Wojciechowski** (Glasgow Math. J. 2025) — see existing entry below. Confirmed as 2025 Watanabe AI citer; rank-1 BDI diagrammatics.

### Found 2026-05-20 (browse cycle 17 — new):

- **Kobayashi arXiv:2604.22262** ⭐⭐⭐ STRUCTURAL CONTEXT — "Stability of Branching Multiplicities for Orthogonal Gelfand Pairs" (April 24, 2026, 50pp, math.RT). For orthogonal reductive pairs (G,H), proves branching multiplicities are locally constant on polyhedral regions bounded by universal piecewise-linear "fences." BDI = (GL_{2n+1}, O_{2n+1}) is exactly an orthogonal Gelfand pair — Kobayashi's fences theorem predicts the linear form of Rick's cross-chain indicator $[S \le P_{n-1}^{\text{cum}}]$ from Theorem E. **Slow read after v3 OPEN-2 closes; may deserve a brief remark in v3 §5.**
- **Chou-Hamaker arXiv:2604.03379** ⭐⭐ — "Coxeter and Schubert Combinatorics of μ-Involutions" (April 3, 2026, math.CO). Cell decomposition of GL_n/O_n wonderful compactification by Borel orbits indexed by μ-involutions; exchange principle + Bruhat order + μ-involution Schubert polynomials. **Speculative connection:** do μ-involutions correspond to Rick's chain-factor orbits? Post-v3 investigation.
- **Cao-Huang arXiv:2604.19511** ⭐ — "Verma Bases for spo(4|1)" (April 21, 2026, math.RT+QA). Companion to 2604.19490 (already in feeds). Verma bases for orthosymplectic superalgebra spo(4|1) via KN tableau conditions. Low priority.
- **Hong-Tsymbaliuk arXiv:2604.21785** ⭐ — "Orthosymplectic quantum groups revisited" (April 23, 2026, math.RT+QA). RLL-realization of extended orthosymplectic quantum supergroups. Technical infrastructure; very low priority.
- **Nguyen-Pylyavskyy arXiv:2605.12880** ⭐ — "TL-Immanants of Ribbon Decomposition Matrices" (May 13, 2026, math.CO+RT). TL-immanants from dual canonical basis are Schur-positive on ribbon matrices. Adjacent to R. Chen 2605.00013; low priority.
- **Marberg arXiv:2512.19045** ⭐ calibration — "Classical Double Grothendieck Transitions" (Dec 2025, math.CO). Resolves K-Stanley type B/C/D positivity conjectures. This is K-Stanley positivity, NOT the twisted-involution KL positivity (arXiv:1306.2980 — those 4 conjectures remain completely unguarded; Marberg has pivoted away from them).
- **Marberg arXiv:2512.19034** ⭐ calibration — "Brion Atoms for Classical Types" (Dec 2025, math.CO). Involution Schubert polynomials for type B/D. Adjacent.

### Found 2026-05-18 (browse cycle 13 — new):
- **Watanabe arXiv:2509.00853** ⭐⭐⭐⭐⭐ URGENT — "Berele row-insertion and quantum symmetric pairs" (Aug 2025, math.RT). Lifts Kobayashi-Matsumura King-tableau RSK (2506.06951) to AII QSP representation isomorphisms: Berele-RS + full KM RSK = coideal module isomorphisms. Dual RSK of type AII established. **This is the capstone of the AII RSK chain and the direct template for OQ-BDIqLR.** READ NEXT before v3 draft. (Was in feeds as 2506.06951 companion but now confirmed critical.)
- **Azenhas arXiv:2601.06930** ⭐⭐⭐ NEW UNTRACKED — "The symplectic left companion of a LR-Sundaram tableau and the Kwon property" (Jan 2026, math.CO). Proves Lecouvey-Lenart conjecture; bijection Kwon ↔ Sundaram branching models via LR commuters + Kumar-Torres flagged hives. Paper #0 in Azenhas's 2026 AII quantum LR series (before 2603 and 2604). Read after Watanabe 2509.
- **Halacheva trajectory update:** No 2026 crystal/iquantum output. Has shifted to KV theory and moduli spaces. Reduced competition on type-B KN-tableau cactus — gap even more open.
- **Watanabe 2110.07177: still 12 citers. 13th consecutive MathOverflow null.** Possible 13th citer: Azenhas 2601.06930 (not yet confirmed by SS). All confirmed citers = type AII or type C only. BDI slot uncontested.
- **Lu-Pan arXiv:2605.13578** — "Quiver varieties and dual canonical bases" (May 2026, math.QA). ADE types only; positivity and braid invariance for iquantum dual canonical bases; resolves Berenstein-Greenstein. Monitor; not BDI-immediate.
- **FPSAC 2026:** Lee's invited talk covers type B spin weights + KR crystals via SSOT/King-tableau framework. Adjacent combinatorial world — compare against BDI crystal predictions eventually (low priority now).
- **Lee arXiv:1910.04459** ("Crystal structure on King tableaux and semistandard oscillating tableaux," Transformation Groups 30, 2025, pp. 823–853) ✓ SCOPED — purely type C/AII, NO BDI content. 11 citers, all AII/type C. This is [Lee25] in Watanabe 2509 §4e. There is NO type-B analog in the literature — BDI oscillating tableaux = open. See also Lee's 2024 follow-up arXiv:2409.02341 (SSOT energy formula, type C).

### Found 2026-05-18 (browse cycle 12 — new):
- **Azenhas 2603.16698 FULL DETAIL**: Recording tableaux equinumerous to LRS tableaux (AII); injectivity combinatorial + surjectivity via NSW. Orthogonal transpose symmetry map analyzed. **Primary template for OQ-BDIqLR — READ NEXT WAKE.**
- **Azenhas 2604.25856 FULL DETAIL**: "Slack" of recording tableau = extra data needed to invert quantum LR map; uses reverse Schensted column insertion routes. Compare Rick's (step_type, factor) descent recording to "slack" structure. **Read alongside 2603. KEY: does R(π) = slack for BDI?**
- **Kolb-Yakimov arXiv:2603.06132 CONFIRMED**: Short star product paper. Quasi K-matrix = Letzter-projected quasi R-matrix. Elementary proofs of bar involution + Balagovic-Kolb + tensor quasi K-matrix. Algebraic infrastructure simplification for all QSP including BDI. **Read before algebraic-level BDI work.**
- **Kolb-Stephens arXiv:2407.15538** (2024, 2 cit) — "Representation theory of very non-standard quantum so(2N-1)": type B QSP at non-standard parameters. First serious non-standard-parameter rep theory for so(2N-1). Watch.
- **Song 2512.01398** — symmetric subgroup schemes for QSP (Jinfeng Song solo). Algebraic geometry side of QSP. 0 citations. Monitor.
- **Song-Zhang 2601.19670 ICMS SLIDES CONFIRMED**: Content = Frobenius center Z₀ı ≅ C[K^⊥\G*]; Uı_ε free of rank ℓ^{dim k}; irreps by θ-twisted conjugacy classes; explicit Frobenius map at split rank 1. Roots of unity = new direction.
- **Li Jianrong ICMS slides EXTRACTED**: Boundary q-characters for affine QSP via **semistandard orthogonal tableaux** (SSOTs) + content monomials Υ_{i,b}. Orthogonal tableaux = affine-level cousin of Rick's finite-level work. Notes at 2026-05-18-browse12.md.
- **Park ICMS slides EXTRACTED**: Matches arXiv:2507.01306. PBW/String parametrization of quantum twist ηw via integer matrices N_i, M_i. Not QSP/coideal.
- **Watanabe 2110.07177 still 12 citers, NSW still 4 citers.** No movement. 12th consecutive MathOverflow null. BDI slot confirmed uncontested.
- **Chen-Lu 2601.00524: 0 citers. Park-Jung 2507.01306: 0 citers.** Both clean fields.
- **IMJ-PRG dates corrected**: June 15-19 (not 17-18).
- **Muniz 2505.21738 CONFIRMED**: Third AII branching proof (pure crystal, no iquantum). Short paper, complementary tools. Cites Kumar-Torres 2412.19721.

### Found 2026-05-17 (browse cycle 11 — new):
- **Brundan-Wang-Webster arXiv:2505.22929** ⭐⭐⭐⭐⭐ URGENT — "Categorification of quasi-split iquantum groups in all symmetric types" (91pp, May 2025, Wang group). If "all symmetric types" includes BDI, this is the 2-categorical framework above Rick's crystal-level v2. Framework-level bridge = permissible. Read abstract immediately.
- **Park-Jung arXiv:2507.01306** ⭐⭐⭐⭐ — "Crystals and quantum twist automorphisms on unipotent coordinate rings" (July 2025, Euiyong Park + Jung). KKOP-group paper. Park presented at ICMS Edinburgh Nov 2025. Quantum twist automorphisms = crystal-theoretic cactus direction. Check type B scope.
- **Azenhas arXiv:2604.25856** ⭐⭐⭐ (Apr 2026) — "Quantum LR maps via AII branching rule"; operationalizes NSW for quantum LR maps. Rick's BDI tensor product rule = natural BDI analog.
- **Azenhas arXiv:2603.16698** ⭐⭐⭐ (Mar 2026) — "Symplectic tableaux and quantum LR map"; companion to above.
- **Muniz arXiv:2505.21738** ⭐⭐⭐ (May 2025) — alternative crystal proof of Naito-Sagaki conjecture (NSW result). Two independent proofs now; method is robust.
- **Stroppel-Wojciechowski arXiv:2406.12132** ⭐⭐⭐ — CONFIRMED arXiv ID (was searching). "Diagrammatics for the smallest quantum coideal and Jones-Wenzl projectors." Glasgow Math. J. April 2025. Type B/D Jones-Wenzl projectors via coideal diagrammatics.
- **NSW 2502.07270 UPDATE**: now 4 citers (Azenhas ×2, Watanabe 2509, Muniz). All AII. No BDI move.
- **FPSAC 2026 programme POSTED**: sites.math.washington.edu/fpsac2026/program/ — Lee invited (type B spin weights, arXiv:2412.20757); zero talks on iquantum/coideal. Rick's territory unrepresented.
- **IMJ-PRG Summer School 2026 POSTED**: indico.math.cnrs.fr/event/14175/ — Schilling mini-course June 17-18, Paris.
- **ICMS Edinburgh slides**: Park-Jung posted. Halacheva NOT posted. Kolb "Letzter map for QSP" posted (get slides).
- **Svyatnyy 2605.00514 VERDICT**: type D (so_{2n}) spinor crystal, NOT type B KN-tableaux. Gap still open. But check: does so_{2n+1} coverage exist in the paper?

### Found 2026-05-17 (browse cycle 10 — new):
- **arXiv:2509.18982 (Weinan Zhang, Sep 2025/Jan 2026)** — "Quantum Howe duality and Schur duality of type AIII": proves iquantum AIII weight spaces ≅ type B Hecke algebra modules; relative braid group action on iweight spaces = type B Hecke algebra action; bridge between Paths 2↔3 (iquantum crystal ↔ type B Hecke). HIGH PRIORITY READ. ⭐⭐⭐⭐⭐
- **Stroppel-Wojciechowski (Glasgow Math. J. 2025)** — "Diagrammatics for the smallest quantum coideal and Jones-Wenzl projectors": diagrammatic approach to "smallest" quantum coideal; Watanabe-2110.07177 citer; arXiv ID unknown (find it). ⭐⭐ FIND ARXIV ID
- **Han J. Algebraic Combin. 2024** — "Finite Young wall model for representations of iquantum groups": Young wall model for iquantum representations; Watanabe-2110.07177 citer; arXiv ID STILL UNKNOWN. If this covers type B, direct competitor territory. FIND ARXIV ID. ⭐⭐⭐
- **KKOP arXiv:2512.03425 (Dec 2025)** — "Faithful action of braid group on bosonic extensions" (Kashiwara-Kim-Oh-Park follow-up to 2408.07312); 12 pages; faithfulness of braid action on bosonic extensions. ⭐ MEDIUM, no coideal content
- **ICMS Edinburgh Nov 2025, "New Perspectives in Quantum Representation Theory"** — slides may be posted at icms.ac.uk/activities/workshop/new-perspectives-in-quantum-representation-theory/; check Park "Crystals and quantum twist automorphisms" + Halacheva "Categorical braid group actions." ⭐⭐⭐
- **Confirmed: KOW arXiv:2209.10325** — "KR modules and quantum K-matrices" (Kusano-Okado-Watanabe, Comm. Math. Phys. 2024). "All quasi-split Satake diagrams" = general K-matrix framework; explicit combinatorial KR crystal = affine type A only. BDI slot open. ✓ scope check done.
- **Confirmed: JLW arXiv:2502.20958** — 0 citers as of May 2026. Intellectual lineage: Bao-Wang + Kolb-Letzter + Lu-Wang Hall algebras + Watanabe crystal paper (only crystal input). Rick's v2 is the natural crystal-level sequel. ✓
- **Confirmed: Bodish-Kalmykov** — DOI 10.1007/s00220-025-05482-4 (Comm. Math. Phys. 2025). ⛔ SCOPED OUT (no BDI/crystal content). Among Watanabe's 12 citers: zero work on type BDI crystals. Territory confirmed open. ✓
- **Territory confirmation:** Watanabe 2110.07177 has 12 citers. ALL stay in quasi-split simply-laced or type AII (Sp). Nobody in type BDI. MathOverflow: ZERO threads on any of Rick's five topics. Wang 2024 survey (arXiv:2112.10911) explicitly calls crystal theory for iquantum groups "not in full generality."

### Found 2026-05-16 (browse cycle 9 — new):
- **Bodish & Kalmykov (2025) "Orthogonal Howe Duality and Dynamical (Split) Symmetric Pairs"** — CRITICAL COMPETITOR FLAG. Cites Watanabe 2110.07177. "Orthogonal" + "split" terminology overlaps with Rick's type BDI. Find arXiv ID immediately. If this paper constructs a crystal for split SO-type, it's a priority conflict. ⭐⭐⭐⭐⭐ FIND ARXIV ID
- **Kusano–Okado–Watanabe (2024)** — "KR modules for all quasi-split Satake diagrams" (Watanabe co-author). "All quasi-split" may include BDI (all-black Satake diagram = split = BDI). Scope check needed. ⭐⭐⭐ FIND ARXIV ID
- arXiv:math/0603547 (Sternberg 2006) — "Local structure of doubly laced crystals"; proves Stembridge's conjecture for B, C, F4, G2; local axioms characterize what the $a_{ij}=-2$ short-long edge forces on tensor product rules. Key technical input for P1. ⭐⭐⭐
- arXiv:2501.15837 (Biswal-Gaussent 2025) — tensor product decomposition via Littelmann paths; only citer of Azenhas-Torres 2409.12666; no type BDI content. ⭐ low priority
- arXiv:2502.07270 (Naito-Suzuki-Watanabe Feb 2025) — proof of Naito-Sagaki conjecture via type AII iquantum crystal; Watanabe's latest crystal paper, entirely type AII/symplectic. Confirms BDI not in his current program. ⭐⭐

### Found 2026-05-16 (browse cycle 8 — new):
- arXiv:2409.12666 (Azenhas-Gonzalez-Huang-Torres 2024) — "Keys and Evacuation via Virtualization"; works DIRECTLY on type B KN-tableaux; proves Fujita and PPSS virtualizations coincide with De Concini-Lecouvey splitting map; gives COMBINATORIAL DEFINITION OF ORTHOGONAL EVACUATION (one cactus generator for type B); Torres group; full cactus action not done but evacuation = highest priority pre-v2 read ⭐⭐⭐⭐⭐ **READ IMMEDIATELY before v2**
- arXiv:2412.02614 (Brown-Elek-Halacheva Dec 2024) — "Cacti, Toggles, and Reverse Plane Partitions"; type D cactus on B(nw_1) via RPP toggles; type D done = confirms type B KN-tableau = ONLY open case; Halacheva group ⭐⭐⭐
- arXiv:2605.01696 (Shen-Zhang May 2026) — ibraid on quantum supersymmetric pairs type sAIII; algebra level not crystal; active frontier May 2026 ⭐⭐
- arXiv:2506.05959 (Bae-Kwon 2025) — q-Howe duality orthosymplectic; cites Watanabe AI-crystal; type B geometry present but no BDI braid ⭐
- arXiv:2502.20958 (2025) — "Lyndon bases of split iquantum groups"; CHECK IF BDI COVERED ⭐⭐ (could be algebraic foundation for Rick's braid)
- arXiv:2505.22929 (2025) — "Categorification of quasi-split iquantum groups"; CHECK ABSTRACT for type BDI coverage ⭐

### Found 2026-05-15 (browse cycle 7 — new):
- arXiv:2604.19490 (Cao-Huang Apr 2026) — "Verma Bases and Kashiwara-Nakashima Tableaux of sp₄"; natural bijection Verma basis vectors ↔ KN tableaux for sp₄ = B₂ = C₂; direct check on Rick's B₂ Aug~ / BGG-Verma differential; fresh, no citations ⭐⭐⭐⭐ **READ before v2**
- arXiv:2504.14042 (Li-Przezdziecki Apr 2025/Apr 2026 rev) — "Boundary q-characters of evaluation modules for split quantum affine symmetric pairs"; Lu-Wang framework; "extra symmetry" = affine analogue of Rick's on-slice commutativity; boundary q-characters new invariants ⭐⭐⭐
- arXiv:2601.19670 (Song-Zhang Jan 2026) — "Representations of quantum symmetric pairs at roots of unity"; Frobenius center = coideal subalgebra; θ-twisted conjugacy classes; may explain why q→0 ALG limit has poles ⭐⭐ CONTEXT
- **Han Shaolong** — ⛔ **PHANTOM REFERENCE (Browse 21).** "Finite Young wall model for iquantum groups" does NOT exist on arXiv. Han's actual iquantum paper is **arXiv:2203.03900** ("Differential operator approach to iquantum groups and their oscillator representations") — uses oscillator/differential operator models, not Young walls. The Semantic Scholar citer "Han (2024)" in Watanabe 2110.07177 citer list needs title verification in Browse 22.
- arXiv:2409.12666 (Azenhas-Gonzalez-Huang-Torres 2024) — "Keys and evacuation via virtualization"; Torres follow-up to 2302.11560; still at RSK/Littelmann level; CONFIRMS type B KN-tableau gap has NO direct citer from Torres ⭐ (gap confirmation)
- arXiv:2408.07312 (Kashiwara-Kim-Oh-Park 2024) — "Braid symmetries on bosonic extensions"; extends crystal braid theory to coideal-adjacent bosonic extensions; Kashiwara as author; 6 cit ⭐⭐ RADAR
- arXiv:2207.08446 v4 (Torres-Azenhas-Tarighat Feller, Aug 2025 in press JCA) — already in list as "type C done"; v4 may have new virtualization content; CHECK v4 abstract for "orthogonal" or "type B" content specifically (agent claimed potential type-B closure but this appears to be agent error — paper is symplectic/type C)
- "Poset modules of 0-Hecke algebras of type B" (arXiv ID unknown, 2024/2025) — one of 4 citers of Defant-Searles 2404.04961; may fill in NSym^B direction; FIND ID ⭐⭐

### Found 2026-05-15 (browse cycle 6 — new):
- arXiv:2508.12041 (Wang-Zhang Aug 2025/Jan 2026 rev) — "Relative braid group symmetries on modified iquantum groups"; 3 rank-one formulas for quasi-split iquantum groups. ⛔ **READ 2026-05-15 — REFUTED as categorical home for three-strand braid.** The "3 formulas" are indexed by node $\tau$-orbit type (split / diagonal / quasi-split, $c_{i,\tau i} \in \{2, 0, -1\}$): ONE formula PER NODE depending on Satake class, NOT three formulas per node decomposing a pair-catalog. In split B_n, $\tau = \mathrm{id}$ everywhere → $c_{i,\tau i} = 2$ everywhere → only formula (i) applies → trichotomy degenerates to single class. Cardinality coincidence, not structure. Browse-6 misread the abstract.
- arXiv:2601.18709 (Stroppel-Wang Jan 2026) — "Weight modules for QSP subalgebras"; explicit BGG resolution for QSP coideal subalgebra of gl₄; potential categorical home for off-slice obstruction ⭐⭐⭐⭐⭐ **READ SECOND next wake**
- arXiv:2605.00514 (Svyatnyy May 2026) — "Cactus group on short SSYT"; BK-generator action on short SSYT (entries ≤ N); potential type-B cactus gap closure at KN-tableau level ⭐⭐⭐⭐ **READ THIRD next wake**
- arXiv:2601.13482 (Ziming Chen Jan 2026) — "iCanonical basis, quasi-split rank one iquantum group"; explicit transition matrices at rank one; checkable against B_2 computations ⭐⭐⭐
- arXiv:2112.10911 (Wang ICM 2022 survey, updated Jan 2024) — best expository reference for QSP / iHopf algebraic framework; read before Chen-Lu iHopf papers ⭐⭐⭐ **ORIENTATION READ**
- Kumar-Torres (2024) "Branching models of Kwon and Sundaram via flagged hives" — HUB PAPER bridging Kwon B/C Lusztig data and Torres virtual cactus; Torres as co-author; 5 citations; arXiv ID unknown — FIND ⭐⭐⭐
- arXiv:2605.09589 (Luo-Su-Xu May 2026) — "Affine iquantum groups and Steinberg varieties of type C, II"; geometric K-theory for quasi-split AIII_{2n}; indirect connection ⭐ low priority

### Found 2026-05-14 (browse cycle 5 — new):
- arXiv:2308.01718 (Watanabe 2023/JCA 2025) — **PREDECESSOR FOUND**: "Symplectic tableaux and quantum symmetric pairs"; type AII (gl_{2n}, sp_{2n}) = type C; finite-dim only; NO type B; generators quadratic not quartic ⭐⭐⭐ CONTEXT
- arXiv:2601.00524 (Chen-Lu-Pan-Ruan-Wang Jan 2026) — iQuantum Groups + iHopf Algebras II: dual canonical bases for ALL finite types; settles Berenstein-Greenstein conjectures; ALGEBRAIC FOUNDATION for iQSP B(∞) ⭐⭐⭐⭐⭐
- arXiv:2511.11291 (Chen-Lu-Pan-Ruan-Wang Nov 2025) — iQuantum Groups + iHopf Algebras I: iHopf algebra as framework for quasi-split iquantum groups; ibraid group; Hopf-algebraic home for coideal embedding ⭐⭐⭐⭐
- **arXiv:2407.07280 (Watanabe Jul 2024, v3 May 2025)** ⭐⭐⭐⭐⭐ **URGENT P3** — integrable modules over QSP coideal subalgebras; integrability-preservation theorem = existence guarantee for projection p_ν : V(ν) → V^ı_{BDI}(ν). Matrix coefficients = Bao-Song coordinate ring. Read concurrently with Meereboer 2510.17655 before OPEN-2.
- arXiv:2502.07270 (Naito-Suzuki-Watanabe Feb 2025) — proves Naito-Sagaki conjecture via iQSP crystal theory; GL_{2n}→Sp_{2n} branching via promotion operators ⭐⭐⭐
- arXiv:2601.22926 (Kim-Searles Jan 2026) — **NSym^B FRONTIER**: poset modules of 0-Hecke type B; K_0 = QSym^B (comodule); NSym^B = dual NOT constructed; gap confirmed open ⭐⭐⭐⭐
- arXiv:2302.11560 (Torres EJC 2024) — virtual cactus group + Littelmann paths; type B COVERED via A_{2n-1}→B_n folding at Littelmann path level; KN tableau level still open ⭐⭐⭐⭐
- arXiv:2603.06132 (Kolb-Yakimov Mar 2026) — short star products for QSP; elementary proofs of bar involution + quasi-K-matrix; simplifies QSP infrastructure ⭐⭐⭐
- arXiv:2512.15322 (Lu-Zhao Dec 2025) — Hall algebra framework for QSP; integral coideal embedding + coproduct; derived-category structure for off-slice conjecture ⭐⭐⭐
- arXiv:1610.02640 (Kwon 2016/J.Alg 2018) — Lusztig data of KN tableaux types B/C (13 cit); stronger hub than CST (1708.04311) for the KN-tableau/Lusztig-data territory ⭐⭐⭐
- arXiv:1603.09013 (Salisbury-Schultze-Tingley 2016) — PBW crystal combinatorics, CST predecessor (21 cit); worth mining its own citation tree ⭐⭐
- **BNS CORRECTION**: arXiv:2107.01190 BGG complex is Section 6 (not 4-5); abstract alternating-sum homomorphisms, type A cyclotomic only; no orbit-swap formula, no type-uniform content
- **Torres type-B coverage**: virtual cactus on Littelmann paths covers type B; KN tableau level gap is the concrete open problem
- **Marberg twisted-involution conjectures (1306.2980)**: Marberg pivoted to K-theory (square-root crystals); 4 conjectures STILL OPEN; unguarded territory confirmed

### Found 2026-05-14 (browse cycle 3):
- arXiv:2603.16698 (Azenhas 2026) — "orthogonal transpose symmetry map in quantum LR map"; cites Watanabe coideal RSK; may be same construction as Aug~ from QLR direction; HIGHEST PRIORITY READ ⭐⭐⭐⭐⭐
- arXiv:2506.06951 (Kobayashi-Matsumura Jun 2025 / Feb 2026 v2) — **FIRST explicit BK involution at crystal level for type C** on SSOTs; type-C structural mirror of Aug~; READ BEFORE FINALIZING AUG~ PAPER ⭐⭐⭐⭐⭐
- arXiv:2504.14344 (Svyatnyy Apr 2025) — cactus group on GT patterns for so_N including so_{2n+1} = type B; predecessor to 2605.00514; may partially close type-B cactus gap; VERIFY type-B coverage ⭐⭐⭐⭐
- arXiv:2107.01190 (Bowman-Norton-Simental JIMJ 2024) — BGG resolutions in cyclotomic Hecke; sections 4-5 have explicit differential formulas; calibrated ↔ on-slice correspondence; the ID Rick was missing ⭐⭐⭐
- arXiv:2207.08446 (Azenhas-Rodrigues-Tarighat-Feller JCA 2022) — symplectic cactus group action on KN-tableaux via symplectic jeu de taquin; structural model for type B; type C done ⭐⭐⭐
- arXiv:2412.02614 (Brown-Elek-Halacheva 2024) — type-D cactus via toggles on reverse plane partitions; type D now done; type B confirmed as ONLY remaining open case ⭐⭐⭐
- arXiv:2601.17603 (Kobayashi-Matsumura-Sugimoto Jan 2026) — SSOT generating functions symmetric + Schur-positive + saturated Newton polytope ⭐ NOTE
- **arXiv:2510.17655 (Meereboer Oct 2025)** ⭐⭐⭐⭐⭐ **URGENT P2** — baby version of v3 OPEN-2 PROVED. 1-dim modules, all finite types incl. BDI: projection from based U-module to B-submodule is a based morphism via ıcrystal at q=∞ (leading-term conditions). Direct technique template for general ν. Read before OPEN-2 work.
- Chow 2001 "Noncommutative symmetric functions of type B" (57 cit) — foundational NSym^B paper; shared ancestor of all type-B 0-Hecke work; find arXiv ID ⭐⭐
- Kwon 2016 "Lusztig data of KN tableaux, types B/C" (13 cit) — direct companion to CST bridge; computed same combinatorial content from other direction ⭐⭐
- **Cactus program confirmed complete** except type B: A, C (2207.08446), D (2412.02614) done; type B THE ONLY OPEN CASE
- **Marberg twisted-involution conjectures (arXiv:1306.2980)**: STILL OPEN. Marberg moved to K-theory. Virgin territory for Rick.
- **CST bridge (arXiv:1708.04311) confirmed uncited** in research direction: 2 citations in 8 years, none in coideal/crystal direction. Strong differentiator.

### Found 2026-05-13 (browse cycle 2 — post Day-11):
- arXiv:2509.00853 (Watanabe 2025) — Berele RSK lifted to quantum symmetric pairs, coideal subalgebra type AII; any type-B BK involution must respect coideal action; HIGH for P0.5 ⭐⭐⭐
- arXiv:2301.02624 (J. Algebra 2024) — Shapovalov elements, explicit Verma module map formulas for all classical types via Cartan-Weyl + R-matrix; independent algebraic verification of Rick's Section 3 ⭐⭐ CHECK
- arXiv:1708.04311 (Salisbury-Tingley 2017) — explicit bijection PBW Kostant partitions ↔ KN tableaux for B(∞); bridge needed for P0.5 Aug~↔Gutiérrez BK^B ⭐⭐⭐ READ BEFORE P0.5
- arXiv:2401.17360 (Barkley-Defant-Hodges-Kravitz-Lee 2024) — BK involutions for all Coxeter groups as noninvertible toggles; non-invertibility = structural explanation for why type-B KN-tableau BK is hard ⭐⭐
- arXiv:2512.16095 (Hirota 2025) — BGG-type resolution for gl(m|n) via odd reflections; super-analogue of doubly-laced story ⭐ FILE
- arXiv:2404.10266 (Jeralds 2024) — Hochschild cohomology of flag varieties via HV's BGG algorithm; ONLY post-2020 paper doing actual BGG computations; Rick's formula would be faster/more explicit ⭐⭐
- arXiv:2605.00514 (Svyatnyy May 2026) — type-D spinor crystal cactus; type B still open ⭐ CONFIRM GAP
- arXiv:2407.13127 (Lu-Yang-Zhang 2024) — PBW bases for ι quantum groups; compare to Rick's Kostant=PBW basis ⭐⭐
- Kostant game arXiv:2601.16326 + 2605.11449 — game terminates uniquely on simply-laced, FAILS on doubly-laced (B,C,F₄,G₂); may be same obstruction as RAW orbit-swap non-uniqueness ⭐⭐⭐ INVESTIGATE
- **MFF CORRECTION**: Malikov-Feigin-Fuks 1986 at q=1 applies to ALL positive roots including doubly-laced; "straight root" restriction is Dobrev 1991 quantum extension only. MFF is a DIRECT verification path for Section 3, not a fallback. ⭐⭐⭐
- **Seung Jin Lee FPSAC 2026** talk covers type B spin weights jointly with Choi-Kim; check for preprint — complementary to Rick's v1 paper

### Found 2026-05-13 (browse cycle):
- arXiv:1911.00871 (Hemelsoet-Voorhaar 2019/2020) — computer algorithm for BGG resolutions; computes UEA differentials for ALL simple types incl. F_4; does NOT give Kostant-basis orbit-swap form (Rick's form is new); code at https://github.com/RikVoorhaar/bgg-cohomology ⭐⭐ CROSS-VERIFY
- arXiv:2506.06951 (Kobayashi-Matsumura 2025/2026 J. Algebra) — RSK for King tableaux via Berele insertion; type-C BK involution; new SSOT Q-symbol; one of 2 papers citing Gutiérrez ⭐ CONTEXT
- arXiv:2412.19721 (Sathish Kumar-Torres Dec 2024) — Kwon↔Sundaram branching bijection via flagged hives; type C; does NOT fill type-B KN-Sundaram gap ⭐ FILE
- arXiv:2101.05931 (Halacheva-Licata-Losev-Yacobi 2021) — categorical cactus on crystals via Rickard complexes; SIMPLY-LACED ONLY (A, D, E); type B explicitly excluded ⭐⭐⭐ CORRECTION to prior working assumption
- arXiv:1310.0103 (Bao-Wang 2013, Memoirs AMS) — foundational type-B KL canonical bases / positivity; 195 citations; THIS is the paper Rick wants for Marberg P3, NOT Shen-Wang 2108.00630 ⭐⭐⭐ CORRECTION
- arXiv:2510.15462 (Godelle Oct 2025) — minimal generating set of cactus groups for all finite Coxeter types incl. B_n; cites Rouquier-White ⭐ CONTEXT
- Sheats 1999, "A symplectic jeu-de-taquin bijection between King and De Concini tableaux" (64 citations) — hub paper in type-C tableau chain; may suggest type-B analog ⭐⭐ READ FOR P0.5
**FPSAC 2026 talks to watch (July 13-17, Seattle):**
- Pamela E. Harris — "Kostant's Partition Function: Support, Structure, and Surprises" (adjacent to Rick's orbit-swap work)
- Seung Jin Lee — "Lusztig's q-weight multiplicities and their refinements" (type B spin weights + KR crystals; directly relevant)

### Corrected reading list entry:
- arXiv:2108.00630 (Shen-Wang 2021/2023) — ι-Schur duality (ι-quantum group AIII ↔ H(B_n)), NOT KL positivity per se. The actual foundational positivity paper is Bao-Wang 2013 arXiv:1310.0103.

### Found 2026-05-12 (must-read):
- arXiv:2510.21499 (Lusztig Oct 2025) — positivity for W-modules of all classical types via asymptotic Hecke algebra J; directly relevant to Marberg B'/C'/D' conjectures ⭐⭐⭐⭐⭐
- arXiv:2311.10659 (Gutiérrez 2023/2024) — Bender-Knuth involutions for types B and C; crystal-level type-B BK explicitly missing (Aug~ candidate) ⭐⭐⭐
- arXiv:2601.06930 (Azenhas 2026) — symplectic left companion + Kwon property; crystal commutor theory for type C ⭐⭐
- Ilin-Kamnitzer-Li-Przytycki-Rybnikov 2023 — "virtual cactus group and moduli space of cactus flower curves"; 9 cit = hot; find arXiv ID ⭐⭐⭐
- arXiv:2504.01623 (Khare-Matherne-St.Dizier Apr 2025) — log-concavity fails for type B Kostant partition functions
- arXiv:2506.16561 (Liao-Rybnikov 2025) — maximal transitivity of cactus on SYT; type-B analogue open

## Browse 85 updates (2026-07-13)

### GMSW group — new papers added
- arXiv:2507.06220 (Gangl-Gutiérrez-Szwej, July 8, 2026) — dual of Foulkes-Howe map = k-fold plethystic substitution; generalised Foulkes under divisibility; NEW — Track
- arXiv:2412.15006 (Gutiérrez solo, Dec 2024) — sl_2 plethystic crystals; decomposition coefficients a_{1^n[r]}^k; Watch for recursion identification with M_j
- arXiv:2509.01490 (GMSW, Sep 2025) — hook partition modular isomorphisms; proves Martínez-Wildon conjecture; categorifies Stanley Hook Content Formula
- arXiv:2508.14788 (GMSW, 2025) — Weyl module as quotient by dual Garnir relations; foundation for 2607.06749
- arXiv:2505.08422 (GMSW, 2025) — bijective proof of q-Pfaff-Saalschütz; Cartan subalgebra of U_Z(sl_2)
- **Pipeline:** GMSW have several papers in preparation including "full filtration paper" (journal version of 2607.06749)

### β'(c) digit-sum project — new predecessor identified
- **Alekseyev-Amdeberhan-Shallit-Vukusic arXiv:2505.08935** (2025) — "p-adic valuations of values of Legendre polynomials." DIRECT predecessor to Iverson 2603.11069. Technique: find 2-adically dominant term → digit-sum formula. READ THIS before next CODE session on β'(c).
- arXiv:2606.23398 (June 2026) — first-exit proof of Cusick conjecture. Key identity: s_2(n+t) - s_2(n) = s_2(t) - v_2(C(n+t,t)). Kummer as digit-sum.

### FPSAC 2026 status (Day 1 today)
- FPSAC started July 13, 2026. No slides posted yet. Check again July 14-15.
- GMSW poster "Plethystic lifts of q-binomial identities" confirmed.
- Seung Jin Lee (KR crystals types B/C) = July 14. Bergeron (QSym) = July 17.

### Paris summer school slides — NOW AVAILABLE
- Anne Schilling "Crystals and symmetric functions" (June 15-19, 2026): https://www.math.ucdavis.edu/~anne/talk-Paris2026.pdf (~10MB)

### Mittag-Leffler workshop (July 27-31)
- Abstracts still not posted (as of July 13). Recheck July 20-23.

### Complexity ceiling
- arXiv:2602.08441 (Christandl-Harrow-Panova-Posta-Walter, 2026) — "Plethysm is in #BQP." Any algorithm for M_j is in #BQP.

### Type D calibration
- arXiv:2607.03966 (Gerber-Ion-Lecouvey-Lenart, July 7, 2026) — X=K via Koornwinder. Type D_n^{(1)} EXPLICITLY EXCLUDED. Watanabe-Hoshino still not posted.

## Browse 87 updates (2026-07-14, second session)

### β'(c) digit-sum structural derivation — KEY NEW TOOLS

- **Amdeberhan-Manna-Moll arXiv:0707.2119** (2007) — v₂((a)_k) = k − s₂(a+k−1) + s₂(a−1). The exact formula for 2-adic valuation of rising factorials. Apply to (a+3)_{c-1-k} and (b+2)_{c-1-k} in h_k^{(c)} to get digit-sum formula structurally. **Priority PROVE target.**
- **Adamczewski et al. arXiv:2209.11075** — Christol step function: v_p((a)_k) = Σ_{r≥1}(⌊(a+k−1)/p^r⌋ − ⌊(a−1)/p^r⌋). General p-adic case.
- **Beluhov arXiv:2504.21451** "Powers of 2 in Balanced Grid Colourings" (Apr 2026, ECA companion) — proves ν₂(B(m,n)) = s₂(m)·s₂(n). Multi-parameter (2D) Beluhov abacus — directly relevant to Rick's 3-parameter H_c(a,b,k). **Add to PROVE context.**

### Baolahy-Randrianirina 2604.10336 — CORRECTION

- K_{(2^j,1^{n-2j})} = **h_2^j · p_1^{n-2j}**, NOT e_2^j · p_1^{n-2j}. C_{(2)} = h_2 (trivial Z/2 action). CHECK DONE NEGATIVE for M_j identification. **New OQ-SIGN-SPECIES-E-BASIS:** sign-action analog → E_α basis with E_{(2^j,1^{n-2j})} = e_2^j · p_1^{n-2j}. Genuinely open construction.

### New crystal papers
- **He-Tubbenhauer arXiv:2606.02249** (June 2026) — "Presentations for categories of crystals." Generators and relations for monoidal crystal categories from fundamental crystals. Most direct 2026 paper for Path 4 (crystal tensor product = Sym coproduct). Priority read next session.

### New Hopf algebra papers (from Grinberg-Reiner reverse citations)
- arXiv:2506.00380 (Yichen Ma, June 2026) — "Convex Geometries and Hopf Monoids." Canonical characters + QSym invariants for convex geometries. Path 1.
- arXiv:2504.20622 (Hao-Zhu, Apr 2026) — Graded dual of partition diagram Hopf algebra. QSym/NSym analogy.
- arXiv:2506.08883 (Bastidas et al., June 2026) — Hecke factorizations with q-Catalan numbers. Path 3.

### New KL papers (from Barkley-Gaetz-Lam reverse citations)
- arXiv:2606.16894 (Barkley-Gaetz, June 2026) — Bounded Bruhat intervals in affine Coxeter groups. Affine extension of CIC techniques.
- arXiv:2606.11776 (Caselli-Marietti, June 2026) — **Proves Brenti's 2003 conjecture on R-polynomials via special matchings.** KL R-polys have nonneg coefficients.

### FPSAC 2026 full program (today = Day 2)
- **CONFIRMED HAPPENING NOW:** Full program at sites.math.washington.edu/fpsac2026/program/ (109 papers)
- TODAY: Tianyi Yu 10:00 "Grothendieck positivity for square root crystals" (arXiv:2501.16640)
- FRIDAY: McConville-Propp-Sagan "Hyperbinary partitions and q-deformed rationals" (2-adic flavor)
- POSTER: Gutiérrez-Martínez-Szwej-Wildon arXiv:2603.21021 "Plethystic lifts of q-binomial identities" — COMPANION to 2607.06749. Add to GMSW tracking.
- ZERO type-D/DIII content confirmed across all 109 papers.

### β'(c) OEIS gap
- The sequence β'(c) for c = 4,5,6,... = (7,7,10,8,11,11,14,12,...) and D(c) = (1,0,2,2,3,5,3,5,...) are NOT in OEIS. Both submittable. Note: OEIS blocks automated fetches — need manual submission.

### Mittag-Leffler workshop watch
- July 27-31. Schilling + Scrimshaw (KR crystals type D) confirmed participants. Abstracts still not posted as of July 14. Check July 20-21.

---

## Browse 138 updates (2026-09-10, post-Day 185 PROVE / BDI-Hopf refutation)

### (q,t)-LIFT ARC REDIRECTED

Browse 138 confirms: Hikita 2503.23597 closes the (q,t)-lift of (†) IN THE E-BASIS (e-expansion coefficients are q-independent). But the **quantum Pieri rule** (Theorem 3.12 of 2503.23597) is new information:

```
e₁ ⋆ eᵣ = (1-q⁻¹)[r+1]_t · e_{r+1} + q⁻¹ · e₁eᵣ
```

This generates a path-graph recursion in the affine Hecke algebra framework. The open question: does this produce a closed GF identity for Σ_n X_{P_n}(q,t) z^n in the **h-basis or power-sum basis**? That is the actual (q,t)-lift arc — not e-basis (closed), but other bases.

### NEW ORGANIZING STRUCTURE POST-STANLEY-GASHAROV

Kai Zhang 2608.16613: "level-k nice property" hierarchy
- Schur-positive ⊂ strongly nice ⊂ nice
- Three infinite separating families
- Closest thing to a new organizing conjecture

### NC GEODE + FREE CUMULANTS

NT 2511.18366 Browse 138 update: k=-1 geode specialization = **free cumulants**. OEIS sequences A071724, A239204, A006318 (Schröder) appear. Rick's b_k FGCCHA structure + Milnor-Moore (free Lie) + k=-1 geode (free cumulants) might all be the same thing from different angles.

### CITATION ACTIVITY

- Huh et al. 2504.09123: 3 citers (Wang-Wang, Siegl, Hikita). Path graphs = generative set for e-positivity is being used as a working tool.
- Matherne-Morales 2607.21508: 7 citers in 6 weeks. **ChatGPT-5.6 Sol Pro credited by name** as having assisted in finding the counterexample — new methodology acknowledgment.
- AGGSZ 2505.06941: 1 citer — Lauve-Lazzeroni 2603.19494 (r-quasisymmetric → Hopf monoids).

### FPSAC 2027 SPEAKER LIST CONFIRMED

Galway, July 5-9, 2027. **7 speakers: Bouvel, Alex Fink, Haiman, Iyama, Marietti, Mishna, Yip.** PC: D'Adderio, Pilaud, Rajchgot. No deadline yet; expect Nov-Dec call. Abstract draft target: Day 187 (2026-09-14).

### Priority queue update (Browse 138 additions)

1. **Hikita 2503.23597 quantum Pieri recursion for P_n** ★★★ — can the path-graph Pieri recursion close to a GF identity in h-basis?
2. **NC Geode k=-1 ↔ free cumulant check** ★★ — is Rick's b_k GF literally the geode at k=-1, with a_k = geode free-cumulant count?
3. **Siegl 2509.02841 strong P-tableau check** ★★ — test lower bounds against Theorem B coefficients for P_3, P_4, P_5
4. **Kai Zhang 2608.16613 read** ★★ — level-k nice hierarchy for path graphs
5. **Wang-Wang 2608.22184 PDF check** ★★★ — verify SW 2016 = [19] before sending letter (SS API doesn't see it)

---

## Browse 144 updates (2026-09-16)

### HEADLINE: D'Adderio et al. 2608.14836 = potential Route-2 attack vector; novelty confirmed absolute

**D'Adderio–Interdonato–Iraci–Pagaria arXiv:2608.14836 (Aug 14, 2026):** "Leaving the Hall: explicit formulas for Neguț operators." Gives explicit linear-time formula for D_γ inside A_{q,t}. At γ=(m), D_{(m)}·F = e_m·F at q=1. If D_{(a)} = e_a(Y) action in Hikita's level-1 polynomial representation, then this IS the Lemma-3.11-analogue for all a ≥ 2. **30-min SymPy check in next wake session: run D_{(2)} on e_r(X) at m=3,4 and compare with Rick's e_2 ★ e_r formula.** Also proves Theta conjecture.

**arXiv:2508.19704 (Aug 2025):** "Generalized Macdonald functions and quantum toroidal gl(1)." Level-(a,0) operators diagonalized by a-tuple Macdonald functions. Route 3 template: if level-(a,0) = e_a ★ (·), entire Pieri program follows. Check level-(2,0) vs Rick's e_2 ★ e_r at small r.

**Griffin-Mellit et al. arXiv:2504.06936 (Apr 2025):** Bridges A_{q,t} and Hikita. Only e_1 Pieri (Prop 2.4). Does Cor 3.8 imply Rick's closed forms? Must check (1 hr combinatorics).

**Novelty confirmed:** Hikita's verbatim quote (from source text): *"It seems likely that similar Pieri type formula exists for more general quantum multiplication of e_r(X) and Schur functions, but we do not pursue this direction here."* Best possible open-problem citation for Rick's FPSAC abstract.

**Hikita forward cites = 3 total** (Colmenarejo-Klein = different direction; 2 data artifacts). Zero papers build on ★-product. Rick is alone in this space.

**FPSAC 2027:** July 5-9, Galway. D'Adderio is PC (ideal fit). Deadline not yet posted; check fpsac.org in early October 2026. Historical pattern: submission opens Nov 2026.

### Priority queue update (Browse 144 additions)

1. **D'Adderio et al. 2608.14836 §2-3 read** ★★★ — check D_{(a)} = e_a(Y) in level-1 AHA. SymPy test at m=3, a=2.
2. **arXiv:2508.19704 §1 read** ★★★ — level-(2,0) Macdonald operator vs Rick's e_2 ★ e_r formula.
3. **Griffin-Mellit 2504.06936 §2 Prop 2.4** ★★ — same operator as Hikita Thm 3.12? Positioning check.
4. **Goodberry-Orr 2312.11657 Thm 6.1** ★★ — calibrate P_1 coefficient structure.
5. **q^{-n(λ)} vs q^{n(λ)}** ★ — HHL vs DS normalization. Is this the Macdonald involution ω?

## Added 2026-09-25 (Browse 148)
- BIRS 27w5730 Multivariate Orthogonal Polynomials (Banff Jun 27–Jul 2 2027) — Macdonald-adjacent; check application window.
- FPSAC 2027 page fpsac.org/confs/fpsac-2027/ — still no deadline; recheck mid-Oct 2026.
- Hub: Nazarov–Sklyanin "operators at infinity" (links Thibon 2609.10284 and Di Francesco–Vu 2606.12796).
- Note: MathOverflow/math.SE are blocked for the WebSearch/WebFetch crawler (Sep 2026) — community agent yields nothing; try Playwright or drop.

## Added 2026-09-26 (Browse 150)
- Parabolic/partially symmetric Macdonald cluster (track forward cites): BW–Orr 2410.13642, Goodberry–Orr 2312.11657, Lapointe 2206.05177, Cho–Oh 2609.03840, BHMP nonsymmetric shuffle 2509.24040, Qiu–Zhang 2604.10226.
- FPSAC 2027 committee page updated 2026-09-11; /dates/ 404; deadline unpublished. Contact fpsac2027@universityofgalway.ie.
- symmetricfunctions.com (SymCat) HL + chromatic pages: 2026-current reference lists.
- MO/math.SE blocked for WebFetch AND WebSearch — need Playwright for MO 411889.
