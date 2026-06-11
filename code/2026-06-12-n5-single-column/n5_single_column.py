"""
Day 64 CODE Task 3 — Single-column lemma at n=5.

Day-62 closed branch (a) of OQ-PI3-GROWTH at n ∈ {2, 3, 4}: long[1] is
the unique free AII variable, and pi^(g)(a) := a[long[1]] * g is a valid
integer-PL piece (lands in BDI cone for any g ∈ P^BDI ∩ Z^(2n-1)).

Extend to n=5. At n=5 (odd), f(5)=3, so the AII polytope has 15 = 3n dims.
long[1] should still be the free var (no Main_i, no link eq at odd n).

Test:
  1. Verify long[1] is free at n=5 (no Main, no eq).
  2. Enumerate BDI lattice at n=5, sum ≤ N.
  3. For 100 sampled g ∈ BDI lattice, verify pi^(g) maps each AII point
     into BDI cone.
  4. Sub-N coverage stat.
"""

import sys, json, random
from pathlib import Path
import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational')
from dim_gap_verify import aii_structure


def verify_long1_free(n):
    struct = aii_structure(n)
    long1_idx = struct['long_idx'][0]
    appears_ineq = any(row[long1_idx] != 0 for row in struct['A_ineq'])
    appears_eq = any(row[long1_idx] != 0 for row in struct['A_eq'])
    return {
        'long1_var': struct['vars'][long1_idx],
        'long1_idx': long1_idx,
        'appears_in_ineq': appears_ineq,
        'appears_in_eq': appears_eq,
        'is_free': not (appears_ineq or appears_eq),
    }


def enumerate_aii(n, N_max):
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
    gen(N_max, 0, [])
    return pts, struct


def enumerate_bdi_n5(N_max):
    """BDI at n=5. Vars: M_2..M_4, B_1..B_4, T_1..T_4, S (3+4+4+1=12 vars).
    Constraints: T_a ≤ B_a (a=1..4); P_a = sum_{b≤a} 2(B_b-T_b) ≥ 0;
                 M_a ≤ min(P_{a-1}, P_a) for a=2,3,4; S ≤ P_4."""
    pts = set()
    for B_1 in range(N_max + 1):
        for T_1 in range(B_1 + 1):
            P_1 = 2 * (B_1 - T_1)
            for B_2 in range(N_max + 1 - B_1 - T_1):
                for T_2 in range(B_2 + 1):
                    P_2 = P_1 + 2 * (B_2 - T_2)
                    if P_2 < 0: continue
                    for B_3 in range(N_max + 1 - B_1 - T_1 - B_2 - T_2):
                        for T_3 in range(B_3 + 1):
                            P_3 = P_2 + 2 * (B_3 - T_3)
                            if P_3 < 0: continue
                            for B_4 in range(N_max + 1 - B_1 - T_1 - B_2 - T_2 - B_3 - T_3):
                                for T_4 in range(B_4 + 1):
                                    P_4 = P_3 + 2 * (B_4 - T_4)
                                    if P_4 < 0: continue
                                    base = B_1 + T_1 + B_2 + T_2 + B_3 + T_3 + B_4 + T_4
                                    if base > N_max: continue
                                    M_2_max = min(P_1, P_2)
                                    M_3_max = min(P_2, P_3)
                                    M_4_max = min(P_3, P_4)
                                    for M_2 in range(M_2_max + 1):
                                        if base + M_2 > N_max: break
                                        for M_3 in range(M_3_max + 1):
                                            if base + M_2 + M_3 > N_max: break
                                            for M_4 in range(M_4_max + 1):
                                                if base + M_2 + M_3 + M_4 > N_max: break
                                                for S in range(P_4 + 1):
                                                    if base + M_2 + M_3 + M_4 + S > N_max: break
                                                    pts.add((M_2, M_3, M_4,
                                                              B_1, T_1, B_2, T_2,
                                                              B_3, T_3, B_4, T_4, S))
    return pts


def bdi_n5_feasible(q):
    M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S = q
    if any(v < 0 for v in q): return False
    if T_1 > B_1 or T_2 > B_2 or T_3 > B_3 or T_4 > B_4: return False
    P_1 = 2 * (B_1 - T_1)
    P_2 = P_1 + 2 * (B_2 - T_2)
    P_3 = P_2 + 2 * (B_3 - T_3)
    P_4 = P_3 + 2 * (B_4 - T_4)
    if P_2 < 0 or P_3 < 0 or P_4 < 0: return False
    if M_2 > P_1 or M_2 > P_2: return False
    if M_3 > P_2 or M_3 > P_3: return False
    if M_4 > P_3 or M_4 > P_4: return False
    if S > P_4: return False
    return True


def main():
    print("="*70)
    print("Day 64 CODE Task 3 — Single-column lemma at n=5")
    print("="*70)

    # Step 1: Verify long[1] is free
    info = verify_long1_free(5)
    print(f"\nStep 1: 'free variable' check at n=5")
    print(f"  long[1] = '{info['long1_var']}'")
    print(f"  appears in Main_i ineq? {info['appears_in_ineq']}")
    print(f"  appears in linking eq?   {info['appears_in_eq']}")
    print(f"  -> IS FREE: {info['is_free']}")
    if not info['is_free']:
        print("FAIL: long[1] not free at n=5")
        sys.exit(1)

    # Step 2: enumerate
    N_max = 8
    print(f"\nStep 2: AII enumeration at n=5, N <= {N_max}")
    aii_pts, struct = enumerate_aii(5, N_max)
    print(f"  # AII lattice pts: {len(aii_pts)}")
    long1_idx = struct['long_idx'][0]
    L1_max = max(p[long1_idx] for p in aii_pts)
    print(f"  long[1] range: 0..{L1_max}")

    print(f"\nStep 3: BDI enumeration at n=5, N <= {N_max}")
    bdi_pts = enumerate_bdi_n5(N_max)
    print(f"  # BDI lattice pts: {len(bdi_pts)}")

    # Step 4: 100 sample pieces
    print(f"\nStep 4: build 100 single-column pieces, verify feasibility")
    rng = random.Random(64)
    bdi_list = sorted(bdi_pts)
    sample = rng.sample(bdi_list, min(100, len(bdi_list)))
    n_ok = 0
    n_fail = 0
    for g in sample:
        all_ok = True
        for p in aii_pts:
            k = p[long1_idx]
            q = tuple(k * x for x in g)
            if not bdi_n5_feasible(q):
                all_ok = False
                break
        if all_ok:
            n_ok += 1
        else:
            n_fail += 1
    print(f"  feasible pieces: {n_ok}/{len(sample)}")
    print(f"  fail pieces:     {n_fail}/{len(sample)}")

    # Step 5: 1-column saturation
    print(f"\nStep 5: 1-column saturation analysis at n=5")
    rows = []
    g_at_or_below = {G: [g for g in bdi_pts if sum(g) <= G] for G in range(1, N_max + 1)}
    target = bdi_pts

    hit_total = set()
    for G in range(1, N_max + 1):
        new_g_set = set(g_at_or_below[G])
        for g in new_g_set:
            sum_g = sum(g)
            if sum_g == 0:
                hit_total.add(g)
                continue
            k_max = min(L1_max, N_max // sum_g)
            for k in range(0, k_max + 1):
                q = tuple(k * x for x in g)
                if sum(q) <= N_max:
                    hit_total.add(q)
        cov = 100 * len(hit_total & target) / len(target)
        rows.append((G, len(g_at_or_below[G]), len(hit_total & target), len(target), cov))
        print(f"  G={G:>2}: |g|<=G count={len(g_at_or_below[G]):>6}, "
              f"hits={len(hit_total & target):>6}, target={len(target):>6}, cov={cov:6.2f}%")

    # Save
    out = {
        'verify_long1_free_n5': info,
        'n': 5, 'N': N_max,
        'n_aii_pts': len(aii_pts),
        'n_bdi_pts': len(bdi_pts),
        'sample_size': len(sample),
        'pieces_ok': n_ok,
        'pieces_fail': n_fail,
        'saturation': [
            {'G': r[0], 'n_g': r[1], 'n_hit': r[2], 'n_target': r[3], 'coverage_pct': r[4]}
            for r in rows
        ],
        'conclusion': ("Single-column lemma EXTENDS to n=5" if n_fail == 0
                       else "Single-column lemma FAILS at n=5"),
    }
    with open(Path(__file__).parent / 'n5_single_column.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {Path(__file__).parent / 'n5_single_column.json'}")
    print(f"\nCONCLUSION: {out['conclusion']}")


if __name__ == "__main__":
    main()
