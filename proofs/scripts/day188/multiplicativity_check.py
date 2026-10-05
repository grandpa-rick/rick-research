"""
Day 188 — Multiplicativity spot-check for Rick's h-basis (q)-GF world.

Goal: verify X_{K_2 ⊔ P_2}(q) = X_{K_2}(q) · X_{P_2}(q) = X_{P_2}(q)^2
      (since K_2 = P_2 as unlabeled graphs / same chromatic quasisymmetric function).

Method:
  1. Compute X_{P_2}(q) via (Re) recursion and (Comp) formula independently.
  2. Square it in the symmetric-function e-basis.
  3. Independently compute X_{K_2 ⊔ P_2}(q) via direct enumeration of proper
     colorings with Ellzey-Wachs asc statistic, using SymPy monomial symmetric
     functions in 4 variables, then convert to e-basis.
  4. Compare.

Ellzey-Wachs convention (Definition 2.1 of Ellzey-Wachs 2018):
  For G on vertex set V = {1,...,n} with edge set E, proper coloring κ,
    asc(κ) = |{ (i,j) ∈ E : i < j, κ(i) < κ(j) }|,
    X_G(x; q) = Σ_{κ proper} q^{asc(κ)} ∏_v x_{κ(v)}.
"""

from itertools import product, combinations
from sympy import symbols, expand, simplify, Poly, Rational, sympify, Symbol
from sympy import factor
from sympy.polys.orderings import lex


# ---------------------------------------------------------------------------
# Utilities: elementary symmetric functions in n variables, e-basis conversion
# ---------------------------------------------------------------------------

def elementary_sym(k, xs):
    """e_k in variables xs; k=0 gives 1."""
    if k == 0:
        return sympify(1)
    if k > len(xs):
        return sympify(0)
    s = 0
    for combo in combinations(xs, k):
        prod = 1
        for x in combo:
            prod *= x
        s += prod
    return expand(s)


def to_e_basis(poly_expr, xs, q, max_deg):
    """
    Given a symmetric polynomial in xs (with coefficients polynomial in q),
    express it in the basis of e-monomials e_{λ_1} e_{λ_2} ... where the
    partition λ has parts ≤ len(xs) and |λ| = total degree in x's.

    Returns dict: partition (tuple, weakly decreasing) → coefficient (in q).

    Uses the standard lex-leading-term subtraction algorithm:
      A symmetric polynomial's leading monomial (in lex, x1>x2>...) is
      x1^{λ_1} x2^{λ_2} ... where λ is a partition; subtract
      coeff · m_λ or equivalently work in e-basis via the fact that
      e_{λ'_1} e_{λ'_2} ... (conjugate partition) has leading monomial
      x1^{λ_1} x2^{λ_2} ... times monomial symmetric function structure.

    Simpler approach: use the fact that {e_λ : λ partition of d, parts ≤ n}
    forms a basis when d ≤ n (for larger d it's still a basis of symmetric
    polynomials of degree d in n variables, indexed by partitions with parts ≤ n).

    We'll do lex-leading-monomial elimination using e_λ directly.
    """
    n = len(xs)
    p = expand(poly_expr)
    # Partitions of degree d with parts between 1 and n (for e-basis in n vars,
    # e_k = 0 for k > n).
    result = {}

    # Extract homogeneous components
    from sympy import Poly
    # Build polynomial over Q(q)[xs]
    P = Poly(p, *xs)

    # Work degree by degree — the whole thing is homogeneous of degree max_deg
    # by construction, but just to be safe:
    # For each homogeneous piece:
    total_deg = P.total_degree()
    # We assume homogeneous of degree max_deg. Verify.
    # But to be robust, iterate over degree.
    homog = {}
    for monom, coef in P.terms():
        d = sum(monom)
        homog.setdefault(d, []).append((monom, coef))

    for d, terms in homog.items():
        # Reconstruct the homogeneous polynomial
        hp = 0
        for monom, coef in terms:
            m = coef
            for xi, e in zip(xs, monom):
                m *= xi**e
            hp += m
        hp = expand(hp)
        e_expansion = homogeneous_to_e(hp, xs, d)
        for lam, c in e_expansion.items():
            result[lam] = result.get(lam, 0) + c

    # Clean zero coefficients
    return {lam: expand(c) for lam, c in result.items() if expand(c) != 0}


def homogeneous_to_e(hp, xs, d):
    """
    Convert a homogeneous symmetric polynomial hp of degree d in xs to e-basis.
    Uses lex-leading-term elimination.

    Leading monomial (lex x1>x2>...) of e_λ (as product e_{λ_1}·e_{λ_2}·...
    with λ weakly decreasing) has leading monomial x1^{λ'_1} x2^{λ'_2} ...
    where λ' is the conjugate. Wait — let's be careful.

    e_k = x1 x2 ... x_k + ...; leading monomial is x1·x2·...·x_k.
    So e_{λ_1} e_{λ_2} ... e_{λ_r} has leading monomial
      (x1·x2·...·x_{λ_1}) · (x1·x2·...·x_{λ_2}) · ...
    which, sorted, is x1^r x2^r ... x_{λ_r}^r x_{λ_r+1}^{r-1} ... etc.
    That's the conjugate partition λ' viewed as an exponent vector on x1,x2,...

    So leading monomial of e_λ (as multiset product) = x^{λ'} where λ' is
    the conjugate partition, considered as exponent vector (λ'_1, λ'_2, ...).

    Algorithm:
      While hp != 0:
        Find lex-leading monomial x^α = x1^{α_1} x2^{α_2} ... in hp.
        α must be a partition (weakly decreasing) since hp is symmetric.
        Let λ = α' (conjugate).
        Subtract coeff · e_λ from hp.
        Record coefficient.
    """
    n = len(xs)
    result = {}
    hp = expand(hp)
    from sympy import Poly, Symbol
    q = Symbol('q')

    while hp != 0:
        # Extract leading monomial in lex order x1 > x2 > ... > xn
        P = Poly(hp, *xs)
        terms = P.terms()  # list of (monom_tuple, coef)
        if not terms:
            break
        # Sort by monom_tuple descending (lex with x1 first)
        terms_sorted = sorted(terms, key=lambda t: t[0], reverse=True)
        alpha, coef = terms_sorted[0]
        # alpha should be a partition (weakly decreasing). Verify.
        if not all(alpha[i] >= alpha[i+1] for i in range(len(alpha)-1)):
            raise ValueError(f"Leading monomial exponent {alpha} is not a partition; polynomial not symmetric?")
        # Conjugate partition λ = α'
        # α as list, ignore trailing zeros
        alpha_list = list(alpha)
        while alpha_list and alpha_list[-1] == 0:
            alpha_list.pop()
        if not alpha_list:
            # constant term
            lam = ()
            result[lam] = result.get(lam, 0) + coef
            hp = expand(hp - coef)
            continue
        max_part = alpha_list[0]
        conjugate = tuple(sum(1 for a in alpha_list if a >= i) for i in range(1, max_part + 1))
        lam = conjugate  # e-partition (weakly decreasing)
        # Build e_lam
        e_lam = 1
        for part in lam:
            e_lam *= elementary_sym(part, xs)
        e_lam = expand(e_lam)
        # Sanity: leading monomial of e_lam should equal x^alpha with coefficient 1
        P_elam = Poly(e_lam, *xs)
        e_terms_sorted = sorted(P_elam.terms(), key=lambda t: t[0], reverse=True)
        assert e_terms_sorted[0][0] == alpha, f"leading monomial mismatch: e_{lam} has {e_terms_sorted[0][0]}, expected {alpha}"
        assert e_terms_sorted[0][1] == 1, f"leading coefficient of e_{lam} should be 1, got {e_terms_sorted[0][1]}"
        result[lam] = result.get(lam, 0) + coef
        hp = expand(hp - coef * e_lam)

    return result


def format_e_basis(d):
    """Format e-basis dict as readable string."""
    if not d:
        return "0"
    parts = []
    for lam in sorted(d.keys(), key=lambda x: (-sum(x), x)):
        c = d[lam]
        c_str = str(c)
        if lam == ():
            lam_str = "1"
        else:
            lam_str = "*".join(f"e_{p}" for p in lam)
        parts.append(f"({c_str}) * {lam_str}")
    return "  +  ".join(parts)


# ---------------------------------------------------------------------------
# (Re): X_{P_n}(q) = e_n + q Σ_{k=2}^n [k-1]_q e_k X_{P_{n-k}}
# ---------------------------------------------------------------------------

def q_int(k, q):
    """[k]_q = 1 + q + ... + q^{k-1}."""
    return sum(q**i for i in range(k))


def X_Pn_Re(n, xs, q):
    """Compute X_{P_n}(q) via (Re) recursion. Returns dict λ → coef(q)."""
    # Return as e-basis dict for stability
    if n == 0:
        return {(): sympify(1)}
    # X_{P_n} = e_n + q Σ_{k=2}^n [k-1]_q · e_k · X_{P_{n-k}}
    # In e-basis, prepending e_k to a partition (weakly decreasing) means
    # inserting k in the right spot.
    result = {}
    # e_n term
    if n > 0:
        result[(n,)] = sympify(1)
    for k in range(2, n + 1):
        sub = X_Pn_Re(n - k, xs, q)
        coeff = q * q_int(k - 1, q)
        for lam, c in sub.items():
            new_lam = tuple(sorted((k,) + lam, reverse=True))
            result[new_lam] = result.get(new_lam, 0) + expand(coeff * c)
    return {lam: expand(c) for lam, c in result.items() if expand(c) != 0}


# ---------------------------------------------------------------------------
# (Comp): compositional formula
# ---------------------------------------------------------------------------

def compositions_comp(n):
    """
    Yield all compositions (k_1, ..., k_r) of n with k_i >= 2 for i < r and k_r >= 1.
    """
    if n == 0:
        return
    # k_r >= 1, k_1, ..., k_{r-1} >= 2
    # Enumerate r from 1 to n
    def rec(remaining, prefix, first_is_last):
        if first_is_last:
            # We're placing the last part; k_r >= 1, k_r = remaining
            if remaining >= 1:
                yield tuple(prefix) + (remaining,)
            return
        # Either terminate now (this part is k_r)
        if remaining >= 1:
            yield tuple(prefix) + (remaining,)
        # Or extend: current part is k_i for i < r, so >= 2
        for k in range(2, remaining):
            # remaining - k > 0 still, more parts to add
            yield from rec(remaining - k, prefix + [k], False)
    # Careful with duplicate paths — let me restructure
    def gen(remaining):
        # yield compositions (k_1,...,k_r) with all k_i>=2 except last k_r>=1
        # base case r=1: single part k_r = remaining, need >= 1
        if remaining >= 1:
            yield (remaining,)
        # r >= 2: first part k_1 >= 2, rest recursively
        for k in range(2, remaining):  # k <= remaining - 1 so tail non-empty
            for tail in gen(remaining - k):
                yield (k,) + tail
    yield from gen(n)


def X_Pn_Comp(n, xs, q):
    """Compute X_{P_n}(q) via (Comp) formula. Returns dict λ → coef(q)."""
    if n == 0:
        return {(): sympify(1)}
    result = {}
    for comp in compositions_comp(n):
        r = len(comp)
        k_r = comp[-1]
        coeff = q**(r - 1) * q_int(k_r, q)
        for i in range(r - 1):
            coeff *= q_int(comp[i] - 1, q)
        lam = tuple(sorted(comp, reverse=True))
        result[lam] = result.get(lam, 0) + expand(coeff)
    return {lam: expand(c) for lam, c in result.items() if expand(c) != 0}


# ---------------------------------------------------------------------------
# Multiply two e-basis dicts (formal product in Λ)
# ---------------------------------------------------------------------------

def multiply_e(d1, d2):
    """Multiply two e-basis dicts as products of e_k's."""
    result = {}
    for lam1, c1 in d1.items():
        for lam2, c2 in d2.items():
            lam = tuple(sorted(lam1 + lam2, reverse=True))
            result[lam] = result.get(lam, 0) + expand(c1 * c2)
    return {lam: expand(c) for lam, c in result.items() if expand(c) != 0}


def e_dict_to_poly(d, xs):
    """Convert e-basis dict to actual symmetric polynomial in xs."""
    total = 0
    for lam, c in d.items():
        term = c
        for part in lam:
            term *= elementary_sym(part, xs)
        total += term
    return expand(total)


# ---------------------------------------------------------------------------
# Direct chromatic quasisymmetric function for K_2 ⊔ P_2 (Ellzey-Wachs)
# ---------------------------------------------------------------------------

def X_G_direct(edges, num_verts, xs, q):
    """
    Compute X_G(q) directly by summing over all proper colorings κ: V → {1,...,len(xs)}
    with asc weight.

    edges: list of (i, j) with i < j (using 1-indexed vertex labels 1..num_verts).
    """
    n_colors = len(xs)
    total = 0
    for coloring in product(range(1, n_colors + 1), repeat=num_verts):
        # check proper
        proper = all(coloring[i - 1] != coloring[j - 1] for (i, j) in edges)
        if not proper:
            continue
        asc = sum(1 for (i, j) in edges if coloring[i - 1] < coloring[j - 1])
        weight = q**asc
        for v in range(num_verts):
            weight *= xs[coloring[v] - 1]
        total += weight
    return expand(total)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    q = Symbol('q')
    # Use 4 variables for direct computation (K_2 ⊔ P_2 has 4 vertices)
    N_VARS = 4
    xs = symbols(f'x1:{N_VARS+1}')

    print("=" * 78)
    print("Day 188 — Multiplicativity spot-check: X_{K_2 ⊔ P_2}(q) =? X_{P_2}(q)^2")
    print("=" * 78)

    # -- Step 1: X_{P_2}(q) via (Re) and (Comp) --
    print("\nStep 1a: X_{P_2}(q) via (Re):")
    XP2_Re = X_Pn_Re(2, xs, q)
    print("  ", format_e_basis(XP2_Re))

    print("\nStep 1b: X_{P_2}(q) via (Comp):")
    XP2_Comp = X_Pn_Comp(2, xs, q)
    print("  ", format_e_basis(XP2_Comp))

    # Check they agree
    all_lams = set(XP2_Re.keys()) | set(XP2_Comp.keys())
    agree_1 = True
    for lam in all_lams:
        diff = expand(XP2_Re.get(lam, 0) - XP2_Comp.get(lam, 0))
        if diff != 0:
            agree_1 = False
            print(f"  MISMATCH at {lam}: {diff}")
    print(f"  (Re) vs (Comp) for P_2: {'AGREE' if agree_1 else 'DISAGREE'}")

    # Sanity: also compute via (Re) for P_1, P_3 as a smoke test
    print("\nSmoke tests (Re vs Comp) for n=1,3,4:")
    for n in (1, 3, 4):
        r = X_Pn_Re(n, xs, q)
        c = X_Pn_Comp(n, xs, q)
        lams = set(r.keys()) | set(c.keys())
        ok = all(expand(r.get(l, 0) - c.get(l, 0)) == 0 for l in lams)
        print(f"  n={n}: {'AGREE' if ok else 'DISAGREE'}")

    # -- Step 2: X_{P_2}(q)^2 --
    print("\nStep 2: X_{P_2}(q)^2 (from (Re), formal e-basis square):")
    XP2_sq = multiply_e(XP2_Re, XP2_Re)
    print("  ", format_e_basis(XP2_sq))

    # -- Step 3: Direct X_{K_2 ⊔ P_2}(q) --
    # Graph: vertices {1,2,3,4}, edges {(1,2), (3,4)} — K_2 on {1,2} disjoint K_2 on {3,4}
    # (K_2 = P_2 as unlabeled graphs.)
    print("\nStep 3: Direct X_{K_2 ⊔ P_2}(q) via Ellzey-Wachs enumeration:")
    edges = [(1, 2), (3, 4)]
    XG_poly = X_G_direct(edges, 4, xs, q)
    print(f"  Polynomial in x1..x4 has {len(Poly(XG_poly, *xs).terms())} monomials.")

    # -- Step 4: Convert to e-basis --
    XG_e = to_e_basis(XG_poly, xs, q, max_deg=4)
    print("  In e-basis:")
    print("  ", format_e_basis(XG_e))

    # -- Compare --
    print("\nStep 5: Compare X_{K_2 ⊔ P_2}(q) vs X_{P_2}(q)^2:")
    all_lams = set(XG_e.keys()) | set(XP2_sq.keys())
    all_match = True
    for lam in sorted(all_lams, key=lambda x: (-sum(x), x)):
        a = expand(XG_e.get(lam, 0))
        b = expand(XP2_sq.get(lam, 0))
        d = expand(a - b)
        marker = "OK" if d == 0 else "DIFF"
        if d != 0:
            all_match = False
        print(f"  λ={lam}: direct={a}   squared={b}   diff={d}  [{marker}]")

    print("\n" + "=" * 78)
    print(f"  RESULT: {'PASS' if all_match else 'FAIL'}")
    print("=" * 78)

    # If FAIL, try the descent convention as a sanity check
    if not all_match:
        print("\n[Convention sanity check] Trying descent (i<j, κ(i) > κ(j))...")

        def X_G_desc(edges, num_verts, xs, q):
            n_colors = len(xs)
            total = 0
            for coloring in product(range(1, n_colors + 1), repeat=num_verts):
                proper = all(coloring[i - 1] != coloring[j - 1] for (i, j) in edges)
                if not proper:
                    continue
                desc = sum(1 for (i, j) in edges if coloring[i - 1] > coloring[j - 1])
                weight = q**desc
                for v in range(num_verts):
                    weight *= xs[coloring[v] - 1]
                total += weight
            return expand(total)

        XG_poly2 = X_G_desc(edges, 4, xs, q)
        XG_e2 = to_e_basis(XG_poly2, xs, q, max_deg=4)
        print("  Descent-convention direct e-basis:", format_e_basis(XG_e2))
        all_lams2 = set(XG_e2.keys()) | set(XP2_sq.keys())
        match2 = all(expand(XG_e2.get(l, 0) - XP2_sq.get(l, 0)) == 0 for l in all_lams2)
        print(f"  Descent match: {'PASS' if match2 else 'FAIL'}")


if __name__ == '__main__':
    main()
