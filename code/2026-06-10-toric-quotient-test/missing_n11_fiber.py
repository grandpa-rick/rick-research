"""
Day 60 Task 4: For each missing BDI point at N=11, analyze the fiber-
coord requirements.

For a missing g = (M_2, B_1, T_1, B_2, T_2, S), we want to know:
  (a) The T_1 : T_2 ratio required.
  (b) Which AII free-vars COULD in principle hit g, given the BDI cone
      constraints.
  (c) Which pieces of the registry are "close" (off by some integer
      ratio mismatch).

For (c), "close" means: there's a piece pi such that for some AII pt
x, pi(x) differs from g by a small adjustment in one or two coords.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

import numpy as np
import sympy as sp
from collections import defaultdict, Counter
from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, enumerate_bdi_n3, apply_pi

AII_VARS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
            "m_2345", "m_1235", "m_1234"]
BDI_VARS = ["M_2", "B_1", "T_1", "B_2", "T_2", "S"]


def find_missing(N):
    """Find BDI points at level N not hit by any piece."""
    bdi_pts = enumerate_bdi_n3(N)
    aii_pts = enumerate_aii_n3_full(N)
    hit = set()
    for p in aii_pts:
        for pname, spec in ALL_PI.items():
            q = apply_pi(spec, p)
            ok, _ = bdi_feasible_n3(q)
            if not ok: continue
            hit.add((0, q["M_2"], q["B_1"], q["T_1"],
                    q["B_2"], q["T_2"], q["S"]))
    missing = [q for q in bdi_pts if q not in hit]
    return missing, hit


def nearby_hits(g, hit_set, dist=2):
    """Find lattice points within L1 distance 'dist' of g in hit_set."""
    near = []
    for q in hit_set:
        d = sum(abs(g[i] - q[i]) for i in range(1, 7))
        if 0 < d <= dist:
            near.append((d, q))
    near.sort()
    return near[:8]


def main():
    print("=" * 72)
    print("Day 60 Task 4: Missing N=11 fiber-coord analysis")
    print("=" * 72)
    print()

    N = 11
    missing, hit_set = find_missing(N)
    print(f"  BDI lattice pts at N=11: {len(enumerate_bdi_n3(N))}")
    print(f"  Hit under 94-piece registry: {len(hit_set)}")
    print(f"  Missing: {len(missing)}")
    print()

    if not missing:
        print("  ✓ No missing points!")
        return

    print("--- Missing point detail ---")
    for g in missing:
        M_1, M_2, B_1, T_1, B_2, T_2, S = g
        P_1 = 2 * (B_1 - T_1)
        P_2 = P_1 + 2 * (B_2 - T_2)
        print(f"\n  g = (M_2={M_2}, B_1={B_1}, T_1={T_1}, B_2={B_2}, T_2={T_2}, S={S})")
        print(f"      |g| = {sum(g)}, P_1 = {P_1}, P_2 = {P_2}")
        print(f"      Required T_1:T_2 = {T_1}:{T_2}")

        # (a) Look at which pieces have "T_1 = X, T_2 = Y" patterns
        # that could give this ratio.
        # Each piece's T_1, T_2 is a linear combo of AII vars; the
        # ratio T_1:T_2 at a specific AII pt depends on the AII coords.
        # For a piece to be able to give T_1:T_2 = a:b, the supports
        # must permit it.
        # We don't enumerate this carefully; instead, list nearby hits.

        # (c) Nearby hits at dist <= 2.
        near = nearby_hits(g, hit_set, dist=2)
        print(f"      Nearby hits (L1-distance ≤ 2):")
        for d, q in near[:5]:
            _, m2, b1, t1, b2, t2, s = q
            delta = [m2-M_2, b1-B_1, t1-T_1, b2-B_2, t2-T_2, s-S]
            label = []
            for i, name in enumerate(["ΔM_2","ΔB_1","ΔT_1","ΔB_2","ΔT_2","ΔS"]):
                if delta[i] != 0:
                    label.append(f"{name}={delta[i]:+d}")
            print(f"        d={d}: {q[1:]} ({', '.join(label)})")

    # Aggregate: T_1:T_2 ratio distribution
    print()
    print("--- Aggregate T_1:T_2 ratio distribution ---")
    from math import gcd
    ratios = Counter()
    for g in missing:
        t1, t2 = g[3], g[5]
        if t1 == 0 and t2 == 0:
            ratios["both_zero"] += 1
        elif t1 == 0:
            ratios[f"0:{t2}"] += 1
        elif t2 == 0:
            ratios[f"{t1}:0"] += 1
        else:
            d = gcd(t1, t2)
            ratios[f"{t1//d}:{t2//d}"] += 1
    for r, c in ratios.most_common():
        print(f"    {r}: {c}")

    # Identify common patterns
    print()
    print("--- Pattern hypothesis: 'asymmetric T_a edge'? ---")
    # Hypothesis: missing points have one of:
    #   - T_a = 0, T_{a+1} > 0 (asymmetric vanishing)
    #   - T_a > T_{a+1} with specific ratios incompatible with pieces
    edge_cases = Counter()
    for g in missing:
        _, M_2, B_1, T_1, B_2, T_2, S = g
        if T_1 == 0 and T_2 > 0:
            edge_cases["T_1=0, T_2>0"] += 1
        elif T_2 == 0 and T_1 > 0:
            edge_cases["T_1>0, T_2=0"] += 1
        elif T_1 > 0 and T_2 > 0 and T_1 != T_2:
            edge_cases["both>0, T_1 != T_2"] += 1
        elif T_1 > 0 and T_2 > 0 and T_1 == T_2:
            edge_cases["both>0, T_1 = T_2"] += 1
        else:
            edge_cases["both=0"] += 1
    for k, v in edge_cases.most_common():
        print(f"    {k}: {v}")

    # Pattern: high-S patterns
    print()
    print("--- High-S/ M_2 patterns ---")
    for g in missing:
        _, M_2, B_1, T_1, B_2, T_2, S = g
        P_1 = 2 * (B_1 - T_1)
        P_2 = P_1 + 2 * (B_2 - T_2)
        is_S_at_P2 = (S == P_2)
        is_M2_at_P1 = (M_2 == P_1) or (M_2 == P_2)
        flags = []
        if is_S_at_P2: flags.append("S=P_2")
        if is_M2_at_P1: flags.append("M_2=P_a (boundary)")
        if S > 0 and M_2 > 0: flags.append("S,M_2 both pos")
        print(f"    g={g[1:]}: P_1={P_1}, P_2={P_2}, flags={flags}")


if __name__ == "__main__":
    main()
