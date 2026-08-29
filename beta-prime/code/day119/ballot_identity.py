"""Verify the ballot formula for Kostka numbers at d = d_max, and the
alternating identity.

Claim (odd j = 2l+1):
   K_{(3^{l-m}, 2^{2m+1}, 1^{l-m}), (2^{2l+1})}  =  C(2l+1, l-m) - C(2l+1, l-m-1)  (ballot number)

Claim (even j = 2l):
   K_{(3^{l-m}, 2^{2m}, 1^{l-m}), (2^{2l})}  =  C(2l, l-m) - C(2l, l-m-1)  (ballot number)

Identity B (odd j):
   sum_{m=0}^{l} (-1)^m (m+1) K = 0.

Identity A (even j):
   sum_{m=0}^{l} (-1)^m K = 0.
"""

from math import comb
from kostka import kostka_mu_prime_2j

def conjugate(mu):
    if not mu:
        return ()
    return tuple(sum(1 for x in mu if x > i) for i in range(mu[0]))

def kostka_by_shape(shape, content):
    """Direct Kostka via SSYT enumeration."""
    # For our specific shape (3^a, 2^b, 1^c), we know column 1 must be sorted
    # (uses each number at most once), so this is actually a specific enumeration.
    # But let's do it generally.
    lam = list(shape)
    n_rows = len(lam)
    def enum(row_idx, prev_row, rem):
        if row_idx == n_rows:
            return 1 if all(c == 0 for c in rem) else 0
        row_len = lam[row_idx]
        def fill_row(pos, prev_val, row_so_far, r):
            if pos == row_len:
                # move to next row
                return enum(row_idx + 1, row_so_far, r)
            total = 0
            start = prev_val
            if pos == 0:
                start = 1
            for v in range(start, len(content) + 1):
                if r[v - 1] > 0:
                    # column strict: below prev_row[pos]
                    if pos < len(prev_row) and v <= prev_row[pos]:
                        continue
                    new_r = list(r)
                    new_r[v - 1] -= 1
                    total += fill_row(pos + 1, v, row_so_far + [v], new_r)
            return total
        return fill_row(0, 1, [], list(rem))
    return enum(0, [], list(content))


def verify_ballot_formula():
    print("=== Verify K = ballot number formula ===\n")
    print("Odd j (j = 2l+1):")
    for l in range(1, 8):
        j = 2 * l + 1
        print(f"  l = {l} (j = {j}):")
        for m in range(l + 1):
            shape = tuple([3]*(l - m) + [2]*(2*m + 1) + [1]*(l - m))
            mu = conjugate(shape)
            K = kostka_mu_prime_2j(mu)
            ballot = comb(2*l+1, l-m) - (comb(2*l+1, l-m-1) if l-m-1 >= 0 else 0)
            ok = "OK" if K == ballot else "!!!"
            print(f"    m={m}, shape={shape}, K={K}, ballot={ballot}  {ok}")
    print("\nEven j (j = 2l):")
    for l in range(1, 8):
        j = 2 * l
        print(f"  l = {l} (j = {j}):")
        for m in range(l + 1):
            shape = tuple([3]*(l - m) + [2]*(2*m) + [1]*(l - m))
            shape = tuple(x for x in shape if x > 0)  # remove empty
            mu = conjugate(shape)
            K = kostka_mu_prime_2j(mu)
            ballot = comb(2*l, l-m) - (comb(2*l, l-m-1) if l-m-1 >= 0 else 0) if l-m >= 0 else 0
            ok = "OK" if K == ballot else "!!!"
            print(f"    m={m}, shape={shape}, K={K}, ballot={ballot}  {ok}")


def verify_identity():
    print("\n=== Verify alternating identity ===\n")
    print("Identity B (odd j): sum (-1)^m (m+1) K = 0")
    for l in range(1, 15):
        j = 2 * l + 1
        total = 0
        for m in range(l + 1):
            shape = tuple([3]*(l - m) + [2]*(2*m + 1) + [1]*(l - m))
            K = comb(2*l+1, l-m) - (comb(2*l+1, l-m-1) if l-m-1 >= 0 else 0)
            total += (-1)**m * (m+1) * K
        ok = "OK" if total == 0 else f"!!! = {total}"
        print(f"  l = {l} (j = {j}): sum = {total}  {ok}")
    print("\nIdentity A (even j): sum (-1)^m K = 0")
    for l in range(1, 15):
        j = 2 * l
        total = 0
        for m in range(l + 1):
            K = comb(2*l, l-m) - (comb(2*l, l-m-1) if l-m-1 >= 0 else 0)
            total += (-1)**m * K
        ok = "OK" if total == 0 else f"!!! = {total}"
        print(f"  l = {l} (j = {j}): sum = {total}  {ok}")


if __name__ == "__main__":
    verify_ballot_formula()
    verify_identity()
