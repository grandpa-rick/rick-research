"""Day 130 — Analyze top-weight expansions of Ψ(e_2^b), b = 2..6.

Data comes from Day 128 (task1_psi_e2_b5_b6.py). To be safe, we RECOMPUTE
using the corrected library, then look for closed forms.
"""

import sys, time, itertools, math
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import (reduce_y, falling, apply_S, apply_T_then_S,
                 antisym_orbit, tau_deg, top_tau,
                 s, y, t, u1, u2, u3)
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, list_top_weight_coeffs,
                                 e1_u, e2_u, e3_u, E1, E2, E3)

from sympy import (symbols, expand, Poly, Integer, S, prod, factor,
                    Rational, binomial, factorial, simplify)


def stirling2(n, k):
    """Stirling numbers of the second kind."""
    if n == 0 and k == 0:
        return 1
    if k == 0 or k > n:
        return 0
    # Explicit formula
    return sum((-1)**i * math.comb(k, i) * (k-i)**n for i in range(k+1)) // math.factorial(k)


def stirling1_unsigned(n, k):
    """Unsigned Stirling numbers of the first kind c(n,k)."""
    if n == 0 and k == 0:
        return 1
    if k == 0 or k > n:
        return 0
    # Recurrence: c(n,k) = c(n-1,k-1) + (n-1)*c(n-1,k)
    tbl = [[0]*(n+2) for _ in range(n+2)]
    tbl[0][0] = 1
    for nn in range(1, n+1):
        for kk in range(0, nn+1):
            tbl[nn][kk] = tbl[nn-1][kk-1] + (nn-1)*tbl[nn-1][kk] if kk > 0 else (nn-1)*tbl[nn-1][kk]
    return tbl[n][k]


def stirling1_signed(n, k):
    """Signed Stirling numbers of the first kind s(n,k) = (-1)^(n-k) c(n,k)."""
    return (-1)**(n-k) * stirling1_unsigned(n, k)


def main():
    print("Computing Psi(e_2^b) top-weight expansions for b=2..6 ...", flush=True)
    all_coeffs = {}  # {b: {(a1,a2,a3): coeff}}
    for b in range(2, 7):
        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        psi_e = sym_to_ebasis_direct(psi_u)
        tw_list = list_top_weight_coeffs(psi_e, b)
        all_coeffs[b] = {k: int(c) for k, c in tw_list}
        print(f"  b={b}: {len(tw_list)} monomials, "
              f"{sum(1 for _,c in tw_list if c != 0)} nonzero  "
              f"(t={time.time()-t0:.2f}s)", flush=True)

    # ----- Full table dump -----
    lines = []
    lines.append("=" * 78)
    lines.append("Top-weight expansions of Psi(e_2^b) in E-basis, b = 2..6")
    lines.append("(All monomials with i + j + 2k = b, i.e. weight b.)")
    lines.append("=" * 78)
    lines.append(f"{'b':>3} {'(a1,a2,a3)':>12}  {'coeff':>10}")
    lines.append("-" * 78)
    for b in range(2, 7):
        for k in range(b // 2 + 1):
            for j in range(b - 2*k + 1):
                i = b - 2*k - j
                c = all_coeffs[b].get((i, j, k), 0)
                lines.append(f"{b:>3} {str((i,j,k)):>12}  {int(c):>10}")
        lines.append("")
    print('\n'.join(lines))

    # ----- Pattern checks -----
    print("\n" + "=" * 78)
    print("Pattern checks")
    print("=" * 78)

    # 1) E1^b coefficient: (-1)^b * b!
    print("\n[1] Coefficient of E1^b:")
    for b in range(2, 7):
        c = all_coeffs[b][(b, 0, 0)]
        pred = (-1)**b * math.factorial(b)
        print(f"    b={b}: actual = {c:>8}, (-1)^b b! = {pred:>8}  "
              f"{'OK' if c == pred else 'MISMATCH'}")

    # 2) E2^b coefficient: 1
    print("\n[2] Coefficient of E2^b: expected 1")
    for b in range(2, 7):
        c = all_coeffs[b][(0, b, 0)]
        print(f"    b={b}: actual = {c}")

    # 3) E1^{b-1} E2 coefficient: Stirling-like?
    #    Values: b=2: -3, b=3: 11, b=4: -50, b=5: 274, b=6: -1764
    #    These are (-1)^{b-1} times: 3, 11, 50, 274, 1764
    #    Look up: 3, 11, 50, 274, 1764  -- OEIS A000670? No.
    #    A001705? Let's check c(b+1, 2) unsigned Stirling of first kind:
    #      c(3,2) = 3, c(4,2) = 11, c(5,2) = 50, c(6,2) = 274, c(7,2) = 1764. YES.
    print("\n[3] Coefficient of E1^{b-1} E2:")
    print("    Try: (-1)^{b-1} * c(b+1, 2)  [unsigned Stirling of 1st kind]")
    for b in range(2, 7):
        c = all_coeffs[b][(b-1, 1, 0)]
        pred = (-1)**(b-1) * stirling1_unsigned(b+1, 2)
        print(f"    b={b}: actual = {c:>8}, formula = {pred:>8}  "
              f"{'OK' if c == pred else 'MISMATCH'}")

    # 4) Generalize: E1^{b-j} E2^j coefficient (j=0..b, k=0)
    #    b=2, (2,0): 2; (1,1): -3; (0,2): 1
    #    b=3, (3,0): -6; (2,1): 11; (1,2): -6; (0,3): 1
    #    b=4, (4,0): 24; (3,1): -50; (2,2): 35; (1,3): -10; (0,4): 1
    #    b=5, (5,0): -120; (4,1): 274; (3,2): -225; (2,3): 85; (1,4): -15; (0,5): 1
    #    b=6, (6,0): 720; (5,1): -1764; (4,2): 1624; (3,3): -735; (2,4): 175; (1,5): -21; (0,6): 1
    #
    # Row for b=4: 24, -50, 35, -10, 1  --- signed
    # abs: 24, 50, 35, 10, 1 --- these look like Stirling1 numbers!
    # c(5,1)=24, c(5,2)=50, c(5,3)=35, c(5,4)=10, c(5,5)=1  --- YES! Row of c(b+1, k)
    # Check b=3: c(4,1)=6, c(4,2)=11, c(4,3)=6, c(4,4)=1  Actual: -6, 11, -6, 1  matches with sign (-1)^(b-j).
    # b=5: c(6,1)=120, c(6,2)=274, c(6,3)=225, c(6,4)=85, c(6,5)=15, c(6,6)=1  YES.
    # b=6: c(7,1)=720, c(7,2)=1764, c(7,3)=1624, c(7,4)=735, c(7,5)=175, c(7,6)=21, c(7,7)=1 YES.
    #
    # So coefficient of E1^{b-j} E2^j (k=0) = (-1)^{b-j} c(b+1, j+1)
    #    = s(b+1, j+1) * (-1)^{... check sign convention...}
    # s(b+1, j+1) = (-1)^{b-j} c(b+1, j+1). So coeff = s(b+1, j+1). Clean!
    print("\n[4] Coefficient of E1^{b-j} E2^j (k=0, j=0..b):")
    print("    Try: s(b+1, j+1)  [signed Stirling 1st kind]")
    for b in range(2, 7):
        for j in range(b+1):
            i = b - j
            c = all_coeffs[b].get((i, j, 0), 0)
            pred = stirling1_signed(b+1, j+1)
            status = 'OK' if c == pred else 'MISMATCH'
            print(f"    b={b}, j={j}: actual = {c:>8}, s({b+1},{j+1}) = {pred:>8}  {status}")

    # 5) k=1 row: (i, j, 1) with i + j = b - 2
    # b=2: (0,0,1): -3
    # b=3: (1,0,1): 25, (0,1,1): -9
    # b=4: (2,0,1): -190, (1,1,1): 118, (0,2,1): -18
    # b=5: (3,0,1): 1526, (2,1,1): -1260, (1,2,1): 340, (0,3,1): -30
    # b=6: (4,0,1): -13356, (3,1,1): 13276, (2,2,1): -4845, (1,3,1): 770, (0,4,1): -45
    #
    # Look at "leading" column (j=0): -3, 25, -190, 1526, -13356
    # abs: 3, 25, 190, 1526, 13356
    # Ratios: 25/3, 190/25=7.6, 1526/190=8.03, 13356/1526=8.75
    # Try c(b+2, 3)? c(4,3)=6, c(5,3)=35, c(6,3)=225 -- no.
    # Try to see if it matches -3 * something. 3=3, 25, 190, 1526, 13356.
    #   Divide by 3: 1, 25/3, ... not integer. So 3 isn't a factor.
    # OEIS: 3, 25, 190, 1526, 13356 ... let me check via formula
    #
    # Actually try (a1, 0, 1) = (b-2, 0, 1). Coeff = ?
    # Try: (-1)^(b-1) * something.
    # signs: b=2: -, b=3: +, b=4: -, b=5: +, b=6: -.  So (-1)^(b-1).
    # abs values: 3, 25, 190, 1526, 13356.  Differences? Try dividing by binomial(b+1, 2):
    #   b=2: 3/3=1
    #   b=3: 25/6 = 4.17
    #   b=4: 190/10 = 19
    #   b=5: 1526/15
    # Not obviously binomial.
    # Try Stirling S(?). Actually the "last" column (j = b-2) with k=1:
    # b=2: j=0: -3. b=3: j=1: -9. b=4: j=2: -18. b=5: j=3: -30. b=6: j=4: -45.
    # These are: -3, -9, -18, -30, -45.  Differences: -6, -9, -12, -15. Second diff: -3.
    # -3 * triangular?  -3 * C(b, 2)? C(2,2)=1: -3*1=-3 OK. C(3,2)=3: -9 OK.
    # C(4,2)=6: -18 OK. C(5,2)=10: -30 OK. C(6,2)=15: -45 OK. YES.
    # So coeff of E2^{b-2} E3 = -3 * C(b, 2) = -3 b(b-1)/2.
    print("\n[5a] Coefficient of E2^{b-2} E3 (i=0, k=1):")
    for b in range(2, 7):
        c = all_coeffs[b].get((0, b-2, 1), 0)
        pred = -3 * (b*(b-1)) // 2
        print(f"    b={b}: actual = {c:>6}, -3 C(b,2) = {pred:>6}  "
              f"{'OK' if c == pred else 'MISMATCH'}")

    # 5b) (b-2, 0, 1): -3, 25, -190, 1526, -13356
    # OEIS lookup 3, 25, 190, 1526, 13356... Not immediately recognizable.
    # Note: c(b+2, 4) = ? c(4,4)=1, c(5,4)=10, c(6,4)=85, c(7,4)=735, c(8,4)=6769.  Not it.
    # 3*Stirling1(b+1, 3)? c(3,3)=1, c(4,3)=6, c(5,3)=35, c(6,3)=225, c(7,3)=1624
    # 3*1=3 ok; 3*6=18 not 25. no.
    # Try: 3 * (something binomial). 3 = 3*1. 25 = ? 190 = ?
    # Maybe: (b-2, 0, 1) = 3 * c(b+1,3) + c(b+1, 2)?
    #  b=2: 3*1 + 3 = 6. Not 3.
    # Try: 3 * s(b+2, something)?
    # Let's just print for the record.
    print("\n[5b] Coefficient of E1^{b-2} E3 (j=0, k=1):")
    for b in range(2, 7):
        c = all_coeffs[b].get((b-2, 0, 1), 0)
        print(f"    b={b}: actual = {c}")

    # 6) Try: total-row-sum test: sum of all top-weight coeffs at value E1=E2=E3=1
    print("\n[6] Sum of ALL top-weight coefficients (set E1=E2=E3=1):")
    for b in range(2, 7):
        s_val = sum(all_coeffs[b].values())
        print(f"    b={b}: sum = {s_val}")

    # 7) Try: substituting E1=x, E2=E3=0 => just extract coefficient of E1^b:
    # already done. Try E2=x, others 0: coef of E2^b = 1.
    # Try E1=t, E2=t, E3=t^2 (all weight-1 -> in weight sense):
    # This is a weight-graded eval. Should give a polynomial in t of degree b.
    print("\n[7] Evaluate at E1=E2=t, E3=t^2:")
    for b in range(2, 7):
        val = sum(c * 1**a[0] * 1**a[1] * 1**a[2]
                  for a, c in all_coeffs[b].items())
        # This is same as sum. Try weighted eval:
        val2 = sum(c for a, c in all_coeffs[b].items())
        print(f"    b={b}: sum(all) = {val}")

    # 8) Try to find generating functions.
    # Let P_b(E1,E2,E3) = top-weight of Psi(e_2^b).
    # EGF: F(t) = sum_b P_b t^b / b!.  Does this factor?
    # Since coeff of E1^b in P_b is (-1)^b b!, coeff of E1^b in F is (-1)^b t^b,
    # so the E1-only part gives sum (-t E1)^b = 1/(1 + t E1).  Interesting.
    # Coeff of E2^b in P_b is 1, so E2-only part of F is sum (t E2)^b / b! = exp(t E2).
    # So maybe F(t) = exp(t E2) / (1 + t E1) * (something involving E3)?
    # Let's compute and see.
    print("\n[8] EGF candidate factorization: F(t) = exp(t E2) / (1 + t E1) * G(t, E1, E2, E3)")
    print("    Extracting G(t) up to t^6:")
    from sympy import Symbol, series, together, cancel
    tsym = Symbol('t_')
    F = Integer(0)
    for b in range(2, 7):
        Pb = sum(c * E1**a[0] * E2**a[1] * E3**a[2]
                 for a, c in all_coeffs[b].items())
        F += Pb * tsym**b / factorial(b)
    # Add lower b's to get proper EGF... but we don't have b=0, 1.
    # b=0: e_2^0 = 1, Psi(1) = something. Let's compute.
    psi0 = Psi_direct(Integer(1))
    psi0_e = sym_to_ebasis_direct(psi0)
    tw0 = top_weight_part(psi0_e, 0)
    print(f"    Psi(1) top-weight = {tw0}")
    psi1 = Psi_direct(e2_u)
    psi1_e = sym_to_ebasis_direct(psi1)
    tw1 = top_weight_part(psi1_e, 1)
    print(f"    Psi(e_2)^{{top}} = {tw1}")
    F0 = tw0
    F1 = tw1
    F = F0 + F1 * tsym + F
    print(f"    Full EGF (through t^6):")
    print(f"      {expand(F)}")

    # Try dividing F by exp(tsym * E2) / (1 + tsym * E1) formally.
    # Actually easier: since coefficient of E1^b in P_b is (-1)^b b!, and coeff of E2^b is 1,
    # try P_b(E1, E2, 0) — the k=0 part is  sum_{j} s(b+1, j+1) E1^{b-j} E2^j.
    # In terms of falling factorial:  sum_{j} s(b+1, j+1) E1^{b-j} E2^j.
    # Recall: (x)_{n} = sum_k s(n,k) x^k  -- falling factorial in x.
    # Consider F_0(t) = sum_b P_b(E1, E2, 0) t^b.
    # Coefficient at t^b of E1^{b-j} E2^j is s(b+1, j+1).
    # So we're building sum_b t^b * sum_j s(b+1, j+1) E1^{b-j} E2^j.
    # Let u = E1, v = E2. Then row for b is s(b+1, j+1) u^{b-j} v^j for j=0..b.
    # = sum_j s(b+1, j+1) u^{b-j} v^j
    # = u^b * sum_j s(b+1, j+1) (v/u)^j
    # From (x)_{b+1} = sum_{k=0}^{b+1} s(b+1, k) x^k, so sum_k s(b+1, k) x^k = (x)(x-1)...(x-b).
    # Setting k = j+1: sum_{j} s(b+1, j+1) x^{j+1} = (x)_{b+1}, so sum_j s(b+1, j+1) x^j = (x)_{b+1}/x = (x-1)(x-2)...(x-b) = (x-1)_{b}.
    # So P_b(E1, E2, 0) = E1^b * ((E2/E1 - 1)_b) = E1^b * (E2/E1 - 1)(E2/E1 - 2)...(E2/E1 - b)
    # = prod_{r=1}^{b} (E2 - r E1).
    print("\n[9] Predicted k=0 slice: P_b(E1, E2, 0) = prod_{r=1}^b (E2 - r*E1)")
    for b in range(2, 7):
        predicted = Integer(1)
        for r in range(1, b+1):
            predicted *= (E2 - r*E1)
        predicted = expand(predicted)
        actual_k0 = Integer(0)
        for (i,j,k), c in all_coeffs[b].items():
            if k == 0:
                actual_k0 += c * E1**i * E2**j
        actual_k0 = expand(actual_k0)
        diff = expand(actual_k0 - predicted)
        print(f"    b={b}: {'OK' if diff == 0 else 'MISMATCH (diff = ' + str(diff) + ')'}")

    # 10) Now look at k >= 1 corrections. Define Q_b = P_b - prod_{r=1}^b (E2 - r E1).
    # This should be divisible by E3.
    print("\n[10] Q_b := P_b - prod_r (E2 - r E1). Should be divisible by E3.")
    for b in range(2, 7):
        Pb = sum(c * E1**a[0] * E2**a[1] * E3**a[2]
                 for a, c in all_coeffs[b].items())
        prod_part = Integer(1)
        for r in range(1, b+1):
            prod_part *= (E2 - r*E1)
        Qb = expand(Pb - prod_part)
        # Check divisibility by E3
        Qb_poly = Poly(Qb, E3)
        low_coef = Qb_poly.coeff_monomial(E3**0) if Qb != 0 else 0
        print(f"    b={b}: Q_b/E3 = {expand(Qb / E3) if Qb != 0 else 0}")

    # 11) Now try:  P_b = prod_{r=1}^b (E2 - r E1) + E3 * R_b(E1, E2, E3)
    # Guess R_b has similar product form.
    # For b=2: Q_b / E3 = -3.  So R_2 = -3.
    # For b=3: Q_3 / E3 = 25 E1 - 9 E2.  Hmm.
    # For b=4: Q_4 / E3 = -190 E1^2 + 118 E1 E2 - 18 E2^2 + 27 E3.
    # For b=5: Q_5 / E3 = 1526 E1^3 - 1260 E1^2 E2 + 340 E1 E2^2 - 30 E2^3 - 615 E1 E3 + 135 E2 E3.
    # For b=6: Q_6 / E3 = -13356 E1^4 + 13276 E1^3 E2 - 4845 E1^2 E2^2 + 770 E1 E2^3 - 45 E2^4 + 10300 E1^2 E3 - 4095 E1 E2 E3 + 405 E2^2 E3 - 405 E3^2.
    # Look at the k=1 part of R_b (which is k=1 in Q_b, i.e., k=1 in P_b).
    # (b-2, 0, 1) values: -3, 25, -190, 1526, -13356 (for b=2,3,4,5,6).
    # (b-3, 1, 1) values: for b=3: -9; b=4: 118; b=5: -1260; b=6: 13276.
    # (b-4, 2, 1) values: b=4: -18; b=5: 340; b=6: -4845.
    # (b-5, 3, 1) values: b=5: -30; b=6: 770.
    # (b-6, 4, 1): b=6: -45.
    #
    # Corner: (0, b-2, 1) = -3*C(b,2) already established.
    #
    # Try: R_b(E1, E2, 0) = (E3 coefficient of P_b) is a polynomial in E1, E2 of weight b-2
    # (since E3 has weight 2).
    #
    # Look at R_b(E1, E2, 0):
    # b=2: -3
    # b=3: 25 E1 - 9 E2
    # b=4: -190 E1^2 + 118 E1 E2 - 18 E2^2
    # b=5: 1526 E1^3 - 1260 E1^2 E2 + 340 E1 E2^2 - 30 E2^3
    # b=6: -13356 E1^4 + 13276 E1^3 E2 - 4845 E1^2 E2^2 + 770 E1 E2^3 - 45 E2^4
    #
    # Note: -3 * C(b,2) is coeff of E2^{b-2}. And 3 * (- something) is coeff of E1^{b-2}.
    # Try to factor R_b(E1, E2, 0).
    print("\n[11] R_b := (E3-coefficient of P_b) as polynomial in E1, E2 alone:")
    for b in range(2, 7):
        Pb = sum(c * E1**a[0] * E2**a[1] * E3**a[2]
                 for a, c in all_coeffs[b].items())
        # E3-coefficient
        R = Integer(0)
        for a, c in all_coeffs[b].items():
            if a[2] == 1:
                R += c * E1**a[0] * E2**a[1]
        print(f"    b={b}: R_b(E1,E2,0) = {expand(R)}")
        print(f"           factored:    {factor(R)}")

    # 12) Try the "sum" pattern:
    # Consider substitution E1 = 0, E2 = something.  Look at what R_b is at E1 = 0:
    # b=2: -3, b=3: -9 E2, b=4: -18 E2^2, b=5: -30 E2^3, b=6: -45 E2^4.
    # = -3 C(b,2) E2^{b-2}.  So R_b(0, E2) = -3 * C(b,2) * E2^{b-2}.  Known.

    # Look at R_b(E1, 0):
    # b=2: -3
    # b=3: 25 E1
    # b=4: -190 E1^2
    # b=5: 1526 E1^3
    # b=6: -13356 E1^4
    # These are (-3, 25, -190, 1526, -13356). Try formula (-1)^{b-1} times {3, 25, 190, 1526, 13356}.
    # OEIS: Let me try dividing by successive... maybe binomial(b+2, 3)?
    # b=2: C(4,3)=4; b=3: C(5,3)=10; b=4: C(6,3)=20; b=5: C(7,3)=35; b=6: C(8,3)=56.
    # 3/4 = 0.75; 25/10 = 2.5; 190/20 = 9.5; 1526/35 = 43.6; 13356/56=238.5. No.
    # Try c(b+2, 3) [unsigned Stirling1]: c(4,3)=6, c(5,3)=35, c(6,3)=225, c(7,3)=1624, c(8,3)=13132.
    # Hmm 13356 vs 13132 close but no.
    # What about 3 * ?  Or via 3 = 3, 25 = 3 * 8 + 1 ...  Or generating function.
    # Consider e.g. R_b(E1, 0) / E1^{b-2}:  -3, 25, -190, 1526, -13356.
    # Let a_b = |R_b(E1,0)/E1^{b-2}|.  a_2=3, a_3=25, a_4=190, a_5=1526, a_6=13356.
    # Ratios: 25/3 ≈ 8.33, 190/25 = 7.6, 1526/190 ≈ 8.03, 13356/1526 ≈ 8.75. Growing but not smooth.
    # Try a_b / b!: 3/2=1.5, 25/6≈4.17, 190/24≈7.92, 1526/120≈12.72, 13356/720≈18.55.
    # Try a_b / (b+1)!: 3/6=0.5, 25/24, 190/120, ...
    # Try adding recurrence check:  maybe a_b = ?
    # Actually there's a cool observation: these might just be the k=1 slice of some
    # 3-Stirling / harmonic sum.
    # Let me compute (b-1) * c(b+2, 3) or similar:
    #   b=2: 1 * c(4,3) = 6. No.
    # Try summing Stirling1 * Stirling2:
    # 25 = ? c(5,3) = 35. c(5,2)=50. c(4,2)=11.
    #
    # Note also: 3, 25, 190 doesn't match anything super-canonical.  OK give up on closed form for now.
    print("\n[12] R_b(E1, 0) / E1^{b-2}:")
    vals = []
    for b in range(2, 7):
        Pb = sum(c * E1**a[0] * E2**a[1] * E3**a[2]
                 for a, c in all_coeffs[b].items())
        # E3 coeff, E2=0
        v = Integer(0)
        for a, c in all_coeffs[b].items():
            if a[2] == 1 and a[1] == 0:
                v = c  # only one term: (b-2, 0, 1)
        vals.append(v)
        print(f"    b={b}: {v}")
    print(f"    Sequence: {vals}")

    # 13) Compute OGF partial factorization attempt
    # Consider G(t) = sum_b P_b * t^b (OGF).
    # E1-only part: sum_b (-1)^b b! t^b E1^b -- factorial series, no rational closed form.
    # So OGF is not rational. Try EGF:
    # E1-only part: sum_b (-1)^b E1^b t^b = 1/(1 + t E1).
    # E2-only part: sum_b (E2 t)^b / b! = exp(t E2).
    # Reasonable guess: EGF(t) = something like  exp(tau(t)) / (1 + t E1)
    # where tau(t) has E2 and E3 terms.
    # But (E1, E2) mixed part is prod_{r=1}^b (E2 - r E1) / b!.  This is:
    #   sum_b t^b/b! * prod_{r=1}^b (E2 - r E1)
    # Let x = E2/E1 (so E2 - r E1 = E1 (x - r)).
    # sum_b (t E1)^b (x-1)(x-2)...(x-b) / b!
    # = sum_b (t E1)^b * (x-1)_b_falling / b!
    # where (x-1)_b_falling = prod_{r=1}^b (x - r).
    # Recall generating function: sum_n (x)_n t^n / n! = (1+t)^x for the FALLING factorial (x)_n
    # (with (x)_n = x(x-1)...(x-n+1)). Careful with conventions.
    # Here (x-1)_b_falling means (x-1)(x-2)...(x-b) = falling factorial of (x-1) length b? No.
    # (x-1)(x-2)...(x-b) with b factors — this is falling factorial (x-1)_{(b)} using the notation
    # (y)_{(b)} := y (y-1) ... (y-b+1).  We have y = x-1, so (y)_{(b)} = (x-1)(x-2)...(x-b). YES.
    # And sum_b y_{(b)} t^b / b! = (1+t)^y.  So the sum becomes:
    #   sum_b (t E1)^b (x-1)_{(b)} / b! = (1 + t E1)^{x - 1}
    # where x = E2/E1.  So:
    #   k=0 slice of EGF = (1 + t E1)^{E2/E1 - 1}
    # Wow. Let me double check by expanding:
    #   (1+u)^y = sum_n y_{(n)} u^n / n!  where u = t E1, y = E2/E1 - 1
    #   coeff of u^b: y(y-1)...(y-b+1) / b! = (E2/E1 - 1)(E2/E1 - 2) ... (E2/E1 - b) / b!
    #   times u^b = (t E1)^b, gives (t^b / b!) * prod_{r=1}^b (E2 - r E1).  YES.
    print("\n[13] Nice closed form for k=0 slice of EGF!")
    print("     EGF|_{E3=0} = (1 + t*E1)^(E2/E1 - 1)")
    print("     [Verified analytically above.]")

    # 14) Attempt full EGF factorization: EGF = (1 + t E1)^(E2/E1 - 1) * H(t, E1, E2, E3)
    # where H starts as 1 + O(t^2 E3) (since first E3 shows up at b=2).
    # Compute: EGF / (1 + t E1)^(E2/E1 - 1) truncated to low order.
    # This is hard to do symbolically. Let's just compute EGF and log it.
    print("\n[14] EGF coefficients (truncating):")
    from sympy import series
    # We have P_b for b=0..6.
    # P_0 = 1, P_1 = ? Compute Psi(e_2)|_top
    Pb_dict = {}
    for b in range(0, 7):
        if b == 0:
            Pb_dict[0] = Integer(1)  # Psi(1) top-weight (verify)
        else:
            psi_u = Psi_direct(e2_u**b) if b > 0 else Psi_direct(Integer(1))
            psi_e = sym_to_ebasis_direct(psi_u)
            Pb_dict[b] = top_weight_part(psi_e, b)
        print(f"    P_{b} = {Pb_dict[b]}")

    # 15) Verify: does P_b satisfy a recurrence?
    # For E1^{b-1} E2 coefficient, we have the Stirling s(b+1, 2), which satisfies
    #   s(b+1, 2) = -b! * H_b (harmonic number).
    # So coefficient of E1^{b-1} E2 = -b! H_b * sign. Actually c(b+1, 2) = b! H_b.
    print("\n[15] Coefficient of E1^{b-1} E2 = (-1)^{b-1} * b! * H_b:")
    from fractions import Fraction
    for b in range(2, 7):
        H = sum(Fraction(1, k) for k in range(1, b+1))
        pred = (-1)**(b-1) * math.factorial(b) * H
        c = all_coeffs[b][(b-1, 1, 0)]
        print(f"    b={b}: actual = {c}, b! H_b = {pred}, match = {pred == c}")

    # 16) Verify sign pattern in E3 direction.
    print("\n[16] Sign of leading E3-power coefficient (k=floor(b/2)):")
    # For even b, max k = b/2, monomial E3^(b/2), coeff:
    #   b=2: E3^1: -3
    #   b=4: E3^2: 27
    #   b=6: E3^3: -405
    # For odd b, max k = (b-1)/2, monomials with i+j=1:
    #   b=3: E1 E3, E2 E3 with coeffs 25, -9  (k=1 max)
    #   b=5: E1 E3^2, E2 E3^2 with coeffs -615, 135
    # -3, 27, -405: ratios 27/-3 = -9, -405/27 = -15. So pattern -3, -3*(-9), -3*(-9)*(-15).
    # -9 = -(2b-1) for b=4 (2b-1=7? no b=4: 2*4-1=7).  Try -3, -3*C, -3*C*C'...
    # -3 = -3, 27 = -3 * -9, -405 = -3 * -9 * -15.  Ratios: -9, -15.
    # These are -3(2j+1) style?  -9 = -3*3, -15 = -3*5.  So ratio at step j is -3(2j+1)?
    # -3 * (-3*3) * (-3*5) = -3 * -9 * -15 = -405. YES.
    # So Psi(e_2^{2j})|_{E3^j top} = -3 * prod_{i=1}^{j} (2i - 1)... let's check.
    # 2j = b even. Coeff of E3^{b/2} in P_b is:
    # b=2 (j=1): -3
    # b=4 (j=2): 27
    # b=6 (j=3): -405
    # Ratio -9 = ? at step 1->2. -15 at step 2->3.
    # -9 = -3 * 3, -15 = -3 * 5.
    # So a(j) = (-1)^j * 3^j * (odd double factorial)?
    # 3^1 * 1 = 3.  3^2 * 1*3 = 27. 3^3 * 1*3*5 = 27 * 15 = 405. YES!
    # a(j) = (-1)^j * 3^j * (2j-1)!!
    # Check: j=1: -3 * 1 = -3. j=2: 9 * 3 = 27. j=3: -27 * 15 = -405.  All match.
    print("    Even b=2j: coeff of E3^j = (-1)^j * 3^j * (2j-1)!!")
    for j in range(1, 4):
        b = 2*j
        c = all_coeffs[b].get((0, 0, j), 0)
        dfact = 1
        for r in range(1, 2*j, 2):
            dfact *= r
        pred = (-1)**j * 3**j * dfact
        print(f"    b={b}, j={j}: actual = {c}, pred = {pred}, "
              f"{'OK' if c == pred else 'MISMATCH'}")

    # 17) For odd b, leading E3-power is (b-1)/2, monomials with i+j=1.
    # b=3, j=1: (1,0,1): 25, (0,1,1): -9
    # b=5, j=2: (1,0,2): -615, (0,1,2): 135
    # Ratio (0,1,1)/(0,0,1)-analog: hmm.
    # (0,1,1)/((0,0,1) for even b analog): -9/-3 = 3, 135/27 = 5. So E2 coefficient
    # is 3, 5, ... at step j. These are (2j+1)!!/(2j-1)!! = 2j+1. So (0,1, j) = P_(2j)(0,0,j) * (2j+1)?
    # b=3=2*1+1: (0,1,1) = -9 = -3 * 3.  (E3^1 for b=2 is -3; times 3 gives -9). YES.
    # b=5=2*2+1: (0,1,2) = 135 = 27 * 5.  (E3^2 for b=4 is 27; times 5 gives 135.) YES.
    #
    # So Psi(e_2^{2j+1})|_{E2 E3^j} = Psi(e_2^{2j})|_{E3^j} * (2j+1) = (-1)^j 3^j (2j-1)!! (2j+1)
    # = (-1)^j 3^j (2j+1)!!
    print("\n[17] Odd b=2j+1: coeff of E2 E3^j = (-1)^j * 3^j * (2j+1)!!")
    for j in range(1, 3):
        b = 2*j + 1
        c = all_coeffs[b].get((0, 1, j), 0)
        dfact = 1
        for r in range(1, 2*j+2, 2):
            dfact *= r
        pred = (-1)**j * 3**j * dfact
        print(f"    b={b}, j={j}: actual = {c}, pred = {pred}, "
              f"{'OK' if c == pred else 'MISMATCH'}")

    # Also check E1 E3^j coefficient for odd b:
    # b=3: (1,0,1): 25. b=5: (1,0,2): -615. Ratio -615/25 = -24.6. Hmm.
    # b=3 -> 25. Try  ???
    # 25 = ?  -615 = ?
    print("\n[17b] Odd b=2j+1: coeff of E1 * E3^j:")
    for j in range(1, 3):
        b = 2*j + 1
        c = all_coeffs[b].get((1, 0, j), 0)
        print(f"    b={b}, j={j}: actual = {c}")

    # Save table
    with open('/home/agent/projects/beta-prime/code/day130/coefficients_table.txt', 'w') as f:
        f.write("Top-weight coefficients of Psi(e_2^b) in E-basis, b = 2..6\n")
        f.write("Monomials: E1^a1 E2^a2 E3^a3 with a1 + a2 + 2*a3 = b\n")
        f.write("=" * 60 + "\n")
        f.write(f"{'b':>3} {'a1':>4} {'a2':>4} {'a3':>4}  {'coeff':>10}\n")
        f.write("-" * 60 + "\n")
        for b in range(2, 7):
            for k in range(b // 2 + 1):
                for j in range(b - 2*k + 1):
                    i = b - 2*k - j
                    c = all_coeffs[b].get((i, j, k), 0)
                    f.write(f"{b:>3} {i:>4} {j:>4} {k:>4}  {c:>10}\n")
            f.write("\n")

    print("\nSaved coefficients_table.txt")


if __name__ == '__main__':
    main()
