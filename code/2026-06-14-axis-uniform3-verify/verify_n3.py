"""Verify R-double recipe V2 at n=3 using the full AII feasibility from verify_full.py."""
import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

from verify_full import (enumerate_aii_n3_full, bdi_feasible_n3, apply_pi)
from verify_full_v7 import ALL_PI

# Test the actual R-double pieces at n=3
print("Testing actual n=3 R-double pieces at N<=4:")
pts = enumerate_aii_n3_full(4)
print(f"# AII feasible points at sum<=4: {len(pts)}")

for name in ["R_double_m2345", "P5d_Rdouble_plus_m2", "P7_Rdouble_m2_dbl_S"]:
    spec = ALL_PI[name]
    bad = []
    for p in pts:
        q = apply_pi(spec, p)
        ok, err = bdi_feasible_n3(q)
        if not ok:
            bad.append((p, q, err))
    print(f"  {name}: {len(bad)} infeasible out of {len(pts)}")
    if bad:
        print(f"    First failure: p={bad[0][0]}, err={bad[0][2]}")

# Now check the 3 pieces differ ONLY in (S, m_2) entry
import sympy as sp
AII_VARS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346", "m_2345", "m_1235", "m_1234"]
BDI_VARS = ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]

def make_mat(name):
    spec = ALL_PI[name]
    A = sp.zeros(7, 9)
    for bi, bv in enumerate(BDI_VARS):
        for coef, av in spec.get(bv, []):
            ai = AII_VARS.index(av)
            A[bi, ai] = coef
    return A

mats = [make_mat(n) for n in ["R_double_m2345", "P5d_Rdouble_plus_m2", "P7_Rdouble_m2_dbl_S"]]
print("\nDifferences between R-double pieces (R_double_m2345 = α=0, P5d = α=1, P7 = α=2):")
for i in range(3):
    for j in range(i+1, 3):
        D = mats[i] - mats[j]
        nz = [(BDI_VARS[r], AII_VARS[c], int(D[r,c])) for r in range(7) for c in range(9) if D[r,c] != 0]
        print(f"  D[{i}][{j}]: {nz}")
