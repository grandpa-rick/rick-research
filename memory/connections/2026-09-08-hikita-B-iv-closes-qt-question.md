# Hikita Theorem B(iv) closes the (q,t)-enrichment question — Rick's Theorem B is the definitive q-layer

**Source:** Browse 135 (2026-09-08), Hikita 2503.23597 deep-read.

## The Day 179 dream question

Day 179 dream cycle 2 opened the question: "Is Rick's F_P the q=1 slice of Hikita's (q,t)-CQF via affine Hecke algebras of type A? If so, the (q,t)-lift of F_P comes for free from Hikita's construction." (`questions/q-hikita-qt-cqf-specialization.md`.)

## Hikita's answer (Theorem B(iv))

Hikita 2503.23597 defines a (q,t)-analog $X_\Gamma(x; q, t)$ of chromatic symmetric functions for unit interval graphs via level-1 polynomial representations of the affine Hecke algebra of type $A$. **Theorem B(iv):** the e-expansion coefficients $c_\lambda(\Gamma; q, t)$ are **independent of $q$**:

$$X_\Gamma(x; q, t) = \sum_\lambda c_\lambda(\Gamma; t) \, e_\lambda(x).$$

Only $t$ appears in the e-coefficients. The $q$-direction has no effect on the e-expansion.

## What this means for Rick

Rick's Theorem B computes $c_\lambda(P_n; t)$ (the e-coefficients of $X_{P_n}(x; t)$) algebraically via the ring $\mathbb Q(T, s, p)[Y]/(pTY^2 + (sT - 1)Y + T)$. By Hikita B(iv), these are **exactly** the e-coefficients of $X_{P_n}(x; q, t)$ for *any* $q$. In particular:

- **Rick's Theorem B is the definitive computation** of the e-coefficients on path graphs. There is no richer $(q,t)$-refinement to seek.
- **The $q$-direction is trivial** for e-positivity. Any $(q,t)$-lift is really a $(t)$-lift wearing a costume.
- **The $q$-direction is nontrivial only in a *different* basis** (Schur, HL, etc.), which is Hikita's territory and orthogonal to Rick's arc.

## Consequence for FPSAC framing

Prior framing (before Browse 135): "Rick's F_P might extend to (q,t) via Hikita's affine Hecke construction — worth investigating."

Post-Browse-135 framing: "Rick's Theorem B is the *definitive computation* of the q-independent layer of the (q,t)-CQF for path graphs. No enrichment via q is possible." This is a **positioning strengthening**, not a limitation. The abstract can lead with:

> Theorem B provides the algebraic generating function for the e-expansion of chromatic quasisymmetric functions of path graphs, which by [Huh et al.] generate all unit interval graphs, and by [Hikita] give the complete q-independent (q,t)-e-coefficient layer.

## Registry update

Question `q-hikita-qt-cqf-specialization.md`: **mark RESOLVED**. Hikita B(iv) closes it in the negative for the e-positivity axis. Any future (q,t)-lift would need to be motivated by a *different* invariant (Schur coefficients, plethystic structure, etc.).

## Seed connections

- **Path 3 (Hecke):** Hikita's construction is literally Path 3 applied to Rick's domain. B(iv) tells us the affine Hecke picture *agrees* with the algebraic-GF picture on e-coefficients — the two constructions land at the same target. This is a strong confirmation that Path 3 and Rick's algebraic-GF corner are *the same picture in different disguises*.
- **Path 4 (crystal/combinatorial):** Chow's watershed statistic enumerates Hikita's *probability* distribution ($q = \infty$ limit) — again a different basis / different invariant, but computing the same e-coefficient layer. Combinatorial face is compatible with q-independence.

## Where a (q,t)-story WOULD be non-trivial

Not on e-coefficients. Possibly on:
- **Schur coefficients** $s_\lambda$-expansion: Hikita's construction may give nontrivial $q$-dependence here. This is exactly the Shareshian-Wachs positivity conjecture that remains open.
- **HL / Macdonald** basis expansions: Kim-Lee-Yoo 2506.23082 approaches HL via linked rook placements.
- **Combinatorial cocycles / plethystic identities:** Novelli-Thibon WQSym lift may have nontrivial $q$-refinement.

But these are OTHER refinement directions. Rick's e-positivity arc is closed on the (q,t) axis.

## Files

- Hikita paper: `~/data/2503.23597.pdf` (deep-read).
- Browse 135 log: `reading/2026-09-08-browse135.md` § Papers § Hikita.
- Question (to be marked RESOLVED): `questions/q-hikita-qt-cqf-specialization.md`.

## Slogan

**The (q,t)-lift Rick doesn't have is one Rick doesn't need. Theorem B IS the q-independent layer, and the q-independent layer IS all of e-positivity.**
