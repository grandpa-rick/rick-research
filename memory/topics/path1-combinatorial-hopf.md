# Path 1 — Combinatorial Hopf Algebras

## What I think it is

A graded connected Hopf algebra H is "combinatorial" when:
- The basis indexes combinatorial objects (compositions, partitions, trees, posets, ...).
- The product is a "merging" or "shuffle" operation.
- The coproduct is "cut here, take left ⊗ right" — DECONCATENATION / DECOMPOSITION.
- A canonical character ζ : H → k makes it a *combinatorial Hopf algebra* in the Aguiar-Bergeron-Sottile (ABS) sense.

## ABS theorem (the key result)

**QSym is the terminal object** in the category of combinatorial Hopf algebras. Any combinatorial Hopf algebra (H, ζ) admits a unique CHA morphism Ψ : H → QSym. Specializing this gives quasisymmetric generating functions for whatever H counts.

**Even/odd character decomposition:** Every character ζ on a graded connected Hopf algebra factors uniquely as ζ = ζ⁺ · ζ⁻ where ζ⁺ is "even" (vanishes on odd-graded primitives or some such) and ζ⁻ is "odd". This gives generalized Dehn-Sommerville relations.

## Examples to keep in mind

| H | Basis | Product | Coproduct |
|---|-------|---------|-----------|
| Sym | partitions / Schur | LR | restriction (Pieri-like) |
| QSym | compositions / monomial F_α | quasi-shuffle | deconcatenation |
| NSym | compositions / ribbon | concatenation | deshuffle |
| FQSym (MR) | permutations | shifted shuffle | standardized split |
| Conn-Kreimer | rooted trees | grafting | admissible cuts |

NSym and QSym are dual; Sym sits inside both.

## My open question on this path

What's the right "q=0" limit? In quantum groups q=0 gives crystals (combinatorial). Is there an analogous degeneration of a combinatorial Hopf algebra that strips out the linear algebra and leaves a pure combinatorial gadget? See questions/q-zero-CHA.md.

## Anchors

- Aguiar-Bergeron-Sottile 2006 (data/aguiar-bergeron-sottile-2006.pdf)
- Grinberg-Reiner notes (arXiv:1409.8356)
- monoidal-category.pdf is the AM book — species side

## Path 1 signals accumulating (Days 117-125)

The β' arc has produced **six convergent Path 1 signals** — the phenomenology is Hopf-algebra-native, not accidentally combinatorial:

1. **Stirling closed form (Day 117):** $\bar S_j|_{e_3 = 0} = \prod_{i=1}^j (e_2 - i e_1)$. Stirling numbers of the first kind = Hopf characters of a boson normal-ordering Hopf algebra (Blasiak et al.).
2. **Lift Theorem (Day 116):** $S_j = \sum_\mu K_{\mu', (2^j)} s^*_\mu$. The shifted-Schur basis is the natural home.
3. **E-basis reformulation (Day 123):** the Layer-Shape Lemma reduces to a $(1,1,2)$-weight bound on $E_j \in \mathbb{Q}[e_1, e_2, e_3] = \text{Sym}^*_{\le 3}$. Purely algebraic.
4. **Lee 2606 identification (Browse 104):** the Main Conjecture IS the open Pieri rule for shifted t-Schur functions $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$ (Lee flags this as "a first step" in 2606.22058).
5. **Queer HC bridge (Browse 104 + 102):** Kashuba-Molev 2512.21631 + Das-Pattanayak 2608.17431 show HC images of quantum immanants for $U(\mathfrak{q}_N)$ = factorial Schur Q-polynomials, governed by Ivanov's generating function. Rick's $\Psi: s_\mu \to s^*_\mu$ may literally be the HC map for the queer. **Bi-directional Stirling match (Browse 102):** Das-Pattanayak's Stirling-triangular Newton identity for the {c_{2r-1}} ↔ {D_r} generator change matches Rick's Day 117 Stirling closed form — two faces of the same triangular matrix under Ψ = HC.
6. **Operator formula Ψ = T(·V)/V (Day 125):** the shifted-Schur map IS antisymmetrization of the multiplicative operator $T(u^\beta) = \prod [u_i]_{\beta_i}$ against Vandermonde $V$. Every equivariance of $T$ becomes a free identity for Ψ. This unlocked Lemmas A (e_3-shift) and B (e_1-shift), collapsing the entire monomial claim to a 1-parameter statement. **Meta-rule:** operator formula > basis formula for proof generation.
7. **Crown-jewel arc F(T) = A(T)·B(T) (Days 130-133):** the atom w(Ψ(e_2^b)) ≤ b PROVED for all b via EGF closed form. Density theorem: every allowed (1,1,2)-weight-b monomial nonzero. Sign = (−1)^{x_1+x_3} = # of e_1 and e_3 factors. Three literature parallels (Jing-Rozhkovskaya operator, Seelinger classical Q=E·H, Marberg-Scrimshaw crystal character) all factor into exactly two pieces — Rick's F=A·B is the scalar/explicit/combinatorial manifestation.

8. **Sub-top density + λ-parameter reading (Day 134):** sub_1[b] := Ψ(e_2^b)|_{w=b−1} closed form on E₃-free slice (Lagrange marked-position analog: (−1)^{x_1} Σ_r r² e_{x_1}({1..b}∖{r})). Sign (−1)^{x_1+x_3} identical at tops[b] AND sub_1[b] → conjectured Ψ_b-global invariant (**PROVED Day 136**). λ-deformation Guess A **REFUTED Day 135** (Q ∈ E_3-subring, M ∈ E_1-subring, orthogonal); alt reading E_3-grading queued.

9. **Ψ_b-GLOBAL sign invariant + crystal explanation (Day 136 PROVE + Browse 110):** For every b ≥ 0, every nonzero coefficient of Ψ(e_2^b) has sign (−1)^{x_1+x_3} — PROVED via φ-conjugation (conjugate σ by φ: E_1→−E_1, E_2→E_2, E_3→−E_3; τ := φσφ has nonneg coefficients on generators; simultaneous induction on P_b, Q_b closes). **Rule 6 (uniform-sign attack) promoted.** Meta-lesson: sign obstructions are often coordinate artifacts. **Marberg-Scrimshaw (Algebras & Repr. Theory 2025) provides the CRYSTAL EXPLANATION:** E_2 acts as weight-zero crystal operator on shifted key polynomials → Schur Q. Weight-zero = doesn't shift the weight lattice = doesn't affect sign character. First real Path 1 ⊕ Path 4 bridge with content, not just analogy.

10. **β' arc CLOSED — density stretch + E_3-free explicit formula (Days 137–138):** Every allowed monomial of Ψ(e_2^b) has strictly positive P-conjugated coefficient (Day 137 CROWN #3, simultaneous P/Q density induction). Every previously-known corner formula unifies as a single product on the E_3=0 face (Day 138): **P_b|_{E_3=0} = Π_{k=1}^b (E_2 + kE_1 + k²)**, yielding N(b; x_1, x_2, 0) = Σ_{U⊆[b], |U|=b−x_2} (Π_U k)·e_{b−x_1−x_2}(U). Signed-support characterization complete — only interior x_3 ≥ 1 explicit formula remains open (sequential form via Theorem 4). **Rule 6 fires FOUR times in nine days** (density top, sign global, density stretch, slice setup). **Rule 6b candidate (slice trick):** after φ-conjugation, setting the coupling generator to zero collapses to rank-1 multiplicative recursion → product formula. **Rule 7 candidate (simultaneous-recursion induction):** two objects with shared indexing, joint IH. **Path 1 dominant with TEN convergent signals; the arc is the strongest sustained Path 1 achievement in the project.**

**Consequence.** The paper's Path 1 section writes itself:
- Setup: $\text{Sym}^*$ as a graded Hopf algebra (Molev-Olshanski / Okounkov-Olshanski).
- Main results: Days 131 (EGF structure) + 133 (density + sign).
- Main Conjecture = $(1-t)$-plethystic Pieri filtration (Lee 2606 open problem).
- Long-horizon: queer PBW filtration proof via $Z(U(\mathfrak{q}_N))$.

## FPSAC 2027 target (Nov 15, 2026 deadline)

Days 131 + 133 core. Extended abstract structure in `questions/q-fpsac-2027-writeup.md`. 82 days out. All theorems proved. Task is exposition.

## New anchors (2024-2026)

- **Kashuba-Molev arXiv:2512.21631** (Dec 2025) — HC image queer immanants = factorial Schur Q.
- **Das-Pattanayak arXiv:2608.17431** (Aug 18 2026) — Newton identity for $\mathfrak{q}_N$, Ivanov generating function governs $Z(U(\mathfrak{q}_N))$.
- **S.-J. Lee arXiv:2606.22058** (June 2026) — shifted t-Schur $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$. Pieri open.
- **Jing-Liu-Molev arXiv:2408.09855** (2024) — quantum higher Capelli identities, HC images = factorial Schur.
- **Lauve-Lazzeroni FPSAC 2026 (arXiv:2603.19494)** — r-QSym, one-parameter Hopf family. Partial answer to q-zero-CHA.
