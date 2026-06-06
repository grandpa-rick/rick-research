# Lusztig, arXiv:2510.21499 — Notes

## Bibliographic info

- **Title:** Positivity for certain Weyl group representations
- **Author:** George Lusztig (MIT)
- **arXiv:** 2510.21499, October 2025
- **Length:** 19 pages, 7 sections
- **References:** 5 items — only Lusztig's own work (L87, L87a, L16, L18, L19) plus Bezrukavnikov–Finkelberg–Ostrik (BFO 2009). **No reference to Marberg.** No reference to involutions, twisted KL, or Vogan.

## Abstract (verbatim)

> Let W be a Weyl group. We define the notion of positivity of a W-module in terms of the corresponding module over the asymptotic Iwahori–Hecke algebra. Assuming that W is of classical type, we describe a large collection of W-modules which are positive. This includes the special representations of W, the W-modules carried by the left cells of W and also some W-modules which interpolate between these two kinds of modules.

## Contents

1. The algebra F. 2. Proof of Theorem 1.6. 3. Trace computation. 4. The algebra F-bar^e. 5. The centre of F-bar^e. 6. Simple F-modules. 7. Positivity for Weyl group modules.

## Setup and main definitions

### What "positive" means here (Section 0.1, Section 7)

- G is a finite group acting on a finite set X. On X^2 = X × X, the equivariant K-theory K_G(X^2) has a convolution product making it an associative ring (Lusztig 1987a). It has a **C-basis** (0.1)(a): irreducible G-equivariant vector bundles on X^2.
- An K_G(X^2)-module M is called **positive** if there exists a C-basis of M such that every basis element of (a) acts by a matrix with **entries in R_{≥0}**.
- For W an irreducible Weyl group, the asymptotic Hecke ring **J** (Lusztig 1987 §2) has C-basis {t_w : w ∈ W} and decomposes J = ⊕_{c ∈ ce(W)} J_c by two-sided cells. Each J_c is conjecturally (proved in classical types via BFO) isomorphic to a K_G(X^2) ring (with G, X depending on the cell). A C[W]-module E becomes a J-module E_∞ via the canonical iso C[W] ≃ J (L87 3.1).
- **Definition (7.2):** E ∈ Mod_c(W) is **positive** if E_∞ has a C-basis in which every t_w (w in c) acts with entries in R_{≥0}.

### The main combinatorial algebra F (Section 1)

For W of type B/C/D the relevant G is E = a finite-dimensional F_2-vector space (the (Z/2)^n encoding the "type B" signs). The paper builds, completely combinatorially, an algebra **F** modeled on the subspace lattice L of E, with basis indexed by pairs of subspaces and a character ε ∈ (A ∩ B)*. The product is the explicit formula in 1.2. It is shown (Section 4) that F is isomorphic via Fourier transform to ⊕_e F-bar^e, where each F-bar^e is the algebra of E-equivariant endomorphisms of the permutation module on X^e — hence semisimple.

### Main theorems

- **Theorem 1.6:** For any C ∈ L, D ∈ L_X, the subspace [[CD]] of F spanned by an explicit positive basis B_CD is a **left ideal of F**, hence an F-module, **and it is positive** (in the sense above).
- **Theorem 2.4:** [[O]]^α ∈ [[Co]] generates [[Co]] as an F-module.
- **Theorem 5.3:** F-bar^{e,e^*} is a simple algebra (used to identify simple F-modules combinatorially).
- **Theorem 6.2:** The F-module (MP) (for M ⊂ P with M ⊂ D ⊂ E for some D ∈ L_X) decomposes as ⊕_{(e,e^*) ∈ M × P^⊥} ((e,e^*)), a direct sum of |M||P^⊥| pairwise non-isomorphic simple F-modules, multiplicity-free.
- **Corollary 6.3:** ⊕_{(e,e^*) ∈ M × P^⊥} ((e,e^*)) is positive (immediate from 6.2 + 4.7).
- **Theorem 7.5(b)/(c) — the headline result:** For W of type B, C, or D, every irreducible E ∈ Mod_c(W) of the form E^!_∞ = (MP) is positive. Moreover, **every "new representation"** in Mod_c(W) (in the sense of L19's new basis of the representation ring) is positive. For type A, this is also true. Type-exceptional case left as an expectation.

### Positivity for "interpolating" modules (Section 7.4–7.5)

L19 introduced a Z-basis of the Grothendieck group of Mod_c(W) consisting of "new representations" — including but not limited to special representations and constructible (left-cell) representations. The main theorem 7.5(c) is that **all** new representations are positive in classical types.

## What is being shown positive

The polynomials whose nonnegativity is established are the **structure constants of t_w (w ∈ c) acting on a J_c-module in a specific basis** — these are nonnegative integers, by virtue of being matrix entries of the K-theory convolution action of irreducible equivariant vector bundles. There is **no statement about Kazhdan–Lusztig polynomials P_{y,w}** of any kind in this paper. KL polynomials, twisted KL polynomials, involutions, and Vogan's module never appear.

## Method / proof strategy

1. Build the combinatorial algebra F over the lattice L of subspaces of E = F_2^n (Section 1). Prove associativity by direct calculation (1.2(a)).
2. Show that [[CD]] is a left F-module (Theorem 1.6) by the combinatorial trace formula in Section 2.
3. Pass through the Fourier transform F → ⊕_e F-bar^e to identify F as a sum of matrix algebras over the E-orbits of X^e (Section 4). This identifies all simple F-modules combinatorially (Sections 5–6).
4. Theorem 6.2 explicitly decomposes (MP) into simples. This is multiplicity-free.
5. Connect to W via the BFO theorem (the asymptotic ring J_c is iso to K_G(X^2) in classical types). Apply the L19 parametrization of "new representations" to identify (MP) ≃ E^!_∞ for the new reps of cells of classical Weyl groups.

## Connection to Marberg 1306.2980

**The paper does NOT cite Marberg, does NOT mention twisted Kazhdan–Lusztig polynomials, does NOT mention involutions, and does NOT mention Marberg's conjectures B', C', D'.**

The notions of "positivity" are different:

- **Marberg B'/C'/D'** ask that the **twisted KL polynomials P^±_{y,w}** (for pairs of involutions y ≤ w in a Weyl group of type B/D, with the bar-involution twisted by a sign) have **non-negative integer coefficients as polynomials in q^{1/2}**. This is a statement about polynomial coefficients in the involution Hecke module of Lusztig–Vogan (2012/2014).
- **Lusztig 2510.21499** shows that **certain irreducible W-modules** (the "new representations" of L19, which include special reps and left-cell reps) admit a basis in which the standard basis {t_w}_{w∈c} of J_c acts with **non-negative real matrix entries**. These entries are not KL polynomial coefficients — they are structure constants of an asymptotic Hecke algebra acting on a basis of a simple module, equivalent under BFO to integers counting fibers of equivariant K-theory.

There is **no direct logical implication from Lusztig's theorem to Marberg's B'/C'/D'**: the polynomials are not even the same objects.

A speculative bridge: the J-ring J has well-known nonnegativity of its structure constants h^c_{x,y,z} (proved by Bezrukavnikov–Ostrik / BFO for cells, and by Elias–Williamson via Soergel calculus for the full Hecke algebra). Marberg's twisted polynomials live in a quotient/twisted version of H, not in J or in modules over J. So even passing through J (where positivity is "easy") does not visibly produce Marberg's nonnegativity of P^±_{y,w}.

**Verdict on Marberg B'/C'/D': not closed, not partially closed, not obviously approached. The two papers occupy adjacent but disjoint corners of the Hecke-positivity world.**

## Connection to Rick's Aug~ = BGG-Verma differential program

Lusztig's setup is **representation-theoretic of W and J**, working modulo the geometry of K-equivariant sheaves. It says nothing about:
- chain-level / homological models of category O,
- BGG resolutions or Verma differentials,
- the twisted involution Hecke module of Lusztig–Vogan,
- the bidegree-graded Aug~ differential at B_n.

The proof uses combinatorics of F_2-subspace lattices, but this is a different combinatorics than the bidegree (Aug~) one: it indexes simple modules of cells, not the resolution-level chain complexes that Rick targets.

**Bottom line:** Lusztig's J-ring positivity is **unrelated** (in technique) and **non-competing** (in scope) with Aug~. Aug~ aims at a chain-level realization of P^±_{y,w} (Marberg's polynomials); Lusztig's paper proves matrix-entry positivity for new W-modules over J. **Aug~ is not made obsolete; it remains the only candidate combinatorial chain model for Marberg's conjectures.**

## Bottom line in 3 sentences

1. Lusztig 2510.21499 proves that all "new representations" (in the L19 sense, including special and left-cell reps) of W of classical type are **J-positive**: the basis {t_w}_{w∈c} of the asymptotic Hecke algebra acts by nonnegative-real matrices in some basis of the module.
2. This does **NOT** close Marberg B'/C'/D': the polynomials there (twisted KL polynomials P^±_{y,w} for involutions) are different objects from the matrix entries Lusztig proves nonnegative, and the paper does not cite Marberg, involutions, twisted KL, or Vogan.
3. Rick's Aug~ program — a chain-level / bidegree realization of the involution-KL differential — is **not made obsolete** by this paper; it remains the leading candidate for a combinatorial attack on Marberg B'/C'/D'.
