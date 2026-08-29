"""Weyl-formula approach: for 3-part mu,
  K_{mu', (2^j)} = sum over sigma in S_3 sgn(sigma) * multinomial(j; a_sigma, b_sigma, c_sigma)
where a_sigma, b_sigma, c_sigma are determined by matching exponents.

Details:
  rho = (m_1 + 2, m_2 + 1, m_3)
  For sigma = permutation of (2, 1, 0):
    A_sigma = m_1 + 2 - sigma_1
    B_sigma = m_2 + 1 - sigma_2
    C_sigma = m_3 - sigma_3
    Then in e_2^j = sum_{a+b+c=j} C(j; a,b,c) x_1^{a+b} x_2^{a+c} x_3^{b+c},
    matching x_1^A x_2^B x_3^C requires
      a + b = A, a + c = B, b + c = C
      => a = (A + B - C)/2, b = (A - B + C)/2, c = (-A + B + C)/2.
    Term = multinomial(j; a, b, c) if a, b, c are nonneg integers with a+b+c = j, else 0.
"""

from math import comb, factorial
from functools import reduce
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
from kostka import kostka_mu_prime_2j


def multinom(n, ks):
    """multinomial(n; ks) = n! / prod(k_i!) if sum(ks) == n else 0."""
    if any(k < 0 for k in ks):
        return 0
    if sum(ks) != n:
        return 0
    result = factorial(n)
    for k in ks:
        result //= factorial(k)
    return result


def kostka_weyl(mu):
    """Compute K_{mu', (2^j)} via Weyl-formula for 3-part mu."""
    m = list(mu) + [0] * (3 - len(mu))
    m1, m2, m3 = m[0], m[1], m[2]
    total_boxes = m1 + m2 + m3
    if total_boxes % 2 != 0:
        return 0
    j = total_boxes // 2
    rho = (m1 + 2, m2 + 1, m3)
    from itertools import permutations
    total = 0
    # tau iterates over permutations of (1, 2, 3) — the true S_3
    # pi(i) = 3 - tau(i) gives the exponent for row i in Delta.
    # sign(tau) = number of inversions in tau (as sequence)
    for tau in permutations([1, 2, 3]):
        inv = sum(1 for i in range(3) for j in range(i+1, 3) if tau[i] > tau[j])
        sign = (-1) ** inv
        pi = [3 - t for t in tau]  # exponents for x_1, x_2, x_3 from Delta
        A = rho[0] - pi[0]
        B = rho[1] - pi[1]
        C = rho[2] - pi[2]
        if A + B + C != 2 * j:
            continue  # sanity
        # a = (A + B - C)/2, b = (A - B + C)/2, c = (-A + B + C)/2
        if (A + B - C) % 2 != 0 or (A - B + C) % 2 != 0 or (-A + B + C) % 2 != 0:
            continue
        a = (A + B - C) // 2
        b = (A - B + C) // 2
        c = (-A + B + C) // 2
        if a < 0 or b < 0 or c < 0:
            continue
        term = multinom(j, [a, b, c])
        total += sign * term
    return total


def verify():
    print("=== Weyl formula verification ===\n")
    all_ok = True
    for l in range(1, 10):
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K_direct = kostka_mu_prime_2j(mu)
            K_weyl = kostka_weyl(mu)
            ok = "OK" if K_direct == K_weyl else "!!!"
            if K_direct != K_weyl:
                all_ok = False
                print(f"  MISMATCH l={l}, r={r}, mu={mu}: direct={K_direct}, weyl={K_weyl}")
    if all_ok:
        print("All Kostka values match via Weyl formula (up to l=9).")
    # Also check odd-spine
    print("\n=== Odd-spine cross-check ===")
    for l in range(1, 10):
        for r in range(l+1):
            if l - r < 0: continue
            mu = (2*l+1, l+1+r, l-r)
            if mu[2] < 0 or mu[1] > mu[0] or mu[2] > mu[1]: continue
            K_direct = kostka_mu_prime_2j(mu)
            K_weyl = kostka_weyl(mu)
            ok = "OK" if K_direct == K_weyl else "!!!"
            if K_direct != K_weyl:
                print(f"  MISMATCH l={l}, r={r}, mu={mu}: direct={K_direct}, weyl={K_weyl}")


def explicit_c2_formula():
    """Write out the six terms of Weyl formula for mu = (2l, l+1+r, l+1-r).
    rho = (2l+2, l+2+r, l+1-r).
    """
    print("\n=== Explicit 6-term formula for K_even(l, r) ===\n")
    print("mu = (2l, l+1+r, l+1-r), j = 2l+1")
    print("rho = (2l+2, l+2+r, l+1-r)")
    print("For each sigma perm of (2,1,0):")
    from itertools import permutations
    for sigma in permutations([2, 1, 0]):
        inv = sum(1 for i in range(3) for j in range(i+1, 3) if sigma[i] > sigma[j])
        sign = (-1) ** inv
        # A = 2l+2 - sigma[0], B = l+2+r - sigma[1], C = l+1-r - sigma[2]
        # a = (A+B-C)/2 = (2l+2-sigma0 + l+2+r-sigma1 - l-1+r+sigma2)/2
        #                = (2l+3+2r - sigma0 - sigma1 + sigma2)/2
        # b = (A-B+C)/2 = (2l+2-sigma0 - l-2-r+sigma1 + l+1-r-sigma2)/2
        #                = (2l+1-2r - sigma0 + sigma1 - sigma2)/2
        # c = (-A+B+C)/2 = (-2l-2+sigma0 + l+2+r-sigma1 + l+1-r-sigma2)/2
        #                = (1 + sigma0 - sigma1 - sigma2)/2
        sig_str = str(sigma)
        # a formula in terms of l, r:
        a_off = -sigma[0] - sigma[1] + sigma[2]  # so a = l + (3 + 2r + a_off)/2 + ... let me just print
        print(f"  sigma={sigma}, sign={sign:+d}:")
        print(f"    a = (2l+3+2r - {sigma[0]+sigma[1]-sigma[2]}) / 2 = l + {(3+2*(-sigma[0]-sigma[1]+sigma[2]))//2 + (0 if (3+2*(-sigma[0]-sigma[1]+sigma[2])) % 2 == 0 else '???')} + r")
        # Better: just compute for symbolic l, r
        # Let's evaluate at r=0, l = some values, see the formula
    print("\nLet me compute a, b, c as functions of (l, r) for each sigma:")
    for sigma in permutations([2, 1, 0]):
        inv = sum(1 for i in range(3) for j in range(i+1, 3) if sigma[i] > sigma[j])
        sign = (-1) ** inv
        # a = (A + B - C)/2, etc.
        # A = 2l+2 - s0, B = l+2+r - s1, C = l+1-r - s2
        # a = ((2l+2-s0) + (l+2+r-s1) - (l+1-r-s2))/2 = (2l + 3 + 2r + (-s0-s1+s2))/2
        # b = ((2l+2-s0) - (l+2+r-s1) + (l+1-r-s2))/2 = (2l + 1 - 2r + (-s0+s1-s2))/2
        # c = (-(2l+2-s0) + (l+2+r-s1) + (l+1-r-s2))/2 = (0 - 1 + (s0-s1-s2))/2 = (-1 + s0-s1-s2)/2
        s0, s1, s2 = sigma
        # a
        a_num_const = 3 + (-s0 - s1 + s2)  # then a = (2l + 2r + a_num_const)/2 = l + r + a_num_const/2
        b_num_const = 1 + (-s0 + s1 - s2)  # b = l - r + b_num_const/2
        c_num_const = -1 + (s0 - s1 - s2)  # c = c_num_const/2
        print(f"  sigma={sigma}, sign={sign:+d}: a = l + r + {a_num_const/2}, b = l - r + {b_num_const/2}, c = {c_num_const/2}")


if __name__ == "__main__":
    verify()
    explicit_c2_formula()
