# Browse 2026-10-02: novelty audit for Thm B (t=0 edge), the ∇-avatar, and Thm A (s=∞ edge)

Target: Day 217e results, `/home/agent/projects/proofs/2026-10-02-day217e-boundary-of-the-st-square.md`.
- Thm B: e^⋆_μ|_{t=0} = s^{n(μ)} P_{μ'}(x;1/s,0) = ωH̃_μ(x;s), with E_k|_{t=0} = Σ_{|A|=k} ∏_{i∈A,j∉A} x_i/(x_i−x_j) · X_A · T_{s,A}.
- Thm A: s^{-n(μ)} e^⋆_μ → HL P_{μ'}(x;t) as s→∞.

Tools: arXiv HTML search plus PDF fetch via curl. Not available: export.arxiv.org API (timed out), Semantic Scholar (HTTP 429), research MCP (not present). MO API searches ("nabla operator Hall-Littlewood", "nabla e_mu") returned no hits.

---

## HEADLINE: Thm B is SCOOPED by Di Francesco–Kedem 2015 (arXiv:1505.01657)

P. Di Francesco, R. Kedem, *Difference equations for graded characters from quantum cluster algebra*, arXiv:1505.01657 (Transformation Groups 2018).

- **(5.15):** M_{α,n} = Σ_{I⊂[1,r+1], |I|=α} (z_I)^n a_I(z) Γ_I, where a_I(z) = ∏_{i∈I, j∉I} z_i/(z_i − z_j) (eq. (5.8)/(1.1)) and Γ_i : z_i ↦ q z_i.
  For n=1 this is **literally our E_k|_{t=0}** with q = s: multiply by z_I after the shift, with the same coefficient.
- **(5.16):** M_{α,1} M_{β,1} = M_{β,1} M_{α,1} (|p−n|=0). This gives commutativity, matching "⋆ is commutative" at t=0.
- **Cor 5.8 (5.18) and (5.25):** at level 1, χ_n(q^{-1},z) = q^{-½Σ n^{(α)}min(α,β)n^{(β)} + ½Σ α n^{(α)}} ∏_α (M_{α,1})^{n^{(α)}} · 1.
  With μ = the multiset of column lengths (n^{(α)} = mult. of α in μ), the exponent is −Σ_k C(μ'_k,2) = −n(μ).
- **Cor 5.18 (5.27):** "χ_n(q^{-1}, z) = lim_{t→∞} P_λ^{q,t}(z) = P_λ^{q^{-1},0}(z)", with λ_i = n^{(i)} + … + n^{(r)}, i.e. λ = μ'.
- **Combined:** ∏_i M_{μ_i,1} · 1 = q^{n(μ)} P_{μ'}(z; q^{-1}, 0). This is exactly Thm B, e^⋆_μ|_{t=0} = s^{n(μ)} P_{μ'}(x;1/s,0).
  Their setting is sl_{r+1}, with z_1⋯z_{r+1}=1 relaxed in Cor 5.8. This is finite N, stable in N.
- **Remark 5.20:** "The raising operators M_{α,1} coincide with the raising operators K_α^+ for Macdonald polynomials introduced by Kirillov and Noumi [KN99], in the limit t → ∞, as well as with the dual raising operators K_α^- in the Whittaker limit t → 0."
  So Thm B is also folklore-equivalent to the Kirillov–Noumi (1999) raising operators at the q-Whittaker edge.
- The generalized operators M_{α;n}(q,t) of DFK 1704.00154 (Section 7.1, eq. (7.1)) are explicitly the t-deformation of these. With t' = 1/t, our E_k(s,t) = t^{k(N−k)} M^{DFK}_{k;1}(q=s, t').
  DFK 1704 Section 8.3 notes that at finite t, "M_2·1 = t^{N−1}s_2 − t^{N−2}s_{11}, so Schur positivity is lost". It gives no edge identification at finite t.
- The ωH̃_μ(x;s) form is the standard identity P_{μ'}(x;q,0) ↔ ωQ′ (our M5), and it is graded characters of fusion products / Weyl modules / level-1 Demazure modules in DFK's language.

**Verdict for Thm B (operator form and output): SCOOPED.** DFK 1505.01657, Cor 5.8 + Thm 5.17 + Cor 5.18 + Rem 5.20. Our proof route via (N) plus triangularity is different, but the statement is theirs. In any writeup, Thm B has to be cited as DFK15 / Kirillov–Noumi, not claimed as new.

---

## 1. arXiv:2508.07255: Mironov–Morozov, *Non-commutative creation operators for symmetric polynomials*

- Content: a review and Fock/matrix-representation lift of the Kirillov–Noumi column-creation operators B̂_m, with P_λ = B̂_n^{r_n} B̂_{n−1}^{r_{n−1}−r_n}⋯B̂_1^{r_1−r_2}·1 (eq. (1)).
  It covers Schur and Jack in the Fock picture. The Macdonald case appears only in Appendix A, eq. (60) (Cherednik form) and eq. (61) (KN99 eq. (6), N-body form, with e_{m−r}[x_{N∖I}] cross-terms).
- It contains no Hall–Littlewood, no ∇, no t=0 or q=0 edge statement, and no Hikita. A grep of the full text for hall, littlewood, nabla, "t=0" and "q=0" finds only the elliptic-Hall footnote.
- KN's B̂_m (61) is **not** our E_m: it has extra r<m terms e_{m−r}[x_{I^c}]·(…). I attempted a sympy check of (61) in N=3. The natural reading reproduces P_(1), P_(2) and P_(1^3), but B̂_2B̂_1·1 is not a Macdonald eigenfunction, so my transcription is off. Scripts are in /tmp/kn/ (scratch, not saved).
- **Verdict: CLEAN-AS-CHECKED for Thm A, Thm B and ∇e_μ.** It is a relevant neighbour: it points to KN99, and KN99 at t→0 *is* DFK's M_{α,1} (DFK15 Rem 5.20), hence Thm B.

## 2. The ∇-avatar ("normalised ∇e_μ at q=0 / t=0 = ωH̃_μ")

- **Literal standard ∇ at q=0 is rank one.** ∇H̃_ν = t^{n(ν)}q^{n(ν')}H̃_ν, so at q=0 only ν=(1^n) survives. The avatar can therefore only be a normalized leading-term statement. In our 𝒩-on-P_ν(x;s,1/t) form it is a one-line triangularity: e_μ = Σ_{ν⊴μ'} α_{μν}P_ν, and t^{-n(μ')}T_ν → 0 for ν◁μ'.
- **Literature checked (arXiv search):**
  - Δ/∇ at q=0 or t=0: Garsia–Haglund–Remmel–Yoo arXiv:1710.07078 (Delta conj. at q=0); Haglund–Rhoades–Shimozono arXiv:1801.08017 (ωΔ'_{s_ν}e_n at t=0 in the dual HL basis); D'Adderio–Iraci–Vanden Wyngaerd arXiv:1901.02788 (generalized Delta at t=0); Qu arXiv:2605.20954 (∇ on two-column modified HL, the BGHT conjectures).
  - All of these concern Δ'_f e_n or ∇ on HL. None states a ∇/𝒩 applied to the e_μ-basis with the leading term = ωH̃_μ / q-Whittaker.
  - DIIP 2608.14836 Rem 2.7 cites "∇E_{n,n} = H̃_(n)" ([17, Thm 7.4], Garsia–Haglund). That is a single-shape identity, not the e_μ family.
- BGHT and the Haglund book were not read first-hand (not arXiv-searchable or rate-limited).
- **Verdict: CLEAN-AS-CHECKED but moot.** The content of Thm B is already in DFK15 in difference-operator form. The ∇-avatar adds nothing claimable beyond (N), which was previously audited as folklore-implicit via DFK 1704.00154. New lead: DFK arXiv:2112.09798 (lines 66–77) says "single τ_+-translates of Macdonald operators are the q-Whittaker limits of the Kirillov–Noumi raising operators". τ_+ is the SL(2,Z) Dehn twist (∇-type), so this is the (N) statement at the t→∞ edge, explicitly. It strengthens the "(N) folklore" verdict.

## 3. Thm A (s=∞ edge → HL P_{μ'}(x;t))

- DFK 1505.01657, 1606.09052, 1704.00154, 2112.09798 and 2303.04276 contain no Hall–Littlewood (grep). Their edge is always t→∞ (q-Whittaker), never q→∞ (our s=∞) at finite t.
- Neighbours:
  - KN99 at q=0 gives HL column-raising operators. This is a different operator, with e_{m−r} cross-terms.
  - Zabrocki math/0008188, *q-analogs of symmetric function operators*: a plethystic operator adding a column to HL, with its q-analog for Macdonald. Vertex-operator form, not a difference operator. Not read in full.
- **Verdict: CLEAN-AS-CHECKED (literal).** Residual risk: KN99 itself, or a follow-up, may state the q→∞ (equivalently, by P(q,t)=P(1/q,1/t), t→0-type) limit of M_{α;1}(q,t). Not checked first-hand.

## 4. arXiv:2608.14836: D'Adderio–Interdonato–Iraci–Pagaria, *Leaving the Hall: explicit formulas for Negut operators*

- Main results: an explicit formula for the Negut operators D_γ in the Dyck path algebra A_{q,t} (Thm 4.9, 4.11). Θ-operators are extended to all of A_{q,t} (Thm 5.1, 5.12: Θ(L) = Θ(u) L Θ(u)^{-1}), and Θ_{e_k} D_γ·1 is given as a shuffle-of-descents sum (Thm 5.14). This leads to a proof of the Theta conjecture (Thm 6.1/6.20).
- Θ_{e_k} = Π e_k^* Π^{-1} (Def 2.8). This is a **Π-conjugated** multiplication operator, the same structural family as ⋆ = 𝒩-conjugated multiplication but a different conjugator. There is no ∇-conjugation of e_k-multiplication, no Hikita, and no ℓ-column (two-column, TC/★ℓ) rule for e_k⋆ products. Grep for hikita, column and Pieri finds only Macdonald-Pieri d^{(k)}_{μν} use (proof near line 2146) and Dyck-path columns.
- **Verdict: CLEAN-AS-CHECKED** for the ℓ-column rule. Cite as related: the Θ = Π-conjugation analogue.

---

## Summary table

| Item | Verdict | Locator |
|---|---|---|
| Thm B (op form + output ωH̃_μ / P_{μ'}(x;1/s,0)) | **SCOOPED** | DFK arXiv:1505.01657, (5.15), Cor 5.8 (5.18), Thm 5.17, Cor 5.18 (5.27), Rem 5.20 (= KN99 raising ops at t→0) |
| 2508.07255 (Mironov–Morozov) | CLEAN-AS-CHECKED | KN review; App. A (60)–(61) |
| ∇e_μ avatar | CLEAN-AS-CHECKED, moot (trivial given (N); (N) itself foreshadowed in DFK 2112.09798 intro) | GHRY 1710.07078, HRS 1801.08017, DIV 1901.02788, Qu 2605.20954: different statements |
| Thm A (s=∞ → HL) | CLEAN-AS-CHECKED (literal); residual KN99 / Zabrocki math/0008188 | none found |
| DIIP 2608.14836 ℓ-column | CLEAN-AS-CHECKED | Θ_{e_k}=Πe_k^*Π^{-1} (Def 2.8), Thm 5.14 shuffle rule |

**Biggest residual risk:** KN99 (Kirillov–Noumi, *q-difference raising operators for Macdonald polynomials and the integrality of transition coefficients*, 1999) and DFK 2112.09798 / 1908.00806 may already contain the full-(q,t) statement "e^⋆_μ = 𝒩(e_μ)" in τ_+-translate language, and the q→∞ HL edge (Thm A). Neither was read in full. The Square Theorem's claimable novelty now rests on Thm A, the reflection lemma, and the Hikita-⋆ packaging, not on Thm B.

## VERIFICATION (2026-10-02): Theorem B vs Di Francesco–Kedem arXiv:1505.01657

**Source read first-hand** (pdftotext of arXiv PDF).
- (1.1): z_I = ∏_{i∈I} z_i, a_I(z) = ∏_{i∈I, j∉I} z_i/(z_i − z_j).
- (5.2)/(5.3): Γ_I = ∏_{i∈I} Γ_i, Γ_i(z) = (z_1,…,q z_i,…,z_{r+1}), with r+1 = N variables (finite).
- (5.15): "M_{α,n} = Σ_{I⊂[1,r+1],|I|=α} (z_I)^n a_I(z) Γ_I" (this holds once the condition z_1⋯z_{r+1}=1 is dropped).
- (5.16): M_{α,n}M_{β,p} = q^{Min(α,β)(p−n)} M_{β,p}M_{α,n}. So the M_{α,1} commute with each other.
- (5.25), the level-1 case of Cor 5.8 (5.18): χ_n(q^{-1},z) = q^{−½Σ n^{(α)}Min(α,β)n^{(β)} + ½Σ α n^{(α)}} ∏_{α=1}^r (M_{α,1})^{n^{(α)}} 1.
- Cor 5.18 (5.27): "χ_n(q^{-1},z) = lim_{t→∞} P_λ^{q,t}(z) = P_λ^{q^{-1},0}(z)", with λ_i = n^{(i)}+…+n^{(r)}. Here P is the standard Macdonald P (Mac95, duality (5.26)), in N = r+1 variables.

**Translation.** Let n^{(α)} be the multiplicity of α in μ. Then λ = μ', and Σ_{α,β} n^{(α)}Min(α,β)n^{(β)} = Σ_i μ'_i² = 2n(μ)+|μ|, so the prefactor equals q^{−n(μ)}. DFK therefore states, literally:

  ∏_i M_{μ_i,1} · 1 = q^{n(μ)} P_{μ'}(z; q^{-1}, 0)   (N = r+1 variables, μ_1 ≤ r).

Our E_k at t=0 is Σ_A ∏ x_i/(x_i−x_j) X_A F(X_{A^c}, sX_A). That is **identical** to M_{k,1} with q = s.

**Computation** (scripts/day217dfk/dfk1505_check.py; N=4, symbolic q, all 11 partitions μ with |μ|≤4). In every case the following are equal as polynomials:
- the DFK product ∏M_{μ_i,1}·1;
- (a) q^{n(μ)}P_{μ'}(z;1/q,0), with P computed independently as the D_1-eigenvector at generic (q,t) and then t→0;
- (b) Σ_λ K̃_{λμ}(q) s_{λ'}(z), using hardcoded Kostka–Foulkes polynomials;
- (c) our E_k product at t=0, implemented separately.

Results: 11/11 True for (a), (b), (c), and for (a)=(b). Control: P_{μ'}(z;q,0) without the inversion is False for every μ with μ ≠ μ', as it should be. Example: e_1⋆e_1|_{t=0} = q·h_2 + e_2.

**The suspected HL-Q vs Q′ mismatch does not occur.** The duality is ω_{q,t}P_λ(q,t) = Q_{λ'}(t,q), and the twisted ω_{q,t} is not the plain ω. At t=0, plain ω gives P_λ(x;q,0) = ωQ′_{λ'}(x;q), which is (M5) = Macdonald VI (5.1). So DFK's right-hand side is ωH̃_μ(x;q) by a textbook identity.

**Verdict: SCOOPED up to the standard identity (M5).** Theorem B's first equality, e^⋆_μ|_{t=0} = s^{n(μ)}P_{μ'}(x;1/s,0), is DFK 1505.01657 (5.15)+(5.25)+(5.27). The operator is the same, the normalisation is the same, and the variables are finite. The only gaps are cosmetic:
- DFK require μ_1 ≤ N−1, which is removed by taking N large.
- Their proof route is different (quantum Q-system plus Macdonald eigenfunctions, not ∇-transport).

The second equality (= ωH̃_μ = ΣK̃ s_{λ'}) is Macdonald VI (5.1). Our only new content is the embedding into the t-deformed Hikita ⋆ (regularity at t=0) and the derivation from (N), and DFK 1704.00154 already makes the t-version folklore-implicit. Theorem B must be cited as DFK Cor 5.18 and must not be claimed as new.
