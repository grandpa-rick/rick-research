"""Verify the closed form for K_even(l, r):

  K_even(l, r) = (2l+1) [C(2l, l-r) - C(2l, l-r-1)]
                 - [C(2l+1, l-r+1) - C(2l+1, l-r-1)]

Then plug into A_even(l) = sum_{r=0}^{l-1} (-1)^r K_even(l, r) and verify = (-1)^{l+1}.
"""

from math import comb
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
from kostka import kostka_mu_prime_2j


def K_even_closed(l, r):
    """Closed form via 4-term Weyl formula."""
    def c(n, k):
        return comb(n, k) if 0 <= k <= n else 0
    term1 = (2*l+1) * c(2*l, l-r)
    term2 = -(2*l+1) * c(2*l, l-r-1)
    term3 = -c(2*l+1, l-r+1)
    term4 = c(2*l+1, l-r-1)
    return term1 + term2 + term3 + term4


def verify_closed():
    print("=== Verify K_even closed form ===\n")
    all_ok = True
    for l in range(1, 12):
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K_direct = kostka_mu_prime_2j(mu)
            K_closed = K_even_closed(l, r)
            ok = "OK" if K_direct == K_closed else "!!!"
            if K_direct != K_closed:
                all_ok = False
                print(f"l={l}, r={r}: direct={K_direct}, closed={K_closed}  {ok}")
    if all_ok:
        print("All match!")


def verify_A_even_via_closed():
    print("\n=== Compute A_even(l) via closed form ===\n")
    for l in range(1, 15):
        total = 0
        for r in range(l):
            K = K_even_closed(l, r)
            total += (-1)**r * K
        expected = (-1)**(l+1)
        ok = "OK" if total == expected else "!!!"
        print(f"l={l}: A_even = {total}, expected {expected}  {ok}")


def analytical_reduction():
    """Simplify A_even(l) = sum_r (-1)^r K_even(l, r) symbolically."""
    print("\n=== Analytical reduction ===\n")
    # K_even(l, r) = (2l+1)[C(2l, l-r) - C(2l, l-r-1)] - [C(2l+1, l-r+1) - C(2l+1, l-r-1)]
    # A_even(l) = sum_{r=0}^{l-1} (-1)^r K_even(l, r)
    #
    # Split into 4 pieces:
    #   S1 = sum (-1)^r (2l+1) C(2l, l-r)  for r=0..l-1
    #   S2 = -sum (-1)^r (2l+1) C(2l, l-r-1) for r=0..l-1
    #   S3 = -sum (-1)^r C(2l+1, l-r+1) for r=0..l-1
    #   S4 = sum (-1)^r C(2l+1, l-r-1) for r=0..l-1
    from math import comb
    for l in range(1, 12):
        S1 = sum((-1)**r * (2*l+1) * comb(2*l, l-r) for r in range(l))
        S2 = -sum((-1)**r * (2*l+1) * (comb(2*l, l-r-1) if l-r-1 >= 0 else 0) for r in range(l))
        S3 = -sum((-1)**r * (comb(2*l+1, l-r+1) if l-r+1 <= 2*l+1 else 0) for r in range(l))
        S4 = sum((-1)**r * (comb(2*l+1, l-r-1) if l-r-1 >= 0 else 0) for r in range(l))
        total = S1 + S2 + S3 + S4
        # Expected: (-1)^(l+1)
        print(f"l={l}: S1={S1}, S2={S2}, S3={S3}, S4={S4}, S1+S2+S3+S4={total}, (-1)^{l+1}={(-1)**(l+1)}")


def analytical_2():
    """Combine S1+S2 = (2l+1) sum (-1)^r [C(2l, l-r) - C(2l, l-r-1)] for r=0..l-1
    = (2l+1) * (telescoping? or ballot-type sum).
    """
    from math import comb
    print("\n=== S1+S2 (2l+1)-scaled part ===\n")
    for l in range(1, 12):
        # sum (-1)^r ballot(2l, l-r) for r = 0..l-1
        # where ballot(n, k) = C(n, k) - C(n, k-1)
        S12 = sum((-1)**r * (comb(2*l, l-r) - (comb(2*l, l-r-1) if l-r-1 >= 0 else 0)) for r in range(l))
        # This is the "even j" identity from Day 119: sum (-1)^m [C(2l, l-m) - C(2l, l-m-1)] = 0
        # But summed r = 0..l-1 only (skips r = l).
        # At r = l: ballot(2l, l-l) - ballot(2l, l-l-1) = C(2l, 0) - 0 = 1.
        # So sum r=0..l = 0 => sum r=0..l-1 = -(-1)^l * 1 = (-1)^{l+1}.
        print(f"l={l}: S1+S2 = {(2*l+1)*S12}, i.e., (2l+1) * {S12}, (-1)^(l+1) = {(-1)**(l+1)}")


def analytical_3():
    """Reduce S3+S4."""
    from math import comb
    print("\n=== S3+S4 (constant-part) ===\n")
    for l in range(1, 12):
        # S3+S4 = sum (-1)^r [-C(2l+1, l-r+1) + C(2l+1, l-r-1)]
        # Let k = l - r (so r = l - k, r=0..l-1 => k = l..1)
        # (-1)^r = (-1)^{l-k}
        # = sum_{k=1}^{l} (-1)^{l-k} [-C(2l+1, k+1) + C(2l+1, k-1)]
        S34 = sum((-1)**r * (-((comb(2*l+1, l-r+1) if l-r+1 <= 2*l+1 else 0)) + (comb(2*l+1, l-r-1) if l-r-1 >= 0 else 0)) for r in range(l))
        print(f"l={l}: S3+S4 = {S34}")


if __name__ == "__main__":
    verify_closed()
    verify_A_even_via_closed()
    analytical_reduction()
    analytical_2()
    analytical_3()
