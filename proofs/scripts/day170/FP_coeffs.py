"""Self-contained FP_coeffs — raw umbral definition of F_P.

Extracted from scratch/day152/lib.py so the Day 170 provenance pipeline
(step11 -> step13 -> step18) is reproducible from the shipped repo alone.

Definition (Day 152, clean-room):
    F_P(u_1, u_2, u_3; T) = [1 / V(u)] * T^+(exp(T * e_2(u)) * V(u))
where V(u) = (u_1 - u_2)(u_1 - u_3)(u_2 - u_3) is the Vandermonde and T^+
sends monomials u_1^i u_2^j u_3^k to rising factorials u_1^{(i)} u_2^{(j)} u_3^{(k)}.

FP_coeffs(N) returns the list of [T^n] F_P for n = 0, 1, ..., N, each as a
u-polynomial represented as a dict {(i, j, k): Fraction}.

Only stdlib imports (fractions, itertools, collections, math).
"""
from fractions import Fraction as Fr
from itertools import product  # noqa: F401 (kept for parity with the original library)
from collections import defaultdict
import math

# ---- polynomial primitives on dict {(i, j, k): Fraction} ----

def pzero():
    return {}

def pconst(c):
    return {(0, 0, 0): Fr(c)} if c else {}

def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        w = r.get(k, Fr(0)) + v
        if w:
            r[k] = w
        elif k in r:
            del r[k]
    return r

def pneg(a):
    return {k: -v for k, v in a.items()}

def psub(a, b):
    return padd(a, pneg(b))

def pscal(a, c):
    c = Fr(c)
    if c == 0:
        return {}
    return {k: v * c for k, v in a.items()}

def pmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
            w = r.get(k, Fr(0)) + v1 * v2
            if w:
                r[k] = w
            elif k in r:
                del r[k]
    return r

def ppow(a, n):
    r = pconst(1)
    for _ in range(n):
        r = pmul(r, a)
    return r

# ---- fixed generators ----

U = [{(1, 0, 0): Fr(1)}, {(0, 1, 0): Fr(1)}, {(0, 0, 1): Fr(1)}]
E1u = padd(padd(U[0], U[1]), U[2])
E2u = padd(padd(pmul(U[0], U[1]), pmul(U[0], U[2])), pmul(U[1], U[2]))
E3u = pmul(pmul(U[0], U[1]), U[2])
V = pmul(pmul(psub(U[0], U[1]), psub(U[0], U[2])), psub(U[1], U[2]))

# ---- exact division by linear factor and by the Vandermonde ----

def divlin(a, i, j):
    """exact division of a by (u_i - u_j), i < j. synthetic division in variable i."""
    byd = defaultdict(dict)
    for k, v in a.items():
        d = k[i]
        rest = list(k)
        rest[i] = 0
        byd[d][tuple(rest)] = v
    D = max(byd) if byd else 0
    q = {}
    carry = {}
    for d in range(D, 0, -1):
        carry = padd(byd.get(d, {}), pmul(carry, U[j]))
        for k, v in carry.items():
            kk = list(k)
            kk[i] = d - 1
            kk = tuple(kk)
            w = q.get(kk, Fr(0)) + v
            if w:
                q[kk] = w
            elif kk in q:
                del q[kk]
    rem = padd(byd.get(0, {}), pmul(carry, U[j]))
    assert not rem, "not divisible"
    return q

def divV(a):
    return divlin(divlin(divlin(a, 1, 2), 0, 2), 0, 1)

# ---- rising factorials and the umbral map T^+ ----

def rising(x_index, n):
    """u^{(n)} = u(u+1)...(u+n-1) as poly in variable x_index"""
    r = pconst(1)
    for s in range(n):
        r = pmul(r, padd(U[x_index], pconst(s)))
    return r

_RIS = {}

def Tplus(a):
    r = {}
    for k, v in a.items():
        key = k
        if key not in _RIS:
            p = pconst(1)
            for i in range(3):
                p = pmul(p, rising(i, k[i]))
            _RIS[key] = p
        for kk, vv in _RIS[key].items():
            w = r.get(kk, Fr(0)) + v * vv
            if w:
                r[kk] = w
            elif kk in r:
                del r[kk]
    return r

# ---- main entry point ----

def FP_coeffs(N):
    """[T^n] F_P for n = 0..N, as u-polys (dict {(i, j, k): Fraction})."""
    out = []
    e2b = pconst(1)
    for b in range(N + 1):
        Pb = divV(Tplus(pmul(e2b, V)))
        out.append(pscal(Pb, Fr(1, math.factorial(b))))
        e2b = pmul(e2b, E2u)
    return out
