"""
Day 60 (2026-06-10) Task 1: Computational verification of dim-gap parity
at n = 5 and n = 6.

Approach:
  For each n, enumerate AII free vars + Cor 8 linking equations + Main_i
  inequalities, build the constraint matrices, and compute the affine
  hull dim of P^{AII}_{2n-1} as

      dim = (# free vars) - rank(equations restricted to feasible interior).

  Then BDI dim = 3n - 3 (well-known: M_2..M_{n-1}, B_1..B_{n-1}, T_1..T_{n-1}, S
  with M_1 = 0).

  Cross-check the affine hull dim by (a) finding an interior point via LP
  and verifying no inequality is forced tight on the interior, and (b)
  enumerating small-N lattice points and fitting the affine span.

Expected (per Day-59 analytic):
  n=5 odd : dim AII = 15, dim BDI = 12, gap = 3.
  n=6 even: dim AII = 17, dim BDI = 15, gap = 2.
"""

import numpy as np
import sympy as sp
import itertools
from scipy.optimize import linprog


# ----------------------------------------------------------------------
# General-n AII polytope structure (per Azenhas Thm 6 / Cor 8)
# ----------------------------------------------------------------------

def aii_structure(n):
    """
    Return a dict describing the AII polytope at level n.

    Variables (3n total):
      prefix[i]   for i = 1..n   (m_2, m_{23}, m_{236}, ..., m_{2,3,..,n+1})
      long[i]     for i = 1..n   (red^{-1}(u_i), length 2n-1)
      short[i]    for i = 1..n-1 (= long[i] with 2n removed, length 2n-2)
                                  these are the "slack" vars in linking eq
      EXTRA at even n:
        linkLHS               (length 2n-1, missing index 2n-1 — m_{1..(2n-2)·2n})
      EXTRA at odd n:
        short[n]              (a length-(2n-2) variable filling the count to 3n)
                                — at n=3 this is m_{1234}; appears via Singleton
                                  bound, not a linking equation.

    Inequalities (Main_i, i = 2..n):  long[i] + short[i] <= prefix[i-1]
                                       (at i=n EVEN: short[n] is absorbed
                                        into linkLHS, so Main_n becomes
                                        long[n] <= prefix[n-1])
    Equations: at EVEN n only:
        linkLHS = short[1] + short[2] + ... + short[n-1]
    All vars >= 0.
    """
    vars_list = []
    prefix_idx = []
    long_idx = []
    short_idx = []

    # prefix vars (m_2, m_23, m_236, m_2367, ...) length 1..n
    for i in range(1, n + 1):
        vars_list.append(f"prefix[{i}]")
        prefix_idx.append(len(vars_list) - 1)

    # long vars (red^{-1}(u_i), length 2n-1)
    for i in range(1, n + 1):
        vars_list.append(f"long[{i}]")
        long_idx.append(len(vars_list) - 1)

    if n % 2 == 0:
        # short[1..n-1], one linkLHS
        for i in range(1, n):
            vars_list.append(f"short[{i}]")
            short_idx.append(len(vars_list) - 1)
        vars_list.append("linkLHS")
        linkLHS_idx = len(vars_list) - 1
    else:
        # short[1..n], no linkLHS
        for i in range(1, n + 1):
            vars_list.append(f"short[{i}]")
            short_idx.append(len(vars_list) - 1)
        linkLHS_idx = None

    assert len(vars_list) == 3 * n, (n, len(vars_list))

    # Inequalities: long[i] + short[i] - prefix[i-1] <= 0 for i=2..n,
    # except at even n, i=n: short[n] doesn't exist; only long[n] <= prefix[n-1].
    A_ineq = []
    b_ineq = []
    for i in range(2, n + 1):
        row = [0] * (3 * n)
        row[long_idx[i - 1]] = 1
        if i - 1 < len(short_idx) and (n % 2 == 1 or i < n):
            # short[i] exists in the index range
            row[short_idx[i - 1]] = 1
        row[prefix_idx[i - 2]] = -1
        A_ineq.append(row)
        b_ineq.append(0)

    # Equations: at even n, linkLHS = sum of short[1..n-1].
    A_eq = []
    b_eq = []
    if n % 2 == 0:
        row = [0] * (3 * n)
        row[linkLHS_idx] = 1
        for sh in short_idx:
            row[sh] = -1
        A_eq.append(row)
        b_eq.append(0)

    return {
        "n": n,
        "vars": vars_list,
        "n_vars": 3 * n,
        "prefix_idx": prefix_idx,
        "long_idx": long_idx,
        "short_idx": short_idx,
        "linkLHS_idx": linkLHS_idx,
        "A_ineq": np.array(A_ineq, dtype=float) if A_ineq else np.zeros((0, 3 * n)),
        "b_ineq": np.array(b_ineq, dtype=float) if b_ineq else np.zeros(0),
        "A_eq": np.array(A_eq, dtype=float) if A_eq else np.zeros((0, 3 * n)),
        "b_eq": np.array(b_eq, dtype=float) if b_eq else np.zeros(0),
    }


# ----------------------------------------------------------------------
# BDI polytope structure (general n)
# ----------------------------------------------------------------------

def bdi_dim(n):
    """
    BDI polytope at level n. Variables:
      M_2, ..., M_{n-1}   (n-2 vars; M_1 = 0 forced, M_n absent)
      B_1, ..., B_{n-1}   (n-1 vars)
      T_1, ..., T_{n-1}   (n-1 vars)
      S                   (1 var)
    Total: (n-2) + (n-1) + (n-1) + 1 = 3n - 3.
    No equations among variables (constraints are pure inequalities
    M_a <= P_{a-1}, M_a <= P_a, S <= P_{n-1}, T_a <= B_a, P_a >= 0).

    Returns the dim and var count.
    """
    n_vars = (n - 2) + (n - 1) + (n - 1) + 1
    assert n_vars == 3 * n - 3, n
    return n_vars  # dim = var count since no eqs


# ----------------------------------------------------------------------
# Affine hull dim from constraint system
# ----------------------------------------------------------------------

def affine_hull_dim_from_constraints(struct):
    """
    Affine hull dim = (# vars) - rank(equations) - (# inequalities always
    tight on the interior of the polytope ∩ R_+^k).

    We use rank(A_eq) for the equation part, and we check (via LP) that
    none of the inequalities is always tight by finding an interior
    point with positive slack.
    """
    n_vars = struct["n_vars"]
    A_eq = struct["A_eq"]
    A_ineq = struct["A_ineq"]
    b_ineq = struct["b_ineq"]
    b_eq = struct["b_eq"]

    rank_eq = np.linalg.matrix_rank(A_eq) if A_eq.shape[0] else 0

    # Find Chebyshev center via LP to confirm interior point exists with
    # positive slacks. Use LP: max t s.t. A_ineq x + t <= b_ineq,
    # x >= t, A_eq x = b_eq, t >= 0. Maximize t (slack magnitude).
    # Practical workaround: max t with simple LP.
    if A_ineq.shape[0] == 0:
        # All R_+^{n_vars} is feasible interior (modulo equations).
        interior_slack = float('inf')
        binding_extra = 0
    else:
        # Construct LP: variables x_1,...,x_{n_vars}, slack t.
        # max t  ==  min -t
        c = np.zeros(n_vars + 1)
        c[-1] = -1  # max t

        # Inequalities: A_ineq @ x <= b_ineq - t (slack t)
        # rewrite as: A_ineq @ x + t * 1 <= b_ineq
        A_ub = np.hstack([A_ineq, np.ones((A_ineq.shape[0], 1))])
        b_ub = b_ineq

        # x >= t : -x_i + t <= 0
        A_ub2 = []
        b_ub2 = []
        for i in range(n_vars):
            row = [0] * (n_vars + 1)
            row[i] = -1
            row[-1] = 1
            A_ub2.append(row)
            b_ub2.append(0)
        A_ub2 = np.array(A_ub2, dtype=float)
        b_ub2 = np.array(b_ub2, dtype=float)

        A_ub_full = np.vstack([A_ub, A_ub2])
        b_ub_full = np.concatenate([b_ub, b_ub2])

        if A_eq.shape[0]:
            A_eq_full = np.hstack([A_eq, np.zeros((A_eq.shape[0], 1))])
            b_eq_full = b_eq
        else:
            A_eq_full = None
            b_eq_full = None

        # Bounds: 0 <= t <= 1, 0 <= x_i <= 1000 (bounded box for LP)
        bounds = [(0, 1000)] * n_vars + [(0, 1)]

        res = linprog(c, A_ub=A_ub_full, b_ub=b_ub_full,
                      A_eq=A_eq_full, b_eq=b_eq_full,
                      bounds=bounds, method="highs")
        if not res.success:
            print(f"  WARNING: LP failed: {res.message}")
            interior_slack = 0
            binding_extra = 0
        else:
            t_max = -res.fun
            if t_max <= 1e-8:
                # Some inequality is always tight; LP can't escape.
                # Need to find which.
                interior_slack = 0
                # Find binding inequalities
                x_int = res.x[:n_vars]
                binding = []
                for k in range(A_ineq.shape[0]):
                    slack = b_ineq[k] - A_ineq[k] @ x_int
                    if abs(slack) < 1e-6:
                        binding.append(k)
                # Rank of the binding inequalities NOT in span of A_eq
                # gives extra reduction.
                if binding:
                    A_bind = A_ineq[binding]
                    if A_eq.shape[0]:
                        A_stack = np.vstack([A_eq, A_bind])
                        rank_stack = np.linalg.matrix_rank(A_stack)
                        binding_extra = rank_stack - rank_eq
                    else:
                        binding_extra = np.linalg.matrix_rank(A_bind)
                else:
                    binding_extra = 0
            else:
                interior_slack = t_max
                binding_extra = 0

    dim = n_vars - rank_eq - binding_extra
    return {
        "n_vars": n_vars,
        "rank_eq": rank_eq,
        "binding_extra": binding_extra,
        "interior_slack": interior_slack,
        "dim": dim,
    }


# ----------------------------------------------------------------------
# Sanity check: enumerate lattice points at small N and fit affine span
# ----------------------------------------------------------------------

def enumerate_aii_lattice_points(struct, N_max):
    """
    Direct enumeration of integer points x >= 0 with sum(x) <= N_max,
    satisfying A_ineq @ x <= b_ineq and A_eq @ x = b_eq.

    Slow for large N or many variables; we use N_max=2 or 3 for n=5,6.
    """
    n_vars = struct["n_vars"]
    A_ineq = struct["A_ineq"]
    b_ineq = struct["b_ineq"]
    A_eq = struct["A_eq"]
    b_eq = struct["b_eq"]

    pts = []
    # Generate all x_i >= 0 with sum <= N_max
    def gen(remaining, depth, current):
        if depth == n_vars:
            x = np.array(current, dtype=float)
            if A_ineq.shape[0] and not np.all(A_ineq @ x <= b_ineq + 1e-9):
                return
            if A_eq.shape[0] and not np.all(np.abs(A_eq @ x - b_eq) < 1e-9):
                return
            pts.append(current.copy())
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()

    gen(N_max, 0, [])
    return pts


def construct_independent_feasible(struct):
    """
    Explicitly construct a list of dim+1 feasible lattice points whose
    affine span has the expected dim. Strategy:

    Base point: x = 0 (always feasible since A_eq @ 0 = 0 = b_eq,
                       A_ineq @ 0 = 0 <= b_ineq).

    For each "free" direction (variable that doesn't appear in any
    binding equation or always-tight inequality), the unit vector e_i
    scaled by 1 is feasible IF Main_i for that variable allows. We pad
    by prefix vars (which have no upper bound) as needed.

    Specifically:
      - For each prefix var: e_{prefix[i]} feasible (no constraint).
      - For each long[i] (i=2..n): set prefix[i-1] = 1, long[i] = 1.
        Main_i: 1 + 0 <= 1 ✓. Point span includes both prefix[i-1]
        and long[i] directions.
      - For long[1] (which doesn't appear in any Main_i): e_{long[1]}
        directly.
      - For each short[i] (i=2..n-1 even n, 2..n odd n) that appears
        in Main_i: set prefix[i-1] = 1, short[i] = 1.
      - For short[1] (which doesn't appear in Main_i): e_{short[1]} (but
        constrained by linking eq at even n).
      - At even n, linkLHS = sum of shorts, so linkLHS = 1 paired with
        short[1] = 1 (and other shorts 0) is feasible.

    Returns list of points (each a list of length n_vars).
    """
    n = struct["n"]
    n_vars = struct["n_vars"]
    prefix_idx = struct["prefix_idx"]
    long_idx = struct["long_idx"]
    short_idx = struct["short_idx"]
    linkLHS_idx = struct["linkLHS_idx"]
    A_ineq = struct["A_ineq"]
    b_ineq = struct["b_ineq"]
    A_eq = struct["A_eq"]
    b_eq = struct["b_eq"]

    pts = []

    def zero():
        return [0] * n_vars

    def add(p):
        # Verify feasibility before adding.
        x = np.array(p, dtype=float)
        if A_ineq.shape[0] and not np.all(A_ineq @ x <= b_ineq + 1e-9):
            raise AssertionError(f"Inequality violated by point {p}")
        if A_eq.shape[0] and not np.all(np.abs(A_eq @ x - b_eq) < 1e-9):
            raise AssertionError(f"Equation violated by point {p}")
        pts.append(p)

    # Base: zero vector.
    add(zero())

    # Prefix vars: e_i for each.
    for pi in prefix_idx:
        p = zero(); p[pi] = 1
        add(p)

    # long[1] (i=0 in 0-indexed): doesn't appear in any Main_i.
    p = zero(); p[long_idx[0]] = 1
    add(p)

    # long[i] for i=2..n: needs prefix[i-1] = 1 to satisfy Main_i.
    for i in range(2, n + 1):
        p = zero()
        p[prefix_idx[i - 2]] = 1
        p[long_idx[i - 1]] = 1
        add(p)

    # short[i] for i=2..(n or n-1): needs prefix[i-1] = 1.
    # At even n, short_idx = [s[1], s[2], ..., s[n-1]] (n-1 entries).
    # At odd n, short_idx = [s[1], s[2], ..., s[n]] (n entries).
    for k, si in enumerate(short_idx[1:], start=2):
        # k is the index (2, 3, ...) of this short var.
        # short[k] appears in Main_k IF k <= n (i.e., k-th Main exists)
        # AND short[k] is in Main_k's LHS (which is true unless even n
        # and k==n).
        if n % 2 == 0 and k == n:
            # short[n] doesn't exist for even n; skip.
            continue
        p = zero()
        p[prefix_idx[k - 2]] = 1
        p[si] = 1
        # At even n, also set linkLHS = 1 to satisfy linking equation.
        if n % 2 == 0:
            p[linkLHS_idx] = 1
        add(p)

    # short[1] direction: at even n, linkLHS is linked, so use the
    # point (short[1] = 1, linkLHS = 1, rest 0). This is feasible since
    # short[1] doesn't appear in any Main_i.
    # At odd n, short[1] = 1 alone is feasible (no linkLHS, no Main).
    if n % 2 == 0:
        p = zero()
        p[short_idx[0]] = 1
        p[linkLHS_idx] = 1
        add(p)
    else:
        p = zero()
        p[short_idx[0]] = 1
        add(p)

    return pts


def affine_span_dim(points):
    """Affine span dim = rank of (P - p_0)."""
    if len(points) < 2:
        return 0
    P = np.array(points, dtype=float)
    P0 = P - P[0]
    return int(np.linalg.matrix_rank(P0))


# ----------------------------------------------------------------------
# Main: tabulate dim AII, dim BDI, gap at n = 3..6 and verify n=5, 6.
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("Day 60 Task 1: Computational dim-gap verification at n = 5, 6")
    print("=" * 72)
    print()

    for n in [3, 4, 5, 6]:
        print(f"--- n = {n} ({'odd' if n%2 else 'even'}) ---")
        struct = aii_structure(n)
        print(f"AII polytope:")
        print(f"  # variables: {struct['n_vars']}")
        print(f"  # inequalities (Main_i): {struct['A_ineq'].shape[0]}")
        print(f"  # equations (linking): {struct['A_eq'].shape[0]}")
        if struct["A_eq"].shape[0]:
            print(f"  Equation rank: {np.linalg.matrix_rank(struct['A_eq'])}")
            print(f"  Equation: linkLHS = sum of short[1..{n-1}]")

        info = affine_hull_dim_from_constraints(struct)
        print(f"  Interior slack (LP Chebyshev): {info['interior_slack']:.4f}")
        print(f"  Affine hull dim of AII = {info['dim']}")

        dim_bdi = bdi_dim(n)
        print(f"BDI polytope:")
        print(f"  # variables = dim = {dim_bdi}")

        gap = info["dim"] - dim_bdi
        print(f"  *** dim gap = {info['dim']} - {dim_bdi} = {gap} ***")
        print()

    # Cross-check 1: explicit construction of independent feasible points
    print("=" * 72)
    print("Cross-check (explicit): construct dim+1 independent feasible points")
    print("=" * 72)
    for n in [3, 4, 5, 6]:
        struct = aii_structure(n)
        pts = construct_independent_feasible(struct)
        d = affine_span_dim(pts)
        print(f"  n={n}: constructed {len(pts)} feasible pts, affine span dim = {d}"
              f"  (expected {3*n if n%2 else 3*n-1})")

    print()
    print("=" * 72)
    print("Summary:")
    print("=" * 72)
    print(f"{'n':>3} | {'dim AII':>10} | {'dim BDI':>10} | {'gap':>5}")
    print("-" * 40)
    for n in [3, 4, 5, 6]:
        struct = aii_structure(n)
        info = affine_hull_dim_from_constraints(struct)
        dim_bdi = bdi_dim(n)
        gap = info["dim"] - dim_bdi
        print(f"{n:>3} | {info['dim']:>10} | {dim_bdi:>10} | {gap:>5}")


if __name__ == "__main__":
    main()
