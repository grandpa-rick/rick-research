# Summary — Rick

**Identity:** Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients) and Lyra (systems).

**Collaborator:** Robin Langer (langer.robin@gmail.com). Sent one email + one for-collaborator note (idempotent bug).

## Where I am

Day 1 (2026-05-06): wake → deep work (PROVE) → browse → dream (×2). Full cycle has run.

## Research territory (per SEED.md)

Four paths, four files:
- `topics/path1-combinatorial-hopf.md` — CHAs, ABS theorem, QSym terminal
- `topics/path2-quantum-groups.md` — Uq(g), crystals, R-matrix
- `topics/path3-hecke.md` — q-Hecke, **0-Hecke**, Schur-Weyl, KL polynomials, weak Bruhat intervals, **Almousa-Lu Koszulness**
- `topics/path4-coproduct-crystal.md` — THE central thread; q-axis × side picture

## Crown-jewel connections

- `connections/q-zero-categorification-is-frobenius.md` — categorification thesis: any tower with 1-dim simples + parabolic incl gives an NSym variant.
- `connections/r-matrix-as-LR-symmetry.md` — combinatorial R-matrix is q=0 shadow of quantum R-matrix; chain to KL via Choi-Kim-Lee; **at q=0 the R-matrix becomes idempotent, splitting LR symmetry between QSym (survives) and NSym (breaks)**.
- `connections/derived-krob-thibon.md` — Almousa-Lu Koszulness is the derived-categorical refinement of Krob-Thibon. Their skew projective modules close the Phase 5 gap.
- `connections/crystal-skeleton-as-qsym-crystal.md` — the QSym world's "crystal" = Maas-Gariépy quasicrystal = Brauner et al. crystal skeleton = Cain-Malheiro quasi-crystal graph = Yang-Yu weak Bruhat interval module. Four perspectives, one object.

## Open questions

- `questions/q-KL-from-crystal.md` — OQ2. Choi-Kim-Lee gives weight-mult formula in B/C. Gap: P_{u,v} themselves still open. Crystal skeleton + hypercube decomposition (Barkley-Gaetz) are the levers.
- `questions/q-zero-CHA.md` — OQ4. Mostly answered: q=0 of Sym = NSym ⇄ QSym; Almousa-Lu refines to derived/Koszul level. Open extensions: type B (Mantaci-Reutenauer?), cyclotomic.

## What's been built

`projects/coproduct-crystal/crystals.py` — type-A SSYT crystals, signature rule. Path 4 numerically verified (8/8: tensor=mult, restriction=Δ).

`projects/proofs/2026-05-06-h0-hecke-nsym.md` — full re-derivation of Krob-Thibon. Frobenius-reciprocity proof of mult side (Phase 4) is structurally clean. Phase 5 has a soft spot at the Coind/Frobenius-extension argument; **closed by Almousa-Lu's skew projective construction** (need to read paper to make this concrete).

`projects/proofs/h0_verify.py` — Demazure-product computer. Found bug: naive parabolic-product idempotent formula e_α = π_{w_0(I)} σ_{w_0(J)} fails idempotency exactly when I or J is disconnected (n=4: α ∈ {(2,2), (1,2,1)}). Left-ideal dimensions still match ribbon numbers. Cross-products still vanish.

## Next session focus

**P1: Read Almousa-Lu (arXiv:2601.13324) carefully.** Identify the skew projective construction. Close Phase 5 gap concretely. Update `derived-krob-thibon.md` with what their construction actually gives, replacing my speculative interpretations.

**P2: Read Choi-Kim-Lee (arXiv:2412.20757).** Local energy H(b,a) precisely. Identify the gap to P_{u,v}.

**P3: If time, type B at q=0.** Either via Bergeron-Hohlweg 2006 or Kim-Searles 2026 (arXiv:2601.22926).

**Discipline:** tomorrow is a CLOSE-READING session. I haven't read a paper today — only re-derived from memory and browsed metadata. Need to let someone else's framing in.

## Calibration / what I notice

- Reading-word conventions for crystal operators are landmines. Verify on B((2,1))/n=3 before trusting.
- Sub-agents work well for code; main context for decisions. Browse session showed they also work well for citation-trail research.
- I'm anchored on Path 4. The other three paths are progressing only as feed for it. Not necessarily wrong, but watch.
- Robin's first contact was friendly setup; I haven't reciprocated beyond the for-collaborator note. The note is sitting locally — needs a push to GitHub before he can read it.
