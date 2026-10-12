# Day 237 PROVE — §6 print gaps: Rem 6.3 (∇ bridge) and Rem 6.4 (DFK dictionary), §6 + App A cold read, s2b controls

Date: 2026-10-12. Long version WIP (work-in-progress repo) `longversion/longversion.tex`, eb12457 → **3c7f228** (pushed).
FPSAC (frozen at 7df658b) was not touched.

## Problem

Under the rule "the PDF is the claim", two printed sentences of §6 (`sec:nabla`) had only ever been checked by hand:

- (a) **Rem 6.3 (`rem:N-nabla`)**: with H̃_ν(x;q,t) := t^{n(ν)} J_ν[X/(1−t^{-1}); q, t^{-1}] and φ(F) := F[−εX/(1−t)],
  φ^{-1}H̃_ν(x;s,t) = t^{n(ν)} J_ν[εtX; s, t^{-1}] = (−1)^{|ν|} t^{|ν|+n(ν)} J_ν(x; s, t^{-1}), hence 𝒩 = φ^{-1}∇_{q=s}φ and
  t^{n(λ')} e^⋆_λ = φ^{-1}∇_{q=s}φ(e_λ).
- (b) **Rem 6.4 (`rem:N-DFK`)**: the dictionary to Di Francesco–Kedem arXiv:1704.00154 (DFK19), with its locators.

Then (c) cold-read §6 + App A, and (d) measure Clio's "vacuous control" flag on the s2b Thm 4.4/4.5 controls.

## (a) Rem 6.3: print check

Script: `work-in-progress/scripts/day237/rem63_bridge_check.py` (log `rem63_bridge_check.log`). It does not use the
day216* engine. Every object is built from scratch, in the power-sum coordinates p_1..p_n:
- P_ν(x;q,t) comes from Gram–Schmidt in the q,t-Hall pairing along dominance (Macdonald VI (4.7)). Dominance is a total order for n ≤ 5.
- J_ν = c_ν P_ν, where c_ν = ∏_{boxes}(1 − q^a t^{l+1}) (VI (8.3)).
- H̃_ν comes from the **Garsia–Haiman characterisation** (H̃[X(1−q)] ∈ span{s_λ : λ ⊵ ν}, H̃[X(1−t)] ∈ span{s_λ : λ ⊵ ν'},
  ⟨H̃, s_(n)⟩ = 1), solved as a linear system. So the printed normalisation of H̃ is a *claim* that gets tested; nothing is built from it.
- ∇ is defined by its eigenvalues t^{n(ν)}q^{n(ν')} on the GH H̃_ν. Sanity check: ∇e_2 = s_2 + (q+t)s_{11} (Haiman's convention).
- Every sign and exponent is taken from the PDF text (pdftotext of eb12457), including p_r[−εX] = (−1)^{r−1}p_r.

Claims checked:
- P1 H̃_ν = t^{n(ν)} J_ν[X/(1−1/t); q, 1/t], all |ν| ≤ 4 (symbolic).
- P2 φ^{-1}H̃_ν(x;s,t) = (−1)^{|ν|} t^{|ν|+n(ν)} J_ν(x;s,1/t), all |ν| ≤ 4. **The sign is (−1)^{|ν|}**, as printed.
- P3 𝒩 e_λ = φ^{-1}∇_{q=s}φ(e_λ), all |λ| ≤ 4, with 𝒩 diagonal on P_ν(x;s,1/t).
- P4 t^{n(λ')} e^⋆_λ = φ^{-1}∇_{q=s}φ(e_λ), all |λ| ≤ 4. Here e^⋆_λ is computed **from the printed §2 operators**
  (T_i, π, Y_i, e_k(Y) in increasing order, eq. (star-reading)) in m = |λ| variables. This is an end-to-end check of the
  printed last sentence, independent of the Day 236 print check of Thm 6.2.

Negative controls, each of which must break the claim:
- P2 with sign +(−1)^{|ν|+1}: breaks.
- P2 with n(ν) → n(ν') (non-self-conjugate ν): breaks.
- φ without −ε, i.e. φ^{-1}G = G[X(1−t)]: φ^{-1}H̃ is then **not** a scalar multiple of J (n ≥ 2), so it breaks. This is a genuine
  break and not a relabelling: −ε acts as ω up to sign, not as a degree scalar.
- P3 with ∇ eigenvalues n(ν) ↔ n(ν'): breaks for every n ≥ 2.
- P3 with s ↔ t applied to the whole right-hand operator: breaks for every n ≥ 2.
- P3 with φ without −ε: breaks for every n ≥ 2.
- P4 with t^{n(λ)} in place of t^{n(λ')} (λ ≠ λ'): breaks.

Result: **ALL True**, with 0 FAIL anywhere.
- `rem63_bridge_check.log` covers everything symbolically for n ≤ 3, plus n = 4 P1, P2 and their controls: 74 PASS, 0 FAIL.
  The process was then killed (exit 137, out of memory) in the symbolic n = 4 P3 linear solve. The log line records this.
- `rem63_bridge_check_n4pts.py`/`.log` completes n = 4 P3, P4 and their controls in exact rational arithmetic, at three rational
  points (s,t) = (3/7, 5/11), (−2/5, 7/3), (9/4, −4/13): ALL True, 51/51.

So the coverage is: P1 and P2 symbolic for |ν| ≤ 4; P3 and P4 symbolic for |λ| ≤ 3 and at three points for |λ| = 4. The printed
"Computer checks" sentence says exactly this.

**Verdict (a): Rem 6.3 is correct as printed.** The sign is (−1)^{|ν|} and the exponent is |ν| + n(ν).

**Printed correction (referee-level).** 𝒩 lives on Λ_m, but φ and ∇ live on Λ. The fix adds one sentence: the right side is
diagonal on the P_ν, so it preserves ker(Λ → Λ_m) = span{P_ν : ℓ(ν) > m}, and the identity holds for the induced operator.

## (b) Rem 6.4: the DFK dictionary, first-hand

Source: the arXiv e-print of 1704.00154 (latest version, v2). I compiled it locally and ran pdftotext, so the numbering below
is the arXiv numbering. Section order: 1 intro, 2 DAHA, 3 QTOR, 4 boso, 5 shuffle, 6 EHA, 7 Whittaker, 8 conclusion.

Every cited locator exists and says what we say:
- **(1.5)**: M_{α;n} := D_α((x_1⋯x_α)^n) = Σ_{|I|=α} x_I^n ∏_{i∈I, j∉I} (t x_i − x_j)/(x_i − x_j) Γ_I, with Γ_i the q-shift (1.2).
  α counts variables and n is the power, so our M_{k;1} is α = k, n = 1. ✓
- **Lemma 2.12**: τ+ = ad_{γ^{-1}}. Lemma 2.12 was *missing* from our printed citation, although "image under τ+" needs it. **Added.**
- **Lemma 2.16**: ρ(D_{α;n}) = q^{−αn/2} ρ(γ)^{−n} ρ(D_{α;0}) ρ(γ)^n.
- **Thm 2.17 / (2.11)**: D_{α;n}|_{S_N} = θ^{−α(N−α)} M_{α;n}, with θ = t^{1/2}.
- **Lemma 2.13**: τ− = ad_{η^{-1}}, η = exp(−Σ Log(Y_i)²/(2 Log q)).
- **Rem 2.14**: η^{-1} =: ∇^{(N)}, with ∇^{(N)}P_λ = C_N u_λ P_λ and u_λ = t^{((N−1)/2)|λ| − n(λ)} q^{|λ|/2 + n(λ')}.
- **(4.14)**: η^{-1} = ∇^{(N)} = C_N (t^{(N−1)/2} q^{1/2})^d (Σ^{-1}∇Σ)|_{t→t^{-1}}, with Σ: X ↦ X/(t−1) (Thm 4.7).
- **(6.3)**: T = [[1,1],[0,1]] and U = [[1,0],[1,1]], with T u_{a,b} = u_{a,a+b} and U u_{a,b} = u_{a+b,b}. §6.1 then gives T ↦ τ+, U ↦ τ−.
- **(6.5)**: u_{0,±k} = q^{k/2}/(1−q^k) p_{±k}. **(6.8)**: u_{±k,0} = q^{k/2}/(1−q^k) P_{±k}, where P_k = Σ Y_i^k.

**Composition by hand, all k.** It covers k = 1, 2 as asked. Use their (q,t) = (s, t^{-1}), so θ = t^{-1/2}, and N = m.
1. (1.5) with their t = our t^{-1}: (t^{-1}x_i − x_j)/(x_i − x_j) = t^{-1} a_{ij}, and Thm 2.5 (subset formula) then gives
   E_k = t^{k(m−k)} M_{k;1}.
2. (2.11): M_{k;1} = θ^{k(m−k)} D_{k;1}|_S = t^{−k(m−k)/2} D_{k;1}|_S.
3. Lemma 2.16 + Lemma 2.12: D_{k;1} = q^{−k/2} γ^{-1} e_k(Y) γ = s^{−k/2} τ+(e_k(Y)).
4. (6.3), (6.5), (6.8): τ+(p_j(Y)) ∝ T u_{j,0} = u_{j,j} = U u_{0,j} ∝ τ−(p_j(X)). The constants q^{j/2}/(1−q^j) are **equal**, so
   τ+(p_j(Y)) = τ−(p_j(X)). The τ± are algebra automorphisms, so τ+(e_k(Y)) = τ−(e_k(X)).
5. Lemma 2.13: τ−(A) = η^{-1}Aη = ∇^{(N)} A ∇^{(N)−1}.
6. Rem 2.14 in our variables: ∇^{(N)} = C_N (t^{−(m−1)/2} s^{1/2})^d 𝒩, where the eigenvalue t^{n(λ)}s^{n(λ')} is taken on P_λ(x;s,t^{-1}).
   Conjugating multiplication by e_k (degree +k) yields (t^{−(m−1)/2}s^{1/2})^k, and C_N cancels.
7. Total scalar: t^{k(m−k)} · t^{−k(m−k)/2} · s^{−k/2} · t^{−k(m−1)/2} · s^{k/2} = t^{(k(m−k) − k(m−1))/2} = t^{−k(k−1)/2} = **t^{−C(k,2)}**.
   - k = 1: t^0, so E_1 = 𝒩 e_1 𝒩^{-1}.
   - k = 2: t^{−1}, so E_2 = t^{−1} 𝒩 e_2 𝒩^{-1}.

   This is exactly Thm 6.2, normalisation included, with no free constant. The m- and s-dependence cancels.
   The printed Rem 6.4 now records this composition in one sentence.

**Rem 4.8 = our Rem 6.3.** DFK Rem 4.8 states (Σ^{-1}∇Σ)|_{t→t^{-1}} P_λ = t^{−n(λ)} q^{n(λ')} P_λ. In our variables, this is
𝒩 = Σ^{-1}∇Σ. Since F[εX] = (−1)^d F, we have φ = (−1)^d Σ, so φ^{-1}∇φ = Σ^{-1}∇Σ.

I first suspected a plethystic sign slip in DFK (Rem 4.8 writes H̃ ∝ P[X/(t−1)]|_{t→1/t}, where Macdonald has
J[X/(1−1/t)]). **Computation refuted the suspicion.** `scripts/day237/dfk_rem48_sign.py` checks DFK's literal statement for n = 2, 3:
- DFK literal: TRUE.
- ε-twisted version: TRUE (as it must be, since ε is a degree sign).
- The "sign-fixed" X/(1−t) version: FALSE.

So DFK is correct as written. My slip was forgetting that "|_{t→t^{-1}}" applies to the whole operator. No erratum. Rem 6.3 now
credits DFK Rem 4.8 / Thm 4.7 for this identity.

**Registry numbering (DFK15 = arXiv:1505.01657v2), settled first-hand.** I compiled the v2 e-print locally and ran pdftotext:
- **Corollary 5.8** = graded characters at level k, display **(5.18)**. Its level-one form is (5.25).
- **Corollary 5.18** = χ_n(q^{-1}, z) = lim P_λ^{q,t}(z) = P_λ^{q,0}(z), display **(5.27)**.

They are two different corollaries. The longversion text (line ~780: "Cor. 5.8 in its level-one form (5.25), Cor. 5.18 (eq. (5.27))")
is **correct**. The registry note in thmC-block-law-exact, Day 220 dream PROPOSAL, has the phrase "Cor 5.8 (display (5.18);
journal numbering Cor 5.18)". That phrase is **wrong**: it conflated the display number (5.18) with Cor 5.18. A correction field is
now added. The historical note is left in place and not rewritten.

## (c) Cold read of §6 + App A

- **Definitions before use.**
  - b_μ (Rem 6.5) is defined in §5 (`sec:edge`), before §6. ✓
  - 𝖯_ν and 𝒩 are defined before Thm 6.2. ✓
  - E_λ comes from Cor A.5, a forward reference to the appendix, which is acceptable.
  - Rem 6.3 now refers forward to Rem 6.4's dictionary. That is the adjacent remark, which is acceptable.
- **Twisted vs untwisted are kept apart.**
  - Prop 6.7 conjugates x_i to the *twisted* Y_i (§2).
  - The i = 1 step uses Y_1 = x_1 Y°_1.
  - "γ̂ commutes with T_i" uses the *untwisted* Y° only (f_d(Y°), Lemma A.1, Thm A.2).
  - The "all i" step uses Lemma A.1(a) for π (twisted). Lemma A.1 is stated for any ϖ with ϖT_k = T_{k+1}ϖ.
  - Lemma 6.8 uses π° for (H5) → (R3).
  - Rem A.3 handles the twisted π on Laurent polynomials.

  No leak found.
- **Line checks.**
  - Lemma A.1(b) both relations and the product identity: re-derived. ✓
  - Lemma A.1(c), case j ≤ i−1, braid manipulation: re-derived. ✓
  - Thm A.4, all-swap path coefficient vs rk_i: re-derived. ✓
  - Prop 6.7, the t^r coefficient comparison: ✓.
  - Lemma 6.8: t^{m−1} D^1_m with (q,t) = (s,1/t) has eigenvalue Σ s^{ν_i} t^{i−1}. ✓
  - Rem 6.5: a_{μν} is regular at s = 0, because P_ν(x;0,1/t) is HL and so the transition matrix is unitriangular. The remark's
    "modulo s" is sound, although the remark does not claim it.
- **Printed example after Thm A.4** (m = 3, λ = (2,0,1), Y°_1): recomputed from the printed T_i and π°. The gr part plus the
  extra term −s(t−1)x^{(1,1,1)} is exactly as printed (`scripts/day237/appA_example_check.py`: True).
- **Shorter route?** Rem 6.3 can now *cite* DFK Rem 4.8 rather than present itself as ours, and the text now does so. I found no
  other compression. §6.1–6.3 are already minimal: one commutator plus one Gaussian.
- **Rebuild**: 37 pp. Overfull count from `grep -a -c Overfull longversion.log` = 0. No undefined references or citations.

## (d) The s2b Thm 4.4 / 4.5 controls (Clio's flag)

Script: `rick-research/scripts/day233b/s2d.py` (log `s2d.log`), n ≤ 7, same engine and cost cut as s2b.
- **Thm 4.4 dedupe**:
  - Structurally blind on **58/146** cases, i.e. no two labelled set partitions share a block multiset. These are exactly s2b's "58 ok".
  - It fires on all 88/88 cases where it can differ.
  - Clio's diagnosis was "λ with distinct parts". That is only part of the story: of the 58 blind cases, 17 have λ with distinct
    parts and 41 have a repeated part, but no collision occurs among the set partitions with block sums μ.
- **Thm 4.5 overcount**:
  - Structurally blind on **131/217** cases, where every assignment multiplicity is 1. Mostly these are μ with distinct parts
    (128 of 131), not λ with distinct parts.
  - It fires on all 86/86 cases where it can differ.
- **New controls that can fail everywhere**, replacing the block factor's s-order [(s−1)^{|B|−1}] by [(s−1)^{|B|}]:
  - Thm 4.4: fires on 146/146.
  - Thm 4.5: fires on 213/217. The 4 coincidences are (a,2) → (a+1,1), a = 2..5, all with κ = 1.
- Side finding: 56 of the 217 Thm 4.5 cases have κ = 1. In those cases the identity is a tautology (one block, factor = lhs), so
  the substantive count is 161.
- The paper does not print these controls, so no .tex change is needed. RESULTS/INVENTORY record the stratified rank.

## Gaps

None in (a)–(d).

Residual, not ours to close: DFK's own §6 identification T ↦ τ+, U ↦ τ− for **finite N**. It is their footnote/quotient claim
on top of Schiffmann–Vasserot (N = ∞). Rem 6.4 cites it as theirs and Thm 6.2 does not depend on it.

## Files

- work-in-progress: `longversion/longversion.tex` (Rem 6.3, Rem 6.4, §6 computer checks); `scripts/day237/rem63_bridge_check.{py,log}`,
  `dfk_rem48_sign.py`, `appA_example_check.py`; registry.
- rick-research: `scripts/day233b/s2d.{py,log}`; this file; registry copy.
