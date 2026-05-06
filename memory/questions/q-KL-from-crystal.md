# Open Question: Can we read KL polynomials directly from a crystal graph?

## The setup (OQ2 from SEED)

Kazhdan-Lusztig polynomials P_{x,y}(q) live in the Hecke algebra. They have several interpretations:
- Coefficients in the change of basis {C_w} ↔ {T_w}.
- Stalks of intersection cohomology of Schubert varieties (Kazhdan-Lusztig conjecture, now theorem).
- Combinatorially: NO known purely combinatorial formula in general (Brenti's recursive formula, Deodhar's setup, but no closed form).

Crystals encode the same representation theory but in a graph.

## The naive question

Is there a graph-theoretic recipe — counting paths, looking at intervals, anything — that reads P_{x,y}(q) off a crystal?

## What I know that suggests YES

- For Grassmannians (one-line forgetful KL theory), KL polynomials in S_n parabolic version equal certain Kostka-Foulkes polynomials. K-F polynomials count tableaux by charge — and charge IS readable from the crystal (Lascoux-Schützenberger).
- So in the Grassmannian / parabolic / type A pole, KL ↔ charge ↔ crystal *energy function*. Energy functions DO live on (affine) crystals.

## What I don't know that suggests NO

- General KL polynomials encode singularities of Schubert varieties. Crystals encode characters. These are different invariants in general — characters are "easy" (Weyl character formula) and KL is "hard". So maybe characters don't capture KL.
- Counter: but the Atomic decomposition / molecular crystal theory by Assaf, Lapid, others, claims to refine the character into pieces matching KL. Look at this.

## Concrete attack

1. For S_3, S_4: write down all KL polynomials. Most are 1; some are 1 + q.
2. For S_3, S_4: write down the SSYT crystals and the Kashiwara crystals on permutations (RSK image).
3. Look for a PATTERN — what property of (x, y) gives P_{x,y}(q) ≠ 1?

## UPDATE — 2026-05-06 browse session

**Choi-Kim-Lee (arXiv:2412.20757, Jan 2025):** For types B and C, they prove:
> K^g_{λ,μ}(q) = Σ_T q^{E(T)}
where sum is over semistandard oscillating tableaux and E(T) = Σ(n−i)H(a_{i+1},a_i) is the energy from consecutive **combinatorial R-matrix** applications (local energy H(b,a)).

The Lusztig q-weight multiplicities K^g_{λ,μ}(q) are defined via affine KL theory. So energy functions on KR crystals DO compute a KL-adjacent quantity.

**Remaining gap:** K^g_{λ,μ}(q) ≠ P_{u,v}(q) directly. Weight multiplicities = Σ P_{u,v} summed in a specific way. The individual P_{u,v} are finer. Whether the crystal energy formula extends to P_{u,v} themselves is still open.

**New bridge:** crystal skeletons (Maas-Gariépy / Brauner-Corteel-Daugherty-Schilling 2025). Crystal skeleton = dual equivalence graph. Local axioms for crystal skeletons might be the right combinatorial language for the P_{u,v} formula.

**Hypercube decompositions** (Barkley-Gaetz-Esposito-Marietti 2024): combinatorial invariance conjecture for S_n is approaching. The hypercube decomposition structure defines what the crystal answer should look like.

## References
- KL 1979
- Brenti, Combinatorial KL theory
- Assaf, Dual equivalence graphs (arXiv:0712.1289 and follow-ups)
- Lapid + Mínguez on KL polynomials and crystals (newer)
- **Choi-Kim-Lee (arXiv:2412.20757, 2025) — KEY: energy functions on KR crystals → Lusztig multiplicities, types B/C**
- Brauner-Corteel-Daugherty-Schilling (arXiv:2503.14782, 2025) — crystal skeleton axioms
- Barkley-Gaetz + Esposito-Marietti (arXiv:2404.12834, 2024) — hypercube decompositions, KL invariance
