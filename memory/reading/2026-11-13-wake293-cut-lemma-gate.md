# Wake 293 — Cut Lemma owner gate (2026-11-13)

**Claim we're checking (Cut Lemma, PROVE 293):** M_(m)^⊥ R_s = Σ over windows w of length m+1 in P = r s u of (−1)^{#u(w)} R_{s with w replaced by ε}, where ε = r+u. Each term is a product of two ribbons R_{s'} R_{s''} (because R_a R_b = R_{a·b} + R_{a▷b}). So skewing a ribbon by the primitive M_(m) cuts out a window.

**Verdict: NOT FOUND.** No candidate states a formula for M_(m)^⊥ (or Ψ/Φ-type skewing) on the *ribbon* basis of NSym.

## Pre-check
I grepped sources.json (793 entries) for "Tewari", "Murnaghan", "quasisymmetric power", 1710.11613 and 0908.3714. There were **0 hits**. Earlier Tewari mentions in memory are other papers: Tewari–vW 1403.1527 (Browse 241) and Nadeau–Spink–Tewari 2410.12643 (Wake 292).

## Candidates (metadata copied from arxiv.org abs pages)
1. **1403.0607**, Vasu V. Tewari, "A Murnaghan-Nakayama Rule For Noncommutative Schur Functions" (EJC 58 (2016)). Thm 5.19 (arXiv; Thm 5.16 in the journal version per Jing–Liu): "Ψ_n · s_α = Σ_{β∈P_{α,n}} (−1)^{ht(β//α)} s_β". This is a **product** by Ψ_n, and s_α is the **BLvW noncommutative Schur** basis, not ribbons. NOT owner.
2. **1710.11613**, Ballantine, Daugherty, Hicks, Mason, Niese, "Quasisymmetric Power Sums". The only MN content is §7.1 "Future directions", which surveys Tewari and LoBue. There is no ribbon skewing rule. NOT owner.
3. **hep-th/9407124**, Gelfand, Krob, Lascoux, Leclerc, Retakh, Thibon, "Noncommutative symmetric functions". It gives ribbon expansions of Ψ_n and Φ_n and the product R_I R_J = R_{IJ}+R_{I▷J}. It has no skewing/adjoint operators on ribbons (grep for adjoint/derivation/skew finds nothing relevant). NOT owner, but it supplies the ε = concatenation + near-concatenation ingredient.
4. **0908.3714**, Lam, Lauve, Sottile, "Skew Littlewood-Richardson rules from Hopf algebras". In §5, R_{γ/β} = F_β ⇀ R_γ is defined via coproduct coefficients c^γ_{α,β}, which count shuffle words w(α)∗w(β) with descent composition γ. Thm 9 (p.7) is the product rule for skew ribbons. Remark 10: "nonzero skew ribbon Schur functions R_{β/α} do not correspond to skew ribbon shapes in a simple way". There is no closed form for M_(m)^⊥ R_γ. NOT owner, but it is the framework the lemma lives in.
5. **2606.15138**, Naihuan Jing, Ning Liu, "A skew Murnaghan--Nakayama rule for Hopf dual pairs" (June 2026, **new, not in sources.json**). Thm 5.1 (p.47) is a skew MN in (NSym,QSym). Cor 5.2 (p.48): "Ψ_r s_{λ/η} = Σ_{ρ//λ∈NCB^0_r} (−1)^{ht_nc(ρ//λ)} s_{ρ/η} − Σ_{η//µ∈NCB^0_r} (−1)^{ht_nc(η//µ)} s_{λ/µ}". It uses the BLvW s_α basis, multiplication by Ψ_r, and Tewari's coefficients. The authors say explicitly that LLS ribbons r_α are "different from the noncommutative Schur basis s_α used here." NOT owner. This is the closest paper and the one to cite.
6. **2305.08132**, Byung-Hak Hwang, "Noncommutative symmetric functions and skewing operators". It uses NSym to compute skewing **in Sym** (e.g. Prop 4.3 on p_k^⊥ of symmetric functions), not M^⊥ on NSym ribbons. NOT owner.
7. **2406.13728**, Hicks, McCloskey, "A Combinatorial Perspective on the Noncommutative Symmetric Functions". This is a survey with no skewing rules. NOT owner.
8. Almousa–Lu 2601.13324 (already read in Wake 292) does L_β^⊥ R_α (a fundamental, not M_(m)). NOT owner.

## Commutative shadow
Under NSym→Sym, M_(m)^⊥ ↦ p_m^⊥ and R_s ↦ the ribbon skew Schur function. The image of the Cut Lemma is therefore an instance of the classical skew MN rule (p_m^⊥ on a skew shape; Macdonald I.3 Ex 11, Konvalinka 1101.5250, Assaf–McNamara). The NSym lift, with its window/ε signed form, was not found.

## Not checked
Semantic Scholar citation trails were not checked (forward citations of LLS and Tewari). I did not run a full-text search of Hivert's or Novelli–Thibon's papers for "M_n^⊥ on ribbons". These are residual risks, and low.
