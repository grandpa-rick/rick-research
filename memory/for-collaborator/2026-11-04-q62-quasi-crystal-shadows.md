# Q62 (PROVE 275, 2026-11-04): which Hopf operation the quasi-crystal tensor rule shadows

Not for the FPSAC cut or the 11-04 note. File: `proofs/2026-11-04-q62-quasi-crystal-tensor-rule.md`.

- The hypoplactic quasi-Kashiwara operators on words are factor-local. The rule is Kashiwara's signature rule plus a kill clause:
  if the left factor has an i+1 and the right factor has an i, then ε̈ = φ̈ = ∞. This is almost surely owned by Cain–Malheiro(–Rodrigues). Owner check owed.
- Quasi-crystal components = standardisation classes, with character F_{iDes}. The tensor product decomposes by position-shuffles, so the tensor rule shadows
  the QSym **product**. It does **not** shadow deconcatenation. Smallest counterexample: F_1F_2 ∋ F_21, but ΔF_21 has no F_1⊗F_2 term.
- Deconcatenation is the shadow of **Levi branching** (drop the operator i = a). For crystals the two coincide (c^λ_{μν}); in QSym they don't, and σ↔σ⁻¹ swaps them.

**Dream 275 update.** Owner of the first bullet: Cain–Guilherme–Malheiro arXiv:2301.00271 §5.2 (Z_0-valued signature rule, Prop 5.9). I haven't read it first-hand yet, and their
⊗ order looks reversed relative to word concatenation, so check that before anyone cites it. The σ↔σ⁻¹ swap is almost certainly Malvenuto–Reutenauer's FQSym self-duality seen through the
quasi-crystal. The Path-4 takeaway (`connections/2026-11-04-tensor-and-branching-split-in-QSym.md`): "coproduct = branching = tensor rule" in Sym is two operations that self-duality merges.
