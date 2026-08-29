"""Day 120 — For each j, list which d-values are ACHIEVED by some mu in support.

Support: {mu : |mu|=2j, ell<=3, K_{mu',(2^j)} > 0} = all such mu (since K>0 for
these).

For each d in [j+1, d_max], list mu with d_mu = d (leading contributors) and
mu with d_mu > d (subleading contributors, ordered by delta).
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts


def analyze(j):
    twoj = 2 * j
    support = []
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K > 0:
            support.append((mu, d_mu(mu), K))
    d_max = max(d for _, d, _ in support)
    # Bucket by d
    buckets = {}
    for mu, d, K in support:
        buckets.setdefault(d, []).append((mu, K))
    print(f"\n=== j = {j}, d_max = {d_max}, target: [t^d] S_j = 0 for d > {j} ===")
    print(f"  Buckets by d_mu:")
    for d in sorted(buckets.keys(), reverse=True):
        mus = buckets[d]
        parities = ["e" if (mu[1]-mu[2]) % 2 == 0 else "o" for mu, _ in mus]
        s = ", ".join(f"{mu}({p})K={K}" for (mu, K), p in zip(mus, parities))
        print(f"    d_mu = {d}: {s}")
    # Also print, for each d in (j, d_max], the delta of contributing mu's
    print(f"  For each d in (j, d_max]:")
    for d in range(j+1, d_max + 1):
        deltas_present = sorted(set(dv - d for _, dv, _ in support if dv >= d))
        print(f"    d={d}: contributors have delta in {deltas_present}")


if __name__ == "__main__":
    for j in range(2, 13):
        analyze(j)
