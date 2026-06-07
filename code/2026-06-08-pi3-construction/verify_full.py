"""
Verification of pi_3 candidate projections AGAINST THE FULL 9-VAR POLYTOPE
(Theorem 6, n=3 odd, ALL Cor 6 constraints including Main_3 and the variable
m_1234, m_23456 that task2_verify_pi.py omitted).

Variables: m_2, m_23, m_236, m_23456, m_12356, m_12346, m_2345, m_1235, m_1234
Constraints:
  Main_2: m_12356 + m_1235 <= m_2
  Main_3: m_12346 + m_1234 <= m_23
  Singleton: m_1235 + m_2345 <= m_12346 <= m_23 + m_1235 + m_2345
  all >= 0
  m_23456 free (no Cor 6 constraint)

Derived: m_1234 + m_1235 + m_2345 <= m_23 (from Main_3 + Singleton LB).

BDI: (M_1=0, M_2, B_1, T_1, B_2, T_2, S) with
  T_a <= B_a, M_2 <= P_1, M_2 <= P_2, S <= P_2
  P_1 = 2(B_1-T_1), P_2 = P_1 + 2(B_2-T_2)
"""

import csv
import json
from pathlib import Path


OUT_DIR = Path(__file__).parent


def enumerate_aii_n3_full(N):
    """Enumerate all 9-tuples (m_2, m_23, m_236, m_23456, m_12356, m_12346,
    m_2345, m_1235, m_1234) satisfying full Cor 6 + Main_3 with sum <= N."""
    pts = []
    for m_2 in range(N + 1):
        for m_23 in range(N + 1 - m_2):
            for m_236 in range(N + 1 - m_2 - m_23):
                rest1 = N - m_2 - m_23 - m_236
                # Main_2: m_12356 + m_1235 <= m_2
                for m_12356 in range(min(m_2, rest1) + 1):
                    for m_1235 in range(min(m_2 - m_12356, rest1 - m_12356) + 1):
                        rest2 = rest1 - m_12356 - m_1235
                        # Main_3: m_12346 + m_1234 <= m_23
                        for m_12346 in range(min(m_23, rest2) + 1):
                            for m_1234 in range(min(m_23 - m_12346,
                                                     rest2 - m_12346) + 1):
                                rest3 = rest2 - m_12346 - m_1234
                                # Singleton: m_2345 in [max(0, m_12346 - m_1235 - m_23),
                                #                       min(rest3, m_12346 - m_1235)]
                                lo = max(0, m_12346 - m_1235 - m_23)
                                hi = min(rest3, m_12346 - m_1235)
                                if hi < lo:
                                    continue
                                for m_2345 in range(lo, hi + 1):
                                    rest4 = rest3 - m_2345
                                    # m_23456 free, [0, rest4]
                                    for m_23456 in range(rest4 + 1):
                                        pts.append({
                                            "m_2": m_2, "m_23": m_23,
                                            "m_236": m_236, "m_23456": m_23456,
                                            "m_12356": m_12356,
                                            "m_12346": m_12346,
                                            "m_2345": m_2345,
                                            "m_1235": m_1235,
                                            "m_1234": m_1234,
                                        })
    return pts


def bdi_feasible_n3(q):
    """Check BDI feasibility. q is a 7-tuple/dict with M_1, M_2, B_1, T_1,
    B_2, T_2, S."""
    for k, v in q.items():
        if v < 0:
            return (False, f"non-neg: {k}")
    if q["M_1"] != 0:
        return (False, "L_1: M_1 = 0")
    if q["T_1"] > q["B_1"]:
        return (False, "T_1 <= B_1")
    if q["T_2"] > q["B_2"]:
        return (False, "T_2 <= B_2")
    P_1 = 2 * (q["B_1"] - q["T_1"])
    P_2 = P_1 + 2 * (q["B_2"] - q["T_2"])
    if P_2 < 0:
        return (False, "P_2 >= 0")
    if q["M_2"] > P_1:
        return (False, f"L_2: M_2 <= P_1 = {P_1}")
    if q["M_2"] > P_2:
        return (False, f"U_2: M_2 <= P_2 = {P_2}")
    if q["S"] > P_2:
        return (False, f"E: S <= P_2 = {P_2}")
    return (True, "")


def enumerate_bdi_n3(N):
    """All 7-tuples (M_1=0, M_2, B_1, T_1, B_2, T_2, S) feasible with sum <= N."""
    out = set()
    for B_1 in range(N + 1):
        for T_1 in range(B_1 + 1):
            P_1 = 2 * (B_1 - T_1)
            for B_2 in range(N + 1):
                for T_2 in range(B_2 + 1):
                    P_2 = P_1 + 2 * (B_2 - T_2)
                    if P_2 < 0:
                        continue
                    base = B_1 + T_1 + B_2 + T_2
                    if base > N:
                        continue
                    for M_2 in range(min(P_1, P_2) + 1):
                        for S in range(P_2 + 1):
                            if base + M_2 + S > N:
                                continue
                            out.add((0, M_2, B_1, T_1, B_2, T_2, S))
    return out


# Candidate projections. Each: {var: [(coeff, aii_var), ...]} mapping
# AII point -> BDI point (output tuple in order M_1, M_2, B_1, T_1, B_2, T_2, S).

PROJECTIONS = {
    "section_4_strawman": {
        "M_1": [], "M_2": [],
        "B_1": [(1, "m_2"), (1, "m_2345")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(1, "m_12346"), (2, "m_1234")],
    },
    # Augmented: include m_23456 in B_1 and m_12356 as M_2 to recover more BDI.
    "section_4_aug_M2": {
        "M_1": [], "M_2": [(1, "m_12356")],
        "B_1": [(1, "m_2"), (1, "m_2345"), (1, "m_23456")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235"), (1, "m_236")],
        "T_2": [(1, "m_1235"), (1, "m_236")],
        "S":   [(1, "m_12346"), (2, "m_1234")],
    },
    # Doubled-Σ candidate (replaces "m_1234" in §4 with Σ = m_12346 - m_1235 - m_2345).
    "doubled_Sigma": {
        "M_1": [], "M_2": [],
        "B_1": [(1, "m_2"), (1, "m_2345")],
        "T_1": [(1, "m_2345")],
        "B_2": [(1, "m_23"), (1, "m_1235")],
        "T_2": [(1, "m_1235")],
        "S":   [(3, "m_12346"), (-2, "m_1235"), (-2, "m_2345")],
    },
}


def apply_pi(spec, p):
    out = {}
    for var, terms in spec.items():
        s = 0
        for coeff, name in terms:
            s += coeff * p[name]
        out[var] = s
    return out


def run_check(name, spec, N):
    print(f"\n=== {name} at |m| <= {N} (FULL 9-var polytope) ===")
    aii_pts = enumerate_aii_n3_full(N)
    n_aii = len(aii_pts)
    print(f"AII lattice pts: {n_aii}")
    bad = []
    image = set()
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, reason = bdi_feasible_n3(q)
        if not ok:
            bad.append((p, q, reason))
        image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                   q["B_2"], q["T_2"], q["S"]))

    n_bad = len(bad)
    print(f"  Land-in-cone: {n_aii - n_bad}/{n_aii} ({100*(n_aii-n_bad)/n_aii:.1f}%)")
    if bad:
        from collections import Counter
        c = Counter(r for _, _, r in bad)
        for r, k in c.most_common(5):
            print(f"     {k:5d} x {r}")
        for p, q, reason in bad[:3]:
            print(f"     witness AII={p}")
            print(f"             BDI={q} failed: {reason}")

    bdi_pts = enumerate_bdi_n3(N)
    image_in_window = image & bdi_pts
    print(f"  BDI lattice pts (|.|<={N}): {len(bdi_pts)}")
    cov = len(image_in_window)
    print(f"  Coverage: {cov}/{len(bdi_pts)} = {100*cov/len(bdi_pts):.1f}%")
    return {"name": name, "N": N, "n_aii": n_aii, "n_bad": n_bad,
            "n_bdi": len(bdi_pts), "covered": cov}


def main():
    summary = []
    for N in [4, 5, 6]:
        for name, spec in PROJECTIONS.items():
            summary.append(run_check(name, spec, N))

    out_csv = OUT_DIR / "verify_full_results.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "N", "n_aii", "n_bad", "n_bdi", "covered",
                    "coverage_pct"])
        for s in summary:
            w.writerow([s["name"], s["N"], s["n_aii"], s["n_bad"],
                        s["n_bdi"], s["covered"],
                        round(100 * s["covered"] / s["n_bdi"], 2)])
    print(f"\nWrote {out_csv}")


if __name__ == "__main__":
    main()
