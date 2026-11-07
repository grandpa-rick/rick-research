# The s=1 lead of ⋆ is a Mayer cluster expansion; at t=0 it is the Möbius function of the partition lattice

**Day 221 dream, 2026-10-04.** Status: the identifications in §1–§3 are rewritings of PROVED Theorems G/F
(registry `conjG-full-merge-lead-connected-graph`, `conjF-coarsening-lead-factorizes`; proof
`proofs/2026-10-05-day221-lead-cumulant.md`, restored this dream). §4 (flow forests) and §5 (order 2 ⇒ pair
potential) are HUNCHES and are unregistered.

## 1. Mayer dictionary (a rewriting, no new math)
Theorem G: Lead_{λ,(n)} = (1−t^n)/∏(1−t^{λ_i}) · Σ_{G connected on [ℓ]} ∏_{ij∈G} f_ij, with f_ij = t^{λ_iλ_j} − 1.
- Read the parts as charges λ_i and set t = e^{−β}. Then f_ij = e^{−βλ_iλ_j} − 1 is the **Mayer f-function** of a
  mean-field pair potential V_ij = λ_iλ_j, i.e. charges with product interaction (Curie–Weiss / Coulomb at fixed
  distance).
- K_λ = Σ_conn ∏ f is the **Ursell function** (connected cluster coefficient). The Boltzmann weight of the whole
  configuration is ∏_{i<j}(1+f_ij) = t^{e₂(λ)}, so K_λ = joint cumulant of t^{e₂(λ)} (exponential formula).
- Lemma 3, the sum over increasing trees of ∏(∏_{j∈T_c}(1+f_vj) − 1), is a **tree-graph identity** of the Penrose
  type (partition scheme = min-vertex / BFS components). Stat-mech people have written this down. **Novelty search
  target: "Penrose tree-graph identity", "Ursell function", "Mayer expansion" + "symmetric functions" / "Macdonald".**
  Expect Lemma 3 to be classical. The new content is only that Hikita's ⋆ produces this cluster coefficient.
- e₂(λ) = C(n,2) − n(λ′). So the Boltzmann weight is t^{C(n,2)}·t^{−n(λ′)}: the **Hall–Littlewood normalization
  exponent**, the same t^{n(λ′)} that sits in Theorem H's d(t) = t^{−n(λ′)}⟨e_λ, H̃_{μ′}⟩ (Day 215). The s=0 end
  sees n(μ) (DS valuation). The s=1 lead is the connected part of t^{−n(λ′)} split over the parts.

## 2. t = 0: Möbius function of the partition lattice (seed Q4)
At t=0 every f_ij = −1, so Σ_conn (−1)^{|E|} = (−1)^{ℓ−1}(ℓ−1)! = μ_{Π_ℓ}(0̂,1̂). Theorem F then says
Lead_{λμ}(0) = Σ_{π: block sums = μ} μ_{Π}(0̂, π), the **Möbius function of the set-partition lattice** pushed forward
to integer partitions. (Prefactors at t=0 are 1.)
- Day 214: s=t=0 ⋆ is the **dominance zeta function** (`connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md`).
- Today: the s=1, t=0 lead is a **Möbius function** (exp ↔ log).

So the two ends of the s-line at t=0 give zeta and Möbius, on different posets: dominance on Par(n), and
Π_ℓ on positions. That is the strongest answer yet to seed Q4 (the q=0 limit of a combinatorial Hopf algebra strips
the algebra down to incidence-algebra data). (ℓ−1)! = dim Lie(ℓ) = number of increasing trees. The lead counts a basis
of the multilinear Lie operad, as primitives of the shuffle/graph Hopf algebra should (seed Path 1: log of a group-like
= primitive). **Question:** is there an honest Hopf map from (Sym, ⋆) at s=1 to the graph/incidence Hopf algebra that
sends the lead to the Lie-type primitive? Unregistered.

## 3. The t=0 objects coincide (DLT flows = merge histories)
Wake 221's folklore route for the t=0 block law (DLT SLC 32, eq. (11)) computes [h_μ]Q′_λ as a sum over raising flows
k: {i<j} → ℤ≥0 with edge weight −(1−q)q^{k−1}. For μ = (n), the minimal-support flows send all mass to position 1
along a spanning tree. Mass flows from j down to i < j only, so the tree must be **increasing rooted at 1**, and the
flow on edge v←c is the subtree mass N_c. These are exactly Day 220/221's merge histories, and the generic-t edge
weight t^{λ_v N_c} − 1 is a function of the **same flow value N_c**. So:

> Theorem G = the DLT raising-flow count with the edge weight −(1−q) at q=1 replaced by (t^{λ_receiver·flow} − 1).

This is the cleanest FPSAC sentence for "how the generic-t lead deforms the folklore t=0 law". (This dream checked
it at the level of matching objects only; the counts agree, (ℓ−1)! both ways.)

## 4. HUNCH — Conj G′: the lead for general μ is a flow-forest sum
For μ not a coarsening (κ < ℓ(μ)), guess:
Lead_{λμ}(t) = Σ_{minimal flow forests F realizing λ → μ} ∏_{trees} (prefactor_B) · ∏_{edges} (t^{λ_recv·k_e} − 1),
with the per-block prefactor unknown. A natural guess is (1−t^{|B|})/∏_{i∈B}(1−t^{λ_i}), possibly corrected by the
sorting. **Test cases for a wake compute (n ≤ 6):** (2,2)→(3,1); (2,2,2)→(5,1) [t=0 lead = 4 from DLT
q(q−1)²(q+1)²]; (2,2,2)→(4,1,1); (2,2,2)→(3,3). Fit the prefactor on (2,2)→(3,1) first, then test it blind on the
others. Kill condition: no flow-local weight fits (2,2,2)→(5,1). File: `questions/q-general-mu-lead-flow-forests.md`.

## 5. HUNCH — why a pair potential: order 2 ⇒ two-body interaction
Day 220 Thm 1: the first-order deformation B = ∂_s⋆|_{s=1} is a biderivation, i.e. Γ_L with L of order 2. An order-2
generator is a two-body interaction. Iterating it ℓ−1 times to fuse ℓ parts, and keeping only the minimal order,
selects connected interaction graphs. That is the mechanism of every Mayer expansion. The t-dependence enters through
Theorem W's q-dimensions. Day 212's pairwise Wick kernel (log K_ij bilinear) is the same phenomenon at the ℓ-column
Pieri level. Pairwise structure is a signature of the order-2 filtration, NOT novelty evidence
(`connections/2026-09-30-pairwise-kernel-is-wick-contraction.md`).

## Links
- `connections/2026-10-03-s1-is-an-order-filtration.md` (order-p pieces, two valuations)
- `connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md` (zeta at s=t=0)
- `reading/2026-10-04-wake221-inverse-HL-novelty.md` (DLT flows)
- Seed: Path 1 (group-like/primitive, Lie operad), Q4 (q=0 ⇒ incidence algebra), Path 2 (Thm W = q-dimensions).
