"""Check identities at d = d_max only, and compute full sum of top-t parts (both parities).

The idea: sum_{d_mu = d_max} K_{mu',(2^j)} bar s*_mu(s) MUST = 0 for the top-t
of S_j to vanish (since only d_max contributes). We want to see what identity
this gives, in terms of alpha_mu, beta_mu components.
"""

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts


def dmax_analysis():
    for j in range(2, 15):
        # find d_max
        support = []
        d_max = 0
        for mu in all_mu_3parts(2 * j):
            K = kostka_mu_prime_2j(mu)
            if K > 0:
                support.append((mu, d_mu(mu), K))
                d_max = max(d_max, d_mu(mu))
        # only d_max terms
        top_terms = [(mu, K) for (mu, d, K) in support if d == d_max]
        if not top_terms:
            continue

        # Compute Identity A: sum over even parity of sign * K
        # Compute Identity B: sum over odd parity of sign_odd * wt * K
        A_sum = 0
        B_sum = 0
        even_list = []
        odd_list = []
        for mu, K in top_terms:
            m1, m2, m3 = mu
            diff = m2 - m3
            if diff % 2 == 0:
                sign = (-1) ** (diff // 2)
                A_sum += sign * K
                even_list.append((mu, K, sign))
            else:
                sign = (-1) ** ((diff - 1) // 2)
                wt = (diff + 1) // 2
                B_sum += sign * wt * K
                odd_list.append((mu, K, sign, wt))

        okA = "OK" if A_sum == 0 else f"!!! ={A_sum}"
        okB = "OK" if B_sum == 0 else f"!!! ={B_sum}"
        print(f"j={j:2d}, d_max={d_max:2d}: A={A_sum:4d} {okA:>10} | B={B_sum:4d} {okB:>10}")
        if A_sum != 0 or B_sum != 0:
            print(f"  even: {even_list}")
            print(f"  odd:  {odd_list}")


if __name__ == "__main__":
    dmax_analysis()
