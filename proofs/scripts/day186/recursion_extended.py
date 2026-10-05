#!/usr/bin/env python3
"""
Day 186: Extended h-basis recursion hunt.
Try X_n = sum_{k=1}^{n} A_k(q) h_k X_{n-k}, allowing all "add a strip of size k" terms.
"""
from sympy import symbols, expand, simplify, factor, Rational, Integer, Poly, solve

q = symbols('q')
h1, h2, h3, h4, h5, h6 = symbols('h1 h2 h3 h4 h5 h6', commutative=True)

X = {
    0: Integer(1),
    1: h1,
    2: (q + 1) * h1**2 - (q + 1) * h2,
    3: (q**2 + q + 1) * h3 - (2*q**2 + 3*q + 2) * h2 * h1 + (q + 1)**2 * h1**3,
    4: -(q + 1)*(q**2 + 1) * h4 + (q + 1)*(2*q**2 + q + 2) * h3 * h1
       + (q + 1)*(q**2 + q + 1) * h2**2
       - (q + 1)*(3*q**2 + 4*q + 3) * h2 * h1**2
       + (q + 1)**3 * h1**4,
}
h_map = {1: h1, 2: h2, 3: h3, 4: h4, 5: h5}
h_gens = [h1, h2, h3, h4, h5, h6]


def fit_recursion(n, allowed_terms):
    """Fit X_n = sum_{k} coef_k * term_k, where allowed_terms is a list of expressions."""
    coefs = symbols(f'a0:{len(allowed_terms)}')
    rhs = sum(c * t for c, t in zip(coefs, allowed_terms))
    diff = expand(X[n] - rhs)
    p_diff = Poly(diff, *h_gens)
    eqs = list(p_diff.as_dict().values())
    sol = solve(eqs, list(coefs), dict=True)
    return sol, coefs


print("=== Ansatz X_n = sum_{k=1..n} A_k(q,n) h_k X_{n-k}  (Zabrocki-type) ===\n")

for n in range(2, 5):
    print(f"--- n = {n} ---")
    terms = [h_map[k] * X[n-k] for k in range(1, n+1)]
    labels = [f"h_{k} * X_{{{n-k}}}" for k in range(1, n+1)]
    sol, coefs = fit_recursion(n, terms)
    if sol:
        s = sol[0]
        print(f"  Solution:")
        for lbl, c in zip(labels, coefs):
            val = s.get(c, c)  # free variables map to themselves
            print(f"    coef of {lbl}: {factor(simplify(val))}")
    else:
        print(f"  No solution.")
    print()

# The recursion X_n = sum_{k=1..n} A_k(q) h_k X_{n-k} is a classical form.
# For q=1, Stanley-Stembridge, path graphs, we know X_{P_n} satisfies:
# X_{P_n} = sum_{k=1..n} e_k * X_{P_{n-k}} * (-1)^{k-1} ... (not exactly)
# Actually, path chromatic sym fn has: p_1 X_{P_n} = ...

# Try a more constrained ansatz: X_n = A h1 X_{n-1} + B (some fixed comb) X_{n-2} + ...
# where coefficients are UNIVERSAL polynomials in q, n-independent.

print("=== Testing n-independent ansatz X_n = A(q) h_1 X_{n-1} + B(q) h_2 X_{n-2} + C(q) h_3 X_{n-3} + D(q) h_4 X_{n-4} ===")
print("(fit each n's data and see if A(q), B(q), C(q), D(q) stay CONSTANT in n)\n")

# For each n, solve for A, B, C, D universal.
# From n=2: X_2 = A h1 X_1 + B h2 X_0 => A h1^2 + B h2 = X_2 => A = q+1, B = -(q+1)
# From n=3: X_3 = A h1 X_2 + B h2 X_1 + C h3 X_0
#   h1 X_2 = (q+1)(h1^3 - h1 h2)
#   h2 X_1 = h1 h2
#   h3 X_0 = h3
#   So: A(q+1)h1^3 + [-A(q+1) + B] h1 h2 + C h3 = X_3
#     h1^3: A(q+1) = (q+1)^2 => A = q+1  ✓ (matches n=2)
#     h1 h2: -A(q+1) + B = -(2q^2+3q+2) => B = -(2q^2+3q+2) + (q+1)^2 = -(q^2+q+1)
#       BUT from n=2, B = -(q+1). MISMATCH.

print("From n=2: A = q+1, B = -(q+1)")
print("From n=3: A = q+1 (consistent!), but B = -(q^2+q+1) (INCONSISTENT with n=2).")
print()
print("=> Universal-coefficient 3-term h-basis recursion FAILS.")
print("   The h_k X_{n-k} coefficients depend on n.")

# Now try algebraic GF ansatz: does Z(z) = sum X_{P_n}(q) z^n satisfy a polynomial
# in z, Z, h1, h2, ... with q-coefficients?
# At q=1, Stanley's classical CSF for path graph: known algebraic (in p-basis via exp).
# At general q, unknown to me — Rick's Day 170 gives an algebraic F for the (q,t)
# path graph in a specific slice.

# Try: the "path graph deletion-contraction" identity.
# For path P_n: delete edge (n-1, n). Then chromatic quasisym satisfies:
#   X_{P_n}(q) = X_{P_{n-1}}(q) * (p_1 - h_1)   ???
# No — deletion/contraction is per-EDGE and gives the standard
#   chi_G = chi_{G-e} - chi_{G/e}   (chromatic polynomial)
# but for symmetric-fn version and with q, this is subtler.

# Try: does X_{P_n}(q) satisfy p_1 * X_{P_{n-1}} = X_{P_n} + q * (h_1^2 X_{P_{n-2}}) ???
# This would be a p-basis / power-sum recursion.

print()
print("=== Try p-basis / power-sum recursion via p_1 = h_1 ===")
print("Check if p_1 * X_{P_{n-1}} - X_{P_n} = q * h_2 * X_{P_{n-2}} or similar\n")

# p_1 = h_1. So p_1 * X_{n-1} - X_n = ?
for n in range(2, 5):
    diff = expand(h1 * X[n-1] - X[n])
    print(f"n={n}: h1 * X_{n-1} - X_n = {diff}")
    # Try dividing by h2 X_{n-2}:
    if n >= 2:
        candidate = h2 * X[n-2]
        try:
            from sympy import div
            # Poly division in the polynomial ring:
            p_diff = Poly(diff, *h_gens)
            p_cand = Poly(candidate, *h_gens)
            quo, rem = p_diff.div(p_cand)
            if rem.as_expr() == 0:
                print(f"     h1 X_{n-1} - X_n = ({factor(quo.as_expr())}) * h2 * X_{n-2}")
            else:
                print(f"     Not divisible by h2 * X_{n-2}. rem = {rem.as_expr()}")
        except Exception as e:
            print(f"     div error: {e}")


# Try a plethystic / Zabrocki H_t style ansatz.
# In Zabrocki 1998, there's an operator H_t s.t. Q_n = H_t(1) applied recursively
# gives Hall-Littlewood / Macdonald. Ellzey-Wachs proved q-analogue of the
# Shareshian-Wachs conjecture in a specific case using such operators.

# Direct check: is there a "modified Zabrocki" operator D_q such that
# X_{P_n}(q) = D_q^n(1)?
# If X_{P_n}(q) = D_q(X_{P_{n-1}}(q)) for some LINEAR operator D_q on Λ ⊗ Q(q),
# then Z(z) = sum X_{P_n} z^n = (1 - z D_q)^{-1}(1).

# Test: is X_n / X_{n-1} an "operator applied to X_{n-1}"? I.e., is there a
# LINEAR map (in h-basis) D_q s.t. D_q(X_{n-1}) = X_n?

# D_q would need to send h1 -> X_2 = (q+1)(h1^2 - h2), etc. Nonlinear in h so
# not really a linear operator on Λ — it's a differential operator.
#
# Well-known: X_{P_n} = h_1^n at q = 0? Let's check.

print()
print("=== q = 0 case ===")
for n in range(1, 5):
    v = X[n].subs(q, 0)
    print(f"  X_{{P_{n}}}(0) = {factor(v)}")
# Should be: at q=0, only INCREASING colorings, and only distinct-color... hmm
# actually at q=0 we keep only asc=0 colorings, i.e., WEAKLY DECREASING
# proper colorings of the path. A proper coloring with all c(i) >= c(i+1) is
# strictly decreasing = e_n? So X_{P_n}(0) = e_n?

print()
print("=== q = -1 case ===")
for n in range(1, 5):
    v = X[n].subs(q, -1)
    print(f"  X_{{P_{n}}}(-1) = {factor(v)}")
