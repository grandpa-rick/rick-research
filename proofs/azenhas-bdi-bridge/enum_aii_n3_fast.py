"""
Faster enumeration of AII n=3 by integrating out m_12346 analytically.

For fixed (m_2, m_23, m_236, m_12356, m_1235, m_2345), m_12346 ranges
over [m_1235 + m_2345, m_1235 + m_2345 + m_23], an interval of width m_23 + 1
(assuming all constraints satisfied).
But we also need the SUM constraint:
   m_2 + m_23 + m_236 + m_12356 + m_12346 + m_1235 + m_2345 <= N

So m_12346 ranges over
   [m_1235 + m_2345, min(m_1235 + m_2345 + m_23, N - rest)]
where rest = m_2 + m_23 + m_236 + m_12356 + m_1235 + m_2345.
"""

import math


def enumerate_aii_n3(N):
    count = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            if m_2 + m_23 > N: break
            for m_236 in range(N+1):
                if m_2 + m_23 + m_236 > N: break
                for m_12356 in range(m_2 + 1):
                    for m_1235 in range(m_2 - m_12356 + 1):
                        rest_so_far = m_2 + m_23 + m_236 + m_12356 + m_1235
                        if rest_so_far > N: break
                        # m_2345 from 0
                        for m_2345 in range(N - rest_so_far + 1):
                            rest = rest_so_far + m_2345
                            # m_12346 lo = m_1235 + m_2345, hi = min(m_1235+m_2345+m_23, N-rest)
                            lo = m_1235 + m_2345
                            hi1 = lo + m_23
                            hi2 = N - rest
                            hi = min(hi1, hi2)
                            if hi >= lo:
                                count += hi - lo + 1
    return count


def main():
    print("AII n=3 lattice counts (extended):")
    counts = []
    for N in range(21):
        c = enumerate_aii_n3(N)
        counts.append(c)
        print(f"  N={N}: {c}")

    # Compare ratios with N^d / d! for various d
    print()
    print("Slope (log c_N+1 / log c_N) - dim estimate:")
    for i in range(5, len(counts)-1):
        if counts[i] > 0 and counts[i+1] > 0:
            slope = math.log(counts[i+1]/counts[i]) / math.log((i+1)/i)
            print(f"  N={i}->{i+1}: slope = {slope:.4f}")


if __name__ == "__main__":
    main()

# minor edit to change hash
