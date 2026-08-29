"""Day 117 — Route V probe.

Goal: check that A_j := ds_j / (y - c), expressed in (u, sigma, pi) with
      sigma = y + c, pi = y*c, has joint (u, pi)-degree <= j + 2.

If yes, then S_j = A_j / (u^2 - u*sigma + pi) has joint (u, pi)-degree <= j
because the top-(u,pi)-degree part of (u^2 - u*sigma + pi) is u^2 (deg 2)
which is a non-zero-divisor in Q[u, sigma, pi].

We compute A_j for j <= 6 or so and print the joint (u, pi)-degree of each
monomial vs the bound j + 2.
"""
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer

u, y, c = symbols('u y c')
sig, pi = symbols('sigma pi')


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


def bt_tables(M):
    """Rick's bt: iteratively add a vertical-2-strip M times, restricted to
    partitions of length <= 3. Returns {j: [(mu_padded_len3, kappa_mu)]}."""
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
        for mu, cn in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cn))
        T[jj] = rs
    return T


def ds_uyc(j, T):
    xs = (u, y, c)
    total = Integer(0)
    for mu, kap in T[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def divide(num, denom, vars_):
    q, r = sp.div(Poly(num, *vars_), Poly(denom, *vars_))
    if r.as_expr() != 0:
        raise ValueError("no clean division")
    return q.as_expr()


def substitute_sigma_pi(expr):
    """Substitute y + c = sigma, y*c = pi. expr must be symmetric in y, c.
    We do it by expressing as a polynomial in y, c and then converting
    each symmetric part.
    Trick: for a symmetric polynomial P(y, c), P = sum_{a >= b} c_{a,b} m_{a,b}
    where m_{a,b} = y^a c^b + y^b c^a (or y^a c^a if a=b).
    m_{a,a} = (y c)^a = pi^a.
    m_{a, b} for a > b: use the recursion m_{a,b} = sigma * m_{a-1, b} - pi * m_{a-1, b-1}
      (from y^a c^b + y^b c^a = (y+c)(y^{a-1} c^b + y^b c^{a-1}) - y c (y^{a-2} c^b + y^b c^{a-2})
       ... hmm let me use a simpler route)
    Simpler: express P(y, c) as a poly in y with coefficients in c, then use
    y^2 = sigma * y - pi (since y and c are roots of t^2 - sigma t + pi = 0).
    Reduce all y^k to a + b*y, then P = A(c) + B(c) * y. Symmetry then implies
    A(c) + B(c) c = A(y) + B(y) y... this is getting messy.

    Alternative: use resultants / direct sympy. Let me just expand P as poly
    in y, c, then group by (a+b, a*b)-like invariants.
    """
    # Approach: reduce modulo y^2 - sigma*y + pi.
    # Represent as A + B*y where A, B are polys in c and sigma, pi.
    # Do this by iteratively replacing y^k by (sigma * y^{k-1} - pi * y^{k-2}).
    p = Poly(expand(expr), y)
    coeffs = p.all_coeffs()[::-1]  # index k = coefficient of y^k
    # Reduce: represent as [A, B] with sum A + B*y where A, B are in c, sigma, pi.
    A = Integer(0)
    B = Integer(0)
    # y^0 = 1, y^1 = y
    # y^k = sigma * y^{k-1} - pi * y^{k-2}
    # Precompute reduction table
    reductions = [(Integer(1), Integer(0)), (Integer(0), Integer(1))]  # [A_k, B_k] for y^k
    for k in range(2, len(coeffs)):
        prev_A, prev_B = reductions[k - 1]
        pprev_A, pprev_B = reductions[k - 2]
        A_k = sig * prev_A - pi * pprev_A
        B_k = sig * prev_B - pi * pprev_B
        reductions.append((expand(A_k), expand(B_k)))
    for k, coeff in enumerate(coeffs):
        A_k, B_k = reductions[k]
        A += coeff * A_k
        B += coeff * B_k
    A = expand(A)
    B = expand(B)
    # Symmetry check: A + B*y should equal expr AND swap y<->c should preserve
    # Also, since expr is symmetric in y, c, we should have that after substitution
    # of y -> c... but actually, we've eliminated y^2 by using y^2 = sigma*y - pi
    # which holds for BOTH y and c. So A + B*y and A + B*c both make sense.
    # For symmetry: A + B*y = A + B*c means B*(y - c) = 0, so B must be 0 in Q(sigma, pi, c).
    # Wait that's wrong because y and c are symmetric roots — the poly A + B*y evaluated at
    # y is one root, and if we swap, A + B*c is the other root. Symmetry means the swap gives
    # the same expression AFTER we treat y, c symmetrically... hmm.
    #
    # Actually: after reducing modulo y^2 - sigma*y + pi, expr = A(c, sigma, pi) + B(c, sigma, pi) * y.
    # For expr to be symmetric in y, c (as a polynomial in y, c), we need... well the reduction
    # is not respecting c. Let me redo this — I should reduce w.r.t. BOTH y^2 = sigma y - pi
    # and c^2 = sigma c - pi.
    #
    # Since expr is symmetric in y, c, after reducing y^2 -> sigma y - pi, it's still
    # a poly in y, c. Now also reduce c^2 -> sigma c - pi. Result: linear in y AND linear in c.
    # I.e., expr = P + Q y + R c + S y c with P, Q, R, S in Q[sigma, pi].
    # Symmetry: Q y + R c = Q c + R y => (Q - R)(y - c) = 0 => Q = R.
    # And S y c = S pi. So expr = P + S pi + Q (y + c) = P + S pi + Q sigma.
    # This becomes a poly in sigma, pi.
    #
    # Let me redo A above but now reduce B (a poly in c) mod c^2 = sigma c - pi.
    A_poly = Poly(A, c)
    A_coeffs = A_poly.all_coeffs()[::-1]
    B_poly = Poly(B, c)
    B_coeffs = B_poly.all_coeffs()[::-1]
    # y^k for c
    c_reductions = [(Integer(1), Integer(0)), (Integer(0), Integer(1))]
    max_deg = max(len(A_coeffs), len(B_coeffs), 2)
    for k in range(2, max_deg):
        prev_A, prev_B = c_reductions[k - 1]
        pprev_A, pprev_B = c_reductions[k - 2]
        A_k = sig * prev_A - pi * pprev_A
        B_k = sig * prev_B - pi * pprev_B
        c_reductions.append((expand(A_k), expand(B_k)))
    A_new = Integer(0)
    B_new = Integer(0)
    for k, coeff in enumerate(A_coeffs):
        Ak, Bk = c_reductions[k]
        A_new += coeff * Ak
        B_new += coeff * Bk
    C_new = Integer(0)
    D_new = Integer(0)
    for k, coeff in enumerate(B_coeffs):
        Ak, Bk = c_reductions[k]
        C_new += coeff * Ak
        D_new += coeff * Bk
    # expr = A_new + B_new * c + C_new * y + D_new * y * c
    A_new = expand(A_new)
    B_new = expand(B_new)
    C_new = expand(C_new)
    D_new = expand(D_new)
    # Check symmetry
    if expand(B_new - C_new) != 0:
        raise ValueError(f"Not symmetric: B_new = {B_new}, C_new = {C_new}")
    # expr = A_new + D_new * pi + B_new * (y + c) = A_new + D_new * pi + B_new * sigma
    result = A_new + D_new * pi + B_new * sig
    return expand(result)


def joint_u_pi_deg(expr):
    """Given expression in u, sig, pi: return max deg_u + deg_pi over monomials."""
    p = Poly(expand(expr), u, sig, pi)
    max_d = 0
    for mono, _ in p.terms():
        d_u, d_sig, d_pi = mono
        max_d = max(max_d, d_u + d_pi)
    return max_d


if __name__ == "__main__":
    JMAX = 5
    T = bt_tables(JMAX)
    print(f"Route V probe: computing A_j = ds_j / (y - c) for j <= {JMAX}\n")
    print(f"{'j':>3} {'bound j+2':>10} {'actual (u,pi)-deg A_j':>25} {'(u,pi)-deg S_j':>18}")
    print('-' * 60)
    for j in range(JMAX + 1):
        dsj = ds_uyc(j, T)
        # Divide by (y - c)
        Aj_yc = divide(dsj, y - c, [u, y, c])
        # Substitute sigma, pi
        Aj = substitute_sigma_pi(Aj_yc)
        Aj_deg = joint_u_pi_deg(Aj)
        # Also compute S_j and its (u, pi)-deg
        V_full = (u - y) * (u - c) * (y - c)
        S_uyc = divide(dsj, expand(V_full), [u, y, c])
        S_sigpi = substitute_sigma_pi(S_uyc)
        S_deg = joint_u_pi_deg(S_sigpi)
        print(f"{j:>3} {j + 2:>10} {Aj_deg:>25} {S_deg:>18}")
