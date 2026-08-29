"""Explore: what is K_{(2l, l+1+r, l+1-r)', (2^{2l+1})} in closed form?

Setup: j = 2l+1 odd, d_max = 3l+1.
Even-parity spine (3-part): mu = (2l, l+1+r, l+1-r), for r = 0, 1, ..., l-1.
Sum: |mu| = 2l + 2(l+1) = 4l+2 = 2j.

Note: mu has 3 parts, so mu' has parts of size at most 3.
Column of mu' of index c has length = # rows of mu with mu_i >= c.

Column 1 length = 3 (all three parts nonempty when l >= 1, r < l).
Column 2 length = 2 (both mu_1 and mu_2 >= 2, since mu_2 = l+1+r >= l+1 >= 2 for l >= 1). Actually all three >= 2 when mu_3 = l+1-r >= 2 iff r <= l-1. So for r = l-1, mu_3 = 2. Good.
  Wait: column 2 length = # rows with mu_i >= 2. mu_3 = l+1-r. For r = l-1, mu_3 = 2, so column 2 length = 3.
  For r < l-1, mu_3 = l+1-r >= 3, so column 2 length = 3 (all 3 rows have mu_i >= 2, actually all >= 3 for smaller r).
  Hmm let's just compute.

For general r in [0, l-1]:
  mu_1 = 2l, mu_2 = l+1+r, mu_3 = l+1-r.
  So mu_3 >= 2 iff r <= l-1. Good, always in our range.
  mu' = conjugate.
  Column c length = # rows with mu_i >= c.
    c = 1: all 3 rows always.
    c = 2: 3 rows (since all mu_i >= 2 for l >= 1).
    c = 3: rows with mu_i >= 3. mu_1 = 2l >= 3 for l >= 2. mu_2 = l+1+r >= 3 for l+r >= 2. mu_3 = l+1-r >= 3 iff r <= l-2.
    c = 4: mu_1 = 2l >= 4 for l >= 2. mu_2 >= 4 iff l+r >= 3. mu_3 >= 4 iff r <= l-3.
    ...
    c = 2l: mu_1 = 2l (equality), mu_2 = l+1+r >= 2l iff r >= l-1. mu_3 = l+1-r >= 2l iff r <= 1-l (never for l >= 2).

Let's think of mu' as a partition of size 4l+2 with first part = 3.

Actually let me just compute lots and look at the numbers.
"""

from math import comb
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
from kostka import kostka_mu_prime_2j


def conjugate(mu):
    if not mu:
        return ()
    return tuple(sum(1 for x in mu if x > i) for i in range(mu[0]))


def survey_c2():
    print("=== (C2) Kostkas for even-parity 3-part spine ===\n")
    print("l  r  mu=(2l,l+1+r,l+1-r)   K   ballots to compare")
    for l in range(1, 10):
        j = 2*l+1
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K = kostka_mu_prime_2j(mu)
            # Try various guesses:
            # G1: comb(2l+1, l-r) - comb(2l+1, l-r-1) -- but for these Kostkas
            # G2: some Kostka-like ballot
            g1 = comb(2*l+1, l-r) - (comb(2*l+1, l-r-1) if l-r-1 >= 0 else 0)
            # G3: known formula for K_{(n,n,n)', (2^n)} = Catalan
            # G4: try Lindstrom-Gessel-Viennot style
            print(f"  l={l}, r={r}: mu={mu}, K={K}, ballot(2l+1,l-r)={g1}")
        print()


def compare_to_odd_spine_kostkas():
    """Compare (C2) even-spine Kostkas to (2A)/(2B) odd-spine Kostkas."""
    print("=== Compare even vs odd spine at same (l, r) ===\n")
    for l in range(2, 8):
        print(f"l = {l}:")
        for r in range(l+1):
            # Odd spine: mu = (2l+1, l+1+r, l-r), sign (-1)^r wt (r+1)
            if l - r >= 0:
                mu_odd = (2*l+1, l+1+r, l-r)
                K_odd = kostka_mu_prime_2j(mu_odd)
                ballot_odd = comb(2*l+1, l-r) - (comb(2*l+1, l-r-1) if l-r-1 >= 0 else 0)
                print(f"  r={r}: odd-spine mu={mu_odd}, K={K_odd}, ballot={ballot_odd}")
            if r < l:
                mu_even = (2*l, l+1+r, l+1-r)
                K_even = kostka_mu_prime_2j(mu_even)
                print(f"        even-spine mu={mu_even}, K={K_even}")


def try_binomial_diff():
    """Try K_even = C(2l+1, l-r) - C(2l+1, l-r-2), or similar."""
    print("\n=== Try C(2l+1, ?) formulas for K_even ===\n")
    for l in range(1, 8):
        print(f"l = {l}:")
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K = kostka_mu_prime_2j(mu)
            # Try: is K a Narayana number? A ballot? A LGV det?
            # NarayanaP(n, k) = (1/n) C(n, k) C(n, k-1)?
            # K_{(2l, l+1+r, l+1-r)', (2^{2l+1})} — hmm.
            g1 = comb(2*l+1, l-r) - comb(2*l+1, l-r-2) if l-r-2 >= 0 else comb(2*l+1, l-r)
            g2 = comb(2*l+1, l-r) - comb(2*l+1, l-r-1)  # ballot for 2l+1
            g3 = comb(2*l+2, l-r) - comb(2*l+2, l-r-1)  # ballot for 2l+2
            g3b = comb(2*l+2, l+1-r) - comb(2*l+2, l-r)  # ballot with j-shift
            # difference of ballots?
            print(f"  r={r}: K={K}, g1={g1}, g2={g2}, g3={g3}, g3b={g3b}")


def try_factor_out():
    """Try K = (2l+1) * f(l, r) or K / (something)"""
    print("\n=== Look for factors ===\n")
    for l in range(1, 8):
        print(f"l = {l} (2l+1 = {2*l+1}):")
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K = kostka_mu_prime_2j(mu)
            if K > 0:
                # try dividing
                print(f"  r={r}: K={K}, K/(2l+1)={K/(2*l+1):.4f}, K/C(2l+1,l-r)={K/comb(2*l+1,l-r):.4f}")


if __name__ == "__main__":
    survey_c2()
    compare_to_odd_spine_kostkas()
    try_binomial_diff()
    try_factor_out()
