"""
Task 2: Verify the projection pi_n : AII_(2n-1) -> BDI_n lands in the BDI cone.

Loads candidate pi_n formulas from pi_spec.json. For each lattice point in
the AII polytope at n=2, n=3 (total weight |m| <= 6), compute the candidate
BDI image and check EVERY BDI inequality. Report any failures.

Also report surjectivity / image-coverage statistics so Clio can see how much
of the BDI cone each candidate covers.
"""

import csv
import json
from pathlib import Path

OUT_DIR = Path(__file__).parent
SPEC = OUT_DIR / "pi_spec.json"


# ----- AII enumerators (by hand at small n) -----

def enumerate_aii_n2(N):
    """All non-negative integer 5-tuples (m_2, m_23, m_14, m_123, m_124) with
    m_14 = m_23, m_123 <= m_2, m_124 <= m_23, and sum <= N."""
    pts = []
    for m_2 in range(N + 1):
        for m_23 in range(N + 1):
            m_14 = m_23
            base = m_2 + m_23 + m_14
            if base > N:
                continue
            for m_123 in range(m_2 + 1):
                for m_124 in range(m_23 + 1):
                    if base + m_123 + m_124 <= N:
                        pts.append({
                            "m_2": m_2, "m_23": m_23, "m_14": m_14,
                            "m_123": m_123, "m_124": m_124,
                        })
    return pts


def enumerate_aii_n3(N):
    """Cor 6 (n=3 odd) polytope. Variables m_2, m_23, m_236, m_12356,
    m_12346, m_1235, m_2345 with
        m_12356 + m_1235 <= m_2
        0 <= m_12346 - m_1235 - m_2345 <= m_23
        all >= 0
        total sum <= N.
    """
    pts = []
    for m_2 in range(N + 1):
        for m_23 in range(N + 1 - m_2):
            for m_236 in range(N + 1 - m_2 - m_23):
                # m_12356 in [0, m_2]; m_1235 in [0, m_2 - m_12356]
                for m_12356 in range(m_2 + 1):
                    for m_1235 in range(m_2 - m_12356 + 1):
                        rest0 = m_2 + m_23 + m_236 + m_12356 + m_1235
                        if rest0 > N:
                            continue
                        for m_2345 in range(N - rest0 + 1):
                            lo = m_1235 + m_2345
                            hi_singleton = lo + m_23
                            hi_total = N - rest0 - m_2345
                            hi = min(hi_singleton, hi_total)
                            for m_12346 in range(lo, hi + 1):
                                pts.append({
                                    "m_2": m_2, "m_23": m_23, "m_236": m_236,
                                    "m_12356": m_12356, "m_12346": m_12346,
                                    "m_1235": m_1235, "m_2345": m_2345,
                                })
    return pts


# ----- BDI feasibility checker (parameterised by n) -----

def bdi_feasible_n2(q):
    M_1, B_1, T_1, S = q["M_1"], q["B_1"], q["T_1"], q["S"]
    if any(v < 0 for v in (M_1, B_1, T_1, S)):
        return (False, "non_negativity")
    if M_1 != 0:
        return (False, "L_1: M_1 = 0")
    if T_1 > B_1:
        return (False, "T_1 <= B_1")
    P_1 = 2 * (B_1 - T_1)
    if S > P_1:
        return (False, f"E: S <= P_1 = {P_1}")
    return (True, "")


def bdi_feasible_n3(q):
    M_1, M_2 = q["M_1"], q["M_2"]
    B_1, T_1, B_2, T_2, S = q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"]
    for k, v in q.items():
        if v < 0:
            return (False, f"non-neg: {k}")
    if M_1 != 0:
        return (False, "L_1: M_1 = 0")
    if T_1 > B_1:
        return (False, "T_1 <= B_1")
    P_1 = 2 * (B_1 - T_1)
    P_2 = P_1 + 2 * (B_2 - T_2)
    if P_2 < 0:
        return (False, "P_2 >= 0")
    if M_2 > P_1:
        return (False, f"L_2: M_2 <= P_1 = {P_1}")
    if M_2 > P_2:
        return (False, f"U_2: M_2 <= P_2 = {P_2}")
    if S > P_2:
        return (False, f"E: S <= P_2 = {P_2}")
    return (True, "")


BDI_CHECKERS = {2: bdi_feasible_n2, 3: bdi_feasible_n3}


# ----- Apply pi -----

def apply_pi(spec, aii_point):
    """Compute the BDI image of an AII point using a JSON-spec linear map."""
    out = {}
    for bdi_var, terms in spec["pi"].items():
        s = 0
        for coeff, name in terms:
            s += coeff * aii_point[name]
        out[bdi_var] = s
    return out


# ----- BDI enumeration (for surjectivity stats) -----

def enumerate_bdi_n2(N):
    out = set()
    for B in range(N + 1):
        for T in range(B + 1):
            d = B - T
            for S in range(2 * d + 1):
                if B + T + S <= N:
                    out.add((0, B, T, S))
    return out


def enumerate_bdi_n3(N):
    out = set()
    for B1 in range(N + 1):
        for T1 in range(B1 + 1):
            P1 = 2 * (B1 - T1)
            for B2 in range(N + 1):
                for T2 in range(N + 1):
                    if T2 > B2 + (B1 - T1):  # need P2 >= 0
                        continue
                    P2 = P1 + 2 * (B2 - T2)
                    if P2 < 0:
                        continue
                    if B1 + T1 + B2 + T2 > N:
                        continue
                    for M2 in range(min(P1, P2) + 1):
                        for S in range(P2 + 1):
                            tot = B1 + T1 + M2 + B2 + T2 + S
                            if tot <= N:
                                out.add((0, M2, B1, T1, B2, T2, S))
    return out


# ----- Test driver -----

def run_check(spec_name, spec, N):
    n = spec["n"]
    print(f"\n=== {spec_name} at |m| <= {N} ===")
    print(f"Note: {spec.get('note', '')}")

    if n == 2:
        aii_pts = enumerate_aii_n2(N)
        bdi_check = bdi_feasible_n2
    elif n == 3:
        aii_pts = enumerate_aii_n3(N)
        bdi_check = bdi_feasible_n3
    else:
        raise ValueError(f"unsupported n={n}")

    n_aii = len(aii_pts)
    print(f"AII lattice points enumerated: {n_aii}")
    bad = []
    image = set()
    for p in aii_pts:
        q = apply_pi(spec, p)
        ok, reason = bdi_check(q)
        if not ok:
            bad.append((p, q, reason))
        # for surjectivity stats
        if n == 2:
            image.add((q["M_1"], q["B_1"], q["T_1"], q["S"]))
        elif n == 3:
            image.add((q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                       q["B_2"], q["T_2"], q["S"]))

    n_bad = len(bad)
    print(f"  Image lands in BDI cone: {n_aii - n_bad}/{n_aii} "
          f"({100*(n_aii-n_bad)/n_aii:.1f}%)")
    if bad:
        print(f"  FAILURES: {n_bad}")
        # show first 5 failures
        for p, q, reason in bad[:5]:
            print(f"    AII {p}")
            print(f"    -> BDI {q}")
            print(f"    failed: {reason}")
        # tally failure reasons
        from collections import Counter
        c = Counter(reason for _, _, reason in bad)
        print("  Failure reasons:")
        for r, k in c.most_common():
            print(f"    {k:5d} x {r}")

    # surjectivity stats
    if n == 2:
        bdi_pts = enumerate_bdi_n2(N)
    else:
        bdi_pts = enumerate_bdi_n3(N)
    # We only want to count image elements that are in the BDI lattice of
    # weight <= N; image may include points beyond it.
    image_in_window = image & bdi_pts
    covered = len(image_in_window)
    print(f"  BDI lattice points (|.| <= {N}): {len(bdi_pts)}")
    print(f"  In image and in window: {covered} "
          f"({100*covered/len(bdi_pts):.1f}% coverage)")

    return {
        "spec": spec_name,
        "N": N,
        "n_aii": n_aii,
        "n_bad": n_bad,
        "n_bdi": len(bdi_pts),
        "covered": covered,
    }


def main():
    with open(SPEC) as f:
        specs = json.load(f)
    specs = {k: v for k, v in specs.items() if not k.startswith("_")}

    summary = []
    for name, spec in specs.items():
        # CODE.md asks for |m| <= 6 at both n=2, n=3
        summary.append(run_check(name, spec, N=6))

    # Higher N for the corrected n=2 to cross-check verify_pi_v2.py
    for name in ("pi_2_corrected", "pi_2_strawman"):
        summary.append(run_check(name, specs[name], N=20))

    # CSV
    out_csv = OUT_DIR / "pi_verification_results.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["spec", "N", "n_aii", "n_bad",
                    "n_bdi", "covered", "coverage_pct"])
        for s in summary:
            w.writerow([s["spec"], s["N"], s["n_aii"], s["n_bad"],
                        s["n_bdi"], s["covered"],
                        round(100 * s["covered"] / s["n_bdi"], 2)])
    print(f"\nSummary CSV: {out_csv}")


if __name__ == "__main__":
    main()
