---
name: The 15-move catalog of $e_n^{k(n)}$ at B_n short simple is a three-strand braid through Rick's three seed paths
description: NEW 2026-05-14 dream cycle. The catalog of $n(2n-1)$ net moves decomposing $e_n^{k(n)}$ at B_n short simple splits into intra-chain (Path 3 / BGG-Verma), cross-chain (Path 2 / Watanabe quartic / iquantum group), and singleton-involving (Path 1+4 / off-slice Hopf boundary) pieces. Single combinatorial object touching all four seed paths.
type: project
---

# The 15-move catalog of $e_n^{k(n)}$ at B_n short simple is a three-strand braid

**Status:** Type-uniform at B_n short simple, EMPIRICALLY CONFIRMED at B_3 + B_4 + B_5. Born 2026-05-14 dream cycle. B_4 verification 2026-05-15: 0 falsifiers across axiom/commutativity/obstruction tests + exact (9, 12, 7) split. **B_5 verification 2026-05-17: exact (12, 24, 9) split, catalog saturates at max_total=3 like B_3/B_4, no anomalies.** Three non-degenerate rank confirmations + Theorem 5.1 lift = solid type-uniform evidence base.

## Statement

Let $\widetilde{\mathrm{Aug}}_n^{\rm multi} = e_n^{k(n)} = e_n^2$ on the slice $S_n \subset B(\infty)$ at the short simple of $B_n$. As proved in `multiorbit-aug-as-e-k-decomposition.md`, this operator decomposes into $\binom{2n}{2} = n(2n-1)$ distinct net moves indexed by unordered pairs (with repetition) of $2n-1$ $e_n$-primitives:
- For each of the $n-1$ chain orbits: top-to-mid + mid-to-bot primitives (2 each).
- Singleton $\alpha_n$ primitive (1).

The $n(2n-1)$ pairs split into three structural classes:

| Class | Count at B_3 | Count at B_n | Conjectured categorical home | Seed path |
|-------|--------------|--------------|------------------------------|-----------|
| Intra-chain (pair within one chain) | 6 | $\binom{n-1}{1} \cdot 3 = 3(n-1)$ | BGG-Verma single-step differential | **Path 3** |
| Cross-chain (pair from two chains) | 4 | $\binom{n-1}{2} \cdot 4 = 2(n-1)(n-2)$ | Watanabe quartic at iquantum group | **Path 2** |
| Singleton-involving (pair containing $\alpha_n$) | 5 | $2(n-1) + 1$ | Off-slice 2-step coideal complex / Hopf-algebraic boundary | **Path 1 + 4** |

Total: $3(n-1) + 2(n-1)(n-2) + 2(n-1) + 1 = (n-1)(2n-1) + 2(n-1) + 1 = n(2n-1)$. ✓

The whole catalog *sums* to a single operator $e_n^{k(n)}$ whose commutativity with $B_n$ on $S_n$ is the 5-line crystal-axiom theorem — **Path 4 / coideal commutativity**.

## Why this matters

A single combinatorial object ($e_n^2$) that *simultaneously*:
1. Decomposes into pieces matching the three combinatorial homes Rick has been building separately (BGG-Verma, Watanabe quartic, off-slice 2-step).
2. Satisfies the on-slice commutativity that is the q=0 shadow of the coideal-restriction picture (Path 4).
3. Has a type-uniform formula $n(2n-1)$ that ports across all $B_n$.

This is the **first place** all four seed paths meet in an explicit, computable combinatorial decomposition. Before today, the four paths were related by analogy and shared upstream structure (doubly-laced asymmetry, BGG/Hecke duality). Now there is a single object whose pieces *are* the four paths in disguise.

## Concrete tests

1. **B_4 catalog (28 moves). ✅ CONFIRMED 2026-05-15.** Predicted: $3 \cdot 3 = 9$ intra-chain, $2 \cdot 3 \cdot 2 = 12$ cross-chain, $2 \cdot 3 + 1 = 7$ singleton-involving. Total $= 28$. Empirical: exactly 9 + 12 + 7 = 28. All 28 predicted (chain, primitive) pair signatures matched empirical deltas; 0 unmatched on either side. Stable across `max_total` ∈ {3, 4, 5}. On-slice $[e_i^{k(i)}, B_i] = 0$ for $i \in \{1, 2, 3, 4\}$: 0 falsifiers over 10447–13272 partitions each. Off-slice obstruction at $\varepsilon_i = k(i) - 1$: 0 mismatches over ~5000–7000 partitions per case. See `projects/proofs/2026-05-14-multiorbit-aug-b4-result.md`.

2. **Cross-chain ↔ Watanabe quartic.** At $n = 2$ the cross-chain class is empty (only one chain). At $n = 3$ there are exactly 4 cross-chain pairs, matching the 4 nested commutator terms in Watanabe's quartic $B_{2i} = F_{2i} - q[E_{2i-1}, [E_{2i+1}, E_{2i}]_{q^{-1}}]_{q^{-1}} K_{2i}^{-1}$. Predict: at $B_4$ there should be $2 \cdot 3 \cdot 2 = 12$ cross-chain pairs corresponding to a deeper (sextuply?) nested commutator. **Concrete check**: compute Watanabe's $B_{2i}$ at general $n$ and count nested-commutator terms; compare to $2(n-1)(n-2)$.

3. **Intra-chain ↔ BGG-Verma differential.** Each chain orbit at B_n corresponds to a single chain in the Bruhat order; pair of primitives within one chain = one BGG-Verma step ($\binom{2}{2}$ with repetition = 3 per chain → 3 pieces per chain → $3(n-1)$ total). This should correspond directly to BGG single-step differentials in Rick's SU1 v1 framework. **Concrete check**: do the 3 intra-chain pieces per chain exhaust the BGG-Verma single-step moves at the short simple?

4. **Singleton-involving ↔ off-slice obstruction.** The $2(n-1) + 1$ singleton-involving pairs are exactly the moves whose support touches the $\alpha_n$ singleton. The off-slice obstruction $[e_n^k, B_n]\pi = e_n^{k-1}\pi$ at $\varepsilon_n = k - 1$ is "one $\alpha_n$ step short of slice." Conjecture: the off-slice obstruction's orbit-decomposition is *exactly* the singleton-involving sub-catalog. **Concrete check**: extend `b_i_b3.py` off-slice and verify the obstruction decomposes into singleton-class moves only.

## What this gives the program

- **A single object to point at when explaining the unification.** Future papers / talks: "the $n(2n-1)$ catalog of $e_n^2$ at $B_n$ short simple is where the four threads meet."
- **A type-uniform structural prediction.** The three counts should all scale with the same combinatorial formula at every $B_n$. Falsifiable.
- **A concrete bridge to test against Watanabe.** The cross-chain count $2(n-1)(n-2)$ should match the number of nested-commutator terms in Watanabe's iquantum-group generator. Independent algebraic check.
- **A natural categorification target.** 15 net moves at B_3 → 15 sub-objects in an iquantum-group / BGG-Verma categorification. The categorification must respect the 6 / 4 / 5 split.

## Cross-references

- `connections/multiorbit-aug-as-e-k-decomposition.md` — primary result; this connection enriches the "categorical home" subsection.
- `connections/coideal-commutativity-on-slice-B2-PROVED.md` — Path 4 base.
- `connections/aug-tilde-as-bgg-differential.md` — Path 3.
- `connections/coideal-subalgebra-as-aug-tilde-home.md` — Path 2.
- `connections/off-slice-obstruction-as-2-step.md` — Path 1 (Hopf-derived boundary).
- `topics/path4-coproduct-crystal.md` — central thread.
- Watanabe arXiv:2509.00853 — quartic iquantum-group generator.
- Chen-Lu-Pan-Ruan-Wang arXiv:2601.00524 — iHopf algebra algebraic home (newly identified browse 5).

## Caveats

- ~~The intra-chain / cross-chain / singleton split is a hand-classification at B_3. Need to verify the same partition holds at B_4.~~ **RESOLVED 2026-05-15: confirmed at B_4 with 0 mismatched moves.** Type-uniform claim now has 2 ranks of empirical support; suggests pursuing a structural (not just empirical) proof of the type-uniform decomposition.
- The Watanabe-quartic ↔ cross-chain identification is *count-level* at B_3 (4 = 4). The structural correspondence (which quartic term ↔ which cross-chain pair) is not yet pinned down.
- The off-slice ↔ singleton-involving identification is conjectural; off-slice multi-orbit decomposition has not been computed.
- The B_n long-simple version (where $k(i) = 1$) is qualitatively simpler; the multi-orbit / three-strand structure may collapse. Worth a separate look.

## Risk

~~If the B_4 verification fails the 9 / 12 / 7 prediction, the three-strand structure is rank-specific and the unification claim weakens to "B_3 coincidence."~~ **RESOLVED 2026-05-15: B_4 confirms.** Risk has shifted: now the question is whether the type-uniform structural *proof* exists, and whether the categorical-home identifications (Watanabe quartic ↔ cross-chain, BGG ↔ intra-chain, off-slice ↔ singleton) are real correspondences or numerical coincidences across two ranks. Three-rank confirmation at B_5 would help but is now ancillary; the structural proof is the right next move.
