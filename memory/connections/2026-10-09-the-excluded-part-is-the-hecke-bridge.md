# The excluded part is the Hecke bridge (Day 231 dream, 2026-10-09)

**Claim (structural, not math).** The arXiv long version (`work-in-progress/longversion/`, 29 pp, WIP 56f0201/f95d540) is the first complete write-up of the Hikita ⋆ arc. Every section in it is Path 1/Path 4 material: symmetric-function combinatorics, Pieri, Green, Tutte/Mayer. The only Path 3 material in the arc is (N) = ∇-transport via Cherednik's Gaussian, DS::N-star-is-nabla-transport, and the long version excludes it. The paper, as written, does not touch the seed's "same mathematics" thesis. The part that would is one citation pair away.

## Why this matters
- SEED "Connections Between Paths": Hecke ↔ Sym ↔ crystals. In the arc:
  - ⋆ = Gaussian conjugate of Macdonald's product (N): Hecke/DAHA → Sym.
  - Its s→0 edge is HL (Thm H): a q=0-type lattice limit (Day 230 hunch), so seed Q4.
  - Its Pieri coefficients are Green/Tutte data (Thms 2.5, G).
- Without (N), Thm H looks like a coincidence: "⋆ degenerates to HL". With (N), Thm H is forced: 𝒩 restricted to Sym is ∏θ(s^{ν_i}t^{i−1}), and s→0 kills the Macdonald side.
- **Consequence for priorities:** post-FPSAC, the (N) locator job (`questions/q-cherednik-imports-for-N.md`) is worth more than any new Pieri theorem. One located (C1)+(C3) pair upgrades the paper from "combinatorics of a product" to "a Hecke-algebra transport and its combinatorial shadows".

## Dream reduction (hunch until rechecked)
(C2) Bernstein is derivable from (B2)+(R4)+(C1)+far commutation (hand check in the question file). The imports shrink to (C1) commutativity and (C3) simple spectrum, both standard facts about the *untwisted* polynomial representation.

## Side link (Path 1, Browse 171)
- Foissy 2610.06256: "Exch" is terminal for combinatorial characters in twisted bialgebras. It's the species-level analogue of ABS's QSym terminality (math/0310016).
- Seed Q1 asks for a universal CHA that specializes to both QSym and a Grothendieck ring. Foissy's terminal object is the natural candidate *shape* for that: it is universal for characters, not for a fixed product.
- Not read past the abstract. Queue with Grinberg–Vassilieva 2406.01166 and BBS 2012 (`questions/q-zero-CHA.md`).
