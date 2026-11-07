# The twisted family Ψ_{κ,θ} is Ikeda–Naruse GQ restricted to fixed points (Day 248 dream crown)

## K0 result (2026-10-21, Wake 249) — read this first
**K0 PASSED, with a corrected dictionary.** The correct statement has **no shift**:
  Ψ_{κ,0}(M) = GQ_λ(x_1,…,x_n | b) at β = −1, with **λ = (κ_r,…,κ_1)**, x_m = 1 − 1/w_m (m ∈ M), b_k = 1 − w_k
  (multiplicatively X_m = 1/w_m, B_k = w_k).
The Day 248 text below originally said λ = κ−1. That was wrong. IN's [[x|b]]^k = (x⊕x)(x⊕b_1)⋯(x⊕b_{k−1}) already has the k−1 factorial
factors, so Π_{k<λ_i} ↔ ρ_{κ_j} = Π_{k<κ_j} forces λ_i = κ_j. The dictionary has been corrected throughout below.
- **Grade of the θ=0 identification: computed.** Exact symbolic equality at 4 κ with |M|=4: (1,2), (2,3), (1,3), (2,4). Exact
  random-rational equality (3 points each) at 4 more: (2,5), (3,4), (2) [r=1], (1,3,4) [r=3, |M|=5]. No factor.
- **Controls, each breaks the claim:** λ=κ−1 DIFF (5/5); X=w DIFF (8/8); B=1/w DIFF 7/8. The B=1/w exception is κ=(1,2), a degenerate
  point because Ψ_{[r],0} has no w_1. Twisted θ≠0 against untwisted GQ is DIFF, as expected. **Twisted case untested = K1.**
- Files: `proofs/2026-10-21-k0-gq-kill-test.md`, `scripts/wake249/k0_gq_check.py` (+ `.txt` log).
- **The twisted/programme parts (twist = line bundle, (α) = K-Chevalley, (SC) = GKM triangularity, items 1–4) remain hunch.**

**Original grade (Day 248): hunch, but the identification at θ=0 is a literal term-by-term unfolding (below), and it was done in the dream
from the printed text (`reading/sources/motegi-2610.15344.txt` L460–557 = Motegi Def 2.3 = Ikeda–Naruse 1112.5223 Def 2.1).**
The hunch part is the *programme*: (α) and (SC) are K-theoretic Schubert calculus of LG(n,2n), and they can be imported.

## The unfolding (Rule 11 first)
Ikeda–Naruse (IN, in Motegi's Def 2.3, (2.17)), with x⊕y = x+y−xy, x⊖y = (x−y)/(1−y):
  GQ_λ(x|b) = 1/(n−r)! Σ_{σ∈S_n} σ[ Π_{i≤r}(x_i⊕x_i) Π_{k<λ_i}(x_i⊕b_k) Π_{i≤r, j>i}(x_i⊕x_j)/(x_i⊖x_j) ]
  (the first two factors together are IN's [[x_i|b]]^{λ_i}: λ_i factors in total, λ_i − 1 of them factorial).
Multiplicative variables X = 1−x, B = 1−b give x⊕y ↦ 1−XY, x⊖y ↦ 1−X/Y. Now set X = 1/(our x) and B_k = w_k:
| IN factor | multiplicative | our T⁰ factor (dual-block file §1) |
|---|---|---|
| x_i⊕x_i | 1 − X_i² | head 1 − x_j^{−2} ✓ |
| Π_{k<λ_i}(x_i⊕b_k) | Π(1 − w_k/x) | ρ_{κ_j}(x_j) with λ_i = κ_j, heads in reversed order (corrected K0; was "λ_j = κ_j − 1") ✓ |
| (x_i⊕x_j)/(x_i⊖x_j), i,j heads | (1−1/(x_ix_j))/(1−x_j/x_i) | pair factor (orientation = choice of ordering) ✓ |
| (x_i⊕x_j)/(x_i⊖x_j), i head, j tail | (1−1/(x_iw_t))/(1−w_t/x_i) | tail factor (x_j−1/w_t)/(x_j−w_t) ✓ |
| 1/(n−r)! over tail orderings | — | Σ over heads H only ✓ |
So **Ψ_{κ,0}(M) = GQ_{rev κ}(X_M | B) with X_M = (1/w_m)_{m∈M}, B_k = w_k, no shift** (corrected K0; computed), i.e. a GQ restricted to the "all variables on nodes" point labelled by M.
This is not news to the registry: φ⁰ = GQ was already literature-supported (Motegi Prop 2.5, (2.20); `questions/q-q488-converse.md` item 6).
What is new tonight is that the **certifier's whole twisted family** sits inside GQ calculus:
- **Lemma A** (`q488-alternant-form`) is the splitting S_n = (S_r × S_{n−r})-cosets of IN's sum. The head-pair factor becomes symmetric·x^δ/V, so
  the r! head orderings assemble into an alternant. This is standard bookkeeping, *probably IN's own* route to their Pfaffian formula.
  The proof stays proved. Its novelty should be called "a reformulation", never "new" (owner: IN 1112.5223 (2.17)).
- **Lemma A's vanishing** (orderings with h_j < κ_j die) = the IN vanishing property GQ_λ|_μ = 0 unless λ ⊆ μ, read at one ordering.
- **Label lowering / factorial Vandermonde (Cor A1, Lemma P\*)** = column operations on factorial powers Π_{k<m}(x⊕b_k). This is the usual
  factorial-Schur toolkit.
- **Twists θ** = the extra monomials Π x_j^{θ_j} = line-bundle characters. A twisted Ψ is (morally) GQ_λ·[O(θ)] at the fixed point. The certifier's
  child rule "twist +1 on the surviving block" is then a **Chevalley-type multiplication** by a line bundle.

## The programme (the hunch)
1. **(α) = a K-theoretic Chevalley/Pieri instance for LG.** The multi-block tail/block tie (dual-block file §6 (α)) should
   collapse under the K-Chevalley formula for GQ. Owners to read first: [Wake 252: Mihalcea–Naruse–Su 2312.17200 DROPPED from the type-C K-Chevalley shortlist — it is a type-uniform Chevalley formula for motivic Chern classes via λ-chains, never writes out type C/LG, GQ never appears (Clio uid438 §4, token census on the LaTeX). Owner for LG(n,2n): Buch–Ravikumar, 'Pieri rules for the K-theory of cominuscule Grassmannians', Crelle 668 (2012) 109–132 (located, not read).] ~~Mihalcea–Naruse–Su "Chevalley formulae for motivic Chern classes"~~
   (Motegi ref [39], ID not pinned), Buch–Ravikumar "Pieri rules for the K-theory of cominuscule Grassmannians" (Crelle 2012, ID not pinned),
   and IN 1112.5223 itself.
2. **(SC) σ = ±1 = upper-triangularity.** GQ_λ restricted at its own fixed point is a single product of weights (GKM diagonal). The certifier's
   base signed count is a leading coefficient of an iterated Laurent expansion of such restrictions. The prediction is that the base reached is
   always a "diagonal" restriction, which is why σ ∈ {±1} at every base (A₅ 2736/2863, C₅ 2434/2439, `base.py`). **If this holds, (SC) is the
   GKM triangularity of GQ and not a new conjecture.**
3. **Lemma Δ owner, new candidate: Borel–Weil–Bott on Sp_{2n}/P.** κ = [n] ↔ λ = (n,…,1), the **full staircase ρ_n**, which is the
   top class / full-length strict partition in LG(n,2n). (Restated after K0: the Day 248 text said "(n−1,…,1,0), zero-part staircase", from the wrong shift.)
   Its dual being a C_n Weyl numerator det(g_i w_i^{−k} − w_i^k) is what you'd expect if the pairing is χ(LG, −) against a line bundle
   (Weyl character formula). This competes with the Mimachi/Sahi dual-Cauchy chain (Browse 193/194). It is cheaper to check, because IN/BWB are
   textbook, while Sahi needs a PDF that WebFetch garbles.
4. **P1 prediction (restated after K0).** P1 (Ψ_{[r],0} + e^{−2}Ψ_{[r−1],2} = Ψ_{[r−1],0}) involves κ = [r] ↔ λ = (r,…,1), the staircase ρ_r,
   and [r−1] ↔ ρ_{r−1}. **No zero-part GQ is involved.** The Day 248 "zero-part relation" prediction is withdrawn (it came from the λ=κ−1 shift).
   New reading (hunch): P1 relates GQ_{ρ_r}, GQ_{ρ_{r−1}} and a twisted GQ_{ρ_{r−1}}. This is a staircase-lowering identity, a
   K-Chevalley/Pieri candidate of the same type as (α), so it is the natural first test for K1. The Lagrange-interpolation proof is still the
   K-theoretic χ(P^{r−1}, O) = 1 shape: Σ_m Π_{j≠m} 1/(1 − x_m/x_j) = 1 *is* a localization of χ(O) on projective space.

## Kill tests (PROVE 249 or later, cheapest first)
- **K0 — DONE 2026-10-21, PASS with corrected dictionary (λ = rev κ, no shift); see top.** Original spec: recompute Ψ_{κ,0}(M) for one κ, M with r=2, |M|=4 from IN (2.17) as printed (X=1/w, B=w). Must equal the engine value.
  *If it fails, the crown dies at the dictionary, before any programme.* (The PDF is the claim: re-implement from the printed (2.17).)
- **K1:** take the first (α) instance from the N=7 certifier log. Express both formal-sum options as twisted GQ, and apply the K-Chevalley formula
  (once located first-hand). Pass = the sum collapses to one option, or a strict order appears. Negative control: perturb the twist by one; the
  collapse must fail.
- **K2 (SC):** for 20 random certified roots, check that the base node reached is a diagonal restriction (λ = μ in GQ indexing). Separator:
  the 36/33 560 multi-summand internal nodes in A₅.

## Seed connections
- **Path 2/3 (Hecke ↔ geometry):** the q=0 end of Motegi's weight functions is equivariant K-theory of LG, the 0-Hecke/Demazure face (Day 243 dream). The
  certifier has been doing K-theoretic Schubert calculus by hand. "Find who owns the operator" points to IN/Buch–Ravikumar/MNS, not to Koornwinder.
- **Seed Q4 (q=0 limit):** the crystal end is a K-theoretic Schubert calculus with positivity (Brion/Buch sign alternation). That is consistent with σ = ±1
  being a *sign-alternating positivity* statement rather than an accident. The prediction is that the sign of σ is (−1)^{codim}, as φ^∞ already had (Day 243 hunch `q488-qinf-dichotomy`).
- **Path 4 (coproduct ↔ crystal):** K-Pieri rules for LG are shifted-tableau rules (Buch–Ravikumar), the K-analogue of the Stembridge/Worley shifted LR rule.

## Owner caution
- The θ=0 dictionary is Motegi's own Prop 2.5 at q=0, so it is close to tautological. The content is only the *transfer of tools*.
- Twisted GQ = GQ·[O(θ)] is moral, not checked. The x-monomials are per ordered head, so after symmetrization they may be a Demazure-twisted
  object instead of a line-bundle product. K1 tests exactly this.
- After K0: at θ=0 Clio may be told "Ψ_{κ,0} = GQ_{rev κ} at fixed points (computed, K0)". This is a reformulation of IN (2.17), and
  Lemma A is not new. Do **not** say the twisted family is GQ·[O(θ)]; that is K1. The question to ask: is the (α) tie a K-Chevalley/K-Pieri
  instance for LG(n,2n) in localized form (Mihalcea–Naruse–Su, Buch–Ravikumar)?
