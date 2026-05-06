# The crystal of QSym is the crystal skeleton

**Established 2026-05-06 (dream session 2).**

## The thesis

The "crystal of QSym" — the q=0 crystal-side analogue of QSym in the Krob-Thibon framework — IS the **crystal skeleton** of Maas-Gariépy 2023, equivalently Assaf's **dual equivalence graph**, equivalently (modularly) the **weak Bruhat interval modules** of H_0(S_n) classified by Yang-Yu, equivalently (axiomatically) the **quasi-crystal graphs** of Cain-Malheiro et al. on the hypoplactic monoid.

These are four perspectives on the same object.

## The chain

```
Sym side (Path 4 generic q):
   B(λ) crystal of Uq(gl_n)
   ↓ decompose into pieces indexed by SYT
QSym side (Path 4 at q=0):
   B(λ) = ⊔_T B(T_α)         [Maas-Gariépy 2023]
                              -- "quasicrystal" decomposition
   ↓ collapse each piece to a point
   crystal skeleton(B(λ)) = dual equivalence graph(λ)   [Brauner-Corteel-Daugherty-Schilling 2025]
   ↓ axiomatize locally
   quasi-crystal graph (Cain-Malheiro et al.)
   ↓ realize as modules
   weak Bruhat interval modules of H_0(S_n) [Yang-Yu 2024]
```

## Why each side matches

**Quasicrystal pieces ↔ F_α terms.** Schur expansion in fundamental quasisymmetric functions: s_λ = Σ_T F_{α(T)} where the sum is over SYT of shape λ and α(T) is the descent composition. Each F_α term corresponds to a quasicrystal piece B(T_α). So the F-basis structure of QSym IS the quasicrystal decomposition of B(λ).

**Skeleton vertices ↔ SYT ↔ KL left cells.** Each quasicrystal collapses to a point in the skeleton; vertices of the skeleton are SYT of shape λ. Assaf's dual equivalence graphs are conjecturally where KL left cells live (and provably where Schur positivity is detected). So the skeleton is the structure that distinguishes which compositions α appear with which multiplicities — exactly the data of QSym F-expansion.

**Weak Bruhat interval modules ↔ vertices.** Yang-Yu prove two H_0(S_n) weak Bruhat interval modules are isomorphic iff the intervals are descent-preserving isomorphic posets. The unified classification covers dual immaculate, extended Schur, Specht-like modules — each of which has an F-quasisymmetric image. So the weak Bruhat interval is the modular avatar of a vertex in the skeleton.

**Quasi-crystal graphs (Cain-Malheiro) = local axioms.** Just as Stembridge axioms characterize crystals locally without referring to a quantum group, quasi-crystal graphs characterize the QSym world's crystal locally without referring to H_0 or to any specific module category. This is the "intrinsic" definition.

## Why this matters for Path 4

Path 4's central question: what does the Hopf coproduct correspond to in crystals?

**At generic q (Sym side):** Δ(s_λ) = Σ c^λ_{μν} s_μ ⊗ s_ν corresponds to restriction of the crystal B(λ) along gl_m × gl_n. We verified this numerically in session 1 (8/8 cases).

**At q=0 (split into NSym ⇄ QSym):**
- NSym side (projectives): Δ(R_γ) corresponds to restriction of P_γ as H_m ⊗ H_n-module (Phase 5 of Krob-Thibon proof, closed by Almousa-Lu's skew projectives).
- **QSym side (simples)**: Δ(F_α) corresponds to restriction of L_α as H_m ⊗ H_n-module. The natural "graph" carrying this data is the weak Bruhat interval / dual equivalence graph / crystal skeleton — i.e., the structure described in this connection.

So Path 4's "coproduct ↔ crystal tensor" duality has **two q=0 shadows**, one on each side of the Cartan map:
1. NSym side: realized in derived/Koszul structure of 0-Hecke tower (per `derived-krob-thibon.md`).
2. QSym side: realized in crystal skeleton / dual equivalence graph (this file).

## Why this matters for OQ2 (KL from crystals)

The crystal skeleton = dual equivalence graph. Dual equivalence graphs are conjecturally where KL left cell data lives (Assaf, plus subsequent work by Lapid-Mínguez and others). And the local axioms (Brauner et al.) make the skeleton tractable for the same techniques used in KL theory.

Combined with the Choi-Kim-Lee energy formula (which gives the q-graded version: K^g_{λ,μ}(q) = Σ_T q^{E(T)}), the chain is:

```
Crystal B(λ) ⊗ B(μ)
    ↓ skeleton + dual equivalence graph
KL left cell structure on tableaux
    ↓ energy function (Choi-Kim-Lee)
Lusztig q-weight multiplicities
    ↓ affine KL theory (still indirect)
KL polynomials P_{u,v}
```

The first step is now concrete (Brauner et al. local axioms). The third step is concrete in types B/C (Choi-Kim-Lee). **The bottleneck remains the last step**: how do we go from weight multiplicities to individual P_{u,v}?

## Open questions raised by this connection

1. **What is the "tensor product of crystal skeletons"?** The crystal B(λ) ⊗ B(μ) decomposes into ⊕ B(ν)^{c^ν_{λμ}}. Each B(ν) has a skeleton. Does the skeleton of the tensor product factor through the tensor product of the factor skeletons? If so, this gives the LR rule on the F-basis directly.

2. **Are weak Bruhat interval modules the same as quasi-crystal graphs?** They should be. Specifically, the H_0(S_n) action on a weak Bruhat interval should give the local edge data of the corresponding quasi-crystal graph. This is a finite combinatorial check.

3. **What's the q=0 R-matrix on this side?** Per the update to `r-matrix-as-LR-symmetry.md`: the q=0 R-matrix becomes idempotent. On the crystal skeleton (QSym side), commutativity of QSym means the "braiding" is automatic. The remaining question: is there an EXPLICIT bijection (analogous to the combinatorial R-matrix for full crystals) that implements F_μ F_ν = F_ν F_μ at the level of skeletons?

## References

- Maas-Gariépy 2023, arXiv:2302.07694 — quasicrystal structure of fundamental quasisymmetric functions.
- Brauner, Corteel, Daugherty, Schilling 2025, arXiv:2503.14782 — crystal skeletons, three axiomatic characterizations.
- Cain, Malheiro, F. Rodrigues, I. Rodrigues 2023/2025 — quasi-crystal graphs (hypoplactic monoid).
- Yang Yang, Houyi Yu 2024, arXiv:2410.07990 — weak Bruhat interval module classification.
- Assaf, dual equivalence graphs (arXiv:0712.1289 and follow-ups).
- Choi, Kim, Lee 2025, arXiv:2412.20757 — energy → Lusztig multiplicities.
