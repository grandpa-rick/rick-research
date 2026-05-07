"""
For B_2: decompose KL^{B_2}_{lam,mu}(q,t) as a signed sum over W of
bigraded Verma weight-mu pieces.

By the WCF / Kostant identity:
  KL_{lam,mu}(q,t) = sum_w (-1)^w K_{q,t}(w·lam - mu)
                   = sum_w (-1)^w dim_{q,t} M(w·lam)_mu

For each (lam, mu), enumerate all w in W(B_2) and report the support
of each M(w·lam)_mu in (q,t)-bidegrees. This makes visible WHICH
bidegrees cancel and WHICH leave a residual (positive or negative).
"""

from fractions import Fraction
from collections import defaultdict


def weyl_B2():
    out = []
    # Use signed permutations + length
    # encode w by (s1, s2, sigma) and compute length = number of positive roots sent to negative.
    pos_roots = [(1, -1), (1, 1), (0, 1), (1, 0)]  # (long, long, short, short)
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            for sig in [(0, 1), (1, 0)]:
                if sig == (0, 1):
                    def w(v, s1=s1, s2=s2):
                        return (s1 * v[0], s2 * v[1])
                else:
                    def w(v, s1=s1, s2=s2):
                        return (s1 * v[1], s2 * v[0])
                # length: count positive roots whose image is negative
                length = sum(1 for r in pos_roots
                             if (lambda im: (im[0], im[1]) < (0, 0) if im[0] != 0 else im[1] < 0)(w(r)))
                # Use a cleaner length: compare lex?
                # Alternative: length = number of w in W expressed... easier: build W from generators.
                out.append((w, length, (s1, s2, sig)))
    return out


def length_B2_via_inversions(w_func):
    """Length = #(positive roots that w sends to negative root)."""
    # In B_2, positive roots in bottom-up order: (0,1), (1,0), (1,-1), (1,1).
    pos_roots = [(0, 1), (1, 0), (1, -1), (1, 1)]
    cnt = 0
    for r in pos_roots:
        wr = w_func(r)
        # Negative root means -wr is positive. List of positive roots above.
        if wr in [(0, -1), (-1, 0), (-1, 1), (-1, -1)]:
            cnt += 1
    return cnt


def weyl_B2_v2():
    out = []
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            for sig in [(0, 1), (1, 0)]:
                if sig == (0, 1):
                    def w(v, s1=s1, s2=s2):
                        return (s1 * v[0], s2 * v[1])
                else:
                    def w(v, s1=s1, s2=s2):
                        return (s1 * v[1], s2 * v[0])
                length = length_B2_via_inversions(w)
                out.append((w, length, (s1, s2, sig)))
    return out


def kostant_qt_B2(beta):
    """Return dict (q-deg, t-deg) -> count for K_{q,t}(beta) for B_2."""
    out = defaultdict(int)
    # Allow Fraction inputs; check integer
    bx, by = beta[0], beta[1]
    try:
        bx_i = int(bx)
        by_i = int(by)
    except (TypeError, ValueError):
        return {}
    if bx != bx_i or by != by_i:
        return {}
    x, y = bx_i, by_i
    if x < 0:
        return {}
    # a + b + d = x, c = a - b + y (need c, d >= 0)
    # d = x - a - b
    for a in range(x + 1):
        for b in range(x + 1 - a):
            d = x - a - b
            c = a - b + y
            if c >= 0 and d >= 0:
                out[(a + b, c + d)] += 1
    return dict(out)


def fmt_qt(d):
    if not d:
        return "0"
    parts = []
    for (qd, td), c in sorted(d.items()):
        if qd == 0 and td == 0:
            mon = "1"
        elif qd == 0:
            mon = "t" if td == 1 else f"t^{td}"
        elif td == 0:
            mon = "q" if qd == 1 else f"q^{qd}"
        else:
            qmon = "q" if qd == 1 else f"q^{qd}"
            tmon = "t" if td == 1 else f"t^{td}"
            mon = qmon + tmon
        parts.append(f"{c}*{mon}" if c != 1 else mon)
    return " + ".join(parts)


def w_label(s1, s2, sig):
    map_ = {(1, 1, (0, 1)): "e",
            (-1, 1, (0, 1)): "s2 s1 s2",
            (1, -1, (0, 1)): "s2",
            (-1, -1, (0, 1)): "s1 s2 s1 s2 (= w_0)",
            (1, 1, (1, 0)): "s1",
            (-1, 1, (1, 0)): "s1 s2 s1",
            (1, -1, (1, 0)): "s2 s1",
            (-1, -1, (1, 0)): "s1 s2"}
    return map_[(s1, s2, sig)]


def decompose_kl(lam, mu):
    rho = (Fraction(3, 2), Fraction(1, 2))
    lr = (Fraction(lam[0]) + rho[0], Fraction(lam[1]) + rho[1])
    mr = (Fraction(mu[0]) + rho[0], Fraction(mu[1]) + rho[1])

    print(f"\n=== KL^{{B_2}}_{{{lam},{mu}}}(q,t) decomposition by Weyl element ===")
    print(f"  λ+ρ = {tuple(map(str, lr))},  μ+ρ = {tuple(map(str, mr))}")
    print()
    print(f"  {'w':<25} {'len':<5} {'sign':<6} {'w(λ+ρ)-(μ+ρ)':<18} {'M(w·λ)_μ in (q,t)':<40}")
    print("  " + "-" * 100)
    chi = defaultdict(int)
    for w, length, (s1, s2, sig) in weyl_B2_v2():
        wlr = w(lr)
        diff = (wlr[0] - mr[0], wlr[1] - mr[1])
        sign = (-1) ** length
        lbl = w_label(s1, s2, sig)
        kqt = kostant_qt_B2(diff)
        print(f"  {lbl:<25} {length:<5} {('+' if sign>0 else '-'):<6} "
              f"{str(diff):<18} {fmt_qt(kqt):<40}")
        for k, v in kqt.items():
            chi[k] += sign * v

    chi = {k: v for k, v in chi.items() if v != 0}
    print(f"\n  χ_{{q,t}} = {fmt_qt(chi)}")
    has_neg = any(v < 0 for v in chi.values())
    if has_neg:
        print(f"  >>> NEGATIVE coefficient detected: {[(k, v) for k, v in chi.items() if v < 0]}")
    else:
        print(f"  >>> Positive (all coefs ≥ 0)")


if __name__ == "__main__":
    # The Remark 4.7 case
    decompose_kl((1, 0), (0, 0))
    # The "spin-aligned" case
    decompose_kl((1, 1), (0, 0))
    # Other interesting cases
    decompose_kl((2, 0), (0, 0))
    decompose_kl((2, 1), (1, 0))
    decompose_kl((2, 2), (0, 0))
    decompose_kl((3, 1), (1, 1))
    print("\n\n========= SPIN CASES (half-integer weights) =========")
    # The spin analog of (1,0) -> (0,0): use spin fundamental shifts
    # lam^# = lam + (1/2, 1/2), mu^# = mu + (1/2, 1/2)
    F = Fraction
    decompose_kl((F(3, 2), F(1, 2)), (F(1, 2), F(1, 2)))
    decompose_kl((F(5, 2), F(1, 2)), (F(1, 2), F(1, 2)))
    decompose_kl((F(3, 2), F(3, 2)), (F(1, 2), F(1, 2)))
    decompose_kl((F(5, 2), F(3, 2)), (F(1, 2), F(1, 2)))
    decompose_kl((F(5, 2), F(3, 2)), (F(3, 2), F(1, 2)))
