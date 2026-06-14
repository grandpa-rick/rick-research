#!/usr/bin/env python3
"""
Day 71 CODE Task B — Even-n Λ analysis at n=4 and n=6.

Hypothesis (Day-70 Theorem 4.2 sketch): at even n the linking equation
    linkLHS = sum_{i=1..n-1} short[i]
collapses one ray of the AII cone, so the cone has 3n - 1 extreme rays.

Closed-form facet count: 3n - [n even]
  n=3: 9, n=4: 11, n=5: 15, n=6: 17, n=7: 21, n=8: 23  -- matches Day-69.

This task: enumerate the EXTREME RAYS of the AII cone at n=4, 6 and
verify the count matches 3n - 1.

Method:
  1. Build AII cone:   A_ub x <= 0,  A_eq x = 0.
  2. Compute irredundant facets via LP (already done Day-69; redo here
     to be self-contained).
  3. Enumerate extreme rays: a ray r is determined by binding at least
     (d_cone - 1) of the facets (where d_cone = n_vars - rank(A_eq)).
     For each (d_cone - 1)-subset of irredundant facets:
       solve  A_eq r = 0  AND  a_S r = 0
       if nullspace has dim exactly 1, take the generator,
       orient positively, check all other inequalities are <= 0,
       hash the normalized vector.
  4. Dedupe & count.

Cross-check: also enumerate at odd n=3, 5 to confirm 3n rays at odd n.
"""

import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import numpy as np

sys.path.insert(0, "/home/agent/projects/code/2026-06-14-azenhas-aii-walls")
from azenhas_aii_walls import (  # noqa: E402
    azenhas_system_TheoremDE_strict,
    count_facets,
)

OUT_DIR = Path("/home/agent/projects/code/2026-06-16-even-n-lambda")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------
# Exact rational nullspace via row-reduction.
# ---------------------------------------------------------------
def rational_matrix(A):
    """Numpy float ndarray -> list of list of Fraction."""
    return [[Fraction(int(round(float(x)))) for x in row] for row in A]


def _to_frac_row(row):
    """Convert a numpy row (any dtype) to a list of Fractions safely."""
    return [Fraction(int(round(float(x)))) for x in row]


def rref(M):
    """In-place reduced row echelon form on rational matrix M (list of
    lists of Fraction). Returns rank and pivot columns."""
    m = len(M)
    if m == 0:
        return 0, []
    n = len(M[0])
    pivot_cols = []
    r = 0
    for c in range(n):
        # find pivot row
        piv = None
        for k in range(r, m):
            if M[k][c] != 0:
                piv = k
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        # normalize
        d = M[r][c]
        M[r] = [x / d for x in M[r]]
        # eliminate other rows
        for k in range(m):
            if k != r and M[k][c] != 0:
                f = M[k][c]
                M[k] = [a - f * b for a, b in zip(M[k], M[r])]
        pivot_cols.append(c)
        r += 1
        if r == m:
            break
    return r, pivot_cols


def nullspace_basis(rows, n):
    """Given a list of length-n rational rows of a linear system Ax=0,
    return a list of basis vectors (each a tuple of Fractions) for the
    nullspace. Uses exact rational RREF."""
    if not rows:
        # all of R^n
        basis = []
        for j in range(n):
            v = [Fraction(0)] * n
            v[j] = Fraction(1)
            basis.append(tuple(v))
        return basis
    M = [list(r) for r in rows]
    rank, pivots = rref(M)
    pivot_set = set(pivots)
    free_cols = [j for j in range(n) if j not in pivot_set]
    basis = []
    for j in free_cols:
        v = [Fraction(0)] * n
        v[j] = Fraction(1)
        for pi, pc in enumerate(pivots):
            v[pc] = -M[pi][j]
        basis.append(tuple(v))
    return basis


def normalize_ray(v):
    """Normalize ray direction to canonical form: scale so first nonzero
    entry is +1 (Fraction). Returns tuple of Fractions."""
    v = tuple(v)
    # find first nonzero
    first = None
    for x in v:
        if x != 0:
            first = x
            break
    if first is None:
        return None
    if first < 0:
        v = tuple(-x for x in v)
        first = -first
    return tuple(x / first for x in v)


# ---------------------------------------------------------------
# Enumerate extreme rays via binding-facet subsets.
# ---------------------------------------------------------------
def enumerate_rays(A_ub, b_ub, A_eq, b_eq, labels):
    """Enumerate extreme rays of the cone {x : A_ub x <= 0, A_eq x = 0}.

    Assumes b_ub = 0 and b_eq = 0 (it's a cone).

    Strategy: filter to irredundant facets, then for each (d_cone-1)-
    subset of facets, solve the system with those binding + A_eq = 0;
    check 1-dim nullspace; check remaining ineqs nonpositive; dedupe.
    """
    assert np.allclose(b_ub, 0), "expected cone (b_ub=0)"
    assert np.allclose(b_eq, 0), "expected cone (b_eq=0)"
    n_vars = A_ub.shape[1]
    A_eq_rows = [_to_frac_row(row) for row in A_eq]

    # 1) find irredundant facets via LP
    res_facets = count_facets(A_ub, b_ub, A_eq, b_eq, labels)
    facet_labels = res_facets["facet_labels"]
    facet_indices = [i for i, lab in enumerate(labels)
                     if lab in facet_labels]
    # Cone dimension = n_vars - rank(A_eq)
    rank_eq, _ = rref([_to_frac_row(r) for r in A_eq])
    d_cone = n_vars - rank_eq

    print(f"  n_vars={n_vars}, rank(A_eq)={rank_eq}, "
          f"d_cone={d_cone}, n_irredundant_facets={len(facet_indices)}")
    print(f"  enumerate {d_cone - 1}-subsets of "
          f"{len(facet_indices)} facets... "
          f"({len(list(combinations(range(len(facet_indices)), d_cone-1)))} subsets)")

    A_ub_rat = [_to_frac_row(row) for row in A_ub]

    rays = {}  # normalized ray -> info
    n_skip_dim = 0
    n_skip_neg = 0

    for subset in combinations(range(len(facet_indices)), d_cone - 1):
        # Combine binding rows + eq rows
        binding_rows = [A_ub_rat[facet_indices[s]] for s in subset]
        sys_rows = list(A_eq_rows) + list(binding_rows)
        basis = nullspace_basis(sys_rows, n_vars)
        if len(basis) != 1:
            n_skip_dim += 1
            continue
        r = list(basis[0])
        # try both orientations
        oriented = None
        for sign in (1, -1):
            v = [sign * x for x in r]
            # Check all inequalities A_ub v <= 0
            ok = True
            for row in A_ub_rat:
                s = Fraction(0)
                for a, x in zip(row, v):
                    s += a * x
                if s > 0:
                    ok = False
                    break
            if ok:
                oriented = v
                break
        if oriented is None:
            n_skip_neg += 1
            continue
        norm = normalize_ray(oriented)
        if norm is None:
            continue
        if norm not in rays:
            rays[norm] = {
                "subset_facet_indices": [int(facet_indices[s])
                                          for s in subset],
                "subset_facet_labels": [labels[facet_indices[s]]
                                         for s in subset],
                "ray": [str(x) for x in norm],
            }

    return {
        "n_rays": len(rays),
        "n_irredundant_facets": len(facet_indices),
        "d_cone": d_cone,
        "n_skip_dim": n_skip_dim,
        "n_skip_neg": n_skip_neg,
        "rays": list(rays.values()),
        "facet_labels": facet_labels,
    }


# ---------------------------------------------------------------
# Run
# ---------------------------------------------------------------
def labelled_ray(ray_strs, var_names):
    out = {}
    for nm, s in zip(var_names, ray_strs):
        if s != "0":
            out[nm] = s
    return out


def main():
    print("=" * 72)
    print("Day 71 CODE Task B — Even-n Λ analysis at n=4, 6")
    print("=" * 72)

    results = {}
    for n in [3, 4, 5, 6]:
        print(f"\n--- n = {n} ({'even' if n % 2 == 0 else 'odd'}) ---")
        A_ub, b_ub, A_eq, b_eq, labels, n_vars, vars_list = (
            azenhas_system_TheoremDE_strict(n)
        )
        r = enumerate_rays(A_ub, b_ub, A_eq, b_eq, labels)
        pred = 3 * n - (1 if n % 2 == 0 else 0)
        r["closed_form_pred"] = pred
        r["closed_form_match"] = (r["n_rays"] == pred)
        r["n_vars"] = n_vars
        r["vars"] = vars_list
        # label rays nicely
        for ray_info in r["rays"]:
            ray_info["labelled"] = labelled_ray(ray_info["ray"], vars_list)
        results[n] = r
        print(f"  n_rays = {r['n_rays']}  (predicted 3n - [n even] = {pred})")
        match = "MATCH" if r["closed_form_match"] else "MISMATCH"
        print(f"  closed-form check: {match}")
        print(f"  example rays (up to 5):")
        for ri, ray_info in enumerate(r["rays"][:5]):
            print(f"    ray[{ri}] = {ray_info['labelled']}")

    print("\n" + "=" * 72)
    print("SUMMARY TABLE — extreme ray counts of AII cone")
    print("=" * 72)
    print(f"  {'n':>2}  {'parity':>5}  {'#rays':>6}  {'closed':>6}  {'match?':>7}")
    for n in [3, 4, 5, 6]:
        r = results[n]
        print(f"  {n:>2}  "
              f"{'even' if n%2==0 else 'odd':>5}  "
              f"{r['n_rays']:>6}  "
              f"{r['closed_form_pred']:>6}  "
              f"{'YES' if r['closed_form_match'] else 'NO':>7}")

    # Period-2 finite difference (quasipoly check)
    print("\n  Period-2 finite-difference check (Day-58 calibration):")
    rays = [results[n]["n_rays"] for n in [3, 4, 5, 6]]
    d1 = [rays[i+1] - rays[i] for i in range(3)]
    print(f"    #rays = {rays}")
    print(f"    Δ1    = {d1}")
    # Period-2 Δ²: f(n+2) - 2 f(n+1) + f(n)
    if len(rays) >= 3:
        period2 = [rays[i+2] - 2*rays[i+1] + rays[i] for i in range(2)]
        print(f"    Δ² (single-step) = {period2}")

    # Verdict
    all_match = all(results[n]["closed_form_match"] for n in [4, 6])
    print()
    if all_match:
        verdict = (
            "VERIFIED: extreme ray count at n=4, 6 matches 3n - 1 = 11, 17. "
            "Λ-collapse hypothesis (Day-70 Theorem 4.2) holds — "
            "even-n linking equation kills exactly one ray relative to "
            "the 3n-ray odd-n pattern."
        )
    else:
        verdict = (
            "MISMATCH at even n. Day-70 Theorem 4.2 must be REFORMULATED. "
            "See per-n ray breakdown."
        )
    print(verdict)

    # Save
    save = {
        "verdict": verdict,
        "results": {str(k): v for k, v in results.items()},
    }
    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(save, f, indent=2, default=str)
    print(f"\nsaved: {OUT_DIR/'results.json'}")


if __name__ == "__main__":
    main()
