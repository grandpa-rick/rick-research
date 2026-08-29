"""Day 124: Verify the T-shift pattern

    T(e_1^a * e_k) = [e_1 - k]_a * e_k         for k = 4, 5
                                                 (extending k=2,3 result)

where T acts on monomials in x_1, ..., x_n by
    T(x_1^{a_1} ... x_n^{a_n}) = [x_1]_{a_1} ... [x_n]_{a_n}
with [x]_m = x(x-1)...(x-m+1) the falling factorial.

Method:
    - Fix n variables x_1, ..., x_n.
    - Form f = e_1^a * e_k (as polynomial in the x_i).
    - Expand into monomials in x_i's.
    - Replace each x_i^{a_i} factor by [x_i]_{a_i}.
    - Symmetrize the result back into the e-basis.
    - Compare to [e_1 - k]_a * e_k (also in the e-basis).

If T(e_1^a e_k) - [e_1 - k]_a * e_k = 0 (in the e-basis after symmetrizing),
the shift-by-k prediction holds.

We test:
    k in {2, 3, 4, 5}
    n in {k, k+1}     -- enough variables so e_k != 0
    a in {0, 1, 2, 3, 4}
"""

import sys
from itertools import combinations

import sympy as sp
from sympy import Integer, Poly, Rational, expand, symbols
from sympy.polys.polyfuncs import symmetrize


def elementary(k, xs):
    """e_k(x_1, ..., x_n)."""
    if k == 0:
        return Integer(1)
    n = len(xs)
    if k > n:
        return Integer(0)
    total = Integer(0)
    for combo in combinations(range(n), k):
        term = Integer(1)
        for i in combo:
            term *= xs[i]
        total += term
    return total


def falling(x, m):
    """[x]_m = x(x-1)...(x-m+1)."""
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def apply_T(f, xs):
    """Apply T monomial-wise:  x_1^{a_1} ... x_n^{a_n} -> [x_1]_{a_1} ... [x_n]_{a_n}."""
    poly = Poly(expand(f), *xs)
    out = Integer(0)
    for monom, coef in poly.terms():
        term = Integer(coef)
        for i, ai in enumerate(monom):
            term *= falling(xs[i], ai)
        out += term
    return expand(out)


def sym_to_e_basis(f, xs, e_syms):
    """Convert a symmetric polynomial f(x_1, ..., x_n) to a polynomial in e_1, ..., e_n.

    Uses SymPy's symmetrize with formal=True.  Any e_i with i > n gets zero-substituted
    because the symmetric polynomial in n variables has no such generator.
    """
    result, remainder, formulas = symmetrize(expand(f), list(xs), formal=True)
    if expand(remainder) != 0:
        raise ValueError(f"Not symmetric; remainder = {remainder}")
    # formulas is a list of (s_i_symbol, elementary_polynomial_expression)
    s_syms = [pair[0] for pair in formulas]
    # Map s_i -> e_i (aligning by position i = 1..len(formulas))
    subs = {}
    for i, s_sym in enumerate(s_syms):
        if i < len(e_syms):
            subs[s_sym] = e_syms[i]
        else:
            # would only appear if degree > n; shouldn't happen here since result is
            # in the same number of formal generators as xs
            subs[s_sym] = Integer(0)
    return expand(result.subs(subs))


def run_case(k, n, a_max=4, verbose=False):
    """Return list of (k, n, a, ok, diff_in_e_basis)."""
    xs = symbols(f"x1:{n + 1}")
    # e_1, ..., e_n symbols
    e_syms = symbols(f"e1:{n + 1}")
    e1_sym = e_syms[0]
    e_k_sym = e_syms[k - 1]

    e_k = elementary(k, xs)
    e_1 = elementary(1, xs)

    results = []
    for a in range(a_max + 1):
        f = expand(e_1 ** a * e_k)
        Tf = apply_T(f, xs)
        Tf_e = sym_to_e_basis(Tf, xs, e_syms)

        # Prediction: [e1 - k]_a * e_k
        predicted = falling(e1_sym - k, a) * e_k_sym
        predicted = expand(predicted)

        diff = expand(Tf_e - predicted)
        ok = (diff == 0)
        results.append((k, n, a, ok, Tf_e, predicted, diff))

        if verbose:
            print(f"    a={a}: T(e1^{a} e{k}) = {Tf_e}")
            print(f"          predicted    = {predicted}")
            print(f"          diff         = {diff}  ({'MATCH' if ok else 'MISMATCH'})")
    return results


def main():
    print("Day 124 T-shift verification")
    print("=" * 78)
    print("Testing:  T(e_1^a * e_k) ?= [e_1 - k]_a * e_k")
    print("for k in {2,3,4,5}, n in {k, k+1}, a in {0,1,2,3,4}.")
    print()

    all_results = []
    for k in [2, 3, 4, 5]:
        for n in [k, k + 1]:
            print(f"--- k = {k}, n = {n} ---")
            res = run_case(k, n, a_max=4, verbose=True)
            all_results.extend(res)
            print()

    # Summary
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"{'k':>3} {'n':>3} {'a':>3}  status")
    for (k, n, a, ok, Tf_e, predicted, diff) in all_results:
        status = "MATCH" if ok else "MISMATCH"
        print(f"{k:>3} {n:>3} {a:>3}  {status}")

    # Any failures?
    fails = [r for r in all_results if not r[3]]
    print()
    if not fails:
        print("ALL CASES MATCH.  The identity T(e_1^a e_k) = [e_1 - k]_a * e_k")
        print("is verified empirically for k in {2,3,4,5}, n in {k,k+1}, a in {0..4}.")
    else:
        print(f"{len(fails)} MISMATCHES:")
        for (k, n, a, ok, Tf_e, predicted, diff) in fails:
            print(f"  k={k}, n={n}, a={a}:")
            print(f"    T(...)       = {Tf_e}")
            print(f"    predicted    = {predicted}")
            print(f"    discrepancy  = {diff}")


if __name__ == "__main__":
    main()
