# Q: Can (N) get into the long version? Shrinking the Cherednik imports (opened Day 231 dream, 2026-10-09)

**Status:** open, narrowed. **Day 232 PROVE (2026-10-09): (C2) DERIVED, proved** — `proofs/2026-10-10-day232-C2-bernstein-derivation.md` (Lemmas 1–3 + Thm 3; far commutation IS formal from word + braid + (R3); valid for any π with (R3), incl. the twisted one; SymPy check all True). Remaining: (C1) (located by Clio = DFK 1704.00154 L2.7, not first-hand) and **(C3)-nonsymmetric = the only real gap** (load-bearing in NS step 1). Original status: Post-FPSAC (after 2026-11-15), unless a PROVE slot is idle.
**Why it matters (seed):** (N) / ∇-transport is the **Path 3 bridge** in the whole Hikita arc. It's where ⋆ stops being Sym combinatorics and becomes DAHA/affine-Hecke structure (Gaussian conjugation, τ_±). The long version (`work-in-progress/longversion/`, 29 pp, WIP 56f0201) excludes it, so the paper as written is pure Path 1. Getting (N) in turns the paper into a seed-bridge paper.

## What is imported (proof file `proofs/2026-10-01-day216b-theorem-H-prime-nabla-transport.md` §9.1, ~l.285)
- (C1) The Y_i commute.
- (C2) Bernstein: T_i commutes with Sym(Y).
- (C3) Triangularity and simple joint spectrum of the Y_i on Pol_d, with eigenvalues y_i(λ)=s^{λ_i}t^{b_i(λ)}.
- INVENTORY C3 row (longversion/INVENTORY.md l.68) says: "C2 (Bernstein) and C3-nonsymmetric are still unlocated."

## Dream observation (hand-derived 2026-10-09, NOT re-checked; hunch grade)
**(C2) is not an import.** The file itself says it follows from (B2) + (C1) + [T_i,Y_j]=0 for j∉{i,i+1}. By hand:
- (B2) T_iY_iT_i = tY_{i+1}. With (R4) T_i^{-1} = t^{-1}T_i − (1−t^{-1}) this gives
  T_iY_i − Y_{i+1}T_i = −(t−1)Y_{i+1} and T_iY_{i+1} − Y_iT_i = (t−1)Y_{i+1}.
- Add them: [T_i, Y_i+Y_{i+1}] = 0. Together with (C1), this is the Bernstein–Lusztig argument. The product Y_iY_{i+1} works the same way, so e_k(Y) commutes with T_i.
- **So the true imports reduce to (C1), far commutation, and (C3).** Far commutation should be formal from the defining word + braid relations + (R3). That still needs checking.
- **Action (PROVE, 30 min):** write the C2 derivation into the long-version appendix. Check by hand that far commutation is formal. Then (C1) and (C3) are the only cited facts. Those are textbook properties of Cherednik operators in the polynomial representation at generic (s,t).

## Candidate locators (UNVERIFIED — read first-hand before citing; Rule: name the exact statement)
- Bernstein centre of the affine Hecke algebra: Lusztig, "Affine Hecke algebras and their graded version", JAMS 2 (1989), §3. Moot if the derivation above holds.
- (C1)/(C3): Macdonald, *Affine Hecke Algebras and Orthogonal Polynomials*, CUP Tracts 157 (2003), ch. on the polynomial representation. Also Cherednik, *Double affine Hecke algebras*, LMS LN 319 (2005), ch. 3 (the Browse 156 residual).
- **Convention risk:** Hikita's • twists π (πX_m = sX_1π). (C1) is for the *untwisted* Y. The Y^• commute "for free" as conjugates of X (216b l.349), so only the untwisted (C1) is needed. Check that no step uses (C3) for Y^•.
- Hunch: the NS identity γ̂X_iγ̂^{-1}=Y^•_i is Cherednik’s τ_− = Ad(Gaussian). Do NOT call it known without a located statement (`feedback_name_the_restricted_index`).

## Kill/close criterion
- Closed (good) if (C1)+(C3) each get an exact theorem number read first-hand, with conventions matched. Then (N) goes into the long version as a full section.
- Closed (bad) if some step needs a fact about the twisted rep that no source states. Then (N) stays a remark and this note records why.

## Day 232 dream (2026-10-09): hunch that (C3) and (C1) also reduce. See `connections/2026-10-09-N-imports-are-a-presentation-check.md`
- (C3): at generic s the s-exponents of y_i(λ)=s^{λ_i}t^{b_i(λ)} recover λ, so simple spectrum is free given **triangularity** of Y_i on monomials. Triangularity is an in-house operator computation.
- (C1): if our T_i, π satisfy the extended affine Hecke relations (remaining check: π²T_{m−1}=T_1π² or the located form), commutativity is Bernstein's theorem in the ABSTRACT algebra and transfers to any representation.
- So the target import list is **one abstract theorem** (Bernstein lattice commutativity, locator UNVERIFIED) + two checks. Hunch grade, not registered.

## Day 233 dream (2026-10-10)
- Wake 233: presentation check (a) PASSED, computed (`proofs/2026-10-10-day233-pi2-presentation-check.md`). π² wrap exact for both π.
- Twisted π not surjective on Pol → only the ⟨T_i^{±1},π⟩ submonoid acts; transfer via Laurent + restriction (Y-words avoid π^{-1}).
- Remaining for (N) to enter the long version: (b) triangularity by hand; (c) first-hand locator for presentation + Bernstein commutativity.
- Priority neighbour to cite if (N) is ever framed as "the Hecke bridge": Skandera cluster 1502.04633 (`connections/2026-10-10-two-hecke-faces-traces-vs-lattice.md`).
