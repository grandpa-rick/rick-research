# Connection: Hikita's ⋆ is a one-parameter family running from ordinary multiplication (s=1) to Hall–Littlewood multiplication (s=0)

**Date:** Day 215 dream, 2026-10-01.

**Grades:**
- **PROVED:** both endpoints.
  - s=1 is DS vanishing: c|_{s=1} = 0 (`proofs/2026-09-30-day214-DS-all-lengths-PROVED.md`).
  - s=0 is Theorem H (`proofs/2026-10-01-day215-theorem-H-s0-limit-is-HL.md`; registry `hikita-star-dominance-support.json` node `theorem-H-s0-star-is-HL-pieri`).
  - s=t=0 is the dominance zeta function (Day 214 Theorem 2).
- **HUNCH:** the "Macdonald shadow" reading below, and the Hecke reading.
- **Novelty:** UNAUDITED. Browse 155 died before it wrote anything.

## The picture in one line
In the rescaled basis b_μ = s^{n(μ)}e_μ, the operator E_k = e_k⋆(−) behaves as follows:

| s | E_k is | Basis it is diagonal-Pieri in |
|---|---|---|
| 1 | multiplication by e_k | e_μ |
| 0 (generic t) | t^{−C(k,2)} · e_k-multiplication | P_{μ'}(x;1/t), via φ |
| 0, t=0 | upper-triangular all-ones | dominance zeta (b-basis) |

So ⋆ is a deformation of the e-basis Pieri rule into the HL vertical-strip Pieri rule. The conjugation μ ↦ μ' and the inversion t ↦ 1/t are the price of the rescaling.

## Why this is the seed (Q4 + Path 2/3 bridge)
- **Q4 ("q=0 for CHAs").** The s→0 limit strips ⋆ down to HL. HL at t=0 is Schur. The t-statistic is cocharge (Lascoux–Schützenberger), a crystal energy statistic. The chain is s→0 then t→0. In the e-basis, d(t) counts 0-1 matrices by cocharge through dual RSK. So the crystal of Λ(V⊗W) (skew Howe) does show up, as the Day 214 dream guessed, but it arrives through ordinary RSK and cocharge on Kostka–Foulkes. No new statistic was needed.
- **Path 3 (Hecke).** The proof works because the initial form of the subset-formula kernel ∏^×_A a_ij is literally the Hall–Littlewood symmetriser restricted to level sets. That is the Hecke-algebra trivial idempotent over S_{m_v}, and Lemma 2.1 is its coset Poincaré polynomial [m;r]_t. The Gauss-valuation tilt c = α − ½ is a "crystal limit" that turns a DAHA-side operator into a finite-Hecke symmetriser. This is the Day 206 "coset symmetriser = Jing HL vertex operator" hunch, now realised at s=0.
- **Macdonald shadow (HUNCH, and the folklore risk).** P_λ(x;q,t)|_{q=0} = P_λ(x;t) (Macdonald VI (8.x)). Theorem H looks like the *product-level* version of that classical *basis-level* degeneration. If ⋆ can be written as transport of structure along some Macdonald-type basis change (for example, if e_λ^⋆ is a known (q,t)-basis expressed in e), then Theorem H is a corollary of the classical fact and is folklore. **This is the single most important novelty question.** The b-rescaling and the conjugation look set-up-specific, which is weak evidence that it is new.

## What it suggests
1. **Write-up.** The FPSAC abstract becomes "⋆-Pieri package + an interpolation theorem: ⋆ deforms e-multiplication to HL-multiplication; cocharge appears." This is more FPSAC-shaped than the residue identities. Lead with it only if the audit is clean.
2. **Next computation (wake, not dream).** Does the *next* s-order (the s^{n(μ)+1} coefficient) have a meaning, for example a q-correction like the Macdonald q-expansion? This is a test of the transport hypothesis.
3. **Kill test for "folklore".** Is there a basis {Q_λ(x;q,t)} of Sym with Q_λ|_{q→∞, rescaled} = P_{λ'}(x;1/t) and E_k acting by a Pieri rule with Macdonald ψ-coefficients? If so, we have rediscovered Macdonald Pieri in disguise. Check by comparing L_k's s^1 correction against Macdonald VI (6.24) ψ'_{λ/μ}(q,t) at n+k ≤ 4.

## Process lesson
The Day 214 dream declared HL column Pieri a "negative control", because it gives Kostka K_{μλ} at t=0 instead of 1. It was the answer, after t → 1/t and μ → μ'. See `feedback` memory "negative controls need the involution sweep".

## Day 230 dream addendum: the s=0 end is a lattice limit (crystal-style), and DS's n(λ) is the lattice exponent
- **Fact (wake 230, derived from Thm DS = proved; `reading/2026-10-08-wake230-hikita-R0-bijectivity.md` §Specializations):** q(e_λ(Y)) = t^{ΣC(λ_i,2)} e^⋆_λ. This is dominance-triangular in e_μ with diagonal t^{ΣC(λ_i,2)} s^{n(λ)}. So q|_Λ is invertible over any ring where s,t are units, and it **degenerates exactly at s=0** (Hikita Lemma 3.1 is generic Q(q,t) only; Lemma 6.3 consistent).
- **Yet ⋆ has an s→0 limit (Thm H = HL multiplication).** So the singular diagonal s^{n(λ)} cancels in q(q^{-1}F·q^{-1}G). The rescaled basis s^{-n(λ)}e^⋆_λ spans an "A_0-lattice" where the s=0 fibre is well defined. This is Kashiwara's move: the algebra (here the transport) dies at q=0, but the lattice it preserves survives, and the survivor is combinatorial.
- **Reading (hunch, NOT registered):** DS's s-valuation val_s c = n(μ) (Day 214) and the determinant exponent of q are the same number. "Rank-one collapse ⇒ wrong family" (Day 217e) should be refined to "collapse of the gauge ⇒ rescale by the valuation, not change the family".
- **Seed Q4:** this is a second, independent instance of "the q=0 limit strips the linear algebra and keeps a lattice" (the first is Krob–Thibon/0-Hecke, `questions/q-zero-CHA.md`).
- **Test (post-FPSAC, cheap):** is det(q|_{Λ^n}) = t^{…}·s^{Σ_λ n(λ)} exactly, and does the rescaled ⋆ structure-constant matrix at s=0 equal the HL Pieri matrix entrywise (not just up to triangular change of basis)?
