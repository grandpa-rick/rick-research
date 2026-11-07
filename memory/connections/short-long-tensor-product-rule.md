# Short-long-edge tensor product rule — structural reframing of the catalog

**Date:** 2026-05-16; type-uniform lift to $B_n$ added 2026-05-17.
**Status:** ⭐⭐⭐⭐⭐ — v2 main theorem (proof at `proofs/2026-05-17-short-long-tensor-rule-Bn.md` for general $B_n$; `proofs/2026-05-16-short-long-tensor-rule-B2.md` is the $B_2$ progenitor).
**Related:** PROVE.md Sub-problem 1 closed Day-18; Sub-problems 2, 5 (type-uniform lift) closed Day-20. C2 (external iSerre shadow) REFUTED Day-19.

## Day-20 (2026-05-17) lift summary

The Day-18 $B_2$ proof lifts type-uniformly to all $B_n$ ($n \geq 2$). The four phases (chain factor uniformity, tensor product as ι-crystal, on-slice catalog factor-by-factor, type-uniformity wrap) all dropped without per-rank ansatz. Key technical point: cross-chain witnesses for non-adjacent chain pairs $(a, b)$ work identically to adjacent ones because intermediate chains $c$ with $a < c < b$ get zero multiplicity in the witness and contribute no bracket symbols — chain-$a$ trailing mid-(s are directly adjacent to chain-$b$ leading mid-)s.

Verified all 24 cross-chain witnesses at $B_5$ across all 6 chain pairs (including maximally non-adjacent $(1, 4)$). All fire with predicted net delta.

## The reframing

The catalog of $n(2n-1)$ net moves of $e_n^2$ on the slice $S_n$ at $B_n$
short simple has been articulated as the catalog of a **Watanabe-style
tensor product rule** for ι-crystals, extended across the short-long edge
$a_{n-1, n} = -2$.

The decomposition:
$$
\mathrm{Kp}(\infty)\big|_{B_n\text{-action}} \;\cong\; \bigotimes_{a=1}^{n-1} \mathcal{C}_a \;\otimes\; \mathcal{C}_{\mathrm{sing}}
$$
as ι-crystals, with:

- **Chain factor** $\mathcal{C}_a = \mathbb{K}[c_{\text{mid}_a}, c_{\text{bot}_a}, c_{\text{top}_a}]$
  with bracket block $)^{M}_{E_a} (^{2B}_{E_a-E_n} )^{2T}_{E_a+E_n} (^{M}_{E_a}$.
- **Singleton factor** $\mathcal{C}_{\mathrm{sing}} = \mathbb{K}[B_n]$ with
  bracket block $)^{S}_{E_n}$.

The doubled interior brackets $(^{2B} \, )^{2T}$ are the bracket-level
encoding of $a_{n-1, n} = -2$. This is **the new building block** beyond
Watanabe (arXiv:2110.07177) Prop 5.1.1, which only handles simply-laced
edges $a_{ij} \in \{0, -1\}$.

## Why this matters for v2

1. **Citation hook for Watanabe 2110.07177.** Before this reframing, v2 had
   no clean way to cite the foundational Watanabe quasi-split paper because
   the paper explicitly excludes type B. Now we can cite it as the
   simply-laced precedent and position the short-long-edge tensor product
   rule as the *natural extension*.

2. **Per-node compatibility (C1) becomes a precise lemma.** The singleton
   factor $\mathcal{C}_{\mathrm{sing}} \cong \mathbb{K}[B_n]$ matches
   Watanabe's split-node case ($a_{i, \tau(i)} = 2$) verbatim. The chain
   factor $\mathcal{C}_a$ is the new content. This is the cleanest possible
   factorisation of "what is Watanabe-borrowed" vs "what is new."

3. **Cross-chain emergence becomes a structural theorem.** The 4 cross-chain
   entries at each chain pair are exactly the *tensor product interaction
   term* of the rule — two distinct factors are coupled via cross-factor
   bracket cancellation. This explains *why* there are $2(n-1)(n-2)$ of
   them: 4 per chain pair times $\binom{n-1}{2}$ pairs. The three-class
   decomposition of three-strand-braid Theorem 5.1 acquires structural
   meaning: intra-chain (factor-internal), cross-chain (two-factor
   interaction), singleton-involving (singleton-factor coupling).

4. **Type-uniform proof of (C3) catalog match is automatic.** The tensor
   product rule = CST bracketing (Theorem 4.2 of proof note), and the CST
   bracketing has been computationally verified at $B_2$ (6 moves), $B_3$
   (15), $B_4$ (28).

## What's deferred

- **(C2) iSerre compatibility.** Sub-problem 4 in PROVE.md. Requires
  symbolic expansion of the type-B iSerre at $a_{n-1, n} = -2$ (cubic in
  $B_{n-1}$ with $B_n$ inserted; see CLW arXiv:1810.12475 Eq. 1.2 for the
  precise formula). At $q = 0$, the iSerre should hold as a polynomial
  identity on $K_p(\infty)$. Independent confirmation would give external
  algebraic backing for the tensor product rule.

- **Sub-problem 3 (lift catalog-count proof to TP language).** The
  three-strand-braid Theorem 5.1 already gives $n(2n-1) = 3(n-1) + 2(n-1)(n-2) + (2n-1)$
  type-uniformly. Lifting to TP language is essentially relabelling. A
  cleaner generating-function proof on $\bigotimes_a \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$
  would be desirable but not load-bearing for v2.

## v2 structural framing (post-reframing)

**Theorem (proposed for v2):** *Let $\mathfrak{g}$ be of type $B_n$, $n \geq 2$.
The restriction of $\mathrm{Kp}(\infty)$ to the action of $B_n$ (the short
simple) admits an ι-crystal structure as a tensor product*
$$
\bigotimes_{a=1}^{n-1} \mathcal{C}_a \;\otimes\; \mathcal{C}_{\mathrm{sing}},
$$
*where $\mathcal{C}_a$ is the chain ι-crystal of the short-long edge (with
doubled interior brackets) and $\mathcal{C}_{\mathrm{sing}} \cong \mathbb{K}[B_n]$
matches Watanabe (arXiv:2110.07177) §4.1. The tensor product rule extends
Watanabe Prop 5.1.1 past the simply-laced restriction (S1)–(S3)'. The
on-slice catalog of $e_n^2$ on this ι-crystal consists of $\binom{2n}{2} = n(2n-1)$
net moves, decomposing as $3(n-1)$ intra-chain + $2(n-1)(n-2)$ cross-chain
+ $(2n-1)$ singleton-involving entries.*

This is the *standalone* theorem statement, no bridge required.

## Connection to past attempts

- **The "tensor product framing" finally snapped into place.** PROVE.md
  Sub-problem 1 expected this to take 3-4h; it took ~2h once I stopped
  trying to *derive* the rule from Watanabe's framework and instead
  *reverse-engineered* it from the CST bracketing already in the
  implementation. The bracket block $)^M (^{2B} )^{2T} (^M$ is the
  tensor-factor-internal structure of $\mathcal{C}_a$; concatenation in
  convex chain order plus singleton is the tensor product rule.

- **F5 of PROVE.md (rule dissolves) was NOT triggered.** This is the first
  v2 structural ingredient to *not* refute itself in 5 days of bridge
  conjectures. The reason: I wasn't conjecturing a bridge to an *external*
  object — I was just relabelling the existing CST bracketing in
  Watanabe-compatible language. The reframing is internal to the standalone
  combinatorial object.

- **AT-bridge MALFORMED (Day 18 AM) was the wrong shape: cactus generator
  ≠ catalog of net deltas.** The tensor product rule is the *right* shape:
  Watanabe's framework already operates on net deltas of $B_i$-actions on
  ι-crystal tensor products. Same kind, same operations, same level. No
  kind-mismatch.

— Rick, 2026-05-16
