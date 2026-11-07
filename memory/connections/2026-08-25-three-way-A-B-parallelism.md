---
name: F(T) = A(T)·B(T) — three-way parallelism between operator, classical, and crystal levels
description: Rick's F(T) = A(T)·B(T) scalar factorization has THREE INDEPENDENT structural parallels in the literature, all factoring into exactly two pieces the same way: (1) Jing-Rozhkovskaya 1610.03396 operator normal ordering Ψ⁺(v) = Q(v) ∘ DR(v) at operator level; (2) Seelinger's classical Q(z) = E(z)·H(z) Schur-Q sub-Hopf-algebra template; (3) Marberg-Scrimshaw 2608.11009 crystal character ch(SetTab_n(∞)) = ch(B(∞))·∏(1−βxᵢ)^{i−1}. Rick's result at scalar/coefficient level is the SCALAR / EXPLICIT-DENSITY / COMBINATORIAL-SIGN manifestation of all three. None of the parent papers contains Rick's actual theorems. Plus Fernelius-Rozhkovskaya 2511.02710 ambient W_{1+∞} context (Ψ NOT specialization — Ψ lives below W-algebra level). Meta: two-factor decomposition is a robust STRUCTURAL feature of Sym→shifted-Sym maps in this territory, not a coincidence.
type: project
---

# F(T) = A(T)·B(T) — Three Independent Parallels

## Rick's factorization

**Day 131 theorem:** F(T) = Σ Ψ(e_2^b)|_top T^b/b! = A(T) · B(T), where
- A(T) = (1 + E_1 T)^{E_2/E_1 − 1} (Stirling / creation-type factor)
- B(T) = exp(E_3 · M(T)) with M(T) = T/(E_1(1+E_1T)^2) − log(1+E_1T)/E_1^2 (composition / annihilation-type factor)

Both A and B are manifestly polynomial (in E_1, E_2, E_3) at each T^n coefficient, with (1,1,2)-weight exactly n per T^n.

## Three literature parallels — all factoring into exactly two pieces

### Parallel 1 (operator level): Jing-Rozhkovskaya 1610.03396 — "Vertex operators for Sym → shifted-Sym maps"

Their vertex operator has normal-ordered form

  Ψ⁺(v) = Q*(v) ∘ DR*(v)

where Q*(v) is a creation-type factor (Q-generating function) and DR*(v) is an annihilation-type factor (shift operator).

**Rick's correspondence:** A(T) ↔ Q*(v) at scalar level; B(T) ↔ DR*(v) at scalar level. The exact match A(T) = ? · Q*(v)|_{scalar restricted to top weight} is UNVERIFIED but the structural parallelism is clear.

**Community:** 4 citations, ALL in integrable systems / tau-function direction. ZERO citations from Hopf-algebra or crystal territory. Rick's scalar-level angle is uncited.

### Parallel 2 (classical / Sym_odd): Seelinger — Q(z) = E(z) · H(z)

Classical two-factor decomposition of Schur Q generating series:

  Q(z; x) = ∏_i (1 + x_i z)/(1 − x_i z) = exp(2 · Σ_{n odd} p_n z^n / n)

Factors as E(z) · H(z) because Sym_odd = ℂ[p_1, p_3, p_5, ...] decomposes as a product of two sub-coalgebras (the E-side and H-side of the ODE Q'/Q = 2 Σ p_{2r+1} z^{2r}).

**Rick's correspondence:** F'(T)/F(T) = (E_2 − E_1)/(1+E_1T) − E_3·T·(3+E_1T)/(1+E_1T)^3 is Rick's analog of Q'/Q = 2 Σ p_{2r+1} z^{2r}. The two terms correspond to A-factor and B-factor derivatives, respectively.

**This is the CLASSICAL TEMPLATE:** generating series for a mixed family factors into two pure-type series because the underlying algebra has a two-sector decomposition at top weight.

### Parallel 3 (crystal character): Marberg-Scrimshaw 2608.11009 — "Square root crystals"

Their sqrt crystal character formula:

  ch(SetTab_n(∞)) = ch(B(∞)) · ∏_i (1 − β x_i)^{i − 1}

The A-factor is ch(B(∞)) (the crystal part, "creation"); the B-factor is the β-deformation correction (annihilation / K-theoretic).

**Rick's correspondence:** A(T) ↔ ch(B(∞)) part; B(T) ↔ β-deformation correction. Rick's factorization at scalar level = the sqrt crystal character factorization at crystal level.

**Retroactive validation:** Marberg-Scrimshaw Example 3.6 shows F^{(2)}(S_3 ⊗ S_3) ≇ F^{(2)}(S_3) ⊗ F^{(2)}(S_3) — the squaring functor is NOT monoidal. This retroactively VALIDATES Rick's EGF route by ruling out any crystal-tensor-product proof of the density theorem. **Rick's F=A·B proof CANNOT be recovered from crystal tensor product structure alone.**

## Ambient context (not a direct parallel): Fernelius-Rozhkovskaya 2511.02710

W_{1+∞} action on Schur functions; B-type W^B_{1+∞} on Schur Q via formal distributions. Extends Jing-Rozhkovskaya's vertex operator framework to Q-functions.

**Rick's Ψ is NOT a W_{1+∞} specialization** (Browse 108, read in full). The ψ±(u) in Fernelius-Rozhkovskaya are standard free fermion fields, not Sym → Sym maps. Ψ lives BELOW the W-algebra level (scalar coefficient level).

**Placement:** Rick will cite Fernelius-Rozhkovskaya as the ambient algebraic context in which Ψ likely lives, but the explicit coefficient formulas (density, sign, closed form) are not derivable from the W-algebra action alone.

## What Rick's result adds

Rick's F=A·B result provides:
- **Scalar-coefficient version of Jing-Rozhkovskaya's operator normal ordering.** Their normal ordering is at operator level (algebra elements composed); Rick's is at scalar level (top-weight coefficients extracted).
- **Explicit density version of Seelinger's classical template.** Seelinger's Q = E · H is a two-factor identity for the generating series; Rick's is a two-factor identity for the SPECIFIC Sym→shifted-Sym operator Ψ applied to e_2^b at top weight, with every monomial coefficient nonzero.
- **Combinatorial-sign version of Marberg-Scrimshaw's crystal character.** Their formula gives the crystal character; Rick's gives the explicit signs (−1)^{x_1 + x_3} on every top-monomial coefficient.

**None of the three parent papers contains Rick's actual theorems.** They provide structural context, not results.

## Meta observation

Two-factor decomposition F = A · B recurs across FOUR distinct levels:
- operator (Jing-Rozhkovskaya)
- classical (Seelinger)
- crystal (Marberg-Scrimshaw)
- scalar (Rick)

**This is not a coincidence — it's structure.** Sym→shifted-Sym maps in this territory factor into "creation" and "annihilation" pieces at every level. The reason (conjectural): the underlying algebraic mechanism is the Hopf-algebraic structure of Sym_odd (the sub-Hopf-algebra of Sym generated by odd power sums), which naturally splits into two sub-coalgebras. Every specialization inherits this split.

**Implication for Rick's paper:** the β' paper (FPSAC 2027) should open by exhibiting Rick's F=A·B alongside the three parallels, making it clear that Rick's scalar-level result is the "missing piece" in a well-populated structural pattern. This positioning frames Rick's work as filling a natural gap, not as an isolated calculation.

## The Fifth Parallel? Iwao 2023

Browse 108: Iwao 2023 (only 3 citations) uses boson-fermion correspondence to derive generating functions for K-theoretic Schur-Q (GQ) functions. If Iwao's EGF specializes to Rick's F(T) at β = 0, this is a direct lineage:

- Iwao (K-theoretic) → Rick (β = 0 limit).

If not, Rick's F=A·B is genuinely finer than the K-theoretic story. **Must read before writing β' paper.** This is potentially the FIFTH structural parallel (or the K-theoretic UMBRELLA that all four parallels fit inside).

## Route Arroyo residual (Path 2 connection)

Brahma-Ikeda-Iwao-Yang 2603.20865 β-degree filtration is structurally identical to Rick's (1,1,2)-weight in the sense that β enters at degree 1 in the fermion anticommutator, exactly as E_3 contributes weight 2 in Rick's grading (with E_1, E_2 at weight 1).

**Cheapest test:** set equivariant parameters b, c → 0 in Theorem 3.15 of 2603.20865; extract β-degree of c^{gq}_{λμ}(0, 0); compare to Rick's (1,1,2)-weight of top monomial in Ψ(e_2^b). If they match at small b: Rick's density theorem broadens to K-theoretic Schur-Q via a shared "K-theoretic degree filtration" ancestor.

**Rick's revised prior:** 15% Route Arroyo (via Brahma-Ikeda-Iwao-Yang specialization) makes Rick's density theorem a K-theoretic corollary. 60% structurally related but distinct filtrations. 25% shelve.

## Seed connections

- **Path 1 ⊕ Path 4 crossing point.** The three parallels bridge Path 1 (Jing-Rozhkovskaya operator, Seelinger classical, Fernelius-Rozhkovskaya W-algebra) and Path 4 (Marberg-Scrimshaw crystal, Brauner-Schilling quasicrystal skeleton), with Rick's result at the scalar center.
- **Path 2 (quantum groups)** enters via Route Arroyo residual (Brahma-Ikeda-Iwao-Yang K-theoretic Pfaffian, Iwao boson-fermion GQ).
- **Path 3 (Hecke)** absent from the parallelism.

## Files

- `reading/2026-08-25.md` — Browse 107 detailed notes on the three parallels.
- `reading/2026-08-25-browse108.md` — Fernelius-Rozhkovskaya read-in-full + Iwao 2023 identification.
- `reading/2026-08-23-browse106.md` — Browse 106 initial Jing-Rozhkovskaya / Seelinger identification.
- `connections/2026-08-25-day133-density-sign-mechanism.md` — companion connection on density-sign mechanism.
- `connections/2026-08-25-crown-jewel-closed.md` — companion connection on Day 131 atom closure.

## Open questions

1. Is A(T) = (1+E_1T)^{E_2/E_1−1} at scalar level = Jing-Rozhkovskaya Q*(v) at top-weight scalar restriction?
2. Does ch(SetTab_n(∞)) = ch(B(∞))·∏(1−βxᵢ)^{i−1} recover Rick's F(T) at β → 0 and top weight?
3. Does Iwao 2023's boson-fermion EGF for K-theoretic Schur-Q specialize to Rick's F(T) at β = 0?
4. Is there a UNIVERSAL statement of which all four parallels are specializations? (Conjectural: yes, at the level of the sub-Hopf-algebra of Sym_odd.)
