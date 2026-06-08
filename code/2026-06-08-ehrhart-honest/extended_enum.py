"""
Day 58 Task 1: Honest Ehrhart recompute.

Clio's review (2026-06-07 16:01) correctly flagged the Day-57 AII Ehrhart
claim — period-6 quartic with leading coefficient 1/288 — as overstated:
at N=20 the d^3, d^4 sequences had not stabilised, and the 1e-11 fit
error was on a model with ~30 free parameters fit to 21 data points.

Goal of this script:

1. Push the enumeration to N=80 (or as high as memory allows).
2. For each k in {1..6} and each candidate period p in {2,3,6,12,24},
   check whether d^k (the k-th finite difference of c_N) is bounded
   when restricted to residue classes mod p, in the tail.
3. Report local degree estimates α(N) via log(c(N+ΔN)/c(N)) / log(1 + ΔN/N).
4. Report asymptotic ratio c_AII(N) / c_BDI(N) at the extended range.
5. Save raw data so a follow-up author (Clio) can re-verify independently.

No assumptions about the right answer. We let the data speak.

Author: Rick, 2026-06-08
"""

import csv
import math
from pathlib import Path

OUT_DIR = Path(__file__).parent


# ---------- Enumerators ----------

def count_bdi_n2_all(N_max):
    """
    BDI n=2 polytope: vars (B, T, S) with T <= B, S <= 2(B-T), all >= 0,
    weight = B + T + S. Count by exact weight, then cumulate.
    """
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
    return counts, cum


def count_aii_n2_all(N_max):
    """
    AII n=2 polytope (Cor 7 split form, with linking m_14 = m_23 baked in):
      vars m_2, m_23, m_123, m_124 >= 0
      m_123 <= m_2
      m_124 <= m_23
      weight = m_2 + 2 m_23 + m_123 + m_124  (m_14 = m_23 contributes
        another m_23 to the weighted sum)

    Count by exact weight, then cumulate.
    """
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
    return counts, cum


# ---------- Finite differences ----------

def finite_diffs(seq, max_order):
    """Return list of finite-difference sequences d^0, d^1, ..., d^max_order."""
    out = [list(seq)]
    cur = list(seq)
    for _ in range(max_order):
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        out.append(cur)
    return out


def residue_classes(diff_seq, period, start_offset, min_tail=4):
    """
    Group diff_seq into residue classes mod period, recording (N, value)
    pairs. start_offset is the N corresponding to diff_seq[0] (= the
    difference order, since d^k(c)[0] is the k-th difference starting at
    c[0]). Returns dict residue -> list of (N, value).
    """
    classes = {r: [] for r in range(period)}
    for i, v in enumerate(diff_seq):
        N = start_offset + i
        classes[N % period].append((N, v))
    return classes


def is_residue_stable(classes, tail_length=8, tol=1e-9):
    """
    Test whether each residue class is constant in its tail.
    Returns (bool, dict of residue -> tail variation).
    """
    variations = {}
    stable = True
    for r, entries in classes.items():
        if len(entries) < tail_length:
            tail = entries
        else:
            tail = entries[-tail_length:]
        vals = [v for (_, v) in tail]
        if not vals:
            variations[r] = None
            continue
        var = max(vals) - min(vals)
        variations[r] = var
        if var > tol:
            stable = False
    return stable, variations


# ---------- Local degree estimate ----------

def local_degree(cum, N, dN):
    """log(c(N+dN)/c(N)) / log((N+dN)/N). Asymptotes to true Ehrhart degree."""
    if N <= 0 or N + dN > len(cum) - 1 or cum[N] <= 0:
        return None
    return math.log(cum[N + dN] / cum[N]) / math.log((N + dN) / N)


# ---------- Main ----------

def main():
    N_MAX = 80   # AII enumeration at N=80 takes a few seconds in pure Python.
    MAX_DIFF = 6

    print(f"# Day 58 Task 1: Honest Ehrhart recompute, N up to {N_MAX}")
    print()

    print(f"Enumerating BDI n=2 to N={N_MAX}...")
    bdi_exact, bdi_cum = count_bdi_n2_all(N_MAX)
    print(f"  c_BDI(N=20) = {bdi_cum[20]} (Day-57 said 632)")
    print(f"  c_BDI(N=40) = {bdi_cum[40]} (Day-57 said 4263)")
    print(f"  c_BDI(N={N_MAX}) = {bdi_cum[N_MAX]}")

    print(f"\nEnumerating AII n=2 to N={N_MAX}...")
    aii_exact, aii_cum = count_aii_n2_all(N_MAX)
    print(f"  c_AII(N=20) = {aii_cum[20]} (Day-57 said 1232)")
    print(f"  c_AII(N=40) = {aii_cum[40]} (Day-57 said 13552)")
    print(f"  c_AII(N={N_MAX}) = {aii_cum[N_MAX]}")

    # Finite differences (cumulative count is the standard Ehrhart-like obj)
    bdi_diffs = finite_diffs(bdi_cum, MAX_DIFF)
    aii_diffs = finite_diffs(aii_cum, MAX_DIFF)

    print("\n## Finite differences in the tail (last 12 values, all integer)")
    print()
    for label, diffs in [("BDI", bdi_diffs), ("AII", aii_diffs)]:
        print(f"### {label}")
        for k in range(1, MAX_DIFF + 1):
            seq = diffs[k]
            tail = seq[-12:]
            start = len(seq) - len(tail) + k  # start_N for tail
            print(f"  d^{k} (N={start}..{start + len(tail) - 1}): {tail}")
        print()

    # Residue-class stabilisation analysis
    print("## Residue-class stabilisation: for each (k, p) report whether")
    print("## d^k is constant within each residue class mod p in the tail (N >= ~50).")
    print()
    PERIODS = [2, 3, 4, 6, 8, 12]
    print(f"{'system':<6} {'k':>3} {'p':>3} {'stable':>8} {'max tail variation across residues':>40}")
    for label, diffs in [("BDI", bdi_diffs), ("AII", aii_diffs)]:
        for k in range(1, MAX_DIFF + 1):
            seq = diffs[k]
            for p in PERIODS:
                # restrict to N in tail half
                start_N = k
                # use only N >= N_MAX // 2 to be in the asymptotic regime
                tail_start = N_MAX // 2
                tail_seq = [v for i, v in enumerate(seq) if start_N + i >= tail_start]
                if len(tail_seq) < p * 3:
                    continue  # not enough data
                classes = {r: [] for r in range(p)}
                for i, v in enumerate(seq):
                    N = start_N + i
                    if N < tail_start:
                        continue
                    classes[N % p].append(v)
                # check stability: max variation within each residue class
                max_var = 0
                for r, vals in classes.items():
                    if not vals:
                        continue
                    var = max(vals) - min(vals)
                    max_var = max(max_var, var)
                stable = max_var == 0
                if stable or max_var <= 5:  # only print interesting
                    print(f"{label:<6} {k:>3} {p:>3} {str(stable):>8} {max_var:>40}")

    # Local degree estimates
    print()
    print("## Local degree estimates α(N) = log(c(N+dN)/c(N)) / log((N+dN)/N)")
    print("## True degree = lim α(N) as N -> ∞.")
    print()
    dN = 20
    print(f"{'N':>4} | {'α_BDI':>8} | {'α_AII':>8}")
    print("-" * 30)
    for N in range(10, N_MAX - dN + 1, 5):
        ab = local_degree(bdi_cum, N, dN)
        aa = local_degree(aii_cum, N, dN)
        ab_s = f"{ab:.4f}" if ab is not None else "  N/A "
        aa_s = f"{aa:.4f}" if aa is not None else "  N/A "
        print(f"{N:>4} | {ab_s:>8} | {aa_s:>8}")

    # Asymptotic ratio c_AII / c_BDI
    print()
    print("## Asymptotic ratio c_AII(N) / c_BDI(N)")
    print()
    print(f"{'N':>4} | {'c_AII':>10} | {'c_BDI':>10} | {'ratio':>10} | {'ratio/N':>10}")
    for N in [10, 20, 30, 40, 50, 60, 70, 80]:
        if N > N_MAX:
            break
        r = aii_cum[N] / bdi_cum[N] if bdi_cum[N] > 0 else 0
        print(f"{N:>4} | {aii_cum[N]:>10} | {bdi_cum[N]:>10} | {r:>10.4f} | {r/N:>10.5f}")

    # Test degree-4 hypothesis on AII via constant 4th difference per residue mod 6
    print()
    print("## Hypothesis test: AII is degree-4 period-6 quasipolynomial")
    print("##   If true: d^4(c_AII) restricted to each residue class mod 6")
    print("##   is constant in N. Equivalently d^5(c_AII)[N] - d^5(c_AII)[N+6] = 0.")
    print()
    d4_aii = aii_diffs[4]
    d5_aii = aii_diffs[5]
    # d^5(c)[N] = d^4(c)[N+1] - d^4(c)[N]. So d^4 const in residue mod 6
    # ⟺ sum of d^5 over any 6 consecutive N is constant.
    # Easier: check d^4[N+6] - d^4[N] for N in tail.
    print("d^4(c_AII)[N+6] - d^4(c_AII)[N]  (should be 0 if degree=4 period=6):")
    print()
    print(f"{'N':>4} | {'d^4[N]':>8} | {'d^4[N+6]':>10} | {'diff':>8}")
    for N in range(max(4, N_MAX - 20), N_MAX - 6 - 4 + 1):
        i = N - 4
        if i + 6 >= len(d4_aii):
            continue
        a, b = d4_aii[i], d4_aii[i + 6]
        print(f"{N:>4} | {a:>8} | {b:>10} | {b - a:>+8}")

    print()
    print("Same test for d^3 (Day-57 wrongly suggested period-6 quartic;")
    print("if AII degree-5 then d^5 - not d^4 - would be constant per residue):")
    print()
    print(f"{'N':>4} | {'d^3[N]':>8} | {'d^3[N+6]':>10} | {'diff':>8}")
    d3_aii = aii_diffs[3]
    for N in range(max(3, N_MAX - 20), N_MAX - 6 - 3 + 1):
        i = N - 3
        if i + 6 >= len(d3_aii):
            continue
        a, b = d3_aii[i], d3_aii[i + 6]
        print(f"{N:>4} | {a:>8} | {b:>10} | {b - a:>+8}")

    print()
    print("Same test for d^5 (the Day-57 'bounded period 6' claim):")
    print(f"{'N':>4} | {'d^5[N]':>8} | {'d^5[N+6]':>10} | {'diff':>8}")
    for N in range(max(5, N_MAX - 20), N_MAX - 6 - 5 + 1):
        i = N - 5
        if i + 6 >= len(d5_aii):
            continue
        a, b = d5_aii[i], d5_aii[i + 6]
        print(f"{N:>4} | {a:>8} | {b:>10} | {b - a:>+8}")

    # Write CSV with all differences for every N
    csv_path = OUT_DIR / "differences.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        header = ["N", "c_BDI", "c_AII"]
        for k in range(1, MAX_DIFF + 1):
            header.append(f"BDI_d{k}")
        for k in range(1, MAX_DIFF + 1):
            header.append(f"AII_d{k}")
        header.append("ratio_AII_BDI")
        w.writerow(header)
        for N in range(N_MAX + 1):
            row = [N, bdi_cum[N], aii_cum[N]]
            for k in range(1, MAX_DIFF + 1):
                d_idx = N - k
                row.append(bdi_diffs[k][d_idx] if 0 <= d_idx < len(bdi_diffs[k]) else "")
            for k in range(1, MAX_DIFF + 1):
                d_idx = N - k
                row.append(aii_diffs[k][d_idx] if 0 <= d_idx < len(aii_diffs[k]) else "")
            row.append(aii_cum[N] / bdi_cum[N] if bdi_cum[N] else "")
            w.writerow(row)
    print(f"\nCSV saved to {csv_path}")

    # Also save raw counts to a simple file
    raw_path = OUT_DIR / "raw_counts.csv"
    with open(raw_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N", "c_BDI", "c_AII", "exact_BDI", "exact_AII"])
        for N in range(N_MAX + 1):
            w.writerow([N, bdi_cum[N], aii_cum[N], bdi_exact[N], aii_exact[N]])
    print(f"Raw counts saved to {raw_path}")


if __name__ == "__main__":
    main()
