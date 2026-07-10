"""Day 87 - Derive Clio's H_4 polynomial structurally, then verify min v_2 = 4.

Strategy:
  (1) Reuse the c-uniform template inversion at c=4 with correct parity.
  (2) Use Sym-side M_j at c=4 (from Day 86 P_j closed forms).
  (3) Fit an explicit polynomial H_4(a,b,j) = sum_{k=0}^{2c-1=7} h_k^{(4)}(a,b) C(j,k).
  (4) Test the c-uniform pattern for h_k^{(c)} deduced from Day-84 mnemonic.
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


# ============================================================
# c-uniform h_k mnemonic (Day 84 §6 conjecture, extended)
#
# For H_c(a, b, j) = sum_{k=0}^{2c-1} h_k^{(c)}(a, b) C(j, k),
# based on the c=5 pattern:
#
#   h_0 = prod_{i=3}^{c+1} (a+i) * prod_{i=2}^{c} (b+i)     [Day 84 §6.5]
#   h_1 = -20 * (c-3-terms) at c=5...
#         Actually needs to be derived. Let me use a different approach:
#         directly fit h_k^{(4)}(a,b) from the empirical values.
# ============================================================


# ============================================================
# Compute H_4 for many test points and fit each h_k^{(4)}(a,b)
#
# Approach: For each (a, b), H_4(a, b, j) = sum_k h_k^{(4)}(a,b) C(j,k),
# which is a polynomial in j of degree <= 2c-1 = 7. So we can solve for
# h_k^{(4)}(a,b) by evaluating H_4(a,b,j) at j = 0, 1, ..., 7.
#
# The inversion C(j,k) matrix is triangular; we can invert it.
# ============================================================


def hook_length_lambda(lam):
    n = sum(lam)
    a = lam[0]
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


def M_j_sym(a, b, c, j):
    """M_j(a,b,c) via Sym-side formula."""
    tables = {
        0: [((0, 0, 0), 1)],
        1: [((1, 1, 0), 1)],
        2: [((2, 2, 0), 1), ((2, 1, 1), 1)],
        3: [((3, 3, 0), 1), ((3, 2, 1), 2), ((2, 2, 2), 1)],
        4: [((4, 4, 0), 1), ((4, 3, 1), 3), ((4, 2, 2), 2), ((3, 3, 2), 3)],
        5: [((5, 5, 0), 1), ((5, 4, 1), 4), ((5, 3, 2), 5), ((4, 4, 2), 6),
            ((4, 3, 3), 5)],
    }
    if j == 0:
        return hook_length_lambda((a, b, c)) if (a >= b >= c >= 0) else 0
    if j not in tables:
        raise ValueError(f"j={j} not tabulated")
    xs = (a + 2, b + 1, c)
    n = a + b + c
    if n < 2 * j:
        return 0
    total = Fraction(0)
    for mu, k in tables[j]:
        ks = [mu[jj] + (2 - jj) for jj in range(3)]
        def fall(x, kk):
            p = 1
            for i in range(kk):
                p *= (x - i)
            return p
        M = [[fall(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        det = (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
             - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
             + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))
        f_lam_mu_num = factorial(n - 2*j) * det
        f_lam_mu_den = factorial(a+2) * factorial(b+1) * factorial(c)
        total += Fraction(k * f_lam_mu_num, f_lam_mu_den)
    assert total.denominator == 1, f"M_{j}({a},{b},{c}) = {total} not integer"
    return int(total)


def H_c_template(a, b, c, j):
    """H_c(a,b,j) via template inversion, assuming Sym-side M_j."""
    N = a + b + c - 2*j
    if N < 0 or (b - j) < 0 or (b - j) > N:
        return None
    Mj = M_j_sym(a, b, c, j)
    prod_bij = 1
    for i in range(1, c+1):
        prod_bij *= (b + i - j)
    CNbj = C(N, b - j)
    if CNbj == 0 or (a - b + 1) == 0 or (a - c + 2) == 0 or (b - c + 1) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    val = Fraction(numer_A, CNbj * (a - b + 1)) + factorial(2*c) * C(j, 2*c)
    h = val / Fraction((a - c + 2) * (b - c + 1))
    if h.denominator == 1:
        return int(h)
    return None


# ============================================================
# Empirical H_5 (Clio) — for cross-check
# ============================================================
def H5_clio(a, b, j):
    hs = [
        (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5),
        -20*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4),
        -10*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 22),
        360*(a+3)*(b+2)*(a*b + a + 2*b - 2),
        240*(a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a + 2*b*b - 34*b - 24),
        -7200*(a*b + b - 2),
        -7200*(a*b - a - 6),
        100800,
        201600,
    ]
    return sum(hs[k] * C(j, k) for k in range(9))


def sanity_h5_valid_parity():
    """Sanity: template inversion matches Clio H_5 on valid parity (a+b odd for c=5)."""
    print("=" * 60)
    print("Sanity: template vs Clio H_5, ONLY on valid parity (a+b odd)")
    print("=" * 60)
    passes = 0
    total = 0
    fails = []
    for a in range(5, 15):
        for b in range(5, min(a, 12) + 1):
            if (a + b) % 2 != 1:  # c=5 needs a+b odd
                continue
            for j in range(0, 6):  # M_j_sym only tabulated to j=5
                clio = H5_clio(a, b, j)
                tmpl = H_c_template(a, b, 5, j)
                total += 1
                if tmpl is None:
                    continue
                if tmpl == clio:
                    passes += 1
                else:
                    fails.append((a, b, j, clio, tmpl))
    print(f"  {passes}/{total} matches on valid parity")
    for f in fails[:5]:
        print(f"    MISMATCH {f}")


# ============================================================
# Extract h_k^{(4)}(a,b) coefficients from H_4 samples
# ============================================================
def extract_h_k_from_H_4(a, b, jmax=6):
    """Given H_4(a,b,j) for j=0,1,...,jmax, solve for h_k^{(4)}(a,b) for k=0..jmax."""
    Hs = []
    for j in range(jmax + 1):
        h = H_c_template(a, b, 4, j)
        if h is None:
            return None
        Hs.append(h)
    # H(j) = sum_{k=0}^{jmax} h_k C(j, k)
    # Triangular. C(0,0)=1, C(1,0)=1, C(1,1)=1, C(2,0)=1, C(2,1)=2, C(2,2)=1, ...
    hks = []
    for k in range(jmax + 1):
        val = Hs[k]
        for kk in range(k):
            val -= hks[kk] * C(k, kk)
        hks.append(val)
    # Verify
    for j in range(jmax + 1):
        check = sum(hks[k] * C(j, k) for k in range(jmax + 1))
        assert check == Hs[j]
    return hks


def survey_h_k_c4():
    """For a range of (a,b) with a+b even (c=4 parity), extract h_k^{(4)}(a,b)."""
    print("=" * 60)
    print("Extract h_k^{(4)}(a,b) from H_4 samples")
    print("=" * 60)
    # Sample at a few (a,b) with a+b even, a >= b >= 4
    samples = []
    for a in range(4, 12):
        for b in range(4, a + 1):
            if (a + b) % 2 != 0:
                continue  # c=4 valid parity
            hks = extract_h_k_from_H_4(a, b, jmax=5)
            if hks is None:
                continue
            samples.append((a, b, hks))
    print(f"  {len(samples)} sample points")
    print()
    # Print h_k at (a, b) = (4, 4), (6, 4), (5, 5), etc.
    for (a, b, hks) in samples[:8]:
        print(f"  (a,b) = ({a}, {b}):")
        for k, h in enumerate(hks):
            print(f"    h_{k} = {h}  (v_2 = {v2(h) if h else 'inf'})")
        print()
    return samples


# ============================================================
# Test structural conjecture: H_4 = polynomial with c-uniform structure
# The Day-84 mnemonic says:
#   h_0^{(c)}(a, b) = prod_{i=3}^{c+1} (a+i) · prod_{i=2}^{c} (b+i)
#   h_2^{(c)}(a, b) = -C(c,2) · prod_{i=3}^{c-1} (a+i) · prod_{i=2}^{c-2} (b+i)
#                       · [(a+2)(b+1) - (c-1)!]
#
# At c=4:
#   h_0^{(4)}(a, b) = (a+3)(a+4)(a+5) · (b+2)(b+3)(b+4)
#   h_2^{(4)}(a, b) = -6 · (a+3) · (b+2) · [(a+2)(b+1) - 6]
#
# Let me verify this against extract_h_k_from_H_4.
# ============================================================
def verify_c4_mnemonic():
    print("=" * 60)
    print("Verify c=4 mnemonic against extracted h_k^{(4)}")
    print("=" * 60)
    # From mnemonic:
    def h0_conj(a, b):
        return (a+3)*(a+4)*(a+5) * (b+2)*(b+3)*(b+4)
    def h2_conj(a, b):
        return -6 * (a+3) * (b+2) * ((a+2)*(b+1) - 6)

    passes_h0 = 0
    fails_h0 = []
    passes_h2 = 0
    fails_h2 = []
    for a in range(4, 12):
        for b in range(4, a + 1):
            if (a + b) % 2 != 0:
                continue
            hks = extract_h_k_from_H_4(a, b, jmax=5)
            if hks is None:
                continue
            if hks[0] == h0_conj(a, b):
                passes_h0 += 1
            else:
                fails_h0.append((a, b, hks[0], h0_conj(a, b)))
            if hks[2] == h2_conj(a, b):
                passes_h2 += 1
            else:
                fails_h2.append((a, b, hks[2], h2_conj(a, b)))
    print(f"  h_0 mnemonic: {passes_h0} passes, {len(fails_h0)} fails")
    for f in fails_h0[:3]:
        print(f"    (a,b)=({f[0]},{f[1]}): extracted={f[2]}, mnemonic={f[3]}")
    print(f"  h_2 mnemonic: {passes_h2} passes, {len(fails_h2)} fails")
    for f in fails_h2[:3]:
        print(f"    (a,b)=({f[0]},{f[1]}): extracted={f[2]}, mnemonic={f[3]}")


if __name__ == "__main__":
    sanity_h5_valid_parity()
    print()
    survey_h_k_c4()
    verify_c4_mnemonic()
