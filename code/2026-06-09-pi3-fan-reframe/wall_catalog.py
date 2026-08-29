"""
Day 61 fan reframe — catalog of pullback walls.

For each of the 26 pieces of pi_3', compute:
  (1) The 5 BDI inequalities pulled back to AII (T_a >= 0 trivial; the
      nontrivial 5 are B_a - T_a >= 0, M_2 <= P_1, S <= P_2, plus M_1 = 0
      forced).
  (2) Of these 5*26 = 130 inequalities, which are AII-redundant (i.e.,
      always satisfied on P^AII_5)?
  (3) The REMAINING inequalities are the ACTIVE WALLS of piece i's
      pullback domain D_i = { p in P^AII_5 : pi^(i)(p) in P^BDI_3 }.

Then test FAN CONJECTURE: do the {D_i} form a fan?
  Specifically:
   - Is the AII polytope EQUAL to bigcup D_i (covering)?
   - Are pairwise intersections D_i cap D_j common faces?
   - Are the D_i 9-dim and (D_i cap D_j) lower-dim?

If the D_i overlap heavily (most have full domain), then they DON'T form
a fan in AII. The fan structure (if any) must come from elsewhere.

Test ALTERNATIVE: do the IMAGES C_i = pi^(i)(P^AII_5) form a fan in
BDI-space? Each C_i is a polyhedral cone in BDI; pairwise intersections
should be common faces.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
from verify_full_v7 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS, BDI_VARS

# AII polytope constraints (written as expressions >= 0):
# - Main_2: m_2 - m_12356 - m_1235 >= 0
# - Main_3: m_23 - m_12346 - m_1234 >= 0
# - Singleton L: m_12346 - m_1235 - m_2345 >= 0
# - Singleton R: m_23 + m_1235 + m_2345 - m_12346 >= 0
# - all m_X >= 0 (9 of these)
# Total: 4 + 9 = 13 AII inequalities.

# AII inequality matrix A: A[i] . p >= 0 for p in P^AII_5.
def aii_matrix():
    rows = []
    # 9 nonnegativity
    for i in range(9):
        v = [0]*9
        v[i] = 1
        rows.append(v)
    # Main_2: m_2 - m_12356 - m_1235 >= 0
    v = [0]*9
    v[AII_VARS.index("m_2")] = 1
    v[AII_VARS.index("m_12356")] = -1
    v[AII_VARS.index("m_1235")] = -1
    rows.append(v)
    # Main_3: m_23 - m_12346 - m_1234 >= 0
    v = [0]*9
    v[AII_VARS.index("m_23")] = 1
    v[AII_VARS.index("m_12346")] = -1
    v[AII_VARS.index("m_1234")] = -1
    rows.append(v)
    # Singleton L: m_12346 - m_1235 - m_2345 >= 0
    v = [0]*9
    v[AII_VARS.index("m_12346")] = 1
    v[AII_VARS.index("m_1235")] = -1
    v[AII_VARS.index("m_2345")] = -1
    rows.append(v)
    # Singleton R: m_23 + m_1235 + m_2345 - m_12346 >= 0
    v = [0]*9
    v[AII_VARS.index("m_23")] = 1
    v[AII_VARS.index("m_1235")] = 1
    v[AII_VARS.index("m_2345")] = 1
    v[AII_VARS.index("m_12346")] = -1
    rows.append(v)
    return sp.Matrix(rows)

AII_INEQ = aii_matrix()
AII_INEQ_LABELS = (
    [f"m_{v[2:]} >= 0" for v in AII_VARS] +
    ["Main_2", "Main_3", "Sing_L", "Sing_R"]
)


def piece_pullback_walls(name):
    """For piece i, return [(label, vector)] for the 5 nontrivial BDI
    inequalities pulled back to AII.

    Inequality is in form "vec . p >= 0". We extract:
      B_1 - T_1 >= 0   -> A[1] - A[2] >= 0
      B_2 - T_2 >= 0   -> A[3] - A[4] >= 0
      P_1 - M_2 >= 0   -> 2(A[1] - A[2]) - A[0] >= 0
      P_2 - S >= 0     -> 2(A[1] - A[2]) + 2(A[3] - A[4]) - A[5] >= 0
      T_1 >= 0         -> A[2] >= 0    (also include for completeness)
      T_2 >= 0         -> A[4] >= 0
    """
    A = piece_matrix(ALL_PI[name])
    walls = []
    # T_1 >= 0
    walls.append(("T_1", A[2, :]))
    # T_2 >= 0
    walls.append(("T_2", A[4, :]))
    # B_1 - T_1 >= 0
    walls.append(("B_1-T_1", A[1, :] - A[2, :]))
    # B_2 - T_2 >= 0
    walls.append(("B_2-T_2", A[3, :] - A[4, :]))
    # P_1 - M_2 >= 0
    walls.append(("P_1-M_2", 2*(A[1, :] - A[2, :]) - A[0, :]))
    # P_2 - S >= 0
    walls.append(("P_2-S", 2*(A[1, :] - A[2, :]) + 2*(A[3, :] - A[4, :]) - A[5, :]))
    return walls


def is_aii_redundant(vec):
    """Check if 'vec . p >= 0' is implied by AII_INEQ (always true on P^AII_5).

    Use LP / Farkas: vec . p >= 0 for all p in {p : A p >= 0}
      iff  vec is in cone of rows of A
      iff  exists lambda >= 0 such that vec = lambda^T A.

    Reformulated as LP feasibility: find lambda >= 0 with A^T lambda = vec.
    """
    # vec: 1x9 row vector
    # We want lambda >= 0 with A.T @ lambda = vec.T
    n_ineq = AII_INEQ.shape[0]
    A_T = AII_INEQ.T  # 9 x n_ineq
    vec_col = sp.Matrix([vec[i] for i in range(9)])
    # Solve linear system A.T @ lambda = vec_col with lambda >= 0
    # Try LP via scipy
    import numpy as np
    from scipy.optimize import linprog
    A_eq = np.array(A_T.tolist(), dtype=float)  # 9 x n_ineq
    b_eq = np.array([float(vec[i]) for i in range(9)])
    c = np.zeros(n_ineq)
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)]*n_ineq,
                  method='highs')
    return res.success


def main():
    print("=" * 78)
    print("DAY 61 — WALL CATALOG OF PIECE PULLBACK DOMAINS")
    print("=" * 78)

    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    print(f"\nPieces analyzed: {len(pieces)}")

    # For each piece, compute walls and check redundancy
    piece_active_walls = {}
    all_active_walls = []  # list of (piece_name, label, vec)

    for name in pieces:
        walls = piece_pullback_walls(name)
        active = []
        for label, vec in walls:
            # vec is a row vector (1x9)
            vec_list = [int(vec[0, j]) for j in range(9)]
            # Check redundancy
            if all(v == 0 for v in vec_list):
                # 0 >= 0, trivially true
                continue
            redundant = is_aii_redundant(vec_list)
            if not redundant:
                active.append((label, tuple(vec_list)))
                all_active_walls.append((name, label, tuple(vec_list)))
        piece_active_walls[name] = active

    # Per-piece summary
    print("\n--- Per-piece active walls ---")
    full_domain_count = 0
    for name in pieces:
        active = piece_active_walls[name]
        if not active:
            print(f"  {name}: FULL DOMAIN (no active walls)")
            full_domain_count += 1
        else:
            print(f"  {name}: {len(active)} active wall(s):")
            for label, vec in active:
                # Pretty-print
                terms = []
                for j, c in enumerate(vec):
                    if c != 0:
                        sgn = "+" if c > 0 else "-"
                        val = abs(c)
                        if val == 1:
                            terms.append(f"{sgn}{AII_VARS[j]}")
                        else:
                            terms.append(f"{sgn}{val}*{AII_VARS[j]}")
                print(f"    {label}: {' '.join(terms)} >= 0")
    print(f"\nPieces with FULL DOMAIN (no nontrivial constraints): {full_domain_count}/{len(pieces)}")

    # Distinct active wall normals
    print("\n--- Distinct active wall normals ---")
    normals = set()
    for (_, label, vec) in all_active_walls:
        # Normalize: gcd
        from math import gcd
        from functools import reduce
        g = reduce(gcd, [abs(v) for v in vec if v != 0])
        norm = tuple(v // g for v in vec)
        # Also flip sign so first nonzero is positive
        first_nz = next((v for v in norm if v != 0), 0)
        if first_nz < 0:
            norm = tuple(-v for v in norm)
        normals.add(norm)
    print(f"  Distinct wall normals (up to scaling/sign): {len(normals)}")
    for n in sorted(normals):
        terms = []
        for j, c in enumerate(n):
            if c != 0:
                sgn = "+" if c > 0 else "-"
                val = abs(c)
                if val == 1:
                    terms.append(f"{sgn}{AII_VARS[j]}")
                else:
                    terms.append(f"{sgn}{val}*{AII_VARS[j]}")
        print(f"    {' '.join(terms)}")

    # Coverage test: does union of D_i cover P^AII_5?
    # If most pieces have FULL DOMAIN, this is trivially yes.
    print("\n--- Coverage ---")
    if full_domain_count > 0:
        print(f"  YES — {full_domain_count} pieces have full AII domain.")
        print("  Union of D_i = P^AII_5 trivially.")
    else:
        print("  Need to check via covering analysis.")


if __name__ == "__main__":
    main()
