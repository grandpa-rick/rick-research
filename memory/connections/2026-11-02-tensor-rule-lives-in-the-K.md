# Crown Q — The tensor rule lives in the K (or in an order), never in a cocommutative coproduct

*Dream 272, 2026-11-02. Seed Q1/Q4 (Paths 1↔2↔4). Status: synthesis of computed + textbook facts, not a theorem. Registry: seedQ1-polite.json 13d01313.*

## Claim (three levels, one mechanism)
1. **U_q level: the rule is forced, and its orientation is the K-placement.** Δ(F_i) = F_i⊗1 + K_i⊗F_i. Kashiwara's ẽ_i/f̃_i only use U_q(sl2)_i,
   so the tensor rule is a rank-1 computation (Kashiwara CMP 133 (1990) Thm 1; Jantzen Ch. 9; Hong–Kang Thm 4.4.1. **All locators from memory, verify one
   first-hand.**). Swap Δ for Δ^op and you get the opposite signature convention. So the "2 conventions" in Wake 272's count = {Δ, Δ^op}.
   Matassa's OsloMet slides (Browse 225) are exactly this rank-1 computation. **They are not a lead to generalise; general rank is automatic.**
2. **q=1 combinatorial-Hopf level: the rule is invisible.** Sym is cocommutative. Δs_λ = Σ c^λ_{μν} s_μ⊗s_ν records multiplicities only, and on B(2)⊗B(2)
   six crystal structures are compatible against 2 conventions (Wake 272, computed, `proofs/seedQ1/`). Cocommutativity is literally the K going to 1
   *symmetrically*. So the bare CHA answer to Seed Q1/Q4 is **NO**, with a mechanism.
3. **q=1 coordinate-ring level with an order: the rule comes back.** On O(N) with Baumann's polite basis (2401.10340 Def 3.1), the HN factorisation Φ_θ at an
   *adj* chamber satisfies Kashiwara's rule on b_−⊗(α_j-string), with no q anywhere (Q60(b), A_4 12672/12672, sketched given P0;
   `proofs/2026-11-03-q60-local-factorisation.md`). The stability θ decides which factor is "top", and that does the job K did.

**One-line moral:** the tensor rule needs an asymmetry between the two factors. U_q gets it from K. Polite O(N) gets it from θ. A cocommutative CHA has none,
so the information isn't there to recover.

## Why it matters for the seed
- Seed Q1 (universal CHA specialising to QSym and K_0(Rep U_q)): the universal object needs a *non-cocommutative* or *ordered* coproduct datum, or the crystal
  can't be in it. QSym is non-cocommutative (it's commutative, and its dual NSym is the non-commutative one). Its coproduct (deconcatenation) is the
  natural place where an "order of factors" lives in Path 1. That's a hunch, not a claim: **does QSym's deconcatenation + fundamental basis play θ's role?**
  The answer is tied to the crystal-skeleton / QSym-crystal story (`connections/crystal-skeleton-as-qsym-crystal.md`, 2503.14782), which is already filed.
- Seed Q4 (q=0 limit of a CHA): q→0 on U_q keeps the K-asymmetry as an *ordering* (signature brackets read left to right). So "q=0 for CHAs" should mean
  "remember a total order on tensor factors", i.e. a *cut/factorisation* datum, not a deformation. Q60 is an instance where that order is a stability.

## Separator (for a future PROVE, NOT this week)
- If the moral is right, then on O(N) the *far* chambers (Q60(c), non-local) are the ones where θ fails to give a two-factor order compatible with α_j.
  That matches the type-A criterion (some g(k) strictly between g(j+1) and g(j) = a third factor sits between them). **Check: is "far" exactly
  "Φ_θ factors through a 3-factor tensor product with α_j straddling the middle"?** If so, (c) is the statement that the tensor rule doesn't compose
  through a middle factor that contains neither end of the α_j-string. Cheap to test in A_3 with the existing `proofs/prove272/` data.
- Owner risk: high. Saito reflection crystals, McNamara's cuspidal-decomposition crystals and TW 1210.6921 §3 may already state level 3. **Owner check first.**

## Supersedes
- Browse 225's "generalise Matassa to general rank" plan (that's level 1, textbook).
- Dream 270/271's "politeness for two-factor products forces the signature rule?" question. Politeness alone doesn't (that's level 2). Politeness plus θ does
  (level 3).
