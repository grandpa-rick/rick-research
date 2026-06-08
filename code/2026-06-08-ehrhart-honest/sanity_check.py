"""
Sanity check: the AII n=2 lattice-counting data appears to contradict
Ehrhart theory (period should divide 6, but d^5(c)[N+6]-d^5(c)[N] != 0).

Possible bugs:
(a) Bug in count_aii_n2_all.
(b) Wrong polytope interpretation.
(c) I'm misremembering Ehrhart theory.

This script does:
1. Brute-force enumeration (4 nested loops, no shortcuts).
2. Direct check: count = #{(m_2, m_23, m_123, m_124) ≥ 0 integer :
   m_2 + 2 m_23 + m_123 + m_124 = w, m_123 <= m_2, m_124 <= m_23}.
3. Compare cumulative counts with extended_enum output.
4. If they match: the data is correct, so theory or polytope dim is wrong.
"""

import csv
from pathlib import Path

OUT_DIR = Path(__file__).parent


def brute_count_at_weight(w, N_search):
    """Count points of weight exactly w."""
    c = 0
    for m_2 in range(min(N_search, w) + 1):
        for m_23 in range(min(N_search, (w - m_2) // 2) + 1):
            partial = m_2 + 2 * m_23
            for m_123 in range(min(m_2, w - partial) + 1):
                m_124 = w - partial - m_123
                if 0 <= m_124 <= m_23:
                    c += 1
    return c


def main():
    print("# Brute-force sanity check")
    print()
    # Compare at small N
    for w in range(31):
        c = brute_count_at_weight(w, w)
        print(f"  weight={w}: count={c}")

    # Cumulative
    print()
    print("# Cumulative counts")
    cum = 0
    cum_brute = []
    for w in range(31):
        cum += brute_count_at_weight(w, w)
        cum_brute.append(cum)

    # Compare with raw_counts.csv
    raw = []
    with open(OUT_DIR / "raw_counts.csv") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            raw.append((int(row[0]), int(row[1]), int(row[2])))

    for N in range(31):
        c_brute = cum_brute[N]
        _, _, c_aii_csv = raw[N]
        match = "OK" if c_brute == c_aii_csv else "DIFFER"
        print(f"  N={N}: brute={c_brute}, csv={c_aii_csv}  {match}")

    # If they match, let's just print the exact-weight counts to look for
    # periodicity / quasipolynomial structure
    print()
    print("# Exact weight counts (Ehrhart of the slice {weight = N})")
    print("# This is a degree-3 quasipoly of the slice 3-dim polytope.")
    print()
    weights = list(range(61))
    f_N = [brute_count_at_weight(w, w) for w in weights]
    # Print finite differences
    for w in weights:
        print(f"  f({w}) = {f_N[w]}")

    def diff(s):
        return [s[i+1] - s[i] for i in range(len(s) - 1)]
    print()
    print("Finite differences of f_N (Ehrhart of slice):")
    d1 = diff(f_N); d2 = diff(d1); d3 = diff(d2); d4 = diff(d3); d5 = diff(d4)
    print(f"  d^1 tail: {d1[-12:]}")
    print(f"  d^2 tail: {d2[-12:]}")
    print(f"  d^3 tail: {d3[-12:]}")
    print(f"  d^4 tail: {d4[-12:]}")
    print(f"  d^5 tail: {d5[-12:]}")
    # d^4 of cumulative = d^3 of exact-weight count. So d^3 of f_N tail
    # being ±something matches.
    # For slice = 3-dim Ehrhart, period divides ? Let's see what period works.
    # If degree=3 period=6, d^4(f_N) within residue mod 6 should be 0.
    print()
    print("d^4(f_N)[N+6] - d^4(f_N)[N]:")
    for N in range(len(d4) - 6):
        if N < len(d4) - 18:
            continue
        print(f"  N={N+4}: {d4[N+6] - d4[N]}")


if __name__ == "__main__":
    main()
