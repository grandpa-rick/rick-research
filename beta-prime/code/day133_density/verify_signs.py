"""Verify: (1) closed-form A(T)*B(T) recovers tops[b] for small b,
          (2) uniform-sign prediction (-1)^(b-x2-x3) matches every coefficient."""
import sympy as sp
from sympy import symbols, series, Rational, prod, factorial, binomial, log, exp

E1, E2, E3, T = symbols('E1 E2 E3 T')

def A_series(N):
    """Return list of A_n for n=0..N-1 as polynomials in E1,E2."""
    # A_n = prod_{k=0..n-1} (E2 - (k+1)*E1)
    A = [sp.Integer(1)]
    for n in range(1, N):
        A.append(sp.expand(A[-1] * (E2 - n*E1)))
    return A

def M_coeffs(N):
    """Return mu_n for n=2..N, mu_n = (-1)^{n-1} (n^2-1)/n."""
    mu = {n: (-1)**(n-1) * Rational(n*n-1, n) for n in range(2, N+1)}
    return mu

def B_via_series(N):
    """B(T) = exp(E3 * M(T)) as series to order N."""
    mu = M_coeffs(N)
    Mpoly = sum(mu[n] * E1**(n-2) * T**n for n in range(2, N+1))
    Bexp = sp.Integer(1)
    # exp(E3 M) = sum_{k>=0} (E3 M)^k / k! ; truncate at k <= N//2
    curr = sp.Integer(1)
    for k in range(1, N//2 + 1):
        curr = sp.expand(curr * E3 * Mpoly / k)
        # keep terms up to T^N
        curr = sp.Poly(curr, T).as_expr() if False else curr
        # extract series in T up to order N
        curr = sp.series(curr, T, 0, N+1).removeO() if False else curr
        # simpler: expand as poly in T, drop T^{>N}
        p = sp.Poly(sp.expand(curr), T)
        curr = sum(c * T**deg[0] for deg, c in p.terms() if deg[0] <= N)
        Bexp = sp.expand(Bexp + curr)
    # extract B_m = m! * [T^m] Bexp
    p = sp.Poly(sp.expand(Bexp), T)
    Bm = {m: sp.Integer(0) for m in range(N+1)}
    for deg, c in p.terms():
        Bm[deg[0]] = sp.expand(c * factorial(deg[0]))
    return Bm

def tops_via_closed_form(B):
    """tops[b] = sum_{n+m=b} C(b,n) A_n B_m."""
    N = 12
    A = A_series(N+1)
    Bm = B_via_series(N)
    tops = {}
    for b in range(N+1):
        s = sp.Integer(0)
        for n in range(b+1):
            m = b - n
            s = s + binomial(b, n) * A[n] * Bm[m]
        tops[b] = sp.expand(s)
    return tops

tops = tops_via_closed_form(None)

# Check sanity list from PROVE.md
print("=== Sanity checks ===")
for b in range(9):
    p = sp.Poly(tops[b], E1, E2, E3)
    d_E1b = p.coeff_monomial((b, 0, 0)) if b > 0 else (1 if b == 0 else 0)
    d_E2b = p.coeff_monomial((0, b, 0)) if b > 0 else (1 if b == 0 else 0)
    print(f"b={b}: [E1^b]={d_E1b}  (expect (-1)^b * b! = {(-1)**b * factorial(b)})")
    print(f"      [E2^b]={d_E2b}  (expect 1)")
    if b % 2 == 0 and b > 0:
        e3half = p.coeff_monomial((0, 0, b//2))
        print(f"      [E3^{{b/2}}]={e3half}")

# Full uniform-sign check for b = 0..8
print("\n=== Uniform-sign check for every coefficient ===")
failed = 0
for b in range(9):
    p = sp.Poly(tops[b], E1, E2, E3)
    for (a, c, d), coeff in p.terms():
        if coeff == 0:
            continue
        # (1,1,2)-weight check
        if a + c + 2*d != b:
            print(f"  b={b} WEIGHT VIOLATION E1^{a}E2^{c}E3^{d} coeff={coeff}")
            failed += 1
            continue
        expected_sign = (-1)**(b - c - d)
        actual_sign = 1 if coeff > 0 else -1
        if expected_sign != actual_sign:
            print(f"  b={b} SIGN MISMATCH E1^{a}E2^{c}E3^{d}: coeff={coeff}, expected sign (-1)^{{{b-c-d}}}={expected_sign}")
            failed += 1
if failed == 0:
    print("  ALL SIGNS MATCH (-1)^(b-x2-x3) for b=0..8. Uniform sign confirmed.")

# Explicit tops[2] to eyeball
print("\ntops[2] =", tops[2])
print("tops[3] =", tops[3])
print("tops[4] =", tops[4])
