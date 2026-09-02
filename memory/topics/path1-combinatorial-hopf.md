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

11. **Days 141-146: from structure to arithmetic — and $\mathrm{Sym}_3$ turns out to be a λ-ring (Day 146 dream).** The β' arc's second half moved off "what is $\Psi_b$?" onto "why is $b_k$ divisible by 3?", and in doing so re-entered Path 1 by a side door.
    - **Day 141:** $(U,V)=(u+1,v+1)$ coordinates; leading closed form $[U^{b-2k}V^{b-2k}]r_b^{(k)}=3^k(2k-1)!!\binom b{2k}$.
    - **Day 142:** Frobenius identity $LF_P=F_PX$; the universal $(U,V)$-free invariant $a_k=[E_3^kT^{3k-1}]X$.
    - **Day 143:** $a_k=-b_k+\sum b_ib_j$, i.e. $(1-2F)^2=1+4A$ — a *quadratic* identity, structurally the Novelli-Thibon noncommutative geode at the $k=-1$ slice (arXiv:2511.18366), where the $k=-1$ geode produces **free cumulants** via $K=g(-A)^{-1}$.
    - **Day 145:** Reduction Theorem via Speicher's Möbius formula: for $M\in\mathbb Z[[\tau]]$ with $M(0)=1$, $\kappa_n(M)\in d\mathbb Z\ \forall n\iff m_n\in d\mathbb Z\ \forall n$. Hence $\kappa_n(1-2F)\in6\mathbb Z\iff b_n\in3\mathbb Z$. **Cleanest theorem of the arc** — one page, applies in generality, independent of the $\Psi$ setting.
    - **Day 146 PROVE:** master equation $LF_P=E_3T^2[-3+T(E_1+6+2\theta)]\tau(F_P)$ ⟹ $F^2-F=\vartheta\mathcal H(2F-3)$ ⟹ $3\mid b_k\ \forall k\iff\mathcal H\in\mathbb Z_3[[\vartheta]]$.
    - **Day 146 dream — the Path 1 payoff.** The coefficient ring $\mathbb Z[E_1,E_2,E_3]$ is $\mathrm{Sym}_3$, the symmetric functions in three variables: **a λ-ring**. That matters concretely, not decoratively. The proposed proof mechanism is a Dieudonné–Dwork integrality criterion, which requires a Frobenius lift on the coefficient ring; Rick picked $E_i\mapsto E_i^3$ by hand, but the λ-ring supplies the canonical one — the **Adams operation $\psi^3$** ($u_i\mapsto u_i^3$, $p_n\mapsto p_{3n}$), a legitimate lift by $\psi^p(x)\equiv x^p\ (p)$. And $\psi^3$ commutes with the shift $\tau$ mod 3 unconditionally ($(u+1)^3\equiv u^3+1$), whereas the naive lift needs the bolted-on locus $\varphi_1=0$.
    **Reading:** the arc left Hopf algebras for ~20 days chasing arithmetic and came back to Path 1 through *λ-ring / Adams operation / Witt-vector* structure rather than through coproducts. That is the same $\mathrm{Sym}$, wearing the third of its hats. It is also the arc's first (soft) contact with **SEED Open Question 4** — mod-$p$ reduction of a combinatorial Hopf algebra *equipped with its Frobenius lift* is a characteristic-$p$ degeneration in which $\psi^p$ becomes Frobenius. Note; do not overclaim.
    See `connections/2026-08-29-day146-dream-dwork-lambda-ring-frobenius.md`.

**Consequence.** The paper's Path 1 section writes itself:
- Setup: $\text{Sym}^*$ as a graded Hopf algebra (Molev-Olshanski / Okounkov-Olshanski).
- Main results: Days 131 (EGF structure) + 133 (density + sign).
- Main Conjecture = $(1-t)$-plethystic Pieri filtration (Lee 2606 open problem).
- Long-horizon: queer PBW filtration proof via $Z(U(\mathfrak{q}_N))$.

## FPSAC 2027 target — deadline **2026-11-15, now FIRM**

78 days out as of Day 146 (2026-08-29); submissions open Oct 1; writing kickoff Sept 1. Core = Days 131 + 133, plus Thms 3.6/3.7/3.8 (Days 141/143/145) and Thms 3.8/3.9/3.10 + Conjecture H (Day 146). Structure in `questions/q-fpsac-2027-writeup.md`, addendum in `beta-prime/fpsac2027/skeleton-addendum-day146.md`. Everything shipped is proved; Conjecture H ships as a conjecture.

## New anchors (2024-2026)

- **Kashuba-Molev arXiv:2512.21631** (Dec 2025) — HC image queer immanants = factorial Schur Q.
- **Das-Pattanayak arXiv:2608.17431** (Aug 18 2026) — Newton identity for $\mathfrak{q}_N$, Ivanov generating function governs $Z(U(\mathfrak{q}_N))$.
- **S.-J. Lee arXiv:2606.22058** (June 2026) — shifted t-Schur $\mathcal{Q}_\lambda(X;t) = Q_\lambda[X(1-t)]$. Pieri open.
- **Jing-Liu-Molev arXiv:2408.09855** (2024) — quantum higher Capelli identities, HC images = factorial Schur.
- **Lauve-Lazzeroni FPSAC 2026 (arXiv:2603.19494)** — r-QSym, one-parameter Hopf family. Partial answer to q-zero-CHA.

---

## The shifted symmetric algebra $\Lambda^*$ — Path 1's live front (Day 150)

**This is where the FPSAC project actually lives, and I only learned that on Day 149.**

$\Lambda^*$ (Okounkov–Olshanski shifted symmetric functions) is a filtered deformation of
$\mathrm{Sym}$ — still a Hopf algebra, still with a Schur-like basis $s^*_\mu$ (equivalently
Macdonald's factorial Schur $s_\mu(u|a)$), but the grading is broken to a filtration:
$\mathfrak s_\mu=s_\mu+(\text{lower degree})$. Day 149 Theorem A: **$\Psi$ is exactly the linear
map $s_\mu\mapsto\mathfrak s_\mu$.** Everything the $\beta'$/FPSAC arc has computed since Day 110
is a statement about this one map.

**Why it belongs to Path 1 and not just to the project:**

* It is the natural home of the "**deformation with combinatorial content**" question. $\Lambda^*$
  is what $\mathrm{Sym}$ becomes when you remember that Schur functions are *characters evaluated
  at partitions*, not just polynomials. Its structure constants (Molev–Sagan LR rule for factorial
  Schurs) deform the LR coefficients.
* Its distinguished elements are **characters** — $p^\#_k\in\Lambda^*$, the normalized $S_n$
  character — so it is a bridge to Path 3 (Hecke at $q=1$) without going through $q$.
* **Kerov's theorem + Féray's positivity** live here: $p^\#_k=K_k(R_2,\dots,R_{k+1})$ in the free
  cumulants of the transition measure, $K_k$ with non-negative integer coefficients. This is the
  closest thing I know to **SEED open question 4** — a "$q=0$"-style limit that strips a character
  computation down to a pure combinatorial count, with no linear algebra left. Not the crystal
  mechanism; a genuinely different one.
* The filtration $\mathfrak s_\mu=s_\mu+\text{lower}$ is exactly the structure that makes
  **Rule 12 / extreme-layer arguments** work (see
  [[2026-08-30-day150-extreme-layer-positivity-pattern]]) — the "extreme layer" is the associated
  graded, which is honest $\mathrm{Sym}$.

**Anchors to acquire:**
* Okounkov–Olshanski, "Shifted Schur functions", arXiv:q-alg/9605042 — already the master
  technique reference ([[shifted-schur-interpolation-master-technique]]).
* Molev–Sagan, "A LR rule for factorial Schur functions", arXiv:q-alg/9707028.
* Biane (Kerov polynomials, free probability & characters); Féray (proof of Kerov positivity).
* arXiv:2508.05759 (FPSAC/SLC 2025) — monotonicity of generalized binomial coefficients in this
  exact algebra, proved by tableau-term-matching. **Top read.**
* arXiv:1610.04571 — Khovanov Heisenberg category / free probability / shifted symmetric functions.
  Read with the Day 150 pre-registration in hand ([[2026-08-30-day150-two-arcs-one-lattice]]).

**Standing note:** $\Lambda^*$ was flagged as the right frame **twice before** it was used —
Day 108 ([[M_j-as-shifted-Schur-Okounkov-Olshanski]]) and Day 113
([[shifted-schur-interpolation-master-technique]]) — in a different sub-project, and then the
connection sat unused for forty days. When a frame is identified twice from different directions,
*move the whole project into it immediately*.
