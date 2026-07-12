"""Day 90/91 CODE — Stage 2 pattern analysis on Δ_k^{(c)} / LB_k catalog.

Attempts closed-form fits:
    1. Δ_k^{(c)} = v_2(P_k(c)) for polynomial P_k in c.
    2. Δ_k^{(c)} piecewise in c mod 2^T.
    3. Compare LB_k^{(c)} across parity and shell configurations.
"""
import json
from math import factorial
from sympy import symbols, sympify, expand, factor, Poly

CATALOG = '/home/agent/projects/code/2026-07-12-Delta-k-c-catalog.json'


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
    """Base-2 digit sum."""
    return bin(int(n)).count('1')


def main():
    with open(CATALOG) as f:
        cat_full = json.load(f)
    data = cat_full['data']

    # Reconstruct matrix.
    rows = {}
    for key, entry in data.items():
        # key = 'c{c},k{k}'
        c_str, k_str = key.split(',')
        c = int(c_str[1:])
        k = int(k_str[1:])
        rows[(c, k)] = entry

    c_range = list(range(5, 12))
    max_k = 11
    print("=" * 74)
    print("Δ_k^{(c)} closed-form pattern hunt (Stage 2)")
    print("=" * 74)

    # --- Δ_k as function of c, for each k ---
    print("\n--- Δ_k^{(c)} sequences (c = 5..11), and closed-form checks ---\n")
    for k in range(max_k + 1):
        seq = []
        for c in c_range:
            if (c, k) not in rows:
                seq.append(None)
                continue
            d = rows[(c, k)].get('Delta')
            seq.append(d)
        if all(x is None for x in seq):
            continue
        print(f"k={k:>2d}: Δ_k^{{(c)}} = {seq}")

        # Guess 1: Δ_k = v_2(P_k(c)) where P_k is a polynomial.
        if k == 0:
            # Δ_0 = 0 when locus non-empty
            print("       Guess: Δ_0 = 0 (Poch-min locus non-empty case).")
        elif k == 1:
            # From Q_1 = -c(c-1), Δ_1 = v_2(c(c-1)) always.
            preds = [v2_int(c * (c - 1)) for c in c_range]
            match = seq == preds
            print(f"       Guess: Δ_1 = v_2(c(c-1)) = {preds}  {'MATCH' if match else 'MISS'}")
        elif k == 2:
            # Q_2 = -c(2ab+2a+4b-c^3+4c^2-5c+6). For odd c: v_2(Q_2) = 1?
            preds = []
            for c in c_range:
                if c % 2 == 1:
                    preds.append(1)  # data says uniform 1
                else:
                    preds.append('inf')
            print(f"       Guess: Δ_2 = 1 for odd c, inf for even c: {preds}")
        elif k == 3:
            # Q_3 = c(c-1)(c-2) * (...). Δ_3 includes v_2(c(c-1)(c-2)) + bracket.
            base = [v2_int(c * (c - 1) * (c - 2)) for c in c_range]
            print(f"       v_2(c(c-1)(c-2)) = {base}, so Δ_3 - v_2(base) = {[s - b if s is not None and s != 'inf' else '-' for s, b in zip(seq, base)]}")

    # --- LB_direct patterns ---
    print("\n--- LB_direct = min v_2(h_k) over shell, as sequence in c ---\n")
    for k in range(max_k + 1):
        seq = []
        for c in c_range:
            if (c, k) not in rows:
                seq.append(None)
                continue
            v = rows[(c, k)].get('LB_direct')
            seq.append(v)
        if all(x is None for x in seq):
            continue
        seq_int = [None if x is None or str(x) == 'inf' else int(x) for x in seq]
        print(f"k={k:>2d}: LB_k = {seq_int}")

    print("\n--- min_k LB_direct per c ---\n")
    for c in c_range:
        vals = []
        argmins = []
        for k in range(c):
            if (c, k) in rows:
                v = rows[(c, k)].get('LB_direct')
                if v is not None and str(v) != 'inf':
                    vals.append((k, int(v)))
        if not vals:
            continue
        m = min(v for _, v in vals)
        argmins = [k for k, v in vals if v == m]
        # Predictions
        legendre_c = c - s2(c)
        print(f"  c={c:>2d} (c-1={c-1:>2d}, s_2(c)={s2(c)}, v_2(c!)={legendre_c}): "
              f"β'(c) = {m}, k* ∈ {argmins}")

    # --- try closed form for β'(c) ---
    print("\n--- β'(c) closed-form candidates ---\n")
    beta_prime = {}
    for c in c_range:
        vals = [rows[(c, k)].get('LB_direct') for k in range(c) if (c, k) in rows]
        vals = [int(v) for v in vals if v is not None and str(v) != 'inf']
        if vals:
            beta_prime[c] = min(vals)

    # Candidate A: β'(c_odd) = 3(c-3)/2 for c odd ≥ 5.
    print("Odd c:")
    for c in c_range:
        if c % 2 == 0:
            continue
        pred = 3 * (c - 3) // 2
        print(f"  c={c}: β'={beta_prime[c]}, 3(c-3)/2={pred}   {'MATCH' if pred == beta_prime[c] else 'MISS'}")

    # Candidate B (even c): various
    print("\nEven c candidates:")
    for c in c_range:
        if c % 2 == 1:
            continue
        b = beta_prime[c]
        candidates = {
            'c + v_2((c/2)!)': c + v2_int(factorial(c // 2)),
            '2c - 2s_2(c-1) + v_2(c) - 1': 2 * (c - 1) - 2 * s2(c - 1) + v2_int(c),
            '3(c-2)/2 + 1': 3 * (c - 2) // 2 + 1,
            '2·v_2((c-1)!) + v_2(c)': 2 * (c - 1 - s2(c - 1)) + v2_int(c),
            '2·v_2((c-1)!) + 1': 2 * (c - 1 - s2(c - 1)) + 1,
        }
        matches = {name: v for name, v in candidates.items() if v == b}
        misses = {name: v for name, v in candidates.items() if v != b}
        print(f"  c={c}: β'={b}")
        for name, v in candidates.items():
            print(f"     {name}: {v}  {'✓' if v == b else '✗'}")

    # --- Δ_1 confirmation across parities ---
    print("\n--- Δ_1^{(c)} test: v_2(c(c-1)) hypothesis ---\n")
    for c in c_range:
        d1 = rows[(c, 1)].get('Delta')
        pred = v2_int(c * (c - 1))
        print(f"  c={c}: Δ_1={d1}, v_2(c(c-1))={pred}   {'MATCH' if d1 == pred else 'MISS'}")

    # --- LB_k pattern per c (uniform vs non-uniform) ---
    print("\n--- Uniformity of LB_k^{(c)} across k, per c ---\n")
    for c in c_range:
        vals = [(k, rows[(c, k)].get('LB_direct')) for k in range(c) if (c, k) in rows]
        vals = [(k, int(v)) for k, v in vals if v is not None and str(v) != 'inf']
        vs = [v for _, v in vals]
        if not vs:
            continue
        uniq = sorted(set(vs))
        counts = {u: vs.count(u) for u in uniq}
        print(f"  c={c}: LB values {uniq}, distribution {counts}")

    print("\n--- Δβ'(c) sequential differences ---")
    prev = None
    for c in sorted(beta_prime.keys()):
        b = beta_prime[c]
        if prev is not None:
            dd = b - prev
            # D1 for odd c: 1 - max(2, v_2(c-1))
            d1 = 1 - max(2, v2_int(c - 1)) if c % 2 == 1 else '(even c)'
            print(f"  Δβ'({c}) = β'({c}) - β'({c-1}) = {b} - {prev} = {dd}   D1_pred={d1}")
        prev = b


if __name__ == "__main__":
    main()
