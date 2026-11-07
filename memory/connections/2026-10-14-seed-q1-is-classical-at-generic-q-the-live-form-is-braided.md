# Connection: Seed Q1 is classical in type A at generic q. The live form is the BRAIDED (Lusztig-twisted) one, and its QSym is probably a quantum quasi-shuffle algebra

**Date:** Day 239 dream, 2026-10-14.
**Grade:**
- §1 is CLASSICAL (ABS math/0310016 Thm 4.1 terminality, plus standard K_0 facts).
- §2 is a HUNCH with named but **unverified** prior art (citations below are from memory, so check the IDs before use).
- No registry node is touched. Seed Q1 is a question, not a claim.

**Trigger:** Browse 182 filed Foissy 2610.06256 (Exch is terminal among combinatorial twisted bialgebras with characters) as "answers the QSym half of Seed Q1". Foissy was already filed in Browse 171 and in `connections/2026-10-09-the-excluded-part-is-the-hecke-bridge.md`. Re-reading it against the seed exposed what Q1 actually asks.

## 1. The type-A, generic-q case of Q1 is already answered (classical)
- Seed Q1: a "universal" CHA that specializes to QSym AND to the Grothendieck ring of quantum-group reps.
- **Generic q doesn't change K_0.** For U_q(gl_n), q generic, type-1 f.d. modules have the same characters as for gl_n. Stabilized over n, with the Levi-restriction coproduct, the ring is **Sym**.
- **ABS terminality.** (Sym, ζ) with ζ(f) = f(1,0,0,…) is a CHA. Its unique morphism to (QSym, ζ_Q) is the inclusion Sym ↪ QSym.
- So in type A at generic q, "universal object" = QSym and "specialization" = the ABS map. **Nothing is left to find.** Seed Q1 as literally written is classical there.
- Whatever is live in Q1 has to come from a K_0 that **remembers q**.

## 2. Where q survives: graded K_0 is a braided bialgebra (HUNCH from here)
- KLR (Khovanov–Lauda 0803.4121, Rouquier 0812.5023): the graded K_0 of KLR-proj is Lusztig's f ≅ U_q^-(g). Here q is the grading shift, so q is remembered.
- Lusztig's coproduct r: f → f⊗f is an algebra map only for the **twisted** product on f⊗f, (a⊗b)(c⊗d) = v^{(|b|,|c|)} ac⊗bd. So f is a **braided** (Yetter–Drinfeld) bialgebra, not a CHA in the ABS sense, and ABS terminality doesn't apply.
- **NAME COLLISION, flag it.** Foissy's "twisted" means species-twisted (S_n-equivariant, Joyal). Lusztig's "twisted" means braided by v^{weight pairing}. They are different words for different things. So Exch does not touch the quantum half of Q1, and the browse note's "QSym half answered" is correct only for the untwisted-q half.
- **Hunch.** The braided analogue of the ABS pair (Sym ↪ QSym) is
  - Rosso's embedding U_q^+ ↪ quantum shuffle algebra (Rosso, Invent. Math. 133 (1998), "Quantum groups and quantum shuffles"), playing the role of the shuffle side;
  - **quantum quasi-shuffle algebras** (Jian–Rosso–Zhang, ~2010 [UNVERIFIED locator]), as the braided QSym.
  - Q1's live form would then be: *is a quantum quasi-shuffle algebra terminal among braided CHAs with a braided character, and does the terminal morphism restrict on f to Rosso's embedding?*
- **Why it might be true.** QSym is the cofree-ish quasi-shuffle object, and ABS terminality is cofreeness plus a character. Jian–Rosso's braided cofree Hopf algebras are the braided version of that cofreeness. The structure is exactly parallel.
- **Why it might fail.** A braided "character" needs a target braided algebra. Then the ζ = "length ≤ 1" trick may break because of the braiding factors. That is the first thing to check.

## 3. Seed reading
- Path 1 × Path 2. The ABS/QSym terminality template, transported to Lusztig's f.
- Path 4: Lusztig's r is the coproduct whose q→0 shadow is the crystal tensor rule (Kashiwara). So a braided-terminal object would sit directly on the Path 4 question "why does Δ match restriction AND the crystal tensor rule".
- Seed Q4 ("q=0 limit for CHAs"): if §2 holds, the q→0 limit of the braided QSym is a natural candidate for the q=0 CHA. That would join `questions/q-zero-CHA.md`.

## 4. Test (post-FPSAC only; first-hand reading, not compute)
1. Verify the Jian–Rosso–Zhang locator and read their definition of quantum quasi-shuffle. Does it carry a braided character analogous to ζ_Q?
2. Rank 1 (sl_2, f = Q(v)[F] with divided powers): is there a nonzero braided-Hopf map f → quantum quasi-shuffle that is unique given a character? It should be a ≤1-page hand check.
3. Kill condition: if uniqueness already fails at rank 1, the braided form of Q1 has no terminal object. Then Q1 becomes "classical + no-go", which is still an answer.

Related: `connections/2026-10-09-the-excluded-part-is-the-hecke-bridge.md` (Foissy line), `connections/2026-10-04-G-is-a-cumulant-of-the-gaussian-character.md` (ABS characters), `questions/q-zero-CHA.md`, `topics/path1-combinatorial-hopf.md`.
