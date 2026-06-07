"""
Enumerate BDI and Azenhas (AII) polytopes at n=3 and n=4 to determine
their dimensions empirically.

We fit lattice-point counts |P ∩ Z^k|_{sum ≤ N} ~ c N^d to recover d = dim.

BDI P_n:
  Vars: M_1, ..., M_{n-1}, B_1, ..., B_{n-1}, T_1, ..., T_{n-1}, S
  with M_1 forced to 0 via L_1.
  Inequalities:
    M_a ≤ P_{a-1}  (L_a)
    M_a ≤ P_a      (U_a)
    S   ≤ P_{n-1}  (E)
  where P_a = sum_{b≤a} 2(B_b - T_b).
  Equivalently P_a ≥ 0 (else M_a or S becomes negative).

Azenhas n=3 (odd, Theorem 6):
  Vars: m_2, m_23, m_236, m_12356, m_12346, m_1235, m_2345
  Inequalities (from Corollary 6):
    m_12356 + m_1235 ≤ m_2
    0 ≤ m_12346 - m_1235 - m_2345 ≤ m_23

Azenhas n=4 (even, Theorem 7):
  Vars: m_2, m_23, m_236, m_2367
        plus 4 "red^-1(u_i)" length-7 vars
        plus 3 "slack" length-6 vars
        plus 1 linking var (or absorbed)
  Inequalities (Main_i): m_{red⁻¹(u_i)} + m_{red⁻¹(u_i)\{2n}} ≤ m_{u_1...u_{i-1}}, i=2,...,n
  Linking equality: m_{12...(2n-2)·2n} = sum of slacks.

We'll do empirical fits to determine dimensions.
"""

from itertools import product
import math

def enumerate_bdi(n, N):
    """Enumerate BDI lattice points at level n, sum ≤ N."""
    count = 0
    # Variables: B_1..B_{n-1}, T_1..T_{n-1}, M_2..M_{n-1}, S (M_1=0 forced)
    if n == 2:
        for B1 in range(N+1):
            for T1 in range(B1+1):  # T1 ≤ B1 enforces P_1 ≥ 0
                P1 = 2*(B1 - T1)
                for S in range(P1+1):
                    if B1 + T1 + S <= N:
                        count += 1
        return count
    elif n == 3:
        # Vars: B1, T1, M2, B2, T2, S; M1=0
        for B1 in range(N+1):
            for T1 in range(N+1):
                P1 = 2*(B1 - T1)
                if P1 < 0: continue
                for B2 in range(N+1):
                    for T2 in range(N+1):
                        P2 = P1 + 2*(B2 - T2)
                        if P2 < 0: continue
                        for M2 in range(min(P1, P2)+1):
                            for S in range(P2+1):
                                tot = B1+T1+M2+B2+T2+S
                                if tot <= N:
                                    count += 1
        return count
    elif n == 4:
        # Vars: B1, T1, M2, B2, T2, M3, B3, T3, S; M1=0
        for B1 in range(N+1):
            for T1 in range(B1+1):  # bound T1 since P1 ≥ 0 requires T1 ≤ B1 if no neg later
                # Actually P_1 ≥ 0 needs B1 ≥ T1. P_2 = P_1 + 2(B2-T2), need ≥ 0.
                P1 = 2*(B1-T1)
                if P1 < 0: continue
                for B2 in range(N+1):
                    for T2 in range(N+1):
                        P2 = P1 + 2*(B2-T2)
                        if P2 < 0: continue
                        if B1+T1+B2+T2 > N: continue
                        for B3 in range(N+1):
                            for T3 in range(N+1):
                                P3 = P2 + 2*(B3-T3)
                                if P3 < 0: continue
                                if B1+T1+B2+T2+B3+T3 > N: continue
                                for M2 in range(min(P1,P2)+1):
                                    for M3 in range(min(P2,P3)+1):
                                        for S in range(P3+1):
                                            tot = B1+T1+M2+B2+T2+M3+B3+T3+S
                                            if tot <= N:
                                                count += 1
        return count


def enumerate_azenhas_n3(N):
    """
    Azenhas n=3 polytope, 7 vars:
      m_2, m_23, m_236, m_12356, m_12346, m_1235, m_2345
    Inequalities:
      m_12356 + m_1235 ≤ m_2
      0 ≤ m_12346 - m_1235 - m_2345 ≤ m_23
    All vars ≥ 0.

    Note: m_236 is free (only constrained by sum ≤ N).
    """
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            for m_236 in range(N+1):
                if m_2 + m_23 + m_236 > N: continue
                for m_12356 in range(m_2 + 1):
                    for m_1235 in range(m_2 - m_12356 + 1):
                        # m_12356 + m_1235 ≤ m_2 ✓
                        for m_2345 in range(N+1):
                            for m_12346 in range(N+1):
                                # 0 ≤ m_12346 - m_1235 - m_2345 ≤ m_23
                                diff = m_12346 - m_1235 - m_2345
                                if not (0 <= diff <= m_23): continue
                                tot = m_2 + m_23 + m_236 + m_12356 + m_12346 + m_1235 + m_2345
                                if tot <= N:
                                    count += 1
    return count


def main():
    print("BDI lattice counts:")
    print("n=2:")
    counts_b2 = []
    for N in range(8):
        c = enumerate_bdi(2, N)
        counts_b2.append(c)
        print(f"  N={N}: {c}")

    print("n=3:")
    counts_b3 = []
    for N in range(7):
        c = enumerate_bdi(3, N)
        counts_b3.append(c)
        print(f"  N={N}: {c}")

    print()
    print("Azenhas (AII_5) at n=3:")
    counts_a3 = []
    for N in range(7):
        c = enumerate_azenhas_n3(N)
        counts_a3.append(c)
        print(f"  N={N}: {c}")

    # Asymptotic estimate: if count ~ c N^d, log count ~ d log N + const
    print()
    print("Power-law fits (last two ratios):")
    def fit(counts):
        # Use last 3 entries
        ratios = []
        for i in range(2, len(counts)-1):
            if counts[i] > 0:
                # log(c_{N+1}/c_N) ≈ d log((N+1)/N)
                r = math.log(counts[i+1]/counts[i]) / math.log((i+1)/i)
                ratios.append((i, r))
        return ratios
    print("  BDI n=2:", fit(counts_b2))
    print("  BDI n=3:", fit(counts_b3))
    print("  AII n=3:", fit(counts_a3))


if __name__ == "__main__":
    main()

# minor edit to change hash
