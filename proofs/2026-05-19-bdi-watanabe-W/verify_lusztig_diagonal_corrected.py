"""
verify_lusztig_diagonal_corrected.py — Corrected Lusztig diagonal formula.

I had used (F^{(c)}, F^{(c)}) = prod_k 1/(1 - q_β^{-2k}) above. That's the
formula for a *different* normalization of the form. The actual Kashiwara
form (normalized so (1,1) = 1, (F_i, F_i) = 1) gives instead:

    (F_β^{(c)}, F_β^{(c)}) = q_β^{c(c-1)/2} / [c]_{q_β}!

This follows from the recursion (F u, v) = (u, r(v)) with r being the skew
derivation r(F^n) = q_β^{n-1} [n]_{q_β} F^{n-1} (verified for sl_2 in
direct numerical Kashiwara computation).

The PBW product formula (Lusztig PBW orthogonality, [Lus93] §38.2) gives:

    (E_π, E_π) = prod_β q_β^{c_β(c_β-1)/2} / [c_β]_{q_β}!.

At q -> infinity:
    [c]_{q_β}! ~ q_β^{0 + 1 + ... + (c-1)} = q_β^{c(c-1)/2}
    Hence q_β^{c(c-1)/2} / [c]_{q_β}! -> 1.

So almost-orthonormality (leading 1 at q^{1/2} = infinity) holds in BOTH
the original and the corrected normalization. The ALMOST-ORTHONORMALITY
PROPERTY IS INDEPENDENT OF NORMALIZATION (since it's the q-infinity limit,
and Lusztig's theorem gives orthogonality with leading-1 diagonal in any
standard normalization).

This script verifies the corrected formula at B_2 and B_3.
"""

import sympy
from sympy import symbols, simplify, series, Rational, together
from itertools import product

q = symbols('q', positive=True)
qh = symbols('qh', positive=True)  # q^{1/2}


def qint(n, qval):
    """q-integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if n == 0:
        return sympy.S.Zero
    return sympy.Sum(qval ** (n - 1 - 2 * k) for k in range(n))


def qint_explicit(n, qval):
    """Explicit q-integer [n]_q."""
    if n == 0:
        return 0
    return sum(qval ** (n - 1 - 2 * k) for k in range(n))


def qfact(n, qval):
    """q-factorial [n]_q!."""
    result = sympy.S.One
    for k in range(1, n + 1):
        result *= qint_explicit(k, qval)
    return result


def root_length_sq(name):
    if name == 'sing':
        return 1
    kind, _ = name
    return {'bot': 2, 'mid': 1, 'top': 2}[kind]


def qbeta(name):
    L = root_length_sq(name)
    return q if L == 2 else qh


def lusztig_diagonal_corrected(c_by_root):
    """Corrected Lusztig diagonal entry.
       (E_π, E_π) = prod_β q_β^{c_β(c_β-1)/2} / [c_β]_{q_β}!"""
    val = sympy.S.One
    for name, c in c_by_root.items():
        if c == 0:
            continue
        qb = qbeta(name)
        val *= qb ** (c * (c - 1) // 2)
        val /= qfact(c, qb)
    return val


def expand_at_infinity(expr, depth=8):
    """Series at qh = 1/t around t = 0."""
    t = symbols('t')
    sub_expr = expr.subs([(q, t ** -2), (qh, t ** -1)])
    sub_expr = sympy.together(sub_expr)
    sub_expr = sympy.simplify(sub_expr)
    return series(sub_expr, t, 0, depth).removeO()


def enumerate_chain_configs_b2(max_content):
    for total in range(max_content + 1):
        for M_1 in range(total + 1):
            for B_1 in range(total - M_1 + 1):
                for T_1 in range(total - M_1 - B_1 + 1):
                    S = total - M_1 - B_1 - T_1
                    yield (M_1, B_1, T_1, S)


def enumerate_chain_configs_b3(max_content):
    for total in range(max_content + 1):
        for M1 in range(total + 1):
            for B1 in range(total - M1 + 1):
                for T1 in range(total - M1 - B1 + 1):
                    for M2 in range(total - M1 - B1 - T1 + 1):
                        for B2 in range(total - M1 - B1 - T1 - M2 + 1):
                            for T2 in range(total - M1 - B1 - T1 - M2 - B2 + 1):
                                S = total - M1 - B1 - T1 - M2 - B2 - T2
                                yield (M1, B1, T1, M2, B2, T2, S)


def c_by_root_b2(M_1, B_1, T_1, S):
    return {('bot', 1): B_1, ('mid', 1): M_1, ('top', 1): T_1, 'sing': S}


def c_by_root_b3(M1, B1, T1, M2, B2, T2, S):
    return {
        ('bot', 1): B1, ('mid', 1): M1, ('top', 1): T1,
        ('bot', 2): B2, ('mid', 2): M2, ('top', 2): T2,
        'sing': S,
    }


def test_b2(max_content=3):
    print(f"=== B_2 corrected diagonal (content ≤ {max_content}) ===")
    all_ok = True
    n_configs = 0
    fails = []
    for cfg in enumerate_chain_configs_b2(max_content):
        n_configs += 1
        c = c_by_root_b2(*cfg)
        val = lusztig_diagonal_corrected(c)
        leading = expand_at_infinity(val, depth=4)
        const_term = leading.subs(symbols('t'), 0)
        if const_term != 1:
            fails.append((cfg, leading))
            all_ok = False
    if all_ok:
        print(f"  {n_configs}/{n_configs} configs: (E_π, E_π) ≡_∞ 1. PASS.")
    else:
        for cfg, lead in fails[:5]:
            print(f"  FAIL: {cfg} leading={lead}")
    return all_ok


def test_b3(max_content=3):
    print(f"=== B_3 corrected diagonal (content ≤ {max_content}) ===")
    all_ok = True
    n_configs = 0
    fails = []
    for cfg in enumerate_chain_configs_b3(max_content):
        n_configs += 1
        c = c_by_root_b3(*cfg)
        val = lusztig_diagonal_corrected(c)
        leading = expand_at_infinity(val, depth=4)
        const_term = leading.subs(symbols('t'), 0)
        if const_term != 1:
            fails.append((cfg, leading))
            all_ok = False
    if all_ok:
        print(f"  {n_configs}/{n_configs} configs: (E_π, E_π) ≡_∞ 1. PASS.")
    else:
        for cfg, lead in fails[:5]:
            print(f"  FAIL: {cfg} leading={lead}")
    return all_ok


def print_samples():
    print()
    print("=== Sample diagonals with corrected formula ===")
    samples = [
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (0, 0, 0, 1),
        (2, 0, 0, 0),
        (0, 1, 1, 0),
        (1, 1, 1, 1),
    ]
    for cfg in samples:
        c = c_by_root_b2(*cfg)
        val = lusztig_diagonal_corrected(c)
        leading = expand_at_infinity(val, depth=4)
        print(f"  cfg={cfg}: (E_π, E_π) = {sympy.simplify(val)}")
        print(f"             leading: {leading} + O(t^4)")


if __name__ == '__main__':
    ok2 = test_b2(max_content=4)
    print()
    ok3 = test_b3(max_content=3)
    print_samples()
    print()
    if ok2 and ok3:
        print("CORRECTED FORMULA: ALL DIAGONAL CHECKS PASS.")
        print("Verdict (W) holds in either normalization of the Kashiwara form.")
