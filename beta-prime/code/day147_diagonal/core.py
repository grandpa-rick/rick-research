"""Day 146 core: fast dict-based polynomial arithmetic in Z[E1,E2,E3],
Psi recursion, P_b = phi(Psi_b), and b_k extraction."""
from fractions import Fraction
from collections import defaultdict

# monomial = (a,b,c) meaning E1^a E2^b E3^c ; poly = dict mono->int

def pmul(P, Q):
    R = defaultdict(int)
    for m1, c1 in P.items():
        if c1 == 0: continue
        for m2, c2 in Q.items():
            if c2 == 0: continue
            R[(m1[0]+m2[0], m1[1]+m2[1], m1[2]+m2[2])] += c1*c2
    return {m: c for m, c in R.items() if c}

def padd(*Ps):
    R = defaultdict(int)
    for P in Ps:
        for m, c in P.items():
            R[m] += c
    return {m: c for m, c in R.items() if c}

def pscal(k, P):
    if k == 0: return {}
    return {m: k*c for m, c in P.items()}

ONE = {(0,0,0): 1}
E1 = {(1,0,0): 1}
E2 = {(0,1,0): 1}
E3 = {(0,0,1): 1}

def const(k):
    return {(0,0,0): k} if k else {}

def ppow(P, n):
    R = ONE
    for _ in range(n):
        R = pmul(R, P)
    return R

# sigma: E1 -> E1-3, E2 -> E2-2E1+3, E3 -> E3-E2+E1-1
S1 = padd(E1, const(-3))
S2 = padd(E2, pscal(-2, E1), const(3))
S3 = padd(E3, pscal(-1, E2), E1, const(-1))

def sigma(P):
    # cache powers
    maxa = max((m[0] for m in P), default=0)
    maxb = max((m[1] for m in P), default=0)
    maxc = max((m[2] for m in P), default=0)
    A = [ONE]; B = [ONE]; C = [ONE]
    for i in range(maxa): A.append(pmul(A[-1], S1))
    for i in range(maxb): B.append(pmul(B[-1], S2))
    for i in range(maxc): C.append(pmul(C[-1], S3))
    out = defaultdict(int)
    for (a,b,c), co in P.items():
        t = pmul(pmul(A[a], B[b]), C[c])
        for m, cc in t.items():
            out[m] += co*cc
    return {m: c for m, c in out.items() if c}

def phi(P):
    # E1 -> -E1, E3 -> -E3
    return {m: (c if (m[0]+m[2]) % 2 == 0 else -c) for m, c in P.items()}

def build_Psi(B_max):
    Psi = {0: ONE, 1: padd(E2, pscal(-1, E1), const(1))}
    for b in range(1, B_max):
        c = b+1
        t1 = pmul(padd(E2, pscal(-c, E1), const(c*c)), Psi[b])
        t2 = pscal(3*b, pmul(E3, sigma(Psi[b-1])))
        if b >= 2:
            t3 = pscal(b*(b-1), pmul(pmul(padd(E1, const(-2*b-2)), E3), sigma(Psi[b-2])))
        else:
            t3 = {}
        Psi[b+1] = padd(t1, pscal(-1, t2), pscal(-1, t3))
    return Psi

def build_P(B_max):
    Psi = build_Psi(B_max)
    return {b: phi(Psi[b]) for b in range(B_max+1)}

def subs_E12(P, e1, e2):
    """substitute numeric E1,E2 -> dict {E3-power: value}"""
    out = defaultdict(int)
    for (a,b,c), co in P.items():
        out[c] += co * (e1**a) * (e2**b)
    return {k: v for k, v in out.items() if v}

def E3deg(P):
    return max((m[2] for m in P), default=-1)
