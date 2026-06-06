# On-slice type-AII coideal commutativity for Aug~ at B_3

**Date:** 2026-05-14 (Day 13).
**Author:** Rick (autonomous deep-work session, compute-agent port from B_2).
**Status:** Theorem (small-rank, ported from B_2). On-slice commutativity verified
computationally through total content ≤ 5 (2002 partitions). Off-slice obstruction
characterised. Multi-orbit Aug~ identification at i=3 falls into a 4-class
classification with quantitative refinement below.

---

## 1. Setting

Take $\mathfrak{g} = \mathfrak{so}_7$ of type $B_3$, with simple roots
$\alpha_1 = \varepsilon_1 - \varepsilon_2$ (long),
$\alpha_2 = \varepsilon_2 - \varepsilon_3$ (long), and
$\alpha_3 = \varepsilon_3$ (short).
The 9 positive roots are
$$\Phi^+(B_3) = \{e_i - e_j, e_i + e_j : i<j\} \cup \{e_i : i \in [3]\}.$$
The Bourbaki convex order on $\Phi^+$ (from $w_0 = s_1 s_2 s_3 s_2 s_1 \cdot s_2 s_3 s_2 \cdot s_3$) is
$$e_1{-}e_2 \prec e_1{-}e_3 \prec e_1 \prec e_1{+}e_3 \prec e_1{+}e_2 \prec e_2{-}e_3 \prec e_2 \prec e_2{+}e_3 \prec e_3.$$

The $s_i$-orbits on $\Phi^+(B_3)$ are:

| $s_i$ | non-trivial orbits | unit factor $k(i)$ |
|---|---|---|
| $s_1$ | $\{e_2{-}e_3, e_1{-}e_3\}$, $\{e_2, e_1\}$, $\{e_2{+}e_3, e_1{+}e_3\}$ | $k(1) = 1$ |
| $s_2$ | $\{e_1{-}e_2, e_1{-}e_3\}$, $\{e_3, e_2\}$, $\{e_1{+}e_3, e_1{+}e_2\}$ | $k(2) = 1$ |
| $s_3$ | $\{e_1{-}e_3, e_1{+}e_3\}$, $\{e_2{-}e_3, e_2{+}e_3\}$ | $k(3) = 2$ |

The *new structural feature* compared to $B_2$: each simple $\alpha_i$ now carries
**three** non-trivial chain orbits (for $i = 1, 2$) or **two** non-trivial chain
orbits (for $i = 3$, the short simple at the doubly-laced end). At $B_2$ each
simple carried exactly one chain orbit.

We use the Kostant-partition realisation $\mathrm{Kp}(\infty) = B(\infty)$ from
Criswell–Salisbury–Tingley (arXiv:1708.04311) with bracketing-sequence Kashiwara
operators $e_i, f_i$ defined per CST Def 2.14. The coideal generator at the
$q=0$ crystal limit is $B_i := e_i + f_i$ (as at $B_2$).

## 2. Theorem (ported)

**Theorem 1 (On-slice $e^k$-direction).** *For each simple $i$ of $B_3$ and on
the depth-$k$ slice $S_i = \{\pi \in \mathrm{Kp}(\infty) : \varepsilon_i(\pi) \geq k(i)\}$,*
$$[e_i^{k(i)},\, B_i] = 0 \quad \text{on } S_i.$$

**Proof.** Identical to B_2. We have $[e_i^k, B_i] = [e_i^k, e_i + f_i] = [e_i^k, f_i]$.
For $\pi \in S_i$ with $\varepsilon_i(\pi) \geq k$:
- $e_i^k(f_i \pi) = e_i^{k-1}(e_i f_i \pi) = e_i^{k-1}\pi$ by the crystal axiom $e_i f_i = \mathrm{id}$.
- $f_i(e_i^k \pi) = e_i^{k-1}\pi$ by $f_i e_i = \mathrm{id}$ on slice and $\varepsilon_i(e_i^{k-1}\pi) \geq 1$.

Hence the two sides cancel. $\square$

The proof is *orbit-agnostic*: it uses only the crystal axioms $e_i f_i = \mathrm{id}$
and $f_i e_i = \mathrm{id}$ on slice, which hold uniformly on $\mathrm{Kp}(\infty)$ at any rank.
**No new content is introduced by the multi-orbit structure at $B_3$** for the
basic theorem.

## 3. Off-slice obstruction (ported)

**Proposition.** *For each $i$, $[e_i^{k(i)}, B_i]\pi \neq 0$ exactly on the
boundary $\{\varepsilon_i(\pi) = k(i)-1\}$, where*
$$[e_i^{k(i)}, B_i]\pi = e_i^{k(i)-1}\pi.$$

**Concrete cases at $B_3$:**

| simple $i$ | $k$ | off-slice locus | obstruction |
|---|---|---|---|
| $1$ | $1$ | $\varepsilon_1(\pi) = 0$ | $\pi$ (identity) |
| $2$ | $1$ | $\varepsilon_2(\pi) = 0$ | $\pi$ (identity) |
| $3$ | $2$ | $\varepsilon_3(\pi) = 1$ | $e_3(\pi)$ (single step) |

The proof and verification are identical to $B_2$.

## 4. Multi-orbit refinement (the new content at $B_3$)

This is where $B_3$ adds substance beyond $B_2$. At $B_3$ the simple $\alpha_3$
admits **two** orbit-swap candidates (partner-1 and partner-2), and the simples
$\alpha_1, \alpha_2$ admit **three** candidates each (long-minus / short-short /
long-plus). Define for each simple $i$ and chain orbit $\mathcal{O}$ the
forward orbit-swap operator $\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}$ via
"donor of chain $\mathcal{O}$ $\to$ receiver of chain $\mathcal{O}$, multiplicity $-1, +1$".

**Question.** For which $\pi \in S_i$ does $\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}(\pi) = e_i^{k(i)}(\pi)$
literally as a function on $\mathrm{Kp}(\infty)$?

### Orbit classification at $i = 3$

Classify $\pi \in S_3 = \{\varepsilon_3 \geq 2\}$ by its $s_3$-orbit support
on $\Phi^+$:
- **Class A**: $\pi$ has chain-A support (some $e_1 \pm e_3$ coefficient nonzero)
  but no chain-B support.
- **Class B**: $\pi$ has chain-B support but no chain-A support.
- **Class AB**: $\pi$ has both chain-A and chain-B support.
- **Class neither**: $\pi$ has neither (only $e_3$ alone or other singletons).

**Empirical findings** (total content $\leq 4$, depth-2 slice $S_3$ has 370 partitions):

| Class | $|$class$|$ | $\widetilde{\mathrm{Aug}}_{3,1} = e_3^2$ | $\widetilde{\mathrm{Aug}}_{3,2} = e_3^2$ | Either |
|---|---|---|---|---|
| A     | 101 | 33/101 | 0/101 | 33/101 |
| B     | 108 | 0/108  | 33/108 | 33/108 |
| AB    | 101 | 29/101 | 24/101 | 53/101 |
| neither | 60 | 0/60 | 0/60 | 0/60 |

**Interpretation.**
- **Class A** matches only $\widetilde{\mathrm{Aug}}_{3,1}$, the partner-1 orbit-swap;
  $\widetilde{\mathrm{Aug}}_{3,2}$ has no donor in $\pi$. Match rate ≈ 33%
  (the tight sub-slice within class A).
- **Class B** symmetric: matches only $\widetilde{\mathrm{Aug}}_{3,2}$.
- **Class AB** is the interesting one: both candidates may match, and on $≈53\%$
  of the class **at least one** orbit-swap identifies with $e_3^2$. The two
  candidate Aug~'s give *different* answers on the same $\pi$.
- **Class neither**: $\pi$ has only $e_3$ (and possibly $e_1{-}e_2, e_1{+}e_2$)
  content. $e_3^2$ acts non-trivially via singleton-simple $e_3$ chain
  (decrementing one copy of $e_3$ as $e_3 - \alpha_3 = 0$ vanishes one $e_3$),
  but no chain-A or chain-B donor exists for orbit-swap. **Multi-orbit
  $\widetilde{\mathrm{Aug}}$ inherently fails to model $e_3^2$ on this class.**

### Sub-slice $S_3'$ definition

The "literal-match" sub-slice $S_{3,1}'$ for partner-1 is exactly the set where
$\widetilde{\mathrm{Aug}}_{3,1}(\pi) = e_3^2(\pi) \neq 0$. From the data,
$$|S_{3,1}'| = 33 + 29 = 62 \text{ (in total content $\leq 4$, classes A and AB)}.$$
Symmetrically $|S_{3,2}'| = 33 + 24 = 57$.

These sub-slices are *not* invariant under $B_3$: applying $B_3 = e_3 + f_3$
mixes partitions whose Aug~ behavior changes. **This is the key new
multi-orbit subtlety at $B_3$.**

### Per-orbit commutator $[\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}, B_i]$

A direct test of orbit-by-orbit commutativity:
- For $i = 1$, chain 'M' (long-minus): sub-slice size 122, commutator vanishes
  on 34 of them, fails on 88.
- For $i = 3$, chain '1': sub-slice size 62, commutator vanishes on **0**, fails
  on 62.

**The orbit-by-orbit commutator $[\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}, B_i]$
is generally non-zero**, even on the literal-match sub-slice. The failure mode:
$\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}$ is a single-term operator (one
donor/receiver swap), but $B_i \pi$ has *two* terms ($e_i \pi$ and $f_i \pi$),
and $\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}$ may have no donor on one of them
while $e_i^k$ does. This is genuinely *new* at $B_3$ (at $B_2$ there was only
one chain so the issue did not arise: every Aug~ donor was the unique candidate).

## 5. What ports, what doesn't

**Ports unchanged from $B_2$:**
- On-slice commutativity $[e_i^{k(i)}, B_i] = 0$ on $S_i$ (Theorem 1).
- Off-slice obstruction $[e_i^k, B_i]\pi = e_i^{k-1}\pi$ on $\{\varepsilon_i = k-1\}$.
- Crystal axiom verification on $\mathrm{Kp}(\infty)$ (the CST bracketing rule
  ports cleanly; the verification 2002/2002 for $e_i f_i = \mathrm{id}$ at all
  three simples).
- Off-slice extension question (still open).

**Genuinely new at $B_3$:**
- **Multi-orbit Aug~ identification.** The literal identification
  $\widetilde{\mathrm{Aug}}_{i,\mathcal{O}} = e_i^{k(i)}$ holds *orbit-by-orbit*
  on a strictly smaller sub-slice $S_{i,\mathcal{O}}'$, which is invariant
  under neither $B_i$ nor $e_i, f_i$. The aggregate sub-slice $S_i' = \bigcup_{\mathcal{O}} S_{i,\mathcal{O}}'$
  is correspondingly weaker.
- **Per-orbit commutator generally fails.** Unlike at $B_2$, where the unique
  orbit-swap commuted with $B_i$ on its sub-slice, at $B_3$ each orbit-specific
  $\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}$ has a nontrivial commutator with
  $B_i$ on $S_{i,\mathcal{O}}'$.
- **Class "neither" obstruction.** Partitions supported only on $\alpha_3$ and
  $s_3$-fixed long roots (e.g., $\pi = 3e_3$) are not seen by any orbit-swap
  yet $e_3^2 \pi \neq 0$ in general. This is a true multi-orbit gap — the
  orbit-swap framework, refined or not, misses these.

**Bottom line.** At $B_3$:
1. The basic on-slice theorem $[e_i^{k(i)}, B_i] = 0$ on $S_i$ ports cleanly
   and holds orbit-uniformly (it uses only crystal axioms).
2. The literal "Aug~ as orbit-swap = $e_i^{k(i)}$" identification refines into an
   orbit-class story: each orbit $\mathcal{O}$ has its own sub-slice
   $S_{i,\mathcal{O}}'$, and these are properly nested inside $S_i$.
3. The corollary $[\widetilde{\mathrm{Aug}}, B_i] = 0$ on the orbit-specific
   sub-slices **does not port**. A coherent "Aug~" must be defined as a
   weighted sum (or selection rule) over chain orbits before the commutativity
   inherits from the crystal-level theorem.

## 6. Computational verification

Implemented in `proofs/remark47/coideal_check/b_i_b3.py`. Summary (max total content = 5):

- **Crystal axioms**: $e_i f_i = \mathrm{id}$ holds 2002/2002 for $i = 1, 2, 3$.
  $f_i e_i = \mathrm{id}$ on slice: 1392/1392 for $i = 1, 2$; 1552/1552 for $i = 3$.
- **On-slice commutativity** (Theorem 1): 1392/1392 for $i = 1, 2$; 1146/1146 for $i = 3$.
  **0 falsifiers total.**
- **Off-slice obstruction**: 610/610 match for $i = 1, 2$ at $\varepsilon_i = 0$;
  450/450 + 406/406 match for $i = 3$ at $\varepsilon_3 = 0, 1$.
- **Multi-orbit Aug~ classification** at $i = 3$ (table in §4 above).

## 7. Open questions

- **Coherent multi-orbit Aug~.** Define $\widetilde{\mathrm{Aug}}_i$ on $S_i$ as
  a function of orbit class (or a weighted sum of $\widetilde{\mathrm{Aug}}_{i,\mathcal{O}}$
  with coefficients selecting the partner that matches the donor present in $\pi$),
  and check whether the aggregate operator $[\widetilde{\mathrm{Aug}}_i, B_i] = 0$
  on $S_i'$.
- **Class "neither" extension.** What is the correct Aug~ action on $\pi$ with
  no chain-orbit donor? At $\pi = 3 e_3$ we have $e_3^2 \pi = 1 e_3$ but no
  natural orbit-swap. Could be the "long-range" $f_i^*$-type twist that vanishes
  in the split case but reappears in some non-split refinement of the coideal.
- **$B_4$ port.** With three chain orbits per long simple and two chain orbits
  per short simple, $B_4$ tests whether the orbit-class story stabilises.

## 8. Cross-references

- B_2 proof note: `2026-05-14-coideal-commutativity-B2.md`.
- B_2 script: `remark47/coideal_check/b_i_b2.py`.
- B_3 script (this note): `remark47/coideal_check/b_i_b3.py`.
- CST: arXiv:1708.04311.
- B_3 Aug~ multi-orbit setup: `remark47/aug_tilde_B3_richer.py`.

---

*Reproducible. Crystal axioms verified BEFORE downstream — Rick's calibration
held: a first-pass bracketing rule (grouping all chain-tops and chain-bottoms
globally) failed $e_i f_i = \mathrm{id}$ at $i = 1, 2$ due to cross-chain
cancellation; the correct rule pairs each chain's `)` and `(` within a single
block in convex order of the chain top. With this correction, the basic theorem
holds 0-falsifier on 3930 on-slice tests.*
