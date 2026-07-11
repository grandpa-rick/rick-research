"""Day 89 CODE — targeted Q_7(a, b, c) fit.

Q_6 succeeded in 2026-07-11-Qk-fit-extended.py at total degree 12 with
455 monomials. Q_7 failed there due to insufficient samples (only ~364
samples in the (7, 32) box). This script uses a much wider ab_range
and prints with flush=True so we can see live progress.

Empirically: normalized h_k has total degree ≤ 2k+2 (k=0: 0; k=6: 12;
k=7: 14 expected). Deg 14 needs C(15, 3) = 680 monomials.
"""
import json
import pickle
import sys
import time
from importlib import util

from sympy import Matrix, Rational, expand, factor, symbols

# Force unbuffered stdout
print = lambda *a, **kw: sys.stdout.write(" ".join(str(x) for x in a) + kw.get("end", "\n")) or sys.stdout.flush()

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
        print(f"    c={c_val}: {cnt} samples (running total {len(samples)}, {time.time()-t0:.1f}s)")
    return samples, per_c


def fit_at_degree(samples, deg):
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
        row = [av ** da * bv ** db * cv ** dc for (da, db, dc) in monomials]
        A_rows.append(row)
        yy.append(val)
    print(f"    Built matrix in {time.time()-t0:.1f}s. Running rref...")
    t1 = time.time()
    A = Matrix(A_rows)
    y = Matrix(yy)
    aug = A.row_join(y)
    rref, pivots = aug.rref()
    print(f"    rref done in {time.time()-t1:.1f}s. pivots = {len(pivots)}, aug cols = {aug.cols}.")
    if (aug.cols - 1) in pivots:
        print("    INCONSISTENT (last col is pivot).")
        return None
    if len(pivots) != N:
        print(f"    UNDERDETERMINED (rank {len(pivots)} < {N}).")
        return None
    sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
    for s in sol:
        if not isinstance(s, Rational) or s.q != 1:
            print(f"    NON-INTEGER coefs (found {s}); shape mismatch.")
            return None
    poly = 0
    for (da, db, dc), coef in zip(monomials, sol):
        poly += int(coef) * a ** da * b ** db * c ** dc
    poly = expand(poly)
    print(f"    Verifying {len(samples)} samples...")
    for (av, bv, cv, val) in samples:
        if poly.subs({a: av, b: bv, c: cv}) != val:
            print(f"    VERIFY FAIL at (a,b,c)=({av},{bv},{cv})")
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
    for a_val in range(0, 25):
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
    print("Day 89 CODE — targeted Q_7(a, b, c) fit")
    print("=" * 76)

    # ~840 samples target for deg 14 (680 monomials).
    # Choose c_vals so that (a, b) box has enough pairs per c.
    # For c=15, need b in [15, ab_max], a in [15, ab_max]. If ab_max=45,
    # pairs = 31*30/2 + 31 ~ 500. Then across 8 c-values, we get ~4000 samples.

    c_vals = tuple(range(7, 20))
    ab_range = (7, 45)
    k_target = 7

    samples, per_c = collect_samples(k_target, c_vals, ab_range)
    # Truncate to speed up rref — 1200 rows is plenty for a 969-monomial fit
    # (deg 16), still overdetermined by ~25%.
    max_samples = 1200
    if len(samples) > max_samples:
        # Sample uniformly at random for representativeness
        import random
        random.seed(20260711)
        samples = random.sample(samples, max_samples)
    print(f"  Total samples (post-cap): {len(samples)}")

    poly = None
    for deg in [13, 14, 15, 16]:
        poly = fit_at_degree(samples, deg)
        if poly is not None:
            print(f"  ✓ Q_{k_target} fits at total degree ≤ {deg}")
            print(f"    Q_{k_target}(a, b, c) = {factor(poly)}")
            break

    if poly is None:
        print(f"  ↳ Q_{k_target}: NO FIT within deg <= 16.")
        return

    ok, fail = cross_validate_c8(k_target, poly)
    print(f"  CV: {ok} pass, {fail} fail")

    # Update the JSON catalog.
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    cat["Q_k_extended"][str(k_target)] = {
        "poly_expanded": str(poly),
        "poly_factored": str(factor(poly)),
        "total_degree": deg,
        "num_samples": len(samples),
        "cv_c8_pass": (fail == 0),
    }
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json", "w") as f:
        json.dump(cat, f, indent=2)
    print(f"  Wrote updated 2026-07-11-Qk-catalog.json")


if __name__ == "__main__":
    main()
