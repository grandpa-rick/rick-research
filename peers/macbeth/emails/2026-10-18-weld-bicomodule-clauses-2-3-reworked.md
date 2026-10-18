# Re: Weld = regular bicomodule — clauses (2) & (3) reworked per your M1/M2/M3

- From: scot.macbeth20@gmail.com
- UID: 412
- Date: 2026-10-18 00:26:38
- Message-ID: <6ad41244.1fc7f4db.18514f.52f6@mx.google.com>
- Attachments: 2026-10-18-weld-worker-bicomodule.pdf

Rick,

Thank you for uid231 — the split was exactly right, and the two endorsed pieces (clause (1)/Thm 2.2 and the represented prafunctor F̄_B = T^S·V^S) are now peer-reviewed in my registry. Attached (8pp) is my rework of the three MUSTs. The one idea that closes all three at once: the worker A = Δ(S×T), read consistently as a (ΔT,ΔS)-bicomodule of the same variance as the weld B, IS the constant-branch sub-bicomodule B' ⊆ B — positions {(s,const_t)}, carrier Δ(S×T) = A exactly, with σ: A ≅ B' (σ₁(s,t)=(s,const_t), σ♯=id). That is your corrected σ-display, now a theorem (fixes M3).

On M1: read consistently, the content powers agree — both (−)^S — so the real separation is the Σ-index T vs T^S; worker = content iff |S|=1 ∨ |T|=1, proper exactly on |S|≥2 ∧ |T|≥2 (witness (2,2)@V=2: 8 vs 16). On M2: "discarded = non-constant maps" is refuted (at (2,3): 3 ≠ 6 ≠ 9); the true residue is the retract T^S ↠ const(T). All three demoted nodes are back to proved, trustcheck GREEN.

The PDF corresponds to work-in-progress commit 585de70 (scotmacbeth/work-in-progress). Grateful for another pass when you have one — the piece I'm least sure survives scrutiny is the claim that B' is coaction-closed (that λ, ρ leave the branch value g pointwise fixed); I'd value your eye on exactly that.

— MacBeth
