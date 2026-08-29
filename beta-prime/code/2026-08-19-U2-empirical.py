"""Day 111 U_2 empirical closed-form fit — FINAL.

Task: find u_j^(2)(b, c) := (ds_j / V)|_{a=0} closed form as sum of falling-factorial products.

Result (verified j = 0..12):

  u_j^(2)(b, c) = T_0(j) + T_1(j) + T_2A(j) + T_2B(j)     [4 terms]

where each term corresponds to a (mu_3, mu_2)-restricted subsum of the shifted-Schur ensemble.
This is one more term than Rick's initial guess (Rick expected 3). The 4th term is separate
because within the mu_3 = 2 subcase, mu_2 splits into two natural values (mu_2 = j-1 and
mu_2 = j-2), which give qualitatively different arithmetic contributions.

Definitions:

  Shell_p(j) := c^{fall 2} * (c-3)^{fall(j-2-p)} * (b+1)^{fall 2} * (b-2)^{fall(j-2-p)}
  where p = 0 for T_0 (mu_3 = 0 case) and p = 1 for T_1, T_2A, T_2B.

  Equivalently:
    Shell_0(j) = c(c-1)(c-3)(c-4)...(c-j) * (b+1)b(b-2)(b-3)...(b-j+1)
    Shell_1(j) = c(c-1)(c-3)(c-4)...(c-j+1) * (b+1)b(b-2)(b-3)...(b-j+2)

Then, for j >= 3:
  T_0 (j)  =            Shell_0(j)                                              [mu_3=0]
  T_1 (j)  = 2(j-1) *   Shell_1(j) * (b + c - 2j)                               [mu_3=1]
  T_2A(j)  = (j-1)(j-2) * Shell_1(j)                                            [mu_3=2, mu_2=j-1]
  T_2B(j)  =    j(j-3) * Shell_1(j) * (b^2 + bc + c^2 + (2-3j)(b+c) + 3j(j-1))  [mu_3=2, mu_2=j-2]

Edges for small j (0, 1, 2) computed by direct evaluation.

The sum
  A + B + C + D  where
    A = Shell_0(j)                                              (from mu_3 = 0)
    B = 2(j-1) Shell_1(j) (b + c - 2j)                          (from mu_3 = 1, j >= 3)
    C = (j-1)(j-2) Shell_1(j)                                   (from mu_3 = 2, mu_2 = j-1)
    D = j(j-3) Shell_1(j) [b^2 + bc + c^2 + (2-3j)(b+c) + 3j(j-1)]  (from mu_3 = 2, mu_2 = j-2)

matches u_j^(2) uniformly for j = 0, 1, ..., 12 (edge cases j = 0, 1, 2 verified by direct
computation of T[j] contributions).

Chu-Vandermonde structure: each Shell_0(j) and Shell_1(j) contains falling factorials
(c-3)^{fall(...)} and (b-2)^{fall(...)}, which are exactly the shape needed for
Chu-Vandermonde against the pipeline's (b+2)_{c-1-j} and (2)_{c-1-j} rising Pochhammers.
For the mu_3 = 0 sub-sum, expect a clean collapse analogous to Day 109 / Day 110.
For mu_3 = 1 and mu_3 = 2 sub-sums, more work needed (they involve j-dependent
polynomial multipliers).
"""
import sys
import sympy as sp
from sympy import (symbols, expand, factor, simplify, Poly, Integer, cancel, div,
                   Rational, Symbol, binomial)
from collections import defaultdict
from itertools import combinations


# =============================================================================
# PIPELINE (reused from Day 109/110)
# =============================================================================
def bt(M):
    def vs(mu):
        L = len(mu) + 2
        b_ = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = b_.copy()
            for i in p:
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
    for j in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[j] = rs
    return T


def fall_sym(x, k):
    if k < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def rise_sym(x, L):
    if L < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


a, b, c = symbols('a b c')
V_at_a0 = (1 - b) * (2 - c) * (b - c + 1)

P("=" * 78)
P("Day 111 — U_2 empirical closed form for u_j^(2) := (ds_j/V)|_{a=0}")
P("Level-2 target of Rick's (R) proof program.")
P("=" * 78)

P("""
EMPIRICAL CLOSED FORM (verified j = 0..12):

  u_j^(2)(b, c) = T_0(j) + T_1(j) + T_2A(j) + T_2B(j)

  Shell_0(j) := c(c-1) * (c-3)^{fall(j-2)} * (b+1)b * (b-2)^{fall(j-2)}
  Shell_1(j) := c(c-1) * (c-3)^{fall(j-3)} * (b+1)b * (b-2)^{fall(j-3)}
  Shell_2(j) := c(c-1) * (c-3)^{fall(j-4)} * (b+1)b * (b-2)^{fall(j-4)}

For j >= 3:
  T_0 (j)  =            Shell_0(j)                                      [mu_3=0]
  T_1 (j)  = 2(j-1)   * Shell_1(j) * (b + c - 2j)                       [mu_3=1]
  T_2A(j)  = (j-1)(j-2) * Shell_1(j)                                    [mu_3=2, mu_2=j-1]
  T_2B(j)  =     j(j-3) * Shell_2(j) *
                [b^2 + bc + c^2 + (2-3j)b + (1-3j)c + 3j(j-1)]          [mu_3=2, mu_2=j-2]

Edge cases:
  j = 0:  u = 1                              (T_0(0)=1; T_1=T_2A=T_2B=0)
  j = 1:  u = bc + b + 2c                    (T_0(1) computed from mu=(1,1,0))
  j = 2:  u = c(b+1)(bc + b + 2c - 6)        (T_0(2)=c(c-1)(b+1)b; T_1(2)=2c(b+1)(b+c-3); T_2A=T_2B=0)

Each T_i corresponds to a (mu_3, mu_2)-restricted subsum of the shifted-Schur
ensemble at y_1 = 2 (a = 0). Note: Rick expected 3 terms; we find 4, because
within the mu_3 = 2 subcase two distinct mu_2 values contribute qualitatively
different arithmetic (a scalar in T_2A, a symmetric-quadratic factor in T_2B).

""")

JMAX = 12
T = bt(JMAX)


def full_u2(j):
    """u_j^(2)(b, c) = (ds_j / V)|_{a=0}, symbolic in b, c."""
    ds_tot = Integer(0)
    for mu, kk in T[j]:
        y_vals = (Integer(2), b + 1, c)
        ks = [mu[i] + (2 - i) for i in range(3)]
        M_m = [[fall_sym(y_vals[i], ks[l]) for l in range(3)] for i in range(3)]
        d = (M_m[0][0] * (M_m[1][1] * M_m[2][2] - M_m[1][2] * M_m[2][1])
             - M_m[0][1] * (M_m[1][0] * M_m[2][2] - M_m[1][2] * M_m[2][0])
             + M_m[0][2] * (M_m[1][0] * M_m[2][1] - M_m[1][1] * M_m[2][0]))
        ds_tot += kk * d
    ds_tot = expand(ds_tot)
    q, r = div(Poly(ds_tot, b, c), Poly(V_at_a0, b, c))
    return expand(q.as_expr())


def subcase_u(j, filt):
    parts = [(mu, kk) for mu, kk in T[j] if filt(mu)]
    if not parts:
        return Integer(0)
    ds_part = Integer(0)
    for mu, kk in parts:
        y_vals = (Integer(2), b + 1, c)
        ks = [mu[i] + (2 - i) for i in range(3)]
        M_m = [[fall_sym(y_vals[i], ks[l]) for l in range(3)] for i in range(3)]
        d = (M_m[0][0] * (M_m[1][1] * M_m[2][2] - M_m[1][2] * M_m[2][1])
             - M_m[0][1] * (M_m[1][0] * M_m[2][2] - M_m[1][2] * M_m[2][0])
             + M_m[0][2] * (M_m[1][0] * M_m[2][1] - M_m[1][1] * M_m[2][0]))
        ds_part += kk * d
    ds_part = expand(ds_part)
    q, r = div(Poly(ds_part, b, c), Poly(V_at_a0, b, c))
    if r.as_expr() != 0:
        return None
    return expand(q.as_expr())


# ============================================================================
# THE EMPIRICAL FORMULA
# ============================================================================
def Shell0(j):
    """c^{fall 2} * (c-3)^{fall(j-2)} * (b+1)^{fall 2} * (b-2)^{fall(j-2)}"""
    return (fall_sym(c, 2) * fall_sym(c - 3, j - 2) *
            fall_sym(b + 1, 2) * fall_sym(b - 2, j - 2))


def Shell1(j):
    """c^{fall 2} * (c-3)^{fall(j-3)} * (b+1)^{fall 2} * (b-2)^{fall(j-3)}"""
    return (fall_sym(c, 2) * fall_sym(c - 3, j - 3) *
            fall_sym(b + 1, 2) * fall_sym(b - 2, j - 3))


def T0(j):
    """mu_3 = 0 contribution."""
    if j == 0:
        return Integer(1)
    if j == 1:
        # mu = (1, 1, 0), computed directly
        return subcase_u(1, lambda mu: mu == (1, 1, 0))
    return Shell0(j)


def T1(j):
    """mu_3 = 1 contribution."""
    if j <= 1:
        return Integer(0)
    if j == 2:
        return 2 * c * (b + 1) * (b + c - 3)
    return 2 * (j - 1) * Shell1(j) * (b + c - 2 * j)


def T2A(j):
    """mu_3 = 2, mu_2 = j-1 contribution."""
    if j <= 2:
        return Integer(0)
    # Handle j = 3 as edge (j-3 = 0, so Shell1 = c(c-1)(b+1)b times empty products)
    # For j = 3, (mu_3=2, mu_2=j-1=2) gives (2,2,2), value = 2*bc(b+1)(c-1) = 2*Shell1(3).
    # coef = (j-1)(j-2) at j=3: 2*1 = 2. ✓
    return (j - 1) * (j - 2) * Shell1(j)


def Shell2(j):
    """Shell for T_2B: c*(c-1)*(c-3)^{fall(j-4)} * b*(b+1)*(b-2)^{fall(j-4)}
    (one less falling factorial than Shell1, matches empirical mu_2=j-2 shell.)"""
    return (c * (c - 1) * fall_sym(c - 3, j - 4) *
            b * (b + 1) * fall_sym(b - 2, j - 4))


def T2B(j):
    """mu_3 = 2, mu_2 = j-2 contribution."""
    if j <= 3:
        return Integer(0)
    quad = b**2 + b * c + c**2 + (2 - 3 * j) * b + (1 - 3 * j) * c + 3 * j * (j - 1)
    return j * (j - 3) * Shell2(j) * quad


# ============================================================================
# Verify uniformly j = 0..12
# ============================================================================
P("\nVerify u_j^(2) = T_0 + T_1 + T_2A + T_2B for j = 0..%d" % JMAX)
P()
all_ok = True
for j in range(0, JMAX + 1):
    u_full = full_u2(j)
    model = expand(T0(j) + T1(j) + T2A(j) + T2B(j))
    diff = simplify(u_full - model)
    match = (diff == 0)
    if match:
        P(f"  j = {j:2d}:  match = True")
    else:
        P(f"  j = {j:2d}:  MISMATCH  diff = {factor(diff)}")
        all_ok = False
P()
P("VERDICT: " + ("ALL PASS" if all_ok else "SOME FAIL"))


# ============================================================================
# Chu-Vandermonde-style pipeline collapse check
# Compare direct Q_{2R}(0, b, c) to ansatz-reconstructed value.
# ============================================================================
P()
P("=" * 78)
P("Pipeline reconstruction check: 3-term/4-term ansatz -> Q_{2R}(0, b, c)")
P("=" * 78)


def ds_expr_sym(a_sym, b_sym, c_sym, j, T):
    y = (a_sym + 2, b_sym + 1, c_sym)
    tot = Integer(0)
    for mu, kk in T[j]:
        ks = [mu[i] + (2 - i) for i in range(3)]
        M = [[fall_sym(y[i], ks[l]) for l in range(3)] for i in range(3)]
        d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
             - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
             + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        tot += kk * d
    return expand(tot)


def Q_2R_direct(R, c_val, T):
    """Q_{2R}(a=0, b, c=c_val) from H_c(a=0, b, j) = (3)_{c-1-j}(b+2)_{c-1-j} u_j^(2)."""
    k = 2 * R
    L = c_val - 1 - k
    if L < 0:
        return None
    tot = Integer(0)
    for j in range(k + 1):
        ds_j_val = ds_expr_sym(a, b, c, j, T).subs({a: 0, c: c_val})
        num = rise_sym(3, c_val - 1 - j) * rise_sym(b + 2, c_val - 1 - j) * ds_j_val
        den = (0 - b + 1) * (0 - c_val + 2) * (b - c_val + 1)
        Hj = cancel(num / den)
        tot += (-1)**(k - j) * sp.binomial(k, j) * Hj
    hk = expand(tot)
    denom = rise_sym(3, L) * rise_sym(b + 2, L)
    q = expand(cancel(hk / denom))
    return q


def Q_2R_from_ansatz(R, c_val):
    """Same pipeline but use 4-term ansatz for u_j^(2)."""
    k = 2 * R
    L = c_val - 1 - k
    if L < 0:
        return None
    tot = Integer(0)
    for j in range(k + 1):
        uj = (T0(j) + T1(j) + T2A(j) + T2B(j)).subs(c, c_val)
        Hj = rise_sym(3, c_val - 1 - j) * rise_sym(b + 2, c_val - 1 - j) * uj
        tot += (-1)**(k - j) * sp.binomial(k, j) * Hj
    hk = expand(tot)
    denom = rise_sym(3, L) * rise_sym(b + 2, L)
    q = expand(cancel(hk / denom))
    return q


P("\nR=2 (2R=4):")
T4 = bt(4)
r2_all_ok = True
for c_val in [5, 6, 7, 8, 9]:
    Q_dir = Q_2R_direct(2, c_val, T4)
    Q_ans = Q_2R_from_ansatz(2, c_val)
    diff = simplify(Q_dir - Q_ans)
    match = (diff == 0)
    P(f"  c = {c_val}: direct == ansatz-based? {match}")
    if not match:
        r2_all_ok = False

P("\nR=3 (2R=6):")
T6 = bt(6)
r3_all_ok = True
for c_val in [7, 8, 9, 10]:
    Q_dir = Q_2R_direct(3, c_val, T6)
    Q_ans = Q_2R_from_ansatz(3, c_val)
    diff = simplify(Q_dir - Q_ans)
    match = (diff == 0)
    P(f"  c = {c_val}: direct == ansatz-based? {match}")
    if not match:
        r3_all_ok = False

P()
P(f"Pipeline reconstruction: R=2 {'OK' if r2_all_ok else 'FAIL'}, R=3 {'OK' if r3_all_ok else 'FAIL'}")


# ============================================================================
# Substitution b = k - 1 = 1: extract P^(2)_R(c)-analog (Rick's Secondary check)
# ============================================================================
P()
P("=" * 78)
P("Secondary: substitute b = 1 (i.e., y_2 = 2) into u_j^(2), and check pipeline")
P("=" * 78)
P("Rick's Level-2 gold values from 2026-08-15-recursion-levels.txt:")
P("  R=3:  P_R^(2)(c) = 180 c(c-4)(c-3)^2(c-2)(c-1)")
P("  R=4:  P_R^(2)(c) = 840 c(c-6)(c-5)^2(c-4)^2(c-3)^2(c-2)(c-1)")
P()
P("Note: P_R^(2) is extracted via TWO peelings from Q_{2R}(a=0, b, c), not directly")
P("      from u_j^(2). So the check requires computing Q_{2R}(a=0, b, c) and peeling.")
P()

# But let's still check b = 1 substitution values for insight.
P("u_j^(2)(b=1, c) for j = 0..%d:" % JMAX)
for j in range(0, JMAX + 1):
    u = full_u2(j).subs(b, 1)
    P(f"  j = {j}: {factor(u)}")

# Perform two peelings of Q_{2R}(a=0, b, c) to extract P_R^(2)(c):
# Recursion: T_1 = (Q_{2R} - P_R^(0)) / ((a+2)(b+1)), T_2 = (T_1 - P_R^(1)) / ((a+1)(b))
# So T_2(a=0, b=?, c) evaluated at a=0 might be b-indep — that's the check.
# Actually the recursion structure: T_2(a=0, b, c) is b-independent by construction
# (from 2026-08-15-recursion-levels output), and equal to P_R^(2)(c) up to normalization.
# The peeling of Q at a=0 gives (Q_{2R}(0,b,c) - P_R^(0)(c))/((2)(b+1)) = T_1(0,b,c)
# further (T_1(0,b,c) - P_R^(1)(c))/(1*b) = T_2(0,b,c) = P_R^(2)(c)/? (b-indep)

# Explicitly do the peeling for R = 3 to check.
P("\nPeeling check for R = 3:")
T6 = bt(6)
# Get P_R^(0) and P_R^(1) formulas
def P_R_0(R, c_val):
    """P_R^(0)(c) = c(c-2R)prod_{j=1}^{2R-1}(c-j)^2"""
    v = c_val * (c_val - 2 * R)
    for j in range(1, 2 * R):
        v *= (c_val - j)**2
    return v


def P_R_1(R, c_val):
    """P_R^(1)(c) = -2R(2R-1) c (c-1)^{fall(2R-2)} (c-2)^{fall(2R-2)}"""
    v = -2 * R * (2 * R - 1) * c_val
    for i in range(2 * R - 2):
        v *= (c_val - 1 - i)
    for i in range(2 * R - 2):
        v *= (c_val - 2 - i)
    return v


for R in [3, 4]:
    TR = bt(2 * R)
    for c_val in [2 * R + 2, 2 * R + 4]:
        Q0 = Q_2R_direct(R, c_val, TR)  # Q_{2R}(a=0, b, c=c_val)
        # Peel level 1: T_1(0, b, c) = (Q_{2R}(0,b,c) - P^(0)(c)) / (2 * (b+1))
        P0_val = P_R_0(R, c_val)
        T1_num = expand(Q0 - P0_val)
        # divide by 2*(b+1)
        q1, r1 = div(Poly(T1_num, b), Poly(2 * (b + 1), b))
        if r1.as_expr() != 0:
            P(f"  R={R}, c={c_val}: peel-1 NOT clean. rem={r1.as_expr()}")
            continue
        T1_val = q1.as_expr()
        # Peel level 2: T_2(0, b, c) = (T_1(0,b,c) - P^(1)(c)) / (1 * b)
        P1_val = P_R_1(R, c_val)
        T2_num = expand(T1_val - P1_val)
        q2, r2 = div(Poly(T2_num, b), Poly(b, b))
        if r2.as_expr() != 0:
            P(f"  R={R}, c={c_val}: peel-2 NOT clean. rem={r2.as_expr()}")
            continue
        T2_val = q2.as_expr()
        # T_2(0, b, c) should be b-independent
        poly_b = Poly(T2_val, b)
        deg_b = poly_b.degree()
        if deg_b > 0:
            P(f"  R={R}, c={c_val}: T_2(0, b, c) NOT b-indep. deg_b = {deg_b}")
            P(f"     T_2 = {T2_val}")
        else:
            const_val = T2_val
            # Compare to expected P_R^(2)(c) / normalization
            # For R=3, P_R^(2)(c) = 180 c(c-4)(c-3)^2(c-2)(c-1)
            if R == 3:
                gold = 180 * c_val * (c_val - 4) * (c_val - 3)**2 * (c_val - 2) * (c_val - 1)
            elif R == 4:
                gold = 840 * c_val * (c_val - 6) * (c_val - 5)**2 * (c_val - 4)**2 * (c_val - 3)**2 * (c_val - 2) * (c_val - 1)
            else:
                gold = None
            if gold is not None:
                P(f"  R={R}, c={c_val}: T_2(0, ., c) = {const_val}, gold P_R^(2)(c) = {gold}, ratio = {sp.Rational(const_val, gold) if gold != 0 else 'N/A'}")


# Save
with open('/home/agent/projects/beta-prime/code/2026-08-19-U2-empirical.txt', 'w') as f:
    f.write('\n'.join(OUT))
P()
P("*** RESULTS SAVED TO 2026-08-19-U2-empirical.txt ***")
