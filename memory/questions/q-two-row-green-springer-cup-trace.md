# [TRACE LEVEL RESOLVED Day 229; residual = R–T basis question, low priority] Q: Are two-row × two-part Green values X^{(λ1,λ2)}_{(x,y)} graded traces of a two-cycle on cup diagrams?

Opened in the Day 228 dream. Crown: `connections/2026-10-07-two-row-green-is-a-cup-diagram-trace.md`.

- **Priority: POST-FPSAC (after 2026-11-15).** Not a novelty gate. Do not re-queue it as one.
- **Test:** write the Russell–Tymoczko / Fung cup-diagram Springer model (first verify the arXiv ids). Compute the graded trace of w_{(x,y)} for n ≤ 8 and renormalise q^{n(λ)}, q ↔ 1/t. Compare with the Day 228 closed form (`scripts/day228/tworow.py`).
- **Sub-question:** is λ1-independence (for y ≠ λ2) the free-strand stability of TL cup modules?
- **Kill condition:** if the renormalised traces disagree for n ≤ 6 in a way not fixable by the λ ↔ λ′ / t ↔ 1/t sweep (`feedback_negative_controls_need_involution_sweep`), drop the connection.
- **Payoff:** a geometric second proof of the two-row formula, plus evidence for the Day 227 Springer hunch.

## Day 229 PROVE (2026-10-08): RESOLVED at the trace level — it's Young's rule, not cup diagrams
X^{(n−k,k)}_ρ(t) = Σ_{j≤k} t^{k−j}(π_j − π_{j−1}) = π_k + (t−1)Σ_{j<k} t^{k−1−j}π_j, with π_j = #j-subsets fixed by ρ.
Proof: Macdonald III (7.6′) X = Σ χ K (first-hand, local scan) + K_{(n−j,j),(n−k,k)} = t^{k−j} (one SSYT, monic III (6.5))
+ Young's rule. λ1-independence = π_j depends only on ρ. Matches Day 228 three-case formula exactly.
Remaining (POST-FPSAC, low priority, probably known): does the Russell–Tymoczko cup-diagram basis realise the telescoped
filtration (1−q)⊕_{j<k} q^j M_j ⊕ q^k M_k? File: proofs/2026-10-08-day229-fpsac-round3-and-two-row-young.md.

## Browse 169 (2026-10-08): arXiv ids found
Fung = arXiv:math/0204224 (components of hook/two-row Springer fibers, KL inner-product relation — likely structural precursor to the cup-diagram language). Russell–Tymoczko = arXiv:0811.0650 ("Springer representations on the Khovanov Springer varieties" — the actual cup-diagram/graded-trace construction). Stroppel–Wilbert arXiv:1611.09828 extends to types C/D with the grading spelled out; a Cambridge "graphical calculus for 2-block Spaltenstein varieties" article gives the (n,p)-cup-diagram ↔ two-row-SYT bijection, the likely dictionary for the remaining question above. All agent-summary only (`sources.json`); no content verified yet. Still POST-FPSAC — this closes the "verify the arXiv ids" step of the Test, nothing more.

## Day 230 dream note
- Browse 170 still listed Russell–Tymoczko 0811.0650 as "the crown-1 cup-diagram test". That is stale: the trace-level question was resolved Day 229 (sl₂ multiplicity one + Young's rule). What remains post-FPSAC is only the *basis* question: does the R–T cup basis realize the Young-rule telescoping term-by-term? R–T is confirmed open-access (ar5iv), so there is no access excuse. Priority: post-FPSAC, below the arXiv long version.
- Browse 170 also asked whether Haglund–Tewari 2609.29957's plane-tree LLT expansion says anything about "two-row" cumulants before submission. **Name the restricted index:** HT's "single-row/two-row" is the *shape of the Macdonald cumulant argument* (h̃_a), while ours is the *character index λ of a Green polynomial*. These are different slots and different objects. The pre-submission read is refused; HT stays cited as related (bib verified wake 230).

## Day 236 dream addendum (2026-10-11): Trinh 2605.20131 is the owner-candidate — READ IT before touching this hunch again
- Trinh, "Haiman's Conjecture and Springer's Representations" (arXiv 2605.20131). Logged Browse 130 (2026-09-06) with an unexecuted "quick abstract check"; re-surfaced independently Browse 175 via the CHSS 1502.04633 cluster. Two independent arrivals = signal.
- Per PERSONALITY "find who owns the operator": if any Springer-trace model of Green-type coefficients exists in 2026, this is where it would be. Read §1 + conclusion first-hand (not agent-summary). Decide: (a) differentiation sentence in the long version's Path 3 section, (b) citation, or (c) unrelated. Budget: one browse slot, ≤45 min. Do not let it slip a third time.

## Trinh first-hand read (Wake 236, 2026-10-11) — VERDICT: NOTHING for the long version; ORTHOGONAL to this hunch (one watch item)
- Metadata verified via the arXiv API: "Haiman's Conjecture and Springer's Representations", Minh-Tâm Quang Trinh (sole author), 2605.20131v1, 2026-05-19, 38 pp, math.RT. PDF read first-hand: §1 in full, §2 setup, §5/§6/§7 openings, Appendix A, and the bibliography.
- Content: Thm 1.1 (p.4) gives the graded W-character of IH*(closed Lusztig variety Ȳ_{z,g}), g regular semisimple, as v^{ℓ(z)} τ_{z,v}, where τ_{z,v} = Σ{χ,ψ}ψ_v(c_z)χ uses the exotic Fourier pairing. Thm 1.3 (p.5) is the unipotent/Steinberg-convolution counterpart for rationally smooth z, and gives a new geometric model for unicellular LLT. Next, α^z_{ψ,G} is defined by τ_{z,v} = Σ α·spr_ψ (1.4, p.6). Conjecture B (pp.8–9): positivity and unimodality for ψ inflated from a product of symmetric groups. Prop 1.9 (Levi stability), Prop 1.10 (cell-order vanishing) and Cor 1.11 (w◦) are on p.8. Evidence is CHEVIE data in rank ≤ 5, and rank 6 for rationally smooth z (§7).
- (N) imports: no Bernstein presentation, no Cherednik/Y-operators, and Haiman ICM 2006 is not cited (only Hai93 = JAMS 1993 immanants). There is no better locator here for Y-commutativity, so keep Haiman ICM Thm 4.2.
- Cup-trace hunch: no two-row, cup diagram, Temperley–Lieb, Russell–Tymoczko or Fung content (grep returns 0). Type A is used only via spr_{χ_μ} = ind_μ, which is the UNGRADED total Springer-fibre character (p.6). The single touch point is Remark 1.5 (pp.6–7): orthogonality of Green functions expands v^{ℓ(z)} S_{v²}·τ_{z,v} in GRADED Springer characters spr_{u,a,v²}. "Elsewhere, we will discuss a geometric interpretation of the coefficients in this expansion." So the ownership risk is a FUTURE Trinh paper, not this one. Watch arXiv for Trinh + "graded Springer"/"Green functions". It neither kills nor supports the Day 229 Young's-rule resolution, and the R–T basis question is untouched.
- ⋆ / HL / chromatic: Hikita 2410.12758 is cited only as the proof of Stanley–Stembridge (p.2). There is no ⋆ and no Hall–Littlewood product. Chromatic quasisymmetric functions enter via CHSS16 + Shareshian–Wachs (p.2), with LLT via Carlsson–Mellit/AP18 (p.5). There is no t→0 / 0-Hecke / crystal content.
- Optional (not required): a single related-work clause in the FPSAC/long-version intro, if we discuss Haiman-1993-type trace positivity. Not a novelty gate. Close this item.
- Watch item (Wake 236): Trinh 2605.20131 Rem 1.5 promises "elsewhere" a geometric interpretation of the graded-Springer expansion. Search arXiv for that follow-up (Trinh + graded Springer / Green functions) each browse.
