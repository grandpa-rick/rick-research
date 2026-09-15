"""
Arity decomposition of B_1^{(n)}(m) + B_0^{(n)}(m) at n=4.

For each m in a chosen list, compute:
- AR_0(m), AR_1(m), AR_2(m): the arity-k slice of (B_1+B_0)(m)
- Verify each slice is a polynomial in u (poles cancel across summands)
- Symmetrize to polynomial in E_1..E_n
- Take top-ρ (ρ-weight ρ(m)+1) and restrict mod E_4

Compare arity-0 alone vs total against (n-1) E_1 S(m).
"""

import sympy as sp
from itertools import combinations
from sympy import symbols, Rational, together, cancel, simplify, expand, Poly, binomial, symmetrize
from sympy.polys.specialpolys import symmetric_poly

n = 4
u = sp.symbols(f'u1:{n+1}')  # u1..u4
n_sym = sp.symbols('n_sym', positive=True)  # symbolic n (for reporting)

# Elementary symmetric E_1..E_n in the u's
E = [None] + [sp.symmetric_poly(k, u) for k in range(1, n+1)]
# rho weight function
def rho_weight_of_E_monomial(monomial_tuple):
    """monomial_tuple = (a1,...,an) for E_1^a1 ... E_n^an. rho weight = sum a_k * ceil(k/2)."""
    return sum(a * ((k + 1) // 2 + (1 if False else 0)) for k, a in enumerate(monomial_tuple, start=1))
# Actually ceil(k/2) = (k+1)//2 for positive integer k
def rho(k):
    return (k + 1) // 2

# --------- Helpers ---------

def vratio(i, j):
    """V_n(u + e_i + e_j) / V_n(u), i,j are 1-indexed indices in [1..n]."""
    # Product over l<m of ((u+e_i+e_j)_l - (u+e_i+e_j)_m)/(u_l-u_m)
    # Only pairs involving i or j (but not both, since both shift by 1 leaves them equal) matter.
    # Standard formula: V_n(u+e_i+e_j)/V_n(u) = prod_{l != i,j} (1 + 1/(u_i-u_l)) * (1 + 1/(u_j-u_l))
    ii = i - 1
    jj = j - 1
    prod = sp.Integer(1)
    for l in range(n):
        if l == ii or l == jj:
            continue
        prod *= (1 + 1/(u[ii] - u[l])) * (1 + 1/(u[jj] - u[l]))
    return prod

def delta(i, j, l):
    """Delta_{ij}(l) = 1/(u_i-u_l) + 1/(u_j-u_l) + 1/[(u_i-u_l)(u_j-u_l)], 1-indexed."""
    ii, jj, ll = i-1, j-1, l-1
    return 1/(u[ii]-u[ll]) + 1/(u[jj]-u[ll]) + 1/((u[ii]-u[ll])*(u[jj]-u[ll]))

def shifted_m(m_expr, i, j):
    """Substitute u_i -> u_i+1, u_j -> u_j+1 into m_expr (function of u tuple)."""
    return m_expr.subs([(u[i-1], u[i-1]+1), (u[j-1], u[j-1]+1)], simultaneous=True)

def AR_k_operator(m_expr, k):
    """
    (B_1+B_0)(m) arity-k slice:
    Sum_{i<j} (1 + u_i + u_j) * m(u+e_i+e_j) * Sum_{L subseteq [n]\{i,j}, |L|=k} prod_{l in L} Delta_{ij}(l)
    """
    total = sp.Integer(0)
    idx = list(range(1, n+1))
    for i, j in combinations(idx, 2):
        rest = [l for l in idx if l != i and l != j]
        mij = shifted_m(m_expr, i, j)
        # weight for B_1 + B_0 = (u_i + u_j) + 1
        weight = (u[i-1] + u[j-1]) + 1
        arity_sum = sp.Integer(0)
        for L in combinations(rest, k):
            prod = sp.Integer(1)
            for l in L:
                prod *= delta(i, j, l)
            arity_sum += prod
        total += weight * mij * arity_sum
    return total

# --------- Symmetrization to E_1..E_n ---------

def symmetric_to_E(poly_expr):
    """
    Given a symmetric polynomial in u_1..u_n, express as polynomial in E_1..E_n.
    Uses sympy.symmetrize with formal=True to get formal E symbols.
    """
    p_together = sp.together(poly_expr)
    p_c = sp.cancel(p_together)
    p_c = sp.expand(p_c)
    denom = sp.together(p_c).as_numer_denom()[1]
    if denom.free_symbols & set(u):
        raise ValueError(f"Not a polynomial in u; denom = {denom}")
    # Use formal=True; supply our own symbols
    E_syms = sp.symbols(f'E1:{n+1}')
    result, rem, subs_list = sp.symmetrize(p_c, u, formal=True, symbols=E_syms)
    # subs_list is like [(E1, u1+..+un), (E2, ...), ...]
    if sp.expand(rem) != 0:
        raise ValueError(f"symmetrize left remainder: {rem}")
    return sp.expand(result), E_syms

# --------- rho weight & top-rho projection ---------

def rho_weight_of_monom_in_E(monom_powers):
    """monom_powers = dict-like or tuple of exponents on (E1, E2, ..., En)."""
    w = 0
    for k, a in enumerate(monom_powers, start=1):
        w += a * rho(k)
    return w

def project_top_rho_mod_E4(expr_in_E, E_syms, target_weight):
    """
    Keep only monomials in E1..En with rho-weight == target_weight AND E_4 exponent == 0.
    Returns polynomial in E1, E2, E3.
    """
    p = sp.Poly(sp.expand(expr_in_E), *E_syms)
    result = sp.Integer(0)
    for monom, coeff in p.terms():
        # monom = (a1, a2, a3, a4)
        a4 = monom[3] if len(monom) >= 4 else 0
        if a4 != 0:
            continue
        w = rho_weight_of_monom_in_E(monom)
        if w != target_weight:
            continue
        term = coeff
        for k, a in enumerate(monom, start=1):
            term *= E_syms[k-1]**a
        result += term
    return sp.expand(result)

# --------- S operator: E_2 -> E_2 + E_1 ---------

def S_op(expr, E_syms):
    """S = e^{E_1 d/dE_2}: shifts E_2 -> E_2 + E_1."""
    E1, E2 = E_syms[0], E_syms[1]
    return sp.expand(expr.subs(E2, E2 + E1))

# --------- Test items ---------

def m_from_E_indices(indices, E_syms_local=None):
    """Build monomial m(u) in u's from list of E indices, e.g. [1,2] -> E_1*E_2."""
    prod = sp.Integer(1)
    for k in indices:
        prod *= E[k]
    return sp.expand(prod)

# ρ weights: rho(E_1)=1, rho(E_2)=1, rho(E_3)=2, rho(E_2^2)=2, rho(E_1 E_2)=2, rho(E_2 E_3)=3
test_ms = [
    ("1", []),
    ("E_1", [1]),
    ("E_2", [2]),
    ("E_3", [3]),
    ("E_2^2", [2, 2]),
    ("E_1 E_2", [1, 2]),
    ("E_2 E_3", [2, 3]),
]

def rho_of_indices(indices):
    return sum(rho(k) for k in indices)

# --------- Main ---------

def run():
    out_lines = []
    def P(s=""):
        out_lines.append(str(s))
        print(s)

    P(f"n = {n}")
    P(f"Arity decomposition of (B_1 + B_0)(m), n=4")
    P("="*70)

    for name, indices in test_ms:
        P("")
        P("#"*70)
        P(f"m = {name}")
        rho_m = rho_of_indices(indices)
        target = rho_m + 1
        P(f"rho(m) = {rho_m}, top-rho target weight = {target}")
        m_expr = m_from_E_indices(indices)
        P(f"m(u) = {sp.expand(m_expr)}")

        # Compute per arity
        contributions = {}
        arity_pi_rho = {}
        for k in range(0, 3):  # arities 0, 1, 2
            AR = AR_k_operator(m_expr, k)
            # Check polynomiality: cancel denominators
            AR_c = sp.cancel(sp.together(AR))
            num, den = sp.together(AR_c).as_numer_denom()
            poly_ok = not (den.free_symbols & set(u))
            P(f"\n--- Arity k = {k} ---")
            P(f"  Polynomiality check: {'PASS' if poly_ok else 'FAIL (denom has u)'}")
            if not poly_ok:
                P(f"  denominator = {den}")
            # Symmetrize
            try:
                AR_E, E_syms = symmetric_to_E(AR_c)
            except Exception as e:
                P(f"  Symmetrize failed: {e}")
                continue
            # Print in E form (may be long; truncate)
            s = str(AR_E)
            if len(s) > 220:
                s = s[:220] + "..."
            P(f"  AR_{k}(m) in E-basis (n={n}): {s}")
            # Project to top-rho mod E_4
            proj = project_top_rho_mod_E4(AR_E, E_syms, target)
            arity_pi_rho[k] = (proj, E_syms)
            P(f"  pi_rho(AR_{k}(m)) | mod E_4 = {proj}")
            contributions[k] = proj

        # Sum
        E_syms = arity_pi_rho[0][1]
        total_proj = sum(p for p, _ in arity_pi_rho.values())
        total_proj = sp.expand(total_proj)
        P(f"\n  SUM over arities 0,1,2 = {total_proj}")

        # Predicted: (n-1) E_1 S(m)
        # Interpret S(m): S acts on m written in E's -> substitute E_2 -> E_2 + E_1.
        m_in_E = sp.Integer(1)
        for k in indices:
            m_in_E *= E_syms[k-1]
        Sm = S_op(m_in_E, E_syms)
        # Also drop E_4-containing terms in Sm (there won't be any since indices <= 3)
        predicted_n_sym = (n_sym - 1) * E_syms[0] * Sm
        # For n=4:
        predicted_num = (n - 1) * E_syms[0] * Sm
        predicted_num = sp.expand(predicted_num)
        P(f"  Predicted (n=4): (n-1) E_1 S(m) = 3 * E_1 * ({Sm}) = {predicted_num}")
        P(f"  Predicted symbolic:  (n-1) E_1 S(m) = (n-1) * E_1 * ({Sm})")

        # Match?
        diff = sp.expand(total_proj - predicted_num)
        # Also drop E_4 terms in diff (shouldn't be any)
        p_diff = sp.Poly(diff, *E_syms)
        # Zero out E_4-containing terms just to be safe
        diff_no_E4 = sp.Integer(0)
        for monom, coeff in p_diff.terms():
            a4 = monom[3] if len(monom) >= 4 else 0
            if a4 != 0:
                continue
            term = coeff
            for kk, a in enumerate(monom, start=1):
                term *= E_syms[kk-1]**a
            diff_no_E4 += term
        diff_no_E4 = sp.expand(diff_no_E4)
        P(f"  TOTAL - predicted (mod E_4) = {diff_no_E4}")

        # Arity-0 alone vs predicted?
        ar0 = contributions.get(0, sp.Integer(0))
        diff0 = sp.expand(ar0 - predicted_num)
        p_diff0 = sp.Poly(diff0, *E_syms)
        diff0_no_E4 = sp.Integer(0)
        for monom, coeff in p_diff0.terms():
            a4 = monom[3] if len(monom) >= 4 else 0
            if a4 != 0:
                continue
            term = coeff
            for kk, a in enumerate(monom, start=1):
                term *= E_syms[kk-1]**a
            diff0_no_E4 += term
        diff0_no_E4 = sp.expand(diff0_no_E4)
        P(f"  ARITY-0 - predicted (mod E_4) = {diff0_no_E4}")

    with open('/home/agent/projects/scratch/day178/arity_out.txt', 'w') as f:
        f.write("\n".join(out_lines))

if __name__ == "__main__":
    run()
