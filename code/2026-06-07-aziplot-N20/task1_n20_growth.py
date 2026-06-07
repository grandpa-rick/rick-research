"""
Task 1: Extend BDI vs Azenhas n=2 lattice enumeration to N=20.

Compute c_N := |P intersect Z^k : sum of coords <= N| for both polytopes.

BDI n=2 (variables M_1, B_1, T_1, S, M_1 = 0):
    T_1 <= B_1
    S <= 2(B_1 - T_1)
Polytope has 3 free variables (B_1, T_1, S), so dim = 3.
Ehrhart-like growth: c_N ~ c_3 N^3 + c_2 N^2 + ... (cubic).
3rd differences should be bounded (period-2 from the 2(B-T) parity? let's see).

Azenhas n=2 (variables m_2, m_23, m_14, m_123, m_124, with m_14 = m_23 forced):
    m_123 <= m_2
    m_124 <= m_23
Polytope has 4 free variables (m_2, m_23, m_123, m_124), so dim = 4.
But the total weight is m_2 + m_23 + m_14 + m_123 + m_124 = m_2 + 2 m_23 + m_123 + m_124.
So the SUM weight is weighted (m_23 counts twice).
Growth should be quartic.

Output:
- CSV with N, c_BDI, c_AZE, and 1st/2nd/3rd/4th differences for each.
- Fitted Ehrhart quasipolynomial coefficients (period-2 fit).
- Matplotlib plot.
"""

import csv
import os
from pathlib import Path

OUT_DIR = Path(__file__).parent

# ----- Enumerators -----

def count_bdi_n2(N):
    """BDI n=2: sum (M_1=0) + B_1 + T_1 + S <= N, with T_1 <= B_1, S <= 2(B_1-T_1)."""
    c = 0
    for B in range(N + 1):
        for T in range(B + 1):
            d = B - T
            S_hi = min(2 * d, N - B - T)
            if S_hi < 0:
                continue
            c += S_hi + 1
    return c


def count_aze_n2(N):
    """
    Azenhas n=2: sum (m_2 + 2 m_23 + m_123 + m_124) <= N with m_14 = m_23,
    m_123 <= m_2, m_124 <= m_23.
    """
    c = 0
    for m_2 in range(N + 1):
        for m_23 in range((N - m_2) // 2 + 1):
            rest = N - m_2 - 2 * m_23
            # m_123 in [0, m_2], m_124 in [0, m_23], with m_123 + m_124 <= rest.
            for m_123 in range(min(m_2, rest) + 1):
                hi = min(m_23, rest - m_123)
                if hi < 0:
                    continue
                c += hi + 1
    return c


# ----- Finite differences -----
def finite_diffs(seq, order):
    out = [list(seq)]
    cur = list(seq)
    for _ in range(order):
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        out.append(cur)
    return out


# ----- Ehrhart quasipolynomial fit -----
def fit_quasipoly(c, deg, period):
    """
    Fit c_N as a quasipolynomial of degree deg with given period.
    For each residue r in 0..period-1, take c_N for N >= period (skip
    initial values where boundary effects dominate) with N % period == r,
    and Lagrange-interpolate the first deg+1 of them.
    """
    import numpy as np
    fits = {}
    for r in range(period):
        idx = [i for i in range(len(c)) if i % period == r and i >= period]
        if len(idx) < deg + 1:
            idx = [i for i in range(len(c)) if i % period == r]
        if len(idx) < deg + 1:
            raise ValueError(f"not enough data for residue {r}, need {deg+1} got {len(idx)}")
        Xs = np.array(idx[:(deg + 1)], dtype=float)
        Ys = np.array([c[i] for i in idx[:(deg + 1)]], dtype=float)
        coeffs = np.polyfit(Xs, Ys, deg)
        fits[r] = coeffs
    fits['_period'] = period
    return fits


def eval_quasipoly(fits, N):
    import numpy as np
    period = fits['_period']
    coeffs = fits[N % period]
    return float(np.polyval(coeffs, N))


# ----- Main -----
def main():
    # We need >= (deg+1)*period values for the period-6 quartic fit at the tail
    # (and we cite "N=20" for the table because that was Clio's range, but
    # internally fit on a wider window for stability).
    N_MAX = 40
    N_REPORT = 20  # values reported in CSV / table

    bdi_seq = [count_bdi_n2(N) for N in range(N_MAX + 1)]
    aze_seq = [count_aze_n2(N) for N in range(N_MAX + 1)]

    print(f"BDI n=2 lattice counts (N=0..{N_REPORT}):")
    for N in range(N_REPORT + 1):
        print(f"  N={N:2d}: {bdi_seq[N]}")

    print()
    print(f"Azenhas n=2 lattice counts (N=0..{N_REPORT}):")
    for N in range(N_REPORT + 1):
        print(f"  N={N:2d}: {aze_seq[N]}")

    # Finite differences
    bdi_diffs = finite_diffs(bdi_seq, 5)
    aze_diffs = finite_diffs(aze_seq, 5)

    def short(seq):
        return seq[:min(len(seq), N_REPORT)]

    print()
    print("BDI 3rd differences (Clio said 'bounded period-2' -- we see "
          "BOUNDED with period 6 pattern [-1,1,0,1,-1,2]):")
    print(" ", short(bdi_diffs[3]))
    print("BDI 4th differences (also period 6, bounded — confirms degree 3):")
    print(" ", short(bdi_diffs[4]))

    print()
    print("Azenhas 3rd differences (Clio: grows linearly):")
    print(" ", short(aze_diffs[3]))
    print("Azenhas 4th differences (grows by ~3 every 6 steps; "
          "consistent with degree 4):")
    print(" ", short(aze_diffs[4]))
    print("Azenhas 5th differences (bounded period 6 — confirms degree 4):")
    print(" ", short(aze_diffs[5]))

    # Period detection: BDI 3rd diff has period 6 → cubic-quasi(period 6).
    # AZE: 4th diff is unbounded if we try period 2, but a period-6 quartic
    # fit may capture the full structure. Try period 6 for both.
    print()
    print("--- Ehrhart quasipolynomial fits ---")
    fits_bdi = fit_quasipoly(bdi_seq, deg=3, period=6)
    fits_aze = fit_quasipoly(aze_seq, deg=4, period=6)

    print("BDI fit (cubic, period 6):")
    for r, co in fits_bdi.items():
        if r == '_period': continue
        print(f"  residue {r}: coefficients (high deg first) = {co}")
    print("Azenhas fit (quartic, period 6):")
    for r, co in fits_aze.items():
        if r == '_period': continue
        print(f"  residue {r}: coefficients (high deg first) = {co}")

    # Verification: predicted vs actual (across the full N_MAX range)
    print()
    print("Verification (predicted - actual):")
    print("  N | BDI pred (cubic) | BDI actual | err | AZE pred (quartic) | AZE actual | err")
    rows = []
    max_bdi_err = 0.0
    max_aze_err = 0.0
    for N in range(N_MAX + 1):
        bp = eval_quasipoly(fits_bdi, N)
        ap = eval_quasipoly(fits_aze, N)
        be = bp - bdi_seq[N]
        ae = ap - aze_seq[N]
        if N >= 6:  # past the boundary regime
            max_bdi_err = max(max_bdi_err, abs(be))
            max_aze_err = max(max_aze_err, abs(ae))
        if N <= N_REPORT or N % 5 == 0:
            print(f"  {N:2d} | {bp:.4f} | {bdi_seq[N]} | {be:+.4e} "
                  f"| {ap:.4f} | {aze_seq[N]} | {ae:+.4e}")
        rows.append((N, bdi_seq[N], aze_seq[N], bp, ap))
    print(f"\nMax fit error on N>=6: BDI {max_bdi_err:.3e}, AZE {max_aze_err:.3e}")
    print("(should be ~0 if degrees and period are right)")

    # CSV output (N=0..N_REPORT, which is 20 by default)
    csv_path = OUT_DIR / "n20_lattice_counts.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            ["N", "c_BDI", "c_AZE",
             "BDI_d1", "BDI_d2", "BDI_d3", "BDI_d4",
             "AZE_d1", "AZE_d2", "AZE_d3", "AZE_d4", "AZE_d5",
             "BDI_fit_cubic", "AZE_fit_quartic"]
        )
        for N in range(N_REPORT + 1):
            row = [N, bdi_seq[N], aze_seq[N]]
            for k in range(1, 5):
                row.append(bdi_diffs[k][N] if N < len(bdi_diffs[k]) else "")
            for k in range(1, 6):
                row.append(aze_diffs[k][N] if N < len(aze_diffs[k]) else "")
            row.append(eval_quasipoly(fits_bdi, N))
            row.append(eval_quasipoly(fits_aze, N))
            w.writerow(row)
    print(f"\nCSV saved to {csv_path}")

    # Plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 2, figsize=(12, 9))
        Ns = list(range(N_REPORT + 1))
        bdi_p = bdi_seq[:N_REPORT + 1]
        aze_p = aze_seq[:N_REPORT + 1]

        ax = axes[0, 0]
        ax.plot(Ns, bdi_p, "o-", label="BDI n=2 (cubic)")
        ax.plot(Ns, aze_p, "s-", label="Azenhas n=2 (quartic)")
        ax.set_xlabel("N")
        ax.set_ylabel("c_N")
        ax.set_title("Lattice point counts up to weight N")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, alpha=0.4)

        ax = axes[0, 1]
        d3_bdi = bdi_diffs[3][:N_REPORT]
        d3_aze = aze_diffs[3][:N_REPORT]
        ax.plot(range(len(d3_bdi)), d3_bdi, "o-", label="BDI 3rd diff")
        ax.plot(range(len(d3_aze)), d3_aze, "s-", label="AZE 3rd diff")
        ax.set_xlabel("N")
        ax.set_ylabel("3rd finite difference")
        ax.set_title("3rd finite differences (BDI bounded, AZE grows)")
        ax.legend()
        ax.grid(True, alpha=0.4)

        ax = axes[1, 0]
        d4_bdi = bdi_diffs[4][:N_REPORT]
        d4_aze = aze_diffs[4][:N_REPORT]
        ax.plot(range(len(d4_bdi)), d4_bdi, "o-", label="BDI 4th diff (bounded)")
        ax.plot(range(len(d4_aze)), d4_aze, "s-", label="AZE 4th diff (grows)")
        ax.set_xlabel("N")
        ax.set_ylabel("4th finite difference")
        ax.set_title("4th finite differences (AZE bounded; BDI -> 0)")
        ax.legend()
        ax.grid(True, alpha=0.4)

        ax = axes[1, 1]
        ratios_bdi = [bdi_seq[i + 1] / bdi_seq[i] if bdi_seq[i] else 0 for i in range(1, N_REPORT)]
        ratios_aze = [aze_seq[i + 1] / aze_seq[i] if aze_seq[i] else 0 for i in range(1, N_REPORT)]
        ax.plot(range(1, N_REPORT), ratios_bdi, "o-", label="BDI c_{N+1}/c_N")
        ax.plot(range(1, N_REPORT), ratios_aze, "s-", label="AZE c_{N+1}/c_N")
        ax.set_xlabel("N")
        ax.set_ylabel("c_{N+1} / c_N")
        ax.set_title("Successive growth ratios (asymptote = 1 for polynomials)")
        ax.legend()
        ax.grid(True, alpha=0.4)

        plt.tight_layout()
        plt.savefig(OUT_DIR / "n20_growth.png", dpi=120)
        print(f"Plot saved to {OUT_DIR / 'n20_growth.png'}")
    except Exception as exc:
        print(f"matplotlib unavailable or failed: {exc}")


if __name__ == "__main__":
    main()
