"""Investigate the actual condition needed for S_j = sum K_{mu',(2^j)} s*_mu to have t-degree <= j."""

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts, identity_A_sum, identity_B_sum


def support_analysis():
    for j in range(1, 13):
        twoj = 2 * j
        entries = []
        for mu in all_mu_3parts(twoj):
            K = kostka_mu_prime_2j(mu)
            if K == 0:
                continue
            entries.append((mu, d_mu(mu), K))
        if not entries:
            print(f"j={j}, NO SUPPORT?!")
            continue
        Dmax = max(e[1] for e in entries)
        print(f"j={j}, D_max = {Dmax} (j+{Dmax-j}), #support = {len(entries)}")
        # show top-3 d_mu values
        entries.sort(key=lambda e: -e[1])
        print(f"  Top 3 by d_mu:")
        for mu, dm, K in entries[:5]:
            parity = "even" if (mu[1] - mu[2]) % 2 == 0 else "odd"
            print(f"    mu={mu}, d_mu={dm}, K={K}, parity={parity}")

def check_sum_at_d(j, d):
    """Compute sum over ALL mu (both parities) at d_mu = d, both parts."""
    entries = []
    for mu in all_mu_3parts(2*j):
        if d_mu(mu) != d:
            continue
        K = kostka_mu_prime_2j(mu)
        if K == 0:
            continue
        m1, m2, m3 = mu
        parity = (m2 - m3) % 2
        entries.append((mu, K, parity))
    # separate
    even_terms = [(mu, K, (-1)**((mu[1]-mu[2])//2)) for (mu,K,p) in entries if p == 0]
    odd_terms = [(mu, K, (-1)**((mu[1]-mu[2]-1)//2), (mu[1]-mu[2]+1)//2) for (mu,K,p) in entries if p == 1]
    A_partial = sum(sign * K for (mu, K, sign) in even_terms)
    B_partial = sum(sign * wt * K for (mu, K, sign, wt) in odd_terms)
    return {
        'even_terms': even_terms,
        'odd_terms': odd_terms,
        'A_partial (even-only, constant identity guess)': A_partial,
        'B_partial (alpha identity)': B_partial,
    }


if __name__ == "__main__":
    print("=== Support analysis: max d_mu with K != 0 ===")
    support_analysis()

    print("\n=== Detailed check at d = d_max for j = 5..10 ===")
    for j in [5, 6, 7, 8, 9, 10]:
        # find d_max
        d_max = 0
        for mu in all_mu_3parts(2*j):
            K = kostka_mu_prime_2j(mu)
            if K > 0:
                d_max = max(d_max, d_mu(mu))
        print(f"\n--- j={j}, d_max = {d_max} ---")
        for d in range(d_max, j, -1):
            info = check_sum_at_d(j, d)
            if not info['even_terms'] and not info['odd_terms']:
                continue
            print(f"  d = {d}:")
            print(f"    Even (partity 0): {info['even_terms']}")
            print(f"    Odd  (parity 1):  {info['odd_terms']}")
            print(f"    A_partial = {info['A_partial (even-only, constant identity guess)']}")
            print(f"    B_partial = {info['B_partial (alpha identity)']}")
