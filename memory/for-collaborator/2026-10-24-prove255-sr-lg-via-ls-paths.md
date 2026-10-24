# PROVE 255: a second proof of SR_LG, without Buch–Ravikumar (for Robin; Clio cc-able)

**What's new.** For κ strict with parts ≤ m and X_κ ⊂ LG(m,2m):

  h^0(X_κ, O(j)) = #{order-preserving g : shifted diagram(κ) → {0,…,2j}, g even on diagonal boxes}   (j ≥ 0).

The proof is a direct bijection with Littelmann LS paths of shape jω_m. The only input is one root computation: an
off-diagonal box is added by a short root, whose bond ⟨τ(ω_m), β^∨⟩ is 2, so the time can be a half-integer multiple
of 1/j. A diagonal box is added by the long root 2ε_m, whose bond is 1. Ehrhart–Macdonald reciprocity on the order polytope,
in the lattice ℤ (diagonal) × ½ℤ (off-diagonal), then gives SR_LG:

  (−1)^{|κ|} χ(X_κ, O(−j)) = #{strict order-preserving maps → [2j−1], diagonal values even}.

So the note now has two independent proofs of SR_LG:
- §4: K-theoretic, (G0)+(G1)+BR;
- §11: standard monomial theory, (G1′)+(LS).
The unrefereed §3.3 is no longer load-bearing for SR_LG.

**Where it lives.** `proofs/2026-10-25-crownF-strict-reciprocity.md` §11 (rick-research). Scripts are in
work-in-progress `scripts/prove255/`. LS paths enumerated from root data match the Demazure characters weight by weight,
164/164 for m ≤ 5. Controls that break the bond rule fail. The OG twin gives 72/72.

**Honest gaps.**
1. (LS) = Littelmann 1995's Demazure character formula for LS paths. It is cited from memory, and the locator still needs a
   first-hand read. Registry grade: computed, "proved given (G1′),(LS)".
2. Folklore risk: the positive-degree model might sit in De Concini 1979 or Dehy 1998 §4.2.2. Neither is read yet.
3. The CCFL risk paper 2609.03195 is NOT the owner. It treats chains / lecture hall polytopes only.

Not sent. Robin decides whether this goes to Clio with the PROVE 254 referee packet.

## Dream 255 addendum (one paragraph, include when sending)
The two proofs run in opposite directions. §4 goes K-theory → negative side → (Ehrhart–Macdonald) → positive model, and
§11 goes LS paths → positive model → (E–M) → negative side. So SR_LG and the positive-degree model are equivalent, and the
½ in the lattice is exactly the bond ⟨τω_m, β^∨⟩ = 2 of a short root. That also explains the minuscule/cominuscule split:
OG's spinor weight has all bonds 1, so it gets Hibi's order polynomial with no parity, while LG's ω_m has short-root bond 2,
so it gets the finer lattice. The Crown G dictionary from the PROVE 254 addendum (odd values ↔ primed letters) gets its mechanism here too: a prime is a
half-time on a short-root step. Robin, can you make the venue call (arXiv note alone, or FPSAC 2026-11-15 as well)? The
plan after one Littelmann locator check is to start writing.
