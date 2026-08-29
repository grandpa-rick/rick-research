"""Look for a RECURSION on S_j that preserves e-wdeg <= j.

Idea: maybe S_{j+1} = A(u, y, c) * S_j + B(u, y, c) * S_{j-1} + ... for some operators
A, B... with e-wdeg <= 2 (for A) so that if e-wdeg(S_j) <= j, then e-wdeg(A * S_j) <= j + 2
which is TOO BIG. But if we subtract off cleverly, we may get j+1.

Alternate idea: perhaps  S_{j+1} - e_2 * S_j  has e-wdeg <= j (i.e., e-wdeg decreases by 1
relative to S_{j+1}).  If so, induction is easy.

Or perhaps  S_{j+1} = e_2 * S_j + T_j  where e-wdeg(T_j) <= j-1 (or something).

Also test: is  S_j  itself expressible as  a polynomial in (e_2, e_1 e_2 - e_3, ...)  ?
Sometimes structure hides in a nonstandard basis.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer


u_var, y_var, c = symbols('u y c')
e1_v, e2_v, e3_v = symbols('e1 e2 e3')


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def bt(M):
    def vs(mu):
        L = len(mu) + 2
        bb = list(mu) + [0] * (L - len(mu))
        r = []
        for pp in combinations(range(L), 2):
            n = bb.copy()
            for i in pp:
                n[i] += 1
            ok = True
            for i in range(L - 1):
                if n[i] < n[i + 1]:
                    ok = False
                    break
            if not ok:
                continue
            while n and n[-1] == 0:
                n.pop()
            if len(n) > 3:
                continue
            r.append(tuple(n))
        return r
    cu = defaultdict(int)
    cu[()] = 1
    T = {0: [((0, 0, 0), 1)]}
    for jj in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[jj] = rs
    return T


def V_uyc():
    return (u_var - y_var) * (u_var - c) * (y_var - c)


def S_of_uyc(jj, tables):
    xs = (u_var, y_var, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    total = expand(total)
    V = V_uyc()
    q, r = sp.div(Poly(total, u_var, y_var, c), Poly(V, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def to_elem_uyc(F):
    """Rewrite symmetric F(u, y, c) in (e1, e2, e3)."""
    F = expand(F)
    result = Integer(0)
    while True:
        F = expand(F)
        P = Poly(F, u_var, y_var, c)
        if P.total_degree() < 0 or P.as_expr() == 0:
            break
        terms = sorted(P.terms(), reverse=True)
        (dm, cf) = terms[0]
        du, dy, dc = dm
        if not (du >= dy >= dc):
            return None
        result += cf * e1_v ** (du - dy) * e2_v ** (dy - dc) * e3_v ** dc
        sub = cf * (u_var + y_var + c) ** (du - dy) * (
            u_var * y_var + u_var * c + y_var * c) ** (dy - dc) * (
            u_var * y_var * c) ** dc
        F = expand(F - sub)
    return result


def ewdeg(F_e):
    if F_e == 0:
        return -1
    P = Poly(F_e, e1_v, e2_v, e3_v)
    m = -1
    for mo, cf in P.terms():
        if cf == 0:
            continue
        i1, i2, i3 = mo
        w = i1 + i2 + 2 * i3
        if w > m:
            m = w
    return m


def main():
    J_MAX = 6
    tables = bt(J_MAX)
    Ss = {jj: S_of_uyc(jj, tables) for jj in range(J_MAX + 1)}
    Ses = {jj: to_elem_uyc(Ss[jj]) for jj in range(J_MAX + 1)}

    e2_ord = u_var * y_var + u_var * c + y_var * c
    e1_ord = u_var + y_var + c
    e3_ord = u_var * y_var * c

    print("=" * 78)
    print("Test 1: What is e-wdeg(S_j) as a function of j?")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        print(f"  j={jj}: e-wdeg(S_j) = {ewdeg(Ses[jj])}   S_j = {Ses[jj]}")

    print("\n" + "=" * 78)
    print("Test 2: Is  S_{j+1} - e_2 * S_j  of lower e-wdeg?")
    print("=" * 78)
    for jj in range(J_MAX):
        diff = expand(Ss[jj + 1] - e2_ord * Ss[jj])
        diff_e = to_elem_uyc(diff)
        w = ewdeg(diff_e)
        print(f"  j={jj}: e-wdeg(S_{jj+1} - e_2*S_j) = {w}   (was {ewdeg(Ses[jj+1])})")
        if w > jj:
            print(f"    diff_e = {diff_e}")

    print("\n" + "=" * 78)
    print("Test 3: Try  S_{j+1} = e_2 * S_j + (e_1 e_2 - 3 e_3) * ???   etc.")
    print("        Or  S_{j+1} - e_2^{j+1} = f(e_1, e_2, e_3) that recurses cleanly")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        # top-part removed = S_j - e_2^j
        diff = expand(Ss[jj] - e2_ord ** jj)
        diff_e = to_elem_uyc(diff)
        w = ewdeg(diff_e)
        print(f"  j={jj}: e-wdeg(S_j - e_2^j) = {w}   (S_j - e_2^j in e-basis)")
        if diff_e != 0 and jj <= 4:
            print(f"    = {diff_e}")

    print("\n" + "=" * 78)
    print("Test 4: e_2 * S_j has what e-wdeg?  (Should be j + 1.)")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        e2Sj = expand(e2_ord * Ss[jj])
        e2Sj_e = to_elem_uyc(e2Sj)
        print(f"  j={jj}: e-wdeg(e_2 * S_j) = {ewdeg(e2Sj_e)}")

    print("\n" + "=" * 78)
    print("Test 5: Homogeneous decomp of S_j by ordinary total degree; e-wdeg per piece.")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        S = Ss[jj]
        P = Poly(S, u_var, y_var, c)
        components = defaultdict(lambda: Integer(0))
        for m, cf in P.terms():
            deg = sum(m)
            components[deg] += cf * u_var**m[0] * y_var**m[1] * c**m[2]
        print(f"  j={jj}: total degree 0..{2*jj}")
        for d in sorted(components.keys()):
            f_e = to_elem_uyc(expand(components[d]))
            w = ewdeg(f_e)
            print(f"    deg={d:2d}: e-wdeg = {w:2d}  {'(=j)' if w == jj else ''}"
                  f"   e-poly = {f_e}")

    print("\n" + "=" * 78)
    print("Test 6: Check what e-poly the j=5 case explicitly is:")
    print("=" * 78)
    print(f"  S_5 (e-basis) = {Ses[5]}")

    print("\n" + "=" * 78)
    print("Test 7: shifted-e_2 recursion?  Define  E_2^* = e_2 + f(e_1, e_3)  such that")
    print("        S_{j+1} - E_2^* S_j has e-wdeg <= j - 1?  Search f.")
    print("=" * 78)
    # Try e_2 + c_1 * e_1 + c_2 (constant) + c_3 e_3 / e_1  ...
    # Only linear correction in low-degree e-vars. Try E = e_2 + c1*e_1 + c0
    # Fit E to make S_{j+1} - E * S_j small e-wdeg
    # This is heuristic: try to fit c1, c0 for j=2 -> want small e-wdeg diff
    # We can attempt: e-wdeg(S_3 - E*S_2) < 3.
    # Solve numerically.
    for j_fit in [1, 2, 3]:
        for c1 in range(-3, 4):
            for c0 in range(-6, 7):
                for c3_e1 in range(-3, 4):
                    E_op = e2_ord + c1 * e1_ord + c0
                    # skip c3_e1 for now
                    diff = expand(Ss[j_fit + 1] - E_op * Ss[j_fit])
                    diff_e = to_elem_uyc(diff)
                    w = ewdeg(diff_e)
                    if w <= j_fit:
                        print(f"  j_fit={j_fit}: (c1, c0) = ({c1}, {c0})  "
                              f"e-wdeg(S_{j_fit+1} - E*S_{j_fit}) = {w}  <= {j_fit}  HIT")


if __name__ == "__main__":
    main()
