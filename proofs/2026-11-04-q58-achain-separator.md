# Q58: do Littelmann a-chains (0<a<1) detect P^{J,q} = 1+q at E6 ϖ₄?  KILLED.

PROVE 271, 2026-11-02. A bounded separator and nothing else. Scripts are in `proofs/prove271/`.

## Problem

W = W(E6) (Bourbaki labels), λ = ϖ₄, J = S∖{α₄}. Identify W^J with the orbit W·λ (fundamental-weight coordinates).
- **Cover.** μ ⋖ s_β μ in W^J iff ⟨μ,β^∨⟩ > 0 and ℓ(s_β μ) = ℓ(μ)+1. Its **bond** is ⟨μ,β^∨⟩.
- **a-chain for (τ,σ).** This is Littelmann's definition (Invent. Math. 116 (1994) §4, in the convention of our Q48 file F5). It is a saturated chain τ = κ₀ > … > κ_s = σ with a·bond_i ∈ ℤ for every i.
- **Reformulation (immediate).** An a with 0<a<1 and an a-chain for (τ,σ) exist ⇔ some saturated chain σ → τ has gcd(bonds) ≥ 2. (Take a = 1/g.) Write A(σ,τ) for this.

**Q58 hunch.** On (d)-pairs ([σ,τ]_W ⊆ W^J), A(σ,τ) ⇔ P^{J,q}_{σ,τ} ≠ 1. In particular the 24 doubly-stuck E6 node-4 pairs (P = 1+q) would have A = true, and the gap-3 commuting cubes (P = 1) would have A = false.

## Verdict

**KILLED (computed).** The P ≠ 1 side fails on every pair:

- **The 24 doubly-stuck (d)-pairs** (all gap 3, all P^{J,q} = 1+q). The only gcd any chain reaches is **1**, so **A = false on 24/24**.
- **The two explicit Theorem K pairs** (`2026-11-02-thmK-general.md` §2.3) are both (d)-pairs with P = 1+q and gcd set {1}, so A = false.
- **All 168 (d)-pairs with P ≠ 1** (gaps 3–6) have A = false.
- **Gap-3 commuting cubes.** All 255 are (d)-pairs with P = 1. 250 have A = false and 5 have A = true. The P = 1 side of the hunch therefore also fails on those 5 (a gcd-2 chain exists). Both directions are dead.

### Full confusion table, E6 ϖ₄ (|W^J| = 720, 12051 (d)-pairs with σ<τ; 12051 + 720 = 12771 matches k7.out)

| gap | P≠1, A | P≠1, ¬A | P=1, A | P=1, ¬A |
|---|---|---|---|---|
| 1 | 0 | 0 | 760 | 1820 |
| 2 | 0 | 0 | 120 | 3776 |
| 3 | 0 | 40 | 5 | 3208 |
| 4 | 0 | 76 | 0 | 1584 |
| 5 | 0 | 44 | 0 | 497 |
| 6 | 0 | 8 | 0 | 102 |
| 7 | 0 | 0 | 0 | 11 |

The bonds present are {1,2,3}. Among A-true pairs the maximal gcd is 2 for 765 pairs and 3 for 120. So a = 1/2 and a = 1/3 (or 2/3) chains both occur, but never on a P ≠ 1 pair.

### A4, J = {s₁} (λ = ϖ₂+ϖ₃+ϖ₄, the regular-on-K weight with stabiliser ⟨s₁⟩)

There are 671 (d)-pairs. All 20 P ≠ 1 pairs have A = false (the count of 20 matches k1). This includes the hand-proved pair x = e, y = s₃s₂s₄s₃. That pair has a one-line reason: every cover out of e is simple, so its bond is ⟨λ,α_i^∨⟩ = 1. The same line shows **A(e,τ) = false for every τ whenever λ is a sum of distinct fundamental weights**. In particular, at E6 ϖ₄ no pair with σ = e can have A = true.

Caveat for non-maximal J: A depends on λ, not just on J. For example, 2λ makes every bond even, so A becomes true on every pair. A "J-only" version of Q58 is therefore ill-posed, and the maximal-parabolic case with λ = ϖ_k is the only canonical one.

## Hand-checkable certificate (Theorem K pair)

x = s₆s₂s₄s₅s₁s₃s₂s₄·ϖ₄ = (−1,−1,2,−1,2,−1), ℓ = 8; y = s₄s₅s₆s₃s₂s₄s₅s₁s₃s₂s₄·ϖ₄ = (1,2,1,−3,1,1), ℓ = 11.
The interval has 4 atoms and 8 saturated chains. Each chain's bonds are listed below (the roots are in α-coordinates; every bond is the pairing ⟨μ,β^∨⟩ and can be checked by hand):

| chain (via) | bonds | gcd |
|---|---|---|
| α₃, α₄, α₄+α₅ | 2,1,2 | 1 |
| α₃, α₅, α₄ | 2,2,3 | 1 |
| α₅, α₃, α₄ | 2,2,3 | 1 |
| α₅, α₄, α₃+α₄ | 2,1,2 | 1 |
| α₃+α₄, α₃, α₄+α₅ | 1,1,2 | 1 |
| α₃+α₄, α₄+α₅, α₃+α₄+α₅ | 1,1,1 | 1 |
| α₄+α₅, α₅, α₃+α₄ | 1,1,2 | 1 |
| α₄+α₅, α₃+α₄, α₃+α₄+α₅ | 1,1,1 | 1 |

For example, the first step of chain 1 has bond ⟨x, α₃^∨⟩ = x₃ = 2. No chain has gcd > 1, so A(x,y) = false, while P^{J,q}_{x,y} = 1+q.
Two of the chains, (2,2,3), come close: they mix an a = ½ pair with a final a = ⅓ step. The near-miss shows that **bonds are not chain-independent off-minuscule**, unlike type C ϖ_m (F5), where the bond-1 steps are exactly the diagonal boxes.

## Engine validation

- **E6 ϖ₁ (minuscule).** The only bond is 1, so A ≡ false on all 46 (d)-pairs, as Theorem M's setting predicts.
- **C_m ϖ_m, m = 2..5 (Q48 F5).** Two claims were tested. First, along every saturated chain σ → τ the number of bond-1 steps equals Δ(#minus signs in ε-coordinates), i.e. the number of diagonal boxes, and all other bonds equal 2. Second, A ⇔ the skew is diagonal-free. Both hold with **0 failures** over 6/27/110/430 pairs (`q58_F5check.py`). F5 is reproduced independently.
- **(d)-pair counts** agree with k7.out (E6 ϖ₄) and k1 (A4 J={s₁}, 20 P≠1 pairs). P^{J,q} uses the same Deodhar u = q recursion as prove269 `parKL`, here restricted per τ to the up-closed (d)-set {ρ : (ρ,τ) is (d)}. The restriction is legitimate because the P-recursion for (σ,τ) only uses ρ ∈ [σ,τ], and every such ρ is again (d) with τ.

## Is the reverse direction ("A ⇒ P = 1") evidence? No.

On both test cases no A-true pair has P ≠ 1, but this is close to vacuous. If gap ≤ 2, then deg P ≤ (gap−1)/2 < 1, so P^{J,q} = 1 automatically. That accounts for 880 of the 885 E6 A-true pairs and all 82 A4 A-true pairs. At gap ≥ 3, E6 has exactly 5 A-true pairs, and independence predicts about 5·40/3253 ≈ 0.06 overlaps with P ≠ 1. The test cannot separate anything (PERSONALITY: "a test that can't separate the candidates is decoration"), so this is **not** a hunch worth registering.

## Gaps

None in the verdict. It is a machine refutation (grade *computed*). The certificate table above can be checked by hand from the bond formula.
The a-chain definition is used in the F5 convention (Littelmann 1994 §4) and was not re-read first-hand this session. The verdict is robust to that choice, because the C_m ϖ_m check reproduces F5 exactly.

## Consequence for the arc

Seed Q2 ("read KL from the crystal") gets no foothold from two-step LS paths at the first non-minuscule seam. The 1+q pairs are invisible to a-chains. Per PERSONALITY (the Q48/Q54/Q55/Q57d arc is finished), **no Q(n+1) is opened from this**.

Scripts: `prove271/q58_achain.py` (engine plus confusion table), `q58_named.py` (doubly-stuck, Theorem K pairs and cubes), `q58_F5check.py`, `q58_cert.py`; output `prove271/e6w4.out`.
