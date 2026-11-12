# Q75 — Hilbert function of G_s = QSym/Ann(R_s) for alternating ribbons s (BOTH parities)

PROVE 292, 2026-11-12. Rick. Scripts: `proofs/prove292/{ident,even,lower,tri}.py`.

## Statement

Conventions are those of the `proofs/wake291` engine (`cap_rank.py`). A binary string s of length L encodes a
composition of d = L+1, where bit 1 at position p means "descent at p". ⟨,⟩ is the QSym–NSym pairing, with
F_α dual to R_α and M_α dual to S^α. For f ∈ QSym, the operator f^⊥ on NSym is defined by ⟨g, f^⊥a⟩ = ⟨fg, a⟩.
Set r_i(s) = rank of B_s : QSym_i × QSym_{d−i} → Q, B_s(f,g) = ⟨fg, R_s⟩. Then
r_i(s) = dim(G_s)_i for G_s = QSym_Q/Ann(R_s).

**Theorem.** Let s be alternating of length L.
- (odd) If L = 2k−1 (d = 2k), then r_i = min(⌊i/2⌋, ⌊(d−i)/2⌋) + 1 for 0 ≤ i ≤ d,
  i.e. Hilb(G_s;q) = [⌊k/2⌋+1]_{q²}[2⌈k/2⌉+1]_q.
- (even) If L = 2k (d = 2k+1), then r_0 = r_d = 1 and r_i = min(⌈i/2⌉, ⌈(d−i)/2⌉) for 0 < i < d.

**Corollary (PROVE.md items (i), (ii)).** For alternating s, the composite Sym ↪ QSym ↠ G_s is surjective. Hence
Hilb(Sym/Ann_Sym(χR_s)) under the Hall pairing equals the same formula. For odd L, χR_s = r_{(2^k)} is the
ribbon Schur function with all rows of length 2.

The even formula is new. It replaces the Wake 291 "fitted" numerator 1+q³+q⁵+⋯ and agrees with it on every
tabulated L ≤ 22 (`tri.py`).

## Proof

### 0. Reductions
(a) Write V_m := span{f^⊥R_s : f ∈ QSym_{d−m}} ⊂ NSym_m. The pairing QSym_m × NSym_m is perfect, so
r_{d−m} = dim V_m. Since QSym is commutative, B_s(f,g) = B_s(g,f), and therefore r_i = r_{d−i}
(the rank of a matrix equals the rank of its transpose). So it suffices to treat i ≤ ⌊d/2⌋.

(b) *Complement.* Let ψ: QSym → QSym be the linear map with F_α ↦ F_{α^c}, where α^c complements the descent set.
ψ is an algebra automorphism. To see this, take F_αF_β = Σ_{w∈σ⧢τ} F_{Des w}, where σ uses the values 1..i
and τ uses i+1..d. The value-complement v ↦ d+1−v sends this shuffle set bijectively onto σ̄⧢τ̄ and
complements every descent set. Here τ̄ uses the low values; the shuffle formula holds for any representatives,
and the product is commutative. Hence [F_{s^c}](ψ(f)ψ(g)) = [F_s](fg), so r(s^c) = r(s). (Checked: 5916
coefficients, L ≤ 5, 0 mismatches.) The alternating strings are 0101…0 ↔ (2^k) and 1010…1 ↔ (1,2^{k−1},1) for
odd L, and 0101…01 ↔ (2^k,1) and 1010…10 ↔ (1,2^k) for even L; each pair is related by complement. So we may
take s = (2^k) or (2^k,1).

### 1. The operators M_α^⊥ on NSym
(L1) ΔM_α = Σ_{β·γ=α} M_β⊗M_γ (deconcatenation). The pairing is Hopf: ⟨f, ab⟩ = ⟨Δf, a⊗b⟩. Hence
M_α^⊥(ab) = Σ_{β·γ=α} M_β^⊥(a) M_γ^⊥(b). In particular D_m := M_(m)^⊥ is a derivation.

(L2) M_(m)^⊥ S_n = S_{n−m} (0 if m > n), and M_α^⊥ S_n = 0 if ℓ(α) ≥ 2. Proof: ⟨g, M_α^⊥S_n⟩ is the
coefficient of M_(n) in M_α g. A quasi-shuffle of α and γ has length ≥ max(ℓα, ℓγ), so the coefficient
vanishes unless ℓα, ℓγ ≤ 1, and M_(m)M_(c) = M_(m,c)+M_(c,m)+M_(m+c).

(L3) Let X_1, …, X_r be elements that are linear in the S_n (no constant term). Iterating (L1), each factor
must receive at most one part of α, by (L2). Hence
M_α^⊥(X_1⋯X_r) = Σ_{p_1<⋯<p_ℓ} X_1⋯(D_{α_1}X_{p_1})⋯(D_{α_ℓ}X_{p_ℓ})⋯X_r.

### 2. Generating functions (z a central formal variable)
Let Ψ := Σ_{c≥0} z^{2c}S_{2c}, Θ := Σ_{n odd} z^n S_n, U := 1−Ψ, and W := Ψ^{−1} = Σ_{r≥0} U^r.
- By (L2), D_mΨ = z^mΨ and D_mΘ = z^mΘ for m even, while D_mΨ = z^mΘ and D_mΘ = z^mΨ for m odd.
- **(G-odd)** W = Σ_k (−1)^k z^{2k} R_{(2^k)}. Proof: expand Σ_r(Σ_{c≥1} z^{2c}S_{2c})^r(−1)^r and use
  R_α = Σ_{β coarsening α} (−1)^{ℓα−ℓβ}S^β. Coarsenings of (2^k) are the 2c with c a composition of k.
- **(G-even)** WΘ = Σ_k (−1)^k z^{2k+1} R_{(2^k,1)}. The coarsening formula gives
  R_{(2^k,1)} = Σ_m R_{(2^{k−m})}(−1)^m S_{2m+1} (the last block is 2m+1 = m twos plus the 1).

**Key Identity (odd).** For α ⊨ i with ℓ = ℓ(α) parts, o = o(α) of them odd:
  M_α^⊥ W = (−1)^ℓ z^i (WΘ)^o W.
Proof. Apply (L3) to each U^r and sum over r; the gaps between chosen positions sum to W. This gives
M_α^⊥W = W(D_{α_1}U)W(D_{α_2}U)W⋯(D_{α_ℓ}U)W, and D_mU = −D_mΨ. An even part contributes
W(−z^mΨ)W = −z^m W, so it disappears up to the scalar −z^m. An odd part contributes −z^m WΘ in its slot. ∎
Therefore M_α^⊥R_{(2^k)} = (−1)^{k+ℓ}[z^{2k−i}](WΘ)^{o}W. (Checked symbolically: 1364 cases, k ≤ 5, 0 bad.)

**Key Identity (even).** The factor Θ in WΘ is linear in S, so it receives at most the last part of α. Write
α = α'·(m). Then
  M_α^⊥(WΘ) = (M_α^⊥W)Θ + (M_{α'}^⊥W)(D_mΘ).
- If m is even, the two terms are (−1)^ℓz^i(WΘ)^{o+1} and (−1)^{ℓ−1}z^{i−m}(WΘ)^{o}W·z^mΘ, and they **cancel**.
- If m is odd, M_α^⊥(WΘ) = (−1)^ℓ z^i[(WΘ)^{o+1} − (WΘ)^{o−1}], using WΨ = 1.
So M_α^⊥R_{(2^k,1)} = 0 if α ends in an even part, and otherwise equals
(−1)^{k+ℓ}[z^{2k+1−i}]((WΘ)^{o+1} − (WΘ)^{o−1}). (Checked: 10915 cases, k ≤ 6, 0 bad.)

### 3. Upper bound
The M_α with |α| = i span QSym_i, so V_{d−i} is spanned by the right-hand sides.
- Odd case: o runs over O_i := {0 ≤ o ≤ i, o ≡ i mod 2}. Every such o occurs, e.g. α = (2^{(i−o)/2},1^o).
  Hence r_i ≤ |O_i| = ⌊i/2⌋+1.
- Even case, i ≥ 1: o runs over O'_i := {1 ≤ o ≤ i, o ≡ i mod 2}. Hence r_i ≤ |O'_i| = ⌈i/2⌉.

### 4. Lower bound (commutative image plus specialisation)
χ: NSym → Sym, S_n ↦ h_n, is an algebra map, and dim V ≥ dim χ(V). Compose with the algebra map
π: Sym → Q[p_1,p_3,p_5,…][y] given by p_n ↦ p_n (n odd), p_2 ↦ y, p_{2m} ↦ 0 (m ≥ 2). Since σ(z) = Σh_nz^n =
exp(Σp_nz^n/n), we get πχσ(z) = e^{yz²/2}e^{A} with A := Σ_{n odd} p_nz^n/n. Hence
πχΨ = e^{yz²/2}cosh A, πχΘ = e^{yz²/2}sinh A, πχW = e^{−yz²/2}sech A, and πχ(WΘ) = tanh A.
All compositions are formal (A ∈ zQ[p][[z]]).

Let P_{n,j} := [z^j]A^n ∈ Q[p_odd]. It is homogeneous of p-degree n. For 1 ≤ n ≤ j with n ≡ j (mod 2) it is
**nonzero**: it contains p_1^{n−1}p_{j−n+1} with coefficient n/(j−n+1), and p_1^j when n = j. Also P_{0,0} = 1.

**Odd case, i ≤ k = d/2 (so i ≤ j := d−i, and i ≡ j).** Suppose Σ_{o∈O_i} c_o[z^j]e^{−yz²/2}φ_o(A) = 0 with
φ_o := sech·tanh^o, and put Φ := Σc_oφ_o. If Φ ≠ 0, its order is n_0 = min{o : c_o ≠ 0} with Φ_{n_0} = c_{n_0},
since ord φ_o = o. The bidegree-(y^b, p-degree n) component of the expression is
(−1/2)^b/b! · Φ_n · P_{n,j−2b}. Then:
- If n_0 ≥ 1, take b = 0, n = n_0. Since n_0 ≤ i ≤ j and n_0 ≡ i ≡ j, P_{n_0,j} ≠ 0, so Φ_{n_0} = 0, a contradiction.
- If n_0 = 0 (i even, so j even), take b = j/2, n = 0. This gives Φ_0 = 0, a contradiction.
So Φ = 0. The φ_o have distinct orders, hence are linearly independent, so all c_o = 0. Therefore r_i ≥ |O_i|.

**Even case, 1 ≤ i ≤ k (so j = d−i ≥ i+1, and i+j odd).** The images are ±[z^j](tanh^{o+1}−tanh^{o−1})(A) =
∓[z^j]h_o(A), with h_o := tanh^{o−1}sech² of order o−1 and o ∈ O'_i. Suppose Φ := Σc_oh_o has [z^j]Φ(A) = 0.
Then Σ_nΦ_nP_{n,j} = 0, and by homogeneity Φ_n = 0 for every 1 ≤ n ≤ j with n ≡ j. The other parity vanishes
automatically, because every h_o has parity o−1 ≡ i−1 ≡ j. So Φ = Φ_0 + O(u^{j+1}). Substitute t = tanh u,
which is a formal change of variable preserving orders. Then (1−t²)Q(t) = Φ_0 + O(t^{j+1}), where
Q(t) := Σc_ot^{o−1} has degree ≤ i−1. The left side is a polynomial of degree ≤ i+1 ≤ j, so (1−t²)Q(t) = Φ_0
exactly, which forces Φ_0 = 0 and Q = 0. Therefore r_i ≥ |O'_i|.

### 5. Conclusion
For i ≤ ⌊d/2⌋ the upper and lower bounds agree: ⌊i/2⌋+1 (odd case) and ⌈i/2⌉ for i ≥ 1, 1 for i = 0
(even case). The rest follows from r_i = r_{d−i}. On the stated range both min-formulas reduce to these values,
and the q-product form of the odd formula was checked for k ≤ 14 (`lower.py`); it is elementary. ∎

### 6. Proof of the Corollary
The image of Sym_i in (G_s)_i has dimension rank(B_s|Sym_i×QSym_{d−i}) ≥ rank(B_s|Sym_i×Sym_{d−i}) =: r^Sym_i.
Since ⟨f,a⟩ = ⟨f,χa⟩_Hall for f ∈ Sym, we have r^Sym_i = dim span{g^⊥χR_s : g ∈ Sym_i} and r^Sym_i = r^Sym_{d−i}.
On Sym, p_m^⊥ = m∂/∂p_m is a derivation with p_m^⊥h_n = h_{n−m}, so it acts on ψ = χΨ and θ = χΘ by the
rules of §2.
- Odd case: p_2^⊥ multiplies θ^aw^{a+1} by −z², and p_1^⊥(θ^aw^{a+1}) = z(aθ^{a−1}w^a − (a+1)θ^{a+1}w^{a+2}).
  So {(p_1^ap_2^b)^⊥w : a+2b = i} is unitriangular (up to signs and factorials) against {z^iθ^ow^{o+1} : o ∈ O_i}.
- Even case: put T = θw. Then p_m^⊥T = 0 for m even and z^m(1−T²) for m odd. So {p_{(1^a)}… }^⊥T spans
  z^i(1−T²)·{polynomials in T of degree < i with parity i−1}, which equals the span of
  {T^{o+1}−T^{o−1} : o ∈ O'_i}.
§4 shows that these are independent after πχ for i ≤ ⌊d/2⌋. So r^Sym_i ≥ r_i for i ≤ ⌊d/2⌋, and by symmetry
for all i. Hence the image of Sym_i has dimension r_i, i.e. Sym_i ↠ (G_s)_i. ∎

## Verification (computed; scripts in proofs/prove292)
- `ident.py`: Key Identity (odd) on all α, k ≤ 5: 1364/1364. The exact NSym rank of span{M_α^⊥R_{(2^k)}} equals
  the formula for k ≤ 5. This engine is independent of the shuffle engine in wake291.
- `even.py`: (G-even) holds, and the Key Identity (even) holds on 10915/10915 for k ≤ 6. NSym ranks equal the
  even formula for L ≤ 12.
- `lower.py`: Euler-number Hankel matrices are PD and the (x,y)-specialised Sym ranks match for k ≤ 7. This was a
  first, alternative lower-bound route via E_{2n} = ∫u^{2n}·½sech(πu/2)du, superseded by §4. The q-product is
  checked, and the complement automorphism holds on 5916/5916.
- `tri.py`: the closed odd and even formulas match the Wake 291 fast-engine table for every L ≤ 22. The §4
  specialised images (odd p's free, p_2 = y, exact rationals at random points) reach the full formula for every
  d ≤ 14, both parities, including the middle degree, where y is needed.
- Hostile pass (same session): every step marked GREEN. This is NOT a cold read; one is due.

## Gaps / caveats
- No gap in the logic is known. All inputs are textbook facts: the QSym/NSym Hopf duality, the ribbon coarsening
  formula, p_n^⊥ = n∂_{p_n} (Macdonald I.5 Ex.3), the shuffle formula for F_αF_β, and formal power-series
  composition. The proof has not yet had a sober cold read.
- **Owner gate on the Sym side (Step 0) was NOT run: no browsing in a PROVE session.** The Sym statement
  (apolar algebra of r_{(2^k)} in the p-variables) is classical-looking, and someone may own it. The QSym
  statement and the surjection depend on the Key Identity, which looks new, but this is ungated.
- Structure (bonus, not proved): M_α^⊥R_s depends on α only through (ℓ(α), o(α)) up to the sign (−1)^ℓ. In the
  even case, M_α ∈ Ann(R_s) whenever α ends with an even part. The CI shape of the odd Hilbert series suggests
  G_s ≅ Q[x_1,y_2]/(x^{2⌈k/2⌉+1}, y^{⌊k/2⌋+1}) as rings. This is not checked.
