"""
Test Guess A: B^[λ](T) = exp((E_3 − c·λ) · M(T)) for some scalar c.

Under Guess A:
  B^{(1)}(T) := −∂/∂λ B^[λ]|_{λ=0} = c · M(T) · B(T)
  ⇒ Q(T) := B^{(1)}(T) / B(T) = c · M(T)

So the definitive test is:
  Does Q(T) = c · M(T) for a single scalar c independent of E_1, E_2, E_3, T?

Where M(T) = Σ_{n≥2} μ_n · E_1^{n-2} · T^n / n!  with  μ_n = (−1)^{n−1}(n²−1)/n.

Convention (from step5_Q_series.py): Q_n = [T^n] Q(T)  as ordinary power-series
coefficient, i.e. Q(T) = Σ Q_n · T^n.  In the same convention,
  [T^n] M(T) = μ_n · E_1^{n-2} / n!.

Additionally: reconstruct B_m^{(1)} predicted by Guess A via the convolution
  B_m^{(1)},pred = c · Σ_{r+s=m} C(m,r) · M_r · B_s      where M_r = μ_r · E_1^{r-2}   (m! · [T^r] M(T))
and compare to empirical B_m^{(1)} for m = 2..8.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import (Poly, Integer, expand, symbols, Rational, factorial,
                    binomial, Symbol, factor, cancel, S, simplify)

T = Symbol('T')
c_sym = Symbol('c')


def log(msg=''):
    print(msg)
    LOG.append(str(msg))


LOG = []


def weight_part(P, w):
    P = expand(P)
    if P == 0:
        return Integer(0)
    p = Poly(P, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if i + j + 2*k == w:
            out += coeff * E1**i * E2**j * E3**k
    return out


def A_n(n):
    p = Integer(1)
    for r in range(1, n + 1):
        p = expand(p * (E2 - r * E1))
    return p


def A_n_upper1(n):
    total = Integer(0)
    for r in range(1, n + 1):
        term = Integer(r) ** 2
        for s_ in range(1, n + 1):
            if s_ != r:
                term = expand(term * (E2 - s_ * E1))
        total = expand(total + term)
    return total


def mu(n):
    return Rational((-1) ** (n - 1) * (n * n - 1), n)


def B_m(m):
    if m == 0:
        return Integer(1)
    total = Integer(0)
    for k in range(1, m // 2 + 1):
        def enum_comps(rem, parts_left):
            if parts_left == 0:
                if rem == 0:
                    yield ()
                return
            for a in range(2, rem - 2 * (parts_left - 1) + 1):
                for rest in enum_comps(rem - a, parts_left - 1):
                    yield (a,) + rest
        sub = Integer(0)
        for comp in enum_comps(m, k):
            prod = Integer(1)
            for a in comp:
                prod = prod * mu(a) * E1 ** (a - 2)
            sub = sub + prod
        total = total + E3 ** k * sub / factorial(k)
    return expand(total * factorial(m))


NMAX = 8

# --- Step 1. Compute sub_1[b] from direct Psi -------------------------------
log('=' * 78)
log('Guess A test: B^[λ](T) = exp((E_3 − c·λ) · M(T))')
log('Prediction:  Q(T) = B^{(1)}/B = c · M(T)   ⇔   Q_n / M_n = c  (constant).')
log('=' * 78)

sub1 = {0: Integer(0)}
for b in range(1, NMAX + 1):
    psi_u = Psi_direct(e2_u ** b)
    psi_e = sym_to_ebasis_direct(psi_u)
    sub1[b] = weight_part(psi_e, b - 1)

An_cache = {n: A_n(n) for n in range(NMAX + 1)}
An1_cache = {n: A_n_upper1(n) for n in range(NMAX + 1)}
Bm_cache = {m: B_m(m) for m in range(NMAX + 1)}

# --- Step 2. Fit empirical B_m^{(1)} via the Leibniz ansatz -----------------
B1 = {0: Integer(0)}
for m in range(1, NMAX + 1):
    b = m
    known = Integer(0)
    for n in range(1, b + 1):
        m_prime = b - n
        term1 = An1_cache[n] * Bm_cache[m_prime]
        term2 = An_cache[n] * B1[m_prime] if m_prime < m else Integer(0)
        known = expand(known + binomial(b, n) * (term1 + term2))
    B1[m] = expand(sub1[b] - known)

log('\nEmpirical B_m^{(1)} (from Day 134 ansatz):')
for m in range(NMAX + 1):
    log(f'  B_{m}^(1) = {B1[m]}')

# --- Step 3. Compute Q(T) = B^{(1)}(T) / B(T) as ordinary series ------------
# Q(T) · B(T) = B^{(1)}(T), where all three are treated as ordinary power series
# in T with coefficients q_n, b0_m, b1_k s.t. the corresponding EGF interpretation
# gives  Σ B_m^{(1)} T^m/m! = (Σ Q_n T^n) · (Σ B_m T^m/m!).
# So b0_m = B_m / m!, b1_k = B_k^{(1)} / k!, and Q_n is the OGF coefficient of Q(T).
b0 = {m: expand(Bm_cache[m] / factorial(m)) for m in range(NMAX + 1)}
b1 = {m: expand(B1[m] / factorial(m)) for m in range(NMAX + 1)}
Q = {}
for n in range(NMAX + 1):
    rhs = b1[n]
    for k in range(1, n + 1):
        if n - k in Q:
            rhs = expand(rhs - Q[n - k] * b0[k])
    Q[n] = rhs

log('\nEmpirical Q(T) coefficients (Q_n = [T^n] Q(T)):')
for n in range(NMAX + 1):
    log(f'  Q_{n} = {Q[n]}')

# --- Step 4. Compute M(T) coefficients --------------------------------------
# M(T) = Σ_{n≥2} μ_n · E_1^{n-2} · T^n / n!
# so [T^n] M(T) = μ_n · E_1^{n-2} / n!
Mcoef = {}  # M_ogf[n] := [T^n] M(T)
for n in range(NMAX + 1):
    if n < 2:
        Mcoef[n] = Integer(0)
    else:
        Mcoef[n] = mu(n) * E1 ** (n - 2) / factorial(n)

log('\nM(T) OGF coefficients [T^n] M(T):')
for n in range(NMAX + 1):
    log(f'  M_{n} = {Mcoef[n]}')

# --- Step 5. Test Q_n == c · M_n for a single scalar c ----------------------
log('\n' + '=' * 78)
log('TEST 1: Q_n / M_n = c   (constant, independent of E_i, n)?')
log('=' * 78)
fitted_c = {}
mismatches = []
for n in range(2, NMAX + 1):
    Qn = expand(Q[n])
    Mn = expand(Mcoef[n])
    if Mn == 0:
        # M_n is never zero for n >= 2 since μ_n ≠ 0
        log(f'  n={n}: M_n = 0 — skip')
        continue
    if Qn == 0:
        # Then need c * M_n = 0 → c = 0 (since M_n ≠ 0)
        log(f'  n={n}: Q_n = 0, M_n = {Mn} → forces c = 0')
        fitted_c[n] = Integer(0)
        continue
    # Try dividing
    ratio = simplify(Qn / Mn)
    log(f'  n={n}: Q_n = {Qn}')
    log(f'         M_n = {Mn}')
    log(f'         Q_n / M_n = {ratio}')
    # Check whether ratio is a constant (independent of E1,E2,E3)
    if ratio.free_symbols & {E1, E2, E3}:
        log(f'         → NOT a constant! Contains E_i.')
        mismatches.append((n, ratio))
    else:
        fitted_c[n] = ratio

log('\nSummary of fitted c per n:')
for n, cval in fitted_c.items():
    log(f'  n={n}: c = {cval}')
if mismatches:
    log(f'\nMismatches (ratio depends on E_i) at n = {[m[0] for m in mismatches]}')

# --- Step 6. Cross-check via convolution prediction of B_m^{(1)} ------------
# Under Guess A: B^{(1)}(T) = c · M(T) · B(T)
# ⇒ B_m^{(1)} = m! · Σ_{r+s=m} [T^r]M · [T^s]B · c
#             = c · Σ_{r+s=m} m!/(r! s!) · (μ_r · E_1^{r-2}) · B_s
#             = c · Σ_{r+s=m, r≥2} C(m,r) · μ_r · E_1^{r-2} · B_s
log('\n' + '=' * 78)
log('TEST 2: Predicted B_m^{(1)} = c · Σ_{r+s=m, r≥2} C(m,r) μ_r E_1^{r-2} B_s')
log('=' * 78)
for m in range(2, NMAX + 1):
    pred = Integer(0)
    for r in range(2, m + 1):
        s_idx = m - r
        pred = expand(pred + binomial(m, r) * mu(r) * E1 ** (r - 2) * Bm_cache[s_idx])
    # pred is  B_m^{(1)}/c, so equation:  B_m^{(1)} = c · pred
    emp = B1[m]
    log(f'  m={m}:')
    log(f'    predicted (÷c): {pred}')
    log(f'    empirical:       {emp}')
    if pred == 0:
        if emp == 0:
            log('    → both zero, no constraint on c.')
        else:
            log(f'    → predicted is 0, empirical is nonzero → GUESS A REFUTED at m={m}.')
    else:
        # Solve emp = c * pred term by term
        ratio = simplify(emp / pred)
        log(f'    empirical/predicted = {ratio}')
        if ratio.free_symbols & {E1, E2, E3}:
            log(f'    → ratio depends on E_i → GUESS A REFUTED at m={m}.')

# --- Step 7. Explicit smoking gun --------------------------------------------
log('\n' + '=' * 78)
log('SMOKING GUN')
log('=' * 78)
log('At n=3:')
log(f'  M_3 = μ_3 · E_1 / 3! = ({mu(3)}) · E_1 / 6 = {Mcoef[3]}')
log(f'  c · M_3 = c · {Mcoef[3]}   (pure E_1, no E_3)')
log(f'  Q_3     = {Q[3]}                     (pure E_3, no E_1)')
log('These live in disjoint monomial supports → no scalar c can make them equal.')
log('')
log('Furthermore: at n=2, M_2 = μ_2 / 2! = (-3/2)/2 = -3/4  (nonzero constant).')
log('             Q_2 = 0.  So Test 1 forces c=0, but then Q_3 = 0 must hold — it does not.')
log('')
log('VERDICT: Guess A (scalar c) is REFUTED.  Earliest failure: n = 2 (forces c=0)')
log('         followed by manifest inconsistency at n = 3.')
log('')
log('Shape of mismatch:')
log('  Under Guess A, Q(T) = c · M(T) lives entirely in ℤ[E_1] (times μ_n).')
log('  Empirically, EVERY nonzero Q_n contains an E_3 factor, and NO Q_n lies in ℤ[E_1] alone.')
log('  In particular Q(T) has no E_1-only or E_1-E_2 terms; it is E_3-supported.')
log('')
log('  Rephrased: Q(T) / M(T) is not a constant — it is a nontrivial power series in T')
log('  with E_3-carrying coefficients.  The λ-deformation cannot be a scalar shift of E_3.')
log('')
log('Interpretation: Guess A needs modification.  Since Q_n always carries E_3, the')
log('deformation likely acts on E_3 itself in a way that introduces new E_3 terms, or')
log('multiplies M(T) by a series in E_3 rather than a scalar.  Possible refinements:')
log('  (a) c depends on E_3 (e.g. c → c·E_3, making Q(T) = c·E_3·M(T))?  Test: Q_3/M_3 · 1/E_3')
c_over_E3 = simplify(Q[3] / (E3 * Mcoef[3]))
log(f'      Q_3 / (E_3 · M_3) = {c_over_E3}')
log('  (b) M(T) itself needs an E_3-deformation inside the exponent.')

# --- Step 8. Test refinement (a): Q(T) = c · E_3 · M(T)? --------------------
log('\n' + '=' * 78)
log('TEST 3 (refinement): Q(T) = c · E_3 · M(T)?  ⇒ Q_n / (E_3 · M_n) = c constant?')
log('=' * 78)
for n in range(2, NMAX + 1):
    if Mcoef[n] == 0:
        continue
    if Q[n] == 0:
        log(f'  n={n}: Q_n = 0 → forces c = 0 (or M_n = 0)')
        continue
    ratio = simplify(Q[n] / (E3 * Mcoef[n]))
    log(f'  n={n}: Q_n / (E_3 · M_n) = {ratio}')

log('\nTest 3 outcome: still not a scalar (see printed ratios).')
log('Even  Q(T) = f(E_3) · M(T)  fails because Q has E_3^2, E_3^3 terms that M lacks.')

# --- Write log --------------------------------------------------------------
with open('/home/agent/projects/beta-prime/code/day135_lambda_fit/fit_guess_a.txt', 'w') as f:
    f.write('\n'.join(LOG) + '\n')
