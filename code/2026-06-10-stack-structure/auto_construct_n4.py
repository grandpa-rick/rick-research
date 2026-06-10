"""
Day 62 CODE Task 2 — Single-column lemma at n=4.

The Day-59 lemma at n=3:
    For each g in P^BDI_3 cap Z^7, define pi^(g)(a) := a[m_23456] * g.
    Then pi^(g) is a valid integer-PL piece (BDI is a cone; m_23456 is free).

m_23456 is "free" at n=3 because it's the long[1] variable: the only long
that doesn't appear in any Main_i inequality and isn't in any linking equation.

Conjecture at n=4: long[1] is similarly the unique free variable. The single-
column piece pi^(g)(a) := a[long[1]] * g is valid for any g in P^BDI_4.

This script:
  1. Verifies that long[1] is free at n=4 (no Main_i, no linking eq).
  2. Enumerates AII at n=4, N <= 10.
  3. Enumerates BDI at n=4, N <= 10.
  4. For 100 sampled g in BDI lattice, constructs pi^(g) and verifies that
     for every AII lattice point p with long[1](p) >= 0, the image is in BDI.
     (This is mostly a sanity check — the proof is trivial.)
  5. Coverage statistic: the existential form is trivially 100% (each q is
     hit by its own pi^(q) at preimage (long[1]=1, rest=0)). We instead
     report the "1-column saturation": how many distinct BDI lattice points
     at N <= 10 are hit by SOME single-column piece pi^(g) with |g| <= G_max,
     for various G_max — measures the speed of saturation.
"""

import sys
import random
from pathlib import Path
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational')

import numpy as np
from dim_gap_verify import aii_structure


# ------------------------------------------------------------------
# Step 1: verify long[1] is free at n=4
# ------------------------------------------------------------------

def verify_long1_free(n):
    struct = aii_structure(n)
    long1_idx = struct['long_idx'][0]
    appears_ineq = False
    for row in struct['A_ineq']:
        if row[long1_idx] != 0:
            appears_ineq = True
            break
    appears_eq = False
    for row in struct['A_eq']:
        if row[long1_idx] != 0:
            appears_eq = True
            break
    return {
        'long1_var': struct['vars'][long1_idx],
        'long1_idx': long1_idx,
        'appears_in_ineq': appears_ineq,
        'appears_in_eq': appears_eq,
        'is_free': not (appears_ineq or appears_eq),
    }


# ------------------------------------------------------------------
# Step 2: AII enumeration at n=4
# ------------------------------------------------------------------

def enumerate_aii(n, N):
    """Enumerate AII lattice points at level <= N.
    Returns list of np.array(n_vars) tuples."""
    struct = aii_structure(n)
    n_vars = struct['n_vars']
    A_ineq = struct['A_ineq']
    b_ineq = struct['b_ineq']
    A_eq = struct['A_eq']
    b_eq = struct['b_eq']

    pts = []

    def gen(remaining, depth, current):
        if depth == n_vars:
            x = np.array(current, dtype=int)
            if A_ineq.shape[0] and not np.all(A_ineq @ x <= b_ineq + 1e-9):
                return
            if A_eq.shape[0] and not np.all(np.abs(A_eq @ x - b_eq) < 1e-9):
                return
            pts.append(tuple(current))
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()

    gen(N, 0, [])
    return pts, struct


# ------------------------------------------------------------------
# Step 3: BDI enumeration at n=4
# ------------------------------------------------------------------

def enumerate_bdi_n4(N):
    """Enumerate BDI lattice points at n=4, level <= N.
    Variables: M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S.
    Constraints: T_a <= B_a; P_a = P_{a-1} + 2(B_a - T_a) >= 0;
                 M_2 <= min(P_1, P_2); M_3 <= min(P_2, P_3); S <= P_3."""
    pts = set()
    for B_1 in range(N + 1):
        for T_1 in range(B_1 + 1):
            P_1 = 2 * (B_1 - T_1)
            for B_2 in range(N + 1 - B_1 - T_1):
                for T_2 in range(B_2 + 1):
                    P_2 = P_1 + 2 * (B_2 - T_2)
                    if P_2 < 0:
                        continue
                    for B_3 in range(N + 1 - B_1 - T_1 - B_2 - T_2):
                        for T_3 in range(B_3 + 1):
                            P_3 = P_2 + 2 * (B_3 - T_3)
                            if P_3 < 0:
                                continue
                            base = B_1 + T_1 + B_2 + T_2 + B_3 + T_3
                            if base > N:
                                continue
                            M2_max = min(P_1, P_2)
                            M3_max = min(P_2, P_3)
                            for M_2 in range(M2_max + 1):
                                if base + M_2 > N:
                                    break
                                for M_3 in range(M3_max + 1):
                                    if base + M_2 + M_3 > N:
                                        break
                                    for S in range(P_3 + 1):
                                        if base + M_2 + M_3 + S > N:
                                            break
                                        pts.add((M_2, M_3, B_1, T_1, B_2, T_2,
                                                 B_3, T_3, S))
    return pts


def bdi_n4_feasible(q):
    """Check BDI feasibility at n=4. q = (M_2, M_3, B_1, T_1, B_2, T_2,
    B_3, T_3, S)."""
    M_2, M_3, B_1, T_1, B_2, T_2, B_3, T_3, S = q
    if any(v < 0 for v in q):
        return False
    if T_1 > B_1 or T_2 > B_2 or T_3 > B_3:
        return False
    P_1 = 2 * (B_1 - T_1)
    P_2 = P_1 + 2 * (B_2 - T_2)
    P_3 = P_2 + 2 * (B_3 - T_3)
    if P_2 < 0 or P_3 < 0:
        return False
    if M_2 > P_1 or M_2 > P_2:
        return False
    if M_3 > P_2 or M_3 > P_3:
        return False
    if S > P_3:
        return False
    return True


# ------------------------------------------------------------------
# Step 4: Single-column piece construction & verification
# ------------------------------------------------------------------

def piece_image_on_aii(g, aii_pts, struct):
    """For piece pi^(g)(a) := a[long[1]] * g, compute the image over
    aii_pts. Each image point is k*g for k = long[1](p) >= 0.
    Returns dict {bdi_pt: count_of_preimages}."""
    long1_idx = struct['long_idx'][0]
    image_counts = {}
    for p in aii_pts:
        k = p[long1_idx]
        q = tuple(k * g_i for g_i in g)
        # k=0 gives (0,...,0) which is in BDI ✓; k>=1 gives k*g.
        if not bdi_n4_feasible(q):
            return None, f"piece pi^(g={g}) at p={p} gives infeasible q={q}"
        image_counts[q] = image_counts.get(q, 0) + 1
    return image_counts, None


def main():
    print("="*70)
    print("Day 62 CODE Task 2 — Single-column lemma at n=4")
    print("="*70)

    # Step 1: verify long[1] is free at n=4
    info = verify_long1_free(4)
    print(f"\nStep 1: 'free variable' check at n=4")
    print(f"  long[1] = '{info['long1_var']}', idx = {info['long1_idx']}")
    print(f"  appears in any Main_i inequality? {info['appears_in_ineq']}")
    print(f"  appears in linking equation?      {info['appears_in_eq']}")
    print(f"  -> IS FREE: {info['is_free']}")
    if not info['is_free']:
        print("\nFAIL: long[1] is not free at n=4; lemma does not extend trivially.")
        sys.exit(1)

    # Also at n=3 for sanity
    info_n3 = verify_long1_free(3)
    print(f"\n  Sanity at n=3: long[1] = '{info_n3['long1_var']}', free = {info_n3['is_free']}")
    print(f"   (Should be m_23456 morally; we labelled it long[1].)")

    # Step 2: enumerate AII at n=4
    N = 10
    print(f"\nStep 2: AII enumeration at n=4, N <= {N}")
    aii_pts, struct = enumerate_aii(4, N)
    print(f"  # AII lattice pts at level <= {N}: {len(aii_pts)}")
    long1_idx = struct['long_idx'][0]
    long1_vals = [p[long1_idx] for p in aii_pts]
    print(f"  long[1] values range: 0..{max(long1_vals)}")

    # Step 3: enumerate BDI at n=4
    print(f"\nStep 3: BDI enumeration at n=4, N <= {N}")
    bdi_pts = enumerate_bdi_n4(N)
    print(f"  # BDI lattice pts at level <= {N}: {len(bdi_pts)}")

    # Step 4: pick 100 random g in BDI, build pi^(g), verify land-in-cone
    print(f"\nStep 4: build single-column pieces for 100 sample g in BDI lattice")
    rng = random.Random(42)
    bdi_list = sorted(bdi_pts)
    if len(bdi_list) >= 100:
        sample = rng.sample(bdi_list, 100)
    else:
        sample = bdi_list
    n_ok = 0
    n_fail = 0
    image_sizes = []
    for g in sample:
        result, err = piece_image_on_aii(g, aii_pts, struct)
        if err is not None:
            n_fail += 1
            print(f"  FAIL: {err}")
            if n_fail >= 5:
                break
        else:
            n_ok += 1
            image_sizes.append(len(result))
    print(f"  OK   pieces (land in BDI for all AII pts): {n_ok}/{len(sample)}")
    print(f"  FAIL pieces:                                {n_fail}/{len(sample)}")
    if image_sizes:
        print(f"  Image size (distinct BDI pts hit per piece):"
              f" min={min(image_sizes)}, mean={sum(image_sizes)/len(image_sizes):.2f},"
              f" max={max(image_sizes)}")

    # Step 5: coverage statistic
    # Existential: every q in BDI is hit by pi^(q). So 100% trivially.
    # Saturation: how many distinct BDI lattice points at N <= 10 are
    # hit by single-column pieces pi^(g) with |g| <= G for G=1..10?
    print(f"\nStep 5: 1-column saturation analysis")
    print(f"  For each G in 1..{N}, count BDI lattice pts at level <= {N}")
    print(f"  hit by SOME pi^(g) with |g| <= G.")
    print()

    # Pre-compute image of each pi^(g) = {k*g : 0 <= k, |kg| <= N}
    # Only nonzero g contribute interesting points.
    L1_max = max(long1_vals)
    print(f"  {'G':>3} | {'|g|<=G':>8} | {'#hit':>6} | {'#BDI_target':>11} | {'coverage':>9}")
    print(f"  ---+----------+--------+-------------+----------")
    g_at_or_below = {G: [g for g in bdi_pts if sum(g) <= G] for G in range(1, N+1)}

    # Targets: BDI pts at level <= N
    target = bdi_pts

    hit_total = set()
    cum_g = []
    rows = []
    for G in range(1, N+1):
        new_g = [g for g in g_at_or_below[G] if g not in g_at_or_below.get(G-1, set())]
        new_g_set = set(g_at_or_below[G])
        for g in new_g_set:
            # k*g for k=0..L1_max with |k*g| <= N
            sum_g = sum(g)
            if sum_g == 0:
                hit_total.add(g)  # just origin
                continue
            k_max = min(L1_max, N // sum_g if sum_g > 0 else 0)
            for k in range(0, k_max + 1):
                q = tuple(k * x for x in g)
                if sum(q) <= N:
                    hit_total.add(q)
        cov = 100 * len(hit_total & target) / len(target)
        rows.append((G, len(g_at_or_below[G]), len(hit_total & target),
                     len(target), cov))
        print(f"  {G:>3} | {len(g_at_or_below[G]):>8} | "
              f"{len(hit_total & target):>6} | {len(target):>11} | {cov:>8.2f}%")

    print("\nNote: at G=N=10, single-column pieces with |g| <= 10 hit every")
    print("BDI lattice point at level <= 10 (since each q is hit by pi^(q)).")
    print("This confirms the existential form of OQ-PI3-GROWTH at n=4, N <= 10.")

    # Write a small JSON summary
    import json
    out = {
        'verify_long1_free_n4': info,
        'verify_long1_free_n3': info_n3,
        'n': 4,
        'N': N,
        'n_aii_pts': len(aii_pts),
        'n_bdi_pts': len(bdi_pts),
        'sample_pieces': len(sample),
        'pieces_ok': n_ok,
        'pieces_fail': n_fail,
        'image_sizes': {
            'min': min(image_sizes) if image_sizes else 0,
            'mean': sum(image_sizes)/len(image_sizes) if image_sizes else 0,
            'max': max(image_sizes) if image_sizes else 0,
        },
        'saturation_table': [
            {'G': r[0], 'n_g_le_G': r[1], 'n_hit': r[2], 'n_target': r[3], 'coverage_pct': r[4]}
            for r in rows
        ],
    }
    out_path = Path(__file__).parent / 'auto_construct_n4_result.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
