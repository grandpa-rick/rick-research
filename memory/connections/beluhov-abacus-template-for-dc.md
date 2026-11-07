---
name: Beluhov abacus method as structural template for D(c) derivation
description: Beluhov 2506.12789 proves ν₂ of lattice walk counts via abacus stratification by d mod 4, structurally identical to Rick's D(c) split by c mod 4. Template for structural derivation of beta-prime-digit-sum-formula.
type: project
tier: A
status: active-open (derivation needed)
---

# Beluhov Abacus Method → D(c) Structural Derivation

**Source:** arXiv:2506.12789 (Nikolai Beluhov, 2026). "Powers of 2 in High-Dimensional Lattice Walks." Enumerative Combinatorics and Applications, vol. 6, issue 2, 2026.
**Discovered:** Browse 86, 2026-07-14.

## Beluhov's result

Computes w_d(n) = ν₂(W_d(n)) where W_d(n) = number of 2n-step origin-to-origin walks in Z^d.

Main theorem (mod-4 split):
- d odd: w_d(n) = s₂(n)
- d ≡ 2 mod 4: w_d(n) = 2·s₂(n)
- d ≡ 4 mod 8: w_d(n) ≥ 3·s₂(n), equality iff n has no adjacent 1-bits
- d with ν₂(d) = k+2 (k ≥ 1): w_d(n) ≥ (3+k)·s₂(n), with equality condition = finite automaton on binary words

**Proof strategy (the relevant one):** ABACUS METHOD
1. Stratify the combinatorial objects by "abacus type" — a labeling of paired adjacent binary digits in the binary expansion of the counting argument
2. Each stratum contributes exactly one factor of 2 per 1-bit in s₂(n) via Kummer's theorem for multinomial valuations
3. The mod-4 splitting reflects the 2-adic depth of d in the pairing structure

## Structural parallel to D(c)

Rick's digit-sum formula: D(c) = β(c) − β'(c) splits by c mod 4 as:
- c ≡ 0 mod 4: D = s₂(⌊c/4⌋) − 1
- c odd: D = 4 + 2·s₂(⌊c/4⌋ − 1)  [NOTE: k = ⌊c/4⌋]
- c ≡ 2 mod 4: D = 1 + s₂(⌊c/4⌋ − 1)

Both:
- Are 2-adic valuations of combinatorially defined quantities
- Result in pure digit-sum formulas (linear in s₂)
- Split by the same mod-4 residue class structure
- Involve a SCALED argument (⌊c/4⌋ rather than c — a "one level up" Kummer carry)

## The derivation blueprint

1. **Write D(c) = ν₂(explicit product/quotient of Pochhammer-type quantities).** Rick's Pochhammer h_k^{(c)}(a,b) factors are known: h_k^{(c)} = (a+3)_{c-1-k}(b+2)_{c-1-k} · Q_k(a,b,c) from the three-variable factorization (Day 88). The carrier summand structure from the Sharp Cancellation Principle means β'(c) = min_k LB_k^{(c)}.

2. **Apply Kummer's theorem to the Pochhammer product.** LB_k^{(c)} = ν₂(h_k^{(c)}) over the specific achiever (a*,b*,k*). The Pochhammer factors are products of consecutive integers, so ν₂((n)_m) = Σ_{i=1}^{m} ν₂(n+i-1) = Legendre formula.

3. **Identify the scale.** The s₂(⌊c/4⌋) argument suggests carries are being counted at scale c/4 — i.e., the relevant binary structure is in the second pair of bits of c. This matches: Δ_1^{(c)} = v_2(c(c-1)) (F2 proved uniformly) already captures the mod-2 structure; the mod-4 refinement (F3) handles the ⌊c/4⌋ level.

4. **Abacus stratification.** Stratify the achiever (a*,b*) by its "abacus type" at scale ⌊c/4⌋. Each stratum should contribute exactly one factor of 2 per 1-bit in s₂(⌊c/4⌋), matching Beluhov's mechanism.

## Next step

Write D(c) = ν₂(P_{k*}(a*,b*,c)) where P is the carrier Pochhammer expression, and verify that Beluhov's abacus stratification applies. Targets PROVE.md: structural derivation of beta-prime-digit-sum-formula from Kummer carries at scale ⌊c/4⌋.

**This is the missing structural mechanism for promoting beta-prime-digit-sum-formula from checked-sober → proved.**
