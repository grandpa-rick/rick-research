"""Compute K^{even}_m(l) = K_{mu', (2^{2l+1})} where mu = (2l, l+1+m, l+1-m).
Verify A_even = sum (-1)^m K^{even}_m = (-1)^{l+1}.
Also verify beta formula: beta_m = (-1)^{m+1}[(m+1)(2l+1) - delta_{m,l}].
"""

from kostka import kostka_mu_prime_2j

def K_even(l, m):
    """Kostka for even-parity mu at d_max, odd j."""
    if m > l - 1:
        return 0
    mu = (2*l, l+1+m, l+1-m)
    return kostka_mu_prime_2j(mu)

def K_odd_ballot(l, m):
    from math import comb
    return (comb(2*l+1, l-m) if l-m >= 0 else 0) - (comb(2*l+1, l-m-1) if l-m-1 >= 0 else 0)

def verify_A_even():
    print("A_even for odd j = 2l+1:")
    for l in range(1, 10):
        total = 0
        terms = []
        for m in range(l):
            K = K_even(l, m)
            sign = (-1)**m
            total += sign * K
            terms.append(f"({sign:+d})*{K}")
        expected = (-1)**(l+1)
        ok = "OK" if total == expected else "!!!"
        print(f"  l={l}: {' + '.join(terms)} = {total}  (expected {expected})  {ok}")

def verify_beta_identity():
    """beta_m = (-1)^{m+1}[(m+1)(2l+1) - delta_{m,l}].
    Need sum beta_m K^{odd}_m = (-1)^l.
    """
    print("\nsum beta K^{odd} = (-1)^l  (using conjectured beta formula):")
    for l in range(1, 10):
        total = 0
        for m in range(l + 1):
            beta = (-1)**(m+1) * ((m+1)*(2*l+1) - (1 if m == l else 0))
            K = K_odd_ballot(l, m)
            total += beta * K
        expected = (-1)**l
        ok = "OK" if total == expected else "!!!"
        print(f"  l={l}: sum = {total} (expected {expected})  {ok}")


if __name__ == "__main__":
    verify_A_even()
    verify_beta_identity()
