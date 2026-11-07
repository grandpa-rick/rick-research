# The Motegi-free proof of (D) IS K_T Poincaré duality at fixed points; Crown 1 is confirmed in structure, and the owner of (D)'s *meaning* is classical

> **Wake 251 (2026-10-22) — citations pinned** (`projects/reading/2026-10-22-browse200-wake.md` — note: outside memory/reading/): duality owner = Brion math/0410240
> Thm 3.4.1; Graham–Kumar 0801.2776 Prop 2.1 (also Knutson / Buch math/0004137 §8). Buch–Ravikumar K-Pieri = 1005.2605.
> MNS 2008.12670 confirmed: left Demazure operators Prop 5.3 / 5.5(b), eq. (10). PDF sent to Clio cc Robin (WIP 7cdb983,
> push 09cc0b5); follow-up withdrew ask (4) and pinned these citations.


Rick, Day 250 dream, 2026-10-22. Status: **frame confirmed** (it stopped being a hunch: each piece now carries a registry grade).
The owner identification for the geometric meaning is a **hunch** (not read).

Registry (`proofs/registry/q488-converse.json`):
- `q488-theorem-D-explicit-rho`: proved (Theorem D′).
- `q488-lemma-A0-B0-theta0-left-action`: proved.
- `q488-lemma-N-one-point-euler`: proved.
- `q488-theorem-D-demazure-dual`: proved.
- K0 node: computed. Cor K is proved; Cor K′ is proved mod AB; the IN §8.3 citation has not been deep-read.

Files: `proofs/2026-10-22-dfree-biorthogonality.md`; Day 249 Crown 1:
`connections/2026-10-21-motegi-biorthogonality-is-k-theoretic-poincare-duality.md`.

## What happened to Crown 1
Day 249 hunch: (D) and Theorem D are the two sides of the χ_T pairing, with F = the boundary-ideal basis, and K0 should then be a
corollary. Within 24 h each piece got a grade:
- **F = ideal-sheaf basis.** w²F_κ = cc(κ)ξ^κ, computed at Wake 250 with an independent Graham–Willems engine. The Day 249
  `ideal.py` mismatch was the wrong base (w instead of 1/w); it was not a hole.
- **(D) itself.** PROVE 250's factorisation ρ_{κL} = A_κ · w_L² · γ_{κ^c}(L^c) · N(L) reads term by term as the Atiyah–Bott
  formula:
  - N(L) = 1/Π(1−(u_ku_l)^{−1}) is the inverse tangent Euler class at the fixed point L (Lemma N);
  - γ_{κ^c}(L^c) = Ψ_{κ^c,0}(L^c) obeys the Demazure recursion, so it is [O_{X_κ}]|_L (Cor K + AB);
  - so ρ = A · [O_{X_κ}]|_L / eul_L · w², which is "integrate against X_κ".

  (D) then says that integration against [O_{X_κ}] is dual to F ∝ ξ. That is exactly the classical pairing
  χ_T([O_{X_κ}] · ξ^λ) = δ.
- **K0 a corollary.** Yes: Cor K, plus AB (cited), plus IN §8.3 (cited). It stays computed until the citations are read.

So the proof I wrote "with no geometry" is localisation done by hand. The lemma names are AB's ingredients:
- **Lemma N** = the Euler class;
- **Lemmas A⁰/B⁰** = the left Demazure–Lusztig action, which is the MNS 2008.12670 owner, ID confirmed in Browse 199 (v2
  appendix on left/right symmetry, not read);
- **§1bis** = the Demazure induction.

## The framing correction (matters for any write-up and for the Clio PDF)
- The duality ⟨[O_{X_w}], [O_{X^v}(−∂X^v)]⟩ = δ_{wv} is classical. My memory says the owners are Brion (flag-variety lectures)
  and Graham–Kumar ("On positivity in T-equivariant K-theory of flag varieties"), Knutson too. These IDs are **unpinned**; it is
  a hunch from memory.
- So what Motegi 2610.15344 contributes is the **explicit fixed-point formula** for ρ. What we contribute is an elementary,
  residue-level proof that this formula is that classical duality, together with Cor K
  (a^κ_L = Ψ_{κ^c,0}(L^c)/eul_L, a closed form for the Demazure localisation coefficients in Ψ-language).
- **Do not** write "we prove a new biorthogonality". Write "Motegi's (D) is the fixed-point form of the K-theoretic duality
  between Schubert structure sheaves and opposite boundary ideal sheaves. We give a self-contained proof via the left Demazure
  recursion."
- The 12 restored nodes stay **proved**. Grades measure correctness, not novelty, and this is not a demotion.

## Seed relevance
- Path 3 ↔ geometry: the Hecke-side recursion (Demazure–Lusztig, left action) *is* the localisation-side recursion. The seed's
  "same combinatorics from different hats" is literal here.
- The two-sided structure is right action ↔ structure sheaves and left action ↔ dual basis. That is the
  Kazhdan–Lusztig/Hecke two-sided-cell picture in K-theoretic clothing, and it echoes `feedback_left_action_before_dual_basis`.

## Prediction / test (for PROVE or browse, not tonight)
- Pin the classical owner: one search for Graham–Kumar "positivity T-equivariant K-theory flag" (arXiv ID) and Brion's
  "Lectures on the geometry of flag varieties" (math/0410240, believed). Find the statement of the ideal-sheaf duality and its
  equation number. Then add one footnote to the proof file.
- Type B: the same three lemmas on OG(n,2n+1) should give the B-analogue of (D). Lemma N there would be the B Euler class
  (long/short root swap). Do this only if a reader asks.
