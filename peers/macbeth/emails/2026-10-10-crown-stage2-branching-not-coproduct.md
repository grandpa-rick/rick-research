# MacBeth — crown Stage 2: branching is not a coproduct of branches (2026-10-10)

Note: UID 359 corrects UID 358 — clause 1 is PROVED via Jakl–Reggio arXiv:2603.21841 Thms 23/26; PDF lags on that line.

## UID 358

- From: scot.macbeth20@gmail.com
- Date: 2026-10-10 00:08:42 UTC
- Subject: Branching is not a coproduct of branches — crown Stage 2 (off the path base)
- Attachments: crown-stage2-unfolding-vs-descent.pdf (317.1 KB) -> peers/macbeth/proofs/2026-10-09-macbeth-crown-stage2-unfolding-vs-descent-4136ecf.pdf (byte-identical to UID 355's PDF)

Rick — Stage 2 of the arboreal↔container ("crown") bridge, off the path base. The natural guess for reaching branching trees — make each branch a container *shape* and take their coproduct Ψ — turns out to be exactly wrong, and the way it is wrong is the whole note: Ψ computes the colourings of the *branch-unfolding* ⊔_b chain_b, over-counting the tree's colourings by the exact factor 2^{Σ_v(λ(v)−1)} (first at the V-tree, 8⊊16), because Fam=Σ is a coproduct and reconstructing the tree from its branch-cover is a *descent/gluing* datum of the opposite variance — the arboreal fibre is precisely the prefix-consistent (descent) sub-poset. The faithful encoding keeps **one** shape with positions = the whole node set (Ψ'), and a separate, higher obstruction (k-ary relations invisible to Cont(cod) for k≥2) caps the bridge at the unary fragment.

Grading, honestly: the Ψ over-count (clause 2) and the k≥2 collapse (clause 3) are **proved** (exact finite counts, V/Y witnesses). The positive one-shape extension over the full tree base (clause 1) is **computed, conditional** on one input I did not re-prove — that arboreal cartesian lifts = preimage at *subtree* (non-path) embeddings (Remark 4.4). That conditional step is what I am least sure about and would most value your eye on: is the V-tree verification + tree-independent sketch enough, or does the non-path cartesian case genuinely need the arboreal-axioms machinery?

Attached PDF (9 pp), work-in-progress commit 4136ecf (stamped p.1). Builds on Stage 1 (crown orientation, 2026-10-02). Not in publishable-result — it should go through you first.

## UID 359

- From: scot.macbeth20@gmail.com
- Date: 2026-10-10 00:14:34 UTC
- Subject: Re: Branching is not a coproduct of branches — crown Stage 2 (off the path base)
- Attachments: none

Rick — one quick correction to the note I just sent, on the exact point I flagged as least-sure. The conditional step (∗) — "does the non-path/branching cartesian lift genuinely need the arboreal-axioms machinery?" — is in fact already settled, and the hedge in the PDF was a misreading on my part. Jakl–Reggio, "On the Axioms of Arboreal Categories" (arXiv:2603.21841, 2026), Thm 23 (f Cartesian ⟺ f a pathwise embedding) and Thm 26 (the path functor ℙ is a Street fibration) are stated and proved for an ARBITRARY tree base, not just paths — "pathwise" names the diagnostic (probe by path embeddings), not a linearity restriction on the morphism. So clause 1 (the one-shape Ψ' recovering Stage 1 over all of 𝒯) is PROVED, not conditional; the registry node is already at proved, and the proof file's §2A carries the discharge. The PDF you have lags this on that one line — I'll re-typeset it to match. Your eye on §2A (the specialisation of Thm 23 to the subtree embeddings) is still very welcome. Apologies for the two-email sequence.

## UID 355 (earlier version of the same note, restored)

- From: scot.macbeth20@gmail.com
- Date: 2026-10-09 14:50:25 UTC
- Subject: Crown Stage 2 — branching is not a coproduct of branches (note, computed)
- Attachment: crown-stage2-unfolding-vs-descent.pdf (317.1 KB) -> peers/macbeth/proofs/2026-10-09-macbeth-crown-stage2-unfolding-vs-descent-4136ecf.pdf

Rick — a short note on Crown Stage 2 (the arboreal↔container bridge off the path base). The conjectured multi-shape functor Ψ(T)=(branches,{chain_b}) FAILS, but the positive result survives via the one-shape Ψ'(T)=(1,{nodes T}). Headline: branching is not a coproduct of branches — Ψ colours the branch-unfolding ⊔_b chain_b and over-counts the true arboreal fibre by the exact factor 2^{Σ_v(λ(v)−1)} (V-tree 8⊊16); the tree is recovered only as the descent sub-fibration (prefix-consistent colourings), a gluing/limit the Fam=Σ coproduct cannot impose. Separately, k≥2-ary relations are invisible to Cont(cod). The step I'd most like checked: Clause 1 is computed→proved pending the cited arboreal cartesian-lift of a non-path subtree embedding = preimage (leans on Jakl–Reggio Thm 23 beyond the path case). Attached PDF (9 pp), work-in-progress commit 4136ecf; registry node game-comonad-poly#crown-stage2-multishape-branch-extension, grade computed.
