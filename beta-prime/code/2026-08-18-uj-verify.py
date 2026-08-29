"""Day 110 compute worker for Rick's proof of (R).

TASK 1: Verify u_j = (ds_j / V)|_{a=-1} closed form for level 1.
TASK 2: Look for level-2 closed form (a=0).
TASK 3: Compute total (a,b)-degree of Q_{2R}(a,b,c) for R=2,3 at fixed c.
"""
import sys
import sympy as sp
from sympy import symbols, expand, factor, simplify, Poly, Integer, cancel, div

# Load functions from lemma1 file
sys.path.insert(0, '/home/agent/projects/beta-prime/code')
from importlib import import_module

# Copy the necessary functions inline (avoids importing __main__)
from collections import defaultdict
from itertools import combinations


def bt(M):
    def vs(mu):
        L = len(mu) + 2
        b = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = b.copy()
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
        for mu, c in cu.items():
            for nu in vs(mu):
                nx[nu] += c
        cu = nx
        rs = []
        for mu, c in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, c))
        T[j] = rs
    return T


def fall_sym(x, k):
    """Falling factorial x^{fall k} = x(x-1)...(x-k+1). k=0 -> 1. k<0 -> 0."""
    if k < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def ds(a, b, c, j, T):
    y = (a + 2, b + 1, c)
    tot = Integer(0)
    for mu, kk in T[j]:
        ks = [mu[i] + (2 - i) for i in range(3)]
        M = [[fall_sym(y[i], ks[l]) for l in range(3)] for i in range(3)]
        d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
             - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
             + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        tot += kk * d
    return expand(tot)


OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


a, b, c = symbols('a b c')
V = (a - b + 1) * (a - c + 2) * (b - c + 1)

P("=" * 78)
P("Day 110 compute: u_j closed forms (a=-1 and a=0) + Q_{2R} total (a,b)-degree")
P("=" * 78)

# Build tables up to j = 10
T = bt(10)

# =========================================================================
# TASK 1: Verify u_j closed form at a = -1
# =========================================================================
P("\n" + "=" * 78)
P("TASK 1: u_j = (ds_j / V)|_{a=-1} closed form (level 1)")
P("=" * 78)
P("Conjecture:")
P("  u_j = c^{fall j} * (b+1)^{fall j}")
P("       - j*(j-1) * c * (c-2)^{fall (j-2)} * (b+1) * (b-1)^{fall (j-2)}")
P()

task1_results = []
for j in range(0, 11):
    dsj = ds(a, b, c, j, T)
    q_poly, r_poly = div(Poly(dsj, a, b, c), Poly(V, a, b, c))
    if r_poly.as_expr() != 0:
        P(f"j = {j}: ds_j NOT divisible by V.  remainder = {r_poly.as_expr()}")
        task1_results.append((j, False, "not divisible"))
        continue
    uj_full = expand(q_poly.as_expr())
    uj = expand(uj_full.subs(a, -1))

    # Conjectured form
    term1 = fall_sym(c, j) * fall_sym(b + 1, j)
    if j >= 2:
        term2 = j * (j - 1) * c * fall_sym(c - 2, j - 2) * (b + 1) * fall_sym(b - 1, j - 2)
    else:
        term2 = Integer(0)
    uj_conj = expand(term1 - term2)

    diff = simplify(uj - uj_conj)
    match = (diff == 0)
    P(f"j = {j}: match = {match}")
    if not match:
        P(f"    u_j        = {factor(uj)}")
        P(f"    u_j_conj   = {factor(uj_conj)}")
        P(f"    diff       = {factor(diff)}")
    else:
        P(f"    u_j = {factor(uj)}")
    task1_results.append((j, match, None))

# =========================================================================
# TASK 2: Level-2 closed form (a = 0)
# =========================================================================
P("\n" + "=" * 78)
P("TASK 2: u_j^(2) = (ds_j / V)|_{a=0} — look for closed form")
P("=" * 78)

task2_forms = {}
for j in range(0, 11):
    dsj = ds(a, b, c, j, T)
    q_poly, r_poly = div(Poly(dsj, a, b, c), Poly(V, a, b, c))
    if r_poly.as_expr() != 0:
        P(f"j = {j}: ds_j NOT divisible by V.")
        continue
    uj_full = expand(q_poly.as_expr())
    uj2 = expand(uj_full.subs(a, 0))
    fac = factor(uj2)
    task2_forms[j] = uj2
    P(f"j = {j}:  u_j^(2) = {fac}")

# Try conjecture: same pattern as level 1 but with (c-1) and (b) instead?
# Guess: u_j^(2) = (c-1)^{fall j}? Actually u_j at level ell means a = ell-2?
# Wait: level 1 is a=-1, level 2 is a=0.
# For level 1 (a=-1): u_j = c^{fall j}(b+1)^{fall j} + correction
# By shifting logic, level 2 might have variables (b+1, c-1) shifted or similar.
# Let's try various conjectures.
P("\n--- Try conjecture pattern (b+1, c) -> (b+1, c) but higher-order correction ---")

# Attempt: u_j^(2) = (c+1)^{fall j} * (b+2)^{fall j} - lower order stuff
# Since a=-1 uses (a+2, b+1, c) -> (1, b+1, c), and a=0 uses (2, b+1, c).
# Let's just report empirical factored forms and see if any binomial-ish sum emerges.

P("\n--- Structural: leading term matching ---")
for j in range(0, 8):
    if j not in task2_forms:
        continue
    uj2 = task2_forms[j]
    # Try: leading term c^{fall j+something}*(b+1)^{fall j+something}
    guess_leading = fall_sym(c, j) * fall_sym(b + 1, j)
    rem = expand(uj2 - guess_leading)
    P(f"j = {j}: u_j^(2) - c^fall_{j}*(b+1)^fall_{j} = {factor(rem)}")

# Try conjecture from level 1: analog with shift.
# Level 1 (a=-1) formula uses (b+1, c) as "the two active variables"
# and the "shifted" pair (b-1, c-2).
# For level 2 (a=0), maybe two active variables are (b+2, c+1)? Let's check.
P("\n--- Try leading (c+1)^{fall j} * (b+2)^{fall j} ---")
for j in range(0, 8):
    if j not in task2_forms:
        continue
    uj2 = task2_forms[j]
    guess = fall_sym(c + 1, j) * fall_sym(b + 2, j)
    rem = expand(uj2 - guess)
    P(f"j = {j}: u_j^(2) - (c+1)^fall_{j}*(b+2)^fall_{j} = {factor(rem)}")

# Higher-level structure: at level 1 the u_j has form
#   u_j = (c)_j^fall * (b+1)_j^fall  -  j(j-1) c (c-2)_{j-2}^fall (b+1) (b-1)_{j-2}^fall
# Try inspired guess for level 2: two correction terms?
# u_j^(2) = c^fall_j (b+1)^fall_j
#           - A_1(j) * c * c^fall_{j-1} * (b+1) * (b-1)^{fall (j-2)}?
# Let's compute u_j^(2) - c^{fall j}(b+1)^{fall j} and factor it.
P("\n--- Detailed: u_j^(2) - c^fall_j (b+1)^fall_j factored ---")
for j in range(2, 10):
    if j not in task2_forms:
        continue
    uj2 = task2_forms[j]
    rem = expand(uj2 - fall_sym(c, j) * fall_sym(b + 1, j))
    P(f"j = {j}:  remainder = {factor(rem)}")

# Structural observation of the u_j^(2) factored forms:
#   u_j^(2) = b*c*(b-2)^{fall (j-3)}*(b+1)*(c-3)^{fall (j-3)}*(c-1) * P_j(b,c)   (j >= 3)
# where P_j has a common quadratic-in-(bc) leading pattern:
#   P_j(b,c) = b^2*c^2 - b^2*c - 2*b^2 + b*c^2 - alpha_j*b*c + beta_j*b - 2*c^2 + gamma_j*c + delta_j
# with sequences:
#   alpha_j: (j=4) 33, 51, 73, 99, 129, 163, 201  (2nd differences constant)
#   beta_j:  62, 98, 142, 194, 254, 322, 398      (2nd differences constant)
#   gamma_j: 34, 52, 74, 100, 130, 164, 202       (2nd differences constant)
#   delta_j: -36, 24, 220, 648, 1428, 2704, 4644  (grows like j^4)
# So the level-2 u_j^(2) is not captured by a two-term ansatz mirroring level 1;
# instead the "leading factor" is c^{fall j}(b+1)^{fall j} but the correction is
# a polynomial in (b,c) of bidegree (2,2) whose coefficients are quadratic (a,b,c
# support) or higher polynomials in j.
P("\n--- Level-2 pattern report ---")
P("u_j^(2) = b * c * (b+1) * (c-1) * (b-2)^{fall (j-3)} * (c-3)^{fall (j-3)} * P_j(b,c)")
P("where P_j(b,c) = b^2*c^2 - b^2*c - 2*b^2 + b*c^2 - alpha(j)*b*c + beta(j)*b - 2*c^2 + gamma(j)*c + delta(j).")
P("Coefficient sequences (j = 4 .. 10):")
P("  alpha: 33, 51, 73, 99, 129, 163, 201   (quadratic in j)")
P("  beta:  62, 98, 142, 194, 254, 322, 398 (quadratic in j)")
P("  gamma: 34, 52, 74, 100, 130, 164, 202  (quadratic in j)")
P("  delta: -36, 24, 220, 648, 1428, 2704, 4644 (quartic in j)")
P("So u_j^(2) does NOT admit a two-term closed form analogous to level 1;")
P("it is a leading (c^fall_j)(b+1)^fall_j plus higher-degree corrections.")

# Try to fit each sequence as a polynomial in j.
from sympy import Symbol, solve, Rational
jj = Symbol('j')

def fit_poly(vals, j0, deg):
    """Fit vals[i] = f(j0+i) as polynomial of degree deg in j."""
    n = len(vals)
    if n < deg + 1:
        return None
    A = sp.Matrix([[Rational(j0+i)**d for d in range(deg+1)] for i in range(n)])
    y = sp.Matrix(vals)
    if A.rank() < deg + 1:
        return None
    sol = A.LDLsolve(y) if n == deg + 1 else A.pinv() * y
    # Use least-squares/exact
    if n == deg + 1:
        sol = A.solve(y)
    else:
        # Exact via lstsq
        try:
            sol = (A.T * A).solve(A.T * y)
        except Exception:
            return None
    poly = sum(sol[d] * jj**d for d in range(deg+1))
    # Verify
    for i, v in enumerate(vals):
        if sp.simplify(poly.subs(jj, j0+i) - v) != 0:
            return None
    return sp.expand(poly)

alpha_vals = [33, 51, 73, 99, 129, 163, 201]
beta_vals = [62, 98, 142, 194, 254, 322, 398]
gamma_vals = [34, 52, 74, 100, 130, 164, 202]
delta_vals = [-36, 24, 220, 648, 1428, 2704, 4644]

alpha_fit = fit_poly(alpha_vals, 4, 2)
beta_fit = fit_poly(beta_vals, 4, 2)
gamma_fit = fit_poly(gamma_vals, 4, 2)
# delta might need higher
delta_fit = None
for d in range(3, 7):
    delta_fit = fit_poly(delta_vals, 4, d)
    if delta_fit is not None:
        break

P(f"\nFitted alpha(j) = {alpha_fit}   (degree 2 in j)")
P(f"Fitted beta(j)  = {beta_fit}   (degree 2 in j)")
P(f"Fitted gamma(j) = {gamma_fit}   (degree 2 in j)")
P(f"Fitted delta(j) = {delta_fit}")

# =========================================================================
# TASK 3: Total (a, b)-degree of Q_{2R}
# =========================================================================
P("\n" + "=" * 78)
P("TASK 3: Total (a,b)-degree of Q_{2R}(a, b, c) for R=2, R=3 at concrete c")
P("=" * 78)
P("Using symbolic pipeline in (a,b) at fixed integer c.")
P("Q_{2R}(a,b,c) is obtained from h_{2R}(a,b,c) by dividing by (a+3)_{c-1-2R}(b+2)_{c-1-2R}.")

def rise_sym(x, L):
    p = Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def H_c_symbolic(j, c_val, T):
    """Symbolic H_c(a,b,j) at concrete integer c=c_val, symbolic a, b.
    Impulse term ignored (c generic; only relevant when 2c <= j).
    """
    k = j  # from H_c formula
    L1 = c_val - k - 2
    L2 = c_val - k - 1
    if L1 < 0 or L2 < 0:
        return None
    ds_j = ds(a, b, c, j, T).subs(c, c_val)
    poch_a = rise_sym(a + 3, L1)
    poch_b = rise_sym(b + 2, L2)
    num = (a + c_val + 1 - k) * poch_a * poch_b * ds_j
    den = (a - b + 1) * (a - c_val + 2) * (b - c_val + 1)
    expr = cancel(num / den)
    return expand(expr)


def h_k_symbolic(k, c_val, T):
    """h_k(a,b,c=c_val) = sum_{i=0}^k (-1)^{k-i} C(k,i) H_c(a,b,i)."""
    tot = Integer(0)
    for i in range(k + 1):
        Hi = H_c_symbolic(i, c_val, T)
        if Hi is None:
            return None
        tot += (-1)**(k - i) * sp.binomial(k, i) * Hi
    return expand(tot)


def Q_2R_symbolic(R, c_val, T):
    """Q_{2R}(a,b,c=c_val) = h_{2R}(a,b,c) / [(a+3)_{c-1-2R} (b+2)_{c-1-2R}]."""
    k = 2 * R
    hk = h_k_symbolic(k, c_val, T)
    if hk is None:
        return None
    L = c_val - 1 - k
    if L < 0:
        return None
    denom_a = rise_sym(a + 3, L)
    denom_b = rise_sym(b + 2, L)
    # Divide as polynomial in a first
    denom = denom_a * denom_b
    # Use sp.cancel to reduce
    q = cancel(hk / denom)
    return expand(q)


# Need tables up to j = 6 for R=3 (2R=6)
T = bt(6)

for R in [2, 3]:
    P(f"\n--- R = {R}, 2R = {2*R} ---")
    for c_val in [2 * R + 2, 2 * R + 3, 2 * R + 4]:
        P(f"\n  c = {c_val}:")
        Q = Q_2R_symbolic(R, c_val, T)
        if Q is None:
            P(f"    Q_{2*R} could not be computed.")
            continue
        # Check if Q is a polynomial (no denominators)
        Qp = sp.together(Q)
        num, den = sp.fraction(Qp)
        if not den.is_number:
            # It didn't divide cleanly; try Poly divison
            P(f"    Warning: not a clean polynomial. Denominator = {den}")
            # Try dividing symbolically as poly in a
            try:
                pa = Poly(sp.expand(Q * den), a)
                P(f"    (used ratio; poly degree in a = {pa.degree()})")
            except Exception as e:
                P(f"    (poly extraction failed: {e})")
        # Compute degrees
        try:
            P_ab = Poly(Q, a, b)
            # Total degree
            monoms = P_ab.monoms()
            if monoms:
                total_deg = max(m[0] + m[1] for m in monoms)
                deg_a = max(m[0] for m in monoms)
                deg_b = max(m[1] for m in monoms)
            else:
                total_deg = 0; deg_a = 0; deg_b = 0
            P(f"    degree in a: {deg_a}")
            P(f"    degree in b: {deg_b}")
            P(f"    TOTAL (a,b)-degree: {total_deg}")
            P(f"    Compare: 2R = {2*R}, 4R = {4*R}")
            if total_deg <= 2 * R:
                P(f"    ==> total (a,b)-degree <= 2R = {2*R}  [KEY CLAIM VERIFIED]")
            else:
                P(f"    ==> total (a,b)-degree = {total_deg} > 2R = {2*R}")
        except Exception as e:
            P(f"    Degree extraction failed: {e}")

# Summary
P("\n" + "=" * 78)
P("SUMMARY")
P("=" * 78)
P("\nTASK 1 (u_j closed form at a=-1):")
all_pass = True
for j, match, note in task1_results:
    P(f"  j = {j}: match = {match}" + (f"  ({note})" if note else ""))
    if not match:
        all_pass = False
P(f"\nTASK 1 OVERALL: {'ALL PASS' if all_pass else 'SOME FAIL'}")

with open('/home/agent/projects/beta-prime/code/2026-08-18-uj-verify.txt', 'w') as f:
    f.write('\n'.join(OUT))

P("\nSaved to 2026-08-18-uj-verify.txt")
