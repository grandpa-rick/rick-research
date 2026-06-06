"""
KL-polynomial sanity check for B_3 (analog of B_2 check).

For each dominant spin (lam, mu) tested in bgg_aug_compare_B3.py, compute:
  - kl_fp[bd] = # fixed points of Aug~ at bidegree bd (= # even items - # odd items matched, by bidegree)
  - kl_bgg[bd] = Σ_w (-1)^{ℓ(w)} K_{q,t}(w·lam - mu) at bidegree bd

Check: kl_fp == |kl_bgg| for dominant mu (where KL is non-negative).
"""

import os, sys
from fractions import Fraction
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aug_tilde_B3_richer as B3
import bgg_aug_compare_B3 as cmp

N = 3


def kostant_at(beta, N, pos_roots_ord):
    out = defaultdict(int)
    pis = B3.all_kostant_partitions(beta, N, pos_roots_ord)
    for pi in pis:
        bd = B3.bidegree_of_partition(pi, N)
        out[bd] += 1
    return dict(out)


def kl_via_bgg(lam, mu, N):
    """KL_{lam, mu}(q,t) = Σ_w (-1)^{l(w)} K_{q,t}(w·lam - mu) at each bidegree."""
    rho = tuple(Fraction(2*N - 1 - 2*i, 2) for i in range(N))
    lr = tuple(lam[i] + rho[i] for i in range(N))
    mr = tuple(mu[i] + rho[i] for i in range(N))
    if not all(x.denominator == 1 for x in lr + mr):
        return None
    lr_int = tuple(int(x) for x in lr)
    mr_int = tuple(int(x) for x in mr)
    pos_roots_ord = B3.positive_roots_Bn_ordered(N)
    out = defaultdict(int)
    for w_func, length, label in B3.weyl_Bn(N):
        wlr = w_func(lr_int)
        diff = tuple(wlr[i] - mr_int[i] for i in range(N))
        # Require non-negative leading coord
        if diff[0] < 0:
            continue
        sign = (-1) ** length
        kqt = kostant_at(diff, N, pos_roots_ord)
        for k, v in kqt.items():
            out[k] += sign * v
    return {k: v for k, v in out.items() if v != 0}


def kl_via_fp_matching(lam, mu, N):
    """Aug~ fixed-point count per bidegree.

    Using the pure-then-mixed full matching, the FIXED POINTS are even items
    not matched (no odd partners) and any unmatched odds.

    Returns {bd: count}.
    """
    res = cmp.match_pure_then_mixed(lam, mu, N)
    if res is None:
        return None
    items, _, pair_odd, unmatched, _ = res
    matched_evens = set(e for (e, mv) in pair_odd.values())
    matched_odds = set(pair_odd.keys())
    out = defaultdict(int)
    for idx, (lbl, length, pi, bd) in enumerate(items):
        if idx in matched_odds:
            continue
        if length % 2 == 0 and idx not in matched_evens:
            out[bd] += 1
        elif length % 2 == 1 and idx not in matched_odds:
            out[bd] += 1  # shouldn't happen
    return dict(out)


def run_kl_check(max_lam1_int=4):
    pairs = B3.enumerate_dominant_spin_pairs(max_lam1_int, N)
    print(f"Running KL check on {len(pairs)} dominant spin pairs.")
    n_strict = 0   # fp == kl
    n_abs = 0      # fp == |kl|
    n_dom = 0      # dominant mu count
    n_strict_dom = 0
    n_abs_dom = 0
    failures = []
    for lam, mu in pairs:
        kl_bgg = kl_via_bgg(lam, mu, N)
        if kl_bgg is None:
            continue
        kl_fp = kl_via_fp_matching(lam, mu, N)
        if kl_fp is None:
            continue
        is_dom = (mu[0] >= mu[1] >= mu[2] >= 0)
        if is_dom:
            n_dom += 1
        # Strict: fp dict == kl_bgg dict
        if kl_fp == kl_bgg:
            n_strict += 1
            if is_dom:
                n_strict_dom += 1
        # Abs: fp[bd] == |kl_bgg[bd]| for all bd
        kl_abs = {k: abs(v) for k, v in kl_bgg.items()}
        if kl_fp == kl_abs:
            n_abs += 1
            if is_dom:
                n_abs_dom += 1
        else:
            if len(failures) < 5:
                failures.append((lam, mu, kl_fp, kl_bgg))
    print(f"  Total pairs: {len(pairs)}, Dominant μ: {n_dom}")
    print(f"  Strict (fp == kl):                {n_strict}/{len(pairs)}  (dominant: {n_strict_dom}/{n_dom})")
    print(f"  Abs-value (fp == |kl|):           {n_abs}/{len(pairs)}    (dominant: {n_abs_dom}/{n_dom})")
    if failures:
        print(f"  First abs-value failure examples:")
        for lam, mu, fp, kl in failures:
            print(f"    λ={lam}, μ={mu}")
            print(f"      fp={fp}")
            print(f"      kl={kl}")
    return {'n_strict': n_strict, 'n_abs': n_abs, 'n_dom': n_dom,
            'n_strict_dom': n_strict_dom, 'n_abs_dom': n_abs_dom,
            'n_total': len(pairs), 'failures': failures}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-lam', type=int, default=4)
    args = parser.parse_args()
    run_kl_check(max_lam1_int=args.max_lam)
