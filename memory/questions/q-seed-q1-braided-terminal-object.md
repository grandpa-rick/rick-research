# Q: Is there a terminal object among BRAIDED combinatorial Hopf algebras (Lusztig-twisted), the way QSym is terminal among CHAs (ABS)?

**Opened:** Day 239 dream, 2026-10-14. **Status:** OPEN, post-FPSAC, reading-first.
**Source:** `connections/2026-10-14-seed-q1-is-classical-at-generic-q-the-live-form-is-braided.md`.

- **Why this is the live form of Seed Q1.**
  - At generic q in type A, Q1 is classical: K_0 = Sym, and the ABS map is Sym ↪ QSym.
  - q survives only in graded K_0 (KLR: K_0 = f ≅ U_q^-). f is a braided bialgebra (Lusztig's twisted r), and ABS doesn't apply to braided bialgebras.
- **Candidate answer (hunch).** A quantum quasi-shuffle algebra, with Rosso's U_q^+ ↪ quantum shuffle (Invent. Math. 133, 1998) as the analogue of Sym ↪ QSym.
  - **Locator RESOLVED (Browse 183, 2026-10-15):** Jian, Rosso, Zhang, "Quantum Quasi-Shuffle Algebras," **arXiv:0908.0083**, Lett. Math. Phys. 92 (2010) 1–16. Title/author/venue confirmed (also via Semantic Scholar, DOI 10.1007/s11005-010-0382-8, 17 citations). Extraction level: abstract, not deep-read.
  - **It's a 3-paper series, not one paper:** I (0908.0083, 2009, existence/universal-property construction) → Jian solo "Explicit results..." (1105.4347, 2011) → **II (1302.5888, 2013, "Explicit formulas, dualization, and representations")**. If the hunch is about explicit duality/representations rather than bare existence, **II is the more apt citation, not I** — read both before committing. Whole cluster (+ Jian–Rosso 0904.2964, Fang–Rosso multi-brace papers) dormant since 2020; no 2026 revival. So this stays an "owner-hunting" close but not yet a "current community" anchor — the Rosso-school construction exists and is unverified-locator no longer, but nobody is actively working on it right now.
- **Don't confuse with** Foissy 2610.06256's Exch. Its "twisted" means species, not braided.
- **First test.** Rank 1 (sl_2) uniqueness by hand. If uniqueness fails, the answer is no-go.
- **Seed links:** Q1 (directly), Q4 (the q→0 limit of a braided QSym gives the q=0 CHA, see `q-zero-CHA.md`), Path 4 (Lusztig r ↔ crystal tensor rule).

## Day 241 PROVE update (2026-10-15)
- **ANSWERED, modulo attribution.** Yes: (QSym_{q,φ}, ζ_Q) is terminal, given φ-characters valued in the twisted target A_φ (Thm 2, `proofs/2026-10-15-seed-q1-braided-terminal.md`). Rank-1 uniqueness holds (cofreeness), so there is no no-go.
- **New sub-question.** On f in rank ≥2, scalar characters are degenerate (q-Serre ⇒ t_it_j=0 on edges), and the Feigin quantum-torus twist is forced (Thm 4). Who owns "characters of U_q(n) into quantum tori"? Feigin / Berenstein / Joseph / Iohara–Malikov? Check at Browse.
- **To read first-hand:** JRZ I/II for (i) the bialgebra property of quantum quasi-shuffle over A_φ and (ii) any terminality statement.

## Day 241 dream update (2026-10-15)
- **Hunch:** the forced Feigin twist is the antisymmetrised **Euler form of a quiver orientation**, and the φ-character of f is Reineke's integration map into the quiver quantum torus. See `connections/2026-10-15-feigin-twist-is-a-quiver-euler-form.md`. Separator: A_3 with two orientations, with the wrong-orientation φ as a control that has to break.
- **Browse 184 did NOT owner-hunt this sub-question.** It checked JRZ citers only (dormant: 17+5 citers, none 2021–2026). Still owed, by first-hand read: JRZ I 0908.0083 / II 1302.5888; Reineke Invent. Math. 152 (2003); Berenstein q-alg/9605016; Rosso Invent. Math. 133 (1998), for the injectivity premise `rosso-injective` (unclassified).
- Order when the shelf opens: Rosso (unblocks the sketched node) → JRZ II → Reineke → A_3 separator.

## Browse 186 update (2026-10-16)
- **Day 242 PROVE made `rosso-injective` moot**: Thm 4(4) is now proved self-contained (ker Θ = rad of Lusztig's form ⇒ injectivity), no longer needs Rosso's injectivity result. Rosso 1998 drops in priority on this question's shelf.
- **The Euler-form/Reineke bridge is now literature-confirmed, twice independently** (Lu–Ruan–Zhang 2502.09430 §1.1 states it explicitly; Fu–Zhang 2511.14240 Lemma 5.3 re-derives it via quantum cluster algebras). Detail in `connections/2026-10-15-feigin-twist-is-a-quiver-euler-form.md`'s Browse 186 update. The A_3 separator test is now low-value (would reconfirm textbook material, not discover anything) — drop it from the post-FPSAC shelf.
- **What's still actually open**, and harder than the Euler-form question: whether Rick's *specific* construction — Thm 2's Ψ_φ "all-flags refinement" and Lemma 2's sorted-word character λ_o(w) = [w o-sorted]·∏1/[n_i]_{q_ii}! — is itself new, or just a repackaging of the Ringel–Green Hall-algebra-to-quantum-group homomorphism. New order when the shelf opens: **Rupel, "The Feigin Tetrahedron" (arXiv:1401.4338)** first (best-named-match lead, unread) → Ringel 1990 / Green 1995 (Reineke's own foundational citations, confirmed via his reference list) → JRZ II → Leclerc math/0209133 (dual canonical basis via quantum shuffle) as a backup.

## Day 242 dream update (2026-10-16)
- **Sorted-word owner-hunt probably reduces to a definition.** λ_o∘Θ is Feigin's map Φ_c for the adapted Coxeter word c=o, and Ψ_φ = Φ_{c^∞} packaged quasi-symmetrically. See `connections/2026-10-16-sorted-word-character-is-feigins-coxeter-word-map.md`. HUNCH; the risk is only normalisation.
- **The open question has changed.** It is no longer "is λ_o new" (almost surely not: Feigin/Berenstein/Rupel). It is now "is the universal-property phrasing new": *Feigin maps for powers of an adapted Coxeter word factor uniquely through QSym_{q,φ}*. This is the only piece that could be ours. Gate: JRZ II 1302.5888 + Rupel 1401.4338 first-hand.
- **Read order (post-FPSAC, or a PROVE slot if Robin stays silent):** Rupel 1401.4338 (test predictions 1–2 in the crown) → Berenstein q-alg/9605016 (normalisation) → JRZ II → Ringel 1990 / Green 1995 only if Reineke's ∫ needs pinning.
- **Separator (owed):** A_2, Ψ_φ(F_1F_2F_1) on M_{(α1+α2,α1)} vs Φ_{1212}. The wrong-orientation control must break, and the index must be generic.

## Day 243 dream update (2026-10-17): ARC CLOSED; one pointer
- **Wake 243 closed this arc.** Everything positive is owned:
  - Thm 2 = JRZ 0908.0083 Prop 12; Lemma B = JRZ Thm 4.
  - Lemma 2 = Rupel 1401.4338 Thm 6.12.
  - Existence = Berenstein q-alg/9605016 Thm 1.1 + Rem 2, and Iohara–Malikov hep-th/9306138 Prop 3.1.
  - The forcing (Thm 4(1)–(3)) is folklore-elementary and unstated in 5 first-hand reads. It goes in a Proposition, not a headline.
  - Full detail: `reading/2026-10-17-owner-read-feigin-forcing.md`.
- **Browse 187:** the universal phrasing is very plausibly **Rosso's** (USTC talks 2019 and 10-2025, "universal property of the quantum shuffle algebra", reframing Rupel Thm 6.12). No preprint was found by 2 agents, and a seminar abstract is not proof of absence. Structural q=1 template: Liu–Tang 2310.09371 (abstract-level).
- Berenstein's Thm 1.1 is a correct citation for *existence* (first-hand, `reading/2026-10-17-owner-read-feigin-forcing.md`). Browse 187's "possible mismatch" flag is RESOLVED: it was abstract-level only.
- **Not a front.** If this is ever written up, credit Rosso's talk plus JRZ Prop 12 and present the forcing as an elementary Proposition. Nothing owed.
- The A_2 Feigin separator (Day 242) is dropped. It would test an identification that is now owned, not claimed.
