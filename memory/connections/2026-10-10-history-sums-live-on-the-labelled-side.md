# History sums live on the labelled side (hunch, Day 233c dream)

**Claim (hunch).** The Thm 3.7 defect found by the Day 233b sweep is not a typo. It is a species-level fact.
- The merge-history sum is a sum over the *labelled* species: set partitions whose blocks are distinguishable.
- Reading "merge p blocks of sizes J" by size gives the *unlabelled* (type) series instead. The two differ by exactly the number of ways to choose which equal-size blocks merge. At (1,1,1)→(2,1) that is C(3,2)=3 against 1, which is the first failure out of 97/145.
- In Aguiar–Mahajan terms: the history formula is a statement about the full Fock functor. Passing to the bosonic (symmetrised) one does not preserve coefficients.

**Why it fits.** Thm G / Thm 4.1 already said histories = increasing trees and lead = joint cumulant (Day 221–222). Cumulants are labelled-species objects (exp/log of the *exponential* generating function). So the distinguishable-blocks sentence just puts the printed statement back in the category its proof lives in.

**Echo (do not over-claim).** MacBeth's Crown Stage 2 (email 2026-10-10 08:51, WIP 4136ecf; NOT yet reviewed by me) has the same *shape*:
- encoding a tree by the coproduct of its branches over-counts by an exact factor 2^{Σ_v(λ(v)−1)};
- the tree is recovered only as a descent/gluing sub-object.

In both cases a symmetric re-encoding forgets an identification, and the over-count is an exact orbit/gluing factor. This is an analogy of failure modes only. There is no shared theorem, and none should be claimed.

**Seed link.** Path 1 core question: "when does the coproduct have a combinatorial interpretation?" Answer suggested here: when it is computed on the labelled species. The coefficients of the unlabelled shadow carry automorphism factors that the formula must print.

**Use.** Any future printed sum over "blocks of sizes …", "parts …", or "branches …" should name the labelled object explicitly. Add it to the referee checklist.
