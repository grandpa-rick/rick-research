"""
Derive analytically the dual cone of Phi(P_n) by computing the polar.

Phi(P_n) in R^n has H-rep defined by inequalities c.lambda <= 0 where (c_1, ..., c_n)
is in the polar cone (Phi(P_n))^* = {c : c.lambda <= 0 for all lambda in Phi(P_n)}.

A vector c is in the polar iff c.Phi(x) <= 0 for all x in P_n iff Phi^T c is in the polar
of P_n in R^{chain coords}.

Polar of P_n: (P_n)^* = {y in R^chain : y.x <= 0 for all x in P_n}.

P_n has H-rep: x in R^{chain} s.t. {chain ineqs}_j: A_j . x <= 0. So (P_n)^* = conic hull of
{-A_j} (the inward normals to the facets) extended by R^positive in directions of free
variables. Equivalently, c is in polar iff Phi^T c = - (non-neg combo of A_j).

So: c in (image polytope)^* iff there exist mu_j >= 0 with Phi^T c + sum mu_j A_j = 0.

Equivalently: -Phi^T c is in conic hull of {A_j}.

Equivalently: Phi^T c is in conic hull of {-A_j}, where -A_j are the inward normals.

OK let me just compute the polar dual abstractly.

For B_n, chain ineqs (after M_1 = 0):
   nn: -x_i <= 0 for each chain/NT coord x_i
   L_a: M_a - 2 sum_{b<a}(B_b - T_b) - 2 (B_{a-1} - T_{a-1}) <= 0? Wait L_a: M_a <= P_{a-1} = 2 sum_{b<a}(B_b - T_b). So L_a: M_a - 2(B_1 + ... + B_{a-1}) + 2(T_1 + ... + T_{a-1}) <= 0.
   U_a: M_a - 2 sum_{b<=a}(B_b - T_b) <= 0.
   E: S - 2 sum_b (B_b - T_b) <= 0.

I'll set up the system as a sympy LP/cone problem... actually simpler: just enumerate.

But also: just compute the polar directly via:

Phi(P_n) is a finitely-generated cone (= conic hull of Phi(extreme rays of P_n)).
Polar of this is intersection of half-spaces orthogonal to each extreme ray.

So I need: extreme rays of P_n. Then Phi() them. Then polar.

Let me do this for B_3 and B_4 symbolically.
"""

import itertools
import numpy as np
from fractions import Fraction

# B_3 setup
# Chain coords: (B1, T1, M2, B2, T2, S, Nm, Np) -- 8 vars (M_1=0)
# Constraints (Ax <= 0): nn x 8, L_2, U_2, E
def make_B3_system():
    labels = ['B1','T1','M2','B2','T2','S','Nm','Np']
    n = len(labels)
    A = []  # each row: vector of length n, meaning row . x <= 0
    for i in range(n):
        v = [Fraction(0)]*n
        v[i] = Fraction(-1)
        A.append(v)  # -x_i <= 0
    # L_2: M2 - 2 B1 + 2 T1 <= 0
    v = [Fraction(0)]*n
    v[labels.index('M2')] = Fraction(1)
    v[labels.index('B1')] = Fraction(-2)
    v[labels.index('T1')] = Fraction(2)
    A.append(v)
    # U_2: M2 - 2 B1 + 2 T1 - 2 B2 + 2 T2 <= 0
    v = [Fraction(0)]*n
    v[labels.index('M2')] = Fraction(1)
    v[labels.index('B1')] = Fraction(-2)
    v[labels.index('T1')] = Fraction(2)
    v[labels.index('B2')] = Fraction(-2)
    v[labels.index('T2')] = Fraction(2)
    A.append(v)
    # E: S - 2 B1 + 2 T1 - 2 B2 + 2 T2 <= 0
    v = [Fraction(0)]*n
    v[labels.index('S')] = Fraction(1)
    v[labels.index('B1')] = Fraction(-2)
    v[labels.index('T1')] = Fraction(2)
    v[labels.index('B2')] = Fraction(-2)
    v[labels.index('T2')] = Fraction(2)
    A.append(v)
    return labels, A

labels, A_B3 = make_B3_system()
print(f'B_3 chain system: {len(A_B3)} ineqs in {len(labels)} vars')
for i, row in enumerate(A_B3):
    s = ' + '.join(f'{c}*{labels[j]}' for j, c in enumerate(row) if c != 0)
    print(f'  ineq {i}: {s} <= 0')

# Polar dual: c is in polar iff Phi^T c = -sum mu_j A_j (with mu_j >= 0)
# Equivalently: Phi^T c is a non-positive combo of A_j, i.e., -Phi^T c in cone(A_j).
# Equivalently: Phi^T c in cone(-A_j) = cone of inward normals.

# For each combination c = (c_1, c_2, c_3), Phi^T c = (B1: c_1, T1: c_1, M2: c_2, B2: c_2,
#   T2: c_2, S: c_3, Nm: c_1 - c_2, Np: c_1 + c_2).
# Wait check: Phi: x -> (sum_i Phi_{0,i} x_i, ...). Phi^T c: (Phi^T c)_j = sum_i Phi_{i,j} c_i.

# Phi matrix (3 x 8): rows are lambda_1, lambda_2, lambda_3 in terms of x.
Phi_B3 = [
    [1,1,0,0,0,0,1,1],   # lambda_1
    [0,0,1,1,1,0,-1,1],  # lambda_2
    [-1,1,0,-1,1,1,0,0]  # lambda_3
]

def PhiT_c(c, Phi):
    # Phi^T c, returning vector of length n.
    n = len(Phi[0])
    return [sum(Phi[i][j] * c[i] for i in range(len(c))) for j in range(n)]

# For c in polar: -Phi^T c is non-neg combo of A_j. Equivalently, we need to solve LP:
#   find mu >= 0 s.t. -Phi^T c = A^T mu.
# Feasibility region for c.

# Print Phi^T c symbolically for c = (c1, c2, c3):
from sympy import symbols, Symbol
c1, c2, c3 = symbols('c1 c2 c3')
c = [c1, c2, c3]
phiTc = PhiT_c(c, Phi_B3)
print('\nPhi^T c =', list(zip(labels, phiTc)))

# Conditions on c: -Phi^T c = sum mu_j A_j with mu_j >= 0.
# Variables: c_1, c_2, c_3, and mu_0, ..., mu_{10}.
# 8 equations (one per chain coord), 14 unknowns (3 c + 11 mu).
# Slack: mu_j must be >= 0.

# We want: characterize the cone of valid c.
# Let me set up symbolically and try to read off conditions.

print('\nEquations -Phi^T c = sum mu_j A_j (one per chain coord):')
labels_ineq = ['nn_'+l for l in labels] + ['L2', 'U2', 'E']
from sympy import Matrix, zeros, eye

# Build A^T (8 rows x 11 cols)
A_mat = Matrix(A_B3)  # 11 x 8
AT = A_mat.T  # 8 x 11

# -Phi^T c = AT mu
# Solve for mu in terms of c, with mu free.
# Equivalently: form the system AT mu + Phi^T c = 0, solve.

mus = symbols('m0:11')  # 11 mu variables, m0..m10
lhs = AT * Matrix(mus) + Matrix(phiTc)  # should be zero vector

print('System (should be zero):')
for i, row in enumerate(lhs):
    print(f'  {labels[i]}: {row} = 0')

# This is 8 equations in 14 unknowns. Solve for 8 of them in terms of others.
from sympy import solve
sol = solve(list(lhs), list(mus), dict=True)
print('\nGeneral solution for mu in terms of c (and free params):')
if sol:
    for var, val in sol[0].items():
        print(f'  {var} = {val}')
else:
    print('  no solution')
