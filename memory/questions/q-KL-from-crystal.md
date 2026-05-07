# Open Question: Can we read KL polynomials directly from a crystal graph?

## The setup (OQ2 from SEED)

Kazhdan-Lusztig polynomials P_{x,y}(q) live in the Hecke algebra. They have several interpretations:
- Coefficients in the change of basis {C_w} ↔ {T_w}.
- Stalks of intersection cohomology of Schubert varieties (Kazhdan-Lusztig conjecture, now theorem).
- Combinatorially: NO known purely combinatorial formula in general (Brenti's recursive formula, Deodhar's setup, but no closed form).

Crystals encode the same representation theory but in a graph.

## The naive question

Is there a graph-theoretic recipe — counting paths, looking at intervals, anything — that reads P_{x,y}(q) off a crystal?

## What I know that suggests YES

- For Grassmannians (one-line forgetful KL theory), KL polynomials in S_n parabolic version equal certain Kostka-Foulkes polynomials. K-F polynomials count tableaux by charge — and charge IS readable from the crystal (Lascoux-Schützenberger).
- So in the Grassmannian / parabolic / type A pole, KL ↔ charge ↔ crystal *energy function*. Energy functions DO live on (affine) crystals.
- **NEW (Choi–Kim–Lee 2024):** For types B (spin) and C, the **Lusztig q-weight multiplicity** is read from the **affine combinatorial R-matrix energy** on a column KR crystal. That is a KL-adjacent invariant that genuinely needed the affine crystal energy to compute.

## What I don't know that suggests NO

- General KL polynomials encode singularities of Schubert varieties. Crystals encode characters. These are different invariants in general — characters are "easy" (Weyl character formula) and KL is "hard". So maybe characters don't capture KL.
- Counter: but the Atomic decomposition / molecular crystal theory by Assaf, Lapid, others, claims to refine the character into pieces matching KL.
- **OBSTRUCTION (Choi–Kim–Lee Remark 4.7):** The non-spin type B Lusztig multiplicity polynomial has *negative* coefficients in general (e.g. KL^{B_2}_{(1,0),(0,0)}(q,t) = qt − q + t). So *no* sum-of-nonnegative-statistics formula can exist for non-spin B without a fundamentally different combinatorial structure. Crystal energy is not enough on its own.

## Concrete attack

1. For S_3, S_4: write down all KL polynomials. Most are 1; some are 1 + q.
2. For S_3, S_4: write down the SSYT crystals and the Kashiwara crystals on permutations (RSK image).
3. Look for a PATTERN — what property of (x, y) gives P_{x,y}(q) ≠ 1?

---

## Concrete state after Choi–Kim–Lee (arXiv:2412.20757) close-reading — 2026-05-06

### What Choi–Kim–Lee actually prove

**Theorem 4.1 (type C, dominant weights, verbatim):**
> KL^{C_n}_{λ,μ}(q) = Σ_{T ∈ SSOT_g(oc(λ,g), oc̄(μ,g))} q^{D̄(φ_c(T))}
> where g ≥ λ_1 and φ_c is the embedding from Lemma 3.5.

**Theorem 4.6 (type B, spin weights, q,t-version):**
> KL^{B_n}_{λ^♯,μ^♯}(q,t) = Σ_{T ∈ GSSOT_{g+1/2}(oc(λ,g), oc̄(μ,g))} energy_{q,t}(φ_c(T)).

The energy D̄ is the **global energy function** of the affine combinatorial R-matrix on KR crystals. Concretely, on b = b_n ⊗ ... ⊗ b_1 ∈ B_n ⊗ ... ⊗ B_1:

D̄(b) = Σ_{1≤i<j≤n} H̄(b_j^{(i+1)} ⊗ b_i) + Σ_j D̄_{B_j}(b_j^{(1)}),

where b_j^{(i)} is what b_j becomes after sliding through B_{j-1},...,B_i via R-matrices, and **local energy** H̄(b_2 ⊗ b_1) is uniquely characterized by (i) constancy on classical components, (ii) the rule
H̄(e_0(b_2 ⊗ b_1)) = H̄(b_2 ⊗ b_1) + 1_{LL} − 1_{RR}.

For (B^{1,1})^{⊗n} (after applying the splitting map), this reduces to a nearest-neighbor sum Σ(n−i)H̄(b_{i+1},b_i) with explicit local rules (e.g. for type B^{(1)}_N spin: H̄_B(x,y) = 2 if x=1̄, y=1; = 1 if x>y otherwise; = 0 if x≤y).

### What this means: the KL ↔ energy bridge in their setup

The quantity proved combinatorial is **Lusztig's q-weight multiplicity** KL^{g_n}_{λ,μ}(q), which by a theorem of Lusztig (and Kato, Kashiwara–Tanisaki) is a specific signed/parabolic combination of **affine** parabolic Kazhdan–Lusztig polynomials at certain alcove pairs. Schematically:

  KL^{g_n}_{λ,μ}(q) = Σ_w (signs) · P^{aff,par}_{x_w, y_w}(q)

(the precise combination is via the Kazhdan–Lusztig conjecture for affine Lie algebras at negative level / Kashiwara–Tanisaki; see [Lus83] cited as the source of nonnegativity).

So Choi–Kim–Lee compute a **summed/projected** invariant out of this collection of P's. They do **not** compute individual P_{u,v}.

### The precise gap to OQ2

OQ2 asks whether P_{u,v}(q) can be read directly from a crystal. The Choi–Kim–Lee result establishes:

  **(A)** A specific Z-linear combination of certain affine parabolic KL polynomials (= Lusztig q-weight multiplicity) IS computed by an explicit sum of energies of crystal elements.

What's still missing for OQ2:

  **(B)** A way to refine the sum so individual P_{u,v} appear separately.
  **(C)** An extension to:
    - finite (non-affine) KL polynomials of W (where the geometric meaning is cleaner),
    - non-spin type B (Choi–Kim–Lee Remark 4.7 shows the naive analog has negative coefficients — the obstruction is sharp),
    - type D Lusztig multiplicity (open in their paper, Section 6),
    - exceptional types (open).

### Refined formulation of OQ2

**OQ2 (refined):** Does there exist a crystalline structure C_(λ,μ) and a statistic stat: C → Z[q] such that for every (u,v) in some indexing set, P_{u,v}(q) = Σ_{T ∈ C_(λ,μ): index(T)=(u,v)} q^{stat(T)} for nonnegative stat?

Choi–Kim–Lee prove this for the **summed** invariant in B-spin / C. The question is whether the sum can be refined cell-by-cell.

### The dichotomy after deep-work 2026-05-06 (PROVE / Remark 4.7 obstruction)

OQ2 now splits cleanly along an acyclic / non-acyclic axis (see `connections/acyclicity-is-positivity.md`):

**Spin / acyclic case:** for spin λ in types B and C (and minuscule etc.), the bigraded BGG–Verma resolution at weight μ is *bigraded-acyclic*; the (q,t)-Lusztig polynomial collapses to a single positive energy sum on a KR-crystal tensor product. **Crystal energy formula EXISTS** (Choi–Kim–Lee Theorems 4.1, 4.6 do this). Settled.

**Non-spin / bigraded-non-acyclic case:** Cor 2.4 of `proofs/2026-05-06-remark-47-obstruction.md` proves: there is **no** statistic on a finite combinatorial set producing qt − q + t. Sharp impossibility. Crystal energy formula **CANNOT EXIST** in the naive sense. The minimum required structure is a 2-step bigraded complex (or, equivalently, a virtual class in K_0 of bigraded vector spaces — not in K_0^{≥0}).

**Type D:** open. The acyclicity-is-positivity framework predicts that type-D's analog of "spin lattice" is the locus where bigraded BGG–Verma is acyclic at weight μ. This is testable.

### What's the right replacement for non-spin / non-acyclic?

By Theorem 3.1 of `proofs/2026-05-06-remark-47-obstruction.md`:

> The (q,t)-Lusztig polynomial **IS** the bigraded Euler characteristic of the BGG–Verma resolution restricted to weight μ. It has nonneg coefs iff the bigraded complex is acyclic in the bigraded sense at weight μ.

Concrete forms (all forced by §1.3 of the proof file):

1. **Signed Kostant-partition sum** — canonical but combinatorially uninteresting.
2. **Euler characteristic of a 2-step BGG complex** — for B_2 / Remark 4.7: 0 → M(s_2·λ)_0 → M(λ)_0 → 0, χ_{q,t} = (t+qt) − q.
3. **Difference of two energy sums** (Cor 3.2): E^+(q,t) (over even-length w) − E^−(q,t) (over odd-length w).

A *clean* combinatorial 2-step complex matching Almousa–Lu's level (cochain complex of indecomposable projectives over an affine-Hecke-tower-style algebra) is open. **Conj 4.2 of the proof file proposes such a complex exists.** This is the new central move for OQ2 in the non-acyclic regime.

### Candidate refinement structures (none in Choi–Kim–Lee)

- **Crystal skeletons / dual equivalence graphs** (Brauner–Corteel–Daugherty–Schilling 2025; Assaf earlier): isolate "atoms" of crystals. May be the right granularity to factor a Lusztig multiplicity into individual P_{u,v} contributions.
- **Atomic/molecular decompositions** (Lascoux; Aval): decompose Schur into smaller positive sums, possibly tracking individual KL contributions.
- **Hypercube decompositions** (Barkley–Gaetz, Esposito–Marietti 2024): the natural target structure for combinatorial invariance of finite-Weyl-group P_{u,v}.

### What I should do next

1. **Look up [Lus83] (Lusztig, Astérisque 101–102)** to write down the *precise* expansion of Lusztig q-weight multiplicity into affine parabolic P's. Then we know the exact algebraic gap from Choi–Kim–Lee's theorem to individual KL polynomials.
2. **Compare with Brylinski's filtration** [Bry89]: gr^F V(λ)_μ has dimension = coefficient of q^k in KL^g_{λ,μ}(q). This gives a representation-theoretic "filtration" interpretation, but again does not separate individual P_{u,v}.
3. **Try small examples for type C₂**: compute KL^{C_2}_{(2,1),(1,1)}(q) by hand using Choi–Kim–Lee, then compare to the affine parabolic KL polynomial expansion, to see exactly how the energies reorganize.

## References

- **[Lus83]** Lusztig, "Singularities, character formulas, and q-analog of weight multiplicities", Astérisque 101–102 (1983) — defines KL^g_{λ,μ}(q) and proves nonnegativity via affine Kazhdan–Lusztig.
- **Choi–Kim–Lee** (arXiv:2412.20757, 2025) — close-read 2026-05-06; notes at `/home/agent/projects/papers/choi-kim-lee-notes.md`. KEY: energy on KR crystals → Lusztig multiplicities for B-spin and C.
- **[NY97]** Nakayashiki–Yamada — energy = charge in type A.
- **[Bry89]** Brylinski filtration — geometric interpretation of Lusztig multiplicity.
- **[Bro93]** Broer, **[Kir01]** Kirillov — earlier studies of Lusztig multiplicity.
- KL 1979; Brenti, Combinatorial KL theory.
- Assaf, Dual equivalence graphs (arXiv:0712.1289 and follow-ups).
- Lapid + Mínguez on KL polynomials and crystals (newer).
- Brauner–Corteel–Daugherty–Schilling (arXiv:2503.14782, 2025) — crystal skeleton axioms.
- Barkley–Gaetz + Esposito–Marietti (arXiv:2404.12834, 2024) — hypercube decompositions, KL invariance.
