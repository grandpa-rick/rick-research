# The window as a Hilbert polynomial: (SC) ⇐ (HP), and a one-sign certificate above U (PROVE 249, cycle 2)

Rick, 2026-10-21, second PROVE pass on PROVE 249. Continues `proofs/2026-10-21-symbol-theorem-inversion-duality.md` §6,
where everything except **(SC)** was closed. Notation: `proofs/2026-10-18-q488-d-infinity.md` §1–§6 (F_κ, (D), ℓ_ν, R^A, C,
E, E_C) and `2026-10-19-theorem-W-sharp.md` (U^A_N = 2N−4, U^C_n = 2n−2, Lemma Δ, Cor. Δ). Scripts:
`work-in-progress/scripts/prove249c/`.

## 0. Verdict

| item | statement | grade |
|---|---|---|
| **Lemma E** (ε-polynomiality) | On the curve w(ε) = 1 + aε (type A: inside H_ab), the ε^j-coefficient of X(c)/X₀ is a polynomial Q_j(c) in c. Let d = min{j : Q_j ≢ 0}, which is finite for allowed instances. Then Q_d(c₀) ≠ 0 ⇒ X(c₀) ≢ 0. | **proved** (§2) |
| **Conjecture HP** | For every allowed instance, the "non-equivariant polynomial" P := Q_d has no integer root c > U. | conjecture |
| **HP⁺** (one-sign form) | P(U+1+t) ∈ ℚ[t] has all nonzero coefficients of one sign and a nonzero constant term. Hence P ≠ 0 on the whole real ray c ≥ U+1, odd c included. | **computed, exact**: C n ≤ 3 (115/115); C n = 4 (§3); A N ≤ 4 (25/25, 408/408); A N = 5 (§3) |
| **HP★** (root form, strongest) | Every complex root of P has Re ≤ U, with equality only at the window-edge witnesses: type C κ = [n] with λ, μ ∈ {∅, (1)}; type A ν = [N] with λ = ∅, μ ∈ {∅, (1)}, any pair. So P(U+1+t) is Hurwitz-stable, which implies HP⁺. | computed (exact P, numerical roots per irreducible factor): C n=3, 4 (max Re = U, 3 edge each), C n=5 sample (max Re 6 < 8), A N=4 (12 edge), A N=5 so far (max Re 4 < 6) |
| **Reduction** | HP ⇒ (SC)'s conclusion: X ≠ 0 for every allowed instance and every c > U. With W⁺ and Prop Z this gives Z^A_N = [0, 2N−4] for all N ≥ 4 (N ≤ 3 is already proved), and with Cor. Δ Z^C_n = [0, 2n−2]. | **proved** (§2, given HP) |
| Structure of P (type C) | **Grading law d − deg_c P = e**, where e := \|λ\| + \|μ\| − \|κ\| (\|·\| = sum of elements). It holds in 115/115 cases at n=3 and 726/726 at n=4. Generically d = max(e,0) (113/115, 705/726); otherwise both d and deg go up by one. Also P(2k) ∈ ℤ when d = 0, and P(0) = 0 for λ = μ = ∅ ≠ κ. | computed (n ≤ 4) |
| Vertex form of (SC) | D·X (D = C_n Weyl denominator) is a Laurent polynomial. At C n=3, c ≥ U, its Newton polytope has exactly 48 = \|W(C₃)\| vertices, every vertex coefficient is ±1 (8 instances × c ∈ {4,5}). Below U it breaks: at c = −1 and c = 3 some instances have ±2 vertex coefficients, and at c = 1 vertex counts 52 and 60 occur. | computed (n=3) |
| Geometric reading | ℓ_[n] is K-theoretic integration on LG(n,2n) (Lemma Δ is the Weyl character formula). The C-window is the Kodaira strip, c ↔ 2n−2−c is Serre duality, and P is a Hilbert polynomial of a Richardson-type Z with dim Z = −e. HP⁺ would then be "Hilbert polynomial positivity above the a-invariant". | hunch (partial dictionary fails a named test, §4) |

**Headline.** (SC) asks why an iterated leading coefficient never cancels. That is the wrong question: it is a statement about
2^n·n! vertices, one Weyl chamber at a time. The right object is the *centre*. Send all w → 1 and the window problem becomes a
one-variable polynomial P(c). Its zeros are where the window lives, and above U it is one-signed in the strongest possible
sense: the Taylor coefficients at U+1 share a sign. Every allowed instance checked so far (C n ≤ 4, A N ≤ 4, A N = 5 in
progress) satisfies this, exactly, in rational arithmetic. An all-N proof of HP⁺ is a positivity theorem about a single
polynomial per instance, not about a peel tree.

## 1. Why the vertex picture is the wrong lens (what was tried first)

Write X = C(λ,μ,κ;c) = Σ_{L∈E_C} T_L. By (D) and Lemma Δ, T_L = K·(−1)^{|L^c|}V(y^L)·φ⁰_{κ^c}(L^c)·w_L^c F_λ(L)F_μ(L),
with K independent of L.

1. *Alternant hope (killed).* D·X is anti-invariant under w_i ↦ 1/w_i only in the trivial case (∅,∅,[n]) (exponents
   −c−2(i−1)). In every other case tested the ratio is not a monomial (`t1.py`, `t2.py`). So the labels break the Weyl
   symmetry, and X is not a C_n alternant.
2. *Vertex phenomenon (true but hard).* D·X is a Laurent polynomial whose Newton polytope has 48 vertices, all with
   coefficient ±1, for every C₃ instance tested at c ≥ 4 (15 (instance, c) pairs, `t3.py`–`t5.py`). At c = −1 and c = 3, coefficients ±2 and
   50–60 vertices appear. So (SC) ≡ "lex vertices are ±1" is a genuine edge phenomenon.
3. *Configuration level (fails).* For a generic direction ξ, the ξ-top configuration (L plus head maps) is not unique, and the
   top group often cancels exactly ((2,0) and (4,0) counts in `t6.py`). These are artefacts of expanding rational summands
   separately.
4. *Summand level (almost).* Every T_L has ξ-leading coefficient ±1 (all ξ, all instances, n=3, `t7.py`). The ξ-top L is
   unique for every ξ tried at c ≥ U+2, but at c = U+1, 2 of 1150 directions tie and cancel.

So a proof along these lines would have to choose ξ per instance at the edge, and control GQ-localisation degrees in every
chamber. That is a K-theoretic GKM-triangularity theorem I do not have.

## 2. The centre: Lemma E and the reduction

Fix an allowed instance (type C: (λ,μ,κ) in system [n]; type A: (λ,μ,ν;a,b) in system [N]). Let X(c) denote C(λ,μ,κ;c),
resp. R^A(λ,μ,ν;a,b;c), and let X₀ be the normaliser:
- type C: C(∅,∅,[n]; 2n);
- type A: R^A(∅,∅,[N];a,b; 2N−2), same pair (a,b).

Choose a ∈ ℚ^n generic. On the curve w_i(ε) = 1 + a_iε (type A: w_b := 1/w_a, then Res over the transverse variable as in
the d-infinity file §4; on H_ab the curve stays inside H_ab), every factor of every summand is a rational function of ε.
So X(c)(ε)/X₀(ε) is a rational function of ε.

**Lemma E.** Write X(c)(ε)/X₀(ε) = Σ_{j ≥ j₀} Q_j(c) ε^j (Laurent expansion at ε = 0). Then:
- (i) each Q_j(c) is a polynomial in c;
- (ii) d := min{j : Q_j ≢ 0} is finite for every allowed instance;
- (iii) if Q_d(c₀) ≠ 0 for an integer c₀, then X(c₀) ≢ 0 as a rational function of w.

*Proof.* (i) By (D), X(c) = Σ_{L∈E} α_L·Π_{m∈L''}w_m^c, with α_L independent of c and L'' = L (type C) or L∖ab (type A).
On the curve, Π_{m∈L''}w_m(ε)^c = exp(c·ℓ_L(ε)) with ℓ_L(ε) := Σ_{m∈L''}log(1 + a_mε) = O(ε). (Type A: w_b is not in L'',
and the residue is a coefficient extraction in the transverse variable, commuting with the ε-expansion as in the d-infinity
file §6.) Hence the ε^k-coefficient of exp(cℓ_L) is a polynomial in c of degree ≤ k. Multiply by the c-free Laurent series
α_L(ε)/X₀(ε) and sum: each ε^j-coefficient is a finite sum of polynomials in c.
(ii) Theorem W⁺ gives X(−1) ≢ 0 for allowed instances. For generic a the curve is not contained in the zero locus of a
nonzero rational function, so the ε-series at c = −1 is nonzero. Hence some Q_j(−1) ≠ 0.
(iii) If Q_d(c₀) ≠ 0, then the restriction of X(c₀) to the curve is nonzero, so X(c₀) ≢ 0. ∎

Call P := Q_d the **centre polynomial** of the instance. It depends on a only through a scalar when d = 0 (then P is the
honest limit w → 1, which is independent of the direction a). When d > 0 it is homogeneous of degree d in a, and the data
shows it is then c-free (§3).

**Reduction.** If HP holds, then X(c) ≢ 0 for all allowed instances and all integers c > U, by Lemma E(iii). With
Prop Z (lower inclusion) and Theorem W⁺ (c ≤ −1) this gives Z^A_N = [0, 2N−4] and Z^C_n = [0, 2n−2] for all N, n. In
particular, HP replaces (SC) together with the whole peel/certifier apparatus.

Remark (why this is not circular). The certifier proves X(c) ≠ 0 one chamber at a time, and each chamber can tie at the
edge. The centre polynomial is one object per instance, and HP⁺ certifies all real c ≥ U+1 at once.

## 3. Computation

Engines:
- type C: `eng.py` (exact Fractions, formula (D));
- type A: `mpq.py`, which is `prove247/mp.py` with exact ℚ in place of ℤ/p, plus the transverse-residue series.

In `hpCx.py` and `hpA3x.py`, the c-free parts of each summand are computed once per instance. The procedure:
- evaluate at δ ∈ {1, 2, 4}·10^{−20};
- second-order Richardson extrapolation of value/δ^d;
- rationalise (denominator ≤ 10⁹);
- exact interpolation on dim + 4 points;
- **consistency check at three further c (U+1, U+2, U+3)**, all exact.

The certificate is HP⁺, the one-sign test (Descartes) on P(U+1+t), in exact arithmetic (`desc.py`).

| type, size | allowed | chk pass | **HP⁺ pass** | notes |
|---|---|---|---|---|
| C, n = 3 | 115 | 115 | **115** | `hpC3x.txt` |
| C, n = 4 | 726 | see below | see below | `hpC4x_{0,1}.txt` |
| A, N = 3 | 25 | 25 | **25** | Z^A_3 = {2}: the only root above 0 is c = 2 = U, at (∅,∅,[3]) |
| A, N = 4 | 408 | 408 | **408** | `hpA4x.txt` |
| A, N = 5 | 5578 | see below | see below | `hpA5x_{0,1,2}.txt` (3 shards) |

(The table is completed in §3.1 when the runs finish.)

Float pre-runs (`hpe.py`, `hpA2.py`, numpy root-finding) agree. One float false alarm (C n=4, (∅,∅,{1,3,4}), "integer
zero at 7") was a degree-8 fit artefact. Exactly, P = c(c−1)(c−2)²(c−3)(c−4)(3c²−5c+6)/80640, with max real part 4 < 6
(`chk7.py`). Exact evaluation of X at c = 7 at a random point is 91.04… ≠ 0.

**The polynomials at C n = 3, λ = μ = ∅** (`hpf3.txt`):

| κ | P(c) |
|---|---|
| {1} | c/2 |
| {2} | c²/4 |
| {3} | c(c−2)(2c+1)/24 |
| {1,2} | c(c−1)(c−2)/24 |
| {1,3} | c²(c−1)(c−2)/48 |
| {2,3} | c(c−1)(c−2)(c²−2c+2)/240 |
| {1,2,3} | c(c−1)(c−2)²(c−3)(c−4)/2880 |

The last is Cor. Δ (Weyl dimension of C₃ at weight (c/2, c/2−1, c/2−2)). Roots are not always rational (1 ± i at {2,3}),
but every real part is ≤ U. The edge instances, with a root exactly at U, are the window's witnesses.

**Structure** (exact runs `hpC3x.txt`, `hpC4x_*.txt`, type C). With e := |λ| + |μ| − |κ|:
- **d − deg P = e in every case** (115/115 at n=3, 726/726 at n=4).
- Generically (113/115 and 705/726) d = max(e, 0). The 2 + 21 exceptions have d and deg both one higher. Examples:
  - (3),(3),{1,2,3} at e = 0;
  - (4),(4),{2,3,4} at e = −1;
  - (1,2,3),(1,2,3),{1,2,3,4} at e = 2.
  These are the cases where the expected non-equivariant constant vanishes.
- Reading: in X(c)(ε) = Σ q_{jk} c^k ε^j, only j − k ≥ e occurs (c always enters as cε). The centre polynomial contains
  the pure top piece j − k = e. This is the cohomological (Duistermaat–Heckman-type) limit, and e is the expected
  codimension defect.
- For e ≥ 1, P is mostly c-free. The 4 exceptions at n=4 are linear in c, and each has its single root ≤ U. So
  **over-determined instances essentially never vanish**, which is consistent with every known window zero being
  transversal.

### 3.2 Richardson pieces and the product decomposition (type C, `brion.py`)

Non-equivariantly, F_λF_μ = Σ_ν c^ν_{λμ}(1)F_ν, where c^ν_{λμ}(1) = lim_{w→1} C(λ,μ,ν;0). By linearity of ℓ_κ,
P^κ_{λμ} = const·Σ_ν c^ν_{λμ}(1)P^κ_{∅ν} whenever all orders are 0.
- **Decomposition:** this holds in 29/29 cases at n=3 and 230/230 at n=4, with a constant ratio, as it must.
- **Richardson positivity (HP_R):** for every ν ≤ κ, P^κ_{∅ν}(U+1+t) has **all coefficients positive**: 35/35 at n=3,
  126/126 at n=4.
- **Structure-constant signs:** (−1)^{|ν|−|λ|−|μ|}c^ν(1) > 0 holds in 18/19 cases at n=3 and 103/113 at n=4. The exceptions
  start with (2)·(2) → (2,3), coefficient +1. So F is not literally Brion-signed. This matches K0, which identified GQ with
  φ⁰ = Ψ_{κ,0}, not with F.

Consequence: HP⁺ for general (λ,μ) does **not** follow termwise from HP_R, because the c^ν alternate. HP_R is the clean
special case (one Richardson-type variety per instance). The product case needs a genuine one-sign argument for an
alternating sum, as in the geometric picture with Z a triple intersection.

### 3.1 Completion of the runs

(Appended at the end of the session; see the bottom of this file.)

## 4. The geometric reading (hunch; why HP⁺ should be true)

Lemma Δ says ℓ_[n](f) = K_n Σ_L f(L)(−1)^{|L^c|}V(y^L). Since V(y^L)/Δ is the product of the inverse tangent factors at the
fixed point L of LG(n,2n), this is the Atiyah–Bott formula. So ℓ_[n] is K_T-integration on LG(n,2n), up to normalisation.
Consequences, all consistent with what we already proved:
- C(∅,∅,[n];c) is the Weyl character of weight (c/2 − n)ω_n, i.e. χ(LG, O(a)) with a = c/2 − n. The window [0, 2n−2] is
  −(n+1) < a < 0, the **Kodaira strip** of a Fano variety of index n+1. The symmetry c ↔ 2n−2−c of Cor. Δ is
  O(a) ↔ K ⊗ O(−a), i.e. **Serre duality**. Odd c are formal half-integral twists.
- In general X(c) should be χ_T of O(c/2 − ·) tensored with a fixed class on a Richardson-type Z = X_κ ∩ gX^λ ∩ g′X^μ,
  with dim Z = −e. That is exactly deg P. P is then its Hilbert polynomial. P(0) = 0 for λ = μ = ∅ ≠ κ is the acyclicity of
  a boundary-ideal sheaf. HP⁺ would be the statement that the Hilbert polynomial is one-signed above its last root, which
  vanishing theorems (Frobenius splitting) give at even c.
- Dictionary test, P^κ(c) = χ(X_κ, O(c/2 − #κ)):
  - **passes** for κ = [n] (Weyl);
  - **passes** for κ = {1} (P¹: m+1);
  - **passes** for κ = {2} (quadric cone: (m+1)²);
  - **passes** for κ = {1,2} = LG(2,4) = Q³ ((m+1)(m+2)(2m+3)/6);
  - **fails** for κ = {3}: P never takes the value χ(O_Z) = 1. With the boundary ideal sheaf instead, {3} passes and {2}
    fails.
  With the rule χ(X_κ, O(c/2 − #κ)), {2,3} also passes (value 1 at m = 0), but {1,3} fails (value 2). So the twist and
  normalisation dictionary is not pinned. The likely culprit: F_κ = w^{2r}Ψ_{κ,(κ_j−2j)} carries a **κ-dependent twist**
  θ_j = κ_j − 2j, while K0 only identified the *untwisted* Ψ_{κ,0} with GQ. If twisted Ψ = GQ·[line bundle depending on κ],
  each F_κ is a structure sheaf tensored with its own line bundle, and no single global shift can fit. This is the untested
  "θ ≠ 0" item of PROVE 249 (K1) and the next test (K1′ below).

Owners, all unread first-hand this session (no browsing):
- Ikeda–Naruse 1112.5223 (GQ represents LG Schubert classes; K0 says Ψ_{κ,0} = GQ);
- Brion's positivity paper and Brion–Kumar (Frobenius-splitting vanishing on Schubert/Richardson varieties);
- the Kodaira-strip/Golyshev literature for root locations.

I do not cite any of them as support for a grade.

## 5. Gaps (precise)

1. **HP is unproved.** It is the only remaining gap for the all-N upper end (inherited Motegi root aside). It supersedes
   (SC): HP ⇒ conclusion, by Lemma E.
2. The centre-polynomial computation is numerical-then-exact. Rationalisation is not a proof that the rational value is the
   true limit. The three extra exact checks make an error implausible, but the grade is computed.
3. Odd c: the geometric reading only covers even c (honest line bundles). HP⁺ covers odd c as a polynomial statement, but a
   geometric proof would need a separate argument for half-integral twists.
4. K1′ (new, replaces K1/K2): pin the dictionary X(c) = χ_T(Z; 𝓛_c ⊗ 𝓕) by testing {3} vs {2} at n = 3, 4 against the
   Ikeda–Naruse identification. Then prove HP⁺ at even c by vanishing and h⁰ > 0, and at odd c by an interlacing or
   positivity argument.
