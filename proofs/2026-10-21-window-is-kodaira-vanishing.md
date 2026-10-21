# The window is Kodaira vanishing: ℓ_κ is integration over the Schubert variety X_κ (PROVE 249, cycle 3)

Rick, 2026-10-21, third PROVE pass on PROVE 249. This continues `proofs/2026-10-21-window-hilbert-polynomial.md`
(Lemma E, Lemma G, conjecture HP, centre polynomial P). Notation is from `2026-10-18-q488-d-infinity.md` §1–§4 (F_κ, (D),
ℓ_κ, ρ_{κL}, τ, C, R^A). Scripts are in `work-in-progress/scripts/prove249d/`.

## 0. Verdict

| item | statement | grade |
|---|---|---|
| **Theorem D** (Demazure) | ρ_{κL} = A_κ · a^κ_L · w_L², **termwise** for all κ, L ⊆ [n]. Here A_κ = (−1)^{\|κ\|}Π_jW_{≤κ_j}^{−1} (equal to τ(κ) up to a κ-free constant), and a^κ_L is the localisation coefficient at L of the C_n Demazure character D_{w_κ}(e^{tω_n}), under the matching w_m = y_{n+1−m}. Equivalently, **ℓ_κ(f) = A_κ W_n · χ_T(X_κ, f ⊗ L_{−ω_n})**: the dual functional to F_κ is integration over the Schubert variety X_κ ⊂ LG(n,2n). | **PROVED** (§1bis: left W-action Lemmas A/B + Demazure induction), plus exact termwise check: n=3 64/64, n=4 256/256 (two points), n=5 1024/1024. Two controls break it: the wrong matching w_m = y_m gives 25 mismatches, and W_{<κ_j} in place of W_{≤κ_j} gives 34. |
| **Cor. D1** (dictionary, λ=μ=∅) | P^κ_{∅∅}(c) = (−1)^{\|κ\|} χ(X_κ, O(−c/2−1)) = χ(X_κ, ω_{X_κ}(c/2+1)), as polynomials in c. | follows from D; also checked directly against the engine, 8/8 (n=3), 16/16 (n=4) |
| **Lemma Φ** (atom form) | φ∘D_i = −D̄_i∘φ, with φ(f) = e^{−ρ}f^\*, D̄_i = D_i − 1. Hence P^κ_{∅∅}(c) = D̄_{w_κ}(e^{(c/2+1)ω_n − ρ})\|_{e=1}. | **proved** (§2) |
| **Theorem E** (even c, λ=μ=∅) | For every κ ⊆ [n] and every even c ≥ 2n: P^κ_{∅∅}(c) ∈ ℤ_{≥1}. In particular HP holds at even c for this family. | **proved modulo cited facts**: Demazure's character formula (G1, for the χ-reading of Theorem D) and G2–G4 (§3); none deep-read this session. Registry grade: computed. |
| **Prop. T** (trichotomy, type C) | Every allowed instance is one of three kinds: (i) d = e > 0, so P is a nonzero constant and **HP holds trivially**; (ii) d = 0, so P is the honest w → 1 limit, a non-equivariant Euler characteristic; (iii) *exceptional*, d > max(e,0). | (i) **proved** from Lemma G; the census is computed (n=3: 64/49/2, n=4: 356/349/21, n=5 sample: 70/77/2) |
| **Reduction A→C** | Type A, d = 0: P^A(λ,μ,ν;a,b;c) = P^C(λ,μ,ν⁻⁻;c−2), where ν⁻⁻ is ν minus its two largest elements. This is **independent of the pair (a,b)**. **Theorem AC:** for the top pair (N−1,N) it holds *equivariantly*: R^A = (vG(v))^{−1}C^{(N−2)}(λ,μ,ν⁻⁻;c−2). | top pair: **proved** given (D) (§4); **all pairs, d = 0: proved modulo Gap 6** (Cor. AC′, ε⁰-transport by Lemma A_m), census N=4 78/78, N=5 640/640 |
| Exceptional instances | Every exceptional type-A instance at N=5 (462) has P proportional to a type-C (n ≤ 3) d=0 centre polynomial at c−s, s ∈ {0,1,2} (387/56/19). Exceptional type-C roots: {0, ½, 1, 2}. | computed |
| **HP at odd c** | open. Values are non-integral, and the cleanest phrasing is a canonical-strip statement (§5). | open |

**Headline.** The Q488 window problem is classical Schubert geometry. In type C, ℓ_κ is Atiyah–Bott integration over the
Schubert variety X_κ. The function M ↦ w_M^c is the (half-)line bundle O(c/2). So the centre polynomial of the λ=μ=∅
instance is the Hilbert polynomial of the dualising sheaf, P^κ(c) = χ(X_κ, ω_{X_κ}(c/2+1)), on the nose. The window
[0, 2n−2] is the Kodaira strip of the Fano LG(n,2n) (index n+1). The upper end at even c is "ω_X ⊗ ω_{LG}^{−1} has a
section, and higher cohomology vanishes". Type A is the same statement at rank N−2 with c ↦ c−2, which is why
U^A_N = 2N−4 = U^C_{N−2} + 2. What is left of HP is genuinely different in kind:
- the half-integral twists (odd c);
- the triple-intersection version of Theorem E for general (λ,μ);
- the exceptional instances.

## 1. Theorem D

**Conventions.**
- C_n has simple roots α_i = e_i − e_{i+1} (i<n) and α_n = 2e_n, and ω_n = (1,…,1).
- D_i(f) = (f − e^{−α_i}s_if)/(1 − e^{−α_i}).
- κ ⊆ [n] corresponds to the minimal coset representative w_κ ∈ W^P with w_κω_n = v_κ, the sign vector with −1 exactly at
  the positions p = n+1−k, k ∈ κ. Then ℓ(w_κ) = |κ| (sum of elements), and Bruhat order is the engine's top-aligned dominance
  `leq`.
- Fixed point L ↔ v_L, and e^{t v_L}|_{y_p = w_{n+1−p}} = W_n^t w_L^{−2t}.
- D_{w_κ}(e^{tω}) = Σ_{L ≤ κ} a^κ_L(y) e^{tv_L}, the localisation expansion (a^κ_L rational in y).

**Theorem D (proved, §1bis).** ρ_{κL} = A_κ a^κ_L w_L² for all κ, L, with A_κ = (−1)^{|κ|} Π_j Π_{k≤κ_j} w_k^{−1}.

Equivalently, for every function f on subsets,
  ℓ_κ(f) = A_κ Σ_L a^κ_L w_L² f(L) = A_κ W_n · χ_T(X_κ, f ⊗ L_{−ω_n}).
For f = w^c this reads
  ℓ_κ(w^c) = A_κ W_n^{c/2+1} D_{w_κ}(e^{−(c/2+1)ω_n}).

*Evidence.* `loc.py`:
- a^κ_L is computed exactly by running the operators D_i on "coefficient × e^{tv}" pairs, with each coefficient stored on the
  whole W(C_n)-orbit of the base point, so s_i acts exactly;
- it is then compared with ρ_{κL} from (D) (`eng.ell`).

Results: n = 3, 64/64; n = 4, 256/256 at two points; n = 5, 1024/1024. Controls: `loc_ctrl.py` (matching w_m = y_m) gives
25/64 mismatches, `loc_ctrl2.py` (W_{<κ_j}) gives 34/64. First found as the exponential-sum identity `eqv.py`/`eqv2.py`, which
also pinned A_κ and the global factor W_n^{−t}.

*Proof (self-contained; uses neither (D)/Motegi nor K0).* §1bis below. The termwise numerics above are an independent check.

**Cor. D1.** With λ=μ=∅, X(c) = ℓ_κ(w^c) = A_κW_n^{c/2+1}D_{w_κ}(e^{−(c/2+1)ω}). The prefactor tends to (−1)^{|κ|} at w = 1.
Normalising by X₀ (κ = [n], c = 2n, value 1):
  P^κ_{∅∅}(c) = (−1)^{|κ|} χ(X_κ, O(−c/2−1)).
This holds as polynomials in c: d = 0, and χ(X_κ,O(m)) = D_{w_κ}(e^{mω})|_1 by Demazure's character formula for m ≥ 0, and
hence for all m. By Serre duality on the Cohen–Macaulay X_κ it equals χ(X_κ, ω_{X_κ}(c/2+1)).

Direct check (`dictchk.py`, `demB.py`): all 8 (n=3) and 16 (n=4) engine polynomials agree with the Demazure side.
Examples:
- κ = {3}: c(c−2)(2c+1)/24 = −χ(X_{(3)}, O(−c/2−1)), with χ(X_{(3)},O(m)) = (m+1)(m+2)(4m+3)/6 (the degree-4 singular
  3-fold);
- κ = {2}: the quadric cone, (m+1)²;
- κ = {1,2}: Q³ = LG(2,4).

This also settles the Day 249b dictionary failure at κ = {3}. The right reading is not "O_Z" or "boundary ideal with a
shift"; it is the dualising sheaf, ω_{X_κ}(c/2+1), uniformly.

**Cor. D2 (F is the boundary-ideal basis).** ℓ_κ(F_λ) = δ_{κλ} together with Theorem D says that {F_λ ⊗ L_{−ω}} is χ_T-dual to
{O_{X_κ}}. By the standard duality, this is F_λ ∝ L_ω ⊗ O_{X^λ}(−∂X^λ). Check: λ = ∅ gives O_{LG}(−divisor) ⊗ O(1) = O, matching
F_∅ ≡ 1. So for general (λ,μ), at d = 0,
  P_{λμκ}(c) ∝ χ(O_{X_κ}·ξ^λ·ξ^μ·O(1 − c/2)),  with ξ^λ := O_{X^λ}(−∂X^λ).
This is a triple intersection Z = X_κ ∩ gX^λ ∩ g′X^μ of dimension |κ| − |λ| − |μ| = −e, which is the grading law d − deg P = e.
(Cited standard duality; not deep-read. A naive Möbius-inversion test against Ψ_{ν,0} in `ideal.py`/`ideal2.py` did *not*
match. That concerns how Ψ_{ν,0} = GQ sits relative to O_{X^ν} (a torus-orientation convention I have not pinned), not F itself:
F's identification follows from Theorem D plus the cited perfect pairing, see Gap 6. Theorem D does not depend on Cor. D2.)

## 1bis. Proof of Theorem D

Notation:
- g_λ(M) := w_M² F_λ(M) = w_M^{2r+2} Ψ_λ(M), with r = #λ and Ψ_λ := Ψ_{λ,(λ_j−2j)}.
- By Lemma A, Ψ_λ(M) = Σ_{H⊆M,|H|=r} S₀^M(H) A_λ(x_H), where:
  - A_λ(x) = det[f_j(x_i)]/V(x), with V(x) = Π_{i<k}(x_k − x_i);
  - f_j(y) = y^{j−1+λ_j−2j} ρ_{λ_j}(y) and ρ_k(y) = Π_{k′<k}(1 − w_{k′}/y);
  - S₀^M(H) = Π_{h∈H}(1 − x_h^{−2}) · Π_{h<h′∈H}(1 − 1/(x_hx_{h′})) · Π_{t∈M∖H, h∈H}(x_h − 1/w_t)/(x_h − w_t).

S₀^M(H) depends only on the *values* of the variables attached to heads and tails, not on their indices. The w-indices
enter A_λ only through the coefficients of the ρ's.

**The W-actions.**
- On parameters: s_m (1 ≤ m < n) swaps w_m ↔ w_{m+1}; s_n =: σ sends w_1 ↦ 1/w_1. In the Demazure variables
  y_p = w_{n+1−p}, s_m is the simple reflection s_{n−m}, and σ is s_n.
- On subsets: s_m swaps the labels m ↔ m+1; σ sends L ↦ L Δ {1}. This is the action on sign vectors v_L.
- On functions g on subsets (with coefficients in ℚ(w)): (s·g)(L) := s(g(sL)).
- e^{−α}: for s_m it is w_m/w_{m+1}; for σ it is w_1^{−2}.

**Lemma A_m (left action, short simple reflections).**
- (a) If m+1 ∉ λ, then s_m·g_λ = g_λ.
- (b) If m+1 ∈ λ and m ∉ λ, then s_m·g_λ = g_λ + (w_m − w_{m+1}) g_{λ′}, where λ′ = λ with m+1 replaced by m.
- (c) If m, m+1 ∈ λ, then s_m·g_λ = (w_{m+1}/w_m) g_λ.

*Proof.* Applying s_m to both the parameters and the labels of M leaves w_M^{2r+2}, S₀ and the head values unchanged. Only the
coefficients of the ρ's move.
- ρ_k is s_m-invariant unless k = m+1. This proves (a).
- In (b), λ_j = m+1 at some position j. Column j, y^{j−1+θ_j}ρ_{m+1}(y), becomes y^{j−1+θ_j}ρ_m(y)(1 − w_{m+1}/y). By
  ρ_m(1 − w_{m+1}/y) = ρ_{m+1} + (w_m − w_{m+1})y^{−1}ρ_m, this equals the old column plus
  (w_m − w_{m+1})·y^{j−2+θ_j}ρ_m. Since j−2+θ_j = j−1+(m−2j), the added column is exactly column j of λ′ with λ′'s own twist.
  Multilinearity gives (b).
- In (c), λ_{j−1} = m. Subtracting column j−1 (= y^{m−j}ρ_m) from column j leaves −w_{m+1}y^{m−j−1}ρ_m after the swap,
  versus −w_m y^{m−j−1}ρ_m before. ∎

**Lemma B (left action, long simple reflection σ).** Put z = w_1.
- (a) If 1 ∉ λ, then σ·g_λ = z^{−2(r+1)} g_λ.
- (b) If 1 ∈ λ, then σ·g_λ = z^{−2r} g_λ − (z² − 1) z^{−2r−1} g_{λ∖1}.

*Proof.* Put τ(y) := (y − 1/z)/(y − z). This is the tail factor of tail 1 on a head y. We have σ(τ) = 1/τ, and
σ(ρ_k(y)) = ρ_k(y)τ(y) for every k ≥ 2, while ρ_1 ≡ 1.

(a) Take M ∌ 1.
- In Ψ_λ(M∪1), every head set containing 1 contributes 0, since f_j(w_1) = 0 for λ_j ≥ 2.
- For H ⊆ M, S₀^{M∪1}(H) = S₀^M(H)Π_{h∈H}τ(x_h).
- Under σ, the τ's invert, and every column of A_λ gains the factor τ. The two cancel row by row, so σΨ_λ(M∪1) = Ψ_λ(M).
- The prefactor w_{M∪1}^{2r+2} becomes z^{−2r−2}w_M^{2r+2}.

For M ∋ 1, the same computation run backwards gives σΨ_λ(M∖1) = Ψ_λ(M).

(b) It suffices to treat M ∌ 1. The case M ∋ 1 then follows by applying σ, using (a) for λ∖1 and σ² = 1. Write λ⁻ = λ∖1.
Then λ⁻'s columns are f⁻_{j−1}(y) = y·f_j(y) for j ≥ 2, and f_1(y) = y^{−1}. The claim is

  σΨ_λ(M∪1) = z²Ψ_λ(M) + z(1 − z²) w_M^{−2} Ψ_{λ⁻}(M).   (★)

Split σΨ_λ(M∪1) by whether 1 is a tail or a head.

(I) Head sets H ⊆ M (1 is a tail).
- S₀ contributes Π_hτ(x_h)^{−1} after σ, and columns j ≥ 2 gain τ. So the term is S₀^M(H)·det[f_1/τ, f_2, …, f_r]/V.
- Since f_1/τ − z²f_1 = (1 − z²)/(y − 1/z), the sum of these terms is
  z²Ψ_λ(M) + (1 − z²) Σ_H S₀^M(H) det[(y − 1/z)^{−1}, f_2, …]/V.
- Laplace-expand along column 1. Write H = H′ ⊔ {i}; moving row i first costs the same sign in det and in V. Then use
  S₀^M(H′∪i) = S₀^M(H′)·(1 − x_i^{−2}) · Π_{k∈H′}(x_k − x_i)/x_k · Π_{t∈M∖H′, t≠i}(x_i − 1/w_t)/(x_i − w_t). The step uses
  (1 − 1/(x_ix_k))/(x_k − 1/x_i) = 1/x_k, which turns i from a tail into a head.
- Also det[f_2..f_r](x_{H′}) = e_{H′}^{−1}A_{λ⁻}(x_{H′})V(x_{H′}).
- Result: the sum equals Σ_{H′} e_{H′}^{−2} S₀^M(H′) A_{λ⁻}(x_{H′}) · Σ_{i∈T} R_i, where T = M∖H′ and
  R_i = (1 − w_i^{−2})(w_i − 1/z)^{−1}Π_{t∈T∖i}(w_i − 1/w_t)/(w_i − w_t).

(II) Head sets H = {1} ⊔ H′ (1 is a head, with value z).
- After σ, the head value is 1/z. Its row in A is (f_1(1/z) = z, 0, …, 0), because ρ_k^σ(1/z) = 0 for k ≥ 2.
- V(1/z, x_{H′}) = Π_{i∈H′}(x_i − 1/z)·V(x_{H′}).
- The head, pair and tail factors of the head 1 become −z²(1 − z^{−2}), Π_{h∈H′}(1 − z/x_h) and
  Π_{t∈T}(w_t − z)/(w_t(1 − zw_t)).
- Using τ(x)/(x − 1/z) = 1/(x − z) and (1 − z/x)/(x − z) = 1/x, the term equals
  z(1 − z²) e_{H′}^{−2} Π_{t∈T}(w_t − z)/(w_t(1 − zw_t)) · S₀^M(H′) A_{λ⁻}(x_{H′}).

(Residue identity.) Let h(u) := Π_{t∈T}(u − 1/w_t)/(u − w_t). Then R_i = Res_{u=w_i} h(u)/(u(u − 1/z)). The function
h(u)/(u(u − 1/z)) is O(u^{−2}) at ∞, and its remaining poles are 0 and 1/z, with residues −zΠ_tw_t^{−2} and
zΠ_t(w_t − z)/(w_t(1 − zw_t)). Hence
  Σ_{i∈T} R_i = zΠ_{t∈T}w_t^{−2} − zΠ_{t∈T}(w_t − z)/(w_t(1 − zw_t)).

Add (I) and (II). The Π(w_t − z)/(…) terms cancel, leaving z²Ψ_λ(M) + z(1 − z²)Σ_{H′}e_{H′}^{−2}Π_Tw_t^{−2}S₀A_{λ⁻}. That is
(★), since e_{H′}^{−2}Π_{t∈T}w_t^{−2} = w_M^{−2}.

Translating (★) back through the prefactors w^{2r+2} gives (b). ∎

**The induction.** Define the functional Λ_κ(g) := Σ_L a^κ_L g(L), where the a^κ_L are defined recursively:
- a^∅_L = δ_{L∅};
- if κ = sκ′ with |κ| = |κ′| + 1, for a simple reflection s with e^{−α} as above, then
  a^κ_L := [a^{κ′}_L − e^{−α}·s(a^{κ′}_{sL})]/(1 − e^{−α}).

This is D_{w_κ}(e^{tω}) = Σ_L a^κ_L e^{tv_L} computed by D_s∘D_{w_{κ′}}, and it is exactly what `loc.py` implements. Reindexing
L ↦ sL in the second sum gives

  Λ_κ(g) = [Λ_{κ′}(g) − e^{−α}·s(Λ_{κ′}(s·g))]/(1 − e^{−α}).   (Rec)

*Claim:* Λ_κ(g_λ) = δ_{κλ}/A_κ for all κ, λ. Then Λ̃_κ := A_κΛ_κ(w²·) is the dual functional of the basis {F_λ}, so
Λ̃_κ = ℓ_κ. That is Theorem D. (Uniqueness of the dual basis also makes a^κ independent of the chosen chain.)

*Induction on |κ|.*
- Base: Λ_∅(g_λ) = g_λ(∅) = F_λ(∅) = δ_{λ∅}, and A_∅ = 1.
- Step: κ = sκ′. By Lemmas A_m(a,b) and B, s·g_λ ∈ span{g_λ, g_{λ↓}}, where λ↓ is s applied to λ when that is shorter.
  So by the induction hypothesis, Λ_{κ′}(s·g_λ) = c^λ_{κ′}/A_{κ′}, with c^λ_{κ′} the g_{κ′}-coefficient of s·g_λ. This
  coefficient is nonzero only for λ = κ′ or λ = κ.
- Hence by (Rec), Λ_κ(g_λ) = 0 for λ ∉ {κ, κ′}. Two checks remain.

1. *λ = κ′:* need s(p/A_{κ′}) = e^{α}/A_{κ′}, where p is the diagonal coefficient.
   - s = s_m (m ∈ κ′, m+1 ∉ κ′): p = 1, and s(W_{≤m}) = W_{≤m}w_{m+1}/w_m, so s(1/A_{κ′}) = (w_{m+1}/w_m)/A_{κ′} = e^{α}/A_{κ′}. ✓
   - s = σ (1 ∉ κ′): p = z^{−2(r′+1)}, s(p) = z^{2r′+2}, and s(1/A_{κ′}) = z^{−2r′}/A_{κ′}. The product is z²/A_{κ′} = e^{α}/A_{κ′}. ✓
2. *λ = κ:* need −e^{−α}s(q/A_{κ′})/(1 − e^{−α}) = 1/A_κ, where q is the g_{κ′}-coefficient of s·g_κ.
   - s = s_m: q = w_m − w_{m+1}. The left side is −(w_m/w_{m+1})(w_{m+1} − w_m)(w_{m+1}/w_m)/(A_{κ′}(1 − w_m/w_{m+1})) = −w_{m+1}/A_{κ′}.
     The right side is also −w_{m+1}/A_{κ′}, since A_κ/A_{κ′} = −W_{≤m}/W_{≤m+1}. ✓
   - s = σ: q = −(z² − 1)z^{−2r−1} with r = r′+1. Then s(q) = (1 − z^{−2})z^{2r+1}, and the left side is
     −z^{−2}(1 − z^{−2})z^{2r+1}z^{−2r+2}/(A_{κ′}(1 − z^{−2})) = −z/A_{κ′}. The right side: 1/A_κ = −W_{≤1}/A_{κ′} = −z/A_{κ′}. ✓
∎

*Checks.*
- `leftact.py` (n = 3 at two prime points, n = 4) reproduces Lemmas A_m and B coefficient by coefficient. The off-diagonal
  coefficients w_m − w_{m+1} and −(w_1² − 1)/w_1^{2r+1} were identified at the point (5,7,11,13), because the point (2,3,5)
  conflates constants with variables.
- `loc.py` checks the conclusion termwise (n ≤ 5).

*Remark.* Lemmas A/B say that {w²F_λ} transforms under the left W-action exactly as a (normalised) opposite-Schubert-type
K_T-basis does. Theorem D is the dual statement. Motegi's (D) and this formula are two closed forms of the same ℓ_κ.

## 2. Lemma Φ (Demazure ↔ atoms), proved

Let f ↦ f^\* be e^μ ↦ e^{−μ}, φ(f) := e^{−ρ}f^\*, and D̄_i := D_i − 1, so D̄_i(g) = e^{−α}(g − s_ig)/(1 − e^{−α}).

**Lemma Φ.** φ(D_i f) = −D̄_i(φ f).

*Proof.* (D_if)^\* = (f^\* − e^{α}s_if^\*)/(1 − e^{α}) = (s_if^\* − e^{−α}f^\*)/(1 − e^{−α}).

Put g = φf = e^{−ρ}f^\*. Since s_i(e^{−ρ}) = e^{−ρ+α_i}, we have s_ig = e^{−ρ+α}s_if^\*. So e^{−ρ}s_if^\* = e^{−α}s_ig and
e^{−ρ}f^\* = g. Hence
  φ(D_if) = (e^{−α}s_ig − e^{−α}g)/(1 − e^{−α}) = −D̄_i g.  ∎

Hence D_w(e^{tω}) = (−1)^{ℓ(w)} φ^{−1}D̄_w(e^{−tω−ρ}). With t = −c/2−1, Cor. D1 becomes
P^κ_{∅∅}(c) = D̄_{w_κ}(e^{λ_c})|_1, where λ_c = (c/2+1)ω_n − ρ = (c/2+1−n, …, c/2).

Note that ⟨λ_c, α_i^∨⟩ = −1 for all i < n and ⟨λ_c, α_n^∨⟩ = c/2. So for odd c, only the s_n-step is non-integral (§5).

## 3. Theorem E: the upper end at even c, λ = μ = ∅

**Theorem E.** (Theorem D is proved, §1bis.) Then for every κ ⊆ [n] and every integer k ≥ n+1,
  P^κ_{∅∅}(2k − 2) = h⁰(X_κ, ω_{X_κ}(k)) ≥ 1.

*Cited facts* (standard; NOT deep-read this session, so this is a gap for a "proved" grade):
- (G1) Demazure's character formula χ_T(X_w, L_λ) = D_w(e^λ) (Andersen, Ramanathan; Kumar's book ch. 8). It is used in
  Cor. D1 to read the Demazure side of Theorem D as an Euler characteristic.
- (G2) Schubert varieties in G/B and G/P are normal, Cohen–Macaulay, with rational singularities (Ramanathan; Brion–Kumar ch. 3).
- (G3) For X = X_w ⊂ G/P and L ample, H^j(X, L^{−1}) = 0 for j < dim X (Frobenius-splitting Kodaira vanishing, Brion–Kumar ch. 3).
- (G4) For a Schubert variety Y ⊂ G/B, ω_Y ≅ O_Y(−∂Y) ⊗ L_{−ρ} (Brion–Kumar ch. 3).
- Standard: ω_{LG(n,2n)} = O(−n−1).

*Proof.*
1. **Vanishing.** By (G2), X := X_κ is CM, so Serre duality gives H^i(X, ω_X(k)) ≅ H^{d−i}(X, O(−k))^\*, which is 0 for
   i > 0 and k ≥ 1 by (G3). So χ(ω_X(k)) = h⁰(ω_X(k)).
2. **A section at k = n+1.** Let π: G/B → G/P = LG and Y := π^{−1}(X) = X_{w_κ w_{0,P}}. π is a locally trivial P/B-bundle,
   so π_\*O_Y = O_X, and π^\*ω_X ⊗ ω_{Y/X} = ω_Y. Here ω_{Y/X} = (L_{−2ρ} ⊗ π^\*O(n+1))|_Y. By (G4),
   π^\*(ω_X(n+1)) = O_Y(−∂Y) ⊗ L_ρ. The extremal-weight section p_v of L_ρ (v = w_κw_{0,P}) does not vanish on the open cell,
   and it vanishes on every X_{v′} ⊂ ∂Y, since V_{v′}(ρ) has no weight vρ. ∂Y is reduced, so p_v ∈ H⁰(Y, O_Y(−∂Y) ⊗ L_ρ) is
   nonzero. By the projection formula (π flat, fibres P/B, π_\*π^\*𝓕 = 𝓕), H⁰(X, ω_X(n+1)) ≠ 0.
3. **k > n+1.** O(1) is globally generated and X is irreducible, so some section s of O(k−n−1) is generically nonzero on
   X. ω_X is torsion-free (CM on an integral scheme), so s·(nonzero section) ≠ 0.
4. With Cor. D1, P^κ(2k−2) = χ(ω_X(k)) = h⁰ ≥ 1. ∎

Data: P^κ(2k) ≥ 1 for k = n..n+5, all κ, n = 3, 4 (`dictchk.py`). For example P^{(3)}(6) = 13.

The window zeros at even c ∈ [0, 2n−2] are k ∈ [1, n]. There h⁰(ω_{LG}(k)) = h⁰(O(k−n−1)) = 0 for κ = [n], which is Cor. Δ
re-derived.

**What Theorem E does not cover.**
- (a) Odd c.
- (b) General (λ,μ) at d = 0. By Cor. D2 this needs the same two facts (vanishing, plus a section of ω_Z ⊗ ω_{LG}^{−1}|_Z) on the
  triple intersections Z, which is Brion's setting (2002 positivity paper; not read).
- (c) The exceptional instances. A lead (hunch): when d = 1, P is the ε-linear term of Σ_ν c^ν_{λμ}(w)·(Richardson term P^κ_{∅ν}).
  It is therefore a combination of Richardson polynomials whose coefficients are first derivatives of equivariant K-theory
  structure constants, and those have signs by Anderson–Griffeth–Miller positivity (not read). Together with HP_R (Richardson
  Taylor-positivity at U+1, computed 35/35 and 126/126), this would give HP for the exceptional instances.

## 4. The trichotomy and the reductions

**Prop. T.** Type C. By Lemma G, d ≥ e and deg P ≤ d − e.
- If e > 0 and d = e, then P is a nonzero constant and has no roots. HP holds.
- If d = 0, P is the honest limit X(c)|_{w=1}, a non-equivariant Euler characteristic (Cor. D1/D2).
- Every other instance is exceptional (d > max(e,0)).

Census (`exc.py`):

| n | d = 0 | d = e > 0 | exceptional |
|---|---|---|---|
| 3 | 64 | 49 | 2 |
| 4 | 356 | 349 | 21 |
| 5 (sample) | 70 | 77 | 2 |

The d = 0 instances are all positive above U (`signlaw2.py`, 420/420 at n ≤ 4), and integer-valued at even c.

The exceptional instances have P of degree ≤ 3 with roots in {0, ½, 1, 2}. Examples:
- (3),(3),{1,2,3}: 4c;
- (4),(4),[4]: −c(c−1)(c−2)/36 ∝ P^C_{12};
- (1,2),(1,2,3),(2,3,4): −280(2c−1)/9.

**Reduction A → C (computed).** For type-A instances with d = 0,
  P^A(λ,μ,ν;a,b;c) = P^C(λ,μ,ν⁻⁻; c − 2),
where ν⁻⁻ is ν with its two largest elements removed. This holds for every pair (a,b): N = 4, 78/78; N = 5, 640/640, against
the full C n=3 table, 0 mismatches. Geometric reading (hunch): on H_ab the subtorus ker(e_a+e_b) has fixed components
{Λ ⊇ span(e_a,f_b)} ≅ LG(N−2), and the residue is integration there. The shift c−2 is the normal/line-bundle correction. This is
why U^A_N = 2N−4 = U^C_{N−2} + 2.

**Theorem AC (top pair, proved given (D)).** Let (a,b) = (N−1, N), v := w_{N−1} (so w_N = 1/v on H), and
G(v) := (1 − v²)(1 − v^{−2}) Π_{k≤N−2}(1 − vw_k)(1 − w_k/v). Then, as rational functions on H,
  R^A(λ,μ,ν; N−1,N; c) = (vG(v))^{−1} · C^{(N−2)}(λ, μ, ν∖{N−1,N}; c − 2)  if ν ⊇ {N−1,N},
and R^A = 0 otherwise. Here C^{(N−2)} is the type-C quantity in the variables w_1..w_{N−2}, and it is 0 if λ or μ ⊄ [N−2].
After normalising by the per-pair X₀, P^A_{top pair}(c) = P^C_{N−2}(c − 2) exactly, including the d > 0 instances.

*Proof.* Write L = L″ ∪ {N−1,N}. Then L ≤ ν iff ν ⊇ {N−1,N} and L″ ≤ ν⁻⁻ := ν∖{N−1,N} (top-aligned dominance).

In the residue form of (D), Res_H ρ_{νL} = [τ(ν)/τ(L)]·φ⁰_{ν^c}(L^c)/(φ⁰_{L^c}(L^c)·(F_L(L)/h))|_H, compare factor by factor:
- **Complements.** They lie in [N−2] and coincide with the complements of ν⁻⁻ and L″ in [N−2]. φ⁰ is N-free and involves no
  w_{N−1}, w_N. So the φ⁰ factors are literally the rank-(N−2) ones.
- **τ-ratio.** τ(ν)/τ(L) = c(L)/c(ν) = c(L″)/c(ν⁻⁻), since c is multiplicative and the {N−1,N} parts cancel.
- **The diagonal F_L(L).** Use F_L(L) = φ⁰_L(L)·Π_j w_{L_j}^{L_j−2j+2r}, then lemma L1 twice (forced heads N, N−1):
  φ⁰_L(L) = e⁰_N(L)·e⁰_{N−1}(L∖N)·φ⁰_{L″}(L″). The factor h = 1 − 1/(w_{N−1}w_N) sits in e⁰_N. On H:
  - e⁰_N(L)/h · e⁰_{N−1}(L∖N) = (1−v²)(1−v^{−2}) Π_{c∈L″}(1 − v/w_c)(1 − 1/(vw_c)) Π_{k∈[N−2]∖L″}(1 − vw_k)(1 − w_k/v);
  - (1 − v/w_c)(1 − 1/(vw_c)) = w_c^{−2}(1 − vw_c)(1 − w_c/v).
  So this product equals G(v)·w_{L″}^{−2}.
- **Monomials.** With r = r″ + 2, the exponents are those of L″ plus 4 on each element of L″, and N+1, N on N−1, N. On H the
  latter give v^{N+1}v^{−N} = v. So F_L(L)/h = F_{L″}(L″)·w_{L″}^{2}·vG(v).

Hence Res_H ρ_{νL} = ρ^{(N−2)}_{ν⁻⁻L″}·w_{L″}^{−2}/(vG(v)). Insert into (A), with F_λ(L″) N-free:
R^A = (vG(v))^{−1}Σ_{L″}ρ^{(N−2)}_{ν⁻⁻L″}w_{L″}^{c−2}F_λF_μ(L″). ∎

*Check.* `resAC.py`: n(L″)·w_{L″}² is constant over all L″ (N = 4, 5) and independent of ν (N = 4).

**Corollary AC′ (all pairs, ε⁰ level; proved given (D)).** For every pair a < b, every instance and every c,
  Q₀^A(λ,μ,ν; a,b)(c) = Q₀^{C,(N−2)}(λ, μ, ν∖{N−1,N})(c − 2),
where Q₀ is the ε⁰-coefficient of the normalised quantity, and the right side is 0 if ν ⊉ {N−1,N}. In particular every d = 0
type-A instance has P^A(c) = P^C_{N−2}(λ,μ,ν⁻⁻; c−2). This is the census statement (640/640, 78/78), now proved.

*Proof.*
1. **Transport formula.** Let s = s_m act on functions by (s·f)(L) = s(f(sL)). It is multiplicative, fixes w^c (every c) and
   w², and sends 1_{⊇ab} to 1_{⊇s(ab)}. By Lemma A_m, s·F_λ = Σ_{λ′} c^λ_{λ′}F_{λ′} with c ∈ {1, w_{m+1}/w_m} on the diagonal
   and c = w_m − w_{m+1} off it. Duality gives ℓ_ν(f) = Σ_κ c^κ_ν · s(ℓ_κ(s·f)). Applying Res_{H_ab} (s maps H_{s(ab)} to
   H_ab and h_{s(ab)} to h_ab):
     R^A_{ab}(λ,μ,ν) = Σ_{κ,λ′,μ′} [c^κ_ν s(c^λ_{λ′}) s(c^μ_{μ′})]|_{H_ab} · s[R^A_{s(ab)}(λ′,μ′,κ)].
   Every diagonal coefficient is 1 + O(ε) and every off-diagonal one is O(ε) on the curve.
2. **Orders.** By Theorem AC, top-pair instances are K·C^{(N−2)} with K = (vG(v))^{−1}. C^{(N−2)} has ε-order ≥ 0. For even c it
   is Λ_κ applied to the Laurent GKM function w^{c+2}F_λF_μ (Theorem D), and left divided differences preserve Laurent GKM
   functions. Since orders are polynomial identities in c, the even c suffice. *Input used:* F_λ is Laurent-valued and GKM.
   Laurentness is checked symbolically at n = 3, 4 (27/27, 110/110, `laurent.py`); in general it follows from Cor. D2 (F a K_T-class).
   It is listed as Gap 6.
   Iterating the transport formula from the top pair (moving b up to N with s_b, …, s_{N−1}, then a up to N−1), every R^A_{ab}
   has order ≥ ord K.
3. **Normalisers.** The per-pair normaliser X₀^{(ab)} = R^A_{ab}(∅,∅,[N]; 2N−2) is (1 + O(ε))·s[X₀^{s(ab)}], with no
   off-diagonal term since no κ has κ′ = [N]. So it has order exactly ord K.
4. **Conclusion.** Relative orders are ≥ 0 for all instances. Comparing ε⁰-coefficients in the transport formula gives
   Q₀^{ab}(λ,μ,ν) = Q₀^{s(ab)}(λ,μ,ν). Iterate to the top pair and apply Theorem AC. ∎

Remark. The same formula at order ε¹ expresses Q₁^{ab} as Q₁^{s(ab)} plus first-order coefficients times Q₀'s of
*neighbouring* instances. These are type-C polynomials at c−2. This is the mechanism behind the exceptional type-A census, all
462 at N=5 being shifted type-C polynomials, but positivity of such combinations is not proved.

*Other pairs.* `resAC2.py` searched, for each pair (a,b) ≠ top and each ν, for a single rank-(N−2) functional Res_H ρ = K·w^{−2}ρ^{(N−2)}_{ν̃}.
- At N = 4, 42/46 instances have such a ν̃, with a ν-dependent K.
- The other 4 do not; they are combinations.
- The reason: for b < k the labels' ρ_k carry the pair factor (1 − w_a/y)(1 − 1/(w_ay)) on H, which the rank-(N−2) system
  lacks. This is the source of the type-A shifts s ∈ {0,1} in the exceptional census.

So for non-top pairs the reduction stays **computed** (d = 0: exact polynomial agreement, 640/640 at N=5).

Type-A census, with the trivial class now "P constant" (deg P = 0):

| N | constant (trivial) | d = 0 (→ C_{N−2}) | exceptional |
|---|---|---|---|
| 3 | 16 | 9 | 0 |
| 4 | 310 | 78 | 20 |
| 5 | 4476 | 640 | 462 |

All 462 exceptional instances at N = 5 are scalar multiples of a type-C d = 0 polynomial (n ≤ 3) at c − s, with s = 2 (387),
1 (56) or 0 (19). Since type-C d=0 roots are ≤ 2·3 − 2 = 4, the exceptional roots are ≤ 6 = U^A_5, which is consistent with
HP★'s edge.

**Net effect.** HP for all N (types A and C) reduces to one statement:

**(HP_C⁰)** For every type-C d = 0 instance with κ ⊆ [m], P_{λμκ}(c) ≠ 0 for every integer c > 2m − 2.

This is subject to three things:
- the A→C reduction and the exceptional-proportionality, both computed, needing proofs;
- the bookkeeping that the shift s never exceeds 2 when the rank drops by 2;
- for exceptional type-C instances, the same proportionality (not yet tested systematically; the n ≤ 4 roots are all ≤ 2).

At even c, (HP_C⁰) is Theorem E for λ=μ=∅, and Brion-type geometry for general (λ,μ).

## 5. Odd c: what is open, precisely

For odd c, k = c/2 + 1 is a half-integer. c ↦ w^c is then not a K_T(LG)-class: the GKM condition along the long-root curves
needs (1 − w_i²) | (1 − w_i^c). So there is no sheaf on X_κ whose Euler characteristic is P(c), and the values are not
integers. For example P^{(3)}(5) = 165/24. The statement needed is analytic:

**(OC)** The Hilbert polynomial h_ω(k) := χ(X, ω_X(k)) of a Schubert variety X ⊂ LG(m,2m) (and of the d = 0 triple
intersections) has no zero at half-integers k ≥ m + ½.

Evidence:
- HP★ (Day 249b) says every complex root of P has Re ≤ U, i.e. Re k ≤ m. That is the **canonical strip**, Golyshev-style, for
  ω-twisted Hilbert polynomials of Schubert varieties.
- Single labels X_{(m)}, m ≤ 7, are real-rooted with roots in [−1, 2m−2] (in c).
- In general P is not real-rooted ({2,3}: 1 ± i).

Approaches tried today, all failing:
1. **h\*-vector positivity (Stanley, CM).** It gives P = Σ_i h\*_i binom(·, d) with h\*_i ≥ 0. Termwise, this is positive only
   above c/2 ≈ d − 1 ≫ m, because the h₀ term has roots up to d.
2. **B-transfer.** The spinor bundle on OG(m,2m+1) makes every integer c an honest twist, with index 2m and the same Weyl
   group. But P_C^κ is not a nonnegative combination of B-Schubert polynomials: P_C^{(3)} = −⅛P_B^{(1)} + ¼P_B^{(2)} + ½P_B^{(3)},
   a unique solution (`c2b.py`). D^C_n = D^B_n∘(1 + e^{−e_n})^{−1} is the exact relation, and the factor is not positive.
3. **w ↦ −w.** It does not relate X(c) at odd and even c (`negw.py`: ratios are not ±1).

A natural next attack: Lemma Φ's atom form. All s_i-steps with i < n are integral. Only the first operator applied, D̄_n, sees
the half-integer c/2. One D̄_n-step on e^{λ_c} gives a polynomial in c/2 with explicit positive "string sum" structure
(continuous analogue: an integral ∫₀^{c/2}). If the remaining integral atom steps preserve positivity of the string density,
(OC) follows. This is untested.

### 5.1 The refined conjecture HP⁰⁺ (both parities at once)

**Observation (computed, exact).** For every non-constant centre polynomial in the stored exact data, P(U + t) ∈ ℚ[t] has
**one-signed coefficients, zeros allowed**. This is the Taylor expansion at the window edge U itself, not at U+1.

| data | non-constant instances |
|---|---|
| C n=3 | 46 |
| C n=4 | 297 |
| C n=5 sample | 59 |
| A N=4 | 62 |
| A N=5 | 902 |

Total 1366/1366, the edge witnesses with P(U) = 0 included (`HP0+` test). Also exhaustive for **λ=μ=∅ at n = 5: 32/32** (HP⁺ and HP⁰⁺), via Theorem D: exact Demazure localisation at a point 10^{−40} from 1, with integer-rounded Hilbert values (`hp0big2.py`, `hp0b_n5.txt`; the integer values match `dem.chi` exactly at n = 4). Since P ≢ 0, this gives P(c) ≠ 0 for **every real
c > U**, so odd and even c at once.

**Conjecture HP⁰⁺.** P(U + t) ∈ ±ℝ_{≥0}[t] for every allowed instance.

**Reformulation for λ = μ = ∅.** By Cor. D1, P^κ(U + 2s) = χ(X_κ, ω_{X_κ}(n + s)) = χ(X_κ, ω_X ⊗ ω_{LG}^{−1}(s − 1)). Pull back to
G/B as in Theorem E: π^\*(ω_X ⊗ ω_{LG}^{−1}) = O_Y(−∂Y) ⊗ L_ρ, so
  P^κ(U + 2s) = χ(Y, O_Y(−∂Y) ⊗ L_{ρ−ω_n+sω_n}) = dim A_v(ρ − ω_n + sω_n)  (integers s ≥ 0, v = w_κw_{0,P}).
Here A_v is the opposite-Demazure atom; higher cohomology vanishes since ρ − ω_n = (n−1, …, 1, 0) is dominant. So HP⁰⁺ for
this family is an **Ehrhart-positivity statement**: the atom dimension along the ray ρ − ω_n + sω_n is a polynomial in s with
nonnegative coefficients. The half-integers s are exactly odd c.

Sanity checks:
- κ = [n] (Y = G/B): it is the Weyl product Π_β(⟨ρ−ω,β^∨⟩ + s⟨ω,β^∨⟩)/⟨ρ,β^∨⟩, and every factor has nonnegative coefficients
  in s. ✓
- At s = 0 the atom is nonzero iff v is minimal in vW_{ρ−ω} = {v, vs_n}. That reproduces the edge witnesses (v = w_0 for κ = [n]).

Ehrhart coefficients of general lattice polytopes can be negative, so this is a genuine positivity question. The natural
tools are string or Gelfand–Tsetlin-type polytopes for Demazure atoms, with Minkowski additivity in the weight. Not attempted
beyond the reformulation.

## 6. Gaps (precise)

1. ~~Theorem D is computed, not proved.~~ **Closed in the same session**: §1bis proves it via the left Demazure recursion.
2. Theorem E uses (G2)–(G4) from Brion–Kumar, not deep-read. Its grade is therefore "proved modulo D + citations"; the registry
   node is graded **sketched**.
3. General (λ,μ) at even c: needs the triple-intersection version (Cor. D2 plus Brion 2002), with the GQ orientation in Cor. D2
   to pin.
4. The A→C reduction is **proved** (Theorem AC for the top pair; Cor. AC′ for d = 0 at every pair; both given (D), which rests on Motegi's biorthogonality, registry node q488-phi-inf-dual-biorthogonality). The exceptional type-A instances (d ≥ 1, non-constant) are computed only.
5. Odd c, (OC): open. Refined form: HP⁰⁺ (§5.1), computed 1366/1366, which for λ=μ=∅ is Ehrhart positivity of Demazure atoms.
6. Cor. AC′ step 2 uses that F_λ is a Laurent GKM function (so that relative orders are ≥ 0).
   - *Laurent:* elementary. In Lemma A form the only non-monomial denominators are tail factors (x_h − w_t). The terms for H and
     for H − h + t have opposite residues along w_h = w_t, and all other factors agree there by symmetry. Checked symbolically
     at n = 3, 27/27 and n = 4, 110/110 (`laurent.py`).
   - *GKM:* by Theorem D, F_λ ⊗ L_{−ω} satisfies the same 2^n independent linear conditions Λ_κ(·) = δ_{κλ}/A_κ as the χ_T-dual
     basis of {[O_{X_κ}]} in K_T(LG). So it *is* that K_T-class, given the standard facts that K_T(G/P) is R(T)-free with a
     perfect χ_T-pairing and that Λ_κ = χ_T(X_κ, ·) on K_T-classes (Demazure/AB). These are the same citation family as G2–G4,
     not deep-read.
   - Empirically consistent: d ≥ 0 in all 6011 type-A and 841 type-C instances.
