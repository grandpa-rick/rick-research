# Q68 type A: parabolic heredity of dominated twins on the census (Wake 284, 2026-11-08)

Grade: **computed** (on the census certificate files; the census itself is "computed", see
`../2026-11-08-q68-typeA-closure.md` §7). Script `twin_heredity.py`, output `out_twin_heredity.txt`.

## Conventions and inputs
- Twins are tableau-level pairs (P_x, P_z) (Prop Q). L(w) = Des P(w), where i ∈ Des P iff i+1 sits in a strictly lower row.
  The script asserts `A == Des P_x` and `RSK(x) = (P_x, Q)` on every census record.
- Census: n=14 `wake282/certs14_*` (4 TWIN); n=15 `prove281/certs15_*` (26 TWIN / 22 NO);
  n=16 `wake282/certs16_*` + `prove283/certs16_6433_ext.json` (2 TWIN, 2 NO overrides), the 5 (5,5,3,3) UNDECIDED set to NO (prove282 verify_red). Totals 4/26/114. These match the closure note.
- An embedded pair that is not in the S_{n+1} candidate list is not a twin (C2). Every candidate pair of S_{n+1} has a verdict.
- Embedding (i): w ↦ w·(n+1). Here J = {s_1..s_{n-1}}, the omitted generator is s_n, and the boundary generator is s_{n-1}.
  Embedding (ii): w ↦ 1⊕(w+1). Here J = {s_2..s_n}, the omitted generator is s_1, and the boundary generator is s_2 (that is, s_1 before the shift).
- Parabolic membership (some common Q puts x, z in S_k × S_{N−k}). The criterion: every row of P is (entries ≤ k) followed by (entries > k), the large parts left-justified form an SYT, and the small and large shapes agree for P_x and P_z. The script checks this at the P-level against brute force for all N ≤ 7 and all k.

## Results
| n | emb | boundary ∈ L(x) | S_{n+1} verdict | count |
|---|---|---|---|---|
| 14 | i | yes | not candidate | 2 |
| 14 | i | no | TWIN / NO | 1 / 1 |
| 14 | ii | yes | not candidate | 2 |
| 14 | ii | no | TWIN / NO | 1 / 1 |
| 15 | i | yes | not candidate / NO | 12 / 4 |
| 15 | i | no | TWIN / NO | 7 / 3 |
| 15 | ii | yes | not candidate / NO | 12 / 4 |
| 15 | ii | no | TWIN / NO | 7 / 3 |

- **Boundary kill: 0 violations.** 36 of the 60 embeddings have the boundary generator in L(x), and none is a twin. 28 of them are already non-candidates via C2; the other 4 + 4 are census NO.
- **Converse FALSE: 16 supports, 8 counterexamples.** The smallest is the S_14 (4,4,3,3) twin
  x = [5,9,13,14,1,4,8,12,3,7,11,2,6,10], z = [8,12,13,14,4,9,10,11,5,6,7,1,2,3], L(x) = {2,3,4,6,7,8,10,11,12}.
  Neither 1 nor 13 is in L(x), yet both embeddings are NO in S_15. The (5,3,3,3) twin lifts to TWIN under both embeddings.
- **Embedded vs native.** In S_15, 2 of the 26 twins lie in a proper standard parabolic. Both are images of S_14 twins, of shape (6,3,3,3); the other 24 are native. In S_16, 13 of the 114 lie in a proper parabolic, all are images of S_15 twins, and the other 101 are native. Every parabolic twin lies in a maximal S_{N−1}; some splits are also k=2 or k=14, which are sub-parabolics of those.
  So downward heredity holds on the data: every twin lying in W_J is the image of a W_J-twin (15/15). Images that fail to be twins: 6 in S_15, 38 in S_16.

## S_14 twins, L(x) = Des P_x
| λ | L(x) | L(z) |
|---|---|---|
| (4,4,3,3) | {2,3,4,6,7,8,10,11,12} | {3,7,11} |
| (5,3,3,3) | {2,3,4,6,7,8,10,11,12} | {3,7,11} |
| (4,4,4,1,1) | {1,2,4,5,6,8,9,10,12,13} | {1,5,9,13} |
| (4,4,4,2) | {1,2,4,5,6,8,9,10,12,13} | {1,5,9,13} |
(x, z one-line: see `out_twin_heredity.txt`.)
