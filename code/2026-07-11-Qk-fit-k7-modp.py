"""Day 89 CODE — Q_7(a, b, c) fit via mod-p Vandermonde solve.

Sympy's rref over rationals is very slow at 1200x561. Instead:
  1. Solve the Vandermonde system mod a large prime p using numpy int64.
  2. If the resulting integer polynomial verifies EXACTLY at all
     over-determining samples, accept.

If the true coefficients are integers and |coefs| < p/2, mod-p solve
recovers them exactly (via signed representative). We pick p ~ 10^9
prime, and monomials of degree ≤ 14 at (a, b, c) ~ 20 have values up
to 20^14 = 1.6e18, which overflows int64. So use uint64 with careful
mod ops, or use Python's arbitrary-precision int with a smaller prime.

Approach: use Python-level modular arithmetic (arbitrary-precision int
% p) with p ~ 10^18. This is slow-ish but fast enough. Verify samples
independently using Python arbitrary-precision.
"""
import json
import pickle
import random
import sys
import time
from importlib import util

from sympy import factor, symbols, expand

sys.stdout.reconfigure(line_buffering=True)

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables


a, b, c = symbols('a b c')


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def collect_samples(k_target, c_vals, ab_range):
    print(f"  Collecting samples for k={k_target}, c_vals={c_vals}, ab_range={ab_range}...")
    tables = build_e2_tables(max_j=k_target + 2)
    samples = []
    per_c = {}
    t0 = time.time()
    for c_val in c_vals:
        n_norm = c_val - 1 - k_target
        if n_norm < 0:
            continue
        cnt = 0
        for a_val in range(ab_range[0], ab_range[1]):
            for b_val in range(ab_range[0], min(a_val, ab_range[1]) + 1):
                if b_val < c_val:
                    continue
                hks = extract_h_k(a_val, b_val, c_val, k_target, tables)
                if hks is None or len(hks) <= k_target:
                    continue
                y = hks[k_target]
                denom = rising_fact(a_val + 3, n_norm) * rising_fact(b_val + 2, n_norm)
                if denom == 0 or y % denom != 0:
                    continue
                samples.append((a_val, b_val, c_val, y // denom))
                cnt += 1
        per_c[c_val] = cnt
        print(f"    c={c_val}: {cnt} samples (total {len(samples)}, {time.time()-t0:.1f}s)")
    return samples, per_c


def gaussian_elim_modp(A_rows, rhs, p):
    """In-place Gaussian elimination on augmented matrix mod p.
    A_rows: list of lists of ints, dim M x N.
    rhs: list of ints, dim M.
    Returns solution vector length N if uniquely determined,
    or None if underdetermined or inconsistent.
    """
    M = len(A_rows)
    N = len(A_rows[0])
    # Build augmented matrix as list of lists
    aug = [row[:] + [rhs[i]] for i, row in enumerate(A_rows)]

    row = 0
    pivot_cols = []
    for col in range(N):
        # Find pivot in column
        piv = -1
        for r in range(row, M):
            if aug[r][col] % p != 0:
                piv = r
                break
        if piv == -1:
            continue  # no pivot in this column
        # Swap
        if piv != row:
            aug[row], aug[piv] = aug[piv], aug[row]
        # Normalize
        inv = pow(aug[row][col], -1, p)
        for j in range(col, N + 1):
            aug[row][j] = (aug[row][j] * inv) % p
        # Eliminate
        for r in range(M):
            if r != row and aug[r][col] % p != 0:
                factor_ = aug[r][col]
                for j in range(col, N + 1):
                    aug[r][j] = (aug[r][j] - factor_ * aug[row][j]) % p
        pivot_cols.append(col)
        row += 1
        if row == M:
            break

    # Check
    if len(pivot_cols) != N:
        return None  # underdetermined
    # Check consistency: all rows past 'row' must be zero
    for r in range(row, M):
        if aug[r][N] % p != 0:
            return None
    # Extract solution
    sol = [0] * N
    for i, col in enumerate(pivot_cols):
        sol[col] = aug[i][N]
    return sol


def signed_mod(x, p):
    """Return signed representative in (-p/2, p/2]."""
    x = x % p
    if x > p // 2:
        x -= p
    return x


def fit_at_degree(samples, deg, p):
    print(f"  Trying total degree ≤ {deg}...")
    t0 = time.time()
    monomials = []
    for da in range(deg + 1):
        for db in range(deg + 1 - da):
            for dc in range(deg + 1 - da - db):
                monomials.append((da, db, dc))
    N = len(monomials)
    print(f"    #monomials = {N}, #samples = {len(samples)}")
    if len(samples) < N:
        print(f"    UNDERDETERMINED: {len(samples)} < {N}")
        return None
    A_rows = []
    yy = []
    for (av, bv, cv, val) in samples:
        row = [(av ** da * bv ** db * cv ** dc) % p for (da, db, dc) in monomials]
        A_rows.append(row)
        yy.append(val % p)
    print(f"    Built matrix in {time.time()-t0:.1f}s. Solving mod {p}...")
    t1 = time.time()
    sol_mod = gaussian_elim_modp(A_rows, yy, p)
    print(f"    Gaussian elim done in {time.time()-t1:.1f}s.")
    if sol_mod is None:
        print(f"    Under-determined or inconsistent mod {p}.")
        return None
    # Signed rep
    sol = [signed_mod(s, p) for s in sol_mod]
    # Build the polynomial
    poly = 0
    for (da, db, dc), coef in zip(monomials, sol):
        if coef != 0:
            poly += coef * a ** da * b ** db * c ** dc
    poly = expand(poly)
    print(f"    Verifying {len(samples)} samples with Python arbitrary-precision int...")
    for (av, bv, cv, val) in samples:
        got = poly.subs({a: av, b: bv, c: cv})
        if got != val:
            print(f"    VERIFY FAIL at (a,b,c)=({av},{bv},{cv}): got {got}, expect {val}")
            return None
    print(f"    ✓ Fit accepted (total {time.time()-t0:.1f}s).")
    return poly


def cross_validate_c8(k_target, poly):
    with open("/home/agent/projects/code/2026-07-11-c8-hk-fits.pkl", "rb") as f:
        h_c8_str = pickle.load(f)
    from sympy import sympify
    h_c8_k = sympify(h_c8_str[k_target])
    n_norm = 8 - 1 - k_target
    ok = fail = 0
    a_s = symbols('a')
    b_s = symbols('b')
    for a_val in range(0, 30):
        for b_val in range(0, a_val + 1):
            denom = rising_fact(a_val + 3, n_norm) * rising_fact(b_val + 2, n_norm)
            if denom == 0:
                continue
            hk_val = int(h_c8_k.subs({a_s: a_val, b_s: b_val}))
            if hk_val % denom != 0:
                continue
            Q_actual = hk_val // denom
            Q_pred = int(poly.subs({a: a_val, b: b_val, c: 8}))
            if Q_actual == Q_pred:
                ok += 1
            else:
                fail += 1
                if fail <= 3:
                    print(f"    CV FAIL k={k_target} at (a,b)=({a_val},{b_val}): pred={Q_pred} actual={Q_actual}")
    print(f"    Cross-val vs c=8 fits: {ok} match, {fail} fail")
    return ok, fail


def main():
    print("=" * 76)
    print("Day 89 CODE — Q_7(a, b, c) fit via mod-p Vandermonde")
    print("=" * 76)

    c_vals = tuple(range(7, 20))
    ab_range = (7, 45)
    k_target = 7

    samples, per_c = collect_samples(k_target, c_vals, ab_range)
    max_samples = 1000
    if len(samples) > max_samples:
        random.seed(20260711)
        samples = random.sample(samples, max_samples)
    print(f"  Post-cap samples: {len(samples)}")

    # Large prime for mod solve. Coefficients of Q_k likely fit in |c| < 10^18.
    p = (1 << 61) - 1  # Mersenne prime 2^61 - 1 = 2305843009213693951

    poly = None
    for deg in [13, 14, 15, 16]:
        poly = fit_at_degree(samples, deg, p)
        if poly is not None:
            print(f"  ✓ Q_{k_target} fits at total degree ≤ {deg}")
            print(f"    Q_{k_target}(a, b, c) = {factor(poly)}")
            break

    if poly is None:
        print(f"  ↳ Q_{k_target}: NO FIT within deg ≤ 16.")
        return

    ok, fail = cross_validate_c8(k_target, poly)
    print(f"  CV: {ok} pass, {fail} fail")

    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    cat["Q_k_extended"][str(k_target)] = {
        "poly_expanded": str(poly),
        "poly_factored": str(factor(poly)),
        "total_degree": deg,
        "num_samples": len(samples),
        "cv_c8_pass": (fail == 0),
        "method": "mod-p Vandermonde (Mersenne p = 2^61 - 1) + full-precision verify",
    }
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json", "w") as f:
        json.dump(cat, f, indent=2)
    print(f"  Wrote updated Qk-catalog.json")


if __name__ == "__main__":
    main()
