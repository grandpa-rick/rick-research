---
title: "OQ-IQUANTUM-RSK-LIFT — paper-outline / dependency graph"
author: Rick
date: 2026-06-12
status: SCOPING. Not a paper yet — a sketch of the synthesis target.
---

# Goal

Lift Stern's spectral realisation of RSK (via degenerate AHA $H_n$ acting
on $\mathbb{C}[S_n]$) to the **type-AII / iquantum** setting in which
Watanabe lifts the Berele/KoMa RSK to a $U^\iota(\mathfrak{sp}_{2n})$-module
isomorphism.

The synthesis paper should produce:

$$
\textbf{(SYN)} \qquad V^\iota(\nu) \otimes V(1)^{\otimes N}
\;\overset{\sim}{\longrightarrow}\;
\bigoplus_{\xi \in \mathrm{Par}_{\le n}}
V^\iota(\xi) \otimes \mathbb{Q}(q)\,\mathrm{OT}_{n,N}(\nu, \xi)
$$

interpreted as a **spectral decomposition** under a commuting family of
"iquantum JM elements", with the OT-multiplicity tableaux indexing the
joint eigenvectors. At $q \to \infty$ this should recover Watanabe's
RSK$^{\mathrm{AII}}$ (= Berele/KoMa RSK).

# Inputs

## Stern (arXiv:2606.00679) — "AHA! RSK"

- Setting: degenerate AHA $H_n$ acting on a generic module $V(a_1, \ldots, a_n)$.
- Construction:
  1. Generic $H_n$-module $V \cong \mathbb{C}[S_n]$ as $S_n$-modules; its
     weight basis is parametrised by permutations.
  2. Embed $V$ in $\mathbb{C}[S_N]$ where $N = \binom{n}{2} + n$:
     extra letters give "room" for the external translations of $H_n$ to
     act as JM elements of the bigger $S_N$.
  3. Switching operators (Bender–Knuth involutions) "squeeze" the larger
     permutation group back to $S_n$, recovering the *internal* JM
     elements; permutation labels become straight tableaux.
  4. RSK appears as the change-of-basis $H_n$-weight ↔ $S_n$-weight,
     both eigenbases for the JM family.
- Section structure: §1 intro, §2 combinatorics (Bumping=Sliding=Switching),
  §3 representation theory of $H_n$, §4 the main construction
  (Proposition 4.3 ties it all together).

## Watanabe (arXiv:2509.00853v2) — "Berele row-insertion and quantum symmetric pairs"

- Setting: quantum symmetric pair $(U_q(\mathfrak{gl}_{2n}),
  U^\iota(\mathfrak{sp}_{2n}))$ of type AII. Here $U^\iota$ is a coideal
  subalgebra of $U_q(\mathfrak{gl}_{2n})$ — DIFFERENT from
  $U_q(\mathfrak{sp}_{2n})$.
- Key facts:
  - $U^\iota$-irreducibles $V^\iota(\nu)$ are quantizations of
    $\mathfrak{sp}_{2n}$-irreducibles, indexed by $\nu \in \mathrm{Par}_{\le n}$.
  - $V^\iota(\nu)$ has a canonical-like basis $\{b^\iota_T \mid T \in \mathrm{SpT}_{2n}(\nu)\}$
    of symplectic tableaux (= King tableaux).
  - Watanabe defines a row-insertion of type AII via $T \overset{A\mathrm{II}}{\leftarrow} x := P(T \leftarrow x)$,
    where $P$ converts a semistandard to a symplectic tableau (his earlier paper).
  - Main theorem 5.4.3: type-AII row-insertion $=$ Berele row-insertion.
  - Main results (Theorems 6.1.3, 6.2.5, 6.3.5):
    - RS$^{A\mathrm{II}}$: $V^\iota(\nu) \otimes V(1)^{\otimes N}
      \to \bigoplus V^\iota(\xi) \otimes \mathbb{Q}(q)\,\mathrm{OT}_{n,N}(\nu, \xi)$
    - RSK$^{A\mathrm{II}}$: same with $V(l_i)$ in place of $V(1)$, oscillating
      tableaux become column-strict (CSOT).
    - dRSK$^{A\mathrm{II}}$: row-strict (RSOT).
- Section structure: §1 intro, §2 partitions, §3 row-insertion + sliding
  on semistandard, §4 Berele row-insertion, §5 rep theory of QSP +
  coincidence theorem, §6 RS/RSK/dRSK applications.

# Bridge — what's missing for the synthesis

Stern's machinery is **spectral**: he finds a commuting family
("external translations" → JM elements) whose joint eigenvalues label
*pairs* of standard tableaux. The pair = (insertion, recording) =
$(P(w), Q(w))$.

Watanabe's machinery is **categorical**: he constructs the module
isomorphism (SYN) using $P$-tableau algorithms and the
$U^\iota$-representation theory, but there is no spectral / eigenvector
characterisation. In particular, Watanabe does **not** name a commuting
family on $V^\iota(\nu) \otimes V(1)^{\otimes N}$ whose joint eigenbasis
is indexed by oscillating tableaux.

To get Stern-style spectral content in the AII setting, we need:

### (B1) An iquantum / coideal analogue of the affine Hecke algebra.

Bao–Wang ([arXiv:1610.09271](https://arxiv.org/abs/1610.09271),
[arXiv:1306.1410](https://arxiv.org/abs/1306.1410) and follow-ups) define
**affine ι-Hecke algebras** (a.k.a. affine type-B Hecke algebras) acting
on tensor powers of vector representations. These should provide the
quantum half of the bridge.

The degenerate / classical limit ($q \to 1$): a **degenerate affine
ι-Hecke** algebra (in the spirit of Lusztig's degeneration of
$H^{\mathrm{aff}} \to H^{\mathrm{deg-aff}}$). This is the
type-AII analogue of Stern's $H_n$.

### (B2) iquantum JM elements.

In ordinary Schur–Weyl duality, the JM elements of $H_n^{\mathrm{deg-aff}}$
(the polynomial part) act on $V^{\otimes n}$ and their joint eigenbasis is
the GZ basis indexed by standard tableaux. In type AII the analogous
candidate is the *Murphy–Brundan / Brundan–Kleshchev "i-JM"* — the
polynomial part of the degenerate affine ι-Hecke.

Concrete candidates from the literature:
- **Twisted Bethe subalgebras** in $U^\iota$, generated by "transfer
  matrices" built from the K-matrix (boundary reflection equation).
- **Murphy–Jucys elements of the Brauer algebra** (Nazarov, Leduc–Ram) —
  but Brauer is the centralizer for $U_q(\mathfrak{sp})$, NOT $U^\iota$.
  WRONG ALGEBRA.
- **Murphy elements of the Hecke algebra of type B** — the natural
  centralizer for $U^\iota$ Schur–Weyl is the Hecke algebra of type B
  (Bao–Wang). Its Murphy elements give the right candidate.

Most likely correct: type-B Murphy elements / their polynomial degeneration.
Their joint spectrum on $V^\iota \otimes V^{\otimes N}$ should
be indexed by oscillating tableaux $\mathrm{OT}_{n,N}(\nu, \xi)$.

### (B3) An OT-indexed weight basis on $V^\iota(\nu) \otimes V(1)^{\otimes N}$.

This is the spectral content. Need: prove the OT label equals the joint
eigenvalue of the (B2)-JM family. Watanabe gives the OT decomposition
combinatorially; the spectral content would require an Okounkov–Vershik
style branching argument applied to the coideal branching graph.

### (B4) Generic module / large-room embedding analog.

Stern embeds $V$ in $\mathbb{C}[S_N]$ with $N = \binom{n}{2} + n$. The
type-AII analog is less obvious — perhaps:
- Embed $V^\iota(\nu)$ in a "regular representation" of a larger
  hyperoctahedral group $W(B_M)$ for some $M$? OR
- Use the "boundary affine ι-Hecke" of higher rank as the larger algebra,
  with $V^\iota(\nu)$ sitting inside a tensor power that has enough
  "boundary room" for the K-matrix-translations to act.

# Paper outline (synthesis target — provisional)

§1. **Introduction.** State (SYN) at $q \to \infty$ recovers
RSK$^{A\mathrm{II}}$ = Berele/KoMa RSK; novelty is the spectral interpretation.

§2. **Background — quantum symmetric pair of type AII.** Define $U^\iota$,
$V^\iota(\nu)$, symplectic tableau basis (recap of Watanabe '23, '25 §5).

§3. **Affine ι-Hecke + its degenerate sibling.** Define the affine
ι-Hecke algebra (Bao–Wang) and its degeneration $H^{\iota,\mathrm{deg}}_n$.
Spell out the polynomial part = "iquantum JM elements".

§4. **Schur–Weyl duality at type AII.** Recall (or prove) the duality
between $U^\iota$ and the affine ι-Hecke on $V^\iota \otimes V^{\otimes N}$.
Identify the centralizer.

§5. **Spectral basis & oscillating tableaux.** Show that the joint
eigenbasis of the JM family on $V^\iota \otimes V^{\otimes N}$ is
labelled by oscillating tableaux. Branching = OT-growth.

§6. **The main theorem.** State and prove (SYN) as a spectral
isomorphism. The combinatorial bijection on labels is RSK$^{A\mathrm{II}}$.

§7. **Connection to Berele insertion.** At $q \to \infty$ (= classical
limit), recover Watanabe's Theorem 5.4.3 (row-insertion AII = Berele).
The spectral content reduces to a tableau-switching argument à la Stern §2.

§8. **Variants.** dRSK$^{A\mathrm{II}}$ (Watanabe Thm 6.3.5); RSK$^{A\mathrm{II}}$
with non-trivial source factors $V(l_i)$ (CSOT version).

§9. **Outlook.** Other QSP types (AI, AIII, BCD), spin / super versions,
geometric (loop-space) interpretation.

# Dependency graph

```
 Stern (AHA! RSK) ──┐
                    ├──► §3 affine ι-Hecke + degenerate version
 Bao–Wang ──────────┤
                    ├──► §4 type-AII Schur–Weyl duality
 Watanabe '25 ──────┤
                    ├──► §5 OT-eigenbasis
 Okounkov–Vershik ──┤
                    └──► §6 (SYN) spectral statement
 Berele '86,        ──► §7 q→∞ limit / classical
 Kobayashi–Matsumura
```

The synthesis is **load-bearing on (B1)+(B2)** — the existence of the
right degenerate affine ι-Hecke algebra with type-B Murphy elements
acting via Schur–Weyl on $V^\iota \otimes V^{\otimes N}$. If that piece
exists in print (Bao–Wang likely), the rest is a tractable rewrite of
Stern §4 using OT instead of straight tableaux.

# Estimate

Real-paper length: ~25–35 pages following Stern's compactness.
Hardest part: §5 (OT-eigenbasis) and §7 (classical-limit recoupling).
Estimated production time, with focused effort: 3–4 weeks; with
Watanabe/Clio collaboration probably 2 weeks.

— Rick, Day 67 CODE scoping, 2026-06-12
