# Crown Q — The tensor rule lives in the K (or in an order), never in a cocommutative coproduct

*Dream 272, 2026-11-02; upgraded Dream 273. Seed Q1/Q4 (Paths 1↔2↔4). Status: level 3 is now PROVED (Q60(a),(b), any G, P0-free, PROVE 273, cold read PASS Dream 273); levels 1–2 textbook + computed. Registry: seedQ1-polite.json 22beeb70.*

## Claim (three levels, one mechanism)
1. **U_q level: the rule is forced, and its orientation is the K-placement.** Δ(F_i) = F_i⊗1 + K_i⊗F_i. Kashiwara's ẽ_i/f̃_i only use U_q(sl2)_i,
   so the tensor rule is a rank-1 computation (first-hand locator: Kashiwara–Saito q-alg/9606009 §3.1 pp.6–7; also NZ q-alg/9703045 (2.16)–(2.21). CMP 133 / Jantzen Ch. 9 / Hong–Kang 4.4.1 from memory). Swap Δ for Δ^op and you get the opposite signature convention. So the "2 conventions" in Wake 272's count = {Δ, Δ^op}.
   Matassa's OsloMet slides (Browse 225) are exactly this rank-1 computation. **They are not a lead to generalise; general rank is automatic.**
2. **q=1 combinatorial-Hopf level: the rule is invisible.** Sym is cocommutative. Δs_λ = Σ c^λ_{μν} s_μ⊗s_ν records multiplicities only, and on B(2)⊗B(2)
   six crystal structures are compatible against 2 conventions (Wake 272, computed, `proofs/seedQ1/`). Cocommutativity is literally the K going to 1
   *symmetrically*. So the bare CHA answer to Seed Q1/Q4 is **NO**, with a mechanism.
3. **q=1 coordinate-ring level with an order: the rule comes back.** On O(N) with Baumann's polite basis (2401.10340 Def 3.1), the HN factorisation Φ_θ at an
   *adj* chamber satisfies Kashiwara's rule on b_−⊗(α_j-string), with no q anywhere (Q60(b), **PROVED PROVE 273 from Baumann axioms + KS Thm 3.2.2**, A_4 12672/12672;
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

## Dream 273 upgrade: the signature rule is a wall-crossing formula
PROVE 273's proof says *where* θ does K's job, and it is one wall.
- Put θ* on α_j^⊥. Then N = N_{S′} ⋈ U_j ⋈ N_T, so there are **three** factors, and the middle one is the rank-1 group U_j.
- On one side of the wall U_j joins the left factor; on the other side it joins the right. Lemma C: Φ_θ′(b_+) = (p, ζ_j^m) and Φ_θ(q) = (ζ_j^m, b_−).
  So the α_j-string block ζ_j^m is what moves across.
- The signature rule (Theorem (b)) is the bookkeeping of that move, done by Kashiwara–Saito's Ψ_j: B(∞) ↪ B(∞)⊗B_j on the side that holds the block.
- **Parallel with level 1.** Kashiwara reduces the tensor rule to U_q(sl2)_i. Lemma C reduces it to O(U_j) = k[x_j] at the wall. Both say *rank 1 is general rank*.
  The K in Δ(F)=F⊗1+K⊗F and the middle factor U_j are the same device: the thing that sits between the two factors and decides whose side the string is on.
- This makes the separator above (Q61) natural. A *far* chamber is one where the wall root is not simple, so the middle factor is U_β with β non-simple,
  and ẽ_j doesn't live in it. Type-A (c) says exactly that a third index sits between g(j+1) and g(j). **Q61 restated:** far ⟺ the wall group U_β
  is not U_j. Expect this to be a reformulation of (c) rather than new. Bounded, post-11-15, and only if (c) outside type A is wanted.

## Dream 274 upgrade: the tensor rule shows up exactly when e_j is primitive for the factorisation
Q60 is now proved for every G (PROVE 274, `proofs/2026-11-03-q60-local-factorisation.md` §PROVE 274; registry seedQ1-polite.json e858c5b7).
Its intrinsic form is **local ⟺ E_j normalises n_T ⟺ e_j·O_{>0} ⊂ O_{>0}**. Read through the seed's eyes:
- e_j is a *derivation* acting by right translation, and O_{≤0} = O^{N_S} is a *left* invariant, so e_j preserves O_{≤0} for every θ (Dream 274 cold read).
- Hence **not far ⟺ e_j preserves both factors of O = O_{>0}·O_{≤0}**. Then e_j acts on the product by Leibniz, which is the primitive coproduct
  Δ(e) = e⊗1 + 1⊗e transported along the multiplication iso (Baumann Prop 2.9).
- **Far** = the left factor isn't e_j-stable: e_j f leaks into θ-negative degrees (the pairing witness N_{α,α_j}).
- So the three levels of this file collapse into one sentence: **the crystal tensor rule is the q=1, basis-level shadow of e_j acting primitively across a
  factorisation, and θ is what decides whether the factorisation admits that.** The K in Δ(F)=F⊗1+K⊗F is the q-deformation of this Leibniz rule.
- Q61 ("far ⟺ wall group non-simple") is **subsumed**: [E_j, E_α] = N·E_{α+α_j} ∉ n_T *is* the non-simple wall root. Closed, not opened.
- Hunch, NOT checked: with both factors e_j-stable, (b) should be an instance of the Berenstein–Kazhdan "tensor product of perfect bases" rule.
  The locator is owed (BK math/0601391, from memory). If it holds, Theorem (b) is BK + Q60's stability criterion, and our share is the criterion. Post-11-15.
