"""
Day 189 — Verify that X_G for every unit-interval graph on n=4 vertices
lies in the linear span of path-graph products {X_{P_lambda} : lambda |- 4}.

At q=1 (Stanley 1995 chromatic symmetric function), X_G is Sym-valued and
depends only on the iso type of G. This is a sanity check on the "hunch"
that HHKKO Thm 3.7 kills (Algorithm 3.5 gives the explicit reduction).

We verify only Test A (linear span, dim-count). HHKKO Algorithm 3.5 gives
Test B (explicit reduction via modular law) — we do not implement it here.
"""

from itertools import product, combinations
from sympy import symbols, expand, sympify, Symbol, Rational, Matrix, Poly, factor
from sympy import zeros, eye


def elementary_sym(k, xs):
    if k == 0:
        return sympify(1)
    if k > len(xs):
        return sympify(0)
    s = 0
    for combo in combinations(xs, k):
        p = 1
        for x in combo:
            p *= x
        s += p
    return expand(s)


def X_G_stanley(edges, num_verts, xs):
    """Stanley chromatic symmetric function via direct proper-coloring sum.
    Edges are 1-indexed."""
    n_colors = len(xs)
    total = 0
    for coloring in product(range(n_colors), repeat=num_verts):
        if all(coloring[i - 1] != coloring[j - 1] for (i, j) in edges):
            w = 1
            for v in range(num_verts):
                w *= xs[coloring[v]]
            total += w
    return expand(total)


def homogeneous_to_e(hp, xs):
    """Convert homogeneous symmetric poly to e-basis dict."""
    result = {}
    hp = expand(hp)
    while hp != 0:
        P = Poly(hp, *xs)
        terms = P.terms()
        if not terms:
            break
        terms_sorted = sorted(terms, key=lambda t: t[0], reverse=True)
        alpha, coef = terms_sorted[0]
        alpha_list = list(alpha)
        while alpha_list and alpha_list[-1] == 0:
            alpha_list.pop()
        if not alpha_list:
            result[()] = result.get((), 0) + coef
            hp = expand(hp - coef)
            continue
        # Conjugate partition
        max_part = alpha_list[0]
        conjugate = tuple(sum(1 for a in alpha_list if a >= i)
                          for i in range(1, max_part + 1))
        lam = conjugate
        e_lam = 1
        for part in lam:
            e_lam *= elementary_sym(part, xs)
        e_lam = expand(e_lam)
        result[lam] = result.get(lam, 0) + coef
        hp = expand(hp - coef * e_lam)
    return {k: v for k, v in result.items() if expand(v) != 0}


def X_Pn_re_q1(n, xs):
    """X_{P_n} at q=1 via Rick's (Re) recursion (== Ellzey 2017 (6.7) at t=1)."""
    if n == 0:
        return {(): sympify(1)}
    result = {}
    # e_n term
    result[(n,)] = sympify(1)
    for k in range(2, n + 1):
        sub = X_Pn_re_q1(n - k, xs)
        coeff = k - 1
        for lam, c in sub.items():
            new_lam = tuple(sorted((k,) + lam, reverse=True))
            result[new_lam] = result.get(new_lam, 0) + coeff * c
    return {k: v for k, v in result.items() if v != 0}


def e_dict_multiply(d1, d2):
    result = {}
    for l1, c1 in d1.items():
        for l2, c2 in d2.items():
            lam = tuple(sorted(l1 + l2, reverse=True))
            result[lam] = result.get(lam, 0) + c1 * c2
    return {k: v for k, v in result.items() if v != 0}


def partitions(n):
    if n == 0:
        yield ()
        return
    def gen(rem, cap):
        if rem == 0:
            yield ()
            return
        for k in range(min(rem, cap), 0, -1):
            for tail in gen(rem - k, k):
                yield (k,) + tail
    yield from gen(n, n)


def path_products(n, xs):
    """Return dict {partition lambda |- n : X_{P_lambda} in e-basis dict}."""
    XP = {k: X_Pn_re_q1(k, xs) for k in range(0, n + 1)}
    out = {}
    for lam in partitions(n):
        prod = {(): sympify(1)}
        for part in lam:
            prod = e_dict_multiply(prod, XP[part])
        out[lam] = prod
    return out


# All unit-interval graphs on n=4 (Hessenberg functions m: [4] -> [4], m(i) >= i,
# m increasing), enumerated. 14 total (Catalan C_4).
def hessenberg_graphs(n):
    """Yield (m_tuple, edges) for each Hessenberg function on [n]."""
    def gen(prefix, i):
        if i > n:
            yield tuple(prefix)
            return
        lo = max(i, prefix[-1] if prefix else 1)
        for m_i in range(lo, n + 1):
            yield from gen(prefix + [m_i], i + 1)
    for m in gen([], 1):
        edges = []
        for i in range(1, n + 1):
            for j in range(i + 1, m[i - 1] + 1):
                edges.append((i, j))
        yield m, edges


def graph_signature(edges, n):
    """Isomorphism signature: sorted degree sequence + edge multiset by degrees.
    Good enough to distinguish 4-vertex graphs."""
    from collections import Counter
    deg = [0] * (n + 1)
    for (i, j) in edges:
        deg[i] += 1
        deg[j] += 1
    ds = tuple(sorted(deg[1:]))
    # Also count triangles for extra discrimination
    tris = 0
    E = set()
    for (i, j) in edges:
        E.add((i, j))
        E.add((j, i))
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in E and (b, c) in E and (a, c) in E:
                    tris += 1
    return (ds, len(edges), tris)


def format_e(d):
    if not d:
        return "0"
    parts = []
    for lam in sorted(d.keys(), key=lambda x: (-sum(x), x)):
        c = d[lam]
        if lam == ():
            parts.append(f"({c})")
        else:
            parts.append(f"({c})*e_{''.join(str(p) for p in lam)}")
    return " + ".join(parts)


def name_partition(lam):
    if lam == ():
        return "1"
    return "".join(str(p) for p in lam)


def solve_in_basis(target_dict, basis_dicts, basis_keys):
    """Solve target = sum c_k * basis[k] in e-basis. Return dict k -> c_k or None."""
    # Collect all monomial keys
    all_keys = set(target_dict.keys())
    for b in basis_dicts:
        all_keys.update(b.keys())
    key_list = sorted(all_keys, key=lambda x: (-sum(x), x))
    # Build matrix: rows = e-monomials, cols = basis elements
    ncols = len(basis_dicts)
    nrows = len(key_list)
    M = zeros(nrows, ncols)
    rhs = zeros(nrows, 1)
    for r, k in enumerate(key_list):
        for c, b in enumerate(basis_dicts):
            M[r, c] = Rational(b.get(k, 0))
        rhs[r, 0] = Rational(target_dict.get(k, 0))
    # Solve M x = rhs
    sol = M.solve(rhs)
    return {basis_keys[c]: sol[c, 0] for c in range(ncols)}


def main():
    N = 4
    xs = symbols(f'x1:{N+1}')

    print("=" * 78)
    print(f"Day 189 — path-product span check for unit-interval graphs on n={N}")
    print("=" * 78)

    # Step 1: enumerate unit-interval graphs, dedup by iso signature
    print("\nStep 1: Enumerate Hessenberg unit-interval graphs on n=4:")
    seen = {}
    for m, edges in hessenberg_graphs(N):
        sig = graph_signature(edges, N)
        if sig not in seen:
            seen[sig] = (m, edges)
        # else already have iso type
    print(f"  {len(seen)} isomorphism types (up to graph iso via degree seq + #tri + |E|):")
    for sig, (m, edges) in seen.items():
        print(f"    m={m}, edges={edges}, sig={sig}")

    # Step 2: build path products
    print("\nStep 2: Build path-graph products X_{P_lambda} for lambda |- 4:")
    prods = path_products(N, xs)
    for lam, d in prods.items():
        print(f"  X_{{P_{name_partition(lam)}}} = {format_e(d)}")

    part_list = list(partitions(N))
    basis_dicts = [prods[lam] for lam in part_list]

    # Step 3: verify linear independence via dim check
    print("\nStep 3: Linear independence check (should have rank = p(4) = 5):")
    all_keys_e = set()
    for d in basis_dicts:
        all_keys_e.update(d.keys())
    key_list_e = sorted(all_keys_e, key=lambda x: (-sum(x), x))
    M = zeros(len(key_list_e), len(basis_dicts))
    for r, k in enumerate(key_list_e):
        for c, d in enumerate(basis_dicts):
            M[r, c] = Rational(d.get(k, 0))
    rank = M.rank()
    print(f"  rank(M) = {rank}, expected = {len(part_list)} = p(4) = 5")
    assert rank == len(part_list), "Path products fail to be linearly independent!"
    print("  PASS: path products are linearly independent, hence span Lambda_4.")

    # Step 4: for each iso type, compute X_G and express in path-product basis
    print("\nStep 4: Express each X_G in path-product basis:")
    for sig, (m, edges) in seen.items():
        Xg = X_G_stanley(edges, N, xs)
        Xg_e = homogeneous_to_e(Xg, xs)
        try:
            coeffs = solve_in_basis(Xg_e, basis_dicts, part_list)
        except Exception as ex:
            print(f"  m={m}: SOLVE FAILED: {ex}")
            continue
        # Format expansion
        expansion_parts = []
        for lam in part_list:
            c = coeffs.get(lam, 0)
            if c != 0:
                expansion_parts.append(f"({c})*X_{{P_{name_partition(lam)}}}")
        expansion = " + ".join(expansion_parts) if expansion_parts else "0"
        print(f"\n  Graph m={m}, edges={edges}")
        print(f"    X_G in e-basis:  {format_e(Xg_e)}")
        print(f"    In path-basis:   {expansion}")

    print("\n" + "=" * 78)
    print("Conclusion: for n=4, path products form a basis of Lambda_4.")
    print("Every X_G on 4 vertices lies in this span (by dimension).")
    print("This is Test A — a trivial dim-count consequence.")
    print("HHKKO Thm 3.7 + Algorithm 3.5 give the ACTUAL rewriting procedure")
    print("via the restricted modular law. That's what kills Rick's Day 189 hunch.")
    print("=" * 78)


if __name__ == '__main__':
    main()
