"""Route 2b: GENERATING FUNCTION viewpoint on Psi.

Key identity: T(exp(x_1 u_1 + x_2 u_2 + x_3 u_3))
            = (1+x_1)^{u_1} (1+x_2)^{u_2} (1+x_3)^{u_3}.

So T is the transform "exp(x u) -> (1+x)^u" applied coordinate-wise.
Equivalently: T[F(x_1,x_2,x_3)] = F(log(1+x_1), log(1+x_2), log(1+x_3))
where F is expanded as sum_{a,b,c} f_{a,b,c} x_1^a x_2^b x_3^c / (a! b! c!).

For Psi(f) = T(f V)/V, if we take EGF in an auxiliary variable T of f = e_2^b/b!:
sum_b (e_2^b / b!) T^b = exp(T e_2)  = exp(T (u_1 u_2 + u_1 u_3 + u_2 u_3)).

So the FULL Psi generating function (not just top-weight) has expression:
F_full(T; u_1, u_2, u_3) = Psi(exp(T e_2))
                         = T_op[exp(T e_2) V] / V
                         = T_op[exp(T (u_1 u_2 + u_1 u_3 + u_2 u_3)) V] / V.

We can then extract the top-weight part.

Let's compute T_op[exp(T e_2) V] as a symbolic exercise.  This looks hard because
e_2 is not linear in each u_i.  But we can try.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau_var, u1, u2, u3
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3)
from sympy import (expand, Poly, Integer, factor, simplify, symbols, series,
                    Symbol, log, exp, together, Rational)

# Alternative: express T(f V) using integral/residue formula.
# We have T[u_i^n] = (u_i)_n = n! [x^n] (1+x)^{u_i}.
# So T[u_i^n f(u_1,u_2,u_3)] applied to a monomial u_1^a u_2^b u_3^c gives
# (u_1)_a (u_2)_b (u_3)_c.
#
# INTEGRAL FORM: T[u_i^n] = n! [x^n](1+x)^{u_i} = n!/(2pi i) \oint (1+x)^{u_i} / x^{n+1} dx.
# So T[g(u_1,u_2,u_3)] for g homogeneous can be written as an iterated residue.
# For g(u) = u_1^a u_2^b u_3^c, T[g] = (u_1)_a (u_2)_b (u_3)_c.
# Generating function: G(x_1,x_2,x_3) = sum_{a,b,c} g_{a,b,c} x_1^a x_2^b x_3^c / (a! b! c!)
# (EGF in each var). Then T[g] = "same G but at (u_i) instead of u_i^{a_i}", which
# equals G(log(1+x_1)/1, ...) but that's for f applied at.
# Actually:
# EGF_{a,b,c}(g)(x) := sum g_{a,b,c} x^a/a! x^b/b! x^c/c!
# then g = e_2^b V has a specific EGF representation, and T just shifts x_i -> log(1+x_i).

# For our purpose I want: coefficient of x_1^{a} x_2^{b} x_3^{c} in the expansion of
# g = e_2^k V.  These are specific.  Not sure of shortcut.

# --- Better strategy: use the algebraic identity for Psi(e_2^b) ---
# Since T is multiplicative on individual u-variables (T(u_i^a u_j^b) = T(u_i^a) T(u_j^b)
# when i != j), we have T factoring over products of independent-variable pieces.
# The Vandermonde V = (u1-u2)(u1-u3)(u2-u3) is NOT a product of independent-variable
# pieces, but we can expand it.
# Better: EACH monomial u_1^p u_2^q u_3^r has T image (u_1)_p (u_2)_q (u_3)_r,
# which factors as product of falling factorials.  So T is
# "T = (falling factorial substitution) applied coordinate-wise".

# Try: e_2 V = (u_1 u_2 + u_1 u_3 + u_2 u_3) * (u_1-u_2)(u_1-u_3)(u_2-u_3).
# Substitution: e_2 V is antisymmetric with a specific structure.
# Consider the identity e_2 V = (u_1^2 + u_2^2 + u_3^2 - e_1^2 + e_2) V? No, algebraic identity.
# Actually e_2 = e_1^2/2 - (u_1^2+u_2^2+u_3^2)/2... no, p_2 = e_1^2 - 2 e_2, so e_2 = (e_1^2 - p_2)/2.
# Hmm. Alternative: e_2 V = det of some 3x3 matrix?

# --- Let me just directly play with the "clean" formula for Psi(e_2^b) ---
# top(Psi(e_2^b)) = P_b(E1, E2, E3) has a factored EGF.
# The empirical form P_b(E1, E2, 0) = prod (E2 - r E1) is REALLY suggestive.
#
# Interpret: T([e_2^b V]|_{low_e3=0}) / V = prod (E2 - r*E1) top-part.
# But e_3 is a variable in u's, not a "low-e3" thing.
# Actually top-weight in (1,1,2) means top total degree.
# tops[b] is the top-DEGREE part of Psi(e_2^b) when we use the E-basis
# and w(E3)=2. This equals: (top-degree of Psi(e_2^b) in u_i, expressed in E1,E2,E3).
# Because Psi(e_2^b) has degree 2b in the u's, and top-degree part in u_i's
# expressed in E-basis has E-degree matching to weight = 2b.
# Wait: e_1 has u-degree 1, e_2 has u-degree 2, e_3 has u-degree 3. Then
# a monomial E1^a E2^b E3^c has u-degree a + 2b + 3c. NOT (1,1,2) weight.
# Hmm confusion. Let me recheck. Actually the code says weight_of_e_monom = i + j + 2*k.
# But u-degree of E1^i E2^j E3^k is i + 2j + 3k.
# So (1,1,2)-weight is NOT u-degree. Curious.

# Let me check by computing u-degree of top(Psi(e_2^b)) for small b:
from sympy import degree, Poly
E1_val = e1_u; E2_val = e2_u; E3_val = e3_u
for b in range(0, 5):
    psi_u = Psi_direct(e2_u**b) if b > 0 else Psi_direct(Integer(1))
    max_deg = 0
    if psi_u != 0:
        p = Poly(expand(psi_u), u1, u2, u3)
        for m, c in p.as_dict().items():
            if c != 0:
                max_deg = max(max_deg, sum(m))
    print(f"b={b}: u-degree of Psi(e_2^b) = {max_deg} (expected 2b = {2*b})")

# So Psi(e_2^b) has u-degree 2b.  In E-basis, top u-degree monomials satisfy
# i + 2j + 3k = 2b.  This is NOT the (1,1,2)-weight condition!
# So "top-weight" in the (1,1,2)-weight sense (i + j + 2k = b) is DIFFERENT from
# top u-degree.
# The (1,1,2)-weight is a different grading.  Where does it come from?
# Rick's context: this weight refers to something specific — likely a filtration
# on symmetric functions from the beta' calculus.

# The key observation is that (1,1,2)-weight assigns weight 1 to e_1, e_2, and weight 2 to e_3.
# In u-degree, e_i has degree i. So (1,1,2)-weight assigns weight 1 to e_1 (degree 1),
# weight 1 to e_2 (degree 2), and weight 2 to e_3 (degree 3).
# So (1,1,2)-weight = "u-degree floor divided by 2 rounded up... no.
# Weight = floor((u-degree+1)/2)?  E1: udeg 1 -> weight 1 (matches).
# E2: udeg 2 -> weight 1 (matches).
# E3: udeg 3 -> weight 2 (matches).
# So weight = ceil(u-degree/2).
# For E1^i E2^j E3^k: weight = i + j + 2k. u-degree = i + 2j + 3k.
# Are these related? i + j + 2k vs i + 2j + 3k. Differ by j + k.
# So weight = udeg - j - k.
# For top-weight-b, we need i + j + 2k = b.
# u-degree of that monomial: i + 2j + 3k = b + j + k = b + (j+k).
# Since Psi(e_2^b) has max u-degree 2b, we need b + j + k <= 2b, i.e. j + k <= b.
# But also i + j + 2k = b, so i = b - j - 2k >= 0 needs j + 2k <= b.
# So (1,1,2)-weight b is a specific slice, NOT the top u-degree.
# In particular the top u-degree monomials at weight b have j + k = 2b - (i+2j+3k)+... hmm.

# Let me just take the formula at face value. The empirical F(T) = A(T)*B(T) is the
# top-(1,1,2)-weight generating function. And we've verified the ODE
#   F'(T) = [(E2-E1)/(1+E1 T) - E3 T(3+E1 T)/(1+E1 T)^3] * F(T)
# holds equivalently to F = A B.

# --- Reorienting Route 2 ---
# Under the u-degree grading, top-u-degree of Psi(e_2^b) is the DIFFERENT operator
# 'top-degree Psi' which is easier to analyze algebraically. Maybe THAT's the more
# natural object.
# Let's compute the top-u-degree part of Psi(e_2^b) in E-basis, and see if it has
# a clean structure.
print("\n\n=== Top u-degree part of Psi(e_2^b) ===")
def top_udeg_in_ebasis(psi_e, target_udeg):
    p = Poly(expand(psi_e), E1, E2, E3)
    out = Integer(0)
    for m, c in p.as_dict().items():
        i, j, k = m
        if i + 2*j + 3*k == target_udeg:
            out += c * E1**i * E2**j * E3**k
    return out

for b in range(0, 5):
    psi_u = Psi_direct(e2_u**b) if b > 0 else Psi_direct(Integer(1))
    psi_e = sym_to_ebasis_direct(psi_u)
    top_ud = top_udeg_in_ebasis(psi_e, 2*b)
    print(f"  b={b}: top-u-deg part = {top_ud}")
    print(f"     factored: {factor(top_ud)}")
