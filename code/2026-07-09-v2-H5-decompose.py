"""Day 87 CODE Task 2 — Factor-by-factor v_2 decomposition of H_5(a, b, j).

Clio's Lemma-1 template at c=5 (with the c=5 constants α=3, γ=4, β=6,
δ_i=i for i=1..5, const=120=5!, tip=10!·C(j,10)):

    C(N, b-j) · (a-b+1) · [(a-3)(b-4) H_5(a, b, j) - 10! · C(j, 10)]
      = 120 · (a+6-j) · ∏_{i=1..5}(b+i-j) · M_j(a, b, 5)             (†)

where N = a + b + 5 - 2j, M_j = <s_{(a,b,5)}, e_2^j p_1^{N}>.

For j < 10 the tip vanishes, so at those (a, b, j):

    H_5 = [120 · (a+6-j) · ∏(b+i-j) · M_j] / [(a-b+1) · C(N, b-j) · (a-3) · (b-4)]

Per-factor v_2 decomposition (LHS - RHS conventions on the two sides):

    v_2(H_5) = v_2(120) + v_2(a+6-j) + Σ_{i=1..5} v_2(b+i-j) + v_2(M_j)
             - v_2(a-b+1) - v_2(C(N, b-j)) - v_2(a-3) - v_2(b-4)

Report the decomposition at each of the top-5 low-v_2 (a, b, j) where all
factors are nonzero, plus at the M_j-degenerate min points.

Rick, Day 87.
"""
from math import factorial
from fractions import Fraction
from sympy import binomial as sbinom


def v2(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def Cn(n, k):
    if k < 0 or n < 0:
        return 0
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def hook_length_lambda(lam):
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    n = sum(lam)
    a0 = lam[0]
    cols = [0] * a0
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


from collections import defaultdict


def _add_vertical_2_strip(mu, max_rows=4):
    mu = list(mu) + [0] * (max_rows - len(mu))
    results = []
    for i1 in range(max_rows):
        v1 = mu[:]
        v1[i1] += 1
        if i1 > 0 and v1[i1] > v1[i1 - 1]:
            continue
        for i2 in range(i1 + 1, max_rows):
            v2 = v1[:]
            v2[i2] += 1
            if v2[i2] > v2[i2 - 1]:
                continue
            results.append(tuple(x for x in v2 if x > 0))
    return results


_kostka_cache = {}


def kostka_e2_power(j, max_rows=3):
    if j in _kostka_cache:
        return _kostka_cache[j]
    current = defaultdict(int)
    current[tuple()] = 1
    for _ in range(j):
        nxt = defaultdict(int)
        for mu, coef in current.items():
            for nu in _add_vertical_2_strip(mu, max_rows=max(4, max_rows + 1)):
                nxt[nu] += coef
        current = nxt
    filtered = [(mu, k) for mu, k in current.items() if len(mu) <= max_rows]
    _kostka_cache[j] = filtered
    return filtered


def M_j_sym(a, b, c, j):
    """Sym-side M_j via Aitken determinant. Uses cached Kostka expansion."""
    if j == 0:
        return hook_length_lambda((a, b, c)) if (a >= b >= c >= 0) else 0
    table = kostka_e2_power(j, max_rows=3)
    xs = (a + 2, b + 1, c)
    n = a + b + c
    if n < 2 * j:
        return 0

    def fall(x, kk):
        p = 1
        for i in range(kk):
            p *= (x - i)
        return p

    total = Fraction(0)
    for mu, kmult in table:
        mu3 = tuple(list(mu) + [0] * (3 - len(mu)))
        ks = [mu3[jj] + (2 - jj) for jj in range(3)]
        M = [[fall(xs[i], ks[jj]) for jj in range(3)] for i in range(3)]
        det = (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
             - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
             + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))
        f_lam_mu_num = factorial(n - 2 * j) * det
        f_lam_mu_den = factorial(a + 2) * factorial(b + 1) * factorial(c)
        total += Fraction(kmult * f_lam_mu_num, f_lam_mu_den)
    if total.denominator != 1:
        return None
    return int(total)


# Reuse Clio H_5 for a ground-truth reference
def h5_coeffs(a, b):
    h0 = (a+3)*(a+4)*(a+5)*(a+6) * (b+2)*(b+3)*(b+4)*(b+5)
    h1 = -20 * (a+3)*(a+4)*(a+5) * (b+2)*(b+3)*(b+4)
    h2 = -10 * (a+3)*(a+4) * (b+2)*(b+3) * (a*b + a + 2*b - 22)
    h3 = 360 * (a+3) * (b+2) * (a*b + a + 2*b - 2)
    h4 = 240 * (a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a
                + 2*b*b - 34*b - 24)
    h5 = -7200 * (a*b + b - 2)
    h6 = -7200 * (a*b - a - 6)
    h7 = 100800
    h8 = 201600
    return [h0, h1, h2, h3, h4, h5, h6, h7, h8]


def H5_direct(a, b, j):
    hks = h5_coeffs(a, b)
    tot = 0
    for k, hk in enumerate(hks):
        c_jk = int(sbinom(j, k))
        tot += hk * c_jk
    return tot


def decompose_H5(a, b, j):
    """Return dict of per-factor v_2's and computed vs template value."""
    c = 5
    N = a + b + c - 2*j
    Mj = M_j_sym(a, b, c, j)
    const = 120
    factors_num = {
        'const=120': const,
        f'a+6-j={a+6-j}': a + 6 - j,
    }
    prod_bij_val = 1
    for i in range(1, 6):
        v = b + i - j
        factors_num[f'b+{i}-j={v}'] = v
        prod_bij_val *= v
    if Mj is not None:
        factors_num[f'M_{j}(a,b,5)={Mj}'] = Mj

    factors_den = {
        f'a-b+1={a-b+1}': a - b + 1,
        f'C(N={N},b-j={b-j})': Cn(N, b - j),
        f'a-3={a-3}': a - 3,
        f'b-4={b-4}': b - 4,
    }

    tip = factorial(2*c) * Cn(j, 2*c)  # = 10! * C(j, 10)

    return {
        'a': a, 'b': b, 'j': j,
        'N': N,
        'M_j': Mj,
        'factors_num': factors_num,
        'factors_den': factors_den,
        'tip': tip,
        'H5_direct': H5_direct(a, b, j),
    }


def format_decomposition(d):
    lines = []
    a, b, j = d['a'], d['b'], d['j']
    H5 = d['H5_direct']
    lines.append(f"--- (a, b, j) = ({a}, {b}, {j})  N={d['N']}  H_5={H5}  v_2(H_5)={v2(H5)}")
    if d['tip'] != 0:
        lines.append(f"    (tip term 10!·C(j,10) = {d['tip']}, v_2={v2(d['tip'])})")
    else:
        lines.append(f"    (tip term = 0, only M_j-contribution)")
    lines.append("    Numerator factors (positive contribution to v_2(H_5)):")
    total_pos = 0
    for name, val in d['factors_num'].items():
        vv = v2(val)
        total_pos += vv if vv != float('inf') else 0
        lines.append(f"      {name:30s}  v_2 = {vv}")
    lines.append(f"      TOTAL numerator v_2 = {total_pos}")
    lines.append("    Denominator factors (negative contribution):")
    total_neg = 0
    for name, val in d['factors_den'].items():
        vv = v2(val)
        total_neg += vv if vv != float('inf') else 0
        lines.append(f"      {name:30s}  v_2 = {vv}")
    lines.append(f"      TOTAL denominator v_2 = {total_neg}")
    net = total_pos - total_neg
    lines.append(f"    NET (num - den) = {net}, actual v_2(H_5) = {v2(H5)}")
    lines.append("")
    return "\n".join(lines)


def find_top_nondegenerate_min_points(nmax=30):
    """Find the top low-v_2 (a, b, j) with all denominator factors nonzero."""
    rows = []
    for a in range(0, 30):
        for b in range(0, a + 1):
            for j in range(0, 11):
                # skip degenerate points
                if a == 3 or b == 4 or a == b - 1:
                    continue
                N = a + b + 5 - 2*j
                if N < 0:
                    continue
                if b - j < 0 or b - j > N:
                    continue
                val = H5_direct(a, b, j)
                if val == 0:
                    continue
                rows.append((v2(val), a, b, j, val))
    rows.sort()
    return rows[:nmax]


def main():
    lines = []
    lines.append("=" * 78)
    lines.append("Day 87 CODE Task 2 — Per-factor v_2 decomposition of H_5(a, b, j)")
    lines.append("=" * 78)
    lines.append("")
    lines.append("Clio's Lemma-1 template at c=5 gives H_5 as a rational function of")
    lines.append("integer factors (assuming j < 10 so the tip vanishes):")
    lines.append("")
    lines.append("  H_5 = [120 · (a+6-j) · Π(b+i-j) · M_j] / ")
    lines.append("        [(a-b+1) · C(N, b-j) · (a-3) · (b-4)]")
    lines.append("")
    lines.append("v_2(H_5) = v_2(120) + v_2(a+6-j) + Σv_2(b+i-j) + v_2(M_j)")
    lines.append("        - v_2(a-b+1) - v_2(C(N,b-j)) - v_2(a-3) - v_2(b-4)")
    lines.append("")
    lines.append("Note: at DEGENERATE points (a=3 or b=4) the denominator vanishes,")
    lines.append("but H_5 is still well-defined via Clio's 9-term polynomial. The")
    lines.append("decomposition-formula v_2 is undefined at those points.")
    lines.append("")

    # Day-85 minimizer (degenerate): (3, 0, 2)
    lines.append("=" * 78)
    lines.append("Day-85 minimizer (a, b, j) = (3, 0, 2) — DEGENERATE (a-3 = 0)")
    lines.append("=" * 78)
    lines.append("")
    d = decompose_H5(3, 0, 2)
    lines.append(format_decomposition(d))

    # Top-5 non-degenerate min points
    lines.append("=" * 78)
    lines.append("Top-10 non-degenerate low-v_2 points (a, b, j) with a≠3, b≠4, a-b+1≠0:")
    lines.append("=" * 78)
    lines.append("")
    tops = find_top_nondegenerate_min_points(nmax=10)
    for (vv, a, b, j, val) in tops:
        d = decompose_H5(a, b, j)
        lines.append(format_decomposition(d))

    # Also examine (7, 4, 2) — a "top" point despite b=4 degeneration
    lines.append("=" * 78)
    lines.append("Cross-check: b=4 semi-degenerate point (7, 4, 2)")
    lines.append("=" * 78)
    lines.append("")
    d = decompose_H5(7, 4, 2)
    lines.append(format_decomposition(d))

    out = "\n".join(lines)
    print(out)
    with open("/home/agent/projects/code/2026-07-09-v2-H5-decompose-output.txt", "w") as f:
        f.write(out)


if __name__ == "__main__":
    main()
