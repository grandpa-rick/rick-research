"""Quick 3-var fit for h_3 with lean sample count and deg 6."""
from sympy import symbols, factor, expand, Matrix

exec(open('2026-07-10-hk-three-var-fit.py').read().replace(
    "if __name__ == \"__main__\":", "if False and __name__ == \"__main__\":"))


def main():
    a_sym, b_sym, c_sym = symbols('a b c')
    max_jmax = max(2 * c - 2 for c in (4, 5, 6, 7, 9))
    tables = build_e2_tables(max_j=max_jmax + 2)

    # Compact sampling: 20 samples per c, each c value included.
    samples = []
    per_c = {}
    for c_val in (4, 5, 6, 7, 9):
        count = 0
        for a_val in range(c_val + 2, c_val + 12):
            for b_val in range(c_val - 1, min(a_val, c_val + 12) + 1):
                if count >= 20:
                    break
                jmax = 2 * c_val - 2
                hks = extract_h_k(a_val, b_val, c_val, jmax, tables)
                if hks is None or len(hks) <= 3:
                    continue
                n = c_val - 1 - 3
                if n < 0:
                    continue
                denom = rising_fact(a_val + 3, n) * rising_fact(b_val + 2, n)
                if denom == 0 or hks[3] % denom != 0:
                    continue
                y = hks[3] // denom
                samples.append((a_val, b_val, c_val, y))
                count += 1
            if count >= 20:
                break
        per_c[c_val] = count
    print(f"samples per c: {per_c}, total: {len(samples)}")

    # Fit at degree 6.
    for deg in [6, 7, 8, 9, 10]:
        print(f"\n--- degree <= {deg} ---")
        monomials = []
        for da in range(deg + 1):
            for db in range(deg + 1 - da):
                for dc in range(deg + 1 - da - db):
                    monomials.append((da, db, dc))
        N = len(monomials)
        print(f"  N = {N} monomials")
        if N > len(samples):
            print("  under-determined")
            continue
        A_rows = []
        yy = []
        for (av, bv, cv, val) in samples:
            row = []
            for (da, db, dc) in monomials:
                row.append(av ** da * bv ** db * cv ** dc)
            A_rows.append(row)
            yy.append(val)
        A = Matrix(A_rows); y = Matrix(yy); aug = A.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            print("  inconsistent")
            continue
        if len(pivots) != N:
            print(f"  under-determined ({len(pivots)} pivots)")
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        poly = sum(sol[i] * a_sym ** monomials[i][0]
                        * b_sym ** monomials[i][1]
                        * c_sym ** monomials[i][2]
                   for i in range(N))
        poly = expand(poly)
        # Verify
        ok = all(poly.subs({a_sym: av, b_sym: bv, c_sym: cv}) == val
                 for (av, bv, cv, val) in samples)
        if ok:
            fpoly = factor(poly)
            print(f"  FIT: normalized h_3(a, b, c) = {fpoly}")
            # Cross-validate at c=8.
            xtables = build_e2_tables(max_j=2 * 8)
            cv_ok = 0
            cv_fail = 0
            for a_val in range(10, 20):
                for b_val in range(8, a_val + 1):
                    if b_val < 8:
                        continue
                    hks = extract_h_k(a_val, b_val, 8, 14, xtables)
                    if hks is None or len(hks) <= 3:
                        continue
                    n = 8 - 1 - 3
                    denom = rising_fact(a_val + 3, n) * rising_fact(b_val + 2, n)
                    if denom == 0 or hks[3] % denom != 0:
                        continue
                    y_actual = hks[3] // denom
                    predicted = poly.subs({a_sym: a_val, b_sym: b_val, c_sym: 8})
                    if predicted == y_actual:
                        cv_ok += 1
                    else:
                        cv_fail += 1
                        if cv_fail <= 2:
                            print(f"    FAIL ({a_val}, {b_val}): pred={predicted}, actual={y_actual}")
            print(f"  Cross-val at c=8: {cv_ok} pass, {cv_fail} fail")
            return
        else:
            print("  fitted but sample-verify FAIL (numerical issue?)")


if __name__ == "__main__":
    main()
