"""Extended verification of u_j formulas.

Task A: Verify Level 1 u_j closed form for j = 11, ..., 16.
Task B: Study D_j = u_j^(2) - c^{fall j}(b+1)^{fall j}, extract j^{fall l}
        coefficient polynomials in (b, c) for j = 0, ..., 10.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code')

from collections import defaultdict
from itertools import combinations
import sympy as sp
from sympy import symbols, expand, factor, simplify, Poly, Integer, cancel, div, Rational


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
P("Extended verification: Level 1 u_j (j=11..16), and Level 2 D_j structure")
P("=" * 78)

# =========================================================================
# TASK A: Verify u_j closed form at a = -1 for j = 11, ..., 16
# =========================================================================
P("\n" + "=" * 78)
P("TASK A: Level 1 u_j closed form for j = 11, ..., 16")
P("=" * 78)
P("Conjecture:")
P("  u_j = c^{fall j} * (b+1)^{fall j}")
P("       - j*(j-1) * c * (c-2)^{fall (j-2)} * (b+1) * (b-1)^{fall (j-2)}")
P()

# Build T table up through j=16
P("Building T table up to j=16 ...")
T16 = bt(16)
P("Done.")

taskA_results = []
for j in range(11, 17):
    dsj = ds(a, b, c, j, T16)
    q_poly, r_poly = div(Poly(dsj, a, b, c), Poly(V, a, b, c))
    if r_poly.as_expr() != 0:
        P(f"j = {j}: ds_j NOT divisible by V.  remainder = {r_poly.as_expr()}")
        taskA_results.append((j, False, "not divisible"))
        continue
    uj_full = expand(q_poly.as_expr())
    uj = expand(uj_full.subs(a, -1))

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
        P(f"    diff = {factor(diff)}")
    else:
        P(f"    u_j = {factor(uj)}")
    taskA_results.append((j, match, None))

# =========================================================================
# TASK B: Level 2 u_j^(2) = (ds_j / V)|_{a=0} - study D_j = u_j^(2) - c^{fall j}(b+1)^{fall j}
# =========================================================================
P("\n" + "=" * 78)
P("TASK B: Level 2 D_j = u_j^(2) - c^{fall j}(b+1)^{fall j}, j = 0, ..., 10")
P("=" * 78)

# Compute D_j
T10 = bt(10)
D_vals = {}  # j -> D_j as polynomial in (b, c)

for j in range(0, 11):
    dsj = ds(a, b, c, j, T10)
    q_poly, r_poly = div(Poly(dsj, a, b, c), Poly(V, a, b, c))
    if r_poly.as_expr() != 0:
        P(f"j = {j}: ds_j NOT divisible by V.")
        continue
    uj_full = expand(q_poly.as_expr())
    uj2 = expand(uj_full.subs(a, 0))
    D_j = expand(uj2 - fall_sym(c, j) * fall_sym(b + 1, j))
    D_vals[j] = D_j
    P(f"\nj = {j}:  D_j (factored) =")
    P(f"    {factor(D_j)}")

# Now do finite differences to extract coefficients of j^{fall l}.
# The idea: any polynomial-in-j sequence D_j = sum_l coef_l * j^{fall l} can be
# extracted via finite differences at j=0:
#   coef_l = (Delta^l D)_{j=0} / l!
# where Delta D_j = D_{j+1} - D_j.
#
# However, D_j is a polynomial in (b, c) with coefficients that may include
# things like (b-1), (b-2), ..., (c-1), (c-2), etc — so D_j is NOT simply a
# polynomial in j with (b,c)-coefficients. Even so, we can try to expand D_j
# as a polynomial in j with coefficients that are polynomials in (b, c).

# Convert each D_j to a polynomial in (b, c) with integer coefficients.
# Then treat the sequence D_0, D_1, ..., D_10 as a sequence of polynomials
# and apply finite differences. Each finite difference is itself a polynomial
# in (b, c).

P("\n" + "-" * 78)
P("Finite differences of D_j (treating j as varying).")
P("Extract coef_l(b,c) such that D_j = sum_{l=0}^L coef_l(b,c) * j^{fall l}.")
P("Using: coef_l(b,c) = Delta^l D_j evaluated at j=0, divided by l!.")
P("-" * 78)

max_j = 10
seq = [expand(D_vals[j]) for j in range(0, max_j + 1)]

# Compute forward differences.
# diffs[l][k] = Delta^l applied to sequence, starting at index k (so requires k+l <= max_j)
diffs = [seq[:]]  # diffs[0] = original
for l in range(1, max_j + 1):
    prev = diffs[-1]
    nxt = [expand(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)]
    diffs.append(nxt)

# coef_l = diffs[l][0] / l!
from math import factorial

coefs = {}
for l in range(0, max_j + 1):
    if len(diffs[l]) == 0:
        break
    v = diffs[l][0]
    c_l = expand(v / Integer(factorial(l)))
    coefs[l] = c_l

# Verify: D_j = sum_l coef_l * j^{fall l}
P("\nVerify reconstruction D_j = sum_{l=0}^{10} coef_l(b,c) * j^{fall l}:")
all_ok = True
for j in range(0, max_j + 1):
    if j not in D_vals:
        continue
    reco = Integer(0)
    jS = Integer(j)
    for l, cl in coefs.items():
        reco += cl * fall_sym(jS, l)
    diff = simplify(reco - D_vals[j])
    ok = (diff == 0)
    all_ok = all_ok and ok
    P(f"  j = {j}: reconstruction matches = {ok}")

P(f"\nAll reconstructions OK: {all_ok}")

# Print coefficient polynomials factored
P("\n" + "-" * 78)
P("Coefficient polynomials coef_l(b, c) for l = 0, 1, ..., 10:")
P("-" * 78)
for l in range(0, max_j + 1):
    if l not in coefs:
        continue
    cl = coefs[l]
    if cl == 0:
        P(f"\ncoef_{l}(b,c) = 0")
        continue
    cl_e = expand(cl)
    cl_f = factor(cl_e)
    P(f"\ncoef_{l}(b,c):")
    P(f"  expanded: {cl_e}")
    P(f"  factored: {cl_f}")

# Specifically report the asked-for ones
P("\n" + "=" * 78)
P("SPECIFIC REQUESTED COEFFICIENTS")
P("=" * 78)
for l in [0, 1, 2, 3, 4]:
    if l in coefs:
        cl_f = factor(coefs[l])
        P(f"\nCoefficient of j^{{fall {l}}}:")
        P(f"  {cl_f}")

# Truncation check: are coefficients zero beyond some l?
P("\n" + "-" * 78)
P("Which coef_l are nonzero?")
P("-" * 78)
nz = [l for l in range(max_j + 1) if l in coefs and expand(coefs[l]) != 0]
P(f"Nonzero coefs at l = {nz}")
P(f"(If D_j is polynomial in j of degree <= d, only l = 0, ..., d appear nonzero.)")

# Attempt to check whether D_j is actually a polynomial in j with (b,c)-coeffs
# by checking whether coef_l = 0 for l > some threshold. Note: D_j is NOT
# polynomial in j alone because coefs like (b - (j-2)), (c - (j-1)) appear,
# so we do NOT expect truncation. But we can see the growth structure.

# Optional: also examine E_j := u_j^(2) but structured differently.
# Original ask suggests trying D_j = j*(...) - j^{fall 2}*(...) + j^{fall 4}*(...).
# So check: is coef_l = 0 for l = 0, 3, and other l between 4 and top?

# Better structure attempt: consider substitution. Let's also try the
# "level-1-shifted" ansatz to see if a subset of coefs vanish.

P("\n" + "-" * 78)
P("Try ansatz A: D_j = alpha(j) * c * (c-2)^{fall (j-2)} * (b+1) * (b-1)^{fall (j-2)}")
P("             + beta(j) * <higher order>")
P("-" * 78)
# Subtract the level-1-like correction with coefficient j*(j-1) and see remainder.
# In level 1: correction was -j*(j-1)*c*(c-2)^fall(j-2)*(b+1)*(b-1)^fall(j-2).
# Try same shape but different scalar coefficient A(j).

# For each j >= 2, compute D_j / [c*(c-2)^{fall (j-2)}*(b+1)*(b-1)^{fall (j-2)}]
# and see if the quotient simplifies.
P()
for j in range(2, 11):
    if j not in D_vals:
        continue
    denom = c * fall_sym(c - 2, j - 2) * (b + 1) * fall_sym(b - 1, j - 2)
    if denom == 0:
        continue
    q = simplify(D_vals[j] / denom)
    P(f"j = {j}:  D_j / [c*(c-2)^fall_{j-2}*(b+1)*(b-1)^fall_{j-2}] = {factor(q)}")

# Save output
with open('/home/agent/projects/beta-prime/code/2026-08-18-uj-extended.txt', 'w') as f:
    f.write('\n'.join(OUT))

P("\n" + "=" * 78)
P("SUMMARY")
P("=" * 78)
P("\nTASK A (Level 1 u_j formula for j = 11..16):")
all_pass = all(m for _, m, _ in taskA_results)
for j, m, note in taskA_results:
    P(f"  j = {j}: match = {m}" + (f"  ({note})" if note else ""))
P(f"\nTASK A OVERALL: {'ALL PASS' if all_pass else 'SOME FAIL'}")

P("\nTASK B: See coefficient polynomials above.")
P(f"  Nonzero coefs at l = {nz}")

with open('/home/agent/projects/beta-prime/code/2026-08-18-uj-extended.txt', 'w') as f:
    f.write('\n'.join(OUT))
P("\nSaved to 2026-08-18-uj-extended.txt")
