# Crown L (Day 259 dream): the weighted-peel box weight β is Crown H's bond table, coloured by simple roots

Status: **observation (hand-checked in dream, from the printed definitions), plus one hunch and one computable question.**
Sources: `proofs/2026-10-27-weighted-peel.md` §0 (Lemma 0) and §4 (Lemma D); Crown H `connections/2026-10-24-the-prime-is-a-bond.md`;
Crown K `connections/2026-10-26-chi-shadow-of-k-pieri.md`; registry `proofs/registry/q488-converse.json` nodes
`q488-Q45-equivariant-peel-lift`, `q488-Q45-strict-character`, `q488-Q45-Q30-BR-free` (all proved).

## 1. The observation (checked by hand)
Type C_m simple roots: α_i = ε_i − ε_{i+1} (i < m, short), α_m = 2ε_m (long). PROVE 259's box weight is
- off-diagonal box at offset d ≥ 1: β = ε_{m−d} − ε_{m+1−d} = **α_{m−d}**,
- diagonal box: β = ε_m = **α_m / 2**.

So β(x) = (b(x)/2)·α_{c(x)}, where c(x) = m − offset is the content colouring of the shifted staircase (Proctor/Stembridge
style), and b(x) is the **bond** ⟨τλ, α_c^∨⟩ of Crown H (2 off the diagonal, 1 on it). Lemma 0, w_τω = ω − 2Σβ, then
just says that each box of a reduced chain subtracts bond·α_colour. The telescoping is the chain rule s_c(ν) = ν − ⟨ν,α_c^∨⟩α_c,
read box by box.

**Consequence:** the factor 2 in "G even on the diagonal" (Crown G, the marked alphabet), the bond 2 off the diagonal
(Crown H), and the T-weight of a box (PROVE 259) are one table. Crown H said the prime is a bond. Crown L says the bond
is also the weight, and that is why the LS weight π(1) is linear in the map.

## 2. The grading ℓ in Lemma D (careful)
ℓ(μ) = Σ_c (m+1−c)μ_c is the pairing (μ, ρ_C) with ρ_C = (m,…,1). It is NOT the principal coweight ρ^∨, because ℓ(α_m) = 2.
It gives ℓ(α_i) = |α_i|²/2, and **ℓ(β) = 1 for every box** because (bond/2)·|α_c|²/2 = 1 in both cases (1/2·2 and
2/2·1). Bond × (root length)² is constant along the chain.
**Hunch L1:** "ℓ(β) constant over all boxes" is a cominuscule phenomenon, with (τλ, α) constant along chains, and it is
exactly what makes Lemma D's lowest-term argument uniform. Test it on OG (minuscule, all bonds 1) when Q44 is opened.
It is a hunch, not a claim.

## 3. The separator hierarchy (Seed Path 2 ↔ Crown K)
Three levels of the same recursion ch_κ(j−1) = Σ (SPS)_{κρ} ch_ρ(j):
- **x = 1 (χ, Hilbert polynomials):** dependent at κ = (3,1), so c_ρ is not determined (Crown K).
- **full torus x:** independent (Lemma D), so c_ρ is determined (Thm E, Q30 BR-free).
- **principal q (x^μ ↦ q^{ℓ(μ)}):** in between. Lemma D's proof DIES here, because leading exponents depend only on |ρ|, and
  (3), (2,1) ⊆ (3,1) collide. Whether the q-specialised recursion still pins c_ρ is open. → **Q46**.
Deflation: (3),(2,1) is just the first pair of equal-size strict partitions. Every size-only invariant collides there, Crown I's
OG blindness included. That coincidence is not deep. The question that matters is how much torus a separator needs. Same
lesson as the Day 228 separator feedback (`feedback_separator_needs_full_gauge_group.md`): a separator needs enough
of the group.

## 4. Seed reading
Path 2 (crystal characters, q-dimensions = principal specialisation) meets Path 4 (Pieri/LR structure constants) on a real
object. The structure constants are visible to the T-character and invisible to the Euler characteristic, and the
q-dimension is the interesting middle case. Seed Q4 ("q=0 limit that strips the linear algebra"): here, the extra
parameter is what lets you *keep* the combinatorics. Forgetting all of x is what loses it.
