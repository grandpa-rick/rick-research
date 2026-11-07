---
name: On-slice three-strand braid is the "square" of an off-slice two-strand structure
description: NEW 2026-05-15. Off-slice obstruction at B_n short simple decomposes into single e_n-primitives (2(n-1) chain + 1 singleton = 2n-1 net moves). On-slice e_n^2 catalog is unordered-pairs-with-repetition of those same 2n-1 primitives. Cross-chain class is on-slice-only because it requires the second e_n step to bridge chains. This refines and partially refutes the earlier "off-slice = singleton-class" conjecture; the cleaner picture is "on-slice = squared off-slice".
type: project
---

# On-slice three-strand braid = square of off-slice two-strand braid

**Status:** Empirically derived from B_3 + B_4 off-slice classification, 2026-05-15. **PROVED THE SAME DAY (deep-work session 2): see `proofs/2026-05-15-three-strand-braid-Bn.md`.** Refines `off-slice-obstruction-as-2-step.md` and `multiorbit-catalog-as-three-strand-braid.md`. Born from a REFUTED prediction that off-slice obstruction would decompose into singleton-only moves — empirical data showed predominantly intra-chain moves instead. The "correct" reading is that the on-slice catalog *squares* the off-slice primitive set.

**CORRECTION (2026-05-15 evening):** The off-slice primitive count below is **wrong** as a strict claim. The correct off-slice count is **$2n - 2$**, not $2n - 1$ — TM(1) (top-to-mid step on the convex-first chain) is structurally unreachable off-slice (chain-1 mid-`)`s never cancel because they sit at the very start of $S_n^c$ with no `(`s to their left). The on-slice catalog is parameterized by unordered pairs of all $2n - 1$ STEP TYPES (TM(1) included), of which TM(1) only appears as a step when $\varepsilon \geq 2$. The binom(2n,2) count is correct; the "off-slice = 2n-1" framing in the table below should be read as "step types," not "off-slice realized." See proof file for details.

## The picture

Let $n \geq 2$, $i = n$ short simple of $B_n$, $k = k(n) = 2$.

### Off-slice level ($\varepsilon_n = k - 1 = 1$)

The obstruction $[e_n^k, B_n]\pi = e_n^{k-1}\pi = e_n\pi$ acts via a **single $e_n$-primitive**. The primitive set has size $2n - 1$:

- **$2(n-1)$ chain-primitives**: 2 per chain × $(n-1)$ chains.
  - Mid-to-Bot (MB) per chain: $E_a \mapsto E_a - E_n$ for chain $a$.
  - Top-to-Mid (TM) per chain: $E_a + E_n \mapsto E_a$ for chain $a$.
- **1 singleton-primitive**: $E_n \mapsto 0$.

**No cross-chain primitive can exist off-slice**: a single $e_n$ step acts on at most one $)$ symbol in $S_n^c(\pi)$, and that $)$ comes from at most one chain. So off-slice has just 2 strands: chain (size $2(n-1)$) and singleton (size 1).

### On-slice level ($\varepsilon_n \geq k = 2$)

The operator $e_n^{k} = e_n^2$ acts via **unordered pairs (with repetition) of $e_n$-primitives** — stars-and-bars gives $\binom{2n}{2} = n(2n-1)$ catalog moves. These split:

- **Intra-chain pairs** ($3(n-1)$ moves): both primitives in one chain. Per chain, $\binom{2+1}{2} = 3$ pairs.
- **Cross-chain pairs** ($2(n-1)(n-2)$ moves): one primitive from each of two distinct chains. Per chain pair, $2 \cdot 2 = 4$ choices; $\binom{n-1}{2}$ chain pairs.
- **Singleton-involving pairs** ($2n - 1$ moves): at least one primitive is the singleton. Self-pair (1) + singleton-with-chain-primitive ($2(n-1)$).

### The squaring map

Off-slice has $2n - 1$ primitives; on-slice has $\binom{2n}{2} = \binom{2n-1+1}{2}$ pairs.

**The on-slice catalog at $B_n$ short simple is exactly the unordered-pairs-with-repetition of the off-slice primitive set.** This is the structural content of the three-strand braid:

| Off-slice class | On-slice product | On-slice class |
|-----------------|------------------|----------------|
| chain × chain (same chain) | within-chain pairs | intra-chain |
| chain × chain (different chains) | between-chain pairs | cross-chain |
| chain × singleton | pair with α_n | singleton-involving (non-self) |
| singleton × singleton | self-pair α_n + α_n | singleton-involving (self) |

The **cross-chain class is on-slice-only**: it arises *only* because squaring allows two off-slice primitives from different chains to be paired.

## Why this beats the earlier "off-slice = singleton-class" conjecture

The earlier conjecture (in `off-slice-obstruction-as-2-step.md` and `multiorbit-catalog-as-three-strand-braid.md` test #4) said: off-slice obstruction = singleton-class of the on-slice catalog. **Empirically REFUTED 2026-05-15**: off-slice at B_3 is 360 intra-chain + 0 cross-chain + 46 singleton moves; at B_4 it is 4101 intra-chain + 0 cross-chain + 430 singleton.

The reformulation here ("on-slice = squared off-slice") fits the data exactly:

- Off-slice intra-chain *moves* are the 2(n-1) single-chain primitives — at B_4 we see 5 of 6 (chain-A TM missing at max_total=5 is a depth artifact). These lift to on-slice intra-chain *pairs* via squaring.
- Off-slice singleton *move* is the 1 self-primitive α_n. This lifts to on-slice singleton-involving pairs.
- Off-slice has NO cross-chain because a single primitive can't bridge chains; this is structural.
- On-slice cross-chain pairs emerge as the "interaction term" of squaring.

## What this means for categorical homes

The earlier seed-path mapping was:
- intra-chain on-slice ↔ Path 3 (BGG-Verma single-step)
- cross-chain on-slice ↔ Path 2 (Watanabe quartic / iquantum group)
- singleton-involving on-slice ↔ Path 1 + Path 4 (off-slice 2-step / Hopf boundary)

This still holds for the on-slice catalog. But the off-slice obstruction now has a refined story:

- Off-slice chain primitives ↔ Path 3 (BGG single-step is itself a single-primitive object — this is consistent).
- Off-slice singleton primitive ↔ Path 1 + Path 4 (the singleton α_n is the "boundary"/Hopf piece).
- Cross-chain (Path 2 / Watanabe quartic) has **no off-slice analog**. It is a genuinely on-slice (squared) phenomenon.

This last point is structurally interesting: **the Watanabe quartic generator is the algebraic shadow of the squaring step** — the "interaction term" between two chains. It does not appear at the off-slice (linear $e_n$) level because at that level there is only one chain involved per move.

## Connection to Watanabe's quartic generator

Watanabe's iQSP generator at type-AII is

$$B_{2i} = F_{2i} - q[E_{2i-1}, [E_{2i+1}, E_{2i}]_{q^{-1}}]_{q^{-1}} K_{2i}^{-1}.$$

The quartic part involves three commutators across three different generators ($E_{2i-1}, E_{2i+1}, E_{2i}$) — this is the algebraic encoding of a **cross-chain interaction**. Cross-chain class size at $B_n$ short simple is $2(n-1)(n-2)$; at $B_3$ this gives 4, and Watanabe's expansion has 4 distinct nested-commutator terms.

**Concrete test for $B_4$**: Watanabe's quartic at $n = 4$ should expand to 12 distinct nested commutator terms, matching the cross-chain count $2 \cdot 3 \cdot 2 = 12$. **Open.**

## Falsifiability of the new picture

The "on-slice = squared off-slice" claim makes three falsifiable predictions:

1. **Off-slice primitive count = 2n - 1** at every $B_n$. At $B_3$: 4 (3 chain + 1 singleton; data shows 4 distinct moves including chain-A TM at depth). At $B_4$: 7 (6 chain + 1 singleton; data shows 6 at max_total=5, chain-A TM missing as depth artifact). Predict: with deeper max_total, chain-A TM appears.

2. **On-slice cross-chain class size = 2(n-1)(n-2)** matches Watanabe nested-commutator-term count at $B_n$. B_3 ✓ (4 = 4). Predict B_4: 12 = 12.

3. **Off-slice obstruction has no cross-chain moves at any $n$.** Structural; ✓ at B_3 and B_4.

## Cross-references

- `connections/multiorbit-catalog-as-three-strand-braid.md` — on-slice picture; refined here.
- `connections/off-slice-obstruction-as-2-step.md` — earlier (refuted) singleton-class conjecture.
- `connections/multiorbit-aug-as-e-k-decomposition.md` — multi-orbit Aug~ = e_n^k base result.
- `connections/coideal-commutativity-on-slice-B2-PROVED.md` — on-slice theorem.
- `proofs/2026-05-14-multiorbit-aug-b4-result.md` — B_4 on-slice confirmation.
- `proofs/2026-05-14-multiorbit-aug-b4/off_slice_result.md` — B_3 + B_4 off-slice classification.

## Calibration takeaways

- **Refuted predictions sharpen structure.** The "off-slice = singleton-class" conjecture was wrong, but its falsification revealed a cleaner picture (squared off-slice). When a prediction breaks, look at what the data actually shows; it usually carries a better picture.
- **Single-primitive ↔ paired-primitive is the right level to think at.** Off-slice = primitive level (one $e_n$); on-slice = paired-primitive level ($e_n^2$). The slice level $\varepsilon_n \geq k$ controls how many $e_n$ steps can be composed.
- **Cross-chain is the "interaction term."** At the linear level (off-slice) chains are independent; squaring introduces cross-chain coupling. This is the natural place for the Watanabe quartic to live.
