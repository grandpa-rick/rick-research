"""
Day 179 — Full rho-degree decomposition of AR_k(m) mod E_{>=4} at n=5.

For each test m and each arity k in {0, 1, 2, 3}:
  1. Compute AR_k(m).
  2. Symmetrize to E-basis.
  3. Drop all monomials containing E_4 or E_5.
  4. Split the remaining polynomial into rho-graded pieces.
  5. Report the FULL expression and each rho-graded slice.

Conjecture to test (k >= 1, m in Q[E_1, E_2, E_3]):
    max rho-weight of AR_k(m) mod E_{>=4}  <=  rho(m)
    (compared to AR_0(m) which has top rho-weight rho(m)+1).
"""

import sympy as sp
from itertools import combinations

n = 5
u = sp.symbols(f'u1:{n+1}')
E_syms = sp.symbols(f'E1:{n+1}')

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
    result, rem, _ = sp.symmetrize(p_c, u, formal=True, symbols=E_syms)
    if sp.expand(rem) != 0:
        raise ValueError(f"symmetrize left remainder: {rem}")
    return sp.expand(result)

def rho_weight_of_monom(monom):
    return sum(a * rho(k) for k, a in enumerate(monom, start=1))

def drop_E_geq_4(expr_in_E):
    """Keep only monomials whose E_4, E_5, ... exponents are all 0."""
    p = sp.Poly(sp.expand(expr_in_E), *E_syms)
    result = sp.Integer(0)
    for monom, coeff in p.terms():
        if any(monom[k-1] > 0 for k in range(4, n+1)):
            continue
        term = coeff
        for k, a in enumerate(monom, start=1):
            term *= E_syms[k-1]**a
        result += term
    return sp.expand(result)

def split_by_rho(expr_in_E):
    """Return {rho_weight: expression} for expr already restricted to E_1,E_2,E_3."""
    if expr_in_E == 0:
        return {}
    p = sp.Poly(sp.expand(expr_in_E), *E_syms)
    slices = {}
    for monom, coeff in p.terms():
        w = rho_weight_of_monom(monom)
        term = coeff
        for k, a in enumerate(monom, start=1):
            term *= E_syms[k-1]**a
        slices[w] = slices.get(w, sp.Integer(0)) + term
    return {w: sp.expand(v) for w, v in slices.items()}

def m_from_indices(indices):
    prod = sp.Integer(1)
    for k in indices:
        prod *= sp.symmetric_poly(k, u)
    return sp.expand(prod)

def rho_of_indices(indices):
    return sum(rho(k) for k in indices)

test_ms = [
    ("1",           []),
    ("E_1",         [1]),
    ("E_2",         [2]),
    ("E_3",         [3]),
    ("E_1^2",       [1, 1]),
    ("E_1*E_2",     [1, 2]),
    ("E_2^2",       [2, 2]),
    ("E_1^3",       [1, 1, 1]),
    ("E_1^2*E_2",   [1, 1, 2]),
    ("E_1*E_3",     [1, 3]),
]

out_lines = []
def P(s=""):
    out_lines.append(str(s))
    print(s, flush=True)

P(f"n = {n}")
P(f"rho(E_1)=1  rho(E_2)=1  rho(E_3)=2")
P("="*72)

# Track conjecture verification
conjecture_records = []  # list of dicts

for name, indices in test_ms:
    P("")
    P(f"### m = {name}   (rho(m) = {rho_of_indices(indices)})")
    m_expr = m_from_indices(indices)
    rho_m = rho_of_indices(indices)

    for k in range(0, 4):  # arity 0, 1, 2, 3
        P("")
        P(f"  --- AR_{k}(m) ---")
        try:
            AR = AR_k_operator(m_expr, k)
            AR_E = symmetric_to_E(AR)
            AR_E_reduced = drop_E_geq_4(AR_E)
            P(f"  Full AR_{k}(m) mod E_(>=4): {AR_E_reduced}")
            slices = split_by_rho(AR_E_reduced)
            if not slices:
                P(f"    (zero)")
                max_w = None
            else:
                max_w = max(slices.keys())
                for w in sorted(slices.keys()):
                    P(f"    rho-weight {w}:  {slices[w]}")
            if k >= 1:
                conj_ok = (max_w is None) or (max_w <= rho_m)
                conjecture_records.append(
                    dict(m=name, k=k, rho_m=rho_m, max_w=max_w, ok=conj_ok)
                )
                verdict = "PASS" if conj_ok else "FAIL"
                mw_str = "none" if max_w is None else str(max_w)
                P(f"    [conjecture: k>=1 => max_w <= rho(m)={rho_m};  observed max_w={mw_str};  {verdict}]")
        except Exception as e:
            P(f"  ERROR: {e}")

P("")
P("="*72)
P("SUMMARY OF CONJECTURE (k >= 1, m in Q[E_1,E_2,E_3]):")
P("  max rho-weight of AR_k(m) mod E_(>=4)  <=  rho(m)")
P("")
P(f"{'m':<15} {'k':>3} {'rho(m)':>7} {'max_w':>7}  verdict")
P("-"*50)
all_ok = True
for r in conjecture_records:
    mw_str = "none" if r['max_w'] is None else str(r['max_w'])
    verdict = "PASS" if r['ok'] else "FAIL"
    if not r['ok']:
        all_ok = False
    P(f"{r['m']:<15} {r['k']:>3} {r['rho_m']:>7} {mw_str:>7}  {verdict}")

P("")
P(f"OVERALL: {'ALL PASS' if all_ok else 'FAILURES PRESENT'} "
  f"({sum(1 for r in conjecture_records if r['ok'])}/{len(conjecture_records)})")

with open('/home/agent/projects/scratch/day179/rho_drop_full_out.txt', 'w') as f:
    f.write("\n".join(out_lines))
