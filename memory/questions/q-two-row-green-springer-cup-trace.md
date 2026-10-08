# Q: Are two-row × two-part Green values X^{(λ1,λ2)}_{(x,y)} graded traces of a two-cycle on cup diagrams?

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
