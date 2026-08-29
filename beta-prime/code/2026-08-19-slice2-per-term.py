"""Day 112 — Slice-2 per-term verification.

Task:
  Split u_j^(2)(b, c) into 4 terms T_0 + T_1 + T_2A + T_2B, run each term
  independently through the pipeline, get Q^(0), Q^(1), Q^(2A), Q^(2B),
  each as polynomials in b (with c symbolic).

For each R in {2, 3, 4}:
  1. Compute b-degree of Q^(0), Q^(1), Q^(2A), Q^(2B).
  2. Confirm Q^(0) + Q^(1) + Q^(2A) + Q^(2B) = Q_{2R}(0, b, c) (direct pipeline).

For R in {2, 3}: report closed-form expressions.

Also: attempt to rewrite T_2B's quadratic
   [b^2 + bc + c^2 + (2-3j)b + (1-3j)c + 3j(j-1)]
as a linear combination of products (b - alpha)^{fall r} (c - beta)^{fall s}
times polynomials in j of low degree — for Chu-Vandermonde compatibility.
"""
import sys
import sympy as sp
from sympy import (symbols, expand, factor, simplify, Poly, Integer, cancel, div,
                   Rational, Symbol, binomial)
from collections import defaultdict
from itertools import combinations


# =============================================================================
# PIPELINE HELPERS
# =============================================================================
def bt(M):
    """Build the shifted-Schur ensemble S_j up to j=M via vertical 2-strip additions,
    length <= 3.  Returns dict j -> [(mu, multiplicity), ...]."""
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


# =============================================================================
# THE 4-TERM (U_2) MODEL
# =============================================================================
def Shell0(j):
    return (fall_sym(c, 2) * fall_sym(c - 3, j - 2) *
            fall_sym(b + 1, 2) * fall_sym(b - 2, j - 2))


def Shell1(j):
    return (fall_sym(c, 2) * fall_sym(c - 3, j - 3) *
            fall_sym(b + 1, 2) * fall_sym(b - 2, j - 3))


def Shell2(j):
    return (fall_sym(c, 2) * fall_sym(c - 3, j - 4) *
            fall_sym(b + 1, 2) * fall_sym(b - 2, j - 4))


def T0(j):
    """mu_3 = 0 contribution."""
    if j == 0:
        return Integer(1)
    if j == 1:
        # mu = (1, 1, 0)
        return b * c + b + 2 * c
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
    return (j - 1) * (j - 2) * Shell1(j)


def T2B(j):
    """mu_3 = 2, mu_2 = j-2 contribution."""
    if j <= 3:
        return Integer(0)
    quad = b**2 + b * c + c**2 + (2 - 3 * j) * b + (1 - 3 * j) * c + 3 * j * (j - 1)
    return j * (j - 3) * Shell2(j) * quad


# =============================================================================
# Q_{2R}(0, b, c) from per-term u contributions, symbolic in c.
# =============================================================================
def Q_2R_per_term(R, uj_func):
    """Given uj_func(j) returning u_j part (b, c symbolic), compute
       Q_{2R}(0, b, c) = h_k / [(3)_{c-1-k}(b+2)_{c-1-k}]
       symbolically in b, c.

       Uses:
         H_c(0, b, j) = (3)_{c-1-j} (b+2)_{c-1-j} u_j
         h_k = sum_{j=0}^{k} (-1)^{k-j} C(k,j) H_c(0, b, j)
         Q_{2R}(0, b, c) = h_k / [(3)_{c-1-k}(b+2)_{c-1-k}]

       For symbolic c, use factored form:
         (3)_{c-1-j} = 3*4*...*(c+1-j)     has (c-1-j) factors, starting at 3
         (3)_{c-1-k} = 3*4*...*(c+1-k)
         Ratio (3)_{c-1-j} / (3)_{c-1-k} = (c+2-k)(c+3-k)...(c+1-j)
                                         = (c-k+2)^{rise(k-j)}   [start c-k+2, len k-j]
         (b+2)_{c-1-j} / (b+2)_{c-1-k} = (b+c-k+1)(b+c-k+2)...(b+c-j)
                                       = (b+c-k+1)^{rise(k-j)}
       so h_k / prefactor = sum_j (-1)^(k-j) C(k,j) (c-k+2)^{rise(k-j)} (b+c-k+1)^{rise(k-j)} u_j.
    """
    k = 2 * R
    tot = Integer(0)
    for j in range(k + 1):
        uj = uj_func(j)
        if uj == 0:
            continue
        L_j = k - j  # rise length
        rise_c = rise_sym(c - k + 2, L_j)
        rise_bc = rise_sym(b + c - k + 1, L_j)
        tot += (-1)**(k - j) * sp.binomial(k, j) * rise_c * rise_bc * uj
    return expand(tot)


def Q_2R_full_direct(R, c_val, T_ens):
    """Q_{2R}(0, b, c=c_val) via direct pipeline with numeric c.  For sanity check."""
    k = 2 * R
    L = c_val - 1 - k
    if L < 0:
        return None
    tot = Integer(0)
    for j in range(k + 1):
        # compute ds_j / V at a=0 with c=c_val
        y = (Integer(2), b + 1, Integer(c_val))
        ds = Integer(0)
        for mu, kk in T_ens[j]:
            ks = [mu[i] + (2 - i) for i in range(3)]
            M = [[fall_sym(y[i], ks[l]) for l in range(3)] for i in range(3)]
            d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                 - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                 + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            ds += kk * d
        ds = expand(ds)
        # divide by V at a=0, c=c_val
        V_val = (1 - b) * (2 - c_val) * (b - c_val + 1)
        # do polynomial division in b
        q, r = div(Poly(ds, b), Poly(V_val, b))
        if r.as_expr() != 0:
            P(f"    ! ds_{j}/V not exact for c={c_val}: remainder {r.as_expr()}")
            return None
        uj = expand(q.as_expr())
        Hj = rise_sym(3, c_val - 1 - j) * rise_sym(b + 2, c_val - 1 - j) * uj
        tot += (-1)**(k - j) * sp.binomial(k, j) * Hj
    hk = expand(tot)
    denom = rise_sym(3, L) * rise_sym(b + 2, L)
    q = expand(cancel(hk / denom))
    return q


# =============================================================================
# MAIN
# =============================================================================
P("=" * 78)
P("Day 112 — Slice-2 per-term verification (4-term U_2 model)")
P("=" * 78)

# We work with c SYMBOLIC (as instructed).  Per-term Q^(X) as poly in b, c.
# Then check b-degree.

for R in [2, 3, 4]:
    P()
    P("-" * 78)
    P(f"R = {R}  (k = 2R = {2*R})")
    P("-" * 78)
    Q_0  = Q_2R_per_term(R, T0)
    Q_1  = Q_2R_per_term(R, T1)
    Q_2A = Q_2R_per_term(R, T2A)
    Q_2B = Q_2R_per_term(R, T2B)
    Q_sum = expand(Q_0 + Q_1 + Q_2A + Q_2B)

    def bdeg(poly_expr):
        if poly_expr == 0:
            return -1
        return Poly(poly_expr, b).degree()

    P(f"  deg_b Q^(0)   = {bdeg(Q_0)}")
    P(f"  deg_b Q^(1)   = {bdeg(Q_1)}")
    P(f"  deg_b Q^(2A)  = {bdeg(Q_2A)}")
    P(f"  deg_b Q^(2B)  = {bdeg(Q_2B)}")
    P(f"  deg_b Q_sum   = {bdeg(Q_sum)}")

    # Sanity: compare Q_sum to direct pipeline for a few c values.
    T_ens = bt(2 * R)
    for c_val in [2 * R + 2, 2 * R + 3, 2 * R + 4]:
        Q_dir = Q_2R_full_direct(R, c_val, T_ens)
        Q_ans = expand(Q_sum.subs(c, c_val))
        diff = expand(Q_dir - Q_ans)
        match = (simplify(diff) == 0)
        P(f"  c = {c_val}:  direct vs per-term sum match? {match}")

    # For R = 2, 3: report closed forms in b, factored/collected.
    if R in [2, 3]:
        P()
        P(f"  Closed-form per-term Q^(X)(0, b, c) for R = {R}:")
        for name, Q in [('Q^(0)', Q_0), ('Q^(1)', Q_1), ('Q^(2A)', Q_2A), ('Q^(2B)', Q_2B)]:
            # Present as poly in b with c-coefficients (factored)
            pb = Poly(Q, b)
            deg = pb.degree()
            P(f"    {name}: deg_b = {deg}")
            for i, coef in enumerate(pb.all_coeffs()):
                actual_deg = deg - i
                cf = factor(coef)
                P(f"      b^{actual_deg} coeff: {cf}")
            P()
        # Total
        pb_s = Poly(Q_sum, b)
        deg_s = pb_s.degree()
        P(f"    Q_sum: deg_b = {deg_s}")
        for i, coef in enumerate(pb_s.all_coeffs()):
            actual_deg = deg_s - i
            cf = factor(coef)
            P(f"      b^{actual_deg} coeff: {cf}")


# =============================================================================
# STRUCTURAL ANALYSIS: T_2B's quadratic factor
# =============================================================================
P()
P("=" * 78)
P("Structural analysis: T_2B's quadratic factor")
P("=" * 78)
P()
P("Quadratic: Q(b,c,j) = b^2 + b c + c^2 + (2-3j) b + (1-3j) c + 3j(j-1).")
P()
P("Attempt: rewrite in a basis good for Chu-Vandermonde.")
P("We want (c - alpha)^{fall s} (b - beta)^{fall r} times poly(j) of low degree.")

j = symbols('j')
Qquad = b**2 + b*c + c**2 + (2 - 3*j)*b + (1 - 3*j)*c + 3*j*(j-1)

# Convert b^2 -> b(b-1) + b, c^2 -> c(c-1) + c.
Qquad_ff = expand(Qquad).subs({b**2: b*(b-1) + b, c**2: c*(c-1) + c})
Qquad_ff = expand(Qquad_ff)
P()
P("Expanded in falling-factorial basis (b^2 = b(b-1)+b, c^2 = c(c-1)+c):")
P(f"  {Qquad_ff}")
P()

# Try to organize by "monomials" in (b-alpha)(b-alpha-1)... × (c-beta)(c-beta-1)...
# In the context of T_2B, the shell is (b+1)b(b-2)^fall(j-4) and c(c-1)(c-3)^fall(j-4).
# So we have "used" (b+1)b*(b-2)*(b-3)... etc — remaining b-piece is polynomial;
# similarly for c.

# The remaining quadratic Q(b,c,j) sits atop this shell in T_2B.
# For CV to work, we want Q(b,c,j) = sum_i P_i(j) * (b - beta_i)^{r_i} * (c - gamma_i)^{s_i}
# with r_i, s_i shifted-into (b-2)^fall etc. structure so that Shell2 * Q reorganizes as
# sum of (b+1)b(b-2)^{fall (j-4+r)} × (c-...)^{...} times poly in j.

# Simplest: try to write Q(b,c,j) as A(j) * 1 + B(j) * (b-something) + ... in
# 2-D basis {1, (b-p), (c-q), (b-p)(c-q), (b-p)(b-p-1), (c-q)(c-q-1)}.

# Try center: shift b by an offset s.t. it aligns with the "next" (b-2)^fall factor.
# The current tail is (b-2)^{fall(j-4)}, whose last factor is (b - (j-5)) = (b - j + 5).
# The next one down would multiply by (b - (j-4)) = (b - j + 4) — but j-dependent.
# We can factor:  b^2 + ... = A + B*(b - x) + C*(b - x)(b - x - 1) with j-dep x.
# But CV needs j-independent shifts on b and c.

# Try direct decomposition in basis {1, b, c, b*(b-1), c*(c-1), b*c}:
basis_elts = [Integer(1), b, c, b*(b-1), c*(c-1), b*c]
basis_names = ['1', 'b', 'c', 'b(b-1)', 'c(c-1)', 'b*c']

# Fit Q = sum_i coef_i(j) * basis_elts[i]. Solve for coef_i as poly in j.
# Since Q is quadratic in b,c, and basis includes all quadratic monomials in b,c
# via {1,b,c,b(b-1),c(c-1),bc}, this is exact.

sol = sp.solve(
    [sp.Poly(Qquad - sum(sp.Symbol(f'A{i}')*basis_elts[i] for i in range(6)),
             b, c).nth(*deg) for deg in [(0,0), (1,0), (0,1), (2,0), (0,2), (1,1)]],
    [sp.Symbol(f'A{i}') for i in range(6)]
)
P("Q(b,c,j) in basis {1, b, c, b(b-1), c(c-1), b*c}:")
for i in range(6):
    key = sp.Symbol(f'A{i}')
    val = sol.get(key, 0)
    val_s = sp.expand(val)
    if val_s != 0:
        P(f"  {basis_names[i]:>12s} : {val_s}   (deg_j = {Poly(val_s, j).degree() if val_s != 0 else '-'})")
P()

# Try basis {1, b, c, b(b-1), c(c-3), b*c}: aligns better with shell (c-3)^fall
basis_elts2 = [Integer(1), b, c, b*(b-1), c*(c-3), b*c]
basis_names2 = ['1', 'b', 'c', 'b(b-1)', 'c(c-3)', 'b*c']
# Test whether Q can be expressed in this basis.
sol2 = sp.solve(
    [sp.Poly(Qquad - sum(sp.Symbol(f'B{i}')*basis_elts2[i] for i in range(6)),
             b, c).nth(*deg) for deg in [(0,0), (1,0), (0,1), (2,0), (0,2), (1,1)]],
    [sp.Symbol(f'B{i}') for i in range(6)]
)
P("Q(b,c,j) in basis {1, b, c, b(b-1), c(c-3), b*c}:")
for i in range(6):
    key = sp.Symbol(f'B{i}')
    val = sol2.get(key, 0)
    val_s = sp.expand(val)
    if val_s != 0:
        P(f"  {basis_names2[i]:>12s} : {val_s}   (deg_j = {Poly(val_s, j).degree() if val_s != 0 else '-'})")
P()

# Try aligning: what if we use (b-2)^{fall 2}, (c-3)^{fall 2}, etc.?
# (b-2)(b-3), (c-3)(c-4), (b-2), (c-3), (b-2)(c-3)
basis_elts3 = [Integer(1), b - 2, c - 3, (b-2)*(b-3), (c-3)*(c-4), (b-2)*(c-3)]
basis_names3 = ['1', 'b-2', 'c-3', '(b-2)(b-3)', '(c-3)(c-4)', '(b-2)(c-3)']
sol3 = sp.solve(
    [sp.Poly(Qquad - sum(sp.Symbol(f'C{i}')*basis_elts3[i] for i in range(6)),
             b, c).nth(*deg) for deg in [(0,0), (1,0), (0,1), (2,0), (0,2), (1,1)]],
    [sp.Symbol(f'C{i}') for i in range(6)]
)
P("Q(b,c,j) in basis {1, (b-2), (c-3), (b-2)(b-3), (c-3)(c-4), (b-2)(c-3)}:")
P("  (This basis aligns with Shell2's tails (b-2)^{fall(j-4)}, (c-3)^{fall(j-4)}.)")
for i in range(6):
    key = sp.Symbol(f'C{i}')
    val = sol3.get(key, 0)
    val_s = sp.expand(val)
    if val_s != 0:
        deg_j = Poly(val_s, j).degree() if val_s != 0 else '-'
        P(f"  {basis_names3[i]:>18s} : {val_s}   (deg_j = {deg_j})")
P()

# The really relevant thing for CV: the "j-content" of each basis element's coefficient.
# We want them to be POLYNOMIALS IN j OF LOW DEGREE (so that finite differences kill them).
# Anything degree <= 2R-1 gets killed by 2R-th finite diff.

# =============================================================================
# Save
# =============================================================================
with open('/home/agent/projects/beta-prime/code/2026-08-19-slice2-per-term.txt', 'w') as f:
    f.write('\n'.join(OUT))

P()
P("*** RESULTS SAVED to 2026-08-19-slice2-per-term.txt ***")
