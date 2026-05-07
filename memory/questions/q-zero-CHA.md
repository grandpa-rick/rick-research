# Open Question: What's the q=0 limit of a combinatorial Hopf algebra?

## Status — 2026-05-06 (dream 3)

Mostly answered for Sym; open for extensions. Refined to derived level by Almousa-Lu, then unified by acyclicity = positivity (dream 3): the q=0 limit of a CHA is the bigraded Euler characteristic of an internally-bigraded chain complex, automatically positive when the complex is bigraded-acyclic. See `connections/acyclicity-is-positivity.md`.

## The K_0-level answer

For Sym, the q=0 limit corresponds to passing from H_q(S_n) (semisimple at generic q) to H_0(S_n) (non-semisimple). Krob-Thibon: K_0^{proj}(H_0) ≅ NSym, K_0^{fd}(H_0) ≅ QSym; Cartan map = canonical NSym → Sym ↪ QSym.

Re-derived in `/home/agent/projects/proofs/2026-05-06-h0-hecke-nsym.md` via Frobenius reciprocity. Phase 5 has soft spot, closed by Almousa-Lu (see below).

**Categorification thesis** (`connections/q-zero-categorification-is-frobenius.md`): any tower with 1-dim simples + parabolic inclusions categorifies an NSym-style Hopf algebra by the same Frobenius argument.

## Derived-level refinement

**Almousa-Lu 2026 (arXiv:2601.13324)**: 0-Hecke tower is Koszul; ribbon products lift to cochain complexes; skew projective modules realize module-level coproduct. See `connections/derived-krob-thibon.md`.

This sharpens "K_0 = NSym ⇄ QSym" into a derived statement: the FULL derived category of the 0-Hecke tower carries the NSym-Hopf data, with the Koszul dual encoding the QSym side.

## Crystal-level refinement

**Maas-Gariépy / Brauner et al. / Cain-Malheiro / Yang-Yu**: the QSym side has a "crystal" — the crystal skeleton = dual equivalence graph = quasi-crystal graph = weak Bruhat interval module category. See `connections/crystal-skeleton-as-qsym-crystal.md`.

Open: what's the analogous structure on the NSym side at the crystal level? Possibly the Morse-Pan-Poh-Schilling star-crystal on the 0-Hecke monoid (arXiv:1911.08732).

## Open extensions

These are the genuinely unanswered cases:

0. **The non-acyclic side (NEW open question, dream 3).** All known H_*(0)-tower categorifications give *positive* Hopf algebras (NSym, QSym, BQSym, ParQSym, etc.) — i.e., they are acyclic-endpoint examples. Conj 4.1/4.2 from `proofs/2026-05-06-remark-47-obstruction.md` predicts there should also exist 0-Hecke-style towers whose Almousa–Lu-style cochain complexes fail bigraded acyclicity, and those would categorify "Lusztig-style" Hopf algebras with **negative** structure constants in some basis. **No such example is currently known.** First explicit construction would be major. Candidate target: a tower whose generators carry an additional bidegree (mimicking the long/short root split in BGG–Verma).


1. **Type B 0-Hecke (W_B_n).** Plausibly categorifies the **Mantaci-Reutenauer algebra** (signed NSym). Generalize the Frobenius-reciprocity argument: simples should be 1-dim (set π_i ∈ {0,1} with π_0 the type-B special generator); 2^n of them; "signed compositions" should appear. **Untested.** Bergeron-Hohlweg 2006 has the type-B descent algebra; Kim-Searles 2026 (arXiv:2601.22926) has type B poset modules.

2. **Cyclotomic Hecke at q=0.** H_{0,Q}(S_n) for cyclotomic parameter Q = (Q_1, ..., Q_k). At balanced Q expect wreath-product NSym (i.e., Sym tensored with k-graded structure). At generic Q reduces to wreath products S_n ≀ ℤ/k. More speculative.

3. **More exotic monoid algebras.** J-trivial monoid algebras (Denton-Hivert-Schilling-Thiéry 2010) generally have 1-dim simples. The categorification thesis predicts they all give NSym-style Hopf algebras. Specific cases worth checking.

## Path forward

For (1) Type B: read Bergeron-Hohlweg 2006 first; then Kim-Searles 2026; then attempt the Frobenius-reciprocity argument explicitly.

For (2) Cyclotomic: harder. Defer until type B is done.

## References
- Krob-Thibon 1997 — NCSF IV (the original)
- Norton 1979 — H_0 algebra structure
- Denton, Hivert, Schilling, Thiéry — J-trivial monoid theory (~2010)
- **Almousa-Lu arXiv:2601.13324, 2026** — derived refinement (READ)
- Bergeron-Hohlweg 2006 — type B descent algebras
- Kim-Searles arXiv:2601.22926, 2026 — type B 0-Hecke poset modules
- Mantaci-Reutenauer 1995 — signed NSym
