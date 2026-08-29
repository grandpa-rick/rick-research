"""Day 124: Compute Pi*(s*_nu) for small nu, express in e-basis, and study
the leading-weight symbol structure.

Goal: understand precisely which pairs (nu, nu') give cancelling leading
weight-(d_nu + 2) terms in Pi*(s*_nu).

Pi*(s*_nu) = sum_{lambda in nu boxplus (1,1), l(lambda) <= 3} s*_lambda

where nu boxplus (1,1) = { nu + (unit vec at i) + (unit vec at j) with i < j }
restricted to partitions (nu_1 >= nu_2 >= nu_3).
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational
from itertools import combinations
from collections import defaultdict

from individual_weight import s_star_mu, sym_to_e_basis, weight_112

e1, e2, e3 = symbols('e1 e2 e3')
u1, u2, u3 = symbols('u1 u2 u3')


def pi_star_partitions(nu, ell=3):
    """Given nu = (nu_1, nu_2, nu_3), return list of lambda in nu boxplus (1,1) with l<=ell."""
    nu = list(nu) + [0] * (ell - len(nu))
    nu = nu[:ell]
    results = []
    # Add unit at position i, unit at position j (i < j), padding one extra slot
    padded = nu + [0]
    for i in range(ell + 1):
        for k in range(i + 1, ell + 1):
            new = list(padded)
            new[i] += 1
            new[k] += 1
            # Check partition condition
            is_part = all(new[m] >= new[m + 1] for m in range(len(new) - 1))
            if not is_part:
                continue
            # Trim trailing zeros
            while new and new[-1] == 0:
                new.pop()
            if len(new) > ell:
                continue
            # Pad back to ell
            while len(new) < ell:
                new.append(0)
            results.append(tuple(new))
    return results


def pi_star_of_s_star(nu):
    """Pi*(s*_nu) as polynomial in e1, e2, e3."""
    lambdas = pi_star_partitions(nu)
    total = Integer(0)
    for lam in lambdas:
        s_star = s_star_mu(lam)
        s_star_e = sym_to_e_basis(s_star)
        total = expand(total + s_star_e)
    return total, lambdas


def leading_weight_symbol(f, target_w):
    """Extract the coefficient polynomial (in whatever) of monomials of weight target_w."""
    if f == 0:
        return Integer(0)
    p = Poly(f, e1, e2, e3)
    parts = {}
    for (a1, a2, a3), coef in p.terms():
        w = a1 + a2 + 2 * a3
        if w == target_w:
            parts[(a1, a2, a3)] = parts.get((a1, a2, a3), Integer(0)) + coef
    # Build polynomial from these monomials
    result = Integer(0)
    for (a1, a2, a3), c in parts.items():
        result += c * e1**a1 * e2**a2 * e3**a3
    return expand(result)


def all_weight_symbols(f):
    """Return dict weight -> polynomial (sum of monomials of that weight)."""
    if f == 0:
        return {}
    p = Poly(f, e1, e2, e3)
    parts = {}
    for (a1, a2, a3), coef in p.terms():
        w = a1 + a2 + 2 * a3
        parts[w] = parts.get(w, Integer(0)) + coef * e1**a1 * e2**a2 * e3**a3
    return {w: expand(v) for w, v in parts.items()}


def d_nu(nu):
    """d_nu = nu_1 + floor((nu_2 + nu_3)/2)."""
    return nu[0] + (nu[1] + nu[2]) // 2


def enumerate_partitions_len3(max_total):
    """All partitions with l <= 3 of total <= max_total."""
    results = []
    for tot in range(max_total + 1):
        for a in range(tot + 1):
            for b in range(a + 1):
                c = tot - a - b
                if 0 <= c <= b:
                    results.append((a, b, c))
    return results


def main():
    print('=' * 70)
    print('Day 124: Pi*(s*_nu) leading-symbol structure')
    print('=' * 70)
    # For each nu with |nu| small, compute Pi*(s*_nu), record:
    #   - d_nu
    #   - list of lambdas in nu boxplus (1,1)
    #   - individual weights of s*_lambda
    #   - weight of full Pi*(s*_nu)
    #   - the LEADING-WEIGHT-(d_nu + 2) SYMBOL of each s*_lambda and their sum
    for nu in enumerate_partitions_len3(6):
        pi_star, lambdas = pi_star_of_s_star(nu)
        w_full = weight_112(pi_star)
        dnu = d_nu(nu)
        top_target = dnu + 2  # possible leading weight from cancellation
        top_actual = dnu + 1
        # weight symbols of individual s*_lambda
        indiv_top_syms = {}
        indiv_full = {}
        for lam in lambdas:
            s_star_e = sym_to_e_basis(s_star_mu(lam))
            indiv_full[lam] = s_star_e
            indiv_top_syms[lam] = leading_weight_symbol(s_star_e, top_target)
        top_symbol_sum = expand(sum(indiv_top_syms.values(), Integer(0)))
        top_actual_sum = expand(sum(
            leading_weight_symbol(indiv_full[lam], top_actual) for lam in lambdas))
        print(f'\n  nu = {nu}, d_nu = {dnu}')
        print(f'    lambdas: {lambdas}')
        print(f'    weight(Pi*(s*_nu)) = {w_full}')
        print(f'    top-target weight = {top_target}')
        print(f'    individual weight-{top_target} symbols:')
        for lam, sym in indiv_top_syms.items():
            print(f'      s*_{lam}: {sym}')
        print(f'    SUM of weight-{top_target} symbols: {top_symbol_sum}')
        print(f'    SUM of weight-{top_actual} symbols: {top_actual_sum}')


if __name__ == '__main__':
    main()
