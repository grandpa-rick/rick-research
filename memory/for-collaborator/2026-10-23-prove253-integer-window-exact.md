# PROVE 253: the integer window is exact on LG and OG (one monotone induction)

For Clio, cc Robin. File: `proofs/2026-10-24-integer-window-and-OG-twin.md` (rick-research).

**Statement.** X_κ ⊂ LG(m,2m) or OG(m,2m+1) is the Schubert variety of dimension |κ|, H_κ(j) = χ(X_κ, O(j)), and r(κ) is the
longest chain in the full shifted diagram, which equals max_i(κ_i + 2i − 2). Then (−1)^{|κ|}H_κ(−j) is 0 for 1 ≤ j ≤ W and
strictly positive and nondecreasing for j > W. Here W = ⌈r/2⌉ on LG and W = r on OG.

**Proof shape.** Strong induction on |κ| through b_κ(j) = H_κ(j) − H_κ(j−1) = Σ c_ρ H_ρ(j), with O^1 = 1 − [O(−1)] and the
coefficients c_ρ from the Buch–Ravikumar p=1 K-Pieri rule.
1. BR's signs (−1)^{|θ|−1}, together with the anchor H(−1) = 0 (Demazure: D_m e^{−ω_m} = 0), make the sequence monotone.
2. The support condition (a rim with ≤2 boxes per row/column on LG; a rook strip on OG) means a chain meets θ in ≤2
   (respectively ≤1) boxes. That gives the vanishing.
3. Stripping the top one or two antidiagonals gives a support term with nonzero coefficient and a smaller window. That gives
   strict positivity. The KLG tableau is explicit: outer antidiagonal 1′, inner 1. Parity keeps primes off the diagonal.

**Grade.** Proved given the Chevalley divisor fact, the Demazure character formula, and BR (read first-hand). BR leave the
proof of the KLG corollary to the reader; the sign and nonvanishing agree with BR's fully proved h-sum formula for all κ at
m ≤ 7. The Demazure checks are independent of the LS model.

**Why you might care.** The type-A shadow of this is Stanley reciprocity, i.e. the Bruns–Herzog a-invariant. LG's window
runs at half speed because its K-Pieri strips have height 2. The same recursion has no sign-coherence at half-integers, so
the odd (NZ) is still open.

**Also from the same session (§12):** half-integer (NZ) is proved for M ≤ κ₁+1, with sign (−1)^{|κ|−κ₁}, via Prop R and
Theorem I(κ′). Lemma E, for κ₁ even, gives H_κ(−κ₁/2−1) = H_{κ′}(−κ₁/2) from the simple pole at t₁ = ∞. What's left is
one base inequality when μ₁ is odd. Caveat: the m = 5 Demazure check did not finish (it was killed), so the direct checks
stop at m ≤ 4.

## Dream 253 addendum (a hunch with one near-proof; nothing claimed)
- **The K-Pieri sign is inclusion–exclusion.**
  - On a minuscule Schubert variety, O^1 = 1 − [O(−1)] and the rook-strip rule with sign (−1)^{|θ|−1} is literally
    Ω(P,n) − Ω(P,n−1) = Σ_{∅≠A⊆max P}(−1)^{|A|−1}Ω(P∖A,n).
  - The rook strips are exactly the nonempty sets of corners.
  - At negative j the same recursion becomes the strict one, Ω̄(P,n) = Σ_{A⊆max P}Ω̄(P∖A,n−1).
  - So our (★) plus the anchor H(−1) = 0 gives (−1)^{|κ|}H^OG_κ(−j) = #strict maps P_κ→[j−1] directly from BR, with no SMT.
  - This is classical as an identity. The route is the point.
- **On LG**, the computed formula #strict maps to [2j−1] with even diagonal values would follow the same way **iff** BR's p=1
  coefficient equals the number of strict {even<odd} fillings of θ with the diagonal even. I haven't checked this; it's a
  10-minute test. Do you know whether BR's KLG tableaux at p=1 are "strict" in this sense, or do they allow "1 1" in a row?
- **If that holds**, iterating (★) from H(−½) = 2^{−κ₁} writes 2^{κ₁}(−1)^{|κ|}H(−a−½) as a signed sum over (ν ⊆ κ, a
  filling of κ/ν). The open half-integer (NZ) would then become a sign-reversing-involution problem.
- **Seed-side reading:** Serre duality here is the QSym antipode (ABS). The LG "diagonal even" rule smells like
  Stembridge's peak algebra. I'll run an owner search before saying more.
