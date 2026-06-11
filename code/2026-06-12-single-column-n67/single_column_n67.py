#!/usr/bin/env python3
"""
Task C — extend the single-column lemma (Day-62 OQ-PI3-GROWTH branch (a))
to n=6 and n=7.

Single-column piece pi^(g)(p) := p[long[1]] * g  for g in BDI lattice,
p in AII lattice. Day-62 closed branch (a) at n in {2,3,4}; Day-64 at n=5;
we extend here to n=6, 7 with 100 sampled BDI g's at each.

The BDI polytope is a rational polyhedral cone (all defining ineqs
linear, no equations), so closed under nonneg integer scaling. Hence
g feasible -> k*g feasible for all k>=0 integer. The test verifies
that this stays true under the explicit feasibility predicate at n=6,7.

Also verifies that long[1] remains a FREE AII variable at n=6 (even,
has Cor 8 linking eq) and n=7 (odd, no link).
"""

import sys, json, random
from pathlib import Path

sys.path.insert(
    0, "/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational"
)
from dim_gap_verify import aii_structure


# ---------------------------------------------------------------------
# General-n BDI feasibility
# ---------------------------------------------------------------------

def bdi_vars_general(n):
    """Variable order: (M_2..M_{n-1}, B_1..B_{n-1}, T_1..T_{n-1}, S)."""
    names = []
    for i in range(2, n):
        names.append(f"M_{i}")
    for i in range(1, n):
        names.append(f"B_{i}")
    for i in range(1, n):
        names.append(f"T_{i}")
    names.append("S")
    return names


def bdi_n_feasible(q, n):
    """
    q is a tuple in the var order from bdi_vars_general(n).
    Returns True iff q satisfies all BDI inequalities at level n.

    Constraints (M_1 = 0 forced):
      T_a >= 0, B_a >= 0, T_a <= B_a            (a = 1..n-1)
      P_a := 2 * sum_{b<=a} (B_b - T_b) >= 0    (a = 1..n-1)
      M_a >= 0, M_a <= P_{a-1}, M_a <= P_a      (a = 2..n-1; M_1=0)
      S >= 0, S <= P_{n-1}
    """
    names = bdi_vars_general(n)
    if len(q) != len(names):
        raise ValueError(f"q has {len(q)} entries, expected {len(names)}")
    idx = {nm: i for i, nm in enumerate(names)}

    if any(v < 0 for v in q):
        return False

    # T_a <= B_a
    for a in range(1, n):
        if q[idx[f"T_{a}"]] > q[idx[f"B_{a}"]]:
            return False

    # Partial sums P_a = 2*sum(B - T)
    P = {0: 0}
    for a in range(1, n):
        P[a] = P[a - 1] + 2 * (q[idx[f"B_{a}"]] - q[idx[f"T_{a}"]])
        if P[a] < 0:
            return False

    # M_a constraints (M_1 = 0 forced; we don't store M_1)
    for a in range(2, n):
        Ma = q[idx[f"M_{a}"]]
        if Ma > P[a - 1] or Ma > P[a]:
            return False

    # S <= P_{n-1}
    if q[idx["S"]] > P[n - 1]:
        return False

    return True


def sample_bdi_point(n, N_max, rng):
    """
    Sample a random BDI-feasible lattice point with total mass <= N_max.

    Strategy: pick B_a, T_a with T_a <= B_a, walk forward computing P_a;
    pick M_a uniformly in [0, min(P_{a-1}, P_a)]; pick S in [0, P_{n-1}],
    all subject to remaining budget. Resample if a step exhausts budget.
    """
    for _ in range(1000):
        q_map = {}
        budget = N_max
        ok = True
        # B and T
        P = {0: 0}
        for a in range(1, n):
            if budget <= 0:
                B_a = T_a = 0
            else:
                B_a = rng.randint(0, max(0, budget // 2))
                T_a = rng.randint(0, B_a)
            q_map[f"B_{a}"] = B_a
            q_map[f"T_{a}"] = T_a
            budget -= B_a + T_a
            if budget < 0:
                ok = False
                break
            P[a] = P[a - 1] + 2 * (B_a - T_a)
            if P[a] < 0:
                ok = False
                break
        if not ok:
            continue
        # M_a for a=2..n-1
        for a in range(2, n):
            M_max = min(P[a - 1], P[a], budget if budget >= 0 else 0)
            if M_max < 0:
                ok = False
                break
            M_a = rng.randint(0, M_max)
            q_map[f"M_{a}"] = M_a
            budget -= M_a
            if budget < 0:
                ok = False
                break
        if not ok:
            continue
        # S
        S_max = min(P[n - 1], budget if budget >= 0 else 0)
        if S_max < 0:
            continue
        S = rng.randint(0, S_max)
        q_map["S"] = S

        names = bdi_vars_general(n)
        q = tuple(q_map[nm] for nm in names)
        if bdi_n_feasible(q, n):
            return q
    raise RuntimeError(f"failed to sample BDI feasible point at n={n}")


def verify_long1_free(n):
    struct = aii_structure(n)
    long1_idx = struct["long_idx"][0]
    in_ineq = any(struct["A_ineq"][k, long1_idx] != 0
                  for k in range(struct["A_ineq"].shape[0]))
    in_eq = any(struct["A_eq"][k, long1_idx] != 0
                for k in range(struct["A_eq"].shape[0]))
    return {
        "long1_var": struct["vars"][long1_idx],
        "appears_in_ineq": bool(in_ineq),
        "appears_in_eq": bool(in_eq),
        "is_free": not (in_ineq or in_eq),
    }


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def test_single_column_n(n, n_samples=100, N_max=10,
                         k_range=(0, 11), seed=None):
    rng = random.Random(seed if seed is not None else 6500 + n)
    free_info = verify_long1_free(n)
    print(f"\n--- n = {n} ({'even' if n%2==0 else 'odd'}) ---")
    print(f" long[1] = {free_info['long1_var']}")
    print(f" long[1] in any Main_i?    {free_info['appears_in_ineq']}")
    print(f" long[1] in any link eq?   {free_info['appears_in_eq']}")
    print(f" long[1] is FREE?          {free_info['is_free']}")
    if not free_info["is_free"]:
        raise AssertionError(f"long[1] not free at n={n}")

    names = bdi_vars_general(n)
    print(f" BDI vars ({len(names)}): {names}")

    n_pass = 0
    n_fail = 0
    failures = []
    samples = []
    for s in range(n_samples):
        g = sample_bdi_point(n, N_max, rng)
        # Verify g itself is feasible (sanity)
        assert bdi_n_feasible(g, n), f"sampled g not feasible: {g}"
        # Scale g by k = 0..k_range[1] and verify
        all_ok = True
        bad_k = None
        for k in range(k_range[0], k_range[1]):
            q = tuple(k * x for x in g)
            if not bdi_n_feasible(q, n):
                all_ok = False
                bad_k = k
                break
        samples.append({"g": list(g), "all_k_ok": all_ok, "bad_k": bad_k})
        if all_ok:
            n_pass += 1
        else:
            n_fail += 1
            failures.append({"g": list(g), "bad_k": bad_k})

    print(f" sampled {n_samples} BDI lattice points, sum(g) <= {N_max}")
    print(f" verified k*g feasible for k in [{k_range[0]}, {k_range[1]})")
    print(f"   pass: {n_pass}/{n_samples}")
    print(f"   fail: {n_fail}/{n_samples}")
    if failures:
        print(f"   FAILURES:")
        for f in failures[:5]:
            print(f"     {f}")

    return {
        "n": n,
        "long1_info": free_info,
        "n_samples": n_samples,
        "N_max": N_max,
        "k_range": list(k_range),
        "n_pass": n_pass,
        "n_fail": n_fail,
        "failures": failures,
        "samples_preview": samples[:5],
    }


def main():
    print("=" * 70)
    print("Task C — Single-column lemma at n=6, n=7")
    print("=" * 70)
    print()
    print(" Strategy: BDI is a polyhedral cone -> closed under nonneg")
    print(" integer scaling, so pi^(g) := long[1]*g is automatically")
    print(" feasible whenever g is. We sample 100 random BDI-feasible")
    print(" lattice points at each n and verify scaling by k=0..10")
    print(" preserves feasibility -- this exercises the explicit BDI")
    print(" predicate as a check of our enumeration logic.")

    results = {}
    for n in [6, 7]:
        results[n] = test_single_column_n(n, n_samples=100, N_max=10,
                                          k_range=(0, 11), seed=6500 + n)

    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    for n in [6, 7]:
        r = results[n]
        print(f" n={n}: {r['n_pass']}/{r['n_samples']} pass, "
              f"{r['n_fail']} fail, long[1] free: "
              f"{r['long1_info']['is_free']}")

    # Save
    out_dir = Path(__file__).parent
    with open(out_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nsaved: {out_dir/'results.json'}")


if __name__ == "__main__":
    main()
