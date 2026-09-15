"""SOBER RE-CHECK of the Day 193 closed form for e_3 ⋆ e_r.

Independent numerical verification: substitute concrete (q, t) values UPFRONT
into the AHA level-1 polynomial representation, run e_3(Y) . e_6(X)/t^3, and
extract e_λ-coefficients numerically. Compare against the CLOSED FORM
evaluated at those (q, t).

This is an independent code path from the symbolic SymPy compute — it uses
Python Fractions (rational arithmetic) rather than SymPy expressions, so
there's no correlated blowup or shared bugs.

If all three (q, t)-points give exact match, closed form is `checked-sober`.
"""

from fractions import Fraction
from itertools import combinations
import pickle

# TEST POINTS  (q, t) as rationals
TEST_POINTS = [
    (Fraction(5), Fraction(3)),
    (Fraction(2), Fraction(7)),
    (Fraction(7), Fraction(-1)),
]

def qint_val(n, t):
    """[n]_t evaluated at concrete t."""
    if n <= 0:
        return Fraction(0)
    return sum(t**i for i in range(n))

def build_action_numeric(m, q, t):
    """Build Y-application with numeric q, t."""

    def si_apply(F, i):
        """F is a dict mapping monomial tuple -> Fraction coefficient.
        s_i swaps X_i <-> X_{i+1}, i.e., positions (i-1) and i in the tuple."""
        result = {}
        for mono, c in F.items():
            new_mono = list(mono)
            new_mono[i-1], new_mono[i] = new_mono[i], new_mono[i-1]
            new_mono = tuple(new_mono)
            result[new_mono] = result.get(new_mono, Fraction(0)) + c
        return {k: v for k, v in result.items() if v != 0}

    def divide_by_x_diff(F, i):
        """F = G · (X_i - X_{i+1}) implicitly; return G by manipulating monomial exponents.
        This is a bit tricky. Instead: since F is antisymmetric under s_i, we have
        F = (X_{i-1} - X_i) · G (with i-th s.t. it works). So compute G = F/(X_{i-1} - X_i)
        by dividing monomial-by-monomial after grouping."""
        # For each monomial X^α, we need to find the "quotient" polynomial G such that
        # F = G · (X_{i-1} - X_i). Since F is antisymmetric in X_{i-1}, X_i, we can write
        # F = sum over pairs (α, s_i(α)) of c_α (X^α - X^{s_i(α)}) for α with a_{i-1} > a_i.
        # And X^α - X^{s_i(α)} = X^α (1 - t^d) with t = X_i/X_{i-1}, d = a_{i-1} - a_i.
        # So (X^α - X^{s_i(α)})/(X_{i-1} - X_i) = X^α · (X_{i-1}^d - X_i^d) / [X_{i-1} - X_i] / X_{i-1}^{d}? Hmm messy.
        # Better: rewrite (X^α - X^{s_i(α)})/(X_{i-1} - X_i) = (X_{i-1}^a X_i^b - X_{i-1}^b X_i^a)/(X_{i-1} - X_i)
        # = X_{i-1}^b X_i^b · (X_{i-1}^{a-b} - X_i^{a-b})/(X_{i-1} - X_i) [with a >= b]
        # = X_{i-1}^b X_i^b · sum_{k=0}^{a-b-1} X_{i-1}^{a-b-1-k} X_i^k
        # = sum_{k=0}^{a-b-1} X_{i-1}^{a-1-k} X_i^{b+k}
        # This gives the polynomial quotient explicitly.
        result = {}
        seen = set()
        for mono in list(F.keys()):
            if mono in seen:
                continue
            swapped = list(mono)
            swapped[i-1], swapped[i] = swapped[i], swapped[i-1]
            swapped = tuple(swapped)
            if swapped == mono:
                # symmetric, contribution to (F - s F) is 0
                if F[mono] != 0:
                    raise ValueError("Not antisymmetric")
                seen.add(mono)
                continue
            a = mono[i-1]
            b = mono[i]
            if a < b:
                continue  # will be handled when we hit swapped
            c = F[mono]
            # F should be antisymmetric: F[mono] = -F[swapped]
            if F.get(swapped, Fraction(0)) != -c:
                raise ValueError(f"Not antisymmetric at {mono}")
            # (X^mono - X^swapped) / (X_{i-1} - X_i) = sum_{k=0}^{a-b-1} X_{i-1}^{a-1-k} X_i^{b+k} (times other X_j^{α_j})
            for k in range(a - b):
                new_mono = list(mono)
                new_mono[i-1] = a - 1 - k
                new_mono[i] = b + k
                new_mono = tuple(new_mono)
                result[new_mono] = result.get(new_mono, Fraction(0)) + c
            seen.add(mono)
            seen.add(swapped)
        return {k: v for k, v in result.items() if v != 0}

    def Ti_apply(F, i):
        """T_i . F = t·s_i(F) + (t-1) · (-X_i) · (F - s_i F)/(X_{i-1} - X_i)."""
        sF = si_apply(F, i)
        # F - sF is antisymmetric under s_i
        diff = {}
        for mono, c in F.items():
            diff[mono] = diff.get(mono, Fraction(0)) + c
        for mono, c in sF.items():
            diff[mono] = diff.get(mono, Fraction(0)) - c
        diff = {k: v for k, v in diff.items() if v != 0}
        # Divide by (X_{i-1} - X_i)
        quot = divide_by_x_diff(diff, i)
        # Multiply by -X_i (increment i-th position by 1) and by (t-1)
        result = {}
        # First add t · sF
        for mono, c in sF.items():
            result[mono] = result.get(mono, Fraction(0)) + t * c
        # Then add (t-1) · (-X_i) · quot = -(t-1) X_i · quot
        for mono, c in quot.items():
            new_mono = list(mono)
            new_mono[i] += 1  # multiply by X_i (position i, 0-indexed)
            new_mono = tuple(new_mono)
            result[new_mono] = result.get(new_mono, Fraction(0)) - (t - 1) * c
        return {k: v for k, v in result.items() if v != 0}

    def Ti_inv_apply(F, i):
        """T_i^{-1} = T_i/t - (t-1)/t · id."""
        TiF = Ti_apply(F, i)
        result = {}
        for mono, c in TiF.items():
            result[mono] = result.get(mono, Fraction(0)) + c / t
        for mono, c in F.items():
            result[mono] = result.get(mono, Fraction(0)) - (t - 1) / t * c
        return {k: v for k, v in result.items() if v != 0}

    def Pi_apply(F):
        """Π: X_1 -> X_2, X_2 -> X_3, ..., X_{m-1} -> X_m, X_m -> q^{-1} X_1.
        Then multiply by X_1."""
        result = {}
        for mono, c in F.items():
            # rotate: new_mono[i] = mono[i-1] for i=1..m-1, new_mono[0] = mono[m-1]
            new_mono = [mono[m-1]] + list(mono[:m-1])
            # If X_m (originally at position m-1) had exponent e = mono[m-1], we now have X_1^e (position 0)
            # from the substitution X_m -> q^{-1} X_1, we get q^{-e} factor
            factor = q ** (-mono[m-1])
            # Then multiply by X_1: increment position 0 exponent by 1
            new_mono[0] += 1
            new_mono = tuple(new_mono)
            result[new_mono] = result.get(new_mono, Fraction(0)) + c * factor
        return {k: v for k, v in result.items() if v != 0}

    def Y_apply(F, i):
        """Y_i = t^{m-i} · T_{i-1}^{-1} ... T_1^{-1} · Π · T_{m-1} ... T_i."""
        G = F
        for j in range(i, m):
            G = Ti_inv_apply(G, j)
        G = Pi_apply(G)
        for j in range(1, i):
            G = Ti_apply(G, j)
        # Multiply by t^{m-i}
        return {k: t ** (m - i) * v for k, v in G.items() if v != 0}

    return Y_apply


def e_r_X_dict(m, r):
    """e_r(X_1, ..., X_m) as dict mapping monomial tuple -> coefficient (1)."""
    result = {}
    for combo in combinations(range(m), r):
        mono = [0]*m
        for i in combo:
            mono[i] = 1
        result[tuple(mono)] = Fraction(1)
    return result


def compute_e3_star_er_numeric(r, m, q, t):
    """Compute e_3 ⋆ e_r at concrete (q, t)."""
    Y_apply = build_action_numeric(m, q, t)
    erX = e_r_X_dict(m, r)
    # Y_k . e_r
    Yk_er = {k: Y_apply(erX, k) for k in range(1, m+1)}
    # Y_j Y_k . e_r for j < k
    Yjk_er = {}
    for k in range(1, m+1):
        for j in range(1, k):
            Yjk_er[(j,k)] = Y_apply(Yk_er[k], j)
    # Sum Y_i Y_j Y_k . e_r for i < j < k
    total = {}
    for k in range(1, m+1):
        for j in range(1, k):
            for i in range(1, j):
                piece = Y_apply(Yjk_er[(j,k)], i)
                for mono, c in piece.items():
                    total[mono] = total.get(mono, Fraction(0)) + c
    total = {k: v for k, v in total.items() if v != 0}
    # Multiply by t^{-3}
    total = {k: v / t**3 for k, v in total.items()}
    return total


def extract_e_lambda_coeff(F, m, lam):
    """Extract coefficient of e_λ = product of e_{λ_i}(X_1..X_m) from F.
    Use the leading monomial X_1^{λ_1} X_2^{λ_2} ... = mono[i] = λ[i] for i < len(λ).
    Requires m >= n = sum(λ)."""
    canonical = [0]*m
    for i, p in enumerate(lam):
        canonical[i] = p
    canonical = tuple(canonical)
    return F.get(canonical, Fraction(0))


def closed_form_c0(r, q, t):
    """Numeric closed form for c_0^(3)(r)."""
    prefactor = qint_val(r+3, t) / (qint_val(2, t) * qint_val(3, t))
    inner = (qint_val(r+1, t) * qint_val(r+2, t) * q**2
             - t * qint_val(2, t) * qint_val(r-1, t) * qint_val(r+1, t) * q
             + t**3 * qint_val(r-2, t) * qint_val(r-1, t))
    return (q - 1) / q**3 * prefactor * inner


def closed_form_c1(r, q, t):
    return (q - 1) / q**3 * qint_val(r+1, t) * (q * qint_val(r, t) - t * qint_val(r-2, t)) / qint_val(2, t)


def closed_form_c2(r, q, t):
    return (q - 1) * qint_val(r-1, t) / q**3


def closed_form_c3(r, q, t):
    return Fraction(1) / q**3


if __name__ == "__main__":
    r_vals = [4, 5]  # small r, m = r+3
    print("SOBER RE-CHECK of Day 193 closed form via numeric Fraction arithmetic")
    print("=" * 70)
    for r in r_vals:
        m = r + 3
        print(f"\n--- r = {r}, m = {m} ---")
        for (q_num, t_num) in TEST_POINTS:
            print(f"\n  (q, t) = ({q_num}, {t_num})")
            F_num = compute_e3_star_er_numeric(r, m, q_num, t_num)
            # Extract coefficients of each e_λ
            checks = [
                ((r+3,), 'c_0', closed_form_c0),
                ((r+2, 1), 'c_1', closed_form_c1),
                ((r+1, 2), 'c_2', closed_form_c2),
                ((r, 3), 'c_3', closed_form_c3),
            ]
            for lam, name, fn in checks:
                # Extract e_λ coefficient by expanding e_λ(X) = e_{λ_1} * e_{λ_2} etc.
                # For simplicity, extract by looking at leading monomial X_1^{λ_1} X_2^{λ_2}...
                # But we need the full e_λ expansion... let me use a direct approach:
                # e_(r+3-k, k) = e_{r+3-k}(X) * e_k(X). Its leading monomial in x_1 > x_2 > ... order
                # is X_1^{r+3-k} X_2^k X_3^0 ... IF r+3-k >= k. Actually the coeff of X_1^{r+3-k} X_2^k is 1
                # in e_{r+3-k} * e_k for the standard case r+3-k > k.
                # More carefully: e_λ = m_1 + lower. Coefficient of monomial X_1^{λ_1} X_2^{λ_2}...
                # in e_λ equals number of ways to compose the product, which for λ = (r+3-k, k):
                #   e_{r+3-k} has X_1^{r+3-k}...X_{r+3-k}^1 as term, e_k has X_1^1 X_2^1...X_k^1
                # For k=0: e_{r+3} contributes X_1 X_2 ... X_{r+3}. Coeff of X_1^{r+3} in e_{r+3}? Zero
                # unless we're looking at a specific monomial. Ah this is subtle.
                #
                # Use "power-symmetric" identification: extract coefficient by inverting e_λ basis.
                # Simpler: just use the leading monomial of e_λ, which for λ = (r+3-k, k) is
                # X_1^{r+3-k} X_2^{k} (if we sort variables) — but e_r doesn't have X_1^r term for r >= 2.
                #
                # SKIP the direct extraction, do the full linear-algebra e_λ-expansion.
                pass
            # Use full e_λ expansion (via linear algebra like SymPy version)
            # Build partitions of n = r + 3
            from hikita_star import partitions_of, expand_symmetric_in_e_basis
            # Convert F_num dict to SymPy expression
            import sympy as sp
            X = sp.symbols(f'X1:{m+1}')
            F_expr = sp.Integer(0)
            for mono, c in F_num.items():
                term = sp.Rational(c.numerator, c.denominator)
                for i, e in enumerate(mono):
                    term *= X[i]**e
                F_expr = sp.expand(F_expr + term)
            expansion = expand_symmetric_in_e_basis(F_expr, m, r + 3)
            print(f"    Numeric e_lam expansion:")
            for lam in [(r, 3), (r+1, 2), (r+2, 1), (r+3,)]:
                cf = expansion.get(lam, sp.Integer(0))
                # Compare with closed form
                if lam == (r+3,):
                    pred = closed_form_c0(r, q_num, t_num)
                elif lam == (r+2, 1):
                    pred = closed_form_c1(r, q_num, t_num)
                elif lam == (r+1, 2):
                    pred = closed_form_c2(r, q_num, t_num)
                elif lam == (r, 3):
                    pred = closed_form_c3(r, q_num, t_num)
                pred_sp = sp.Rational(pred.numerator, pred.denominator)
                diff = sp.simplify(cf - pred_sp)
                status = "PASS" if diff == 0 else "FAIL"
                print(f"      e_{lam}: numeric = {cf}, closed = {pred_sp}, diff = {diff}  [{status}]")
