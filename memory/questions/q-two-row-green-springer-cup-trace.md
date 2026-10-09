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
