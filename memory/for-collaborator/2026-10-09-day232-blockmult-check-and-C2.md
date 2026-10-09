# Day 232 PROVE — for Robin (digest item, not a separate email)

Two loose ends from the long version are now closed. Nothing in the paper changed.

1. **Thm 7.8 (block multiplicativity) check coverage.** The empty n=6 log from Day 231 is replaced.
   - The checker re-implements the theorem from the printed statement. Results:
     - n=6, all κ≥2 pairs: 37/37 OK;
     - n=7, non-coarsening pairs: 11/11;
     - n=8, non-coarsening pairs: 29/29.
   - Negative controls fail as they should.
   - Note that n=6 has only three non-coarsening pairs with κ≥2. That is forced, because the smallest non-trivial connected block is (2,2)→(3,1).
   - Some leads vanish at t=−2, and the identity holds there as 0=0. This fits Open Problem (2).
   - Details: `rick-research/proofs/2026-10-10-day232-blockmult-printed-n6-check.md`.
2. **Bernstein (C2) is derived, not cited.**
   - T_i commuting with Sym(Y) follows in about ten lines from the defining word of Y_i, the quadratic relation, the braid relations, and πT_k=T_{k+1}π, once the Y_i commute. It works for Hikita's twisted π too.
   - So if (N) ever enters the paper, its Cherednik imports are only (C1) commutativity and (C3) the simple nonsymmetric spectrum.
   - A ready-to-paste lemma is in `work-in-progress/longversion/appendix-C2-bernstein.tex`. It is not included in the paper.

No action needed from you. FPSAC still waits only on your reply to the 6 \todo defaults.
