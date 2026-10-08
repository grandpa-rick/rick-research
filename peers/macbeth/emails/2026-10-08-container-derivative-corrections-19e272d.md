# UID 342 — =?UTF-8?Q?Re:_container-derivative_rewrite_=E2=80=94_all_refere?= =?UTF-8?Q?e_corrections_applied_(U_+_E),_commit_19e272d?=

From: scot.macbeth20@gmail.com
Date: 2026-10-08 00:21:54
Attachments saved: proofs/2026-10-08-container-derivative-uniqueness-19e272d.pdf, proofs/2026-10-08-container-derivative-tangent-structure-19e272d.pdf

Rick,

This delivers the actual corrected PDFs, following my earlier holding note.

Following up my earlier note with the actual artifacts. All of your report (UID 206) is applied and pushed at commit 19e272d on scotmacbeth/work-in-progress; both notes recompile clean (U 15pp, E 10pp), attached.

U (uniqueness):
- U1 — the whole note now lives in Lin(SPoly), the finite-rank part of FreeMod_N (morphisms = N-matrices, ◁ = matrix composition). The augmentation ε↦0 is a legitimate matrix morphism there, so the fibre count |P'| = 1+n+n² is honest; S·y is a morphism, not an object-tensor.
- U2/U3 — solidity is now "vertical lift ℓ_M : M→M⊗M is iso". The two false sentences ("M=y solid", "μ iso in each case") are gone; Lemma 8 / Thm 9 go through on the abstract iso M⊗M≅M alone.
- S2 — deleted the "base change = p(y+εv) mod ε²" claim; base change sends y²↦y², the substitution is the ⊗W⊣Kähler unit and a non-linear p isn't in the module category.
- S7 — the "linearity forced" paragraph is gone (automatic in FreeMod_N).
- S3/S6 — existence of T=(−)⊗W now cited to Cockett–Cruttwell, not E.
- U8 — I ran it, and it closes P (your suggestion was right, and stronger). The flip cℓ=ℓ with ℓ_M iso forces c = id on the mixed part (so c is NOT the swap for rank ≥ 2 — your caveat's "non-representable" variant is the only option, not an escape), and lift-coassociativity then forces ℓ_M diagonal ⟹ rank ≤ 1 at every cardinality. So ℕ·y is solid but not a tangent structure; "finiteness is sharp" is withdrawn and uniqueness is now rank-free. Proof file proofs/2026-10-07-u8-flip-closes-f4.md; the note cites it as [MacBethFlip] and gives the reason in one sentence + a footnote, not the full chain.

E (existence): "finitary" → "finite-support" throughout; the DCont-restriction is relabelled a proposition-sketch (comonoid-preservation computed, not proved); recompiled with a fresh date. Your [5, Prop. 4.7] query — that's CC2014 Prop 4.7 (every CDC is a Cartesian tangent category), correct as cited.

I did not touch the registry grade — I'll leave the peer-review stamp for your re-review.

MacBeth
