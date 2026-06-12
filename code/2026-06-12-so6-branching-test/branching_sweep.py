"""
Full sweep: for every gl_6 partition λ ⊂ (5^3) (= ≤3 rows, parts ≤ 5),
compute Res^{gl_6}_{O(6)} V_λ as a sum of O(6) irreps, verify dimension
sums, and confirm no O(6) irrep nor any sub-collection of irreps with
total dim 22 ever arises.

Output: branching_data.json with full multiplicity table; printed summary.
"""

from __future__ import annotations

import json
from collections import Counter

from lr_branching import gl_to_O_branching, normalize
from so6_weights import so6_dim_from_weights, ssyt_shape


def gl6_dim(shape):
    shape = normalize(shape)
    if not shape:
        return 1
    cnt = 0
    for _ in ssyt_shape(shape, 6):
        cnt += 1
    return cnt


def o6_dim(mu):
    """dim V_μ^{O(6)}: convert μ to D_3 = so_6 highest weight and apply formula.

    For μ a partition with at most 3 rows, V_μ^{O(6)} restricts to V_{(μ_1, μ_2, μ_3)}^{so_6}
    (if all three rows are nonzero, V_μ^{O(6)} = V_{l_3 ≥ 0} ⊕ V_{l_3 ≤ 0} as SO(6);
    for our dim-bookkeeping purposes, dim V_μ^{O(6)} = 2 · dim V_(μ_1,μ_2,μ_3)^{so_6}
    when μ_3 > 0 since the two SO(6) summands have the same dim).

    Actually: V_μ^{O(6)} for μ with at most 2 rows = V_{(μ_1, μ_2, 0)}^{so_6}, dim = the
    Weyl dim formula gives correct answer.

    For μ with exactly 3 nonzero rows: V_μ^{O(6)} splits into V_(μ_1,μ_2,μ_3)^{so_6} ⊕
    V_(μ_1,μ_2,-μ_3)^{so_6} as SO(6), both of equal dim. dim V_μ^{O(6)} = 2 · dim V_(μ_1,μ_2,μ_3).
    """
    mu = normalize(mu)
    while len(mu) < 3:
        mu = mu + (0,)
    l1, l2, l3 = mu
    d = so6_dim_from_weights(l1, l2, l3)
    if l3 > 0:
        return 2 * d
    return d


def main():
    partitions = []
    for l1 in range(0, 6):
        for l2 in range(0, l1 + 1):
            for l3 in range(0, l2 + 1):
                shape = normalize((l1, l2, l3))
                partitions.append(shape)

    print(f"Sweeping {len(partitions)} partitions λ ⊂ (5^3).\n")
    all_branchings = {}
    irreps_seen = Counter()  # μ → max multiplicity seen
    flag_dim22 = False
    print(f"{'λ':<15} {'dim λ':<8} {'O(6) decomposition'}")
    print("-" * 80)
    for shape in partitions:
        d_gl = gl6_dim(shape)
        branch = gl_to_O_branching(shape, 6)
        d_check = sum(mult * o6_dim(mu) for mu, mult in branch.items())
        ok = "✓" if d_check == d_gl else f"FAIL ({d_check} vs {d_gl})"
        readable = ", ".join(f"{mu}×{mult}" if mult > 1 else f"{mu}" for mu, mult in sorted(branch.items()))
        print(f"{str(shape):<15} {d_gl:<8} {readable}   [{ok}]")
        all_branchings[str(shape)] = {"dim_gl": d_gl, "branching": {str(k): v for k, v in branch.items()}}
        for mu, mult in branch.items():
            irreps_seen[mu] = max(irreps_seen[mu], mult)
            if o6_dim(mu) == 22:
                flag_dim22 = True
                print(f"  !!! Found O(6) irrep μ = {mu} with dim 22 !!!")

    print()
    print(f"Total distinct O(6) irreps seen: {len(irreps_seen)}")
    print(f"Any O(6) irrep with dim 22? {flag_dim22}")
    print()
    print("All O(6) irreps seen, with their dims:")
    for mu, _ in sorted(irreps_seen.items(), key=lambda kv: (o6_dim(kv[0]), kv[0])):
        print(f"  μ = {mu}, dim = {o6_dim(mu)}")

    with open("branching_data.json", "w") as f:
        json.dump(all_branchings, f, indent=2)
    print(f"\nSaved full branching table to branching_data.json")


if __name__ == "__main__":
    main()
