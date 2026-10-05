#!/usr/bin/env python3
"""Fast independent re-derivation of H = tau(F_P)/F_P from the DEFINITION, to T^14.

Key simplification: tau (u_i -> u_i+1) fixes V, so with A_n := T^+(e2^n V) = n! * [T^n](F_P * V),
   H = tau(F_P)/F_P = tau(F_P V)/(F_P V),
and the recursion is pure integer arithmetic:
   n! * V * H_n = tau(A_n) - sum_{k=1}^{n} (n!/k!) * A_k * H_{n-k}.
No sympy; compared monomial-by-monomial against day149/H16.pkl expanded into u-coordinates.
"""
import pickle, math, sys
from collections import defaultdict

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 14

def mul(A, B):
    R = defaultdict(int)
    for m1, c1 in A.items():
        for m2, c2 in B.items():
            R[(m1[0]+m2[0], m1[1]+m2[1], m1[2]+m2[2])] += c1*c2
    return {m: c for m, c in R.items() if c}
def add(A, B):
    R = defaultdict(int)
    for X in (A, B):
        for m, c in X.items(): R[m] += c
    return {m: c for m, c in R.items() if c}
def scal(k, A): return {m: k*c for m, c in A.items()} if k else {}

# V = (u1-u2)(u1-u3)(u2-u3)
V = mul(mul({(1,0,0):1,(0,1,0):-1}, {(1,0,0):1,(0,0,1):-1}), {(0,1,0):1,(0,0,1):-1})
E2 = {(1,1,0):1,(1,0,1):1,(0,1,1):1}
E1 = {(1,0,0):1,(0,1,0):1,(0,0,1):1}
E3 = {(1,1,1):1}

# unsigned Stirling numbers of the first kind: x^{(n)} = sum_k st[n][k] x^k
D = NMAX*2 + 8
st = [[0]*(D+1) for _ in range(D+1)]; st[0][0] = 1
for n in range(1, D+1):
    for k in range(1, n+1):
        st[n][k] = st[n-1][k-1] + (n-1)*st[n-1][k]

def Tplus(A):
    """u^alpha -> prod_i u_i^{(alpha_i)} (rising factorial)"""
    R = defaultdict(int)
    for (i,j,k), c in A.items():
        for a in range(i+1):
            if not st[i][a]: continue
            ca = c*st[i][a]
            for b in range(j+1):
                if not st[j][b]: continue
                cb = ca*st[j][b]
                for d in range(k+1):
                    if not st[k][d]: continue
                    R[(a,b,d)] += cb*st[k][d]
    return {m: c for m, c in R.items() if c}

binom = [[math.comb(n,k) for k in range(D+1)] for n in range(D+1)]
def tau(A):
    """u_i -> u_i + 1"""
    R = defaultdict(int)
    for (i,j,k), c in A.items():
        for a in range(i+1):
            ca = c*binom[i][a]
            for b in range(j+1):
                cb = ca*binom[j][b]
                for d in range(k+1):
                    R[(a,b,d)] += cb*binom[k][d]
    return {m: c for m, c in R.items() if c}

def divlin(A, p, q):
    """exact division by (u_p - u_q); synthetic division treating u_p as main variable"""
    # write A = sum_d c_d(rest) u_p^d ; dividing by (u_p - u_q):
    # quotient Q with Q_{d-1} = A_d + u_q * Q_d  (descending)
    byd = defaultdict(dict)
    for m, c in A.items():
        rest = list(m); dpow = rest[p]; rest[p] = 0
        byd[dpow][tuple(rest)] = c
    dmax = max(byd) if byd else 0
    Qd = {}
    out = defaultdict(int)
    rem = {}
    for d in range(dmax, -1, -1):
        cur = add(dict(byd.get(d, {})), Qd)      # A_d + u_q*Q_d  (Qd already multiplied)
        if d == 0:
            rem = cur
            break
        # Q_{d-1} = cur
        for m, c in cur.items():
            mm = list(m); mm[p] = d-1
            out[tuple(mm)] += c
        # prepare u_q * Q_{d-1} for next round
        Qd = {}
        for m, c in cur.items():
            mm = list(m); mm[q] += 1
            Qd[tuple(mm)] = c
    assert not {m: c for m, c in rem.items() if c}, "division by (u%d-u%d) not exact" % (p, q)
    return {m: c for m, c in out.items() if c}

def divV(A):
    return divlin(divlin(divlin(A, 0, 1), 0, 2), 1, 2)

# A_n = T^+(e2^n V)
A = []
cur = dict(V)
for n in range(NMAX+1):
    A.append(Tplus(cur))
    cur = mul(cur, E2)

# n! V H_n = tau(A_n) - sum_{k=1}^n (n!/k!) A_k H_{n-k}
H = []
for n in range(NMAX+1):
    acc = tau(A[n])
    for k in range(1, n+1):
        acc = add(acc, scal(-(math.factorial(n)//math.factorial(k)), mul(A[k], H[n-k])))
    fn = math.factorial(n)
    assert all(c % fn == 0 for c in acc.values()), n
    acc = {m: c//fn for m, c in acc.items()}
    H.append(divV(acc))
    print("  T^%d built (#mon %d)" % (n, len(H[n]))); sys.stdout.flush()

# compare against H16.pkl
ref = pickle.load(open('/home/agent/projects/beta-prime/code/day149/H16.pkl', 'rb'))
def Emon(a, b, c):
    r = {(0,0,0):1}
    for _ in range(a): r = mul(r, E1)
    for _ in range(b): r = mul(r, E2)
    for _ in range(c): r = mul(r, E3)
    return r
allok = True
for n in range(NMAX+1):
    R = {}
    for (a,b,c), co in ref[n].items(): R = add(R, scal(co, Emon(a,b,c)))
    ok = (R == H[n]); allok &= ok
    print("T^%d : match=%s" % (n, ok))
print("INDEPENDENT CHECK of H16.pkl to T^%d: %s" % (NMAX, "PASS" if allok else "FAIL"))
