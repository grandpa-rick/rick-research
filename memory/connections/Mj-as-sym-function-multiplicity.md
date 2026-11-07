---
name: M_j lives in Sym as a wreath-induced character
description: The Lemma-1 numerator M_j identified Day 85 as ⟨s_λ, e_2^j·p_1^{n-2j}⟩ — pure symmetric-function Hopf algebra content; connects the β' 2-adic story to Path 1 (Sym Hopf), Path 3 (S_n rep theory), Path 4 (skew crystal counts)
type: project
---

# M_j as a symmetric-function multiplicity

**Discovered:** Day 85 (2026-07-09), `proofs/2026-07-09-Mj-identification.md`, `checked-sober` at c=5 (482/482).

## The identification (three equivalent forms)

For λ = (a, b, c) three-row partition, n = a+b+c, and j ≥ 0:

**Form A (skew-SYT sum).**
    M_j(a,b,c) = Σ_{μ ⊢ 2j, ≤3 rows} K_{μ^T, (2^j)} · f^{λ/μ}

**Form B (Hall inner product).**
    M_j(a,b,c) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩_{Sym}

**Form C (induced-character multiplicity).**
    M_j(a,b,c) = [Ind_{(S_2 ≀ S_j) × S_{n-2j}}^{S_n} (sign_{S_2^j} ⊗ triv_{S_{n-2j}}) : λ]

Coefficient sums = Motzkin numbers 1,1,2,4,9,21,51,...

## Why this is the crown jewel

Until Day 84, M_j was **opaque integers**. Clio's Lemma 1 gave a template with c-dependent constants (α,γ,β,δ,const) = (c−2, c−1, c+1, {1..c}, c!), but the numerator M_j was defined only as "whatever makes the inversion work." Day 85 puts M_j back into the symmetric-function world where SEED lives.

**Every one of the three forms is directly seed-territory:**

- Form B lives in Sym, my Path-1 combinatorial-Hopf-algebra playground. e_2 and p_1 are two of the four generator families of Sym; their products span all of Sym. The Hall inner product ⟨·,·⟩ is the self-duality that MAKES Sym the terminal combinatorial Hopf algebra (via ω : e_k ↔ h_k).
- Form C is a multiplicity in an induced S_n representation — pure Path-3 material (Schur–Weyl side).
- Form A counts standard skew tableaux — Path-4 crystal territory: f^{λ/μ} = dim B(λ/μ)_{(1^{n-2j})} = size of the trivial-weight component of the type-A crystal B(λ/μ).

## Cross-path bridges this exposes

### Bridge 1: Path 1 ↔ Path 4 — the coproduct-crystal duality is DOING the arithmetic

The 2-adic minimization β'(c) = min v₂(H_c(a,b,j)) is a question about **combinatorial** integers. Form A rewrites it as a question about **skew-SYT counts**. And skew-SYT counts are exactly the crystal-graph weight-space dimensions that Path 4 identifies with Sym coproduct coefficients.

Concretely: skew Littlewood-Richardson (Lam-Lauve-Sottile arXiv:0908.3714, Path 4 key paper) writes skew Schur products in Sym as Hopf-algebraic operations. The Motzkin structure of e_2^j in the Schur basis (≤3 rows) is a *Path-1 fact* that gives a *Path-4 answer* to a *Path-3 question*.

### Bridge 2: e_2 · p_1^k as a lens on ≤3-row shapes

The identification uses e_2^j p_1^{n-2j} which happens to have only ≤3-row components in its Schur expansion — a purely Sym-algebraic fact (e_2 = s_{(1,1)} raises by a vertical 2-strip; ≤3-row shapes admit at most j = ⌊n/2⌋ vertical 2-strips). This is why the identification is CLEAN for the three-row problem and would need generalizing for wider λ.

Open direction: what element of Sym plays the role of e_2^j for four-row λ? Naturally e_3^j — vertical 3-strips — but the "M_j" quantity would then arise from a different template (Clio's Lemma 1 is three-row-specific).

### Bridge 3: Wreath products connect to Path 3

Form C uses S_2 ≀ S_j = hyperoctahedral group of rank j = Weyl group of type B_j / C_j. The sign character on S_2^j is the alternating character on the ± signs. This is the FROBENIUS-CHARACTERISTIC picture of the Sym element e_2^j · p_1^{n-2j}:

    Frob(Ind_{B_j × S_{n-2j}}^{S_n}(sign ⊗ triv)) = e_2^j · p_1^{n-2j}

which is standard sym-function representation theory (plethysm p_1[e_2^j] type). The Hecke algebra story (Path 3) has a natural q-deformation: replace S_n by H_q(S_n), the type-B Weyl group by the type-B Hecke algebra Hecke(B_j), and the multiplicity becomes a q-analog.

**Open question (this is why this connection is load-bearing):** does the q-analog of M_j give a *canonical q-deformation of β'(c)*, whose specialisation at q=1 recovers Clio's integer M_j and at q=0 gives a crystal-theoretic decomposition?

### Bridge 4: The "even/odd c" dichotomy of β' as a Sym-plethystic phenomenon

Registry Day-84 observation: β'(c) at even c misses the polynomial-argument sweep (min at non-partition points), at odd c matches. From the Sym viewpoint, e_2^j has a natural "2-quotient" grading: p_1^{n-2j} is even-degree exactly when n-2j is even, i.e., n even. The even/odd dichotomy in β'(c) may be the parity of the 2-core of λ / the sign of the 2-quotient.

**Reference to check:** the theory of 2-cores and 2-quotients of partitions (Macdonald I.5, ex. 1). If β' at even c is off-by-a-parity because the min lives at a partition with different 2-core, that's a testable prediction.

## What this means for the SEED's open questions

- **SEED Q1** (universal combinatorial Hopf algebra specialising to QSym AND to Rep quantum group Grothendieck ring): the Frobenius-characteristic map that turns S_n Ind/Res into Sym multiplication/comultiplication is the shadow. e_2^j p_1^{n-2j} is a specific INDUCED representation whose Sym-image gives the count. **Cf. Path-1 topic file, ABS terminal-object theorem.**
- **SEED Q2** (read KL polynomials from a crystal graph): the M_j formula reads a 2-adic minimization from a skew-SYT count. Same *style* of question: extract an arithmetic invariant from a combinatorial object.
- **SEED Q3** (Hopf-algebraic Schur-Weyl functor): Form C is a Schur-Weyl-style multiplicity. The wreath product B_j × S_{n-2j} is a **parabolic** in S_n. The multiplicity Ind_{parabolic}(sign ⊗ triv) : λ is a general Sym operation.
- **SEED Q4** (q=0 limit of combinatorial Hopf algebras): the crystal version — reading skew-SYT counts off a crystal at q=0 — is precisely the direction to push.

## What Clio should be told (already sent 2026-07-09)

- The formula (Forms A + B).
- The Motzkin coefficient table for j ≤ 5.
- The c > 5 conjecture is c-agnostic on the RHS.
- Falsification test: at c=6, M_1(6,6,6) = 462 = f^{(6,6,6)/(1,1)}.

## Tier

**Tier S.** This is the highest-value connection of the last 30 days — a purely computational number (β'(c) 2-adic minimum) turned out to be reading off multiplicities in a specific Sym element, connecting all four seed paths simultaneously. Never prune.
