"""
Compute the (q,t)-Lusztig multiplicity polynomial for type B_2 directly from the WCF.

KL^{B_n}_{lam,mu}(q,t) = sum_{w in W} (-1)^w [e^{w(lam+rho)-(mu+rho)}]
                         prod_{alpha in R+_long} 1/(1 - q e^alpha)
                         prod_{alpha in R+_short} 1/(1 - t e^alpha)

(Macdonald-style unequal-parameter q-multiplicity: q for long roots, t for short.)

For B_2:
  Long pos: (1,-1), (1,1)
  Short pos: (0,1), (1,0)
  rho = (3/2, 1/2)

Setting t=q recovers the usual KL^{B_2}_{lam,mu}(q).
"""

from fractions import Fraction
from collections import defaultdict


def weyl_B2():
    """Return list of (w-function, det-w) for W(B_2), 8 elements."""
    out = []
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            for sig in [(0, 1), (1, 0)]:
                if sig == (0, 1):
                    sgn_sig = 1
                    def w(v, s1=s1, s2=s2):
                        return (s1 * v[0], s2 * v[1])
                else:
                    sgn_sig = -1
                    def w(v, s1=s1, s2=s2):
                        return (s1 * v[1], s2 * v[0])
                out.append((w, s1 * s2 * sgn_sig))
    return out


def kl_B2_qt(lam, mu):
    """Compute KL^{B_2}_{lam, mu}(q, t) as dict{(q-deg, t-deg) : coeff}."""
    rho = (Fraction(3, 2), Fraction(1, 2))
    lr = (lam[0] + rho[0], lam[1] + rho[1])
    mr = (mu[0] + rho[0], mu[1] + rho[1])

    poly = defaultdict(int)
    for w, det in weyl_B2():
        wlr = w(lr)
        diff = (wlr[0] - mr[0], wlr[1] - mr[1])
        x_w, y_w = diff
        # diff must be integer linear combo of roots; for integer lam,mu it is.
        if x_w.denominator != 1 or y_w.denominator != 1:
            continue
        x_w = int(x_w)
        y_w = int(y_w)
        if x_w < 0:
            continue
        # a, b, c, d >= 0 with a + b + d = x_w, -a + b + c = y_w
        # so c = a - b + y_w, d = x_w - a - b
        for a in range(x_w + 1):
            for b in range(x_w + 1 - a):
                d = x_w - a - b
                c = a - b + y_w
                if d >= 0 and c >= 0:
                    poly[(a + b, c + d)] += det
    return {k: v for k, v in poly.items() if v != 0}


def fmt(poly):
    if not poly:
        return "0"
    terms = []
    for (qd, td), c in sorted(poly.items()):
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
        sign = "+" if c > 0 else "-"
        cabs = abs(c)
        coef = "" if cabs == 1 else f"{cabs}"
        terms.append(f"{sign} {coef}{mon}")
    s = " ".join(terms)
    return s.lstrip("+ ").strip()


def specialize_to_q(poly):
    """Set t = q."""
    out = defaultdict(int)
    for (qd, td), c in poly.items():
        out[qd + td] += c
    return {k: v for k, v in out.items() if v != 0}


def fmt_q(poly):
    if not poly:
        return "0"
    terms = []
    for k, v in sorted(poly.items()):
        if k == 0:
            mon = "1"
        else:
            mon = "q" if k == 1 else f"q^{k}"
        sign = "+" if v > 0 else "-"
        absv = abs(v)
        coef = "" if absv == 1 else f"{absv}"
        terms.append(f"{sign} {coef}{mon}")
    s = " ".join(terms)
    return s.lstrip("+ ").strip()


if __name__ == "__main__":
    # Survey: focus on integer-weight (non-spin in the CKL sense) cases.
    # We want to identify which λ produce nonneg (q,t)-polynomial for various μ.
    cases = []
    for l1 in range(0, 5):
        for l2 in range(0, l1 + 1):  # dominant: l1 >= l2
            for m1 in range(0, l1 + 1):
                for m2 in range(0, m1 + 1):
                    cases.append(((l1, l2), (m1, m2)))
    print(f"{'(lam, mu)':<25} {'KL^B2_{lam,mu}(q,t)':<55} {'sign':<8} {'(t->q)':<20}")
    print("-" * 110)
    nonzero_cases = []
    for lam, mu in cases:
        p = kl_B2_qt(lam, mu)
        if not p:
            continue
        nonzero_cases.append((lam, mu, p))
        ps = specialize_to_q(p)
        has_neg = any(c < 0 for c in p.values())
        sign = "NEG" if has_neg else "pos"
        print(f"{str((lam, mu)):<25} {fmt(p):<55} {sign:<8} {fmt_q(ps):<20}")

    print()
    print("=" * 60)
    print("SUMMARY: Cases with NEGATIVE coefficients in (q,t):")
    print("=" * 60)
    for lam, mu, p in nonzero_cases:
        if any(c < 0 for c in p.values()):
            print(f"  λ={lam}, μ={mu}:  {fmt(p)}")
    print()
    print("=" * 60)
    print("Cases with all-NONNEGATIVE coefficients in (q,t):")
    print("=" * 60)
    for lam, mu, p in nonzero_cases:
        if not any(c < 0 for c in p.values()):
            print(f"  λ={lam}, μ={mu}:  {fmt(p)}")
