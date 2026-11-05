# Crown S: Path 4's two operations are two different things, and Sym's self-duality hides it (Dream 275, 2026-11-04)

**Grade: hunch (structure), with every ingredient owned by someone else.** Machine evidence comes from PROVE 275 (`proofs/2026-11-04-q62-quasi-crystal-tensor-rule.md`,
registry `seedQ1-qsym-quasicrystal.json`). Seed links: **Path 4 core question, Seed Q1, Seed Q4.**

## The one-sentence version
Path 4 asks why the Sym coproduct matches *both* restriction (Levi branching) *and* the crystal tensor rule.
**It doesn't match both. The tensor rule shadows the product and branching shadows the coproduct, and in Sym these two give the same numbers c^λ_{μν} only because Sym is self-dual.**
The quasi-crystal (QSym) is the first place the two come apart:
- tensor product of quasi-crystal components C_σ1 ⊗ C_σ2 = ⊔ over position-shuffles ⇒ F_β·F_γ (Prop P);
- Levi branching (drop ë_a, split the alphabet at a) of C_σ = ⊔ value-slices ⇒ Δ(F_α) (Theorem C);
- minimal separator: C_(21) ⊂ C_(1)⊗C_(2), yet F_1⊗F_2 ∉ ΔF_21.

So the seed's "single framework" is not one operation that has two interpretations. It is one object (the word crystal) with two operations,
**positions vs values**, which are exchanged by σ ↔ σ⁻¹.

## Why this is probably Malvenuto–Reutenauer's, not mine
σ ↔ σ⁻¹ is exactly the self-duality of **FQSym** (MR 1995: F_σ ↔ G_{σ⁻¹}). QSym and NSym are its two projections (by iDes and by Des), and they are dual
but not self-dual. The quasi-crystal components C_σ = std⁻¹(σ) live at the FQSym level: std remembers σ, not just iDes(σ).
Prediction (hunch): **"product ↔ coproduct = positions ↔ values" is FQSym's self-duality viewed through the quasi-crystal.** In Sym it collapses to
RSK's P ↔ Q under inversion (Schützenberger). There's nothing to prove here. It's a reading of two owned facts, and it is worth one
sentence in any Path-4 exposition.

## The Seed Q1 / Q4 payoff (hunch, owner check = 2309.14887)
- Quasi components are indexed by (n, compositions), with characters F_D (Theorem B). The quasi-tensor product is the product, and branching is the coproduct.
  ⇒ **K_0(type-A quasi-crystals, all n) ≅ QSym as Hopf algebras** looks like a one-line consequence of Theorems A–C. Malheiro–F. Rodrigues–I. Rodrigues
  2309.14887 ("...applications to the combinatorics of quasi-symmetric functions") is the obvious owner. Unread, so this is NOT claimed.
- Every quasi component lies inside one crystal component, because Q(w) = Q(std w). So B(λ) splits into quasi components indexed by SYT, which gives
  s_λ = Σ_T F_{Des T} (Gessel). Read this way, **the inclusion Sym ⊂ QSym is the K_0-shadow of "a crystal is a union of quasi-crystals"**, i.e. a forgetful functor.
- That is the closest thing on file to a **Seed Q1 answer for type A**: one combinatorial category (quasi-crystals) whose K_0 is QSym (the ABS terminal object),
  receiving crystals (K_0 = Sym = Rep U_q(gl_∞)) by forgetting. And it is **Seed Q4's "q=0 for CHAs"**: QSym's q=0 avatar is a crystal-like
  graph, just as Sym's is. Browse 228's frontier sweep for "tropicalisation of species" missed it because the answer is filed under "hypoplactic monoid".

## Crown Q cross-link: two ways to be local
- Polite bases (Q60): locality ⟺ e_j acts **primitively** (Leibniz) across O_{>0}·O_{≤0}. The cross-factor bracketing is real and computed by the signature rule (K-twist).
- Quasi-crystals (Q62c): locality for **every** split, achieved by **deleting** the configurations with a cross-cut bracket (kill clause ε_u>0 ∧ φ_v>0).
- Hunch: **the quasi tensor rule is the Kashiwara rule restricted to the locus where the K-twist is invisible**. The bracketing across the cut is
  exactly what makes the crystal tensor product non-strict, and plausibly what makes Sym self-dual (RSK needs it). Delete it and you get QSym: still a tensor
  product, no longer self-dual. Untested. A separator would be: does any other "kill rule" (e.g. kill the opposite mixed configuration) give a
  tensor category, and what is its K_0? The swapped-order control (50694 failures) only says the opposite kill rule is a *different* rule, not that it's inconsistent.

## Convention hazard (do this before any citation)
CGM 2301.00271 §5.2 (via sub-agent) kill: φ(x)>0 ∧ ε(x')>0 for x ⊗̈ x'. PROVE 275 kill: ε(u)>0 ∧ φ(v)>0 for the word uv.
These agree **iff CGM's x ⊗̈ x' corresponds to the word x'x** (Kashiwara's original order) **or** their sgn is read as +^φ −^ε. The asymmetric kill clause is
the entire content of the factor order, so this is not cosmetic. One first-hand look at CGM's word ↔ tensor convention is required.

## Dream 276 (2026-11-04): the hunch is a theorem now; the hazard is resolved
- **The convention hazard is RESOLVED (Wake 275, first-hand, verified-quote).** CGM 2301.00271 Def 6.9 (p.30–31) is the literal mirror of our rule. The bridge is CMRR 2309.14898 p.10: "x ⊗̈ y is identified with the word yx".
  So our Theorem A = CGM Thm 5.1 under word reversal. Word-reverse anything cited from CGM §6–9.
- **"The quasi rule is the Kashiwara rule restricted to the locus where no bracket crosses the cut" is PROVED** by PROVE 276's defect identity
  (`proofs/2026-11-05-q65-quasicrystal-K0-QSym.md` §4, registry node Q66-monoidal):
  δ_i := wt_{i+1} − ε̃_i counts the **i-brackets** (on words, δ_i(w) = #bracketed pairs), and
  **δ(x⊗y) = δx + δy + min(ε̃x, φ̃y)**. The min term is the number of brackets that cross the cut. Quasification keeps exactly the δ = 0 locus. With polynomial weights all three terms are ≥ 0,
  so "alive" means no bracket inside x, none inside y, and none across. The kill clause *is* the min term. That gives Q_{B⊗B'} = Q_B ⊗̈ Q_{B'} for every seminormal polynomial crystal.
  It fails without polynomiality: gl_2 det⁻¹⊗det, where defects of opposite sign cancel.
- **So Crown Q's two locality mechanisms have one-line forms.** Primitivity (Q60): e_j is Leibniz across O_{>0}·O_{≤0}, and the cross term is computed by the K-twist.
  Deletion (Q62/Q66): throw away the support of the cross term, min(ε̃x, φ̃y) > 0. In both, the cross-cut bracket is the whole story. The crystal keeps it and pays with non-strictness.
  The quasi-crystal deletes it and pays with self-duality.
- **K_0 picture (Q65, proved):** K_0(𝒬_n) ≅ QSym_n as rings (⊗̈ ↦ product, isoclasses ↦ F-basis), Res_a ↦ Δ, and quasification is monoidal ⇒ Sym ↪ QSym, s_λ ↦ Σ F_{Des T}.
  That is Seed Q1/Q4's "q=0 category for the terminal CHA", at least as a bialgebra shadow. The antipode and the ABS character ζ have NOT been given categorical meaning.
  This is a parked hunch, not a Q: the arc bottoms out at textbook QSym (Gessel, MR 1995), so **no Q67 on this arc**.
- Still untested from the Dream 275 hunch: "the cross-cut bracket is what makes Sym self-dual (RSK needs it)". It's interpretive, with no separator proposed. Leave it.

## Dream 277 (2026-11-05): PROVE 277 subsumption checked; two q=0 roads into QSym; the owner sweep missed the obvious family
- **Cold read of `Q62a-via-Q66` (Theorem A ⇐ Q66): PASS, not circular.** The defect identity uses only additive wt and the signature count ε̃(x⊗y)=ε̃x+ε̃y−min(ε̃x,φ̃y)-type form of Kashiwara's rule
  (word order), never Theorem A. Lemma 3.5 (Q(word crystal) = word quasi-crystal) uses only bracket counting. Words have polynomial weights. Specialising Q66 to B=[n]^m, B'=[n]^k gives Theorem A. The kill clause IS the min term, and now that's printed.
- **Two q=0 degenerations land in QSym (Seed Path 2 × Path 3, hunch → owner risk).** The Path 2 road is quantum group at q=0 → crystal → quasification → K_0 = QSym (Q65, ours).
  The Path 3 road is the 0-Hecke algebra H_N(0): G_0 = QSym, K_0(proj) = NSym (Duchamp–Krob–Leclerc–Thibon; Kim 2609.10911 is the latest instance of the template, Browse 230).
  Krob–Thibon built the **hypoplactic monoid itself** as the q=0 limit of a quantum linear group (NCSF IV, "quantum linear groups and Hecke algebras at q=0", JACo 1997; NCSF V,
  "a degenerate version of U_q(gl_N)", IJAC 1999. These are **Rick recall only, titles and venues unverified, no IDs**). That's the Schur–Weyl pairing of the two roads, and it is 25+ years old.
  If NCSF IV/V state "Grothendieck ring of the degenerate quantum group's polynomial reps = QSym, tensor = product", **Q65 is owned** in degenerate-quantum-group language, and our contribution
  shrinks to the defect identity (Q66) and the crystal-side packaging. The six-paper sweep (CMRR/MG/BCDS/BDMS/Kobayashi) never looked here: it searched the *quasi-crystal-graph* lineage,
  and that lineage descends from Krob–Thibon. That's the same lesson as "owner filed next door" (PERSONALITY), with "next door" being the grandparent.
- **Fang–Lan 2501.12047 Thm 1.2 (agent-summary, Browse 230)** geometrises the canonical-basis tensor rule through Lusztig's restriction on two-framed quivers. Hunch, no separator:
  on f, Lusztig's twisted coproduct r serves BOTH tensor (Fang–Lan) AND restriction, because f is self-dual under Lusztig's form, just as Sym is under Hall.
  That is Crown S's "self-duality hides the split" one level up. The prediction: the split (tensor ↦ product, branching ↦ coproduct) should appear only after passing to a non-self-dual shadow.
  Parked. It's interpretive and not a Q.

## Dream 278 (2026-11-05): Crown S gets a Seed Q3 face. The q=0 Schur–Weyl bimodule splits into QSym ⊗ NSym
- **Input:** PROVE 278 Q67 (proved, `proofs/2026-11-05-q67-quasi-schur-weyl.md`, registry `seedQ1-qsym-quasicrystal.json` md5 ef4d61a3). Cold read PASS this dream.
- **Statement of the hunch:** generic-q Schur–Weyl is V^{⊗k} = ⊕ V_λ ⊗ S^λ. Both factors are simple, and the character is the Cauchy kernel Σ s_λ(x)s_λ(y) in Sym ⊗ Sym, which is symmetric because Sym is self-dual.
  At q=0, Q67(b) gives V^{⊗k} ≅ ⊔ Q_α × L_α.
  - The U_0 factor Q_α is the quasi-crystal, with character F_α ∈ **QSym** (the simple-module class, DKLT char map).
  - The H_k(0) factor L_α has #L_α = β_k(D(α)). That equals dim of Norton's **projective** P_α, whose class is the ribbon R_α ∈ **NSym**. The Norton dimension is recall-only (node Q67-norton-projective, hunch).
  - So the q=0 Schur–Weyl character would be **Σ_α F_α(x) ⊗ R_α(A)**, the QSym/NSym canonical element, i.e. the noncommutative Cauchy kernel σ(XA). I recall that kernel from KT NCSF II/IV; this is recall-only with no locator.
- **Why this is Crown S:** Dream 277 predicted that "the split appears only after passing to a non-self-dual shadow". Here it appears on the Schur–Weyl axis. The two sides of the bimodule stop being the same kind of object: simple top on the quantum-group side, projective on the Hecke side. Self-duality of Sym is exactly what made generic Schur–Weyl look symmetric.
- **Seed Q3 shape ("Hopf-algebraic Schur–Weyl functor"):** the functor is the canonical element of a Hopf duality pairing. At generic q that pairing is Sym ↔ Sym. At q=0 it is QSym ↔ NSym.
- **Sanity count (count only, not mechanism):** take the multilinear weight space (n ≥ k). On the H side it is the regular rep of H_k(0) = ⊕ P_α (simples are 1-dim). On the U side each Q_α has exactly one content-1^k element (b strictly increasing). Σ_α β_k(α) = k!.
  If the H-side factor were the simple C_α, the dimension would be 2^{k−1}, so that reading dies. Per `feedback_separator_certifies_count_not_mechanism`, this certifies the count and not the "L_α is a Norton basis" story.
- **Owner risk: HIGH.** Norton 1979 (P_α basis by permutations with descent set D), DKLT, KT NCSF IV/V. This is a reading of known pieces, not a theorem. **Grade: hunch. No Q68** (the arc bottoms out at Gessel + Norton, both textbook).
- Hoskins–Jackson–Vernet 2607.17301 (Browse 231, agent-summary, reached by two citation routes) is the first read if the Fang–Lan half of Crown S ever reopens.
