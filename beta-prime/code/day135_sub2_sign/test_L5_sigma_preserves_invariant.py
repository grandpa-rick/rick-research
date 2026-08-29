"""Day 135 bonus — test key lemma L5:

    L5:  If P has sign (-1)^{y_1+y_3} on every nonzero coefficient,
         then σ(P) has sign (-1)^{y_1+y_3} on every nonzero coefficient too.

σ(E_1) = E_1 - 3
σ(E_2) = E_2 - 2 E_1 + 3
σ(E_3) = E_3 - E_2 + E_1 - 1

Test on pure monomials E_1^{a_1} E_2^{a_2} E_3^{a_3} for a_1+a_2+a_3 up to weight 8.
BUT: a single pure monomial does NOT satisfy the invariant (it has just ONE nonzero
coefficient — sign is 1 whether or not it matches).

So we test the correct statement: for each pure monomial P = (-1)^{a_1+a_3} · E_1^{a_1}
E_2^{a_2} E_3^{a_3} (which DOES satisfy the invariant with its one coefficient),
does σ(P) also satisfy the invariant on ALL of its (many) coefficients?

This is equivalent to asking: after applying σ to a pure monomial, do all
resulting coefficients c_{y_1, y_2, y_3} satisfy sign(c) = (-1)^{a_1+a_3} ·
(-1)^{y_1+y_3}?

Equivalently, define ε(y_1, y_3) = (-1)^{y_1+y_3}. The invariant on P is
"every nonzero coeff of P at (y_1,y_2,y_3) has sign ε(y_1,y_3)".

L5 empirical test on a pure monomial (a_1, a_2, a_3):
   σ(E_1^{a_1} E_2^{a_2} E_3^{a_3}) — compute all coefficients — check
   sign(c_{y_1, y_2, y_3}) == (-1)^{a_1 + a_3} · (-1)^{y_1 + y_3}
      = (-1)^{a_1 + a_3 + y_1 + y_3}.

Test up to weight w = a_1 + a_2 + 2 a_3 = 8, but pure monomials only.
"""

from sympy import symbols, Poly, expand, Integer

E1, E2, E3 = symbols('E1 E2 E3')

# σ definitions:
def sigma_of_E1():  return E1 - 3
def sigma_of_E2():  return E2 - 2*E1 + 3
def sigma_of_E3():  return E3 - E2 + E1 - 1

def sigma_of_monom(a1, a2, a3):
    """Compute σ(E_1^{a_1} E_2^{a_2} E_3^{a_3})."""
    result = Integer(1)
    for _ in range(a1):
        result = result * sigma_of_E1()
    for _ in range(a2):
        result = result * sigma_of_E2()
    for _ in range(a3):
        result = result * sigma_of_E3()
    return expand(result)


def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 78)
    log("Day 135 bonus — L5 test: does σ preserve the Ψ-global sign invariant?")
    log("For each pure monomial E_1^{a_1} E_2^{a_2} E_3^{a_3}, compute σ(monomial),")
    log("expand, and check every coefficient's sign against (-1)^{a_1+a_3+y_1+y_3}.")
    log("=" * 78)

    total_mismatches = 0
    mismatch_examples = []

    WEIGHT_MAX = 8
    n_monomials_tested = 0

    for a3 in range(0, WEIGHT_MAX // 2 + 1):
        for a2 in range(0, WEIGHT_MAX - 2*a3 + 1):
            for a1 in range(0, WEIGHT_MAX - 2*a3 - a2 + 1):
                # weight = a1 + a2 + 2 a3 (should be <= WEIGHT_MAX)
                w = a1 + a2 + 2*a3
                if w > WEIGHT_MAX:
                    continue
                n_monomials_tested += 1

                sig = sigma_of_monom(a1, a2, a3)
                if sig == 0:
                    continue
                p = Poly(sig, E1, E2, E3)
                monom_mismatches = []
                for monom, c in p.as_dict().items():
                    y1, y2, y3 = monom
                    if c == 0:
                        continue
                    expected_sign = 1 if (a1 + a3 + y1 + y3) % 2 == 0 else -1
                    actual_sign = 1 if c > 0 else -1
                    if expected_sign != actual_sign:
                        monom_mismatches.append((y1, y2, y3, c, expected_sign))
                if monom_mismatches:
                    total_mismatches += len(monom_mismatches)
                    log(f"  ({a1},{a2},{a3}): weight {w}, {len(monom_mismatches)} mismatch(es):")
                    for (y1, y2, y3, c, expected_sign) in monom_mismatches[:3]:
                        log(f"      → coeff at E1^{y1} E2^{y2} E3^{y3} = {c}, expected sign = {expected_sign:+d}")
                        mismatch_examples.append(((a1,a2,a3), (y1,y2,y3), c, expected_sign))

    log(f"\nTotal pure monomials tested (weight ≤ {WEIGHT_MAX}): {n_monomials_tested}")
    log(f"Total sign mismatches: {total_mismatches}")

    if total_mismatches == 0:
        log("\nL5 STATUS: EMPIRICALLY CONFIRMED (pure monomials, weight ≤ 8).")
        log("σ preserves the Ψ-global sign invariant. This unlocks the induction plan.")
    else:
        log(f"\nL5 STATUS: EMPIRICALLY REFUTED. σ does NOT preserve the invariant.")
        log("The Day 136 PROVE plan needs revision — direct σ-preservation fails.")
        log("Possible remediation: L5 holds only for σ_top / weight-drop-by-k projections,")
        log("not for full σ. Or L5 holds only in the presence of the specific coefficient")
        log("polynomials in the Ψ-recursion (i.e., not term-by-term).")

    # Extra: also test σ² and σ³ for completeness (these appear in higher-b Ψ recursion depths)
    # Skip for now; σ alone is the load-bearing question.

    out_path = '/home/agent/projects/beta-prime/code/day135_sub2_sign/test_L5_sigma_preserves_invariant.txt'
    with open(out_path, 'w') as fp:
        fp.write('\n'.join(log_lines))
    log(f"\nSaved log to {out_path}")


if __name__ == '__main__':
    main()
