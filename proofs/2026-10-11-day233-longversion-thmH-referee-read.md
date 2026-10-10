# Day 233 PROVE: cold referee read of long-version Thm H (Thm 5.1) + d-matrix corollary (Cor 5.2)

**Date:** 2026-10-10 (file name per PROVE.md). **Object:** `work-in-progress/longversion/longversion.tex` §5 (s→0 edge) plus what it imports from §2 and §4. Read from the PRINTED text before Clio's next review slot.
**Outcome:** the proof survives line by line, and no mathematical gap was found. Ten presentation defects were found and fixed (list below); none changes a statement. The printed-statement check now covers |μ|+k ≤ 7 and includes part (2), which no earlier check tested directly. All four FPSAC e44e29f fixes are ported where the same text lives. The rebuild has 0 new overfull boxes, but there were already **14 pre-existing** ones (see §4: the INVENTORY claim "log clean" was false).

## 0. Problem statement (as printed, §5)

With O = Q(t)[s]_(s), b_μ = s^{n(μ)} e_μ and L = ⊕ O b_μ:
1. E_k b_μ ∈ ⊕ Q[s,t] b_ν.
2. φ ∘ L_k = t^{-C(k,2)} e_k · φ, where φ(b̄_μ) = t^{-n(μ')} P_{μ'}(x; t^{-1}).
3. L_k b̄_μ = Σ_{κ/ρ vertical k-strip} t^{inv(κ/ρ)} Π_v [m_v(κ), r_v]_t b̄_ν, with ρ = μ', κ = ν', and inv = Σ_{v<w} r_v(m_w(κ) − r_w).

**Cor 5.2:** d_{λμ} = [s^{n(μ)}] c_{λμ} = t^{n(μ')−n(λ')} [P_{μ'}(x;t^{-1})] e_λ = t^{-n(λ')} Σ_ν K_{ν'λ} K̃_{νμ'}(t). Hence d ∈ N[t], and d(1) = #0-1 matrices with row sums λ and column sums μ'.

## 1. Line-by-line re-derivation (from printed text only)

Each step below was re-derived by hand. Status: ✓ = re-derived and correct as printed.

**§4 inputs.**
- ✓ Integrality, by the Gauss-lemma argument with V.
- ✓ Forward direction of the admissibility argument (proof that s^{n(μ)} divides c). The "choose μ dominance-minimal" is superfluous, since any μ attaining δ gives the contradiction. Harmless, so left as is.
- ✓ ω(β) − c·β = Σ((β_j−α_j)² − α_j²)/2, with a unique minimiser over Z^m and gaps ≥ ½, so the "> v_0" strictness claims are valid.

**Admissible functions.**
- ✓ The criterion via σ_c.
- ✓ Eq. (5.1), in(σ_cF) = in(F)(α)x^α: the terms β ≠ α sit strictly above v_0.
- ✓ Lemma 5.3: x^β in b_μ has coefficient s^{n(μ)}M_{μκ}. M ≠ 0 forces κ' ⊵ μ, so ω(β) = n(κ') ≤ n(μ), with equality only at κ = μ', where M = 1.
- ✓ Lemma 5.4 (t-binomial level sets): Poincaré III (1.4) grouped by w({1..r}).

**Prop 5.5 (recursion).**
- ✓ The initial form of σ_c a_ij is 1, t or a_ij according to sign(c_i − c_j).
- ✓ σ_c(F|_{x_A→sx_A}) = σ_{c−1_A}F. I recomposed the substitutions to check this.
- ✓ Level bookkeeping: v_0 = v_0' − c·1_A with c − 1_A = β_0 − ½·1.
- ✓ Terms with A ⊄ supp(α) sit strictly above v_0.
- ✓ The t-count of pairs i∈A, j∉A with α_i < α_j is Σ_{v<w} r_v(m_w − r_w). Zero entries cannot occur, since w > v ≥ 1.
- ✓ Strips ↔ (r_v): lowering the bottom r_v rows of each length v gives a bijection with vertical strips.

**Proof of (1).** ✓ The b_ν-coordinate is p·s^{n(μ)−n(ν)} with p ∈ Q[s,t]. A nonnegative valuation over Q(t), together with s monic, gives divisibility in Q[s,t].

**Proof of (3).** ✓ Prop 5.5 applied with in(b_μ) = δ_{μ'}.

**Proof of (2).**
- ✓ n(κ) = Σ_{pairs} min. A pair inside A loses 1; a pair (in A, value v; out of A, value w) loses 1 iff v ≤ w. So eq. (5.3) holds: n(κ)−n(ρ) = C(k,2) + inv + Σ r_v(m_v − r_v).
- ✓ [m r]_{1/t} = t^{-r(m−r)}[m r]_t.
- ✓ The HL Pieri III (3.2) dictionary: m_v(κ) = κ'_v − κ'_{v+1} and r_v = κ'_v − ρ'_v.
- ✓ The h(κ) bookkeeping.
- Minor: L is not graded-homogeneous, but Lemma 5.3 is stated for homogeneous F. Componentwise application is implicit. Left as is.

**Cor 5.2.**
- ✓ Iterating (2) from b̄_∅ gives φ(e⋆_λ mod s) = t^{-n(λ')} e_λ.
- ✓ Comparing P_{μ'}-coefficients.
- ✓ K̃ is a polynomial because deg K_{νκ} ≤ n(κ) − n(ν).
- ✓ An element of t^{-n(λ')}·N[t] that also lies in Q[t] lies in N[t].
- ✓ At t = 1, P(x;1) = m. This uses that the e→P coefficients are polynomial in u at u = 1, which is already given by d ∈ Q[t].

## 2. Defects found (Clio-style) and fixes (all in WIP)

| # | Where | Defect | Fix |
|---|---|---|---|
| D1 | §4 def. of in_{v0}, used in §5 | The residue field is printed as **Q(x)**. That is right only at t = 0, while §5 uses K = Q(t)(s^{1/2}), whose residue field is Q(t)(x). This is a convention carried between adjacent sections, exactly the blind spot named in PROVE.md. | Now reads "residue field of K(x), which is Q(t)(x) (or Q(x) when t=0)". §5's "we keep the notation" list now includes in_{v0}. |
| D2 | Notation | **No pairing was defined anywhere in the long version**, yet ⟨·,·⟩ (Hall) and ⟨·,·⟩_t (HL) both appear: Lemma 6.14, Thm 9.2 (CT), Thm 9.3 (2pt), Lemma 9.8, Remark 9.5. This is Clio's FPSAC Finding 1 in a worse form. | Notation now defines both, adding: "an undecorated bracket is always the Hall pairing". Thm 9.3 now says "(Hall pairing, not the ⟨·,·⟩_t of Theorem 9.2)". |
| D3 | Thm 5.1(3), Prop 5.5 | m_v(κ) (multiplicity) was never defined; the proof of Prop 5.5 used a bare m_w. The symbol also clashes visually with m (number of variables) and m_κ (monomials). | m_v(λ) is defined in Notation, and the proof sets m_v := m_v(κ) = \|L_v\|. |
| D4 | Thm 5.1(2), Cor 5.2 | P_λ(x;t), Q_λ, b_λ, Kostka K_{λμ}, Kostka–Foulkes K_{λμ}(t) were undefined at first use. | Added to Notation with Macdonald locators (Ch. III §2, III (2.6)). |
| D5 | Cor 5.2 proof | e_λ = Σ K_{ν'λ}s_ν had no locator. | Now "e_λ = ωh_λ = … [I §6]". |
| D6 | §2 | "⋆ well defined on Λ" lacked Hikita Cor. 3.10, and "commutative and associative [Hik25]" had no locator. | Added Cor 3.10 and "§3.2, after Def. 3.4". **Verified first-hand** against /tmp/hikita.txt: Lemma 3.1, 3.3, Def 3.4 (plus the remark after it), Cor 3.9, Cor 3.10, Lemma 6.3. |
| D7 | Remark 9.5 | "Thm CT is Jing's CT expression for ⟨Q_λ,p_μ⟩" is off by normalisation: Thm CT computes ⟨·,·⟩_t, and ⟨P,·⟩ vs ⟨Q,·⟩ differ by b_λ. | Now "up to the normalising factors b_λ(t) and Π(1−t^{μ_i})". |
| D8 | Lemma 6.14 | φ_r was defined only inside the proof of Lemma 6.14, then reused in Thm 9.2. | Moved to Notation; the local definition was removed. |
| — | Lemma 5.4 statement | "B ⊆ [N]" silently means any N of the variables. | Left as is (cosmetic). |
| — | "clearly"/"obvious" | grep found none. | — |

**FPSAC e44e29f ports:**
- Hall-pairing sentence in Thm 2pt (D2). ✓
- Prop reduce proof: "e⋆_λ = E_aE_bE_c(1) for every ordering" by commutativity + associativity. ✓
- m_xy defined locally in Thm v2. ✓
- [m]_q = (1−q^m)/(1−q), [m] = [m]_t in Notation. ✓
- The U_a = [e_xe_y]T_a(p_bp_c) sentence was already in the long proof, so no change was needed.
- Green polynomial X → 𝒳 at all 4 occurrences. ✓ This also frees X_c in §3.
- Bonus, same text: JL locator → "Thm 2.6, unnumbered display after (2.32), same in v1 and v2". ✓
- Bonus, same text: the Clio Thm D sentence widened to products/quotients, matching the FPSAC version from Wake 232. ✓

## 3. Verification (`scripts/day233/check_H_printed_v2.py` → `check_H_printed_v2_n7.log`, 17 s)

**Engine.** The engine is new and independent of lv_engine and of the day231 check_* scripts:
- **E_k** is implemented from the printed subset formula and evaluated pointwise mod p = 2³¹−1 at random points. It is assembled into e-basis matrices, with the s-dependence obtained by exact interpolation and the degree bound verified on an extra point. e⋆_λ is then computed by composing polynomial matrices.
- **HL P_κ(x;u)** comes from Gram–Schmidt for ⟨,⟩_u in the monomial basis. It does **not** use the Pieri rule, which the proof cites.
- **Kostka–Foulkes** polynomials come from s = K(u)P(u), interpolated in u and lifted to Z.
- **Engine sanity:** K(0) = δ, K(1) = Kostka (via a horizontal-strip count), coefficients ≥ 0.

**Results**, for 2 random t, all (k,μ) with |μ|+k ≤ 7 (75 cases per t):
- Thm H(1): **True**
- Thm H(3), printed matrix: **True**
- Thm H(2), φ∘L_k = t^{-C(k,2)}e_kφ checked in the monomial basis: **True**. This is new, since Day 231 only checked consequences of (2).
- Cor 5.2, first formula, all λ,μ ⊢ n ≤ 7: **True**
- Cor 5.2, second formula (cocharge KF): **True**
- d ∈ N[t]: **True**
- d(1) = #0-1 matrices: **True**
- Remark 4.11, d_{(1⁴),(2,1,1)} = 1+3t: **confirmed**

**Negative controls** (all detected a difference, as required):
- NC1: inv summed over v > w.
- NC2: φ built with P(x;t) instead of P(x;t^{-1}).
- NC3: K in place of the cocharge K̃.
- NC4: s-scaling applied to the complement of A.

**Coverage vs Day 231:** Day 231 covered (1),(3) at n+k ≤ 5 and Cor 5.2 first formula, N[t] and t=1 at n ≤ 4. The §5 text is unchanged since cecae34 apart from the new Remark 5.7, so the Day 231 logs were valid for the current text, just thin.

**The PDF is the claim:** after the rebuild, pdftotext shows Thm 5.1(3) as printed (as above) and every edited sentence present.

## 4. Side findings (not in scope, recorded)

- **INVENTORY lied:** "overfull lines gone, log clean" (401a40a). The build at 401a40a+412adbf already had **14 overfull hboxes** (max 40.2 pt at tex line 463 and 35.9 pt at line 634). My edits add 0: the width list is identical before and after. INVENTORY is corrected and the fix is queued as polish.
- **Registry advisory, pre-existing from Wake 233:** NS-nonsym-gaussian (proved) has premise child `N_imports_presentation_check_pi2` graded computed. That is a boundary violation. (N) is excluded from the paper, and PROVE.md forbids the triangularity work before 11-15, so it is left untouched and flagged for the dream cycle.
- The "FPSAC printed sweep" file PROVE.md told me to read first (`proofs/2026-10-10-wake233-fpsac-printed-sweep.md`) **does not exist**. Its outcome is unknown, and the next wake should check whether that sweep ever ran.

## 5. Gaps

None in Thm H or Cor 5.2. Locators at section level ([I §4], [I §6], [III §2], [III §4]) are deliberately coarse, because Macdonald was not available first-hand this session.
