"""
Extend Day 178 verification to n=6.

Verify at n=6, for test m in {1, E_1, E_2, E_3, E_1*E_2, E_1*E_3, E_2^2}:
- Lemma 1: pi_rho(AR_0(m)) mod E_{>=4} = (n-1) E_1 S(m) = 5 E_1 S(m)
- Lemma 2: pi_rho(AR_k(m)) mod E_{>=4} = 0 for k in {1,2,3,4}

If arity 4 is too slow for a given m, we still record arity 0..3.
"""

import sympy as sp
from itertools import combinations
import time
import sys

n = 6
u = sp.symbols(f'u1:{n+1}')  # u1..u6

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
    ("1",       []),
    ("E_1",     [1]),
    ("E_2",     [2]),
    ("E_3",     [3]),
    ("E_1*E_2", [1, 2]),
    ("E_1*E_3", [1, 3]),
    ("E_2^2",   [2, 2]),
]

# Max arity to attempt per m. Keep small for E_1*E_3 and E_2^2 which are heavier.
# n-1 = 5 in principle but Lemma 2 targets k=1..4.
MAX_ARITY = {
    "1":       4,
    "E_1":     4,
    "E_2":     4,
    "E_3":     4,
    "E_1*E_2": 4,
    "E_1*E_3": 4,
    "E_2^2":   4,
}

# Per-arity timeout (seconds) — if a single AR_k takes longer, we abort that (m,k).
# We don't have SIGALRM budget here — instead we time each and warn.

print(f"n = {n}")
print("="*70)

out_lines = []
def P(s=""):
    out_lines.append(str(s))
    print(s)
    sys.stdout.flush()

def flush_report():
    with open('/home/agent/projects/scratch/day179/verify_n6_out.txt', 'w') as f:
        f.write("\n".join(out_lines))

pass_count = 0
fail_count = 0
skip_count = 0
per_line_results = []  # list of (m_name, k, status_str)

for name, indices in test_ms:
    P("")
    P(f"### m = {name}")
    t_m_start = time.time()
    rho_m = rho_of_indices(indices)
    target = rho_m + 1
    P(f"rho(m) = {rho_m}, top-rho target = {target}")
    m_expr = m_from_indices(indices)

    max_k = MAX_ARITY[name]
    contributions = {}
    E_syms = None
    for k in range(0, max_k + 1):
        t0 = time.time()
        try:
            AR = AR_k_operator(m_expr, k)
            AR_c = sp.cancel(sp.together(AR))
            num, den = sp.together(AR_c).as_numer_denom()
            if den.free_symbols & set(u):
                elapsed = time.time() - t0
                P(f"  arity {k}: FAILED polynomiality; denom={den} ({elapsed:.1f}s)")
                per_line_results.append((name, k, "FAIL (not polynomial)"))
                fail_count += 1
                continue
            AR_E, E_syms = symmetric_to_E(AR_c)
            proj = project_top_rho_mod_E4(AR_E, E_syms, target)
            contributions[k] = proj
            elapsed = time.time() - t0
            P(f"  pi_rho(AR_{k}(m)) mod E_(>=4) = {proj}   [t={elapsed:.1f}s]")
        except Exception as e:
            elapsed = time.time() - t0
            P(f"  arity {k}: ERROR {e} [t={elapsed:.1f}s]")
            per_line_results.append((name, k, f"ERROR {e}"))
            fail_count += 1
            continue
        # incremental flush after each (m,k)
        flush_report()

    # Predicted
    if E_syms is None:
        E_syms = sp.symbols(f'E1:{n+1}')
    m_in_E = sp.Integer(1)
    for k in indices:
        m_in_E *= E_syms[k-1]
    Sm = S_op(m_in_E, E_syms)
    predicted = (n - 1) * E_syms[0] * Sm
    predicted = sp.expand(predicted)
    P(f"  Predicted (n-1) E_1 S(m) = {predicted}")

    # Check L1
    if 0 in contributions:
        ar0 = contributions[0]
        diff = sp.expand(ar0 - predicted)
        status = "PASS" if diff == 0 else "FAIL"
        P(f"  L1 CHECK: arity-0 - predicted = {diff}  ({status})")
        per_line_results.append((name, 0, status))
        if diff == 0:
            pass_count += 1
        else:
            fail_count += 1
    else:
        P(f"  L1 CHECK: SKIPPED (arity 0 not computed)")
        per_line_results.append((name, 0, "SKIP"))
        skip_count += 1

    # Check L2 for k=1..min(4, max_k)
    for k in range(1, max_k + 1):
        if k in contributions:
            ar_k = contributions[k]
            status = "PASS" if ar_k == 0 else "FAIL"
            P(f"  L2 CHECK arity {k}: {ar_k}  ({status})")
            per_line_results.append((name, k, status))
            if ar_k == 0:
                pass_count += 1
            else:
                fail_count += 1
        else:
            P(f"  L2 CHECK arity {k}: SKIPPED")
            per_line_results.append((name, k, "SKIP"))
            skip_count += 1

    dt = time.time() - t_m_start
    P(f"  (total time for m={name}: {dt:.1f}s)")
    flush_report()

P("")
P("="*70)
P("PER-LINE SUMMARY")
for name, k, status in per_line_results:
    P(f"  m={name:<10} k={k}  {status}")

total = pass_count + fail_count
P("")
P(f"OVERALL: {pass_count}/{total} pass  ({fail_count} fail, {skip_count} skip)")

flush_report()
