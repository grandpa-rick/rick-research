# Multi-orbit Aug~ at B_3: structure of $e_3^{k(3)}$ as a Weyl-orbit-pair sum

**Date:** 2026-05-14 (deep work session continuation).
**Author:** Rick.
**Status:** Theorem (B_3, short simple). Computational verification through total
content ≤ 6 (3082 partitions on slice, 0 falsifiers). Type-uniform conjecture
for $B_n$ short simple: catalog has $n(2n-1)$ moves; proof of commutativity is
crystal-axiom 5-line and ports unchanged.

---

## 1. Setting

$\mathfrak{g} = \mathfrak{so}_7$ of type $B_3$. Simple roots
$\alpha_1 = e_1 - e_2$ (long), $\alpha_2 = e_2 - e_3$ (long),
$\alpha_3 = e_3$ (short). At the short simple, $k(3) = 2$ (the $s_3$-chain
$\{e_p - e_3, e_p, e_p + e_3\}$ has length 3).

The coideal generator at the $q=0$ crystal limit is $B_i := e_i + f_i$.

We work on $\mathrm{Kp}(\infty) = B(\infty)$ with the CST bracketing-sequence
$e_i, f_i$ (Criswell–Salisbury–Tingley arXiv:1708.04311 Def. 2.14).

The depth-$k$ slice for $i = 3$ is
$$S_3 := \{\pi \in \mathrm{Kp}(\infty) : \varepsilon_3(\pi) \geq 2\}.$$

## 2. Main theorem

**Theorem 1 (Multi-orbit Aug~_3 commutes with $B_3$ on $S_3$).**
*Define $\widetilde{\mathrm{Aug}}_3^{\rm multi} := e_3^{k(3)} = e_3^2$ as an
operator on $\mathbb{Z}[\mathrm{Kp}(\infty)]$, restricted to $S_3$. Then*
$$[\widetilde{\mathrm{Aug}}_3^{\rm multi}, B_3]\pi = 0 \quad \forall\, \pi \in S_3.$$

**Proof.** Standard 5-line crystal-axiom argument, identical to B_2 and to the
on-slice statement of `2026-05-14-coideal-commutativity-B3.md`:
$$[e_3^2, B_3] = [e_3^2, e_3 + f_3] = [e_3^2, f_3].$$
For $\pi \in S_3$ (i.e., $\varepsilon_3(\pi) \geq 2$):
- $e_3^2(f_3 \pi) = e_3 (e_3 f_3 \pi) = e_3(\pi) = e_3 \pi$ using the axiom
  $e_3 f_3 = \mathrm{id}$.
- $f_3(e_3^2 \pi) = e_3(\pi)$ using the inverse axiom $f_3 e_3 = \mathrm{id}$
  on $\{\varepsilon_3 \geq 1\}$, applied at $e_3 \pi$ where
  $\varepsilon_3(e_3\pi) = \varepsilon_3(\pi) - 1 \geq 1$.

Hence the two evaluations of $[e_3^2, f_3]\pi$ agree and the commutator
vanishes. $\square$

**Remark.** The theorem makes no use of the orbit-class structure of $\pi$ —
the proof is *orbit-agnostic*. The orbit structure enters only in the
*description* of what $\widetilde{\mathrm{Aug}}_3^{\rm multi}$ does on $\pi$,
which is the content of §3.

## 3. Multi-orbit structure: $e_3^2$ as a sum over Weyl-orbit-pair moves

This is the substantive new content at $B_3$ compared to $B_2$.

### 3.1 The $e_3$-primitive moves

A single $e_3$-step at $B_3$ acts on $\pi \in \mathrm{Kp}(\infty)$ via the
CST bracketing rule, picking the rightmost $)$-bracket in cancelled
$S_3(\pi)$ and decrementing the associated root by one $\alpha_3$. The
distinct $e_3$-primitives — atomic actions of $e_3$ — are determined by the
$s_3$-orbits on $\Phi^+(B_3)$:

| Primitive | Action on multiplicities | $\alpha_3$-coefficient drops by |
|---|---|---|
| $p_{A,T}$ (chain A, top→mid) | $c_{e_1+e_3} \mathrel{-}= 1$, $c_{e_1} \mathrel{+}= 1$ | 1 |
| $p_{A,M}$ (chain A, mid→bot) | $c_{e_1} \mathrel{-}= 1$, $c_{e_1-e_3} \mathrel{+}= 1$ | 1 |
| $p_{B,T}$ (chain B, top→mid) | $c_{e_2+e_3} \mathrel{-}= 1$, $c_{e_2} \mathrel{+}= 1$ | 1 |
| $p_{B,M}$ (chain B, mid→bot) | $c_{e_2} \mathrel{-}= 1$, $c_{e_2-e_3} \mathrel{+}= 1$ | 1 |
| $p_{S}$ (singleton, simple) | $c_{e_3} \mathrel{-}= 1$ | 1 |

There are **five $e_3$-primitives** at $B_3$, organised into 2 chain orbits
(each with 2 primitives, one per length-3-chain step) and 1 singleton
($\alpha_3 = e_3$).

Each primitive realises weight change $-\alpha_3$.

### 3.2 The 15 $e_3^2$ net moves

Composing two primitives in sequence — applied via the bracketing rule —
yields a net move with weight change $-2\alpha_3$. As an unordered multiset
(the bracketing rule may select primitives in either order, but the net effect
on multiplicities is symmetric), the pairs $(p, q)$ with $p, q$ ranging over
the 5 primitives give

$$\binom{5+1}{2} = \binom{6}{2} = 15$$

distinct net move types:

| Move | Primitive pair | Multiplicity change |
|---|---|---|
| $A_{TB}$ | $\{p_{A,T}, p_{A,M}\}$ | $c_{e_1+e_3} \mathrel{-}= 1$, $c_{e_1-e_3} \mathrel{+}= 1$ (top-to-bottom swap) |
| $A_{TM^2}$ | $\{p_{A,T}, p_{A,T}\}$ | $c_{e_1+e_3} \mathrel{-}= 2$, $c_{e_1} \mathrel{+}= 2$ |
| $A_{MB^2}$ | $\{p_{A,M}, p_{A,M}\}$ | $c_{e_1} \mathrel{-}= 2$, $c_{e_1-e_3} \mathrel{+}= 2$ |
| $B_{TB}$ | $\{p_{B,T}, p_{B,M}\}$ | $c_{e_2+e_3} \mathrel{-}= 1$, $c_{e_2-e_3} \mathrel{+}= 1$ |
| $B_{TM^2}$ | $\{p_{B,T}, p_{B,T}\}$ | $c_{e_2+e_3} \mathrel{-}= 2$, $c_{e_2} \mathrel{+}= 2$ |
| $B_{MB^2}$ | $\{p_{B,M}, p_{B,M}\}$ | $c_{e_2} \mathrel{-}= 2$, $c_{e_2-e_3} \mathrel{+}= 2$ |
| $AB_{TT}$ | $\{p_{A,T}, p_{B,T}\}$ | $c_{e_1+e_3} \mathrel{-}= 1$, $c_{e_1} \mathrel{+}= 1$, $c_{e_2+e_3} \mathrel{-}= 1$, $c_{e_2} \mathrel{+}= 1$ |
| $AB_{TM}$ | $\{p_{A,T}, p_{B,M}\}$ | $c_{e_1+e_3} \mathrel{-}= 1$, $c_{e_1} \mathrel{+}= 1$, $c_{e_2} \mathrel{-}= 1$, $c_{e_2-e_3} \mathrel{+}= 1$ |
| $AB_{MT}$ | $\{p_{A,M}, p_{B,T}\}$ | $c_{e_1} \mathrel{-}= 1$, $c_{e_1-e_3} \mathrel{+}= 1$, $c_{e_2+e_3} \mathrel{-}= 1$, $c_{e_2} \mathrel{+}= 1$ |
| $AB_{MM}$ | $\{p_{A,M}, p_{B,M}\}$ | $c_{e_1} \mathrel{-}= 1$, $c_{e_1-e_3} \mathrel{+}= 1$, $c_{e_2} \mathrel{-}= 1$, $c_{e_2-e_3} \mathrel{+}= 1$ |
| $E_{S^2}$ | $\{p_{S}, p_{S}\}$ | $c_{e_3} \mathrel{-}= 2$ |
| $AE_T$ | $\{p_{A,T}, p_{S}\}$ | $c_{e_1+e_3} \mathrel{-}= 1$, $c_{e_1} \mathrel{+}= 1$, $c_{e_3} \mathrel{-}= 1$ |
| $AE_M$ | $\{p_{A,M}, p_{S}\}$ | $c_{e_1} \mathrel{-}= 1$, $c_{e_1-e_3} \mathrel{+}= 1$, $c_{e_3} \mathrel{-}= 1$ |
| $BE_T$ | $\{p_{B,T}, p_{S}\}$ | $c_{e_2+e_3} \mathrel{-}= 1$, $c_{e_2} \mathrel{+}= 1$, $c_{e_3} \mathrel{-}= 1$ |
| $BE_M$ | $\{p_{B,M}, p_{S}\}$ | $c_{e_2} \mathrel{-}= 1$, $c_{e_2-e_3} \mathrel{+}= 1$, $c_{e_3} \mathrel{-}= 1$ |

These 15 net moves partition $S_3$ into 15 sub-slices
$\{S_3^{(M)}\}_{M \in \text{moves}}$ such that
$\pi \in S_3^{(M)} \iff e_3^2(\pi) = M\cdot\pi$.

### 3.3 Sub-slice decomposition

Each sub-slice $S_3^{(M)}$ has a clean multiplicity-based characterisation
visible from the CST bracketing structure. Counting at max total content
$\leq 5$ (slice size $|S_3| = 1146$):

| Move $M$ | $|S_3^{(M)}|$ | Sample $\pi \in S_3^{(M)}$ |
|---|---|---|
| $A_{TB}$ | 165 | $\pi = (e_1 + e_3)$ |
| $A_{TM^2}$ | 88 | $\pi = 2(e_1 + e_3)$ |
| $A_{MB^2}$ | 156 | $\pi = 2 e_1$ |
| $B_{TB}$ | 149 | $\pi = (e_2 + e_3)$ |
| $B_{TM^2}$ | 125 | $\pi = 2(e_2 + e_3)$ |
| $B_{MB^2}$ | 105 | $\pi = 2 e_2$ |
| $AB_{TT}$ | 13 | $\pi = (e_1 + e_3) + e_1 + (e_2 + e_3)$ |
| $AB_{TM}$ | 69 | $\pi = (e_1 + e_3) + e_2$ |
| $AB_{MT}$ | 25 | $\pi = e_1 + (e_2 + e_3)$ |
| $AB_{MM}$ | 18 | $\pi = e_1 + 2 e_2$ |
| $E_{S^2}$ | 94 | $\pi = 2 e_3$ |
| $AE_T$ | 35 | $\pi = (e_1 + e_3) + e_3$ |
| $AE_M$ | 16 | $\pi = e_1 + 2 e_3$ |
| $BE_T$ | 75 | $\pi = (e_2 + e_3) + e_3$ |
| $BE_M$ | 13 | $\pi = e_2 + 2 e_3$ |

Total = 1146. ✓

The sub-slice $S_3^{(A_{TB})}$ is the *literal-match sub-slice* of
`coideal-commutativity-B3.md`'s single-orbit chain-A Aug~_{3,1}: it is exactly
the set where the single chain-A top-to-bottom orbit-swap coincides with
$e_3^2$ as a function on $\mathrm{Kp}(\infty)$. Symmetrically $S_3^{(B_{TB})}$.

The remaining 13 sub-slices are the *new content at $B_3$* — they appear only
because chain length is 3, allowing intra-chain doubling and cross-chain
mixing within a single $e_3^2$ step.

### 3.4 Decomposition by chain-support orbit class

Reorganising the 15 sub-slices by chain-support orbit class of $\pi$ (where
"chain A" means any of $\{c_{e_1\pm e_3}, c_{e_1}\}$ is positive, etc.):

| Class | $|$ class $|$ | Moves appearing |
|---|---|---|
| A only | 226 | $A_{TB}, A_{TM^2}, A_{MB^2}, AE_T, AE_M, E_{S^2}$ |
| B only | 226 | $B_{TB}, B_{TM^2}, B_{MB^2}, BE_T, BE_M, E_{S^2}$ |
| AB | 674 | all 15 except sometimes $E_{S^2}$ alone |
| neither | 20 | $E_{S^2}$ |

This reproduces the 4-class statement of `coideal-commutativity-B3.md` §4
with the refined 15-move decomposition.

## 4. Comparison with B_2 (3 primitives, 6 moves)

At $B_2$ the short simple is $\alpha_2 = e_2$ with $k(2) = 2$. The single
non-trivial $s_2$-chain is $\{e_1 - e_2, e_1, e_1 + e_2\}$ (length 3). The
$e_2$-primitive set has 3 elements:
- $p_T$: chain top-to-mid ($e_1 + e_2 \to e_1$).
- $p_M$: chain mid-to-bot ($e_1 \to e_1 - e_2$).
- $p_S$: singleton ($e_2 \to 0$).

Unordered pairs (with repetition): $\binom{3+1}{2} = 6$ net moves at $B_2$:

| Move | Pair |
|---|---|
| top-to-bot swap | $\{p_T, p_M\}$ |
| top-to-mid² | $\{p_T, p_T\}$ |
| mid-to-bot² | $\{p_M, p_M\}$ |
| singleton² | $\{p_S, p_S\}$ |
| top-mid + singleton | $\{p_T, p_S\}$ |
| mid-bot + singleton | $\{p_M, p_S\}$ |

These 6 are exactly the moves observed by `verify_catalog.py` at $B_2$.

So the move count follows the *type-uniform formula*

$$|\text{$e_n^2$ moves}| = \binom{p_n + 1}{2} = \frac{p_n (p_n + 1)}{2}, \qquad p_n = 2(n-1) + 1 = 2n - 1,$$

evaluating to $6$ at $n=2$ and $15$ at $n=3$.

## 5. Type-uniform conjecture at $B_n$ short simple

**Conjecture (Type-uniform multi-orbit Aug~ at $B_n$, short simple).**
*Let $i = n$, the short simple of $B_n$ (with $k(n) = 2$). Define
$\widetilde{\mathrm{Aug}}_n^{\rm multi} := e_n^{k(n)} = e_n^2$ on*
$S_n = \{\pi : \varepsilon_n(\pi) \geq 2\}$. *Then $[\widetilde{\mathrm{Aug}}_n^{\rm multi}, B_n]\pi = 0$
on $S_n$, with the same 5-line crystal-axiom proof. The action of
$\widetilde{\mathrm{Aug}}_n^{\rm multi}$ on $S_n$ is one of $\binom{2n}{2} = n(2n-1)$
distinct net move types, parametrised by unordered pairs (with repetition) of
$e_n$-primitives. The $e_n$-primitive set has $2n-1$ elements: 2 primitives
per $s_n$-orbit chain (length-3, partner $p \in \{1, ..., n-1\}$) plus 1
singleton.*

The proof of commutativity is type-uniform — it uses only the crystal axioms
$e_n f_n = \mathrm{id}$ and $f_n e_n = \mathrm{id}$ on the slice, which hold
at all ranks.

The substantive content of the conjecture is the **15** at $B_3$, **28** at
$B_4$, … $n(2n-1)$ at $B_n$ — and the assertion that each net move arises
on a non-empty sub-slice.

A B_4 sanity check is the natural next computational test. Crystal-axiom
verification on $B_4$ Kp(∞) would be the first step (per Rick's calibration:
*verify axioms before testing downstream*).

## 6. Why $\widetilde{\mathrm{Aug}}_n^{\rm multi} = e_n^{k(n)}$ is the "right"
multi-orbit Aug~

The B_2 picture (single-orbit Aug~) suggested that Aug~ at higher rank should
be some natural orbit-swap-style operator. The B_3 computation refutes this at
the level of single orbit-swap (per
`coideal-commutativity-B3.md`'s falsification of single-orbit
commutativity).

The resolution is structural: the genuinely multi-orbit object at B_n short
simple **is** $e_n^{k(n)}$ itself, written via the orbit-pair catalog above.
The "many orbit-swaps" $\widetilde{\mathrm{Aug}}_{3,\mathcal{O}}$ are exactly
the chain-top-to-bottom move ($A_{TB}$ or $B_{TB}$) for each chain
$\mathcal{O}$; they are 2 of the 15 net moves at $B_3$. The other 13 net moves
involve intra-chain doubling, cross-chain mixing, and singleton interaction —
all of which are required for $e_3^2$ to act consistently on $S_3$ via the
CST bracketing rule.

The commutativity with $B_3$ follows from the crystal axiom on the slice. No
extra structure is needed.

**Note on the failed candidate $\widetilde{\mathrm{Aug}}_3 := \widetilde{\mathrm{Aug}}_{3,A} + \widetilde{\mathrm{Aug}}_{3,B}$.** The naive sum of
single-orbit operators (candidate C1 in PROVE.md) fails commutativity with
$B_3$ on $S_3$ (verified: 305 of 370 partitions at max=4 have non-zero
commutator). The structural reason is that this candidate only captures the
2 chain-top-to-bottom move types ($A_{TB}$, $B_{TB}$) — it misses the other
13. Adding the missing 13 simply reconstructs $e_3^2$.

## 7. Connection to type-AII iquantum-group picture

The Watanabe quartic formulation (arXiv:2509.00853) at type-AII even nodes
has 4 nested commutator terms. The B_3 short-simple multi-orbit Aug~ has
15 = $\binom{6}{2}$ net moves, decomposed into:
- 3 + 3 = 6 pure chain moves (2 chains × 3 intra-chain pair types).
- 4 cross-chain pairs.
- 1 + 2 + 2 = 5 singleton + chain moves.

The "quartic shadow" hypothesis (PROVE.md C4) would predict 4 cross-chain
mixings = 4 nested commutator terms. The 4 cross-chain mixings are
$\{AB_{TT}, AB_{TM}, AB_{MT}, AB_{MM}\}$, matching the structural prediction.
The other 11 are intra-chain or singleton-involving and aren't quartic. This
suggests the iquantum-group quartic captures only the cross-chain part of
Aug~ at $B_n$; the intra-chain part requires separate categorical
structure (likely from the BGG-Verma chain-product, per
`aug-tilde-as-bgg-differential.md`).

## 8. Computational verification

Implemented at:
- `proofs/2026-05-14-multiorbit-aug-b3/explore_e3sq_v2.py` — move catalog.
- `proofs/2026-05-14-multiorbit-aug-b3/verify_catalog.py` — verifies 15 moves
  appear at $B_3$, 6 at $B_2$, stable across max_total ∈ {4, 5, 6}.
- `proofs/2026-05-14-multiorbit-aug-b3/characterize_moves.py` — sub-slice
  decomposition $|S_3^{(M)}|$ per move.
- `proofs/2026-05-14-multiorbit-aug-b3/multiorbit_candidates.py` —
  refutation of the naive sum candidate.

Summary at max_total = 6:
- $B_3$, slice size 3082, 15 distinct net moves.
- $B_2$, slice size 144, 6 distinct net moves.

## 9. What's open

1. **$B_4$ confirmation.** Expected 28 net moves and a clean type-uniform
   verification. Requires only the $B_4$ analog of `b_i_b3.py` (axiom check
   FIRST, then on-slice commutativity, then move catalog).

2. **Long-simple multi-orbit.** This note covered only the short simple
   ($i = n$, $k = 2$). The long simples ($i < n$, $k = 1$) have multiple
   chain orbits at $B_3$ too (3 each for $i = 1, 2$), but $k(i) = 1$ means
   $e_i^1 = e_i$ acts via a *single* primitive, so the multi-orbit
   decomposition is into $2n - 3$ primitives at $B_n$ long simple $i$. The
   commutativity $[e_i, B_i] = e_i + 0 = e_i^0 = 1$ off-slice, $0$ on-slice:
   same crystal-axiom proof.

3. **Categorical interpretation.** The 15 moves correspond to 15 sub-objects
   in a categorification scheme. The 6 pure-chain ones are intra-chain BGG
   differentials. The 4 cross-chain ones are iquantum-group-quartic-like.
   The 5 singleton-involving ones are "boundary" terms.

4. **Aug~ as crystal-extension off-slice.** Off-slice ($\varepsilon_3 < 2$),
   the commutator $[e_3^2, B_3]\pi = e_3^{k-1}\pi = e_3 \pi$ (an explicit
   obstruction). The multi-orbit decomposition off-slice is open.

## 10. Cross-references

- `2026-05-14-coideal-commutativity-B3.md`: on-slice $[e_3^2, B_3] = 0$
  proof and 4-class orbit-classification.
- `connections/coideal-commutativity-on-slice-B2-PROVED.md`: B_2 reference.
- `connections/aug-tilde-as-bgg-differential.md`: SU1 REDUCED-multiset
  uniqueness at B_3.
- CST: arXiv:1708.04311.
- Watanabe: arXiv:2509.00853.

---

*Verified across $B_3$ slice ($|S_3| = 3082$ at max_total = 6, 0 falsifiers).
The catalog is stable across max_total ∈ {4, 5, 6}.*
