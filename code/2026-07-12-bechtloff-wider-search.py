#!/usr/bin/env python3
"""
Wider search: for n = 3, 4, extend |alpha|, |beta| up to 2n. Also try
linear combinations (sum of two pairs) briefly to see if the identity
holds up to a small sum -- although the conjecture only asks for one pair.

Also: check whether ANY (alpha, beta) with bounded size gives s_alpha[S+] * s_beta[S-]
whose degree-n part is a *positive* rational multiple of the target (indicating
we might be off by a normalisation).
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
    if not f or not tgt:
        return None
    for k in tgt:
        if tgt[k] != 0:
            if k not in f:
                return None
            c = f[k] / tgt[k]
            break
    else:
        return None
    keys = set(f) | set(tgt)
    for k in keys:
        fv = f.get(k, Fraction(0))
        tv = tgt.get(k, Fraction(0))
        if fv != c * tv:
            return None
    return c


def wider(n, j, K):
    N = n
    Splus = hunt.build_S_plus(N)
    Sminus = hunt.build_S_minus(N)
    tgt = hunt.target(n, j)
    print(f"=== n={n}, j={j}, K={K} ===")
    print(f"  target = {hunt.sf_str(tgt)}")
    parts = []
    for k in range(K + 1):
        parts.extend(hunt.partitions(k))
    matches = []
    scalar_mults = []
    for alpha in parts:
        sa = hunt.schur_p(alpha, N)
        A = hunt.plethysm(sa, Splus, N)
        for beta in parts:
            sb = hunt.schur_p(beta, N)
            B = hunt.plethysm(sb, Sminus, N)
            prod = hunt.sf_mul(A, B, N)
            deg_n = hunt.sf_degree_n(prod, n)
            if hunt.sf_equal(deg_n, tgt):
                matches.append((alpha, beta))
            else:
                c = sf_scalar_multiple(deg_n, tgt)
                if c is not None and c != 0:
                    scalar_mults.append((alpha, beta, c))
    print(f"  Exact matches: {len(matches)}")
    for a, b in matches[:20]:
        print(f"    alpha={a}, beta={b}")
    print(f"  Scalar-multiple matches: {len(scalar_mults)}")
    for a, b, c in scalar_mults[:20]:
        print(f"    alpha={a}, beta={b}, c={c}")


# n=3: full search up to |alpha|,|beta| <= 6
wider(3, 0, 6)
wider(3, 1, 6)
# n=4: full search up to |alpha|,|beta| <= 6
wider(4, 0, 6)
wider(4, 1, 6)
wider(4, 2, 6)
# n=5: |alpha|,|beta| <= 5 to keep runtime manageable
wider(5, 2, 5)
