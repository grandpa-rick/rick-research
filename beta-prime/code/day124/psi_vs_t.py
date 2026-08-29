"""Day 124: Compare Psi (Schur -> shifted-Schur) against T (falling-factorial
monomial map) on the polynomials appearing in E_j.

Psi is defined on Sym via s_mu |-> s^*_mu, extended linearly.  We work in three
variables x_1, x_2, x_3 (matches Day 123's framework — Rick's E_j's live there).

Test:
    For each Schur s_mu with mu partition of n (l(mu) <= 3), is
        Psi(s_mu)  ?=  T(s_mu)
    when both sides are compared as polynomials in x_1, x_2, x_3?

If yes for all mu, then Psi = T on Sym (in 3 vars).  Otherwise, we get a
concrete discrepancy showing that Psi and T are different maps and the T-shift
identity does not directly close Lemma 2 via Psi = T.

Also test:
    T(e_1^a e_k)  ?=  Psi(e_1^a e_k)  for small a, k.
This directly probes the E_j-relevant case.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import Integer, Poly, Rational, expand, symbols, factor
from sympy.polys.polyfuncs import symmetrize
from itertools import combinations

from t_shift_verify import elementary, falling, apply_T, sym_to_e_basis


# Fixed: 3 variables (Rick's setting)
X = symbols("x1 x2 x3")
x1, x2, x3 = X
E = symbols("e1 e2 e3")


def V_of_x():
    """Vandermonde V = (x1-x2)(x1-x3)(x2-x3)."""
    return (x1 - x2) * (x1 - x3) * (x2 - x3)


def schur_mu(mu):
    """Ordinary Schur s_mu(x_1, x_2, x_3), classical Weyl formula:
       s_mu = det(x_i^{mu_j + n - j}) / V,   n = 3.
    """
    mu = list(mu) + [0] * (3 - len(mu))
    mu = mu[:3]
    exps = [mu[0] + 2, mu[1] + 1, mu[2]]
    rows = [[X[i]**exps[l] for l in range(3)] for i in range(3)]
    numer = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
             - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
             + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
    V = V_of_x()
    q, r = sp.div(sp.Poly(expand(numer), *X), sp.Poly(expand(V), *X))
    if r.as_expr() != 0:
        raise ValueError(f"Schur numerator not divisible by V for mu={mu}")
    return expand(q.as_expr())


def s_star_mu(mu):
    """Shifted Schur s^*_mu(x_1, x_2, x_3) via
       s^*_mu = det([x_i]_{mu_j + n - j}) / V,   n = 3.
    """
    mu = list(mu) + [0] * (3 - len(mu))
    mu = mu[:3]
    exps = [mu[0] + 2, mu[1] + 1, mu[2]]
    rows = [[falling(X[i], exps[l]) for l in range(3)] for i in range(3)]
    numer = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
             - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
             + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
    V = V_of_x()
    q, r = sp.div(sp.Poly(expand(numer), *X), sp.Poly(expand(V), *X))
    if r.as_expr() != 0:
        raise ValueError(f"Shifted-Schur numerator not divisible by V for mu={mu}")
    return expand(q.as_expr())


def enumerate_partitions_le3(n):
    """All partitions of n with at most 3 parts."""
    parts = []
    for a in range(n + 1):
        for b in range(a + 1):
            c = n - a - b
            if 0 <= c <= b:
                parts.append((a, b, c))
    # dedupe (a,b,c) as partition (largest first)
    return parts


def compare_psi_vs_t_on_schur(mu, verbose=True):
    """For a partition mu, compare Psi(s_mu) = s^*_mu vs T(s_mu)."""
    s_mu = schur_mu(mu)
    s_star = s_star_mu(mu)
    T_smu = apply_T(s_mu, list(X))
    diff = expand(s_star - T_smu)
    ok = (diff == 0)
    if verbose:
        status = "MATCH" if ok else "DIFFER"
        print(f"  mu = {str(mu):12s}  T(s_mu) vs s*_mu:  {status}")
        if not ok:
            print(f"     s_mu       = {s_mu}")
            print(f"     s^*_mu     = {s_star}")
            print(f"     T(s_mu)    = {T_smu}")
            print(f"     s*_mu - T(s_mu) = {diff}")
    return ok, diff


def apply_psi_to_symmetric(f):
    """Apply Psi = (s_mu |-> s^*_mu) to a symmetric polynomial f in x_1,...,x_3.

    Method: expand f in Schur basis, then swap each s_mu for s^*_mu.
    We do this by writing f in e-basis first, then evaluating each e^a in
    Schur basis, but the cleanest way is to compute the change-of-basis
    directly for each monomial x^alpha (dominant weight -> Schur).
    Simpler: since we know f is symmetric, we expand f in terms of Schurs
    by Gaussian elimination against the Schur basis for partitions of that
    degree with l <= 3.
    """
    f = expand(f)
    total_deg = Poly(f, *X).total_degree()
    result = Integer(0)
    remainder = f
    # partitions of each degree d <= total_deg (l <= 3), but we only need to peel by
    # degree.  Enumerate all partitions with l <= 3 and total <= total_deg.
    schur_basis = {}
    for d in range(total_deg + 1):
        for mu in enumerate_partitions_le3(d):
            schur_basis[mu] = schur_mu(mu)

    # Peel off Schurs by leading monomial (dominant term).
    # Ordering: (deg desc, then mu lex desc)
    partitions_sorted = sorted(schur_basis.keys(), key=lambda mu: (-sum(mu), tuple(-x for x in mu)))

    for mu in partitions_sorted:
        s_mu = schur_basis[mu]
        # Coefficient of leading monomial x1^mu[0] x2^mu[1] x3^mu[2] in s_mu is 1.
        # Find that coeff in remainder.
        poly_rem = Poly(remainder, *X) if remainder != 0 else None
        if poly_rem is None:
            break
        coeff = poly_rem.coeff_monomial(tuple(mu))
        if coeff != 0:
            result += coeff * s_star_mu(mu)
            remainder = expand(remainder - coeff * s_mu)
    # Sanity: remainder should be zero if f was symmetric
    if expand(remainder) != 0:
        # If f has parts that don't fit in l<=3 partition support (i.e., needs more vars),
        # we get residue.  For safety, warn.
        print(f"    WARNING: Schur expansion left remainder {remainder}")
    return expand(result)


def compare_psi_t_on_e1a_ek(a, k):
    """Compare Psi(e_1^a * e_k) vs T(e_1^a * e_k) in 3 variables."""
    if k > 3:
        return None  # e_k = 0 in 3 vars for k > 3
    e_1 = elementary(1, list(X))
    e_k = elementary(k, list(X))
    f = expand(e_1**a * e_k)
    T_f = apply_T(f, list(X))
    Psi_f = apply_psi_to_symmetric(f)
    diff = expand(T_f - Psi_f)
    return T_f, Psi_f, diff


def main():
    print("=" * 78)
    print("Day 124  Psi vs T  comparison (3 variables)")
    print("=" * 78)

    print("\n(A) Test Psi(s_mu) = s^*_mu  vs  T(s_mu)  for all partitions mu, |mu| <= 5, l <= 3.\n")
    all_match = True
    diffs = []
    for n in range(0, 6):
        for mu in enumerate_partitions_le3(n):
            ok, diff = compare_psi_vs_t_on_schur(mu, verbose=True)
            if not ok:
                all_match = False
                diffs.append((mu, diff))
    print()
    if all_match:
        print("  ALL Psi(s_mu) = T(s_mu)  for tested mu.  ==> Psi = T on Sym.")
    else:
        print(f"  {len(diffs)} DISCREPANCIES.  Psi != T in general.")

    print()
    print("=" * 78)
    print("(B) Test Psi(e_1^a * e_k) vs T(e_1^a * e_k)  (the E_j-relevant case).\n")
    for k in [1, 2, 3]:
        for a in range(0, 5):
            r = compare_psi_t_on_e1a_ek(a, k)
            if r is None:
                continue
            T_f, Psi_f, diff = r
            ok = (diff == 0)
            status = "MATCH" if ok else "DIFFER"
            print(f"  a = {a}, k = {k}:  {status}")
            if not ok:
                print(f"     T(e_1^{a} e_{k})   = {T_f}")
                print(f"     Psi(e_1^{a} e_{k}) = {Psi_f}")
                print(f"     diff = T - Psi   = {diff}")
                # factor the difference
                print(f"     factored diff    = {factor(diff)}")

    print()
    print("=" * 78)
    print("(C) Test on individual e_k first (a = 0), since e_k = s_{1^k}.")
    print("    Psi(e_k) = s^*_{1^k}.  What is T(e_k)?  (By multilinearity, T(e_k) = e_k.)")
    print()
    for k in [1, 2, 3]:
        e_k = elementary(k, list(X))
        T_ek = apply_T(e_k, list(X))
        Psi_ek = s_star_mu(tuple([1] * k))  # partition (1,1,...,1) k times
        # If Psi(e_k) = T(e_k) = e_k, then s^*_{1^k} = e_k.
        print(f"  k = {k}:")
        print(f"     e_k         = {e_k}")
        print(f"     T(e_k)      = {expand(T_ek)}")
        print(f"     s^*_{{1^{k}}}   = Psi(e_k) = {expand(Psi_ek)}")
        print(f"     Psi(e_k) - T(e_k) = {expand(Psi_ek - T_ek)}")
        print()


if __name__ == "__main__":
    main()
