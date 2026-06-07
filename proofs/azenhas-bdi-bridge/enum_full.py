"""
Enumerate the full Azenhas AII polytopes at n=2, 3, 4 — using ALL
variables and ALL constraints from Theorems 6/7 and Corollaries 7/8.

n = 2 (Theorem 7 + Cor 7):
  Vars: m_2, m_23, m_124, m_123, slack m_{red^-1(u_1) \\ {4}} =: m_12
  Main_2 (combined): m_123 + m_12 <= m_2
  Linking eq: m_124 = m_12
  Cor 7 SPLIT inequalities: m_123 <= m_2 AND m_124 <= m_23
  (Combined+linking: m_123 + m_124 <= m_2, m_124 = m_12.)

  We use the SPLIT form from Cor 7 (which is what Azenhas establishes).
  Vars (after substituting m_12 = m_124): m_2, m_23, m_123, m_124.

n = 3 (Theorem 6 + Cor 6):
  Vars: prefix m_2, m_23, m_236;
        red^-1: m_23456 (= red^-1(2)), m_12356 (= red^-1(3)), m_12346 (= red^-1(6));
        slack: m_2345 (= red^-1(2)\\{6}), m_1235 (= red^-1(3)\\{6}), m_1234 (= red^-1(6)\\{6})
  So 9 variables.
  Constraints:
    Main_2: m_12356 + m_1235 <= m_2
    Main_3: m_12346 + m_1234 <= m_23
    Singleton: 0 <= m_12346 - m_1235 - m_2345 <= m_23

n = 4 (Theorem 7 + Cor 8):
  Vars: prefix m_2, m_23, m_236, m_2367
        red^-1: m_2345678, m_1235678, m_1234678, m_1234567 (red^-1 of u_1,2,3,4=2,3,6,7)
        slack (\\{8}): m_234567, m_123567, m_123467 (for i=1,2,3)
        linking LHS: m_1234568
  So 12 variables.
  Cor 8 SPLIT inequalities:
    m_1235678 + m_123567 <= m_2
    0 <= m_1234678 + m_123467 <= m_23
    0 <= m_1234567 <= m_236
  Linking eq: m_1234568 = m_234567 + m_123567 + m_123467
"""

import math


def enum_aii_n2(N):
    """
    n=2 AII: vars m_2, m_23, m_123, m_124 (m_14 = m_23 already substituted via linking).
    Inequalities (split from Cor 7):
      m_123 <= m_2
      m_124 <= m_23
    Sum <= N.

    NOTE: per verdict m_14 = m_23 is the linking equality. Let's count both
    with and without that 5th variable to see.

    Variant A (4 vars, split): m_2, m_23, m_123, m_124.
    Variant B (5 vars, with m_14 free + linking): same as A since m_14 = m_23 eliminates m_14.
    """
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            if m_2 + m_23 > N: continue
            for m_123 in range(min(m_2, N - m_2 - m_23) + 1):
                rest = N - m_2 - m_23 - m_123
                # m_124 ranges in [0, min(m_23, rest)]
                hi = min(m_23, rest)
                if hi < 0: continue
                count += hi + 1
    return count


def enum_aii_n2_verdict(N):
    """
    Verdict's variant: 5 vars (m_2, m_23, m_14, m_123, m_124) with m_14 = m_23.
    Sum includes m_14, so effective total is m_2 + 2*m_23 + m_123 + m_124.
    """
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            if m_2 + 2*m_23 > N: continue
            m_14 = m_23
            for m_123 in range(min(m_2, N - m_2 - 2*m_23) + 1):
                rest = N - m_2 - 2*m_23 - m_123
                hi = min(m_23, rest)
                if hi < 0: continue
                count += hi + 1
    return count


def enum_aii_n3_full(N):
    """
    Full n=3 polytope: 9 variables.
      Vars: m_2, m_23, m_236, m_23456, m_12356, m_12346, m_2345, m_1235, m_1234
    Constraints:
      Main_2: m_12356 + m_1235 <= m_2
      Main_3: m_12346 + m_1234 <= m_23
      Singleton: m_1235 + m_2345 <= m_12346 <= m_23 + m_1235 + m_2345
    Note: m_23456 is FREE — no Cor 6 constraint mentions it.
    """
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            if m_2 + m_23 > N: continue
            for m_236 in range(N + 1 - m_2 - m_23):
                rest1 = N - m_2 - m_23 - m_236
                # red^-1(2) = m_23456: free, ≤ rest1.
                # Loop over m_23456 last.
                # Main_2: 0 <= m_12356 + m_1235 <= m_2
                # Main_3: 0 <= m_12346 + m_1234 <= m_23
                # Singleton LB: m_12346 >= m_1235 + m_2345
                # Singleton UB: m_12346 <= m_23 + m_1235 + m_2345
                for m_12356 in range(min(m_2, rest1) + 1):
                    for m_1235 in range(min(m_2 - m_12356, rest1 - m_12356) + 1):
                        rest2 = rest1 - m_12356 - m_1235
                        for m_12346 in range(min(m_23, rest2) + 1):
                            for m_1234 in range(min(m_23 - m_12346, rest2 - m_12346) + 1):
                                rest3 = rest2 - m_12346 - m_1234
                                # m_2345 must satisfy:
                                #   m_2345 >= m_12346 - m_1235 - m_23 (Singleton UB)
                                #   m_2345 <= m_12346 - m_1235 (Singleton LB)
                                lo = max(0, m_12346 - m_1235 - m_23)
                                hi = min(rest3, m_12346 - m_1235)
                                if hi < lo: continue
                                # m_23456 free
                                # Total over m_2345 in [lo, hi] and m_23456 in [0, rest3 - m_2345]:
                                for m_2345 in range(lo, hi + 1):
                                    m_23456_max = rest3 - m_2345
                                    if m_23456_max < 0: continue
                                    count += m_23456_max + 1
    return count


def enum_aii_n3_cor6_only(N):
    """Cor 6 inequalities only (no Main_3). 7 vars + m_23456 free + m_1234 free."""
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            if m_2 + m_23 > N: continue
            for m_236 in range(N + 1 - m_2 - m_23):
                rest1 = N - m_2 - m_23 - m_236
                for m_12356 in range(min(m_2, rest1) + 1):
                    for m_1235 in range(min(m_2 - m_12356, rest1 - m_12356) + 1):
                        rest2 = rest1 - m_12356 - m_1235
                        for m_12346 in range(rest2 + 1):
                            for m_2345 in range(rest2 - m_12346 + 1):
                                # Singleton: m_1235 + m_2345 <= m_12346 <= m_23 + m_1235 + m_2345
                                if not (m_1235 + m_2345 <= m_12346 <= m_23 + m_1235 + m_2345):
                                    continue
                                rest3 = rest2 - m_12346 - m_2345
                                # m_23456 and m_1234 both free, sum <= rest3
                                # Number of (m_23456, m_1234) with m_23456, m_1234 >= 0, sum <= rest3
                                count += (rest3 + 1) * (rest3 + 2) // 2
    return count


def slope(counts, lo, hi):
    if counts[lo] <= 0 or counts[hi] <= 0: return None
    return math.log(counts[hi]/counts[lo]) / math.log(hi/lo)


def main():
    print("== AII n=2 (vars m_2, m_23, m_123, m_124, split inequalities) ==")
    counts = []
    for N in range(21):
        c = enum_aii_n2(N)
        counts.append(c)
        print(f"  N={N}: {c}")
    print(f"  slope 10->20: {slope(counts, 10, 20):.3f} (expect dim 4 → 4.0)")

    print()
    print("== AII n=2 (5 vars with m_14 = m_23 linking) ==")
    counts = []
    for N in range(21):
        c = enum_aii_n2_verdict(N)
        counts.append(c)
        print(f"  N={N}: {c}")
    print(f"  slope 10->20: {slope(counts, 10, 20):.3f}")

    print()
    print("== AII n=3 (full Theorem 6, 9 vars, Main_2 + Main_3 + Singleton) ==")
    counts = []
    for N in range(16):
        c = enum_aii_n3_full(N)
        counts.append(c)
        print(f"  N={N}: {c}")
    print(f"  slope 8->15: {slope(counts, 8, 15):.3f}")

    print()
    print("== AII n=3 (Cor 6 only, no Main_3, m_23456 and m_1234 free) ==")
    counts = []
    for N in range(13):
        c = enum_aii_n3_cor6_only(N)
        counts.append(c)
        print(f"  N={N}: {c}")
    print(f"  slope 8->12: {slope(counts, 8, 12):.3f}")


if __name__ == "__main__":
    main()
