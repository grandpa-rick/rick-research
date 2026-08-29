"""Verify: each individual (n, m) contribution to a fixed coefficient of tops[b]
has sign (-1)^(b-x2-x3), matching the uniform-sign prediction."""
import sympy as sp
from sympy import symbols, Rational, factorial, binomial, prod

E1, E2, E3 = symbols('E1 E2 E3')

def A_n(n):
    """A_n = prod_{r=1}^n (E2 - r*E1)."""
    if n == 0: return sp.Integer(1)
    return sp.expand(prod(E2 - r*E1 for r in range(1, n+1)))

def M_series_expand_pow(k, m):
    """[T^m E1^{m-2k}] M(T)^k as a Rational.
    M(T) = sum_{n>=2} mu_n E1^{n-2} T^n, mu_n = (-1)^{n-1} (n^2-1)/n.
    [T^m] M(T)^k = sum over compositions (n_1,...,n_k), n_i>=2, sum=m, of prod mu_{n_i}.
    """
    if k == 0:
        return sp.Integer(1) if m == 0 else sp.Integer(0)
    if m < 2*k:
        return sp.Integer(0)
    def mu(n): return Rational((-1)**(n-1) * (n*n - 1), n)
    def compositions(m, k):
        if k == 1:
            if m >= 2: yield (m,)
            return
        for first in range(2, m - 2*(k-1) + 1):
            for rest in compositions(m - first, k - 1):
                yield (first,) + rest
    return sum(prod(mu(n) for n in c) for c in compositions(m, k))

def B_m_coeff_E3k_E1_rest(m, k):
    """[E3^k E1^{m-2k}] B_m = m!/k! * [T^m E1^{m-2k}] M^k."""
    return factorial(m) / factorial(k) * M_series_expand_pow(k, m)

def A_n_coeff_E1_E2(n, x2):
    """[E1^{n-x2} E2^{x2}] A_n."""
    if x2 < 0 or x2 > n: return sp.Integer(0)
    An = A_n(n)
    return sp.Poly(An, E1, E2).coeff_monomial((n - x2, x2))

# Check every coefficient of tops[b] for b = 2..7, decomposed as sum over (n,m)
# Also verify each individual term has the predicted sign
mismatches = 0
sample_shown = 0
for b in range(2, 8):
    # allowed monomials (x1, x2, x3) with x1 + x2 + 2 x3 = b
    for x3 in range(b//2 + 1):
        for x2 in range(b - 2*x3 + 1):
            x1 = b - x2 - 2*x3
            k = x3
            terms = []
            for n in range(x2, b - 2*k + 1):
                m = b - n
                cn = binomial(b, n) * A_n_coeff_E1_E2(n, x2) * B_m_coeff_E3k_E1_rest(m, k)
                if cn != 0:
                    terms.append((n, cn))
            total = sum(c for _, c in terms)
            expected_sign = (-1)**(b - x2 - x3)
            if total == 0:
                print(f"ZERO COEFF b={b} monomial ({x1},{x2},{x3}): total={total}")
                mismatches += 1
            actual_sign = 1 if total > 0 else -1
            if actual_sign != expected_sign:
                print(f"TOTAL SIGN MISMATCH b={b} ({x1},{x2},{x3}): total={total}")
                mismatches += 1
            # Check individual terms
            for n, cn in terms:
                asig = 1 if cn > 0 else -1
                if asig != expected_sign:
                    print(f"INDIV SIGN MISMATCH b={b} ({x1},{x2},{x3}) n={n}: contrib={cn}")
                    mismatches += 1
            if sample_shown < 8 and len(terms) > 1:
                print(f"b={b} monomial E1^{x1}E2^{x2}E3^{x3}: {len(terms)} contribs, total={total}, terms={terms}")
                sample_shown += 1

print(f"\nTotal mismatches: {mismatches}")
