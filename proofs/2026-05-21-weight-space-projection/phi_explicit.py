"""
Phase 1+2: explicit chain-to-weight map Phi at B_3, compute facet normals,
project them to weight space, test linear independence.

Chain coords: x = (M1, B1, T1, M2, B2, T2, S, N_minus, N_plus) in Z^9_{>=0}.
(NT block at B_3: roots E_1-E_2 (N_minus), E_1+E_2 (N_plus).)

We constrain M_1 = 0 (chain polytope lives in this hyperplane by Theorem F).

Weight nu = sum m_beta * beta in (E1, E2, E3):
  lambda_1 = M1 + B1 + T1 + N_minus + N_plus
  lambda_2 = M2 + B2 + T2 - N_minus + N_plus
  lambda_3 = -B1 + T1 - B2 + T2 + S

Phi: R^9 -> R^3, a Z-linear surjection.

Chain facets at B_3:
  L_2: M_2 <= P_1 = 2(B_1 - T_1),      i.e., M_2 - 2 B_1 + 2 T_1 <= 0
  U_2: M_2 <= P_2 = 2(B_1-T_1+B_2-T_2),  i.e., M_2 - 2 B_1 + 2 T_1 - 2 B_2 + 2 T_2 <= 0
  E:   S   <= P_2,                       i.e., S   - 2 B_1 + 2 T_1 - 2 B_2 + 2 T_2 <= 0

QUESTION (Q1): When we project the chain polytope P_3 to weight space via Phi,
do the boundaries Phi(L_2), Phi(U_2), Phi(E) become 3 DISTINCT codimension-1
hyperplanes in weight coordinates (i.e., 3 distinct facets of Phi(P_3))?

QUESTION (Q2): Does varying the NT-block (N_minus, N_plus) contribute >= 1
additional codim-1 hyperplane to the boundary of Phi(P_3)?

APPROACH:
  Compute image polytope Phi(P_3) explicitly by Fourier-Motzkin elimination.
  Read off the facets of the image polytope; identify each one.
"""

import numpy as np
from sympy import Matrix, Rational, eye, zeros, symbols, Poly, simplify

# Coordinate labels
labels = ['M1','B1','T1','M2','B2','T2','S','Nm','Np']
nvars = len(labels)

# Constraints on chain space P_3 (with NT block extension):
# Format: each row is (a, b) meaning a . x <= b. Use sympy for exact arithmetic.
# All as <=0 form: row is (A, 0) meaning A x <= 0, since b=0 throughout here.

constraints = []  # list of (vector, label)

def vec(**kwargs):
    v = [0]*nvars
    for k, val in kwargs.items():
        v[labels.index(k)] = val
    return v

# Non-negativity: -x_i <= 0, i.e., x_i >= 0
for L in labels:
    constraints.append((vec(**{L: -1}), f'nn_{L}'))

# M_1 = 0 (degenerate L_1). Encode as two inequalities: M1 <= 0 and -M1 <= 0
constraints.append((vec(M1=1), 'L1_M1<=0'))
# (nn_M1 above is -M1 <= 0)

# L_2: M_2 - 2 B_1 + 2 T_1 <= 0
constraints.append((vec(M2=1, B1=-2, T1=2), 'L2'))

# U_2: M_2 - 2 B_1 + 2 T_1 - 2 B_2 + 2 T_2 <= 0
constraints.append((vec(M2=1, B1=-2, T1=2, B2=-2, T2=2), 'U2'))

# E: S - 2 B_1 + 2 T_1 - 2 B_2 + 2 T_2 <= 0
constraints.append((vec(S=1, B1=-2, T1=2, B2=-2, T2=2), 'E'))

# U_1: M_1 <= P_1 = 2(B_1 - T_1), i.e., M_1 - 2 B_1 + 2 T_1 <= 0
# Already redundant given M_1 = 0 and B_1, T_1 generic; but include for completeness.
constraints.append((vec(M1=1, B1=-2, T1=2), 'U1'))

# Print system
print("Chain polytope constraints (Ax <= 0):")
for A, lbl in constraints:
    s = ' + '.join(f'{c}*{labels[i]}' for i, c in enumerate(A) if c != 0)
    print(f'  {lbl:8s}: {s} <= 0')

# Phi: R^9 -> R^3 given by the matrix
# lambda_1 = M1 + B1 + T1 + Nm + Np
# lambda_2 = M2 + B2 + T2 - Nm + Np
# lambda_3 = -B1 + T1 - B2 + T2 + S
Phi = Matrix([
    [1, 1, 1, 0, 0, 0, 0, 1, 1],   # lambda_1
    [0, 0, 0, 1, 1, 1, 0, -1, 1],  # lambda_2
    [0, -1, 1, 0, -1, 1, 1, 0, 0]  # lambda_3
])
print(f'\nPhi as 3x9 matrix:\n{Phi}')

# We want the image polytope Phi(P_3).
# We extend the system to (x, lambda) coordinates with:
#   Ax <= 0
#   Phi x = lambda (3 equalities)
# Then eliminate x to get the H-rep of Phi(P_3) in lambda alone.
#
# Use sympy's linear algebra + a Fourier-Motzkin loop.

# Variables: x_1, ..., x_9, lambda_1, lambda_2, lambda_3
# Total 12 vars. Order: eliminate x's first.

# Build matrix [A | 0_3] x_extended <= 0 (where x_extended = [x; lambda])
# Equality Phi x - lambda = 0 split into two inequalities Phi x - lambda <= 0 and -(Phi x - lambda) <= 0.

ext_nvars = nvars + 3  # x (9) + lambda (3)

ineqs = []  # list of vectors of length ext_nvars; meaning v . [x; lambda] <= 0

for A, lbl in constraints:
    row = list(A) + [0, 0, 0]
    ineqs.append((row, lbl))

# Phi x - lambda = 0  =>  add Phi x - lambda <= 0 and -(Phi x - lambda) <= 0
for i in range(3):
    row1 = list(Phi.row(i)) + [0,0,0]
    row1[nvars + i] = -1
    ineqs.append((row1, f'PhiUp_{i}'))
    row2 = [-c for c in Phi.row(i)] + [0,0,0]
    row2[nvars + i] = 1
    ineqs.append((row2, f'PhiDn_{i}'))

print(f'\nTotal inequalities: {len(ineqs)}')

# Fourier-Motzkin elimination of x_1, ..., x_9.
# Eliminate var index `vi`: split ineqs by sign of coefficient on vi.
#   pos: a_vi > 0, becomes x_vi <= (something)
#   neg: a_vi < 0, becomes x_vi >= (something)
#   zero: a_vi = 0, kept as-is
# For each pos × neg pair, combine to eliminate vi.

from fractions import Fraction

def to_fracs(row):
    return [Fraction(c) for c in row]

# Convert ineqs to Fraction form
ineqs_F = [(to_fracs(row), lbl) for row, lbl in ineqs]

def fm_eliminate(ineqs, var_idx):
    pos, neg, zero = [], [], []
    for row, lbl in ineqs:
        c = row[var_idx]
        if c > 0:
            pos.append((row, lbl))
        elif c < 0:
            neg.append((row, lbl))
        else:
            zero.append((row, lbl))
    new_ineqs = list(zero)
    for prow, plbl in pos:
        pc = prow[var_idx]
        for nrow, nlbl in neg:
            nc = nrow[var_idx]
            # We want to combine: (positive coef row) * |nc| + (negative coef row) * pc
            # so that the var_idx coefficient becomes pc*|nc| + nc*pc = 0.
            # i.e., new = |nc| * prow + pc * nrow.
            new = [abs(nc)*p + pc*n for p, n in zip(prow, nrow)]
            new_lbl = f'({plbl})+({nlbl})'
            # Normalize by gcd of nonzero entries to keep numbers small
            from math import gcd
            from functools import reduce
            nzs = [abs(c.numerator) for c in new if c != 0]
            if nzs:
                g = reduce(gcd, nzs)
                if g > 1:
                    new = [c / g for c in new]
            new_ineqs.append((new, new_lbl))
    return new_ineqs

cur = list(ineqs_F)
# Eliminate variables 0..8 (the x's)
for vi in range(nvars):
    print(f'Eliminating {labels[vi]} (var {vi}): {len(cur)} ineqs ...', end=' ')
    cur = fm_eliminate(cur, vi)
    print(f'-> {len(cur)} ineqs')

print(f'\nAfter eliminating all x: {len(cur)} inequalities in (lambda_1, lambda_2, lambda_3).')

# Now we have inequalities A_lambda * lambda <= 0 (since rhs = 0 throughout).
# Many are redundant. Print non-trivially-zero ones; then dedupe.

def normalize(row):
    """Drop x-coords (they should all be zero now), keep lambda coords, reduce."""
    lam_row = row[nvars:]
    # All x coords should be 0
    assert all(c == 0 for c in row[:nvars]), f'non-zero x coord left: {row}'
    return tuple(lam_row)

lam_ineqs = []
for row, lbl in cur:
    lr = normalize(row)
    if all(c == 0 for c in lr):
        continue  # 0 <= 0, trivial
    # Normalize by GCD then by sign of first nonzero to canonicalize.
    from math import gcd
    from functools import reduce
    nzs = [abs(c.numerator) for c in lr if c != 0]
    g = reduce(gcd, nzs)
    norm = tuple(c / g for c in lr)
    lam_ineqs.append((norm, lbl))

# Dedupe by normalized vector (same direction = same hyperplane scaled)
seen = {}
for norm, lbl in lam_ineqs:
    if norm not in seen:
        seen[norm] = []
    seen[norm].append(lbl)

print(f'\n{len(seen)} distinct constraint vectors after dedup:')
for norm, lbls in seen.items():
    s = ' + '.join(f'{c}*L{i+1}' for i, c in enumerate(norm) if c != 0)
    short_lbls = lbls[:3]
    print(f'  {s} <= 0   [via {len(lbls)} derivations, e.g. {short_lbls}]')

print('\n--- Done.')
