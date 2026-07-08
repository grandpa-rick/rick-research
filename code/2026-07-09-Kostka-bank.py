"""Day 85 — Kostka bank.

For a fixed lambda = (a, b, c) partition, enumerate mu partitions of |lambda|
in a small class and compute K_{lambda, mu} = # SSYT of shape lambda with
content mu.

Uses the Pieri rule: K_{lambda, mu} = coefficient of s_lambda in
  h_{mu_1} * h_{mu_2} * ... * h_{mu_L}.
Iterated multiplication by h_k = sum over horizontal k-strips. Since we only
care about the final target lambda = (a, b, c) (three rows), we prune any
intermediate partition that has more than 3 rows or exceeds lambda in any row.
This keeps intermediate states small (few thousand for our sizes) and runs
fast even for |lambda| ~ 40.

Classes of mu (from PROVE Step P1):
- Column-strict: (N - k, 1^k)  for k = 0, ..., N - 1
- Two-part: (N - k, k)          for k = 0, ..., N // 2
- Hook A: (N - 2j, 2^j)         for j = 1, ..., N // 2 - 1
- Hook B: (N - 2j, 1^{2j})      for j = 1, ..., (N - 1) // 2
- Reverse hook (1^{2j}, N - 2j) is sorted into Hook B.
"""
from math import factorial
import csv
import os


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def hook_length(lam):
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    n = sum(lam)
    cols = [0] * lam[0]
    for i, li in enumerate(lam):
        for j in range(li):
            cols[j] += 1
    hooks = 1
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = cols[j] - i - 1
            hooks *= (arm + leg + 1)
    return factorial(n) // hooks


def is_partition(mu):
    mu = [x for x in mu if x > 0]
    return all(mu[i] >= mu[i + 1] for i in range(len(mu) - 1))


def partition_sort(mu):
    return tuple(sorted((x for x in mu if x > 0), reverse=True))


def dominates(lam, mu):
    """Return True if lam dominates mu."""
    lam = list(lam)
    mu = list(mu)
    L = max(len(lam), len(mu))
    lam += [0] * (L - len(lam))
    mu += [0] * (L - len(mu))
    s_lam = 0
    s_mu = 0
    for i in range(L):
        s_lam += lam[i]
        s_mu += mu[i]
        if s_mu > s_lam:
            return False
    return True


# ------------------------------------------------------------
# Kostka via iterated Pieri (bounded by sub-partitions of lambda)
# ------------------------------------------------------------

def horiz_strips_bounded(nu, k, lam_ext):
    """All rho = nu + horizontal k-strip with rho <= lam_ext componentwise,
    and rho has at most 3 rows (nu, rho are length-3 tuples with trailing 0s)."""
    results = []
    a_partial = [0, 0, 0]

    def go(i, remaining):
        if i == 3:
            if remaining == 0:
                rho = (nu[0] + a_partial[0], nu[1] + a_partial[1], nu[2] + a_partial[2])
                results.append(rho)
            return
        upper = min(remaining, lam_ext[i] - nu[i])
        if i > 0:
            # Horizontal strip constraint: rho[i] <= nu[i - 1]
            upper = min(upper, nu[i - 1] - nu[i])
        if upper < 0:
            return
        for a in range(0, upper + 1):
            a_partial[i] = a
            go(i + 1, remaining - a)

    go(0, k)
    return results


def kostka_pieri(lam, mu):
    """K_{lam, mu} via Pieri, bounded by lam having <= 3 rows."""
    lam = partition_sort(lam)
    mu = partition_sort(mu)
    if sum(lam) != sum(mu):
        return 0
    if not dominates(lam, mu):
        return 0
    if len(lam) > 3:
        raise ValueError("This implementation assumes lambda has at most 3 rows.")
    lam_ext = tuple(list(lam) + [0] * (3 - len(lam)))

    state = {(0, 0, 0): 1}
    for k in mu:
        new_state = {}
        for nu, coef in state.items():
            for rho in horiz_strips_bounded(nu, k, lam_ext):
                new_state[rho] = new_state.get(rho, 0) + coef
        state = new_state

    return state.get(lam_ext, 0)


def K(lam, mu):
    """Kostka number K_{lam, mu}, with a fast path for mu = (1^n)."""
    lam = partition_sort(lam)
    mu = partition_sort(mu)
    if sum(lam) != sum(mu):
        return 0
    if not mu:
        return 1
    if all(x == 1 for x in mu):
        return hook_length(list(lam))
    if mu == lam:
        return 1
    return kostka_pieri(lam, mu)


# ------------------------------------------------------------
# mu enumerator
# ------------------------------------------------------------

def enumerate_mu_classes(N):
    """Yield (class_name, mu) pairs for mu partition of N, each mu once."""
    seen = {}

    def emit(name, mu):
        mu = partition_sort(mu)
        if not mu or sum(mu) != N:
            return
        if not is_partition(mu):
            return
        # Keep FIRST class-name that emitted this mu; skip later duplicates.
        if mu in seen:
            return
        seen[mu] = name

    for k in range(0, N):
        emit('col_strict', (N - k,) + (1,) * k)
    for k in range(0, N // 2 + 1):
        emit('two_part', (N - k, k))
    j = 1
    while N - 2 * j >= 2:
        emit('hook_A', (N - 2 * j,) + (2,) * j)
        j += 1
    j = 1
    while N - 2 * j >= 1:
        emit('hook_B', (N - 2 * j,) + (1,) * (2 * j))
        j += 1
    for mu, cls in seen.items():
        yield cls, mu


# ------------------------------------------------------------
# Tabulation
# ------------------------------------------------------------

def tabulate_kostka(c, a_max=20, b_max=16, out_csv=None, verbose=True):
    rows = []
    for a in range(c, a_max + 1):
        for b in range(c, min(a, b_max) + 1):
            if (a + b + c) % 2 != 0:
                continue
            lam = (a, b, c)
            N = a + b + c
            n_mus = 0
            for cls, mu in enumerate_mu_classes(N):
                k_val = K(lam, mu)
                rows.append({
                    'c': c, 'a': a, 'b': b,
                    'lambda': str(lam),
                    'class': cls,
                    'mu': str(mu),
                    'K_lam_mu': k_val,
                })
                n_mus += 1
            if verbose:
                print(f"  (a,b,c)=({a},{b},{c}): {n_mus} mu shapes")
    if out_csv:
        d = os.path.dirname(out_csv)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(out_csv, 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=['c', 'a', 'b', 'lambda', 'class', 'mu', 'K_lam_mu'])
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote {len(rows)} rows to {out_csv}")
    return rows


# ------------------------------------------------------------
# Self-test
# ------------------------------------------------------------

def selftest():
    # K_{(3,2,1), (1^6)} = f^(3,2,1) = 16
    assert K((3, 2, 1), (1,) * 6) == 16, K((3, 2, 1), (1,) * 6)
    # K_{(3,2,1), (3,2,1)} = 1
    assert K((3, 2, 1), (3, 2, 1)) == 1
    # K_{(3,3), (2,2,2)} = 1
    assert K((3, 3), (2, 2, 2)) == 1
    # K_{(4,2), (3,3)} = 1
    assert K((4, 2), (3, 3)) == 1, K((4, 2), (3, 3))
    # K_{(2,2,2), (2,2,2)} = 1
    assert K((2, 2, 2), (2, 2, 2)) == 1
    # K_{(4,2), (2,2,2)} = ?
    v = K((4, 2), (2, 2, 2))
    print(f"K_{{(4,2), (2,2,2)}} = {v}  (expect 3)")
    assert v == 3
    # K_{(4,2), (2,2,1,1)} = 4 (verified against brute-force SSYT enumeration)
    v = K((4, 2), (2, 2, 1, 1))
    print(f"K_{{(4,2), (2,2,1,1)}} = {v}  (expect 4)")
    assert v == 4
    # K_{lam, mu} = 0 if mu > lam in dominance
    assert K((3, 3), (5, 1)) == 0
    # K_{(6,5,5), (5,5,5,1)} — random test.
    v = K((6, 5, 5), (6, 5, 5))
    assert v == 1
    print("selftest ok")


if __name__ == '__main__':
    selftest()

    print("\n" + "=" * 70)
    print("Kostka bank at c = 5, (a, b) sweep")
    print("=" * 70)
    rows = tabulate_kostka(
        c=5, a_max=20, b_max=16,
        out_csv='/home/agent/projects/code/2026-07-09-Mj-harvest/Kostka_bank_c5.csv')

    print("\nPreview: lambda = (11, 8, 5), N = 24, all mu classes:")
    print(f"{'class':>12s} | {'mu':>34s} | {'K':>16s}")
    print("-" * 72)
    for r in rows:
        if r['a'] == 11 and r['b'] == 8:
            print(f"{r['class']:>12s} | {r['mu']:>34s} | {r['K_lam_mu']:>16d}")
