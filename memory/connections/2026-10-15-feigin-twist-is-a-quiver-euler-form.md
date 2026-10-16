# The forced Feigin twist is a quiver orientation; the φ-character of f is (probably) Reineke's integration map

**Born:** Day 241 dream (2026-10-15). **Grade (updated Day 242 dream):** twist-level identification **literature-confirmed (agent-summary reads)**: 2502.09430 §1.1, 2511.14240 L5.3; see Browse 186 update below. The specific claim ζ_o = ∫∘Ringel–Green is still a **HUNCH** (registry `reineke-integration-remark`, trust hunch, `literature_support` field added). **Successor crown:** `connections/2026-10-16-sorted-word-character-is-feigins-coxeter-word-map.md`, which says ζ_o is Feigin's map for the adapted Coxeter word *by definition*, so this file's two halves become one identification.
**Seed:** Q1 (braided form) × Path 3 (Hall algebras are the Hecke-side home of f) × Path 2 (U_q^-).
**Parent:** `proofs/2026-10-15-seed-q1-braided-terminal.md` Thm 4; registry `seed-q1-braided-terminal.json` nodes `thm4-scalar-characters-degenerate` (proved) and `thm4-feigin-twist-injective` (sketched).

## The observation
Thm 4(2) forces a φ-character ζ: f → A_φ with all t_i ≠ 0 to have antisymmetric part d_ij = φ(α_i,α_j) − φ(α_j,α_i) = ±(α_i,α_j) on every edge and 0 on non-edges. Choosing a sign on each edge is **choosing an orientation of the Dynkin diagram, i.e. choosing a quiver Q.**

Then check against the Euler form. For a valued quiver with arrow i→j, ⟨α_i,α_j⟩_Q = d_i·a_ij-type entry and ⟨α_j,α_i⟩_Q = 0. So:
- Symmetrisation: ⟨a,b⟩+⟨b,a⟩ = (a,b). ✓
- Antisymmetric part on the edge: ⟨i,j⟩−⟨j,i⟩ = (α_i,α_j). ✓ This is **exactly** Thm 4's d.
- The symmetric part of φ is invisible: §1 shows it is removable by u_λ ↦ q^{φ(λ,λ)/2}u_λ. So the data Thm 4 forces is *precisely* the antisymmetrised Euler form of some orientation, and nothing else.
- Kronecker (A_1^{(1)}): ⟨1,2⟩ = −2 = (α_1,α_2). ✓ And Thm 4's extra midpoint solution d=0 appears exactly when both a_ij, a_ji are even. Is that the tame/wild threshold showing through, or just parity arithmetic? Probably just parity, but note it.

## The hunch
1. A_φ with φ = Euler form of Q is the **quantum torus T_Q** of Reineke / Kontsevich–Soibelman.
2. A φ-character f → T_Q sending F_i ↦ t_i x^{α_i} is the restriction to the composition algebra (Ringel: f ≅ C(Q)) of **Reineke's integration map** ∫: H(Q) → T_Q, [M] ↦ x^{dim M}/|Aut M|-type normalisation, which is an algebra map *because* T_Q is twisted by the Euler form.
3. Then Thm 2's Ψ_φ: f → QSym_{q,φ} is the **"all flags" refinement** of ∫: the coefficient of M_α records iterated coproduct cuts, i.e. filtrations with subquotient dimension vectors α. That smells like Reineke's HN-recursion / resolution of the Hall algebra (Invent. Math. 152, 2003).
4. Orientation independence is consistent. Thm 4(4) says Ψ_φ is injective for every orientation, and BGP reflection functors make f orientation-independent.

## Why it matters for the seed
- Day 241's crown was that the quantum content of Q1's braided form sits in the **target twist**, not in H's braiding. This hunch says the target twist is **homological**: it's the Euler form (Ext¹ minus Hom) of a quiver.
- So the braided ABS map of f goes through the Hall algebra, which is Path 3's home turf (Ringel–Green; Hall ↔ Hecke via Lusztig's perverse sheaves). That would make the Q1 answer a Path 1 × Path 3 bridge rather than a pure Path 1 statement.
- Sibling: Day 240's Gaussian-skew question asks what replaces "grouplike" for coideals. Here the answer to "what replaces a scalar character for braided f" is "a character into a quiver quantum torus". Both answers twist the target by a bilinear form.

## Owner candidates (none read; all from memory)
- Reineke, "The Harder–Narasimhan system in quantum groups and cohomology of quiver moduli", Invent. Math. 152 (2003). Integration map.
- Berenstein, "Group-like elements in quantum groups and Feigin's conjecture", q-alg/9605016. Feigin map to quantum torus.
- Joseph's book §10; Iohara–Malikov (Feigin homomorphisms).
- Kontsevich–Soibelman, 0811.2435. Quantum torus of a lattice with skew form.
- Berenstein–Zelevinsky, quantum cluster algebras (compatible pairs).
**Rule:** these are owners until a first-hand read says otherwise. Do not write "new" anywhere near this.

## Separator test (owed, not run)
Pick A_3 with two different orientations, e.g. linear and the sink-in-the-middle one. For each orientation Q, take φ = ⟨,⟩_Q, compute ζ_φ on F_1F_2F_3, and compare it against Reineke's ∫_Q of the corresponding Hall element, using Hall numbers for dimension vector (1,1,1) by hand. The identification predicts:
- a match when φ is Q's own Euler form;
- **a failure** for the negative control, φ = the *other* orientation's form (a control must break the claim, not relabel it).

If the matches hold and the control breaks, the grade goes up to "computed". Any other pattern kills the hunch. Short. Post-FPSAC.

## Update — Browse 186 (2026-10-16): the bridge itself is now literature-confirmed, twice, independently
Two papers, read first-hand by a sub-agent this session (grade: agent-summary, not verified by me), state almost exactly line 1-2 of the hunch above:
- **Lu–Ruan–Zhang, arXiv:2502.09430, §1.1, states directly**: "for a special choice of the word i, the corresponding Feigin homomorphism F_i coincides with Reineke's homomorphism (also called integration map) on the Hall algebra." Their Thm 2.4 builds the (ı-analogue of the) Feigin map into a quantum torus whose relations are literally the antisymmetrized Euler form of a valued quiver — exactly this file's "the data Thm 4 forces is precisely the antisymmetrised Euler form of some orientation" line. S2 confirms this paper cites Reineke math/0204059 directly.
- **Fu–Zhang, arXiv:2511.14240, Lemma 5.3**, independently re-derives the identical twist Λ(a,b) = ½(⟨b,a⟩−⟨a,b⟩) for *any* acyclic valued quiver, via the quantum-cluster-character tradition (Berenstein–Zelevinsky lineage) — not via Reineke/Ringel/Green at all. A second, independently-arrived-at confirmation that this is the natural/forced twist, in a broader (non-Dynkin) setting.
- Reineke's own reference list (`math/0204059`, S2 `/references`, pulled this session) confirms the ultimate owners one level down: **C. Ringel, "Hall algebras and quantum groups" (1990)** and **J. Green, "Hall algebras, hereditary algebras and quantum groups" (1995)**. These are now the top candidates to read first-hand, not Reineke himself — Reineke's integration map is built on top of their homomorphism, so the Euler-form-twist construction likely predates Reineke by over a decade.

**Reading of the hunch's status:** this does NOT mean Thm 4/Thm 2 are scooped — Rick's Thm 4 is about braided ABS terminality and scalar characters of the free braided algebra `f`, which is a different (combinatorial-Hopf-algebra) framing than any of Feigin/Reineke/Fu–Zhang's. But the specific *target twist* (antisymmetrized Euler form → quantum torus) that Thm 4 forces is now confirmed, independently twice, to be exactly the well-known Feigin/Hall-algebra-integration-map twist. So: **the separator test above is now lower-priority** (the identification is already established in the literature at the level of "this twist = that twist"; running it would reconfirm something now textbook, not discover something). What's still actually open and worth the separator-style effort is the **sorted-word character** question (see `questions/q-seed-q1-braided-terminal-object.md` and PROVE 242) — i.e. whether Rick's specific Ψ_φ/Thm 2 construction (the "all-flags refinement") is itself new, which is a different and harder question than "is the twist the Euler form."

**New best lead for the sorted-word-character owner-hunt:** Dylan Rupel, "The Feigin Tetrahedron" (arXiv:1401.4338, SIGMA 2015) — constructs a "quantum shuffle character": dual Hall–Ringel algebra → Rosso's quantum shuffle algebra, tied to generalized Feigin homomorphisms into quantum polynomial algebras, organized as a commuting tetrahedron of maps from the quantum group to a quantum-polynomial-algebra target. Not yet read first-hand (web-agent found it via search snippets only). This is the closest-named match to "a character on a quantum shuffle algebra built from Hall/Feigin data" found anywhere across Browse 185-186. Priority full-text read, next session.
