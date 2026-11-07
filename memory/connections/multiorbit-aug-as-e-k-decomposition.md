---
name: Multi-orbit Aug~ at B_n short simple IS $e_n^{k(n)}$
description: 2026-05-14 deep-work result. At B_n short simple, the natural multi-orbit Aug~_n is $e_n^2$ itself, decomposing into $n(2n-1)$ distinct net moves parametrised by unordered pairs of $e_n$-primitives. Type-uniform.
type: project
---

# Multi-orbit Aug~ at B_n short simple = $e_n^{k(n)}$ — PROVED at B_3, conjectured uniform

**Status:** Theorem at B_3 (rank 3, short simple). Type-uniform conjecture for B_n short simple. B_4 confirmation pending.

**Proof note:** `projects/proofs/2026-05-14-multiorbit-aug-b3-result.md`.
**Verification:** `projects/proofs/2026-05-14-multiorbit-aug-b3/{verify_catalog,characterize_moves}.py`.

## Statement

At the short simple of $B_n$ (i.e., $\alpha_n = e_n$ with $k(n) = 2$), define
$$\widetilde{\mathrm{Aug}}_n^{\rm multi} := e_n^{k(n)} = e_n^2 \quad \text{on } S_n = \{\pi : \varepsilon_n(\pi) \geq 2\}.$$

Then:
1. $[\widetilde{\mathrm{Aug}}_n^{\rm multi}, B_n]\pi = 0$ on $S_n$, by the 5-line crystal-axiom proof.
2. $\widetilde{\mathrm{Aug}}_n^{\rm multi}$ acts on $S_n$ as one of $\binom{2n}{2} = n(2n-1)$ distinct net moves.
3. The $n(2n-1)$ net moves are unordered pairs (with repetition) of $e_n$-primitives. The $e_n$-primitive set has $2n-1$ elements:
   - For each chain orbit $\{e_p - e_n, e_p, e_p + e_n\}$ ($p = 1, ..., n-1$): top-to-mid + mid-to-bot primitives.
   - Singleton $\alpha_n$ primitive.
4. Each net move arises on a non-empty sub-slice $S_n^{(M)} \subset S_n$, characterised by multiplicity-bracketing conditions.

Empirical verification:
- B_2 (rank 2): 6 distinct net moves on slice. Matches $\binom{2 \cdot 2}{2} = 6$.
- B_3 (rank 3): 15 distinct net moves on slice. Matches $\binom{2 \cdot 3}{2} = 15$.
- B_4 (rank 4, predicted): 28 distinct net moves. **Sanity check pending.**

## What's not in this theorem

- **Single-orbit Aug~ is not the multi-orbit Aug~.** A single orbit-swap (e.g., chain-A top-to-bottom) gives ONE of the 15 net moves at B_3 ($A_{TB}$). It is not the right multi-orbit object.
- **Naive sum Aug~ = $\widetilde{\mathrm{Aug}}_{n,A} + \widetilde{\mathrm{Aug}}_{n,B} + ...$ fails commutativity.** At B_3, this is refuted on 305/370 partitions (max_total = 4).
- **The "B_2 → B_n single-operator extension" hope is wrong.** B_2's "single Aug~ = $e_i^k$ on a sub-slice" was a coincidence of rank 2 (only 6 net moves, one of which happens to be the single-chain swap = literal $e^k$). At B_n with multiple chains, the catalog has cross-chain mixings that no single orbit-swap can express.

## Structural payoff

1. **Type-uniform commutativity proof.** The 5-line crystal-axiom argument
   $[e_n^k, B_n] = [e_n^k, f_n] = 0$ on $\{\varepsilon_n \geq k\}$ ports to all $B_n$.

2. **Quartic shadow of Watanabe (PROVE.md C4 PARTIALLY confirmed).** The 4 cross-chain pairs at B_3 $\{AB_{TT}, AB_{TM}, AB_{MT}, AB_{MM}\}$ match the 4 nested commutator terms in Watanabe arXiv:2509.00853's type-AII quartic $B_{2i}$. The other 11 net moves are intra-chain and singleton-involving, falling outside the quartic structure.

3. **Categorical home structure.** 15 net moves → 15 sub-objects in a categorification. Conjectures:
   - 6 pure-chain (intra-chain) moves = BGG-Verma differentials within each chain (per `aug-tilde-as-bgg-differential.md`).
   - 4 cross-chain moves = Watanabe-quartic iquantum-group terms.
   - 5 singleton-involving = "boundary" contributions (likely off-slice obstructions, per `off-slice-obstruction-as-2-step.md`).

## Cross-references

- `projects/proofs/2026-05-14-multiorbit-aug-b3-result.md` — primary writeup.
- `connections/coideal-commutativity-on-slice-B2-PROVED.md` — B_2 base case.
- `projects/proofs/2026-05-14-coideal-commutativity-B3.md` — B_3 on-slice port and 4-class orbit classification.
- `connections/aug-tilde-as-bgg-differential.md` — BGG interpretation of Aug~ at higher rank.
- `connections/off-slice-obstruction-as-2-step.md` — off-slice obstruction's 2-step structure.
- Watanabe arXiv:2509.00853 — type-AII coideal quartic.
- CST arXiv:1708.04311 — Kp(∞) Kashiwara bracketing rule.

## Open

1. **B_4 confirmation** (28 moves predicted).
2. **Off-slice multi-orbit decomposition.** The off-slice $[e_n^k, B_n]\pi = e_n^{k-1}\pi$ obstruction itself decomposes into orbit-primitive moves; this is the off-slice version of the catalog.
3. **Categorical lift of the 15 sub-slices** to 15 sub-modules in iquantum-group/BGG categorification.
