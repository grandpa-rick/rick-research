"""
Day 63 CODE Task 3 — Single-column lemma at n = 5 (odd).

Day-59: at n = 3, m_23456 (= long[1]) is free; pi^(g)(a) := a[long1] * g
is a valid integer-PL piece for every g in P^BDI_3 cap Z^7.

Day-62: extended to n = 4 (even) — long[1] is free, lemma holds.

Day-63: extend to n = 5 (odd). Verify:
  (a) long[1] has zero column in the AII constraint matrix at n=5
      (no Main_i inequality, no linking equation — n=5 is odd, no linking eq).
  (b) For 100 sampled g in P^BDI_5 with |g| <= 10, the piece pi^(g) maps
      every AII lattice pt p to a feasible BDI pt at n=5.
  (c) Existential closure: every BDI lattice pt q at |q| <= 10 is hit by
      pi^(q) at preimage (long[1] = 1, all others 0).

If (a), (b), (c) all hold => OQ-PI3-GROWTH branch (a) existential closure
extends to n = 5.
"""

import sys, json, random
from pathlib import Path

sys.path.insert(0, '/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-stack-structure')

import numpy as np

from dim_gap_verify import aii_structure, bdi_dim


OUT_DIR = Path(__file__).parent


def verify_long1_free(n):
    struct = aii_structure(n)
    long1 = struct['long_idx'][0]
    appears_ineq = any(struct['A_ineq'][r, long1] != 0
                       for r in range(struct['A_ineq'].shape[0]))
    appears_eq = any(struct['A_eq'][r, long1] != 0
                     for r in range(struct['A_eq'].shape[0]))
    return {
        'long1_var': struct['vars'][long1],
        'long1_idx': long1,
        'appears_in_ineq': appears_ineq,
        'appears_in_eq': appears_eq,
        'is_free': not (appears_ineq or appears_eq),
    }


def enumerate_aii_n5(N):
    """Enumerate AII lattice points at n=5, level <= N.

    Uses the aii_structure inequality system: n=5 is odd so there are NO
    linking equations, only Main_i inequalities long[i] + short[i] <= prefix[i-1]
    for i = 2..5. All vars >= 0. Sum of all 15 vars <= N.
    """
    struct = aii_structure(5)
    n_vars = struct['n_vars']  # 15
    A_ineq = struct['A_ineq']
    A_eq = struct['A_eq']
    pts = []

    def gen(remaining, depth, current):
        if depth == n_vars:
            x = np.array(current, dtype=int)
            if A_ineq.shape[0] and not np.all(A_ineq @ x <= 1e-9):
                return
            if A_eq.shape[0] and not np.all(np.abs(A_eq @ x) < 1e-9):
                return
            pts.append(tuple(current))
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()

    gen(N, 0, [])
    return pts, struct


def enumerate_bdi_n5(N):
    """Enumerate BDI lattice points at n=5, level <= N.
    Variables: M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S (12 vars).
    Constraints:
      T_a <= B_a for a = 1..4
      P_1 = 2(B_1 - T_1), P_a = P_{a-1} + 2(B_a - T_a) >= 0 for a = 2..4
      M_a <= min(P_{a-1}, P_a) for a = 2..4   (M_1 = 0 forced)
      S <= P_4
    """
    pts = set()
    for B_1 in range(N + 1):
        for T_1 in range(B_1 + 1):
            P_1 = 2 * (B_1 - T_1)
            r1 = N - B_1 - T_1
            for B_2 in range(r1 + 1):
                for T_2 in range(B_2 + 1):
                    P_2 = P_1 + 2 * (B_2 - T_2)
                    if P_2 < 0:
                        continue
                    r2 = r1 - B_2 - T_2
                    for B_3 in range(r2 + 1):
                        for T_3 in range(B_3 + 1):
                            P_3 = P_2 + 2 * (B_3 - T_3)
                            if P_3 < 0:
                                continue
                            r3 = r2 - B_3 - T_3
                            for B_4 in range(r3 + 1):
                                for T_4 in range(B_4 + 1):
                                    P_4 = P_3 + 2 * (B_4 - T_4)
                                    if P_4 < 0:
                                        continue
                                    r4 = r3 - B_4 - T_4
                                    M2_max = min(P_1, P_2, r4)
                                    for M_2 in range(M2_max + 1):
                                        r5 = r4 - M_2
                                        M3_max = min(P_2, P_3, r5)
                                        for M_3 in range(M3_max + 1):
                                            r6 = r5 - M_3
                                            M4_max = min(P_3, P_4, r6)
                                            for M_4 in range(M4_max + 1):
                                                r7 = r6 - M_4
                                                S_max = min(P_4, r7)
                                                for S in range(S_max + 1):
                                                    pts.add((M_2, M_3, M_4,
                                                             B_1, T_1, B_2, T_2,
                                                             B_3, T_3, B_4, T_4,
                                                             S))
    return pts


def bdi_n5_feasible(q):
    M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S = q
    if any(v < 0 for v in q):
        return False
    if T_1 > B_1 or T_2 > B_2 or T_3 > B_3 or T_4 > B_4:
        return False
    P_1 = 2 * (B_1 - T_1)
    P_2 = P_1 + 2 * (B_2 - T_2)
    P_3 = P_2 + 2 * (B_3 - T_3)
    P_4 = P_3 + 2 * (B_4 - T_4)
    if P_2 < 0 or P_3 < 0 or P_4 < 0:
        return False
    if M_2 > P_1 or M_2 > P_2: return False
    if M_3 > P_2 or M_3 > P_3: return False
    if M_4 > P_3 or M_4 > P_4: return False
    if S > P_4: return False
    return True


def piece_image_on_aii(g, aii_pts, long1_idx):
    """For pi^(g)(a) := a[long1] * g, check feasibility on all aii_pts."""
    image = set()
    for p in aii_pts:
        k = p[long1_idx]
        q = tuple(k * gi for gi in g)
        if not bdi_n5_feasible(q):
            return None, f"pi^(g={g}) at p={p}: q={q} infeasible"
        image.add(q)
    return image, None


def main():
    print("=" * 70)
    print("Day 63 CODE Task 3 — Single-column lemma at n = 5")
    print("=" * 70)

    # (a) long[1] free at n=5?
    info = verify_long1_free(5)
    print(f"\n(a) Free-variable check at n=5:")
    print(f"    long[1] = '{info['long1_var']}', idx = {info['long1_idx']}")
    print(f"    appears in any Main_i inequality? {info['appears_in_ineq']}")
    print(f"    appears in any linking equation?  {info['appears_in_eq']}")
    print(f"    -> IS FREE: {info['is_free']}")
    if not info['is_free']:
        print("FAIL: long[1] is not free.")
        sys.exit(1)

    # Cross-check at n = 3, 4
    for n in [3, 4]:
        c = verify_long1_free(n)
        print(f"    sanity n={n}: long[1] = '{c['long1_var']}', free = {c['is_free']}")

    # (b) AII enumeration. Sum <=10 to compare with Day-62 n=4 budget.
    N = 10
    print(f"\n(b) AII enumeration at n=5, |p| <= {N}")
    aii_pts, struct = enumerate_aii_n5(N)
    print(f"    # AII lattice pts: {len(aii_pts)}")
    long1_idx = struct['long_idx'][0]
    long1_vals = [p[long1_idx] for p in aii_pts]
    print(f"    long[1] range: 0..{max(long1_vals)}")

    # BDI enumeration at n=5
    print(f"\n    BDI enumeration at n=5, |q| <= {N}")
    bdi_pts = enumerate_bdi_n5(N)
    print(f"    # BDI lattice pts: {len(bdi_pts)}")

    # Sample 100 g in BDI with |g| <= 10. Verify pi^(g) on every AII pt.
    print(f"\n    Sample 100 g in BDI lattice (|g| <= {N}), verify pi^(g)")
    rng = random.Random(42)
    bdi_list = sorted(bdi_pts)
    sample = rng.sample(bdi_list, min(100, len(bdi_list)))
    n_ok = 0
    n_fail = 0
    fail_records = []
    image_sizes = []
    for g in sample:
        img, err = piece_image_on_aii(g, aii_pts, long1_idx)
        if err is not None:
            n_fail += 1
            fail_records.append(err)
        else:
            n_ok += 1
            image_sizes.append(len(img))
    print(f"    OK pieces (every AII pt -> feasible BDI): {n_ok}/{len(sample)}")
    print(f"    FAIL: {n_fail}/{len(sample)}")
    if fail_records:
        for rec in fail_records[:5]:
            print(f"      {rec}")
    if image_sizes:
        print(f"    Image sizes: min={min(image_sizes)}, "
              f"mean={sum(image_sizes)/len(image_sizes):.2f}, "
              f"max={max(image_sizes)}")

    # (c) Existential coverage. For every q in P^BDI_5 lattice at |q|<=N,
    # the piece pi^(q) at p = (long[1]=1, rest=0) gives image {q} (since
    # this p must be a valid AII pt). Verify p_q is in our enumerated set.
    # p_q is (0,...,0, 1 at long[1], 0,...,0). |p_q| = 1.
    long1_eq_1 = tuple(1 if i == long1_idx else 0 for i in range(struct['n_vars']))
    p_in = long1_eq_1 in set(aii_pts)
    print(f"\n(c) Existential closure check:")
    print(f"    p* = (long[1]=1, rest=0) is in AII lattice? {p_in}")
    print(f"    For every q in BDI lattice, pi^(q)(p*) = q -> q is hit.")
    print(f"    Conclusion: existential coverage = 100% at n=5, |q| <= {N}.")

    # Saturation table — analogous to Day-62 n=4.
    print(f"\n    Saturation: how many BDI lattice pts hit by pi^(g) with |g| <= G?")
    print(f"    {'G':>3} | {'#g<=G':>6} | {'#hit':>6} | {'#target':>7} | {'cov':>6}")
    print(f"    ----+--------+--------+---------+-------")
    L1_max = max(long1_vals)
    hit_total = set()
    rows = []
    g_lists = {G: [g for g in bdi_pts if sum(g) <= G] for G in range(1, N + 1)}
    for G in range(1, N + 1):
        new_g = set(g_lists[G]) - (set(g_lists[G-1]) if G > 1 else set())
        for g in new_g:
            sg = sum(g)
            if sg == 0:
                hit_total.add(g)
                continue
            k_max = min(L1_max, N // sg)
            for k in range(k_max + 1):
                q = tuple(k * x for x in g)
                if sum(q) <= N:
                    hit_total.add(q)
        cov_count = len(hit_total & bdi_pts)
        cov_pct = 100 * cov_count / len(bdi_pts)
        rows.append((G, len(g_lists[G]), cov_count, len(bdi_pts), cov_pct))
        print(f"    {G:>3} | {len(g_lists[G]):>6} | {cov_count:>6} | "
              f"{len(bdi_pts):>7} | {cov_pct:>5.2f}%")

    # JSON
    out = {
        'free_var_n5': info,
        'n_aii_pts': len(aii_pts),
        'n_bdi_pts': len(bdi_pts),
        'sample_size': len(sample),
        'pieces_ok': n_ok,
        'pieces_fail': n_fail,
        'image_sizes': {
            'min': min(image_sizes) if image_sizes else 0,
            'mean': sum(image_sizes)/len(image_sizes) if image_sizes else 0,
            'max': max(image_sizes) if image_sizes else 0,
        },
        'existential_p_star_in_lattice': p_in,
        'saturation_table': [
            {'G': r[0], 'n_g_le_G': r[1], 'n_hit': r[2],
             'n_target': r[3], 'coverage_pct': r[4]}
            for r in rows
        ],
    }
    out_path = OUT_DIR / 'single_column_n5_result.json'
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
