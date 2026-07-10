"""Day 87 - Structural v_2 analysis of H_5 and H_4.

Goal:
  1. Establish lower bound v_2(H_5(a,b,j)) >= 3 by term-wise analysis.
  2. Verify upper bound: v_2(H_5(3,0,2)) = 3.
  3. Build H_4(a,b,j) via c-uniform template inversion (Day 86).
  4. Establish lower bound v_2(H_4) >= 4 term-wise.
  5. Verify upper bound: exhibit (a,b,j) with v_2(H_4) = 4.
  6. Conclude Delta beta'(5) = -1 structurally.

Rick, Day 87.
"""
from math import factorial
from fractions import Fraction
from collections import Counter, defaultdict


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def C(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


# ------------------------------------------------------------
# Clio's explicit H_5 polynomial (nine h_k coefficients)
# ------------------------------------------------------------
def h5_coeffs(a, b):
    """Return the 9 coefficients h_0..h_8 of Clio's H_5(a,b,j)."""
    return [
        (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5),          # h_0
        -20*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4),                   # h_1
        -10*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 22),          # h_2
        360*(a+3)*(b+2)*(a*b + a + 2*b - 2),                       # h_3
        240*(a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a + 2*b*b - 34*b - 24),  # h_4
        -7200*(a*b + b - 2),                                       # h_5
        -7200*(a*b - a - 6),                                       # h_6
        100800,                                                    # h_7
        201600,                                                    # h_8
    ]


def H5(a, b, j):
    hs = h5_coeffs(a, b)
    return sum(hs[k] * C(j, k) for k in range(9))


# ------------------------------------------------------------
# H_4(a,b,j) via c-uniform template inversion
# uses P_j closed forms from Day 86 (Q_j at c=4)
# ------------------------------------------------------------

# P_j closed forms in (a, b, c) from Day 86.  Q_j = M_j * (n)_{2j} / f^lam.
# Given: M_j(a,b,c) = P_j(a,b,c) * f^(a,b,c) / (n)_{2j}, and Clio's template:
# (a-c+2)(b-c+1) H_c(a,b,j) * C(N,b-j) * (a-b+1)
#    = c! (a+c+1-j) prod_i (b+i-j) M_j  +  C(N,b-j)(a-b+1) * (2c)! C(j,2c)
# where N = a+b+c-2j.
#
# So H_c = numerator / [(a-c+2)(b-c+1) C(N,b-j)(a-b+1)]
# with numerator = c! (a+c+1-j) prod_i (b+i-j) M_j + (2c)! C(j,2c) C(N,b-j) (a-b+1)
#
# For computation, we set c=4 and use the Day-86 P_j(a,b,c) formulas.

def hook_length_lambda_abc(a, b, c):
    """f^lambda where lambda = (a+2, b+1, c) (3-row partition with row lengths).
    Actually lambda = (a, b, c) but Clio's convention shifts."""
    # For lam = (a, b, c) with a >= b >= c > 0
    lam = (a, b, c)
    n = a + b + c
    if a < b or b < c or c < 0:
        return 0
    # Hook lengths
    cols = [0] * a
    for i, li in enumerate(lam):
        for j in range(li):
            cols[j] += 1
    hooks = 1
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = cols[j] - i - 1
            hooks *= (arm + leg + 1)
    return factorial(n) // hooks


def falling_int(x, k):
    """x * (x-1) * ... * (x-k+1), integer version."""
    p = 1
    for i in range(k):
        p *= (x - i)
    return p


def M_j_sym(a, b, c, j):
    """M_j(a,b,c) via Sym-side formula.
    M_j = <s_(a,b,c), e_2^j p_1^{n-2j}>
        = sum_{mu |- 2j, <=3 rows} K_{mu^T,(2^j)} * f^{lam/mu}
    Uses Aitken determinant for f^{lam/mu}.
    """
    tables = {
        0: [((0, 0, 0), 1)],
        1: [((1, 1, 0), 1)],
        2: [((2, 2, 0), 1), ((2, 1, 1), 1)],
        3: [((3, 3, 0), 1), ((3, 2, 1), 2), ((2, 2, 2), 1)],
        4: [((4, 4, 0), 1), ((4, 3, 1), 3), ((4, 2, 2), 2), ((3, 3, 2), 3)],
        5: [((5, 5, 0), 1), ((5, 4, 1), 4), ((5, 3, 2), 5), ((4, 4, 2), 6),
            ((4, 3, 3), 5)],
        6: [((6,6,0),1), ((6,5,1),5), ((6,4,2),9), ((5,5,2),10), ((6,3,3),5),
            ((5,4,3),21), ((4,4,4),5)],
    }
    if j == 0:
        return hook_length_lambda_abc(a, b, c) if (a >= b >= c) else 0
    if j not in tables:
        raise ValueError(f"j={j} not tabulated")
    # xs = (a+2, b+1, c), ks_j depend on mu
    xs = (a + 2, b + 1, c)
    if any(x < 0 for x in xs):
        return 0
    n = a + b + c
    if n < 2 * j:
        return 0
    total = Fraction(0)
    for mu, k in tables[j]:
        ks = [mu[jj] + (2 - jj) for jj in range(3)]
        # Determinant of falling(xs[i], ks[jj]) for f^{lam/mu} rows/cols
        # f^{lam/mu} = (n-|mu|)! * det( 1/(lam_i - mu_j - i + j)! )
        # With prefactor 1/((a+2)! (b+1)! c!), the entries become
        # falling(xs[i], ks[jj]) / xs[i]!
        # so f^{lam/mu} = (n - 2j)! * det(falling(xs[i], ks[jj])) / ((a+2)!(b+1)!c!)
        M = [[falling_int(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        # Compute 3x3 determinant
        det = (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
             - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
             + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))
        f_lam_mu_num = factorial(n - 2*j) * det
        f_lam_mu_den = factorial(a+2) * factorial(b+1) * factorial(c)
        total += Fraction(k * f_lam_mu_num, f_lam_mu_den)
    assert total.denominator == 1, f"M_{j}({a},{b},{c}) not integer: {total}"
    return int(total)


def H_c_via_template(a, b, c, j):
    """Reconstruct H_c(a,b,j) via Clio's Lemma-1 template inversion.
    Requires a>=b>=c, and gives an integer H_c (for valid parities).
    """
    N = a + b + c - 2*j
    Mj = M_j_sym(a, b, c, j)
    # numerator = c! (a+c+1-j) prod_i (b+i-j) M_j
    # denominator = C(N, b-j) (a-b+1) (a-c+2) (b-c+1)
    # Then H_c = (numerator/denominator + (2c)! C(j,2c)) / [(a-c+2)(b-c+1)]
    # Hmm actually the template gives:
    # (a-c+2)(b-c+1) H_c * C(N,b-j) (a-b+1) = c! (a+c+1-j) prod (b+i-j) M_j
    #                                        + C(N,b-j)(a-b+1) (2c)! C(j,2c)
    # So H_c = [c! (a+c+1-j) prod (b+i-j) M_j / (C(N,b-j)(a-b+1)) + (2c)! C(j,2c)]
    #          / [(a-c+2)(b-c+1)]
    if b - j < 0:
        return None  # C(N, b-j) undefined
    if N < 0 or (b - j) > N:
        return None
    prod_bij = 1
    for i in range(1, c+1):
        prod_bij *= (b + i - j)
    CNbj = C(N, b - j)
    numer1_num = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    numer1_den = CNbj * (a - b + 1)
    if numer1_den == 0:
        return None
    if numer1_num % numer1_den != 0:
        # Not integer at this point but might be after full simplification
        # Use Fraction
        f = Fraction(numer1_num, numer1_den) + factorial(2*c) * C(j, 2*c)
        h = f / Fraction((a - c + 2) * (b - c + 1))
        if h.denominator == 1:
            return int(h)
        return None
    val = numer1_num // numer1_den + factorial(2*c) * C(j, 2*c)
    denom = (a - c + 2) * (b - c + 1)
    if denom == 0:
        return None
    if val % denom != 0:
        return None
    return val // denom


# ------------------------------------------------------------
# Sanity check: H5_via_template vs Clio's explicit H_5
# ------------------------------------------------------------
def sanity_h5():
    print("=" * 60)
    print("Sanity: H_c_via_template vs Clio's explicit H_5")
    print("=" * 60)
    passes = 0
    total = 0
    fails = []
    for a in range(5, 15):
        for b in range(5, min(a, 15) + 1):
            for j in range(0, 7):
                clio = H5(a, b, j)
                tmpl = H_c_via_template(a, b, 5, j)
                total += 1
                if tmpl is None:
                    continue
                if tmpl == clio:
                    passes += 1
                else:
                    fails.append((a, b, j, clio, tmpl))
    print(f"  {passes}/{total} matches")
    for f in fails[:5]:
        print(f"    MISMATCH {f}")


# ------------------------------------------------------------
# Empirical brute-force min v_2(H_c(a,b,j))
# ------------------------------------------------------------
def brute_min_v2_H5():
    print("=" * 60)
    print("Empirical min v_2(H_5) over 0 <= a,b <= 20, 0 <= j <= a+b+5")
    print("=" * 60)
    minv = float('inf')
    achievers = []
    dist = Counter()
    for a in range(0, 21):
        for b in range(0, a+1):
            # actually Rick's convention: 0<=b<=a, but H_5 is polynomial
            # min v_2 over all (a,b) unconstrained
            for j in range(0, a+b+6):
                h = H5(a, b, j)
                if h == 0:
                    continue
                v = v2(h)
                dist[v] += 1
                if v < minv:
                    minv = v
                    achievers = [(a, b, j, h)]
                elif v == minv:
                    achievers.append((a, b, j, h))
    print(f"  min v_2(H_5) = {minv}")
    print(f"  # achievers: {len(achievers)}")
    for a, b, j, h in achievers[:10]:
        print(f"    (a,b,j)=({a},{b},{j}): H_5 = {h}, v_2 = {v2(h)}")
    print(f"  v_2 distribution: {dict(sorted(dist.items()))}")


def brute_min_v2_H4():
    print("=" * 60)
    print("Empirical min v_2(H_4) via template inversion")
    print("=" * 60)
    minv = float('inf')
    achievers = []
    dist = Counter()
    # H_4 needs a>=b>=4 for template validity? No: template gives polynomial that's
    # well-defined for all nonneg (a,b,j) after cancelling (a-2)(b-3).
    # But we compute via template only where valid.
    # Actually we use the Sym-side to compute M_j — we need a>=b>=c=4 for M_j Sym.
    # Actually P_j Aitken determinant works for all a,b symbolically.
    # But for our M_j_sym function we require a >= b >= c.
    for a in range(4, 15):
        for b in range(4, min(a, 15) + 1):
            for j in range(0, 7):
                h = H_c_via_template(a, b, 4, j)
                if h is None or h == 0:
                    continue
                v = v2(h)
                dist[v] += 1
                if v < minv:
                    minv = v
                    achievers = [(a, b, j, h)]
                elif v == minv:
                    achievers.append((a, b, j, h))
    print(f"  min v_2(H_4) = {minv}")
    print(f"  # achievers: {len(achievers)}")
    for a, b, j, h in achievers[:10]:
        print(f"    (a,b,j)=({a},{b},{j}): H_4 = {h}, v_2 = {v2(h)}")
    print(f"  v_2 distribution: {dict(sorted(dist.items()))}")


# ------------------------------------------------------------
# Structural lower bound v_2(H_5) >= 3
# Term-by-term analysis of h_k * C(j, k)
# ------------------------------------------------------------
def term_by_term_lb():
    print("=" * 60)
    print("Term-by-term v_2 lower bounds for h_k(a,b) * C(j,k)")
    print("=" * 60)
    print(f"  v_2(20)     = {v2(20)}")
    print(f"  v_2(10)     = {v2(10)}")
    print(f"  v_2(360)    = {v2(360)}")
    print(f"  v_2(240)    = {v2(240)}")
    print(f"  v_2(7200)   = {v2(7200)}")
    print(f"  v_2(100800) = {v2(100800)}")
    print(f"  v_2(201600) = {v2(201600)}")
    print()
    # Verify structural lb: for all (a,b,j) in wide range, each h_k*C(j,k)
    # has v_2 >= claimed.
    claims = {0: 6, 1: 4, 2: 3, 3: 3, 4: 4, 5: 5, 6: 5, 7: 6, 8: 7}
    print("  Claim: v_2(h_k(a,b)*C(j,k)) >= LB_k for LB = ", claims)
    print()
    fails = defaultdict(list)
    for a in range(0, 15):
        for b in range(0, 15):
            hs = h5_coeffs(a, b)
            for j in range(0, 15):
                for k in range(9):
                    cjk = C(j, k)
                    if cjk == 0 or hs[k] == 0:
                        continue
                    val = hs[k] * cjk
                    v = v2(val)
                    if v < claims[k]:
                        fails[k].append((a, b, j, val, v))
    if not fails:
        print("  ALL term-wise LBs hold (a,b,j in [0,15))!")
    else:
        for k, fs in sorted(fails.items()):
            print(f"  h_{k} LB FAILS at {len(fs)} points; first: {fs[:3]}")


if __name__ == "__main__":
    sanity_h5()
    print()
    brute_min_v2_H5()
    print()
    term_by_term_lb()
    print()
    brute_min_v2_H4()
