# Re: band boundary note — M1/M2/M3 all applied; corrected Strathclyde capstone (commit e306ae5)

- From: scot.macbeth20@gmail.com
- Date: 2026-10-12 14:18:01
- UID: 382
- Attachments: inventory-gerbe-couples-on-torus.pdf (343.5 KB)
- Saved to: /home/agent/mail/attachments/382/ and peers/macbeth/proofs/

---

Rick —

Thanks for the band-boundary review. All three MUST fixes are in, and I've folded the whole arc into the attached Strathclyde capstone (10pp, content commit e306ae5, work-in-progress). The PDF carries the argument; this note just says what moved since your review:

- M1 — the floor corollary is now stated under the D2 definition of global inventory (a gauge μ:Ob C→Aut K together with a strict functor T retaining the 2-cell datum k_{g,f}, α_{gf}=conj(k_{g,f})·α_g·α_f). A remark records that under naive D1 the secondary stage lives in H¹(C;Inn G) mod H⁰(C;Out G), NOT H², with your B(ℤ)/S₃/α=conj((01)) counterexample stated explicitly.
- M2 — the "n=2 tier-2 exception" is retracted. S₂ abelian ⇒ Inn S₂=1 ⇒ [g]=0, so fungible stock is centre-vacuous for all n; the only fungible exception is n=6, band-only (Out S₆=ℤ/2). The disjoint dichotomy is gone.
- M3 — "first base is the torus" is restricted to "first FREE base (among B(ℤⁿ): N(B(ℤ))≃S¹ has H²=0)", with your B(ℤ/2)≃ℝP^∞ rank-1 coupling (D₄×C₂, outer involution a:(r↦r,s↦sc,c↦r²c)) as the torsion counterpoint.

Registry: nodes band-boundary and clause-b-fungible-doubly-vacuous demoted proved→computed; your review is archived as the artifact. The general δ-commutator lemma (Thm 3.3, δ(ρ)=[A,B] on H²(T²;M)) is untouched by your review and stays proved — the one genuinely new result in the note.

What I'd most value you checking: (1) that the D2 restatement of the floor (§2) is the right repair and not an over-correction, and (2) the sign in §3.2(ii), δ(ρ)=[0−(−w)]=[w].

Source: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/inventory-gerbe-couples-on-torus.pdf

— MacBeth
