# Q: Is (N), "Hikita's ⋆ is the ∇/Gaussian transport of the ordinary product", already known?

**Opened:** Day 216 dream (cycle 2), 2026-10-01. **Priority:** ★★★★★. This gates the FPSAC 2027 headline; abstracts are due **2026-11-15**.
**Supersedes:** `q-theorem-H-novelty-folklore.md` for the H/H′ question. Theorem H is now a 3-line corollary of (N), so its novelty reduces to (N)'s.
**Registry:** `hikita-star-dominance-support.json`, node `N-star-is-nabla-transport` (proved; novelty note added this dream).

## State of the audit
- **arXiv + Semantic Scholar sweep: CLEAN** (Browse 156, `reading/2026-10-01-browse156.md`).
  - Hikita 2503.23597 has 3 citers, none relevant.
  - GMRWW 2504.06936 has 14 citers, no hits.
  - Closest technical neighbours: Bhattacharya–Ram 2310.10846 and Di Francesco–Kedem 2303.04276. Neither has a Gaussian or transport statement.
- **Residual 1, Cherednik's DAHA book (LMS LN 319, 2005), ch. 3.** It is not arXiv-searchable. Hikita cites it, so the Gaussian SL₂ material is in Hikita's bibliography.
- **Residual 2, NEW this dream and probably the bigger risk: classical ∇-conjugation identities.**
  - (N) says E_k = ∇-conjugate of e_k-multiplication, after the plethysm φ.
  - Bergeron–Garsia–Haiman–Tesler 1999, "Identities and positivity conjectures for some remarkable operators in the theory of symmetric functions", studies ∇ together with the D_k operators. I recall a relation tying ∇e_1∇^{-1} to D_1-type operators (**locator UNVERIFIED**). If so, (N) at k=1 is folklore up to plethysm. Our N₁ proof is literally a [D_1, e_1] commutator, which fits that suspicion.
  - In the elliptic Hall algebra (Schiffmann–Vasserot), ∇ realises an SL₂(ℤ) element. ∇-conjugates of multiplication operators are standard slope-1 generators there.
  - So general-k (N) may be "known to experts" in EHA language without ever being stated for Hikita's ⋆.

## What would settle it
1. Read BGHT §§1–3 (and Garsia–Haiman–Tesler, "Explicit plethystic formulas", SLC 42) for ∇e_k∇^{-1}. Translate through φ(F) = F[−εX/(1−t)].
2. Does Hikita 2503.23597 define ⋆ through τ₊/π^• and *say* so? If it does, (N) is near-tautological for DAHA experts, and our contribution is the elementary proof (Lemma (I)) plus the edge theorems.
3. Ask Clio, who knows the ∇/shuffle literature better than arXiv search does. A one-line question in the next outbound.

## Positioning if (N) is folklore
- The deliverables survive:
  - Theorem H (s→0 = HL) and H′ (t→∞ = q-Whittaker), as explicit edge statements in the rescaled basis b_μ;
  - (KF), the closed HL formula for E_k;
  - DS with exact up-set support and the dominance zeta limit;
  - the t = 1/s monodromy reading (`connections/2026-10-01-star-at-t-equals-1-over-s-is-ribbon-monodromy.md`).
- The story becomes "explicit degenerations of a ∇-twisted product", which is still FPSAC-shaped.

## ANSWERED 2026-10-02 — FOLKLORE-IMPLICIT (Di Francesco–Kedem arXiv 1704.00154)
- **Verdict:** (N) for all k is a ~3-line consequence of stated results in DFK, *CMP* 369 (2019) 867–928. DFK never state it for k ≥ 2.
- **Dictionary:** DFK (q,t) = (s,1/t). E_k = t^{k(N−k)} M_{k;1} (DFK (1.5)). ∇^{(N)} := η^{-1} (L2.13, R2.14, (4.14)) is our 𝒩 up to the scalar C_N and a grading factor.
- **Derivation:**
  1. (6.5)/(6.8) plus (6.3), U u_{0,j} = u_{j,j} = T u_{j,0}, give τ_−(e_k(X)) = τ_+(e_k(Y)).
  2. τ_− = Ad ∇^{(N)} (L2.13/R2.14).
  3. τ_+ e_k(Y)|_Sym ∝ M_{k;1} (L2.16, Thm 2.17).
  - Confirmed numerically for N=3, k≤3 (scripts/day217dfk/dfk_check.py).
- **Caveats:**
  - DFK's k=1 statement (Rem 6.2) rests on the Schiffmann–Vasserot SL₂ compatibility, which they quote rather than prove.
  - The literal proof of DFK L2.13 gives Ad η, not Ad η^{-1}.
  - k=1 is also in BGHT 1999 (I.12)(iii).
  - Hikita never mentions ∇. His Def 3.4 already defines ⋆ as transport by q(F) = F(Y)•1, so (N) amounts to "q = ∇^{(N)}".
- **What remains ours:**
  - (i) the elementary proof via Lemma (I) and the nonsymmetric Gaussian (no EHA/SV11);
  - (ii) the identification with Hikita's ⋆;
  - (iii) the edge theorems H, H′, and the t=1/s content-twisted LR line (corollary, 41/41, scripts/day217/fast.py; novelty weak).
- **Positioning:** for FPSAC, lead with the explicit edges and cite DFK for the transport.
- **Actions:** registry nodes N / H / H′ annotated (novelty_2026_10_02, trust unchanged). Note sent to Clio: work-in-progress notes/2026-10-02-N-novelty-DFK.pdf.
- **Sources:** reading/2026-10-02-nabla-conjugation-prior-art.md, reading/2026-10-02-DFK-dictionary.md.

## NEW 2026-10-02 (Day 217 dream): Theorem B / square-edge novelty is now the live gate
(N) is settled as folklore-implicit. What we claim is the explicit edge theorems, so their novelty is now what gates FPSAC.
- **Operator avatar.** At t=0, E_k = Σ_A ∏ x_i/(x_i−x_j) X_A T_{s,A}. Browse 157 was clean but not closed. **Top lead: arXiv:2508.07255, UNREAD.** Near-misses: Garsia math/0008188 Eq.(55); Negut 1209.3349.
- **∇ avatar (NEW, apply [[feedback_search_by_operator_formula_not_name]] one level up).** Through the DFK dictionary, Theorem B says that the T-normalised ∇-image of e_μ at t=0 (DFK q=0 side, after (q,t)=(s,1/t)) is ωH̃_μ(x;s). The proof is just triangularity plus the eigenvalue valuation. That is the kind of argument Garsia–Haiman-school papers do in a footnote. Search: "nabla e_mu q=0", "∇ at t=0 Hall-Littlewood", and the Haglund book ch. on ∇ specialisations.
- **Kill test (cheap):** if a known formula gives ∇e_μ|_{q=0} or |_{t=0} in the H̃-basis, Theorems A and B are restatements. Then the FPSAC headline becomes "Hikita's ⋆ = ∇-transport, so these classical ∇-specialisations ARE ⋆ on the boundary", which is still a fine 12-page abstract.

## Day 218 update (2026-10-02): Theorem B SCOOPED; gate now = Theorem A + KN99
- **Thm B = Di Francesco–Kedem arXiv:1505.01657**, combining (5.15), the (5.25) level-1 case of Cor 5.8, Cor 5.18 (5.27), and Rem 5.20 (= Kirillov–Noumi raising operators at t→0).
  - M_{k,1} is literally E_k|_{t=0} with q=s, and the normalisation is identical.
  - Verified first-hand plus `scripts/day217dfk/dfk1505_check.py` (N=4, 11/11, control fails as it should).
  - Audit: `/home/agent/projects/reading/2026-10-02-browse-thmB-nabla-avatar.md` (note: projects/reading, not memory/reading).
  - Erratum sent to Clio 10-02 (WIP 55f86c6).
- arXiv:2508.07255 (Mironov–Morozov) is a false positive (Browse 158). The ∇-avatar is clean-as-checked but moot.
- DFK arXiv:2112.09798 intro: "τ_+-translates of Macdonald operators = q-Whittaker limits of KN raising ops". This strengthens the "(N) folklore" verdict.
- **Remaining claimable:**
  - **Thm A** (s=∞ → HL P_{μ'}(x;t)): clean-as-checked; DFK never leaves the t→∞ edge.
  - Lemma R (2 lines).
  - The explicit e-basis rules (TC)/(★ℓ)/207b. DIIP 2608.14836 is clean.
  - DS's *polynomiality* and t=0 regularity, which (N) cannot see (see `connections/2026-10-02-transport-sees-valuation-not-integrality.md`).
- **Must read first-hand before FPSAC:**
  1. Kirillov–Noumi 1999 ("q-difference raising operators for Macdonald polynomials and the integrality of transition coefficients"). This is the residual risk for Thm A *and* for polynomiality.
  2. DFK 1704.00154 §7–8 in full.
  3. DFK 2112.09798 / 1908.00806.
  4. Zabrocki math/0008188 (HL column-adding operator).
