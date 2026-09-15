"""
Arity decomposition of B_1^{(n)}(m) + B_0^{(n)}(m) at n=5, small monomials.
Verify Lemma 1 (arity-0 = (n-1) E_1 S(m) mod E_{>=4})
and Lemma 2 (arity 1, 2, 3 vanish mod E_{>=4} at top-rho)
for a few m to increase confidence.
"""

import sympy as sp
from itertools import combinations

n = 5
u = sp.symbols(f'u1:{n+1}')  # u1..u5

def rho(k):
    return (k + 1) // 2

def delta(i, j, l):
    ii, jj, ll = i-1, j-1, l-1
    return 1/(u[ii]-u[ll]) + 1/(u[jj]-u[ll]) + 1/((u[ii]-u[ll])*(u[jj]-u[ll]))

def shifted_m(m_expr, i, j):
    return m_expr.subs([(u[i-1], u[i-1]+1), (u[j-1], u[j-1]+1)], simultaneous=True)

def AR_k_operator(m_expr, k):
    total = sp.Integer(0)
    idx = list(range(1, n+1))
    for i, j in combinations(idx, 2):
        rest = [l for l in idx if l != i and l != j]
        mij = shifted_m(m_expr, i, j)
        weight = (u[i-1] + u[j-1]) + 1
        arity_sum = sp.Integer(0)
        for L in combinations(rest, k):
            prod = sp.Integer(1)
            for l in L:
                prod *= delta(i, j, l)
            arity_sum += prod
        total += weight * mij * arity_sum
    return total

def symmetric_to_E(poly_expr):
    p_c = sp.cancel(sp.together(poly_expr))
    p_c = sp.expand(p_c)
    denom = sp.together(p_c).as_numer_denom()[1]
    if denom.free_symbols & set(u):
        raise ValueError(f"Not polynomial in u; denom={denom}")
    E_syms = sp.symbols(f'E1:{n+1}')
    result, rem, _ = sp.symmetrize(p_c, u, formal=True, symbols=E_syms)
    if sp.expand(rem) != 0:
        raise ValueError(f"symmetrize left remainder: {rem}")
    return sp.expand(result), E_syms

def rho_weight_of_monom(monom):
    return sum(a * rho(k) for k, a in enumerate(monom, start=1))

def project_top_rho_mod_E4(expr_in_E, E_syms, target_weight):
    p = sp.Poly(sp.expand(expr_in_E), *E_syms)
    result = sp.Integer(0)
    for monom, coeff in p.terms():
        # zero if any exponent E_{>=4}
        if any(monom[k-1] > 0 for k in range(4, n+1)):
            continue
        w = rho_weight_of_monom(monom)
        if w != target_weight:
            continue
        term = coeff
        for k, a in enumerate(monom, start=1):
            term *= E_syms[k-1]**a
        result += term
    return sp.expand(result)

def S_op(expr, E_syms):
    return sp.expand(expr.subs(E_syms[1], E_syms[1] + E_syms[0]))

def m_from_indices(indices):
    prod = sp.Integer(1)
    for k in indices:
        prod *= sp.symmetric_poly(k, u)
    return sp.expand(prod)

def rho_of_indices(indices):
    return sum(rho(k) for k in indices)

test_ms = [
    ("1", []),
    ("E_1", [1]),
    ("E_2", [2]),
    ("E_3", [3]),
    ("E_1*E_2", [1, 2]),
]

print(f"n = {n}")
print("="*70)

out_lines = []
def P(s=""):
    out_lines.append(str(s))
    print(s)

all_pass = True
for name, indices in test_ms:
    P("")
    P(f"### m = {name}")
    rho_m = rho_of_indices(indices)
    target = rho_m + 1
    P(f"rho(m) = {rho_m}, top-rho target = {target}")
    m_expr = m_from_indices(indices)

    # arity 0 first
    contributions = {}
    for k in range(0, min(4, n-1)):  # arity 0..3 at n=5
        try:
            AR = AR_k_operator(m_expr, k)
            AR_c = sp.cancel(sp.together(AR))
            num, den = sp.together(AR_c).as_numer_denom()
            if den.free_symbols & set(u):
                P(f"  arity {k}: FAILED polynomiality; denom={den}")
                continue
            AR_E, E_syms = symmetric_to_E(AR_c)
            proj = project_top_rho_mod_E4(AR_E, E_syms, target)
            contributions[k] = proj
            P(f"  pi_rho(AR_{k}(m)) mod E_(>=4) = {proj}")
        except Exception as e:
            P(f"  arity {k}: ERROR {e}")
            continue

    # Predicted
    m_in_E = sp.Integer(1)
    for k in indices:
        m_in_E *= E_syms[k-1]
    Sm = S_op(m_in_E, E_syms)
    predicted = (n - 1) * E_syms[0] * Sm
    predicted = sp.expand(predicted)
    P(f"  Predicted (n-1) E_1 S(m) = {predicted}")

    # Check
    ar0 = contributions.get(0, sp.Integer(0))
    diff = sp.expand(ar0 - predicted)
    P(f"  L1 CHECK: arity-0 - predicted = {diff}  ({'PASS' if diff == 0 else 'FAIL'})")
    if diff != 0:
        all_pass = False

    for k in range(1, min(4, n-1)):
        ar_k = contributions.get(k, sp.Integer(0))
        P(f"  L2 CHECK arity {k}: {ar_k}  ({'PASS' if ar_k == 0 else 'FAIL'})")
        if ar_k != 0:
            all_pass = False

P("")
P("="*70)
P(f"OVERALL: {'ALL PASS' if all_pass else 'FAILURES'}")

with open('/home/agent/projects/scratch/day178/arity_n5_out.txt', 'w') as f:
    f.write("\n".join(out_lines))
