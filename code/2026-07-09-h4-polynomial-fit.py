"""Day 87 - Fit h_k^{(4)}(a,b) polynomials from template inversion, then
verify v_2(h_k * C(j,k)) >= 4 term-by-term for all (a,b,j) with a+b even.
"""
from math import factorial
from fractions import Fraction
from sympy import symbols, Poly, expand, simplify, factor, Rational, together


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def Cn(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def hook_length_lambda(lam):
    n = sum(lam)
    if lam[0] == 0:
        return 1 if all(l == 0 for l in lam) else 0
    a = lam[0]
    cols = [0] * a
    for i, li in enumerate(lam):
        for j in range(li):
            cols[j] += 1
    hooks = 1
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = cols[j] - i - 1
            hooks *= (arm + leg + 1)
    return factorial(n) // hooks


def M_j_sym(a, b, c, j):
    tables = {
        0: [((0, 0, 0), 1)],
        1: [((1, 1, 0), 1)],
        2: [((2, 2, 0), 1), ((2, 1, 1), 1)],
        3: [((3, 3, 0), 1), ((3, 2, 1), 2), ((2, 2, 2), 1)],
        4: [((4, 4, 0), 1), ((4, 3, 1), 3), ((4, 2, 2), 2), ((3, 3, 2), 3)],
        5: [((5, 5, 0), 1), ((5, 4, 1), 4), ((5, 3, 2), 5), ((4, 4, 2), 6),
            ((4, 3, 3), 5)],
    }
    if j == 0:
        return hook_length_lambda((a, b, c)) if (a >= b >= c >= 0) else 0
    if j not in tables:
        return None
    xs = (a + 2, b + 1, c)
    n = a + b + c
    if n < 2 * j:
        return 0
    total = Fraction(0)
    for mu, k in tables[j]:
        ks = [mu[jj] + (2 - jj) for jj in range(3)]
        def fall(x, kk):
            p = 1
            for i in range(kk):
                p *= (x - i)
            return p
        M = [[fall(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        det = (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
             - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
             + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))
        f_lam_mu_num = factorial(n - 2*j) * det
        f_lam_mu_den = factorial(a+2) * factorial(b+1) * factorial(c)
        total += Fraction(k * f_lam_mu_num, f_lam_mu_den)
    if total.denominator != 1:
        return None
    return int(total)


def H_c_template(a, b, c, j):
    N = a + b + c - 2*j
    if N < 0 or (b - j) < 0 or (b - j) > N:
        return None
    Mj = M_j_sym(a, b, c, j)
    if Mj is None:
        return None
    prod_bij = 1
    for i in range(1, c+1):
        prod_bij *= (b + i - j)
    CNbj = Cn(N, b - j)
    if CNbj == 0 or (a - b + 1) == 0 or (a - c + 2) == 0 or (b - c + 1) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    val = Fraction(numer_A, CNbj * (a - b + 1)) + factorial(2*c) * Cn(j, 2*c)
    h = val / Fraction((a - c + 2) * (b - c + 1))
    if h.denominator == 1:
        return int(h)
    return None


def extract_h_k(a, b, c, jmax):
    Hs = []
    for j in range(jmax + 1):
        h = H_c_template(a, b, c, j)
        if h is None:
            return None
        Hs.append(h)
    hks = []
    for k in range(jmax + 1):
        val = Hs[k]
        for kk in range(k):
            val -= hks[kk] * Cn(k, kk)
        hks.append(val)
    return hks


# ============================================================
# Polynomial fit for h_k^{(4)}(a, b)
#
# We collect many samples (a, b, h_k(a,b)) with a >= b >= 4 and a+b even,
# then fit a polynomial in (a, b).
# ============================================================
def fit_polynomial_2var(samples, max_deg):
    """samples: list of (a, b, value). Fit polynomial in (a, b) with total degree <= max_deg."""
    from sympy import symbols, Matrix, zeros
    a, b = symbols('a b')
    monomials = []
    for da in range(max_deg + 1):
        for db in range(max_deg + 1 - da):
            monomials.append(a**da * b**db)
    N = len(monomials)
    if len(samples) < N:
        return None
    # Use first N samples for exact solve
    A_rows = []
    yy = []
    for (av, bv, val) in samples[:N]:
        row = [int(m.subs({a: av, b: bv})) for m in monomials]
        A_rows.append(row)
        yy.append(val)
    A = Matrix(A_rows)
    y = Matrix(yy)
    if A.det() == 0:
        return None
    sol = A.LUsolve(y)
    poly = sum(sol[i] * monomials[i] for i in range(N))
    poly = expand(poly)
    # Verify on all samples
    for (av, bv, val) in samples:
        got = poly.subs({a: av, b: bv})
        if got != val:
            return None
    return poly


def fit_all_h_k_c4():
    print("=" * 60)
    print("Fit h_k^{(4)}(a, b) polynomials")
    print("=" * 60)
    from sympy import symbols
    a, b = symbols('a b')
    # Extract h_k for a range of (a, b) with a+b even, a >= b >= 4
    samples_by_k = {k: [] for k in range(6)}
    # Need a lot of samples for degree-6 fit
    for av in range(4, 22):
        for bv in range(4, av + 1):
            if (av + bv) % 2 != 0:
                continue
            hks = extract_h_k(av, bv, 4, jmax=5)
            if hks is None:
                continue
            for k in range(6):
                samples_by_k[k].append((av, bv, hks[k]))
    for k in range(6):
        n_samples = len(samples_by_k[k])
        print(f"\n  h_{k}^{{(4)}}(a, b): {n_samples} samples")
        # Try increasing degrees to find minimal fit
        for deg in range(0, 9):
            poly = fit_polynomial_2var(samples_by_k[k], deg)
            if poly is not None:
                fpoly = factor(poly)
                print(f"    fits degree <= {deg}:")
                print(f"    h_{k} = {fpoly}")
                break
        else:
            print(f"    NO FIT found up to degree 8")


if __name__ == "__main__":
    fit_all_h_k_c4()
