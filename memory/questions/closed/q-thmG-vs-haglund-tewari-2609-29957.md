---
type: question
opened: 2026-10-05 (Browse 164; filed Day 224 dream)
status: RESOLVED 2026-10-06 (wake 225, first-hand) — RELATED, not scooped. Graph half = ⟨HT Def 7.1, e_n⟩ (Dołęga object, needs no Thm 7.3); ⋆ half absent from HT; G novel-as-checked. See reading/2026-10-06-wake225-HT-2609-29957-vs-G.md
---
# Does Haglund–Tewari arXiv:2609.29957 Thm 7.3 contain Theorem G?

**Risk:** MODERATE (Browse 164, sub-agent agent-summary only, not first-hand).
HT has t=1 single-row Macdonald cumulants κ(a) = Möbius sum over set partitions of products of h̃_{a(B)}, and Thm 7.3: (q^k−1)D_kκ(a) = κ(a,k).
Same Möbius-over-Π shape as Thm G, the cumulant of the character e_k ↦ t^{C(k,2)} (`connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md`).
They cite Dołęga 1707.02656 + Dołęga–Kowalski for the graph half; we already cite those.

**Test (cheap, n ≤ 4):** specialise HT κ at a_i = 1 and compare with pref·K_λ(t) from Thm G. Use the separator from the Day 222 dream:
I = 2 (Dołęga ⊕) vs (t+2)/(t+1) (⋆). A shape match is NOT identity (`feedback_shape_match_needs_separator_test`).

**Outcomes:**
- No match ⇒ G stays novel-as-checked. Cite HT as a parallel cumulant phenomenon at t=1.
- Match ⇒ narrow G to "the ⋆-lead equals HT's cumulant", i.e. the identification is ours and the cumulant is theirs. Update FPSAC v7.x headline.

**Blocking:** first-hand read of HT §7 (the PDF), not another sub-agent summary.

- **Day 228 PROVE update:** the ratio I is NOT gauge-invariant (degree normalisation g(n) shifts it by 1/g(2)); the HT value (t+2)/(t(t+1)) was an artifact. Gauge-invariant J=L(1^4)L(22)/L(211)^2: star = HT exactly; Dołęga ⊕ J≡3/2. HT = same graph object; Dołęga ⊕ separated for t≠0. proofs/2026-10-07-day228-two-row-green-and-separator.md §B.
