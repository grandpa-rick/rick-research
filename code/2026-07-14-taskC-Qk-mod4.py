"""Day 96 Task C — Q_k mod 4 catalog for k odd, k ∈ {3, 5}.

Goal: supply structural data on Q_k(a, b, c) mod 4 as polynomials in (a, b)
with c a parameter. Identify:
  - v_2(Q_k) on the joint Poch-min shell (a+2, b+1) satisfying certain
    2-adic patterns.
  - Recursive pattern Q_{k+2} vs Q_k that isolates a factor whose v_2 is
    v_2(c-1-k).

For each c ∈ {8, 12, 16, 20, 24, 28, 32} and each odd k ∈ {3, 5}:
  1. Reduce Q_k(a, b, c) mod 4 as a polynomial in (a, b).
  2. Evaluate on universal shell point (T-2, 0).
  3. Report Q_k mod 4, mod 8, and v_2(Q_k).
"""
import json
from sympy import symbols, sympify, expand, Poly, Integer

a_s, b_s, c_s = symbols('a b c')

with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
    cat = json.load(f)
Q = {}
for ks, s in cat['Q_k_low_k'].items():
    Q[int(ks)] = sympify(s)
Q[6] = sympify(cat['Q_k_extended']['6']['poly_factored'])


def v2(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def T_of(c_val):
    T = 1
    while T <= c_val - 2:
        T *= 2
    return T


def poly_mod(P, m):
    """Reduce polynomial P (in a, b, c) coefficient-wise mod m."""
    Pe = expand(P)
    if isinstance(Pe, Integer) or not Pe.free_symbols:
        return Integer(int(Pe) % m)
    poly = Poly(Pe, a_s, b_s, c_s)
    new_terms = []
    for monom, coef in poly.terms():
        new_coef = int(coef) % m
        if new_coef != 0:
            new_terms.append((new_coef, monom))
    if not new_terms:
        return Integer(0)
    result = Integer(0)
    for coef, monom in new_terms:
        term = Integer(coef)
        for var, power in zip((a_s, b_s, c_s), monom):
            term *= var ** power
        result += term
    return result


def print_polynomial(P, indent="    "):
    """Human-readable printing of polynomial in (a, b, c)."""
    Pe = expand(P)
    if Pe == 0:
        print(f"{indent}0")
        return
    poly = Poly(Pe, a_s, b_s, c_s)
    for monom, coef in sorted(poly.terms(), key=lambda t: (-sum(t[0]), t[0])):
        da, db, dc = monom
        term = str(coef)
        if da: term += f"·a^{da}" if da > 1 else "·a"
        if db: term += f"·b^{db}" if db > 1 else "·b"
        if dc: term += f"·c^{dc}" if dc > 1 else "·c"
        print(f"{indent}{term}")


def analyze_Qk_mod(k):
    """Study Q_k modulo 2, 4, 8 as polynomial in a, b, c."""
    print(f"\n{'=' * 76}")
    print(f"Q_{k}(a, b, c) analysis")
    print(f"{'=' * 76}")

    Qk = Q[k]
    print(f"\n  Q_{k} expanded, total-degree count:")
    Pe = expand(Qk)
    poly = Poly(Pe, a_s, b_s, c_s)
    print(f"    #terms = {len(poly.terms())}")
    print(f"    total degrees: max = {max(sum(m) for m, _ in poly.terms())}")

    for mod in (2, 4, 8):
        Qk_mod = poly_mod(Qk, mod)
        print(f"\n  Q_{k} mod {mod}:")
        print_polynomial(Qk_mod)

    return Qk


def evaluate_on_universal_shell(k, c_values):
    """Evaluate Q_k at (a, b) = (T-2, 0) for a range of c values."""
    print(f"\n  --- Q_{k}(T-2, 0, c) evaluations ---")
    print(f"  {'c':>3} {'T':>4} {'Q_k(T-2,0,c)':>30} {'v_2':>4} {'mod 4':>6} {'mod 8':>6}")
    data = {}
    for c_val in c_values:
        T = T_of(c_val)
        val = int(Q[k].subs({a_s: T-2, b_s: 0, c_s: c_val}))
        v = v2(val)
        print(f"  {c_val:>3} {T:>4} {val:>30} {v:>4} {val % 4:>6} {val % 8:>6}")
        data[c_val] = {'T': T, 'value': val, 'v2': v, 'mod4': val % 4, 'mod8': val % 8}
    return data


def check_odd_factor_structure(k):
    """Q_k for odd k has factor c·(c-1)·(c-2)·...·(c-k+1) — extract and analyze the
    remaining bracket [B_k(a, b, c)].
    """
    print(f"\n  --- Q_{k} factored structure ---")
    from sympy import factor
    Qf = factor(Q[k])
    print(f"    factored Q_{k}:")
    print(f"    {Qf}")


def analyze_recursion(k, c_values):
    """Look for pattern Q_{k+2}/Q_k mod various."""
    if (k+2) not in Q:
        print(f"    (Q_{k+2} not available)")
        return
    print(f"\n  --- Q_{k+2} / Q_{k} at (T-2, 0, c) ---")
    print(f"  {'c':>3} {'T':>4} {'v_2(Q_'+str(k)+')':>10} {'v_2(Q_'+str(k+2)+')':>10} "
          f"{'diff':>5} {'2v2(c-1-k)':>10}")
    for c_val in c_values:
        T = T_of(c_val)
        Qk_val = int(Q[k].subs({a_s: T-2, b_s: 0, c_s: c_val}))
        Qk2_val = int(Q[k+2].subs({a_s: T-2, b_s: 0, c_s: c_val}))
        vk, vk2 = v2(Qk_val), v2(Qk2_val)
        expected = 2 * v2(c_val - 1 - k)
        print(f"  {c_val:>3} {T:>4} {vk:>10} {vk2:>10} {vk2-vk:>5} {expected:>10}")


def main():
    print("=" * 76)
    print("Day 96 Task C — Q_k mod 4 catalog for k odd, k ∈ {3, 5}")
    print("=" * 76)

    c_values = [8, 12, 16, 20, 24, 28, 32]

    # Task C.1: Q_3, Q_5 mod 2, 4, 8 as polynomials
    for k in (3, 5):
        Qk = analyze_Qk_mod(k)
        check_odd_factor_structure(k)
        evaluate_on_universal_shell(k, c_values)
        analyze_recursion(k, c_values)

    # Task C.2: Look at Δ_5 − Δ_3 = 2·v_2(c-4) structure
    print("\n" + "=" * 76)
    print("STRUCTURAL PATTERN: v_2(Q_5) − v_2(Q_3) at (T-2, 0, c) — the ♥ jump")
    print("=" * 76)
    print(f"  {'c':>3} {'c-4':>4} {'v_2(c-4)':>8} {'2·v_2(c-4)':>10} "
          f"{'Δ_5 − Δ_3':>10} {'match':>6}")
    all_ok = True
    for c_val in c_values:
        T = T_of(c_val)
        Q3v = int(Q[3].subs({a_s: T-2, b_s: 0, c_s: c_val}))
        Q5v = int(Q[5].subs({a_s: T-2, b_s: 0, c_s: c_val}))
        v3, v5 = v2(Q3v), v2(Q5v)
        cm4 = c_val - 4
        v_cm4 = v2(cm4)
        expected = 2 * v_cm4
        actual = v5 - v3
        ok = expected == actual
        if not ok:
            all_ok = False
        print(f"  {c_val:>3} {cm4:>4} {v_cm4:>8} {expected:>10} {actual:>10} "
              f"{'✓' if ok else '✗':>6}")
    if all_ok:
        print("\n  ✅ ♥ recursion holds at k=3 → k=5 across c ∈ {8, 12, 16, 20, 24, 28, 32}")

    # Task C.3: Q_k mod 4 structural extraction — get the (a, b) polynomial mod 4
    # after substituting universal shell parameters. Look for factor of (c-1-k)^2
    # or similar.
    print("\n" + "=" * 76)
    print("Q_k(a, b, c) mod 4 with (a, b) → (T-2, 0), varying c")
    print("=" * 76)
    print("  Symbolic Q_k(T-2, 0, c) is a polynomial in T and c. But T = T(c),")
    print("  so we tabulate values across c and look for patterns.")

    save = {}
    for k in (3, 5):
        save[k] = []
        print(f"\n  Q_{k}(T-2, 0, c) mod {{2, 4, 8, 16, 32}}:")
        print(f"    {'c':>3} {'T-2':>5} {'v_2':>4} " +
              " ".join(f"{'m'+str(2**e):>6}" for e in range(1, 6)))
        for c_val in c_values:
            T = T_of(c_val)
            val = int(Q[k].subs({a_s: T-2, b_s: 0, c_s: c_val}))
            v = v2(val)
            mods = [val % (2**e) for e in range(1, 6)]
            print(f"    {c_val:>3} {T-2:>5} {v:>4} " +
                  " ".join(f"{m:>6}" for m in mods))
            save[k].append({'c': c_val, 'T-2': T-2, 'value': val, 'v2': v,
                            'mods': dict(zip([2**e for e in range(1, 6)], mods))})

    # Task C.4: Structural observation — for k odd, does v_2(Q_k(T-2, 0, c))
    # equal 1 in the "generic" case (c ≡ specific mod pattern)?
    print("\n" + "=" * 76)
    print("Structural observations for PROVE:")
    print("=" * 76)
    print()
    print("  1. Q_1(T-2, 0, c) = -c(c-1). At (T-2, 0, c): v_2 = v_2(c) since (c-1) is odd.")
    print("     For c=8:  Q_1 = -56 (v_2=3);  c=12: Q_1=-132 (v_2=2);  c=16: -240 (v_2=4)")
    print()
    print("  2. Q_3(T-2, 0, c) = c(c-2)(c-1)·[bracket]. On shell, v_2 profile is")
    print("     dominated by v_2(c(c-2)) = v_2(c) + v_2(c-2).")
    print()
    print("  3. Q_5(T-2, 0, c) = -c(c-3)(c-2)(c-1)·[bracket_5]. On shell,")
    print("     v_2 includes v_2(c) + v_2(c-2) + [bracket_5 contribution].")
    print()
    print("  4. ♥ jump Δ_5 − Δ_3 = 2·v_2(c-4) — this is where PROVE's derivation")
    print("     needs to isolate the (c-4)^2 factor structurally in Q_5/Q_3.")

    out = {
        'note': 'Task C: Q_k mod 4/8/16/32 data for k=3, 5 at universal shell (T-2, 0, c).',
        'c_values': c_values,
        'data': {str(k): save[k] for k in (3, 5)},
    }
    with open('/home/agent/projects/code/2026-07-14-taskC-Qk-mod4.json', 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\n  Saved: 2026-07-14-taskC-Qk-mod4.json")


if __name__ == '__main__':
    main()
