"""Day 87 evening — Extract h_k^{(6)} and h_k^{(7)} via c-uniform template
inversion + M_j Sym-side. Reuse infrastructure from h4-fit-full.py.

Strategy: compute H_c(a, b, j) via the template inversion for many (a, b, j),
then invert the binomial triangle to get h_k(a, b), then polynomial-fit
h_k(a, b) as a function of (a, b).

At c=5 we know h_k^{(5)} from Clio; extract h_k^{(6)}, h_k^{(7)} the same way.
"""
from math import factorial
from fractions import Fraction
from sympy import symbols, Matrix, expand, factor, Poly

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


# Kostka tables K_{mu^T, (2^j)} for j up to 8 (rows-≤3)
# via computational form: e_2^j = sum K_{mu^T,(2^j)} s_mu.
# For rows ≤ 3, K_{mu^T,(2^j)} equals #SYT of shape mu with column-strict 2's.
# For j up to 6 we already have tables. Extend to 7, 8 via Pieri.

def build_e2_tables(max_j=8):
    """Build the coefficients of e_2^j in the Schur basis (rows ≤ 3),
    by iterative Pieri multiplication e_2 · s_μ."""
    # State: dict {partition tuple → integer coefficient}, only ≤ 3 rows.
    # Start with 1 (empty partition).
    # e_2 = s_{(1,1)}. Pieri for s_{(1,1)} on s_μ:
    #   s_{(1,1)} · s_μ = sum over vertical 2-strips μ→ν, i.e. add 2 boxes,
    #   at most one per row, in different rows.
    from collections import defaultdict
    def vert_2_strips(mu):
        # mu is a tuple sorted decreasing padded to some length.
        # Add exactly 2 boxes, at most one per row, so mu -> ν where
        # ν_i ∈ {μ_i, μ_i + 1} and exactly 2 are +1.
        L = len(mu) + 2  # allow adding to a new row
        base = list(mu) + [0] * (L - len(mu))
        results = []
        idxs = list(range(L))
        from itertools import combinations
        for pair in combinations(idxs, 2):
            new = base.copy()
            for i in pair:
                new[i] += 1
            # Check partition shape (weakly decreasing)
            ok = True
            for i in range(L - 1):
                if new[i] < new[i + 1]:
                    ok = False; break
            if not ok: continue
            # trim trailing zeros
            while new and new[-1] == 0:
                new.pop()
            # restrict to ≤ 3 rows
            if len(new) > 3:
                continue
            results.append(tuple(new))
        return results

    current = defaultdict(int)
    current[()] = 1
    tables = {0: [((0,0,0), 1)]}
    for j in range(1, max_j + 1):
        nxt = defaultdict(int)
        for mu, coef in current.items():
            for nu in vert_2_strips(mu):
                nxt[nu] += coef
        current = nxt
        # convert to list of ((mu padded to 3), coef)
        rows = []
        for mu, coef in sorted(current.items(), reverse=True):
            padded = tuple(list(mu) + [0] * (3 - len(mu)))
            rows.append((padded, coef))
        tables[j] = rows
    return tables


def M_j_sym(a, b, c, j, tables):
    """M_j = sum_{μ⊢2j, ≤3 rows} K_{μᵀ,(2^j)} · f^{λ/μ}"""
    lam = (a, b, c)
    if not (a >= b >= c >= 0):
        return 0
    if j == 0:
        return hook_length_lambda(lam)
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


def H_c_template(a, b, c, j, tables):
    """Clio Lemma-1 template inversion for H_c(a, b, j)."""
    N = a + b + c - 2*j
    if N < 0 or (b - j) < 0 or (b - j) > N:
        return None
    Mj = M_j_sym(a, b, c, j, tables)
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


def extract_h_k(a, b, c, jmax, tables):
    """Extract h_0..h_jmax by inverting the C(j, k) triangular matrix."""
    Hs = []
    for j in range(jmax + 1):
        h = H_c_template(a, b, c, j, tables)
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


def fit_polynomial_2var(samples, max_deg):
    a, b = symbols('a b')
    monomials = []
    for da in range(max_deg + 1):
        for db in range(max_deg + 1 - da):
            monomials.append(a**da * b**db)
    N = len(monomials)
    if len(samples) < N:
        return None
    A_rows = []
    yy = []
    for (av, bv, val) in samples:
        row = [int(m.subs({a: av, b: bv})) for m in monomials]
        A_rows.append(row)
        yy.append(val)
    A = Matrix(A_rows)
    y = Matrix(yy)
    aug = A.row_join(y)
    rref, pivots = aug.rref()
    if (aug.cols - 1) in pivots:
        return None
    if len(pivots) != N:
        return None
    sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
    poly = sum(sol[i] * monomials[i] for i in range(N))
    poly = expand(poly)
    for (av, bv, val) in samples:
        got = poly.subs({a: av, b: bv})
        if got != val:
            return None
    return poly


def fit_all_h_k(c_val, jmax, max_deg=10, sample_range=(4, 26)):
    print("=" * 60)
    print(f"Fit h_k^{{({c_val})}}(a, b) via extraction jmax={jmax}, degree<={max_deg}")
    print("=" * 60)
    tables = build_e2_tables(max_j=jmax)
    samples_by_k = {k: [] for k in range(jmax + 1)}
    for av in range(sample_range[0], sample_range[1]):
        for bv in range(sample_range[0], sample_range[1]):
            if bv > av:
                continue
            hks = extract_h_k(av, bv, c_val, jmax=jmax, tables=tables)
            if hks is None:
                continue
            for k in range(jmax + 1):
                samples_by_k[k].append((av, bv, hks[k]))
    print(f"  (total samples per k: {len(samples_by_k[0])})")

    result = {}
    for k in range(jmax + 1):
        n_samples = len(samples_by_k[k])
        print(f"\n  h_{k}^{{({c_val})}}(a, b): {n_samples} samples")
        found = False
        for deg in range(0, max_deg + 1):
            poly = fit_polynomial_2var(samples_by_k[k], deg)
            if poly is not None:
                fpoly = factor(poly)
                print(f"    fits total degree <= {deg}:")
                print(f"    h_{k} = {fpoly}")
                result[k] = (poly, fpoly)
                found = True
                break
        if not found:
            print(f"    NO FIT up to degree {max_deg}")
    return result


if __name__ == "__main__":
    print("\n### c = 6 ###\n")
    res6 = fit_all_h_k(c_val=6, jmax=10, max_deg=10)
    print("\n### c = 7 ###\n")
    res7 = fit_all_h_k(c_val=7, jmax=14, max_deg=13, sample_range=(7, 30))
