# =?UTF-8?Q?Standalone_band-boundary_note_(ex?= =?UTF-8?Q?tract_of_gerbe_=C2=A75)_=E2=80=94_for_your_eye?=

- From: scot.macbeth20@gmail.com
- Date: 2026-10-11 13:46:14
- UID: 374
- Message-ID: <6acb932c.99020481.232b09.7100@mx.google.com>
- Attachments: inventory-band-boundary.pdf (297.3 KB)

---

Rick —

I have pulled the band story out of §5 of the inventory gerbe note (the one you are re-reviewing) and written it up as a self-contained ~8-page note: "The band boundary: the first nonabelian obstruction of the supply-chain inventory gerbe" (attached). It is a Strathclyde mini-course handout and a grant beat; a one-slide summary lives alongside it on GitHub. It re-proves nothing new — it restructures already-submitted material for a reader who has not seen the parent note.

What is claimed, and at what grade (please hold me to these):
1. Lemma (band is a strict Out-cocycle), Thm a (triviality criterion, β=0 ⟺ transport inner up to outer relabel), Cor a′ (staged obstruction) — proved, elementary Schreier; D4 machine-check. Unchanged from §5.
2. Thm b (fungible S_n doubly vacuous; disjoint exceptions n=6 / n=2) — proved, classical Aut(S_n)/Z(S_n) arithmetic + explicit S_6 outer-automorphism witness. Unchanged.
3. Thm c (nonvacuous band on (Z/p)^2 + BZ) — explicit machine-checked witness (β=[A]≠0), clean S^1 separation. Unchanged.
4. §6 coupling on T^2 — NEW relative to the gerbe note you have, flagged explicitly as trust grade `computed` (not refereed, not Lean). Reports the G=D4×C2 witness where a nonzero band forces a nonzero degree-2 lifting class δ(β)=[A,B]=[s]≠0. Two honest corrections baked in: (i) the connecting-map coefficient is Inn G, NOT Z(Aut F); (ii) δ(β) is independent of the band trivialisation. Minimality over order ≤16 is not claimed; the structured classification is the one open problem.

I would value your eye on: the (⇐)/(⇒) Schreier step in Thm a (surjectivity-of-q lift stated cleanly? cocycle-preservation line watertight?); whether "staged" is right in Cor a′ (that [g] is only defined once β=0, leaning on your N2 that an H² class is a splitting obstruction of an already-associative structure); and whether `computed` is the honest grade for §6.

I have your three round-2 reviews (gerbe r2, crown Stage 2 r2, nerve+uniqueness r2) in hand and am reading them in full now — substantive corrections will follow separately. Note in particular that your N2 (the general "nonabelian + nontrivial centre ⇒ [γ]≠0" is false; sharp criterion = non-splitting of Z→K→Inn K, i.e. 4∣n) does not touch this note's specific witnesses, but I am retracting that general framing wherever it appears in my registry/commit history.

On GitHub (content commit 2fa15ef): papers/inventory-band-boundary.tex (+ .pdf), papers/inventory-band-boundary-slide.md.

Thanks — MacBeth
(CC Robin, as always)
