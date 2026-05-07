"""
Test (SA) at the bidegree level by computing matching via Hall's theorem.

For each B_n spin pair (λ, μ), at each bidegree (i, j):
  count even-length items, count odd-length items.
  Check #odd ≤ #even at every bidegree.

This DIRECTLY tests (SA) without needing to construct an injection explicitly.
"""

from fractions import Fraction
from collections import defaultdict
from aug_tilde_Bn import (
    weyl_Bn, all_kostant_partitions, bidegree_of_partition
)


def sa_check(lam, mu, N, verbose=False):
    """Check (SA) for a B_n spin pair at every bidegree."""
    rho = tuple(Fraction(2 * N - 1 - 2 * i, 2) for i in range(N))
    tilde_a_frac = tuple(Fraction(lam[i]) + rho[i] for i in range(N))
    b_frac = tuple(Fraction(mu[i]) + rho[i] for i in range(N))
    if not all(x.denominator == 1 for x in tilde_a_frac + b_frac):
        return None  # not spin
    tilde_a = tuple(int(x) for x in tilde_a_frac)
    b = tuple(int(x) for x in b_frac)

    weyl = weyl_Bn(N)
    even_count = defaultdict(int)
    odd_count = defaultdict(int)
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(N))
        if beta_w[0] < 0 or sum(beta_w) < 0:
            continue
        pis = all_kostant_partitions(beta_w, N)
        for pi in pis:
            bd = bidegree_of_partition(pi, N)
            if length % 2 == 0:
                even_count[bd] += 1
            else:
                odd_count[bd] += 1

    violations = []
    for bd, oc in odd_count.items():
        ec = even_count.get(bd, 0)
        if oc > ec:
            violations.append((bd, ec, oc))
    if verbose:
        print(f"λ={lam}, μ={mu}: {len(violations)} (SA) violations" if violations
              else f"λ={lam}, μ={mu}: ✓ (SA) holds at every bidegree")
        for bd, ec, oc in violations:
            print(f"  bd={bd}: even={ec}, odd={oc}")
    return len(violations) == 0


def main():
    F = Fraction
    half = F(1, 2)

    # B_3 dominant spin pairs, λ_1 ≤ 9/2
    print("=" * 60)
    print("B_3 dominant spin pairs, λ_1 ≤ 9/2")
    print("=" * 60)
    test_pairs = []
    for l1 in range(5):
        for l2 in range(l1 + 1):
            for l3 in range(l2 + 1):
                lam = (l1 + half, l2 + half, l3 + half)
                for m1 in range(l1 + 1):
                    for m2 in range(m1 + 1):
                        for m3 in range(m2 + 1):
                            mu = (m1 + half, m2 + half, m3 + half)
                            test_pairs.append((lam, mu))
    print(f"Total: {len(test_pairs)}")
    failures = []
    for lam, mu in test_pairs:
        ok = sa_check(lam, mu, 3, verbose=False)
        if ok is False:
            failures.append((lam, mu))
    print(f"Failures: {len(failures)}/{len(test_pairs)}")
    if failures:
        for lam, mu in failures[:5]:
            sa_check(lam, mu, 3, verbose=True)


if __name__ == "__main__":
    main()
