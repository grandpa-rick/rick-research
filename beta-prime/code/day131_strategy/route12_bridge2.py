"""Turn the T-commutation identity into a Psi recursion.

We have:
  T(e_2 f) = e_2(u) T(f) - u_1 T((D_2+D_3) f) - u_2 T((D_1+D_3) f) - u_3 T((D_1+D_2) f)
             + T(e_2(D_1, D_2, D_3) f)

Applied with f = e_2^b V, then divide by V:

  Psi(e_2^{b+1}) = T(e_2 · e_2^b V)/V
                 = e_2(u) T(e_2^b V)/V
                   - u_1 T((D_2+D_3)(e_2^b V))/V - ...
                   + T(e_2(D_1,D_2,D_3)(e_2^b V))/V

Split into terms.  Let g = e_2^b V.  Then:
  (i)   e_2(u) T(g)/V = e_2(u) * Psi(e_2^b)
  (ii)  sum_i u_i T((D_j + D_k) g)/V  -- need to evaluate
  (iii) T(e_2(D_1,D_2,D_3) g)/V

Note D_i is a derivation, so D_i(f * g) = D_i(f) g + f D_i(g).
For g = e_2^b V:
  D_i(g) = D_i(e_2^b) V + e_2^b D_i(V)
         = b e_2^{b-1} D_i(e_2) V + e_2^b D_i(V).
  D_i(e_2) = u_i (partial e_2 / partial u_i) = u_i(u_j + u_k) where {i,j,k} = {1,2,3}.
  D_i(V) = u_i (partial V / partial u_i).  V = (u_1-u_2)(u_1-u_3)(u_2-u_3), so
     D_1(V) = u_1 * [(u_1-u_3)(u_2-u_3) + (u_1-u_2)(u_2-u_3)] = u_1 (u_2-u_3)(2 u_1 - u_2 - u_3).
     Etc.
By symmetry these are cleaner in the antisymm/symm decomposition.

We want to show the resulting identity, when converted to an ODE on the (1,1,2)-top-weight EGF
F(T) = sum tops[b] T^b / b!, becomes:
  F'(T) = [(E2-E1)/(1+E1 T) - E3 T (3 + E1 T)/(1+E1 T)^3] F(T).

Strategy for the deep-work session:
 (a) Reduce (ii) and (iii) to operators on Psi(e_2^b) modulo LOWER-weight terms.
     Because we care about the TOP-WEIGHT recursion, we can systematically discard
     lower-weight contributions.
 (b) The (1,1,2)-weight is preserved / shifted in a controlled way by:
       multiplication by u_i (which effectively multiplies by "some E_i" thing)
       and derivatives D_i (which lower or preserve weight).
 (c) The RHS should collect to give the explicit g_j coefficients.

This is a well-defined structural project.  Let me sanity check the RHS by computing
(ii) and (iii) for b=1..3 and seeing if the top-weight part matches
   sum_{j=1}^{b} (b)_j * g_j * tops[b-j]
   (the "correction" beyond the (E2 - (b+1) E1) tops[b] leading term).

Alternate cleaner form (via change of basis f -> Vandermonde-symmetric split):
   For symmetric g and antisymm h = V g, we have D_i(V) = ?
Actually let me just verify numerically that the identity gives the right recursion at top weight.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom, max_weight)
from sympy import expand, Poly, Integer, factor, simplify, symbols, Rational, diff

D1 = lambda p: expand(u1 * diff(p, u1))
D2 = lambda p: expand(u2 * diff(p, u2))
D3 = lambda p: expand(u3 * diff(p, u3))

def e2_D(p):
    return expand(D1(D2(p)) + D1(D3(p)) + D2(D3(p)))

def psi_recursion_via_T(b):
    """Compute Psi(e_2^{b+1}) using the T-identity, and compare with direct."""
    g = expand(e2_u**b * V)
    lhs_num = T_u(expand(e2_u * g))
    rhs_num = (expand(e2_u * T_u(g))
               - u1 * T_u(expand(D2(g) + D3(g)))
               - u2 * T_u(expand(D1(g) + D3(g)))
               - u3 * T_u(expand(D1(g) + D2(g)))
               + T_u(e2_D(g)))
    diff_check = expand(lhs_num - rhs_num)
    print(f"  b={b}: T-identity check on e_2^{b} V: {'OK' if diff_check == 0 else 'FAIL'}")

    # Now divide both sides by V:
    def divV(x):
        x = expand(x)
        q, r = Poly(x, u1, u2, u3).div(Poly(V, u1, u2, u3))
        if r.as_expr() != 0:
            print(f"    WARNING nonzero remainder: {r.as_expr()}")
        return q.as_expr()

    # Term-by-term:
    # (i) e_2(u) T(g)/V.  Note T(g)/V = Psi(e_2^b), so this is e_2(u) * Psi(e_2^b).
    # But e_2(u) is symmetric, and Psi(e_2^b) is symmetric.  Product is symmetric.
    # In E-basis: this is E_2 * Psi(e_2^b).
    term1 = expand(e2_u * divV(T_u(g)))  # ∈ symmetric poly
    # (ii) sum_i u_i T((D_j + D_k) g)/V  -- these are NOT symmetric individually
    # but they sum with (i) and (iii) to give symmetric Psi(e_2^{b+1}).
    # We need to handle them.
    # Divide each term by V:
    t_u1 = T_u(expand(D2(g) + D3(g)))
    t_u2 = T_u(expand(D1(g) + D3(g)))
    t_u3 = T_u(expand(D1(g) + D2(g)))
    # These are ANTISYMM (since D_i (antisymm) is not antisymm in general, but T
    # commutes with S_3, and (D_2 + D_3) applied to antisymm g...
    # Let's check: (D_2 + D_3) g = D_2 g + D_3 g, where D_i g is like "u_i times derivative".
    # If g is antisymm in u_1<->u_2, then D_2 g is not antisymm.
    # Actually the SUM u_1 T((D_2+D_3) g) + u_2 T((D_1+D_3)g) + u_3 T((D_1+D_2) g) IS
    # symmetric enough that after mult by symmetric u_i coefficients, dividing by V works.
    # Let's just check divisibility:
    S_middle = u1 * t_u1 + u2 * t_u2 + u3 * t_u3
    S_middle_div = divV(S_middle)  # will complain if not divisible
    # (iii) T(e_2(D) g)/V.
    term3 = divV(T_u(e2_D(g)))

    result = expand(term1 - S_middle_div + term3)
    # Compare with actual Psi(e_2^{b+1}):
    actual = Psi_direct(e2_u**(b+1))
    diff2 = expand(result - actual)
    print(f"    Reconstructed Psi(e_2^{b+1}) matches actual? {'YES' if diff2 == 0 else 'NO'}")
    if diff2 != 0:
        print(f"    diff = {diff2}")
    return term1, S_middle_div, term3, result

print("=== Verify the T-identity gives Psi(e_2^{b+1}) exactly ===")
for b in range(0, 5):
    psi_recursion_via_T(b)

# Now: extract TOP-WEIGHT part of each term and verify they combine as expected.
# For that we need each term separately in E-basis.
print("\n\n=== Top-weight contribution of each term (in E-basis) ===")
for b in range(1, 4):
    term1, term_mid, term3, result = psi_recursion_via_T(b)
    from task1_psi_e2_b5_b6 import sym_to_ebasis_direct
    # term1 is e_2(u) * Psi(e_2^b) — should be symmetric.
    # term_mid is not symmetric, but term_mid = e_2(u) Psi(e_2^b) + term3 - Psi(e_2^{b+1})? no.
    # Actually the full expression term1 - term_mid + term3 = Psi(e_2^{b+1}) is symmetric,
    # but term_mid individually is symmetric? Let's check.
    from itertools import permutations
    def is_symmetric(p):
        p = expand(p)
        subs_list = list(permutations([u1, u2, u3]))
        base = p
        for sigma in subs_list:
            q = p.subs({u1: sigma[0], u2: sigma[1], u3: sigma[2]}, simultaneous=True)
            if expand(q - base) != 0:
                return False
        return True
    print(f"\nb={b}:")
    print(f"  term1 (e2*Psi) symmetric? {is_symmetric(term1)}")
    print(f"  term_mid symmetric? {is_symmetric(term_mid)}")
    print(f"  term3 (T(e2(D) g)/V) symmetric? {is_symmetric(term3)}")

    # Print E-basis form of each (if symmetric)
    if is_symmetric(term1):
        term1_E = sym_to_ebasis_direct(term1)
        top1 = top_weight_part(term1_E, b+1)
        print(f"  top-weight(term1) = {top1}")
    if is_symmetric(term_mid):
        term_mid_E = sym_to_ebasis_direct(term_mid)
        top_mid = top_weight_part(term_mid_E, b+1)
        print(f"  top-weight(term_mid) = {top_mid}")
    if is_symmetric(term3):
        term3_E = sym_to_ebasis_direct(term3)
        top3 = top_weight_part(term3_E, b+1)
        print(f"  top-weight(term3) = {top3}")
