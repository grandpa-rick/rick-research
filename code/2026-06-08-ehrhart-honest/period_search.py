"""
The standard story (Day 57) said AII = degree-4 quasipolynomial period 6.
extended_enum.py showed d^4(c_AII)[N+6] - d^4(c_AII)[N] = ±3 at N >= 60,
so degree-4-period-6 is FALSIFIED.

This script:
1. Loads the cumulative count from raw_counts.csv.
2. Sweeps (k, p) for k in 1..8, p in {1..24}, and tests whether
   d^k(c) is constant within each residue class mod p in the tail.
3. Also tests: for which (deg, p) is c_N a quasipolynomial of degree
   `deg` with period `p` in the tail? (Equivalent: d^{deg+1} restricted
   to each residue mod p is zero.)
4. Reports the smallest (deg, p) that works for both BDI and AII.

NOTE: even at N=80 the AII residue-class tails may still be too short to
distinguish "true period > 6" from "approaching-bounded slowly". We
extend the enumeration to N=120 within this script for AII alone.
"""

import csv
import math
from pathlib import Path

OUT_DIR = Path(__file__).parent


def count_bdi_n2_all(N_max):
    counts = [0] * (N_max + 1)
    for B in range(N_max + 1):
        for T in range(B + 1):
            d = B - T
            rest_max = N_max - B - T
            if rest_max < 0:
                continue
            S_max = min(2 * d, rest_max)
            base = B + T
            for S in range(S_max + 1):
                counts[base + S] += 1
    cum = [0] * (N_max + 1)
    cum[0] = counts[0]
    for i in range(1, N_max + 1):
        cum[i] = cum[i - 1] + counts[i]
    return cum


def count_aii_n2_all(N_max):
    counts = [0] * (N_max + 1)
    for m_2 in range(N_max + 1):
        for m_23 in range((N_max - m_2) // 2 + 1):
            partial = m_2 + 2 * m_23
            rest_max = N_max - partial
            m_123_hi = min(m_2, rest_max)
            for m_123 in range(m_123_hi + 1):
                rem = rest_max - m_123
                m_124_hi = min(m_23, rem)
                base = partial + m_123
                for m_124 in range(m_124_hi + 1):
                    counts[base + m_124] += 1
    cum = [0] * (N_max + 1)
    cum[0] = counts[0]
    for i in range(1, N_max + 1):
        cum[i] = cum[i - 1] + counts[i]
    return cum


def finite_diffs(seq, max_order):
    out = [list(seq)]
    cur = list(seq)
    for _ in range(max_order):
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        out.append(cur)
    return out


def residue_tail_variation(seq, start_N, period, tail_start_N):
    """For each residue r mod period, compute max variation of seq values
    at N in tail (N >= tail_start_N) with N % period == r. Return list."""
    classes = {r: [] for r in range(period)}
    for i, v in enumerate(seq):
        N = start_N + i
        if N >= tail_start_N:
            classes[N % period].append(v)
    vars_ = []
    for r in range(period):
        vals = classes[r]
        if not vals:
            vars_.append(None)
        else:
            vars_.append(max(vals) - min(vals))
    return vars_


def main():
    N_MAX = 120

    print(f"# Period search: extend to N={N_MAX} and sweep (k, p)")
    print()

    print(f"Enumerating BDI to N={N_MAX}...")
    bdi = count_bdi_n2_all(N_MAX)
    print(f"  c_BDI({N_MAX}) = {bdi[N_MAX]}")

    print(f"Enumerating AII to N={N_MAX}...")
    aii = count_aii_n2_all(N_MAX)
    print(f"  c_AII({N_MAX}) = {aii[N_MAX]}")

    MAX_DIFF = 7
    bdi_d = finite_diffs(bdi, MAX_DIFF)
    aii_d = finite_diffs(aii, MAX_DIFF)

    PERIODS = [1, 2, 3, 4, 6, 8, 9, 12, 18, 24]
    TAIL_START_N = N_MAX // 2  # asymptotic regime
    print(f"Using tail N >= {TAIL_START_N}.")
    print()

    print("Per-residue tail variation (max - min within each residue class). 0 means constant.")
    print()
    for label, diffs in [("BDI", bdi_d), ("AII", aii_d)]:
        print(f"## {label}")
        print(f"{'k':>3} {'p':>4} | max variation across all residues (tail N>={TAIL_START_N})")
        for k in range(1, MAX_DIFF + 1):
            seq = diffs[k]
            start_N = k
            for p in PERIODS:
                vars_ = residue_tail_variation(seq, start_N, p, TAIL_START_N)
                vars_ok = [v for v in vars_ if v is not None]
                if len(vars_ok) < p:
                    continue
                max_v = max(vars_ok)
                marker = "  <-- STABLE" if max_v == 0 else ""
                print(f"{k:>3} {p:>4} | {max_v:>4}{marker}")
        print()

    # Specific tests for AII degree hypotheses
    print()
    print("## AII targeted tests")
    print()
    for k in range(3, 8):
        seq = aii_d[k]
        start_N = k
        for p in [6, 12, 24]:
            # is d^k[N+p] - d^k[N] = 0 in the tail?
            diffs_p = []
            for i in range(len(seq) - p):
                N = start_N + i
                if N < TAIL_START_N:
                    continue
                diffs_p.append((N, seq[i + p] - seq[i]))
            if not diffs_p:
                continue
            non_zero = [d for _, d in diffs_p if d != 0]
            n_zero = len(diffs_p) - len(non_zero)
            n_tot = len(diffs_p)
            print(f"d^{k}(c_AII)[N+{p}] - d^{k}(c_AII)[N]:  {n_zero}/{n_tot} are zero, "
                  f"sample = {diffs_p[:6]}")

    # Conclude: does any (k, p) make d^k bounded periodic?
    # If degree of AII is 4 with period p, then d^4[N+p] - d^4[N] = 0 for large N.
    # If degree is 4 but period is large, this requires p large.
    # If degree > 4, no period works for d^4.

    # Test by trying to fit a quasipolynomial of degree d, period p and
    # checking residuals.
    print()
    print("## Quasipolynomial fit residuals (least squares per residue class)")
    print("## For each (deg, period), fit each residue class to a degree-deg polynomial")
    print("## using only data with N >= TAIL_START_N. Report max abs residual.")
    print()
    import numpy as np
    print(f"{'sys':>3} {'deg':>3} {'period':>6} | max abs residual on tail")
    for label, c in [("BDI", bdi), ("AII", aii)]:
        for deg in [3, 4, 5]:
            for period in [1, 2, 3, 6, 12, 24]:
                if period * (deg + 1) > N_MAX - TAIL_START_N:
                    continue  # not enough data
                max_res = 0.0
                for r in range(period):
                    Ns = [N for N in range(TAIL_START_N, N_MAX + 1) if N % period == r]
                    if len(Ns) < deg + 1:
                        continue
                    Ys = [c[N] for N in Ns]
                    coeffs = np.polyfit(Ns, Ys, deg)
                    preds = np.polyval(coeffs, Ns)
                    res = np.max(np.abs(np.array(Ys) - preds))
                    max_res = max(max_res, res)
                print(f"{label:>3} {deg:>3} {period:>6} | {max_res:>10.4e}")
        print()

    # Save extended counts
    with open(OUT_DIR / "raw_counts_extended.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N", "c_BDI", "c_AII"])
        for N in range(N_MAX + 1):
            w.writerow([N, bdi[N], aii[N]])
    print(f"Extended counts saved to {OUT_DIR / 'raw_counts_extended.csv'}")


if __name__ == "__main__":
    main()
