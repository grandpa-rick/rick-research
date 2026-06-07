"""
Push lattice enumeration to higher N to nail down the dimension.

Use Ehrhart-style growth: c_N / N^d → vol(P)/d! as N → infinity.
We fit log c_N = d log N + const using regression on the tail.
"""

from itertools import product
import math

def enumerate_bdi(n, N):
    count = 0
    if n == 2:
        for B1 in range(N+1):
            for T1 in range(B1+1):
                P1 = 2*(B1 - T1)
                for S in range(P1+1):
                    if B1 + T1 + S <= N:
                        count += 1
        return count
    elif n == 3:
        for B1 in range(N+1):
            for T1 in range(B1+1):
                P1 = 2*(B1 - T1)
                for B2 in range(N+1):
                    for T2 in range(N+1):
                        P2 = P1 + 2*(B2 - T2)
                        if P2 < 0: continue
                        if B1+T1+B2+T2 > N: continue
                        for M2 in range(min(P1, P2)+1):
                            for S in range(P2+1):
                                tot = B1+T1+M2+B2+T2+S
                                if tot <= N:
                                    count += 1
        return count


def enumerate_azenhas_n3_loose(N):
    """
    7 vars: m_2, m_23, m_236, m_12356, m_12346, m_1235, m_2345
    Constraints from Cor 6:
      C1: m_12356 + m_1235 <= m_2
      C2: m_1235 + m_2345 <= m_12346  (lower bound on diff)
      C3: m_12346 - m_1235 - m_2345 <= m_23 (upper bound on diff)
    """
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            if m_2 + m_23 > N: continue
            for m_236 in range(N+1):
                if m_2 + m_23 + m_236 > N: continue
                for m_12356 in range(m_2 + 1):
                    for m_1235 in range(m_2 - m_12356 + 1):
                        rest_max = N - (m_2 + m_23 + m_236 + m_12356 + m_1235)
                        if rest_max < 0: continue
                        # m_2345 from 0 to rest_max; m_12346 from 0 to rest_max
                        # constraints:
                        #   m_2345 + m_12346 + 0 <= rest_max
                        #   m_1235 + m_2345 <= m_12346
                        #   m_12346 - m_1235 - m_2345 <= m_23
                        for m_2345 in range(rest_max + 1):
                            lo = m_1235 + m_2345
                            hi_from_total = rest_max - m_2345
                            hi_from_C3 = m_1235 + m_2345 + m_23
                            hi = min(hi_from_total, hi_from_C3)
                            if lo > hi: continue
                            count += hi - lo + 1
    return count


def enumerate_azenhas_n3_strict(N):
    """
    Same as loose, but ALSO impose the Main_3 inequality:
      m_red^-1(u_3) + m_red^-1(u_3) \ {2n} <= m_{u_1 u_2} = m_{23}
    For n=3, u_3 = 6 = 2n.
    The red^-1(u_3) here might be m_23456 or similar new variable.
    But if we identify m_red^-1(u_3) with m_12346 (from Cor 6's singleton),
    then this is something like 'm_12346 + (slack at level 3) <= m_23'.
    Without a clean interpretation, omit.
    """
    pass


def main():
    print("BDI lattice counts (extended N):")
    print("n=2:")
    counts_b2 = []
    for N in range(15):
        c = enumerate_bdi(2, N)
        counts_b2.append(c)
        print(f"  N={N}: {c}")

    print("n=3 (slow):")
    counts_b3 = []
    for N in range(11):
        c = enumerate_bdi(3, N)
        counts_b3.append(c)
        print(f"  N={N}: {c}")

    print()
    print("Azenhas n=3 (Cor 6 constraints only):")
    counts_a3 = []
    for N in range(11):
        c = enumerate_azenhas_n3_loose(N)
        counts_a3.append(c)
        print(f"  N={N}: {c}")

    # Linear regression of log c_N vs log N for last 4 values
    def linreg(counts):
        xs = []
        ys = []
        for i in range(max(1, len(counts)-5), len(counts)):
            if counts[i] > 0:
                xs.append(math.log(i))
                ys.append(math.log(counts[i]))
        n = len(xs)
        mx = sum(xs)/n
        my = sum(ys)/n
        num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
        den = sum((xs[i]-mx)**2 for i in range(n))
        slope = num/den
        return slope

    print()
    print(f"BDI n=2: regression dim = {linreg(counts_b2):.3f} (expected 3)")
    print(f"BDI n=3: regression dim = {linreg(counts_b3):.3f} (expected 6)")
    print(f"AII n=3 (Cor 6 only): regression dim = {linreg(counts_a3):.3f}")


if __name__ == "__main__":
    main()
