# CLOSED (Day 214, 2026-09-30): DS PROVED for all lengths by a termwise degree count on the subset formula. It is not analytic in the sense of this file; none of the strategies below was needed. See proofs/2026-09-30-day214-DS-all-lengths-PROVED.md and registry hikita-star-dominance-support.json (root = proved). Follow-up: q-d-lambda-mu-t-count-01-matrices.md.

# Question — Analytic proof strategies for the DS (Dominance-Support) conjecture

**Status:** OPEN. `computed` 22-for-22 (Day 196). Analytic proof `hunch`.
**Impact:** DS is the FPSAC 2027 anchor. Even a partial proof (e.g., length-3 case) sharpens the story significantly.

## The claim to prove

For any partition λ of n:
$$e_\lambda^{(q,t)}(X) = q^{-n(\lambda)} e_\lambda(X) + \sum_{\mu \succ \lambda} c_{\lambda\mu}(q,t) e_\mu(X)$$
where n(λ) = Σᵢ (i−1)λᵢ (Macdonald n-statistic).

## Strategy 1 (REFUTED Day 197): via Route 2c (D'Adderio D_{(a)} identification)

**Status:** REFUTED across three variants (direct, h-side, ω-conjugacy). See `q-D-a-equals-e-a-Y-level-1-AHA.md` (CLOSED). D_{(a)} lives at a different rep-theoretic layer than Hikita's level-1 rep.

## Strategy 6 (NEW highest EV, Day 199): via Thibon triangle — A^{(2)} = p_2(Y) identification

**Setup:** Day 198 introduced Lemma 1 (p_2(Y)-Pieri), reducing DS(2,1,1) to p_2(Y) atomic-Pieri + Day 191 SP via C = p_2(Y)•e_2 + 2t·D. Browse 145 identified Thibon 2608.30791's Nazarov-Sklyanin operator A^{(2)} as the primary candidate for a q,t-analog of p_2(Y). If A^{(2)} = c_{q,t} · p_2(Y) with a monomial rescaling, Thibon's Thm 2.3 gives an explicit operator formula for Lemma 1, hence an analytic proof.

**Iterated framework:** For length-k DS products,
1. Newton identity in $\Lambda(Y)$: $e_1(Y)^k = p_k(Y) + $ lower-order polynomials in $p_j(Y), j < k$.
2. Apply 𝔮: $(e_1 \star)^k F = t^{-*} \cdot [p_k(Y) + \text{corrections}] \bullet F$.
3. p_k(Y)-Pieri hierarchy conjecture (`hunch`, Day 199): each $p_k(Y)\bullet e_r$ has $k+2$ nonzero DS-interval terms, $k+1$ r-independent.
4. DS at $(r, 1^k)$ falls out by induction.

**Cost estimate:** 1-2 hours for Vertex A test (A^{(2)} vs p_2(Y)). If YES, Lemma 1 immediately promoted to `proved`; further hierarchy takes 1-2 weeks.

See `connections/2026-09-16-thibon-triangle-p2Y-candidates.md`, `questions/q-A2-equals-p2Y-normalized.md`, `questions/q-p_k-Y-Pieri-hierarchy.md`.

## Strategy 2: via Cho-Oh 2609.03840 Macdonald involution

**Setup**: Cho-Oh 2609.03840 gives HHL-formula-via-A_{q,t} in K-theory. Their expansion has q^{n(λ)} factor. Rick's DS has q^{−n(λ)}. These differ by Macdonald involution ω.

**Sketch**: if ω sends H̃_λ basis to some scalar × e_λ^{(q,t)} with dominance-tracking under ω:
1. HHL is dominance-triangular in H̃_λ with q^{n(λ)} leading coefficient.
2. Apply ω. ω exchanges e_λ ↔ h_λ and (dominance ≽) ↔ (dominance ≼ conjugated).
3. Track through ω: should land on dominance-triangularity in e_λ with q^{−n(λ)} leading coefficient.

**Cost estimate**: 2-4 hours read + calculation.

## Strategy 3: direct AHA induction

Prove DS by induction on length l of λ = (λ_1, ..., λ_l):
- Base l = 1: e_r^{(q,t)} = e_r trivially DS-triangular. ✓
- Base l = 2: SP (Day 195 conjecture). Special case, still open analytically.
- Inductive step l → l+1: use associativity + Thm 3.12 + a Lemma-3.11-analogue.

Problem: the Lemma-3.11-analogue is exactly what Route 2 needs. Circular unless Route 2 is closed independently.

## Strategy 4: row-length filtration

Look for a filtration F_0 ⊂ F_1 ⊂ ... in Λ_{q,t} such that:
- F_k = span{e_λ : λ_1 ≥ some function of k} (or similar).
- e_a ⋆ (·) shifts within/across specific F_k's in a dominance-controlled way.

If such a filtration exists structurally (from Hikita §3–4), DS follows immediately.

**Cost estimate**: 3+ hours careful reading of Hikita §3–4. Higher risk (may not exist as stated).

## Strategy 5: identify basis with a known Macdonald-family basis

**Hypothesis**: {e_λ^{(q,t)}} equals some already-studied basis (up to normalization) whose dominance-triangularity is already proved.

Candidates:
- Cherednik's E_λ (non-symmetric Macdonald).
- Modified Macdonald polynomials H̃_λ.
- Some inhomogeneous Macdonald basis.
- Some Hall-Littlewood-adjacent basis.

**Cost estimate**: 1-2 hours literature search + coefficient-comparison SymPy.

## Priorities (updated Day 199)

1. **Strategy 6 (Thibon triangle, Vertex A: A^{(2)} = p_2(Y))** — highest EV. Day 200 primary target.
2. **Strategy 6, Vertex B (Jack shape-match via Thibon 2609.10284 §7.1)** — cheap parallel check.
3. **Strategy 2 (via Cho-Oh)** — medium EV. Deferred pending Vertex A outcome.
4. **Strategy 5 (identify basis)** — cheap. Parallel background research.
5. **Strategy 3, 4** — expensive; only if above fail.
6. **Strategy 1 (D'Adderio D_{(a)})** — DEAD. See `q-D-a-equals-e-a-Y-level-1-AHA.md`.

## Partial-DS-proof targets (checkpoint milestones)

- **Prove DS at length 3 for one λ** (say (2,1,1)) via Thm 3.12 + associativity. Even without a general strategy, this pins down whether "SP + associativity" propagates upward. If YES, all length-3 DS follows. If NO, structural obstruction is precise.
- **Prove leading coefficient q^{−n(λ)}** by counting how many T_i-actions "swap indices" during the length-l computation. May be doable independent of the full DS statement.

## Cross-references

- `connections/2026-09-16-DS-macdonald-triangularity.md` — full DS discussion.
- `connections/2026-09-16-DAdderio-Negut-route-2-unlock.md` — Route 2c.
- `proofs/2026-09-16-day196-dominance-support.md` — Day 196 writeup.
- `proofs/registry/hikita-star-dominance-support.json` — registry.
