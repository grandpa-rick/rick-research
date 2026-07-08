"""Day 86 CODE Task 1 — Q_j(a, b, c) closed-form polynomial extraction.

We already have (Day 86 symbolic script):

    Q_j(a, b, c) := <s_(a,b,c), e_2^j * p_1^{n-2j}> * (n)_{2j} / f^(a,b,c)
                  = sum_{mu ⊢ 2j, <= 3 rows} K_{mu^T, (2^j)} * f^{(a,b,c)/mu}
                    * (n)_{2j} / f^(a,b,c)

The Aitken determinant makes each f^{(a,b,c)/mu} symbolic in (a, b, c). Sum
them with the Pieri-derived Kostka numbers to get Q_j.

This script:
  1) Builds the e_2^j Schur expansion (Kostka table) via vertical-2-strip
     Pieri, for j = 1..6.
  2) Uses the Aitken formula to make f^{(a,b,c)/mu} symbolic in (a, b, c).
  3) Extracts Q_j(a, b, c) as an expanded polynomial for j = 0..6.
  4) Specializes to c = 5, 6, 7 for downstream use (Task 4 needs c=6, 7).
  5) Cross-checks against the c=5 numeric Q_j from Day-85 M_j-final.py at
     30+ (a, b) points.

Output:
  - Q_j closed forms printed to stdout AND saved to
    code/2026-07-08-Q_j-closed-forms.txt.
"""
from sympy import symbols, Matrix, simplify, expand, factor, Poly
from math import factorial as pyfact
from collections import defaultdict


a, b, c = symbols('a b c')


# ---------------------------------------------------------------------------
# Pieri: build e_2^j in Schur basis (restricted to <= 3 rows)
# ---------------------------------------------------------------------------

def add_vertical_2_strip(mu, max_rows=4):
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
    """Returns {mu: K_{mu^T, (2^j)}} restricted to mu with <= max_rows parts."""
    current = defaultdict(int)
    current[tuple()] = 1
    for _ in range(j):
        nxt = defaultdict(int)
        for mu, k in current.items():
            for nu in add_vertical_2_strip(mu):
                nxt[nu] += k
        current = nxt
    return {mu: k for mu, k in current.items() if len(mu) <= max_rows}


# ---------------------------------------------------------------------------
# Aitken determinant for f^{(a,b,c)/mu}, symbolic in (a, b, c).
# We use the identity that lets us pull common factorial prefactors out:
#
#   f^{(a,b,c)/mu} = (n - |mu|)! * det(1/(lam_i - mu_j - i + j)!)
#
# Set A = a+2, B = b+1, C = c. Then
#   1/(lam_i - mu_j - i + j)! = 1/(x_i - k_j)! where x = (A, B, C)
#   and k_j = mu_j + (2 - j).
#
# Factor 1/x_i! out of each row; the residual entry is falling(x_i, k_j).
# So det(1/(...)!) = det(falling(x_i, k_j)) / (A! B! C!).
#
# Then f^{(a,b,c)/mu} = (n - |mu|)! * det(falling(x_i, k_j)) / (A! B! C!).
#
# We work with the RATIO Q_j = M_j * (n)_{2j} / M_0 = (n)_{2j} * M_j / f^lam.
# f^lam has an identical A!B!C! prefactor and the same n! part, so the ratio
# leaves us with det(falling(x_i, k_j)) / D0 where D0 = det for mu = ()
# (which equals (A-B)(B-C)(A-C)).
# ---------------------------------------------------------------------------

def falling(x, k):
    p = 1
    for i in range(k):
        p *= (x - i)
    return p


def det_mu_3row(mu):
    xs = [a + 2, b + 1, c]
    ks = [mu[j] + (2 - j) for j in range(3)]
    return Matrix([[falling(xs[i], ks[j]) for j in range(3)] for i in range(3)]).det()


# D_0 = det for empty mu, corresponds to f^lam ratio prefactor.
D0 = det_mu_3row((0, 0, 0))
print(f"D_0 (should be (A-B)(B-C)(A-C) with A=a+2, B=b+1, C=c) = {expand(D0)}")
print(f"    factored: {factor(D0)}")
print()


def Q_j_symbolic(j):
    """Return Q_j(a, b, c) as an expanded SymPy polynomial in (a, b, c)."""
    if j == 0:
        return expand(D0 / D0)  # = 1
    kostka = e2_power_kostka(j, max_rows=3)
    numer = 0
    for mu, k in kostka.items():
        mu3 = tuple(list(mu) + [0] * (3 - len(mu)))
        numer += k * det_mu_3row(mu3)
    return expand(simplify(numer / D0))


# ---------------------------------------------------------------------------
# Cross-check vs Day-85 c=5 numeric M_j oracle.
# ---------------------------------------------------------------------------

def C_int(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return pyfact(n) // (pyfact(k) * pyfact(n - k))


def H5(av, bv, j):
    h0 = (av+3)*(av+4)*(av+5)*(av+6)*(bv+2)*(bv+3)*(bv+4)*(bv+5)
    h1 = -20*(av+3)*(av+4)*(av+5)*(bv+2)*(bv+3)*(bv+4)
    h2 = -10*(av+3)*(av+4)*(bv+2)*(bv+3)*(av*bv + av + 2*bv - 22)
    h3 = 360*(av+3)*(bv+2)*(av*bv + av + 2*bv - 2)
    h4 = 240*(av*av*bv*bv + av*av*bv + 3*av*bv*bv - 15*av*bv - 18*av + 2*bv*bv - 34*bv - 24)
    h5 = -7200*(av*bv + bv - 2)
    h6 = -7200*(av*bv - av - 6)
    h7 = 100800
    h8 = 201600
    hs = [h0, h1, h2, h3, h4, h5, h6, h7, h8]
    return sum(hs[k] * C_int(j, k) for k in range(9))


def M_j_c5(av, bv, j):
    """Day-85 c=5 M_j oracle."""
    cc = 5
    m = (av + bv + cc) // 2
    N = 2 * (m - j)
    Q5 = (av - 3) * (bv - 4) * H5(av, bv, j) - pyfact(10) * C_int(j, 10)
    den = 120 * (av + 6 - j)
    for i in range(1, 6):
        den *= (bv + i - j)
    num = C_int(N, bv - j) * (av - bv + 1) * Q5
    if den == 0:
        return None
    if num % den != 0:
        return None
    return num // den


def f_lambda_c5(av, bv):
    """f^(av, bv, 5) via hook length."""
    lam = [av, bv, 5]
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


def Q_j_c5_from_oracle(av, bv, j):
    m = M_j_c5(av, bv, j)
    if m is None:
        return None
    f = f_lambda_c5(av, bv)
    n = av + bv + 5
    return m * falling_int(n, 2 * j) // f  # integer for M_0 shape


# ---------------------------------------------------------------------------
# Main: extract closed forms and cross-check.
# ---------------------------------------------------------------------------

def main():
    lines = []
    lines.append("=" * 72)
    lines.append("Q_j(a, b, c) CLOSED FORMS  —  Day 86 CODE Task 1")
    lines.append("=" * 72)
    lines.append("")
    lines.append("Q_j(a, b, c) := <s_(a,b,c), e_2^j p_1^{n-2j}> * (n)_{2j} / f^(a,b,c)")
    lines.append("             = sum over mu ⊢ 2j (<=3 parts) of K_{mu^T,(2^j)}")
    lines.append("               * det(falling(x_i, k_j)) / D_0")
    lines.append("               with x=(a+2,b+1,c), k_j = mu_j+(2-j),")
    lines.append("               D_0 = (a - b + 1)(b - c + 1)(a - c + 2).")
    lines.append("")

    Qj_forms = {}
    for j in range(0, 7):
        Qj = Q_j_symbolic(j)
        Qj_forms[j] = Qj
        lines.append("-" * 72)
        lines.append(f"j = {j}")
        lines.append("-" * 72)
        lines.append(f"Q_{j}(a, b, c) =")
        lines.append(f"  {expand(Qj)}")
        lines.append("")
        lines.append(f"Q_{j}(a, b, 5) =")
        lines.append(f"  {expand(Qj.subs(c, 5))}")
        lines.append("")
        lines.append(f"Q_{j}(a, b, 6) =")
        lines.append(f"  {expand(Qj.subs(c, 6))}")
        lines.append("")
        lines.append(f"Q_{j}(a, b, 7) =")
        lines.append(f"  {expand(Qj.subs(c, 7))}")
        lines.append("")

    # Cross-check vs c=5 oracle across many (a, b).
    lines.append("=" * 72)
    lines.append("CROSS-CHECK Q_j(a, b, 5) SYMBOLIC vs Day-85 M_j oracle")
    lines.append("=" * 72)
    total = 0
    matches = 0
    fails = []
    for j in range(0, 7):
        Qj_c5 = expand(Qj_forms[j].subs(c, 5))
        for av in range(5, 22):
            for bv in range(5, min(av, 18) + 1):
                if (av + bv + 5) % 2 != 0:
                    continue
                oracle = Q_j_c5_from_oracle(av, bv, j)
                if oracle is None:
                    continue
                pred = int(Qj_c5.subs([(a, av), (b, bv)]))
                total += 1
                if pred == oracle:
                    matches += 1
                else:
                    fails.append((j, av, bv, pred, oracle))
    lines.append(f"  {matches}/{total} matches across (a, b, c=5), j = 0..6")
    if fails:
        lines.append(f"  FAILURES (first 5): {fails[:5]}")
    lines.append("")

    # Compact per-j "structure" printout for the report.
    lines.append("=" * 72)
    lines.append("STRUCTURE:  Q_j leading behavior and total degree")
    lines.append("=" * 72)
    for j in range(0, 7):
        Qj = expand(Qj_forms[j])
        p = Poly(Qj, a, b, c)
        deg_total = p.total_degree()
        deg_a = Poly(Qj, a).degree()
        deg_b = Poly(Qj, b).degree()
        deg_c = Poly(Qj, c).degree()
        lines.append(f"  j = {j}: total degree {deg_total}, deg_a {deg_a}, "
                     f"deg_b {deg_b}, deg_c {deg_c}, # terms {len(p.terms())}")
    lines.append("")

    out = "\n".join(lines)
    print(out)

    outfile = "/home/agent/projects/code/2026-07-08-Q_j-closed-forms.txt"
    with open(outfile, "w") as f_:
        f_.write(out)
    print(f"\nWritten: {outfile}")

    assert matches == total, "Q_j cross-check FAILED"
    print("Cross-check: PASS.")


if __name__ == "__main__":
    main()
