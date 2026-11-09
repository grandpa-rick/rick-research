# H3 5_2 KL-cone non-maximality: mechanism (wake286 compute, 2026-11-09)

Setting: GW convention C, as in wake279 `cell_module(...,'C')`: (1+s)c_w = 0 if s in D(w), otherwise 2c_w + sum_{z: s in D(z)} mu(z,w) c_z.
What test (B) does (wake279 cones.py): it perturbs to v = c_i - 0.05 c_j, closes the orbit of v under the (1+s) (only images leaving the orthant are kept), and checks that cone(orthant + orbit) is pointed and closed. "3 survivors" for 5_2 means the pairs (i,j) = (3,1), (4,0), (4,2) pass.

## 1. Matrices (cell of 12121; every 5_2 cell gives identical matrices)
Basis c0..c4 = 12121, 312121, 2312121, 12312121, 212312121. Descent sets D: {1,2}, {1,3}, {2,3}, {1,3}, {2}. The W-graph is the path 0-1-2-3-4 with all mu = 1.
**The matrices are integers, not merely elements of Z[phi]** (all in-cell mu are 1). Columns are the images:
- 1+s1 = [[0,0,0,0,0],[0,0,1,0,0],[0,0,2,0,0],[0,0,1,0,1],[0,0,0,0,2]]
- 1+s2 = [[0,1,0,0,0],[0,2,0,0,0],[0,1,0,1,0],[0,0,0,2,0],[0,0,0,1,0]]
- 1+s3 = [[2,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,2]]

5_1 = 5_2 ⊗ sgn (the descent sets are complements). These two are not Galois conjugates; both are rational representations.

## 2. Larger cones (all exact, sympy)
(a) **Coupled rational twin pair** (tsys.py). Take T = basis {c0, c1, c2, c3-c1, c4-c0}. Then T^{-1}(1+s)T >= 0 entrywise for every s, so T·orthant is a simplicial, invariant, pointed cone strictly containing C_KL. Neither substitution works alone: (1+s3)(c4-c0) = 2(c4-c0)+(c3-c1), and (1+s2)(c3-c1) = 2(c3-c1)+(c4-c0). Each pair fails the twin inequality only because of the other pair. Among 0/1 unipotent T with up to 3 off-diagonal entries, this T is the only minimal one, in all five 5_2 cells.

(b) **The unique maximal cone is irrational** (exact_max52.py, nice.py):
C_max = cone(c0, c1, c2, c3 - φc1, c4 - φc0 - φ^{-1}c2).
- Check: N^{-1}(1+s)N >= 0 exactly in Q(√5). For example (1+s3) has entry √5-1, and (1+s1) has entries 1+√5, (3+√5)/2 and (3-√5)/2.
- Why it is maximal (a dual argument). The dual cone K_0 = cone(e3, e4, e3+φ^{-1}e1, e2+φ^{-1}e4, e4+φ^{-1}e0) is simplicial and invariant under the transposes (R^{-1}B_sR >= 0 exactly). Each of its rays is the Perron vector of a word in B_s = (1+s)^T. The words are s1s3s2, s1s3, s1s2, s2s1 and s2s1s2s3, with dominant eigenvalues 2, 4, φ², φ², φ². Each eigenvalue is algebraically simple and strictly dominant, and each left eigenvector is >= 0; all of this is verified exactly. Because of that, every full-dimensional B-invariant cone inside the orthant contains K_0. So **every invariant pointed cone containing C_KL lies in K_0^* = C_max**, which makes C_max the unique maximum.
- C_max contains both T·orthant and the test-(B) family c4 - t c2. That family is invariant and pointed exactly for t <= 1/φ: a facet normal has c1-coefficient 2(1-t-t²)/(t(t+3)). At t = 1/φ it was verified exactly (verify_phi.py).
- This holds for all five 5_2 cells.

## 3. Mechanism
The hypothesis is confirmed in refined form. The maximal cone is an **irrational twin system**: two simultaneous substitutions, c3 → c3 - φc1 and c4 → c4 - φc0 - φ^{-1}c2, with coefficients in Q(√5) \ Q. The φ comes from the I2(5) products: (1+s1)(1+s2) has eigenvalue φ². The *failure* of maximality, though, is already witnessed rationally, by the coupled 0/1 twin pair in (a). "No twin" in wake279 meant only that no single pair passes the twin inequality.

## 4. Controls: the 5_1 cells (all 5 identical)
- They fail too, through the Thm B single twin c2 → c2 - c0 (pair (0,2), exact).
- A unique maximum K_0^* still exists, by the same forcing argument. But its number of extreme rays keeps growing with word length: 13, 20, 27, 32 at L = 4, 6, 8, 10, and ray ratios approach φ. So it looks **non-polyhedral** (numerical only).

## Grades
- (1), (2a), (2b) and the 5_2 maximality are **computed exact**; the Perron-forcing argument amounts to a proof given the code.
- The 1/φ threshold is also exact: c4 - t c2 lies in C_max iff its c2-coordinate 1/φ - t is >= 0 (bisection agrees, 0.61803402).
- 5_1 non-polyhedral: **hunch**.
