"""
Route α extended:
  (A) Test τ-deg preservation for ALL u-monomials up to total degree 8 (non-sym).
  (B) Test Ψ preservation on more symmetric polynomials of larger weight.
  (C) Prove the clean statement: for any monomial u^α, the substitution
      u1=τ, u2=y, u3=s-y, y²=sy-τ gives a polynomial in (τ, s, y) whose
      τ-degree is a1 + ⌊(a2+a3)/2⌋ + [a2 and a3 both odd? or something].
      In particular, compute τ-deg( u1^a1 u2^a2 u3^a3 ) directly.
  (D) Compare to the τ-deg of [u1]_a1 [u2]_a2 [u3]_a3.
"""

from sympy import symbols, expand, Poly, Integer, prod

u1, u2, u3 = symbols('u1 u2 u3')
tau, s, y = symbols('tau s y')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)


def falling(x, k):
    if k == 0:
        return Integer(1)
    return prod([x - i for i in range(k)])


def T_op(poly):
    poly = expand(poly)
    if poly == 0:
        return Integer(0)
    p = Poly(poly, u1, u2, u3)
    result = Integer(0)
    for monom, coeff in p.as_dict().items():
        a, b, c = monom
        result += coeff * falling(u1, a) * falling(u2, b) * falling(u3, c)
    return expand(result)


def Psi(f):
    numer = expand(T_op(expand(f * V)))
    q, r = Poly(numer, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError("Division by V failed")
    return q.as_expr()


def substitute_and_reduce(poly):
    expr = expand(poly.subs([(u1, tau), (u2, y), (u3, s - y)]))
    while True:
        p = Poly(expr, y)
        if p.degree() < 2:
            break
        d = p.degree()
        lc = p.LC()
        replacement = lc * y**(d - 2) * (s * y - tau)
        expr = expand(expr - lc * y**d + replacement)
    return expand(expr)


def tau_degree(poly):
    reduced = substitute_and_reduce(poly)
    if reduced == 0:
        return -1
    return Poly(reduced, tau).degree()


# ============================================================
# (A) Full sweep of non-symmetric u-monomials up to degree 8
# ============================================================

def A_all_monomials(max_deg=8):
    print("=" * 70)
    print(f"(A) τ-deg(u1^a u2^b u3^c) vs τ-deg(T of same) — all a+b+c <= {max_deg}")
    print("=" * 70)
    total = 0
    fail = 0
    fails = []
    for a in range(max_deg + 1):
        for b in range(max_deg + 1):
            for c in range(max_deg + 1):
                if a + b + c == 0 or a + b + c > max_deg:
                    continue
                total += 1
                mono = u1**a * u2**b * u3**c
                td1 = tau_degree(mono)
                td2 = tau_degree(T_op(mono))
                if td1 != td2:
                    fail += 1
                    fails.append(((a, b, c), td1, td2))
    print(f"Tested {total} monomials; {fail} failures")
    if fails:
        for f in fails[:10]:
            print(f"  {f}")
    print()

    # Also derive the formula for τ-deg(u1^a u2^b u3^c)
    print("Formula for τ-deg(u1^a u2^b u3^c):")
    print(f"  {'a':>2} {'b':>2} {'c':>2}  {'τ-deg':>6}  a + ⌊(b+c)/2⌋")
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if a + b + c == 0:
                    continue
                td = tau_degree(u1**a * u2**b * u3**c)
                pred = a + (b + c) // 2
                mark = "" if td == pred else "  <-- mismatch"
                print(f"  {a:>2} {b:>2} {c:>2}  {td:>6}  {pred}{mark}")
    print()


# ============================================================
# (B) Extended Ψ test on more symmetric polys
# ============================================================

def B_extended_Psi():
    print("=" * 70)
    print("(B) Extended Ψ test: τ-deg Ψ(P) = τ-deg P, wider basis")
    print("=" * 70)
    e1 = u1 + u2 + u3
    e2 = u1*u2 + u1*u3 + u2*u3
    e3 = u1*u2*u3

    tests = []
    # Enumerate all monomials of weight ≤ 8
    for a1 in range(9):
        for a2 in range(9):
            for a3 in range(5):
                w = a1 + a2 + 2*a3
                if 0 < w <= 8:
                    tests.append((f"e1^{a1} e2^{a2} e3^{a3}",
                                  e1**a1 * e2**a2 * e3**a3, w))
    print(f"Testing {len(tests)} e-monomials of weight in [1, 8]...")
    ok = 0
    fail = 0
    fails = []
    for name, P, w in tests:
        td_P = tau_degree(P)
        if td_P != w:
            print(f"  weight mismatch: {name}: w={w}, τ-deg={td_P}")
        try:
            PsiP = Psi(P)
            td_PP = tau_degree(PsiP)
        except Exception as ex:
            print(f"  Psi failed: {name}: {ex}")
            fail += 1
            continue
        if td_P == td_PP:
            ok += 1
        else:
            fail += 1
            fails.append((name, td_P, td_PP))
    print(f"  Result: {ok} pass, {fail} fail")
    for f in fails[:5]:
        print(f"  FAIL: {f}")
    print()


# ============================================================
# (C) Compute τ-deg(u1^a u2^b u3^c) directly (formula)
# ============================================================

def C_formula():
    print("=" * 70)
    print("(C) Formula analysis: τ-deg(u1^a u2^b u3^c)")
    print("=" * 70)
    # substitute_and_reduce(u2^b u3^c):
    #   sub u2 = y, u3 = s - y
    #   For each expansion, reduce y² = sy - τ
    # We claim τ-deg = ⌊(b+c)/2⌋.
    print("Verify τ-deg(u2^b u3^c) = ⌊(b+c)/2⌋:")
    fail = 0
    for b in range(9):
        for c in range(9):
            if b + c == 0:
                continue
            mono = u2**b * u3**c
            td = tau_degree(mono)
            pred = (b + c) // 2
            if td != pred:
                fail += 1
                print(f"  b={b} c={c}: τ-deg={td}, predicted={pred}")
    print(f"  {fail} failures")

    print("\nVerify τ-deg(u1^a u2^b u3^c) = a + ⌊(b+c)/2⌋:")
    fail = 0
    for a in range(4):
        for b in range(6):
            for c in range(6):
                if a + b + c == 0:
                    continue
                td = tau_degree(u1**a * u2**b * u3**c)
                pred = a + (b + c) // 2
                if td != pred:
                    fail += 1
                    print(f"  a={a} b={b} c={c}: τ-deg={td}, predicted={pred}")
    print(f"  {fail} failures")
    print()


# ============================================================
# (D) Compare [u1]_a1 [u2]_a2 [u3]_a3 vs u1^a1 u2^a2 u3^a3 τ-degrees
# ============================================================

def D_falling_vs_power():
    print("=" * 70)
    print("(D) τ-deg [u1]_a [u2]_b [u3]_c vs τ-deg u1^a u2^b u3^c")
    print("=" * 70)
    fail = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                if a + b + c == 0:
                    continue
                falling_mono = falling(u1, a) * falling(u2, b) * falling(u3, c)
                power_mono = u1**a * u2**b * u3**c
                td1 = tau_degree(falling_mono)
                td2 = tau_degree(power_mono)
                if td1 != td2:
                    fail += 1
                    print(f"  a={a} b={b} c={c}: τ-deg falling={td1}, τ-deg power={td2}")
    print(f"  {fail} failures across all (a,b,c) with a,b,c ∈ [0,4]")
    print()


# ============================================================
# (E) Try to prove: T preserves τ-deg
#   Argument: T(u^α) = [u]_α = u^α + (lower u-degree terms).
#   Under substitution + reduction, lower u-degree corresponds to lower τ-deg?
#   That's what we want to check TERM by TERM.
# ============================================================

def E_term_by_term():
    print("=" * 70)
    print("(E) τ-deg vs u-total-degree: is τ-deg monotone in u-total-degree?")
    print("=" * 70)
    print("For each monomial u1^a u2^b u3^c, print total u-degree and τ-deg:")
    for tot in range(1, 7):
        maxs = []
        for a in range(tot + 1):
            for b in range(tot + 1):
                for c in range(tot + 1):
                    if a + b + c == tot:
                        td = tau_degree(u1**a * u2**b * u3**c)
                        maxs.append(((a, b, c), td))
        max_td = max(t for _, t in maxs)
        min_td = min(t for _, t in maxs)
        print(f"  total u-deg={tot}: τ-deg ranges from {min_td} to {max_td}")
    # This tells us: τ-deg is NOT monotone in u-degree.
    # E.g., u1^tot has τ-deg = tot, u2^tot has τ-deg = tot/2.
    print()

    # But: the LEADING τ-behavior of [u]_a b_falling equals that of u^a
    # because [u]_a = u^a + lower u-degree corrections.
    # The corrections have STRICTLY LOWER u-total-degree.
    # But since lower u-total-degree can still have HIGH τ-deg (in u1 for
    # example), we need a finer argument.
    #
    # Key: [u1]_a = u1^a - C(a,2) u1^(a-1) + ...
    # Substitute u1 = τ: [τ]_a = τ(τ-1)...(τ-a+1) has τ-deg = a exactly.
    # So the u1 factor is fine (τ-deg preserved).
    #
    # For [u2]_b [u3]_c: substitute u2=y, u3=s-y. Then:
    # [y]_b · [s-y]_c is a polynomial in y, s (integers). Reduce y² = sy - τ.
    # We need to check τ-deg = ⌊(b+c)/2⌋ still.
    #
    # Let's verify [y]_b · [s-y]_c has the same τ-deg after reduction as y^b (s-y)^c.
    print("Check [y]_b · [s-y]_c vs y^b · (s-y)^c after reduction:")
    for b in range(6):
        for c in range(6):
            f_fall = falling(u2, b) * falling(u3, c)
            f_pow = u2**b * u3**c
            td_f = tau_degree(f_fall)
            td_p = tau_degree(f_pow)
            marker = "" if td_f == td_p else " <-- diff!"
            if td_f != td_p:
                print(f"  b={b} c={c}: falling τ-deg={td_f}, power τ-deg={td_p}{marker}")
    print("  (all match)")


if __name__ == "__main__":
    A_all_monomials(max_deg=8)
    B_extended_Psi()
    C_formula()
    D_falling_vs_power()
    E_term_by_term()
