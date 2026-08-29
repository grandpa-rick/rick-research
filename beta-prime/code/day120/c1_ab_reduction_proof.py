"""Final verification: W_{k_2, k_3} = 0, and the full identity via the (A, B) reduction."""
import sympy as sp
from sympy import symbols, expand, Poly, Integer

t = symbols('t')

def AB_recursion(k, j_val):
    """Compute (A_k, B_k) via recursion: A_{k+1} = (j - k) A_k + B_k, B_{k+1} = -t A_k - k B_k."""
    A = [Integer(0)]
    B = [Integer(1)]
    for a in range(k):
        A_next = expand((j_val - a) * A[a] + B[a])
        B_next = expand(-t * A[a] - a * B[a])
        A.append(A_next)
        B.append(B_next)
    return A, B

def W(a, b, A, B):
    return expand(A[a] * B[b] - A[b] * B[a])

def fall_t(k):
    p = Integer(1)
    for i in range(k):
        p *= (t - i)
    return expand(p)

# Verify for various (l, m) that:
# 1. W_{k_2, k_3} = 0
# 2. F_mu = ([t]_{k_3} W_{k_1, k_2} - [t]_{k_2} W_{k_1, k_3}) / (t(t-2l))
# 3. [t^{d_mu}] F_mu = (-1)^m if m=l else 0

for l_val in range(1, 5):
    j_val = 2*l_val + 1
    k_max = 2*l_val + 4  # need A_k up to k_1 = 2l+3
    A, B = AB_recursion(k_max, j_val)
    print(f"\nl={l_val}, j={j_val}:")
    for m_val in range(l_val + 1):
        k1 = 2*l_val + 3
        k2 = l_val + 2 + m_val
        k3 = l_val - m_val
        W_23 = W(k2, k3, A, B)
        W_13 = W(k1, k3, A, B)
        W_12 = W(k1, k2, A, B)
        N_mu = expand(fall_t(k3) * W_12 - fall_t(k2) * W_13)
        # Check: N_mu / (t(t-2l)) should be polynomial F_mu
        divisor = expand(t * (t - 2*l_val))
        Fpoly, r = sp.div(Poly(N_mu, t), Poly(divisor, t))
        if r.as_expr() != 0:
            print(f"  m={m_val}: DIVISION FAILED. remainder = {r.as_expr()}")
            continue
        F = Fpoly.as_expr()
        d_mu = k1 - 2 + (k2 - 1 + k3) // 2  # = mu_1 + (mu_2 + mu_3)/2
        # verify d_mu = 3l+1
        d_mu_true = 3*l_val + 1
        F_t = Poly(F, t)
        top_coef = F_t.nth(d_mu_true)
        expected = ((-1)**m_val) if m_val == l_val else 0
        match = "OK" if top_coef == expected else "MISMATCH"
        W23_zero = "OK" if W_23 == 0 else "NONZERO"
        print(f"  m={m_val}, k=({k1},{k2},{k3}): W_{{k2,k3}}={W_23} [{W23_zero}], [t^{d_mu_true}]F={top_coef} vs {expected} [{match}]")
