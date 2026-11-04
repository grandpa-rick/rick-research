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
