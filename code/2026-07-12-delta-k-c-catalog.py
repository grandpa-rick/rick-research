"""Day 91 — Compute Delta_k^{(c)} catalog for the LB_k^{(c)} closed-form hunt.

Recap of decomposition (from PROVE, Day 90 structural insight):

For k <= c-1 (clean regime):

    h_k^{(c)}(a, b) = (a+3)_{c-1-k} * (b+2)_{c-1-k} * Q_k(a, b, c)

with L := c - 1 - k. By Kummer/Lucas, min_a v_2((a+3)_L) = v_2(L!), achieved
when (a+2) & L == 0 (bitwise). Similarly (b+1) & L == 0.

    LB_k^{(c)} = 2 * v_2(L!) + Delta_k^{(c)}     [clean regime]

where

    Delta_k^{(c)} := min v_2(Q_k(a, b, c))  over (a, b) satisfying:
                    * (a + b) parity: registry says shell = a+b odd for odd c.
                      general rule from PROVE: a + b + c even.
                      Hmm - looking at c=5,6,7,8,9 witnesses:
                        c=5 witness (3,0,2) a+b=3 odd
                        c=7 witness (1,2,6) a+b=3 odd
                        c=9 witness (7,0,2) a+b=7 odd
                        c=6 witness (0,0,0) a+b=0 even
                        c=8 witness (8,8,2) a+b=16 even
                      So shell parity = c parity (a+b ~ c mod 2).
                    * (a+2) & L == 0  [Lucas-odd for (a+3)_L]
                    * (b+1) & L == 0  [Lucas-odd for (b+2)_L]

For k = c-1, L = 0, empty Pochhammer, Delta_{c-1}^{(c)} = min v_2(Q_{c-1}(a,b,c)).

This script:
  1. Loads Q_k catalog for k = 0..6 (symbolic in a,b,c).
  2. For c in {5..11}, k in {0..min(6, c-1)}, enumerates (a,b) satisfying
     the three constraints in [0, 2^T)^2 for T = 8, computes v_2 of Q_k.
  3. Reports Delta_k^{(c)} as a matrix.
"""
import json
import sys
from sympy import symbols, sympify, factor, expand

CAT_PATH = "/home/agent/projects/code/2026-07-11-Qk-catalog.json"

def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def load_Qk_symbolic():
    """Load Q_k(a, b, c) for k = 0..6 as sympy expressions."""
    with open(CAT_PATH) as f:
        cat = json.load(f)
    Q = {}
    for k_str, s in cat["Q_k_low_k"].items():
        Q[int(k_str)] = sympify(s)
    # k = 6 from extended
    Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])
    return Q


def compute_delta(Q_poly, a_s, b_s, c_s, c_val, k_val, T=6, restrict_to_lucas=True):
    """Compute Delta_k^{(c)} = min v_2(Q_k(a, b, c_val)) over shell x Lucas-odd (a, b).

    Returns (delta, achievers) where achievers is a list of (a, b, val) at min.
    """
    L = c_val - 1 - k_val
    shell_parity = c_val % 2  # a + b ~ c mod 2
    # Substitute c first for speed
    Q_c = Q_poly.subs(c_s, c_val)
    Q_c_expanded = expand(Q_c)
    # Compile as coefficient dict for fast evaluation
    from sympy import Poly
    p = Poly(Q_c_expanded, a_s, b_s)
    coeffs = p.as_dict()  # {(da, db): coeff}
    def eval_Q(av, bv):
        s = 0
        for (da, db), coef in coeffs.items():
            s += int(coef) * (av ** da) * (bv ** db)
        return s

    min_v = float('inf')
    achievers = []
    for a in range(2 ** T):
        if (a + 2) & L != 0 and restrict_to_lucas:
            continue
        for b in range(2 ** T):
            if (a + b) % 2 != shell_parity:
                continue
            if (b + 1) & L != 0 and restrict_to_lucas:
                continue
            val = eval_Q(a, b)
            if val == 0:
                continue
            v = v2(val)
            if v < min_v:
                min_v = v
                achievers = [(a, b, val)]
            elif v == min_v and len(achievers) < 8:
                achievers.append((a, b, val))
    return min_v, achievers


def main():
    print("=" * 78)
    print("Day 91 — Delta_k^{(c)} catalog")
    print("=" * 78)
    Q = load_Qk_symbolic()
    a_s, b_s, c_s = symbols('a b c')
    print()
    print("Loaded Q_k for k = 0..6 (symbolic).")
    print()

    # Sanity check: c=5, k=2 should give Delta = 1 (per PROVE)
    print("Sanity check: c=5, k=2")
    delta52, ach = compute_delta(Q[2], a_s, b_s, c_s, 5, 2, T=6)
    print(f"  Delta_2^{{(5)}} = {delta52}   (expected 1)")
    print(f"  achievers: {ach[:5]}")
    print()

    print("Sanity check: c=9, k=2")
    delta92, ach = compute_delta(Q[2], a_s, b_s, c_s, 9, 2, T=7)
    print(f"  Delta_2^{{(9)}} = {delta92}   (expected 1)")
    print(f"  achievers: {ach[:5]}")
    print()

    # Full catalog
    print()
    print("=" * 78)
    print("FULL CATALOG   Delta_k^{(c)}   (T = 7)")
    print("=" * 78)
    header = "     " + "  ".join(f"c={c:>2d}" for c in range(5, 12))
    print(header)

    rows = {}
    for k in range(7):
        row = []
        for c in range(5, 12):
            if k > c - 1:
                row.append("  -  ")
                continue
            # Choose T large enough: need L < 2^T so Lucas constraint doesn't kill everything
            L = c - 1 - k
            T = max(7, L.bit_length() + 2)
            delta, _ = compute_delta(Q[k], a_s, b_s, c_s, c, k, T=T)
            if delta == float('inf'):
                row.append("  inf")
            else:
                row.append(f"  {delta:>2d} ")
        rows[k] = row
        print(f"k={k}: " + "  ".join(row))

    # Also compute LB_k = 2*v_2(L!) + Delta_k for each (c, k), then min_k
    print()
    print("=" * 78)
    print("LB_k^{(c)}   =   2 * v_2(L!) + Delta_k^{(c)}   [clean regime, k<=c-1]")
    print("=" * 78)
    print(header)
    from math import factorial

    lbs = {}
    for k in range(7):
        row = []
        for c in range(5, 12):
            if k > c - 1:
                row.append("  -  ")
                continue
            L = c - 1 - k
            T = max(7, L.bit_length() + 2)
            delta, _ = compute_delta(Q[k], a_s, b_s, c_s, c, k, T=T)
            if delta == float('inf'):
                row.append("  inf")
                continue
            lb = 2 * v2(factorial(L)) + delta
            lbs[(c, k)] = lb
            row.append(f"  {lb:>2d} ")
        print(f"k={k}: " + "  ".join(row))

    # For each c, find min_k LB_k
    print()
    print("=" * 78)
    print("min_k LB_k^{(c)}  vs  target beta'(c)")
    print("=" * 78)
    beta_prime = {5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14, 11: None}
    print(f"{'c':>3s}  {'min_k LB':>10s}  {'argmin k':>10s}  {'target':>8s}  match?")
    for c in range(5, 12):
        cand = [(k, lbs.get((c, k))) for k in range(7) if k <= c-1 and lbs.get((c, k)) is not None]
        if not cand:
            continue
        mk, mlb = min(cand, key=lambda x: x[1])
        tgt = beta_prime.get(c)
        mtch = "?" if tgt is None else ("MATCH" if mlb == tgt else "MISMATCH")
        print(f"{c:>3d}  {mlb:>10d}  {mk:>10d}  {str(tgt):>8s}  {mtch}")


if __name__ == "__main__":
    main()
