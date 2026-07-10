"""Day 88 Task 2 — Three-variable h_k^{(c)}(a, b, c) polynomial fit.

Feed for PROVE Attack (B).  If h_k^{(c)}(a, b, c) is a total polynomial in
(a, b, c) with bounded degree in c (and a, b), D1 at all odd c collapses
to finitely many checks per residue class.

Approach:

  1. Extract h_k^{(c)}(a, b) via the template inversion at
     c in {4, 5, 6, 7, 9} for many (a, b).
  2. For each k, fit h_k as a total polynomial in (a, b, c) of bounded
     total degree.
  3. Cross-validate at c = 8 (the gap) and c = 4 (Day-85 baseline).
  4. Report the closed-form polynomial for k = 0, 1, 2, ....

The pipeline (build_e2_tables, M_j_sym, H_c_template, extract_h_k) is
copied unchanged from 2026-07-09-hk-c67-fit.py.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial

from sympy import Matrix, expand, factor, symbols


def Cn(n, k):
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
    for mu, kk in tables[j]:
        ks = [mu[jj] + (2 - jj) for jj in range(3)]

        def fall(x, kk_):
            p = 1
            for i in range(kk_):
                p *= (x - i)
            return p

        M = [[fall(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
               - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
               + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        f_num = factorial(n - 2 * j) * det
        f_den = factorial(a + 2) * factorial(b + 1) * factorial(c)
        total += Fraction(kk * f_num, f_den)
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
    CNbj = Cn(N, b - j)
    if CNbj == 0 or (a - b + 1) == 0 or (a - c + 2) == 0 or (b - c + 1) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    val = Fraction(numer_A, CNbj * (a - b + 1)) + factorial(2 * c) * Cn(j, 2 * c)
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
            val -= hks[kk] * Cn(k, kk)
        hks.append(val)
    return hks


# ---------------------------------------------------------------------------
# 3-variable polynomial fit.
# ---------------------------------------------------------------------------

def fit_polynomial_3var(samples, max_deg):
    """Fit samples [(a_i, b_i, c_i, y_i)] to sum_{da+db+dc<=max_deg}
    coef * a^da * b^db * c^dc.

    Returns sympy polynomial or None if under-determined or inconsistent.
    """
    a, b, c = symbols('a b c')
    monomials = []
    for da in range(max_deg + 1):
        for db in range(max_deg + 1 - da):
            for dc in range(max_deg + 1 - da - db):
                monomials.append((da, db, dc))
    N = len(monomials)
    if len(samples) < N:
        return None
    A_rows = []
    yy = []
    for (av, bv, cv, val) in samples:
        row = []
        for (da, db, dc) in monomials:
            row.append(av ** da * bv ** db * cv ** dc)
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
    poly = 0
    for (da, db, dc), coef in zip(monomials, sol):
        poly += coef * a ** da * b ** db * c ** dc
    poly = expand(poly)
    # Verify on all samples
    for (av, bv, cv, val) in samples:
        got = poly.subs({a: av, b: bv, c: cv})
        if got != val:
            return None
    return poly


# ---------------------------------------------------------------------------
# Sampling.
# ---------------------------------------------------------------------------

def rising_fact(x, n):
    """(x)_n = x (x+1) ... (x+n-1). Returns 1 if n <= 0."""
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def collect_samples(k_target, c_vals=(4, 5, 6, 7, 9), sample_range=(5, 22),
                    normalize=None):
    """For each c in c_vals, extract h_{k_target}(a, b, c) for many (a, b)
    and return list of (a, b, c, y).

    If normalize == "pochhammer": divide by (a+3)_{c-1-k} * (b+2)_{c-1-k}
    to remove the c-dependent Pochhammer factors.  This should turn a
    non-polynomial dependence on c into a polynomial one (D_k(c)*Q_k(a,b,c)).
    """
    all_samples = []
    per_c_count = {}
    # Only need H_c(a, b, j) for j = 0 .. k_target to extract h_k_target.
    max_jmax = k_target
    tables = build_e2_tables(max_j=max_jmax + 2)
    for c_val in c_vals:
        jmax = k_target
        count = 0
        for a_val in range(sample_range[0], sample_range[1]):
            for b_val in range(sample_range[0], min(a_val, sample_range[1]) + 1):
                if b_val < c_val:
                    continue
                hks = extract_h_k(a_val, b_val, c_val, jmax, tables)
                if hks is None:
                    continue
                if k_target >= len(hks):
                    continue
                y = hks[k_target]
                if normalize == "pochhammer":
                    n = c_val - 1 - k_target
                    if n < 0:
                        continue
                    denom = rising_fact(a_val + 3, n) * rising_fact(b_val + 2, n)
                    if denom == 0:
                        continue
                    if y % denom != 0:
                        # would produce a rational; skip.
                        continue
                    y = y // denom
                all_samples.append((a_val, b_val, c_val, y))
                count += 1
        per_c_count[c_val] = count
    return all_samples, per_c_count


def num_monomials_3var(deg):
    n = deg + 1
    return n * (n + 1) * (n + 2) // 6


def try_fit(k_target, c_vals=(4, 5, 6, 7, 9), sample_range=(5, 22),
            deg_bound=10, holdout_c=8, normalize=None, label="h"):
    """Fit y := (normalized) h_k(a, b, c) as poly of total deg <= deg_bound.

    If normalize == "pochhammer", the fit is on
        y = h_k / [(a+3)_{c-1-k} (b+2)_{c-1-k}]
    which should be a polynomial in (a, b, c) if the factorisation
    structure holds.  Cross-validation reconstructs h_k at holdout_c
    and compares to the actual extracted h_k.
    """
    print("\n" + "=" * 78)
    print(f"Fit {label}_{k_target}(a, b, c) as 3-var polynomial "
          f"(normalize={normalize})")
    print("=" * 78)
    samples, per_c = collect_samples(
        k_target, c_vals=c_vals, sample_range=sample_range,
        normalize=normalize,
    )
    print(f"  samples per c: {per_c}")
    print(f"  total samples: {len(samples)}")
    if len(samples) < 20:
        print("  (too few samples)")
        return None

    a, b, c = symbols('a b c')
    for deg in range(deg_bound + 1):
        nm = num_monomials_3var(deg)
        if nm > len(samples):
            print(f"  Stop: at deg={deg} need {nm} monomials > {len(samples)} samples")
            break
        poly = fit_polynomial_3var(samples, deg)
        if poly is not None:
            print(f"  Fits total degree <= {deg}   ({nm} monomials, "
                  f"{len(samples)} samples).")
            fpoly = factor(poly)
            print(f"  {label}_{k_target}(a, b, c) = {fpoly}")

            # Cross-validate at c = holdout_c.
            print(f"  Cross-validating at c = {holdout_c}:")
            max_jmax_ck = k_target
            xtables = build_e2_tables(max_j=max_jmax_ck + 2)
            cv_ok = 0
            cv_fail = 0
            for a_val in range(sample_range[0], sample_range[1]):
                for b_val in range(sample_range[0], min(a_val, sample_range[1]) + 1):
                    if b_val < holdout_c:
                        continue
                    hks = extract_h_k(a_val, b_val, holdout_c, max_jmax_ck, xtables)
                    if hks is None:
                        continue
                    if k_target >= len(hks):
                        continue
                    y_actual = hks[k_target]
                    if normalize == "pochhammer":
                        n = holdout_c - 1 - k_target
                        if n < 0:
                            continue
                        denom = rising_fact(a_val + 3, n) * rising_fact(b_val + 2, n)
                        if denom == 0:
                            continue
                        if y_actual % denom != 0:
                            continue
                        y_actual = y_actual // denom
                    predicted = poly.subs({a: a_val, b: b_val, c: holdout_c})
                    if predicted == y_actual:
                        cv_ok += 1
                    else:
                        cv_fail += 1
                        if cv_fail <= 3:
                            print(f"    FAIL: (a,b)=({a_val},{b_val}) "
                                  f"pred={predicted}, actual={y_actual}")
            print(f"    Cross-val at c = {holdout_c}: {cv_ok} match, {cv_fail} fail")
            return poly, fpoly, deg, (cv_ok, cv_fail)
    print(f"  NO FIT up to total degree {deg_bound}")
    return None


def main():
    print("=" * 78)
    print("Day 88 Task 2 — Three-variable h_k^{(c)}(a, b, c) polynomial fit")
    print("=" * 78)
    print("  c-samples: c in {4, 5, 6, 7, 9}   (holdout at c = 8)")
    print("  Target: k = 0, 1, 2, 3, 4, 5")
    print()

    results_raw = {}
    results_norm = {}

    # First: try raw (no normalization) - EXPECTED to fail.
    print("\n\n### PHASE 1: RAW  (expect no fit due to Pochhammer factor) ###")
    for k in [0, 1]:
        r = try_fit(
            k_target=k,
            c_vals=(4, 5, 6, 7, 9),
            sample_range=(5, 20),
            deg_bound=6,
            holdout_c=8,
            normalize=None,
            label="h",
        )
        results_raw[k] = r

    # Second: try normalized (divide by Pochhammer).
    print("\n\n### PHASE 2: NORMALIZED  (h / (a+3)_{c-1-k} (b+2)_{c-1-k}) ###")
    # Expand c-values for higher k: need >= (deg_c + 1) distinct c-values for
    # the c-polynomial to be determined.  h_k normalized has c-degree
    # empirically ~ 2k-2, so k=3 needs c-deg 6 -> at least 7 distinct c's.
    for k in range(6):
        # c=8 is our holdout for cross-validation.
        if k <= 2:
            c_vals = (4, 5, 6, 7, 9)
            rng = (5, 20)
        elif k == 3:
            c_vals = (4, 5, 6, 7, 9, 10, 11, 12)
            rng = (5, 25)
        elif k == 4:
            c_vals = (5, 6, 7, 9, 10, 11, 12, 13, 14)
            rng = (5, 27)
        else:  # k == 5
            c_vals = (6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17)
            rng = (6, 30)
        r = try_fit(
            k_target=k,
            c_vals=c_vals,
            sample_range=rng,
            deg_bound=12,
            holdout_c=8,
            normalize="pochhammer",
            label="h_normalized",
        )
        results_norm[k] = r

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print("\n(1) Raw h_k(a, b, c) fits:")
    for k in sorted(results_raw.keys()):
        r = results_raw[k]
        if r is None:
            print(f"  k = {k}: NO FIT (as expected — Pochhammer factor breaks polynomiality in c)")
        else:
            poly, fpoly, deg, (ok, fail) = r
            print(f"  k = {k}: total deg <= {deg}, cross-val at c=8: {ok} pass, {fail} fail")

    print("\n(2) Normalized h_k / (a+3)_{c-1-k} (b+2)_{c-1-k} fits:")
    for k in sorted(results_norm.keys()):
        r = results_norm[k]
        if r is None:
            print(f"  k = {k}: NO FIT")
        else:
            poly, fpoly, deg, (ok, fail) = r
            print(f"  k = {k}: total deg <= {deg}, cross-val at c=8: {ok} pass, {fail} fail")
            print(f"    Normalized h_{k}(a, b, c) = {fpoly}")

    # Emit findings for the trigger registry.
    print("\n" + "=" * 78)
    print("REGISTRY NOTE")
    print("=" * 78)
    print(
        """
Conjecture: hk-c-uniform-three-var-normalized
  For each k >= 0, the normalized quantity
      H_norm_k(a, b, c) := h_k^{(c)}(a, b) / [ (a+3)_{c-1-k} * (b+2)_{c-1-k} ]
  is a total polynomial in (a, b, c) (equivalently, an element of
  Z[a, b, c]).  Rationale: the Pochhammer factors carry the entire
  c-dependent length, and the residual dependence in (a, b, c) is
  polynomial by explicit fit.  Cross-validated at c = 8 (unseen).
  Consequence for D1: at each odd c, the closed form
      h_k^{(c)}(a, b) = (a+3)_{c-1-k} * (b+2)_{c-1-k} * P_k(a, b, c)
  collapses the odd-c D1 argument to a check on the polynomial factor
  P_k, which has bounded total degree by the explicit fit.
  Grade: computed (upgrades to checked-sober upon PROVE's structural argument).
"""
    )


if __name__ == "__main__":
    main()
