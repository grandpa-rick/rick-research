"""Day 139 — Alternative ansatz.

Idea: the E_3 factor arises from replacing two "singletons" in the p_b product
by a pair. Each singleton φ_k = E_2 + k E_1 + k² makes a triple choice.
A pair (i,j) with j-i > threshold might behave differently.

Alternative: think of the OPERATOR tau. Lemma 5 says τ(φ_k) = φ_{k+2} - (k+1)
and τ(E_3) = E_3 + φ_1.

Theorem 4:
  r_b^(1) = Σ_{j=1}^{b-1} (p_b/p_{j+1}) [3j τ̌(P_{j-1}) - j(j-1)(E_1+2j+2) τ̌(P_{j-2})]

Iterate — τ̌(P_{j-1}) = P_{j-1}|substituted, so at E_3^0 level τ̌(P_{j-1}) = P_{j-1}(E_1+3, 2E_1+E_2+3, E_1+E_2+1)
i.e. it's just plugging p_{j-1} shifted.

Actually specifically for [E_3^1] we only need τ̌(P_{j-1}) which is P_{j-1}|_{E_3=0} substituted:
τ̌(P_{j-1}) = p_{j-1}(E_1+3, 2E_1+E_2+3) — but wait, no, the E_3^1 part of τ(P_{j-1}) matters too,
via τ(E_3) = E_3 + φ_1: setting E_3=0 in τ(f) means E_3 -> φ_1, so...

Actually reading Lemma 5's proof more carefully:
  τ(f)|_{E_3=0} = f(E_1+3, 2E_1+E_2+3, φ_1)
i.e. E_1 -> E_1+3, E_2 -> 2E_1+E_2+3, E_3 -> φ_1 = E_1+E_2+1.

So τ̌(P_{j-1}) is a full polynomial in E_1, E_2 obtained by substituting P_{j-1}
with all three shifts. That means every E_3^k in P_{j-1} becomes φ_1^k contribution.

So r_b^(1) — computed via Theorem 4 — has TWO layers of history:
  - the boundary p_b/p_{j+1} factor (just E_1, E_2 polys)
  - the τ̌(P_{j-1}) which unfolds itself recursively.

**New idea**: Try to fit N(b;x1,x2,1) as a "signed sum over pairs" where
the pair (i,j) contributes with weight that DEPENDS on j-i (not the individual
values). Or as a sum indexed by triples (a, i, j) — i,j the "pair" and a a
"marker".

Direct approach: try to fit N(b;x1,x2,1) using the basis of Σ_{i<j in [b]} f(i,j)
* [x_3=0 boundary formula on complement] with f(i,j) = polynomial in i, j of low degree.

Ansatz:
   N(b;x1,x2,1) = Σ_{i<j} (α + β*i + γ*j + δ*i*j + ε*(i+j) + ...) N_ij(b-2;x1,x2)

Just try 3 different constant models:
   (a) f(i,j) = i*j
   (b) f(i,j) = i^2 j^2 (matches φ_k structure)
   (c) f(i,j) = (i-j)^2

Then explicitly test.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, sympify
from sympy import Rational, binomial, factorial, Matrix as M
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
    n = len(S)
    if x2 > n:
        return Integer(0)
    r = n - x1 - x2
    if r < 0:
        return Integer(0)
    total = Integer(0)
    for U in combinations(S, n - x2):
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


# Try: fit N(b;x1,x2,1) as Σ_{i<j in [b]} f(i,j) N_S(b-2;x1,x2) with S = [b]\{i,j}
# where f is a polynomial in i, j of bounded degree.

def fit_with_basis(b, basis_funcs, basis_names):
    """Try to fit N(b;x1,x2,1) as linear combo of Σ_{i<j} bf(i,j) N_S(b-2;x1,x2)."""
    # eq[k] (for basis func k): coefficient of c_k in a given (x1,x2) equation
    pairs = list(combinations(range(1, b+1), 2))
    equations = []
    labels = []
    rhs = []
    for x1 in range(b - 1):
        for x2 in range(b - 1 - x1):
            if x1 + x2 > b - 2:
                continue
            eq_row = []
            for bf in basis_funcs:
                s = Integer(0)
                for (i, j) in pairs:
                    S = tuple(k for k in range(1, b+1) if k != i and k != j)
                    s += bf(i, j) * N_boundary_on_S(S, x1, x2)
                eq_row.append(s)
            equations.append(eq_row)
            labels.append((x1, x2))
            rhs.append(int(coeff(P[b], x1, x2, 1)))
    A = M(equations)
    bvec = M([[r] for r in rhs])
    return A, bvec, labels


# Basis 1: constants (just one function f(i,j) = 1)
# Basis 2: {1, i+j, ij, i^2 + j^2, (i-j)^2, ...}

for b in [3, 4, 5, 6, 7, 8]:
    print(f"\n=== b = {b} ===")
    # Try polynomial-in-(i,j) basis of degree ≤ 4 in each variable, symmetric in (i,j)
    # Symmetric polynomials of degree up to 4 in i,j:
    # 1, i+j, ij, i^2+j^2, ij(i+j), (i^2+j^2)(...), (ij)^2, i^2+j^2+ij, etc.
    basis = [
        (lambda i, j: 1, "1"),
        (lambda i, j: i + j, "i+j"),
        (lambda i, j: i * j, "ij"),
        (lambda i, j: i*i + j*j, "i²+j²"),
        (lambda i, j: (i + j) * i * j, "ij(i+j)"),
        (lambda i, j: i*i*j*j, "(ij)²"),
        (lambda i, j: (i*i + j*j)*i*j, "ij(i²+j²)"),
        (lambda i, j: i*i*j + i*j*j, "ij(i+j)"),   # duplicate
        (lambda i, j: i**3 + j**3, "i³+j³"),
        (lambda i, j: i**4 + j**4, "i⁴+j⁴"),
        (lambda i, j: (i*j)**2 * (i + j), "(ij)²(i+j)"),
        (lambda i, j: (i*j)**3, "(ij)³"),
    ]
    # Deduplicate: filter out entry 7 (duplicate)
    basis = [b for k, b in enumerate(basis) if k != 7]
    basis_funcs = [b[0] for b in basis]
    basis_names = [b[1] for b in basis]

    A, bvec, labels = fit_with_basis(b, basis_funcs, basis_names)
    print(f"  Matrix: {A.shape}, {len(basis)} basis functions")
    print(f"  # equations: {len(labels)}")
    try:
        sol = (A.T * A).solve(A.T * bvec)
        resid = A * sol - bvec
        if all(r == 0 for r in resid):
            print("  EXACT FIT!")
            for name, s in zip(basis_names, sol):
                if s != 0:
                    print(f"    {name}: {s}")
        else:
            print(f"  Not exact — residual norm² = {sum(r*r for r in resid)}")
    except Exception as e:
        print(f"  Fit failed: {e}")


# Simple direct test: check pair-weight w(i,j) = 3*ij (matches structure of p)
print("\n\n" + "=" * 78)
print("TEST: w(i,j) = 3ij ?")
print("=" * 78)
for b in [3, 4, 5]:
    pairs = list(combinations(range(1, b+1), 2))
    print(f"\nb={b}:")
    all_match = True
    for x1 in range(b-1):
        for x2 in range(b-1-x1):
            if x1+x2 > b-2:
                continue
            actual = int(coeff(P[b], x1, x2, 1))
            s = Integer(0)
            for (i, j) in pairs:
                S = tuple(k for k in range(1, b+1) if k != i and k != j)
                s += 3*i*j * N_boundary_on_S(S, x1, x2)
            match = "OK" if actual == s else "MISS"
            if actual != s:
                all_match = False
            print(f"  N(b;{x1},{x2},1) = {actual}  vs Σ 3ij N_S = {s}  {match}")
    if all_match:
        print("  ALL MATCH!")


# Test w(i,j) = 3(ij)^2 / something
