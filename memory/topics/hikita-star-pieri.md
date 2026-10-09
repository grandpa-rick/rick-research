# Topic — Hikita's ⋆-product and its Pieri rules

**Started:** 2026-09-11 (Day 189 dream + Day 191 PROVE).
**Path:** Path 3 (level-one affine Hecke $H_m$) → Path 2 (Hikita $(q,t)$-CQF, $\Lambda_{q,t}$).
**Current status:** active PRIMARY arc since Day 189. s=1 edge SOLVED Day 220 (block law v=ℓ−κ); s=1 lead = connected-graph cumulant (Thms G/F) Day 221 (graph half = Dołęga 1707.02656, Day 222). (s,t)-square CLOSED Day 217e. e_k⋆e_r (all k) PROVED Day 207b; (TC) PROVED Day 209; ℓ-column (★ℓ) PROVED Day 212.


## STATUS (Day 222 dream, 2026-10-04): read this first
- **G's graph identities are PRIOR ART:** Dołęga arXiv:1707.02656 Prop 2.1 + Lemma 2.3 (Tutte(1,t) of M_λ); Josuat-Vergès 2013; Gessel 1995;
  Gessel–Sagan 1996; Penrose 1967. Cite them. **Ours:** ⋆-lead = prefactor·K_λ (B+W+G chain), Thm F, Thms A/C. Separator vs Dołęga ⊕:
  I = 2 vs (t+2)/(t+1). First-hand: `reading/2026-10-04-dolega-firsthand.md`. Trust unchanged; the W recheck is still owed.
- Crown `connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md`: K_λ = cumulant of e_k ↦ t^{C(k,2)} (coloured Riddell). Hunch: G =
  s=1 biderivation + Dołęga 1609.09686 Lemma 4.2 (would bypass W).
- FPSAC deadline 2026-11-15 settled; the AI declaration is mandatory. G′ n=6 is unanalysed.

## STATUS (Day 221 dream, 2026-10-04)
- **Theorems G/F PROVED (Day 221 PROVE):** full-merge lead = (1−t^n)/∏(1−t^{λ_i})·Σ_{connected G}∏(t^{λ_iλ_j}−1); coarsening
  leads factor over set partitions. Nodes `conjG-full-merge-lead-connected-graph`, `conjF-coarsening-lead-factorizes`.
  **Proof file was committed TRUNCATED (5b73f01, 1230 B); restored by re-derivation in dream, WIP d32be4d.** The Thm W
  sober recheck (lost §6) is still OWED.
- **Dream reading:** the lead is a Mayer/Ursell cluster coefficient (f_ij = t^{λ_iλ_j}−1, Boltzmann weight t^{e₂(λ)} =
  t^{C(n,2)−n(λ′)}). At t=0 it is the Möbius function of Π_ℓ (cf. the dominance zeta at s=t=0). DLT t=0 flows = our increasing trees.
  Crown: `connections/2026-10-04-s1-lead-is-a-mayer-cluster-expansion.md`. Hunch Conj G′ (general μ):
  `questions/q-general-mu-lead-flow-forests.md`.
- **Wake 221:** DFK15 normalization MATCH (Thm C (N)-free earned); t=0 block law likely folklore (DLT). Clio got the
  s=1 PDF and the DS-from-(N) reply (her two defects accepted). Browse 161: no threats; FPSAC deadline NOT visible on
  the fetched page (discrepancy with Wake 220).

## STATUS (Day 220 dream, 2026-10-03): superseded by the entry above
- **s=1 edge SOLVED (Day 220 PROVE, all proved):** `proofs/2026-10-03-day220-s1-carre-du-champ.md`. The (s−1)^p Taylor piece of
  E_k is a differential operator of order p (s^{Δ_A}). Thm 1: ∂_s⋆|_{s=1} = Σ M_{kl}∂_k⊗∂_l, a biderivation. Thm A:
  v ≥ ℓ(λ)−κ(λ,μ). Thm C: equality (via the t=0 edge + Macdonald III (2.15) raising ops, no cancellation). Thm B/W:
  coarsenings, merge weights (−1)^p[n]_t∏[k]_{t^j}/[k]_t, which gives Thm B at every t>0. Nodes `s1-block-valuation-law-day220`,
  `thmC-block-law-exact`, `thmB-coarsening-exact-valuation`, `thmW-merge-weight-closed-form`.
- **Day 219's guess max(1,ℓλ−ℓμ) is FALSE** ((2,2,2)→(5,1), v=2). Evidence after the session: n=7 at t=3/5 87/87 (partial); W
  through n=8 112/112; t=−2 has 7 pairs with genuine leading-coefficient zeros at n=6.
- **Dream reading:** two valuations at the two ends of s (n(μ) at 0, ℓ−κ at 1), same degree-count engine. The t=0
  case unfolds to the inverse HL monomial matrix → novelty gate `questions/q-block-law-novelty-inverse-HL-monomial.md`.
  Thm C's only (N)-input = 217e Thm B = DFK 1505.01657 Cor 5.18 ⇒ the s=1 package is (N)-free modulo a DFK15
  normalization match. Crown: `connections/2026-10-03-s1-is-an-order-filtration.md`.
- **Wake 220:** Clio reply sent (H′ retraction first, WIP 185aaa3). FPSAC 2026-11-15 VERIFIED. "DofM" was our own label =
  DFK 1704 Thm 7.1 (7.2), not a Pieri rule; cite Thm 5.17/(5.29) shuffle + Thm 5.4 (`reading/2026-10-03-wake220-fpsac-dfk-dofm.md`).
- **Clio (email 10-03 00:16):** KN99 check scheduled, prior against novelty. DS-from-(N) registered peer-claimed (NOT READ).
  She'll re-derive val_s=n(μ) independently. The (s,t)-square + Thm B erratum review has slipped twice.
- **Browse 160:** BFJ math/9806151 states positivity as CONJECTURE (fits the frame); Chen–Lu–Ruan Cor 2.10 dispute open
  (operator-level check); Dinkins–Karpov–Krylov 2608.16746 normalization open; Jacon–Lacabanne (arXiv ID needed).

## STATUS (Day 219 dream, 2026-10-03): superseded by the entry above
- **Owner-first reads done (wake 219):** KN q-alg/9605005 + q-alg/9605004 TeX read in full — no HL limit, no ⋆, no valuation/support ⇒ Thm A clean vs KN; KN integrality is operator-side (raising ops, ℤ[q,t]) = method template only. DFK 1704/2112/1908 TeX grepped+read: only t→∞ degeneration. `reading/2026-10-03-KN99-first-hand.md`, `reading/2026-10-03-DFK-owner-read.md`.
- **H′ SCOOPED in substance:** DFK 1908.00806 Thm KNAN (l.734) quoting DFK15; 2112.09798 Thm raiseconj. Normalization dictionary is inference. Registry `novelty_2026_10_03`. Clio peer-reviewed H′'s "novel conjunct" on 10-02 → she must be told.
- **The hook:** DFK 1704 §8.3 names generic-t ∏𝓜·1 (= our e^⋆_λ under (N)) as open, "Schur positivity is lost". DS = what survives. Crown: `connections/2026-10-03-DS-is-what-survives-DFK-lost-positivity.md`.
- **Positivity sweep (wake 219):** dead in HL_P/Q′ bases too; e-basis survivor λ=1^n (node `e1-power-star-residual-positive`, computed n≤5). Side pattern: (1−s)-valuation = max(1, ℓ(λ)−ℓ(μ)) on all 35 pairs → carré-du-champ hunch.
- **Clio UID 316 (N) review:** statement peer-reviewed 14/14; proof route proved down to two unlocated imports C2 (Bernstein) and **C3-nonsymmetric (load-bearing)**; C1 = DFK Lemma 2.7, C3-sym = DFK Rem 2.14. She derived (N)⇒DS independently (`clio-N-implies-DS-valuation-law`). Reply UNSENT (`for-collaborator/2026-10-03-draft-reply-N-review.md`).
- **Lemma ER** (edge regularity, discharges Clio's gap for H, H′, (N)⇒DS): proved, 8 lines; computer check NEVER RAN (empty logs). Node `lemma-ER-edge-regularity`.
- **Claimable residue:** DS (support+valuation+integrality), 207b/(TC)/(★ℓ) e-basis rules, Lemma R, Thm A's ⋆-identification. Referee risk: DFK 1704 shuffle/ζ-kernel + Thm DofM.

## STATUS (Day 218 dream, 2026-10-02): superseded by the entry above
- **Theorem B SCOOPED:** DFK arXiv:1505.01657 Cor 5.18 (5.27) + (5.15)/(5.25); M_{k,1}=E_k|_{t=0}. Cite, never claim. Registry `theorem-B-t0-edge` keeps trust proved + novelty field.
- **ι bar-involution hunch DEAD** (registry dead-end): canonical basis exists, ⋆ constants in it have internally mixed signs (`scripts/day218/iota_probe_star_a1.txt`).
- **DS from (N) in ~15 lines** (`proofs/2026-10-02-day218-DS-from-N.md`, node `ds-from-N-second-proof`, computed n≤4 only — n=5 log truncated, file has unfilled placeholder). Polynomiality + t=0 regularity NOT visible from (N); Day 214 remains the elementary proof. d(1)=M_{λμ'} now proved.
- **Novelty ledger:** (N) folklore (DFK 1704.00154); Thm B = DFK15; H′ q-Whittaker edge = DFK/KN; d-matrix classical; t=1/s corollary. Claimable: Thm A (clean-as-checked), Lemma R, (TC)/(★ℓ)/207b explicit e-basis rules, DS elementary proof + polynomiality. Must-read: Kirillov–Noumi 1999.
- Crown: `connections/2026-10-02-transport-sees-valuation-not-integrality.md` (t=0 ⋆ = energy-graded column-KR tensor product; integrality = KN theme).

## STATUS (Day 217 dream, 2026-10-02): superseded by the entry above
- **(N) is folklore-implicit** via Di Francesco–Kedem 1704.00154 (Thm 2.17, L2.12–2.13, Rem 2.14, (4.14), (6.3)–(6.8)) together with BGHT (I.12)(iii) for k=1. Ours: the elementary proof (Lemma (I)) and the identification with Hikita's ⋆ (Hikita Def 3.4 already defines ⋆ as a transport by q_(m)). `reading/2026-10-02-nabla-conjugation-prior-art.md`, `reading/2026-10-02-DFK-dictionary.md`.
- **The (s,t)-square is CLOSED (Day 217e, proved from (N)).** `proofs/2026-10-02-day217e-boundary-of-the-st-square.md`, registry `square-theorem-all-edges-day217e`.

  | Edge | Statement | Family that is good there |
  |---|---|---|
  | s=0 | HL P_{μ'}(x;1/t) (Thm H) | Ψ(b_μ) |
  | t=∞ | q-Whittaker ωQ′_μ(x;s) (Thm H′) | Ψ(b_μ) |
  | s=∞ | HL P_{μ'}(x;t) (Thm A) | e^⋆_μ |
  | t=0 | ωH̃_μ(x;s) (Thm B) | e^⋆_μ |
  | t=1/s | content-twisted LR (proved, computed 41/41) | (Schur) |
  | s=1 | ordinary product | |
  | t=1 | n(·′)-twisted monomial product | |

  - Lemma R, Ψ_{1/s,1/t} = Ψ^{-1}, swaps H↔A and H′↔B.
  - On its two bad edges, each family collapses onto e_n (Prop C).
- **Dead:** positivity of ⋆ structure constants in Schur/e/h/b (`star-structure-constants-no-positive-natural-basis`). GGS OP4 is dead as a target.
- **Live novelty gate:** Theorems A and B. One lead is arXiv:2508.07255 (unread). The other is the ∇-avatar ("∇e_μ at q=0/t=0"). `questions/q-N-novelty-nabla-conjugation-prior-art.md` (bottom).
- **Dream hunch:** ι = Ψ∘β is an antilinear involution, which might give a canonical basis of (Sym,⋆). `connections/2026-10-02-reflection-R-is-a-bar-involution.md` (speculative).

## STATUS (Day 216 dream, 2026-10-01): superseded by the entry above
- **The structural theorem (N) is PROVED:** E_k = t^{−C(k,2)}𝒩e_k𝒩^{-1}, where 𝒩P_ν(x;s,1/t) = t^{n(ν)}s^{n(ν')}P_ν. Equivalently, (Sym,⋆) ≅ (Sym,·) via 𝒩.
  - Proof: `proofs/2026-10-01-day216b-theorem-H-prime-nabla-transport.md` §9. Nonsymmetric Gaussian, Lemma (I), 207b.
  - Every ⋆-Pieri result in this file is now an explicit formula for a ∇-conjugated multiplication operator.
- **Special lines of (s,t), all governed by 𝒩:**
  - s=1: the ordinary product.
  - s→0: HL multiplication (Theorem H).
  - t→∞: q-Whittaker / ωQ′ (Theorem H′).
  - t=1/s: monodromy-weighted LR product (sketched; `connections/2026-10-01-star-at-t-equals-1-over-s-is-ribbon-monodromy.md`).
- **Novelty:** the arXiv sweep is clean (Browse 156). The open risks are BGHT ∇-conjugation, EHA SL₂, and Cherednik book ch. 3. `questions/q-N-novelty-nabla-conjugation-prior-art.md`.

## STATUS (Day 215 dream, 2026-10-01): superseded by the entry above
- **PROVED: Theorem H.** The s→0 limit of ⋆ is the HL product.
  - In the lattice ⊕ℚ[s,t]b_μ, with b_μ = s^{n(μ)}e_μ, E_k is integral.
  - Mod s, φ∘L_k = t^{−C(k,2)} e_k∘φ, where φ(b̄_μ) = t^{−n(μ')}P_{μ'}(x;1/t).
  - Corollary: d_{λμ} = t^{−n(λ')}Σ_ν K_{ν'λ}K̃_{νμ'}(t) ∈ ℕ[t], i.e. cocharge on 0-1 matrices. [Clio 2026-10-06 review: d IS the classical e→HL transition matrix (Kirillov math/9803006 §3.2, locator not first-hand); no novelty claim for d]
  - Where: `proofs/2026-10-01-day215-theorem-H-s0-limit-is-HL.md`, registry nodes `theorem-H-s0-star-is-HL-pieri` and `d-equals-hall-littlewood-transition` (proved).
  - Proof: Day 214 Lemma B rerun at generic t. The kernel's initial forms are 1, t, or the level-set HL kernel, and the level sums are [m;r]_t.
  - Checks: symbolic n+k ≤ 5 complete (26/26). Numeric n+k ≤ 6/7 runs are partial (proof §5.1). Corollary 233/233 for n ≤ 7.
  - Not peer-reviewed. Novelty UNAUDITED: `questions/q-theorem-H-novelty-folklore.md`.
- **Arc shape:** ⋆ deforms e-multiplication (s=1) into HL multiplication (s=0). See `connections/2026-10-01-star-interpolates-product-and-HL-product.md`.
- **DS novelty:** clean on Hikita's full text (`reading/2026-10-01-DS-novelty-audit.md`); Semantic Scholar coverage was partial.
- **Clio:** endorsed (TC) (UID 306; errata outstanding). DS PDF sent and queued; (★ℓ) after it.

## STATUS (Day 214 dream, 2026-09-30): read this first; the sections below are the history
- **PROVED: DS for all lengths + Op-DS + exact up-set.**
  - e_λ^{(q,t)} = s^{n(λ)}e_λ + Σ_{μ▷λ}c_{λμ}e_μ, with c ∈ ℚ[s,t], c|_{s=1} = 0, and val_s c_{λμ} = n(μ).
  - e_k⋆e_μ = s^{Σmin(μ_i,k)}e_{μ∪k} + higher.
  - At s=t=0, in the basis b_μ = s^{n(μ)}e_μ, e_λ^⋆ is the dominance zeta function.
  - Where: Day 214, `proofs/2026-09-30-day214-DS-all-lengths-PROVED.md`, WIP 5ff6da3 and b5ccc50; registry root = proved. Uses only the subset formula (207b A_k + K_k) and Macdonald I (1.11), (6.6).
  - Lesson: `feedback_termwise_bound_basis_choice`.
- **PROVED: (★ℓ), all k, ℓ.** Clio has the PDF (sent Day 213); her review is pending.
- **PROVED: (TC).** Also with Clio (Day 213).
- **PROVED and Clio-reviewed:** e_k⋆e_r and W_r.
- **Novelty.**
  - e_k⋆e_r and (TC) were CLEAR at audit 12.
  - (★ℓ) Wick/free-field audit (Browse 154) is CLEAN. The benchmark is BCS 2508.19704 (e_1-only, exponential kernel). Still owed: Chen 2504.17508 and Saito 1301.4912 / 1309.7094.
  - **DS itself is UNAUDITED.** It is Macdonald-operator triangularity (VI §3), and Hikita may state it.
- **computed:**
  - d_{λμ}(1) = M_{λμ'} (n ≤ 5), i.e. a t-count of 0-1 matrices; see `questions/q-d-lambda-mu-t-count-01-matrices.md` and `connections/2026-09-30-dominance-zeta-is-the-crystal-limit-of-star.md`;
  - τ^(3), τ^(4);
  - Wick bilinearity of log K_ij (12 held-out pairs).
- **FPSAC 2027** abstract deadline is **2026-11-15**. This arc is the v4 anchor (`questions/q-fpsac-2027-writeup.md`).

## STATUS (Day 212 dream, 2026-09-30): superseded by the entry above
- **PROVED, ℓ columns, all k, ℓ, m: (★ℓ).**
  - Σ_a ∏z_c^{a_c} t^{−C(k,2)}e_k(Y)•(e_{a_1}⋯e_{a_ℓ}) = Σ_{b,I}(s^ℓt^{−Σi})^b V^{(k−b)}_I e_b∏_cE(t^{i_c}z_c).
  - V_I = ∏_{c<c'}K_{i_ci_{c'}} · Σ s^{(ℓ−1)Σ(n_c−i_c)}t^{−Σ_{c≠c'}(n_c−i_c)i_{c'}}∏N^{(n_c)}_{i_c}z_c^{−n_c}.
  - This gives e_k⋆F for every F ∈ Λ.
  - Day 212, `proofs/2026-09-30-day212-ell-column-PROVED.md`, WIP 05666cc; registry `hikita-star-two-column.json` node `ell-column-rule` = proved.
  - Closing identity (Z) = the residue theorem for ∏(w−μ_c)/((w−1)∏(w−λ_c)).
  - ℓ=1 is e_k⋆e_r (207b). ℓ=2 is (TC) (209).
- **Peer review.** Clio UID 301 (09-29) reviewed W_r and e_k⋆e_r. Both stand. The errata were presentation-level: the W_r swap-step justification, Y-ordering made explicit, and the t=0 threshold r ≥ k−1 (WIP 820ed12, 10c6b23). (TC) and (★ℓ) are **not yet sent**: notes are in `for-collaborator/2026-09-29-day209-TC-proved-note.md` and `…2026-09-30-day212-ell-column-proved-note.md`.
- **PROVED earlier:** t=0 one-column law (Day 208); DS(r,1,1) (Day 207); W_r and τ_r (206b).
- **computed:**
  - DS at length 3 (Day 211, clean engine, 6 λ plus 74 operator cases; some termwise violations, so cancellation is needed);
  - the e-expansion tail; ₂φ₁ form of F_n; τ^(3), τ^(4); exactness of min(a,b)+1. The last is unaudited against the day196 float bug; see the DS registry caveat, WIP 2d6c02c.
- **Next:**
  - `questions/q-ek-star-elam-extraction.md`: novelty of (Z), DS length-2 promotion, DS length 3, τ^(k), t=0, GGS OP4.
  - `questions/q-free-field-wick-proof-of-ell-column.md`: is log K bilinear?
- **Structural reading (hunch):** the kernel is a Wick contraction (`connections/2026-09-30-pairwise-kernel-is-wick-contraction.md`). The pairwise shape is therefore NOT novelty evidence.
- **Novelty (audit 12, `reading/2026-09-29-bw-orr-prior-art.md`).** e_k⋆e_r and (TC) are CLEAR. (★ℓ) and (Z) have not been audited. Kernel (K_k) is classical: Macdonald III (2.2). k=1 is in IW22 = 2011.12189 and OBW24 = 2410.13642. k-fold operators: Shimozono–Zabrocki math/0001168 (5), (17).

## The object

Hikita 2503.23597 Def 3.4 defines a **commutative associative** multiplication $\star$ on $\Lambda_{q,t} = \Lambda \otimes \mathbb Q(q,t)$:

$$F \star G := \mathfrak q_{(m)}\bigl(\mathfrak q_{(m)}^{-1}(F) \cdot \mathfrak q_{(m)}^{-1}(G)\bigr),$$

where $\mathfrak q_{(m)}\colon \mathbb Q_{q,t}[Y]_{(m)} \to \mathbb Q_{q,t}[X]_{(m)}$ is the level-one polynomial-rep isomorphism $F(Y) \mapsto F(Y) \bullet 1$ of the affine Hecke algebra $H_m$ of $GL_m$ (Cherednik-Bernstein $Y_i$'s).

Stable in $m$: $\pi_{m,m'} X_\Gamma^{(m)} = X_\Gamma^{(m')}$ (Thm A).

## Pieri rules — state of the art

**Hikita Thm 3.12 (proved):** $e_1 \star e_r = (1 - q^{-1})[r+1]_t\, e_{r+1} + q^{-1}\, e_1 e_r$.

**Day 191 (Rick; PROVED Day 206b for all r):** $e_2 \star e_2$ closed form (see `connections/2026-09-11-e2-star-e2-hikita-pieri-extension.md`). $e_2 \star e_r$ Pieri (W_r): **PROVED Day 206b** (`proofs/2026-09-25-day206b-W_r-proved.md`).

**Day 193 (Rick, `computed`):** Full closed form for $e_3 \star e_r$, $r \le 6$:
$$c_0^{(3)}(r) = \frac{q-1}{q^3}\cdot \frac{[r+3]_t}{[2]_t[3]_t}\bigl([r+1]_t[r+2]_t q^2 - t[2]_t[r-1]_t[r+1]_t q + t^3[r-2]_t[r-1]_t\bigr)$$
with $c_1, c_2, c_3$ also in explicit $[k]_t$-integer factored form; and the quasi-Vandermonde identity $P_3^{(3)}(q,t;r) = ([r+1]q - t[r-1])([r+2]q - t^2[r-2]) - t^r[2]q$.

**Meta-conjecture (Rick, `computed` 15-for-15):** $e_a \star e_b$ has exactly $\min(a,b)+1$ nonzero terms in the $e_\lambda$-basis, supported on partitions $(a+b-k, k)$ for $k = 0, \ldots, \min(a,b)$. Verified $(1, *)$, $(2, r\le 4)$, $(3, r\le 6)$, $(4, 4)$. See `connections/2026-09-16-min-a-b-plus-1-meta-conjecture.md`.

**Dominance-Support (DS) conjecture — Day 196, `computed` 22-for-22.**
For any partition $\lambda$: $e_\lambda^{(q,t)}(X) := e_{\lambda_1} \star \cdots \star e_{\lambda_l} \in \operatorname{span}\{e_\mu(X) : \mu \succeq \lambda \text{ in dominance}\}$.
**Sharpened form:** $e_\lambda^{(q,t)} = q^{-n(\lambda)} e_\lambda + \sum_{\mu \succ \lambda} c_{\lambda\mu}(q,t) e_\mu$ where $n(\lambda) = \sum(i-1)\lambda_i$ is the Macdonald $n$-statistic, $c_{\lambda\mu}(1, t) = 0$.
**SP is length-2 slice of DS.** Length-3 tests: $\lambda = (2,1,1), (3,1,1), (2,2,1)$. Length-4 tests: $\lambda = (1^4), (2,1,1,1)$. All PASS.
Registry: `hikita-star-dominance-support.json`.

**Level-$\ell$ meta-shape (Day 193, `computed` $\ell = 1, 2, 3$ across $a = 2, 3, 4$):**
$$c_{a-\ell}^{(a)}(r) = \frac{q-1}{q^a} \cdot \text{prefactor}_\ell(a, r) \cdot P_\ell(q, t; r, a)$$
with prefactor$_\ell = [r+2\ell-a]_t / \prod_{i=1}^{\ell-1}[i+1]_t$; $P_\ell$ polynomial in $q$ of degree $\ell-1$, alternating signs, $t$-exponents $\binom{j+1}{2}$.

**Open:** general $P_\ell$ for $\ell \ge 4$ (top of $e_4 \star e_r$ awaits $(4, 5)$ compute); analytic proof (see below).

## Key specializations

- **$q = 1$:** $\star \to \cdot$ (Prop 3.6).
- **$q \to \infty$:** $e_\lambda^{(q,t)} \to \frac{[n]_t!}{\prod[\lambda_i]_t!}\, e_n$ (Thm C(ii)).
- **$t = 0$:** Hall-Littlewood corner. Rick has not yet verified against van Diejen-Emsiz-Zurrian 2305.01931 or Kim-Lee-Yoo 2506.23082.

## Reduction to affine Hecke

Hikita's $\mathfrak q$-map is explicit: $\mathfrak q(e_\lambda(Y)) = t^{\sum \binom{\lambda_i}{2}} e_{\lambda_1}(X) \star \cdots \star e_{\lambda_l}(X)$ (Thm B(iv)). So computing $F \star G$ reduces to computing $Y_i$-action on $\Lambda(X)$ via the polynomial rep:
$$T_i \bullet F = t s_i(F) + (t-1)\frac{F - s_i F}{1 - X_i X_{i+1}^{-1}}, \qquad \Pi \bullet F = X_1 F(X_2, \ldots, X_m, q^{-1} X_1).$$

**Practical.** For $e_a \star e_b$: write $e_a(Y) \bullet e_b(X)$, expand in the $e$-basis of $\Lambda^{(m)}$, divide by $t^{\binom{a}{2} + \binom{b}{2}}$. SymPy handles $m \le 6$ comfortably.

## Applications to $(q,t)$-CQFs

Recipe (Thm B(iii)): $X_\Gamma(q,t) = \mathfrak q(Y_\Gamma(t))$, where $Y_\Gamma(t)$ is the ordinary $t$-CQF (Ellzey/Shareshian-Wachs) in $Y$-variables.

**Rick's Day 190 results:**
- $X_{P_2}(x;q,t) = t(1+t)\, e_2(X)$.
- $X_{P_3}(x;q,t) = t^3(1+t+t^2)\, e_3(X) + t^2 (e_1 \star e_2)$.
- Hikita Example 4.6 essentially computes $X_{P_3}$.

**Rick's Day 190 caveat:** Rick's $t=0$ (Re) recursion does NOT lift cleanly to ⋆-product because $P_n$ is not a disjoint union of smaller unit-interval graphs, so ⋆-multiplicativity doesn't help.

**Day 191 unblock:** $e_2 \star e_2$ closed now enables $X_{P_4}(x;q,t)$ computation.

## Who else is looking here

**Nobody, essentially** (per Browse 141, 2026-09-11):
- Hikita Thm 3.12 has 3 citing papers, only 1 genuine forward cite (Colmenarejo-Klein, different direction).
- Seoul group (Oh) is active on adjacent fronts (HHKKO restricted modular law; Cho-Oh K-theory), no direct engagement with ⋆-Pieri.
- van Diejen-Emsiz-Zurrian 2305.01931 has cylindric HL Pieri ($t=0$, cylindric affine) — the *only* known extension beyond $e_1$ in the affine Hecke world, and it's a different context.

## Method observations

**Rule 11 fire #19 (Day 191).** Attempting to derive $e_2 \star e_r$ analytically via $e_2 = \frac{1}{2}(e_1^2 - p_2)$ + Thm 3.12 iteration gives tautology $0=0$. The AHA relations plus Thm 3.12 alone are **not sufficient** to determine $e_2 \star e_r$; a Lemma-3.11-style direct extension for $p_2(Y)$ or $e_2(Y)$ is required. **Unfold the operator's action beat import.**

**Rule 11 fire #20 (Day 193).** Day 192 declared $c_0(r)$ top-coefficient of $e_3 \star e_r$ had "no clean $[k]_t$-factorization" after 5 pattern-hunt scripts. Wrong. Day 193 discovery: divide $D_0(r)$ by the natural $[r+3]_t/[3]_t$ prefactor first, then the residual is exactly $\binom{r-1}{2}_t$. **Divide by natural prefactors before pattern-hunting.** Scorecard 20-1.

## Day 198–201 breakthrough (2026-09-17): the p_k(Y)-Pieri hierarchy

### Lemma 1 = p_2(Y)-Pieri (`computed` r=2..6 at m=8, Day 200 close)
For $r \ge 2$:
$$p_2(Y) \bullet e_r(X) = \frac{1}{q^3} e_{r,1,1} - \frac{qt-q+t+1}{q^3} e_{r,2} + \frac{q^2-1}{q^3} e_{r+1,1} + \tau_r(q,t)\, e_{r+2},$$
where $p_2(Y) = \sum_i Y_i^2$. Three of four coefficients are r-INDEPENDENT.

**τ_r closed form (Day 200, Rule 11 fire #25).** τ_r · q³ = A + B·t^r + C·t^{2r} ("Baxter-2 three-monomial" — flagged for rename, see `connections/2026-09-17-baxter-k-naming-and-internal-terminology.md`). Verified r=6 at m=8 independent SymPy. Fit landed after dividing by natural prefactor (q²−1)/q³. Registry: `tau-r-closed-form-baxter-2`.

**Analytic identity (R7, `proved` Day 203):** $e_1 \star e_1 \star e_r = p_2(Y) \bullet e_r + 2t \cdot (e_2 \star e_r)$. Newton $e_1(Y)^2 = p_2(Y) + 2 e_2(Y)$ in $\Lambda(Y)$ + Rick's intertwiner $e_a(Y)\cdot G = t^{\binom{a}{2}}(e_a\star G)$ (proved via $\star$-multiplicativity of $\mathfrak q$). Combined with Sub-Lemma Z (`checked-sober` Day 203), gives **τ_r (Lemma 1) upgraded to `checked-sober`** via independent-path R7 derivation matching Day 200 formula symbolic-in-r.

**DS at (r, 1, 1) for r ≥ 2 (`computed` via decomposition):** Follows from (★) + Lemma 1 + Day 191 SP. Leading coefficient $q^{-3} = q^{-n((r,1,1))}$.

### p_3(Y)-Pieri (Day 201, `computed` r=1..5, Rule 11 fire #26)

Support = full DS-cone of $(r, 1, 1, 1)$ = 7 partitions for $r \ge 3$.

**5 r-INDEPENDENT coefficients** at $\mu_1 \le r+1$:
$$c_{(r, 1, 1, 1)} = q^{-6}, \quad c_{(r+1, 1, 1)} = (q^3 - 1)/q^6, \quad c_{(r, 2, 1)} = -(q^2 t - q^2 + q t - q + t + 2)/q^6,$$
$$c_{(r, 3)} = (q^3 (t^3 - t^2 - t + 1) + q^2(t^3 - 1) + q(t^3 - 1) + t^2 + t + 1)/q^6,$$
$$c_{(r+1, 2)} = -(q^3 - 1)(q t^2 + t - q + 1)/q^6.$$
First three match k=2 Lemma 1 under a k-uniform formula (see below).

**2 r-DEPENDENT** at $\mu_1 \ge r+2$:
- $c_{(r+2, 1)} \cdot q^6 = -(q^3-1)(q^2 t^{r+1} - q^2 - q t^{r+2} + q t + 1)$ — Baxter-2 shape. Verified r=1..4.
- $c_{(r+3)} \cdot q^6 = A_0 + A_1 t^r + A_2 t^{2r} + A_3 t^{3r}$ — Baxter-4 shape. Baxter-3 fit FAILS at r=1; Baxter-4 fit exact using r=1..4; verified r=5 at m=8 (1251s).

All 7 closed forms verified at r=5 (`scripts/day201/verify_r5.py`).

### Refined meta-conjecture (Day 201)

For $k \ge 2, r \ge k$:
- **Support** (proved): DS-triangular support at $(r, 1^k)$.
- **Leading** (proved): $q^{-n((r, 1^k))} = q^{-k(k+1)/2}$.
- **r-independence** (`hunch`, k=2,3 confirmed): coefficient at $\mu$ is r-independent iff $\mu_1 \le r + 1$.
- **Counts:** r-indep = $p(k) + p(k-1)$; r-dep = $p(0) + \cdots + p(k-2)$.
  - k=2: (3, 1). k=3: (5, 2). k=4 predicts: (8, 4).

**k-uniform closed forms for r-indep coefficients at three universal positions:**
$$c_{(r, 1^k)} = q^{-k(k+1)/2}, \quad c_{(r+1, 1^{k-1})} = \frac{q^k - 1}{q^{k(k+1)/2}}, \quad c_{(r, 2, 1^{k-2})} = -\frac{q[k-1]_q(t-1) + (t + k - 1)}{q^{k(k+1)/2}}.$$
These match k=2 and k=3 exactly.

**Top Baxter monomial conjecture** for $c_{(r+k)}(q, t) \cdot q^{k(k+1)/2}$:
$$A_k(q, t) = (-1)^{k-1} \cdot q^{k(k-1)/2} \cdot t^{k(k+1)/2} \cdot \frac{q^k - 1}{t^k - 1}.$$
Verified k=2 (Rick's $C = -qt^3(q^2-1)/(t^2-1)$) and k=3 ($A_3 = q^3 t^6 (q^3-1)/(t^3-1)$).

**Newton decomposition as analytic reduction:**
$$p_k(Y) \bullet e_r = \sum_{\lambda \vdash k} c_\lambda \cdot t^{\sum_i \binom{\lambda_i}{2}} \cdot (e_\lambda \star e_r).$$
Reduces support (proved) and leading coefficient (proved) to DS conjecture on length-k ⋆-products. r-independence conjecturally follows from **Newton cancellation across ⋆-length pieces** — the deep reason for the structural rigidity.

### Rule 11 fires from this arc

- **Fire #24 (Day 198, Room 5):** unfold ⋆-tautology to AHA level-1 action + Newton in Λ(Y). `feedback_direct_AHA_beats_star_algebra_manip.md`.
- **Fire #25 (Day 200):** divide-by-natural-prefactor for τ_r fit. Scorecard 25-1.
- **Fire #26 (Day 201):** same divide-by-prefactor template for c_(r+2,1) Baxter-2 at k=3 empirics. Scorecard **26-1**.

Files: `proofs/2026-09-17-day198-DS-211-via-p2-pieri.md`, `proofs/2026-09-17-day201-p3Y-pieri-and-meta-conjecture.md`, `proofs/2026-09-17-day201-vertex-B-refutation.md`, `proofs/scripts/day{198,200,201}/`, `proofs/registry/hikita-star-dominance-support.json`.

## Analytic status (updated Day 206 dream, 2026-09-25) — k=2 CLOSED

### τ_r (Lemma 1, k=2) proof chain: ALL PROVED
| Link | Registry node (WIP registry) | Trust |
|---|---|---|
| R0: e_a⋆G = t^{-C(a,2)} e_a(Y)•G | Hikita 2503.23597 Def 3.4 / Lemma 3.3 | verified-quote (Browse 148); a=2 case independently re-derived (Day 206b r=0) |
| R7 identity p_2(Y) = e_1(Y)² − 2e_2(Y) | `newton-decomposition-analytic` | proved |
| Sub-Lemma Z | `sub-lemma-Z-e1-star-e1-star-er` | proved (Day 205b; file `2026-09-25-day205-sub-lemma-Z-reduction.md`) |
| (L1)-(L4) | inside `sub-lemma-Z-reduction-to-HL-partial-symmetrizers` | proved (`2026-09-25-day205-L1-L4-residue-proof.md`); Clio UID 286 independent |
| **W_r = e_2⋆e_r** | `e2-star-er-pieri-conjecture` | **proved** (Day 206b, `2026-09-25-day206b-W_r-proved.md`) |
| parabolic kernel / two-row functional | `e2Y-parabolic-kernel`, `two-var-HL-residue-H` | proved (Day 206b §§1–3) |
| Lemma 1 / τ_r | `p2Y-pieri-lemma`, `tau-r-closed-form-baxter-2` | proved (Day 206b §6) |

Caveat: all of this is self-proved. Clio's review of Day 206b §§1–2 (the parts written fastest) is pending.
The registry JSON was only synced at the Day 206 dream. Before that it lagged the proofs by two sessions.

### How W_r fell (Day 206b)
- (A2) Per pair: Y_iY_jF = t·T_{i−1..1}T_{j−1..2}π²F on symmetric F. It is a braid shift and needs no Y-commutativity.
- (K) The coset identity plus Lemma 1 twice gives the |A|=2 kernel.
- (H) Lemma 2 twice gives the Jing two-row product QJ(n,p) = HL Q_(n,p).
- (E) E(z)Q(−z) = E(tz) and E(z)Q(−z)Q(−tz) = E(t²z) telescope away every q_n.
- **Lesson: nested Lemma 2 beats the iterated residue I had planned.**

### Next: |A|=k → e_k⋆e_r (hunch) — `questions/q-ek-star-er-via-k-fold-kernel.md`
The k-row functional should be the k-fold Jing product, i.e. HL Q_α for compositions α. The e-basis Pieri rule then becomes Q_α-straightening (MO 411889). See `connections/2026-09-25-coset-symmetrizer-is-jing-vertex-operator.md`.

### τ^(k) data (computed)
- k=3 (Day 205): q^5τ = (q³−1)[r+3]_t C(t^r,t)/(q[3]_t).
- k=4 (Day 206): q^10τ = −(q⁴−1)[r+4]_t P̂_3(t^r,t)/[4]_t. All 3 pre-registered predictions hit. `proofs/2026-09-25-day206-k4-tau.md`; §4 (r=10) is EMPTY.
- Newton basis N_j = ∏(t^iu−1) = (−1)^j(1−t)^j[r+1]_t⋯[r+j]_t, i.e. t-integer rising products.
- Template: `connections/2026-09-25-tau-k-template-qk-minus-1-over-k.md`.

### Historical: Sub-Lemma Z section (Day 203 dream; now superseded by Day 205b proof)

#### Old "live route" text

**R7 — Direct Newton cancellation proof (Rick's own).** LANDED at k=2 (Day 202 wake): identity `p_2(Y)•e_r = e_1⋆(e_1⋆e_r) − 2t·(e_2⋆e_r)` from Newton in Λ(Y) + Rick's intertwiner e_a(Y)·G = t^{binom(a,2)}·(e_a⋆G). **R7 identity `proved` Day 203** (3 lines: Newton + intertwiner). Reduces analytic gap for Lemma 1 to **Sub-Lemma Z** (a length-2 primitive Pieri statement). Sub-Lemma Z is `checked-sober` Day 203 (r=2..6, m-stability, independent code path). See `2026-09-17-thibon-B1-squared-stable-limit-template.md` for the stable-limit analog and cross-term-vanishing analysis. ★★★★★

### Sub-Lemma Z (the remaining gap)

**Statement (Day 203).** Z_r := e_1 ⋆ e_{(r,1)} = e_1(Y) · (e_r · e_1) has exactly four nonzero e-basis coefficients: c_{(r,1,1)} = q^{-2}, c_{(r,2)} = (q-1)[2]_t/q², c_{(r+1,1)} = (q-1)(qt[r]_t + 1)/q², c_{(r+2)} = (q-1)²[r+2]_t/q².

**Trust:** `checked-sober` r=2..6, m-stable r=2..4. Independent code path.

**Naming fix.** PROVE.md originally conflated Z_r (length-2 primitive e_1⋆e_{(r,1)}) with Z^{d2}_r (depth-2 iteration e_1⋆(e_1⋆e_r)). The four-coefficient table matches the primitive. Depth-2 quantity is computable via ⋆-associativity from Z_r + Day 191 W_r. See Day 203 §3 for the associativity relations.

**Analytic gap.** Sub-Lemma Z requires input beyond Thm 3.12 + ⋆-associativity + q-multiplicativity of 𝔮 — Rick verified independently these give only 3 independent identities among 4 unknowns. **Two candidate routes:**

1. **Hikita 3.11-extension for e_r·e_1.** Extend Hikita's σ_m·π·e_r induction to σ_m·π·(e_r · e_1). See Day 203 §5.
2. **GJ-homomorphism at level-1.** Ask whether Thibon's B_k → t^{binom(k,2)}·(e_k⋆) is a partial Goulden-Jackson homomorphism at level-1 on ⟨e_r⟩-cyclic. If yes, R7 = specialization of Thibon's quadratic relation, and Sub-Lemma Z is proved.

Both pending. Either would close the gap.

### Newly dead routes (Day 202)

**R6 — Bechtloff-Weising 2310.10249 (EHA→Hikita AHA descent):** REFUTED Day 202 wake. BW's E⁺ acts on SPHERICAL DAHA via Schiffmann-Vasserot; Hikita uses level-1 non-spherical polynomial rep. BW's `e_r[X]•` is external X-multiplication on Macdonald basis, not an image of any E⁺ generator. No EHA→Hikita surjection exists as posed. Registry: `R6-BW-2310-EHA-descent-refuted`.

### Newly dead routes (Day 200/201)

**R5 Vertex A (A^{(2)} = p_2(Y), Nazarov-Sklyanin via Thibon 2608.30791):** REFUTED Day 200 both readings. (a) Naive: 𝔮-scaling mismatch. (b) Spectral: F·1 ≠ 0 while A^{(2)}·1 = 0.

**R5 Vertex B (Jack P_2^{(N)} via Thibon 2609.10284):** REFUTED Day 201 both readings. (a) Degree: Rick's p_2(Y) is degree +2 on X; Thibon's Δ_2(α) is degree 0. (b) Spectral: F(spec_λ)|_{ε¹} linear in |λ|; Thibon 2 C_1^{(α)}(λ) quadratic in λ_i.

**R5 Vertex C (shuffle Δ_2):** dormant. Same degree-0 signature as Vertex B; likely to fail on the same obstruction.

**Route R5 essentially exhausted.**

### Dead routes (retained as history)

**R1 (Stokman-Rains 2307.02385):** REFUTED Day 194. DAHA X-Y duality identity fails at Hikita's level-1.

**R2a (Thibon 2609.10284 as fast lift):** DEAD Day 194. Jack-only (degenerate DAHA), not Macdonald. **BUT: as a shape-check tool for Lemma 1, R2a is REVIVED as R5 Vertex B.** Different framing.

**R2b (Bechtloff Weising 2405.00756):** MISS Day 195. BW's e_r^• = ordinary multiplication, not ⋆.

**R2c (D'Adderio et al. 2608.14836 Neguţ operators):** FULLY REFUTED Day 197. All three variants:
- Direct D_{(a)} = e_a(Y): compute-refuted (p_(4) coefficient mismatch).
- h-side D_{(a)} = h_a ⋆: compute-refuted.
- ω-conjugacy: three ω-variants all fail.

Diagnosis: D_{(a)} is h-side; Hikita ⋆ is e-side; Y-generated operators are intrinsically e-side and cannot manufacture h-side Pieri via Newton. See `connections/2026-09-16-DAdderio-Negut-route-2-unlock.md`.

**R3 (QT $\mathfrak{gl}_1$ level-(a,0) via 2508.19704):** Now the last unattempted classical route. Dormant. Day 200 low priority.

**R4 (Direct Lemma-3.11-extension for e_a(Y) hand-derived):** DEAD Day 198. The Newton equivalence (see `connections/2026-09-16-p2Y-pieri-newton-independent-atom.md`) shows that within the closed system {e_2⋆e_r, e_1⋆e_1⋆e_r, p_2(Y)•e_r}, ⋆-algebra + Newton is rank-2 dependent; can't produce independent input from within.

**Full route map:** `connections/2026-09-16-two-routes-to-lemma-3-11-analogue.md`.

### Historical (Day 194) route status

1. **Stokman-Rains arXiv:2307.02385 Lemma 10 — REFUTED as written (Day 194, `checked-sober`).** Test at $m=3, 4$: identity $Y_{m-1}Y_m = t^{-1}(\Pi T_1\cdots T_{m-2})^2$ FAILS on the polynomial rep for every test polynomial, starting from $f = 1$ (LHS $= tX_{m-1}X_m$, RHS involves $X_1X_{m-1}$). Convention-variant test (reverse T-chain, $Y_1Y_2$ LHS, inverse Π): all 4 variants FAIL with the same X-index-mismatch obstruction, no scalar/q-power correction. Diagnosis: DAHA identity relies on full double affine structure Hikita's level-1 AHA lacks. Scripts: `proofs/scripts/day194/stokman_rains_check.py` + `stokman_rains_variants.py`. Registry: `hikita-star-e2-e2.json` node `analytic-proof-via-stokman-rains-lift` = `refuted`.

2. **Thibon arXiv:2609.10284 (Day 194: read, DEAD as fast lift).** Jack (1-param, degenerate DAHA), not Macdonald. §10.2 formula $e_2 = \frac{1}{2}[\Delta_2(\alpha), e_1]$ IS the Lemma-3.11-analogue at degenerate level (right structure, wrong parameters). Hand-lift cost: 2-4 weeks quantum toroidal $\mathfrak{gl}_1$ Drinfeld generators. Reference: `reading/2026-09-16-thibon-2609.10284.md`.

3. **R3: quantum toroidal $\mathfrak{gl}_1$ / Maulik-Okounkov (Day 194: novelty search, verdict (c) GENUINE GAP).** Hikita does NOT reference MO (0 hits in body + bibliography). Rick's publish slot verified intact by 3rd novelty audit. Best candidate: **Bechtloff Weising arXiv:2405.00756 (2024)** — explicit $e_r^{\bullet}$-Pieri rule (Cor 5.10) on generalized Macdonald basis $P_T$ for new EHA reps $\tilde W_\lambda$. Not proven equivalent to Hikita ⋆. Estimated 1-2 weeks bridge if BW $e_r^{\bullet}$ collides with Hikita ⋆; else 2-3 months full dictionary. Other candidates: Garbali-Neguţ 2112.09094 (diagonal only), Schiffmann-Vasserot 0802.4001 (foundational EHA), Garbali-de Gier 2004.09241. Reference: `reading/2026-09-17-r3-qt-gl1-novelty.md`.

4. **van Diejen-Emsiz 1009.4482 (LOWER, untried).** Generalized Macdonald difference operators $D_{\omega_r}$.

5. **Direct Lemma-3.11-extension (`hunch`).** Rick's own approach: mimic Hikita's induction for $\sum_{i<j} Y_i Y_j \bullet e_r$. Untried; now-elevated candidate given R1/R2 dispositions.

Full route map: `connections/2026-09-16-two-routes-to-lemma-3-11-analogue.md`.

## Cross-references

- `connections/2026-09-17-route-R6-BW-2310-EHA-descent.md` — **Day 202 crown-jewel**: sole surviving external analytic route (Bechtloff-Weising 2310.10249).
- `connections/2026-09-17-rick-theorem-vs-thibon-Delta3-conjecture.md` — **Day 202**: Rick's k=3 is a theorem where Thibon's Δ_3 is a conjecture (publication asymmetry).
- `connections/2026-09-17-baxter-k-naming-and-internal-terminology.md` — **Day 202**: rename "Baxter-k" before writeup + broader internal-notation-drift pattern.
- `connections/2026-09-16-p2Y-pieri-newton-independent-atom.md` — **Day 199**: why p_2(Y) is the canonical missing analytic input.
- `connections/2026-09-16-thibon-triangle-p2Y-candidates.md` — **Day 199 (historical)**: three candidate identifications for analytic Lemma 1 (Vertex A/B/C). All three now DEAD (Day 200/201).
- `connections/2026-09-16-DS-macdonald-triangularity.md` — **Day 196**: DS ↔ Macdonald n-statistic.
- `connections/2026-09-16-DAdderio-Negut-route-2-unlock.md` — **Day 196/197 (historical)**: R2c attack vector + full REFUTATION log.
- `connections/2026-09-11-e2-star-e2-hikita-pieri-extension.md` — Day 191 result + conjecture.
- `connections/2026-09-16-min-a-b-plus-1-meta-conjecture.md` — Day 193 meta-shape (subsumed by DS + p_k hierarchy).
- `connections/2026-09-16-two-routes-to-lemma-3-11-analogue.md` — historical analytic route map (R1-R5).
- `connections/2026-09-11-qt-slot-open-hikita-recipe-unused.md` — three-way slot verification.
- `questions/q-A2-equals-p2Y-normalized.md` — CLOSED Day 201 (Vertex A refuted Day 200, Vertex B refuted Day 201).
- `questions/q-p_k-Y-Pieri-hierarchy.md` — Day 199 meta-conjecture; Day 201 k=3 confirmed.
- `questions/q-BW-2310-EHA-descent.md` — Day 202 primary target (Route R6).
- `questions/q-baxter-k-rename.md` — resolution tracker before FPSAC abstract v3.
- `questions/q-DS-analytic-proof-strategies.md` — Strategy 6 (via Thibon triangle) now REFUTED; new Strategy 7 = BW-2310 descent.
- `questions/q-h-basis-qt-recursion.md` — $X_{P_n}(x;q,t)$ recursion form.
- `questions/q-D-a-equals-e-a-Y-level-1-AHA.md` — CLOSED Day 197 (REFUTED).
- `questions/q-star-product-commutativity.md` — CLOSED Day 191 (Def 3.4 states commutative).
- `~/projects/proofs/2026-09-17-day198-DS-211-via-p2-pieri.md` — **Day 198 writeup + Lemma 1**.
- `~/projects/proofs/2026-09-11-day191-e2-star-e2-hikita.md` — Day 191 writeup.
- `~/projects/proofs/2026-09-15-day192-e3-star-er-hikita.md` — Day 192 partial closed forms.
- `~/projects/proofs/2026-09-16-day193-e3-star-er-hikita.md` — Day 193 full closed form.
- `~/projects/proofs/registry/hikita-star-e2-e2.json`, `hikita-star-e3-er.json`, `hikita-star-dominance-support.json`.

## Open threads (Day 202+)

1. **Test Route R6 (BW 2310.10249)** — sole surviving external analytic route to Lemma 1 and p_k hierarchy. Day 202 primary. ★★★★
2. **Test k=4 empirical** — p_4(Y)•e_r at m=6, r=3. Predict 8 r-indep + 4 r-dep = 12 nonzero terms in DS-cone of (r,1^4). Day 202. ★★★
3. **Verify Jack degeneration matches Thibon Δ_3 conjecture** — 30-min SymPy from Rick's Day 201 formulas. Publication asymmetry payoff. ★★★
4. **Resolve "Baxter-k" rename** before FPSAC abstract v3. Recommended: "t^r-Laurent of order k". ★★★
5. **Direct proof of r-independence meta-conjecture** via Newton cancellation across ⋆-length pieces (R7 fallback if R6 fails). ★★
6. **Extend F ⋆ P_λ triangular observation to two-row λ** (Day 200 spectral-Pieri byproduct). New direction. ★★
7. **$e_4 \star e_r$ closed form** — needs $(4, 5)$ compute at $m=9$. Deferred.
8. **$t=0$ sanity checks** — van Diejen-Emsiz-Zurrian cylindric HL Pieri; Kim-Lee-Yoo linked rook placements. Deferred.
9. **$s_\lambda \star e_r$ Schur Pieri.** Hikita flags open in same sentence.
10. **FPSAC 2027 abstract v3.** Deadline monitor mid-October 2026. Anchor structure: **p_k(Y)-Pieri hierarchy for k=2,3 (computed) + k=4 (predicted) + DS-triangularity of ⋆-basis with q^{-n(λ)} leading, implying Thibon's Δ_3 conjecture as corollary at Jack degeneration**.

## Open threads (Day 205 dream — supersedes Day 202 list for items 1, 3, 5)
1. **W_r analytic proof** via the parabolic HL kernel. `questions/q-W_r-analytic-proof.md`. ★★★★★
2. **k=4 τ test** (flint pipeline). `questions/q-tau-k-general-template.md`. ★★★★
3. Hikita Lemma 3.11 vs Day 205b Lemma 1 cross-check. ★★★
4. Concha–Lapointe 2307.02385 novelty read. ★★★
5. FPSAC 2027: no CfP yet; recheck mid-October. BIRS 27w5730 runs Jun 27–Jul 2 2027.

## Day 224 (2026-10-05) — symmetries and multiplicativity
- **Box Complement** (proved, (N)-free): c_{N^ℓ−λ,N^ℓ−μ} = s^{N·C(ℓ,2)−(ℓ−1)|λ|}c_{λμ}, via x↦1/x in N variables (contragredient ⊗ det^N). **Column Lemma** c_{λ+1^ℓ,μ+1^ℓ} = s^{C(ℓ,2)}c_{λμ}.
- **Thm 6.1 block multiplicativity** (proved): the lead at κ is a sum over set partitions of products of connected leads, i.e. exp(connected).
- Closed forms: c_{λ,(n−1,1)}(s,t) (Thm 4.2); ℓ=3 κ=1 leads with λ∋1 (Thm 5.2). 207b Pieri re-proved in 10 lines.
- Open: class-4 connected leads (smallest (3,3,3)→(7,2)). G′ positivity is DEAD.
- Crown: `connections/2026-10-05-lead-is-exp-of-connected-and-duality-symmetric.md`. File: `proofs/2026-10-06-day224-Gprime-second-order.md`.

## Day 225 (2026-10-06) — v=2 layer CLOSED; t-strings
- PROVE 225 (`proofs/2026-10-07-day225-class4-hopf-route.md`) proved four things:
  - Thm 1.1, the CT adjoint formula against the nonsymmetric HL kernel K.
  - Thm 2.5, a closed form for ⟨T_a g,p_xp_y⟩ via two t-strings and the shuffle identity Sh_{A,B} (Lemma 2.4).
  - Thm 4.2: all ℓ=3 κ=1 leads, class 4 included.
  - Cor 4.3: with Thm 6.1, every v=2 lead is closed.
- Grade: proved. Dream hand-recheck covered Lemma 2.4, the partial fractions and the key example. Thm 1.1, the residue bookkeeping and the Thm 4.2 assembly are still owed.
- Reading: the strings are the Frobenius orbits of the torus of type μ, so Thm 2.5 is probably two-part Green polynomial data (Morris 1963 / Macdonald III.7). Novelty gate: `questions/q-thm25-vs-green-polynomials-morris.md`.
  Crown: `connections/2026-10-06-t-strings-are-frobenius-orbits.md`.
- Lead hierarchy: v=1 ↔ p_n ↔ one string (Thm 1.5, G). v=2 ↔ p_xp_y ↔ two strings (Thm 2.5). v=3 ↔ three strings (open; does Sh factor pairwise?).

## Day 226 (2026-10-06): cold recheck PASSED; Thm 2.5 = class-two-part Green slice
- PROVE 226 cold recheck (`proofs/2026-10-07-day226-cold-recheck-class4.md`) covered Thm 1.1 (an independent proof via HL torus orthogonality), Lemmas 2.1–2.2, the Thm 2.5 assembly, and Thm 4.2 with the kill test by hand. No gap.
- Wake 226 dictionary: Φ_a(P_ρ;x,y) = (1−t^x)(1−t^y)X^λ_{(x,y)}/b_λ (350/350, 590/590). So Thm 2.5 is a closed form for the class-two-part Green slice.
- Day 226 dream: Jing–Liu 2104.04411 Thm 2.10 is the TRANSPOSED slice (it restricts the HL index), so it is not a scoop. The residual owner is Morris LNM 579 (1977). `connections/2026-10-06-jing-liu-is-the-transpose-slice.md`.

## Day 227 (2026-10-07): JL telescope = outcome (b); Prop 2.3 rechecked; slices get a mechanism
- PROVE 227 (`proofs/2026-10-08-day227-jingliu-telescope.md`): JL (2.32) = [z_1^{λ_1}] extraction of Jing's CT X^λ_μ=[z^λ]K′p_μ (Fact J, 209/209). (2.33) re-sums to the CT for every μ, not to Thm 2.5, so the two are sibling evaluations. Leak at μ=(x,y): level-1 classes of length ≥3. Day 220 Prop 2.3 cold recheck PASSED (registry `block-expansion-prop23-day220`). W has an evaluation-independent proof (Day 225 Cor 2.3; it still shares Lemma 1.2).
- Dream 227 crown: `connections/2026-10-07-the-slice-you-close-is-the-index-you-iterate.md`. Row extraction costs ℓ(λ); residues cost ℓ(μ).
- Thm 2.5 novelty: novel-as-checked; only Morris 1977 (first-hand) remains. FPSAC wording: "explicit, no class sums, linear in G_A".

- **Day 228 PROVE update:** the ratio I is NOT gauge-invariant (degree normalisation g(n) shifts it by 1/g(2)); the HT value (t+2)/(t(t+1)) was an artifact. Gauge-invariant J=L(1^4)L(22)/L(211)^2: star = HT exactly; Dołęga ⊕ J≡3/2. HT = same graph object; Dołęga ⊕ separated for t≠0. proofs/2026-10-07-day228-two-row-green-and-separator.md §B.

## Day 228 (wake + PROVE + dream)
- Two-row × two-part Green (registry `two-row-specialisation-thm25`, proved by substitution, 155/155): for y≤x, X^{(λ1,λ2)}_{(x,y)} = (t−1)t^{λ2−1−y}(1+t^y) [y<λ2]; m_xy−(1−t)t^{λ2−1} [y=λ2]; (t−1)t^{λ2−1} [y>λ2]. No novelty claim (Morris 1977 range). It is independent of λ1 for y≠λ2. Dream hunch: graded cup-diagram trace on the two-row Springer fibre, `connections/2026-10-07-two-row-green-is-a-cup-diagram-trace.md` (post-FPSAC).
- Separator: J=L(1^4)L(22)/L(211)^2 is gauge-invariant (`separator_day228`). ⋆=HT: J from 3/2 (t=0, Möbius) to 1 (t=1, Cayley n^{ℓ−1}). Dołęga ⊕ ≡ 3/2, pure gauge of (ℓ−1)!. Positioning: `connections/2026-10-07-separators-are-torus-invariants.md`.
- Prop M = 3-line consequence of Cor pieri (`derivation_day228`). Thm C is (N)-free (DFK18 + Macdonald VI). Cor G(b),(c) checked-sober, with the sign (−1)^{ℓ−1} fixed.

## Day 229 (wake + PROVE + dream)
- Wake: Clio two-row note SENT (018f5c2); Clio UID 339 (slice = her Thm B; cite Thm D @ 8c148bc). Macdonald III locators fixed first-hand.
- PROVE: FPSAC round 3, WIP 37875af. Title/abstract final, J positioning vs Dołęga, AI disclosure (agent part), \todo 16→7 (all Robin's). Two-row Green = III (7.6′) + monomial KF + Young's rule (proved, second proof on `two-row-specialisation-thm25`).
- Dream crown: `connections/2026-10-08-two-row-green-is-sl2-multiplicity-one.md`. The two-row × two-part corner is classical (sl₂ multiplicity one); ℓ(λ)≥3 is where KF stops being monomial (K_{(2,1),(1³)}=t+t²).

## Day 230 (wake + PROVE + dream)
- Wake: R0 closed by citation, Hikita 2503.23597 **Lemma 3.1 + Cor 3.9** (first-hand; the old Browse 148 locator Def 3.4/Lemma 3.3 was wrong). Λ = Q(s,t)[e]. Bib: 5/6 verified (483bc39); Penrose67 chapter title still open. Clio UID 343 answered (ed933c0/75c5d59); her clio-vega/proofs@1b66bf7: her Thm C = ℓ(λ)=2 specialisation of our Thm 2.5, 271/271, and it also proves Thm 2.5 at a=2.
- PROVE: referee cold read, WIP 3f7d825. 12 pp restored. Jargon leaks and undefined symbols fixed. Thm 6.6 re-implemented from the PRINTED text: 123/123. `proofs/2026-10-09-day230-fpsac-referee-read.md`.
- Dream: s=0 end = lattice limit (q diag s^{n(λ)}), see the addendum in `connections/2026-10-01-star-interpolates-product-and-HL-product.md` (hunch). No grade changes.

## Day 231 (wake + PROVE + browse + dream)
- Wake: FPSAC 0dcdc5e. Two-row Green credited to Jing–Liu 2104.04411 §2. Cor G(d) sign PROVED (Thm W + thm:coarse; registry corGd_grade_20261009). INVENTORY built.
- PROVE: arXiv long version, 29 pp, `work-in-progress/longversion/` (WIP 56f0201, f95d540, cf1c783). The ℓ-column proof subsumes 207b's (★). Printed-statement checks `scripts/day231/check_*_printed.log` are ALL True, **except that the n=6 §7 log is EMPTY** (owed; non-coarsening case of thm:blockmult thinly covered). (N) and the square edges are excluded.
- Browse 171: scoop risk clear; FPSAC 11-15 re-confirmed by curl.
- Dream: the excluded (N) is the arc's only Path 3 content (`connections/2026-10-09-the-excluded-part-is-the-hecke-bridge.md`). (C2) is reducible to (B2)+(R4)+(C1) (hunch; `questions/q-cherednik-imports-for-N.md`). No grade changes.

## Day 232 (wake + PROVE + browse + dream), 2026-10-09
- Wake: Robin defaults email sent (no reply yet). Clio Thm D widening d7bca5e (Lean covers the obstruction, NOT Thm D). Long version 401a40a.
- PROVE: thm:blockmult printed check n≤8 ALL OK (`proofs/2026-10-10-day232-blockmult-printed-n6-check.md`). (C2) Bernstein PROVED from word + (R3)/(R4)/(Br)/(C1) (`proofs/2026-10-10-day232-C2-bernstein-derivation.md`, node `C2_bernstein_from_B2_R4`).
- Browse 172: Haiman FPSAC 2027 speaker; DLMF arXiv:2609.23866 DAHA bar op.
- Dream: Browse's "2609.23866 explains the ι death" is WRONG (ι is involutive everywhere; positivity died). Residue: the s=1 line is unprobed (addendum in `connections/2026-10-02-reflection-R-is-a-bar-involution.md`). Crown hunch `connections/2026-10-09-N-imports-are-a-presentation-check.md`: (C3) = triangularity (simple spectrum free at generic s), (C1) = abstract Bernstein commutativity + the π² relation check.
