"""Day 87 CODE Task 4 — v_2(H_c^pred(a, b, j)) predictions at c = 6, 7, 9.

Uses the c-uniform Clio Lemma-1 template inversion with Sym-side M_j:

  H_c^pred = { c!(a+c+1-j) · Π_{i=1..c}(b+i-j) · M_j(a,b,c)
               / [C(N,b-j)(a-b+1)] + (2c)! · C(j, 2c) }
             / [(a-(c-2))(b-(c-1))]

where M_j(a,b,c) = <s_{(a,b,c)}, e_2^j p_1^{n-2j}>, computed via the
Aitken determinant on the Sym side (Day 86 c-uniform structural, checked-sober).

Predictions:
  β'(6), β'(7), β'(9)  = min_{a, b, j} v_2(H_c^pred(a, b, j))
  on the parity shell (a + b + c) even.

Clio-shipped values (per CODE.md, Day 87 spec):
  β'(7) = 6
  β'(9) = 9

Also examines the per-factor v_2 at minimizers.

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


def Hc_pred(a, b, c, j):
    """Template inversion at c-uniform. Assumes integer output; returns None if degenerate."""
    N = a + b + c - 2 * j
    if N < 0:
        return None
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
    tip = factorial(2 * c) * Cn(j, 2 * c)
    val = Fraction(numer_A, Cnbj * (a - b + 1)) + tip
    h = val / Fraction((a - (c - 2)) * (b - (c - 1)))
    if h.denominator != 1:
        return None
    return int(h)


def sweep_Hc(c, amax=30, jmax=None):
    """Sweep H_c^pred at fixed c. Returns list of (a, b, j, val, v_2) rows
    for parity-shell (a+b+c) even, and off-shell separately."""
    if jmax is None:
        jmax = 2 * c + 4  # enough to cover tip term regime
    rows_shell = []
    rows_offshell = []
    for a in range(c, amax + 1):
        for b in range(c, a + 1):  # physical: a >= b >= c
            for j in range(0, jmax + 1):
                val = Hc_pred(a, b, c, j)
                if val is None or val == 0:
                    continue
                row = (a, b, j, val, v2(val))
                if (a + b + c) % 2 == 0:
                    rows_shell.append(row)
                else:
                    rows_offshell.append(row)
    return rows_shell, rows_offshell


def decompose_Hc(a, b, c, j):
    N = a + b + c - 2 * j
    Mj = M_j_sym(a, b, c, j)
    factors_num = {
        f'const={factorial(c)}=c!': factorial(c),
        f'a+{c+1}-j={a+c+1-j}': a + c + 1 - j,
    }
    for i in range(1, c + 1):
        v = b + i - j
        factors_num[f'b+{i}-j={v}'] = v
    if Mj is not None:
        factors_num[f'M_{j}(a,b,{c})={Mj}'] = Mj
    factors_den = {
        f'a-b+1={a-b+1}': a - b + 1,
        f'C(N={N},b-j={b-j})': Cn(N, b - j),
        f'a-(c-2)={a-(c-2)}': a - (c - 2),
        f'b-(c-1)={b-(c-1)}': b - (c - 1),
    }
    tip = factorial(2 * c) * Cn(j, 2 * c)
    return {
        'a': a, 'b': b, 'c': c, 'j': j,
        'N': N, 'M_j': Mj,
        'factors_num': factors_num,
        'factors_den': factors_den,
        'tip': tip,
        'Hc': Hc_pred(a, b, c, j),
    }


def format_decomp(d):
    lines = []
    a, b, c, j = d['a'], d['b'], d['c'], d['j']
    Hc = d['Hc']
    lines.append(f"--- (a, b, j) = ({a}, {b}, {j})  N={d['N']}  H_{c}={Hc}  v_2={v2(Hc)}")
    if d['tip'] != 0:
        lines.append(f"    (tip term (2c)!·C(j,2c) = {d['tip']}, v_2={v2(d['tip'])})")
    else:
        lines.append(f"    (tip term = 0)")
    lines.append("    Numerator factors:")
    tot_pos = 0
    for name, val in d['factors_num'].items():
        vv = v2(val)
        tot_pos += vv if vv != float('inf') else 0
        lines.append(f"      {name:32s}  v_2 = {vv}")
    lines.append(f"      TOTAL numerator v_2 = {tot_pos}")
    lines.append("    Denominator factors:")
    tot_neg = 0
    for name, val in d['factors_den'].items():
        vv = v2(val)
        tot_neg += vv if vv != float('inf') else 0
        lines.append(f"      {name:32s}  v_2 = {vv}")
    lines.append(f"      TOTAL denominator v_2 = {tot_neg}")
    net = tot_pos - tot_neg
    lines.append(f"    NET = {net}, actual v_2 = {v2(Hc)}")
    lines.append("")
    return "\n".join(lines)


def analyze_c(c, expected_beta_prime, amax=25, out_lines=None):
    if out_lines is None:
        out_lines = []
    rows_shell, rows_offshell = sweep_Hc(c, amax=amax)
    rows_shell.sort(key=lambda r: r[4])
    rows_offshell.sort(key=lambda r: r[4])

    out_lines.append("=" * 78)
    out_lines.append(f"c = {c}: v_2(H_{c}^pred) sweep")
    out_lines.append(f"  Sample sizes: {len(rows_shell)} parity-shell, {len(rows_offshell)} off-shell.")
    out_lines.append("=" * 78)
    out_lines.append("")
    if not rows_shell:
        out_lines.append("(no shell samples)")
        return out_lines
    min_v_shell = rows_shell[0][4]
    out_lines.append(f"PARITY-SHELL min v_2 = {min_v_shell}")
    out_lines.append(f"  Expected β'({c}) = {expected_beta_prime}")
    out_lines.append(f"  Match: {min_v_shell == expected_beta_prime}")
    out_lines.append("")
    out_lines.append(f"  min minimizers (first 10):")
    for r in [r for r in rows_shell if r[4] == min_v_shell][:10]:
        out_lines.append(f"    a={r[0]:3d}  b={r[1]:3d}  j={r[2]:3d}  H_{c}={r[3]:>20d}  v_2={r[4]}")
    out_lines.append("")
    out_lines.append(f"  Off-shell min v_2 = {rows_offshell[0][4] if rows_offshell else 'n/a'}")
    if rows_offshell:
        r = rows_offshell[0]
        out_lines.append(f"    off-shell min: (a, b, j) = ({r[0]}, {r[1]}, {r[2]}), H_{c} = {r[3]}, v_2 = {r[4]}")
    out_lines.append("")
    out_lines.append(f"  v_2 distribution (parity shell):")
    dist = {}
    for r in rows_shell:
        dist[r[4]] = dist.get(r[4], 0) + 1
    for v in sorted(dist.keys())[:15]:
        out_lines.append(f"    v_2 = {v:3d}: {dist[v]}")

    # Show per-factor decomposition at first non-degenerate min
    out_lines.append("")
    out_lines.append(f"  Per-factor decomposition at first non-degenerate min:")
    for r in rows_shell:
        (a, b, j, val, vv) = r
        if vv != min_v_shell:
            continue
        if a == c - 2 or b == c - 1 or a - b + 1 == 0:
            continue
        d = decompose_Hc(a, b, c, j)
        out_lines.append(format_decomp(d))
        break
    out_lines.append("")
    return out_lines


def main():
    lines = []
    lines.append("=" * 78)
    lines.append("Day 87 CODE Task 4 — v_2(H_c^pred) predictions at c = 6, 7, 9")
    lines.append("=" * 78)
    lines.append("")
    lines.append("Method: Sym-side M_j via Aitken → template inversion → H_c^pred.")
    lines.append("If H_c^pred matches Clio's β'(c) via 2-adic minimization,")
    lines.append("the c-uniform M_j chain is empirically validated at c > 5.")
    lines.append("")

    # Clio-shipped β' values (from CODE.md, Day 87)
    clio_beta_prime = {
        4: 4,     # Day-87 proved
        5: 3,     # Day-85 verified
        6: None,  # unknown
        7: 6,     # Clio-shipped
        8: None,
        9: 9,     # Clio-shipped
    }

    for c in (6, 7, 9):
        exp = clio_beta_prime.get(c)
        analyze_c(c, expected_beta_prime=exp if exp is not None else -1,
                  amax=24, out_lines=lines)

    # Also 8 for completeness (even c, structural check)
    lines.append("=" * 78)
    lines.append("Also c = 8 (for reference)")
    lines.append("=" * 78)
    analyze_c(8, expected_beta_prime=-1, amax=22, out_lines=lines)

    out = "\n".join(lines)
    print(out)
    with open("/home/agent/projects/code/2026-07-09-v2-Hc-predictions-output.txt", "w") as f:
        f.write(out)


if __name__ == "__main__":
    main()
