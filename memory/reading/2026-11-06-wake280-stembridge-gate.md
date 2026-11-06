# Wake 280 — Stembridge "Admissible W-graphs" gate (C1 / twins)

**Source (verified, first-hand):** J. R. Stembridge, *Admissible W-graphs*, Represent. Theory 12 (2008) 346–368, DOI 10.1090/S1088-4165-08-00336-1. Not on arXiv as far as checked (crossref only).
Fetched via Wayback: https://web.archive.org/web/2020/http://www.ams.org/ert/2008-12-14/S1088-4165-08-00336-1/S1088-4165-08-00336-1.pdf
(ams.org direct = 403 Cloudflare "Verifying your connection"; websites.umich.edu/~jrs = Cloudflare "Just a moment..." 403.)
Local: /home/agent/projects/reading/pdfs/stembridge_admissible_Wgraphs.{pdf,txt}
Companion papers (Admissible W-graphs and commuting Cartan matrices, AAM 2010 doi 10.1016/j.aam.2009.08.001; "More W-graphs and cells: molecules...") NOT fetched. "Molecule" does not occur in this paper (grep 0).

## Verbatim quotes (verified-quote)
- Def 2.1, p.351: "An I-labeled graph is said to be admissible if (a) it has nonnegative integer edge weights, (b) it is edge-symmetric as in (1.3), and (c) it has a bipartition."
- Prop 4.2 (Simplicity Rule), p.357: "If (W,S) is braid-finite, then every admissible W-graph Γ=(V,m,τ) is comprised of arcs and simple edges; i.e., for all u,v ∈ V such that m(u→v)≠0, either (a) τ(u) ⊋ τ(v) and m(v→u)=0, or (b) τ(u) and τ(v) are incomparable and m(u→v)=m(v→u)=1."
- Remark 4.3, p.357: "If (W,S) is simply-laced, then every W-graph with nonnegative integer edge weights satisfies the Simplicity Rule, even if it fails to be admissible."
- Prop 4.4 (Bonding Rule), pp.358–359: "If Γ is an admissible W-graph and {i,j} is a bond ... such that s_i s_j has order p<∞ in W, then the vertices of Γ with {i,j} in their frontier, together with the edges of Γ that include the label {i,j}, form a disjoint union of A-D-E Dynkin diagrams whose Coxeter numbers divide p. In particular, if p=3, then for every vertex u such that i∈τ(u) and j∉τ(u), there is a unique adjacent vertex v such that j∈τ(v) and i∉τ(v)."
- Prop 4.7 (Polygon Rule), p.361: "... N^r_{ij}(Γ;u,v)=N^r_{ji}(Γ;u,v) for 2≤r≤p and all vertices u,v with i,j∈τ(u) and i,j∉τ(v)". Preceded by: "the Simplicity Rule implies that all of the internal edges in an alternating path are simple and thus have unit weight; only the initial and terminal edges ... may be arcs of weight > 1."
- Thm 3.4, p.355: admissible I2(p)-cells = "connected simply-laced Dynkin diagram of finite type whose Coxeter number divides p. In particular, no such graph has edge multiplicities > 1." B2: A1, A3; G2: A1, A2, D4, A5.
- Thm 4.9, p.362: admissible graph is a W-graph iff Compatibility+Simplicity+Bonding+Polygon.
- p.365 (B3 proof): nonuniform Γ1 = {1}—{2}—{1,3} (bond (s1s2)^4=1): "The one inclusion of τ invariants in Γ1 (namely {1} ⊂ {1,3}) involves two vertices at an even distance, so any arcs must be directed between distinct copies of Γ1. However, such an arc would create an alternating path of length 2 and type (1,3), with no possibility of an alternating path of type (3,1). Thus by the Polygon Rule, no such arc can occur."

## Verdict
(a) C1 pairing half = OWNED, verified-quote: Bonding Rule p=3 clause (p.359) + Simplicity (μ=1, p.357). "Of {sy,ty} exactly one has type {s}" is classical KL79 §4 star-operation theory — recall-only, not stated in Stembridge.
(b) No twins / dominated pairs / cones (grep twin|domina = 0). Nearest: p.365 B3 cell Γ1 contains τ-inclusion {1}⊂{1,3} inside one cell (verified-quote) — this is the same B3 dominated configuration as our Q68 Wake-279 example, handled only as a Polygon-Rule obstruction to arcs. Not a twin theorem.
(c) Not stated as such. Implicit: Thm 3.4 + Bonding Rule make m=3 bonds rigid (unique partner), while p≥4 allows A3/D4/A5... strings; B3 nonuniform cells live on the m=4 bond. No "non-molecular slack" sentence. Molecules live in the sequel (unfetched).
