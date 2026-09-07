"""Day 169 Step 15 — Find closed form for L_{-1}.

The δ=2 diagonal of the Riccati is linear in L (up to L^2 which comes in via G^2 but
that's wt+wt so wt (m+2-a)+(m+2-b) with a+b = 4 ==> lower wt at [T^m], not contributing to δ=2).

Actually L^2 CAN appear at δ=2 diagonal:
  G^3 layer 2 (e=2): 3 H^2 L + 3 H K^2 (no L^2). OK.
  G^2 layer 2 (e=2): 2 H L + K^2 (no L^2). OK.
So the δ=2 equation is LINEAR in L. Good — the equation for L is a linear equation.

Structure: [linear operator on L] = [expression in H, K].

Let me now separate the linear-in-L part and the "source" part explicitly.
"""
import sympy as sp

T, E1, E2, s, p = sp.symbols('T E1 E2 s p')
s, p = E1, E2  # aliases

# Reuse setup from step 14
def wt_split(expr, s, p):
    result = {}
    if expr == 0: return result
    poly = sp.Poly(expr, s, p, T)
    for (ds, dp, dT), coef in poly.terms():
        w = ds + 2*dp
        term = coef * s**ds * p**dp * T**dT
        result[w] = result.get(w, sp.S(0)) + term
    return result

def to_coefs(split_dict):
    result = {}
    for w, e in split_dict.items():
        pol = sp.Poly(e, T)
        for (dT,), c in pol.terms():
            result[(w, dT)] = c
    return result

q2_x = (1 - s*T)**2 - 4*p*T**2
D = lambda k: -q2_x + T**2 + k*T
P3 = T**2 * D(6)
P2 = ((s+3)*T - 1) * D(8)
P1 = (1 + s + p) * D(10) + 2

P1_coefs = to_coefs(wt_split(P1, s, p))
P2_coefs = to_coefs(wt_split(P2, s, p))
P3_coefs = to_coefs(wt_split(P3, s, p))

# Contributions to δ=2 diagonal:
# For each Riccati term (top_X, X_layer_e formula), enumerate (w, d, e) with
# e = w - d + top_X - 2, e in {0, 1, 2} (only these layers exist for our purposes).

# Now, separate L parts and source parts.
# L appears at layer e = 2 for G, G', G'', G''' (as L, L', L'', L''').
# For G^2 layer e = 2: L^2 doesn't appear but 2 H L does. So L appears linearly.
# For G^3 layer e = 2: 3 H^2 L appears (linear in L).
# For G G' layer e = 2: H L' + L H'. Linear in L (and L').
# Sub-sub-top of Riccati contains L, L', L''.

# Linear-in-L part:
# From P_3 G'' (contribution e = w - d + 4 - 2 = w - d + 2):
#   For e = 2: w - d = 0, i.e., w = d. P_3^[w][d]. Sum over w = d:
#     P_3^[0][0] = 0 (P_3 has no T^0 term). P_3^[1][1] = 0. P_3^[2][2] = 0.
#     Actually P_3^[w] has T-degrees from 2 onward (P_3 = T^2 D_6). So w = d requires d >= 2, w = d, but
#     P_3^[0] has d in {2,3,4}, P_3^[1] has d in {3}, P_3^[2] has d in {4}. w=d requires d=w.
#     So (w, d, e=2) = (2, 2), but P_3^[2] has no T^2 coef. => nothing.
#   For e = 2 in G'' means L''.
#   Hmm wait let me re-examine.

# P_3 G'' contributes to δ=2 via (w, d, e) with e = w - d + 4 - 2 = w - d + 2 and e = 2.
# So w - d + 2 = 2, i.e., d = w.
# For (w, d = w) to be in P_3 coefs: P_3^[0] has smallest d = 2, so w = 0 gives d = 0 — but P_3^[0][0] = 0.
# Same for w = 1: P_3^[1][1] = 0. And P_3^[2][2] = 0 (only d=4 for w=2).
# So P_3 G'' has NO contribution to L''.

# Similarly for other terms:
# P_3 G G' (top_X = 5): e = w - d + 5 - 2 = w - d + 3. e = 2 requires d = w + 1.
#   P_3^[0][1] = 0. P_3^[1][2] = 0. P_3^[2][3] = 0.
#   Also gives L' contributions (e = 2 of G G' includes H L' + L H').
#   Nope, no contribution.
# P_3 G^3 (top_X = 6): e = w - d + 6 - 2 = w - d + 4. e = 2 requires d = w + 2.
#   P_3^[0][2] = -1. So contribution: -1 * T^2 shift * (G^3)^{[e=2]}.
#     (G^3)^{[e=2]} = 3 H^2 L + 3 H K^2.
#   P_3^[1][3] = 2s. Contribution: 2s T^3 * (G^3)^{[e=2]}.
#   P_3^[2][4] = 4p - s^2. Contribution: (4p - s^2) T^4 * (G^3)^{[e=2]}.
# P_2 G' (top_X = 3): e = w - d + 3 - 2 = w - d + 1. e = 2 requires d = w - 1.
#   P_2^[0][d=-1]: invalid. P_2^[1][0]: P_2^[1] has smallest d = 1, so P_2^[1][0] = 0.
#   P_2^[2][1]: P_2^[2] has d in {2,3}, so P_2^[2][1] = 0.
#   P_2^[3][2]: P_2^[3] has d = 3, so P_2^[3][2] = 0.
#   So P_2 G' has no e = 2 contribution. Only e = 0, 1 contributions.
#   e = 1 requires d = w. Check (w, d = w): P_2^[0][0] = 1, P_2^[1][1] = -3s, P_2^[2][2] = 3s^2 - 4p, P_2^[3][3] = 4ps - s^3.
#   These contribute to K' via (G')^[e=1] = K'.
# P_2 G^2 (top_X = 4): e = w - d + 4 - 2 = w - d + 2. e = 2 requires d = w.
#   P_2^[0][0] = 1: contribution 1 * T^0 * (G^2)^{[e=2]} = 2 H L + K^2.
#   P_2^[1][1] = -3s: contribution -3s T (2 H L + K^2).
#   P_2^[2][2] = 3s^2 - 4p: (3s^2 - 4p) T^2 (2 H L + K^2).
#   P_2^[3][3] = 4ps - s^3: (4ps - s^3) T^3 (2 H L + K^2).
# P_1 G (top_X = 2): e = w - d + 2 - 2 = w - d. e = 2 requires d = w - 2.
#   P_1^[0][d=-2]: invalid. P_1^[1][d=-1]: invalid.
#   P_1^[2][0]: P_1^[2][0] = -p. Contribution: -p * L[m].
#   P_1^[3][1]: P_1^[3][1] = 2ps. Contribution: 2ps T * L[m-1].
#   P_1^[4][2]: P_1^[4][2] = 4p^2 - ps^2. Contribution: (4p^2 - ps^2) T^2 L[m-2].

# So the LINEAR L operator part of δ=2 equation:
# LHS(L) = [P_3 G^3 term with L] + [P_2 G^2 term with L] + [P_1 G term with L]
#        = [linear operator on L]
# Rearranging: LHS(L) = -RHS (source in H, K).

# Let's compute LHS(L) and RHS explicitly as series in T.
# L parts:
# From P_3 G^3 (e=2 layer of G^3): terms with L:
#   (G^3)^[2] = 3 H^2 L + 3 H K^2. L part = 3 H^2 L.
# So P_3 G^3 L-part contribution:
#   [-T^2 + 2sT^3 + (4p-s^2)T^4] * 3 H^2 L
#   = R_3(T) * 3 H^2 L
# where R_3(T) = -T^2 + 2sT^3 + (4p - s^2) T^4 (same as top-diagonal R_3).
#
# From P_2 G^2 (e=2 of G^2): terms with L:
#   (G^2)^[2] = 2 H L + K^2. L part = 2 H L.
# P_2 G^2 L-part:
#   [1 - 3sT + (3s^2 - 4p)T^2 + (4ps - s^3) T^3] * 2 H L = R_2(T) * 2 H L
# where R_2(T) = 1 - 3sT + (3s^2 - 4p) T^2 + (4ps - s^3) T^3. (Same as top-diagonal R_2.)
# Wait: earlier I had R_2 = 1 - 3sT + (-4p + 3s^2) T^2 + (4ps - s^3) T^3. Same.
#
# From P_1 G (e=2): L part = L. Coefficient:
#   P_1^[2][0] * T^0 + P_1^[3][1] * T + P_1^[4][2] * T^2 = -p + 2psT + (4p^2 - ps^2) T^2
#   = R_1(T) (same as top-diagonal R_1).
# P_1 G L-part: R_1(T) * L.

# So LINEAR L OPERATOR on L is: [R_3 * 3 H^2 + R_2 * 2 H + R_1] * L.
# But recall top-diagonal equation: R_3 H^2 + R_2 H + R_1 = 0 (dividing by H).
# So R_1 = -R_3 H^2 - R_2 H.
# Substituting: L-operator = 3 R_3 H^2 + 2 R_2 H + (-R_3 H^2 - R_2 H) = 2 R_3 H^2 + R_2 H = H (2 R_3 H + R_2).
# From top-diagonal eq: R_3 H^2 + R_2 H + R_1 = 0. If H solves R_3 H^2 + R_2 H + R_1 = 0, then
# ∂/∂H of LHS = 2 R_3 H + R_2 = discriminant square-root (up to sign).
# Actually R_3 H^2 + R_2 H + R_1 = 0 => 2 R_3 H + R_2 = ±sqrt(R_2^2 - 4 R_3 R_1). This is the discriminant.

# So the L-operator IS L times a specific function of T (no derivatives of L!)
# Actually wait — I forgot the derivative terms.

# Hmm wait: In P_3 G G' contributions to L' (via e=2 of GG' = H L' + L H' + K K'), and
# P_3 G'' contributions to L'' (via e=2 of G'' = L''), and P_2 G' contributions to L' (via e=2 of G' = L').
# But we established P_3 G'', P_3 G G', P_2 G' have NO e=2 (or the coefs are zero).
# So L operator has NO derivatives! It's just linear multiplication by [2 R_3 H^2 + R_2 H] = H (2 R_3 H + R_2).

# Let me verify this compute-wise. It's an amazing simplification if true.

T, E1, E2 = sp.symbols('T E1 E2')
s, p = E1, E2
Y = sp.symbols('Y')

R3 = -T**2 + 2*s*T**3 + (4*p - s**2) * T**4
R2 = 1 - 3*s*T + (3*s**2 - 4*p) * T**2 + (4*p*s - s**3) * T**3
R1 = -p + 2*p*s*T + (4*p**2 - p*s**2) * T**2

# H = E_2 Y / T. Compute L_operator = 2 R_3 H^2 + R_2 H.
H_expr = E2 * Y / T
L_op = sp.expand(2 * R3 * H_expr**2 + R2 * H_expr)
print(f"L-operator = 2 R_3 H^2 + R_2 H = {L_op}")

# Reduce modulo Y = T(1 + E1 Y + E2 Y^2):
Y2_sub = (Y - T - T*E1*Y) / (T*E2)  # from Y - T - T E_1 Y - T E_2 Y^2 = 0
# Multiply by T^2 to clear denominators:
L_op_T2 = sp.expand(L_op * T**2)
# Iteratively reduce Y^k for k >= 2
def reduce_Y(expr, max_iter=20):
    e = sp.expand(expr)
    for _ in range(max_iter):
        pp = sp.Poly(e, Y) if Y in e.free_symbols else None
        if pp is None or pp.degree() < 2:
            break
        e = sp.expand(e.subs(Y**2, Y2_sub))
    return e

L_op_T2_reduced = reduce_Y(L_op_T2)
print(f"\nL-op * T^2, reduced: {sp.expand(L_op_T2_reduced)}")

# Also express as function of q, Y.
# Actually since 2 R_3 H + R_2 = ± discriminant/H, and R_3 H^2 + R_2 H + R_1 = 0,
# the L-operator = H * (2 R_3 H + R_2). Compute directly.

L_op2 = sp.expand(H_expr * (2*R3*H_expr + R2))
print(f"\nL-op via H(2 R_3 H + R_2): {sp.expand(L_op2)}")

# Check: is L_op ± symmetric with q, Y, etc?
# Let's substitute the known relations and see if the L-op simplifies to something nice.

# Substitute Y in terms of q and T using formulas.
# Or check numerically: L-op at series level.

# Now compute the SOURCE term (RHS = -H-K only parts of the equation).
# It's the constant term (in L). Let's extract all non-L contributions.
# Wait we still need K' from P_2 G'; K^2 (G^2 e=2 K^2); 3 H K^2 (G^3 e=2 K^2 part); H K' + K H' + K K'
# (G G' e=2 includes: (a=0,b=2): H*L' (skip - has L); (a=1,b=1): K K'; (a=2,b=0): L H' (skip); so K K' only for non-L parts... wait
# Actually e=2 of G G' = H L' + K K' + L H'. Non-L parts: K K'.
# Wait I need to enumerate all (a,b) with a+b=2: (0,2): H*L' (has L'); (1,1): K K'; (2,0): L H' (has L).
# So GG' at e=2, non-L part = K K'.

# Also G'' at e=2: L''. All L.
# G' at e=2: L'. All L. So P_2 G' has NO L' contribution (from step above), so K' contribution comes from e=1 not e=2.
# But P_2 G' e=1 contributes at wt δ=1, not δ=2!

# Actually re-examine: e = w - d + top_X - δ where δ is the diagonal offset from max wt.
# For δ = 2 (sub-sub-top of Riccati), e = w - d + top_X - 2.
# For P_2 G' with e = 2: w - d + 3 - 2 = w - d + 1 = 2 => d = w - 1.
# (w, d): (0, -1) invalid; (1, 0): P_2^[1][0] = 0; (2, 1): P_2^[2][1] = 0; (3, 2): P_2^[3][2] = 0. None contribute.
# For e = 1 (K'): w - d + 1 = 1 => d = w. P_2^[0][0] = 1: contributes K' at wt (m+3 -2 = m+1)? Let me recompute wt.
# The wt of the contribution at [T^m] is w + top_X - d - e + m = w + 3 - d - e + m. For δ = 2, we need wt = m + 4 - 2 = m + 2.
# So w + 3 - d - e = 2, i.e., e = w + 1 - d. For (w, d) = (0, 0), e = 1. YES.
# So P_2 G' contributes at δ = 2 via e = 1 (K'): P_2^[0][0] * K' = K'. Also P_2^[1][1] * K', etc.

# Let me redo the enumeration carefully — I was sloppy.

# Recompute δ=2 contribution formula:
# For P_i^[w][d] * X^{[e]}: wt at [T^m] = w + (m - d) + top_X - e.
# For δ=2 (wt = m + 2): w - d + top_X - e = 2, i.e., e = w - d + top_X - 2.

# Now for each Riccati term:
# P_3 G'' (top_X = 4): e = w - d + 2. Contributions at each e in {0, 1, 2}:
#   e=0: w - d = -2, d = w + 2. (0, 2) = -1, (1, 3) = 2s, (2, 4) = 4p - s^2. Contribs: -H'' + 2s T H''... wait.
#   Actually T^d shift means [T^m] (T^d * f)[m] = f[m-d]. So contribution to series is c_wd * T^d * X^[e].
#   For e=0: c * T^d * H''. c={-1 at d=2, 2s at d=3, 4p-s^2 at d=4}.
#   Actually this only contributes when P_3 has that (w, d).
#
# I had this right. Let me recompute all e-contributions to δ=2:

# For each Riccati term, iterate e = 0, 1, 2 and find (w, d) contributing.
# X_data: (label, coefs of P_i, top_X, layer at e -> series generator)
# The layer e series for P_3 G'' is G^{[e]}'' (double derivative of layer e).

# Let me recompute all contributions symbolically to δ=2 equation:

print("\n--- Enumerating δ=2 contributions ---")

# Contributions structure: list of (P_dict, top_X, layer_at_e_func) with layer_at_e_func(e) returning
# a description like "(G^3)_e = 3H^2 L + 3 H K^2" for e=2 etc.

# Just list all valid (P_i, w, d, e) and expand what X_layer[e] represents.

terms = [
    ('P3_Gpp',   P3_coefs, 4, {0: "H''", 1: "K''", 2: "L''"}),
    ('P3_GGp',   P3_coefs, 5, {0: "H*H'", 1: "H*K' + K*H'", 2: "H*L' + K*K' + L*H'"}),  # * multiplier 3 (from 3 G G')
    ('P3_G3',    P3_coefs, 6, {0: "H^3", 1: "3 H^2 K", 2: "3 H^2 L + 3 H K^2"}),
    ('P2_Gp',    P2_coefs, 3, {0: "H'", 1: "K'", 2: "L'"}),
    ('P2_G2',    P2_coefs, 4, {0: "H^2", 1: "2 H K", 2: "2 H L + K^2"}),
    ('P1_G',     P1_coefs, 2, {0: "H", 1: "K", 2: "L"}),
]

for name, P_dict, top_X, layer_desc in terms:
    print(f"\nTerm {name} (top_X = {top_X}):")
    for (w, d), coef in sorted(P_dict.items()):
        e = w - d + top_X - 2
        if e in [0, 1, 2] and coef != 0:
            mult = 3 if name == 'P3_GGp' else 1
            print(f"  (w={w}, d={d}, coef={coef}), e={e}, contribution: T^{d} * ({coef}) * {mult} * ({layer_desc[e]})")
