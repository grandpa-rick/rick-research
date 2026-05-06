# H_0(S_n) categorifies NSym (after Krob-Thibon)

**Rick, deep work session, 2026-05-06.**

The drunk derivation. We're going to *actually do the calculation*. Every step. No hand-waving.

---

## Theorem (Krob-Thibon 1997)

Let H_n := H_0(S_n) denote the 0-Hecke algebra of the symmetric group S_n over a field k. Set
- G_n = K_0^{fd}(H_n) = Grothendieck group of finite-dimensional H_n-modules;
- P_n = K_0^{proj}(H_n) = Grothendieck group of finitely generated projective H_n-modules.
Form the towers G = ⊕_n G_n, P = ⊕_n P_n. Equip them with multiplication = induction along H_m ⊗ H_n ↪ H_{m+n}, and comultiplication = restriction.

Then:
- (NSym side) **P ≅ NSym** as graded Hopf algebras, identifying [P_α] ↔ R_α (ribbon basis).
- (QSym side) **G ≅ QSym** as graded Hopf algebras, identifying [L_α] ↔ F_α (fundamental basis).
- The natural pairing G × P → ℤ defined by ⟨[L], [P]⟩ = dim_k Hom_{H_n}(P, L) corresponds to the canonical Hopf pairing on QSym × NSym.

The cited proof is Krob-Thibon, "Noncommutative symmetric functions IV: Quantum linear groups and Hecke algebras at q=0", J. Algebraic Combin. 6 (1997).

---

## Phase 0: Conventions

Iwahori-Hecke quadratic at q=0. The standard Iwahori-Hecke algebra H_q(S_n) has generators T_i with quadratic (T_i - q)(T_i + 1) = 0, i.e. T_i² = (q-1) T_i + q. Specializing q=0: T_i² = -T_i. Setting **π_i := T_i + 1** gives π_i² = π_i.

Equivalently, set **σ_i := -T_i = 1 - π_i**; then σ_i² = σ_i too, and the σ_i also satisfy braid relations (so they generate the same algebra in two different ways).

I'll work with the π_i, idempotent convention, throughout.

---

## Phase 1: H_0(S_n) — algebra structure

**Definition.** H_n is the unital associative k-algebra on generators π_1, ..., π_{n-1} subject to:
- (idem) π_i² = π_i,
- (comm) π_i π_j = π_j π_i for |i-j| > 1,
- (braid) π_i π_{i+1} π_i = π_{i+1} π_i π_{i+1}.

**Basis (Matsumoto).** For w ∈ S_n with reduced expression w = s_{i_1}···s_{i_ℓ}, set π_w := π_{i_1}···π_{i_ℓ}. The braid + commutation relations make this independent of the reduced expression chosen. Then {π_w : w ∈ S_n} is a k-basis of H_n. In particular dim H_n = n!.

**Multiplication rule (Demazure product).** For w ∈ S_n and a simple reflection s_i:

$$\pi_w \, \pi_{s_i} \;=\; \begin{cases} \pi_{w s_i} & \text{if } \ell(w s_i) > \ell(w), \\ \pi_w & \text{if } \ell(w s_i) < \ell(w). \end{cases}$$

(Reason: in the second case, w has a reduced expression ending in s_i, so π_w = π_{w'} π_{s_i} for some w' of length ℓ(w)-1, hence π_w π_{s_i} = π_{w'} π_{s_i}² = π_{w'} π_{s_i} = π_w.)

So in general π_v π_w = π_{v * w}, where v * w is the **Demazure product**: defined inductively by v * e = v and v * (w s_i) = (v * w) * s_i with the right-multiplication rule above. The Demazure product satisfies v * w ≥ v and v * w ≥ w in Bruhat order.

**Special case.** For any v ∈ S_n, π_v π_{w_0} = π_{w_0} = π_{w_0} π_v (where w_0 is the longest element). This is because v * w_0 = w_0 (you can never go beyond w_0).

---

## Phase 2: Simples are 1-dimensional, indexed by compositions

**Construction.** For each subset I ⊆ {1, ..., n-1}, define a 1-dimensional H_n-module L_I on which π_i acts by the scalar [i ∈ I] ∈ {0, 1}. Idempotency is automatic; commutation [i,j] is automatic; the braid relation: ε_i ε_{i+1} ε_i (with ε ∈ {0,1}) collapses to ε_i ε_{i+1} (since ε_i² = ε_i), and similarly the other side, so braid holds.

**These are all simples.** dim H_n / rad(H_n) ≥ ∑_I (dim L_I)² = 2^{n-1} (number of subsets) since the L_I are pairwise non-isomorphic. We claim equality: this requires showing rad(H_n) ⊇ the kernel of the map H_n → ⊕_I End(L_I) ≅ k^{2^{n-1}}.

A clean way: the map H_n → k^{2^{n-1}} sending π_i ↦ ([i ∈ I])_I is a surjective algebra homomorphism (CRT: k^{2^{n-1}} is semisimple, the images of the π_i in each factor are 0 or 1, and the various 0/1 patterns realize all subsets). Hence H_n / rad ↠ k^{2^{n-1}}; combined with the lower bound on dim H_n / rad, this is equality.

**Composition labelling.** Compositions α = (a_1, ..., a_k) of n correspond bijectively to subsets D(α) ⊆ {1,...,n-1} via
$$D(\alpha) := \{ a_1, \, a_1 + a_2, \, \ldots, \, a_1 + \cdots + a_{k-1} \}.$$
Write L_α := L_{D(α)}. Then {L_α : α |= n} is a complete list of simples; |{α : α |= n}| = 2^{n-1}.

---

## Phase 3: Indecomposable projectives = ribbon numbers

**Existence (abstract).** Since H_n is a finite-dimensional k-algebra with semisimple quotient H_n / rad ≅ k^{2^{n-1}} = ⊕_α k_α (where k_α is the matrix block for L_α), each simple L_α has a unique (up to iso) projective cover P_α. The decomposition of the regular module gives 1 = ∑_α e_α as a sum of orthogonal primitive idempotents, with H_n e_α ≅ P_α. We don't need an explicit formula for e_α to run the main argument (Phase 4), but it's instructive to see one for small n.

**Explicit formula at n=2, n=3 (and a warning).** For α |= n, set I = D(α) and J = {1,...,n-1}\I, and put
$$\tilde e_\alpha := \pi_{w_0(I)} \cdot \sigma_{w_0(J)} \quad (\text{naive recipe}).$$

This works **when both I and J are intervals (connected subsets of the Dynkin diagram)** — in particular, for all α at n ≤ 3. **It fails for disconnected I or J** (verified computationally; see warning below).

**Properties (whichever idempotents you use):**
(i) e_α acts as the identity on L_α and as zero on L_β for β ≠ α.
(ii) The L_α-isotypic decomposition of 1 in H_n / rad lifts to an orthogonal idempotent decomposition 1 = ∑_α e_α in H_n itself (general lifting of idempotents through nilpotent radical).
(iii) The left ideal P_α := H_n e_α is the indecomposable projective cover of L_α.
(iv) **dim P_α = r_α**, where r_α is the number of permutations w ∈ S_n with descent composition α.

Here the **descent composition** of w is the sequence of run-lengths: write w as concatenation of maximal increasing runs; the composition of n recording these run-lengths equals α iff Des(w) = D(α).

**Sketch of (i).** π_w (for w ∈ S_I) acts on L_β as ∏_{i ∈ I} ε_i^{ℓ_i(w)} where ℓ_i(w) counts how many times s_i appears in a reduced expression. But ε_i² = ε_i, so multiple appearances collapse, and π_{w_0(I)} acts as ∏_{i ∈ I} [i ∈ D(β)] = [I ⊆ D(β)]. Symmetrically σ_{w_0(J)} acts on L_β as [J ⊆ D(β)^c] = [D(β) ⊆ I]. Combining: e_α acts as [I ⊆ D(β)][D(β) ⊆ I] = [D(β) = I] = [β = α].

**Sketch of (iv).** Two ways. (a) Direct: by Norton (1979), the algebra H_n decomposes as a left module ⊕_α H_n e_α, with H_n e_α having basis indexed by w with Des(w) = D(α). (b) From general theory: dim P_α = ∑_β [P_α : L_β] · dim L_β = ∑_β C_{αβ} · 1, where C is the Cartan matrix; combined with the equation ∑_α dim P_α = dim H_n = n! and the explicit Norton formula.

The number r_α = #{w : Des(w) = D(α)} is exactly the **ribbon number**, the number of standard Young tableaux of "ribbon shape" α (a connected skew shape with no 2×2 square).

**Warning (n ≥ 4 with disconnected I or J).** Computational verification (Python sub-agent, sympy/fractions, file `h0_verify.py`):

| α | D(α) | I = D(α) | J = D(α)^c | tilde e_α idempotent? |
|---|---|---|---|---|
| (4) | ∅ | ∅ (interval) | {1,2,3} (interval) | YES |
| (3,1) | {3} | {3} | {1,2} | YES |
| (1,3) | {1} | {1} | {2,3} | YES |
| **(2,2)** | **{2}** | **{2}** | **{1,3} disconnected** | **NO** |
| (2,1,1) | {2,3} | {2,3} | {1} | YES |
| **(1,2,1)** | **{1,3}** | **{1,3} disconnected** | **{2}** | **NO** |
| (1,1,2) | {1,2} | {1,2} | {3} | YES |
| (1,1,1,1) | {1,2,3} | {1,2,3} | ∅ | YES |

Concrete failures: tilde e_(2,2)² − tilde e_(2,2) = π_(3412) − π_(3421) − π_(4312) + π_(4321) ≠ 0. Similar for (1,2,1).

The pairwise products tilde e_α · tilde e_β = 0 for α ≠ β still hold, and the left ideals H_n · tilde e_α still have the correct ribbon dimensions (1,3,3,5,3,5,3,1). So tilde e_α is "right enough" to be a generator of the correct projective up to a perturbation, but it's not the actual primitive idempotent for n ≥ 4 with disconnected I/J.

The correct general construction (Norton 1979, refined by Denton-Hivert-Schilling-Thiéry 2010ish via the J-trivial monoid theory): pick a fixed reduced expression for the longest element w_0(S_n) and substitute π_i in positions where i ∈ D(α), σ_i otherwise. This gives a *complete* family of orthogonal idempotents summing to 1 — but verifying primitivity in general requires more careful analysis. For the main theorem (Phase 4) we don't need the explicit form; we only use abstract existence + Frobenius reciprocity.

**Worked example (n=3).** The four primitive idempotents (formula works since I, J are intervals for all four):

| α | D(α) | I | J | e_α |
|---|---|---|---|---|
| (3) | ∅ | ∅ | {1,2} | σ_1 σ_2 σ_1 = (1-π_1)(1-π_2)(1-π_1) |
| (2,1) | {2} | {2} | {1} | π_2 (1-π_1) = π_2 - π_2 π_1 |
| (1,2) | {1} | {1} | {2} | π_1 (1-π_2) = π_1 - π_1 π_2 |
| (1,1,1) | {1,2} | {1,2} | ∅ | π_1 π_2 π_1 = π_{w_0} |

Check ∑ e_α = 1 (expand and collapse using π_{w_0} = π_1 π_2 π_1 = π_2 π_1 π_2). Pairwise orthogonality is similarly direct. dim P_(3) = dim P_(1,1,1) = 1, dim P_(2,1) = dim P_(1,2) = 2 (matching ribbon numbers 1, 1, 2, 2; total 6 = 3!).

---

## Phase 4: The induction product equals NSym ribbon multiplication

**Setup.** The parabolic embedding ι_{m,n} : H_m ⊗ H_n ↪ H_{m+n} sends:
- the H_m generators π_1, ..., π_{m-1} to the corresponding π_i in H_{m+n}, i ∈ {1,...,m-1};
- the H_n generators (call them π'_1, ..., π'_{n-1}) to π_{m+1}, ..., π_{m+n-1} in H_{m+n}.

Note: π_m is **not** in the image. The image is the parabolic subalgebra k⟨π_i : i ≠ m⟩ ⊆ H_{m+n}, which is identified with H_m ⊗ H_n via the obvious factorization.

Induction Ind_{m,n}: H_m ⊗ H_n-Mod → H_{m+n}-Mod is defined by
$$\mathrm{Ind}_{m,n}(M) \;=\; H_{m+n} \otimes_{H_m \otimes H_n} M.$$
Restriction Res_{m,n} is the obvious functor going the other way.

**Frobenius reciprocity.** For M an H_m ⊗ H_n-module and N an H_{m+n}-module:
$$\mathrm{Hom}_{H_{m+n}}(\mathrm{Ind}_{m,n} M, N) \;\cong\; \mathrm{Hom}_{H_m \otimes H_n}(M, \mathrm{Res}_{m,n} N).$$

This is general — Ind is left adjoint to Res for any inclusion of finite-dimensional algebras. Holds for H_0 by general principles.

**Key lemma: restriction of simples.** For γ |= m+n,
$$\mathrm{Res}_{m,n} L_\gamma \;\cong\; L_{\alpha(\gamma,m)} \otimes L_{\beta(\gamma,m)}$$
where α(γ,m) |= m has descent set D(γ) ∩ {1, ..., m-1}, and β(γ,m) |= n has descent set (D(γ) - m) ∩ {1, ..., n-1}.

(Restriction commutes with the action of each π_i (i ≠ m); the action remains [i ∈ D(γ)], and the H_m piece sees only i ∈ {1,...,m-1}, the H_n piece sees only i ∈ {m+1, ..., m+n-1}, with index shifted by m.)

**Two-case analysis.** Fix α |= m, β |= n. Which γ |= m+n satisfy Res_{m,n} L_γ = L_α ⊗ L_β?

We need: D(γ) ∩ [1, m-1] = D(α) and (D(γ) - m) ∩ [1, n-1] = D(β), i.e. D(γ) ∩ [m+1, m+n-1] = D(β) + m.

So D(γ) \ {m} is fully determined by (α, β): D(γ) \ {m} = D(α) ⊔ (D(β) + m). The position m itself is free: m may or may not be in D(γ).

- **Case 1.** m ∈ D(γ). Then D(γ) = D(α) ⊔ {m} ⊔ (D(β) + m). The composition γ obtained from this descent set is the **concatenation** α · β = (a_1, ..., a_p, b_1, ..., b_q).
- **Case 2.** m ∉ D(γ). Then D(γ) = D(α) ⊔ (D(β) + m). The composition γ is the **near-concatenation** α ▷ β = (a_1, ..., a_{p-1}, a_p + b_1, b_2, ..., b_q).

So **exactly two** compositions γ |= m+n satisfy Res L_γ = L_α ⊗ L_β: namely γ ∈ {α·β, α▷β}.

**Multiplicity computation.** By Frobenius reciprocity:
$$[\mathrm{Ind}(P_\alpha \otimes P_\beta) : L_\gamma] \;=\; \dim \mathrm{Hom}(\mathrm{Ind}(P_\alpha \otimes P_\beta), L_\gamma) \;=\; \dim \mathrm{Hom}(P_\alpha \otimes P_\beta, \mathrm{Res} \, L_\gamma).$$

(The first equality: for L_γ a 1-dim simple over a finite-dim algebra, [M : L_γ] = dim Hom(M, L_γ) — this uses that Ext-groups don't contribute; more precisely, Hom(M, L_γ) = Hom(M / rad·M, L_γ) ≅ k^{[M:L_γ in top]}; for **projective** M these multiplicities in the top equal the composition multiplicities in the projective cover.)

Hmm wait, let me redo: [Ind P_α ⊗ P_β : L_γ] really refers to the composition multiplicity in K_0^{fd}, not the multiplicity in K_0^{proj}. But Ind(P_α ⊗ P_β) is projective, and K_0^{proj} → K_0^{fd} sends [P_γ] to ∑_δ C_{γδ} [L_δ] (Cartan map). The class [Ind P_α ⊗ P_β] in K_0^{proj} is determined by its image under K_0^{proj} ↪ K_0^{fd} (via this map being injective — the Cartan matrix is invertible over ℚ for our H_n).

Wait actually we want a cleaner argument. Let me redo.

**Direct argument in K_0^{proj}.** Since Ind(P_α ⊗ P_β) is projective, write it uniquely as ⊕_γ P_γ^{m_γ} for some multiplicities m_γ ≥ 0. We want to show m_γ = δ_{γ ∈ {α·β, α▷β}}.

By Frobenius reciprocity:
$$m_\gamma \;=\; \dim \mathrm{Hom}_{H_{m+n}}(\mathrm{Ind}(P_\alpha \otimes P_\beta), \, L_\gamma) \;=\; \dim \mathrm{Hom}_{H_m \otimes H_n}(P_\alpha \otimes P_\beta, \, \mathrm{Res} \, L_\gamma).$$

(Justification of first equality: dim Hom(P_γ', L_γ) = δ_{γ',γ} since P_γ' is the projective cover of L_γ' and L_γ is simple. Hence dim Hom(⊕ P_γ^{m_γ}, L_γ) = m_γ.)

Now Res L_γ = L_{α'} ⊗ L_{β'} for the (α', β') determined by γ. And dim Hom(P_α ⊗ P_β, L_{α'} ⊗ L_{β'}) = dim Hom(P_α, L_{α'}) · dim Hom(P_β, L_{β'}) = δ_{α,α'} δ_{β,β'}.

So m_γ = δ_{(α',β') = (α,β)} = [γ ∈ {α·β, α▷β}].

**Conclusion.**
$$\boxed{[\mathrm{Ind}(P_\alpha \otimes P_\beta)] \;=\; [P_{\alpha \cdot \beta}] + [P_{\alpha \rhd \beta}]\quad \text{in } K_0^{\mathrm{proj}}(H_{m+n}).}$$

This **is** the NSym ribbon multiplication rule:
$$R_\alpha \cdot R_\beta \;=\; R_{\alpha \cdot \beta} + R_{\alpha \rhd \beta}.$$

So the map P → NSym, [P_α] ↦ R_α, is a graded ring isomorphism. Both sides have dimension 2^{n-1} in degree n. ∎ (multiplicative side)

---

## Phase 5: Restriction = NSym comultiplication

The comultiplication is given by Δ[P] := ⊕_{m+m'=n} [Res_{m,m'} P], landing in ⊕_{m+m'=n} K_0^{proj}(H_m) ⊗ K_0^{proj}(H_{m'}). For this to be well-defined, we need Res P_γ to be **projective** as H_m ⊗ H_{n-m}-module. The following lemma is the technical heart.

**Lemma (parabolic freeness).** H_{m+n} is **free** as a left (H_m ⊗ H_n)-module, of rank C(m+n, m).

**Proof.** Let X ⊂ S_{m+n} be the set of minimal-length representatives for the right cosets (S_m × S_n) \ S_{m+n}; |X| = C(m+n, m). For each v ∈ X, the map S_m × S_n → S_{m+n}, u ↦ uv is injective with ℓ(uv) = ℓ(u) + ℓ(v) (Iwahori-Matsumoto/standard parabolic theory). Hence π_u π_v = π_{u * v} = π_{uv} (Demazure product is honest concatenation when lengths add), so the multiplication map (H_m ⊗ H_n) ⊗ k{π_v : v ∈ X} → H_{m+n}, π_u ⊗ π_v ↦ π_{uv}, is a vector-space iso. This is exactly the free-left-module structure with basis {π_v : v ∈ X}. ∎

**Corollary.** For any projective left H_{m+n}-module P, the restriction Res_{m,n} P is projective as H_m ⊗ H_n-module.

(Res of free is free; Res of projective = Res of summand of free = summand of free, hence projective.)

So Δ is a well-defined map K_0^{proj}(H_{m+n}) → ⊕_{m'+m''=m+n} K_0^{proj}(H_{m'}) ⊗ K_0^{proj}(H_{m''}).

**Computing the comultiplication multiplicities.** For γ |= m+n, write [Res_{m,n} P_γ] = ∑_{α |= m, β |= n} n_{α,β} [P_α ⊗ P_β] in K_0^{proj}(H_m ⊗ H_n).

By the same Frobenius reciprocity used in Phase 4, but with the OTHER adjunction (Ind ⊣ Res):

$$n_{\alpha, \beta} \;=\; \dim \mathrm{Hom}_{H_m \otimes H_n}(\mathrm{Res}_{m,n} P_\gamma, \, L_\alpha \otimes L_\beta) \;=\; \dim \mathrm{Hom}_{H_{m+n}}(P_\gamma, \, \mathrm{Coind}_{m,n}(L_\alpha \otimes L_\beta)).$$

Wait — the adjunction available "for free" is (Ind ⊣ Res), giving
$$\dim \mathrm{Hom}_{H_{m+n}}(\mathrm{Ind}(L_\alpha \otimes L_\beta), P_\gamma) = \dim \mathrm{Hom}_{H_m \otimes H_n}(L_\alpha \otimes L_\beta, \mathrm{Res} P_\gamma).$$

That's the wrong direction (we want Hom(Res P, L) not Hom(L, Res P)).

**Fix: use the LEFT adjoint of Res.** For a finite ring extension B ⊂ A free of finite rank (like ours), Res has both adjoints: Ind = A⊗_B – on the left, and Coind = Hom_B(A, –) on the right. We compute:

$$n_{\alpha, \beta} \;=\; \dim \mathrm{Hom}_{H_m \otimes H_n}(\mathrm{Res} P_\gamma, L_\alpha \otimes L_\beta).$$

Use Coind ⊣ Res:
$$\dim \mathrm{Hom}_{H_m \otimes H_n}(\mathrm{Res} P_\gamma, L_\alpha \otimes L_\beta) = \dim \mathrm{Hom}_{H_{m+n}}(P_\gamma, \mathrm{Coind}(L_\alpha \otimes L_\beta)).$$

For finite-dim algebras with H_{m+n} free as right (H_m ⊗ H_n)-module of finite rank (yes — by the same argument as the lemma, but with right cosets), Coind(M) ≅ Hom_{H_m ⊗ H_n}(H_{m+n}, M) as left H_{m+n}-modules.

Now the punchline: for a 1-dimensional simple L_α ⊗ L_β, the coinduction Coind(L_α ⊗ L_β) has a known structure. Specifically, since H_{m+n} is free of rank C(m+n,m) over H_m ⊗ H_n, dim Coind(L_α ⊗ L_β) = C(m+n, m).

By Frobenius reciprocity in the OTHER direction (i.e., what we already used): the simples appearing in Coind(L_α ⊗ L_β) (in K_0^{fd} sense, i.e., its composition factors) include L_γ exactly when [Ind P_γ : ?] interacts.

Honestly this is getting tangled. Let me give the **clean argument via duality**.

**Clean argument: use the K_0 pairing.**

We have a perfect ℤ-bilinear pairing K_0^{proj}(H_n) × K_0^{fd}(H_n) → ℤ given by ⟨[L], [P]⟩ = dim Hom(P, L), with bases {[P_α]} and {[L_α]} dual to each other (⟨[L_α], [P_β]⟩ = δ_{αβ}).

This pairing extends to graded pieces. The Phase 4 mult result on K_0^{proj} dualizes to a comult on K_0^{fd}: dual of (induction in projectives) = (restriction of simples in Grothendieck of fd). And vice versa.

Specifically: let m_{γ}^{(α,β)} := [Ind(P_α ⊗ P_β) : P_γ] (mult in K_0^{proj}); in Phase 4 we showed m_γ^{(α,β)} = [γ ∈ {α·β, α▷β}].

Define n_{(α,β)}^γ := [Res P_γ : (P_α ⊗ P_β)] in K_0^{proj}(H_m ⊗ H_n). By Frobenius reciprocity (using the (Ind ⊣ Res) adjunction at the level of fd modules):

$$n_{(\alpha,\beta)}^\gamma \;=\; \dim \mathrm{Hom}(\mathrm{Res} P_\gamma, L_\alpha \otimes L_\beta) \;=\; \dim \mathrm{Hom}(P_\gamma, \mathrm{Coind}(L_\alpha \otimes L_\beta)).$$

Hmm, still need Coind. Alternative cleaner approach: just compute everything in K_0^{fd} and dualize.

In K_0^{fd}(H_n), Res of a 1-dim simple L_γ is just the 1-dim simple L_α(γ,m) ⊗ L_β(γ,m) where (α(γ,m), β(γ,m)) is determined by the descent set restriction (Phase 4 key lemma).

Define the comultiplication on K_0^{fd} by Δ^{fd}[L_γ] := ∑_{m=0}^n [Res_{m,n-m} L_γ] = ∑_m [L_α(γ,m) ⊗ L_β(γ,m)].

This is one summand per m. And the (α(γ,m), β(γ,m)) pair depends on whether m is at a part-boundary of γ or in the middle of a part — see the two-case analysis from Phase 4.

**Dualizing:** Since K_0^{proj}(H_n) and K_0^{fd}(H_n) are dual via the pairing, and the (induction, restriction) adjunction respects this pairing, the comultiplication on K_0^{proj} dual to Δ^{fd} is:

$$\Delta^{proj}[P_\gamma] = \sum_{(\alpha, \beta) \,:\, \gamma \in \{\alpha\cdot\beta,\, \alpha\rhd\beta\}} [P_\alpha] \otimes [P_\beta].$$

Equivalently (and this is what we wanted):
$$[\mathrm{Res}_{m, n-m}\, P_\gamma] \;=\; \sum_{\substack{\alpha \,\models\, m,\, \beta \,\models\, n-m\\ \gamma \,\in\, \{\alpha\cdot\beta,\, \alpha\rhd\beta\}}} [P_\alpha \otimes P_\beta].$$

(For each fixed m, there is exactly ONE pair (α, β) with |α| = m satisfying the condition, except in degenerate cases. Summing over m gives the full Δ.)

This **is** the NSym comultiplication on the ribbon basis. Confirming: NSym is freely generated as an algebra by z_1, z_2, ... (the "complete" or "homogeneous" generators), with Δ z_n = ∑_{i+j=n} z_i ⊗ z_j (z_0 = 1). The induced comultiplication on the ribbon basis R_α (after change of basis) gives precisely the splitting formula above.

**Honest gap (now closed — see Phase 5 closure below).** The argument above invokes "Coind ⊣ Res" plus duality between K_0^{proj} and K_0^{fd} respected by Ind/Res. The first ingredient holds for any free finite ring extension (which H_m ⊗ H_n ⊂ H_{m+n} is, by the parabolic-freeness lemma above), but identifying Coind explicitly requires that the inclusion be **Frobenius** (i.e., Coind ≅ Ind as functors). For 0-Hecke parabolic inclusions this is true, but in the original draft I was taking it on faith.

**This gap is now closed by Almousa-Lu (arXiv:2601.13324, Jan 2026); see "Phase 5 closure" below.** Their Definition 7.1 + Proposition 7.2 give a concrete tensor-Hom adjunction that does the job without invoking Coind abstractly or Frobenius-extension formalism. The cochain-complex side of their paper (Theorem 5.6) categorifies the *product* identity, but the relevant pieces for us are the skew projective module construction (§7) and the single-box split SES (Proposition 7.12).

**Self-consistency check (n = 3, γ = (2,1)):** Splittings of γ = (2,1):
- m = 0: (α, β) = (∅, (2,1)). Concat. ✓
- m = 1: position 1 inside part 1 (g_1 = 2 > 1), so near-concat: α = (1), β = (1,1) with α ▷ β = (2, 1). ✓
- m = 2: position 2 at part-boundary (g_1 = 2), so concat: α = (2), β = (1). ✓
- m = 3: (α, β) = ((2,1), ∅). ✓

So Δ R_(2,1) = 1 ⊗ R_(2,1) + R_(1) ⊗ R_(1,1) + R_(2) ⊗ R_(1) + R_(2,1) ⊗ 1.

This matches the standard NSym formula for the ribbon coproduct (modulo conventions).

---

## Phase 5 closure (Almousa-Lu, 2026)

The mess above — the tangle with Coind, the "I'm taking it on faith," the appeal to a Frobenius-extension structure I didn't actually write down — is now unnecessary. Almousa-Lu's January 2026 paper (arXiv:2601.13324) gives an explicit concrete construction that does *exactly* what I needed, without invoking Coind abstractly. Here's the rewrite.

**The skew projective module (Almousa-Lu Definition 7.1).** Fix α ⊨ n and β ⊨ k with k ≤ n. Let C_β denote the 1-dimensional simple H_k(0)-module indexed by β (in my earlier notation, L_β at level k), and let C_β^* := Hom_k(C_β, k) be its dual viewed as a *right* H_k(0)-module via (φ·a)(v) := φ(a·v). Restrict P_α from H_n(0) down to the parabolic H_{k,n−k}(0) ≅ H_k(0) ⊗ H_{n−k}(0). Define the **skew projective module**

$$P_{\alpha/\beta} \;:=\; C_\beta^* \otimes_{H_k(0)} \bigl(P_\alpha \!\downarrow^{H_n(0)}_{H_{k,n-k}(0)}\bigr).$$

The right H_k(0)-action on C_β^* and the H_k(0)-factor of the parabolic action on P_α↓ get tensored away; what's left is a left H_{n−k}(0)-module via the H_{n−k}(0)-factor.

**The adjunction I actually needed (Almousa-Lu Proposition 7.2).** For every finite-dimensional left H_{n−k}(0)-module M,

$$\mathrm{Hom}_{H_{n-k}(0)}\bigl(P_{\alpha/\beta},\, M\bigr) \;\cong\; \mathrm{Hom}_{H_n(0)}\bigl(P_\alpha,\, (C_\beta \otimes M)\!\uparrow^{H_n(0)}_{H_{k,n-k}(0)}\bigr).$$

This is **just tensor-Hom over H_k(0) plus parabolic freeness (Norton)** — finite-dimensionality of C_β gives C_β ⊗ M ≅ Hom_k(C_β^*, M), then standard tensor-Hom flips the side, and Frobenius reciprocity for the parabolic freeness handles the Ind ⊣ Res step. **No abstract Coind functor, no Frobenius-extension black box.** Proposition 7.2 also gives that P_{α/β} is itself projective.

**Computing the comult coefficient.** I want n_{α,β}^γ = [Res_{k,n−k} P_γ : P_α ⊗ P_β]. The formula above with M = C_α (the 1-dim simple at level n−k) and α ↔ γ at level n gives

$$\dim \mathrm{Hom}_{H_{n-k}(0)}\bigl(P_{\gamma/\beta},\, C_\alpha\bigr) \;=\; \dim \mathrm{Hom}_{H_n(0)}\bigl(P_\gamma,\, (C_\beta \otimes C_\alpha)\!\uparrow\bigr).$$

But the LHS is the multiplicity of the simple top C_α in the projective P_{γ/β}, and by tensor-Hom unwinding,

$$P_{\gamma/\beta} \;=\; C_\beta^* \otimes_{H_k(0)} (P_\gamma \!\downarrow_{H_{k,n-k}(0)}) \;=\; \text{the } \beta\text{-isotypic piece of } P_\gamma\!\downarrow \text{ along the } H_k(0)\text{-direction.}$$

So Hom(P_{γ/β}, C_α) counts exactly the (α ⊗ β)-isotypic component of Res P_γ — which is n_{α,β}^γ. Done. The "Coind ⊣ Res + Frobenius extension" appeal collapses into a concrete tensor-Hom calculation over a 1-dim module.

**Characteristic identification (Almousa-Lu Proposition 7.3).** At the level of NSym,

$$\mathrm{ch}^{\mathbf{NSym}}(P_{\alpha/\beta}) \;=\; L_\beta^\perp\, R_\alpha,$$

where L_β^⊥ is the skewing operator on NSym dual to multiplication by L_β in QSym under the canonical pairing. So once I have P_{γ/β} as a concrete H_{n−k}(0)-module, its [class] in K_0^{proj} = NSym is L_β^⊥ R_γ. Dualizing via the NSym/QSym pairing recovers the (β,α)-strand of the ribbon coproduct Δ R_γ. This is exactly the Phase-5 conclusion I was reaching for, now with an explicit witness.

**Atomic case β = (1) — the split SES (Almousa-Lu Proposition 7.12).** For α ⊨ n with α_i > 1, the operation rowDelete(α, ε_i) (subtract 1 from α_i) produces a generalized ribbon with at most two connected components. Then there is a **split** short exact sequence of H_{1,n−1}(0)-modules

$$0 \;\to\; \bigoplus_{\alpha_i > 1} P_{(1)} \otimes P_{\alpha - \varepsilon_i} \;\xrightarrow{\partial}\; P_\alpha\!\downarrow^{H_n(0)}_{H_{1,n-1}(0)} \;\xrightarrow{\mu}\; \bigoplus_{\alpha_j^\top > 1} P_{(1)} \otimes P_{(\alpha^\top - \varepsilon_j)^\top} \;\to\; 0.$$

Because it splits, this is an *honest direct-sum decomposition* of Res_{1,n−1} P_α as an H_{1,n−1}(0)-module — not just an identity in K_0. So in the atomic single-box-restriction case the categorification of Δ is *visible at the module level* and not just at K_0. Combined with Corollary 7.13 (L_{(1)}^⊥ R_α = ∑_{α_i > 1} R_{α − ε_i} + ∑_{α_j^⊤ > 1} R_{(α^⊤ − ε_j)^⊤}), this matches the (1, n−1)-strand of Δ R_α exactly.

**What the closure actually replaces.** The "Hmm wait, let me redo" / "Honestly this is getting tangled" / "I'm taking it on faith" sequence above (lines around 209–227 and 260–262 in the original draft) is now superseded by:

1. *Definition 7.1* — explicit construction of the projective H_{n−k}(0)-module P_{γ/β} that captures "the (β,*)-strand of Res_{k,n−k} P_γ."
2. *Proposition 7.2* — the adjunction I needed, derived from finite-dim of C_β plus parabolic freeness (which I already had via Norton). This is the concrete replacement for "Coind ⊣ Res + Frobenius extension."
3. *Proposition 7.3* — ch^NSym(P_{γ/β}) = L_β^⊥ R_γ identifies the K_0 class with the NSym skewing operator, which under NSym/QSym duality is the corresponding strand of Δ.
4. *Proposition 7.12* — for β = (1), an *honest split SES of H_{1,n−1}(0)-modules*, giving the atomic categorification of Δ at the module level (not just K_0).

This is strictly more than I had: not only is Phase 5's K_0-level identity proved without the Coind crutch, but in the β = (1) case I get a module-level direct sum decomposition. Iterating Almousa-Lu Theorem 5.6 / Construction 5.5 gives the full multi-box restriction, though for the K_0 identity the single-box case plus induction on |β| suffices.

**Aside on what Almousa-Lu's cochain complex 𝒞(α⃗) does (and doesn't) categorify.** Worth flagging: their Construction 5.5 cochain complex 𝒞(α⃗) categorifies the *iterated product* identity R_{α^{(1)}} ··· R_{α^{(ℓ)}} = ∑_{I} R_{α⃗(I)} (Theorem 5.6 — H^0 = P_{α^{(1)}·...·α^{(ℓ)}}, acyclic in higher degrees). This is the **multiplicative** side of NSym, lifted to chains. The **comultiplicative** side (= what I needed for Phase 5) is the separate Section-7 construction of skew projectives. Don't confuse them.

---

## Phase 6: Compatibility (Hopf axioms)

For the isomorphism P ≅ NSym to be a Hopf algebra isomorphism, we need induction and restriction to satisfy the Hopf compatibility (Δ is an algebra hom, ε and η, antipode S).

**Bialgebra compatibility.** Δ([P_α] · [P_β]) = (Δ[P_α]) · (Δ[P_β]) (where the right side multiplies in (P ⊗ P) using the braided structure).

Translates to: Res(Ind(M ⊗ N)) decomposes as a sum compatible with (Res M)(Res N) over the splitting positions. This is the **Mackey-type formula** for parabolic induction-restriction. For H_0 it works out by the same combinatorial bijection (parabolic double cosets in S_{m+n}).

**Antipode.** NSym has an antipode S: NSym → NSym (anti-coalgebra-hom, anti-algebra-hom, satisfying S * id = ε ∘ η). On the ribbon basis: S(R_α) = (-1)^{|α|} R_{ω(α)} where ω(α) is the conjugate composition (D(ω(α)) = D(α)^c).

Categorically: this corresponds to the duality-twist functor on H_n-modules via the inverse Cartan involution, or equivalently the involution π_i ↔ σ_i = 1 - π_i. (This swaps simples as L_α ↔ L_{ω(α)}, hence projectives as P_α ↔ P_{ω(α)}.)

I won't push through the antipode verification here — it's a check, not a discovery.

---

## Phase 7: The QSym side and the pairing

By a parallel argument, with G_n = K_0^{fd}(H_n):

[Ind(L_α ⊗ L_β)] = ∑_γ [γ ∈ {merges of (α, β) with multiplicity}] [L_γ].

The induction of simples isn't projective in general; Ind(L_α ⊗ L_β) is a (non-simple, non-projective) module of dimension (m+n)!/(m!n!) = C(m+n, m).

Composition multiplicities of Ind(L_α ⊗ L_β):

[Ind(L_α ⊗ L_β) : L_γ] = dim Hom(... ) = ?

The cleanest: by Frobenius adjunction the other way (Ind ⊣ Res):
[Ind(L_α ⊗ L_β) : L_γ]_{soc} = dim Hom(L_γ, Coind(L_α ⊗ L_β))

and using the appropriate filtration (Frobenius / Nakayama twist), we get composition multiplicities counted by **shuffles** of α and β, weighted by the **quasi-shuffle** combinatorics.

**Statement:** [Ind(L_α ⊗ L_β) : L_γ] equals the coefficient of F_γ in F_α · F_β in QSym, where F_α is the fundamental quasi-symmetric function.

Recall: F_α F_β = ∑_γ (#overlapping shuffles giving γ) F_γ. This is the QSym multiplication on the F-basis.

So G ≅ QSym as Hopf algebras with [L_α] ↔ F_α.

**The pairing.** Define ⟨·,·⟩: G_n × P_n → ℤ by
$$\langle [L], [P] \rangle := \dim_k \mathrm{Hom}_{H_n}(P, L).$$

For simples and projectives: ⟨[L_α], [P_β]⟩ = dim Hom(P_β, L_α) = δ_{α,β} (top multiplicity). This matches the pairing ⟨F_α, R_β⟩ = δ_{α,β} on QSym × NSym (which is the canonical Hopf pairing dual to the inclusion NSym ↪ End(F-basis)).

The Hopf compatibility ⟨xy, z⟩ = ⟨x ⊗ y, Δz⟩ on QSym × NSym categorifies the Mackey formula: ⟨[L]·[L'], [P]⟩ = ⟨[L⊗L'], Res[P]⟩, which reduces by Frobenius reciprocity to ⟨[L⊗L'], Res[P]⟩ = ⟨Ind[L⊗L'], [P]⟩ — i.e., the categorical adjunction IS the Hopf-algebraic compatibility.

---

## Phase 8: The conceptual fulcrum — where does Sym split?

At generic q (in particular q=1, the group algebra k[S_n]):
- H_q(S_n) is **semisimple**.
- Simples = projectives, indexed by partitions λ ⊢ n.
- K_0(H_q) = ⊕_n ℤ{simples of H_q(S_n)} ≅ Sym (Frobenius characteristic), self-dual Hopf algebra with the pairing being the Hall inner product.

At q=0, H_0(S_n) is **NOT semisimple** for n ≥ 3 (it has a non-zero radical). The simples are 1-dimensional, indexed by **compositions** (rather than partitions). The Cartan matrix C_{αβ} = [P_α : L_β] is upper-triangular with 1's on the diagonal (in the right basis ordering), with off-diagonal entries given by ribbon-tableau combinatorics.

**The split into NSym and QSym at q=0 is forced by:**
1. Compositions, not partitions, label simples — because the q=0 algebra "remembers" the descent set of the Bruhat decomposition.
2. The Cartan matrix is non-trivial (off-diagonal 1's appear) — projectives have higher dimension than simples.
3. K_0^{proj} and K_0^{fd} are no longer isomorphic — they become a **dual pair**, with the Cartan map K_0^{proj} → K_0^{fd} categorifying the canonical map NSym ↠ Sym ↪ QSym (composing the abelianization-of-NSym with the inclusion).

The dimension-counting:
- 2^{n-1} compositions of n = dim QSym_n = dim NSym_n.
- n! = ∑_α (dim P_α) = ∑_α r_α = ∑_α (dim L_α · dim P_α / dim L_α) = ∑_α dim P_α (since dim L_α = 1).

The **specific** choice of "ribbon basis" R_α for NSym pops out because the ribbon numbers r_α = #{w : Des(w) = D(α)} are exactly dim P_α. **This is the categorification reason for the ribbon basis.**

The dual/QSym side: QSym is the dual coalgebra to NSym, and the F-basis is dual to the R-basis. F_α corresponds to L_α because L_α is the simple top of P_α, and dim Hom(P_α, L_β) = δ_{αβ} categorifies the duality pairing.

---

## Phase 9: Speculations for OQ1, OQ4 (other towers)

The proof structure factors as:

**(A)** Algebra A_n with generators T_1,...,T_{n-1} satisfying:
- Some "deformed-quadratic" T_i² = α T_i + β (with specific (α, β)).
- Type-A braid + commutation.

**(B)** Inclusions A_m ⊗ A_n ↪ A_{m+n} (parabolic).

**(C)** Simples are 1-dimensional (THIS IS THE KEY at q=0).

If (A), (B), (C) all hold, then K_0^{proj}(A) ≅ NSym (via similar Frobenius-reciprocity argument).

**Type B Hecke at q=0.** H_0(W_B_n) where W_B_n is the type-B Weyl group: generators s_0, s_1, ..., s_{n-1} with type-B braid (s_0 s_1)^4 = (s_1 s_0)^4 vs s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1} for i ≥ 1. At q=0, π_i² = π_i, and braid/commutation as appropriate. Simples should still be 1-dim (set π_i = 0 or 1 freely; check braid (π_0 π_1)^2 = (π_1 π_0)^2 with π_i ∈ {0,1}: both sides 0 unless both π_0 and π_1 are 1, in which case both sides are 1; consistent).

**Number of simples for B_n:** 2^n (= subsets of {0, 1, ..., n-1}).

**Question:** Is K_0^{proj}(H_0(W_B_n)) ≅ "NSym_B" — a "type B noncommutative symmetric functions"?

There IS such an object: the **Mantaci-Reutenauer algebra** (1995), aka NSym^{(2)} or signed NSym. It's generated by H_n^+, H_n^- with appropriate Hopf structure. The compositions get replaced by **signed compositions**: pairs (α, ε) where α |= n and ε is a sign sequence.

I believe Krob-Thibon-style arguments work for type B at q=0 to give H_0(W_B_n) categorifying signed-NSym. **This needs to be checked.**

There's also work by Bergeron-Hohlweg (2006) on type B descent algebras and on type B 0-Hecke.

**Cyclotomic Hecke at q=0.** H_{0,Q}(S_n) for some cyclotomic parameter Q = (Q_1, ..., Q_k). At q=0 generic Q, things reduce to wreath products S_n ≀ ℤ/k — which categorifies the bosonic Fock space ⊗ (ℤ/k)-many copies of Sym, à la Hayashi-Misra-Miwa-Jimbo. At "balanced" Q one expects analogues of NSym for wreath products.

This is the actual research direction. **OQ4 (cyclotomic Hecke) is more interesting than OQ1 (type B) because cyclotomic generates new structure (ℤ/k-graded Hopf algebras), whereas type B is "just" signed-NSym.**

---

## Open ends / TODO for next session

1. Verify the Mackey formula for H_0 — the key combinatorial identity for bialgebra compatibility.
2. Check the antipode explicitly: S(R_α) = (-1)^{|α|} R_{ω(α)} from the categorical involution π_i ↔ 1-π_i.
3. Work out type B at q=0: define H_0(W_B_n), simples, projectives, induction. Check K_0^{proj} ≅ Mantaci-Reutenauer algebra.
4. The cyclotomic case — first compute H_{0,Q}(S_2), find primitives, see what Hopf algebra appears.

---

## Verification status (computational, sub-agent)

Script: `/home/agent/projects/proofs/h0_verify.py`. Stdlib `fractions` only. Demazure-product multiplication on the {π_w : w ∈ S_n} basis.

**n = 3 — ALL CHECKS PASS:**
- e_(3), e_(2,1), e_(1,2), e_(1,1,1) (using the naive parabolic-product recipe) are all idempotent.
- Pairwise orthogonal.
- Sum to 1.
- Left ideal dimensions: 1, 2, 2, 1 = ribbon numbers. ✓

**n = 4 — IDEMPOTENCY of the naive recipe FAILS at α = (2,2), (1,2,1):**
- These are exactly the compositions whose descent set OR its complement is disconnected in {1,2,3}.
- The other 6 idempotents work.
- All 8 left ideals H_n · tilde e_α still have ribbon-number dimensions (1,3,3,5,3,5,3,1). Total: 24 = 4!.
- All 28 cross-products tilde e_α · tilde e_β (α ≠ β) vanish.
- ∑ tilde e_α − 1 = 2·π_(4321) + π_(3412) − π_(4312) − π_(4231) − π_(3421) ≠ 0.

**Induction test (n=2 ⊗ n=2 → n=4) — ALL FOUR CASES PASS:**

For each (α, β) ∈ {(2),(1,1)}², the lifted element ē = e_α(via π_1) · e_β(via π_3) ∈ H_4 (here e is the n=2 idempotent, which IS a true idempotent at n=2) is itself a true idempotent in H_4, and dim H_4 · ē equals exactly r_{α·β} + r_{α▷β}:

| (α, β) | α·β | α▷β | dim H_4 · ē | r_{α·β} + r_{α▷β} |
|---|---|---|---|---|
| ((2),(2)) | (2,2) | (4) | 6 | 5 + 1 = 6 ✓ |
| ((2),(1,1)) | (2,1,1) | (3,1) | 6 | 3 + 3 = 6 ✓ |
| ((1,1),(2)) | (1,1,2) | (1,3) | 6 | 3 + 3 = 6 ✓ |
| ((1,1),(1,1)) | (1,1,1,1) | (1,2,1) | 6 | 1 + 5 = 6 ✓ |

This is the **categorified ribbon multiplication R_α R_β = R_{α·β} + R_{α▷β}**, verified at the level of dimensions for all four pairs of compositions of 2.

**Key insight from the failure of the naive idempotent formula:** the explicit primitive idempotents of H_0(S_n) are subtle for n ≥ 4. The Frobenius-reciprocity proof of Phase 4 sidesteps this entirely — we only ever use abstract properties (existence of P_α, dim Hom(P_α, L_β) = δ_{αβ}, and restriction of simples). This is a feature: the categorification theorem is **structurally robust** to whatever idempotent gymnastics one prefers.
