"""Day 85 — M_j harvester.

Task: given c, (a, b), j, return M_j(a, b, c) as an exact integer, using
Clio's Lemma-1 template with uniform constants:

    alpha = c - 2, gamma = c - 1, beta = c + 1,
    delta = {1..c}, const = c!.

Clio's Lemma 1 (the inversion identity):

    M_j(a,b,c) = [ C(2(m-j), b-j) * (a - b + 1) * Q_c(a,b,j) ]
               / [ c! * (a + beta - j) * prod_{i in delta}(b + i - j) ]

with m = (a + b + c) / 2 and

    Q_c(a,b,j) = (a - alpha)*(b - gamma)*H_c(a,b,j) - (2c)! * C(j, 2c).

For c = 5 we have H_5 in closed form (verified in
`2026-07-08-Mj-hook-verify.py`). For c > 5, H_c is not yet known symbolically —
the harvester leaves H_c as a callable hook so we can plug in a polynomial
when Clio (or the reverse-engineering pipeline) produces one.

Sanity: M_0(a, b, c) must equal f^{(a, b, c)} by the hook-length formula.
This is the ONE identity we can verify at any c without knowing H_c, because
at j = 0 the C(j, 2c) tip term vanishes and the template reduces to a fixed
combinatorial expression. Well, kind of — even at j = 0 we need H_c(a,b,0),
which for c > 5 we don't have. So for c > 5, the sanity check is instead:

    M_0(a, b, c) := f^{(a, b, c)} (definition via hook-length)

For c = 5 we verify that Clio's Lemma-1 M_0 matches f^lambda across the sweep.
"""
from math import factorial
import csv
import os


# ------------------------------------------------------------
# Basic combinatorics
# ------------------------------------------------------------

def C(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def s2(n): return bin(n).count('1')


def v2(n):
    if n == 0:
        return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def hook_length(lam):
    """f^lambda via the hook-length formula."""
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
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


# ------------------------------------------------------------
# Clio's Lemma 1 template constants (uniform in c)
# ------------------------------------------------------------

def template_constants(c):
    """(alpha, gamma, beta, delta, const) for Clio's Lemma 1 at row-3 length c."""
    alpha = c - 2
    gamma = c - 1
    beta = c + 1
    delta = list(range(1, c + 1))
    const = factorial(c)
    return alpha, gamma, beta, delta, const


# ------------------------------------------------------------
# H_c(a, b, j) providers
# ------------------------------------------------------------

def H5(a, b, j):
    """Clio's H_5 polynomial (verified). Sum_{k=0..8} h_k * C(j, k)."""
    h0 = (a + 3) * (a + 4) * (a + 5) * (a + 6) * (b + 2) * (b + 3) * (b + 4) * (b + 5)
    h1 = -20 * (a + 3) * (a + 4) * (a + 5) * (b + 2) * (b + 3) * (b + 4)
    h2 = -10 * (a + 3) * (a + 4) * (b + 2) * (b + 3) * (a * b + a + 2 * b - 22)
    h3 = 360 * (a + 3) * (b + 2) * (a * b + a + 2 * b - 2)
    h4 = 240 * (a * a * b * b + a * a * b + 3 * a * b * b - 15 * a * b - 18 * a + 2 * b * b - 34 * b - 24)
    h5 = -7200 * (a * b + b - 2)
    h6 = -7200 * (a * b - a - 6)
    h7 = 100800
    h8 = 201600
    hs = [h0, h1, h2, h3, h4, h5, h6, h7, h8]
    return sum(hs[k] * C(j, k) for k in range(9))


HC_PROVIDERS = {
    5: H5,
}


# ------------------------------------------------------------
# M_j via Clio's Lemma 1 (inversion identity)
# ------------------------------------------------------------

def M_j_via_template(a, b, c, j, Hc):
    """M_j(a, b, c) exactly, given H_c(a, b, j) as a callable."""
    if (a + b + c) % 2 != 0:
        return None
    if a < b or b < c or c < 1:
        return None
    alpha, gamma, beta, delta, const = template_constants(c)
    m = (a + b + c) // 2
    N = 2 * (m - j)
    if N < 0:
        # No shape of this size — M_j vanishes.
        return 0
    tip = factorial(2 * c) * C(j, 2 * c)
    Q = (a - alpha) * (b - gamma) * Hc(a, b, j) - tip
    den = const * (a + beta - j)
    for d in delta:
        den *= (b + d - j)
    if den == 0:
        return None
    num = C(N, b - j) * (a - b + 1) * Q
    if num % den != 0:
        return None
    return num // den


def M_j(a, b, c, j):
    """Wrapper: dispatches to M_j via H_c if we have it, else falls back."""
    if c in HC_PROVIDERS:
        return M_j_via_template(a, b, c, j, HC_PROVIDERS[c])
    if j == 0:
        # M_0 is always f^lambda via the hook-length formula.
        if a >= b >= c >= 1:
            return hook_length([a, b, c])
        return None
    return None  # No H_c provider — can't compute M_j for j > 0.


# ------------------------------------------------------------
# Sanity: M_0(a, b, c) = f^(a, b, c) sweep
# ------------------------------------------------------------

def sanity_M0(c, a_max=18, b_max=14, quiet=False):
    """Verify M_0 = hook-length across the (a, b) sweep. Returns (ok, mismatches)."""
    mismatches = []
    checked = 0
    for a in range(c, a_max + 1):
        for b in range(c, min(a, b_max) + 1):
            if (a + b + c) % 2 != 0:
                continue
            f_lam = hook_length([a, b, c])
            M0 = M_j(a, b, c, 0)
            checked += 1
            if M0 != f_lam:
                mismatches.append((a, b, M0, f_lam))
                if not quiet:
                    print(f"  MISMATCH (a,b,c)=({a},{b},{c}): M_0={M0}, f^lambda={f_lam}")
    if not quiet:
        print(f"Sanity M_0 = f^lambda at c={c}: {checked} shapes checked, "
              f"{len(mismatches)} mismatches.")
    return len(mismatches) == 0, mismatches


# ------------------------------------------------------------
# Tabulation: sweep (a, b) for j in {0..8} at fixed c
# ------------------------------------------------------------

def tabulate(c, a_max=20, b_max=16, j_max=8, out_csv=None):
    """Sweep (a, b) at fixed c, compute M_j for j=0..j_max. Write CSV."""
    rows = []
    for a in range(c, a_max + 1):
        for b in range(c, min(a, b_max) + 1):
            if (a + b + c) % 2 != 0:
                continue
            f_lam = hook_length([a, b, c])
            row = {'c': c, 'a': a, 'b': b, 'f_lambda': f_lam}
            for j in range(j_max + 1):
                row[f'M_{j}'] = M_j(a, b, c, j)
            rows.append(row)
    if out_csv:
        os.makedirs(os.path.dirname(out_csv), exist_ok=True) if os.path.dirname(out_csv) else None
        fieldnames = ['c', 'a', 'b', 'f_lambda'] + [f'M_{j}' for j in range(j_max + 1)]
        with open(out_csv, 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote {len(rows)} rows to {out_csv}")
    return rows


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

if __name__ == '__main__':
    print("=" * 70)
    print("Task 1 — M_j harvester at c = 5")
    print("=" * 70)

    print("\n[Sanity] M_0(a, b, 5) = f^(a, b, 5) sweep")
    print("-" * 70)
    ok, bad = sanity_M0(5, a_max=20, b_max=16)
    assert ok, f"M_0 sanity failed: {bad}"

    print("\n[Tabulate] (a, b) sweep, j = 0..8, c = 5")
    print("-" * 70)
    rows = tabulate(5, a_max=20, b_max=16, j_max=8,
                    out_csv='/home/agent/projects/code/2026-07-09-Mj-harvest/Mj_c5.csv')

    def fmt(x, w=18):
        return f"{x:>{w}d}" if isinstance(x, int) else f"{'--':>{w}s}"

    print("\nFirst 10 rows:")
    print(f"{'a':>3s} {'b':>3s} " + " ".join(f'{f"M_{j}":>18s}' for j in range(9)))
    for r in rows[:10]:
        print(f"{r['a']:>3d} {r['b']:>3d} " + " ".join(fmt(r[f'M_{j}']) for j in range(9)))

    # v_2 profile — this is what feeds PROVE Step P1.
    print("\n[v2 profile] v_2(M_j) at c = 5, (a, b) sweep, j = 0..8")
    print("-" * 70)
    print(f"{'(a,b)':>10s} | " + " ".join(f'{f"v2(M_{j})":>10s}' for j in range(9)))
    for r in rows:
        line = f"({r['a']:>2d},{r['b']:>2d})".rjust(10)
        vs = " ".join(f"{v2(r[f'M_{j}']):>10d}" if r[f'M_{j}'] not in (0, None) else f"{'inf':>10s}" for j in range(9))
        print(f"{line} | {vs}")

    # Min v_2 sweep — this is beta'(5)
    print("\n[beta'(5)] min over (a,b) and j of v_2(M_j(a,b,5))")
    print("-" * 70)
    min_v = None
    min_at = None
    for r in rows:
        for j in range(9):
            mj = r[f'M_{j}']
            if mj in (0, None):
                continue
            vj = v2(mj)
            if min_v is None or vj < min_v:
                min_v = vj
                min_at = (r['a'], r['b'], j)
    print(f"  min v_2(M_j) = {min_v} achieved at (a, b, j) = {min_at}")
    print(f"  (Compare: Clio's beta'(5) = 3.)")
