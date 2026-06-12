"""
Day 66 PROVE Phase 1 — n=4 R-double backbone test.

Define the analog of R_double_m2345 at n=4 and test if α P1 in S admits
{0, 1, 2}-multiplicity, like at n=3.

The n=3 R-double:
  M_2:  m_12356  ( = L2 )
  B_1:  m_2 + 2 m_2345 + m_23456     ( = P1 + 2 S1 + L1 )
  T_1:  m_2345 + m_23456              ( = S1 + L1 )
  B_2:  m_23 + m_1235 + m_236         ( = P2 + S2 + P4-analog (P3 at n=3) )
  T_2:  m_1235 + m_236                ( = S2 + P4-analog )
  S:    m_12346 + 2 m_1234 + 2 m_2345 ( = L3 + 2 S3 + 2 S1 )
                                       (at n=3, L3 = m_12346 unconstrained, S3 = m_1234)
The α m_2 in S gives the 3 B0 pieces.

n=4 analog (using analog roles):
  M_2:  L2
  M_3:  L3
  B_1:  P1 + 2 S1 + L1     ← double S1 in B_1 (R-double signature)
  T_1:  S1 + L1
  B_2:  P2 + S2 + P4       ← P4 here as "free prefix"
  T_2:  S2 + P4
  B_3:  P3 + S3 + Λ
  T_3:  S3 + Λ
  S:    L4 + 2 S3 + 2 S1 + α P1   ← S3 doubled in S, S1 doubled in S (analog: 2 m_1234 + 2 m_2345)
"""
import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-12-n4-registry')

from n4_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS,
                       bdi_feasible_n4, aii_feasible_n4)

# Build piece_matrix and feasibility loop.
# enumerate AII at small N.
import itertools, numpy as np

def enumerate_aii_n4(N):
    pts = []
    for vec in itertools.product(range(N+1), repeat=12):
        if sum(vec) > N: continue
        ok, _ = aii_feasible_n4(vec)
        if ok:
            pts.append(vec)
    return pts

PREFIX_IDX = [0, 1, 2, 3]
LONG_IDX = [4, 5, 6, 7]
SHORT_IDX = [8, 9, 10]
LINKLHS_IDX = 11
# AII_VARS labels
P1, P2, P3, P4 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3]
L1, L2, L3, L4 = AII_VARS[4], AII_VARS[5], AII_VARS[6], AII_VARS[7]
S1, S2, S3 = AII_VARS[8], AII_VARS[9], AII_VARS[10]
LAMBDA = AII_VARS[11]

def make_r_double_n4(alpha):
    return {
        "M_2": [(1, L2)],
        "M_3": [(1, L3)],
        "B_1": [(1, P1), (2, S1), (1, L1)],
        "T_1": [(1, S1), (1, L1)],
        "B_2": [(1, P2), (1, S2), (1, P4)],
        "T_2": [(1, S2), (1, P4)],
        "B_3": [(1, P3), (1, S3), (1, LAMBDA)],
        "T_3": [(1, S3), (1, LAMBDA)],
        "S":   [(1, L4), (2, S3), (2, S1), (alpha, P1)],
    }

VAR_INDEX = {v: i for i, v in enumerate(AII_VARS)}

def apply_pi_n4(spec, p):
    """p is a length-12 AII vector. Apply spec to get length-9 BDI vector."""
    q = [0] * N_BDI
    for i, bdi in enumerate(BDI_VARS):
        s = 0
        for coef, av in spec.get(bdi, []):
            s += coef * p[VAR_INDEX[av]]
        q[i] = s
    return tuple(q)

print("=== n=4 R-double analog test (α P1 in S) ===")
N = 4
aii_pts = enumerate_aii_n4(N)
print(f"# AII pts at N={N}: {len(aii_pts)}")
for alpha in [0, 1, 2, 3]:
    spec = make_r_double_n4(alpha)
    bad = 0
    image = set()
    for p in aii_pts:
        q = apply_pi_n4(spec, p)
        ok, _ = bdi_feasible_n4(q)
        if not ok:
            bad += 1
        else:
            image.add(q)
    n_total = len(aii_pts)
    pct = 100.0 * (n_total - bad) / n_total if n_total else 0
    print(f"  α={alpha}: lands {n_total-bad}/{n_total} ({pct:.1f}%), image size {len(image)}")

print()
print("If α=0 fails too, the n=4 backbone is structurally infeasible.")
print("That would explain B0(n=4) = 0 (parity collapse).")
