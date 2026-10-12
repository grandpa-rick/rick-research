# MacBeth — corrected Crown Stage 2 note, contravariant Ψ′ (supersedes 4136ecf / 8972231)

- **UID:** 369 | **From:** scot.macbeth20@gmail.com | **Date:** 2026-10-11 01:56
- **Repo:** github.com/scotmacbeth/work-in-progress, content commit 4e7264d (same hash as UID 368); proof file `proofs/2026-10-10-crown-stage2-repair.md`
- **Attachment:** `proofs/2026-10-11-crown-stage2-unfolding-vs-descent-4e7264d.pdf` (11 pp)
- Root cause accepted: encoding functor was covariant, patched with nearest-ancestor retraction ρ_f "which does not compute preimage". Now contravariant.

## Fixes
- **M1:** Ψ′:𝒯^op→Cont, Ψ′(f)=(id₁,j), j node injection carried backward, opcartesian leg = j⁻¹. Stated as iso of indexed posets 𝒯^op→Pos, T↦(2^{nodes T},⊆), f↦j⁻¹; ℙ = opfibration part of Ψ′*Cont(cod) over 𝒯^op. "conditional" removed from abstract/Thm 1(1)/scope. Remark on ρ_f failure (our V-tree: Σ_{ρf}{b}={r}≠∅). Stage 1 uses Φ:𝒫^op→Cont.
- **M2:** (∗) is now our six-line direct proof in coloured category 𝒜. Jakl–Reggio dependence deleted; cited correctly (arXiv:2603.21841, CMCS 2026) as NOT used.
- **M3:** new §4 no-go THEOREM: T↦(br(T),{chain_b}) extends to no functor in either variance (contravariant fails existence; covariant fails functoriality via sibling-swap σ). Branch relation is a SPAN R_f; recovery is descent.
- **M4:** k≥2 "beyond Cont(cod)" claim WITHDRAWN; Ψ′_k(T)=(1,{nodes(T)^k}) with backward j^k reproduces k-ary fibre; 2^{n^k} count corrected.
- Should-fix: descent object = equalizer; cover = Alexandrov topology of down-sets; Open Problem 3 = descent along R_f.
- Clause 2 over-count 2^{Σ(λ−1)} untouched (lean-verified). Registry: crown-stage2-multishape-branch-extension re-promoted to proved; new proved child crown-stage2-psi-no-functorial-action; ceiling node corrected.

## Ask
"I'd welcome a check of the contravariant indexed-poset statement and the no-go before it moves toward publishable."
