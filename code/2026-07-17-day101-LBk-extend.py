"""Day 101 (2026-07-17) — LB_k^{(c)} extension to k = 7, 8.

Using the fresh Q_7, Q_8 catalog (from qk-catalog.json, Day 100 fits),
extend the LB_k sweep to k = 7, 8 for c ∈ {8, 10, 14, 18, 22, 26, 30}.

LB_k^{(c)} := min_{(a, b) : a+b ≡ c mod 2} v_2(h_k^{(c)}(a, b))
            = min_{(a, b)} [v_2((a+3)_L) + v_2((b+2)_L) + v_2(Q_k(a, b, c))]

where L = c - 1 - k.

Goal: for each k ∈ {7, 8}:
  - Report LB_k^{(c)} for each c in the list.
  - Check if there's a c-uniform closed form.
"""
import json
import time

from sympy import symbols, sympify, expand, lambdify


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
    """v_2((x)_L), x >= 1: AMM identity."""
    if L <= 0:
        return 0
    if x <= 0:
        if x + L - 1 >= 0:
            return float('inf')
        p = 1
        for i in range(L):
            p *= (x + i)
        return v2_int(p)
    return L - s2(x + L - 1) + s2(x - 1)


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


def D_anchor(c):
    """Δ(c) = s_2(m) + v_2(m), c = 4m+2 (c ≡ 2 mod 4)."""
    assert c % 4 == 2, f"only c ≡ 2 mod 4, got c={c}"
    m = (c - 2) // 4
    return s2(m) + v2_int(m)


def load_Q_catalog_extended():
    """Load Q_k from qk-catalog.json (has k=0..8)."""
    d = json.load(open('/home/agent/projects/code/qk-catalog.json'))
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


def compute_LB_k(Q_kabc, c_val, k, T=8):
    """Empirical min over (a, b) ∈ [0, 2^T)^2 with a+b ≡ c mod 2.
    Returns (min_v, achievers[:5], val_at_02)."""
    a_s, b_s, c_s = symbols('a b c')
    L = c_val - 1 - k
    if L < 0:
        return None, [], None
    Q_ab = expand(Q_kabc.subs(c_s, c_val))
    # int-based eval for reliability with huge integer coefs
    from sympy import Poly
    P = Poly(Q_ab, a_s, b_s)
    coeff_dict = {tuple(m): int(c) for m, c in P.as_dict().items()}

    def eval_Q(a, b):
        v = 0
        for (da, db), coef in coeff_dict.items():
            v += coef * (a ** da) * (b ** db)
        return v

    parity = c_val % 2
    N = 1 << T
    min_v = float('inf')
    achievers = []
    val_at_02 = None

    for a in range(N):
        va_poch = v2_pochhammer_via_amm(a + 3, L)
        if va_poch == float('inf'):
            continue
        for b in range(N):
            if (a + b) % 2 != parity:
                continue
            vb_poch = v2_pochhammer_via_amm(b + 2, L)
            if vb_poch == float('inf'):
                continue
            Q_val = eval_Q(a, b)
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


def main():
    print("=" * 78)
    print("Day 101 CODE — LB_k^{(c)} extension to k = 7, 8")
    print("=" * 78)

    Q_catalog = load_Q_catalog_extended()
    print(f"\nLoaded Q_k from qk-catalog.json for k ∈ {sorted(Q_catalog.keys())}")

    c_list = [8, 10, 14, 18, 22, 26, 30]
    k_list = [7, 8]
    T = 8

    results = {}
    for c_val in c_list:
        print(f"\n{'=' * 78}")
        if c_val % 4 == 2:
            bc = beta(c_val)
            Dc = D_anchor(c_val)
            target = bc - Dc
            print(f"c = {c_val}   β(c) = {bc}   D_anchor = {Dc}   β − D_anchor = {target}")
        else:
            bc = beta(c_val)
            print(f"c = {c_val}   β(c) = {bc}   (c not ≡ 2 mod 4; no D_anchor)")
        print("=" * 78)

        row = {}
        for k in k_list:
            L = c_val - 1 - k
            if L < 0:
                print(f"  k={k}: SKIP (L = {L} < 0)")
                row[k] = {'LB': None, 'status': 'L_negative'}
                continue
            if k not in Q_catalog:
                print(f"  k={k}: SKIP (no Q_k)")
                row[k] = {'LB': None, 'status': 'no_Q_k'}
                continue
            t0 = time.time()
            LB, ach, val_02 = compute_LB_k(Q_catalog[k], c_val, k, T=T)
            dt = time.time() - t0
            ach_str = ", ".join(f"({a},{b})" for (a, b) in ach[:5])
            print(f"  k={k:>2d}: L={L:>3d}, LB = {LB}   min at (a,b) ∈ {{{ach_str}}}   "
                  f"val@(0,2) = {val_02}   [{dt:.1f}s]")
            row[k] = {
                'LB': LB, 'status': 'ok', 'L': L,
                'achievers': [list(x) for x in ach[:5]],
                'val_at_02': val_02,
            }
        results[c_val] = row

    # Table
    print("\n" + "=" * 78)
    print("COMPACT TABLE — LB_k^{(c)} for k = 7, 8")
    print("=" * 78)
    print(f"\n{'c':>4}  β(c)  β − D  " + "  ".join(f"LB_{k}" for k in k_list))
    for c_val in c_list:
        row = results[c_val]
        bc = beta(c_val)
        target = (bc - D_anchor(c_val)) if c_val % 4 == 2 else '-'
        cells = []
        for k in k_list:
            lb = row.get(k, {}).get('LB')
            cells.append(f"{lb!s:>4}" if lb is not None else '  - ')
        print(f"{c_val:>4}  {bc:>4}  {target!s:>5}  " + "  ".join(cells))

    # Uniform-form check: any k such that LB_k(c) as a function of c has a
    # simple closed form?  Try LB_k(c) - β(c) and LB_k(c) - c and LB_k(c) - v_2((c-4)).
    print(f"\n{'=' * 78}\nUniform-form probes for LB_k(c) at k=7, 8")
    print(f"{'=' * 78}")
    for k in k_list:
        print(f"\n  k = {k}:")
        print(f"  {'c':>4}  {'LB_k':>5}  {'β(c)':>5}  {'LB_k − β':>9}  {'LB_k − 2c':>10}")
        for c_val in c_list:
            row = results[c_val]
            lb = row.get(k, {}).get('LB')
            bc = beta(c_val)
            if lb is None:
                continue
            print(f"  {c_val:>4}  {lb:>5}  {bc:>5}  {lb - bc:>9}  {lb - 2*c_val:>10}")

    # Save
    out = {
        'note': 'Day 101 LB_k extension to k = 7, 8',
        'date': '2026-07-17',
        'T': T,
        'c_list': c_list,
        'k_list': k_list,
        'results': {str(c): {str(k): v for k, v in row.items()} for c, row in results.items()},
    }
    with open('/home/agent/projects/code/2026-07-17-day101-LBk-extend.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("\nSaved /home/agent/projects/code/2026-07-17-day101-LBk-extend.json")

    txtpath = '/home/agent/projects/code/2026-07-17-day101-LBk-extend.txt'
    with open(txtpath, 'w') as f:
        f.write("Day 101 — LB_k^{(c)} extension to k = 7, 8\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"c_list: {c_list}\n")
        f.write(f"k_list: {k_list}\n")
        f.write(f"T = {T}\n\n")
        f.write(f"{'c':>4}  β(c)  β − D  " + "  ".join(f"LB_{k}" for k in k_list) + "\n")
        for c_val in c_list:
            row = results[c_val]
            bc = beta(c_val)
            target = (bc - D_anchor(c_val)) if c_val % 4 == 2 else '-'
            cells = []
            for k in k_list:
                lb = row.get(k, {}).get('LB')
                cells.append(f"{lb!s:>4}" if lb is not None else '  - ')
            f.write(f"{c_val:>4}  {bc:>4}  {target!s:>5}  " + "  ".join(cells) + "\n")
    print(f"Saved {txtpath}")


if __name__ == '__main__':
    main()
