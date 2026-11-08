# Wake 283 — Lemma I / Crown U owner gate (literature agent log)

Date: 2026-11-08. Agent: literature sub-agent for Rick. Timebox ~40 min.

Lemma I (ours, conjectural): x, z in the same left cell, L(z) ≠ ∅, N[L(z)] ⊆ L(x), L(x) ≠ S ⇒ μ(x,z) = 0.
Layer Lemma (ours): K ⊆ S, u ∈ ^K W, v, v' ∈ W_K ⇒ P_{v'u, vu} = P_{v', v}.

## Files obtained (all in /home/agent/projects/reading/pdfs/, pdftotext'd to .txt)

| file | paper | how | read |
|---|---|---|---|
| stembridge_admissible_Wgraphs.{pdf,txt} | Stembridge, Admissible W-graphs, Represent. Theory 12 (2008) 346–368 | already on disk | first-hand §2, §4 (Props 4.1–4.7, Thm 4.9, Rem 4.5), §5 Steps 1–2 |
| stembridge_finite.{pdf,txt} | Stembridge, A finiteness theorem for W-graphs, Adv. Math. 229 (2012) 2405–2414 | Wayback copy of dept.math.lsa.umich.edu/~jrs/papers/finite.pdf | first-hand by grep + intro |
| stembridge_bigraphs.{ps,pdf,txt} | Stembridge, Admissible W-graphs and commuting Cartan matrices, Adv. Appl. Math. 44 (2010) 203–224 | Wayback copy of ~jrs/papers/bigraphs.ps.gz (actually uncompressed PS) | first-hand by grep + §6 |
| arx_1307.8354.{pdf,txt} | M. Chmutov (sole author), Type A molecules are Kazhdan–Lusztig | arXiv | first-hand §2 (arc transport), §3.4, §4 Lemmas 4.1–4.2 |
| arx_1807.07457.{pdf,txt} | Van Minh Nguyen (sole author), Type A-admissible cells are Kazhdan–Lusztig | arXiv | first-hand §5–9 by grep; Lemmas 7.23–7.25, §8 opening, Prop 9.5 |
| arx_1706.00471.{pdf,txt} | Chmutov, Lewis, Pylyavskyy, Monodromy in KL cells in affine type A | arXiv | grep only |
| arx_1511.05861.{pdf,txt} | Chmutov, Pylyavskyy, Yudovina, Matrix-ball construction of affine RS | arXiv | grep only |
| arx_math0202252.{pdf,txt} | S. Billey, T. Braden, Lower bounds for KL polynomials from patterns | arXiv | first-hand §2 Thm 2, §3.1 Thms 5–7 |

Access notes: umich.edu (all hostnames: dept.math.lsa / www.math.lsa / websites / public.websites) is behind a Cloudflare JS challenge (403) — use web.archive.org/web/2020/http://www.math.lsa.umich.edu/~jrs/papers/<name>. ams.org also 403s to curl and WebFetch (Polo 1999 not obtained).

## Q1 — Stembridge sequels

Stembridge's own publication list (Wayback, ~jrs/papers.html snapshot 2021-01-15 and papers/pub_list) has exactly three W-graph papers: #60 Admissible W-graphs (RT 2008), #62 Admissible W-graphs and commuting Cartan matrices (AAM 2010), #63 A finiteness theorem for W-graphs (Adv. Math. 2012). Nothing later (#64 Kronecker, #65 odd inversions, #66 Wronskian Appell).

**"More W-graphs and cells: molecules and components at infinity" — NOT FOUND.** Not on Stembridge's own publication list, and the exact-phrase web search found nothing. Treat the title as likely hallucinated. The 2008 paper does promise a sequel (p. 346 intro and p. 363: "In a sequel to this paper, we will describe a much more refined approach to the cell classification problem that is suitable for larger Coxeter systems."). As far as we can tell, the 2010 bigraphs paper is the published sequel.

Arc content in the 2008 paper (first-hand):
- p. 357, before Prop 4.2: "note that τ(u) ⊃ τ(v) forces m(v → u) = 0. In such cases, we say that u → v is an arc of Γ."
- Prop 4.2 (Simplicity Rule), p. 357: "either (a) τ(u) ⊋ τ(v) and m(v → u) = 0, or (b) τ(u) and τ(v) are incomparable and m(u → v) = m(v → u) = 1."
- Prop 4.1 (Compatibility Rule): "every i ∈ τ(u) − τ(v) must be bonded to every j ∈ τ(v) − τ(u)". This is vacuous for arcs, since τ(v) − τ(u) = ∅.
- Prop 4.7 (Polygon Rule), p. 361: N^r_ij(Γ;u,v) = N^r_ji(Γ;u,v) for 2 ≤ r ≤ p, "for all vertices u, v with i, j ∈ τ(u) and i, j ∉ τ(v)". This is the only general constraint on arc weights. It is an equality of path counts, not a vanishing rule.
- Rem 4.5, p. 359: "no admissible A3-cell can have arcs". This is a rank-3 classification fact, not a general rule.
- §5 Step 2, p. 363: "Every arc in an admissible cell supported on the multiset M must be directed from a vertex in Γi to a vertex in Γj such that Γj ≺ Γi". This is about ordering between molecules.
- 2010 (bigraphs) and 2012 (finite) papers: grep for arc/neighbo/nested/μ gives nothing on arcs. Bigraphs §6 just restates (6.2)–(6.3) KL edge weights and Question 6.3 / Thm 6.4–6.5 (dihedral cell classification). The finiteness paper is pure matrix theory (p(t)-cells).

**Verdict Q1: NOT FOUND.** No Stembridge result forbids arcs in terms of N[τ(target)] ⊆ τ(source). Lemma I's in-cell arc exclusion is not stated, and is not an immediate special case of Props 4.1–4.7.

## Q2 — Chmutov / Lewis / Pylyavskyy (arXiv IDs verified via export.arxiv.org API)

- 1307.8354: "Type A Molecules are Kazhdan-Lusztig", **Michael Chmutov alone** (arxiv abs citation_author = "Chmutov, Michael").
- 1706.00471: "Monodromy in Kazhdan-Lusztig cells in affine type A", Michael Chmutov, Joel Brewster Lewis, Pavlo Pylyavskyy. ID correct.
- 1511.05861: "Matrix-Ball Construction of affine Robinson-Schensted correspondence", Michael Chmutov, Pavlo Pylyavskyy, Elena Yudovina.
- 1806.07429: "An affine generalization of evacuation", M. Chmutov, G. Frieden, D. Kim, J. B. Lewis, E. Yudovina.
- 1807.07457: "Type A-admissible cells are Kazhdan-Lusztig", **Van Minh Nguyen alone**. It proves Stembridge's conjecture and is the most relevant paper here.

Findings:
- 1706.00471 / 1511.05861: no μ-values or W-graph edges, only AMBC and τ-invariants of tabloids (1706.00471 Prop 3.6: "L(w) = τ(P(w)) and R(w) = τ(Q(w))"). Nothing relevant.
- Chmutov 1307.8354 §2.1: "if u → v is an arc, then τ(u) ⊃ τ(v)". §2.3 "Arc transport. The following three propositions follow from the local polygon rules." Prop 2.7: for simple edges (x,y), (x',y') activating the same bond (i,j), with k ∈ τ(x) ∩ τ(y) and k ∉ τ(x') ∪ τ(y'), "Then m(x, x′) = m(y, y′)". Props 2.8 and 2.9 give A3/A4 analogues. These are equalities of arc weights. None of them makes an arc vanish.
- Nguyen 1807.07457:
  - Prop 9.5 proof, p. 35: "µ(c_u, c_t) = µ^(λ)(u,t) = 0 unless u < t or u = s_i t > t", and "all that remains is to show that µ(c_u, c_t) = µ^(λ)(u,t) whenever u < t and D(t) ⊊ D(u)" ("probable pairs"). The paper shows that the arc weights inside a type-A cell are forced by the Stembridge rules, through an induction on lexicographic order. It does not give an explicit vanishing criterion.
  - Lemma 7.25 (p. 20): for D(u) = {n−1} ∪ D(t) with µ ≠ 0 and restriction number n−2, "either u < t and D(v) = {n−2, n−1} ∪ D(x) … or else (λ,α) = (µ,β) and u = s_{n−1}t > t, and µ(c_{β,u}, c_{α,t}) = 1". This is an arc-transport and normal-form statement. It is not a neighbourhood vanishing rule.
  - §8 opening, p. 21: between different molecules, "we must have D(t) ⊊ D(u) and µ(c_{α,t}, c_{β,u}) = 0".

**Verdict Q2: NOT FOUND (closest: PARTIAL-mechanism).** No statement that arcs with N[τ(target)] ⊆ τ(source) carry zero weight within a cell. Nguyen's transport machinery (Lemmas 7.20–7.25, Def. "probable pair", Prop 9.5) is the natural tool to prove or disprove Lemma I in type A, and should be cited as the framework. It does not own the statement.

## Q3 — Layer Lemma owner

Billey–Braden, math/0202252, read first-hand:
- §2 Thm 2, p. 4: pattern map φ: W → W′ with "φ(wx) = wφ(x)"; "φ^{-1}(1) ∩ W′x is the unique minimal element in W′x". So for W′ = W_K standard, φ(vu) = v for u ∈ ^K W, v ∈ W_K.
- §3.1, p. 9: "If both (a) and (b) hold, then Theorem 5 is implied by a well-known equality (see [P, Lemma 2.6]): Theorem 6. If W′ or x^{-1}W′x is a standard parabolic subgroup of W and w ∈ W′x, then P_{x,w}(q) = P′_{φ(x),φ(w)}(q)."
- [P] = P. Polo, Construction of arbitrary Kazhdan–Lusztig polynomials in symmetric groups, Represent. Theory 3 (1999) 90–104, Lemma 2.6. Polo was not obtained (AMS 403).

Take x = v′u, w = vu: Theorem 6 gives P_{v′u,vu} = P′_{v′,v}, where P′ is the KL polynomial of W_K. That P′ equals P in W is the standard parabolic fact. So this is exactly the Layer Lemma.

Two caveats. Billey–Braden's §3 is set in Weyl groups, and Polo's paper is about S_n. Our use is type A, so the scope is covered.

**Verdict Q3: OWNED (folklore).** Called "well-known" in Billey–Braden Thm 6, citing Polo 1999 Lemma 2.6. We read Billey–Braden first-hand; the Polo locator is secondary (not opened). Björner–Brenti was not accessed.

## Overall gate verdict

Lemma I (and its type-A special case) is **not owned** by the literature checked: Stembridge 2008/2010/2012, Chmutov 2013, Nguyen 2018, CLP 2017, CPY 2015. The Stembridge axioms constrain arcs only through Simplicity (arcs are nested) and Polygon/arc-transport (equalities of weights), never through a neighbourhood vanishing rule. Nguyen proves that type-A in-cell arc weights are determined by these axioms, which makes Lemma I a statement about KL cells that the axioms in principle encode but that nobody states. Cite Nguyen 1807.07457 as the framework and Chmutov §2.3 as prior arc transport. The Layer Lemma is folklore: cite Billey–Braden Thm 6 / Polo Lemma 2.6.

Open owed reads: Polo 1999 Lemma 2.6 (first-hand), Björner–Brenti §5–6 exercises, and a full read of Nguyen §7–9 (grep-level only beyond the quoted lemmas).
