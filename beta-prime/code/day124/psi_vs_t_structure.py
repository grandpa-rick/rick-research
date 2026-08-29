"""Day 124: Structural comparison of Psi - T.

Findings from psi_vs_t.py:
  - Psi != T in general (even Psi(e_1) = e_1 - 3 vs T(e_1) = e_1).
  - But: for symmetric f, Psi(f) - T(f) is *lower-degree* than f.

To help decide whether T-shift is USEFUL for Lemma 2 attack:
  (a) Verify that Psi(f) - T(f) has strictly lower TOTAL degree than f.
  (b) Compare (1,1,2)-weights of Psi(e_1^a * e_k) and T(e_1^a * e_k) in e-basis.
      If T has weight <= a + 2k/2 = a + k... and Psi has weight <= (matching bound),
      then T-shift + lower-degree correction gives filtration bound for Psi.
  (c) Is Psi = T composed with a "shift by rho" or similar operation?
      Test: Psi(f)(x_1, x_2, x_3) ?= T(f)(x_1, x_2, x_3) after some substitution.
      Or:  Psi(f) = T(f(x - c))  for some vector c?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import Integer, Poly, Rational, expand, symbols, factor
from itertools import combinations

from t_shift_verify import elementary, falling, apply_T, sym_to_e_basis
from psi_vs_t import X, apply_psi_to_symmetric, schur_mu, s_star_mu, enumerate_partitions_le3, x1, x2, x3

E = symbols("e1 e2 e3")
e1, e2, e3 = E


def total_degree(f):
    if f == 0:
        return -1
    return Poly(expand(f), *X).total_degree()


def weight_112_in_e(f_e):
    """Given f in e_1, e_2, e_3, compute max(a1 + a2 + 2*a3)."""
    f_e = expand(f_e)
    if f_e == 0:
        return -1
    p = Poly(f_e, e1, e2, e3)
    w = -1
    for (a1, a2, a3), coef in p.terms():
        w = max(w, a1 + a2 + 2 * a3)
    return w


def check_degree_of_correction():
    print("=" * 78)
    print("(A) TOTAL DEGREE of Psi(f) - T(f) vs total degree of f")
    print("=" * 78)
    print("If Psi(f) - T(f) has strictly lower total degree than f, then T is")
    print("the 'top' of Psi (up to lower terms).\n")

    for k in [1, 2, 3]:
        for a in range(0, 5):
            e_1 = elementary(1, list(X))
            e_k = elementary(k, list(X))
            f = expand(e_1**a * e_k)
            T_f = apply_T(f, list(X))
            Psi_f = apply_psi_to_symmetric(f)
            diff = expand(T_f - Psi_f)
            df, dTf, dPsi, ddiff = (
                total_degree(f), total_degree(T_f), total_degree(Psi_f), total_degree(diff)
            )
            print(f"  a={a}, k={k}:  deg(f)={df}, deg(T_f)={dTf}, deg(Psi_f)={dPsi}, deg(T-Psi)={ddiff}")


def check_112_weights():
    print()
    print("=" * 78)
    print("(B) (1,1,2)-WEIGHTS in e-basis  (relevant to E_j Lemma 2 filtration)")
    print("=" * 78)
    print("Compare weight_112 of Psi(e_1^a e_k) vs T(e_1^a e_k).\n")
    print(f"  {'a':>2} {'k':>2} | {'w_T':>4} {'w_Psi':>6} | equal?")

    for k in [1, 2, 3]:
        for a in range(0, 5):
            e_1 = elementary(1, list(X))
            e_k = elementary(k, list(X))
            f = expand(e_1**a * e_k)
            T_f = apply_T(f, list(X))
            Psi_f = apply_psi_to_symmetric(f)
            T_f_e = sym_to_e_basis(T_f, list(X), list(E))
            Psi_f_e = sym_to_e_basis(Psi_f, list(X), list(E))
            wT = weight_112_in_e(T_f_e)
            wPsi = weight_112_in_e(Psi_f_e)
            eq = "YES" if wT == wPsi else "NO"
            print(f"  {a:>2} {k:>2} | {wT:>4} {wPsi:>6} | {eq}")


def check_leading_symbol():
    print()
    print("=" * 78)
    print("(C) 'LEADING SYMBOL' compare: top-degree part of T vs Psi")
    print("=" * 78)
    print("For each Schur s_mu, extract the top-degree homogeneous component of")
    print("both T(s_mu) and s^*_mu and check equality (which is s_mu itself,")
    print("by the standard fact that top(s^*_mu) = s_mu).\n")

    for n in range(0, 5):
        for mu in enumerate_partitions_le3(n):
            s_mu = schur_mu(mu)
            s_star = s_star_mu(mu)
            T_smu = apply_T(s_mu, list(X))
            d = total_degree(s_mu)
            # top of s_star = homogeneous degree-d part
            def top_hom(f, deg):
                if f == 0: return 0
                p = Poly(expand(f), *X)
                out = Integer(0)
                for m, c in p.terms():
                    if sum(m) == deg:
                        out += c * x1**m[0] * x2**m[1] * x3**m[2]
                return expand(out)
            top_smu = top_hom(s_mu, d)
            top_sstar = top_hom(s_star, d)
            top_Tsmu = top_hom(T_smu, d)
            top_eq_smu = (expand(top_sstar - top_smu) == 0)
            top_T_eq_smu = (expand(top_Tsmu - top_smu) == 0)
            print(f"  mu={str(mu):12s}  top(s*_mu)=s_mu: {top_eq_smu}  top(T(s_mu))=s_mu: {top_T_eq_smu}")


if __name__ == "__main__":
    check_degree_of_correction()
    check_112_weights()
    check_leading_symbol()
