"""
Enumerate BDI B_2 chain-HW polytope lattice points and compare with
Azenhas's n=2 (AII_3) k-highest weight family.

Goal: test whether there's a natural bijection between the two combinatorial
families that would lift the Azenhas inequalities to the BDI facets.

BDI B_2 chain-HW polytope P_n:
    (M_1, B_1, T_1, S) in Z_{>=0}^4
    L_1: M_1 <= 0       (degenerate -> M_1 = 0)
    U_1: M_1 <= 2(B_1 - T_1)   (redundant given L_1 + E)
    E:   S <= 2(B_1 - T_1)

So lattice points: M_1 = 0, T_1 <= B_1, 0 <= S <= 2(B_1 - T_1).

Azenhas n=2 AII_3 k-highest weight tableaux (Corollary 7):
    Family of patterns (117) and (118). Each is parameterised by a
    slack vector r and gives a tableau in SST_4(lambda) with
    multiplicities (m_2, m_23, m_123, m_124, m_14, ...).
    Inequalities: m_123 <= m_2, m_124 <= m_23.
    Equality:   m_14 = m_23  (from Theorem 7 with n=2).

In Corollary 7 the slack sequence r = (1,...,1, 2,...,2, 3,...,3, (),...,())
has integer multiplicities (#1's, #2's, #3's, M).
The induced tableau (117) has #2 copies of column (2), #1 copies of column (23),
extra 3 contributions giving columns (123), (124)...

Let me just count lattice points in both polytopes at small total weight
and see if the f-vectors agree.
"""

from itertools import product

def enumerate_bdi_b2(N):
    """Enumerate BDI HW Kostant partitions with total mult <= N."""
    out = []
    for B in range(N+1):
        for T in range(B+1):
            d = B - T
            for S in range(2*d+1):
                if B + T + S <= N:
                    out.append((0, B, T, S))
    return out


def azenhas_n2_polytope(N):
    """
    Azenhas n=2 lattice points in the inequality system:
    m_123 <= m_2, m_124 <= m_23, m_14 = m_23, all >= 0.
    For a fair count, we count (m_2, m_23, m_123, m_124, m_14) with
    m_14 = m_23 and total sum <= N.
    """
    out = []
    # Vars: m_2, m_23, m_123, m_124
    # m_14 = m_23
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            m_14 = m_23
            for m_123 in range(m_2+1):
                for m_124 in range(m_23+1):
                    tot = m_2 + m_23 + m_123 + m_124 + m_14
                    if tot <= N:
                        out.append((m_2, m_23, m_123, m_124, m_14))
    return out


def main():
    print("BDI B_2 lattice counts (|pi| <= N):")
    for N in range(8):
        n = len(enumerate_bdi_b2(N))
        print(f"  N={N}: {n}")
    print()
    print("Azenhas n=2 lattice counts in the (m_2, m_23, m_123, m_124, m_14) polytope (sum <= N):")
    for N in range(8):
        n = len(azenhas_n2_polytope(N))
        print(f"  N={N}: {n}")


if __name__ == "__main__":
    main()
