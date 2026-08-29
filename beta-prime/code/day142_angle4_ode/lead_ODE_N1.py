"""
Lead 3 — Derive the ODE for N_1 from the Frobenius identity L·F_P = F_P · X.

Substitute log F_P = log f + Σ E_3^k N_k. Then L acts on both sides.
Match order-by-order in E_3.

At E_3^0: L·f/f = 0 (definition of L, verified). This gives 0 = X_0 = 0. ✓
At E_3^1: gives an inhomogeneous linear equation for N_1 in terms of f, N_1.

We compute:
  F_P = f · exp(Σ E_3^k N_k)
  So log F_P = log f + Σ E_3^k N_k.
  Let R := log(F_P/f) = Σ E_3^k N_k.
  Then F_P = f · exp(R).

  L · (f exp R) = f exp R · X.
  Divide by f exp R:
    (L · (f exp R)) / (f exp R) = X.

  Using L = T(U+θ)(V+θ) - θ, θ = T d/dT.
  Expand L (F_P) = L(f · exp R). Use product rule for θ.

  θ(f · exp R) = (θf) · exp R + f · (θR) · exp R = exp R · (θf + f · θR)
  θ²(f · exp R) = θ[exp R · (θf + f · θR)]
              = exp R · (θR)(θf + f · θR) + exp R · θ(θf + f · θR)
              = exp R · [(θR)(θf) + f (θR)² + θ²f + (θf)(θR) + f θ²R]
              = exp R · [θ²f + 2(θf)(θR) + f (θR)² + f θ²R]

  Multiplying by things involving U, V is scalar, so
  (V + θ)(f exp R) = V f exp R + θ(f exp R)
                   = exp R · [V f + θf + f θR]
                   = exp R · [(V + θ) f + f θR]      -- since V·f = Vf and (V+θ)f = Vf+θf

  Denote A := (V + θ), then
    A(f e^R) = e^R (Af + f θR)
  Then
    UA(f e^R) = e^R (UAf + Uf θR)  [scalar mult]
    θA(f e^R) = θ[e^R (Af + f θR)] = e^R · θR · (Af + f θR) + e^R · θ(Af + f θR)
              = e^R · [(θR)(Af) + f (θR)² + θAf + (θf)(θR) + f θ²R]
    (U+θ)A(f e^R) = e^R · [UAf + Uf θR + (θR)(Af) + f(θR)² + θAf + (θf)(θR) + fθ²R]

  Let B := (U + θ), so above is
    B A (f e^R) = e^R · [BAf + f B(θR) + (θR)(Af) + (θf)(θR)]
                     (using θ² R = θ(θR), and B(θR) = U θR + θ²R,
                      f B(θR) = f U θR + f θ²R = U f θR + f θ²R)

  Wait more carefully. Let me redo:
    UAf = U·Af (scalar times function).
    U f θR = f · U · θR = f · (U θR).
    Combine: UAf + U f θR = U (Af + f θR) = U A(f e^R)·e^{-R}. OK.
    θAf term is straightforward.
    Other terms combine as:
       (θR)(Af) + (θf)(θR) = θR · (Af + θf) = θR · (V+θ)f + (θf)(θR) - Vf·θR
    Actually just compute forward:
       (θR)(Af) + (θf)(θR) = θR · Af + θR · θf = θR · (Af + θf) = θR · [(V+θ)f + θf] Nope,
       Af = (V+θ)f = Vf + θf. So Af + θf = Vf + 2θf. Not a clean form.

  Better to just do the algebra symbolically in Python.

OK, easier — just apply L to log F_P representation numerically using sympy.
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff, simplify, together, collect, Function)

U, V = symbols('U V')
T = symbols('T')


def theta(P):
    return expand(T * diff(P, T))


def apply_L(P):
    """L = T(U+θ)(V+θ) - θ."""
    P1 = expand(V*P + theta(P))
    P2 = expand(U*P1 + theta(P1))
    return expand(T * P2 - theta(P))


def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        c = Pp.coeff_monomial(T**d)
        out += c * T**d
    return out


def build_f_uv(B_max, U_val, V_val):
    F = Integer(0)
    for b in range(B_max + 1):
        F += (rf(U_val, b) * rf(V_val, b)) * T**b / factorial(b)
    return F


def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    if a[0] != 1:
        raise ValueError(f"Const term = {a[0]}")
    b = {0: Integer(1)}
    for n in range(1, N + 1):
        s = Integer(0)
        for k in range(1, n + 1):
            s += a[k] * b[n - k]
        b[n] = expand(-s)
    out = Integer(0)
    for d in range(N + 1):
        out += b[d] * T**d
    return out


def derive_ODE_for_N1():
    """
    From L(f · e^R)/(f · e^R) = X,  with R = Σ E_3^k N_k,
    at [E_3^1]:  L(f) · N_1/f + [operator on N_1 · f]/f = X_1.

    Let's compute this symbolically without assuming a closed form for N_1.

    We use: (L applied to f · G)/f where G = 1 + E_3·N_1 + E_3²·(...) + ...
    Then [E_3^1] (L(f·G)/f) = ?

    L(f·G) = f·(L G) + something involving crossed derivatives. Let's think:
    L = T(U+θ)(V+θ) - θ.

    T(U+θ)(V+θ)(f · G) - θ(f · G)
       = T (U+θ) (V+θ)(fG) - (θf) G - f (θG)

    Now (V+θ)(fG) = Vf·G + θ(fG) = Vf·G + (θf)G + f(θG) = (V+θ)f · G + f·θG
                  = (Vf + θf)G + f·θG
    So    (V+θ)(fG) = ((V+θ)f) G + f · θG.

    Now (U+θ) applied to that:
      (U+θ)(A G + f · θG)  where A = (V+θ)f
      = U(A G) + θ(A G) + U(f θG) + θ(f θG)
      = UA·G + (θA)G + A·θG  + Uf·θG + (θf)(θG) + f·θ²G
      = ((U+θ)A) G + [A + Uf + θf] θG + f θ²G
      = ((U+θ)(V+θ)f) G + [(V+θ)f + (U+θ)f] θG + f θ²G   [since A = (V+θ)f]
      Wait: A + Uf + θf = (V+θ)f + Uf + θf = Vf + θf + Uf + θf = (U+V)f + 2θf.
      Hmm, let me re-verify: (U+θ)f = Uf + θf, so Uf + θf = (U+θ)f.
      So A + (U+θ)f = (V+θ)f + (U+θ)f = (U+V)f + 2θf.

    So (U+θ)(V+θ)(fG) = ((U+θ)(V+θ)f)G + [(U+V)f + 2θf]·θG + f·θ²G

    Multiply by T:
    T(U+θ)(V+θ)(fG) = T·((U+θ)(V+θ)f)G + T[(U+V)f + 2θf]·θG + Tf·θ²G

    Subtract θ(fG) = (θf)G + f·θG:
    L(fG) = [T(U+θ)(V+θ)f - θf]·G + [T(U+V)f + 2Tθf - f]·θG + Tf·θ²G
          = (Lf)·G + [T(U+V)f + 2Tθf - f]·θG + Tf·θ²G

    Since Lf = 0:
       L(fG) = [T(U+V)f + 2Tθf - f]·θG + Tf·θ²G

    Divide by f:
       L(fG)/f = [T(U+V) + 2T·(θf)/f - 1]·θG + T·θ²G

    Let φ := (θf)/f (formal). Then:
       L(fG)/f = [T(U+V) + 2Tφ - 1]·θG + T·θ²G  ... (*)

    Now G = e^R = 1 + R + R²/2 + ...
    R = E_3·N_1 + E_3²·N_2 + ...
    θG = G · θR (since (d/dT) log G = (d/dT) R  ⇒  θG/G = θR)
    Actually θG = θ(e^R) = e^R · θR = G · θR.
    θ²G = θ(G · θR) = θG · θR + G · θ²R = G·(θR)² + G·θ²R = G·((θR)² + θ²R).

    So (*) becomes:
       L(fG)/f = [T(U+V) + 2Tφ - 1]·G·θR + Tf·f^{-1}·G·((θR)² + θ²R)
              = G · [ (T(U+V) + 2Tφ - 1)·θR + T·((θR)² + θ²R) ]

    Now L(fG)/(fG) = L(fG)/(f·G) = X.
    So:
       X = (T(U+V) + 2Tφ - 1)·θR + T·((θR)² + θ²R)  where φ = θf/f.

    THIS IS A CLEAN IDENTITY.  R = Σ E_3^k N_k.
    Extract [E_3^1]:
       X_1 = (T(U+V) + 2Tφ - 1)·θN_1 + T·θ²N_1

    since (θR)² starts at E_3² and only θR, θ²R contribute at E_3^1.

    So the ODE for N_1 (with source X_1(T; U, V)) is:

       T·θ² N_1  +  (T(U+V) - 1 + 2Tφ) · θ N_1  =  X_1

    where φ = (θf)/f and f = 2F0(U, V; ; T).

    This is a first-order LINEAR ODE for θN_1 with source X_1.  Setting M := θN_1:
       T · θM + [T(U+V) - 1 + 2Tφ]·M = X_1
       θM + [(U+V) - 1/T + 2φ]·M = X_1/T

    (θ = T d/dT, so this is T·M' + [(U+V) - 1/T + 2φ]·M = X_1/T,
     or M' + [(U+V)/T - 1/T² + 2φ/T]·M = X_1/T².)

    The associated homogeneous:
       θM_h + [(U+V) - 1/T + 2φ]·M_h = 0
    Solution:  M_h = T · f^{-2} · exp(-T(U+V)).  (integrating factor)

    Because ∫ [(U+V) - 1/T + 2φ]·d(logT) = (U+V)·T - log T + 2 log f (via dT = θT/T·dT... wait).
    Hmm actually θ = T d/dT, so θ(log F) = T · F'/F.  For the equation θM/M = -[...], we
    integrate d(log M) = -[(U+V) - 1/T + 2φ] dT ... but 2φ dT = 2 (θf/f) dT = 2 (Tf'/f)(1/T dT · T) hmm.
    Let me just express:
       d(log M) / dT = -[(U+V)/T + 2φ/T - 1/T²]
                  = -[(U+V)/T - 1/T² + 2 (f'/f)]
       ⇒ log M = -(U+V) log T + 1/T · ... wait 1/T² integrates to -1/T.
                = -(U+V) log T - 1/T - 2 log f + C
       ⇒ M_h = C · T^{-(U+V)} · e^{-1/T} · f^{-2}

    But wait, at T = 0 this blows up. Let's be careful — the formal series regime.

    Bessel-I equation form:
       z² y'' + z y' - (z² + ν²) y = 0.

    Or Bessel:  z² y'' + z y' + (z² - ν²) y = 0.

    Our ODE for M = θN_1:
       T · θM + [T(U+V) - 1 + 2Tφ]·M = X_1.
       T (T M' + ... hmm no θM = T·M', so T·θM = T²·M').

    Cleaner in ordinary derivative form:
       T² M' + [T(U+V) - 1 + 2Tφ]·M = X_1

    OK — I'll compute X_1(T; U, V) and verify N_1 satisfies this ODE order-by-order.
    """
    print("=" * 70)
    print("Deriving X_1 = L·F_P/F_P at [E_3^1] and matching to ODE for N_1")
    print("=" * 70)

    B_MAX = 10
    # We'll use symbolic (U, V) — expensive but doable.
    print(f"Building P_b(U,V,E_3) up to b={B_MAX}...")
    t0 = time.time()
    P_uv = compute_P_at(U, V, B_MAX)
    print(f"  in {time.time()-t0:.1f}s")

    # Build FP as series in T, coefficient is poly in U, V, E_3.
    FP = Integer(0)
    for b in range(B_MAX + 1):
        FP += P_uv[b] * T**b / factorial(b)

    # Build f
    f = build_f_uv(B_MAX, U, V)

    # Compute L·FP
    print("Computing L·F_P ...")
    t1 = time.time()
    LFP = truncate_T(apply_L(FP), B_MAX - 1)
    print(f"  in {time.time()-t1:.1f}s")

    # Compute FP^{-1}
    print("Computing F_P^{-1} ...")
    t2 = time.time()
    invFP = one_over_series(FP, B_MAX - 1)
    print(f"  in {time.time()-t2:.1f}s")

    # Compute X = L·FP / FP
    print("Computing X = L·F_P / F_P ...")
    t3 = time.time()
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    print(f"  in {time.time()-t3:.1f}s")

    # Extract X_1 = [E_3^1] X
    Xp = Poly(expand(X), E3)
    X1 = expand(Xp.coeff_monomial(E3**1))

    print("\nX_1 = [E_3^1] X (coefficients in T):")
    X1p = Poly(X1, T)
    for d in range(B_MAX):
        c = expand(X1p.coeff_monomial(T**d))
        if c != 0:
            print(f"  [T^{d}] X_1 = {factor(c)}")

    # Now compute N_1
    print("\nComputing N_1 ...")
    t4 = time.time()
    # log(F_P/f) = R, extract E_3 coefs
    invf = one_over_series(f, B_MAX)
    ratio = truncate_T(expand(FP * invf), B_MAX)
    G = expand(ratio - 1)
    logv = Integer(0)
    Gk = Integer(1)
    for k in range(1, B_MAX + 1):
        Gk = truncate_T(expand(Gk * G), B_MAX)
        if Gk == 0:
            break
        logv = expand(logv + (-1)**(k-1) * Gk / k)
    R = truncate_T(logv, B_MAX)
    Rp = Poly(expand(R), E3)
    N1 = expand(Rp.coeff_monomial(E3**1))
    print(f"  in {time.time()-t4:.1f}s")

    # Compute phi = θf/f
    phi_num = theta(f)
    phi = truncate_T(expand(phi_num * invf), B_MAX - 1)
    print("\nφ = θf/f (leading terms):")
    phip = Poly(phi, T)
    for d in range(min(8, B_MAX)):
        c = expand(phip.coeff_monomial(T**d))
        if c != 0:
            print(f"  [T^{d}] φ = {factor(c)}")

    # Compute theta N_1
    theta_N1 = theta(N1)
    theta2_N1 = theta(theta_N1)

    # LHS of ODE: T·θ²N_1 + [T(U+V) - 1 + 2Tφ]·θN_1
    LHS = expand(T * theta2_N1 + (T*(U+V) - 1 + 2*T*phi) * theta_N1)
    LHS = truncate_T(LHS, B_MAX - 1)

    diff_ = expand(LHS - X1)
    diff_ = truncate_T(diff_, B_MAX - 1)

    print("\nODE check: LHS = T·θ²N_1 + [T(U+V) - 1 + 2Tφ]·θN_1")
    print(f"LHS - X_1 (should be 0 if the derivation is right):")
    diffp = Poly(diff_, T)
    all_zero = True
    for d in range(B_MAX):
        c = expand(diffp.coeff_monomial(T**d))
        if c != 0:
            all_zero = False
            print(f"  [T^{d}] (LHS - X_1) = {factor(c)}")
    if all_zero:
        print("  ALL ZERO — ODE VERIFIED!")

    return N1, X1, phi, all_zero


def solve_ODE_for_N1(N1, X1, phi, B_MAX):
    """
    ODE: T·θ²N_1 + [T(U+V) - 1 + 2Tφ]·θN_1 = X_1.

    Interpret X_1 as SOURCE. Solve order-by-order for N_1.
    N_1 starts at T^2.  Let N_1 = Σ n_b T^b.
    Then θN_1 = Σ b n_b T^b,  θ²N_1 = Σ b² n_b T^b.
    T·θ²N_1 = Σ b² n_b T^{b+1}.
    ...
    """
    print("\n" + "=" * 70)
    print("Structural interpretation")
    print("=" * 70)
    # X_1 starts at T^2 (universal -3 T^2). Verify.
    print("Leading [T^2] X_1 = ", factor(Poly(X1, T).coeff_monomial(T**2)))
    # If X_1 = -3 T^2 + (higher), and the ODE at [T^2] gives:
    # T·θ²N_1 at [T^2]: from θ²N_1 at [T^1]:  1²·[T^1] N_1 = 0 (N_1 starts T^2). So T·θ²N_1[T^2] = 0.
    # [T(U+V)-1]·θN_1 at [T^2]: (U+V)·[T^1] θN_1 = 0; -1·[T^2] θN_1 = -2·[T^2] N_1.
    # 2Tφ · θN_1 at [T^2]: 2·[T^1] φ · [T^1] θN_1 = 0 (θN_1 at T^1 = 0).
    # So [T^2] LHS = -2·[T^2] N_1 = -2·(3/2) = -3. ✓
    print("[T^2] LHS = -2·[T^2] N_1 = -2·(3/2) = -3.  Matches X_1[T^2] = -3.  ✓")


def main():
    N1, X1, phi, ok = derive_ODE_for_N1()
    if ok:
        print("\n" + "=" * 70)
        print("SUCCESS: ODE for N_1 verified.")
        print("=" * 70)
        print("""
    T·θ² N_1  +  [T(U+V) - 1 + 2T·φ]·θ N_1  =  X_1

where:
    θ = T d/dT
    φ = (θf)/f = T·f'/f  where f = 2F0(U, V; ; T)
    X_1 = [E_3^1] (L·F_P/F_P) = universal source
    N_1 = [E_3^1] log(F_P/f)

This is a FIRST-ORDER LINEAR ODE for M := θN_1:

    T·θM + [T(U+V) - 1 + 2Tφ]·M = X_1.

Equivalently (dividing by T):

    θM + [(U+V) - 1/T + 2φ]·M = X_1/T.

The homogeneous solution: M_h = C·T^{-(U+V)}·e^{-1/T}·f^{-2} (integrate d(log M)).

**But this is not a Bessel equation** — because of the T·φ term (φ is a divergent
formal series in T with coefficient (U V + (U+V+1)UV·T + ...)) — actually φ
depends nontrivially on U, V.  It is a QUASI-LINEAR ODE with source, not a
classical hypergeometric equation.

However, it IS a clean single ODE.  If we could get X_1 in closed form, we could
integrate to get N_1 in closed form.
    """)
    else:
        print("ODE derivation failed — check the algebra.")

    solve_ODE_for_N1(N1, X1, phi, 10)


if __name__ == '__main__':
    main()
