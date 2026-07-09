"""Day 87 CODE Task 1 — v_2(H_5(a, b, j)) sweep across (a, b, j).

Uses Clio's exact 9-term H_5 polynomial (peer-verified 482/482 at Day 85).
Computes v_2 via SymPy integer arithmetic across:
    a in [5, 30], b in [c, a], j in [0, 12], where non-vacuous.

Records:
  - min v_2 over the sweep and (a, b, j) minimizer
  - top-10 low-v_2 points
  - full CSV of (a, b, j, H_5, v_2)

Expected: beta'(5) = 3, minimizer at (a, b, j) = (3, 0, 2) per Day 85.

Rick, Day 87.
"""
from sympy import Rational, Integer, binomial
import csv


def v2(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


# Clio's exact 9-term H_5 polynomial (see proofs/2026-07-09-d1-c5-structural.md)
# H_5(a, b, j) = sum_{k=0}^{8} h_k^{(5)}(a, b) * C(j, k)

def h5_coeffs(a, b):
    """Return list [h_0, ..., h_8] as integers."""
    h0 = (a+3)*(a+4)*(a+5)*(a+6) * (b+2)*(b+3)*(b+4)*(b+5)
    h1 = -20 * (a+3)*(a+4)*(a+5) * (b+2)*(b+3)*(b+4)
    h2 = -10 * (a+3)*(a+4) * (b+2)*(b+3) * (a*b + a + 2*b - 22)
    h3 = 360 * (a+3) * (b+2) * (a*b + a + 2*b - 2)
    h4 = 240 * (a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a
                + 2*b*b - 34*b - 24)
    h5 = -7200 * (a*b + b - 2)
    h6 = -7200 * (a*b - a - 6)
    h7 = 100800
    h8 = 201600
    return [h0, h1, h2, h3, h4, h5, h6, h7, h8]


def H5(a, b, j):
    hks = h5_coeffs(a, b)
    tot = 0
    for k, hk in enumerate(hks):
        c_jk = int(binomial(j, k))
        tot += hk * c_jk
    return tot


def sweep():
    rows = []
    # H_5 is a polynomial in (a, b, j); evaluate everywhere.
    # Day-85 min at (3, 0, 2) is polynomial-valued despite b < j.
    for a in range(0, 31):
        for b in range(0, a + 1):
            for j in range(0, 13):
                val = H5(a, b, j)
                if val == 0:
                    continue
                rows.append((a, b, j, val, v2(val)))
    return rows


def main():
    rows = sweep()
    rows.sort(key=lambda r: r[4])
    lines = []
    lines.append("=" * 78)
    lines.append("Day 87 CODE Task 1 — v_2(H_5(a, b, j)) sweep")
    lines.append("=" * 78)
    lines.append("")
    lines.append(f"Sample size: {len(rows)} (a in [0..30], b in [0..a], j in [0..12], b>=j)")
    lines.append("")
    min_v = rows[0][4]
    min_pts = [r for r in rows if r[4] == min_v]
    lines.append(f"MIN v_2 = {min_v}")
    lines.append(f"Number of (a, b, j) at min: {len(min_pts)}")
    lines.append("")
    lines.append("First 20 minimizers (a, b, j, H_5, v_2):")
    for r in min_pts[:20]:
        lines.append(f"  a={r[0]:3d}  b={r[1]:3d}  j={r[2]:3d}  H_5={r[3]:>18d}  v_2={r[4]}")
    lines.append("")
    lines.append("Top-30 lowest-v_2 (a, b, j, H_5, v_2):")
    for r in rows[:30]:
        lines.append(f"  a={r[0]:3d}  b={r[1]:3d}  j={r[2]:3d}  H_5={r[3]:>18d}  v_2={r[4]}")
    lines.append("")
    lines.append("Distribution of v_2 (v, count):")
    dist = {}
    for r in rows:
        dist[r[4]] = dist.get(r[4], 0) + 1
    for v in sorted(dist.keys()):
        lines.append(f"  v_2 = {v:3d}: {dist[v]}")
    lines.append("")
    lines.append("Sanity check on Day-85 expected minimizer (a, b, j) = (3, 0, 2):")
    lines.append(f"  H_5(3, 0, 2) = {H5(3, 0, 2)}, v_2 = {v2(H5(3, 0, 2))}")

    out = "\n".join(lines)
    print(out)
    with open("/home/agent/projects/code/2026-07-09-v2-H5-sweep-output.txt", "w") as f:
        f.write(out)

    # Write CSV
    with open("/home/agent/projects/code/2026-07-09-v2-H5-sweep.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["a", "b", "j", "H_5", "v_2"])
        for r in rows:
            w.writerow(r)


if __name__ == "__main__":
    main()
