"""
Day-57 used UNIT-step finite differences as a degree-test for the
Ehrhart quasipolynomial — that test is *wrong* for period p > 1. For a
quasipoly f of degree d period p, only the PERIOD-step (d+1)-th
difference Δ_p^{d+1} f vanishes; the unit-step Δ^{d+1} f can grow
linearly. Clio caught the resulting overstatement.

This script applies the correct test:
  Δ_p^{d+1} f(N) = sum_{i=0}^{d+1} (-1)^{d+1-i} C(d+1, i) f(N + i*p)
should be identically 0 on N ≥ 0 (a true equality from Ehrhart theory).

We verify:
  (BDI) Δ_6^4 c_BDI(N) = 0  ⇒  c_BDI is degree-3, period-6 quasipoly.
  (AII) Δ_6^5 c_AII(N) = 0  ⇒  c_AII is degree-4, period-6 quasipoly.

We then extract the leading coefficients honestly from the residue
sub-polynomials and report the asymptotic ratio.

This is the *correct* version of Day-57 Task 1.
"""

import csv
import math
from fractions import Fraction
from pathlib import Path

OUT_DIR = Path(__file__).parent


def load_counts(path):
    bdi, aii = [], []
    with open(path) as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if not row[0]:
                continue
            N = int(row[0])
            assert N == len(bdi), f"unexpected N={N}, expected {len(bdi)}"
            bdi.append(int(row[1]))
            aii.append(int(row[2]))
    return bdi, aii


def period_step_diff(seq, p, k, N):
    """Δ_p^k f(N) = sum_{i=0}^{k} (-1)^{k-i} C(k, i) f(N + i*p)."""
    s = 0
    for i in range(k + 1):
        if N + i * p >= len(seq):
            raise IndexError(f"need f(N + {i*p}) but len={len(seq)}")
        s += (-1) ** (k - i) * math.comb(k, i) * seq[N + i * p]
    return s


def fit_residue_poly_exact(seq, residue, period, deg):
    """
    Fit a polynomial of degree `deg` to the residue-r subsequence using
    Fraction-arithmetic Lagrange interpolation. Returns coefficients
    a_d, a_{d-1}, ..., a_0 (high degree first) as Fractions, with
    polynomial in N (not in k = (N-r)/period).
    """
    # Points (N, f(N)) with N ≡ residue mod period, N ≥ residue
    Ns = [N for N in range(residue, len(seq), period)]
    Fs = [Fraction(seq[N]) for N in Ns]
    if len(Ns) <= deg:
        raise ValueError(f"not enough data: need {deg + 1}, have {len(Ns)}")
    # Use the first deg+1 points for Newton interpolation, then verify
    # against the remaining points.
    pts = list(zip(Ns[:deg + 1], Fs[:deg + 1]))
    # Lagrange interpolation -> polynomial coefficients (in N)
    # Build by expanding sum_i f_i * prod_{j != i} (x - N_j) / (N_i - N_j).
    # Result is a list of Fractions [a_d, ..., a_0].
    coeffs = [Fraction(0)] * (deg + 1)
    for i, (Ni, fi) in enumerate(pts):
        # weight = fi / prod_{j != i} (N_i - N_j)
        denom = Fraction(1)
        for j, (Nj, _) in enumerate(pts):
            if i == j:
                continue
            denom *= Fraction(Ni - Nj)
        w = fi / denom
        # polynomial prod_{j != i} (x - N_j), expanded as coefficient list
        poly = [Fraction(1)]  # poly[k] = coeff of x^k; start with constant 1
        for j, (Nj, _) in enumerate(pts):
            if i == j:
                continue
            # multiply by (x - N_j)
            new = [Fraction(0)] * (len(poly) + 1)
            for k, c in enumerate(poly):
                new[k + 1] += c            # x * c x^k
                new[k] += -Nj * c          # -N_j * c x^k
            poly = new
        # accumulate w * poly into coeffs
        for k, c in enumerate(poly):
            coeffs[deg - k] += w * c  # high-degree first
    # Verify on remaining points
    max_err = 0
    for N, f in zip(Ns[deg + 1:], Fs[deg + 1:]):
        val = Fraction(0)
        for k, c in enumerate(coeffs):
            val += c * Fraction(N) ** (deg - k)
        err = abs(val - f)
        if err > max_err:
            max_err = err
    return coeffs, len(Ns) - (deg + 1), max_err


def main():
    bdi, aii = load_counts(OUT_DIR / "raw_counts_extended.csv")
    N_MAX = len(bdi) - 1
    print(f"# Verify quasipolynomial structure (N up to {N_MAX})")
    print()

    # Test BDI: degree 3 period 6
    print("## BDI test: Δ_6^4 c_BDI(N) should be 0 for all N s.t. N + 24 ≤ N_MAX")
    bad_bdi = 0
    for N in range(N_MAX - 24 + 1):
        v = period_step_diff(bdi, 6, 4, N)
        if v != 0:
            bad_bdi += 1
            if bad_bdi <= 5:
                print(f"  FAIL: Δ_6^4 c_BDI({N}) = {v}")
    print(f"  RESULT: {'PASS' if bad_bdi == 0 else 'FAIL'}: "
          f"{N_MAX - 24 + 1 - bad_bdi}/{N_MAX - 24 + 1} N values give exact 0")
    print()

    # Test AII: degree 4 period 6
    print("## AII test: Δ_6^5 c_AII(N) should be 0 for all N s.t. N + 30 ≤ N_MAX")
    bad_aii = 0
    for N in range(N_MAX - 30 + 1):
        v = period_step_diff(aii, 6, 5, N)
        if v != 0:
            bad_aii += 1
            if bad_aii <= 5:
                print(f"  FAIL: Δ_6^5 c_AII({N}) = {v}")
    print(f"  RESULT: {'PASS' if bad_aii == 0 else 'FAIL'}: "
          f"{N_MAX - 30 + 1 - bad_aii}/{N_MAX - 30 + 1} N values give exact 0")
    print()

    # Cross-check: AII degree 4 BUT period < 6?
    print("## AII counter-tests")
    for p in [1, 2, 3]:
        bad = 0
        for N in range(N_MAX - 5 * p + 1):
            v = period_step_diff(aii, p, 5, N)
            if v != 0:
                bad += 1
        n_tot = N_MAX - 5 * p + 1
        print(f"  Δ_{p}^5 c_AII = 0?  {n_tot - bad}/{n_tot} pass.")
    # Lower degree (degree=3)?
    bad = 0
    for N in range(N_MAX - 24 + 1):
        v = period_step_diff(aii, 6, 4, N)
        if v != 0:
            bad += 1
    n_tot = N_MAX - 24 + 1
    print(f"  Δ_6^4 c_AII = 0 (degree-3 hypothesis)?  {n_tot - bad}/{n_tot} pass.")
    print()

    # Extract leading coefficients (Ehrhart polynomial restricted to res 0 mod 6)
    print("## Leading coefficients (exact via Lagrange interpolation, residue 0 mod 6)")
    print()

    coeffs_bdi, n_extra_bdi, err_bdi = fit_residue_poly_exact(bdi, 0, 6, 3)
    print(f"BDI residue 0 mod 6, degree-3 fit:")
    for d, c in enumerate(coeffs_bdi):
        deg = 3 - d
        print(f"  N^{deg} coeff = {c}  ({float(c):.10f})")
    print(f"  Verification on {n_extra_bdi} extra points: max abs err = {float(err_bdi)}")
    print()

    coeffs_aii, n_extra_aii, err_aii = fit_residue_poly_exact(aii, 0, 6, 4)
    print(f"AII residue 0 mod 6, degree-4 fit:")
    for d, c in enumerate(coeffs_aii):
        deg = 4 - d
        print(f"  N^{deg} coeff = {c}  ({float(c):.10f})")
    print(f"  Verification on {n_extra_aii} extra points: max abs err = {float(err_aii)}")
    print()

    # Leading coefficient × d! = polytope volume
    a3_bdi = coeffs_bdi[0]  # N^3 coeff
    a4_aii = coeffs_aii[0]  # N^4 coeff
    print(f"BDI Ehrhart: leading coeff = {a3_bdi} = {float(a3_bdi):.10f}")
    print(f"  Volume(BDI polytope) = 3! · leading = {6 * a3_bdi} = {float(6 * a3_bdi):.10f}")
    print(f"AII Ehrhart: leading coeff = {a4_aii} = {float(a4_aii):.10f}")
    print(f"  Volume(AII polytope) = 4! · leading = {24 * a4_aii} = {float(24 * a4_aii):.10f}")
    print()

    # Leading coefficients should be the same across all residues mod 6
    print("## Leading-coefficient consistency across residues mod 6 (Ehrhart theorem)")
    print()
    print("BDI:")
    for r in range(6):
        cs, _, err = fit_residue_poly_exact(bdi, r, 6, 3)
        print(f"  residue {r}: N^3 coeff = {cs[0]} = {float(cs[0]):.10f}  (verify err = {float(err)})")
    print("AII:")
    for r in range(6):
        cs, _, err = fit_residue_poly_exact(aii, r, 6, 4)
        print(f"  residue {r}: N^4 coeff = {cs[0]} = {float(cs[0]):.10f}  (verify err = {float(err)})")
    print()

    # Asymptotic ratio
    print("## Asymptotic ratio c_AII(N) / c_BDI(N)")
    print()
    # Leading: a4_aii N^4 / a3_bdi N^3 = (a4_aii / a3_bdi) N. So ratio ~ R · N.
    R = float(a4_aii) / float(a3_bdi)
    print(f"Leading-order: ratio = ({float(a4_aii):.10f} N^4) / ({float(a3_bdi):.10f} N^3) "
          f"~ {R:.6f} · N")
    print()
    print(f"{'N':>4} | {'c_AII':>10} | {'c_BDI':>10} | {'ratio':>10} | "
          f"{'ratio/N':>10} | {'predicted':>10}")
    for N in [20, 40, 60, 80, 100, 120]:
        r_ = aii[N] / bdi[N]
        pred = R * N
        print(f"{N:>4} | {aii[N]:>10} | {bdi[N]:>10} | {r_:>10.4f} | "
              f"{r_ / N:>10.5f} | {pred:>10.4f}")
    print()
    print(f"Asymptote: ratio/N → {R:.6f} = {Fraction(a4_aii / a3_bdi)} as N → ∞")


if __name__ == "__main__":
    main()
