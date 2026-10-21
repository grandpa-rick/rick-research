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
| **HP⁺** (one-sign form) | P(U+1+t) ∈ ℚ[t] has all nonzero coefficients of one sign and a nonzero constant term. Hence P ≠ 0 on the whole real ray c ≥ U+1, odd c included. | **computed, exact**: C n = 3 (115/115); C n = 4 (726/726); C n = 5 sample (149/149); A N ≤ 4 (25/25, 408/408); **A N = 5 (5578/5578)** |
| **HP★** (root form, strongest) | Every complex root of P has Re ≤ U, with equality only at the window-edge witnesses: type C κ = [n] with λ, μ ∈ {∅, (1)}; type A ν = [N] with λ, μ ∈ {∅, (1)}, any pair (at N=4 only λ = ∅ occurs; at N=5 all three combinations, 30 = 10 pairs × 3). So P(U+1+t) is Hurwitz-stable, which implies HP⁺. | computed (exact P, numerical roots per irreducible factor): C n=3, 4 (max Re = U, 3 edge each), C n=5 sample (max Re 6 < 8), A N=4 (12 edge), A N=5 (max Re = 6 = U, 30 edge; 872 others < U, 4676 constant) |
| **Reduction** | HP ⇒ (SC)'s conclusion: X ≠ 0 for every allowed instance and every c > U. With W⁺ and Prop Z this gives Z^A_N = [0, 2N−4] for all N ≥ 4 (N ≤ 3 is already proved), and with Cor. Δ Z^C_n = [0, 2n−2]. | **proved** (§2, given HP) |
| **Lemma G** (grading inequality, type C) | Every nonzero coefficient q_{jk} of c^kε^j in X(c)(1+aε) has j − k ≥ e. Hence d ≥ e and deg P ≤ d − e. | **proved** (§2) |
| Structure of P | **Grading law d − deg_c P = e** (equality in Lemma G), where e := \|λ\| + \|μ\| − \|κ\| (\|·\| = sum of elements). It holds in 115/115 cases at n=3 and 726/726 at n=4. Generically d = max(e,0) (113/115, 705/726); otherwise both d and deg go up by one. Also P(2k) ∈ ℤ when d = 0, and P(0) = 0 for λ = μ = ∅ ≠ κ. **Type A (per-pair normaliser):** d − deg P = \|λ\| + \|μ\| − \|ν\| + 2N − 1, for every pair (a,b): 25/25 (N=3), 408/408 (N=4), 5578/5578 (N=5). | computed (C n ≤ 4, A N ≤ 5) |
| Vertex form of (SC) | D·X (D = C_n Weyl denominator) is a Laurent polynomial. At C n=3, c ≥ U, its Newton polytope has exactly 48 = \|W(C₃)\| vertices, every vertex coefficient is ±1 (8 instances × c ∈ {4,5}). Below U it breaks: at c = −1 and c = 3 some instances have ±2 vertex coefficients, and at c = 1 vertex counts 52 and 60 occur. | computed (n=3) |
| Geometric reading | ℓ_[n] is K-theoretic integration on LG(n,2n) (Lemma Δ is the Weyl character formula). The C-window is the Kodaira strip, c ↔ 2n−2−c is Serre duality, and P is a Hilbert polynomial of a Richardson-type Z with dim Z = −e. HP⁺ would then be "Hilbert polynomial positivity above the a-invariant". | hunch (partial dictionary fails a named test, §4) |

**Headline.** (SC) asks why an iterated leading coefficient never cancels. That is the wrong question: it is a statement about
2^n·n! vertices, one Weyl chamber at a time. The right object is the *centre*. Send all w → 1 and the window problem becomes a
one-variable polynomial P(c). Its zeros are where the window lives, and above U it is one-signed in the strongest possible
sense: the Taylor coefficients at U+1 share a sign. Every allowed instance checked satisfies this, exactly, in rational arithmetic:
C n ≤ 4 (841), a C n = 5 sample (149), and A N ≤ 5 (25 + 408 + 5578 = 6011). The A count covers *all* of Z^A_5's
instances, independently of the certifier. An all-N proof of HP⁺ is a positivity theorem about a single
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

**Lemma G (grading inequality, type C).** Let a be generic: a_i ≠ 0, a_i ≠ ±a_j. Write X(c)(w(ε)) = Σ q_{jk}c^kε^j, with
X(c) = C(λ,μ,κ;c), unnormalised. Then q_{jk} = 0 whenever j < k + e, where e = |λ| + |μ| − |κ|. In particular d ≥ e
and deg P ≤ d − e.

*Proof.* "ord" is the ε-order on the curve.

(a) ord F_I(M) ≥ |I| for every M, with equality at M = I.
- By Lemma A, F_I(M) = w_M^{2r}·Σ_{H⊆M,|H|=r} S₀^M(H)·A_{I,θ}(x_H) with θ_j = I_j − 2j.
- In S₀^M(H), there are r head factors 1 − x_j^{−2} (order exactly 1) and C(r,2) pair factors 1 − 1/(x_jx_k) (order exactly
  1, since a_j + a_k ≠ 0). Each tail factor (x_j − 1/w_t)/(x_j − w_t) has order 0, a ratio of two order-1 quantities since
  a_j ≠ ±a_t.
- In A = det[F_j(x_i)]/V(x_H), column j is y^{j−1+θ_j}ρ_{I_j}(y), and ρ_{I_j}(y) = Π_{k<I_j}(1 − w_k/y) has order ≥ I_j − 1
  at y = x_i. By multilinearity, ord det ≥ Σ_j(I_j − 1). Also ord V = C(r,2) exactly.
- Each H-term therefore has order ≥ r + C(r,2) + Σ_j(I_j − 1) − C(r,2) = |I|.
- At M = I, F_I(I) = monomial·φ⁰_I(I). This is a product of r + (|I| − C(r+1,2)) + C(r,2) = |I| factors, each of exact
  order 1, so ord F_I(I) = |I|.

(b) If ord g(M) ≥ m for all M, then ord ℓ_κ(g) ≥ m − |κ|. Solve g = Σ_I ℓ_I(g)F_I triangularly along a linear extension
of ≤:
  ℓ_M(g) = (g(M) − Σ_{I<M}ℓ_I(g)F_I(M))/F_M(M).
By induction ord ℓ_I(g) + |I| ≥ m, so by (a) the numerator has order ≥ m, and the denominator has order exactly |M|.

(c) w_M^c = Σ_k (c^k/k!)·ℓ_M(ε)^k, where ℓ_M(ε) := Σ_{m∈M}log(1 + a_mε) = O(ε). So X(c) = Σ_k (c^k/k!)·ℓ_κ(g_k) with
g_k(M) = ℓ_M(ε)^kF_λ(M)F_μ(M), and ord g_k ≥ k + |λ| + |μ| by (a). Hence by (b) the c^k-part has order ≥ k + e. ∎

The data (§3) shows **equality** d − deg P = e in every case. That is, the top c-coefficient of P always lies on the
extremal line j − k = e, which is the cohomological limit. Equality is not proved. Lemma G is checked numerically for (a)
at n ≤ 4 (`ordF.py`: 0/35 and 0/126 violations, all diagonals exact).

**Reduction.** If HP holds, then X(c) ≢ 0 for all allowed instances and all integers c > U, by Lemma E(iii). With
Prop Z (lower inclusion) and Theorem W⁺ (c ≤ −1) this gives Z^A_N = [0, 2N−4] for all N ≥ 4 and Z^C_n = [0, 2n−2] for all n (with Cor. Δ). In
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
- exact interpolation on dim + 4 points (c = −2, …, dim+1);
- **over-determination check:** a correct P has degree ≤ dim, so an interpolant of degree ≤ dim means at least 3 of the
  dim + 4 exact values were *predicted* by the others. Every instance has at least 3 such redundant exact checks
  (`dim + 3 − deg`). Exactly one interpolant failed this test (degree 18 at N=5, dim 15), see below.

**Correction (found during the session).** The scripts' printed "chk" compared P at c = U+1, U+2, U+3. Those points lie
*inside* the interpolation range, so that check was vacuous. The over-determination check above is the real safeguard.
The scripts now check at c = dim+4, dim+5, dim+7, outside the range. Reruns with the corrected check reproduce identical
polynomials: C n=3 115/115, A N=3 25/25, A N=4 408/408, C n=4 726/726 (§3.1).

**The one failure.** A N=5, (a,b) = (3,4), λ = μ = (5), ν = [5], d = 5. The ε^5-values have large denominators, and the
10⁹ rationalisation garbled them into a degree-18 interpolant. It was also the lone exception to the grading law.
Recomputed (`fix1.py`) at δ = 10^{−40} and 10^{−60}, with rationalisation bounds 10^{30} and 10^{45}, giving the same
answer twice and passing three genuine out-of-range checks (c = 30, 31, 40):
P = −(29312594647/29703440000)(c − 2). That is degree 1, root 2 < U, grading law satisfied, HP⁺ passes.

The certificate is HP⁺, the one-sign test (Descartes) on P(U+1+t), in exact arithmetic (`desc.py`).

| type, size | allowed | chk pass | **HP⁺ pass** | notes |
|---|---|---|---|---|
| C, n = 3 | 115 | 115 | **115** | `hpC3x.txt` |
| C, n = 4 | 726 | 726 (over-determination) | **726** | `hpC4x_{0,1}.txt` |
| C, n = 5 | random 3% sample, 149 | 149 | **149** | `hpC5s.txt`; max Re root 6 < U = 8 |
| A, N = 3 | 25 | 25 | **25** | Z^A_3 = {2}: the only root above 0 is c = 2 = U, at (∅,∅,[3]) |
| A, N = 4 | 408 | 408 | **408** | `hpA4x.txt` |
| A, N = 5 | 5578 | 5578 (after the one recompute) | **5578** | `hpA5_all.txt`; grading law 5578/5578; max Re root = 6 = U, attained at 30 edge witnesses (ν = [5], λ, μ ∈ {∅,(1)}, all 10 pairs) |



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

**Negative control and independent cross-check** (`desc.py`, `zcmp.py`).
- *Teeth.* Centre the one-sign test at U instead of U+1. It must then fail where P(U) = 0, and it does: exactly the
  3 C n=4 edge witnesses and the 12 A N=4 edge witnesses. Centred at c = 3 for C n=4, it fails 35 times.
- *Zero sets, A N=4, c ∈ [−2, 6], all 408 instances.* I compared {X(c) ≡ 0}, computed by the *independent* mod-p engine
  `prove247/mp.py` at two random points, with {P(c) = 0}. Lemma E's direction "X(c) = 0 ⇒ P(c) = 0" has **0 violations**.
  The two sets are **equal** at c = −2, −1, 0, 1, 2, 4, 5, 6 (counts 0, 0, 1, 3, 52, 12, 0, 0), and the 1/3/52/12 match
  the Day 246 positive-control census. The only difference is c = 3: P(3) = 0 for 12 instances but X(3) = 0 for only 6 of
  them. So the centre polynomial sees the window essentially exactly. It only over-reports at an odd c, which is a formal
  half-integral twist in the geometric reading.
- *Zero sets, C n=4, c ∈ [−2, 8], all 726 instances* (`zcmpC.py`).
  - Lemma E's direction has **0 violations**.
  - The sets are equal at c = −2, −1, 2, 4, 5, 6, 7, 8, with X-zero counts 0, 0, 126, 31, 3, 3, 0, 0.
  - P over-reports at c = 0 (1 instance), c = 1 (45) and c = 3 (2).
  - Zeros stop at c = 6 = U, as Z^C_4 = [0,6] requires.

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

- **A N = 5:** 5578/5578 pass HP⁺, after the one recompute described above. Grading law d − deg P = e^A + 9: 5578/5578.
  Root maximum Re = 6 = U, attained at 30 edge witnesses. Zero sets at c = 6, 7 on the first 3417 instances match exactly:
  12 = 12 at c = U, and 0 = 0 at c = U+1.
- **C n = 5 sample:** 149/149, max Re root 6 < U = 8.
- **Reruns with genuine out-of-range checks (c = dim+4, dim+5, dim+7):** C n=3 115/115, C n=4 726/726, A N=3 25/25 and
  A N=4 408/408. Every polynomial is identical to the first run (`hpC4x_rechk_*.txt`, `hpA4x_rechk.txt`; empty diffs).
  A N=5 rests on over-determination (at least 3 redundant exact points per instance) plus the one high-precision recompute.

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
