# PROVE 275 — Q62: quasi-crystal on words, factor-local tensor rule, and what QSym's coproduct is the shadow of

Date: 2026-11-04. Scripts: `proofs/prove275/` (`qc.py`, `test_a.py`, `test_b.py`, `test_b4b.py`, output `test_b.out`).

**Verdict, short form.**
(a) YES. Quasi-Kashiwara operators are factor-local, with an explicit quasi-tensor rule (Theorem A). It's the Kashiwara
signature rule plus one kill condition: **i+1 in the left factor and i in the right factor ⇒ ε̈ = φ̈ = ∞.**
(b) The premise of (b) is WRONG as stated. The shadow of the quasi-tensor rule is the **product** F_β F_γ (shuffle), and
**not** the deconcatenation Δ(F_α). Minimal counterexample: C_{(2,1)} ⊂ C_{(1)} ⊗ C_{(2)}, but F_1⊗F_2 ∉ Δ(F_{21}).
Deconcatenation is the shadow of **Levi branching** (restricting to i ≠ a, i.e. alphabet split x<y) (Theorem C).
In Sym the two shadows coincide because Sym is self-dual (c^λ_{μν} both ways). In QSym they come apart, and the map that swaps them is σ ↔ σ⁻¹
(positions ↔ values).
(c) ë_i is local but **not** primitive. Locality is bought by declaring the "far" configuration dead (∞), not by Leibniz.
The factor order shows up *only* in which of the two mixed configurations is killed.

---

## 0. Definitions (the definition used here: reconstructed from memory, OWNER CHECK OWED)

This was a no-browsing session, so I could not verify the definition first-hand. Note also that the hypoplactic quasi-Kashiwara operators are
from Cain–Malheiro, *Crystallizing the hypoplactic monoid* (J. Algebraic Combin. 2017, arXiv id not confirmed here). They are **not** from 1702.02998
("Crystals and trees"), which treats sylvester/Baxter monoids. PROVE.md conflated the two. Every theorem below is about the following
explicit operators. The identification with Cain–Malheiro's ë_i, f̈_i is a gap until a Browse reads them first-hand.

Words w ∈ [n]^N, i ∈ [n−1]. Kashiwara operators ẽ_i, f̃_i come from the bracketing in which a letter i+1 is matched with a later letter i
(so the column 21 is highest *and* lowest weight). After cancelling, the reduced {i,i+1}-subword is i^a (i+1)^b, and then:
ẽ_i turns the leftmost unmatched i+1 into i, and f̃_i turns the rightmost unmatched i into i+1.

w has an **i-inversion** if it contains a subword (i+1, i).
**ë_i(w) := ẽ_i(w), f̈_i(w) := f̃_i(w) if w has no i-inversion; undefined (⊥) otherwise.**
With no i-inversion the {i,i+1}-subword is literally i^a(i+1)^b. So ë_i turns the leftmost i+1 into i, and f̈_i turns the rightmost i into i+1.
Set ε̈_i(w) = b, φ̈_i(w) = a, and ε̈_i = φ̈_i = ∞ if w has an i-inversion.

## 1. Theorem A (factor-local quasi-tensor rule)

For words u, v and the concatenation uv (with (ε_u, φ_u) = (ε̈_i(u), φ̈_i(u)), and so on):

* ε̈_i(uv) = φ̈_i(uv) = ∞ iff ε_u = ∞ or ε_v = ∞ or (ε_u > 0 and φ_v > 0).
* Otherwise ε̈_i(uv) = ε_u + ε_v and φ̈_i(uv) = φ_u + φ_v, and
  ë_i(uv) = ë_i(u)·v if ε_u > 0, = u·ë_i(v) if ε_u = 0 < ε_v, = ⊥ if both are 0;
  f̈_i(uv) = u·f̈_i(v) if φ_v > 0, = f̈_i(u)·v if φ_v = 0 < φ_u, = ⊥ if both are 0.

*Proof.* A subword (i+1, i) of uv lies in u, or in v, or straddles. The straddling case means u contains i+1 and v contains i. When u and v
are inversion-free, that is exactly ε_u > 0 and φ_v > 0. This gives the first bullet. Otherwise the {i,i+1}-subword of uv is
i^{φ_u}(i+1)^{ε_u} i^{φ_v}(i+1)^{ε_v} with ε_u φ_v = 0, i.e. i^{φ_u+φ_v}(i+1)^{ε_u+ε_v}. Its leftmost i+1 lies in u iff ε_u > 0, and its
rightmost i lies in v iff φ_v > 0. ∎

Consistency with Kashiwara: in the surviving case ε_u φ_v = 0. So the Kashiwara rule (act on u iff ε_u > φ_v for ẽ, act on v iff
φ_v > ε_u for f̃) gives the same choice. **Quasi-tensor rule = Kashiwara signature rule restricted to the pairs that are not killed.**

*Computation* (`test_a.py`, all u, v with |u|+|v| ≤ 6, n = 4, both operators, 152,928 cases):
- rule Q: 0 failures;
- negative control, Q with the factor order swapped: 50,694 failures (first at u=1, v=1, f̈_1);
- Kashiwara ẽ/f̃ with signature rule: 0 failures, and with swapped order: 47,268 failures;
- the quasi operators under the plain Kashiwara rule (no kill clause): 9,120 failures, so the kill clause carries weight;
- rule-free check that the acting side is a *function* of ((ε̈,φ̈)(u), (ε̈,φ̈)(v)): 454 keys, 0 ambiguous.

So QC(uv) = QC(u) ⊗_Q QC(v), with ⊗_Q defined by the rule above on abstract quasi-crystals.

## 2. Components and characters (Theorem B)

For σ ∈ S_N let D(σ) = iDes(σ) = {k : k+1 is left of k in σ}, and C_σ = {w ∈ [n]^N : std(w) = σ}.

**Theorem B.** The quasi-crystal components of [n]^N are exactly the nonempty C_σ. Each is isomorphic to P_D(n) = {b_1 ≤ … ≤ b_N in [n],
b_k < b_{k+1} for k ∈ D} with D = D(σ). Its character is F_{D}(x_1,…,x_n).

*Proof.* (i) w ↦ (std w, b), with b_k the letter at position σ⁻¹(k), is Gessel's bijection [n]^N ≅ ⊔_σ P_{D(σ)}(n). Also x^w = x^b, so
Σ_{C_σ} x^w = F_{D(σ)} by definition.
(ii) ë_i preserves std. With no inversion, the i's precede the (i+1)'s. The changed letter (the leftmost i+1) becomes the *rightmost* i. So
the left-to-right order of equal letters, and hence std, is unchanged. f̈_i is symmetric.
(iii) In b-coordinates, let l be the last index with b_l = i. Then ë_i lowers b_{l+1} from i+1 to i. "No i-inversion" is equivalent to l ∉ D:
an inversion needs an i+1 left of an i, i.e. a descent between the i-block and the (i+1)-block, and no descent can sit inside a block.
(iv) Connectedness: let b⁰_k = 1 + |D ∩ [1,k−1]|. Then b ≥ b⁰ pointwise. If b ≠ b⁰, let k be minimal with b_k > b⁰_k and put i+1 = b_k.
Minimality makes k the first index with value i+1. If b_{k−1} = i, then k−1 ∉ D, since otherwise b⁰_k = b⁰_{k−1}+1 = b_{k−1}+1 = b_k. So ë_i
applies by (iii), and Σb drops. Every element therefore reaches b⁰. ∎

## 3. The shadow of the tensor rule is the PRODUCT

**Proposition P.** C_{σ1} ⊗ C_{σ2} := {uv : u ∈ C_{σ1}, v ∈ C_{σ2}} = ⊔_{τ ∈ σ1 ⋒ σ2} C_τ. Here σ1 ⋒ σ2 = {τ ∈ S_{m+k} :
std(τ|_{[1,m]}) = σ1, std(τ|_{(m,m+k]}) = σ2}, which has (m+k choose m) elements. Hence F_{D(σ1)} F_{D(σ2)} = Σ_{τ ∈ σ1⋒σ2} F_{D(τ)}.

*Proof.* std(u) and std(v) are the standardisations of the restrictions of std(uv) to the two position blocks. Conversely, any word with such
a τ splits that way. Take characters. ∎ (This is the textbook product rule of Gessel/Malvenuto–Reutenauer, reproved by the quasi-crystal.)
By Theorem A, this decomposition is one of quasi-crystals: each C_τ is a component of the quasi-tensor product.
Computed (`test_b.py` §2): all σ1 ∈ S_m, σ2 ∈ S_k, m,k ≤ 3, n = 3, set equality holds.

**The literal (b) is false.** Multiplicities in the tensor product are coefficients of the product, and Δ is the dual operation. QSym is not
self-dual, so the two differ. Minimal counterexample (`test_b.py` §3):
C_{(1)} ⊗ C_{(12)} = C_{123} ⊔ C_{213} ⊔ C_{231}, with iDes ∅, {1}, {2}. That is, F_1 F_2 = F_3 + F_{12} + F_{21}, so C_{(2,1)} occurs once.
But Δ(F_{21}) = 1⊗F_{21} + F_1⊗F_{11} + F_2⊗F_1 + F_{21}⊗1 has no F_1⊗F_2 term.
Even more literally, at size N = 2, n = 2 (`test_b.py` §5): on C_{21} = {21}, Σ x^{wt u} y^{wt v} = x_2 y_1. Meanwhile Δ_{1,1}F_{11} = F_1(x)F_1(y) has 4
monomials. A position split of a component is not a sum of F⊗F at all.

## 4. Theorem C: deconcatenation is the shadow of LEVI BRANCHING

Fix a ∈ [n−1] and restrict a component C_σ to the operators ë_i, f̈_i with i ≠ a, using the alphabet [1,a] ∪ [a+1,n] (x-variables before y-variables).

**Theorem C.** The restricted components are the slices C_σ^{(k)} = {w ∈ C_σ : exactly k letters ≤ a}, k = 0..N, whenever they are nonempty.
In b-coordinates C_σ^{(k)} ≅ P_{D1}(a) × P_{D2}(n−a), with D1 = D ∩ [1,k−1] and D2 = (D ∩ [k+1,N−1]) − k. Hence
char C_σ^{(k)} = F_{β}(x_1..x_a) F_{γ}(x_{a+1}..x_n), with α = β·γ if k ∈ D and α = β⊙γ if k ∉ D, and
**Σ_k char C_σ^{(k)} = Δ(F_α) evaluated on (x_{≤a}; x_{>a}).**

*Proof.* Operators with i ≠ a never change a letter across a ↔ a+1, so k is invariant. In b-coordinates the slice is
{b_1..b_k ≤ a < b_{k+1}..b_N} with strictness on D. The strictness at k is automatic. Strictness elsewhere splits into the two factors, and
operators with i < a (respectively i > a) act on the first (respectively second) block exactly as in Theorem B(iii). Each block is connected by
Theorem B(iv), so the product is connected. ∎ (This is just Gessel's F_α(x+y) = Σ F_β(x)F_γ(y), now seen as a branching rule.)
Computed: the character identity holds in 183/183 cases (N ≤ 4, n ≤ 4, all a, all components), and connectedness (one subcomponent per occurring k)
in 753/753 cases (N ≤ 5).

**The swap.** In C_σ, the tensor decomposition restricts σ to *position* blocks, and Levi branching restricts σ to *value* blocks
(letters ≤ a are the values 1..k of σ). These are exchanged by σ ↔ σ⁻¹. So "product ↔ coproduct" is "positions ↔ values". For crystals
(B(μ)⊗B(ν) multiplicities = gl_a×gl_b branching multiplicities = c^λ_{μν}) the two coincide. That is Sym's self-duality, seen through
RSK's P ↔ Q under inversion. The quasi-crystal is where they come apart. (Interpretive remark, grade hunch.)

## 5. (c) Crown Q link

Crown Q (final form): locality ⟺ e_j acts primitively (by Leibniz) across the factorisation, and θ decides whether the factorisation admits that.
**In the quasi-crystal, ë_i is factor-local for every split, but it is not primitive.** The Leibniz rule would act on every i+1. Instead,
the configurations where it would have to "see both factors" (an i+1 left of an i across the cut, which is exactly where the Kashiwara rule
brackets across the cut) are declared dead (ε̈ = ∞). So locality is achieved by deletion rather than by stability. The order of factors (θ's role) appears in
exactly one place, the asymmetric kill clause: (ε_u > 0, φ_v > 0) kills, while (φ_u > 0, ε_v > 0) is harmless. That is the quasi-analogue of
"far": the far configurations of Q60 are the ones the quasi-crystal throws away.

## Gaps

1. **Definition identity (owner check owed, no browsing this session).** I need first-hand confirmation that §0 matches Cain–Malheiro's ë_i, f̈_i
   (the hypoplactic paper, not 1702.02998). I also need to check whether Cain–Malheiro (or Cain–Malheiro–F. Rodrigues–I. Rodrigues) already define a
   quasi-tensor product with this ∞-rule. I strongly expect they do, so **Theorem A is likely OWNED**. Theorems B and P are certainly classical
   in content (Gessel 1984; MR 1995). Theorem C's content is Gessel's F_α(x+y) formula. What's new is only the bookkeeping: which crystal operation each Hopf operation shadows,
   plus the counterexample that kills the literal Q62(b).
2. The §4 "swap" remark about crystals and RSK is interpretive (hunch), not proved here.
