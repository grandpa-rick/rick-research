"""Verify uniform-n R-double / prefix[n] / long[1] constructions are
BDI-feasible at n=3, 4, 5, 6, 7. Sanity check before writeup."""

import numpy as np


def make_base(n):
    """Standard base piece at level n. Returns dict mapping AII var indices to BDI coefficient lists.
    AII vars indexed 0..3n-1: prefix 0..n-1, long n..2n-1, short 2n..3n-1.
    BDI vars indexed: M_2..M_{n-1}, B_1, T_1, ..., B_{n-1}, T_{n-1}, S.
    """
    nAII = 3 * n
    P = list(range(n))            # P[i] = prefix[i+1] idx
    L = list(range(n, 2*n))        # L[i] = long[i+1] idx
    S = list(range(2*n, 3*n))      # S[i] = short[i+1] idx
    BDI_vars = []
    M = {}
    for i in range(2, n):
        M[i] = len(BDI_vars); BDI_vars.append(f"M_{i}")
    Bb = {}; Tt = {}
    for i in range(1, n):
        Bb[i] = len(BDI_vars); BDI_vars.append(f"B_{i}")
        Tt[i] = len(BDI_vars); BDI_vars.append(f"T_{i}")
    Sn = len(BDI_vars); BDI_vars.append("S")
    nBDI = len(BDI_vars)
    pi = np.zeros((nBDI, nAII), dtype=int)
    # M_i <- l_i for i=2..n-1
    for i in range(2, n):
        pi[M[i], L[i-1]] += 1
    # B_1 <- p_1 + s_1 + l_1
    pi[Bb[1], P[0]] += 1
    pi[Bb[1], S[0]] += 1
    pi[Bb[1], L[0]] += 1
    # T_1 <- s_1
    pi[Tt[1], S[0]] += 1
    # B_i, T_i for i=2..n-1
    for i in range(2, n):
        pi[Bb[i], P[i-1]] += 1
        pi[Bb[i], S[i-1]] += 1
        pi[Tt[i], S[i-1]] += 1
    # S <- l_n
    pi[Sn, L[n-1]] += 1
    return pi, P, L, S, Bb, Tt, M, Sn, BDI_vars


def make_rdouble(n, alpha):
    """Level-1 R-double piece."""
    pi, P, L, S, Bb, Tt, M, Sn, BV = make_base(n)
    # Override B_1, T_1, S.
    # B_1 <- p_1 + 2 s_1 + l_1
    pi[Bb[1], :] = 0
    pi[Bb[1], P[0]] += 1
    pi[Bb[1], S[0]] += 2
    pi[Bb[1], L[0]] += 1
    # T_1 <- s_1 + l_1
    pi[Tt[1], :] = 0
    pi[Tt[1], S[0]] += 1
    pi[Tt[1], L[0]] += 1
    # S <- l_n + 2 s_{n-1} + 2 s_1 + alpha p_1
    pi[Sn, :] = 0
    pi[Sn, L[n-1]] += 1
    pi[Sn, S[n-2]] += 2
    pi[Sn, S[0]] += 2
    pi[Sn, P[0]] += alpha
    return pi, BV


def make_pn_variant(n, k):
    """Add k p_n to (B_{n-1}, T_{n-1})."""
    pi, P, L, S, Bb, Tt, M, Sn, BV = make_base(n)
    pi[Bb[n-1], P[n-1]] += k
    pi[Tt[n-1], P[n-1]] += k
    return pi, BV


def make_l1_variant(n, k):
    """Vary multiplicity of l_1 in B_1. k=1 standard, k=2,3 variants."""
    pi, P, L, S, Bb, Tt, M, Sn, BV = make_base(n)
    pi[Bb[1], L[0]] = k
    return pi, BV


def feasible(pi, n):
    """Test BDI feasibility on AII lattice points up to small sum."""
    nAII = 3 * n
    # AII feasibility: l_i + s_i <= p_{i-1} for i=2..n
    # All vars >= 0.
    # BDI feasibility: T_i <= B_i, M_i <= P_{i-1}, M_i <= P_i, S <= P_{n-1}, P_i >= 0.
    P = list(range(n)); L = list(range(n, 2*n)); S = list(range(2*n, 3*n))
    BDI_vars_names = []
    M = {}
    for i in range(2, n):
        M[i] = len(BDI_vars_names); BDI_vars_names.append(f"M_{i}")
    Bb = {}; Tt = {}
    for i in range(1, n):
        Bb[i] = len(BDI_vars_names); BDI_vars_names.append(f"B_{i}")
        Tt[i] = len(BDI_vars_names); BDI_vars_names.append(f"T_{i}")
    Sn = len(BDI_vars_names); BDI_vars_names.append("S")
    
    def gen(remaining, depth, cur):
        if depth == nAII:
            ok = True
            # AII feasible?
            for i in range(2, n+1):
                if cur[L[i-1]] + cur[S[i-1]] > cur[P[i-2]]:
                    ok = False; break
            if not ok:
                return None
            q = pi @ np.array(cur)
            # BDI feasible?
            for i in range(1, n):
                if q[Tt[i]] > q[Bb[i]]:
                    return (tuple(cur), q, f"T_{i}>B_{i}")
            Pa = [0] * n
            Pa[0] = 2 * (q[Bb[1]] - q[Tt[1]])
            if Pa[0] < 0:
                return (tuple(cur), q, f"P_1<0")
            for i in range(2, n):
                Pa[i-1] = Pa[i-2] + 2*(q[Bb[i]] - q[Tt[i]])
                if Pa[i-1] < 0:
                    return (tuple(cur), q, f"P_{i}<0")
            for i in range(2, n):
                if q[M[i]] > Pa[i-2]:
                    return (tuple(cur), q, f"M_{i}<=P_{i-1}")
                if q[M[i]] > Pa[i-1]:
                    return (tuple(cur), q, f"M_{i}<=P_{i}")
            if q[Sn] > Pa[n-2]:
                return (tuple(cur), q, f"S<=P_{n-1}")
            return None
        for v in range(remaining + 1):
            cur.append(v)
            r = gen(remaining - v, depth + 1, cur)
            cur.pop()
            if r is not None:
                return r
        return None
    bad = gen(3, 0, [])  # up to sum 3
    return bad


for n in [3, 4, 5, 6, 7]:
    print(f"\n=== n={n} ===")
    for alpha in [0, 1, 2, 3]:
        pi, _ = make_rdouble(n, alpha)
        bad = feasible(pi, n)
        status = "FEAS" if bad is None else f"INFEAS at p={bad[0]}: {bad[2]}"
        print(f"  Rd_{n}(α={alpha}): {status}")
    for k in [0, 1, 2]:
        pi, _ = make_pn_variant(n, k)
        bad = feasible(pi, n)
        status = "FEAS" if bad is None else f"INFEAS at p={bad[0]}: {bad[2]}"
        print(f"  Pn_{n}(k={k}): {status}")
    for k in [0, 1, 2, 3]:
        pi, _ = make_l1_variant(n, k)
        bad = feasible(pi, n)
        status = "FEAS" if bad is None else f"INFEAS at p={bad[0]}: {bad[2]}"
        print(f"  L1_{n}(k={k}): {status}")
