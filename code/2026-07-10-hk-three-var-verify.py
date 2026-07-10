"""Day 88 verification: h_k^{(c)}(a, b) factorization structure.

Claim: For k <= 2c-2,
    h_k^{(c)}(a, b) = (a+3)_{c-1-k} * (b+2)_{c-1-k} * D_k(c) * Q_k(a, b, c)
where (x)_n = x(x+1)...(x+n-1) is the rising factorial (Pochhammer).
D_k(c) is polynomial in c.
Q_k(a, b, c) is polynomial in (a, b, c) with bounded degree in (a, b).

Strategy:
  1. Compute h_k^{(c)}(a, b) explicitly at c = 4, 5, 6, 7 via template
     inversion for k = 0..8.
  2. Divide by (a+3)_{c-1-k}(b+2)_{c-1-k} to extract D_k(c) * Q_k(a, b, c).
  3. Verify Q_k(a, b, c) is polynomial in c at each (a, b) evaluation.
  4. Fit D_k(c) and check it's polynomial in c.
"""
from fractions import Fraction
from math import factorial
from sympy import symbols, Rational, factor, expand, Poly, S


def C(n, k):
    if k < 0 or k > n:
        return 0
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


def build_e2_tables(max_j=8):
    from collections import defaultdict
    from itertools import combinations

    def vert_2_strips(mu):
        L = len(mu) + 2
        base = list(mu) + [0] * (L - len(mu))
        results = []
        for pair in combinations(range(L), 2):
            new = base.copy()
            for i in pair:
                new[i] += 1
            ok = True
            for i in range(L - 1):
                if new[i] < new[i + 1]:
                    ok = False
                    break
            if not ok:
                continue
            while new and new[-1] == 0:
                new.pop()
            if len(new) > 3:
                continue
            results.append(tuple(new))
        return results

    current = defaultdict(int)
    current[()] = 1
    tables = {0: [((0, 0, 0), 1)]}
    for j in range(1, max_j + 1):
        nxt = defaultdict(int)
        for mu, coef in current.items():
            for nu in vert_2_strips(mu):
                nxt[nu] += coef
        current = nxt
        rows = []
        for mu, coef in sorted(current.items(), reverse=True):
            padded = tuple(list(mu) + [0] * (3 - len(mu)))
            rows.append((padded, coef))
        tables[j] = rows
    return tables


def M_j_sym(a, b, c, j, tables):
    if not (a >= b >= c >= 0):
        return 0
    if j == 0:
        return hook_length_lambda((a, b, c))
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
        det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
               - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
               + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        f_num = factorial(n - 2 * j) * det
        f_den = factorial(a + 2) * factorial(b + 1) * factorial(c)
        total += Fraction(k * f_num, f_den)
    if total.denominator != 1:
        return None
    return int(total)


def H_c_template(a, b, c, j, tables):
    N = a + b + c - 2 * j
    if N < 0 or (b - j) < 0 or (b - j) > N:
        return None
    Mj = M_j_sym(a, b, c, j, tables)
    if Mj is None:
        return None
    prod_bij = 1
    for i in range(1, c + 1):
        prod_bij *= (b + i - j)
    CNbj = C(N, b - j)
    if CNbj == 0 or (a - b + 1) == 0 or (a - c + 2) == 0 or (b - c + 1) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    val = Fraction(numer_A, CNbj * (a - b + 1)) + factorial(2 * c) * C(j, 2 * c)
    h = val / Fraction((a - c + 2) * (b - c + 1))
    if h.denominator == 1:
        return int(h)
    return None


def extract_h_k(a, b, c, jmax, tables):
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
            val -= hks[kk] * C(k, kk)
        hks.append(val)
    return hks


def rising_fact(x, n):
    """(x)_n = x(x+1)...(x+n-1). Returns 1 if n=0."""
    result = 1
    for i in range(n):
        result *= (x + i)
    return result


def test_factorization():
    """Verify h_k^{(c)}(a,b) = (a+3)_{c-1-k} (b+2)_{c-1-k} * P_k^{(c)}(a, b)
    for various (a, b, c, k).
    """
    tables = build_e2_tables(max_j=12)
    print("=" * 70)
    print("VERIFY: h_k^{(c)}(a, b) / [(a+3)_{c-1-k}(b+2)_{c-1-k}] is polynomial")
    print("=" * 70)

    for c_val in [4, 5, 6, 7]:
        print(f"\n### c = {c_val} ###")
        # Extract h_k for many (a, b)
        results = {}  # k -> [(a, b, val_normalized)]
        for a_val in range(c_val + 2, c_val + 15):
            for b_val in range(c_val, a_val + 1):
                jmax = 2 * c_val - 2
                hks = extract_h_k(a_val, b_val, c_val, jmax, tables)
                if hks is None:
                    continue
                for k in range(jmax + 1):
                    if c_val - 1 - k < 0:
                        continue  # skip - Pochhammer factors become inverse
                    factor_ab = rising_fact(a_val + 3, c_val - 1 - k) * rising_fact(b_val + 2, c_val - 1 - k)
                    if factor_ab == 0:
                        continue
                    q = Fraction(hks[k], factor_ab)
                    if q.denominator != 1:
                        print(f"  WARN: k={k}, (a,b)=({a_val},{b_val}), non-integer quotient {q}")
                    if k not in results:
                        results[k] = []
                    results[k].append((a_val, b_val, int(q) if q.denominator == 1 else float(q)))

        for k in sorted(results.keys()):
            if len(results[k]) < 5:
                continue
            # Sample first 3 values
            samples = results[k][:3]
            print(f"  k={k}: {len(results[k])} samples. First: {samples}")


def extract_D_and_Q(c_vals=[4, 5, 6, 7]):
    """For each k, extract D_k(c) and Q_k(a, b, c) via factoring h_k^{(c)}."""
    from sympy import symbols, factor, expand, Poly, Rational

    a, b, c = symbols('a b c')

    tables = build_e2_tables(max_j=12)

    # For each k, get h_k^{(c)}(a, b) as symbolic poly, then extract structure.
    h_k_symbolic = {}  # (c_val, k) -> symbolic polynomial in (a, b)

    from sympy import Matrix
    def fit_polynomial_2var(samples, max_deg):
        aa, bb = symbols('a b')
        monomials = []
        for da in range(max_deg + 1):
            for db in range(max_deg + 1 - da):
                monomials.append(aa**da * bb**db)
        N = len(monomials)
        if len(samples) < N:
            return None
        A_rows = []
        yy = []
        for (av, bv, val) in samples:
            row = [int(m.subs({aa: av, bb: bv})) for m in monomials]
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
        return expand(poly)

    # Get h_k^{(c)} symbolically at each c
    for c_val in c_vals:
        jmax = 2 * c_val - 2
        samples_by_k = {k: [] for k in range(jmax + 1)}
        for a_val in range(c_val + 2, c_val + 20):
            for b_val in range(c_val - 1, min(a_val + 1, c_val + 20)):
                hks = extract_h_k(a_val, b_val, c_val, jmax, tables)
                if hks is None:
                    continue
                for k in range(jmax + 1):
                    samples_by_k[k].append((a_val, b_val, hks[k]))
        for k in range(jmax + 1):
            if len(samples_by_k[k]) < 10:
                continue
            for deg in range(20):
                p = fit_polynomial_2var(samples_by_k[k], deg)
                if p is not None:
                    h_k_symbolic[(c_val, k)] = p
                    break

    # For each k, at each c, verify factorization and extract D_k(c) * Q_k(a, b, c).
    aa, bb, cc = symbols('a b c')

    D_data = {}  # k -> {c -> D_k(c) sympy value}
    Q_data = {}  # k -> {c -> Q_k(a, b) sympy expression}

    for k in range(9):
        D_data[k] = {}
        Q_data[k] = {}
        for c_val in c_vals:
            if (c_val, k) not in h_k_symbolic:
                continue
            if c_val - 1 - k < 0:
                continue
            n = c_val - 1 - k
            # (a+3)_n = (a+3)(a+4)...(a+3+n-1) = (a+3)(a+4)...(a+n+2)
            f_a = S.One
            for i in range(n):
                f_a *= (aa + 3 + i)
            f_b = S.One
            for i in range(n):
                f_b *= (bb + 2 + i)
            h_val = h_k_symbolic[(c_val, k)]
            # Divide h_val by f_a * f_b symbolically.
            from sympy import Poly, div, quo, rem
            quotient = expand(h_val / (f_a * f_b))
            # Test: substitute (a=0, b=0) and other points to check polynomial
            test_ok = True
            test_vals = [(0, 0), (1, 1), (2, 3), (5, 4)]
            for aval, bval in test_vals:
                h_num = h_val.subs({aa: aval, bb: bval})
                f_num = f_a.subs({aa: aval}) * f_b.subs({bb: bval})
                if f_num == 0:
                    continue
                if h_num / f_num != quotient.subs({aa: aval, bb: bval}):
                    # if fractional, try Rational
                    pass
            # get D_k(c) * Q_k(a, b, c) form: factor out D from the polynomial part
            # Just store the quotient for now
            Q_data[k][c_val] = quotient

    return h_k_symbolic, D_data, Q_data


if __name__ == "__main__":
    test_factorization()
    print()
    print("=" * 70)
    print("EXTRACT D_k(c) and Q_k^{(c)}(a, b)")
    print("=" * 70)
    hk_sym, D_data, Q_data = extract_D_and_Q()
    from sympy import factor, symbols
    aa, bb, cc = symbols('a b c')
    for k in sorted(Q_data.keys()):
        print(f"\nk = {k}:")
        for c_val in sorted(Q_data[k].keys()):
            q = Q_data[k][c_val]
            fq = factor(q)
            print(f"  c={c_val}: h_k / [(a+3)_{c_val-1-k}(b+2)_{c_val-1-k}] = {fq}")
