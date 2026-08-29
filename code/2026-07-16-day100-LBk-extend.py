"""Day 100 CODE — Empirical LB_k^{(c)} sweep for c ≡ 2 mod 4, c > 11.

Sweeps the FULL shell (a+b ≡ c mod 2) — NOT restricted to Poch-min locus —
to determine the true empirical min of v_2(h_k^{(c)}(a, b)).

Uses three-var factorisation:
    h_k^{(c)}(a, b) = (a+3)_L · (b+2)_L · Q_k(a, b, c),   L = c-1-k.

Q_k for k = 0..6 from catalog `2026-07-11-Qk-catalog.json`.
For k >= 7, extraction pipeline is skipped (too slow within budget).

Verifies whether min_{k<=6} LB_k^{(c)} matches β(c) − D_anchor(c) for
c ∈ {14, 18, 22, 26, 34, 42, 66}.
"""
import json
import time
from math import factorial

from sympy import symbols, sympify, expand, lambdify


# ------------------------------------------------------------------------ #
# 2-adic helpers
# ------------------------------------------------------------------------ #

def v2_int(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def s2(n):
    return bin(int(n)).count('1') if n >= 0 else 0


def v2_pochhammer_via_amm(x, L):
    """v_2((x)_L) where (x)_L = x(x+1)...(x+L-1).

    Uses AMM identity: v_2((x)_L) = L - s_2(x+L-1) + s_2(x-1).
    Requires x >= 1 (otherwise the Pochhammer contains 0 and is 0).
    For x = a+3, L = c-1-k: needs a+3 >= 1 (always true for a >= 0).
    """
    if L <= 0:
        return 0
    if x <= 0:
        # (x)_L contains zero or crosses zero → value is 0 (if L large enough)
        # or a signed product. Handle: if x <= 0 < x+L-1, product includes 0
        if x + L - 1 >= 0:
            return float('inf')
        # else all negative; falls back to Γ ratio, use direct.
        p = 1
        for i in range(L):
            p *= (x + i)
        return v2_int(p)
    # Standard case
    return L - s2(x + L - 1) + s2(x - 1)


# ------------------------------------------------------------------------ #
# β(c), D_anchor(c)
# ------------------------------------------------------------------------ #

def beta(c):
    """β(c) = 2(c-1) - s_2(c-1)."""
    return 2 * (c - 1) - s2(c - 1)


def D_anchor(c):
    """D_anchor(c) = s_2(m) + v_2(m), c = 4m+2.  Only defined for c ≡ 2 mod 4."""
    assert c % 4 == 2, f"D_anchor only for c ≡ 2 mod 4, got c={c}"
    m = (c - 2) // 4
    return s2(m) + v2_int(m)


# ------------------------------------------------------------------------ #
# Load Q_k catalog
# ------------------------------------------------------------------------ #

def load_Q_catalog():
    d = json.load(open('/home/agent/projects/code/2026-07-11-Qk-catalog.json'))
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


# ------------------------------------------------------------------------ #
# LB_k^{(c)} sweep on full shell
# ------------------------------------------------------------------------ #

def compute_LB_k(Q_kabc, c_val, k, T=8, verbose=False):
    """min over (a, b) ∈ [0, 2^T)^2 with a+b ≡ c (mod 2)  of v_2(h_k^{(c)}(a,b)).

    Returns (min_v, [(a, b) achievers])  or  (None, []) if L < 0.

    Also returns v_2 evaluated at (0, 2) specifically (for k=4 diagnostic).
    """
    a_s, b_s, c_s = symbols('a b c')
    L = c_val - 1 - k
    if L < 0:
        return None, [], None

    # Q_k(a, b) at c = c_val, as a lambdified function returning int
    Q_ab = expand(Q_kabc.subs(c_s, c_val))
    f_Q = lambdify((a_s, b_s), Q_ab, modules='math')

    parity = c_val % 2  # need a + b ≡ c mod 2

    N = 1 << T
    min_v = float('inf')
    achievers = []
    val_at_02 = None

    for a in range(N):
        va_poch = v2_pochhammer_via_amm(a + 3, L)  # v_2((a+3)_L)
        if va_poch == float('inf'):
            continue
        for b in range(N):
            if (a + b) % 2 != parity:
                continue
            vb_poch = v2_pochhammer_via_amm(b + 2, L)
            if vb_poch == float('inf'):
                continue
            try:
                Q_val = int(f_Q(a, b))
            except Exception:
                continue
            if Q_val == 0:
                continue
            v = va_poch + vb_poch + v2_int(Q_val)

            if (a, b) == (0, 2):
                val_at_02 = v

            if v < min_v:
                min_v = v
                achievers = [(a, b)]
            elif v == min_v and len(achievers) < 5:
                achievers.append((a, b))

    return min_v, achievers, val_at_02


# ------------------------------------------------------------------------ #
# Main
# ------------------------------------------------------------------------ #

def main():
    print("=" * 78)
    print("Day 100 CODE — Empirical LB_k^{(c)} on FULL shell for c ≡ 2 mod 4")
    print("=" * 78)

    Q_catalog = load_Q_catalog()
    print(f"\nLoaded Q_k(a,b,c) from catalog for k ∈ {sorted(Q_catalog.keys())}")
    print("(Q_k for k >= 7 not in catalog; those k are skipped this run.)")

    c_list = [14, 18, 22, 26, 34, 42, 66]
    k_list = list(range(13))
    T = 8

    results = {}

    for c_val in c_list:
        assert c_val % 4 == 2
        m = (c_val - 2) // 4
        bc = beta(c_val)
        Dc = D_anchor(c_val)
        target = bc - Dc
        print("\n" + "=" * 78)
        print(f"c = {c_val}  (m = {m}),   β(c) = {bc},   D_anchor = {Dc},   "
              f"β − D_anchor = {target}")
        print("=" * 78)

        row = {}
        for k in k_list:
            if k not in Q_catalog:
                # Skip - no Q_k available
                print(f"  k={k}: SKIP (Q_k not in catalog)")
                row[k] = {'LB': None, 'status': 'no_Q_k',
                          'achievers': [], 'val_at_02': None}
                continue
            L = c_val - 1 - k
            if L < 0:
                print(f"  k={k}: SKIP (L = {L} < 0)")
                row[k] = {'LB': None, 'status': 'L_negative',
                          'achievers': [], 'val_at_02': None}
                continue
            t0 = time.time()
            LB, ach, val_02 = compute_LB_k(Q_catalog[k], c_val, k, T=T)
            dt = time.time() - t0
            ach_str = ", ".join(f"({a},{b})" for (a, b) in ach[:3])
            extra = ""
            if k == 4:
                extra = f"    v_2(h_4)(0,2) = {val_02}"
            print(f"  k={k:>2d}: L={L:>3d}, LB = {LB}   "
                  f"min at (a*,b*) ∈ {{{ach_str}}}    [{dt:.1f}s]{extra}")
            row[k] = {'LB': LB, 'status': 'ok',
                      'achievers': [list(x) for x in ach[:5]],
                      'val_at_02': val_02,
                      'L': L}

        # Summary
        good_LBs = [(k, row[k]['LB']) for k in k_list
                    if row[k]['LB'] is not None]
        if good_LBs:
            min_LB = min(lb for _, lb in good_LBs)
            argmin = [k for k, lb in good_LBs if lb == min_LB]
            match = "YES" if min_LB == target else "NO"
            print(f"\n  min_k LB_k = {min_LB}  at k ∈ {argmin}   "
                  f"(target β − D_anchor = {target})   MATCH? {match}")
            row['_summary'] = {'min_LB': min_LB, 'argmin': argmin,
                               'target': target, 'match': match == 'YES'}
        else:
            print("  no data")
            row['_summary'] = {'min_LB': None, 'target': target,
                               'match': None}

        results[c_val] = row

    # Compact table
    print("\n" + "=" * 78)
    print("COMPACT TABLE (LB_k^{(c)} for k = 0..6)")
    print("=" * 78)
    print(f"\n{'c':>4} {'β':>4} {'β-D':>4}  " + " ".join(f"k={k:<3d}" for k in range(7))
          + "   min_k  match")
    for c_val in c_list:
        row = results[c_val]
        bc = beta(c_val)
        Dc = D_anchor(c_val)
        target = bc - Dc
        cells = []
        for k in range(7):
            lb = row[k]['LB'] if row.get(k) else None
            cells.append(f"{lb!s:<4}" if lb is not None else "  - ")
        summary = row.get('_summary', {})
        min_lb = summary.get('min_LB')
        match = summary.get('match')
        match_str = ("YES" if match else "NO ") if match is not None else "?  "
        print(f"{c_val:>4} {bc:>4} {target:>4}  " + " ".join(cells) +
              f"   {min_lb!s:<4}  {match_str}")

    # Verdict
    print("\n" + "=" * 78)
    print("VERDICT (per c)")
    print("=" * 78)
    for c_val in c_list:
        summary = results[c_val].get('_summary', {})
        min_lb = summary.get('min_LB')
        target = summary.get('target')
        match = summary.get('match')
        if match is None:
            print(f"  c={c_val}: NO DATA")
        elif match:
            print(f"  c={c_val}: min_k LB_k = {min_lb} = β − D_anchor = {target}  ✓ MATCH")
        else:
            print(f"  c={c_val}: min_k LB_k = {min_lb} ≠ β − D_anchor = {target}   MISMATCH "
                  f"(min_k is over k ≤ 6 only — mismatch could disappear if k ≥ 7 gives smaller LB)")

    # Save
    out = {
        'note': 'Day 100 empirical LB_k^{(c)} sweep on full shell, c ≡ 2 mod 4.',
        'T': T,
        'c_list': c_list,
        'k_range_computed': [0, 6],
        'results': {str(c): {str(k): v for k, v in row.items()}
                    for c, row in results.items()},
    }
    with open('/home/agent/projects/code/2026-07-16-day100-LBk-extend.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("\nSaved /home/agent/projects/code/2026-07-16-day100-LBk-extend.json")


if __name__ == '__main__':
    main()
