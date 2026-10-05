#!/usr/bin/env python3
"""
Day 186: Compute Shareshian-Wachs / Ellzey-Wachs chromatic quasisymmetric
function X_{P_n}(q) for the path graph P_n, then convert to h-basis and
look for a generating-function recursion in the h-basis with q-coefficients.

Also compute the two-parameter (q,t) via Hikita's e-basis prescription:
X_{P_n}(q,t) has e-coefs = q-independent = t-analogues.

Path graph P_n has edges {(i,i+1) : i = 1,...,n-1}. As a Hessenberg / unit
interval graph in the Shareshian-Wachs paradigm, this is the "boundary"
case ("staircase" Hessenberg). In Hikita's e ∈ E_n notation, this
corresponds to e(i) = i (natural pairing i ~ i+1), a specific element of E_n.

Approach: build X_G(q) monomial-symmetric via ascent statistic on proper
colorings, use direct enumeration of colorings on a bounded alphabet, then
extract m_lambda coefficients and convert via standard changes of basis.
"""

from sympy import symbols, Rational, Poly, expand, simplify, factor, together, cancel
from sympy import Symbol, Matrix, eye, zeros, Integer, sympify
from itertools import product
from collections import defaultdict, Counter

q = symbols('q')
t = symbols('t')

def partitions(n):
    """All partitions of n as tuples in weakly decreasing order."""
    if n == 0:
        return [()]
    out = []
    def rec(remain, largest, prefix):
        if remain == 0:
            out.append(tuple(prefix))
            return
        for k in range(min(remain, largest), 0, -1):
            rec(remain - k, k, prefix + [k])
    rec(n, n, [])
    return out


def sort_desc(t):
    return tuple(sorted(t, reverse=True))


def X_path_q_monomial(n, N=None):
    """
    Compute X_{P_n}(q) = sum over proper colorings c: [n] -> [N] of
    q^{asc(c)} * x_{c(1)} x_{c(2)} ... x_{c(n)},
    where asc(c) = #{i : c(i) < c(i+1)}, edges (i, i+1) in P_n.
    Returns dict: partition -> coefficient of m_lambda (q-poly), so we can
    read symmetric-function content.

    A monomial x_{c(1)}...x_{c(n)} on n vars, with colors in {1,...,N},
    contributes to m_lambda where lambda = sort_desc(multiplicities of colors).

    Since X_G is symmetric (Shareshian-Wachs Thm), we can compute the coefficient
    of the monomial x_1^{lambda_1} x_2^{lambda_2}...x_l^{lambda_l} and this gives
    the m_lambda coefficient directly.

    Enumerate all proper colorings using color labels from 1..l where l=len(lambda),
    with multiplicities exactly lambda_i for color i. Sum q^{asc} weighted by
    permutations of the color labels... no. Simpler: m_lambda coefficient =
    coefficient of the specific monomial x_1^{lambda_1} ... x_l^{lambda_l} in X_G.
    """
    if N is None:
        N = n  # enough colors to see all partitions
    coef = defaultdict(lambda: Integer(0))
    # enumerate all proper colorings c: [n] -> [N] with adjacent distinct
    def rec(i, colors, prev, ascents):
        if i == n:
            mult = Counter(colors)
            lam = sort_desc(mult.values())
            coef[lam] += q**ascents
            return
        for col in range(1, N + 1):
            if col == prev:
                continue
            new_asc = ascents + (1 if prev is not None and prev < col else 0)
            rec(i + 1, colors + [col], col, new_asc)
    rec(0, [], None, 0)
    # Now: coef[lam] = sum over ALL colorings with color-multiset = lam of q^asc
    # We want coefficient of m_lam = one specific monomial x_1^lam_1 ... x_l^lam_l.
    # coef[lam] counts ALL orderings, so we must divide by the number of ways
    # to ASSIGN colors to distinct color-labels giving that multiset...
    # Actually: for each lam, the number of ways to pick which color plays role i
    # is N!/((N-l)! * (mult of repeated parts)) where l=len(lam).
    # Simpler and safer: enumerate only colorings using colors 1..len(lam) with
    # exactly multiset = lam.
    #
    # But then coef[lam] is sum q^asc over ALL colorings on {1,..,l} realizing
    # multiset lam, and this equals SUM over permutations of that multiset that
    # give proper coloring times... hmm.
    #
    # Cleanest: coefficient of x_1^{lam_1} x_2^{lam_2} ... x_l^{lam_l} in X_G(q)
    # equals sum over proper colorings c: [n] -> [1..l] using color i exactly
    # lam_i times, of q^{asc(c)}. This is the coefficient in the MONOMIAL basis
    # of the monomial (x_1^lam_1 ... x_l^lam_l).
    # But then converting to m_lam basis: m_lam = sum over ALL rearrangements of
    # that monomial into distinct-index tuples. So we need coefficient of ANY ONE
    # rearrangement, and since X_G is symmetric they're all equal.
    #
    # So: below we do it directly by fixing that specific target multiset.
    return None  # this method is convoluted; use the cleaner one below.


def X_path_q_via_target(n, lam):
    """
    Coefficient of the monomial x_1^{lam_1} x_2^{lam_2} ... x_l^{lam_l}
    in X_{P_n}(q). That is: sum q^{asc(c)} over proper colorings
    c: [n] -> [1..l=len(lam)] with color i used exactly lam_i times.
    edges: i-(i+1).
    """
    l = len(lam)
    # each color i appears lam[i-1] times
    target = list(lam)
    total_ways = 0
    # enumerate with backtracking
    result = Integer(0)
    def rec(i, prev, ascents, remaining):
        nonlocal result
        if i == n:
            if all(r == 0 for r in remaining):
                result += q**ascents
            return
        for c in range(l):
            if remaining[c] == 0:
                continue
            color = c + 1
            if color == prev:
                continue
            new_asc = ascents + (1 if prev is not None and prev < color else 0)
            remaining[c] -= 1
            rec(i + 1, color, new_asc, remaining)
            remaining[c] += 1
    rec(0, None, 0, target)
    return result


def X_path_q_expanded(n):
    """Return X_{P_n}(q) as dict lambda -> coefficient in the monomial basis:
    coefficient of m_lambda for each partition lambda of n."""
    out = {}
    for lam in partitions(n):
        out[lam] = X_path_q_via_target(n, lam)
    return out


# Basis-change utilities: work in Q(q).
# We'll compute m_lambda -> h_lambda and m_lambda -> e_lambda transitions
# by using power-sum p as an intermediary.
#
# For symmetric functions of degree n, indexed by partitions of n:
#   m_lambda in monomial basis
#   e_lambda, h_lambda, p_lambda in respective bases
# The change-of-basis matrices are standard. We'll build them numerically
# via direct expansion on a "sufficient" number of variables.

def poly_to_dict(poly_expr, gens_vars):
    """expand a polynomial in given generators (list of Sympy symbols) into
    dict monomial-tuple -> coefficient"""
    p = Poly(expand(poly_expr), *gens_vars)
    return dict(p.as_dict())


def sym_basis_monomial_expansion(basis_kind, lam, xs):
    """Expand basis_kind_lambda in variables xs (list of Symbols).
    basis_kind in {'e', 'h', 'p', 'm'}.
    Returns Sympy expression (polynomial in xs).
    """
    N = len(xs)
    from sympy import symbols, prod, Add
    if basis_kind == 'p':
        # p_k = sum x_i^k, p_lambda = prod p_{lam_i}
        expr = Integer(1)
        for k in lam:
            expr = expand(expr * sum(x**k for x in xs))
        return expand(expr)
    if basis_kind == 'e':
        # e_k = sum_{i1 < i2 < ... < ik} x_i1 x_i2 ... x_ik
        from itertools import combinations
        expr = Integer(1)
        for k in lam:
            ek = sum(sympy_prod([xs[i] for i in comb]) for comb in combinations(range(N), k))
            expr = expand(expr * ek)
        return expand(expr)
    if basis_kind == 'h':
        # h_k = sum_{i1 <= i2 <= ... <= ik} x_i1 ... x_ik
        from itertools import combinations_with_replacement
        expr = Integer(1)
        for k in lam:
            hk = sum(sympy_prod([xs[i] for i in comb]) for comb in combinations_with_replacement(range(N), k))
            expr = expand(expr * hk)
        return expand(expr)
    if basis_kind == 'm':
        # m_lambda: sum over distinct-index orbits of x_1^{lam_1} x_2^{lam_2} ...
        # Simpler: iterate over injections [len(lam)] -> [N] (up to symmetry of parts)
        # We enumerate all tuples of distinct indices (i_1,...,i_l), assign lam[j] to i_j,
        # and take the sum, dividing by symmetry of equal parts of lam.
        from itertools import permutations
        l = len(lam)
        if l > N:
            return Integer(0)
        # generate all tuples (i_1, ..., i_l) with distinct entries in [N]
        from itertools import permutations as _perm
        # count multiplicity of each part
        from collections import Counter
        part_counts = Counter(lam)
        # unique monomials
        seen = set()
        total = Integer(0)
        for tup in _perm(range(N), l):
            mon = tuple(sorted([(tup[i], lam[i]) for i in range(l)]))
            if mon in seen:
                continue
            seen.add(mon)
            e = Integer(1)
            for idx, power in mon:
                e *= xs[idx]**power
            total += e
        return expand(total)


def sympy_prod(lst):
    from sympy import Integer
    r = Integer(1)
    for v in lst:
        r *= v
    return r


def convert_m_to_basis(mon_dict, target_basis, n, xs):
    """Given dict lambda -> coefficient in monomial basis (for degree-n
    symmetric function), express in target basis ('h' or 'e' or 'p').
    Returns dict lambda -> coefficient in target basis.
    We work by:
      f = sum_lambda coef[lambda] * m_lambda
      expand into variables xs, then match against basis expansion.
    """
    from sympy import Integer
    # First: build f as polynomial in xs
    f = Integer(0)
    parts = partitions(n)
    for lam, c in mon_dict.items():
        if c == 0:
            continue
        f += c * sym_basis_monomial_expansion('m', lam, xs)
    f = expand(f)
    # Now express f in target basis. Build "basis matrix": for each partition mu
    # of n, expand target_mu in monomials (in xs), collect coefficient dict.
    basis_dicts = {}
    for mu in parts:
        b = sym_basis_monomial_expansion(target_basis, mu, xs)
        basis_dicts[mu] = poly_to_dict(b, xs)
    f_dict = poly_to_dict(f, xs)

    # We want coefficients c_mu such that sum_mu c_mu * basis_mu = f in xs.
    # Solve a linear system: rows = monomials, columns = mu's.
    all_mons = set()
    for d in basis_dicts.values():
        all_mons.update(d.keys())
    all_mons.update(f_dict.keys())
    all_mons = sorted(all_mons)
    mu_list = parts
    A = zeros(len(all_mons), len(mu_list))
    b = zeros(len(all_mons), 1)
    for i, mon in enumerate(all_mons):
        for j, mu in enumerate(mu_list):
            A[i, j] = basis_dicts[mu].get(mon, Integer(0))
        b[i, 0] = f_dict.get(mon, Integer(0))
    # Solve. Since basis is a basis, the solution is unique among mu's of size n.
    sol = A.solve(b)
    out = {}
    for j, mu in enumerate(mu_list):
        c = simplify(sol[j, 0])
        if c != 0:
            out[mu] = c
    return out


def pretty_dict(d):
    lines = []
    for lam in sorted(d.keys(), key=lambda l: (-sum(l), l)):
        lines.append(f"  {lam}: {factor(d[lam])}")
    return "\n".join(lines) if lines else "  (0)"


def main():
    for n in range(1, 5):
        print(f"\n=== n = {n}: X_{{P_{n}}}(q) ===")
        # need enough variables; N = n is enough (a partition of n has <= n parts)
        xs = symbols(f'x1:{n + 2}')  # N = n+1 to be safe
        m_dict = X_path_q_expanded(n)
        # note: X_path_q_expanded returns coefficient of the monomial x_1^lam_1..x_l^lam_l
        # This IS the m_lambda coefficient. (Because in the monomial expansion
        # of X_G, coeff of x_1^lam_1 x_2^lam_2 ... = m_lam-coefficient.)
        print("Monomial basis (m_lambda):")
        print(pretty_dict(m_dict))

        h_dict = convert_m_to_basis(m_dict, 'h', n, list(xs))
        print("h-basis:")
        print(pretty_dict(h_dict))

        e_dict = convert_m_to_basis(m_dict, 'e', n, list(xs))
        print("e-basis:")
        print(pretty_dict(e_dict))


if __name__ == "__main__":
    main()
