"""Day 86 CODE Task 4 — c=6 and c=7 falsification predictions for Clio.

We predict M_j(a, b, c) for c ∈ {6, 7}, j ∈ {1, 2, 3, 4}, and (a, b) values
by evaluating the Q_j(a, b, c) closed forms (Task 1) as:

    M_j(a, b, c) = f^(a,b,c) · Q_j(a, b, c) / (n)_{2j},  where n = a+b+c.

These are integer predictions Clio can attack directly with her code.
If any single prediction fails, either:
  (i) the c-uniform Sym-side identification is wrong, or
  (ii) her M_j oracle disagrees with the Kostka-Aitken derivation.
Either way, we want to know.

Output: 2026-07-08-Mj-cgt5-predictions.txt — plain table with the numbers.
"""
from math import factorial as pyfact
from fractions import Fraction
from sympy import symbols, Matrix, simplify, expand
from collections import defaultdict


a, b, c = symbols('a b c')


# ---------------------------------------------------------------------------
# Recompute Q_j symbolically (small j).
# ---------------------------------------------------------------------------

def falling(x, k):
    p = 1
    for i in range(k):
        p *= (x - i)
    return p


def det_mu_3row(mu, lam=(a, b, c)):
    xs = [lam[0] + 2, lam[1] + 1, lam[2]]
    ks = [mu[j] + (2 - j) for j in range(3)]
    return Matrix([[falling(xs[i], ks[j]) for j in range(3)] for i in range(3)]).det()


D0 = det_mu_3row((0, 0, 0))


def add_v2_strip(mu, max_rows=4):
    mu = list(mu) + [0] * max_rows
    out = []
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
            out.append(tuple(x for x in v2 if x > 0))
    return out


def e2_power_kostka(j, max_rows=3):
    current = defaultdict(int)
    current[tuple()] = 1
    for _ in range(j):
        nxt = defaultdict(int)
        for mu, k in current.items():
            for nu in add_v2_strip(mu):
                nxt[nu] += k
        current = nxt
    return {mu: k for mu, k in current.items() if len(mu) <= max_rows}


def Q_j_symbolic(j):
    if j == 0:
        return 1
    table = e2_power_kostka(j)
    num = 0
    for mu, k in table.items():
        mu3 = tuple(list(mu) + [0] * (3 - len(mu)))
        num += k * det_mu_3row(mu3)
    return expand(simplify(num / D0))


# ---------------------------------------------------------------------------
# f^lambda via hook length.
# ---------------------------------------------------------------------------

def f_lambda(lam):
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    # Must be a valid partition (non-increasing).
    for i in range(len(lam) - 1):
        if lam[i] < lam[i + 1]:
            return None
    n = sum(lam)
    cols = [0] * lam[0]
    for i, li in enumerate(lam):
        for j in range(li):
            cols[j] += 1
    h = 1
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = cols[j] - i - 1
            h *= (arm + leg + 1)
    return pyfact(n) // h


def falling_int(n, k):
    r = 1
    for i in range(k):
        r *= (n - i)
    return r


# ---------------------------------------------------------------------------
# Predict M_j(a, b, c) = f^lam · Q_j(a, b, c) / (n)_{2j}.
# ---------------------------------------------------------------------------

def M_j_predict(av, bv, cv, j, Qj):
    if av < bv or bv < cv:
        return None
    Qj_val = int(Qj.subs([(a, av), (b, bv), (c, cv)]))
    f = f_lambda([av, bv, cv])
    if f is None:
        return None
    n = av + bv + cv
    fall = falling_int(n, 2 * j)
    if fall == 0:
        return None
    x = Fraction(f * Qj_val, fall)
    if x.denominator != 1:
        return None
    return int(x)


def main():
    # Precompute Q_j for j = 0..6.
    Q = {}
    for j in range(0, 7):
        Q[j] = Q_j_symbolic(j)
        print(f"  computed Q_{j}(a, b, c)")

    lines = []
    lines.append("=" * 78)
    lines.append("Day 86 — M_j PREDICTIONS at c ∈ {6, 7} for Clio")
    lines.append("=" * 78)
    lines.append("")
    lines.append("Predicted via M_j(a, b, c) = f^(a,b,c) * Q_j(a, b, c) / (n)_{2j}.")
    lines.append("Q_j closed forms — see 2026-07-08-Q_j-closed-forms.txt.")
    lines.append("")
    lines.append("If Clio's independent M_j at c=6 or c=7 disagrees with ANY value below,")
    lines.append("the c-uniform identification is FALSIFIED at that (a, b, c, j).")
    lines.append("")
    lines.append("Table columns: shape λ = (a, b, c), j, predicted M_j.")
    lines.append("")

    # Pick a modest grid of (a, b) values for each c. Require a >= b >= c.
    for cv in (6, 7):
        test_ab = [(a_, b_) for a_ in range(cv, cv + 10)
                            for b_ in range(cv, min(a_, cv + 7) + 1)]
        lines.append("")
        lines.append("-" * 78)
        lines.append(f"c = {cv}")
        lines.append("-" * 78)
        lines.append(f"{'a':>4s} {'b':>4s} {'c':>4s} {'j':>3s} | {'M_j predicted':>18s}")
        lines.append("-" * 50)
        for (av, bv) in test_ab:
            if (av + bv + cv) % 2 != 0:
                # Parity constraint for M_j to be a well-formed skew count only
                # applies to some of the M_j-oracle setups; we still list.
                pass
            for j in range(1, 5):
                pred = M_j_predict(av, bv, cv, j, Q[j])
                if pred is None:
                    lines.append(f"{av:>4d} {bv:>4d} {cv:>4d} {j:>3d} | {'(nonint)':>18s}")
                else:
                    lines.append(f"{av:>4d} {bv:>4d} {cv:>4d} {j:>3d} | {pred:>18d}")
        lines.append("")

    # Also emit the CLOSED-FORM Q_j(a, b, 6) and Q_j(a, b, 7) for j = 1..4 to
    # be used symbolically.
    lines.append("=" * 78)
    lines.append("Symbolic Q_j(a, b, c) at c ∈ {6, 7}, j = 1..4")
    lines.append("=" * 78)
    for cv in (6, 7):
        lines.append(f"\n--- c = {cv} ---")
        for j in range(1, 5):
            Qval = expand(Q[j].subs(c, cv))
            lines.append(f"  Q_{j}(a, b, {cv}) =")
            lines.append(f"    {Qval}")

    out = "\n".join(lines)
    print(out)
    with open("/home/agent/projects/code/2026-07-08-Mj-cgt5-predictions.txt", "w") as f:
        f.write(out)
    print("\nWritten: /home/agent/projects/code/2026-07-08-Mj-cgt5-predictions.txt")


if __name__ == "__main__":
    main()
