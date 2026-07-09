"""
Spot-check of Clio's post-outage claims (2026-07-05 peer review).
- Theorem A γ(c) formula match.
- H_5(3,0,2) sharp for β'(5) = 3.
- Lemma 1 closed form + J* prediction across 7 (a,b,5) shapes.
- Independent hook-length cross-check of f^(13,13,6).
"""
from math import factorial


def s2(n): return bin(n).count('1')


def v2(n):
    if n == 0: return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def C(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def gamma(c):
    # Theorem A: content of H_c(0) on the valid-parity sheet.
    if c % 2 == 0:
        k = c // 2
        return 4 * k - 2 - s2(k) - s2(k - 1)
    k = (c - 1) // 2
    return 4 * k - 2 * s2(k)


def beta_rick(c):
    return 2 * (c - 1) - s2(c - 1)


def H5(a, b, j):
    h0 = (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5)
    h1 = -20*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4)
    h2 = -10*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 22)
    h3 = 360*(a+3)*(b+2)*(a*b + a + 2*b - 2)
    h4 = 240*(a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a + 2*b*b - 34*b - 24)
    h5 = -7200*(a*b + b - 2)
    h6 = -7200*(a*b - a - 6)
    h7 = 100800
    h8 = 201600
    hs = [h0, h1, h2, h3, h4, h5, h6, h7, h8]
    return sum(hs[k] * C(j, k) for k in range(9))


def M_j(a, b, c, j):
    """Clio's Lemma 1 closed form, c=5 only."""
    assert c == 5
    m = (a + b + c) // 2
    N = 2 * (m - j)
    Q5 = (a - 3) * (b - 4) * H5(a, b, j) - factorial(10) * C(j, 10)
    den = 120 * (a + 6 - j)
    for i in range(1, 6):
        den *= (b + i - j)
    num = C(N, b - j) * (a - b + 1) * Q5
    if num % den != 0:
        return None
    return num // den


def Jstar(a, b, c):
    m = (a + b + c) // 2
    vs = []
    for j in range(0, b + 1):
        Mj = M_j(a, b, c, j)
        Cmj = C(m, j)
        if Mj is None or Cmj * Mj == 0:
            continue
        v = j + 2 * v2(Cmj * Mj)
        vs.append((v, j))
    V = min(v for v, _ in vs)
    return V, sorted(j for v, j in vs if v == V)


def hook_length(lam):
    """f^λ by hook-length formula."""
    n = sum(lam)
    cols = [0] * lam[0]
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


if __name__ == "__main__":
    print("γ(c) for c=4..10 (Theorem A):",
          [gamma(c) for c in range(4, 11)],
          "expected [4,6,7,8,11,14,15]")
    print("β(c) rigid NL:",
          [beta_rick(c) for c in range(4, 11)],
          "β(5) = 7 (rigid floor, opposite of β'(5)=3)")

    H = H5(3, 0, 2)
    print(f"H_5(3,0,2) = {H}, v2 = {v2(H)} — expected 3 (β'(5) sharp).")

    # Direct min of v2(H_c(0)) — should match γ(c)
    def H4_0(a, b):
        return (a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4)
    def H5_0(a, b):
        return (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5)
    def H6_0(a, b):
        r = 1
        for t in range(3, 8): r *= (a + t)
        for t in range(2, 7): r *= (b + t)
        return r

    for c, Hfn, parity in [(4, H4_0, 0), (5, H5_0, 1), (6, H6_0, 0)]:
        m = min(v2(Hfn(a, b)) for a in range(32) for b in range(32)
                if (a + b) % 2 == parity)
        print(f"min v2(H_{c}(0)) brute (a,b<32) = {m}, γ({c}) formula = {gamma(c)}")

    # J* verification for c=5
    shapes = [(11, 8), (12, 9), (11, 10), (13, 10), (14, 11), (16, 13), (15, 12)]
    print("\nJ* verification for c=5:")
    for (a, b) in shapes:
        V, J = Jstar(a, b, 5)
        print(f"  λ=({a},{b},5): (a,b) mod 4 = ({a%4},{b%4}), V={V}, J* = {J}")

    # (13,13,6) hook-length cross-check
    f = hook_length([13, 13, 6])
    print(f"\nf^(13,13,6) = {f}")
    print(f"Clio: M_0 = 230,814,869,760 — match: {f == 230814869760}")
