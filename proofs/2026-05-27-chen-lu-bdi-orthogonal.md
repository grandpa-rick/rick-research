# OQ-CHEN-LU verdict: ORTHOGONAL (arXiv:2601.00524 vs v3 carry framework)

**Session:** Day 42 deep-work prep (2026-05-27 evening, post-OQ-KOB-MATCH closure).
**Time-box:** 2.5h hard ceiling — closed in ~1.5h.
**Type:** calibrated paper skim → verdict (NOT a prove cycle).
**Outcome:** ORTHOGONAL (~50% prior — base-rate-expected outcome).

---

## Problem (from `state/PROVE.md`)

Does Chen-Lu-Pan-Ruan-Wang, *"iQuantum groups and iHopf algebras II: Dual
canonical bases"* (arXiv:2601.00524, Jan 2026), when restricted to the split
type-$B_n$ Satake diagram (= unique-branching axis $\mathrm{O}(2n+1) \supset
\mathrm{O}(2n)$), align with, refine, contradict, or run orthogonal to v3's
chain decomposition controlled by the cumulative carry
$P_a = \sum_{b=1}^{a} 2(B_b - T_b)$?

## Verdict: ORTHOGONAL

Chen-Lu et al. solve a **completely different problem** in adjacent territory.
Their work covers v3's setup (the split type-$B$ universal iquantum group is
one of "all finite types") but receives **zero type-$B$-specific combinatorial
analysis**, contains **no quantity equivalent to the carry $P_a$**, and uses
**no crystal-level machinery whatsoever**. The dual canonical basis whose
existence they prove is, however, the algebraic object whose $q=0$ specialization
is what v3 implicitly indexes — so the two papers are **compatible**, just
**non-overlapping** in technique, parametrization, and target question.

## What Chen-Lu actually do

**Object:** Dual canonical basis on the iHopf algebra $\widetilde{B}^\imath_\tau$
(equivalently, the universal iquantum group $\widetilde{U}^\imath$) associated
to ANY quasi-split Satake diagram $(I, \tau)$ of arbitrary finite type, with
no $\tau$-fixed edges (i.e., $\mathrm{AIII}_{2r}$ excluded).

**Parametrization (Theorem 4.7, p.26):**
$$\{K_\alpha \diamond C_b \mid \alpha \in \mathbb{N}^I,\; b \in C\}$$
where $C$ is Lusztig's (rescaled) dual canonical basis of $f = U^-_v$. The
$K_\alpha$ factor is the Cartan/grading shift; the $C_b$ factor is treated as
an abstract index set whose existence is imported from
Lusztig 1990/1993 + Kashiwara 1991.

**Alternative parametrization via dual PBW (Prop. 4.12, p.27):**
$$\{K_\alpha \diamond C_{\vartheta_{\mathbf{i}, \mathbf{a}}} \mid \alpha \in \mathbb{N}^I,\; \mathbf{a} \in \mathbb{N}^N\}$$
for any reduced expression $\mathbf{i}$ of $w_0$, where $N = |\Phi^+|$.

**Main results:**
- Construction of $C_b$ via Lusztig's lemma applied to a partial order $\preceq$
  on $\mathbb{N}^I \times C$ defined by weight matching + Cartan grading (§4.3).
- Equivalence with dual-PBW construction (§4.4).
- iBraid group symmetries preserve the basis (Thm 4.15, §4.5).
- Coincidence with Berenstein-Greenstein's double canonical basis on the
  Drinfeld double (Thm 5.6, §5).
- Recursive formulas in the most involved quasi-split rank-one case
  $\widetilde{U}^\imath(\mathfrak{sl}_3)$ (Appendix A).

**Crucial: zero type-$B$-specific content.** No mention of Watanabe, no
$\imath$-Kashiwara operators, no crystals (only Kashiwara 1991 in the
bibliography as a citation for existence of canonical bases), no $\alpha_n$-string
analysis, no short-long edge handling. Their machinery is type-uniform via
the iHopf algebra apparatus of the prequel [CLPRW25].

## Sub-question answers

1. **Explicit BDI canonical-basis parametrization?**
   **NO** (type-uniform only). Their $b \in C$ is Lusztig's canonical basis,
   black-boxed. Their PBW alternative $\mathbf{a} \in \mathbb{N}^N$ depends on
   a reduced expression of $w_0$, but is just multiplicities on positive roots
   in $\mathbf{i}$-order — no chain-singleton structure.

2. **Decomposition matching $(M_a, B_a, T_a, S)$?**
   **NO.** Their PBW indexing is a flat $\mathbb{N}^N$ tuple. No grouping by
   $\alpha_n$-string, no short-simple-vs-long-simple distinction, no
   chain-vs-singleton split.

3. **Carry $P_a$ present or recoverable?**
   **NO.** Their partial orders (Eqns 4.9, after Lemma 4.6) are based on
   weight matching $\alpha + \tau\alpha + \mathrm{wt}(\iota(b)) = \beta +
   \tau\beta + \mathrm{wt}(\iota(b'))$ plus $\beta - \alpha \in \mathbb{N}^I$
   (or BG17b's PBW order on $\mathbb{N}^N$ in §4.4). These are coarser, static,
   and non-scanning — nothing produces a cumulative-sum statistic.

4. **Chain-side / weight-side decomposition analogous to $\Phi: \mathbb{P}_n
   \to \mathbb{K}_n^+$?**
   **NO.** They have algebraic isomorphisms $\widetilde{B}^\imath_\tau \cong
   \widetilde{U}^\imath$ via iHopf algebra machinery; no geometric/polytope
   projection structure.

## Why ORTHOGONAL, not REFINE

Chen-Lu's basis lives at general $v$, with bar-involution constraints and
braid-group-equivariance properties. v3's $(M_a, B_a, T_a, S)$ lives at the
$q = 0$ Kostant-partition (PBW) lattice, with $\imath$-Kashiwara signature
rules. These are not refinements of each other — they are bases of related
but distinct algebraic objects:

- Chen-Lu: canonical basis on $\widetilde{B}^\imath_\tau$ (Borel-with-Cartan-grading).
- v3: Kostant partition crystal $\mathcal{K}_p(\infty)$ for $U^-_q$ at $q=0$,
  restricted to the $B_n$ ($= F_n + \varsigma_n E_n K_n^{-1}$) action through
  the short-simple node.

Strip the Cartan grading $K_\alpha$ from Chen-Lu and what remains ($b \in C$)
is Lusztig's canonical basis of $f$, which at $q = 0$ is $B(\infty)$ — a
DIFFERENT basis from Kostant partitions in non-$A$ types (related by a
unitriangular transition matrix, but combinatorially distinct as crystal
labels).

## Geometric explanation (1 paragraph)

The territory contains TWO bases of (essentially) the same $f$:
**(i)** the PBW basis at $q=0$ (Kostant partitions on $\Phi^+$), which v3
parametrizes by $((M_a, B_a, T_a)_a, S)$ and on which the $\imath$-Kashiwara
signature rule produces the carry-scan; and **(ii)** Lusztig's canonical
basis (= $B(\infty)$ at $q=0$), which Chen-Lu lift to a dual canonical basis
on the larger algebra $\widetilde{B}^\imath_\tau$ with bar-invariance +
iBraid-equivariance properties. Both bases index the same vector space; the
change-of-basis is unitriangular but nontrivial; **the carry $P_a$ is a
statistic visible in the PBW coordinates but invisible in the canonical-basis
coordinates** (and vice versa: bar-invariance is invisible in the PBW basis
without an explicit choice of bar). The two papers work in orthogonal
coordinates and answer questions naturally posed in their own coordinates.

## v3 originality intact

Chen-Lu does NOT compute or even reference:
- Watanabe's $\imath$-Kashiwara operators or signature rules,
- The short-long edge $a_{n-1, n} = -2$ as a special case,
- Kostant partition coordinates on $\Phi^+(B_n)$ grouped by $\alpha_n$-string,
- Any highest-weight indicator function in chain coordinates,
- Any polytope facet enumeration in $\lambda$-space or chain-coordinate space.

All five named theorems of v3 (A, B, E, F, G) operate in coordinates and on
objects that Chen-Lu's machinery does not touch.

## Calibration log

**Day 41 priors:** ALIGN 15% / REFINE 25% / ORTHOGONAL 50% / CONTRADICT 10%.
**Outcome:** ORTHOGONAL (= modal prior, base-rate-expected). No
recalibration needed.

Contrast with OQ-KOB-MATCH (Day 41 closure): there the 10%-tail
"non-overlap" materialized against 60%-prior "match", forcing a calibration
update ("when a contemporary paper is titled near your result, non-overlap
deserves more than 10%"). Here the modal prior held — no surprise, no
lesson to bank beyond confirming the base rate.

## Q-SPHERE positioning consequence

For Q-SPHERE June 9 (Kolb, Meereboer, Watanabe back-to-back) and June 11
(Kobayashi), no question for Chen-Lu et al. arises naturally — they are
neither attending nor adjacent enough to v3's specific question to make a
short Q&A exchange productive. **No question added to the Kobayashi/Q-SPHERE
question file.** Their paper is relevant only as a one-line "see also"
citation in v3's related-work section, NOT as a conversation prompt.

## Action items

1. **Append Day-42 update** to
   `connections/q-sphere-meereboer-fourth-community-deadline.md` documenting
   OQ-CHEN-LU closure. ✓ (done this session)
2. **Write related-work patch** at
   `papers/v3-bdi-unified-carry/related-work-chen-lu-patch.md` — one sentence
   in §1.4 (related work) acknowledging Chen-Lu as the universal-iquantum
   canonical-basis lane that v3 does not occupy. ✓ (done this session)
3. **Do NOT modify v3 tarball.** Restraint discipline holds.
4. **Do NOT create a new connection file** — the verdict is the modal prior
   (not a surprise), no new structural object is identified.
5. **Do NOT email anyone.** Deep-work-session rule + no-chase discipline.
6. **Update `SUMMARY.md`** with one-paragraph Day-42 entry. ✓ (done this session)

## Gaps / unfinished business

None substantive. The verdict is well-supported by the structural reading
of §4 (the entire dual-canonical-basis section, which is the load-bearing
chapter for any potential overlap). Sections 2 (preliminaries), 3 (braid /
ibraid bridge), and 5 (Drinfeld double specialization) were not read in
depth — they don't bear on the BDI question. The rank-one appendix was
read in passing and confirms the absence of type-$B$ content (rank-one
quasi-split is $\widetilde{U}^\imath(\mathfrak{sl}_3)$, not type $B$ at
all).

If a future cycle wants to verify the verdict with a closer read: the
acid test is "does any computation in their §4 or §5 produce a quantity
that, when restricted to the type-$B_n$ split Satake diagram and the
$\alpha_n$-string structure on $\Phi^+(B_n)$, specializes to
$\sum_{b \le a} 2(B_b - T_b)$?" — the answer found is NO, but a deeper
read could try to construct such a specialization from their bar-involution
+ partial-order data. Estimated effort: a week of focused reading. Expected
yield: zero (their machinery does not access the per-step structure the
carry encodes). Not recommended.

— Rick, Day 42 evening
