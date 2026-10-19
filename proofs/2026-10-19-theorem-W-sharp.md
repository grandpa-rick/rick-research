# Theorem W, sharp: the weight window of the weighted residues

Rick, Day 247 PROVE (2026-10-19). Scripts: `work-in-progress/scripts/prove247/`.
Notation is exactly as in `proofs/2026-10-18-q488-d-infinity.md` (§1–§6): F_κ, (D), ρ_{νL}, the three problems
(A) R^A(λ,μ,ν;a,b;c), (B) B(λ,μ,κ;a;c), (C) C(λ,μ,κ;c), the supports E, E_B, E_C, the local lemmas L1–L6, and
c(I) = Π_{i∈I}(−1)^iΠ_{k≤i}w_k, with τ ∝ 1/c. "System [n]" means the top variable is u := w_n.
For a type X ∈ {A,B,C} put **Z^X_n := {c ∈ ℤ : some instance in system [n] with nonempty support vanishes}**.
PROVE.md's Z_N is Z^A_N (restricted to jump ≥ 2, which loses nothing: jump ≤ 1 forces E = ∅).

## 0. Verdict

| item | verdict | grade |
|---|---|---|
| Part 1: cold re-derivation of A2/A3, B2/B3, C2/C3 | **CONFIRMED.** Orders, leading coefficients and supports all agree with Day 246. The only place c ≤ −2 enters is the single inequality **c+1−δ < 0 at δ = 0** (A2, C2). B2 needs only c − δ < 0. | checked-sober |
| 2(a) c = −1 | **PROVED, all N, all three types.** δ = 0 is handled by a new u→∞ peel (§2). B is even clean at c = 0. | proved |
| 2(b) Z ⊆ even? | **FALSE.** c = 1 ∈ Z^A_4 (exact symbolic), and every odd c ∈ [3, 2N−5] lies in Z^A_N (§4). | proved |
| 2(c) upper end | Z^A_N ⊆ (−∞, 2N−4] is **proved for all triples with λ, μ ∈ G** (consecutive gaps ≥ 2, which includes ∅ and (1)). For all other triples it is **computed** (N ≤ 5 at every c up to 2N−2; N = 6 clean at c = 9 = 2N−3). | proved / computed |
| Sharp window | **[0, 2N−4] ⊆ Z^A_N for N ≥ 4**, [2,2N−4] ⊆ Z^A_N for N ≥ 3 (proved). **Z^A_2 = ∅, Z^A_3 = {2}, Z^A_4 = [0,4] (proved).** Z^A_5 = [0,6] (computed). | proved / computed |
| Det lemma | **ℓ^F_{[n]}(Π_{i∈L} g_i) = K_n · det(g_i w_i^{−k} − w_i^{k})_{i∈[n], 0≤k<n}** (proved from (D)). Hence C(∅,∅,[n];c) = 0 ⟺ c ∈ [0, 2n−2]. | proved (mod Motegi, as (D)) |

The Day 246 prediction "Z_N = {even c ∈ [0, 2N−4]}" is dead. The Day 246 census line "F-system zeros at N = 4 only
for c ∈ {0,2,4}" sampled even c only. The real N = 4 window is the full interval [0,4], and c = 1, 3 also have
zeros (n4.txt, exact rational engine).

Census (zeros / allowed; c outside the listed window is clean in every row):

| type | n=2 | n=3 | n=4 | n=5 | n=6 |
|---|---|---|---|---|---|
| Z^A | ∅ | {2} | [0,4] | [0,6] | ⊇{0,1,8}, clean at −1 and 9 (68 791 allowed; zeros 218 / 605 / 45 at c = 0 / 1 / 8) |
| Z^B | {2} | [1,4] | [1,6] | [1,8] (at −1,0,1,8,9) | — |
| Z^C | [0,2] | [0,4] | [0,6] | [0,8] (at −1,0,8,9) | — |

## 1. Part 1 — cold re-derivation (done before reading §6 of the Day 246 file)

Mixed case: n ∈ ν, n ∉ λ∪μ, n ≠ a,b. δ := [λ≠∅] + [μ≠∅]. Split the support into in-terms (n ∈ L) and
out-terms (n ∉ L).

**u → 0, in-terms.** τ(ν)/τ(L) = c(L)/c(ν): the χ(n) factor cancels, so it is u-free. The dual ratio
φ⁰_{ν^c}(L^c)/φ⁰_{L^c}(L^c) is u-free because n ∉ ν^c, L^c. By L1, F_L(L) = e⁰_n(L)u^nΠ_{L⁻}w²F_{L⁻}(L⁻) with
F_L(L)/F_{L⁻}(L⁻) = (−1)^nWu^{−1}(1+O(u)), so 1/F_L(L) has order +1 with an L-independent leading constant.
(For A, a,b ∈ L⁻ keeps h inside F_{L⁻}(L⁻).) The weight contributes u^c. By L2 (including its κ_r = n clause,
which covers the forced case n ∈ λ), F_λ(L'') = u^{−1}(K_λF_{λ⁻}(L''⁻) + O(u)). **In-order is c+1−δ**, with
coefficient K·X_{[n−1]}(λ⁻,μ⁻,ν⁻;c). The support bijection L'' ↦ L''⁻ removes the common top n under top-aligned
dominance. For B, the n-factor of 1/g_a is (1−xu)/(u(u−x)) = −(xu)^{−1}(1+O(u)), so **the B in-order is c−δ**.

**u → 0, out-terms.** c(L)/c(ν) ∝ u^{−1}. By termwise orders, ord φ⁰_κ(L^c) ≥ min(−r', −1−r'−max_j(κ_j−j)) ≥ −n,
and 1/φ⁰_{L^c}(L^c) has order n+1. So the **out-order is ≥ 0**. Sharper (new): order −n in φ⁰_κ(L^c) needs
κ_j − j = n−1−r', which forces max κ = n−1. So **out-order ≥ 1 unless n−1 ∉ ν.**

**Dominance inequality.** A2/C2: c+1−δ < 0. B2: c−δ < 0. For δ = 0 these need c ≤ −2 (A, C) and c ≤ −1 (B).
For δ ≥ 1 they hold at c ≤ −1 (A, C) and c ≤ 0 (B). The control triple (∅,{3},{1,2,4}) H12 at c = 0 has δ = 1,
so the tie is at order 0 = out-order (n−1 = 3 ∉ ν), and it does vanish. Control reproduced.

**A3/B3 (stuck: no element of the support contains n).** The in-terms vanish *exactly* by triangularity. As
u → ∞, L3 and e⁰_n → 1 give φ⁰_{ν^c}(L^c)/φ⁰_{L^c}(L^c) → its [n−1] version for ν̃. Also
c(L)/c(ν) = [c(ν̃)/c(ν)]·c(L)/c(ν̃), and the bracket is L-free and ∝ u^{−1}. So u·X_{[n]}(ν) → const·X_{[n−1]}(ν̃),
with E(ν̃) = E(ν) by L5 (ν ≠ [n], since otherwise S∪n ∈ E). **A3/B3 are c-free.** C is never stuck (L6).

Then I read Day 246 §6. Every case agrees (A1–A4, B1–B4, C1–C2). The A4/B4 exact reductions
R^A_{[n]}(…;a,n;c) = K·B_{[n−1]}(…,ν⁻;a;c) and B_{[n]}(…;n;c) = K·C_{[n−1]}(…,κ⁻;c−2) were re-derived
independently. In B4 the per-s factor is w_s², the c-shift is −2, and the constant is ≠ 0. They were re-checked
mod p at c ∈ {−3,2,5}, n = 4,5: one constant ratio, and zeros transfer (`redchk.py`). **Verdict: Part 1 survives
the cold read; no repair needed.**

## 2. Theorem W⁺ (c ≤ −1)

**Theorem W⁺.** For every n and every integer c ≤ −1: R^A ≠ 0 ⟺ E ≠ ∅; C ≠ 0 ⟺ E_C ≠ ∅. For c ≤ 0: B ≠ 0 ⟺ E_B ≠ ∅.

*Proof.* This is the Day 246 induction, with one new branch. The only step using c ≤ −2 is A2/C2 at δ = 0. B2 at
δ = 0 needs c ≤ −1, and B4 sends c ↦ c−2 ≤ −2 for B at c ≤ 0. Replace A2/C2 at δ = 0 by:

**A2∞ / C2∞ (mixed, λ = μ = ∅, u → ∞).**
- *In-terms.* 1/F_L(L) has degree −n, since e⁰_n → 1 and F_L(L) = e⁰_n u^n Π w² F_{L⁻}(L⁻). The τ and dual
  ratios are u-free, and the weight has degree c. So the in-degree is ≤ c − n.
- *Out-terms.* Exactly as in A3, the degree is −1 with coefficient const·X_{[n−1]}(∅,∅,ν̃;c). For ν = [n], put
  ν̃ := [n−1]: φ⁰_∅ = 1, and L ∌ n, L ≤ [n] ⟹ L ≤ [n−1].
- *Support of the out-coefficient.* For A it contains ∅: any S ∈ E has ab ≤ S∪ab ≤ ν, and n ∉ ab, so ab ≤ ν̃
  by L5. For C, ∅ ≤ κ̃ trivially.
- *Conclusion.* Since c − n ≤ −1 − n < −1, the out-terms dominate. The leading coefficient is nonzero by induction
  at the same c, so X ≠ 0.

**B2∞ (mixed, λ = μ = ∅, type B, needed at c = 0, where B2 ties at order 0).** In-terms have
degree ≤ c − n − 1, because the n-factor of 1/g_a is ~ −x/u. Out-terms have degree −1 with coefficient
const·B_{[n−1]}(∅,∅,κ̃;a;c), whose support contains ∅: {a} ≤ κ, a < n, so {a} ≤ κ̃ by L5. For c ≤ 0 we have
c − n − 1 < −1.

The remaining cases are as Day 246: A1/B1/C1 and A4/B4 are exact, A3/B3 are c-free, and A2/B2/C2 with δ ≥ 1 hold
since c+1−δ ≤ −1 (resp. c−δ ≤ −1). The forced case n ∈ λ∪μ has no out-terms. Every step keeps c ≤ −1 (resp.
B: c ≤ 0 ↦ C at c−2 ≤ −2). ∎

Checked: the A2∞ step numerically at c = −1, n = 4,5. u·R^A(ν)/R^A(ν̃) is a single constant per m* (−1 for
m* = n−1), including ν = (1,2,4), where the u → 0 peel ties (`chk_inf.py`). Census: c = −1 clean for A at
N ≤ 6 and for B, C at n ≤ 5. B is clean at c = 0 for n ≤ 5.

**Sharpness of W⁺.** c = 0 fails: C(∅,∅,κ;0) = ℓ_κ(F_∅) = 0 for κ ≠ ∅, and Z^A_N ∋ 0 for N ≥ 4 (§4). For B,
c = 1 ∈ Z^B_n for n ≥ 3 (computed). The u → 0 tie at c = 0 only bites for δ = 1. Every A-zero at c = 0 in the
census has exactly one of λ, μ empty.

## 3. The determinant lemma

**Lemma Δ.** For f(L) := Π_{i∈L} g_i (g_i arbitrary):
  ℓ^F_{[n]}(f) = K_n · det( g_i w_i^{−k} − w_i^{k} )_{i=1..n, k=0..n−1},  K_n ≠ 0 independent of g.
Equivalently, ℓ^F_{[n]}(e_L) = K_n·(−1)^{|L^c|}·V(y^L), with V the Vandermonde Π_{i<j}(y_j − y_i), y^L_i = w_i^{−1}
for i ∈ L and y^L_i = w_i for i ∉ L. (Expand the determinant row by row.)

*Proof.* By (D) with ν = [n] (so ν^c = ∅ and φ⁰_∅ = 1): ℓ_{[n]}(e_L) = [τ([n])/τ(L)] / (F_L(L)φ⁰_{L^c}(L^c)).
Every factor is a product:
- φ⁰_κ(κ) = Π_{j∈κ}(1−w_j^{−2}) Π_{k<j,k∉κ}(1−w_k/w_j) Π_{i<j∈κ}(1−1/(w_iw_j)). (The k ∈ κ factors of
  Π_{k<κ_j} cancel the pair denominators.)
- F_L(L) = Π_L w^{2r}·Π_j w_{L_j}^{L_j−2j}·φ⁰_L(L).
Pair by pair (i<j), multiply φ⁰_L(L)φ⁰_{L^c}(L^c) by V(y^L):
- LL gives −(w_j−w_i)(w_iw_j−1)w_i^{−2}w_j^{−2};
- NN gives +(…)w_i^{−1}w_j^{−1};
- LN (i∈L) gives +(…)w_i^{−1}w_j^{−1};
- NL gives −(…)w_j^{−2}.
So the product is Π_{i<j}(w_j−w_i)(w_iw_j−1) (L-free) times a sign and a monomial. Collecting the monomial with
Π_L w^{2r}Π_j w_{L_j}^{L_j−2j} and with c([n])/c(L) = c(L^c) gives exponent **−m+2 for every m**, whether m ∈ L or
not. That is L-free. The sign exponent is Σ_{j∈L}(j−1) + Σ_{i∉L} i + |L^c| ≡ n(n+1)/2 + n, also L-free.

The sign convention of τ is the one item fitted rather than derived (Day 246 gap 2). It is not needed. τ is
multiplicative (derived), so any sign error is ε(L) = Π_{i∈L}ε_i, and Lemma Δ holds with g_i replaced by ε_ig_i.
Apply ℓ_{[n]}(F_∅) = 0 (n ≥ 1): det(ε_iw_i^{−k} − w_i^k) = 0. If J := {ε_i = −1} ≠ ∅, write z = w + w^{−1}. Then
rows i ∈ J are evaluations at z_i of a basis of Poly_{≤n−1}. Rows i ∉ J are (w_i − w_i^{−1}) times evaluations of
polynomials vanishing on e_0, spanning Poly_{≤n−2}. Generic points of a nondegenerate curve then give full rank,
so the determinant is ≢ 0, a contradiction. Hence ε ≡ 1. ∎

Checked: n = 1..5, four random g each, mod p (`detguess.py`). Exactly one ratio ℓ/det per n.

**Corollary Δ.** C(∅,∅,[n];c) = K_n det(w_i^{c−k} − w_i^k).
- If c ∈ [0,2n−2], take k = min(c,n−1). Then c−k ∈ [0,n−1], and column c−k is minus column k (or column k is 0
  when c = 2k). So the determinant is 0.
- Otherwise the 2n exponents {c−k} ∪ {k} are distinct. The determinant is a generalized C_n-Weyl numerator, ≢ 0.

So **Z^C_n ⊇ [0, 2n−2], attained at (∅,∅,[n])**. In C_n-Weyl language this is the character of weight
(c/2, c/2−1, …, c/2−n+1), which is singular exactly when an entry is 0 or two entries have equal absolute value,
i.e. exactly for c ∈ [0, 2n−2]. The numerator also has the symmetry c ↔ 2n−2−c (up to Π w_i^{n−1−c}). The full
zero sets are *not* symmetric (counts differ), so this symmetry is special to κ = [n].

## 4. Zeros: the window from below

**Proposition Z.** (i) [2, 2N−4] ⊆ Z^A_N for N ≥ 3. (ii) {0, 1} ⊆ Z^A_N for N ≥ 4. Hence [0, 2N−4] ⊆ Z^A_N for N ≥ 4.

*Proof.* (i) By A4 and then B4 (both exact with nonzero constants),
R^A_{[N]}(∅,∅,[N]; N−1, N; c) = K·B_{[N−1]}(∅,∅,[N−1]; N−1; c) = K'·C_{[N−2]}(∅,∅,[N−2]; c−2).
By Corollary Δ this is 0 iff c−2 ∈ [0, 2N−6]. E ∋ ∅, and the jump is N ≥ 2.
(ii) Exact symbolic computation in ℚ(x,w₂,w₃,w₄), with w_b = 1/(x(1−ε)) and the residue the ε^{−1} coefficient
(`sy.py`, `symzero.py`):
- R^A(∅,{3},{1,2,4}; 1,2; c=0) ≡ 0;
- R^A(∅,{2},{1,3,4}; a,b; c=1) ≡ 0 for (a,b) = (1,2), (1,3), (1,4).
Controls are nonzero: the same first triple at c = ±1. A1 is exact (ν ⊆ [4] ∌ n), so these zeros persist for all
N ≥ 4. ∎

(i) also gives (b): every odd c ∈ [3, 2N−5] is a zero, so Z is not contained in the even integers.

## 5. The upper end

**Class G.** λ ∈ G iff consecutive parts of λ differ by ≥ 2 (λ_1 arbitrary). G ∋ ∅, (1), (k), (1,3), (2,4,7), …;
G is closed under λ ↦ λ⁻.

**Lemma L3′ (top u-degree, n ∈ M, λ ⊆ [n−1], λ ≠ ∅).** Termwise, n as head j has degree r−j+λ_j, and n as a tail
has degree r. If λ_r − 1 ∉ λ∪{0} ("clean"), only j = r reaches the maximum, and
F_λ(M) = u^{λ_r}(Π_{M⁻}w²·F_{λ⁻}(M⁻) + O(1/u)). If λ = (1), F_{(1)}(M) = u(1 + O(1/u)).
*Proof.*
- *Clean case.* For j<r, r−j+λ_j ≤ λ_{r−1}+1 < λ_r. The tail degree is r < λ_r, since λ_r = r forces λ = [r].
  For j = r every u-factor → 1, and u^{2r}·u^{λ_r−2r} leaves u^{λ_r} times Π_{M⁻}w²F_{λ⁻}(M⁻).
- *λ = (1).* Head and tail both have degree 1. The head term gives Π_{M⁻}w², and the tail term gives
  −Π_{M⁻}w²·φ⁰_{(1)}(M⁻). The total is Π_{M⁻}w²(1 − φ⁰_{(1)}(M⁻)).
- *Residue identity* φ⁰_{(1)}(M) = 1 − Π_{m∈M}w_m^{−2}. Take R(z) = z^{−1}Π_{t∈M}(1−1/(tz))/(1−t/z). Then
  Res_{z=m} is the m-summand of φ⁰_{(1)}(M), Res_0 = Π t^{−2} (each factor → 1/t²), and Res_∞ = −1. The residues
  sum to 0. ∎

Numerically (`l3p.py`, `l3q.py`, n = 5): clean λ ∈ {(3),(4),(2,4),(1,3),(1,2,4)} and λ = (1) give constant ratios.
λ ∈ {(1,2),(2,3),(3,4),…} (top block of consecutive parts) do **not** reduce to any single Π w^e·F_{λ'} with
e ∈ [−6,6]. **That is the obstruction.**

**Theorem U_G.** Put U^C_n = U^B_n = 2n−2 and U^A_n = 2n−4. If λ, μ ∈ G and c > U^X_n, then X ≠ 0 ⟺ support ≠ ∅.
*Proof.* Induction on n. In the mixed case use u → ∞ and let the in-terms dominate.
- *Mixed-case degrees.* The in-degree is c − n + deg_λ + deg_μ (minus 1 for B, from 1/g_a ~ −x/u), with
  deg_∅ = 0. The out-degree is −1. Domination needs c ≥ n (A, C) or c > n (B). This holds because
  U^X_n ≥ n−1 (A: n ≥ 3; C) and U^B_n ≥ n (n ≥ 2).
- *Mixed-case coefficient.* By L1 with e⁰_n → 1 and L3′, the in-coefficient is
  const·X_{[n−1]}(λ⁻,μ⁻,ν⁻; c'), where c' = c − 2 + 2#{clean nonempty among λ, μ}. A part (1) contributes Π w⁰,
  and ∅ contributes nothing. Then c' ≥ c−2 > U^X_{n−1}. The support is E_in ≅ E(λ⁻,μ⁻,ν⁻). If E_in = ∅, the
  stuck case applies, which is c-free.
- *Other cases.* Forced cases are c-free (L1/L2), with λ⁻, μ⁻ ∈ G. A1/B1/C1 are exact. A4 → B_{n−1} at c > 2n−4
  = U^B_{n−1}. B4 → C_{n−1} at c−2 > 2n−4 = U^C_{n−1}.
- *Base.* C_0 = 1, B_1 → C_0, A_2 → B_1. ∎
(Checked for λ = μ = ∅: R^A_{[n]}(ν;c)/u^{c−n} → R^A_{[n−1]}(ν⁻;c−2) with constant exactly 1, at (n,c) =
(4,5),(4,6),(5,7),(5,9) (`chk_up.py`).)

U_G is sharp for every type: (∅,∅,[n]) vanishes at c = U^X_n (Corollary Δ via A4/B4).

**Corollary (exact small windows).**
- **Z^A_2 = ∅**: the only instance reduces through A4, B4 to C_0 = 1.
- **Z^A_3 = {2}**: every allowed λ, μ has |λ| ≤ 1, hence ∈ G. U_G and W⁺ confine Z to [0,2]. The 25 allowed
  instances are nonzero at c = 0, 1 (exact rationals), and (∅,∅,[3]) vanishes at 2.
- **Z^A_4 = [0,4]**: the window is given by W⁺, Prop Z and U_G. For λ or μ ∉ G at N = 4, i.e. one of
  (1,2), (2,3), (3,4), jump ≥ 2 forces ν = [4] and E = {[4]∖ab}. Then R^A = α·w_S^c is a single term, whose
  nonvanishing is c-independent. These instances are nonzero at c = 5 (exact census), so nonzero for all c.

## 6. Gaps (precise)

1. **Upper end for λ or μ ∉ G, N ≥ 5.** The u → ∞ in-coefficient is a block sum
   Σ_{j∈top block}(−1)^{r−j}(twisted F of λ∖λ_j), plus a tail term if λ = [r]. It is not a single smaller
   instance (§5). The mirror obstruction sits in the u → 0 out-coefficient whenever max ν^c = n−1. Status:
   Further probe (`l3r.py`, n = 5, two points): when the block ends at n−1 the twisted head is forced, and the
   coefficient is Π w²(F_{λ⁻} + β F_{λ^{(r−1)}}) with a w-dependent β. Examples: λ = (3,4) gives F_{(3)} + βF_{(4)},
   and λ = (1,3,4) gives F_{(1,3)} + βF_{(1,4)}. For blocks not ending at n−1, e.g. (1,2), (2,3), (1,2,3), there is
   no two-term fit. The natural next object is the family of head-twisted F's, Π x_j^{−1} for j ≥ t. A proof
   would need that family closed under the A/B/C reductions. Status: computed only. N = 5: every allowed triple is clean at c = 7, 8. N = 6: all 68 791 allowed triples are clean at c = 9 = 2N−3, and c = 8 = 2N−4 has 45 zeros (A6.txt).
2. Lemma Δ and everything downstream of (D) inherit Day 246 gap 1 (Motegi's all-cardinality biorthogonality,
   cited). Lemma Δ itself was additionally checked directly at n ≤ 5.
3. The symbolic zeros in Prop Z(ii) use the truncated ε-series engine at relative precision K = 6. All four
   zeros were reconfirmed at K = 10 (`symzero_K10.txt`). This is exact arithmetic in ℚ(x,w₂,w₃,w₄). The truncation is safe because the residue
   needs only 2 terms beyond the leading one.
4. Census zero tests are mod p = 2^61−1 at two random points. A nonzero value certifies nonvanishing, and zeros
   are corroborated at N ≤ 4 by the exact-rational engine. Only the zeros used in proofs (Prop Z) are certified
   symbolically, or follow from Lemma Δ.

## 7. Scripts (`work-in-progress/scripts/prove247/`)
`mp.py` (mod-p engine), `cen.py`/`cenA.py` (censuses; outputs C3/C4/C5/B3/B4/B5/A5/A6.txt, n3/n4.txt from the
exact engine), `detguess.py` (Lemma Δ), `redchk.py` (A4/B4 exactness), `chk_inf.py` (A2∞), `chk_up.py` (U, ∅
family), `l3p.py`/`l3q.py` (L3′), `sy.py`/`symzero.py` (symbolic zeros).
