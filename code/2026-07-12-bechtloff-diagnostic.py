#!/usr/bin/env python3
"""
Diagnostic: for a few (n, j), scan (alpha, beta) pairs and record
the degree-n part of s_alpha[S_+] * s_beta[S_-]. Sort by "distance"
from the target (e_2^j * p_1^{n-2j}), report the closest matches.

Also probe scalar multiples: check if the degree-n part is a *rational
multiple* of the target -- that would still be diagnostic (some c > 0
means we've found the "shape" but a scaling issue in the conjecture).
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import importlib.util
spec = importlib.util.spec_from_file_location(
    "hunt", os.path.join(os.path.dirname(__file__), "2026-07-12-bechtloff-plethystic-hunt.py"))
hunt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hunt)

from fractions import Fraction


def sf_scalar_multiple(f, tgt):
    """If f = c * tgt for some rational c (both nonzero), return c; else None."""
    if not f or not tgt:
        return None
    # Pick a key present in tgt.
    for k in tgt:
        if tgt[k] != 0:
            if k not in f:
                return None
            c = f[k] / tgt[k]
            break
    else:
        return None
    # Check all keys.
    keys = set(f) | set(tgt)
    for k in keys:
        fv = f.get(k, Fraction(0))
        tv = tgt.get(k, Fraction(0))
        if fv != c * tv:
            return None
    return c


def sf_dist(f, g):
    """Sum of |c_mu(f) - c_mu(g)| as Fraction."""
    keys = set(f) | set(g)
    return sum(abs(f.get(k, Fraction(0)) - g.get(k, Fraction(0))) for k in keys)


def diagnose(n, j, K=6):
    N = n
    Splus = hunt.build_S_plus(N)
    Sminus = hunt.build_S_minus(N)
    tgt = hunt.target(n, j)
    print(f"=== n={n}, j={j} ===")
    print(f"  target = {hunt.sf_str(tgt)}")
    all_parts = []
    for k in range(K + 1):
        all_parts.extend(hunt.partitions(k))
    # Compute all s_alpha[S+] and s_beta[S-].
    Aplus = {}
    Bminus = {}
    for p in all_parts:
        sp = hunt.schur_p(p, N)
        Aplus[p] = hunt.plethysm(sp, Splus, N)
        Bminus[p] = hunt.plethysm(sp, Sminus, N)
    # For each pair, look at degree-n part.
    scalar_mults = []
    exact_matches = []
    close_matches = []
    for alpha in all_parts:
        for beta in all_parts:
            prod = hunt.sf_mul(Aplus[alpha], Bminus[beta], N)
            deg_n = hunt.sf_degree_n(prod, n)
            if not deg_n:
                continue
            if hunt.sf_equal(deg_n, tgt):
                exact_matches.append((alpha, beta))
                continue
            c = sf_scalar_multiple(deg_n, tgt)
            if c is not None:
                scalar_mults.append((alpha, beta, c))
                continue
            d = sf_dist(deg_n, tgt)
            close_matches.append((d, alpha, beta, deg_n))
    close_matches.sort(key=lambda x: (x[0], sum(x[1]) + sum(x[2]), x[1], x[2]))
    print(f"  exact matches ({len(exact_matches)}):")
    for a, b in exact_matches[:10]:
        print(f"    alpha={a}, beta={b}")
    print(f"  scalar-multiple matches (c * target) ({len(scalar_mults)}):")
    for a, b, c in sorted(scalar_mults, key=lambda x: (abs(x[2]), sum(x[0]) + sum(x[1])))[:10]:
        print(f"    alpha={a}, beta={b}, c={c}")
    print(f"  top 5 closest non-multiple:")
    for d, a, b, dn in close_matches[:5]:
        print(f"    dist={d}, alpha={a}, beta={b}")
        print(f"      deg-{n} part: {hunt.sf_str(dn)}")


for n in [2, 3, 4, 5, 6]:
    for j in range(n // 2 + 1):
        diagnose(n, j, K=n)
    print()
