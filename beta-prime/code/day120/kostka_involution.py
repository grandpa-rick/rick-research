"""Day 120 — Look for a Kostka-preserving involution.

Given the parity split fails at d < d_max, we want an involution I on the support
such that:
  1) I preserves K_{mu', (2^j)}  (or scales it in a controlled way)
  2) I flips parity of (mu_2 - mu_3)
  3) I acts on the [t^d] contribution in a way that induces cancellation.

Try Bender-Knuth-style involutions:
  - On mu' (the conjugate). mu' has parts of size <= 3, weight 2^j.
    K_{mu', (2^j)} = # SSYT of shape mu' filled with entries 1, ..., j each twice.
    Bender-Knuth (i, i+1) swap is an involution on SSYT preserving content up to
    (m_i, m_{i+1}) swap. Here content is (2, 2, ..., 2, ...) so BK on (i, i+1)
    swaps 2 with 2 which does nothing.

  - However Ilona Naor / Bender-Knuth on the SHAPE side: switch mu <-> nu where
    (mu_2, mu_3) or (mu_1, mu_2, mu_3) get modified.

Let me just search combinatorially: for each pair (mu, nu) with |mu|=|nu|=2j and
different parity, list all pairs where K_mu' = K_nu' and see if any pattern
emerges.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts


def parity(mu):
    return (mu[1] - mu[2]) % 2


def kostka_matches(j):
    twoj = 2 * j
    entries = []
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K > 0:
            entries.append((mu, K, d_mu(mu), parity(mu)))
    print(f"\n=== j={j} (2j={twoj}), support size {len(entries)} ===")
    # Group by (K, d_mu)
    by_K_d = {}
    for mu, K, d, p in entries:
        by_K_d.setdefault((K, d), []).append((mu, p))
    for (K, d), mus in sorted(by_K_d.items()):
        if len(mus) >= 2:
            print(f"  K={K}, d={d}: {mus}")


if __name__ == "__main__":
    for j in range(3, 12):
        kostka_matches(j)
