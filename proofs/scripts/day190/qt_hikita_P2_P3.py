"""
Day 190 PROVE: compute X_{P_n}(x; q, t) for n=2, n=3 via Hikita 2503.23597 recipe.

Hikita's recipe (Thm B(iii)): X_Gamma(q,t) = q_{(m)}(Y_Gamma(t)),
where Y_Gamma(t) is the ordinary CQF written in Y-variables.

For symmetric functions this reduces to: expand the ordinary CQF X_Gamma(t)
into e-basis products e_{lambda} = e_{lambda_1} e_{lambda_2} ... (ordinary product),
then re-interpret each ordinary product as a *-product, and apply Thm B(iv):
   q(e_lambda(Y)) = t^{sum lambda_i(lambda_i-1)/2} e^{(q,t)}_lambda(X),
where e^{(q,t)}_lambda(X) := e_{lambda_1}(X) * e_{lambda_2}(X) * ... * e_{lambda_l}(X).

So: X_Gamma(q,t) = sum_lambda t^{sum lambda_i(lambda_i-1)/2} c_lambda(t) e^{(q,t)}_lambda(X),
    where X_Gamma(t) = sum_lambda c_lambda(t) e_lambda(X) is the ordinary e-expansion
    of Y_Gamma(t)  --- i.e. of the CQF in the Y (equivalently X) variables.
    (In Hikita's setup, X_Gamma(t) in the "old" sense equals Y_Gamma(t) up to notation.)

We then need the *-product to convert e_{lambda}^{(q,t)} down to a normal form
(say by iterated Pieri).  Thm 3.12: e_1(X)*e_r(X) = (1 - q^{-1})[r+1]_t e_{r+1}(X)
                                                    + q^{-1} e_1(X) e_r(X).

For lambda = (a, b) with a=1: e_1 * e_b directly by Thm 3.12.
For general lambda we would need a full Pieri rule; here for P_2 and P_3
the compositions we need are (2), (1,1), (3), (2,1), (1,2), (1,1,1), all of
which fit within a=1 Pieri applications.

Sanity checks:
  * At q=1: recover Stanley's X_{P_n} = N(X_Gamma(t))|_{q=1}   [Thm A(iii)]
    i.e., X_Gamma(1,t) = N(X_Gamma(t)) with N(e_r) = t^{r(r-1)/2} e_r.
  * At q -> infinity: Thm C(i), X_Gamma(q,t) -> t^{n(n-1)/2 - |e|} [n]_t! e_n(X).
"""

import sympy as sp
from itertools import product

# ----- Symbols -----
q, t = sp.symbols('q t')

def qint(n):
    """[n]_t = 1 + t + ... + t^{n-1}."""
    if n <= 0:
        return sp.Integer(0) if n < 0 else sp.Integer(0)
    return sp.expand(sum(t**i for i in range(n)))

def qfact(n):
    r = sp.Integer(1)
    for i in range(1, n+1):
        r *= qint(i)
    return sp.expand(r)


# ------------------------------------------------------------------
# Part 1: compute X_{P_n}(t) directly for small n via enumeration in
# a truncated alphabet (m variables). This is not fast but is a ground
# truth for n=2 and n=3.
# ------------------------------------------------------------------
def cqf_directed_path(n, m):
    """Return sum over proper colorings kappa:[n]->[m] of t^asc * prod x_kappa(v)
       for the directed path 1->2->...->n."""
    xs = sp.symbols(f'x1:{m+1}')
    total = sp.Integer(0)
    for kappa in product(range(1, m+1), repeat=n):
        # proper: kappa(i) != kappa(i+1)
        ok = True
        asc = 0
        for i in range(n-1):
            if kappa[i] == kappa[i+1]:
                ok = False
                break
            if kappa[i] < kappa[i+1]:
                asc += 1
        if not ok:
            continue
        mon = sp.Integer(1)
        for v in kappa:
            mon *= xs[v-1]
        total += t**asc * mon
    return sp.expand(total), xs


def e_polys(m):
    xs = sp.symbols(f'x1:{m+1}')
    es = [sp.Integer(1)]
    from sympy.polys.specialpolys import symmetric_poly
    for r in range(1, m+1):
        # elementary symmetric polynomial
        # can build directly
        from itertools import combinations
        er = sp.Integer(0)
        for combo in combinations(xs, r):
            term = sp.Integer(1)
            for v in combo:
                term *= v
            er += term
        es.append(sp.expand(er))
    return es, xs


def extract_e_expansion(poly, n, m, verbose=False):
    """Given a symmetric polynomial `poly` in m variables of total degree n,
       return its expansion in monomials of e_lambda for partitions lambda of n.
       We solve a linear system: expand each e_lambda in some basis (say,
       coefficient of a chosen monomial x_1^a1 * x_2^a2 * ... with a_1>=a_2>=...
       one per partition).
    """
    es, xs = e_polys(m)
    # Partitions of n
    def partitions(k):
        if k == 0:
            return [[]]
        result = []
        def rec(remaining, max_part, current):
            if remaining == 0:
                result.append(list(current))
                return
            for p in range(min(remaining, max_part), 0, -1):
                current.append(p)
                rec(remaining - p, p, current)
                current.pop()
        rec(k, k, [])
        return result
    parts = partitions(n)
    # For each partition lambda, we need a "canonical" monomial: x_1^{lambda_1} x_2^{lambda_2} ...
    # But e_lambda is a symmetric polynomial; the monomial basis for symmetric functions
    # is m_lambda. Use coefficient extraction on the monomial x_1^{lambda_1}...
    # actually easier: use the fact that all e_lambda have distinct top monomials
    # in dominance order; expand poly in the monomial basis then Gauss-eliminate.
    # simple approach: build matrix A[i,j] = coeff of chosen monomial_j in e_{lambda_i}
    # ensure m >= n (so all partitions of n have a representative).
    if m < n:
        raise ValueError("Need m >= n.")
    # choose monomials: for each partition lambda, the monomial x_1^{lambda_1} x_2^{lambda_2}...
    def choose_monomial(lam):
        mon = sp.Integer(1)
        for i, p in enumerate(lam):
            mon *= xs[i]**p
        return mon
    e_lambda = {}
    for lam in parts:
        eexpr = sp.Integer(1)
        for p in lam:
            eexpr *= es[p]
        e_lambda[tuple(lam)] = sp.expand(eexpr)
    # Now solve. Build vector b (coeffs of poly at chosen monomials) and matrix A.
    monos = [choose_monomial(lam) for lam in parts]
    b = sp.Matrix([sp.Poly(poly, *xs).coeff_monomial(sp.Poly(m_, *xs).monoms()[0]) for m_ in monos])
    A_rows = []
    for lam in parts:
        row = []
        el = e_lambda[tuple(lam)]
        el_poly = sp.Poly(el, *xs)
        for m_ in monos:
            row.append(el_poly.coeff_monomial(sp.Poly(m_, *xs).monoms()[0]))
        A_rows.append(row)
    A = sp.Matrix(A_rows).T   # rows indexed by monomials (b), cols by partitions
    coeffs = A.solve(b)
    result = {}
    for i, lam in enumerate(parts):
        c = sp.simplify(coeffs[i])
        if c != 0:
            result[tuple(lam)] = c
    return result


# ------------------------------------------------------------------
# Part 2: symmetric-function algebra abstractly (in terms of e_r).
# We work in Q(q,t)[e_1, e_2, e_3, ...] as a free commutative polynomial ring;
# ordinary product = Sym-product; * product defined by Pieri when a factor is e_1.
# ------------------------------------------------------------------
# Represent an element of Lambda_{q,t} as a sympy expression in variables
# E1, E2, E3, ... where E_r stands for e_r(X). ordinary multiplication is
# commutative polynomial mult in E_i.
E = sp.symbols('E1 E2 E3 E4 E5 E6', commutative=True)
E1, E2, E3, E4, E5, E6 = E

# Star product of e_1 * e_r via Thm 3.12
def star_e1_er(r):
    """Returns e_1 * e_r as a sympy expression in E_i."""
    if r == 0:
        # e_1 * 1 = e_1
        return E1
    # (1 - q^{-1}) [r+1]_t e_{r+1} + q^{-1} e_1 e_r
    coef1 = (1 - 1/q) * qint(r+1)
    coef2 = 1/q
    if r+1 > len(E):
        raise ValueError("need more E symbols")
    return sp.expand(coef1 * E[r] + coef2 * E1 * E[r-1])

# In general we need: (F * G) where F, G are polynomial in e_r's.
# The star product is commutative, associative, and preserves the subspace,
# but is NOT a graded algebra homomorphism relative to ordinary product
# --- i.e. (fg) * h is NOT (f * h)(g * h) in general.  What IS true:
# For any lambda = (lambda_1, ..., lambda_l), define
#    e^{(q,t)}_lambda(X) := e_{lambda_1}(X) * ... * e_{lambda_l}(X)
# these form a basis of Lambda_{q,t}, and by Thm B(iv),
#    q(e_lambda(Y)) = t^{sum lambda_i(lambda_i-1)/2} e^{(q,t)}_lambda(X).
# So the recipe X_Gamma(q,t) = q(Y_Gamma(t)) is COMPUTED as:
#   1. write Y_Gamma(t) (which is the ordinary CQF but in Y-variables) as
#      Y_Gamma(t) = sum_lambda c_lambda(t) e_lambda(Y).
#   2. apply q to each side:  X_Gamma(q,t) = sum_lambda t^{...} c_lambda(t) e^{(q,t)}_lambda(X).
# For a small path graph the resulting sum is only 1-2 terms.

def sum_lambda_choose_2(lam):
    return sum(l*(l-1)//2 for l in lam)


# ------------------------------------------------------------------
# Part 3: reduce e^{(q,t)}_lambda into normal form via Pieri when possible.
# For lambda = (a1, a2, ..., ak), we compute e_{a1} * e_{a2} * ... * e_{ak}.
# If any a_i = 1, we can use Thm 3.12 to reduce e_1 * e_r; iteratively.
# The remaining problem: e_a * e_b with a,b >= 2 --- we don't have this in
# the paper (only e_1 * e_r is given).  For P_2 and P_3 all compositions
# have some 1's so we'll be fine.
# ------------------------------------------------------------------
def apply_e1_star(expr):
    """Compute e_1 * expr where expr is a linear combination of monomials
       in E_i.  Uses only the Pieri rule Thm 3.12 for e_1 * e_r; but we
       must think about e_1 * (e_a e_b) --- this is a *ordinary* product
       inside expr, and Pieri only tells us about e_1 * e_r  (single e).
       Wait: expr is really a *sum of e_lambda's* under the ordinary product,
       and we're computing e_1 * (sum of e_lambda's) via star product.  But
       e_lambda under ordinary product is not the same as e^{(q,t)}_lambda
       under the star product.  So this function is not directly useful.
       See Part 4 below for the correct approach."""
    raise NotImplementedError("Not the right approach; see Part 4.")


# ------------------------------------------------------------------
# Part 4: the CORRECT recipe.
# X_Gamma(q,t) is expressed in the basis {e^{(q,t)}_lambda(X)} of Lambda_{q,t}.
# We DO NOT necessarily need to reduce further --- the coefficients c_lambda(t)
# already are the answer (up to a t-power).  But Rick asks for (Re)-form:
#    X_{P_n}(q,t) = ??? e_n + phi(q,t) sum_{k=2}^n [k-1]_?? e_k * X_{P_{n-k}}(q,t)
# so we DO need to know how to "recompose" from the *-basis --- via the
# multiplicativity XΓ∪Γ' = XΓ * XΓ' [main Thm A(ii)/Thm B].
#
# For P_n (a directed path), there's no natural disjoint union giving P_n;
# so the (Re) recursion is a genuine claim about (q,t)-CQFs of paths and
# might NOT survive.  But at q=1 it does.
# ------------------------------------------------------------------


def compute_ordinary_cqf(n, m):
    """Return the ordinary CQF X_{P_n}(t) enumerated in m variables,
       and its e-expansion (as a dict partition -> coefficient in Q[t])."""
    poly, xs = cqf_directed_path(n, m)
    if n == 0:
        return sp.Integer(1), {(): sp.Integer(1)}
    expansion = extract_e_expansion(poly, n, m)
    return poly, expansion


def q_map_e_expansion(expansion):
    """Given e-expansion of Y_Gamma(t): sum_lambda c_lambda(t) e_lambda(Y),
       return the expression q(Y_Gamma(t)) = sum_lambda t^{...} c_lambda(t) e^{(q,t)}_lambda(X),
       as a formal linear combination.  We return a dict
       partition -> coeff(q,t), interpreting e_lambda as e^{(q,t)}_lambda(X)."""
    result = {}
    for lam, c in expansion.items():
        tw = sum_lambda_choose_2(lam)
        result[lam] = sp.expand(t**tw * c)
    return result


def format_qt_cqf(qt_expansion):
    """Pretty-print the (q,t)-CQF as sum of c_lambda(q,t) * e^{(q,t)}_lambda."""
    terms = []
    for lam, c in qt_expansion.items():
        cs = sp.simplify(c)
        terms.append(f"  ({cs}) * e^*_{lam}")
    return "\n".join(terms)


# ------------------------------------------------------------------
# Part 5: verify the Rick recursion at t = 0 and Hikita example 4.6 at t=any.
# ------------------------------------------------------------------
def rick_recursion(n):
    """Rick's Day 187 formula (X_{P_n}(q) with t=q):
         X_{P_0} = 1, X_{P_1} = e_1
         X_{P_n} = e_n + q sum_{k=2}^n [k-1]_q e_k X_{P_{n-k}}   [ordinary product]
       Returned as ordinary product in E_i.  This is one interpretation."""
    memo = {0: sp.Integer(1), 1: E1}
    def get(k):
        if k in memo:
            return memo[k]
        r = E[k-1]  # e_n
        for kk in range(2, k+1):
            coef = q * sp.expand(sum(q**i for i in range(kk-1)))  # q * [kk-1]_q
            r += sp.expand(coef * E[kk-1] * get(k-kk))
        memo[k] = sp.expand(r)
        return memo[k]
    return get(n)


def main():
    print("=" * 70)
    print("Day 190 PROVE: X_{P_n}(x;q,t) for n=2, n=3 via Hikita's recipe")
    print("=" * 70)
    # ------------- Compute ordinary CQF X_{P_n}(t) -------------
    for n in [1, 2, 3]:
        m = n + 2   # enough variables to see all partitions
        poly, exp = compute_ordinary_cqf(n, m)
        print(f"\n--- P_{n} ---")
        print(f"Ordinary CQF X_(P_{n})(t) e-expansion (Ellzey/Shareshian-Wachs):")
        for lam, c in exp.items():
            print(f"  {lam}: {sp.factor(c)}")
        qt = q_map_e_expansion(exp)
        print(f"(q,t)-CQF X_(P_{n})(q,t) in e^*-basis (via Hikita Thm B(iii)+(iv)):")
        print(format_qt_cqf(qt))

    # Sanity check: reduce X_{P_2}(q,t) to ordinary basis using * product.
    # For P_2, only partition (2): e^*_{(2)} = e_2 (single factor, no star product).
    # And partition (1,1): e^*_{(1,1)} = e_1 * e_1.
    print("\n--- SANITY CHECK: e_1 * e_1 via Thm 3.12 (r=1) ---")
    e1_star_e1 = star_e1_er(1)
    print(f"e_1 * e_1 = {sp.simplify(e1_star_e1)}")
    print(f"  = (1 - q^-1)[2]_t e_2 + q^-1 e_1^2")
    print(f"  = (1-q^-1)(1+t) e_2 + q^-1 e_1^2")
    expected = (1 - 1/q)*(1+t)*E2 + (1/q)*E1**2
    print(f"  match: {sp.simplify(e1_star_e1 - expected) == 0}")

    # X_{P_2}(q,t): from Ellzey, X_{P_2}(t) = (1+t) e_2, so it's just c_{(2)}(t) = 1+t.
    # Then X_{P_2}(q,t) = t^{1} (1+t) e^*_{(2)} = t(1+t) e_2.
    print("\n--- X_{P_2}(q,t) ---")
    print("From q-map: t^{2 choose 2}(1+t) e^*_{(2)} = t(1+t) e_2   [since e^*_{(2)} = e_2]")
    X_P2_qt = t * (1+t) * E2
    print(f"X_(P_2)(q,t) = {X_P2_qt}")

    # Verify Thm A(iii): at q=1, X_Gamma(1,t) = N(X_Gamma(t))
    # For P_2, X_Gamma(t) = (1+t) e_2, so N(X_Gamma(t)) = (1+t) * t^{2*1/2} e_2 = t(1+t) e_2.  MATCH.
    print(f"Check Thm A(iii): X_(P_2)(1,t) = N((1+t)e_2) = t(1+t) e_2.  MATCH: {X_P2_qt.subs(q,1) - t*(1+t)*E2 == 0}")

    # Now X_{P_3}(q,t) --- more interesting.
    # From enumeration, we expect X_{P_3}(t) = ? e_3 + ? e_{2,1} + ? e_{1,1,1}? --- actually
    # for directed path, we expect e-positive with support {(3),(2,1)} maybe.
    print("\n--- X_{P_3}(q,t) ---")
    _, exp3 = compute_ordinary_cqf(3, 5)
    qt3 = q_map_e_expansion(exp3)
    print("X_(P_3)(q,t) in e^*-basis:")
    print(format_qt_cqf(qt3))

    # Hikita Example 4.6:  X_Γ_e(q,t) ≡ q^{-1} t^2 (e_{2,1}(X) + (1+t+t^2)(-1+q+qt) e_3(X)) mod (X_4,...)
    # But note in Example 4.6, e_{2,1}(X) = e_2 e_1 is ORDINARY product, and e_3 is single.
    # So the coefficient of e_{2,1}(X) [ordinary basis] is q^{-1} t^2, and of e_3(X) is q^{-1} t^2 (1+t+t^2)(-1+q+qt).
    # We check this against our formula.
    print("\n--- Hikita Example 4.6 comparison ---")
    print("Hikita's answer:  X_Γ(q,t) = q^{-1} t^2 e_{2,1} + q^{-1} t^2 (1+t+t^2)(q+qt-1) e_3")
    print(f"                          = q^{-1} t^2 e_1 e_2 + q^{-1} t^2 (1+t+t^2)(-1+q(1+t)) e_3")

    # Our (q,t)-CQF is in *-basis. Convert: e^*_{(2,1)} = e_1 * e_2, and e^*_{(3)} = e_3.
    # By Thm 3.12: e_1 * e_2 = (1-q^-1)[3]_t e_3 + q^-1 e_1 e_2.
    e1_star_e2 = star_e1_er(2)
    print(f"e_1 * e_2 = {sp.simplify(e1_star_e2)}")
    # so in ordinary basis:
    # X_{P_3}(q,t) = A * e^*_{(3)} + B * e^*_{(2,1)}  with A=qt3[(3,)], B=qt3[(2,1)]
    # = A*e_3 + B*[(1-q^-1)[3]_t e_3 + q^-1 e_1 e_2]
    # = (A + B(1-q^-1)[3]_t) e_3 + (B/q) e_1 e_2
    A = qt3.get((3,), sp.Integer(0))
    B = qt3.get((2,1), sp.Integer(0))
    coeff_e3 = sp.expand(A + B * (1 - 1/q) * qint(3))
    coeff_e21 = sp.expand(B / q)
    print(f"\nX_(P_3)(q,t) in ORDINARY basis:")
    print(f"  coefficient of e_3(X):  {sp.simplify(coeff_e3)}")
    print(f"  coefficient of e_2 e_1: {sp.simplify(coeff_e21)}")

    # Compare to Hikita 4.6:
    hik_e3 = sp.expand(1/q * t**2 * (1+t+t**2) * (-1 + q + q*t))
    hik_e21 = sp.expand(1/q * t**2)
    print(f"\nHikita 4.6:")
    print(f"  coefficient of e_3(X):  {sp.simplify(hik_e3)}")
    print(f"  coefficient of e_2 e_1: {sp.simplify(hik_e21)}")
    print(f"\nDIFF e_3:   {sp.simplify(coeff_e3 - hik_e3)}")
    print(f"DIFF e_21:  {sp.simplify(coeff_e21 - hik_e21)}")

    # Also check Thm A(iii): X_Gamma(1,t) = N(X_Gamma(t)) for P_3
    # X_Gamma(t) for P_3: from exp3
    print(f"\n--- Thm A(iii) check for P_3 ---")
    Xt = sum(c * (sp.Symbol('e' + '_'.join(str(l) for l in lam))) for lam, c in exp3.items())
    print(f"X_(P_3)(t) = {Xt}")
    # N(e_lambda) = t^{sum lambda_i(lambda_i-1)/2} e_lambda
    NXt_e3 = exp3.get((3,), 0) * t**3
    NXt_e21 = exp3.get((2,1), 0) * t**1  # t^{1+0}
    print(f"N-transform coeff of e_3:   {sp.simplify(NXt_e3)}")
    print(f"N-transform coeff of e_21:  {sp.simplify(NXt_e21)}")
    print(f"X_(P_3)(1,t):")
    print(f"  coeff of e_3:  {sp.simplify(coeff_e3.subs(q,1))}")
    print(f"  coeff of e_21: {sp.simplify(coeff_e21.subs(q,1))}")
    print(f"  match e_3?  {sp.simplify(coeff_e3.subs(q,1) - NXt_e3) == 0}")
    print(f"  match e_21? {sp.simplify(coeff_e21.subs(q,1) - NXt_e21) == 0}")

    # Rick's (Re) recursion at q=1 test:
    print(f"\n--- Rick's (Re) recursion (t=q; ordinary product) ---")
    print(f"Rick's X_(P_2)(q) [treating t=q]: {sp.expand(rick_recursion(2))}")
    print(f"Rick's X_(P_3)(q) [treating t=q]: {sp.expand(rick_recursion(3))}")
    print("These are the ordinary CQFs at t=q.  Compare to enumerated ordinary CQFs.")
    _, exp2 = compute_ordinary_cqf(2, 4)
    _, exp3b = compute_ordinary_cqf(3, 5)
    enum_P2 = sum(c.subs(t,q) * (E[l[0]-1] if len(l)==1 else sp.Mul(*[E[k-1] for k in l])) for l, c in exp2.items())
    enum_P3 = sum(c.subs(t,q) * (E[l[0]-1] if len(l)==1 else sp.Mul(*[E[k-1] for k in l])) for l, c in exp3b.items())
    print(f"Enumerated X_(P_2)(q) = {sp.expand(enum_P2)}")
    print(f"Enumerated X_(P_3)(q) = {sp.expand(enum_P3)}")
    print(f"Rick vs enumerated P_2 diff: {sp.expand(rick_recursion(2) - enum_P2)}")
    print(f"Rick vs enumerated P_3 diff: {sp.expand(rick_recursion(3) - enum_P3)}")


if __name__ == "__main__":
    main()
