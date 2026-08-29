"""Day 139 — Systematic hypothesis testing.

Attempt: N(b; x_1, x_2, x_3) might be a sum indexed by triples
(A, B, C, D, ...) partitioning [b] where D of size 2*x_3 = "special pairs" contributing E_3^{x_3}.

Concretely, extending the x_3=0 formula
  N(b; x_1, x_2, 0) = Σ_{U ⊆ [b], |U|=b-x2} (Π_U k) · e_{b-x1-x2}(U)
                    = Σ_{disjoint A,B,C: A∪B∪C=[b], |A|=x2, |B|=x1, |C|=b-x1-x2}
                        (Π_B k) · (Π_C k^2)

For x_3=1, we need to distinguish 2 elements as a "special pair" that give an E_3.
Try:
  N(b;x1,x2,1) = Σ_{(i,j) special pair, i<j} w(i,j) · N_{i,j}(b; x1, x2, 0-analog)

where N_{i,j} is the boundary formula restricted to [b] \\ {i,j}.

The simplest ansatz:
   N(b;x1,x2,1) = Σ_{i<j in [b]} w(i,j) · Σ_{U ⊆ [b]\\{i,j}, |U|=b-2-x2} (Π_U k) e_{b-2-x1-x2}(U)
              = Σ_{i<j} w(i,j) · N'(b-2; x1, x2)
where N'(b'; x1, x2) = Σ_{U ⊆ set of size b'} formula but indexed by the correct set.

Let's test this ansatz numerically. If the pair-weight is w(i,j) = c constant, then
   N(b;x1,x2,1) = c * Σ_{i<j in [b]} N_{i,j}(b-2; x1, x2)

where N_{i,j}(b-2; x1, x2) := Σ_{U ⊂ [b]\\{i,j}, |U|=b-2-x2} (Π_U k) e_{b-2-x1-x2}(U).

But summed over all pairs i<j, this is a symmetric function of [b].
Alternative: for a "hafnian" model with variable pair weights.

The simplest first-order test: check if
   N(b;x1,x2,1) / [Σ_{i<j in [b]} N_{ij}(b-2; x1, x2)] is a constant depending only on b.

Also test: could w(i,j) = a·(i+j) + b·ij + c ? Do a fit.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, sympify
from sympy import Rational, binomial, factorial, Matrix, solve, linsolve
from itertools import combinations

E1, E2, E3 = symbols('E1 E2 E3')


def sigma(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
        simultaneous=True))


def phi_map(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, -E1), (E3, -E3)], simultaneous=True))


def build_P(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}


def coeff(P_b, x1, x2, x3):
    d = Poly(P_b, E1, E2, E3).as_dict()
    return d.get((x1, x2, x3), Integer(0))


def N_boundary_on_S(S, x1, x2):
    """N-formula but summed over U ⊂ S with |U| = |S| - x2."""
    n = len(S)
    if x2 > n:
        return Integer(0)
    r = n - x1 - x2
    if r < 0:
        return Integer(0)
    total = Integer(0)
    for U in combinations(S, n - x2):
        if len(U) < r:
            continue
        prod_U = Integer(1)
        for k in U:
            prod_U *= k
        e_r = Integer(0)
        for T in combinations(U, r):
            m = Integer(1)
            for k in T:
                m *= k
            e_r += m
        total += prod_U * e_r
    return total


B_MAX = 8
P = build_P(B_MAX)

print("=" * 78)
print("PAIR-INDEXED HAFNIAN ANSATZ")
print("  N(b;x1,x2,1) ?= Σ_{i<j in [b]} w(i,j) * N_{S}(b-2; x1, x2)")
print("  where S = [b] \\ {i,j}")
print("=" * 78)

# For each b, extract N(b; x1, x2, 1) for all valid (x1, x2)
# and compute the "geometric factor" g_ij(x1, x2) = N_S(b-2; x1, x2)
# with S = [b] \ {i,j}.
# Then solve for w_ij.

# Start with b=3: only one pair (1,2), (1,3), (2,3). 3 unknowns.
# valid (x1,x2) at x3=1: x1+x2 <= 1.
# (0,0): N = 57
# (1,0): N = 25
# (0,1): N = 9
# 3 unknowns w_{12}, w_{13}, w_{23}, 3 equations.

# For each pair (i,j), S = [3]\{i,j} = singleton {k}
# N_S(1; 0, 0) = sum U ⊆ S, |U|=1: (prod k)*e_1(U) = for U={k}, k*k = k^2
# N_S(1; 1, 0) = |U|=1: (prod k) * e_0(U) = k
# N_S(1; 0, 1) = |U|=0: 1 * e_0(∅) = 1

def hafnian_fit(b):
    """Return system: for each pair (i,j), a column of coefficients for x_ij = w(i,j)."""
    from sympy import Symbol
    P_b = P[b]
    pairs = list(combinations(range(1, b+1), 2))
    # Collect equations for each (x1, x2) with x1+x2 <= b-2
    equations = []
    rhs = []
    coeff_matrix = []  # rows: eqs, cols: pairs
    row_labels = []
    for x1 in range(b - 1):
        for x2 in range(b - 1 - x1):
            if x1 + x2 > b - 2:
                continue
            row = []
            for (i, j) in pairs:
                S = tuple(k for k in range(1, b+1) if k != i and k != j)
                val = N_boundary_on_S(S, x1, x2)
                row.append(val)
            coeff_matrix.append(row)
            rhs.append(int(coeff(P_b, x1, x2, 1)))
            row_labels.append((x1, x2))
    return pairs, coeff_matrix, rhs, row_labels


# Try b=3
print("\n--- b=3 (constant weight test): ---")
pairs, mat, rhs, labels = hafnian_fit(3)
print(f"pairs: {pairs}")
print(f"matrix:")
for lab, row in zip(labels, mat):
    print(f"  (x1,x2)={lab}: {row}, rhs = {rhs[labels.index(lab)]}")

# Solve
from sympy import Matrix as M
A = M(mat)
b_vec = M([[r] for r in rhs])
try:
    sol = A.solve(b_vec)
    print(f"\nSolution:")
    for p, s in zip(pairs, sol):
        print(f"  w{p} = {s}")
except Exception as e:
    # Overdetermined? Try least squares
    print(f"Solve failed: {e}")

# Solve b=4
print("\n--- b=4: ---")
pairs, mat, rhs, labels = hafnian_fit(4)
print(f"pairs: {pairs}")
A = M(mat)
b_vec = M([[r] for r in rhs])
print(f"Matrix is {A.shape} — {'square' if A.rows == A.cols else 'overdet' if A.rows > A.cols else 'underdet'}")
try:
    if A.rows == A.cols:
        sol = A.solve(b_vec)
    else:
        # Try lstsq
        sol = (A.T * A).solve(A.T * b_vec)
        # verify
        resid = A * sol - b_vec
        print(f"Residual: {resid.T}")
    print(f"\nSolution:")
    for p, s in zip(pairs, sol):
        print(f"  w{p} = {s}")
except Exception as e:
    print(f"Solve failed: {e}")

# Same b=5
print("\n--- b=5: ---")
pairs, mat, rhs, labels = hafnian_fit(5)
A = M(mat)
b_vec = M([[r] for r in rhs])
print(f"Matrix is {A.shape}")
print(f"# pairs = {len(pairs)}, # eqs = {A.rows}")
try:
    if A.rows == A.cols:
        sol = A.solve(b_vec)
    elif A.rows > A.cols:
        # overdetermined
        try:
            sol = (A.T * A).solve(A.T * b_vec)
            resid = A * sol - b_vec
            print(f"Residual: {resid.T}")
            if all(r == 0 for r in resid):
                print("EXACT FIT")
            else:
                print("NO EXACT FIT — hafnian ansatz with constant w(i,j) fails")
        except Exception as e:
            print(f"Overdet solve failed: {e}")
    print(f"\nSolution:")
    for p, s in zip(pairs, sol):
        print(f"  w{p} = {s}")
except Exception as e:
    print(f"Solve failed: {e}")
