#!/usr/bin/env python3
"""
Day 186: Verify the recursion also holds for n=5 by computing X_{P_5}(q)
via direct enumeration.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day186')

from chromatic_qt_path import X_path_q_expanded, convert_m_to_basis, partitions, pretty_dict
from sympy import symbols, expand, simplify, factor, Integer, Poly

q = symbols('q')
n = 5

print(f"Computing X_{{P_{n}}}(q) by direct enumeration (may take a while)...")
xs = symbols(f'x1:{n + 2}')
m_dict = X_path_q_expanded(n)
print("Monomial basis:")
print(pretty_dict(m_dict))

h_dict = convert_m_to_basis(m_dict, 'h', n, list(xs))
print("h-basis:")
print(pretty_dict(h_dict))

# Now compare against recursion prediction.
h1, h2, h3, h4, h5 = symbols('h1 h2 h3 h4 h5', commutative=True)
h_map = {1: h1, 2: h2, 3: h3, 4: h4, 5: h5}

# Rebuild X_1..X_5 from h_dict format.
X_prev = {
    0: Integer(1),
    1: h1,
    2: (q + 1) * h1**2 - (q + 1) * h2,
    3: (q**2 + q + 1) * h3 - (2*q**2 + 3*q + 2) * h2 * h1 + (q + 1)**2 * h1**3,
    4: -(q + 1)*(q**2 + 1) * h4 + (q + 1)*(2*q**2 + q + 2) * h3 * h1
       + (q + 1)*(q**2 + q + 1) * h2**2
       - (q + 1)*(3*q**2 + 4*q + 3) * h2 * h1**2
       + (q + 1)**3 * h1**4,
}

def q_int(k):
    return sum(q**j for j in range(k))

# Predicted X_5 by recursion (form 1):
predicted = sum((-1)**(k-1) * q_int(k+1) * h_map[k] * X_prev[n-k] for k in range(1, n+1))
predicted += (-1)**n * q**n * h_map[n]
predicted = expand(predicted)

# Actual X_5 from h_dict:
def hdict_to_expr(hd):
    e = Integer(0)
    for lam, c in hd.items():
        term = Integer(1)
        for part in lam:
            term *= h_map[part]
        e += c * term
    return expand(e)

actual = hdict_to_expr(h_dict)

print()
print("Predicted X_5 by recursion:")
print(f"  {predicted}")
print()
print("Actual X_5:")
print(f"  {actual}")
print()
diff = expand(predicted - actual)
print(f"diff = {diff}   {'PASS - recursion holds for n=5!' if diff == 0 else 'FAIL - recursion breaks'}")
