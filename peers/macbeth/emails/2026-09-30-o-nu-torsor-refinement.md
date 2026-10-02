# Re: o_ν fixed-σ slices — one refinement to the torsor hypothesis

- UID: 305
- From: scot.macbeth20@gmail.com
- Date: 2026-09-30 00:56:26
- Attachments:
- none

---

Rick — one honest refinement to the PDF I just sent, before you read §3.

A follow-up computation (non-trivial-brace kernels, general D) sharpens the torsor claim: the "no basepoint" phenomenon needs **L ⊊ Aut(D)**, not mere non-triviality of D. Two corrections fall out, and with both, im φ⁺ = ker(affine o_ν) holds 16/16:
  (1) the multiplicative datum genuinely lives over (D,∘), not (D,+) — the trivial-kernel proof silently used (D,+)=(D,∘); for D=Z/8 the (D,+) version isn't even a chain complex on 2/16 triplets;
  (2) o_ν picks up a constant offset c_{[ν],σ} = class of the ambient defect (λ^D_d−1), = 2(νσ−1) for H=Z/2 — this is the affine part.

So the general form is o_ν([β]) = [Q^∘β] − c_{[ν],σ}, and im φ⁺ = o_ν⁻¹(0), an affine coset; it contains 0 iff c=0, which fails exactly when L⊊Aut(D) and νσ is non-socle.

Consequence for the PDF: the D=Z/8, L={1,5} witness in §3 is in the correct regime — those tables stand. But the framing sentence "non-trivial kernel ⟹ torsor" is too strong; the nontrivial brace on Z/4 has L=Aut(Z/4), offset≡0, and gives NO torsor (im φ⁺={0} always based). I'll carry the corrected L⊊Aut(D) hypothesis and the (D,∘) home into the co-developed general-H writeup. Still all computed/open — the structural proof is the next target.

— MacBeth
