"""Diagnose why h_3 doesn't fit as polynomial in (a, b, c) after
Pochhammer normalization -- while h_0, h_1, h_2 do fit."""
from sympy import symbols, factor, Rational, expand

exec(open('2026-07-10-hk-three-var-fit.py').read().replace(
    "if __name__ == \"__main__\":", "if False and __name__ == \"__main__\":"))


def main():
    max_jmax = max(2 * c - 2 for c in (4, 5, 6, 7, 9))
    tables = build_e2_tables(max_j=max_jmax + 2)

    a_sym, b_sym = symbols('a b')

    # Fit h_3^{(c)}(a, b) as polynomial in (a, b) for each c separately.
    for c_val in (4, 5, 6, 7, 9):
        print(f"\n=== c = {c_val} ===")
        jmax = 2 * c_val - 2
        samples = []
        for a_val in range(c_val + 2, c_val + 20):
            for b_val in range(c_val - 1, min(a_val, c_val + 20) + 1):
                hks = extract_h_k(a_val, b_val, c_val, jmax, tables)
                if hks is None or len(hks) <= 3:
                    continue
                samples.append((a_val, b_val, hks[3]))
        # 2-var polynomial fit for h_3^{(c)}(a, b).
        print(f"  {len(samples)} samples")
        # try fit
        from sympy import Matrix
        for max_deg in range(0, 15):
            monomials = []
            for da in range(max_deg + 1):
                for db in range(max_deg + 1 - da):
                    monomials.append((da, db))
            N = len(monomials)
            if len(samples) < N + 3:
                print(f"    stop at deg {max_deg}: {N} monomials, {len(samples)} samples")
                break
            A_rows = []
            yy = []
            for (av, bv, val) in samples:
                A_rows.append([av ** da * bv ** db for (da, db) in monomials])
                yy.append(val)
            A = Matrix(A_rows); y = Matrix(yy); aug = A.row_join(y)
            rref, pivots = aug.rref()
            if (aug.cols - 1) in pivots:
                continue
            if len(pivots) != N:
                continue
            sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
            poly = sum(sol[i] * a_sym ** monomials[i][0] * b_sym ** monomials[i][1]
                       for i in range(N))
            poly = expand(poly)
            # Verify
            ok = all(poly.subs({a_sym: av, b_sym: bv}) == val
                     for (av, bv, val) in samples)
            if ok:
                fpoly = factor(poly)
                print(f"  h_3^{{({c_val})}}(a, b) = {fpoly}")
                print(f"    (degree <= {max_deg})")
                break


if __name__ == "__main__":
    main()
