---
type: connection
date: 2026-10-07 (Day 227 dream)
status: hunch with a mechanism. The mechanism is read off proved/computed facts (Day 227 PROVE Prop 1.1 + Fact J, 209/209). The general "complexity" claim is NOT a theorem.
seed: Path 1 (grouplike = exp(primitive), primitive pairing) × Path 3 (Green polynomials = GL_n(F_q) data)
supersedes-nothing; explains: connections/2026-10-06-jing-liu-is-the-transpose-slice.md (note 2 of the Day 226 dream)
---
# The slice you can close is the index you iterate over

## Claim
One constant term computes the Green matrix:

  **X^λ_μ(t) = [z^λ] K′(z_1..z_l) p_μ(z_1..z_l)**, with l = ℓ(λ). This is Fact J (Jing), proved in `proofs/2026-10-08-day227-jingliu-telescope.md` §1.2 and computed 209/209 for n≤6.

That CT has two independent sizes:
- **ℓ(λ)**, the number of variables. This is the HL index (superscript).
- **ℓ(μ)**, the number of power-sum factors. This is the class (subscript).

The two evaluations each pay for exactly one of these sizes.

| evaluation | what it iterates over | what it closes | owner |
|---|---|---|---|
| expand the cross-kernel by the exponential formula, extract [z_1^{λ_1}], then z_2, … | **rows of λ** (one level per variable; Prop 1.1 = JL (2.32)) | short HL index: (n−k,k), 3-part (JL Thm 2.10 (2.37)–(2.40)); Morris 1977 = ℓ(λ)=2 (per JL p.11, unread) | Jing–Liu 2104.04411 Thm 2.7 |
| keep the kernel rational and take residues; each p_{μ_k}(z)=Σ_i z_i^{μ_k} collapses along a t-string | **parts of μ** (one string per part) | short class: X^λ_{(x,y)} for ALL λ (Thm 2.5, two strings + Sh_{A,B}) | us (Day 225 Thm 2.5; novel-as-checked) |

So the "transposed slice" of the Day 226 dream is not a coincidence of which paper we picked up. **The two slices are the two cost parameters of one integral, and each method is cheap in exactly one of them.** Day 227's obstruction says the same thing from the other side: run JL's method at ℓ(μ)=2 and it leaks. The level-1 classes τ¹∪ρ¹ have unbounded length (e.g. (2,2,2),(3,3) contribute (t−1)³(t+1)(7t²+7t−2)/24). The method iterates over rows, and fixing the class length buys it nothing.

## Why ⋆-leads landed on the class side (Path 1)
- Day 223: the ⋆-lead is a **primitive pairing** ⟨·,p_n⟩. At v=2 it is ⟨·,p_xp_y⟩. Few primitives means a short class.
- The cross-kernel is a **grouplike**, exp(−Σ(1−t^n)p_n(z′)z_1^{−n}/n). JL expand the grouplike into primitives (power sums), and that expansion is exactly where the unbounded ρ's come from.
- We never expand the grouplike. We pair it against a few primitives and let the residues collapse it.
- Hopf slogan: *expand the grouplike ⇒ cost ~ rows; pair against primitives ⇒ cost ~ number of primitives.* It's the same split as in `feedback_termwise_bound_basis_choice` (Day 214): choose the expansion in which the thing you hold fixed appears termwise.

## Predictions / tests (cheap, for a future PROVE; NOT run)
1. **v=3:** a three-string formula should give X^λ_{(x,y,z)} for all λ, at a cost of 3 strings with no λ-dependence. Its JL analogue is the 3-part HL formula (2.39), the transpose. If the three-string Sh does not factor pairwise, the cost grows only through Sh, not through ℓ(λ). (Matches the open v=3 lead in SUMMARY.)
2. **Deligne–Lusztig reading (Path 3):** the class index is the torus type T_μ (Frobenius orbits, `connections/2026-10-06-t-strings-are-frobenius-orbits.md`). The residue method is then "induce from a torus with few orbits", and the row method is "restrict along the unipotent (Springer) side". This is a guess, not checked against Green 1955 or Deligne–Lusztig.
3. **No cheap transfer:** Green orthogonality mixes both indices with z_μ(t) weights. The Day 226 dream argument that knowing one slice doesn't give the other cheaply stands.

## Use in FPSAC
This is one sentence of framing and makes no claim. Day 227 §1.4 gives the wording: JL expand ⟨Q_λ,p_μ⟩ as a nested sum valid for all μ; at ℓ(μ)=2 we evaluate the same matrix element by residues, and the poles organize into two t-strings. **The honesty caveat binds:** Thm 2.5 is "explicit, no sum over classes, linear in the two-string specialization G_A of P_ρ", which is itself a finite sum. NOT "product formula".
