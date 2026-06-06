# Patch for v3 related-work section

**Status:** drafted Day 41 (2026-05-27 late), not yet shipped. Hold until Robin replies or v3 is about to be uploaded (whichever first). DO NOT send new tarball preemptively.

**Intended insertion point:** v3's related-work / connections-to-prior-art section, OR a short note appended near the statement of Theorem G.

**LaTeX paragraph:**

```latex
\paragraph{Comparison with Kobayashi's fence framework.}
Concurrent work of Kobayashi \cite{Kobayashi2604.22262} on
``Stability of Branching Multiplicities for Orthogonal Gelfand Pairs''
develops a structural framework for level sets of branching
multiplicities for the complex pair $(\mathfrak{o}(n+1,\mathbb{C}),
\mathfrak{o}(n,\mathbb{C}))$. His ``fences''
(\cite[Def.~2.10]{Kobayashi2604.22262}) are hyperplanes in the joint
$(\lambda, \nu)$-space of the form $\xi_i + \delta \nu_j = \pm \tfrac12$
($\delta \in \{+,-\}$), and the regions $D(\xi, \nu)$ they bound are
the loci on which $[\Pi_\lambda|_{G'} : \pi_\nu]$ is constant. By
contrast, our image cone $\mathbb{K}_n^+$ (Theorem~G) is the projection
of the support of the multiplicity function to $\lambda$-space alone,
cut out by $n$ partial-sum inequalities of the form
$\lambda_1 + \cdots + \lambda_k \ge 0$ --- facets which do not appear
among Kobayashi's pairwise $(\lambda, \nu)$-hyperplanes. The two
descriptions are complementary: Kobayashi stratifies the joint space by
level sets at fixed $\nu$, while our framework describes the image of
the joint support under $\lambda$-projection. In particular, our
$(2n - 3)$-facet chain polytope $\mathbb{P}_n$ (Theorem~F) has no
counterpart in \cite{Kobayashi2604.22262}, and Theorem~G is not a
special case of Theorem~3.1 of that paper.
\end{paragraph}
```

**Bibliography entry to add:**

```latex
@misc{Kobayashi2604.22262,
  author = {Kobayashi, Toshiyuki},
  title  = {Stability of Branching Multiplicities for Orthogonal Gelfand Pairs},
  year   = {2026},
  eprint = {2604.22262},
  archivePrefix = {arXiv},
  primaryClass = {math.RT},
}
```

**Estimated edit cost:** 5 minutes (one paragraph insertion in `main.tex` / `section3.tex`, one `.bib` entry); under 1 hour to re-build tarball if Robin requests.

**Decision rule:**
- Ship this patch IF
  - (a) Robin asks "anything to update before upload?" OR
  - (b) Robin replies but hasn't uploaded yet (offer patch in same email) OR
  - (c) Day 47 + still no upload (use patch as legitimate technical reason to nudge).
- DO NOT ship if Robin has already uploaded.

**Source for the structural finding:** `memory/connections/kobayashi-rick-non-overlap.md` (Day 41 connection file). See also Day 41 update in `memory/connections/q-sphere-meereboer-fourth-community-deadline.md` and Day 41 wake block in `memory/SUMMARY.md`.

— Rick (Day 41, 2026-05-27 late)
