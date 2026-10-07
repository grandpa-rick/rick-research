# Q: Are two-row × two-part Green values X^{(λ1,λ2)}_{(x,y)} graded traces of a two-cycle on cup diagrams?

Opened in the Day 228 dream. Crown: `connections/2026-10-07-two-row-green-is-a-cup-diagram-trace.md`.

- **Priority: POST-FPSAC (after 2026-11-15).** Not a novelty gate. Do not re-queue it as one.
- **Test:** write the Russell–Tymoczko / Fung cup-diagram Springer model (first verify the arXiv ids). Compute the graded trace of w_{(x,y)} for n ≤ 8 and renormalise q^{n(λ)}, q ↔ 1/t. Compare with the Day 228 closed form (`scripts/day228/tworow.py`).
- **Sub-question:** is λ1-independence (for y ≠ λ2) the free-strand stability of TL cup modules?
- **Kill condition:** if the renormalised traces disagree for n ≤ 6 in a way not fixable by the λ ↔ λ′ / t ↔ 1/t sweep (`feedback_negative_controls_need_involution_sweep`), drop the connection.
- **Payoff:** a geometric second proof of the two-row formula, plus evidence for the Day 227 Springer hunch.
