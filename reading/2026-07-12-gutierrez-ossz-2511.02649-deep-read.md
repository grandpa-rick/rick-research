# Deep read: Gutiérrez–Orellana–Saliola–Schilling–Zabrocki, arXiv:2511.02649

Day 92 P0. Route IV identification check for M_j Sym form.

## §0. Metadata

- **Title:** A geometric and generating function approach to plethysm
- **Authors:** Álvaro Gutiérrez, Rosa Orellana, Franco Saliola, Anne Schilling, Mike Zabrocki
- **arXiv:** 2511.02649, v1 4 Nov 2025, v2 4 Apr 2026 (dated April 7, 2026)
- **Abstract (verbatim):**
  > Plethysm coefficients a^λ_{μ[ν]} are the structure coefficients of the plethysm of Schur
  > functions s_μ[s_ν] = Σ_λ a^λ_{μ[ν]} s_λ. We study a bivariate generating function of plethysm
  > coefficients when λ has bounded length. We show that this generating function is rational.
  > A key step is MacMahon's combinatory analysis. When the bound on the length is 2 we give
  > an explicit geometric algorithm to compute it using q-Ehrhart theory. We give evidence that
  > the generating function is the quantum Ehrhart series of a union of half-open polytopes and
  > show that it satisfies a reciprocity theorem reminiscent of Ehrhart reciprocity. Furthermore,
  > we give a set of linear recursions that completely describe the SL_2-plethysm coefficients.

## §1. Their coefficient definition

From §1 eq. before (1.1) (their Introduction):

> The plethysm coefficients a^λ_{μ[ν]} are the structure constants of the plethysm of Schur
> functions,  s_μ[s_ν] = Σ_λ a^λ_{μ[ν]} s_λ.

So **both slots inside the plethysm bracket are Schur functions**: outer s_μ composed with inner
s_ν. No products, no power sums, no elementary. This is pure Schur∘Schur plethysm.

For the SL_2-restriction, §2.2 makes it more concrete. From eq. (1.4)–(1.6) and §2.2:

- Inner partition is a single row ν = (h), i.e. s_ν = s_(h) = h_h (complete homogeneous of
  degree h).
- Outer partition μ arbitrary of size w = |μ|.
- λ has length ≤ 2 (the "SL_2-restriction"), writable as (λ_1, λ_2). Since the coefficient
  depends only on the difference, they parametrise it by k = λ_1 − λ_2 + 1.
- Explicit expansion (eq. 1.4, §2.2):
  s_μ[s_(h)](q, q^{-1}) = Σ_{k≥0} a^{[k]}_{μ[h]} · [k]_q,
  with [k]_q = (q^k − q^{−k})/(q − q^{-1}) the symmetric q-integer (character of the (k−1)-th SL_2
  irrep).
- These a^{[k]}_{μ[h]} are what they call the **SL_2-plethysm coefficients**.

The base case w = |μ| = w (single row): (from §2.2, Macdonald ref)
> s_w[s_h](q^{-1}, q) = [w+h choose w]_q = Σ_{k≥1} a^{[k]}_{w[h]} · [k]_q.

## §2. Main theorem: rational bivariate GF

The bivariate GF (their eq. (1.6)):
> A_μ(z, q) := q · A_μ(q, q^{-1}; z) = Σ_{k≥1, h≥0} a^{[k]}_{μ[h]} · q^k · z^h.

The two variables track: **q** = SL_2 weight index k (outer partition size differential),
**z** = inner row length h.

**Theorem 4.9** (paraphrase — full formula in §4): there exists a polynomial p_μ(z,q) ∈ Z[q^±, z]
such that A_μ(z,q) = p_μ(z,q) / d_{|μ|}(z,q), where d_w(z,q) is an explicit product of factors of
form (1 − z^{2i}) and (1 − q^{2i-1}z) or (1 − q^{2i}z) depending on parity of w. Conjecture 4.1
sharpens this using hook-length products.

Rationality follows from Elliott-rationality preservation under the MacMahon operator applied
to a q-Ehrhart series (Theorem 2.25, Corollary 2.26).

## §3. Complete linear recursion (SL_2 case)

**Proposition 3.2** (verbatim, §3.2, eq. (3.5)). For 1 ≤ k ≤ hw + 1 and k ≡ wh + 1 (mod 2):

    a^{[k]}_{w[h]} =
      { a^{[k-h]}_{(w-1)[h]}                              if wh+1-2w < k ≤ wh+1,
      { a^{[k-h]}_{(w-1)[h]} + a^{[k+w]}_{w[h-1]}         if h < k ≤ hw+1-2w,
      { a^{[k+w]}_{w[h-1]} - a^{[h-k]}_{(w-1)[h]}         if 1 ≤ k ≤ h.

Proof: q-Pascal identity applied to the q-binomial [w+h choose h]_q. Symmetric recursion
(3.6) obtained by swapping w ↔ h.

This recursion is **only for μ = (w) a single row** at the outer slot. Extending to general
outer μ needs §6 machinery (Theorem 6.2).

## §4. Identification attempt: does Rick's M_j fit?

Rick's coefficient:
    M_j(λ) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩  in Λ, with |λ| = n and 2j ≤ n.

Gutiérrez et al. coefficient:
    a^λ_{μ[ν]} = ⟨s_λ, s_μ[s_ν]⟩  in Λ.

For M_j to fit, we need e_2^j · p_1^{n-2j} = s_μ[s_ν] for some (μ,ν) depending on (j,n).

**e_2 as Schur:** e_2 = s_{(1,1)}. So e_2^j = s_{(1,1)}^j.
**p_1 as Schur:** p_1 = h_1 = e_1 = s_{(1)}. So p_1^{n-2j} = s_{(1)}^{n-2j}.

Therefore e_2^j · p_1^{n-2j} = (s_{(1,1)})^j · (s_{(1)})^{n-2j} — a **product** of Schur functions.

A product of Schur functions is generically **not** a single plethysm composition s_μ[s_ν].
Concrete check j=1, n-2j=1:
    e_2 · p_1 = s_{(1,1)} · s_{(1)} = s_{(2,1)} + s_{(1,1,1)}  (Pieri).
There is no (μ,ν) with s_μ[s_ν] = s_{(2,1)} + s_{(1,1,1)}: any nontrivial plethysm s_μ[s_ν]
with both partitions of size ≥ 1 has a canonical leading term but expands into many Schur
functions with specific structure (e.g. s_1[s_ν] = s_ν; s_2[s_1] = h_2 = s_(2); s_(1,1)[s_1] =
e_2 = s_(1,1); s_1[s_2] = s_(2); none of these are s_(2,1) + s_(1,1,1)).

More decisively: for arbitrary j and n-2j, the degree of e_2^j · p_1^{n-2j} is n = 2j + (n-2j).
For s_μ[s_ν] of degree n we need |μ|·|ν| = n. This is a strong constraint that rules out
most (j, n) pairs immediately: e.g. (j=2, n=5) gives n=5 prime, forcing (|μ|,|ν|) ∈ {(1,5),(5,1)},
i.e. s_(1)[s_5] = s_5 = h_5 or s_μ[s_1] = s_μ. Neither equals e_2^2 · p_1.

The paper's Section 6 handles the general "GL_n" case with outer μ still a partition, inner ν
still a partition — see Theorem 6.2. It stays in Schur∘Schur throughout. Products of Schur
functions are not in scope.

**λ length is a separate obstruction.** Even if we ignored the product vs. composition issue,
their P0 theorem (rational bivariate GF, linear recursion) is stated for λ with **bounded
length** — length ≤ 2 for the SL_2 case. Rick needs c-uniformity for arbitrary λ ⊢ n, in
particular for λ with long tails. §6 loosens this (Theorem 6.4 handles B_μ with arbitrary
outer ν), but does not change the Schur∘Schur restriction on the coefficient itself.

**Trying to force it via the identity p_γ[s_ν] expansion:** Eq. (6.5) gives
    P̃_γ(Xn; Ym) = Σ_ν p_γ[s_ν[Xn]] y^ν.
This uses p_k [f] (power-sum plethysm of a Schur function), which is NOT the same as p_k · f
(the product). Power-sum plethysm p_k[f] is the ring endomorphism sending x_i ↦ x_i^k, applied
to f. Rick has p_1 · e_2 (product), not p_1[e_2] (which incidentally is just e_2 by p_1 being
the identity plethysm). So even the §6 machinery does not accommodate Rick's expression.

## §5. VERDICT

**DEAD.**

Rick's M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ has a product s_{(1,1)}^j · s_{(1)}^{n-2j} in the second
slot; Gutiérrez–Orellana–Saliola–Schilling–Zabrocki parametrise ⟨s_λ, s_μ[s_ν]⟩ with a plethysm
composition. A product of Schur functions is not a plethysm composition (Pieri check, degree
count |μ|·|ν| = n obstruction), so the identification fails on the algebra. Their rational GF
and linear recursion (Prop 3.2) buy nothing for M_j. Route IV joins Routes I–III in the graveyard.

---

## Followup notes for the registry

- Rick's `Mj-c-uniform-conjecture` stays at `checked-sober`. No promotion.
- The paper is still worth flagging in `/home/agent/projects/memory/reading/` — the SL_2
  q-Ehrhart / MacMahon operator machinery is a **potential** future tool if Rick can ever
  rewrite M_j as a Schur∘Schur plethysm coefficient by some auxiliary trick. Not seeing that
  trick right now. Registry note: "SL_2-plethysm GF machinery — inapplicable to M_j directly
  (product ≠ composition), keep on ice."
- Kill list update: Routes I (Kannan–Song Λ^[2]), II (Motzkin K-triangle), III (Bechtloff
  Weising (α,β)), IV (Gutiérrez–OSSZ SL_2-plethysm GF) — all falsified as direct identifications
  for the M_j Sym form.
- The right move now is **/expository or /assumptions on M_j itself**. The empirical
  c-uniformity 482/482 is real, but four external frameworks have failed. That means M_j has
  its own internal structure that no existing plethysm/Sym-func literature indexes cleanly.
  Time to build the theory from inside, not fish for external identifications.
