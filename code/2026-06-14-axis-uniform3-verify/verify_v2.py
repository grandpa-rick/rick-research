"""Verify R-double recipe for n>=4 with the corrected p_n in (B_2,T_2) routing."""
import numpy as np


def make_rdouble_v2(n, alpha, even_with_lambda=False):
    """R-double at n>=4: B_1 doubles s_1, p_n in (B_2,T_2) balanced,
    S has 2 s_{n-1} + 2 s_1 + α p_1.
    
    AII indexing: 0..n-1 = prefix, n..2n-1 = long, 2n..3n-1 = short (for odd n) or 2n..3n-2 = short + 3n-1 = lambda (even n).
    BDI: M_2..M_{n-1}, B_1, T_1, ..., B_{n-1}, T_{n-1}, S.
    """
    P = list(range(n))
    L = list(range(n, 2*n))
    S_short = list(range(2*n, 3*n))  # use 3n for both, treating last as Λ at even n
    nAII = 3 * n
    M = {}
    Bb = {}
    Tt = {}
    BDI = []
    for i in range(2, n):
        M[i] = len(BDI); BDI.append(f"M_{i}")
    for i in range(1, n):
        Bb[i] = len(BDI); BDI.append(f"B_{i}")
        Tt[i] = len(BDI); BDI.append(f"T_{i}")
    Sn = len(BDI); BDI.append("S")
    nBDI = len(BDI)
    pi = np.zeros((nBDI, nAII), dtype=int)
    for i in range(2, n):
        pi[M[i], L[i-1]] = 1
    # B_1: p_1 + 2 s_1 + l_1
    pi[Bb[1], P[0]] = 1
    pi[Bb[1], S_short[0]] = 2
    pi[Bb[1], L[0]] = 1
    # T_1: s_1 + l_1
    pi[Tt[1], S_short[0]] = 1
    pi[Tt[1], L[0]] = 1
    # B_2: p_2 + s_2 + p_n
    pi[Bb[2], P[1]] = 1
    pi[Bb[2], S_short[1]] = 1
    pi[Bb[2], P[n-1]] = 1
    # T_2: s_2 + p_n
    pi[Tt[2], S_short[1]] = 1
    pi[Tt[2], P[n-1]] = 1
    # B_i, T_i for 3..n-2
    for i in range(3, n - 1):
        pi[Bb[i], P[i-1]] = 1
        pi[Bb[i], S_short[i-1]] = 1
        pi[Tt[i], S_short[i-1]] = 1
    # B_{n-1}, T_{n-1}
    if n > 2:
        pi[Bb[n-1], P[n-2]] = 1
        pi[Bb[n-1], S_short[n-2]] = 1
        pi[Tt[n-1], S_short[n-2]] = 1
        # Λ at even n
        if even_with_lambda and n % 2 == 0:
            pi[Bb[n-1], S_short[n-1]] = 1  # treating last short index as Λ
            pi[Tt[n-1], S_short[n-1]] = 1
    # S: l_n + 2 s_{n-1} + 2 s_1 + α p_1
    pi[Sn, L[n-1]] = 1
    pi[Sn, S_short[n-2]] = 2
    pi[Sn, S_short[0]] = pi[Sn, S_short[0]] + 2  # accumulate
    pi[Sn, P[0]] = alpha
    return pi, BDI, P, L, S_short, M, Bb, Tt, Sn


def feasible_v2(pi, n, S_short, P, L, M, Bb, Tt, Sn, even=False):
    nAII = 3 * n
    def gen(remaining, depth, cur):
        if depth == nAII:
            # AII feasible?
            for i in range(2, n+1):
                if i == n and even:
                    # at even n, Main_n: l_n <= p_{n-1} (no s_n)
                    if cur[L[i-1]] > cur[P[i-2]]:
                        return None  # not feasible AII, skip
                else:
                    if cur[L[i-1]] + cur[S_short[i-1]] > cur[P[i-2]]:
                        return None  # not feasible AII, skip
            # linkLHS at even n: not implemented; ignore
            q = pi @ np.array(cur)
            for i in range(1, n):
                if q[Tt[i]] > q[Bb[i]]:
                    return (tuple(cur), q.tolist(), f"T_{i}>B_{i}")
            Pa = [0] * (n + 1)
            Pa[0] = 0
            for i in range(1, n):
                Pa[i] = Pa[i-1] + 2*(q[Bb[i]] - q[Tt[i]])
                if Pa[i] < 0:
                    return (tuple(cur), q.tolist(), f"P_{i}<0")
            for i in range(2, n):
                if q[M[i]] > Pa[i-1]:
                    return (tuple(cur), q.tolist(), f"M_{i}<=P_{i-1}")
                if q[M[i]] > Pa[i]:
                    return (tuple(cur), q.tolist(), f"M_{i}<=P_{i}")
            if q[Sn] > Pa[n-1]:
                return (tuple(cur), q.tolist(), f"S<=P_{n-1}")
            return None
        for v in range(remaining + 1):
            cur.append(v)
            r = gen(remaining - v, depth + 1, cur)
            cur.pop()
            if r is not None and len(r) == 3 and 'feasible' not in r[2]:
                return r
        return None
    return gen(4, 0, [])

print("Recipe V2 (with p_n in (B_2,T_2) balanced):")
for n in [3, 4, 5, 6, 7]:
    print(f"\n=== n={n} ===")
    even = (n % 2 == 0)
    for alpha in [0, 1, 2, 3]:
        pi, BDI, P, L, S_short, M, Bb, Tt, Sn = make_rdouble_v2(n, alpha, even_with_lambda=even)
        bad = feasible_v2(pi, n, S_short, P, L, M, Bb, Tt, Sn, even=even)
        if bad is None:
            print(f"  Rd_{n}(α={alpha}): FEAS")
        else:
            print(f"  Rd_{n}(α={alpha}): INFEAS at p={bad[0]} ({bad[2]})")
