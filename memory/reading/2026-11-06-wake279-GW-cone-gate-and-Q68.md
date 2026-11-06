# Wake 279 (2026-11-06) — Goertzen–Williamson cone gate + Q68 opened

## GW gate (first-hand, papers/GoertzenWilliamson_2604.18894.{pdf,txt})
- arXiv 2604.18894v1 [math.RT], Goertzen & Williamson, submitted 2026-04-20.
- Thm 4.5 cites Mejstrik–Protasov for uniqueness of the maximal invariant cone (irreducible modules).
- S_n Specht modules: C_KL is the maximal {1+s}-invariant cone for hooks (Thm 4.11), two-column (Thm 4.14), (n−2,2) (Thm 4.17); computed n ≤ 8; fails (non-simplicial maximal cone) at (4,4,1), Ex 4.21.
- W-graph convention C (Ex 4.7): (1+s)e_x = 0 if s∈D(x), else 2e_x + Σ_{y: s∈D(y)} μ(x,y) e_y.
- Other types: not addressed for cell modules. Only group-ring Problem 3.1 / Rem 3.3 (different question), quote:
  "We have verified that the Kazhdan–Lusztig basis at v = 1 is the unique solution to Problem 3.1, for all finite Coxeter groups with rank ≤ 3"
- Citers: none (Semantic Scholar, Wake 279).
- sources.json entry for 2604.18894 still says extraction=agent-summary — upgrade owed.

## Convention trap
C′ convention ((1+s)c_w = 2c_w for sw<w) ⇒ maximality fails already in S_4 (A3); that is the dual / w0-twisted question (= minimality for Γw0). Use GW convention C. (proofs/wake279/out_I2_Cp.txt, out_A3.txt)

## Scan (convention C; proofs/wake279/out_*.txt)
| type | result |
|---|---|
| A3 | all cells pass (calibrates GW) |
| D4 | irreducible cells (dims 3,4) pass; reducible dims 10,14 fail |
| I2(m), m=4,5,6,8 | middle cells (reducible) fail |
| B3 | all non-degenerate cells fail, incl. 6 irreducible 3-dim |
| H3 | all fail, incl. irreducible 5-dim; type 5_2 cells fail with no twin |
Dominated twin found: all B3 3-dim & 4-dim cells, every dihedral middle cell, 15/22 H3 cells; never A3, A4, D4.
Caveat: test (A) depth-limited; evidence = test (B) witnesses + twin lemma.

## B3 witness (computed, sympy exact, b3_witness.py; hand-check passed Wake 279)
Irreducible 3-dim left cell {x=s3s1, y=s2s3s1, z=s1s2s3s1}; D(x)={1,3}, D(y)={2}, D(z)={1}; edges x–y, y–z; μ(x,z)=0.
v=c_z−c_x: (1+s1)v=0, (1+s2)v=2v, (1+s3)v=2c_z. cone{c_x,c_y,v} invariant simplicial ⊋ C_KL; irreducible ⇒ unique C^max ⊋ C_KL.

## Dominated-twin lemma (sketched)
x≠z in Γ, D(z)⊆D(x), μ(y,z) ≥ μ(y,x) ∀y∈Γ with D(y)⊄D(x) ⇒ replacing c_z by c_z−c_x gives an invariant simplicial cone ⊋ C_KL.

## Open
- Hunch: simply-laced W have no dominated twin (twins need m≥4 strings x, s_j x, s_i s_j x). Data: A3, A4, D4.
- I2(4) middle / B3 4-dim cells: two distinct maximal pointed cones ⇒ "the maximal cone" ill-posed for reducible cells.
- H3 type 5_2: second obstruction mechanism, unknown.
- OWED: owner-risk read of Mejstrik–Protasov arXiv 2505.01229 (not yet read).

Registry: proofs/registry/seedQ2-kl-cone.json (Q68).
