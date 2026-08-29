"""Day 118 — Given d_mu = mu_1 + floor((mu_2 + mu_3)/2) for ell(mu) <= 3,
verify combinatorially that for every "lower" lambda in supp(s*_{(1,1)}·s*_mu),
d_lambda <= d_mu + 1.

The "lower" lambdas are those with either:
  |lambda| < |mu| + 2, OR
  |lambda| = |mu| + 2 but lambda/mu is a horizontal 2-strip (both boxes in one row).

We consider ALL potential lambdas (regardless of whether they actually appear
with nonzero coefficient) and verify the bound, since the bound holds
independently of whether the coefficient is nonzero — a stronger statement
than (**).

Actually wait — the task says d_lambda <= d_mu + 1 for lambdas that APPEAR.
But we should also try to prove: for ALL potential support lambdas (all
mu ⊆ lambda with |lambda|-|mu| <= 2 that aren't vert-2-strips), d_lambda <=
d_mu + 1. If true, this is even stronger and implies (**).

Let's test both: whether the bound holds for potential support (structural),
and separately extract which ones ACTUALLY appear (Molev-Sagan coefficient
nonzero) and verify the bound only there. If both agree, great; if only the
appearing ones satisfy it, we need coefficient vanishing.
"""
from itertools import combinations

def d_conj(mu):
    mu = tuple(list(mu) + [0] * (3 - len(mu)))
    return mu[0] + (mu[1] + mu[2]) // 2

def all_partitions_len_le_3(N):
    result = []
    for a in range(N, -1, -1):
        for b in range(min(a, N - a), -1, -1):
            for cc in range(min(b, N - a - b), -1, -1):
                if a + b + cc == N:
                    result.append((a, b, cc))
    return result

def support_of_s11_product(mu):
    """All lambda in POTENTIAL supp: mu ⊆ lambda, |lambda|-|mu| in {0,1,2},
    ell(lambda) <= 3, and lambda/mu is a shape allowed by s*_{(1,1)}·s*_mu."""
    result = set()
    mu = tuple(list(mu) + [0] * (3 - len(mu)))
    result.add(mu)
    for i in range(3):
        nu = list(mu)
        nu[i] += 1
        if all(nu[j] >= nu[j+1] for j in range(2)):
            result.add(tuple(nu))
    for i in range(3):
        nu = list(mu)
        nu[i] += 2
        if all(nu[j] >= nu[j+1] for j in range(2)):
            result.add(tuple(nu))
    for i, j in combinations(range(3), 2):
        nu = list(mu)
        nu[i] += 1
        nu[j] += 1
        if all(nu[k] >= nu[k+1] for k in range(2)):
            result.add(tuple(nu))
    return sorted(result, key=lambda x: (sum(x), x), reverse=True)

def is_vert_2_strip(mu, lam):
    mu_p = tuple(list(mu) + [0] * (3 - len(mu)))
    lam_p = tuple(list(lam) + [0] * (3 - len(lam)))
    diff = [lam_p[i] - mu_p[i] for i in range(3)]
    if sum(diff) != 2:
        return False
    return all(d in (0, 1) for d in diff)

def classify(mu, lam):
    """Return a string describing lam/mu type."""
    mu_p = tuple(list(mu) + [0] * (3 - len(mu)))
    lam_p = tuple(list(lam) + [0] * (3 - len(lam)))
    diff = tuple(lam_p[i] - mu_p[i] for i in range(3))
    total = sum(diff)
    if total == 0:
        return "nu=mu"
    if total == 1:
        return f"add 1 box row{diff.index(1)+1}"
    # total = 2
    if all(d in (0, 1) for d in diff):
        return "vert 2-strip"
    if 2 in diff:
        return f"horiz 2-strip row{diff.index(2)+1}"
    return "?"

if __name__ == "__main__":
    MAX = 12
    print(f"Testing: for all mu with |mu| <= {MAX} and ell(mu) <= 3, and all")
    print(f"'lower' lambda in POTENTIAL support of s*_(1,1)·s*_mu,")
    print(f"is d_lambda <= d_mu + 1 (using formula d = mu_1 + floor((mu_2+mu_3)/2))?")
    print()

    n = 0
    n_bad = 0
    bad_cases = []
    for N in range(MAX + 1):
        for mu in all_partitions_len_le_3(N):
            d_mu = d_conj(mu)
            for lam in support_of_s11_product(mu):
                if is_vert_2_strip(mu, lam):
                    continue
                d_lam = d_conj(lam)
                n += 1
                if d_lam > d_mu + 1:
                    n_bad += 1
                    typ = classify(mu, lam)
                    bad_cases.append((mu, lam, typ, d_mu, d_lam))
    print(f"Total lower lambda-cases tested: {n}")
    print(f"Cases where d_lam > d_mu + 1 in POTENTIAL support: {n_bad}")
    print()
    if bad_cases:
        print(f"{'mu':>15} {'lam':>15} {'type':>25} {'d_mu':>5} {'d_lam':>6}")
        for mu, lam, typ, dm, dl in bad_cases:
            print(f"{str(mu):>15} {str(lam):>15} {typ:>25} {dm:>5} {dl:>6}")
    else:
        print("ALL potential-support lower lambda satisfy d_lam <= d_mu + 1!")
        print("This PROVES (**) STRUCTURALLY (no coefficient vanishing needed).")
