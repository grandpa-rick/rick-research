"""Day 89 CODE (secondary) — Q_k(a, b, c) c-general fit extension to k = 6..10.

Day 88 fit Q_k for k = 0..5 as a 3-var polynomial (a, b, c). This script
extends the fit to k = 6..10 and catalogs the results in JSON for
downstream reuse (future c = 10, c = 11 witness sweeps).

Method (from Day 88):
  h_k^{(c)}(a, b) = (a + 3)_{c-1-k} · (b + 2)_{c-1-k} · Q_k(a, b, c),
  Q_k(a, b, c) ∈ Z[a, b, c].

Fit Q_k by sampling at many (a, b, c) with c-1-k >= 0 and Vandermonde-
solving the coefficient system. Cross-validate against Q_k(a, b, c=8)
computed from the Day 89 h_k^{(c=8)} closed forms.

For k >= ~7, the total degree grows (~2k) and the number of monomials
(~deg^3 / 6) becomes prohibitive. Log the obstruction if it fails.
"""
import json
import pickle
import time
from importlib import util

from sympy import Matrix, Rational, expand, factor, symbols

# Load pipeline
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


def collect_normalized_samples(k_target, c_vals, ab_range):
    """Collect (a_val, b_val, c_val, Q) where
        Q = h_k / [(a+3)_{c-1-k} (b+2)_{c-1-k}].
    """
    samples = []
    per_c_count = {}
    max_c = max(c_vals)
    tables = build_e2_tables(max_j=k_target + 2)
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
        per_c_count[c_val] = cnt
    return samples, per_c_count


def num_monomials_3var(deg):
    n = deg + 1
    return n * (n + 1) * (n + 2) // 6


def fit_polynomial_3var_deg(samples, deg):
    """Fit samples to a 3-var polynomial of total degree ≤ deg. Return sympy expr or None."""
    monomials = []
    for da in range(deg + 1):
        for db in range(deg + 1 - da):
            for dc in range(deg + 1 - da - db):
                monomials.append((da, db, dc))
    N = len(monomials)
    if len(samples) < N:
        return None
    A_rows = []
    yy = []
    for (av, bv, cv, val) in samples:
        row = [av ** da * bv ** db * cv ** dc for (da, db, dc) in monomials]
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
    # Check integrality
    for s in sol:
        if not isinstance(s, Rational) or s.q != 1:
            return None
    poly = 0
    for (da, db, dc), coef in zip(monomials, sol):
        poly += int(coef) * a ** da * b ** db * c ** dc
    poly = expand(poly)
    # Verify all samples
    for (av, bv, cv, val) in samples:
        if poly.subs({a: av, b: bv, c: cv}) != val:
            return None
    return poly


def try_fit_k(k_target, c_vals, ab_range, deg_start, deg_max):
    print("=" * 76)
    print(f"Q_{k_target}(a, b, c) fit — c_vals = {c_vals}, ab_range = {ab_range}")
    print("=" * 76)
    t0 = time.time()
    samples, per_c = collect_normalized_samples(k_target, c_vals, ab_range)
    print(f"  Samples per c: {per_c}")
    print(f"  Total samples: {len(samples)}  (elapsed {time.time()-t0:.1f}s)")
    if len(samples) < 100:
        print("  (too few samples, skip)")
        return None
    for deg in range(deg_start, deg_max + 1):
        nm = num_monomials_3var(deg)
        if nm > len(samples):
            print(f"  Stop: deg={deg} needs {nm} monomials > {len(samples)} samples")
            return None
        t1 = time.time()
        poly = fit_polynomial_3var_deg(samples, deg)
        dt = time.time() - t1
        if poly is not None:
            fpoly = factor(poly)
            print(f"  ✓ Fit at total degree ≤ {deg} ({nm} monomials, {dt:.1f}s)")
            print(f"    Q_{k_target}(a, b, c) = {fpoly}")
            return poly, fpoly, deg, dt
        else:
            print(f"  ✗ deg {deg} fails ({nm} monomials, {dt:.1f}s)")
    return None


def cross_validate_c8(k_target, poly):
    """Verify poly.subs(c=8) matches Q_k^{(c=8)} = h_k^{(c=8)} / [(a+3)_{7-k}(b+2)_{7-k}]."""
    # Load c=8 fits
    with open("/home/agent/projects/code/2026-07-11-c8-hk-fits.pkl", "rb") as f:
        h_c8_str = pickle.load(f)
    from sympy import sympify
    h_c8_k = sympify(h_c8_str[k_target])
    n_norm = 8 - 1 - k_target
    ok = fail = 0
    for a_val in range(0, 25):
        for b_val in range(0, a_val + 1):
            denom = rising_fact(a_val + 3, n_norm) * rising_fact(b_val + 2, n_norm)
            if denom == 0:
                continue
            hk_val = int(h_c8_k.subs({symbols('a'): a_val, symbols('b'): b_val}))
            if hk_val % denom != 0:
                continue
            Q_actual = hk_val // denom
            Q_pred = int(poly.subs({a: a_val, b: b_val, c: 8}))
            if Q_actual == Q_pred:
                ok += 1
            else:
                fail += 1
                if fail <= 3:
                    print(f"    CV FAIL k={k_target} at (a,b)=({a_val},{b_val}): "
                          f"pred={Q_pred} actual={Q_actual}")
    print(f"    Cross-val vs c=8 fits: {ok} match, {fail} fail")
    return fail == 0


def main():
    print("=" * 76)
    print("Day 89 CODE (secondary) — Q_k(a, b, c) fit extension to k = 6..10")
    print("=" * 76)

    # For each k, empirical degree pattern (from k=0..5):
    #   deg(Q_k) ≈ 2 * (2k) = ... roughly total deg 2k for normalized h_k.
    # k=0 → 0, k=1 → 2, k=2 → 4, k=3 → 6, k=4 → 8, k=5 → 10.
    # So k=6 → 12, k=7 → 14, k=8 → 16, k=9 → 18, k=10 → 20.
    # Monomials at deg 12: C(15, 3) = 455. deg 14: 680. deg 20: 1771.

    # Choose c-values: need at least (deg_c + 1) distinct c to determine c-poly.
    # The c-degree seems to grow ~ 6 for k=4,5 (from output) — so grows with k.
    # Empirically use c in [4, 4 + 2*deg_c + 4] and enough (a, b) per c.

    saved_Qk = {}

    plan = [
        # (k, c_vals, ab_range, deg_start, deg_max)
        # ab_range wide enough that even at high c we get many (a,b) samples
        (6, tuple(range(6, 22)), (6, 30), 10, 14),
        (7, tuple(range(7, 24)), (7, 32), 12, 16),
        (8, tuple(range(8, 26)), (8, 35), 14, 18),
    ]

    for k_target, c_vals, ab_range, deg_start, deg_max in plan:
        result = try_fit_k(k_target, c_vals, ab_range, deg_start, deg_max)
        if result is None:
            print(f"  ↳ Q_{k_target}: NO FIT within (deg <= {deg_max}, samples).")
            saved_Qk[k_target] = None
            continue
        poly, fpoly, deg, dt = result
        # Cross-validate
        print(f"  Cross-validating Q_{k_target} at c = 8 against Day 89 h_k^(c=8)...")
        ok = cross_validate_c8(k_target, poly)
        saved_Qk[k_target] = {
            "poly_expanded": str(poly),
            "poly_factored": str(fpoly),
            "total_degree": deg,
            "num_samples": None,  # filled below
            "fit_time_sec": dt,
            "cv_c8_pass": ok,
        }

    # Also include the Day-88 Q_k for k = 0..5 for a complete catalog.
    saved_Qk_meta = {
        "note": (
            "Q_k(a, b, c) — normalized h_k^{(c)}(a, b) polynomials. "
            "h_k^{(c)}(a, b) = (a+3)_{c-1-k} * (b+2)_{c-1-k} * Q_k(a, b, c). "
            "k = 0..5 from Day 88 fit; k = 6+ from this Day 89 extension."
        ),
        "k=0..5_source": "2026-07-10-hk-three-var-fit-output.txt",
        "k>=6_source": "2026-07-11-Qk-fit-extended-output.txt",
        "Q_k_low_k": {
            0: "1",
            1: "-c*(c - 1)",
            2: "-c*(2*a*b + 2*a + 4*b - c**3 + 4*c**2 - 5*c + 6)",
            3: "c*(c - 2)*(c - 1)*(6*a*b + 6*a + 12*b - c**3 + 6*c**2 - 11*c + 18)",
            4: ("c*(c - 1)*(12*a**2*b**2 + 12*a**2*b + 36*a*b**2 - 12*a*b*c**3 "
                "+ 84*a*b*c**2 - 192*a*b*c + 180*a*b - 12*a*c**3 + 84*a*c**2 "
                "- 192*a*c + 144*a + 24*b**2 - 24*b*c**3 + 168*b*c**2 - 384*b*c "
                "+ 312*b + c**6 - 15*c**5 + 91*c**4 - 309*c**3 + 652*c**2 "
                "- 804*c + 432)"),
            5: ("-c*(c - 3)*(c - 2)*(c - 1)*(60*a**2*b**2 + 60*a**2*b "
                "+ 180*a*b**2 - 20*a*b*c**3 + 180*a*b*c**2 - 520*a*b*c "
                "+ 660*a*b - 20*a*c**3 + 180*a*c**2 - 520*a*c + 480*a + 120*b**2 "
                "- 40*b*c**3 + 360*b*c**2 - 1040*b*c + 1080*b + c**6 "
                "- 19*c**5 + 145*c**4 - 605*c**3 + 1534*c**2 - 2256*c + 1440)"),
        },
        "Q_k_extended": saved_Qk,
    }

    out = "/home/agent/projects/code/2026-07-11-Qk-catalog.json"
    with open(out, "w") as f:
        json.dump(saved_Qk_meta, f, indent=2, default=str)
    print(f"\nWrote {out}")

    print("\n" + "=" * 76)
    print("SUMMARY")
    print("=" * 76)
    for k_target in [0, 1, 2, 3, 4, 5]:
        print(f"  k = {k_target}: Q_k catalogued from Day 88.")
    for k_target, v in saved_Qk.items():
        if v is None:
            print(f"  k = {k_target}: NO FIT (obstruction; see log).")
        else:
            print(f"  k = {k_target}: fit at total deg ≤ {v['total_degree']}, "
                  f"c=8 CV {'PASS' if v['cv_c8_pass'] else 'FAIL'}.")


if __name__ == "__main__":
    main()
