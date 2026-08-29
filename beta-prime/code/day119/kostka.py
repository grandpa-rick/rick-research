"""Kostka number computation and verification of identities (A) and (B).

K_{lambda, nu} = # SSYT of shape lambda, content nu.
We need K_{mu', (2^j)} for mu = (mu_1, mu_2, mu_3), |mu| = 2j.

Efficient approach: K_{mu', (2^j)} = [s_mu] e_2^j
via Pieri: e_2 * s_nu = sum over vertical 2-strips lambda >= nu.
So iterate: build up shape mu step by step adding vertical 2-strips (i.e., 2 boxes in distinct rows).
"""

from functools import lru_cache
from collections import defaultdict


def add_vertical_2strip(shape, max_len):
    """Given shape (tuple, mu_1 >= mu_2 >= ... >= 0), return list of shapes obtained by adding 2 boxes in different rows.
    max_len is max allowed length of partition (we cap at 3 for our problem)."""
    # pad shape to length max_len + 1 (allow adding to new row) with zeros
    s = list(shape) + [0] * (max_len + 1 - len(shape))
    # We add one box to each of two distinct rows i < j (0-indexed).
    # After adding, shape must remain a partition (weakly decreasing).
    # Adding to row i is allowed iff s[i] < s[i-1] (or i = 0).
    n = max_len + 1  # allow one extra row, but we'll truncate
    results = set()
    for i in range(n):
        for j in range(i+1, n):
            new_s = list(s)
            new_s[i] += 1
            new_s[j] += 1
            # check partition
            ok = True
            for k in range(len(new_s) - 1):
                if new_s[k] < new_s[k+1]:
                    ok = False
                    break
            if ok:
                # truncate trailing zeros
                while new_s and new_s[-1] == 0:
                    new_s.pop()
                if len(new_s) <= max_len:
                    results.add(tuple(new_s))
    return results


def kostka_mu_prime_2j(mu, max_len=None):
    """K_{mu', (2^j)} where |mu| = 2j.
    Compute [s_mu] e_2^j via iterated vertical 2-strip Pieri.
    max_len: max length of shapes (mu' can have up to mu_1 parts).
    """
    total = sum(mu)
    if total % 2 != 0:
        return 0
    j = total // 2
    if max_len is None:
        max_len = mu[0] if mu else 0  # mu' has mu_1 parts
    # Actually, since we're computing [s_mu] e_2^j and mu has length <= 3, mu' has parts of size <= 3.
    # We build shapes mu step by step, so shape has same # parts as mu.
    # Let's just track shapes as tuples of length up to len(mu).
    target_len = len(mu)
    # We only care about tracking shapes whose parts are at most mu_1 and whose length is at most target_len.
    counts = {(): 1}
    for step in range(j):
        new_counts = defaultdict(int)
        for shape, c in counts.items():
            for new_shape in add_vertical_2strip(shape, target_len):
                # early prune: check new_shape is componentwise <= mu (padded)
                dominated = True
                padded_ns = list(new_shape) + [0] * (target_len - len(new_shape))
                for a, b in zip(padded_ns, mu):
                    if a > b:
                        dominated = False
                        break
                if dominated:
                    new_counts[new_shape] += c
        counts = dict(new_counts)
    # Normalize mu by stripping trailing zeros (shapes are stored that way)
    mu_key = list(mu)
    while mu_key and mu_key[-1] == 0:
        mu_key.pop()
    return counts.get(tuple(mu_key), 0)


def d_mu(mu):
    """d_mu = mu_1 + floor((mu_2 + mu_3)/2)."""
    m1 = mu[0] if len(mu) > 0 else 0
    m2 = mu[1] if len(mu) > 1 else 0
    m3 = mu[2] if len(mu) > 2 else 0
    return m1 + (m2 + m3) // 2


def all_mu_3parts(twoj):
    """All partitions of 2j with at most 3 parts, as tuples (mu_1, mu_2, mu_3)."""
    for m1 in range(twoj + 1):
        for m2 in range(min(m1, twoj - m1) + 1):
            m3 = twoj - m1 - m2
            if m3 > m2:
                continue
            if m3 < 0:
                continue
            yield (m1, m2, m3)


def identity_A_sum(j, d):
    """Sum for identity (A): mu_1 = 2k where k = d - j, mu_2 - mu_3 even."""
    k = d - j
    if k < 1:
        return None  # only defined for d > j
    twoj = 2 * j
    m1 = 2 * k
    if m1 > twoj:
        return 0, []
    total = 0
    terms = []
    for m2 in range(min(m1, twoj - m1) + 1):
        m3 = twoj - m1 - m2
        if m3 > m2 or m3 < 0:
            continue
        mu = (m1, m2, m3)
        assert (m2 - m3) % 2 == 0
        sign = (-1) ** ((m2 - m3) // 2)
        K = kostka_mu_prime_2j(mu)
        total += sign * K
        terms.append((mu, sign, K))
    return total, terms


def identity_B_sum(j, d):
    """Sum for identity (B): mu_1 = 2k+1 where k = d - j, mu_2 - mu_3 odd."""
    k = d - j
    if k < 1:
        return None
    twoj = 2 * j
    m1 = 2 * k + 1
    if m1 > twoj:
        return 0, []
    total = 0
    terms = []
    for m2 in range(min(m1, twoj - m1) + 1):
        m3 = twoj - m1 - m2
        if m3 > m2 or m3 < 0:
            continue
        mu = (m1, m2, m3)
        assert (m2 - m3) % 2 == 1
        sign = (-1) ** ((m2 - m3 - 1) // 2)
        wt = (m2 - m3 + 1) // 2
        K = kostka_mu_prime_2j(mu)
        total += sign * wt * K
        terms.append((mu, sign, wt, K))
    return total, terms


if __name__ == "__main__":
    print("=== Sanity check: some Kostka numbers ===")
    for mu in [(2, 1, 1), (3, 1, 0), (4, 0, 0), (2, 2, 0), (3, 2, 1), (4, 2, 0), (6, 4, 2)]:
        j = sum(mu) // 2
        K = kostka_mu_prime_2j(mu)
        print(f"  K_{{mu'={mu[::-1] if True else mu}, (2^{j})}} = {K}, for mu={mu}")

    print("\n=== Verify Identity (A) for j in [1..12], d > j ===")
    all_A_zero = True
    for j in range(1, 13):
        for d in range(j+1, j + 20):
            res = identity_A_sum(j, d)
            if res is None:
                continue
            total, terms = res
            if not terms:
                continue
            marker = "OK" if total == 0 else f"!!! NONZERO = {total}"
            if total != 0:
                all_A_zero = False
                print(f"  j={j}, d={d}: {marker}")
                for mu, sign, K in terms:
                    print(f"    mu={mu}, sign={sign:+d}, K={K}")
    if all_A_zero:
        print("  Identity (A) VERIFIED for all tested (j, d).")

    print("\n=== Verify Identity (B) for j in [1..12], d > j ===")
    all_B_zero = True
    for j in range(1, 13):
        for d in range(j+1, j + 20):
            res = identity_B_sum(j, d)
            if res is None:
                continue
            total, terms = res
            if not terms:
                continue
            marker = "OK" if total == 0 else f"!!! NONZERO = {total}"
            if total != 0:
                all_B_zero = False
                print(f"  j={j}, d={d}: {marker}")
                for mu, sign, wt, K in terms:
                    print(f"    mu={mu}, sign={sign:+d}, wt={wt}, K={K}")
    if all_B_zero:
        print("  Identity (B) VERIFIED for all tested (j, d).")
