"""Day 87 - Full polynomial fit for all h_k^{(4)}(a, b) coefficients including h_6.
"""
from math import factorial
from fractions import Fraction
from sympy import symbols, Matrix, expand, factor


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
        6: [((6,6,0),1), ((6,5,1),5), ((6,4,2),9), ((5,5,2),10), ((6,3,3),5),
            ((5,4,3),16), ((4,4,4),5)],
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
    """Extract h_0..h_jmax by inverting the C(j, k) triangular matrix."""
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


# Solve polynomial fit exactly, with rank check
def fit_polynomial_2var(samples, max_deg):
    from sympy import symbols, Matrix
    a, b = symbols('a b')
    monomials = []
    for da in range(max_deg + 1):
        for db in range(max_deg + 1 - da):
            monomials.append(a**da * b**db)
    N = len(monomials)
    if len(samples) < N:
        return None
    # Build big rectangular system
    A_rows = []
    yy = []
    for (av, bv, val) in samples:
        row = [int(m.subs({a: av, b: bv})) for m in monomials]
        A_rows.append(row)
        yy.append(val)
    A = Matrix(A_rows)
    y = Matrix(yy)
    # Solve using nullspace approach — find x with Ax = y or fail
    # Combine A and y, row reduce
    aug = A.row_join(y)
    rref, pivots = aug.rref()
    # If a pivot lies in the last column, no solution
    if (aug.cols - 1) in pivots:
        return None
    # If not enough pivots to determine all coefficients uniquely, could be
    # multiple solutions — but for polynomial extraction we expect unique fit.
    if len(pivots) != N:
        return None
    # Read off solution
    sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
    poly = sum(sol[i] * monomials[i] for i in range(N))
    poly = expand(poly)
    for (av, bv, val) in samples:
        got = poly.subs({a: av, b: bv})
        if got != val:
            return None
    return poly


def fit_all_h_k_c4(max_deg=8, jmax=6):
    print("=" * 60)
    print(f"Fit h_k^{{(4)}}(a, b) via extraction jmax={jmax}, degree<={max_deg}")
    print("=" * 60)
    from sympy import symbols
    a, b = symbols('a b')

    # Collect samples: (a, b) with a+b even and full extraction succeeds
    samples_by_k = {k: [] for k in range(jmax + 1)}
    for av in range(4, 26):
        for bv in range(4, av + 1):
            if (av + bv) % 2 != 0:
                continue
            hks = extract_h_k(av, bv, 4, jmax=jmax)
            if hks is None:
                continue
            for k in range(jmax + 1):
                samples_by_k[k].append((av, bv, hks[k]))

    for k in range(jmax + 1):
        n_samples = len(samples_by_k[k])
        print(f"\n  h_{k}^{{(4)}}(a, b): {n_samples} samples")
        for deg in range(0, max_deg + 1):
            poly = fit_polynomial_2var(samples_by_k[k], deg)
            if poly is not None:
                fpoly = factor(poly)
                print(f"    fits total degree <= {deg}:")
                print(f"    h_{k} = {fpoly}")
                break
        else:
            print(f"    NO FIT up to degree {max_deg}")


if __name__ == "__main__":
    fit_all_h_k_c4()
