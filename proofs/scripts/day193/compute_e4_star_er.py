"""Compute e_4 ⋆ e_r for small r, to test the min(a,b)+1-terms meta-conjecture at (4,r).

Extends hikita_star.py to a = 4.

For a=4: e_4(Y) = sum_{i<j<k<l} Y_i Y_j Y_k Y_l.
"""

import sys
import time
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day192')

from hikita_star import build_action, e_r_X, e_lambda_X, partitions_of, expand_symmetric_in_e_basis, sanity_q1
import sympy as sp
import pickle
from itertools import combinations

q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


def compute_e4_star_er(r, m, verbose=True):
    """Compute e_4(X) ⋆ e_r(X) = t^{-6} e_4(Y) . e_r(X)."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    erX = e_r_X(m, r)
    if verbose:
        print(f"[m={m}] Computing e_4(Y) . e_{r}(X) ...")

    # Step 1: compute Y_l.e_r for each l
    Yl_er = {}
    for l in range(1, m + 1):
        Yl_er[l] = Y_apply(erX, l)
        if verbose:
            print(f"  Y_{l}.e_{r} done. #terms = {len(sp.Add.make_args(Yl_er[l]))}")

    # Step 2: compute Y_k Y_l.e_r for k < l
    Ykl_er = {}
    for l in range(1, m + 1):
        for k in range(1, l):
            Ykl_er[(k, l)] = Y_apply(Yl_er[l], k)
        if verbose:
            print(f"  Y_k Y_{l} pairs done.")

    # Step 3: compute Y_j Y_k Y_l.e_r for j < k < l
    Yjkl_er = {}
    for l in range(1, m + 1):
        for k in range(1, l):
            for j in range(1, k):
                Yjkl_er[(j, k, l)] = Y_apply(Ykl_er[(k, l)], j)
        if verbose:
            print(f"  Y_j Y_k Y_{l} triples done.")

    # Step 4: sum i < j < k < l of Y_i Y_j Y_k Y_l.e_r
    total = sp.Integer(0)
    count = 0
    tot_count = sum(1 for _ in combinations(range(1, m+1), 4))
    for l in range(1, m + 1):
        for k in range(1, l):
            for j in range(1, k):
                for i in range(1, j):
                    piece = Y_apply(Yjkl_er[(j, k, l)], i)
                    total = sp.expand(total + piece)
                    count += 1
                    if verbose and count % 5 == 0:
                        print(f"  quadruple {count}/{tot_count}; running #terms = {len(sp.Add.make_args(total))}")

    tw = t ** sp.Rational(-4 * 3, 2)  # t^{-6}
    star = sp.expand(tw * total)
    n = 4 + r
    if verbose:
        print(f"[m={m}] e_4 ⋆ e_{r} computed. Expanding in e_lambda-basis of deg {n}...")
    expansion = expand_symmetric_in_e_basis(star, m, n)
    return expansion


if __name__ == "__main__":
    import sys
    r = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 4 + r  # m = a + r

    print("=" * 80)
    print(f"Day 193 meta-conjecture test: e_4 ⋆ e_{r} at m={m}")
    print("=" * 80)
    start = time.time()
    expansion = compute_e4_star_er(r, m, verbose=True)
    end = time.time()
    print(f"\nWallclock: {end - start:.1f}s")

    # Save
    with open(f'/home/agent/projects/proofs/scripts/day193/e4_e{r}_m{m}.pkl', 'wb') as f:
        pickle.dump({(lam): c for lam, c in expansion.items()}, f)

    # Print nonzero terms
    print(f"\n--- e_4 ⋆ e_{r} at m={m} ---")
    nonzero = 0
    for lam, c in expansion.items():
        cs = sp.simplify(c)
        if cs != 0:
            nonzero += 1
            print(f"  e_{lam} = {sp.factor(cs)}")
    print(f"\n  #nonzero = {nonzero}, predicted min(4,{r})+1 = {min(4,r)+1}")

    # Sanity q=1
    print(f"\n--- Sanity check: at q=1 ---")
    for lam, c in expansion.items():
        cs = sp.simplify(c.subs(q, 1))
        if cs != 0:
            print(f"  e_{lam} at q=1 = {cs}")
