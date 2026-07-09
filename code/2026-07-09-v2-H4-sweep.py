"""Day 87 CODE Task 3 — v_2(H_4(a, b, j)) sweep + per-factor decomposition.

Uses Clio's c-uniform Lemma-1 template at c=4:
  (α, γ, β, δ, const, tip) = (2, 3, 5, {1..4}, 24, 8!·C(j, 8))

The c=4 predicted H_4 polynomial comes from Day 87's h_k^{(4)} fit:
  h_0^{(4)} = (a+3)(a+4)(a+5) · (b+2)(b+3)(b+4)
  h_1^{(4)} = -12 (a+3)(a+4) · (b+2)(b+3)
  h_2^{(4)} = -8 (a+3) · (b+2) · (ab + a + 2b - 7)
  h_3^{(4)} = 144 (ab + a + 2b + 1)
  h_4^{(4)} = 144 (ab + b - 4)
  h_5^{(4)} = -1440
  h_6^{(4)} = 120 (a²b - 2a² + ab² - 11ab + 18a - b² + 10b - 40)

Sweep (a, b, j) and record min v_2 + decomposition at min points.

Rick, Day 87.
"""
from math import factorial
from fractions import Fraction
from collections import defaultdict


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
    if k < 0 or n < 0 or k > n:
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


# H_4 polynomial (Day 87 h_k^{(4)} fits — see proofs/2026-07-09-d1-c5-structural.md)
def h4_coeffs(a, b):
    h0 = (a+3)*(a+4)*(a+5) * (b+2)*(b+3)*(b+4)
    h1 = -12 * (a+3)*(a+4) * (b+2)*(b+3)
    h2 = -8 * (a+3) * (b+2) * (a*b + a + 2*b - 7)
    h3 = 144 * (a*b + a + 2*b + 1)
    h4 = 144 * (a*b + b - 4)
    h5 = -1440
    h6 = 120 * (a*a*b - 2*a*a + a*b*b - 11*a*b + 18*a - b*b + 10*b - 40)
    return [h0, h1, h2, h3, h4, h5, h6]


def H4_direct(a, b, j):
    from sympy import binomial as sbinom
    hks = h4_coeffs(a, b)
    tot = 0
    for k, hk in enumerate(hks):
        c_jk = int(sbinom(j, k))
        tot += hk * c_jk
    return tot


def H4_via_template(a, b, j):
    """H_4 via Clio's inverse template using Sym-side M_j at c=4.
    Serves as consistency check on the fit."""
    c = 4
    N = a + b + c - 2*j
    Mj = M_j_sym(a, b, c, j)
    if Mj is None:
        return None
    prod_bij = 1
    for i in range(1, c + 1):
        prod_bij *= (b + i - j)
    Cnbj = Cn(N, b - j)
    if Cnbj == 0 or (a - b + 1) == 0 or (a - (c - 2)) == 0 or (b - (c - 1)) == 0:
        return None
    numer_A = factorial(c) * (a + c + 1 - j) * prod_bij * Mj
    tip = factorial(2 * c) * Cn(j, 2 * c)  # 8! · C(j, 8) at c=4
    val = Fraction(numer_A, Cnbj * (a - b + 1)) + tip
    h = val / Fraction((a - (c - 2)) * (b - (c - 1)))
    if h.denominator == 1:
        return int(h)
    return None


def sweep_c4(parity_shell_only=True):
    """Sweep H_4(a, b, j). If parity_shell_only, restrict to a+b even
    (equivalently a+b+4 even), which is the "physical" parity shell for c=4.
    Off-shell values also polynomial-valued but generically not integer or
    not the honest Clio-side count."""
    rows_shell = []
    rows_offshell = []
    for a in range(0, 31):
        for b in range(0, a + 1):
            for j in range(0, 13):
                val = H4_direct(a, b, j)
                if val == 0:
                    continue
                if (a + b) % 2 == 0:
                    rows_shell.append((a, b, j, val, v2(val)))
                else:
                    rows_offshell.append((a, b, j, val, v2(val)))
    return rows_shell, rows_offshell


def decompose_H4(a, b, j):
    c = 4
    N = a + b + c - 2*j
    Mj = M_j_sym(a, b, c, j)
    factors_num = {
        'const=24=4!': 24,
        f'a+5-j={a+5-j}': a + 5 - j,
    }
    for i in range(1, c + 1):
        v = b + i - j
        factors_num[f'b+{i}-j={v}'] = v
    if Mj is not None:
        factors_num[f'M_{j}(a,b,4)={Mj}'] = Mj

    factors_den = {
        f'a-b+1={a-b+1}': a - b + 1,
        f'C(N={N},b-j={b-j})': Cn(N, b - j),
        f'a-2={a-2}': a - 2,
        f'b-3={b-3}': b - 3,
    }

    tip = factorial(2 * c) * Cn(j, 2 * c)  # = 8! · C(j, 8)

    return {
        'a': a, 'b': b, 'j': j,
        'N': N,
        'M_j': Mj,
        'factors_num': factors_num,
        'factors_den': factors_den,
        'tip': tip,
        'H4_direct': H4_direct(a, b, j),
    }


def format_decomposition(d):
    lines = []
    a, b, j = d['a'], d['b'], d['j']
    H4 = d['H4_direct']
    lines.append(f"--- (a, b, j) = ({a}, {b}, {j})  N={d['N']}  H_4={H4}  v_2(H_4)={v2(H4)}")
    if d['tip'] != 0:
        lines.append(f"    (tip term 8!·C(j,8) = {d['tip']}, v_2={v2(d['tip'])})")
    else:
        lines.append(f"    (tip term = 0, only M_j-contribution)")
    lines.append("    Numerator factors:")
    total_pos = 0
    for name, val in d['factors_num'].items():
        vv = v2(val)
        total_pos += vv if vv != float('inf') else 0
        lines.append(f"      {name:30s}  v_2 = {vv}")
    lines.append(f"      TOTAL numerator v_2 = {total_pos}")
    lines.append("    Denominator factors:")
    total_neg = 0
    for name, val in d['factors_den'].items():
        vv = v2(val)
        total_neg += vv if vv != float('inf') else 0
        lines.append(f"      {name:30s}  v_2 = {vv}")
    lines.append(f"      TOTAL denominator v_2 = {total_neg}")
    net = total_pos - total_neg
    lines.append(f"    NET (num - den) = {net}, actual v_2(H_4) = {v2(H4)}")
    lines.append("")
    return "\n".join(lines)


def find_top_nondegenerate_min_c4(rows, nmax=10):
    """Rows already sorted; pick min-v_2 with all denominator factors nonzero."""
    tops = []
    for r in rows:
        (a, b, j, val, vv) = r
        # skip degenerate denominator points
        if a == 2 or b == 3 or (a - b + 1) == 0:
            continue
        N = a + b + 4 - 2*j
        if N < 0 or Cn(N, b - j) == 0:
            continue
        tops.append(r)
        if len(tops) >= nmax:
            break
    return tops


def main():
    rows_shell, rows_offshell = sweep_c4()
    rows_shell.sort(key=lambda r: r[4])
    rows_offshell.sort(key=lambda r: r[4])
    rows = rows_shell
    lines = []
    lines.append("=" * 78)
    lines.append("Day 87 CODE Task 3 — v_2(H_4(a, b, j)) sweep at c=4")
    lines.append("=" * 78)
    lines.append("")
    lines.append(f"Sample size (parity shell a+b even): {len(rows_shell)}")
    lines.append(f"Sample size (off-shell a+b odd):    {len(rows_offshell)}")
    lines.append("")
    lines.append(f"Off-shell MIN v_2 (a+b odd, for reference): {rows_offshell[0][4]}")
    lines.append(f"Off-shell min pt: (a, b, j) = ({rows_offshell[0][0]}, {rows_offshell[0][1]}, {rows_offshell[0][2]}), H_4 = {rows_offshell[0][3]}")
    lines.append("")
    min_v = rows[0][4]
    min_pts = [r for r in rows if r[4] == min_v]
    lines.append(f"PARITY-SHELL MIN v_2 = {min_v}  (expected β'(4) = 4)")
    lines.append(f"Number of (a, b, j) at min: {len(min_pts)}")
    lines.append("")
    lines.append("First 20 minimizers (a, b, j, H_4, v_2):")
    for r in min_pts[:20]:
        lines.append(f"  a={r[0]:3d}  b={r[1]:3d}  j={r[2]:3d}  H_4={r[3]:>18d}  v_2={r[4]}")
    lines.append("")
    lines.append("Top-30 lowest-v_2 (a, b, j, H_4, v_2):")
    for r in rows[:30]:
        lines.append(f"  a={r[0]:3d}  b={r[1]:3d}  j={r[2]:3d}  H_4={r[3]:>18d}  v_2={r[4]}")
    lines.append("")
    lines.append("v_2 distribution:")
    dist = {}
    for r in rows:
        dist[r[4]] = dist.get(r[4], 0) + 1
    for v in sorted(dist.keys()):
        lines.append(f"  v_2 = {v:3d}: {dist[v]}")
    lines.append("")
    lines.append("=" * 78)
    lines.append("Day-87 expected minimizer (a, b, j) = (0, 0, 2)")
    lines.append("=" * 78)
    lines.append("")
    d = decompose_H4(0, 0, 2)
    lines.append(format_decomposition(d))

    # Non-degenerate min points
    lines.append("=" * 78)
    lines.append("Top-10 non-degenerate low-v_2 points (a≠2, b≠3, a-b+1≠0):")
    lines.append("=" * 78)
    lines.append("")
    tops = find_top_nondegenerate_min_c4(rows, nmax=10)
    for (a, b, j, val, vv) in tops:
        d = decompose_H4(a, b, j)
        lines.append(format_decomposition(d))

    # ============ Δβ' comparison =============
    lines.append("=" * 78)
    lines.append("COMPARISON: β'(5) - β'(4) = Δβ'(5) mechanism")
    lines.append("=" * 78)
    lines.append("")
    lines.append("From Task 1:  β'(5) = 3, min at (3, 0, 2), H_5 = 88200 = 2^3 · 11025.")
    lines.append(f"From Task 3:  β'(4) = {min_v}, min at {min_pts[0][:3]}, H_4 = {min_pts[0][3]}.")
    lines.append(f"Δβ'(5) = β'(5) - β'(4) = 3 - {min_v} = {3 - min_v}.")
    lines.append(f"D1 predicts Δβ'(5) = 1 - max(2, v_2(5-1)) = 1 - max(2, 2) = -1.")
    lines.append(f"Empirical match: {3 - min_v == -1}")
    lines.append("")
    lines.append("PER-FACTOR shift: v_2 of the c! constant")
    lines.append(f"  c=5: v_2(120) = {v2(120)}   (= β'(5))")
    lines.append(f"  c=4: v_2(24)  = {v2(24)}   (= β'(4))")
    lines.append(f"  Δ = v_2(5!) - v_2(4!) = 3 - 3 = 0.")
    lines.append("")
    lines.append("So the c! constant DOES NOT explain Δβ'(5) = -1. The mechanism")
    lines.append("must come from ONE OTHER factor whose v_2 contribution differs")
    lines.append("between c=5 and c=4 minimizers.")

    out = "\n".join(lines)
    print(out)
    with open("/home/agent/projects/code/2026-07-09-v2-H4-sweep-output.txt", "w") as f:
        f.write(out)


if __name__ == "__main__":
    main()
