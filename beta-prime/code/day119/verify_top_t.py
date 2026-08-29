"""Verify top-t parts of s*_mu and Kostka numbers using SymPy directly."""

import sympy as sp
from sympy import symbols, expand, Poly, Integer, factorial

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts

# Cross-check Kostka via sympy
from sympy.combinatorics.partitions import Partition


def kostka_via_sympy(lam, mu):
    """K_{lam, mu} via sympy or direct enumeration."""
    # Direct SSYT enumeration for shapes with few boxes.
    # Represent SSYT as list of rows.
    n_rows = len(lam)
    if n_rows == 0:
        return 1 if len(mu) == 0 else 0
    # Enumerate.
    def enum(row_idx, prev_row, remaining_content, current_tableau):
        if row_idx == n_rows:
            return 1 if all(c == 0 for c in remaining_content) else 0
        row_len = lam[row_idx]
        count = 0
        # Fill this row weakly increasing, strictly > column above
        def fill_row(pos, prev_val, row_so_far, rem):
            if pos == row_len:
                min_needed = 1
                # Column-strict: for each column c, this row's val > prev_row[c] if exists
                for c in range(row_len):
                    if c < len(prev_row) and row_so_far[c] <= prev_row[c]:
                        return 0
                return enum(row_idx + 1, row_so_far, rem, None)
            total = 0
            start = prev_val
            if pos == 0:
                start = 1
            for v in range(start, len(mu) + 1):
                if rem[v-1] > 0:
                    # column-strict check with prev row
                    if pos < len(prev_row) and v <= prev_row[pos]:
                        continue
                    new_rem = list(rem)
                    new_rem[v-1] -= 1
                    total += fill_row(pos + 1, v, row_so_far + [v], new_rem)
            return total
        count += fill_row(0, 1, [], list(remaining_content))
        return count
    return enum(0, [], list(mu), None)


def conjugate(mu):
    if not mu:
        return ()
    return tuple(sum(1 for x in mu if x > i) for i in range(mu[0]))


def check_kostka():
    print("=== Kostka cross-check ===")
    for mu in [(4,3,3), (4,4,2), (5,3,2), (5,4,1), (5,5,0), (3,3,2), (2,2,2), (6,4,2)]:
        j = sum(mu) // 2
        K_mine = kostka_mu_prime_2j(mu)
        muprime = conjugate(mu)
        K_direct = kostka_via_sympy(list(muprime), [2]*j)
        status = "OK" if K_mine == K_direct else "!!!MISMATCH!!!"
        print(f"  mu={mu}, mu'={muprime}, j={j}: K_mine={K_mine}, K_direct={K_direct}  {status}")


if __name__ == "__main__":
    check_kostka()
